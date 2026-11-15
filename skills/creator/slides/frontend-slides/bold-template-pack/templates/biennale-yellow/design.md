---
version: alpha
name: Biennale Yellow
description: "A literary-editorial presentation system in the visual register of an art biennale catalogue or quiet exhibition poster. The aesthetic is built on warm parchment grounds (`#E9E5DB`) flooded with soft solar yellow (`#F1EE2E`) radial blooms, set against a single deep indigo navy ink color. Display type is Instrument Serif — a contemporary high-contrast serif with tall ascenders and elegant italics — paired with Archivo for sans-serif chrome and JetBrains Mono for numerical and metadata callouts. No drop shadows, no rounded corners, no bordered cards: the only structural lines are hairline 1px rules in ink. The mood sits between a folded museum brochure, a slow-reading literary quarterly, and a Mediterranean exhibition poster — confident, atmospheric, and deeply restrained."

colors:
  paper: "#E9E5DB"
  paper-deep: "#DCD6C4"
  sun: "#F1EE2E"
  sun-soft: "#F8F39B"
  haze: "#F0DA7C"
  ink: "#1B2566"
  ember: "#E26B4A"

color-aliases:
  line: ink

typography:
  display:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(120px, min(14.6vw, 22vh), 240px)"
    lineHeight: 0.86
    letterSpacing: -0.018em
  display-md:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(80px, min(10vw, 16vh), 200px)"
    lineHeight: 0.86
    letterSpacing: -0.018em
  display-sm:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(110px, min(11vw, 18vh), 200px)"
    lineHeight: 0.86
    letterSpacing: -0.018em
  display-it:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontStyle: italic
    fontSize: "clamp(56px, min(7vw, 11vh), 120px)"
    lineHeight: 1.04
    letterSpacing: -0.005em
  numeral-jumbo:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(220px, min(28vw, 64vh), 720px)"
    lineHeight: 0.84
    letterSpacing: -0.04em
  numeral-lg:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(120px, min(15vw, 22vh), 280px)"
    lineHeight: 0.9
    letterSpacing: -0.04em
  numeral-md:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(72px, min(7vw, 12vh), 144px)"
    lineHeight: 0.92
    letterSpacing: -0.01em
  headline:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(40px, min(4.6vw, 7vh), 88px)"
    lineHeight: 1.06
    letterSpacing: -0.005em
  headline-sm:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(32px, min(3.6vw, 6vh), 56px)"
    lineHeight: 1
  date-rail:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(48px, min(5.2vw, 9vh), 96px)"
    lineHeight: 0.96
    letterSpacing: -0.005em
  ledger-title:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(20px, 1.6vw, 30px)"
    lineHeight: 1.15
  strand-title:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(22px, 1.7vw, 32px)"
    lineHeight: 1.1
  strand-num:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(28px, 2vw, 38px)"
    lineHeight: 1
  body-lede:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: "clamp(15px, 1.05vw, 18px)"
    lineHeight: 1.55
  body:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: "clamp(14px, 0.95vw, 16px)"
    lineHeight: 1.5
  body-sm:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: "clamp(11px, 0.78vw, 13px)"
    lineHeight: 1.5
  micro-label:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 600
    fontSize: "clamp(11px, 0.85vw, 14px)"
    lineHeight: 1.2
    letterSpacing: 0.18em
    textTransform: uppercase
  micro-label-tight:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 600
    fontSize: "clamp(10px, 0.72vw, 12px)"
    lineHeight: 1.2
    letterSpacing: 0.16em
    textTransform: uppercase
  rail-label:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 600
    fontSize: "clamp(11px, 0.85vw, 13px)"
    lineHeight: 1
    letterSpacing: 0.32em
    textTransform: uppercase
  mono-data:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontWeight: 400
    fontSize: "clamp(12px, 0.85vw, 14px)"
    lineHeight: 1.4
    letterSpacing: 0.04em
  mono-date:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontWeight: 400
    fontSize: "clamp(13px, 0.95vw, 16px)"
    lineHeight: 1.4
    letterSpacing: 0.02em
  pagenum:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontWeight: 400
    fontSize: "clamp(11px, 0.85vw, 13px)"
    lineHeight: 1
    letterSpacing: 0.08em

spacing:
  pad-edge: "clamp(40px, 4vw, 76px)"
  pad-region: "clamp(40px, 4.2vw, 80px)"
  pad-foot: "clamp(56px, 5vh, 88px)"
  pad-strand-y: "clamp(12px, 1.6vh, 22px)"
  gap-region: "clamp(20px, 2.5vw, 48px)"
  gap-strand: "clamp(14px, 1.8vh, 22px)"
  gap-footer-col: "clamp(20px, 2.4vw, 44px)"
  pagenum-bottom: "clamp(22px, 2.4vh, 42px)"
  pagenum-right: "clamp(24px, 2.4vw, 48px)"

canvas:
  width: 100vw
  height: 100vh
  background: "{colors.paper}"

