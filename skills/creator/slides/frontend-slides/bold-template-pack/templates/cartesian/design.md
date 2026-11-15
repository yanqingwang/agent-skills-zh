---
version: alpha
name: Cartesian
description: A quiet, museum-catalog editorial system built on Playfair Display serif headlines, Inter sans body, and a five-tone warm-stone palette. The aesthetic is "consulting deck meets architectural monograph" — minimal geometric line decorations (thin circles, dashed arcs, vertical and horizontal hairlines) drift behind content, suggesting drafting paper and compass work. Every divider is a single 1px line in a muted taupe; nothing is bold, nothing is loud. The cultural reference is Massimo Vignelli's editorial work, the Cooper Hewitt catalog, and pencil-and-tracing-paper urban planning documents.

colors:
  bg-primary: "#EDE8E0"
  bg-secondary: "#E2DBD1"
  text-primary: "#1A1A1A"
  text-secondary: "#5A5A5A"
  accent: "#8A8178"
  line: "#B8B0A4"
  white-overlay: "rgba(255, 255, 255, 0.3)"

typography:
  display:
    fontFamily: "Playfair Display, serif"
    fontSize: "clamp(3rem, 6vw, 5.5rem)"
    fontWeight: 400
    lineHeight: 1.1
  h1:
    fontFamily: "Playfair Display, serif"
    fontSize: "clamp(2.5rem, 5vw, 4.5rem)"
    fontWeight: 400
    lineHeight: 1.1
  h2:
    fontFamily: "Playfair Display, serif"
    fontSize: "clamp(1.8rem, 3.5vw, 3rem)"
    fontWeight: 400
    lineHeight: 1.1
  h3:
    fontFamily: "Playfair Display, serif"
    fontSize: "clamp(1.2rem, 2vw, 1.6rem)"
    fontWeight: 400
    lineHeight: 1.1
  stat-figure:
    fontFamily: "Playfair Display, serif"
    fontSize: "2rem"
    fontWeight: 400
    lineHeight: 1
  agenda-numeral:
    fontFamily: "Playfair Display, serif"
    fontSize: "1.5rem"
    fontWeight: 400
    lineHeight: 1
  team-initial:
    fontFamily: "Playfair Display, serif"
    fontSize: "2rem"
    fontWeight: 400
    lineHeight: 1
  quote-mark:
    fontFamily: "Playfair Display, serif"
    fontSize: "5rem"
    fontWeight: 400
    lineHeight: 1
  card-headline:
    fontFamily: "Playfair Display, serif"
    fontSize: "1.3rem"
    fontWeight: 400
    lineHeight: 1.1
  timeline-headline:
    fontFamily: "Playfair Display, serif"
    fontSize: "1.2rem"
    fontWeight: 400
    lineHeight: 1.1
  body:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(0.9rem, 1.2vw, 1.1rem)"
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.6
  subtitle:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(1rem, 1.5vw, 1.3rem)"
    fontWeight: 400
    lineHeight: 1.5
  attribution:
    fontFamily: "Inter, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 2px
    textTransform: uppercase
  label:
    fontFamily: "Inter, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 3px
    textTransform: uppercase
  micro:
    fontFamily: "Inter, sans-serif"
    fontSize: "0.7rem"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
    textTransform: uppercase

spacing:
  pad-y: "4vh"
  pad-x: "4vw"
  gap-xl: "6vw"
  gap-lg: "5vw"
  gap-md: "3vw"
  gap-sm: "2vh"
  card-pad: "4vh 2vw"

canvas:
  width: 100vw
  height: 100vh

