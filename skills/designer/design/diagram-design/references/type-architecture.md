> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-architecture.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 架构图（Architecture）

**适用场景：** 系统总览、数据流图、集成地图、基础设施拓扑。

## 版式约定
- 按层或信任边界分组组件（前端 → 后端 → 数据；公网 → 内网）。
- 主流向从左到右或自上而下。选定一个并贯彻到底。
- 先画箭头后画方框，让 z 序把连线压在组件后面。
- 1–2 个 coral 焦点节点：主集成点、主数据存储，或关键判定节点。
- 虚线边界矩形标记区域（VPC、安全组、信任区）；标签放在边界线上纸色遮罩之上。

## 连接线风格

**圆角直角（正交）连接线是强制的**，适用于一切非水平/垂直连接——离轴节点之间的斜 `<line>` 是硬失败（见 SKILL.md §6 强制连接线规则）。两折肘形路径，`r=8`：

```svg
<!-- right+down: from (x1,y1) to (x2,y2), mid = (x1+x2)/2 -->
<path d="M x1,y1 H mid-8 Q mid,y1 mid,y1+8 V y2-8 Q mid,y2 mid+8,y2 H x2"
      fill="none" stroke="…" stroke-width="1.2" marker-end="url(#arrow)"/>
```

右+向上时翻转垂直方向的符号。只有端点共享同一 x 或 y 时才用纯 `<line>`。箭头标签放在垂直线段上，水平对齐 `mid`，垂直居中于两个拐角之间。

**垂直连接线的挂点选择。** 终点明显在起点上方或下方时，从终点的上边或下边进入。用单折 L 形路径：从面向目标列的侧边离开源，水平前进，折一次，再垂直进入终点：

```svg
<!-- destination above source: leave the source's right edge at (x_right, y_port), enter the destination's bottom edge at x2 -->
<path d="M x_right,y_port H x2-8 Q x2,y_port x2,y_port-8 V y_dst"
      fill="none" stroke="…" stroke-width="1.2" marker-end="url(#arrow)"/>
```

每条线段都垂直于它出发的那条边离开方框。绝不要从上边或下边出发水平线段：它会沿着边框走、藏在节点填充后面，箭头看起来像从拐角里长出来。两条这样的连接线从同一条侧边出发时，扇开它们的挂点（primitives-core.md 规则 4），每个挂点距拐角至少 8px，避免落在拐角圆弧上。

目标的左右挂点留给以水平为主的连接。主要垂直的路径却从侧面进入节点，看起来像箭头戳穿了节点面，而不是从上或从下抵达。

**虚线路径：同一路由规则。** 可选、返回、异步与被动流使用 `stroke-dasharray="4,3"` 与更轻的描边（`stroke-width="1"`）。套用与实线路径**相同的正交路由、挂点选择与桥/跳规则**：虚线图案只表达语义轻重，不是另一套路由语法。虚线路径与实线路径必须交叉时，桥虚线那条（它按定义是较不重要的连接）。

**分区标签边距。** 分区眉标签底部与首个被包含节点顶部之间留 ≥16px。分区 rect 要足够高以容纳这段头部间隙（分区 `y` = node_top − 32；标签遮罩 `y` = zone_y + 4）。

## 交叉箭头：桥 / 跳线

两条正交箭头必须交叉时，在**较不重要**的箭头上、于交叉点处加一个小弧（hop/bridge）。较重要的箭头不间断绘制。

```svg
<!-- Horizontal hop over a vertical crossing at x=cx, on a line at y -->
<path d="M x1,y H cx-8 a 8,8 0 0,1 16,0 H x2"
      fill="none" stroke="…" stroke-width="1.2" marker-end="url(#arrow)"/>
```

`a 8,8 0 0,1 16,0` 是 SVG 弧：rx=ry=8、large-arc=0、sweep=1（视觉上向上拱起），向右推进 16px——在交叉处形成一个半径 8px 的半圆形凸起。垂直方向跨过水平线时，在垂直路径上用 `a 8,8 0 0,0 0,16`。

决定桥哪支箭头：桥语义上较不重要的那支（被动、次要、回写），或描边更轻的那支（虚线、muted）。绝不两支都桥。

## 分区分组

把服务于同一层或信任边界的 2 个以上节点用一个分区 rect 归组：在箭头与节点**之前**绘制（z 序：bg → zones → arrows → nodes）：

```svg
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8"
      fill="{ink @ 0.02}" stroke="{ink @ 0.10}" stroke-width="0.8"/>
<rect x="{label_x}" y="{y+4}" width="{label_w}" height="12" rx="2" fill="{paper}"/>
<text x="{label_cx}" y="{y+13}" fill="{soft}" font-size="7"
      font-family="{eyebrow}" text-anchor="middle" letter-spacing="0.14em">LAYER</text>
```