components:
  pagenum:
    position: "absolute, right + bottom"
    color: "{colors.ink}"
    opacity: 0.75
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "clamp(11px, 0.85vw, 13px)"
    letterSpacing: 0.08em
    description: "Single mono pagenum NN / NN pinned to bottom-right of every slide at 75% opacity. The only persistent chrome on every surface."
  hairline-rule:
    border: "1px solid {colors.ink}"
    description: "1px solid ink horizontal or vertical rule. The system's only border treatment — separates header bands from content, footer columns from each other, ledger rows from each other. No thicker rule exists."
  hairline-rule-soft:
    border: "1px solid rgba(27, 37, 102, 0.18-0.2)"
    description: "1px ink at 18-20% opacity. Used for between-row separators inside dense ledger or strand lists where a full-weight rule would feel oppressive."
  sun-bloom:
    background: "radial-gradient using {colors.sun} {colors.sun-soft} {colors.haze} blending to transparent on {colors.paper}"
    description: "Large soft radial bloom of solar yellow placed off-center or behind a focal element. The system's primary atmospheric layer. Sized 42-70% of viewport in the larger axis."
  ember-bloom:
    background: "radial-gradient using {colors.ember} at 15-22% opacity blending to transparent"
    description: "Small warm peach bloom used as a counter-temperature accent in a corner opposite the sun bloom. Always subordinate; never dominant."
  block-tile:
    background: "{colors.sun} at 40-70% opacity"
    description: "Geometric blocks of translucent solar yellow placed on an 8-row × 4-column grid behind cover or colophon surfaces. Suggests a layered poster underprint."
  yellow-panel:
    background: "{colors.sun}"
    color: "{colors.ink}"
    description: "Full-bleed yellow panel covering a column or third of the slide. The strongest possible color statement — used when a region needs to read as poster-fill, not paper."
  bar-ink:
    background: "{colors.ink}"
    height: "clamp(14px, 1.6vh, 22px)"
    description: "Solid ink horizontal bar for data charts. Width carries the data value."
  bar-lit:
    background: "{colors.sun}"
    border: "1px solid {colors.ink}"
    height: "clamp(14px, 1.6vh, 22px)"
    description: "Highlighted variant of bar-ink — yellow fill with 1px ink stroke. Used to mark the current or featured row in a series."
  strand-row:
    layout: "grid 56px 1fr, gap clamp(14px, 1.4vw, 24px), border-bottom hairline-soft, padding-bottom clamp(12px, 1.6vh, 22px)"
    description: "Numbered editorial list row — numeral cell + content cell separated by hairline-soft. Used for programmes, agendas, and curated lists."
  ledger-row:
    layout: "grid 92px 1.6fr 0.9fr 80px, gap clamp(14px, 1.4vw, 28px), border-bottom hairline-soft, padding clamp(10px, 1.3vh, 18px) 0"
    description: "Four-column tabular row for calendars and itineraries. Date column is mono, title is serif, venue is sans, duration is mono right-aligned."
  footer-band:
    layout: "grid 4-column with hairline-rule top border on each cell, gap clamp(20px, 2.4vw, 44px)"
    description: "Four-column metadata strip pinned to the bottom of cover and colophon surfaces. Each cell has a tiny uppercase tag + a brief plain-English statement."
  vertical-rail:
    transform: "rotate(-90deg) translateY(-50%) at left edge"
    fontFamily: "'Archivo', sans-serif"
    fontSize: "clamp(11px, 0.85vw, 13px)"
    letterSpacing: 0.32em
    textTransform: uppercase
    description: "Rotated vertical text label running up the left edge. Used on chapter/divider surfaces as a section marker."
  date-rail-stack:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontSize: "clamp(48px, min(5.2vw, 9vh), 96px)"
    lineHeight: 0.96
    textAlign: right
    description: "Large serif date or date-range stacked at top-right of cover surfaces. Uses an en-dash to indicate spans."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/biennale-yellow/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Biennale Yellow 是一套**文学编辑式演示系统**，取法欧洲艺术双年展图录、慢节奏展览海报与文学季刊的视觉语言。没有卡片、没有按钮、没有阴影、没有圆角。结构语汇只有三样：纸、墨、黄。

排印系统以 **Instrument Serif** 为轴，这是一款当代高对比衬线，升部高、斜体优雅、字端微张。它承载每一个展示瞬间、每一个数字、每一段引文，尺度从小标题（40px）一直跨到 700px 以上的巨型数字。排得紧（行高 0.86、字距 −0.018em）时，它读起来是自信的编辑式展示；换到斜体排得松些（行高 1.04、字距 −0.005em），又成了慢读的引文字面。**Archivo** 是无衬线搭档，用于正文段落，以及小巧、宽字距的大写标签（即 micro-label 处理）。**JetBrains Mono** 承担所有数字与元数据标注：日期、账目数字、页码。三字面系统严谨克制，三者之间的反差就是整套排印叙事。

色彩世界以**暖羊皮纸**（`{colors.paper}` — `#E9E5DB`）作通用底，配一色 **ink**（`{colors.ink}` — `#1B2566`，深靛海军蓝），所有文字与所有分隔线都用它。系统招牌色是 **sun**（`{colors.sun}` — `#F1EE2E`），高饱和日照黄，可作满铺面板、柔和放射状光晕，或几何拼块底纹。一抹**柔暖灰桃**（`{colors.ember}` — `#E26B4A`）只作从属的反向温度点缀，永远以 15-22% 不透明度出现在对角的径向光晕里。系统不用反色处理，始终认准暖底上的海军蓝墨。

纵深是**氛围性的，不是结构性的**。系统里没有任何投影。纵深来自层叠的黄色径向渐变（sun-bloom 与 ember-bloom 组件），以及封面类表面上可选的 block-tile 底纹。卡片没有边框，区域之间只用 1px 墨色细线分隔。不靠边框重量，这本身就是美学：设计读起来像印出来的，不像搭出来的。

