---
version: alpha
name: Scatterbrain
description: "A Post-it-note-and-cork-board presentation system. Every content block is a colored sticky note on a textured paper or cork surface, layered with red thumbtacks, masking tape, and decorative doodles. Display type runs in Shrikhand (a chunky decorative display serif) on every headline; body type runs in Zilla Slab (a friendly slab serif); handwritten emphasis runs in Caveat. The palette is pastel sticky-note colors (yellow, blue, pink, green, orange, purple) on cream paper / cork / warm gradient backgrounds. The aesthetic borrows from creative-workshop wall art, brainstorming boards, and indie-studio mood boards: scattered slight rotations, multiple background texture variants per slide, pin / tape / drop-shadow combinations. The effect is warmth, play, and tactile creative-process energy."

colors:
  yellow: "#ffe066"
  yellow-deep: "#ffd43b"
  blue: "#a5d8ff"
  blue-deep: "#74c0fc"
  pink: "#ffc9c9"
  pink-deep: "#ff9f9f"
  green: "#b2f2bb"
  green-deep: "#8ce99a"
  orange: "#ffcc80"
  purple: "#d0bfff"
  cream: "#faf8f3"
  paper: "#f7f5f0"
  ink: "#2d2a26"
  ink-light: "#5c5750"
  shadow: "rgba(45, 42, 38, 0.15)"
  shadow-deep: "rgba(45, 42, 38, 0.25)"

typography:
  display-hero:
    fontFamily: "'Shrikhand', cursive"
    fontSize: "clamp(2.5rem, 5vw, 4.5rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  statement:
    fontFamily: "'Shrikhand', cursive"
    fontSize: "clamp(2rem, 4vw, 3.5rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  headline:
    fontFamily: "'Shrikhand', cursive"
    fontSize: "clamp(1.8rem, 3.5vw, 3rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  title:
    fontFamily: "'Shrikhand', cursive"
    fontSize: "clamp(1.3rem, 2.5vw, 1.8rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  body:
    fontFamily: "'Zilla Slab', serif"
    fontSize: "clamp(1rem, 1.5vw, 1.25rem)"
    fontWeight: 400
    lineHeight: 1.7
  list-item:
    fontFamily: "'Zilla Slab', serif"
    fontSize: "1.1rem"
    fontWeight: 400
    lineHeight: 1.6
  handwritten:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(1.2rem, 2vw, 1.6rem)"
    fontWeight: 400
    lineHeight: 1.4
  handwritten-lg:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(1.4rem, 2.5vw, 2rem)"
    fontWeight: 600
    lineHeight: 1.3
  handwritten-sm:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(1.2rem, 1.5vw, 1.4rem)"
    fontWeight: 500
    lineHeight: 1.3
  label-script:
    fontFamily: "'Caveat', cursive"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  stat-value:
    fontFamily: "'Shrikhand', cursive"
    fontSize: "1.8rem"
    fontWeight: 400
    lineHeight: 1.1
  caption-subtitle:
    fontFamily: "'Zilla Slab', serif"
    fontSize: "1.3rem"
    fontWeight: 400
    lineHeight: 1.6

spacing:
  slide-pad: 3rem
  post-it-pad-lg: "3rem 4rem"
  post-it-pad-md: "2.5rem"
  post-it-pad-sm: "1.5rem"
  post-it-pad-statement: "3.5rem 4rem"
  gap-lg: "3rem"
  gap-md: "2.5rem"
  gap-sm: "2rem"

canvas:
  width: 100vw
  height: 100vh

