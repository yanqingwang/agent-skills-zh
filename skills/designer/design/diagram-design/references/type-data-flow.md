> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-data-flow.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 数据流图（Data Flow）

**最适用于：** 可视化数据如何*跨越组织角色*在管道中流动：谁发起、谁处理、谁发布、谁消费。典型用例是多角色的数据平台（Admin → Engineers → Scientists → Consumers），带 4–6 个流程步骤。当读者需要理解**每个阶段谁做什么**，而不只是技术组件时使用。

跨职能业务流程（HR 审批、支持工单）请选标准 **Swimlane**。主题是带类型化载荷（原始文件、表、报表）与角色级访问边界的数据管道时，用 **Data flow**。

本类型是**参数化的**：§1 的输入 schema 通过 §2 的公式驱动每个坐标。同一份输入的两次生成必须产出视觉上完全一致的 SVG。

---

## 1. 输入：参数契约

```yaml
lanes:                              # 1..4 horizontal swimlanes (top to bottom)
  - { name: ["DATA", "ADMINS"],     key: "ADM" }
  - { name: ["DATA", "ENGINEERS"],  key: "ENG" }
  - { name: ["DATA", "SCIENTISTS"], key: "SCI" }
  - { name: ["DATA", "CONSUMERS"],  key: "CON" }

steps:                              # 1..6 columns (left to right)
  - { number: "01", label: "COLLECT" }
  - { number: "02", label: "STORE" }
  - { number: "03", label: "TRANSFORM" }
  - { number: "04", label: "ANALYZE",  focal: true }   # focal step header chip — accent fill
  - { number: "05", label: "PUBLISH" }

nodes:                              # explicit per-cell entries; empty cells render nothing
  - { lane: "ADM", step: 0, title: "Project Setup",   sub: "create · assign roles",     tool: "Platform console" }
  - { lane: "ADM", step: 1, title: "Access Control",  sub: "bucket policies · LDAP",    tool: "MinIO · LDAP console",
      color: "#b85450" }            # tinted rust-red to flag governance/identity concern
  - { lane: "ENG", step: 0, title: "Source Ingest",   sub: "ext. sources → raw",        tool: "NiFi · API · SFTP",
      chips: {in: "WB", out: "DB"} }                    # web payload in, dataset out
  - { lane: "ENG", step: 1, title: "Raw Store",       sub: "raw landing zones",         tool: "MinIO raw",
      chips: {in: "DB", out: "DB"} }                    # raw stays raw inside the landing zone
  - { lane: "ENG", step: 2, title: "Clean & Stage",   sub: "raw → staging → anon",      tool: "NiFi · Trino",
      chips: {in: "DB", out: "TB"} }                    # raw dataset → analysis-ready table
  - { lane: "SCI", step: 3, title: "Explore & Model", sub: "anon data → insights",      tool: "JupyterHub · Trino",
      chips: {in: "TB", out: "FL"}, focal: true }       # focal — table in, file/report out
  - { lane: "SCI", step: 4, title: "Publish Findings", sub: "models → dashboards",      tool: "Superset · Reports",
      chips: {in: "FL", out: "FL"} }                    # report in, report out (pass-through to publish)
  - { lane: "CON", step: 4, title: "Query Insights",   sub: "aggregated views",         tool: "Trino (read-only)",
      chips: {in: "TB", out: "TB"} }                    # consumers read tables, hand off tables

arrows:                             # explicit edges; styles bind to topology (see §3)
  - { from: {lane: "ADM", step: 0}, to: {lane: "ADM", step: 1}, style: "muted" }
  - { from: {lane: "ADM", step: 0}, to: {lane: "ENG", step: 0}, style: "trigger" }   # dashed governance
  - { from: {lane: "ADM", step: 1}, to: {lane: "ENG", step: 1}, style: "trigger" }
  - { from: {lane: "ENG", step: 0}, to: {lane: "ENG", step: 1}, style: "muted" }
  - { from: {lane: "ENG", step: 1}, to: {lane: "ENG", step: 2}, style: "muted" }
  - { from: {lane: "ENG", step: 2}, to: {lane: "SCI", step: 3}, style: "accent",     # focal cross-role
      label: "anon data" }
  - { from: {lane: "SCI", step: 3}, to: {lane: "SCI", step: 4}, style: "muted" }
  - { from: {lane: "SCI", step: 4}, to: {lane: "CON", step: 4}, style: "link" }     # teal: published

dark: false
```

