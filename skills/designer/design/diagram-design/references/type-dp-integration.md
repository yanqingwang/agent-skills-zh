> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-dp-integration.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# DP 集成图（DP integration）

**最适用于：** 数据平台的集成拓扑：哪些源系统接入、哪些消费界面接出、各自说什么协议。中心辐射式布局，外面裹着一个显式的 **Data platform** 层；没有时间/阶段轴。

当问题是*"这个平台暴露了哪些界面、走什么线路？"*而非*"数据如何流经各阶段？"*时使用。

本类型是**参数化的**：与 `type-high-level.md` 一样，每个坐标都由一份小的输入 schema 推导。同一份输入的两次生成必须产出视觉上完全一致的 SVG。

---

## 1. 输入：参数契约

```yaml
sources:                            # left column, 0..6 nodes
  - { name: "Databases",  type: "db",        subtitle: "SQL · MariaDB",
      connects_to: [{to: "NiFi", label: "JDBC"},
                    {to: "Trino", label: "FEDERATE", style: "federated"}] }
  - { name: "SFTP drops", type: "sftp",      subtitle: "scheduled pulls",
      connects_to: [{to: "NiFi", label: "SFTP"}] }
  - { name: "Email",      type: "mail",      subtitle: "IMAP attachments",
      connects_to: [{to: "NiFi", label: "IMAP"}] }
  - { name: "IBM legacy", type: "mainframe", subtitle: "file export",
      connects_to: [{to: "NiFi", label: "FILE"}] }

platform:
  name: "DATA PLATFORM"             # zone label (paper-masked top border)
  rows:                             # ordered top→bottom; each is bar or row
    - { kind: bar, name: "Trino",   icon: trino,   subtitle: "federated query · push-down",
        role: "SQL", focal: true }
    - { kind: row, nodes: [
        { name: "Apache NiFi",  icon: nifi,    role: "INGEST",   subtitle: "flow-based ETL" },
        { name: "MinIO",        icon: minio,   role: "STORE",    subtitle: "S3 object store · medallion", focal: true },
        { name: "JupyterLab",   icon: jupyter, role: "NOTEBOOK", subtitle: "Python · R · pandas" }
      ]}
    - { kind: bar, name: "Apache Airflow", icon: airflow,
        subtitle: "scheduler · DAG triggers · backfill", role: "DAG" }

consumers:                          # right column, 0..6 nodes
  - { name: "Desktop apps",   type: "monitor", subtitle: "SPSS · SAS · Stata",
      connects_from: [{from: "Trino", label: "ODBC"}] }
  - { name: "BI & reports",   type: "chart",   subtitle: "Tableau · Power BI",
      connects_from: [{from: "Trino", label: "JDBC"}] }
  - { name: "Public website", type: "globe",   subtitle: "NatStat portal",
      connects_from: [{from: "Trino", label: "HTTPS"}] }
  - { name: "API gateway",    type: "api",     subtitle: "3rd-party / OAuth2",
      connects_from: [{from: "Trino", label: "REST"}] }

footer:                             # 0..N cross-cutting bars stacked below zone (full-canvas width)
  - { name: "Active Directory", icon: key,        subtitle: "LDAP · SSO · group RBAC",
      color: "#b85450" }            # tinted red to flag the security concern
  # additional footer nodes (Observability, Backup, …) stack below this one

internal_connections:               # explicit platform-component edges
  - { from: "NiFi",        to: "MinIO",      style: "primary",   label: "WRITE" }
  - { from: "MinIO",       to: "JupyterLab", style: "secondary", label: "READ"  }
  - { from: "MinIO",       to: "Trino",      style: "secondary" }
  - { from: "JupyterLab",  to: "Trino",      style: "secondary", dashed: true }
  - { from: "Airflow",     to: ["Apache NiFi", "MinIO", "JupyterLab"], style: "trigger" }

focal_accent: accent                # one color for all focal components; the `accent` role by default,
                                    # or an explicit "#hex" to override it
dark: false
```

