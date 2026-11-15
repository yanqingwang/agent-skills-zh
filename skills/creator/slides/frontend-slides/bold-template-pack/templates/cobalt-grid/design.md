---
version: alpha
name: Cobalt Grid
description: "A Japanese-magazine trend-report system built on warm cream paper, electric cobalt ink, and a graph-paper grid that lives permanently behind every slide. Newsreader serif headlines tower at 18vh while DM Mono carries chrome and ticker text. The signature decoration is a pixel-glitch column — vertical scanlines stair-stepped down the right edge of declarative slides — paired with QR-style 8×8 grid patches. The cultural reference is WIRED Japan, Shift magazine, and architectural trend reports printed in two-color risograph: cream + one cobalt."

colors:
  paper: "#F0EBDE"
  paper-2: "#E6E0CE"
  ink: "#1F2BE0"
  ink-soft: "#5560E5"
  grid: "rgba(31, 43, 224, 0.10)"
  ink-faint: "rgba(31, 43, 224, 0.18)"

color-aliases:
  rule: ink
  bg: paper

typography:
  display-hero:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(100px, min(11vw, 18vh), 200px)"
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.008em
  display-closing:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(72px, min(8.4vw, 14vh), 180px)"
    fontWeight: 400
    lineHeight: 0.96
    letterSpacing: -0.005em
  display-chapter:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(56px, min(6vw, 10vh), 130px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -0.005em
  display-quote:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(50px, min(5.6vw, 9vh), 110px)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.005em
  display-manifesto:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(56px, min(6.4vw, 11vh), 120px)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.005em
  headline:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(46px, min(4.8vw, 8.2vh), 92px)"
    fontWeight: 400
    lineHeight: 0.95
  headline-index:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(48px, min(5vw, 8.5vh), 100px)"
    fontWeight: 400
    lineHeight: 0.95
  vbig-numeral:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(110px, min(11vw, 18vh), 240px)"
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.015em
  ed-callout:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(28px, min(2.8vw, 4.6vh), 50px)"
    fontWeight: 400
    lineHeight: 1.1
  row-headline:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(26px, 2vw, 40px)"
    fontWeight: 400
    lineHeight: 1.05
  table-name:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(20px, 1.6vw, 28px)"
    fontWeight: 400
    lineHeight: 1.15
  micro:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(12px, 0.9vw, 14px)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.16em
    textTransform: uppercase
  micro-strong:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(13px, 1vw, 16px)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.18em
    textTransform: uppercase
  micro-sm:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(11px, 0.75vw, 12px)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.18em
    textTransform: uppercase
  body:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(14px, 0.95vw, 15px)"
    fontWeight: 400
    lineHeight: 1.5
  body-lede:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(15px, 1vw, 18px)"
    fontWeight: 400
    lineHeight: 1.5
  body-stat:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(15px, 1vw, 17px)"
    fontWeight: 400
    lineHeight: 1.5
  mono-tag:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: "clamp(13px, 0.9vw, 15px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em
  mono-chrome:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: "clamp(11px, 0.82vw, 13px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.06em
  mono-tick:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: "clamp(12px, 0.85vw, 14px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em

spacing:
  edge: "clamp(36px, 3.6vw, 80px)"
  edge-inner: "clamp(60px, 8vw, 160px)"
  pad-top: "clamp(76px, 8vh, 130px)"
  pad-bottom: "clamp(100px, 10vh, 150px)"
  gap-lg: "clamp(28px, 3vw, 56px)"
  gap-md: "clamp(20px, 2.2vh, 36px)"
  gap-sm: "clamp(14px, 1.6vh, 24px)"
  gap-xs: "clamp(10px, 1.2vh, 18px)"

canvas:
  width: 100vw
  height: 100vh

components:
  graph-paper-grid:
    backgroundImage: "linear-gradient(to right, {colors.grid} 1px, transparent 1px), linear-gradient(to bottom, {colors.grid} 1px, transparent 1px)"
    backgroundSize: "clamp(28px, 2.2vw, 44px) clamp(28px, 2.2vw, 44px)"
    description: "Permanent ::before pseudo on every stage. 28–44px squared graph paper grid in 10%-opacity cobalt that sits behind every slide at z-index 1. Cannot be turned off — it is the canvas tone."
  hairlines:
    height: "1.5px"
    background: "{colors.ink}"
    description: "Two persistent slim cobalt rules — one at the top of every slide (≈2.6vh from top) and one near the bottom (≈2vh from bottom) — both inset from edges by {spacing.edge}. They frame the slide composition."
  pagenum:
    position: absolute
    right: "{spacing.edge}"
    bottom: "clamp(48px, 4.8vh, 76px)"
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: "clamp(11px, 0.82vw, 13px)"
    color: "{colors.ink}"
    letterSpacing: 0.06em
    description: "Mono cobalt page number anchored bottom-right above the bottom hairline. One per slide."
  nav-hint:
    position: fixed
    left: "{spacing.edge}"
    bottom: "clamp(48px, 4.8vh, 76px)"
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: "clamp(10px, 0.75vw, 12px)"
    color: "{colors.ink}"
    letterSpacing: 0.08em
    opacity: 0.4
    description: "Mono cobalt navigation hint anchored bottom-left, mirrors pagenum."
  pixel-glitch:
    description: "Stair-stepped column of vertical scanlines, rendered as inline SVG. Each stepped rectangle contains evenly-spaced cobalt vertical lines on cream. Sits absolutely positioned (typically right edge) at z-index 3, decorative only. Size ranges from 16vw × full-height (compact decoration) to 32vw × full-height (signature cover decoration)."
  qr-block:
    display: grid
    gridTemplateColumns: "repeat(8, 1fr)"
    gridTemplateRows: "repeat(8, 1fr)"
    gap: 1.5px
    background: "{colors.paper}"
    padding: 4px
    boxShadow: "0 0 0 1.5px {colors.paper}"
    description: "8×8 QR-style mosaic of cobalt cells on cream background. Paper-fill ensures it reads as a discrete patch when overlapping the pixel-glitch column. Typical size 58–100px square."
  topbar-rule:
    borderBottom: "1.5px solid {colors.ink}"
    paddingBottom: "clamp(12px, 1.4vh, 22px)"
    description: "1.5px cobalt rule under the topbar of an index, data, or table layout. Below the rule sits a Newsreader headline (left) and a mono lab-tag (right)."
  row-divider:
    borderBottom: "1px solid {colors.ink-faint}"
    description: "Faint 18%-opacity cobalt rule between rows of an index list, table, or ledger."
  attribution-rule:
    borderTop: "1px solid {colors.ink}"
    paddingTop: "clamp(10px, 1.2vh, 18px)"
    description: "Solid cobalt rule above a quote attribution or manifesto byline."
  pixel-stack-bars:
    description: "Vertical bar chart rendered as a column of stacked 'cells' — flex column-reverse with 3px gaps, each cell a small horizontal block. Cells default to 10%-opacity cobalt (the grid color); .on cells fill solid cobalt to represent the value. Reads as a pixelated bar made of grid units."
  ledger-row:
    display: grid
    gridTemplateColumns: "76px 0.6fr 1.4fr 0.7fr 0.5fr"
    gap: "clamp(14px, 1.4vw, 28px)"
    borderBottom: "1px solid {colors.ink-faint}"
    description: "Dense table row carrying a num-tag, name (Newsreader), description (Hanken Grotesk), mood-tag, and delta-tag (mono with up/down arrow prefix). Header row uses 1.5px solid cobalt bottom border."
  vstack-label:
    fontFamily: "DM Mono, ui-monospace, monospace"
    writingMode: "vertical-rl"
    textOrientation: "mixed"
    letterSpacing: 0.04em
    description: "Vertical-orientation mono label column anchored to the right edge of a slide. Replaces the Korean vertical column of the reference with mono catalogue text rotated 90°."
  delta-up:
    content: "↑ "
    description: "Up arrow prefix via ::before on a mono delta tag in the ledger table."
  delta-down:
    content: "↓ "
    opacity: 0.6
    description: "Down arrow prefix via ::before, dimmed 40% to read as decline."
  delta-flat:
    content: "— "
    opacity: 0.6
    description: "Em-dash prefix via ::before, dimmed 40% to read as neutral."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/cobalt-grid/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Cobalt Grid 是一套**双色趋势报告编辑系统**，建立在三块不可动摇的地基上：暖奶油纸画布（`{colors.paper}`）、电光钴蓝墨（`{colors.ink}`），以及**常驻每页背后的方格纸网格**。网格不是可选装饰，它经每个 `.stage` 上的 `::before` 伪元素渲染，无法关闭。美学是"双色 risograph 专著"：只有奶油 + 钴蓝，网格给整份文稿带来建筑描图纸或日本趋势报告的感觉。

字面栈是刻意的三字面对话。**Newsreader**，当代文学衬线、正体字形调制低，承载每个展示瞬间、每个分节标题、每个统计数字。Newsreader 只用字重 400，靠尺寸而非字重主张层级。**Hanken Grotesk**，人文无衬线，承载每个正文段落、每个大写标签、每个微型文字。Hanken 正文用 400、标签用 600。**DM Mono**，等宽体，承载每个外壳元素：页码、等宽小片、轴刻度、竖排标签、表格里的增减箭头。三字面系统造出系统身份：衬线陈述 + 无衬线正文 + 等宽外壳。

配色**严格双色**：奶油与钴蓝，另有柔和钴蓝 `{colors.ink-soft}` 与两档不透明度色调（`{colors.grid}` 10%、`{colors.ink-faint}` 18%）作氛围与结构用途。没有强调色。钴蓝是**唯一**的墨色，用于标题、正文、边框、页码、方格纸、像素故障装饰、QR 拼块。奶油纸是**唯一**的表面。连像素堆叠条形图都用两档不透明度的钴蓝（10% 灭、100% 亮）来渲染数据。

纵深是**平中带结构线**。没有投影、没有抬升卡片、没有圆角表面。层级来自：
- 1.5px 钴蓝**细线画框**（每页顶部与底部）。
- 分节页眉下的 1.5px 钴蓝**顶栏线**。
- 表格或索引条目之间 1px 淡钴蓝**行分隔线**。
- 背后 10% 不透明度的**方格纸网格**。
- 像素故障与 QR 拼块**装饰 SVG 补丁**作构图点缀。

**密度取向：中到密，由网格组织。** Cobalt Grid 为编辑密度而生：杂志跨页、趋势索引、数据账目。构图正确的一页，配一个大 Newsreader 标题加多条结构化信息行（六条趋势的索引、八条条目的账目、带八根像素堆叠条的图表）。底下的方格纸主动想被填满，稀疏的页露出太多网格，读起来像线框图。例外是宣言、引文、版权页布局，它们刻意留白，让方格纸呼吸。按页型选密度：章节 / 宣言 / 引文 / 版权页稀疏，索引 / 数据 / 表格页密集。

**关键特征：**
- 奶油纸画布 `{colors.paper}` 配电光钴蓝 `{colors.ink}` 作唯一墨色，严格双色。
- 常驻的 28–44px 方格纸网格，10% 不透明度钴蓝，在每页背后。
- 顶部与底部 1.5px 钴蓝细线以 `{spacing.edge}` 内缩框住每页。
- Newsreader 衬线字重 400 用于每个展示/标题，Hanken Grotesk 无衬线用于正文/标签，DM Mono 用于所有外壳。
- 像素故障竖向扫描线列与 QR 式 8×8 拼块，作系统招牌装饰补丁。
- 展示字可以极大，`{typography.display-hero}` 到 18vh（1080 高屏上约 194px），`{typography.vbig-numeral}` 到 240px。
- Hanken 标签大写、0.16–0.18em 字距，等宽小片带 0.04–0.06em 字距。
- 像素堆叠条形图把数据渲染成网格单元格的堆叠（钴蓝亮 / 10% 钴蓝灭）。
- 页码在右下，等宽导航提示在左下，都锚在底部细线上方。

## 颜色

### 双色系统
- **Paper**（`{colors.paper}` — #F0EBDE）：画布。暖奶油米白，明显偏黄暖，更像"新闻纸"而非"空白白"。用作通用幻灯片背景，也作 QR 拼块背后的填充，让它们相对像素故障列读作一块块独立补丁。
- **Paper-2**（`{colors.paper-2}` — #E6E0CE）：略深的奶油。调色板里定义了但用得省，需要微妙区域区隔时可用。
- **Ink**（`{colors.ink}` — #1F2BE0）：电光钴蓝 / 品蓝。系统**唯一**的墨色。用于所有标题、所有正文、所有边框、所有外壳、方格纸网格、像素故障装饰、QR 拼块。高饱和是刻意的，全强度下读起来是 risograph 印出的钴蓝，不是海军蓝。
- **Ink Soft**（`{colors.ink-soft}` — #5560E5）：较浅的钴蓝，用于次级标记。调色板里定义了但用得省，系统里大部分柔化钴蓝来自对 ink 调不透明度，而非这个专用色。
- **Grid**（`{colors.grid}` — rgba(31, 43, 224, 0.10)）：10% 不透明度钴蓝。只用于每页背后常驻的方格纸网格，以及像素堆叠条形图里"灭"的单元格。
- **Ink Faint**（`{colors.ink-faint}` — rgba(31, 43, 224, 0.18)）：18% 不透明度钴蓝。只用于索引列表、表格、账目里淡行分隔线，隔开的那些行属于同一密集信息层。

### 默认值
- **默认幻灯片表面**：`{colors.paper}`。
- **默认标题色**：`{colors.ink}`，每个 Newsreader 衬线标题都是钴蓝。没有别的标题色。
- **默认正文文字色**：`{colors.ink}`，正文也是钴蓝，只是更小。钴蓝压奶油是系统唯一的文字关系。
- **默认标签 / 等宽 / 微型色**：`{colors.ink}`。
- **默认边框色（结构线）**：`{colors.ink}` 1.5px 实线。
- **默认边框色（密集列表内行分隔）**：`{colors.ink-faint}` 1px 实线。
- **默认网格色**：`{colors.grid}`，绝不以全强度显形，绝不禁用。
- **默认图表数据色（亮）**：`{colors.ink}`。
- **默认图表数据色（灭）**：`{colors.grid}`。

系统**没有平民化意义上的强调色**。第二色不存在，加一个红色标注、绿色统计、黄色高亮都会破掉 risograph 双色身份。需要强调时，放大字号、从 Hanken 切到 Newsreader、加一个等宽增减箭头，或用不透明度压暗，而不是靠上色提亮。

## 排印

### 字族
系统跑在**三字面对话**上：`Newsreader`（衬线，字重 400 / 500 斜体）承载每个展示与标题；`Hanken Grotesk`（无衬线，字重 400–700）承载每个正文、标签、微型文字；`DM Mono`（等宽，400–500）承载每个外壳元素。没有第四字面。

Newsreader 的正体字形几乎只跑字重 400，靠尺寸而非字重主张层级。斜体 Newsreader 已加载（300/400/500 斜体轴），用在宣言的 `.roman` 修饰里（这个修饰符其实**非斜**，它把斜体正文翻回正体作行内拉页瞬间），也可用于行内 `<em>` 强调。Hanken Grotesk 正文用 400、标签用 600。DM Mono 外壳用 400。

衬线/怪诞/等宽的三方搭配是系统主要的排印节奏。每款字面角色严格：衬线 = 陈述，怪诞 = 辅助文案，等宽 = 目录外壳。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.vbig-numeral}` | clamp(110px, min(11vw, 18vh), 240px) | Newsreader | 400 | 最大数字展示，英雄统计数字 |
| `{typography.display-hero}` | clamp(100px, min(11vw, 18vh), 200px) | Newsreader | 400 | 最大标题，封面或英雄展示 |
| `{typography.display-closing}` | clamp(72px, min(8.4vw, 14vh), 180px) | Newsreader | 400 | 版权页/收尾布局上的收束标题 |
| `{typography.display-chapter}` | clamp(56px, min(6vw, 10vh), 130px) | Newsreader | 400 | 分节开场或章节标题 |
| `{typography.display-manifesto}` | clamp(56px, min(6.4vw, 11vh), 120px) | Newsreader | 400 | 宣言陈述展示 |
| `{typography.display-quote}` | clamp(50px, min(5.6vw, 9vh), 110px) | Newsreader | 400 | 拉页引文正文 |
| `{typography.headline-index}` | clamp(48px, min(5vw, 8.5vh), 100px) | Newsreader | 400 | 索引或趋势列表分节页眉 |
| `{typography.headline}` | clamp(46px, min(4.8vw, 8.2vh), 92px) | Newsreader | 400 | 数据、表格或图表分节页眉 |
| `{typography.ed-callout}` | clamp(28px, min(2.8vw, 4.6vh), 50px) | Newsreader | 400 | 英雄标题下的编辑副标题 |
| `{typography.row-headline}` | clamp(26px, 2vw, 40px) | Newsreader | 400 | 索引列表里逐行标题 |
| `{typography.table-name}` | clamp(20px, 1.6vw, 28px) | Newsreader | 400 | 账目表格里逐行名称单元格 |
| `{typography.body-lede}` | clamp(15px, 1vw, 18px) | Hanken Grotesk | 400 | 章节标题下的导语段 |
| `{typography.body-stat}` | clamp(15px, 1vw, 17px) | Hanken Grotesk | 400 | 统计数字旁的说明段落 |
| `{typography.body}` | clamp(14px, 0.95vw, 15px) | Hanken Grotesk | 400 | 标准段落正文 |
| `{typography.micro-strong}` | clamp(13px, 1vw, 16px) | Hanken Grotesk | 600 | 最大大写标签 / 眉题 |
| `{typography.micro}` | clamp(12px, 0.9vw, 14px) | Hanken Grotesk | 600 | 标准大写标签 / lab-tag |
| `{typography.micro-sm}` | clamp(11px, 0.75vw, 12px) | Hanken Grotesk | 600 | 最小大写标签 / 表头 |
| `{typography.mono-tag}` | clamp(13px, 0.9vw, 15px) | DM Mono | 400 | 等宽目录小片、索引行里的 num-tag |
| `{typography.mono-tick}` | clamp(12px, 0.85vw, 14px) | DM Mono | 400 | 等宽图表刻度标签、竖排标签条目 |
| `{typography.mono-chrome}` | clamp(11px, 0.82vw, 13px) | DM Mono | 400 | 等宽页码、导航提示、次级元信息 |

### 默认值
- **分节主标题（索引、数据、表格）默认尺寸**：`{typography.headline}`（clamp 46–92px），索引布局用 `{typography.headline-index}`。
- **封面或英雄展示默认尺寸**：`{typography.display-hero}`（clamp 100–200px）。
- **章节或分节开场标题默认尺寸**：`{typography.display-chapter}`（clamp 56–130px）。
- **段落正文默认尺寸**：`{typography.body}`（clamp 14–15px）。
- **任何行内大写标签默认尺寸**：`{typography.micro}`（clamp 12–14px），字重 600、0.16em 字距。
- **任何等宽外壳（页码、小片、刻度）默认尺寸**：`{typography.mono-tag}`（clamp 13–15px）。
- **Newsreader 默认字重**：400。不用 Newsreader 粗体。
- **Hanken 正文默认字重**：400。
- **Hanken 标签默认字重**：600。

拿不准时，页面分节主标题取 `{typography.headline}`（clamp 46–92px），不要用 `{typography.display-chapter}`（后者只给章节开场瞬间）。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个 Newsreader 元素都设字重 400。** 系统里不用 600/700 的 Newsreader，文学衬线美学靠适中字重下开放的正体字形。
- **每个 Newsreader 元素都以 `{colors.ink}`（钴蓝）渲染。** 奶油色衬线标题不存在。
- **每个 Hanken 标签、眉题、lab-tag、微型文字都大写、字重 600、至少 0.16em 字距。** 没有字距的 Hanken capitals 读起来像没处理过。
- **每个 DM Mono 元素都以 `{colors.ink}` 渲染、0.04–0.08em 字距。** 字距更紧的等宽读成代码，不像编辑。
- **每个展示元素都带负字距。** display-hero -0.008em，vbig-numeral -0.015em，章节 / 收尾 / 宣言 / 引文 -0.005em。
- **方格纸网格每页常驻。** `.stage::before` 规则不可逐页覆盖，每个构图都坐在它上面。
- **顶部与底部细线框住每页。** `.hairlines::before` 与 `.hairlines::after` 规则默认生效，不得压掉。
- **页码坐在底部细线上方、留清晰纵向空间。** 底部细线锚在 `bottom: clamp(20px, 2vh, 32px)`，页码锚在 `bottom: clamp(48px, 4.8vh, 76px)`，两者不得相撞。

### 排印原则
Newsreader-400 + Hanken-600-大写-宽字距 + DM-Mono-宽字距的组合是系统的声部。换掉这三套字面/字重/大小写规则中的任一条，都会读成另一套设计系统。斜体允许通过 Newsreader 斜体（已加载）用于行内 `<em>`，以及宣言里带 `.roman` 翻转的编辑斜体处理。不用下划线。

行高在顶端收紧：display-hero / vbig-numeral 0.92，display-chapter 1.0，正文 1.5。紧展示 + 松正文的反差，给系统带来趋势报告的节奏。

## 布局

### 画布系统
画布是 `100vw × 100vh`，全视口、溢出隐藏。每张 `.slide` 绝对定位铺满视口，同一时刻一张带 `.active`（opacity 1、pointer-events auto）。过渡是 280ms opacity 淡入。

`.deck`（`position: fixed; inset: 0`）里坐一个 `.stage` 包装，提供奶油背景加常驻的 `::before` 方格纸网格。

### 边距与内边距比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.edge}` | clamp(36px, 3.6vw, 80px) | 内容、页码、细线的标准幻灯片边内缩 |
| `{spacing.edge-inner}` | clamp(60px, 8vw, 160px) | 宣言式居中陈述用的更紧内缩 |
| `{spacing.pad-top}` | clamp(76px, 8vh, 130px) | 顶部细线下、索引/数据/表格画框内的顶部内边距 |
| `{spacing.pad-bottom}` | clamp(100px, 10vh, 150px) | 底部细线上、索引/数据/表格画框内的底部内边距 |
| `{spacing.gap-lg}` | clamp(28px, 3vw, 56px) | 页内主区域之间的大间隙 |
| `{spacing.gap-md}` | clamp(20px, 2.2vh, 36px) | 标准元素间距 |
| `{spacing.gap-sm}` | clamp(14px, 1.6vh, 24px) | 紧间距，外壳条内间隙、出处到引文间隙 |
| `{spacing.gap-xs}` | clamp(10px, 1.2vh, 18px) | 竖排行间隙、最小元素间距 |