components:
  bg-cork:
    backgroundLayers: "radial-gradient ellipse + linear-gradient (warm browns) + SVG plus-sign pattern at 15% opacity"
    description: "Cork-board background variant. Warm tan/brown tonal gradient with a faint pattern of small plus-sign marks suggesting cork texture. Used on slides that feel like 'a wall of pinned notes.'"
  bg-paper:
    backgroundLayers: "linear-gradient (cream) + 40px grid lines at 8% opacity"
    description: "Desk-paper background variant. Cream gradient with a faint 40px grid overlay suggesting graph or notebook paper. Used on slides that feel like 'notes arranged on a desk.'"
  bg-warm:
    backgroundLayers: "multiple radial-gradients (yellow/blue/pink soft glows) + linear-gradient cream base"
    description: "Warm gradient background variant. Cream base with soft-glow ellipses of yellow, blue, and pink suggesting morning light. Used on slides that need a softer, less-textured atmosphere."
  grain-overlay:
    backgroundImage: "SVG fractal-noise filter, 256×256 tile"
    opacity: 0.04
    zIndex: 9999
    description: "Fixed full-viewport SVG grain texture above all content at 4% opacity. Reinforces the paper-and-cork tactile register. Always present."
  post-it:
    padding: "2rem"
    boxShadow: "2px 3px 15px {colors.shadow}, 0 1px 3px {colors.shadow-deep}"
    description: "Generic colored sticky-note base. Soft drop-shadow simulates the note's slight lift off the surface. Always carries a background color from the post-it palette (yellow, blue, pink, green, orange, purple, or white)."
  post-it-yellow:
    background: "linear-gradient(135deg, {colors.yellow} 0%, {colors.yellow-deep} 100%)"
    description: "Yellow sticky variant. Soft 135° gradient from light to deep yellow."
  post-it-blue:
    background: "linear-gradient(135deg, {colors.blue} 0%, {colors.blue-deep} 100%)"
    description: "Blue sticky variant."
  post-it-pink:
    background: "linear-gradient(135deg, {colors.pink} 0%, {colors.pink-deep} 100%)"
    description: "Pink sticky variant."
  post-it-green:
    background: "linear-gradient(135deg, {colors.green} 0%, {colors.green-deep} 100%)"
    description: "Green sticky variant."
  post-it-orange:
    background: "{colors.orange}"
    description: "Orange sticky variant. Flat fill (no gradient) — the only post-it that ships flat."
  post-it-purple:
    background: "{colors.purple}"
    description: "Purple sticky variant. Flat fill."
  post-it-white:
    background: "#fff"
    border: "2px solid {colors.ink}"
    description: "White note variant. Carries a 2px ink border (because pure white otherwise disappears into cream/paper backgrounds). Used as a 'plain note' in timelines or comparisons."
  pin:
    width: 16px
    height: 16px
    position: "::before, top: -12px, centered"
    background: "radial-gradient(circle at 30% 30%, #ff6b6b, #c92a2a)"
    boxShadow: "0 2px 4px {colors.shadow-deep}, inset -2px -2px 4px rgba(0,0,0,0.2)"
    description: "Red thumbtack mark sitting at the top-center of a post-it via ::before. Radial-gradient gives it a 3D bead-shaped highlight; inset shadow adds dimension. The default pin color."
  pin-blue:
    background: "radial-gradient(circle at 30% 30%, #4dabf7, #1864ab)"
    description: "Blue thumbtack variant."
  pin-green:
    background: "radial-gradient(circle at 30% 30%, #69db7c, #2f9e44)"
    description: "Green thumbtack variant."
  pin-gold:
    background: "radial-gradient(circle at 30% 30%, #ffd43b, #f59f00)"
    description: "Gold thumbtack variant."
  tape:
    width: 80px
    height: 25px
    position: "::after, top: -15px, centered, rotate(-2deg)"
    background: "rgba(255, 255, 255, 0.4)"
    border: "1px solid rgba(255, 255, 255, 0.3)"
    description: "Masking-tape mark across the top-center of a post-it via ::after. Translucent white, slightly rotated. Often combined with .pin so a single note has both tape and a tack."
  card-rotation:
    rotation: "±1° to ±15°"
    description: "Every post-it carries a small rotation. Statement and feature cards: ±1° to ±3°. Accent / floating notes: ±5° to ±15° (more dramatic to read as 'casually applied'). Rotations alternate direction across adjacent notes."
  feature-icon:
    width: 60px
    height: 60px
    border: "3px solid {colors.ink}"
    borderRadius: "50%"
    fontFamily: "'Shrikhand', cursive"
    fontSize: 1.5rem
    description: "Round ink-bordered icon containing a single character (letter, number, or symbol) in Shrikhand display. Used as a category marker at the top of feature post-its."
  versus-circle:
    width: 60px
    height: 60px
    background: "{colors.ink}"
    color: "{colors.paper}"
    borderRadius: "50%"
    fontFamily: "'Shrikhand', cursive"
    fontSize: 1.2rem
    boxShadow: "0 2px 8px {colors.shadow-deep}"
    description: "Ink-filled circle with cream text used between two compare-cards. Centered between the two cards with absolute positioning; reads as a 'vs' / 'and' connector."
  photo-frame:
    background: "#fff"
    padding: "1rem"
    boxShadow: "2px 3px 15px {colors.shadow}"
    rotation: "±1° to ±2°"
    description: "Polaroid-style image frame. White paper with 1rem padding around the inner image area; same drop shadow as post-its; small rotation. The inner image area has a 4:3 aspect ratio."
  chart-canvas:
    background: "#fff"
    padding: "2.5rem"
    boxShadow: "2px 3px 15px {colors.shadow}"
    rotation: "±1°"
    description: "White paper card hosting an inline SVG chart. Same drop shadow as post-its and photo-frames; small rotation. Charts use the post-it color palette for fills."
  stat-row:
    borderBottom: "1px dashed rgba(45, 42, 38, 0.2)"
    padding: "1rem 0"
    description: "A label-and-value row inside a stat post-it. Label in Zilla Slab body color; value in Shrikhand stat-value. Bottom-divider is a dashed ink-alpha hairline."
  doodle:
    opacity: 0.15
    stroke: "{colors.ink}"
    strokeWidth: 3
    description: "Decorative SVG mark placed absolutely in slide corners — a circle, squiggle, triangle, line, or X+ pair. All at 0.15 opacity, all in 3px ink stroke. Slides have 0–2 doodles each."
  timeline-connector:
    height: 60px
    pathStyle: "Q (quadratic) bezier curve at 0.3 opacity, stroke-dasharray '8 4', polygon arrowhead at end"
    description: "Dashed quadratic-bezier line between timeline nodes. Curve direction alternates row to row (concave up, concave down). Always ends with a triangle arrowhead."
  custom-cursor:
    cursor: "URL data-svg red-and-white thumbtack, 24×24, hotspot 12×12"
    description: "Browser cursor replaced with a tiny SVG thumbtack circle (red outer, white center) when hovering over any slide. Reinforces the 'pinning ideas to a board' metaphor."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/scatterbrain/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Scatterbrain 是一套**便利贴与软木板演示系统**。每个内容块都是一张彩色便利贴（`{components.post-it}`），叠在三种带纹理背景变体之一上，软木板、桌面纸、暖渐变，配红 / 蓝 / 绿 / 金图钉别住便签，有时再在顶上添半透明美纹纸胶带。视觉隐喻是彻底的：文稿是一面创意工作坊墙、一块头脑风暴板、或一张思考者的书桌，内容就是别满其上的便利贴簇。

