---
version: alpha
name: Signal
description: A literary editorial presentation system in the spirit of a long-form magazine — The Economist's restraint crossed with a private intelligence briefing. Source Serif 4 carries every headline with roman/italic mixing mid-sentence in antique gold, DM Sans steps back for body, and IBM Plex Mono runs all the timestamps, kickers, and chrome. The dual surface system is warm cream paper (#F0ECE3) and deep editorial navy (#1C2644), connected by a single hot accent — antique gold (#C8A870) — used only on rules, italic emphasis, and numerical figures. A near-invisible 80px grid texture overlays every dark slide as a fingerprint. The effect is sober, considered, and a little bit aristocratic.

colors:
  navy: "#1C2644"
  navy-alt: "#232F55"
  cream: "#F0ECE3"
  cream-alt: "#E6E0D4"
  text-warm: "#E2DCD0"
  text-muted-dark: "#8A96A8"
  text-hint-dark: "#4E5A6E"
  ink: "#1A2030"
  text-muted-light: "#5A6270"
  text-hint-light: "#9AA0A8"
  gold: "#C8A870"
  border-dark: "#2E3D5C"
  border-light: "#CAC4B4"

color-aliases:
  c-bg: navy
  c-bg-alt: navy-alt
  c-bg-light: cream
  c-bg-light-alt: cream-alt
  c-fg: text-warm
  c-fg-2: text-muted-dark
  c-fg-3: text-hint-dark
  c-fg-light: ink
  c-fg-light-2: text-muted-light
  c-fg-light-3: text-hint-light
  c-accent: gold
  c-border: border-dark
  c-border-light: border-light

typography:
  display:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 9.5vw
    fontWeight: 700
    lineHeight: 0.96
    letterSpacing: -0.02em
  h1:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 5.2vw
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: -0.01em
  h2:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 3vw
    fontWeight: 600
    lineHeight: 1.18
  h3:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 1.9vw
    fontWeight: 500
    lineHeight: 1.3
  lead:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.4vw
    fontWeight: 400
    lineHeight: 1.58
  body:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.05vw
    fontWeight: 400
    lineHeight: 1.65
  caption:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 0.82vw
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "IBM Plex Mono, JetBrains Mono, monospace"
    fontSize: 0.7vw
    fontWeight: 500
    letterSpacing: 0.14em
    textTransform: uppercase
  stat-value:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 5.5vw
    fontWeight: 600
    lineHeight: 1
    letterSpacing: -0.02em
  quote-text:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 3.6vw
    fontWeight: 400
    lineHeight: 1.28
    letterSpacing: -0.01em
  quote-mark:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 8vw
    fontWeight: 300
    lineHeight: 0.6
  editorial-headline:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 2.75vw
    fontWeight: 600
    lineHeight: 1.2
  dense-headline:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 2.4vw
    fontWeight: 600
    lineHeight: 1.2

spacing:
  pad-x: 7.5vw
  pad-y: 5.5vh
  gap-lg: 4vh
  gap-md: 2.5vh
  gap-sm: 1.2vh
  grid-cell: 80px

canvas:
  width: 100vw
  height: 100vh

