---
version: alpha
name: Editorial Tri-Tone
description: A literary magazine-meets-annual-report presentation system built on a strict three-color palette — blush pink, golden butter, and deep burgundy wine. Despite having eleven CSS variable names, only three hex values exist in the entire system; every alias is a semantic rename of one of those three. Headlines run Bricolage Grotesque (a variable grotesque with an optical-size axis) at extreme weights and negative letter-spacing. Instrument Serif (italic-cut only) appears as the expressive accent face for chapter numerals, pull-quotes, years, and signatures. JetBrains Mono carries all metadata, labels, and section markers at tight uppercase tracking. The aesthetic is "independent arts publication" — the kind with a colophon, hand-numbered editions, and an editorial desk.

colors:
  pink: "#F2B6C6"
  butter: "#F2D86A"
  burgundy: "#7A1F35"

color-aliases:
  pink-deep: pink
  sky: pink
  cream: butter
  lime: butter
  terracotta: butter
  navy: burgundy
  forest: burgundy
  ink: burgundy

typography:
  display-wordmark:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 300px
    fontWeight: 800
    lineHeight: 0.82
    letterSpacing: -0.04em
  display-closer:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 320px
    fontWeight: 700
    lineHeight: 0.82
    letterSpacing: -0.05em
  display-stat:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 540px
    fontWeight: 700
    lineHeight: 0.78
    letterSpacing: -0.06em
  display-stat-unit:
    fontFamily: "Instrument Serif, serif"
    fontSize: 220px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
  chapter-num:
    fontFamily: "Instrument Serif, serif"
    fontSize: 240px
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: 0
  quote-mark:
    fontFamily: "Instrument Serif, serif"
    fontSize: 200px
    fontWeight: 400
    lineHeight: 0.6
    letterSpacing: 0
  display-xl:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 84px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -0.02em
  display-lg:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 76px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -0.02em
  signature:
    fontFamily: "Instrument Serif, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
  endorsement-num:
    fontFamily: "Instrument Serif, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    color: pink
  timeline-year:
    fontFamily: "Instrument Serif, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
  subhead-serif:
    fontFamily: "Instrument Serif, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  lede:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -0.02em
  cover-pill:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  chart-title:
    fontFamily: "Instrument Serif, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
  card-title:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -0.02em
  quote-heading:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -0.02em
  body-lg:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  body-md:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-sm:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.15em
    textTransform: uppercase
  label-wide:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.18em
    textTransform: uppercase
  label-mid:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.12em
    textTransform: uppercase
  label-tight:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.10em
    textTransform: uppercase
  footer:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.12em
    textTransform: uppercase
    opacity: 0.75

spacing:
  slide-pad: 96px
  chrome-gutter: 64px
  section-gap: 48px
  card-pad: 28px 28px 30px
  chart-pad: 48px 48px 56px
  footer-bottom: 36px
  grid-gap: 24px
  endorsement-pad: 20px 0

canvas:
  width: 1920px
  height: 1080px

