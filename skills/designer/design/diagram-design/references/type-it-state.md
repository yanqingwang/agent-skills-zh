> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-it-state.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# IT 现状图（IT current-state）

**最适用于：** 记录现代化提案的*改造前*图景：遗留 IT 版图按阶段或部门分组（采集 → 处理 → 传播，或前端 / 后端 / 存储，或调查 → 分析师 → 报表），标出痛点，标注基于文件的交接（CSV / Excel / Email / 拷贝），并让平台出现之前的工具可见。它是 `type-dp-integration.md` 的配套件：本类型展示数据平台提案将要填补的差距。

当利益相关方需要看到现有配置中的摩擦时使用：孤立的脚本、手工搬文件、缺失的版本控制、单点故障，以及从这些问题通往目标平台拓扑的路径。

本类型是**参数化的**：§1 的输入 schema 通过 §2 的公式驱动每一个坐标。规则形态沿用 `type-dp-integration.md`（区域 + 横切底栏）、`type-process.md`（圆角直角连接线）与 `type-medallion.md`（逐元素 `color` 覆盖），因此焦点规则、颜色覆盖、暗色模式与可复现清单在各类型间读法一致。

---

## 1. 输入：参数契约

```yaml
title:    "Current IT Landscape"
subtitle: "Data pipeline before the platform"
eyebrow:  "NatStat · Before the platform"

orientation: horizontal      # horizontal (default, zones L→R) | vertical (zones T→B)

zones:                       # 2..4 zones, ordered along the orientation axis
  - name: "COLLECTION"
    components:              # 1..5 components per zone
      - id: survey-solutions
        name: "Survey Solutions"
        sub:  "CAPI · PostgreSQL"
        icon: postgres               # any id from references/primitive-icons.md
        kind: standard               # standard | focal | external (external → dashed stroke)
      - { id: aspnet,    name: "ASP.NET Apps",    sub: "migration · admin portals", icon: server }
      - { id: civil-reg, name: "Civil Registry",  sub: "external · CRVS data",      icon: database, kind: external }
  - name: "PROCESSING"
    components:
      - { id: shared-drive,  name: "Shared Drive",     sub: "No version control · Windows file share", icon: file,      kind: focal }
      - { id: analyst-mach,  name: "Analyst Machines", sub: "SPSS · SAS · Stata · Excel",              icon: desktop }
      - { id: sql-server,    name: "SQL Server",       sub: "on-premises · core RDBMS",                icon: sqlserver, color: "#7a8c47" }  # custom olive
  - name: "DISSEMINATION"
    components:
      - { id: legacy-portal,   name: "LegacyPortal",      sub: "manual bottleneck",     icon: cloud,    kind: focal }
      - { id: natstat-website, name: "NatStat Website",   sub: "public · static pages", icon: internet }
      - { id: ministry,        name: "Ministry Partners", sub: "~6 ministries",         icon: users,    kind: external }

connectors:                   # ordered list; each links two component ids
  - { from: survey-solutions, to: shared-drive,   label: "CSV",     icon: csv,   style: link }
  - { from: aspnet,           to: shared-drive,   label: "EMAIL",   icon: file,  style: link }      # `mail` MISSING in catalog → falls back to `file`
  - { from: civil-reg,        to: shared-drive,   label: "EXCEL",   icon: excel, style: link, dashed: true }
  - { from: shared-drive,     to: analyst-mach,   label: "COPY",                 style: accent, dashed: true }
  - { from: analyst-mach,     to: sql-server,     label: "LOAD",                 style: neutral }
  - { from: analyst-mach,     to: legacy-portal,   label: "EXCEL",  icon: excel, style: accent }
  - { from: legacy-portal,    to: natstat-website, label: "WEB",                 style: neutral }
  - { from: natstat-website,  to: ministry,        label: "CSV DL", icon: csv,   style: link, dashed: true }

footer:                       # 0..3 optional full-canvas-width bars (cross-cutting concerns)
  - { name: "Identity Manager", sub: "Active Directory · LDAP · SSO", icon: active-directory }
  - { name: "Observability",    sub: "logs · metrics · alerts",       icon: monitoring }

legend:                       # auto-generated from styles used; user can override labels
  - { swatch: link,    label: "data flow" }
  - { swatch: accent,  label: "pain-point" }
  - { swatch: dashed,  label: "external" }
  - { swatch: focal,   label: "bottleneck" }

dark: false
```

