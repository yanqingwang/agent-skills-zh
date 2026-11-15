---
version: alpha
name: Bold Poster
description: "A populist editorial poster system that mashes vintage Italian sports-magazine display lettering with classical serif body and tight monospace metadata. The display face is Shrikhand — a heavy slab/script hybrid with playful italic personality — rendered at poster scale (often 200-320px) and routinely tilted off-axis. Body runs Libre Baskerville for a literary editorial register; Space Grotesk handles tiny uppercase labels and chrome. The palette is uncompromising: white canvas, deep brown-black ink (#1C1410), single saturated tomato red (#D8000F), and a warm off-white (#F5F2EF) for alternating panels. Borders are bold 1.5-3px ink rules; the only shadow is a single stacked offset behind red display text. The aesthetic is loud, confident, and unmistakably print-poster — closer to a 1970s European brand annual report or a wine merchant's catalogue than a contemporary slide deck."

colors:
  bg: "#FFFFFF"
  dark: "#1C1410"
  red: "#D8000F"
  light: "#F5F2EF"

typography:
  hero-title:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(72px, 16vw, 220px)"
    lineHeight: 0.88
    letterSpacing: 1px
    color: "{colors.dark}"
  hero-title-red:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(84px, 18vw, 260px)"
    lineHeight: 0.85
    color: "{colors.red}"
    transform: "rotate(-4deg)"
  hero-title-bottom:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(64px, 14vw, 200px)"
    lineHeight: 0.9
    color: "{colors.dark}"
    transform: "rotate(2deg)"
  close-big:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(80px, 18vw, 260px)"
    lineHeight: 0.88
    color: "{colors.red}"
    transform: "rotate(-5deg)"
  stat-big:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(120px, 26vw, 320px)"
    lineHeight: 0.82
    color: "{colors.red}"
    transform: "rotate(-6deg)"
  red-quote:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(32px, 7vw, 90px)"
    lineHeight: 1.15
    color: "{colors.bg}"
    textShadow: "2px 2px 0 rgba(28,20,16,0.25), 4px 4px 0 rgba(28,20,16,0.2), 6px 6px 0 rgba(28,20,16,0.15)"
  section-header:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(32px, 5vw, 64px)"
    lineHeight: 1
    color: "{colors.dark}"
  section-header-lg:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(36px, 6vw, 72px)"
    lineHeight: 1
    color: "{colors.dark}"
  cell-number-lg:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(28px, 3.5vw, 52px)"
    lineHeight: 1
    color: "{colors.red}"
  cell-number-md:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(28px, 3.5vw, 48px)"
    lineHeight: 1
    color: "{colors.red}"
  card-title:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(22px, 3vw, 36px)"
    lineHeight: 1.1
    color: "{colors.dark}"
  card-title-sm:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(20px, 2.5vw, 32px)"
    lineHeight: 1.1
    color: "{colors.dark}"
  pillar-num:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(36px, 5vw, 64px)"
    lineHeight: 1
    color: "{colors.red}"
  pillar-title:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(18px, 2.2vw, 28px)"
    lineHeight: 1.15
    color: "{colors.dark}"
  stat-item-num:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(28px, 4vw, 56px)"
    lineHeight: 1
    color: "{colors.dark}"
  roadmap-title:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(18px, 2.5vw, 32px)"
    lineHeight: 1.1
  inline-stat:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(18px, 2vw, 28px)"
    lineHeight: 1
    color: "{colors.red}"
  body:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(13px, 1.2vw, 16px)"
    lineHeight: 1.75
    color: "{colors.dark}"
  body-card:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(12px, 1.1vw, 14px)"
    lineHeight: 1.6
    color: "{colors.dark}"
  body-cell:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(11px, 1vw, 13px)"
    lineHeight: 1.55
    color: "{colors.dark}"
  body-small:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(11px, 1vw, 13px)"
    lineHeight: 1.5
    color: "{colors.dark}"
  hero-meta:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(11px, 1vw, 14px)"
    lineHeight: 1.5
    color: "{colors.dark}"
  tag-body:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(13px, 1.2vw, 16px)"
    lineHeight: 1.6
    color: "{colors.dark}"
  red-cite:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(13px, 1.3vw, 16px)"
    lineHeight: 1.5
    color: "{colors.bg}"
  close-sub:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(14px, 1.5vw, 18px)"
    lineHeight: 1.6
    color: "{colors.dark}"
  label:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 10px
    letterSpacing: 2px
    textTransform: uppercase
    color: "{colors.dark}"
  label-red:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 10px
    letterSpacing: 2px
    textTransform: uppercase
    color: "{colors.red}"
  rm-label:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 9px
    letterSpacing: 3px
    textTransform: uppercase
    color: "{colors.red}"
  tag-label:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(10px, 0.9vw, 12px)"
    letterSpacing: 3px
    textTransform: uppercase
    color: "{colors.red}"
  bullet-body:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 400
    fontSize: "clamp(10px, 0.9vw, 12px)"
    lineHeight: 1.45
    color: "{colors.dark}"
  counter:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 11px
    lineHeight: 1
    letterSpacing: 2px
    textTransform: uppercase
    color: "{colors.dark}"
  link:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(10px, 0.9vw, 12px)"
    letterSpacing: 2px
    textTransform: uppercase
    color: "{colors.dark}"
  fc-micro:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 400
    fontSize: 10px
    lineHeight: 1.4
    color: "{colors.dark}"

spacing:
  pad-slide: "48px 56px"
  pad-cell: "22px 20px"
  pad-cell-sm: "20px 24px"
  pad-pillar: "32px 24px"
  pad-card: "24px"
  pad-roadmap: "40px 48px"
  gap-grid-md: "24px 32px"
  gap-grid-roadmap: "28px 36px"
  gap-grid-stats: "48px"
  gap-stat-row: "20px"
  pad-bottom-clearance: "40px"
  max-width-content: 1100px
  max-width-services: 1000px

canvas:
  width: 100vw
  height: 100vh
  background: "{colors.bg}"

