> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-process.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 过程图（Process）

**最适用于：** 有多个参与者/部门的顺序业务流程，读者需要看清*谁*在*做什么*、每一步*进出什么数据*、*使用哪些工具*，而不只是步骤顺序。覆盖职责审计、数据质量门禁评审、跨部门交接图与端到端工作流文档。

数据类型和工具不重要时，选更简单的泳道图。每一步的输入/输出载荷与责任团队需要一眼看清时，选过程图。核心论点是各阶段的台前与幕后之分（一条可视线，而非顺序交接）时，选**服务蓝图**（`type-service-blueprint.md`）。

本类型是**参数化的**：§1 的输入模式经 §2 的公式驱动每一个坐标。相同输入生成两次，必须产出视觉上完全一致的 SVG。规则形态与 `type-data-flow.md` 一致，因此颜色覆盖、IN/OUT 标签片语义与可复现性检查清单在各类型间读法相同。

---

## 1. 输入：参数契约

```yaml
lanes:                              # 1..6 horizontal swimlanes (top to bottom)
  - { name: ["RD&E"],                 key: "RDE" }
  - { name: ["IT"],                   key: "IT"  }
  - { name: ["FIELD", "SERVICES"],    key: "FLD" }
  - { name: ["SURVEY", "SERVICES"],   key: "SVY" }
  - { name: ["HOUSEHOLD", "UNIT"],    key: "HHU" }
  - { name: ["COMMS &", "MARKETING"], key: "CMM" }

steps:                              # 1..12 vertical step columns (left to right)
  - { number: "1",  label: "Design"   }
  - { number: "2",  label: "Build"    }
  - { number: "3",  label: "Test", focal: true }       # focal step header chip — accent fill
  - { number: "4",  label: "Train"    }
  # ... up to 12

nodes:                              # explicit per-cell entries; empty cells render nothing
  - { lane: "RDE", step: 0,  title: "Survey design",      sub: "questionnaire · sampling", tool: "Excel · CSPro",
      chips: {in: null,  out: "FL"} }              # first step has no input chip
  - { lane: "IT",  step: 1,  title: "Build app",          sub: "form + validation",        tool: "CSPro · scripts",
      chips: {in: "FL", out: "TB"}, color: "#5a7d9a" }    # slate-blue — data quality concern
  - { lane: "RDE", step: 2,  title: "Pilot test",         sub: "field debug",              tool: "tablet · script",
      chips: {in: "TB", out: "TB"}, focal: true }   # focal node — accent border
  - { lane: "FLD", step: 3,  title: "Train enumerators",  sub: "protocols · safety",       tool: "manual",
      chips: {in: "TB", out: "LS"}, color: "#b85450" }    # rust-red — governance / training
  # ... etc

arrows:                             # explicit edges; styles bind to topology (see §3)
  - { from: {lane: "RDE", step: 0}, to: {lane: "IT",  step: 1}, style: "normal" }
  - { from: {lane: "IT",  step: 1}, to: {lane: "RDE", step: 2}, style: "focal-in" }     # accent — into focal
  - { from: {lane: "RDE", step: 2}, to: {lane: "FLD", step: 3}, style: "focal-out" }    # accent — out of focal
  - { from: {lane: "RDE", step: 2}, to: {lane: "IT",  step: 1}, style: "trigger" }      # dashed trigger
  # ... etc

dark: false
```

**保留字段语义：**
- `lanes[k].key`：该泳道内每个节点里显示的 3 字母角色徽章文字。
- `lanes[k].name`：1 或 2 行的泳道标签；大写等宽字体。
- `steps[j].focal: true`：只允许**一个**步骤声明。头部标签片以 accent 渲染。
- `nodes[i].focal: true`：只允许**一个**节点声明。以 accent 描边渲染（§5）。
- `nodes[i].chips`：`{in: "<CODE>", out: "<CODE>"}` 对象（任一侧为 `null` 表示省略）。代码见 §8。第一步的节点**跳过**输入标签片，最后一步的节点**跳过**输出标签片（没有上游/下游）。
- `nodes[i].color`：可选的**按节点颜色覆盖**。任何合法的 `"#hex"` 字符串；为了跨图一致性，推荐使用 §4 的调色板。