components:
  card:
    border: "1px solid {colors.line}"
    padding: "{spacing.card-pad}"
    background: "{colors.white-overlay}"
    description: "Tracing-paper card — 1px taupe outline with semi-transparent white fill that lets the canvas tone bleed through. No radius, no shadow."
  card-icon:
    width: 40px
    height: 40px
    border: "1px solid {colors.line}"
    borderRadius: "50%"
    color: "{colors.accent}"
    fontSize: "1rem"
    description: "Small ringed circle (40px) containing a 1–3 character Roman numeral or letter in accent taupe."
  agenda-row:
    padding: "2vh 0"
    borderBottom: "1px solid {colors.line}"
    description: "List row separated only by a 1px taupe hairline. Numeral at left, label at right."
  timeline-rule:
    height: "1px"
    background: "{colors.line}"
    description: "Single horizontal 1px taupe line connecting timeline items. No nodes, no markers — just the line."
  vertical-line:
    width: "1px"
    height: "100%"
    background: "{colors.line}"
    opacity: 0.3
    description: "Optional decorative vertical hairline anchored at left edge (default 8vw from edge) at low opacity. Provides drafting-paper grid feel."
  horizontal-accent:
    width: "20vw"
    height: "1px"
    background: "{colors.text-primary}"
    description: "Single short ink-black 1px horizontal line used as a strong accent rule. Black, not taupe."
  geo-circle:
    border: "1px solid {colors.line}"
    borderRadius: "50%"
    opacity: 0.5
    description: "Thin solid taupe ring at low opacity, used as decorative geometry behind content."
  geo-arc:
    border: "1px dashed {colors.line}"
    borderRadius: "50%"
    opacity: 0.3
    description: "Thin dashed taupe ring at very low opacity, paired with geo-circle to suggest compass construction."
  geo-decoration:
    border: "1px solid {colors.line}"
    borderRadius: "50%"
    description: "Large decorative ring (30–50vw diameter) anchored to a corner or center. Always pairs with a ::before pseudo-element rendering a smaller dashed ring inside it, suggesting concentric drafting."
  geo-ring:
    width: "50vw"
    height: "50vw"
    border: "1px solid {colors.line}"
    borderRadius: "50%"
    opacity: 0.3
    description: "The largest geometric decoration variant — a 50vw centered ring with an inner ::before dashed ring at 70% diameter."
  image-placeholder:
    background: "{colors.bg-secondary}"
    border: "1px solid {colors.line}"
    description: "Solid taupe-tinted block with two crossed 1px diagonal hairlines via ::before/::after at +30° and -30°, suggesting an X over a blank frame. Holds a small uppercase label centered."
  team-photo:
    width: "12vw"
    height: "12vw"
    borderRadius: "50%"
    border: "1px solid {colors.line}"
    background: "{colors.bg-secondary}"
    description: "Circular portrait frame (12vw) in slightly darker stone, ringed in taupe, holding a single Playfair initial in accent taupe at center."
  nav-arrow:
    width: 40px
    height: 40px
    border: "1px solid {colors.line}"
    background: "transparent"
    description: "Square 40px button with 1px taupe border holding an arrow glyph. Hover state inverts to ink fill with cream text."
  nav-dot:
    width: 8px
    height: 8px
    borderRadius: "50%"
    background: "{colors.line}"
    description: "Small taupe dot at right edge as navigation indicator. Active state shifts to ink and scales 1.3."
  chart-stroke-primary: "{colors.text-primary}"
  chart-stroke-comparison: "{colors.line}"
  chart-comparison-dash: "5, 5"
  chart-grid-color: "{colors.bg-secondary}"
  chart-axis-tick-color: "{colors.accent}"
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/cartesian/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Cartesian 是一套**安静的博物馆图录式编辑系统**。定义性前提是**以 1px 线克制**：每个结构元素（列表分隔、议程线、时间轴连线、卡片边、表格分隔）都是一条单一 1px 的柔和灰褐线 `{colors.line}`。没有粗边、没有填充、没有阴影、没有圆角表面。层级靠字面反差与负空间搭起，常规意义上的纵深并不存在。

字面栈是文学专著式搭配。**Playfair Display**，受迪多尼影响的高对比衬线，承载每个标题、每个统计数字、每个卡片标题、每个团队首字母、每个引号。Playfair 几乎只跑字重 400（常规），系统里不用粗体或 700 字重的 Playfair。细笔画的迪多尼美学靠让字形在适中字重下呼吸。**Inter**，干净的现代怪诞体，承载每个正文段落、每个副标题、每个标签、每个出处。Inter 正文用 400、标签用 500。这个搭配造出系统的编辑声部：衬线陈述 + 干净无衬线辅助结构。

配色是**五种暖石色加墨**。画布是 `{colors.bg-primary}`，暖砂岩米白。略深的石色 `{colors.bg-secondary}` 提供微妙的区域区隔（图片占位、团队照片框）。墨色 `{colors.text-primary}` 是标题色，中灰 `{colors.text-secondary}` 是正文。更暖的灰褐 `{colors.accent}` 承载标签、出处、小数字。最浅的灰褐 `{colors.line}` 是通用 1px 线色。没有平民化意义上的强调色，没有红、没有橙、没有蓝。配色就是石、石、石、墨、墨。系统里唯一的"颜色"是字面对比。