components:
  progress-bar:
    position: "fixed, bottom 0 left 0"
    height: 5px
    background: "{colors.red}"
    description: "Persistent thick red progress strip at the bottom of the viewport. Width grows linearly with slide index. The system's most prominent piece of chrome."
  counter:
    position: "fixed, bottom 18px right 24px"
    color: "{colors.dark}"
    opacity: 0.5
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 11px
    letterSpacing: 2px
    description: "Persistent slide counter NN / NN at 50% opacity in Space Grotesk uppercase."
  hint-pill:
    position: "fixed, bottom 18px center"
    background: "{colors.light}"
    padding: "6px 14px"
    borderRadius: 4px
    fontSize: 10px
    opacity: 0
    description: "Bottom-center hint pill that fades to 50% opacity on body hover. Subtle wayfinding only."
  section-bordered-grid:
    border: "3px solid {colors.dark}"
    description: "Heavy 3px ink border enclosing a grid of cells. Each child cell carries a 1.5px ink inner border, producing a hairline-on-heavy double-border tabular grid. Used for financial-figure and summary-highlight grids."
  cell-bordered:
    border: "1.5px solid {colors.dark}"
    padding: "22px 20px"
    description: "Tabular cell with 1.5px ink border. Lives inside a 3px-bordered parent grid; the two border weights touch to produce the system's signature grid-with-double-edge."
  red-leftbar-card:
    borderLeft: "4px solid {colors.red}"
    paddingLeft: 18px
    description: "Service or content card marked by a 4px solid red left rule and 18px left padding. The system's editorial card pattern — no outline, just the red rule signaling the start of a block."
  red-leftbar-card-thin:
    borderLeft: "3px solid {colors.red}"
    paddingLeft: 16px
    description: "Thinner variant of the red-leftbar card used on dark surfaces (roadmap phases). Same pattern, scaled-down rule weight."
  bullet-em-dash:
    glyph: "—"
    color: "{colors.red}"
    fontWeight: 700
    paddingLeft: 14px
    description: "List bullet using a red em-dash (—) glyph in place of a disc. The dash sits at position absolute left and the body text indents to clear it."
  bullet-bullet:
    glyph: "•"
    color: "{colors.red}"
    paddingLeft: 12px
    description: "List bullet using a red round bullet (•) glyph. Same indent pattern as the em-dash variant."
  pillar-panel:
    flex: 1
    padding: "32px 24px"
    borderRight: "3px solid {colors.dark}"
    description: "Vertical column panel inside a multi-pillar layout. Each pillar separated by a 3px ink vertical rule. Alternating panels swap background from {colors.bg} to {colors.light} for striping."
  pillar-bullet-row:
    padding: "5px 0"
    borderBottom: "1px solid rgba(28, 20, 16, 0.08)"
    description: "Bullet row inside a pillar with a hairline-soft bottom border (ink at 8%) separating items. The last item drops the border."
  global-card:
    border: "2px solid {colors.dark}"
    padding: 24px
    description: "Bordered information card with 2px ink outline. Used on the global presence layout. Heavier than the leftbar pattern, more contained."
  stacked-text-shadow:
    textShadow: "2px 2px 0 rgba(28,20,16,0.25), 4px 4px 0 rgba(28,20,16,0.2), 6px 6px 0 rgba(28,20,16,0.15)"
    description: "Three-step decreasing-opacity stacked offset shadow in ink. Applied only to large red display text on red panels. The system's only shadow treatment."
  red-panel:
    background: "{colors.red}"
    color: "{colors.bg}"
    description: "Full-bleed saturated red panel surface. Carries white text with the stacked-text-shadow treatment on display."
  dark-panel:
    background: "{colors.dark}"
    color: "{colors.bg}"
    description: "Full-bleed deep brown-black panel surface. Carries white text and red accents (left bars, mono labels)."
  link-underline:
    color: "{colors.dark}"
    borderBottom: "2px solid {colors.red}"
    paddingBottom: 4px
    description: "Footer link style — Space Grotesk uppercase with a 2px red underline. Hover swaps text color to red."
  hero-title-stack:
    description: "A three-line stacked title where each line is a Shrikhand display element at a slightly different size. Two of the three lines carry rotation transforms (-4deg, +2deg) and one is set in red. The composition is the system's signature opener."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/bold-poster/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Bold Poster 是一套**平民化编辑海报系统**，视觉语汇取自老式意大利体育杂志、中世纪欧洲品牌年报与酒商目录。前提是每一页都该像印出来的：重磅展示字、锁死一种强红色强调、白或米白纸面、墨线打格、装饰压到最低。

字体系统由三款字面严守角色构成。**Shrikhand**（Google Fonts）是展示字面，一款厚重的板衬/手写混合体，字端粗、开口窄，带着鲜明的意大利体育手书气质。以海报尺度（常 100-320px）出现，几乎总带俏皮旋转（-6° 到 +2°），承载每个英雄标题、每个分节标题、每个统计数字、每个卡片标题。**Libre Baskerville**（Google Fonts）是正文字面，一款笔画对比强的古典文学衬线，把系统锚在编辑语域里。以 11-16px、行高 1.5-1.75、深墨色呈现，正是它让系统读起来像印刷而非数字。**Space Grotesk**（Google Fonts）是外壳字面，只用于极小的大写标签（9-12px、2-3px 字距）、卡片内项目正文、页码与页脚链接。Space Grotesk 处理是系统的"元数据"声部。

色彩理念是**不留余地的克制**：白画布、深棕黑墨（`{colors.dark}` — `#1C1410`）、单一饱和番茄红（`{colors.red}` — `#D8000F`），以及供交替面板用的暖米白（`{colors.light}` — `#F5F2EF`）。没有次级品牌色，没有渐变（堆叠文字阴影内部除外），没有淡色，没有语义状态色。每个数字标注、每条激活线、每个 CTA、每个强调瞬间都是红色，而红色只留给这些瞬间（绝不用于正文，绝不作为没有文字压在上头的卡片填充，绝不作为淡色）。

纵深是**结构性的，不是氛围性的**。系统除红面板上红展示文字所用的一枚堆叠文字阴影（2/2、4/4、6/6 三级递减墨色不透明度）外没有投影。其余纵深全来自重磅边框：表格网格 3px 墨轮廓、单元格 1.5-2px 墨边、编辑卡片 4px 红左线、项目之间 1px 细线。双线处理（3px 外 + 1.5px 内）是系统招牌的表格模式，造出定义整套外观的印刷新闻纸质感。

