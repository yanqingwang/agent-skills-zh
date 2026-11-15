---
version: alpha
name: Broadside
description: A protest-poster editorial system built on massive Barlow type and a single fire-orange environment color. The aesthetic is "ink on fire" — dark slides for documentation, orange slides for declaration. Display type is enormous (13vw, roughly 187px at 1440 width) in weight 900 lowercase, treating words as graphic elements rather than reading copy. The cultural reference is broadside printing, SPACE10 reports, and Wim Crouwel grids reinterpreted with one loud color and zero decoration.

colors:
  ink-black: "#111111"
  ink-black-alt: "#1A1A18"
  fire-orange: "#E85D26"
  cream: "#F0ECE5"
  cream-muted: "#888880"
  cream-hint: "#505048"
  border-dark: "#282826"
  ink-on-orange-muted: "rgba(17, 17, 17, 0.75)"
  ink-on-orange-hint: "rgba(17, 17, 17, 0.55)"
  ink-on-orange-faint: "rgba(17, 17, 17, 0.40)"
  ink-on-orange-border: "rgba(17, 17, 17, 0.20)"

color-aliases:
  c-bg: ink-black
  c-bg-alt: ink-black-alt
  c-bg-light: ink-black            # Broadside collapses "light" → dark; there are no cream slides
  c-bg-orange: fire-orange
  c-fg: cream
  c-fg-2: cream-muted
  c-fg-3: cream-hint
  c-accent: fire-orange
  c-border: border-dark

typography:
  display:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "13vw"
    fontWeight: 900
    lineHeight: 0.88
    letterSpacing: -0.04em
  h1:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "7.5vw"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.03em
  h2:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "4.5vw"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  h3:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "2.8vw"
    fontWeight: 600
    lineHeight: 1.2
  lead:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "1.6vw"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "1.2vw"
    fontWeight: 400
    lineHeight: 1.6
  caption:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "0.9vw"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "IBM Plex Mono, monospace"
    fontSize: "0.72vw"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.14em
    textTransform: uppercase
  stat-value:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "5.5vw"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: -0.04em
  quote-mark:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "10vw"
    fontWeight: 900
    lineHeight: 0.6
  quote-text:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "3.8vw"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  fadelist-item:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "7.5vw"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: -0.03em
  fadelist-title:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "10.5vw"
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.04em

spacing:
  pad-x: "5.5vw"
  pad-y: "5.5vh"
  gap-lg: "3.5vh"
  gap-md: "2vh"
  gap-sm: "1vh"

canvas:
  width: 100vw
  height: 100vh

motion:
  ease-slide: "cubic-bezier(0.77, 0, 0.175, 1)"
  dur-slide: "0.8s"
  ease-enter: "cubic-bezier(0.16, 1, 0.3, 1)"
  dur-enter: "0.5s"