纵深**在常规意义上完全缺席**。没有阴影、没有抬升卡片、没有圆角表面、没有渐变。氛围由**几何线装饰**造出：`{colors.line}` 里 20–50% 不透明度的细实线与虚线圆，像用圆规画在描图纸上一样漂在内容后方。它们不造层级，只造情绪。装饰几何传递"打过草稿、推敲过、精确"。

**密度取向：稀疏、能呼吸。** Cartesian 稀疏时优雅，拥挤时散架。构图正确的一页，配一个 Playfair 标题加一段正文，或一张图表加一句短图注，由宽裕负空间框住。多数页用居中或不对称双栏布局，`5–6vw` 栏间距、显著的纵向呼吸。装饰圆规弧线强化稀疏：周围有空间时它们最有效。塞得满满当当、顶到边的页在这套系统里就是坏了；正确的密度是"一个清楚的想法，框得妥帖，落在石纸上"。

**关键特征：**
- 暖砂岩画布 `{colors.bg-primary}`，单 1px 灰褐 `{colors.line}` 分隔线作通用结构元素。
- Playfair Display 衬线字重 400 用于每个标题/数字/引号；Inter 无衬线用于每个正文/标签/出处。
- 五调单色配色：两石、两灰、一墨。哪里都没有鲜艳强调色。
- 装饰几何环（细实线 + 虚线圆，20–50% 不透明度）漂在内容后方，作圆规打稿的氛围。
- 每个标签、出处、微型文字都是大写 Inter 配 2–3px 字距。
- 所有边框都是 1px 细线，没有元素带更粗的边、阴影或圆角填充。
- 右边缘竖向导航点列、左下方形导航箭头按钮、右下等宽页码。
- 图片占位带一对交叉的 1px 对角线（一个 X），压在石色块上，是签名手法。

## 颜色

### 石与墨配色
- **Background Primary**（`{colors.bg-primary}` — #EDE8E0）：画布。暖砂岩米白，更像"马尼拉文件夹"而非"白纸"。默认幻灯片背景。
- **Background Secondary**（`{colors.bg-secondary}` — #E2DBD1）：略深的石色，用于图片占位、团队照片框，以及任何需要从画布上微妙分开、又不用彩色填充或边框的区域。
- **Text Primary**（`{colors.text-primary}` — #1A1A1A）：近黑墨。用于标题、统计数字，以及特别的 `{components.horizontal-accent}` 线。系统里对比最强的颜色。
- **Text Secondary**（`{colors.text-secondary}` — #5A5A5A）：中暖灰。用于所有正文段落文字。比墨柔，可读但往后退。
- **Accent**（`{colors.accent}` — #8A8178）：暖灰褐。用于标签、出处、议程数字、页码、卡片图标文字、团队成员角色文字。系统的"小文字"色。
- **Line**（`{colors.line}` — #B8B0A4）：浅灰褐。通用 1px 线色：卡片边、议程线、时间轴连线、团队照片环、导航箭头边、几何装饰环。

### 默认值
- **默认表面背景**：`{colors.bg-primary}`。
- **默认标题色**：`{colors.text-primary}`，始终墨色，绝不上彩，绝不用强调灰褐。Playfair 标题一律墨色。
- **默认正文文字色**：`{colors.text-secondary}`（中暖灰）。
- **默认标签 / 出处 / 微型文字色**：`{colors.accent}`（暖灰褐）。
- **默认边框色**：`{colors.line}`，每条 1px 结构边。除罕见的 `horizontal-accent` 线外，绝不用墨黑做边。
- **默认次级表面填充**：`{colors.bg-secondary}`。
- **默认图表主系列色**：`{colors.text-primary}`（墨）。
- **默认图表比较/次级系列色**：`{colors.line}` 配 5px 虚线描边。
- **默认图表网格色**：`{colors.bg-secondary}`。
- **默认图表轴刻度色**：`{colors.accent}`。

Cartesian **没有平民化意义上的强调色**。红色标注、蓝色条、绿色统计，这些都不存在。需要强调时，放大字号、从无衬线切到衬线，或加一条墨色 1px `horizontal-accent` 线。颜色在这套系统里不是强调机制，克制才是。

## 排印

