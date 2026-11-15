---
version: alpha
name: Pin & Paper
description: A field-notebook editorial system rendered as yellow legal-pad paper with deep cobalt-blue ink. Every slide carries a fractalnoise paper-grain overlay, hand-drawn safety-pin SVG illustrations that "pin" cards to the page, and a hand-script Caveat face for personal annotations. Space Grotesk at heavy weights carries the printed headlines; DM Mono handles archival labels. The aesthetic borrows from analog field reports, vintage public-notice boards, and the diary pages of scientific notebooks — closer to a lab journal pinned to a corkboard than a polished deck.

colors:
  paper: "#EFE56A"
  paper-2: "#F5ECA0"
  paper-3: "#E8D85A"
  paper-extra: "#FBE6A4"
  cream: "#F8F1D6"
  kraft: "#C9A66B"
  ink: "#1F3A8A"
  ink-soft: "#2D4FB8"
  ink-line: "#3457C4"
  ink-deep: "#0E1430"
  red: "#C2342B"
  olive: "#6B7A2E"
  orange: "#D8702A"

color-aliases:
  c-bg: paper
  c-text: ink
  c-card: cream
  c-stamp: red

typography:
  display-mega:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 196px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.04em
  display-section:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 168px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.04em
  display-stat:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 168px
    fontWeight: 700
    lineHeight: 0.85
    letterSpacing: -0.04em
  h1-cta:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 130px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.035em
  h1-chart:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 110px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.035em
  h2:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 96px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.03em
  h2-md:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 84px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.03em
  h2-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 50px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.02em
  quote-text:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 50px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  card-row:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 44px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -0.02em
  card-h3:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: -0.02em
  card-h3-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.015em
  body:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.45
  body-md:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 21px
    fontWeight: 400
    lineHeight: 1.35
  body-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.45
  body-list:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
  scribble-mega:
    fontFamily: "Caveat, cursive"
    fontSize: 360px
    fontWeight: 700
    lineHeight: 0.8
  scribble-lg:
    fontFamily: "Caveat, cursive"
    fontSize: 70px
    fontWeight: 700
    lineHeight: 0.9
  scribble-md:
    fontFamily: "Caveat, cursive"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 0.9
  scribble-sm:
    fontFamily: "Caveat, cursive"
    fontSize: 38px
    fontWeight: 600
    lineHeight: 1.05
  scribble-xs:
    fontFamily: "Caveat, cursive"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.05
  label-top:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: 18px
    fontWeight: 500
    letterSpacing: 0.12em
    textTransform: uppercase
  label-meta:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: 16px
    fontWeight: 500
    letterSpacing: 0.18em
    textTransform: uppercase
  label-footer:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: 15px
    fontWeight: 500
    letterSpacing: 0.14em
    textTransform: uppercase
  stamp:
    fontFamily: "DM Mono, monospace"
    fontSize: 16px
    fontWeight: 500
    letterSpacing: 0.18em
    textTransform: uppercase

spacing:
  pad-edge: 64px
  pad-top: 110px
  pad-bottom: 90px
  card-pad-md: "28px 28px 24px"
  card-pad-lg: "32px 22px 22px"
  card-pad-xl: "36px 28px 28px"
  card-pad-quote: "60px 80px"
  grid-gap-sm: 22px
  grid-gap-md: 28px
  grid-gap-lg: 32px

canvas:
  width: 1920px
  height: 1080px