components:
  slide-chrome:
    layout: "flex row, justify space-between"
    paddingBottom: "{spacing.gap-sm}"
    borderBottom: "1px solid {colors.border-dark}"
    marginBottom: "{spacing.gap-md}"
    description: "Top chrome bar carrying section label on left, slide number/meta on right. Suppressed on cover, chapter, quote, and end slides."
  slide-foot:
    layout: "flex row, justify space-between"
    paddingTop: "{spacing.gap-sm}"
    borderTop: "1px solid {colors.border-dark}"
    marginTop: "{spacing.gap-md}"
    description: "Bottom chrome bar, mirrors top chrome. Same suppression rules."
  rule:
    width: 36px
    height: 2px
    background: "{colors.fire-orange}"
    description: "Stub accent rule. On orange slides this flips to {colors.ink-black}."
  rule-full:
    width: "100%"
    height: 2px
    background: "{colors.border-dark}"
  kicker:
    fontFamily: "{typography.label.fontFamily}"
    fontSize: "{typography.label.fontSize}"
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.fire-orange}"
    description: "Eyebrow above headlines. Orange on dark; dark-ink-at-55%-opacity on orange."
  tag:
    fontFamily: "{typography.label.fontFamily}"
    fontSize: "{typography.label.fontSize}"
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.fire-orange}"
    border: "1px solid {colors.fire-orange}"
    padding: "0.3em 0.8em"
    description: "Bordered mono tag. On orange slides flips to dark ink with 40%-opacity dark border."
  broadside-num:
    fontFamily: "IBM Plex Mono, monospace"
    fontSize: "1.1vw"
    fontWeight: 500
    letterSpacing: 0.1em
    color: "rgba(17, 17, 17, 0.45)"
    description: "Catalogue-style slide number, typically anchored top-left on orange slides. On dark slides, color shifts to {colors.cream-hint}."
  stat-card:
    borderTop: "1px solid {colors.border-dark}"
    padding: "{spacing.gap-md} {spacing.gap-md} {spacing.gap-md} 0"
    description: "Top-border-only data card. Big orange numeral above body label above mono note."
  bullet-marker:
    content: "/"
    color: "{colors.fire-orange}"
    fontFamily: "IBM Plex Mono, monospace"
    fontWeight: 700
    description: "Slash glyph rendered via ::before on every bullet item. Orange on dark, dark-at-45%-opacity on orange."
  compare-panel-left:
    paddingRight: "calc({spacing.pad-x} * 0.55)"
    borderRight: "1px solid {colors.border-dark}"
  compare-panel-right:
    paddingLeft: "calc({spacing.pad-x} * 0.55)"
  compare-panel-orange:
    background: "{colors.fire-orange}"
    description: "Right-half panel filled with fire orange — the 'after' or payoff side in compare layouts."
  bar-track:
    height: "30vh"
    borderLeft: "1px solid {colors.border-dark}"
    description: "Vertical bar chart container. Bars are cream-hint by default; one bar per chart gets the .accent class for fire orange."
  bar-fill:
    background: "{colors.cream-hint}"
  bar-fill-accent:
    background: "{colors.fire-orange}"
  img-placeholder:
    height: "55vh"
    background: "rgba(255, 255, 255, 0.04)"
    border: "1px dashed {colors.border-dark}"
    textTransform: uppercase
    letterSpacing: 0.12em
    description: "Dashed-border placeholder shown when no image is wired. Same 55vh footprint as a real img."
  fadelist-stack:
    description: "Vertical stack of three display-weight words, opacities 1.0 / 0.5 / 0.22 top-to-bottom. The SPACE10 'before/during/after' treatment."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/broadside/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Broadside 是一套**抗议海报式编辑系统**。定义性前提是：文字大到不再像文字，而开始像图形原语。展示尺寸取 `13vw`（`{typography.display}`），1440 宽的屏上单个词约 187px，宽到眼睛先扫字形、再读内容。这是系统主要的表情工具。

字面栈是铁板一块。**Barlow** 承担从 `{typography.display}` 到 `{typography.body}` 的每一个文字角色，没有衬线搭档、没有手书强调、没有次级展示字面。表情幅度全靠字重（400 到 900）与尺寸，不靠字面对比。**IBM Plex Mono** 是唯一次级字面，只出现在外壳里：页码、眉题、标签、小片、图注、项目列表的斜杠标记。**Noto Sans SC** 以匹配字重坐在每个 font-family 栈里作 CJK 回退。声部统一、厚重、小写，**Broadside 不用大写标题**。这是对粗野主义常态的有意反转。

配色分两种截然不同的语域。**深色语域**用近黑画布 `{colors.ink-black}` 配奶油文字 `{colors.cream}`，`{colors.fire-orange}` 作唯一强调，橙只用于强调（眉题、强调统计、项目标记、领先条）。**橙色语域**彻底翻转关系：`{colors.fire-orange}` 成为整页背景，同一深色 `#111111` 墨用来写标题和正文。没有浅/奶油页变体，源码里 `.light` 类被刻意别名到深色。封面与章节页默认橙色语域，内容页默认深色。

纵深是**平的**。没有投影、没有抬升 token、没有柔和表面。层级完全由字重、字号与 1px 细线分隔搭起。`slide-chrome` 与 `slide-foot` 的边、`stat-card` 的顶边、`compare-panel` 的分隔线，是系统仅有的纵深信号。一切落在同一平面。

**密度取向：低到中。** Broadside 为负空间而生。构图正确的一页，配一个巨大展示瞬间 + 1–2 行图注，别无他物。项目列表明确封顶三项，系统重冲击密度甚于信息密度。四栏正文互抢注意力的页，在这套系统里就是坏了；正确的密度是一句陈述、一条线、留白。封面、章节、引文页把这一点做到极致，彻底压掉外壳，让文字独自留在场里。

