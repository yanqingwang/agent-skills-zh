> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-high-level.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 高层架构图（High-Level）

**最适用于：** 端到端数据栈总览（采集 → 存储 → 查询 → 分析 → 可视化），部署在容器编排器（Kubernetes、ECS、Nomad）上。组合了阶段 V 形横幅（chevron banner）、部署边界、编排条带、身份页脚，以及（可选的）承载横切关注点（Orchestration、Security、Observability）的右侧垂直 V 形条带。

本类型是**参数化的**。整张图完全由一小份输入清单（chevrons、sources、components、connections）决定。下面的公式精确给出在这些输入下每个形状落在哪里：相同输入生成两次，必须产出视觉上完全一致的 SVG。

---

## 1. 输入：参数契约

动笔前，先向用户收集以下内容（或接受一份 YAML/JSON 块）。本参考中的一切都由这些输入推导。不要临场发明几何。

```yaml
chevrons:                       # ordered left → right; reserved names auto-promote to vertical
  - { name: "Data sources",         columns: 1 }
  - { name: "Ingestion",            columns: 1 }
  - { name: "Storage",              columns: 1 }
  - { name: "Transformation",       columns: 1 }
  - { name: "Visualization",        columns: 1 }
  - { name: "Orchestration",        vertical: true }                     # reserved → pairs with the bar
  - { name: "Security",             vertical: true, color: "#b85450" }   # tinted to match the Identity bar below
  - { name: "Observability",        vertical: true }                     # reserved → pairs with crosscut #2

sources:                        # external; rendered in the dashed zone on the left
  - { name: "PostgreSQL", type: "db",     connects_to: ["NiFi"] }
  - { name: "SFTP drop",  type: "ftp",    connects_to: ["NiFi"] }
  - { name: "Web forms",  type: "web",    connects_to: ["NiFi"] }
  - { name: "Legacy",     type: "legacy", connects_to: ["NiFi"] }

components:                     # inside the cluster, plus bars and cross-cutting rows
  - { name: "NiFi",       chevron: "Ingestion",      kind: node,          icon: nifi,     role: "COLL"  }
  - { name: "MinIO",      chevron: "Storage",        kind: node,          icon: minio,    role: "STORE", focal: true }
  - { name: "Trino",      chevron: "Storage",        kind: node,          icon: trino,    role: "VIRT"  }
  - { name: "Notebooks",  chevron: "Transformation", kind: node,          icon: jupyter,  role: "ANLZ"  }
  - { name: "Superset",   chevron: "Visualization",  kind: node,          icon: superset, role: "DASH" }
  - { name: "Airflow",    chevron: "Orchestration",  kind: bar,           icon: airflow,    subtitle: "Apache Airflow" }
  - { name: "Identity",   chevron: "Security",       kind: cross-cutting, icon: keycloak,   subtitle: "Keycloak · LDAP · OIDC",     color: "#b85450" }
  - { name: "Monitoring", chevron: "Observability",  kind: cross-cutting, icon: prometheus, subtitle: "Prometheus · Grafana · Loki" }

connections:                    # explicit edges; focal-touching ones become accent automatically
  - { from: "NiFi",    to: "MinIO",                style: "primary" }
  - { from: "NiFi",    to: "Trino",                style: "secondary" }
  - { from: "MinIO",   to: "Notebooks",            style: "primary" }
  - { from: "Trino",   to: "MinIO",                style: "query" }   # read-back (dashed)
  - { from: "Notebooks", to: "Superset",           style: "secondary" }
  - { from: "Airflow", to: ["NiFi", "Trino", "Notebooks"], style: "trigger" }

focal: "MinIO"                  # exactly one; defaults to first kind=node under "Storage"
dark: false
```

**保留的 chevron 名称**（始终垂直，即使省略 `vertical: true`）：`Orchestration`、`Security`、`Observability`、`Governance`、`Backup`。

