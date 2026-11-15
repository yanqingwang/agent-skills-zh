---
version: alpha
name: Grove
description: A quiet, editorial-serif presentation system in the register of a well-bound monograph or boutique brand book. Playfair Display at weight 400 (never bold) carries every headline, italicized in terracotta coral for accent emphasis as the signature move. Jost weight 300 carries every paragraph as the "good paper" body face. JetBrains Mono at weight 300 holds labels, kickers, and the thin chrome bars. The palette pairs a deep forest green canvas (#192b1b) with warm cream text (#d4cfbf) and a single terracotta coral accent (#c8524a). Generous negative space, hairline 1px borders, and a near-invisible serif watermark numeral give it the calm authority of a literary journal.

colors:
  bg: "#192b1b"
  bg-alt: "#1e3221"
  bg-light: "#e8e4d6"
  bg-light-alt: "#dedad0"
  fg: "#d4cfbf"
  fg-2: "rgba(212, 207, 191, 0.6)"
  fg-3: "rgba(212, 207, 191, 0.32)"
  fg-light: "#192b1b"
  fg-light-2: "rgba(25, 43, 27, 0.58)"
  fg-light-3: "rgba(25, 43, 27, 0.33)"
  accent: "#c8524a"
  border: "rgba(212, 207, 191, 0.12)"
  border-light: "rgba(25, 43, 27, 0.14)"
  watermark-dark: "rgba(212, 207, 191, 0.06)"
  watermark-light: "rgba(25, 43, 27, 0.06)"

color-aliases:
  fg-light: bg
  fg-light-canonical: "fg-light shares hex #192b1b with bg — the green is reused as both surface and primary text-on-light"

typography:
  display:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "10vw"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -0.01em
  h1:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "5.5vw"
    fontWeight: 400
    lineHeight: 1.1
  h1-statement:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "min(4.5vw, 7.5vh, 88px)"
    fontWeight: 400
    lineHeight: 1.15
  h2:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "3.2vw"
    fontWeight: 400
    lineHeight: 1.2
  h3:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "2vw"
    fontWeight: 400
    lineHeight: 1.3
  quote-text:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "3.2vw"
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: -0.01em
    fontStyle: italic
  quote-mark:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "8vw"
    fontWeight: 400
    lineHeight: 0.6
  stat-value:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "4.5vw"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -0.02em
  grove-num:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "18vw"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -0.03em
  lead:
    fontFamily: "'Jost', 'Noto Sans SC', system-ui, sans-serif"
    fontSize: "1.45vw"
    fontWeight: 300
    lineHeight: 1.65
  body:
    fontFamily: "'Jost', 'Noto Sans SC', system-ui, sans-serif"
    fontSize: "1.05vw"
    fontWeight: 300
    lineHeight: 1.75
  body-list-emph:
    fontFamily: "'Jost', 'Noto Sans SC', system-ui, sans-serif"
    fontSize: "max(1.4vw, 17px)"
    fontWeight: 300
    lineHeight: 1.6
  caption:
    fontFamily: "'Jost', 'Noto Sans SC', system-ui, sans-serif"
    fontSize: "0.82vw"
    fontWeight: 300
    lineHeight: 1.55
  label:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: "0.7vw"
    fontWeight: 300
    letterSpacing: 0.12em
  kicker:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: "0.7vw"
    fontWeight: 300
    letterSpacing: 0.14em
    textTransform: uppercase
  chapter-num:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: "0.7vw"
    fontWeight: 300
    letterSpacing: 0.2em
    textTransform: uppercase
  stat-label:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: "0.7vw"
    fontWeight: 300
    letterSpacing: 0.12em
    textTransform: uppercase

spacing:
  pad-x: "8vw"
  pad-y: "6.5vh"
  pad-quote-x: "calc(8vw * 1.1)"
  pad-quote-y: "calc(6.5vh * 1.2)"
  gap-lg: "4.5vh"
  gap-md: "2.8vh"
  gap-sm: "1.4vh"
  rule-short: "36px"

motion:
  ease-slide: "cubic-bezier(0.77, 0, 0.175, 1)"
  dur-slide: "0.9s"
  ease-enter: "cubic-bezier(0.16, 1, 0.3, 1)"
  dur-enter: "0.7s"
  stagger-delays: "0 / 0.08s / 0.18s / 0.3s / 0.44s / 0.6s / 0.78s"

canvas:
  width: 100vw
  height: 100vh

components:
  slide-chrome:
    description: "Thin top bar separating slide content from the page edge. A flex space-between row holding mono label text on each side, separated below by a 1px hairline in {colors.border} (or {colors.border-light} on light slides). Pads with {spacing.gap-sm} above the rule, then {spacing.gap-md} below before content starts."
    border: "1px solid {colors.border}"
    typography: "{typography.label}"
  slide-foot:
    description: "Matching bottom bar. Flex space-between row holding section name and 'NN / TT' counter, with 1px hairline border-top. The chrome and foot together frame every content slide; cover, chapter, quote, and end slides hide both."
    border: "1px solid {colors.border}"
    typography: "{typography.label}"
  grove-num:
    description: "Massive serif digit placed in the background at very low opacity (6%) as compositional texture. Sits absolutely at right: {spacing.pad-x}, bottom: -0.15em, with pointer-events disabled. The system's signature wallpaper element on chapter and section moments."
    fontSize: "18vw"
    color: "{colors.watermark-dark} on dark / {colors.watermark-light} on light"
  grove-stat:
    description: "Stat card: large Playfair value in {colors.accent}, mono uppercase label beneath, 1px border-bottom hairline. No background fill — the card is defined by the rule and the type ratio alone."
    valueColor: "{colors.accent}"
    valueSize: "4.5vw"
    labelTypography: "{typography.stat-label}"
    borderBottom: "1px solid {colors.border}"
  bullet-list:
    description: "Two-column grid list (2em / 1fr) where the bullet is a coral em-dash glyph rendered in JetBrains Mono, not a CSS bullet. The em-dash is the system's bullet language."
    bulletGlyph: "—"
    bulletColor: "{colors.accent}"
    bulletFont: "'JetBrains Mono', monospace"
  rule-coral:
    width: "{spacing.rule-short}"
    height: "1px"
    background: "{colors.accent}"
    description: "A 36px-wide 1px-tall terracotta coral rule. The compositional beat between a kicker and the headline that follows."
  rule-full:
    width: "100%"
    height: "1px"
    background: "{colors.border} on dark / {colors.border-light} on light"
    description: "Full-width hairline divider. Used between stacked sections inside a slide."
  kicker:
    typography: "{typography.kicker}"
    color: "{colors.accent}"
    description: "Mono uppercase eyebrow in coral, placed above an h1/h2 headline."
  chapter-num:
    typography: "{typography.chapter-num}"
    color: "{colors.accent}"
    marginBottom: "{spacing.gap-md}"
  quote-mark:
    typography: "{typography.quote-mark}"
    color: "{colors.accent}"
    description: "Massive Playfair opening-quote glyph in coral, placed above the italic quote body."
  img-placeholder:
    background: "{colors.bg-alt} on dark / {colors.border-light} on light"
    color: "{colors.fg-3} on dark / {colors.fg-light-3} on light"
    typography: "{typography.label}"
    minHeight: "30vh"
    description: "Image-region marker — solid darker-than-background fill with a mono caption stating the placeholder text. Use this in place of <img> until a real image is available."
  nav-dots:
    position: "fixed"
    placement: "bottom: 24px, horizontally centered"
    dotSize: "5px"
    dotBackground: "rgba(255, 255, 255, 0.22)"
    activeBackground: "rgba(255, 255, 255, 0.8)"
    activeTransform: "scale(1.4)"
    description: "Small white dots at the bottom of the viewport indicating slide position. The fixed counter (#slide-counter) is intentionally disabled — the slide-foot already shows NN / TT."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/grove/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Grove 是一套**安静的编辑衬线演示系统**，语域落在文学专著或精品品牌书。底层前提是克制：每页承载一个聚焦内容瞬间，由深负空间环绕，以顶底细 1px 外壳条锚定，并由一小组构图节拍支撑（珊瑚眉题、36px 珊瑚线、斜体珊瑚强调、破折号项目、几乎不可见的水印数字）。

排印栈跑四款字面，各守单一字重：

- **Playfair Display 字重 400** 承载每个标题、每段引文、每个统计数字、每个水印数字。**粗衬线不允许**，无粗体规则是系统最重要的排印承诺。`{colors.accent}` 珊瑚色的斜体 Playfair 是招牌强调手法：任何标题里的 `<em>` 都切到斜体珊瑚。
- **Jost 字重 300** 承载每段正文和每个项目正文。轻字重就是"好纸"感，它往后坐、让衬线领衔。
- **JetBrains Mono 字重 300** 承载每个标签、眉题、页脚线、页码、统计图注。始终大写、始终至少 0.12em 字距。
- **Noto Serif SC / Noto Sans SC 字重 300–500** 作为中文回退为每个角色加载。整套文稿具备双语意识，内容里出现汉字时经 Noto 切分渲染。

配色是紧凑的双表面系统加一种强调。深色页用 `{colors.bg}`（深森林绿）配 `{colors.fg}`（暖奶油，绝不纯白）作正文。浅色页翻到 `{colors.bg-light}`（暖羊皮纸）配 `{colors.fg-light}`（同一森林绿此时作文字）。唯一强调是**陶土珊瑚**（`{colors.accent}` — #c8524a），只用在小而刻意的地方：标题内的斜体强调、眉题下的 36px 线、破折号项目、统计数字、章节序数、起始引号。珊瑚是系统的强调声部，拿它作表面填充或正文段落会击碎编辑纪律。

纵深是**平的、空气感的**。没有投影、没有渐变、没有模糊、没有辉光。仅有的"纵深"装置是 1px 细线边（外壳条、统计卡片分隔、比较面板分隔）和 6% 不透明度的水印数字。整套系统读起来像印在亚麻纸上的墨，不是数字表面。

系统带一套内置**动效语汇**：页到页过渡用 0.9s 的锐利 `cubic-bezier(0.77, 0, 0.175, 1)` 平移，元素入场经 `[data-anim]` 与 `[data-delay]` 属性错峰（fade-up / fade-in / reveal-right / reveal-left / scale-in），配 0.7s 带弹性的 `cubic-bezier(0.16, 1, 0.3, 1)` 曲线，延迟 0 / 0.08 / 0.18 / 0.3 / 0.44 / 0.6 / 0.78s。动效是系统身份的一部分，新页应使用该动画属性栈，而非自写过渡。

**密度取向：稀疏、能呼吸。** Grove 页面安静时显得优雅：一个标题、一段辅助正文、一排三个统计、两栏图文。8vw 横向、6.5vh 纵向内边距刻意宽裕。把 6 个元素塞进画布的页会破掉系统，一个标题 + 一段导语 + 一条强调线的页才权威。宁可更少、更大。系统奖励文字周围的静默，不奖励内容密度。

**关键特征：**
- Playfair Display 字重 400，绝不粗，用于每个衬线瞬间。`{colors.accent}` 斜体是标题强调。
- Jost 字重 300 用于每段正文。更轻字重是系统的"好纸"声部。
- JetBrains Mono 字重 300 大写、0.12em–0.2em 字距，用于每个标签、眉题、页脚线、计数器、图注。
- 深色页用 `{colors.bg}` 深森林绿配 `{colors.fg}` 暖奶油文字，浅色页用 `{colors.bg-light}` 羊皮纸配 `{colors.fg-light}` 绿文字。
- 一种强调色：`{colors.accent}` 陶土珊瑚。只给斜体标题强调、36px 珊瑚线、破折号项目、统计数字、章节序数、引号。
- 仅 1px 细线边（深色 `{colors.border}`、浅色 `{colors.border-light}`）。无粗边、无阴影、无渐变。
- JetBrains Mono 珊瑚色渲染的破折号字形是系统通用项目符号。
- 巨型衬线水印数字（`{components.grove-num}` 18vw、6% 不透明度）坐在章节与分节页右下角作构图纹理。
- 内置错峰淡入 / 揭示动画系统（`[data-anim]` + `[data-delay]`），新内容应使用它，而非无入场直接出现。

## 颜色

### 调色板
- **BG / Deep Forest**（`{colors.bg}` — #192b1b）：主导深色画布。深沉、有分寸的森林绿，落地、编辑，Grove 基底。默认幻灯片背景。
- **BG Alt**（`{colors.bg-alt}` — #1e3221）：略浅的森林绿，用于次级深色表面。作深色页上 `{components.img-placeholder}` 的填充，读起来是从画布往上一档色调，又不离开绿系。
- **BG Light / Parchment**（`{colors.bg-light}` — #e8e4d6）：浅色页用的暖羊皮纸表面。读起来是优质纸料，不是数字白。
- **BG Light Alt**（`{colors.bg-light-alt}` — #dedad0）：略冷的羊皮纸，用于次级浅色表面。可供相邻浅色区域之间作色调分隔。
- **FG / Warm Cream**（`{colors.fg}` — #d4cfbf）：深色表面上的主文字色。暖奶油，绝不纯白。这份米白温度对印刷墨感不可少。
- **FG-2**（`{colors.fg-2}` — rgba(212,207,191,0.6)）：深色上次级 / 柔化文字。用于导语、图注、需要往后退的辅助文案。
- **FG-3**（`{colors.fg-3}` — rgba(212,207,191,0.32)）：深色上三级 / 提示文字。几乎不可见，用于图片占位图注与最淡的元数据。
- **FG Light**（`{colors.fg-light}` — #192b1b）：浅色表面上的主文字。**与 `{colors.bg}` 共用同一十六进制**，深森林绿既作深色画布，也作浅底上的深色文字。这是系统主表面的文字反色装置。
- **FG Light 2**（`{colors.fg-light-2}` — rgba(25,43,27,0.58)）：浅色上次级柔化文字。
- **FG Light 3**（`{colors.fg-light-3}` — rgba(25,43,27,0.33)）：浅色上三级文字。
- **Accent / Terracotta Coral**（`{colors.accent}` — #c8524a）：唯一的暖音符。省着用：标题内斜体强调、眉题下 36px 珊瑚线、破折号项目、统计数字、章节序数、起始引号、导航点激活态。绝不作为表面填充，绝不用于正文段落。
- **Border**（`{colors.border}` — rgba(212,207,191,0.12)）：深色页上的细线分隔。12% 奶油，作为结构线可见但不响。
- **Border Light**（`{colors.border-light}` — rgba(25,43,27,0.14)）：浅色页上的细线分隔。14% 森林绿。

### 默认值
- **默认幻灯片背景**：`{colors.bg}`（深森林绿）作整稿主导色调。内容想要字面"页面"感时取 `{colors.bg-light}`（羊皮纸），通常用于引文页、较浅的章节或作对比。
- **深色表面默认主文字色**：`{colors.fg}`（暖奶油）。
- **浅色表面默认主文字色**：`{colors.fg-light}`（深森林绿，与深色表面同一十六进制）。
- **默认次级 / 柔化文字**：深色 `{colors.fg-2}`、浅色 `{colors.fg-light-2}`，用 `.muted` 工具类。
- **默认标题色**：跟随表面的主文字色。除标题内斜体 `<em>` 强调外，标题绝不出现在珊瑚里。
- **默认正文色**：跟随表面的主文字色。
- **默认边框色**：深色 `{colors.border}`、浅色 `{colors.border-light}`，都是 1px 实线细线粗细。
- **默认眉题 / 章节号色**：`{colors.accent}`（陶土珊瑚）。等宽大写眉题是唯一取强调色的外壳元素。
- **眉题下短 36px 构图线的默认线色**：`{colors.accent}`。满宽分节分隔线改用 `{colors.border}`。

配色刻意极简。深森林 / 浅羊皮纸 / 陶土珊瑚三元组就是整个色彩语汇。引入第四色（海军、黄、第二强调）会破掉系统的编辑克制。

## 排印

### 字族
系统从 Google Fonts 加载四款字族：

- **Playfair Display** 字重 400 与 500（斜体和正体）。**已发布页面只用字重 400。** 字重 500 加载了但预留，系统规则明确不允许粗衬线（字重 700）。
- **Jost** 字重 200、300、400、500。**只用字重 300。** 轻字重是系统的正文声部。
- **JetBrains Mono** 字重 300 与 400。**只用字重 300。** 轻等宽是外壳声部。
- **Noto Serif SC / Noto Sans SC** 字重 300–500，作为每个角色的中文回退链加载。

四字族栈按角色严格：Playfair 管每个衬线瞬间（展示、标题、引文、统计数字、水印），Jost 管每段正文和项目，JetBrains Mono 管每个标签 / 眉题 / 页脚线 / 计数器 / 图注。

### 展示、正文、外壳比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.grove-num}` | 18vw | Playfair | 400 | 水印序数数字，6% 不透明度，绝对右下 |
| `{typography.display}` | 10vw | Playfair | 400 | 封面英雄标题 |
| `{typography.quote-mark}` | 8vw | Playfair | 400 | 起始引号字形 |
| `{typography.h1}` | 5.5vw | Playfair | 400 | 章节标题、陈述标题 |
| `{typography.stat-value}` | 4.5vw | Playfair | 400 / 珊瑚 | 统计卡片数值 |
| `{typography.h2}` | 3.2vw | Playfair | 400 | 常规页面标题 |
| `{typography.quote-text}` | 3.2vw | Playfair | 400 斜体 | 引文正文 |
| `{typography.h3}` | 2vw | Playfair | 400 | 副标题、比较面板标题 |
| `{typography.lead}` | 1.45vw | Jost | 300 | 导语段 |
| `{typography.body-list-emph}` | max(1.4vw, 17px) | Jost | 300 | 列表页正文 / 项目，为可读性强调 |
| `{typography.body}` | 1.05vw | Jost | 300 | 标准正文段落 |
| `{typography.caption}` | 0.82vw | Jost | 300 | 图注、脚注、图表来源 |
| `{typography.label}` | 0.7vw | JetBrains Mono | 300 / 0.12em | 外壳标签、等宽元数据 |
| `{typography.kicker}` | 0.7vw | JetBrains Mono | 300 / 0.14em / 大写 | 标题上方眉题 |
| `{typography.chapter-num}` | 0.7vw | JetBrains Mono | 300 / 0.2em / 大写 | 章节序数标签 |
| `{typography.stat-label}` | 0.7vw | JetBrains Mono | 300 / 0.12em / 大写 | 统计数字下方等宽标签 |

### 默认值
- **常规页面标题默认尺寸**：`{typography.h2}`（3.2vw）。
- **章节或陈述标题默认尺寸**：`{typography.h1}`（5.5vw）。陈述类瞬间特别用 `{typography.h1-statement}`，封顶 `min(4.5vw, 7.5vh, 88px)` 防止矮视口溢出。
- **封面英雄标题默认尺寸**：`{typography.display}`（10vw）。
- **正文段落默认尺寸**：`{typography.body}`（1.05vw），Jost 字重 300。
- **导语 / 开场段落默认尺寸**：`{typography.lead}`（1.45vw）。
- **眉题 / eyebrow 默认尺寸**：`{typography.kicker}`（0.7vw），JetBrains Mono 大写 0.14em、`{colors.accent}` 色。
- **统计卡片数字默认尺寸**：`{typography.stat-value}`（4.5vw），Playfair 珊瑚。
- **每个衬线元素默认字重**：400。
- **每个正文 / Jost 元素默认字重**：300。
- **每个等宽 / JetBrains 元素默认字重**：300。

列表式页上的正文在常见笔记本视口下按 1.05vw 读起来偏小时，系统会提到 `{typography.body-list-emph}`（取 1.4vw 或 17px 的较大值）。页面主内容瞬间是正文段落或项目列表时取强调尺寸，默认 1.05vw 是为投影观看校准，不是笔记本阅读。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个 Playfair 元素都跑字重 400。** 系统任何地方都不用粗衬线（字重 700）。这是系统最重要的排印规则。
- **任何 Playfair 标题（h1、h2、h3 或引文）里的 `<em>` 标签都渲染成 `{colors.accent}` 珊瑚斜体。** 这是招牌 Grove 强调，给标题加强调的方式就是把一个词斜体成珊瑚。em 样式切换由 CSS 自动完成。
- **引文页上的起始引号渲染成 8vw 的巨型 Playfair 字形，`{colors.accent}` 珊瑚色。** 没有超大珊瑚引号的引文是坏的。
- **引文正文始终斜体。** 系统里不存在正体式引文文字。
- **每个眉题 / 章节号 / 页脚线 / 标签 / 图注都是 JetBrains Mono 大写、至少 0.12em 字距。** 句首大写或无字距的等宽读成代码，不像外壳。
- **项目字形是 JetBrains Mono `{colors.accent}` 珊瑚渲染的破折号（`—`）。** 绝不用圆点（`•`）、连字符（`-`）、星号。破折号是系统的项目语言。
- **每条外壳条（顶与底）都带 1px 实线 `{colors.border}` 线（浅色页 `{colors.border-light}`）。** 细线让外壳读作"页面周围的画框"，而非横幅。

### 排印原则
Playfair-400 / Jost-300 / JetBrains-Mono-300 的字重承诺是系统的声部，换掉任一款字重都会破掉编辑语域。没有字重阶梯，每款字面恰好一个字重。

斜体只留给两个特定角色：标题内的珊瑚强调（经 `<em>`）和引文正文。斜体正文段落不用。不用下划线。正文里的强调靠 `.accent` 颜色工具（把颜色改成珊瑚）传达，不靠斜体或粗体。

## 布局

### 画布系统
系统以流式视口为目标，每张 `.slide` 是 `100vw × 100vh`、`padding: {spacing.pad-y} {spacing.pad-x}`（6.5vh / 8vw）。幻灯片在横向 `#deck` flex 条里并排，经 `transform: translateX(...)` 配 `{motion.dur-slide}` / `{motion.ease-slide}` 过渡平移。同一时刻只有一页 `is-active`，非激活页内容保持不可见（`[data-anim]` 是 `opacity: 0`），直到 active 类触发入场动画。

### 内边距比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 8vw | 横向幻灯片内边距 |
| `{spacing.pad-y}` | 6.5vh | 纵向幻灯片内边距 |
| `{spacing.pad-quote-x}` | 8.8vw | 引文页略宽的横向内边距 |
| `{spacing.pad-quote-y}` | 7.8vh | 引文页略高的纵向内边距 |
| `{spacing.gap-lg}` | 4.5vh | 主内容分节之间 |
| `{spacing.gap-md}` | 2.8vh | 相关元素之间 |
| `{spacing.gap-sm}` | 1.4vh | 紧密耦合元素之间 |

### 外壳解剖
每张内容页顶部带 **slide-chrome**：一个细 flex space-between 行，两侧各一条等宽标签，下方由 1px 细线分隔；底部带 **slide-foot**：对应的一行，装分节名 + "NN / TT" 计数器，上方由对应的细线分隔。

封面、章节、引文、收尾页隐藏 chrome 与 foot，它们是整套文稿无外壳的情绪瞬间。其余每页都带画框。

### 圆角
**零结构半径。** 没有圆角卡片、圆角按钮、圆角图片占位。系统里唯一的圆是视口底部 5px 导航点（50% 半径，全圆）。

## 纵深与层级

### 平、无阴影
系统**零 box-shadow、零 text-shadow、零模糊、零渐变**。纵深完全靠：
1. **1px 细线边**：顶底外壳条、统计卡片分隔、比较面板分隔、分节分隔线。
2. **文字颜色的不透明度层**：主（`{colors.fg}`）、柔化（`{colors.fg-2}`）、提示（`{colors.fg-3}`）。三级不透明度阶梯是系统的文字抬升装置。
3. **6% 不透明度的水印数字**：巨型 Playfair 数字坐在章节与分节页右下角作构图纹理，不作 UI。

没有阴影本身就是抬升语言。加 `box-shadow: 0 4px 12px rgba(0,0,0,0.1)` 会击碎印刷墨感。

### 水印数字
`{components.grove-num}` 元素是 18vw / 6% 不透明度的 Playfair 数字，绝对定位在 `right: {spacing.pad-x}, bottom: -0.15em`。读作淡背景纹理，绝非内容。用在章节 / 分节 / 陈述页右下角，否则那里空着会显得没锚。它虽以装饰元素面貌出现，却属于纵深语言的一部分。

## 形状与处理

### 边框粗细与样式
- **1px 实线 `{colors.border}`**：深色页的通用细线。外壳条边、统计卡片底、比较面板分隔、满宽分节分隔。
- **1px 实线 `{colors.border-light}`**：浅色页上对应的细线。
- **1px 实线 `{colors.accent}`**：36px 宽的珊瑚线（`{components.rule-coral}`），作眉题与其后标题之间的构图节拍。

边框绝不粗于 1px，绝不用虚线、绝不用点线。1px 细线是系统的结构节奏。

### 装饰元素类型

**Slide Chrome 条**（`{components.slide-chrome}`）：细顶条，两侧等宽标签，下方 1px 细线。系统通用的"你在读一页"画框。

**Slide Foot 条**（`{components.slide-foot}`）：对应的底条，装分节名 + 计数器，上方 1px 细线。

**珊瑚线**（`{components.rule-coral}`）：36px 宽、1px 陶土珊瑚横线。坐在眉题（上）与标题（下）之间的构图节拍。每页用一次，眉题引向主标题处，别叠多条珊瑚线。

**满线**（`{components.rule-full}`）：`{colors.border}` / `{colors.border-light}` 的满宽 1px 细线分隔。用作页内分节断口。

**眉题**（`{components.kicker}`）：珊瑚色的等宽大写 eyebrow，放在 h1 或 h2 标题上方。常配下方一条珊瑚线。

**章节号**：珊瑚色的等宽大写序数（`{typography.chapter-num}`），在章节标题上方。在章节开场页确立章节身份。

**破折号项目**（`{components.bullet-list}`）：两列网格列表（2em / 1fr），项目是 JetBrains Mono 渲染的珊瑚破折号字形。绝不用真圆点（`•`），始终破折号。

**Grove 统计**（`{components.grove-stat}`）：纵向叠排，上方大 Playfair 珊瑚值（4.5vw）、下方等宽大写标签、1px 底边细线。无背景填充，卡片由线 + 字定义，不由容器盒子定义。

**引号标记**（`{components.quote-mark}`）：8vw 的巨型 Playfair 起始引号字形，珊瑚色，放在斜体引文正文上方。引文页始终出现。

**水印数字**（`{components.grove-num}`）：18vw / 6% 不透明度的 Playfair 数字，右下角。仅构图纹理，绝非 UI。

**图片占位**（`{components.img-placeholder}`）：实 `{colors.bg-alt}`（深色）或 `{colors.border-light}`（浅色）填充，标记真实 `<img>` 将放的位置。装一条 `{colors.fg-3}` 的等宽图注，如 "[ image ]"。

**导航点**（`{components.nav-dots}`）：固定在视口底部的 5px 圆点，指示页位置。未激活 22% 白，激活 80% 白、1.4× 缩放。

## 该做与不该做

### 该做
- 每个衬线瞬间都用 Playfair Display 字重 400，绝不粗。
- 任何 Playfair 标题里用 `<em>` 把一个词切到斜体陶土珊瑚，这是系统招牌强调手法。
- 每段正文都用 Jost 字重 300，更轻字重是系统的正文声部。
- 每个标签、眉题、章节号、页脚线、计数器、统计图注都用 JetBrains Mono 字重 300 大写、至少 0.12em 字距。
- 默认幻灯片背景设成 `{colors.bg}`（深森林绿）。引文页及任何想要字面"页面"感的瞬间用 `{colors.bg-light}`（羊皮纸）。
- 把眉题与 36px 珊瑚线配成单一构图单元，放在页面主标题上方。
- 用珊瑚色破折号字形（`—`）作通用项目符号，绝不用圆点或连字符。
- 给章节与分节开场页套 `{components.grove-num}` 水印数字，右下角需要那个锚。
- 每个新内容元素都用内置 `[data-anim]` + `[data-delay]` 动画栈（fade-up / fade-in / reveal-right / reveal-left / scale-in，延迟 0–6）。动效是系统身份的一部分，不是可选润色。
- 让页面宽裕，一个标题 + 一段辅助正文 + 一条强调线是节奏。宁可更少元素、更大尺寸。

### 不该做
- 不要用粗衬线。系统里没有字重 700 的 Playfair，粗衬线会破掉编辑声部。
- 不要引入 Playfair、Jost、JetBrains Mono、Noto SC 之外的第四款字体。四字族栈是全部排印身份。
- 不要用珊瑚作表面填充或正文段落。珊瑚是强调声部：斜体强调、眉题、线、破折号项目、统计数字、引号、章节序数。这就是珊瑚的全部语汇。
- 不要用 box-shadow、渐变、模糊或任何 rgba 阴影。系统是平的。
- 不要用粗边（2px+）。1px 细线是系统的结构节奏。
- 不要给任何角加圆角。唯一的圆是 5px 导航点。
- 不要用圆点、连字符或星号作列表项目。珊瑚破折号是唯一项目字形。
- 不要让眉题下方没有珊瑚线。眉题 → 线 → 标题三件套是一个单元。
- 不要把等宽文字渲染成句首大写或无字距。等宽始终是大写外壳、0.12em+ 字距。
- 不要省掉内容页的 slide-chrome 与 slide-foot。顶底细画框让页面读作一页。
- 不要把画布塞满。Grove 奖励文字周围的静默。页面显得满时，去掉一个辅助元素，别缩小文字。

## 响应式行为

系统通篇用 **vw / vh 单位**，每个尺寸、内边距、间隙、线都随视口成比例。同一构图在 1280×720 笔记本、1920×1080 显示器、2560×1440 屏上无需断点都能正确渲染。

### 缩放行为
- 展示标题随视口宽度线性缩放（10vw，1920 下 192px，1280 下 128px）。
- 正文同样缩放（1.05vw，1920 下 20.16px，1280 下 13.44px），唯列表页正文有 `max(1.4vw, 17px)` 下限，防止小视口上读不了。
- 内边距、间隙、grove-num 都随 vw/vh 成比例缩放。
- 1px 细线边是固定像素、不缩放，于是大视口下比例上显得更细，这是刻意的。

### 放映行为
- 右 / 下方向键 / 空格 / page-down 前进（由 deck JavaScript 处理）。
- 左 / 上方向键 / page-up 后退。
- 横向 `#deck` 条经 `transform: translateX(-N * 100vw)` 在页间平移，配 `{motion.dur-slide}` 锐减速曲线、0.9s。
- 每页带 `is-active` 类，触发 `[data-anim]` 元素的错峰入场动画。
- 底部导航点反映当前页位置，点击圆点跳到该页。

### 动画
`[data-anim]` + `[data-delay]` 系统内置：
- `fade-up`：opacity 0 → 1，translateY 28px → 0
- `fade-in`：opacity 0 → 1
- `reveal-right`：clip-path inset(0 100% 0 0) → inset(0 0 0 0)
- `reveal-left`：clip-path inset(0 0 0 100%) → inset(0 0 0 0)
- `scale-in`：opacity 0 → 1，scale 0.94 → 1

所有入场动画用 `{motion.ease-enter}` 配 `{motion.dur-enter}`（0.7s）。错峰延迟：0 / 0.08s / 0.18s / 0.3s / 0.44s / 0.6s / 0.78s。

### 打印 / 导出
系统没有 `@media print` 规则。打印导出会继承横向条布局，不太可能干净分页。把 Grove 当屏幕优先系统，PDF 导出需要专用打印样式表。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 中文字面 | 字重 | 理由 |
|---|---|---|---|
| 展示 / h1 / h2 / h3（Playfair 角色，2–10vw） | 霞鹜文楷 LXGW WenKai | 400 | 文学、手工排的暖意，映照 Playfair Display 字重 400，绝不粗，正是 Grove 规则 |
| 引文文字 / 标记（8vw 标记、3.2vw 文字） | 霞鹜文楷 LXGW WenKai | 400 | 同一份文学暖意承载斜体引文瞬间，中文没有斜体所以由字面承担表情工作 |
| 统计数字（4.5vw，珊瑚） | 霞鹜文楷 LXGW WenKai | 400 | 把统计数字留在 Playfair 语域，珊瑚色承载强调 |
| 水印数字（18vw） | 霞鹜文楷 LXGW WenKai | 400 | 6% 不透明度水印以 LXGW WenKai 开放字形在该尺度下成立 |
| 正文 / 导语（Jost 角色，1.05–1.45vw） | 思源宋体 Noto Serif SC | 300–400 | 明朝正文声部，平静、文学，像 Jost 字重 300 一样往后坐 |
| 标签 / 眉题 / 章节号（JetBrains Mono 角色） | 思源等宽 Noto Sans Mono CJK SC | 300–400 | 为眉题与页脚线保住打字机外壳质感 |

### 混排策略

用**策略 C**：保留 Playfair Display 作拉丁衬线，让 CJK 字形回退到 LXGW WenKai。Playfair Display 字重 400（绝不粗）是系统最重要的排印承诺，整体换成 CJK 衬线会破掉定义 Grove 的专著 / 精品品牌书语域。系统已按既有字体栈加载 Noto Serif SC / Noto Sans SC 作回退，改动是把 LXGW WenKai 作为首选 CJK 展示字面加在 Noto Serif SC 之前：

```css
/* Playfair roles (display, h1, h2, h3, quote, stat, watermark) */
font-family: 'Playfair Display', 'LXGW WenKai TC', 'Noto Serif SC', Georgia, serif;
/* Jost roles (lead, body, caption) */
font-family: 'Jost', 'Noto Serif SC', system-ui, sans-serif;
/* JetBrains Mono roles (label, kicker, chapter-num, stat-label) */
font-family: 'JetBrains Mono', 'Noto Sans Mono CJK SC', monospace;
```

（注：系统当前 Jost 栈里列的是 `'Noto Sans SC'`，为 Grove 的文学语域，换成 `'Noto Serif SC'`。明朝正文声部比黑体无衬线更接近 Jost 字重 300 的"好纸"感。）

展示尺寸（5.5–10vw）的基线错位轻微，LXGW WenKai 与 Playfair Display 光学基线相近，于是像 `A Quiet 山林` 这样的混排标题读起来干净。`<em>` 斜体珊瑚强调规则更微妙（见下方已知 CJK 缺口）。

### 加载

把既有仅 Noto 的回退换成 LXGW WenKai + Noto Serif SC + Noto Sans Mono CJK 组合：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=LXGW+WenKai+TC&family=Noto+Serif+SC:wght@300;400;500&family=Noto+Sans+Mono+CJK+SC:wght@300;400&display=swap" rel="stylesheet">
```

LXGW WenKai TC 是 Google Fonts 托管的版本（同时覆盖繁体和简体字形）。

### 通用 CJK 调整

以下调整适用于本系统**每一个 CJK 块**，无论尺寸或角色：

- **行高放宽 0.05–0.08。** CJK 字形是全宽方块，视觉分量比拉丁字形重，为拉丁调的行高（展示 1.0–1.1、正文 1.65–1.75）在中文里读起来局促。展示放到 1.15–1.25，正文放到 1.7–1.85。
- **去掉 CJK 标题的负字距。** Playfair Display 用 -0.01em 到 -0.03em 字距，会撞在一起。CJK 段设 `letter-spacing: 0`，标题看着挤时可用微小的正 `0.02em`。
- **绝不对 CJK 文字用 `text-transform: uppercase`。** 中文没有大小写，CSS 属性对汉字无效，却会悄悄破坏混排行里本该大写的 JetBrains Mono 部分。
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不用拉丁对应物（`,.:;!?""''()`）。同一句里混用标点系统读起来是排印错误。
- **CJK 标题末尾不加句号（。）。** 中文标题与拉丁遵循同一规则，标题式行去掉末尾标点。正文段落保留 。
- **在 CJK 与拉丁串交界处套用盘古之白。** 汉字与相邻拉丁词或数字之间应有一个空格（或 0.25em 外边距），例如 `2026 年 5 月` 而非 `2026年5月`。要么手打空格，要么用 `pangu.js` 式自动加空格器。
- **一句一款字体。** 不要在同一句里切换 LXGW WenKai 与 Noto Serif SC，挑与角色匹配的字面（展示 = LXGW WenKai，正文 = Noto Serif SC），整段从一而终。

### 本系统的美学提示

Grove 的整个声部是"文学专著 / 精品品牌书"，配一抹陶土珊瑚作单一强调。这种安静权威的中文对应是：每个衬线瞬间用 **LXGW WenKai**（手工排的暖意是最接近 Playfair Display 字重 400 的中文类比），正文用 **Noto Serif SC 字重 300–400**（匹配 Jost 字重 300 克制的明朝平静）。中文正文别用 Noto Sans SC，几何无衬线会把系统从"好纸"翻成"现代应用"。

DM Mono 珊瑚色破折号项目字形在中文里无需改动，破折号字符本身是同一个 Unicode 字形（—），放在中文列表项前读起来就是一个刻意的标记。项目列保持在 Noto Sans Mono CJK SC 字重 300 珊瑚，精确镜像拉丁模式。

水印数字（18vw、6% 不透明度）在中文里尤其有效，渲染一个中文序数字符（例如「三」或「五」）而非西方数字。6% 不透明度下它读作淡构图纹理，汉字在该尺度下更密的视觉分量比纤细的西方数字更能平衡页面。

### 已知 CJK 缺口

系统招牌的 `<em>` 斜体珊瑚处理最难汉化：**中文没有斜体概念**，倾斜的汉字读成坏了，不是强调。当前 Grove CSS 依赖浏览器默认 `<em>` 样式（斜体）加一条珊瑚色 CSS 规则。中文里斜体视觉上不起作用，于是强调塌成"标题里一段珊瑚文字"。这不算坏，LXGW WenKai 标题里的珊瑚仍是刻意的强调，但系统丢掉了两个强调维度（颜色 + 倾斜）之一，只剩颜色。

补偿有两个办法：（1）接受中文标题上仅颜色强调，让珊瑚承担分量，或（2）把中文标题里的 `<em>` 部分换成另一款字面，例如**站酷小薇体（ZCOOL XiaoWei）**，提供近似拉丁斜体倾斜反差的基于字面的对比。加进 CSS：

```css
.h1 em, .h2 em, .h3 em, .quote-text em {
  color: var(--c-accent);
  font-family: 'Playfair Display', 'ZCOOL XiaoWei', 'LXGW WenKai TC', serif;
  font-style: italic; /* Latin renders italic; CJK ignores */
}
```

这给拉丁部分斜体珊瑚、给 CJK 部分换字面珊瑚。逐套文稿测试，对许多 Grove 文稿，仅颜色强调已足够。

## 迭代指南

1. 任何新标题都是 Playfair Display 字重 400。从标题阶梯里挑尺寸（10vw display / 5.5vw h1 / 3.2vw h2 / 2vw h3），别自创尺寸。
2. 标题内任何新强调都用 `<em>`，自动渲染成斜体珊瑚。别手写颜色/斜体样式。
3. 任何新正文段落都是 Jost 字重 300、1.05vw（导语 1.45vw，列表式页 `max(1.4vw, 17px)`）。
4. 任何新标签 / 眉题 / 页脚线 / 计数器 / 图注都是 JetBrains Mono 字重 300 大写、至少 0.12em 字距。
5. 任何新外壳线（顶条、底条、分节分隔、统计卡片边）都是 1px 实线细线，深色 `{colors.border}`、浅色 `{colors.border-light}`。不要更粗的边。
6. 任何新项目列表都用 `{components.bullet-list}` 模式（两列网格、珊瑚等宽破折号）。别自写别的项目样式。
7. 任何新强调瞬间都用 `{colors.accent}` 陶土珊瑚。强调只给斜体标题强调、36px 线、破折号、统计数字、引号、章节序数、眉题文字，别无他用。
8. 任何新章节或分节开场页都在右下角带 `{components.grove-num}` 水印数字。
9. 任何新内容元素都带 `[data-anim]` 属性（fade-up、fade-in、reveal-right、reveal-left 或 scale-in）加 `[data-delay]`（0–6）作错峰入场。别自写过渡。
10. 拿不准时，加空间而非内容。Grove 的编辑语域是静默，不是密度。

## 已知缺口

- 四款 Google Fonts（Playfair Display、Jost、JetBrains Mono、Noto Serif SC / Noto Sans SC）经 `<link>` 加载。离线渲染会分别回退到 Georgia、system-ui、monospace 及系统衬线/无衬线承担 Noto 角色，能保住大致性格，但丢掉排印身份。离线 / 打印可靠性建议自托管。
- 系统加载了 Playfair 字重 500 与 Jost 字重 200/400/500，已发布 CSS 里未用，但可用。使用它们会破掉系统单字重承诺。
- `<em>` 斜体珊瑚处理依赖 CSS 规则 `.h1 em, .h2 em, .h3 em { color: var(--c-accent); }`，注意规则里**并未设置**斜体属性（注释块是空的）。斜体来自浏览器默认 `<em>` 样式。若某条样式覆盖去掉了默认斜体，珊瑚强调会丢掉斜体性格。
- grove-num 水印用 18vw 字号，极宽视口（3000px+）下会变得很大，可能挤到 slide-foot 区域。CSS 把它定位在 `bottom: -0.15em` 吸收一部分溢出，但极宽视口下很高的数字可能仍需调整。
- 竖向侧栏组件（`.grove-sidebar`）在 CSS 里加载了但显式禁用（`display: none !important`）。它本是章节标签装饰，读起来杂乱，slide-chrome 条已经提供分节名。
- 固定页码（`#slide-counter`）同样禁用，slide-foot 条已显示 "NN / TT"，固定计数器是重复。
- CSS 里有几个空规则块（`.h1 em { }`、`.grove-stat-val em { }`、`.quote-text { ... }`），看似早期迭代留下的桩。它们无作用，删掉没影响。
- 整套文稿具备双语意识（经 Noto Serif SC / Noto Sans SC 中文回退），但已发布源码里没有实际中文内容，双语支持是结构性的、未激活。
- 图片占位组件是布局预留，不是真实图片。把占位 div 换成 `<img>` 需手动匹配父级 flex 行为与背景。
