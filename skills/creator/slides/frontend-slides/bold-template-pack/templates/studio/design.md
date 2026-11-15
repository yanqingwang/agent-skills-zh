---
version: alpha
name: Studio
description: "A \"Boring Studios\" agency presentation system — type-as-graphic-mass in the spirit of contemporary design-studio decks (Pentagram, Anti, Order). The entire system runs on Barlow at weight 900 uppercase, with type so heavy at display scale that it stops being type and starts being a shape. The palette is binary plus one: near-black field (#1C1C1C), acid yellow type (#F5D200), and the same yellow as a full slide background. IBM Plex Mono carries every footer metadata, slide counter, and three-column lockup. No drop shadows, no rounded corners, no accent colors — the headline IS the design, and the only chromatic decision per slide is dark-yellow-on-near-black or near-black-on-acid-yellow."

colors:
  near-black: "#1C1C1C"
  near-black-alt: "#242422"
  acid-yellow: "#F5D200"
  acid-yellow-alt: "#F0CC00"
  text-on-dark-2: "rgba(245,210,0,0.58)"
  text-on-dark-3: "rgba(245,210,0,0.32)"
  text-on-light-2: "rgba(28,28,28,0.62)"
  text-on-light-3: "rgba(28,28,28,0.35)"
  border-dark: "#2E2E2C"
  border-light: "rgba(28,28,28,0.18)"

color-aliases:
  c-bg: near-black
  c-bg-alt: near-black-alt
  c-bg-light: acid-yellow
  c-bg-light-alt: acid-yellow-alt
  c-fg: acid-yellow
  c-fg-light: near-black
  c-accent: acid-yellow
  c-fg-2: text-on-dark-2
  c-fg-3: text-on-dark-3
  c-fg-light-2: text-on-light-2
  c-fg-light-3: text-on-light-3

typography:
  display:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 12vw
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.02em
    textTransform: uppercase
  h1:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 7.5vw
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: -0.02em
    textTransform: uppercase
  h2:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 4.8vw
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -0.01em
    textTransform: uppercase
  h3:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 2.8vw
    fontWeight: 700
    lineHeight: 1.1
    textTransform: uppercase
  quote-text:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 3.8vw
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -0.02em
    textTransform: uppercase
  stat-value:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 5.5vw
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.03em
    textTransform: uppercase
  lead:
    fontFamily: "Barlow, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.6vw
    fontWeight: 500
    lineHeight: 1.45
  body:
    fontFamily: "Barlow, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.15vw
    fontWeight: 400
    lineHeight: 1.6
  caption:
    fontFamily: "Barlow, Noto Sans SC, system-ui, sans-serif"
    fontSize: 0.85vw
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "IBM Plex Mono, monospace"
    fontSize: 0.72vw
    fontWeight: 500
    letterSpacing: 0.06em

spacing:
  pad-x: 5vw
  pad-y: 5vh
  gap-lg: 3.5vh
  gap-md: 2vh
  gap-sm: 1vh

canvas:
  width: 100vw
  height: 100vh

