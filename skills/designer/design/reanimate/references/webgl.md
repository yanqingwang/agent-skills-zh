> **中文汉化版** · 上游：[NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate) · 原文件：`skills/designer/design/reanimate/references/webgl.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Canvas、WebGL 和 3D

canvas 只给你看像素，但生成这些像素的一切都经过了成百上千次 API 调用：着色器源码、uniform 值、draw call、纹理、场景图。`capture.ts --gl` 把这些调用记下来，`--clock virtual` 让这份记录逐帧可复现。两者合起来，就把一个 WebGL 场景变成了 CSS 动画给你的那种证据：有精确常量可抄、有曲线可拟合、有能判失败的对比。

## 抓取

```bash
bun <skill>/scripts/capture.ts --url https://example.com --out .reanimate/<name>/ref \
  --viewport 1440x900 --selector ".hero" --trigger move --target ".hero canvas" --path "0.5,0.5;0.2,0.3;0.8,0.7" \
  --duration 3000 --clock virtual --gl --assets
bun <skill>/scripts/gl.ts summary .reanimate/<name>/ref
```

| Flag | 作用 | 何时用 |
|---|---|---|
| `--clock virtual` | 页面跑在抓取器推进的时钟上：`performance.now`、`Date`、定时器、`requestAnimationFrame`（稳定 60 Hz，`--raf-hz`）、CSS / WAAPI 动画、`<video>`、`Event.timeStamp`。不论渲染花多久，每帧都精确在 t = k/fps 截图，网络和 worker 看起来是瞬时的，同一页面抓两次逐字节一致。 | 一律用，针对 canvas 和 WebGL。对任何 JS 驱动的动效也有帮助。 |
| `--seed N` | 给页面及其 worker 里的 `Math.random` 下种子（虚拟时钟下默认 1）。同一 seed 给出同样的粒子、弧线和噪声。 | 随机内容。参考和克隆用同一个 seed。 |
| `--gl` | 跟踪 WebGL 1/2、WebGPU、canvas 2D，以及 three.js、Pixi、PlayCanvas、Babylon、OGL 的场景图，含 worker 里的 OffscreenCanvas。 | 任何 canvas。 |
| `--gl-buffers 16` | 额外转储顶点和索引缓冲（首次上传，最多 16 MB）。 | 想精确拿到位置的粒子和点云。 |
| `--assets` | 保存模型（glb、gltf、hdr、ktx2、drc、usdz、splat…）、Spline、Rive、Lottie 和 Unicorn Studio 文件、着色器文件、GPU 采样过的纹理（按 URL）以及每个脚本。 | 由文件搭起来的场景；找驱动某个通道的代码。 |
| `--gpu hardware` | 用真实 GPU 代替 SwiftShader（macOS：ANGLE/Metal，约快 10×；Linux：Vulkan，需驱动，此处未验证）并启用 WebGPU。 | WebGPU 页面、重场景。参考和克隆用同一模式抓；否则 `compare.ts` 会报警。 |

不用 `--clock virtual`，软件 GL 里的重场景会掉帧、时序会漂。随机内容于是每次加载都不同，你只能拿它和参考的第二次录制比。

## 拿到的东西

| 文件 | 读它拿什么 |
|---|---|
| `gl/summary.md` | 从这里开始。Canvas（尺寸、CSS 尺寸、像素比、`antialias` / `alpha` / `premultipliedAlpha`）、引擎和版本、renderer 设置、场景树、每个被绘制的 program 及其固定与动态 uniform 和 attribute、每块 canvas 一帧的 pass、纹理，以及动态通道。 |
| `gl/shaders/` | 每个 program 编译后的 GLSL（`p3-<label>.vert/.frag`）和 WGSL 模块（`m12-….wgsl`）。three.js 的会带 three 注入的前缀（`#define`、内建 uniform 和 attribute）；干净的 `vertexShader` / `fragmentShader` 在 `three/scene-N.json` 里。 |
| `gl/gl.json` | summary 里一切的完整版：uniform 类型和最终值、attribute 布局（buffer、size、type、stride、divisor）、blend / depth / cull 状态、带来源 URL 的纹理、framebuffer 及其写入的纹理、three.js renderer 设置、带关键帧的 `AnimationMixer` clip、loader URL、canvas 2D 文件。`constants` 存着每个从未变过的 uniform 和场景值。 |
| `gl-track.json` | 每渲染帧一个采样，含每个变化了的值：uniform（`p3:ShaderMaterial.u_progress`，向量写成 `.x .y .z .w`，矩阵写成 `[i]`）、场景图值（`three:s0/Card#12.rotation.x`、`three:s0/mat:ShaderMaterial#8.u_hover`、`pixi:…`、`babylon:…`、`playcanvas:…`、`ogl:…`）和 WebGPU uniform buffer 浮点（`gpu:gb3@0[4]`）。`channels` 给出每个的类型、量程和变化窗口。 |
| `gl/draws.json` | 每帧的每次 draw call：program、primitive、count、instances、目标 framebuffer、绑定的纹理、状态。用它看渲染节奏（每帧还是每隔一帧）和 pass 顺序。 |
| `three/scene-N.json` | 用 three 的 JSON 格式保存的整个 three.js 场景，含几何体、材质（ShaderMaterial 源码和 uniform）和内嵌图片。`new THREE.ObjectLoader().parse(json)` 能把它载回去。 |
| `gl/buffers/`、`gl/textures/` | 缓冲转储（`b7.Float32.bin`）和 canvas 生成的纹理，存成 PNG。 |
| `gl/canvas2d-c1.txt` | Canvas 2D：每第 15 帧的完整调用列表（`arc(172.3, 132.5, 8, 0, 6.283)`、`fillStyle=(hsl(30 80% 60%))`），逐帧调用数在 `draws.json` 里。 |
| `assets/` + `assets.json` | 上面那些文件，按 URL 哈希命名。 |

