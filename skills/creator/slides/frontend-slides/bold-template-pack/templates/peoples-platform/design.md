---
version: alpha
name: People's Platform
description: "A WPA-poster-meets-political-campaign presentation system built on three typefaces and a five-color palette that reduces to three functional roles. Alfa Slab One — a compressed slab serif — does all the heavy lifting at extreme sizes in pure uppercase. Caveat Brush drops in as a handwritten human interrupt: lowercase, slightly rotated, emotionally warm. DM Mono carries all metadata at tight uppercase tracking. The palette is electric cobalt blue, amber orange, and hot red — with red functioning exclusively as a shadow/depth color, never as a surface fill. Every slide gets a paper grain overlay that makes the whole deck feel screen-printed. The aesthetic is loud, confident, and populist — the kind of visual language that belongs on a protest placard, a union newsletter, or a campaign bus."

colors:
  blue: "#2C2CDC"
  blue-deep: "#1B1BB0"
  orange: "#F2A03A"
  orange-deep: "#E89321"
  red: "#E83A2A"
  red-deep: "#B7281C"
  cream: "#F4E9D6"
  paper: "#F5F2EA"
  ink: "#0E0E14"

typography:
  display-jumbo:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 540px
    fontWeight: 400
    lineHeight: 0.82
    letterSpacing: -0.02em
    textTransform: uppercase
  display-hero:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 260px
    fontWeight: 400
    lineHeight: 0.86
    letterSpacing: 0.005em
    textTransform: uppercase
  display-title:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 240px
    fontWeight: 400
    lineHeight: 0.86
    letterSpacing: 0.005em
    textTransform: uppercase
  display-xl:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 180px
    fontWeight: 400
    lineHeight: 0.88
    letterSpacing: 0.005em
    textTransform: uppercase
  display-lg:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 140px
    fontWeight: 400
    lineHeight: 0.88
    letterSpacing: 0.005em
    textTransform: uppercase
  display-md:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 120px
    fontWeight: 400
    lineHeight: 0.88
    letterSpacing: 0.005em
    textTransform: uppercase
  display-sm:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 108px
    fontWeight: 400
    lineHeight: 1.04
    letterSpacing: 0.005em
    textTransform: uppercase
  stat-unit:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 130px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  section-num:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 54px
    fontWeight: 400
    lineHeight: 1.0
    textTransform: uppercase
  card-title:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 54px
    fontWeight: 400
    lineHeight: 1.0
    textTransform: uppercase
  kpi-value:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 88px
    fontWeight: 400
    lineHeight: 0.9
    textTransform: uppercase
  quote-mark:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 300px
    fontWeight: 400
    lineHeight: 0.7
    textTransform: uppercase
  quote-body:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 78px
    fontWeight: 400
    lineHeight: 1.08
    textTransform: uppercase
  item-title:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.0
    textTransform: uppercase
  item-title-sm:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 30px
    fontWeight: 400
    lineHeight: 1.0
    textTransform: uppercase
  toc-entry:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.0
    textTransform: uppercase
  subtitle:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.01em
    textTransform: uppercase
  cta:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 48px
    fontWeight: 400
    letterSpacing: 0.02em
    textTransform: uppercase
  stamp:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 28px
    fontWeight: 400
    letterSpacing: 0.04em
    textTransform: uppercase
  url:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 46px
    fontWeight: 400
    letterSpacing: 0.02em
    textTransform: uppercase
  script-lg:
    fontFamily: "Caveat Brush, cursive"
    fontSize: 96px
    fontWeight: 400
    textTransform: lowercase
  script-md:
    fontFamily: "Caveat Brush, cursive"
    fontSize: 64px
    fontWeight: 400
    textTransform: lowercase
  body-lg:
    fontFamily: "Archivo Narrow, sans-serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Archivo Narrow, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-sm:
    fontFamily: "Archivo Narrow, sans-serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-xs:
    fontFamily: "Archivo Narrow, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label:
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.18em
    textTransform: uppercase
  label-wide:
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.22em
    textTransform: uppercase
  label-accent:
    fontFamily: "DM Mono, monospace"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.16em
    textTransform: uppercase
  signoff:
    fontFamily: "DM Mono, monospace"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.20em
    textTransform: uppercase

spacing:
  slide-gutter: 90px
  content-gutter: 120px
  topbar-height: 90px
  section-border: 6px
  inner-border: 3px
  grid-gap-lg: 90px
  grid-gap-md: 30px
  frame-inset: 48px

