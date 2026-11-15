---
version: alpha
name: Monochrome (Ivory Ledger)
description: A literary editorial system rendered in black ink on cream paper. Ultra-light geometric sans (Jost at weight 200–300) carries every headline; Lora italic serif handles quote text and insight-card titles; JetBrains Mono provides the structural chrome. There are no chromatic accents — every color in the palette is a graphite or cream tone, and "accent" simply means "darker ink." The aesthetic borrows from independent research reports, scholarly monographs, and the quietest end of contemporary editorial design — closer to a printed journal than a tech presentation.

colors:
  cream-paper: "#FAFADF"
  cream-paper-2: "#F2F2D2"
  cream-paper-3: "#F0F0D4"
  cream-warm: "#F5F0E4"
  ink-black: "#1A1A16"
  ink-graphite: "#5E5E54"
  ink-graphite-light: "#8A8A80"

color-aliases:
  c-bg: cream-paper
  c-bg-light: cream-paper
  c-bg-cream: cream-warm
  c-fg: ink-black
  c-fg-light: ink-black
  c-fg-2: ink-graphite
  c-fg-3: ink-graphite-light
  c-accent: ink-black
  c-border: ink-black
  c-border-light: ink-black

typography:
  display:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 8.5vw
    fontWeight: 200
    lineHeight: 0.96
    letterSpacing: -0.02em
  h1:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 5vw
    fontWeight: 200
    lineHeight: 1.1
    letterSpacing: -0.01em
  h2:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 3.2vw
    fontWeight: 300
    lineHeight: 1.2
  h3:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 2vw
    fontWeight: 400
    lineHeight: 1.3
  lead:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.5vw
    fontWeight: 300
    lineHeight: 1.65
  body:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.1vw
    fontWeight: 300
    lineHeight: 1.7
  caption:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 0.85vw
    fontWeight: 300
    lineHeight: 1.55
  label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 0.72vw
    fontWeight: 400
    letterSpacing: 0.12em
    textTransform: uppercase
  quote-serif:
    fontFamily: "Lora, Noto Serif SC, Georgia, serif"
    fontSize: 3.2vw
    fontWeight: 400
    lineHeight: 1.35
  insight-serif:
    fontFamily: "Lora, Noto Serif SC, Georgia, serif"
    fontSize: 2.8vw
    fontWeight: 400
    lineHeight: 1.15
  stat-value:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 5.5vw
    fontWeight: 200
    lineHeight: 1.0
    letterSpacing: -0.03em
  flow-num:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 3.5vw
    fontWeight: 200
    lineHeight: 1.0
    letterSpacing: -0.02em

spacing:
  pad-x: 8vw
  pad-y: 6vh
  gap-lg: 5vh
  gap-md: 3vh
  gap-sm: 1.5vh

canvas:
  width: 100vw
  height: 100vh