components:
  paper-surface:
    background: "radial-gradient(120% 90% at 20% 10%, rgba(255,255,255,.18), transparent 60%), radial-gradient(140% 100% at 80% 95%, rgba(0,0,0,.05), transparent 55%), {colors.paper}"
    description: "Default slide surface — yellow paper with a soft upper-left highlight gradient and a soft lower-right shadow gradient layered over the base paper color."
  paper-grain-overlay:
    selector: ".slide::before"
    background: "fractalNoise SVG via data URI, baseFrequency=1.4, octaves=2"
    opacity: 0.35
    mixBlendMode: multiply
    description: "Non-optional fractal-noise paper grain overlay on every slide. Lives on the ::before pseudo-element; opacity 0.35, multiply blend. On ink slides, opacity drops to 0.25 with screen blend."
  pinned-card:
    background: "{colors.cream}"
    border: "1.5px solid {colors.ink}"
    borderRadius: 4px
    boxShadow: "5px 6px 0 0 {colors.ink}"
    padding: "{spacing.card-pad-md}"
    description: "Cream paper card with a 1.5px ink border, 4px micro-radius, and a hard 5px-6px ink-blue offset shadow. The system's universal card pattern — every card looks like a piece of paper pinned to the surface."
  pinned-card-alt:
    background: "{colors.paper-2}"
    description: "Card variant using the lighter paper-2 tone. Used to break up adjacent same-tone cards."
  pinned-card-alt2:
    background: "{colors.paper-extra}"
    transform: "rotate(0.6deg)"
    description: "Card variant with the deepest paper tone and a slight rotation (0.6 to 1.5 degrees) — gives the impression of being pinned slightly askew."
  pin-illustration:
    width: "varies (110–640px)"
    color: "currentColor"
    transform: "rotate(-14deg to +20deg)"
    description: "Hand-drawn safety-pin SVG illustration in ink-blue or paper (when on ink surface). Multiple variants: closed pin (#pin), open pin (#pin-open). Always rotated slightly off-axis. Acts as both decoration and the visual signal that a card is 'pinned' to the page."
  scribble:
    fontFamily: "Caveat, cursive"
    color: "{colors.ink}"
    lineHeight: 1.05
    description: "Caveat hand-script face used for handwritten notes, marginalia, and 'me' voice annotations. May be rotated slightly (-3 to -1.5 degrees) and underlined via 2px solid ink for emphasis."
  stamp:
    border: "3px solid {colors.red}"
    color: "{colors.red}"
    padding: "6px 16px"
    fontFamily: "DM Mono, monospace"
    fontSize: 16px
    letterSpacing: 0.18em
    textTransform: uppercase
    transform: "rotate(-4deg)"
    description: "Cinnabar-red rubber stamp — 3px solid red border, red mono text, rotated -4 degrees. Used for status marks like CONFIDENTIAL or RECEIVED."
  top-chrome:
    position: "absolute; top: 44px; left: 64px; right: 64px"
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: 18px
    fontWeight: 500
    letterSpacing: 0.12em
    textTransform: uppercase
    description: "Top metadata band — brand lockup on left (with inline #mark SVG glyph), meta tags on right. Mono uppercase, line-height 1."
  footer-chrome:
    position: "absolute; left: 64px; right: 64px; bottom: 36px"
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: 15px
    fontWeight: 500
    letterSpacing: 0.14em
    textTransform: uppercase
    opacity: 0.65
    description: "Bottom metadata band — typically left-source + right-page-position pair at 65% opacity."
  pin-glyph-closed:
    svgId: "#pin"
    viewBox: "0 0 360 110"
    description: "Closed safety-pin SVG glyph — coiled spring on the right, shaft sweeping left, oval clasp cap on the left."
  pin-glyph-open:
    svgId: "#pin-open"
    viewBox: "0 0 360 130"
    description: "Open safety-pin SVG glyph — clasp lifted, sharp point exposed pointing left."
  mark-glyph:
    svgId: "#mark"
    viewBox: "0 0 32 16"
    description: "Small inline mark glyph for the top-chrome brand lockup — circle on the right, arrow shaft pointing left."
  table-cell:
    padding: "18px 22px"
    borderBottom: "1.5px solid rgba(31,58,138,.5)"
    borderRight: "1.5px solid rgba(31,58,138,.5)"
    fontSize: 21px
    lineHeight: 1.35
    description: "Comparison table cell with semi-transparent ink-blue dividers. Sits inside the same cream + ink-border + offset-shadow card pattern."
  pill-yes:
    background: "{colors.ink}"
    color: "{colors.paper}"
    border: "1.5px solid {colors.ink}"
    borderRadius: 999px
    padding: "4px 14px"
    fontFamily: "Caveat, cursive"
    fontSize: 28px
    fontWeight: 600
    description: "Affirmative pill — solid ink fill with paper text, rounded 999px, Caveat script face. Unusual treatment: handwritten letterforms inside a UI pill shape."
  pill-no:
    background: transparent
    color: "{colors.red}"
    border: "1.5px solid {colors.red}"
    fontFamily: "DM Mono, monospace"
    fontSize: 16px
    letterSpacing: 0.14em
    textTransform: uppercase
    description: "Negative pill — red mono uppercase text in a red-bordered transparent pill. The only place red appears in regular use (outside the stamp component)."
  pill-part:
    background: "{colors.paper-2}"
    color: "{colors.ink}"
    fontFamily: "Caveat, cursive"
    description: "Partial-state pill — light paper fill with Caveat script ink text."
  number-script:
    fontFamily: "Caveat, cursive"
    fontWeight: 700
    fontSize: "60–70px"
    color: "{colors.ink}"
    description: "Hand-script numeral used as step numbers in process diagrams and ordered CTA steps. The script face makes ordering feel hand-counted, not algorithmic."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/pin-and-paper/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Pin & Paper 是一套**田野笔记编辑系统**，建立在单一材料前提上：每页都是黄色法律拍纸簿纸面。纸由一层底色（`{colors.paper}`，饱和镉黄）、两道柔和径向渐变高光（左上亮、右下暗），以及一个不可省略的分形噪声颗粒叠层（`::before` 伪元素、multiply 混合）渲染出来。这套叠层造出一块读起来像侧光下实体纸的表面。没有颗粒，系统就塌成扁平卡通黄；纹理是地基，不是装饰。

