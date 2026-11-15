---
version: alpha
name: Retro Zine
description: "A risograph-zine editorial system on warm khaki paper with a deep forest-green accent and ink-black structure. Display type runs in Bebas Neue (condensed industrial sans, uppercase, generously tracked); body type runs in Space Grotesk at weight 300–500; handwritten emphasis runs in Caveat. A subtle SVG grain overlay sits over every slide, reinforcing the printed-paper feel. The aesthetic borrows from independent press, mid-century activist posters, and DIY zine culture: slightly rotated stamp marks, masking-tape pieces in collage layouts, drop caps, and offset paper-on-paper shadows. The effect is hand-printed editorial — warm but disciplined, confident but tactile."

colors:
  bg: "#C8B99A"
  bg-dark: "#B8A98A"
  green: "#008F4D"
  green-light: "#00A85D"
  black: "#1A1A1A"
  white: "#F4EFE6"

color-aliases:
  line: black

typography:
  display-hero:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(56px, 10vw, 160px)"
    fontWeight: 400
    lineHeight: 0.85
    letterSpacing: 0.04em
    textTransform: uppercase
  display-cover:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(48px, 10vw, 140px)"
    fontWeight: 400
    lineHeight: 0.88
    letterSpacing: 0.04em
    textTransform: uppercase
  display:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(48px, 8vw, 120px)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: 0.04em
    textTransform: uppercase
  headline:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(42px, 6vw, 90px)"
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: 0.03em
    textTransform: uppercase
  headline-md:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(36px, 5vw, 72px)"
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: 0.03em
    textTransform: uppercase
  statement:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(36px, 6vw, 90px)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
    textTransform: uppercase
  title:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(24px, 3vw, 42px)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.04em
    textTransform: uppercase
  number-hero:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(80px, 12vw, 160px)"
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.02em
  number-md:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(44px, 6vw, 80px)"
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.02em
  drop-cap:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(48px, 6vw, 80px)"
    fontWeight: 400
    lineHeight: 0.8
    letterSpacing: 0.02em
  body:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: "clamp(13px, 1.2vw, 16px)"
    fontWeight: 400
    lineHeight: 1.7
  body-md:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: "clamp(14px, 1.3vw, 18px)"
    fontWeight: 400
    lineHeight: 1.6
  label-eyebrow:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "14–18px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.2em
    textTransform: uppercase
  label-spaced:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: "12–14px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25em
    textTransform: uppercase
  caption-feature:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "13–15px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.2em
    textTransform: uppercase
  hand-script:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(22px, 3vw, 36px)"
    fontWeight: 600
    lineHeight: 1.3
  hand-script-sm:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(16px, 2vw, 22px)"
    fontWeight: 400
    lineHeight: 1.3
  hand-script-lg:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(24px, 3vw, 36px)"
    fontWeight: 600
    lineHeight: 1.3

spacing:
  slide-pad: 60px
  slide-pad-wide: "60px 80px"
  card-pad-lg: 48px
  card-pad-md: 32px
  card-pad-sm: 24px
  gap-lg: 60px
  gap-md: 40px
  gap-sm: 24px

canvas:
  width: 100vw
  height: 100vh

