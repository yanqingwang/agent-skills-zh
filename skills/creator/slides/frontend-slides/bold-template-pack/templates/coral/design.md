---
version: alpha
name: Coral
description: "A bold magazine-poster system that runs on three surface registers — coral fire, ink black, and warm cream — animated by Bebas Neue display caps and a constant 45° diagonal hatch pattern. Inter handles body copy; Bebas Neue handles every headline, stat, title, and meta-figure at heavy letter-spacing. The cultural reference is mid-century travel posters, Saul Bass film titles, and modern editorial sport magazines: solid color planes meeting at hard edges, oversized condensed caps as architectural elements, and a single coral hue used both as accent and as full-slide environment."

colors:
  coral: "#E85D5D"
  coral-dark: "#D44A4A"
  cream: "#F5F0E8"
  cream-dark: "#E8E0D4"
  black: "#1A1A1A"
  gray: "#6B6B6B"
  light-gray: "#B0B0B0"
  white: "#FFFFFF"

color-aliases:
  bg: cream
  ink: black

typography:
  hero-title:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "min(120px, 9vw, 13vh)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: 4px
  jumbo-feature:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(80px, 15vw, 200px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 12px
  display-statement:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(42px, 7vw, 100px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  section-headline:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(40px, 6vw, 80px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  column-title:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(36px, 5vw, 72px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  stat-numeral:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(48px, 7vw, 96px)"
    fontWeight: 400
    lineHeight: 1
  card-stat:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(36px, 4vw, 56px)"
    fontWeight: 400
    lineHeight: 1
  sidebar-value:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(28px, 3vw, 48px)"
    fontWeight: 400
    lineHeight: 1
  card-title:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(24px, 2.5vw, 36px)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 1px
  bar-title:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(28px, 4vw, 56px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  meta-figure:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "min(44px, 3.5vw, 5.5vh)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  meta-date:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "min(38px, 3vw, 4.8vh)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  background-numeral:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(100px, 15vw, 200px)"
    fontWeight: 400
    lineHeight: 1
    description: "Decorative oversized numeral placed inside a coral region at rgba(0,0,0,0.12) — wallpaper opacity. Sits behind the actual column title at full opacity."
  giant-mark:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(140px, 20vw, 280px)"
    fontWeight: 400
    lineHeight: 1
    description: "Oversized quote mark or single character placed inside a coral region at opacity 0.35 — half-decorative, half-content."
  body:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(15px, 1.4vw, 20px)"
    fontWeight: 400
    lineHeight: 1.7
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(13px, 1.1vw, 16px)"
    fontWeight: 400
    lineHeight: 1.6
  body-light:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(20px, 2.5vw, 36px)"
    fontWeight: 300
    lineHeight: 1.5
    description: "Lighter-weight Inter for pull quotes — weight 300 to contrast against the Bebas Neue dominant voice."
  item-text:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(14px, 1.2vw, 18px)"
    fontWeight: 400
    lineHeight: 1.6
  card-text:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(13px, 1.1vw, 16px)"
    fontWeight: 400
    lineHeight: 1.6
  bar-meta:
    fontFamily: "Inter, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 2px
    textTransform: uppercase
  section-label:
    fontFamily: "Inter, sans-serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 4px
    textTransform: uppercase
  item-label:
    fontFamily: "Inter, sans-serif"
    fontSize: "11px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 3px
    textTransform: uppercase
  meta-label:
    fontFamily: "Inter, sans-serif"
    fontSize: "11px"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 3px
    textTransform: uppercase
  sidebar-label:
    fontFamily: "Inter, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1px
  quote-attribution:
    fontFamily: "Inter, sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 3px
    textTransform: uppercase
  quote-role:
    fontFamily: "Inter, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1px

spacing:
  pad-y: "clamp(40px, 6vh, 80px)"
  pad-x: "clamp(40px, 8vw, 100px)"
  pad-y-tight: "clamp(28px, 4.5vh, 60px)"
  pad-col: "clamp(32px, 4vw, 60px)"
  gap-grid: "32px"
  gap-md: "40px"
  card-pad: "clamp(24px, 3vh, 40px)"
  bar-pad: "clamp(24px, 4vh, 40px)"

canvas:
  width: 100vw
  height: 100vh

components:
  diagonal-hatch:
    background: "repeating-linear-gradient(45deg, transparent, transparent 20px, rgba(0,0,0,0.06) 20px, rgba(0,0,0,0.06) 40px)"
    description: "Signature 45° diagonal hatch pattern in 6%-opacity black. Applied as a pseudo-element overlay on coral regions to provide texture without changing the surface color. Variant: -45° hatch on coral quote-left, with 30/60px stride. Variant: 90° vertical hatch in 10%-opacity black on coral gradient regions, with 60/62px stride. The hatch is a per-region atmospheric treatment, not a slide-level overlay."
  accent-line:
    width: "80px"
    height: "4px"
    background: "{colors.coral}"
    description: "Solid 80×4 coral rectangle used as a sub-headline accent rule. Closing or section-divider variant uses 60×4."
  quote-accent:
    width: "60px"
    height: "4px"
    background: "{colors.coral}"
    description: "60×4 coral rectangle placed above a quote attribution as a terminal accent."
  title-rule:
    width: "100%"
    height: "3px"
    background: "{colors.black}"
    opacity: 0.15
    description: "Full-width 3px ink rule at 15% opacity used as a subtle horizontal divider beneath the hero title on the cover composition."
  card:
    background: "{colors.white}"
    padding: "{spacing.card-pad}"
    borderTop: "5px solid {colors.coral}"
    description: "Column card — white surface with a 5px solid coral top border as the only border on the element. No shadow, no radius."
  sidebar-item:
    background: "{colors.white}"
    padding: "20px 24px"
    borderLeft: "4px solid {colors.coral}"
    description: "Compact data tile — white surface with a 4px solid coral left border. Holds a Bebas value and an Inter label."
  card-icon:
    width: "48px"
    height: "48px"
    background: "{colors.coral}"
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "24px"
    color: "{colors.white}"
    description: "48px solid coral square (no radius) containing a 1-character Bebas Neue glyph in white. Used as a card mark."
  timeline-line:
    height: "4px"
    background: "{colors.black}"
    description: "Horizontal 4px solid ink line spanning the timeline width. A ::after pseudo overlays a repeating linear-gradient (20px ink + 10px transparent) to create a dashed effect. The dashed pattern is rendered through the gradient, not the border-style."
  t-point-dot:
    width: "20px"
    height: "20px"
    borderRadius: "50%"
    background: "{colors.coral}"
    border: "4px solid {colors.cream}"
    description: "Timeline node — 20px coral circle with a 4px cream halo, sitting on the timeline-line."
  nav-dot:
    width: "10px"
    height: "10px"
    borderRadius: "50%"
    background: "rgba(255, 255, 255, 0.3)"
    border: "2px solid rgba(255, 255, 255, 0.5)"
    description: "Small 10px nav indicator. White-translucent default on dark/coral surfaces; ink-translucent .dark variant on cream surfaces. Active state fills with coral."
  nav-arrow:
    width: "44px"
    height: "44px"
    borderRadius: "50%"
    background: "rgba(255, 255, 255, 0.1)"
    border: "2px solid rgba(255, 255, 255, 0.3)"
    description: "44px circular nav button with translucent fill and 2px translucent border. .dark variant for cream surfaces. Hover state fills with coral."
  zigzag-layer:
    description: "SVG zigzag pattern overlay used decoratively on the cover's coral top-section. Renders as a thin black zigzag line at low opacity behind the title."
  pattern-overlay:
    description: "Decorative repeating-pattern overlay applied to feature regions — typically 90° vertical hatch in ink at 10% opacity on coral gradient backgrounds. Separate from the 45° diagonal-hatch which is the system's primary texture."
  bar-fill:
    description: "Chart.js horizontal bar fills use solid coral (#E85D5D) as the primary series color, with a darker coral (#D44A4A) for comparison or secondary series."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/coral/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Coral 是一套**大胆的杂志海报系统**，建立在三种表面语域上：珊瑚火、墨黑、暖奶油，以硬边相接。定义性的结构前提是**实色平面**：单页会切成珊瑚一半 + 奶油一半 + 墨色顶段，每个区域是一块平实色，装着自己自足的构图。区域之间没有渐变过渡，两色相接处就是布局。这是相对精致编辑系统更平民化的一版，更像体育杂志封面而非文学图录。

字面栈是**两级层级**。**Bebas Neue**，高窄的紧缩无衬线展示字面，承载每个标题、每个统计、每个栏目标题、每个元数字、每个分节名。Bebas 跑它唯一的可用字重（400），被当作建筑元素处理：重字距（2–12px）、超大尺度（巨型特写最多 200px）、始终用原生大写。**Inter**，当代人文无衬线，承载每个正文段落、每个标签、每个微型文字、每个出处。Inter 跨字重 300 到 700：拉页引文正文用 300，段落正文用 400，元标签用 600，分节眉题用 700。Bebas/Inter 搭配造出系统声部：Bebas 宣告，Inter 解释。

配色是**三表面 + 墨 + 中性色**。珊瑚 `{colors.coral}` 既是**那一强调**（侧栏块上的 4px 左边、卡片上的 5px 顶边、48px 实色图标方块），也是整页环境（满珊瑚面板、封面顶段、珊瑚渐变特写区域）。奶油 `{colors.cream}` 是暖画布，杂志纸。墨 `{colors.black}` 是最强的表面，作引文与陈述布局的整页背景。白只作珊瑚或奶油区域上的卡片填充。两档灰（`{colors.gray}`、`{colors.light-gray}`）承载正文与元文字。

纵深是**平中带硬色边**。没有投影、没有圆角表面、没有柔和抬升。层级来自：
- **实色区域切分**：珊瑚 / 墨 / 奶油区域以硬边相接。
- **强调边框**：4px 珊瑚左、5px 珊瑚顶、3px 墨顶、4px 墨横。
- **45° 对角斜纹**：招牌的 6% 不透明度黑色对角重复图案，叠在珊瑚区域上提供纹理。
- **超大装饰排印**：背后 12% 不透明度的数字、35% 不透明度的巨型引号，坐在主内容后方或旁边。

**密度取向：中高，由区域组织。** Coral 页面是"有结构"而非"密"：每个色区装一个自足构图（一个栏目标题配一段正文、一个统计块配一个标签、一条时间轴线配五个点）。美学依赖区域在自身边界内显得填满，而非整页拥挤。构图正确的一页配 2–3 个实质区域，每个充分表达。显得坏掉的页，是珊瑚区域只装了稀疏碎片，或奶油区域试图承载太多互抢的元素。内容自身填不满平面时，区域主标题背后 12% 不透明度的超大装饰数字，就是标准的"填满区域"手法。

**关键特征：**
- 三表面系统：`{colors.coral}`（火）、`{colors.black}`（墨）、`{colors.cream}`（纸），作以硬边相接的实色区域。
- Bebas Neue 大写紧缩展示用于每个标题/统计/标题；Inter 无衬线用于每个正文/标签/出处。
- 45° 对角斜纹，珊瑚区域上 6% 不透明度黑，作招牌氛围纹理。
- 珊瑚既作强调（4–5px 边、48px 图标方块、4 点时间轴点），又作环境（整区域表面）。
- 珊瑚区域内栏目标题背后 12% 不透明度的超大装饰数字。
- 珊瑚区域内 35% 不透明度的超大引号，作半装饰内容。
- 矩形不加圆角，圆形只给导航点、导航箭头、时间轴节点。
- 每个 Bebas 元素重字距：多数 1–4px，最大特写处理 12px。
- 硬边色切分（纵向、横向或 40/60 比例）定义页面构图。

## 颜色

### 三表面系统
- **Coral**（`{colors.coral}` — #E85D5D）：招牌色，暖橙红，鲜艳但不霓虹。既作强调（侧栏项 4px 左边、卡片 5px 顶边、48px 卡片图标填充、80×4 强调线、60×4 引文强调、时间轴点、图表主系列、悬停态填充、分节眉题、奶油表面上的统计数字），也作整区域表面（封面顶段、双栏左面板、满宽特写区域、引文左面板）。定义系统。
- **Coral Dark**（`{colors.coral-dark}` — #D44A4A）：更深的珊瑚变体。用作线性渐变特写区域（从 coral-dark 到 coral 的 135°）的起始色标，以及图表次级/比较系列色。
- **Cream**（`{colors.cream}` — #F5F0E8）：暖画布。用作默认幻灯片背景、封面底段、信息条表面、墨黑表面上的正文文字色、时间轴点光晕。
- **Cream Dark**（`{colors.cream-dark}` — #E8E0D4）：略深的奶油。调色板里可用于微妙区域区隔，但用得省。
- **Black**（`{colors.black}` — #1A1A1A）：近黑墨。用作奶油表面上的标题色、引文与某些特写页的整页背景墨语域、时间轴线色、标题线色、珊瑚区域内装饰背景数字色（12% 不透明度）、巨型标记色（35% 不透明度）。
- **Gray**（`{colors.gray}` — #6B6B6B）：中中性色。用于奶油表面上的正文段落、元标签、侧栏标签、卡片正文、引文角色。
- **Light Gray**（`{colors.light-gray}` — #B0B0B0）：浅中性色。调色板里定义了但用得省，可供灰太重时的三级文字使用。
- **White**（`{colors.white}` — #FFFFFF）：真白。用作卡片填充（侧栏项、卡片、栏目卡片）、墨表面上的项目文字色、导航点/导航箭头半透明填充。

### 默认值
- **默认幻灯片表面**：`{colors.cream}`。（封面与特写页用混合表面构图；陈述、引文、三栏页默认奶油或墨。）
- **奶油表面上默认标题色**：`{colors.black}`，Bebas Neue 标题是墨色，不是珊瑚。
- **珊瑚表面上默认标题色**：`{colors.black}`，火上墨。Bebas 压珊瑚永远是墨，绝不是白。
- **墨表面上默认标题色**：`{colors.cream}`。
- **奶油表面上默认正文文字色**：`{colors.gray}`。
- **墨表面上默认正文文字色**：`{colors.cream}`。
- **珊瑚表面上默认正文文字色**：`{colors.black}`，墨，不是白。
- **默认眉题 / 分节标签色**：奶油与墨表面上 `{colors.coral}`，珊瑚表面上 `{colors.black}`。
- **默认强调边框色**：`{colors.coral}`，4px 左（侧栏块）、5px 顶（卡片）、48px 实色（图标方块）。
- **珊瑚区域内默认装饰数字色**：`rgba(0, 0, 0, 0.12)`（12% 不透明度墨）。
- **珊瑚区域内默认巨型标记色**：`rgba(0, 0, 0, 0.35)`（35% 不透明度墨）。
- **默认图表主系列色**：`{colors.coral}`。
- **默认图表比较系列色**：`{colors.coral-dark}`。

三种表面按构图混用：一页可切成珊瑚/奶油、珊瑚/墨、墨/奶油，或保持单一表面。表面之间没有语义映射，每种都按构图平衡与对比挑选。

## 排印

### 字族
系统跑在**两级层级**上：`Bebas Neue`（展示，单字重 400）承载每个标题、统计数字、栏目标题、元数字、条标题、卡片统计、侧栏数值、装饰数字；`Inter`（无衬线，字重 300 / 400 / 600 / 700）承载每个正文段落、标签、眉题、元标签、出处、角色、图表图例。没有第三字面。

Bebas Neue 是高窄的紧缩无衬线展示字面，窄字形让它放到很大也不压页宽，唯一的可用字重（400）被当作系统唯一的字重。Bebas 始终用原生大写。系统的展示性格来自重字距（标准标题 1–4px、最大巨型特写 12px）与超大尺度（巨型 / 巨型标记瞬间 200–280px）。

Inter 以字重反差承载辅助声部：拉页引文正文用 300（对着 Bebas 的主导更轻的语域），段落正文用 400，元标签用 600，分节眉题用 700。不用斜体，不用下划线。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.giant-mark}` | clamp(140px, 20vw, 280px) | Bebas Neue | 400 | 珊瑚区域内超大装饰引号或特写字符 |
| `{typography.jumbo-feature}` | clamp(80px, 15vw, 200px) | Bebas Neue | 400 | 填满特写区域的单个主导词 |
| `{typography.background-numeral}` | clamp(100px, 15vw, 200px) | Bebas Neue | 400 | 珊瑚区域内 12% 不透明度的装饰壁纸数字 |
| `{typography.hero-title}` | min(120px, 9vw, 13vh) | Bebas Neue | 400 | 最大封面标题，3 行标题按大写断行 |
| `{typography.display-statement}` | clamp(42px, 7vw, 100px) | Bebas Neue | 400 | 奶油表面上的大宣告陈述 |
| `{typography.stat-numeral}` | clamp(48px, 7vw, 96px) | Bebas Neue | 400 | 英雄统计数字 |
| `{typography.section-headline}` | clamp(40px, 6vw, 80px) | Bebas Neue | 400 | 分节主标题 |
| `{typography.column-title}` | clamp(36px, 5vw, 72px) | Bebas Neue | 400 | 区域内栏目或面板标题 |
| `{typography.card-stat}` | clamp(36px, 4vw, 56px) | Bebas Neue | 400 | 逐卡统计数字 |
| `{typography.bar-title}` | clamp(28px, 4vw, 56px) | Bebas Neue | 400 | 信息条标题 |
| `{typography.sidebar-value}` | clamp(28px, 3vw, 48px) | Bebas Neue | 400 | 侧栏块数值 |
| `{typography.card-title}` | clamp(24px, 2.5vw, 36px) | Bebas Neue | 400 | 卡片或栏目卡片标题 |
| `{typography.meta-figure}` | min(44px, 3.5vw, 5.5vh) | Bebas Neue | 400 | 封面元数值（地点、日期、品牌） |
| `{typography.meta-date}` | min(38px, 3vw, 4.8vh) | Bebas Neue | 400 | 封面日期变体 |
| `{typography.body-light}` | clamp(20px, 2.5vw, 36px) | Inter | 300 | 拉页引文正文（对着 Bebas 主导更轻的字重） |
| `{typography.body}` | clamp(15px, 1.4vw, 20px) | Inter | 400 | 标准段落正文 |
| `{typography.item-text}` | clamp(14px, 1.2vw, 18px) | Inter | 400 | 墨表面上的项目正文 |
| `{typography.card-text}` | clamp(13px, 1.1vw, 16px) | Inter | 400 | 卡片正文 |
| `{typography.body-sm}` | clamp(13px, 1.1vw, 16px) | Inter | 400 | 紧凑正文 |
| `{typography.section-label}` | 12px | Inter | 700 | 标题上方的分节眉题，4px 字距 |
| `{typography.item-label}` | 11px | Inter | 700 | 列表里的项目眉题，3px 字距 |
| `{typography.meta-label}` | 11px | Inter | 600 | 封面元标签，3px 字距 |
| `{typography.quote-attribution}` | 14px | Inter | 600 | 拉页引文下方作者名，3px 字距 |
| `{typography.bar-meta}` | 12px | Inter | 400 | 信息条元文字，2px 字距 |
| `{typography.sidebar-label}` | 12px | Inter | 400 | 侧栏块标签，1px 字距 |
| `{typography.quote-role}` | 12px | Inter | 400 | 引文出处下方作者角色，1px 字距 |

### 默认值
- **分节主标题默认尺寸**：`{typography.section-headline}`（clamp 40–80px）。
- **封面/英雄标题默认尺寸**：`{typography.hero-title}`（min(120px, 9vw, 13vh)）。
- **特写主导词默认尺寸**：`{typography.jumbo-feature}`（clamp 80–200px）配 12px 字距。
- **段落正文默认尺寸**：`{typography.body}`（clamp 15–20px）。
- **任何大写眉题 / 标签默认尺寸**：`{typography.section-label}`（12px）字重 700、4px 字距；列表语境用 `{typography.item-label}`（11px）字重 700、3px 字距。
- **任何 Bebas Neue 元素默认字重**：400（唯一可用字重）。
- **正文默认字重**：400，拉页引文 300。
- **标签默认字重**：600 或 700。
- **英雄统计数字默认尺寸**：`{typography.stat-numeral}`（clamp 48–96px）。
- **卡内统计数字默认尺寸**：`{typography.card-stat}`（clamp 36–56px）。

拿不准时，页面主要文字瞬间取 `{typography.section-headline}`。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个 Bebas Neue 元素都用原生大写。** 系统里不存在句首大写的 Bebas Neue，字面本身不支持。这是系统最基础的排印规则。
- **每个 Bebas Neue 元素都带至少 1px 字距。** 标准标题 2px，hero-title 4px，jumbo-feature 12px。没字距的 Bebas 读起来像没处理过。
- **每个 Inter 标签、眉题、元文字都大写、1–4px 字距。** 分节标签 4px、项目标签 3px、bar-meta 2px、侧栏标签 1px。没有字距的 Inter caps 会破掉编辑语域。
- **每个 Bebas 标题都按表面对比渲染成 `{colors.black}`、`{colors.cream}` 或 `{colors.coral}`，绝不用灰。** 配色选择：奶油/珊瑚上墨、墨上奶油、奶油上需要强调时珊瑚。
- **每个分节眉题**在奶油或墨上渲染成 `{colors.coral}`，在珊瑚上渲染成 `{colors.black}`。珊瑚压珊瑚不存在。
- **珊瑚区域内每个超大装饰数字都渲染成 `rgba(0, 0, 0, 0.12)`**，壁纸数字签名，以全不透明度坐在主内容后方。
- **珊瑚区域内每个巨型装饰标记（引号、单字符）都渲染成 `rgba(0, 0, 0, 0.35)`**，半装饰半内容。
- **拉页引文正文用 Inter 字重 300，不用 Bebas。** 这是系统主要的"声部破口"：内容需要显得私人而非宣告时，交给 Inter Light。

### 排印原则
Bebas 大写宽字距 + Inter 混合字重的组合是系统的声部。换掉任一款字面（标题用别的展示无衬线、正文用 Bebas）都会彻底破掉系统。不出现斜体，不出现下划线。强调机制只有字重（Bebas 主导）、大小写（Bebas + 标签始终大写）、颜色（奶油表面上珊瑚）、表面反色（把元素放进不同区域）。

行高在尺度顶端一律收紧：Bebas 元素 0.9–1.0，Inter 正文 1.6–1.7。展示压缩 + 松正文，给系统带来杂志海报的节奏。

## 布局

### 画布系统
画布是 `100vw × 100vh`，全视口、溢出隐藏。每张 `.slide` 绝对定位铺满视口，同一时刻一张带 `.active`（opacity 1、visibility visible）。过渡是 0.6s opacity + visibility 淡入。

系统**没有通用外壳条**。每页是自带内边距、区域结构、色彩处理的自足构图。导航逐页设置（导航箭头 + 导航点 + 页码），以 `.dark` 变体浮在激活表面上供奶油表面使用。

### 内边距与间隙比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-y}` | clamp(40px, 6vh, 80px) | 标准纵向幻灯片内边距 |
| `{spacing.pad-x}` | clamp(40px, 8vw, 100px) | 标准横向幻灯片内边距 |
| `{spacing.pad-y-tight}` | clamp(28px, 4.5vh, 60px) | 紧凑纵向内边距（封面底段） |
| `{spacing.pad-col}` | clamp(32px, 4vw, 60px) | 区域内栏目内边距 |
| `{spacing.gap-grid}` | 32px | 栏目网格间隙 |
| `{spacing.gap-md}` | 40px | 图表容器内部间隙 |
| `{spacing.card-pad}` | clamp(24px, 3vh, 40px) | 卡片内部内边距 |
| `{spacing.bar-pad}` | clamp(24px, 4vh, 40px) | 信息条内部内边距 |

### 区域构图
Coral 主要的布局手法是**多表面构图**。页面切成若干实色区域，区域之间的边界定义布局。标准切分包括：
- `grid-template-rows: 32% 68%`：顶部强调条 + 主体（封面构图）。
- `grid-template-rows: 1fr auto`：大特写区域 + 底部信息条。
- `grid-template-columns: 1fr 1fr`：均等纵向切分（常珊瑚左 + 墨右）。
- `grid-template-columns: 40% 60%`：窄强调列 + 宽内容列（引文布局）。
- 单表面页：奶油或墨作整张画布（陈述、三栏、时间轴布局）。

区域之间的边界始终是**硬色边**：交界的软过渡、跨边界渐变、交界圆角都没有。两块实色相接就是布局结构。

## 纵深与层级

### 平中带硬色边
Coral 没有投影、没有柔和抬升、没有圆角表面。每个元素落在单一平面。

纵深信号全是结构性的：
- **硬色区域边界**：主结构信号。
- **强调边框**：卡片 5px 珊瑚顶、侧栏块 4px 珊瑚左、时间轴线 4px 墨横、标题线 15% 不透明度 3px 墨。
- **45° 对角斜纹**：6% 不透明度黑色对角重复线性渐变叠在珊瑚区域上，造纹理而不造纵深。
- **装饰壁纸排印**：12% 不透明度超大数字与 35% 不透明度巨型标记，坐在主内容后方作壁纸，不用 z-index 技巧就造出层次。

引入 box-shadow、抬升卡片或柔和渐变，会破掉定义系统的平民海报美学。

### 氛围斜纹变体
45° 对角斜纹是系统主要的氛围处理，但会出现几种步长/角度变体：
- **45°、20/40px 步长**，6% 不透明度黑：标准珊瑚区域叠层。
- **-45°、30/60px 步长**，6% 不透明度黑：珊瑚引文左面板变体。
- **90° 竖向、60/62px 步长**，10% 不透明度黑：珊瑚渐变特写区域叠层。

所有斜纹都微妙（6–10% 不透明度黑），提供纹理而不与内容相争。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 50%（圆） | 仅圆形元素：`nav-dot`（10px）、`nav-arrow`（44px）、`t-point-dot`（20px 时间轴节点） |
| 0 | 其余一切：每个区域、每张卡片、每个侧栏块、每个图标方块、每张图表、每条强调线、每条强调边 |

系统**只用两种半径值**：50%（正圆）或 0（尖角矩形）。柔和圆角不存在。卡片、图标方块、信息条、特写区域都是严格矩形。

### 边框粗细
- **5px 实线 `{colors.coral}`（顶）**：卡片顶边（栏目卡片模式）。
- **4px 实线 `{colors.coral}`（左）**：侧栏项左边。
- **4px 实线 `{colors.black}`（横）**：时间轴线。
- **4px 实线 `{colors.cream}`（环）**：20px 珊瑚时间轴点周围的光晕。
- **3px 实线 `{colors.black}` 15% 不透明度**：封面英雄标题下的标题线。
- **2px 实线半透明**：导航点与导航箭头边（深表面 rgba(255,255,255,0.3–0.5)，奶油表面 rgba(26,26,26,0.2–0.4)）。

所有边框不是珊瑚、黑、奶油，就是半透明。带边矩形上没有 border-radius。

### 装饰元素类型

**45° 对角斜纹**：`repeating-linear-gradient(45deg, transparent, transparent 20px, rgba(0,0,0,0.06) 20px, rgba(0,0,0,0.06) 40px)`，作珊瑚区域上的 `::before` 伪元素叠层。招牌氛围纹理。变体有 -45°、90° 竖向、不同步长。

**背景数字**：超大 Bebas Neue 数字（clamp 100–200px）、`rgba(0, 0, 0, 0.12)`，放在珊瑚区域内。以全不透明度坐在区域主栏目标题后方，造出层叠的"序数壁纸"效果。

**巨型标记**：超大 Bebas Neue 字符（clamp 140–280px）、`rgba(0, 0, 0, 0.35)`，放在珊瑚区域内。作半装饰半内容元素，通常是引文布局珊瑚左面板上的引号。

**卡片（栏目卡片）**：白填充矩形，唯一的边是 5px 珊瑚顶边。顶部一个 48px 实珊瑚图标方块、一个 Bebas 卡片标题、一段 Inter 卡片正文、底部一个珊瑚卡片统计数字。5px 顶边是唯一外壳，没有别的边、没有阴影、没有半径。

**侧栏项**：白填充矩形，唯一的边是 4px 珊瑚左边。装一个 Bebas 侧栏数值和一个 Inter 侧栏标签。4px 左边是唯一外壳。

**图标方块**：48px 实珊瑚矩形（无半径），内含一个白色 Bebas 字形。用作卡片标记。

**信息条**：横跨区域满宽的 flex 行，左 Bebas 条标题、右大写 Inter 条元文字。奶油背景，作特写区域下方的页脚带。

**时间轴**：4px 实线墨横线横跨时间轴宽度，`::after` 重复线性渐变叠层（20px 墨 + 10px 透明）造虚线效果。时间轴点是 20px 珊瑚圆配 4px 奶油光晕，沿线均分。

**强调线**：80×4 实珊瑚矩形，作副标题下的强调线；收尾/引文语境用 60×4。始终珊瑚，始终实色，无半径。

**标题线**：满宽 3px 实线墨、15% 不透明度，作封面英雄标题下微妙的横向分隔。

**锯齿层**：SVG 锯齿图案，以低不透明度细墨线渲染，装饰性叠在封面珊瑚顶段上。

**图案叠层**：另一层重复图案叠层（通常 10% 不透明度墨的 90° 竖向斜纹），用于珊瑚渐变特写区域。与标准 45° 对角斜纹不同。

## 该做与不该做

### 该做
- 把页面构图成多表面区域切分，珊瑚、墨、奶油以硬色边相接。区域边界就是布局结构。
- 每个 Bebas Neue 元素都用原生大写、至少 1px 字距：标准标题 2px、英雄标题 4px、巨型特写 12px。
- 奶油与墨表面上，每个分节眉题用 `{colors.coral}` 大写 Inter 字重 700、3–4px 字距。
- 把 45° 对角斜纹（6% 不透明度黑、20/40px 步长）作 `::before` 叠层套在珊瑚区域上，作氛围纹理。
- 卡片用 5px 珊瑚顶边、侧栏块用 4px 珊瑚左边，作这些元素唯一的外壳，不配别的边、不配阴影、不配半径。
- 区域需要比标题独撑更多的视觉分量时，在珊瑚区域内栏目标题后方放 12% 不透明度的超大装饰 Bebas 数字。
- 墨表面引文布局的拉页引文正文用 Inter 字重 300（light），更轻的字重对着 Bebas 主导形成反差。
- 珊瑚表面上的 Bebas 标题用 `{colors.black}`（火上墨）渲染。系统里不存在珊瑚上的白标题。
- 任何图表数据都用珊瑚主系列 + coral-dark 比较系列的约定。
- 48px 实珊瑚图标方块（无半径、单个白 Bebas 字形）作标准卡片标记。

### 不该做
- 不要把 Bebas Neue 渲染成句首大写。这款字面只有大写，那就是全部身份。
- 不要渲染没字距的 Bebas。没字距的 Bebas 即便放到很大也读起来像没处理过。
- 不要引入第四种表面色。三表面（珊瑚 / 墨 / 奶油）就是系统，加黄或蓝区域会破掉杂志海报身份。
- 不要把标题渲染成 `{colors.gray}`。标题是墨、奶油或珊瑚，灰只留给正文与元文字。
- 不要加投影、抬升卡片或圆角表面。系统是平的，纵深来自色区切分与强调边。
- 不要给任何矩形元素加圆角。卡片、侧栏块、信息条、图标方块、强调线全是尖角矩形。
- 不要给 Bebas 换别的无衬线正文搭档。Bebas + Inter 搭配是固定的。
- 不要把 Inter 标签渲染成句首大写。小号 Inter 文字始终大写、1–4px 字距。
- 不要用渐变柔化区域边界（罕见的 135° coral-dark → coral 特写渐变除外）。区域边是硬色相接。
- 不要往珊瑚区域里塞稀疏内容。珊瑚要有分量，要么把区域构图填满，要么用超大装饰数字 / 巨型标记作壁纸。

## 响应式行为

Coral 是视口流式的 1920×1080 演示系统，通篇用 `clamp()`、`min()` 与视口相对单位。源码里没有显式响应式断点，每个尺寸在最小与最大界之间缩放。

### 缩放行为
- 英雄标题通过 `min(120px, 9vw, 13vh)` 缩放，同时受宽高封顶，3 行标题不会在矮笔记本屏上溢出。
- 巨型特写从最小视口 80px 缩放到最大 200px。
- 正文从 15px 缩放到 20px。
- 内边距逐区域通过 `clamp` 缩放。
- 边框、图标方块（48px）、导航点（10px）、导航箭头（44px）、时间轴点（20px）固定不缩放。

### 放映行为
- 用 `ArrowRight` 或 `Space` 前进。
- 用 `ArrowLeft` 后退。
- 导航点浮在右缘，导航箭头在左下，页码在右下。三者都带 `.dark` 变体供奶油表面用（墨半透明填充），珊瑚/墨表面用标准变体（白半透明填充）。
- 激活导航点无论表面都填 `{colors.coral}`。

### 图表
图表用 Chart.js（经 CDN 加载）渲染。主系列用 `{colors.coral}`，比较系列用 `{colors.coral-dark}`。图表样式在 JS 里内联配置，改样式要改 JS，不是改 CSS。

### 打印 / 导出
未明确处理。每页是 100vw × 100vh 块，导出流程应逐页按 1920×1080 截图。45° 斜纹叠层在 PDF 抓取里应能正确渲染。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 推荐中文搭配 | 来源 |
|---|---|---|---|
| 展示 / 标题（Bebas Neue 大写 400） | Bebas Neue | 站酷小薇体 ZCOOL XiaoWei | Google Fonts |
| 正文 / 标签（Inter 300–700） | Inter | 悠哉字体 Yozai | cn-fontsource CDN |

### 混排策略

用**策略 A — 单字体栈带回退**：在同一条 `font-family` 栈里把 ZCOOL XiaoWei 声明在 Bebas Neue **之后**、Yozai 声明在 Inter **之后**，这样拉丁字形渲染成 Bebas / Inter，CJK 字形自动落到中文字面。每个角色一条 CSS 规则，无需手动切类。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300..700&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-yozai-regular/font.css" rel="stylesheet">
```

```css
:root {
  --font-display: "Bebas Neue", "ZCOOL XiaoWei", sans-serif;
  --font-body: "Inter", "Yozai", sans-serif;
}
```

### 通用 CJK 调整

- **行高**：把 CJK 正文行高提到约 1.8（从 1.7 上调），汉字比拉丁小写需要更多纵向呼吸，而 Coral 的正文已偏爱宽裕行距。
- **字距**：把汉字段上的 `letter-spacing` 清零（Bebas 的 1–12px 字距与 Inter 的 1–4px 字距会打碎汉字节奏）。重字距只保留在拉丁 span 上。
- **文字变换**：任何标签/眉题/元文字是汉字时，去掉 `text-transform: uppercase`。中文没有大小写；强制大写对汉字无效，却会破坏里面混排的拉丁缩写的渲染。
- **标点**：中文句子用中文全角标点（，。：；「」），拉丁用半角（`,.:;""`）。绝不把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略末尾的 。，展示字符串里要去掉。
- **盘古之白**：相邻的汉字与拉丁/数字串之间插入一个细空格（或普通空格），例如 `2026 年`、`AI 产品`，提升混排可读性。
- **一句一款字体**：不要在句中切换 CJK 字族。按角色在 ZCOOL XiaoWei 或 Yozai 里挑一款给某段文字，绝不在同一短语里两款都用。

### 美学提示

ZCOOL XiaoWei 承载 Bebas Neue 为拉丁提供的杂志海报声部，它高窄的汉字形态有相近的建筑展示语域，在 Coral 用于巨型特写的 80–200px 尺寸下能撑住形状，不像系统汉字那样散架。关键是，Bebas Neue"只大写配重字距"的规则对汉字毫无意义（没有大小写、没有字距），所以系统最基础的排印规则对 CJK 直接不适用：去掉字距、去掉大写，让 ZCOOL XiaoWei 单靠尺寸立住。Yozai 与 Inter 搭档作正文和标签，圆润的人文形态贴合 Inter 的暖意，在珊瑚 / 奶油 / 墨表面里仍清晰。三表面区域切分、45° 对角斜纹、超大装饰数字（可以保留拉丁，01、02、03 作中文栏目标题背后的壁纸完全成立）、5px 珊瑚顶边都与内容无关，任何语言里表现一致。

### 已知 CJK 缺口

ZCOOL XiaoWei 是单字重展示字面，相比 Noto 家族字形覆盖有限，生僻或技术汉字（罕见姓氏、古字、GB2312 之外的仅简体变体）可能回退到系统字体。繁体中文文稿把 Yozai 换成 `LXGW WenKai TC`（Google Fonts），它繁体覆盖更全。Bebas Neue 的窄紧缩比例没有精确的中文对应，ZCOOL XiaoWei 顶多算中等紧缩，中文英雄标题会比拉丁对应多占约 20% 横向空间。调整断行（通常 2 行中文标题填满 3 行英文 hero-title 的同一块区域），中文标题偏长时考虑抬高 hero-title 的 `min()` 上限。

## 迭代指南

1. 每张新页都是一到三块表面区域（珊瑚、墨、奶油）以硬边相接的构图。按内容强调挑表面切分。
2. 每个新标题都用 Bebas Neue 大写、至少 1–2px 字距。别句首大写，别不带字距。
3. 每个新分节眉题都用 Inter 字重 700 大写、4px 字距，奶油/墨上 `{colors.coral}`，珊瑚上 `{colors.black}`。
4. 每张新卡片都用 5px 珊瑚顶边 + 白填充 + 无阴影 + 无半径模式。
5. 每个新侧栏块都用 4px 珊瑚左边 + 白填充 + 无半径模式。
6. 每个新珊瑚区域都带 45° 对角斜纹叠层（6% 不透明度）作纹理。
7. 显得分量不足的新珊瑚区域，在主标题后方放 12% 不透明度的超大装饰 Bebas 数字作壁纸。
8. 新图表系列用珊瑚 + coral-dark，别引入额外系列色。
9. 新引文布局把珊瑚左面板（带 35% 不透明度巨型标记）与墨或奶油右面板（承载 Inter 字重 300 的引文正文）配对。
10. 系统有三表面和一种强调（珊瑚）。别引入第四表面色或第二强调色。

## 已知缺口

- Chart.js 库经 CDN 加载，图表样式在 JS 里内联配置而非读 CSS 变量，改样式要改 JS。
- 45° 对角斜纹步长值（标准 20px/40px、变体 30px/60px、竖向 60px/62px）按每次用法硬编码，没有参数化斜纹组件。
- 超大装饰数字以内联内容、硬编码数值摆放，没有生成式序数系统。
- 封面构图的 SVG 锯齿层是嵌在源码里的内联 SVG，调整锯齿图案要改 SVG 标记。
- 时间轴线的虚线效果经 `::after` 重复线性渐变叠层渲染，而非 `border-style: dashed`，这样能精确控制虚线尺寸，但做法不寻常。
- 封面构图用 `min(120px, 9vw, 13vh)` 三重封顶，防止 3 行标题在矮笔记本上溢出，新封面变体应遵循同样的多轴封顶模式。
- 拉页引文布局用 Inter 字重 300，这个字重显式加载了但别处未用，是系统唯一的 Inter Light 部署。
- `cream-dark` 与 `light-gray` 调色板 token 已定义但源码里用得省，可供需要额外中性深浅的新构图使用。
- 奶油表面页必须手动给导航点与导航箭头套 `.dark` 变体以保可见，没有自动表面检测。
- 线性渐变特写区域（135° coral-dark → coral）是系统唯一刻意的渐变，其余表面都是平色。在别处用渐变会破掉平表面美学。