### 通用外壳画框
每页都带四件套外壳画框：
1. **顶部细线**：距顶约 2.6vh、左右内缩 `{spacing.edge}` 的 1.5px 实线钴蓝。
2. **底部细线**：距底约 2vh、左右内缩 `{spacing.edge}` 的 1.5px 实线钴蓝。
3. **页码**：锚在右下、距底约 4.8vh（底部细线上方）的 DM Mono 钴蓝。
4. **导航提示**：锚在左下、与页码同高度、40% 不透明度的 DM Mono 钴蓝。

这套画框由 `.hairlines` 与 `.pagenum` / `.nav-hint` 规则自动渲染，每张新页继承它。

一个嵌套的 **`.frame` 内容矩形** 坐在索引、数据、表格、章节布局的外壳内部。它以 `inset: {spacing.pad-top} {spacing.edge} {spacing.pad-bottom}` 绝对定位，充当真正的内容容器。

### 构图模式
外壳画框内，内容通常走以下某种构图手法（这里不枚举可用布局，是描述性而非规定性的）：
- `topbar` 块（左 Newsreader 标题、右等宽 lab-tag、下方 1.5px 钴蓝线）压在主内容区上方。
- 锚在内容区右缘的像素故障列（偶尔在左，如版权页）。
- 作小标点用的 QR 拼块补丁（通常右上角）。
- 锚在某条边的竖排等宽标签列。
- 由淡钴蓝分隔线隔开的等 flex 行组成的密集账目或索引。

