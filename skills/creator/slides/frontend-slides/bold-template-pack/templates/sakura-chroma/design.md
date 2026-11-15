---
version: alpha
name: Sakura Chroma
description: "A cassette-package editorial system on warm cream paper with a six-color primary palette and warm-brown ink. Display type runs in Big Shoulders Display (condensed industrial display sans at weight 900); body in Albert Sans; tabular and tag content in JetBrains Mono; occasional Japanese accents in Noto Sans JP. The aesthetic borrows from 1970s consumer cassette packaging, Japanese print catalogues, and lo-fi product zines: petal-cluster blob clusters, diagonal multi-color ribbon bands, 12-point starburst seals, red rectangular stamps, and tracked uppercase micro-labels. The effect is hand-curated industrial editorial — warm but disciplined, playful but tightly typeset, with the cassette as its visual metaphor."

colors:
  paper: "#F1E6CB"
  paper-dk: "#E5D6B0"
  ink: "#3A2516"
  red: "#E5392A"
  pink: "#E54489"
  orange: "#F09131"
  green: "#3D9F47"
  blue: "#3F8BC4"
  yellow: "#F0BC2A"

color-aliases:
  line: ink

typography:
  disp-hero:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(120px, min(14vw, 22vh), 280px)"
    fontWeight: 900
    lineHeight: 0.84
    letterSpacing: -0.025em
  disp-statement:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(70px, min(8.4vw, 14vh), 168px)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: -0.022em
  disp-title:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(80px, min(9vw, 14vh), 180px)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: -0.022em
  disp-lockup:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(56px, min(7vw, 11vh), 130px)"
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.015em
  disp-section:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(52px, min(5.6vw, 9vh), 100px)"
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.018em
  disp-quote:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(48px, min(5.4vw, 9vh), 110px)"
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: -0.018em
  disp-quote-lg:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(56px, min(6.4vw, 10.5vh), 130px)"
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.018em
  disp-brand:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(32px, min(3.4vw, 5.4vh), 56px)"
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: -0.02em
  disp-card-name:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(28px, min(2.6vw, 4.6vh), 48px)"
    fontWeight: 900
    lineHeight: 0.94
    letterSpacing: -0.012em
  num-hero:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(110px, min(11vw, 18vh), 240px)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: -0.025em
  num-md:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(70px, min(7vw, 11vh), 150px)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: -0.02em
  ttl-row:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(22px, 1.7vw, 30px)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.005em
  body:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(14px, 1vw, 17px)"
    fontWeight: 400
    lineHeight: 1.5
  body-md:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(14px, 0.95vw, 15px)"
    fontWeight: 400
    lineHeight: 1.4
  body-emphasis:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(15px, 1.1vw, 20px)"
    fontWeight: 600
    lineHeight: 1.4
  micro:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(12px, 0.9vw, 14px)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.16em
    textTransform: uppercase
  micro-lg:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(12px, 0.9vw, 14px)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2em
    textTransform: uppercase
  micro-xl:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(12px, 0.92vw, 14px)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.32em
    textTransform: uppercase
  micro-spec:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(14px, 1.1vw, 20px)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.04em
  mono:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "clamp(11px, 0.78vw, 12px)"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  mono-md:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "clamp(14px, 0.95vw, 16px)"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  mono-tag:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "clamp(12px, 0.85vw, 14px)"
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.04em
  jp:
    fontFamily: "'Noto Sans JP', sans-serif"
    fontSize: "inherit"
    fontWeight: 500
    lineHeight: inherit
  stamp-text:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(20px, 1.6vw, 28px)"
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: 0.02em
  seal-text:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(22px, 2vw, 38px)"
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.01em

spacing:
  frame-inset: "clamp(36px, 3.6vw, 72px)"
  frame-inset-bottom: "clamp(72px, 7vh, 110px)"
  topbar-gap: "clamp(12px, 1.4vh, 22px)"
  card-pad-x: "clamp(14px, 1.4vw, 20px)"
  card-pad-y: "clamp(16px, 1.7vw, 24px)"
  grid-gap: "clamp(16px, 1.6vw, 26px)"
  col-gap: "clamp(28px, 3vw, 56px)"
  pagenum-inset: "clamp(20px, 2.2vh, 36px) clamp(24px, 2.2vw, 44px)"

canvas:
  width: 100vw
  height: 100vh

