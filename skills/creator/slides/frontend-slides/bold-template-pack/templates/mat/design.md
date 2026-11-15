---
version: alpha
name: Mat
description: A warm, material-tactile presentation system inspired by a high-end product landing page. Dark forest green is the dominant environment, warmed by a low atmospheric wood-brown glow from the bottom-right corner of every dark slide. Cream type floats directly on the field; warm orange acts as the single accent. The typeface stack pairs Bricolage Grotesque (a heavy, rounded grotesque) for display with DM Sans for body and DM Mono for labels — the result reads as industrial-design portfolio meets boutique product launch, never tech demo.

colors:
  bg-dark: "#232E26"
  bg-dark-alt: "#2E3D30"
  bg-cream: "#EDE6D0"
  bg-cream-alt: "#E4DAC4"
  ink-cream: "#F0E8D2"
  ink-cream-2: "rgba(240, 232, 210, 0.58)"
  ink-cream-3: "rgba(240, 232, 210, 0.3)"
  ink-dark: "#1E2820"
  ink-dark-2: "rgba(30, 40, 32, 0.6)"
  ink-dark-3: "rgba(30, 40, 32, 0.3)"
  accent-orange: "#C07030"
  border-on-dark: "rgba(240, 232, 210, 0.12)"
  border-on-cream: "rgba(30, 40, 32, 0.14)"
  wood-glow: "#7A4E24"

color-aliases:
  c-fg: ink-cream
  c-fg-light: ink-dark
  c-bg: bg-dark
  c-bg-light: bg-cream
  c-accent: accent-orange

typography:
  display:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 12vw
    fontWeight: 800
    lineHeight: 0.88
    letterSpacing: -0.03em
  h1:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 7vw
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: -0.025em
  h2:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 4vw
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.02em
  h3:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 2.4vw
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.01em
  lead:
    fontFamily: "DM Sans, Noto Sans SC, sans-serif"
    fontSize: 1.5vw
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "DM Sans, Noto Sans SC, sans-serif"
    fontSize: 1.05vw
    fontWeight: 400
    lineHeight: 1.65
  caption:
    fontFamily: "DM Sans, Noto Sans SC, sans-serif"
    fontSize: 0.82vw
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "DM Mono, monospace"
    fontSize: 0.7vw
    fontWeight: 400
    letterSpacing: 0.12em
    textTransform: uppercase
  stat-value:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 5.5vw
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -0.025em
  quote-text:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 3.4vw
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.02em
  quote-mark:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 8vw
    fontWeight: 800
    lineHeight: 0.6

spacing:
  pad-x: 5.5vw
  pad-y: 5.5vh
  gap-lg: 4.5vh
  gap-md: 2.8vh
  gap-sm: 1.4vh

canvas:
  width: 100vw
  height: 100vh

