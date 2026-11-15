---
version: alpha
name: Emerald Editorial
description: "A bold display-serif editorial system in the register of a fashion masthead or vintage magazine cover. Bodoni Moda runs at weight 900 across a wide scale (44–460px), set against a saturated emerald-green canvas with deep navy ink and oat-paper accents. The signature treatment is a stacked double-rule ornament that brackets centered display words like a 19th-century theatrical playbill. The aesthetic borrows from Harper's Bazaar / Vogue / Wallpaper covers: confident, theatrical, paper-and-ink committed, with a tight three-color palette and zero gradients or shadows."

colors:
  bg: "#3CD896"
  bg-2: "#2DC684"
  bg-3: "#25B377"
  ink: "#0F1A5C"
  ink-2: "#1B2774"
  ink-3: "#3A4593"
  paper: "#F1E9D6"
  rule: "rgba(15, 26, 92, 0.22)"
  rule-strong: "rgba(15, 26, 92, 0.85)"

typography:
  numeral-jumbo:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 460
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.04em
  display-section:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 200
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.015em
  display-cover:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 184
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: -0.01em
  display:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 130
    fontWeight: 900
    lineHeight: 0.96
    letterSpacing: -0.015em
  display-md:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 128
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -0.015em
  display-sm:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 120
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -0.015em
  headline-xl:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 104
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -0.015em
  headline:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 92
    fontWeight: 900
    lineHeight: 1
    letterSpacing: -0.02em
  ornament-word-lg:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 84
    fontWeight: 800
    lineHeight: 1
  ornament-word:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 76
    fontWeight: 800
    lineHeight: 1
  ornament-word-sm:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 68
    fontWeight: 800
    lineHeight: 1
  title-card-lg:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 64
    fontWeight: 800
    lineHeight: 1
    letterSpacing: -0.005em
  title-card:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 48
    fontWeight: 800
    lineHeight: 1
    letterSpacing: -0.005em
  title-card-sm:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 44
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -0.005em
  step-numeral:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 80
    fontWeight: 900
    lineHeight: 1
  step-title:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 40
    fontWeight: 800
    lineHeight: 1
    letterSpacing: -0.005em
  kpi-figure:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 144
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.03em
  kpi-figure-unit:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 60
    fontWeight: 800
  stat-figure:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 92
    fontWeight: 900
    lineHeight: 1
    letterSpacing: -0.02em
  stat-figure-unit:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 48
    fontWeight: 900
  eyebrow:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 28
    fontWeight: 800
    letterSpacing: 0.18em
    textTransform: uppercase
  label:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 26
    fontWeight: 700
    letterSpacing: 0.08em
    textTransform: uppercase
  label-tight:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 26
    fontWeight: 700
    letterSpacing: 0.05em
    textTransform: uppercase
  tag:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 24
    fontWeight: 800
    letterSpacing: 0.12em
    textTransform: uppercase
  caption:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 24
    fontWeight: 700
    letterSpacing: 0.1em
    textTransform: uppercase
  body-lg:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 28
    fontWeight: 500
    lineHeight: 1.5
  body:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 26
    fontWeight: 500
    lineHeight: 1.5
  body-sm:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 24
    fontWeight: 500
    lineHeight: 1.45
  credit:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 28
    fontWeight: 700
    letterSpacing: 0.18em
    textTransform: uppercase

spacing:
  pad-default: "110px 110px 70px"
  pad-cover: "56px 110px"
  pad-closing: "80px 110px"
  pad-statement: "110px 110px 70px"
  masthead-inset: "56px 80px"
  rule-thick: "4px"
  rule-thicker: "5px"
  rule-thin: "2px"

canvas:
  width: 1920px
  height: 1080px

