---
version: alpha
name: Retro Windows
description: A Windows 95 / 98 desktop-OS aesthetic rendered as a presentation system. Every slide is a window — beveled chrome, navy gradient title bar, MS Sans Serif body type, with chart areas, group boxes, and panels arranged as if they were software UI from 1995. The palette is the original Win9x system colors (gray button-face, navy title bars, white sunken inputs) with retro accent hues (DOS green, brick red, mustard yellow, teal cyan) reserved for status text and chart data. Pixel-font (Press Start 2P) and terminal-font (VT323) appear sparingly for nostalgic punctuation. The effect is half playful nostalgia, half functional dashboard — a deck that reads as a software product running on a CRT monitor.

colors:
  bg-gray: "#c0c0c0"
  bg-light: "#d4d0c8"
  bg-dark: "#808080"
  white: "#ffffff"
  black: "#000000"
  text-dark: "#222222"
  blue-navy: "#000080"
  blue-bright: "#0000a0"
  blue-light: "#1084d0"
  green-retro: "#008000"
  red-retro: "#800000"
  yellow-retro: "#808000"
  cyan-retro: "#008080"
  text-gray: "#555555"

color-aliases:
  btn-face: bg-light
  btn-highlight: white
  btn-shadow: "#404040"
  btn-dark-shadow: black

typography:
  body:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  text-xl:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
  text-lg:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
  text-md:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
  text-sm:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  text-xs:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
  metric-xl:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.1
  title-bar:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.5px
  group-box-title:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.0
  pixel-display:
    fontFamily: "'Press Start 2P', cursive"
    fontSize: "20–24px"
    fontWeight: 400
    lineHeight: 1.8
  terminal:
    fontFamily: "'VT323', monospace"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
  nav-hint:
    fontFamily: "'VT323', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.0

spacing:
  slide-pad: "24px 32px 44px 32px"
  win-body-pad: "20px 24px 24px 24px"
  panel-pad: 16px
  group-box-pad: "20px 18px 16px 18px"
  panel-sunken-pad: 12px
  gap-1: 6px
  gap-2: 10px
  gap-3: 16px
  gap-4: 24px

canvas:
  width: 100vw
  height: 100vh