---

## 2. 布局公式：确定性几何

```
label_col_w      = 140
step_slot_w      = 112                                # 100-px node + 12-px corridor
right_pad        = 28
n_steps          = len(steps)
n_lanes          = len(lanes)

# Canvas
viewBox_w        = label_col_w + n_steps * step_slot_w + right_pad   # 11 steps → 1400
header_h         = 36
lane_h           = 80
has_color_row    = any(node.color or step.color or lane.color in inputs)
legend_h         = 100 if has_color_row else 80       # 4 rows when colors are present
viewBox_h        = header_h + n_lanes * lane_h + legend_h            # 6 lanes, no colors → 596; with → 616

# Header strip (top)
chip_y           = 8
chip_w           = 16                                  # 20 if step.number has 2 digits
chip_h           = 16
chip_rx          = 8                                   # pill

# Lane positions
lane_y_top(k)    = header_h + k * lane_h               # 36, 116, 196, 276, 356, 436
lane_y_mid(k)    = lane_y_top(k) + lane_h/2            # 76, 156, 236, 316, 396, 476
lane_label_x     = label_col_w / 2                     # 70

# Step / node centers
step_cx(j)       = label_col_w + 8 + j * step_slot_w + node_w/2      # 198, 310, 422, ...
                                                                      # (8-px gutter inside content area)

# Nodes
node_w           = 100
node_h           = 64
node_x(j)        = step_cx(j) - node_w/2
node_y(k)        = lane_y_top(k) + (lane_h - node_h)/2     # 8-px top/bottom margin inside lane

# Legend strip (bottom)
legend_y_top     = header_h + n_lanes * lane_h
legend_row_y     = [legend_y_top + 16, legend_y_top + 37,
                    legend_y_top + 58, legend_y_top + 79]
```

### 2.1 背景结构

- 整个 viewBox 铺纸面填充。
- 圆点纹理：22×22 网格，`circle r=0.8`，`fill ink @ 0.10`。不透明度 0.55。
- 交替泳道底色：奇数序位泳道（0, 2, …）从 `x=140` 到 `viewBox_w` 接受 `ink @ 0.018` 填充。
- 泳道分隔线：在每个 `lane_y_top(k)` 与 `legend_y_top` 处画水平发丝线；描边 `ink @ 0.12`，宽 0.8。
- 标签列右边框：在 `x = label_col_w` 处画垂直发丝线，描边 `ink @ 0.20`，宽 1，从 `y = header_h` 到 `y = legend_y_top`。

### 2.2 步骤头部标签片与标签

对每个步骤 `j`：

```
chip_w(j)        = 20 if len(step.number) >= 2 else 16
chip_x(j)        = step_cx(j) - chip_w(j)/2
number_anchor    = (step_cx(j), chip_y + 11)
label_anchor     = (step_cx(j), 32)              # 8-px gap below chip
```

**标签片**（每列顶部的编号胶囊）：
- 默认填充：`ink @ 0.12`，编号文字为 ink。
- 焦点填充：`accent @ 0.20`，编号文字为 accent（§5）。
- 按步骤 `color` 覆盖（§4）：把填充替换为 `rgba(C, 0.20)`，编号填充替换为 `C`。

**标签**（标签片下方的大写等宽文字）：
- 渲染 `steps[j].label`（转大写），锚定在 `label_anchor`。
- 字体：`eyebrow` 角色的等宽字族，6 px，weight 500，`letter-spacing="0.12em"`，`text-anchor="middle"`。
- 默认填充：`muted`。
- 焦点填充：`accent`。
- 按步骤 `color` 覆盖：填充 = `C`（与标签片编号颜色一致）。
- 标签要短（≤ 9 字符）。过长会截断；不够用就缩写。

### 2.3 泳道标签

