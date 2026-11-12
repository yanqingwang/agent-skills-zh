> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-medallion.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Medallion（奖牌架构图）

**最适用于：**记录多级的存储布局，其中每一级都是同一数据集的一个不同的*质量/访问级别*，典型为：原始落地区、匿名化、staging/清洗、聚合业务指标、冷归档。当读者需要一眼看清*每个桶里有什么*、*谁在写*、*用什么工具与格式*，以及*数据如何在层级间晋升*时使用。

若主题是带角色泳道的工作流，改用 **Process**。若主题是集群架构而非存储分层组织，改用 **High-Level**。

该类型是**参数化的**：§1 的输入 schema 经 §2 的公式驱动每一个坐标。同一输入的两次生成必须产出视觉完全一致的 SVG。规则形态与 `type-process.md`、`type-data-flow.md` 镜像一致，因此颜色覆盖、焦点规则与可复现性检查清单在各类型间读法相同。

---

## 1. 输入：参数契约

```yaml
title:    "Five-Tier Medallion Architecture"
subtitle: "Quarterly survey through Raw → Anonymized → Staging → Aggregated → Archive"

tiers:                                # 3..6 tier columns, ordered left → right
  - { name: "Raw",        bucket: "raw-bucket",        style: "outer",
      fields: { tool: "NiFi · raw write",          format: "CSV · Parquet · JSON", writer: "Data Engineer",
                example: ["Q1 dump · w/ PII", "verbatim CAPI export"] } }
  - { name: "Anonymized", bucket: "anon-bucket",       style: "default",
      fields: { tool: "Trino INSERT",              format: "Iceberg · partitioned", writer: "Data Engineer",
                example: ["no name · address", "stable household ID"] } }
  - { name: "Staging",    bucket: "staging-bucket",    style: "default",  color: "#c9a23a",   # warm yellow — analytical working zone
      fields: { tool: "Trino · JupyterHub",        format: "Iceberg · cleaned",     writer: "Data Scientist",
                example: ["weighted records", "harmonised codings"] } }
  - { name: "Aggregated", bucket: "aggregated-bucket", style: "focal",  focal: true,
      fields: { tool: "Trino INSERT · SAS JDBC",   format: "Iceberg · indicators",  writer: "Data Scientist",
                example: ["unemployment rate", "labour participation"] } }
  - { name: "Archive",    bucket: "archive-bucket",    style: "cold",
      fields: { tool: "MinIO lifecycle",           format: "cold tier · immutable", writer: "Data Administrator",
                example: ["historical Q1–Q4 sets", "5+ years retained"] } }

example_label: "Quarterly survey example" # bottom field label (varies per domain)

promotions:                           # adjacent-tier arrows; len = n_tiers - 1
  - { from: 0, to: 1, label: "PII REMOVE",    style: "normal"    }
  - { from: 1, to: 2, label: "CLEAN+WEIGHT",  style: "normal"    }
  - { from: 2, to: 3, label: "AGGREGATE",     style: "focal"     }    # auto-accent because target is focal
  - { from: 3, to: 4, label: "LIFECYCLE",     style: "lifecycle" }    # dashed

paths:                                # 0..2 write-method cards at the bottom (optional)
  - { tag: "SQL PATH",      title: "Trino INSERT INTO … SELECT",
      sub: "filter · reshape · join · aggregate — set-based transforms" }
  - { tag: "NOTEBOOK PATH", title: "DuckDB + Python/R in JupyterHub",
      sub: "stats · ML · interactive analysis — row-iterative work" }

dark: false
```

**保留字段语义：**
- `tiers[i].style`：取 `outer`、`default`、`focal`、`cold` 之一。决定卡片的填充/描边配色（§2.4）。
- `tiers[i].focal: true`：只能有**一个**层级声明此项。它把 `style` 覆盖为 `focal`，并把指向该级的晋升箭头自动切换为 `focal`。
- `tiers[i].fields`：`{tool, format, writer, example}`。`example` 是 1–2 项的列表；小节标题使用 `example_label`。
- `tiers[i].color`：可选的每级 `"#hex"` 颜色覆盖。见 §4。
- `promotions[].style`：`normal` | `focal` | `lifecycle`。连线规则（§3）把每种样式绑定到固定的笔画/虚线/marker。
- `paths`：0–2 项。为 0 时省略底部行，`viewBox_h` 相应缩小。