## 纵深与层级

### 平中带结构线
Cobalt Grid 没有投影、没有抬升卡片、没有圆角表面、没有渐变。每个元素落在单一平面。

纵深信号全是结构性的：
- **1.5px 钴蓝线**：页顶/页底细线、顶栏线、出处线。
- **1px 淡钴蓝分隔线**：索引列表、表格、账目里的行分隔。
- **方格纸网格**：10% 不透明度钴蓝背景，造出被丈量过的平面感。
- **像素故障装饰**：竖向扫描线列加视觉纹理，不带 z 轴抬升。
- **QR 拼块补丁**：因纸色填充与 1.5px 纸色外凸，在网格 + 故障背景上读作独立图形物件（这个外凸功能上是"反阴影"，它把网格推开，好让 QR 拼块保持可读）。

QR 拼块的 1.5px 纸色外凸是系统里**唯一**类阴影效果，它为在像素故障列上保住可读性而存在，不造抬升。没有 z 轴纵深。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 0 | 每个结构元素：画框、卡片、账目行、QR 单元格、像素故障矩形、图表、表格 |
| 50%（圆） | 无，Cobalt Grid 没有圆形元素 |

系统**零圆角**。每个形状都是严格矩形。这在编辑系统里不寻常，也是趋势报告身份的一部分。