components:
  paper-texture:
    backgroundImage: "radial-gradient(circle at 1px 1px, rgba(58,37,22,0.55) 1px, transparent 1.6px)"
    backgroundSize: "4px 4px"
    opacity: 0.16
    zIndex: 1
    description: "Subtle 4px-period halftone-dot paper texture sitting over every slide stage at 16% opacity. Drawn as a 1px-period radial-gradient. Required — it is the paper-grain that anchors every flat color block in the print register."
  petals-cluster:
    description: "A decorative cluster of 4–5 overlapping perfect circles (each `aspect-ratio: 1/1, border-radius: 50%`) in the primary palette colors. Circles overlap and tile within a bounded container. Used as a brand mark, decorative anchor in slide corners, or quote-page ornament."
  ribbon-band:
    height: "clamp(40px, 6vh, 96px)"
    width: "160% (oversize so rotation clears the frame)"
    transform: "rotate(-22deg) or rotate(22deg)"
    description: "A bundle of 5 stacked solid-color horizontal bars (pink, orange, yellow, green, blue) rotated -22° or +22° to sweep diagonally across a region. Echoes the cassette-label color-stripe motif. Anchored to one edge of the slide and bleeds off the opposite edge."
  ribbon-single:
    height: "16–18%"
    width: "160%"
    transform: "rotate(±22deg)"
    description: "A single solid-color ribbon in a multi-color stack; each ribbon is positioned with its own top/bottom percentage so the stack reads as parallel rays."
  rosette-seal:
    width: "clamp(60px, 6vw, 110px)"
    aspectRatio: "1 / 1"
    background: "{colors.ink}"
    color: "{colors.paper}"
    clipPath: "32-point starburst polygon"
    description: "12+ point starburst clip-path shape filled ink with cream text. Used as an authority seal or volume marker. Always carries a 1–4 character glyph (a number, two-letter abbreviation, or short word) in Big Shoulders 900."
  red-stamp:
    background: "{colors.red}"
    color: "{colors.paper}"
    padding: "clamp(8px, 1vh, 14px) clamp(12px, 1.4vw, 22px)"
    transform: "rotate(-3deg) or rotate(0)"
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontWeight: 900
    description: "Red rectangular stamp with cream text, optionally rotated -3°. Used for status badges (COMPLETE, AS SEEN ON, LIMITED) and product callouts."
  card-product:
    border: "1.5px solid {colors.ink}"
    background: "{colors.paper}"
    overflow: hidden
    description: "Vertical product card with a 1.5px ink border, a colored topstrip header band, and a stacked body of name + description + extras + monospaced spec rows. The catalogue grid's primary unit."
  card-topstrip:
    height: "clamp(18px, 2vh, 32px)"
    description: "Colored horizontal band running the full width of a product card's top — fills in red, pink, orange, or blue depending on the card variant. Reads as a Pantone color tab."
  spec-checklist:
    description: "Vertical column of inline rows with a 14–20px square ink-bordered box (filled or empty) followed by a small caps label (COLOR, LO-FI, STEREO, LP). Echoes the cassette package's feature-spec checklist."
  bar-eq:
    bgUntint: "rgba(58, 37, 22, 0.10)"
    borderUntint: "rgba(58, 37, 22, 0.22)"
    description: "Equalizer-style bar chart. Each column is a stack of 6 equal-height tiles (segments). 'On' segments fill with one of the primary colors (red, pink, orange, yellow, green, blue) per column; 'off' segments fill with a translucent ink tint. column-reverse stacking means on-segments stack from the bottom up, like a VU meter."
  ledger-row:
    gridColumns: "96px 1.4fr 0.9fr 0.6fr 64px"
    paddingY: "clamp(10px, 1.2vh, 18px)"
    borderBottom: "1px solid rgba(58,37,22,0.22)"
    description: "5-column tabular row pattern: date | title | edition | chip | nr indicator. Header row uses a 1.5px ink border-bottom; body rows use 1px hairline ink-alpha dividers."
  chip:
    padding: "4px 10px"
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "11–12px"
    color: "{colors.paper}"
    textTransform: uppercase
    letterSpacing: 0.06em
    description: "Mono-font color chip tagging a ledger row's category. Background pulls from red, pink, orange, blue, or green."
  topbar-rule:
    borderBottom: "1.5px solid {colors.ink}"
    paddingBottom: "clamp(12px, 1.4vh, 22px)"
    description: "Section header underline pattern. A title (Big Shoulders 900 with optional red em-emphasis) on the left aligned-end with a tracked-caps label on the right, separated from the body by a 1.5px ink rule."
  qbody-box:
    background: "{colors.paper}"
    border: "1.5px solid {colors.ink}"
    boxShadow: "8px 8px 0 {colors.ink}"
    padding: "clamp(20px, 2.4vh, 40px) clamp(28px, 2.6vw, 48px)"
    description: "Quote body container with a 1.5px ink border and a hard 8px ink offset shadow. Sits on top of diagonal ribbons as a paper-on-ribbons callout."
  petal:
    aspectRatio: "1 / 1"
    borderRadius: "50%"
    description: "A single perfect circle in one of the primary colors. The atomic unit of petal-clusters and scattered blobs. Always perfectly round — never an ellipse."
  pagenum:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "clamp(11px, 0.82vw, 13px)"
    color: "{colors.ink}"
    letterSpacing: 0.06em
    description: "Bottom-right page indicator — mono font, formatted NN / TT. Required on every content slide."
  nb-checkbox:
    width: "clamp(14px, 1.1vw, 20px)"
    aspectRatio: "1 / 1"
    border: "2px solid {colors.ink}"
    checkedFill: "{colors.ink}"
    checkedMarker: "× (cream-colored multiplication sign in Big Shoulders 900)"
    description: "Ink-bordered square checkbox used in spec-checklists and the cover footer. Checked state fills ink and centers a cream multiplication-sign glyph (not a checkmark)."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/sakura-chroma/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Sakura Chroma 是一套**卡带包装编辑系统**，把每页当作一本小型日本音响产品目录里的印刷产品页。视觉隐喻是彻底的：花瓣簇色块标记、对角多色飘带、12 角星芒封印、红色矩形印章、等宽字体规格行、颜色编码小片、均衡器式条形图。一切都像从 1970 年代消费音响宣传册的封底跨页上抽出来的，温暖、手工甄选、工业式排印。

字体栈搭配四款字面，各有分明的功能角色。**Big Shoulders Display** 是展示声部，一款压缩工业无衬线，字重 900、紧负字距（-0.012em 到 -0.025em）。它承载每个展示瞬间：英雄数字、陈述、品牌锁定、卡片名、分节标题。它压缩的竖向感与厚重字重给系统响亮的目录封面声部。**Albert Sans** 是正文声部，一款干净的现代人文无衬线，字重 400–700 用于正文段、微标签、规格图注。**JetBrains Mono** 是表格声部，用于规格行、页码、日期、小片、均衡器刻度，以及一切需要读作"数据"而非"编辑"的瞬间。**Noto Sans JP** 是文化点缀，偶用于日文字符（限定版 "limited edition"），标示松本工坊的声部。四款字面合起来构成"工业展示 + 干净正文 + 等宽数据 + 日式调味"。

