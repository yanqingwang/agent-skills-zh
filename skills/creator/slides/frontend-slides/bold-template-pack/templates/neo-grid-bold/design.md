---
version: alpha
name: Neo-Grid Bold
description: A heavy editorial poster system built on a strict 12-column × 8-row block grid with neon-yellow accents on putty-ecru. Space Grotesk at weight 700 in strict uppercase carries every display moment; JetBrains Mono carries every label and metadata tag. Each slide reads as a magazine spread divided into colored panels — paper-ecru, ink-black, and electric lemon-yellow trading roles across cells. The aesthetic borrows from contemporary editorial print, brutalist annual reports, and the populist-poster end of design week showcases.

colors:
  paper: "#F5F4EF"
  bg: "#ECECE8"
  ink: "#0A0A0A"
  accent-lemon: "#E6FF3D"
  muted: "#8A8A85"
  stage-bg: "#1A1A1A"

color-aliases:
  line: ink
  primary-bg: bg
  card-bg: paper

typography:
  display:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 132px
    fontWeight: 700
    lineHeight: 0.92
    letterSpacing: -0.02em
    textTransform: uppercase
  title:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 88px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -0.015em
    textTransform: uppercase
  subtitle:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.01em
    textTransform: uppercase
  section-num:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 320px
    fontWeight: 700
    lineHeight: 0.85
    letterSpacing: -0.05em
  stat-num:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 156px
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: -0.03em
  stat-num-lg:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 240px
    fontWeight: 700
    lineHeight: 0.85
    letterSpacing: -0.04em
  stat-num-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 96px
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: -0.03em
  card-headline:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.01em
    textTransform: uppercase
  card-h3:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.005em
    textTransform: uppercase
  body:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.35
  body-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 24px
    fontWeight: 400
    letterSpacing: 0.08em
    textTransform: uppercase
  label-sm:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 16px
    fontWeight: 400
    letterSpacing: 0.08em
    textTransform: uppercase
  label-xs:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    letterSpacing: 0.12em
    textTransform: uppercase
  pagenum:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 24px
    fontWeight: 400
    letterSpacing: 0.04em

spacing:
  frame-inset: 40px
  grid-gap: 12px
  grid-gap-lg: 18px
  card-pad-sm: "24px 28px"
  card-pad-md: "28px 32px"
  card-pad-lg: "36px 32px"
  card-pad-xl: "40px 44px"

canvas:
  width: 1920px
  height: 1080px

