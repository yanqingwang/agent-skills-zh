---
name: performance-optimization
description: >
  通过实测定位并修复 Godot、Unity、Unreal 或 Roblox 中的游戏帧率问题：先判断是 CPU
  受限还是 GPU 受限，再解决影响最大的一项（draw call、对象池、GC 尖峰）。适用于低 FPS、
  卡顿、首次使用时的卡顿，或优化与性能分析需求。不适用于构建体积（`unity-build-size`）、
  物理抖动（`physics-tuning`）或网络延迟（`roblox-networking`、`godot-multiplayer`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/disciplines/performance-optimization/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 性能优化

整个循环是：**设定预算、测量、找出唯一瓶颈、修复、再测量、报告数据。** 凭猜测通常针对错误的系统，因此在分析器或帧时间捕获指出时间花在哪里之前，做什么都不会有变化。本 Skill 讲的是跨引擎的方法以及反复出现的修复手段；各引擎的分析器在下文和参考文档中列出。

## 适用场景

- 帧率偏低或不稳，或未达到目标（桌面端 60 FPS，移动端 30 或 60）。
- 卡顿：首次出现的特效、游戏途中加载、周期性的 GC 停顿、大规模战斗。
- 决定优化什么、设定预算，或向 CI 加入性能检查。

**不适用本 Skill：** 物理稳定性（`physics-tuning`）、安装或下载体积（`unity-build-size`）、网络延迟（`roblox-networking`、`godot-multiplayer`）、着色器数学（`shader-programming`）。

## 核心工作流

1. **把问题变成一个数字。** 目标 FPS 决定预算：60 FPS 是 16.67 ms，30 是 33.3 ms，120 是 8.33 ms。找一个可复现的最差场景并保存下来（测试关卡、录制的操作、固定种子）。
2. **测量前先解除上限。** VSync 和帧率上限会掩盖余量：4 ms 的帧和 15 ms 的帧都显示 60 FPS。Godot 用 `--disable-vsync`（以及 `--max-fps 0`）；Unity 在桌面端设 `QualitySettings.vSyncCount = 0` 并配合 `Application.targetFrameRate = -1`；Unreal 用 `r.VSync 0` 和 `t.MaxFPS 0`。然后读取以 ms 为单位的帧时间，而不是 FPS。
3. **在目标硬件上分析接近发布版的构建。** 编辑器和调试构建会带来额外开销并跳过编译器优化；使用 Godot 的 release 导出、附加了分析器的 Unity Development 构建，或 Unreal 的 Development 或 Test 构建。
4. **把 CPU 与 GPU 分开。** 对比主线程、渲染线程和 GPU 的时间。与帧时间最接近的一方就是瓶颈；修另一方不会有任何变化。
5. **只修最大的那一处开销**，优先减少工作量（缓存、空间分区、降低执行频率），而不是打磨某条热点代码。然后套用下文中对应的修复。
6. **在同一台机器上对同一场景重新测量**，每次跑三轮，依据数据决定保留还是回退。
7. **设定预算**：按子系统和按资产分别设定，让修复成果保持住，并在引擎允许的地方把帧时间检查加入 CI。
8. **报告**场景、硬件、构建类型、修复前后（帧时间的平均值与 p95 或 p99）、瓶颈以及修复内容。说明哪些是在 headless 或编辑器中测得的，哪些仍需要用户的设备来验证。

## 模式

### 1. 帧预算拆分


```text
@60 FPS = 16.67 ms. The slower of CPU frame and GPU frame sets the frame rate.
Example sub-budgets: gameplay/scripts ~5 ms · physics ~3 ms · render submit ~4 ms · UI ~2 ms · slack.
Mobile: keep 20-30% headroom so the game survives thermal throttling.
```


### 2. 各引擎在哪里报告该拆分


```text
Godot 4.7     : Debugger > Profiler (script and physics), Visual Profiler (CPU vs GPU render time
                per pass), Monitors (FPS, draw calls, memory, pipeline compilations).
                Performance.get_monitor(TIME_PROCESS) is the worst frame of the last second in
                SECONDS, refreshed once a second; time frames yourself for per-frame spikes.
Unity 6.3 LTS : Profiler window + Frame Debugger. ProfilerRecorder on "CPU Main Thread Frame Time"
                and "GPU Frame Time" (release players need Frame Timing Stats in Player Settings).
Unreal 5.8    : stat unit (Frame / Game / Draw / RHIT / GPU), stat scenerendering (draw calls),
                Unreal Insights; `csvprofile frames=600` writes a CSV capture you can read.
Roblox        : MicroProfiler (Ctrl+F6 in Studio and the desktop client; mobile via its web UI).
# Game and Draw are CPU threads; GPU is the graphics card. Whichever is nearest Frame wins.
```