**密度取向：编辑式克制。** 这套系统稀疏时优雅，拥挤时散架。典型一页承载一个大型展示瞬间 + 少量辅助元素（一个 micro-label、一段正文、一组有序列表，或单单一团径向光晕）。用卡片、按钮、面板或堆叠组件塞满画布，会把它变成另一套美学。即便是密集表面（日历或节目单），密度也来自表格的重复，而非视觉的丰富：许多安静的、由细线分隔的元数据行，而不是许多带框的格子。宽裕的边内边距（40-76px）与宽的页脚/页眉带让画布能呼吸。

**关键特征：**
- 每处表面都是暖羊皮纸底（`{colors.paper}`）；绝不用纯白，绝不用灰。
- 单一墨色（`{colors.ink}`）用于所有文字与所有分隔线，没有次级文字色。
- 日照黄（`{colors.sun}`）有三种用法：满铺面板、柔和径向光晕、半透明几何拼块底纹。
- Instrument Serif 承担 40px 到 720px+ 的每一个展示瞬间。
- Archivo Bold 大写 + 0.16–0.32em 字距是通用标签声部。
- JetBrains Mono 只留给日期、账目数字与页码。
- 1px 的 `{colors.ink}` 细线是唯一边框处理，用于页眉带、账目行、页脚列与 strand 分隔线。
- 没有投影、没有圆角、没有卡片轮廓、没有按钮。装饰是氛围性的（径向光晕）或几何性的（半透明拼块）。
- 每处表面右下角有常驻的 `01 / NN` JetBrains Mono 页码，75% 不透明度。
- 章节/分隔页左边缘可选旋转的竖排 rail-label。

## 颜色

### 调色板

- **Paper**（`{colors.paper}` — `#E9E5DB`）：暖羊皮纸画布。默认且近乎通用的背景。读起来是柔化的、暖意明显的灰白，绝不中性，绝不冷。
- **Paper-deep**（`{colors.paper-deep}` — `#DCD6C4`）：略深的羊皮纸调，可作次级表面，或用来暗示一条暗带而不真用阴影。留给需要在暖纸家族内做表面区隔的时刻。
- **Ink**（`{colors.ink}` — `#1B2566`）：全系统唯一的文字与线条色。一种深靛海军蓝，读起来是自信的、偏蓝的编辑黑。用于标题、正文、micro-label、等宽字、细线与墨条填充。CSS 变量 `--line` 也解析到这个颜色。
- **Sun**（`{colors.sun}` — `#F1EE2E`）：系统招牌的日照黄。高饱和、略偏绿。三种用法：满出血或整列出血的面板、柔和径向光晕的核心、以及 40-70% 不透明度的几何拼块。
- **Sun-soft**（`{colors.sun-soft}` — `#F8F39B`）：更淡的奶油黄，用在 sun-bloom 渐变的中段色标，柔化从饱和 sun 到纸的过渡。
- **Haze**（`{colors.haze}` — `#F0DA7C`）：偏芥末的暖黄，用在 sun-bloom 渐变最外层色标，让光晕没有硬边地融进纸里。
- **Ember**（`{colors.ember}` — `#E26B4A`）：暖桃橙，只作 15-22% 不透明度径向光晕里从属的反向温度点缀。绝不作为填充色，绝不作为文字色。它的职责是在画布另一侧与 sun-bloom 取得平衡。

### 默认值

- **默认表面背景**：`{colors.paper}`。每处表面都从这里起。
- **默认标题色**：`{colors.ink}`。始终如此。标题绝不出现在黄、灰桃或 paper-deep 里，只用墨色。
- **默认正文文字色**：`{colors.ink}`。正文与展示用同一颜色，反差靠尺寸与字重，不靠颜色。
- **默认分隔线色**：`{colors.ink}`（1px 实线）作主分隔，墨色 18-20% 不透明度作次级行分隔。
- **海报瞬间的默认强调表面**：`{colors.sun}`，满铺日照黄面板，其上压 `{colors.ink}` 文字。
- **默认氛围层**：一枚偏心的 `{components.sun-bloom}`，对角可选配一枚 `{components.ember-bloom}`。
- **默认图表条色**：`{colors.ink}`。当前/精选条用 `{components.bar-lit}`（黄填充、墨描边）。
- **默认标签色**：文字用 `{colors.ink}`，无填充。标签靠字距 + 大写 + 字重 600，不是填充胶囊。

系统绝不反色：黄面板上压墨色文字是对的（也是招牌处理），但墨底上放黄文字不存在。文字永远是墨色，变化在文字背后的东西，不在文字颜色本身。

## 排印

### 字族栈
系统用三款字面，各守一个严密定义的角色。

**Instrument Serif**（Google Fonts，斜体 + 正体）是展示兼编辑字面。高对比、升部高、字端微张，气质是当代文学，更接近杂志刊头而非传统书籍衬线。正体用于标题、数字、账目标题、日期栏。斜体用于宣言式引文和某些强调时刻。排得紧（行高 ≤ 1.06，负字距 −0.005 到 −0.04em）。

**Archivo**（Google Fonts）是无衬线搭档。字重 400 用于正文段落（行高 1.5），字重 600 用于通用 micro-label 处理（大写、0.16-0.32em 字距、10-14px）。绝不用中间字重，绝不用于标题。

