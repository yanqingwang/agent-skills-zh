---
version: alpha
name: Blue Professional
description: A restrained, consulting-grade presentation system on a warm cream canvas (#fdfae7) with a single saturated cobalt blue (#1e2bfa) as the only accent color. Display type runs Space Grotesk for headlines and numerical callouts; Inter handles body and chrome. Cards are soft-tinted cobalt at 4% opacity with 1.5px translucent borders and 10-14px rounded corners — quiet, never bordered in solid color. The aesthetic borrows from investment-research reports, McKinsey-grade quarterly briefings, and contemporary financial dashboards — measured, data-dense without feeling crowded, and unmistakably professional. The system is built for executive readability at distance, with strong typographic hierarchy and a single accent color carrying every emphasis moment.

colors:
  bg: "#fdfae7"
  primary: "#1e2bfa"
  text: "#111111"
  text-muted: "#6b6b6b"
  text-light: "#9a9a9a"
  accent-light: "rgba(30, 43, 250, 0.08)"
  accent-medium: "rgba(30, 43, 250, 0.15)"
  border: "rgba(30, 43, 250, 0.2)"
  card-bg: "rgba(30, 43, 250, 0.04)"
  positive: "#059669"
  negative: "#dc2626"

typography:
  h1:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: "clamp(44.8px, 5vw, 67.2px)"
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(28.8px, 3vw, 41.6px)"
    lineHeight: 1.1
    letterSpacing: -0.02em
  h3:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: "clamp(17.6px, 1.8vw, 24px)"
    lineHeight: 1.3
    letterSpacing: -0.02em
  h4-eyebrow:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(13.6px, 1.2vw, 16px)"
    lineHeight: 1.1
    letterSpacing: 0.08em
    textTransform: uppercase
    color: "{colors.primary}"
  body:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 400
    fontSize: "clamp(13.6px, 1.1vw, 16.8px)"
    lineHeight: 1.6
    color: "{colors.text-muted}"
  metric-value:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: "clamp(35.2px, 3.4vw, 48px)"
    lineHeight: 1
    color: "{colors.primary}"
  metric-label:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 600
    fontSize: "clamp(15.2px, 1.3vw, 17.6px)"
    lineHeight: 1.3
    color: "{colors.text}"
  metric-desc:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 400
    fontSize: "clamp(12.5px, 0.95vw, 14.4px)"
    lineHeight: 1.5
    color: "{colors.text-muted}"
  metric-support:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 400
    fontSize: "clamp(12px, 0.9vw, 13.6px)"
    lineHeight: 1.45
    color: "{colors.text-muted}"
  stat-num:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: "clamp(25.6px, 2.4vw, 33.6px)"
    lineHeight: 1
    color: "{colors.primary}"
  stat-name:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 500
    fontSize: "clamp(13.6px, 1vw, 15.2px)"
    lineHeight: 1.35
    color: "{colors.text}"
  stat-context:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 400
    fontSize: 12px
    lineHeight: 1.4
    color: "{colors.text-light}"
  agenda-num:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: 28.8px
    lineHeight: 1
    color: "{colors.primary}"
  insight-num:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 12.5px
    lineHeight: 1.7
    letterSpacing: 0.05em
    color: "{colors.primary}"
  split-highlight:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: "clamp(18.4px, 1.55vw, 24px)"
    lineHeight: 1.4
    color: "{colors.text}"
  blockquote:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: "clamp(25.6px, 2.8vw, 38.4px)"
    lineHeight: 1.35
    color: "{colors.text}"
  quote-mark:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: "128px"
    lineHeight: 0.5
    color: "{colors.primary}"
    opacity: 0.15
  step-circle-text:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: 20.8px
    lineHeight: 1
  step-title:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(15.2px, 1.4vw, 18.4px)"
    lineHeight: 1.2
  bar-label:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 500
    fontSize: "clamp(12.8px, 1.1vw, 16px)"
    lineHeight: 1.3
    color: "{colors.text}"
  bar-pct:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 15.2px
    color: "{colors.primary}"
  tag:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: 12px
    lineHeight: 1
    color: "{colors.primary}"
  counter:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: 12.8px
    lineHeight: 1
    letterSpacing: 0.05em
    color: "{colors.text-muted}"
  meta:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 400
    fontSize: 12.8px
    lineHeight: 1.4
    letterSpacing: 0.05em
    color: "{colors.text-light}"
  cite:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: 12.5px
    lineHeight: 1.4
    letterSpacing: 0.04em
    textTransform: uppercase
    color: "{colors.text-muted}"

spacing:
  pad-slide-x: "4vw"
  pad-slide-y-top: "3.5vw"
  pad-slide-y-bottom: "8.5vh"
  pad-card-lg: "1.5rem 1.6rem"
  pad-card-md: "1.4rem 1.5rem"
  pad-card-sm: "1rem 1.2rem"
  pad-mini: "0.9rem 1rem"
  gap-grid-lg: "3.5rem"
  gap-grid-md: "2rem 3rem"
  gap-grid-sm: "1.5rem"
  gap-cards: "1.2rem"
  gap-mini: "1rem"
  header-margin: "2.5vh"
  accent-line-width: "60px"
  accent-line-height: "4px"

canvas:
  width: 100vw
  height: 100vh
  background: "{colors.bg}"

radii:
  pill: "100px"
  card-lg: "14px"
  card-md: "12px"
  card-sm: "10px"
  bar: "6px"
  circle: "50%"

components:
  card-tinted:
    background: "{colors.card-bg}"
    border: "1.5px solid {colors.border}"
    borderRadius: 14px
    padding: "1.5rem 1.6rem"
    description: "Primary content card. Cobalt tinted at 4% with a 20% cobalt 1.5px border. Soft 14px radius. Never solid-colored, never outlined in full primary."
  card-tinted-sm:
    background: "{colors.card-bg}"
    border: "1px solid {colors.border}"
    borderRadius: 12px
    padding: "1.4rem 1.5rem"
    description: "Compact tinted card with 1px border. Used for stat cells and small data blocks."
  card-tinted-xs:
    background: "{colors.card-bg}"
    border: "1px solid {colors.border}"
    borderRadius: 10px
    padding: "0.9rem 1rem"
    description: "Mini tinted card used for inline mini-stats."
  detail-block:
    background: "{colors.card-bg}"
    border: "1px solid {colors.border}"
    borderRadius: 10px
    padding: "1rem 1.2rem"
    description: "Detail block holding a small h3 + a bulleted ul. Used in detail-analysis grids."
  tag-pill:
    background: "{colors.accent-light}"
    color: "{colors.primary}"
    padding: "0.35rem 0.9rem"
    borderRadius: 100px
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: 12px
    description: "Pill-shaped tag sitting in the top-right of the slide-header. Fully rounded, soft cobalt tint background, cobalt text."
  cta-button:
    background: "{colors.primary}"
    color: "{colors.bg}"
    padding: "0.9rem 2.2rem"
    borderRadius: 100px
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 15.2px
    description: "Primary CTA. Fully rounded solid cobalt pill with cream text. Hover lifts -2 with a soft cobalt drop shadow."
  nav-btn:
    width: 44px
    height: 44px
    borderRadius: 50%
    border: "1.5px solid {colors.border}"
    background: "{colors.bg}"
    color: "{colors.primary}"
    description: "Circular nav-arrow button. Hover inverts: cobalt fill, cream icon. Disabled state at 30% opacity."
  accent-line:
    width: 60px
    height: 4px
    background: "{colors.primary}"
    borderRadius: 2px
    description: "Short horizontal cobalt rule, 60×4px, slightly rounded. Used above cover titles and as eyebrow separators."
  accent-dot:
    width: 8px
    height: 8px
    background: "{colors.primary}"
    borderRadius: 50%
    description: "Small inline cobalt dot. Decorative inline marker."
  bar-track:
    height: 28px
    background: "{colors.accent-light}"
    borderRadius: 6px
    description: "Horizontal bar chart track. Soft cobalt tint with 6px rounded corners."
  bar-fill:
    height: "100%"
    background: "{colors.primary}"
    borderRadius: 6px
    description: "Solid cobalt fill inside bar-track. Width carries the data value. Animates from 0 to value on slide entry."
  step-circle:
    width: 56px
    height: 56px
    borderRadius: 50%
    background: "{colors.primary}"
    color: "{colors.bg}"
    description: "Circular numbered step marker in cobalt with cream numeral. Sequential steps reduce opacity (1.0 → 0.85 → 0.7 → 0.55) to suggest fade-into-future."
  metric-change-positive:
    color: "{colors.positive}"
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 12.5px
    description: "Inline positive-change chip with up-arrow glyph and percentage. Green text inline; no border or fill."
  metric-change-negative:
    color: "{colors.negative}"
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 12.5px
    description: "Inline negative-change chip with up/down-arrow glyph and percentage. Red text inline; no border or fill."
  insight-list-item:
    paddingLeft: "2.6rem"
    description: "Numbered insight list with a Space Grotesk 600 counter (decimal-leading-zero) at position absolute left. Numbers in cobalt, body in default text color."
  split-highlight-block:
    background: "{colors.accent-light}"
    borderLeft: "4px solid {colors.primary}"
    borderRadius: 12px
    padding: "1.3rem 1.5rem"
    description: "Highlighted callout block with cobalt left rule and tinted cobalt fill. Used for inline pull-quotes inside split-column layouts."
  progress-bar:
    position: "fixed bottom 0 left 0"
    height: 3px
    background: "{colors.primary}"
    description: "Thin cobalt progress bar at the bottom edge of the viewport, width grows linearly with slide index."
  cover-decoration:
    background: "{colors.accent-light}"
    clipPath: "polygon(30% 0, 100% 0, 100% 100%, 0% 100%)"
    description: "Diagonal accent panel filling the right ~35% of cover surfaces. Soft cobalt tint, clip-path angled cut on the left edge."
  cover-dots:
    layout: "3x3 grid of 6px cobalt dots at 12px gap, 25% opacity"
    description: "Small dotted decoration used on cover and other open-space surfaces."
  closing-circles:
    border: "1px solid {colors.border}"
    borderRadius: "50%"
    description: "Two concentric centered circles (500px outer, 360px inner) as atmospheric decoration on closing-class surfaces. Opacity 0.3-0.4."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/blue-professional/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Blue Professional 是一套**咨询级演示系统**，为高管简报、研究交付物与季度复盘而设计。它的底层视觉前提是**克制加一项强承诺**：暖奶油画布（`{colors.bg}` — `#fdfae7`）配一色饱和钴蓝（`{colors.primary}` — `#1e2bfa`），由它承载每一处强调、每一个指标、每一个 CTA、每一条眉题、每一条图表填充。没有次级品牌色，没有浅彩调色板，没有冷暖对搭，只有奶油、钴蓝，以及给正文文字用的一小段柔和灰阶。

字体系统用两款开源 Google Fonts，各守严密定义的角色。**Space Grotesk**（字重 300-700）是展示、标题、数字与外壳字面，用于 h1-h3 标题、所有指标/统计数字、眉题标签（大写、0.08em 字距）、标签胶囊、CTA、页码、议程编号与步骤圆。它略带几何的性格加柔和的人文暖意，读起来既现代（适合 AI/科技受众）又可信（适合金融受众）。**Inter**（字重 300-600）是正文字面，用于段落文字、列表正文、指标说明和表格化内容。Space Grotesk / Inter 的搭配刻意普通，让系统显得独特的是用法的纪律，不是字面本身有多新奇。

色彩理念是**一种强调色，三级文字灰**。钴蓝包揽全部强调：标题保持 `{colors.text}`（近黑 `#111111`），但每个指标值、每条眉题、每个 CTA、每根图表条、每个标注边框、每个步骤圆、每个进度指示都是钴蓝。正文文字用三级灰阶：`{colors.text}` 作主正文，`{colors.text-muted}`（`#6b6b6b`）作段落正文与指标说明，`{colors.text-light}`（`#9a9a9a`）作三级元数据。只有两种非钴蓝的强调色存在：`{colors.positive}`（柔和绿 `#059669`）与 `{colors.negative}`（柔和红 `#dc2626`），只用于方向变化指示（指标卡片上的箭头与百分比），而且是行内文字色，不是填充。

纵深是**柔和且带色调的**，从不做偏移或阴影。卡片是 4% 钴蓝淡色（`{colors.card-bg}`），配 1.5px 半透明钴蓝边（`{colors.border}`，钴蓝 20% 不透明度）与 10-14px 圆角。除 CTA 悬停态上唯一一枚微妙的钴蓝淡影（`0 8px 24px rgba(30, 43, 250, 0.25)`），系统没有投影。没有刺眼阴影，正是它安静、高级感的来源：每一处抬升都由边框 + 淡色暗示，不靠阴影。

**密度取向：均衡、数据密而不挤。** 这套系统生来承载信息：六指标仪表盘、六细节块网格、七条排名、带标注与迷你统计的多栏分栏。填入实质内容时它显得权威，稀疏时显得怯。典型一页承载：slide-header（h4 眉题 + 标签胶囊）+ 一个分节 h2 标题 + 3-6 个信息单元格的网格或列表。卡片内部内边距中等（1.5rem）、卡间间隙中等（1.2-1.5rem），既不紧也不空。系统既能撑起引文/封面类表面（空间里一句强陈述），也能撑起仪表盘类表面（六张密数据卡片），而不会像两套系统。

**关键特征：**
- 每处表面都是暖奶油底（`{colors.bg}`），绝不纯白，绝不灰。
- 单一饱和钴蓝（`{colors.primary}`）作唯一强调色，用于每条眉题、指标、CTA、图表填充与进度指示。
- Space Grotesk（展示 + 外壳）+ Inter（正文），两者都不得替换。
- 卡片是 4% 钴蓝淡色，配 20% 钴蓝的 1.5px 边与 10-14px 圆角。
- 柔和胶囊形外壳（`{components.tag-pill}`、`{components.cta-button}`）用满 `100px` border-radius。
- 标题用 Space Grotesk 字重 600-700、-0.02em 字距、近黑文字色。
- 正文用 Inter 字重 400、13.6-16.8px、行高 1.6、柔和灰。
- 每页都带 slide-header（眉题 + 标签胶囊）、单个 h2 与弹性内容区，整份文稿里这个结构有节奏地重复。
- 常驻外壳：底边钴蓝进度条、左下页码、右下圆形导航箭头。
- 装饰性氛围元素（同心圆、点网格、斜向强调面板）只出现在封面与收尾类表面。

## 颜色

### 调色板

- **Bg**（`{colors.bg}` — `#fdfae7`）：暖奶油画布。默认且通用的表面。略偏绿奶油的暖意，把系统与公司模板白区分开。每页都落在这个底上。
- **Primary**（`{colors.primary}` — `#1e2bfa`）：招牌钴蓝。高饱和电光蓝，承载每一处强调瞬间。用于 h4 眉题、指标值、统计数字、图表条填充、CTA 填充、步骤圆、进度条、强调线、议程编号，以及高亮块上的 cite 边。没有别的强调色。
- **Text**（`{colors.text}` — `#111111`）：主文字色。近黑、比 `#000000` 略暖。用于 h1-h3 标题、主内容文字、指标标签，以及任何该有全部分量的文字。
- **Text-muted**（`{colors.text-muted}` — `#6b6b6b`）：次级文字，用于正文段落、指标说明、图注。比主文字柔和得舒服，又不会消失。
- **Text-light**（`{colors.text-light}` — `#9a9a9a`）：三级文字，用于页面元信息、文字里的细线分隔、统计上下文行。可读灰里最浅的一档；再往下文字就成环境噪声了。
- **Accent-light**（`{colors.accent-light}` — `rgba(30, 43, 250, 0.08)`）：标签胶囊、条轨、高亮标注与封面装饰面板的默认钴蓝淡色。
- **Accent-medium**（`{colors.accent-medium}` — `rgba(30, 43, 250, 0.15)`）：略深的钴蓝淡色，可用，但用得省。
- **Border**（`{colors.border}` — `rgba(30, 43, 250, 0.2)`）：20% 不透明度钴蓝。卡片、导航按钮、装饰圆与结构分隔线的通用柔和边框色。
- **Card-bg**（`{colors.card-bg}` — `rgba(30, 43, 250, 0.04)`）：4% 不透明度钴蓝。通用卡片填充，比 accent-light 更淡，读起来是一层几乎无色的表面，从奶油底上微微抬起。
- **Positive**（`{colors.positive}` — `#059669`）：柔和绿。只作正向变化指示（上箭头 + 百分比）的行内文字色。绝不做填充或边框。
- **Negative**（`{colors.negative}` — `#dc2626`）：柔和红。只作负向变化指示的行内文字色。绝不做填充或边框。

### 默认值

- **默认表面背景**：`{colors.bg}`，每处表面都从奶油起。
- **默认标题色**：`{colors.text}`（`#111111`），标题近黑，绝不钴蓝。钴蓝只留给强调瞬间（眉题、指标、CTA）。
- **默认正文文字色**：`{colors.text-muted}`（`#6b6b6b`），正文段落默认柔和灰，不是全黑。
- **默认眉题 / h4 色**：`{colors.primary}`，眉题始终钴蓝、始终大写、始终 0.08em 字距。
- **默认卡片填充**：`{colors.card-bg}`（4% 钴蓝），通用柔和淡色。
- **默认卡片边框**：`{colors.border}`（20% 钴蓝）1px 或 1.5px。绝不用全钴蓝实线边。
- **默认卡片圆角**：按卡片大小取 10-14px（统计单元格用 `{radii.card-sm}`，统计卡片与细节块用 `{radii.card-md}`，指标卡片用 `{radii.card-lg}`）。
- **任何数值的默认强调色（指标、统计、议程编号、条百分比）**：`{colors.primary}`。
- **默认图表条色**：`{colors.accent-light}` 轨道上的 `{colors.primary}` 实填充。
- **默认 CTA**：`{components.cta-button}`，实钴蓝胶囊配奶油文字、100px border-radius。
- **默认标签胶囊**：`{components.tag-pill}`，柔和钴蓝淡色配钴蓝文字、100px border-radius，与 slide-header 里的 h4 眉题成对出现。

系统**没有次级强调色**。别去拿橙、青、紫来区分类别，单一钴蓝纪律就是系统的身份。类别区分要靠位置、尺寸或标签，不靠多加色相。

## 排印

### 字族栈
系统用两款字面，各守一个角色。

**Space Grotesk**（Google Fonts，字重 300-700）是展示 + 数字 + 外壳字面。用于每个 h1、h2、h3、h4 标题；每个数字标注（指标值、统计数字、议程编号、条百分比、步骤圆）；每个外壳元素（标签胶囊、CTA、页码、提示文字）；以及每个 0.08em 字距的大写眉题。它略带几何的性格加柔和圆润的人文形态，读起来既当代又可信，AI/科技与金融受众都合适。

**Inter**（Google Fonts，字重 300-600）是正文字面。用于段落文字、列表正文、指标说明、议程说明、细节块正文，以及任何较长的内容。设字重 400、行高 1.6、柔和灰，Inter 读起来舒服、宽裕、有编辑感。

两个字面角色不重叠：Space Grotesk 管每个数字、每个标题；Inter 管每个段落、每段列表正文。别越界，Inter 的 h1 读起来像另一个品牌，Space Grotesk 的正文读起来像科技创业公司落地页。

### 排印比例

| Token | 尺寸（clamp / px） | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.h1}` | 44.8–67.2px clamp | Space Grotesk | 700 | 封面或收尾标题 |
| `{typography.h2}` | 28.8–41.6px clamp | Space Grotesk | 600 | 每页分节主标题 |
| `{typography.h3}` | 17.6–24px clamp | Space Grotesk | 500 | 议程项 / 区域标题 |
| `{typography.h4-eyebrow}` | 13.6–16px clamp | Space Grotesk | 600 | slide-header 里的大写眉题（始终钴蓝） |
| `{typography.body}` | 13.6–16.8px clamp | Inter | 400 | 标准正文段落 |
| `{typography.metric-value}` | 35.2–48px clamp | Space Grotesk | 700 | 标注卡片里的大指标数字 |
| `{typography.metric-label}` | 15.2–17.6px clamp | Inter | 600 | 数字下方的指标标签行 |
| `{typography.metric-desc}` | 12.5–14.4px clamp | Inter | 400 | 指标辅助说明段落 |
| `{typography.metric-support}` | 12–13.6px clamp | Inter | 400 | 指标辅助项目列表 |
| `{typography.stat-num}` | 25.6–33.6px clamp | Space Grotesk | 700 | 统计单元格数字（小于 metric-value） |
| `{typography.stat-name}` | 13.6–15.2px clamp | Inter | 500 | 统计单元格描述名行 |
| `{typography.stat-context}` | 12px | Inter | 400 | 细线分隔下方的统计单元格三级上下文行 |
| `{typography.agenda-num}` | 28.8px | Space Grotesk | 700 | 议程项数字 |
| `{typography.insight-num}` | 12.5px | Space Grotesk | 600 | 洞察列表项上的计数器式数字前缀 |
| `{typography.split-highlight}` | 18.4–24px clamp | Space Grotesk | 500 | split-highlight 块内的行内拉页引文文字 |
| `{typography.blockquote}` | 25.6–38.4px clamp | Space Grotesk | 500 | 引文类标题正文 |
| `{typography.quote-mark}` | 128px | Space Grotesk | 700 | blockquote 上方 15% 不透明度的装饰超大引号字形 |
| `{typography.step-circle-text}` | 20.8px | Space Grotesk | 700 | 圆形步骤标记内数字 |
| `{typography.step-title}` | 15.2–18.4px clamp | Space Grotesk | 600 | 步骤圆下方的步骤标题 |
| `{typography.bar-label}` | 12.8–16px clamp | Inter | 500 | 条形图行标签 |
| `{typography.bar-pct}` | 15.2px | Space Grotesk | 600 | 条形图行百分比数值 |
| `{typography.tag}` | 12px | Space Grotesk | 500 | slide-header 里的标签胶囊文字 |
| `{typography.counter}` | 12.8px | Space Grotesk | 500 | 常驻页码 |
| `{typography.meta}` | 12.8px | Space Grotesk | 400 | 封面元信息行（例如日期 / 保密标记） |
| `{typography.cite}` | 12.5px | Space Grotesk | 500 | 拉页引文下方的引文/出处，大写配 0.04em 字距 |

### 默认值

- **封面标题默认尺寸**：`{typography.h1}`（44.8–67.2px）。始终 Space Grotesk 字重 700、-0.02em 字距。
- **每页分节主标题默认尺寸**：`{typography.h2}`（28.8–41.6px）。Space Grotesk 字重 600。"分节 h2" 是系统的结构主力，每张内容页都有一个。
- **区域或议程项标题默认尺寸**：`{typography.h3}`（17.6–24px）。
- **h2 上方眉题默认尺寸**：`{typography.h4-eyebrow}`（13.6–16px），钴蓝、大写、0.08em 字距。
- **段落正文默认尺寸**：`{typography.body}`（13.6–16.8px clamp）。Inter 字重 400、行高 1.6。
- **大指标数字默认尺寸**：`{typography.metric-value}`（35.2–48px）。仪表盘统计单元格降一档到 `{typography.stat-num}`（25.6–33.6px）。
- **引文正文默认尺寸**：`{typography.blockquote}`（25.6–38.4px）。始终 Space Grotesk 字重 500。
- **Space Grotesk 标题默认字重**：500（h3）→ 600（h2 与眉题）→ 700（h1 与数字标注）。别去取字重 400 或 800，字重阶梯是固定的。
- **Inter 正文默认字重**：400。Inter 正文 500-600 太强势，300 太细。
- **h1-h3 标题默认字距**：-0.02em。没有负字距，Space Grotesk 展示读起来像没处理过。
- **h4 眉题默认字距**：0.08em 大写。没有宽字距 + 大写的组合，眉题就读不成眉题。

拿不准该用哪个标题 token 时，页面主要文字瞬间默认取 `{typography.h2}`（28.8–41.6px）。`{typography.h3}` 留给区域或议程项标题，`{typography.h1}` 只留给封面与收尾。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每个 h4 眉题都是 Space Grotesk 字重 600、`{colors.primary}` 钴蓝、大写、0.08em 字距。** 没有例外。缺了大写 + 字距 + 钴蓝的眉题不是系统的眉题，只是一段游离的无衬线文字。
- **每个标题（h1、h2、h3）都用 -0.02em 负字距。** 默认字距的 Space Grotesk 展示读起来没处理过，会破掉编辑纪律。
- **每个标题都用 `{colors.text}`（`#111111`），不用钴蓝。** 钴蓝标题禁用，钴蓝只留给强调瞬间（眉题、指标、CTA、图表条）。反过来会压塌视觉层级。
- **每个数字标注（指标值、统计数字、议程编号、条百分比、步骤圆）都是 Space Grotesk 字重 600-700 的 `{colors.primary}` 钴蓝。** 数值是系统主要的强调瞬间。
- **每个正文段落都是 Inter 字重 400、`{colors.text-muted}`（`#6b6b6b`）、行高 1.6。** 纯黑正文太重，text-light 正文太淡。
- **每个 CTA 都是 `{components.cta-button}` 模式：实钴蓝胶囊配奶油文字、100px border-radius、0.9rem × 2.2rem 内边距。** 别的形状或颜色的 CTA 不存在。
- **每个标签胶囊都是 `{components.tag-pill}` 模式：柔和钴蓝淡色配钴蓝文字、100px border-radius、0.35rem × 0.9rem 内边距。** 实底或带边的标签胶囊会破掉系统。
- **每个 slide-header 都把 h4 眉题放左、标签胶囊放右。** 这是每张内容页的结构节奏。