components:
  rule:
    width: 36px
    height: 1px
    background: "{colors.ink-black}"
    description: "A 36-pixel hairline accent rule. The system's signature small punctuation mark — appears under chapter labels, beside kickers, above stat values."
  rule-full:
    width: "100%"
    height: 1px
    background: "{colors.ink-black}"
    description: "Full-width 1px hairline rule for chrome bands, foot bands, and section dividers."
  kicker:
    fontFamily: "{typography.label.fontFamily}"
    fontSize: "{typography.label.fontSize}"
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.ink-graphite-light}"
    description: "Muted mono uppercase eyebrow label above a headline."
  tag:
    border: "1px solid {colors.ink-black}"
    padding: "0.3em 0.8em"
    fontFamily: "{typography.label.fontFamily}"
    fontSize: "{typography.label.fontSize}"
    letterSpacing: 0.12em
    textTransform: uppercase
    description: "Bordered inline tag for version numbers, status labels."
  bullet-marker:
    content: "—"
    color: "{colors.ink-graphite-light}"
    fontFamily: "{typography.label.fontFamily}"
    description: "Em-dash in muted graphite via JetBrains Mono. The standard list mark; never a dot, never a check."
  insight-card:
    background: "{colors.cream-warm}"
    borderRadius: 16px
    padding: "3vh 2.5vw"
    description: "Tall rounded-rectangle card in cream tone (one of three near-identical creams). Holds a large Lora serif title and a Jost body block at the bottom."
  stat-cell:
    borderTop: "1px solid {colors.ink-black}"
    padding: "{spacing.gap-md} {spacing.gap-md} {spacing.gap-md} 0"
    description: "Rule-topped vertical cell with a 5.5vw weight-200 numeral, a Jost label, and a mono source note."
  timeline-dot:
    width: 8px
    height: 8px
    borderRadius: 50%
    background: "{colors.ink-black}"
    border: "2px solid {colors.cream-warm}"
    description: "Solid black dot with a cream border ring that punches through a horizontal connector rule."
  vtimeline-spine:
    width: 1px
    background: "{colors.ink-black}"
    description: "1px vertical rule that anchors a vertical timeline. Carries a 9px solid black dot at the top of each entry."
  pie-donut:
    width: "min(26vw, 42vh)"
    height: "min(26vw, 42vh)"
    borderRadius: 50%
    description: "Donut ring rendered by overlaying a same-color circular ::after pseudo on a conic-gradient or similar. Center cutout is the slide background."
  pyramid-bar:
    borderLeft: "2px solid {colors.ink-black}"
    background: "color-mix(in srgb, {colors.ink-black} N%, {colors.cream-paper})"
    description: "Horizontal pyramid level. Width grows down each level (36% → 100%); fill darkens up the pyramid via color-mix at increasing percentages."
  bar-fill:
    width: "100%"
    background: "{colors.ink-graphite-light}"
    opacity: 0.5
    description: "Vertical bar in muted graphite at half opacity. Accented variant uses solid ink-black at full opacity."
  img-placeholder:
    border: "1px solid {colors.ink-black}"
    background: "{colors.cream-paper-3}"
    color: "{colors.ink-graphite}"
    description: "Hairline-bordered cream void with a centered mono label. Used until photography is dropped in."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/monochrome/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Monochrome（Ivory Ledger）是一套**文学编辑系统**，建立在单一材料约束之上：奶油纸上的黑墨，别无他物。调色板有八个 token，其中七个是奶油或石墨的色调变体。没有彩色强调，"强调"色只是更深的墨。结果是一套读起来像精心排印的研究报告或安静的当代专著、而不像演示文稿的系统。

字体栈是三声部编辑搭配。**Jost** 字重 200、300、400 承载每个展示、标题、正文、标签，它的几何无衬线构造在极轻字重下依然平静，字重 200（展示）与字重 300（正文）的反差是系统的主排印节奏。**Lora** 斜体衬线只留给两个特定瞬间：引文正文与 insight 卡片标题。衬线斜体提供系统里唯一的排印暖意，出现在哪里，哪里就标示"这是人的声音"。**JetBrains Mono** 字重 400 承载每个结构标记：外壳标签、侧栏标记、版本号、页脚文字、项目破折号、坐标轴标签、日期。等宽全大写、字距 0.12em 或更宽。

配色分三个角色。**奶油纸**（`{colors.cream-paper}` 及其三个近乎一样的兄弟色调）是画布，页面从不是白，始终是暖的偏黄奶油。**黑墨**（`{colors.ink-black}`，实为 #1A1A16，极深的橄榄黑）是每一处文字、每一条边框、每一道分隔、每一个非装饰奶油的形状填充。**石墨**两档（`{colors.ink-graphite}` 作次级文字、`{colors.ink-graphite-light}` 作三级）处理柔化文案。这就是全部色彩系统。

纵深完全靠 **1px 细线** 与 **宽裕留白**。没有投影、没有渐变、没有抬升、没有氛围效果。两个区域要分开时，一条 1px 黑线隔开。一个区域要视觉分量时，给它更多内边距，而不是换填充色。insight 卡片表面与页面本身几近难分，卡片靠圆角与内边距定义，不靠反差跳变。