**JetBrains Mono**（Google Fonts）是数字/元数据字面。只用于账目里的日期、数据页的等宽数字标注、页码和导航提示。它的板状特征让数字内容有编辑分量，不必靠加粗。

### 排印比例

| Token | 尺寸（clamp） | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 120–240px | Instrument Serif | 400 | 封面级展示标题 |
| `{typography.display-sm}` | 110–200px | Instrument Serif | 400 | 面板语境下的编辑式展示 |
| `{typography.display-md}` | 80–200px | Instrument Serif | 400 | 收尾陈述展示 |
| `{typography.display-it}` | 56–120px | Instrument Serif italic | 400 | 宣言级斜体引文正文 |
| `{typography.numeral-jumbo}` | 220–720px | Instrument Serif | 400 | 章节分隔的序数数字 |
| `{typography.numeral-lg}` | 120–280px | Instrument Serif | 400 | 装饰性引号、超规格标点 |
| `{typography.numeral-md}` | 72–144px | Instrument Serif | 400 | 英雄统计数字 |
| `{typography.headline}` | 40–88px | Instrument Serif | 400 | 分节主标题、大号引文正文 |
| `{typography.headline-sm}` | 32–56px | Instrument Serif | 400 | 区域标题、账目/日历顶栏 |
| `{typography.date-rail}` | 48–96px | Instrument Serif | 400 | 叠在表面顶部的日期或日期区间 |
| `{typography.ledger-title}` | 20–30px | Instrument Serif | 400 | 日历/账目行内的标题单元格 |
| `{typography.strand-title}` | 22–32px | Instrument Serif | 400 | 编号 strand/列表行内的标题 |
| `{typography.strand-num}` | 28–38px | Instrument Serif | 400 | strand 行内的数字单元格 |
| `{typography.body-lede}` | 15–18px | Archivo | 400 | 章节标题后的导语段 |
| `{typography.body}` | 14–16px | Archivo | 400 | 标准正文段落 |
| `{typography.body-sm}` | 11–13px | Archivo | 400 | 页脚带正文、密集元数据 |
| `{typography.micro-label}` | 11–14px | Archivo | 600 | 通用大写眉题标签 |
| `{typography.micro-label-tight}` | 10–12px | Archivo | 600 | 页脚单元格内更小的大写标签 |
| `{typography.rail-label}` | 11–13px | Archivo | 600 | 竖排旋转的栏标签 |
| `{typography.mono-data}` | 12–14px | JetBrains Mono | 400 | 图表年份/数值标签、行内等宽数据 |
| `{typography.mono-date}` | 13–16px | JetBrains Mono | 400 | 日历账目里的日期列 |
| `{typography.pagenum}` | 11–13px | JetBrains Mono | 400 | 常驻页码 |

### 默认值

- **封面级展示标题默认尺寸**：`{typography.display}`（120–240px clamp）。再小就读成分节级，不是封面级。
- **分节主标题默认尺寸**：`{typography.headline}`（40–88px clamp）。
- **章节分隔数字默认尺寸**：`{typography.numeral-jumbo}`（220–720px clamp）。别缩小，巨型数字就是分隔页的意义所在。
- **英雄统计默认尺寸**：`{typography.numeral-md}`（72–144px clamp）。统计数字与标题共用同一衬线，它们是展示瞬间，不是数据外壳。
- **段落正文默认尺寸**：`{typography.body}`（14–16px）。章节标题后的导语升一档到 `{typography.body-lede}`（15–18px）。
- **任何眉题标签默认尺寸**：`{typography.micro-label}`（11–14px），字重 600、大写、0.18em 字距。
- **任何 Archivo 正文默认字重**：400。Archivo 正文用别的字重会破掉节奏。
- **任何 micro-label 默认字重**：600。字重 400 或 700 的标签读起来要么怯要么过大。
- **任何大写标签默认字距**：最低 0.16em，最高 0.32em。没有宽字距的标签读成代码，不像编辑。

拿不准该用哪个展示 token 时，主瞬间默认取 `{typography.headline}`（40–88px），单个英雄统计取 `{typography.numeral-md}`（72–144px）。display、display-sm、display-md 留给封面/版权页/海报级时刻。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每一个 display、numeral、headline、ledger-title 元素都是 Instrument Serif 字重 400。** 系统里没有粗衬线展示，这款字面的对比度本身就是字重信号。把 Instrument Serif 设成字重 700 会毁掉全部优雅。
- **每个 Instrument Serif 展示元素都用紧行高（0.84–1.06）。** 展示上宽松行高会毁掉编辑海报感，大衬线标题必须显得叠紧，而不是透气。
- **每个 Instrument Serif 展示元素都用负字距。** 展示、标题、巨型数字用 −0.018 到 −0.04em；斜体展示用 −0.005em。没有负字距，宽身字形读起来像没处理过。
- **每个 micro-label 都是大写 Archivo 字重 600、字距 ≥ 0.16em。** 没有例外。没有大写 + 字距的标签在这套系统里不算标签，只是一段游离的无衬线文字。
- **每个数字元数据元素（日期、页码、图表数值、日历日期）都是 JetBrains Mono。** 衬线数字用于展示瞬间，等宽数字用于数据外壳。别越线。
- **每个斜体宣言级引文都用 `{typography.display-it}`。** 把斜体引文设成标题尺度（40–88px）会读成更小的瞬间，斜体本该主导全场。
- **每个正文段落都是 Archivo 字重 400、行高 ≥ 1.45。** 系统里不存在 Instrument Serif 正文，Instrument 只做展示。