### 字族
系统跑在**两字面对话**上：`Playfair Display`（衬线，字重 400/600/700，有斜体）承载每个标题、统计数字、引号、卡片标题、团队首字母；`Inter`（无衬线，字重 300/400/500/600）承载每个正文、副标题、标签、出处、微型文字。没有第三字面。

Playfair Display 几乎只用在**字重 400（常规）**。系统刻意避开粗 Playfair，迪多尼美学依赖细笔画调制，字重一重就没了。斜体 Playfair 已加载，但默认模板不用，留给正文里的行内强调。

Inter 正文用字重 400、标签与微型文字用 500、罕见的强调行内元素用 600。Playfair 的高调制衬线与 Inter 的均匀无衬线之间的反差，是系统主要的排印节奏。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | clamp(3rem, 6vw, 5.5rem) | Playfair Display | 400 | 封面或大开场标题 |
| `{typography.h1}` | clamp(2.5rem, 5vw, 4.5rem) | Playfair Display | 400 | 分节开场或大收尾标题 |
| `{typography.h2}` | clamp(1.8rem, 3.5vw, 3rem) | Playfair Display | 400 | 页面主标题 |
| `{typography.h3}` | clamp(1.2rem, 2vw, 1.6rem) | Playfair Display | 400 | 区域内的副标题 |
| `{typography.card-headline}` | 1.3rem | Playfair Display | 400 | 卡片或支柱块标题 |
| `{typography.timeline-headline}` | 1.2rem | Playfair Display | 400 | 时间轴步骤或阶段标题 |
| `{typography.stat-figure}` | 2rem | Playfair Display | 400 | 数值统计数字（通常行内放在统计簇里） |
| `{typography.team-initial}` | 2rem | Playfair Display | 400 | 团队照片圆内居中的首字母 |
| `{typography.agenda-numeral}` | 1.5rem | Playfair Display | 400 | 议程行前的序数数字 |
| `{typography.quote-mark}` | 5rem | Playfair Display | 400 | 拉页引文的起始引号字形 |
| `{typography.subtitle}` | clamp(1rem, 1.5vw, 1.3rem) | Inter | 400 | 展示标题下方的副标题段落 |
| `{typography.body}` | clamp(0.9rem, 1.2vw, 1.1rem) | Inter | 400 | 标准段落正文 |
| `{typography.body-sm}` | 0.9rem | Inter | 400 | 卡片或时间轴项内紧凑正文 |
| `{typography.attribution}` | 0.85rem | Inter | 400 | 引文下方出处行，2px 字距 + 大写 |
| `{typography.label}` | 0.75rem | Inter | 500 | 标题上方的分节标签 / 眉题，3px 字距 + 大写 |
| `{typography.micro}` | 0.7rem | Inter | 400 | 图片标签、页码、最小外壳文字 |

### 默认值
- **页面主标题默认尺寸**：`{typography.h2}`（clamp 1.8–3rem）。
- **封面或大开场标题默认尺寸**：`{typography.h1}`（clamp 2.5–4.5rem）；最铺张的封面用 `{typography.display}`（clamp 3–5.5rem）。
- **段落正文默认尺寸**：`{typography.body}`（clamp 0.9–1.1rem）。
- **任何行内标签或眉题默认尺寸**：`{typography.label}`（0.75rem），始终 3px 字距 + 大写。
- **任何 Playfair 标题默认字重**：400。别去取 600 或 700。
- **正文默认字重**：400。
- **标签/微型默认字重**：500。
- **统计簇内统计数字默认尺寸**：`{typography.stat-figure}`（2rem）。Cartesian 没有英雄统计数字模式（没有 5–7rem 的展示统计），统计以适中尺度的行内排位呈现。

拿不准时，页面主要文字瞬间取 `{typography.h2}`，不要用 `{typography.h3}`（后者是区域内的副标题）。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个 Playfair 标题、统计、引文、卡片标题、首字母都设字重 400。** 系统里不存在粗 Playfair。细笔画迪多尼美学就是身份。
- **每个 Playfair 元素都句首大写（专有名词用真正的标题式大写）。** 不用大写 Playfair。
- **每个 Inter 标签、出处、微型文字元素都大写、2–3px 字距。** 标签 3px 字距，出处与微型 2px。没有字距，Inter capitals 读起来像没处理过。
- **每个 Playfair 元素都以 `{colors.text-primary}`（墨）渲染。** 标题绝不用强调灰褐，绝不用灰。例外是圆形 `card-icon` 或 `team-photo` 内的装饰首字母，字形用 `{colors.accent}` 渲染。
- **每条 1px 结构边都用 `{colors.line}`。** 别的边框色不存在，除罕见的墨色 `horizontal-accent` 线外。
- **每张卡片、图片占位、团队照片、导航箭头边都是 1px 实线。** 系统里不存在更粗的边。
- **图表主系列用墨黑，比较系列用灰褐虚线（5px, 5px）。** 这一对是唯一的图表配色规则。