**`platform.rows` 的保留 `kind` 值：**
- `bar` — 占满区域宽度的横条。默认高 44px（焦点横条为 56px）。必填字段：`name`、`icon`。可选：`subtitle`、`role`、`color`、`focal`。
- `row` — N 个节点在区域宽度上均匀排布。必填：`nodes` 列表。每个节点有 `name`、`icon`，可选 `role`、`subtitle`、`color`、`focal`。

**源/消费端 `type` 值 → 图标映射**（扩展 `references/primitive-icons.md`）：
- `db` → 圆柱体，`sftp` → 带箭头的文件夹，`mail` → 信封，`mainframe` → 带散热孔的服务器
- `monitor` → 桌面屏幕，`chart` → 柱状图，`globe` → 地球，`api` → 花括号
- `key` → 钥匙 + 圆环（身份 / IDP）
- `primitive-icons.md` 中任何显式图标名同样接受。

**逐组件 `color: "#hex"`** 对任意节点、横条或底栏条目都是可选的。见 §4。

---

## 2. 布局公式：确定性几何

```
# Canvas
viewBox_w        = 1200
n_sources        = len(sources)
n_consumers      = len(consumers)
n_footer         = len(footer)

# Side columns (sources left, consumers right)
col_top          = 92
col_node_h       = 64
col_gap          = 24                    # stride = col_node_h + col_gap = 88
col_h_min        = 336                   # default fits 4 sources (4 * 88 - 24)
col_h            = max(col_h_min, max(n_sources, n_consumers) * 88 - 24)
left_x           = 40
left_w           = 160
right_x          = 1000
right_w          = 160
col_node_y(k)    = col_top + k * 88
col_node_cy(k)   = col_node_y(k) + col_node_h/2     # 124, 212, 300, 388 by default

# Platform zone
zone_x           = 260
zone_w           = 696
zone_y           = 72
zone_h           = col_h                            # zone always matches column height
zone_cx          = zone_x + zone_w/2                # 608
zone_pad_x       = 16                               # inside left/right padding for bars
zone_label_y     = zone_y + 3                       # paper-masked label across top border

# Footer bars (below zone — each cross-cutting concern is a full-width bar)
footer_top       = zone_y + zone_h + 52             # 52-px gap below zone
footer_bar_h     = 56
footer_bar_x     = 40                               # aligned with source column left edge
footer_bar_w     = viewBox_w - 80                   # = 1120 — spans from source col left to consumer col right
footer_gap       = 8
footer_y(k)      = footer_top + k * (footer_bar_h + footer_gap)
footer_bottom    = footer_top + n_footer * (footer_bar_h + footer_gap) - footer_gap

viewBox_h        = max(600, footer_bottom + 84)     # 84 reserved for legend

# Platform.rows allocation inside zone
bar_h_focal      = 56
bar_h_default    = 44
row_h            = 72
row_gap          = 16
```

### 2.1 行摆放（游标算法）

自上而下为每个 `platform.rows` 条目分配位置。唯一的 `row` 条目（N>1 时为第一个 row）锚定到侧列第 2 行，让它的连接线保持水平：

```
primary_row_idx  = index of first kind=row in platform.rows
primary_row_top  = col_node_y(1) - (row_h - col_node_h)/2     # 176 by default
                                                              # 4-px nudge so cy aligns with side row 2

# Place rows above primary
y = primary_row_top
for entry in platform.rows[:primary_row_idx] reversed:
    y -= row_gap
    entry.h     = bar_h_focal if (entry.kind == bar and entry.focal) else bar_h_default
    y          -= entry.h
    entry.y_top = y                                            # Trino bar lands at y=104

# Place primary row
platform.rows[primary_row_idx].y_top = primary_row_top         # NiFi/MinIO/Jupyter at y=176
platform.rows[primary_row_idx].h     = row_h

# Place rows below primary
y = primary_row_top + row_h
for entry in platform.rows[primary_row_idx+1:]:
    y          += row_gap
    entry.y_top = y
    entry.h     = bar_h_focal if (entry.kind == bar and entry.focal) else bar_h_default
    y          += entry.h

# Constraint: y <= zone_y + zone_h
```