### 排印原则

声部对比是**近黑展示标题 ↔ 钴蓝眉题 + 数字 ↔ 柔和灰正文**。不用斜体，不用下划线。强调机制只有三样：在 Space Grotesk 阶梯内切字重、把颜色从 text-muted 切到 text 或钴蓝、标签上的大写 + 字距。

数字内容**始终用 Space Grotesk**，连很小的数字标签（条百分比、页码、迷你统计值）也一样。Space Grotesk 在数字尺寸下的准等宽性格能模仿表格数字，不必真用等宽字面。

## 布局

### 画布系统
系统以每页 `100vw × 100vh` 为目标。幻灯片绝对定位，入场用 opacity + translateX（40px → 0px）动画，500ms ease。只有 `.active` 页是 `opacity: 1`；前一页得到 `.prev` 类并平移 -40px 移出视野。

默认幻灯片内边距不对称：左、上、右 `3.5vw`，底 `8.5vh`。多出的底部空间给固定在 `bottom: 2.5vh`、压在视口底边的页码（左）与导航控件（右）留位。

### 内边距与间隙比例

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-slide-x}` | 4vw | 幻灯片横向内边距 |
| `{spacing.pad-slide-y-top}` | 3.5vw | 幻灯片顶部内边距 |
| `{spacing.pad-slide-y-bottom}` | 8.5vh | 幻灯片底部内边距（额外给导航外壳让位） |
| `{spacing.pad-card-lg}` | 1.5rem 1.6rem | 大卡片内部内边距（指标卡片） |
| `{spacing.pad-card-md}` | 1.4rem 1.5rem | 中等卡片内部内边距（统计单元格） |
| `{spacing.pad-card-sm}` | 1rem 1.2rem | 小卡片内部内边距（细节块） |
| `{spacing.pad-mini}` | 0.9rem 1rem | 迷你卡片内部内边距（迷你统计单元格） |
| `{spacing.gap-grid-lg}` | 3.5rem | 分栏之间的大间隙 |
| `{spacing.gap-grid-md}` | 2rem 3rem | 双栏网格里的中等间隙（行 × 列） |
| `{spacing.gap-grid-sm}` | 1.5rem | 三列指标网格里的标准间隙 |
| `{spacing.gap-cards}` | 1.2rem | 仪表盘统计单元格之间的间隙 |
| `{spacing.gap-mini}` | 1rem | 迷你统计之间的间隙 |
| `{spacing.header-margin}` | 2.5vh | slide-header 下方的外边距 |

### 常驻外壳
每页都出现三个元素：
- **页码**在左下：Space Grotesk 12.8px 字重 500、text-muted 灰，固定在 `bottom: 2.5vh; left: 3vw`。
- **导航控件**在右下：两枚圆形 44px 导航按钮，带 20% 钴蓝的 1.5px 边，固定在 `bottom: 2.5vh; right: 3vw`。禁用态 30% 不透明度（首页 / 末页）。
- **进度条**在底边：3px 实钴蓝条，宽度 = `(currentSlide + 1) / total * 100%`。切页时动画。

底部居中还有一条**键盘提示**（"Use arrow keys to navigate"），text-light 灰。

### Slide-Header 结构
每张内容页顶部都有一条 `.slide-header` 带：左边 h4 眉题，右边标签胶囊。slide-header 下方是分节 h2，再是内容区（网格、列表、图表或分栏）。封面、引文、收尾页跳过 slide-header，改用居中内容。

### 内容网格
系统用重复的网格模式排内容：2×3 议程网格、三列指标行、三列统计网格（仪表盘上变两行）、1.05fr/1fr 分栏正文、四步时间轴行、双列细节网格。这些是内容密度容器，网格取哪种看内容量，不是固定布局语汇。

## 纵深与层级

### 淡色卡片（主要纵深机制）
系统用**柔和钴蓝淡底 + 柔和钴蓝边 + 圆角**造出抬升的印象，不用阴影。一张 `background: {colors.card-bg}`（4% 钴蓝）、`border: 1.5px solid {colors.border}`（20% 钴蓝）的卡片，没有任何实际偏移就视觉上浮在奶油底之上。这套处理就是系统的纵深语言。

### 卡片上无投影
卡片、统计单元格、细节块或任何内容容器上都没有 `box-shadow` 声明。系统唯一的阴影是 CTA 按钮上一枚柔和的钴蓝淡色悬停态：`0 8px 24px rgba(30, 43, 250, 0.25)`，悬停出现 200ms、移出消失。这是系统里唯一带色、带模糊的阴影。

### 左侧强调边（高亮块）
`{components.split-highlight-block}` 用 4px 实钴蓝左边发出信号："这是引文标注，与周围正文不同"。这是系统的结构强调机制，不是阴影，却承担同样的抬升暗示（彩色线把整块往前拉）。

### 圆角即柔和
卡片上的 10-14px border-radius 是纵深语言的一部分。没有圆角，钴蓝淡卡片会读成平板；柔和半径把它们软化成"被抬起"的表面。

### 氛围装饰
装饰元素（封面装饰斜面板、同心收尾圆、封面点网格、引文装饰圆）只出现在封面、引文、收尾类表面。它们是氛围，不是结构，用来柔化开放空间的表面而不往里塞内容。

## 形状与处理

### 圆角
- **`{radii.pill}` = 100px**：全圆。用于 `{components.tag-pill}`、`{components.cta-button}`，以及任何胶囊形外壳。
- **`{radii.card-lg}` = 14px**：大指标卡片。
- **`{radii.card-md}` = 12px**：标准统计单元格、split-highlight 块。
- **`{radii.card-sm}` = 10px**：细节块与迷你统计。
- **`{radii.bar}` = 6px**：条轨与条填充。
- **`{radii.circle}` = 50%**：步骤圆、导航按钮圆、强调点、收尾装饰圆、封面点、引文装饰圆。

半径阶梯是渐进的：小外壳用更紧的半径，大卡片用更大的半径，胶囊全圆，外壳用正圆。除进度条外，系统里**没有方角（0px）**。

### 边框粗细
- **1px 实线 `{colors.border}`**：通用柔和边。用于统计单元格、迷你统计、细节块、议程项（仅底边）、stat-context 分隔线（仅顶边）。
- **1.5px 实线 `{colors.border}`**：略重的柔和边。用于指标卡片、导航按钮。
- **2px 实线 `{colors.border}`**：分栏分隔线（分栏布局右列的 border-left）。
- **4px 实线 `{colors.primary}`**：只作 `{components.split-highlight-block}` 的左侧线，提示引文标注。

边框**从不是不透明钴蓝**，始终是 20% 不透明度（`{colors.border}`）。这正是系统安静、抬升质地的来源。

### 装饰元素类型

**淡色卡片**（`{components.card-tinted}`）：4% 钴蓝底、20% 钴蓝的 1.5px 边、14px 半径。主内容卡片。

**标签胶囊**（`{components.tag-pill}`）：8% 钴蓝的全圆胶囊，配钴蓝文字。位于 slide-header 右上。

**眉题**（`{typography.h4-eyebrow}`）：0.08em 字距的大写钴蓝标签。位于 slide-header 左上。

**CTA 按钮**（`{components.cta-button}`）：实钴蓝胶囊配奶油文字。系统唯一的实色元素，每个收尾表面用一次。

**强调线**（`{components.accent-line}`）：60×4 的短横钴蓝线，2px 半径。用于封面标题上方，以及开放空间表面上的眉题分隔。

**步骤圆**（`{components.step-circle}`）：56×56 实钴蓝圆，内含奶油 Space Grotesk 数字。连续时间轴步骤递减不透明度（1.0 → 0.85 → 0.7 → 0.55），暗示淡入未来。

**条轨 + 填充**（`{components.bar-track}` + `{components.bar-fill}`）：28px 高、8% 钴蓝的轨道，配实钴蓝填充，宽度承载数据。两者都是 6px 圆角。

**洞察列表项**（`{components.insight-list-item}`）：用 CSS counter() 渲染十进制补零前缀（"01"、"02"）的计数器编号列表，钴蓝 Space Grotesk 600 / 12.5px，绝对定位在左。

**Split highlight 块**（`{components.split-highlight-block}`）：8% 钴蓝淡块，配 4px 钴蓝左边线，下方一条 cite 行。用于分栏布局里的行内拉页引文。

**封面装饰**（`{components.cover-decoration}`）：裁剪过的斜向钴蓝淡面板，占封面表面右侧约 35%。读起来是印刷强调，不把布局框死。

**封面点**（`{components.cover-dots}`）：3×3 网格的 6px 钴蓝点、12px 间隙、25% 不透明度。开放空间表面上的装饰氛围。

**收尾圆**（`{components.closing-circles}`）：两个居中的同心圆（外 500px、内 360px），20% 钴蓝 1px 边，不透明度 0.3-0.4。收尾类表面的氛围装饰。

**指标变化小片**（`{components.metric-change-positive}` / `{components.metric-change-negative}`）：行内方向指示，一个小箭头字形 + 百分比数值，用 `{colors.positive}` 或 `{colors.negative}`。无填充、无边框，纯行内文字色。

## 该做与不该做

### 该做

- 用 `{colors.bg}`（奶油）作通用画布。每处表面都从暖奶油起，绝不纯白。
- 整份文稿用 `{colors.primary}` 钴蓝作唯一强调色：眉题、指标、CTA、图表填充、步骤圆、进度指示。
- 标题（h1、h2、h3）用 `{colors.text}`（`#111111`）近黑配 -0.02em 字距。钴蓝标题禁用，钴蓝只给强调瞬间。
- 每个 h4 眉题用钴蓝 Space Grotesk 字重 600、大写 + 0.08em 字距。眉题是通用分节开场。
- 用 `{components.card-tinted}`（4% 钴蓝填充 + 20% 钴蓝的 1.5px 边 + 14px 半径）作通用内容卡片模式。
- 每个 slide-header 都左边 h4 眉题、右边 `{components.tag-pill}`。这个节奏是系统的结构身份。
- 正文用 Inter 字重 400、13.6-16.8px、`{colors.text-muted}`（`#6b6b6b`）、行高 1.6。柔和灰正文是系统高级感的来源。
- 每个数字标注（指标、统计、条百分比、议程编号）都用 Space Grotesk 字重 600-700 的钴蓝。钴蓝数字强调是系统的数据声部。
- 所有外壳（标签胶囊、CTA、导航按钮）用满 100px border-radius。胶囊形状是系统的外壳签名。
- 方向变化小片（`{components.metric-change-positive}` / `{components.metric-change-negative}`）行内无填充使用，绿正红负，都柔和。