components:
  crt-overlay:
    backgroundImage: "repeating-linear-gradient(0deg, rgba(0,0,0,0.03) 0px, rgba(0,0,0,0.03) 1px, transparent 1px, transparent 3px)"
    zIndex: 9999
    description: "Fixed, full-viewport scanline overlay at 3% black opacity that sits above all content. Imitates the horizontal phosphor lines of a CRT monitor. Pointer-events disabled."
  win-window:
    background: "{colors.bg-light}"
    border: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    boxShadow: "inset 1px 1px 0 {colors.white}, inset -1px -1px 0 #404040"
    description: "The signature framing element. Every slide is one (or more) win-window. The asymmetric border + double inset shadow creates the Win9x beveled raised effect — top-left highlighted, bottom-right shadowed."
  win-titlebar:
    background: "linear-gradient(90deg, {colors.blue-navy} 0%, {colors.blue-bright} 100%)"
    color: "{colors.white}"
    padding: "4px 8px"
    fontSize: 14px
    fontWeight: 700
    description: "Navy-blue gradient bar at the top of every window. Contains a left lockup (icon + filename in caps) and a right cluster of three minimize/maximize/close buttons (_, [], X)."
  win-titlebar-inactive:
    background: "linear-gradient(90deg, #808080 0%, #a0a0a0 100%)"
    description: "Grayed-out title bar variant for inactive/secondary windows (used when a slide contains multiple stacked windows representing different states)."
  win-btn:
    width: 20px
    height: 18px
    background: "{colors.bg-light}"
    border: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    description: "Beveled-raised mini button used inside the title bar (_, [], X) and elsewhere. Active state inverts the bevel."
  btn-retro:
    background: "{colors.bg-light}"
    border: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    padding: "6px 24px"
    fontSize: 14px
    description: "Standard Win9x command button. Beveled raised; active state inverts the bevel so the button appears pressed in."
  group-box:
    border: "2px solid #404040 (top/left) + 2px solid {colors.white} (right/bottom)"
    padding: "20px 18px 16px 18px"
    background: "{colors.bg-light}"
    description: "Sunken-bevel framed container with a title label that breaks the top border (the title sits in a small background-painted notch at top-left). The Win9x equivalent of a fieldset/legend."
  group-box-title:
    position: absolute
    top: -10px
    left: 12px
    background: "{colors.bg-light}"
    padding: "0 8px"
    fontSize: 13px
    fontWeight: 700
    description: "The title label that sits on top of a group-box's upper border, painted with the parent background to mask the border behind it."
  panel-raised:
    background: "{colors.bg-light}"
    border: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    padding: 16px
    description: "Raised-bevel panel. Used for tool palettes, button strips, and elevated content regions inside a window body."
  panel-sunken:
    background: "{colors.white}"
    border: "2px solid #404040 (top/left) + 2px solid {colors.white} (right/bottom)"
    padding: 12px
    description: "Sunken-bevel panel with a white interior. Used for text input fields, read-only data displays, and status regions. The white interior is the system's signal for 'this is content, not chrome.'"
  progress-bar:
    width: "100%"
    height: 24px
    background: "{colors.white}"
    border: "2px solid #404040 (top/left) + 2px solid {colors.white} (right/bottom)"
    padding: 2px
    description: "Sunken white well containing a solid navy fill div whose width represents the data value. The fill is `{colors.blue-navy}` solid — no gradient, no animation beyond width transition."
  retro-list:
    listStyle: none
    marker: "> (chevron)"
    markerColor: "{colors.blue-navy}"
    description: "Custom-bullet list where each item is prefixed with a navy '>' character. The chevron is set via ::before, never via list-style."
  retro-check:
    checkBoxSize: "16px"
    checkBoxBorder: "2px solid {colors.black} (top/left) + 2px solid {colors.white} (right/bottom)"
    checkMarker: "x"
    description: "Sunken white square checkbox with a literal lowercase 'x' character as the checked-state marker. Inset-beveled the opposite direction from buttons."
  retro-table:
    borderCollapse: collapse
    fontSize: 14px
    headerBackground: "{colors.bg-gray}"
    headerBorder: "1px solid #404040"
    cellBackground: "{colors.white}"
    cellBorder: "1px solid {colors.bg-gray}"
    zebraRowBackground: "#f0f0f0"
    description: "Pixel-flat data table with gray headers, white cells, light-gray border lines, and a barely-different zebra fill on alternate rows."
  marquee:
    background: "{colors.white}"
    border: "1px inset {colors.bg-gray}"
    padding: "3px 0"
    animation: "marquee 14s linear infinite"
    description: "Scrolling text inside a sunken white well. The animation translates the text from 100% right to -100% left over 14 seconds. The original Win marquee element re-implemented in CSS."
  win-icon:
    width: 18px
    height: 18px
    background: "{colors.white}"
    border: "1px solid {colors.black}"
    fontSize: 11px
    color: "{colors.blue-navy}"
    fontWeight: 700
    description: "Tiny 18px square icon next to a title-bar filename — a navy-on-white letter glyph that imitates an application icon. The glyph is a 1-character mnemonic of the window's role (P for Presentation, R for README, D for Dataview, etc.)."
  tree-item:
    fontSize: 14px
    indent: "24px per level"
    folderGlyph: "📁 (U+1F4C1)"
    fileGlyph: "📄 (U+1F4C4)"
    expandedMarker: "-"
    collapsedMarker: "+"
    description: "Explorer-style hierarchical tree view. Each row carries an expand marker (+/−), a folder or file emoji glyph, and the label text. Indentation steps by 24px per nesting level."
  separator-vertical:
    width: 2px
    background: "#404040"
    borderLeft: "1px solid {colors.white}"
    margin: "0 12px"
    description: "Beveled vertical separator between inline elements — the Win9x equivalent of a vertical rule."
  hr-retro:
    borderTop: "1px solid #404040"
    borderBottom: "1px solid {colors.white}"
    margin: "14px 0"
    description: "Beveled horizontal rule. Two stacked 1px lines (dark on top, white on bottom) create the engraved-in look."
  nav-dot:
    width: 12px
    height: 12px
    background: "{colors.bg-gray}"
    border: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    activeBackground: "{colors.blue-navy}"
    description: "Beveled square mini-dot used as a slide-indicator chip. Active state fills navy with a 4px white center square."
  chart-canvas-host:
    background: "{colors.bg-light}"
    description: "Chart.js canvas embedded inside a panel-raised. Chart colors use {colors.blue-navy}, {colors.blue-bright}, {colors.blue-light}, {colors.green-retro}, {colors.cyan-retro}, {colors.yellow-retro}. Axis labels use MS Sans Serif at 11–12px in {colors.text-dark}. Gridlines in {colors.bg-gray}."
  scrollbar:
    width: 16px
    trackBackground: "{colors.bg-gray}"
    thumbBackground: "{colors.bg-gray}"
    thumbBorder: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    description: "Custom webkit scrollbar styled as a beveled-raised gray thumb on a flat gray track. Width is fixed 16px to match Win9x default."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/retro-windows/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Retro Windows 是一套**Windows 95 / 98 桌面操作系统美学**，被做成幻灯片模板。每页都构造成一个 `win-window`，带斜角矩形外壳、海军蓝渐变标题栏、右上角三个按钮图标（`_`、`[]`、`X`），以及装着应用式内容的正文区。构图是"这页是 1995 年桌面上跑的软件，内容是软件显示的东西"。这个设定是彻底的：没有现代演示意义上的幻灯片标题，只有按文件名样式排的窗口标题（`README.DOC`、`DATAVIEW.CSV`、`METRICS.LOG`）。

字体栈以 **MS Sans Serif**（及其现代回退 Segoe UI / Tahoma / Verdana）作系统字体，承载几乎全部内容，**Press Start 2P**（8 位像素展示字面）与 **VT323**（粗壮 CRT 终端等宽）留给怀旧标点，开场屏标题、导航提示、跑马灯文字。按现代标准正文字面偏小（默认 16px，多数工作文字 14px），这是 OS-UI 美学的一部分：那个年代的软件 UI 跑在固定像素尺寸上，文稿继承了这份约束。