字体栈是刻意的三声部编辑搭配。**Space Grotesk** 字重 600–700 承载每个印刷标题与展示瞬间，重字重下紧致几何的字形读成海报或公告栏打印件。**Caveat**（手写脚本字面）承载每个手写瞬间：页边批注、"我"声部旁注、步骤数字、胶囊标签、超大脚本序数。Caveat 是系统的个人声部机制，脚本出现在哪里，语气就从"官方通知"切到"页边手写便签"。**DM Mono** 字重 500 承载每个档案元数据标记：顶部外壳品牌锁定、页脚元数据、来源归属、坐标轴标签。三个声部（印刷标题、手写便签、档案目录标签）互不重叠，系统的编辑节奏靠它们各守其道。

配色锚定在黄蓝互补对上。**纸黄**（`{colors.paper}` 及其三个相近变体）是每一处表面。**墨蓝**（`{colors.ink}`，深钴 #1F3A8A）是每一处文字、每一条边框、每一道分隔、每一个别针插画。**奶油**（`{colors.cream}`）是卡片背景，更安静的米白象牙调，让卡片从响亮的黄页上视觉后退。**朱红**（`{colors.red}` — #C2342B）只用在两个特定角色：旋转橡皮印章组件与否定态胶囊。红在这两个角色之外，绝不作为文字、填充或边框。三级色（olive、orange、kraft）在 token 表里，但源码里未实际启用。

纵深由单一招牌机制建立：**硬边偏移阴影**。每张卡片带 `5px 6px 0 0 {colors.ink}`（或 `4px 5px 0 0`，最大引文面板用 `8px 9px 0 0`），一块朝右下偏移、零模糊的实墨蓝矩形。这道阴影加 4px 微圆角加 1.5px 墨边框，定义了通用卡片式样。卡片看着像被别住、从页面上微微掀起，硬边偏移是系统唯一的纵深语言。

**密度取向：中等偏密，填满。** 卡片以清晰排布别满整页时，Pin & Paper 才显得权威，典型每页 3 到 6 张卡，各带一个标题、一段正文块，往往还有一条手写页边批注。只有一个居中标题、其余空白的页读作坏了；系统是当填满的田野笔记页设计的，几乎空白的笔记页读起来没写完。卡片要填满，别针要出现，手写层至少在一半的页上添一条页边注。例外是封面与分节断口页，按惯例更疏，但用超大展示文字（196px）和大号别针插画补偿。

**关键特征：**
- 黄色纸背景（`{components.paper-surface}`），两层径向渐变，每页叠不可省略的分形噪声颗粒（`{components.paper-grain-overlay}`）。
- 深钴蓝墨（`{colors.ink}`）作通用文字、边框、分隔、别针插画色。
- 奶油卡片表面（`{colors.cream}`）配 1.5px 墨边框、4px 微圆角、**硬墨蓝偏移阴影**（5px–6px、零模糊）。
- 手绘安全别针 SVG 插画（`{components.pin-illustration}`），闭合与张开两版，以轻微旋转角别在卡片上。
- 三声部排印：Space Grotesk 作印刷标题，Caveat 手写脚本作个人声部，DM Mono 作档案标签。
- 招牌朱红旋转橡皮印章（`{components.stamp}`）作状态标记（CONFIDENTIAL、RECEIVED 等）。
- 每张卡片 4px 微圆角；胶囊走满 999px。
- 交替卡片带轻微面板旋转（0.6 到 1.5 度），造"别歪了"的效果。

## 颜色

### 调色板

- **纸黄**（`{colors.paper}` — #EFE56A）：主导表面色。饱和镉黄。配上分层径向渐变与颗粒叠层，正是它让页面读作实体纸。
- **浅纸**（`{colors.paper-2}` — #F5ECA0）：更浅、饱和度更低的黄。作备选卡片填充，打破相邻同色调卡片。
- **深纸**（`{colors.paper-3}` — #E8D85A）：更深、更饱和的黄。用于 `.deep` 页变体的高反差瞬间。
- **特调纸**（`{colors.paper-extra}` — #FBE6A4）：带一丝奶油的暖黄，作区分度最高的卡片变体，常配轻微旋转。
- **奶油**（`{colors.cream}` — #F8F1D6）：卡片背景。柔和米白象牙，让卡片从响亮黄页上后退。用在每张标准卡片表面。
- **牛皮纸**（`{colors.kraft}` — #C9A66B）：暖棕 / 牛皮纸调。token 系统里有定义，源码里未实际使用。
- **墨蓝**（`{colors.ink}` — #1F3A8A）：深钴海军蓝。通用文字、边框、分隔、别针插画、阴影色。系统的结构身份。
- **柔墨**（`{colors.ink-soft}` — #2D4FB8）：略浅的钴蓝变体，可用但很少用。
- **线墨**（`{colors.ink-line}` — #3457C4）：略亮的钴蓝，用于线条装饰，很少用。
- **深墨**（`{colors.ink-deep}` — #0E1430）：带一丝蓝调的近黑。用于 `.ink` 页变体背景。
- **朱红**（`{colors.red}` — #C2342B）：印章色，也是否定态胶囊的边框 / 文字色。只用在两个角色，绝不作为通用强调。
- **橄榄**（`{colors.olive}`）与**橙**（`{colors.orange}`）：有定义但未启用。作为保留的三级色调可用。