一到两行的等宽标签，全大写，letter-spacing 0.08em，字号 8，填充 muted。居中于 `(lane_label_x, lane_y_mid(k))`：
- 单行：锚定在 `(lane_label_x, lane_y_mid(k) + 4)`
- 两行：分别位于 `(lane_label_x, lane_y_mid(k) - 4)` 与 `(lane_label_x, lane_y_mid(k) + 4)`

按泳道 `color` 覆盖（§4）：把标签填充替换为 `C`，泳道条纹底色替换为 `rgba(C, 0.04)`。

### 2.4 节点内容布局（100×64 矩形内部）

```
role_chip          rect 14×10 at (node_x+4, node_y+4),  rx=2
role_chip_text     centered at (node_x+11, node_y+12), font-size=6, weight=600
                                                                # text = lanes[k].key (3-letter lane code)
title              centered at (step_cx(j), node_y+26),  font-size=9 sans semibold
in→out             centered at (step_cx(j), node_y+40),  font-size=6.5 mono muted
tool               centered at (step_cx(j), node_y+52),  font-size=6.5 mono soft
data chip IN       rect 16×8 at (node_x+4,   node_y+54), rx=2      # payload entering
data chip OUT      rect 16×8 at (node_x+80,  node_y+54), rx=2      # payload leaving
```

**角色徽章文字规则：**每个节点内的徽章渲染 `lanes[k].key`，其中 `k` 是节点所在泳道的序号，**不是**步骤编号（步骤编号已在该列顶部的头部标签片里，见 §2.2）。用泳道 key 作节点徽章，让每个节点自带“谁”的标识，单个节点被摘出上下文后依然可读。与 `type-data-flow.md` §2.4 的规则一致。

空单元格（无节点条目）**什么都不渲染**。没有占位矩形、没有角色徽章、没有标签。

**标签片与工具文字冲突规则：**标签片位于 `node_y + 54..62`；工具文字基线在 `node_y + 52`。若节点标题有两行（少见），把 node_h 加大到 72，或者省略该节点的标签片。默认行为：冲突时省略标签片。

---

## 3. 连线规则（强制）

三种样式，与拓扑绑定。连线绘制在**所有**节点矩形**之前**（z-order 规则）。

| `style` | 描边 | 宽度 | 虚线 | Marker | 何时必须使用 |
|---|---|---|---|---|---|
| `normal` | `muted` | 1.0 | — | `arrow` | 步骤之间或参与者之间的标准数据交接。不带标签。 |
| `focal-in` / `focal-out` | `accent` | 1.2 | — | `arrow-accent` | 终点是焦点节点（`focal-in`）或起点是焦点节点（`focal-out`）的每条边。 |
| `trigger` | `muted` | 1.0 | `4,3` | `arrow-sm` | 编排触发（调度器 → 工具，人工干预 → 上游步骤）。不带标签。 |

**Defs 块**（必需，三个 marker）：

```svg
<defs>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="11" cy="11" r="0.8" fill="{ink @ 0.10}"/>
  </pattern>
  <marker id="arrow"        markerWidth="8" markerHeight="6" refX="7" refY="3"   orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{muted}"/></marker>
  <marker id="arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3"   orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{accent}"/></marker>
  <marker id="arrow-sm"     markerWidth="6" markerHeight="5" refX="5" refY="2.5" orient="auto"><polygon points="0 0, 6 2.5, 0 5" fill="{muted}"/></marker>
</defs>
```

输出前，先按 [`style-guide.md`](style-guide.md) 中当前皮肤解析 `{ink @ 0.10}`、`{muted}` 与 `{accent}`。

### 3.1 布线规则（不可妥协）

**单折直角：**从右侧出 → 走廊 → 从顶部进入（↓ 目标在下方）或底部进入（↑ 目标在上方）。

- 起点侧：从 `(node_x + 100, lane_y_mid(src_lane))` 出发，即节点右边缘、垂直居中。
- 终点侧：向下时进入 `(step_cx(dst_step), node_y(dst_lane))`，向上时进入 `(step_cx(dst_step), node_y(dst_lane) + 64)`。
- 圆角：折弯处用 8px 的 Q 贝塞尔曲线。
- 同泳道边（少见：同泳道、相邻步骤）：从源右侧到目标左侧的水平 `<line>`。
- **不允许斜线。不允许从左侧进入。不允许从节点顶部/底部出发。**