---

## 2. 布局公式：确定性几何

```
# Tier dimensions
tier_w           = 172
tier_h           = 380
tier_gap         = 16
left_pad         = 16
right_pad        = 100
n_tiers          = len(tiers)

# Canvas
viewBox_w        = left_pad + n_tiers * tier_w + (n_tiers - 1) * tier_gap + right_pad
                                                    # 5 tiers → 16 + 860 + 64 + 100 = 1040
arc_band_h       = 80                               # space above tiers reserved for promotion arcs
path_h           = 56
path_gap         = 16                               # gap between tier row and path row
bottom_pad       = 16
viewBox_h        = arc_band_h + tier_h + (path_gap + path_h if paths else 0) + bottom_pad
                                                    # with paths → 80+380+72+16 = 548
                                                    # without paths → 80+380+16 = 476

# Tier positions
tier_x(i)        = left_pad + i * (tier_w + tier_gap)    # 16, 204, 392, 580, 768
tier_y           = arc_band_h                            # 80 — tier tops sit just below the arc band
tier_cx(i)       = tier_x(i) + tier_w/2                  # 102, 290, 478, 666, 854

# Promotion arcs (between adjacent tiers — over the top, anchored at tier top-centers)
arc_src_x(i)     = tier_cx(i)                            # top-center of tier i      (102, 290, 478, 666)
arc_dst_x(i)     = tier_cx(i+1)                          # top-center of tier i+1    (290, 478, 666, 854)
arc_peak_x(i)    = (arc_src_x(i) + arc_dst_x(i)) / 2     # midpoint                  (196, 384, 572, 760)
arc_label_y      = 50                                    # label sits inside the arc, 30px below tier top

# Path row (bottom)
path_y           = tier_y + tier_h + path_gap            # 476
path_w           = (viewBox_w - 2*left_pad - path_gap) / 2 if len(paths) == 2 else (viewBox_w - 2*left_pad)
                                                          # Canonical 5-tier shape uses path_w=460 explicitly (see §2.5)
```

### 2.1 背景

整个 viewBox 用纯色 paper 填充。无点状纹理。

### 2.2 层级卡片（172 × 380）

每级渲染为圆角矩形卡片：一条着色的头部色带、居中的桶名、四行带标签的字段，以及底部附近独立的 `example_label` 小节。

```
tier_x(i),  tier_y       =  card top-left  (tier_y = 80, just below the arc band)
header_band_h            = 40            # band from y=tier_y to y=tier_y+40 (i.e., 80..120)
header_band_extra        = 10            # 10-px extension below band, same tint

# Inside the card (absolute y; tier_y = 80):
title_text            at (tier_cx(i), 106)                # node-name role, 13px, weight 700, ink
bucket_text           at (tier_cx(i), 144)                # sublabel role, muted (accent on focal tier)

field_x               = tier_x(i) + 16                    # 16-px left inset for field text
field_w               = 140                               # 172-px tier_w minus two 16-px insets
field rows (absolute y):
  tool_label  at 180,    tool_value  at 186 (foreignObject, height 24)
  format_label at 220,   format_value at 226 (foreignObject, height 24)
  writer_label at 260,   writer_value at 266 (foreignObject, height 24)
  # gap (open whitespace below writer row, above the example section)
  example_label_text at 360,  example_line_0 at 374,  example_line_1 at 388
```

**字段值换行规则：**字段值（tool / format / writer）渲染在 SVG `<foreignObject>` 内的 HTML `<div>` 中，文本超过 140 px 时自动换行。每个 `foreignObject` 为 140 宽 × 24 高（`sublabel` 角色、1.25 行高下可容纳 2 行）。到下一个字段标签的 26 px 间隙正好吸收第二行。

