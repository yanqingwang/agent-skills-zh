---
name: morph-ppt
description: "当用户想要一份带跨页平滑动画的 .pptx 时使用本 Skill —— PowerPoint Morph 切换、Keynote 式连续运动、形状随翻页生长 / 移动 / 旋转。触发词：'morph'、'morph transition'、'smooth transition'、'continuous animation across slides'、'Keynote-style transition'、'animated slide sequence'、'shape continuity across slides'。输出为单个 .pptx。本 Skill 是 officecli-pptx 之上的场景层 —— 继承全部 pptx v2 规则（视觉交付底线、网格、配色、连接线规范、Delivery Gate 1–5a）。没有跨页运动的普通幻灯片、路演稿（pitch deck）或董事会评审材料，不要调用本 Skill —— 应路由到 officecli-pptx 基础版或 officecli-pitch-deck。"
---

> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# OfficeCLI Morph-PPT Skill

**本 Skill 是 `officecli-pptx` 之上的场景层（scene layer）。** 每一条 pptx 硬规则 —— 视觉交付底线（标题 ≥ 36pt / 正文 ≥ 18pt / 标题 ≥ 2× 正文）、33.87×19.05cm 上的 12 列网格、规范配色、图表选型决策表、连接线规范（connector canon）、shell 转义、常驻模式 + 批处理、Delivery Gate 1–5a —— 均为继承而来，本文不再重复教授。本文件只补充 **Morph** 在其之上所需的内容：跨页形状名称绑定、Scene Actors 与内容前缀、幽灵（ghost）纪律、`transition=morph` 的 CLI 怪癖、52 式视觉库查找，以及 morph 专属的全新视角 Gate 5b 扩展。

凡是 pptx 基础规则已覆盖的内容，本文一律写作 `→ see pptx v2 §X`。如果还没有读过，请先阅读 `skills/officecli-pptx/SKILL.md`。

## 安装（Setup）

如果缺少 `officecli`：

- **macOS / Linux**：`curl -fsSL https://d.officecli.ai/install.sh | bash`
- **Windows (PowerShell)**：`irm https://d.officecli.ai/install.ps1 | iex`

用 `officecli --version` 验证（若 PATH 尚未生效，请打开新终端）。如果安装失败，从 https://github.com/iOfficeAI/OfficeCLI/releases 下载二进制文件。

## ⚠️ 先查帮助规则（Help-First Rule）

**本 Skill 教的是 Morph 工作流 —— 形状名称何时必须一致、何时做幽灵化、CLI 何时自动加前缀 —— 而不是每一条命令旗标。** 当属性名、枚举值或预设不确定时，先查帮助，再去猜测。

```bash
officecli help pptx slide           # authoritative for: transition, advanceTime, advanceClick, background
officecli help pptx transition      # transition / transitionDuration / transitionSpeed (Parent: slide)
officecli help pptx shape           # name, preset, x/y/width/height, fill, rotation, opacity, animation
officecli help pptx animation       # preset + trigger + duration values
officecli help pptx <element> --json  # machine-readable schema
```

帮助信息反映的是已安装的 CLI 版本。当 Skill 与帮助信息不一致时，**以帮助为准。** 本文件中的每一个 `--prop X=` 都已对照 `officecli help pptx <element>` 做过 grep 验证。已确认的要点：`transition=morph` 是 `slide` 上列出的合法值；`advanceTime` / `advanceClick` 有效。`transition` 是一个真实存在的元素（`officecli help pptx transition`，Parent: slide，支持 set/get）—— 它暴露 `transition`、`transitionDuration` 和 `transitionSpeed`。用高层路径设置切换：`set <slide> --prop transition=morph`；用组合简写微调速度/时长：`transition=morph-slow`（或 `-fast`，或 `transition=morph-<DUR_MS>`）。速度/时长只能通过 `transition` 属性上的这一简写设置，不能作为独立子属性。两者在回读时均可往返还原：`transition=morph-slow`/`-fast` 回读为 `transitionSpeed=slow`/`fast`，`transition=morph-<DUR_MS>`（例如 `morph-1500`）回读为 `transitionDuration=1500`。

## 心智模型与继承

**继承 pptx v2。** 你应当已经先读过 `skills/officecli-pptx/SKILL.md`。本 Skill 假设你已经会：添加幻灯片 + 形状 + 图表 + 连接线；用 `@name=` / `@id=` 寻址；给路径加引号；使用 `batch` heredoc；在流程连接线上使用 `tailEnd=triangle`；执行 Delivery Gate 1–5a；归因区分 `[AGENT-ERROR]` vs `[RENDERER-BUG]` vs `[SKILL gap]`。如果其中任何一项不熟悉，请先读 pptx v2。

**继承自 pptx v2（本文不再重复教授）：**

- 视觉交付底线 —— 标题 ≥ 36pt / 正文 ≥ 18pt / 标题 ≥ 2× 正文、封面信息饱满度、对比度底线、禁止 `\$\t\n` 字面量、每页 ≤ 1 个动画 / ≤ 600ms。
- 网格数学 —— 33.87 × 19.05cm，边缘留白 ≥ 1.27cm，块间距 ≥ 0.76cm，留白（负空间）≥ 20%。N 卡片网格：`col = (33.87 − 2·margin − (N−1)·gap) / N`。
- 四套规范配色（Executive navy / Forest & moss / Warm terracotta / Charcoal minimal）—— morph 文稿可以从 `reference/styles/` 另选基调，但对比度规则仍然适用。
- 图表选型表 —— 柱形 vs 条形 vs 折线 vs 饼图 vs 散点 vs 大字号 KPI；`> 3 series + > 8 categories` = 拆分。
- 连接线规范 —— `shape=straight|elbow|curve`，from/to 用 `@id=`（C-P-6），每条流程线都用 `tailEnd=triangle`。
- Shell 转义三层 —— `$` 用单引号，批处理用 heredoc，真实换行用 `<a:br/>`。
- 常驻模式 + batch ≤ 12 个操作，`<<'EOF'` 单引号定界符。
- Delivery Gate 1-5a（schema、token grep、超链接 rPr、幻灯片顺序、深底深字）—— 每一道门都打印 OK 之后才能宣布完成。
- 已知问题 C-P-1..7（超链接 rPr、图表 spPr 警告、动画时长回读、动画移除、连接线枚举、连接线 `@name=`、图表颜色渲染器归一化）。
- 归因分诊 —— `[AGENT-ERROR]` vs `[RENDERER-BUG]` vs `[SKILL gap]`。

**Morph 的身份 —— 本 Skill 自有的内容（叠加在 pptx v2 之上的增量）：**