字体栈搭配三款 Google Fonts，各有分明的情绪角色。**Shrikhand** 是展示声部，一款粗壮的装饰展示衬线，曲线俏皮、对比强烈。以字重 400（唯一可用字重）用于每个标题、陈述、特性图标字形、统计值、超大标注。它响亮、友好的个性是系统的主信号，读作手写的马克笔字，而非排印出版物。**Zilla Slab** 是正文声部，一款友好的现代板衬线，带人文比例。字重 300–700 用于正文段、列表项、标签。它的板衬线贴合 Shrikhand 温暖手绘的语域，又不抢注意力。**Caveat** 是手写脚本声部，一款随意草书。用于私人便签、页边批注、脚本式 eyebrow 标签、统计分隔俏皮话，以及一切该读作"用笔草草写在便签上"的瞬间。

色彩理念是**触感纸背景上的柔和便利贴调色板**。七种便利贴色（黄、蓝、粉、绿、橙、紫，外加带边框的白）提供分类变化，每种都有一个更深的兄弟色来驱动 135° 渐变填充。墨（`{colors.ink}` — #2d2a26）是柔和暖炭而非纯黑，舒服地落在暖柔和色上。三种背景变体（软木 `bg-cork`、纸 `bg-paper`、暖渐变 `bg-warm`）在页间提供触感变化，让文稿不显单调。柔和色淡到墨文字在每种便利贴色上都无需反转仍可读。

纵深来自**柔和投影 + 小旋转 + 分层触感元素**（图钉、胶带、涂鸦）。招牌处理是每张 post-it 带一道柔和模糊投影（`2px 3px 15px {colors.shadow}`），暗示从表面微微掀起，再加一个小旋转（±1° 到 ±15°），读作手放而非吸附网格。可选图钉（经 `::before` 的红图钉）与胶带（经 `::after` 的半透明白）不靠 box-shadow 花招添触感纵深。

**密度取向：中等。** 每页由 1–4 张便利贴加 1–2 处点缀装饰锚定（浮动的侧便签、涂鸦、装饰形状）。一张居中大 post-it 的页读作宣言瞬间，三张特性卡的页读作布局页，一张主 post-it 加 2–4 张小浮动点缀 post-it 的页读作英雄跨页。同时叠满便利贴会把俏皮能量挤成混乱。对的密度是便签多到像一张创意过程跨页，又有足够负空间把每张便签读清楚。

**关键特征：**
- 三种带纹理背景变体：软木（`{components.bg-cork}`）、纸（`{components.bg-paper}`）、暖渐变（`{components.bg-warm}`）。每页挑一种。
- 一层固定的 SVG 颗粒叠层以 4% 不透明度盖在全部内容之上，强化纸语域。
- 七种便利贴色：黄、蓝、粉、绿、橙、紫、带边框白。除橙 / 紫 / 白外都是渐变填充。
- 每张 post-it 带柔和投影 + 小旋转。相邻便签间旋转方向交替。
- 经 `::before` 的红图钉（及蓝 / 绿 / 金变体），经 `::after` 的美纹纸胶带。常在同一张便签上合用。
- 展示标题用 Shrikhand（粗壮展示衬线），正文用 Zilla Slab（友好板衬线），私人批注用 Caveat（随意脚本）。
- 装饰 SVG 涂鸦（圆、扭动、三角、X 记号）以 0.15 不透明度住在页角。
- 自定义图钉光标强化"把点子别到板上"的隐喻。

## 颜色

### 调色板

**便利贴色**（渐变填充或平涂）：
- **黄**（`{colors.yellow}` — #ffe066 → `{colors.yellow-deep}` — #ffd43b）：经典便利贴黄。最常见的便签色。系统的"默认"便利贴。
- **蓝**（`{colors.blue}` — #a5d8ff → `{colors.blue-deep}` — #74c0fc）：柔和天蓝。系统的"次级"便利贴。
- **粉**（`{colors.pink}` — #ffc9c9 → `{colors.pink-deep}` — #ff9f9f）：柔和玫瑰粉。系统的"暖强调"便利贴。
- **绿**（`{colors.green}` — #b2f2bb → `{colors.green-deep}` — #8ce99a）：薄荷绿。系统的"冷强调"便利贴。
- **橙**（`{colors.orange}` — #ffcc80）：暖桃橙。平涂填充，无渐变。作三级强调求变化。
- **紫**（`{colors.purple}` — #d0bfff）：薰衣草紫。平涂填充，无渐变。作三级强调求变化。

**特殊便签色**：
- **白**（`#fff`）：带边框的白便利贴，用于时间轴与比较里需要"朴素"或"中性"便签处。始终带 2px 墨边框，否则纯白会消失进奶油 / 纸背景。

**纸 / 表面色**：
- **奶油**（`{colors.cream}` — #faf8f3）：最浅的纸变体。用在 `bg-paper` 与 `bg-warm` 背景渐变里。
- **纸**（`{colors.paper}` — #f7f5f0）：正文背景，坐在每页之后，是透过 bg 叠层可见的页面色。用作深墨表面上的反色文字色。

**墨 / 文字色**：
- **墨**（`{colors.ink}` — #2d2a26）：结构色。全部标题、全部正文、全部边框、全部涂鸦描边。比纯黑略柔求暖。
- **浅墨**（`{colors.ink-light}` — #5c5750）：次级文字色，用于正文段、图注、弱化文字。