components:
  grain-overlay:
    backgroundImage: "SVG fractal-noise filter, base 200×200 tile"
    opacity: 0.07
    zIndex: 9999
    description: "Fixed, full-viewport SVG grain overlay sitting above all content. Imitates the print-grain texture of a risograph or letterpress page. Pointer-events disabled. Required on every slide."
  line-box:
    border: "3px solid {colors.black}"
    description: "Generic outlined card with 3px solid black border on khaki background. The system's default content container."
  line-divider:
    border: "3px solid {colors.black}"
    description: "Strict 3px black rule used as a region divider. May be top, bottom, left, or right of a region; meets adjacent borders without gap."
  line-thin:
    border: "2px solid {colors.black}"
    description: "2px black rule used inside a section for sub-region division (editorial column rule, ed-header bottom rule)."
  line-fine:
    border: "1.5px solid {colors.black}"
    description: "1.5px black rule used inside grid containers for cell separation (sub-cells inside a 3px-bordered grid)."
  stamp:
    transform: "rotate(-8deg) or rotate(6deg)"
    display: inline-block
    description: "Any element may be rotated -8deg (stamp) or 6deg (stamp-alt) to read as a hand-pressed ink stamp or applied label. Reserve for badges, callouts, and decorative overlays."
  stamp-mark:
    background: "{colors.black}"
    color: "{colors.green}"
    fontFamily: "'Bebas Neue', sans-serif"
    padding: "10px 24px"
    border: "2px solid {colors.green}"
    transform: "rotate(-8deg)"
    fontSize: 18px
    letterSpacing: 0.1em
    description: "Approval / status stamp — black background, green text, green 2px border, rotated -8deg. Used as a 'stamp of authenticity' callout."
  ribbon-bar:
    background: "{colors.green}"
    color: "{colors.white}"
    padding: "4–8px 12–20px"
    description: "Solid green color-block that contains light cream text — used as section labels, accent strips, and inline highlight bars."
  inline-highlight:
    background: "{colors.black}"
    color: "{colors.bg}"
    padding: "2px 8px"
    fontWeight: 600
    description: "Black-on-khaki marker highlight applied inline inside body paragraphs to lift a phrase. The print equivalent of a marker pen swipe."
  drop-cap:
    float: left
    fontSize: "clamp(48px, 6vw, 80px)"
    fontFamily: "'Bebas Neue', sans-serif"
    color: "{colors.green}"
    lineHeight: 0.8
    marginRight: 12px
    description: "Oversized green initial cap at the start of an editorial paragraph. Bebas Neue, line-height 0.8, floated left so body text wraps around."
  card-offset:
    background: "{colors.white}"
    border: "3px solid {colors.black}"
    positionBefore:
      offset: "12px down, 12px right"
      background: "{colors.green}"
      zIndex: -1
    description: "Card with a paper-on-paper offset effect — a solid green slab sits 12px behind the card, offset down-and-right. Reads as a colored shadow without using box-shadow."
  collage-piece:
    border: "3px solid {colors.black}"
    padding: 24px
    position: absolute
    transform: "rotate(-5deg to 5deg)"
    description: "Free-positioned collage panel with a 3px black border and small rotation. Backgrounds vary across pieces — white, khaki-dark, green, or black-with-inversion. Used in scatter-on-page compositions."
  tape:
    width: 80px
    height: 24px
    background: "rgba(255,255,255,0.4)"
    border: "1px solid rgba(0,0,0,0.1)"
    transform: "rotate(-40deg to 35deg)"
    description: "Translucent masking-tape rectangle layered at random angles over a collage to suggest physically taped-down pieces. Positioned absolutely; 1px hairline border. Always semi-transparent white."
  divider-stub:
    width: 60–80px
    height: 4px
    background: "{colors.white} or {colors.green}"
    description: "Short solid horizontal rule used as a centered visual breath above/below a statement or closing title. 4px tall."
  rsvp-field:
    borderBottom: "2px solid {colors.black}"
    paddingBottom: 8px
    description: "Form-field row pattern: small Bebas Neue green label, hand-script value drawn over a 2px black underline. Mimics a written form."
  ledger-row:
    borderBottom: "1.5px solid {colors.black} (header) or 1px solid rgba(black, 0.22) (body)"
    padding: "10–18px 0"
    description: "Horizontal data row pattern: date | title | edition | track | nr. Header row has stronger bottom border; body rows have hairline dividers."
  chip:
    padding: "4px 10px"
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "11–12px"
    color: "{colors.white}"
    textTransform: uppercase
    letterSpacing: 0.06em
    description: "Mono-font color chip used inline in tabular ledger rows to tag a row's category. Fill pulls from green / red-stamp / orange / pink / blue as a categorical palette extension."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/retro-zine/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Retro Zine 是一套**孔版印刷杂志编辑系统**，落在暖卡其画布（`{colors.bg}` — #C8B99A）上，以深森林绿（`{colors.green}` — #008F4D）作真正算数的强调，墨黑（`{colors.black}` — #1A1A1A）作结构色。美学借自独立出版文化、世纪中叶行动主义海报与 DIY 杂志排版：压缩的工业展示字面、手写脚本强调、略带旋转的印章、美纹纸胶带拼贴痕、首字下沉，以及把每处表面系在印刷纸语域上的颗粒叠层。

字体栈搭配三款字面，各有分明的情绪角色。**Bebas Neue** 是展示声部，一款压缩的全大写工业无衬线，带宽裕字距（0.02–0.04em），用于每个标题、陈述、统计、数字、标签。它压缩的竖向感是系统的视觉身份，换成别的展示无衬线就丢了杂志声部。**Space Grotesk** 是正文声部，一款干净的人文几何无衬线，字重 300–500 用于段落，以小尺寸（13–18px）使用，保住杂志栏文的密度。**Caveat** 是手写脚本声部，一款随意的圆珠笔草书，用于作者署名、旁注、展示元素上的图注，以及 RSVP 式布局里表单栏的"填写"。三款字面合起来读作"一份小出版社排的编辑跨页"。

色彩理念是**土地 + 森林**：暖卡其纸画布、更深的卡其色调兄弟作分层表面、深森林绿作强调与强调表面、墨黑作结构与正文，以及米白奶油（`{colors.white}` — #F4EFE6）作卡片与反色文字填充。白刻意不纯，是柔和奶油，作为纸中纸坐着，而非一块硬矩形。绿承载系统的情绪声部：它激活一个分节、盖下批准、标出品牌。同一个十六进制（#008F4D）出现在首字下沉、飘带条、行内标签、陈述页背景、进度条里。