配色是**原版 Win9x 系统色集**：按钮面灰（`{colors.bg-light}` #d4d0c8）、高光白、阴影深灰，以及预留给激活标题栏与主数据填充的海军蓝 / 蓝色渐变（`{colors.blue-navy}` → `{colors.blue-bright}`）。第二簇"复古强调"色相，DOS 绿（#008000）、砖红（#800000）、芥末黄（#808000）、青蓝（#008080），是系统的状态调色板：绿表 OK / 成功 / 在线，红表警告，黄表"中等"风险，青表三级图表数据。图表从这套状态调色板加海军蓝阶梯里取色。没有现代饱和色相。

纵深靠**斜角错觉**达成，每个表面要么凸起（左上高光、右下阴影），要么凹陷（反过来）。系统不用模糊投影，而是用双色非对称边框加内嵌 box-shadow 造出斜角错觉。这是地基性的纵深语法：按钮凸起、文本输入凹陷、分组框凹陷且带一个嵌在缺口上的标题、按钮按下激活态把斜角反过来。

**密度取向：高。** Win9x 应用 UI 很密，每个像素都有用，分组框塞满控件，状态栏带多个读数，对话框排得紧。文稿美学就靠这份密度。一个居中标题加大片空白的页读作坏了或没做完。对的密度是窗口正文里塞满叠放的面板、分组框、表格、图表、按钮条、状态页脚，每页都该像一个应用屏幕，多个区域同时干活。CRT 扫描线叠层强化这一点：纹理只有底下有密集内容时才读得出来。

**关键特征：**
- 每页都是一个 `{components.win-window}`，带斜角外壳、海军蓝渐变标题栏、三个系统按钮（`_`、`[]`、`X`）。
- 固定 3px 周期的 CRT 扫描线叠层（`{components.crt-overlay}`）以 3% 不透明度盖在全部内容之上。
- 基于斜角的纵深：凸起（`{components.panel-raised}`、`{components.btn-retro}`）与凹陷（`{components.panel-sunken}`、`{components.group-box}`），无模糊阴影。
- 字体栈是 MS Sans Serif / Segoe UI / Tahoma 回退，Press Start 2P 与 VT323 作怀旧点缀。
- 状态色（绿 / 红 / 黄 / 青）带语义：绿 = OK，红 = 警告，黄 = 中等，青 = 三级数据。
- 海军蓝 `{colors.blue-navy}` 是主数据色，进度条、图表条、关键标题、激活导航点。
- 列表用海军蓝 `>` 尖括号前缀，复选框用字面量 `x` 字符，树视图用 `📁` / `📄` emoji 字形。
- 窗口标题文字读作带扩展名的全大写文件名（`AGENDA.TXT`、`METRICS.LOG`、`EXPLORER.EXE`）。

## 颜色

### 调色板
- **按钮面浅灰**（`{colors.bg-light}` — #d4d0c8）：窗口、面板、分组框、按钮的基础外壳色。Win9x 的"3D 对象"系统色。略暖的灰。任何非内容区域的默认填充。
- **背景灰**（`{colors.bg-gray}` — #c0c0c0）：略深的灰。用于表头、滚动条轨道、导航点非激活填充。即"灰色背景"系统色。
- **背景深灰**（`{colors.bg-dark}` — #808080）：深灰，用于窗口之外的桌面填充与非激活标题栏起点。即"非激活标题栏"色。
- **白**（`{colors.white}` — #ffffff）：内容填充，用于凹陷面板内、文本输入、表格单元、进度条井，以及标题栏文字色。白标示"这是内容，不是外壳"。
- **黑**（`{colors.black}` — #000000）：斜角边框里最深的阴影色，也是最强的文字色。也用作凸起斜角右 / 下边缘的按钮边框。
- **文字深**（`{colors.text-dark}` — #222222）：默认正文色。比纯黑略柔，好让正文不与斜角暗阴影抢。
- **文字灰**（`{colors.text-gray}` — #555555）：柔化灰，用于次级文字、图注、状态提示。
- **海军蓝**（`{colors.blue-navy}` — #000080）：主品牌色，标题栏起点、图表条、进度填充、标题文字、激活导航点、复古列表尖括号标记。系统的"主"色。
- **亮蓝**（`{colors.blue-bright}` — #0000a0）：标题栏渐变终点。比海军蓝略亮、略蓝。用作图表条第二变体。
- **浅蓝**（`{colors.blue-light}` — #1084d0）：更浅的蓝，用作图表条第三变体。
- **复古绿**（`{colors.green-retro}` — #008000）：DOS 绿。预留给 OK 状态、成功消息、增长百分比、`READY` / `LIVE` 徽章、`On Track` 标签。
- **复古红**（`{colors.red-retro}` — #800000）：砖红。预留给错误 / 警告文字与砖红状态族。
- **复古黄**（`{colors.yellow-retro}` — #808000）：芥末黄。预留给"中等"风险标签与警告图表分段。
- **复古青**（`{colors.cyan-retro}` — #008080）：青蓝。预留给三级图表分段与次级状态点缀。