components:
  kicker:
    fontFamily: "{typography.label.fontFamily}"
    fontSize: "{typography.label.fontSize}"
    letterSpacing: 0.12em
    textTransform: uppercase
    color: "{colors.accent-orange}"
  rule:
    width: 32px
    height: 1px
    background: "{colors.accent-orange}"
  bullet-marker:
    content: "—"
    color: "{colors.accent-orange}"
    fontFamily: "{typography.label.fontFamily}"
    description: "Em-dash prefix in warm orange; emerges in mono face. The system's standard list mark; never a bullet, never a checkmark."
  info-card:
    background: "{colors.bg-cream}"
    color: "{colors.ink-dark}"
    padding: "{spacing.gap-md} calc({spacing.pad-x} * 0.8)"
    maxWidth: 28vw
    description: "Cream inset box embedded on a dark green field. The signature material-contrast component; carries a heading and a body block, no border, no shadow."
  chrome-band:
    borderBottom: "1px solid {colors.border-on-dark}"
    paddingBottom: "{spacing.gap-sm}"
    description: "Label-pair on top of a 1px rule; suppressed on cover/quote/end slide types."
  foot-band:
    borderTop: "1px solid {colors.border-on-dark}"
    paddingTop: "{spacing.gap-sm}"
    description: "Label-pair under a 1px rule; mirrors the chrome band."
  stat-cell:
    borderRight: "1px solid {colors.border-on-dark}"
    padding: "{spacing.gap-md} {spacing.pad-x} {spacing.gap-md} 0"
    description: "A vertically-divided cell containing a large numerical value (with optional inline orange-emphasis em-span) and a one-line label. Last cell has no right border."
  bar-fill:
    width: "100%"
    background: "{colors.ink-cream-3}"
    description: "Vertical bar in muted cream; gets the orange accent (.accent variant) when it's the highlighted data point."
  compare-divider:
    width: 1px
    background: "{colors.border-on-dark}"
    description: "A 1px-wide vertical column (not a border) used to split a before/after comparison; subtle, not loud."
  image-placeholder:
    background: "rgba(240, 232, 210, 0.06)"
    border: "1px solid {colors.border-on-dark}"
    color: "{colors.ink-cream-3}"
    description: "Hairline-bordered void with centered mono label until photography is available."
  atmospheric-glow:
    selector: ".slide.dark::before"
    position: "bottom-right ellipse, 55% wide × 70% tall"
    gradient: "radial-gradient(ellipse at 70% 80%, rgba(122, 78, 36, 0.28) 0%, rgba(80, 50, 20, 0.14) 40%, transparent 70%)"
    description: "The wood-brown atmospheric glow that lives on every dark slide via ::before. Non-optional on dark surfaces; defines the warmth of the system."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/mat/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Mat 是一套**材料触感演示系统**，围绕单一环境前提搭建：深森林绿表面，从右下角被一束低矮的木棕辉光烘暖。氛围承担了主要工作——内容还没落地，页面就已经像午后光线里的一张工作台。奶油色文字直接浮在绿色场地上，没有卡片、没有面板、没有画框。系统需要打破绿色时，只用一个奶油色内嵌盒（info-card），读起来像一张暖纸铺在深色表面上。

字体栈是刻意的三声部搭配。**Bricolage Grotesque** 字重 700 与 800 是展示主力，粗壮、圆润，带一点机械气质，适合产品文案又不像科技创业公司。**DM Sans** 字重 400 是正文声部，中性到足以让展示字面呼吸。**DM Mono** 字重 400 掌管所有标签、眉题、元数据与外壳，也就是一切需要读成标签而非句子的结构性文字。本系统里展示文字**始终大小写混排**，绝不全大写；全大写留给等宽标签。

配色刻意收窄。**深森林绿**是主导表面（`{colors.bg-dark}`），另备一档略浅的绿用于分层区域。**暖奶油**是深底上的主文字色，页面翻浅时作次级表面色。**暖橙**（`{colors.accent-orange}`）是唯一强调色，只以小面积行内标记出现：眉题文字、项目破折号、统计数字里的 `<em>`、起始引号、图表里那根高亮的条。橙色绝不作为背景，绝不做大标题色；它是系统的结构性重点符。

纵深极浅、靠氛围，不靠堆叠。没有投影。任何结构元素都没有圆角。唯一的纵深信号是木棕色径向辉光，经 `::before` 伪元素落在每张深色页背后。区域分隔靠**低不透明度奶油的 1px 细线**：外壳条、页脚条、统计单元分隔、比较面板切分、图表基线。这套系统没有一处是响的。

**密度取向：中等偏疏。** 页面留得开时 Mat 才显得优雅：宽裕的左右内边距（`{spacing.pad-x}` 5.5vw）、一个主排印瞬间、一段辅助文案。把三栏项目塞进一页会破掉系统；暖绿色场地需要负空间来做它的氛围工作。例外是统计页与比较页，克制的三栏或两栏单元排列才算对。一个标题加一段导语的页面正合这套系统的路数。用文字填满 80% 面积的页面是在跟设计较劲。

**关键特征：**
- 深森林绿画布（`{colors.bg-dark}`）配暖木棕径向辉光（`{components.atmospheric-glow}`），锚定在每张深色页右下角。
- 奶油文字（`{colors.ink-cream}`）直接浮在绿色场地上，周围无卡片、无面板、无画框。
- Bricolage Grotesque 展示文字**始终大小写混排**，绝不全大写。全大写留给 DM Mono 标签。
- 单一强调色暖橙（`{colors.accent-orange}`），只作小面积行内强调（眉题、项目标记、行内 `<em>`、引号、一根图表条）。
- 奶油 **info-card**（`{components.info-card}`）是招牌材料反差组件，一块暖纸矩形内嵌在深色场地上。
- 项目列表用 DM Mono 渲染的暖橙破折号前缀，绝不用圆点，绝不用对勾。
- 低不透明度奶油的 1px 细线是唯一的分隔语言。无粗边、无阴影。
- 系统只有一个浅色变体（奶油底配深绿文字），作整套文稿里的色调反转，绝不作默认。