### 默认值

- **默认页面表面**：`{components.paper-surface}`，带分层渐变的黄纸。始终如此。
- **默认表面颗粒**：`{components.paper-grain-overlay}`，不透明度 0.35、multiply 混合。不可省略。
- **默认主标题色**：黄表面 `{colors.ink}`；墨表面 `{colors.paper}`。
- **默认正文色**：黄 / 奶油上 `{colors.ink}`；墨上 `{colors.paper}`（柔化导语用 `opacity: 0.85`）。
- **默认卡片表面**：`{colors.cream}`。取 `{colors.paper-2}` 或 `{colors.paper-extra}` 来打破相邻同色调卡片。
- **默认边框色**：`{colors.ink}`，1.5px。始终如此。
- **默认阴影**：`5px 6px 0 0 {colors.ink}`（硬偏移、零模糊）。较小卡片可用 `4px 5px 0 0`，最大引文面板用 `8px 9px 0 0`。
- **默认标签 / 元数据色**：`{colors.ink}`，外壳与页脚以 0.65–0.75 不透明度。
- **默认涂写 / 手写色**：`{colors.ink}`。Caveat 在黄上始终是墨蓝。
- **默认印章色**：`{colors.red}`，红唯一常规的用法。

奶油是卡片填充，黄是页面填充。两者混用会破掉视觉层级：黄页上的黄卡片会消失，奶油页上的奶油卡片会塌掉层叠纸的读感。

## 排印

### 字族

系统加载三款网络字体：**Space Grotesk**（字重 400、500、600、700）承载全部印刷展示与正文；**Caveat**（字重 500、600、700）承载全部手写 / 个人声部瞬间；**DM Mono**（字重 400、500）承载全部档案元数据。

每款字面的情绪语域各自分明且承重：
- Space Grotesk 读作**印刷、官方、排印**，文件本身的声音。
- Caveat 读作**手写、私人、页边便签**，读文件的人的声音。
- DM Mono 读作**档案、目录卡、索引**，归档这套文件的系统的声音。

一条关键行内混排规则：**嵌在 Caveat 数字里的 `<small>` 元素切到 60px 的较小 Caveat**，用于单位后缀（如 `M`、`×`、`%`）。手写后缀保住父级数字手工点数的感觉。