### 排印原则
Playfair-400 + Inter-400 的组合是系统的声部。换掉任一家族、或把 Playfair 跳到字重 700，都会读成另一套设计系统。斜体强调允许通过正文里的行内 `<em>`（Inter 斜体）；斜体 Playfair 已加载但留给罕见用途。不用下划线。

行高保持宽松：标题 1.1，正文 1.6。宽正文行高是呼吸感美学的一部分。

## 布局

### 画布系统
画布是 `100vw × 100vh`，全视口、溢出隐藏。每张 `.slide` 绝对定位铺满视口，同一时刻一张带 `.active`（opacity 1、visibility visible）。过渡是 0.6s 的 opacity + visibility 淡入。

### 内边距与间隙比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-y}` | 4vh | 默认纵向幻灯片内边距 |
| `{spacing.pad-x}` | 4vw | 默认横向幻灯片内边距 |
| `{spacing.gap-xl}` | 6vw | 主双栏栏间距（最宽裕） |
| `{spacing.gap-lg}` | 5vw | 标准双栏或网格栏间距 |
| `{spacing.gap-md}` | 3vw | 卡片网格栏间距 |
| `{spacing.gap-sm}` | 2vh | 议程行纵向内边距、出处间距 |
| `{spacing.card-pad}` | 4vh 2vw | 内容卡片内部内边距 |

标题通常带上方标签下来的 2–3vh margin-bottom、下方正文出去的 2vh margin-bottom。3 卡或 4 团队网格上方的分节页眉带 6vh margin-bottom 到网格（显著的呼吸）。

### 装饰几何层
Cartesian 的签名是**描图纸式几何装饰**。每页可叠一个或多个：
- 锚在角落的大 `geo-decoration` 环（通常 30–50vw 直径），带约 80% 直径的内虚线环（`::before` 伪元素）。
- 距左边缘约 8vw、从地面到顶的 `vertical-line`，30% 不透明度。
- 锚在左下 15vh 处的 `horizontal-accent`（一条短黑 1px 线）。
- 收尾或沉思页上居中的 `geo-ring`（50vw 圆）。

这些元素**不带信息角色**，只造氛围。完全没有几何装饰的页是有效的；装饰过度（每页超过两个 geo 元素）会破掉克制。

### 外壳
系统的外壳极简：
- 右边缘竖向列的小 `nav-dot` 指示器（8px 灰褐圆）。
- 左下一对方形 `nav-arrow` 按钮（40×40，1px 灰褐边，透明填充）。
- 右下 `slide-counter` 文字，Inter 0.75rem、2px 字距、`{colors.accent}`。

没有顶部外壳条、没有常驻页眉、没有页脚线。

## 纵深与层级

### 平面（唯一手法）
Cartesian 没有阴影、没有抬升卡片、没有圆角表面、没有渐变。每个元素落在单一平面。

层级来自：
- **字面对比**：Playfair 衬线对 Inter 无衬线，尺寸从 5rem 到 0.7rem 的尺度。
- **1px 细线分隔**：议程行、时间轴线、卡片轮廓、图片占位轮廓、统计顶边、团队照片环、导航箭头边。
- **色调**：墨对灰对灰褐。
- **负空间**：每个元素周围宽裕内边距。
- **几何氛围**：内容后方圆规打稿般的环，暗示纵深而不真的造出纵深。

引入 `box-shadow`、抬升卡片或柔和渐变，会破掉定义系统的克制。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 50%（圆） | 每个圆形元素：`card-icon`（40px）、`team-photo`（12vw）、`nav-dot`（8px）、`geo-circle`、`geo-arc`、`geo-decoration`、`geo-ring` |
| 0 | 其余一切：卡片、图片占位、导航箭头、议程行、时间轴、统计块、图表容器 |

系统**只用两种半径值**：50%（正圆）或 0（尖角矩形）。柔和圆角不存在。