纵深来自**纸压纸偏移块**与**轻微旋转**，不靠模糊阴影。招牌处理是 `{components.card-offset}` 带一块实绿色板，经绝对定位的 `::before` 伪元素坐在它背后朝右下 12px。视觉效果是分层纸或凸版套印，而非柔和投影。印章上的旋转（`-8deg` 或 `6deg`）与拼贴件上的旋转（`-5deg` 到 `5deg`）添上手放感。

**密度取向：中高。** 杂志语域依赖视觉丰盛，拼贴构图、多栏编辑布局、正文里的首字下沉、带类别小片的账表、斜盖的飘带头。只有一个居中标题的页读作设计不足，杂志声部期待一个版面塞满编辑动作。对的密度是一个主导文字瞬间，由多个从属组件支撑（装饰印章、eyebrow 标签、分隔短线、手写脚本署名、首字下沉）。把真正的稀疏留给宣言 / 陈述瞬间，那里一条大引文主导一整块实绿场地。

**关键特征：**
- 暖卡其纸画布（`{colors.bg}`）+ 深森林绿强调（`{colors.green}`）+ 墨黑结构（`{colors.black}`）。
- SVG 颗粒叠层（`{components.grain-overlay}`）以 0.07 不透明度盖在每页上，强化印刷纸语域。
- Bebas Neue 全大写加字距用于每个展示瞬间，Space Grotesk 小尺寸作正文，Caveat 作手写脚本强调。
- 3px 实黑结构边框分隔区域，2px 与 1.5px 边框再细分。
- 纸压纸偏移卡片：绿色板经 `::before` 坐在白卡背后 12px。
- 印章与拼贴件带小旋转（-8°、+6°、-5° 到 +5°）。
- 半透明美纹纸胶带片（`{components.tape}`）叠在拼贴构图上。
- 绿色首字下沉、绿色飘带条、绿色行内高亮标出编辑强调。

## 颜色

### 调色板
- **背景**（`{colors.bg}` — #C8B99A）：暖卡其纸画布。每页默认表面。饱和到读作"有历史的纸"而非中性色，又暖到与森林绿强调相谐。
- **深背景**（`{colors.bg-dark}` — #B8A98A）：画布略深的色调兄弟。用于分层表面区域，即分屏中一半需要在视觉上坐在另一半之后时，以及想读作"卡其纸上的纸"的拼贴件。
- **绿**（`{colors.green}` — #008F4D）：深森林绿。系统强调色，英雄数字、首字下沉、飘带条、陈述页背景、进度条、行内高亮、RSVP 标签、卡片背后的偏移板、收尾页分隔短线。最鲜明的非画布色。
- **浅绿**（`{colors.green-light}` — #00A85D）：绿略亮的兄弟。深绿需要抬一档时，可作悬停态或次级绿，基线静态页里很少用。
- **黑**（`{colors.black}` — #1A1A1A）：墨黑。结构色，全部边框、全部正文、全部分隔、全部收尾页背景、全部标签填充（反色时）。比纯黑（#000000）略柔，好作为暖墨落在暖纸上。
- **白 / 奶油**（`{colors.white}` — #F4EFE6）：柔和奶油。用作卡片填充（纸压纸）、黑表面里的文字、陈述页上的分隔短线色。关键是这不是纯白，是纸奶油，哪怕当作"白"表面用也维持暖纸语域。

### 默认值
- **默认表面背景**：`{colors.bg}`，每页都在暖卡其纸上开场。
- **默认标题色**：主分节标题与英雄标题用 `{colors.green}`；双栏或分屏布局里与正文配对的标题用 `{colors.black}`。拿不准时取 `{colors.green}`，绿标题是系统最响的编辑信号。
- **默认正文色**：`{colors.black}`。
- **默认边框色**：`{colors.black}`，每条结构边框都是黑，无例外。
- **强调默认表面（陈述、英雄标注）**：`{colors.green}` 配 `{colors.white}` 文字。
- **`{colors.green}` 表面上默认文字色**：`{colors.white}`（奶油）。
- **`{colors.black}` 表面上默认文字色**：`{colors.bg}`（卡其画布），于是即便反转，文字仍读作"纸上的墨"。黑表面上的绿点缀（收尾页 eyebrow + 手写脚本）把反转提亮。
- **默认 eyebrow / 标签色**：Bebas Neue 标签用 `{colors.green}`，加字距的 Space Grotesk 标签用 `{colors.black}`。
- **默认首字下沉色**：`{colors.green}`。首字下沉是编辑指纹，始终是绿。
- **默认手写脚本色**：卡其 / 奶油表面上 `{colors.black}`，黑表面上（收尾页）`{colors.green}`。
- **默认行内高亮**：黑压卡其（`{components.inline-highlight}`），用来把正文段里的短语提起来，像用笔划过。

绿与黑的点缀不可互换：**绿 = 强调**（这是要你注意的），**黑 = 结构**（这是把页面撑住的）。把两者反过来，用黑做强调、绿做结构，会翻转系统的声部。

