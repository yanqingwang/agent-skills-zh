---
version: alpha
name: Creative Mode
description: A neo-brutalist editorial presentation system built for 1920x1080 slides. The deck anchors on a warm cream canvas with heavy 4px ink borders, hard offset drop-shadows, and a bold four-color accent palette (forest green, hot pink, burnt orange, sunshine yellow). Display headlines run Archivo Black in pure uppercase — aggressive, loud, zero letter-spacing softness. Monospace labels in JetBrains Mono echo a typesetting rule-sheet. Body copy sits in Space Grotesk. Every slide uses flat color-blocking with no gradients, no rounded cards, and no subtlety. The aesthetic is part Bauhaus grid, part punk zine, part Swiss editorial.

colors:
  cream: "#EFE9D9"
  cream-2: "#E4DCC4"
  ink: "#0F0F0F"
  ink-2: "#2A2A2A"
  green: "#1F8A4C"
  green-dark: "#136636"
  pink: "#F06CA8"
  pink-dark: "#D14E8B"
  orange: "#E85A1F"
  yellow: "#F5C518"

typography:
  display-jumbo:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 220px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-hero:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 160px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-xl:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 140px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-lg:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 100px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-md:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 96px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-sm:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 84px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-xs:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: -0.01em
    textTransform: uppercase
  stat-num:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 96px
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: 0
  step-num:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 140px
    fontWeight: 400
    lineHeight: 0.85
    letterSpacing: 0
  step-title:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 34px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  stamp-num:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: 0
  marker-label:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 46px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  badge-label:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  table-head:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  table-label:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  body-lg:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  mono-label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.06em
    textTransform: uppercase
  mono-kicker:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.14em
    textTransform: uppercase
  mono-tag:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.1em
    textTransform: uppercase
  mono-chart:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase

spacing:
  slide-gutter: 96px
  chrome-gutter: 64px
  grid-gap: 28px
  cell-pad: 32px
  step-pad: 28px
  topbar-top: 48px
  meta-bottom: 40px
  table-cell-pad: 18px 26px

canvas:
  width: 1920px
  height: 1080px

