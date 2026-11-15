> **中文汉化版** · 上游：[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · 原文件：`skills/taste-skill/references/scenes.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 大场景

技术页里唯一一处整屏变成一个场景、由滚动驱动的地方。每个场景是 `assets/scenes/<id>/` 里的一个文件夹（`scene.js`、`scene.css`、`meta.json`、`demo.html`）；`index.json` 列出它们，`lib.js` 是它们共享的常驻舞台，`scenes.js` 负责加载，`print.js` 为两个对象场景挂载一份 object render。

## 谁能有一个

- **只给技术页：** 软件（应用、AI、开发者工具、金融科技）、科技（技术产品、硬件、网络）和游戏。一个地点、一项服务或一件普通产品（site-kind 为 other：咖啡馆、民宿、商店、工作室）永远拿不到场景：它拿照片。`index.json` 里的 `types` 恰好是 `software`、`tech` 和 `gaming`。
- **每页至多一个，** 且只在需求简报里有该场景 `needs` 的东西时（它自己的照片、它自己的屏幕、它自己的文字；游戏的关键美术和引擎内截图就是它的照片）。需求没满足就没有场景：绝不拿替身冒充客户的图片。没有美术文件的游戏，把它的名字大字压在布景的替身照片上（`photo` hero 和它的世界区块；只有需求简报要 3D 才上 render），绝不用特效顶替（`sections.md`，Gaming）。
- **发牌：** 在 `fits` 含该区块、`types` 含页面类型、需求简报又满足其 `needs` 的场景里随机发，按 `weight` 加权，避开 `.taste-skill/scenes-history.json` 里最近三个（命令在 `effects-usage.md`）。在计划里点名场景和它的区块。一个大场景就是页面的唯一特效：不要 shader 地面，不要在它旁边再放一个 WebGL 部件。
- **hero 静止时占一屏，** 所以只有 `restH` 为 1 的场景才能发成 hero。`restH` 为 2 的场景（今天三个 hero 场景都是）只能放在 hero 之下，作为一个两屏区块（`--h: 2`），标题用 h2；hero 照常发牌。
- **两个对象场景**（`fixed-hero-object`、`object-through-giant-type`）画的是客户本行业的物件 render（卡牌引擎的一副牌，边缘网络的一只地球仪）；绝不做别的行业的物件，绝不给咖啡馆放一只杯子。
- **页面其余部分保持安静：** 任何卡片、行或磁贴都不因页面滚动而动。场景旁边，页面还可以再拿一两个区块时刻（家规覆盖：一个大场景加一两个滚动时刻），按 `moments.md` 发（短页一个，八区块以上两个），绝不放进场景所在区块或它旁边那个，绝不放进场景的 `avoidMoments` 或它的孪生（`effects-usage.md`，Big scene）。

| id | fits | types | needs | WebGL | restH | phone |
| --- | --- | --- | --- | --- | --- | --- |
| `descend-through-weather` | hero（仅其下方） | tech, gaming | 客户世界的高低两张照片 | - | 2 | still |
| `shaped-window-over-fixed-world` | hero（仅其下方） | tech, gaming | 客户世界的一张宽幅照片 | - | 2 | still |
| `fixed-hero-object` | hero（仅其下方） | tech, gaming | 一个物件 render 或抠图，1-4 章 | 1 | 2 | still |
| `powers-of-ten-pullback` | product | software, tech | 真实尺寸的产品 UI | - | 1 | still |
| `product-assembles-into-its-action` | product | software, tech | 以 HTML 重做的屏幕，4-6 步 | - | 1 | still |
| `parts-lock-into-the-whole` | product | software, tech | 沿面板切开的屏幕 | - | 1 | still |
| `fly-into-the-shape` | between, product | software, tech, gaming | 标志的单条路径，一张暗色照片 | - | 1 | still |
| `letter-physics` | statement | software, tech, gaming | 一句主张和它的回答 | - | 1 | light |
| `object-through-giant-type` | statement | software, tech, gaming | 3-5 行的短引文，一个物件 | 1 | 1 | still |
| `dot-becomes-the-full-stop` | statement | software, tech, gaming | 一句 4-6 个词的主张 | - | 1 | light |
| `letter-bar-floods-the-ground` | between, statement | software, tech, gaming | 两段宣言文案，其后接一个反色区块 | - | 1 | still |

`powers-of-ten-pullback` 绝不做 hero：它的第一屏没有标题也没有行动点。
每个场景在 `scene.js` 里的头部注释保存它的标记结构与选项；`meta.json` 保存它的
`look`、`needs`、`never` 和 `avoidWith`。

## 把一个放上页面

把场景文件夹和共享文件（`scenes.js`、`lib.js`、`scenes.css`，对象场景再加 `print.js`）拷进 `assets/scenes`。按场景头部注释写标记，用客户自己的文字和图片。`<head>` 里放那唯一一行提前加载 script 与两份样式表的代码，成品构图在无 script 时也有样式、场景挂载时什么都不跳；`<body>` 末尾放一次运行时：

```html
<head>
  …
  <script>document.documentElement.classList.add('sc-js');setTimeout(()=>document.documentElement.classList.add('sc-safe'),2500)</script>
  <link rel="stylesheet" href="assets/scenes/scenes.css">
  <link rel="stylesheet" href="assets/scenes/<id>/scene.css">
</head>
…
<section class="sc" data-big-scene="<id>" data-big-scene-opts='{"hold": 1}' style="--h: <the scene's restH>" aria-labelledby="…">
  <div class="sc__stage">…</div>
</section>
…
<script type="module" src="assets/scenes/scenes.js"></script>
```

该区块是 `main` 的直接子元素。`<html data-scenes-ready>` 表示已挂载；`data-scenes-over` 是故障。场景取用页面的 token、字体、圆角和按钮。

### 它的高度（规则 3）

场景区块像其他区块一样留在页面节奏里：恰好一屏或两屏，文字在导航之下。活体状态是 (hold + 1) 屏；`lib.js` 和每个场景默认 `hold` 为 1，所以活体区块是两屏（1440x900 下 1800px）。静止状态（手机、reduced motion、无 script）下，`scenes.css` 把区块的 `--h` 和 padding 保底为最小高度，所以给它 `--h` = 场景的 `restH`（上表），并且不为它写任何页面 CSS：固定高度会切掉构图、压到下一个区块上。绝不拿 `data-screen="free"` 把场景从检查里藏起来。看 390 截图：静止构图填不满半屏就显空（规则 2）。

## 规则

- **demo 只是占位：** 上线场景里的每张图、每个词、每个物件都是客户的。照片在页脚一行致谢，被裁出原框的注明"adapted"。
- **没有它也要可读：** 场景的文字是标记里的真实文本，按阅读顺序；成品构图说尽场景所说的一切。
- **只用原生滚动：** 舞台在 `hold` 屏内吸住；任何东西不得劫持滚轮。
- **手机拿到静止版或轻量版，绝不是完整场景：** 768px 以下每个场景显示成品构图，两个标 light 的文字场景除外（不做深度，没有重叠）。
- **reduced motion、无 script、模块加载失败：** 都落回成品构图，它同时也是 hold 的终点。此时对象场景显示物件的静态图，不挂 WebGL。
- **WebGL：** 每个场景至多一个 context，从页面共享预算里取（`lib.glBudget`、`window.__tpGl`，每页四个），只在区块处于活体状态且进入视口一屏之内时挂载，离开即销毁；WebGL 或 shader 失败时底下永远垫一张静态图。绝不拿 GLSL ES 保留字当名字。
- **没有任何移动的东西穿过正在阅读的文字；** 每个 rest 上宣言都完整可读。照片上的文字站在页面底色的平色带上，或站在照片安静、深色的部分，对比 4.5:1（展示文字 3:1）；绝不在照片上盖 scrim 或渐变（`system.md`）。
- **成本：** 固定尺寸图层上的 transform、opacity 和 clip-path；绝不做每帧重绘的 width、height 或 SVG clip。
- **不要解释场景的说明字幕**，无论在下面还是旁边；不要随滚动起飞的卡片边框、chip 或标签。

## 检查它

```bash
node <skill>/assets/scenes/_demo/shoot.mjs shoot --out <dir> --profile <your own Chrome profile dir> [--only <id>] [--page <url>] [--reduced] [--port 5836]
node <skill>/assets/scenes/_demo/shoot.mjs index [--out <file|dir>]   # from the project folder: its own index.json
```

`index` 在含有 `assets/scenes` 的项目文件夹里运行时，写出项目自己的 `assets/scenes/index.json`（或用 `--out <file|dir>` 指定）。
在已安装的 skill 内部它会拒绝并且什么都不写；`--in-skill` 是故意改写 skill 自己的索引，那不是页面工作的一部分。只有场景的 `meta.json` 变过之后页面才需要它，普通页面跳过即可。

一个开了 CPU WebGL 的 headless Chrome，按自己的 PID 关闭：起点、中段和终点都拍 1440 和 390，每个场景一张 contact sheet。逐张细看；`--reduced` 拍一次。