canvas:
  width: 1920px
  height: 1080px

components:
  inset-frame:
    border: "6px solid {colors.cream}"
    position: absolute
    inset: 48px
  topbar:
    position: absolute
    top: 0
    left: 0
    right: 0
    height: 90px
    background: "{colors.blue}"
    color: "{colors.cream}"
    padding: 0 90px
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.18em
    borderBottom: "6px solid {colors.cream}"
  section-divider:
    borderBottom: "6px solid {colors.ink}"
    height: 6px
  toc-row:
    display: grid
    gridTemplateColumns: "90px 1fr 100px"
    gap: 24px
    padding: "20px 0"
    borderBottom: "3px solid {colors.ink}"
  toc-num:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 54px
    color: "{colors.orange}"
    textShadow: "3px 3px 0 {colors.red}"
  pillar-col:
    padding: "60px 50px"
    borderRight: "6px solid {colors.ink}"
    background: "{colors.paper}"
  pillar-col-alt:
    background: "{colors.blue}"
    color: "{colors.cream}"
  pillar-tag:
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.18em
    borderTop: "3px solid {colors.ink}"
    paddingTop: 18px
    marginTop: 14px
    alignSelf: flex-start
  kpi-card:
    border: "5px solid {colors.ink}"
    padding: "28px 30px"
    background: "{colors.paper}"
  kpi-card-alt:
    background: "{colors.blue}"
    color: "{colors.cream}"
  timeline-dot:
    width: 60px
    height: 60px
    borderRadius: 50%
    background: "{colors.orange}"
    border: "6px solid {colors.ink}"
    boxShadow: "6px 6px 0 {colors.red}"
  timeline-dot-alt:
    background: "{colors.blue}"
  timeline-track:
    height: 14px
    background: "{colors.ink}"
  compare-side-left:
    background: "{colors.paper}"
    borderRight: "6px solid {colors.ink}"
    padding: "60px 70px"
  compare-side-right:
    background: "{colors.blue}"
    color: "{colors.cream}"
    padding: "60px 70px"
  compare-label:
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.22em
    paddingBottom: 14px
    borderBottom: "4px solid {colors.ink}"
    alignSelf: flex-start
  diamond-bullet:
    width: 24px
    height: 24px
    background: "{colors.red}"
    borderRadius: 4px
    transform: rotate(45deg)
  diamond-bullet-alt:
    background: "{colors.orange}"
  avatar:
    width: 120px
    height: 120px
    borderRadius: 50%
    background: "{colors.blue}"
    border: "6px solid {colors.blue}"
    boxShadow: "6px 6px 0 {colors.red}"
  quote-stamp:
    background: "{colors.blue}"
    color: "{colors.orange}"
    padding: "18px 32px"
    transform: rotate(-3deg)
    border: "5px solid {colors.cream}"
    fontFamily: "Alfa Slab One, serif"
    fontSize: 28px
    letterSpacing: 0.04em
    boxShadow: "6px 6px 0 {colors.red}"
    textTransform: uppercase
  circular-stamp:
    width: 200px
    height: 200px
    borderRadius: 50%
    background: "{colors.cream}"
    color: "{colors.blue}"
    border: "6px solid {colors.orange}"
    transform: rotate(-9deg)
    boxShadow: "8px 8px 0 {colors.red}"
  meta-pill:
    border: "3px solid {colors.cream}"
    padding: "8px 20px"
    borderRadius: 999px
  ribbon:
    position: absolute
    bottom: 0
    left: 0
    right: 0
    height: 60px
    background: "{colors.orange}"
    color: "{colors.blue}"
    borderTop: "6px solid {colors.ink}"
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.22em
    fontWeight: 600
  lede-block:
    fontFamily: "Archivo Narrow, sans-serif"
    fontWeight: 500
    fontSize: 28px
    lineHeight: 1.35
    borderLeft: "4px solid {colors.ink}"
    paddingLeft: 50px
  lede-block-top:
    borderTop: "6px solid {colors.ink}"
    paddingTop: 24px
  underline-rule:
    height: 14px
    background: "{colors.ink}"
    width: "30%"
    marginTop: 60px
  kicker:
    fontFamily: "DM Mono, monospace"
    letterSpacing: 0.22em
    fontSize: 26px
    color: "{colors.red}"
    marginBottom: 48px
  grain-overlay:
    position: absolute
    inset: 0
    pointerEvents: none
    backgroundImage: "radial-gradient(rgba(0,0,0,.06) 1px, transparent 1px), radial-gradient(rgba(255,255,255,.05) 1px, transparent 1px)"
    backgroundSize: "3px 3px, 5px 5px"
    backgroundPosition: "0 0, 1px 2px"
    mixBlendMode: multiply
    opacity: 0.5
  orange-dot:
    width: 10px
    height: 10px
    borderRadius: 50%
    background: "{colors.orange}"
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/peoples-platform/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