**阴影 token**：
- `{colors.shadow}`（rgba(45, 42, 38, 0.15)）：柔和投影，用在每张 post-it 上。
- `{colors.shadow-deep}`（rgba(45, 42, 38, 0.25)）：更强的接触阴影，用作 post-it 投影的第二层。

### 默认值
- **默认表面背景**：每页从 `{components.bg-cork}` / `{components.bg-paper}` / `{components.bg-warm}` 里挑一种。软木默认给触感 / 便签墙瞬间，纸给桌面 / 专注内容瞬间，暖渐变给英雄 / 氛围瞬间。
- **默认 post-it 色**：`{components.post-it-yellow}`，黄是最常见的便利贴，读作系统基线。
- **默认标题色**：`{colors.ink}`（#2d2a26），每张 post-it 上柔和暖炭的 Shrikhand 展示。
- **默认正文色**：段落正文 `{colors.ink-light}`（#5c5750），列表项与强调正文 `{colors.ink}`。
- **默认边框色**：白便签的 2px 边框与特性图标圆边框用 `{colors.ink}`。多数便利贴没有边框（渐变填充定义它们）。
- **默认图钉色**：`{components.pin}`（红），系统的"默认"图钉。需要视觉变化时用蓝 / 绿 / 金变体去配底下 post-it 的颜色。
- **默认胶带**：省着用，典型贴在英雄 / 陈述 post-it 上，让便签同时带图钉与一条胶带，显得"正式贴出"。
- **墨表面上默认文字色**：`{colors.paper}`（#f7f5f0）。
- **默认装饰涂鸦色**：0.15 不透明度、3px 描边的 `{colors.ink}`。

七种便利贴色**没有固定语义**，黄不表"警告"、绿不表"成功"。它们是分类型调色板，选择标示"这是簇里哪张便签"。轮换颜色求视觉变化，把渐变填充便签（黄、蓝、粉、绿）与平涂便签（橙、紫）配对求纹理变化。

## 排印

### 字族
系统有三款 Google Fonts，各有分明角色：

- **Shrikhand**（展示）：粗壮装饰展示衬线，笔画对比高、曲线俏皮、带手写马克笔感。单字重（400）。用于每个展示瞬间，标题、陈述、题目、特性图标字形、统计值、versus 圆文字。它响亮的个性是系统的主身份，换成别的展示衬线会丢掉工作坊声部。
- **Zilla Slab**（正文）：友好的现代板衬线，带人文暖意。多字重（300–700，斜体变体 300 与 400）。正文段默认字重 400，最轻图注 300，强调 500–700。板衬线读作暖手作而非机械。
- **Caveat**（手写脚本）：随意草书，多字重（400–700）。用于私人便签、页边批注、脚本式 eyebrow 标签（全大写加 0.15em 字距）、收尾页落款、统计分隔行里的装饰俏皮话。

Zilla Slab 有斜体（300 与 400 斜体）但很少用，强调来自换字重或换字面，不来自斜体。下划线不用。

### 排印比例