**保留字段的语义：**

- `orientation` — `horizontal`（区域沿横轴从左到右排布，组件在每个区域内纵向堆叠）或 `vertical`（区域从上到下堆叠，组件在每个区域内横向排布）。
- `zones[i].name` — 大写短标签（≤ 14 字符）。以 `eyebrow` 角色渲染在区域框左上角，字距 0.14em，压在区域边框的一处纸色遮挡断口上。
- `components[i][k].id` — 全局唯一的 slug；被 `connectors[].from/to` 引用。
- `components[i][k].name` — `node-name` 角色（人类可读标签）。
- `components[i][k].sub` — `sublabel` 角色，10px，muted 色（技术性子标签；组件高度增长到 72 时可经自动换行占两行）。
- `components[i][k].icon` — `references/primitive-icons.md` 中的任意 id。缺失则不显示图标，名称左移。（目录共 41 个图标；`mail` 目前缺失，邮件交接请回退用 `icon: file`。）
- `components[i][k].kind` — `standard | focal | external`。`focal` 触发 accent 调色板（§5）；`external` 切换为 4-2 虚线描边与 muted 墨色，表示"这不在我们范围内"。
- `components[i][k].color` — 可选的逐组件颜色覆盖（§4）。在 `kind: focal` 上被忽略（accent 优先）。
- `connectors[k].from` / `connectors[k].to` — 指向某个组件 `id`。跨区域、跨行、同区域纵向、同区域横向都合法；走线方式由 §3 决定。
- `connectors[k].label` — 大写短文本（≤ 8 字符）。`arrow-label` 角色，9px，字重 600。
- `connectors[k].icon` — 可选的内联图标，位于文本左侧。与组件图标同一目录。
- `connectors[k].style` — `neutral | link | accent`。决定描边颜色与箭头标记。
- `connectors[k].dashed` — `true | false`。
- `footer[k]` — 可选的横切栏。横跨画布全宽减去边距。不从底栏引出任何连接线。
- `legend[k].swatch` — `link | accent | dashed | focal | neutral`。按图示实际用到的样式自动挑选；用户可重排或重命名。

---

## 2. 布局公式：确定性几何

```
# Horizontal orientation (default)
left_pad        = 16
right_pad       = 16
zone_gap        = 20
zone_y          = 52
zone_h          = 360
n_zones         = len(zones)

# Zone widths: base 200 + 24 per component to give vertical room for icons + 2-line subs.
# In the canonical example (3 / 3 / 3 components) the replication used 256 / 360 / 272 —
# the formula approximates that with hand-picked widths in the worked YAML (§10).
zone_w(i)       = base + n_components_i * comp_slack             # base ≈ 200, slack ≈ 24
viewBox_w       = left_pad + Σ zone_w(i) + (n_zones-1) * zone_gap + right_pad

# Component placement within zone i
comp_pad_x      = 20                                              # x-inset from zone border
comp_h          = 56                                              # 68 for focal (2-line sub), 72 if both sub lines present
comp_gap        = 32
comp_y(i, k)    = zone_y + 28 + k * (comp_h + comp_gap)

# Component centerlines (used for connector routing)
comp_x(i)       = zone_x(i) + comp_pad_x
comp_w(i)       = zone_w(i) - 2 * comp_pad_x
comp_cx(i)      = comp_x(i) + comp_w(i)/2
comp_cy(i, k)   = comp_y(i, k) + comp_h/2

# Footer bars (if present)
footer_bar_h    = 56
footer_gap      = 8
footer_top      = zone_y + zone_h + 24
footer_y(k)     = footer_top + k * (footer_bar_h + footer_gap)
footer_bottom   = footer_top + N_footer * (footer_bar_h + footer_gap) - footer_gap

# Total canvas height
legend_block_h  = 40
content_bottom  = N_footer > 0 ? footer_bottom : zone_y + zone_h
viewBox_h       = content_bottom + legend_block_h + 24
```