People's Platform 是一套 **WPA 海报遇上政治竞选的幻灯片系统**，信念的视觉语言、公共演说的图形语域。画布是暖纸（`{colors.paper}` — #F5F2EA），比白暖一丝，每页都经 CSS 伪元素叠一层颗粒纹理，让整份文稿读起来像丝网印刷，而非渲染出来。

字体栈是一套三向阶级系统。**Alfa Slab One** 在极端尺寸下霸占舞台，压缩、板衬线厚重、全大写、天生权威。它是呐喊的声部。**Caveat Brush** 是人的打断，手写、小写、略带旋转、情绪在场。它是低语的声部。**DM Mono** 是官僚的记录员，等宽、宽字距全大写、恒定 24px，负责交代事项的声部。Archivo Narrow 是主力正文字面，绝不在展示尺寸出现，始终窄体，字重 500 求可读。

配色有五个具名颜色，却只担三个功能角色。**蓝**（`{colors.blue}` — #2C2CDC）是主结构色：高强调表面的背景、内容分隔的边框、非蓝底上的文字色。**橙**（`{colors.orange}` — #F2A03A）是能量色：统计数字、栏序数、蓝表面内的强调文字。**红**（`{colors.red}` — #E83A2A）是纵深色，它绝不作为表面填充出现，只作堆叠 text-shadow 或 box-shadow 的第一层。blue-deep 与 red-deep 是双层堆叠阴影系统的外层。

招牌纵深手法是**堆叠偏移 text-shadow**：橙文字在 6–12px 处投下红影，红影再在 12–24px 处投下 red-deep 影。这造出三层准 3D 凸版印刷效果，是系统最易认的特征。交互元素上的 box-shadow 镜像同一处理：`6px 6px 0 {colors.red}`。

**关键特征：**
- 纸画布（`{colors.paper}` — #F5F2EA），每页经 CSS 伪元素叠颗粒。
- 堆叠双层 text-shadow：`Npx Npx 0 {colors.red}, 2Npx 2Npx 0 {colors.red-deep}`。阴影尺寸随字号缩放。
- Alfa Slab One 承载全部展示与结构文字，全大写、行高 0.82–1.04、字距 0.005em。
- 红（`{colors.red}`）专作阴影色，绝不作表面背景。
- 厚重 6px 墨边框用于所有主结构分隔（顶条、分节头、栏分隔、内嵌画框）。
- DM Mono 标签恰好 24px，全稿 0.18–0.22em 字距。
- Caveat Brush 出现在 64–96px，始终小写、始终旋转 2–5 度，是刻意的粗糙信号。
- 橙色底部飘带：锚在数据密集页底部的水平跑马灯条。
- 内嵌装饰画框（6px 实奶油、`inset: 48px`），用在蓝底页上。

## 颜色

### 主调色板
- **蓝**（`{colors.blue}` — #2C2CDC）：电光钴蓝。高强调页与结构元素的主导表面色。用作整页背景、栏填充、顶条背景、奶油 / 纸表面上的文字、头像填充、比较面板的深色一侧。
- **深蓝**（`{colors.blue-deep}` — #1B1BB0）：更深的蓝。专作堆叠 text-shadow 的最外层。绝不作为表面填充。
- **橙**（`{colors.orange}` — #F2A03A）：暖琥珀。能量强调。用于超大统计数字、栏序数、CTA 按钮填充、飘带背景、蓝表面内的强调文字、印章元素上 text-shadow 的内层。
- **深橙**（`{colors.orange-deep}` — #E89321）：更深的琥珀。预留给橙色元素上最深的阴影层。不作表面填充。
- **红**（`{colors.red}` — #E83A2A）：热红。纵深色。专用于 text-shadow 与 box-shadow，多数展示文字与按钮的第一层偏移。绝不作为背景或主文字色出现。
- **深红**（`{colors.red-deep}` — #B7281C）：暗红。最大展示元素上双层 text-shadow 的最外层。绝不作为表面填充。