### 不该做

- 不要引入第二强调色。钴蓝是唯一强调色，橙、青、紫或任何新增品牌色都会破掉单一强调纪律。
- 不要把标题设成钴蓝。标题近黑，钴蓝只留给眉题、指标、CTA、图表填充。
- 不要在卡片或内容上用投影。系统除一枚柔和钴蓝 CTA 悬停外零 box-shadow。
- 不要用方角（0px 半径）。系统建立在柔和圆角上，方角会立刻读成另一套美学。
- 不要在卡片上用不透明钴蓝边。边框永远是 20% 钴蓝（`{colors.border}`），全不透明边会破掉安静、抬升的质感。
- 不要替换字体。Space Grotesk + Inter 是固定搭配，换成 Arial、Helvetica、Roboto 或 Open Sans 会压塌排印身份。
- 不要用带框硬边元素塞满画布。系统依赖柔和淡色与温和边框，加重轮廓会显得像另一套系统。
- 不要在内容页省掉 slide-header（h4 眉题 + 标签胶囊）。页眉是编辑节奏。
- 不要把正文设成大写。大写只留给 h4 眉题与高亮块下的 cite 行。
- 不要把方向变化小片用于非方向性强调。绿/红变化小片留给真正的正负比较（例如"+11 pts vs. prior quarter"），不是通用强调色。