components:
  ornament-double-rule:
    description: "The system's signature treatment. A centered serif word framed by two stacked 4px horizontal rules on each side. The rules sit 3px apart on top and 3px apart on bottom, giving a 19th-century playbill / theatrical-poster bracket effect. Configurable via :root[data-ornament] to switch between double (default), single, or none."
    ruleHeight: "4px"
    ruleGap: "3px"
    wordWeight: 800
    wordFamily: "'Bodoni Moda', serif"
  ornament-vertical:
    description: "An inline horizontal pair of stacked rules (each 4px tall, 8px apart) on either side of a small serif word. Used as a side bracket around connector words like prepositions."
    ruleHeight: "4px"
    ruleGap: "8px"
    barWidth: "64px"
  masthead:
    position: "absolute"
    placement: "top: 56px, full-width between 80px side padding"
    layout: "flex space-between"
    typography: "{typography.label-tight}"
    color: "{colors.ink}"
  footline:
    position: "absolute"
    placement: "bottom: 56px, full-width between 80px side padding"
    layout: "flex space-between"
    typography: "{typography.label-tight}"
    color: "{colors.ink}"
  rule-h-thick:
    height: "4px"
    background: "{colors.ink}"
    description: "Universal 4px horizontal rule used as section separator and tile/row border. The system's standard rule weight."
  agenda-row:
    description: "A three-column grid row (130px / 1fr / 320px) with 4px ink top borders. Holds a serif ordinal, serif name, and sans-serif kind label. The last row in a list also carries a 4px bottom border, sealing the list."
    rowPad: "26px 0"
    topBorder: "4px solid {colors.ink}"
  inverse-tile:
    description: "A solid {colors.ink} rectangle holding {colors.bg} text. Used for chart-card containers, kpi tiles, process steps, section-opener panels. Carries no corner radius and no shadow."
    background: "{colors.ink}"
    color: "{colors.bg}"
    padding: "32px to 36px"
  paper-tile:
    description: "A solid {colors.paper} rectangle holding {colors.ink} text. The alt variant of inverse-tile — used in rotation across a row of process steps or kpi tiles to break the monotony of ink fills."
    background: "{colors.paper}"
    color: "{colors.ink}"
  mark-pill:
    background: "{colors.ink}"
    color: "{colors.bg}"
    padding: "10px 22px"
    fontWeight: 700
    letterSpacing: 0.1em
    fontSize: 24
    textTransform: uppercase
    description: "A small ink-on-bg pill used as a category mark or section tag. No border-radius — strict rectangle."
  tag-pill:
    background: "{colors.ink}"
    color: "{colors.bg}"
    padding: "8px 20px"
    fontWeight: 700
    letterSpacing: 0.12em
    fontSize: 24
    textTransform: uppercase
  delta-pill:
    background: "{colors.bg}"
    color: "{colors.ink}"
    padding: "6px 16px"
    fontWeight: 800
    letterSpacing: 0.08em
    fontSize: 24
    textTransform: uppercase
    description: "A small bg-on-ink delta indicator placed inside an inverse kpi tile to show change direction. Inverted to ink-on-bg when inside a paper-tile."
  bar:
    description: "A vertical rectangular chart bar in bg (primary), paper (alt). Value label printed above bar in Bodoni 30px. No corner radius."
    background: "{colors.bg} or {colors.paper}"
  chart-card:
    background: "{colors.ink}"
    color: "{colors.bg}"
    padding: "36px 50px 30px"
    gridLineColor: "rgba(60, 216, 150, 0.22)"
    description: "An ink container framing a bar chart on bg. Y-axis labels are Bodoni 26px on the left; x-axis labels are Manrope 24px. Grid lines are 2px at 22% bg-on-ink."
  ornament-numeral-panel:
    description: "A full-bleed inverse panel (ink background) holding a single oversized Bodoni numeral (~460px weight 900) centered. Used as a section-opener device. Topbar / footline strings sit absolutely positioned in the panel corners."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/emerald-editorial/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Emerald Editorial 是一套**大胆的展示衬线编辑系统**，扎根于时尚杂志与 19 世纪戏剧演出单的视觉语言。底层前提是单一排印字面 **Bodoni Moda 字重 900**，以毫不歉疚的尺度使用：常规标题 92px，陈述与分节开场 130–200px，英雄数字 460px。衬线响亮、戏剧化、自信。每页以文字领衔，不以图像领衔。

配色是紧凑的三色编辑组：**饱和翡翠绿**（`{colors.bg}` — #3CD896）作主导表面，**深海军墨**（`{colors.ink}` — #0F1A5C）既作主文字色也作反色面板表面，**燕麦纸**（`{colors.paper}` — #F1E9D6）作交替拼块的次级表面。海军 / 翡翠的对比是系统的色彩身份，每段文字不是海军压翡翠、就是翡翠压海军。token 系统里还有两组翡翠近重复色（`{colors.bg-2}`、`{colors.bg-3}`）和两组海军近重复色（`{colors.ink-2}`、`{colors.ink-3}`），但都被预留，已发布的页面几乎完全认准三种主色。

辅助字面是 **Manrope**，人文几何无衬线，正文段落跑字重 500，每个标签、小片、眉题、图注、页脚线跑字重 700–800 的大写宽字距。Manrope 绝不跨进展示领地，它止步于 28px、待在外壳层。

招牌处理是**双线装饰**：一个居中的衬线词，两侧各由两条叠起的 4px 横线夹住，线与线间隔 3px。这个处理作封面核心，也作反复出现的陈述括号。读起来像 19 世纪演出单或老节目册，"The [word] of [word]" 式框定装置。双线装饰可经 `:root[data-ornament]` 属性配置成单线或无线变体，但双线变体才是系统身份。

纵深是**平的、墨基的**。没有投影、没有渐变、没有模糊、没有辉光。每个表面都是实翡翠、实海军或实纸。抬升靠色块反色（翡翠画布上的海军拼块就是"抬起"的元素）和分隔分节的 4px 墨线发生。整套系统读起来像印在纸上的墨，不是数字界面。

**密度取向：中满、居中。** 多数页承载一个大尺度展示标题（92–200px）加 3–4 个辅助元素（统计行、kpi 网格、流程流、图表卡片）。110px 的幻灯片内边距留出呼吸，顶底的刊头/页脚外壳锚住页面。塞进六个小元素的页读起来像坏了，一个巨型标题加三张辅助拼块的页读起来才权威。宁可更少、更大。例外是议程列表模式（由 4px 墨线分隔的大编号行纵向列表）天然密集、纵向填满画布，用到时理应如此。