**密度取向：高，平民化且填满。** 这套系统在页面密集时显得权威，稀疏时显得怯。路线图、支柱、财务页常承载 3-6 个带正文段落、项目列表与表格数据的独立单元格，读起来有活力、不拥挤。反过来，英雄、收尾、陈述页刻意降到一两个巨大展示元素配大面积负空间，极低和极高两端都是刻意的。典型内容页承载一个分节标题 + 3-6 个单元格网格，每格装一个红色数字/标题 + 一段 Libre Baskerville 正文 + 3-6 条 Space Grotesk 等项目。典型陈述页承载一个旋转的红色 Shrikhand 元素占掉半张画布，下方一句标语。

**关键特征：**
- 白（`{colors.bg}`）画布与米白（`{colors.light}`）面板交替作条纹，另有深色（`{colors.dark}`）与红色（`{colors.red}`）满出血面板表面供陈述瞬间使用。
- 单色番茄红（`{colors.red}`）作唯一强调，用于每个数字、每条分节线、每个标签、每个左线标记。
- 三字面栈：Shrikhand（展示 + 数字）、Libre Baskerville（正文）、Space Grotesk（等宽标签 + 项目 + 外壳）。
- 展示用 Shrikhand 常被倾斜（-6° 到 +2°），旋转是系统招牌的动态。
- 重磅墨边：表格网格容器 3px、单元格 1.5-2px、编辑左线卡片 4px 红、项目行之间 1px 细线。
- 红展示元素上的堆叠文字阴影（2/2、4/4、6/6 三级递减墨色不透明度），系统唯一阴影。
- 每页底边常驻 5px 厚红色进度条。
- 红色的破折号与圆点字形作列表标记，绝不用默认圆点。
- 英雄构图把三行 Shrikhand 按不同尺寸叠起，至少一行红、至少一行倾斜。
- 页脚链接用 Space Grotesk 大写配 2px 红色下划线。

## 颜色

### 调色板

- **Bg**（`{colors.bg}` — `#FFFFFF`）：纯白画布。多数表面的默认底。读起来是干净的新闻纸。
- **Dark**（`{colors.dark}` — `#1C1410`）：带暖偏的深棕黑，不是纯黑。用于每一行正文、每一条边、每个 Space Grotesk 标签、每段 Libre Baskerville 段落，并作路线图类表面的满出血面板底。这份暖意把它与通用编辑黑区分开。
- **Red**（`{colors.red}` — `#D8000F`）：饱和番茄红。系统唯一强调。用于每个数字（红色 Shrikhand 数字是最常见的元素）、每个分节眉题标签、编辑卡片的每条左线、每个列表项目字形、每条页脚链接下划线、常驻进度条，以及陈述类表面的满出血面板底。绝不作为正文色，绝不作为淡色，绝不作为没有叠加文字的卡片填充。
- **Light**（`{colors.light}` — `#F5F2EF`）：暖米白。用于支柱布局内的交替面板背景（每隔一根支柱换成米白作纵向条纹）以及 hint-pill 外壳的底。比白画布略暖，制造表面区隔而不破坏印刷纸语域。

### 默认值

- **默认表面背景**：`{colors.bg}`（白）。陈述瞬间换成 `{colors.red}`（满出血红面板）。路线图类瞬间换成 `{colors.dark}`。支柱布局内的条纹交替 `{colors.bg}` 与 `{colors.light}`。
- **白表面上的默认标题 / 展示色**：主标题用 `{colors.dark}`，数字与统计类展示元素用 `{colors.red}`。
- **红面板上的默认标题色**：`{colors.bg}`（白）配堆叠文字阴影处理。
- **深面板上的默认标题色**：`{colors.bg}`（白）。数字强调仍是 `{colors.red}`。
- **默认正文文字色**：白/浅表面上 `{colors.dark}`，深/红表面上 `{colors.bg}`（白），三级内容用 0.5-0.8 不透明度。
- **默认眉题 / 标签色**：白表面上 `{colors.red}`（红色 Space Grotesk 大写、2-3px 字距），网格内较小的单元格标签用 `{colors.dark}`。
- **默认左线色**：`{colors.red}`。4px（深表面上 3px）红色左线是编辑卡片签名。
- **单元格与网格的默认边框色**：`{colors.dark}`。没有彩色单元格边框。
- **默认项目字形色**：`{colors.red}`。系统里不存在默认圆点，每个列表都用红色破折号或红色圆点字形。

系统**硬认**四色调色板。不要引入第五色（绿表正向、蓝表信息、黄表高亮）。所有强调靠红，所有正文是浅底深墨，所有反色是红底或深底白字。类别区分靠位置、标签、倾斜，绝不靠颜色。

## 排印

### 字族栈
系统用三款字面，各严绑一个角色。

**Shrikhand**（Google Fonts）是展示兼数字字面。单字重（400）的厚重板状手写体，字形带俏皮斜意、开口窄，读起来既旧世界（明信片手书）又当代（可变字重数字展示）。尺度从 18px（行内统计）到 320px（英雄统计）都用它。始终字重 400（这款字面没有别的字重）。旋转是字面声部的一部分：每页多个 Shrikhand 元素带 -6° 到 +2° 的 transform。

**Libre Baskerville**（Google Fonts，400 / 700 + 斜体）是正文字面。笔画对比强的古典文学衬线，用于每个段落、每个正文单元格、每行元数据、每条引文出处、每个收尾副标题。以 11-16px、行高 1.5-1.75 排，读起来舒服地有编辑感。斜体与粗体字重都加载了，但用得省：斜体用于行内强调，字重 700 极少需要，因为所有重磅展示工作已由 Shrikhand 承担。

**Space Grotesk**（Google Fonts，字重 400-700）是元数据兼外壳字面。以 9-12px 大写、2-3px 字距用于标签、眉题、页码、链接文字、卡片项目正文（不用 Libre Baskerville 时）以及进度外壳。宽字距大写处理是系统的"盖章元数据"声部。