**保留字段语义：**
- `lanes[k].key` — 3 字母角色徽章文本（如 `ADM`、`ENG`、`SCI`、`CON`）。用于该泳道内每个节点。
- `lanes[k].name` — 两行泳道标签；两行都用大写 `eyebrow` 角色。
- `steps[j].focal: true` — 恰好**一个**步骤可声明此项。页眉徽章以 accent 渲染。
- `nodes[i].focal: true` — 恰好**一个**节点可声明此项。以 accent 边框渲染（§5）。
- `nodes[i].chips` — 节点的数据类型徽章。两种形式都接受：
  - **对象形式（推荐）：** `{in: "<CODE>", out: "<CODE>"}` — 显式的输入/输出语义。任一侧可省略。
  - **数组形式：** `["<INPUT_CODE>", "<OUTPUT_CODE>"]` — 第一项是输入，第二项是输出。
  - 代码取自 §8（`WB`、`DB`、`TB`、`FL`、`LS`）。位置**固定**：输入徽章在节点底部**左**侧，输出徽章在底部**右**侧。
- `nodes[i].color` — 可选的**逐节点颜色覆盖**。接受任何合法的 `"#hex"` 字符串；建议用 §4 调色板保持跨图一致，但不是必须。每个节点都可独立携带自己的颜色。

---

## 2. 布局公式：确定性几何

```
label_col_w      = 140
step_slot_w      = 112
right_pad        = 28
n_steps          = len(steps)
n_lanes          = len(lanes)

# Canvas
viewBox_w        = label_col_w + n_steps * step_slot_w + right_pad   # 5 steps → 728
header_h         = 36
lane_h           = 80
has_color_row    = any(node.color or step.color or lane.color in inputs)
legend_h         = 100 if has_color_row else 80                      # 4 rows when colors are present
viewBox_h        = header_h + n_lanes * lane_h + legend_h            # 4 lanes, no colors → 436; with colors → 456

# Header strip (top)
header_y         = 0                                                  # ends at header_h = 36
step_chip_y      = 6                                                  # 16-px chip at y=6..22
step_label_y     = 29                                                 # text line below chip

# Lane positions
lane_y_top(k)    = header_h + k * lane_h                              # 36, 116, 196, 276
lane_y_mid(k)    = lane_y_top(k) + lane_h/2                           # 76, 156, 236, 316
lane_label_x     = label_col_w / 2                                    # 70

# Step / node center x
step_cx(j)       = label_col_w + j * step_slot_w + step_slot_w/2      # 196, 308, 420, 532, 644

# Nodes
node_w           = 100
node_h           = 64
node_x(j)        = step_cx(j) - node_w/2                              # 146, 258, 370, 482, 594
node_y(k)        = lane_y_top(k) + 8                                  # 44, 124, 204, 284

# Legend strip (bottom)
legend_y_top     = header_h + n_lanes * lane_h                        # 356
legend_row_y     = [legend_y_top + 16, legend_y_top + 37, legend_y_top + 59]
                                                                      # 372, 393, 415
```

### 2.1 背景结构