components:
  rule-short:
    width: 36px
    height: 1px
    background: "{colors.gold}"
    description: "Short gold rule used as a kicker separator above headlines and as a chapter accent mark."
  rule-full:
    width: "100%"
    height: 1px
    background: "{colors.border-dark}"
    description: "Full-width hairline divider, color shifts to {colors.border-light} on cream surfaces."
  kicker:
    color: "{colors.gold}"
    typography: "{typography.label}"
    description: "Mono uppercase label in antique gold, sits above a headline."
  tag:
    border: "1px solid {colors.gold}"
    color: "{colors.gold}"
    padding: "0.3em 0.8em"
    typography: "{typography.label}"
    description: "Outlined gold pill containing a mono uppercase label."
  chrome-bar:
    borderBottom: "1px solid {colors.border-dark}"
    paddingBottom: "{spacing.gap-sm}"
    marginBottom: "{spacing.gap-md}"
    description: "Top chrome strip with mono label left, mono counter right, hairline rule beneath."
  foot-bar:
    borderTop: "1px solid {colors.border-dark}"
    paddingTop: "{spacing.gap-sm}"
    marginTop: "{spacing.gap-md}"
    description: "Bottom chrome strip, mirror of chrome-bar."
  stat-card:
    borderTop: "1px solid {colors.border-dark}"
    padding: "{spacing.gap-md} {spacing.gap-md} {spacing.gap-md} 0"
    description: "Stat tile with a top hairline rule, big gold serif numeral above a sans label and mono note."
  bullet-marker:
    content: "—"
    color: "{colors.gold}"
    fontFamily: "{typography.label.fontFamily}"
    description: "Em-dash bullet rendered in mono gold prefixes every list item."
  vt-spine:
    width: 1px
    background: "{colors.border-dark}"
    description: "Vertical hairline spine for timeline column, with a 9px gold dot marking each entry."
  vt-dot:
    width: 9px
    height: 9px
    borderRadius: 50%
    background: "{colors.gold}"
    description: "Gold node sitting on the timeline spine at each date."
  pie-donut:
    borderRadius: 50%
    innerCutout: "22% inset, painted to match slide background"
    description: "SVG/CSS donut chart, segments in palette colors with a 1px gold ring divider where used."
  bar-fill-default:
    background: "{colors.text-hint-dark}"
    description: "Default bar fill in muted slate; switches to gold for the highlighted bar."
  bar-fill-accent:
    background: "{colors.gold}"
  compare-divider:
    borderRight: "1px solid {colors.border-dark}"
    description: "Single vertical hairline separating two comparison panels."
  pyramid-band:
    borderLeft: "3px solid {colors.gold}"
    padding: "1.3vh 2.5vw"
    fillFunction: "color-mix(in srgb, {colors.gold} N%, {colors.navy})"
    description: "Horizontal band in pyramid layouts; opacity of gold mix decreases from top tier to bottom."
  grid-texture:
    background: "linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px)"
    backgroundSize: "80px 80px"
    description: "Near-invisible 80px grid overlay applied to every dark slide via ::before pseudo-element."
  cycle-step:
    borderTop: "2px solid {colors.gold}"
    padding: "{spacing.gap-md}"
    description: "Cycle/process step card with a 2px gold rule at top, gold numeral, serif title, sans body."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/signal/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Signal 是一套**文学编辑**演示系统，是一份长篇情报简报或严肃杂志的季度评述若以文稿形式呈现会有的样子。视觉前提是两款字面的联姻：一款苏格兰深烘调的编辑衬线（Source Serif 4）承载声音，一款精密怪诞体（DM Sans）承载实质，再配一款压缩等宽（IBM Plex Mono）承载每个时间戳、眉题、外壳元数据碎片。结果读作安静的权威，文稿无需呐喊，因为排印已经把郑重传达出来了。

系统跑在**双表面**模型上。深色表面是 `{colors.navy}`（#1C2644），一种深编辑蓝，比海军蓝暖、比午夜蓝冷。浅色表面是 `{colors.cream}`（#F0ECE3），一种暖的旧纸调，绝非纯白。两个表面承载同一套同尺度的排印词汇，变的是前景色。深表面上主文字是 `{colors.text-warm}`（暖米白，绝非纯白）。奶油上主文字是 `{colors.ink}`（带蓝偏的近黑）。两个表面在页间可互换，相邻页可以无解释地交替，奶油表面在一段较长的深色连续里充当"重置"。

强调色恰好一种：**古金**（`{colors.gold}` — #C8A870）。金只出现在三处语境：隔开眉题与标题的短线，混进正体衬线标题里的 `<em>` 标签（"Signal 瞬间"），以及任何数字。金绝不承载正文段落，绝不填充背景。它是一件精密工具，省着用，好让出现时带分量。

纵深是**扁平加细线**。没有投影、没有圆角卡片外壳、没有抬升系统。区域靠 `{colors.border-dark}` 的 1px 细线（奶油上 `{colors.border-light}`）分隔。系统里唯一的"纹理"是深色页上一层几乎看不见的 80px 网格叠层，3% 白不透明度，只有刻意去找的眼睛才看得见。它是系统的指纹。

**密度取向：中低且非对称。** Signal 是编辑系统，它呼吸。典型一页只用它一小部分面积，一个眉题、一个标题、一句话、一条页脚。封面与章节页最疏（一条展示标题对着大片奶油或海军蓝）。密集编辑布局是例外而非常态，连那些也留宽裕的内部内边距。在 Signal 里读着别扭的页，是把画布从边到边填满内容的页；对的语域是"我有一件事要说，我会说得仔细"。

