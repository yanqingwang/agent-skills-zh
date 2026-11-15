---
version: alpha
name: Soft Editorial
description: A warm magazine spread aesthetic — the kind of layout a small print quarterly with field-notes pretensions would commission. Cormorant Garamond carries every headline and ornamental moment with mixed roman and italic; Work Sans recedes into supporting body. The palette is cream paper with a quartet of pastel candy accents (dusty pink, chartreuse lemon, soft peach blush, sage green, lilac) used as colored card backgrounds. Generous rounded cards (24–36px radius) float on translucent white over the cream field. The mood is editorial calm with a sprinkling of riso-print color — closer to a literary research notebook than a corporate deck.

colors:
  paper: "#F2EEDF"
  paper-2: "#ECE6D2"
  ink: "#2A241B"
  ink-soft: "#5C5345"
  pink: "#E1A4C2"
  lemon: "#D6DD63"
  blush: "#E8C9B6"
  sage: "#B7C7A8"
  lilac: "#C9BEDC"
  card-fill: "rgba(255,255,255,0.55)"
  rule-soft: "rgba(42,36,27,0.18)"
  rule-medium: "rgba(42,36,27,0.35)"

color-aliases:
  background: paper
  text-primary: ink
  text-secondary: ink-soft

typography:
  display:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 232px
    fontWeight: 500
    lineHeight: 0.92
    letterSpacing: -0.02em
  title:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 188px
    fontWeight: 500
    lineHeight: 0.95
    letterSpacing: -0.015em
  closer:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 168px
    fontWeight: 500
    lineHeight: 0.95
    letterSpacing: -0.015em
  numeral-hero:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 320px
    fontWeight: 500
    lineHeight: 0.9
    letterSpacing: -0.02em
  numeral-lg:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 200px
    fontWeight: 500
    lineHeight: 0.9
    letterSpacing: -0.02em
  panel-headline:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 124px
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: -0.01em
  section-headline:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 96px
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: -0.01em
  page-headline:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 88px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: -0.01em
  quote-text:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 88px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -0.01em
  quote-mark:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 220px
    fontWeight: 500
    lineHeight: 0.7
    fontStyle: italic
  card-headline:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 72px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: -0.01em
  drop-cap:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 132px
    fontWeight: 500
    lineHeight: 0.85
  opener:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 56px
    fontWeight: 500
    fontStyle: italic
    lineHeight: 1.1
  numeral-step:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 92px
    fontWeight: 500
    fontStyle: italic
    lineHeight: 0.9
  numeral-card:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 64px
    fontWeight: 500
    fontStyle: italic
    lineHeight: 1
  subhead-lg:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 56px
    fontWeight: 500
    fontStyle: italic
    lineHeight: 1.1
  subhead-md:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.05
  subhead-sm:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 38px
    fontWeight: 500
    lineHeight: 1.05
  kicker:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 38px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.2
  marker:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 32px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.3
  card-sub:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.1
  eyebrow:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 28px
    fontWeight: 400
    letterSpacing: -0.005em
  page-marker:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 26px
    fontWeight: 400
    fontStyle: italic
  footer:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 26px
    fontWeight: 400
    fontStyle: italic
  body:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.5
  body-md:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.5
  attr:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
  swatch-label:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 11px
    fontWeight: 400
    letterSpacing: 0.06em
    textTransform: uppercase

spacing:
  pad-outer: 80px
  pad-top: 60px
  pad-bottom: 50px
  card-pad-lg: "64px 48px"
  card-pad-md: "48px 52px"
  card-pad-sm: "28px 30px"
  gap-cards: 28px
  gap-cards-lg: 36px
  gap-stack: 36px

canvas:
  width: 1920px
  height: 1080px