第二条行内混排规则：**Caveat 涂写文字里的 `.underline` span 得到一条 2px 实墨蓝下划线**，用来模仿手画的强调线。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.scribble-mega}` | 360px | Caveat | 700 | 装饰性超大引号字形 |
| `{typography.display-mega}` | 196px | Space Grotesk | 700 | 封面标题 |
| `{typography.display-section}` | 168px | Space Grotesk | 700 | 分节断口标题（墨色页上） |
| `{typography.display-stat}` | 168px | Space Grotesk | 700 | 英雄统计数字 |
| `{typography.h1-cta}` | 130px | Space Grotesk | 700 | 收尾 CTA 标题 |
| `{typography.h1-chart}` | 110px | Space Grotesk | 700 | 图表页标题 |
| `{typography.h2}` | 96px | Space Grotesk | 700 | 标准议程或统计标题 |
| `{typography.h2-md}` | 84px | Space Grotesk | 700 | 密集页里的分节标题 |
| `{typography.scribble-lg}` | 70px | Caveat | 700 | 流程步骤数字 |
| `{typography.scribble-md}` | 60px | Caveat | 700 | CTA 步骤数字、大号脚本强调 |
| `{typography.quote-text}` | 50px | Space Grotesk | 500 | 引文正文 |
| `{typography.h2-sm}` | 50px | Space Grotesk | 700 | 告示页标题 |
| `{typography.card-row}` | 44px | Space Grotesk | 600 | 议程行标签 |
| `{typography.card-h3}` | 38px | Space Grotesk | 700 | 卡片标题 |
| `{typography.scribble-sm}` | 38px | Caveat | 600 | 封面手写页边注、告示卡元数据 |
| `{typography.scribble-xs}` | 32px | Caveat | 600 | 卡内小号手写旁注 |
| `{typography.card-h3-sm}` | 28px | Space Grotesk | 700 | 子卡片标题 |
| `{typography.body}` | 22px | Space Grotesk | 400 | 标准正文段落 |
| `{typography.body-md}` | 21px | Space Grotesk | 400 | 表格内正文 |
| `{typography.body-sm}` | 19px | Space Grotesk | 400 | 密集卡内紧凑正文 |
| `{typography.body-list}` | 18px | Space Grotesk | 400 | 卡内列表项 |
| `{typography.label-top}` | 18px | DM Mono | 500 | 顶部外壳品牌锁定与元数据 |
| `{typography.label-meta}` | 16px | DM Mono | 500 | 日期条、归属 |
| `{typography.stamp}` | 16px | DM Mono | 500 | 印章文字 |
| `{typography.label-footer}` | 15px | DM Mono | 500 | 页脚外壳 |

### 默认值

- **默认主内容标题**：`{typography.h2}`（96px Space Grotesk 700）。
- **默认封面 / 开场标题**：`{typography.display-mega}`（196px）。
- **默认分节断口标题**：`{typography.display-section}`（168px），用在墨蓝页变体上。
- **默认正文段落尺寸**：`{typography.body}`（22px）。密集多卡片页降到 `{typography.body-sm}`（19px）。
- **默认卡片标题**：标准卡片 `{typography.card-h3}`（38px），子卡片 `{typography.card-h3-sm}`（28px）。
- **默认统计数字**：`{typography.display-stat}`（168px），配 Caveat `<small>` 后缀作单位（M、%、×）。
- **默认标签 / 外壳尺寸**：顶部外壳 `{typography.label-top}`（18px），底部 `{typography.label-footer}`（15px）。
- **默认手写旁注尺寸**：页边注 `{typography.scribble-sm}`（38px），步骤数字 `{typography.scribble-lg}`（70px）。
- **任何展示元素默认字重**：700。
- **正文默认字重**：400。

拿不准时，标准卡片构图是：38px Space Grotesk 卡片标题 + 22px Space Grotesk 正文段 + 底部一条 32px Caveat 手写便签。这三层排印节奏（印刷标题、印刷正文、手写页边注）是系统最易认的内部式样。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每页都带纸张颗粒叠层（`{components.paper-grain-overlay}`）。** 没它纸的美学就塌。颗粒属于表面，不是装饰点缀。
- **每张卡片都带 1.5px 实墨边框、4px border-radius，以及一道硬墨蓝偏移阴影（5–8px 偏移、零模糊）。** 三者缺一不可，缺阴影卡片像没别住，缺边框像没印刷。
- **Caveat 在黄 / 奶油表面上始终是墨蓝**（`{colors.ink}`），在墨表面上始终是纸黄。别种颜色的 Caveat 不存在。
- **别针插画（`{components.pin-illustration}`）始终离轴旋转**（典型范围 -14° 到 +20°）。0° 渲染的别针会破掉手别美学。
- **印章组件（`{components.stamp}`）始终旋转 -4°**，3px 实红边框、红色等宽文字、零圆角。印章文字始终是 DM Mono 全大写。
- **每个 Space Grotesk 展示标题都用负字距**，区间 -0.02 到 -0.04em，尺寸越大越紧。
- **手写脚本数字（60–70px 的 Caveat）是流程图与有序 CTA 列表里唯一的步骤编号机制。** 别拿 Space Grotesk 数字替代。
- **顶部外壳锁定包含行内 `#mark` SVG 字形**，与品牌文字并排。字形属于品牌身份，不可省略。

### 排印原则

Pin & Paper 的节奏是**印刷标题 + 印刷正文 + 手写页边注 + 等宽档案标签**，四个声部各归其字面。换掉任一声音（例如把页边注排成 Space Grotesk，或把正文段排成 Caveat），系统的编辑语域就塌了。

斜体字形不用。下划线只用在 Caveat 涂写文字里的 `.underline` span（2px 实墨）。正文里粗体很少，强调要么靠换到更大尺寸的较重 Space Grotesk 字重，要么靠在下方添一条 Caveat 手写旁注。

## 布局

### 画布系统

系统以**固定 1920×1080 画布**为目标，渲染在 `<deck-stage>` web component 内。所有尺寸像素固定，stage 负责等比缩放适配浏览器视口。

多数页用**绝对定位**，内容舞台以贴边元素锚定（`left: 64px`、`right: 64px`、`top: 110px`、`bottom: 100px`），卡片行再配定向网格布局。别针插画是叠在卡片堆之上的绝对定位叠层。

### 内边距与锚定

| 锚点 | 值 | 用途 |
|---|---|---|
| `pad-edge` | 64px | 每页左右边缘内缩 |
| `pad-top` | 110px | 内容顶部内缩（在 44px 顶部外壳之下） |
| `pad-bottom` | 90px | 内容底部内缩（在 36px 页脚外壳之上） |
| `grid-gap-sm` | 22px | 流程卡片间隙 |
| `grid-gap-md` | 28px | 告示 / 统计卡片间隙 |
| `grid-gap-lg` | 32px | 便签卡网格间隙 |

卡片通常用顶部 `28px–36px`、两侧 `22px–28px`、底部 `22px–28px` 的内部内边距。

### 外壳画框