- 整个 viewBox 铺纸底。
- 点阵：22×22 网格，`circle r=0.8`，`fill ink @ 0.10`。
- 交替泳道淡染：奇数索引泳道（0、2、…）获得 `ink @ 0.018` 填充。
- 泳道分隔线：在每条 `lane_y_top(k)` 与 `legend_y_top` 处的水平发丝线，描边 `ink @ 0.12` 宽 0.8。
- 标签列右边框：`x = label_col_w` 处的垂直发丝线，从 `y = header_h` 到 `y = legend_y_top`。

### 2.2 步骤页眉徽章

每个步骤 `j`：

```
chip_x(j)        = step_cx(j) - 16        # 16×16 chip
chip_y           = 6
chip_w           = 32
chip_h           = 16
chip_rx          = 8                       # pill-shaped
number_anchor    = (step_cx(j), 14)
label_anchor     = (step_cx(j), 29)
```

默认填充：`ink @ 0.12`，编号文本 ink，标签文本 muted。
焦点填充：`accent @ 0.20`，编号与标签文本 accent。
逐步骤 `color` 覆盖（§4）：填充替换为 `rgba(C, 0.20)`，文本填充替换为 `C`。

### 2.3 泳道标签

两行 `eyebrow` 角色标签，两行都大写，填充 muted：
- 第 1 行在 `(lane_label_x, lane_y_mid(k) - 4)`
- 第 2 行在 `(lane_label_x, lane_y_mid(k) + 8)`

逐泳道 `color` 覆盖（§4）：标签填充替换为 `C`，泳道淡染替换为 `rgba(C, 0.04)`（替代默认的 `ink @ 0.018`）。

### 2.4 节点内容布局（100×64 矩形内）

```
role_chip          rect 18×10 at (node_x+4, node_y+4),  rx=3
role_chip_text     centered at (node_x+13, node_y+9), eyebrow role, font-size=6, weight=600
title              centered at (step_cx(j), node_y+23), node-name role, font-size=9
sub                centered at (step_cx(j), node_y+35), sublabel role, font-size=6.5, muted
tool               centered at (step_cx(j), node_y+47), sublabel role, font-size=6.5, soft
data chip IN       rect 16×8 at (node_x+4,   node_y+54), rx=3      # payload type entering the node
data chip OUT      rect 16×8 at (node_x+80,  node_y+54), rx=3      # payload type leaving the node
```

空格子（无节点条目）**什么都不渲染**。没有占位矩形、没有角色徽章、没有标签：该格不可见。

---

## 3. 箭头规则（强制）

四种样式，绑定拓扑。连接线画在**所有**节点矩形**之前**（Z 顺序规则）。

| `style` | 描边 | 宽度 | 虚线 | 标记 | 何时必须使用 |
|---|---|---|---|---|---|
| `muted` | `muted` | 1.0 | — | `arr-muted` | 步骤之间或泳道之内的标准数据交接。 |
| `trigger` | `muted` | 1.0 | `4,3` | `arr-muted` | 治理触发：一个管理员动作让下游工作得以进行。不加标签。 |
| `accent` | `accent` | 1.2 | — | `arr-accent` | 焦点跨角色交接。**每图恰好一条**，带标签。 |
| `link` | `link` | 1.0 | — | `arr-link` | 已发布 / 被外部消费的输出。 |

**Defs 块**（必需，三个标记）：

```svg
<defs>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="11" cy="11" r="0.8" fill="{ink @ 0.10}"/>
  </pattern>
  <marker id="arr-muted"  markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{muted}"/></marker>
  <marker id="arr-accent" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{accent}"/></marker>
  <marker id="arr-link"   markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{link}"/></marker>
</defs>
```

### 3.1 走线规则（不可协商）