这为标准形态（顶部横条 / 3 节点行 / 底部横条）产出规范布局：Trino 在 `y=104 h=56`，主行在 `y=176 h=72`，Airflow 在 `y=324 h=44`。Airflow 底边锚在 y=368（距 y=408 的区域底部净空 40px）。**注意**：规范布局下，主行底部（y=248）与 Airflow 顶部（y=324）之间有 76px 间隙。这个间隙是有意的：Airflow 在视觉上与源/消费端第 4 行（cy=388）处于同一 y 波段，读起来像底部侧列行的兄弟。

### 2.2 `row` 条目内的节点摆放

```
N            = len(row.nodes)
node_w       = (zone_w - 2*zone_pad_x - (N-1) * 16) / N
node_x(j)    = zone_x + zone_pad_x + j * (node_w + 16)
node_cx(j)   = node_x(j) + node_w/2
```

对规范的 3 节点行：`node_w = (696 - 32 - 32) / 3 = 210.67`。随附示例使用固定 `node_w=160` 与自定义 x 位置（`288, 480, 672`），让每个节点的 `cx` 对齐到连接线走廊：368、560、752。**两种布局都合法**；上面的公式是新图的默认值。任何偏离都要在渲染出的 SVG 里用注释说明。

### 2.3 横条（占满区域宽）摆放

```
bar_x      = zone_x + zone_pad_x         # 276
bar_w      = zone_w - 2*zone_pad_x       # 664
bar_cx     = zone_cx                     # 608
```

横条横跨区域全宽减去两侧各 16px 内边距。标记 `focal: true` 的横条使用 `bar_h_focal=56` 与 accent 样式（填充 `rgba(focal_accent, 0.08)`，描边 `focal_accent`）。非焦点横条使用 `bar_h_default=44` 与 muted 样式（填充 `ink @ 0.05`，描边 `ink @ 0.32`）。

### 2.4 源 / 消费端摆放（侧列）

```
source_y(k)       = col_top + k * 88            # 92, 180, 268, 356, …
source_cy(k)      = source_y(k) + col_node_h/2  # 124, 212, 300, 388, …
consumer_y(k)     = source_y(k)                 # mirrored
consumer_cy(k)    = source_cy(k)
```

所有侧列节点使用固定 `w=160 h=64`。相同的填充/描边模式：填充 `muted @ 0.06`，描边 `soft`，描边宽度 1。

---

## 3. 连接线规则（强制）

五种样式，绑定到拓扑。触及焦点、起自横条、以及 Trino → 消费端的边线，不要让用户覆盖样式：这些由规则固定。

| `style` | 描边 | 宽度 | 虚线 | 标记 | 何时必须使用 |
|---|---|---|---|---|---|
| `primary` | `focal_accent`（默认 `accent`） | 1.4 | — | `arrow-focal` | 每条端点为 `focal: true` 组件的边。也包括每条 Trino → 消费端边（服务流规则）。 |
| `secondary` | `muted` | 1.2 | — | `arrow` | 内部平台组件边，以及不触及焦点的源 → 平台边的默认值。 |
| `federated` | `link` | 1.0 | `4,3` | `arrow-link` | 联邦查询（如源 DB → Trino）。 |
| `trigger` | `muted` | 1.0 | `4,3` | `arrow` | 每条起自 `kind: bar` 组件的边（Airflow 下发）。不加标签。 |
| `auth` | `accent` | 1.2 | `5,4` | `arrow-accent` | 每条从底栏节点向上到区域底边的边。**绝不指向具体组件。** |

**Defs 块**（必需，恰好六个标记）：