**保留的 `kind` 取值：**
- `node`：集群内的标准方框（默认）。
- `bar`：横跨集群顶部的水平条带。通常只有一个（Orchestration）；配对规则见 §5。
- `cross-cutting`：横跨主体宽度（止于右栏留白处）的水平条带，堆叠在集群下方。**允许零个或多个**；每个在其前一个下方 44px 处堆叠（§2.5），并与一条垂直 chevron 1:1 配对（§5）。

**可选 `color`**（按组件，hex 字符串）：给组件的容器与内容着色，连线不受影响。见 §3.4。克制使用：自定义颜色是语义旗标（例如红色 = 安全关注点），不是装饰。

**Source 的 `type` 取值** → 图标映射（使用 `references/primitive-icons.md`）：
- `db` → `database`
- `ftp` → `bucket` 或上传箭头
- `web` → `internet`
- `legacy` → `server`
- `api` → `api`
- `primitive-icons.md` 中的任何显式图标名也都接受。

---

## 2. 布局公式：确定性几何

以下每个坐标都由输入推导。**示例中不允许出现本文没有给出依据的硬编码数字。**

### 2.1 画布

```
has_vertical       = any(c.vertical or c.name in reserved_names for c in chevrons)
right_strip_w      = 28  if has_vertical else 0
strip_margin       = 8   if has_vertical else 0   # gap between body and right strip
effective_w        = 1000 - right_strip_w - strip_margin     # 1000 or 964

n_cross            = count of components with kind == "cross-cutting"
strip_y_bot        = max(428, 388 + n_cross * 44 - 4)        # extends to last crosscut row
viewBox_h          = max(540, strip_y_bot + 112)             # 112 reserved for legend
viewBox            = f"0 0 1000 {viewBox_h}"
```

每个水平元素（chevron 横幅、集群、编排条带、身份/横切条带）都止于 `effective_w`。右侧栏位于 `x = 1000 - right_strip_w`（= 972）。两者之间 8px 的空档是视觉呼吸空间，绝不放内容。

声明了多于一个横切条带时 `viewBox_h` 会增大：1 个 crosscut → 540，2 个 → 600（想紧凑也可以 584；规则会向上取整到 20 的倍数，保证网格干净）。

### 2.2 水平 chevron 横幅

```
y_banner           = 4
h_banner           = 28
horizontals        = [c for c in chevrons if not c.vertical and c.name not in reserved_names]
sum_columns        = sum(c.columns for c in horizontals)
base_unit          = floor_to_4(effective_w / sum_columns)        # multiple of 4
widths             = [max(120, base_unit * c.columns) for c in horizontals]
widths[-1]         += effective_w - sum(widths)                   # trailing absorbs remainder
x_boundaries       = cumulative_sum([0] + widths)                 # length sum_columns+1
chevron_cx(C)      = (x_boundaries[index(C)] + x_boundaries[index(C)+1]) / 2
```

**多边形形状：**
- 第一个（最左）：`(x0,4) (x1-12,4) (x1,18) (x1-12,32) (x0,32)`
- 中间：`(x0,4) (x1-12,4) (x1,18) (x1-12,32) (x0,32) (x0+12,18)`
- 最后（最右）：`(x0,4) (effective_w,4) (effective_w,32) (x0,32) (x0+12,18)`

填充在**阶段色带调色板**（§6.1）的两档之间交替：浅色模式用 `band-1` / `band-2`，深色模式用 `band-2` / `band-3`。标签：`band-label` 填充，`eyebrow` 角色（等宽），`font-size=7`，`letter-spacing=0.14em`，`text-anchor=middle`，居中于 `chevron_cx, 21`。

**颜色覆盖**（按 chevron，水平与垂直皆可）：chevron 可声明可选的 `color: "#hex"`，替换该 chevron 的交替填充。用于标记与自定义配色组件配对的阶段（例如 Identity 条带用了 `color: "#b85450"` 时，`Security` chevron 用红色）。规则：