components:
  chrome-bar:
    borderBottom: "1px solid {colors.border-dark} (or {colors.border-light} on yellow)"
    paddingBottom: "{spacing.gap-sm}"
    marginBottom: "{spacing.gap-md}"
    description: "Top chrome bar — mono label left, mono counter right, hairline rule beneath."
  foot-bar:
    borderTop: "1px solid {colors.border-dark} (or {colors.border-light} on yellow)"
    paddingTop: "{spacing.gap-sm}"
    marginTop: "{spacing.gap-md}"
    description: "Bottom chrome bar — mirror of chrome-bar."
  cover-meta:
    display: "grid 1fr 1fr 1fr"
    borderTop: "1px solid rgba(245,210,0,0.25)"
    description: "Three-column mono metadata footer over the cover image: studio × client + date, presentation title (center), studio name (right). The signature 'Boring Studios' lockup."
  stat-card:
    borderTop: "2px solid (acid-yellow on dark, near-black on yellow)"
    padding: "{spacing.gap-md} {spacing.gap-md} {spacing.gap-md} 0"
    description: "Stat tile with a 2px top rule. Value at 5.5vw weight 900 in the surface's foreground color; label and mono note beneath."
  bullet-marker:
    content: "—"
    color: "acid-yellow on dark, near-black on yellow"
    fontFamily: "{typography.body.fontFamily}"
    description: "Em-dash bullet prefix on every list item; color follows the surface accent."
  compare-divider:
    borderRight: "2px solid (near-black on yellow, dark-text-3 on dark)"
    description: "Single vertical 2px rule separating two compare panels."
  bar-fill-default:
    background: "muted text-on-surface (dark-text-3 or light-text-3)"
    description: "Default chart bar fill — muted version of the surface text color."
  bar-fill-accent:
    background: "acid-yellow on dark, near-black on yellow"
    description: "Highlighted chart bar — the surface's primary foreground color."
  chart-baseline:
    height: "2px"
    background: "muted accent (dark-text-3 or border-light)"
    description: "Heavier 2px baseline beneath chart bars — Studio uses thicker rules than Signal."
  cover-img-area:
    position: "absolute inset 0"
    background: "{colors.near-black-alt}"
    description: "Cover image placeholder filling the entire slide behind the cover-type and cover-meta. Image-or-placeholder occupies the whole canvas; type sits on top."
  img-placeholder:
    background: "near-black-alt on dark, acid-yellow-alt on yellow"
    description: "Warm-toned rectangular placeholder for images, centered mono label inside, no border on dark / hairline border on yellow."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/studio/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Studio 是一套**文字即图形质量块**的演示系统，是当代设计工作室文稿的视觉语域（Pentagram、Anti、Order、"Boring Studios" 事务所美学）。前提精简到近乎严苛：单一字面（Barlow）、单一字重（900）、严格全大写，尺度大到文字不再像文字、开始像一个图形形状。标题*就是*设计，没有装饰元素、没有强调色、没有纹样。若把 Studio 页上其余元素全去掉、只留标题，那页仍读作 Studio。

配色是**二元加一**。深色表面是 `{colors.near-black}`（#1C1C1C），一种暖深，不是冷中性。浅色表面是 `{colors.acid-yellow}`（#F5D200），一种饱和镉黄，填满整页，不是强调而是环境。深色页上文字是 `{colors.acid-yellow}`，黄页上文字是 `{colors.near-black}`。这就是整套色彩系统：深 / 黄、黄 / 深。没有次级色、没有灰、没有暖强调。连柔化文字也只是同色降低不透明度（黄 58%、近黑 62%）。

字体栈是**功能而非表现**。Barlow 字重 900 承载每个尺度上的每个标题，从 1.15vw 正文一路到 12vw 封面展示。Barlow 500 承载正文与导语段。IBM Plex Mono 承载元数据页脚、页码、三栏封面锁定，是系统里唯一出现第二款字面的地方。等宽是系统的"规格表"声部，别处一律由 Barlow 主导。

纵深是**扁平而严苛**。没有投影，没有圆角，没有渐变。边框是 `{colors.border-dark}` 或 `{colors.border-light}` 的 1px 或 2px 细线。2px 图表基线与 2px 统计卡顶线是系统里最重的线。系统读作建筑图纸或宣言海报，每条线都有意，无一处装饰。

**密度取向：低而刻意。** Studio 按设计就稀疏。陈述页是一条标题填满大半画布，上下留空。章节页是一条小等宽标签加一条标题。封面是图片占位后压一个 12vw 的单词。内边距比 Signal 更紧（5vw / 5vh 对 7.5vw / 5.5vh），因为文字本身就快跑到边缘，标题是空间填充，不是页边距。在 Studio 里读着别扭的页，是含多个互相竞争的元素、或把画布填满正文段的页。对的语域是"一件巨大的事，说一次，用 900 字重全大写"。

**关键特征：**
- 二元配色，`{colors.near-black}` 场地配 `{colors.acid-yellow}` 文字，或 `{colors.acid-yellow}` 场地配 `{colors.near-black}` 文字。无第三种颜色。
- Barlow 字重 900 全大写用于每个尺度上的每个标题，Barlow 400/500 用于正文，IBM Plex Mono 仅用于元数据外壳。
- 标题跑得极大，封面展示 12vw（1920px 视口下约 230px）、陈述 7.5vw、分节头 4.8vw。
- 所有展示文字紧负字距（-0.01 到 -0.03em），全大写不可商量。
- 扁平：无投影、无圆角、无渐变、无黄 / 深二元之外的强调色。
- 外壳上 1px 细线边框，统计卡顶、图表基线、比较面板分隔用 2px。
- 封面页三栏等宽元数据页脚是系统的招牌锁定（studio × client / 演示标题 / 工作室名）。
- 表面强调色的破折号项目标记（深底黄、黄底近黑）。
- 正文与外壳是同色的不透明度调节版（黄 58%/32%、近黑 62%/35%），绝不是单独的灰色。