**关键特征：**
- 巨型 Barlow 展示字，字重 900、**小写**，展示元素绝不大写。
- 双色语域系统：深页配奶油字，或橙页配深墨字。没有奶油/白页。
- `{colors.fire-orange}` 既是强调（深页上）又是环境（橙页上），从不是次要色，永远是**那一色**。
- Barlow 单字面系统 + 只给外壳的 IBM Plex Mono。没有衬线、没有手书、没有第三字面。
- 1px 细线分隔（深页上 `{colors.border-dark}`；橙页上 `rgba(17,17,17,0.2)`）提供全部层级结构。
- 等宽眉题、等宽小片、等宽目录号，外壳声部始终是 IBM Plex Mono 大写。
- 项目列表用等宽 `/` 字形作标记，每列封顶三项。
- 平面：无阴影、无圆角表面、无渐变背景。
- `{spacing.pad-x}` 5.5vw + `{spacing.pad-y}` 5.5vh 造出宽裕画框，文字填满其余空间。

## 颜色

### 两种语域
Broadside 跑在二值表面上。每页要么**深色**（近黑背景、奶油文字、橙作唯一强调），要么**橙色**（火橙背景、深墨文字、深墨作柔化强调调）。没有奶油/纸语域，源码里 `.light` 类别名到深色。每页选一种语域并从一而终。

### 调色板
- **Ink Black**（`{colors.ink-black}` — #111111）：深色语域的主画布，也是橙页上的主文字色。比纯黑略柔，读起来仍是黑。系统通用的"墨"。
- **Ink Black Alt**（`{colors.ink-black-alt}` — #1A1A18）：深色语域的次级表面，某区域需要从基底画布上微微抬起、又不破平面时用它。
- **Fire Orange**（`{colors.fire-orange}` — #E85D26）：招牌色。深页上是强调：眉题、强调统计值、项目标记、图表里的领先条、橙色起始引号。橙页上是整个环境。饱和度高但色相偏暖而非电光，读起来是抗议海报，不是安全背心。
- **Cream**（`{colors.cream}` — #F0ECE5）：深页上的主文字色。暖米白，绝不纯白；这份暖意柔化深色画布，带出编辑语域。
- **Cream Muted**（`{colors.cream-muted}` — #888880）：深页上的次级文字，用于辅助正文、副标题、比较里被弱化的一半。
- **Cream Hint**（`{colors.cream-hint}` — #505048）：深页上的三级文字，用于图表轴标签、来源注、非等宽语境下的页码。
- **Border Dark**（`{colors.border-dark}` — #282826）：深页上的 1px 分隔色。在画布上几乎看不见，给结构又不抢眼。
- **橙上墨叠层**：深墨四档不透明度（75% / 55% / 40% / 20%），用于橙页上的正文、提示、标签、边框处理。这些是橙色语域里"柔化"的对应物。

### 默认值
- **内容页默认表面**：`{colors.ink-black}`（深色语域）。
- **封面、章节、陈述收尾、分节分隔页默认表面**：`{colors.fire-orange}`（橙色语域）。
- **深色表面上默认标题色**：`{colors.cream}`。
- **橙色表面上默认标题色**：`{colors.ink-black}`。
- **深色表面上默认正文色**：`{colors.cream}`。
- **橙色表面上默认正文色**：`rgba(17, 17, 17, 0.75)`。
- **深色表面上默认强调色**：`{colors.fire-orange}`，用于眉题、强调统计值、项目标记、图表领先条、起始引号。
- **橙色表面上默认强调色**：`{colors.ink-black}`，深墨自己成了对比爆点。
- **默认外壳边框色**：深页 `{colors.border-dark}`；橙页 `rgba(17, 17, 17, 0.2)`。

橙色语域没有第三色。橙页上需要强调时，用现有墨色的字重或不透明度反差，不要加新色相。引入第二强调色会破掉系统。

## 排印

### 字族
系统在 **Barlow** 上单语（Noto Sans SC 作 CJK 回退，覆盖相同角色）。每个展示、标题、导语、正文、图注 token 都用 Barlow。唯一次级字面是 **IBM Plex Mono**，完全留给外壳：页码、眉题、小片、标签、图表轴图注、项目列表标记、图片说明、来源注。Barlow 紧实怪诞密度与 IBM Plex Mono 均匀等宽之间的反差，是系统的次级排印节奏；主节奏是 Barlow 自身的字重与尺寸轴。

不用斜体，不用下划线。强调机制只有字重、尺寸、颜色（深页上橙强调，或橙页上纯字重）。