components:
  card-soft:
    background: "{colors.card-fill}"
    borderRadius: "24px to 36px"
    padding: "{spacing.card-pad-sm} to {spacing.card-pad-lg}"
    description: "Translucent white card floating on the cream field. The system's default container — used for stats, columns, panels, content blocks."
  card-color:
    background: "any of pink, lemon, blush, sage, lilac"
    borderRadius: "22px to 36px"
    padding: "{spacing.card-pad-sm}"
    description: "Saturated pastel card containing numerals, step content, or featured items. Text stays ink/ink-soft on every accent fill — never inverted."
  pill:
    borderRadius: "999px"
    padding: "4px 14px"
    fontWeight: 500
    description: "Status pill in a pastel fill (lemon=yes, blush=partial, pink=no) or translucent white with a soft border for notes."
  swatch-dot:
    width: 56px
    height: 56px
    borderRadius: "50%"
    description: "Circular accent disc shown in a row at the top of cover slides — the visual signature of the system's color palette."
  swatch-tile:
    aspectRatio: "1/1.2"
    borderRadius: "16px"
    description: "Rounded rectangle paint chip used in palette displays and design-system layouts."
  rule-dashed:
    borderColor: "{colors.rule-soft}"
    borderStyle: "dashed"
    borderWidth: "1px"
    description: "1px dashed warm-ink hairline used inside matrix tables, panel dividers, and any subdivision that wants to read softer than a solid rule."
  rule-solid:
    borderColor: "{colors.rule-medium}"
    borderStyle: "solid"
    borderWidth: "1.5px"
    description: "Slightly heavier hairline for major dividers inside cards (head-row underlines, column rules)."
  drop-cap:
    typography: "{typography.drop-cap}"
    float: "left"
    description: "First letter of an opener paragraph floats left at ~132px, line-height 0.85, with 8px 14px 0 0 padding. The visible signature of editorial reads."
  legend-bar:
    width: 28px
    height: 12px
    borderRadius: "6px"
    description: "Rounded color bar used as a chart legend swatch."
  marker-rule:
    width: "auto"
    borderTop: "1px dashed {colors.rule-soft}"
    description: "Dashed top-rule used to mark source attributions or sign-offs beneath content."
  action-bar:
    background: "{colors.lemon}"
    borderRadius: "24px"
    padding: "24px 36px"
    description: "Lemon-yellow action band running near the top of a slide, containing a tag separator and a serif headline — used for important CTAs or callouts."
  chrome-eyebrow:
    position: "absolute top-left at 60px / 80px"
    typography: "{typography.eyebrow}"
    color: "{colors.ink}"
    description: "Section name in plain sans, sits at the top-left corner of standard slides."
  chrome-pagedot:
    position: "absolute top-right at 60px / 80px"
    typography: "{typography.page-marker}"
    color: "{colors.ink-soft}"
    description: "Roman or arabic page numeral in italic serif at the top-right corner."
  chrome-footer:
    position: "absolute bottom at 50px"
    typography: "{typography.footer}"
    color: "{colors.ink-soft}"
    description: "Two-column italic serif footer running across the bottom — date left, publication name right."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/soft-editorial/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Soft Editorial 是一套**暖杂志跨页**演示系统，视觉线索取自小型出版社的文学季刊与设计研究笔记本。前提是单一字面（Cormorant Garamond）几乎包办所有表达，只在衬线会累的地方由一款克制的人文无衬线（Work Sans）支撑。奶油纸场地是常量，每页都坐在 `{colors.paper}`（#F2EEDF）上，一种暖的旧奶油，读作实体纸而非屏幕白。场地上，圆角卡片以两种语域漂浮：默认内容用半透明白柔和感，强调瞬间用饱和柔和糖果色。

排印系统是**单字族混风格**。标题是 Cormorant Garamond medium（字重 500），但正体标题常常句中带一个 `<em>`，切到字重 400 的斜体，斜体短语是同字族更轻的字重，给系统标志性的"轻柔强调"调子。斜体也跑在小号装饰文字上（眉题、标记、页码、落款、开场段、步骤数字）。Work Sans 只在正文段、eyebrow，以及一小撮衬线个性太重的元标签里登场。

色彩理念是**奶油加五种柔和色**。这些柔和色，雾粉（`{colors.pink}`）、查特酒柠檬（`{colors.lemon}`）、柔桃腮红（`{colors.blush}`）、鼠尾草绿（`{colors.sage}`）、丁香紫（`{colors.lilac}`），是可互换的卡片填充。没有哪个带固定语义角色（柠檬不表"警告"、粉不表"错误"）。它们是颜料，文稿轮换着用求变化，常常一页上同时露出三四种。每个柔和表面上的文字都保持 `{colors.ink}`（暖近黑，#2A241B）。系统从不在强调表面上反转文字色。

纵深来自**柔和圆角卡片**，大 border-radius（默认卡 24–36px，胶囊可到 999px）配半透明白填充，微微坐在奶油场地之上。没有投影，纵深由半透明与圆润形态暗示。卡内细线以低不透明度暖墨画成虚线，强化"笔记本"感。

**密度取向：卡内中高，卡间宽裕。** 卡片本身能装可观内容，多栏矩阵、密集步骤网格、长段引文。但页面画布在它们周围留舒服的空气：80px 外内边距、卡间 28–36px 间隙、大量奶油场地透出来。在这套系统里读着别扭的页，要么是（a）卡片挤在一起没有呼吸场地，要么是（b）页稀疏到纸场地读作空、而非刻意的留白。目标是"一张排得宽裕的杂志页，卡片成组、呼吸、引导视线"。

**关键特征：**
- 每页单一暖奶油表面（`{colors.paper}`），柔和色只作卡片填充、绝不作页面背景（例外是满幅收尾页，用 `{colors.pink}` 填满）。
- Cormorant Garamond 承载每个展示、标题、眉题、装饰瞬间，Work Sans 预留给正文与 eyebrow。
- 标题内混排正体 + 斜体是系统的排印信号，斜体短语从标题字重 500 降到 400。
- 饱和柔和色（`{colors.pink}`、`{colors.lemon}`、`{colors.blush}`、`{colors.sage}`、`{colors.lilac}`）是可互换卡片填充，无固定语义。
- 圆角卡片（24–36px 半径）是默认容器，胶囊全圆（999px），半透明白（`{colors.card-fill}`）是默认卡片填充。
- 无投影。纵深来自叠在奶油场地上的半透明与卡片的圆润外壳。
- 页面外壳是斜体衬线（页码与页脚）加朴素无衬线（eyebrow），绝不等宽、绝不全大写。
- 首字下沉出现在长篇开场段开头，约 132px 的 Cormorant Garamond medium。