**密度取向：稀疏。** 宽裕留白主导、单一排印瞬间锚定页面时，Ivory Ledger 才显得优雅。横向内边距设到 8vw（全库最宽裕），内容通常只占画布中间 60–70%。用文字填满 80% 面积的页面读作局促，会破掉编辑阅读感。系统在要求代理留出空间，让一个 Jost-200 标题独自扛起一页几乎空白的幻灯片。需要密度时（研究时间轴、双栏密文铺排、12 行表格），系统仍能成立，只因字面极轻、线极细，连密集内容都读起来透气。

**关键特征：**
- 每页奶油纸背景（`{colors.cream-paper}`），绝不白、默认绝不深。奶油是表面，不是风格选择。
- 极轻 Jost（展示字重 200、正文字重 300）是主导排印声部。
- Lora 斜体衬线只出现在两个特定瞬间：引文正文与 insight 卡片标题。别处不用。
- JetBrains Mono 全大写、0.12em+ 字距处理每个结构标签、外壳标记、坐标轴、项目标记。
- 系统没有彩色强调。强调色是 `{colors.ink-black}`，略深的墨。
- 所有结构分隔都是 1px 黑色细线，外加招牌 36px 短线（`{components.rule}`）作小标点。
- 项目列表标记是柔化石墨色、JetBrains Mono 渲染的破折号。
- 宽裕的 8vw 横向内边距，模板库里最宽敞。

## 颜色

### 调色板

- **奶油纸**（`{colors.cream-paper}` — #FAFADF）：默认表面。暖偏黄，绝非纯白。每页背景都是这个色或近乎一样的变体。
- **奶油纸 Alt**（`{colors.cream-paper-2}` — #F2F2D2）：略深的奶油，用于内嵌表面。省着用，与默认奶油的差别几乎看不出。
- **奶油纸 Deep**（`{colors.cream-paper-3}` — #F0F0D4）：图片占位填充。饱和度略高的奶油，把一个空矩形与幻灯片表面区分开。
- **暖奶油**（`{colors.cream-warm}` — #F5F0E4）：insight / 时间轴页背景，更暖的色调，标示这些页是整套文稿里相关的一组亚美学瞬间。
- **墨黑**（`{colors.ink-black}` — #1A1A16）：每一处文字、每一条线、每一道分隔、每一条边框。极深橄榄黑，不是纯黑，特意选它来在奶油纸上取暖。
- **石墨墨**（`{colors.ink-graphite}` — #5E5E54）：次级文字色。用于柔化导语、密集页的正文段落、需要从标题分量往后退的标签。
- **浅石墨墨**（`{colors.ink-graphite-light}` — #8A8A80）：三级文字。用于眉题、坐标轴标签、来源注、项目标记、页脚外壳，一切该读作几乎不在场的结构元数据。

### 默认值

- **默认表面背景**：`{colors.cream-paper}`。系统默认单表面。
- **默认主标题色**：`{colors.ink-black}`。标题绝不出现在石墨或别的色调里。
- **默认正文色**：浅色页主文案 `{colors.ink-black}`，柔化导语段 `{colors.ink-graphite}`。
- **默认眉题 / 标签色**：`{colors.ink-graphite-light}`，最柔的石墨。标签该往后坐，不该领衔。
- **默认边框 / 分隔线色**：`{colors.ink-black}`，每条分隔都是实黑。没有柔化边框色调。
- **默认线粗**：1px。系统绝不用更粗的线。
- **默认"强调"色**：`{colors.ink-black}`，与主文字色相同。本系统里强调意味着更深的重点墨，不是彩色切换。
- **insight / 时间轴组默认暖表面处理**：`{colors.cream-warm}`，用来在色调上标出一组页，又不破掉单色配色。

系统没有暖 / 冷配对，没有语义色（红不表警告、绿不表成功），没有彩色强调。每处强调都来自排印（尺寸、字重、斜体切换）或来自一条线，绝不来自颜色。

## 颜色（续）

三个"insight 卡片表面"（`--c-card-a`、`--c-card-b`、`--c-card-c`）都是近乎一样的奶油调（#FAFADF、#F5F0E4、#FAFADF）。它们被刻意塌缩，卡片的区分本就该来自内边距与衬线标题，而非表面色。把三个卡片表面 token 当作同一个表面。

