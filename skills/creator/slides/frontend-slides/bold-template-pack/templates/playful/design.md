---
version: alpha
name: Playful
description: "A warm, hand-crafted editorial system built on a peach-clay canvas with charcoal ink as the only \"color.\" Display type runs in Syne (weight 700–800, tight negative tracking); body type runs in Space Grotesk at weight 400–500. The aesthetic borrows from independent studio decks, risograph zines, and sketchbook spreads: organic blob frames, scribbled SVG doodles, slightly rotated cards, and double-stroke offset borders give every slide a hand-touched, unpolished warmth. The effect is creative-studio editorial, not corporate pitch — confident but human, structured but loose."

colors:
  bg: "#F0C8A0"
  bg-alt: "#E8B88E"
  light: "#F7DEC6"
  text: "#1A1A1A"

color-aliases:
  accent: text

typography:
  display-hero:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(4rem, 10vw, 9rem)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.03em
  display:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(3rem, 8vw, 7rem)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.02em
  headline:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(2.5rem, 6vw, 5rem)"
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.01em
  statement:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(2.5rem, 5vw, 4.5rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.01em
  title:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(2rem, 4vw, 3.5rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.01em
  title-sm:
    fontFamily: "Syne, sans-serif"
    fontSize: "1.3rem"
    fontWeight: 700
    lineHeight: 1.2
  number-hero:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(4rem, 8vw, 7rem)"
    fontWeight: 800
    lineHeight: 1.0
  number-md:
    fontFamily: "Syne, sans-serif"
    fontSize: "2.5rem"
    fontWeight: 800
    lineHeight: 1.0
  number-sm:
    fontFamily: "Syne, sans-serif"
    fontSize: "2rem"
    fontWeight: 800
    lineHeight: 1.0
  body:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "clamp(1rem, 1.2vw, 1.1rem)"
    fontWeight: 400
    lineHeight: 1.7
  body-md:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 500
    lineHeight: 1.6
  label-eyebrow:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  caption:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 500
    lineHeight: 1.4
  tag:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    lineHeight: 1.2

spacing:
  pad-slide-lg: "4rem 5rem"
  pad-slide-md: "3rem 4rem"
  pad-card-lg: "2rem 3rem"
  pad-card-md: "1.5rem"
  gap-lg: "3rem"
  gap-md: "2rem"
  gap-sm: "1.5rem"

canvas:
  width: 100vw
  height: 100vh

components:
  rough-box:
    border: "3px solid {colors.text}"
    background: "{colors.bg}"
    padding: "1.5rem"
    offsetShadowOffset: "6px 6px"
    offsetShadowBorder: "2–3px solid {colors.text}"
    description: "Generic content card with a double-stroke effect — the inner box has a 3px solid border, and an absolutely-positioned ::before pseudo-element offsets a second 2–3px border down-and-right by 6–8px to simulate a hand-drawn double outline. No fill on the offset; the canvas shows through."
  filled-block:
    background: "{colors.text}"
    color: "{colors.bg}"
    padding: "1.5rem"
    description: "Inverted card: dark charcoal background with peach text. Used as the visual counterpoint to outlined cards in a collage of mixed treatments."
  blob-frame-organic:
    border: "3px solid {colors.text}"
    borderRadius: "40% 60% 70% 30% / 40% 50% 60% 50%"
    description: "Organic outlined blob, asymmetric border-radius. Decorative wrapper that holds a smaller solid filled-blob inside it."
  blob-frame-pebble:
    border: "3px solid {colors.text}"
    borderRadius: "255px 15px 225px 15px / 15px 225px 15px 255px"
    description: "Pebble-shaped frame with extreme alternating border-radius — two opposing corners pulled long, the other two pinched short. Reads as a hand-drawn lozenge."
  blob-fill:
    background: "{colors.text}"
    borderRadius: "60% 40% 30% 70% / 60% 30% 70% 40%"
    description: "Solid dark blob with asymmetric organic radius. Used inside an outlined blob-frame or floating on its own as decorative mass."
  scribble-svg:
    stroke: "{colors.text}"
    strokeWidth: 2
    fill: none
    strokeLinecap: round
    description: "Inline SVG path drawn as a single hand-drawn line — wavy stub, scribbled circle, star outline, squiggle, arrow. Always 2px stroke, rounded caps. Placed absolutely in corners and edges as decorative breath."
  doodle-circle:
    border: "3px solid {colors.text}"
    borderRadius: "50%"
    description: "Plain round outlined circle used as a decorative anchor in slide corners."
  doodle-rect:
    border: "3px solid {colors.text}"
    rotation: "5–10deg"
    description: "Plain outlined rectangle, slightly rotated, used as a decorative anchor in slide corners."
  card-rotated:
    transform: "rotate(-3deg to 3deg)"
    description: "Any card or block can carry a small ±3deg rotation. Rotations stagger so adjacent cards rotate in opposite directions — never all in the same direction, never more than 3deg."
  step-node-circle:
    width: 64px
    height: 64px
    border: "3px solid {colors.text}"
    borderRadius: "50%"
    background: "{colors.bg}"
    fontFamily: "Syne, sans-serif"
    fontSize: 1.5rem
    fontWeight: 800
    description: "Round outlined node containing a single numeric digit at display weight. Used as a timeline or process marker; alternates between outlined (bg fill) and filled (charcoal fill, bg text)."
  avatar-placeholder:
    width: 60px
    height: 60px
    background: "{colors.text}"
    borderRadius: "50%"
    description: "Solid dark circle used as a portrait stand-in inside a team or people card."
  tag-pill:
    background: "{colors.text}"
    color: "{colors.bg}"
    padding: "0.4rem 0.8rem"
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    description: "Small charcoal pill with peach text, anchored to the bottom-left of an image frame as a category label."
  bar-chart:
    barFillSolid: "{colors.text}"
    barFillOutlined: "3px solid {colors.text} + transparent"
    axisStroke: "3px solid {colors.text}"
    description: "Custom HTML bar chart. Bars are either solid charcoal (primary series) or outlined transparent (secondary series). Axes are 3px solid charcoal lines, no grid."
  vertical-text:
    fontFamily: "Syne, sans-serif"
    fontWeight: 700
    letterSpacing: 0.1em
    transform: "rotate(90deg)"
    description: "Display-weight text rotated 90deg, anchored to a slide edge as a magazine-style spine label."
  ghost-blob:
    background: "{colors.text}"
    borderRadius: "40% 60% 70% 30% / 40% 50% 60% 50%"
    opacity: 0.08
    description: "Oversized organic blob at very low opacity placed behind content as atmospheric wallpaper. Functions like a watermark cloud."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/playful/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Playful 是一套**手作编辑系统**，锚定在单一暖画布上，桃黏土色 `{colors.bg}`（#F0C8A0），配炭色 `{colors.text}`（#1A1A1A）作唯一真正算数的"颜色"。一切都读作黏土纸上的墨。没有次级品牌色、没有渐变、没有彩色强调。系统彻底奉行单色纪律，把表现力放在形状、字重、旋转与手绘标记上，而不是配色变化里。

字体栈是 **Syne 作展示、Space Grotesk 作正文**。Syne 是个性，一款高对比展示无衬线，带古怪的人文比例，读作当代独立工作室声部，而非企业无衬线。它以字重 700 与 800、紧负字距（-0.01em 到 -0.03em）用于每个标题、陈述、统计、数字。Space Grotesk 是主力，一款稳定、中性的几何无衬线，正文用字重 400–500、标签用 500–600。这对搭配读作"可靠网格上长出的表现力编辑"。

色彩理念是**单色暖调**：单一墨色落在单一暖表面上，外加画布的两个色调兄弟（`{colors.bg-alt}` 略深，用于图片占位；`{colors.light}` 略浅，用于柔和分层）。桃色饱和到足以读作刻意的美学选择，而非中性色。墨从纯黑稍稍柔化到 #1A1A1A，好舒服地落在暖纸上。系统的情绪语域是"工作室速写本"，笃定却温暖，有结构却不打磨。

纵深靠**双描边偏移边框**与**手绘标记**，不靠模糊阴影。招牌处理是卡片上一条 3px 炭边框，加一个朝右下偏移 6–8px 的 `::before` 伪元素、带第二条 2–3px 边框，视觉效果是一道手绘双轮廓，像描得不完美。再配小旋转（卡片 ±0.5deg 到 ±3deg）与放在页角的涂鸦 SVG 路径，系统读起来像手工做的，而非软件渲的。

**密度取向：中低。** 每页由一个主导元素锚定，一句陈述、一张图表、一份名单，周围是刻意的呼吸空间加一两个装饰涂鸦。同时塞进卡片、涂鸦、文案会把手作感挤成杂乱。对的密度是每页一个实质瞬间，配一两个 SVG 涂鸦或有机色块在负空间里当视觉标点。

**关键特征：**
- 桃黏土画布（`{colors.bg}`）配炭墨（`{colors.text}`）作唯一颜色。无次级品牌配色。
- Syne 字重 700–800 配负字距用于每个展示与数字瞬间；Space Grotesk 400–500 用于正文。
- 卡片双描边偏移边框，3px 轮廓加经 `::before` 的 6–8px 偏移幽灵边框。
- 卡片、区块、统计带 ±0.5deg 到 ±3deg 小旋转，求手放感。
- 非对称 border-radius 的有机色块形状作装饰画框与填充。
- 行内 2px 描边 SVG 涂鸦（波浪、星、圆、箭头）住在页角，作手绘标点。
- 无网页阴影。纵深来自双边框、旋转、墨密度反差。
- 每页一个主导元素配宽裕负空间，绝不铺满到边。

## 颜色

### 调色板
- **背景**（`{colors.bg}` — #F0C8A0）：桃黏土画布。每页默认表面。饱和到足以成为系统招牌，又暖到让炭墨读起来柔和不刺。
- **背景 Alt**（`{colors.bg-alt}` — #E8B88E）：画布略深的色调兄弟。用作图片占位区填充，以及需要某张卡读作"在另一张后面"、又不想引入新颜色时的细微表面区分。
- **Light**（`{colors.light}` — #F7DEC6）：画布略浅的色调兄弟。区域需要靠单一色调台阶从背景抬起、又不引入白时，可用于柔和分层。
- **文字 / 墨**（`{colors.text}` — #1A1A1A）：炭墨，系统里唯一非画布色。从纯黑柔化，好作为暖墨落在暖纸上。用于全部正文、全部展示文字、全部边框、全部 SVG 描边、全部实心块、全部深色填充。

`accent` 别名解析到 `{colors.text}`，系统没有独立强调色。Playful 里的"强调"是对画布的反差，不是第三种色相。

### 默认值
- **默认表面背景**：`{colors.bg}`，每页都在桃黏土上开场。
- **默认标题色**：`{colors.text}`，始终如此。标题绝不着色或改色。
- **默认正文色**：`{colors.text}`，弱化时偶尔取 0.7–0.9 不透明度，但底色仍是炭。
- **默认边框色**：`{colors.text}`，每张描边卡片、色块、涂鸦、图表轴都是炭。
- **炭实心块上默认文字色**：`{colors.bg}`，深表面上的桃文字是唯一的颜色反转。
- **默认图片占位填充**：`{colors.bg-alt}`，比画布略深，让占位读成独立区域而不用白。
- **默认装饰色块填充**：全不透明度的 `{colors.text}`（前景），或 0.08 不透明度（内容背后的氛围幽灵色块）。

系统没有"主色对次色"的概念。每个视觉决定都是画布（桃）与墨（炭）之间的二元，靠不透明度、尺度、形状调制。

## 排印

### 字族
系统搭配两款精挑的 Google Fonts：

- **Syne**（展示）：当代人文展示无衬线，字形古怪、开口窄、比例略压缩。以字重 700 与 800 用于每个展示瞬间，标题、陈述、题目、数字、竖排标签。正是它的性格把 Playful 与一般暖调文稿区分开：Syne 读作独立工作室声部，不是企业页眉。
- **Space Grotesk**（正文）：干净、略几何的无衬线，带友好的人文暖意。字重 400–500 用于正文段落，500–600 用于标签与图注。给 Syne 的表现力一个稳定、易读的对重。

没有第三款字面。斜体与下划线不用。强调来自字重（700 → 800）、尺寸，以及 Syne 对 Space Grotesk 的反差本身。

### 排印比例

| Token | 尺寸（clamp） | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-hero}` | 4–9rem | Syne | 800 | 超大封面或开场日期 / 标题 |
| `{typography.display}` | 3–7rem | Syne | 800 | 收尾或主要宣言标题 |
| `{typography.headline}` | 2.5–5rem | Syne | 700 | 主分节标题 |
| `{typography.statement}` | 2.5–4.5rem | Syne | 700 | 长引述陈述或宣言行 |
| `{typography.title}` | 2–3.5rem | Syne | 700 | 区域或分节标题 |
| `{typography.number-hero}` | 4–7rem | Syne | 800 | 英雄统计数字 |
| `{typography.number-md}` | 2.5rem | Syne | 800 | 中尺度序数或统计数字 |
| `{typography.number-sm}` | 2rem | Syne | 800 | 行内序数或步骤数字 |
| `{typography.title-sm}` | 1.3rem | Syne | 700 | 小块里的卡片标题 |
| `{typography.body-md}` | 1.2rem | Space Grotesk | 500 | 副标题或强调正文 |
| `{typography.body}` | 1–1.1rem | Space Grotesk | 400 | 段落正文 |
| `{typography.label-eyebrow}` | 0.85rem | Space Grotesk | 600 | 标题上方的分节 eyebrow，全大写加字距 |
| `{typography.caption}` | 0.85rem | Space Grotesk | 500 | 副标题、细则、脚注 |
| `{typography.tag}` | 0.75rem | Space Grotesk | 600 | 炭标签里的胶囊标签文字 |

### 默认值
- **主分节标题默认尺寸**：`{typography.headline}`（2.5–5rem clamp）。
- **封面或主要开场瞬间默认尺寸**：`{typography.display-hero}`（4–9rem clamp）。
- **段落正文默认尺寸**：`{typography.body}`（1–1.1rem clamp）。
- **副标题或强调导语正文默认尺寸**：`{typography.body-md}`（1.2rem）。
- **任何行内图注、脚注、细则默认尺寸**：`{typography.caption}`（0.85rem）。
- **英雄数字默认尺寸**：`{typography.number-hero}`（4–7rem clamp）。
- **统计块或序数数字默认尺寸**：`{typography.number-md}`（2.5rem）。
- **任何展示元素（标题、陈述、题目、数字）默认字重**：700 或 800，绝不更低。
- **任何正文元素默认字重**：400 或 500。

页面主文字在 `{typography.title}` 与 `{typography.headline}` 间拿不准时，取 `{typography.headline}`，`{typography.title}` 留给页内子区域。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个展示元素都用 Syne。** 标题、陈述、题目、数字、竖排标签、装饰性单字标记，全是 Syne。大尺寸用 Space Grotesk 是错的系统信号。
- **每个 Syne 元素都用负字距**：按尺寸 -0.01em 到 -0.03em。Syne 用默认字距读作未处理，负字距才给展示文字紧致压缩的个性。
- **每个正文与标签元素都用 Space Grotesk。** Syne 排正文段读作用力过猛。
- **Eyebrow 标签全大写、0.15em 字距。** 没有全大写 + 加字距的标签读成正文碎片，不像标签。
- **统计与数字始终字重 800。** 连中尺度数字（2rem）也守展示字重惯例。字重 500 的数字读成库存清单，不像值得炫耀的数。
- **数字与统计作为独立统计项（而非在图表或表格里）时可带小旋转（±0.5deg 到 ±1deg）**。旋转强化手放感。

### 排印原则
系统的排印节奏来自 **Syne 对 Space Grotesk 的反差**，不是在一款字面里混字重。只用 Syne 换字重的页读起来单调，只用 Space Grotesk 的页低调到近乎企业。对的节奏是 Syne 标题 + Space Grotesk 正文，有纪律地重复。

行高：展示紧（0.85–1.1），正文宽（1.5–1.7）。绝不给正文用紧行高、给展示用宽行高，两种倒置都会破掉节奏。

本系统里斜体不存在。下划线不存在。强调靠换字面（正文 → 展示）或换字重（400 → 700）达成，绝不靠斜体。

## 布局

### 画布系统
系统以 `100vw × 100vh` 满视口为目标。每张 `.slide` 绝对定位铺满视口，只有 `.active` 页可见（opacity 1，其余 opacity 0）。翻页由 JS 驱动，方向键、空格、点击上一页 / 下一页按钮、触屏滑动。一条 4px 高的炭色进度条贴在视口底部，随页推进增长。所有尺寸用 `clamp()`，布局无需断点便流式缩放，直到 768px 的移动端重排。

### 内边距比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-slide-lg}` | 4rem 5rem | 封面、陈述、收尾页，宽裕外边距 |
| `{spacing.pad-slide-md}` | 3rem 4rem | 标准内容页外边距 |
| `{spacing.pad-card-lg}` | 2rem 3rem | 大卡片或联系块内部内边距 |
| `{spacing.pad-card-md}` | 1.5rem | 标准卡片内部内边距 |
| `{spacing.gap-lg}` | 3rem | 主区域间大网格 / flex 间隙 |
| `{spacing.gap-md}` | 2rem | 单元格间标准网格 / flex 间隙 |
| `{spacing.gap-sm}` | 1.5rem | 紧凑行内间隙 |

### 外壳
右下角一组固定 48px×48px 导航簇（上一页箭头、页码、下一页箭头，全以 2px 炭描边）。一条 4px 高炭色进度条齐平贴在视口底边。两者都不属于页面构图，它们是文稿常驻的放映外壳，不该拿来做样式参照。

进度条与导航按钮是仅有的常驻 UI 元素。页面自身在画布内不带顶条、不带页脚外壳、不带页码。

## 纵深与层级

### 双描边偏移边框（主手法）
招牌纵深处理是**双描边偏移边框**。卡片带一条 3px 实炭边框，一个绝对定位覆在卡片上的 `::before` 伪元素带第二条 2–3px 边框、朝右下偏移 6–8px。偏移边框无填充，画布透出来。视觉效果是一道手绘双轮廓，像笔在一道边上描了两次，暗示描得不完美。这是系统的抬升装置，取代多数系统会用 `box-shadow` 做的事。

### 旋转（次级手法）
卡片、区块、统计、装饰形状上的小旋转（±0.5deg 到 ±3deg）提供手放感。相邻元素间旋转方向交替，绝不让两张相邻卡朝同方向转，好暗示有人一件件手放，而非吸附到网格。

### 氛围幽灵色块
一个招牌处理：超大有机色块（`{components.ghost-blob}`）以 0.08 不透明度炭填充，绝对定位在页角作氛围壁纸。色块读作内容背后一朵柔和水印云。省着用，每页最多一个幽灵色块，锚在主内容不占的角上。

### 无网页阴影
系统用**零 `box-shadow` 模糊值、零 `drop-shadow`、零 rgba 阴影**。一切表观纵深来自双描边偏移边框、旋转、墨密度反差。任何元素上的模糊阴影都会破掉手作美学，标记该看着是画的，不是渲的。

## 形状与处理

### 圆角比例
| 值 | 用途 |
|---|---|
| 0px | 卡片、区块、标签、图片框、表格单元 |
| 50% | 圆头像占位、步骤节点圆、涂鸦圆 |
| 非对称有机（如 `40% 60% 70% 30% / 40% 50% 60% 50%`） | 仅色块画框与色块填充 |
| 卵石非对称（如 `255px 15px 225px 15px / 15px 225px 15px 255px`） | 仅卵石形画框 |

系统避开平滑的中等圆角（4px、8px、12px），角要么尖、要么全圆、要么有机色块状。中间地带读作通用网页应用，是错的信号。

### 边框粗细
- **3px 实 `{colors.text}`**：标准描边卡片与色块画框的边框粗细。
- **2–3px 实 `{colors.text}`**：`::before` 伪元素上偏移幽灵边框的粗细（比主线略细）。
- **3px 实 `{colors.text}`**：图表轴粗细（条形图的 X 与 Y 轴）。
- **2px 实 `{colors.text}`**：导航按钮边框粗细与时间轴轨道水平线。
- **2px 描边**：标准 SVG 涂鸦描边粗细，配圆形线端。

### 装饰元素类型

**粗盒卡片**：矩形内容卡，带招牌双描边偏移边框。背景可为画布桃（默认）或实炭（反色卡）。内边距取 `{spacing.pad-card-*}` 比例。可选小旋转（±0.5–3deg）。

**有机色块画框**：装饰性描边包装，带非对称 border-radius。作肖像框或装饰锚点，里面常装一块较小的实色块填充。两种特征形状：波浪有机色块（`{components.blob-frame-organic}`）与卵石形（`{components.blob-frame-pebble}`）。

**实色块填充**：带非对称 border-radius 的炭有机形状。可放在描边色块画框里（造出画框加质量块配对），也可单独浮动作装饰质量块。

**涂鸦 SVG**：行内 SVG 路径，画成单条 2px 描边炭线、圆线端。词表包括波浪短线、星轮廓、涂鸦圆、扭动波形、箭头、同心圆。绝对定位在页角或页边作装饰呼吸。每页至少一条涂鸦，最满的页带两三条。

**涂鸦圆 / 涂鸦矩形**：朴素描边圆或矩形，略旋转，绝对定位在页角作极简装饰锚点。是色块形状更简单的对位，页面需要视觉标点而色块显得太有机时用它。

**步骤节点圆**：64px 圆描边节点，内含一个 Syne 800 的数字。在描边（画布填充、炭数字）与实心（炭填充、画布数字）间按序交替，奇数步实心、偶数步描边，或任何一致式样。

**标签胶囊**：小炭矩形，配 0.75rem 字重 600 的桃文字。锚在图片框左下作类别标签。是唯一不是整张卡的反色"炭上文字"元素。

**竖脊标签**：1.5rem Syne 700 文字旋转 90deg，以 0.1em 字距锚在页右边缘。读作杂志书脊导视。

**幽灵色块壁纸**：0.08 不透明度的超大有机色块，绝对定位在页角作氛围壁纸。

**连接箭头涂鸦**：小的 SVG 手画箭头（单条 2px 线配 V 形箭头），在页负空间里暗示"下一页"或"另见"。

## 该做与不该做

### 该做
- 每个展示瞬间（标题、陈述、题目、数字、竖排标签）用 Syne，每段正文与标签用 Space Grotesk。两字面反差是系统的排印节奏。
- 给每个 Syne 元素套负字距（-0.01em 到 -0.03em）。Syne 用默认字距读作未处理。
- 给每张主内容卡套双描边偏移边框，3px 主轮廓加经 `::before` 的 6–8px 偏移幽灵边框。这是系统的招牌抬升装置。
- 每页至少一个角放一枚涂鸦 SVG 标记（扭动、星、圆、箭头）作手绘呼吸。标记是标点，不是内容。
- 给卡片、区块、统计一个 ±0.5–3deg 小旋转。相邻元素交替旋转方向，别让任何东西读成吸附到网格。
- 用 `{colors.text}`（炭）作唯一墨色。标题、正文、边框、涂鸦、填充，全是同一个色。
- 区域需要读成独立表面、又不引入白或新颜色时，取 `{colors.bg-alt}`。
- 让负空间呼吸。每页一个主导元素加一两个涂鸦，是对的密度。
- 需要肖像式装饰锚点时，把描边色块画框与里面较小的实色块填充配对。
- 负空间显空、而涂鸦又太小时，在页角放一个超大幽灵色块（0.08 不透明度炭）。

### 不该做
- 不要引入第三种颜色。系统只有桃画布 + 炭墨。无蓝、无红、无图表分段配色，图表条是实炭或描边炭，绝不上色。
- 不要用模糊 `box-shadow`。纵深全来自双边框与旋转。模糊阴影会立刻破掉手绘美学。
- 不要用中等 border-radius（4px、8px、12px）。角要么尖、要么全圆、要么有机色块状，中间没有。
- 不要用 Space Grotesk 做标题或展示瞬间。Syne 是个性字面，换成 Space Grotesk 会丢掉工作室声部。
- 不要用 Syne 排正文段。小尺寸、低字重下它读作用力过猛。
- 不要把元素旋转超过 3deg。超过 ±3deg，手放感就歪成业余。
- 不要把所有元素朝同一方向转。相邻元素交替 ± 方向，一致性读成"画布歪了"，不是手放。
- 不要用同时涌来的卡片、统计、涂鸦挤满页面。系统稀疏时读作贵，密集时读作坏。
- 不要用斜体或下划线强调。换字面或换字重。
- 不要把展示字重文字设成默认字距。始终把 Syne 用负字距收紧。

## 响应式行为

系统以 `100vw × 100vh` 为目标、通篇用 `clamp()`，字号与内边距在视口尺寸间流式缩放，无需媒体查询。单条 `max-width: 768px` 媒体查询把多列网格重排成单列、把横向时间轴轨道收成纵向、把页内边距降到 2rem。

### 放映行为
- `ArrowRight`、`Space`、`Enter` 前进。
- `ArrowLeft` 后退。
- 激活页带 `.active` 类，非激活页以 opacity 0 隐藏。
- 页间过渡用 0.6s opacity 淡入。
- 一条 4px 高炭色进度条贴在视口底部，随文稿推进增长。
- 右下导航簇显示上 / 下一页按钮（48px 描边方块）与当前 / 总页数计数器。
- 移动端横向触屏滑动前进 / 后退。

### 打印行为
没有定义 `@media print` 规则。文稿以网页 / 视口为先，不写自定义打印样式就打印不对。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字面 | 中文字面 | 字重 |
|---|---|---|---|
| 展示 / 标题 / 数字（Syne 700–800） | Syne | 站酷快乐体 ZCOOL KuaiLe | 400（唯一可用字重） |
| 正文 / 标签（Space Grotesk 400–600） | Space Grotesk | 悠哉字体 Yozai | 400 |

### 混排策略

策略 A：把每个 token 的 `fontFamily` 扩展成拉丁字面之后跟中文字面。Syne token 变 `"Syne, ZCOOL KuaiLe, sans-serif"`；Space Grotesk token 变 `"Space Grotesk, Yozai, sans-serif"`。拉丁字形用原字面渲染，CJK 字符自动落下。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Space+Grotesk:wght@400;500;600;700&family=ZCOOL+KuaiLe&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-yozai-regular/font.css" rel="stylesheet">
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

Playful 是建立在 Syne（古怪人文展示）加 Space Grotesk（暖几何正文）之上、落在桃黏土画布的手作编辑系统。中文迁移格外贴合，因为这里选的两款中文字面都带着与拉丁搭配相同的"温暖、手作、独立工作室"语域。

**站酷快乐体 ZCOOL KuaiLe** 是圆润、友好的中文展示字面，带古怪人文比例，是 CDN 上最接近 Syne 表现力工作室声部的对应。在展示尺寸（4–9rem）下，KuaiLe 读作当代独立中文工作室声部，而非企业或正式体。它与桃画布、炭墨天然相配。**中文展示要丢掉负字距（-0.01em 到 -0.03em）**，KuaiLe 按方形 em 框设计，收紧会造成字撞字。字面自带的暖意取代了负字距对 Syne 起的作用。

**悠哉字体 Yozai** 是为放松正文阅读设计的中文无衬线，终端略圆、人文比例友好，刻意去贴合 Space Grotesk 带给拉丁的暖意。每段中文正文与标签都设 Yozai 400。eyebrow 标签处理（拉丁里的 0.15em 字距 + 全大写）迁移不到 CJK；中文 eyebrow 用同样 0.85rem 的 Yozai，字距 0、无 uppercase，单靠小尺寸就读出标签感。

双描边偏移边框、±3deg 小旋转、有机色块形状、SVG 涂鸦、幽灵色块壁纸，都与文字无关。单色纪律（桃 + 炭）与手作美学能完整跨文字存活。

系统的排印节奏（Syne 对 Space Grotesk 反差）在纯中文里变成（KuaiLe 对 Yozai 反差），两对都带着同样的"可靠网格上长出的表现力编辑"节奏。统计与数字是纯数字，在 Syne 800 里原样迁移，只有统计带中文单位后缀（`亿`、`万`）时后缀字形才落到 KuaiLe。

### 已知 CJK 缺口

ZCOOL KuaiLe 与 Yozai 都是单字重字面（400）。系统对字重反差的依赖（子展示层级用 Syne 700 对 800，标签层级用 Space Grotesk 400 对 500 对 600）在纯中文里塌成只靠尺寸的层级。这不算有意义的损失，Playful 的层级本就主要由尺寸驱动，缺的字重档不足以改变视觉节奏。旋转、涂鸦、双边框处理无论字重是否可用都扛着系统的性格。

## 迭代指南

1. 任何新卡片都用粗盒式样：3px 炭边框、桃背景（或反色时炭）、内边距取 `{spacing.pad-card-*}`，加一个朝右下偏移 6–8px、2–3px 粗细的 `::before` 幽灵边框。
2. 任何新卡片都带小旋转（±0.5–3deg）。与邻卡交替旋转方向，绝不让所有卡对齐同一角度。
3. 任何新标题都用 Syne 字重 700–800 配负字距。标题若是页面主瞬间，取 `{typography.headline}` 或 `{typography.display}`，别取 `{typography.title}`（那是子区域尺度）。
4. 任何新正文或标签都用 Space Grotesk 字重 400–600。标题上方的小标签用 `{typography.label-eyebrow}`（0.85rem、字重 600、全大写、0.15em 字距）。
5. 任何新统计或数字都用 Syne 字重 800 配负字距。连小数字（2rem）也守展示字重惯例。
6. 任何新页都至少在页角放一枚涂鸦 SVG 标记，扭动、星、圆、箭头。描边 2px、圆形线端、`{colors.text}` 色。
7. 任何装饰形状都用非对称有机 border-radius（色块）、尖 0px（矩形）或 50%（圆）。避开中等圆角。
8. 页面负空间显重时，加一个幽灵色块（0.08 不透明度炭、超大有机形状），锚在内容不占的角上。
9. 图表（条形、环形、折线）只用 `{colors.text}` 与 `{colors.bg-alt}` 作填充。不要引入彩色图表配色。
10. 卡片可描边（默认，画布填充、炭边框、炭文字）或反色（炭填充、桃文字）。反色卡是系统的强调装置，留给那个要锚住页面注意力的格子。

## 已知缺口

- 系统经网络加载两款 Google Fonts（Syne、Space Grotesk）。字体加载失败时无衬线回退仍会渲染，但系统声部会丢。生产环境建议自托管。
- 双描边偏移边框（带 6–8px 偏移的 `::before`）要求父卡片有 `position: relative`，且伪元素在视觉上落在卡片边界框加偏移之内。靠近页边的卡片，偏移边框可能被裁掉。
- 768px 移动端断点只重排网格，不调整绝对定位的装饰 SVG 与色块，它们仍停在桌面坐标，小视口上可能重叠或跑出屏幕。把响应式当作基础级，别当打磨过的。
- 桃画布（#F0C8A0）带很强的文化语域（土气、暖、略质朴）。它与冷调品牌配色不搭，也不能拿中性奶油或白替换，这份暖是地基。
- 图片占位（`{colors.bg-alt}` 填充配居中 "IMG 01" 标签）只是桩。生产文稿需要尊重暖配色的真实图片，冷调照片会跟画布打架。
- 没有定义深色模式变体。系统单模式（仅暖桃画布）。
- 导航按钮的悬停态（背景填成炭、文字反转成桃）是放映外壳的交互行为，不属于文稿的页面构图。