## 颜色

### 调色板

- **近黑**（`{colors.near-black}` — #1C1C1C）：深色表面。暖深，略偏棕而非冷中性。系统的"墨"。
- **近黑 Alt**（`{colors.near-black-alt}` — #242422）：勉强抬起的近黑，用于图片占位与次级深色表面。视觉上与近黑几近一致。
- **酸性黄**（`{colors.acid-yellow}` — #F5D200）：浅色表面，同时是深色表面上的主文字色。镉黄，饱和、略暖。深色页上它是文字色，浅色页上它是背景。同色两角。
- **酸性黄 Alt**（`{colors.acid-yellow-alt}` — #F0CC00）：略冷的黄，用于浅色页上的相邻表面区分。省着用。
- **深底文字 2**（`{colors.text-on-dark-2}` — rgba(245,210,0,0.58)）：深色上次级文字，58% 不透明度的黄。系统绝不用单独的"灰"色，柔化只靠不透明度。
- **深底文字 3**（`{colors.text-on-dark-3}` — rgba(245,210,0,0.32)）：深色上三级文字，32% 的黄。
- **浅底文字 2**（`{colors.text-on-light-2}` — rgba(28,28,28,0.62)）：黄上次级文字，62% 的近黑。
- **浅底文字 3**（`{colors.text-on-light-3}` — rgba(28,28,28,0.35)）：黄上三级文字，35% 的近黑。
- **深色边框**（`{colors.border-dark}` — #2E2E2C）：深色表面上的细线边框色。比近黑略抬起，好读作一条线而非一片虚空。
- **浅色边框**（`{colors.border-light}` — rgba(28,28,28,0.18)）：黄表面上的细线边框色。低不透明度近黑，作细微分隔。

### 默认值

- **默认表面**：整套文稿在 `{colors.near-black}`（深）与 `{colors.acid-yellow}`（浅）间交替。两个表面都是一等。拿不准时，封面 / 引文 / 陈述页取近黑，章节与收尾页取酸性黄。
- **深色上默认主文字**：`{colors.acid-yellow}`。
- **黄上默认主文字**：`{colors.near-black}`。
- **深色上默认次级文字**：`{colors.text-on-dark-2}`（58% 不透明度的黄）。
- **黄上默认次级文字**：`{colors.text-on-light-2}`（62% 的近黑）。
- **默认三级文字**（等宽图注、图表轴标签、统计注）：表面强调色的三级不透明度。
- **深色上默认边框**：`{colors.border-dark}`。
- **黄上默认边框**：`{colors.border-light}`。
- **默认标题色**：表面强调色，深底黄、黄底近黑。绝不别的颜色。
- **默认图表强调填充**：表面强调色（深底黄、黄底近黑）。"高亮"条就是主文字色，"默认"条是三级柔化。

没有语义颜色角色。黄不表"警告"，近黑不表"主"。它们只是两个表面。二者之间的选择是节奏性的，交替着变视觉节拍，或连跑几张深色页作安静段落、再用单张黄页作标点瞬间。

## 排印

### 字族

Studio 以严格分开的角色跑**两款字族**：

- **Barlow**（`{typography.display.fontFamily}`）：当代怪诞体，字重轴宽。承载每个尺度上的每个标题（display 到 h3）、每个数字（stat-value）、每条引文、全部正文、全部导语段。系统用字重 900 给全部展示与标题 token，字重 700 给 h3，字重 500 给导语与项目标记，字重 400 给正文与图注。
- **IBM Plex Mono**（`{typography.label.fontFamily}`）：精密等宽。**仅**用于元数据标签，外壳条、页码、章节号、三栏封面锁定、统计注、cover-meta 内的等宽图注。等宽是系统的"元数据声部"，别处一律由 Barlow 主导。

情绪分工是二元的：Barlow 作内容（响、全大写、主导），IBM Plex Mono 作规格表元数据（小、精密、支撑）。没有第三款字面。

