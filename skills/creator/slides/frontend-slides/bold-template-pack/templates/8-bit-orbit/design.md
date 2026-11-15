---
version: alpha
name: 8-Bit Orbit
description: A retro-futuristic pixel-art presentation system that fuses 16-bit arcade nostalgia with editorial discipline. Display type runs in Tektur (a chunky geometric display face built on pixel-grid logic) paired with Chakra Petch for body and Space Mono for code-flavored labels and tabular data. The palette pivots on a deep cosmic navy (`#0F1B3D` / `#0A0E27`) lit by three saturated neons — cyan, hot pink, and a high-key yellow — with a soft lavender pastel for warm reprieves. Depth is built from stacked hard offset shadows in 4px increments (the pixel unit), CRT scanlines, atmospheric grain, vignettes, and animated starfields. The effect sits between an arcade cabinet and a Tron-era boardroom — unmistakably digital, intentionally lo-fi, and engineered to feel as if it just booted up.

colors:
  dark-void: "#0A0E27"
  deep-navy: "#0F1B3D"
  neon-cyan: "#5EDCF4"
  neon-pink: "#F0A6CA"
  neon-yellow: "#F4D03F"
  soft-lavender: "#E2D5F2"
  white: "#FFFFFF"

shadows:
  pixel-stack-cyan-yellow: "4px 0 0 0 {colors.deep-navy}, 0 4px 0 0 {colors.deep-navy}, 4px 4px 0 0 {colors.deep-navy}, 8px 4px 0 0 {colors.neon-yellow}, 4px 8px 0 0 {colors.neon-yellow}, 8px 8px 0 0 {colors.neon-yellow}"
  pixel-stack-pink-cyan: "4px 0 0 0 {colors.deep-navy}, 0 4px 0 0 {colors.deep-navy}, 4px 4px 0 0 {colors.deep-navy}, 8px 4px 0 0 {colors.neon-cyan}, 4px 8px 0 0 {colors.neon-cyan}, 8px 8px 0 0 {colors.neon-cyan}"
  pixel-l-shape: "4px 0 0 0 {colors.deep-navy}, 0 4px 0 0 {colors.deep-navy}, 4px 4px 0 0 {colors.deep-navy}"
  pixel-text-shadow: "4px 4px 0 {colors.neon-yellow}, 8px 8px 0 {colors.deep-navy}"
  pixel-text-shadow-small: "3px 3px 0 {colors.deep-navy}"
  card-offset: "6px 6px 0 rgba(15, 27, 61, 0.15)"
  card-featured: "8px 8px 0 {colors.neon-yellow}"

typography:
  pixel-hero:
    fontFamily: "'Tektur', cursive"
    fontSize: "clamp(48px, 10vw, 128px)"
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: 0.04em
  display:
    fontFamily: "'Tektur', cursive"
    fontSize: "clamp(32px, 5vw, 64px)"
    fontWeight: 700
    lineHeight: 1.15
  headline:
    fontFamily: "'Tektur', cursive"
    fontSize: "clamp(24px, 3.5vw, 45px)"
    fontWeight: 700
    lineHeight: 1.15
  subhead:
    fontFamily: "'Tektur', cursive"
    fontSize: "clamp(17.6px, 2vw, 24px)"
    fontWeight: 700
    lineHeight: 1.15
  stat-number:
    fontFamily: "'Tektur', cursive"
    fontSize: "clamp(32px, 4vw, 56px)"
    fontWeight: 900
    lineHeight: 1
  body:
    fontFamily: "'Chakra Petch', sans-serif"
    fontSize: "clamp(14.4px, 1.2vw, 18.4px)"
    fontWeight: 400
    lineHeight: 1.7
  hero-tagline:
    fontFamily: "'Chakra Petch', sans-serif"
    fontSize: "clamp(14.4px, 1.5vw, 19.2px)"
    fontWeight: 400
    lineHeight: 1.8
  quote-body:
    fontFamily: "'Chakra Petch', sans-serif"
    fontSize: "clamp(17.6px, 2.2vw, 25.6px)"
    fontWeight: 500
    lineHeight: 1.8
  label-pill:
    fontFamily: "'Space Mono', monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.2em
    textTransform: uppercase
  label-eyebrow:
    fontFamily: "'Space Mono', monospace"
    fontSize: 13.6px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.3em
    textTransform: uppercase
  badge:
    fontFamily: "'Space Mono', monospace"
    fontSize: 11.2px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  chart-value:
    fontFamily: "'Space Mono', monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
  chart-label:
    fontFamily: "'Space Mono', monospace"
    fontSize: 11.2px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.05em
  date-chip:
    fontFamily: "'Space Mono', monospace"
    fontSize: 11.2px
    fontWeight: 400
    lineHeight: 1
  counter:
    fontFamily: "'Space Mono', monospace"
    fontSize: 12.8px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.15em

spacing:
  pixel-unit: 4px
  pad-slide-y: "3vh"
  pad-slide-x: "4vw"
  pad-card-lg: "32px 40px"
  pad-card-md: "28px"
  pad-card-sm: "16px 20px"
  gap-grid-lg: 32px
  gap-grid-md: 24px
  gap-grid-sm: 16px
  content-max-width: 1200px

canvas:
  width: 100vw
  height: 100vh