```svg
<defs>
  <marker id="arrow"        markerWidth="8" markerHeight="6" refX="7" refY="3"   orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{muted}"/></marker>
  <marker id="arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3"   orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{accent}"/></marker>
  <marker id="arrow-focal"  markerWidth="8" markerHeight="6" refX="7" refY="3"   orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{focal_accent}"/></marker>
  <marker id="arrow-link"   markerWidth="8" markerHeight="6" refX="7" refY="3"   orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{link}"/></marker>
  <marker id="arrow-sm"     markerWidth="6" markerHeight="5" refX="5" refY="2.5" orient="auto"><polygon points="0 0, 6 2.5, 0 5" fill="{muted}"/></marker>
  <marker id="arrow-dim"    markerWidth="8" markerHeight="6" refX="7" refY="3"   orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{ink @ 0.45}"/></marker>
</defs>
```

### 3.1 出边 / 入边侧（不可协商）

| 边类型 | 源出边侧 | 目标入边侧 |
|---|---|---|
| 源 → 平台组件 | 源的**右侧** | 目标的**左侧** |
| 平台 → 平台（同行） | **右侧** | **左侧** |
| 横条 → 行节点（垂直下落） | 横条**底部**，位于 `node_cx(target)` | 目标**顶部** |
| 平台 → 消费端 | 源平台组件的**右侧** | 消费端的**左侧** |
| 底栏 → 区域 | 底栏**顶部**（位于 `footer_auth_x(k)`） | 区域底边 `y = zone_y + zone_h` |
| 底栏 → 组件（任何具体组件） | **禁止** |

### 3.2 走线

- 正交折线，至多两个拐弯；每个拐角用 `r=8` 的 Q 贝塞尔。
- **扇出错位：** 一个节点向同侧的 N 个目标扇出时，按索引以 ±4px 错开出边 y，避免箭头重叠（如 Trino → 4 个消费端在 y=124、132、140、148 出边）。垂直段在区域边缘与消费端列之间的走廊里运行，同样按 y 错开。
- **Z 顺序：** 所有连接线画在任何矩形**之前**（节点填充由此遮住线端）。
- **标记：** 每条 `<line>` / `<path>` 恰好一个 `marker-end`。绝不使用 `marker-start`。
- **标签：** 每条 `primary`、`secondary`、`federated`、`auth` 边都带协议标签（`arrow-label` 角色，8px，纸色填充矩形遮罩，距描边上方留 6–10px 净空）。`trigger` 边不加标签。

### 3.3 底栏 → 区域干线

只有 1 条底栏时：`x = zone_cx` 处一条垂直线，从 `footer_y(0)` 到 `zone_y + zone_h`。

有 N≥2 条底栏时：错开 AUTH 线，避免压到堆叠的底栏。对底栏索引 `k`：

```
footer_auth_x(k) = zone_cx + (k - (N-1)/2) * 32     # 32-px stride per footer
```

示例：
- N=1 → 560
- N=2 → 544, 576
- N=3 → 528, 560, 592

每条 AUTH 线从 `(footer_auth_x(k), footer_y(k))` 向上到 `(footer_auth_x(k), zone_y + zone_h)`。AUTH 标签紧贴区域底边箭头的上方。

### 3.4 交叉

避免。接受交叉之前，先经由走廊 x 位置改线。实在无法避免时，后画的路径在先画路径上方带一个 6px 弧形跳线。

---

## 4. 组件颜色覆盖（与 `type-high-level.md` §3.4 一致）

任何源、消费端、平台组件（节点或横条）或底栏节点都可接受可选的 `color: "#hex"`。与 high-level 保持一致，规则在各类型间读法相同。

**颜色的施加位置**（`C = color`）：

| 元素 | 浅色 | 暗色 |
|---|---|---|
| 容器填充（`rect` 主体） | `rgba(C, 0.06)` | `rgba(C_light, 0.10)` |
| 容器描边 | `rgba(C, 0.35)`（节点 `stroke-width=1`，横条 `0.8`） | `rgba(C_light, 0.45)` |
| 角色徽章描边 | `rgba(C, 0.40)` | `rgba(C_light, 0.55)` |
| 角色徽章文本 | `rgba(C, 0.85)` | `rgba(C_light, 1.0)` |
| 图标描边 / 填充 | `C` | `C_light` |
| 名称文本 | `C` | `C_light` |
| 副标题文本 | **不变**（muted） | **不变**（muted） |
| 触及该组件的连接线 | **不变**，由拓扑决定 | **不变** |

