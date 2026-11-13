---
name: reanimate
description: 从任意参考（在线网站 URL、屏幕录制、mp4/mov/webm、gif、Lottie 文件、原型导出）逐帧克隆一个区块、组件、页面或动画到用户自己的代码库，然后录制克隆结果，与参考逐帧对比验证，迭代到时序、缓动、顺序和布局都匹配。只要用户想从某个网站或视频里 clone、copy、replicate、recreate、reverse-engineer、port 或"偷"一个 hero、区块、组件、marquee、轮播、hover 效果、页面转场、loader、滚动动画或交互，说"make it look/feel/move like this"（做成这个样子）、"same animation as"（动画一样）、"match this exactly"（完全照这个），或者交来一个 gif/视频要求照着做，就使用本 Skill——包括用户还想在上面加自己的内容、配色或额外功能，或只要参考的一部分（一个区块、一个组件、几秒钟）的情况。覆盖 canvas、WebGL、WebGPU 和 three.js / 3D 场景（着色器、粒子、球体、glTF 模型），也覆盖 CSS 和 JS 动效。字体、配色和间距的像素级匹配只在用户明确要求时才做。
---

> **中文汉化版** · 上游：[NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate) · 原文件：`skills/reanimate/SKILL.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# reanimate

把用户指的东西重建出来，让它以参考运动的方式运动；用逐帧对比来证明，一直迭代到对比通过。交付物是用户项目里的代码加上证据（数字和并排对比图），绝不是"看起来差不多了"。

## 什么算"完成"

从用户的措辞里选定保真级别，并在第一条消息里说明；它决定你要验证什么。

| 级别 | 何时 | 必须匹配 | 可以不同 |
|---|---|---|---|
| **motion-faithful**（默认） | "clone this animation"（克隆这个动画）、"make ours feel like theirs"（让我们的感觉像他们家）、"same hero as X but our copy"（hero 同 X，文案换我们的） | 触发方式、顺序与先后、stagger、每一步的时序（±80 ms）、缓动家族、相对元素尺寸的移动方向与距离、布局比例 | 文案、配色、字体、图片、品牌细节 |
| **pixel-faithful** | "match it exactly"（完全一致）、"pixel-perfect"（像素级还原）、"details should match"（细节要对上）、"1:1" | 以上全部，另加字体、字号、配色、间距、圆角、阴影、素材；平均帧差异 ≤ 2 % | 无；用户要求改动的除外 |
| **mixed** | "clone X and add Y"（克隆 X 再加 Y）、"like theirs but with our pricing tiers"（像他们家的，但用我们的价格档） | 克隆部分达到上表某个级别 | 新增部分：描述并展示它们，但只验证不破坏克隆的动效 |

用户可以把目标缩小到一个区块、一个组件、一个页面，或视频的某一段时间（"the first 3 seconds"／前 3 秒，"0:12 to 0:15"）。只克隆这个范围；不要把页面其余部分扯进来。

## 工作流

下面所有东西都放在用户项目内的 `.reanimate/<name>/`（把它加进 `.gitignore`，除非用户想提交这些证据）。保留每一轮的产物；它们就是证据。

### 0. 范围

在任何抓取之前，先在 `.reanimate/<name>/spec.md` 顶部写下三行：

- **Target**：要克隆什么，按用户所说的精确程度（URL + selector / 时间范围 / "gif 里那个开关"）。
- **Destination**：代码放在哪、用什么技术栈（读 `package.json`、现有组件和已在用的动画库；匹配它，而不是引入新的）。
- **Fidelity**：motion-faithful、pixel-faithful 或 mixed；mixed 还要附新增项清单。

能从请求和仓库推断的就推断。只有两种理解会导向不同工作时才提问（比如页面上有两个候选区块，用户只说"the hero"）。当参考是登录墙后的页面，或是这里无法下载的 YouTube/Loom 链接时，向用户要一段屏幕录制，同时继续做其余所有事。

### 1. 准备

下文的 `<skill>` 指本 SKILL.md 所在目录。脚本需要 [Bun](https://bun.sh)；首次运行会下载 Playwright 的 Chromium 和静态 ffmpeg（约 250 MB）。

```bash
bash <skill>/scripts/setup.sh      # installs playwright, ffmpeg, pixelmatch once; prints "ready"
```

所有脚本都用 `bun <skill>/scripts/<name>.ts --help` 运行。它们是确定性的，并共享一条规则：用**相同的**视口、selector 裁剪、触发方式、时长和 fps 抓取参考和克隆，否则对比测量的就是你的配置，而不是你的作品。

### 2. 抓取参考

读 `references/capture.md`，按你的源类型查对应配方。简述：

- **网站**：`capture.ts --url … --out ref --selector <section> --trigger load|scroll|hover|click|none --duration … --track "<moving elements>"`。你会得到 `video.webm`、`frames/`、`inspect.json`（声明的动画、keyframes、计算样式、字体、检测到的库）和 `track.json`（每个动画帧中每个被跟踪元素的位置、尺寸、透明度、transform）。对 CSS/WAAPI 动效，`inspect.json` 往往直接含有精确的时长、延迟和缓动：直接用它们，比估测强。
- **视频或 gif**：`frames.ts --in file --out ref/frames --fps 10..30 --start … --end … --crop …`。先用 `--probe` 探查，再看几帧，确定要克隆组件的裁剪范围。
- **Canvas、WebGL、WebGPU、3D**（`inspect.json › canvases` 有记录，或页面用了 three.js、Pixi、Babylon、Spline…）：抓取时加 `--clock virtual --gl --assets`，读 `gl/summary.md`（`gl.ts summary <out>`）。你会得到着色器源码、每个常量 uniform、场景图、渲染 pass、纹理和模型，以及每个动态 uniform 或对象属性，作为 `gl-track.json` 里的通道。虚拟时钟让每一帧都精确、每次抓取都一致，随机粒子也不例外。读 `references/webgl.md`。
- **Lottie / Rive / 原型导出**：文件本身就是规格；读它，不要从像素重新推导。

然后生成带标签的对比图并查看：`sheet.ts filmstrip --frames ref/frames --out ref/sheets`。用图片查看器逐张读完。这就是用户要的逐帧检查；不要跳过，也不要只抽看第一张。

### 3. 写动效规格

按 `references/analysis.md` 的模板填写 `spec.md`。每个元素的每个属性一行：触发方式、开始时间、时长、延迟或 stagger、from → to、缓动、备注。数字按优先顺序取自：`inspect.json` 的 animations 和 keyframes → 对 `track.json` 跑 `easing.ts`（canvas 场景对 `gl-track.json --channel`）→ 读帧（第一次变化的帧、最后一次变化的帧、有没有过冲）。同时记下动效依赖的静态事实：元素尺寸和位置、z 顺序、overflow 裁剪、transform origin；pixel-faithful 工作还要记字体、配色、间距和素材。

规格就是参考与克隆之间的契约。每一行都会变成第 5 步的一项检查。某一行还写着"?"，就说明你还没把帧读完。

### 4. 构建

按 `references/implementation.md` 在用户的技术栈里实现（缓动表、stagger 计算、滚动与 hover 触发、reduced motion）。DOM 结构尽量贴近参考的角色结构，让被跟踪的 selector 有对应物。mixed 工作要把新增内容放进明显独立的组件或块里，并在 `spec.md` 的 "Additions" 下注明。

给克隆提供与参考相同的抓取途径：一个路由或静态页面，在参考的视口下、用相同的触发方式渲染该组件。dev server 就行（`capture.ts --url http://localhost:5173/…`）；独立 HTML 文件也可以。