### 表面调色板
- **奶油**（`{colors.cream}` — #F4E9D6）：暖奶油。用作蓝表面上的文字 / 边框色（反色模式）、内嵌画框边框，以及奶油调页的整页背景。
- **纸**（`{colors.paper}` — #F5F2EA）：带暖调的米白。默认幻灯片背景，比 #fff 略暖、不那么刺。多数内容页用它。
- **墨**（`{colors.ink}` — #0E0E14）：近黑，带一丝几乎看不出的蓝底。用于全部结构边框、正文、栏分隔、时间轴轨道、KPI 卡片边框。

### 颜色角色小结
- **蓝表面** = 高强调、定论、权威瞬间
- **纸 / 奶油表面** = 内容优先、可读、从属瞬间
- **橙** = 数字、能量、某页上最要紧的东西
- **红** = 你从不直接看见的颜色，只感受得到它的阴影

## 排印

### 字族
三款字面，各占完全不重叠的语域：

**Alfa Slab One** 是主声部。压缩、厚重的板衬线，竖笔强、衬线方块状。以字重 400（唯一可用字重，天生就粗）严格全大写，用于从 28px 印章到 540px 统计数字的每个展示瞬间。压缩的字形意味着再大也不显宽，而是显高、像柱子。轻微的正字距（0.005em）防止大尺寸下字碰字。

**Caveat Brush** 是人的声部。粗糙的手写脚本字面，只在大尺寸（64–96px）用，始终小写，始终带一点旋转（-2 到 -5 度）。出现在温暖、过渡、或随意的瞬间，是本就结构严谨的文稿里一条脚本旁注。绝不用于正文或标签。

**DM Mono** 是记账声部。等宽、24px、宽字距（0.18–0.22em）、全大写。出现在顶条、页脚、眉题标签、元数据行、来源引注、飘带文字。它始终是辅助元素，海报底部印的技术规格，不是标题。

**Archivo Narrow** 是正文声部。窄体无衬线，承载全部连续正文：支柱描述、列表项段落、比较列表项、统计注解。多数正文用字重 500，较小图注用 400。绝不在展示尺寸出现。

### 展示比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-jumbo}` | 540px | Alfa Slab One | 400 | 满幅超大统计数字 |
| `{typography.display-hero}` | 260px | Alfa Slab One | 400 | 收尾或开场主导标题 |
| `{typography.display-title}` | 240px | Alfa Slab One | 400 | 文稿主标题 |
| `{typography.display-xl}` | 180px | Alfa Slab One | 400 | 大栏序数数字 |
| `{typography.display-lg}` | 140px | Alfa Slab One | 400 | 分节标题，一级 |
| `{typography.display-md}` | 120px | Alfa Slab One | 400 | 分节标题，二级 |
| `{typography.display-sm}` | 108px | Alfa Slab One | 400 | 贴近正文的宣言标题 |
| `{typography.stat-unit}` | 130px | Alfa Slab One | 400 | 统计旁的上标单位符号 |
| `{typography.quote-mark}` | 300px | Alfa Slab One | 400 | 装饰性超大引号 |
| `{typography.quote-body}` | 78px | Alfa Slab One | 400 | 引文正文 |
| `{typography.kpi-value}` | 88px | Alfa Slab One | 400 | KPI 或指标卡数值 |
| `{typography.subtitle}` | 72px | Alfa Slab One | 400 | 主标题旁的副标题或次级标题 |
| `{typography.card-title}` | 54px | Alfa Slab One | 400 | 卡片或栏标题 |
| `{typography.section-num}` | 54px | Alfa Slab One | 400 | 分节或条目序数数字 |
| `{typography.cta}` | 48px | Alfa Slab One | 400 | CTA 按钮标签 |
| `{typography.url}` | 46px | Alfa Slab One | 400 | URL 或联系地址 |
| `{typography.item-title}` | 38px | Alfa Slab One | 400 | 列表项或节点标题 |
| `{typography.toc-entry}` | 36px | Alfa Slab One | 400 | 目录条目标题 |
| `{typography.item-title-sm}` | 30px | Alfa Slab One | 400 | 密集列表项标题 |
| `{typography.stamp}` | 28px | Alfa Slab One | 400 | 印章或徽章标签 |

### 脚本比例