## 排印

### 字族

系统加载五款字面：**Jost**（字重 200、300、400、500、600）承载全部无衬线展示与正文；**Lora**（斜体与正体，字重 400、500、600）只承载引文文字与 insight 卡片标题；**JetBrains Mono**（字重 300、400、500）承载每个结构标签；**Noto Serif SC** 是 Lora 的 CJK 回退；**Noto Sans SC** 是 Jost 的 CJK 回退。

情绪语域是刻意的：
- Jost 字重 200 读作**安静、几何、近乎数学**。它是系统的编辑声部。
- Lora 斜体读作**文学、私人、手工排版**。它标示"这是人或引文的声音"，出现在哪里，语气就从分析切到抒情。
- JetBrains Mono 读作**档案、索引、结构**。它是系统的目录卡声部，版本号、日期、坐标轴标签，一切是元数据而非信息的文字。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 8.5vw | Jost | 200 | 封面或开场英雄展示，宽裕透气 |
| `{typography.h1}` | 5vw | Jost | 200 | 章节开场或分节断口标题 |
| `{typography.h2}` | 3.2vw | Jost | 300 | 内容页主标题 |
| `{typography.stat-value}` | 5.5vw | Jost | 200 | 统计单元里的大数值 |
| `{typography.quote-serif}` | 3.2vw | Lora 斜体 | 400 | 引文正文 |
| `{typography.insight-serif}` | 2.8vw | Lora | 400 | insight 卡片标题 |
| `{typography.h3}` | 2vw | Jost | 400 | 副标题、区域标题、流程步骤标题 |
| `{typography.lead}` | 1.5vw | Jost | 300 | 导语段或大号项目 |
| `{typography.body}` | 1.1vw | Jost | 300 | 正文段落 |
| `{typography.caption}` | 0.85vw | Jost | 300 | 图片图注、来源注、细则 |
| `{typography.label}` | 0.72vw | JetBrains Mono | 400 | 眉题、外壳标签、坐标轴标签、版本标记 |
| `{typography.flow-num}` | 3.5vw | Jost | 200 | 流程图里的大步骤数字 |

### 默认值

- **默认主分节标题**：`{typography.h2}`（3.2vw、字重 300）。常规内容页别去取 `{typography.h1}`，那个尺寸留给章节断口。
- **默认开场或封面展示**：`{typography.display}`（8.5vw、字重 200）。
- **默认正文段落尺寸**：`{typography.body}`（1.1vw、字重 300）。
- **默认导语段尺寸**：段落是标题下唯一一段辅助文字时用 `{typography.lead}`（1.5vw、字重 300）。
- **默认标签 / 眉题尺寸**：`{typography.label}`（0.72vw）。
- **任何展示元素默认字重**：200。Jost 200 是系统的展示声部。
- **正文默认字重**：300。

拿不准时，标准配对是标题用 `{typography.h2}`（字重 300）、辅助块一段 `{typography.lead}`（字重 300）。窄字重差（300 对 300，仅靠尺寸区分）是对的，Ivory Ledger 不靠重字重反差。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每个 Jost display、h1、h2、h3 元素都大小写混排**，绝不全大写。全大写专属 JetBrains Mono 标签。
- **每个标签、眉题、外壳标记、页脚、坐标轴标签、来源注都用 JetBrains Mono 全大写、至少 0.12em 正字距**（多数 0.14–0.18em）。本系统不存在句首大写式等宽。
- **引文正文始终是 Lora 斜体。** 用 Jost 排引文读起来是另一套设计系统。
- **insight 卡片标题始终是 Lora 正体（非斜体）。** 衬线字面是卡片的定义性视觉信号。
- **项目列表标记始终是 `{colors.ink-graphite-light}` 色 JetBrains Mono 的破折号。** 绝不用圆点、对勾、数字。
- **统计值、展示标题、流程数字都用 Jost 字重 200 配负字距。** 极轻字重加紧字距的组合是系统的展示招牌。
- **标题与正文着 `{colors.ink-black}`，柔化导语着 `{colors.ink-graphite}`，标签着 `{colors.ink-graphite-light}`。** 标题绝不承载石墨色调。