components:
  slide-chrome:
    topbar:
      fontFamily: "JetBrains Mono, monospace"
      fontSize: 24px
      letterSpacing: 0.08em
      textTransform: uppercase
      position: absolute
      left: 64px
      right: 64px
      top: 48px
    topbar-pill:
      border: "2px solid {colors.ink}"
      padding: 6px 14px
      borderRadius: 999px
    slide-meta:
      fontFamily: "JetBrains Mono, monospace"
      fontSize: 24px
      letterSpacing: 0.06em
      textTransform: uppercase
      position: absolute
      left: 64px
      right: 64px
      bottom: 40px
    slide-meta-dot:
      width: 10px
      height: 10px
      background: "{colors.ink}"
      borderRadius: 50%
  stat-cell:
    border: "4px solid {colors.ink}"
    padding: 28px 32px
  stat-cell-green:
    background: "{colors.green}"
    color: "{colors.cream}"
  stat-cell-pink:
    background: "{colors.pink}"
    color: "{colors.ink}"
  stat-cell-cream:
    background: "{colors.cream}"
    color: "{colors.ink}"
  stat-cell-orange:
    background: "{colors.orange}"
    color: "{colors.cream}"
  step-card:
    border: "4px solid {colors.ink}"
    padding: 28px
    height: 420px
  step-card-cream:
    background: "{colors.cream}"
    color: "{colors.ink}"
  step-card-pink:
    background: "{colors.pink}"
    color: "{colors.ink}"
  step-card-yellow:
    background: "{colors.yellow}"
    color: "{colors.ink}"
  step-card-green:
    background: "{colors.green}"
    color: "{colors.cream}"
  step-arrow:
    borderTop: "18px solid transparent"
    borderBottom: "18px solid transparent"
    borderLeft: "24px solid {colors.ink}"
  table:
    border: "4px solid {colors.ink}"
    background: "{colors.cream-2}"
    rowBorder: "3px solid {colors.ink}"
    colBorder: "3px solid {colors.ink}"
  table-head-row:
    background: "{colors.ink}"
    color: "{colors.cream}"
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 28px
    borderColor: "{colors.cream}"
  table-col-pink:
    background: "{colors.pink}"
    color: "{colors.ink}"
  table-col-green:
    background: "{colors.green}"
    color: "{colors.cream}"
  table-col-orange:
    background: "{colors.orange}"
    color: "{colors.cream}"
  marker-block:
    background: "{colors.pink}"
    border: "4px solid {colors.ink}"
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 46px
    hardShadow: "24px 24px 0 {colors.orange}, 24px 24px 0 4px {colors.ink}"
  iso-panel:
    background: "{colors.green}"
    border: "4px solid {colors.ink}"
  stacked-block:
    border: "4px solid {colors.ink}"
    hardShadow: "18px 18px 0 {colors.ink}"
  badge-rotated:
    background: "{colors.yellow}"
    border: "4px solid {colors.ink}"
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 28px
    textTransform: uppercase
    transform: rotate(-4deg)
  stamp:
    background: "{colors.pink}"
    border: "4px solid {colors.cream}"
    width: 340px
    height: 340px
    transform: rotate(-6deg)
  stamp-inner:
    border: "4px solid {colors.cream}"
    borderRadius: 50%
  kicker-block:
    background: "{colors.ink}"
    color: "{colors.cream}"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.14em
    textTransform: uppercase
    padding: 8px 16px
  bar-chart-bar:
    border: "3px solid {colors.ink}"
  bar-chart-axis:
    borderRight: "3px solid {colors.ink}"
    borderBottom: "3px solid {colors.ink}"
  decorative-circle:
    background: "{colors.yellow}"
    border: "4px solid {colors.ink}"
    borderRadius: 50%
  closing-slide:
    background: "{colors.green}"
    color: "{colors.cream}"
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/creative-mode/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Creative Mode 是一套**新粗野主义编辑式幻灯片系统**，面向 1920x1080 演示。底层美学选择是手法克制、表达张扬：没有圆角卡片、没有渐变、没有暗示光源的阴影，只有平色块与硬边偏移投影（"Risograph" 或"丝网印"那种同色实色偏移的阴影）。

画布是暖奶油（`{colors.cream}` — #EFE9D9），近黑墨（`{colors.ink}` — #0F0F0F）用于边框、文字、分隔线。四种强调色以全饱和开火：森林绿、亮粉、焦橙、阳光黄。它们从不交融，在页上彼此碰撞，碰撞就是设计。

标题跑 **Archivo Black**（因展示字面天生厚重，用字重 400），严格大写、紧行高（0.92）。字号极端：收尾页 220px，标题 160px。**JetBrains Mono** 承载所有元数据、标签、顶栏文字、轴标签，强化"设计成品"或"技术手册"语域。**Space Grotesk** 处理所有正文段落。

每页遵循同一套外壳画框：顶部 48px 处一条 JetBrains Mono 顶栏（左文字 + 右胶囊），底部 40px 处一条 JetBrains Mono 元信息页脚（左标签，右页码，中间墨点分隔）。内容住在这个画框里，左右各留 96px 栏距。

**关键特征：**
- 奶油画布（`{colors.cream}` — #EFE9D9）作通用背景，绿（`{colors.green}` — #1F8A4C）只给收尾页用。
- 每个结构元素（卡片、面板、表格单元格、图表轴）都有 4px 实线墨边。
- 硬边偏移盒阴影取代模糊投影：精选块上 `24px 24px 0 color, 24px 24px 0 4px ink`。
- Archivo Black 展示字大写成 0.92 行高，紧到极致。
- 四种强调色作平填充，每页用其中两到三种，绝不同时用全四种。
- 顶栏胶囊徽章（JetBrains Mono、2px 墨边、999px 半径）是每页唯一的圆角元素。

## 颜色

