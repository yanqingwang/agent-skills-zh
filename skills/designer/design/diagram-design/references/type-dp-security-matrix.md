> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-dp-security-matrix.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# DP 安全矩阵（DP security matrix）

**最适用于：** 记录数据平台中按角色 / 按组件的访问权限：一个网格，每行是一个平台组件（Keycloak、MinIO 桶、Trino catalog、JupyterHub、NiFi 等），每列是一个角色 / AD 组（Data Administrators、Data Engineers、Data Scientists、Data Consumers 等）。每个交叉格里放一个权限值（Admin / Full / R/W / Read / SELECT / Login / 无访问），并带与权限级别匹配的视觉类别。一个格可标记为焦点，用来突出关键访问规则（如"Data Consumers 只能对 aggregated catalog 执行 `SELECT`，这是消费端唯一的访问途径"）。

当利益相关方需要审计平台中*谁能做什么*时使用。问题若是*谁能和谁通信*（拓扑/协议）而非*谁能写/读什么*（权限），请选 **DP integration**。

本类型是**参数化的**：§1 的输入 schema 通过 §2 的公式驱动每个坐标。规则形态与 `type-medallion.md` / `type-process.md` / `type-data-flow.md` 一致，因此焦点规则、颜色覆盖、暗色模式与可复现清单在各类型间读法相同。

---

## 1. 输入：参数契约

```yaml
title:    "Platform Access Matrix"
subtitle: "Four canonical groups × platform components"

roles:                                  # 2..6 columns, ordered left → right
  - { name: "Data Administrators", code: "DL-DataAdmins"      }
  - { name: "Data Engineers",      code: "DL-DataEngineers"   }
  - { name: "Data Scientists",     code: "DL-DataScientists"  }
  - { name: "Data Consumers",      code: "DL-DataConsumers"   }

components:                             # 2..14 rows, ordered top → bottom
  - { name: "Keycloak",                          hint: "SSO" }   # `hint` = right-aligned aside in label cell
  - { name: "MinIO · raw bucket" }
  - { name: "MinIO · anon · staging · agg" }
  - { name: "Trino · raw catalog" }
  - { name: "Trino · anon-staging" }
  - { name: "Trino · aggregated" }
  - { name: "JupyterHub" }
  - { name: "NiFi" }

cells:                                  # explicit (row, col) entries; omitted → defaults to "none"
  # value = displayed text (free-form)
  # level = visual category: full | rw | read | none  (closed vocabulary, drives styling)
  # focal: true (max 1)            — overrides level to focal styling
  # sub: "second-line text"        — used inside focal cell
  # color: "#hex"                  — optional per-cell color override (§4)
  - { row: 0, col: 0, value: "Admin", level: "full" }
  - { row: 0, col: 1, value: "Login", level: "read" }
  - { row: 0, col: 2, value: "Login", level: "read" }
  - { row: 0, col: 3, value: "Login", level: "read" }

  - { row: 1, col: 0, value: "Full",       level: "full" }
  - { row: 1, col: 1, value: "R/W",        level: "rw"   }
  - { row: 1, col: 2, value: "No access",  level: "none" }
  - { row: 1, col: 3, value: "No access",  level: "none" }

  # ... rows 2..4 follow the same pattern ...

  - { row: 5, col: 0, value: "Full",       level: "full" }
  - { row: 5, col: 1, value: "R/W",        level: "rw"   }
  - { row: 5, col: 2, value: "SELECT",     level: "read" }
  - { row: 5, col: 3, value: "SELECT only", sub: "sole consumer access", focal: true }

  # ... rows 6..7 ...

none_label: "No access"                 # default text rendered when a cell is omitted
dark: false
```

**保留字段语义：**
- `roles[j].name` — 主角色标签（`node-name` 角色，11px，ink 横幅上的白字）
- `roles[j].code` — 次要 AD 组标识（`sublabel` 角色，白字，透明度 0.85）
- `components[i].hint` — 可选，标签格内右对齐的 `sublabel` 文本（如 `"SSO"`、`"S3 API"`）
- `cells[k].level` — 封闭词表 `full | rw | read | none`。按 §2.4 驱动填充/描边/文本颜色。
- `cells[k].value` — 自由格式的显示文本。领域特定标签（`"R/W"`、`"SELECT"`、`"Login"`）无需发明新 level 即可使用。
- `cells[k].focal: true` — 恰好**一个**格可声明此项。将 `level` 覆盖为焦点样式。
- `cells[k].sub` — 可选的第二行文本（配合焦点使用）。以 `sublabel` 角色、8px 渲染在主值下方。
- `cells[k].color: "#hex"` — 可选的逐格颜色覆盖（§4）。