### 边框粗细
- **1px 实线 `{colors.line}`**：通用结构边。用于每张卡片、图片占位、团队照片环、导航箭头、议程行底边、时间轴线、统计顶边、geo-circle、geo-decoration。
- **1px 虚线 `{colors.line}`**：用于 `geo-arc`，以及 `geo-decoration` / `geo-ring` 内的内 `::before` 环。虚线提示"构造线 / 弧"。
- **1px 实线 `{colors.text-primary}`**：只用于罕见的 `horizontal-accent` 装饰线。系统唯一的墨黑线。
- **图表条/线描边宽度**：Chart.js 系列 1px（条边）、2px（线系列）。比较系列 2px 虚线（5px 实、5px 空）。

所有结构边都是 `{colors.line}`。更粗的边、彩色边、虚线结构边（geo 弧除外）都不存在。

### 装饰元素类型

**几何环（geo-circle / geo-decoration / geo-ring）**：各种尺寸（10vw、30vw、50vw）、20–50% 不透明度的细 1px 灰褐圆。通常配一个外径 70–80% 的内虚线 `::before` 环，暗示圆规作图里同时有主圆和偏置弧。锚在角落或中心，以 `z-index: 0`、`pointer-events: none` 坐在内容后方。

**竖线**：单条 1px 灰褐列，锚在距左页边约 8vw 处，从地面到顶，30% 不透明度。暗示描图纸的对齐辅助线。每页可选。

**横向强调**：单条 20vw × 1px 黑线，锚在页面左下 15vh 处。系统唯一的墨黑线，作封面或收尾布局上强收尾强调线。用得省。

**图片占位**：一块实色 `{colors.bg-secondary}` 块，两条 150% 对角 1px 灰褐线以 +30° 和 -30° 经 `::before` / `::after` 交叉成一个 X。中央一个小大写 Inter 标签（"Visual Reference" 或类似）。X 图案是图片未接时的签名处理。

**团队照片框**：12vw 圆形 `{colors.bg-secondary}` 块，1px 灰褐环，中央一个 2rem 的 Playfair-400 首字母，`{colors.accent}`。用作肖像占位。

**卡片**：1px 灰褐边的块，内部半透明白填充（`{colors.white-overlay}`），让画布色调微微透出。正是这层淡白填充把卡片与光区域区分开，去掉填充卡片就消失了。

**议程行**：flex 行，左边一个 `{colors.accent}` 的 Playfair `{typography.agenda-numeral}`，右边一个标签，2vh 内边距、1px 灰褐底边。叠起来的行构成议程列表。

**时间轴**：一排均分时间轴项上方一条 1px 灰褐顶边；每项带一个灰褐的小 Inter `year` 标签、一个 Playfair `{typography.timeline-headline}`、一段 Inter 正文。细线是时间轴唯一的结构，没有节点、没有标记、没有圆点。

**统计簇**：由 `gap-md` 分隔的一排统计项，以 1px 灰褐顶边框住，装行内 `{typography.stat-figure}` Playfair 数字，下方灰褐的小大写 Inter 标签。

**引号**：5rem 的 Playfair 引号字形，50% 不透明度灰褐，放在 Playfair `{typography.h2}` 标题 + 下方小大写灰褐出处之上。

**图表**：Chart.js 条形或折线图，墨黑主系列、灰褐虚线比较系列。网格线用 `{colors.bg-secondary}`，轴刻度用 `{colors.accent}`。主系列始终不填充（折线图可用 5% 墨色淡填充）。

## 该做与不该做

### 该做
- 每个结构分隔都用一条 1px 的 `{colors.line}` 线：议程线、时间轴连线、卡片边、统计顶边、团队照片环。1px 细线是 Cartesian 的身份。
- 每个 Playfair 标题、统计、引号、卡片标题都设字重 400。别取粗体，细笔画迪多尼美学靠它。
- 每个标题都用 `{colors.text-primary}`（墨）渲染。Playfair 绝不出现在灰褐或彩色里。
- 每个标签、出处、议程数字、微型文字都用 `{colors.accent}`（灰褐）、大写 + 2–3px 字距。
- 在内容后方叠装饰几何环（实线 + 虚线）、20–50% 不透明度作氛围。每页一到两个 geo 元素，绝不多。
- 把 Playfair Display（衬线标题）与 Inter（无衬线正文）配对。两字面搭配是固定的。
- 图片占位内用交叉对角 X 图案。这是系统签名占位处理。
- 让页面呼吸，宽裕负空间的稀疏布局才是正确密度。
- 图片占位与团队照片框用 `{colors.bg-secondary}` 作填充，是微妙石色，不是白，不是灰。
- 单条 `horizontal-accent`（20vw × 1px 墨线）省着用，作封面或收尾构图上的强收尾线。