**关键特征：**
- Source Serif 4 承载每个标题，句中混排正体 / 斜体，标题里的斜体始终是金。
- DM Sans 作正文，IBM Plex Mono 作每个时间戳、眉题、标签、外壳元素。
- 双表面，`{colors.navy}`（深）与 `{colors.cream}`（浅），可互换使用，除特殊分屏布局外不在同一页混用。
- 古金（`{colors.gold}`）是唯一强调。它标线、斜体强调、数字，别处不出现。
- `{colors.border-dark}` / `{colors.border-light}` 的 1px 细线分隔每个区域。无卡片外壳、无圆角面板。
- 一层几乎看不见的 80px 网格纹理盖在每张深色页上，作几乎不可察觉的指纹。
- 金色等宽的破折号项目标记取代标准圆点。
- 每张标准页顶部的等宽全大写外壳承载分节标签与页码。
- 无投影、无渐变（满幅图片页上自下而上的遮罩除外）、无圆角（环形图除外）。

## 颜色

### 调色板

- **海军蓝**（`{colors.navy}` — #1C2644）：深色表面。深编辑蓝，比午夜蓝暖、比靛蓝冷。是"情报"色，权威而不进攻。
- **海军蓝 Alt**（`{colors.navy-alt}` — #232F55）：略抬起的海军蓝，预留给次级深色表面（占位面板、图片回退）。视觉上与海军蓝几近一致，只在紧贴相邻时才显差别。
- **奶油**（`{colors.cream}` — #F0ECE3）：浅色表面。暖的旧纸调，绝不中性、绝不明亮。读作"大幅报纸"或"手稿"，不是"屏幕白"。
- **奶油 Alt**（`{colors.cream-alt}` — #E6E0D4）：略冷的奶油，用于次级浅色表面。角色同 navy alt，但在浅侧。
- **暖文字**（`{colors.text-warm}` — #E2DCD0）：暖米白。海军蓝表面上的主文字色。绝不用 `#FFFFFF`，纯白会与系统暖纸逻辑冲突。
- **深色柔化文字**（`{colors.text-muted-dark}` — #8A96A8）：柔化蓝灰。海军蓝上次级文字，描述、想往后退的导语段。
- **深色提示文字**（`{colors.text-hint-dark}` — #4E5A6E）：海军蓝上三级文字。用于统计注、等宽图注、以及该可读但安静的元素。
- **墨**（`{colors.ink}` — #1A2030）：带蓝偏的近黑。奶油上的主文字。它拾起深色表面的颜色，而非与之对抗。
- **浅色柔化文字**（`{colors.text-muted-light}` — #5A6270）：奶油上次级文字。
- **浅色提示文字**（`{colors.text-hint-light}` — #9AA0A8）：奶油上三级文字。
- **金**（`{colors.gold}` — #C8A870）：古金。系统唯一强调色。出现在线、标题内斜体强调、统计数字、眉题标签、项目标记上。绝不作为填充，绝不用于正文。
- **深色边框**（`{colors.border-dark}` — #2E3D5C）：海军蓝表面上的细线分隔。可见但安静。
- **浅色边框**（`{colors.border-light}` — #CAC4B4）：奶油表面上的细线分隔。暖灰米。

### 默认值

- **默认表面**：整套文稿在 `{colors.navy}`（深）与 `{colors.cream}`（浅）间交替。没有"主"表面，两者都是一等。拿不准时，章节开场与陈述页取海军蓝，密集编辑阅读页取奶油。
- **海军蓝上默认主文字**：`{colors.text-warm}`。
- **奶油上默认主文字**：`{colors.ink}`。
- **海军蓝上默认次级文字**：`{colors.text-muted-dark}`。
- **奶油上默认次级文字**：`{colors.text-muted-light}`。
- **默认三级 / 提示文字**：海军蓝上 `{colors.text-hint-dark}`、奶油上 `{colors.text-hint-light}`，用于等宽图注、统计注、脚注。
- **默认强调**：`{colors.gold}`，施于线、标题内斜体强调、统计数字、眉题标签。
- **默认边框**：海军蓝上 `{colors.border-dark}`、奶油上 `{colors.border-light}`。
- **默认眉题色**：`{colors.gold}`。

两个表面可互换、承载同一金色强调，海军蓝上的金线与奶油上的金线读起来一样。正文绝不出现在金色里。金绝不作区域填充。

## 排印

### 字族

Signal 以精心分开的角色跑四款字族：