三个角色不重叠：Shrikhand 管每个展示瞬间、每个数字；Libre Baskerville 管每个正文段落、每段编辑文字；Space Grotesk 管每个大写标签、项目、外壳元素。别越界：Shrikhand 排正文会不可读，Libre Baskerville 做标签像书脚注，Space Grotesk 做标题像科技创业公司。

### 排印比例

| Token | 尺寸（clamp / px） | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.stat-big}` | 120–320px clamp | Shrikhand | 400 | 英雄级统计数字（始终旋转 -6°、始终红） |
| `{typography.hero-title-red}` | 84–260px clamp | Shrikhand | 400 | 多行英雄叠排里的红色词（始终旋转 -4°） |
| `{typography.close-big}` | 80–260px clamp | Shrikhand | 400 | 收尾陈述标题（始终旋转 -5°、始终红） |
| `{typography.hero-title}` | 72–220px clamp | Shrikhand | 400 | 英雄叠排顶行（默认不旋转） |
| `{typography.hero-title-bottom}` | 64–200px clamp | Shrikhand | 400 | 英雄叠排底行（始终旋转 +2°） |
| `{typography.section-header-lg}` | 36–72px clamp | Shrikhand | 400 | 财务 / 密集数据页的大分节标题 |
| `{typography.section-header}` | 32–64px clamp | Shrikhand | 400 | 标准分节标题（摘要、服务、全球、收尾） |
| `{typography.pillar-num}` | 36–64px clamp | Shrikhand | 400 | 支柱面板顶部的数字（红） |
| `{typography.cell-number-lg}` / `{typography.cell-number-md}` | 28–52px clamp | Shrikhand | 400 | 表格单元格数字（始终红） |
| `{typography.stat-item-num}` | 28–56px clamp | Shrikhand | 400 | 行内辅助统计数字（深色） |
| `{typography.card-title}` | 22–36px clamp | Shrikhand | 400 | 服务卡片或全球卡片标题 |
| `{typography.card-title-sm}` | 20–32px clamp | Shrikhand | 400 | 更小的卡片标题（全球卡片） |
| `{typography.pillar-title}` | 18–28px clamp | Shrikhand | 400 | 支柱面板标题 |
| `{typography.roadmap-title}` | 18–32px clamp | Shrikhand | 400 | 路线图阶段标题（深表面上白字） |
| `{typography.red-quote}` | 32–90px clamp | Shrikhand | 400 | 红面板上的引文正文（白字 + 堆叠阴影） |
| `{typography.inline-stat}` | 18–28px clamp | Shrikhand | 400 | 正文块里的行内迷你统计数（红） |
| `{typography.body}` | 13–16px clamp | Libre Baskerville | 400 | 标准正文段落 |
| `{typography.body-card}` | 12–14px clamp | Libre Baskerville | 400 | 服务/全球卡片内正文 |
| `{typography.body-cell}` | 11–13px clamp | Libre Baskerville | 400 | 网格内表格单元格正文 |
| `{typography.body-small}` | 11–13px clamp | Libre Baskerville | 400 | 摘要亮点用小正文 |
| `{typography.hero-meta}` | 11–14px clamp | Libre Baskerville | 400 | 标题叠排上方的英雄元信息行 |
| `{typography.red-cite}` | 13–16px clamp | Libre Baskerville | 400 | 红面板引文下的出处（白字） |
| `{typography.close-sub}` | 14–18px clamp | Libre Baskerville | 400 | 收尾标题下的副标题 / 联系方式行 |
| `{typography.label-red}` / `{typography.tag-label}` | 10–12px | Space Grotesk | 600 | 分节标签（大写、2-3px 字距、红） |
| `{typography.label}` | 10px | Space Grotesk | 600 | 网格内单元格标签（大写、2px 字距、深） |
| `{typography.rm-label}` | 9px | Space Grotesk | 600 | 路线图阶段标签（大写、3px 字距、红） |
| `{typography.bullet-body}` | 10–12px clamp | Space Grotesk | 400 | 卡片与支柱内的列表项目正文 |
| `{typography.counter}` | 11px | Space Grotesk | 600 | 常驻页码 |
| `{typography.link}` | 10–12px clamp | Space Grotesk | 600 | 页脚 / 收尾链接文字（大写、2px 字距） |
| `{typography.fc-micro}` | 10px | Space Grotesk | 400 | 表格单元格底部的极小上下文行 |

### 默认值

- **英雄或封面标题默认尺寸**：叠排顶行用 `{typography.hero-title}`（72–220px），第二行配 `{typography.hero-title-red}`（84–260px，红，旋转 -4°），第三行配 `{typography.hero-title-bottom}`（64–200px，旋转 +2°）。三行叠排构图是系统标准英雄模式。
- **分节主标题默认尺寸**：`{typography.section-header}`（32–64px）。始终 Shrikhand。
- **英雄级统计默认尺寸**：`{typography.stat-big}`（120–320px）旋转 -6°、始终红。
- **表格单元格数字默认尺寸**：`{typography.cell-number-md}`（28–52px）红。
- **正文默认尺寸**：`{typography.body}`（13–16px）Libre Baskerville、行高 1.75。
- **卡片正文默认尺寸**：`{typography.body-card}`（12–14px）、行高 1.6。
- **分节眉题标签默认尺寸**：`{typography.tag-label}`（10–12px）Space Grotesk 字重 600、红、大写、2-3px 字距。
- **列表项目正文默认尺寸**：`{typography.bullet-body}`（10–12px）Space Grotesk 字重 400。
- **Shrikhand 默认字重**：400，这款字面没有别的字重。
- **Libre Baskerville 正文默认字重**：400。粗体（700）只用于正文段落内的行内强调。
- **Space Grotesk 标签默认字重**：600。宽字距是系统的标签声部，字重 400 只给项目正文。

拿不准该用哪个展示 token 时，页面分节开场默认取 `{typography.section-header}`（32–64px）。`{typography.stat-big}` 留给英雄统计瞬间，`{typography.hero-title}` 三连留给封面类表面。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每个英雄级 Shrikhand 元素都属于多行叠排构图，至少一行旋转、至少一行红。** 没有旋转或色彩反差的单行 Shrikhand 英雄标题会塌成通用展示瞬间。
- **每个表格数字单元格数字都是 cell-number 尺度（28–52px）的 `{colors.red}` Shrikhand。** 深墨数字单元格会破掉系统层级，红是数据信号。
- **每个分节眉题都是 `{colors.red}` 的 Space Grotesk 字重 600、大写、2-3px 字距。** 没有例外。字距、字重、颜色或大小写任一项不对的眉题，都不是系统的眉题。
- **每个陈述类 Shrikhand 元素（stat-big、close-big）都旋转 -5° 到 -6°、用 `{colors.red}`。** 英雄尺度下不倾斜的红 Shrikhand 像个放错地方的词，倾斜是系统的"动势"信号。
- **每个红面板展示元素都带堆叠文字阴影**（`2px 2px 0 rgba(28,20,16,0.25), 4px 4px 0 rgba(28,20,16,0.2), 6px 6px 0 rgba(28,20,16,0.15)`）。没有阴影，红底白 Shrikhand 读起来在飘；有了阴影，文字才像被压印进面板。
- **每个列表项目都用 `{colors.red}` 破折号（—）或圆点（•）字形**，绝对定位在左，正文留 12-14px padding-left。默认圆点不存在，红标记是系统的列表信号。
- **每段 Libre Baskerville 正文行高 ≥ 1.5（最好 1.6-1.75）。** 行高再紧会压塌编辑语域。
- **Libre Baskerville 段落里的每个 body strong（`<strong>`）都切换字面到 Space Grotesk 字重 600。** 这种行内换字面是系统主要的行内强调机制，衬线 strong 标签达不到同样效果。

### 排印原则

声部对比是**粗壮倾斜的展示 Shrikhand ↔ 文学衬线正文 ↔ 宽字距等宽标签**。斜体罕见（Libre Baskerville 斜体存在，但只用于正文内的行内强调）；下划线只留给红下划线页脚链接处理。Libre Baskerville 正文里的加粗被行内换到 Space Grotesk 字重 600 取代，换字面本身就是强调信号。

数字内容（统计数字、财务数值、百分比标注、迷你统计）始终是红色 Shrikhand。连正文单元格里很小的行内统计也变成红 Shrikhand。把数字当展示，正是这套系统体育杂志语域的来源。

## 布局

### 画布系统
系统以每页 `100vw × 100vh` 为目标。幻灯片绝对定位，以 opacity + translateY（30px）+ scale（0.98 → 1）在 550ms ease 内入场。同一时刻只有一页 `.active`。默认幻灯片内边距 `48px 56px`，主要有几种变化：
- 英雄页：`5vh 7vw` 顶部内边距，对齐移到左上。
- 路线图页：`40px 48px` 以容纳密集双栏网格。
- 支柱页：`0`（支柱列自带内部内边距）。

### 内边距与间隙比例

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-slide}` | 48px 56px | 默认幻灯片内边距 |
| `{spacing.pad-cell}` | 22px 20px | 表格单元格内部内边距（财务网格） |
| `{spacing.pad-cell-sm}` | 20px 24px | 摘要亮点单元格内边距 |
| `{spacing.pad-pillar}` | 32px 24px | 支柱列内边距 |
| `{spacing.pad-card}` | 24px | 全球卡片内边距 |
| `{spacing.pad-roadmap}` | 40px 48px | 路线图表面内边距 |
| `{spacing.gap-grid-md}` | 24px 32px | 标准服务/全球网格间隙（行 × 列） |
| `{spacing.gap-grid-roadmap}` | 28px 36px | 路线图双栏网格间隙 |
| `{spacing.gap-grid-stats}` | 48px | 大统计行间隙 |
| `{spacing.gap-stat-row}` | 20px | 统计项叠排内的纵向间隙 |