components:
  frame:
    position: "absolute; inset: 40px"
    display: grid
    gridTemplateColumns: "repeat(12, 1fr)"
    gridTemplateRows: "repeat(8, 1fr)"
    gap: "{spacing.grid-gap}"
    description: "The universal slide frame — a 12-column × 8-row CSS grid inset 40px from each slide edge with 12px gaps between cells. Every slide composes its layout by spanning cells inside this frame."
  card:
    background: "{colors.paper}"
    position: relative
    overflow: hidden
    description: "Generic colored panel. Paper is the default fill; .ink switches to black with paper text; .lemon switches to yellow with ink text; .photo switches to deep-black with white text for image regions."
  card-ink:
    background: "{colors.ink}"
    color: "{colors.paper}"
    description: "Inverted card — black background, paper text. Used as a contrast block in any composition."
  card-lemon:
    background: "{colors.accent-lemon}"
    color: "{colors.ink}"
    description: "Yellow accent card — full neon-yellow fill with ink text. The system's loudest signal."
  pagenum:
    position: "absolute; left: 0; bottom: 0"
    background: "{colors.paper}"
    color: "{colors.ink}"
    padding: "14px 22px"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.04em
    description: "Bottom-left page-number tag in the format '01 / 12'. Three variants: default (paper bg), .invert (ink bg), .lemon (yellow bg)."
  corner-mark:
    position: "absolute; top: 22px; right: 22px"
    width: 36px
    height: 36px
    display: "grid 2x2"
    gap: 4px
    description: "Top-right 2x2 block mark — three solid currentColor squares plus one transparent. A small structural identity stamp."
  blockmark:
    width: 56px
    height: 56px
    display: "grid 2x2"
    gap: 4px
    description: "Larger 2x2 block stamp with diagonal squares filled — used as a brand mark on covers and dividers. May be sized 56px, 96px, or larger."
  qr-tile:
    width: 90px
    height: 90px
    display: "grid 5x5"
    description: "Decorative QR-pattern tile composed of a 5x5 grid of black squares with some accent-lemon squares interspersed. Decorative, not a real scannable code."
  table-cell:
    padding: "18px 22px"
    borderBottom: "1.5px solid {colors.ink}"
    borderRight: "1.5px solid {colors.ink}"
    fontSize: 24px
    lineHeight: 1.35
    description: "Comparison-matrix cell. Solid hairline ink dividers on bottom and right; last column has no right border."
  table-head-row:
    background: "{colors.ink}"
    color: "{colors.paper}"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 14px
    letterSpacing: 0.12em
    textTransform: uppercase
    description: "Inverted table header — black row with paper mono uppercase text."
  pill-yes:
    background: "{colors.accent-lemon}"
    color: "{colors.ink}"
    padding: "6px 14px"
    description: "Affirmative pill in a comparison cell — yellow fill, ink text, mono uppercase."
  pill-part:
    background: "{colors.paper}"
    color: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    description: "Partial-state pill — paper fill, ink border, ink text."
  pill-no:
    background: "{colors.ink}"
    color: "{colors.paper}"
    description: "Negative pill — black fill, paper text."
  arrow:
    width: 64px
    height: 64px
    description: "Inline SVG arrow glyph (right-pointing) at 64px square. Used as a flow indicator between process steps and as an out-of-cell pointer on stat cards."
  highlight-mark:
    background: "{colors.accent-lemon}"
    color: "{colors.ink}"
    padding: "0 6px"
    description: "Inline <mark> element — yellow background swatch wrapping one or more words inside a headline for emphasis."
  bar-fill-ink:
    background: "{colors.ink}"
    description: "Solid black vertical bar for chart series A."
  bar-fill-lemon:
    background: "{colors.accent-lemon}"
    border: "1.5px solid {colors.ink}"
    description: "Yellow vertical bar with ink border for chart series B."
  copyright:
    position: "absolute; left: 22px; bottom: 22px"
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 16px
    lineHeight: 1.4
    color: "{colors.ink}"
    opacity: 0.85
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/neo-grid-bold/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Neo-Grid Bold 是一套**厚重编辑海报系统**，建立在单一结构前提上：每页都是 12 列 × 8 行的 CSS 网格，距页面边缘内缩 40px，单元格间 12px 间隙。构图靠把彩色面板指派给网格跨度完成，`grid-column: 4 / span 5`、`grid-row: 1 / span 5` 就是描述布局的方式。网格是刚性的，视觉变化来自 `{colors.paper}`、`{colors.ink}`、`{colors.accent-lemon}` 的面板在单元格间如何排布。

字体栈刻意收窄。**Space Grotesk** 字重 700 承载每个展示瞬间，严格全大写、负字距。正文以字重 400 大小写混排。**JetBrains Mono** 字重 400 承载每个标签、页码、坐标轴标记、元数据串，始终全大写、0.08–0.12em 正字距。没有第三款字面。厚重 Space Grotesk 全大写与 JetBrains Mono 全大写之间的反差，是系统的主排印节奏。

配色有三款工作色加一种腻子表面。**Paper**（`{colors.paper}`，暖本白）是默认面板填充。**Ink**（`{colors.ink}`，近黑）是结构色：纸上的文字、反色面板填充、所有分隔、所有线。**Accent Lemon**（`{colors.accent-lemon}`，电光霓虹黄 #E6FF3D）是响亮的信号，用作面板填充、标题内 `<mark>` 高亮色块、图表的第二系列。**Putty BG**（`{colors.bg}`）是略冷的本白，衬在 40px 内缩之后，像卡纸一样框住构图。**柔化石墨**在 token 表里，实际很少用。

纵深完全靠**面板相邻与颜色反差**建立，不靠阴影。卡片不带 box-shadow，卡片没有圆角，卡片没有边框（表格单元与胶囊描边除外，用 1.5px 实墨）。一页的视觉分量由多少个单元格填了 `{colors.ink}`、`{colors.accent-lemon}`、`{colors.paper}` 决定。三块黄面板的构图比单块黄面板读起来进攻性强得多。

