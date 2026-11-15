---
version: alpha
name: BlockFrame
description: "A maximalist neobrutalist presentation system built on 4px solid black borders, 8px hard offset shadows, and a high-key candy palette of five saturated pastels plus cream and off-white. Display type runs Inter at weight 800-900 in tight uppercase; secondary chrome uses Space Grotesk as a quasi-monospace label face. Tilted decorative shapes (rotated stars, rectangles, badges) puncture the borders and break the grid intentionally. Pastels are paired loudly: pink + blue + green + yellow + cream cycle through every region with deliberate juxtaposition. The aesthetic borrows from zine layout, 1990s-revival sticker books, and contemporary toy packaging — bold, joyful, slightly chaotic, never timid."

colors:
  black: "#000000"
  white: "#FFFFFF"
  offwhite: "#FFFDF5"
  pink: "#FE90E8"
  blue: "#C0F7FE"
  green: "#99E885"
  yellow: "#F7CB46"
  cream: "#FFDC8B"

borders:
  primary: "4px solid {colors.black}"
  thin: "3px solid {colors.black}"

shadows:
  default: "8px 8px 0px {colors.black}"
  small: "4px 4px 0px {colors.black}"
  hover: "6px 6px 0px {colors.black}"
  close-yellow: "12px 12px 0px {colors.yellow}"
  close-white: "6px 6px 0px {colors.white}"

typography:
  heading-xl:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: "clamp(48px, 6vw, 96px)"
    lineHeight: 0.95
    letterSpacing: -0.03em
    textTransform: uppercase
  heading-lg:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 800
    fontSize: "clamp(32px, 4vw, 64px)"
    lineHeight: 1
    letterSpacing: -0.02em
    textTransform: uppercase
  heading-md:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 700
    fontSize: "clamp(24px, 2.5vw, 40px)"
    lineHeight: 1.1
    letterSpacing: -0.01em
  close-title:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: "clamp(40px, 5vw, 80px)"
    lineHeight: 0.95
    letterSpacing: -0.03em
    textTransform: uppercase
  quote-text:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: "clamp(28px, 3.5vw, 52px)"
    lineHeight: 1.15
    letterSpacing: -0.02em
    textTransform: uppercase
  stat-number:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: "clamp(36px, 4vw, 64px)"
    lineHeight: 1
  card-title:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 700
    fontSize: 22px
    lineHeight: 1.2
    textTransform: uppercase
  step-num:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: 48px
    lineHeight: 1
  body:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 500
    fontSize: "clamp(16px, 1.2vw, 20px)"
    lineHeight: 1.6
  body-card:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 500
    fontSize: 15px
    lineHeight: 1.6
  list-body:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 500
    fontSize: 16px
    lineHeight: 1.5
  label:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 600
    fontSize: 13px
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  mono-tag:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 600
    fontSize: 14px
    lineHeight: 1
    letterSpacing: 0.05em
    textTransform: uppercase
  mono-meta:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 500
    fontSize: 15px
    letterSpacing: 0.02em
  subtitle-mono:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 500
    fontSize: 18px
    lineHeight: 1.5
  counter:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 700
    fontSize: 14px
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  legend-item:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 600
    fontSize: 13px

spacing:
  slide-pad: 60px
  card-pad-lg: 60px
  card-pad-md: 36px
  card-pad-sm: 28px
  card-pad-xs: 22px
  gap-lg: 48px
  gap-md: 32px
  gap-sm: 24px
  gap-xs: 16px
  pad-bottom-clearance: 110px

canvas:
  width: 100vw
  height: 100vh
  default-background: "{colors.offwhite}"