### 5. 验证、修复、重复

用抓取参考时的原命令抓取克隆，只改 `--url` 和 `--out clone-N`，然后：

```bash
bun <skill>/scripts/compare.ts --ref ref/frames --clone clone-N/frames --out compare-N
bun <skill>/scripts/sheet.ts compare --ref ref/frames --clone clone-N/frames --diff compare-N/diff --out compare-N/sheets --every 2
bun <skill>/scripts/easing.ts --track clone-N/track.json --selector "<el>" --prop <translateY|opacity|…> --compare-track ref/track.json
```

canvas 工作还要跑 `gl.ts compare --ref ref --clone clone-N`，它会检查 canvas 设置、绘制结构和每个动态通道。

读 `references/verify.md`：怎么读报告、每个保真级别的通过标准、每类失败通常需要什么修复。每一轮都要亲眼看对比图；数字告诉你有问题，对比图告诉你问题是什么。

循环到规格的每一行都通过。每轮：按证据指向改最小的那一处，重新抓取、重新对比。预期 2 到 5 轮。5 轮后仍有某行不过，就停下来，在报告里给出该行的数字和原因（缺字体、用户可能无权复制的着色器或模型、你做了近似的物理弹簧），不要悄悄放低阈值，也不要删掉那一行。

### 6. 报告

最终消息必须能独立成立：

- 保真级别；克隆了什么，新增了什么。
- 代码在哪里（哪些文件），以及如何触发动效。
- 最后一轮对比的简表：时序误差、平均差异、每个关键元素的缓动匹配情况、通过/未通过。
- 最终对比图的路径；环境支持展示图片时以内嵌图片给出。
- 残留偏差，每条都附数字和原因。

## 浪费轮数的坑

- 参考与克隆的视口或裁剪不一致：先修抓取，再动代码。
- 只看第一帧和最后一帧就下结论：缓动藏在中间帧里；去读对比图。
- 字体：fallback 字体不同，每一帧的像素都会变。pixel-faithful 工作先加载同一字体（来自 `inspect.json` 的 fonts）再判差异；motion-faithful 工作忽略文字像素，读时序列。
- 参考录自已加载完的页面，克隆却是冷启动抓的：用 `--wait-before`，或用 `--trigger none` 配一段重启动画的 `--pre-js`，让两边都从静止开始。
- 滚动驱动的动效：它是滚动位置的函数，不是时间的函数。两边用相同的 `--scroll-steps` 和 `--scroll-ms` 抓取，并按滚动位置（track 的 `scrollY`）对比，不按秒。
- JS 库（GSAP、Framer Motion 弹簧）：`--playback-rate` 对它们不起减速作用。用 `track.json` 和 `easing.ts`（它会报告过冲和"spring-like"判定），依据过冲量和稳定时间调弹簧参数。
- 别人屏幕录出的视频带光标、浏览器边框和压缩噪点：把它们裁掉，把 `--pixel-threshold` 略微调高（0.15），而不是去追噪点。
- Canvas 和 WebGL 用真实时钟抓取：软件 GL 下会掉帧，随机内容每次加载都不同，对比测出的就成了机器差异。两边都用 `--clock virtual` 和相同的 `--seed` 抓取。
- 靠截图重建着色器：trace 里已经有它的源码和每个常量。写 GLSL 之前，先读 `gl/shaders/` 和固定 uniform。