- **单拐弯走线**：先水平后垂直。从节点**右边缘**出边；从**左侧**（同泳道水平）或**顶部/底部**（跨泳道垂直）入边。
- **不用对角线。** 拐弯用 8px 的 Q 贝塞尔角。
- **同步骤跨泳道（垂直）**：直接在 `(step_cx(j), lane_y_top(k_to)−12)` 与 `(step_cx(j), lane_y_top(k_to))` 之间连线。用于同一步骤下的 admin → engineers 触发。
- **跨泳道跨步骤（焦点）**：向右出边，水平越过源节点右边缘，行进到目标步骤之前的走廊 x，再垂直下落。
- **标签：** 只有 `accent` 箭头带标签。文本后 6px 处用纸色填充矩形遮罩（不透明）。其他箭头不加标签。
- **Z 顺序：** 所有箭头先于任何节点矩形输出（矩形填充遮住节点内部的线端）。

---

## 4. 组件颜色覆盖

任何节点、泳道或步骤都可声明可选的 `color: "#hex"`。与 high-level §3.4 和 dp-integration §4 一致，规则在各类型间读法相同。

### 4.1 逐节点 `color`

施加于：

| 元素 | 浅色 | 暗色 |
|---|---|---|
| 容器填充（`rect`） | `rgba(C, 0.06)` | `rgba(C_light, 0.10)` |
| 容器描边 | `rgba(C, 0.35)`（描边宽度 1） | `rgba(C_light, 0.45)` |
| 角色徽章填充 | `rgba(C, 0.18)` | `rgba(C_light, 0.22)` |
| 角色徽章文本 | `C` | `C_light` |
| 标题文本 | `C` | `C_light` |
| 子标签 | **不变**（muted） | **不变**（muted） |
| 工具标签 | **不变**（soft） | **不变**（soft） |
| 数据类型徽章 | **不变** | **不变** |
| 触及该节点的箭头 | **不变**，由拓扑决定 | **不变** |

`C_light` = 同一十六进制色提亮约 15% 以保证暗色对比（如 `#b85450` → `#d97a78`）。

### 4.2 逐步骤 `color`

把步骤页眉徽章的填充替换为 `rgba(C, 0.20)`，徽章的编号 + 标签文本填充替换为 `C`。图例中对应的步骤条目使用相同颜色。

### 4.3 逐泳道 `color`

把泳道条纹淡染替换为 `rgba(C, 0.04)`（仅适用于默认获得淡染的奇数索引泳道；显式选择时也可扩展到所有泳道），并把泳道标签文本填充替换为 `C`。节制使用；泳道淡染容易用过头。

### 4.4 规则

- **绝不用于焦点节点 / 焦点步骤。** accent 已承载该信号。焦点元素上的 `color` 被忽略。
- **绝不用于箭头。** 箭头由拓扑决定。想要彩色边线，从 §3 选一个不同的 `style`，而不是颜色覆盖。
- **每图自定义着色元素上限 3 个**（节点 + 泳道 + 步骤合计），焦点对（焦点节点 + 焦点步骤页眉）之外。超过 3 个，视觉信号开始碎片化：还需要更多就拆图，或者重新想想每种颜色是否承载了不同的含义。
- **副标题与工具标签保持 muted。** 只有主身份（边框 + 角色徽章 + 标题 + 图标）承载颜色信号。

### 4.5 语义调色板（推荐）

与 high-level / dp-integration 相同的调色板，让读者扫过多张图时，同一颜色始终意味着同一件事：

- `#b85450` 铁锈红：安全 / 身份 / 治理（管理员节点、LDAP、访问控制）
- `#5a7d9a` 石板蓝：可观测性 / 质量（监控、数据质量门、血缘）
- `#7a8c47` 橄榄绿：治理 / 血缘（catalog、元数据）
- `#8c6d3f` 暖棕：备份 / 灾备 / 归档

---

## 5. 焦点规则

数据流图围绕**一个跨角色交接**构建，它承载全图的核心主张。三个焦点槽位，各恰好一个条目：