### 常驻外壳
每页都出现三个元素：
- **进度条**在底边：5px 厚 `{colors.red}` 条，宽度随页序号增长。最厚、最显眼的外壳，既作进度指示也作底边海报压边。
- **页码**在右下（`bottom: 18px right: 24px`）：Space Grotesk 字重 600 大写 NN / NN、50% 不透明度。
- **提示胶囊**在底部居中：米白胶囊里的 Space Grotesk 大写文字，默认不透明度 0，`body:hover` 淡到 50%。

### 表面变化
文稿轮用五种表面处理：
- **白色内容表面**：默认，多数页面。
- **米白条纹面板**：支柱布局内，交替列取 `{colors.light}` 背景作纵向条纹。
- **满出血红面板**：陈述 / 引文页把画布铺成 `{colors.red}`，配白展示文字与堆叠文字阴影。
- **满出血深面板**：路线图类表面用 `{colors.dark}` 底、白字、红强调。
- **带框表格网格**：财务数字与摘要亮点网格带 3px 墨外框 + 1.5px 墨内单元格边，造出系统招牌的双线表格构图。

### 英雄叠排构图
标准封面/英雄模式是**三行 Shrikhand 叠排**，每行尺寸不同，至少一行旋转、至少一行红。叠排从左上读到右下，最小一行在底，最重的红色旋转在中间。这是系统最鲜明的开场。

## 纵深与层级

### 无卡片，基本无阴影
系统**几乎不用 box-shadow**。卡片不靠阴影浮出表面。纵深来自：
- **重磅边框**（表格网格 3px 外 + 1.5px 内双线；全球卡片 2px 实线边；编辑左线卡片 4px 红左线）。
- **表面反色**（满出血红或深面板切换整片表面）。
- **倾斜展示元素**破开网格对齐。

### 唯一阴影模式（堆叠文字阴影）
整个系统唯一的阴影是**红面板上红展示文字的堆叠文字阴影**：2/2、4/4、6/6 三级，墨色填充不透明度递减（0.25、0.20、0.15）。阴影用 `text-shadow:` 而非 `box-shadow:`。效果是压印感：文字像被略微错版地盖了三次。这个处理只出现在 red-quote 和红面板上某些旋转的 Shrikhand 展示瞬间。

### 边框即纵深（表格网格签名）
财务网格与摘要亮点网格模式用 **3px 实线墨外框**配 **1.5px 实线墨内单元格边**，两种边框粗细在每个单元格交点相接，造出印刷新闻纸质感。这是数据密集表面上系统主要的结构纵深机制。