```svg
<!-- Downward (destination lane > source lane) -->
<path d="M {rx},{src_cy} H {dst_cx - 8} Q {dst_cx},{src_cy} {dst_cx},{src_cy + 8} V {dst_top}"
      fill="none" stroke="…" stroke-width="…" marker-end="…"/>

<!-- Upward (destination lane < source lane) -->
<path d="M {rx},{src_cy} H {dst_cx - 8} Q {dst_cx},{src_cy} {dst_cx},{src_cy - 8} V {dst_bottom}"
      fill="none" stroke="…" stroke-width="…" marker-end="…"/>

<!-- Same lane (adjacent step) -->
<line x1="{src_right}" y1="{lane_cy}" x2="{dst_left}" y2="{lane_cy}"
      stroke="…" stroke-width="…" marker-end="…"/>
```

- **Z-order：**所有 `<path>` 与 `<line>` 连线都先于任何节点 `<rect>` 输出。
- **Marker：**每条 path 恰好一个 `marker-end`。绝不用 `marker-start`。
- **标签：**所有过程箭头默认不带标签。步骤编号 + 参与者泳道已经承载语义，每条箭头都贴标签就是噪音。只有当箭头表示非步骤概念（复测循环、升级上报）时才加标签，此时用 6.5px 等宽文字，背后垫纸面色遮罩矩形。

### 3.2 交叉

避免交叉。走廊的 x 位置（目标节点前 8px）是唯一的布线列：若两条箭头会在此交叉，**调换步骤分配**或**拆成两张图**，不要引入绕行折弯。交叉会掩盖底层的控制流。

---

## 4. 组件颜色覆盖

任意节点、泳道或步骤都可接受可选的 `color: "#hex"`。规则与 `type-data-flow.md` §4、`type-high-level.md` §3.4 一致，各类型间读法相同。

### 4.1 按节点 `color`

应用于：

| 元素 | 浅色 | 深色 |
|---|---|---|
| 容器填充（`rect`） | `rgba(C, 0.06)` | `rgba(C_light, 0.10)` |
| 容器描边 | `rgba(C, 0.35)`（stroke-width 1） | `rgba(C_light, 0.45)` |
| 角色徽章填充 | `rgba(C, 0.18)` | `rgba(C_light, 0.22)` |
| 角色徽章文字 | `C` | `C_light` |
| 标题文字 | `C` | `C_light` |
| 子标签（in → out） | **不变**（muted） | **不变**（muted） |
| 工具标签 | **不变**（soft） | **不变**（soft） |
| 数据类型标签片 | **不变** | **不变** |
| 与该节点相连的箭头 | **不变**（由拓扑决定） | **不变** |

`C_light` = 同一色值提亮约 15% 以保证深色模式对比度（例如 `#b85450` → `#d97a78`）。

### 4.2 按步骤 `color`

把步骤头部标签片的填充替换为 `rgba(C, 0.20)`，编号文字填充替换为 `C`。图例中对应的步骤条目使用相同颜色。

### 4.3 按泳道 `color`

把泳道条纹底色替换为 `rgba(C, 0.04)`，泳道标签文字填充替换为 `C`。克制使用：泳道底色很容易用过量。

### 4.4 规则

- **焦点节点/焦点步骤上绝不用。**accent 已经承载该信号；焦点元素上的 `color` 会被忽略。
- **箭头上绝不用。**箭头由拓扑决定。想要彩色边，就从 §3 选另一种 `style`，不要用颜色覆盖。
- 每张图**最多 3 个自定义配色元素**（节点 + 泳道 + 步骤合计），焦点对（焦点节点 + 焦点步骤头部）不计入。超过 3 个，视觉信号就开始碎片化。
- 无论组件是什么 `color`，**副标题与工具标签保持 muted**。