### 不该做
- 不要引入平民化强调色。没有红、橙、蓝、绿。配色是石压石，标题用墨。
- 不要把 Playfair 标题渲染成 `{colors.accent}`（灰褐）。标题是墨，灰褐只留给小文字。
- 不要把任何 Playfair 元素加粗。字重 400 是常驻规则，粗体会破掉迪多尼美学。
- 不要加阴影、抬升卡片或渐变填充。Cartesian 是平的，纵深来自几何与文字，不来自 z 轴。
- 不要在卡片或矩形上用圆角。唯一的圆是正圆（半径 50%）。
- 不要用粗边（2px+）。每条结构边都是 1px。
- 不要把页面塞满。稀疏、能呼吸的布局读起来优雅，塞满的布局读起来像坏了。
- 不要给 Playfair 换别的无衬线搭档。Inter 搭配是固定的。
- 不要把标签或微型文字渲染成句首大写。小号 Inter 文字始终大写 + 2–3px 字距。
- 不要每页加超过两个 geo 装饰。克制是规则，装饰过度读起来杂乱。

## 响应式行为

Cartesian 是视口流式的 1920×1080 演示系统，通篇用 `vw` / `vh` 单位与 `clamp()`。有一个 `@media (max-aspect-ratio: 4/3)` 断点把双栏网格收成单栏、隐藏时间轴线（堆叠后失去意义）、并把团队与卡片网格纵向堆叠。其余部分无断点响应式。

### 缩放行为
- 展示标题经 `clamp()` 从最小视口 2.5rem 缩放到最大 5.5rem。
- 正文从 0.9rem 缩放到 1.1rem。
- 内边距用随视口线性缩放的 `vh` / `vw` 单位。
- 1px 边、8px 导航点、40px 导航箭头固定不缩放。

### 放映行为
- 用 `ArrowRight` 或 `Space` 前进。
- 用 `ArrowLeft` 后退。
- 右边缘导航点可点击跳转到指定页。
- 左下导航箭头可点击，悬停态把背景反成墨色、文字反成奶油。
- 右下页码以两位数补零显示 当前 / 总数。

### 图表
图表用 Chart.js（经 CDN 加载）渲染。源码里的两种图表是条形和折线，都遵守墨主系列 / 灰褐虚线比较系列的约定。自定义字体设置把 Inter 注入 Chart.js 的标签渲染。

### 打印 / 导出
未明确处理。每页是 100vw × 100vh 块，导出流程应逐页按 1920×1080 截图。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 推荐中文搭配 | 来源 |
|---|---|---|---|
| 展示 / 标题（Playfair Display 400） | Playfair Display | 思源宋体 Noto Serif SC 700 | Google Fonts |
| 正文 / 标签（Inter 400–500） | Inter | 思源宋体 Noto Serif SC 400 | Google Fonts |

### 混排策略