### 画布与墨
- **Cream**（`{colors.cream}` — #EFE9D9）：通用幻灯片背景。暖，不是白。把整套文稿与冷冰冰的白底幻灯片区分开。
- **Cream 2**（`{colors.cream-2}` — #E4DCC4）：深一档的奶油。只用作比较表格的背景填充，在墨边内部造出微微下陷的表面。
- **Ink**（`{colors.ink}` — #0F0F0F）：近黑，用于所有边框、正文文字、分隔线、顶栏外壳、收尾印章边。不是纯 #000000，略柔化。
- **Ink 2**（`{colors.ink-2}` — #2A2A2A）：更柔的近黑，用于次级正文文字、统计单元格内的说明、图表脚注。

### 强调色
- **Green**（`{colors.green}` — #1F8A4C）：森林绿。主导强调色。适用于统计单元格、图示面板、流程步骤，以及作整页背景取得最大视觉冲击。
- **Green Dark**（`{colors.green-dark}` — #136636）：更深的绿变体，可供操纵杆/纵深装饰效果使用。不作主表面填充。
- **Pink**（`{colors.pink}` — #F06CA8）：亮粉。高能量。适用于开关拨钮插图、分节标记、统计单元格、流程步骤、印章元素。
- **Pink Dark**（`{colors.pink-dark}` — #D14E8B）：更深的粉，用于装饰操纵杆的纵深，可供阴影侧强调使用。
- **Orange**（`{colors.orange}` — #E85A1F）：焦橙。精选块上的硬边投影色，也作统计单元格填充、条形图色、表格列背景。
- **Yellow**（`{colors.yellow}` — #F5C518）：阳光黄。适用于装饰圆、流程步骤、旋转徽章、条形图条。暖标点色。

## 排印

### 字族
系统用三款字面，各守严格语域：
- **Archivo Black**：展示标题、步骤数字、统计数字、表格标签、所有大写呈现文字。天生厚重，无需额外 font-weight。
- **JetBrains Mono**：所有元数据，顶栏标签、元信息页脚、眉题标签、图表轴、图例行、层小片、图注。承载"技术规格"声部。
- **Space Grotesk**：仅正文，正文栏文字（slide 2）、统计单元格描述、图示副文、步骤说明、收尾标语。

### 展示比例
幻灯片画布是 1920x1080px，所以字号远大于网页常规。

| Token | 尺寸 | 用途 |
|---|---|---|
| `{typography.display-jumbo}` | 220px | 巨型标题或收尾标题 |
| `{typography.display-hero}` | 160px | 主文稿标题或英雄名 |
| `{typography.display-xl}` | 140px | 分节开场展示标题 |
| `{typography.display-lg}` | 100px | 配面板的分节标题 |
| `{typography.display-md}` | 96px | 中等分量分节标题 |
| `{typography.display-sm}` | 84px | 数据密集布局的分节标题 |
| `{typography.display-xs}` | 72px | 网格布局的分节标题 |
| `{typography.step-num}` | 140px | 阶梯布局里的大序数数字 |
| `{typography.stat-num}` | 96px | 统计或数据单元格里的大数字 |
| `{typography.stamp-num}` | 64px | 印章或封印数字 |
| `{typography.marker-label}` | 46px | 精选标记或标注块标签 |
| `{typography.step-title}` | 34px | 卡片或步骤标题 |
| `{typography.table-head}` | 28px | 表头或标签行文字 |
| `{typography.badge-label}` | 28px | 旋转徽章或注释标签 |

### 等宽比例
所有 JetBrains Mono 文字都是 24px。字距按用途变化：
- 顶栏标签：0.08em
- 元信息页脚：0.06em
- 眉题标签（反色）：0.14em
- 图表轴：0.08em（经 `{typography.mono-chart}`）
- 图例行：0.06em
- 层小片：0.1em

### 正文比例
- `{typography.body-lg}`（28px）：宽栏布局或导语段的正文。
- `{typography.body-md}`（24px）：统计单元格、图示注释、步骤说明、脚注、标语行的正文。

### 原则
Archivo Black 行高 0.92，标题会压到自身的 cap-height，这是刻意的。展示字面大小写锁定不可商量，小写 Archivo Black 会破掉编辑语域。等宽字面用宽裕字距（0.06–0.16em）读起来像打字机标签。绝不给 Archivo Black 或 Space Grotesk 加字距。

