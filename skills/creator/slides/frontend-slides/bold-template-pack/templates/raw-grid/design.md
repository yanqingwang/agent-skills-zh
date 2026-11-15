---
version: alpha
name: Raw Grid
description: A neobrutalist presentation system where 3px solid black borders ARE the layout. Display type runs in the native system sans-serif stack (Segoe UI / system-ui) at weight 900 in strict uppercase — no web fonts loaded. The palette is white canvas + black structure + two muted pastel accents (blush pink #F2D4CF and sage green #E5EDD6) + a neutral gray. Depth comes from hard offset shadows in solid black at 4px and 6px — never blurred, never colored. The aesthetic borrows from brutalist editorial web design and zine layout: borders meet without gaps, contrast is high but warmed by the pastel accents, and large numerals sit at very low opacity behind content as decorative wallpaper. The effect is sharp, system-native, and unmistakably digital — closer to a Notion-meets-protest-poster than a polished pitch deck.

colors:
  black: "#0A0A0A"
  white: "#FFFFFF"
  pink: "#F2D4CF"
  green: "#E5EDD6"
  gray: "#F5F5F5"
  darkgray: "#333333"

borders:
  primary: "3px solid {colors.black}"

shadows:
  default: "6px 6px 0 {colors.black}"
  small: "4px 4px 0 {colors.black}"

typography:
  display:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(48px, 7vw, 96px)"
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -0.02em
    textTransform: uppercase
  headline:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(32px, 4.5vw, 64px)"
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.01em
    textTransform: uppercase
  title:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(24px, 2.5vw, 36px)"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0.01em
    textTransform: uppercase
  subtitle:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(16px, 1.4vw, 22px)"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.04em
    textTransform: uppercase
  body:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(16px, 1.3vw, 20px)"
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(11px, 1vw, 13px)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  number:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(64px, 8vw, 120px)"
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: -0.04em
  number-md:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(36px, 4vw, 56px)"
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: -0.02em
  number-lg:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(48px, 6vw, 80px)"
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: -0.02em
  label-text:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase

spacing:
  pad-lg: "clamp(32px, 4vw, 64px)"
  pad-md: "clamp(20px, 2.5vw, 40px)"
  pad-sm: "clamp(12px, 1.5vw, 20px)"
  gap-lg: "clamp(24px, 3vw, 48px)"
  gap-md: "clamp(16px, 2vw, 32px)"
  gap-sm: "clamp(8px, 1vw, 16px)"

canvas:
  width: 100vw
  height: 100vh

components:
  label:
    background: "{colors.black}"
    color: "{colors.white}"
    padding: "6px 14px"
    fontSize: 11px
    fontWeight: 800
    letterSpacing: 0.08em
    textTransform: uppercase
  line-h:
    width: 60px
    height: 4px
    background: "{colors.black}"
  line-v:
    width: 4px
    height: 60px
    background: "{colors.black}"
  line-full:
    width: "100%"
    height: 4px
    background: "{colors.black}"
  arrow-prefix:
    content: "→\\00a0"
    description: "Inline right-arrow glyph (U+2192) followed by a non-breaking space. Prepended via ::before on CTAs and interactive list items."
  icon-box:
    width: 48px
    height: 48px
    border: "3px solid {colors.black}"
    background: "{colors.white}"
    fontSize: "18px–20px"
    fontWeight: 900
    description: "Square white box with 3px black border, used for logos and feature icons. Contains 1–3 character glyph or Roman numeral."
  bar-track:
    width: "100%"
    height: 32px
    border: "3px solid {colors.black}"
    background: "{colors.white}"
  bar-fill-pink:
    background: "{colors.pink}"
  bar-fill-green:
    background: "{colors.green}"
  bar-fill-black:
    background: "{colors.black}"
    color: "{colors.white}"
  stat-box:
    border: "3px solid {colors.black}"
    padding: "clamp(16px, 2vw, 28px)"
    background: "{colors.white}"
  card:
    padding: "clamp(24px, 3vw, 48px)"
    border: "3px solid {colors.black}"
    description: "Generic content card. Background may be white, pink, green, or gray."
  decorative-numeral:
    fontWeight: 900
    fontSize: "clamp(40px, 5vw, 72px)"
    lineHeight: 1.0
    opacity: 0.2–0.35
    description: "Oversized numeral placed inside a card at very low opacity as decorative wallpaper behind the actual content."
  decorative-quote-mark:
    fontSize: "clamp(80px, 12vw, 160px)"
    fontWeight: 900
    opacity: 0.15
    description: "Oversized opening quotation mark placed absolutely at the top-left of a quote region at very low opacity."
  connector-node:
    width: 32px
    height: 32px
    border: "3px solid {colors.black}"
    background: "{colors.black}"
    color: "{colors.white}"
    fontSize: 16px
    fontWeight: 900
    description: "Small black square with white arrow glyph, used as a connector between sequential items in a horizontal flow."
  legend-swatch:
    width: 16px
    height: 16px
    border: "3px solid {colors.black}"
  donut-stroke-width: 24
  donut-track-stroke-width: 1.5
  table-cell:
    border: "3px solid {colors.black}"
    padding: "clamp(12px, 1.5vw, 20px)"
    fontWeight: 600
  table-header:
    background: "{colors.black}"
    color: "{colors.white}"
    fontWeight: 800
    letterSpacing: 0.06em
    textTransform: uppercase
  table-zebra-row:
    background: "{colors.gray}"
  hover-highlight:
    background: "{colors.green}"
    transition: "background 0.15s"
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/raw-grid/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Raw Grid 是一套**新粗野主义演示系统**，建立在单一结构前提上：**3px 实黑边框就是布局**。区域之间没有外边距，单元格之间没有间隙，没有圆角，没有渐变。两个区域相接时，一条 3px 黑线把它们分开，那条线就是整个网格系统。

字体的选择刻意不事装饰。系统用**原生系统无衬线栈**（`Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif`），无 Google Fonts、无网络字体、无授权。展示文字以字重 900 严格全大写、紧负字距运行。正文以字重 500 句首大写式运行。厚重全大写展示与轻句首大写正文的视觉反差，是系统的排印节奏。选系统字体本身就是美学表态：它读作"这是软件，不是印刷品"，是多数粗野主义系统那种印刷杂志美学的数字原生对位。

配色有六个 token，却担四个角色。**白**（`{colors.white}`）是画布。**黑**（`{colors.black}`）是结构：边框、标题、正文、标签填充、阴影色。**粉**（`{colors.pink}`，柔和腮红 #F2D4CF）与**绿**（`{colors.green}`，鼠尾草青瓷 #E5EDD6）是强调表面，暖与冷的对位，绝不用于文字，始终作区域填充。**灰**（`{colors.gray}` — #F5F5F5）是中性填充，用于表格斑马纹与三级表面。这些浅彩淡到黑文字在上面仍完全可读，这点不可少：系统从不在强调表面上反转文字色。

纵深完全是**硬边偏移阴影**，6px 与 4px 偏移、实黑、零模糊。没有 `rgba(...)`，没有 `0 4px 12px`。要么阴影是硬边实黑，要么根本没有阴影。

**密度取向：中等。** 系统用边框把区域干净地隔开，但每个区域装克制的内容，典型是一个展示元素配一段正文，或一个统计配一条图注。边框是响的（3px 实黑，不让步），区域里的内容是静的。在这套系统里读着别扭的页，是某个区域*空着*或*塞爆*；对的密度是每个带边框区域一个实质元素。

**关键特征：**
- 白（`{colors.white}`）画布配 3px 实黑（`{colors.black}`）边框分隔每个区域。单元格间无间隙，边框边到边相接。
- 系统无衬线，字重 900 全大写用于全部展示文字，字重 500 句首大写用于全部正文。
- 6px 与 4px 的硬边偏移阴影，实黑、无模糊，始终如此。
- 两种柔和浅彩强调表面，腮红粉与鼠尾草绿，作区域填充，绝不作为文字色。
- 招牌黑色胶囊 `label` 组件（`{components.label}`），小黑矩形里装白色全大写文字，作通用分节标签。
- 0.15–0.35 不透明度的超大装饰数字坐在内容背后当壁纸。
- 经 `::before` 给 CTA 与可交互列表项前置一个箭头字形（→ 配不换行空格）。
- 系统任何地方都没有圆角。每个形状都是严格矩形、方形或圆形。
- 系统零外部字体加载，任何有默认字体的浏览器里渲染都一致。

## 颜色

### 调色板
- **黑**（`{colors.black}` — #0A0A0A）：结构色。全部边框、全部标题文字、全部正文、全部标签填充、全部阴影值。比纯 #000000 略柔，但任何合理尺寸下都读作黑。
- **白**（`{colors.white}` — #FFFFFF）：画布。用作默认幻灯片背景、默认卡片背景，以及黑表面里的文字色（标签、表头、深色统计块）。
- **粉**（`{colors.pink}` — #F2D4CF）：柔和腮红。暖强调表面，区域背景、条形填充、统计块填充。浅彩饱和度让黑文字无需反转仍完全可读。
- **绿**（`{colors.green}` — #E5EDD6）：鼠尾草青瓷。冷强调表面，区域背景、条形填充、悬停态高亮、交替卡片。始终与粉配对，作为强调系统的两半，同一构图里很少单独出现。
- **灰**（`{colors.gray}` — #F5F5F5）：米白中性。用于表格斑马纹行与三级卡片背景，即某个区域需要与白区分、又不想用彩色强调时。
- **深灰**（`{colors.darkgray}` — #333333）：保留的三级文字色，token 系统里有，用得省。可供需要比纯黑读起来更柔的弱化文字使用。

### 默认值
- **默认表面背景**：`{colors.white}`。
- **默认标题色**：`{colors.black}`，始终如此。标题绝不出现在粉、绿、灰里，只在浅表面上为黑、黑表面上为白。
- **默认正文色**：`{colors.black}`。
- **默认边框色**：`{colors.black}`，始终如此。
- **暖区域默认强调表面**：`{colors.pink}`。
- **冷区域默认强调表面**：`{colors.green}`。
- **三级区域默认中性填充**：`{colors.gray}`。
- **`{colors.black}` 表面上默认文字色**：`{colors.white}`，系统里唯一的颜色反转。

强调表面（粉、绿）可互换，两者都没有固定语义角色（例如粉不表"警告"、绿不表"成功"）。挑最服务于构图的颜色反差即可。两个强调区域相邻时，把粉与绿配成暖 / 冷平衡，而不是一种色叠两次。

## 排印

### 字族
整套系统跑在**原生系统无衬线栈**上：`Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif`。不加载网络字体。这是刻意的，数字原生美学依赖文字用用户实际的系统字体渲染，而非下载的展示字面。结果只在精神上一致，字形不精确一致：macOS 渲染会与 Windows 略不同，而这份可变性落在系统容差之内，可以接受。

字重轴是全部的表现工具。展示文字用字重 900（最重），题目用 800，副标题用 700，正文用 500，无斜体变体、无替代字面。字重 900 全大写与字重 500 句首大写之间的反差，是系统的主排印节奏。

### 展示与数字比例

| Token | 尺寸（clamp） | 字重 | 字距 | 用途 |
|---|---|---|---|---|
| `{typography.number}` | 64–120px | 900 | -0.04em | 英雄数字统计 |
| `{typography.display}` | 48–96px | 900 | -0.02em | 分节开场或封面展示 |
| `{typography.number-lg}` | 48–80px | 900 | -0.02em | 大号装饰或精选数字 |
| `{typography.headline}` | 32–64px | 900 | -0.01em | 主分节标题 |
| `{typography.number-md}` | 36–56px | 900 | -0.02em | 统计块或指标数字 |
| `{typography.title}` | 24–36px | 800 | 0.01em | 区域或分节标题 |
| `{typography.subtitle}` | 16–22px | 700 | 0.04em | 副标题、区域内标题 |
| `{typography.body}` | 16–20px | 500 | 0 | 段落正文 |
| `{typography.caption}` | 11–13px | 700 | 0.08em | 图注、细则、脚注 |
| `{typography.label-text}` | 11px | 800 | 0.08em | 黑色标签胶囊里的文字 |

### 默认值
- **主分节标题默认尺寸**：`{typography.headline}`（32–64px clamp）。
- **封面或开场展示默认尺寸**：`{typography.display}`（48–96px clamp）。
- **段落正文默认尺寸**：`{typography.body}`（16–20px clamp）。
- **任何行内标签或图注默认尺寸**：`{typography.caption}`（11–13px clamp）。
- **任何展示元素默认字重**：900。
- **任何正文元素默认字重**：500。
- **英雄数字默认尺寸**：`{typography.number}`（64–120px clamp）。

拿不准时，页面主文字瞬间取 `{typography.headline}`，别取 `{typography.title}`（那是页内区域级标题）。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个 display、headline、title、subtitle 元素都全大写。** 本系统不存在句首大写式展示文字。文字若落在 `{typography.display}`、`{typography.headline}`、`{typography.title}` 或 `{typography.subtitle}`，就必须全大写。
- **每个正文元素都句首大写。** 绝不给 `{typography.body}` 元素全大写，展示与正文之间的全大写 / 句首大写反差是系统的排印信号。
- **每个展示元素都用负字距。** Display（–0.02em）、headline（–0.01em）、number（–0.04em）。展示用默认字距读作未处理，负字距才给文字压缩的粗野密度。
- **每个图注与标签都用至少 0.06em 的正字距。** 不加字距的图注与标签字形读成代码，不像编辑。
- **所有数字都用字重 900 配负字距。** 连小统计数字（36–56px）也守展示字重惯例。

### 排印原则
字重 900 + 全大写 + 负字距的组合是系统的主"声部"。三者中任一属性被换掉（例如字重 700 全大写，或字重 900 句首大写）都读作另一套设计系统。字重 800 预留给 `{typography.title}` 与标签，字重 700 给 `{typography.subtitle}` 与 `{typography.caption}`，字重 500 给正文。不要用中间字重（400、600），字重阶梯是固定的。

系统任何地方都不用斜体。下划线不用。唯一的强调机制是字重反差。

## 布局

### 画布系统
系统以 `100vw × 100vh` 满视口为目标。每张 `.slide` 绝对定位铺满视口，同一时刻只有一页 `display: flex`（翻页由 JS 驱动，键盘方向键、空格、触屏滑动）。所有尺寸用 CSS `clamp()`，布局无需断点便在最小与最大之间流式缩放。

### 内边距与间隙比例
| Token | 区间 | 用途 |
|---|---|---|
| `{spacing.pad-lg}` | 32–64px | 外层幻灯片区域内边距、满区域单元格 |
| `{spacing.pad-md}` | 20–40px | 头带、次级区域 |
| `{spacing.pad-sm}` | 12–20px | 紧凑区域、表格单元 |
| `{spacing.gap-lg}` | 24–48px | 大 flex/grid 间隙 |
| `{spacing.gap-md}` | 16–32px | 标准 flex/grid 间隙 |
| `{spacing.gap-sm}` | 8–16px | 紧凑行内间隙 |

### 边框即布局原则
定义性的结构式样：**区域由 3px 实黑边框分隔，而非由间隙分隔**。页面分成两列网格时，两列共享中间一条 3px 黑色竖边框，单元格直接贴着那条边，没有 `gap` 属性、没有外边距。头带坐在内容区上方时，一条 3px 黑色水平线把它们分开，两个区域都紧贴这条线。这是系统最鲜明的结构选择。

区域内部的内边距（`{spacing.pad-lg}` 等）提供单元格里的呼吸空间。单元格之间的间隙不存在。

## 纵深与层级

### 硬边偏移阴影（唯一手法）
系统恰好用两个阴影值：
- **`{shadows.default}`** = `6px 6px 0 {colors.black}`，抬升元素（大卡片、主标注）的标准硬边偏移阴影。
- **`{shadows.small}`** = `4px 4px 0 {colors.black}`，较小抬升元素的轻偏移。

两个阴影都是**实黑、零模糊、固定朝右下偏移**。没有按颜色变化的阴影、没有模糊投影、没有柔化抬升。一个元素要么投硬边偏移阴影，要么完全不投。

### 基于边框的纵深
系统多数表观"纵深"其实来自边框，而非阴影。彩色背景上卡片周围的 3px 实黑边框，无论卡片是否带阴影都读作抬升。只在元素需要显得"从下方表面掀起"时才用阴影，典型是与所在区域重叠或浮在其上的卡片。

### 装饰壁纸（氛围纵深）
一个招牌处理：以极低不透明度放在卡片内的超大数字（最大引号标记 0.15、步骤数字 0.20、卡片序数 0.35），坐在真实内容背后作装饰壁纸。数字填满区域左上或上部，真实标题以全不透明度压在前面。这造出分层效果，内容压装饰，却不用任何 z-index 花招。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 0px | 除圆以外的一切 |
| 50%（圆） | 仅环形图形状 |

系统**没有圆角**。卡片、按钮、标签、图标盒、统计块、表格单元、图片框，全是严格矩形或方形。唯一的圆是 SVG 环形图，它因几何必需而是圆。

### 边框粗细
- **3px 实 `{colors.black}`**：通用边框。用于每处结构分隔：区域分隔、卡片轮廓、表格单元、图标盒、连接节点、色样、条轨道、统计块边框。绝不更细、绝不更粗、绝不上色、绝不成虚线。
- **4px 实 `{colors.black}`**：只用于 `{components.line-h}` 与 `{components.line-v}` 装饰线元素（60px 短线）。
- **4px 实 `{colors.white}`**：只用于黑色图片区里的图片占位框（白压黑语境下的反色边框处理）。
- **1.5px 描边**：只用于 SVG 环形图 0.1 不透明度的内描边（一条几乎看不见的内环）。

### 装饰元素类型

**黑色标签胶囊**：小黑矩形，内装 11px / 字重 800 / 0.08em 字距的白色全大写文字，6px × 14px 内边距。系统的通用分节标签、财年标记、状态小片。CTA 变体可前置 `{components.arrow-prefix}`。

**水平短线**：60px × 4px 实黑矩形（`{components.line-h}`），作标签旁的行内视觉分隔或强调。在编辑布局里充当"分节断口"标记。

**图标盒**：48px × 48px 白方块，3px 黑边框，内含一个 18–20px 字重 900 的 1–3 字符字形（首字母、罗马数字、单字母）。用作标志标记与特性图标。

**装饰超大数字**：一个大数字字符（通常是步骤号或分节序数），字重 900，以 0.15–0.35 不透明度放在卡片里。坐在卡片真实内容背后或上方作壁纸。

**连接节点**：32px × 32px 实黑方块，内含字重 900 的白色箭头字形。绝对定位在横向流程里相邻条目之间（如时间轴步骤间）。充当阶段之间的视觉"→"。

**条轨道**：32px 高横向矩形，3px 黑边框、白内部。填充（粉、绿或黑）是一个子 `div`，其 `width` 百分比代表数据值，数值标签以 12px 字重 800 印在填充里。黑条文字色反转成白。

**统计块**：带边框的卡片（`{components.stat-box}`），上方一个大数字（`{typography.number-md}`）、下方一条小图注（`{typography.caption}`）。背景可为白、粉、绿、灰或黑（配相应文字反转）。

**箭头前置文字**：文字元素（CTA、可交互列表行）经 `::before` 前置一个 `→`（U+2192）配不换行空格，标示动作或导航。这是系统的可交互性信号。

**环形图**：多段 SVG 环，24px 描边宽度，配 0.1 不透明度的 1.5px 内分隔环。分段用调色板色（黑、粉、绿），中心放一对数值 + 标签。

## 该做与不该做

### 该做
- 每处结构分隔都用 3px 实黑边框。边框粗细是系统的身份，更细读作通用网页应用，更粗读作坏了。
- 标题色默认设 `{colors.black}`。本系统不存在粉、绿、灰的标题。
- 两个强调表面同现时，把粉与绿配成对位，暖配冷，绝不让两粉或两绿相邻。
- 每个展示元素一起套全大写 + 负字距 + 字重 900。三个特征不可分，单独用会丢掉粗野性格。
- 用黑色标签胶囊（`{components.label}`）作通用分节标签。它是系统最鲜明的小组件，应大方出现。
- 每个 CTA 与可交互列表行都用箭头前置（`→ + nbsp`）。它是系统的可交互性信号。
- 阴影渲染成 `6px 6px 0 {colors.black}` 或 `4px 4px 0 {colors.black}`。只有两个阴影值，挑一个。
- 有数字身份的卡片（步骤号、序数、引号标记）里，把超大装饰数字以 0.15–0.35 不透明度放在内容背后。壁纸数字式样是系统招牌。
- 让边框直接相接。两个区域在一条 3px 黑线处相接是对的，它们之间有间隙是错的。
- 正文用字重 500 句首大写，展示用字重 900 全大写。两者的反差是排印节奏。

### 不该做
- 不要加载任何网络字体。系统跑在原生无衬线栈上，Segoe UI / system-ui / Helvetica。加 Google Fonts 会破掉数字原生美学。
- 不要给任何角加圆角。卡片、按钮、标签、图标盒，全是严格矩形。border-radius 只允许给圆（环形图）。
- 不要用模糊阴影。`0 4px 12px rgba(0,0,0,0.1)` 在这里不存在。要么 4px/6px 硬实黑偏移，要么没有。
- 不要给边框上色。所有结构边框都是黑。彩色边框会破掉系统。
- 不要用中间字重（400、600）。字重阶梯固定在 500 / 700 / 800 / 900。
- 不要用斜体或下划线。唯一的强调机制是字重反差。
- 不要把展示字重文字排成句首大写。全大写在 display、headline、title、subtitle、caption token 上不可商量。
- 不要引入第三种强调表面色。粉与绿是仅有的强调表面。加黄卡或蓝卡会破掉暖 / 冷配对系统。
- 不要在由边框分隔的区域之间用 gap 属性。区域在边框处相接，彼此之间没有外边距。
- 不要在粉、绿、灰表面上反转文字色。浅彩本就为黑文字压在上面设计，反转处理只适用于 `{colors.black}` 表面。

## 响应式行为

与本库多数模板不同，Raw Grid **按设计就是视口流式**。整套系统用 CSS `clamp()` 定尺寸，没有固定画布尺寸。每个 `font-size`、`padding`、`gap`、`width` 值都按视口宽度在最小与最大之间线性缩放。同一构图在 1280×720 笔记本、1920×1080 显示器、2560×1440 屏上无需媒体查询都能正确渲染。

### 缩放行为
- 展示标题从最小视口的 48px 缩到最大的 96px。
- 正文从 16px 缩到 20px。
- `{spacing.pad-lg}` 内边距从 32px 缩到 64px。
- 边框、标签胶囊内边距、阴影偏移固定（3px、6px 14px、6px 6px），不缩放，这意味着视口越大，边框在比例上显得越细。

### 放映行为
- `ArrowDown`、`ArrowRight`、`Space` 前进。
- `ArrowUp`、`ArrowLeft` 后退。
- `Home` 跳到首页，`End` 跳到末页。
- 移动端竖向触屏滑动前进 / 后退。
- 激活页带 `.active` 类，非激活页 `display: none`。

### 打印行为
一条 `@media print` 规则把所有页设为 `display: flex` 配 `page-break-after: always`，打印文稿会产出逐页顺序的 PDF。

### 悬停态
系统独有一处：交互悬停态被烘进设计里，列表项与表格行悬停时经 0.15s 过渡高亮到 `{colors.green}`。这对演示系统不寻常，反映 Raw Grid 兼具演示与产品原型的混合身份。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁 | 中文 | 字重映射 |
|---|---|---|---|
| 展示 / 标题 / 题目 / 副标题 | Segoe UI / system-ui（900） | **思源黑体 Noto Sans SC** | 900 |
| 正文 / 图注 / 标签 | Segoe UI / system-ui（500–800） | **思源黑体 Noto Sans SC** | 500（正文），700–800（图注 / 标签） |

### 混排策略

**策略 A：整套系统用单一 CJK 字族。** Raw Grid 刻意是单字族系统，每个字重（900 / 800 / 700 / 500）都来自同一条拉丁栈。用单一 CJK 字族 Noto Sans SC 镜像它，保住系统最定义性的属性：排印统一性。由于拉丁栈是 `system-ui`（Windows 上 Segoe UI、macOS 上 San Francisco），配一款高质量 CJK 网络字体，能让渲染尽可能贴近数字原生美学要求的"系统原生"。用两款 CJK 字族会碎掉新粗野主义的单一体制。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@500;700;800;900&display=swap" rel="stylesheet">
```

然后在每个 font-family token 里把 `'Noto Sans SC'` 追加到拉丁栈之后：
```css
font-family: 'Segoe UI', system-ui, -apple-system, Helvetica, Arial, 'Noto Sans SC', sans-serif;
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

- **定义拉丁展示声部的负字距迁移不过来。** 给每个 CJK 展示元素设 `letter-spacing: 0`。Noto Sans SC 字重 900 本就读作致密、粗野，负字距会把字挤在一起，读成渲染 bug 而非设计选择。
- **全大写是整个拉丁展示声部，而它在中文里不存在。** 补偿办法是更倚重字重反差（900 展示对 500 正文）与标签胶囊的白压黑反转。粗野密度来自字重阶梯，不来自大小写。
- **黑色标签胶囊（`{components.label}`）漂亮地扛住了翻译。** 2–4 字的中文标签（品牌、信号源、第四季度）用 Noto Sans SC 800，读起来比英文对应更紧凑，甚至更醒目。
- **0.15–0.35 不透明度的装饰超大数字应保持拉丁**（阿拉伯数字在这套系统里看着对，全角中文数字零一二三不承载同样的壁纸数字信号）。
- **箭头前置（`→`）在 CJK 语境里渲染一致**，对两种语言都是对的可交互性信号。

### 已知 CJK 缺口

Raw Grid 的整个美学论点是"这是用户实际的系统字体，不是下载的展示字面"。加载 Noto Sans SC 在技术上破了这份纯粹，但没有可接受的替代。macOS 自带 PingFang SC、Windows 自带 Microsoft YaHei，可两者在 "900" 下渲染出的字重明显不同，而数字原生美学依赖字重 900 读起来一致。Noto Sans SC 是对网络字体最小的可接受让步，把它当作"无网络字体"规则仅对 CJK 内容的唯一例外。

## 迭代指南

1. 任何新结构区域都用 3px 实黑边框与邻区隔开。绝不在区域之间用间隙或外边距，边框就是分隔。
2. 任何新卡片或面板都继承带边框矩形式样：3px 实黑边框、方角、内边距取 `{spacing.pad-*}` 比例、背景取调色板（白、粉、绿、灰、黑）。
3. 任何新标题都用 `{colors.black}` 色的 `{typography.headline}`（封面级瞬间用 `{typography.display}`）、全大写。主瞬间别取 `{typography.title}`，那是副标题。
4. 任何新标签或小片都用 `{components.label}` 式样：黑背景、11px / 字重 800 / 0.08em 的白色全大写文字。
5. 任何新数字都守字重 900 + 负字距惯例。统计块用 `{typography.number-md}`，英雄统计用 `{typography.number}`。
6. 任何新强调表面按暖 / 冷需要挑粉或绿。不要引入第三种颜色。
7. 任何新 CTA 或可交互元素都带 `→` 箭头前置，若抬升再加 `6px 6px 0 {colors.black}` 阴影。
8. 卡片需要"个性"元素时，加一个 0.15–0.35 不透明度的超大装饰数字，而非图形或图标。壁纸数字处理是系统招牌装饰手法。
9. 表格守带边框单元格 + 斑马纹 + 黑表头式样。别重新设计它们，粗野表格美学是系统身份的一部分。

## 已知缺口

- `--darkgray`（#333333）CSS 变量有定义，但没有任何规则在用它。它作为保留的三级文字色可用，源码里未部署到任何地方。
- 系统不加载外部字体，渲染出的字形会随操作系统不同。macOS 把 system-ui 渲染成 San Francisco，Windows 渲染 Segoe UI，Linux 渲染所配置的无衬线。这份视觉不一致是刻意的，但值得记下。
- 悬停态（列表项 → 绿、表格行 → 绿）是交互网页行为，在打印或静态导出里没有对应物。当作附赠的交互，别当核心设计系统。
- 翻页 JavaScript 内联嵌着，处理键盘、触屏与 active 类系统。任何新页都必须遵循 `<div class="slide sN">` 式样并遵守 `current` 索引。
- SVG 环形图用硬编码的 `stroke-dasharray` 值，需按分段百分比与图表 80px 半径周长（约 502.4）手工计算。没有数据绑定层。
- 图片配对区域上的图片占位只是一个带 4px 白边框、写 "[ Image Placeholder ]" 的 div，真正插入图片需把占位 div 换成 `<img>`，并让父级背景与图片负空间相配。
- `.s5-image-placeholder` 里含 "Cohots"（原文如此）一词，看起来是源码里 "Cohorts" 的笔误。复用内容时标一下。