## 颜色

### 调色板

- **纸**（`{colors.paper}` — #F2EEDF）：奶油页。默认幻灯片背景，全稿的常量。暖而旧，绝不明亮。
- **纸 Alt**（`{colors.paper-2}` — #ECE6D2）：略冷的奶油，预留给相邻表面区分。省着用，许多文稿根本用不到。
- **墨**（`{colors.ink}` — #2A241B）：带棕偏的暖近黑。每个表面上的主文字色，绝非纯黑。
- **柔墨**（`{colors.ink-soft}` — #5C5345）：柔化的暖灰棕。次级文字，图注、导语、描述、页码标记、落款。
- **粉**（`{colors.pink}` — #E1A4C2）：雾玫瑰柔和色。最常用的强调填充，出现在封面色样、步骤卡、满幅收尾页、状态胶囊（矩阵里读作"否"）。
- **柠檬**（`{colors.lemon}` — #D6DD63）：查特酒黄绿。最亮的强调，用于英雄数字卡、动作条、"是"胶囊。
- **腮红**（`{colors.blush}` — #E8C9B6）：柔桃。柔和色里最中性的，用于步骤卡、"部分"胶囊，以及任何需要暖中性的槽位。
- **鼠尾草**（`{colors.sage}` — #B7C7A8）：柔化绿。加入求变化的"额外"强调，流程图、设计系统网格、次级步骤卡。
- **丁香**（`{colors.lilac}` — #C9BEDC）：柔紫灰。鼠尾草的冷对位，多出现在五种柔和色全部轮换的五步流程里。
- **卡片填充**（`{colors.card-fill}` — rgba(255,255,255,0.55)）：半透明白。默认卡片背景，作为"抬起"的表面坐在奶油场地上，又不承诺一种饱和色。
- **柔线**（`{colors.rule-soft}` — rgba(42,36,27,0.18)）：低不透明度暖墨，用于卡内虚线细线。
- **中线**（`{colors.rule-medium}` — rgba(42,36,27,0.35)）：略重的细线，用于卡内主分隔。

### 默认值

- **默认页面背景**：`{colors.paper}`，每张标准页。
- **默认主文字色**：`{colors.ink}`，每个表面上，包括所有柔和卡。文字在柔和填充上绝不反转成白。
- **默认次级文字色**：`{colors.ink-soft}`，用于描述、导语段、图注、页码标记、落款。
- **默认卡片填充**：`{colors.card-fill}`，半透明白。内容容器不需要饱和色时一律取它。
- **默认强调卡片填充（需要时）**：最暖瞬间 `{colors.pink}`、最亮 `{colors.lemon}`、中性暖 `{colors.blush}`、冷变化 `{colors.sage}`、五连网格第五槽 `{colors.lilac}`。
- **默认标题色**：`{colors.ink}`。
- **默认 eyebrow 色**：`{colors.ink}`（eyebrow 是左上角外壳标签）。
- **默认页脚色**：`{colors.ink-soft}`。

柔和色不带语义。矩阵布局里的惯例是柠檬 = 肯定 / 部分 / 是，腮红 = 部分，粉 = 否定 / 否。矩阵之外，任何柔和色可填任何卡片而不传达状态。

## 排印

### 字族

Soft Editorial 以精心分开的角色跑**两款字族**：

- **Cormorant Garamond**（`{typography.display.fontFamily}`）：精致的老式衬线，带极富表现力的斜体轴。承载每个尺度上的每个标题（display、title、closer、page-headline、card-headline、所有副标题）、每个数字、每条引文、每个眉题、每个装饰标记、每个页码、每条页脚、每个首字下沉。这款字面的斜体细腻而私人，系统用得大方，斜体承载眉题、标记、页码、页脚、步骤数字、落款，以及标题里的任何 `<em>`。
- **Work Sans**（`{typography.body.fontFamily}`）：人文怪诞体。预留给正文段、eyebrow、卡片子标签、归属，以及 Work Sans 专属标签（色板展示里的小号全大写色样标签）。Work Sans 从不承载标题。