### 左线
编辑卡片（服务卡片、路线图阶段、全球卡片）以 **4px（深表面上 3px）红实线左边**配 16-18px padding-left 标记。左线发出"这是卡片"的信号而不把它框死，卡片读起来像从红线上悬挑出来。这是系统最常见的卡片模式。

### 倾斜即纵深
旋转的 Shrikhand 展示元素打破水平基线，不用透视就造出维度感。标准旋转是 -6°（stat-big）、-5°（close-big）、-4°（hero-title-red）、+2°（hero-title-bottom）。这些倾斜是系统空间语言的一部分。

## 形状与处理

### 圆角
- **0px**：除 hint-pill（4px）和条轨元素（本模板里没有，若用也该是 0px）外，一律为零。每张卡片、每个单元格、每块面板、每个标注都是严格矩形。
- **4px**：只给 hint-pill，算是对浮动外壳的一点让步。

方角纪律不可少。圆角卡片会立刻把印刷海报感压塌成通用网页美学。

### 边框粗细
- **5px 实线 `{colors.red}`**：只用于常驻进度条。
- **4px 实线 `{colors.red}`**：编辑左线卡片（白表面上的服务卡片）。
- **3px 实线 `{colors.dark}`**：表格网格外框（财务网格、摘要亮点），以及支柱纵向分隔线。
- **3px 实线 `{colors.red}`**：路线图阶段卡片左线（深表面上）。
- **2px 实线 `{colors.red}`**：页脚链接下划线。
- **2px 实线 `{colors.dark}`**：全球卡片轮廓边。
- **1.5px 实线 `{colors.dark}`**：表格网格内单元格边。
- **1px 实线 `rgba(28, 20, 16, 0.08)`**：支柱面板内项目行之间的柔和细线分隔。

边框阶梯（1px 柔线 / 1.5px / 2px / 3px / 4px / 5px）固定。每条边都是实线，虚线与点线不存在。

### 装饰元素类型

**英雄标题叠排**：三行 Shrikhand 构图，尺寸各异，带旋转与色彩反差。系统招牌开场。

**红面板**：满出血 `{colors.red}` 底，配带堆叠文字阴影的白展示文字。用于陈述 / 引文瞬间。

**深面板**：满出血 `{colors.dark}` 底，配白字与红强调。用于路线图类密集数据表面。

**带框表格网格**：3px 墨外框 + 1.5px 墨内单元格边，造出双线表格构图。每格装一个红色 Shrikhand 数字 + Space Grotesk 大写标签 + Libre Baskerville 正文段落 + 底部可选的 Space Grotesk 微型行。

**红左线卡片**：4px 实线红左线配 18px 左内边距，装 Shrikhand 卡片标题 + Libre Baskerville 正文 + Space Grotesk 红项目列表。系统主要的编辑卡片模式。

**支柱面板**：多支柱布局里的一根纵向列，由 3px 墨竖线分隔，白与米白背景交替。每根装一个红色 Shrikhand 数字、Shrikhand 标题、Libre Baskerville 导语，以及由 1px 柔和细线分隔的 Space Grotesk 项目。

**全球卡片**：2px 实线墨边、24px 内边距的卡片，装 Space Grotesk 红标签 + Shrikhand 标题 + Libre Baskerville 正文 + 行内 gc-stats 行。用于全球布局表面。

**破折号项目**：红色破折号字形，绝对定位在左，正文留 14px padding-left。系统主要列表标记。

**圆点项目**：红色圆点字形，绝对定位在左，正文留 12px padding-left。次级列表标记，用于卡片与支柱项目。

**页脚链接**：Space Grotesk 大写文字配 2px 红下划线、4px padding-bottom。悬停把文字色换成红。

**堆叠文字阴影**：三级递减墨色不透明度阴影，用于红面板上的红展示文字。系统唯一的阴影处理。

**倾斜展示**：旋转 -6° 到 +2° 的 Shrikhand 元素。用于 hero-title-red、stat-big、close-big、hero-title-bottom。

## 该做与不该做

### 该做

- 多数表面用 `{colors.bg}`（白）作默认画布。陈述页换 `{colors.red}`，密集数据页换 `{colors.dark}`，纵向支柱条纹交替 `{colors.bg}` / `{colors.light}`。
- 把每个英雄级标题设成多行 Shrikhand 叠排，至少一行旋转、至少一行红。叠排构图是系统开场签名。
- 每个数字标注瞬间（表格单元格、摘要亮点、支柱数字、行内迷你统计）都在 `{colors.red}` 用 Shrikhand。红色 Shrikhand 数字是系统的数据声部。
- 每个分节眉题用 `{colors.red}` 的 Space Grotesk 字重 600 大写、2-3px 字距。宽字距红标签是通用分节开场。
- 给红面板上的红展示文字套堆叠文字阴影。三级递减墨色不透明度阴影是系统唯一阴影，造出压印感。
- 编辑卡片用 4px 红左线模式（`{components.red-leftbar-card}`）。从线上悬挑出的处理是系统主要卡片模式。
- 表格网格用双线处理搭：3px 墨外框 + 1.5px 墨内单元格边在交点相接。
- 每个列表项目都用红色破折号（`{components.bullet-em-dash}`）或红色圆点（`{components.bullet-bullet}`）绝对定位在左渲染。默认圆点禁用。
- 把 Shrikhand 陈述元素倾斜（-5° 到 -6°）造出系统招牌的动势。不倾斜的红色陈述展示读起来像放错位置。
- 每个正文段落用行高 1.5-1.75、`{colors.dark}` 的 Libre Baskerville。文学编辑正文是系统印刷感的来源。

### 不该做