```svg
<foreignObject x="{field_x}" y="{value_top}" width="140" height="24">
  <div xmlns="http://www.w3.org/1999/xhtml"
       style="font-family: {sublabel}; color: {muted}; line-height: 1.25;">
    {field_value}
  </div>
</foreignObject>
```

`<div>` 上的 HTML 命名空间声明是 SVG 渲染内联内容的必要条件。浏览器与 Playwright/Chromium 都能如实渲染；若导出目标不支持 `<foreignObject>`（部分旧版 Inkscape），改为手工把长值拆成两行 `<tspan>`。

字段标签用 `node-name` 角色、11px、ink 色。字段值用 `sublabel` 角色、muted 色。桶名与字段值可被 `color` 覆盖重新着色（§4）。

### 2.3 层级样式

四种规范样式，通过 `tiers[i].style` 按级选择。`style` 省略时的默认映射：第 0 级 → `outer`，最后一级 → `cold`，焦点级（若有）→ `focal`，其余 → `default`。

| `style` | 卡片填充 | 卡片描边 | 头部色带填充 | 桶名文字 | 示例值文字 |
|---|---|---|---|---|---|
| `outer` | `#FFFFFF` | `muted` 1.0 solid | `muted @ 0.10` | `muted` | `muted` |
| `default` | `#FFFFFF` | `ink` 1.0 solid | `ink @ 0.06` | `muted` | `muted` |
| `focal` | `accent @ 0.07` | `accent` 1.6 solid | `accent @ 0.14` | `accent` | `accent` |
| `cold` | `paper-2` | `muted` 1.0 dashed `5,3` | `muted @ 0.18` | `muted` | `muted` |

所有卡片矩形 `rx = 6`。

**焦点样式说明：**焦点级的 accent 处理会级联：桶名与示例值行都用 accent 渲染。其余字段值（tool/format/writer）保持 muted；只有桶名与示例数据承载焦点信号，避免层级卡片整个淹没在珊瑚色里。

### 2.4 晋升弧线（从层级顶部上方跨过）

每条晋升线都是**三次贝塞尔弧**，锚定在相邻两级的**顶部中心**，即 `(tier_cx(i), tier_y)` 到 `(tier_cx(i+1), tier_y)`。弧线升入卡片上方 80 px 的 `arc_band`，峰点约在 y ≈ 20。连线与其标签始终完全可见：不用 paper 遮罩，也不与卡片内容重叠。

```svg
<path d="M {tier_cx(i)},{tier_y} C {tier_cx(i)},0 {tier_cx(i+1)},0 {tier_cx(i+1)},{tier_y}"
      fill="none" stroke="…" stroke-width="…" marker-end="…"/>
```

规范 5 级形状下的具体值（`tier_y = 80`，层级中心 x = 102, 290, 478, 666, 854）：
- 0→1: `M 102,80 C 102,0 290,0 290,80`
- 1→2: `M 290,80 C 290,0 478,0 478,80`
- 2→3: `M 478,80 C 478,0 666,0 666,80`  （focal：accent）
- 3→4: `M 666,80 C 666,0 854,0 854,80`  （lifecycle：虚线）

三次曲线几何：锚点 y = 80（层级顶部），控制点 y = 0（viewBox 顶部）。t=0.5 处曲线峰点 y ≈ 20（由 `0.125·80 + 0.375·0 + 0.375·0 + 0.125·80 = 20` 算得）。每条弧横跨一个完整层步距（规范布局下 188 px），使连线有清晰可见的纵向起伏。

**marker 朝向：**带 `orient="auto"` 的 `marker-end` 会把箭头旋转到与端点处路径切线一致。控制点正对锚点上方，因此落点处切线竖直向**下**，箭头干净地扎进第 *i+1* 级的顶部中心，指向头部色带。