### 展示、标题与正文比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 13vw | Barlow | 900 | 封面级展示，文字即构图的页面上唯一主导元素 |
| `{typography.fadelist-title}` | 10.5vw | Barlow | 900 | fadelist 构图里舞台侧的超大展示 |
| `{typography.quote-mark}` | 10vw | Barlow | 900 | 拉页引文页上的起始引号字形 |
| `{typography.h1}` | 7.5vw | Barlow | 800 | 章节或分节开场标题 |
| `{typography.fadelist-item}` | 7.5vw | Barlow | 900 | 三段 fadelist 处理里每个叠起的词 |
| `{typography.stat-value}` | 5.5vw | Barlow | 900 | 统计卡片里的大数据数字 |
| `{typography.h2}` | 4.5vw | Barlow | 700 | 页面主标题 |
| `{typography.quote-text}` | 3.8vw | Barlow | 700 | 拉页引文正文 |
| `{typography.h3}` | 2.8vw | Barlow | 600 | 副标题或比较里的面板标题 |
| `{typography.lead}` | 1.6vw | Barlow | 400 | 导语段、列表项、显著辅助文案 |
| `{typography.body}` | 1.2vw | Barlow | 400 | 标准正文段落 |
| `{typography.caption}` | 0.9vw | Barlow | 400 | 图片说明、脚注、来源行 |
| `{typography.label}` | 0.72vw | IBM Plex Mono | 500 | 外壳标签、眉题、小片、等宽注 |

### 默认值
- **内容页主标题默认尺寸**：`{typography.h2}`（4.5vw）。
- **封面或章节标题默认尺寸**：`{typography.h1}`（7.5vw）。
- **陈述页上单个宣告展示瞬间默认尺寸**：`{typography.display}`（13vw）。
- **段落正文默认尺寸**：`{typography.body}`（1.2vw）；紧跟标题的导语段用 `{typography.lead}`（1.6vw）。
- **任何行内外壳元素（标签、眉题、小片、页码、轴标签）默认尺寸**：`{typography.label}`（0.72vw）。
- **统计卡片里英雄数字默认尺寸**：`{typography.stat-value}`（5.5vw）。
- **任何 Barlow 展示瞬间（h2 及以上）默认字重**：700+，最大展示用 900。
- **正文默认字重**：400。

拿不准时，页面主要文字瞬间取 `{typography.h2}`。`{typography.h1}` 只留给章节/分节开场，`{typography.display}` 留给文字即整幅构图的罕见时刻。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **所有 Barlow 展示、标题、导语、正文文字都句首大写（专有名词用真正的标题式大写）。** 系统里不存在展示字重的大写 Barlow，那样读起来完全是另一套设计语言。小写展示是 Broadside 最鲜明的单项决策。
- **所有 IBM Plex Mono 外壳文字都大写、至少 0.1em 字距。** 等宽标签、眉题、小片、页码、轴标签、来源注、项目标记始终大写。Barlow 正文与等宽外壳之间的大写/小写切分，是系统主要的大小写节奏。
- **所有展示 token 都带负字距。** `{typography.display}` 与 `{typography.stat-value}` 用 -0.04em；`{typography.h1}` 与 `{typography.fadelist-title}` 用 -0.03em 或 -0.04em；`{typography.h2}` 与 `{typography.quote-text}` 用 -0.02em。展示字重的 Barlow 没有负字距会显得没处理过。
- **所有 Barlow 展示元素都跑字重 700、800 或 900，绝不更轻。** 展示尺寸下更轻的 Barlow 会丢掉 broadside 密度。
- **橙页上每个 Barlow 展示 / h1 / h2 / h3 元素都强制 `{colors.ink-black}`。** 这是"火上墨"规则，橙页上不存在奶油色标题。
- **每个项目列表项都通过 `::before` 带橙色 `/` 等宽标记。** 系统里不存在圆点、破折号或数字项目符号。
- **每个眉题都是 `{typography.label}` 尺度的 `{colors.fire-orange}` 大写 IBM Plex Mono**（橙页上用 55% 不透明度深墨）。

### 排印原则
字重 900 + 小写 + 负字距 + Barlow 的组合是系统的声部。换成大写、降到字重 600、或去掉负字距，各自都会读成另一套系统。外壳的 IBM Plex Mono 大写 + 0.14em 字距同样不可拆。