components:
  card-elevated:
    border: "4px solid {colors.black}"
    background: "{colors.white}"
    boxShadow: "{shadows.default}"
    description: "Primary elevated card. 4px ink border + 8px ink offset shadow. Background is white by default; on darker surfaces background may shift to offwhite or to a colored fill."
  card-flat:
    border: "4px solid {colors.black}"
    background: "{colors.white}"
    description: "Bordered card without elevation shadow. Used for secondary content cells inside multi-card grids where the shadow would compound."
  card-small:
    border: "3px solid {colors.black}"
    background: "{colors.white}"
    boxShadow: "{shadows.small}"
    description: "Compact card with thinner border + smaller offset shadow. Used for intro-cards, stat-cards, team-cards, and timeline-steps."
  label-pill:
    border: "3px solid {colors.black}"
    padding: "6px 16px"
    fontFamily: "'Space Grotesk', monospace"
    fontSize: 13px
    fontWeight: 600
    letterSpacing: 0.08em
    textTransform: uppercase
    background: "{colors.white}"
    boxShadow: "{shadows.small}"
    description: "Universal section eyebrow. White base by default; pink, blue, green, yellow, cream variants swap background. Always sits on a 3px black border with a 4px hard offset shadow."
  button-primary:
    border: "3px solid {colors.black}"
    background: "{colors.yellow}"
    color: "{colors.black}"
    padding: "14px 32px"
    fontFamily: "'Inter', sans-serif"
    fontWeight: 700
    fontSize: 16px
    boxShadow: "{shadows.small}"
    description: "Primary CTA. Yellow fill with black text, 3px black border, 4px offset shadow. Hover lifts the button -2/-2 and grows shadow to 6px."
  corner-bracket:
    width: 24px
    height: 24px
    border: "3px solid {colors.black}"
    description: "Two L-shaped brackets at opposite corners of a card or frame (tl + br + tr + bl pattern available). Sits inside the card edge as a decorative frame-within-frame."
  icon-square:
    width: 64px
    height: 64px
    border: "3px solid {colors.black}"
    description: "Solid pastel square (pink/blue/green) holding a single uppercase letter glyph at weight 700 / 28px. Used as feature-card icons."
  feature-deco:
    width: 48px
    height: 48px
    border: "3px solid {colors.black}"
    background: "{colors.yellow}"
    position: "absolute top -12px right 24px"
    description: "Yellow square notch that protrudes from the top edge of a feature card, breaking the card's top border line."
  stat-deco-dot:
    width: 12px
    height: 12px
    borderRadius: 50%
    border: "2px solid {colors.black}"
    description: "Small black-bordered colored circle pinned to the top-right of a stat card. The only round shape used on cards. Fill cycles through the pastel palette."
  avatar-square:
    width: 72px
    height: 72px
    border: "3px solid {colors.black}"
    background: "{colors.pink}"
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: 28px
    textTransform: uppercase
    description: "Square avatar with two-letter initials, used in team grids. Fill cycles through the pastel palette."
  list-number:
    width: 36px
    height: 36px
    border: "3px solid {colors.black}"
    background: "{colors.yellow}"
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 700
    fontSize: 14px
    description: "Square numerical bullet pinned to the left of each list item. Black border, yellow fill, mono numeral."
  star-burst:
    clipPath: "polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)"
    border: "3px solid"
    background: "{colors.pink}"
    description: "10-point star clipped via CSS clip-path with a 3px border. Decorative attention-grabber pinned to corners of close-frames and feature cards."
  stripe-block:
    background: "repeating-linear-gradient(45deg, {colors.black}, {colors.black} 4px, {colors.green} 4px, {colors.green} 12px)"
    border: "3px solid {colors.black}"
    description: "Black-and-color diagonal stripe panel used as decorative attention block on poster-class surfaces."
  bg-dot-grid:
    backgroundImage: "radial-gradient(circle, {colors.black} 1.2px, transparent 1.2px)"
    backgroundSize: "24px 24px"
    description: "Faint dot-grid background pattern used as an overlay on light surfaces or as decoration in corners of cards."
  tilt-card:
    transform: "rotate(±2deg) or rotate(±8deg)"
    description: "Card with intentional tilt. Stat cards alternate -2deg / +2deg; decorative rectangles tilt up to ±12deg. The tilt is the system's playful structural signature."
  nav-btn:
    width: 48px
    height: 48px
    border: "3px solid {colors.black}"
    background: "{colors.white}"
    boxShadow: "{shadows.small}"
    description: "Square nav arrow button. Hover translates -2/-2 and grows shadow; active translates 2/2 and shrinks shadow."
  slide-counter:
    border: "3px solid {colors.black}"
    background: "{colors.white}"
    padding: "10px 18px"
    boxShadow: "{shadows.small}"
    description: "Persistent slide counter pill at bottom-left. Space Grotesk uppercase NN / NN format."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/block-frame/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

BlockFrame 是一套**极繁的新粗野主义演示系统**，建立在五条结构定律上：每个区域都有 4px 黑边、每个抬升元素都有 8px 硬边偏移阴影、每个角都是方角、每种强调色都是饱和浅彩、每个布局都允许稍微歪一点。系统的乐趣来自这些定律的刻意碰撞：带框卡片撞带框卡片，阴影叠阴影，倾斜装饰有意破开网格。

字体系统以 **Inter**（字重 400-900）为轴，兼顾展示、正文与统计：标题用字重 800-900、紧大写、负字距；正文用字重 500 句首大写；卡片标题用字重 700 大写。**Space Grotesk**（字重 400-700）是次级字面，作准等宽的标签声部，用于眉题、页码、统计标签、等宽小片，以及任何该读成"系统"而非"编辑"的外壳。字面组合刻意普通，两款都是随处可得的开源无衬线，但处理方式（重磅大写 Inter + 宽字距 Space Grotesk）赋予了它们鲜明的新粗野主义语域。

配色围绕**五种饱和浅彩**（粉 `#FE90E8`、蓝 `#C0F7FE`、绿 `#99E885`、黄 `#F7CB46`、奶油 `#FFDC8B`）加**纯黑**（`#000000`）作边框与文字、**白**（`#FFFFFF`）作干净卡片填充、**米白**（`#FFFDF5`）作暖画布。浅彩不是微妙点缀，而是满出血的表面填充。典型演示文稿让每一页轮过不同色底（米白封面 → 蓝导言 → 米白内容 → 绿图表 → 粉引文 → 黄分栏 → 米白时间轴 → 蓝统计 → 奶油团队 → 黑收尾）。这种换色循环是系统的主节奏。

纵深是 **4px 与 8px 的硬边偏移阴影**，始终纯黑、始终零模糊、始终落在右下。大元素用 8px，小外壳用 4px。收尾框用单枚 12px 的**黄色**偏移（系统里唯一的彩色阴影），是系统最响的纵深表态；反色收尾框则在黑表面上配 6px **白色**阴影。主卡片边框 4px 实线黑，次级外壳 3px 实线黑。边框粗细与阴影尺寸紧密绑定：4px 边配 8px 阴影，3px 边配 4px 阴影。