系统的排印信号是**同一标题内混字重**：字重 500 的衬线标题里，一个 `<em>` 降到字重 400（斜体）。字重差是轻柔的，读成一种软化，而非粗重强调。这与杂志"斜体表加粗"的惯例相反，这里斜体是更轻、更私密的调子。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.numeral-hero}` | 320px | Cormorant Garamond | 500 | 跨两栏统计卡里的精选英雄数字 |
| `{typography.display}` | 232px | Cormorant Garamond | 500 | 封面尺度展示标题 |
| `{typography.numeral-lg}` | 200px | Cormorant Garamond | 500 | 独立大统计数字 |
| `{typography.title}` | 188px | Cormorant Garamond | 500 | 近封面尺度的分节或章节标题 |
| `{typography.closer}` | 168px | Cormorant Garamond | 500 | 满幅彩色页上的收尾或"瞬间"标题 |
| `{typography.panel-headline}` | 124px | Cormorant Garamond | 500 | 填满双栏布局一栏的标题 |
| `{typography.section-headline}` | 96px | Cormorant Garamond | 500 | 图表、比较、分析分节标题 |
| `{typography.numeral-step}` | 92px | Cormorant Garamond 斜体 | 500 | 步骤卡上的斜体序数数字（i.、ii.、iii.） |
| `{typography.page-headline}` | 88px | Cormorant Garamond | 500 | 流程图或通用页面标题 |
| `{typography.quote-text}` | 88px | Cormorant Garamond | 500 | 引文正文 |
| `{typography.card-headline}` | 72px | Cormorant Garamond | 500 | 填满方形强调卡头部的标题 |
| `{typography.numeral-card}` | 64px | Cormorant Garamond 斜体 | 500 | 较小条目卡上的斜体序数数字 |
| `{typography.opener}` | 56px | Cormorant Garamond 斜体 | 500 | 序言 / 长篇阅读的斜体开场段 |
| `{typography.subhead-lg}` | 56px | Cormorant Garamond 斜体 | 500 | 双栏开场用的斜体大副标题 |
| `{typography.subhead-md}` | 44px | Cormorant Garamond | 500 | 卡片或栏标题 |
| `{typography.subhead-sm}` | 38px | Cormorant Garamond | 500 | 面板内副标题，列表里的条目标题 |
| `{typography.kicker}` | 38px | Cormorant Garamond 斜体 | 400 | 封面标题上方的斜体眉题 |
| `{typography.card-sub}` | 32px | Work Sans | 500 | 衬线卡头下的子标签（唯一的无衬线副标题） |
| `{typography.marker}` | 32px | Cormorant Garamond 斜体 | 400 | 斜体标记文字（落款、版次标签、"vol. iii"） |
| `{typography.eyebrow}` | 28px | Work Sans | 400 | 标准页左上角的朴素无衬线分节名 |
| `{typography.page-marker}` | 26px | Cormorant Garamond 斜体 | 400 | 右上角的罗马或阿拉伯页码 |
| `{typography.footer}` | 26px | Cormorant Garamond 斜体 | 400 | 斜体衬线页脚行（日期、刊物名） |
| `{typography.body}` | 26px | Work Sans | 400 | 默认段落正文 |
| `{typography.body-md}` | 24px | Work Sans | 400 | 卡片正文、列表项正文、卡内密集段落 |
| `{typography.attr}` | 24px | Work Sans | 500 | 引文署名 |
| `{typography.drop-cap}` | 132px | Cormorant Garamond | 500 | 长篇开场段开头的首字下沉 |
| `{typography.swatch-label}` | 11px | Work Sans 全大写 | 400 | 色样块内的小号全大写标签（色板展示） |

### 默认值

- **主分节标题默认尺寸**：标准页 `{typography.section-headline}`（96px），标题填满双栏布局一栏时 `{typography.panel-headline}`（124px）。
- **封面或章节标题默认尺寸**：`{typography.title}`（188px）到 `{typography.display}`（232px）。
- **段落正文默认尺寸**：开放页 `{typography.body}`（26px），卡内或更密栏里 `{typography.body-md}`（24px）。
- **眉题或标记默认尺寸**：封面眉题 `{typography.kicker}`（38px），较小装饰注记 `{typography.marker}`（32px）。
- **精选统计数字默认尺寸**：`{typography.numeral-lg}`（200px），仅当一个统计主导布局时取 `{typography.numeral-hero}`（320px）。
- **步骤或条目数字默认尺寸**：整张步骤卡 `{typography.numeral-step}`（92px），较小条目 `{typography.numeral-card}`（64px）。
- **默认标题字重**：500（medium）。里面的斜体 `<em>` 降到 400。
- **默认标题色**：`{colors.ink}`。

页面主瞬间在尺寸间拿不准时，取 `{typography.section-headline}`（96px），它是编辑阅读的主力尺寸。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每个带强调短语的标题都把 `<em>` 渲染成字重 400 的斜体 Cormorant Garamond**（周围标题跑字重 500）。斜体字重下降是系统的主排印信号。
- **所有页面外壳（eyebrow、page-marker、footer）都以固定偏移绝对定位**（eyebrow 左上 60/80px，pagedot 右上 60/80px，页脚左右 80px / 下 50px）。标准页上外壳位置不可商量。
- **Eyebrow 是 28px 朴素 Work Sans**，不斜体、不全大写。它们是唯一的无衬线外壳元素。
- **页码与页脚是 `{colors.ink-soft}` 的 26px 斜体衬线。** 绝不是无衬线、绝不全大写、绝不粗。
- **步骤数字是斜体衬线小写罗马数字（i.、ii.、iii.、iv.、v.）**，绝不用阿拉伯数字、绝不全大写。罗马数字属于编辑语域。
- **开场段里的首字下沉是字重 500、约 132px 的 Cormorant Garamond，行高 0.85、内边距 `8px 14px 0 0`。** 不符这精确规格的首字下沉读作另一套系统。
- **卡片始终带 22–36px 区间的 border-radius**（胶囊为 999px）。本系统不存在方角卡片。

### 排印原则

衬线 / 无衬线分离是结构性的：Cormorant Garamond 承载个性（每个标题、每个数字、每个装饰），Work Sans 承载实质（每段正文、每个 eyebrow、每个 Work Sans 专属标签）。跨过这些轨道会破掉编辑的平静。

斜体用得大方，不吝啬。斜体衬线出现在眉题、标记、页码、页脚、步骤数字、开场段、标题 `<em>` 短语，以及任何小装饰瞬间。无衬线绝不斜体，Work Sans 应始终直立。

行高在展示尺度上紧（0.9–0.98），正文与卡片正文放开到 1.4–1.55。字距在最大尺寸上略负（–0.01 到 –0.02em），正文为零或近零。11px Work Sans 色样标签是系统里唯一的全大写元素，它带宽裕的 0.06em 字距，让 11px 尺寸可读。

## 布局

### 画布系统

Soft Editorial 经 `<deck-stage>` 元素以**固定 1920×1080 画布**为目标。布局建立在距页边的绝对定位上，每个元素都经 `position: absolute` 以相对页面的 `top`/`left`/`right`/`bottom` 偏移定位。系统不用视口相对单位，靠 deck-stage 的缩放处理视口差异。

### 内边距与间隙比例

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-outer}` | 80px | 内容块标准左右内缩 |
| `{spacing.pad-top}` | 60px | eyebrow / pagedot 外壳顶部内缩 |
| `{spacing.pad-bottom}` | 50px | 页脚外壳底部内缩 |
| `{spacing.card-pad-lg}` | 64px 48px | 宽绰卡片内边距（洞见、收尾） |
| `{spacing.card-pad-md}` | 48px 52px | 中等卡片内边距（下一步面板） |
| `{spacing.card-pad-sm}` | 28px 30px | 紧凑卡片内边距（栏、设计系统块） |
| `{spacing.gap-cards}` | 28px | 一行或网格里卡片间标准间隙 |
| `{spacing.gap-cards-lg}` | 36px | 主面板间较大间隙 |
| `{spacing.gap-stack}` | 36px | 叠放文字元素间纵向间隙 |

