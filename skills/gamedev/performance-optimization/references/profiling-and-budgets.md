> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/disciplines/performance-optimization/references/profiling-and-budgets.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 性能剖析与预算

适用 Godot 4.7、Unity 6.3 LTS 与 Unreal 5.8。

目录：
1. CPU 与 GPU 分诊
2. 各引擎剖析器快速上手（Godot、Unity、Unreal、外部工具）
3. 对象池管理器
4. 合批与实例化规则
5. 内存分配与 GC 指南
6. 少做技术
7. 资产预算与移动端发热

## 1. CPU 与 GPU 分诊（先判断，再动手）

```text
1. Read total frame time vs your budget (16.67 ms @60).
2. Compare CPU-frame time and GPU-frame time:
     GPU >> CPU  → GPU-bound  → overdraw, shader cost, resolution, lights/shadows.
     CPU >> GPU  → CPU-bound  → inspect main AND render threads: scripts, physics, pathfinding,
                                allocations/GC, draw submission and render-state changes.
     Both high / alternating → find the per-frame spike in the timeline (one function/system).
3. Within the bound side, sort costs descending and attack the top one only.
4. Re-measure. If it didn't move the frame time, you fixed the wrong thing — revert and re-triage.
```

优化实测出的瓶颈。当 draw 提交是帧的限制因素时，减少 draw call（绘制调用）或状态切换能降低 CPU 渲染开销，即使 GPU 尚有余量。合批与实例化自身也有开销，所以改动前后要对比主线程、渲染线程和 GPU 耗时。只有脚本更快，通常救不了被 GPU 工作量限制的帧。

## 2. 各引擎剖析器快速上手

**Godot 4.7**
- 编辑器：**Debugger ▸ Profiler**（逐函数的脚本 + 物理耗时、帧时间）、**Debugger ▸ Visual Profiler**（渲染占用的 CPU 和 GPU 时间；Profiler 标签页不显示 GPU 开销），以及 **Monitors** 标签页（FPS、draw call 数、显存/静态内存、对象/节点计数）。
- 代码：`Performance.get_monitor(Performance.TIME_PROCESS)`（最近一秒里最慢的一帧 process，单位是**秒**，每秒刷新一次）、`Performance.TIME_PHYSICS_PROCESS`、`Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME`、`Performance.RENDER_TOTAL_PRIMITIVES_IN_FRAME`、`Performance.MEMORY_STATIC`，以及 `PIPELINE_COMPILATIONS_*` 监视器（4.4+，排查 shader 卡顿）：Surface 或 Draw 计数在加载画面之外跳升，就是首次游玩卡顿。
- 可视化调试：3D 视口的 **View Information / View Frame Time** 覆盖层。
- 原生代码追踪：用 `scons profiler=tracy`（或 `perfetto`、`instruments`）从源码编译引擎，引擎 zone 会流式输出到对应的剖析器。

**Unity 6.3 LTS**
- **Profiler** 窗口：CPU Usage、GPU Usage、Rendering、Memory 各模块。**Deep Profile** 节制使用（开销大，且会扭曲数据）。
- 用 **Frame Debugger** 逐步查看 draw call，找出破坏合批的原因（SetPass calls、batches）。
- 代码：把 `ProfilerRecorder` 挂在内置计数器 `"CPU Main Thread Frame Time"`、`"GPU Frame Time"`（release 版需启用 **Frame Timing Stats**）和 `"GC Allocated In Frame"`（仅 development 版）上，做包内 HUD/CSV；CPU/GPU 帧时间用 `FrameTimingManager`。
- **在真机上剖析 Development 构建**（`Autoconnect Profiler`），别只看编辑器。
- **Project Auditor**（`com.unity.project-auditor` 包）在剖析前静态标记高开销的代码与设置。

**Unreal 5.8**
- 控制台：`stat unit`（Frame / Game / Draw / RHIT / GPU 毫秒；Game 是游戏线程，Draw 是渲染线程，两者都是 CPU）、`stat fps`、`stat scenerendering`（draw call 数、图元数）、`stat game`、`stat gpu`、`stat hitches`（记录超过 `t.HitchFrameTimeThreshold` 的帧）。
- 完整时间线追踪用 **Unreal Insights**；GPU 耗时分解用 `ProfileGPU`（Ctrl+Shift+,）。

**外部工具（跨引擎通用）**
- **RenderDoc**：对 Vulkan、D3D11/12 和 OpenGL/ES 做 GPU 帧捕获，覆盖 Windows、Linux 和 Android；不支持 Metal。Apple 平台用 Xcode Metal debugger 和 Instruments；Windows 的 D3D12 用 PIX。
- **Tracy**：面向原生代码的插桩式 CPU/GPU 时间线；客户端库与查看器要用同一个 release，因为网络协议可能变动。