色彩理念是**暖奶油纸 + 墨棕结构 + 六色主强调集**。纸（`{colors.paper}` — #F1E6CB）是暖奶油，比常见骨白略深，另有一个更深的色调兄弟（`{colors.paper-dk}` — #E5D6B0）作分层表面。墨（`{colors.ink}` — #3A2516）是深暖棕而非纯黑，让每一处文字与边框都带纸上印刷的暖意。六种主色（红、粉、橙、黄、绿、蓝）出现在花瓣簇填充、飘带、卡片顶条、均衡器条填充、小片背景、红色矩形印章里。红与粉主导作强调色，橙 / 黄 / 绿 / 蓝阶梯充当分类型强调集。

纵深来自**硬边偏移阴影**（8px 8px 0 ink）、**纸张颗粒纹理**、**色块分层**，不靠模糊投影。招牌处理是 qbody-box（引文标注）带一道零模糊的 8px 硬墨色阴影；每页带一层 4px 周期的半调网点纸纹，16% 不透明度，把每个色块落实在印刷语域里；对角多色飘带扫在内容背后，是系统最鲜明的氛围层。

**密度取向：中高。** 目录语域依赖视觉丰盛：产品卡网格里 4 张叠卡各装名称 + 描述 + 规格行，7 行以上的账表，把英雄统计与均衡器图合起来的仪表盘，把品牌锁定 + 花瓣 + 飘带 + 英雄数字 + 规格清单 + 页脚叠起来的封面跨页。只有一个居中标题的页读作宣言瞬间（为冲击力刻意的稀疏），其余每页都该像塞满的目录页。对的密度是"每个区域都在同时干活"，顶条带标题 + 元数据标签，正文带主视觉 + 次级面板，往往还有一枚小片 / 印章 / 封印作装饰标点。

**关键特征：**
- 暖奶油纸画布（`{colors.paper}`）配暖棕墨（`{colors.ink}`）作结构，再加六种主强调色。
- 4px 周期半调网点纸纹（`{components.paper-texture}`）以 16% 不透明度盖在每页上。必需。
- Big Shoulders Display 字重 900 配负字距用于每个展示瞬间；Albert Sans 作正文；JetBrains Mono 作表格 / 数据；Noto Sans JP 作日文点缀。
- 花瓣簇色块标记（4–5 个重叠的正圆）作招牌装饰元素。
- 对角多色飘带（5 条叠放的彩色条，-22° 或 +22°）作氛围分层。
- 32 角星芒封印（`{components.rosette-seal}`）与红色矩形印章（`{components.red-stamp}`）作权威标记。
- 硬边偏移阴影：引文标注上 8px 8px 0 ink，任何地方无模糊、无柔和投影。
- 目录产品卡带彩色顶条 + 名称 + 描述 + 虚线 + 等宽规格行。
- 均衡器条形图，每列叠 6 块瓦片，"亮"段像 VU 表一样从底部往上叠。
- 每张内容页右下角有 JetBrains Mono 页码。

## 颜色

### 调色板
- **纸**（`{colors.paper}` — #F1E6CB）：暖奶油画布。每页默认表面。比常见米白略深略暖，给文稿印刷纸的暖意。
- **深纸**（`{colors.paper-dk}` — #E5D6B0）：画布略深的色调兄弟。用于分层表面、半区背景，以及某一纸区需要读作坐在另一区之下时。
- **墨**（`{colors.ink}` — #3A2516）：深暖棕墨。结构色，全部正文、全部边框、全部分隔、全部硬边偏移阴影色、全部封印填充、全部顶条线。略偏冷的棕而非纯黑，好作为暖墨落在暖纸上。
- **红**（`{colors.red}` — #E5392A）：主强调色与印章色。用于 Big Shoulders 展示标题内的行内 `em` 强调、红色矩形印章、第一张卡的目录卡顶条、数据页的英雄数字，以及飘带第一色。
- **粉**（`{colors.pink}` — #E54489）：明亮洋红粉。用作封面英雄锁定的锁定条背景、飘带色、第二变体的卡片顶条色、小片背景。
- **橙**（`{colors.orange}` — #F09131）：暖落日橙。用作花瓣色、飘带色、第三变体的卡片顶条色、小片背景。
- **黄**（`{colors.yellow}` — #F0BC2A）：芥末暖黄。用作花瓣色、飘带色。预留作分类型强调。
- **绿**（`{colors.green}` — #3D9F47）：中等草绿。用作花瓣色、飘带色、小片背景、均衡器条色。
- **蓝**（`{colors.blue}` — #3F8BC4）：暖中蓝。用作花瓣色、飘带色、第四变体的卡片顶条色、小片背景，以及主红统计需要配对时的第二英雄统计色。