- 覆盖只作用于多边形填充。标签保持 `band-label`，绝不取当前皮肤的 `paper`。
- 交替序号不移位；相邻 chevron 保持各自自然填充，即使出现两块相邻同色填充也不管。不要去“修正”它：覆盖应当少见（每图 ≤ 2 处）。
- 深色模式下用同一 hex，除非它与 `band-label` 的对比度低于 4.5:1；若低于，就为深色模式选更深的色阶，并在该 chevron 上以 `color_dark` 字段记录。
- chevron 颜色覆盖独立于任何配对组件的颜色，但把两者配套（chevron 与条带用同一 hex）是让这一列在视觉上“读作”同一关注点的惯例做法。

### 2.3 来源区（虚线，外部）

```
sources_x          = 4
sources_y          = 40
sources_w          = x_boundaries[1] - 8           # width of the first chevron, minus 4px gutter each side
sources_h          = 336
```

描边：`ink @ 0.20`，`stroke-width=0.8`，`stroke-dasharray=6,3`，`rx=6`。区域填充：`ink @ 0.02`。

### 2.4 集群边界（实线）

```
cluster_x          = x_boundaries[1] + 4           # starts at end of source zone + 4px gutter
cluster_y          = 40
cluster_w          = effective_w - cluster_x       # extends to right strip / canvas edge
cluster_h          = 336
```

描边：`ink @ 0.18`，`stroke-width=1.2`，`rx=8`。填充：`ink @ 0.02`。K8s 图标与标签位于 `(cluster_x + 16, 352)`（图标）与 `(cluster_x + 40, 362)`（文字）。

### 2.5 横切条带（身份、可观测性等）

零个或多个 `kind: cross-cutting` 组件堆叠在集群下方。每个占一行 40px 高，行间 4px。

```
crosscuts          = [c for c in components if c.kind == "cross-cutting"]   # ordered as declared
cross_x            = 4
cross_y(k)         = 388 + k * 44                  # 388, 432, 476, …
cross_w            = effective_w - 4               # spans body width, stops at the strip margin
cross_h            = 40
```

描边：`ink @ 0.20`，`stroke-width=0.8`，`rx=6`。填充：`ink @ 0.05`。图标位于 `(16, cross_y(k) + 10)`，名称居中于 `(effective_w / 2, cross_y(k) + 22)`，副标题位于 `(effective_w / 2, cross_y(k) + 34)`。

保留的横切*关注点*（仅供参考；实际条带名称用户随意取）：
- **身份 / 安全**：Keycloak、LDAP/AD、Okta、Auth0、OIDC 提供商
- **可观测性**：Prometheus + Grafana、Datadog、OpenTelemetry、Loki
- **备份 / 灾备**：Velero、Restic、快照编排器
- **治理 / 血缘**：OpenMetadata、DataHub、Apache Atlas
- **密钥 / 配置**：Vault、Sealed Secrets、External Secrets

每条横切条带与右侧栏中的一条垂直 chevron 1:1 配对（§5）。

### 2.6 编排条带组件（集群内）

```
bar_x              = cluster_x + 12
bar_y              = 52
bar_w              = cluster_w - 24
bar_h              = 44
```

描边：`ink @ 0.18`，`stroke-width=0.8`，`rx=4`。填充：`ink @ 0.05`。工具图标在最右侧（`bar_x + bar_w - 50, 58`）；名称居中于 `(bar_x + bar_w/2, 71)`；副标题位于 `(bar_x + bar_w/2, 84)`。

### 2.7 组件节点（集群内）

```
node_w             = 152
node_h             = 80                            # focal same height, accent border
node_cx(N)         = chevron_cx(N.chevron)         # ← non-negotiable
node_x(N)          = node_cx(N) - node_w/2
```

若某个 chevron 分配到 K 个节点，纵向堆叠：