**关键特征：**
- Bodoni Moda 字重 900 用于每个展示瞬间，Manrope 字重 500/700/800 用于每个正文和标签瞬间。
- 饱和翡翠画布（`{colors.bg}`）配深海军墨（`{colors.ink}`）文字与反色面板。
- 带居中衬线词的双线装饰是招牌装饰装置。
- 4px 墨色横线分隔每个叠起的分节、每个列表行、每条图表边。4px 粗细是系统的默认线。
- 哪里都没有圆角，每个形状都是严格矩形，只有 logo/排印字形本身是圆的。
- 无阴影、无渐变、无模糊。纵深靠色块反色 + 4px 线。
- 展示字放得极开，英雄 / 分节开场 / 收尾瞬间 184–460px。
- Manrope 外壳（标签、小片、图注）始终大写、0.05em–0.18em 字距。

## 颜色

### 调色板
- **BG / Emerald**（`{colors.bg}` — #3CD896）：主导幻灯片画布。饱和、略冷的翡翠，饱和到像印出来的墨而非 CSS 预设。默认幻灯片背景。
- **BG-2**（`{colors.bg-2}` — #2DC684）：略深的翡翠，留给色调变化，token 系统里有但用得省。只在两块翡翠表面相邻、需要分开时取用。
- **BG-3**（`{colors.bg-3}` — #25B377）：最深的翡翠变体，同样预留。
- **Ink / Navy**（`{colors.ink}` — #0F1A5C）：深海军主色。翡翠与纸表面上的文字色，反色面板背景色，线色，边框色。系统的结构色。
- **Ink-2**（`{colors.ink-2}` — #1B2774）：略浅的海军变体，可供墨压墨情境里的色调反差，但很少用。
- **Ink-3**（`{colors.ink-3}` — #3A4593）：最浅的海军变体，预留。
- **Paper**（`{colors.paper}` — #F1E9D6）：燕麦奶油次级表面。用作流程 / kpi 行里的交替拼块填充、交替条形图系列，以及任何需要第三种"暖"表面来打破一整排海军反色拼块的地方。承载 `{colors.ink}` 文字。
- **Rule**（`{colors.rule}` — `rgba(15, 26, 92, 0.22)`）：半透明海军，只用于微妙的内部网格线（例如深底上的图表网格线）。不是结构线色。
- **Rule Strong**（`{colors.rule-strong}` — `rgba(15, 26, 92, 0.85)`）：85% 不透明度海军，可作近乎实线的替代。

### 默认值
- **默认幻灯片背景**：`{colors.bg}`（翡翠）。瞬间需要分量（分节开场、收尾）时取 `{colors.ink}`（海军）作整页表面。
- **翡翠上默认标题色**：`{colors.ink}`。
- **海军上默认标题色**：`{colors.bg}`，翡翠压海军是系统唯一给展示文字用的翻色。
- **翡翠上默认正文色**：`{colors.ink}`。
- **海军上默认正文色**：`{colors.bg}`。
- **纸上默认正文色**：`{colors.ink}`。
- **默认标签 / 眉题 / 小片色**：翡翠与纸表面 `{colors.ink}`，海军表面 `{colors.bg}`。
- **默认线色**：`{colors.ink}` 4px 实线，始终如此。
- **默认反色拼块填充**：`{colors.ink}` 配 `{colors.bg}` 文字。一行里的交替拼块用 `{colors.paper}` 配 `{colors.ink}` 文字。
- **墨拼块内默认 delta / 胶囊填充**：`{colors.bg}` 底配 `{colors.ink}` 文字。纸拼块内反成 `{colors.ink}` 底配 `{colors.bg}` 文字。

配色刻意收紧。引入第四色系（红、黄、橙、薰衣草）会击碎编辑承诺。守在翡翠 / 海军 / 纸里。bg-2/3 与 ink-2/3 变体供色调细微差别，但应极少需要。

## 排印

### 字族
系统从 Google Fonts 加载几款展示衬线字族（Bodoni Moda、Playfair Display、DM Serif Display、Rozha One、Yeseva One）加 Manrope 作辅助无衬线。**实际只有 Bodoni Moda 用于展示**，其余衬线字族加载了但休眠，预留作未来变体。Bodoni Moda 是规范展示字面，其余不属于系统声部。

Bodoni Moda 几乎只跑**字重 900**，最重的一档。字重 800 出现在小装饰词和拼块标题（略轻，免得与主标题相争）。字重 700 在小装饰介词上出现一两次。已发布系统里没有字重 500 的 Bodoni。900 字重的承诺，正是系统戏剧演出单声部的来源。

Manrope 承担其余一切：正文段落字重 500，标签 / 眉题 / 小片 / 图注字重 700 或 800 的大写、0.05em–0.18em 字距。Manrope 绝不出现在展示尺度，Bodoni 绝不出现在外壳尺度。