### 默认值
- **默认表面背景**：`{colors.paper}`，每页都在暖奶油纸上开场。
- **默认标题色**：`{colors.ink}`，展示标题是暖棕墨，不是红或别的强调。红只作为墨色标题内的行内 `em` 强调出现。
- **默认正文色**：`{colors.ink}`。
- **默认边框色**：`{colors.ink}`，每条结构边框都是暖棕墨，无例外。
- **默认表格 / 等宽文字色**：`{colors.ink}`。等宽行偶尔在关键标签上用 `opacity: 0.7` 求视觉层级。
- **默认强调色（展示标题内的行内 `em`）**：正文与目录跨页用 `{colors.red}`；正文的色彩故事里已经含红时，引文跨页用 `{colors.blue}`。
- **默认英雄数字色**：`{colors.red}`，数据页大统计是红。两个统计同现时配 `{colors.blue}` 作第二统计。
- **默认印章色**：`{colors.red}` 背景配 `{colors.paper}` 文字，用于每个红色矩形印章。
- **默认封印色**：`{colors.ink}` 背景配 `{colors.paper}` 文字，用于每个星芒封印。
- **`{colors.red}`、`{colors.pink}`、`{colors.orange}`、`{colors.green}`、`{colors.blue}` 表面上默认文字色**：`{colors.paper}`（奶油），系统里唯一的颜色反转。
- **`{colors.ink}` 表面上默认文字色**：反色时用 `{colors.paper}`（奶油）。
- **默认小片调色板顺序**（账表 / 表格里的分类型小片）：红 → 粉 → 橙 → 蓝 → 绿。

六种主色**没有固定语义**（红不表"危险"、绿不表"成功"）。它们充当分类型强调集，挑最适合构图的颜色即可。例外是 `{colors.red}` 作强调：它带冷色没有的"注意"语域，所以预留给行内 `em` 与最强调的英雄数字。

## 排印

### 字族
系统有四款 Google Fonts，各有分明的功能角色：

- **Big Shoulders Display**（展示）：压缩工业无衬线，字重 700 与 900。用于每个展示瞬间，标题、陈述、英雄数字、品牌锁定、卡片名、封印文字、印章文字、账表行标题。始终配负字距（-0.012em 到 -0.025em）。它高窄的压缩字形就是整套系统的视觉身份。
- **Albert Sans**（正文）：干净的现代人文无衬线，字重 400、500、600、700。用于正文段（400）、描述（400）、加字距全大写微标签（700）、强调正文（600–700）。是 Big Shoulders 表现力的中性对位。
- **JetBrains Mono**（数据）：等宽，字重 400、500。用于产品卡里的规格行、账表里的日期标签、页码、均衡器刻度标签、小片文字、导航提示、元数据标记。一切读作"数据"而非"编辑"的瞬间。
- **Noto Sans JP**（文化点缀）：日文无衬线，字重 500、700。省着用于嵌在封面页脚与品牌标记里的日文字符（限定版、漢字、平仮名）。提供松本工坊的文化语域。

斜体不存在。下划线不存在。强调靠行内 `<em>`（换色到红或蓝，不带斜体样式）、靠字重（Albert Sans 400 → 700）、或靠换字面（Albert Sans 正文 → Big Shoulders 展示）达成。

### 排印比例