```
first_top_y        = 120 if any bar in this column else 64
gap                = 16
row_top(k)         = first_top_y + k * (node_h + gap)   # k = 0..K-1
```

**焦点节点：**`fill="{accent @ 0.08}"`、`stroke="{accent}"`、`stroke-width=1.2`。标题文字用 `accent`。其余节点：白色填充，`stroke={ink @ 0.25}`，`stroke-width=1`。

角色徽章在左上角 `(node_x+8, node_y+6)`，高 12。图标在右上角 `(node_x+node_w-32, node_y+6)`，24×24，经 `currentColor` 单色化。名称居中于 `(node_cx, node_y+44)`，字号 11，sans semibold。副标题位于 `(node_cx, node_y+56)`，字号 8，mono muted。

### 2.8 来源节点（虚线区内）

```
src_node_w         = sources_w - 8
src_node_h         = 64                            # uniform; chosen to fit ≤ 4 sources
src_node_x         = sources_x + 4
src_first_top_y    = 60
src_gap            = 16
src_row_top(k)     = src_first_top_y + k * (src_node_h + src_gap)
```

与集群节点相同的角色徽章 / 图标 / 名称 / 副标题模式（图标位于 `src_node_x+54, row_top(k)+6`；名称居中于 `src_node_x+src_node_w/2, row_top(k)+42`；副标题在其下一行）。角色徽章文字：`EXT`。来源最多 4 个；更多就拆成单独一张图。

### 2.9 右侧栏：垂直 chevron

```
strip_x            = 1000 - right_strip_w       # 972 when present
strip_w            = 28
verticals          = [c for c in chevrons if c.vertical or c.name in reserved_names]
strip_y_top        = 40
strip_y_bot        = max(428, 388 + n_cross * 44 - 4)   # extends to last crosscut row (see §2.1)
strip_h_total      = strip_y_bot - strip_y_top
heights            = [floor_to_4(strip_h_total / len(verticals))] * len(verticals)
heights[-1]       += strip_h_total - sum(heights)       # last absorbs remainder
```

示例：
- 2 条垂直 chevron（Orchestration + Security）、1 个 crosscut → `heights = [192, 196]`，布局 `[40..232, 232..428]`。
- 3 条垂直 chevron（Orchestration + Security + Observability）、2 个 crosscut → `strip_y_bot = 472`、`strip_h_total = 432`、`heights = [144, 144, 144]`，布局 `[40..184, 184..328, 328..472]`。

相邻边界共享同一 y（无缝隙），就像水平 chevron 在边界处共享 x。

**多边形形状**（自上而下，与水平版 §2.2 对应）：
- 第一个（最上）：顶部平直、底端出尖：`(strip_x, y0) (strip_x+strip_w, y0) (strip_x+strip_w, y1-12) (strip_x+strip_w/2, y1) (strip_x, y1-12)`
- 中间：顶部开凹口、底端出尖：`(strip_x, y0) (strip_x+strip_w/2, y0+12) (strip_x+strip_w, y0) (strip_x+strip_w, y1-12) (strip_x+strip_w/2, y1) (strip_x, y1-12)`
- 最后（最下）：顶部开凹口、底部平直：`(strip_x, y0) (strip_x+strip_w/2, y0+12) (strip_x+strip_w, y0) (strip_x+strip_w, y1) (strip_x, y1)`

填充在 `band-1` / `band-2` 之间交替（与水平 chevron 相同的阶段色带调色板，§6.1）。标签：`band-label` 填充，`eyebrow` 角色（等宽），`font-size=7`，`letter-spacing=0.14em`，**旋转 −90°**，锚定于 `(strip_x + strip_w/2, (y0+y1)/2)`。

垂直 chevron 同样遵循 §2.2 的按 chevron `color` 覆盖：hex 用于多边形填充，旋转标签保持 `band-label`。把覆盖与该 chevron 所配对条带/crosscut 上的同一 hex 配套使用，让两者在视觉上绑定为同一关注点。