---

## 2. 布局公式：确定性几何

```
# Constants
left_pad         = 12
right_pad        = 48
comp_col_w       = 208
comp_role_gap    = 12
role_col_w       = 148
role_col_gap     = 16
header_h         = 52
row_h            = 36
row_stride       = 40

# Counts
n_roles          = len(roles)        # 2..6
n_components     = len(components)   # 2..14

# Canvas
viewBox_w        = left_pad + comp_col_w + comp_role_gap
                   + n_roles * role_col_w + (n_roles - 1) * role_col_gap
                   + right_pad
                   # 4 roles → 12 + 208 + 12 + 592 + 48 + 48 = 920

header_y         = 72
row_y(k)         = 140 + k * row_stride                  # 140, 180, 220, ...
rows_bottom      = row_y(n_components - 1) + row_h       # 8 rows → 456
legend_y_top     = rows_bottom + 20                      # 476 for 8-row canonical
viewBox_h        = legend_y_top + 44                     # 520 for 8-row canonical

# Column positions
comp_col_x       = left_pad                                                       # 12
role_col_x(j)    = left_pad + comp_col_w + comp_role_gap
                   + j * (role_col_w + role_col_gap)
                                                                                  # 232, 396, 560, 724
role_col_cx(j)   = role_col_x(j) + role_col_w / 2                                 # 306, 470, 634, 798
```

### 2.1 背景

整个 viewBox 铺满纯色纸底。无点阵。

### 2.2 表头行（`y = 72, h = 52`）

**组件列表头格：**
- 矩形：`(comp_col_x, header_y, comp_col_w, header_h)`，白色填充，描边 `ink @ 0.12` 0.8，`rx=6`
- 两行标签，居中于 `(comp_col_x + comp_col_w/2, header_y+24)` 与 `(…, header_y+40)`：
  - 第 1 行：`"Component"` — `node-name` 角色，11px，ink
  - 第 2 行：`"vs. AD group"` — `sublabel` 角色，muted

**角色横幅（每角色一个）：**
- 矩形：`(role_col_x(j), header_y, role_col_w, header_h)`，填充 `ink`，`rx=6`
- 两行标签居中：
  - 第 1 行 `y=92`：`roles[j].name` — `node-name` 角色，11px，白色
  - 第 2 行 `y=108`：`roles[j].code` — `sublabel` 角色，白色，透明度 0.85

### 2.3 数据行（`y = row_y(k), h = 36`）

**组件标签格：**
- 矩形：`(comp_col_x, row_y(k), comp_col_w, row_h)`，白色填充，描边 `ink @ 0.12` 0.8，`rx=4`
- 名称在 `(comp_col_x + 12, row_y(k) + 22)`：`node-name` 角色，11px，ink，左对齐
- hint（若有）在 `(comp_col_x + comp_col_w − 12, row_y(k) + 22)`：`sublabel` 角色，muted，右对齐

**值格（每对角色 × 组件一格）：**
- 矩形：`(role_col_x(j), row_y(k), role_col_w, row_h)`，`rx=4`，描边 `ink @ 0.12` 0.6
- 填充与文本颜色取决于 `level`（或焦点标记）：见 §2.4
- 值文本居中于 `(role_col_cx(j), row_y(k) + 22)`：`node-name` 角色，10px
- 焦点格的主文本略微上移至 `y=18`，副行在 `y=30`（`sublabel` 角色，8px）

### 2.4 格样式表

| `level` | 填充 | 描边 | 文本颜色 | 文本字重 |
|---|---|---|---|---|
| `full` | `ink @ 0.08` | `ink @ 0.12` | `ink` | 600 |
| `rw` | `#FFFFFF` | `ink @ 0.12` | `ink` | 400 |
| `read` | `muted @ 0.08` | `ink @ 0.12` | `muted` | 400 |
| `none` | `paper` | `ink @ 0.12` | `soft` | 400 |
| **focal** | `accent @ 0.07` | `accent`（1.4） | `accent` | 600 |

焦点格可带第二行（`sub:`），以 `accent` 渲染，`sublabel` 角色，8px，透明度 0.85。

### 2.5 图例（`y_top = legend_y_top, h ≈ 30`）