## 颜色

### 调色板

- **深森林绿**（`{colors.bg-dark}` — #232E26）：主导环境。除非刻意选浅色变体，否则是每页默认背景。绿压得够沉，奶油文字落上去不刺眼。
- **略浅绿**（`{colors.bg-dark-alt}` — #2E3D30）：深底内分层或后陷表面预留的一档色调。可用，但省着用。
- **暖奶油**（`{colors.bg-cream}` — #EDE6D0）：浅色页背景，也是 info-card 内嵌盒的填充色。读起来是暖纸，不是白，这份暖对系统的材料身份不可少。
- **更深的奶油**（`{colors.bg-cream-alt}` — #E4DAC4）：次级奶油调，用于浅色页上的图片占位。
- **奶油墨**（`{colors.ink-cream}` — #F0E8D2）：深色表面上的主文字色。比背景奶油略暖，特意选它，让标题像刻进绿色里，而不是印在上面。
- **58% / 30% 奶油墨**（`{colors.ink-cream-2}`、`{colors.ink-cream-3}`）：深色上次级与三级文字。分别用于柔化的导语和几乎看不见的元数据。
- **深墨**（`{colors.ink-dark}` — #1E2820）：奶油表面上的主文字色（info-card 正文、浅色页）。极深的森林绿，绝非纯黑。
- **60% / 30% 深墨**（`{colors.ink-dark-2}`、`{colors.ink-dark-3}`）：奶油上的柔化与三级文字。
- **暖橙**（`{colors.accent-orange}` — #C07030）：唯一强调色。一种烧过的铜橙，向木头、皮革、氧化金属致意。绝不作背景，绝不做大标题色。
- **木辉光**（`{colors.wood-glow}` — #7A4E24）：径向氛围辉光色，只在右下角渐变里以 0.28 与 0.14 alpha 出现。绝不作为平涂填充。

### 默认值

- **默认表面背景**：`{colors.bg-dark}`（森林绿）。系统默认深色；奶油页是刻意的色调断口，不是常规选择。
- **深色上默认标题色**：`{colors.ink-cream}`。标题绝不出现在橙色里。
- **奶油上默认标题色**：`{colors.ink-dark}`。
- **深色上默认正文色**：`{colors.ink-cream-2}`（58% 奶油，即 `.muted` 工具类）。
- **奶油上默认正文色**：`{colors.ink-dark-2}`。
- **默认边框 / 分隔线色**：深色 `{colors.border-on-dark}`、奶油上 `{colors.border-on-cream}`。始终 1px，绝不更粗。
- **默认眉题色**：`{colors.accent-orange}`。眉题是系统的 eyebrow 标签，也是橙色最稳定出现的位置。
- **默认行内强调色**：`{colors.accent-orange}`。统计值里的 `<em>`、引文署名、图表标签都解析为橙色。
- **深色页默认氛围处理**：木棕色径向辉光（`{components.atmospheric-glow}`）始终开启。它属于深色表面本身。

橙色是标点色：它告诉眼睛结构性重点在哪，从不抢表面面积。同一页上若两处橙色挨在一起，其中一处是错的。

## 排印

### 字族

系统跑三款 Google Fonts 加 CJK 回退。**Bricolage Grotesque** 承载每个展示、h1、h2、h3、统计数字、引文文字，字重 700–800 的圆润粗壮是定义性的声部。**DM Sans** 字重 400 承载每段正文、导语、图注、项目，中性、易读，让展示字面领衔。**DM Mono** 字重 400 承载每个标签、眉题、外壳标记、页脚文字、项目破折号、图表标签，也就是一切要读成结构标记而非散文的元素。**Noto Sans SC** 是全部无衬线角色的 CJK 回退；**Noto Serif SC** 不用。

一条细微但承重的规则：**每个列表项前的破折号以暖橙的 DM Mono 渲染**，而非正文字面。等宽的字形才让这道破折号读成刻意的标记，而不是一个跑偏的标点。