Barlow 字重 900 在展示尺度上不再像一款字面、而开始像一个图形形状，字形重到字腔（字母里的洞）变成结构性负空间，标题在读作词之前先读作一块黑或黄的几何块。这就是系统的身份。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 12vw | Barlow | 900 | 最大尺度的封面英雄 |
| `{typography.h1}` | 7.5vw | Barlow | 900 | 章节标题、满页陈述标题 |
| `{typography.stat-value}` | 5.5vw | Barlow | 900 | 统计卡里的统计数字 |
| `{typography.h2}` | 4.8vw | Barlow | 900 | 页面主标题 |
| `{typography.quote-text}` | 3.8vw | Barlow | 900 | 引文正文（全大写，无引号） |
| `{typography.h3}` | 2.8vw | Barlow | 700 | 副标题、面板标题 |
| `{typography.lead}` | 1.6vw | Barlow | 500 | 导语段、开场句 |
| `{typography.body}` | 1.15vw | Barlow | 400 | 默认正文段、项目正文 |
| `{typography.caption}` | 0.85vw | Barlow | 400 | 图注、来源归属 |
| `{typography.label}` | 0.72vw | IBM Plex Mono | 500 | 等宽外壳、页码、章节号、统计注、cover-meta |

### 默认值

- **主分节标题默认尺寸**：`{typography.h2}`（4.8vw）。
- **章节或陈述标题默认尺寸**：`{typography.h1}`（7.5vw）。
- **封面英雄默认尺寸**：`{typography.display}`（12vw）。
- **段落正文默认尺寸**：`{typography.body}`（1.15vw）。
- **导语句默认尺寸**：`{typography.lead}`（1.6vw）。
- **任何外壳标签、计数器、等宽图注默认尺寸**：`{typography.label}`（0.72vw）。
- **统计数字默认尺寸**：表面强调色的 `{typography.stat-value}`（5.5vw）。
- **任何标题默认字重**：900。
- **任何正文元素默认字重**：400（导语 = 500）。

尺寸间拿不准时，偏大。Studio 的身份依赖文字跑得巨大，4.8vw h2 读作系统，把 2.8vw h3 当主标题读作另一套系统。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每个 display、h1、h2、h3、quote-text、stat-value 都全大写。** 句式展示文字不存在。连 h3（2.8vw、字重 700）也跑全大写。
- **每个展示标题都用字重 900。** display、h1、h2、quote-text、stat-value 全是字重 900，无例外。展示尺度用字重 800 或 700 会破掉文字即图形质量块的效果。
- **每个展示元素都用负字距。** display -0.02em、h1 -0.02em、h2 -0.01em、stat-value -0.03em。不带负字距的展示 Barlow 900 读作未处理，负字距才给文字压缩的密度。
- **所有外壳、标签、计数器、元数据都是 0.06em 字距的 IBM Plex Mono。** 无例外。用 Barlow 排的等宽标签会破掉元数据 / 内容分离。
- **标题始终以表面强调色渲染**，深底黄、黄底近黑。绝不柔化不透明度、绝不别的颜色。
- **正文项目用表面强调色的破折号**，绝不用圆点、绝不用别的字形。破折号带随表面切换的颜色（深底黄、黄底近黑）。
- **统计卡有 2px（而非 1px）顶线**，用表面强调色（深色侧为柔化强调）。2px 线比外壳细线重，因为统计是锚点。
- **三栏 cover-meta 锁定用 IBM Plex Mono，第 1 栏左对齐、第 2 栏居中、第 3 栏右对齐。** 这是 "Boring Studios" 招牌，栏结构不可商量。

### 排印原则

字族阶梯固定：除元数据外一切都用 Barlow，元数据只用 IBM Plex Mono。元数据角色之外用等宽、或元数据角色里用 Barlow，都会破掉排印分离。

字重阶梯也固定：900 / 700 / 500 / 400。中间字重（600、800）不用。这四级字重系统就是排印的全部表现语域。

行高在展示尺度上紧（display 0.9、h1 0.92），正文放开到 1.5–1.6。字距在展示上统一为负（–0.01 到 –0.03em）、正文为零、等宽标签为正 0.06em。

斜体不用。下划线不用。系统里没有 font-style 变化，强调纯靠字重反差（900 标题对 400 正文）。

## 布局

### 画布系统

Studio 以 `100vw × 100vh` 满视口为目标。每张 `.slide` 以 flex 精确铺满视口，页并排坐在一条横向条里，导航时左右平移。所有尺寸用视口相对单位（`vw`、`vh`），布局流式缩放。

### 内边距与间隙比例

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 5vw | 幻灯片横向内边距 |
| `{spacing.pad-y}` | 5vh | 幻灯片纵向内边距 |
| `{spacing.gap-lg}` | 3.5vh | 主内容分节之间 |
| `{spacing.gap-md}` | 2vh | 相关元素之间 |
| `{spacing.gap-sm}` | 1vh | 紧密耦合元素之间 |