### 默认值
- **默认表面背景**：窗口之后的桌面区域用 `{colors.bg-dark}`，窗口正文用 `{colors.bg-light}`。
- **默认标题 / 主文字色**：`{colors.blue-navy}`。本系统里标题是海军蓝而非黑，那是仪表盘 / 应用标题声部。
- **默认正文色**：`{colors.text-dark}`（#222222），不是纯黑。
- **默认次级 / 图注文字色**：`{colors.text-gray}`（#555555）。
- **默认图表主色**：`{colors.blue-navy}`。次级条先取 `{colors.blue-bright}` 与 `{colors.blue-light}`，分类型分段图再取 `{colors.green-retro}`、`{colors.cyan-retro}`、`{colors.yellow-retro}`。
- **默认进度条填充色**：`{colors.blue-navy}`（实色，无渐变）。
- **默认状态 OK 色**：`{colors.green-retro}`，用于 `READY`、`LIVE`、`Approved`、增长百分比，以及任何"一切良好"徽章。
- **默认状态警告色**：`{colors.red-retro}` 或 `{colors.yellow-retro}`，红给硬错误，黄给中等隐忧。
- **默认标题栏背景**：激活窗口用海军蓝 → 亮蓝水平渐变；页里叠放多个窗口时，非激活窗口用灰（`{colors.bg-dark}` → `#a0a0a0`）。
- **海军蓝标题栏内默认文字色**：`{colors.white}`，标题栏里始终白压海军蓝。
- **凹陷白面板内默认文字色**：`{colors.text-dark}`，内容文字深压白。

强调调色板（绿 / 红 / 黄 / 青）有固定语义，别把绿拿去随意装饰，别把红用在非警告文字上。强调是状态信号，不是颜料。

## 排印

### 字族
系统有三款字面，各有分明角色：

- **MS Sans Serif / Segoe UI / Tahoma / Geneva / Verdana 栈**（系统正文）：几乎全部文字的默认。回退链在任何 OS 上都成立，macOS 落到 Geneva 或 Verdana，Windows 落到 Segoe UI 或 MS Sans Serif，Linux 落到某个无衬线回退。美学是"1995 年软件 UI 长什么样"，系统字体栈对这点是关键，绝不要换成定制展示无衬线。
- **Press Start 2P**（像素展示）：8 位像素展示字面，省着用。预留给开场屏标题、收尾页的送别语，以及任何超大怀旧标题瞬间。始终以 `{colors.blue-navy}` 渲染、始终居中。整套文稿用一两次，不是每页都用。
- **VT323**（CRT 终端等宽）：粗壮等宽字面，模仿 CRT 终端。预留给底边导航提示（`<-- ARROW KEYS to navigate -->`）与任何"终端输出"正文区。可选，没有它文稿照样成立。