本系统不用斜体作排印装饰。`<em>` 标签被改作**橙色行内强调**：统计值或引文署名里的 `<em>` 切到 `{colors.accent-orange}` 且保持直立（font-style: normal）。全套系统不存在斜体字面。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 12vw | Bricolage Grotesque | 800 | 封面或开场英雄展示，巨大，每行断成 1–2 个词 |
| `{typography.h1}` | 7vw | Bricolage Grotesque | 800 | 章节开场或收尾标题 |
| `{typography.h2}` | 4vw | Bricolage Grotesque | 700 | 内容页主标题 |
| `{typography.stat-value}` | 5.5vw | Bricolage Grotesque | 800 | 统计单元内的大数值 |
| `{typography.quote-mark}` | 8vw | Bricolage Grotesque | 800 | 暖橙装饰性起始引号字形 |
| `{typography.quote-text}` | 3.4vw | Bricolage Grotesque | 600 | 引文正文 |
| `{typography.h3}` | 2.4vw | Bricolage Grotesque | 600 | 副标题或区域标题 |
| `{typography.lead}` | 1.5vw | DM Sans | 400 | 导语段或大号项目 |
| `{typography.body}` | 1.05vw | DM Sans | 400 | 正文段落、info-card 正文 |
| `{typography.caption}` | 0.82vw | DM Sans | 400 | 图片图注、tagline、细则 |
| `{typography.label}` | 0.7vw | DM Mono | 400 | 眉题、外壳标记、页脚标签、元数据、图表标签 |

### 默认值

- **默认主分节标题**：`{typography.h2}`（4vw）。
- **默认开场或封面展示**：封面用 `{typography.display}`（12vw）；章节或收尾瞬间用 `{typography.h1}`（7vw）。
- **默认正文段落尺寸**：`{typography.body}`（1.05vw）。当段落是大标题下唯一一段辅助文字时，取 `{typography.lead}`（1.5vw）。
- **默认标签 / 眉题尺寸**：`{typography.label}`（0.7vw）。
- **任何展示元素默认字重**：700（h2）或 800（display、h1、stat-value）。
- **正文默认字重**：400。
- **默认标题字距**：负值，display -0.03em、h1 -0.025em、h2 -0.02em。负字距不可少。

拿不准时，主文字瞬间默认取 `{typography.h2}`，配一段 `{typography.lead}` 作辅助文案，这对组合是系统最稳的节奏。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **所有 display、h1、h2、h3 文字都大小写混排**，绝不全大写。本系统不存在全大写展示文字。只要落在 Bricolage Grotesque 里，就是句首大写式。
- **所有标签、眉题、外壳文字、页脚、元数据都是 DM Mono 全大写、0.12em 正字距。** 本系统不存在句首大写式的等宽。
- **眉题永远是暖橙。** 页面带眉题（标题上方的 eyebrow 标签）时，无论何种表面，颜色都是 `{colors.accent-orange}`。
- **项目列表用暖橙 DM Mono 的破折号前缀。** 绝不用圆点、对勾、数字。
- **统计数字里的 `<em>` 标签渲染成暖橙且保持直立。** 这是在数字里高亮单位后缀或某个关键数位的机制。
- **深色表面上的标题是奶油，奶油表面上的标题是深墨。** 标题绝不带橙。
- **所有 Bricolage 展示文字用负字距。** 展示用默认字距读作未处理，负值才带来压缩的高端产品气质。

### 排印原则

系统的节奏是**粗壮混排展示 + 轻混排正文 + 小号全大写等宽标签**。三者中任一模式被换掉（例如把展示全大写，或把正文做成和展示同重），都会破掉编辑语域。Bricolage 700–800 与 DM Sans 400 并置，字重差刻意拉得很开。别用 Bricolage 的中间字重（400、500）做展示瞬间，它们读起来像还没拿定主意。

斜体不用。下划线不用。正文里唯一的强调机制是橙色行内 `<em>`。唯一的结构性强调是眉题与项目破折号。

## 布局

### 画布系统

Mat **设计上就是视口流式**。所有尺寸用 `vw`、`vh` 单位，布局随视口线性缩放。幻灯片容器是 `100vw × 100vh`，文稿是一条横向 flex 条，按整屏宽度左右平移。没有固定画布尺寸，同一构图在任意近似 16:9 的视口上都能正确渲染。