### 2.1 背景与区域框

`viewBox` 内铺满纯色纸底。无点阵。每个区域框：

```svg
<rect x="zone_x(i)" y="zone_y" width="zone_w(i)" height="zone_h"
      fill="{ink @ 0.02}" stroke="{ink @ 0.10}" stroke-width="0.8" rx="8"/>
<!-- paper-masked break for the zone label -->
<rect x="zone_x(i)+20" y="zone_y-8" width="{label_w}" height="16" fill="{paper}"/>
<text x="zone_x(i)+24" y="zone_y+4" fill="{soft}"
      font-family="{eyebrow}" letter-spacing="0.14em">{name}</text>
```

### 2.2 组件框

三种视觉形态：

| `kind` | 填充 | 描边 | 描边宽度 | 描边虚线 | 名称墨色 | 子标签墨色 |
| --- | --- | --- | --- | --- | --- | --- |
| `standard` | `#FFFFFF` | `ink` | 1 | — | `ink` | `muted` |
| `focal` | `accent @ 0.07` | `accent` | 1.4 | — | `ink` | `accent`（第 1 行）+ `muted`（第 2 行） |
| `external` | `#FFFFFF` | `muted` | 1 | `4,3` | `ink` | `muted` |

**图标摆放**（24×24，经 `currentColor` 单色化，见 `references/primitive-icons.md`）：

```svg
<g transform="translate(comp_x + 12, comp_y + (comp_h - 24)/2)" color="{ink_for_kind}">
  <use href="#icon-{name}"/>            <!-- or inline the SVG path from the catalog -->
</g>
```

图标占 24×24，加 12px 左内边距合计 36px 水平占用。名称与子标签基线右移 40px。

**名称与子标签基线**（左对齐，图标在左）：

```
name_x = comp_x + 44
name_y = comp_y + (comp_h/2) - 2
sub_y  = comp_y + (comp_h/2) + 14
```

### 2.3 连接线几何（走线规则见 §3）

```
src_right  = comp_x(i_src) + comp_w(i_src)
src_left   = comp_x(i_src)
src_top    = comp_y(i_src, k_src)
src_bot    = src_top + comp_h_src
src_cy     = src_top + comp_h_src/2

dst_left   = comp_x(i_dst)
dst_right  = comp_x(i_dst) + comp_w(i_dst)
dst_top    = comp_y(i_dst, k_dst)
dst_bot    = dst_top + comp_h_dst
dst_cx     = comp_cx(i_dst)
dst_cy     = dst_top + comp_h_dst/2

# Corridor x for cross-zone H+Q+V routing
corridor_x = dst_cx                            # land arrow on dst horizontal center, enter via top/bot
```

### 2.4 底栏

```svg
<rect x="left_pad" y="footer_y(k)" width="viewBox_w - 2*left_pad" height="footer_bar_h"
      fill="{ink @ 0.03}" stroke="{ink @ 0.18}" stroke-width="0.8" rx="8"/>
<g transform="translate(left_pad + 20, footer_y(k) + (footer_bar_h - 24)/2)" color="{ink}">
  <use href="#icon-{name}"/>
</g>
<text x="left_pad + 56" y="footer_y(k) + 24" font-family="{node-name}" font-size="14" fill="{ink}">{name}</text>
<text x="left_pad + 56" y="footer_y(k) + 40" font-family="{sublabel}" font-size="12" fill="{muted}">{sub}</text>
```

底栏是覆盖整个层面的服务。**绝不从底栏引出连接线。** 它们在视觉上位于区域下方，让读者一眼看到横切关注点。

### 2.5 图例条

在 `y = content_bottom + 16` 处一条发丝线分隔，然后在 `y = content_bottom + 36` 处一行色样与标签。只有 `connectors[]` 实际用到的样式（若存在 `focal` 与 `external` 组件种类，也加上这两种）出现在图例中。

---

## 3. 连接线规则（强制）