## 响应式行为

Blue Professional 设计为 **1920×1080 演示系统**（等效 100vw × 100vh）。排字用 CSS `clamp()`，间距用 `vw / vh / rem`。系统响应式行为极少，为横向演示语境而生。

### 缩放行为
- h1 按视口宽度从 44.8px 缩放到 67.2px。
- h2 从 28.8px 缩放到 41.6px。
- 正文从 13.6px 缩放到 16.8px。
- 指标值从 35.2px 缩放到 48px。
- 卡片内边距（rem 基准）随用户字号设置缩放，默认卡片内部内边距约 24-26px。
- 边框（1px、1.5px、2px）、圆角（10-14px）、胶囊半径（100px）固定不缩放。

### 低视口高度下的组件调整
单独一个 `@media (max-height: 700px)` 块收紧密集页的间距：
- 幻灯片内边距从 3.5vw / 8.5vh 降到 2.5vh / 3vw。
- 议程网格间隙缩小。
- 指标与细节卡片内边距降到 1rem。
- 条项内边距缩小。

这保证系统能塞进较矮的笔记本屏而不破结构布局。

### 放映行为
- 用 `ArrowRight`、`Space` 或 `PageDown` 前进。
- 用 `ArrowLeft` 或 `PageUp` 后退。
- `Home` 跳首页，`End` 跳末页。
- 横向触摸滑动，50px 阈值前进/后退。
- 幻灯片过渡 500ms ease，opacity 淡入 + 40px translateX 滑入/滑出。
- 首页/末页导航按钮禁用（不透明度 0.3）。
- 底边进度条以 400ms ease 动画到当前页百分比。