### 边框粗细
- **1.5px 实线 `{colors.ink}`**：主结构线，页顶/页底细线、顶栏底线、表头行底边、图表基线。
- **1px 实线 `{colors.ink}`**：引文署名上方的出处线、宣言出处顶边。
- **1px 实线 `{colors.ink-faint}`**（18% 不透明度）：密集列表 / 表格 / 账目条目之间的淡行分隔线。
- **1px 实线 `{colors.grid}`**（10% 不透明度）：每页背后常驻的方格纸网格。
- **1.5px box-shadow `{colors.paper}`**：QR 拼块可读性外凸（功能性，非装饰）。

所有结构边都是钴蓝。彩色边不存在（根本没有"彩色"，只有不同不透明度的钴蓝）。

### 装饰元素类型

**像素故障列**：阶梯状竖列，以内联 SVG 渲染。每级是一块填了均匀间隔钴蓝竖向扫描线、压在奶油上的矩形。级宽随列下探递减（或反之），造出"故障"像素化效果。锚在页面某边（通常右）、绝对定位、z-index 3、pointer-events 禁用。纯装饰，尺寸从紧凑 16vw × 全高的次级用法到 32vw × 全高的招牌封面装饰不等。不透明度 0.6–1.0 看语境（作背景时低，作主装饰时满）。