### 3.1 路径形态：圆角直角 Q 贝塞尔，r = 8

逐字沿用 `type-process.md` §3.1。绝不使用对角线。

```svg
<!-- Same zone, adjacent component (same vertical column): single vertical line -->
<line x1="{src_cx}" y1="{src_bot}" x2="{dst_cx}" y2="{dst_top}"
      stroke="…" stroke-width="…" marker-end="…"/>

<!-- Cross-zone or cross-row: exit right → H → Q-bend → V → enter top (or bottom) -->
<path d="M {src_right},{src_cy}  H {dst_cx - 8}  Q {dst_cx},{src_cy} {dst_cx},{src_cy ± 8}  V {dst_top_or_bottom}"
      fill="none" stroke="…" stroke-width="…" marker-end="…"/>
```

- 目的地在源下方时，用 `{src_cy + 8}` 与 `V {dst_top}`。
- 目的地在源上方时，用 `{src_cy − 8}` 与 `V {dst_bottom}`。

### 3.2 出边 / 入边侧（可配置；默认如下）

| 拓扑 | 源默认出边侧 | 目的地默认入边侧 |
| --- | --- | --- |
| 同区域，目的地在下方 | bottom | top |
| 同区域，目的地在上方 | top | bottom |
| 跨区域，水平流动 | right | top（或 bottom，取离 src_cy 更近者） |
| 纵向版式的图 | bottom | top |

连接线可经 `connectors[k].from_side` / `connectors[k].to_side` 覆盖（`top | right | bottom | left`）。**反向引用**（横向版式中的右→左、纵向版式中的向上）仅在至少一个端点为 `kind: external` 时允许，且必须 `dashed: true`。

### 3.3 标记必须贴住目标矩形

路径最后一段命令止于目标矩形边缘（`V {dst_top}` 或 `H {dst_left}`），**不是**质心。对标记应用 `refX=7` 后，三角正好贴住边框。线停在边缘之前，或指向质心把箭头埋进矩形内部，都算硬性失败。

### 3.4 样式 → 描边 + 标记

| `style` | 描边颜色 | 描边宽度 | 标记 |
| --- | --- | --- | --- |
| `neutral` | `muted` | 1.0 | `url(#arrow)` |
| `link` | `link` | 1.2 | `url(#arrow-link)` |
| `accent` | `accent` | 1.4 | `url(#arrow-accent)` |

`dashed: true` 时追加 `stroke-dasharray="4 3"`。

**Defs 块**（始终输出全部三个）：

```svg
<defs>
  <marker id="arrow"        markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{muted}"/></marker>
  <marker id="arrow-link"   markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{link}"/></marker>
  <marker id="arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{accent}"/></marker>
</defs>
```

### 3.5 连接线标签 = 内联图标 + 文本，置于连接线起点并带垂直边距

标签位于连接线**靠近源的一端**（不在中段），并**垂直于线段偏移**，因此永不压住描边。设置了 `icon:` 时，图标放在标签的纸色填充遮罩内、文本左侧。

```svg
<g transform="translate({label_cx}, {label_cy})">
  <rect x="-{w/2}" y="-9" width="{w}" height="18" rx="3" fill="{paper}" stroke="none"/>
  <use href="#icon-{icon}" x="-{w/2 + 4}" y="-6" width="12" height="12" color="{stroke_color}"/>     <!-- if icon set -->
  <text x="{icon ? (-(w/2) + 22) : 0}" y="3" text-anchor="{icon ? 'start' : 'middle'}"
        font-family="{arrow-label}" font-size="9" font-weight="600"
        letter-spacing="0.08em" fill="{stroke_color}">{label}</text>
</g>
```

**摆放公式**（标签盒高 18px × 宽 `w`；以 `{label_cx, label_cy}` 为中心）：