`legend_y_top` 处一条发丝线分隔。分隔线之下是一行样式色样及其标签，只显示图中实际用到的样式。

- `"LEGEND"` eyebrow 位于 `(left_pad, legend_y_top + 20)`：`eyebrow` 角色，muted，字距 0.14em
- 每个样式：色样矩形（14×12 `rx=2`）后接一个 `sublabel` 角色标签
- 条目 x 位置从左到右制表，步距约 120px；仅当 `n_roles ≥ 6` 时图例折到第二个视觉行（否则一行放得下）

---

## 3. 用格，不用连接线

矩阵图**没有连接线**：格与格之间没有箭头，没有流线。图的信息完全在格内容 + 格样式里。唯一"像连接线"的元素是焦点格的 accent 边框，它在视觉上"点名"一个特定交叉。

格**不发出任何边**。不要添加指向格内或格间的箭头：那属于别的图类型。

---

## 4. 颜色覆盖

三条相互独立的覆盖轴：逐格、逐组件（行）、逐角色（列）。全部可选，都用同一个 `color: "#hex"` 字段，都取自同一份推荐调色板。与 `type-high-level.md` §3.4、`type-process.md` §4、`type-medallion.md` §4 一致。

### 4.1 逐格 `color`

给一个特定的交叉格染色。施加于：

| 元素 | 浅色 | 暗色 |
|---|---|---|
| 格填充 | `rgba(C, 0.08)` | `rgba(C_light, 0.12)` |
| 格描边 | `rgba(C, 0.45)` 宽 1.0 | `rgba(C_light, 0.55)` 宽 1.0 |
| 值文本 | `C` | `C_light` |
| 副文本（若有） | `rgba(C, 0.85)` | `rgba(C_light, 0.95)` |

`C_light` = 同一十六进制色提亮约 15% 以保证暗色对比。

### 4.2 逐组件 `color`（`components[i].color`）

只给该行的**标签格**（左列）染色。该行的数据格保持各自的 `level` 样式。行颜色标记的是*这个组件是什么*，不是*它里面装着什么权限*。

| 元素 | 浅色 | 暗色 |
|---|---|---|
| 标签格填充 | `rgba(C, 0.06)` | `rgba(C_light, 0.10)` |
| 标签格描边 | `rgba(C, 0.45)` 宽 0.8 | `rgba(C_light, 0.55)` 宽 0.8 |
| 组件名称 | `C` | `C_light` |
| hint 文本 | 不变（muted） | 不变（muted） |

### 4.3 逐角色 `color`（`roles[j].color`）

只给**列横幅**（顶行）染色。其下的格保持各自的 `level` 样式。用所选十六进制色替换默认的深蓝横幅填充。

| 元素 | 浅色与暗色（横幅在两种模式下相同） |
|---|---|
| 横幅填充 | `C` |
| 角色名 + code 文本 | `C` 偏暗（亮度 ≤ 0.5）时为 `#FFFFFF`，否则 `ink` |

选了中等亮度的色值（如黄色 `#c9a23a`），文本会自动切换为 ink 以保证对比。可用 `roles[j].text_color: "#hex"` 覆盖这个自动选择。

### 4.4 规则

- **焦点格优先。** 焦点格忽略 `color` 覆盖：一定是 accent。
- **逐格 `color` 覆盖该格的 `level` 样式。**
- **逐组件 / 逐角色覆盖有作用域：** 组件 → 只影响行标签；角色 → 只影响横幅。它们**不会**扩散进矩阵主体。要突出特定交叉，用逐格。
- **上限：** 每图自定义着色实体总数 ≤ 5（格 + 组件 + 角色合计）。超过 5，矩阵读起来就是彩色噪音：拆成多张图，或重新想想哪种颜色承载哪种关注。

### 4.5 推荐调色板（与其他参数化类型相同）

- `#b85450` 铁锈红 — 权限提升 / 破窗应急 / SoX 标记
- `#5a7d9a` 石板蓝 — 质量 / 监控 / 可观测性门
- `#7a8c47` 橄榄绿 — 已批准 / 治理通过 / 可发布
- `#c9a23a` 暖黄 — 工作中 / 沙箱 / 数据科学家区
- `#8c6d3f` 暖棕 — 归档 / 冷数据 / 灾备

---

## 5. 焦点规则