陈述与章节页把底部内边距提到 pad-y 的 1.5×，让标题落到页面下部、上方留刻意的空白。封面页用零外内边距，因为图片区填满整块画布。

### 外壳画框

标准页带顶部外壳条与底部页脚条：

- **外壳条**：左对齐等宽标签、右对齐等宽计数器，下方 1px 细线。padding-bottom 是 `{spacing.gap-sm}`，margin-bottom 是 `{spacing.gap-md}`。
- **页脚条**：左对齐等宽标签、右对齐等宽计数器，上方 1px 细线。外壳条的镜像。

封面、章节、陈述、引文、收尾页省掉标准外壳，那些布局要么用 cover-meta 锁定（封面），要么什么都不用（章节、陈述、引文、收尾）。

### 封面锁定

封面页是系统的招牌布局：
- 一个图片占位填满整块画布、压在一切背后。
- 一条展示标题（典型一个 12vw 的单词）以 `cover-type` 坐在上部区域。
- 底部一条三栏等宽元数据页脚，第 1 栏左（"studio × client" + 日期）、第 2 栏中（演示标题）、第 3 栏右（工作室名），由一条 25% 不透明度黄的 1px 细线与图片区隔开。

## 纵深与层级

Studio **按设计是扁平的**。没有投影，没有圆角卡片抬升，没有渐变。每个元素都与表面齐平。

表观纵深来自：
- **表面反差**：近黑对酸性黄同现时（比较面板、图片占位）。
- **细线分隔**：1px 与 2px 边框划分区域。
- **厚重文字**：字重 900 的展示标题造出视觉质量块，在扁平表面上读作前景。

系统刻意严苛。布局若需要抬升才能读对，那布局对 Studio 就是错的，减少内容或重组，让扁平表面 + 厚重文字 + 细线提供足够层级。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0 | 系统里的一切 |
| 50%（圆） | 仅导航点与页码 UI（不属于页面内容） |

Studio **没有圆角外壳**。卡片、面板、统计块、图表框、图片占位、比较面板，全是带尖角的严格矩形。仅有的圆形是导航点与底层页码 UI，它们是 deck-stage 外壳，不是页面内容。

### 边框粗细

- **1px 实线**，`{colors.border-dark}`（近黑上）或 `{colors.border-light}`（黄上）：通用细线。用于外壳条、页脚条、cover-meta 分隔。
- **2px 实线**，表面强调色（深底黄、黄底近黑）：较重的线。用于统计卡顶线、比较面板竖分隔、图表基线、图表条轨道左线。
- **无虚线边框。** 系统里每条边框都是实线。

### 装饰元素类型

**展示标题即图形质量块**：展示尺度（4.8vw 及以上）字重 900 的 Barlow 坐成一块黑或黄的几何块。标题是每页的主装饰元素，没有额外纹样。

**细线**：表面边框色的 1px 实线。用于隔开外壳与正文、正文与页脚，以及比较面板内部。这条线是系统唯一的结构分隔。

**重线**：表面强调色（或柔化强调）的 2px 实线。用于统计卡顶、图表基线、比较面板竖分隔。比外壳细线重，读作"锚"而非"分隔"。

**统计卡**：扁平区域，带 2px 顶线、表面强调色的统计数字（5.5vw Barlow 900）、统计标签（1.15vw Barlow 500）、可选等宽统计注（0.85vw IBM Plex Mono、三级不透明度）。内边距给右与下，左内边距为零（线从卡片左边缘齐平起）。

**Cover-meta 锁定**：封面页底部的三栏等宽页脚。第 1 栏：第 1 行 studio × client 名、第 2 行日期。第 2 栏：演示标题（居中）。第 3 栏：工作室名（右对齐）。由一条 25% 不透明度黄的 1px 细线与 cover-type 隔开。

**图片占位**：扁平矩形，深色上填 `{colors.near-black-alt}`、黄上填 `{colors.acid-yellow-alt}` 配细线边框，内含三级不透明度居中的 IBM Plex Mono 文字。用于尚未填充的图片槽位。

**图表条**：扁平竖矩形，用柔化的表面文字色（默认）或表面强调色（高亮）。无圆端、无渐变。"hi" 变体用全强调色，数值标签上字重 900。

**图表基线**：柔化表面强调色（深色上黄三级、黄上 border-light）的 2px 实线，横贯图表包装器全宽，在条顶之下。

**破折号项目**：每个列表项前置表面强调色的 `—`，配 0.5em 右外边距。颜色随表面翻转。

