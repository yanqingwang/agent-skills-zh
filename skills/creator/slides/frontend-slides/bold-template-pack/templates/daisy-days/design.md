---
version: alpha
name: Daisy Days
description: A cheerful, childlike presentation system built around the chunky display face Fredoka One and the rounded humanist sans Quicksand. The palette is a sunny garden — cream canvas, turquoise, soft pink, butter yellow, mint, lavender, peach, sky blue, and a single coral accent — with charcoal-brown 2D outlines wrapping every shape. Hard offset shadows in dark charcoal, generous border-radius, and hand-drawn SVG decorations (daisies, stars, suns, clouds, rainbows) anchor the aesthetic somewhere between a children's storybook spread and a sticker-sheet kawaii zine.

colors:
  cream: "#F5F0E6"
  turquoise: "#7ECDC0"
  soft-pink: "#F7C8D4"
  butter: "#FDE68A"
  mint: "#A8E6CF"
  lavender: "#D4A5E8"
  peach: "#FFCBA4"
  sky: "#A8D8F0"
  coral: "#F8635F"
  text-dark: "#2D2D2D"
  text-muted: "#6B6B6B"
  white: "#FFFFFF"

borders:
  primary: "3px solid {colors.text-dark}"
  thin: "2px solid {colors.text-dark}"

shadows:
  default: "6px 6px 0 {colors.text-dark}"
  small: "4px 4px 0 {colors.text-dark}"
  text-headline: "3px 3px 0 {colors.text-dark}"
  text-headline-soft: "3px 3px 0 rgba(0,0,0,0.2)"