| Token | 尺寸（clamp） | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-hero}` | 2.5–4.5rem | Shrikhand | 400 | 封面或收尾超大标题 |
| `{typography.statement}` | 2–3.5rem | Shrikhand | 400 | 居中陈述或引文 |
| `{typography.headline}` | 1.8–3rem | Shrikhand | 400 | 页面主标题 / 分节标题 |
| `{typography.title}` | 1.3–1.8rem | Shrikhand | 400 | 子区域或卡片标题 |
| `{typography.caption-subtitle}` | 1.3rem | Zilla Slab | 400 | 英雄标题下的页面副标题 |
| `{typography.body}` | 1–1.25rem | Zilla Slab | 400 | 标准段落正文 |
| `{typography.list-item}` | 1.1rem | Zilla Slab | 400 | 项目 / 勾选列表行 |
| `{typography.handwritten}` | 1.2–1.6rem | Caveat | 400 | 装饰俏皮话、私人便签 |
| `{typography.handwritten-lg}` | 1.4–2rem | Caveat | 600 | 较大的手写副标题 |
| `{typography.handwritten-sm}` | 1.2–1.4rem | Caveat | 500 | 小号强调标签 |
| `{typography.label-script}` | 0.9rem | Caveat | 400 | 加字距全大写 eyebrow 标签 |
| `{typography.stat-value}` | 1.8rem | Shrikhand | 400 | 统计行里的数值 |

### 默认值
- **主分节标题默认尺寸（post-it 内）**：Shrikhand 的 `{typography.headline}`（1.8–3rem clamp）。
- **封面或收尾超大标题默认尺寸**：`{typography.display-hero}`（2.5–4.5rem clamp）。
- **居中宣言 / 引文陈述默认尺寸**：`{typography.statement}`（2–3.5rem clamp）。
- **段落正文默认尺寸**：Zilla Slab 400 的 `{typography.body}`（1–1.25rem clamp）。
- **列表行默认尺寸（项目、勾选、比较列表）**：Zilla Slab 400 的 `{typography.list-item}`（1.1rem）。
- **侧便签或俏皮话默认尺寸**：Caveat 400 的 `{typography.handwritten}`（1.2–1.6rem clamp）。
- **卡片标题上方 eyebrow 标签默认尺寸**：Caveat、全大写、0.15em 字距的 `{typography.label-script}`（0.9rem）。
- **统计值默认尺寸**：Shrikhand 的 `{typography.stat-value}`（1.8rem）。
- **Shrikhand 默认字重**：400（唯一字重）。
- **Zilla Slab 正文默认字重**：400。强调正文 500–700，轻图注 300。
- **Caveat 默认字重**：随意便签 400，强调 500–700。

卡片主文字在 `{typography.headline}` 与 `{typography.title}` 间拿不准时，卡片是页面主导元素就取 `{typography.headline}`，是几张较小卡之一就取 `{typography.title}`。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个展示标题都用 Shrikhand。** 换成 Zilla Slab 或别的展示字面会丢掉工作坊声部。连特性卡里的小标题（1.3rem）也用 Shrikhand。
- **每段正文与每个列表项都用 Zilla Slab。** 正文用 Shrikhand 排读作过火且读不了。
- **每条随意 / 私人便签都用 Caveat。** 包括侧便签、装饰俏皮话（"Jot it down before you forget!"、"OK"、":)"）、统计分隔里的私人观察。换成斜体 Zilla 会丢掉手绘声部。
- **每个 label-script eyebrow 都全大写、0.15em 字距。** Caveat 用正常字距读作正文草书，全大写 + 字距才把它变成分类标签。
- **每个特性图标圆边框都是 3px 墨，内含一个 Shrikhand 字形。** 变形（2px 边框、无衬线字形）会破掉图标的视觉招牌。
- **每张承载主标题的 post-it 都经 `::before` 得到一枚图钉。** 没有图钉的标题便签读作漂浮、没定义。
- **每张英雄 / 陈述 post-it 都同时带图钉与一条胶带**（`.pin .tape` 类一起）。这是系统给最强调便签的"正式贴出"处理。

### 排印原则
系统的排印节奏来自**三字面反差**：Shrikhand 展示（响、装饰、友好衬线）→ Zilla Slab 正文（稳、易读、板衬线）→ Caveat 手写脚本（私人、随意、草书）。只用一款字面的页读作单调，三款合起来的页读作工作坊式正确。

行高：展示紧（1.1）、正文宽（1.6–1.7）、手写脚本适中（1.3–1.4）。展示字距略正（0.02em），给 Shrikhand 比默认多一点开敞；正文不加字距；手写脚本标签带 0.15em 全大写加字距。

## 布局

### 画布系统
系统以 `100vw × 100vh` 为目标。每张 `.slide` 绝对定位铺满视口、默认 `display: none`，`.active` 页 `display: flex` 居中。导航由 JS 驱动，方向键、空格、PageUp/Down、Home/End、触屏滑动、鼠标滚轮（带 700ms 锁防止连跳）。

### 页面构图式样
系统支持若干构图式样，不硬性规定布局：
- **居中单卡**：一张大 post-it（陈述、收尾、RSVP 式）。
- **2 列或 3 列网格**：带小旋转的对齐 post-it 网格。
- **图表 + 图例**：一侧白图表卡，另一侧彩色 post-it 图例。
- **图 + 文**：一侧宝丽来式相框，另一侧文字 post-it 簇。
- **自由簇**：一张英雄 post-it，周围 2–4 张小点缀 post-it，旋转与位置各异。
- **时间轴行**：左右交替的节点 + 虚线曲线连接 + 每行一张内容卡。
- **比较**：两张并排 post-it，中间一个居中墨色 versus 圆。

每种式样里，单张 post-it 都坐在三种背景纹理之一上，带小旋转，空闲页角有装饰涂鸦记号。

### 内边距比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.slide-pad}` | 3rem | 页面外内边距 |
| `{spacing.post-it-pad-lg}` | 3rem 4rem | 英雄 / 标题 post-it 内部内边距 |
| `{spacing.post-it-pad-statement}` | 3.5rem 4rem | 陈述 post-it 内部内边距 |
| `{spacing.post-it-pad-md}` | 2.5rem | 标准 post-it 内部内边距 |
| `{spacing.post-it-pad-sm}` | 1.5rem | 小点缀 post-it 内部内边距 |
| `{spacing.gap-lg}` | 3rem | 多列网格间隙 |
| `{spacing.gap-md}` | 2.5rem | 特性网格间隙 |
| `{spacing.gap-sm}` | 2rem | 时间轴行间隙 |

### 常驻外壳
系统没有常驻页面外壳，没有进度条、没有页码、没有导航提示。自定义图钉光标是唯一的常驻视觉信号。导航纯靠键盘 / 滑动 / 滚轮驱动。

## 纵深与层级

### 柔和投影（主手法）
系统定义性的纵深处理是每张 post-it、相框、图表卡、图画画布上的**柔和投影**：`2px 3px 15px {colors.shadow}, 0 1px 3px {colors.shadow-deep}`。15px 模糊外阴影配 2px 横向、3px 纵向偏移，暗示便签在软木或纸面上微微悬浮。1px 模糊内阴影配 1px 纵向偏移，添上底边的接触阴影。两者合起来读作"别在板上、掀起的便签"。

这是**本库里唯一用柔和模糊阴影定义纵深的系统**，多数其他模板都禁用它们。Scatterbrain 拥抱它们，因为视觉隐喻依赖纸便签从带纹理表面上微微掀起的那份触感。

### 旋转（次级手法）
每张 post-it 带一个小旋转（±1° 到 ±15°）。英雄 / 陈述 / 特性 post-it 取小旋转（±1° 到 ±3°），点缀 / 浮动 / 收尾簇 post-it 取较大旋转（±5° 到 ±15°）。相邻便签间旋转方向交替，让簇读作随意贴上，而非吸附网格。