### 展示、正文、外壳比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.numeral-jumbo}` | 460px | Bodoni Moda | 900 | 反色分节开场面板上的英雄数字 |
| `{typography.display-section}` | 200px | Bodoni Moda | 900 | 议程 / 分节标题英雄 |
| `{typography.display-cover}` | 184px | Bodoni Moda | 900 | 封面刊头标题 |
| `{typography.display}` | 130px | Bodoni Moda | 900 | 陈述 / 拉页引文尺度 |
| `{typography.display-md}` | 128px | Bodoni Moda | 900 | KPI 行引导标题 |
| `{typography.display-sm}` | 120px | Bodoni Moda | 900 | 流程流引导标题 |
| `{typography.headline-xl}` | 104px | Bodoni Moda | 900 | 图表 / 数据引导标题 |
| `{typography.headline}` | 92px | Bodoni Moda | 900 | 常规页面标题 |
| `{typography.ornament-word-lg}` | 84px | Bodoni Moda | 800 | 大装饰括号词（陈述变体） |
| `{typography.ornament-word}` | 76px | Bodoni Moda | 800 | 标准装饰括号词（封面变体） |
| `{typography.ornament-word-sm}` | 68px | Bodoni Moda | 800 | 双线括号之间的封面介词 |
| `{typography.kpi-figure}` | 144px | Bodoni Moda | 900 | KPI 拼块数字 |
| `{typography.kpi-figure-unit}` | 60px | Bodoni Moda | 800 | KPI 数字的单位后缀 |
| `{typography.stat-figure}` | 92px | Bodoni Moda | 900 | 次级统计数字（在侧面板里） |
| `{typography.stat-figure-unit}` | 48px | Bodoni Moda | 900 | 次级统计数字的单位后缀 |
| `{typography.title-card-lg}` | 64px | Bodoni Moda | 800 | 大卡片 / 议程行名称内标题 |
| `{typography.title-card}` | 48px | Bodoni Moda | 800 | 图表卡片结论标题 |
| `{typography.title-card-sm}` | 44px | Bodoni Moda | 800 | 陈述辅助单元格标题 |
| `{typography.step-numeral}` | 80px | Bodoni Moda | 900 | 流程步骤序数 |
| `{typography.step-title}` | 40px | Bodoni Moda | 800 | 流程步骤标题（坐在顶线下） |
| `{typography.body-lg}` | 28px | Manrope | 500 | 导语 / 副标题段落 |
| `{typography.body}` | 26px | Manrope | 500 | 标准正文段落 |
| `{typography.body-sm}` | 24px | Manrope | 500 | 拼块 / 图表侧面板内紧凑正文 |
| `{typography.eyebrow}` | 28px | Manrope | 800 / 0.18em | 标题上方的分节眉题 |
| `{typography.label}` | 26px | Manrope | 700 / 0.08em | 刊头 / 页脚线标签 |
| `{typography.label-tight}` | 26px | Manrope | 700 / 0.05em | 封面顶/底串 |
| `{typography.tag}` | 24px | Manrope | 800 / 0.12em | 反色胶囊 / 小片（标记、delta、侧小片） |
| `{typography.caption}` | 24px | Manrope | 700 / 0.1em | 议程行类型标签、图表 x 轴、kpi 标签 |
| `{typography.credit}` | 28px | Manrope | 700 / 0.18em | 作者 / 机构致谢行 |

### 默认值
- **常规页面标题默认尺寸**：`{typography.headline}`（92px）。
- **英雄 / 封面级瞬间默认尺寸**：`{typography.display-cover}`（184px）或 `{typography.display-section}`（200px）。
- **正文段落默认尺寸**：`{typography.body}`（26px），Manrope 字重 500。
- **拼块内正文段落默认尺寸**：`{typography.body-sm}`（24px）。
- **标题上方眉题默认尺寸**：`{typography.eyebrow}`（28px），Manrope 800 大写 0.18em。
- **小片 / 胶囊 / 芯片默认尺寸**：`{typography.tag}`（24px），Manrope 800 大写 0.12em。
- **KPI 数字默认尺寸**：`{typography.kpi-figure}`（144px），可选 60px 单位。
- **任何 Bodoni 展示瞬间默认字重**：900。800 变体留给装饰词和拼块标题，绝不用于主标题。
- **任何 Manrope 正文行默认字重**：500。

拿不准时，页面主标题取 `{typography.headline}`（92px）。120–200px 一档留给分节开场、陈述、KPI 行标题，拿它排常规标题会把层级压平。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个主 Bodoni 标题都跑字重 900、负字距（-0.01em 到 -0.03em）、紧行高（0.9–0.95）。** 字重 700 或 800 的 Bodoni 标题读成副标题，不是主瞬间。
- **每个 Manrope 标签、眉题、小片、图注、页脚线、致谢元素都大写、至少 0.05em 字距。** 句首大写或默认字距的 Manrope 读成网页应用正文，不像编辑外壳。
- **双线装饰一旦使用就是双边的，居中词两侧都有线。** 单边装饰会破掉括号对称。装饰可经 `:root[data-ornament]` 降成单线或无线变体，但默认且推荐的是双线。
- **每个分节分隔与拼块分隔线都是 4px 实线 `{colors.ink}` 线。** 绝不 1px、绝不 2px、绝不墨色以外上色。4px 粗细是系统的结构节奏。
- **反色拼块永远带 `{colors.ink}` 底配 `{colors.bg}` 文字。** 交替纸拼块带 `{colors.paper}` 底配 `{colors.ink}` 文字。这对搭配之外的颜色组合会破掉系统的印刷墨纪律。
- **巨型尺度（200px+）的 Bodoni 数字活在反色海军面板上。** 把 460px 数字放在翡翠画布上技术上可行，但视觉上会破掉面板锚定的演出单声部，巨型数字属于墨面板内部。