**密度取向：舒适地密。** 这套系统填满时显得权威，稀疏时显得怯。典型一页承载：label-pill 眉题 + 一个大标题 + 多卡片网格（3-6 张）+ 至少一个装饰元素（倾斜矩形、星爆、条纹块、角标、装饰点）。区域内的空白读起来像"坏了"，每张卡片都该填满，每个网格都该排满。系统的乐趣依赖许多带框物件在同一画面里的视觉喧闹。

**关键特征：**
- 主卡片 4px 实线黑边，次级外壳 3px，绝不更细。
- 主卡片 8px 硬边偏移阴影，次级外壳 4px，纯黑、零模糊。
- 五浅彩配色（粉、蓝、绿、黄、奶油）加黑、白、米白，跨表面轮转。
- Inter 字重 800-900 大写配负字距是展示声部；Space Grotesk 字重 600 大写配 0.08em 字距是标签声部。
- 处处方角，唯一例外是统计卡片上的一枚圆形点缀点。
- 倾斜装饰元素（旋转矩形、星星、徽章）有意破开网格。
- 标签胶囊（`{components.label-pill}`）带 3px 边、4px 偏移阴影和浅彩填充变体，是通用分节眉题。
- 彩色填充大胆饱和，浅彩用作面板底，不是轻点缀。
- 黄色是默认 CTA 色，黑色是默认收尾表面色。
- 星爆、条纹块、点网格是可复用的装饰注意力单元。

## 颜色

### 调色板

- **Black**（`{colors.black}` — `#000000`）：结构色。每一条边、每一个主文字瞬间、每一处阴影。纯黑，无暖偏。系统的对比锚点。
- **White**（`{colors.white}` — `#FFFFFF`）：默认卡片填充。每张主卡片、标签胶囊与导航按钮的底。纯白，无暖意。
- **Off-white**（`{colors.offwhite}` — `#FFFDF5`）：暖画布色。没有浅彩底在用时，是默认的正文/幻灯片背景。比纯白略暖，好让压在上头的白卡片仍有层次感。
- **Pink**（`{colors.pink}` — `#FE90E8`）：高明度糖果洋红。用作整片表面底、标签胶囊填充、icon-square 填充、星爆填充，以及浅彩图表系列之一。五浅彩里最饱和的一色。
- **Blue**（`{colors.blue}` — `#C0F7FE`）：淡青冰蓝。用作整片表面底（"导言"与"统计"感）、标签胶囊填充、icon-square 填充，以及一个图表系列。
- **Green**（`{colors.green}` — `#99E885`）：明亮春绿。用作整片表面底、标签胶囊填充、icon-square 填充、stripe-block 斜纹图案，以及一个图表系列。
- **Yellow**（`{colors.yellow}` — `#F7CB46`）：CTA 色。用作默认按钮填充、收尾框阴影色、list-number 方块、feature-deco 缺口、标签胶囊填充。最亮、最抓眼的浅彩。
- **Cream**（`{colors.cream}` — `#FFDC8B`）：暖黄奶油。比黄柔，比米白饱和。用作整片表面底（"团队"或"封面"感）、标签胶囊填充，以及三级图表强调。

### 默认值

- **默认表面背景**：内容多的表面用 `{colors.offwhite}`；需要更强底色的表面轮用 `{colors.cream}`、`{colors.blue}`、`{colors.pink}`、`{colors.green}`、`{colors.yellow}`。循环就是节奏，连着多页停在一个底色会把系统压平。
- **默认标题色**：所有浅/浅彩表面上用 `{colors.black}`；黑色收尾表面上用 `{colors.white}`。
- **默认正文文字色**：所有浅/浅彩表面上用 `{colors.black}`；深色表面上用 `{colors.white}` 或 `{colors.cream}`。
- **默认边框色**：`{colors.black}`，始终如此。除反色收尾框的 4px 白边外，哪里都没有彩色边框。
- **默认卡片填充**：`{colors.white}`。只有当卡片属于多卡一行、每张都需要独立色彩身份时，才用浅彩填充（例如时间轴步骤行，每步一个浅彩）。
- **默认按钮填充**：`{colors.yellow}`。别的浅彩也行，但黄色是系统主要的"点这里"信号。
- **默认标签胶囊基色**：`{colors.white}`；浅彩变体（`{colors.pink}`、`{colors.blue}`、`{colors.green}`、`{colors.yellow}`、`{colors.cream}`）用来标示分节类型或装饰眉题。
- **统计卡片上的默认装饰点缀**：一枚 12px 圆（`{components.stat-deco-dot}`），浅彩填充，在卡片间轮用粉、蓝、绿、黄。
- **默认图表配色顺序**：粉 → 蓝 → 绿（三系列），黄与奶油可作额外系列。

浅彩在角色上可互换，谁都不带固定语义（绿不是"成功"，红根本不在配色里）。按视觉并置来配：粉 + 蓝 + 绿是最常见的三色组，奶油 + 黄是暖对，蓝 + 粉是冷暖对比。

## 排印

### 字族栈
系统用两款字面。

**Inter**（字重 400-900）是展示、正文、标题、统计字面。英雄/收尾标题与引文文字用字重 900，主标题用字重 800，中级标题与卡片标题用字重 700，正文用字重 500。展示字重始终大写配负字距（-0.02 到 -0.03em）；正文字重始终句首大写、默认字距。重磅大写展示与字重 500 句首正文之间的反差，是系统的排印节奏。