每页带 **top chrome band**，顶部 44px / 两侧 64px，左侧品牌锁定（带行内 #mark SVG 字形）、右侧一对元数据标记。外壳是 18px DM Mono 全大写、0.12em 字距。

每页还带 **footer chrome**，底部 36px / 两侧 64px，通常左侧来源归属、右侧页位置标记。页脚是 15px DM Mono 全大写、0.14em 字距、65% 不透明度。

墨蓝页上两条外壳都翻成 `{colors.paper}` 色，颗粒叠层切到不透明度 0.25、screen 混合模式。

## 纵深与层级

### 硬边偏移阴影（主纵深）

系统唯一的纵深处理是每张卡片上的**硬墨蓝偏移阴影**：`5px 6px 0 0 {colors.ink}`（标准）、`4px 5px 0 0`（紧凑）、`6px 7px 0 0 rgba(239,229,106,.25)`（图表卡，带黄调阴影）、`8px 9px 0 0`（最大引文面板）。阴影始终实心、始终朝右下偏移、始终零模糊。系统里没有任何模糊投影。

### 纸纹纵深

不透明度 0.35、multiply 混合的分形噪声颗粒（`{components.paper-grain-overlay}`）添一层微妙的感知纵深，纹理造出读作纸纤维的微观起伏。这是表面层的纵深，不是元素层的。

### 别针插画作纵深信号

手绘安全别针 SVG 放在卡片顶边（典型 `position: absolute; top: -14 to -22px; left: 28–90px; transform: rotate(-6 to -12deg)`），造出卡片被别在页上的视错觉。别针是纵深叙事：卡片顶端出现一枚别针，解释了它为什么有阴影、为什么带旋转。

### 交替卡片的轻微旋转

某些卡片变体（`{components.pinned-card-alt2}`）带轻微旋转（`transform: rotate(0.6deg)` 到 `rotate(1.5deg)`），读作一张别得略歪的纸。这是刻意的瑕疵，省着用（每页一两张卡），不是每张卡都用。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0px | 印章、别针字形、页码 |
| 4px | 卡片、面板、表格容器、图片包装，系统的微圆角 |
| 999px | 仅胶囊 |

系统给每张卡片用 **4px 微圆角**，小到读作"带轻微出血的印刷角"，而非圆润 UI。胶囊是唯一的圆形，且胶囊里装着 Caveat 手写字母这种不寻常处理。

### 边框粗细

- **1.5px 实 `{colors.ink}`**：通用卡片边框。用在每张奶油卡片、每个表格容器、每个面板。
- **1.5px 虚线 rgba(31,58,138,.45)**：作议程行之间、CTA 步骤之间、卡内来源注上方的点状分隔。添"方格纸断行"感。
- **3px 实 `{colors.red}`**：只用在印章组件（`{components.stamp}`）。
- **2px 实 `{colors.ink}`**：只用在 Caveat `.underline` span 处理。

### 装饰元素类型

**别针插画（`{components.pin-illustration}`）**：定义性视觉招牌。手绘安全别针 SVG（两版：闭合与张开），以 `currentColor` 渲染、带轻微旋转角。别针出现在卡片顶端、封面上的装饰叠层、分节断口上超大点缀插画（宽可到 640px），以及别在议程行上。别针是系统的声部，别针出现在哪里，页面就读作一份被别住的文件。

**印章（`{components.stamp}`）**：朱红色旋转橡皮印章标签，3px 实红边框、红色等宽全大写文字、-4° 旋转。用于状态标记（CONFIDENTIAL、RECEIVED）。印章是本系统里红被用到的两个角色之一。

**涂写（`{components.scribble}`）**：Caveat 手写脚本文字块，常旋转 -1.5° 到 -3° 求"手写"感。用于页边注、"我"声部旁注、大号脚本强调。可含 `.underline` span 作手写强调。

**别针卡片（`{components.pinned-card}`）**：通用卡片式样，奶油填充、1.5px 墨边框、4px 微圆角、5–6px 硬墨偏移阴影。常带一枚别针插画叠在顶边。三种备选填充色打破相邻同色调卡片。

**顶部外壳锁定**：品牌文字配一枚行内 #mark SVG 字形（右侧一个圆，箭头杆朝左）。字形属于品牌身份。

**虚线边框分隔**：用作议程列表、CTA 步骤列表的行间分隔，以及卡内来源归属分隔。始终 `1.5px dashed rgba(31,58,138,.45)`。

**Caveat 胶囊（`{components.pill-yes}`、`{components.pill-part}`）**：胶囊里装手写字母（Caveat 28px），配实色或纸调填充。圆润 UI 形状与手写文字的错位是刻意的。

**流程 / CTA 脚本数字**：卡内或列表行里的 60–70px Caveat 序数。手写脚本数字标示"步骤是手点的，不是算法排的"。

**超大脚本引号**：360px 的 Caveat，作引文页的起始字形。脚本尺寸推进到装饰领域，字形大到充当构图，而非标点。

## 该做与不该做