斜体不用。下划线不用（交互链接可带下划线，但没有装饰性下划线）。强调靠字重（400 → 700）与换色（默认 → 海军蓝，或默认 → 绿 / 红）达成。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.text-xl}` | 32px | MS Sans Serif | 700 | 窗口正文里的主幻灯片标题 |
| `{typography.metric-xl}` | 30px | MS Sans Serif | 700 | KPI 块里的英雄指标值 |
| `{typography.text-lg}` | 22px | MS Sans Serif | 700 | 窗口正文里的分节标题 / 副标题 |
| `{typography.text-md}` | 18px | MS Sans Serif | 400 | 标准正文段落 |
| `{typography.body}` | 16px | MS Sans Serif | 400 | 默认工作正文 |
| `{typography.text-sm}` | 14px | MS Sans Serif | 400 | 图注、列表项、按钮标签、表格单元 |
| `{typography.text-xs}` | 12px | MS Sans Serif | 400 | 细则、状态提示、页码 |
| `{typography.title-bar}` | 14px | MS Sans Serif | 700 | 窗口标题栏文件名，始终全大写 |
| `{typography.group-box-title}` | 13px | MS Sans Serif | 700 | 缺口嵌装的分组框标题标签 |
| `{typography.pixel-display}` | 20–24px | Press Start 2P | 400 | 怀旧开场屏或收尾展示标题 |
| `{typography.terminal}` | 22px | VT323 | 400 | 终端式正文或跑马灯文字 |
| `{typography.nav-hint}` | 16px | VT323 | 400 | 底边键盘提示文字 |

### 默认值
- **窗口正文内主幻灯片标题默认尺寸**：`{colors.blue-navy}` 字重 700 的 `{typography.text-lg}`（22px），应用标题声部。超大英雄标题用 `{typography.text-xl}`（32px）。
- **正文段落默认尺寸**：散文段用 `{typography.text-md}`（18px），工作文字与列表行用 `{typography.text-sm}`（14px）。
- **窗口标题栏文件名默认尺寸**：`{typography.title-bar}`（14px 字重 700），始终全大写、始终 `{colors.white}`。
- **指标或英雄数字默认尺寸**：`{colors.blue-navy}` 的 `{typography.metric-xl}`（30px 字重 700）。
- **窗口内分节标题默认尺寸**：`{colors.blue-navy}` 的 `{typography.text-lg}`（22px 字重 700）。
- **任何图注、细则、状态提示默认尺寸**：`{colors.text-gray}` 的 `{typography.text-xs}`（12px）。
- **任何该引人注意的标题或标签默认字重**：700。
- **正文默认字重**：400。

一页叠放多个窗口或面板时，页面主信息放在第一个窗口正文里，用 `{typography.text-lg}` 字重 700 海军蓝。除非是明确的英雄 / 开场瞬间，否则别取更大尺寸。

### 招牌处理
以下处理**只要用到对应元素类型就不可省略**：

- **每个窗口标题栏文字都全大写、按文件名样式排**（带扩展名）：`PRESENTATION.EXE`、`README.DOC`、`METRICS.LOG`、`AGENDA.TXT`、`DATAVIEW.CSV`、`FEATURES.INI`、`EXPLORER.EXE`、`TIMELINE.PRJ`。文件名惯例是美学的一部分，绝不用现代标题式窗口名。
- **每个标题栏都带右上角三按钮簇**（`_` 最小化、`[]` 最大化、`X` 关闭）。按钮是装饰、不可交互，但必须始终存在。
- **每个标题栏左侧都带一个 `{components.win-icon}` 锁定**：18px 白底黑边方块，内含一个海军蓝单字母，以助记方式标识窗口（P、A、R、D、F、G、M、E、T）。
- **每个窗口都用凸起斜角外壳处理**（白上 / 左 + 黑下 / 右边框 + 双重内嵌阴影）。去掉斜角会彻底破掉 Windows 美学。
- **窗口内每个正文标题都是 `{colors.blue-navy}` 字重 700。** 海军蓝是应用标题声部，黑标题读作"年代不对"。
- **状态文字用指定的状态色配字重 700**：绿给 OK / 成功 / 增长，红给错误，黄给中等。默认字重的绿色状态词读作顺带的，不像标签。
- **分组框标题坐在上边框之上一个 0–8px 内边距的缺口里。** 标题背景涂成 `{colors.bg-light}`（父级填充）来遮住身后的边框，绝不让边框穿过标题。

### 排印原则
美学依赖**固定像素尺寸**，而非流式文字。系统为 Win9x 96-DPI 渲染环境设计，文稿靠用整数像素字号（12、13、14、16、18、22、30、32）保住那份感觉。正文别用 `rem`/`em`/`clamp`，OS-UI 错觉在亚像素渲染尺寸下会破。

像素字体（Press Start 2P）与终端字体（VT323）是怀旧点缀，不是主力。Press Start 2P 排正文很快就读不了，VT323 做标题读作用力过猛。每款在整套文稿里各留一两个瞬间。

## 布局

### 画布系统
系统以 `100vw × 100vh` 为目标，每页定位 `position: fixed; top: 0; left: 0`。只有 `.active` 页 `display: flex`，其余 `display: none`。每页内部由单个 `{components.win-window}`（或几个叠放窗口）提供画框外壳。窗口 `max-width: 1200px`、`max-height: calc(100vh - 68px)`，好让桌面灰边始终露在外壳四周。

页面外内边距 `24px 32px 44px 32px`，多出来的底部内边距给常驻导航外壳（视口底边的导航点与页码）让位。

### 窗口解剖
每个窗口有三个纵向叠放的区域：
1. **标题栏**（`{components.win-titlebar}`）：固定 4px-8px 内边距、海军蓝渐变，内含左侧图标锁定 + 文件名与右侧三按钮簇。
2. **正文**（`{components.win-body}`）：20px 24px 24px 24px 内边距，填满剩余高度，装页面内容构图。
3. **正文底部可选状态面板**：一条 `{components.panel-raised}` 或 `{components.panel-sunken}`，承载元信息（数据来源、最后更新、计数、状态徽章）。

一页可并排放多个窗口（典型用于时间轴季度或多屏比较）。出现多个窗口时，只有一个带激活海军蓝标题栏，其余带非激活灰渐变。

### 内边距比例
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.slide-pad}` | 24px 32px 44px 32px | 页面外内边距 |
| `{spacing.win-body-pad}` | 20px 24px 24px 24px | 窗口正文内部 |
| `{spacing.group-box-pad}` | 20px 18px 16px 18px | 分组框内部（多留顶部给缺口标题） |
| `{spacing.panel-pad}` | 16px | 凸起面板内部 |
| `{spacing.panel-sunken-pad}` | 12px | 凹陷白面板内部 |

### 常驻外壳
三个常驻元素活在页面构图之外：
- **导航点**：底部居中，斜角方形指示器，每页一个，激活的那个填海军蓝并带一个 4px 白色中心方块。
- **页码**：右下，凹陷斜角小片，12px 的 `N / TOTAL` 文字。
- **导航提示**：左下，VT323 16px 文字 `<-- ARROW KEYS to navigate -->`。

CRT 扫描线叠层以 z-index 9999 盖在一切之上，每页、每个外壳元素、每块图表画布都在它下面渲染。

## 纵深与层级

### 斜角错觉（主手法）
系统用**双色非对称边框**加**内嵌 box-shadow** 模拟 Windows 95 斜角 UI。有两种状态：

- **凸起**：上 + 左 2px 实白，右 + 下 2px 实黑，再加 `inset 1px 1px 0 white, inset -1px -1px 0 #404040`。读作按钮或面板从表面立起。用于窗口、凸起面板、按钮、导航点。
- **凹陷**：上 + 左 2px 实 `#404040`，右 + 下 2px 实白。读作凹陷的输入框或内容井。用于分组框、凹陷面板、文本输入、进度条轨道、复选框方框、滚动条轨道。

按钮按下激活态把斜角反过来，"按进去"的按钮交换高光 / 阴影边框方向。没有悬停态，OS 美学早于普及的悬停提示。

### 无现代阴影
系统用**零模糊 `box-shadow` 值**、零 `drop-shadow` 滤镜、零 rgba 着色阴影。每个纵深线索都来自斜角边框手法。给窗口或按钮加一道柔现代阴影会立刻破掉年代感。

### 色块纵深
斜角之外，**白对灰的反差**提供区域纵深：白面板在视觉上凸为"内容 / 数据"，灰面板退为"外壳 / 结构"。一页的层级自然从白井落在哪里浮现。