## 布局

### 画布系统
每页恰好 1920×1080px，固定、不滚动的视口。`deck-stage` 自定义元素负责居中与缩放。

### 栏距系统
- **外壳栏距**（左右 64px）：只给顶栏和 slide-meta 用。
- **内容栏距**（左右 96px）：给所有内容用，标题、正文、网格。
- 标题偶尔向右推到距右缘 96px 内，或受 `right: 1000px` / `right: 900px` 约束，好与右侧面板图示共存。

### 外壳画框（所有页）
```
┌─ topbar @ top:48px, left:64px, right:64px ──────────────────────────────────┐
│  SECTION LABEL                                       [pill badge]            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   CONTENT (96px left gutter, 96px right gutter)                            │
│                                                                              │
├─ slide-meta @ bottom:40px, left:64px, right:64px ───────────────────────────┤
│  DESCRIPTOR LABEL                                    01 • 08                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 纵深与层级

系统**零模糊阴影**。纵深用两种手法表达：

### 硬边偏移阴影
招牌处理：第二个实色形状在 X 和 Y 上都偏移固定量。用两个值：
- **大偏移**（24px 24px）：精选块如标记与海报开关，`box-shadow: 24px 24px 0 {colors.orange}, 24px 24px 0 4px {colors.ink}`。第一层阴影是彩色偏移，第二层是围着它的墨边。
- **中偏移**（18px 18px）：图示里的堆叠块，`box-shadow: 18px 18px 0 {colors.ink}`。纯墨阴影。

### 色块反差
纵深感知来自表面并置：奶油压 cream-2（表格）、墨压奶油（眉题块）、绿压奶油（图示面板）。反差够用时不需要阴影。

### 平元素
顶栏、元信息页脚、图表轴线、图例色块：平，无阴影，无 border-radius。

## 形状与处理

### 圆角
- **0px（方）**：所有结构元素，统计单元格、步骤卡片、表格单元格、图表条、图示面板、堆叠块。不圆。
- **50%（圆）**：图示内的装饰圆（黄色 circ）、顶栏胶囊点（slide meta 分隔点）。
- **999px（胶囊）**：仅顶栏徽章胶囊。这是系统整体方角里唯一的例外，读起来像标签芯片而非卡片。
- **旋转元素**：比较徽章旋转 -4deg，收尾印章旋转 -6deg。这些是系统仅有的非正交摆放。

### 边框
- **4px 实线 `{colors.ink}`**：所有结构边，统计单元格、步骤卡片、图示面板、表格（外）、海报块、标记块、开关块、印章。
- **3px 实线 `{colors.ink}`**：所有内部结构线，表格行、表格列、图表轴、条形图条。
- **2px 实线 `{colors.ink}`**：顶栏胶囊徽章。
- **3px 虚线 `{colors.ink}`**：流程页里把顶栏与流程卡片分开的横向虚线。

### 装饰元素
- **开关拨钮**：粉色方块配操纵杆形状（倾斜 div）和厚/深底面，橙色偏移阴影配墨边。
- **堆叠块**：四个重叠的绝对定位矩形，粉、黄、橙、cream-2，带 18px 墨色硬阴影。
- **圆形叠层**：绿方块中央的黄色圆，形状反差充当装饰图形。
- **印章**：带奶油色圆形内边的粉色旋转方块，作封印或核准标记。

## 该做与不该做

### 该做
- 每个结构元素用 4px 墨边。更细显得软，更粗像网页组件。
- 硬边阴影只用两种尺寸：精选英雄块 24px，图示堆叠块 18px。别混尺寸。
- 所有 Archivo Black 用法保持大写。字面句首大写读起来像另一个品牌。
- 四种强调色每页成组用两到三种。一种颜色全上就是噪声。
- 把绿底留给单独一页主导。稀有才有冲击力。
- 所有标签、元数据、索引、图注、轴文字用 JetBrains Mono。绝不用于正文或标题。
- 所有展示文字行高保持 0.92。行距一松就破掉紧编辑语域。
- 所有页一致维持 96px 内容栏距与 64px 外壳栏距。

### 不该做
- 不要给卡片角加圆（顶栏胶囊除外）。圆角提示"友好 SaaS"，尖角提示"编辑精确"。
- 不要用渐变、带模糊的投影或辉光效果。所有纵深必须来自硬边偏移或色彩反差。
- 不要把 Archivo Black 用成句首大写。绝不把展示字面小写化。
- 不要给 Archivo Black 加字距（已编码的 -0.01em 除外）。额外字距会破掉它的密度。
- 不要引入第五种强调色。四色配色是品牌约束。
- 不要用纯白（#ffffff）作背景。奶油才是画布，白读起来是空白。
- 不要用 Space Grotesk 做标签或元数据。那个角色属于 JetBrains Mono。
- 不要加更多字面。三字族栈已经完整。
- 不要把正文居中。所有正文左对齐，居中文字会破掉网格纪律。
- 不要柔化印章或徽章的旋转。-4deg 与 -6deg 是刻意的"不完美"信号。

## 响应式行为

本模板**专为 1920x1080 演示显示设计**。它不是网页，没有移动端断点。`deck-stage` web 组件通过 CSS transform 处理视口缩放，1920x1080 画布在任何屏上等比缩放而不改布局。

### 触摸 / 放映行为
- 幻灯片通过键盘方向键或演示翻页笔前进（由 `deck-stage.js` 处理）。
- 没有定义也不需要悬停态。
- 没有交互式表单元素。

### 打印 / 导出行为
- 在 96dpi 下，1920x1080 画布对应标准 20x11.25 英寸画框。
- PDF 导出建议按 1920x1080 视口抓取，或浏览器 100% 缩放打印成 PDF。
- 在 1pt = 1.333px 下，标题的实际打印尺寸从 54pt（72px）到 165pt（220px），适合海报/标题卡。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 推荐中文搭配 | 来源 |
|---|---|---|---|
| 展示 / 标题（Archivo Black 大写 400） | Archivo Black | 思源宋体 Noto Serif SC 900 | Google Fonts |
| 正文（Space Grotesk 400） | Space Grotesk | 思源宋体 Noto Serif SC 400 | Google Fonts |
| 等宽 / 标签（JetBrains Mono 大写） | JetBrains Mono | JetBrains Mono（仅拉丁/数字，等宽外壳保留拉丁） | Google Fonts |

### 混排策略

用**策略 A — 单字体栈带回退**：在同一条 `font-family` 栈里把 Noto Serif SC 声明在拉丁字面**之后**，这样拉丁字形渲染成 Archivo Black / Space Grotesk，CJK 字形自动落到 NSC。JetBrains Mono 外壳保持拉丁/数字专用：顶栏标签、slide-meta、轴刻度、图注不需要 CJK 回退（JetBrains Mono 按设计没有 CJK 字形）。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Grotesk:wght@300..700&family=JetBrains+Mono:wght@400..500&family=Noto+Serif+SC:wght@400;900&display=swap" rel="stylesheet">
```