- 不要引入第二强调色。红是唯一强调，绿表正向、蓝表信息、黄表高亮都会破掉单一强调纪律。
- 不要给卡片、面板、单元格、标注加圆角。方角不可商量，唯一例外是 4px 的 hint-pill 外壳。
- 不要加投影或模糊阴影。系统零 box-shadow，唯一阴影是红展示文字上的堆叠文字阴影。
- 不要替换字体。Shrikhand + Libre Baskerville + Space Grotesk 是三件套，换掉 Shrikhand 的任何展示字面都会压塌整个身份。
- 不要用 Shrikhand 排正文，也不要用 Libre Baskerville 做标签。三字面角色纪律不可商量。
- 不要用默认圆点或圆点列表标记。列表始终用绝对定位在左的红色破折号或红色圆点字形。
- 不要省掉英雄级红 Shrikhand 元素上的倾斜。旋转是系统招牌动势，不倾斜的红展示显得平。
- 不要在白表面上把标题渲染成红（stat-big、close-big、hero-title-red 这些旋转陈述元素除外）。多数分节标题是 `{colors.dark}` 的 Shrikhand，不是红。
- 不要把 Libre Baskerville 正文行高收到 1.5 以下。正文行高过紧会把文学语域压成局促。
- 不要用卡片或结构内容塞满陈述页。陈述表面（红面板、统计页、收尾页）刻意在单个旋转红展示元素周围留出大面积负空间。

## 响应式行为

Bold Poster 设计为 **1920×1080 演示系统**。展示字用带 `vw` 中值的 CSS `clamp()`，边框与外壳用固定 `px`，单元格内边距用接近 rem 的固定值。系统为窄视口设了一个 768px 响应式断点。

### 缩放行为
- 英雄统计按视口宽度从 120px 缩放到 320px。
- 英雄标题从 64px 缩放到 260px。
- 分节标题从 32px 缩放到 72px。
- 正文从 11px 缩放到 16px。
- 边框（1px 柔线 / 1.5px / 2px / 3px / 4px / 5px）与旋转 transform 固定不缩放。

### 移动端断点（max-width: 768px）
单独一个 `@media (max-width: 768px)` 块为窄视口重构密集布局：
- 幻灯片内边距从 48px × 56px 收到 32px × 24px。
- 摘要列由 2 收到 1。
- 摘要亮点网格由 3 收到 1。
- 财务网格由 3 收到 2。
- 服务网格由 2 收到 1。
- 路线图网格由 2 收到 1。
- 支柱从横向 flex-row 换成纵向 flex-column，竖分隔线变成横向底边。
- 全球网格由 2 收到 1。
- 统计行纵向堆叠。
- 英雄标语从绝对定位的右下移到英雄标题叠排下方的相对定位。

系统在 768px 以下纵向用法里能用，但没做优化，它为横向演示语境而生。

### 放映行为
- 用 `ArrowRight`、`ArrowDown`、`Space`、`Enter` 或 `PageDown` 前进。
- 用 `ArrowLeft`、`ArrowUp` 或 `PageUp` 后退。
- 点击视口右半前进，点击左半后退。
- 横向触摸滑动，50px 阈值前进/后退。
- 幻灯片过渡 550ms cubic-bezier `(0.22, 1, 0.36, 1)`，组合 opacity、translateY（30px）与 scale（0.98 → 1）。
- 底边进度条以 500ms cubic-bezier ease 动画到当前页百分比。

### 打印行为
系统没有 `@media print` 规则。过渡只用于屏幕。静态导出时，逐页截图能保留所有旋转 transform 与堆叠文字阴影（两者都是纯 CSS）。

### 交互状态
- 页脚链接悬停把文字色从 `{colors.dark}` 换成 `{colors.red}`。
- hint-pill 在 `body:hover` 时经 400ms ease 从不透明度 0 淡到 0.5。

## CJK 与国际化内容

用本模板承载中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文搭配，并套用通用 CJK 调整。所有推荐中文字体均通过 CDN 加载，无需安装。

### 推荐中文搭配

| 角色 | 拉丁（默认） | 中文对应 |
|---|---|---|
| 展示 / 英雄 / 统计 / 分节标题 / 数字 / 卡片标题 | Shrikhand 400（厚重板状手写、旋转） | 思源宋体 Noto Serif SC 900 |
| 正文 / 卡片正文 / 单元格正文 / 英雄元信息 / 出处 / 收尾副标题 | Libre Baskerville 400（文学衬线） | 思源宋体 Noto Serif SC 400 |
| 标签 / 项目正文 / 计数器 / 链接 / 微型外壳 | Space Grotesk 400–600（大写、2–3px 字距） | 思源黑体 Noto Sans SC 500（无变换、无字距） |

### 混排策略

**策略 A**：每个角色一款自带拉丁字形覆盖的 CJK 字族。展示与正文都用**思源宋体 Noto Serif SC**（展示字重 900、正文字重 400，视觉层级靠字重、尺寸、颜色、旋转，不靠字面对比）。小型大写外壳（标签、项目正文、计数器、链接）用**思源黑体 Noto Sans SC** 字重 500。思源宋体自带拉丁字形，与汉字并排也干净；混排展示瞬间里，思源宋体字重 900 会把中文和拉丁都渲染成同一种厚衬线声部。

### 加载

在模板 `<head>` 中加入：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700;900&family=Noto+Sans+SC:wght@400;500;600&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- **行高**：在拉丁规格上提高约 15–25%。正文 1.75–1.85（已接近 Libre Baskerville 的 1.75，CJK 保持 1.8），展示 1.1–1.25（从 Shrikhand 极紧的 0.82–0.9 上调）。展示在 0.82 会在 CJK 里纵向相撞，至少放到 1.0。
- **字距**：每段 CJK 文本设为 0。模板里 hero-title 的 1px 正字距与 Space Grotesk 标签的 2–3px 字距，放到方正 CJK 字形上都显得松垮。
- **文字变换**：不要对中文套 `uppercase`，CJK 没有大小写。拉丁原版里每个 Space Grotesk 标签、tag-label、rm-label、计数器、链接都用 `text-transform: uppercase`，CJK 文本要去掉。
- **标点**：用全角中文标点（，。：；！？「」（））。
- **展示标题不加句号**：中文排印惯例，展示级标题末尾不写 。
- **中西文之间加空格（盘古之白）**：每个汉字与相邻的拉丁字符或数字之间插入一个 ASCII 空格。写 `1970 米兰式海报`，不要写 `1970米兰式海报`。
- **一句一款字体**：思源宋体以统一衬线风格覆盖 CJK 与拉丁字形，展示与正文的混排句子交给它处理。不要让浏览器因 ASCII 字符在词中回退到 Shrikhand 或 Libre Baskerville。

### 本系统的美学提示