**Space Grotesk**（字重 400-700）是标签兼外壳字面。字重 600 用于标签胶囊（13px、0.08em 字距、大写），字重 500 用于等宽元数据标注。这款字面严格说不是等宽，但略带几何的性格加宽字距处理，让它读起来像系统的"代码"声部。

不要引入第三款字面。Inter + Space Grotesk 的搭配就是全部排印配色。

### 排印比例

| Token | 尺寸（clamp / px） | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.heading-xl}` | 48–96px clamp | Inter | 900 | 英雄或封面级标题 |
| `{typography.heading-lg}` | 32–64px clamp | Inter | 800 | 分节主标题 |
| `{typography.heading-md}` | 24–40px clamp | Inter | 700 | 区域标题、图表标题 |
| `{typography.close-title}` | 40–80px clamp | Inter | 900 | 收尾陈述标题（反色表面） |
| `{typography.quote-text}` | 28–52px clamp | Inter | 900 | 引文正文，始终大写 |
| `{typography.stat-number}` | 36–64px clamp | Inter | 900 | 统计数字 |
| `{typography.card-title}` | 22px | Inter | 700 | 特性卡片标题，大写 |
| `{typography.step-num}` | 48px | Inter | 900 | 时间轴步骤内的数字（不透明度 0.6） |
| `{typography.body}` | 16–20px clamp | Inter | 500 | 标准正文段落 |
| `{typography.body-card}` | 15px | Inter | 500 | 紧凑卡片内正文 |
| `{typography.list-body}` | 16px | Inter | 500 | 编号列表正文 |
| `{typography.label}` | 13px | Space Grotesk | 600 | 标签胶囊内文字 |
| `{typography.mono-tag}` | 14px | Space Grotesk | 600 | 等宽小片/徽章、页码 |
| `{typography.mono-meta}` | 15px | Space Grotesk | 500 | 行内等宽元数据 |
| `{typography.subtitle-mono}` | 18px | Space Grotesk | 500 | 英雄副标题 / 收尾副标题 |
| `{typography.counter}` | 14px | Space Grotesk | 700 | 常驻页码（NN / NN） |
| `{typography.legend-item}` | 13px | Space Grotesk | 600 | 图表图例标签 |

### 默认值

- **英雄或封面标题默认尺寸**：`{typography.heading-xl}`（48–96px）。始终大写、始终字重 900、始终 -0.03em 字距。
- **分节主标题默认尺寸**：`{typography.heading-lg}`（32–64px）。大写、字重 800、-0.02em。
- **区域或图表标题默认尺寸**：`{typography.heading-md}`（24–40px）。唯一默认不大写的 Inter 标题，不过允许大写。
- **统计数字默认尺寸**：`{typography.stat-number}`（36–64px）。字重 900、行高 1。
- **正文段落默认尺寸**：`{typography.body}`（16–20px clamp）。字重 500、句首大写、行高 1.6。
- **眉题标签默认尺寸**：装在 `{components.label-pill}` 里的 `{typography.label}`（13px）。
- **任何 Inter 展示默认字重**：800 或 900。Inter 展示用字重 700 读起来"差一口气"；700 只留给 `{typography.heading-md}` 或卡片标题。
- **任何 Inter 正文默认字重**：500。正文 400 太轻，700 太大。
- **任何 Space Grotesk 标签/外壳默认字距**：0.05-0.10em。宽字距是这款字面的"外壳"信号。
- **任何 Inter 展示默认字距**：-0.01em（heading-md）到 -0.03em（heading-xl）。展示没有负字距会显得没处理过。

拿不准该用哪个标题 token 时，页面主要文字瞬间默认取 `{typography.heading-lg}`（32–64px）。`{typography.heading-md}` 留给页内的区域或图表标题。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每个 Inter 展示元素（heading-xl、heading-lg、quote-text、close-title）都大写。** 系统里不存在字重 800+ 的句首大写 Inter 展示。大写 + 重磅 + 负字距的组合就是视觉身份。
- **每个 Inter 展示元素都用负字距**（-0.01 到 -0.03em）。展示没有负字距会读成默认 Inter，那是根本不同的美学。
- **每个标签胶囊都带 3px 边 + 4px 阴影 + 大写 Space Grotesk 文字**的组合。缺了三者任一的标签不算标签胶囊，只是一段游离文字。
- **每个 card-title 都是大写 Inter 字重 700。** 句首大写的卡片标题会破掉粗野节奏。
- **每个 Space Grotesk 标签/外壳/计数器都大写、0.05-0.1em 字距。** 系统里不存在句首大写的 Space Grotesk，例外只有贴近正文的元数据（mono-meta、行内等宽）。
- **每个统计数字都是 Inter 字重 900、行高 1。** 统计数字是展示瞬间，不是数据外壳。
- **每个 Inter 正文块都句首大写、行高 1.6（紧凑卡片正文 1.5）。** 正文大写或行高偏紧会读成坏了。
- **时间轴步骤卡片内的步骤数字是 48px、字重 900、不透明度 0.6。** 降低不透明度是强制的，全不透明的步骤数字会压过步骤标题。

### 排印原则

声部对比是**重磅大写展示 ↔ 句首正文 ↔ 宽字距标签**。不用斜体，不用下划线。唯一的强调机制是 Inter 阶梯内的字重反差，以及大写/句首大写的切换。

展示元素应当**主导画布**。系统为海报级排印而生，把 heading-xl 缩到很小会抹掉它的性格。尽量取每个 clamp 的上界。

## 布局

### 画布系统
系统以每页 `100vw × 100vh` 为目标。幻灯片绝对定位，靠 `.active` 类上的 `display: none` / `display: flex` 切换。默认幻灯片内边距四边 60px。含底部锚定网格的页面（时间轴、团队网格、带统计列的图表）另加 `padding-bottom: 110px`，给常驻页码和导航控件外壳让位。

默认幻灯片 flex 方向为 column、`justify-content: center`。双栏分栏（导言页、图文分栏）切换到 row。

### 内边距与间隙比例

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.slide-pad}` | 60px | 默认幻灯片边缘到内容的内边距 |
| `{spacing.card-pad-lg}` | 60px | 英雄框与引文框内部内边距 |
| `{spacing.card-pad-md}` | 36px | 特性卡片内部内边距 |
| `{spacing.card-pad-sm}` | 28px | 导言卡片内部内边距 |
| `{spacing.card-pad-xs}` | 22px | 团队卡片与小单元格内边距 |
| `{spacing.gap-lg}` | 48px | 主分节之间（页眉到网格）的间隙 |
| `{spacing.gap-md}` | 32px | 特性卡片之间的间隙 |
| `{spacing.gap-sm}` | 24px | 导言卡片、统计卡片之间的间隙 |
| `{spacing.gap-xs}` | 16px | 列表项内、卡片内内容之间的间隙 |
| `{spacing.pad-bottom-clearance}` | 110px | 给固定导航外壳让位的底部内边距预留 |