components:
  pill:
    borderRadius: 999px
    padding: 0.35em 0.9em
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontWeight: 500
    lineHeight: 1.0
  cover-pill:
    borderRadius: 999px
    padding: 16px 38px
    fontSize: 44px
    fontWeight: 500
  closer-pill:
    borderRadius: 999px
    padding: 12px 28px
    fontSize: 22px
  value-card:
    borderRadius: 28px
    padding: 28px 28px 30px
    height: 340px
  value-card-dark:
    background: "{colors.burgundy}"
    color: "{colors.butter}"
  value-card-light:
    background: "{colors.butter}"
    color: "{colors.burgundy}"
  chart-card:
    background: "{colors.butter}"
    color: "{colors.burgundy}"
    borderRadius: 32px
    padding: 48px 48px 56px
  timeline-ribbon:
    background: "{colors.burgundy}"
    color: "{colors.butter}"
    borderRadius: 999px
    padding: 24px 44px
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.15em
    textTransform: uppercase
  timeline-ribbon-accent:
    fontFamily: "Instrument Serif, serif"
    fontSize: 30px
    fontWeight: 400
    letterSpacing: 0
    textTransform: none
    color: "{colors.pink}"
  footer-chrome:
    position: absolute
    left: 64px
    right: 64px
    bottom: 36px
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 16px
    letterSpacing: 0.12em
    textTransform: uppercase
    opacity: 0.75
  footer-dot:
    width: 8px
    height: 8px
    borderRadius: 999px
    background: currentColor
    opacity-inactive: 0.3
    opacity-active: 1.0
  swatch-circle:
    width: 36px
    height: 36px
    borderRadius: 999px
  stat-breakdown-bar:
    height: 10px
    borderRadius: 999px
    background: "rgba(246,237,220,0.15)"
  stat-breakdown-divider:
    borderTop: "1px solid rgba(246,237,220,0.25)"
  endorsement-divider:
    borderTop: "1px solid rgba(246,237,220,0.30)"
  avatar:
    width: 72px
    height: 72px
    borderRadius: 999px
    background: "{colors.burgundy}"
    border: "3px solid {colors.burgundy}"
  timeline-axis:
    height: 4px
    background: "{colors.burgundy}"
    opacity: 0.15
  timeline-dot:
    width: 28px
    height: 28px
    borderRadius: 999px
    border: "4px solid {colors.butter}"
    background: "{colors.burgundy}"
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/editorial-tri-tone/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Editorial Tri-Tone 是一套**文学杂志演示系统**，建立在最严格的配色上：三个十六进制值、十一个 CSS 变量名。命名系统透露编辑意图，`--pink` 与 `--sky` 指向同一抹腮红，`--cream`、`--butter`、`--lime`、`--terracotta` 都解析成同一种金黄，`--burgundy`、`--navy`、`--forest`、`--ink` 都收敛到同一种深酒红。别名存在是为传达颜色在语境里的角色，不是为了引入变化。

字面栈是刻意的三方对话：
1. **Bricolage Grotesque**：带光学尺寸轴的可变怪诞体，以字重 500、600、700、800 用于所有展示与正文无衬线文字。
2. **Instrument Serif**：只用字重 400，常以斜体面貌出现。留给章节数字、拉页引号、时间轴年份、签名、推荐序数、统计百分号。
3. **JetBrains Mono**：所有元数据、标签、分节标记、脚注、页脚外壳。

编辑声部是一本带版权页的独立杂志，整套文稿最后一页字面就叫 "Colophon"。分节标记用分节符（§）接数字和标题。语气克制、文学、温暖，不企业化、不高能。

**关键特征：**
- 三色配色带语义别名：腮红粉（#F2B6C6）、金黄奶油（#F2D86A）、深酒红（#7A1F35）。
- 混排：Bricolage Grotesque 怪诞体作展示与正文，Instrument Serif 作表情性强调数字、引文、年份，JetBrains Mono 作所有标签。
- Bricolage Grotesque 标题里的 `em` 标签总会触发切到 Instrument Serif 斜体，是系统主要的排印混搭。
- 胶囊（border-radius 999px）是通用标签组件，在封面、图表图例、收尾处用三种不同尺寸。
- 数值卡片有宽裕的 28px border-radius，柔和圆润，不粗野。
- 深表面上的分隔线用低不透明度 rgba（0.25–0.30）而非实色，是低声的分隔。
- 页脚点行：一组 8px 圆的进度指示，未激活 30% 不透明度、激活 100%。
- 唯一的 SVG 图表在一张画布上结合四种系列类型：填充面积、竖条、连线圆、点线。

## 颜色

### 三种实际颜色
尽管 CSS 变量名很多，配色就是：

| 名称 | 十六进制 | 角色 |
|---|---|---|
| 腮红粉 Blush Pink | #F2B6C6 | 深表面上的强调 / 高亮、统计数字色、引号辉光 |
| 金黄奶油 Golden Butter | #F2D86A | 暖中间调、浅色页背景、深表面上的强调文字 |
| 深酒红 Deep Burgundy | #7A1F35 | 主深表面、墨色、结构调 |

### 别名映射
所有别名都解析成上面三个值之一。别名表示语境：