- **Source Serif 4**（`{typography.display.fontFamily}`）：一款苏格兰深烘调的编辑衬线。承载每个尺度上的每个标题（display、h1、h2、h3、editorial-headline、dense-headline、quote-text、stat-value）。这款字面有完整斜体轴，系统最鲜明的排印动作是**句中混排正体与斜体**：正体承载句子，里面的 `<em>` 标签切到 `{colors.gold}` 斜体。这就是"Signal 瞬间"。
- **DM Sans**（`{typography.body.fontFamily}`）：一款人文怪诞体，用于正文、导语段、项目项、统计标签。DM Sans 是结构性配角，它从不领衔，始终支撑。`<em>` 出现在无衬线 `.lead` 段里时，强调切到**金色斜体衬线**（换 font-family），而非斜体无衬线。
- **IBM Plex Mono**（`{typography.label.fontFamily}`）：一款压缩编辑等宽。承载每个标签、每个眉题、每个外壳元素（顶条、页脚、页码）、每个章节号、每条等宽图注、每条统计注、每个时间轴日期。等宽是系统的"元数据声部"。
- **Noto Serif SC / Noto Sans SC**：衬线与无衬线角色的中文回退。接进每条 font-family 栈，让系统带中文内容时渲染一致。

情绪反差是：衬线 = 声音，无衬线 = 实质，等宽 = 时间戳。在一句里混用它们（无衬线 lead 里嵌一个金色斜体衬线 `<em>`）是系统的小段编排。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 9.5vw | Source Serif 4 | 700 | 最大尺度的英雄封面标题 |
| `{typography.h1}` | 5.2vw | Source Serif 4 | 600 | 章节标题或单句陈述标题 |
| `{typography.stat-value}` | 5.5vw | Source Serif 4 | 600 | 金色大统计数字 |
| `{typography.quote-mark}` | 8vw | Source Serif 4 | 300 | 金色装饰性起始引号字形 |
| `{typography.quote-text}` | 3.6vw | Source Serif 4 | 400 | 引文正文 |
| `{typography.h2}` | 3vw | Source Serif 4 | 600 | 页面主标题 |
| `{typography.editorial-headline}` | 2.75vw | Source Serif 4 | 600 | 编辑 / 简报布局的标题 |
| `{typography.dense-headline}` | 2.4vw | Source Serif 4 | 600 | 双栏密文布局的标题 |
| `{typography.h3}` | 1.9vw | Source Serif 4 | 500 | 副标题、面板标题、区域内标题 |
| `{typography.lead}` | 1.4vw | DM Sans | 400 | 导语段、开场句、列表项正文 |
| `{typography.body}` | 1.05vw | DM Sans | 400 | 段落正文、项目正文 |
| `{typography.caption}` | 0.82vw | DM Sans | 400 | 图注、脚注、来源归属 |
| `{typography.label}` | 0.7vw | IBM Plex Mono | 500 | 等宽全大写外壳标签、眉题、标记、等宽元数据 |

### 默认值

- **主分节标题默认尺寸**：`{typography.h2}`（3vw）。
- **章节开场默认尺寸**：`{typography.h1}`（5.2vw）。
- **封面英雄默认尺寸**：`{typography.display}`（9.5vw）。
- **段落默认尺寸**：`{typography.body}`（1.05vw）。
- **标题下导语句默认尺寸**：`{typography.lead}`（1.4vw）。
- **任何外壳、眉题、元数据标签默认尺寸**：`{typography.label}`（0.7vw）。
- **统计数字默认尺寸**：`{colors.gold}` 的 `{typography.stat-value}`（5.5vw）。
- **默认标题色**：该表面的主文字色（海军蓝上 `{colors.text-warm}`、奶油上 `{colors.ink}`）。绝非金。

主瞬间在 `{typography.h2}` 与 `{typography.h3}` 间拿不准时，取 `{typography.h2}`，h3 留给区域内的副标题，不留给页面主陈述。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **任何衬线标题（`display`、`h1`、`h2`、`h3`、`editorial-headline`、`dense-headline`）里的 `<em>` 标签都必须渲染成 `{colors.gold}` 的斜体 Source Serif 4。** 这是系统最鲜明的排印瞬间，句中混排正体与斜体并换色。带强调短语却没这处理的标题读作另一套设计系统。
- **无衬线 `.lead` 或正文段里的 `<em>` 标签必须把 font-family 切到 Source Serif 4、斜体、`{colors.gold}`。** 正文里的强调绝不留在 DM Sans 斜体，换字面才是强调。
- **每个眉题都是 `{colors.gold}` 的等宽全大写、至少 0.14em 字距。** 无衬线、小写、或非金色的眉题不是眉题。
- **每个统计数字都是 `{colors.gold}` 的 Source Serif 4 600、配 -0.02em 字距。** 无衬线统计、或主文字色的统计都会破掉系统。
- **每条外壳条都在下方带一条 `{colors.border-dark}` / `{colors.border-light}` 的 1px 细线。** 细线才让外壳读作外壳，而非漂浮文字。
- **每张章节页都在章节号与章节标题之间带一条 36px 金线。** 这条线就是分节断口，没线就没章节。
- **项目列表用等宽金色的破折号作标记。** 本系统不存在标准圆点项目。