## 把 trace 读进规格

规格行来自通道，就像 DOM 行来自 `track.json`：

| 通道类型 | 含义 | 规格行 |
|---|---|---|
| `clock` | 全程匀速，例如 `u_time` +1000/s 或旋转 +0.3 rad/s | 「用经过的 ms 驱动 `u_time`」加上速率；无需缓动 |
| `transition` | 从一个静止值到另一个静止值 | from → to、start、duration、easing：`easing.ts --track gl-track.json --channel <key>` |
| `there-and-back` | 升起又落下一次，如 hover 进出或指针划过 | 在转折点切开，每半段用 `--from-ms` / `--to-ms` 拟合 |
| `oscillation` | 重复，带 `periodMs` | 周期、振幅、波形（读着色器或脚本） |
| `steps` | 几次跳变 | 各取值和发生时刻（状态机、时间线） |

- **固定 uniform 是要照抄的常量，不是要猜的**：`u_twistFrequencyX=0.059`、`u_glowAmount=3.86`，还有 `u_resolution`（它告诉你着色器期望的 drawing-buffer 尺寸）。
- **找驱动某个通道的代码**：`grep -l u_scatterPower assets/scripts/*`，读它周围。打包后的代码即便别处都压缩了，uniform 名和常量仍会保留。
- **WebGL 里的指针跟随动效**通常是滞后，逐帧 `x += (target − x) · k`，或逐 ms `1 − exp(−rate·dt)`。看起来像 ease-out，长度取决于指针移动了多远。用 `easing.ts` 在单段指针路径上拟合。若 `k` 是逐帧的，动效就依赖帧率，而帧率由 `--raf-hz` 控制。
- **渲染节奏**：某个 program 0.5 draws per frame 表示每隔一帧才渲染。照抄它，因为它会改变滞后和台阶状动效的观感。
- **Pass**：`framebuffer f4 → texture t5` 后面接一个采样 `t5` 的屏幕 pass，就是一条后处理链。用 render target 重建，或在你的技术栈里用 `EffectComposer` / pass 链重建。
- **带 `AnimationMixer` 的 glb / gltf 场景**：clip 就是规格，和 Lottie 一样。从 `assets/models/` 加载同一文件，按 summary 里显示的 clip 名、`timeScale`、loop 模式和权重播放。
- **canvas 上的 Spline、Rive、Unicorn Studio 和 Lottie**：场景文件就是规格。许可允许时嵌入运行时，否则从文件重建。

## 构建