### 排印原则

声部对比是**缓慢优雅的衬线 ↔ 宽字距大写无衬线 ↔ 表格化等宽**。斜体 Instrument 是系统的"情绪"声部（只留给引文与宣言时刻）；正体 Instrument 是"陈述"声部；Archivo 大写加字距是"标签"声部；等宽是"数据"声部。各司一职。

混排规则很紧：Instrument Serif 标题里的 `<em>` 保持斜体 Instrument Serif（不换字面）。Archivo 正文段落里的 `<em>` 变成斜体 Archivo，不是衬线。不要在行内混字面。

每个元素的颜色都锁死为墨色。系统里没有"强调色文字"处理，强调靠氛围光晕和面板填充，不靠文字颜色。

## 布局

### 画布系统
系统以每页 `100vw × 100vh` 为目标。幻灯片绝对定位，通过 opacity 过渡（280ms ease）交叉淡入。同一时刻只有一页 `.active`。每一处尺寸都用同时带 vw 与 vh 项的 CSS `clamp()`，排印 clamp 里含 `min(...vw, ...vh)` 模式，使展示文字按两条视口轴里较短的一条缩放。

### 内边距与间距比例

| Token | 范围 | 用途 |
|---|---|---|
| `{spacing.pad-edge}` | 40–76px | 任意幻灯片边缘到内容的标准边内边距 |
| `{spacing.pad-region}` | 40–80px | 满铺黄面板或大区域的内部内边距 |
| `{spacing.pad-foot}` | 56–88px | 有页脚带时的底部内边距 |
| `{spacing.gap-region}` | 20–48px | 两个主内容列/区域之间的间隙 |
| `{spacing.gap-strand}` | 14–22px | 编号列表里 strand 行之间的间隙 |
| `{spacing.gap-footer-col}` | 20–44px | 页脚带元数据条的列间隙 |
| `{spacing.pagenum-bottom}` | 22–42px | 常驻页码的下内缩 |
| `{spacing.pagenum-right}` | 24–48px | 常驻页码的右内缩 |

### 常驻外壳
**页码**是画布上唯一的常驻元素。它出现在每页 `bottom-right`，用 11–13px JetBrains Mono、墨色、不透明度 0.75。**nav-hint**（`← / → · space`）只出现一次，固定在视口左下角，10–12px JetBrains Mono / 不透明度 0.4。nav-hint 不属于幻灯片构图，它活在 `.stage` 之外。

### 边缘纪律
每个有意义的元素都遵守最低 40px（移动端）到 76px（桌面）的边内缩。系统的优雅依赖边缘的负空间；把内容推到出血边（满出血面板、光晕、拼块除外）会破掉图录感。

### 氛围层
每页可在内容背后承载一层或两层氛围：
- **sun-bloom**（`{components.sun-bloom}`）：一大团柔和的日照黄径向渐变，尺寸占视口 42-70%，偏心或压在焦点元素后方。
- **ember-bloom**（`{components.ember-bloom}`）：一小团暖桃径向渐变，15-22% 不透明度，放在 sun-bloom 对角的角落。

这些层不是可选装饰，而是系统主要的纵深机制。没有光晕的表面读起来是平羊皮纸。

## 纵深与层级

### 无投影
系统**零投影**。没有 `box-shadow`，没有 `text-shadow`，没有 `filter: drop-shadow(...)`。纵深靠氛围传达。

### 氛围纵深（Sun Bloom）
主要纵深机制是 **sun-bloom**：一大团柔和的日照黄径向渐变，从画布上某点绽开。光晕解剖是一组三到四个色标的层叠径向渐变：
- 0%：`{colors.sun}` 70-95% 不透明度（热核）
- 约 30-40%：`{colors.sun}` 40-65% 不透明度（光晕）
- 约 55-65%：`{colors.haze}` 18-22% 不透明度（柔和外延）
- 80-90%：`{colors.paper}` 0%（平滑融进底）

光晕尺寸与位置随表面需要变化：封面用居中或略偏心的光晕，占视口 42% × 38%；章节页用锚在角落、720px 半径的光晕；收尾页用锚在底部、从下方升起的 55% × 50% 光晕。

### 反向温度点缀（Ember Bloom）
sun-bloom 对角可选一枚 **ember-bloom**，在不抬高画布饱和度的前提下制造冷暖张力。始终 15-22% 不透明度，始终小于 sun-bloom，始终从属。

### 几何底纹（Block Tiles）
在封面与版权页表面，内容背后还可加一层 **block-tile**：半透明日照黄矩形，排在 8 行 × 4 列的网格上，40-70% 不透明度。这层暗示层叠的海报底印，不必落实成实色面板。拼块是装饰几何，不是活动内容区域。

### 黄色面板（结构色）
需要最强色彩表态的表面，用 **yellow-panel** 满铺（`{components.yellow-panel}`）把画布的一列、一半或三分之一盖成饱和 `{colors.sun}`。这是系统唯一的"硬"色彩处理；用了面板，墨色文字就以全不透明度压在上头。面板没有边框也没有阴影，它们直接与纸边或另一块面板边相接。

### 细线
内部结构纵深由 **1px 实线墨色细线**传达，分隔页眉带与内容、账目行彼此、页脚列彼此。细线绝不粗于 1px。次级列表行之间（例如 strand 分隔线），线降到 `rgba(27, 37, 102, 0.18-0.2)`：同色，低不透明度。