| 从源引出的线段 | `label_cx` | `label_cy` | 效果 |
| --- | --- | --- | --- |
| 水平（右出） | `src_right + 6 + w/2` | `src_cy − 14` | 标签在源之后 6px、线上方 5px |
| 水平（左出，反向） | `src_left − 6 − w/2` | `src_cy − 14` | 标签在源之前 6px、线上方 5px |
| 垂直（下出） | `src_cx + 6 + w/2` | `src_bot + 14` | 标签在线右侧 6px、源边缘下方 5px |
| 垂直（上出，反向） | `src_cx + 6 + w/2` | `src_top − 14` | 标签在线右侧 6px、源边缘上方 5px |

跨区域的 H+Q+V 路线中，标签绑定**水平**段，因为该段锚定在源上。把标签放在这段水平行程的靠前位置，绝不放在 Q 拐弯或垂直尾段上。

- `w = text_w + (icon ? 30 : 12)`，自动适配。
- 遮罩 `fill` 在浅色模式解析为 `paper`，暗色模式解析为 `ink`。遮罩作为安全垫保留：标签虽然不再压在线上，仍可能擦过区域背景与组件填充，遮罩保住了对比度。
- `stroke_color` 遵循 §3.4（文本与图标继承连接线的 accent / link / neutral 颜色）。

### 3.6 Z 顺序

所有连接线（路径 + 线段 + 标签）先于任何组件矩形输出，节点填充由此遮住线端。连接线标签是例外：它画在自己的线段之后，让遮罩盖在上面。

---

## 4. 组件颜色覆盖（逐组件 `color: "#hex"`）

逐组件，形态与本 Skill 中其他参数化类型一致。

| 元素 | 浅色 | 暗色 |
| --- | --- | --- |
| 容器填充 | `rgba(C, 0.06)` | `rgba(C_light, 0.10)` |
| 容器描边 | `rgba(C, 0.45)`（宽度 1） | `rgba(C_light, 0.55)` |
| 组件名称文本 | `C` | `C_light` |
| 图标字形 | 经 `currentColor` 继承墨色（不变） | 继承墨色（不变） |
| 子标签 | muted（不变） | muted（不变） |
| 触及该组件的连接线 | **不变**，由拓扑决定 | **不变** |

`C_light` = 同一十六进制色提亮约 15% 以保证暗色对比（如 `#7a8c47` → `#9aac67`、`#b85450` → `#d97a78`）。

**规则：**
- **绝不用于焦点组件。** `kind: focal` 始终按 accent 渲染；`color` 被静默忽略。
- **绝不用于连接线。** 连接线样式由拓扑决定；想要彩色边线，选 `style: accent` / `link` / `neutral`，而不是组件颜色。
- **上限：每图 ≤ 3 个自定义着色组件**（焦点组件之外）。超过 3 个，视觉信号就会碎片化。

**推荐的跨类型调色板**（与 `type-medallion.md` / `type-process.md` / `type-dp-integration.md` / `type-dp-security-matrix.md` 相同）：

- `#b85450` 铁锈红：非焦点的安全 / 治理 / 痛点
- `#5a7d9a` 石板蓝：可观测性 / 质量 / 监控门
- `#7a8c47` 橄榄绿：幸存系统（新平台保留的那一个工具）
- `#c9a23a` 暖黄：沙箱 / 开发 / 草稿
- `#8c6d3f` 暖棕：归档 / 冷数据 / 灾备

---

## 5. 焦点规则

- `kind: focal` 组件：**每图 ≤ 2 个**（没有单一主导痛点的图，0 个也合法）。
- 自动样式：accent 描边 1.4、accent 染色填充 7%、`node-name` 墨色加粗、`sublabel` 第一行用 accent。
- 任何端点为焦点组件的连接线自动以 `style: accent` 渲染；YAML 中的 `style:` 被忽略。
- 焦点组件上的自定义 `color: "#hex"` 被静默忽略：accent 永远优先。

如果你的图需要超过 2 个焦点组件，说明你把两条叙事压在了一起。拆分：一张"采集痛点"图 + 一张"传播痛点"图。

---

## 6. 暗色模式