### 触感分层（图钉 + 胶带）
单张 post-it 上可选的分层记号提供额外纵深：
- **图钉（`{components.pin}`）**：经 `::before` 在便签顶部居中的 16px 圆形红图钉。径向渐变高光 + 内嵌阴影 + 投影让它读作一颗 3D 珠子。
- **胶带（`{components.tape}`）**：经 `::after` 在顶部居中、略旋转的 80×25px 半透明白胶带条。

图钉与胶带可在同一张便签上合用（`.pin.tape` 类对）。图钉的颜色变体（`pin-blue`、`pin-green`、`pin-gold`）配底下便签色求视觉凝聚。

### 背景纹理（氛围层）
三种背景变体（`bg-cork`、`bg-paper`、`bg-warm`）与全视口颗粒叠层（`{components.grain-overlay}` 4% 不透明度）提供基础纹理底。没有背景变体，文稿读成白底上漂浮的便签；有了它们，文稿读作物理落定在软木、桌面纸、或晨光上。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 0px | 全部 post-it、图表卡、相框、图画画布、比较卡 |
| 50%（圆） | 特性图标圆边框、versus 圆、图钉 |
| 3px | 图表条 `<rect>` 圆角（行内 SVG） |
| 自定义（无固定 token） | 相框内图片区遵循宝丽来 4:3 宽高比 |

多数表面是严格矩形。圆形只留给图标、图钉、versus 标记。图表条带细微的 3px 圆角（SVG 内）求友好。

### 边框粗细
- **2px 实 `{colors.ink}`**：白便签边框与图表 SVG `<rect>` 描边。
- **3px 实 `{colors.ink}`**：特性图标圆边框与涂鸦 SVG 路径。
- **1px 虚线 rgba(ink, 0.2)**：统计行细线分隔。
- **1px 实 rgba(ink, 0.1)**：比较列表行分隔。

边框一律是墨（暖炭）。不出现彩色边框。

### 装饰元素类型

**Post-it（`{components.post-it}`）**：七种变体之一的彩色便利贴（黄、蓝、粉、绿、橙、紫、带边框白）。内边距取 `{spacing.post-it-pad-*}` 比例。始终带柔和投影，几乎总带小旋转，通常带图钉、有时带胶带。

**图钉（`{components.pin}`）**：经 `::before` 的红图钉。默认红色，变体蓝、绿、金。坐在便签顶部居中。

**胶带（`{components.tape}`）**：经 `::after` 在便签顶部居中、略旋转的半透明白美纹纸胶带记号。

**特性图标（`{components.feature-icon}`）**：60px 墨边框圆，内含一个 Shrikhand 字形（单字符）。用在特性 post-it 顶端作类别标记。

**Versus 圆（`{components.versus-circle}`）**：墨填充圆配奶油 Shrikhand 文字，以绝对定位居中在两张比较 post-it 之间。自带投影。

**相框（`{components.photo-frame}`）**：宝丽来式白卡，4:3 内图片区周围 1rem 内边距。与 post-it 同样的投影，小旋转。

**图表画布（`{components.chart-canvas}`）**：承载行内 SVG 图表的白卡。与 post-it 同样的投影、小旋转。SVG 图表用便利贴调色板（黄、蓝、粉、绿）作条 / 分段。坐标轴标签用 Zilla Slab，数值标签用 Caveat。

**图画画布**：承载圆形环形 / 饼图 SVG 的白卡。处理同图表画布。SVG 分段用便利贴调色板，图例行用墨文字。

**统计行（`{components.stat-row}`）**：统计 post-it 内的标签-数值行。Zilla Slab 标签 + Shrikhand 统计值，由虚线墨-alpha 底边分隔。

**时间轴节点 + 连接**：每条时间轴行有左侧 post-it（带 phase-label Caveat 图注的时间轴节点）+ 中间虚线贝塞尔 SVG 连接 + 右侧带白边框 post-it（时间轴内容正文）。行方向在偶数行经 `flex-direction: row-reverse` 左右交替。

**涂鸦 SVG（`{components.doodle}`）**：绝对定位在页角的装饰 SVG 记号，圆、扭动、三角、线、X+ 对。3px 墨描边、0.15 不透明度。每页 0–2 个涂鸦。

**自定义光标**：SVG 图钉光标（红外圈 + 白中心），悬停在页上时替换默认光标。

## 该做与不该做

### 该做
- 每页挑一种背景变体："便签墙"能量用 `{components.bg-cork}`、"桌面"专注用 `{components.bg-paper}`、"晨光"氛围用 `{components.bg-warm}`。页间变换求触感多样。
- 每页保留 SVG 颗粒叠层（`{components.grain-overlay}`）于 4% 不透明度。它是把文稿系在纸语域上的纹理。
- 每个展示瞬间（标题、题目、特性图标、统计值）用 Shrikhand，每段正文与每个列表项用 Zilla Slab。
- 随意 / 私人便签用 Caveat，侧批注、装饰俏皮话（"Jot it down before you forget!"、":)"）、label-script eyebrow。手写脚本是系统最鲜明的声部。
- 给每张 post-it 一个小旋转（±1° 到 ±15°）。相邻便签交替旋转方向，别让任何东西对齐网格。
- 给每张 post-it、相框、图表卡、图画画布套标准柔和投影（`2px 3px 15px shadow, 0 1px 3px shadow-deep`）。
- 每张主 post-it 都经 `::before` 别一枚红图钉。post-it 颜色合适时用配色图钉变体（蓝 / 绿 / 金）。
- 英雄 / 陈述 post-it 上把图钉 + 胶带合用，作"正式贴出"处理。
- 在页角以 0.15 不透明度放小 SVG 涂鸦（圆、扭动、三角）作装饰标点。每页 1–2 个就够。
- 多卡网格里轮换 post-it 颜色（黄 → 蓝 → 粉 → 绿 → 橙 → 紫）求视觉变化。别让所有卡重复一色。