**QR 拼块补丁**：8×8 单元格网格（部分 `.on` = 实钴蓝，部分默认 = 纸色），组成类 QR 码拼贴。坐在纸色填充底上，4px 内边距、1.5px 纸色外凸（与像素故障列重叠时保住可读性）。典型尺寸 58–100px 方。用作构图标点，通常右上角。

**竖排标签列**：一列以 `writing-mode: vertical-rl` 与 `text-orientation: mixed` 书写的 DM Mono 标签，把拉丁文字顺时针转 90°。锚在右缘、垂直居中、均匀分布。读起来像沿页边叠起的目录式元数据。

**Topbar（带线）**：flex 行，左 Newsreader 标题、右小等宽 lab-tag，由 1.5px 实线钴蓝底边与下方内容分开。通用分节页眉模式。

**Frame**：以 `inset: {spacing.pad-top} {spacing.edge} {spacing.pad-bottom}` 绝对定位的内容容器。装页面真正的内容，同时避开细线画框、页码、导航提示。

**索引列表**：2×3 网格的等 flex 行，每行是 56px 的 num-tag 列 + 内容列（Newsreader 行标题与 Hanken 正文段落），由 1px 淡钴蓝底边分隔。

**像素堆叠条形图**：一排 8 根竖向"堆"，每根是水平小单元格的 flex column-reverse（默认 10% 钴蓝灭，`.on` 实钴蓝亮）。单元格数代表数值。条下方一条 1.5px 钴蓝顶边配等宽刻度标签作轴。把数据渲染成网格单元组成的像素化条，直接呼应像素故障装饰。