```css
:root {
  --font-display: "Archivo Black", "Noto Serif SC", sans-serif;
  --font-body: "Space Grotesk", "Noto Serif SC", sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
}
/* Display headlines use Noto Serif SC 900; body uses NSC 400. */
```

### 通用 CJK 调整

- **行高**：把 CJK 正文行高提到约 1.55（从 1.4 上调），汉字比拉丁小写需要更多纵向呼吸。展示 NSC 900 在 100–220px 下保持紧行高约 1.0（NSC 重磅在展示尺寸下比 Archivo Black 需要更少的行距）。
- **字距**：把汉字段上的 `letter-spacing` 清零（讨好 Archivo Black caps 的负字距会把汉字笔画挤在一起）。紧字距只保留在拉丁 span 上。
- **文字变换**：任何展示/标签/等宽内容是汉字时，去掉 `text-transform: uppercase`。中文没有大小写；强制大写对汉字无效，却会破坏里面混排的拉丁缩写的渲染。
- **标点**：中文句子用中文全角标点（，。：；「」），拉丁用半角（`,.:;""`）。绝不把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略末尾的 。，展示字符串里要去掉。
- **盘古之白**：相邻的汉字与拉丁/数字串之间插入一个细空格（或普通空格），例如 `2026 年`、`AI 产品`，提升混排可读性。
- **一句一款字体**：不要在句中切换 CJK 字族。某段文字挑 Noto Serif SC 的单一字重，绝不在同一短语里用两个。