## 排印

### 字族
系统搭配三款 Google Fonts：

- **Bebas Neue**（展示）：压缩的全大写工业无衬线。单字重（400），但凭致密的竖笔读起来就粗。以全大写、0.02–0.04em 字距用于每个展示瞬间，标题、陈述、统计、序数、eyebrow 标签。窄而加字距的 Bebas 声部正是让系统一眼是"杂志"的东西。
- **Space Grotesk**（正文）：干净的人文几何无衬线，带细微古怪比例。字重 300–500 用于小尺寸（13–18px）正文段，字重 600 用于加字距的 Space Grotesk 全大写标签。给 Bebas 的表现性密度一个易读的对位。
- **Caveat**（手写脚本）：随意的手写草书。字重 400–700 用于作者署名（"— Our founding principle since day one"）、旁注、展示元素上的装饰图注、RSVP 式表单布局里的填值。在本就排印规整的系统里添暖意与人手声部。

没有第四款字面。斜体不存在（Caveat 是脚本字面，不是斜体）。下划线不存在。强调靠换字面（Space Grotesk 正文 → Caveat 手写脚本写私人便签，Bebas Neue 展示作标注）或换色（`{colors.black}` → `{colors.green}`）达成。

### 排印比例

| Token | 尺寸（clamp） | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-hero}` | 56–160px | Bebas Neue | 400 | 收尾或超大封面标题 |
| `{typography.display-cover}` | 48–140px | Bebas Neue | 400 | 封面 / 开场展示标题 |
| `{typography.display}` | 48–120px | Bebas Neue | 400 | 主要宣言或标注展示 |
| `{typography.headline}` | 42–90px | Bebas Neue | 400 | 主分节标题 |
| `{typography.statement}` | 36–90px | Bebas Neue | 400 | 长引述陈述 |
| `{typography.headline-md}` | 36–72px | Bebas Neue | 400 | 编辑分节头 |
| `{typography.title}` | 24–42px | Bebas Neue | 400 | 区域或拼贴件标题 |
| `{typography.number-hero}` | 80–160px | Bebas Neue | 400 | 英雄统计数字 |
| `{typography.number-md}` | 44–80px | Bebas Neue | 400 | 块或次级统计数字 |
| `{typography.drop-cap}` | 48–80px | Bebas Neue | 400 | 引领编辑段落的首字 |
| `{typography.body-md}` | 14–18px | Space Grotesk | 400 | 导语段或强调正文 |
| `{typography.body}` | 13–16px | Space Grotesk | 400 | 标准段落正文 |
| `{typography.label-eyebrow}` | 14–18px | Bebas Neue | 400 | 标题上方的 eyebrow 标签，字距 0.2em |
| `{typography.label-spaced}` | 12–14px | Space Grotesk | 600 | 加字距的全大写小标签 |
| `{typography.caption-feature}` | 13–15px | Bebas Neue | 400 | 加字距的全大写图注或特性标注标签 |
| `{typography.hand-script}` | 22–36px | Caveat | 600 | 作者署名、装饰便签、陈述署名行 |
| `{typography.hand-script-sm}` | 16–22px | Caveat | 400 | 小号手写标签或描述词 |
| `{typography.hand-script-lg}` | 24–36px | Caveat | 600 | 较大的手写副标题 |

### 默认值
- **主分节标题默认尺寸**：`{colors.green}` 的 `{typography.headline}`（42–90px clamp）。
- **封面或超大开场标题默认尺寸**：`{colors.green}` 的 `{typography.display-cover}`（48–140px clamp）。
- **段落正文默认尺寸**：`{typography.body}`（13–16px clamp），杂志语域要小正文，不是现代 18px+ 段落。
- **导语段或强调正文默认尺寸**：`{typography.body-md}`（14–18px）。
- **标题上方 eyebrow 标签默认尺寸**：`{colors.green}`、0.2em 字距全大写的 `{typography.label-eyebrow}`（14–18px）。
- **英雄数字默认尺寸**：`{colors.green}` 的 `{typography.number-hero}`（80–160px clamp）。
- **任何手写脚本署名 / 旁注默认尺寸**：`{typography.hand-script}`（22–36px clamp）。
- **任何 Bebas 展示元素默认字重**：400（Bebas Neue 出厂即 400，改字重不属于系统）。
- **正文默认字重**：400；加字距全大写小标签：600。

页面主导文字在 `{typography.headline}` 与 `{typography.title}` 间拿不准时，取 `{typography.headline}`，`{typography.title}` 留给页内拼贴件或区域级副标题。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个 Bebas Neue 元素都全大写。** 这款字体有小写字形，但本系统不用。句式 Bebas 不在词表内。
- **每个 Bebas Neue 元素都带至少 0.02em 的正字距。** Bebas 用默认字距读作拥挤，0.02–0.04em 把它打开。标签与 eyebrow 字距更大（0.2–0.25em）。
- **每个主分节标题都设 `{colors.green}`。** 黑标题存在（给与正文配对的栏），但系统最响的编辑声部是绿压卡其。
- **每个开启一栏的编辑段落都可带首字下沉。** 首字下沉始终是 `{components.drop-cap}`，绿色、Bebas Neue、行高 0.8、左浮动。用它作长篇正文栏的开场华彩。
- **每个手写脚本元素都用 Caveat。** 换成别的脚本字面会丢掉私人便签声部。
- **手写脚本署名在引文 / 陈述布局里跟在展示标题之后。** 陈述没有手写脚本署名行读作不完整，署名把引文落成一个人的声音。
- **正文里的行内高亮用黑压卡其式样**（`{components.inline-highlight}`），不用绿压卡其。绿色行内读成笔误，黑色行内读作马克笔划痕。

### 排印原则
系统的排印节奏来自**三字面反差**：压缩工业 Bebas 展示（响、加字距、全大写）→ 干净 Space Grotesk 正文（静、小、句式）→ 表现性 Caveat 手写脚本（私人、松、签名式）。只用一款字面的页读作单调，在单一构图里把三款混起来的页读作杂志式正确。

行高：展示紧（0.85–1.1）、正文宽（1.6–1.7）、手写脚本松（1.3）。绝不要倒置，正文紧、展示松都会破掉节奏。

## 布局

### 画布系统
系统以 `100vw × 100vh` 满视口为目标。每张 `.slide` 绝对定位铺满视口，只有 `.active` 页可见（opacity 1，其余 opacity 0）。页间过渡用 0.6s opacity + translateY(20px) ease，求柔和的翻纸感。导航由 JS 驱动，方向键、空格、点击、触屏滑动。一条 4px 高的 `{colors.green}` 进度条齐平贴在底边。

### 内边距比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.slide-pad}` | 60px | 标准页面外内边距 |
| `{spacing.slide-pad-wide}` | 60px 80px | 编辑栏跨页外内边距 |
| `{spacing.card-pad-lg}` | 48px | 英雄卡片内部（RSVP、大标注） |
| `{spacing.card-pad-md}` | 32px | 网格盒单元内部 |
| `{spacing.card-pad-sm}` | 24px | 拼贴件、较小卡片单元内部 |
| `{spacing.gap-lg}` | 60px | 编辑栏间隙 |
| `{spacing.gap-md}` | 40px | 标准区域间隙 |
| `{spacing.gap-sm}` | 24px | 紧凑行内间隙 |