### 不该做
- 不要省掉背景纹理、让 post-it 浮在纯白视口上。带纹理背景是系统的基础视觉底。
- 不要把 Shrikhand 换成别的展示字面。粗壮装饰衬线是系统身份，换成无衬线或别的衬线会丢掉工作坊声部。
- 不要把 Caveat 换成别的脚本字面。随意草书声部锚住"手草写"语域。
- 不要用 Zilla Slab 做标题，也不要用 Shrikhand 排正文段。搭配锁死：Shrikhand 展示 + Zilla Slab 正文 + Caveat 脚本。
- 不要给 post-it 颜色赋语义（黄 = 警告、绿 = 好）。颜色只作分类。
- 不要把 post-it 旋转超过 ±15°。超过之后，手放就变歪。
- 不要把所有 post-it 朝同一方向转。相邻便签交替 ± 方向，一致性读成"画布歪了"，不是手放。
- 不要用不带 2px 墨边框的纯白作 post-it 填充。白压奶油背景会隐形。
- 不要在标题便签上省掉图钉。没图钉的标题读作漂浮、没定义。
- 不要用重叠 post-it 挤满页面。便签堆起来，俏皮能量就塌；对的密度是 1–4 张主便签加 1–2 张小点缀 / 浮动便签。

## 响应式行为

系统以 `100vw × 100vh` 为目标、通篇用 `clamp()` 流式缩放。单条 `max-width: 900px` 媒体查询把多列网格与时间轴重排成单列、中和部分旋转（versus 圆变成行内而非绝对定位）、把比较卡纵向堆叠。

### 缩放行为
- 展示标题经 `clamp(2.5rem, 5vw, 4.5rem)` 式样缩放，在最小与最大之间流动。
- 正文从最小 1rem 缩到最大 1.25rem。
- post-it 内边距不随视口缩放，固定在间距比例里的值。
- 投影、图钉尺寸、胶带尺寸、装饰 SVG 尺寸固定，与视口无关。

### 放映行为
- `ArrowRight`、`ArrowDown`、`Space`、`PageDown` 前进。
- `ArrowLeft`、`ArrowUp`、`PageUp` 后退。
- `Home` 跳到首页，`End` 跳到末页。
- 移动端横向触屏滑动前进 / 后退。
- 鼠标滚轮前进 / 后退，两次滚动间锁 700ms，防止触控板连跳。
- 自定义图钉光标在每次悬停时强化隐喻。

### 打印行为
一条 `@media print` 规则给每页设 `page-break-after: always` 与 `min-height: 100vh`。打印产出逐页顺序的 PDF。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁 | 中文 | 字重映射 |
|---|---|---|---|
| 展示 / 标题 / 陈述 / 题目 / 统计值 / 特性图标字形 | Shrikhand（400） | **站酷快乐体 ZCOOL KuaiLe** | regular（单字重） |
| 正文 / 列表项 / 副标题 | Zilla Slab（400） | **悠哉字体 Yozai** | regular |
| 手写脚本（Caveat），仅拉丁 | Caveat（400 / 500 / 600） | *（无 CJK 替代）* | 不适用 |

### 混排策略

**策略 A：展示 CJK + 正文 CJK，各有各的个性。** Scatterbrain 整个语域是俏皮-触感-温暖，中文搭配该落在同样的情绪语域里。**ZCOOL KuaiLe（站酷快乐体）** 是粗壮装饰展示字面，曲线圆润、带手绘马克笔感，是 Shrikhand 粗壮装饰衬线声部最接近的 CJK 匹配。两款字面共享定义工作坊板美学的"响亮又友好"个性。**Yozai（悠哉字体）** 是由 M+ Rounded 衍生的暖圆正文字面，带 Zilla Slab 板衬线同样的友好人文气质，柔终端读起来像写下的便签而非排印文字。两款 CJK 字面合起来保住让 Scatterbrain 声部成立的俏皮粗展示 + 暖友好正文节奏。

### 加载

```html
<link href="https://chinese-fonts-cdn.deno.dev/packages/zcool-kuaile/dist/ZCOOLKuaiLe-Regular/result.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-yozai-regular/font.css" rel="stylesheet">
```

然后把 CJK 字族追加到相应字体栈：
```css
/* Display roles */
font-family: 'Shrikhand', 'ZCOOL KuaiLe', cursive;
/* Body roles */
font-family: 'Zilla Slab', 'Yozai', serif;
```

### 通用 CJK 调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 设 0
- 文字变换：CJK 不用 uppercase
- 全角标点
- 展示标题不加句号
- 盘古之白（Pangu spacing）：`使用 Claude` 而非 `使用Claude`
- 一句一款字体

### 本系统的美学提示