### 常驻外壳
每页都出现三个元素：
- **页码**在左下：3px 黑边、白填充、4px 阴影、Space Grotesk 14px 字重 700 大写、NN / NN 格式。
- **导航控件**在右下：两枚 48px 方形导航按钮，带 3px 边、白填充、4px 阴影。
- 页码与导航控件不属于幻灯片构图，它们活在 `.slides-container` 之外，压在底边上。

### 卡上叠卡结构
系统主要的布局模式是**底上的底上的卡片**。典型一页放一张浅彩色底表面，其上坐一张带 4px 黑边 + 8px 阴影的白卡片，卡内还可以装更小的卡片或 icon-square。每一层嵌套自带边框粗细：外层卡片 4px，内层外壳 3px。正是这种嵌套带框结构，给了系统密实、填满的观感。

### 装饰性破局
倾斜装饰元素（旋转矩形、星星、徽章、点网格）绝对定位在页面与卡片表面上，有意破开网格。它们不是"背景装饰"，而是构图的一部分。没有任何装饰元素的表面读起来太干净。

## 纵深与层级

### 硬边偏移阴影栈
系统用三种主要阴影值：
- **`{shadows.default}`** = `8px 8px 0px {colors.black}`：主卡片阴影。用于英雄框、特性卡片、引文框、图表框，以及任何抬升卡片。
- **`{shadows.small}`** = `4px 4px 0px {colors.black}`：次级外壳阴影。用于导言卡片、统计卡片、团队卡片、时间轴步骤、标签胶囊、button-primary、nav-btn、页码。
- **`{shadows.hover}`** = `6px 6px 0px {colors.black}`：按钮与导航的悬停态，配 -2/-2 变换触发。

所有阴影纯黑、零模糊、固定右下偏移。悬停时阴影 + 变换的搭配造出"从纸面抬起"的交互签名：元素平移 -2/-2，阴影长到 6/6，模拟被揭起。

### 反色阴影
在深色收尾表面上，阴影反转颜色但保留偏移逻辑：
- **`{shadows.close-yellow}`** = `12px 12px 0px {colors.yellow}`：系统里最响的纵深表态。用在收尾框上，让反色表面尽管底色深，仍读得出"抬升"。
- **`{shadows.close-white}`** = `6px 6px 0px {colors.white}`：用在 close-btn 上，在黑底上维持抬升感。

这些彩色阴影是"阴影永远黑"规则仅有的例外，且只出现在深色表面上。

### 基于边框的纵深
系统大部分表面层次来自 4px 或 3px 墨边，而非阴影。带边无阴影的卡片仍读作"表面上的一个物件"，阴影才让它读作"被抬起"。抬升卡片用阴影；多卡网格里的次级卡片用纯边框，免得叠起来的阴影糊成噪声。

### 倾斜元素即纵深
系统俏皮的纵深签名是**倾斜**。统计卡片交替 -2deg / +2deg 旋转。装饰粉色矩形最多倾斜 ±12deg。英雄框上的黄色按钮片倾斜 -3deg。这些倾斜有意打破网格对齐，不用真透视或阴影就造出维度感。

## 形状与处理

### 圆角
- 结构上**一律 0px**：卡片、标签胶囊、按钮、icon-square、list-number、头像、徽章。方角不可商量。
- **50%（圆）**只用于 stat-deco 点缀点（钉在统计卡片上的 12×12 圆形点缀）。这是系统唯一的圆形。

方角纪律是系统的结构身份。给任何卡片或小片加圆角，会立刻读成另一套美学。