### 常驻外壳
三个常驻元素活在页面构图之外：
- **进度条**：齐平贴在左下，4px 高，填充 `{colors.green}`，随文稿推进增长。
- **页码**：右下，Bebas Neue 14px，装在 2px 边框奶油小片里、卡其墨色。
- **导航提示**：底部居中，黑填充胶囊配奶油文字，仅在 `body:hover` 时淡入（0.4s opacity 过渡）。

### 区域边框对内部内边距
系统对网格容器遵循**边框即分隔**原则：父容器有 3px 实黑外边框，每个子单元有 1.5px 实黑边框，造出单元间细线分隔。区域在页边相接时（分屏布局），分隔线是 3px 实黑，两个区域直接贴着它，没有间隙。

自由构图（拼贴、英雄、宣言）里，区域带旋转与重叠绝对定位，边框落在各个件上，而非落在页面网格上。

## 纵深与层级

### 纸压纸偏移块（主手法）
招牌纵深处理是**偏移色块**：卡片带一个绝对定位的 `::before` 伪元素，朝右下偏移 12px、填 `{colors.green}`（或别的强调色）、z-index 排在卡片之后。视觉效果是分层纸套印，卡片看着像坐在一张略大的绿纸上面，绿色从右下边缘透出来。用于英雄 RSVP 卡与主标注容器。

### 旋转（次级手法）
印章标记、RSVP 标签、视觉叠加标注、拼贴件上的小旋转（`-8deg` 印章、`+6deg` stamp-alt、`-5deg` 到 `+5deg` 拼贴）给系统手放的能量。旋转是刻意的，绝非偶然歪斜，且只留给该读作实体物件的元素（印章、贴胶带的件、贴上去的标签）。

### 颗粒叠层（氛围纹理）
一层细微的 SVG 分形噪声叠层以 0.07 不透明度盖在每页上，给所有表面染上印刷颗粒。严格说这不是纵深，而是把每块平色块落实在印刷纸语域里的表面纹理。去掉颗粒会立刻破掉杂志声部。

### 无网页阴影
系统用**零模糊 `box-shadow`、零 `drop-shadow`、零 rgba 着色阴影**做纵深。偏移色块、旋转、颗粒叠层就是全部纵深语法。任何元素上的现代柔阴影都会破掉印刷美学。