### 4.5 语义调色板（推荐）

与 `type-high-level.md`、`type-dp-integration.md`、`type-data-flow.md` 相同的调色板：

- `#b85450` 铁锈红：安全 / 身份 / 治理（访问控制、培训、审批）
- `#5a7d9a` 石板蓝：可观测性 / 质量（数据质量门禁、校验、监控）
- `#7a8c47` 橄榄绿：数据产品 / 发布（可直接消费的产出、release）
- `#8c6d3f` 暖棕：备份 / 灾备 / 归档

---

## 5. 焦点规则

过程图有三个焦点槽位，每个恰好填一项：

- **一个焦点步骤**（`steps[j].focal: true`）：通常是分析或决策的转折点（Test、Approve、Validate）。头部标签片与图例标签片以 accent 渲染。
- **一个焦点节点**（`nodes[i].focal: true`）：*接收*关键交接的节点。accent 描边 + accent 角色徽章 + ink 标题（标题文字保持 ink 以保证可读；只有描边与角色徽章承载 accent）。
- **一组焦点箭头**（`style: focal-in` 与 `focal-out`）：进出焦点节点的边。accent 实线描边。

任一焦点槽位声明了零个或超过一个，就停下来询问用户。

---

## 6. 深色模式

`paper`、`ink`、`muted`、`soft` 与 `accent` 随皮肤反转：取值来自 [`style-guide.md`](style-guide.md) 的深色列。本参考中每个派生值都是**某个不透明度下的角色**，因此大多无需深色模式处理：`ink @ 0.12` 在浅色纸面上解析为深墨色，在深色纸面上解析为浅墨色。

只有以下几项在两种模式间不同，且只差在不透明度：

| 元素 | 浅色 | 深色 | 为何不同 |
|---|---|---|---|
| 泳道底色 | `ink @ 0.018` | `ink @ 0.025` | 淡涂层在深色纸面上需要略高的存在感 |
| 标签列分隔线 | `ink @ 0.20` | `ink @ 0.22` | 同上 |
| 焦点标签片填充 | `accent @ 0.20` | `accent @ 0.22` | 同上 |
| 焦点节点填充 | `accent @ 0.08` | `accent @ 0.12` | 同上 |
| 默认节点填充 | `#ffffff`（白） | `ink @ 0.04` | 白色不透明；深色纸面上改为让节点从底面上浮起 |
| 默认节点描边 | `ink @ 0.25` | `ink @ 0.20` | 同等不透明度下，浅墨在深色纸面上视觉更强 |

跨模式不变：圆点纹理 `ink @ 0.10`、分隔线 `ink @ 0.12`、默认标签片填充 `ink @ 0.12`、焦点节点描边 `accent`，以及自定义组件颜色（`C` 浅色 → `C_light`，提亮约 15%）。

---

## 7. 可复现性检查清单（品味门禁）

输出 SVG 前，逐条核对**每一项**：

1. `viewBox = "0 0 {viewBox_w} {viewBox_h}"` 按 §2 推导。
2. 头部条带位于 `y=0..36`；图例条带位于 `y=legend_y_top..viewBox_h`（`legend_y_top = 36 + n_lanes * 80`）。
3. 每个节点位于 `(step_cx(j) - 50, lane_y_top(k) + 8)`，尺寸 `100×64`。
4. 空单元格不渲染任何内容：无占位矩形、无文字。
5. 恰好**一个**焦点步骤（`steps[j].focal: true`）。
6. 恰好**一个**焦点节点（`nodes[i].focal: true`）。
7. 接触焦点的箭头使用 `style: focal-in` / `focal-out`（accent）。
8. 其余箭头为 `style: normal`（muted 实线）或 `style: trigger`（muted 虚线）。默认不带标签。
9. 所有箭头先于任何节点矩形输出（z-order 规则）。
10. 只允许单折直角布线：右侧出、顶部/底部进。无斜线。每个折弯处 Q 贝塞尔 `r=8`。
11. 自定义组件颜色 ≤ 3（焦点对不计入）。箭头绝不会被组件 `color` 改色。
12. 无论组件是什么 `color`，副标题与工具标签保持 muted。第一步节点省略输入标签片，最后一步节点省略输出标签片。