### CRT 扫描线叠层
系统带一层氛围：CRT 扫描线叠层。3px 周期的水平重复渐变、3% 黑不透明度盖在每页上。叠层不添纵深，但添**纹理**，文稿里每个表面都读作"渲在 1995 年 CRT 显示器上"，而非"渲在平屏上"。去掉叠层是允许的，但会丢掉美学里实在的一块。

## 形状与处理

### 圆角
系统**任何地方都没有圆角**。每个盒子、按钮、面板、窗口、表格单元、复选框、导航点、进度条，都是严格矩形。border-radius 全系统为 `0`。

### 边框粗细与样式
- **2px 实线**：窗口、面板、按钮、导航点上的通用斜角边框粗细。以双色非对称式样（白 + 黑或深灰 + 白）使用，造出斜角错觉。
- **1px 实线**：用于较细的元素边框（表格单元边框、win-icon 轮廓、hr-retro 叠线）。
- **`1px inset`**：用于跑马灯容器边框。

边框绝不上色（无海军蓝边框、无绿边框），斜角双色式样（白 + 黑 / 深灰）是唯一的边框词汇。

### 装饰元素类型

**窗口（`{components.win-window}`）**：画框基元。凸起斜角矩形，带一个内含图标 + 文件名 + 三系统按钮的海军蓝标题栏，以及装内容的正文区。每页至少有一个窗口。

**分组框（`{components.group-box}`）**：凹陷斜角容器，左上角带一个缺口嵌装的标题。标题坐在一块 0–8px 内边距、涂了背景的区域里，遮住身后的边框，模仿原生 HTML 表单的 `<fieldset><legend>` 式样。用于把窗口内相关的控件或内容块聚成簇。

**凸起面板（`{components.panel-raised}`）**：凸起斜角灰面板。用于工具面板、按钮条、状态页脚、抬升的内容区域。

**凹陷面板（`{components.panel-sunken}`）**：凹陷斜角白面板。用于文本输入、KPI 显示、状态读数、只读数据。白内部就是线索。

**复古按钮（`{components.btn-retro}`）**：凸起斜角灰按钮，6px × 24px 内边距。始终带 text-md（14px）MS Sans Serif 字重 400。激活态把斜角反过来。

**进度条（`{components.progress-bar}`）**：凹陷白井，内含一块实海军蓝填充 div。填充宽度代表数值，除宽度过渡外无动画。始终 24px 高（嵌在特性卡里时 16px）。

**复古表格（`{components.retro-table}`）**：像素扁平数据表，灰表头、白单元格、浅灰边线、交替行几乎看不出的斑马填充。单元格内边距 6px × 10px。

**复古列表（`{components.retro-list}`）**：无样式列表，每行带一个海军蓝 `>` 尖括号前缀。尖括号经 `::before` 设定，绝不用 list-style。

**复古复选（`{components.retro-check}`）**：16px 凹陷斜角白方块，勾选时装一个字面量小写 `x` 字符。斜角相对按钮是反的（上 / 左黑、下 / 右白）。

**树视图（`{components.tree-item}`）**：资源管理器式层级列表。每行带一个展开标记（+/−）、一个文件夹（`📁`）或文件（`📄`）emoji 字形，以及标签。每嵌套一层缩进 24px。

**KPI 块（分组框变体）**：方形分组框，带一个标题标签（`Revenue`、`Customers`、`Retention`、`NPS Score`）、一个 30px 海军蓝大指标、一行绿色增量（`▲ +18.3%`）、一行 12px 灰色语境文字（`vs previous quarter`）。在仪表盘里四块一排使用。

**跑马灯（`{components.marquee}`）**：凹陷白井，内含横向滚动文字。动画 14s linear infinite，未实现悬停暂停。用于开场与收尾页。

**Win 图标（`{components.win-icon}`）**：18px 方形，白底黑边微型标，内含一个海军蓝单字母字形。在标题栏里作锁定标记。

**分隔线（竖向或 hr-retro）**：斜角线。竖向：2px 深灰 + 1px 左白边，12px 横向外边距。横向：叠放的 1px 上深灰 + 1px 下白线，14px 纵向外边距。

**沙漏 / 睡眠字形（`⌛` 或 `💤`）**：作为单个超大字符（40–52px）用在开场 / 收尾页，作怀旧 OS 感线索。

## 该做与不该做

### 该做
- 每页都包进一个 `{components.win-window}`，带海军蓝标题栏、文件名式标题（如 `METRICS.LOG`）与三按钮簇（`_`、`[]`、`X`）。
- 每个面板、按钮、窗口都用斜角边框手法（凸起用白上 / 左 + 黑下 / 右 + 内嵌阴影，凹陷反过来）。这是系统的身份。
- 主标题设 `{colors.blue-navy}` 字重 700。海军蓝是应用标题声部，黑标题读作年代不对。
- 把每页填密。多个分组框、叠放面板、KPI 条、图表、状态页脚都该在一个窗口正文里共存。空白读作坏了。
- 状态色按语义用：绿给 OK / 在线 / 增长，红给警告 / 错误，黄给中等隐忧，青给三级数据。每个色都带含义，别拿它们重新装修。
- 图表先用海军蓝阶梯（`{colors.blue-navy}`、`{colors.blue-bright}`、`{colors.blue-light}`）渲染，再从状态调色板取色做分类型分段区分。
- 项目列表用 `>` 尖括号复古列表式样，复选框用字面量 `x` 复古复选。浏览器原生项目符号与表单控件会破掉美学。
- 用整数像素字号（12、13、14、16、18、22、30、32）。固定像素定尺寸是 OS-UI 错觉的一部分。
- 每页保留 CRT 扫描线叠层（`{components.crt-overlay}`）。它是把文稿系在 CRT 显示器隐喻上的纹理。
- 窗口标题排成带扩展名的全大写文件名（`PRESENTATION.EXE`、`AGENDA.TXT`）。标题式窗口名会破掉设定。