| 角色 | 浅色 | 暗色 |
| --- | --- | --- |
| paper | `paper` | `ink` |
| ink | `ink` | `paper` |
| muted | `muted` | `muted` |
| accent | `accent` | `accent` |
| link | `link` | `link` |
| 区域背景 | `ink @ 0.02` | `paper @ 0.04` |
| 区域边框 | `ink @ 0.10` | `paper @ 0.14` |
| 标准组件填充 | `#FFFFFF` | `paper @ 0.04` |
| 标准组件描边 | `ink` | `paper @ 0.32` |
| 焦点填充 | `accent @ 0.07` | `accent @ 0.12` |
| 焦点描边 | `accent` | `accent` |
| 外部组件描边 | `muted`（虚线） | `muted`（虚线） |
| 底栏填充 | `ink @ 0.03` | `paper @ 0.05` |
| 底栏描边 | `ink @ 0.18` | `paper @ 0.20` |
| 标签遮罩填充 | `paper` | `ink` |
| 自定义颜色组件 | `C` | `C_light`（≈ +15%） |

---

## 7. 可复现清单（品味门槛）

输出 SVG 前，逐项核验：

1. 页眉 eyebrow + 标题 + 副标题位于规范 y 位置（24 / 36 / 52）；正文内边距 32px。
2. 2..4 个区域；每个区域的大写标签位于其区域框左上角，压在边框的一处纸色遮挡断口上。
3. 每个组件都有 `id`、`name`。`sub`、`icon`、`kind`、`color` 可选。
4. `kind: focal` 组件 ≤ 2 个；焦点样式自动应用（accent 填充 7%、accent 描边 1.4、第一行 sub 斜体）。
5. 每条连接线从源的右侧（或底部）出边，进入目的地的顶部（或左侧）；每个拐弯都用圆角直角 Q 贝塞尔 `r=8`；标记三角肉眼可见地贴住目标矩形边缘。
6. 连接线标签位于连接线**起点**（不在中段），并**垂直**于线段偏移（水平段上方留 5px 间隙，垂直段右侧留 6px 间隙），永不压住描边。文本背后保留纸色填充遮罩；设置了 `icon:` 时，图标在同一遮罩内、文本左侧。
7. 自定义着色组件 ≤ 3 个；焦点组件上不得使用。
8. 底栏 ≤ 3 条；每条横跨 `viewBox_w − 2*left_pad`；不从任何底栏引出连接线。
9. 图例在底部：发丝线分隔 + 每个实际用到的样式一个色样。
10. 连接线标签用 `arrow-label`，页眉 eyebrow 与区域标签用 `eyebrow`，页面标题用 `title`，副标题与组件名称用 `node-name`，技术性子标签用 `sublabel`。
11. 标记 `#arrow` / `#arrow-link` / `#arrow-accent` 在 `<defs>` 中只定义一次；不得内联定义标记。
12. 暗色变体：每个语义 token 都按其暗色值解析；自定义颜色提亮约 15%。

---

## 8. 反模式

- **对角箭头。** NatStat 复刻里有一条（analyst → LegacyPortal）。新类型禁止它：一律圆角直角 Q 贝塞尔。
- **标记没有贴住目标。** 路径止于质心，或停在边框之前。
- **不带遮罩矩形的内联 `text` 连接线标签。** 连接线会从文字下穿透，导致不可读。
- **标签压在连接线中段。** 标签应位于连接线*起点*并带垂直边距（见 §3.5）：埋在线中间会遮住源到目的地的方向感，还逼着读者的眼睛与遮罩打架。
- **用微小文本徽章当图标。** 源图用了 7px 的 `DB` / `APP` / `EXT` 徽章；本类型使用真实的 24px 目录图标。文本徽章只能充当标签文本，不能充当组件"图标"。
- **焦点组件上使用自定义颜色。** 焦点永远优先；`kind: focal` 上用户设置的 `color` 被静默忽略。
- **底栏接到某一个组件。** 底栏 = 横切整个层面的关注点；从底栏连一条线到特定组件是范畴错误（只有当底栏服务确实为*所有*组件做认证时，才可用 `type-dp-integration.md` 的 AUTH 线模式，且即便如此，线也应落在区域底边，而不是落到某个具体工具上）。
- **组件总数 > 16 或每区域 > 5 个。** 密度上限；拆成两张图。
- **一张图内混用两种版式。** 选定一种，`horizontal` 或 `vertical`，应用到所有区域。
- **用 `kind: focal` 标记每一个痛点。** 焦点只为 ≤ 2 个叙事痛点存在；对"这很糟但够不上头条"的情况，改用 `color: "#b85450"` 铁锈红。