---

## 8. 数据类型标签片参考（输入 + 输出）

目录与 `type-data-flow.md` §8 相同。

- **输入标签片**位于 `(node_x+4, node_y+54)`，即左**下**角。进入节点的载荷。
- **输出标签片**位于 `(node_x+80, node_y+54)`，即右**下**角。离开节点的载荷。
- 两个标签片都可以省略（第一步/最后一步、载荷未知）。

### 标签片代码

| 代码 | 颜色（浅色） | 颜色（深色） | 含义 |
|------|---------------|--------------|---------|
| `LS` | `#7c8f6f` 鼠尾草绿 | `#9caf8f` | 清单 / 分派 / 任务 |
| `DB` | `#5e7a9b` 灰蓝 | `#82a0c0` | 数据集 / 表格记录 |
| `TB` | `#b8915a` 芥末黄 | `#d3ad7a` | 表（可直接分析） |
| `FL` | `#9c6b50` 锈棕 | `#b88670` | 文件 / 文档 / 报告 |
| `WB` | `#6e6479` 石板灰 | `#8d8298` | 网页 / 新闻稿 / 公开发布 |
| N/A | 完全省略标签片 | — | 未知或不适用 |

标签片内文字：白色，字号 5，weight 700，等宽。

数据类型标签片的颜色与按节点颜色覆盖（§4）是**两条独立的语义轴**。标签片颜色描述*载荷格式*；节点颜色描述*关注点类型*。一个节点可以同时有 `out: TB` 的芥末黄标签片和铁锈红描边。

---

## 9. 图例（3 或 4 行条带）

每行由位于 `x = label_col_w + 4`（= 144）的类别标签开头。默认图例有 **3 行**（`STEPS` / `DATA TYPE` / `FLOW`）；当有一个或多个节点带 `color` 覆盖（§4）时，增加第 4 行 `CONCERN`，并把 `legend_h` 增至 100。

- **第 1 行 `STEPS`**，位于 `y = legend_y_top + 16`：重复头部标签片及其标签。焦点步骤保持 accent 填充。
- **第 2 行 `DATA TYPE`**，位于 `y = legend_y_top + 37`：图中实际用到的每种标签片类型各一个色块。用 muted 等宽小字补充提示：`left chip = input · right chip = output`。
- **第 3 行 `CONCERN`**（仅当存在颜色覆盖时），位于 `y = legend_y_top + 58`：每个用到的自定义颜色一个 mini 矩形，附其语义标签。
- **第 4 行 `FLOW`**（位置取决于是否存在 `CONCERN` 行）：实际用到的每种箭头样式一段示例，带 marker 与标签。

---

## 10. 复杂度预算

| 维度 | 上限 |
|---|---|
| 泳道（参与者） | 6 |
| 步骤 | 12 |
| 每泳道节点数 | 节点 = 仅有实际动作的步骤，空单元格不可见 |
| 带标签的箭头 | 默认 0（仅为非步骤概念加标签） |
| 每节点数据类型标签片 | 2（输入 + 输出） |
| 自定义配色元素（§4） | 3（焦点节点 + 焦点步骤之外） |

超过 6 条泳道或 12 个步骤：拆成两张图（总览 + 细节）。

---

## 11. 反模式

- **给空单元格放占位**：参与者不参与某步骤时，让单元格留空（无框、无文字）。
- **斜箭头**：每条连线必须恰好一个直角折弯。不同泳道节点之间不允许直线直连。
- **纵向为主的箭头从左/右端口进入**：永远右侧出、顶部或底部进。
- **多于一个焦点步骤/焦点节点**：只选最关键的那一个操作。
- **泳道无标签**：每条泳道都必须标明其参与者。
- **所有箭头一种样式**：编排触发必须是虚线，以区别于数据流连线。
- **焦点元素上的 `color` 覆盖**：会被忽略。accent 永远优先。
- **自定义配色的箭头**：连线由拓扑决定；节点上的 `color` 绝不会扩散到它的边。
- **泳道底色滥用**：每条泳道都染色就成了装饰而非信号。最多染 1 条泳道。
- **双行名称节点里放数据类型标签片**：省略标签片，或把名称缩到一行。
- **超过 12 个步骤还不拆分**：使用总览 + 细节两张图。