每图恰好**一个**焦点格（或零个）。焦点格：
- 使用焦点样式（accent 填充 + accent 描边 1.4 + accent 文本加粗）
- 可带两行内容：主 `value` 在 `y = row_y(k) + 18`，`sub` 在 `y = row_y(k) + 30`
- 点出全图的核心安全主张：*那一条*把这个平台的安全姿态与普通权限表区分开的访问规则

若声明了 0 个或多于 1 个 `focal: true` 格，停下询问用户。

---

## 6. 暗色模式

| Token | 浅色 | 暗色 |
|---|---|---|
| Paper | `paper` | `ink` |
| Ink | `ink` | `paper` |
| Muted | `muted` | `soft` |
| Soft（无访问文本） | `soft` | `muted` |
| Accent | `accent` | `accent` |
| 角色横幅填充 | `ink` | `ink` |
| 表头 / 行描边 | `ink @ 0.12` | `paper @ 0.18` |
| Full / Admin 填充 | `ink @ 0.08` | `paper @ 0.10` |
| R/W 填充 | `#FFFFFF` | `paper @ 0.06` |
| Read 填充 | `muted @ 0.08` | `soft @ 0.12` |
| 无访问填充 | `paper` | `paper @ 0.02` |
| 焦点填充 | `accent @ 0.07` | `accent @ 0.12` |
| 焦点描边 | `accent` | `accent` |
| 自定义组件颜色 | `C` | `C_light`（提亮约 15%） |

---

## 7. 可复现清单（品味门槛）

输出 SVG 前，逐项核验：

1. `viewBox = "0 0 {viewBox_w} {viewBox_h}"`，按 §2 推导（4 角色 × 8 组件 → 920 × 520）。
2. 表头行在 `y=72 h=52`。组件表头格白底，两行标签 `Component / vs. AD group`。角色横幅填充 `ink`，名称与 AD 组 code 为白字。
3. 数据行从 `y=140` 开始，步距 40，高 36。`rows_bottom = 140 + (n_components−1)·40 + 36`。
4. 组件标签格 `rx=4`，名称左对齐于 `x=24`，可选 `hint` 右对齐于 `x = comp_col_x + comp_col_w − 12`。
5. 每个值格 `rx=4`，描边 `ink @ 0.12` 0.6，填充与文本按其 `level` 匹配 §2.4。
6. 恰好**一个**焦点格（或零个）。焦点格描边 `accent` 宽 1.4。主值在 `y = row_y(k) + 18`；`sub`（若有）在 `y = row_y(k) + 30`。
7. 未出现在 `cells:` 中的格按 `level: "none"` 渲染，文本为 `none_label`（默认 `"No access"`）。
8. 自定义着色格 ≤ 2（焦点格之外）。
9. SVG 中任何位置都没有连接线元素。
10. 图例条在 `legend_y_top`，每个实际用到的 `level` 一个色样，上方一条发丝线分隔。
11. `viewBox_h` 随 `n_components` 增长；`viewBox_w` 随 `n_roles` 增长。

---

## 8. 反模式

- **焦点格超过一个** — 焦点存在的意义是标记*那一条*关键访问规则；>1 会抹掉信号。
- **任何位置的连接线** — 矩阵由值驱动；箭头属于 DP integration / 过程图。
- **自由发挥的 `level` 值** — 封闭词表是 `full | rw | read | none`。自由文本用 `value`，任意染色用 `color` 覆盖。
- **整行或整列的颜色染色** — `color` 只按格施加。整行/整列高亮容易过度强调，把矩阵压扁成一个列表。
- **把 `none_label` 当"TBD"占位符** — `none` 的意思是*无访问*。权限未知时，在输入中留空该格并在别处记录；不要渲染一个含糊状态。
- **角色超过 6 个** — 超过 6 列之前拆成两张矩阵（如人类角色 vs 服务账号）。
- **组件超过 14 个** — 超过 14 行之前按域拆分（存储 / 计算 / 可观测性 / 治理）。
- **用矩阵记录权限*如何*授予** — 那属于过程图或时序图。矩阵展示每个角色*能做什么*，不是授予流程。

---

## 9. 示例

- `assets/example-dp-security-matrix.html` — 极简浅色（NatStat 规范样例：4 角色 × 8 组件，焦点在 Data Consumers × Trino aggregated）。图库默认。
- `assets/example-dp-security-matrix-dark.html` — 同一张，暗色皮肤。
- `assets/example-dp-security-matrix-full.html` — 同一张，编辑卡片式外框 + 副标题 + 摘要卡片。

---