| Token | 尺寸 | 用途 |
|---|---|---|
| `{typography.script-lg}` | 96px | 醒目的手写强调，过渡词、情绪开场 |
| `{typography.script-md}` | 64px | 较小的手写旁注，副标题标注、子标签 |

两个脚本 token 都始终小写，且始终带 -2deg 到 -5deg 之间的旋转。绝不在不旋转的情况下用 Caveat Brush。

### 正文与标签比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.body-lg}` | 30px | Archivo Narrow | 500 | 统计注解、主正文段落 |
| `{typography.body-md}` | 28px | Archivo Narrow | 500 | 栏正文、导语段、比较列表 |
| `{typography.body-sm}` | 26px | Archivo Narrow | 500 | 辅助正文段落 |
| `{typography.body-xs}` | 24px | Archivo Narrow | 400 | 密集列表项、图注 |
| `{typography.label}` | 24px | DM Mono | 400 | 标准元数据标签（0.18em 字距） |
| `{typography.label-wide}` | 24px | DM Mono | 400 | 脚线与飘带文字（0.22em 字距） |
| `{typography.label-accent}` | 32px | DM Mono | 600 | 高亮元数据（如分节计数） |
| `{typography.signoff}` | 26px | DM Mono | 400 | 页脚署名块（0.20em 字距） |

### 排印原则
Alfa Slab One 始终全大写，绝不用句首大写式或小写。展示尺寸下行高紧：大标题 0.82–0.88，只有会撞行的多行贴正文文字才用 1.04。0.005em 字距几乎看不见，却能防止 100px+ 尺寸下字碰字。

堆叠 text-shadow 是展示文字的行内样式规则：橙色展示文字始终把 `{colors.red}` 投作第一层阴影。尺寸超过 200px 时，按双倍偏移加第二层 `{colors.red-deep}`。尺寸低于 100px 时，单单一层 3px–6px 的 `{colors.red}` 偏移就够。

DM Mono 标签无论什么语境都恒定 24px。字距按位置变化：顶条 / 页脚 0.18em、飘带与脚线 0.22em、分栏面板里的侧标签 0.16em。绝不给 DM Mono 减字距，24px 不加字距读起来是工具字，不像编辑字。

Archivo Narrow 始终字重 400 或 500。绝不在展示尺寸用它。它是辅助声部，不是标题声部。

## 布局

### 画布系统
每页 1920×1080px。`deck-stage` 自定义元素负责缩放。所有内容用绝对定位或 CSS grid，不滚动。

### 沟槽系统
- **幻灯片沟槽**（左右 90px）：多数内容分节的标准边距。
- **内容沟槽**（左右 120px）：页内已有结构头时给正文用，为阅读文字多留呼吸空间。
- **顶条高度**（90px）：绝对贴在页顶的固定高度蓝色顶条带。
- **画框内缩**（48px）：页边缘到蓝底页所用内嵌装饰画框边框的距离。

### 通用外壳
系统不强制每页都有通用顶条。存在两种外壳式样：

**顶条式样**：全宽 90px 蓝条锚在顶部（`position:absolute; top:0; left:0; right:0`）。内含 0.18em 字距的 DM Mono 24px 标签文字。带 6px 实奶油底边框。用于高强调蓝底页。

**分节断口式样**：头块与下方内容区之间一条 6px 实墨水平线。头块用左右 90px 内边距，下方内容也用 90px 内边距。没有顶条，这条线就是分隔元素。

两种式样可在同一页共存，也可各自独立使用。

## 纵深与层级

### 堆叠 text-shadow（主手法）
系统招牌。展示文字朝同一方向（右下）投分层偏移阴影，造出准 3D 凸版印刷效果。按元素尺寸分三档：

| 档 | 偏移层 1 | 偏移层 2 | 用途 |
|---|---|---|---|
| 小 | `3px 3px 0 {colors.red}` | — | 72px 以下的条目 |
| 中 | `5px–6px 5px–6px 0 {colors.red}` | — | 72px–140px 展示 |
| 大 | `10px 10px 0 {colors.red}, 20px 20px 0 {colors.red-deep}` | | 140px–260px 展示 |
| 特大 | `12px 12px 0 {colors.red}, 24px 24px 0 {colors.red-deep}` | | 260px+ 统计数字 |

橙色展示文字是"面"层，红是"身"，深红是"脚"。错觉是一个有物理厚度的字形。