components:
  label-pill:
    background: "{colors.deep-navy}"
    color: "{colors.neon-yellow}"
    padding: "6px 14px"
    fontSize: 12px
    fontWeight: 700
    letterSpacing: 0.2em
    textTransform: uppercase
    fontFamily: "'Space Mono', monospace"
    description: "Universal section tag. Default fill is deep-navy with neon-yellow text. Variant fills swap text color so the pill stays legible (e.g., navy bg with cyan text, navy bg with pink text)."
  pixel-button:
    background: "{colors.neon-cyan}"
    color: "{colors.deep-navy}"
    padding: "16px 36px"
    fontFamily: "'Tektur', cursive"
    fontWeight: 700
    letterSpacing: 0.08em
    textTransform: uppercase
    boxShadow: "{shadows.pixel-stack-cyan-yellow}"
    description: "The signature stacked-shadow CTA. The pink variant swaps cyan body for pink and yellow shadow halo for cyan halo."
  pixel-corner-bracket:
    width: 24px
    height: 24px
    borderWidth: 4px
    description: "Two outward-facing L-shapes (top-left + bottom-right) bracketing a region. Default color is neon-cyan; yellow and pink variants exist. Sits 8px outside the bracketed element."
  feature-card:
    background: "rgba(255, 255, 255, 0.15)"
    backdropFilter: "blur(8px)"
    padding: "32px 24px"
    border: "2px solid rgba(15, 27, 61, 0.2)"
    description: "Frosted-glass card with inset navy L-brackets (top-left + bottom-right) replacing rounded corners. Used on light-surface slides."
  stat-block:
    background: "rgba(94, 220, 244, 0.08)"
    border: "2px solid rgba(94, 220, 244, 0.2)"
    padding: "32px 16px"
    description: "Cyan-tinted glass stat tile with cyan L-bracket accents at opposite corners. Used on dark surfaces. Stat numeral uses the pixel-text-shadow-small treatment."
  bar-track-light:
    height: 32px
    background: "rgba(15, 27, 61, 0.1)"
    description: "Horizontal track for hbar charts on light surfaces. Fill is solid navy/cyan/pink with a yellow offset shadow."
  bar-vertical:
    background: "{colors.neon-cyan}"
    boxShadow: "{shadows.pixel-l-shape}"
    description: "Vertical chart bar with three-piece navy L-shadow. Color cycles cyan → pink → yellow."
  timeline-node:
    width: 24px
    height: 24px
    background: "{colors.neon-cyan}"
    border: "4px solid {colors.deep-navy}"
    description: "Square pixel node on timeline rails. Active state swaps fill to neon-yellow."
  timeline-rail:
    width: 4px
    background: "repeating-linear-gradient(to bottom, {colors.deep-navy} 0px, {colors.deep-navy} 16px, transparent 16px, transparent 24px)"
    description: "Dashed pixel rail running between timeline nodes."
  date-chip:
    background: "{colors.deep-navy}"
    color: "{colors.neon-cyan}"
    padding: "2px 10px"
    fontFamily: "'Space Mono', monospace"
    fontSize: 11.2px
    description: "Small inline date marker on timeline events."
  hero-badge:
    border: "2px solid {colors.neon-yellow}"
    color: "{colors.neon-yellow}"
    padding: "8px 16px"
    fontFamily: "'Space Mono', monospace"
    fontSize: 11.2px
    letterSpacing: 0.1em
    textTransform: uppercase
    description: "Outline-only chip used in clusters under hero headlines."
  bg-grid:
    backgroundColor: "{colors.dark-void}"
    backgroundImage: "linear-gradient(rgba(94, 220, 244, 0.07) 1px, transparent 1px), linear-gradient(90deg, rgba(94, 220, 244, 0.07) 1px, transparent 1px)"
    backgroundSize: "40px 40px"
    description: "40px cyan-on-navy grid wallpaper for dark surfaces. Pink, cyan, and lavender variants invert the relationship (colored ground with low-opacity navy grid lines)."
  scanlines:
    background: "repeating-linear-gradient(0deg, transparent 0px, transparent 2px, rgba(10, 14, 39, 0.04) 2px, rgba(10, 14, 39, 0.04) 4px)"
    mixBlendMode: multiply
    description: "Horizontal CRT scanline overlay applied via ::after at z-index 50. Always present on every slide."
  grain:
    opacity: 0.035
    description: "SVG fractal-noise grain layer applied via ::before at z-index 49. Always present on every slide."
  crt-glow:
    background: "radial-gradient(ellipse at center, transparent 50%, rgba(10, 14, 39, 0.25) 100%)"
    description: "Radial vignette that darkens the corners to mimic a CRT bulge. Applied to dark-surface slides via ::after at z-index 51."
  starfield:
    description: "Container of small 4-6px colored squares (cyan, yellow, pink) positioned absolutely with a 3s twinkle keyframe. Lives on dark surfaces only."
  pixel-particles:
    description: "Floating 8px colored squares with an 8s float keyframe. Decorative ambient layer on hero and CTA-type surfaces."
  nav-dot:
    width: 12px
    height: 12px
    border: "2px solid {colors.neon-cyan}"
    background: transparent
    description: "Hollow square pip with a 2px inset cyan fill on active state. Fixed vertical rail at right edge."
  quote-line:
    width: 60px
    height: 4px
    background: "{colors.neon-yellow}"
    boxShadow: "4px 4px 0 {colors.deep-navy}"
    description: "Short yellow rule with navy offset shadow, used as a separator under quote bodies."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/8-bit-orbit/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

8-Bit Orbit 是一套**复古未来主义像素艺术演示系统**。它的底层前提是 **4 像素单位**：每一处阴影偏移、每一条边框、每一个角标、每一个标签高度都收敛到 4px 的倍数。布局像是在老 CRT 上栅格化后拖进 HTML，而氛围叠层（扫描线、颗粒、暗角辉光、动态星空）在每一处表面强化这种错觉。