---

## 9. 示例

- `assets/example-it-state.html` — 极简浅色（NatStat 规范样例：3 区域、9 组件、8 连接线、0 底栏，SQL Server 染橄榄绿）。图库默认。
- `assets/example-it-state-dark.html` — 同一张，暗色皮肤。
- `assets/example-it-state-full.html` — 同一张，编辑卡片式外框 + 摘要卡片。

---

## 10. 完整 YAML：`example-it-state.html` 的全部输入

映射到随附规范样例的完整输入。该 SVG 中的每个坐标都可由 §2 的公式作用于这些输入推导得出。

```yaml
title:    "Current IT Landscape"
subtitle: "Data pipeline before the platform"
eyebrow:  "NatStat · Before the platform"

orientation: horizontal

zones:
  - name: "COLLECTION"
    components:
      - { id: survey-solutions, name: "Survey Solutions", sub: "CAPI · PostgreSQL",          icon: postgres }
      - { id: aspnet,           name: "ASP.NET Apps",     sub: "migration · admin portals", icon: server   }
      - { id: civil-reg,        name: "Civil Registry",   sub: "external · CRVS data",      icon: database, kind: external }
  - name: "PROCESSING"
    components:
      - { id: shared-drive,  name: "Shared Drive",     sub: "No version control · Windows file share", icon: file,      kind: focal }
      - { id: analyst-mach,  name: "Analyst Machines", sub: "SPSS · SAS · Stata · Excel",              icon: desktop }
      - { id: sql-server,    name: "SQL Server",       sub: "on-premises · core RDBMS",                icon: sqlserver, color: "#7a8c47" }
  - name: "DISSEMINATION"
    components:
      - { id: legacy-portal,   name: "LegacyPortal",      sub: "manual bottleneck",     icon: cloud,    kind: focal }
      - { id: natstat-website, name: "NatStat Website",   sub: "public · static pages", icon: internet }
      - { id: ministry,        name: "Ministry Partners", sub: "~6 ministries",         icon: users,    kind: external }

connectors:
  - { from: survey-solutions, to: shared-drive,   label: "CSV",    icon: csv,   style: link }
  - { from: aspnet,           to: shared-drive,   label: "EMAIL",  icon: file,  style: link }
  - { from: civil-reg,        to: shared-drive,   label: "EXCEL",  icon: excel, style: link, dashed: true }
  - { from: shared-drive,     to: analyst-mach,   label: "COPY",                style: accent, dashed: true }
  - { from: analyst-mach,     to: sql-server,     label: "LOAD",                style: neutral }
  - { from: analyst-mach,     to: legacy-portal,   label: "EXCEL",  icon: excel, style: accent }
  - { from: legacy-portal,    to: natstat-website, label: "WEB",                 style: neutral }
  - { from: natstat-website,  to: ministry,        label: "CSV DL", icon: csv,   style: link, dashed: true }

dark: false
```

### 10.1 这份 YAML 证明了什么