**链式锚点：**相邻弧共享交汇点（弧 0→1 的终点正是弧 1→2 的起点 `(tier_cx(1), 80)`）。视觉上每级的顶部中心像一个"关节"：数据到达卡片顶部，在内部被加工，再从顶部出发去往下一级。箭头俯冲与下一条弧的直线爬升读起来像一次完整的数据交接动作。

| `style` | 笔画 | 宽度 | 虚线 | Marker |
|---|---|---|---|---|
| `normal` | `muted` | 1.4 | — | `arrow` |
| `focal` | `accent` | 1.6 | — | `arrow-accent` |
| `lifecycle` | `muted` | 1.4 | `4,3` | `arrow` |

**自动样式规则：**
- 若 `promotions[k].to` 指向**焦点级**，样式自动升为 `focal`（accent、宽 1.6、`arrow-accent` marker）。
- 若 `promotions[k].to` 指向带 **`color` 覆盖**（§4）的级，箭头继承该十六进制色：笔画 = `C`，标签填充 = `C`，marker-end 使用同色 marker（如 `#c9a23a` 对应 `arrow-yellow`）。宽度保持 1.4：颜色覆盖是"关注点"信号，不是焦点晋升。lifecycle/虚线箭头保留虚线但改用该色。
- 两者同时成立时焦点优先（被标为焦点的着色级仍用 accent）。

**弧内标签：**
- 锚定在 `(arc_peak_x(k), arc_label_y)` = `((arc_src_x + arc_dst_x) / 2, 50)`。
- `arrow-label` 角色、10px、`letter-spacing=0.08em`、全大写。颜色与箭头笔画一致。
- **无需遮罩矩形**：三次曲线峰点在 y ≈ 20，标签位于 y=50，远低于曲线。标签悬浮在弧线*围出*的空旷区域里，弧线本身作视觉边框，读作"X 变换为 Y"。

层级间隙更小（`tier_gap` 被覆盖到低于默认 16 px）时，弧的锚点内缩量 `arc_inset` 可能需要相应收缩，以保证弧线可见。

### 2.5 路径行（底部，可选）

最多 **2** 张写入方式卡片。规范 5 级形状（`arc_band_h = 80`）下：

```
path_y      = 476       # tier_y + tier_h + path_gap = 80 + 380 + 16
path_h      = 56
path_x[0]   = 16
path_w[0]   = 460
path_x[1]   = 16 + 460 + 16 = 492
path_w[1]   = 460
```

（尽管 viewBox 为 1040，两条路径都落在 460 宽：右侧留白取自卡片层条带，而非路径条带。规范 5 级形状保持 `path_w=460`。其他级数按 `path_w = (viewBox_w - 2*left_pad - path_gap) / 2` 推导。）

每张卡片的内容：
- 容器矩形：白色填充、`ink @ 0.20` 描边宽 1、`rx=6`。
- 标签片：矩形位于 `(path_x + 8, path_y + 6)`，`h=12 rx=2`，透明填充，`ink @ 0.30` 描边宽 0.8。标签文字居中，用 `eyebrow` 角色、letter-spacing 0.08em、ink 色。
- 标题在 `(path_x + 80, path_y + 30)`：`node-name` 角色、11px、ink。
- 副文本在 `(path_x + 80, path_y + 46)`：`sublabel` 角色、muted。

---

## 3. 连线规则（强制）

三种样式，绑定到拓扑。与 `type-process.md` §3 镜像，条文读法一致。

```svg
<defs>
  <marker id="arrow"        markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{muted}"/></marker>
  <marker id="arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{accent}"/></marker>
  <!-- Per-color markers: declare one per custom tier color in use. -->
  <marker id="arrow-yellow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#c9a23a"/></marker>
</defs>
```

图中每用到一个 `color` 覆盖，就新增一个 `<marker>`。命名约定为 `arrow-{semantic}`（如 `arrow-yellow`、`arrow-slate`、`arrow-red`），与推荐调色板对应，marker id 在源码中一目了然。

**绘制顺序：**晋升弧画在**任何**层级卡片矩形**之前**，卡片叠在上层，弧线的出头部分被卡片内部遮住。