### 美学提示

Creative Mode 的新粗野语域依赖 Archivo Black 在 100–220px 下的极端密度，没有汉字字面匹配这种分量，思源宋体字重 900 是最接近的可用替代。NSC 900 带调制的衬线笔画读起来比朋克 zine 的 Archivo Black 更文学，但四色块配色、4px 墨边、硬 24px 偏移阴影承担了大部分粗野工作，排印变成更响系统里的一个组件，而非系统本身。Archivo Black 的"始终大写"规则对汉字毫无意义（没有大小写），内容切到中文时把 `text-transform: uppercase` 和 -0.01em 字距都去掉，NSC 900 单靠尺寸和颜色立住。JetBrains Mono 外壳（顶栏胶囊、slide-meta、轴刻度、眉题块）刻意保持拉丁/数字专用：`04 / 08` 页码用等宽渲染，但元信息页脚里任何中文描述标签用 NSC 400。四种强调（绿 / 粉 / 橙 / 黄）、统计单元格色块、表格处理、装饰几何（印章、徽章、堆叠块）都与内容无关。

### 已知 CJK 缺口

**厚重拉丁展示没有精确的 CJK 对应。** Archivo Black 在 220px 下的粗野密度是系统签名，思源宋体字重 900 是常用汉字里最重的字重，但读起来是文学衬线而非海报怪诞体。用 Creative Mode 搭的中文文稿会比拉丁原版少约 30% "朋克 zine" 感，补偿办法是更倚重强调色块、硬边偏移阴影、旋转徽章 / 印章元素。别改用 `Smiley Sans Oblique` 作展示，它的斜切与系统严格正交的矩形几何冲突。NSC 没有斜体轴，但系统哪里都不用斜体，没有损失。等宽外壳的"技术规格"声部最好靠把全部 JetBrains Mono 内容保持拉丁/数字、NSC 只留给标题和正文角色来保住。

## 迭代指南

1. 新页布局必须遵守外壳画框：topbar 在 top:48px left:64px，slide-meta 在 bottom:40px left:64px。
2. 内容从每侧边缘 96px 处起。
3. 加数据区（图表、表格、网格）时，上方配展示标题、内部配 JetBrains Mono 标签。
4. 每页挑两到三种强调填充。绝不在单页把四种全混上。
5. 硬阴影只给精选单元素（标记、精选块）。网格单元格不各配阴影。
6. 新步骤/统计卡片沿用现有配色序列模式：奶油与强调色交替，序列以绿收尾。
7. 所有边都是 4px 实线墨。表格或轴内的内部子边是 3px 实线墨。
8. 旋转元素（徽章、印章）用单一固定角度（-4deg、-6deg）。别引入别的角度。
9. 图标与插图是纯 CSS 几何形状（div、边框、伪元素）。不需要外部图片或 SVG。

## 已知缺口

- `deck-stage.js` 脚本（前进、键盘导航）是外部依赖，本文件未描述。
- 幻灯片之间的动画与过渡不在本模板范围内，所有页都是静态的。
- 标题页海报含一个由嵌套 div 搭的装饰开关拨钮插图，没有功能状态。
- 图表数据（条高、数值、标签）以内联样式和占位内容硬编码，没有数据绑定层。
- 表格数据全是占位，不支持动态填充。
- `--rule` CSS 变量（#0F0F0F，与 `--ink` 相同）已定义但未显式使用，它留给横向分隔线元素，可视为 ink 的别名。
- Archivo Black 的字体回退是 `sans-serif`，必须从 Google Fonts 加载该字体，设计才能正确渲染。