### 内边距与间隙比例

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 5.5vw | 幻灯片横向内边距，左右边缘的呼吸空间 |
| `{spacing.pad-y}` | 5.5vh | 幻灯片纵向内边距 |
| `{spacing.gap-lg}` | 4.5vh | 主内容分节之间 |
| `{spacing.gap-md}` | 2.8vh | 相关元素之间（标题 → 导语、统计 → 标签） |
| `{spacing.gap-sm}` | 1.4vh | 紧密相关元素之间（外壳条里的标签对） |

横向内边距宽裕，内容大致占视口中间 89%。把内容往边缘推会破掉系统的编辑式宽绰。

### 外壳画框

多数页型顶部带 **chrome band**（`{components.chrome-band}`）、底部带 **foot band**（`{components.foot-band}`）。各是一行 `flex space-between`、两条 DM Mono 标签（通常左侧分节名、右侧页位置或分节号），由 1px 细线与正文隔开。封面、引文、收尾型页把两条都彻底隐去，这些瞬间按惯例无外壳。

### 导航外壳

一排导航点固定在底部居中（5px 圆点、低不透明度白），页码固定在右下（10px DM Mono，`rgba(255,255,255,0.25)`，格式 `01 / 09`）。这些是放映外壳，不算设计语言本身，在本库所有模板族里一致。

## 纵深与层级

### 氛围辉光（主纵深机制）

系统唯一的纵深处理是**右下角木棕色径向辉光**，经 `::before` 落在每张深色页上。伪元素占 55% 宽 × 70% 高，锚在右下角，径向渐变从 `rgba(122,78,36,0.28)` 到 `rgba(80,50,20,0.14)` 再到透明。辉光在 `z-index: 0`，所有页面内容在 `z-index: 1`。这就是纵深，没有投影、没有抬升卡片、没有文字辉光效果。

### 细线（结构分隔）

系统要分隔区域时，用**低不透明度奶油的 1px 细线**（深色表面 `{colors.border-on-dark}` 12% 不透明度，奶油表面用低不透明度深墨 `{colors.border-on-cream}` 14% 不透明度）。这些线出现在外壳条下、页脚条上、统计单元之间、比较面板之间，以及图表基线。细线绝不粗于 1px，绝不上色。

### 无阴影

任何结构元素都没有 `box-shadow` 声明。info-card 落在深色场地上不带阴影，它的材料反差来自奶油对绿的色调跳变，不是抬升。给任何组件加阴影都会破掉系统平的材料摄影美学。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0px | 每个结构元素，info-card、图片占位、统计单元、比较面板、条形 |
| 50% | 仅导航点圆 |

系统在任何组织内容上都**没有圆角**。卡片、面板、图片框都是严格矩形。唯一的圆形是导航 UI 圆点。

### 边框粗细

- **1px 实线细线**：通用结构边框。用于外壳条、页脚条、统计单元分隔、比较面板切分、图表基线、图片占位轮廓。深色表面用 `{colors.border-on-dark}`，奶油用 `{colors.border-on-cream}`。
- 不存在别的边框粗细。2px 边框会破掉系统，3px 边框属于另一个设计族。

### 装饰元素类型

**眉题**：暖橙的小号 DM Mono 全大写标签，0.12em 正字距，作为 eyebrow 标签放在标题上方。系统里橙色最稳定出现的地方。通常 0.7vw 尺寸。

**短线**：32px 宽 × 1px 高的暖橙水平强调线。作眉题与标题之间、或章节号下方的小号下划线式分隔。装饰性，非结构性。

**项目破折号**：每个项目列表的列表标记。渲染成暖橙 DM Mono 的 `—`，经 CSS 网格标记列（`grid-template-columns: 1.4em 1fr`）前置到列表项。系统的项目声部。

**info-card**：深色页上的奶油内嵌矩形（`{components.info-card}`）。承载一个标题（h3 级、深墨）和一段正文块（body 级、柔化深墨）。系统里最鲜明的组件，用来拿一块暖纸刺破绿色场地。无边框、无阴影、无圆角，光靠色调跳变定义边界。

**统计单元**：纵向分隔的单元，上方一个大数值（`{typography.stat-value}`），下方一行标签（柔化奶油的 `{typography.body}`）。单元三个一组排开，以 1px 右边框分隔（末个单元无右边框）。数值支持橙色行内 `<em>` 作单位后缀（如 `4.7k` 里的后缀）。