- **Shrikhand 展示上的 0.02em 正字距在 ZCOOL KuaiLe 上必须降到 0**。加字距的中文展示字符看着是坏的。
- **展示行高应从 1.1 放宽到 1.2–1.3**，圆润粗壮的笔画需要更多纵向呼吸。
- **特性图标圆边框配单个汉字**（新、巧、趣）在 60px 圆里用 ZCOOL KuaiLe 格外漂亮。粗壮展示字重让单字读作盖下的类别标记。
- **Versus 圆配短中文词**（对比、与）在较小展示字重下成立，奶油压墨的反差带得过来。
- **label-script Caveat eyebrow（全大写加 0.15em 字距）是最难的翻译。** 可选做法：（1）eyebrow 保留拉丁（`CHAPTER ONE`、`THE SETUP`）求手写脚本招牌；（2）换成 0.9rem、无字距、无全大写的 Yozai eyebrow，但会丢掉分类标签的可供性。做法（1）保住系统最鲜明的小声部，且拉丁 eyebrow 坐在中文标题上方时很成立（文稿读作带英文眉题的中文文章，是常见编辑惯例）。
- **Caveat 里的私人便签 / 装饰俏皮话（`Jot it down before you forget!`、`:)`）应保持拉丁**，随意圆珠笔脚本没有可接受的中文替代。在以中文为主的页上，把手写脚本瞬间当作拉丁页边注，这其实能加深工作坊声部（文稿读作带英文旁白的中文头脑风暴，对任何现代中文创意团队都合理）。
- **Post-it 图钉、胶带、投影、旋转、自定义光标、涂鸦 SVG、背景纹理**都与字形无关，它们在中文内容背后同样扛得住俏皮触感系统。
- **统计行的标签-数值式样**配 Yozai 的中文标签（用户数量、转化率）与 ZCOOL KuaiLe 的拉丁数值，干净成立。

### 已知 CJK 缺口

Caveat，系统最鲜明的声部（锚住每条私人便签的随意圆珠笔手写脚本），没有 CJK 对应。中文确有手写风网络字体（悠果手写体、站酷庆科黄油体），但随意草书手写在中拉传统间的文化语域差别很大，没有哪款中文字面会读作"与 Caveat 同一个声音"。推荐的变通是即便在其余全中文的页上，也把 Caveat 留给拉丁页边批注，中文正文配英文手写的式样在现代中文编辑设计里很常见，读作本真而非翻译缺口。

## 迭代指南

1. 每张新页都从三种背景变体（`{components.bg-cork}`、`{components.bg-paper}`、`{components.bg-warm}`）里挑一种。页间变换求触感多样。
2. 每个新内容块都是七色之一的 post-it（黄、蓝、粉、绿、橙、紫、带边框白）。黄是默认，多卡时轮换求变化。
3. 每张新 post-it 都带小旋转。英雄 / 陈述 post-it：±1–3°。点缀 / 浮动 post-it：±5–15°。相邻之间交替方向。
4. 每张新 post-it 都带标准柔和投影（`2px 3px 15px shadow, 0 1px 3px shadow-deep`）。
5. 每张新主 post-it 都经 `::before` 带图钉（默认红，配色凝聚用蓝 / 绿 / 金变体）。
6. 英雄 / 陈述 / 收尾 post-it 经 `::after` 加一条胶带，作"正式贴出"处理。
7. 标题用 Shrikhand，尺寸从 `{typography.title}`（1.3rem，小卡标题）到 `{typography.display-hero}`（4.5rem，封面 / 收尾）。正文用 Zilla Slab，私人便签用 Caveat。
8. 特性 post-it 以一个 60px 墨边框圆特性图标开场，内含单个 Shrikhand 字符（A/B/C、1/2/3、!/✓/✗）。
9. 装饰 SVG 涂鸦（圆、扭动、三角、X 记号）每页住在 1–2 个空闲角，0.15 不透明度、3px 墨描边。
10. 图表与图画坐在白图表画布（`{components.chart-canvas}`）里，带与 post-it 相同的投影 + 小旋转。SVG 填充用便利贴调色板（黄、蓝、粉、绿）。

## 已知缺口

- 系统加载三款 Google Fonts（Shrikhand、Zilla Slab、Caveat）。Shrikhand 单字重（仅 400），试图用更重字重会回退。生产环境建议自托管。
- 自定义 SVG 图钉光标（`{components.custom-cursor}`）在所有浏览器里渲染不一致，Safari 与 Firefox 缩放或定位光标热点可能与 Chrome 不同。纯触屏设备上光标无关紧要。
- 背景纹理（`bg-cork`、`bg-paper`、`bg-warm`）用 CSS 渐变与行内 SVG data-URI 图案组合。现代浏览器渲染一致，但色调暖意会随屏幕色彩配置略变。
- 图钉（`::before`）与胶带（`::after`）占掉 post-it 两个伪元素槽位。若还需额外装饰记号（卷角、污渍等），得用真实子元素而非伪元素。
- 每张 post-it 的柔和投影添渲染开销。10 张以上 post-it 的页在低端设备上可能略显阴影渲染滞后。
- 自定义光标与绝对定位的图钉 / 胶带不会如预期与屏幕阅读器交互。装饰元素应保持对辅助技术隐藏。
- 行内 SVG 图表（条形、环形、饼图）是硬编码的，条高、分段路径、标签都烤进 SVG。没有数据绑定层，新图表值需手工重算 SVG 路径 / 位置。
- 自定义光标（红图钉）在包括文字密集页的每页都出现，用户读正文段时可能视觉吵。把光标当作全稿点缀，别当逐页的操作提示。
- 鼠标滚轮导航锁（700ms）不寻常，可能让期待平滑滚动的用户意外。触控板用户尤其可能觉得这种滚轮步进反直觉。