**弧形规则：**medallion 的晋升线永远是跨过层级条带**顶部的三次弧**，锚定在源级与目标级的**顶部中心**；控制点在锚点正上方 y=0 处。不用"从间隙穿过"的水平线：弧线走顶部，才能让连线与标签同时清晰可见。

---

## 4. 组件颜色覆盖

任何层级或路径条目都可接受可选的 `color: "#hex"`。与 `type-process.md` §4 / `type-data-flow.md` §4 镜像。

### 4.1 每级 `color`

应用到：

| 元素 | 浅色 | 暗色 |
|---|---|---|
| 卡片填充 | `rgba(C, 0.07)` | `rgba(C_light, 0.10)` |
| 卡片描边 | `C`（宽 1.4） | `C_light`（宽 1.4） |
| 头部色带填充 | `rgba(C, 0.14)` | `rgba(C_light, 0.18)` |
| 标题文字 | ink（不变，标题保持可读） | ink（不变） |
| 桶名文字 | `C` | `C_light` |
| 示例值 | `C` | `C_light` |
| 字段标签 / 字段值 | **不变**（ink / muted） | **不变** |
| 触及该级的连线 | **不变**：由拓扑决定 | **不变** |

`C_light` 是同一十六进制色提亮约 15%，用于暗色模式对比度。

### 4.2 每条路径 `color`

把路径卡片的描边替换为 `rgba(C, 0.45)`，标签片描边替换为 `rgba(C, 0.55)`。标签文字与标题文字用 `C`。副文本保持 muted。

### 4.3 规则

- **焦点层禁用。**accent 已承载该信号，焦点级上的 `color` 会被忽略。
- **`cold` 级的虚线处理上不再叠加。**二者选一：虚线冷层或自定义颜色，不能两者都有。
- 每张图最多 **2 个自定义着色元素**（层级或路径），焦点级不计入。
- **晋升箭头继承目标级的颜色**（§3 自动样式规则）。Staging 级设 `color: "#c9a23a"` 意味着落进 Staging 的 CLEAN+WEIGHT 弧也用黄色渲染：连线、标签、箭头三者同色。这保证视觉连贯：着色级与其入流读作同一个"关注点"组。箭头**不会**继承源级颜色，只继承目标级；因此从着色级*发出*的弧回退为 muted（或下一目标级的颜色/样式）。

### 4.4 语义调色板（推荐）

与其他参数化类型同一套调色板，读者在多张图之间扫读时，同一种颜色始终意味着同一件事：

- `#b85450` 锈红：安全/身份/治理（含 PII 的层级、审计层级）
- `#5a7d9a` 青灰蓝：可观测性/质量（已校验的层级、受监控区域）
- `#7a8c47` 橄榄绿：数据产品/发布（面向消费方的聚合、公开发布层级）
- `#c9a23a` 暖黄/金：分析/工作区（staging 层、科学家沙盒、中间计算面）
- `#8c6d3f` 暖棕：备份/灾备/归档（冷层样式的替代方案）

---

## 5. 焦点规则

每张图恰好**一个**焦点级。默认取输入中标记了 `focal: true` 的级；若无标记，默认取分析枢纽级（通常是 `Aggregated`，或下游消费方查询的那一级）。

焦点级：
- 使用 `style: focal`（accent 填充 + 描边 1.6 + accent 头部色带）。
- 桶名与示例值行以 accent 渲染。
- 其**入向**晋升箭头自动升为 `style: focal`（accent）。
- 其**出向**晋升箭头（若有，通常指向冷归档）保持用户声明的样式（通常为 `lifecycle` 虚线）。

带有 `focal: true` 的级为 0 个或多于 1 个时，停下询问用户。

---

## 6. 暗色模式