- **跨页形状名称绑定。** PowerPoint 的 Morph 引擎在相邻幻灯片之间按**完全相同的 `name=`** 配对形状，并对其位置 / 尺寸 / 旋转 / 填充 / 不透明度做插值。名称对不上 ⇒ 没有动画，只会静默淡出。这是一条工作流纪律，不是 CLI 功能。
- **命名空间前缀：** `!!scene-*`（持久装饰，永不幽灵化）/ `!!actor-*`（演化后退场的内容）/ `#sN-*`（每页内容，在第 N+1 页幽灵化）。在执行 `add` 之前就规划好所有名称。
- **幽灵位置 `x=36cm`**（33.87cm 画布右边缘之外）。绝不删除带 `!!` 前缀的形状 —— 把它移出画布，这样 morph 的退场动画仍能播放。
- **`transition=morph` 自动加前缀的怪癖。** CLI 会给 morph 页上的每个形状自动前置 `!!`（`#s1-title` 被存为 `!!#s1-title`）。`@name=` 路径选择器**仍然可解析** —— `get .../shape[@name=#s1-title]` 能返回该形状（匹配对后缀/前缀容忍）。回读到的名称是带前缀的形式。见 §Known Issues。
- **相邻页空间差异。** 相邻成对的形状之间位移 ≥ 5cm 或旋转 ≥ 15° —— 否则 morph 插值不出任何可见效果。
- **渲染器现实。** Morph 在 PowerPoint 365 / Keynote / WPS 中渲染。LibreOffice 和许多网页查看器只会渲染成普通淡出（运行时特性）。这不是 Skill 缺陷 —— 属于 `[RENDERER-BUG]`。

### 反向交接 —— 何时退回 pptx 基础版（或兄弟 Skill）

任何没有跨页运动的演示文稿（董事会评审、销售演示、全员大会、培训）都留在 **pptx v2 基础版**。没有 morph 的融资叙事弧线留在 **officecli-pitch-deck**。只有当用户明确要求 "morph" / "smooth transitions" / "continuous animation" 且 ≥ 2 个连续页面共享一个会发生变换的视觉元素时才使用本 Skill。"Animated deck" 若只指一次性的入场动画 → 走 pptx v2 §Animations，不是 morph。

## Shell 与执行纪律

**Shell 引号、增量执行、`$FILE` 约定** → see pptx v2 §Shell & Execution Discipline。规则逐字相同。

**Morph 专属补充：**

- **shell 值中的 `!!` —— 用单引号。** Bash / zsh 的历史扩展会吞掉未加引号的 `!!foo`。始终使用 `--prop 'name=!!scene-ring'`（单引号）。在 Python 的 `subprocess.run([...])` 列表中无需加引号 —— 把 `"name=!!scene-ring"` 作为普通字符串传入即可。
- **属性文本中的 `$` —— 用单引号（价格 token）。** `--prop text='$9/mo'` 和 `--prop text='$199/yr'` —— 绝不写 `--prop text="$9/mo"`（zsh/bash 会把 `$9` 当空变量吞掉 → 文本被渲染成 `.` 或一个孤立的句点）。双引号属性中的 `${VAR}`、`$USER`、`\n`、`\r`、`\t` 同理。下文 Gate 2 morph 附录会 grep 这个泄漏特征。
- **shell 值中的 `#` —— 安全，但仍建议加引号。** `#` 只有在 shell 词首才是注释符。`--prop name=#s1-title` 能工作，但 `--prop 'name=#s1-title'` 才是让你不必猜的习惯。
- **多形状页面最干净的路径是 batch heredoc。** `<<'EOF' | officecli batch $FILE` 关闭所有 shell 展开 —— 对 JSON 体内的 `$`、`!!`、`#`、`'` 都安全。
- **`--json` 响应把负载包在 `.data.results[]` 里。** `query` 和 `get` 都返回 `.data.results[]` 数组。单个节点的 `format` 位于 `.data.results[0].format.X`；该节点的子节点位于 `.data.results[0].children[]`（每个子节点的 format 在 `.data.results[0].children[].format.X`）。始终经由 `.data.results[0]` —— 裸的 `.data.children[]` 或 `.data.format` 会静默返回 null。
- **变量：** 每个构建脚本开头写 `FILE="deck.pptx"`；下文所有示例都使用 `$FILE`。
- **Gate 的 shell 模式 —— 先 COUNT，再 if/else。** 永远不要写 `grep … && echo LEAK || echo OK` —— 当 grep 退出码为 1（0 次匹配）时，`||` 分支会在 stdout 为空的情况下触发，令人困惑地打印 "OK"（或从之前的管道打印出 "LEAK"）。规范形式：`COUNT=$(cmd | wc -l); if [ "$COUNT" -gt 0 ]; then echo "LEAK: …"; else echo "OK"; fi`。

## 本 Skill 自有的两个原语

- **Scene Actors（场景 Actor）** = 持久的 `!!` 命名形状（装饰或内容），**在相邻页面间按完全相同的名称配对**，让 Morph 能对它们做插值。每个 `!!scene-*` / `!!actor-*` 形状都是场景 Actor。
- **Choreography（编排）** = Actor 如何演化的计划 —— 谁移动到哪里、谁入场、谁退场、发生在哪一对页面上。写代码之前先写进 §Morph Pair Planning 表。

当用户要求 morph 运动且 ≥ 2 个连续页面共享一个会发生变换的视觉元素时，使用本 Skill。目标查看器提醒：morph 需要 PowerPoint 365 / Keynote / WPS —— 如果用户只装了 LibreOffice，先警告（见 §Renderer honesty）。

**演讲者备注规则。** 每一页内容页（非封面、非结尾）都必须通过 `officecli add "$FILE" /slide[N] --type notes --prop text='…'` 携带演讲者备注。缺备注 = 不可交付 —— 继承 pptx v2 §Hard rules（H7）。morph 文稿往往视觉上极简，所以旁白要靠备注承载。

## 什么是 Morph？（核心机制）

PowerPoint 的 Morph 切换通过在相邻幻灯片之间对形状属性做插值来产生平滑运动，匹配依据是**完全相同的形状名称**。

```
Slide 1: shape name="!!scene-ring" x=5cm  width=8cm   fill=E94560 opacity=0.3
Slide 2: shape name="!!scene-ring" x=20cm width=12cm fill=E94560 opacity=0.6
         ↓  transition=morph on slide 2
Result:  Ring smoothly moves, grows, and fades darker over ~1 second
```

只有当第 N+1 页携带 `transition=morph` 时 Morph 才会运行。创建时通过 `officecli add / --type slide --prop transition=morph` 应用，或事后用 `officecli set "/slide[N]" --prop transition=morph` 补上。第 2 页起若遗漏该属性，将回落到母版的定义（通常没有切换）—— 运动会静默失效。

**三前缀命名体系（不可协商）：**

| 前缀 | 角色 | 生命周期 | 示例 |
|---|---|---|---|
| `!!scene-*` | 背景 / 装饰 —— 贯穿整份文稿持续存在 | 设置一次，通过调整位置/尺寸制造运动；**很少幽灵化** | `!!scene-ring`, `!!scene-bg-band`, `!!scene-grid` |
| `!!actor-*` | 内容 / 前景 —— 在一个章节内演化 | 在第 N 页引入，在 N+1、N+2… 页修改，在其退场页**幽灵化到 `x=36cm`** | `!!actor-feature-box`, `!!actor-metric`, `!!actor-headline` |
| `#sN-*` | 每页内容（标题、要点、说明） | 在第 N 页新添加，在第 N+1 页**幽灵化到 `x=36cm`** | `#s1-title`, `#s2-kpi`, `#s3-caption` |