## 该做与不该做

### 该做

- 每个尺度上的每个标题都用字重 900 全大写 Barlow，至少 -0.01em 负字距。文字即图形质量块的效果是系统身份。
- 自由交替 `{colors.near-black}` 与 `{colors.acid-yellow}` 表面。两者都是一等，深 / 黄交替的节奏就是系统的节拍。
- 每个标题都着表面强调色，深底黄、黄底近黑。绝不柔化版、绝不第三种颜色。
- IBM Plex Mono 只用于元数据（外壳标签、页码、章节号、cover-meta 锁定、统计注、等宽图注）。等宽是规格表声部，绝不用于内容。
- 把 cover-meta 页脚渲染成三栏等宽锁定（左 / 中 / 右）。这是系统的招牌式样。
- 用不透明度柔化次级文字（黄 .58、近黑 .62），而非单独的灰色。系统没有灰，只有黄与近黑的不透明度变体。
- 给统计卡顶、图表基线、比较面板分隔套 2px 线。2px 粗细把"锚"元素与外壳细线区分开。
- 用表面强调色的破折号作项目标记，绝不用圆点、绝不用圆圈。
- 页面内边距留紧（5vw / 5vh），让展示文字跑到近边缘。Studio 依赖文字填满画布，宽裕内边距会破掉尺度效果。
- 让陈述与章节页刻意稀疏。一条巨大标题对空表面，是那些页型对的语域。

### 不该做

- 不要把标题小写。每个 Barlow 900 元素都跑全大写，无例外。
- 不要在展示尺度用字重 800 或 700。展示 = 始终字重 900。
- 不要给调色板加第三种颜色。系统是二元加不透明度变体，加红、蓝或任何强调都会破掉二元逻辑。
- 不要给任何角加圆角。处处严格矩形，只有导航点是圆。
- 不要加投影或渐变。系统严苛扁平，纵深来自反差与字重，不来自抬升。
- 不要用 Barlow 排外壳元数据。等宽是元数据声部，Barlow 外壳读作内容而非规格。
- 不要用等宽排标题或正文。等宽只活在元数据角色里。
- 不要加斜体、下划线或换色变体作强调。唯一的强调机制是字重反差（900 对 400）。
- 不要引入虚线边框。系统里每条线都是实线。
- 不要让内容填满典型一页超过约 60%。空表面是结构性的，Studio 一挤就读作坏了。

## 响应式行为

Studio 以 1920×1080 视口为目标、通篇用视口相对单位（`vw`、`vh`），于是在 1280×720 与 2560×1440 间无需断点便流式缩放。除 deck 外壳圆点与页码外没有固定像素度量。

### 缩放行为

- 展示标题缩放：12vw → 1920px 视口下约 230px，1280px 下约 154px。
- 正文缩放：1.15vw → 1920px 下约 22px，1280px 下约 15px。
- 内边距缩放：pad-x 5vw → 1920px 下约 96px，1280px 下约 64px。

2px 与 1px 边框粗细是固定像素尺寸、不缩放，视口大时边框在比例上显得更细。

### 放映行为

文稿由 JS 驱动，页并排坐在一条横向条里，导航时左右平移。当前页带 `is-active`，触发任何 `[data-anim]` 元素入场。动画比 Signal 更锐更短（0.5s 时长对 0.65s，0.75s 平移对 0.85s），按源码注释是"事务所的急迫，不是编辑的从容"。动画关键帧含 fade-up、fade-in、reveal-right、reveal-left、scale-in，配错峰 `data-delay`（0–6）。

导航点与页码固定在视口底部，是刻意低调的深底白小 UI。

### 打印行为

没有内嵌打印样式表。横向条布局需为静态导出解开。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字面（默认） | 中文字面 | 字重 | 说明 |
|---|---|---|---|---|
| 展示 / h1 / h2 / quote-text / stat-value | Barlow 900 全大写 | 思源宋体 / Noto Serif SC | 700 | Studio 定义性的"文字即图形质量块"效果依赖单字面最大字重。NSC 700 是 CDN 上最重的宋体衬线，能在 12vw / 7.5vw / 4.8vw 展示尺寸撑住视觉分量。 |
| h3 | Barlow 700 全大写 | 思源宋体 / Noto Serif SC | 700 | 副标题字重相配。 |
| 导语 / 正文 / 图注 | Barlow 500 / 400 | 思源宋体 / Noto Serif SC | 400 | 极简编辑正文，NSC 400 在系统的稀疏布局里读得干净。 |
| 元数据 / 外壳 / 标签 / 统计注 | IBM Plex Mono 500 | IBM Plex Mono + Noto Sans Mono CJK 回退 | 400–500 | 中文等宽很少需要（多数元数据留在拉丁：日期、计数器、工作室名），但外壳里出现中文时，用 Noto Sans Mono CJK SC。 |