行高随尺度收紧：`{typography.display}` 跑 0.88，`{typography.h1}` 0.9，`{typography.h2}` 1.1，直到 `{typography.lead}` 才放到 1.5+。尺度顶端的压缩，正是展示显得浑然一体的原因。

## 布局

### 画布系统
画布是 `100vw × 100vh`，全视口、溢出隐藏。幻灯片在横向 `#deck` flexbox 里并排，导航是横向平移 deck 容器，而不是切 `display`。所有尺寸都是视口相对的（`vw` / `vh`），没有固定 1920×1080 网格。

### 内边距与间隙比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 5.5vw | 每页外横向内边距 |
| `{spacing.pad-y}` | 5.5vh | 每页外纵向内边距 |
| `{spacing.gap-lg}` | 3.5vh | 主块之间的大纵向间距 |
| `{spacing.gap-md}` | 2vh | 同级元素之间的标准间距 |
| `{spacing.gap-sm}` | 1vh | 紧间距，眉题到标题、外壳条内间隙 |

内边距刻意比通用编辑系统紧。Broadside 的巨型文字需要页边显得近、不显得远，文字本该挤着画框。

### 外壳画框
系统有一层可选外壳画框，由两条横向细线组成：顶部 `slide-chrome` 条（左标签、右页码）和底部 `slide-foot` 条（镜像）。两者都是深页上 `{colors.border-dark}`、橙页上 `rgba(17, 17, 17, 0.2)` 的 1px 实线边。内部内边距/外边距用 `{spacing.gap-sm}` 与 `{spacing.gap-md}`。

系统的"宣告式"页型（封面、章节、陈述、引文、收尾）会**彻底压掉外壳**，让文字占满整个场。内容页（分栏、统计、列表、比较、图表、图示）保留外壳。

另有一个独立的 `broadside-num` 元素（等宽、约 1.1vw、低不透明度），可脱离外壳条单独放置，作目录式页码锚在橙色封面/章节页左上。

## 纵深与层级

### 平面（唯一手法）
Broadside 完全平。没有投影、没有内阴影、没有模糊抬升、没有圆角表面渐变。每个元素落在单一平面。

层级来自：
- **字重 + 尺寸反差**：主导信号。
- **1px 细线分隔**：`slide-chrome`/`slide-foot` 边、`stat-card` 顶边、`compare-panel` 分隔线、`bar-track` 左边、`chart-baseline` 基线。
- **颜色切换**：橙对墨、墨对奶油、cream-muted 对 cream。
- **负空间**：宽裕内边距与刻意留空的区域。

引入 `box-shadow`、带抬升的卡片或柔和渐变会破掉系统。平就是编辑信号。

## 形状与处理

### 圆角
除 `nav-dot`（50%，底部的小导航圆）外，圆角**处处 0px**。卡片、面板、小片、图片占位、统计卡片、图表条全是带尖角的矩形。

### 边框粗细
- **1px 实线**：唯一的结构粗细。用于 `slide-chrome`、`slide-foot`、`stat-card` 顶边、`compare-panel` 分隔线、`bar-track` 左边、`chart-baseline`、图片说明、`rule.full` 分隔线。
- **1px 虚线**：只用于 `img-placeholder`，提示"未接图片"。
- **2px 实线**：只用于 36px 宽的小 `rule` 强调残段与 `chapter-rule` 标记。

所有边框不是深页 `{colors.border-dark}`、橙页 `rgba(17, 17, 17, 0.2)`，就是深页小片边上的 `{colors.fire-orange}`。

### 装饰元素类型

**强调残段线**：36×2px 实线，深页用 `{colors.fire-orange}`、橙页用 `{colors.ink-black}`。作章节标题上方、统计上方或眉题旁的视觉"分节断口"标记。是 Broadside 唯一的装饰。

**等宽目录号**：锚在封面/章节页左上、低不透明度的小 IBM Plex Mono 数字（橙页 `rgba(17, 17, 17, 0.45)`、深页 `{colors.cream-hint}`）。读起来像出版物目录标记。

**统计卡片**：只有顶边的数据块：1px 实线顶边、无其他边，内边距里的正文装 `{typography.stat-value}`（深页大橙数字、橙页深墨数字），下方 `{typography.body}`（标签），再下方 `{typography.caption}`（`{colors.cream-hint}` 或淡墨的等宽注）。

**比较面板对**：两片等宽面板，由 1px 竖线分隔。右片可选填 `{colors.fire-orange}`（`compare-panel-orange`）作"之后"/收尾侧，左片在深色画布上保持透明。