### box-shadow（次级手法）
交互与装饰元素（印章、头像、CTA 按钮、KPI 卡片）以 box-shadow 形式用同一偏移逻辑：`6px 6px 0 {colors.red}` 或 `8px 8px 0 {colors.red}`。这让纵深系统统一：文稿里所有元素以同一视在光角朝同一方向投影。

### 颗粒纹理（氛围纵深）
每页带一个 `.grain::before` 伪元素：两张 3px 与 5px 间距的径向渐变点阵叠放，配 `mix-blend-mode: multiply`、50% 不透明度。这模拟丝网印刷的半调纹理，给平的数字表面一层物理的印刷质感。它不是抬升而是氛围，整份文稿读作被制作出来，而非被渲染出来。

### 扁平元素
DM Mono 标签、墨色分节线、正文、网格线完全扁平。结构分隔上不加阴影。

## 形状与处理

### 圆角比例
| 值 | 用途 |
|---|---|
| 999px（胶囊） | 顶条 / 头区里的元数据标签胶囊 |
| 50%（圆） | 头像元素、时间轴里程碑圆点、圆形印章 |
| 4px | 菱形项目伪元素（旋转 45deg 成菱形） |
| 0px | 全部结构元素：栏、卡片、顶条、画框、飘带、KPI 卡片、印章 |

系统几乎全方。仅有的柔和形状是胶囊（元数据小片）、圆（头像、圆点、收尾印章）、菱形项目。结构元素的方角强化印刷 / 构造美学。

### 边框粗细
- **6px 实 `{colors.ink}`**：主结构边框，分节分隔、栏分隔、顶条底边、内嵌画框、KPI 卡片边框、CTA 按钮边框。
- **6px 实 `{colors.cream}`**：蓝表面上的反色结构边框，内嵌画框、奶油压蓝模式下的顶条分隔。
- **5px 实**：次级结构边框，引文印章、比较列表项处理。
- **4px 实**：三级分隔，比较面板里的侧标签、导语左边框。
- **3px 实 `{colors.ink}`**：细结构线，目录行分隔、栏标记、统计来源分隔、时间轴内线。

### 装饰元素

**内嵌画框**：`inset: 48px` 处一条 6px 实奶油边框，在蓝底页上造出第二个内矩形。它强化海报 / 标牌美学，设计里套设计。

**橙色飘带**：底部锚定的 60px 条，`{colors.orange}` 填充、6px 墨顶边框、0.22em 字距的重复 DM Mono 文字。在数据页上当跑马灯页脚。

**菱形项目**：用 `::before` 伪元素做的列表项标记，24px × 24px，`background: {colors.red}`，`border-radius: 4px`，`transform: rotate(45deg)`。蓝底列表上改用 `{colors.orange}`。形状绝对定位在文字左侧 48px。

**圆形印章**：200px 圆（`{components.circular-stamp}`）旋转 -9deg，6px 橙边框、8px 红 box-shadow。充当封印，官僚文件上现实世界的批准标记。

**旋转矩形印章**：旋转 -3deg 的矩形块，5px 奶油边框、6px 红 box-shadow。内含 0.04em 字距的 Alfa Slab One 28px 文字。比圆形印章旋转更轻，像一张略微斜放的地址标签。

**脚本旁注**：Caveat Brush 64–96px、小写、旋转 2–5 度。始终出现在它所限定或打断的 Alfa Slab One 标题旁，绝不单独出现。

**栏序数**：180px Alfa Slab One 橙色数字配 5px 红 text-shadow，下方跟一条带 3px 墨顶边框的 DM Mono 标签。这对组合（大橙数字 + 小等宽标签）是系统标注栏或分节的标准方式。

**下划线**：14px 高的实墨矩形，宽为容器 30%，用作宣言标题后的句号。它比细线重，更接近涂黑条。

**颗粒叠层**：`.grain` 类给每页加 `::before` 伪元素纹理。本系统里它不能从页上移除，是美学的结构组成。

## 该做与不该做