---

## 3. 连线规则（强制）

以下规则不可妥协。样式**自动**由拓扑决定：不要允许用户覆盖接触焦点或从条带出发的边的样式。

| `style` | 描边 | 宽度 | 虚线 | Marker | 何时必须使用 |
|---|---|---|---|---|---|
| `primary` | `accent` | 1.2 | — | `arrow-accent` | 终点为 `focal` 节点的每条边。 |
| `secondary` | `muted` | 1.0 | — | `arrow` | 两端都不是焦点时，source→component 与 component→component 的默认样式。 |
| `trigger` | `muted` | 1.0 | `4,3` | `arrow-sm` | 从 `kind: bar` 组件出发的每条边。 |
| `query` | `ink @ 0.30` | 1.0 | `4,3` | `arrow` | 回读边（例如 focal ↔ Trino）。 |

**Defs 块**（必需，恰好这四个 marker）：

```svg
<defs>
  <marker id="arrow"        markerWidth="8" markerHeight="6" refX="7" refY="3"   orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{muted}"/></marker>
  <marker id="arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3"   orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{accent}"/></marker>
  <marker id="arrow-sm"     markerWidth="6" markerHeight="5" refX="5" refY="2.5" orient="auto"><polygon points="0 0, 6 2.5, 0 5" fill="{muted}"/></marker>
  <marker id="arrow-dim"    markerWidth="8" markerHeight="6" refX="7" refY="3"   orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{ink @ 0.45}"/></marker>
</defs>
```

### 3.1 出边/入边侧（不可妥协）

| 边类型 | 从源哪一侧出 | 从目标哪一侧进 |
|---|---|---|
| Source → 集群节点 | 源节点的**右侧** | 目标的**左侧** |
| 组件 → 组件（集群内） | **右侧** | **左侧** |
| 条带组件 → 节点 | 条带的**底部** | 节点的**顶部** |
| 横切条带 | —（不发边） | — |
| 垂直 chevron | —（仅标签；不发边） | — |

### 3.2 布线

- 正交肘形折线，每条 path **最多两个折弯**。
- 每个折弯用 8px 的 Q 贝塞尔圆角。
- Z-order：**所有连线先于任何节点矩形绘制**（让节点填充遮住线的端头）。
- 每个 `<path>` / `<line>` 恰好一个 `marker-end`。绝不同时用 `marker-start` 与 `marker-end`。
- 标签：每条 `primary` 与 `secondary` 连线都带标签（小号等宽，背后垫不透明纸面色矩形遮罩）。`trigger` 与 `query` 连线不带标签。

### 3.3 交叉

- 避免。接受交叉之前，先尝试经 chevron 分隔主干（§4）重新布线。
- 若无法避免，后画的 path 在先画的那条之上以 6px 弧线跨越。

### 3.4 组件颜色覆盖

组件可声明可选的 `color: "#hex"`（CSS 颜色字符串）。覆盖**只**重新着色组件的容器与内容，连线绝不改色。边保持 §3 的拓扑驱动样式。

**颜色应用位置**（设 `C = color`）：

| 元素 | 浅色模式 | 深色模式 |
|---|---|---|
| 容器填充（`rect` 主体） | `rgba(C, 0.06)` | `rgba(C, 0.10)` |
| 容器描边 | `rgba(C, 0.35)`（节点 `stroke-width=1`，条带 `0.8`） | `rgba(C, 0.45)` |
| 角色徽章描边（节点） | `rgba(C, 0.40)` | `rgba(C, 0.55)` |
| 角色徽章文字（节点） | `rgba(C, 0.85)` | `rgba(C, 1.0)` |
| 图标填充 / 描边 | `C` | 把 `C` 提亮约 15%（若本身已浅则用 `C`） |
| 名称文字 | `C` | 提亮 `C` |
| 副标题文字 | **不变**（`muted`） | **不变**（`muted`） |
| 与该组件相连的连线 | **不变**（仍由拓扑决定） | **不变** |