### 排印原则

字族阶梯固定：衬线作声音（display 到 h3）、无衬线作实质（lead 到 caption）、等宽作元数据（仅 label）。绝不用衬线排正文、绝不用无衬线做标题、绝不在元数据角色之外用等宽。跨过这些轨道会破掉编辑分离。

斜体是结构性的，不是装饰，它是标题内与导语段内的强调载体。下划线不存在。正文里粗体不存在，正文要强调就切到斜体衬线金色 `<em>` 式样。

行高在展示尺度上紧（display 0.96、h1 1.08），随尺寸变小而放开（caption 与 body 1.5–1.72）。字距在 display 与 h1 上为负（–0.01 到 –0.02em）、正文为零。等宽标签带 0.14em 到 0.22em 字距，宽裕字距才是等宽读作编辑而非代码的方式。

## 布局

### 画布系统

系统以 `100vw × 100vh` 满视口为目标。每张 `.slide` 以 flex 精确铺满视口，页并排坐在一条横向条里，导航时左右平移。所有尺寸用视口相对单位（`vw`、`vh`），布局随窗口大小缩放，除外壳圆点 / 计数器尺寸外没有固定像素度量。

### 内边距与间隙比例

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 7.5vw | 幻灯片横向内边距 |
| `{spacing.pad-y}` | 5.5vh | 幻灯片纵向内边距 |
| `{spacing.gap-lg}` | 4vh | 主内容分节之间 |
| `{spacing.gap-md}` | 2.5vh | 相关元素之间 |
| `{spacing.gap-sm}` | 1.2vh | 紧密耦合元素之间 |

引文页把 pad-x 提到 1.1×、pad-y 提到 1.2×，给引文多留呼吸。比较布局用 `pad-x * 0.55` 作每块面板的内缩内边距。

### 外壳画框

标准页带顶部外壳条与底部页脚条，两者都是 flex 行，左侧等宽标签、右侧等宽计数器，由 1px 细线与正文隔开。封面、章节、陈述、引文、收尾页隐去外壳与页脚，那些布局无外壳，让文字从边到边呼吸。

每页是一个 `grid-template-rows: auto 1fr auto` 的 CSS 网格，外壳与页脚是 auto 行，正文是填满的 1fr 行。

### 网格纹理

每张深色页带一层几乎看不见的 80px × 80px 网格叠层，由两张 3% 白不透明度的线性渐变背景画出。网格是系统的视觉指纹，不该被有意识地看见，只被感知为"这页有结构"。奶油页不带这层叠层。

## 纵深与层级

Signal **按设计是扁平的**。没有投影。没有圆角卡片抬升。根本没有抬升系统，每个元素都与表面齐平。

看着像纵深的东西其实是**细线分隔**。区域靠 `{colors.border-dark}`（海军蓝上）或 `{colors.border-light}`（奶油上）的 1px 实边分隔。统计块、外壳条、编辑栏，全由细线分隔，不由阴影或背景分隔。

唯一例外是**满幅渐变遮罩**：满幅图片页上，一条从透明到 `rgba(15, 20, 36, 0.9)` 的线性渐变自下而上铺过页面下部，让压在图片上的文字仍可读。这是系统里唯一的渐变，别处表面都是实色。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0 | 系统里除环形图与环形中心井外的每个形状 |
| 50%（圆） | 环形图形状、9px 时间轴圆点、色样上 2px 圆端边框 |
| 2px | 饼图图例色样（仅细微柔化） |

Signal 实际上**没有圆角外壳**。统计块、外壳条、比较面板、图片框，全是带尖角的矩形。

### 边框粗细

- **1px 实线**：通用细线边框。用在每条外壳条、每条统计块顶线、每条栏分隔、每条比较面板分隔、每条编辑栏边界。颜色随表面（`{colors.border-dark}` 或 `{colors.border-light}`）。
- **1px 虚线**：只用在图表绘图区内的网格线（rgba 透明、极低不透明度）。
- **2px 实 `{colors.gold}`**：用在循环 / 流程步骤的顶线。
- **3px 实 `{colors.gold}`**：用作金字塔带的左边框。