### 外壳画框

每张标准页都在固定位置带三个外壳元素：

- **Eyebrow**：左上角分节名（距顶 60px、距左 80px），`{colors.ink}` 的 28px Work Sans。
- **Pagedot**：右上角页码（距顶 60px、距右 80px），`{colors.ink-soft}` 的 26px 斜体 Cormorant Garamond。
- **页脚**：底部双栏页脚（距底 50px、每侧 80px），`{colors.ink-soft}` 的 26px 斜体 Cormorant Garamond（左日期、右刊物名）。

封面页把 pagedot 换成右上角一排三个圆形柔和色样（文稿配色的视觉招牌）。满幅强调页（收尾）把外壳在彩色场地上换成深墨，位置保持不变。

## 纵深与层级

Soft Editorial 用**零投影**。纵深完全来自半透明与圆润形态：

- **半透明白卡片**：`{colors.card-fill}`（rgba 255,255,255,0.55），坐在奶油场地上。半透明让暖纸透出来，让卡片不用任何阴影就感到"抬起"。
- **饱和柔和卡**：粉、柠檬、腮红、鼠尾草、丁香填充，以全不透明度坐在奶油场地上。卡片与场地的视觉差别是颜色，不是抬升。
- **圆角**：每张卡片带宽裕 border-radius（22–36px），柔化形态，读作"实体卡片"而非"屏幕矩形"。

没有第二层抬升。卡片不叠卡片。布局需要视觉层级时，用尺寸与颜色，不用 z 层叠。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 999px（胶囊） | 状态胶囊（是 / 部分 / 否 / 注） |
| 36px | 大洞见卡、收尾卡 |
| 32px | 方法步骤卡 |
| 28px | 条目卡、流程节点、图表框 |
| 24px | 默认面板卡、咨询栏、设计系统块、动作条 |
| 22px | 设计系统网格里较大的系统块 |
| 18px | 装饰时间轴条 |
| 16px | 色板色样块 |
| 14px | 设计系统网格里最小的装饰小片 |
| 6px | 图表图例色样（一根扁平圆角条） |
| 50%（圆） | 封面色样圆点 |

系统里**没有方角**。每个容器至少 14px 圆角，卡片 22–36px 圆角，胶囊全圆。

### 边框粗细

- **标准卡片上无实边框**。卡片的背景与圆润形态提供定义。
- **1px 虚线** `{colors.rule-soft}`（rgba 42,36,27,0.18）：表格单元、矩阵分隔、来源行标记、系统块分隔的内部细线。
- **1.5px 实线** `{colors.rule-medium}`（rgba 42,36,27,0.35）：矩阵表头行下划线、栏头线等较重分隔。
- **1px 实线** 类似低不透明度墨：用于图表绘图区边缘与一小撮"注"胶囊。