| Token | 尺寸（clamp） | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.disp-hero}` | 120–280px | Big Shoulders Display | 900 | 封面跨页的英雄数字 |
| `{typography.disp-title}` | 80–180px | Big Shoulders Display | 900 | 版权页 / 收尾跨页的超大标题 |
| `{typography.disp-statement}` | 70–168px | Big Shoulders Display | 900 | 宣言 / 单句陈述跨页 |
| `{typography.disp-lockup}` | 56–130px | Big Shoulders Display | 900 | 封面品牌锁定条 |
| `{typography.disp-quote-lg}` | 56–130px | Big Shoulders Display | 900 | 大号引文 |
| `{typography.disp-section}` | 52–100px | Big Shoulders Display | 900 | 分节顶条标题 |
| `{typography.disp-quote}` | 48–110px | Big Shoulders Display | 900 | 标准引文 |
| `{typography.disp-brand}` | 32–56px | Big Shoulders Display | 900 | 品牌子标记或字标 |
| `{typography.disp-card-name}` | 28–48px | Big Shoulders Display | 900 | 产品卡名称 |
| `{typography.num-hero}` | 110–240px | Big Shoulders Display | 900 | 主英雄统计 |
| `{typography.num-md}` | 70–150px | Big Shoulders Display | 900 | 次级统计 |
| `{typography.ttl-row}` | 22–30px | Big Shoulders Display | 700 | 账表行标题 |
| `{typography.body-emphasis}` | 15–20px | Albert Sans | 600 | 导语段或强调正文 |
| `{typography.body}` | 14–17px | Albert Sans | 400 | 标准段落正文 |
| `{typography.body-md}` | 14–15px | Albert Sans | 400 | 卡内紧凑正文 |
| `{typography.micro-spec}` | 14–20px | Albert Sans | 700 | 规格清单标签（略加字距） |
| `{typography.micro-xl}` | 12–14px | Albert Sans | 700 | 最松的加字距全大写微标签（0.32em） |
| `{typography.micro-lg}` | 12–14px | Albert Sans | 700 | 加字距全大写 eyebrow 标签（0.2em） |
| `{typography.micro}` | 12–14px | Albert Sans | 700 | 标准加字距全大写微标签（0.16em） |
| `{typography.mono-md}` | 14–16px | JetBrains Mono | 400 | 表格日期或数值 |
| `{typography.mono}` | 11–12px | JetBrains Mono | 400 | 规格行、页码、均衡器刻度 |
| `{typography.mono-tag}` | 12–14px | JetBrains Mono | 400 | 小片标签文字 |
| `{typography.stamp-text}` | 20–28px | Big Shoulders Display | 900 | 红色矩形印章文字 |
| `{typography.seal-text}` | 22–38px | Big Shoulders Display | 900 | 星芒封印文字 |
| `{typography.jp}` | inherit | Noto Sans JP | 500 | 日文字符点缀 |

### 默认值
- **主分节标题默认尺寸（顶条语境）**：`{colors.ink}` 的 `{typography.disp-section}`（52–100px clamp）。
- **宣言 / 居中陈述跨页默认尺寸**：`{colors.ink}` 的 `{typography.disp-statement}`（70–168px clamp），可选 `<em>` 换色。
- **段落正文默认尺寸**：`{typography.body}`（14–17px clamp）。
- **加字距全大写微标签或 eyebrow 默认尺寸**：`{colors.ink}` 的 `{typography.micro}`（12–14px Albert Sans 字重 700、0.16em 字距、全大写）。
- **英雄统计默认尺寸**：`{colors.red}` 的 `{typography.num-hero}`（110–240px clamp）。
- **表格日期或等宽数值默认尺寸**：`{colors.ink}` 的 `{typography.mono-md}`（14–16px）。
- **页码默认尺寸**：`{colors.ink}` 的 `{typography.mono}`（11–12px）。
- **任何 Big Shoulders Display 元素默认字重**：900（700 预留给 `{typography.ttl-row}`，账表行标题，系统里唯一的次级展示瞬间）。
- **正文默认字重**：400；微标签：700；强调正文：600–700。

主导文字在 `{typography.disp-section}` 与 `{typography.disp-statement}` 间拿不准时，页带顶条 / 正文网格就选 `{typography.disp-section}`，页专给单条居中陈述就选 `{typography.disp-statement}`。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个 Big Shoulders Display 元素都带负字距**（-0.012em 到 -0.025em）。Big Shoulders 用默认字距读作未处理，负字距才给展示文字压缩的目录封面密度。
- **每个微标签都全大写配显著字距**（按语境 0.16em、0.18em、0.2em 或 0.32em）。没有全大写 + 字距的微标签读作正文碎片，不像标签。
- **每个页码都用 JetBrains Mono**，格式 `NN / TT`。页码在每张内容页上不可省略，住在右下。
- **Big Shoulders 展示标题里的每个行内 `<em>` 都换色**到 `{colors.red}`（默认）或 `{colors.blue}`（红已过载的引文跨页）。绝不用斜体样式，换色就是整个强调装置。
- **每条规格行都用 JetBrains Mono。** 用 Albert Sans 排的规格行读作正文句，不像目录数据。
- **每个星芒封印都用 32 角 clip-path 多边形**，`{colors.ink}` 填充、`{colors.paper}` 文字。改动角数或简化（如 8 角、16 角芒）会破掉封印辨识信号。
- **每个红色印章都用 `{colors.red}` 背景配 `{colors.paper}` 文字**与 Big Shoulders 900。印章文字始终全大写、始终配正字距（0.02em）。

### 排印原则
系统的排印节奏来自**字面对字面的反差**：Big Shoulders 展示（响、压缩、墨）→ Albert Sans 正文（静、中性、句式）→ JetBrains Mono 数据（机械、表格、定宽）→ Noto Sans JP（文化标点）。只用一款字面的页读作扁平，把 Big Shoulders + Albert Sans + JetBrains Mono 一起用的页读作目录式正确。

行高：展示紧（0.84–0.94）、正文宽（1.4–1.5）、微标签与等宽紧（1.0–1.3）。倒置会破掉节奏。

## 布局

### 画布系统
系统以 `100vw × 100vh` 为目标。文稿包在 `.deck` 网格里，居中一个铺满视口的 `.stage`。每张 `.slide` 绝对定位 inset 0、opacity 0，只有 `.active` 页 opacity 1。过渡是 280ms ease 的 opacity 淡入。导航由 JS 驱动，方向键、空格、PageUp/Down、Home/End、触屏滑动。

### 画框内缩式样
多数内容页遵循画框内缩式样：一个 `.frame` div 距页边在上 / 左 / 右内缩 `clamp(36px, 3.6vw, 72px)`、在底部内缩 `clamp(72px, 7vh, 110px)`（给页码让位）。画框内，顶条式样（标题 + 元数据标签 + 1.5px 墨线）坐在正文区上方。

封面、宣言、引文跨页打破画框式样，它们把花瓣、飘带、英雄数字、锁定自由叠在画布上，不用顶条 / 正文网格。

### 内边距比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.frame-inset}` | 36–72px | 画框距页边内缩 |
| `{spacing.frame-inset-bottom}` | 72–110px | 画框底部内缩（给页码让位） |
| `{spacing.topbar-gap}` | 12–22px | 顶条下内边距与分节间隙 |
| `{spacing.grid-gap}` | 16–26px | 卡片网格单元间隙 |
| `{spacing.col-gap}` | 28–56px | 双栏正文间隙 |
| `{spacing.card-pad-x}` / `{spacing.card-pad-y}` | 14–20px / 16–24px | 产品卡正文内边距 |
| `{spacing.pagenum-inset}` | 20–36px / 24–44px | 页码距右下内缩 |

### 常驻外壳
两个常驻元素：
- **页码**：每张内容页右下，JetBrains Mono 11–13px `NN / TT` 格式。
- **导航提示**：固定在左下，JetBrains Mono 10–12px 文字 `← / → · space`，0.36 不透明度。

页码属于每张页的构图（不是全局叠层），导航提示是单个全局元素。

## 纵深与层级

### 硬边偏移阴影（主手法）
系统在墨色上用**硬边偏移阴影**，恰好一个值：`8px 8px 0 {colors.ink}`（零模糊、实墨）。施于 qbody-box（引文标注）与其他需要从繁忙底层构图上抬起的"纸压飘带"元素。阴影很少用，多数卡片与面板只靠边框定义，8px 墨阴影留给配得上它的瞬间。

### 纸张颗粒纹理（氛围层）
`{components.paper-texture}` 半调网点图案以 16% 不透明度盖在每页上。严格说这不是纵深，而是让每块平色块读作纸上墨的基础纹理底。去掉它会立刻破掉印刷语域。每页必需。

