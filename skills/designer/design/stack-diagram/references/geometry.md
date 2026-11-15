> **中文汉化版** · 上游：[caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram) · 原文件：`skills/designer/design/stack-diagram/references/geometry.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 几何——坐标、间距和碰撞规则

画布是一个定尺寸、绝对定位的坐标系（默认宽 1000px；高度按需）。节点是 `position:absolute` 的 div；连线放在同一张 SVG overlay 里，viewBox 与画布尺寸相同。因为一切都靠手工摆放，下面这些碰撞规则才是让结果干净的关键。

## 节点盒子

```
left = centerX - 66          (node div is 132 wide, text centered)
tile: 60x60, top of node div (tile spans centerX±30, topY..topY+60)
name: ~13px display font at topY+68
role: ~10px mono at topY+86
node box bottom ≈ topY + 100
```

所以一个节点大致占 **132w × 100h**。所有锚点计算都用这些数字。

## 间距常量

- 水平：同一行节点中心相距 ≥140px（标签宽 132，再近就会挨上）
- 垂直：相邻两行的 tile 顶相距 140px（上一行盒子底与下一行 tile 之间留约 40px 空隙）
- 分组，左右：边界在最外侧节点**盒子**之外 24px，即 `leftmost centerX − 90` 和 `rightmost centerX + 90`。按 132px 盒子量，不要按 60px tile 量，否则名字比 tile 宽时会挤向一侧；每个分组都拿到相同的对称内边距
- 分组，上下：上边界 = 第一个 tile 顶 − 60（分组标签就放在这条带里）；**下边界 ≥ 最后一个 tile 顶 + 150**，让节点文字留在盒子内
- 分组标签：放在左上角内侧（`top:12px; left:12px`，无背景），这样边框不断开。让连线避开那个角。
- 嵌套分组：左右和底部相对父级内缩 ≥24px，顶部从父级上边界往下 ≥48px 起（在父级标签下方）

## 连线锚定——防止文字被压的规则

**一个节点等于它的 tile 加上下面的文字。** 把 `(centerX±66, topY..topY+100)` 当作连接边界。

- **水平连线**（同一行）：在 tile 中线高度 `y = topY+30`，从 `x = centerX+30+4` 连到 `x = targetCenterX-30-4`，tile 边对 tile 边。安全，因为 tile 旁边没有文字。
- **垂直连线**（节点在上、节点在下）：连**盒子底到 tile 顶**：从 `y = topY_upper + 100` 往下到 `y = topY_lower - 4`（或反过来向上）。绝不要从 tile 底（`topY+60`）穿过标签文字往下画。
- **肘形连线**（不同行且不同列）：垂直段走在没有节点盒子的 x 走廊里；水平段走在两行之间的空白带里（`topY_lower - 40 .. topY_lower - 10`）。穿过另一条**连线**是画图的常规做法；穿过**节点盒子**不行。
- 线端与边界之间留 4–6px 间隙；箭头（`marker-end`）负责补上那一碰。

模板内置两层防护，保留它们：
1. 连线标签用 `paint-order: stroke` 配纸色描边（光晕），线从底下过时仍可读。
2. 节点 name/role 文字包在带纸色背景的 `<span>` 里，实在避不开的穿线会消失在文字背后，而不是划过文字。

## 连线类与标签

```html
<path class="e" d="M148 150 H306" marker-end="url(#ar)"/>        accent solid — primary flow
<path class="n" d="M487 226 V344" marker-end="url(#ar)"/>        neutral solid — internal
<path class="n dash" d="M318 380 H208" marker-end="url(#ar)"/>   dashed — dev/deploy
<text class="el a" x="227" y="142" text-anchor="middle">HTTPS</text>
```

箭头 marker 是 `#ar`。它用 `context-stroke` 填充，于是自动取用它的那条线的颜色，两种主题都成立，不要为每种颜色加单独 marker。AWS 图用 `#open`，同理。

- 水平连线标签：居中放在线上方，`y = lineY - 8`
- 垂直连线标签：放在线右侧，`x = lineX + 10`，垂直方向居中于该段
- accent 连线上的标签用 `.el.a`（accent），其余用 `.el`
- 标签只用 1–2 个短词；细节交给节点下面的 role 文字

## 演算示例（模板自带的样例）

画布 1000×540。第 1 行 tile 在 top=120：User(cx 112)、App(cx 342)、API(cx 487)。第 2 行 tile 在 top=350：Tool One(cx 172)、Tool Two(cx 354)。Vendor 分组框住 App 和 API，`left:252 top:60 w:325 h:210`（342−90 → 487+90；top 120−60；bottom 270 = 120+150）；tooling 分组 `left:82 top:290 w:362 h:210`（172−90 → 354+90；top 350−60；bottom 500 = 350+150）。

```
user→app        M148 150 H306      (horizontal, tile-mid: 112+30+6 → 342-30-6)   label "HTTPS" at (227, 142)
app→api         M376 150 H451      (horizontal, tile-mid)
tool2→tool1     M318 380 H208      (dashed, tile-mid of row 2: 354-30-6 → 172+30+6) label "pre-commit" at (263, 372)
```

一条从 API 向下连到第 2 行 cx 487 节点的垂直连线会是 `M487 226 V344`（盒子底 120+100+6 → tile 顶 350-6）。

检查你的方案时，把每条垂直/肘形段列出来，逐段问：在 y1 到 y2 之间，这条 x 走廊穿过了哪些节点盒子？答案必须是：一个都没有。