typography:
  display:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(3.2rem, 7vw, 6.5rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  headline:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(2.5rem, 5vw, 4.5rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  title:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(1.8rem, 3.5vw, 3rem)"
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.02em
  subtitle:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(1.3rem, 2vw, 1.8rem)"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  label-display:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(1rem, 1.5vw, 1.3rem)"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  quote:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(1.3rem, 2.5vw, 2rem)"
    fontWeight: 400
    lineHeight: 1.35
  body:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: "clamp(0.95rem, 1.3vw, 1.15rem)"
    fontWeight: 500
    lineHeight: 1.6
  body-strong:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: "clamp(0.95rem, 1.4vw, 1.15rem)"
    fontWeight: 600
    lineHeight: 1.5
  meta:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: "clamp(0.8rem, 1.1vw, 0.95rem)"
    fontWeight: 600
    lineHeight: 1.45
  badge:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "0.85rem"
    fontWeight: 400
    letterSpacing: 0.02em

spacing:
  pad-slide: "40px 60px"
  pad-card-lg: "48px 56px"
  pad-card-md: "32px 40px"
  pad-card-sm: "16px 24px"
  gap-grid-lg: "28px"
  gap-grid-md: "24px"
  gap-grid-sm: "14px"
  radius: "20px"
  radius-lg: "28px"
  radius-pill: "50px"
  radius-round: "50%"

canvas:
  width: 100vw
  height: 100vh

components:
  card:
    background: "{colors.white}"
    border: "3px solid {colors.text-dark}"
    borderRadius: "{spacing.radius}"
    boxShadow: "{shadows.default}"
  card-lg:
    background: "{colors.white}"
    border: "3px solid {colors.text-dark}"
    borderRadius: "{spacing.radius-lg}"
    boxShadow: "{shadows.default}"
  badge-pill:
    display: "inline-block"
    padding: "8px 20px"
    borderRadius: "{spacing.radius-pill}"
    border: "3px solid {colors.text-dark}"
    fontFamily: "'Fredoka One', cursive"
    fontSize: "0.85rem"
    background: "{colors.butter}"
  framed-header:
    description: "A two-part stacked card: a colored header strip (any accent surface) with rounded top corners and no bottom border, sitting flush above a white body with rounded bottom corners. The pair reads as a single unit with a tonal cap."
    headerBackground: "any accent surface"
    headerBorderRadius: "{spacing.radius-lg} {spacing.radius-lg} 0 0"
    bodyBackground: "{colors.white}"
    bodyBorderRadius: "0 0 {spacing.radius-lg} {spacing.radius-lg}"
    border: "3px solid {colors.text-dark}"
    boxShadow: "{shadows.default}"
  circle-dot:
    width: "48px"
    height: "48px"
    borderRadius: "{spacing.radius-round}"
    border: "3px solid {colors.text-dark}"
    fontFamily: "'Fredoka One', cursive"
    color: "{colors.white}"
    description: "Outlined colored disc holding a numeral or single letter. Used as timeline node, step marker, or list bullet anchor."
  circle-icon:
    width: "44px"
    height: "44px"
    borderRadius: "{spacing.radius-round}"
    border: "3px solid {colors.text-dark}"
    fontFamily: "'Fredoka One', cursive"
    background: "any accent surface"
    description: "Smaller cousin of circle-dot used as a card icon at the top of an info card."
  step-circle-lg:
    width: "90px"
    height: "90px"
    borderRadius: "{spacing.radius-round}"
    border: "3px solid {colors.text-dark}"
    fontFamily: "'Fredoka One', cursive"
    color: "{colors.white}"
    boxShadow: "{shadows.small}"
    description: "Oversized outlined disc used as a process step marker. Carries a hard offset shadow."
  avatar-circle:
    width: "100px"
    height: "100px"
    borderRadius: "{spacing.radius-round}"
    border: "3px solid {colors.text-dark}"
    background: "{colors.white}"
    boxShadow: "{shadows.small}"
    overflow: "hidden"
  bullet-dot:
    width: "20px"
    height: "20px"
    borderRadius: "{spacing.radius-round}"
    border: "2px solid {colors.text-dark}"
    background: "{colors.butter}"
    description: "Small outlined disc used as a ::before bullet for body list items, anchored 4px from the top of the line."
  list-dash:
    description: "A simple muted-text dash character used as a ::before bullet for compact in-card lists (day-card body)."
  legend-swatch:
    width: "18px"
    height: "18px"
    border: "2px solid {colors.text-dark}"
    borderRadius: "4px"
  decoration:
    position: "absolute"
    pointerEvents: "none"
    zIndex: 1
    description: "Hand-drawn SVG sticker (daisy, star, sun, cloud, rainbow) placed at slide corners and edges as atmospheric ornament. Often crops past the slide edge."
  nav-dots:
    position: "fixed"
    placement: "right edge, vertically centered"
    dotSize: "12px"
    dotBorder: "2px solid {colors.text-dark}"
    activeBackground: "{colors.butter}"
    activeTransform: "scale(1.2)"
  slide-counter:
    position: "fixed"
    placement: "bottom center"
    background: "{colors.white}"
    border: "3px solid {colors.text-dark}"
    borderRadius: "{spacing.radius-pill}"
    padding: "6px 20px"
    fontFamily: "'Fredoka One', cursive"
    boxShadow: "{shadows.small}"
  chart-container:
    background: "{colors.white}"
    border: "3px solid {colors.text-dark}"
    borderRadius: "{spacing.radius-lg}"
    boxShadow: "{shadows.default}"
    padding: "{spacing.pad-card-md}"
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/daisy-days/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Daisy Days 是一套**欢快、童趣的演示系统**，扎根于单一排印搭配：圆胖的展示字面 **Fredoka One** 用于每个标题，友好的人文无衬线 **Quicksand** 用于每一行正文与元文字。视觉语言源自绘本插画与贴纸页 kawaii：每个形状都带炭黑 2D 描边，每个抬升元素都投实色偏移阴影，每个表面都是阳光花园配色里的一抹浅彩。

色彩理念是**多浅彩配一抹暖爆点**。背景画布在柔和奶油（`{colors.cream}`）与饱和浅彩（`{colors.turquoise}`、`{colors.soft-pink}`、`{colors.butter}`、`{colors.mint}`、`{colors.lavender}`、`{colors.peach}`、`{colors.sky}`）之间交替。唯一高饱和强调是 `{colors.coral}`，省着用在小标记点和标题描边上，绝不作为整片表面。压在彩色表面上的标题得到 3px 炭黑文字阴影，让展示文字与周围形状有同样的描边外观，奶油上的标题保持平。正文文字绝不离开 `{colors.text-dark}` 或 `{colors.text-muted}`。

纵深是 **2D、图形化的**，不是摄影式的。每个抬升元素都得到 `{shadows.default}` 或 `{shadows.small}`，一块实色炭黑偏到右下、零模糊。厚炭黑描边加硬边偏移阴影的组合，给系统带来贴纸压纸感。没有渐变、没有辉光、没有玻璃效果。

招牌处理是**手绘 SVG 装饰层**。每个区域都带 3–7 个绝对定位的装饰物（黄心雏菊、多色星星、微笑太阳、蓬松云朵、拱形彩虹），簇在角落与边缘，常以 `top:-30px / right:-20px` 裁出页面边界。这些装饰坐在内容（`z-index:2`）后方的 `z-index:1` 层，带与系统其余部分一致的约 2px 炭黑描边，把装饰与结构统一起来。

**密度取向：满而不挤。** 系统每页承载一个聚焦内容区（卡片、画框、网格）在中央，加边缘一大圈角落装饰时显得权威。没有装饰的空角落读起来像坏了，装饰是结构构图的一部分，不是可选点缀。反过来，密集重叠的内容面板读起来焦躁，系统要的是一个被框住、被环绕的主体，而不是三个互抢的主体。目标是每页一个有边/带阴影的容器，由角落装饰填满画布其余部分。

**关键特征：**
- 奶油（`{colors.cream}`）默认画布配轮转浅彩表面，每页可挑不同表面色。
- Fredoka One 用于所有标题 / 展示 / 引文文字，Quicksand 500/600 用于所有正文与元文字。
- 每个形状与卡片都带 3px 实线炭黑描边（`{colors.text-dark}`）加硬边偏移阴影（`{shadows.default}` 或 `{shadows.small}`）。
- 宽裕圆角：标准卡片 20px，精选卡片 28px，徽章用胶囊（`{spacing.radius-pill}`），点与头像用整圆。
- 手绘 SVG 装饰物（雏菊、星星、太阳、云朵、彩虹）簇在角落、裁出页边，作氛围层。
- 彩色表面上的标题始终带 3px 实色炭黑文字阴影，奶油上的标题平放。
- 项目符号是带描边的彩色圆点（`{components.bullet-dot}`），不是字形，列表显得手工排的。
- 每页一个主内容容器，周围 3–7 个装饰物。空角落是错的。

## 颜色

### 调色板
- **Cream**（`{colors.cream}` — #F5F0E6）：默认画布。暖米白，读起来像纸料而非数字白。用作整套文稿的中性表面：标题开场、信息卡片页，任何想有故事书页感的地方。
- **Turquoise**（`{colors.turquoise}` — #7ECDC0）：中饱和青绿。表面浅彩里最响的一色，响到压在上头的标题需要炭黑文字阴影才读得清。
- **Soft Pink**（`{colors.soft-pink}` — #F7C8D4）：泡泡糖腮红。用作整片表面、页头条色、日期标记填充、引文卡片内的引号强调。
- **Butter**（`{colors.butter}` — #FDE68A）：奶油浅黄。导航点激活态色、徽章默认填充、项目圆点默认填充。系统里需要"被标记"感时的高亮色。
- **Mint**（`{colors.mint}` — #A8E6CF）：冷青瓷绿。表面色、页头条色、圆形图标填充、时间轴点色。
- **Lavender**（`{colors.lavender}` — #D4A5E8）：柔和紫。表面、页头条、标记点、日期标记，角色灵活度与薄荷、柔粉相同。
- **Peach**（`{colors.peach}` — #FFCBA4）：暖浅橙。用作表面（通常在流程或序列页）和强调。
- **Sky**（`{colors.sky}` — #A8D8F0）：浅蓝。表面与强调色，常与云朵装饰配对。
- **Coral**（`{colors.coral}` — #F8635F）：唯一饱和强调。只作标记填充（编号点、时间轴节点、步骤圆）和日期页眉，绝不作为整页表面。珊瑚是系统的"看这里"色，用多了就没劲了。
- **Text Dark**（`{colors.text-dark}` — #2D2D2D）：结构色。每条边、浅表面上的每段正文、每处阴影、每根 SVG 描边。比纯黑略暖，读起来是炭黑而非纯黑。
- **Text Muted**（`{colors.text-muted}` — #6B6B6B）：弱化文字色。副标题、标题下说明、列表破折号项目、角色标签。
- **White**（`{colors.white}` — #FFFFFF）：默认卡片填充，每张卡片、每个头像、每个图表容器内部。奶油画布上的卡片仍用白内部，卡片边才读得干净。

### 默认值
- **默认幻灯片背景**：`{colors.cream}`。页面想要调性个性时用饱和浅彩表面（青绿、柔粉、薄荷、奶油黄、薰衣草、桃、天蓝），不想要时默认奶油。
- **默认卡片背景**：`{colors.white}`，任何表面上都如此，包括浅彩表面。白压浅彩是标准卡片处理。
- **默认标题色**：`{colors.text-dark}`，始终如此。
- **默认正文色**：主正文 `{colors.text-dark}`，说明、角色标签、图注、副行用 `{colors.text-muted}`。
- **默认边框色**：`{colors.text-dark}`，始终如此。哪里都没有彩色边框。
- **默认阴影色**：`{colors.text-dark}`，始终如此。阴影从不是浅彩。
- **默认徽章填充**：`{colors.butter}`。
- **元素需要单一"注意"色时的默认标记 / 强调填充**：`{colors.coral}`。需要一串标记时，在序列步骤与点之间轮用整套浅彩（珊瑚 → 薄荷 → 天蓝 → 薰衣草 → 奶油黄）。
- **带框页眉组件上的默认页头条色**：任一浅彩表面，挑与页面表面色最和谐的一色。

浅彩在表面层可互换，不带固定语义（薄荷不是"成功"，珊瑚不是"警告"）。挑最贴合页面情绪语域的表面。唯一规则：珊瑚只留给小而高对比的强调，不作表面。

## 排印

### 字族
系统从 Google Fonts 恰好加载两款网页字体：**Fredoka One**（单字重圆润展示字面）与 **Quicksand**（人文无衬线，400/500/600/700 可用）。这个搭配就是全部排印身份。

Fredoka One 是圆胖的单字重展示字面，没有斜体、没有更轻变体、没有紧缩切分。展示字重按规格是 400，但因字形太圆太满，视觉上读起来像重字重。系统里每个标题、每个题目、每个步骤数字、每段引文都跑 Fredoka One。没有例外，用 Quicksand 做标题或 Fredoka One 排正文段落会立刻破掉系统。

Quicksand 承担其余一切：段落、列表项、角色标签、图注、日期卡片正文列表、图例文字。Quicksand 500 是正文默认，600 是强调正文用的"略强"变体（欢迎列表项、信息卡片说明、图例标签），700 省着用于引文作者出处。

### 展示、正文、标记比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | clamp(3.2rem, 7vw, 6.5rem) | Fredoka One | 400 | 封面 / 开场英雄标题 |
| `{typography.headline}` | clamp(2.5rem, 5vw, 4.5rem) | Fredoka One | 400 | 页面主标题 |
| `{typography.title}` | clamp(1.8rem, 3.5vw, 3rem) | Fredoka One | 400 | 分节标题或带框页眉标题 |
| `{typography.quote}` | clamp(1.3rem, 2.5vw, 2rem) | Fredoka One | 400 | 拉页引文正文 |
| `{typography.subtitle}` | clamp(1.3rem, 2vw, 1.8rem) | Fredoka One | 400 | 副标题、卡内标题 |
| `{typography.label-display}` | clamp(1rem, 1.5vw, 1.3rem) | Fredoka One | 400 | 小 Fredoka 标签，日期卡片页眉、步骤标题 |
| `{typography.body-strong}` | clamp(0.95rem, 1.4vw, 1.15rem) | Quicksand | 600 | 强调正文，欢迎列表、信息卡片说明 |
| `{typography.body}` | clamp(0.95rem, 1.3vw, 1.15rem) | Quicksand | 500 | 标准段落正文 |
| `{typography.meta}` | clamp(0.8rem, 1.1vw, 0.95rem) | Quicksand | 600 | 紧凑次级文字，日期卡片列表、步骤说明、图例行 |
| `{typography.badge}` | 0.85rem | Fredoka One | 400 | 胶囊徽章内文字 |

### 默认值
- **页面主标题默认尺寸**：`{typography.headline}`（clamp 2.5–4.5rem）。
- **封面级标题瞬间默认尺寸**：`{typography.display}`（clamp 3.2–6.5rem）。
- **段落默认尺寸**：`{typography.body}`（clamp 0.95–1.15rem），Quicksand 500。
- **强调列表项默认尺寸**：`{typography.body-strong}`（Quicksand 600）。
- **卡片标题下说明或元图注默认尺寸**：`{colors.text-muted}` 里的 `{typography.meta}`。
- **分节 / 带框页眉标题默认尺寸**：`{typography.title}`。
- **任何大于约 1.3rem 的文字默认字族**：Fredoka One。任何小于该值的文字：Quicksand。这个尺寸阈值大致对应 Fredoka / Quicksand 的角色边界。

拿不准时，页面主文字瞬间取 `{typography.headline}`，不要用 `{typography.subtitle}` 或 `{typography.title}`（它们是内容内标题，不是页面主声部）。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **放在饱和浅彩表面上的每个 Fredoka One 标题都带 3px 炭黑文字阴影**（青绿 / 薄荷等浓表面用 `{shadows.text-headline}`，柔粉 / 薰衣草等淡表面用 `{shadows.text-headline-soft}`）。奶油上的标题平放不带阴影。文字阴影让标题以"描边"的形态融入系统其余语汇。彩色表面上省掉它就读成坏了。
- **放在饱和表面上的标题把文字色换成 `{colors.white}`**；奶油上和浅彩卡片上的标题保持 `{colors.text-dark}`。搭配是饱和面上白、奶油或卡片上深。
- **每个正文列表项都用带描边的彩色圆盘作项目符号，不用字形。** 默认填充 `{colors.butter}`。项目符号渲染成 `::before` 的 20px 圆、2px 炭黑边，定位在首行顶部下 4px。
- **每段引文都用 Fredoka 引号标记处理**：一个超大 `"` 字形，`{colors.soft-pink}`，坐在引文文字上方。引文绝不不带引号锚出现。
- **Quicksand 正文文字绝不大写。** 正文上不做展示式全大写处理。Fredoka 自带个性，不需要喊。

### 排印原则
尺寸阶梯就是节奏。Fredoka One 不斜体、不下划线、不以别的字重渲染，Fredoka 只有一个字重，到此为止。Quicksand 待在 500 / 600 / 700 阶梯里，即便可用也别引入 400 或 800。Fredoka 字距保持规格默认 `0.02em`，Quicksand 字距保持 0。

系统不支持把 Quicksand 混进标题（例如给斜体短语换字面），标题跑一款字面。标题需要不同情绪语域时，靠尺寸和颜色，不靠换字体。

## 布局

### 画布系统
系统以全视口为目标，每张 `.slide` 是 `100vw × 100vh`、`padding: 40px 60px`（默认幻灯片内边距）。幻灯片在 `.slides-container` 内纵向堆叠，用 CSS scroll-snap（`scroll-snap-type: y mandatory`）把每页锁到视口。导航由固定右缘导航点、固定底部居中计数器胶囊、键盘方向键 / 空格、以及 intersection-observer 驱动的点状态处理。

### 内边距与间隙比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-slide}` | 40px 60px | 外幻灯片内边距 |
| `{spacing.pad-card-lg}` | 48px 56px | 大精选卡片（引文框、欢迎正文） |
| `{spacing.pad-card-md}` | 32px 40px | 标准卡片（图表容器、带框页眉正文） |
| `{spacing.pad-card-sm}` | 16px 24px | 紧凑卡片（时间轴卡片、日期卡片正文） |
| `{spacing.gap-grid-lg}` | 28px | 主网格间隙（团队网格、信息卡片网格） |
| `{spacing.gap-grid-md}` | 24px | 标准网格间隙 |
| `{spacing.gap-grid-sm}` | 14px | 紧网格间隙（每周日期卡片网格） |

### 圆角比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.radius}` | 20px | 标准卡片、日期卡片、时间轴卡片 |
| `{spacing.radius-lg}` | 28px | 精选卡片（图表容器、欢迎画框、引文框） |
| `{spacing.radius-pill}` | 50px | 徽章、页码 |
| `{spacing.radius-round}` | 50% | 所有圆（头像、项目点、标记点、步骤圆、图标） |

每个可见区域都带某种半径。除 SVG 装饰本身外，系统里零方角。

### 内容居中
幻灯片内容在内边距里纵向横向都 flex 居中。主内容容器的 max-width 随构图变化（典型 700–1100px），绝不铺满整页宽度，内容与页边之间始终留边距给装饰占据。

## 纵深与层级

### 硬边偏移阴影（唯一手法）
每个抬升元素用两个阴影值之一：
- **`{shadows.default}`** = `6px 6px 0 {colors.text-dark}`，卡片、画框、图表容器、徽章、页码的标准偏移。
- **`{shadows.small}`** = `4px 4px 0 {colors.text-dark}`，较小抬升元素（日期卡片、时间轴卡片、信息卡片、步骤圆、头像）的轻偏移。

阴影是**实色炭黑、零模糊、固定右下偏移**。没有 rgba 阴影、没有模糊、没有柔和抬升。一个元素要么投 `{colors.text-dark}` 的硬边偏移阴影，要么不投。

### 展示文字的文字阴影
另有单独的文字阴影处理，只给放在饱和浅彩表面上的展示标题：
- **`{shadows.text-headline}`** = `3px 3px 0 {colors.text-dark}`，用于浓浅彩表面（青绿、奶油黄、桃）。
- **`{shadows.text-headline-soft}`** = `3px 3px 0 rgba(0,0,0,0.2)`，用于淡浅彩表面（柔粉、薄荷），全炭黑在那里会显重。

奶油上的标题不带文字阴影。

### 装饰 z-index 层
氛围 SVG 装饰活在 `z-index: 1`、`pointer-events: none`。内容坐在 `z-index: 2`。这意味着装饰可以视觉上压住内容矩形，但绝不挡交互。装饰常以 `top:-30px / left:-30px` 之类的负偏移裁出页边，给布局"贴纸伸出纸面"的感觉。

## 形状与处理

### 边框粗细与样式
- **3px 实线 `{colors.text-dark}`**：通用结构边。卡片、带框页眉、徽章、标记圆、步骤圆、头像、图表容器、页码。
- **2px 实线 `{colors.text-dark}`**：轻边，只用于项目 / 导航点 / 图例色块 / 日期页眉分隔尺度的小元素。
- **约 2.1px 实线 `#232323` 或 `#000`**：雏菊 / 星星 / 云朵 / 太阳装饰内部的 SVG 描边粗细。这与 3px 结构边在 SVG 自然尺度下的观感粗细对齐。

边框从不上色，从不用虚线。系统里唯一的线样式是实色炭黑。

### 装饰元素类型

**雏菊**：六瓣白瓣 / 黄心雏菊，成对出现在两种茎位。系统招牌装饰。放在角落（通常 `top-left`、`top-right`、`bottom-left`、`bottom-right`），常以 `top:-30px` 或 `right:-20px` 裁出边缘。两朵雏菊加 2–3 颗星星是最常见的装饰簇。

**星星**：蓬松的五角贴纸星，实浅彩填充（粉、黄、薄荷、薰衣草、白）配炭黑描边。用作较大雏菊 / 太阳 / 云朵装饰之间的散落强调。同一页各实例填充色要变，别全用白星或全用黄星。

**太阳**：奶油黄色带光芒的微笑圆太阳。作单个特色装饰，通常左上或右下。

**云朵**：蓬松的白蓝云，可配更小的云变体。成对出现（对角两朵），或作单朵用在想要天空氛围的页上。

**彩虹**：拱形四带彩虹（珊瑚 / 黄 / 薄荷 / 天蓝），带标准炭黑描边。作单个特色装饰，通常右上或右下。

**带框页眉**（`{components.framed-header}`）：两段叠起的卡片，彩色页头条齐平坐在白正文上方。两者共享一个圆角外半径和一条连续 3px 边，整块投一枚偏移阴影。用作精选信息容器。

**徽章胶囊**（`{components.badge-pill}`）：短圆胶囊芯片，3px 边、奶油黄（默认）填充。用作分节标签或小标签。胶囊文字是 0.85rem 的 Fredoka One。

**标记圆组**：三种尺寸（`{components.bullet-dot}` 20px、`{components.circle-dot}` 48px、`{components.circle-icon}` 44px、`{components.step-circle-lg}` 90px）。都是带描边的圆、浅彩填充、炭黑边。较大标记圆里的数字或单字母始终是白字 Fredoka One（奶油黄底例外，文字回到深色）。

**头像圆**：100px 带描边白圆，装一个小人物 SVG 肖像或首字母。带 `{shadows.small}`。

**引号标记**：约 4rem 的超大 `"` 字形，Fredoka One，`{colors.soft-pink}`，放在引文卡片内引文正文上方。

**流程箭头**：约 2rem 的简单 `→` 字形，Fredoka One，`{colors.text-dark}`，坐在流程步骤之间。

**图例色块**：18px 方块，4px 圆角、2px 边。装与对应数据系列匹配的填充色。

## 该做与不该做

### 该做
- 严格按角色搭配 Fredoka One 与 Quicksand：每个标题和展示瞬间用 Fredoka，每个段落和元行用 Quicksand。两字面反差是系统的声部。
- 默认画布设成 `{colors.cream}`。页面想要调性情绪时用饱和浅彩表面（青绿、柔粉、薄荷等），内容多的瞬间奶油是稳妥默认。
- 每个抬升容器套 3px 实线炭黑描边加 `{shadows.default}` 或 `{shadows.small}` 硬边偏移阴影。描边 + 偏移阴影组合是系统招牌抬升。
- 放在饱和浅彩表面上的每个 Fredoka One 标题套 `{shadows.text-headline}` 文字阴影。只在奶油上省掉。
- 每页边缘簇 3–7 个手绘 SVG 装饰（雏菊、星星、太阳、云朵、彩虹），常裁出边界。这套系统里空角落看着像坏了。
- 用带描边的彩色圆盘作列表项目符号，绝不用光秃秃的连字符或星号。默认用 `{colors.butter}` 填充的 `{components.bullet-dot}`。
- 把 `{colors.coral}` 留给小而高注意力的标记（步骤数字、时间轴点、日期页眉）。珊瑚作整页表面会破掉暖平衡，读起来咄咄逼人。
- 主内容容器以远小于内边距的 max-width 居中。装饰需要边缘的空间，满出血内容会挡住装饰层。
- 序列需要区分步骤时，在浅彩组里轮用标记 / 点色（珊瑚 → 薄荷 → 天蓝 → 薰衣草 → 奶油黄）。别给所有步骤用一色。

### 不该做
- 不要用 Fredoka One 和 Quicksand 之外的任何字体。系统只从 Google Fonts 加载这两款。加第三字面会破掉故事书声部。
- 不要把 Quicksand 放进标题，或把 Fredoka One 放进段落。角色 / 字面映射是严格的。
- 不要用方角。每张卡片、每个徽章、每个标记都带某种半径，系统最小半径是 4px（图例色块），多数是 20px 或更大。
- 不要用模糊或 rgba 阴影。系统只用实色炭黑偏移。`0 4px 12px rgba(0,0,0,0.1)` 在这里不存在。
- 不要用彩色边框。所有边都是炭黑 `{colors.text-dark}`。
- 不要用珊瑚作整页表面。珊瑚是系统高注意力点色，盖住一个区域就没劲了。
- 不要把 Fredoka One 渲染成斜体、下划线或拉伸字重。Fredoka 只有一个字重，这就是设计。
- 不要省掉放在饱和浅彩表面上的 Fredoka 标题的文字阴影。阴影把标题分量统一进描边形状语汇。
- 不要留着页面角落没有装饰。装饰层是构图的一部分，不是可选打扮。
- 不要把两张卡片不加分隔地叠在一起。系统读作每页一个主内容区、由装饰环绕，不是一堆互抢的面板。

## 响应式行为

系统以视口流式布局为目标（一切用 `clamp()` 或 `vw`），但为桌面 / 投影在约 1280–1920 宽调过。两个响应式断点适配网格：

- **`@media (max-width: 768px)`**：幻灯片内边距收紧到 `24px 20px`。多列网格收拢：5 列每周网格降到 3，4 列团队网格降到 2，2 列信息卡片网格降到 1，横向流程流纵向堆叠且箭头旋转，横向圆环布局堆叠。右缘导航点隐藏。装饰不透明度降到 0.6，免得在局促布局里压过内容。
- **`@media (max-width: 480px)`**：3 列每周网格进一步降到 2。装饰不透明度降到 0.4。

### 放映行为
- scroll-snap-y mandatory 在纵向滚动时把每页锁到视口。
- 键盘：ArrowDown / ArrowRight / Space / PageDown 前进，ArrowUp / ArrowLeft / PageUp 后退，Home 跳首页，End 跳末页。
- 右缘导航点显示当前页，可点击跳转。
- 底部居中计数器胶囊显示 `N / total`，经 IntersectionObserver 更新。

### 打印 / 导出
没有定义 `@media print` 规则。打印导出会继承滚动容器布局，可能无法干净分页。把它当屏幕优先系统，PDF 导出需要单独的打印样式表。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 推荐中文搭配 | 来源 |
|---|---|---|---|
| 展示 / 标题（Fredoka One 400） | Fredoka One | 站酷小薇体 ZCOOL XiaoWei | Google Fonts |
| 正文（Quicksand 500–600） | Quicksand | 悠哉字体 Yozai | cn-fontsource CDN |

### 混排策略

用**策略 A — 单字体栈带回退**：在同一条 `font-family` 栈里把 ZCOOL XiaoWei 声明在 Fredoka One **之后**、Yozai 声明在 Quicksand **之后**，这样拉丁字形渲染成拉丁字面，CJK 字形自动落到中文字面。每个角色一条 CSS 规则，无需手动切类。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@400..700&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-yozai-regular/font.css" rel="stylesheet">
```

```css
:root {
  --font-display: "Fredoka One", "ZCOOL XiaoWei", cursive;
  --font-body: "Quicksand", "Yozai", sans-serif;
}
```

### 通用 CJK 调整

- **行高**：把 CJK 正文行高提到约 1.75（从 1.6 上调），汉字比拉丁小写需要更多纵向呼吸。
- **字距**：把汉字段上的 `letter-spacing` 清零（0.02em 的 Fredoka 字距会把汉字笔画挤在一起）。拉丁字距只保留在拉丁 span 上。
- **文字变换**：任何徽章/标签是汉字时，去掉 `text-transform: uppercase`。中文没有大小写；强制大写对汉字无效，却会破坏里面混排的拉丁缩写的渲染。
- **标点**：中文句子用中文全角标点（，。：；「」），拉丁用半角（`,.:;""`）。绝不把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略末尾的 。，展示字符串里要去掉。
- **盘古之白**：相邻的汉字与拉丁/数字串之间插入一个细空格（或普通空格），例如 `2026 年`、`AI 产品`，提升混排可读性。
- **一句一款字体**：不要在句中切换 CJK 字族。按角色在 ZCOOL XiaoWei 或 Yozai 里挑一款给某段文字，绝不在同一短语里两款都用。

### 美学提示

ZCOOL XiaoWei 圆润柔和的展示语域是 Fredoka One 圆胖故事书声部最接近的汉字类比，它在标题尺度上带着同样的"友好童书"情绪，又不会甜到发腻。Yozai 开放的字怀与适度的笔画对比贴合 Quicksand 的人文暖意，于是正文段落和元行与浅彩花园美学连贯。放在饱和浅彩表面上的标题所带 3px 炭黑文字阴影，在 ZCOOL XiaoWei 上同样成立：青绿 / 奶油黄 / 桃表面上的中文标题套 `{shadows.text-headline}`，柔粉 / 薄荷上套 `{shadows.text-headline-soft}`，与拉丁规则完全一致。彩色项目圆点、手绘 SVG 装饰（雏菊、星星、太阳、云朵、彩虹）、带框页眉的盖帽 + 正文模式、浅彩标记轮转都与内容无关。Fredoka One 的单字重约束干净地映射到 ZCOOL XiaoWei 的单字重约束，两款字面都不支持斜体、下划线或字重轴变化，保住系统"一款字重、每角色一款字面"的纪律。

### 已知 CJK 缺口

ZCOOL XiaoWei 是单字重展示字面，相比 Noto 家族字形覆盖有限，生僻或技术汉字（罕见姓氏、古字、GB2312 之外的仅简体变体）可能回退到系统字体。繁体中文文稿把 Yozai 换成 `LXGW WenKai TC`（Google Fonts），它繁体覆盖更全、同样带友好的人文语域。ZCOOL XiaoWei 读起来比 Fredoka One 的圆胖憨态略偏文学端正，用 Daisy Days 搭的中文文稿会比拉丁原版多约 20% "平静浅彩"、少约 20% "贴纸页 kawaii"。手绘 SVG 装饰（雏菊、星星、太阳、云朵、彩虹）承载着排印略丢的故事书情绪，所以中文文稿可考虑每页簇 5–7 个装饰（3–7 区间的上端）找回俏皮分量。

## 迭代指南

1. 任何新容器都是圆角（20px / 28px / 胶囊 / 圆）、3px 炭黑描边、带 `{shadows.default}` 或 `{shadows.small}` 阴影。绝不出一个方角平矩形。
2. 任何新标题都是 Fredoka One。若坐在饱和浅彩表面上，得到 3px 炭黑文字阴影并换成 `{colors.white}`；若坐在奶油或白卡片上，保持 `{colors.text-dark}` 并省掉阴影。
3. 任何新段落默认 Quicksand 500，需要强调时 Quicksand 600。
4. 任何新项目符号都是带描边的彩色圆盘（`{components.bullet-dot}`），不是字形。默认填充奶油黄，但圆形项目可在浅彩组里轮转。
5. 任何新标记序列（步骤、时间轴节点、日期标签）都在浅彩组里轮转（`coral → mint → sky → lavender → butter`），不复用一色。
6. 任何新页都需要 3–7 个 SVG 装饰簇在角落与边缘。从既有装饰类型里挑（雏菊、星星、太阳、云朵、彩虹），别引入新的装饰风格（例如线描箭头、照片剪贴）。
7. 任何新强调表面都从八种浅彩里挑。别引入第九色。
8. 珊瑚保持小标记色专用。别做珊瑚表面、珊瑚卡片或珊瑚标题。
9. 任何列表项目符号坐在首行文字顶部下 4px，与 x-height 竖向对齐，不与行基线对齐。
10. 新组件需要"两段画框"感时，取 `{components.framed-header}` 模式（彩色盖帽 + 白正文），而不是把两张独立卡片叠起来。

## 已知缺口

- 两款 Google Fonts（Fredoka One、Quicksand）经 `<link>` 从 Google Fonts CDN 加载。离线渲染会回退到 `cursive` 与 `sans-serif` 系统默认，整套排印身份塌掉。离线 / 打印可靠性需要自托管字体。
- 手绘 SVG 装饰（雏菊、星星、太阳、云朵、彩虹）是内联 SVG，描边色硬编码为 `#232323` 或 `#2D2D2D`。没有编程方式给它们重染成新配色，扩展装饰库要编写新的 SVG 源文件。
- 系统用 scroll-snap 导航（不是绝对定位幻灯片），没有专用打印样式表，整套文稿的 PDF 导出开箱即用地不会一页一页分页。
- 导航点 / 页码 / 键盘 / observer 的 JavaScript 内联嵌入，并经 `<div class="nav-dot">` 数组硬编码页数。加新页要手动加对应的 nav-dot div。
- 浅彩表面（青绿、薄荷、桃）感知亮度不一，标题的文字阴影处理必须逐表面调（系统已经这么做了，浓表面全炭黑、淡表面 20% 不透明度炭黑）。新表面色需要类似的调校决策。
- `--text-muted` 色（#6B6B6B）用于副标题和图注，但对浅彩表面对比有限。柔化文字留给奶油或白卡片上用，别直接压在浅彩表面上。
- 装饰 SVG 里含一条占位注释串 `SVG created with Arrow, by QuiverAI (https://quiver.ai)`，这是原作者工具署名，删掉不影响渲染。