规则：
- 首个被包含节点上方留 12–16px：眉标签就在这段边距里。
- 分区填充：`ink @ 0.02`（2% ink 水洗）。再强就会与节点填充抢戏。
- **分区标签：用 `soft`，绝不用带透明度的 ink。** 分区眉是边界标签，`soft` 正是 [`style-guide.md`](style-guide.md) 中的边界标签角色。`ink @ 0.40` 这类透明度在每种 `paper` 上合成结果都不同：在浅暖纸上约 2.2:1，7px 下无法阅读。该角色在任何皮肤下都自带对比契约。
- 每张图最多 3 个**扁平**分区。再多读起来就像泳道（那就改用泳道类型）。下方**包含**一节中的嵌套行政与流量范围不受此上限约束：它们是嵌套的，所以上限说的是同一层上的兄弟流量范围。
- 深色模式：角色随皮肤反转，不需要手工换值。从 [`style-guide.md`](style-guide.md) 的深色列取 `ink`、`soft`、`paper`；透明度保持不变。

## 包含（Containment）

**网络层级本身就是含义**时使用本节：读者必须看清什么位于哪个范围之内，而拍平的分区标签（`VNET · SNET-APP`）会歪曲这一层级。连接线仍是架构图的；包含几何来自嵌套类型（一致的缩进、每层一个眉标签、填充向内逐级加深）。这是架构图的变体，不是新类型，也不是特定云商的语法。

两种范围类型，绝不可互换：

| 类型 | 是什么 | 形状 | `data-scope-kind` |
|---|---|---|---|
| **行政（Administrative）** | 计费、权限、生命周期。不承载流量。 | 水平**条带**：全宽包含矩形，带 24px 头部 | `admin` |
| **流量（Traffic）** | 数据包不经显式规则不得穿越的边界。 | **方框**：既有的分区 rect（`rx=8`） | `traffic` |

厂商中立的元数据（无厂商前缀）：

- 根 `<svg>` 上的 `data-grammar="architecture-containment"`——没有它的文件就是普通架构图，本契约不适用。
- 每个范围的边界 rect 上（`data-role="bounds"`）带 `data-scope-id` + `data-scope-kind`。无论范围还是节点，边界一律是 `<rect>`。
- 每个嵌套范围与每个节点带 `data-parent`，指向最内层包围它的 `data-scope-id`。只有不被任何范围包围的最外层范围可以省略。
- 节点：`data-node-id`，`data-kind` 为 `compute`（流量范围内的负载）、`endpoint`（流量范围内的私有端点）或 `managed`（归属行政范围的 PaaS）。
- `endpoint` 带 `data-target`，指明它抵达的 `managed` 节点。
- 对等路径（peering path）带 `data-peering`、`data-from`、`data-to`，指明它连接的两个流量范围。

**PaaS 摆放（规范性）。** 托管服务绝不出现在流量范围内。它放在拥有它的行政条带里。子网里住着的是它的私有端点。把数据库画进子网，等于告诉读者它受该子网安全规则保护，而事实并非如此。`scripts/verify-architecture-containment.py` 会判负任何边界落入 `traffic` 范围的 `managed` 节点，以及不在任何 `traffic` 范围内的 `endpoint`。

**兄弟轴。** 同一层的兄弟流量范围共享一条轴。紧贴行政条带下方时由父级的宽高比决定：宽大于高（或正方）→ 共享一个 `y` 的行；高大于宽 → 共享一个 `x` 的列。嵌套子级取垂直轴：位于某行内流量范围里的兄弟节点排成列，它们自己的子级再排成行。同一层绝不混轴。

**预算**（收紧架构图的扁平 3 分区上限；见 `layout-budget.md`）：≤2 条行政条带、≤4 个流量范围、≤8 个节点、2 个 accent 元素。超了就按订阅拆分。

**在原地绘制范围。** 包含关系从每个边界 rect 自身的 `x`、`y`、`width`、`height` 读出。不要用 `transform` 属性、会动的行内样式（`transform`、`translate`、`x`、`y`、`position`、`margin` 等）、嵌套 `<svg>`、`<style>` 规则或动画来摆放范围或节点，无论作用于该元素还是其周围的分组。检查器对以上每一种都判负。它不评估外部样式表与脚本，所以包含几何也不要放进这两者。

`scripts/verify-architecture-containment.py` 检查 ID 唯一性、最内层父级解析、几何包含、`<rect>` 边界、行政条带与流量方框的形状区分（`stroke-dasharray` 按渲染结果解析，`none` 或全零 dash 计为实线）、PaaS 摆放、endpoint 目标、兄弟轴、声明的对等关系，以及上述"禁止移动几何"规则。没有 `data-grammar="architecture-containment"` 的文件被跳过。

## 反模式
- 每个方框都是 coral（"这个也重要"）：层级感崩塌。
- 一个方向从上下文显而易见时还画双向箭头。
- 图例浮在绘图区内。
- 把两层包含拍平成一个分区眉（`VNET · SNET-APP`）：层级本身就是论断。
- 把托管 PaaS 方框画进子网或 VPC：属于那里的只有它的私有端点。
- 仅用颜色区分行政条带与流量方框：形状必须不同，灰度下仍要分得开。

## 示例
- `assets/example-architecture.html`：极简 light
- `assets/example-architecture-dark.html`：极简 dark
- `assets/example-architecture-full.html`：完整编辑版
- `assets/example-architecture-containment.html`：嵌套行政/流量范围，light
- `assets/example-architecture-containment-dark.html`：嵌套行政/流量范围，dark
- `assets/example-architecture-containment-full.html`：嵌套行政/流量范围，完整编辑版