**硬规则：** `!!scene-*` 与 `!!actor-*` 的名称绝不能撞车（例如同一份文稿中同时出现 `!!scene-card` + `!!actor-card` —— morph 引擎会混淆它们）。消歧方式：`!!scene-card-bg` vs `!!actor-card-content`。

**图表也可以参与 morph 配对。** `officecli add … --type chart` 接受 `--prop name=!!…`（名称可回读），因此相邻两页上 `!!` 名称完全一致的图表会参与形状名称的 morph 配对 —— 图表框架会插值位置 / 尺寸。注意 morph 无法插值图表框架*内部绘制的数据*。对于柱子生长 / 折线生长的叙事，如果柱子本身必须动起来：(a) 接受图表原样淡入，或 (b) 手工构建 N 个按数值定好尺寸的 `!!actor-bar-K` 矩形并对它们做 morph —— 每个矩形在相邻页上携带相同的 `!!actor-bar-K` 名称，而宽度 / 高度 / 填充随之演化。

**幽灵会静默累积。** 一旦某个带 `!!` 前缀的形状出现在任何一页上，它就会在其后每一张 morph 页上保持可见，除非被显式移到 `x=36cm`。`final-check` 辅助工具不会检测滞留在可见区域的 `!!` 形状 —— **只有 Gate 5b 截图审计能发现。** 写代码之前，先在配对表中规划好每个 Actor 的退场页。

**空间差异规则。** 相邻两页的构图必须**显著不同** —— 至少 3 个 morph 配对形状上满足位移 ≥ 5cm 或旋转 ≥ 15° 或尺寸变化 ≥ 30%。否则 morph 插值不出任何可见效果，切换退化为淡出（静默失败）。

**同帧时序约束。** 同一对 morph 中的所有 `!!` 形状同时动画。要让形状 A 先于形状 B，需要插入一个中间关键帧页 —— 没有按形状设置延迟的旋钮。

**配对 vs 入场 vs 退场 —— 三种行为，一条规则。** 同一机制（形状名称匹配）产生三种结果：

| 行为 | 源页 A | 目标页 B | 谁携带 `!!`？ |
|---|---|---|---|
| **配对 morph**（插值） | 有 `!!foo` | 有 `!!foo` | 两页，名称完全一致 |
| **入场**（淡入 / morph 进入） | ——（无对应物） | 有 `!!foo` | 仅目标页 —— 新形状 |
| **经幽灵退场**（滑出画面） | 有 `!!foo`，位于可见 `x` | 有 `!!foo`，位于 `x=36cm` | 两页 —— 名称相同，B 在画布外 |

**应该被打上 `!!` 前缀并幽灵化的是退场内容，不是入场内容。** 忘了给 `!!actor-*` 形状做标记时，它们会静默"消失" —— 名称在第 B 页缺失会被读作一次未配对的退场（普通淡出）。始终显式幽灵化到 `x=36cm`，让退场动画可见地从右边缘滑出。一个可运行示例：

```bash
# Slide 2: actor is visible at x=5cm — Slide 3: same name, ghosted off-canvas → visible slide-off motion
officecli add "$FILE" "/slide[3]" --type shape --prop 'name=!!actor-metric' \
  --prop text="42%" --prop x=36cm --prop y=8cm --prop width=6cm --prop height=3cm
```

**内容（`#sN-*`）每页都是新加的。** 因为文本每页都变，Morph 对标题 / 正文没有有意义的配对可做 —— 只能对它们交叉淡化。这正是 `#sN-*` 每页用不同名称的原因（它们被有意设为不配对），并且必须在第 N+1 页幽灵化。场景 Actor（`!!`）承载连续性；内容（`#`）承载信息。

## Morph 配对规划（写代码前，必须执行）

规划 morph 配对之前，如果文稿的受众 / 目的 / 叙事尚未明确，先运行 `reference/decision-rules.md` 中的规划提示词产出一份 `brief.md` —— 没有叙事主轴的 morph 弧线会退化成"带运动的幻灯片"，而非"带运动的故事"。

**在**写下任何 `officecli add` **之前**，先在 `brief.md` 中用一张表规划每一次切换。构建中途改形状名是幽灵累积 bug 的头号成因。

| 配对 | 幻灯片 A（起点） | 幻灯片 B（终点） | 参与的 Actor | 幻灯片 B 上的幽灵 |
|---|---|---|---|---|
| 1→2 | `!!scene-ring` 居中 5cm，`#s1-title` 可见 | 圆环移到 x=20cm，从 8 生长到 12cm；`#s2-subtitle` 揭示 | `!!scene-ring` 演化 | `#s1-title` → x=36cm |
| 2→3 | `!!actor-feature-box` 较大（宽 14cm） | Feature box 变小（6cm），`!!actor-metric` 入场 | `!!scene-ring`, `!!actor-feature-box`, `!!actor-metric` | `#s2-subtitle` → x=36cm |
| 3→4 | 内容章节 A | 章节 B 分隔页 | —— | `!!actor-feature-box` + `!!actor-metric` → x=36cm（章节退场）；`#s3-*` → x=36cm |

**规划规则：**

1. 一开始就定下所有 `!!` 名称 —— 每个 morph 配对形状在两页上必须使用**完全相同的名称**。
2. 把每个 `!!` 形状归类为 `!!scene-*` 或 `!!actor-*`。场景形状持久存在；Actor 必须有规划好的退场页。
3. **章节切换边界：** 进入新的主题章节时，在新章节首页把上一章节的全部 `!!actor-*` 幽灵化。只有 `!!scene-*`（全稿装饰）保留。
4. 表格补全之前不要开始构建。如果构建中途计划变了，重画表格并重新验证受影响的页面。

## Morph 配方（4 种模式）

四种模式覆盖约 95% 的 morph 文稿。全文使用 `$FILE="deck.pptx"`。每个代码块自成一体且 ≤ 20 行。

### (a) 单元素 morph —— 尺寸 / 位置

**视觉结果。** 一个主标题居中于第 1 页（48pt，y=8cm），第 2 页把它缩小到 32pt 并移到左上角（x=1.5cm, y=1cm）—— 让第 2 页的新内容登上主舞台。一个形状，干净的运动，没有 Actor。

```bash
FILE="deck.pptx"
officecli create "$FILE"; officecli open "$FILE"

# Slide 1 — hero
officecli add "$FILE" / --type slide --prop layout=blank --prop background=1E2761
officecli add "$FILE" /slide[1] --type shape --prop 'name=!!actor-headline' \
  --prop text="The one idea" --prop x=4cm --prop y=8cm --prop width=26cm --prop height=3cm \
  --prop font=Georgia --prop size=48 --prop bold=true --prop color=FFFFFF --prop align=center --prop fill=none

# Slide 2 — headline shrinks + moves; new body takes stage
officecli add "$FILE" / --type slide --prop layout=blank --prop background=1E2761 --prop transition=morph
officecli add "$FILE" /slide[2] --type shape --prop 'name=!!actor-headline' \
  --prop text="The one idea" --prop x=1.5cm --prop y=1cm --prop width=12cm --prop height=1.5cm \
  --prop font=Georgia --prop size=24 --prop bold=true --prop color=FFFFFF --prop align=left --prop fill=none
officecli add "$FILE" /slide[2] --type shape --prop 'name=#s2-body' \
  --prop text="Here is the supporting evidence." --prop x=1.5cm --prop y=5cm --prop width=30cm --prop height=2cm \
  --prop font=Calibri --prop size=20 --prop color=CADCFC --prop fill=none

officecli close "$FILE"; officecli validate "$FILE"
```