### 排印原则

Ivory Ledger 的节奏是**极轻 Jost + 两个特定瞬间的 Lora 斜体 + 加字距等宽标签**。把标题的 Jost 换成更重字重（500+）读作另一套系统。正文用 Lora 排读作另一套系统。标签用 Jost 而非 JetBrains Mono 排也读作另一套系统。每款字面的角色都窄且不动。

斜体只用在 Lora（引文正文），Jost 里不用。下划线哪儿都不用。正文强调不靠粗体，段内强调要么靠罕见的 Lora 斜体切换，要么靠留白隔离。

## 布局

### 画布系统

系统以流式 `100vw × 100vh` 视口为目标，所有尺寸用 `vw`/`vh`。文稿是一条横向 flex 条，页间过渡 0.9s 配平滑缓动曲线。动画 token（`fade-up`、`fade-in`、`reveal-right`、`reveal-left`、`scale-in`）可用，经 `data-delay` 属性错峰，在每页入场时运行。

### 内边距与间隙比例

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 8vw | 幻灯片横向内边距（全库最宽裕） |
| `{spacing.pad-y}` | 6vh | 幻灯片纵向内边距 |
| `{spacing.gap-lg}` | 5vh | 主内容分节之间 |
| `{spacing.gap-md}` | 3vh | 相关元素之间 |
| `{spacing.gap-sm}` | 1.5vh | 紧密相关元素之间 |

幻灯片容器在左侧额外预留 3.5vw 给一个竖向侧栏元素（源码里当前已禁用，见"已知缺口"），所以左侧总内边距约 11.5vw。内容坐落在这套宽裕的沟槽系统里。

### 外壳画框

多数内容页带 **chrome header** 与 **chrome foot**：各是一行 `flex space-between`、两条 JetBrains Mono 标签，由 1px 实黑线与页面正文隔开。封面型、章节断口、引文、收尾页型把 chrome 与 foot 都彻底隐去。

### 已禁用侧栏

CSS 定义了 `.slide-sidebar` 元素，左沟槽里一条细的 1px 黑竖线，配旋转的等宽标签自下而上读。源码用 `display: none !important` 显式禁用，注释说它读起来是"视觉噪声"。样式作为休眠产物留在 CSS 里，没有刻意的设计理由不要重新启用。

## 纵深与层级

### 无阴影，只有细线

系统在任何结构元素上都**零 box-shadow 声明**。纵深由三种机制建立：

1. **实 `{colors.ink-black}` 的 1px 细线**，外壳条下、页脚条上、比较面板之间、统计单元格上方、时间轴轨道上、图表基线上。这条线就是分隔、分隔符、结构标记。
2. **36px 短线**（`{components.rule}`），作章节标签下、眉题旁、或精致强调断口的小标点。
3. **宽裕留白**，主纵深信号是 8vw 横向沟槽与每个排印瞬间周围的空间。

### 无氛围效果

没有渐变、没有辉光、没有纹理、没有颗粒叠层。连环形图中心镂空也只是同色圆盖在 conic 环上，没有反差跳变。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0px | 每个结构元素，图片占位、统计单元、比较面板、表格、图表区 |
| 16px | 仅 insight 卡片 |
| 50%（圆） | 饼 / 环图形状、时间轴小圆点、vt-spine 圆点 |
| 999px（胶囊） | 无，不用胶囊 |

系统以方角为主。insight 卡片上的 16px 圆角是唯一的结构性柔边，也是把卡片与区域区分开的视觉信号。

### 边框粗细

- **1px 实 `{colors.ink-black}`**：通用结构线粗。用于每条分隔、每条外壳线、每条图表轴、每个单元格边框。
- **2px 实 `{colors.ink-black}`**：只用在金字塔条左边缘（`{components.pyramid-bar}`），作该图表类型略强的左锚。

没有更粗的边框，没有虚线边框（密集图表里一条 `1px dashed` 石墨提示除外），没有彩色边框。