### 排印原则
字重 900 + 负字距 + 紧行距的组合是系统的展示声部，换掉三者中任一属性（例如字重 700、默认字距、1.2 行距）都会读成另一套设计系统。衬线/无衬线角色切分严格：Bodoni 绝不出现在正文 / 标签尺度，Manrope 绝不出现在展示尺度。

Bodoni 字体请求里加载了斜体，但已发布系统不用，除非刻意引入新模式，否则挡在外面。不用下划线。强调靠尺寸、颜色反色、装饰传达。

## 布局

### 画布系统
系统以固定 **1920×1080** 画布为目标。幻灯片是精确宽高的 `<section class="slide">` 元素。渲染依赖 `deck-stage.js` 缩放画布适配视口。画布是纸料，不是视口，为投影、打印或 16:9 的 PDF 导出而设计。

### 内边距比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-default}` | 110px 110px 70px | 标准内容页（不对称，底部略少留给页脚线） |
| `{spacing.pad-cover}` | 56px 110px | 封面页（顶部内边距少些，给刊头留位） |
| `{spacing.pad-closing}` | 80px 110px | 收尾页 |
| `{spacing.masthead-inset}` | 顶部 56px、左右 80px | 封面与收尾的刊头 / 页脚线绝对内缩 |

### 外壳解剖
封面与收尾顶部带**刊头**（两条 Manrope 标签串分列两侧的 flex 行），底部带**页脚线**（对应的一行）。内容页通常跳过刊头与页脚线，靠 110px 顶部内边距给标题空间。用刊头时，它位于 `top: 56px, left/right: 80px`。

### 卡片与拼块处理
系统**哪里都没有 border-radius**。卡片、拼块、kpi 面板、装饰线、标记胶囊、小片胶囊全是严格矩形。唯一的圆是 Bodoni 字形本身的自然曲线。视觉节奏完全来自矩形构图与 4px 墨线。

### 线粗细
| 粗细 | 用途 |
|---|---|
| 2px | 图表网格线（微妙、半透明） |
| 4px | 通用结构线，分节分隔、列表行边、拼块顶线 |
| 5px | 封面装饰线（略重，好在 184px 展示标题旁压得住） |
| 18px 高（顶 4px 线 + 底 4px 线） | 双线装饰跨度 |

4px 粗细是系统默认，除非瞬间明确需要封面更重的 5px 线。

## 纵深与层级

### 平、无阴影
系统**零阴影**。没有 box-shadow、没有 text-shadow、没有 filter 模糊、没有渐变。抬升完全靠：
1. **色块反色**：翡翠画布上的海军拼块是系统"抬起"的元素。反色就是纵深语言。
2. **4px 墨线**：分节由 4px 实线海军线分隔，读起来像区域之间的纸折痕。
3. **无 border-radius 的实面板**：严格矩形处理配全反色填充，给拼块带来印刷墨块的分量。

没有柔辉光、没有玻璃、没有新拟态。加 box-shadow 会击碎印刷墨纪律。

### 分节开场面板
一个招牌抬升装置：页面可切成满出血双栏网格，左侧是实 `{colors.ink}` 面板、装一个巨型 Bodoni 数字（`{typography.numeral-jumbo}` 460px），右侧是标准翡翠画布、装标题 + 导语 + 类别标记。面板读起来像杂志扉页开场，厚重、锚定、有仪式感。把这当开场模式，不是常规页面布局。

## 形状与处理

### 圆角
**零。** 每个形状都是严格矩形。胶囊、小片、拼块、面板、条、刊头、页脚线、装饰词全是方角。

### 边框 / 线样式
- **4px 实线 `{colors.ink}`**：通用结构线。分节分隔、列表行边、拼块内部线。
- **5px 实线 `{colors.ink}`**：封面装饰略重的线。
- **4px 实线 `currentColor`**：用于拼块内线应跟随拼块文字色的场合（例如纸拼块的内部线是 `{colors.ink}`，墨拼块的内部线是 `{colors.bg}`）。

线从不用虚线、从不用点线、从不上墨 / currentColor 模式以外的颜色。

### 装饰元素类型

**双线装饰**（`{components.ornament-double-rule}`）：系统签名。一个居中的衬线词，两侧各由两条叠起的 4px 横线夹住（间隔 3px）。用于封面（"The [word] of [word]" 框定）、陈述页（围住小连接词），以及任何排印瞬间需要戏剧括号的地方。可经 `:root[data-ornament]` 配成单线或无线。

**竖向侧括号**（`{components.ornament-vertical}`）：较小的行内变体，一个小衬线介词左侧一对叠起的 4px 线、右侧一对对应的线。用于句中而非居中跨度。

**刊头 / 页脚线**（`{components.masthead}`、`{components.footline}`）：封面与收尾页顶/底绝对定位的 flex 行。两条 Manrope 大写串分列两侧（例如出版物名 + 日期、分节 + 页码）。确立杂志页身份。

