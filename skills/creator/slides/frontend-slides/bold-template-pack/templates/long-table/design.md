---
version: alpha
name: Long Table
description: A warm, single-ink editorial system in the register of a supper-club poster, a small-batch zine, or a Risograph-printed program. The entire system runs in one ink color — a warm rust terracotta (#B53D2A) — on a buttery cream paper ground (#FAF1E2), with a subtle 4px radial-dot texture overlay giving the surface its "printed paper" quality. Display type runs in Bricolage Grotesque at weight 700–800 in uppercase; body and metadata run in Fraunces serif at weight 400–600 with optical-size axis engaged. Pill buttons, outlined edition badges, italic-edition numerals, and dashed/solid 1.5px borders complete the printed-program vocabulary.

colors:
  paper: "#FAF1E2"
  paper-d: "#F2E5CF"
  paper-vd: "#E8D7B6"
  ink: "#B53D2A"
  ink-dp: "#8E2D1F"
  rule: "#B53D2A"
  ink-32: "rgba(181, 61, 42, 0.32)"
  ink-78: "rgba(181, 61, 42, 0.78)"
  ink-50: "rgba(181, 61, 42, 0.5)"

color-aliases:
  rule: ink
  ink-32-canonical: "Same ink #B53D2A at 32% opacity, used for dashed dividers and subtle internal rules"
  ink-78-canonical: "Same ink #B53D2A at 78% opacity, used for de-emphasized metadata"

typography:
  display-jumbo-numeral:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(180px, min(22vw, 38vh), 480px)"
    fontWeight: 400
    lineHeight: 0.86
    letterSpacing: -0.02em
    fontStyle: italic
  display-cover:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(82px, min(8.8vw, 15vh), 180px)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: -0.012em
    textTransform: uppercase
  display:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(72px, min(7.6vw, 13vh), 160px)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.012em
    textTransform: uppercase
  headline-xl:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(60px, min(6.4vw, 10.5vh), 140px)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.012em
    textTransform: uppercase
  headline:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(56px, min(6vw, 10vh), 120px)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.012em
    textTransform: uppercase
  headline-md:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(48px, min(5vw, 8.4vh), 100px)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: -0.012em
    textTransform: uppercase
  quote:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(40px, min(4.4vw, 7.4vh), 96px)"
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -0.012em
    textTransform: uppercase
  card-title:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(28px, 2.4vw, 44px)"
    fontWeight: 800
    lineHeight: 0.95
    letterSpacing: -0.008em
    textTransform: uppercase
  course-name:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(20px, 1.5vw, 28px)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.005em
    textTransform: uppercase
  info-value:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(20px, 1.6vw, 28px)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.005em
    textTransform: uppercase
  edition-label-tracked:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(15px, 1.1vw, 18px)"
    fontWeight: 700
    letterSpacing: 0.18em
    textTransform: uppercase
  who-tag:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(15px, 1.05vw, 18px)"
    fontWeight: 700
    letterSpacing: -0.005em
    textTransform: uppercase
  body-serif-italic-lg:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(20px, 1.5vw, 28px)"
    fontWeight: 400
    lineHeight: 1.45
    fontStyle: italic
  body-serif-italic:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(17px, 1.2vw, 22px)"
    fontWeight: 400
    lineHeight: 1.5
    fontStyle: italic
  body-roman:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(15px, 1vw, 17px)"
    fontWeight: 400
    lineHeight: 1.45
  edition-label:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(20px, 1.6vw, 30px)"
    fontWeight: 400
    lineHeight: 1
    fontStyle: italic
  tagline:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(18px, 1.4vw, 26px)"
    fontWeight: 400
    lineHeight: 1.35
    fontStyle: italic
  stats:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(17px, 1.2vw, 22px)"
    fontWeight: 400
    lineHeight: 1.4
    fontStyle: italic
  pill-text:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(15px, 1.1vw, 20px)"
    fontWeight: 400
    lineHeight: 1
    fontStyle: italic
  meta-tag:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(14px, 0.95vw, 16px)"
    fontWeight: 400
    lineHeight: 1.4
    fontStyle: italic
  info-key:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(14px, 0.95vw, 16px)"
    fontWeight: 400
    letterSpacing: 0.16em
    textTransform: uppercase
    fontStyle: italic
  pagenum:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(14px, 0.95vw, 16px)"
    fontWeight: 400
    letterSpacing: 0.02em
    fontStyle: italic
  nav-hint:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(11px, 0.78vw, 13px)"
    fontWeight: 400
    letterSpacing: 0.02em
    fontStyle: italic

spacing:
  slide-pad-h-default: "clamp(60px, 5vw, 110px)"
  slide-pad-h-wide: "clamp(80px, 7vw, 160px)"
  slide-pad-h-narrow: "clamp(120px, 12vw, 280px)"
  slide-pad-top-default: "clamp(96px, 10vh, 160px)"
  slide-pad-top-cover: "clamp(60px, 6vh, 100px)"
  slide-pad-bottom-default: "clamp(110px, 11vh, 170px)"
  slide-pad-bottom-wide: "clamp(150px, 14vh, 220px)"
  gap-section: "clamp(28px, 3vh, 50px)"
  gap-content: "clamp(18px, 2vh, 32px)"
  gap-row: "clamp(14px, 1.6vh, 24px)"
  gap-tight: "clamp(10px, 1.2vh, 18px)"
  border-weight: "1.5px"
  rule-dashed-color: "{colors.ink-32}"

canvas:
  width: 100vw
  height: 100vh

components:
  pill:
    description: "Outlined rounded-rectangle (border-radius 999px → fully pill) holding short italic Fraunces text. The system's CTA / action button. Border is 1.5px solid {colors.ink}; padding is generous (~12px / 28px); text-color is {colors.ink}."
    border: "1.5px solid {colors.ink}"
    borderRadius: "999px"
    padding: "clamp(8px, 1vh, 14px) clamp(20px, 2vw, 32px)"
    typography: "{typography.pill-text}"
  pill-divider:
    typography: "{typography.pill-text}"
    opacity: 0.7
    description: "A small italic Fraunces divider character (typically · or /) used inline between adjacent pills."
  ed-badge:
    description: "A small circular outlined badge (~38px) holding a single italic Fraunces digit. The edition / chapter ordinal marker. Border is 1.5px solid {colors.ink}; background is transparent."
    width: "clamp(34px, 2.6vw, 44px)"
    height: "clamp(34px, 2.6vw, 44px)"
    border: "1.5px solid {colors.ink}"
    borderRadius: "50%"
  rect-tag:
    description: "Outlined rectangular tag — like the pill but with sharp corners. Holds short italic Fraunces text. Used as a category / status / metadata chip when the pill's roundness isn't appropriate."
    border: "1.5px solid {colors.ink}"
    padding: "clamp(7px, 0.9vh, 12px) clamp(14px, 1.4vw, 22px)"
    typography: "{typography.pill-text}"
  card-outlined:
    description: "A 1.5px ink-outlined rectangular content card. Holds a card-top metadata row (separated below by a 1px @ 32%-opacity rule), a Bricolage card-name, a Fraunces body description, and a meta-row at the bottom (separated above by a 1px dashed @ 32%-opacity rule). The system's primary content card pattern."
    border: "1.5px solid {colors.ink}"
    padding: "clamp(20px, 2vh, 32px) clamp(20px, 1.8vw, 30px)"
    internalDivider-solid: "1px solid {colors.ink-32}"
    internalDivider-dashed: "1px dashed {colors.ink-32}"
  paper-texture:
    description: "Subtle radial-dot texture overlay on the stage. A 4px-tile background-image of 0.5px radial-gradient dots in {colors.ink-50} at 10% opacity. Sits absolutely on the stage with pointer-events disabled, giving the paper its Risograph / printed-stock quality. This is on every slide."
    backgroundImage: "radial-gradient(circle at 1px 1px, {colors.ink-50} 0.5px, transparent 1px)"
    backgroundSize: "4px 4px"
    opacity: 0.1
  topbar-divider:
    description: "A 1.5px ink solid border-bottom under a slide topbar (where a Bricolage headline sits beside a small Fraunces label). The horizontal rule beneath the topbar is the system's universal page-divider device."
    borderBottom: "1.5px solid {colors.ink}"
  pagenum:
    position: "absolute"
    placement: "right: clamp(36px, 3.6vw, 80px); bottom: clamp(40px, 4vh, 64px)"
    typography: "{typography.pagenum}"
    color: "{colors.ink}"
    description: "Italic Fraunces page number at the bottom-right of every slide."
  nav-hint:
    position: "fixed"
    placement: "left: clamp(36px, 3.6vw, 80px); bottom: clamp(40px, 4vh, 64px)"
    typography: "{typography.nav-hint}"
    color: "{colors.ink}"
    opacity: 0.45
    description: "A faint italic Fraunces hint string at the bottom-left of the viewport (e.g. '← → to navigate'). Bonus interactivity affordance."
  ledger-row:
    description: "A horizontal ledger-style row in a calendar/schedule context. Multi-column grid (typical: 80px / 130px / 1.6fr / 0.9fr / auto) with a 1px @ 32%-opacity ink border-bottom. Each cell is a tag, label, or pill. Reads as a guestbook / restaurant-reservation log."
    rowPad: "clamp(11px, 1.3vh, 18px) 0"
    borderBottom: "1px solid {colors.ink-32}"
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/long-table/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Long Table 是一套**单墨编辑系统**，语域落在晚餐俱乐部海报、Risograph zine 或小出版社晚宴节目单。底层前提是单色：系统里每一道可见痕迹（每个标题、每段文字、每条边框、每条线、每片胶囊、每个页码）都以单一暖锈陶土墨（`{colors.ink}` — #B53D2A）渲染在奶油黄纸底（`{colors.paper}` — #FAF1E2）上。唯一的色彩变化是不透明度：同一墨色主痕迹 100%、弱化元数据 78%、内部虚线分隔 32%、纸纹点 10%。

单墨约束是系统的身份。美学借自单色丝网印、凸版海报、Risograph 信笺，这些格式里每多一色就是多一道印刷工序，因此是一个刻意决定。认准一墨，系统取得的是印刷物的安静权威，而非数字表面的抛光感。

招牌的**纸纹叠层**坐在每页上：4px 平铺的径向点图案，50% 不透明度墨色再以 10% 不透明度叠，经 `.stage::before` 伪元素施加。点在交谈距离看不见、凑近才可见，它们给奶油表面"印刷纸"的质感，是设计系统不可少的一部分，不是可选装饰。

排印栈是两字面搭配：

- **Bricolage Grotesque** 字重 700 与 800、**严格大写**承载每个展示瞬间：封面、标题、卡片标题、菜名、引文正文、信息数值、who-tag。Bricolage 是宽而略紧缩的怪诞体，个性强，大写集有手绘海报的冲击力。光学尺寸轴（`opsz` 12..96）已启用。
- **Fraunces** 字重 400–600 承载每段正文、每个元数据字段、每片胶囊、每个页码、每个版次标签。**斜体 Fraunces 是默认正文样式**，倾斜的衬线是系统的正文声部，带来暖意和编辑个性。正体 Fraunces 只出现在特定紧凑场合（信息键、索引卡片内的说明正文）。两种样式的光学尺寸轴（`opsz` 9..144）都已启用。

最大 480px 的**斜体 Fraunces 版次数字**是系统招牌的展示锚点，它取代传统上会填满封面/特写页右半的手绘插图，用与页面其余部分同一墨色的排印中心件给页面定调。

纵深是**平的、印刷的**。没有阴影、没有渐变、没有模糊、没有辉光。抬升完全靠卡片、徽章、胶囊、小片上的 1.5px 实线墨边，32% 不透明度的 1px 实线或虚线内分隔，以及纹理叠层的氛围质感传达。整套系统读起来像墨渗进纸里。

**密度取向：丰富但精心。** Long Table 页面承载实质内容时显得权威：封面有英雄标题 + 标语 + 动作胶囊 + 统计 + 大版次数字，索引页有顶栏标题 + 三张丰富卡片，菜单页有五行菜名 + 说明 + 搭配。页面满但绝不挤，每个区域承载一个聚焦元素、周围有呼吸。只装一个标题的页读起来像"缺了它的节目单"，装 8 个互抢内容块的页读起来像坏了。目标是每页一个主要排印瞬间（Bricolage 展示）锚定 2–4 组辅助组（卡片、胶囊、账目行、信息数值对）。

**关键特征：**
- 一种墨色（`{colors.ink}`，暖锈陶土）压奶油纸（`{colors.paper}`）。不透明度变体是唯一的色彩变化。
- Bricolage Grotesque 字重 700–800 大写用于每个展示瞬间，Fraunces 400–600 默认斜体用于每个正文和元数据瞬间。
- 每页经 `.stage::before` 带微妙的 4px 径向点纸纹，远处不可见、近处可见。
- 胶囊按钮（border-radius 999px）、版次徽章（圆）、方角小片、带描边卡片（1.5px 实线），全是单粗细墨线轮廓、无填充。
- 最大 480px 的斜体 Fraunces 版次数字是封面类页面的英雄排印锚点。
- 1.5px 结构边、32% 不透明度的 1px 实线或虚线内分隔。无更粗的边、无阴影。
- 每页右下角页码（斜体 Fraunces），左下角导航提示（斜体 Fraunces、45% 不透明度）。
- 系统按设计单墨，加任何第二色（海军、绿、黄）都会击碎印刷节目单语域。

## 颜色

### 调色板
- **Paper / Cream**（`{colors.paper}` — #FAF1E2）：主导暖奶油黄表面。读起来是优质纸料，不是白、不是米，介于两者之间。默认幻灯片背景，也是系统唯一使用的背景填充。
- **Paper Dark**（`{colors.paper-d}` — #F2E5CF）：略深的奶油，供次级表面或色调分隔。token 系统里有但用得省。
- **Paper Very Dark**（`{colors.paper-vd}` — #E8D7B6）：更深的奶油，供强调表面，预留。
- **Ink / Warm Rust Terracotta**（`{colors.ink}` — #B53D2A）：单一墨色。每段文字、每条边、每条线、每片胶囊轮廓、每个页码都用它。系统的结构与表情色。
- **Ink Deep**（`{colors.ink-dp}` — #8E2D1F）：更深的锈色，留给强调。token 系统里有，已发布页面用得省。
- **Rule**（`{colors.rule}` — #B53D2A）：`{colors.ink}` 的别名，同一十六进制，语义上用于指代线时用它。
- **Ink @ 78%**（`{colors.ink-78}` — rgba(181,61,42,0.78)）：78% 不透明度墨。用于弱化元数据文字，需要略低对比时（例如菜单行里的搭配注、引文下的元小片）。
- **Ink @ 50%**（`{colors.ink-50}` — rgba(181,61,42,0.5)）：50% 不透明度墨。用于纸纹径向点渐变内部。
- **Ink @ 32%**（`{colors.ink-32}` — rgba(181,61,42,0.32)）：32% 不透明度墨。用于内部分隔线，卡片内、账目行间、菜行间的 1px 实线与虚线。

### 默认值
- **默认幻灯片背景**：`{colors.paper}`，每页都是。系统里没有替代表面。
- **默认文字色**：`{colors.ink}`，每段文字。
- **默认边框色**：结构边 `{colors.ink}` 1.5px 实线，内部分隔 `{colors.ink-32}` 1px 实线或虚线。
- **默认标题色**：`{colors.ink}`。
- **默认正文色**：`{colors.ink}`。
- **默认页码 / 导航提示色**：`{colors.ink}`（页码全不透明度，导航提示 45% 不透明度）。
- **默认弱化元数据色**：`{colors.ink-78}`，当一小片辅助文字需要从主行往后退时。

配色刻意单墨。没有"强调色"可取，设计语言依赖一墨约束。某瞬间需要突出时，放大字面（Bricolage 800 放到 180px）或取斜体 Fraunces 版次数字，别引入第二色。

## 排印

### 字族
系统从 Google Fonts 恰好加载两款网页字体，都带光学尺寸轴：

- **Bricolage Grotesque** 带 `opsz` 12..96 与字重 400、600、700、800。**已发布页面只用 700 和 800。**
- **Fraunces** 带 `opsz` 9..144、正体与斜体两种样式、字重 400、500、600。**已发布页面用斜体全部三档字重、正体 400/600 字重。**

两字面角色切分严格：**Bricolage 大写承载每个展示瞬间**（封面、标题、卡片标题、菜名、引文正文、信息数值、who-tag、带字距的版次标签）。**Fraunces 斜体承载每个正文瞬间**（段落、导语、元数据、标语、胶囊、页码、信息键、无字距版次标签）。**Fraunces 正体**留给特定紧凑角色（信息行里的信息键，斜体字距在那里会不合拍，以及索引卡片内的说明正文，正体更可读）。

光学尺寸轴关键：同一款 Fraunces 在 14px 元数据尺寸与 480px 英雄数字尺寸下会渲染出略不同的字形，小尺寸取到更结实的笔画，大尺寸取到更精细的细节。自托管无 `opsz` 的回退字面会丢掉这份品质。

### 展示、正文、外壳比例

| Token | 尺寸 | 字族 | 字重 / 样式 | 用途 |
|---|---|---|---|---|
| `{typography.display-jumbo-numeral}` | 最大 480px | Fraunces | 400 斜体 | 英雄版次数字（封面类排印锚点） |
| `{typography.display-cover}` | 最大 180px | Bricolage | 800 大写 | 封面级 Bricolage 标题 |
| `{typography.display}` | 最大 160px | Bricolage | 800 大写 | 分节开场 / 宣言标题 |
| `{typography.headline-xl}` | 最大 140px | Bricolage | 800 大写 | 精选版次标题 |
| `{typography.headline}` | 最大 120px | Bricolage | 800 大写 | 索引 / 日历页顶栏标题 |
| `{typography.headline-md}` | 最大 100px | Bricolage | 800 大写 | 菜单 / 节目单标题 |
| `{typography.quote}` | 最大 96px | Bricolage | 700 大写 | 拉页引文 / 推荐正文 |
| `{typography.card-title}` | 最大 44px | Bricolage | 800 大写 | 带描边卡片内标题 |
| `{typography.course-name}` | 最大 28px | Bricolage | 700 大写 | 账目行里菜 / 项名称 |
| `{typography.info-value}` | 最大 28px | Bricolage | 700 大写 | 键/值信息行里的值 |
| `{typography.edition-label-tracked}` | 最大 18px | Bricolage | 700 大写 / 0.18em | 英雄数字下的大版次标签 |
| `{typography.who-tag}` | 最大 18px | Bricolage | 700 大写 | 引文行里的出处姓名 |
| `{typography.body-serif-italic-lg}` | 最大 28px | Fraunces | 400 斜体 | 宣言 / 书信里的导语段 |
| `{typography.body-serif-italic}` | 最大 22px | Fraunces | 400 斜体 | 标准正文段落 / 导语 |
| `{typography.body-roman}` | 最大 17px | Fraunces | 400 正体 | 卡片说明正文（小尺寸下更可读的紧凑排法） |
| `{typography.edition-label}` | 最大 30px | Fraunces | 400 斜体 | 版次徽章旁的 "EDITION N." 斜体标签 |
| `{typography.tagline}` | 最大 26px | Fraunces | 400 斜体 | 封面标题下的标语 / 副标题 |
| `{typography.stats}` | 最大 22px | Fraunces | 400 斜体 | 统计行（"N seats · M cities · L hours"） |
| `{typography.pill-text}` | 最大 20px | Fraunces | 400 斜体 | 胶囊按钮或方角小片内文字 |
| `{typography.meta-tag}` | 最大 16px | Fraunces | 400 斜体 | 卡片元数据（城市小片、数字小片、席位小片、日期小片） |
| `{typography.info-key}` | 最大 16px | Fraunces | 400 斜体 / 0.16em / 大写 | 键/值信息行里的键 |
| `{typography.pagenum}` | 最大 16px | Fraunces | 400 斜体 | 每页右下角页码 |
| `{typography.nav-hint}` | 最大 13px | Fraunces | 400 斜体 / 45% 不透明度 | 视口左下角导航提示 |

### 默认值
- **页面主标题默认尺寸**：`{typography.headline}`（最大 120px），Bricolage 800 大写。
- **封面级标题默认尺寸**：`{typography.display-cover}`（最大 180px）。
- **封面类页面英雄排印锚点默认尺寸**：`{typography.display-jumbo-numeral}`（斜体 Fraunces 最大 480px），系统签名英雄元素。
- **正文段落默认尺寸**：`{typography.body-serif-italic}`（最大 22px），斜体 Fraunces。
- **导语段默认尺寸**：`{typography.body-serif-italic-lg}`（最大 28px）。
- **卡片内正文默认尺寸**：`{typography.body-roman}`（最大 17px），**正体** Fraunces，正体在小尺寸下比斜体更可读。
- **"EDITION N." 标签默认尺寸**：`{typography.edition-label}`（最大 30px），斜体 Fraunces，配 `{components.ed-badge}` 圆形序数。
- **任何 Bricolage 展示瞬间默认字重**：800（字重 700 留给引文正文与菜名/who-tag 元素，800 是主展示字重）。
- **任何 Fraunces 正文瞬间默认字重**：400。

拿不准时，常规页面标题取 `{typography.headline}`（最大 120px）。140–180px 一档给精选版次标题和封面，160px 一档给分节开场。页面是封面类瞬间、需要英雄锚点时取巨型版次数字。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个 Bricolage 展示元素都大写、负字距（-0.005em 到 -0.012em）。** 系统里不存在句首大写的 Bricolage 标题。大写 + 负字距 + 字重 800 的组合是系统的展示声部。
- **每个 Fraunces 正文元素默认斜体。** 正体 Fraunces 只出现在特定紧凑场合（信息行里的信息键、索引卡片内的正文）。拿不准时斜体。
- **版次徽章（`{components.ed-badge}`）永远配一个斜体版次标签**，圆形序数与 "EDITION N." 文字是一个单元，缺一读起来像坏了。
- **每张卡片 / 胶囊 / 方角小片 / 徽章都带 1.5px 实线墨边、无填充。** 单粗细描边形状语汇是系统的结构语言，填充形状不存在。
- **纸纹叠层（`{components.paper-texture}`）在每页上。** 去掉它（或在无纹理的纯平奶油上跑系统）会丢掉印刷纸质感。
- **每页都带页码标记**，右下角斜体 Fraunces。页码是系统的脊梁，没有它页面显得没锚。
- **卡片内的内部分隔线在 1px 实线 @ 32% 不透明度（内容上方）与 1px 虚线 @ 32% 不透明度（内容下方）之间交替。** 实/虚配对是系统的卡片节奏装置。

### 排印原则
字重 800 + 大写 + 负字距的组合是系统 Bricolage 的声部，换掉三者中任一属性（例如字重 700 大写、字重 800 句首大写、默认字距）都会读成另一套设计系统。Fraunces 默认斜体 + opsz 轴的组合是系统的正文声部，用无 opsz 的回退字面会压平小尺寸品质。

不用下划线。正文段落内的加粗用 Fraunces 字重 600（不是 700/800）。颜色强调不存在，因为只有一种颜色。系统仅有的强调机制是：尺度（更大的 Bricolage）、正文内字重切换（Fraunces 400 → 600）、斜体 ↔ 正体切换、不透明度（全 → 78%）。

## 布局

### 画布系统
系统以流式视口为目标，每张 `.slide` 是 `100vw × 100vh`、绝对定位。幻灯片在 `.stage` 容器内堆叠，纸纹叠层绝对坐在 stage 上。同一时刻只有一张 `.slide.active` 可见，页面间 opacity 过渡 280ms。

### 内边距比例（用 `clamp()` 区间）
| Token | 区间 | 用途 |
|---|---|---|
| `{spacing.slide-pad-h-default}` | clamp(60px, 5vw, 110px) | 默认横向幻灯片内边距 |
| `{spacing.slide-pad-h-wide}` | clamp(80px, 7vw, 160px) | 精选 / 日历页更宽的横向内边距 |
| `{spacing.slide-pad-h-narrow}` | clamp(120px, 12vw, 280px) | 菜单 / 引文页较窄的横向内边距（把内容逼进一栏） |
| `{spacing.slide-pad-top-default}` | clamp(96px, 10vh, 160px) | 默认顶部内边距 |
| `{spacing.slide-pad-top-cover}` | clamp(60px, 6vh, 100px) | 封面顶部内边距（少些，给标题留位） |
| `{spacing.slide-pad-bottom-default}` | clamp(110px, 11vh, 170px) | 默认底部内边距（给页码外壳留位） |
| `{spacing.slide-pad-bottom-wide}` | clamp(150px, 14vh, 220px) | 精选 / 引文页更宽的底部内边距 |
| `{spacing.gap-section}` | clamp(28px, 3vh, 50px) | 主内容分节之间 |
| `{spacing.gap-content}` | clamp(18px, 2vh, 32px) | 相关内容块之间 |
| `{spacing.gap-row}` | clamp(14px, 1.6vh, 24px) | 行级元素之间（菜行、账目行） |
| `{spacing.gap-tight}` | clamp(10px, 1.2vh, 18px) | 紧密耦合元素之间 |

### 外壳解剖
每页右下角带**页码标记**（斜体 Fraunces，最大约 16px）。视口还在左下角带**导航提示**（斜体 Fraunces、45% 不透明度），提示键盘导航。这两个外壳元素是系统通用的页面锚点。

带顶栏的页（索引、日历）左边一个 Bricolage 标题、右边一个小的斜体 Fraunces 标签小片，下方由 1.5px 实线墨色横线分隔。顶栏分隔线是系统通用的页面分隔装置。

### 圆角
- **999px**：胶囊按钮（全胶囊形）
- **50%**：圆形版次徽章
- **0**：其余每个形状（卡片、方角小片、信息卡片、账目行、内部分隔线）

系统给内容容器用尖角、给动作和序数标记用胶囊/圆。不存在中等 border-radius 值（4px、8px、12px）。

## 纵深与层级

### 平、无阴影
系统**零阴影**。没有 box-shadow、没有 text-shadow、没有滤镜、没有渐变。抬升完全靠：
1. **卡片、胶囊、徽章、方角小片上的 1.5px 实线墨边**，描边形状语汇是系统的结构纵深。
2. **卡片内、行间 32% 不透明度的 1px 实线或虚线内分隔线**，微妙横线给卡片内部节奏。
3. **每页 10% 不透明度的纸纹叠层**，点状纹理氛围地坐在所有内容下方，给页面印刷纸料质感。
4. **文字的不透明度分层**：主 100%、弱化元数据 78%、几乎不可见的分隔 32%。

没有阴影本身就是纵深语言。加 `box-shadow: 0 4px 12px rgba(0,0,0,0.1)` 会击碎印刷纸感。

### 纸纹作为氛围纵深
`.stage::before` 上的径向点纹理是纵深系统的一部分，不是可选装饰。纹理给奶油表面一种平 #FAF1E2 所没有的质感：表面像带颗粒的纸料，而非 CSS 背景填充。4px 平铺尺寸配 50% 不透明度墨色的 0.5px 径向点、整体 10% 不透明度，校准到交谈距离不可见、凑近细看才可见。

## 形状与处理

### 边框粗细与样式
- **1.5px 实线 `{colors.ink}`**：通用结构边。卡片、胶囊、版次徽章、方角小片、顶栏分隔线、who-row 顶边、信息卡片轮廓。
- **1px 实线 `{colors.ink-32}`**：卡片内实线内分隔（卡片顶部元数据与卡片标题之间）、账目行间、菜行间。
- **1px 虚线 `{colors.ink-32}`**：卡片内虚线内分隔（卡片正文与底部元行之间）、信息卡片内信息行间。

边框绝不粗于 1.5px，绝不上墨色以外的颜色（全或 32%），绝不用点线（点线留给纸纹图案）。卡片内实/虚配对是系统招牌的节奏装置。

### 装饰元素类型

**纸纹叠层**（`{components.paper-texture}`）：`.stage::before` 上 50% 不透明度墨色、整体 10% 不透明度的 4px 平铺径向点图案。系统的氛围基底，每页都有。

**胶囊按钮**（`{components.pill}`）：带描边的全圆角矩形（border-radius 999px），装短斜体 Fraunces 文字。系统的 CTA / 动作按钮。胶囊簇在动作行里（例如封面动作行）。

**胶囊分隔**（`{components.pill-divider}`）：小的斜体 Fraunces 字符（通常 `·` 或 `/`），70% 不透明度，放在一行里胶囊之间。

**版次徽章**（`{components.ed-badge}`）：约 38px 的圆形带描边徽章，装单个斜体 Fraunces 数字。系统的版次 / 章节序数标记，永远配斜体 "EDITION N." 标签。

**方角小片**（`{components.rect-tag}`）：带描边的尖角矩形小片，装短斜体 Fraunces 文字。胶囊的尖角表亲，用在圆角不合适的场合。

**带描边卡片**（`{components.card-outlined}`）：1.5px 墨色描边的矩形卡片。装卡片顶部元数据行（下方由 1px @ 32% 实线分隔）、Bricolage 卡片标题、Fraunces 正文说明、底部元行（上方由 1px @ 32% 虚线分隔）。系统的主内容卡片。

**带分隔线的顶栏**：左边 Bricolage 标题 + 右边小斜体 Fraunces 标签小片，下方由 1.5px 实线墨色横线分隔。系统通用的分节开场。

**信息卡片**：更宽的带描边卡片，内部信息行（键 / 值对由 1px @ 32% 虚线分隔）。用作精选版次辅助面板。

**账目行**（`{components.ledger-row}`）：多列网格行，带 1px @ 32% 实线底边。小片、标签、胶囊在列里对齐。系统的日历 / 日程 / 索引模式。

**菜行**：64px / 1fr / auto 网格行，带 1px @ 32% 实线底边。装一个 Fraunces 数字小片、一个条目（Bricolage 名称 + Fraunces 说明）、一个 Fraunces 搭配小片。菜单 / 节目单模式。

**斜体巨型版次数字**：最大 480px 的斜体 Fraunces 数字。封面类页面系统招牌的英雄排印锚点，下方配一行小字距 Bricolage 标签和一行斜体 Fraunces 元信息。

**页码**（`{components.pagenum}`）：每页右下角斜体 Fraunces。

**导航提示**（`{components.nav-hint}`）：视口左下角、45% 不透明度的斜体 Fraunces，提示键盘导航。

## 该做与不该做

### 该做
- 认准单墨渲染。每段文字、每条边、每条线、每个徽章、每片胶囊都是 `{colors.ink}` 暖锈陶土。用不透明度（78%、32%、10%）作变化，绝不用别的色相。
- 每页都套纸纹叠层。10% 不透明度的 4px 径向点图案是设计系统的一部分，不是可选润色。
- 每个 Bricolage 展示元素跑字重 800（引文 / 菜名 / who-tag 用 700）、严格大写、负字距。
- 每个 Fraunces 正文元素默认斜体。正体只给信息键（斜体字距在那里会不合拍）和卡片正文说明（小尺寸下斜体可读性差）。
- 取斜体 Fraunces 巨型数字（最大 480px）作封面类页面的英雄排印锚点，它是系统签名。
- 每枚版次徽章都配一个斜体 "EDITION N." Fraunces 标签，圆形序数与文字标签是一个单元。
- 主内容卡片用带描边卡片模式（1.5px 墨边 + 内容上方 1px @ 32% 实线内分隔 + 内容下方 1px @ 32% 虚线内分隔）。实/虚配对是系统的节奏。
- 有意识地用胶囊（border-radius 999px）和方角小片（尖角）：胶囊给动作，方角给元数据 / 状态，别混为一谈。
- 每页放页码标记（斜体 Fraunces、右下）。标记是系统的脊梁。
- 页面保持丰富但精心：一个主要 Bricolage 展示瞬间 + 2–4 组辅助组（卡片、胶囊、账目行、信息对）。单元素页显得分量不足，8 元素页显得坏了。

### 不该做
- 不要引入第二墨色。系统单墨，加海军、绿、黄或任何第二色相都会击碎印刷节目单语域。
- 不要填充任何形状。卡片、胶囊、徽章、方角小片只描边，墨色填充矩形不存在。
- 不要给任何元素用 box-shadow、渐变、模糊或滤镜。系统是平的印刷纸。
- 不要省掉纸纹叠层。没有点图案的平 #FAF1E2 背景读起来是数字，不是纸。
- 不要把 Bricolage 跑成句首大写。Bricolage 始终大写、负字距、字重 700 或 800。
- 不要把 Fraunces 默认渲染成正体。斜体是正文声部，正体是特定紧凑场合的例外。
- 不要用更粗的边（2px+）。1.5px 结构边粗细是系统的承诺。
- 不要用中等 border-radius（4px、8px、12px）。系统用 999px（胶囊）、50%（徽章）或 0（其余一切）。
- 不要把版次徽章配非 Fraunces 标签或干脆省掉标签。徽章与标签单元是系统的版次标记。
- 不要用 8 个小元素塞满一页。宁可更少、更大的组，留有呼吸。

## 响应式行为

系统通篇用 **`clamp()` 单位**，每个尺寸、内边距、间隙、线都按视口宽高在最小与最大之间流畅缩放。同一构图在 1280×720 笔记本、1920×1080 显示器、2560×1440 屏上无需媒体查询都能正确渲染。

### 缩放行为
- Bricolage 展示尺寸在最小值（例如 60px）、基于 vw/vh 的中值、最大值（例如 140px）之间 clamp。内层 `min()` 函数把基于宽和基于高的封顶合并，标题不会在矮视口上溢出。
- Fraunces 正文尺寸遵循同样模式但区间更小。
- 内边距与间隙随 vw/vh 线性缩放。
- 1.5px 结构边与 1px @ 32% 内分隔线是固定像素、不缩放，于是大视口下比例上显得更细，这是刻意的。

### 放映行为
- 经键盘导航前进（由 deck JavaScript 处理）。
- 同一时刻只有一张 `.slide.active` 可见，非激活页 `opacity: 0; pointer-events: none`。
- 页到页过渡是 280ms opacity 淡入。
- 左下导航提示（"← → to navigate"）告诉观者如何前进。

### 打印 / 导出
系统没有 `@media print` 规则。打印导出只渲染激活页，多页打印需逐页渲染或专用打印样式表。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 中文字面 | 字重 | 理由 |
|---|---|---|---|
| 展示 / 封面 / 标题（Bricolage 角色，96–180px） | 思源宋体 Noto Serif SC | 700 | 明朝重字重承载 Bricolage 800 在拉丁里提供的印刷节目单分量 |
| 卡片标题 / 菜名 / 信息数值（28–44px） | 思源宋体 Noto Serif SC | 700 | 同一明朝声部在小尺寸保持一致 |
| 英雄版次数字（480px 斜体 Fraunces） | 思源宋体 Noto Serif SC | 400 | 用中文序数字符（一二三 / 春夏秋）作英雄锚点，而非西方数字 |
| 正文 / 导语 / 标语（Fraunces 斜体角色） | 思源宋体 Noto Serif SC | 400 | 明朝正文声部，无斜体也有暖意，因为中文没有斜体 |
| 胶囊文字 / 元小片 / 页码 | 思源宋体 Noto Serif SC | 400 | 所有外壳留在明朝 400，系统的单墨纪律贯穿 |
| 信息键 / 带字距版次标签（大写宽字距角色） | 思源宋体 Noto Serif SC | 400 配 0.16em 字距 | 维持宽字距外壳感 |

### 混排策略

用**策略 A**：把所有角色的整条字面栈切到 Noto Serif SC，替换 Bricolage Grotesque（展示）与 Fraunces（正文）两者。Long Table 是一套极简的单墨数据 / 节目单系统，排印个性更多由**单墨锈陶土**、**描边形状语汇**、**纸纹叠层**承载，而非特定拉丁字面。中文全用明朝体能干净地保住印刷节目单语域，不引入策略 C 在这套排印如此密集的系统上会带来的逐字形基线晃动。栈：

```css
/* Bricolage roles (display, headline, card-title, course-name, info-value) */
font-family: 'Bricolage Grotesque', 'Noto Serif SC', sans-serif;
/* Fraunces roles (body, lede, tagline, pill, pagenum, edition-label) */
font-family: 'Fraunces', 'Noto Serif SC', Georgia, serif;
```

文稿内容是纯中文时，把两条字体栈都覆盖成以 Noto Serif SC 领衔。Bricolage 角色取字重 700（匹配明朝里的 800 分量），Fraunces 角色取字重 400。

### 加载

在既有 Google Fonts `<link>` 里追加：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

以下调整适用于本系统**每一个 CJK 块**，无论尺寸或角色：

- **行高放宽 0.05–0.08。** CJK 字形是全宽方块，视觉分量比拉丁字形重，为拉丁调的行高（展示 0.86–0.95、正文 1.45–1.5）在中文里读起来局促。展示放到 1.0–1.1，正文放到 1.55–1.65。
- **去掉 CJK 标题的负字距。** Bricolage 展示用 -0.005em 到 -0.012em 字距，会撞在一起。CJK 段设 `letter-spacing: 0`，标题看着挤时可用微小的正 `0.02em`。
- **绝不对 CJK 文字用 `text-transform: uppercase`。** 中文没有大小写，CSS 属性对汉字无效，却会悄悄破坏混排行里本该大写的 Bricolage 部分。（这里尤其要紧，源码里每个 Bricolage 展示元素都是 `text-transform: uppercase`。）
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不用拉丁对应物（`,.:;!?""''()`）。同一句里混用标点系统读起来是排印错误。
- **CJK 标题末尾不加句号（。）。** 中文标题与拉丁遵循同一规则，标题式行去掉末尾标点。正文段落保留 。
- **在 CJK 与拉丁串交界处套用盘古之白。** 汉字与相邻拉丁词或数字之间应有一个空格（或 0.25em 外边距），例如 `2026 年 5 月` 而非 `2026年5月`。要么手打空格，要么用 `pangu.js` 式自动加空格器。
- **一句一款字体。** 不要在同一句里切换 Noto Serif SC 字重 400 与 700，挑与角色匹配的字重（标题 = 700，正文 = 400），整段从一而终。

### 本系统的美学提示

Long Table 的整个声部是"晚餐俱乐部海报 / Risograph zine / 小出版社晚宴节目单"，奶油上单墨锈陶土、描边形状、纸纹叠层。中文里系统身份不依赖特定拉丁字面（Bricolage 和 Fraunces），而依赖**单墨承诺**、**1.5px 描边形状语汇**、**4px 径向点纸纹**、**丰富但精心的密度**。全用 Noto Serif SC 能干净保住每一个身份标记。

默认斜体正文规则不汉化到中文（中文没有斜体概念，倾斜汉字读成坏了，不是正文声部）。中文里每个 Fraunces 斜体角色直接变成 **Noto Serif SC 字重 400 正体**，暖意来自明朝字面本身，不来自倾斜。对这套系统是正确的取舍。

英雄斜体 Fraunces 巨型数字（最大 480px）是拉丁里的签名锚点，一个斜体数字充当排印中心件。中文里**用中文序数或季节字符代替西方数字**：「三」、「五」、「春」、「秋」，以 Noto Serif SC 字重 400 渲染。汉字在 480px 下更密的视觉分量比西方数字更能平衡封面页，奶油纸底与暖锈墨把印刷节目单感原样传下来。

系统的描边形状语汇（胶囊、版次徽章、方角小片、带描边卡片）在中文里完全一样，无需调整。与圆形徽章配对的 "EDITION N." 标签变成圆圈里的「第三期」或「第 03 期」，下方元标签用 Noto Serif SC 400。32% 不透明度的实 / 虚内分隔节奏纯结构性，不受语言影响。

### 已知 CJK 缺口

Fraunces 默认斜体正文声部是 Long Table 在拉丁里最鲜明的排印动作之一，斜体明朝式衬线正文给系统带来抒情、手写的暖意。中文没有对应：Google Fonts CDN 上没有常用的"斜体明朝"字面，倾斜汉字无论如何都读成坏了。中文渲染会丢掉默认斜体性格，每段正文行变成正体 Noto Serif SC 字重 400。这是个性上的真实损失，部分由 Noto Serif SC 在正文尺寸下自身的暖意补偿，但中文内容的 Long Table 文稿读起来明显更像"中性杂志"而非"晚餐俱乐部海报"。对这点要紧的文稿，更倚重**单墨色**与**纸纹叠层**来承载拉丁里斜体正文所承载的暖意。

## 迭代指南

1. 页面上的任何新痕迹都是 `{colors.ink}`，主痕迹全不透明度、弱化元数据 78%、内部分隔 32%。没有第二色。
2. 任何新标题都是 Bricolage Grotesque 字重 800 大写、负字距。从标题阶梯里挑尺寸（96 / 100 / 120 / 140 / 160 / 180px 上限），别自创尺寸。
3. 任何新正文段落都是 Fraunces 斜体字重 400。正体只给信息键（宽字距大写）和卡片正文说明。
4. 任何新版次 / 序数标记都用 `{components.ed-badge}`（圆形描边）配斜体 "EDITION N." Fraunces 标签。
5. 任何新动作按钮都是 `{components.pill}`（border-radius 999px），任何新元数据小片都是 `{components.rect-tag}`（尖角）。别把两者混为一谈。
6. 任何新卡片都是 `{components.card-outlined}` 模式：1.5px 墨边、内容上方 1px @ 32% 实线内分隔、内容下方 1px @ 32% 虚线内分隔。
7. 任何新账目 / 日程 / 日历行都用多列网格 + 1px @ 32% 实线底边模式（`{components.ledger-row}`）。
8. 任何新分节开场都用顶栏模式：Bricolage 标题 + 右侧小斜体 Fraunces 标签 + 下方 1.5px 实线墨色横线。
9. 任何新封面类瞬间都取斜体 Fraunces 巨型版次数字作英雄排印锚点，下方配小字距 Bricolage 标签和一行斜体 Fraunces 元信息。
10. 每页都带页码标记。省掉它，页面会显得没锚。

## 已知缺口

- 两款 Google Fonts（Bricolage Grotesque 带 `opsz` 12..96、Fraunces 带 `opsz` 9..144）经 `<link>` 加载。离线渲染会回退到系统无衬线（Bricolage）与 Georgia（Fraunces），丢掉光学尺寸轴和两款字面的个性。离线 / 打印可靠性建议自托管。
- `opsz` 光学尺寸轴对大展示尺寸（480px 巨型数字）和小元数据尺寸（14px 页码）的品质关键，无 `opsz` 的回退字面在两端会明显显平。
- 系统按设计单墨。若文稿需要第二强调色（"标注"或"警告"色相），系统不破掉印刷节目单语域就无法容纳。只把 Bricolage 尺度 + 不透明度 + 斜体/正体切换作为强调机制。
- 纸纹叠层用 `background-image` 径向渐变，某些浏览器高缩放下可能带细微压缩瑕疵。纹理对系统身份不可少，别当"性能优化"去掉它。
- 正文段落默认斜体。文稿内容里斜体在正文尺度难读时（长技术段落、代码示例），系统没有干净的回退，斜体就是正文声部。段落保持短而抒情。
- CSS 里有几个空规则块（`.body-it { ... }`、`.s-cover .stats .num { font-weight: 600; }` 等），原本注释掉的斜体 / 字重属性被剥掉了。许多地方意图中的处理是"斜体 Fraunces 字重 400"，即默认样式，但空块让这变成隐式而非显式。注释暗示处一律把斜体当默认。
- 系统加载 Bricolage 字重 400、600 与 Fraunces 字重 500，已发布 CSS 里未活跃使用，用它们会引入打破每字面单字重承诺的中间字重。
- 回退 `.body-it` 与 `.body-ro` 工具类已定义，但标记里很少显式用这些类名。多数页逐元素设排印，而非经工具类，编写新页时复制逐元素样式，别复制工具类。
- 480px 英雄斜体 Fraunces 巨型数字是字面数字字符，特定字符没有字形替换或字距修正。"0" 与 "8" 字形在极端尺寸下可能需要光学调整，在目标视口核对渲染。
- 系统没有 `@media print` 规则，打印导出不会分页，把 Long Table 当屏幕优先系统。