### 装饰元素类型

**36px 短线**：36px 宽 × 1px 高的实黑水平强调线。系统的招牌标点。用在章节号下、眉题旁，或作精致的分节断口。

**眉题 / 等宽 eyebrow**：`{colors.ink-graphite-light}` 的柔化 JetBrains Mono 全大写标签，放在标题上方。eyebrow 刻意做到几乎不在场。

**带边框标记**：小行内元素，1px 黑边框、0.3em × 0.8em 内边距，装一条等宽全大写字符串。用于版本标记或状态标签。

**项目破折号**：`{colors.ink-graphite-light}` 色 JetBrains Mono 的 `—` 字形，经 CSS 网格标记列（`grid-template-columns: 1.2em 1fr`）前置到每个列表项。

**Insight 卡片**：略暖奶油表面上的 16px 圆角矩形（`{components.insight-card}`）。承载一个 Lora 正体标题（2.8vw 字重 400）和推到卡片底部的 Jost 正文块（字重 300）。卡片靠圆角与衬线标题辨认，不靠颜色反差。

**统计单元**：带 1px 实黑顶线（`{components.stat-cell}`）的竖向区域，装一个 5.5vw Jost-200 数字、一个 Jost 标签、一条小等宽来源注。三个统计单元并排是标准排列。

**时间轴圆点**：8px 实黑圆，配 2px 暖奶油边框环（`{components.timeline-dot}`），穿过横向连接线。环色与暖奶油页表面一致，让圆点读成浮在线上，而非横穿过去。

**竖向时间轴脊**：1px 宽实黑竖线（`{components.vtimeline-spine}`），每条条目顶端有 9px 实黑圆点。用于长的编年列表。

**饼 / 环形图**：min(26vw, 42vh) 尺寸的圆（`{components.pie-donut}`），经 `::after` 做同色圆形镂空形成环。图旁配一列图例。

**金字塔条**：水平条（`{components.pyramid-bar}`），2px 实黑左边缘，填充由 `color-mix(in srgb, ink-black N%, cream-paper)` 算出奶油到石墨的色调，五级里 N 从 4% 到 55%。宽度从 36%（顶层、最深）逐级到 100%（底层、最浅）。

**竖向条形图**：默认条是 50% 不透明度的柔化石墨（`{colors.ink-graphite-light}`），高亮条是全不透明度实黑。图表带 1px 黑左轴与 1px 黑基线。

**图片占位**：1px 边框的 cream-paper-3 矩形，居中一条等宽标签。在照片到位前使用。

**无箭头流程**：本系统的流程图明确不在步骤间用箭头。步骤间的留白暗示顺序，源码用一条 CSS 注释声明了这一点。

## 该做与不该做

### 该做
- 每页都用奶油纸背景（`{colors.cream-paper}`）。单表面画布是系统的地基。
- 每个标题都设 `{colors.ink-black}`，让字重（Jost 200）与尺寸干活。标题从不需要彩色切换。
- 任何展示瞬间都用 Jost 字重 200。极轻字重是系统定义性的排印声部。
- 只在文字是引文正文时取 Lora 斜体，只在是 insight 卡片标题时取 Lora 正体。衬线的两个角色不重叠。
- 每个结构标签、坐标轴标记、页脚、项目标记都用 JetBrains Mono 全大写、至少 0.12em 字距。等宽是目录卡声部。
- 每条结构分隔都渲染成 1px 实黑线。系统里没有更粗、没有柔化、没有虚线边框。
- 每个项目列表都用柔化石墨色 JetBrains Mono 的破折号标记。
- 留出宽裕留白。内容应舒适地坐在画布中间 60–70%，把内容挤到边缘会破掉编辑阅读感。