**账目表格**：密集行的 flex 列，每行是 5 列网格（76px num-tag / 0.6fr 名称 / 1.4fr 描述 / 0.7fr mood-tag / 0.5fr delta-tag），由 1px 淡钴蓝底边分隔。表头行用 1.5px 实线钴蓝。Delta 小片经 `::before` 用 `↑` / `↓` / `—` 前缀。

**宣言**：`{typography.display-manifesto}` Newsreader 的居中陈述，斜体 `<em>` 正文里含行内 `.roman`（非斜）强调瞬间。下方一条 1px 钴蓝顶边，配并排的 Hanken who-tag 与等宽 meta-tag。

**引文**：Hanken 眉题在上，`{typography.display-quote}` Newsreader 拉页引文居中，下方 1px 钴蓝顶边的出处行。右缘配一列紧凑像素故障列。

**版权页**：右对齐收尾布局。一个大 `{typography.display-closing}` Newsreader 标题右对齐，上方眉题。像素故障列锚在左缘（镜像封面）。页脚是 3–4 列网格的段落致谢。

## 该做与不该做

### 该做
- 每个 Newsreader 元素都设字重 400、`{colors.ink}`。适中字重下的细正体衬线是文学语域的身份。
- 每个标签、眉题、微型文字都用 Hanken Grotesk 字重 600 大写、0.16em+ 字距、`{colors.ink}` 渲染。
- 每个外壳元素（页码、等宽小片、刻度标签、竖排标签）都用 DM Mono、0.04–0.08em 字距、`{colors.ink}` 渲染。
- 每页背后保留常驻方格纸网格。网格就是系统，禁用它会破掉身份。
- 每页保持顶部与底部 1.5px 钴蓝细线，页码与导航提示坐在底部细线上方。
- 宣告式页面（封面、章节、引文、版权页）用像素故障列作系统主要装饰手法。
- 构图需要独立图形锚点时，把像素故障列与 QR 拼块补丁配对，QR 的纸色填充让它在故障线之上仍可读。
- 索引、数据、表格布局用 `topbar + 1.5px 钴蓝线` 模式作标准分节页眉处理。
- 密集列表、表格、账目的行之间用 1px 淡钴蓝分隔线。
- 图表渲染成网格单元的像素堆叠列（钴蓝亮 / 10% 钴蓝灭）。像素堆叠条处理呼应装饰故障，统一视觉语言。