| 别名 | 指向 | 使用语境 |
|---|---|---|
| `--pink` | #F2B6C6 | 默认强调标签 |
| `--pink-deep` | #F2B6C6 | （未用的独立值，与 pink 相同） |
| `--sky` | #F2B6C6 | 分解图里的 D 段条 |
| `--cream` | #F2D86A | 浅表面背景 |
| `--butter` | #F2D86A | 深表面上的强调文字、卡片背景 |
| `--lime` | #F2D86A | 丝带强调文字、深表面上的眉题标签 |
| `--terracotta` | #F2D86A | 导语或正文里的斜体 em 高亮 |
| `--navy` | #7A1F35 | 深表面语境的替代标签 |
| `--forest` | #7A1F35 | 深面板或列背景 |
| `--burgundy` | #7A1F35 | 结构背景色 |
| `--ink` | #7A1F35 | 所有文字色 |

## 排印

### 字族
- **Bricolage Grotesque**：主字面。带光学尺寸轴（opsz 12..96）与字重 400 到 800 的可变体。字重区间是表情工具，400 正文、500 导语、600 卡片标题与引文页眉、700 分节标题、800 字标。
- **Instrument Serif**：仅字重 400，加载了斜体变体。作为 Bricolage Grotesque 的表情对应面。绝不用于正文，始终给大数字、引号、签名、年份、推荐序数、统计百分号。关键洞察是系统从不用 Instrument Serif 排"正常"行文，只给人情味瞬间。
- **JetBrains Mono**：字重 400 与 500。所有标签大写、0.10–0.18em 字距。始终是次级信息：分节标记、元数据、脚注、图例类别、眉题、页脚外壳。

### `em` 规则
任何 Bricolage Grotesque 标题里，`<em>` 标签会触发切到 Instrument Serif 字重 400。这是系统主要的行内排印混搭，怪诞标题被一段衬线旁白打断。例如："A short trajectory, told in *five stops*." em 部分读起来是更安静、更沉思的对应声部。

### `b` 规则（仅引文页）
Instrument Serif 块引文里，`<b>` 标签会触发切回 Bricolage Grotesque 字重 600 的酒红色。是 em 规则的反用，衬线引文被一个怪诞强调 punctuate。

### 展示比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-stat}` | 540px | Bricolage Grotesque | 700 | 满出血超大统计或数字 |
| `{typography.display-closer}` | 320px | Bricolage Grotesque | 700 | 巨型标题或收尾字标 |
| `{typography.display-wordmark}` | 300px | Bricolage Grotesque | 800 | 主字标或文稿标题 |
| `{typography.display-stat-unit}` | 220px | Instrument Serif | 400 | 统计数字旁的强调符号 |
| `{typography.chapter-num}` | 240px | Instrument Serif | 400 | 大章节或分节数字 |
| `{typography.quote-mark}` | 200px | Instrument Serif | 400 | 装饰性大引号 |
| `{typography.display-xl}` | 84px | Bricolage Grotesque | 700 | 数据或图表布局的分节标题 |
| `{typography.display-lg}` | 76px | Bricolage Grotesque | 700 | 分节标题 |
| `{typography.signature}` | 64px | Instrument Serif | 400 | 签名或落款元素 |
| `{typography.lede}` | 56px | Bricolage Grotesque | 500 | 导语或开场陈述 |
| `{typography.quote-heading}` | 56px | Bricolage Grotesque | 600 | 面板标题或编辑副题 |
| `{typography.endorsement-num}` | 56px | Instrument Serif | 400 | 推荐或列表序数 |
| `{typography.timeline-year}` | 56px | Instrument Serif | 400 | 年份戳或大序数强调 |
| `{typography.subhead-serif}` | 48px | Instrument Serif | 400 | 深表面上的次级副题 |
| `{typography.cover-pill}` | 44px | Bricolage Grotesque | 500 | 大标签云或关键词胶囊 |
| `{typography.chart-title}` | 40px | Instrument Serif | 400 | 卡片或面板标题 |
| `{typography.card-title}` | 40px | Bricolage Grotesque | 600 | 卡片或数值标题 |