- **一个焦点步骤**（`steps[j].focal: true`）：通常是分析枢纽（Analyze、Model 等）。页眉徽章与图例徽章都以 accent 渲染。
- **一个焦点节点**（`nodes[i].focal: true`）：*接收*焦点交接的节点。accent 边框 + accent 角色徽章 + ink 标题。
- **一条焦点箭头**（`arrows[i].style: "accent"`）：进入焦点节点的跨角色交接。实心 accent 描边 + 带一个简短载荷描述的标签（如 `anon data`）。

任一焦点槽位声明了 0 个或多于 1 个条目时，停下询问用户。

---

## 6. 暗色模式

| Token | 浅色 | 暗色 |
|---|---|---|
| Paper | `paper` | `ink` |
| Ink | `ink` | `paper` |
| Muted | `muted` | `soft` |
| Soft | `soft` | `rule-solid` |
| Accent | `accent` | `accent` |
| Link | `link` | `link` |
| 点阵 | `ink @ 0.10` | `paper @ 0.10` |
| 泳道淡染 | `ink @ 0.018` | `paper @ 0.025` |
| 分隔线 | `ink @ 0.12` | `paper @ 0.12` |
| 默认徽章填充 | `ink @ 0.12` | `paper @ 0.12` |
| 焦点徽章填充 | `accent @ 0.20` | `accent @ 0.22` |
| 默认节点填充 | `paper` | `paper @ 0.04` |
| 默认节点描边 | `ink @ 0.25` | `paper @ 0.20` |
| 焦点节点填充 | `accent @ 0.07` | `accent @ 0.12` |
| 焦点节点描边 | `accent` | `accent` |
| 自定义组件颜色 | `C` | `C_light`（提亮约 15%） |

---

## 7. 可复现清单（品味门槛）

输出 SVG 前，逐项核验：

1. `viewBox = "0 0 {viewBox_w} {viewBox_h}"`，由 `n_steps` 与 `n_lanes` 经 §2 推导。
2. 页眉条在 `y=0..36`；图例条在 `y=legend_y_top..viewBox_h`（`legend_y_top = 36 + n_lanes * 80`）。
3. 每个节点位于 `(step_cx(j) - 50, lane_y_top(k) + 8)`，尺寸 `100×64`。
4. 空格子什么都不渲染：没有占位矩形，没有文本。
5. 恰好**一个**焦点步骤（`steps[j].focal: true`）。
6. 恰好**一个**焦点节点（`nodes[i].focal: true`）。
7. 恰好**一条**焦点箭头（`style: accent`）。带标签，标签后有纸色遮罩矩形。
8. 其他所有箭头不加标签。
9. 所有箭头先于任何节点矩形输出（Z 顺序规则）。
10. 只允许单拐弯走线：不用对角线。每个拐弯用 Q 贝塞尔 `r=8`。
11. 自定义组件颜色 ≤ 3（焦点对之外）。箭头绝不因组件 `color` 而改色。
12. 副标题与工具标签保持 muted，无论任何组件 `color`。

---

## 8. 数据类型徽章参考（输入 + 输出）

每个节点底部的小 `16×8 rx=3` 徽章，输入一个、输出一个。位置**不可协商**：

- **输入徽章**在 `(node_x+4, node_y+54)` — 节点底部**左**侧。表示从上游*进入*节点的载荷格式。
- **输出徽章**在 `(node_x+80, node_y+54)` — 节点底部**右**侧。表示离开节点*流向*下游的载荷格式。

任一徽章都可省略（如汇点只有输入徽章；纯源节点只有输出徽章）。读图因此变成一次载荷变换追踪：扫一行，读每个节点的输入 → 输出，你就能确切看到每次交接时数据是什么形状。

### 徽章代码

| 代码 | 颜色 | 含义 |
|------|-------|---------|
| `WB` | `#6e6479`（紫褐） | Web / 公开数据 |
| `DB` | `#5e7a9b`（钢蓝） | 数据集 / 原始文件 |
| `TB` | `#b8915a`（琥珀） | 表 / 可直接分析 |
| `FL` | `#9c6b50`（赭色 sienna） | 文件 / 报表 / 导出 |
| `LS` | `#4a7c59`（森林绿） | 实时流 / 事件 |