**Roblox：** 在中端手机上做性能分析，因为桌面端的帧率上限会掩盖问题。借助 Studio Assistant，Roblox 内置的 `rbx-perf-profiling`（读取 MicroProfiler 捕获）和 `rbx-scene-analysis`（渲染开销、内存、泄漏的实例）能给出真实数据；用 `roblox-studio-workflow` 在 Studio 里运行检查，用 `roblox-physics` 查看装配体和模拟开销，当 "lag" 指网络延迟而非帧时间时用 `roblox-networking`。

### 3. Headless CPU 帧时间检查（Godot）


```gdscript
# tools/frame_stats.gd: CPU frame time of one scene, headless (no GPU work is measured).
# godot --headless --path . --script res://tools/frame_stats.gd -- res://levels/worst.tscn 600 16.6
extends SceneTree

func _initialize() -> void:
    var args := OS.get_cmdline_user_args()
    var scene_path := args[0] if args.size() > 0 else "res://main.tscn"
    var frames := int(args[1]) if args.size() > 1 else 600
    var budget_ms := float(args[2]) if args.size() > 2 else 16.6
    OS.low_processor_usage_mode_sleep_usec = 0          # headless otherwise sleeps ~6.9 ms a frame
    root.add_child(load(scene_path).instantiate())
    for i in 60:                                       # skip loading and first-use spikes
        await process_frame
    var ms := PackedFloat64Array()
    var last := Time.get_ticks_usec()
    for i in frames:
        await process_frame
        var now := Time.get_ticks_usec()
        ms.append((now - last) / 1000.0)               # whole frame: scripts, physics, engine
        last = now
    ms.sort()
    var avg := 0.0
    for v in ms:
        avg += v / ms.size()
    var p95 := ms[int(ms.size() * 0.95)]
    var p99 := ms[int(ms.size() * 0.99)]
    var over := ms.size() - ms.bsearch(budget_ms, false)
    print("FRAME avg=%.2fms p95=%.2fms p99=%.2fms max=%.2fms over_budget=%d/%d"
            % [avg, p95, p99, ms[-1], over, ms.size()])
    quit(1 if p95 > budget_ms else 0)
```


当 p95 超过预算时它会以 1 退出，因此可以用来在 CI 中卡住脚本和物理开销。Headless 模式没有渲染器，无法反映 GPU 时间或 draw call；要看这些，请用户用 `--disable-vsync --print-fps` 运行游戏，或打开 Visual Profiler 并报告同一场景的 CPU 与 GPU 毫秒数。共享或繁忙的机器会引入噪声，所以对比要在同一台机器上进行。

### 4. 对象池（停止在热循环里分配和释放）


```gdscript
var _pool: Array[Node2D] = []                     # Node3D for 3D; both have `visible`
func acquire() -> Node2D:
    var n: Node2D = _pool.pop_back() if not _pool.is_empty() else bullet_scene.instantiate()
    n.set_process(true); n.visible = true
    return n
func release(n: Node2D) -> void:
    n.set_process(false); n.visible = false       # disable + hide; don't free
    _pool.append(n)
# Pre-warm at load. Also reset velocity, timers and signal connections on release.
```


### 5. 削减 draw call 和状态切换


```text
- Atlas textures and share materials so sprites and meshes batch.
- Identical meshes: GPU instancing (Unity; under URP/HDRP the SRP Batcher or GPU Resident Drawer
  takes over), MultiMesh/MultiMeshInstance (Godot), Instanced Static Mesh (Unreal).
- Static geometry: static batching or baking. Bake lighting that does not move.
- Overdraw: fewer large overlapping transparent and particle layers.
- Fill-rate bound: lower render resolution or scale (2x pixel ratio is 4x the pixels).
Measure draw calls and GPU ms before and after; both should drop.
```


### 6. 消除每帧分配（GC 尖峰就是周期性卡顿）


```csharp
// Unity 6.3 LTS. Steady state should be 0 B "GC Allocated In Frame".
void Update() {
    _hits = Physics.RaycastNonAlloc(ray, _hitBuffer);   // reuse a preallocated array
    for (int i = 0; i < _hits; i++) { /* ... */ }
}   // hit order is undefined and a full buffer may miss the nearest hit: size it, sort if needed
// No LINQ, string building or FindObjectsByType in Update. Cache references once.
// GDScript: reuse Arrays/Dictionaries instead of building new ones each _process.
```


## 易踩的坑