### 装饰元素类型

**短金线**：36px × 1px 实金水平条。坐在眉题与标题之间，或作章节强调标记。系统里最小的原子装饰元素。

**满细线**：100% × 1px 的 `{colors.border-dark}` / `{colors.border-light}` 水平线。用作分节分隔、外壳分隔、统计块顶边、栏边界。

**描边金标签**：小 inline-block，1px 金边框围住等宽全大写金文字。眉题的"胶囊"版，同一排印规格，带描边。

**编辑栏分隔**：编辑布局里两栏之间通顶到地的 1px 细线。栏内内边距为 `pad-x * 0.38`。

**竖向时间轴脊**：贯穿竖向时间轴全高的 1px 竖细线，沿脊每个条目处有 9px 金色圆点。

**金字塔带**：水平带，带 3px 实金左边框，以 `color-mix(in srgb, gold N%, navy)` 填充，N 从顶层的 70% 递减到底层的 8%。每层也逐级变宽（38% → 100%）。它靠色彩饱和度与宽度造出视觉金字塔，不用任何真实三角几何。

**环形中心井**：饼环内侧 22% 内缩填页面背景色（海军蓝或奶油），造出环形孔。

**连接箭头**：循环与图示布局里，一枚 `{colors.border-dark}`（或 `{colors.border-light}`）的低反差箭头字形坐在相邻步骤之间。箭头刻意柔化，步骤领衔，连接后退。

**等宽破折号项目**：每个列表项带一个等宽金色破折号（`—`）作项目标记，标记列 1.2em、间隙 0.5em。

## 该做与不该做

### 该做

- 在同一标题里混排正体与斜体 Source Serif 4，斜体着 `{colors.gold}`，这是 Signal 瞬间，系统依赖它在整份文稿里反复出现。
- 每个眉题、标签、标记、外壳元素、页码、章节号、统计注都用 IBM Plex Mono。等宽是元数据声部。
- 每个眉题都渲染成等宽全大写金、至少 0.14em 字距，字距才是等宽读作编辑的原因。
- 每条外壳条都在下方带一条该表面合适边框色的 1px 细线。细线不可商量，没线的外壳读作漂浮文字。
- 整套文稿里自由交替海军蓝与奶油表面。没有哪个"才是"背景，两者都是一等。
- 每个统计数字都用 Source Serif 4 600、 -0.02em 字距着 `{colors.gold}`。统计是仅次于斜体金色标题强调的第二易认元素。
- 用等宽金色破折号取代标准圆点项目。标准圆点会破掉编辑语域。
- 用 36px 金线作章节断口与眉题分隔。它是系统的小标点。
- 经 `::before` 给每张深色页套 80px 网格纹理叠层。它是系统指纹，绝不该去掉。
- 用 `{spacing.pad-x}` 7.5vw / `{spacing.pad-y}` 5.5vh 留白，Signal 需要呼吸空间，紧内边距会破掉编辑克制。

### 不该做

- 不要把金用在正文文字上，也不要用金填充背景。金只出现在线、斜体强调、数字上。
- 不要在海军蓝上用纯白（`#FFFFFF`）作文字。始终用 `{colors.text-warm}`，暖米白才把系统系在纸语域上。
- 不要加投影或圆角卡片外壳。系统是扁平加细线，抬升会破掉编辑画框。
- 不要把衬线用在正文或段落文字上。衬线 / 无衬线分离是结构性的，衬线领衔，无衬线支撑。
- 不要在正文里用粗体强调。改用斜体衬线金色 `<em>` 式样，换字面才是强调。
- 不要给外壳、面板、统计块、图片框加圆角。系统里仅有的圆形是环形图与 9px 时间轴圆点。
- 不要引入第二种强调色。古金是唯一的暖色，加第二强调会稀释它的分量。
- 不要让内容填满典型一页超过一半。系统一挤就读作坏了，克制才是语域。
- 不要在元数据角色（标签、眉题、外壳、计数器、图注注）之外用等宽。正文或标题里的等宽会破掉排印阶梯。
- 不要省掉外壳下方或统计块上方的 1px 细线。细线是系统的纵深替代物，没它们元素就漂浮。

## 响应式行为

Signal 以 1920×1080 视口为目标，但完全用视口相对单位（`vw`、`vh`）实现，于是在 1280×720 与 2560×1440 间无需断点便流式缩放。80px 网格纹理是唯一跨视口变化仍保留的固定像素度量，视口越大它在比例上越细。

### 缩放行为