- `n_zones = 3`，每区域组件数 `= [3, 3, 3]`，自定义颜色数 = 1（SQL Server），焦点数 = 2（Shared Drive、LegacyPortal），外部数 = 2（Civil Registry、Ministry Partners）。
- 规范样例中的区域宽度：256 / 360 / 272 ⇒ `viewBox_w = 16 + 256 + 20 + 360 + 20 + 272 + 16 = 960` ✓
- `viewBox_h = 52 + 360 + 40 + 24 = 500`（无底栏）✓
- Shared Drive（焦点）位于区域 2 第 0 行：`x = 340, y = 80, w = 264, h = 68`（焦点拉伸到 68 以容纳两行 sub）✓
- LegacyPortal（焦点）位于区域 3 第 0 行：`x = 704, y = 80, w = 208, h = 60` ✓
- SQL Server（自定义橄榄绿）位于区域 2 第 2 行：容器填充 `rgba(122,140,71,0.06)`，描边 `rgba(122,140,71,0.45)`，名称文本 `#7a8c47` ✓
- 连接线 4、5（区域 2 内）与 7、8（区域 3 内）是简单的纵向 `<line>` 元素。跨区域连接线走符合规则的路线（见 SKILL.md §6 规则 4 与 5）：
  - **三条 Survey 一侧 → Shared Drive 的连接线（C1 / C2 / C3）都从 Shared Drive 的左边缘进入。** 从顶边进入会把标记主体（沿行进方向向后 7px，因为 `refX = 7`）推进目标盒*内部*，那里的纸色填充遮罩会把它藏起来，只有 1 像素尖端露在描边上方。以向右的路径从左边缘进入，标记主体留在盒外、箭头可见（盒边缘左侧约 7px 可见）。三个左边缘挂点在 **y = 108 / 124 / 140** 扇形展开（16px 间距，远高于规则 4 的 12px 最小值）。
  - **C1**（Survey → Shared Drive）源 y 与落点 y 一致：单一水平段 `M 252,108 H 340`，无需拐弯。
  - **C2**（ASP.NET → Shared Drive）向上绕行穿过区域 2 背景，垂直段在 `x = 316`（避开 `x = 340` 处 Shared Drive 的左边缘）：`H 308 Q 316,196 316,188 V 132 Q 316,124 324,124 H 340`。落在 `(340, 124)`。
  - **C3**（Civil Registry → Shared Drive）向上绕行穿过区域 2 背景，垂直段在 `x = 332`（避开 `x = 340` 起始的 Analyst Machines）：`H 324 Q 332,284 332,276 V 148 Q 332,140 340,140`。经最后一个 Q 拐弯落在 `(340, 140)`（无需收尾的 H）。
  - **C6**（Analyst Machines → LegacyPortal）无法用直接的 H+Q+V 进入 LegacyPortal 左边缘：Analyst Machines 与 LegacyPortal 不同行，`y = 268` 的直接水平线会穿过 NatStat Website。它绕经区域间隙并从 LegacyPortal **上方**通过：`H 654 Q 662,268 662,260 V 72 Q 662,64 670,64 H 800 Q 808,64 808,72 V 80`。垂直段在 `x = 662`（区域间隙内），水平段在 `y = 64`（LegacyPortal 顶部之上），然后向下进入 LegacyPortal 顶部中心。路径从**上方**向下进入 LegacyPortal，箭头主体因此位于盒上方（可见），只有 1px 尖端进入盒内。

**标记可见性经验法则：** 使用标准箭头标记（`markerWidth = 8`、`refX = 7`）时，箭头主体从端点沿路径方向*向后*延伸 7px。要让箭头可见，这 7px 尾部必须落在目标盒*之外*。换算成各进入方式：
- 从**顶边向上进入**（路径方向朝上，盒在其下方）→ 主体在盒内，**仅 1px 可见。避免这种进入方式。**
- 从**顶边向下进入**（路径方向朝下，盒在其下方）→ 主体在盒上方，约 7px 可见。✓
- 从**左边缘向右进入** → 主体在盒左侧，约 7px 可见。✓
- 从**右边缘向左进入** → 主体在盒右侧，约 7px 可见。✓
- 从**底边向下进入**（盒在其上方）→ 主体在盒内，**仅 1px 可见。避免这种进入方式。**
- 从**底边向上进入**（盒在其上方）→ 主体在盒下方，约 7px 可见。✓

当源所在行与目标行的 y 区间重合时（如 Survey 的 y=108 对 Shared Drive 的 y=80–148），优先**侧边**进入：单一水平路径，箭头完全可见。源行错开时，绕经目标最近的区域背景从侧边进入，而不是从错误一侧接近顶边/底边。

添加底栏后（`N_footer > 0`），`viewBox_h` 按 §2 的画布公式增长，以容纳底栏行与自定义颜色。