系统的身份建立在 **Shrikhand 粗壮板状手写性格 + 旋转 + 饱和红**上。Shrikhand 是本模板最鲜明的单项决策，却没有中文对应。思源宋体字重 900 有分量、有编辑语域，却把俏皮斜意的板状性格完全丢掉。补偿办法是更倚重**非排印签名**：保留所有旋转（stat-big -6°、close-big -5°、hero-title-red -4°、hero-title-bottom +2°）、保留红面板展示上的堆叠文字阴影、保留饱和番茄红作唯一强调、保留 3px + 1.5px 双线表格网格、保留红左线卡片、保留红色破折号项目标记。旋转、红色与印刷新闻纸的结构语言能在换字面后存活。

系统的三字面角色纪律（Shrikhand 展示 / Libre Baskerville 正文 / Space Grotesk 外壳）到了 CJK 收成两字面系统：一切拉丁衬线归思源宋体，一切拉丁等宽归思源黑体。正文与展示的反差变成纯字重（400 对 900）加颜色（深对红）。正文内的行内 `<strong>` 强调，从思源宋体 400 切到思源黑体 600：拉丁原版靠换字面提示强调，CJK 里衬线转无衬线保留了同样的逻辑。

### 已知 CJK 缺口

- **Shrikhand 的板状手写性格没有精确的在线 CJK 对应。** 这款字面是意大利体育杂志展示手书，字端粗、字形带俏皮斜意，Google Fonts、Adobe Fonts、cn-fontsource 上都没有中文对应。思源宋体字重 900 有分量、有编辑语域，但读起来严肃而非俏皮。旋转 transform 与饱和红独自扛起俏皮体育杂志声部，汉化到 CJK 时别丢倾斜。
- **没有可 CDN 加载的中文等宽字面给外壳声部。** Space Grotesk 的角色（大写宽字距标签、页码、带红下划线的页脚链接）依赖大写 + 2–3px 字距处理。思源黑体字重 500–600、0 字距是最接近的匹配，却丢掉"盖章元数据"信号。CJK 版本里，红色与标签/链接上的 1–2px 边框处理承担了大部分外壳识别工作。
- **Libre Baskerville 的古典文学语域没有精确的中文对应。** 思源宋体读起来偏机构现代，而非 19 世纪文学。若项目特别需要文学季刊声部（随笔或宣言里的长正文段落），可考虑用霞鹜文楷 LXGW WenKai 代替思源宋体，它带手写/书法暖意，更接近 Baskerville 的编辑性格。

## 迭代指南

1. 任何新内容页都以 `{colors.dark}` 的 `{typography.section-header}`（32–64px）Shrikhand 分节标题开头，前面可选配 Space Grotesk 红眉题标签。
2. 任何新数字标注（单元格数字、支柱数字、行内统计、摘要亮点）都是相应 cell-number 尺度的 `{colors.red}` Shrikhand。
3. 任何新正文段落都是 `{colors.dark}` 的 Libre Baskerville 字重 400、行高 1.5-1.75。
4. 任何新编辑卡片都用 `{components.red-leftbar-card}` 模式（4px 红左线 + 18px padding-left），装 Shrikhand 标题 + Libre Baskerville 正文 + Space Grotesk 红项目列表。
5. 任何新数据网格都包在 3px 墨外框配 1.5px 墨内单元格边里。每格装：红色 Shrikhand 数字 + Space Grotesk 大写标签 + Libre Baskerville 正文 + 底部可选的 Space Grotesk 微型上下文行。
6. 任何新陈述页都用满出血 `{colors.red}` 面板，白带堆叠文字阴影的 Shrikhand 展示文字，下方白色 Libre Baskerville 出处。
7. 任何新密集数据页都用满出血 `{colors.dark}` 面板，白字、红色 Space Grotesk 标签、阶段卡片上红色 3px 左线、列表上红色圆点字形。
8. 任何新列表都用绝对定位在左的红色破折号或红色圆点字形，绝不用默认圆点。
9. 任何新英雄构图都是多行 Shrikhand 叠排：至少三行、至少一行旋转、至少一行红。别塌成单行横标题。
10. 表面若显得太单一，换表面底（白 → 红 / 深 / 米白面板），别加第二强调色或第三款字体。

## 已知缺口

- **Shrikhand 是单字重（400）展示字面**，没有更粗或更细的字重可用。每个 Shrikhand 元素字重相同，视觉层级只靠尺寸、颜色、旋转。
- **Shrikhand、Libre Baskerville、Space Grotesk 通过单个 `<link>` 请求从 Google Fonts 加载**。除 `cursive` / `serif` / `sans-serif` 外没有系统回退；在 Google Fonts 失效的环境里，系统会塌成通用系统字体，身份尽失。
- **堆叠文字阴影为墨压红语境硬编码**。套到别的颜色组合（例如浅底红字）达不到同样效果，三级阴影是专为红面板表面调的。
- **旋转 transform 按元素类型固定**（stat-big -6°、close-big -5°、hero-title-red -4°、hero-title-bottom +2°）。调整单个旋转要逐实例覆盖样式。
- **财务网格与摘要亮点网格用重叠边框**（3px 外 + 1.5px 内，因 box-sizing 在物理上有半像素重叠）。浏览器渲染这个重叠通常干净，但某些缩放级别下可能产生细微的 1 像素瑕疵。
- **支柱布局每列用 `overflow-y: auto`**。内容长的表面在某些操作系统上会出现可见滚动条，系统为内容塞得进视口而设计。
- **slide-hero 上的英雄标语绝对定位在 `bottom: 8vh; right: 7vw`**，max-width 300px。宽高比极宽或极窄时可能与英雄标题叠排错位。
- **进度条是 5px 高**，在底边有文字的页面上可能视觉压住内容，收尾页尤其把 close-links 放在 `bottom: 5vh`，刚好让开进度条但余量很小。
- **点击前进交互按 50% 宽度把视口分成下一页/上一页**。这可能与页内链接的点击交互冲突（收尾页页脚链接）。系统依赖链接点击事件 stopPropagation，而默认并没有这么做。
- **项目列表类全局定义了破折号字形**，但演示模板里没用：支柱项目、服务项目、路线图项目都在行内重定义了自己的项目样式。定义的工具类与实际用法模式之间有些不一致。