**引号标记**：`{typography.quote-mark}` 尺寸的暖橙超大起始引号字形。坐在引文文字上方作排印装饰。只在引文页型里用。

**比较分隔线**：两个并排面板之间 1px 宽的 CSS 竖列（不是边框）。刻意低调，视觉工作由两面板的反差承担，不靠分隔线。

**图片占位**：空矩形，1px 细线边框、6% 奶油底、居中 DM Mono 标签写占位名。在放进真实照片前使用。占位色刻意贴近背景，图片区域不该自我宣告。

## 该做与不该做

### 该做
- 用深森林绿（`{colors.bg-dark}`）作默认幻灯片背景。系统深色优先，奶油页是色调断口，不是默认。
- 给每张深色页套木棕色氛围辉光。它属于表面，不是可选的点缀。
- 把 Bricolage Grotesque 混排展示与 DM Mono 全大写标签配对。两款字面的大小写反差就是系统的排印节奏。
- 深色上标题用奶油（`{colors.ink-cream}`），奶油上用深墨（`{colors.ink-dark}`）。标题绝不承载橙色强调。
- 用暖橙（`{colors.accent-orange}`）作眉题色、项目破折号色、行内 `<em>` 色。橙色是标点，绝非表面。
- 页面需要在绿色场地上嵌一块暖纸时，用奶油 info-card（`{components.info-card}`），系统的招牌材料反差手法。
- 让页面保持中等偏疏。一个主标题、一段辅助文字、可选一列 3–5 条短项目，就是对的密度。
- 每条结构分隔都用低不透明度奶油或深墨的 1px 细线。边框绝不更粗。
- 每个项目列表都用 DM Mono 的破折号前缀。绝不换成圆点、对勾或数字。
- 把数值里的 `<em>` 渲染成暖橙、font-style normal，单位后缀与强调数位在本系统里就这么读。

### 不该做
- 不要把任何 Bricolage 展示、h1、h2、h3 文字全大写。展示文字始终大小写混排。全大写专属于 DM Mono 标签。
- 不要引入第二种强调色。系统只有一种强调（暖橙），这个角色不能分给别人。
- 不要给任何组件加投影、模糊阴影或抬升效果。纵深只有氛围辉光。
- 不要给任何结构元素加圆角。卡片、面板、图片框、条形，都是严格矩形。只有导航点圆是圆的。
- 不要用三栏项目填满一页，也不要纵向堆五个区域。Mat 一挤就读作坏了。
- 不要把橙色当背景填充。橙色只作行内。
- 不要在任何地方用衬线字面。系统里没有衬线，圆润怪诞体承载每个编辑瞬间。
- 不要给 info-card 加边框。奶油与森林绿之间的色调跳变定义边界，加边框会破掉平的材料读感。
- 不要用斜体字形。`<em>` 标签被改作橙色行内换色，并保持直立。
- 不要把边框粗细加到 1px 以上。2px 边框会破掉系统的细线语言。

## 响应式行为

Mat 以流式 `100vw × 100vh` 视口为目标，每个排印尺寸、内边距、间隙都用 `vw`/`vh` 单位。同一构图在 1280×720、1920×1080、2560×1440 上无需断点都能正确渲染。所有尺寸都相对视口，内容线性缩放，视口越宽文字与内边距同比放大，视觉密度保持恒定。

### 放映行为
- 右 / 下方向键 / 空格前进到下一页。
- 左 / 上方向键后退。
- Home 跳到首页，End 跳到末页。
- 触屏横向滑动在移动端前进 / 后退。
- 鼠标滚轮以前进，配 1000ms 防抖，防止误连跳。
- 幻灯片作为单条 flex 横向平移，过渡 0s（文稿设为即时导航，不做动画过渡，`--dur-slide` token 设为 `0s`）。