### (b) 多元素协同 morph —— Actors / 编排

**视觉结果。** 三个场景 Actor（`!!scene-ring`、`!!scene-dot`、`!!scene-band`）跨越 3 页重新布局，感觉像镜头横移。每页新标题通过 `#sN-*` 幽灵模式淡入 / 淡出。当叙事有连续的视觉背景时使用本配方。

```bash
# Slide 1 — anchor composition (already built via recipe a; here we add actors)
officecli add "$FILE" /slide[1] --type shape --prop 'name=!!scene-ring' --prop preset=ellipse \
  --prop fill=E94560 --prop opacity=0.3 --prop x=5cm --prop y=3cm --prop width=8cm --prop height=8cm
officecli add "$FILE" /slide[1] --type shape --prop 'name=!!scene-dot' --prop preset=ellipse \
  --prop fill=0F3460 --prop x=28cm --prop y=15cm --prop width=1cm --prop height=1cm

# Slide 2 — morph: ring moves + grows, dot slides left (spatial variety ≥ 5cm on both)
officecli set "$FILE" "/slide[2]" --prop transition=morph
officecli add "$FILE" /slide[2] --type shape --prop 'name=!!scene-ring' --prop preset=ellipse \
  --prop fill=E94560 --prop opacity=0.6 --prop x=20cm --prop y=2cm --prop width=12cm --prop height=12cm
officecli add "$FILE" /slide[2] --type shape --prop 'name=!!scene-dot' --prop preset=ellipse \
  --prop fill=0F3460 --prop x=3cm --prop y=16cm --prop width=1.5cm --prop height=1.5cm
# Ghost slide-1 content (name path still resolves after morph — see Known Issues)
officecli set "$FILE" "/slide[2]/shape[@name=#s1-title]" --prop x=36cm 2>/dev/null || true

# Verify morph pair: identical names on slides 1 & 2
officecli get "$FILE" /slide[1] --depth 1 --json | jq -r '.data.results[0].children[]?.format.name // empty'
officecli get "$FILE" /slide[2] --depth 1 --json | jq -r '.data.results[0].children[]?.format.name // empty'
# Compare — `!!scene-ring` and `!!scene-dot` MUST appear on both, byte-identical.
# Note: morph stores names with a `!!` prefix; compare the prefixed forms.
```

### (c) 连续多页 morph（故事弧线）—— 使用辅助工具

**视觉结果。** 一个 5 页弧线讲述一个连续的故事：随着叙事推进，同样的 2 个场景 Actor 在画布上漂移；内容（`#sN-*`）每页刷新并在下一页幽灵化。手工构建约需 60 条命令 —— 使用 `reference/morph-helpers.py` 让构建脚本更短并自动验证。

```python
#!/usr/bin/env python3
# Invoke the provided helper library for clone + ghost + verify
import subprocess, sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HELPERS = os.path.join(SCRIPT_DIR, "reference", "morph-helpers.py")
FILE = "deck.pptx"

def helper(*args):
    subprocess.run([sys.executable, HELPERS, *[str(a) for a in args]], check=True)

# ... assume slide 1 is built with 2 scene actors (!!scene-ring, !!scene-dot) + #s1-title
# Helper builds slide 2–5 with: clone from previous + apply transition=morph + ghost previous #sN- content
# `clone` prints the cloned slide's shape list — read it to pick which shape indices carry the
# previous slide's #s(n-1)- content, then pass those explicit indices to `ghost`.
for n in range(2, 6):
    helper("clone", FILE, n - 1, n)          # clone + set transition=morph + list shapes (note the #s(n-1)- indices)
    helper("ghost", FILE, n, 1, 2)           # ghost the #s(n-1)- content shapes by index (here shapes 1 & 2)
    # …then add THIS slide's #sN- content via officecli add as normal…
helper("final-check", FILE)                   # structural pass; DOES NOT catch !! lingering in visible area
```

辅助工具的签名与源码见 `reference/morph-helpers.py`（`clone`、`ghost`、`verify`、`final-check`）。shell 等价物是 `reference/morph-helpers.sh` —— 每个平台二选一；不要混用。

**何时用辅助工具 vs 裸 `officecli`。** 2-3 页的文稿，裸命令（配方 a、b）更清晰。5 页以上、伴随重复的 clone/ghost/verify 节奏时，辅助工具可省约 40% 的命令并内置验证。交付前每一页仍要用 `officecli validate` 收尾。

### (d) Morph + 淡入混合 —— morph 页上的入场

**视觉结果。** 一个 morph 配对中 `!!scene-ring` 持续移动，同时一张新的每页卡片淡入。当 morph 配对的背景负责引导视线、而前景新内容需要比凭空出现更柔和的入场时使用。

```bash
# Slide 2 already has transition=morph and !!scene-ring. Add a new card with fade-entrance.
officecli add "$FILE" /slide[2] --type shape --prop 'name=#s2-card' --prop preset=roundRect \
  --prop fill=F5F7FA --prop line=none --prop x=2cm --prop y=12cm --prop width=10cm --prop height=5cm

# Apply simultaneous-with-morph fade entrance to the new card.
# 'fade-entrance-300-with' = fade in, 300ms, trigger=withPrevious (plays with the morph transition).
officecli set "$FILE" "/slide[2]/shape[@name=#s2-card]" --prop animation=fade-entrance-300-with
officecli get "$FILE" "/slide[2]/shape[@name=#s2-card]" --json | jq '.data.results[0].format.animation'  # readback sanity — drops the trigger suffix, reads back as "fade-entrance-300"
```

**为什么可行。** Morph 只对 `!!scene-*` 形状做动画（它们在第 1 页有配对）；新的 `#s2-card` 在第 1 页没有对应物，所以 morph 会默认让它淡入 —— `fade-entrance-300-with` 把这次淡入显式化并加上时序。动画遵守 pptx v2 底线：≤ 600ms，禁止 bounce / swivel / fly-from-edge（规范预设清单见 `officecli help pptx animation`）。

## 编排 —— 动画类型 + 错峰时序

Morph 如何对多个形状做动画决定了观众看到什么。为每一对页面选对机制：

| 动画类型 | 如何实现（幻灯片 A 到幻灯片 B 之间） |
|---|---|
| 简单移动 | 两页同名 `!!`、同尺寸、不同的 `x`/`y` —— morph 对位置做插值 |
| 缩放变换 | 同名，不同的 `width`/`height` —— morph 对尺寸做插值（并重新定位中心） |
| 移动 + 缩放 | `x`、`y`、`width`、`height` 同时不同 —— morph 一次性处理所有维度 |
| 颜色 / 不透明度变化 | 同名，不同的 `fill` 或 `opacity` —— morph 对填充做交叉淡化 |
| 旋转 | 同名，不同的 `rotation`（度数）—— morph 沿最短弧旋转 |
| 字号变化 | 同名，文本形状上不同的 `size`（pt）—— 在 PowerPoint 365 中可插值；在 Keynote / WPS / LibreOffice 上不太可靠（可能退化为交叉淡化）。要获得可移植的运动，把 `size` 变化与匹配的 `width`/`height` 差值或 `x`/`y` 位移配对 —— 当尺寸插值失效时，空间变化仍能让运动可见 |
| 入场（淡入） | 形状只存在于幻灯片 B（A 上无对应物）—— morph 让它淡入 |
| 退场（淡出） | 形状只存在于幻灯片 A（B 上无对应物）—— morph 让它淡出 |