**纵向条形图**：`bar-track` 容器只有 `border-left`（无其他轴），条从顶部垂下、`cream-hint` 填充，每张图一根条带 `.accent` 类用火橙。轴标签在基线下用等宽大写。

**Fadelist**：SPACE10 式构图：三个叠起的 Barlow-900 词按递减不透明度（1.0 / 0.5 / 0.22），配页面另一侧一个超大展示标题。用于"之前 / 之中 / 之后"或"过去 / 现在 / 未来"叙事。

**拉页引文**：超大火橙 `{typography.quote-mark}` 字形（行高 0.6，落在基线上而非下方），接宽度封顶约列宽 78% 的 `{typography.quote-text}`，再接两行 `quote-attr`（姓名在上、等宽角色/机构在下）。

**带框等宽小片**：IBM Plex Mono 大写的小行内片，1px 实线边，内边距 0.3em 纵向 × 0.8em 横向。深页上边和文字都是 `{colors.fire-orange}`；橙页上是 40% 不透明度深墨。

## 该做与不该做

### 该做
- 每个 Barlow 展示、标题、导语、正文元素都句首大写。小写展示是 Broadside 最鲜明的单项选择。
- 每个外壳元素（页码、眉题、标签、小片、轴标签、来源注、项目标记）用 IBM Plex Mono 大写、0.1em+ 字距。
- 让 `{colors.fire-orange}` 作深页上的唯一强调：眉题、强调统计值、项目 `/` 标记、领先图表条、起始引号、`rule` 残段。
- 封面、章节、宣告式收尾页把橙色用作**整片背景**。在这些页型上它是环境，不只是强调。
- 项目列表封顶三项。Broadside 重冲击密度甚于信息密度。
- 每个 Barlow 展示瞬间都加负字距，最大者 -0.04em，h2 -0.02em。
- 所有结构分隔都用 1px 细线（深页 `{colors.border-dark}`、橙页 `rgba(17,17,17,0.2)`）。它们是系统唯一的层级外壳。
- 封面、章节、陈述、引文、收尾页压掉 slide-chrome 与 slide-foot，让文字贴边呼吸。
- 橙色封面/章节页左上放 `broadside-num` 目录号，作出版物式标记。
- 每个列表项用火橙的 `/` 等宽字形作标记。

### 不该做
- 不要把 Barlow 在展示或标题字重下大写。13vw 的大写 Barlow 读起来完全是另一套设计系统。
- 不要引入第二强调色。橙就是**那一色**，加蓝、黄、绿强调会破掉抗议海报身份。
- 不要加投影、模糊抬升或圆角表面。Broadside 严格平，纵深来自文字和 1px 线。
- 不要在橙页用奶油色文字。"火上墨"规则是绝对的：橙页标题和正文用 `{colors.ink-black}`。
- 不要给 Barlow 配衬线搭档。单字面铁板是身份的一部分。
- 不要在卡片、小片、面板、统计块上用 border-radius。系统里唯一的圆是底部小导航点。
- 不要在一页里塞超过一个展示瞬间。Broadside 是一句陈述、一条线、留白，不是杂志式层叠构图。
- 不要用 Barlow 渲染外壳元素。外壳专属 IBM Plex Mono 大写。
- 不要引入第三种表面语域。只有两种：深色与橙色。奶油/纸页不存在。
- 不要用斜体或下划线。强调只靠字重、尺寸或橙色。

## 响应式行为

这是一套用 `vw`/`vh` 单位的视口流式 1920×1080 演示系统。没有固定像素断点。每个排印 token、内边距、组件尺寸都随视口线性缩放。

### 缩放行为
- 展示标题（`{typography.display}`）从 1066 宽视口约 138px 缩放到 1920 宽约 250px。
- 正文（`{typography.body}`）在同一区间从约 13px 缩放到约 23px。
- 外内边距（`{spacing.pad-x}` 5.5vw）从约 59px 缩放到约 106px。
- 所有边框固定 1px 或 2px，不缩放。

### 放映行为
- 用 `ArrowRight`、`ArrowDown`、`Space` 或 `PageDown` 前进。
- 用 `ArrowLeft`、`ArrowUp` 或 `PageUp` 后退。
- 导航以 0.8s、`cubic-bezier(0.77, 0, 0.175, 1)` ease 横向平移 deck 容器。
- 逐元素入场动画（`data-anim="fade-up"`、`fade-in`、`reveal-right`、`reveal-left`、`scale-in`）在每页变成 `.is-active` 时重播，按 `data-delay`（0 到 6）错峰。
- 导航点在底部居中，等宽页码在右下。