### 色块反差
阴影与旋转之外，**绿压卡其与黑压卡其的反差**提供区域纵深。卡其区域里的绿飘带条在视觉上往前凸，白卡背后的黑区域在视觉上往后退。调色板的高反差是次级纵深信号。

## 形状与处理

### 圆角
系统**没有圆角**。每个形状，卡片、飘带条、印章、RSVP 卡、表格单元、首字下沉、小片、分隔短线，都是严格矩形或方形。border-radius 全系统为 `0`。

### 边框粗细
- **3px 实 `{colors.black}`**：卡片、区域分隔、网格容器外边框、拼贴件、RSVP 卡、英雄标注上的通用结构边框。
- **2px 实 `{colors.black}`**：编辑栏线、RSVP 栏下划线、ed-header 底边、印章标记的绿边框。
- **1.5px 实 `{colors.black}`**：3px 外边框容器内的网格单元子边框、账表头下划线。
- **1px 实 rgba(black, 0.22)**：账表行分隔与细线表格分隔。

边框始终是黑。除 `{components.stamp-mark}` 批准印章上的绿边框外，不存在彩色边框。

### 装饰元素类型

**线盒（`{components.line-box}`）**：卡其背景上的通用 3px 边框卡片。系统默认内容容器。内边距取 `{spacing.card-pad-*}` 比例。

**带偏移卡片（`{components.card-offset}`）**：白奶油卡，3px 黑边框，一块经 `::before` 坐在背后 12px 偏移的绿板。招牌纸压纸卡片。

**印章（`{components.stamp}` / `{components.stamp-mark}`）**：任何元素可旋转 -8°（stamp）或 +6°（stamp-alt），读作手压的印记。`stamp-mark` 变体是黑矩形配绿文字、绿边框。用作批准封印、`CONTACT US` 徽章、编辑印章。

**拼贴件（`{components.collage-piece}`）**：自由定位面板，3px 黑边框、小旋转。背景在件间轮换：绿、白奶油、深卡其、黑反色。用于多件散落重叠在页上的拼贴构图。

**胶带（`{components.tape}`）**：半透明白矩形，以随机角度叠在拼贴件上，暗示被胶带贴住的实体纸。始终半透明、始终带锐角（-40° 到 +35°）。

**飘带条（`{components.ribbon-bar}`）**：实绿色块配奶油文字，用作 eyebrow 条、强调条、行内分节标签。读作粘在页上的印刷飘带。

**首字下沉（`{components.drop-cap}`）**：开启编辑段落的超大绿色 Bebas Neue 首字母。左浮动、行高 0.8，正文绕排。

**行内高亮（`{components.inline-highlight}`）**：黑压卡其的马克笔划痕，行内施于正文段里提起一个短语。相当于印刷版的马克笔。

**RSVP 栏（`{components.rsvp-field}`）**：表单栏行式样，Bebas Neue 绿标签配手写脚本 Caveat 的"填写"，压在 2px 黑下划线上。系统的"手工填写"表格式样。

**账表行（`{components.ledger-row}`）**：横向数据行式样，列有 date | title | edition | track | nr。表头行带 1.5px 黑下划线，正文行带 1px 细线分隔。每行可含一个颜色编码的 `{components.chip}` 标类别。

**小片（`{components.chip}`）**：等宽字体色块（用则 JetBrains Mono，否则默认等宽），标行类别。填充色：绿，外加从更广印章调色板取色的页上的分类型调色板扩展。

**分隔短线（`{components.divider-stub}`）**：居中的短 4px 实水平线（60–80px 宽），作英雄标题或陈述上下的视觉呼吸。绿表面上为白，黑表面上为绿。

**手写脚本元素**：任何 Caveat 文字。系统标示"人的声音"的信号，署名、旁注、图注、RSVP 栏填值、收尾页落款。

## 该做与不该做

### 该做
- 每页保留 SVG 颗粒叠层（`{components.grain-overlay}`）于 0.07 不透明度。它是把整份文稿锚在印刷纸语域上的纹理。
- 每个展示、标题、陈述、统计、数字、eyebrow 标签都用 Bebas Neue 全大写、0.02–0.04em 字距。
- 主分节标题默认标题色取 `{colors.green}`。绿压卡其是系统最响的编辑信号。
- 英雄标注与 RSVP 式卡片用纸压纸偏移式样（`{components.card-offset}`），经 `::before` 在白卡后放一块绿板。
- 给该读作实体物件的元素套小旋转（-8° 印章、-5° 到 +5° 拼贴件）。旋转始终要显得刻意。
- 用首字下沉（`{components.drop-cap}`）开启编辑正文栏。它们是系统的编辑指纹。
- 在单一构图里混三款字面，Bebas Neue 展示 + Space Grotesk 正文 + Caveat 手写脚本。三字面反差是排印节奏。
- 正文段里的行内高亮设黑压卡其（`{components.inline-highlight}`），模仿马克笔划痕。
- 每条引文 / 陈述都在下方配一行 Caveat 手写脚本署名。脚本署名把引文落成人的声音。
- 在拼贴构图上以锐角叠半透明胶带片（`{components.tape}`），暗示被胶带贴住的实体纸。