### 装饰元素类型

**柔和卡**：默认内容容器。半透明白卡，24–36px border-radius，28–64px 内部内边距。作为抬起的区域坐在奶油场地上。

**彩色卡**：饱和柔和卡（粉、柠檬、腮红、鼠尾草、丁香），22–36px border-radius。用于统计、步骤卡、洞见卡，以及任何想要颜色的瞬间。里面文字保持墨 / 柔墨，绝不反转。

**状态胶囊**：999px 全圆半径胶囊，混装衬线 / 无衬线内容。柔和填充（柠檬、腮红、粉）表肯定 / 部分 / 否定状态，"注"用半透明白配 1px 墨边框。

**动作条**：全宽柠檬填充圆角卡（24px 半径）横贯页顶，内含一个标签分隔结构与一条衬线标题。用于标注、CTA、或吸睛的元数据瞬间。

**封面色样排**：一排 3–5 个 56px 圆形碟，取文稿强调调色板，定位在封面页右上。系统色彩理念的视觉招牌。

**首字下沉**：132px Cormorant Garamond medium 首字母，左浮在开场段开头，内边距 8px 14px 0 0。系统里最编辑化的排印瞬间。

**斜体步骤数字**：64–92px 区间的斜体 Cormorant Garamond 罗马数字（i.、ii.、iii.），坐在步骤卡顶端，上方衬线标题、下方无衬线正文。步骤上罗马数字不可商量。

**引号标记**：单个 220px 的 `{colors.blush}` 斜体 Cormorant Garamond `"`，坐在居中引文上方。引号标记的颜色自成信号，柔桃而非墨。

**图例条**：28px × 12px 圆端（6px 半径）水平条，取图表强调色，配一条标签。

**来源行**：栏或面板底部一条顶边虚线的斜体衬线行，标来源归属或落款。

## 该做与不该做

### 该做

- 每个标题都用字重 500 的 Cormorant Garamond，里面的斜体 `<em>` 短语降到字重 400。字重下降是系统的声部。
- 每张标准页都把背景设成 `{colors.paper}`，暖奶油场地是常量。
- 卡片默认用 24–36px border-radius 的半透明白（`{colors.card-fill}`）。卡片需要颜色或状态时才取柔和填充，不作默认。
- 每个表面上的文字都保持 `{colors.ink}`，包括所有柔和卡。系统从不在柔和色上反转成白。
- 眉题、标记、页码、页脚、步骤数字、落款，以及任何小装饰瞬间都用斜体衬线（Cormorant Garamond 斜体）。
- 长篇阅读的开场段套首字下沉，132px Cormorant Garamond medium、行高 0.85、内边距 8px 14px 0 0。
- 步骤序数用罗马数字（小写斜体：i.、ii.、iii.）。阿拉伯步骤数字会破掉编辑语域。
- 每个页码都渲染成 `{colors.ink-soft}` 的 26px 斜体 Cormorant Garamond，绝对定位在右上。
- Work Sans 只用于正文、eyebrow、归属，以及小号全大写色样标签。Work Sans 从不承载标题。
- 页面留 80px 外内缩、卡间留 28–36px 间隙。卡片周围奶油场地的呼吸是设计的一部分。

### 不该做

- 不要用柔和色填满页面背景，柔和色是卡片填充（一个例外：满幅收尾页可为单一"瞬间"取满幅粉场地）。默认页保持奶油。
- 不要在柔和卡上把文字反转成白。文字始终读作墨压色。
- 不要给任何卡片或容器用方角。可接受的最小半径是 14px，卡片活在 22–36px。
- 不要加投影。系统纵深来自半透明与形态，不来自抬升。
- 不要用第三款字面。Cormorant Garamond 与 Work Sans 是仅有的字族。加展示字体或等宽会破掉编辑语域。
- 不要在正文里用粗体。正文要强调就切斜体衬线，或罕见地在 Work Sans 里用字重 500 的强标签。
- 不要把眉题、标记、页脚渲染成正体衬线。装饰性小文字始终是斜体。
- 不要在 11px 色样标签之外用全大写。系统通篇句式大写。
- 不要用等宽。本系统没有等宽，每个标签都是无衬线或斜体衬线。
- 不要让卡片从边到边挤满。28–36px 间隙与卡片周围的奶油场地是承重的。

## 响应式行为

Soft Editorial 是**固定 1920×1080** 系统，渲染在 `<deck-stage>` web component 内。deck-stage 处理缩放：页面内容按精确 1920×1080 像素尺寸排布，组件把整个舞台缩放到适配视口（留黑边或按 stage 配置贴合）。页内所有 `top`/`left`/`right`/`bottom`/`width`/`height` 值都以像素计，假定固定 1920×1080 画布。

### 缩放行为