### 边框粗细
- **4px 实线 `{colors.black}`**：主卡片（英雄框、特性卡片、引文框、图表框、团队卡片边、时间轴步骤边、统计卡片边），以及收尾框反色版（黑底上 4px 实线白）。
- **3px 实线 `{colors.black}`**：次级外壳（标签胶囊、按钮、导言卡片、icon-square、list-number、头像、角标、nav-btn、页码、stripe-block、star-burst）。3px 表示"次级结构"，4px 表示"主结构"。
- **2px 实线 `{colors.black}`**：只用于图例色块（16×16 图色块）与 stat-deco 点缀点。最细的边框，留给原子级外壳。
- **4px 实线 `{colors.white}`**：只用于反色收尾框、visual-box，以及深色分栏视觉表面上它的 ::after 偏移框。

边框粗细阶梯（2 / 3 / 4）是固定的。没有 1px 边，没有 5px+ 边。

### 装饰元素类型

**Label-pill**：方形带框胶囊（3px 黑边、4px 阴影），浅彩或白填充，Space Grotesk 13px 字重 600 大写文字、0.08em 字距。通用分节眉题。

**Corner-bracket**：卡片四角的两枚 L 形角标（全包围时四枚），3px 黑边。造出框中框的装饰母题。

**Star-burst**：CSS clip-path 剪出的十角星，带 3px 边、浅彩填充。装饰性注意力抓手，钉在收尾框与特性卡片的角上。

**Stripe-block**：黑 + 一色浅彩的 4px 实、8px 空斜纹图案，配 3px 黑边框。海报类表面上的装饰注意力块。

**Dot-grid**：1.2px 径向渐变点图案，24×24 间距。用作页面角落的淡装饰叠层，30-40% 不透明度。

**Feature-deco 缺口**：48×48 黄色方块带 3px 黑边，绝对定位从特性卡片顶边探出。缺口破开卡片顶边，像是被"订上去"的。

**Icon-square**：64×64 浅彩方块带 3px 黑边，内含一个 Inter 字重 700 / 28px 的大写字母字形。用作特性卡片图标。

**Stat-deco 点**：12×12 圆形带 2px 黑边、浅彩填充，钉在统计卡片右上。系统唯一的圆形。

**List-number**：36×36 黄色方块带 3px 黑边，内含 Space Grotesk 14px 字重 700 数字。用作编号列表项目符号。

**Avatar-square**：72×72 浅彩方块带 3px 黑边，内含两个 Inter 字重 900 / 28px 的大写首字母。用于团队网格，填充在浅彩间轮转。

**Step-connector**：28×4 的黑色横条，钉在时间轴步骤卡片右边缘、半高处。视觉上把相邻步骤串成横向流程。

**倾斜装饰**：任何带 `rotate(±2deg 到 ±12deg)` 变换的矩形、徽章或星星。倾斜是对网格的刻意破局，没有它系统会显得太整齐。

## 该做与不该做

### 该做

- 主卡片（`{components.card-elevated}`、英雄框、引文框）用 4px 实线黑边，次级外壳用 3px。边框粗细阶梯是系统的结构脊梁。
- 每条 4px 边配 8px 偏移阴影，每条 3px 边配 4px 偏移阴影。边/影绑定不可商量。
- 让幻灯片背景在浅彩配色里轮转（米白、奶油、蓝、粉、绿、黄），保持视觉节奏。连着多页停在一色会把系统压平。
- 每个 Inter 展示元素都设成大写、负字距（-0.01 到 -0.03em）、字重 800+。这个组合就是排印身份。
- 用 `{components.label-pill}`（3px 边、4px 阴影、浅彩填充、Space Grotesk 大写 0.08em）作每个区域的通用分节眉题。
- 给装饰矩形、统计卡片、星星、徽章加倾斜（±2deg 到 ±12deg）。刻意的错位是系统的俏皮签名。
- 用 `{colors.yellow}` 作默认按钮色。黄配 3px 黑边、4px 黑阴影是系统的"点这里"声部。
- 阴影渲染成纯黑零模糊、始终右下偏移。硬边阴影是纵深语言。
- 每处表面都加一个装饰元素（星爆、条纹块、点网格、角标、倾斜矩形）。视觉喧闹是系统能量的一部分。
- 收尾表面用纯黑 `{colors.black}`，白文字，收尾框上 12px 黄色偏移阴影。反色深表面是系统最响的对比瞬间。

### 不该做

- 不要给卡片、按钮、标签胶囊、icon-square、头像加圆角。除 stat-deco 点（12px 圆）外，border-radius 禁用。
- 不要模糊任何阴影。每处阴影都是零模糊硬边。`box-shadow: 0 4px 12px rgba(0,0,0,0.1)` 在这套系统里不存在。
- 不要用彩色边框。边框永远纯黑，唯一例外是收尾框反色的 4px 白边。
- 不要把 Inter 展示字重写成句首大写。heading-xl、heading-lg、quote-text、close-title、card-title 上大写是强制的。
- 不要设没有负字距的 Inter 展示。重磅默认字距的 Inter 读起来是另一套系统。
- 不要引入第六种浅彩。配色锁死在粉、蓝、绿、黄、奶油。加紫、橙、红会破掉精心收拢的糖果配色。
- 不要省掉区域的标签胶囊。从背景直接跳到标题、没有眉题小片，会破掉系统的编辑节奏。
- 不要把标签胶囊渲染成纯文字。3px 边 + 4px 阴影 + 浅彩填充的组合才定义了胶囊。
- 不要用模糊或彩色的正文文字。浅表面上正文是纯黑，深表面上是纯白或奶油。
- 不要让每张卡片都对齐得整整齐齐。统计卡片、装饰、徽章上的倾斜，正是系统手工感的来源。