## 3. 对象池管理器（通用）

```text
class Pool<T>:
    free: list
    create_fn, reset_fn
    prewarm(n):  for n → free.push(create_fn())          # allocate up front, off the hot path
    acquire():   t = free.pop() or create_fn(); activate(t); return t
    release(t):  reset_fn(t); deactivate(t); free.push(t)  # never destroy; recycle
```

凡是频繁生成、存活很短的对象都进池：子弹、弹壳、粒子、伤害数字、一波波刷出的敌人、一次性音效。加载时预热，避免首次使用卡顿。给池设上限，并定好溢出策略（扩容，或回收最旧的）。

## 4. 合批与实例化规则

- **什么会拆散一批：**对象之间材质、纹理或渲染状态不同。共享材质、把纹理打成**图集（atlas）**，让一串对象合并成一次 draw call 提交。
- **网格相同、实例很多** → GPU instancing：Unity（在材质上勾选 *GPU Instancing*；但 URP/HDRP 下，SRP Batcher 兼容的 shader 会改由 SRP Batcher 绘制；数量很大时启用 **GPU Resident Drawer**，它需要 Forward+ 路径，以及一个支持 compute 的图形 API（OpenGL ES 除外））/ Godot `MultiMesh` + `MultiMeshInstance2D/3D` / Unreal Instanced Static Mesh 或 Hierarchical ISM。
- **静态几何体** → static batching（Unity 里标记 static）；能烘焙就烘焙。Unity 的 dynamic batching 在低端设备之外已不推荐：它的 CPU 开销可能超过省下的 draw call。
- **2D** → 纹理图集 + 共享材质来合批 sprite；避免每个 sprite 单独材质。
- **UI** → 尽量减少 canvas 重建（Unity：把静态/动态 canvas 拆分）；单个元素变化不该弄脏整个 canvas。
- **灯光/阴影** → 静态光照烘焙；限制实时阴影投射者数量；剔除过小的阴影。

## 5. 内存分配 / GC 指南

- **C# (Unity)：**每帧不 `new`、`Update` 里不用 LINQ、避免装箱（如把 `enum` 当字典键）、物理查询用 `NonAlloc` 版本、复用 `List`/数组（用 `Clear()` 而非重新分配）、小而热的数据用 struct、缓存 `GetComponent`/`Find` 的结果。目标是稳态下**每帧 0 B GC.Alloc**。
- **GDScript (Godot)：**别在每次 `_process` 里新建 `Array`/`Dictionary`；要复用；优先用类型化数组；属于 timer/signal 的重活不要放进 `_process`。
- **通用：**字符串是典型的隐性分配来源（拼接、格式化），少构造，缓存结果。

## 6. 少做技术（算法层面的收益）

- **降低执行频率：**AI/HUD/高开销检查放到 timer 上或每 N 帧更新一次，不要每帧都跑；跨帧错开（time-slicing）。
- **空间划分：**grid/quadtree/octree，让查询只碰到附近对象，而不是全部 N 个。
- **LOD 与剔除：**远处降低细节；视锥/遮挡剔除；屏幕外的远处实体直接回收。
- **缓存结果：**寻路、视线、派生数据做记忆化；数据一变就失效。
- **延迟/分摊：**把程序化生成和加载摊到多帧，避免尖峰。

## 7. 资产预算（从源头防回归）

| 资产 | 桌面端典型预算 | 移动端预算 | 备注 |
|-------|------------------------|---------------|-------|
| 纹理最大尺寸 | 2048–4096 | 1024–2048 | 用 mipmaps；压缩（BCn / ASTC） |
| 角色三角面数 | 30k–80k | 5k–20k | 远处用 LOD |
| draw call 数/帧 | 小几千 | 几百 | 移动端最要紧的指标 |
| 实时灯光 | 少量几个 | 1–2 + 烘焙 | 其余烘焙 |
| 音频 | 音乐流式播放，短音效驻留内存 | 同上 | 不要加载时全部解压 |

移动端还多出**热节流（thermal throttling）**问题：前两分钟能跑 60 FPS、随后就掉帧的游戏，是在发热。留足余量，锁住帧率，降低持续 GPU 负载。Agent 感受不到设备发热，所以要请用户在目标手机上玩 15 分钟，报告第一分钟和最后一分钟的帧时间（或 FPS 计数）。