徽章内文本：白色，`eyebrow` 角色，5px，字重 700。

数据类型徽章颜色是与逐节点颜色覆盖（§4）**相互独立的语义轴**。徽章颜色描述*载荷格式*；节点颜色覆盖描述*关注类型*（治理、可观测性等）。不要混为一谈：一个节点可以同时带 `out: TB` 琥珀徽章和铁锈红边框。

---

## 9. 图例（3 行或 4 行条）

每行由 `x=144` 处的类别标签引出。默认图例有 **3 行**（`STEPS` / `DATA TYPE` / `FLOW`）；当一个或多个节点带 `color` 覆盖（§4）时，加第 4 行 `CONCERN`，并把 `legend_h` 增到 100（于是 `viewBox_h = header_h + n_lanes·80 + 100`）。

- **第 1 行，`STEPS`**，在 `y = legend_y_top + 16`：重复页眉徽章及其标签。焦点步骤保持 accent 填充。
- **第 2 行，`DATA TYPE`**，在 `y = legend_y_top + 37`：图中实际用到的每种徽章类型一个色样。在徽章之后以 muted `sublabel` 角色**附一个小提示**：`left chip = input · right chip = output`。这把基于位置的输入/输出约定对首次读者讲明白。
- **第 3 行，`CONCERN`**（仅当存在颜色覆盖时），在 `y = legend_y_top + 58`：每个用到的自定义颜色一个小矩形，带其语义标签（如 `Identity · Governance`、`Data Quality · Observability`）。焦点 accent 色样也显示在这里，读者能并排看到全部三条颜色轴。
- **第 4 行，`FLOW`**（最后一行，位置取决于有无 `CONCERN` 行）：带标记与文本标签的短线段，实际用到的每种箭头样式一条。

所有图例条目在同一行的单一水平条上对齐。不要在盒内纵向堆叠。

---

## 10. 复杂度预算

| 维度 | 上限 |
|---|---|
| 泳道（角色） | 4 |
| 步骤 | 6 |
| 每泳道节点 | 节点 = 活跃步骤而已：空格不可见（无占位框） |
| 带标签的箭头 | 1（仅焦点 accent） |
| 每节点数据类型徽章 | 2 |
| 自定义着色元素（§4） | 3（焦点节点 + 焦点步骤之外） |

超过 4 条泳道或 6 个步骤：拆成两张图（如摄取管道 / 分析管道）。

---

## 11. 反模式

- **占位空格** — 某角色不参与某步骤时，让该格留空（无框、无文本）。
- **带标签的箭头超过一条** — 只有焦点跨角色交接获得标签。
- **对角箭头** — 一律先水平后垂直；单个直角拐弯。
- **节点标题用 `title` 角色** — 节点标题用 `node-name` 角色（技术语境）。只有页面 `<h1>` 用 `title`。
- **accent 用在超过一个节点、一个步骤、一条箭头上** — 焦点 = 一个节点 + 一个步骤 + 一条箭头，上限。
- **角色标签用 `node-name` 角色** — 泳道标签一律用大写 `eyebrow` 角色（它们是标识符，不是散文）。
- **焦点元素上的 `color` 覆盖** — 被忽略。accent 永远优先。
- **自定义着色的箭头** — 箭头由拓扑决定。节点颜色永不扩散到它的边。
- **泳道淡染用过头** — 每条泳道都染色读起来是装饰，不是信号。最多染 1 条。

---

## 12. 示例

- `assets/example-data-flow.html` — 极简浅色（这个平台，4 角色 × 5 步骤：Admin、Engineers、Scientists、Consumers）。图库默认。
- `assets/example-data-flow-dark.html` — 同一张，暗色皮肤。
- `assets/example-data-flow-full.html` — 同一张，编辑卡片式外框。