### 色块分层
纵深主要来自**分层彩色区域**：英雄数字背后的飘带、品牌锁定背后的花瓣、纸卡顶上的顶条色片、对角飘带上的红印章。高反差强调在暖奶油底上往前凸，是系统的主纵深语法。

### 边框定义
多数卡片与面板靠 1.5px 墨边框定义，不靠阴影。同纸色背景上的纸卡周围一道 1.5px 墨边框，单靠边界就读作抬升。

### 无柔和阴影
系统用**零模糊 `box-shadow`**（除 qbody-box 上唯一那道 8px 硬偏移外）、零 `drop-shadow` 滤镜、零 rgba 着色阴影。任何元素上的现代柔阴影都会破掉印刷目录美学。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 0px | 全部卡片、全部印章、全部顶条、全部正文、全部小片、全部账表行 |
| 50% | 花瓣（正圆），仅用于花瓣簇内与散落色块 |
| 多边形 clip-path（32 角星芒） | 花结封印，唯一的复杂形状基元 |

系统除正圆（花瓣）与多边形裁切的星芒（封印）外**没有圆角半径**。其余每个形状都是严格矩形或方形。

### 边框粗细
- **1.5px 实 `{colors.ink}`**：卡片、顶条线、账表头线、qbody-box、封面画框底线、封面页脚顶线的标准边框粗细。
- **2px 实 `{colors.ink}`**：用于规格清单复选框边框。
- **1px 实 `{colors.ink}`**：用于均衡器内刻度 / 标签分隔。
- **1px 实 rgba(58,37,22, 0.22)**：用作账表正文行细线分隔与均衡器段"灭"态边框。
- **1px 虚线 `{colors.ink}`**：用作分隔产品卡描述与等宽规格行的虚线。

边框始终是墨（暖棕）。本系统里不存在彩色边框，除了小片隐含的背景边框。

### 装饰元素类型

**花瓣簇（`{components.petals-cluster}`）**：一个定界容器，装 4–5 个重叠的正圆彩色色块。每片花瓣以百分比偏移绝对定位在容器内。颜色在主调色板间轮换（红、粉、橙、黄、绿、蓝），绝不全同色。用作页角的品牌标记锚点与引文跨页的装饰纹样。招牌装饰元素。

**飘带（`{components.ribbon-band}`）**：5 条实色水平条叠放，旋转 -22° 或 +22°，斜扫过一片区域。条纵向叠放，每条飘带用不同的 `top` 百分比，造出平行射线效果。锚在页的一边、放大到从对边溢出。系统的氛围分层招牌。

**花结封印（`{components.rosette-seal}`）**：32 角星芒 clip-path 形状，`{colors.ink}` 填充配奶油文字。承载一个 1–4 字符字形：年份数字（"26"）、卷号（"VOL 26"）、或 2–3 字母缩写。用作封面与收尾版权页上的权威标记。

**红色矩形印章（`{components.red-stamp}`）**：红矩形，奶油文字，可选 -3° 旋转。用于状态徽章（COMPLETE、AS SEEN ON）与产品标注。始终 Big Shoulders 900 全大写。

**产品卡（`{components.card-product}`）**：竖卡，1.5px 墨边框、一条彩色顶条（红 / 粉 / 橙 / 蓝变体），以及叠放的正文：Big Shoulders 900 卡名 → Albert Sans 400 描述 → 虚线 → 等宽规格行。目录网格的主单元。

**卡片顶条（`{components.card-topstrip}`）**：18–32px 高实色带，横贯产品卡顶部全宽。读作 Pantone 色片，在网格里标出卡片的变体。

**规格清单（`{components.spec-checklist}`）**：`nb-checkbox` + 加字距全大写标签行的竖列。每行有一个 14–20px 墨边框方框（填或空，填态显示奶油 `×` 字形），后跟一条全大写加字距标签。

**账表行（`{components.ledger-row}`）**：5 列表格行式样，日期（等宽）| 标题（Big Shoulders 700）| 版次（Albert Sans）| 小片 | nr 指示（方框）。表头行用 1.5px 墨底边，正文行用 1px 墨-alpha 细线分隔。

**小片（`{components.chip}`）**：等宽字体色块，标账表行类别。背景取主调色板（红、粉、橙、蓝、绿）。始终奶油文字。

**顶条线（`{components.topbar-rule}`）**：分节头下划线式样，左侧标题（展示）与右侧加字距全大写元数据标签对齐末端，由 1.5px 墨线与正文隔开。

**均衡器条形图（`{components.bar-eq}`）**：8 列网格，每列叠 6 块等高瓦片（段）。`column-reverse` flex 方向意味着源码顺序里第一段坐在底部，"亮"段像 VU 表一样从底部往上叠。亮段颜色按列设定（红、粉、橙、黄、绿或蓝），灭段是半透明墨调。

**Qbody-box（`{components.qbody-box}`）**：引文标注容器，1.5px 墨边框、8px 硬墨阴影。坐在对角飘带之上。

**品牌锁定**：Big Shoulders 900 字标压 Albert Sans 600 子标记，绝对定位在封面花瓣附近。

## 该做与不该做