### 打印 / 导出
源码没有明确处理。每页是 `100vw × 100vh` 块，导出流程应以每页 1920×1080 PNG/PDF 为目标。

## CJK 与国际化内容

用本模板承载中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文搭配，并套用通用 CJK 调整。所有推荐中文字体均通过 CDN 加载，无需安装。

### 推荐中文搭配

| 角色 | 拉丁（默认） | 中文对应 |
|---|---|---|
| 展示 / h1 / h2 / h3 / stat-value / 引文 / fadelist | Barlow 700–900（小写、负字距） | 思源宋体 Noto Serif SC 900 |
| 导语 / 正文 / 图注 | Barlow 400 | 霞鹜文楷 LXGW WenKai 400 |
| 标签 / 眉题 / 小片 / 页码 / 项目标记 | IBM Plex Mono 500（大写、0.14em 字距） | 思源黑体 Noto Sans SC 500（无变换、无字距） |

### 混排策略

**策略 A**：每个角色一款自带拉丁字形覆盖的 CJK 字族。所有展示与标题角色用**思源宋体 Noto Serif SC** 字重 900；正文与导语用**霞鹜文楷 LXGW WenKai** 字重 400；外壳（眉题、标签、页码、项目标记）用**思源黑体 Noto Sans SC** 字重 500。三款字面都自带拉丁字形，与汉字并排也干净。衬线/手写/无衬线的反差，大致呼应 Broadside 的展示/正文/等宽区分，尽管源码通篇只用 Barlow。

### 加载

在模板 `<head>` 中加入：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700;900&family=Noto+Sans+SC:wght@400;500&family=LXGW+WenKai+TC&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- **行高**：在拉丁规格上提高约 15–25%。正文 1.75–1.85（从 1.6 上调），展示 1.15–1.25（从 Barlow 展示极紧的 0.88–0.9 上调）。拉丁模板把 quote-mark token 压到 0.6，CJK 在这个压缩下字符会完全重叠。展示至少放到 1.0。
- **字距**：每段 CJK 文本设为 0。模板里 Barlow 展示的 −0.02 到 −0.04em 负字距套在 CJK 上会笔画重叠；IBM Plex Mono 外壳的 +0.14em 正字距放在方正字形上显得松垮。
- **文字变换**：不要对中文套 `uppercase`，CJK 没有大小写。拉丁原版里每个 IBM Plex Mono 标签、眉题、小片、页码、项目标记都用 `text-transform: uppercase`，CJK 文本要去掉。
- **标点**：用全角中文标点（，。：；！？「」（））。
- **展示标题不加句号**：中文排印惯例，展示级标题末尾不写 。对 Broadside 的巨型展示瞬间尤其重要，13vw 下末尾一个 。 视觉上很突兀。
- **中西文之间加空格（盘古之白）**：每个汉字与相邻的拉丁字符或数字之间插入一个 ASCII 空格。写 `2024 大字海报`，不要写 `2024大字海报`。
- **一句一款字体**：思源宋体以统一衬线风格覆盖展示的 CJK 与拉丁字形，霞鹜文楷覆盖正文的两者。不要让浏览器因中文句子里的 ASCII 字符在词中回退到 Barlow。

### 本系统的美学提示

Broadside 最鲜明的单项决策是**字重 900 的小写 Barlow、13vw 展示尺度**。小写展示正是它区别于通用粗野演示的地方。到了 CJK，这个信号彻底消失，中文没有大小写。系统能补偿，是因为它的身份**八成靠结构 + 颜色**：双色语域表面系统（深 / 橙）、唯一的火橙强调、平面、1px 细线分隔、`/` 等宽项目标记、宣告页压掉外壳、负空间即构图的理念，全都能干净迁移。

最接近 Barlow"浑厚粗怪诞"语域的中文字面是**思源宋体字重 900**，但那是厚衬线展示，不是厚无衬线展示。这是一次刻意的语域转移：抗议海报尺度下的厚重中文衬线，读起来比厚重中文无衬线更像"broadside 印刷海报"（系统真正的文化指涉），后者更像"企业标牌"。正文字面用**霞鹜文楷 LXGW WenKai** 带来手写/书法暖意，与编辑抗议语域相配；若要更机构的正文，换成思源宋体 400。