### 正文与标签比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.body-lg}` | 28px | Bricolage Grotesque | 400 | 宣言右栏正文 |
| `{typography.body-md}` | 26px | Bricolage Grotesque | 600/400 | 出处姓名、推荐正文 |
| `{typography.body-sm}` | 24px | Bricolage Grotesque | 400 | 卡片说明、统计注释、收尾索引 |
| `{typography.label}` | 24px | JetBrains Mono | 400 | 标准分节标签（0.15em 字距） |
| `{typography.label-wide}` | 24px | JetBrains Mono | 400 | 深色页上的眉题（0.18em 字距） |
| `{typography.label-mid}` | 24px | JetBrains Mono | 400 | 宣言底部元信息（0.12em） |
| `{typography.label-tight}` | 24px | JetBrains Mono | 400 | 图例类别、分解标签（0.10em） |
| `{typography.footer}` | 16px | JetBrains Mono | 400 | 页脚外壳（0.12em，不透明度 0.75） |

### 原则
Bricolage Grotesque 的光学尺寸轴让字面在大尺寸下明显更有表情、小尺寸下更清晰，而不改字重。540px 与 300px（统计与字标）下展示渲染出宽开字形，24px（正文）下收紧。两者在展示都是字重 700 或 800，正文都是字重 400。字面绝不用于中间尺寸（48–72px），那一档属于 Instrument Serif。

Bricolage Grotesque 展示字距始终为负：300px 时 -0.04em，320px 时 -0.05em，540px 时 -0.06em。正文尺寸（24–28px）不加字距。

JetBrains Mono 标签字距始终为正、按用途变化：密集数据语境 0.10em，次级元信息 0.12em，标准分节标签 0.15em，深色页标题眉题 0.18em。

## 布局

### 画布系统
每页恰好 1920×1080px。`deck-stage` 自定义元素负责居中与缩放。

### 栏距系统
- **外壳栏距**（左右 64px）：给页脚外壳和多数内容边缘用。
- **宽裕幻灯片内边距**（96px）：多数页用 `padding: 96px 64px`，上下内边距大于左右，即便横向页也有纵向出版物的感觉。
- **宽幻灯片内边距**（图表页顶部 88px）：为容纳双栏布局略收。

### 页内间距模式
每页遵循自上而下的阅读顺序：
1. 分节标记（`§ XX — Title`，JetBrains Mono，24px，标签字距）
2. 标题或主内容
3. 正文 / 网格内容
4. 页脚元信息（绝对定位，底部 36px）

## 层级与纵深

系统**完全不用 box shadow**。纵深完全来自：

### 色彩表面对比
酒红/奶油/粉三元组自带层级：
- 奶油表面显得"靠前"（暖、亮）
- 粉显得"被强调"（暖、中）
- 酒红显得"后退"（深、锚定）

分栏页内交替表面色（宣言页奶油左 / 酒红右，引文页 lime 左 / 酒红右）靠边缘对比而非阴影造出纵深。

### 不透明度分隔线
深（酒红）表面上，所有分隔线与结构线用 rgba 而非实色：
- 统计分解里的行分隔：`rgba(246,237,220,0.25)`
- 引文页的推荐行：`rgba(246,237,220,0.30)`
- 时间轴：`opacity: 0.15` 压在实酒红上

那些 rgba 串里的奶油值（246,237,220）近似全不透明度的奶油色，分隔线读起来像凹蚀刻，而非画上去的线。

### 图表卡片抬起
图表卡片（slide 6）靠放在酒红背景上的奶油卡片 32px border-radius 取得"抬起"感。没有阴影，对比表面上的圆角发出抬升信号。

## 形状与处理

### 圆角比例
| 值 | 用途 |
|---|---|
| 999px | 所有胶囊、时间轴丝带、色块圆、头像、分解条、时间轴点、页脚点、图表数据圆 |
| 32px | 图表卡片（slide 6） |
| 28px | 数值卡片（slide 3） |
| 4px | SVG 图表条（rx="4"） |
| 0px | 分节标题、网格单元格（不圆） |

系统有强二元：要么全圆（胶囊、圆），要么方（内容块）。例外是图表卡片（32px）与数值卡片（28px），半径大到显得"柔"，但仍是几何形而非圆形。

### 胶囊系统
胶囊是通用标签/小片组件。三种尺寸变体：
- **封面胶囊**：44px 字、16px 38px 内边距，大到在标签云里读成标题元素。
- **标准胶囊**（分节标签、图例项）：22–24px 字、10–12px 24–28px 内边距。
- **配色分配**交替：封面用酒红底/粉字与奶油底/酒红字，收尾页用酒红/奶油或 lime/墨。