## 响应式行为

BlockFrame 设计为 **1920×1080 演示系统**（等效 100vw × 100vh）。尺寸用 CSS `clamp()` 排字，边框、阴影、结构内边距用固定 px。系统为窄视口设了三个组件级断点。

### 缩放行为
- Heading-xl 按视口宽度从 48px 缩放到 96px。
- Heading-lg 从 32px 缩放到 64px。
- 正文从 16px 缩放到 20px。
- 边框（3px、4px）、阴影（4px、8px）、结构内边距（60px slide-pad）固定不缩放。

### 组件断点
- `max-width: 1024px`：幻灯片内边距由 60px 收到 40px，双栏分栏纵向堆叠，特性卡片行纵向堆叠，时间轴轨道纵向堆叠并隐藏 step-connector，统计网格收成 2 列，团队网格收成 2 列。分栏视觉失去左边框、得到上边框。
- `max-width: 640px`：统计网格收成 1 列，团队网格收成 1 列，英雄框内边距收到 32px，引文框内边距收到 32px。

### 放映行为
- 用 `ArrowRight` 或 `Space` 前进。
- 用 `ArrowLeft` 后退。
- 横向触摸滑动，50px 阈值前进/后退。
- 幻灯片过渡是瞬时的（`.active` 类上 `display: none` ↔ `display: flex`），没有交叉淡入。

### 打印行为
系统没有 `@media print` 规则。幻灯片绝对定位、同一时刻只有一页可见，打印只能得到激活页。静态导出时，逐页截图能保留所有边框、阴影与装饰（全部是 CSS，不是图片资源）。

### 交互状态
- 按钮与导航按钮悬停时平移 -2/-2、阴影长到 6px（`{shadows.hover}`）；激活时平移 2/2、阴影缩到 2px。这种悬停-按下行为在演示系统里不常见，它反映了 BlockFrame 兼具演示文稿与交互式产品原型的双重身份。

## CJK 与国际化内容

用本模板承载中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文搭配，并套用通用 CJK 调整。所有推荐中文字体均通过 CDN 加载，无需安装。

### 推荐中文搭配

| 角色 | 拉丁（默认） | 中文对应 |
|---|---|---|
| 展示 / 英雄 / 引文 / 收尾标题 / 统计数字 | Inter 800–900（大写、负字距） | 思源黑体 Noto Sans SC 900（句首大写、0 字距） |
| 卡片标题 | Inter 700（大写） | 思源黑体 Noto Sans SC 700（无变换） |
| 正文 / 列表正文 | Inter 500 | 思源黑体 Noto Sans SC 400 |
| 标签 / 等宽小片 / 计数器 / 图例 | Space Grotesk 600–700（大写、0.05–0.1em 字距） | 思源黑体 Noto Sans SC 600（无变换、无字距） |

### 混排策略

**策略 A**：用一款自带拉丁字形覆盖的 CJK 字族，把所有文字元素设为 `font-family: 'Noto Sans SC', sans-serif`。思源黑体自带拉丁字形，与汉字并排也干净，混排句子会用一致字面渲染。拉丁原版里 Inter / Space Grotesk 的区分靠字重反差保留下来：字重 900 担粗野展示角色，字重 600 担标签角色，字重 400–500 担正文。即便字面反差没了，视觉层级仍在。

### 加载

在模板 `<head>` 中加入：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700;900&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- **行高**：在拉丁规格上提高约 15–25%。正文 1.75–1.85（从 1.6 上调），展示 1.15–1.25（从 0.95–1 上调）。拉丁展示压到 0.95 行高，CJK 压到这个程度会纵向相撞。
- **字距**：每段 CJK 文本设为 0。模板里 Inter 展示的负字距（−0.02 到 −0.03em）套在 CJK 上会笔画重叠、读着像坏了；Space Grotesk 标签的 0.05–0.1em 正字距放在方正字形上显得松垮。
- **文字变换**：不要对中文套 `uppercase`，CJK 没有大小写。拉丁原版里每个 Inter 展示标题（heading-xl、heading-lg、quote-text、close-title、card-title）都用 `text-transform: uppercase`，CJK 文本要去掉。每个标签胶囊、计数器、外壳元素也用大写，同样去掉。
- **标点**：用全角中文标点（，。：；！？「」（））。
- **展示标题不加句号**：中文排印惯例，展示级标题末尾不写 。
- **中西文之间加空格（盘古之白）**：每个汉字与相邻的拉丁字符或数字之间插入一个 ASCII 空格。写 `BlockFrame 设计系统`，不要写 `BlockFrame设计系统`。
- **一句一款字体**：思源黑体以统一风格覆盖 CJK 与拉丁字形，混排句子交给它处理。不要让浏览器在词中切回 Inter 或 Space Grotesk。

### 本系统的美学提示