### 打印行为
系统没有 `@media print` 规则。幻灯片过渡只用于屏幕，打印只能得到激活页。静态导出时，逐页截图能保留所有氛围元素（封面装饰、点、同心圆都是 CSS）。

### 交互状态
- 导航按钮悬停反色（钴蓝填充、奶油图标）。
- 议程项悬停得到微妙的 `{colors.card-bg}` 背景（200ms 过渡）。
- CTA 按钮悬停抬起 -2px，配柔和钴蓝投影（系统唯一阴影）。
- 条填充以 0.8s ease 从 0 动画到数据值，入场时最明显。

## CJK 与国际化内容

用本模板承载中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文搭配，并套用通用 CJK 调整。所有推荐中文字体均通过 CDN 加载，无需安装。

### 推荐中文搭配

| 角色 | 拉丁（默认） | 中文对应 |
|---|---|---|
| h1 / h2 / h3 / h4-eyebrow / 指标数字 / 图表百分比 | Space Grotesk 500–700（负字距，h4 大写） | 思源黑体 Noto Sans SC 700（0 字距、无变换） |
| 正文 / 指标说明 / 列表正文 | Inter 400 | 思源宋体 Noto Serif SC 400 |
| 等宽 / 计数器 / 标签胶囊 / cite | Space Grotesk 500–600（常大写） | 思源黑体 Noto Sans SC 500（无变换） |