---

## 12. 完整示例：扩展过程变体的完整 YAML

以下输入块描述了一个带自定义颜色与泳道的扩展过程工作流。渲染出的 SVG 中每个坐标都可由该块经 §2 + §3 + §4 推导，端到端演示参数化布局契约。

```yaml
# Quarterly survey — end-to-end workflow (extended variant)
# 6 lanes × 11 steps, 1 focal step + 1 focal node + 3 custom-colored nodes

lanes:
  - { name: ["RD&E"],                 key: "RDE" }
  - { name: ["IT"],                   key: "IT"  }
  - { name: ["FIELD", "SERVICES"],    key: "FLD" }
  - { name: ["SURVEY", "SERVICES"],   key: "SVY" }
  - { name: ["HOUSEHOLD", "UNIT"],    key: "HHU" }
  - { name: ["COMMS &", "MARKETING"], key: "CMM" }

steps:
  - { number: "1",  label: "Design"   }
  - { number: "2",  label: "Assign"   }
  - { number: "3",  label: "Collect",  focal: true }    # focal step header chip
  - { number: "4",  label: "Review"   }
  - { number: "5",  label: "Validate" }
  - { number: "6",  label: "Weight"   }
  - { number: "7",  label: "Clean"    }
  - { number: "8",  label: "Tabulate" }
  - { number: "9",  label: "Approve"  }
  - { number: "10", label: "Publish"  }
  - { number: "11", label: "Upload"   }

nodes:
  - { lane: "RDE", step: 0,  title: "Sample Design",     sub: "Census data → Sample",
      tool: "SAS · Survey Solutions",      chips: {in: null, out: "LS"} }                # first step: no input chip
  - { lane: "IT",  step: 1,  title: "Field Assignment",  sub: "Sample → Field tasks",
      tool: "Survey Solutions",            chips: {in: "LS", out: "LS"} }
  - { lane: "FLD", step: 2,  title: "Data Collection",   sub: "→ 10,464 dwellings",
      tool: "Survey Solutions",            chips: {in: "LS", out: "DB"},  focal: true }   # focal node
  - { lane: "SVY", step: 3,  title: "HQ Review",         sub: "Submissions → Approved",
      tool: "Survey Sol. HQ",              chips: {in: "DB", out: "DB"},  color: "#b85450" }   # rust-red · governance
  - { lane: "IT",  step: 4,  title: "Error Checks",      sub: "Approved → Cleaned",
      tool: "SAS · Scripts",               chips: {in: "DB", out: "DB"},  color: "#5a7d9a" }   # slate-blue · data quality
  - { lane: "RDE", step: 5,  title: "Weight Calculation", sub: "Cleaned → Weighted",
      tool: "SAS",                         chips: null }                                  # 2-line title — chips skipped
  - { lane: "HHU", step: 6,  title: "2° Cleaning",       sub: "Weighted → Analysis",
      tool: "SAS · R · SPSS",              chips: {in: "DB", out: "TB"} }
  - { lane: "HHU", step: 7,  title: "Tables + Brief",    sub: "Analysis → Tables",
      tool: "Excel · SAS",                 chips: {in: "TB", out: "FL"} }
  - { lane: "CMM", step: 8,  title: "Stats Review",      sub: "Tables → Approved",
      tool: "Internal review",             chips: {in: "FL", out: "FL"} }
  - { lane: "CMM", step: 9,  title: "Public Release",    sub: "Approved → Public",
      tool: "Press conference",            chips: {in: "FL", out: "WB"}, color: "#7a8c47" }   # olive-green · data products
  - { lane: "IT",  step: 10, title: "Upload NatStat / SDMX", sub: "Results → Published",
      tool: "Web · SDMX API",              chips: null }                                  # 2-line title — chips skipped

arrows:
  - { from: {lane: "RDE", step: 0}, to: {lane: "IT",  step: 1},  style: "normal"    }
  - { from: {lane: "IT",  step: 1}, to: {lane: "FLD", step: 2},  style: "focal-in"  }     # → focal
  - { from: {lane: "FLD", step: 2}, to: {lane: "SVY", step: 3},  style: "focal-out" }     # ← focal
  - { from: {lane: "SVY", step: 3}, to: {lane: "IT",  step: 4},  style: "normal"    }     # upward
  - { from: {lane: "IT",  step: 4}, to: {lane: "RDE", step: 5},  style: "normal"    }     # upward
  - { from: {lane: "RDE", step: 5}, to: {lane: "HHU", step: 6},  style: "normal"    }     # downward, skips 2 lanes
  - { from: {lane: "HHU", step: 6}, to: {lane: "HHU", step: 7},  style: "normal"    }     # same lane
  - { from: {lane: "HHU", step: 7}, to: {lane: "CMM", step: 8},  style: "normal"    }
  - { from: {lane: "CMM", step: 8}, to: {lane: "CMM", step: 9},  style: "normal"    }     # same lane
  - { from: {lane: "CMM", step: 9}, to: {lane: "IT",  step: 10}, style: "normal"    }     # upward, skips 4 lanes

dark: false
```