### 该做
- 每页保留纸张颗粒半调网点纹理（`{components.paper-texture}`）于 16% 不透明度。它是基础印刷语域，去掉会让文稿看着像扁平网页模板。
- 每个展示瞬间都用 Big Shoulders Display 字重 900 配负字距（-0.012em 到 -0.025em）。
- 给每个微标签套加字距全大写，标准 0.16em、eyebrow 0.2em、最松的宣言眉题 0.32em。默认字距读作正文句。
- 英雄统计设 `{colors.red}` 的 Big Shoulders 900。第二统计配 `{colors.blue}`。
- 展示标题里用行内 `<em>` 换色（默认红，引文跨页蓝）。绝不斜体。
- 把花瓣簇色块标记（4–5 个重叠正圆、主色混用）构造成页角的装饰锚点。
- 在封面与收尾跨页把对角多色飘带（-22° 或 +22°）扫在英雄内容背后作氛围分层。
- 每张内容页右下放 JetBrains Mono 页码（`NN / TT` 格式）。
- 规格行、日期、小片、任何表格数据都用 JetBrains Mono，一切该读作"数据"而非"编辑"的东西。
- 把 32 角星芒封印与红色矩形印章留给权威瞬间（封面、版权页、产品标注）。它们是招牌标记，滥用会稀释。

### 不该做
- 不要给任何角加圆角。卡片、印章、小片、顶条，全是严格矩形。花瓣（圆）与星芒封印（多边形 clip-path）是仅有的非矩形形状。
- 不要用模糊 `box-shadow`。系统里唯一的阴影是引文标注上的 8px 硬墨偏移。现代柔阴影会破掉印刷语域。
- 不要把 Big Shoulders Display 换成别的展示字面。压缩工业 900 声部就是整套系统身份。
- 不要把 JetBrains Mono 换成别的等宽字面。表格声部属于目录设定。
- 不要用 Big Shoulders Display 排正文段。小正文尺寸下它读作用力过猛。
- 不要用 Albert Sans 做展示瞬间。Albert Sans 是中性正文字面，展示瞬间需要 Big Shoulders。
- 不要用斜体强调。用换红或蓝的行内 `<em>`，或换字重（Albert 400 → 700）。
- 不要引入第七种主色。调色板锁在红 / 粉 / 橙 / 黄 / 绿 / 蓝。加紫、青或别的色相会破掉目录色彩故事。
- 不要用饱和强调色填卡片边框（红边框、蓝边框）。边框始终是墨。
- 不要在内容页上省掉页码。它是不可省略的编辑信号。

## 响应式行为

系统以 `100vw × 100vh` 为目标、通篇用 `clamp()`，配 `min(Xvw, Yvh)` 式样把视口宽与视口高约束合起来。这带来桌面尺寸间的流式缩放，无需响应式断点。没有定义移动端断点，文稿以演示为先。

### 缩放行为
- 展示标题经 `min(Xvw, Yvh)` 缩放，视口变矮时也会缩小，不只是变窄时。
- 正文、等宽、微标签按视口宽度在各自 clamp 区间内缩放。
- 花瓣、飘带、封印、印章用 `vw`/`vmin` 单位，随画布成比例缩放。
- 4px 纸张颗粒纹理周期固定，与视口无关。

### 放映行为
- `ArrowRight`、`PageDown`、`Space` 前进。
- `ArrowLeft`、`PageUp` 后退。
- `Home` 跳到首页，`End` 跳到末页。
- 横向触屏滑动前进 / 后退。
- 激活页带 `.active` 类，非激活页 opacity 0。

### 打印行为
没有定义 `@media print` 规则。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁 | 中文 | 字重映射 |
|---|---|---|---|
| 展示 / 标题 / 陈述 / 英雄数字 / 卡名 / 封印 / 印章 / 锁定 | Big Shoulders Display（900） | **站酷小薇体 ZCOOL XiaoWei** | regular（单字重） |
| 正文 / 正文-md / 强调正文 / 微标签 | Albert Sans（400 / 600 / 700） | **霞鹜文楷 LXGW WenKai** | regular |
| 表格 / 规格行 / 小片 / 页码 / 等宽标签 | JetBrains Mono（400 / 500） | **霞鹜文楷 LXGW WenKai**（或规格行保留纯拉丁等宽） | regular |
| 日文点缀 | Noto Sans JP | *（不变）* | 500 / 700 |

### 混排策略

**策略 A：展示 CJK + 正文 CJK，各有各的性格。** 卡带包装美学是女性化花卉配工业纪律，中文搭配该同时敬重这两半。**ZCOOL XiaoWei（站酷小薇体）** 是优雅的压缩展示字面，笔画对比精致，既呼应 Big Shoulders Display 的压缩竖向感，又带更柔、更分明的女性声部，贴合花瓣簇装饰系统。**LXGW WenKai（霞鹜文楷）** 是暖楷书风正文字面，基于 Fontworks Klee，带友好的手工甄选气质，贴合 Albert Sans 作正文声部的角色，在暖奶油纸上的小尺寸下读起来很美。两款 CJK 字面合起来保住拉丁系统"工业展示 + 暖正文"的节奏，又把中文文稿落在一个分明手工甄选、略女性化的语域里，正合 Sakura Chroma 的名字与花卉母题。

### 加载

```html
<link href="https://chinese-fonts-cdn.deno.dev/packages/zcool-xiaowei/dist/ZCOOLXiaoWei-Regular/result.css" rel="stylesheet">
<link href="https://chinese-fonts-cdn.deno.dev/packages/lxgwwenkai/dist/LXGWWenKai-Regular/result.css" rel="stylesheet">
```