### 不该做
- 不要给任何角加圆角。每个形状都是严格矩形。除图表画布内极小的圆细节外，border-radius 全系统为 0。
- 不要用模糊 `box-shadow` 或 `drop-shadow`。纵深全基于斜角。
- 不要引入现代品牌色（饱和紫、橙、洋红）。调色板限于 Win9x 系统灰、海军蓝与四种复古强调。
- 不要给边框上色。边框双色是白 + 黑或深灰 + 白，绝不用海军蓝边框、绝不用绿边框。
- 不要用 `rem`/`em`/`clamp` 定正文尺寸。固定整数像素尺寸保住 OS-UI 错觉。
- 不要用 Press Start 2P 或 VT323 排正文。它们是怀旧点缀，整套文稿里各留一两个瞬间。
- 不要用现代标题式或句式窗口标题。窗口标题是带扩展名的全大写文件名。
- 不要让窗口缺了三按钮簇（`_`、`[]`、`X`）。哪怕是装饰，这簇也是每个窗口署名的一部分。
- 不要给按钮引入悬停态视觉变化。Win9x 年代早于普及的悬停，激活态斜角反转是唯一的状态变化。
- 不要排出一个居中标题加大片空白的稀疏页。系统不像密集应用 UI 时就读作坏了。

## 响应式行为

系统是**视口流式**但**像素固定**：窗口外壳与正文尺寸随视口伸缩（`max-width: 1200px`、`max-height: calc(100vh - 68px)`），但字号是整数像素、不做 clamp。单条 `max-width: 900px` 媒体查询把页面内边距降到 15px-20px、把 4 列网格收成 2 列。

### 缩放行为
- 窗口长大到填满视口，最多 1200×(100vh-68px)，之后停止缩放。
- 所有字号保持固定：14px 标签在任何屏幕尺寸下都是 14px。
- CRT 扫描线叠层的 3px 周期不随视口变化。

### 放映行为
- `ArrowRight`、`ArrowDown`、`Space` 前进。
- `ArrowLeft`、`ArrowUp` 后退。
- `Home` 跳到首页，`End` 跳到末页。
- 底部导航点可点击。
- 默认未实现触屏滑动支持。

### 打印行为
没有定义 `@media print` 规则。打印只会渲染当前激活页。

### 图表渲染
图表用从 CDN 加载的 Chart.js。图表色直接映射到系统 token（`{colors.blue-navy}`、`{colors.blue-bright}`、`{colors.blue-light}`、`{colors.green-retro}`、`{colors.cyan-retro}`、`{colors.yellow-retro}`）。坐标轴标签用 11–12px `{colors.text-dark}` 的 MS Sans Serif。网格线是 1px `{colors.bg-gray}`。图表在其所在页变为激活时懒渲染。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁 | 中文 | 字重映射 |
|---|---|---|---|
| 标题栏 / 标题 / 指标 / 分节标题 | MS Sans Serif → Segoe UI（700） | **思源黑体 Noto Sans SC** | 700 |
| 正文 / 图注 / 列表 / 表格单元 | MS Sans Serif → Segoe UI（400） | **思源黑体 Noto Sans SC** | 400 |
| 像素展示（Press Start 2P），仅拉丁 | Press Start 2P | *（无 CJK 替代）* | 不适用 |
| 终端 / 导航提示（VT323），仅拉丁 | VT323 | *（无 CJK 替代）* | 不适用 |

### 混排策略

**策略 A：所有拉丁系统角色用单一 CJK 字族。** Retro Windows 是系统字体文稿（MS Sans Serif / Segoe UI / Tahoma）。给每个拉丁角色配单一 CJK 字族 Noto Sans SC，保住"这是软件 UI"的语域：Win9x 应用的简体中文本地化会用单一系统 CJK 字面（MS YaHei / SimSun）渲染，而不是展示 + 正文多字族搭配。两款怀旧点缀字体（Press Start 2P、VT323）按设计仅拉丁，绝不要尝试像素字体的 CJK 替代，没有能维持年代感的可接受对应。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