### 该做
- 给每页套纸张颗粒叠层（`{components.paper-grain-overlay}`）。纹理是纸读感的地基。
- 每张卡片都按通用式样设：1.5px 墨边框 + 4px 圆角 + 硬墨偏移阴影。三者一起定义卡片。
- 每个印刷标题都用 Space Grotesk 字重 700 大小写混排、配负字距。
- 每个手写或个人声部瞬间都用 Caveat：页边注、步骤数字、胶囊文字。脚本是系统的"我"声部。
- 每个档案标签、外壳标签、页脚串都用 DM Mono 全大写、0.12–0.18em 字距。
- 每枚别针插画都离轴旋转（典型 -14° 到 +20°）。0° 的别针会破掉手别美学。
- 把卡片填满。3–6 张卡别满整页、各带标题 + 正文 + 页边注时，系统才显得权威。
- 状态标记用旋转印章组件（`{components.stamp}`）。-4° 旋转就是它的身份。
- 流程与 CTA 列表里，把 Caveat 步骤数字与 Space Grotesk 卡片标题配对。脚本数字是系统的排序声部。
- 每页给一张卡加轻微旋转（0.6° 到 1.5°）求"别歪了"效果。不要每张卡都转。

### 不该做
- 不要省掉纸张颗粒叠层。没它表面就塌成扁平卡通黄。
- 不要把 Caveat 手写脚本数字换成别的列表标记。步骤数字始终是手写脚本。
- 不要在印章与否定胶囊之外用红。红是只有两个角色的强调色。
- 不要把别针插画渲染成 0° 旋转。离轴倾斜才是它们读作实体别针的原因。
- 不要用模糊阴影。卡片只用硬墨蓝偏移阴影。
- 不要在黄色页面表面上填黄色卡片。卡片是奶油，奶油卡与黄页的反差就是层叠纸的信号。
- 不要用 Caveat 排正文。手写脚本用于页边注与强调，绝不用于段落。
- 不要用 DM Mono 排标题。等宽是档案声部，不是编辑声部。
- 不要在卡片上用大于 4px 的圆角。微圆角是印刷角的信号，更大圆角会塌成通用 UI。
- 不要排出近乎空白的页。系统是当填满的笔记页设计的，稀疏读作坏了。

## 响应式行为

系统以**固定 1920×1080 画布**为目标，渲染在 `<deck-stage>` web component 内（经 `deck-stage.js` 加载）。stage 负责等比缩放适配浏览器视口，画布内所有像素固定尺寸统一缩放。

### 放映行为
- `<deck-stage>` 组件管理导航、缩放与放映外壳。
- 键盘、触屏、鼠标滚轮导航都由 stage 组件处理。
- 幻灯片画布恒定 1920×1080，与视口尺寸无关。

### 打印行为
打印导出取决于 deck-stage 组件的打印处理。分形噪声颗粒叠层未必在所有 PDF 导出里都能渲染，别假定纹理能迁移，先测试。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字面 | 中文字面 | 字重 |
|---|---|---|---|
| 展示 / 标题（Space Grotesk 700） | Space Grotesk | 龙藏体 Long Cang | 400（唯一可用字重） |
| 正文（Space Grotesk 400） | Space Grotesk | 霞鹜文楷 LXGW WenKai | 400 |
| 手写 / 涂写（Caveat） | Caveat | 龙藏体 Long Cang | 400 |
| 标签 / 等宽（DM Mono 全大写加字距） | DM Mono | 霞鹜文楷 LXGW WenKai | 400（别强给 CJK 套等宽） |

### 混排策略