## 形状与处理

### 圆角
**处处为零。** 每个形状都是严格的矩形。径向光晕技术上是圆，但没有可见边缘，会融进纸里。

### 边框粗细
- **1px 实线 `{colors.ink}`**：通用分隔线。用于页眉带下划线、账目行分隔、页脚列顶线、精选行上带描边的图表条强调。
- **1px 实线 `rgba(27, 37, 102, 0.18-0.2)`**：同款线的柔和变体。用于密集列表内部的次级行分隔，全重墨色在那里会显重。

系统**没有更粗的边框**。哪里都没有 2px、3px、4px 轮廓。视觉结构靠细线的轻。

### 装饰元素类型

**Sun-bloom**：一大团柔和的日照黄径向渐变，偏心或压在焦点元素后方。系统主要的纵深机制。每处表面始终一枚，有时配一枚反向光晕。

**Ember-bloom**：一小团暖桃径向渐变，15-22% 不透明度，放在 sun-bloom 对角。从属的氛围平衡。

**Block-tile 底纹**：半透明日照黄矩形，排在 8×4 网格系统里。暗示层叠海报的装饰几何，用于封面与版权页类表面。

**Yellow panel**：满出血的一列、一半或三分之一画布，铺满 `{colors.sun}`。系统最强的色彩表态。其上承载墨色文字。

**Hairline rule**：1px 实线墨色。用于页眉带下划线、账目分隔、页脚列顶线。系统唯一的边框。

**Footer band**：封面/版权页底部四列元数据条。每个单元格有一条 `{components.hairline-rule}` 顶线、一个 Archivo micro-label 和一句简短正文。

**Strand row**：编号编辑式列表行，衬线数字单元格 + 衬线标题 + 无衬线正文，行与行之间用 hairline-soft 分隔。

**Ledger row**：四列表格化日历/行程行：等宽日期 + 衬线标题 + 无衬线地点 + 等宽时长（右对齐），用 hairline-soft 线分隔。

**Vertical rail label**：竖排旋转的 Archivo 大写文字，沿章节分隔页左边缘上行，0.32em 字距。

**Date rail**：叠在封面表面右上、大号衬线的日期或日期区间，常用连接号表示跨年跨月的区间。

**Jumbo numeral**：单个巨大的 Instrument Serif 数字（220-720px），主导分隔页。始终衬线，始终字重 400，始终紧行高。

**Chart bar**：实色墨色矩形，宽度承载数据值。当前/精选条换成黄填充配 1px 墨描边（`{components.bar-lit}`）。图表布局用网格行模式：等宽年份标签 + 条 + 等宽数值，之间留 gap。

## 该做与不该做

### 该做

- 用 `{colors.paper}` 作通用背景。每处表面都从羊皮纸起。
- 每一行文字都用 `{colors.ink}`：展示、正文、micro-label、等宽，全部如此。单一文字色不可商量。
- 每个展示瞬间都用 Instrument Serif 字重 400、紧行高（0.84-1.06）与负字距（-0.018 到 -0.04em）。衬线的优雅活在这套配置里。
- 每处表面至少加一枚 `{components.sun-bloom}`。氛围纵深就是系统的纵深机制，平的羊皮纸表面读起来像坏了。
- 想要冷暖张力又不想抬高整体饱和度时，给 sun-bloom 在对角配一枚 `{components.ember-bloom}`。
- 每处结构分隔都用 `{components.hairline-rule}`（1px 实线墨色）：页眉带下划线、账目行、页脚列、strand 分隔。
- 每个大写标签都用 Archivo 字重 600、0.16-0.32em 字距。没有宽字距，标签读成代码，不像编辑。
- 表面需要最强色彩投入时用 `{components.yellow-panel}`（满出血的 sun 列或面板），墨色文字以全不透明度压在上头。
- 每处表面右下角放常驻 `{components.pagenum}`（JetBrains Mono、75% 不透明度墨色）。
- JetBrains Mono 只留给数字与元数据标注：日期、账目数字、图表数值、页码、导航提示。绝不用于展示或正文。

### 不该做

- 不要加投影。系统零 box-shadow、零 text-shadow。任何模糊或偏移阴影都会立刻破掉印纸感。
- 不要给任何角加圆角。每个形状都是严格矩形。border-radius 禁用。
- 不要用粗于 1px 的边框。细线是唯一的边框语汇，2px、3px、4px 轮廓不存在。
- 不要把 Instrument Serif 设成字重 700 或任何粗字重。衬线的性格在字重 400；粗衬线展示会把系统压平。
- 不要引入第二种文字色。纸上的黄字、任何地方的灰桃字、柔化墨色的次级文字，都不存在。文字永远是全不透明度墨色。
- 不要用卡片或面板塞满画布。系统稀疏时优雅。带框卡片、成堆按钮、多区域容器网格会破掉编辑式克制。
- 不要反色：墨底配黄字或纸色字不属于系统。墨底只留给图表条和细小的分隔线元素。
- 不要用 Inter、Helvetica、system-ui 顶替 Archivo，也不要用 Times 顶替 Instrument Serif。字体选择就是视觉身份，替换会让美学崩塌。
- 不要把等宽用于正文或标题。JetBrains Mono 只给数字/元数据外壳。
- 不要省掉表面的光晕层。平的羊皮纸页读起来像 CMS 模板，光晕才是传递"双年展"气质的氛围。