| Token | 浅色 | 暗色 |
|---|---|---|
| Paper | `paper` | `ink` |
| Ink | `ink` | `paper` |
| Muted | `muted` | `soft` |
| Accent | `accent` | `accent` |
| Fog（冷级填充） | `paper-2` | `paper @ 0.06` |
| White（默认卡片填充） | `#FFFFFF` | `paper @ 0.04` |
| 卡片描边 ink（default 样式） | `ink` | `paper @ 0.30` |
| 头部色带 ink 色调 | `ink @ 0.06` | `paper @ 0.08` |
| 头部色带 muted 色调 | `muted @ 0.10` | `soft @ 0.16` |
| 头部色带冷色调 | `muted @ 0.18` | `soft @ 0.24` |
| 头部色带 accent 色调 | `accent @ 0.14` | `accent @ 0.20` |
| 自定义组件色 | `C` | `C_light`（提亮约 15%） |

---

## 7. 可复现性检查清单（品味门禁）

输出 SVG 前，逐项核验**全部**条目：

1. `viewBox = "0 0 {viewBox_w} {viewBox_h}"` 按 §2 推导（5 级 + 2 路径 → 1040 × 548）。
2. 每张层级卡片位于 `(tier_x(i), 80)`，尺寸 `172 × 380`，`rx=6`。
3. 层级头部色带填充 `(tier_x(i), 80, 172, 40)`，色带下另有 10 px 延伸。
4. 恰好**一个**焦点级；其入向弧自动套用 `focal` 样式。
5. 晋升弧渲染为跨相邻级顶部的三次贝塞尔曲线；锚点 `(tier_cx(i), 80)` → `(tier_cx(i+1), 80)`，控制点 y=0。标签置于弧内 `(arc_peak_x, 50)`，无遮罩。
6. 仅当 `len(paths) > 0` 才有底部路径行。卡片在 `y=476`，高 56。
7. 除焦点级外，自定义组件色 ≤ 2 个。箭头永不自定义着色。
8. 全部晋升弧与标签遮罩都在**任何**层级矩形之前输出（绘制顺序规则：卡片把线端遮在卡内）。
9. 焦点级的桶名与示例值用 accent 渲染，其余保持 muted。
10. 每张层级卡片与路径卡片 `rx=6`；标签片 `rx=2`。

---

## 8. 反模式

- **焦点级多于一个**：焦点用于标记中央分析面，超过一个就抹掉了信号。
- **非归档级用 cold 样式**：虚线雾面外观专属于保留/归档层级。
- **双向晋升箭头**：晋升永远从左向右流动。回流（如聚合写回 raw）不属于此类型；换一种图。
- **箭头自定义着色**：连线由拓扑驱动，层级的颜色绝不蔓延到其边上。
- **用路径卡片解释层级语义**：路径描述的是*写入方式*（数据如何在层级间移动），不是每级存了什么。如果你在路径卡片里写下 "Raw stores …"，这段内容应放进 Raw 级的字段。
- **缺失 `example_label` 内容**：每级都应展示具体的示例数据（季度调查行、客户记录、理赔单……）。没有它，图表会变得抽象，不再配得上它占的空间。
- **晋升箭头标签超出层级间隙标签遮罩**：标签保持 ≤ 14 字符、`arrow-label` 角色、全大写。长动词（"CALCULATE & SUMMARIZE"）会破坏节奏；缩短为 "AGGREGATE"，或拆成两张图。

---

## 9. 示例

- `assets/example-medallion.html`：极简浅色（NatStat 季度调查：5 级、2 张路径卡片、Aggregated 为焦点）。画廊默认。
- `assets/example-medallion-dark.html`：同上，暗色皮肤。
- `assets/example-medallion-full.html`：同上，编辑卡片式外框，带副标题 + 摘要卡片。

---

## 10. 完整 YAML 实例

§1 的 YAML 就是随库发布的 `example-medallion.html` 的**完整**输入定义。该文件 SVG 中的每个坐标都可用 §2 的公式对这些输入推导得出。同一段 YAML 也以文件头部 HTML 注释的形式嵌在 `example-medallion.html` 里，查看源码时参数化输入就显示在 SVG 正上方。