### 不该做
- 不要引入彩色。红、蓝、绿、黄在本系统里不存在。强调是更深的墨。
- 不要用重字重（Jost 500、600、700）做标题。展示文字重于 300，系统就读作坏了。
- 不要用 Jost 排引文。Lora 斜体正文是引文的身份，换成无衬线会塌掉排印区分。
- 不要给任何元素用 box-shadow。系统没有抬升。
- 不要用带彩色反差的卡片表面。insight 卡片靠圆角与衬线标题辨认，彩色填充会破掉单色读感。
- 不要把页面挤满。横向内边距 8vw 是有原因的，内容需要呼吸。
- 不要用粗体强调正文。行内强调很少用，要用就切 Lora 斜体，不要加字重。
- 不要把破折号项目标记换成圆点、对勾、箭头或数字。破折号是系统唯一的列表标记。
- 不要启用已禁用的侧栏（`.slide-sidebar`）。它是刻意藏起来的，重新启用会加回系统专门调掉的视觉噪声。
- 不要给 insight 卡片（16px）或真圆（圆点、环形）以外的任何元素加圆角。方角是结构默认。

## 响应式行为

系统按设计就是视口流式。所有尺寸用 `vw`/`vh`，同一构图在任意 16:9 视口上无需断点都能正确渲染。视口更小时排印与内边距线性缩放，视觉密度与负空间比例保持恒定。

### 放映行为
- 标准键盘导航：方向键、空格、Home、End。
- 移动端触屏滑动。
- 鼠标滚轮配防抖，防止连跳。
- 页间过渡动画 0.9s，配平滑缓动曲线。
- 每页可经 `data-anim`（fade-up、fade-in、reveal-right、reveal-left、scale-in）给单个元素声明入场动画，错峰延迟由 `data-delay="N"` 提供，N 映射到离散延迟档（0s、0.08s、0.18s、0.3s、0.44s、0.6s、0.78s、0.96s）。
- 带 `[data-anim]` 的元素起始不可见（opacity:0），在 `.is-active` 时入场，重访该页会重播入场。

### 打印行为
模板没有声明 `@media print` 规则。浏览器驱动的 PDF 导出只会抓到当前激活页，多页导出需逐页手动导航。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字面 | 中文字面 | 字重 |
|---|---|---|---|
| 展示 / 标题（Jost 200） | Jost | Noto Sans SC（思源黑体） | 700（可用的最重；CJK 用 200 读作坏了，见美学提示） |
| 正文 / 导语（Jost 300） | Jost | Noto Sans SC（思源黑体） | 400 |
| 引文 / insight 标题（Lora 斜体 / 正体） | Lora | Noto Serif SC（思源宋体） | 400 |
| 标签 / 等宽外壳（JetBrains Mono） | JetBrains Mono | Noto Sans SC | 400（别强给 CJK 套等宽，见美学提示） |

### 混排策略

策略 A：同一条 `font-family` 栈，拉丁优先回退。每个排印 token 已经列了 `"Jost, Noto Sans SC, system-ui, sans-serif"`（或 Lora 对应版）。拉丁字形用 Jost / Lora 渲染，CJK 字形自动落到 Noto Sans SC / Noto Serif SC。不需要按语言加类。像 `使用 Claude 思考` 这样的混排句在一个逻辑行里按文字各取正确字面。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@200;300;400;500;600&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&family=JetBrains+Mono:wght@300;400;500&family=Noto+Sans+SC:wght@300;400;500;700;900&family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 设 0
- 文字变换：CJK 不用 uppercase
- 全角标点（，。：；！？「」（））
- 展示标题不加句号（中文排印惯例）
- 盘古之白（CJK 与拉丁之间加空格：`使用 Claude` 而非 `使用Claude`）
- 一句一款字体

### 本系统的美学提示

Ivory Ledger 的定义性特征是 Jost 字重 200，奶油纸上纸薄的几何笔画。**Noto Sans SC 没有可用的 200 字重。** 它最轻的 300 仍比 Jost 200 读起来重，因为汉字每字笔画多得多。中文展示设 **Noto Sans SC 700** 来匹配 Jost 200 在奶油纸上的*视觉存在感*（反直觉，但中文读者在大尺寸下把轻字重看成贫血）。正文用 Noto Sans SC 400 配 Jost 300 才是对，奶油纸加石墨墨的瞬间可跨文字迁移。