**多形状时序约束。** 同一对 morph 中的所有 `!!` 形状**同时**动画 —— CLI 中没有按形状设置延迟 / 时长的旋钮（帮助确认：slide 上没有 `morph.duration` / `morph.delay`）。要让形状 A 先于形状 B，**用一张中间页把切换拆成两对**：

```
Slide 2 → Slide 3:  !!actor-A moves (!!actor-B stays put)
Slide 3 → Slide 4:  !!actor-B moves (!!actor-A stays put or ghosts)
```

幻灯片 3 是一个显式的中间关键帧。不要试图用形状 `animation=` 属性上的时序参数伪造错峰 —— Morph 在每形状动画之前运行。

**"够用"的多样性启发式（最佳实践 —— 创作弹性）。** 要让 morph 读起来像"运动"，在主导配对形状上至少改变 {x, y, width, height, rotation, fill, opacity} 中的 3 项，且位移 ≥ 5cm 或旋转 ≥ 15° 或尺寸变化 ≥ 30%。单形状 × 3 属性是合法的创作模式（聚焦一个主角元素）。

**Delivery Gate 5b-morph-2 更严格。** 该门硬性断言每一对页面中 ≥ 3 个**不同的** `!!` 前缀形状各在 {x, y, width, height, rotation, font-size} 中至少变化 1 项 —— 这是"这真的是 morph 还是伪装 morph"的完整性检查。启发式指引创作意图；Gate 决定交付。**品牌恒定景物（固定的页眉条、页脚条、logo 徽标）不计入 3 形状配额** —— 它们本来就该待在原地；运动必须来自另外 3 个具名形状。拿不准时，按更严格的 Gate 执行。

**文稿长度节奏。** 给每次切换都塞 morph 读起来焦躁，而非电影感。按文稿长度安排 morph 时刻：
- **8-10 页（密集）：** 3-5 个 morph 时刻；运动可以聚集。
- **12-18 页（仪式感）：** 总计 3-5 个 morph，每 4-6 页一个；在章节分隔处用 `transition=morph`，让动画读作章节标点，而非持续的躁动。
- **18+ 页（幕结构）：** 按 3 幕组织，幕间放 1 个长章节分隔 morph（5-10 秒的刻意运动加短暂停留），每幕内部再放 2-3 个较轻的 morph。更多依赖 `!!scene-*` 的连续性，少用每页 `!!actor-*` 的反复折腾。

## 场景 Actor 空间规则

场景 Actor 与跨画布移动的 Actor 在 morph 期间必须待在可预测的区域 —— 否则它们会穿过内容，读作杂乱。

**安全区（场景 Actor 的停泊位与 morph 路径优先选这些）：**

```
Top-right corner:   x ≥ 24cm, y ≤ 6cm
Bottom-right:       x ≥ 24cm, y ≥ 12cm
Bottom-left:        x ≤ 2cm,  y ≥ 12cm
Off-canvas (ghost): x ≥ 33.87cm  (canvas right edge; use x=36cm for explicit ghost)
```

**避免让 Actor 停泊在内容核心区：** `x = 2~28cm, y = 3~16cm`。Actor 在 morph 途中**可以穿过**核心区（这正是运动本身），但不应该在高不透明度下把一页的终点停在那里 —— 除非它们本身就是内容（承载该页信息的 `!!actor-*`）。

**放置任何场景 Actor 之前，先检查现有形状的边界：**

```bash
officecli get "$FILE" "/slide[$N]" --depth 1 --json | \
  jq -r '.data.results[0].children[]? | "\(.format.name // .path)  x=\(.format.x) y=\(.format.y) w=\(.format.width) h=\(.format.height)"'
```

确认 Actor 的目标位置不与任何 `#sN-*` 内容形状的包围盒（`x` 到 `x + width`，`y` 到 `y + height`）重叠。若会重叠，把 Actor 的 `opacity` 降到 ≤ 0.15，或移到安全区。

## 风格库查找工作流

`reference/styles/` 收纳 52 个视觉风格目录（dark / light / warm / vivid / bw / mixed 基调）—— 是设计灵感，不是模板。把库当作**按需参考**，不是内容倾倒场。

**为什么是查找，不是照抄。** 52 个 `build.sh` 每个都是完整的风格演示 —— 但坐标是为那个特定演示的内容长度手工调的。把它们逐字抄进内容长度不同的文稿会产生重叠与错位（`INDEX.md` L5-11 已标记）。这个库的价值是**设计逻辑**：为某种基调选的配色、标志性形状、编排模式。把那个逻辑应用到自己的网格数学上。

**四步查找：**

1. **浏览 INDEX。** `reference/styles/INDEX.md` 按配色类别与基调分组全部 52 种风格（例如 `dark--premium-navy` = 权威 / 精致；`warm--earth-organic` = 有机 / 踏实）。Quick Lookup 表还列出每种风格的**主三色 hex**（bg / fg / accent）—— 如果用户指定了品牌色，扫 hex 列找最近的匹配，不必打开每个 `style.md`。挑出 1 种匹配主题基调或对齐用户指定 hex 的风格。
2. **读设计理念。** 打开 `reference/styles/<style-id>/style.md` 看设计意图 —— 字体搭配、颜色逻辑、标志性元素。
3. **扫一眼技法。** 打开 `reference/styles/<style-id>/build.sh` 仅作技法参考（标志性形状、配色 hex、编排点子）—— **坐标按 `INDEX.md` L5-11 属已知有 bug**；不要照抄。
4. **应用到自己的画布。** 用 pptx v2 网格数学 + 视觉底线构建文稿；只借配色与标志性手势。

**指针：** `→ see reference/styles/<style-id>/` —— 永远不要从某个风格的 build.sh 内联抄坐标。

## 交付门（继承 pptx v2 + morph 增补）

**Gate 1–5a：从 pptx v2 完整移植。** → see pptx v2 §Delivery Gate。Schema（白名单包含 C-P-2 图表 spPr）、token grep（`$…$` / `{{…}}` / `\$\t\n` / `()` / `[]`）、超链接 rPr（C-P-1）、幻灯片顺序检查、深底深字对比度（Gate 5a）。**在每一道 pptx Gate 1–5a 都打印 OK 消息之前，拒绝宣布完成。** morph 文稿与任何 pptx 一样面临 token / schema / 顺序风险。

### Gate 2 morph 附录 —— 被 zsh 吃掉的价格 / 指标 token