由于 deck-stage 等比缩放，所有元素在任何输出视口下都保持相对位置与尺寸。232px 展示标题在 deck-stage 内部画布上仍是 232px，stage 把整块画布缩放以适配浏览器视口。

### 放映行为

导航由 `deck-stage.js` 脚本处理（外部依赖，未内嵌）。每页带一个 `data-label` 属性在放映 UI 里标识它。翻页经 deck-stage 自身的控件完成。

### 打印行为

没有内嵌打印样式表。静态导出取决于 deck-stage 组件的打印 / 导出行为，生成 PDF 时，deck-stage 应把每页按 1920×1080 画布尺寸渲染为单页。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字面（默认） | 中文字面 | 字重 | 说明 |
|---|---|---|---|---|
| 展示 / 标题 | Cormorant Garamond 500 | 霞鹜文楷 LXGW WenKai（LXGW WenKai TC） | 400 | LXGW WenKai 是带手写感的楷体，映照 Cormorant 的文学语域。单一 regular 字重贴合 Cormorant 轻柔的 medium。 |
| 斜体强调（`<em>`） | Cormorant Garamond 斜体 400 | 霞鹜文楷 LXGW WenKai | 400 | LXGW WenKai 没有真斜体，强调改为降到 `{colors.ink-soft}` 或一道淡下划线。不要合成斜体。 |
| 正文 | Work Sans 400 | 思源宋体 / Noto Serif SC | 400 | 系统正文在 CJK 里从无衬线切到衬线以保住文学语域，Work Sans 挨着楷体标题会丢掉编辑平静。 |
| 正文，备选无衬线（可选） | Work Sans 400 | Noto Sans SC | 400 | 仅在文稿数据极密时用，默认取 Noto Serif SC。 |
| 眉题 / 标记 / 页码 | Cormorant Garamond 斜体 400 | 霞鹜文楷 LXGW WenKai 400 | 400 | 斜体装饰变成直立楷体，靠 `{colors.ink-soft}` 换色而非斜体取得同样的"柔和装饰"感。 |

### 混排策略

本模板用**策略 C（文学）**：保留拉丁字面给英文字形，只在汉字出现时经堆叠 `font-family` 让 CJK 回退进来。Cormorant Garamond 属于 Soft Editorial 的品牌身份，把每个标题都换成楷体会剥掉系统的老式衬线个性。让拉丁留在 Cormorant、中文落进 LXGW WenKai，两种语域都保住。

```css
font-family: 'Cormorant Garamond', 'LXGW WenKai TC', 'Noto Serif SC', serif;  /* headlines */
font-family: 'Work Sans', 'Noto Serif SC', sans-serif;                          /* body */
```

**警告，展示尺寸下的基线错位。** Cormorant Garamond 的 x-height 明显低于 LXGW WenKai 的光学中心。96px+ 标题里，像 `Soft Editorial 软编辑` 这样的短语会显出汉字略浮在拉丁基线之上。缓解办法：
- 给中文段加 `font-feature-settings: "palt"` 收紧度量。
- 把 CJK 包进 `<span lang="zh">`，在展示 token（display、title、closer、numeral-hero、panel-headline）上加一点 `vertical-align: -0.04em` 调整。
- 纯 CJK 标题（无拉丁）时问题消失，错位只在混排行里浮现。

### 加载

加到 `<head>`（Google Fonts 托管 LXGW WenKai TC 与 Noto Serif SC）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Work+Sans:wght@400;500&family=LXGW+WenKai+TC&family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

LXGW WenKai TC 是 Google Fonts 上的繁体中文切分，含完整 CJK 统一汉字区，能干净地渲染简体中文。Noto Serif SC 以恰当的 hinting 承载简体中文正文。

### 通用 CJK 调整

施于任何渲染中文内容的元素（典型用 `:lang(zh)` 或 `<span lang="zh">` 限定范围）：

- **行高**：正文 1.75–1.85（Soft Editorial 的 1.5 无衬线默认需要给 CJK 笔画更多空气），展示 1.15–1.25（比拉丁 0.92–1 紧，因为 CJK 字形已含内在间距）。
- **字距**：CJK 设 0。系统在展示拉丁上的负字距（-0.01 到 -0.02em）对中文是错的，CJK 字形本就预置间距，负字距会造成重叠。
- **文字变换**：CJK 不用 uppercase。中文没有大小写，CSS `text-transform: uppercase` 对汉字本就无效，但要确保没有父级规则尝试它。
- **全角标点**：用 `，。：；！？`（全角）而非 `,.:;!?`（半角）。全角形式自带周围留白并贴合 CJK em 框。
- **展示标题不加句号**：中文标题去掉末尾 `。`，标题的视觉收束已足够。（本系统拉丁标题本就不带句号，规则延伸到 CJK。）
- **盘古之白（Pangu spacing）**：在 CJK 与相邻拉丁 / 数字间插入一个窄空格。写 `使用 Claude` 而非 `使用Claude`，`2024 年` 而非 `2024年`。这是优质中文排印的编辑惯例，贴合 Soft Editorial 的文学讲究。
- **一句一款字体**：不要在同一行里混 LXGW WenKai 与 Noto Serif SC。整段用其中一款，句中切换会造成度量顿挫。