**密度取向：密集。** 12×8 网格被跨度、颜色各异的面板填满时，Neo-Grid Bold 才显得权威。只有一两块面板、大片空网格的页读作坏了；系统是当编辑海报设计的，海报本就密集。预期式样是每页 4–8 块面板，各占一块不小的单元格跨度，网格从角到角用满。例外是分节断口页，一个 320px 的分节号占满网格的一整格，但即便如此，画布其余部分也由第二块反色面板填满。

**关键特征：**
- 通用 12 列 × 8 行 CSS 网格（`{components.frame}`），距每页边缘内缩 40px，单元格间 12px 间隙。
- 三色面板系统：纸本白（`{colors.paper}`）作默认、墨黑（`{colors.ink}`）作反色块、强调柠檬黄（`{colors.accent-lemon}`）作信号块。
- Space Grotesk 字重 700 全大写、负字距，用于每个展示元素。
- JetBrains Mono 全大写、0.08–0.12em 字距，用于每个标签、页码、坐标轴标记。
- 招牌角标与块标，小小的 2×2 方块印章，作装饰性身份标记。
- 行内 `<mark>` 元素把标题里的词包进霓虹黄块，是系统的标题强调机制。
- 常驻页码标签（`{components.pagenum}`）锚在每页左下。
- 无圆角、无投影、无渐变（照片区的风格化噪声纹理除外）。
- 统计数字放大到 240px 甚至 320px，文字允许主导整块面板。

## 颜色

### 调色板

- **Paper**（`{colors.paper}` — #F5F4EF）：暖本白。默认面板填充、反色时的默认文字色、任何"中性"卡片的画布。比纯白略带奶油，特意选它，让霓虹黄强调不刺眼。
- **BG（腻子）**（`{colors.bg}` — #ECECE8）：略冷的本白，衬在 40px 内缩之后，像卡纸一样框住网格构图。每页四周 40px 腻子边是系统的通用画框。
- **Ink**（`{colors.ink}` — #0A0A0A）：结构性近黑。用于纸上全部文字、全部反色面板填充、全部分隔、全部表格单元边框、全部胶囊描边。不是纯 #000，略柔。
- **Accent Lemon**（`{colors.accent-lemon}` — #E6FF3D）：电光霓虹黄。信号色。用作面板填充、标题内行内 `<mark>` 高亮色块、图表第二系列、肯定态胶囊填充、页码变体背景。绝不作为文字色（黄太浅，在任何表面上都读不成字）。
- **Muted**（`{colors.muted}` — #8A8A85）：保留的石墨调，在 token 表里，但只在照片区标签上以低不透明度使用。可用于弱化文字，实际很少派上场。
- **Stage BG**（`{colors.stage-bg}` — #1A1A1A）：1920×1080 幻灯片画布之外的视口背景。这是 deck-stage 容器色，不属于幻灯片设计。

### 默认值

- **默认幻灯片画布背景**：`{colors.bg}`，表现为每幅网格构图四周 40px 的腻子框。
- **默认面板填充**：`{colors.paper}`。拿不准时，面板就是纸色。
- **默认主标题色**：纸色或柠檬黄面板上用 `{colors.ink}`；墨色面板上用 `{colors.paper}`。
- **默认正文色**：纸 / 柠檬黄上 `{colors.ink}`；墨上 `{colors.paper}`。
- **默认标签 / 元数据色**：纸上 `{colors.ink}`，以 0.7–0.85 不透明度柔化；墨上 `{colors.paper}`，0.7–0.85 不透明度。
- **默认图表系列色**：系列 A `{colors.ink}`；系列 B `{colors.accent-lemon}`（配 1.5px 墨边框）。
- **标题内默认强调机制**：用 `<mark>` 包住，在墨色文字上得到霓虹黄块。这是系统标题级的主要强调。
- **默认肯定态**：`{colors.accent-lemon}` 填充。默认否定态：`{colors.ink}` 填充。默认中性态：`{colors.paper}` 填充配 `{colors.ink}` 边框。