`C_light` = 同一十六进制色提亮约 15% 以保证暗色对比（如 `#b85450` → `#d97a78`）。

**规则：**

- **绝不用于焦点组件。** `focal_accent` 永远优先，焦点组件上的 `color` 被忽略。
- **绝不用于连接线。** 想要彩色边线，从 §3 选一个不同的 `style`，而不是颜色覆盖。
- **每图自定义着色组件上限 2 个**（焦点对之外）。

**语义调色板**（除非品牌要求，否则用这些）：
- `#b85450` 铁锈红：安全 / 身份（AD、Keycloak、Vault）
- `#5a7d9a` 石板蓝：可观测性（Prometheus、Datadog、OpenTelemetry）
- `#7a8c47` 橄榄绿：治理 / 血缘（OpenMetadata、DataHub）
- `#8c6d3f` 暖棕：备份 / 灾备（Velero、Restic）

---

## 5. 焦点规则

**恰好两个焦点组件。** 默认：存储枢纽（MinIO / S3 或类似）与联邦引擎（Trino / Dremio 或类似）。这两个界面把"平台"与"一堆工具"区分开。其他一切（NiFi、Jupyter、Airflow、AD、全部源、全部消费端）保持 ink / muted。

- 在组件条目上标 `focal: true`。
- 焦点 `kind: bar` 使用 `bar_h_focal=56`（更高）与 accent 样式。
- 焦点 `kind: row` 节点保持 `row_h=72`，但用 accent 样式。
- **Trino → 全部消费端**的边一律为 `primary`（accent），无论各消费端有无焦点标记：这是服务流规则。
- 若 `focal: true` 的组件少于 2 个或多于 2 个，停下询问用户。

---

## 6. 暗色模式

`paper`、`ink`、`muted`、`soft`、`accent`、`link` 随皮肤反转：取值见 [`style-guide.md`](style-guide.md) 的暗色列。**带透明度的角色**无需暗色处理，因为 `ink @ 0.32` 会针对当前生效的 ink 解析。

只有以下各项在两种模式间不同：

| 元素 | 浅色 | 暗色 | 差异原因 |
|---|---|---|---|
| 侧列填充 | `muted @ 0.06` | `ink @ 0.06` | 石板色调在暗色纸底上像泥渍；纯 ink 保持中性 |
| 侧列描边 | `soft` | `ink @ 0.30` | 同上 |
| 区域填充 | `ink @ 0.025` | `ink @ 0.04` | 淡染在暗色纸底上需要略强的存在感 |
| 非焦点横条填充 | `ink @ 0.05` | `ink @ 0.06` | 同上 |
| 焦点填充 | `accent @ 0.08` | `accent @ 0.12` | 同上 |

两种模式间不变：区域描边 `ink @ 0.32`、焦点描边 `accent`，以及自定义组件颜色（`C` → `C_light`，提亮约 15%）。

---

## 7. 可复现清单（品味门槛）

输出 SVG 前，逐项核验：

1. `viewBox = "0 0 1200 {viewBox_h}"`，其中 `viewBox_h = max(600, footer_bottom + 84)`。
2. 平台区域位于 `x=260 y=72 w=696 h=col_h`。区域标签以纸色遮挡压在顶边框上，`y=zone_y+3`。
3. 左列在 `x=40..200`，右列在 `x=1000..1160`，均宽 160。
4. 源 / 消费端行顶部 `y=92`，步距 88px。
5. `platform.rows` 条目经 §2.1 游标算法在区域内堆叠；总 y 跨度 ≤ `zone_h`。
6. 每个 `kind: row` 内，节点 x 中心在区域宽度上均匀分布（§2.2）。
7. **恰好 2 个**焦点组件（`focal: true`）。
8. 每条起自 `kind: bar` 组件的边用 `style: trigger`（虚线，无标签）。
9. 每条 Trino → 消费端边用 `style: primary`（服务流规则）。
10. 底栏节点只以 `auth` 样式连接区域底边。**不得**有从底栏到具体组件的边。
11. 自定义组件颜色 ≤ 2（焦点对之外）。连接线绝不因组件 `color` 而改色。
12. 所有连接线先于任何节点矩形输出（Z 顺序规则）。