pptx v2 的 Gate 2 覆盖 `$…$`、`{{…}}`、`\$\t\n` 字面量、空 `()` / `[]`。morph 文稿额外多一类泄漏：用双引号 `--prop text="…"` 写的价格 / 指标 token（`$9/mo`、`$29/month`、`$199/yr`）—— shell 把 `$9` 当空变量吃掉，CLI 存下 `/mo` 或一个孤立句点。在 pptx Gate 2 之外再跑这个：

```bash
# Gate 2 morph — price / metric token leaks + stray-period placeholders
# Pattern hits: bare prices ($9, $29, $9.99), /unit suffix ($9/mo, $199/yr), ${VAR}, \n/\r/\t, lone period
LEAKS=$(officecli view "$FILE" text | grep -nE '\$[0-9]+(\.[0-9]+)?(/(mo|month|yr|year|day|wk|week|hr|hour))?|\$\{[A-Z_]+\}|\\[nrt]|^\.$' || true)
if [ -z "$LEAKS" ]; then echo "Gate 2 morph OK"; else echo "LEAK: $LEAKS"; fi
```

覆盖：`$9` `$9.99` `$29/month` `$199/yr` `$1/day` `${VAR}` `\n`/`\r`/`\t` 字面量 + 孤立的 `.` 占位符。修复：给属性加单引号（`--prop text='$9/mo'`）。

### Gate 5b —— 通过 HTML 预览做视觉审计（强制）—— morph 扩展

运行 `officecli view "$FILE" html` 并 Read 返回的 HTML 路径。对每一页回答 pptx v2 Gate 5b 的问题（重叠 / 深底深字 / 分隔线重叠 / 顺序合理 / 缺箭头）外加以下四项 morph 专属检查：

**重要：选择器的前缀匹配。** `officecli query` 只支持运算符 `=`、`!=`、`~=`、`>=`、`<=`、`>`、`<` —— 没有 `^=` 前缀运算符。`shape[name^=!!actor-]` 这样的选择器会返回 `invalid_selector` 错误。做"前缀起于"过滤时，用下文所示的 `get --depth 1` 循环 + `jq startswith()`。

- **5b-morph-1 —— `!!actor-*` 在其章节结束后泄漏进可见区域。** 对每个本应已退场的 `!!actor-*`，确认 `x ≥ 33.87cm`（画布右边缘）。循环 + 过滤（选择器安全）：
  ```bash
  NSLIDES=$(officecli query "$FILE" slide --json | jq '.data.results | length')
  for N in $(seq 1 $NSLIDES); do
    officecli get "$FILE" "/slide[$N]" --depth 1 --json | \
      jq -r --arg n "$N" '.data.results[0].children[]? |
        select(.format.name? // "" | startswith("!!actor-")) |
        select((.format.x // "0cm" | rtrimstr("cm") | tonumber) < 33.87) |
        "slide \($n) leak: \(.format.name) stuck at x=\(.format.x)"'
  done
  ```
  打印出任何一行 = Actor 滞留可见。`final-check` 漏掉这种情况 —— 只有循环 + Read HTML 能抓到。

- **5b-morph-2 —— 相邻页面空间构图完全一致（没有运动）。** 硬规则：每对 morph 页之间，≥ 3 个**不同的** `!!` 前缀形状必须各在 {x, y, width, height, rotation, font-size} 中至少差异 1 项。证明循环（转储两页，diff 同名形状，数差异形状数）：
  ```bash
  for K in 1 2 3 4; do
    A=$(officecli get "$FILE" "/slide[$K]" --depth 1 --json | \
      jq -r '.data.results[0].children[]? | select(.format.name? // "" | startswith("!!")) |
        "\(.format.name)|\(.format.x)|\(.format.y)|\(.format.width)|\(.format.height)|\(.format.rotation // 0)"')
    B=$(officecli get "$FILE" "/slide[$((K+1))]" --depth 1 --json | \
      jq -r '.data.results[0].children[]? | select(.format.name? // "" | startswith("!!")) |
        "\(.format.name)|\(.format.x)|\(.format.y)|\(.format.width)|\(.format.height)|\(.format.rotation // 0)"')
    VARIES=$(diff <(echo "$A") <(echo "$B") | grep -c '^[<>]')
    if [ "$VARIES" -lt 6 ]; then echo "pair $K→$((K+1)) FLAT: only $VARIES diff-lines (need ≥ 6 = 3 shapes × 2 sides)"; fi
  done
  ```

- **5b-morph-3 —— Morph 配对名称不匹配。** 相邻页必须至少精确共享 2 个 `!!` 前缀名称。证明（注意：children 位于 `.data.results[0].children[]` —— 裸的 `.data.children[]` 返回 null）：
  ```bash
  for N in 1 2 3 4 5; do
    echo "--- slide $N ---"
    officecli get "$FILE" "/slide[$N]" --depth 1 --json | \
      jq -r '.data.results[0].children[]? | select(.format.name? // "" | startswith("!!")) | .format.name'
  done
  ```
  目视比较相邻块 —— N 与 N+1 之间共享的 `!!` 名称就是 morph 配对。零重叠 = 这一对只是普通淡出。

- **5b-morph-4 —— `#sN-*` 在第 N+1 页滞留（幽灵泄漏）。** 每页内容必须在**下一页**被幽灵化（`x=36cm`）。对每个 N≥2 循环 + 过滤：
  ```bash
  NSLIDES=$(officecli query "$FILE" slide --json | jq '.data.results | length')
  for N in $(seq 2 $NSLIDES); do
    PREV=$((N-1))
    officecli get "$FILE" "/slide[$N]" --depth 1 --json | \
      jq -r --arg n "$N" --arg p "$PREV" '.data.results[0].children[]? |
        select(.format.name? // "" | startswith("#s\($p)-")) |
        select((.format.x // "0cm" | rtrimstr("cm") | tonumber) < 33.87) |
        "slide \($n) leak: \(.format.name) stuck at x=\(.format.x)"'
  done
  ```
  打印出任何一行 = 某个 `#s(N-1)-*` 形状在第 N 页保持可见。把它幽灵化。

**若任何 5b-morph-1..4 循环打印了行，拒绝交付。** 把四个循环的 stdout 汇总成一个流，并用 COUNT 模式强制执行：`LEAK_COUNT=$(...all four loops... | wc -l); if [ "$LEAK_COUNT" -gt 0 ]; then echo "REJECT: $LEAK_COUNT morph leaks"; else echo "Gate 5b-morph OK"; fi`。

## 渲染器诚实

**Morph 可在以下环境渲染：** PowerPoint 365 (Windows/Mac)、Keynote、WPS、PowerPoint Online。

**Morph 不在以下环境渲染：** LibreOffice Impress（渲染为静态，有时呈淡出）、Google Slides 网页查看器（丢失插值）、大多数 HTML / SVG 查看器、`officecli view html`（仅结构 —— morph 是运行时特性）。这属于 `[RENDERER-BUG]`，不是 Skill 缺陷。明确告诉用户："请在 PowerPoint 365 / Keynote / WPS 中打开以查看 morph 运动；其他查看器只会显示静态画面或普通淡出。"（Open in PowerPoint 365 / Keynote / WPS to see the morph motion; other viewers will show static or plain fade.）