### 12.1 这份 YAML 验证了什么

用这些输入运行本参考的 §2：

- `n_lanes = 6`、`n_steps = 11`、`has_color_row = true`（3 个节点带 `color`）。
- `viewBox_w = 140 + 11 * 112 + 28 = 1400`。✓
- `legend_h = 100`，`viewBox_h = 36 + 6 * 80 + 100 = 616`。✓
- 泳道 y_top = [36, 116, 196, 276, 356, 436]；泳道中点 = [76, 156, 236, 316, 396, 476]。✓
- 步骤 cx = [198, 310, 422, 534, 646, 758, 870, 982, 1094, 1208, 1320]（内容区 8px 边距使每个值比 `140 + j*112 + 50` 偏移 8）。✓
- 节点 4（HQ Review）：step=3，lane="SVY"（k=3）→ x = 534-50 = 484，y = 276+8 = 284。✓
- 节点 5（Error Checks）：step=4，lane="IT"（k=1）→ x = 646-50 = 596，y = 116+8 = 124。✓
- 节点 10（Public Release）：step=9，lane="CMM"（k=5）→ x = 1208-50 = 1158，y = 436+8 = 444。✓

从这份 YAML 重新生成时，坐标直接由公式得出，无需手动微调。

### 12.2 把这份 YAML 改造成其他过程

要记录另一个过程，只需修改以下输入的值：

- **泳道**：把 `lanes[k].name` 改成你的团队名，并同步更新各 `nodes[i].lane`。最多 6 条泳道。
- **步骤**：重命名 `steps[j].label`，把 `focal: true` 移到定义本图核心论点的那一步。最多 12 个步骤。
- **节点**：每个有工作的 `(lane, step)` 单元格写一条条目。留空的单元格（不写条目）不渲染任何内容。
- **颜色**：最多给 3 个节点选 `color: "#hex"`（§4 上限）。除非品牌要求，否则坚持推荐调色板。
- **箭头**：每条边都显式声明，`style: normal | focal-in | focal-out | trigger`。布线规则（§3.1）负责补全几何。

其余一切都是可推导的：viewBox 尺寸、标签片位置、图例布局、深色模式 token 切换。YAML 是**唯一事实来源**；SVG 只是它众多可能渲染中的一种（浅色/深色/full 都由相同输入配不同样式 token 推导）。

---

## 13. 示例

- `assets/example-process.html`：极简浅色版（季度调查：11 步、6 部门、数据类型标签片）。画廊默认。
- `assets/example-process-dark.html`：同上，深色皮肤。
- `assets/example-process-full.html`：同上，编辑卡片边框。
