---
version: alpha
name: Capsule
description: A playful editorial system built on pill-shaped containers, a sun-bleached cream canvas, and a nine-color candy palette. Bodoni Moda serif headlines pair with Space Grotesk body to suggest a literary magazine that took a holiday at a 1970s ice-cream parlor. Every container that holds text is a pill (border-radius 9999px) outlined with a 2px ink stroke, casting a soft 6–12px offset shadow. The aesthetic is "Memphis-meets-editorial" — confident typography, generous bordered shapes, and decorative floating pills as atmospheric wallpaper.

colors:
  cream: "#F5F5F0"
  ink: "#1A1A1A"
  outline: "#1E1E1E"
  white: "#FFFFFF"
  coral: "#E85D4E"
  lime: "#C4D94E"
  lavender: "#C5B5E0"
  sky: "#8BB4F7"
  violet: "#A06CE8"
  yellow: "#F2D160"
  peach: "#F5B895"
  mint: "#A8E6CF"
  shadow: "rgba(26, 26, 26, 0.08)"

color-aliases:
  bg: cream
  fg: ink
  outline: outline                  # same hue family as ink; reserved for stroke role

typography:
  display:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(3rem, 8vw, 7rem)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.02em
  closing-display:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(2.5rem, 6vw, 5rem)"
    fontWeight: 800
    lineHeight: 0.95
    letterSpacing: -0.03em
  headline:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(2rem, 4vw, 3.5rem)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.02em
  section-headline:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(1.8rem, 3.5vw, 3rem)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.01em
  quote-display:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(1.6rem, 3.5vw, 3rem)"
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.01em
  card-headline:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.1
  stat-number:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(2rem, 3.5vw, 3rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: -0.03em
  orbit-numeral:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "2.5rem"
    fontWeight: 700
    lineHeight: 1
  body:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "clamp(0.95rem, 1.2vw, 1.15rem)"
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.55
  subtitle:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "clamp(0.8rem, 1.5vw, 1.1rem)"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.15em
    textTransform: uppercase
  pill-text-md:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  pill-text-sm:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.7rem"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  label:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  mini-label:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.65rem"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase

spacing:
  pad-lg: "3rem 4rem"
  pad-md: "2rem"
  gap-xl: "4rem"
  gap-lg: "3rem"
  gap-md: "2rem"
  gap-sm: "1.5rem"
  gap-xs: "0.75rem"
  card-pad: "2.5rem 2rem"
  pill-pad-lg: "1.5rem 3.5rem"
  pill-pad-md: "1rem 2.5rem"
  pill-pad-sm: "0.4rem 1.2rem"
  pill-pad-xs: "0.35rem 1rem"

canvas:
  width: 100vw
  height: 100vh

components:
  pill:
    borderRadius: 9999px
    border: "2px solid {colors.outline}"
    fontFamily: "Space Grotesk, sans-serif"
    fontWeight: 500
    letterSpacing: 0.02em
    whiteSpace: nowrap
    description: "The universal container shape. Any text container — chip, button, label, statement-highlight, stat tile, card, bar — is a pill with 2px outline. Background can be any palette accent or white."
  pill-card:
    background: "{colors.white}"
    border: "2px solid {colors.outline}"
    borderRadius: "2rem"
    padding: "{spacing.card-pad}"
    boxShadow: "8px 8px 0 {colors.shadow}"
    description: "Larger pill-shaped card (slightly squared corners at 2rem rather than full pill) for content blocks. Always white background, always shadowed."
  stat-pill:
    background: "{colors.white}"
    border: "2px solid {colors.outline}"
    borderRadius: "2rem"
    padding: "2rem 1.5rem"
    boxShadow: "6px 6px 0 {colors.shadow}"
    description: "Stat tile — pill-shaped white card containing a colored stat number, label, and a tiny accent bar."
  bar-track:
    height: 36px
    background: "{colors.cream}"
    border: "2px solid {colors.outline}"
    borderRadius: 9999px
    overflow: hidden
    description: "Horizontal bar chart track shaped as a pill. Fills use the candy palette."
  bar-fill:
    height: "100%"
    borderRadius: 9999px
    borderRight: "2px solid {colors.outline}"
    description: "Inner bar pill with the value label printed at right edge inside the fill."
  accent-line:
    width: 60px
    height: 4px
    background: "{colors.coral}"
    borderRadius: 9999px
    description: "Pill-shaped 60×4 accent rule. Default color coral; closing-context variant uses 80×4."
  card-icon:
    width: 60px
    height: 60px
    borderRadius: "50%"
    border: "2px solid {colors.outline}"
    fontFamily: "Bodoni Moda, serif"
    fontSize: "1.5rem"
    fontWeight: 700
    description: "Circular pill icon (60px) used as a card mark. Background is an accent color; contains a 1–3 character Roman numeral or letter."
  step-node:
    width: 56px
    height: 56px
    borderRadius: "50%"
    border: "2px solid {colors.outline}"
    background: "{colors.white}"
    fontFamily: "Bodoni Moda, serif"
    fontSize: "1.3rem"
    fontWeight: 700
    boxShadow: "4px 4px 0 {colors.shadow}"
    description: "Circular pill node (56px) used as a timeline step or sequence marker. Step accent color appears as filled-pill class on the node."
  orbit-center:
    width: 160px
    height: 160px
    borderRadius: "50%"
    background: "{colors.lime}"
    border: "2px solid {colors.outline}"
    fontFamily: "Bodoni Moda, serif"
    fontSize: "2.5rem"
    fontWeight: 700
    description: "Large circular pill (160px) used as the gravitational anchor of an orbit composition. Default fill lime; small satellite pills orbit around it."
  diagram-node:
    borderRadius: 9999px
    border: "2px solid {colors.outline}"
    padding: "1rem 2rem"
    boxShadow: "6px 6px 0 {colors.shadow}"
    background: "{colors.white}"
    description: "Flow-diagram node — pill-shaped container with shadow. Connected by 50×4 ink connectors with triangular arrowheads."
  diagram-connector:
    width: 50px
    height: 4px
    background: "{colors.outline}"
    description: "Solid 50×4 ink bar with a triangular arrowhead at the right end, connecting two diagram nodes inline."
  visual-frame:
    borderRadius: "2rem"
    border: "2px solid {colors.outline}"
    boxShadow: "12px 12px 0 {colors.shadow}"
    description: "Large image/illustration frame — slightly squared pill (2rem radius) with thicker 12px offset shadow. Often filled with a tri-stop linear gradient and a dot-pattern overlay."
  grain-overlay:
    position: fixed
    inset: 0
    pointerEvents: none
    zIndex: 9999
    opacity: 0.04
    mixBlendMode: multiply
    backgroundImage: "fractalNoise SVG"
    description: "Subtle film-grain noise overlay applied to the entire viewport at 4% opacity in multiply blend mode. Always present, never absent."
  radial-glow:
    description: "Soft radial gradient wash anchored to a corner or center of a slide background. Uses one of the candy palette colors at 6–15% opacity, blended into the cream canvas. Provides atmospheric warmth without changing the surface color."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/capsule/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Capsule 是一套**俏皮的编辑式系统**，定义性的结构前提是**胶囊**：每个文字容器是胶囊，每个图标是胶囊，每根条是胶囊，图里每个节点都是胶囊。`border-radius: 9999px` 规则几乎套在所有 UI 元素上，较大的面板软化到 2rem 半径。配上包裹每个形状的 2px 墨色描边，结果是一套容器显得鼓胀、友好、图形上彼此分明，向孟菲斯设计与 70 年代末冰淇淋店招牌致意，又不丢编辑纪律。

字面栈是刻意的两字面对话。**Bodoni Moda**，高对比的迪多尼衬线，承载每个展示瞬间、每个分节标题、每个统计数字、每个卡片标题、每段引文。Bodoni 的高大 capitals 与粗细笔画对比，给标题带来编辑分量和一抹时尚杂志的华彩。**Space Grotesk**，当代几何无衬线，承载每个正文段落、每个标签、每片胶囊文字、每个副标题。衬线/怪诞的搭配造出系统主要的排印节奏：华丽的衬线陈述 + 干净的怪诞辅助结构。

配色跑九种颜色加三种中性色。画布是 `{colors.cream}`，暖调日晒米白，传递"杂志纸"而非"屏幕白"。墨是 `{colors.ink}`，用于正文、标题与通用描边。七种糖果强调色 `{colors.coral}`、`{colors.lime}`、`{colors.lavender}`、`{colors.sky}`、`{colors.violet}`、`{colors.yellow}`、`{colors.peach}`，再加 `{colors.mint}`，彼此可互换。它们填充胶囊、给统计数字上色、填条形图、作装饰氛围漂浮。没有语义映射：没有颜色代表"警告"，也没有代表"成功"。每种强调色按构图平衡挑选，不按含义。

纵深来自 **4px、6px、8px、12px 的柔和硬边偏移阴影**，颜色是低不透明度墨色（`{colors.shadow}` = `rgba(26, 26, 26, 0.08)`）。与真正的粗野阴影不同，这些略带透明，读起来是"被抬起"而非"被盖印"。配上 2px 描边，每片胶囊都像浮在奶油画布上方一点点。不用模糊投影，偏移始终实色、始终朝右下。

**密度取向：中高，氛围饱满。** Capsule 页面显得热闹。系统围绕一个想法构建：装饰性漂浮胶囊应当像壁纸一样环绕真正的内容，小小的彩色胶囊以 5–25° 旋转散在页面背景上，各装一个大写单词。这些氛围胶囊不带功能，是排印彩纸。构图正确的一页，把一两个实质内容块（胶囊卡片、统计网格、图示）配上边缘 5–8 片漂浮装饰胶囊。在 Capsule 里显得坏掉的页，是角落空着、或大片奶油无处缓解的页：糖果配色即便内容并不严格需要，也想参与进来。

**关键特征：**
- 通用胶囊几何：小容器 `border-radius: 9999px`，较大卡片/画框用 2rem。
- 2px 实线 `{colors.outline}` 描边包裹每片胶囊、每个图标、每张卡片。
- Bodoni Moda 衬线用于每个展示/标题/统计；Space Grotesk 无衬线用于每个正文/标签/胶囊文字。
- 日晒奶油画布 `{colors.cream}` 配糖果强调色 6–15% 不透明度的柔和径向辉光作背景氛围。
- 低不透明度墨色（`{colors.shadow}`）的硬边偏移阴影，4/6/8/12px 偏移，始终实色、始终右下。
- 九色糖果强调配色可互换使用，无语义映射。
- 以 5–25° 旋转的漂浮装饰胶囊铺满页面背景，作氛围壁纸。
- 常驻的分形噪声颗粒叠层（4% 不透明度、multiply 混合）始终盖在整个视口上。
- 全屏竖向导航点列在右侧，等宽页码在右下。

## 颜色

### 画布与墨
- **Cream**（`{colors.cream}` — #F5F5F0）：画布。暖调日晒米白。用作默认幻灯片背景、默认条轨内部，以及任何想要纸感暖意又不想纯白的中性区域。
- **Ink**（`{colors.ink}` — #1A1A1A）：主文字色。用于标题、正文，以及（以 `outline` 别名）通用描边。
- **Outline**（`{colors.outline}` — #1E1E1E）：功能上等同 ink；为语义清晰，专门留作每片胶囊、卡片、图标、画框的描边色。
- **White**（`{colors.white}` — #FFFFFF）：真白。用作胶囊卡片、统计胶囊、图示节点，以及任何需要与奶油画布最高对比的胶囊的默认填充。白胶囊始终带 2px 墨色描边。

### 糖果强调色
- **Coral**（`{colors.coral}` — #E85D4E）：暖橙红。强调色里最"有嗓门"的一色；用作默认强调线色、序列首张卡片上默认的胶囊卡片图标填充，也是最常见的统计数字色。
- **Lime**（`{colors.lime}` — #C4D94E）：鲜亮的黄绿。与珊瑚很搭；用作 orbit 中心锚点默认填充和常见统计数字色。
- **Lavender**（`{colors.lavender}` — #C5B5E0）：柔和淡紫。用作页眉里令人平静的胶囊填充，以及常见的引文高亮色。
- **Sky**（`{colors.sky}` — #8BB4F7）：中饱和矢车菊蓝。默认"第三强调"，在三卡网格里与珊瑚、青柠并排放着舒服。
- **Violet**（`{colors.violet}` — #A06CE8）：更深紫。当某页已有薰衣草作一个强调、还需要同紫系的第二个爆点时使用。
- **Yellow**（`{colors.yellow}` — #F2D160）：暖金盏花。标题胶囊、收尾胶囊，以及任何该读作"重要 / 精选"的胶囊的默认填充。
- **Peach**（`{colors.peach}` — #F5B895）：淡杏。最柔的强调色，用于漂浮装饰胶囊和圆形装饰点。
- **Mint**（`{colors.mint}` — #A8E6CF）：淡青绿。最常用于线性渐变视觉画框内部和低强调的装饰胶囊。
- **Shadow**（`{colors.shadow}` — `rgba(26, 26, 26, 0.08)`）：通用柔和硬边偏移阴影色。绝不用别的阴影色。

### 默认值
- **默认幻灯片表面**：`{colors.cream}`。
- **默认标题色**：`{colors.ink}`，Bodoni 衬线标题永远是墨色，绝不上彩。颜色只出现在统计数字和强调胶囊内部。
- **默认正文文字色**：`{colors.ink}` 以 0.6–0.7 不透明度渲染，柔化它以贴合奶油画布。
- **默认描边色**：`{colors.outline}`（≈ ink），每片胶囊/卡片/图标 2px，无例外。
- **默认卡片填充**：`{colors.white}`。
- **默认强调线色**：`{colors.coral}`。
- **默认标题胶囊填充**：`{colors.yellow}`。
- **默认收尾胶囊填充**：`{colors.yellow}`。
- **默认 orbit 中心填充**：`{colors.lime}`。
- **3 色或 4 色强调序列里的默认首色**：珊瑚 → 青柠 → 天蓝 → 紫罗兰（需要更多色时轮转）。这个序列是系统的"Roy G. Biv"，给 Agent 一个确定顺序可循，糖果配色才不会显得随机。
- **默认装饰胶囊背景不透明度**：全饱和（不淡出）。漂浮胶囊刻意就是响的。

强调色没有语义角色。按冷暖平衡与相邻关系挑色，不按含义。三种强调色同现时，把暖（珊瑚/黄/桃）、冷（天蓝/薰衣草/紫罗兰/薄荷）、中性亮（青柠）搭在一起。避免把同系两色相邻（两紫、两绿、两暖）。

## 排印

### 字族
系统跑在**两字面对话**上：`Bodoni Moda`（衬线，字重 400–900，opsz 轴）承载每个展示与标题；`Space Grotesk`（无衬线，字重 300–700）承载每个正文、标签、胶囊文字。没有第三字面。两款字族都以可变轴字重从 Google Fonts 加载。

Bodoni Moda 的高对比与迪多尼调制给系统带来编辑华彩语域；粗细笔画对比在大尺寸下最明显，所以展示字重应始终 700+ 以保住笔画存在感。Space Grotesk 的几何怪诞体承载干净、现代的正文，从不试图与 Bodoni 标题争。

Bodoni 标题里的行内 `<em>` 保持 Bodoni 并切到斜体。Bodoni 引文正文里的 `quote-highlight` 把被包的词换成一片胶囊（糖果底上的 Space Grotesk 大写胶囊文字）作视觉强调。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | clamp(3rem, 8vw, 7rem) | Bodoni Moda | 800 | 最大封面/标题展示 |
| `{typography.closing-display}` | clamp(2.5rem, 6vw, 5rem) | Bodoni Moda | 800 | 收束性宣告标题 |
| `{typography.headline}` | clamp(2rem, 4vw, 3.5rem) | Bodoni Moda | 700 | 分栏或双栏布局上的页面主标题 |
| `{typography.section-headline}` | clamp(1.8rem, 3.5vw, 3rem) | Bodoni Moda | 700 | 卡片/图表上方的分节开场或居中标题 |
| `{typography.quote-display}` | clamp(1.6rem, 3.5vw, 3rem) | Bodoni Moda | 600 | 拉页引文正文 |
| `{typography.card-headline}` | 1.5rem | Bodoni Moda | 700 | 卡片或支柱块标题 |
| `{typography.stat-number}` | clamp(2rem, 3.5vw, 3rem) | Bodoni Moda | 800 | 大号数值统计数字 |
| `{typography.orbit-numeral}` | 2.5rem | Bodoni Moda | 700 | orbit 中心圆内的居中序数 |
| `{typography.body}` | clamp(0.95rem, 1.2vw, 1.15rem) | Space Grotesk | 400 | 段落正文 |
| `{typography.body-sm}` | 0.9rem | Space Grotesk | 400 | 卡片内紧凑正文 |
| `{typography.subtitle}` | clamp(0.8rem, 1.5vw, 1.1rem) | Space Grotesk | 400 | 展示标题下方的大写宽字距副标题 |
| `{typography.pill-text-md}` | 0.85rem | Space Grotesk | 600 | 标题/收尾胶囊内文字 |
| `{typography.pill-text-sm}` | 0.7rem | Space Grotesk | 600 | 小型漂浮装饰胶囊内文字 |
| `{typography.label}` | 0.75rem | Space Grotesk | 500 | 页眉小片胶囊、出处行 |
| `{typography.mini-label}` | 0.65rem | Space Grotesk | 500 | 小片簇里的迷你胶囊芯片 |

### 默认值
- **分节主标题默认尺寸**：`{typography.section-headline}`（clamp 1.8–3rem）。双栏或分栏布局用 `{typography.headline}`（clamp 2–3.5rem）。
- **封面或开场展示瞬间默认尺寸**：`{typography.display}`（clamp 3–7rem）。
- **段落正文默认尺寸**：`{typography.body}`（clamp 0.95–1.15rem）。
- **任何行内标签或芯片默认尺寸**：`{typography.label}`（0.75rem）。
- **任何 Bodoni 展示元素默认字重**：最低 700，最大展示用 800。
- **任何 Space Grotesk 正文元素默认字重**：400。
- **英雄统计数字默认尺寸**：`{typography.stat-number}`（clamp 2–3rem）。

拿不准时，页面主要文字瞬间取 `{typography.section-headline}`，不要用 `{typography.card-headline}`（后者留给卡片内的块级标题）。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个 display、headline、stat-number、card-headline、quote-display 元素都用 Bodoni Moda。** Space Grotesk 不出现在任何展示角色里。
- **每个 body、subtitle、pill-text、label、芯片元素都用 Space Grotesk。** Bodoni 不出现在正文或芯片角色里。
- **每个 Bodoni 展示元素都用负字距**（-0.01em 到 -0.03em）。大尺寸 Bodoni 用默认字距读起来松。
- **每个 Space Grotesk 副标题、标签、胶囊文字、芯片元素都大写、0.08em+ 字距。** 大写 + 字距是小文字的身份信号。
- **Bodoni 标题始终以 `{colors.ink}` 渲染，绝不用糖果色。** 颜色出现在统计数字上（例如 `color: {colors.coral}`），但不出现在衬线标题上。例外是 orbit 中心数字，它坐在彩色圆胶囊内，但数字本身仍是墨色。
- **每片胶囊元素都带 2px 实线描边。** 没有 2px 墨色描边的胶囊会破掉系统。
- **每个 `border-radius: 9999px` 或 `2rem` 的容器，要么自带 2px 描边，要么坐在一个已描边的父容器内。** 不带描边的圆角容器不存在。
- **每张卡片或抬升胶囊都带硬边偏移阴影**，4/6/8/12px、`{colors.shadow}`。小胶囊用 4–6px，卡片用 8px，视觉画框用 12px。

### 排印原则
Bodoni 标题 + Space Grotesk 正文的搭配是主要节奏，换掉任一款字面都会破系统。斜体只通过 `<em>` 标签出现在拉页引文正文里（Bodoni 斜体）。不用下划线。胶囊包裹是系统主要的强调机制：把短语包进糖果填充的胶囊，等同于传统编辑系统里的粗斜体强调。

行高随尺度收紧：`{typography.display}` 0.9，`{typography.headline}` 1.05，正文 1.6。紧展示 + 松正文的反差，给系统带来编辑呼吸节奏。

## 布局

### 画布系统
画布是 `100vw × 100vh`，全视口、溢出隐藏。每张 `.slide` 绝对定位铺满视口，同一时刻一张带 `.active`（opacity 1）。过渡是 0.6s 的 `cubic-bezier(0.4, 0, 0.2, 1)` opacity 淡入。所有尺寸用 CSS `clamp()` 里的 rem 单位，布局流畅缩放。

### 内边距与间隙比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-lg}` | 3rem 4rem | 默认幻灯片外内边距 |
| `{spacing.gap-xl}` | 4rem | 主双栏栏间距 |
| `{spacing.gap-lg}` | 3rem | 分节块间距 |
| `{spacing.gap-md}` | 2rem | 标准元素间距 |
| `{spacing.gap-sm}` | 1.5rem | 卡片内紧间距 |
| `{spacing.gap-xs}` | 0.75rem | 迷你胶囊之间的行内间隙 |
| `{spacing.card-pad}` | 2.5rem 2rem | 默认支柱卡片内边距 |
| `{spacing.pill-pad-lg}` | 1.5rem 3.5rem | 标题胶囊 / 收尾胶囊内边距 |
| `{spacing.pill-pad-md}` | 1rem 2.5rem | 精选胶囊内边距 |
| `{spacing.pill-pad-sm}` | 0.4rem 1.2rem | 页眉小片胶囊内边距 |
| `{spacing.pill-pad-xs}` | 0.35rem 1rem | 迷你胶囊芯片内边距 |

### 氛围背景层
每页都在奶油画布上叠两层氛围处理：
1. **径向辉光**：一到三团柔和的 `radial-gradient(ellipse at X% Y%, rgba(accent, 0.06–0.15), transparent)`，锚在角落或中心。它们给画布暖暖地染上色，却不改表面颜色本身。
2. **颗粒叠层**：分形噪声 SVG 固定在 `inset: 0`，不透明度 0.04，mix-blend-mode multiply，z-index 9999。始终存在、始终一致、绝不移除。

这些不是可选装饰，而是应出现在每页上的基线画布处理。

### 装饰胶囊壁纸
一个签名手法：小型装饰胶囊（60–160px 宽、35–90px 高）以 -20° 到 +25° 旋转绝对定位在页面背景上，作氛围排印彩纸。每片装一个大写 Space Grotesk 单词和一种糖果填充。有些是圆形（border-radius 50%）而非胶囊形。它们不带信息角色，纯视觉氛围。典型数量：封面/收尾/引文布局每页 5–8 片，密集数据布局 0 片。

## 纵深与层级

### 柔和硬边偏移阴影
系统唯一的纵深手法是低不透明度墨色的**实色硬边偏移阴影**：
- **4px 4px 0**：小型抬升节点（步骤节点、小胶囊）。
- **6px 6px 0**：orbit 胶囊、统计胶囊、图示节点。
- **8px 8px 0**：支柱卡片、图表容器。
- **12px 12px 0**：大视觉画框（系统里抬得最高的元素）。

所有阴影用 `{colors.shadow}`（`rgba(26, 26, 26, 0.08)`）。不透明度是与粗野硬阴影的关键区别：8% 下阴影读成柔和抬起，而非盖印偏移。偏移方向始终右下。

### 基于描边的纵深
大部分表面纵深来自包裹每片胶囊、贴着奶油画布的 2px 墨色描边。描边承担了大部分抬升工作，阴影则给卡片与抬升胶囊补上那一点抬起。

### 平的装饰层
装饰性漂浮胶囊与径向辉光是平的，不投阴影。阴影只留给承载内容的容器（卡片、统计块、图示节点、视觉画框）。这条视觉规则让人一眼分出"内容"与"氛围"。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 9999px（全胶囊） | 所有小胶囊：标题胶囊、收尾胶囊、装饰胶囊、页眉小片、迷你芯片、条轨、条填充、强调线、orbit 胶囊、漂浮胶囊、引文高亮、图示节点 |
| 2rem（32px） | 较大卡片：支柱卡片、统计胶囊、图表容器、视觉画框 |
| 1.5rem（24px） | 视觉画框内部的虚线内框 |
| 50%（圆） | 圆形胶囊：card-icon（60px）、step-node（56px）、orbit-center（160px）、导航点（10px） |
| 0 | 颗粒叠层、幻灯片本身、视觉画框内的糖果色渐变区域 |

系统**没有尖角文字容器**。每个装文字或图标内容的容器都是圆角。

### 边框粗细
- **2px 实线 `{colors.outline}`**：通用描边。用于每片胶囊、卡片、图标、画框、条轨、导航点。
- **2px 虚线 `{colors.outline}`**：只用于 visual-frame 组件内的内框（一条提示"图片占位"的装饰内边）。
- **4px 实线墨**：只用于横向连接连续步骤节点的时间轴线。

所有边框都是 `{colors.outline}`。系统里不存在彩色边框。

### 装饰元素类型

**装饰漂浮胶囊**：小型（60–160px 宽 × 35–90px 高）胶囊或圆形，糖果填充，倾斜 -20° 到 +25° 旋转，绝对定位在页面背景上。内含一个 0.55–0.85rem 的大写 Space Grotesk 单词。作用如排印彩纸 / 氛围壁纸。宣告式页面 5–8 片。

**页眉小片胶囊**：小型（约 0.7rem 文字）胶囊，糖果填充（通常薰衣草），用 `pill-pad-sm` 内边距，居中放在分节标题上方。系统的分节标签芯片。

**标题胶囊 / 收尾胶囊**：中等胶囊（`pill-pad-lg`），`{colors.yellow}` 填充，承载大写 Space Grotesk 文字。放在封面与收尾页最大展示标题上方。

**支柱卡片**：2rem 半径的白卡片，2px 描边 + 8px 偏移阴影，顶部一枚圆形 `card-icon`，一个 Bodoni `card-headline`，一段 Space Grotesk 正文段落。用于 3 卡和 4 卡网格。

**统计胶囊**：2rem 半径的白卡片，装一个彩色 Bodoni 统计数字、一个小大写标签、底部一条 40×4 的小强调条。坐在 3 列或 4 列统计网格里。

**条轨**：36px 高的横向胶囊（9999px 半径），2px 描边、奶油内部。填充是子胶囊，糖果色，数值标签印在填充内右边缘。

**Orbit 构图**：中央 160px 圆形胶囊，`{colors.lime}` 填充，承载一个 Bodoni 序数，周围 4–6 片糖果填充的小 `orbit-pill` 卫星，各自倾斜，以 8–45% / 8–45% 偏移定位，带 6px 阴影。

**图示节点 + 连接线**：胶囊形流程节点（`diagram-node`），6px 阴影，由一根 50×4 墨条配三角箭头连到下一节点。节点可带糖果填充，箭头始终墨色。

**视觉画框**：2rem 半径的大画框，12px 偏移阴影，填三段线性渐变（通常薰衣草 → 天蓝 → 薄荷），叠 0.15 不透明度的点网格图案，内带虚线边提示"图片占位"。用于英雄视觉瞬间。

**引文高亮**：行内胶囊，青柠或天蓝，2px 描边，包住 Bodoni 引文正文里的一个短语。系统主要的行内强调机制。

**强调线**：60×4（收尾页 80×4）的横向胶囊，`{colors.coral}`，作副标题下的强调线。

## 该做与不该做

### 该做
- 把每个文字容器做成胶囊：小胶囊 9999px 半径，较大卡片 2rem 半径。胶囊几何是系统最鲜明的单项特征。
- 给每片胶囊、卡片、图标、画框套 2px `{colors.outline}` 描边。正是描边让糖果配色读起来像图形，而不是糖果。
- 每个 Bodoni 展示元素都用 `{colors.ink}`，绝不用糖果色。颜色属于统计数字和胶囊填充，不属于衬线标题。
- 每个标题/统计/卡片标题用 Bodoni Moda，每个正文/标签/胶囊用 Space Grotesk。两字面切分不可商量。
- 阴影渲染成 4/6/8/12px 的实色硬偏移，用 `{colors.shadow}`（`rgba(26,26,26,0.08)`）。绝不模糊，绝不换色。
- 封面、收尾、引文及其他宣告式布局的页面背景铺 5–8 片以 -20° 到 +25° 旋转的漂浮装饰胶囊。壁纸胶囊处理是系统签名。
- 每页都往奶油画布里叠径向渐变强调辉光（6–15% 不透明度）作氛围暖意。
- 每页保持颗粒叠层（4% 不透明度、multiply 混合）激活，它是基线层，不是可选装饰。
- 在 Bodoni 引文正文里，把行内强调短语包进 `quote-highlight` 胶囊（青柠、天蓝或别的糖果），而不是加粗或斜体。
- 把暖 + 冷强调色相邻搭：珊瑚配天蓝、黄配薰衣草、桃配薄荷。避免两个同系强调色相邻。

### 不该做
- 不要把任何文字容器渲染成尖角。Capsule 里不存在方角文字容器。
- 不要渲染没有 2px 墨色描边的胶囊、卡片或图标。描边是系统的身份。
- 不要把 Bodoni 标题渲染成糖果色。标题永远 `{colors.ink}`，颜色活在统计数字和胶囊填充里。
- 不要用模糊投影。阴影始终是 4/6/8/12px 的实色偏移，`{colors.shadow}`。
- 不要给 Bodoni 换别的无衬线搭档。Bodoni Moda + Space Grotesk 的搭配是固定的。
- 不要在 Bodoni 标题上用大写。系统里的 Bodoni 是句首大写（专有名词才用真正的标题式大写）。
- 不要在 Space Grotesk 副标题、标签、胶囊文字上用句首大写。小号 Space Grotesk 文字始终大写 + 0.08em 字距。
- 不要引入第十种强调色。九种糖果强调色是封闭配色。
- 不要给装饰漂浮胶囊加阴影。阴影只留给承载内容的容器。
- 不要在宣告式布局里留着空角落。奶油画布想要氛围胶囊或径向辉光，光秃秃的角落读起来像坏了。

## 响应式行为

Capsule 是视口流式的 1920×1080 演示系统，通篇用 `clamp()` 与视口相对单位。有一个 `@media (max-width: 900px)` 断点把网格列收成单列堆叠并隐藏导航点列，600px 以下统计网格进一步从 2 列收到 1 列。其余部分无断点响应式。

### 缩放行为
- 展示标题从最小视口 3rem 缩放到最大 7rem。
- 正文从 0.95rem 缩放到 1.15rem。
- 内边距在各布局选择器里通过 `clamp` 缩放。
- 边框、胶囊描边、阴影偏移、颗粒叠层固定不缩放。

### 放映行为
- 用 `ArrowRight`、`ArrowDown` 或 `Space` 前进。
- 用 `ArrowLeft` 或 `ArrowUp` 后退。
- `Home` 跳首页，`End` 跳末页。
- 触摸滑动（横向）：滑动距离 >50px 前进或后退。
- 激活页带 `.active`（opacity 1），非激活页 opacity 0 + pointer-events none。
- 导航点是右边缘的竖列，页码在右下，键盘提示在左下。

### 打印 / 导出
未明确处理；opacity 切换意味着朴素打印只能抓到激活页。导出流程应逐页按 1920×1080 单独截图。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 推荐中文搭配 | 来源 |
|---|---|---|---|
| 展示 / 标题（Bodoni Moda 700–800） | Bodoni Moda | 站酷小薇体 ZCOOL XiaoWei | Google Fonts |
| 正文 / 胶囊文字（Space Grotesk 400–600） | Space Grotesk | 悠哉字体 Yozai | cn-fontsource CDN |

### 混排策略

用**策略 A — 单字体栈带回退**：在同一条 `font-family` 栈里把 CJK 字体声明在拉丁字体**之后**，这样拉丁字形渲染成 Bodoni Moda / Space Grotesk，CJK 字形自动落到中文字面。每个角色一条 CSS 规则，无需手动切类。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Space+Grotesk:wght@300..700&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-yozai-regular/font.css" rel="stylesheet">
```

```css
:root {
  --font-display: "Bodoni Moda", "ZCOOL XiaoWei", serif;
  --font-body: "Space Grotesk", "Yozai", sans-serif;
}
```

### 通用 CJK 调整

- **行高**：把 CJK 正文行高提到约 1.7（从 1.6 上调），汉字比拉丁小写需要更多纵向呼吸。
- **字距**：把汉字段上的 `letter-spacing` 清零（讨好 Bodoni capitals 的负字距会把汉字笔画挤在一起）。紧字距只保留在拉丁 span 上。
- **文字变换**：任何胶囊/标签/副标题内容是汉字时，去掉 `text-transform: uppercase`。中文没有大小写；强制大写对汉字无效，却会破坏里面混排的拉丁缩写的渲染。
- **标点**：中文句子用中文全角标点（，。：；「」），拉丁用半角（`,.:;""`）。绝不把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略末尾的 。，展示字符串里要去掉。
- **盘古之白**：相邻的汉字与拉丁/数字串之间插入一个细空格（或普通空格），例如 `2026 年`、`AI 产品`，提升混排可读性。
- **一句一款字体**：不要在句中切换 CJK 字族。按角色在 ZCOOL XiaoWei 或 Yozai 里挑一款给某段文字，绝不在同一短语里两款都用。

### 美学提示

ZCOOL XiaoWei 是一款偏文学衬线的高对比汉字展示字面，粗细笔画调制呼应 Bodoni Moda 的迪多尼语域，给展示标题带来与拉丁原版同样的编辑华彩分量。Yozai 是友好的圆体汉字无衬线，开放的字怀与适度的笔画对比映照 Space Grotesk 的几何怪诞体，于是胶囊文字、标签、正文段落保住"干净现代无衬线"的感觉，而不退回生硬的系统汉字。两款都与糖果配色搭得干净：ZCOOL XiaoWei 用 `{colors.ink}`，守住"Bodoni 标题绝不上彩"的规则；Yozai 坐在珊瑚 / 青柠 / 黄色胶囊里，配 2px 墨色描边仍清晰。装饰漂浮胶囊壁纸在中文里照样成立，把英文大写彩纸换成单字或双字氛围词（愿景、未来、下一步）即可。

### 已知 CJK 缺口

ZCOOL XiaoWei 是展示字面，字重轴有限（单字重），字形集比 Noto 家族小，生僻或技术汉字（罕见姓氏、古字、GB2312 之外的仅简体变体）可能回退到系统字体。繁体中文文稿把 Yozai 换成 `LXGW WenKai TC`（Google Fonts），它繁体覆盖更全、同样带友好的人文语域。Bodoni 借 opsz 轴做到的 ZCOOL XiaoWei 斜体 / 重磅瞬间，中文字面没有对应，拉丁里靠斜体 Bodoni 的地方要改用尺寸和颜色补偿。

## 迭代指南

1. 任何装文字的新容器都用胶囊几何：小容器 9999px 半径，卡片 2rem 半径。别引入尖角文字容器。
2. 任何新胶囊都带 2px 实线 `{colors.outline}` 描边。别渲染无描边胶囊。
3. 任何新标题都用 `{colors.ink}` 的 Bodoni Moda。别给衬线标题上色，别切到 Space Grotesk 做展示。
4. 任何新卡片都带 `8px 8px 0 {colors.shadow}` 偏移阴影（小节点 4px，视觉画框 12px）。别模糊，别换色。
5. 任何新强调色都按珊瑚 → 青柠 → 天蓝 → 紫罗兰 → 黄 → 薰衣草 → 桃 → 薄荷的默认序列取九色糖果配色。别引入第十色。
6. 任何新宣告式页面（封面、收尾、引文、陈述）都配 5–8 片漂浮装饰胶囊作氛围壁纸。
7. 任何新数据页都在画布背景里配一到两团径向强调辉光。别让奶油表面平着。
8. Bodoni 引文正文里的任何行内强调都用 `quote-highlight` 胶囊。别加粗；除通过 `<em>` 里的 Bodoni 斜体轴外，别用斜体。
9. 新组件继承胶囊几何 + 2px 描边 + 4–12px 阴影模式。若新组件破掉这三条之一，先重新设计再纳入。
10. 新组件的文字内容（单大写 Space Grotesk 词）属于视觉身份的一部分，词不带信息；新构图应挑中性的单字氛围词（"VISION"、"FUTURE"、"NEXT" 等），别用与内容相关的文字。

## 已知缺口

- 加载了两条 Bodoni 字体轴（斜体与 opsz 6..96），但模板只以固定尺寸用正体轴，没有显式启用跨展示尺寸的光学尺寸变化。
- 条形图数值通过 `style="width: NN%"` 内联设定，没有数据绑定层。
- 装饰漂浮胶囊的位置与旋转全靠逐实例内联样式手调，没有生成式排布系统。
- 视觉画框的三段渐变（薰衣草 → 天蓝 → 薄荷）是硬编码的"默认"，别的渐变组合有效，但得逐实例编写。
- 颗粒叠层用内联 SVG data URL，替换或移除要改标记，不是改 CSS 变量。
- 条填充 2px 实线描边的 border-right 正是条端胶囊感的来源，去掉会丢掉条上的胶囊美学。
- 系统继承了全部 9 个糖果强调 CSS 变量，源码里只活跃使用约 6 个，桃与薄荷在配色里存在但用得省。它们可供新构图使用。
- 装饰漂浮胶囊把文字内容当作视觉身份的一部分（单个大写 Space Grotesk 词）。词不带信息，新构图应挑中性单字氛围词，别用与内容相关的文字。