拉丁原版的排印身份完全建立在 Inter 展示上**重磅大写 + 负字距**的组合。CJK 没有大小写，这个信号便消失了。系统之所以能存活，是因为它的身份**八成靠结构、两成靠排印**：4px 黑边、8px 硬边偏移阴影、五浅彩配色、倾斜装饰、标签胶囊、星爆、条纹块、点网格，才是粗野主义的主力。把思源黑体 900 设成句首大写、保持同样的大字号即可；黑压浅彩的厚重加硬阴影框边，不管文字是不是大写，都读得出粗野。

标签胶囊（Space Grotesk 600 大写、0.08em 字距、3px 边 + 4px 阴影、浅彩填充）会丢掉大写 + 宽字距等宽的性格。中文标签胶囊请用思源黑体字重 600、0 字距，字号略收紧（11–12px 而非 13px）：带框胶囊形状和阴影承担外壳识别工作。浅彩填充的轮转（粉 / 蓝 / 绿 / 黄 / 奶油）要保留，它是边框之外系统最易认的信号。

### 已知 CJK 缺口

- **没有可 CDN 加载的中文等宽字面给"系统读数"声部。** Space Grotesk 的准等宽角色（标签胶囊、计数器、等宽小片、页码 NN / NN）依赖它略带几何的性格加宽字距大写处理，这两样都撑不过 CJK 汉化。页码与图表图例可以保留拉丁数字 + 拉丁标签；纯中文外壳只能靠胶囊边 + 阴影 + 浅彩填充来提示"标签"，而不是靠排印处理。
- **"大写粗野"身份变弱。** 系统最鲜明的排印决策是"重磅大写 Inter 配负字距"，这个信号在 CJK 里无可替代。补偿办法是更倚重结构元素：多加装饰破局（额外倾斜矩形、星爆、条纹块）、跨页更饱和的浅彩底轮转、略收紧阴影偏移，以抵消更平静的排印基线。

## 迭代指南

1. 任何新卡片都用 4px 或 3px 实线黑边 + 配重的偏移阴影（8px 或 4px）。绝不出一张两者缺一的卡片。
2. 任何新区域都以 `{components.label-pill}` 眉题（浅彩填充）开头，接着大写字重 800+ 的 Inter 标题，再是内容。标签-标题-内容的顺序是系统的编辑节奏。
3. 任何新标题都用大写 Inter 配负字距、字重 800-900。主瞬间取 `{typography.heading-lg}`（32-64px），封面/英雄级取 `{typography.heading-xl}`（48-96px）。
4. 任何新强调色或表面填充都从五浅彩配色里挑（粉、蓝、绿、黄、奶油），绝不引入第六种浅彩。
5. 任何新 CTA 都用 `{components.button-primary}` 模式：3px 黑边、黄填充、4px 黑阴影、Inter 字重 700 / 16px。悬停抬起 -2/-2、阴影长到 6px。
6. 任何新图表按粉 → 蓝 → 绿的系列顺序轮转，黄/奶油可作额外系列。图例色块用 2px 黑边。
7. 任何新统计或指标都用 Inter 字重 900 + 行高 1 作数字，下方配 Space Grotesk 大写标签。卡片用一枚浅彩 `{components.stat-deco-dot}` 点缀。
8. 任何新页面都至少加一处装饰破局（倾斜矩形、星爆、条纹块、点网格角、角标框），空表面显得怯。
9. 任何新收尾类表面都用纯 `{colors.black}` 底、白文字、4px 白边收尾框、12px 黄色偏移阴影。这是唯一允许的彩色阴影。
10. 表面若显得太吵，去掉一个装饰，别去掉边框或阴影。边框和阴影是结构，装饰才可调。

## 已知缺口

- **Inter 与 Space Grotesk 通过内联 `@import` 从 Google Fonts 加载**。除 `sans-serif` 与 `monospace` 外没有系统回退；在 Google Fonts 失效的环境里，系统会塌成系统默认字体，失去身份。
- **系统用 `<style>` 块内的 `@import`**，而非 `<link>` preconnect。这比标准 `<link>` 方式慢，可能延后排印的首次绘制。
- **图表以内联 SVG 配硬编码坐标渲染**（`viewBox="0 0 800 360"`，每个 `<rect>` 的 `x/y/width/height` 写死）。加新图表页要手算坐标，没有数据绑定层。
- **按钮的悬停/激活态假定有指针设备**。触屏上抬起-按下的反馈只在点按时触发，可能显得不一致。
- **统计卡片的倾斜用 `:nth-child(odd)` -2deg、`:nth-child(even)` +2deg 硬编码**。卡片一重排，倾斜方向就跟着变，除排序外没有逐卡控制。
- **装饰星星用 10 点的 CSS clip-path 多边形**。不支持 clip-path 的浏览器（很老的 IE/Edge）会把星星渲染成一块彩色矩形。
- **页码与导航控件在底边压住幻灯片内容区**。某些页面（slide-4、slide-9）的 110px 底部内边距留了位置，但别的页面可能有内容挤到左下页码胶囊。
- **黑色收尾表面用纯 `#000000` 底配白文字**，无障碍角度是高对比、没问题，但这个表面上的彩色装饰（黄阴影、白边）在小尺寸下过不了 WCAG 色彩对比检查。
- **点网格背景是 CSS 径向渐变**。视口极大时点可能小到读不成网格，极小时又可能糊成一片实噪声。
- **除二值 display 切换外，幻灯片之间没有过渡**。要加淡入或滑动动画得改 JS 并补 transition CSS。