副标题保持 muted，因为它是括注性质的元数据；只有主标识（名称 + 图标 + 描边）承载颜色信号。

**规则**：

- **焦点节点上绝不用。**焦点节点已用 accent 着色（§2.7）；焦点节点上的 `color` 会被忽略，accent 优先。
- **来源节点上绝不用。**来源在集群之外，保持中性。
- 每张图**最多 2 个自定义配色组件**（焦点不计入）。三个及以上彩色元素会抹掉信号，与 §1 把 accent 限制在 1–2 个元素是同一个道理。
- **连线不上色。**想要彩色边时，正确做法是从 §3 换一种 `style`，而不是覆盖。

**语义用法**（推荐）：
- `#b85450`（铁锈红）：安全 / 身份（Keycloak、Vault）
- `#5a7d9a`（石板蓝）：可观测性（Prometheus、Datadog）
- `#7a8c47`（橄榄绿）：治理 / 血缘（OpenMetadata）
- `#8c6d3f`（暖棕）：备份 / 灾备

除非用户品牌另有要求，就用这些。给组件随机配 hex 正是本 Skill 要避免的失败模式。

---

## 4. 块分支规则（扇出）

这是可复现性的最大隐患。固定这些规则，图就变得可预测。

### 4.1 来源扇出（一个 source → N 个组件）

```
exit_x   = source.right
trunk_x  = cluster_x - 8                     # 4-px gutter before cluster border
```

每个目标一条路径：`M exit_x,source_cy → H trunk_x → V target_cy → H target.left`。拐角用 Q 贝塞尔。

### 4.2 组件扇出（一个组件 → N 个组件）

```
exit_x   = node.right
trunk_x  = x_boundaries[index(source.chevron) + 1] + 4   # 4 px past the chevron divider
```

每个目标一条路径：`M exit_x,source_cy → H trunk_x → V target_cy → H target.left`。

### 4.3 扇出上限

**每个节点最多 3 条出边。**超过 3 条就引入枢纽（通常是 `focal` 节点）。chevron 横幅就是图例；一个节点若向四个下游扇出，它其实悄悄成了枢纽，把它显式标出来。

### 4.4 条带垂落（Airflow → N 个节点）

```
drop_x(target) = target.cx
drop_y_start   = bar.bottom
drop_y_end     = target.top
```

垂直直线，`style: trigger`。每个目标一条。无折弯：条带垂落永不打肘弯。

### 4.5 来源纵向错位

多个来源连向同一个目标（例如四个 source → NiFi）时，在目标上错开它们的进入 y：

```
entry_y(k) = target.top + 8 + k * (target_h - 16) / (N - 1)   # k = 0..N-1, evenly spaced
```

避免箭头头部在目标左缘重叠。

---

## 5. 垂直 chevron：语义

保留名称 `Orchestration`、`Security`、`Observability`、`Governance`、`Backup` 始终渲染在右侧栏（§2.9）。任何带 `vertical: true` 的 chevron，无论名称为何，都按保留样式的垂直形处理。规则如下：

- **配对规则（强制，1:1）：**每条垂直 chevron 恰好与一个跨列组件配对，每个跨列组件也恰好与一条垂直 chevron 配对。可配对的两种组件：
  - `kind: bar`：位于集群内（顶行）。惯例上与 `Orchestration` 配对。
  - `kind: cross-cutting`：位于集群下方，每个组件一行。与 `Security`、`Observability`、`Governance` 等配对。

  若输入声明了没有配对组件的垂直 chevron（或反过来），停下来询问用户：图不完整。