**反色拼块**（`{components.inverse-tile}`）：实 `{colors.ink}` 矩形，装 `{colors.bg}` 文字。用作图表卡片容器、kpi 拼块、流程步骤、侧面板。无 border-radius、无阴影。

**纸拼块**（`{components.paper-tile}`）：交替变体，实 `{colors.paper}` 配 `{colors.ink}` 文字。用于在一排反色拼块里轮转打破单调（例如四步流程流交替墨 → 纸 → 墨 → 纸）。

**标记胶囊**（`{components.mark-pill}`）：小的墨压翡翠胶囊，作分节开场底部空白里的类别标记或分节小片。严格矩形。

**小片胶囊**（`{components.tag-pill}`）：略小的胶囊变体，用于图表侧与 kpi 拼块内标记结论或统计类型。

**Delta 胶囊**（`{components.delta-pill}`）：翡翠压墨（或在纸拼块内反成墨压翡翠）的芯片，显示方向变化指示（例如 "↑ 12% YoY"）。位于 kpi 拼块角上。

**议程行**（`{components.agenda-row}`）：三列网格行，上下由 4px 墨线分隔。左列衬线序数、中列衬线名称、右列 Manrope 类型标签。叠起的议程行构成系统的目录模式。

**图表卡片**（`{components.chart-card}`）：海军反色面板，装翡翠 + 纸条的条形图。Y 轴标签 Bodoni，x 轴标签 Manrope。网格线 2px、22% 不透明度翡翠压海军。面板读起来像杂志数据跨页。

**装饰数字面板**（`{components.ornament-numeral-panel}`）：满出血反色半页，装单个 460px 的 Bodoni 数字。顶栏 / 页脚线串坐在角落。只作分节开场装置。

## 该做与不该做

### 该做
- 每个 Bodoni 展示标题都跑字重 900、负字距（-0.01em 到 -0.03em）、紧行高（0.9–0.95）。这个组合就是系统的声部。
- 每个 Manrope 标签 / 眉题 / 小片 / 图注 / 页脚线都大写、至少 0.05em 字距。句首大写的 Manrope 会丢掉编辑语域。
- 把默认幻灯片背景设成 `{colors.bg}`（翡翠）。只有分节开场与收尾瞬间才取 `{colors.ink}` 作整页表面。
- 每个分节分隔、列表边、拼块分隔线都用 4px 实线 `{colors.ink}` 线。4px 粗细是系统的结构节奏。
- 排印瞬间需要戏剧框定时取双线装饰，尤其围住两个展示标题之间的小连接词（"of"、"in"、"for"）。
- 反色拼块（`{colors.ink}` 底配 `{colors.bg}` 文字）作默认抬升元素。在一排里轮入纸拼块打破全反色填充。
- 展示字放得极开，英雄、分节开场、陈述瞬间 130–460px。系统奖励尺度。
- 把墨压翡翠与翡翠压墨配对作颜色翻转。没有明确语义理由，别引入第三种颜色翻转（纸压墨、墨压纸）。
- 每个形状保持严格矩形。零半径承诺与双线装饰并列，是系统签名。

### 不该做
- 不要给任何元素加 box-shadow、text-shadow、渐变或模糊。系统只有平的印刷墨。
- 不要引入 Bodoni Moda 与 Manrope 之外的第三款字体。Google Fonts 请求里其余衬线字族（Playfair、DM Serif、Rozha、Yeseva）加载了但不属于已发布声部，加入它们会击碎 Bodoni 承诺。
- 不要把 Bodoni 跑在字重 500 或更轻。系统认准 900（默认）、800（装饰词、拼块标题）、700（仅小介词）。
- 不要把 Manrope 渲染成句首大写或无字距。Manrope 始终是大写外壳。
- 不要引入第四色系。翡翠 / 海军 / 纸三元组就是整个配色。
- 不要给任何元素用 border-radius。零半径是系统签名。
- 不要用 1px 或 2px 结构线。4px 粗细是结构默认，2px 只留给微妙的图表网格线。
- 不要把 460px 数字放在翡翠画布上而没有墨面板锚定。巨型数字活在反色海军面板上。
- 不要用六个小元素塞满一页。一个展示标题 + 3–4 张辅助拼块是节奏，更多元素需要更小尺度，会破掉编辑语域。
- 不要省掉封面与收尾页的刊头 / 页脚线。正是外壳让它们读作杂志扉页。

## 响应式行为

这是一套**固定 1920×1080 演示系统**，经 `deck-stage.js` 渲染。画布不是 CSS 意义上的响应式，没有媒体查询、没有断点、没有流式尺寸。每处尺寸都是 1920×1080 下的固定像素。

### 缩放行为
`deck-stage.js` 包裹每个 `<section class="slide">`，把 1920×1080 画布等比缩放适配浏览器视口，按需留黑边。文字、内边距、间隙、线粗细全是固定像素，随画布等比缩放。

### 放映行为
导航委托给 `deck-stage.js`。每个 `<section class="slide">` 是一帧，运行时处理过渡。