字体栈由三款字面协同工作。**Tektur** 是展示字面，一款粗壮、几何、半像素化的怪诞体，承载标题、英雄文字、统计数字，以及任何需要"画在像素网格上"感的文字。**Chakra Petch** 是正文字面，一款带细微几何切口的人文无衬线，小尺寸下依然清晰，也不会与 Tektur 抢注意力。**Space Mono** 是系统字面，只用于标签、说明文字、徽章、图表数值、日期和计数器。这些元素上的等宽处理加宽字距，让它们读起来像 HUD 读数，而不是编辑式的图注。

配色以**深海军蓝为底**（`{colors.dark-void}` 与 `{colors.deep-navy}`），由**三种饱和霓虹**点亮：青、亮粉、黄，外加一抹柔和薰衣草浅彩。表面交替出现：先是深海军蓝表面（青色网格壁纸、白字、前方发光的霓虹点缀），再是彩色表面（粉、青或薰衣草底，配海军蓝文字与低不透明度蚀刻的海军蓝网格线）。霓虹从不用于正文，只留给标题、统计数字、强调分隔线和标签填充。结果是高对比却不刺眼：霓虹像被点亮，而不是被印上去。

纵深是这套系统的招牌手法：**以像素单位堆叠的硬边偏移阴影**。旗舰式样是按钮上的六片阴影：三片海军蓝偏移按 4px 向右下递进，再三片彩色光晕偏移按 8px 继续向外递进。英雄文字用两层文字阴影（黄在 +4/+4，海军蓝在 +8/+8）。卡片要么用 6px 海军蓝盒阴影，要么在精选层用 8px 黄色盒阴影。每一处阴影都是硬边、零模糊、锁定 4px 网格。氛围纵深来自始终开启的**扫描线 + 颗粒 + CRT 辉光**叠层三重奏，它微妙地调制每一处表面。

**密度取向：中等偏密，氛围饱满。** 表面干净、周围空无一物时，这套系统就会散架：没有扫描线、颗粒、暗角、粒子或背后的彩色网格，字体便失去街机语境，开始像普通网页排印。氛围层永远要叠上。但在内容区域内部，留白仍然要紧：卡片间距宽（24-32px 间隙）、统计块内部留足内边距、英雄文字允许占据主导。典型一页承载一个展示瞬间 + 一小簇辅助元素（徽章、标签、一张图表或一个小网格），全部坐落在装饰完整的氛围背景之上。

**关键特征：**
- 三字体栈：Tektur（展示）、Chakra Petch（正文）、Space Mono（HUD/标签），不得替换，也不得越出各自角色混用。
- 海军蓝底（`{colors.dark-void}` / `{colors.deep-navy}`）与彩色网格表面（粉、青、薰衣草）交替出现，两者都带 40px 蚀刻网格。
- 三种霓虹（青、粉、黄）只留给展示文字、数字、分隔线与标签填充，绝不用于正文。
- 一切尺寸对齐 4px 像素单位：边框 2-4px、阴影偏移 4px / 8px、角标 24×24 配 4px 描边。
- 堆叠的硬边偏移阴影是这套系统的纵深语言，绝不模糊；文字阴影也不上色，唯一的例外是黄到海军蓝的级联。
- 每页都带常驻的扫描线 + 颗粒 + CRT 暗角三重奏，位于 z-index 49-51。
- L 形角标（`{components.pixel-corner-bracket}`）取代圆角，框住区域、卡片与统计块。
- 等宽标签胶囊（`{components.label-pill}`）作为每个区域通用的眉题，海军蓝填充、霓虹文字、0.2em 字距、大写。
- 动态星空与浮动粒子方块给深色表面铺底，属于氛围而非装饰。

## 颜色

### 调色板

- **Dark Void**（`{colors.dark-void}` — `#0A0E27`）：最深的底，用在 `<body>` 上，也是深色网格表面的基底。在 CRT 暗角下读起来像偏蓝的黑。
- **Deep Navy**（`{colors.deep-navy}` — `#0F1B3D`）：结构色，所有阴影叠层、标签填充、深色卡片、霓虹表面上的按钮文字、图表条文字都用它。比 void 略暖；两者叠放时读起来分别是底与图。
- **Neon Cyan**（`{colors.neon-cyan}` — `#5EDCF4`）：系统的主辉光。用于深色表面上的标题、主按钮填充、统计数字、主图表条、时间轴节点、导航点、角标，以及深色表面上的网格线（7% 不透明度）。
- **Neon Pink**（`{colors.neon-pink}` — `#F0A6CA`）：暖调点缀。用作彩色表面底（40px 海军蓝压粉网格）、次按钮填充、次图表条、像素头像的嘴部细节、三级角标。
- **Neon Yellow**（`{colors.neon-yellow}` — `#F4D03F`）：高明度警示色。用于按钮背后的阴影光晕与精选层卡片、激活态时间轴节点填充、英雄徽章、标签胶囊文字变体、引文线，以及 Tektur 文字阴影第一层。
- **Soft Lavender**（`{colors.soft-lavender}` — `#E2D5F2`）：平静的浅彩表面，给需要从霓虹压海军蓝强度里缓一口气的页面作底。和其他彩色表面一样带蚀刻海军蓝网格壁纸。
- **White**（`{colors.white}` — `#FFFFFF`）：只作深色/霓虹表面上的文字颜色。绝不作为幻灯片背景。

### 默认值