### 打印行为
模板没有声明 `@media print` 规则。要出 PDF，用浏览器的截图或打印工具；多页 PDF 导出需逐页手动触发。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 中文字面 | 字重 | 理由 |
|---|---|---|---|
| 展示 / h1 / h2 / h3 / stat-value（Bricolage 角色，2.4–12vw） | 思源宋体 Noto Serif SC | 700 | 明朝体粗字重提供 Bricolage 700–800 在拉丁里的结构分量，同时保住暖材料语域 |
| 引文文字 / 引号标记（3.4vw / 8vw） | 思源宋体 Noto Serif SC | 600–700 | 编辑瞬间沿用同一明朝声部 |
| 导语 / 正文 / 图注（DM Sans 角色，0.82–1.5vw） | 思源宋体 Noto Serif SC | 400 | 明朝正文声部，平静、材料感，与木辉光的暖意相配 |
| info-card 正文 / 标题 | 思源宋体 Noto Serif SC | 400 / 600 | 在中文里维持暖纸压绿的对比 |
| 标签 / 眉题 / 外壳 / 页脚（DM Mono 角色，0.7vw） | 思源宋体 Noto Serif SC | 500 配 0.05em 字距 | 替换 DM Mono，中文没有读成编辑外壳的等宽传统 |

### 混排策略

用**策略 A**：把整条字面栈在所有角色上切到 Noto Serif SC，替换 Bricolage Grotesque（展示）、DM Sans（正文）、DM Mono（标签）。Mat 的身份不依赖具体的拉丁字面，它依赖**带木棕氛围辉光的深森林绿画布**、**单一暖橙强调**、**奶油 info-card 内嵌**、**1px 细线分隔语言**。中文全用明朝能干净地保住以上每一条身份标记，又不会引入策略 C 在视口流式系统上的基线抖动。字体栈：

```css
/* Bricolage roles (display, h1, h2, h3, stat-value, quote) */
font-family: 'Bricolage Grotesque', 'Noto Serif SC', sans-serif;
/* DM Sans roles (lead, body, caption) */
font-family: 'DM Sans', 'Noto Serif SC', sans-serif;
/* DM Mono roles (label, kicker, chrome, footer) */
font-family: 'DM Mono', 'Noto Serif SC', monospace;
```

系统源码当前把 `'Noto Sans SC'` 列为 CJK 回退，为 Mat 的材料触感语域，**换成 `'Noto Serif SC'`**。明朝字面暖的字形比几何的 Noto Sans SC 更贴木辉光 / 森林绿氛围，后者对这套系统读起来太现代、太临床。

### 加载

把既有的 Noto Sans SC 链接换成 Noto Serif SC：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

以下调整适用于本系统**每一个 CJK 块**，无论尺寸或角色：

- **行高放宽 0.05–0.08。** CJK 字形是全宽方块，视觉分量比拉丁字母重，为拉丁调的行高（展示 0.88–1.1、正文 1.5–1.65）在中文里读起来局促。展示提到 1.0–1.2，正文提到 1.7–1.85。
- **去掉 CJK 标题的负字距。** Bricolage 展示用 -0.025em 到 -0.03em 字距，会把汉字撞在一起。CJK 段设 `letter-spacing: 0`，标题看着挤时可用微小正值 `0.02em`。
- **绝不对 CJK 文字用 `text-transform: uppercase`。** 中文没有大小写，CSS 属性对汉字无效，却会悄悄破坏混排行里本该大写的 DM Mono 部分。（这点在这里要紧：每个 DM Mono 标签、眉题、外壳条、页脚都是 `text-transform: uppercase`。）
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不用拉丁对应物（`,.:;!?""''()`）。同一句里混用标点系统读起来是排印错误。
- **CJK 标题末尾不加句号（。）。** 中文标题与拉丁遵循同一规则，标题式行去掉末尾标点。正文段落保留 。
- **在 CJK 与拉丁串交界处套用盘古之白。** 汉字与相邻拉丁词或数字之间应有一个空格（或 0.25em 外边距），例如 `2026 年 5 月` 而非 `2026年5月`。要么手打空格，要么用 `pangu.js` 式自动加空格器。
- **一句一款字体。** 不要在同一句里切换 Noto Serif SC 字重 400、500、700，挑与角色匹配的字重（标题 = 700、正文 = 400、标签 = 500），整段从一而终。

### 本系统的美学提示

Mat 的整个声部是"工业设计作品集遇上精品产品发布"：深森林绿配木棕辉光、奶油文字浮在场地上、暖橙作唯一强调。中文里系统的身份不依赖 Bricolage / DM Sans / DM Mono 三件套，它依赖**环境氛围**（每张深色页上的径向木辉光）、**单强调纪律**（橙色只作眉题、破折号项目、行内强调）、**奶油 info-card** 这个招牌材料反差手法。这些都不用改动就能迁移。