来自任何渲染器的静态截图**都无法验证 morph 运动**（运动只存在于运行时）。用上文的 Gate 5b 查询证明配对正确性；用实时查看器证明运动质量。

## 幽灵纪律与 Actor 生命周期

**每个 `!!actor-*` 和 `#sN-*` 形状必须在每一页都被管理，而不只是它的"退场"页。**

### 逐页幽灵化规则

构建多页 morph 文稿时：
1. **第 N 页：引入 `!!actor-ring`（在 x=0cm 处可见）**
2. **第 N+1 页：添加新内容。收尾之前，把 `!!actor-ring` 幽灵化到 `x=36cm`。**
3. **第 N+2 页：再添加内容。再次把 `!!actor-ring` 幽灵化到 `x=36cm`。**（不可选 —— 即便它已在画面外，每一页都是新画布。）
4. **第 N+3 页：如果 `!!actor-ring` 应当再次可见，把它移回 x=0cm 或它的新位置。**

**为什么：** 每页的形状列表相互独立。在第 N 页把形状移出画布**不会**带到第 N+1 页 —— 忘了重新幽灵化，它就会在 N+1 的原位重新出现。

### 工作流模式（Bash）

```bash
# After adding new content shapes to slide $SLIDE:
for ACTOR in "!!actor-ring" "!!actor-dot" "!!actor-accent-bar"; do
  officecli set "$FILE" "/slide[$SLIDE]/shape[@name=$ACTOR]" --prop x=36cm || true
done
```

或在构建循环里：

```bash
for SLIDE_NUM in 3 4 5 6 7 8 9 10 11; do
  # Add content specific to this slide
  officecli add "$FILE" "/slide[$SLIDE_NUM]" --type shape ...
  
  # IMMEDIATELY ghost all old actors (M-2 prevention)
  officecli set "$FILE" "/slide[$SLIDE_NUM]/shape[@name=!!actor-ring]" --prop x=36cm || true
  officecli set "$FILE" "/slide[$SLIDE_NUM]/shape[@name=!!actor-dot]" --prop x=36cm || true
done
```

### 检测：幽灵计数门

`morph-helpers.py final-check` 统计所有位于 `x ≥ 34cm` 的形状。若计数 > 50，它打印：
```
REJECT: Found 135 accumulated ghosts — likely M-2 ghost accumulation.
Run: officecli query deck.pptx 'shape[x>=34cm]' --json | jq '.data.results | length'
Expected ≤ 50 (roughly 4–5 active actors × 10–12 slides).
```

**修复：** 回查构建日志，确保每一页都重新幽灵化了所有不该出现在该页的 Actor。重跑 final-check。若仍 > 50，使用 `morph-helpers.py clean-accumulation deck.pptx`（见参考章节）。

## 常见 Morph 陷阱（设计 + 工作流陷阱）

基础 pptx 陷阱（shell 引号、zsh 的 `[N]` 通配、hex `#` 前缀、属性文本中的 `\n`）→ see pptx v2 §Common Pitfalls。以下是 morph 专属陷阱：

| 陷阱 | 正确做法 |
|---|---|
| 同一文稿中同时出现 `!!scene-card` 和 `!!actor-card` | 名称必须跨前缀唯一。改名：`!!scene-card-bg` vs `!!actor-card-content` |
| 部分页面已完成后中途改形状名 | 幽灵累积 bug 一触即发。停下，重画 §Morph Pair Planning 表，重跑受影响页面 |
| 把 `!!actor-*` 放进内容核心区却不规划退场 | 每个 `!!actor-*` 都需要一页幽灵化。写代码前在配对表中规划好 |
| **幽灵累积（M-2）：忘了在后续页面重新幽灵化 `!!actor-*`** | **关键：** 给第 N+1 页添加新内容时，所有不该可见的第 N 页 `!!actor-*` 必须再次移到 `x=36cm`。不要假设幽灵化一次就一直留在画面外 —— 每页相互独立。构建模式：`for each new slide: add content shapes → then loop: set each active !!actor-* to x=36cm`。幽灵计数超过 50 时 `morph-helpers.py final-check` 会 REJECT。 |
| 某页忘了 `transition=morph` | 静默淡出。Gate 5b-morph-2（无运动）能抓到；用 `set /slide[N] --prop transition=morph` 修复 |
| 以为 `@name=` 路径在 morph 页上会失效 | 不会 —— `transition=morph` 之后 `@name=` 仍可解析（M-1）；只有*回读*名称会带上 `!!` 前缀 |
| 相邻页面视觉上完全相同 | Morph 无东西可插值 —— 退化为普通淡出。应用 §Scene-actor spatial rule，把 ≥ 3 个形状移动 ≥ 5cm / ≥ 15° |
| 试图用按形状时序给 2 个形状错峰 | 不支持 —— 用一张中间关键帧页把配对拆成两次切换 |
| 在 LibreOffice 或浏览器里测试 morph 运动 | 属 `[RENDERER-BUG]`，非 Skill 缺陷。在 PowerPoint 365 / Keynote / WPS 中测试 |
| 在退场时删除 `!!` 形状而不是幽灵化 | 删除会破坏 morph 配对 —— 形状无动画直接消失。始终幽灵化到 `x=36cm` |
| 用双引号写 `--prop text="$9/mo"` | Shell 把 `$9` 当空变量吃掉 → 文本存为 `/mo` 或孤立 `.`。用单引号：`--prop text='$9/mo'`。Gate 2 morph 附录会 grep 此泄漏。 |
| 在 `--prop text='line1<a:br/>line2'` 中使用 `<a:br/>` 字面量 | 会被存为 7 个字面字符，不是换行。每行用一次 `officecli add "/slide[N]/shape[@id=K]" --type paragraph`（M-6）。 |
| 使用 `shape[name^=!!actor-]` 选择器 | `officecli query` 没有 `^=` 运算符 —— 返回 `invalid_selector`。改用 `get /slide[N] --depth 1 --json \| jq '.data.results[0].children[]? \| select(.format.name \| startswith("!!actor-"))'`。 |

## 已知问题与陷阱

基础 pptx 缺陷 C-P-1..7（超链接 rPr、图表 ChartShapeProperties 警告、动画时长回读、动画移除、连接线枚举、连接线 `@name=`、图表颜色渲染器归一化）全部适用。**变通方案 → see pptx v2 §Known Issues C-P-1..7。**

**Morph 专属（M-1..5）：**