- 展示标题随视口缩放：1920px 下 9.5vw 渲染约 182px，1280px 下约 122px。
- 正文缩放：1.05vw → 1920px 下约 20px，1280px 下约 13px。
- 内边距缩放：pad-x 7.5vw → 1920px 下约 144px，1280px 下约 96px。

### 放映行为

文稿由 JS 驱动。页经导航条前进（在文稿容器上 translateX），导航点与页码固定在底部。当前页带 `is-active`，带 `[data-anim]` 属性的元素经 fade-up、fade-in、reveal-right、reveal-left、scale-in 关键帧配错峰 `data-delay`（0–6）入场。动画短（0.5–0.85s），用锐利的 `cubic-bezier(0.77, 0, 0.175, 1)` 平移缓动与带弹性的 `cubic-bezier(0.16, 1, 0.3, 1)` 入场缓动。

### 打印行为

没有专用打印样式表。静态导出应把每页渲染成顺序的一页，文稿容器的横向布局需为打印保真而解开。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁 | 中文 | 字重映射 |
|---|---|---|---|
| 展示 / 标题（h1、h2、h3）/ 统计值 / 引文文字 / 编辑标题 / 密集标题 | Source Serif 4（500–700） | **思源黑体 Noto Sans SC** | 700 |
| 导语 / 正文 / 图注 | DM Sans（400） | **思源黑体 Noto Sans SC** | 400 |
| 标签 / 眉题 / 外壳 / 页码 | IBM Plex Mono（500） | **思源黑体 Noto Sans SC** | 500（去掉全大写 + 字距） |

### 混排策略

**策略 A：所有角色用单一 CJK 字族（思源黑体 Noto Sans SC）。** Signal 的拉丁系统已经把 Noto Serif SC 与 Noto Sans SC 接进每条 font-family 栈作回退，系统在设计时就考虑了 CJK。推荐的归并是**每个角色都用 Noto Sans SC**，而非混用 Noto Serif SC（展示）+ Noto Sans SC（正文），理由正是系统最鲜明的处理：标题里的金色斜体 `<em>` 强调。Noto Serif SC 不提供斜体轴，意味着 Signal 瞬间（句中正体切斜体的换色）在中文里无法复现。全系统塌到 Noto Sans SC、给 CJK `<em>` 保留仅换色强调（金而不斜体），比跟一款没有斜体的衬线较劲更干净。定义拉丁阶梯的衬线对无衬线反差在 CJK 里会丢，但系统的编辑克制，细线、等宽眉题、古金点缀、双表面，不受影响地带过来。

### 加载

系统已经通过既有 font-family 栈加载 Noto Sans SC。若用 CDN preconnect 式样：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

既有 CSS 变量已经在每条字体栈里含 Noto Sans SC 与 Noto Serif SC。以中文为主的文稿，把衬线栈换成用 Noto Sans SC 作活跃 CJK 字面（而非 Noto Serif SC），让整套系统塌成一款中文字族：
```css
/* Display / headline roles (CJK-primary) */
font-family: 'Source Serif 4', 'Noto Sans SC', Georgia, serif;
/* Body roles */
font-family: 'DM Sans', 'Noto Sans SC', system-ui, sans-serif;
/* Mono roles */
font-family: 'IBM Plex Mono', 'Noto Sans SC', monospace;
```

### 通用 CJK 调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 设 0
- 文字变换：CJK 不用 uppercase
- 全角标点
- 展示标题不加句号
- 盘古之白（Pangu spacing）：`使用 Claude` 而非 `使用Claude`
- 一句一款字体

### 本系统的美学提示