## 10. 完整 YAML：`example-dp-security-matrix.html` 的全部输入

映射到随附规范样例的完整输入。该 SVG 中的每个坐标都可由 §2 的公式作用于这些输入推导得出。

```yaml
title:    "Platform Access Matrix"
subtitle: "Four canonical groups × platform components"

roles:
  - { name: "Data Administrators", code: "DL-DataAdmins"      }
  - { name: "Data Engineers",      code: "DL-DataEngineers"   }
  - { name: "Data Scientists",     code: "DL-DataScientists"  }
  - { name: "Data Consumers",      code: "DL-DataConsumers"   }

components:
  - { name: "Keycloak",                          hint: "SSO" }
  - { name: "MinIO · raw bucket" }
  - { name: "MinIO · anon · staging · agg" }
  - { name: "Trino · raw catalog" }
  - { name: "Trino · anon-staging" }
  - { name: "Trino · aggregated" }
  - { name: "JupyterHub" }
  - { name: "NiFi" }

cells:
  # Row 0 — Keycloak
  - { row: 0, col: 0, value: "Admin", level: "full" }
  - { row: 0, col: 1, value: "Login", level: "read" }
  - { row: 0, col: 2, value: "Login", level: "read" }
  - { row: 0, col: 3, value: "Login", level: "read" }
  # Row 1 — MinIO raw
  - { row: 1, col: 0, value: "Full", level: "full" }
  - { row: 1, col: 1, value: "R/W",  level: "rw"   }
  - { row: 1, col: 2, value: "No access", level: "none" }
  - { row: 1, col: 3, value: "No access", level: "none" }
  # Row 2 — MinIO anon/staging/agg
  - { row: 2, col: 0, value: "Full", level: "full" }
  - { row: 2, col: 1, value: "R/W",  level: "rw"   }
  - { row: 2, col: 2, value: "Read", level: "read" }
  - { row: 2, col: 3, value: "No access", level: "none" }
  # Row 3 — Trino raw catalog
  - { row: 3, col: 0, value: "Full", level: "full" }
  - { row: 3, col: 1, value: "R/W",  level: "rw"   }
  - { row: 3, col: 2, value: "No access", level: "none" }
  - { row: 3, col: 3, value: "No access", level: "none" }
  # Row 4 — Trino anon-staging
  - { row: 4, col: 0, value: "Full",   level: "full" }
  - { row: 4, col: 1, value: "R/W",    level: "rw"   }
  - { row: 4, col: 2, value: "SELECT", level: "read" }
  - { row: 4, col: 3, value: "No access", level: "none" }
  # Row 5 — Trino aggregated (focal cell at col 3)
  - { row: 5, col: 0, value: "Full",        level: "full" }
  - { row: 5, col: 1, value: "R/W",         level: "rw"   }
  - { row: 5, col: 2, value: "SELECT",      level: "read" }
  - { row: 5, col: 3, value: "SELECT only", sub: "sole consumer access", focal: true }
  # Row 6 — JupyterHub
  - { row: 6, col: 0, value: "Admin", level: "full" }
  - { row: 6, col: 1, value: "R/W",   level: "rw"   }
  - { row: 6, col: 2, value: "R/W",   level: "rw"   }
  - { row: 6, col: 3, value: "No access", level: "none" }
  # Row 7 — NiFi
  - { row: 7, col: 0, value: "Admin", level: "full" }
  - { row: 7, col: 1, value: "R/W",   level: "rw"   }
  - { row: 7, col: 2, value: "Read",  level: "read" }
  - { row: 7, col: 3, value: "No access", level: "none" }

dark: false
```

### 10.1 这份 YAML 证明了什么

用这些输入运行 §2：
- `n_roles = 4`、`n_components = 8`，无颜色覆盖，一个焦点格。
- `viewBox_w = 12 + 208 + 12 + 4·148 + 3·16 + 48 = 920` ✓
- `row_y(k)` 产出 `140, 180, 220, 260, 300, 340, 380, 420` ✓
- `rows_bottom = 420 + 36 = 456`；`legend_y_top = 476`；`viewBox_h = 520` ✓
- `role_col_x(j) = [232, 396, 560, 724]` ✓
- 焦点格在 `(row=5, col=3)` → 矩形 `(724, 340, 148, 36)`，accent 描边 1.4 ✓

由这份 YAML 新生成一次，产出的图与随附的 `example-dp-security-matrix.html` 在视觉上无法区分。