- **默认表面背景**：`{colors.dark-void}` 配 40px 青色网格（`{components.bg-grid}`）。其上始终叠加扫描线 + 颗粒 + crt-glow。
- **深色表面上的默认标题色**：`{colors.neon-cyan}`，英雄级文字配 `{shadows.pixel-text-shadow-small}` 或 `{shadows.pixel-text-shadow}` 处理。
- **彩色网格（粉/青/薰衣草）上的默认标题色**：`{colors.deep-navy}`，霓虹文字在霓虹底上会看不清。
- **深色表面上的默认正文色**：`rgba(255, 255, 255, 0.7)`，柔化白，不是纯白。
- **彩色网格上的默认正文色**：`rgba(15, 27, 61, 0.75)`，柔化海军蓝。
- **默认标签胶囊填充**：`{colors.deep-navy}` 配 `{colors.neon-yellow}` 文字。在彩色网格上，只要与海军蓝的对比度足够，文字可换成青或粉。
- **标注与统计数字的默认强调色**：`{colors.neon-cyan}`。
- **默认图表配色顺序**：青 → 粉 → 黄（跨系列按此顺序）。
- **默认角标颜色**：`{colors.neon-cyan}`。黄、粉变体用于主题点缀。

当某页需要更柔和或更暖时，把彩色网格从青压海军蓝（默认）换成海军蓝压粉、海军蓝压青或海军蓝压薰衣草：结构关系反转（网格线变成低不透明度海军蓝），但排印规则不变。

## 排印

### 字族
系统用三款字面，各锁死一个角色。

**Tektur** 是展示字面，一款宽身、半几何的怪诞体，带细微像素网格切口。用于每一个英雄标题、标题、统计数字、引号和大号数字。Tektur 的粗壮个性让系统有街机原生感；换成 Inter 或 Space Grotesk 会毁掉整个美学。

**Chakra Petch** 是正文字面，一款带轻微几何/方正气质的人文无衬线，14-22px 下清晰易读，个性足够与 Tektur 并置而不被吞没。用于段落、英雄副标题、引文正文，以及一切较长散文。

**Space Mono** 是 HUD 字面，一款等宽体，只用于标签、徽章、图表数值/坐标轴、页码、日期胶囊，以及任何该像系统读数的元素。等宽加宽字距大写的组合，是这套系统的"界面"声部。

绝不用 Tektur 排正文，绝不用 Chakra Petch 做外壳/HUD，绝不用 Space Mono 排标题。三角色分离就是排印结构。

### 排印比例