Lora 斜体是系统在引文正文里的"人的声音"。**Noto Serif SC 没有斜体。** 中文引文彻底丢掉斜体，衬线字面自身承载编辑暖意。别用 `font-style: italic` 假造斜体，Noto Serif SC 会渲染出一个看起来坏掉的自动倾斜字形。

JetBrains Mono 的全大写加字距标签（0.12–0.18em）迁移不到 CJK。**中文标签设 Noto Sans SC 400、大小写混排、字距归 0。** 中文里的"目录卡"声部靠小尺寸与奶油纸浅色达成，不靠等宽加字距。标签若是纯拉丁（版本号、日期），按原设计保留 JetBrains Mono 全大写。

破折号项目标记（`—`）在中文里完美成立，中文破折号也是 `—`，渲染宽度相同。标记照原样保留。

### 已知 CJK 缺口

8vw 横向内边距（全库最宽裕）是为拉丁较窄的字形宽度调的。汉字大致成方，同字号下占更多横向空间。英文里一行放得下的长中文标题可能折成两行。标题是纯中文时，把展示标题尺寸降约 15%（Jost 8.5vw → Noto Sans SC 7.2vw），或接受折行作为编辑节奏的一部分。

## 迭代指南

1. 任何新页背景都是 `{colors.cream-paper}`（insight/时间轴亚美学用 `{colors.cream-warm}`）。绝不引入深色或彩色背景。
2. 任何新标题都用 Jost 大小写混排、字重 200（display、h1）或 300（h2）。绝不取更重字重。
3. 任何新标签、eyebrow、标记、元数据文字都用 JetBrains Mono 全大写、至少 0.12em 字距、着 `{colors.ink-graphite-light}`。
4. 任何新结构分隔都是 1px 实黑线。装饰强调取 `{components.rule}`（36px 短），区域分隔取 `{components.rule-full}`。
5. 任何新引文都用 `{typography.quote-serif}` 尺寸的 Lora 斜体。引文绝不出现在无衬线里。
6. 任何新卡片瞬间都用 16px 圆角与 Lora 正体标题。别引入方角卡片或无衬线标题卡片。
7. 任何新项目列表都用柔化石墨色 JetBrains Mono 的破折号。
8. 宽裕留白是特性，不是布局缺失。别因为有空间就填满。
9. 要强调某个瞬间，加大尺寸或把一段 span 包进 Lora 斜体。不要引入颜色。
10. 看着像彩色的颜色 token（如 `--c-accent`）其实别名到 `{colors.ink-black}`，它们为 token 兼容而存在、解析成黑。别给它们加彩色值。

## 已知缺口

- CSS 定义了 `.slide-sidebar` 元素（左沟槽里旋转的等宽标签），经 `display: none !important` 刻意隐藏。休眠样式留在源码里，未经设计评审重新启用会加回系统专门调掉的视觉噪声。
- 三个 insight 卡片表面 token（`--c-card-a`、`--c-card-b`、`--c-card-c`）解析成两个近乎一样的值（#FAFADF、#F5F0E4）。卡片的"颜色变化"实际上只是装饰，卡片靠衬线标题与内边距区分，不靠表面色调。
- 饼 / 环形图用 `::after` 伪镂空，要求图表背景与页面表面一致。背景不同的页（如暖奶油变体）需调整 `--c-bg-light` token，镂空才能正确消失。
- 金字塔图用 `color-mix(in srgb, ...)`，要求现代浏览器。旧浏览器会把条渲染成实 `{colors.cream-paper}`。
- 动画系统要求给页面加上 `.is-active` 类，入场动画才会播放。导航引擎没接好时，`[data-anim]` 元素会一直停在 opacity 0。
- Lora 斜体大尺寸（3.2vw 引文正文）的笔画反差明显宽过周围 Jost，这是刻意的，却造成可感的字重跳变。别把周围文字加粗来补偿。
- 条形图的 `bar-fill` 用内联 `style="height: XX%"` 声明，没有数据绑定层。高度手工计算。
- 系统在源码注释里原名 "Ivory Ledger"。模板库里以 "Monochrome" 暴露，两个名字指同一套设计系统。