### 混排策略

**策略 A**：每个角色一款自带拉丁字形覆盖的 CJK 字族。所有 Space Grotesk 角色（展示、眉题、数字、外壳）用思源黑体 Noto Sans SC，Inter 正文角色用思源宋体 Noto Serif SC。两款字面都自带拉丁字形，与汉字并排也干净。衬线正文搭配强化了本模板所建的咨询级编辑语域：中文的投资人报告与麦肯锡式简报，常把无衬线展示配衬线正文。

### 加载

在模板 `<head>` 中加入：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700&family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- **行高**：在拉丁规格上提高约 15–25%。正文 1.75–1.85（从 1.6 上调），展示 1.2–1.3（从 1.1 上调）。CJK 字形视觉饱满，纵向比拉丁更挤。
- **字距**：每段 CJK 文本设为 0。模板里 h1–h3 的 −0.02em 负字距套在 CJK 上会笔画重叠；h4 眉题的 +0.08em 正字距放在方正字形上显得松垮。
- **文字变换**：不要对中文套 `uppercase`，CJK 没有大小写。h4-eyebrow 与 cite token 在拉丁原版用 `text-transform: uppercase`，CJK 文本要去掉。
- **标点**：用全角中文标点（，。：；！？「」（））。
- **展示标题不加句号**：中文排印惯例，展示级标题末尾不写 。
- **中西文之间加空格（盘古之白）**：每个汉字与相邻的拉丁字符或数字之间插入一个 ASCII 空格。写 `2024 Q3 业绩复盘`，不要写 `2024Q3业绩复盘`。
- **一句一款字体**：思源黑体 / 思源宋体都覆盖 CJK 与拉丁字形，每句交给一款处理。不要让浏览器因 ASCII 字符在句中回退到 Space Grotesk 或 Inter。