---

## 8. 源与消费端：图标库

在 `<defs>` 中把每个图标定义为 `<g id="ico-…">`，以 translate(cx, cy) 绘制并带 `stroke="currentColor"`，让它继承周围文本颜色。常见图标：

- `ico-db`（圆柱体）：关系型源
- `ico-sftp`（带下箭头的文件夹）：文件投递
- `ico-mail`（信封）：邮件拉取
- `ico-mainframe`（带散热孔的服务器）：遗留系统
- `ico-monitor`：桌面分析工具
- `ico-chart`（柱条）：BI / 报表工具
- `ico-globe`：公开网站
- `ico-api`（括号 `{}`）：网关与第三方客户端
- `ico-key`：身份 / IDP
- `ico-monitoring`（折线图）：可观测性栈

需要更多图标时，浏览 `assets/icons.html` 并定义匹配的 `<symbol>` 块。

---

## 9. 身份等公共服务：接到层，而不是接到组件

**Active Directory**（或 Keycloak、IAM、OPA，任何横切的身份 / 策略 / 密钥存储）为平台中的*每一个*组件做认证。把它接到某个具体工具会低估其信任范围。正确做法是用一条箭头接到平台区域底边，标 `AUTH`（§3.3）。

同样的规则适用于任何其他覆盖整个层面的服务：集中日志、密钥保险库、可观测性栈、审计汇、mTLS 根。每个放进 `footer` 列表，各占一行，各有一条自己的 AUTH 线向上到区域底边（按 §3.3 依索引错开）。视觉读法是"平台层委托给所有这些服务"，这正是架构事实。

---

## 10. 预算：本类型超出默认值

这是唯一有意超出默认 9 节点 / 12 箭头预算的类型。一个真实的平台集成图会展示：

- 4–6 个源节点
- 5 个平台组件
- 4–6 个消费端节点
- 1–3 个底栏节点（身份、可观测性、备份等）

合计 **14–20 个节点**。复杂度本身就是重点：这张图在陈述"不同集成界面的*数量*"。压缩它们就推翻了这个陈述。

当它变得难以驾驭时：
- 合并明显相同的源行（如四个 MariaDB 数据库 → 一个 `Databases` 节点，子标签 `4 × MariaDB`）
- 拆成两张图（每个集成平面一张：数据、身份、可观测性各一）

---

## 11. 反模式

- **≥3 个不同条目时把源或消费端压成单个节点**：违背本类型的全部意义。想折叠就用 Architecture 或 High-level。
- **从"源"到"平台"的一条总线箭头**：每条线都必须标注协议；集成团队就是这样读图的。
- **区域内按工具配色**（teal-NiFi、magenta-MinIO、yellow-Jupyter）：压平层级；只有两个焦点配得上珊瑚色，加上至多 2 个横切组件的自定义颜色（§4 上限）。
- **焦点组件超过 2 个**：焦点存在的意义是区分"平台"与"一堆工具"；>2 会抹掉信号（同 SKILL.md §1 规则）。
- **焦点组件上的 `color` 覆盖**：被忽略。`focal_accent` 永远优先。
- **底栏接到某个具体工具**（如 AD → 只接 Airflow）：除非该服务确实只保护这一个工具，否则是错的。默认是覆盖整个层面的连接。
- **底栏或身份放进区域内**：身份从外部守门这一层。画在内部会歪曲信任模型。
- **顶部的阶段箭头条**：那是 `high-level` 的东西。
- **自定义着色的连接线**：连接线由拓扑决定。样式选颜色；组件的 `color` 永不扩散到它的边。

---

## 12. 示例

- `assets/example-dp-integration.html` — 极简浅色（1 条底栏 = AD）。图库默认。
- `assets/example-dp-integration-dark.html` — 同一张，暗色皮肤。
- `assets/example-dp-integration-full.html` — 同一张，编辑卡片式外框。