### 不该做
- 不要给任何角加圆角。每个元素上 border-radius 全系统为 0。
- 不要用模糊 `box-shadow`。纵深全来自偏移色块、旋转与颗粒叠层。
- 不要把 Bebas Neue 换成别的展示字面。压缩工业加字距全大写的声部就是整套系统身份。
- 不要把 Bebas Neue 排成句式。本系统里 Bebas 始终渲染全大写，小写 Bebas 读作错的。
- 不要把 Caveat 换成别的脚本字面。随意圆珠笔声部属于系统，Lobster、Pacifico 等落在别处。
- 不要引入第三种品牌色。卡其 + 绿 + 黑 + 奶油就是系统。加蓝或加红会破掉土地与森林配色。小片调色板扩展（橙 / 粉 / 蓝 / 红）只预留给账表内分类型小片标签，不作通用强调。
- 不要把绿压卡其用于行内高亮。行内马克笔划痕是黑压卡其，绿色行内读成笔误。
- 不要把元素倾斜超过 ±8°。超过之后，手放就变成坏了。
- 不要把正文放到大于 18px。杂志栏密度语域依赖小正文（13–16px），现代 20px+ 正文读作尺寸过大。
- 不要用纯白（#FFFFFF）做卡片。奶油（`{colors.white}` #F4EFE6）维持纸压纸语域，纯白读作数字感。

## 响应式行为

系统以 `100vw × 100vh` 为目标、通篇用 `clamp()` 流式缩放。单条 `max-width: 768px` 媒体查询把多栏布局重排成单栏、去掉栏间边框线换成底边框、把页面内边距降到 32px。

### 缩放行为
- 展示标题从最小 48px 缩到最大 140–160px。
- 正文从 13px 缩到 16–18px。
- 内边距从 32px（移动端）缩到 60–80px（桌面）。
- 边框、胶带尺寸、印章旋转固定，不随视口缩放。

### 放映行为
- `ArrowRight`、`ArrowDown`、`Space`、`Enter`、`PageDown`、或点击视口右半前进。
- `ArrowLeft`、`ArrowUp`、`PageUp`、或点击左半后退。
- 激活页带 `.active` 类，非激活页 opacity 0 且 `translateY(20px)`。
- 移动端横向触屏滑动前进 / 后退。
- 底部居中导航提示在 `body:hover` 时淡入（0.4s opacity）。

### 打印行为
没有定义 `@media print` 规则。文稿以网页 / 视口为先。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁 | 中文 | 字重映射 |
|---|---|---|---|
| 展示 / 标题 / 陈述 / 题目 / 数字 / 首字下沉 / eyebrow 标签 | Bebas Neue（400） | **思源宋体 Noto Serif SC** | 900 |
| 正文 / 正文-md / 加字距标签 | Space Grotesk（400 / 600） | **思源宋体 Noto Serif SC** | 400（正文），600（标签） |
| 手写脚本（Caveat），仅拉丁 | Caveat（400 / 600） | *（无 CJK 替代）* | 不适用 |

### 混排策略

**策略 A：单一 CJK 字族（思源宋体 Noto Serif SC）承载每个排印角色。** Bebas Neue 压缩工业全大写声部，没有既保住厚重海报分量、又不读成套话汉字展示的中文无衬线对应。而 Noto Serif SC 字重 900 承载真正的印刷机分量，映射到杂志语域：深衬线笔画呼应凸版与木刻印刷，这比任何中文无衬线都*更*贴近系统的世纪中叶行动主义海报美学。拉丁 Bebas 配中文 Noto Serif SC 读作"同一份杂志的翻译版"，而非两套互相打架的系统。正文用同族字重 400，在小尺寸（13–16px）下安稳，保住杂志栏密度。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700;900&display=swap" rel="stylesheet">
```

然后把 `'Noto Serif SC'` 追加到相应字体栈：
```css
/* Display roles */
font-family: 'Bebas Neue', 'Noto Serif SC', sans-serif;
/* Body roles */
font-family: 'Space Grotesk', 'Noto Serif SC', sans-serif;
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

