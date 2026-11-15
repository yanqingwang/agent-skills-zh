---
version: alpha
name: Vellum
description: An essay-pinned-to-a-wall presentation system — a single monochromatic field of deep periwinkle (#2A3870) with warm chartreuse-yellow type (#E8D85C) floating centered on it, every slide. Italic Cormorant Garamond carries every headline at all sizes — the italic serif is the personality, against the bold colorfield. DM Sans handles body in a quiet supporting role. Courier Prime mono provides the typed annotation voice — appearing as a "pin-note" attribution sitting in the bottom-left corner of every slide. The mood is gallery exhibition wall meets archive folder — quiet, monochromatic, deeply still. One color, two warm typefaces, zero motion.

colors:
  navy: "#2A3870"
  navy-alt: "#343F80"
  navy-deep: "#1F2858"
  navy-mid: "#34407A"
  yellow: "#E8D85C"
  yellow-2: "rgba(232,216,92,0.62)"
  yellow-3: "rgba(232,216,92,0.32)"
  emphasis-yellow: "#F5E168"
  teal: "#3A7878"
  border: "rgba(232,216,92,0.20)"

color-aliases:
  c-bg: navy
  c-bg-alt: navy-alt
  c-bg-light: navy
  c-fg: yellow
  c-fg-2: yellow-2
  c-fg-3: yellow-3
  c-fg-light: yellow
  c-emphasis: emphasis-yellow
  c-accent: teal
  c-border: border

typography:
  display:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 11vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 0.92
    letterSpacing: -0.01em
  h1:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 7vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 0.95
    letterSpacing: -0.01em
  h2:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 4vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.05
  h3:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 2.4vw
    fontWeight: 500
    fontStyle: italic
    lineHeight: 1.15
  quote-text:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 3.2vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.25
  quote-mark:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 7vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 0.6
    color: "{colors.teal}"
  stat-value:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 5.5vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1
    letterSpacing: -0.02em
  lead:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.5vw
    fontWeight: 400
    lineHeight: 1.6
  body:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.05vw
    fontWeight: 400
    lineHeight: 1.65
  caption:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 0.85vw
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: 0.72vw
    fontWeight: 400
    letterSpacing: 0.06em
  pin-note:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: 1.15vw
    fontWeight: 500
    lineHeight: 1.5
    color: "{colors.teal}"
    letterSpacing: 0.01em
  bar-val:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: 1.1vw
    fontWeight: 400
    lineHeight: 1

spacing:
  pad-x: 6vw
  pad-y: 6vh
  gap-lg: 5vh
  gap-md: 3vh
  gap-sm: 1.5vh

canvas:
  width: 100vw
  height: 100vh

components:
  pin-annotation:
    position: "absolute bottom-left, padding ~0.9 * pad-y from bottom and 1 * pad-x from left"
    typography: "{typography.pin-note}"
    color: "{colors.teal}"
    maxWidth: "22vw"
    description: "The system's signature element — a small stack of Courier Prime mono lines in dusty teal, sitting in the bottom-left of every slide. Holds slide counter (e.g., '03 / 09'), a short pinned label, and an optional second pin note. Functions as the 'tag stuck to the wall.'"
  kicker:
    typography: "{typography.label}"
    color: "{colors.teal}"
    description: "Small Courier Prime mono label in dusty teal, sits above a headline as a section marker."
  rule:
    width: 28px
    height: 1px
    background: "{colors.teal}"
    description: "A 28px hairline accent rule in dusty teal, used as a small kicker separator."
  chrome-bar:
    borderBottom: "1px solid {colors.border}"
    paddingBottom: "{spacing.gap-sm}"
    marginBottom: "{spacing.gap-md}"
    description: "Top chrome bar — mono label left, mono counter right, low-opacity hairline rule beneath."
  foot-bar:
    borderTop: "1px solid {colors.border}"
    paddingTop: "{spacing.gap-sm}"
    marginTop: "{spacing.gap-md}"
    description: "Bottom chrome bar — mirror of chrome-bar."
  bullet-list-numbered:
    listStyle: "none"
    counter: "list-counter"
    markerFontFamily: "{typography.label.fontFamily}"
    markerColor: "{colors.teal}"
    markerSize: "{typography.label.fontSize}"
    description: "Numbered list using CSS counters — the counter renders in Courier Prime mono at label size in dusty teal, with a 2em column for the number and 0.5em gap to the body."
  pin-stat:
    borderRight: "1px solid {colors.border}"
    padding: "{spacing.gap-md}"
    description: "Vertically-arranged centered stat (italic serif numeral above mono label), separated from neighbors by a single 1px low-opacity hairline. Last stat in row drops the border."
  pin-stat-val:
    typography: "{typography.stat-value}"
    color: "{colors.yellow}"
    description: "Large italic serif stat numeral (5.5vw italic Cormorant Garamond), centered in a pin-stat tile."
  pin-stat-label:
    typography: "{typography.caption}"
    fontFamily: "{typography.label.fontFamily}"
    color: "{colors.yellow-2}"
    description: "Small mono caption beneath a pin-stat numeral."
  compare-panel-dark:
    background: "{colors.navy-deep}"
    description: "Left compare panel — a slightly deeper navy to create internal contrast against the standard navy field."
  compare-panel-light:
    background: "{colors.navy-mid}"
    borderLeft: "1px solid {colors.border}"
    description: "Right compare panel — a slightly lighter navy with a hairline left-border, creating the two-shade panel pair."
  bar-fill-default:
    background: "{colors.yellow-3}"
    description: "Default chart bar fill — yellow at 32% opacity (the tier-3 muted color)."
  bar-fill-accent:
    background: "{colors.yellow}"
    description: "Highlighted chart bar — full yellow."
  chart-baseline:
    height: 1px
    background: "{colors.border}"
    description: "1px hairline baseline beneath chart bars."
  img-placeholder:
    background: "rgba(42,56,112,0.12)"
    border: "1px dashed {colors.border}"
    description: "Image slot — translucent navy fill with a dashed yellow-low-opacity border, centered mono label inside."
  quote-mark:
    typography: "{typography.quote-mark}"
    color: "{colors.teal}"
    description: "A 7vw italic Cormorant Garamond opening quote glyph in dusty teal, sitting centered above a centered pull-quote. The teal color is the system's only large-graphic accent."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/vellum/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Vellum 是一套**单色、墙上的文章**演示系统。视觉前提既严苛又温柔：每页都是同一片深长春花蓝场地（`{colors.navy}` — #2A3870），暖查特酒黄文字（`{colors.yellow}` — #E8D85C）居中浮在其上。没有替代表面，没有浅 / 深主题，没有第二种背景色。场地是常量，文字与左下角一小条批注就是其余的全部。

排印前提是**斜体衬线作个性**。Cormorant Garamond 以斜体、字重 400 跑每个尺度上的每个标题，display 到 h3、quote-text、stat-value。大尺度斜体衬线压在浓烈长春花蓝场地上读作画廊墙上的文字，私人、有思量、略亲密。DM Sans 以安静配角登场，承载正文与导语段，正文本就该后退，让斜体衬线标题引导视线。Courier Prime 等宽扮演最鲜明的角色：它承载"钉注"，一小叠打字机式归属行，坐在每页左下角。灰青色的钉注看着像别在墙上、裱好的文章旁的一张打字机标签，它是系统的招牌。

色彩理念是**一片场地、两种强调**。场地是 `{colors.navy}`。文字是 `{colors.yellow}`，全不透明度作主、62% 作次、32% 作三级。第一强调是 `{colors.emphasis-yellow}`（#F5E168），更亮的黄，只用于斜体标题内的 `<em>` 强调与小号强调文字。第二强调是 `{colors.teal}`（#3A7878），灰调去饱和青，只用于：大引号字形、钉注文字、眉题、28px 强调线、列表计数标记。青是系统里唯一可见的非黄颜色，且出现在精心限定的语境中。

纵深是**扁平且居中**。没有投影，没有圆角，没有渐变。边框是 20% 黄不透明度的 1px 细线，几乎看不见，主要作为淡淡的结构痕迹而非分隔存在。比较布局是唯一例外，它用两档略异的海军蓝（`{colors.navy-deep}` 与 `{colors.navy-mid}`）造出可见的分屏，但即便那里差别也细微。动画时长设为零，页间不过渡。系统按设计完全静止。

**密度取向：稀疏且居中。** Vellum 页是别在墙上的文章，每页装少量内容，居中在画布里，上下左右都有可观呼吸空间。陈述页是一条短标题居中在场地里。封面是一条眉题、一个展示标题、一句导语、角上的钉注，就这些。列表页是居中 60% 宽栏里四条带编号的线。系统一挤就读作坏了，内容周围空着的海军蓝场地是结构性的，不是负空间。它是墙。

**关键特征：**
- 每页单一单色场地，`{colors.navy}`（深长春花蓝）。无浅色主题、无反转。
- 斜体 Cormorant Garamond 字重 400 用于每个标题、每个数字、每个精选衬线瞬间。
- DM Sans 作正文与导语段，Courier Prime 等宽作外壳标签与钉注招牌。
- 黄文字（`{colors.yellow}`）是主，更亮的 `{colors.emphasis-yellow}` 是标题内唯一的 `<em>` 色。
- 灰青（`{colors.teal}`）是第二强调，只用于大引号字形、钉注文字、眉题、28px 线、列表计数标记。
- 钉注（每页左下角灰青色的 Courier Prime 等宽行）是系统的招牌元素。
- 每页内容居中，多数布局 text-align center，内容占画布宽度 55–80%。
- 外壳分隔用 20% 黄不透明度的 1px 细线，其余无边框、无阴影、无抬升。
- 零动效，页间过渡与入场动画时长设为 0。系统本就该静止。
- 斜体是结构性的、非装饰：展示尺度的衬线斜体是系统身份，绝不用直立正体。

## 颜色

### 调色板

- **海军蓝**（`{colors.navy}` — #2A3870）：深长春花蓝场地。每页单一表面。比午夜蓝略暖、比群青略冷，落在一个沉思的蓝色语域。
- **海军蓝 Alt**（`{colors.navy-alt}` — #343F80）：略抬起的海军蓝，用于相邻表面区分。实际很少用。
- **深海军蓝**（`{colors.navy-deep}` — #1F2858）：较深的比较面板调。只用于比较布局左侧，造出面板内部反差。
- **中海军蓝**（`{colors.navy-mid}` — #34407A）：较浅的比较面板调。只用于比较布局右侧。
- **黄**（`{colors.yellow}` — #E8D85C）：暖查特酒黄主文字色。暖、略偏绿，在海军蓝场地上读作旧羊皮纸或查特酒丝绸。
- **黄 2**（`{colors.yellow-2}` — rgba(232,216,92,0.62)）：次级文字，62% 不透明度的黄。用于导语段与描述。
- **黄 3**（`{colors.yellow-3}` — rgba(232,216,92,0.32)）：三级文字，32% 的黄。用于柔化图注、图表轴标签、默认图表条。
- **强调黄**（`{colors.emphasis-yellow}` — #F5E168）：更亮的黄。只用于斜体标题内的 `<em>` 强调（`<em>` 在这更亮的色调里渲染成正体非斜体，见招牌处理）与小号强调文字标签。
- **青**（`{colors.teal}` — #3A7878）：灰调去饱和青。系统的第二强调。只用于：大引号字形、钉注文字、眉题标签、28px 强调线、列表计数标记、项目列表标记。青是系统在黄 / 海军蓝二元之外的色彩招牌。
- **边框**（`{colors.border}` — rgba(232,216,92,0.20)）：细线边框色，20% 不透明度的黄。用于外壳条、统计分隔、图片占位。

### 默认值

- **默认表面**：`{colors.navy}`，每页。
- **默认主文字色**：`{colors.yellow}`。
- **默认次级文字色**：`{colors.yellow-2}`（62% 不透明度的黄）。
- **默认三级文字色**：`{colors.yellow-3}`（32% 的黄）。
- **默认强调色（标题内）**：`{colors.emphasis-yellow}`，施于 `display`、`h1`、`h2` 里的 `<em>` 标签（强调在这更亮的黄里渲染成正体非斜体，提供系统的 `<em>` 机制）。
- **默认眉题 / 钉注 / 强调线色**：`{colors.teal}`。
- **默认大图形强调色**：`{colors.teal}`，专门用于引号字形。
- **默认边框**：`{colors.border}`，20% 不透明度的黄。仅细线。

颜色之间没有语义映射。青不表"警告"，黄不表"高亮"。黄只是文字，青是批注声部，强调黄只是强调旗标。调色板小到不需要语义角色。

## 排印

### 字族

Vellum 以精心分开的角色跑**三款字族**：

- **Cormorant Garamond**（`{typography.display.fontFamily}`）：老式衬线，带极富表现力的斜体轴。承载每个标题（display 到 h3）、每个数字（stat-value）、每个精选衬线瞬间、引文文字、引号字形。标题 token 指定 `fontStyle: italic`，斜体是默认呈现，不是强调变体。字重在 display/h1/h2/quote-text 上是 400（regular），h3 是 500。展示尺度斜体 Cormorant Garamond 压在长春花蓝场地上是系统的定义性视觉瞬间。
- **DM Sans**（`{typography.body.fontFamily}`）：干净的人文怪诞体。承载正文、导语段、项目正文。DM Sans 退在个性字面之后，它是实质，不是声音。
- **Courier Prime**（`{typography.label.fontFamily}`）：打字机式等宽。承载每个外壳标签、每个页码、每页左下角的钉注、列表计数标记、统计标签。等宽是"打字便签声部"，给系统档案 / 展陈语域。

情绪分工：斜体衬线作私人文章声部（标题、引文），无衬线作支撑实质（正文），等宽作打字批注（钉注、外壳）。斜体衬线 + 打字等宽的混搭不寻常，是系统最鲜明的排印组合。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 风格 | 用途 |
|---|---|---|---|---|---|
| `{typography.display}` | 11vw | Cormorant Garamond | 400 | 斜体 | 最大尺度的封面英雄 |
| `{typography.h1}` | 7vw | Cormorant Garamond | 400 | 斜体 | 章节或陈述标题 |
| `{typography.quote-mark}` | 7vw | Cormorant Garamond | 400 | 斜体 | 装饰性起始引号字形（青色） |
| `{typography.stat-value}` | 5.5vw | Cormorant Garamond | 400 | 斜体 | 大斜体衬线统计数字 |
| `{typography.h2}` | 4vw | Cormorant Garamond | 400 | 斜体 | 页面主标题 |
| `{typography.quote-text}` | 3.2vw | Cormorant Garamond | 400 | 斜体 | 引文正文 |
| `{typography.h3}` | 2.4vw | Cormorant Garamond | 500 | 斜体 | 副标题、比较面板标题 |
| `{typography.lead}` | 1.5vw | DM Sans | 400 | 直立 | 导语段、开场句 |
| `{typography.pin-note}` | 1.15vw | Courier Prime | 500 | 直立 | 钉注文字（青色）、bar-val 强调 |
| `{typography.bar-val}` | 1.1vw | Courier Prime | 400 | 直立 | 图表条数值标签 |
| `{typography.body}` | 1.05vw | DM Sans | 400 | 直立 | 默认正文段 |
| `{typography.caption}` | 0.85vw | DM Sans | 400 | 直立 | 图注、次级文字 |
| `{typography.label}` | 0.72vw | Courier Prime | 400 | 直立 | 外壳标签、页码、眉题、统计标签 |

### 默认值

- **主分节标题默认尺寸**：`{typography.h2}`（4vw）。
- **章节或陈述标题默认尺寸**：`{typography.h1}`（7vw）。
- **封面英雄默认尺寸**：`{typography.display}`（11vw）。
- **正文段默认尺寸**：`{typography.body}`（1.05vw）。
- **导语句默认尺寸**：`{typography.lead}`（1.5vw）。
- **任何外壳标签、眉题、等宽元数据默认尺寸**：`{typography.label}`（0.72vw）。
- **钉注默认尺寸**：`{typography.pin-note}`（1.15vw）。
- **统计数字默认尺寸**：`{typography.stat-value}`（5.5vw 斜体）。
- **默认标题字重**：400 斜体。
- **默认标题色**：`{colors.yellow}`。

尺寸间拿不准时，偏大。Vellum 稀疏，标题常常*就是*这一页，所以尺寸应能锚住周围空场地。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每个标题都是字重 400 的斜体 Cormorant Garamond**（h3 是例外，字重 500，仍斜体）。系统里展示尺度的正体（非斜体）衬线不存在，除非作 `<em>` 强调。
- **斜体标题（`display`、`h1`、`h2`）里的 `<em>` 标签渲染成 `{colors.emphasis-yellow}` 的直立正体 Cormorant Garamond、字重 600。** 这是系统的强调机制，斜体翻正体加换色不可商量。它与通行的"斜体表强调"相反，这里斜体是默认，正体才是强调。
- **每页左下角都带一条钉注。** 钉注是一叠 `{colors.teal}` 的 Courier Prime 等宽行，典型是一个页码（如 "03 / 09"）加 1–2 条短钉注（标签、归属、或一个短语）。钉注绝对定位在 `bottom: ~0.9 * pad-y`、`left: pad-x`，max-width 22vw。没有钉注的页读作另一套系统。
- **钉注排印用 `{colors.teal}` 的 Courier Prime 字重 500**，字距 0.01em。换任何别的字面或颜色都会破掉批注语域。
- **眉题用 `{colors.teal}` 的 label 尺寸 Courier Prime 等宽。** 无衬线眉题、斜体眉题、黄眉题都会破掉眉题惯例。
- **大引号字形（7vw 斜体 Cormorant Garamond）渲染成 `{colors.teal}`，而非黄。** 青引号是唯一一处大尺度图形着青，别处青都以小文字（label 尺寸）出现。
- **项目列表用 `{colors.teal}` 的 label 尺寸 Courier Prime 等宽渲染的编号计数器**，绝不用圆点项目、绝不用破折号。编号惯例是系统的列表招牌。
- **每个布局的内容都居中**（text-align: center，flex 列上 items 居中）。左对齐标题会破掉画廊墙上别着文章的语域。

### 排印原则

字族阶梯固定：斜体衬线（Cormorant Garamond 斜体）作标题、数字、引文、任何个性瞬间，无衬线（DM Sans）作正文与导语，等宽（Courier Prime）作外壳、钉注、眉题、列表计数。跨轨道（例如用斜体衬线排正文、或用无衬线做标题）会破掉画廊墙语域。

斜体是结构性的、非强调。标题默认斜体，强调靠切到 `{colors.emphasis-yellow}` 的字重 600 正体达成。这个反转式样是系统最鲜明的排印动作。

行高在展示尺度上紧（display 0.92、h1 0.95），正文放开到 1.5–1.65。展示字距略负（–0.01em），正文与标签近中性。等宽标签带 0.06em 字距，钉注带 0.01em（比外壳标签紧）。

正文里不用粗体。下划线不用。正文里的强调靠与标题内同样的"强调黄正体"式样达成，把 font-style 从斜体切到直立、加重字重、换成更亮的黄。

## 布局

### 画布系统

Vellum 以 `100vw × 100vh` 满视口为目标。每张 `.slide` 以 flex 精确铺满视口，页并排坐在一条横向条里。所有尺寸用视口相对单位（`vw`、`vh`），布局流式缩放。

### 内边距与间隙比例

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 6vw | 幻灯片横向内边距 |
| `{spacing.pad-y}` | 6vh | 幻灯片纵向内边距 |
| `{spacing.gap-lg}` | 5vh | 主内容分节之间 |
| `{spacing.gap-md}` | 3vh | 相关元素之间 |
| `{spacing.gap-sm}` | 1.5vh | 紧密耦合元素之间 |

引文页用 1.2× pad-y 与 1.4× pad-x，给居中引文多留呼吸。比较布局把页面内边距覆盖为 0，因为每个面板自带内部内边距。

### 外壳画框

标准页带外壳条与页脚条（20% 黄不透明度的 1px 细线配等宽标签）。无外壳布局包括封面、陈述、引文、收尾，以及任何内容该无结构画框地漂浮的页，文稿里的大多数。

系统的通用外壳元素是**左下角的钉注**，无论该页是否带外壳 / 页脚条，它都在每页上。钉注是系统常驻的身份标记。

### 内容居中

每个页面布局都让内容居中。封面、陈述、引文、收尾用 `align-items: center; justify-content: center` 配 `text-align: center`。列表、统计、图表用一个 60–80% 宽的居中正文容器。比较布局分成两个等宽面板，各面板内容纵向居中。

内容极少填满超过画布宽度 70% 或高度 60%。余下的海军蓝场地是钉墙语境。

## 纵深与层级

Vellum **完全扁平**。没有投影，没有圆角，没有渐变，根本没有任何抬升系统。

看着像区分的东西来自：
- **海军蓝族内的换色**，比较面板上的 `{colors.navy-deep}` 与 `{colors.navy-mid}` 造出细微的双调配对。
- **20% 黄不透明度的细线边框**，可见但安静的结构痕迹。
- **黄的不透明度层级**，三级（全、62%、32%）提供足够的文字色反差来建立层级，又不引入额外颜色。

系统刻意静止。没有动效（页间与入场动画时长设为 0），没有阴影抬升。页本就该像对开本里的书页一样读，一次一页，无过渡。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0 | 除导航点外的一切 |
| 50%（圆） | 导航点（仅 deck-stage 外壳，不属于页面内容） |

Vellum **没有圆角外壳**。卡片、面板、统计块、图片占位、比较面板，全是严格矩形。仅有的圆形是 deck 导航点，它们属于 deck-stage UI 而非页面内容。

### 边框粗细

- **1px 实线** `{colors.border}`（20% 不透明度的黄）：通用细线。用于外壳条、页脚条、统计分隔、图表基线、比较面板左边缘。
- **1px 虚线** `{colors.border}`：用于图片占位框（虚线边框标示"这是个槽位"）。
- **1px 实线** 略高不透明度（rgba(232,216,92,0.18)）：用于比较面板左 / 右分隔。

系统里没有更重的边框。每条线都是 1px。

### 装饰元素类型

**斜体展示标题**：字重 400 的 Cormorant Garamond 斜体，4–11vw，以 `{colors.yellow}` 居中在页上。标题是每张内容页的主导视觉元素。

**钉注**：一叠 1–3 行 `{colors.teal}` 的 Courier Prime 等宽文字，绝对定位在每页左下角。行里典型含一个页码（如 "04 / 09"）、一条短打字标签、可选第二句钉注短语。行以 0.3vh 间隙叠放，max-width 22vw。这是系统的招牌。

**青引号字形**：7vw 斜体 Cormorant Garamond 的 `"`、着 `{colors.teal}`，居中在居中引文上方。系统里唯一的大尺度青元素。

**眉题**：label 尺寸（0.72vw）`{colors.teal}` 的 Courier Prime 等宽，0.1em 字距。坐在标题上方。

**28px 强调线**：28px × 1px 的 `{colors.teal}` 水平条。作小眉题分隔或章节强调。

**编号列表**：用 CSS `counter-reset: list-counter; counter-increment: list-counter` 以 label 尺寸、`{colors.teal}` 的 Courier Prime 等宽渲染数字，数字占 2em 列、与正文（DM Sans 导语）间 0.5em 间隙。

**钉注统计**：居中一列，上方一个斜体衬线统计数字（5.5vw）、下方一条柔化黄的等宽图注。一排里，钉注统计由单条 20% 黄不透明度的 1px 细线分隔，排末的统计去掉边框。

**比较面板对**：两个并排面板填满页面。左面板 `{colors.navy-deep}` 背景，右面板 `{colors.navy-mid}` 背景配 1px 左边框。每个面板含一条 `{colors.yellow-2}` 的小等宽比较标签、一条斜体 h3、一句斜体导语、一个编号列表。

**图片占位**：`{colors.border}` 的 1px 虚线矩形，内部淡海军蓝，居中 Courier Prime 等宽标签，最小 28vh 高。虚线边框是"槽位"指示。

**图表条**：扁平竖矩形，`{colors.yellow-3}`（默认）或 `{colors.yellow}`（强调）。条数值用 Courier Prime 等宽（`{typography.bar-val}`）渲染。

## 该做与不该做

### 该做

- 每页都填 `{colors.navy}`，单色场地是常量。没有浅色替代。
- 每个标题都用 `{colors.yellow}` 的字重 400 斜体 Cormorant Garamond 渲染。展示尺度的斜体衬线是系统身份。
- 每页左下角放一条钉注，`{colors.teal}` 的 Courier Prime 等宽，1.15vw，max-width 22vw。钉注是系统常驻招牌。
- 标题里的 `<em>` 用 `{colors.emphasis-yellow}` 的字重 600 直立正体（非斜体）。这个斜体翻正体的强调式样不可商量。
- 眉题、列表计数标记、28px 线、大引号字形都着 `{colors.teal}`。青是第二强调，只出现在那些特定语境。
- 每页内容居中。text-align center，items 居中。左对齐标题会破掉别着的文章语域。
- Courier Prime 等宽用于外壳标签、页码、钉注、列表计数标记、条数值。等宽是打字批注声部。
- 项目列表用 `{colors.teal}` 的 Courier Prime 等宽计数器编号。本系统不存在圆点项目与破折号。
- 每个内容块周围留宽裕的空海军蓝场地。稀疏才是对的话语域。
- 页面用 `{spacing.pad-x}` 6vw 与 `{spacing.pad-y}` 6vh 留白，引文页提到 1.2–1.4×。

### 不该做

- 不要引入第二种背景色。海军蓝场地是单一表面。连比较布局也用两档几近一致的海军蓝，而非反差背景。
- 不要把标题渲染成直立正体。展示尺度斜体是默认，正体只作为 `<em>` 强调机制出现。
- 不要加投影、圆角或渐变。系统严苛扁平。
- 不要在引号字形上用黄，也不要把黄当眉题色。那些瞬间是青，换成黄会把青的强调角色压平。
- 不要用圆点项目或破折号。列表以青色 Courier Prime 等宽计数器编号。
- 不要让页动起来。文稿刻意静止，页间过渡与入场动画时长都是 0。
- 不要省掉钉注。无论有无外壳它都在每页上，去掉它会破掉系统招牌。
- 不要引入第三款字面。三款字族（Cormorant Garamond 斜体、DM Sans、Courier Prime）就是整个栈。
- 不要把小文字渲染成斜体衬线。斜体只给展示尺度，正文与图注保持直立无衬线。
- 不要让页从边到边挤满。空海军蓝场地是结构性的，稀疏内容居中、上下有呼吸才是语域。

## 响应式行为

Vellum 以 1920×1080 视口为目标、通篇用视口相对单位（`vw`、`vh`），于是在 1280×720 与 2560×1440 间流式缩放。没有媒体查询，除 deck 外壳圆点与钉注定位偏移外没有固定像素尺寸（那些偏移相对 pad 并随页面内边距缩放）。

### 缩放行为

- 展示标题缩放：11vw → 1920px 视口下约 211px，1280px 下约 141px。
- 正文缩放：1.05vw → 1920px 下约 20px，1280px 下约 13px。
- 钉注定位相对 `pad-y` 与 `pad-x`，随页面内边距缩放。

### 放映行为

文稿由 JS 驱动，但页间过渡时长为零（系统刻意静止）。页并排坐着，经 deck-stage 的 translateX 导航，但用户感知到的是瞬时切换而非动画过渡。没有入场动画系统，因为动画时长为 0，`[data-anim]` 属性没有关联关键帧。

导航点与页码固定在视口底部。

### 打印行为

没有内嵌打印样式表。静态导出取决于把文稿容器解开以逐页顺序渲染。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字面（默认） | 中文字面 | 字重 | 说明 |
|---|---|---|---|---|
| 展示 / h1 / h2 / quote-text / stat-value | Cormorant Garamond 斜体 400 | 霞鹜文楷 LXGW WenKai（LXGW WenKai TC） | 400 | LXGW WenKai 的手写楷体暖意映照 Cormorant 斜体的个性，是 CDN 上唯一带类斜体私人语域的 CJK 字面。 |
| h3 | Cormorant Garamond 斜体 500 | 霞鹜文楷 LXGW WenKai | 400 | 单字重楷体，h2 到 h3 的视觉台阶必须来自尺寸而非字重。 |
| 引号字形（7vw，青） | Cormorant Garamond 斜体 400 | LXGW WenKai 400，或 `「`/`『` 用 NSC | 400 | 中文引文把 `"` 换成同色青的 `「`（全角角引号），用 LXGW WenKai 或 NSC。 |
| 正文 / 导语 | DM Sans 400 | 思源宋体 / Noto Serif SC | 400 | 系统正文在 CJK 里从无衬线切到衬线以保住文学语域，DM Sans 挨着楷体在中文里读成教科书。 |
| 钉注 / 眉题 / 外壳标签 / 列表计数 | Courier Prime 400–500 | Courier Prime + Noto Sans Mono CJK SC 回退 | 400–500 | 钉注通常用拉丁，若出现中文则回退到 Noto Sans Mono CJK SC，青色保留。 |

### 混排策略

本模板用**策略 C（文学）**：保留拉丁字面给英文字形，只在汉字出现时经堆叠 `font-family` 让 CJK 回退进来。Cormorant Garamond 斜体是 Vellum 的定义性品牌身份，把每个标题都换成楷体会剥掉系统"斜体衬线压长春花蓝"的瞬间。让拉丁留在 Cormorant 斜体、中文落进 LXGW WenKai，两种语域都保住。

```css
font-family: 'Cormorant Garamond', 'LXGW WenKai TC', 'Noto Serif SC', Georgia, serif;  /* headlines */
font-family: 'DM Sans', 'Noto Serif SC', system-ui, sans-serif;                         /* body */
font-family: 'Courier Prime', 'Noto Sans Mono CJK SC', 'Courier New', monospace;        /* pin-note / chrome */
```

**警告，展示尺寸下的基线错位。** Cormorant Garamond 斜体的光学中心低于 LXGW WenKai 的光学中心，在 11vw display 与 7vw h1 尤其明显。像 `Vellum 羊皮纸` 这样的短语会显出汉字相对斜体拉丁基线略浮高。缓解办法：
- 给中文段加 `font-feature-settings: "palt"` 收紧度量。
- 把 CJK 包进 `<span lang="zh">`，在展示 token（display、h1、h2、quote-text、stat-value）上加 `vertical-align: -0.05em` 调整。斜体拉丁的倾斜让基线错位比直立配对更显眼，偏移量可能需比非斜体系统略大。
- 纯 CJK 标题（无拉丁）时问题彻底消失。

### 加载

加到 `<head>`（Google Fonts 托管 LXGW WenKai TC、Noto Serif SC、Courier Prime）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:wght@400;500&family=Courier+Prime:wght@400;700&family=LXGW+WenKai+TC&family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

LXGW WenKai TC 是 Google Fonts 上的繁体中文切分，含完整 CJK 统一汉字区，能干净地渲染简体中文。Noto Serif SC 以恰当的 hinting 承载简体中文正文。Cormorant 斜体轴对拉丁保持原样。

### 通用 CJK 调整

施于任何渲染中文内容的元素（典型用 `:lang(zh)` 或 `<span lang="zh">` 限定范围）：

- **行高**：正文 1.75–1.85（Vellum 的 1.65 DM Sans 默认已接近，但为 CJK 笔画再提一点），展示 1.15–1.25（比拉丁 0.92–1.05 松，因为 7–11vw 的 CJK 字形需要纵向呼吸）。
- **字距**：CJK 设 0。Vellum 在展示拉丁上的负字距（-0.01 到 -0.02em）对中文是错的，CJK 字形本就预置间距，负字距会造成重叠。
- **文字变换**：CJK 不用 uppercase。Vellum 在拉丁上也不用全大写（斜体衬线通篇句式），这里只是确认没有父级规则尝试它。
- **全角标点**：用 `，。：；！？`（全角）而非 `,.:;!?`（半角）。中文引文把 `"…"` 换成 `「…」` 或 `『…』`（全角角引号），这些是通行的中文引号字形，贴合系统青引号的处理。
- **展示标题不加句号**：中文标题去掉末尾 `。`，标题的视觉收束已足够。
- **盘古之白（Pangu spacing）**：在 CJK 与相邻拉丁 / 数字间插入一个窄空格。写 `使用 Claude` 而非 `使用Claude`，`2024 年` 而非 `2024年`。这是优质中文排印的编辑惯例，贴合 Vellum 讲究的画廊墙语域。
- **一句一款字体**：不要在同一行里混 LXGW WenKai 与 Noto Serif SC。整段用其中一款，句中切换造成的度量顿挫在这套稀疏居中布局里尤其显眼。

### 本系统的美学提示

LXGW WenKai 与 Vellum 的画廊文章语域极为契合。楷体的手写暖意与 Cormorant Garamond 斜体亲密的私人声部紧密相关，两款字面都读作私人、有思量、略亲密。压在深长春花蓝场地、以暖查特酒黄呈现时，7–11vw 展示的 LXGW WenKai 读作**画廊墙上手写的查特酒黄字**，在中文里可以说比英文原版 Cormorant 处理更有诗意。楷体的笔画起伏与黄的暖意天然相配。

`<em>` 强调机制（斜体 → 正体直立、`{colors.emphasis-yellow}`、字重 600）迁移不到 CJK，因为 LXGW WenKai 没有独立的斜体 / 正体对。CJK 里对等的强调是切到 **`{colors.emphasis-yellow}` 的 NSC 700**，更重字重 + 更亮颜色造出同样的"这就是重点"信号。让强调字重与楷体 regular 明显不同，以保住"直立非斜体"的反转逻辑。

钉注（左下角青色 Courier Prime 等宽）是系统招牌，在混语文稿里无需改动即可成立。纯中文钉注可回退到 Noto Sans Mono CJK SC，打字机纹理部分保住（等宽间距）但打字机性格丢失。可考虑即便在中文文稿里也把钉注留在拉丁（日期、页码、工作室名），这在中文画廊展陈设计里是惯例，读作刻意而非不完整。

编号列表惯例（青色 Courier Prime 计数器）直接迁移，用 Courier Prime 的 `01.` `02.` `03.` 数字而非中文数字（`一、` `二、`），以保住打字批注语域。青色与 2em 列宽不变。

### 已知 CJK 缺口

- LXGW WenKai 只有单一字重（regular）。系统的 h3（字重 500 斜体）在 CJK 里无法靠字重抬一档，视觉层级台阶只能来自尺寸（h2 4vw → h3 2.4vw）。需要更强副标题强调的文稿，可考虑用 NSC 500 作 h3 备选。
- LXGW WenKai 没有斜体轴。Vellum 定义性的"斜体即默认"惯例在 CJK 里无法复现，直立楷体是最接近的类比，它以另一种"手写暖意"语域牺牲了系统的斜体语域。这是 CJK 改编里最大的美学损失。
- 斜体翻正体的 `<em>` 强调机制在 CJK 里不存在。用 `{colors.emphasis-yellow}` 的 NSC 700 替代，取得对等"强调旗标"效果。
- LXGW WenKai TC 的繁体切分字形可能把少量字渲染成繁体形式（如 設 而非 设）。纯简体中文文稿宜以 `font-family: 'Noto Serif SC'` 作主 CJK 字面，把 LXGW WenKai 留给强调瞬间（封面标题、章节标题）。
- 青引号字形（7vw `{colors.teal}` 的 `"`）在 CJK 惯例里不存在。用同尺寸青色的 `「` 或 `『`（全角角引号），这是正确的中文对应，保住系统"青引号瞬间"的信号。
- 展示尺寸下的基线错位（见混排策略）在斜体拉丁 + 直立 CJK 配对里比直立-直立配对更明显。混排封面需逐稿调校。

## 迭代指南

1. 任何新标题都用 `{colors.yellow}` 的字重 400 斜体 Cormorant Garamond。斜体是默认，不是强调。
2. 标题里任何强调短语都切到 `{colors.emphasis-yellow}` 的字重 600 直立正体。斜体翻正体是系统的 `<em>` 机制。
3. 每张新页都必须在左下角含一条钉注。钉注含 1–3 行 `{colors.teal}` 的 Courier Prime 等宽，典型是一个页码加一两条短打字短语。
4. 任何新眉题、列表计数标记、28px 强调线都用 `{colors.teal}`。青是第二强调，预留给这些特定元素。
5. 任何新列表都以青色 Courier Prime 等宽计数器编号。本系统不存在圆点与破折号项目。
6. 任何新布局都让内容居中。text-align center，items 居中。左对齐布局会破掉画廊语域。
7. 任何新背景都会造成系统断裂，只有一种表面色 `{colors.navy}`。比较布局用细微的海军蓝变体，但不引入不同色相。
8. 任何新字体都禁止。Cormorant Garamond、DM Sans、Courier Prime 就是整个栈。
9. 任何新图表、表格、数据展示都用 20% 黄不透明度的 1px 细线。无更重边框、无阴影、无圆角外壳。
10. 内容密度应低且居中。页显得挤时，去掉内容，而非调内边距或缩文字。

## 已知缺口

- 三款字族（Cormorant Garamond、DM Sans、Courier Prime）从 Google Fonts 加载。字体加载失败时，回退是 Georgia（斜体衬线）、system-ui（无衬线）、Courier New（等宽）。缺了 Cormorant 斜体系统会丢掉大量性格，Georgia 斜体替代尚可但比例不同。
- 中文回退（Noto Serif SC、Noto Sans SC）接在栈里，但 Noto Serif SC 没有真斜体，中文斜体标题会回退成直立 Noto Serif SC，丢掉系统定义性的斜体瞬间。
- `.light` 类为向后兼容保留，但渲染与 `.dark` 一致（两者都用海军蓝场地）。`.light` token 别名（`--c-bg-light`、`--c-fg-light`）指向深色 token。
- 动画时长设为 0，系统刻意静止。动画关键帧与 `[data-anim]` 基础设施在引擎里存在，但在 Vellum 里是空操作。重新启用动效需改 token 块里的 `--dur-slide` 与 `--dur-enter`。
- 钉注定位用 `bottom: calc(var(--pad-y) * 0.9)`，刚好略在 pad-y 边界之内，视口极小时钉注可能逼近页边。
- 比较面板用两档几近一致的海军蓝（`{colors.navy-deep}` 与 `{colors.navy-mid}`），在低反差显示器或强环境光下，面板分屏可能难以察觉。
- 青强调色（`{colors.teal}` — #3A7878）去饱和，在某些显示器上可能读作柔化的蓝而非青。
- 系统没有浅色主题、没有反转、没有替代表面。需要"重置"页（用不同颜色背景打断长序列）的文稿，要么接受单色限制，要么走出这套设计系统。