策略 A：把每个 token 的 `fontFamily` 扩展成拉丁字面之后跟中文字面。Space Grotesk 展示 token 变 `"Space Grotesk, Long Cang, Helvetica Neue, Arial, sans-serif"`；Space Grotesk 正文 token 变 `"Space Grotesk, LXGW WenKai, Helvetica Neue, Arial, sans-serif"`；Caveat token 变 `"Caveat, Long Cang, cursive"`。拉丁字形用原字面渲染，CJK 自动落下。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Caveat:wght@500;600;700&family=DM+Mono:wght@400;500&family=Long+Cang&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-lxgw-wen-kai-regular/font.css" rel="stylesheet">
```

### 通用 CJK 调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 设 0
- 文字变换：CJK 不用 uppercase
- 全角标点（，。：；！？「」（））
- 展示标题不加句号（中文排印惯例）
- 盘古之白（CJK 与拉丁之间加空格：`使用 Claude` 而非 `使用Claude`）
- 一句一款字体

### 本系统的美学提示

Pin & Paper 是全库里对中文最贴合的一套。黄色法律拍纸簿表面、钴蓝墨、安全别针插画、田野笔记语域，都能自然迁入中文，无论哪种文字，系统都读作一页笔记本 / 手账。

**龙藏体 Long Cang** 是硬笔手写的中文字面，相当于中文书写里无毛笔、圆珠笔落纸的样子。它是本系统里 Space Grotesk + Caveat 双角色（标题与涂写）的完美中文替身。Long Cang 大尺寸（96–168px）读作笃定的手写田野笔记标题，正是 Pin & Paper 想唤起的。展示标题与 Caveat 等价的涂写层都用它。纯中文里叠两款视觉有别的手写脚本字面没有必要，Long Cang 一身担两角。

**霞鹜文楷 LXGW WenKai** 是由楷书衍生、为屏幕阅读设计的正文字面，带手写楷书的暖意与轻微不规则，却在正文尺寸（18–22px）下保持易读。它是 Long Cang 手写展示最有力的对位，精确贴合系统"田野笔记个人声部"语域。每段中文正文都设 LXGW WenKai 400。

别针插画、旋转红印章、带硬墨偏移阴影的奶油卡片，全都原样迁移。Caveat 胶囊组件（圆胶囊里装手写字母）换成同一胶囊形状里装 Long Cang，在中文里读成讨喜的手点感。

系统最易认的节奏（印刷标题 + 印刷正文 + 手写页边注）变成（Long Cang 标题 + LXGW WenKai 正文 + 尺寸略异的 Long Cang 页边注）。纯中文里的声部区分来自尺寸、旋转、颜色，而非换字面：页边里 38px、旋转 -3° 的 Long Cang，对着标题里 96px、立正的 Long Cang，清楚读作"页边批注"。

DM Mono 全大写加字距标签迁移不到 CJK。顶部外壳里的中文元数据用 LXGW WenKai 400 大小写混排、字距 0。纯拉丁元数据（日期串、来源 URL）保留 DM Mono。

### 已知 CJK 缺口

Long Cang 与 LXGW WenKai 视觉相邻，两者都带手写楷书基因。三声部编辑搭配（印刷 / 手写 / 档案）在纯中文里塌成两声部（手写展示 / 手写正文 / 仅拉丁的档案）。这不是缺陷，Pin & Paper 的纯中文文稿读起来比拉丁版更通体带手作感，其实更贴近系统追求的田野笔记美学。

## 迭代指南

1. 每张新页背景都是带 `::before` 颗粒叠层的纸面（`{components.paper-surface}`）。别跳过纹理。
2. 每张新卡片都用通用式样：奶油填充、1.5px 墨边框、4px 圆角、硬墨偏移阴影。别自行定制。
3. 每条新标题都用 Space Grotesk 字重 700 大小写混排、配负字距。别换别的字重。
4. 每个新步骤数字或有序列表标记都用 60–70px 的 Caveat 手写脚本。别换成数字字体。
5. 每个新标签或元数据标记都用 DM Mono 全大写、0.12–0.18em 字距。
6. 每枚新别针插画都离轴旋转。求"已固定"感选闭合（#pin），求"已掀起"感选张开（#pin-open）。
7. 要给卡片添个人声部，在底部加一条 Caveat 页边注，通常带一个 `.underline` span 作手写强调。
8. 要给卡片标状态，把印章组件（`{components.stamp}`）以轻微旋转放在卡片上部。
9. 要打破相邻同色调卡片，在奶油、paper-2、paper-extra 填充间交替。给一张卡加轻微旋转求变化。
10. 要用墨蓝表面变体（如分节断口），把文字色翻成 `{colors.paper}`，颗粒不透明度降到 0.25、screen 混合模式。

## 已知缺口

- 系统依赖经 `deck-stage.js` 加载的 `<deck-stage>` web component。缺它，1920×1080 画布不会缩放，页会按原生像素尺寸渲染。
- 别针插画以行内 SVG symbol 定义嵌在文档顶部。需要别针插画的新页必须经 `<use href="#pin">` 或 `<use href="#pin-open">` 引用它们，且文档里必须存在这些 symbol 定义。
- 分形噪声颗粒叠层用带 `feTurbulence` 的 data-URI SVG。某些浏览器（尤其较旧 Safari）可能不一致地渲染噪声，或在 PDF 导出时跳过它。
- Caveat 字体带手写连字，跨操作系统可能渲染不一致。默认回退是 `cursive`，而各系统的 cursive 差别极大。
- `kraft`、`olive`、`orange` 颜色 token 有定义但源码里未启用。预留给未来扩展，当前没有角色。
- pill-yes 组件在圆胶囊形状里用 Caveat 字母，这刻意不寻常，但不熟悉系统的观者可能读成 UI bug。
- 纸张颗粒叠层在标准页用 `mix-blend-mode: multiply`、在墨色页用 `mix-blend-mode: screen`。混合模式翻转不可少，深色墨页上用 multiply 会把页面弄浑。
- 条形图与折线图组件用手工定位坐标点的 SVG。没有数据绑定层。
- 手绘别针 SVG 是固定路径插画。改色经 `currentColor` 可行，但不编辑 SVG 路径数据就无法调整别针比例。