- **定义 Bebas 展示的 0.02–0.04em 正字距在 CJK 上必须降到 0**。加字距的汉字看着是坏的，间距在视觉上把每个字切成独立的词。Bebas 的压缩加字距招牌迁移不过来，单靠字重 900 扛起展示声部。
- **展示行高必须从 0.85–0.95 放宽到 1.15–1.25。** Bebas 的紧行高是拉丁展示惯例，CJK 字符占满 em 框，需要纵向呼吸空间。
- **首字下沉要重新想。** Bebas 首字下沉浮在正文左侧，同样尺寸（`clamp(48px, 6vw, 80px)`）的 `{colors.green}` Noto Serif SC 首字下沉视觉上成立，却缺编辑传统的共鸣，中文排印历史上不用首字下沉。要么把它当作西式编辑致意保留，要么换成一条沿开场段落走的绿色竖侧栏（3px 宽、绿填充）。
- **行内高亮、飘带条、印章标记都干净迁移**，它们是色块处理，不依赖字形。
- **手写脚本 Caveat 是系统的"人的声音"，没有能保住圆珠笔草书性格的中文对应。** 把 Caveat 瞬间当作纯拉丁：署名用拉丁，即便在其余全中文的页上旁注也用拉丁，RSVP 表单填值用拉丁。中文排印正文与拉丁手写页边注之间的反差其实能加深杂志声部（读作"译者注"，正贴小出版社语域）。
- **编辑正文尺寸（13–16px）仍然适用**，Noto Serif SC 在该尺寸下读作致密的杂志栏文，对杂志语域是对的。

### 已知 CJK 缺口

系统的三字面反差（Bebas 展示 + Space Grotesk 正文 + Caveat 手写脚本）是拉丁排印论点，塌成单一 CJK 衬线会丢掉一种节奏、换来另一种。选衬线（Noto Serif SC）而非无衬线（Noto Sans SC）是刻意的，杂志的世纪中叶印刷机血脉映射到中文衬线传统，比映射到中文几何无衬线更贴。中英混排的文稿得接受英文 Bebas 声部与中文宋体声部是不同语域，这在任何厚重海报式 CJK 改编里都不可避免。

## 迭代指南

1. 每张新页都带 0.07 不透明度的 SVG 颗粒叠层。去掉颗粒会立刻破掉杂志声部。
2. 任何新标题都用 Bebas Neue 全大写、字重 400、字距 0.02–0.04em。页面主瞬间取 `{colors.green}` 的 `{typography.headline}`；分屏或栏里标题与正文配对时用 `{colors.black}`。
3. 任何新正文都用 13–16px 的 Space Grotesk（导语正文 14–18px），行高 1.6–1.7。别把正文放大超过 18px。
4. 任何新 eyebrow 标签，最强调的用 `{colors.green}` 的 `{typography.label-eyebrow}`（Bebas Neue、14–18px、0.2em 字距），次级标签切到 `{typography.label-spaced}`（Space Grotesk 字重 600、0.25em 字距）。
5. 任何新卡片都用白奶油或卡其背景上的 3px 实黑边框。英雄标注加经 `::before` 的 12px 偏移绿板（`{components.card-offset}`）。
6. 任何新编辑栏都可带首字下沉，绿色 Bebas Neue、左浮动、行高 0.8。首字下沉是编辑指纹。
7. 任何新陈述 / 引文页都把 Bebas Neue 全大写引文与一行 Caveat 手写脚本署名配对。署名不可省略。
8. 任何拼贴构图都用带小旋转（-5° 到 +5°）的 3px 边框拼贴件，接缝处叠锐角半透明胶带片。背景轮换：绿、白奶油、深卡其、黑反色。
9. 任何账表都用 `{components.ledger-row}` 式样，表头下划线 1.5px、正文行分隔 1px 细线。分类型标签用绿色或分类型小片调色板的等宽 `{components.chip}`。
10. 状态 / 批准印章用 `{components.stamp-mark}`，黑背景、绿文字、2px 绿边框、旋转 -8°。留给配得上盖章的瞬间，滥用会稀释信号。

## 已知缺口

- 系统从 CDN 加载三款 Google Fonts（Bebas Neue、Caveat、Space Grotesk）。Bebas Neue 单字重（仅 400），试图用更重字重会回退。生产环境建议自托管。
- 颗粒叠层是带 `feTurbulence` 的行内 SVG data URI，渲染会随浏览器略变，较旧 Safari 与 Firefox 版本尤其。
- 纸压纸偏移块依赖 `z-index: -1` 的 `::before` 伪元素。卡片必须有 `position: relative` 且父级不得裁切 overflow，否则偏移板会被切掉。
- 账表行上的小片颜色扩展用红 / 粉 / 橙 / 蓝 / 绿，仅为表内分类型标记引入。这些颜色不属于通用系统调色板，不该出现在页面构图的别处。
- Caveat 手写脚本字面带很强的文化语域（随意美式手写）。它与非拉丁文字不搭，CJK 或西里尔文稿需要换别的手写脚本替代。
- 导航提示的 `body:hover` 淡入在触屏设备上不触发，意味着移动端用户可能永远看不到导航提示。把提示当作仅桌面外壳。
- 收尾页用 `{colors.black}` 背景配 `{colors.bg}`（卡其）文字。颗粒叠层仍适用，但 0.07 不透明度压在黑上明显更不明显，收尾页的印刷语域比卡其背景页弱。
- 表单 RSVP 卡用手画下划线（`_________`）作"空行"，这些是基于字符的、并非渲染成真正的 `<input>` 下划线，跨系统字体不会完美对齐。