| Token | 尺寸（clamp） | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.pixel-hero}` | 48–128px | Tektur | 900 | 英雄或封面展示标题，始终带两层文字阴影 |
| `{typography.display}` | 32–64px | Tektur | 700 | 大型分节开篇 |
| `{typography.headline}` | 24–45px | Tektur | 700 | 分节主标题 |
| `{typography.subhead}` | 17.6–24px | Tektur | 700 | 区域级副标题或卡片标题 |
| `{typography.stat-number}` | 32–56px | Tektur | 900 | 统计块数字，配小文字阴影 |
| `{typography.body}` | 14.4–18.4px | Chakra Petch | 400 | 段落正文 |
| `{typography.hero-tagline}` | 14.4–19.2px | Chakra Petch | 400 | 英雄副标题 / 像素英雄下方的导语段 |
| `{typography.quote-body}` | 17.6–25.6px | Chakra Petch | 500 | 引文文字 |
| `{typography.label-pill}` | 12px | Space Mono | 700 | 海军蓝标签胶囊内文字 |
| `{typography.label-eyebrow}` | 13.6px | Space Mono | 400 | 标题上方独立的大写眉题（字距比胶囊更宽） |
| `{typography.badge}` | 11.2px | Space Mono | 400 | 仅描边的英雄徽章文字 |
| `{typography.chart-value}` | 12px | Space Mono | 700 | 图表条数值数字 |
| `{typography.chart-label}` | 11.2px | Space Mono | 400 | 图表坐标轴或类别标签 |
| `{typography.date-chip}` | 11.2px | Space Mono | 400 | 时间轴事件上的日期标记 |
| `{typography.counter}` | 12.8px | Space Mono | 400 | 常驻页码（NN / NN） |

### 默认值

- **英雄或封面标题默认尺寸**：`{typography.pixel-hero}`（48–128px clamp），始终 Tektur 字重 900 配两层文字阴影。
- **分节主标题默认尺寸**：`{typography.headline}`（24–45px clamp），Tektur 字重 700。
- **段落正文默认尺寸**：`{typography.body}`（14.4–18.4px clamp），Chakra Petch 字重 400。
- **统计数字默认尺寸**：`{typography.stat-number}`（32–56px clamp），Tektur 字重 900，始终带 3px 海军蓝文字阴影。
- **眉题标签默认尺寸**：装在海军蓝胶囊里的 `{typography.label-pill}`（12px）；若眉题独立放置则用 `{typography.label-eyebrow}`（13.6px）。
- **任何 Space Mono 标签默认字距**：0.1em（徽章）到 0.3em（眉题标签）。等宽不加宽字距会读成代码，不像 HUD。
- **默认正文字重**：Chakra Petch 用 400，引文正文用 500。
- **默认展示字重**：标题用 700，英雄级与统计数字用 900。

拿不准该用哪个展示 token 时，默认取 `{typography.headline}`，它是分节级主力。`{typography.pixel-hero}` 只留给封面与 CTA 时刻。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每个 pixel-hero 元素都带堆叠文字阴影。** 式样是在青色文字上用 `4px 4px 0 {colors.neon-yellow}, 8px 8px 0 {colors.deep-navy}`。没有这层双层级联的 pixel-hero 元素读起来像未处理的展示文字，会破掉街机声部。
- **每个统计数字都带小文字阴影。** 式样是在青色文字上用 `3px 3px 0 {colors.deep-navy}`。深色表面上的统计数字需要这层阴影才有被点亮感；没有就显得平。
- **每个 Space Mono 元素都大写并加宽字距**：图表标签最小 0.05em，胶囊与徽章 0.08–0.2em，独立眉题标签 0.3em。句首大写的等宽在这套系统里不存在。
- **每个 Tektur 展示元素保持原生字距或轻微正值（英雄级 +0.04em）。** Tektur 本就宽身，加负字距会把它压成另一种字面。
- **每个 Chakra Petch 正文块行高 ≥ 1.6。** 这款字面偏密，行高再紧就糊成不可读。
- **每个标签胶囊都用 12px Space Mono、0.2em 字距。** 没有例外，胶囊是系统最易认的小外壳，尺寸或字距一偏就破相。
- **每个图表条数值 / 坐标轴标签都用 Space Mono。** 数值外壳一律等宽，绝不用 Tektur 或 Chakra Petch。

### 排印原则

声部对比是**粗壮展示 ↔ 人文正文 ↔ 宽字距等宽外壳**。把三者中任一角色换成别的字面，系统就塌成普通深色模式美学。展示与正文从不用斜体，唯一出现的斜意只隐含在像素艺术装饰元素的轻微倾斜里。

Tektur 要始终显得**稳稳落地**：左对齐、行高宽裕、正文长度的行绝不居中（只有英雄与 CTA 标题允许居中）。Chakra Petch 要始终显得**平静**：默认左对齐、不用全大写、不加字距。

## 布局

### 画布系统
系统以每页 `100vw × 100vh` 为目标。幻灯片在 `slides-container` 内纵向堆叠，通过 `transform: translateY(...)` 切换导航。同一时刻只有一页占据视口，过渡用 800ms 的 cubic-bezier `(0.22, 1, 0.36, 1)` 缓动。

默认幻灯片内边距是 `3vh 4vw`。内层 `slide-content` 以 `max-width: 1200px` 封顶并居中，宽屏上内容保持编辑式栏宽，而彩色背景铺满视口。

### 像素单位
系统里每一处尺寸都对齐 **4px 网格**。边框 2px 或 4px。阴影偏移 4px 或 8px。角标 24×24 配 4px 描边。背景网格 40px（10 × 像素单位）。卡片内边距通常收敛到 8 的倍数（16、24、32、48）。正是这份纪律让系统读起来像被栅格化过，而不是矢量绘制。

### 常驻外壳
每页都出现三个元素：
- **导航点轨**：12×12 青色描边方块的纵向栈，固定在 `right: 24px`、垂直居中。激活态把内部 8×8 填成青色。
- **页码**：Space Mono `01 / 10` 格式，固定在 `bottom: 24px`、水平居中，深海军蓝半透明胶囊底。
- **导航提示**：`USE KEYS ↑ ↓`，Space Mono 11px、50% 不透明度，固定在 `bottom: 24px right: 24px`。

整份演示文稿的光标是 `crosshair`，这是又一处街机信号。

### 氛围叠层栈
每页都带（按 z 序）：
1. 表面背景，`{components.bg-grid}`（青压海军蓝）或某个彩色网格变体。
2. 颗粒层，z-index 49，不透明度 0.035。
3. 扫描线，z-index 50，multiply 混合模式。
4. CRT 暗角辉光，z-index 51（仅深色表面）。
5. 可选星空 / 像素粒子，位于表面内部 z-index 1。
6. `.slide-content` 在氛围层之上，z-index 10。

这套叠层栈就是系统的身份。少了它渲染出的页面像线框图。

## 纵深与层级

### 堆叠硬边偏移阴影（招牌）
系统用 **4px 像素单位下堆叠、多级的硬边偏移阴影**。每个阴影值都由三种式样之一组成：

- **三级海军蓝 L 形**（`{shadows.pixel-l-shape}`）：`4px 0`、`0 4px`、`4px 4px` 三处深海军蓝偏移，零模糊。用于图表条与小型抬升外壳，暗示单层下落。
- **六级按钮级联**（`{shadows.pixel-stack-cyan-yellow}` / `{shadows.pixel-stack-pink-cyan}`）：先三处海军蓝偏移按 4px 递进，再三处彩色光晕偏移按 8px 在后方递进。造出双层像素斜角效果。只用于 `{components.pixel-button}`。
- **两层文字阴影**（`{shadows.pixel-text-shadow}` / `{shadows.pixel-text-shadow-small}`）：黄层在 +4/+4，海军蓝层在 +8/+8（统计级数字则只在 +3/+3 用海军蓝）。用于每个 Tektur 展示元素。

所有阴影零模糊、硬边、锁定像素单位。模糊投影在这套系统里根本不存在。

### 卡片阴影
卡片用两种更简单的式样：
- `{shadows.card-offset}` = `6px 6px 0 rgba(15, 27, 61, 0.15)`，浅色表面上非精选层卡片的柔和海军蓝偏移。
- `{shadows.card-featured}` = `8px 8px 0 {colors.neon-yellow}`，精选层卡片的霓虹黄偏移，配 `-12px` translateY 抬升。

### 角标即纵深
L 形角标（`{components.pixel-corner-bracket}`）取代区域与卡片上的传统边框处理。对角两枚角标暗示出框而不把框封死，观者自行补上缺边。在统计块与特性卡片上，角标内缩到 `top: -2px / left: -2px` 与 `bottom: -2px / right: -2px`，略微破出单元格边缘，强化像素斜角感。

### 氛围纵深
扫描线 + 颗粒 + CRT 暗角栈在每一处表面提供环境纵深，不需要给单个元素加阴影。动态星空与浮动粒子在内容后方再叠空间线索。这些都不是附加装饰，而是系统纵深感知的核心。

## 形状与处理

### 圆角
基本为零。全场唯一的圆形是圆环式导航点的内部填充（在这套系统里仍是方块，导航点是方形点，不是圆点）。圆角按钮、圆角卡片或圆角胶囊片会立刻破掉像素艺术美学。

像素脸头像区用方形眼睛和矩形嘴，解剖结构以像素而非曲线呈现。

### 边框粗细
- **2px solid**：特性卡片轮廓、英雄徽章、导航点、统计块框、图表条（内联边缘）。
- **3px stroke**：SVG 图表内的图表坐标轴（深海军蓝）。
- **4px solid**：角标、时间轴节点边框、引文线，以及按钮内部的像素斜角。

边框始终实线、始终海军蓝或霓虹，从不用虚线，唯独时间轴轨道（`{components.timeline-rail}`）例外，它刻意用 16px 实、8px 空的重复线性渐变，模仿像素虚线。

### 装饰元素类型

**像素角标**：两枚朝外的 L 形（左上 + 右下）框住一个区域。24×24 配 4px 描边。默认青色，另有黄、粉变体。角标式样是系统最鲜明的非排印标记。

**标签胶囊**：海军蓝矩形，配 12px / 0.2em 的霓虹黄 Space Mono 文字。通用分节眉题。变体把文字色翻成青或粉，海军蓝填充不变。

**英雄徽章**：仅 2px 黄色描边，配黄色 Space Mono 文字。成簇出现在英雄标题下方，作特性标签。

**统计块**：青调玻璃块（8% 青填充、20% 青边框），左上与右下带青色角标。承载一个大统计数字，下方压一行 Space Mono 粉色标签。

**特性卡片**：磨砂玻璃白卡（15% 白填充、模糊），对角带海军蓝角标。用于彩色网格表面。

**像素按钮**：青色矩形，配六级堆叠阴影级联。悬停时按钮平移 +2/+2，阴影收成四级级联，模拟像素艺术里的按键按下。

**引文线**：60×4 黄色矩形，配 4×4 海军蓝偏移阴影。用作引文正文下方的分隔符。

**时间轴节点**：24×24 青色方块，4px 海军蓝边框，坐落在虚线海军蓝轨道上。激活态填充换成黄色。

**日期胶囊**：内联 2px 内边距的海军蓝小片，配青色 Space Mono 文字，用来标记时间轴事件。

**像素脸**：120×120 的方形"五官"组合（青眼、粉嘴），以绝对定位 div 落在海军蓝头像区里。既当友好吉祥物，也是系统招牌装饰模块。

**层级卡片**：白色矩形，6px 海军蓝偏移阴影。精选层把填充换成深海军蓝、阴影换成 8px 黄色，并 `-12px` translateY 抬升。层级特性用青色 `+` ::before 字形代替常规项目符号。

**像素风景**：CTA 类表面底部一排高低不一的深海军蓝山峰，不透明度 0.3。纯装饰，暗示街机地平线。

## 该做与不该做

### 该做

- 给每页都套上扫描线 + 颗粒 + CRT 暗角叠层栈。氛围就是这套设计系统；没有它的表面像线框图。
- 深色表面用 `{colors.neon-cyan}` 作默认标题色，彩色网格（粉/青/薰衣草）上用 `{colors.deep-navy}` 作默认标题色。
- 给每个 pixel-hero 元素套 `{shadows.pixel-text-shadow}`，给每个统计数字套 `{shadows.pixel-text-shadow-small}`。Tektur 展示文字少了文字阴影就显得平。
- 把每一处尺寸都对齐 4px 像素单位：边框粗细、阴影偏移、内边距、角标尺寸。脱格数值会破掉栅格化质感。
- 展示用 Tektur、正文用 Chakra Petch、外壳用 Space Mono，三者各守其位。交叉混用会把系统压平。
- 把眉题装进 `{components.label-pill}`（海军蓝底、黄色 Space Mono 文字、0.2em 字距、大写）当通用分节标签。
- 海军蓝底每个区域至少配一处霓虹辉光：文字、图表条、角标或按钮阴影光晕。纯海军蓝没有霓虹点缀，读起来像熄屏。
- 在深色英雄页与 CTA 表面叠动态星空和像素粒子漂浮物。动效是氛围的一部分。
- 图表按青 → 粉 → 黄系列顺序渲染，数字与标签用 Space Mono。霓虹三色就是图表配色。
- 卡片与统计块用对角两枚 L 形角标框住，不要整圈描边。暗示出来的框是系统招牌的卡片处理。

### 不该做

- 不要替换字体。Tektur、Chakra Petch、Space Mono 是三个声部，换成 Inter、Roboto 或 Space Grotesk 系统就塌。
- 不要给任何角加圆角。像素美学靠方边。border-radius 只留给 SVG 圆环图几何。
- 不要模糊任何阴影。每处阴影都是零模糊硬边。`0 4px 12px rgba(0,0,0,0.1)` 在这里不存在。
- 不要把霓虹文字放在霓虹表面上。青色标题压粉色网格会看不清，彩色底上改用深海军蓝。
- 不要在句首大写正文里用 Tektur，也不要在外壳/标签里用 Chakra Petch。每款字面只有一个角色。
- 不要引入第四种霓虹。配色是青 + 粉 + 黄 + 薰衣草浅彩。加绿或橙会破掉精心收拢的霓虹三色。
- 任何一页都不要省掉氛围叠层栈，哪怕图表密集或表格密集的页面。叠层不可商量。
- 不要把 Chakra Petch 正文设成大写。正文始终句首大写，大写只留给 Space Mono 与 Tektur 展示。
- 不要为了纯文字眉题而丢掉海军蓝标签胶囊。胶囊是系统最易认的小外壳。
- 不要用偏轴偏移给文字或外壳加阴影。每处阴影都按 4px 增量向右下递进，左向或上向偏移不存在。

## 响应式行为

8-Bit Orbit 是**视口流式系统**，围绕基于 `vw/vh` 的尺寸与 CSS `clamp()` 区间构建。演示文稿本身没有硬性断点，每个字号、内边距、间隙都按视口宽度在最小与最大值之间插值。

### 缩放行为
- 英雄文字按视口宽度从 48px 缩放到 128px。
- 统计数字从 32px 缩放到 56px。
- 正文从 14.4px 缩放到 18.4px。
- 4px 像素单位、40px 网格尺寸、扫描线 4px 条纹、角标尺寸都固定不缩放，于是视口越大，像素外壳在比例上越显精细（这是刻意的：画布越大，像素读起来越小越精致）。

### 组件断点
存在三个组件级断点：
- `max-width: 1024px`：特性网格由 4 列收成 2 列，双栏分栏布局堆叠。
- `max-width: 900px`：特性网格进一步收拢，横向条形图的标签列收窄。
- `max-width: 500px`：特性网格变单列，统计网格堆叠。

### 放映行为
- 用 `ArrowDown`、`ArrowRight` 或 `Space` 前进。
- 用 `ArrowUp` 或 `ArrowLeft` 后退。
- `Home` 跳到首页，`End` 跳到末页。
- 触屏纵向滑动以 50px 阈值前进/后退。
- 鼠标滚轮滚动以 800ms 防抖锁前进/后退。
- 幻灯片过渡用 800ms cubic-bezier `(0.22, 1, 0.36, 1)` 配 translateY 变换。

### 动画触发
图表条与统计计数器在页面进入时以 `setTimeout` 错峰入场（条目间 100-150ms）。页面退出时，条/计数器归零，重新进入会重播动画。`prefers-reduced-motion` 媒体查询会关闭过渡与星空/粒子闪烁关键帧。

### 打印行为
系统没有 `@media print` 规则。演示文稿以屏幕为先，打印只能得到当前激活的一页。静态导出时，逐页截图能保留所有氛围叠层（扫描线与颗粒由 CSS 渲染，不是图片资源）。

## CJK 与国际化内容

用本模板承载中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文搭配，并套用通用 CJK 调整。所有推荐中文字体均通过 CDN 加载，无需安装。

### 推荐中文搭配

| 角色 | 拉丁（默认） | 中文对应 |
|---|---|---|
| 展示 / 英雄 / 统计数字 | Tektur 700–900 | 思源黑体 Noto Sans SC 900 |
| 正文 / 英雄副标题 / 引文正文 | Chakra Petch 400–500 | 思源黑体 Noto Sans SC 400 |
| HUD 标签 / 徽章 / 图表数值 / 计数器 | Space Mono 400–700（大写 + 宽字距） | 思源黑体 Noto Sans SC 500（无变换、无字距）——见下方已知 CJK 缺口 |

### 混排策略

**策略 A**：用一款自带拉丁字形覆盖的 CJK 字族，把所有文字元素设为 `font-family: 'Noto Sans SC', sans-serif`。思源黑体自带拉丁字形，与汉字并排也干净，于是像 `使用 Tektur 字体` 这样的句子会用同一款字面连贯渲染，不会在词中切换字体。这套系统平常跑三款字面（展示 / 正文 / HUD），收成一款 CJK 字面是正确的取舍：三款拉丁字面都没有可信的中文对应，而视觉层级仍可靠字重（900 / 700 / 500 / 400）加系统招牌的阴影叠层撑起来。

### 加载

在模板 `<head>` 中加入：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- **行高**：在拉丁规格上提高约 15–25%。正文 1.75–1.85（从 1.7–1.8 上调），展示 1.15–1.25（从 1.05–1.15 上调）。CJK 字形方正饱满，纵向比拉丁更挤。
- **字距**：每段 CJK 文本设为 0。模板里 Tektur 展示的正字距（+0.04em）与 Space Mono 标签的 0.1–0.3em 等宽字距，放到方正 CJK 字形上会显得散架，它们本就按均匀间距设计。
- **文字变换**：不要对中文套 `uppercase`，CJK 没有大小写。系统里每个 Space Mono 标签都用 `text-transform: uppercase`，CJK 文本要去掉。
- **标点**：用全角中文标点（，。：；！？「」（））。
- **展示标题不加句号**：中文排印惯例，展示级标题末尾不写 。
- **中西文之间加空格（盘古之白）**：每个汉字与相邻的拉丁字符或数字之间插入一个 ASCII 空格。写 `8 位赛博 / 1989 模式`，不要写 `8位赛博/1989模式`。
- **一句一款字体**：思源黑体以统一风格覆盖 CJK 与拉丁字形，混排句子交给它处理。不要让浏览器因 ASCII 字符在句中回退到 Tektur 或 Space Mono。

### 本系统的美学提示

系统的身份建立在三个声部上：Tektur（粗壮街机展示）、Chakra Petch（人文正文）、Space Mono（HUD 读数），CJK 版本无法保留这种三字面反差。补偿办法是更倚重**非排印**的招牌元素：堆叠文字阴影（黄在 +4/+4、海军蓝在 +8/+8）用在思源黑体 900 标题上依然成立，字面本身变得普通时，正是它扛起街机声部。所有氛围叠层（扫描线、颗粒、CRT 暗角、星空、网格壁纸）都要保留，它们在 CJK 版本里比在拉丁原版里承担更多身份工作。

系统的 Space Mono 标签胶囊（海军蓝填充、霓虹黄文字、0.2em 字距、大写）是最易认的小外壳，却最不好译：CJK 字符不接受宽字距或大写变换。中文标签胶囊请用思源黑体字重 500、0 字距、无变换，字号略收紧（10–11px 而非 12px），保住小片的紧凑轮廓。彩色胶囊底与角标框边承担识别工作。

### 已知 CJK 缺口

- **没有可 CDN 加载的中文像素字体。** 系统的街机美学依赖 Tektur 的半像素怪诞气质，Google Fonts 或主流 CDN 上没有既读得出"像素艺术"又清晰可读的中文对应字面。思源黑体字重 900 有分量，却把像素网格信号完全丢掉。氛围叠层（扫描线、颗粒、暗角、星空）与像素斜角阴影叠层只能独自扛起街机声部。
- **没有可 CDN 加载的中文等宽字面给 HUD 标签。** Space Mono 的"系统读数"声部依赖等宽节奏 + 大写 + 0.1–0.3em 字距，这些没有一样能迁移到 CJK。标签胶囊会丢掉等宽性格，只能靠海军蓝填充 + 霓虹文字 + 角标框边维持外壳辨识度。

## 迭代指南

1. 任何新页面都配上完整氛围叠层三重奏（深色表面用扫描线 + 颗粒 + crt-glow，彩色表面用扫描线 + 颗粒）和 40px 蚀刻网格表面。不要省叠层。
2. 任何新展示元素用 Tektur，任何新正文元素用 Chakra Petch，任何新标签、徽章、计数器或图表数值用 Space Mono。绝不越过角色边界。
3. 任何新标题在深色表面用 `{colors.neon-cyan}`、在彩色网格上用 `{colors.deep-navy}`，两者都配相应的 Tektur 字重，英雄级再加堆叠文字阴影。
4. 任何新眉题都用 `{components.label-pill}`：海军蓝填充、霓虹黄 Space Mono 文字、12px / 0.2em / 大写。不要用普通 h 标签顶替。
5. 任何新卡片或区域都在对角（左上 + 右下）配 L 形角标，不要整圈描边。暗示出来的框是系统招牌。
6. 任何新尺寸都对齐 4px 像素单位。边框 2-4px、阴影偏移 4px / 8px、角标 24px、网格 40px。脱格数值读着就不对。
7. 任何新阴影都是零模糊硬边。按钮用六级级联，卡片用 6px 海军蓝或 8px 黄色，文字用双层级联。
8. 任何新图表按青 → 粉 → 黄的系列顺序循环。数字标签与坐标轴标签始终用 Space Mono。
9. 若某处表面需要更暖或更柔，换成粉、青或薰衣草的蚀刻网格变体，但所有排印规则保持不动（海军蓝标题、柔化海军蓝正文）。
10. 动画元素（星空、粒子、图表条增长、计数器滚动）应尊重 `prefers-reduced-motion`。氛围叠层（扫描线、颗粒、暗角）不带动画，始终开启。

## 已知缺口

- **Tektur、Chakra Petch 与 Space Mono 都是通过 preconnect + `<link>` 加载的 Google Fonts**。除了 `cursive` / `sans-serif` / `monospace`，系统没有回退策略；在 Google Fonts 失效的环境（离线、受限网络）里，美学会塌成系统默认字体，失去个性。
- **星空与像素粒子元素由内联 JS 生成**，创建固定数量、绝对定位、带随机位置与动画延迟的 div。动画关键帧写在 CSS 里，但只有 JS 成功运行才会创建这些元素。
- **图表系统是硬编码的**：条高、横条宽度、统计计数器目标值存在 `data-*` 属性里，靠幻灯片序号匹配触发的 `setTimeout` 错峰做动画。没有数据绑定层，新增图表要复制 HTML 式样并更新 JS 的幻灯片序号匹配。
- **CTA 表面上的像素风景由 JS 从硬编码高度数组 `[30, 50, 70, ...]` 生成**。每座山宽度按 `60 + (i % 3) * 20px` 变化。替换风景要改 JS 高度数组。
- **CRT 暗角辉光用固定的深海军蓝径向渐变**。调整它要改 CSS 渐变色标，暗角强度没有 token 化。
- **光标全演示文稿设为 `crosshair`**，出于氛围考虑。在嵌入演示文稿、用户预期能选中文字的场景里，这可能造成冲突。
- **滚轮/触摸回退没有键盘导航提示**。哪怕滚轮与触摸都已接好，导航提示仍写 `USE KEYS ↑ ↓`。
- **页码格式固定为 `NN / NN` 补零**。超过 99 页的演示文稿会渲染出会挤动布局的页码。
- **像素角标尺寸固定 24×24 配 4px 描边**，不随视口缩放。视口极大或极小时，角标在比例上可能显得失调。