- **数量约束：**`len(verticals) == len(bars) + len(crosscuts)`。右侧栏在所有垂直 chevron 间均分（§2.9），因此 chevron 与其条带/行的视觉对齐是近似的：重要的是*标签*对上了，不是 y 像素对齐。

- **排序惯例：**垂直 chevron 自上而下按此顺序声明：先配条带的（Orchestration），再按 crosscut 在集群下方的出现顺序排列与之配对的。这样视觉阅读顺序才一致。

- **不发边：**垂直 chevron 自身不发出连线。它们是*一整列横切关注点的标签*。

- **不放节点：**`kind: node` 不可分配给垂直 chevron。节点永远属于某个水平阶段。

- **右侧栏存在性：**只要存在垂直 chevron，就保留右侧栏（`effective_w = 964`），**所有**水平 chevron 宽度与集群几何相应收缩。不要把垂直 chevron 画在集群上面。

视觉契约：垂直 chevron 所在列在视觉上“拥有”其大致 y 波段处的条带/横切行。Orchestration（栏顶）↔ Airflow 条带（集群顶部）。Security ↔ 身份条带。Observability ↔ 监控条带（身份之下）。依此类推。

---

## 6. 深色模式

`paper`、`ink`、`muted` 与 `accent` 随皮肤反转：取值来自 [`style-guide.md`](style-guide.md) 的深色列。本参考中每个派生值都是**某个不透明度下的角色**，因此 `ink @ 0.18` 在浅色纸面上解析为深墨色、在深色纸面上解析为浅墨色，无需额外处理。

两种模式间只有以下几项不同：

| 元素 | 浅色 | 深色 | 为何不同 |
|---|---|---|---|
| muted 文字 | `muted` | `ink @ 0.65` | 深色模式用不透明度而非色相弱化次要文字 |
| 虚线边框 | `ink @ 0.20` | `ink @ 0.22` | 发丝线在深色纸面上需要略多一点存在感 |
| 节点填充 | `#ffffff`（白） | `ink @ 0.06` | 白色不透明；深色纸面上改为让节点从底面上浮 |
| 节点描边 | `ink @ 0.25` | `ink @ 0.20` | 同等不透明度下，浅墨在深色纸面上视觉更强 |
| 焦点填充 | `accent @ 0.08` | `accent @ 0.12` | 同上 |
| 阶段色带 | `band-1` / `band-2` | `band-2` / `band-3` | 交替向浅一档移位（§6.1） |

跨模式不变：集群边框 `ink @ 0.18`、圆点纹理 `ink @ 0.10`、焦点描边 `accent`、accent 连线 `accent`，以及 chevron 标签（始终 `band-label`）。

### 6.1 阶段色带调色板

chevron 横幅需要**在两种模式下都是深色底带配浅色标签**。`ink` 与 `paper` 在两种模式间互换，横幅不能用它们搭建。它使用四个固定 token，不受明暗翻转影响：

| Token | 值 | 用途 |
|---|---|---|
| `band-1` | `#2d3142` | 最深一档：浅色模式的奇数位 chevron |
| `band-2` | `#3d4460` | 中间一档：浅色模式偶数位、深色模式奇数位 chevron |
| `band-3` | `#4a5270` | 最浅一档：深色模式的偶数位 chevron |
| `band-label` | `#f5f5f5` | 固定标签色：对三条色带的对比度分别为 11.82:1、8.78:1、7.05:1 |

**这些是类型级 token，不是皮肤角色，不会反转。**它们是“hex 值只出现在 [`style-guide.md`](style-guide.md)”这条规则的唯一有意例外。`scripts/lint-skin.py` 会把 `band-2` 与 `band-3` 当作调色板外颜色拒绝，这就是随库发布的高层示例都列在 `scripts/lint-skin-baseline.txt` 里的原因。阶段标签永远用 `band-label`，且 `band-label` 对每条色带的对比度都不得低于 4.5:1，因为无论哪种模式这都是 7px 的小字。换肤时，从新品牌最深的中性色派生出三档相近的色阶，再选一个对三档都保持 4.5:1 的固定标签色。