用**策略 A — 单字体栈带回退**：在同一条 `font-family` 栈里把 Noto Serif SC 声明在拉丁字体**之后**，这样拉丁字形渲染成 Playfair / Inter，CJK 字形自动落到 Noto Serif SC。每个角色一条 CSS 规则，无需手动切类。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..700;1,400..700&family=Inter:wght@300..600&family=Noto+Serif+SC:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --font-display: "Playfair Display", "Noto Serif SC", serif;
  --font-body: "Inter", "Noto Serif SC", sans-serif;
}
/* Headlines use Noto Serif SC 700; body uses Noto Serif SC 400. */
```

### 通用 CJK 调整

- **行高**：把 CJK 正文行高提到约 1.75（从 1.6 上调），汉字比拉丁小写需要更多纵向呼吸，而 Cartesian 本就偏爱宽裕行距。
- **字距**：把汉字段上的 `letter-spacing` 清零。2–3px 字距只保留在大写拉丁标签上。
- **文字变换**：任何标签/出处/微型文字是汉字时，去掉 `text-transform: uppercase`。中文没有大小写；强制大写对汉字无效，却会破坏里面混排的拉丁缩写的渲染。
- **标点**：中文句子用中文全角标点（，。：；「」），拉丁用半角（`,.:;""`）。绝不把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略末尾的 。，展示字符串里要去掉。
- **盘古之白**：相邻的汉字与拉丁/数字串之间插入一个细空格（或普通空格），例如 `2026 年`、`AI 产品`，提升混排可读性。
- **一句一款字体**：不要在句中切换 CJK 字族。某段文字挑 Noto Serif SC 的单一字重，绝不在同一短语里用两个。

### 美学提示

Noto Serif SC（思源宋体）是唯一具备 Cartesian 所需克制编辑语域的主流汉字衬线，它横细竖粗的调制笔画呼应 Playfair 的迪多尼美学，均匀齐整的节奏贴合 Cartesian 的"博物馆图录"声部。标题用 NSC 字重 700 保住拉丁展示的视觉分量，NSC 400 承载正文，带着 Inter 所提供的那份安静暖意。五石配色能干净地吸收汉字，因为每个字形都落在墨或灰褐里，没有糖果填充要协商。装饰圆规弧线几何层与内容无关，任何语言里表现一致。避免加粗汉字（相当于 Cartesian"不粗 Playfair"规则的中文排印版本），靠尺寸与 1px 线分隔搭层级。

### 已知 CJK 缺口

系统只加载了 Noto Serif SC 这一款汉字衬线，它没有斜体轴（汉字排印历史上没有斜体），于是正文落到 NSC 时，罕见的斜体 Playfair `<em>` 瞬间会丢掉强调。可把一个单字 span 染成 `{colors.accent}`（灰褐），或把强调短语包进淡淡的「」，以找回强调。NSC 700 是可用的最重字重，系统"以 400 字重克制"的规则自然延伸到中文，所以这个缺口在实践中很少出现。

## 迭代指南

1. 每个新结构分隔都用 1px 实线 `{colors.line}` 边。没有例外。
2. 每个新标题都用 Playfair Display 字重 400、`{colors.text-primary}`。别加粗，别上色。
3. 每个新小文字元素（标签、出处、微型）都用 Inter 大写、2–3px 字距、`{colors.accent}`。
4. 每个新正文段落都用 Inter 字重 400、`{colors.text-secondary}`、行高 1.6。
5. 每张新卡片都用 1px 灰褐边 + 半透明白叠层填充。无阴影，无半径。
6. 新圆形元素（图标、照片、装饰环）用 border-radius 50% 配 1px 灰褐环。
7. 新几何装饰保持微妙：每页 1 或 2 个、20–50% 不透明度、在内容后方（z-index 0、pointer-events none）。
8. 新图表系列遵守墨主系列 / 灰褐虚线比较系列的约定。别引入彩色图表系列。
9. 新布局遵守呼吸密度规则，Cartesian 里稀胜过密。
10. `horizontal-accent` 20vw 墨线是系统唯一的"墨线"，省着用、作收尾强调，绝不当常规分隔线。

## 已知缺口

- Chart.js 库经 CDN 加载；超出条形和折线的新图表类型，需要手动配置以匹配墨主系列 / 灰褐虚线比较系列的美学。
- 装饰 `geo-decoration` 与 `geo-ring` 的 `::before` 内环图案在 CSS 里硬编码，源码所用之外的尺寸变体需要新增样式规则。
- 团队照片占位在灰褐里显示一个 Playfair 首字母，插入真实肖像要把首字母换成 `<img>` 并调整圆形裁切。
- 图表轴标签色与网格色在 Chart.js options 块里内联硬编码（而非读 CSS 变量），改样式要改 JS，不是改 CSS。
- 图片占位 X 图案（交叉的 +30°/-30° 对角线）经 `::before` / `::after` 以固定 150% 宽度渲染，占位尺寸超出源码范围时可能要重算旋转角才能贴边。
- 斜体 Playfair 已加载但默认规则里未用，可用于正文里的行内 `<em>` 强调，但系统本身不编写任何斜体文字。
- `vertical-line` 与 `horizontal-accent` 装饰元素的位置值硬编码（距左 8vw、距底 15vh），脱离默认位置使用要逐实例覆盖样式。
- 页码的 `currentSlide` / `totalSlides` ID 在 JS 里被引用，但系统没有内部页名登记，新页只按 DOM 顺序递增。