- **Signal 瞬间（句中斜体金色 `<em>`）在 CJK 里变成仅换色。** Noto Sans SC 没有斜体变体，连 Noto Serif SC 出厂也无斜体。中文标题里把 `<em>` 渲染成切到 `{colors.gold}` 的换色、*不带*斜体，强调仍成立，因为金是系统负载最重的颜色。把这看作 Signal 瞬间在 CJK 里被有意译到它仅换色的精髓。
- **展示上的负字距（display -0.02em、h1/h2 -0.01em）在 CJK 上必须降到 0。** 系统的紧字距是拉丁展示惯例，会破掉 CJK 渲染。
- **IBM Plex Mono 全大写、0.14–0.22em 字距的等宽眉题仅适用于拉丁。** CJK 眉题把字距降到 0，靠金色 + 小尺寸标示"这是眉题"。混排 CJK + 拉丁的眉题（`第一章 / CHAPTER ONE`）可让拉丁半边保留字距、CJK 半边字距为 0，这种非对称等宽声部读作编辑式双语。
- **Source Serif 4 600 金色的统计数字**保持拉丁数字（现代编辑设计里西方数字表统计是通用惯例）。别换成中文数字（一二三四），它们会丢掉目录统计声部。
- **破折号项目（等宽金色 `—`）完美迁移**，破折号项目在中文排印里同样地道。
- **80px 网格纹理、细线边框、双表面（海军蓝 + 奶油）、金线、章节页、满幅图片遮罩、无外壳陈述布局**都与字形无关。编辑克制与情报简报语域不受影响地带过来。
- **CJK 正文行高应从 1.58–1.72 放宽到 1.75–1.85**，汉字占满 em 框，在系统的正文尺寸（1.05vw、1.4vw）下需要额外纵向呼吸才易读。
- **引号字形（8vw 装饰性起始引号）**应换成中文起始引号（「）或弯引号（"），拉丁起始引号字形落在中文引文上读作外来物。

### 已知 CJK 缺口

系统最鲜明的排印处理（Source Serif 4 标题里句中正体 + 斜体金）根本上是拉丁排印动作，迁移不过来。Noto Serif SC 与 Noto Sans SC 都没有斜体轴，靠 CSS `font-style: italic` 造一个会产出倾斜 / 斜切字形，读作坏了而非强调。把 CJK `<em>` 塌成仅换色（金而不斜体）是最干净的变通，强调短语为拉丁（因而能取斜体金）、周围句子为中文的混语标题，会是 Signal 瞬间在 CJK 里最有力的落地。

## 迭代指南

1. 任何新标题都用 Source Serif 4，且可在句中带一个斜体金色 `<em>`。标题若没有强调短语，想想它是否该有，Signal 声部依赖金色斜体瞬间出现。
2. 任何新区域分隔都是 `{colors.border-dark}` / `{colors.border-light}` 的 1px 细线。绝不更粗、绝不上色、绝不用阴影。
3. 任何新标签、眉题、外壳元素都是等宽全大写，眉题用 `{colors.gold}`、外壳用该表面合适的柔化色。字距至少 0.14em。
4. 任何新统计数字都用 -0.02em 字距的 `{colors.gold}` Source Serif 4 600。统计始终是金色衬线，与表面无关。
5. 任何新强调处理都用 `{colors.gold}`，没有第二强调。页需要更多视觉区分时，变表面（海军蓝对奶油），而非加颜色。
6. 任何新项目列表都用等宽金色破折号标记。加别的项目样式会破掉系统。
7. 封面、章节、陈述、引文、收尾布局无外壳，标准布局带外壳与页脚。别混，无外壳陈述是对的，带外壳陈述读作另一套系统。
8. 80px 网格叠层属于深色表面身份。任何新深色页都应继承 `.slide.dark`，好让 `::before` 叠层自动生效。
9. 新布局应保住编辑呼吸空间。布局若需要内容从边到边，重新想想，Signal 是克制系统。
10. 正文里的斜体始终意味着把 font-family 切到 `{colors.gold}` 的斜体 Source Serif 4。斜体 DM Sans 不是系统基元。

## 已知缺口

- 四款字族在运行时从 Google Fonts 加载。字体加载失败（网络问题、广告拦截器）时，回退是 Georgia（衬线）、system-ui（无衬线）、Courier 式等宽，结果渲染会丢掉大量编辑性格，但仍可读。
- 中文回退（Noto Serif SC、Noto Sans SC）接进了每条 font-family 栈，但度量与拉丁字面略有不同，纯中文文稿会读起来略紧。
- 80px 网格纹理是个绑在视口尺度上的魔法数字，视口极大（>2560px）时，网格可能开始显得粗而非不可察觉。
- 翻页由 JavaScript 驱动，在文稿容器上用硬编码的 `transform: translateX(...)`。系统依赖这套引擎，替换它必须保住 `is-active` 类行为，动画才会触发。
- `--c-bg-alt`、`--c-bg-light-alt` 与若干柔化颜色 token 有定义但用得省，它们作为相邻表面区分的储备存在，源模板只是偶尔用到。
- 金字塔布局用 `color-mix(in srgb, ...)`，要求现代浏览器支持，较旧浏览器可能把带渲染成平填充而非分层。
- 满幅页渐变硬编码为 `rgba(15, 20, 36, 0.9)`（接近海军蓝但未参数化成 token）。改海军蓝色需同步更新这条渐变。