### 不该做
- 不要引入第二墨色。系统严格双色：奶油纸 + 钴蓝墨。第二色相会破掉 risograph 身份。
- 不要把 Newsreader 标题设成字重 600 或 700。400-only 规则是签名。
- 不要禁用或隐藏方格纸网格。它是画布色调，不是可选装饰。
- 不要压掉页顶/页底细线。它们就是画框，每页都带。
- 不要给任何角加圆角。每个形状都是严格矩形，系统零圆形元素。
- 不要加投影、抬升卡片或渐变填充。纵深是结构性的（线 + 网格 + 故障），不是 z 轴。
- 不要用没有 0.16em+ 字距的 Hanken capitals。没字距的 Hanken caps 读起来像没处理过。
- 不要把页码直接放在底部细线上。它坐在 `bottom: clamp(48px, 4.8vh, 76px)`，与细线上方留清晰空间。
- 不要渲染没有纸色填充与 1.5px 纸色外凸的 QR 拼块。填充正是在像素故障列之上保住 QR 可读性的东西。
- 不要把宣言、引文、版权页布局塞满。这些布局刻意露出网格，塞太满会破掉沉思语域。

## 响应式行为

Cobalt Grid 是视口流式的 1920×1080 演示系统，通篇用 `clamp()` 与视口相对单位。源码里没有显式响应式断点，每个尺寸在最小与最大之间缩放。

### 缩放行为
- Display-hero 从最小视口约 100px 缩放到最大约 200px。
- 正文从 14px 缩放到 15px（刻意收得很窄，正文保持紧凑）。
- 方格纸网格从小视口 28px 单元格缩放到大视口 44px 单元格，页宽上大致维持 50–80 个格。
- 边内缩从 36px 缩放到 80px。
- 1.5px 细线与 1px 行分隔线固定不缩放。

### 放映行为
- 幻灯片以 280ms opacity 过渡交叉淡入。
- 导航由 JS 驱动（源码含 `.deck` / `.slide.active` 模式），适用通常的键盘方向键 / 空格约定。
- 左下导航提示以 40% 不透明度的等宽钴蓝显示交互指引。

### 打印 / 导出
未明确处理。每页是 100vw × 100vh 块，导出流程应逐页按 1920×1080 截图。网格与细线叠层在 PDF 抓取里应能正确渲染（无混合模式、无滤镜）。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 推荐中文搭配 | 来源 |
|---|---|---|---|
| 展示 / 标题（Newsreader 400） | Newsreader | 思源宋体 Noto Serif SC 700 | Google Fonts |
| 正文 / 标签（Hanken Grotesk 400–600） | Hanken Grotesk | 思源宋体 Noto Serif SC 400 | Google Fonts |
| 外壳 / 等宽（DM Mono） | DM Mono | DM Mono（仅拉丁/数字，等宽外壳保留拉丁） | Google Fonts |

### 混排策略