### 本系统的美学提示

系统的身份建立在**克制加一项强承诺**上：奶油底、钴蓝强调、柔和淡色卡片、无阴影。这些都不依赖拉丁排印，能干净地迁移到中文。h4-eyebrow 在 CJK 里会丢掉"大写 + 0.08em 字距 + 钴蓝"的性格，因为大写与宽字距都会被去掉。补偿办法是**始终给眉题配上方那条钴蓝强调线组件**：60×4 的钴蓝线承担拉丁里宽字距大写所做的外壳识别工作。眉题的钴蓝颜色与相对柔和灰正文的字重 600 反差要保留。

钴蓝色彩纪律（`#1e2bfa` 作唯一强调，数字与 CTA 上全不透明，边框上 20%，卡片填充上 4%）是系统真正的身份，能整体迁移到 CJK 版本。中文咨询文稿按惯例把数字标注保留为拉丁阿拉伯数字（业绩 $24.3M、同比 +18%），所以钴蓝 Space Grotesk → 思源黑体的替换主要影响标签和标题，不影响最抓眼的数字。数字仍用思源黑体字重 700 渲染。

### 已知 CJK 缺口

- **没有 CDN 中文字面能精确匹配 Space Grotesk 的"可信咨询"语域。** 思源黑体读起来更偏机构、比 Space Grotesk 稍不当代。模板会比拉丁原版略像"官方报告"、略不像"AI 创业公司"。这在中文高管简报语境里通常是优点。
- **h4-eyebrow 信号变弱。** "大写钴蓝 Space Grotesk 600 配 0.08em 字距"的组合是系统最易认的小外壳，到 CJK 会同时丢掉大写与字距信号。推荐在眉题上方或下方补 `{components.accent-line}`；没有它，眉题可能混进正文的字重反差里。
- **正文换成思源宋体会改变语域。** Inter 正文读起来中性现代，思源宋体读起来编辑严肃。系统的"高级咨询"感会略偏向"政策文件"，适合国企或政府受众，对创业路演受众略重。创业语境下把正文换成思源黑体 Noto Sans SC 400 即可。