### SVG 图表（Slide 6）
720×380 viewBox 的内联 SVG 图表刻意结合四种系列类型，展示单张图表表面的表现范围：
- **面积系列**（系列 A）：填充路径，粉填充 0.85 不透明度，酒红描边字重 3。
- **条系列**（系列 C）：酒红矩形配 rx="4"。
- **连线圆系列**（系列 B）：奶油圆（r=8），酒红描边/填充，压在酒红线上，字重 3。
- **点线**（系列 D）：酒红虚线描边（stroke-dasharray="2 10"、stroke-linecap="round"），60% 不透明度。

Y 轴标签是 JetBrains Mono 24px、60% 不透明度、对 x=0 左对齐。

## 该做与不该做

### 该做
- 把三个十六进制值当封闭系统。每个元素都用粉、奶油或酒红，没有中性色、没有灰、没有白。
- Instrument Serif 只给人情味瞬间：数字、年份、签名、引号、推荐序数。绝不用于行文正文。
- Bricolage Grotesque 标题里用 `em` 标签触发衬线切换。这是系统主要的行内混搭，也是最鲜明的编辑声部。
- 所有标签文字（JetBrains Mono）给 0.10em 到 0.18em 的正字距。没有字距的等宽读成代码，不像编辑。
- 双栏分栏页交替表面色。一侧永远奶油，另一侧永远酒红。
- 正文用 Bricolage Grotesque 字重 400（文字）、500–600（强调标签）。字重轴是语气旋钮。
- 胶囊用多种尺寸，胶囊是通用标签，尺寸标示语境：44px 标题级归类，22–24px 实用标签。
- 分节标记遵循 `§ NN — Title` 模式，用 JetBrains Mono，每页以此开场。

### 不该做
- 不要引入第四色。三色约束是设计前提。
- 不要把 Instrument Serif 用小尺寸或放进行文段落。它纯粹是强调字面。
- 不要破掉 em 规则，用 Bricolage Grotesque 斜体代替 Instrument Serif 作行内强调会丢掉排印混搭。
- 不要在 Bricolage Grotesque 展示尺寸上用正字距，只按尺寸用 `letter-spacing: -0.02em` 到 `-0.06em` 的负字距。
- 不要在深（酒红）表面上加实色分隔线。深背景上所有结构线都必须用低不透明度 rgba。
- 不要加 box shadow。系统没有，纵深来自表面对比和对比背景上的 border-radius。
- 不要给大内容容器加圆（分节面板、网格背景）。圆只给胶囊尺度和卡片尺度元素（数值卡片、图表卡片）。
- 不要把 Bricolage Grotesque 字重 800 用在字标以外。800 留给唯一最大的排印瞬间。

## 响应式行为

本模板**专为 1920x1080 演示显示设计**。`deck-stage` web 组件通过 CSS transform 处理视口缩放，1920x1080 画布等比缩放到任何屏幕而不改布局。

### 放映行为
- 前进经键盘或演示翻页笔（由 `deck-stage.js` 处理）。
- 没有定义悬停态。
- 没有交互元素。

### 打印 / 导出
- 96dpi 下，1920x1080 对应 20x11.25 英寸画框。
- 540px 的统计数字渲染成约 405pt，适合大幅面印刷。
- 三色配色印刷安全，酒红是 PMS 区间深酒调，奶油是暖黄，粉是柔腮红，CMYK 胶印都能很好还原。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 中文字面 | 字重 | 理由 |
|---|---|---|---|
| 展示字标 / 收尾 / 统计（300–540px） | 站酷小薇体 ZCOOL XiaoWei | 400 | 文学装饰衬线，带与 Bricolage Grotesque + Instrument Serif 斜体在极端尺度下同样的表情个性 |
| 分节标题（76–84px） | 思源黑体 Noto Sans SC | 700 | CJK 里的怪诞对应，承载 Bricolage Grotesque 的结构分量 |
| 章节数字 / 引号 / 年份（200–240px） | 霞鹜文楷 LXGW WenKai | 400 | 手工排的暖意，匹配 Instrument Serif 的表情强调角色 |
| 正文段落（24–28px） | 思源宋体 Noto Serif SC | 400 | 明朝正文声部，文学语域 |
| 导语 / 引文页眉（56px） | 思源黑体 Noto Sans SC | 500–600 | 匹配 Bricolage Grotesque 字重 500/600 |
| 等宽标签 / 分节标记 / 页脚 | 思源等宽 Noto Sans Mono CJK SC | 400–500 | 为 `§ NN — Title` 标记保住 JetBrains Mono 外壳质感 |