用**策略 A — 单字体栈带回退**：在同一条 `font-family` 栈里把 Noto Serif SC 声明在拉丁字体**之后**，这样拉丁字形渲染成 Newsreader / Hanken Grotesk，CJK 字形自动落到 NSC。等宽外壳保持拉丁/数字专用：页码、刻度、竖排小片不需要 CJK 回退（DM Mono 按设计没有 CJK 字形）。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400..500;1,6..72,400..500&family=Hanken+Grotesk:wght@400..700&family=DM+Mono:wght@400..500&family=Noto+Serif+SC:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --font-display: "Newsreader", "Noto Serif SC", Georgia, serif;
  --font-body: "Hanken Grotesk", "Noto Serif SC", sans-serif;
  --font-mono: "DM Mono", ui-monospace, monospace;
}
/* Headlines use Noto Serif SC 700; body uses Noto Serif SC 400. */
```

### 通用 CJK 调整

- **行高**：把 CJK 正文行高提到约 1.7（从 1.5 上调），汉字比拉丁小写需要更多纵向呼吸。
- **字距**：把汉字段上的 `letter-spacing` 清零（0.16em+ 的 Hanken caps 字距会打碎汉字节奏）。紧字距只保留在拉丁 span 上。
- **文字变换**：任何微型/标签/眉题是汉字时，去掉 `text-transform: uppercase`。中文没有大小写；强制大写对汉字无效，却会破坏里面混排的拉丁缩写的渲染。
- **标点**：中文句子用中文全角标点（，。：；「」），拉丁用半角（`,.:;""`）。绝不把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略末尾的 。，展示字符串里要去掉。
- **盘古之白**：相邻的汉字与拉丁/数字串之间插入一个细空格（或普通空格），例如 `2026 年`、`AI 产品`，提升混排可读性。
- **一句一款字体**：不要在句中切换 CJK 字族。某段文字挑 Noto Serif SC 的单一字重，绝不在同一短语里用两个。

### 美学提示

Noto Serif SC（思源宋体）是 Newsreader 天然的汉字搭档，两款都是安静的文学衬线，粗细调制在极大展示尺寸（vbig-numeral 到 18vh / 240px）下也撑得住。钴蓝压奶油的双色规则能不协商解决地吸收中文，因为只有一种墨色要分配。NSC 700 承载 Newsreader 400 在 100–200px 所做的展示瞬间，NSC 400 承载正文与标签。DM Mono 外壳层（页码、竖排小片、刻度）刻意保持拉丁/数字专用，`编号 001` 渲染成 DM Mono 里的拉丁 "001"，汉字前缀交给 Hanken/NSC，保住等宽目录外壳的"技术规格"声部。方格纸网格、像素故障列、QR 拼块装饰与内容无关，任何语言里读起来一致。以 `writing-mode: vertical-rl` 书写的竖排标签对汉字也成立，中文本就是原生竖排文字，但同一竖排串里混拉丁和汉字会把汉字转正、拉丁仍转 90°，按语言把串隔离开。

### 已知 CJK 缺口

Noto Serif SC 没有斜体轴（汉字排印历史上没有斜体），所以宣言布局里斜体 Newsreader 带 `.roman` 翻转的强调模式，内容是汉字时会塌掉。改用语重反差（NSC 700 对 NSC 400）或淡钴蓝色调（`{colors.ink-faint}`）找回强调语域。Newsreader 的光学尺寸轴（6..72）在 NSC 没有对应，汉字拿不到文学性的"这是小图注"光学修饰，但以 NSC 的品质，这点很少被察觉。

## 迭代指南

1. 每张新页都继承常驻方格纸网格、顶部与底部 1.5px 钴蓝细线、右下页码、左下导航提示。别逐页编写这些，它们活在 `.stage` 与 `.hairlines` 上。
2. 每个新标题都用 Newsreader 字重 400、`{colors.ink}`。别加粗，别上色。
3. 每个新标签都用 Hanken Grotesk 字重 600 大写、0.16em+ 字距、`{colors.ink}`。
4. 每个新外壳元素都用 DM Mono、`{colors.ink}`、0.04–0.08em 字距。
5. 索引 / 数据 / 表格布局上的新内容页用 topbar（左 Newsreader 标题 + 右 Hanken lab-tag）配 1.5px 钴蓝底线。
6. 新图表页用像素堆叠处理，column-reverse 堆里的单元格钴蓝亮 / 10% 钴蓝灭。别引入单块实心的填充条形图。
7. 新宣告式页面（封面、章节、引文、版权页）用像素故障列作主装饰。构图需要独立图形锚点时配 QR 拼块。
8. 密集列表里的新行分隔线用 1px 实线 `{colors.ink-faint}`（18% 不透明度），不用全强度钴蓝。全强度钴蓝留给主结构线。
9. 新组件继承零半径、无阴影、无渐变的平。若组件破掉其中任一条，先重新设计再纳入。
10. 系统有一种墨色（`{colors.ink}`）与一种表面（`{colors.paper}`）。新构图绝不引入第三色或第三种表面色调（paper-2 可用但极少需要）。

## 已知缺口

- 像素故障列按每次用法手写内联 SVG，没有生成式组件，调整阶梯图案要直接改 SVG 标记。
- QR 拼块 8×8 单元格图案按每次用法手写，每个实例手动摆放 `.on` 单元格，没有 QR 码生成逻辑。
- 像素堆叠条形图的单元格数在标记里硬编码，没有把数值翻译成亮单元格数的数据绑定层。
- 竖排标签列用 `writing-mode: vertical-rl`，现代浏览器可用，但混拉丁/CJK 在此方向下的渲染可能跨引擎有差异。
- 宣言布局的斜体带 `.roman` 翻转模式（斜体 Newsreader 正文里含行内非斜 `.roman` span 作强调）是典型斜体强调的反用，规则活在宣言专用 CSS 里，没有通用化。
- QR 拼块上的 1.5px 纸色外凸是当"反阴影"用的 `box-shadow`（把纸色填充向外延，清掉 QR 单元格背后的网格）。这是系统唯一的 `box-shadow`，不得挪作抬升用途。
- 版权页的像素故障列锚在左缘（镜像封面），其他页锚在右缘，方向逐页而定，编写新宣告式布局时要考虑。
- 方格纸网格单元格尺寸经 `clamp` 在 28–44px 间缩放，宽高比极端时页宽上的格数可能显得不均。
- 系统加载三款 Google Fonts 字族（Newsreader、Hanken Grotesk、DM Mono）的多个字重，首次渲染需要字体加载成功，否则 Georgia/Helvetica 回退会挪动视觉节奏。