然后把 CJK 字族追加到相应字体栈：
```css
/* Display roles */
font-family: 'Big Shoulders Display', 'ZCOOL XiaoWei', sans-serif;
/* Body / micro roles */
font-family: 'Albert Sans', 'LXGW WenKai', sans-serif;
/* Mono roles (if used for CJK content) */
font-family: 'JetBrains Mono', 'LXGW WenKai', ui-monospace, monospace;
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

- **Big Shoulders 展示上的负字距（-0.012em 到 -0.025em）在 CJK 上必须降到 0**。ZCOOL XiaoWei 本就是压缩字面，负字距会让字撞字。
- **加字距全大写微标签（0.16em、0.2em、0.32em）没有 CJK 对应。** CJK 微标签把字距降到 0，让暖棕墨色 + 粗字重承担分类型标签信号。一条 "限定版 LIMITED EDITION" eyebrow 可在同一标签里混 CJK + 拉丁，汉字字距保持 0，拉丁给 0.16em+。
- **行内 `<em>` 换色（到红或蓝）在 CJK 里同样成立**，颜色强调与字形无关，落在 ZCOOL XiaoWei 展示标题上很漂亮。
- **花瓣簇、飘带、星芒封印、红色矩形印章都与字形无关**，它们在中文内容背后同样扛得住系统的工业目录声部。
- **承载 2–4 字符字形的 32 角星芒封印**，配单个汉字（限、新、季）、以 `{colors.paper}` 奶油的 ZCOOL XiaoWei 呈现时格外出彩。粗展示字重让中心字形读作制作者标记。
- **JetBrains Mono 规格行是最难的决定**：纯拉丁规格行（`44.1 KHZ`、`LP / 33⅓`）保住目录设定，本地化到 LXGW WenKai 的规格行（`立体声`、`限定版`）读作中国市场目录却丢了技术规格声部。正确做法是**混语规格行，拉丁数值保持等宽，中文描述词行内切到 LXGW WenKai**。
- **Noto Sans JP 点缀（限定版）保持不变**，日文字符在许多情况下与简体中文共享字形，但 Noto Sans JP 渲染是刻意的（日版情调）。在以中文为主的文稿上，把这些字符换成 LXGW WenKai，让它们读作中文而非日文借字。

### 已知 CJK 缺口

ZCOOL XiaoWei 是单字重字面，没有 900 等价。定义拉丁展示声部的 Big Shoulders 900 响度无法精确匹配。补偿办法是把 CJK 展示留给欢迎柔和优雅的瞬间（封面跨页、引文页），而非需要纯粹粗野分量的地方（英雄统计）。英雄数字保留拉丁数字的 Big Shoulders 900，中文数字（一二三四）本就不承载目录封面的统计声部。

## 迭代指南

1. 每张新内容页都带纸张颗粒半调网点纹理、一个画框内缩区（距边 36–72px、距底 72–110px）、以及右下角页码。
2. 任何遵循画框式样的新内容页都以顶条开场：左侧 display-section 标题、右侧加字距全大写元数据标签，由 1.5px 墨线与正文隔开。
3. 任何新标题都用 Big Shoulders Display 字重 900 配负字距。分节顶条用 `{typography.disp-section}`，单句陈述跨页用 `{typography.disp-statement}`，英雄数字用红色的 `{typography.num-hero}`。
4. 任何新正文都用 Albert Sans 400，加字距全大写标签用 Albert Sans 700 全大写、0.16–0.32em 字距，表格内容用 JetBrains Mono 400。
5. 任何新卡片都用 1.5px 墨边框、可选彩色顶条（红 / 粉 / 橙 / 蓝），以及展示名 → Albert 正文 → 虚线 → 等宽规格行的正文式样。
6. 任何新账表 / 表格式样都用 5 列 ledger-row 网格，表头下划线 1.5px 墨、正文细线分隔 1px 墨-alpha。分类型标签用主调色板背景的等宽小片。
7. 任何新装饰锚点都用花瓣簇（4–5 个混主色的重叠正圆花瓣）。避开椭圆，花瓣始终是正圆。
8. 任何新权威标记都用 32 角星芒封印（墨填充、奶油文字）或红色矩形印章。封印正式，印章有劲。
9. 展示标题内的任何行内强调都用换色到 `{colors.red}`（默认）或 `{colors.blue}`（红过载时）的 `<em>`。绝不斜体。
10. 氛围分层，即英雄内容背后 -22° 或 +22° 的对角飘带，出现在封面、收尾、条纹跨页瞬间。它不是常规页元素，留给配得上氛围野心的跨页。

## 已知缺口

- 系统加载四款 Google Fonts（Big Shoulders Display、Albert Sans、JetBrains Mono、Noto Sans JP）。Big Shoulders 多字重（500、700、800、900），系统用 700 与 900。生产环境建议自托管。
- 纸张颗粒纹理是 CSS 径向渐变（不是 SVG 噪声滤镜），因此跨浏览器确定地平铺且性能好。网点周期（4px）固定，不随视口缩放。
- 32 角星芒 clip-path 多边形是硬编码的，改封印形状要重写多边形点列。系统之所以一致，只因处处复用同一个多边形，换成别的星芒多边形会破掉视觉凝聚。
- 对角飘带用 `transform: rotate(-22deg)` 与超宽宽度（160%）从页边溢出。视口很高时，飘带覆盖可能显得比标准 16:9 视口薄。
- 均衡器条形图用 `display: flex; flex-direction: column-reverse;` 把亮段从底部往上叠。这是个细微布局式样，在激进覆盖下可能脆弱，改动 eq 段时必须保住 column-reverse 行为。
- 英雄统计用行内 `<sub>` 与行内样式 `font-size` 覆盖做子单位（`26K`、`61%`），绕过了排印 token 系统。新统计应沿同一式样：超大数字 + 墨色、约为数字尺寸 34% 的较小行内单位。
- Noto Sans JP 有加载但只用了一次（封面页脚的 限定版 "limited edition"）。文稿无日文内容时，这次字体加载是没用上的负担，非日文稿可考虑去掉该 import。
- 左下导航提示不透明度很低（0.36），在默认放映亮度下可能难看见。它本意是氛围外壳，不是醒目的操作提示。