### 混排策略

用**策略 C**：保留 Bricolage Grotesque（展示、正文）与 Instrument Serif（斜体强调）作拉丁字面，CJK 字形才回退到中文栈。Editorial Tri-Tone 的文学杂志身份依赖 Bricolage Grotesque 的光学尺寸轴与 Instrument Serif 的斜体切分作为品牌声部的一部分，整体换成 CJK 字族会把系统压平成"通用中文编辑"。栈：

```css
/* Bricolage Grotesque roles (display, body) */
font-family: 'Bricolage Grotesque', 'Noto Sans SC', sans-serif;
/* Instrument Serif roles (chapter-num, quote-mark, year, signature) */
font-family: 'Instrument Serif', 'LXGW WenKai TC', serif;
/* JetBrains Mono roles (labels, section markers) */
font-family: 'JetBrains Mono', 'Noto Sans Mono CJK SC', monospace;
```

系统招牌的 `<em>` 规则（Bricolage Grotesque → Instrument Serif 斜体行内）是拉丁里承载编辑语气的东西。CJK 对应：思源黑体（Noto Sans SC）标题里的 `<em>` 应切到**站酷小薇体（ZCOOL XiaoWei）**，一款带同款柔和反差的文学装饰衬线。加一条 CSS 规则：

```css
h1 em, h2 em, .lede em, .quote-heading em {
  font-family: 'Instrument Serif', 'ZCOOL XiaoWei', 'LXGW WenKai TC', serif;
  font-style: italic; /* Latin only — CJK ignores font-style */
}
```

留意展示尺寸（300–540px）的基线错位：Bricolage Grotesque 用 -0.04em 到 -0.06em 字距，视觉上比 Noto Sans SC 更紧，于是像 `INTO 中国` 这样的混排字标可能显得不匀。英雄 / 字标瞬间优先用单一文字行，让第二套文字单独落在下方一行。

### 加载