### 混排策略

本模板用**策略 A**：任何渲染汉字的元素，把拉丁字面整体换成 CJK 字面。Studio 的身份是文字即图形质量块，而 Barlow 900 无法渲染 CJK 字形（无字形覆盖）。经栈回退在同一行里混 Barlow 拉丁与 NSC CJK，会在展示尺度造出度量错位，破掉"单字面、单字重"语域。任何含中文的元素都把整条 `font-family` 换成 NSC。

```css
font-family: 'Noto Serif SC', 'Barlow', sans-serif;  /* display / headlines — CJK first */
font-family: 'Noto Serif SC', 'Barlow', sans-serif;  /* body — CJK first */
font-family: 'IBM Plex Mono', 'Noto Sans Mono CJK SC', monospace;  /* mono — Latin first, CJK only if needed */
```

纯中文文稿里系统的"全大写"身份会脱落（中文没有大小写），于是 Studio 的性格从"工业事务所宣言"偏向"编辑式中文报纸标题"。这是真实的语域变化，中文 Studio 读起来郑重而严苛，但不再读作 Pentagram/Anti。接受这个取舍，或把中文限定在特定页、让封面与分节断口保留拉丁 Barlow。

### 加载

加到 `<head>`（Google Fonts 托管 Noto Serif SC 与 Noto Sans SC）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;700;900&family=IBM+Plex+Mono:wght@400;500&family=Noto+Serif+SC:wght@400;500;700;900&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

原 design.md 里的 Barlow 栈已经把 Noto Sans SC 接为 CJK 回退。我们把标题与正文升级到 Noto Serif SC，因为 900 字重的宋体衬线承载的图形分量与 Barlow 900 相当，而同字重的 Noto Sans SC 读起来太顺太圆、丢掉"图形块"性格。偏好更干净无衬线的纯正文文稿可保留 Noto Sans SC。

### 通用 CJK 调整

施于任何渲染中文内容的元素（典型用 `:lang(zh)` 或 `<span lang="zh">` 限定范围）：

- **行高**：正文 1.75–1.85（Studio 的 1.5–1.6 Barlow 默认对拉丁够用、对 CJK 笔画偏紧），展示 1.15–1.25（比拉丁 0.9–0.95 松，因为 12vw 的 CJK 字形需要纵向呼吸）。
- **字距**：CJK 设 0。Studio 在展示拉丁上的负字距（-0.01 到 -0.03em）对中文是错的，CJK 字形本就预置间距，负字距会让展示尺度下的字形相碰或重叠。
- **文字变换**：CJK 不用 uppercase。Studio 在展示 token 上的 `text-transform: uppercase` 对汉字是空操作，但要确保没有父级规则尝试意外行为。系统的"全大写"身份在中文里脱落。
- **全角标点**：用 `，。：；！？`（全角）而非 `,.:;!?`（半角）。全角形式自带周围留白并贴合 CJK em 框。
- **展示标题不加句号**：中文标题去掉末尾 `。`，Studio 标题在拉丁里从不带句号，规则延伸到 CJK。
- **盘古之白（Pangu spacing）**：在 CJK 与相邻拉丁 / 数字间插入一个窄空格。写 `使用 Claude` 而非 `使用Claude`，`2024 年` 而非 `2024年`。Studio 的等宽元数据常挨着中文标签，那里盘古之白不可少。
- **一句一款字体**：不要在同一行里混 NSC 与 Noto Sans SC。衬线 / 无衬线切换应发生在元素边界。

### 本系统的美学提示

Studio 的二元配色（近黑上酸性黄、酸性黄上近黑）在 CJK 里完整保住，没有颜色决定要改。12vw 展示尺寸下、`{colors.near-black}` 场地上 `{colors.acid-yellow}` 的 NSC 700，与同角色 Barlow 900 带着同样的视觉冲击，饱和黄压暖深表面让汉字读出同样的海报式权威。

"文字即图形质量块"的效果在 CJK 里确实被改变，但方式有意思：Barlow 900 全大写块读作西方标牌 / 工业宣言，展示尺度的 NSC 700 读作**中文木刻或活字印刷海报**，同样严苛、同样图形化，但落在不同的文化语域。对中文读者这读作权威且设计精良，对混合受众则把感知调子略推向"编辑出版物"、远离"设计事务所"。