### 该做
- 给每页套颗粒叠层（`.grain::before`）。它不是装饰，是其余一切印在上面的表面。
- 所有橙色与奶油展示文字都用堆叠 text-shadow。没阴影的 Alfa Slab One 读起来是平的，会丢掉凸版性格。
- 阴影偏移随字号成比例缩放：小字小偏移，超大字超大偏移。
- 红只作阴影色。红一旦成为文字色或背景填充，纵深系统就塌了。
- Caveat Brush 只在大尺寸（64px+）用，始终小写、始终略旋转。绝不用于正文。
- DM Mono 标签保持恰好 24px、至少 0.16em 字距。等宽字面用在正文尺寸、正常字距，读起来是代码，不是编辑。
- 主结构分隔用 6px 边框粗细。更细读作 SaaS，更粗像设计失误。
- 页用蓝背景时，用内嵌画框，把蓝底页区分为"带框"而非仅仅是"填色"。
- 在蓝表面上把 `{colors.orange}` 用作数字、数值、强调文字。深色表面上另两种许可的文字组合只有蓝压橙、奶油压蓝。

### 不该做
- 不要把红当背景或主文字色。它是阴影材料，不是表面材料。
- 不要在正文尺寸用 Caveat Brush，也不要不旋转就用。平而小的手写读作凌乱，不是刻意。
- 不要把 Alfa Slab One 用成混排。全大写锁定对板衬线的权威不可少。
- 不要软化边框粗细。结构元素上 1px 或 2px 边框会破掉印刷物美学。
- 不要给卡片或容器加圆角。内嵌画框与 KPI 卡片严格方正。
- 不要用 Archivo Narrow 做标题。它只是正文与导语字面，缺展示所需的视觉分量。
- 不要把 blue-deep 或 red-deep 当表面色。它们是只作阴影的值，角色是纵深，不是填充。
- 不要省掉列表项的菱形旋转。旋转 45deg 的方块是菱形，立正的方块是盒子，形状标示手工，不标示通用。
- 不要改变 DM Mono 字号。24px 是所有等宽标签文字唯一固定尺寸，为强调调大会破掉系统，唯一例外是 `{typography.label-accent}`（32px、字重 600）。

## 响应式行为

本模板专为 1920×1080 演示显示设计。`deck-stage` 自定义元素经 CSS transform 处理视口缩放，1920×1080 画布等比缩放到任意屏幕尺寸，布局不变。

翻页经 `deck-stage.js` 由键盘或演示翻页笔完成。无悬停态、无交互表单元素、无响应式断点。

打印与 PDF 导出：96dpi 下 1920×1080 画布对应 20×11.25 英寸画幅。颗粒叠层用 `mix-blend-mode: multiply`，PDF 导出时混合模式可能被压平，测试打印输出，并考虑在印刷格式里关掉颗粒。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字面 | 中文字面 | 字重 |
|---|---|---|---|
| 展示 / 标题 / 引文（Alfa Slab One 全大写） | Alfa Slab One | Noto Serif SC（思源宋体） | 900 |
| 脚本打断（Caveat Brush 小写旋转） | Caveat Brush | —（无合适对应，见美学提示） | — |
| 正文（Archivo Narrow 500） | Archivo Narrow | Noto Sans SC（思源黑体） | 500 |
| 标签 / 等宽（DM Mono 全大写加字距） | DM Mono | Noto Sans SC | 400（别强给 CJK 套等宽） |

### 混排策略

策略 A：把每个 token 的 `fontFamily` 扩展成拉丁字面之后跟中文字面。Alfa Slab token 变 `"Alfa Slab One, Noto Serif SC, serif"`；Archivo Narrow token 变 `"Archivo Narrow, Noto Sans SC, sans-serif"`；DM Mono token 变 `"DM Mono, Noto Sans SC, monospace"`。拉丁字形用原字面渲染，CJK 自动落到 SC 回退。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Caveat+Brush&family=Archivo+Narrow:wght@400;500;600;700&family=DM+Mono:wght@300;400;500&family=Noto+Serif+SC:wght@400;500;700;900&family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 设 0
- 文字变换：CJK 不用 uppercase
- 全角标点（，。：；！？「」（））
- 展示标题不加句号（中文排印惯例）
- 盘古之白（CJK 与拉丁之间加空格：`使用 Claude` 而非 `使用Claude`）
- 一句一款字体

### 本系统的美学提示

People's Platform 是建立在三款承重字面上的 WPA 海报系统，**三款没有一款能干净迁移到中文**。

**Alfa Slab One** 是极端尺寸（可到 540px）全大写的压缩板衬线。CDN 上没有分量与权威相当的中文板衬线。**Noto Serif SC 字重 900** 是最接近的匹配，它承载板状厚重与结构权威，但读起来更像"文学纪念碑"而非"抗议标牌"。接受这个语域偏移：这套系统的中文版更接近旧时代公共告示栏（想想大字报或博物馆标识），而非 1930 年代 WPA 海报。堆叠红 text-shadow 仍然适用，也仍承载系统的凸版纵深招牌。