### 本系统的美学提示

LXGW WenKai 与 Soft Editorial 的语域格外契合。楷体轻微的手写暖意接住 Cormorant Garamond 老式斜体收束的地方，两款字面在奶油纸场地上都读作私人、有思量、略亲密。在柔和卡（粉、柠檬、腮红、鼠尾草、丁香）上，标题尺度的 LXGW WenKai 读作一个书法瞬间，这强化而非削弱编辑的平静。首字下沉处理（132px Cormorant Garamond medium）迁移不到 CJK，楷体首字下沉看着像被切断而非装饰，中文开场段应彻底去掉首字下沉，靠段落上方的斜体眉题作"文章开场"线索。

衬线正文切换（Work Sans → Noto Serif SC）是最具分量的改动。Work Sans 的人文怪诞体在拉丁里与 Cormorant 相配，但无衬线正文挨着楷体标题，在中文里读成廉价教科书。Noto Serif SC 的宋体笔画与奶油场地、文学标题字面都共鸣，把小型出版社文学季刊的气氛跨语言保住。若想让正文有一点语域偏移，可把 eyebrow（28px）留在 Noto Sans SC，镜像拉丁的无衬线对衬线区分。

### 已知 CJK 缺口

- LXGW WenKai 只有单一字重（regular）。系统招牌的标题内"字重下降"（Cormorant 500 → 斜体 400）在 CJK 里无法复现。替代办法是强调时换色到 `{colors.ink-soft}`，或接受中文标题读作一致字重。
- LXGW WenKai TC 的繁体切分字形可能把少量字渲染成繁体形式（如 設 而非 设）。纯简体中文文稿宜以 `font-family: 'Noto Serif SC'` 作主 CJK 字面，把 LXGW WenKai 留给强调瞬间（封面标题、章节标题）。
- 斜体装饰瞬间（眉题、页码、页脚、落款）在 CJK 里丢掉斜体，因为没有 CJK 字面带真斜体。补偿办法是用 `{colors.ink-soft}` 与略小尺寸保住"装饰耳语"语域。
- 展示尺寸下的基线错位（见混排策略）在封面带混排标题时需要逐稿调校。

## 迭代指南

1. 任何新标题都用字重 500 的 Cormorant Garamond，斜体 `<em>` 短语降到字重 400。字重下降是编辑信号。
2. 任何新卡片都默认 24–36px border-radius 的半透明白（`{colors.card-fill}`）。柔和填充给需要颜色的瞬间，不是每张卡都用。
3. 任何新步骤序数都是 64–92px 的 Cormorant Garamond 斜体小写罗马数字（i.、ii.、iii.）。
4. 任何新眉题、标记、页码、页脚、落款都是 `{colors.ink-soft}` 或 `{colors.ink}` 的 26–38px 斜体 Cormorant Garamond。
5. 任何新引入的柔和色（第六色）都会破掉系统。五柔和色调色板（粉、柠檬、腮红、鼠尾草、丁香）是封闭的。
6. 任何新胶囊都用 999px border-radius 配柔和填充或半透明白。胶囊是副标题级强调单元，不是外壳。
7. 封面色样排（右上三个圆形碟）是系统身份标记。封面页上保住它。
8. 页面外壳（eyebrow、pagedot、页脚）在每张标准页上坐在固定绝对位置。别让位置漂移。
9. 长篇段落阅读应以首字下沉（132px Cormorant Garamond medium）开场，这是系统最鲜明的编辑瞬间。
10. 卡片周围与之间的奶油场地是承重的。布局需要更密时，增加卡片内容，而非缩小场地。

## 已知缺口

- 系统依赖外部 `deck-stage.js` 脚本做页面缩放与导航。脚本被引用但未内嵌，缺它页会按固有 1920×1080 渲染而无视口缩放。
- Cormorant Garamond 与 Work Sans 都从 Google Fonts 加载。字体加载失败时，衬线回退 Garamond/serif、无衬线回退 Helvetica/sans-serif，缺了 Cormorant 编辑性格会显著退化。
- 满幅收尾页是唯一让柔和色覆盖整块画布的地方。式样是刻意的，但应省着用，每个收尾都满幅粉会稀释"奶油即默认"的身份。
- 五种柔和色（`{colors.pink}`、`{colors.lemon}`、`{colors.blush}`、`{colors.sage}`、`{colors.lilac}`）被列为语义可互换，但源模板在矩阵布局里用柠檬 = 是 / 腮红 = 部分 / 粉 = 否。新文稿可遵循或忽略这一惯例。
- 首字下沉处理依赖 CSS `:first-letter` 渲染，其度量处理有轻微跨浏览器差异。内边距与行高值是为 Cormorant Garamond 调的，字体加载失败时可能需调整。
- 半透明白卡片填充（`rgba(255,255,255,0.55)`）依赖奶油纸透出来。换到别的背景色上卡片读起来会不同，规格假定 `{colors.paper}` 是表面。