---

## 7. 可复现性检查清单（品味门禁）

输出 SVG 前，逐条核对**每一项**。有任何一条不过，先修再发布。

1. 每个集群 `node.cx` 等于其 chevron 的 `cx`（§2.2 + §2.7）。正是这一点让 chevron 横幅成为真正的图例。
2. 每个 chevron 的 `width` 是 4 的倍数且 ≥ 120。
3. 保留的右侧栏（28px）**当且仅当**声明了任何垂直 chevron 时才存在。有则 `effective_w = 964`；无则 `effective_w = 1000`。
4. 恰好**一个** `focal` 节点。输入未设 `focal` 时，默认取 chevron "Storage" 下第一个 `kind: node`。
5. 终点为焦点节点的每条边都用 `style: primary`（accent 描边 + `arrow-accent` marker）。
6. 从 `kind: bar` 组件出发的每条边都用 `style: trigger`（虚线 + `arrow-sm`）。
7. 横切条带（如有）**不**发出任何边。
8. 没有节点的出边超过 3 条；若有，它必须就是声明的 `focal` / 枢纽。
9. 所有 `<path>` 与 `<line>` 连线都**先于**任何节点 `<rect>` 输出（z-order）。
10. 每条垂直 chevron 与恰好一个 `bar` 或 `cross-cutting` 组件 **1:1** 配对（§5 配对规则）。`len(verticals) == len(bars) + len(crosscuts)`。
11. `viewBox_h = max(540, strip_y_bot + 112)`：声明了多个 crosscut 时扩大画布，保证图例放得下。
12. 自定义组件颜色（§3.4）只作用于容器 + 图标 + 名称；连线保持拓扑驱动。焦点之外最多 2 个自定义配色组件。
13. 图表通过 SKILL.md §9（4px 网格；≤ 2 个 accent 元素；等宽字体仅用于技术内容；发丝线；无阴影；不用 `rounded-2xl`）。

---

## 8. 反模式

- 省略 chevron 横幅：它是把视觉列映射到功能阶段的关键。
- 节点 x 中心偏离 chevron（§7 第 1 条）：破坏“横幅即图例”的契约。
- 把垂直 chevron 画在集群上（叠加），而不是放进保留的右侧栏。
- 多于一个焦点节点：MinIO/S3（或任何存储枢纽）是*唯一的*焦点。
- 外部区用实线边框：虚线边框才是“这些组件在集群外”的信号。
- 身份条带画进集群边界内：它作用于所有组件，必须横跨整个画布宽度。
- 垂直 chevron 没有配对的条带/横切组件：见 §5 配对规则。
- 条带组件的边画成实线：编排触发必须是虚线。
- 来源向超过 3 个组件扇出却没有枢纽。

---

## 9. 示例

- `assets/example-high-level.html`：仅水平方向，5 阶段，浅色皮肤。
- `assets/example-high-level-dark.html`：同上，深色皮肤。
- `assets/example-high-level-full.html`：同上，编辑卡片边框。
- `assets/example-high-level-vertical.html`：加入垂直 Orchestration + Security chevron、Airflow 条带、Keycloak 横切条带。**完整参数化模式的参照渲染。**
- `assets/example-high-level-vertical-dark.html`：垂直模式，深色皮肤。
- `assets/example-high-level-vertical-full.html`：垂直模式，编辑卡片边框。
- `assets/example-datalake.html`：无集群的五阶段数据栈（Sources → Ingest → Data Lake → Query → Consume），基于分区的流向，没有容器编排器边界。MinIO 湖是焦点节点；垂直关注点被压平进水平 chevron 横幅。浅色皮肤。
- `assets/example-datalake-dark.html`：同上，深色皮肤。
- `assets/example-datalake-full.html`：同上，编辑卡片边框。