破折号项目标记直接迁移，保留表面强调色的 `—`。三栏等宽 cover-meta 锁定也无需改动就能迁移，studio × client / 演示标题 / 工作室名用中文或拉丁写都行，IBM Plex Mono 都能干净渲染（锁定里出现中文时回退到 Noto Sans Mono CJK SC）。

统计卡在 CJK 里运作良好，5.5vw 斜体式统计数字可在值为中文数字（`三百万`）时用 NSC 700 渲染，阿拉伯数字（`3M`）时留在 Barlow。2px 顶线与统计注（等宽）不受影响。

### 已知 CJK 缺口

- 定义系统的"全大写 + 负字距 + 字重 900"公式在 CJK 里无法复现。中文得到字重 700（NSC 最重）、无大小写变换、零字距。纯中文模式下系统丢掉约 30% 的拉丁性格。
- IBM Plex Mono 的完整特性集仅适用拉丁。元数据里出现汉字时（Studio 文稿里罕见），它们回退到 Noto Sans Mono CJK SC 或系统等宽，比例可能与周围的 Plex Mono 视觉不同。
- NSC 900 字重（本可更好匹配 Barlow 900）在 Google Fonts 上存在，但大到在大尺寸下字腔开始闭合，12vw 展示时 NSC 900 可能把某些字渲染成近乎实心的块。NSC 700 是推荐上限，极端展示瞬间可逐例测试 NSC 900。
- 系统的"深 / 黄表面交替"节奏不受 CJK 影响，但中文读者对节奏的解析可能与西方读者不同（颜色的文化阅读惯例影响节拍感知）。

## 迭代指南

1. 任何新标题都用负字距的全大写 Barlow 字重 900。三者（字重、大小写、字距）缺一，文字就丢掉图形质量块性格。
2. 任何新页都与前一页交替表面，一般别连跑超过 2–3 张深色页才给一次黄断口，反之亦然。节奏是设计的一部分。
3. 任何新外壳、元数据、标签、计数器都用 IBM Plex Mono。等宽用在别的角色会破掉元数据分离。
4. 任何新颜色都会给二元调色板引入第三个选项，别加。守着黄与近黑，用不透明度变体柔化。
5. 任何新项目列表都用表面强调色的破折号标记。圆点项目会破掉系统。
6. 统计卡用 2px 顶线加 5.5vw 字重 900 数字。更小的统计、句式统计、或圆角统计块都会破掉式样。
7. 封面页底部用三栏等宽锁定。别省掉它，它是系统最易认的式样。
8. 章节、陈述、引文、收尾页无外壳，标准页带外壳与页脚。别把两者混，无外壳引文是对的，带外壳引文读作另一套系统。
9. 新布局应以一个主导元素（标题）加最少辅助元素为目标。多元素布局（超过 4–5 个不同区域）会把设计挤满。
10. 2px 线粗预留给锚点（统计顶、基线、比较分隔）。外壳与结构分隔保持 1px。

## 已知缺口

- 两款字族（Barlow、IBM Plex Mono）从 Google Fonts 加载。字体加载失败时，回退是 Noto Sans SC / system-ui（Barlow）与 monospace（IBM Plex Mono），缺了 Barlow 900 系统显著退化，因为文字即图形质量块效果依赖具体字形。
- 中文回退（Noto Sans SC）接在 Barlow 栈里，但出厂只有 400、500、700、900 字重，中文内容用 h3（700）与导语（500）渲染干净，中间字重会回退到最接近的可用值。
- `--c-bg-alt`、`--c-bg-light-alt` 与若干柔化颜色 token 有定义但用得省，它们作为相邻表面区分的储备存在。
- 翻页 JS 内联嵌着，系统依赖它做文稿 transform 行为与 `is-active` 类管理。
- 封面图片占位用硬编码的 `IMAGE PLACEHOLDER` 标签与扁平 near-black-alt 填充，真正插入图片需把占位 div 换成带 background-image 样式、与父画布相配的元素。
- 5vw / 5vh 内边距刻意紧，意味着视口极小时标题可能不舒服地逼近边缘，系统为 1280px 及以上的 16:9 显示调校。
- 比较面板只在左面板用 2px 右边框（右面板无左边框），在两面板间造出一种非对称，这是刻意的，但把比较布局扩展到三连时值得记下。