保住外壳的"盖章元数据"声部，靠维持小字号（0.72vw 等效）和眉题/标签上的橙色。IBM Plex Mono 大写加字距的处理在 CJK 里会丢掉两个信号，但橙色本身足够承担外壳识别。`/` 项目标记在中文语境里也能保留为拉丁斜杠字符，它是图形标记，不是语言元素。

### 已知 CJK 缺口

- **没有 CDN 中文字面能匹配 Barlow 的浑厚怪诞 + 小写身份。** Barlow 在这套系统里最鲜明的选择是重磅小写展示，CJK 没有对等的表情杠杆。系统"小写呐喊的抗议海报"性格会柔化成"厚衬线宣告"。双色语域系统（深 / 橙）与唯一火橙强调独自扛起抗议海报身份。
- **没有 CDN 中文等宽字面给外壳声部。** IBM Plex Mono 的角色（眉题、标签、页码、`/` 项目标记）依赖等宽节奏 + 大写 + 0.14em 字距。思源黑体字重 500、0 字距是最接近的匹配，却丢掉"目录标记"信号。保留橙色与小字号，颜色和尺度承担外壳识别工作。
- **霞鹜文楷在受限网络上可能加载不到。** Google Fonts CDN 可靠地提供繁体变体（LXGW WenKai TC），简体变体也可从 cn-fontsource 获取。正文栈里始终带上 `'Noto Serif SC', serif` 作回退。
- **10vw、行高 0.6 的引号字形是拉丁引文惯例。** 中文排印用「」或『』框住，而非超大起始引号字形。中文拉页引文可考虑把超大火橙 quote-mark 换成 8vw 的全角「字，或彻底去掉装饰引号，靠橙色 + 更大字号来提示"这是引文段落"。

## 迭代指南

1. 每张新内容页都以等宽大写火橙 `kicker` 开场，接小写 Barlow 的 `{typography.h2}` 标题。别省 kicker，它是系统内容页的外壳信号。
2. 每张封面、章节、陈述收尾或收尾页都用橙色语域。别把橙色用在内容/数据页，橙是宣告瞬间专用。
3. 新统计卡片用 `stat-card` 仅顶边模式，`{typography.stat-value}` 深页橙、橙页墨。别给统计卡片加底边或整圈边框。
4. 新项目列表用火橙 `/` 等宽标记，封顶三项。
5. 新图表用 `bar-track` 纵条模式，每张图一根火橙强调条，其余条用 `{colors.cream-hint}`。
6. 新引文用超大火橙 `{typography.quote-mark}` 起始字形，接宽度上限 78% 的 `{typography.quote-text}`。
7. 橙页上的标题永远是 `{colors.ink-black}`。橙页没有奶油标题。
8. 新小片用 `tag` 样式：深页 1px 火橙边 + 火橙等宽大写文字；橙页 40% 不透明度深墨。
9. 系统有九种规范布局模式（封面、章节、陈述、分栏、统计、引文、列表、比较、收尾）加 fadelist、图表、图示扩展。新布局应按页面是宣告式还是承载内容来遵守外壳/无外壳规则。

## 已知缺口

- Broadside 的 `.light` 页类被刻意覆盖成深色，源码注释确认"没有奶油/白页"。任何使用 `.light` 的尝试都会回退到深色语域。
- Noto Sans SC 在每个字体栈里作 CJK 回退，但系统并非为拉丁/CJK 混排标题设计；CJK 展示尺寸下的行高行为可能需要逐页调整。
- 项目标记字形（`/`）通过 `::before` 设在 IBM Plex Mono 里，换成别的字形要改 CSS，不是改标记。
- 条形图 `bar-fill` 高度在源码里用 `style="height: NN%"` 内联设定，没有数据绑定层。
- fadelist 与条形图布局不在规范的"9 种布局模式"注释块里，它们是文档化系统之外追加的扩展。
- 图片占位用 `{colors.border-dark}` 虚线边与等宽大写标签，替换成真实 `<img src>` 时保持同样的 55vh 高度以维持布局。
- `c-fg-light` token 在调色板里存在（`#111111`），用于"浅色主题主文字"，但浅色主题被压掉，这个 token 在渲染输出里实际未用。
- 系统加载三款 Google Fonts 字族（Barlow、IBM Plex Mono、Noto Sans SC）的多个字重，首次渲染需要字体加载成功，否则回退到 Times New Roman。