### 打印 / 导出
1920×1080 画布内的固定像素尺寸能干净地以 16:9 导出 PDF。Bodoni Moda 在打印分辨率下渲染良好，因为厚展示字重即便放到很大物理尺寸也压得住页面。

### 装饰变体开关
`:root[data-ornament]` 属性控制全局装饰风格：`"double"`（默认，两条叠起线）、`"single"`（一条居中线）、`"none"`（无线，词独自漂浮）。这是每套文稿的呈现层决策，不是逐页决策。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 中文字面 | 字重 | 理由 |
|---|---|---|---|
| 展示标题（92–460px） | 霞鹜文楷 LXGW WenKai（思源宋体 Noto Serif SC 900 回退） | 400 / 900 | LXGW WenKai 的手写暖意是最接近 Bodoni Moda 戏剧演出单声部的中文类比，思源宋体字重 900 在巨型尺寸承载结构分量 |
| 统计 / KPI 数字（144px+） | 思源宋体 Noto Serif SC | 900 | 明朝体字重 900 提供 Bodoni Moda 在 900 达到的印刷墨分量 |
| 正文段落（24–28px） | 思源宋体 Noto Serif SC | 400 | 温暖杂志跨页阅读的明朝正文声部 |
| 眉题 / 标签 / 小片（24–28px） | 思源黑体 Noto Sans SC | 700–800 | 替换 Manrope 作外壳层中文，几何人文质感 |
| 拼块标记 / 胶囊 / 图注 | 思源黑体 Noto Sans SC | 700 | 为反色胶囊与小片维持大写宽字距外壳感 |

### 混排策略

用**策略 C**：保留 Bodoni Moda 作拉丁展示字面，让 CJK 字形回退到 LXGW WenKai（展示）或 Noto Serif SC（正文）。Bodoni Moda 字重 900 的承诺是 Emerald Editorial 的整个品牌身份，整体换成 CJK 字族会破掉定义整套文稿的时尚杂志 / 19 世纪演出单语域。栈：

```css
/* Bodoni Moda roles (every display moment) */
font-family: 'Bodoni Moda', 'LXGW WenKai TC', 'Noto Serif SC', Georgia, serif;
/* Manrope roles (every chrome / body moment) */
font-family: 'Manrope', 'Noto Sans SC', system-ui, sans-serif;
```

逐字形回退策略让拉丁词渲染成 Bodoni 900（带着给系统声部的戏剧压缩），汉字渲染成 LXGW WenKai 或 Noto Serif SC。巨型尺寸（200–460px）的基线错位是最大留意点，Bodoni Moda 用 -0.03em 字距视觉上比 LXGW WenKai 更密，于是像 `第 3 期` 这样的混排数字面板可能晃动。带巨型数字的分节开场面板，优先用全数字（Bodoni）或全中文（LXGW WenKai）行。

### 加载

