---
version: alpha
name: Editorial Forest
description: A serif-led editorial presentation system in the register of a literary quarterly or art-book monograph. Display type runs in Source Serif 4 at weight 500 with optical-size axis engaged, scaling up to 220px for cover and stat moments. The palette pairs a deep forest green (#2e4a2a) with a dusty rose pink (#e89cb1) over an oat-cream paper ground (#efe7d4), with JetBrains Mono as the editorial chrome (labels, captions, axis ticks). The aesthetic is closer to a Penguin classic, Apartamento spread, or quiet annual report than a tech keynote — confident, paper-feeling, and committed to a small color vocabulary.

colors:
  green: "#2e4a2a"
  green-deep: "#243a21"
  green-lite: "#3a5a36"
  pink: "#e89cb1"
  pink-deep: "#d27e96"
  cream: "#efe7d4"
  cream-2: "#e6dcc4"
  ink: "#1a1a17"

typography:
  display-hero:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 220
    fontWeight: 500
    lineHeight: 0.92
    letterSpacing: -0.02em
  display:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 140
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 96
    fontWeight: 500
    lineHeight: 0.96
    letterSpacing: -0.02em
  headline:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 84
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 80
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: -0.02em
  title-card-lg:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 84
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: -0.01em
  title-card:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 68
    fontWeight: 500
    lineHeight: 0.96
    letterSpacing: -0.01em
  title-card-sm:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 56
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: -0.01em
  figure-caption-serif:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 56
    fontWeight: 500
    lineHeight: 1.05
  name:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 44
    fontWeight: 600
    lineHeight: 1.0
  meta-value:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 32
    fontWeight: 500
  body-lg:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 32
    fontWeight: 400
    lineHeight: 1.32
  body:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 30
    fontWeight: 400
    lineHeight: 1.38
  body-card:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 26
    fontWeight: 400
    lineHeight: 1.34
  label:
    fontFamily: "'JetBrains Mono', ui-monospace, Menlo, monospace"
    fontSize: 26
    fontWeight: 500
    letterSpacing: 0.18em
    textTransform: uppercase
  label-tight:
    fontFamily: "'JetBrains Mono', ui-monospace, Menlo, monospace"
    fontSize: 26
    fontWeight: 500
    letterSpacing: 0.14em
    textTransform: uppercase
  caption-mono:
    fontFamily: "'JetBrains Mono', ui-monospace, Menlo, monospace"
    fontSize: 24
    fontWeight: 500
    letterSpacing: 0.14em
    textTransform: uppercase
  axis-mono:
    fontFamily: "'JetBrains Mono', ui-monospace, Menlo, monospace"
    fontSize: 26
    fontWeight: 500
    letterSpacing: 0.08em
  stat-figure:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 220
    fontWeight: 500
    lineHeight: 0.92
    letterSpacing: -0.03em
  stat-figure-unit:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 110
    fontWeight: 500
    lineHeight: 0.92

spacing:
  slide-pad-default: "96px 120px"
  slide-pad-narrow: "100px 120px"
  slide-pad-wide: "100px 140px"
  slide-pad-statement: "130px 160px"
  grid-gap-cards: 28
  grid-gap-topics: 24
  grid-gap-kpi: 60
  rule-weight: "2px"
  rule-weight-card: "2.5px"
  radius-card: "6px"
  radius-card-step: "8px"
  radius-bar-top: "3px 3px 0 0"
  radius-mark-circle: "50%"

canvas:
  width: 1920px
  height: 1080px

components:
  topic-tile:
    description: "Bordered or filled rectangular region holding a mono ordinal, a serif title, optional body, and a mono foot. Background may be green / green-lite / pink / cream-2-with-green-border. Corner radius 6px."
    borderRadius: "{spacing.radius-card}"
    padding: "40px 40px 36px"
  step-tile:
    description: "Vertical card carrying a mono ordinal, a serif title, body paragraph, and a mono marker row separated by a top rule. Background fills: cream-with-green-border, solid green, or solid pink."
    borderRadius: "{spacing.radius-card-step}"
    padding: "40px 32px 32px"
    minHeight: "470px"
    border: "2.5px solid currentColor-region"
  monogram-circle:
    width: "130px"
    height: "130px"
    borderRadius: "{spacing.radius-mark-circle}"
    border: "2px solid {colors.pink}"
    fontFamily: "JetBrains Mono"
    fontSize: 28
    letterSpacing: 0.1em
    fontWeight: 500
    description: "Outlined round mark holding a short mono monogram. The system's signature identity stamp."
  topbar:
    placement: "top edge of slide"
    layout: "flex space-between, baseline-aligned"
    content: "{components.label} on the left, monogram-circle or counter on the right"
  footline:
    position: "absolute"
    placement: "bottom edge of slide, full-width between slide padding"
    layout: "flex space-between"
    typography: "{typography.caption-mono}"
  meta-dl:
    description: "Three-column definition list separated by a top rule (2px {colors.green}). Each entry has a mono dt label and a serif dd value."
    columns: 3
    gap: "36px"
    topBorder: "2px solid {colors.green}"
  bar:
    width: "56px"
    borderRadius: "{spacing.radius-bar-top}"
    description: "Vertical chart bar in pink, cream, or green. Value label printed above bar in mono."
  chart-axis:
    border: "2px solid currentColor"
    description: "Y-axis and x-axis use a single 2px rule on the inner edges of the plot region; no full axis box."
  rule-thin:
    description: "Hairline 2px rule, used as section separator above kpi rows, summary grids, meta dls. Color follows region (green on cream, pink on green)."
  legend-swatch:
    display: "inline-block"
    width: "26px"
    height: "26px"
    borderRadius: "2px"
    description: "Small filled square preceding a mono legend label. 2px corner radius is the smallest radius in the system."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/editorial-forest/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Editorial Forest 是一套**衬线主导的编辑式演示系统**，语域落在企鹅经典、安静的年报或艺术书跨页。系统的底层前提是单一、自信的排印声部 **Source Serif 4**，以极端尺度（最大 220px）用于标题和统计数字，**JetBrains Mono** 扮演编辑外壳的辅助角色（标签、图注、轴刻度、页脚线）。

衬线几乎每个展示瞬间都跑**字重 500**，从不用更常见的 400 或 700。500 字重是系统最鲜明的排印选择：重到有"被写过"的感觉，轻到让页面保持平静。光学尺寸轴已启用（`opsz` 8..60），意味着同一款 Source Serif 4 在 26px 图注尺寸与 220px 展示尺寸下会渲染出略不同的字形，小尺寸自动得到更多对比和更精细的细节。JetBrains Mono 跑字重 500、大写、0.14em–0.18em 字距，用于每个标签、小片、图注、轴刻度、页脚行。系统绝不混入第三款字体。

配色是紧凑的五色编辑组，围绕三种主表面构建：**深森林绿**（`{colors.green}` — #2e4a2a）、**灰玫瑰粉**（`{colors.pink}` — #e89cb1）、**燕麦奶油纸**（`{colors.cream}` — #efe7d4）。两组近重复色补齐：`{colors.green-deep}` 给粉上绿文字的对比、`{colors.green-lite}` 给需要第二种绿的拼块填充、`{colors.pink-deep}` 给粉压粉边、`{colors.cream-2}` 给坐在主奶油表面上的拼块。正文文字处处是 `{colors.ink}`（#1a1a17），暖近黑，唯独落在绿或粉表面上时换成该表面的互补色（绿上奶油或粉，粉上 green-deep 或奶油）。

纵深是**平的、纸基的**。没有投影、没有辉光、没有渐变、没有叠层。抬升完全靠色块对比、2px 细线、以及"填充区域"与"带边区域"之间的差别来传达。除花押圆外，6px 与 8px 的卡片半径是系统里仅有的圆度。页面读起来像印出来的，不是玻璃。

**密度取向：宽裕且笃定。** 每页承载一个强主体（标题、引文、图表、统计行、卡片网格），由深负空间环绕。96–140px 的幻灯片内边距很宽裕，页顶带等宽顶栏（标签 + 花押或计数器），页底带等宽页脚线，中部把主主体放到大尺度。塞进两个互抢内容块的页读起来像坏了，一个展示标题 + 辅助卡片 + 呼吸空间的页读起来才权威。宁可元素更少、尺寸更大。

**关键特征：**
- 三色编辑配色：深森林绿、灰玫瑰粉、燕麦奶油纸。每页两种表面色调是常态，三种就吵。
- Source Serif 4 字重 500 用于每个标题、正文、展示瞬间。光学尺寸轴启用，字形随尺寸变化。
- JetBrains Mono 字重 500 大写、宽字距（0.14em–0.18em）用于每个标签、图注、轴刻度、页脚线。
- 展示字放大到 220px 供封面和统计数字瞬间，96px 供主标题，56–84px 供卡片标题。
- 2px 细线分隔叠起的章节，绝不更粗，绝不超出区域语境上色。
- 卡片半径 6px 给主题拼块、8px 给步骤拼块。花押圆是唯一全圆形状。
- 每页都带顶栏（标签 + 花押或计数器），多数带页脚线（等宽图注行）。外壳锚住编辑感。
- 无阴影、无渐变、无辉光。抬升靠色块 + 线。

## 颜色

### 调色板
- **Green**（`{colors.green}` — #2e4a2a）：深森林主色。用作幻灯片表面、拼块填充、卡片边、meta-dl 线色、奶油表面上的主文字色。系统最鲜明的表面。
- **Green Deep**（`{colors.green-deep}` — #243a21）：更深的绿，几乎只作粉表面上的文字色，纯绿在那里对比不够。也作粉拼块上的文字色。
- **Green Lite**（`{colors.green-lite}` — #3a5a36）：更浅的绿，当两种绿需并排时作拼块填充（例如同一网格里主绿拼块旁的次绿绿-lite 拼块）。承载粉文字。
- **Pink**（`{colors.pink}` — #e89cb1）：灰玫瑰。用作幻灯片表面、拼块填充、绿上文字色、条形图系列色、花押圆边色。系统的主强调。
- **Pink Deep**（`{colors.pink-deep}` — #d27e96）：略深的玫瑰，只作粉填充拼块上的边框色，同色边需要与填充分开时用。
- **Cream**（`{colors.cream}` — #efe7d4）：燕麦纸表面。非封面页的默认幻灯片背景、绿上正文文字色、奶油条形图系列色。
- **Cream 2**（`{colors.cream-2}` — #e6dcc4）：略深的奶油，用作奶油幻灯片表面上的拼块填充。配 2px 绿边，让拼块读起来与幻灯片底分开。
- **Ink**（`{colors.ink}` — #1a1a17）：奶油表面上的正文文字色。暖近黑，绝不纯 #000。

### 默认值
- **默认幻灯片背景**：内容多的页用 `{colors.cream}`，封面、陈述数据、摘要以及任何需要分量的瞬间用 `{colors.green}`。
- **`{colors.cream}` 表面上默认标题色**：`{colors.green}`。
- **`{colors.green}` 表面上默认标题色**：主标题 `{colors.cream}`，英雄 / 封面级标题 `{colors.pink}`。
- **`{colors.pink}` 表面上默认标题色**：`{colors.green-deep}`。
- **`{colors.cream}` 表面上默认正文色**：`{colors.ink}`。
- **`{colors.green}` 表面上默认正文色**：`{colors.cream}`。
- **`{colors.pink}` 表面上默认正文色**：`{colors.green-deep}`。
- **默认标签 / 图注色**：跟随区域的强调（绿上标签是粉、奶油上是绿、粉上是 green-deep）。
- **奶油页上默认拼块填充**：从轮转里挑，实绿（配粉字）、实粉（配 green-deep 字）、绿-lite（配粉字），或 cream-2 配 2px 绿边（配绿字）。单个网格通常混用其中 3 种。
- **默认线色**：奶油上绿、绿上粉、粉上 green-deep。2px 细线始终取区域的强调。

配色刻意收紧。引入第四色系（黄、蓝、再加一种玫瑰）会破掉编辑纪律。守住绿 / 粉 / 奶油三元组，让填充拼块与带边拼块之间的对比承担变化。

## 排印

### 字族
系统恰好加载两款网页字体：**Source Serif 4**（带完整光学尺寸轴 8..60、字重 300–800）与 **JetBrains Mono**（字重 400、500、700）。Source Serif 4 承载每个编辑瞬间：标题、正文、衬线图注、姓名、数字。JetBrains Mono 承载每一片外壳：标签、标语、轴刻度、页脚线、拼块上的序数。

等宽 / 衬线的搭配是系统的排印身份。等宽从不试图当标题，衬线从不试图当图注。角色相对典型的"无衬线做外壳、衬线做正文"栈是反过来的，这里是"等宽做外壳、衬线做正文和展示"。

Source Serif 4 几乎每个瞬间都跑**字重 500**。字重 400 只出现在正文段落（较轻的字重在小尺度下读起来更好）。字重 600 出现一次，用于陈述页的出处姓名，略重的一档把专有名与周围的等宽标签区分开。字重 700 不用。

### 展示、正文、外壳比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-hero}` | 220px | Source Serif 4 | 500 | 封面级或收尾级标题 |
| `{typography.display}` | 140px | Source Serif 4 | 500 | 拉页引文 / 大想法陈述 |
| `{typography.headline-xl}` | 96px | Source Serif 4 | 500 | 奶油上分节主标题 |
| `{typography.headline}` | 84px | Source Serif 4 | 500 | 绿上分节主标题 |
| `{typography.headline-sm}` | 80px | Source Serif 4 | 500 | 统计行引导标题 |
| `{typography.title-card-lg}` | 84px | Source Serif 4 | 500 | 英雄主题拼块内标题（网格里最大拼块） |
| `{typography.title-card}` | 68px | Source Serif 4 | 500 | 步骤拼块内标题 |
| `{typography.title-card-sm}` | 56px | Source Serif 4 | 500 | 标准主题拼块内标题 |
| `{typography.figure-caption-serif}` | 56px | Source Serif 4 | 500 | 居中的图 / 图片占位图注 |
| `{typography.stat-figure}` | 220px | Source Serif 4 | 500 | KPI 数字 |
| `{typography.stat-figure-unit}` | 110px | Source Serif 4 | 500 | KPI 数字的单位后缀（例如 "%"） |
| `{typography.name}` | 44px | Source Serif 4 | 600 | 出处行里的个人姓名 |
| `{typography.meta-value}` | 32px | Source Serif 4 | 500 | 元行里定义列表的值 |
| `{typography.body-lg}` | 32px | Source Serif 4 | 400 | 摘要或统计说明里的主正文段落 |
| `{typography.body}` | 30px | Source Serif 4 | 400 | 标准正文段落 |
| `{typography.body-card}` | 26px | Source Serif 4 | 400 | 卡片或拼块内正文 |
| `{typography.label}` | 26px | JetBrains Mono | 500 / 0.18em | 顶栏里的眉题或分节标签 |
| `{typography.label-tight}` | 26px | JetBrains Mono | 500 / 0.14em | 图注行、页脚行、出处行、拼块序数 |
| `{typography.caption-mono}` | 24px | JetBrains Mono | 500 / 0.12–0.16em | 拼块脚、拼块标记、kpi 小片、meta-dl 术语 |
| `{typography.axis-mono}` | 26px | JetBrains Mono | 500 / 0.08em | 图表轴刻度与标签 |

### 默认值
- **分节主标题默认尺寸**：奶油表面 `{typography.headline-xl}`（96px），绿表面 `{typography.headline}`（84px）。
- **封面级或收尾级瞬间默认尺寸**：`{typography.display-hero}`（220px）。
- **引文 / 大想法陈述默认尺寸**：`{typography.display}`（140px）。
- **正文段落默认尺寸**：`{typography.body}`（30px），衬线字重 400。
- **卡片 / 拼块内正文段落默认尺寸**：`{typography.body-card}`（26px）。
- **元 dt 标签或拼块序数默认尺寸**：`{typography.caption-mono}`（24px），JetBrains Mono 大写。
- **顶栏标签 / 眉题默认尺寸**：`{typography.label}`（26px），JetBrains Mono 大写、0.18em 字距。
- **任何衬线瞬间默认字重**：500（400 只留给正文段落，600 只留给出处里的专有名）。
- **任何等宽瞬间默认字重**：500。

拿不准时，奶油上的页面主标题取 `{typography.headline-xl}`（96px），不要用更大的展示尺寸。140–220px 一档留给陈述、统计数字、英雄/收尾瞬间，拿它排常规标题会把系统层级压平。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个 JetBrains Mono 元素都大写、至少 0.08em 字距。** 句首大写或无字距的等宽读成代码，不像编辑外壳。宽字距才让等宽像杂志里的图注行，而非终端。
- **每个 Source Serif 4 展示元素都用负字距（-0.01em 到 -0.03em）。** 紧字距把大衬线字形收成整块，对 96–220px 尺寸不可少。展示衬线用默认字距会读得松、像没处理过。
- **展示标题行高在 0.92 到 1.02 之间。** 紧行高是系统展示声部的一部分。较大的标题更紧（220px 时 0.92），较小的标题（84–96px）用 0.96–1.0。
- **正文段落用衬线字重 400，不用 500。** 从标题到正文的字重落差是系统的阅读节奏，正文 500 读起来重。
- **每页都带顶栏**（一侧等宽标签，对侧花押或计数器）。顶栏是系统通用的外壳锚点。
- **章节之间的细线永远是 2px 实线。** 绝不 1px（读成网页应用），绝不 3px+（读成海报）。

### 排印原则
字重 500 + 光学尺寸 + 紧字距的组合是系统的展示声部，换掉三者中任一属性（例如衬线字重 700、默认字距、无 opsz）都会读成另一套设计系统。衬线/等宽角色切分严格：等宽绝不出现在标题尺度，衬线绝不出现在轴刻度尺度。

系统任何地方都不用斜体，不用下划线。强调靠尺寸和颜色反差传达，不靠字体变体。

## 布局

### 画布系统
系统以固定 **1920×1080** 画布为目标。幻灯片是精确宽高的 `<section>` 元素，渲染依赖 `deck-stage.js` 把画布缩放适配视口。画布是纸，不是视口，为投影、打印或 PDF 导出而设计。

### 幻灯片内边距比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.slide-pad-default}` | 96px 120px | 标准幻灯片内边距 |
| `{spacing.slide-pad-narrow}` | 100px 120px | 数据、框架、统计页，顶部内边距略高 |
| `{spacing.slide-pad-wide}` | 100px 140px | 封面、摘要页，英雄标题用额外侧向内边距 |
| `{spacing.slide-pad-statement}` | 130px 160px | 陈述页，展示引文瞬间用最宽裕内边距 |

按内容分量挑内边距。陈述类瞬间用最宽，日常内容页用默认 96×120。

### 外壳解剖
每页（至少）在顶边带一条**顶栏**：一个 flex 行，一侧是 JetBrains Mono `{typography.label}`，另一侧是 `{components.monogram-circle}` 或等宽计数器 / 地点串。较重的页（封面、数据、摘要）还带一条**页脚线**，绝对定位在 `bottom: 60–80px`，等宽图注行在内边距之间横跨页宽。

顶栏是系统的脊梁。没有它，一页读起来像没处理过。

### 卡片半径
| 值 | 用途 |
|---|---|
| 2px | 仅图例色块（系统最小半径） |
| 3px 3px 0 0 | 条形图条的顶角 |
| 6px | 主题拼块（议程式网格） |
| 8px | 步骤拼块（框架式网格） |
| 50% | 花押圆 |

卡片是微妙圆角，绝不尖角，也绝不重圆角。6–8px 半径给系统带来纸而非塑料的质感。

## 纵深与层级

### 平、无阴影
系统里**没有阴影**。卡片、拼块、文字、花押圆上都没有。抬升完全靠：
1. **色块对比**：奶油页上的绿拼块因为深绿块从纸底分离，读起来是抬起的。
2. **2px 细线**：分节分隔线（kpi 行上方、摘要网格、meta dls）坐在区域强调色的 2px 线上。
3. **边对填充**：cream-2 拼块配 2px 绿边，读起来与旁边实填充拼块的抬升层级不同。

没有阴影本身就是抬升语言。加 `box-shadow: 0 4px 12px rgba(0,0,0,0.1)` 会击碎编辑感。

### 纸表面规则
系统里每个表面都读作纸，不是数字窗格。奶油色调（`{colors.cream}`、`{colors.cream-2}`）字面承担这种质感。绿与粉表面靠联想继承它：以全饱和使用、被奶油外壳环绕、绝不配阴影或辉光，读起来就是印在纸料上的墨。

## 形状与处理

### 边框粗细与样式
- **2px 实线**：通用细线。kpi 行 / 摘要网格 / meta dls / 图表轴上方的分节分隔线，cream-2 拼块的边，花押圆的边。
- **2.5px 实线**：步骤拼块边。略重，好让拼块读成独立于细线的物件。

边框取区域的强调色（奶油上 `{colors.green}`、绿上 `{colors.pink}`、粉上 `{colors.green-deep}` 或 `{colors.pink-deep}`）。

### 装饰元素类型

**花押圆**（`{components.monogram-circle}`）：130px 带描边圆，2px 粉边，内含 28px 的 2–3 字符 JetBrains Mono 花押。位于封面与摘要页右上。系统的身份印章。

**顶栏**（`{components.topbar}`）：横跨每页顶部的 flex 行。一侧 JetBrains Mono 标签，另一侧花押或计数器或地点串。顶栏确立页属于哪个表面家族（标签颜色会告诉你）。

**页脚线**（`{components.footline}`）：绝对定位在 `bottom: 60–80px`、在内边距之间横跨页宽的 flex 行。两条等宽图注串（例如左侧分节名、右侧页码）。用于封面、数据、摘要，以及任何想有印刷页感的页面。

**主题拼块**（`{components.topic-tile}`）：6px 半径的矩形区域，装一个等宽序数、一个衬线标题、可选正文、一条等宽脚串。背景填充在绿、绿-lite、粉、或 cream-2 配绿边之间轮转。一排这种拼块就是议程 / 目录模式。

**步骤拼块**（`{components.step-tile}`）：8px 半径的纵向卡片，2.5px 边，装一个等宽序数、一个衬线标题（68px）、一段正文段落、由顶线分开的一行等宽标记。背景填充：奶油配绿边、实绿、或实粉。一排 3–4 个步骤拼块就是框架 / 流程模式。

**KPI 块**：纵向叠排，顶部等宽小片（24px）、超大衬线数字（220px）配可选 110px 单位、下面一段衬线说明段落（30px）。坐在绿表面上由 2px 粉线在上方分隔的一行里。

**图表条**：56px 宽矩形，顶角 3px 圆，填粉、奶油或绿。数值标签是等宽 24px，绝对定位在条上方 38px。

**元定义列表**（`{components.meta-dl}`）：三列 dt/dd 网格，带 2px 顶边。dt 是等宽 24px 大写宽字距，dd 是衬线 32px 字重 500。用作双栏页底部的致谢 / 规格 / 细节行。

**图例行**：等宽大写项的横向 flex，每项前置一个 26×26px 填充色块、2px 圆角半径。用于图表和数据语境。

## 该做与不该做

### 该做
- 每个展示标题都用 Source Serif 4 字重 500、负字距（-0.01em 到 -0.03em）、紧行高（0.92–1.0）。这个组合就是系统的声部。
- 每个标签、图注、小片、轴刻度、页脚线都用 JetBrains Mono 字重 500 大写、0.08em–0.18em 字距。
- 每页放一条顶栏（等宽标签 + 花押或计数器）。顶栏是系统的脊梁。
- 每页挑一种主导表面（绿、粉或奶油），让它承载整张画布。每页两种表面色是上限。
- 网格里配对拼块填充，在绿 + 粉 + 绿-lite + cream-2 配绿边之间轮转，别让所有拼块复用同一填充。
- 用 2px 实线细线分隔叠起的分节（kpi 行、摘要网格、meta dls）。细线是系统的分隔语言。
- 内容容得下时大胆放大展示字，陈述、英雄、收尾瞬间用 140–220px。有空间时系统奖励"大"。
- 用宽裕的幻灯片内边距（96–160px）。负空间是编辑语域的一部分，局促内边距读起来像坏了。
- 把花押圆留给封面和摘要瞬间。每页都用它，会稀释它作为身份印章的功能。

### 不该做
- 不要给任何元素加 box-shadow。系统无阴影，加阴影会击碎纸感。
- 不要引入第三款字体。只有 Source Serif 4 和 JetBrains Mono，没有 Inter，没有系统栈。
- 不要把衬线文字用斜体或下划线。强调靠尺寸和颜色，不靠字体变体。
- 不要把 JetBrains Mono 渲染成句首大写或无字距。没有大写 + 字距的等宽读成代码，不像外壳。
- 不要引入第四色系（黄、蓝、薰衣草）。绿 / 粉 / 奶油三元组就是整个配色。
- 不要用重边（4px+）或细到 1px 的线。系统只有 2px 和 2.5px，挑一个。
- 不要在一页堆两个互抢的内容块。每页一个主体，放大或拆页。
- 不要用 rgba 透明度作表面色。每个表面都是实色墨压纸。
- 不要把衬线正文跑在字重 500，读起来重。正文 400，展示 500。
- 不要省掉顶栏。顶部没有等宽标签的页会丢掉编辑脊梁。

## 响应式行为

这是一套**固定 1920×1080 演示系统**，经 `deck-stage.js` 渲染。画布不是网页意义上的响应式，没有媒体查询、没有断点、没有流式尺寸。每处尺寸都是 1920×1080 下的固定像素。

### 缩放行为
`deck-stage.js` 脚本包裹每个 `<section>`，把 1920×1080 画布等比缩放适配浏览器视口，按需留黑边。文字、内边距、间隙、线粗细全是像素，随画布等比缩放。1920px 下读作 2px 的边，在 960px 视口宽度下会读作 1px，这在系统容差内可接受。

### 放映行为
导航委托给 `deck-stage.js` 提供的任意包装，没有内联键盘处理器。把每个 `<section>` 当作一页，运行时处理过渡。

### 打印 / 导出
因为每处尺寸都是 1920×1080 画布内的固定像素，系统能干净地以同样宽高比（16:9）导出 PDF。Source Serif 4 带光学尺寸轴，在打印分辨率下渲染良好，因为小尺寸变体会自动取到适合印刷的字形细节。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 中文字面 | 字重 | 理由 |
|---|---|---|---|
| 展示标题（220 / 140 / 96 / 84px） | 霞鹜文楷 LXGW WenKai（思源宋体 Noto Serif SC 回退） | 400 | 文学、略带手写笔意，匹配 Source Serif 4 的企鹅经典语域 |
| 正文段落（26 / 30 / 32px） | 思源宋体 Noto Serif SC | 400 | 读起来是文学季刊的印刷正文声部 |
| 统计数字（220px） | 思源宋体 Noto Serif SC | 700 | 明朝体字重 700 给出 Source Serif 4 字重 500 在拉丁里提供的数字分量 |
| 等宽标签 / 图注 / 页脚线（24–26px） | 思源等宽 Noto Sans Mono CJK SC | 500 | JetBrains Mono 没有 CJK 字形，思源等宽保住打字机外壳质感 |

### 混排策略

用**策略 C**：保留 Source Serif 4 作拉丁字面，CJK 字形回退到 LXGW WenKai（标题 / 展示）或 Noto Serif SC（正文 / 统计）。这对 Editorial Forest 是正确选择，因为 Source Serif 4 的光学尺寸轴是系统签名，整体换成明朝体会压平定义整套文稿的企鹅经典语域。font-family 栈把拉丁字面放前、CJK 回退放后、通用 serif 收尾：

```css
font-family: 'Source Serif 4', 'Source Serif Pro', 'LXGW WenKai TC', 'Noto Serif SC', Georgia, serif;
```

浏览器逐字形回退：拉丁字符渲染成启用 opsz 的 Source Serif 4 字重 500，汉字渲染成 LXGW WenKai（展示）或 Noto Serif SC（正文）。展示尺寸（96–220px）下的基线错位是主要留意点，LXGW WenKai 的光学基线比 Source Serif 4 略高，于是像 "Designed in 北京" 这样的混排行可能出现 1–2px 纵向晃动。幻灯片内容可接受，打印导出优先用全 CJK 或全拉丁行。

### 加载

在既有 Google Fonts `<link>` 里追加（或作为第二条 link 标签）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=LXGW+WenKai+TC&family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

LXGW WenKai TC 是 Google Fonts 上提供的版本（简体构建 `LXGW+WenKai+SC` 尚未上 Google CDN，TC 同时带繁体和简体字形，两者都能用）。

### 通用 CJK 调整

以下调整适用于本系统**每一个 CJK 块**，无论尺寸或角色：

- **行高放宽 0.05–0.08。** CJK 字形是全宽方块，视觉分量比拉丁字形重，为拉丁调的行高（展示 0.92–1.0、正文 1.32–1.38）在中文里读起来局促。展示放到 1.0–1.1，正文放到 1.5–1.6。
- **去掉 CJK 标题的负字距。** Source Serif 4 展示用 -0.01em 到 -0.03em 字距，会撞在一起。CJK 段设 `letter-spacing: 0`，标题看着挤时可用微小的正 `0.02em`。
- **绝不对 CJK 文字用 `text-transform: uppercase`。** 中文没有大小写，CSS 属性对汉字无效，却会悄悄破坏混排行里本该大写的拉丁部分。
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不用拉丁对应物（`,.:;!?""''()`）。同一句里混用标点系统读起来是排印错误。
- **CJK 标题末尾不加句号（。）。** 中文标题与拉丁遵循同一规则，标题式行去掉末尾标点。正文段落保留 。
- **在 CJK 与拉丁串交界处套用盘古之白。** 汉字与相邻拉丁词或数字之间应有一个空格（或 0.25em 外边距），例如 `2026 年 5 月` 而非 `2026年5月`。要么手打空格，要么用 `pangu.js` 式自动加空格器。
- **一句一款字体。** 不要在同一句里切换 LXGW WenKai 与 Noto Serif SC，挑与尺寸档匹配的字面（展示 = LXGW WenKai，正文 = Noto Serif SC），整段从一而终。

### 本系统的美学提示

Editorial Forest 的整个声部是"企鹅经典 / 安静年报"，一款字重 500 的衬线、由光学尺寸轴做尺寸感知的字形工作。这个语域的中文对应是：展示瞬间用 **LXGW WenKai**（它带着与 Source Serif 4 字重 500 同样的手工排、略不正式的暖意），正文用 **Noto Serif SC 400**（读起来像文学期刊的平静明朝声部）。正文别用 Noto Sans SC，无衬线字面会把系统翻成"技术报告"而非"专著跨页"。

系统的等宽 / 衬线角色切分（JetBrains Mono 做外壳、Source Serif 4 做其余）能干净地映射到中文。顶栏标签、页脚线串、拼块序数、轴刻度用 Noto Sans Mono CJK SC，保持大写等效（即拉丁标签上 0.14em–0.18em 字距，中文则用等宽 CJK 字重 500 提供同样的外壳质感）。别用 LXGW WenKai 或 Noto Serif SC 跑中文标签，编辑外壳会丢掉打字机感。

### 已知 CJK 缺口

LXGW WenKai 的笔意暖意在大展示尺寸下是长处，但到正文尺度（26–32px）同样笔意会略显噪。系统把正文提升到 Noto Serif SC（更干净的明朝体）来避开，然而 96px LXGW WenKai 标题与下方 30px Noto Serif SC 段落之间的视觉交接，是系统最大的 CJK 接缝，两款字面笔画对比剖面不同。接缝显得响时，展示和正文都用 Noto Serif SC（牺牲暖意换一致），或都用 LXGW WenKai（牺牲正文可读性换一致）。默认切分对多数文稿是正确的取舍，但封面与陈述页值得手动检查。

## 迭代指南

1. 任何新标题都是 Source Serif 4 字重 500 配负字距。从展示阶梯里挑尺寸（220 / 140 / 96 / 84 / 80 / 68 / 56），别自创尺寸。
2. 任何新标签、图注、小片都是 JetBrains Mono 字重 500 大写、0.08em–0.18em 字距。从等宽阶梯里挑尺寸（26 / 24）。
3. 任何新页顶部都带顶栏。等宽标签色跟随表面（绿上粉、奶油上绿、粉上 green-deep）。
4. 任何新卡片用 6px（主题拼块）或 8px（步骤拼块）半径。花押圆是唯一全圆形状，别引入第四种半径。
5. 任何新分节分隔都是区域强调色的 2px 细线。不要 1px 线，不要 3px 线。
6. 任何新填充色都必须来自既有配色（`{colors.green}`、`{colors.green-lite}`、`{colors.pink}`、`{colors.cream}`、`{colors.cream-2}`）。别引入黄、蓝或第三种粉。
7. 任何新正文段落都是衬线字重 400、26–32px。别把正文跑在字重 500。
8. 任何新 KPI 数字都是 `{typography.stat-figure}`（220px）。系统里没有更小的 KPI 尺寸，布局容不下 220px 就重构页面。
9. 任何新图表都用绿表面上的条处理（粉 / 奶油 / 绿填充、等宽轴、2px 轴线）。数据构图是系统身份的一部分。
10. 拿不准时，宁可元素更少、尺寸更大。系统编辑语域一挤就塌。

## 已知缺口

- 系统依赖 `deck-stage.js` 做画布缩放与幻灯片导航。脚本不在本 design.md 描述，视为运行时依赖。
- Source Serif 4 与 JetBrains Mono 经 `<link>` 从 Google Fonts 加载。离线渲染分别回退到 Georgia 衬线和 Menlo 等宽，能保住大致性格，但会丢掉光学尺寸轴与 JetBrains Mono 身份。离线 / 打印可靠性建议自托管。
- Source Serif 4 光学尺寸轴（`opsz` 8..60）对系统品质关键，用无 opsz 的回退字面会压平尺寸感知的字形对比。
- 条形图用手设条高（固定 520px 绘图区的 `%`）。没有数据绑定，扩展图表要手算高度。
- 花押圆、页脚线串、拼块计数器在源码里带硬编码文字。每套文稿需要换成实际身份。
- 系统没有 `@media print` 规则，也没有响应式断点，固定 1920×1080，任何视口适配都依赖 `deck-stage.js`。
- 绿上粉、粉上绿的文字对比比在所用展示尺寸（84px+）下足够，但到正文文字尺寸会过不了 WCAG AA。别把 26px 正文放成粉压绿或绿压粉，小字保持绿上奶油或奶油上墨。