## 响应式行为

本系统构建为**视口流式 100vw × 100vh 演示文稿**，没有响应式断点。每个字号、内边距、间隙都用同时带 vw 与 vh 项的 CSS `clamp()`，`clamp(40px, min(4.4vw, 7vh), 88px)` 是典型模式。展示文字按两条视口轴里较短的一条缩放，纵向摆放不会把标题撑爆。

### 缩放行为
- 封面级展示从 120px 缩放到 240px。
- 章节分隔巨型数字从 220px 缩放到 720px。
- 标题从 40px 缩放到 88px。
- 正文从 14px 缩放到 16px。
- 边内边距从 40px 缩放到 76px。
- 细线（1px）与页码尺寸（11-13px）基本固定。

### 放映行为
- 用 `ArrowRight`、`PageDown` 或 `Space` 前进。
- 用 `ArrowLeft` 或 `PageUp` 后退。
- `Home` 跳首页，`End` 跳末页。
- 横向触摸滑动，40px 阈值前进/后退。
- 幻灯片在 `.active` 类上以 280ms ease 的 `opacity` 切换交叉淡入。只有激活页是 `pointer-events: auto`。

### 打印行为
系统没有 `@media print` 规则。交叉淡入过渡只用于屏幕。静态导出时逐页截图能保留所有氛围层（径向光晕是纯 CSS 渐变，不是图片资源）。

### 移动端行为
展示 clamp 里的 `min(vw, vh)` 模式让窄的纵向视口自动缩小展示文字以适配。strand 与 ledger 行用固定 px 的首列（56px、92px），窄宽度下可能偏紧；系统为横向演示语境设计，在 768px 以下的纵向用法里能用，但没做优化。

## CJK 与国际化内容

用本模板承载中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文搭配，并套用通用 CJK 调整。所有推荐中文字体均通过 CDN 加载，无需安装。

### 推荐中文搭配

| 角色 | 拉丁（默认） | 中文对应 |
|---|---|---|
| 展示 / 数字 / 标题 / 日期栏 | Instrument Serif 400 | 得意黑 Smiley Sans (oblique) 用于展示瞬间；长篇衬线标题回退到思源宋体 Noto Serif SC 400 |
| 正文 / 导语 / micro-label | Archivo 400–600 | 正文用思源宋体 Noto Serif SC 400；micro-label 用思源黑体 Noto Sans SC 600 |
| 等宽数据 / 日期 / 页码 | JetBrains Mono 400 | 思源黑体 Noto Sans SC 500 配表格感对齐，见下方已知 CJK 缺口 |

### 混排策略

**策略 A**：每个角色一款自带拉丁字形覆盖的 CJK 字族。思源宋体与思源黑体都自带拉丁字形，与汉字并排也干净，混排句子会用一致字面渲染。得意黑要克制地用，只用在最大的展示瞬间，它略斜的倾斜正好呼应拉丁原版里 Instrument Serif 所提供的意大利海报气质。其余一切（正文、micro-label、等宽）交给 Noto Serif SC / Noto Sans SC 同时覆盖两套文字。

### 加载