在既有 Google Fonts `<link>` 里追加（或作为第二条 link 标签）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=LXGW+WenKai+TC&family=Noto+Serif+SC:wght@400;700;900&family=Noto+Sans+SC:wght@500;700;800&display=swap" rel="stylesheet">
```

LXGW WenKai TC 是 Google Fonts 上的版本（同时带繁体和简体字形）。

### 通用 CJK 调整

以下调整适用于本系统**每一个 CJK 块**，无论尺寸或角色：

- **行高放宽 0.05–0.08。** CJK 字形是全宽方块，视觉分量比拉丁字形重，为拉丁调的行高（展示 0.9–0.95、正文 1.45–1.5）在中文里读起来局促。展示放到 1.0–1.1，正文放到 1.55–1.65。
- **去掉 CJK 标题的负字距。** Bodoni Moda 展示用 -0.01em 到 -0.03em 字距，会撞在一起。CJK 段设 `letter-spacing: 0`，标题看着挤时可用微小的正 `0.02em`。
- **绝不对 CJK 文字用 `text-transform: uppercase`。** 中文没有大小写，CSS 属性对汉字无效，却会悄悄破坏混排行里本该大写的 Manrope 部分。（这里尤其要紧，每个 Manrope 标签、眉题、小片、图注都用 `text-transform: uppercase`。）
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不用拉丁对应物（`,.:;!?""''()`）。同一句里混用标点系统读起来是排印错误。
- **CJK 标题末尾不加句号（。）。** 中文标题与拉丁遵循同一规则，标题式行去掉末尾标点。正文段落保留 。
- **在 CJK 与拉丁串交界处套用盘古之白。** 汉字与相邻拉丁词或数字之间应有一个空格（或 0.25em 外边距），例如 `2026 年 5 月` 而非 `2026年5月`。要么手打空格，要么用 `pangu.js` 式自动加空格器。
- **一句一款字体。** 不要在同一句里切换 LXGW WenKai 与 Noto Serif SC，挑与尺寸档匹配的字面（展示 = LXGW WenKai，正文 = Noto Serif SC），整段从一而终。

### 本系统的美学提示

Emerald Editorial 的整个声部是"时尚刊头 / 19 世纪戏剧演出单"，Bodoni Moda 字重 900 以极端尺度呈现，双线装饰夹住居中词。这种戏剧厚重感的中文对应是：大展示尺寸用 **LXGW WenKai**（笔意暖意复刻 Bodoni 的手工排性格），巨型数字用**思源宋体字重 900**（纯分量比暖意更要紧）。展示别用思源黑体，几何怪诞体会把演出单声部压平成"现代企业"。

双线装饰在中文里成立，把单个汉字（例如「春」）夹在 4px 叠起线之间，让 LXGW WenKai 的暖意撑起戏剧括号。封面的 "The X of Y" 约定，中文自然读作 `「X」之「Y」` 或 `X 与 Y`，小介词槽里用连接介词（之 / 与 / 的）替换拉丁 "of"。连接词用 LXGW WenKai 字重 400（匹配拉丁的 ornament-word-sm 角色）。

Manrope 作为外壳层（大写 + 0.08em–0.18em 字距）在中文里落到**思源黑体 Noto Sans SC 字重 700–800 配 0.05em 正字距**。别假装大写，在 CJK 段去掉 `text-transform: uppercase`，让思源黑体的几何人文质感靠字重和字距独自撑起外壳感。

### 已知 CJK 缺口

系统对 Bodoni Moda 字重 900、460px（反色海军面板上的巨型数字）的承诺最难汉化，Google Fonts CDN 上没有中文字面能在该尺度提供 Bodoni 900 的光学厚重感。思源宋体字重 900 最接近，但汉字在 460px 的对比剖面视觉上比 Bodoni 数字更重，可能压过海军面板。中文巨型数字分节开场可考虑：（1）用中文数字字符（一二三四五六七八九十），视觉上比西方数字轻，或（2）把数字保留为 Bodoni（拉丁），让面板下方的标签承载中文语境。本系统里纯中文巨型数字是最冒险的瞬间，值得逐页手动复核。

## 迭代指南

1. 任何新展示标题都是 Bodoni Moda 字重 900 配负字距、紧行距。从展示阶梯里挑尺寸（92 / 104 / 120 / 128 / 130 / 184 / 200），别自创尺寸。
2. 任何新外壳行（标签、眉题、小片、图注）都是 Manrope 字重 700 或 800 大写、0.05em–0.18em 字距。从外壳阶梯里挑尺寸（24 / 26 / 28）。
3. 任何新分节分隔或列表行边都是 4px 实线 `{colors.ink}` 线。不要 1px / 2px / 3px 结构线。
4. 任何新拼块都用反色填充模式（`{colors.ink}` 底配 `{colors.bg}` 文字）或纸填充模式（`{colors.paper}` 底配 `{colors.ink}` 文字）。在一排拼块里轮用两者。
5. 任何新胶囊 / 小片 / 芯片都是严格矩形（无 border-radius），取 `{components.tag-pill}` / `{components.delta-pill}` 的反色填充或翡翠填充颜色组合。
6. 任何新 KPI 数字都是 `{typography.kpi-figure}`（144px）配可选 `{typography.kpi-figure-unit}`（60px）后缀。系统里没有更小的 KPI 尺寸。
7. 任何新装饰瞬间默认用双线处理。只经 `:root[data-ornament]` 全局切到单线或无，不逐元素切。
8. 任何新分节开场用半出血反色面板 + 巨型数字模式。数字住在海军面板上，右半装眉题 + 标题 + 导语 + 标记。
9. 任何新色都必须来自 `{colors.bg}` / `{colors.ink}` / `{colors.paper}`（需要色调细微差别时可用预留的 bg-2/3 / ink-2/3 变体）。别引入黄、红或第三种强调。
10. 布局显得挤时放大展示标题，别加更多元素。系统奖励更大的字，不是更多零件。

## 已知缺口

- Google Fonts 请求加载 Bodoni Moda、Playfair Display、DM Serif Display、Rozha One、Yeseva One 和 Manrope。**实际只用了 Bodoni Moda 与 Manrope**，其余四款衬线字族休眠，加载了但 CSS 里未引用。它们可作替代展示声部，但必须显式接进去。
- 系统依赖 `deck-stage.js` 做画布缩放与幻灯片导航。脚本不在本 design.md 描述，视为运行时依赖。
- `:root[data-ornament]` 开关（`double` / `single` / `none`）是全局呈现设置，不能逐页或逐装饰应用，切变体是全稿生效。
- ink-2 / ink-3 与 bg-2 / bg-3 颜色 token 已定义但已发布 CSS 里未活跃使用，预留作色调变化，当前休眠。
- 条形图用手设条高（CSS `%`），没有数据绑定层，扩展图表要手算百分比。
- 离线渲染会把 Bodoni 回退到系统衬线（多半 Georgia）、Manrope 回退到系统无衬线（多半 SF/Segoe）。Bodoni 回退会大幅压平展示声部，离线 / 打印可靠性建议自托管。
- 92px Bodoni 标题在海军压翡翠、翡翠压海军下维持 WCAG AA 对比，但同配色对上更小文字（24–28px Manrope）接近对比下限。小字尽量放在海军压翡翠（对比更强的方向）。
- 刊头与页脚线串是源码里的硬编码占位（出版物名、日期、页码），每套文稿必须改。
- 系统没有 `@media print` 规则，也没有响应式断点，固定 1920×1080，任何视口适配都依赖 `deck-stage.js`。
