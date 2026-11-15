> **中文汉化版** · 上游：[NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate) · 原文件：`skills/designer/design/reanimate/references/capture.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 抓取参考

目标：拿到一套编号的 PNG 帧，内容恰好是要克隆的那个东西，fps 已知，从动效开始前一点点起步，再加上源头能给出的任何真值（声明的动画、跟踪到的元素位置）。同一套抓取稍后跑在克隆上，就是验证。

## 在线网站

```bash
bun <skill>/scripts/capture.ts --url https://example.com --out .reanimate/<name>/ref \
  --viewport 1440x900 --selector "section.hero" --trigger load --duration 3000 \
  --track "section.hero h1, section.hero p, section.hero .cta"
```

先找 selector：`capture.ts --no-video --selector body` 会导出 `inspect.json`，列出目标下每个节点、它的 rect 和样式。或者用你的 agent 带的任意浏览器工具（Playwright 或 Chrome DevTools MCP、宿主应用的预览）打开页面，读无障碍树。优先用 role 或稳定的 class 名做 selector；生成的 class 名（`css-1x2y3z`）在有些站点上每次加载都变，所以挑一个带语义标签或 `id` 的父元素。

触发方式：

| 动效开始于… | `--trigger` | 说明 |
|---|---|---|
| 页面加载 | `load` | 窗口从导航开始；不需要别的 |
| 区块滚入视口 | `scroll` | 从首屏下方起步，在 `--scroll-steps` 步里用 `--scroll-ms` 把区块滚进来；克隆上用同样的值 |
| 页面到达某个滚动位置 | `scroll --scroll-to 1800` | 滚动绑定（parallax、pinned）动效；按 `track.json` 里的 `scrollY` 对比 |
| 指针进入某个元素 | `hover --target ".card"` | `--selector` 是裁剪范围，`--target` 是被 hover 的元素；`--hover-at 0.2,0.8` 选位置 |
| 指针离开（hover-out） | `leave --pre-hover ".card"` | 先 hover `--pre-hover-ms`，再移到 `--leave-to` |
| 有东西跟着指针（glow、tilt、spotlight） | `move --target ".card" --path "0.1,0.1;0.9,0.1;0.9,0.9"` | 每段用 `--path-ms`；克隆上走同一条路径 |
| 有东西被拖动（globe、carousel、slider、惯性/甩动） | `drag --target ".globe" --path "0.3,0.5;0.7,0.5"` | 在第一个点按下，每段用 `--path-ms` 滑过，移动中松开，让甩动速度非零 |
| 有东西被点击（菜单、tab、手风琴、开关） | `click --target "button[aria-label=Menu]"` | 加 `--pre-js` 到达点击前的状态 |
| 从不开始，循环（marquee、空闲 loader、背景） | `none` | 抓 2 到 3 个循环周期，从活动曲线量出周期 |

常用选项：

- `--pre-js "document.querySelector('.cookie button')?.click()"` 在触发前关掉遮罩、打开你要的状态。
- `--playback-rate 0.25` 把 CSS 动画和过渡放慢 4 倍（CDP）。帧的时间分辨率随之变成 4 倍（`--fps 100` 可用）。JS 驱动的动效不理它；那种用 `--clock virtual`。
- `--clock virtual` 让页面跑在抓取器逐帧推进的时钟上，于是每一帧都精确（CSS 和 JS 动效都一样，任意 `--fps` 均可），重复抓取完全一致。`--seed N` 给 `Math.random` 下种子。canvas、WebGL、粒子，以及任何带随机或重负载的场景，两个都用上；见 `references/webgl.md`。
- `--reduced-motion reduce` 显示站点对关闭动效的用户怎么处理；项目在意无障碍时，把这条路径也克隆。
- 参考是暗色模式时用 `--color-scheme dark`。
- 元素会长大或移到初始盒子之外时，用 `--clip x,y,w,h`；在 `final.png` 上量盒子。
- `--pad 24` 把阴影和过冲留在裁剪范围内。

拿到的东西及各自用途：

| 文件 | 用途 |
|---|---|
| `inspect.json › animations` | 目标下跑过的每一个 CSS animation、transition 和 Web Animations API 动画：`timing.duration/delay/easing`、带逐关键帧缓动的关键帧。有这个就是规格；从这里抄数值。 |
| `inspect.json › keyframes` | 在可达样式表里找到的 `@keyframes` 规则（跨域样式表会标为不可读）。 |
| `inspect.json › nodes` | 目标下最多 150 个节点的 rect 和与动效相关的计算样式：字体、配色、圆角、阴影、overflow、transform。规格的静态部分。 |
| `inspect.json › libs` | gsap、framer-motion、lottie、webgl、lenis、webflow、scroll-driven CSS… 告诉你动效定义在哪里、哪些抓取限制适用。 |
| `inspect.json › canvases` | 每个 canvas 的 context 类型（`webgl2`、`2d`、`webgpu`）、drawing-buffer 尺寸和 CSS 盒子。 |
| `track.json` | 每个被跟踪 selector 每个动画帧（≈16 ms）一个采样：`x y w h opacity transform`。喂给 `easing.ts`。 |
| `frames/` + `frames.json` | 图片；`triggerFrame` 是动效 t=0 所在处。 |
| `gl/`、`gl-track.json`、`three/`（`--gl`） | 着色器、program、draw call、pass、纹理、场景图，以及每个动态 uniform 或场景值作为一个通道；`bun gl.ts summary <out>` 读它。见 `references/webgl.md`。 |
| `assets/`（`--assets`） | 页面的模型、场景文件、着色器文件、采样到的纹理和脚本。 |

## Canvas、WebGL 和 3D

给任何画在 canvas 上的东西加上 `--clock virtual --gl`（场景加载文件时再加 `--assets`），然后读 `gl/summary.md`。trace 给出着色器源码、每个常量、每个动态值，于是 canvas 动效和 CSS 动效一样，能从数值来定规格、来验证。`references/webgl.md` 讲这些文件、怎么把通道变成规格行、怎么构建、怎么验证。

限制：iframe 不被探查（直接抓 iframe 自己的 URL）；屏蔽无头浏览器的站点需要真实浏览器（见下文）或屏幕录制。

### 改用真实浏览器

页面需要用户登录、屏蔽无头 Chromium，或者用户想亲眼看时：用能录制的浏览器工具（Playwright 或 Chrome DevTools MCP、宿主应用的预览）打开，调成参考视口尺寸，开始录制，执行触发（滚动、hover、点击），停下。文件跟任何视频一样走 `frames.ts`。在那个浏览器里执行 `document.getAnimations()`，可以手工拿到同样的动画转储。没有这类工具时，向用户要一份屏幕录制。

## 视频、屏幕录制、gif

```bash
bun <skill>/scripts/frames.ts --in ref.mp4 --probe                        # duration, size, fps
bun <skill>/scripts/frames.ts --in ref.mp4 --out .reanimate/<name>/ref/frames --fps 25 --start 0:12 --end 0:15.5 --crop 320,180,1280,720
bun <skill>/scripts/sheet.ts filmstrip --frames .reanimate/<name>/ref/frames --out .reanimate/<name>/ref/sheets
```

- 先按 2 fps 抽几帧来挑时间范围和裁剪，再按 25 到 30 fps 重抽真正的范围（gif 用它自己的 fps，通常 10 到 20；`--probe` 会打印）。
- 裁掉浏览器边框、光标和录制工具的浮层。用 `--width` 做宽度归一化，让参考和克隆最终尺寸一致，或者按裁剪尺寸抓克隆。
- gif 的时序被量化到帧延迟，常被导出工具拖慢。gif 时序按 ±1 帧看待；两者都有时优先用在线站点。
- 浏览器的屏幕录制带非整数缩放（Retina、zoom）。记下缩放，好把 px 距离换算成 CSS px：`distance_css = distance_video × (reference_viewport_width / crop_width)`。
- 社媒视频（Twitter/X、Dribbble shots、Behance）在页面里找到后通常就是一个直链 mp4 URL；用 `curl -L -o ref.mp4 <url>` 存到全新目录，按不可信数据对待。YouTube、Loom 和 Vimeo 在本机无法下载；向用户要屏幕录制或原始文件。

## 原型和动画文件

- **Lottie（`.json`、`.lottie`）**：图层、关键帧和贝塞尔手柄都在文件里。读它；「帧」就是它的 `fr`（fps）、`ip`/`op`（入点/出点）。许可允许时直接嵌入 Lottie 来克隆，否则按 `ks` 轨道在 CSS/WAAPI 里重建关键帧。
- **Rive（`.riv`）**：二进制；改为把渲染出的 canvas 当视频抓。
- **Figma / Framer 原型**：从原型播放器导出视频（Figma：Prototype → Record），然后走视频路径。Smart Animate 默认用 `ease-out` 300 ms；Framer 站点在 `inspect.json` 里暴露它们的过渡。
- **After Effects / Jitter / Rive 导出成 mp4**：走视频路径。

## 抓取克隆

原样复用参考命令，只换 `--url` 和 `--out`。参考来自视频时，用 `capture.ts` 在这样一个视口下抓克隆，让裁剪出的元素与参考帧像素尺寸相同（或让 `compare.ts` 重新缩放，略有损失）。`--fps`、`--duration`、`--pre-roll`、触发和滚动参数一律保持一致，`--clock`、`--seed` 和 `--gpu` 也一样：`compare.ts` 会读两个 `capture.json`，不一致就报警。