| # | 症状 | 变通方案 |
|---|---|---|
| **M-1** | 执行 `officecli set '/slide[N]' --prop transition=morph` 后，该页每个形状的名称被自动前置 `!!`（`#s1-title` → `!!#s1-title`）。回读名称是带前缀的形式。**选择器过滤提醒：** 自动前缀后，`!!#sN-caption` 与 `!!actor-*` 并存 —— 在 `jq` 中用 `startswith("!!")` 过滤"场景 Actor"会误匹配自动前缀的内容。始终用 `startswith("!!actor-")` 或 `startswith("!!scene-")` 过滤，绝不用裸的 `startswith("!!")`。 | `@name=` 路径选择器**仍可解析** —— `/slide[N]/shape[@name=#s1-title]` 能返回该形状（匹配对后缀/前缀容忍），无需改写路径。当需要在 jq 过滤器中使用带前缀的名称时，把开头的 `!!` 算进去。 |
| **M-2 🚨** | **幽灵累积 —— 第 3 页引入的 `!!actor-*` 会在第 4、5、6 页保持可见，除非每一页都显式幽灵化。** `final-check` 辅助工具能检测这一点，幽灵计数 > 50 即拒绝。 | **强制逐页规则：** 给某页添加新内容后，立即把此前各页所有活跃的 `!!actor-*` 设为 `x=36cm`（或在当前上下文中确实属于该页的，显式摆到可见位置）。示例：`officecli set /slide[4]/shape[@name=!!actor-ring] --prop x=36cm`。每次添加页面后都要运行，不能只到最后。见下文 §Ghost Discipline & Actor Lifecycle。 |
| **M-3** | 章节切换边界 —— 在新主题章节的首页，上一章节的 `!!actor-*` 形状可见地滞留。无任何命令报错；只有视觉杂乱。 | 在每个章节起始页，显式把上一章节的全部 `!!actor-*` 幽灵化到 `x=36cm`。场景形状（`!!scene-*`）保留。 |
| **M-4** | Agent 有时会发明 `morph.duration=` / `transition.delay=` 作为独立属性 —— 会被以 UNSUPPORTED 拒绝。 | 使用 `transition` 属性上的组合简写：`transition=morph-slow` / `-fast`，或 `transition=morph-<DUR_MS>`（例如 `transition=morph-1500`）。两者在回读时均可往返还原（`transitionSpeed=slow`、`transitionDuration=1500`）。只有超出简写所及的场合（对原始 XML 的精细控制），才回退到对 `<p:transition>` 做 `raw-set` —— 见下方 M-4 示例块。 |
| **M-5** | `[RENDERER-BUG]` LibreOffice / Google Slides 网页查看器把 morph 页渲染成普通淡出（无插值）。 | 在 PowerPoint 365 / Keynote / WPS 中测试。不是 Skill 缺陷 —— 不要去追。 |
| **M-6** | 写在 `--prop text='line1<a:br/>line2'` 内的 `<a:br/>` 被存为 7 字符的字面字符串，不被解释为换行。观众看到的是逐字渲染的 `line1<a:br/>line2`。 | 多行要点 / 说明，每行加一个段落：先 `officecli add "/slide[N]/shape[@id=K]" --type paragraph --prop text='line1'`，再以 `text='line2'` 重复。真实换行工作流见 pptx v2 §Shell escape。 |

**M-4 示例 —— 放慢所有 morph 切换，raw-set 回退**（优先 `transition=morph-slow`；仅当需要超出简写的控制时才用本方法）。注意 `//p:transition` 会同时匹配 morph 页上的 `mc:Choice` 与 `mc:Fallback`，因此显示 `2 element(s) affected`：

```bash
# Per-slide: add spd="slow" to every transition element on slide N (2 XML hits per morph slide)
for N in 2 3 4; do
  officecli raw-set "$FILE" "/slide[$N]" --xpath "//p:transition" --action setattr --xml 'spd=slow'
done
officecli validate "$FILE"
```

回读：`officecli query "$FILE" slide --json | jq '.data.results[].format | select(.transition=="morph") | .transitionSpeed'` 对每个受影响页打印 `"slow"`。

## 产出与交付

每份 morph 文稿附带三个工件，各自独立成文件：

1. `<topic>.pptx` —— 演示文稿本体，close + `officecli validate` 干净（Delivery Gate 1 OK）。
2. `build.sh` 或 `build.py` —— 可重跑的构建脚本（shell 原生构建用 bash；使用 `morph-helpers.py` 的多页弧线用 Python）。必须能从一次全新的 `officecli create` 调用重建整份文稿。
3. `brief.md` —— **独立文件，不嵌入任何其他文件。** 包含：
   - 第 1 节：主题 / 受众 / 目的 / 叙事 / 风格方向（来自 `reference/styles/INDEX.md` 的 1 个具名风格）
   - 第 2 节：逐页大纲（每页的页面类型 + 一句话论证）
   - 第 3 节：§Morph Pair Planning 表（Pair / Slide A / Slide B / Actors / Ghosts）—— 审计编排所需的**设计记录**（the design record the reviewer needs to audit choreography）

**交付前提醒用户（措辞可直接照用）：**

- "The deck is ready with morph transitions. Open it in PowerPoint 365 / Keynote / WPS to see the motion — LibreOffice and web viewers render static."（文稿已就绪并带 morph 切换。请在 PowerPoint 365 / Keynote / WPS 中打开以查看运动 —— LibreOffice 与网页查看器只会显示静态画面。）
- "While the build script is running, the `.pptx` may be rewritten several times. If you want to preview progress, use `officecli watch "$FILE"` and open the live preview in AionUi — do NOT click 'Open with system app' during the build, or you'll hit a file lock."（构建脚本运行期间，`.pptx` 可能被多次重写。如需预览进度，请使用 `officecli watch "$FILE"` 并在 AionUi 中打开实时预览 —— 构建期间不要点击 "Open with system app"（用系统应用打开），否则会撞上文件锁。）

## 创建后的调整

标准调整表 → see pptx v2 §Common Pitfalls / `swap` / `move` / `remove` / `set`。Morph 注意事项：**任何打乱 morph 配对页面顺序的 `swap` 或 `move` 之后，重新验证共享 `!!` 名称的相邻性。** 对受影响的配对重跑上文的 Gate 5b-morph-3 查询 —— 如果 swap 拆散了一对，要么重命名形状，要么重新编排切换。

**交付前的最终健全性检查。** 运行完整的 Delivery Gate（1 到 5b-morph-1..4），在 PowerPoint 365 / Keynote / WPS 中打开 `.pptx`，完整观看一次页到页的 morph，确认运动可见。任何 Gate 打印 REJECT，修复后重跑 —— 绝不在已知未闭合的 Gate 下交付。

## 参考资料（References）

- `reference/decision-rules.md` —— 金字塔原理、SCQA、页面类型菜单、`brief.md` schema。在 §Morph Pair Planning 期间阅读，用于在写命令前决定叙事弧线。
- `reference/pptx-design.md` —— 残留设计笔记（Scene Actors 机制、页面类型表、编排模式）。画布 / 字体 / 颜色在 pptx v2 中 —— 本文件只覆盖 morph 独有材料。
- `reference/morph-helpers.py` —— 跨平台（Mac / Windows / Linux）Python 辅助工具，覆盖 clone + ghost + verify + final-check。可作为库导入，也可通过 CLI 参数调用。5 页以上的弧线优先使用。
- `reference/morph-helpers.sh` —— Bash 等价物。每个项目二选一；不要混用。
- `reference/styles/INDEX.md` —— 52 式视觉库，按配色（dark / light / warm / vivid / bw / mixed）与基调分组。查找工作流见上文 §Style library lookup workflow。
- `skills/officecli-pptx/SKILL.md` —— 基础 pptx v2 规则（视觉底线、网格、规范配色、图表选型、连接线规范、Delivery Gate 1–5a、已知问题 C-P-1..7、Shell 转义三层）。