- **开着 VSync 测量。** 帧率会一直停在刷新率上，直到帧已经超出预算，于是修复看起来毫无效果。解除上限，再读 ms。
- **在 Godot 里每帧读取 `TIME_PROCESS`。** 它是过去一秒里最差的一帧，每秒更新一次，所以逐帧采样会重复同一个值。直接为帧计时。
- **着色器与管线编译卡顿**：特效、敌人或材质首次出现时发生，第二次运行常消失，因为驱动已缓存。Godot 4.4+：留意管线编译监视器，提前加载相关功能，并在场景中保留生成特效的隐藏实例。Unity 6：用 `GraphicsStateCollection`（实验性）追踪并预热 PSO，或在旧版 API 上预热着色器变体。Unreal：PSO 预缓存以及随包附带的 PSO 缓存。
- **手机上的热降频**：先维持两分钟 60 FPS，然后掉帧。请用户在设备上跑一次 15 分钟的会话，报告开头和结尾的帧时间；限制帧率并留出余量。
- **Unity 在 Android 和 iOS 上默认以 30 FPS 运行**（`targetFrameRate = -1`）。在把它当成性能问题之前，先显式设置 `Application.targetFrameRate`。
- **修错了方向。** 对 GPU 受限的帧做 CPU 微优化毫无作用，反之亦然。
- **在热循环里实例化和释放**会造成内存碎片和 GC 尖峰。改用对象池。
- **Unity 的 "Enable GPU Instancing" 不起作用**（在 URP/HDRP 下）：对兼容的着色器，SRP Batcher 优先。检查 Frame Debugger；对于大量相同网格，使用 GPU Resident Drawer（Forward+、支持 compute 的 API，不含 OpenGL ES）。
- **把 Deep Profile 或编辑器里的数字当作结果汇报。** 两者都会扭曲耗时；要引用构建版本的数据。
- **没有预算。** 缺少每个子系统的毫秒数和资产上限，性能会悄悄退化。
- **在原型还不好玩、也未测量之前就优化**，会加入可能被丢弃的复杂度。

## 参考

- `references/profiling-and-budgets.md`：当你需要各引擎分析器的操作指引、CPU 与 GPU 的分诊步骤、带预热和溢出策略的通用对象池、各引擎的批处理与实例化规则、C# 与 GDScript 的分配规则、少做工作的技巧（LOD、剔除、时间分片）或起始资产预算时阅读。

## 相关 Skill

- `physics-tuning`：固定步长的开销、休眠刚体、broadphase 层。
- `shader-programming`：特效的逐像素开销；`godot-shaders` 用于 Godot 着色器编译。
- `godot-export`、`unity-build-pipeline`、`unreal-packaging`：构建你应该拿来分析性能的发布版本。
- `procedural-gen`、`game-ai`：常见的 CPU 热点（生成、寻路），可延后或分片处理。

## 版本说明

最后验证：2026-11-11。

- Godot 4.7：`TIME_PROCESS` 和 `TIME_PHYSICS_PROCESS` 是在 `main/main.cpp` 中设定的每秒最大值；headless 每帧休眠 `low_processor_usage_mode_sleep_usec`（`core/os/os.cpp`）；CLI 参数 `--disable-vsync`、`--max-fps`、`--print-fps`。管线预编译及其监视器在 4.4 引入，shader baker 在 4.5 引入（https://docs.godotengine.org/en/stable/tutorials/performance/pipeline_compilations.html）。帧时间脚本在 4.7.2 headless 上运行过。
- Unity 6.3：`targetFrameRate` 的默认值以及移动端 30 FPS 的默认值（https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/application/targetframerate）；`GraphicsStateCollection` 为实验性（https://docs.unity.com/en-us/engine/6000.3/manual/materials-and-shaders/shaders/shader-troubleshooting/shader-reduce-stalling/shader-prevent-stutter/shader-pso-trace-warming/shader-pso-introduction）。
- Unreal：PSO 预缓存（https://dev.epicgames.com/documentation/unreal-engine/pso-precaching-for-unreal-engine）；`csvprofile`（https://docs.unrealengine.com/4.27/en-US/TestingAndOptimization/PerformanceAndProfiling/CSVProfiler）。
- Roblox：MicroProfiler 快捷方式和移动端 Web UI（https://create.roblox.com/docs/performance-optimization/microprofiler.md）；内置的 Assistant 技能 `rbx-perf-profiling` 和 `rbx-scene-analysis`（https://create.roblox.com/docs/assistant/skills.md）。
- RenderDoc 1.47（2026-10-31）、Tracy 0.15.0（2026-11-05）、Unity Project Auditor 包 3.2.0（2026-11-03）：来自 GitHub releases 和 Unity 包注册表。