在模板 `<head>` 中加入：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700&family=Noto+Serif+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/cn-fontsource-smiley-sans-oblique/font.min.css">
```

加载后，在需要最强海报气质的展示 token 上把得意黑写作 `font-family: 'Smiley Sans Oblique', 'Noto Serif SC', serif`。

### 通用 CJK 调整

- **行高**：在拉丁规格上提高约 15–25%。正文 1.75–1.85（从 1.5–1.55 上调），展示 1.05–1.15（从 Instrument Serif 极紧的 0.84–0.96 上调）。这里的拉丁展示 token 行高低到 0.84，压到这个程度 CJK 字符会纵向相撞。中文展示至少放到 1.0，多行标题放到 1.15 以上。
- **字距**：每段 CJK 文本设为 0。拉丁展示 token 用 −0.005em 到 −0.04em 的负字距，套在方正 CJK 字形上会笔画重叠、读着像坏了。micro-label 的 0.16–0.32em 宽字距也降到 0。
- **文字变换**：不要对中文套 `uppercase`，CJK 没有大小写。系统里每个 micro-label 与 rail-label 都用 `text-transform: uppercase`，CJK 文本要去掉。
- **标点**：用全角中文标点（，。：；！？「」（））。把日期区间里的连接号分隔符换成中文"至"或全角「—」。
- **展示标题不加句号**：中文排印惯例，展示级标题末尾不写 。
- **中西文之间加空格（盘古之白）**：每个汉字与相邻的拉丁字符或数字之间插入一个 ASCII 空格。写 `2024 春季双年展`，不要写 `2024春季双年展`。
- **一句一款字体**：思源宋体以统一衬线风格覆盖 CJK 与拉丁字形，混排的编辑句子交给它处理。不要让浏览器在段落中途切回 Archivo。

### 本系统的美学提示

系统的编辑身份建立在 Instrument Serif 高对比、升部高的性格上，这款字面传递"艺术双年展图录"和"慢读文学季刊"。语域上最接近的中文对应是：正文与编辑式展示用**思源宋体 Noto Serif SC**，海报级展示瞬间留给**得意黑 Smiley Sans Oblique**——拉丁原版里正是 Instrument Serif 在 120–240px 承担最重的身份工作。得意黑略带斜意的板状特征正好匹配意大利展览海报的气质；纯 Noto Serif SC 放在巨型数字上读起来是克制的学院中文，而不是双年展式的张扬。

系统"单一文字色、单一强调"的纪律能干净地迁移到 CJK：纸上的墨、sun-bloom 氛围、细线、无阴影，都不变。micro-label 处理（Archivo 字重 600、大写、0.16–0.32em 字距）是汉化时最脆的一环：CJK micro-label 会同时丢掉大写信号和宽字距。补偿办法是把中文 micro-label 设成思源黑体字重 600、0 字距，并用**略重的字重反差**（正文降到思源宋体 400，标签保持思源黑体 600），并且**始终在标签下方配一条 hairline-soft 线**：由这条线承担拉丁里宽字距大写所做的外壳识别工作。

### 已知 CJK 缺口

- **没有可 CDN 加载的中文等宽字面给表格数据。** JetBrains Mono 在这里的角色（日历账目日期、图表年份/数值标签、页码）依赖等宽数字节奏，而 CJK 不提供。思源黑体字重 500 配 `font-feature-settings: "tnum"` 能给出表格化的拉丁数字，但汉字仍是比例宽度。对于以对齐为结构前提的账目行，把日期列与数值列保留为拉丁数字（阿拉伯数字 + 拉丁日期缩写），思源黑体只用于标题/地点单元格。
- **Instrument Serif 斜体没有直接的中文对应。** 斜体展示 token（宣言级引文正文）到了 CJK 会彻底失去慢读性格。改用思源宋体 400，行高放宽到 1.4，字号略大作为补偿；可考虑用「」引号框住来提示"这是引文段落"。
- **得意黑在受限网络上可能加载不到。** cn-fontsource CDN 在中国大陆可靠，国际上的表现尚未充分验证。字体栈里始终带上 `'Noto Serif SC', serif` 作回退，这样即便得意黑失败，展示标题仍保持编辑感。

## 迭代指南

1. 任何新表面都从 `{colors.paper}` 起，至少放一枚 `{components.sun-bloom}` 作氛围，并把常驻 `{components.pagenum}` 钉在右下角。
2. 任何新标题都用 Instrument Serif 字重 400、紧行高、负字距。主瞬间取 `{typography.headline}`，封面级才用 `{typography.display}`。
3. 任何新正文段落都用 Archivo 字重 400、行高 1.5。标题后的导语用略大的 `{typography.body-lede}` 留出呼吸。
4. 任何新眉题或分节标签都用 micro-label 处理：Archivo 字重 600、大写、0.16-0.32em 字距、墨色、无填充。不要拿胶囊或小片顶替。
5. 任何新结构分隔都是 1px 的 `{components.hairline-rule}` 墨色，次级列表行用它的柔和变体。绝不取更粗的边框。
6. 任何新数字或元数据内容（日期、页码、图表数值、账目数字）都用 JetBrains Mono。衬线数字只留给展示瞬间。
7. 任何新"海报级"色彩表态都用 `{components.yellow-panel}`：画布的一列或一部分满铺 `{colors.sun}`，其上压墨色文字。
8. 任何新的有序节目列表都用 `{components.strand-row}` 模式：衬线数字单元格 + 衬线标题 + 无衬线正文，用 hairline-soft 线分隔。
9. 任何新表格化行程都用 `{components.ledger-row}` 模式：等宽日期 + 衬线标题 + 无衬线地点 + 等宽时长右对齐，用 hairline-soft 线分隔。
10. 表面若显得平，在 sun-bloom 对角加一枚 `{components.ember-bloom}`——绝不要加卡片边框或阴影。

## 已知缺口

- **Instrument Serif、Archivo 与 JetBrains Mono 都通过 preconnect + `<link>` 从 Google Fonts 加载**。虽然定义了回退（`Georgia`、`Helvetica Neue`、`ui-monospace`），但渲染差别很大；在 Google Fonts 失效的环境里，系统会塌成通用编辑默认值，失去身份。
- **Instrument Serif 斜体轴已加载**，却只用于宣言级引文处理。其他斜体时刻（例如正文段落里的 `<em>`）在风格上不会与专用斜体展示传递同样的信号。
- **系统没有图表引擎**：数据页在条 div 上用内联 `style="width: XX%"`。做动态图表需要在 JS 里算宽度或在服务端模板化标记。
- **block-tile 底纹用硬编码的网格位置**（每块 `grid-column: 1 / 3; grid-row: 6 / 9;`）。拼块是装饰，位置按表面逐处调过，没有参数化的拼块排布系统。
- **竖排 rail-label 用旋转 transform**，某些浏览器上可能产生细微的亚像素渲染瑕疵。标签是装饰性的，渲染看着不对可以安全去掉。
- **幻灯片导航除页码外没有任何页指示器**。没有点轨、没有进度条、没有缩略图条。页码文字是唯一的位置提示。
- **交叉淡入过渡只用于屏幕**，不会退化成合理的打印/静态状态。导出 PDF 需要逐表面手动截图。
- **封面与版权页的 footer-band 列用分数宽度**（`1.1fr 1fr 1.4fr 2fr` 与 `1.2fr 1.1fr 1fr 1.4fr`）。这些比例按演示内容调过，若页脚单元格文字长度差异很大，可能需要重调。
- **系统为 Instrument Serif 加载了 Google Fonts 的 `ital` 轴**，但 Archivo 与 JetBrains Mono 只加载了 `wght` 轴。要加斜体正文或斜体等宽时刻，得改字体加载请求。