然后把 `'Noto Sans SC'` 追加到正文字体栈：
```css
font-family: 'MS Sans Serif', 'Segoe UI', Tahoma, Geneva, Verdana, 'Noto Sans SC', sans-serif;
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

- **窗口标题栏成了一道翻译难题。** `FILENAME.EXT` 惯例仅适用于拉丁，`METRICS.LOG` 没有地道的中文对应。可选做法：（1）保留拉丁文件名（`METRICS.LOG`、`AGENDA.TXT`）求系统 UI 怀旧，让页面正文承载中文内容；（2）用中文描述词 + 拉丁扩展名（`季度指标.LOG`、`议程.TXT`），读作本地化应用。做法（1）对 Win9x 年代更本真，做法（2）对中文读者更易读。
- **标题栏含 CJK 字符时，`title-bar` 排印的 0.5px 字距必须降到 0**。
- **状态徽章（READY、LIVE、OK、WARNING）** 干净地译成短中文词（就绪、在线、通过、警告），字重 700、用指定状态色，绿 / 红 / 黄 / 青的语义信号能带过来。
- **分组框缺口标题在中文里同样成立**，`客户数据`、`销售指标`。缺口遮罩依赖背景涂绘，不依赖字形度量。
- **CRT 扫描线叠层与字形无关**，给中文文字添的怀旧纹理与给拉丁的一样。
- **图表坐标轴标签与小片文字** 应降到 11–12px 的 Noto Sans SC 400，固定像素定尺寸的惯例对 CJK 同样适用。

### 已知 CJK 缺口

两款怀旧点缀字体（Press Start 2P、VT323）根本上仅适用于拉丁，它们作为 8 位像素与 CRT 终端的年代回指，存在于 CJK 渲染还需专用点阵字体、而现代网页没有对应物的年代。文稿若需要中文像素展示瞬间，唯一诚实的做法是用大尺寸 Noto Sans SC 并放弃像素字体性格；不要换另一款"像素风"中文字体（那会读作年代不对且坏掉）。把 Press Start 2P / VT323 留给纯拉丁瞬间（带 `LOADING...` 的开场屏、写 `ARROW KEYS to navigate` 的页脚），让 CJK 页通体用 Noto Sans SC。

## 迭代指南

1. 任何新页都包进一个 `{components.win-window}`，带海军蓝标题栏，内含一个 `{components.win-icon}`（单字母字形）、一个带扩展名的全大写文件名式标题（`.EXE`、`.DOC`、`.LOG`、`.TXT`、`.CSV`、`.INI`、`.PRJ`、`.BMP` 之类）与三按钮簇（`_`、`[]`、`X`）。
2. 窗口内任何新内容区域都用 `{components.group-box}`（凹陷带缺口标题）聚相关项、用 `{components.panel-raised}` 做工具条与仪表盘、或用 `{components.panel-sunken}` 做白井内容展示。
3. 任何新主标题都用 `{colors.blue-navy}` 字重 700 的 `{typography.text-lg}`（22px）。英雄 / 开场标题用 `{typography.text-xl}`（32px）或 Press Start 2P（20–24px）。
4. 任何新指标块都用 `{components.group-box}` + `{typography.metric-xl}` 海军蓝 700 + 绿色增量 + 12px 灰色语境的式样。
5. 任何新图表都用 Chart.js，主数据取海军蓝阶梯、分类型分段取复古状态色。画布始终包在 `{components.panel-raised}` 里。
6. 任何新项目列表都用 `{components.retro-list}` 尖括号式样，任何复选框用 `{components.retro-check}` 式样，任何层级树用 `{components.tree-item}` 文件夹 / 文件 emoji 式样。
7. 任何新按钮都是 `{components.btn-retro}`，斜角灰、6px × 24px 内边距、14px MS Sans Serif。按钮成簇出现（OK / Cancel / Help，或 Export / Print）。
8. 任何新状态徽章都用 OK 的 `{colors.green-retro}` 字重 700、错误的 `{colors.red-retro}`、中等的 `{colors.yellow-retro}`。始终字重 700，绝不装饰。
9. 状态页脚（窗口正文底部的凸起面板条）承载三四个数据点，以 `•` 圆点分隔，数据来源、最后更新、计数、密级。
10. 每页都必须视觉密集，多块面板叠放、底部一条状态页脚、空间允许处放按钮条或导航簇装饰。稀疏会破掉美学。

## 已知缺口

- 系统从 CDN 加载两款 Google Fonts（Press Start 2P、VT323）。它们是可选的怀旧点缀，正文字体栈（MS Sans Serif、Segoe UI、Tahoma、Geneva、Verdana、sans-serif）无任何外部依赖即可正确渲染，即便两款 Google 字体都加载失败，文稿美学仍连贯。
- 从 CDN 加载的 Chart.js（4.4.7）提供图表引擎。Chart.js 加载失败时图表不渲染，页仍会渲染，但画布区为空。
- CRT 扫描线叠层是风格选择，与放映投影输出并不相称，在真实投影幕上叠层可能读成图像噪声而非怀旧纹理。投影时可考虑关掉叠层。
- Win9x 斜角错觉依赖在合适缩放级别下渲染，斜角 1–2px 宽，在极端缩放级别或没有浏览器亚像素渲染的超高 DPI 屏上，可能显成实边框或彻底消失。
- 悬停态按设计缺席（美学早于普及的悬停）。期待悬停提示的现代观众，鼠标交互时可能觉得文稿没反应。
- 复古列表 `>` 尖括号、复古复选 `x`、树视图 emoji 字形是基于字符的、非矢量，它们会按运行时为 `>`、`x`、`📁`、`📄` 提供的默认字体度量渲染。
- 跑马灯动画持续运行、无法暂停。某些无障碍审计会把它标为违反 `prefers-reduced-motion`。
- `lib-cabinets` 以 `bgImage` 派生的行内 SVG 噪声 / 斜线图案设在 CSS 里，这些是内联 data URI，渲染观感会随浏览器略有差别。