## 迭代指南

1. 任何新页面都从 `{colors.bg}` 奶油底起。别逐页换背景，恒定的底就是系统的身份。
2. 任何新内容页顶部都带 slide-header：左边 h4 眉题（钴蓝、大写、0.08em），右边标签胶囊。
3. 任何新标题都用 Space Grotesk 字重 600-700、`{colors.text}` 近黑、-0.02em 字距。主瞬间取 h2（28.8-41.6px）。
4. 任何新卡片都用淡色模式：`{colors.card-bg}`（4% 钴蓝）+ 1-1.5px `{colors.border}`（20% 钴蓝）+ 10-14px 半径。绝不用实色填充或不透明边。
5. 任何新数字标注（指标值、统计数字、议程编号、条百分比、步骤圆）都是 Space Grotesk 字重 600-700 的 `{colors.primary}` 钴蓝。数字是强调瞬间。
6. 任何新强调线、分隔线或方向性线都用钴蓝：主线实色，边框用柔和钴蓝（20% 不透明度）。
7. 任何新 CTA 都用 `{components.cta-button}` 模式：实钴蓝胶囊配奶油文字、100px 半径，不存在别的 CTA 形状。
8. 任何新图表条都用 `{components.bar-fill}`（实钴蓝）压在 `{components.bar-track}`（8% 钴蓝）上，6px 半径。
9. 任何新步骤或顺序指示都用 `{components.step-circle}`，未来步骤递减不透明度（1.0 → 0.85 → 0.7 → 0.55）。
10. 表面若显得太稀，加信息（更多统计、更多细节块），别加第二强调色或更重的边框来填。系统填入实质内容时优雅，不靠噪声。

## 已知缺口

- **Space Grotesk 与 Inter 通过 preconnect + `<link>` 从 Google Fonts 加载**。除 `sans-serif` 外没有系统回退，在 Google Fonts 失效的环境里，系统会塌成系统默认字体，失去个性。
- **方向变化色（`{colors.positive}` 与 `{colors.negative}`）仅行内可用**。除这两色行内文字外，没有 token 级的状态填充、成功/错误徽章或告警支持。
- **单一强调色纪律限制了类别色彩编码**。多系列图表只能靠位置或标签区分，系统对"用不同颜色显示 4 个类别系列"没有设计层面的答案。这是刻意的，但限制了图表表达力。
- **议程项悬停态把背景改成 `{colors.card-bg}`**，悬停时交互。静态屏幕共享场景里可能不如预期。
- **条填充入场时从 0 动画到数值**，但只有激活页的条可见。重新进入会重播动画，系统不保留动画状态。
- **进度条在首页读起来像装饰**（10 页文稿里约 10%），要到文稿后段才有信息量。配合页码给出明确位置提示。
- **幻灯片过渡用 translateX（40px 进出）+ opacity 淡入**。超宽屏上 40px 位移几乎看不出，小屏上可能显得突兀。
- **系统加载 Inter 字重 300-600**，实际只用字重 400。更轻或更重的 Inter 字重不属于视觉语汇，加载它们在技术上浪费。
- **指标变化指示用 HTML 实体（`&uarr;`、`&darr;`）**作箭头字形。多数浏览器渲染正常，但系统字体不同可能字形偏小或不一致；改用 SVG 或 Unicode 字符能统一渲染。
- **收尾装饰同心圆按固定 500px / 360px 绝对定位**。视口极小时可能超出边界，极大时可能显得偏小。
- **封面装饰用 clip-path**，支持广泛但并非通用。不支持 clip-path 的浏览器会把面板渲染成整块右列矩形。