- 用户技术栈允许时，**用同样的引擎和版本**（summary 里的 `three.js r178`）。three.js 在 r152 改了色彩管理（`outputColorSpace`、sRGB 纹理）、在 r155 改了光照单位，所以版本不同，即便着色器一模一样配色也会变。从 summary 抄 `outputColorSpace`、`toneMapping`、`toneMappingExposure`、clear colour 和 alpha，以及 `autoClear`。
- **Canvas 设置**：抄 context 属性（`antialias`、`alpha`、`premultipliedAlpha`）和像素比。2x 屏上比例为 1，说明站点做了封顶（`setPixelRatio(Math.min(devicePixelRatio, …))`）。
- **着色器**：移植用户写的那部分。three.js 是 `three/scene-N.json` 里的 `vertexShader` / `fragmentShader`。原生 WebGL、regl 或 OGL 就是 `gl/shaders/` 里的源码，原样照搬。除非项目有约定，保留 uniform 名，因为 `gl.ts compare` 按名字匹配通道（否则用 `--map`）。
- **Blend 状态 → three.js 材质**：

  | traced state | three.js |
  |---|---|
  | `blend SRC_ALPHA,ONE_MINUS_SRC_ALPHA,ONE,ONE_MINUS_SRC_ALPHA` | `NormalBlending`（默认，`transparent: true`） |
  | `blend ONE,ONE_MINUS_SRC_ALPHA,ONE,ONE_MINUS_SRC_ALPHA` | 带 `premultipliedAlpha: true` 的 `NormalBlending` |
  | `blend SRC_ALPHA,ONE,ONE,ONE` / `blend ONE,ONE` | `AdditiveBlending`（straight / premultiplied） |
  | `blend DST_COLOR,ONE_MINUS_SRC_ALPHA,ZERO,ONE` | 带 `premultipliedAlpha: true` 的 `MultiplyBlending` |
  | anything else | `CustomBlending` 配 `blendSrc` / `blendDst` / `blendSrcAlpha` / `blendDstAlpha` / `blendEquation` |
  | `no-blend`、`no-depth-write`、`cull` | `transparent: false` 或 `NoBlending`、`depthWrite: false`、`side: FrontSide` |

- **几何体**：`PlaneGeometry{…}` 和 `SphereGeometry{radius, widthSegments…}` 给出构造参数。自定义 `BufferGeometry` 给出 attribute 名和顶点数；当它是数据（点云）而非代码时，用 `--gl-buffers` 转储。
- **随机性**：连调用顺序一起移植生成器，两个页面就会看到同一个带 seed 的 `Math.random`，粒子落在同样的位置。做不到时，加载转储出的缓冲只用于验证，或用 `compare.ts --blur` 判断。
- **与帧率无关**：参考若逐帧 lerp，就在 60 Hz 下保留那个逐帧常量，或把它换算成 `1 − (1 − k)^(dt / 16.67)`，并在报告里说明。

## 验证

用参考命令抓克隆，只改 `--url` 和 `--out`，然后：

```bash
bun <skill>/scripts/compare.ts --ref ref/frames --clone clone-1/frames --out compare-1           # pixels and timing
bun <skill>/scripts/gl.ts compare --ref ref --clone clone-1 --grep "<canvas or scene filter>"    # canvas settings, draw structure, every channel
bun <skill>/scripts/easing.ts --track clone-1/gl-track.json --channel u_hover --compare-track ref/gl-track.json
```

- 有 `--clock virtual` 时参考的噪声底是 0 %：两次抓取完全一致，所以任何差异都算克隆的。
- `gl.ts compare` 在通道 start 或 end 偏差超过 80 ms、类型不同、或平均误差超过参考量程 5 % 时判它失败。它还会列出 canvas 属性、renderer 设置和绘制结构的差异：缺了某个 pass、primitive 数不同、blend 模式、渲染节奏。
- 内容带随机而你没移植生成器时，`compare.ts --blur 4` 比的是密度、配色和动效，不是点的位置。清晰和模糊两个数值都报。

## 仍然存在的限制

- Worker 会下种子、会被跟踪（含 OffscreenCanvas），但它们的时钟按真实时间跑，worker 再起的 worker 够不到。主线程等 worker 回复仍被做成确定性的。
- iframe 里的 canvas 会在其帧里被记录，但不导出。直接抓 iframe 的 URL。
- WebGPU uniform 是没有名字的原始 buffer 浮点（`gpu:gb3@0[4]`）。按 offset 对应到 WGSL struct 字段。
- Compute pass 和 GPU 侧模拟（在着色器里推进的粒子）只以输入形式出现（uniform 和 buffer）。动效活在你照抄的着色器里。
- Spector.js（`captureCanvas()` 返回单帧、每次调用带完整状态的 JSON）适合单帧深挖，作为补充。这里的 trace 是为一段时间内的动效做的。
- 着色器、模型和纹理归各自作者所有，和字体、图片一样。读它们理解效果，只在用户有权时才复制。