霓虹黄是系统唯一的彩色强调，绝不以红、蓝或任何第三色替代。黄的角色是吸睛，不是传意（它不是语义上的"警告"或"高亮"，纯粹是信号）。

## 排印

### 字族

系统用两款网络字体：**Space Grotesk**（字重 400、500、700）承载全部展示与正文，**JetBrains Mono**（字重 400、500）承载全部标签与元数据。没有第三款字面，无衬线、无斜体、无展示手写体。系统的性格活在 Space Grotesk 700 全大写与 Space Grotesk 400 混排之间的字重反差里，再加 JetBrains Mono 的结构性等宽标签。

一条具体的行内混排规则：**Space Grotesk 标题里的 `<em>` 标签切到 `{colors.accent-lemon}` 色且保持直立**（font-style 归一为非斜体）。Em 被改作黄色行内换色，像 `<mark>` 色块但没有背景填充。

第二条行内混排规则：**`<mark>` 元素以 `0 6px` 内边距把 Space Grotesk 标题里的词包进霓虹黄块**，造出荧光笔强调，是系统反复出现的招牌。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.section-num}` | 320px | Space Grotesk | 700 | 分节断口面板里的英雄分节序数 |
| `{typography.stat-num-lg}` | 240px | Space Grotesk | 700 | 精选大号统计数字 |
| `{typography.stat-num}` | 156px | Space Grotesk | 700 | 标准统计数字 |
| `{typography.display}` | 132px | Space Grotesk | 700 | 封面、分节或英雄展示标题 |
| `{typography.stat-num-sm}` | 96px | Space Grotesk | 700 | 小卡片里的紧凑统计数字 |
| `{typography.title}` | 88px | Space Grotesk | 700 | 内容页主标题 |
| `{typography.subtitle}` | 56px | Space Grotesk | 700 | 次级标题、区域标题 |
| `{typography.card-headline}` | 44px | Space Grotesk | 700 | 面板填充尺度的卡片标题 |
| `{typography.card-h3}` | 30px | Space Grotesk | 700 | 较小卡片里的副标题 |
| `{typography.body}` | 28px | Space Grotesk | 400 | 特性卡片里的正文段落 |
| `{typography.label}` | 24px | JetBrains Mono | 400 | 标准等宽标签或眉题 |
| `{typography.body-sm}` | 22px | Space Grotesk | 400 | 密集卡片里的紧凑正文 |
| `{typography.pagenum}` | 24px | JetBrains Mono | 400 | 页码标签（如 "01 / 12"） |
| `{typography.label-sm}` | 16px | JetBrains Mono | 400 | 次级元数据标签、版权文字 |
| `{typography.label-xs}` | 14px | JetBrains Mono | 400 | 坐标轴标签、表头文字、细则 |

### 默认值

- **默认主分节标题**：`{typography.title}`（88px），内容页主力标题。
- **默认封面或分节开场展示**：封面用 `{typography.display}`（132px）；分节断口序数用 `{typography.section-num}`（320px）。
- **默认正文段落尺寸**：`{typography.body}`（28px）。密集多卡片页降到 `{typography.body-sm}`（22px）。
- **默认标签 / 元数据尺寸**：独立等宽标记用 `{typography.label}`（24px）；行内元数据用 `{typography.label-sm}`（16px）。
- **默认统计数字**：`{typography.stat-num}`（156px）。仅当统计占满一整块精选面板时才取 `{typography.stat-num-lg}`（240px）。
- **任何展示元素默认字重**：700。本系统不存在别的字重的展示。
- **正文默认字重**：400。

拿不准时，页面主文字瞬间取 `{typography.title}`，辅助文案配 `{typography.body}`。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每个 Space Grotesk display、title、subtitle、card-headline、统计数字都全大写**配负字距（按尺度 -0.005 到 -0.05em）。本系统不存在混排展示。
- **正文以字重 400 大小写混排。** 正文绝不全文大写。
- **每个 JetBrains Mono 元素都全大写**、至少 0.08em 正字距。
- **标题里的 `<mark>` 元素始终用 `{colors.accent-lemon}` 背景、`{colors.ink}` 文字、`0 6px` 内边距。** 黄色荧光块是系统的标题强调信号。
- **标题里的 `<em>` 元素切到 `{colors.accent-lemon}` 色并保持直立（font-style: normal）。** 不用斜体字形。
- **负字距随尺寸缩放**：较小标题用 -0.005em 到 -0.015em；较大展示用 -0.02 到 -0.05em。字距越紧，标题读起来越压缩、越粗野，320px 尺寸下 -0.05em 才对。
- **页码始终用 24px JetBrains Mono、0.04em 字距**，格式 `01 / 12`，单个补零、斜杠分隔。

### 排印原则

节奏是**厚重全大写展示 + 轻混排正文 + 小号全大写等宽标签**。三者中任一模式被换掉都会破掉编辑语域。正文全大写读成一段在吼的段落。展示混排读成另一套设计系统。等宽混排读成代码，不像编辑元数据。

斜体字形不用。`<em>` 与 `<mark>` 标签被改作换色 / 高亮开关，不作斜体强调。下划线不用。正文里不用粗体，强调靠把标题隔离在它自己的单元格里达成。

## 布局

### 画布系统

系统以**固定 1920×1080 画布**为目标，渲染在负责缩放适配视口的 `<deck-stage>` web component 内。所有尺寸用 `px`（不用 vw/vh），排印尺寸、内边距、网格间隙、内缩值都是像素固定。构图按 1920×1080 设计，stage 把整份文稿等比缩放。

deck stage 之外的视口背景是 `{colors.stage-bg}`（#1A1A1A），一道深灰框，把明亮的幻灯片在浏览器外壳里视觉锚住。

### 通用画框

每页带一个 `.frame` div，定位 `absolute; inset: 40px`，`display: grid; grid-template-columns: repeat(12, 1fr); grid-template-rows: repeat(8, 1fr); gap: 12px`。这是系统的结构常量：12 列 × 8 行网格、12px 间隙、距页面边缘内缩 40px。某些页变体把网格间隙加到 16–18px 求呼吸空间，但行列数与 40px 内缩永不变。

构图完全靠在这个网格里跨单元格完成。占 `grid-column: 1 / span 4; grid-row: 1 / span 3` 的面板，就是左上角一块 4 格宽 × 3 行高的卡片。网格是唯一的布局语言，flexbox 只用于单个单元格内部的对齐。

### 单元格内边距

单元格内部的内边距随格子大小与用途变化：
- 紧凑卡片（小统计块）：24px × 28px
- 标准卡片（特性面板）：28px × 32px
- 大卡片（章节面板）：36px × 32px
- 英雄卡片（分节断口）：40px × 44px

这些不是刚性 token，是一套实用比例。挑那个既给卡片内部文字呼吸空间、又不丢面板身份的内边距。

### 常驻外壳

每页左下都带一个 `{components.pagenum}` 标签，格式 `01 / 12`。三种变体：
- 默认：纸背景、墨文字。
- `.invert`：墨背景、纸文字。
- `.lemon`：黄背景、墨文字。

有些页还带右上角的 `{components.corner-mark}`（小 2×2 方块）、左下的 `{components.copyright}`，或作品牌标识的 `{components.blockmark}`（较大的 2×2 印章）。

## 纵深与层级

### 无阴影，只有色块相邻

系统在任何结构面板上**零 box-shadow 声明**。纵深完全是颜色相邻的函数：纸面板挨着墨面板读作抬升（纸朝向观者）；黄面板挨着墨面板读作构图里最响的信号。面板间 12px 网格间隙露出单元格之间的腻子 `{colors.bg}`，充当统一画框色。

### 无渐变（照片区除外）

系统里唯一的渐变在照片区占位纹理内，`radial-gradient` 加 `repeating-linear-gradient` 造出风格化黑白颗粒纹理，代照片站位。这些纹理住在 `.photo` 或 `.ph` 类的单元格里，绝不在结构面板上。

### 表格与胶囊上的边框

- 表格单元（`{components.table-cell}`）用底边与右边 1.5px 实墨分隔，造出线框网格。
- 比较胶囊（`{components.pill-part}`）用 1.5px 实墨边框作部分态描边。
- 图表轴用 2px 实墨作左下线框。
- 条形图里的黄条（`{components.bar-fill-lemon}`）带 1.5px 实墨边框，防止亮填充在纸背景上刺眼。

别的元素都不带边框。卡片无边框，靠填充反差。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0px | 每个元素，卡片、胶囊、标签、页码、表格单元、图表条、块标 |

系统在任何元素上**零 border-radius**。每个形状都是严格矩形或方形。块印与角标字形由直角方块拼成。

### 边框粗细

- **1.5px 实 `{colors.ink}`**：表格单元分隔、胶囊描边、黄条边框。最常见的边框粗细。
- **2px 实 `{colors.ink}`**：图表轴（绘图区左与下），略强的线框。

没有别的边框粗细。没有柔化色边框，没有虚线边框（内部用的一条很特定的 `1px dashed rgba(0,0,0,.18)` 图表网格线除外）。

### 装饰元素类型

**块印（`{components.blockmark}`）**：2×2 小方块网格，左上与右下格填充、另两格透明。对角填充的印章，作品牌身份标记。尺寸从 36px（角标）到 96px（引文页上的块印）。可渲染成墨色或强调柠檬黄。

**角标（`{components.corner-mark}`）**：36px × 36px 版的块印，锚在面板右上。作小结构身份标记。

**QR 片（`{components.qr-tile}`）**：5×5 小方块网格，墨与强调柠檬黄填充呈棋盘式图案。装饰性 QR 纹样视觉，不是真能扫的码。用作封面页的点缀。

**箭头（`{components.arrow}`）**：64px × 64px 的行内 SVG 右指箭头（小流程指示用 24px × 24px）。作流程步骤间的流向信号，也作统计面板上的外指标记。

**高亮块（`{components.highlight-mark}`）**：经 `<mark>` 元素把标题里一个或多个词包进的霓虹黄色块。系统的标题强调机制。内边距 `0 6px`（更大尺寸下 `0 8px`）。

**页码（`{components.pagenum}`）**：左下位置标签，格式 `01 / 12`，带彩色背景。三种背景变体（纸、墨、柠檬黄）让页码能适配当前页主导面板上最显眼的颜色。

**照片区**：`.photo` 类单元格，深黑背景（#111），内含一个 `.ph` 子元素渲染风格化黑白噪声纹理（径向 + 对角条纹）。格内一条小等宽标签标注区域（如 "PORTRAIT / B&W"）。在真实照片到位前作占位。

**胶囊（`{components.pill-yes}`、`{components.pill-part}`、`{components.pill-no}`）**：比较单元里的行内等宽全大写标签，三种颜色态：黄填充（肯定）、纸配墨边框（部分）、墨填充配纸文字（否定）。三者都是 0 圆角矩形，名字叫 pill 其实不圆。

**分节序数面板**：一块面板，内容就是一个 320px Space Grotesk 字重 700 的数字。作分节断口页的视觉身份，页面其余部分配一块墨色标题面板。

**图表条对**：两条一组的竖条（系列 A 实墨、系列 B 黄配墨边框）。条在各自列里等宽，列间隙由父网格决定。

## 该做与不该做

### 该做
- 每页都在 12 列 × 8 行网格（`{components.frame}`）上构图，40px 内缩、12px（求呼吸空间时 18px）间隙。网格就是系统的身份。
- 把网格从角到角填满。网格被跨度各异的面板密集占满时，系统才显得权威。
- 用 `{colors.paper}` 作默认面板填充、`{colors.ink}` 作对比块、每页用 1–3 块 `{colors.accent-lemon}` 信号面板。
- 每个 display、title、subtitle、统计数字都用 Space Grotesk 700 全大写配负字距。这个组合是系统的排印声部。
- 标题里用 `<mark>` 把一个或多个词包进黄色荧光块，系统的主标题强调。
- 标题里用 `<em>` 把一个词切成强调柠檬黄（保持直立、无斜体）。
- 每页左下放一个 `{components.pagenum}` 标签。挑与左下方面板形成反差的背景变体（纸 / 墨 / 柠檬黄）。
- 每个标签、页码、坐标轴标记、元数据串都用 JetBrains Mono 全大写、至少 0.08em 字距。
- 比较表格里按标准三色处理渲染胶囊（yes / part / no）。
- 统计数字占精选面板时允许放大到 156–320px。大数字是编辑海报身份的一部分。

### 不该做
- 不要给任何面板加 box-shadow。纵深只来自颜色相邻。
- 不要给任何元素的任何角加圆角。系统严格矩形。
- 不要把展示标题做成混排。Space Grotesk 展示始终全大写。
- 不要把正文做成全大写。字重 400 混排是正文声部。
- 不要引入第二种强调色。霓虹黄是唯一的彩色强调，加红、蓝、绿都会破掉系统。
- 不要把黄当文字色。强调太浅读不成字，它只是填充色。
- 不要在 12×8 网格之外构图。打破网格的绝对定位元素（页码、角标、版权）是明确仅有的例外。
- 不要用斜体字形。`<em>` 标签被改作换色开关，这里不存在斜体视觉样式。
- 不要因为组件叫 pill 就做成圆"胶囊"。胶囊是 0 圆角矩形。
- 不要把网格填得稀疏。一块面板加七个空格的页读作坏了，系统需要密度才能当编辑海报运作。

## 响应式行为

系统以**固定 1920×1080 画布**为目标，渲染在 `<deck-stage>` web component 内（经 `deck-stage.js` 加载）。stage 把整幅 1920×1080 构图等比缩放适配浏览器视口，字号、面板位置、网格间隙、内缩值在画布内都是像素固定，响应式 transform 由 stage 处理。

这意味着：系统里每个排印与布局决策都在 1920×1080 分辨率下做出。尺寸不按断点缩放，整块画布作为一个单元缩放。幻灯片样式里没有媒体查询。

### 放映行为
- `<deck-stage>` web component 管理页间导航、视口缩放与放映外壳。
- 键盘导航、触屏滑动、鼠标滚轮都由 stage 组件处理，不由内联脚本处理。
- 幻灯片画布恒定 1920×1080，与浏览器视口无关，stage 等比缩放它。

### Frontend Slides 集成说明

在 `frontend-slides` skill 里使用本设计系统时，保留
固定 1920×1080 画布模型。不要把 12 列 × 8 行网格、
固定排印、固定间距翻成各自独立的视口响应式
`clamp()` 值。那会破掉面板尺寸与字号比例之间的关系，
在 CJK 文字下尤其如此，即便原模板本可干净缩放，
也可能造成裁切。

稳妥的单文件实现是：

1. 把每页渲染成 1920×1080 的 `.stage`。
2. 把该 stage 等比缩放适配当前视口。
3. 内部 `.frame` 网格保持 `inset: 40px`、`12` 列、`8` 行、
   `12px` 间隙。
4. 先在 1920×1080 设计尺寸下把内容排妥，再缩放整个 stage。
5. 在渲染出的浏览器里核对文字溢出与面板重叠。`scrollHeight`
   检查可能通过，而一块网格面板在视觉上盖住了另一块。

### 打印行为
模板用 deck-stage 组件渲染。打印导出取决于组件的打印处理，可能逐页渲染，也可能只抓当前激活页。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字面 | 中文字面 | 字重 |
|---|---|---|---|
| 展示 / 标题 / 统计（Space Grotesk 700 全大写） | Space Grotesk | Noto Sans SC（思源黑体） | 900 |
| 正文（Space Grotesk 400） | Space Grotesk | Noto Sans SC | 400 |
| 标签 / 页码（JetBrains Mono 全大写） | JetBrains Mono | Noto Sans SC | 400（别强给 CJK 套等宽） |

### 混排策略

策略 A：单条 `font-family` 栈、拉丁优先回退。把每个 token 的 `fontFamily` 从 `"Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"` 改成 `"Space Grotesk, Noto Sans SC, Helvetica Neue, Helvetica, Arial, sans-serif"`。拉丁字形用 Space Grotesk 700 渲染，CJK 字符自动落到 Noto Sans SC 900。像 `THE CLAUDE 模型` 这样的混排串能正确行内渲染。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
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

Neo-Grid Bold 是厚重全大写 Space Grotesk 700 配负字距，尺寸可到 320px。**中文没有全大写概念**，所以系统的主排印招牌（全大写粗野标题）必须改由*字重与密度*承载。把每个中文展示瞬间设成 **Noto Sans SC 900**（可用的最重字重），去匹配大尺寸 Space Grotesk 700 全大写的视觉分量。中文标题还应彻底丢掉负字距；CJK 字形按方形 em 框设计，收紧会造成字撞字。

`<mark>` 霓虹黄色块高亮标题里一个词，迁移到中文堪称完美，把一个汉字或一个短语包进 `<mark>`，柠檬黄块读起来一样。**保留荧光笔机制作为 CJK 里系统的主标题强调。** `<em>` 换色（黄色行内）也能干净迁移。

JetBrains Mono 全大写标签（`01 / 12` 格式的页码）是纯拉丁 / 数字，保留 JetBrains Mono。别试着用等宽渲染中文；CJK 字形本就按等宽设计，强套 JetBrains Mono 会出缺字。含 CJK 的混排等宽标签，以同样尺寸落到 Noto Sans SC 400。

分节序数（320px Space Grotesk 700）与统计数字（156–240px）是纯数字，原样迁移。霓虹黄强调面板系统与文字无关，只要字重守住 900，粗野海报美学就能跨文字存活。

### 已知 CJK 缺口

负字距（-0.005 到 -0.05em）在本系统里随展示尺寸缩放，是"粗野压缩"招牌的一部分。**为中文字符去掉它，会破掉混排文稿里与拉丁页的视觉对等。** 接受这一点：纯 CJK 页会比纯拉丁页读起来略松。别靠收紧中文来补偿，字撞字是比调性不合更糟的失败。

## 迭代指南

1. 每页新布局都在 12×8 网格上经 `grid-column`、`grid-row` 跨度声明构图。除页码标签、角标、版权印章外，绝不用绝对定位打破网格。
2. 每块新面板都用三种填充色之一：纸（默认）、墨（反色）、强调柠檬黄（信号）。不要引入第四种面板色。
3. 每条新展示标题都用 Space Grotesk 字重 700 全大写，负字距按标题尺寸缩放（30px 时 -0.005em，320px 时到 -0.05em）。
4. 每个新正文元素都用 Space Grotesk 字重 400 混排，取三档正文尺寸之一（28px、24px、22px）。
5. 每个新标签或元数据标记都用 JetBrains Mono 全大写、至少 0.08em 字距。
6. 每个新图表系列色要么 `{colors.ink}`（系列 A），要么 `{colors.accent-lemon}` 配墨边框（系列 B）。不要加第三系列色。
7. 每张新卡片用 0 border-radius。方角不可商量。
8. 要强调标题里的一个词，用 `<mark>` 包成黄色块，或用 `<em>` 换成黄色。不要用粗体、斜体、下划线。
9. 每个新比较单元都用三态胶囊系统：黄填充（yes）、纸配墨边框（partial）、墨填充（no）。
10. 把网格填密。若某行空出两个以上单元格，重新想想是不是少了一块卡片。

## 已知缺口

- 系统依赖经 `deck-stage.js` 加载的 `<deck-stage>` web component。缺这个脚本，1920×1080 画布不会缩放到视口，页会按原生像素尺寸渲染。
- 照片区用 CSS 生成的风格化噪声纹理（径向 + 对角条纹渐变）作占位。真实照片需把 `.photo` 单元格内容换成 `<img>`，并确保周围面板色与照片负空间相配。
- QR 纹样片是装饰性的，5×5 方块网格不编码真能扫的码。真 QR 码需另用外部生成的 SVG。
- 条形图高度在每根条填充上用内联 `style="height: XX%"` 声明设定。没有数据绑定层。
- 流程步骤间的箭头 SVG 在每页模板里手工描路径；若某页增删流程节点，箭头位置需手工重算。
- `<deck-stage>` 组件不由本模板的 script 标签直接加载，预期它经 `deck-stage.js` 全局可用。缺脚本会静默地把页渲染成扁平的绝对定位 div。
- 系统通篇用固定像素尺寸（无 `vw`/`vh`）。视口宽高比异常时，deck-stage 的等比缩放可能给画布留下腻子色黑边。
- `{colors.muted}`（#8A8A85）token 有定义，但只用在照片区标签的低不透明度叠层上，在主文字或面板系统里没有角色。