**Caveat Brush** 是"人的打断"声部，小写、旋转、情绪温暖。**这迁移不到中文。** 中文毛笔书法（Ma Shan Zheng / 马善政）带文化与传统的分量，读作庄重、正式、甚至官僚，不是拉丁 Caveat 那种随意的个人声音。**推荐做法：纯 CJK 页上彻底去掉毛笔瞬间。** 第二个办法：即便在中文内容里，也用一个短的拉丁词以 Caveat Brush 作打断（例如中文标题旁一条脚本 `yes!` 旁注），这保住随意打断的能量、标示"声音切换"，又不牵动中文书法传统。

**DM Mono** 全大写加字距标签迁移不到 CJK。中文元数据设 **Noto Sans SC 400**、字距归 0、不用 uppercase。纯拉丁标签（URL、日期、版次号）保留 DM Mono。

**Archivo Narrow** 字重 500 为窄体。**Noto Sans SC 没有窄体变体。** 用原 Archivo 尺寸下的 Noto Sans SC 500，接受中文正文比拉丁正文略宽。单色纸画布与颗粒叠层会吸收这点宽度差。

堆叠 text-shadow（橙 → 红 → 深红）是系统最易认的特征。**它完美迁移到中文。** 给每条橙色中文展示标题套上，凸版纵深就能跨文字存活。蓝橙红配色也完全与文字无关。

菱形项目标记、旋转橡皮印章、内嵌奶油画框、6px 墨边框，在中文里全都原样成立。

### 已知 CJK 缺口

**Caveat Brush 没有可接受的中文对应。** 纯 CJK 的 People's Platform 文稿里，"人的打断"声部在结构上缺席。两个变通（彻底丢掉打断；脚本瞬间用中文里的拉丁词）都是看得见的美学妥协，这套民粹海报系统被逼进纯中文时会失去三声部之一。混排文稿（英文主导带中文点缀，或反过来）最贴这个模板。

## 迭代指南

1. 堆叠阴影是硬性的不变量，任何新的橙色或奶油展示元素都必须带。偏移按字号除以约 20 得第一层距离，翻倍得第二层。
2. 任何新的蓝底页都配内嵌画框（6px 奶油、`inset: 48px`），若带头条，头条用顶条式样配 6px 奶油底边框。
3. 新栏或并排面板遵循 6px 墨分隔惯例。非对称布局（如 60/40 分栏）可以，只要分隔边框保持 6px。
4. 新 KPI 或数据卡用 `{components.kpi-card}` 式样：5px 墨边框、纸背景、可选蓝色 alt 变体。里面数字用 Alfa Slab One 配标准 text-shadow。
5. 新列表项始终用菱形项目（24px × 24px、4px 圆角、rotate 45deg）。墨底条目用红，蓝底条目用橙。
6. 需要新装饰印章或徽章时，用 Alfa Slab One、`letter-spacing: 0.04em`、`6px 6px 0 {colors.red}` 的 box-shadow、轻微旋转（–3 到 –9deg）。圆形印章给 50% border-radius，矩形保持正方。
7. 颗粒叠层是 `section` 元素上的 CSS 伪元素，每张新页都必须经 `.grain` 类带上。
8. 脚本（Caveat Brush）文字是打断，不是默认。每页最多用一次，且只在 64px+。

## 已知缺口

- `deck-stage.js` 是外部脚本依赖，本文未记。翻页与缩放完全由它处理。
- 数据页上的橙色飘带用静态重复文字实现，没有 JavaScript 跑马灯动画。1920px 宽度下文字自然折行，更长的串需手工复制文字。
- 颗粒叠层用 `mix-blend-mode: multiply`。它要求半透明背景或带可见填充的父级才能产生纹理效果，在纯白或纯黑表面上效果可能看不见。
- 演讲者备注以 `<script type="application/json">` 块嵌在模板里，这类数据是呈现性的、不属于设计系统，未收进这些 token。
- Archivo Narrow 作为网络字体加载。它有宽泛的系统回退（`system-ui, sans-serif`），但系统字体栈回退的窄体宽度会与 Archivo Narrow 差很多，在紧凑网格配置下可能破掉布局。
- 引文文字上的 `text-wrap: pretty` 属性是现代 CSS 特性，浏览器支持有限，在较旧的导出环境里可能不生效。