暖橙破折号项目在中文里同样成立，破折号字符（—）在任何文字里都是同一个字形，暖橙 Noto Serif SC 字重 500 前置到中文列表项前，读起来就和拉丁里一样是一个刻意的标记。项目列保持在 Noto Serif SC 字重 500（替换 DM Mono），明朝字面的暖意比无衬线外壳字面更贴系统的材料触感语域。

Bricolage "始终混排、绝不全大写" 这条规则在中文里很有意思：中文没有大小写，规则自动满足。但系统对标签的全大写规则（DM Mono 0.12em 字距）迁移不过来；中文里标签应是 **Noto Serif SC 字重 500 配 0.05em 正字距**，不要 `text-transform`。正字距靠字重与间距独自撑起外壳质感。

`<em>` 行内橙色规则（统计数字里的单位后缀）在中文里成立：中文单位字如「万」或「亿」放进 `<em>`，渲染成暖橙并保持直立，精确镜像拉丁式样。照同样方式用：`4.7<em>万</em>` 对应 `4.7 万 (47k)`。

### 已知 CJK 缺口

Bricolage Grotesque "粗壮、圆润、带机械气质的怪诞体" 是 Mat 在拉丁里最鲜明的排印手法之一，正是它给系统带来工业产品页的声部。中文没有精确对应：Noto Serif SC 字重 700 有结构分量，却比 Bricolage 的圆润现代读起来更传统、更文学。中文渲染会丢掉一部分工业设计气质，由木辉光氛围与暖橙强调多担一些个性工作来部分补偿。对工业语域吃紧的文稿（例如专讲硬件或材料设计的产品发布稿），可考虑在最大的展示瞬间（封面、英雄）仅补**思源黑体 Noto Sans SC 字重 800**：Noto Sans SC 800 的几何厚重比 Noto Serif SC 更接近 Bricolage Grotesque 800。省着用，好让别处保住文学材料语域。

## 迭代指南

1. 任何新组件都作为奶油文字落在深色表面上，除非是 info-card 手法（奶油压绿色调反差），否则不套卡片、面板或画框。
2. 任何新标题都用 Bricolage Grotesque 混排、字重 700（h2）或 800（display/h1）。展示别去取字重 500。
3. 任何新结构分隔都是低不透明度奶油或深墨的 1px 细线。绝不用更粗或上色的边框。
4. 任何新标签、eyebrow、标记、元数据文字都用 DM Mono 全大写、0.12em 字距。本系统不存在混排等宽。
5. 任何新项目列表都用暖橙 DM Mono 的破折号前缀。标记字面与颜色不可商量。
6. 任何新强调瞬间（高亮数字、强调词、眉题）都用暖橙。不要引入第二种强调。
7. 任何新深色页都在 `::before` 上带氛围辉光。若自定义页面布局，复刻这个伪元素，否则页面读起来是平的。
8. 页面需要一块暖纸来锚定（CTA、小结、署名块）时，用 info-card。别另造一套平行卡片式样。
9. 色调断口页（奶油背景）整套文稿用一次作强调，不作深色的常规替代。系统读作深色默认。

## 已知缺口

- `--c-bg-dark-alt`（#2E3D30）变量为略浅的绿表面而定义，但没有任何选择器在用它。预留给未来的分层区域工作。
- 氛围辉光经 `::before` 伪元素硬编码在右下角。改位置要直接编辑 CSS 规则，没有辉光位置或强度的 token。
- 系统加载四款 Google Fonts（Bricolage Grotesque、DM Sans、DM Mono、Noto Sans SC），渲染一致性取决于这些字体能否加载。CJK 回退栈覆盖中文，但日文与韩文字形回退到系统衬线 / 无衬线。
- 幻灯片过渡时长设为 `0s`（即时）。`--ease-slide` 与 `--dur-slide` token 为动画而存在但闲置；文稿需要动画过渡时，必须提高 duration 值。
- 竖向条形图在每根条填充上用内联 `style="height: XX%"` 声明。没有数据绑定层，条高需手工计算。
- `.split-center` 图片区域固定为 52vh 高。高竖幅图片可能需要布局级覆盖。
- 导航点与页码用硬编码 `rgba(255,255,255,...)` 值，不适配奶油页变体，在奶油页上白点读起来发灰。