在既有 Google Fonts `<link>` 里追加（或作为第二条 link 标签）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Noto+Serif+SC:wght@400;500;700&family=LXGW+WenKai+TC&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
```

ZCOOL XiaoWei 是给 em 切换角色用的装饰终端衬线，Google Fonts 上只以字重 400 提供。

### 通用 CJK 调整

以下调整适用于本系统**每一个 CJK 块**，无论尺寸或角色：

- **行高放宽 0.05–0.08。** CJK 字形是全宽方块，视觉分量比拉丁字形重，为拉丁调的行高（展示 0.78–0.92、正文 1.4–1.45）在中文里读起来局促。展示放到 0.95–1.05，正文放到 1.5–1.6。
- **去掉 CJK 标题的负字距。** Bricolage Grotesque 展示用 -0.04em 到 -0.06em 字距，会撞在一起。CJK 段设 `letter-spacing: 0`，标题看着挤时可用微小的正 `0.02em`。
- **绝不对 CJK 文字用 `text-transform: uppercase`。** 中文没有大小写，CSS 属性对汉字无效，却会悄悄破坏混排行里本该大写的拉丁部分。
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不用拉丁对应物（`,.:;!?""''()`）。同一句里混用标点系统读起来是排印错误。
- **CJK 标题末尾不加句号（。）。** 中文标题与拉丁遵循同一规则，标题式行去掉末尾标点。正文段落保留 。
- **在 CJK 与拉丁串交界处套用盘古之白。** 汉字与相邻拉丁词或数字之间应有一个空格（或 0.25em 外边距），例如 `2026 年 5 月` 而非 `2026年5月`。要么手打空格，要么用 `pangu.js` 式自动加空格器。
- **一句一款字体。** 不要在同一句里切换 Noto Sans SC、Noto Serif SC 与 ZCOOL XiaoWei，挑与角色匹配的字面（标题 = Noto Sans SC，正文 = Noto Serif SC，em 强调 = ZCOOL XiaoWei），整段从一而终。

### 本系统的美学提示

Editorial Tri-Tone 的文学杂志声部依赖 Bricolage Grotesque（结构）与 Instrument Serif 斜体（表情）之间的排印反差。中文里同样的反差活在**思源黑体 ↔ 站酷小薇体**搭配里，一款干净怪诞体对一款文学装饰衬线。标题里的 em 规则应明确切到**站酷小薇体**（不是霞鹜文楷，后者更暖但不够"文学装饰"），这才保住定义系统的排印混搭。

系统招牌的展示瞬间（300px 字标、540px 统计数字、240px 章节数字）是中文最响的时刻。装饰性瞬间（章节序数"第一章"用文学衬线渲染）取**站酷小薇体**，结构性瞬间（"我们的方法"这样的分节标题）取**思源黑体字重 700**。200px 引号字形在中文里更难，中文引号（「」）不像拉丁'弯引号'那样有装饰分量，可考虑把整个引文瞬间用拉丁字形渲染（在标点字符本身用 `Instrument Serif` 字面），下方正文切到思源宋体。

分节标记约定 `§ NN — Title` 在中文里成立：`§ 02 — 我们的承诺`。分节符与数字保留在 JetBrains Mono / Noto Sans Mono CJK SC 里，标题文字可切到思源黑体字重 400 配 0.05em 字距，保住外壳质感。

### 已知 CJK 缺口

ZCOOL XiaoWei 是 em 切换角色在美学上正确的匹配，但它**只以字重 400 提供、没有斜体切分**。中文没有斜体概念（倾斜的汉字读成坏了，不是强调），所以缺斜体没问题，然而 Instrument Serif 斜体在拉丁里提供的视觉柔和反差（倾斜、更流动的字形）在中文里无法精确复刻。ZCOOL XiaoWei 的装饰终端衬线质感是最接近的对应，但它与思源黑体的反差是**基于字面、不是基于倾斜**。大量依赖 em 规则的文稿应先在中文里测试视觉节奏再定稿，反差显得弱时可把 em 部分字号加大 4–8px 补偿。

## 迭代指南

1. 分节标签始终用 JetBrains Mono 的 `§ NN — Title` 约定，配 `{typography.label}` 字距。
2. 每个带 em/斜体瞬间的标题都用 `<em>` 触发 Instrument Serif。绝不直接给 Bricolage Grotesque 用 `font-style: italic`。
3. 数值卡片交替：奇数卡（c1、c3、c5、c7）深（酒红/奶油），偶数卡（c2、c4、c6、c8）浅（奶油/酒红）。
4. 新深表面分节用 `rgba(246,237,220,0.25)` 作分隔线，不用全不透明度 `{colors.butter}`。
5. 新胶囊沿用既有交替：酒红底/粉字与奶油底/酒红字，在簇里取得变化。
6. 加图表系列时先用四种既有视觉编码（面积、条、圆、点线）再自创新的。
7. 所有分节背景必须是三色配色之一，绝不混（不许半粉半奶油）。
8. 页脚外壳全稿共用：`position:absolute; left:64px; right:64px; bottom:36px; font-family:JetBrains Mono; font-size:16px; opacity:0.75`。

## 已知缺口

- `deck-stage.js` 脚本是外部依赖，本文件未描述。
- 页脚点行进度指示器（`.footer .dotrow`）在 HTML 里渲染了，但点全被设成 "on" 类或留作未激活，放映者需要动态更新页状态。
- SVG 图表用硬编码路径、坐标、占位数值，没有数据绑定层。
- slide 4 的分解条用内联 `width: XX%` 作样式，百分比必须手动设。
- 时间轴停靠点（`.stop .dot`）是 `display: none`，有样式但不可见。填充该页的放映者需通过 CSS 启用。
- Instrument Serif 斜体作为字体变体加载了，但并非每个语境都显式用 `font-style: italic` 调用，某些情况下浏览器会根据周围语境从可变字体的斜体轴自动选中。
- slide 4 的色块圆引用 `--terracotta` 与 `--sky`，它们与 `--butter`、`--pink` 解析完全相同，视觉区分只存在于源码语义里，不在视觉上。
