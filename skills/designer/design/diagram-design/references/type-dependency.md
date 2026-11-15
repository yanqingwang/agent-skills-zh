> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-dependency.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 依赖图

**适用：** 跨 package、模块或服务的"谁依赖谁"；具体用于表达**树**在结构上表达不了的两件事：(a) 一个节点有**多个父节点**（多个东西汇聚其上的共享依赖），(b) 一个**环**。数据里两者都不出现（每个节点恰有一个父节点、没有指回去的边）时，改用 [Tree](type-tree.md)；明说这一点，不要把树形数据硬塞进图布局。

## 布局惯例

- **分层排级。** 节点按依赖深度坐进横向的层级行：rank 0（没有东西依赖的入口）在顶，更深的 rank 在下。前向边向下跨 rank，或当依赖被压缩到与其依赖者相同深度时在同一 rank 行内水平走（例如浅层的兄弟依赖）；绝不向上走，被标记的那一个环除外。层级行间距 120px。
- 节点用标准节点框模式（§6，[primitives-core.md](primitives-core.md#node-box--full-pattern)）：`rx=6`、宽 160px、高 56px。
- **扇入徽标。** 每个节点右上角带一个 `eyebrow` 角色的 8px 徽标，装在小 `rx=2` 框里，显示有多少节点依赖它（`4 in`）。完全落在节点内部的 mask 算徽标 chip，不是标签，在 §6 规则 6 下合法。扇入最高的节点就是这张图的结构故事；别的什么都不要放大到与它争。
- **节点处理**（[style-guide.md § Node type → treatment](style-guide.md#node-type--treatment)）：
  - 内部 package/服务 → 白底 + `ink` 描边。
  - 外部 / 第三方 → `ink @ 0.03` 底 + `ink @ 0.30` 描边（External/Cloud 处理）。
  - 无出边的叶子 → `ink @ 0.05` 底 + `muted` 描边。
- **环。** 至多一条反向边逆着 rank 向上。它是这张图的编辑观点：`accent` 描边、虚线 `5,4`、`marker-end="url(#arrow-accent)"`，绕节点堆**外侧**走——绝不从正中间穿过，也绝不从它没有连接的节点背后经过，可见端带被 mask 的 `arrow-label` 角色 8px `CYCLE` 标签。被环触碰的两个节点保持各自的常规节点处理（§5）：节点本身不上 accent 描边或填充，否则 2 个 accent 的预算就花错了元素。
- **焦点规则：** 每图允许的 2 个 accent 元素就是这条反向边和它的 `CYCLE` 标签。依赖图里其他任何东西都不是 accent。
- §6 的六条强制连接线规则全部适用，无豁免：离轴节点之间圆角直角弯（`r=8`）、6–10px 标签边距、连接线不重叠（交叉处 bridge/hop）、多条边共享一条框边时扇形接入点（间距 >=12px）、连接线不从非端点盒子背后穿过、标签 mask 不被后画的节点裁掉。

## 复杂度预算

| 上限 | 规则 |
|---|---|
| 节点上限 | 9 |
| 边上限 | 14 |
| 层级行上限 | 4 |
| 高亮环上限 | 1 |
| accent 元素上限 | 2 |

超预算：把叶子簇收进一个聚合节点，标签写数量（如 `+6 leaves`），并在 caption 里说明：不要悄悄丢节点。

## 反模式

- 数据其实是树（处处单父节点、无环）却画了依赖图，改用 Tree。
- 前向边向上指，却不是那一条被标记的环。
- 毫无排级的毛球布局：永远先排级；排级才是让图可读的东西，不是可选的抛光步骤。
- 每个文件一个节点而不是每个 package/模块/服务一个节点：图说的是依赖结构，不是文件系统。
- 外部依赖不带标签：版本或 registry 放进 `sublabel`（`v3.23 · npm`），不要留成隐含。
- 一张图里高亮多于一个环：挑编辑上最重要的那一个；第二个环会和第一个争，两个都读不出来。
- 漏掉扇入徽标：没有它们，读者一眼看不到依赖集中在哪里，而这正是这个类型胜过普通树的全部理由。

### 弧线图

**适用：** 少数几个 package 之间的两两 import，且"跳"本身就是故事：节点排在一条基线上，每条边是一个上凸的半圆，高度等于它跨过几个座位。排序依赖图会把一条跨层 import 埋进毛球里时用它：交付示例把七个 package 从左到右排开，Checkout 仍在 import Auth 就是最高那条弧。

不适用：一个节点有很多父节点、需要层级行的（那是父级依赖图）；一棵树（每个节点一个父节点，用 Tree）；必须绕开节点堆走的环（父级图用一条虚线反向边标记它）。弧线图没有 rank，也没有反向边语法。

#### 布局惯例

- **一条轨道，从左到右。** 节点是 `r=6` 的圆点，共一条基线，在 `0 0 1000 500` 里 `y=400`，等距（交付示例用 140px 间距，从 `x=80` 起）。标签放在圆点之下，`text-anchor="middle"`。
- **节点数：4–9。** 少于 4 没有可跳的轨道；多于 9 就把总览和一簇拆开。
- **只画上凸半圆。** 每条 import 是 `M x1,y A r,r 0 0 1 x2,y` 配 `fill="none"`。SVG 坐标系里 sweep 1 上凸；sweep 0 会把 import 画到座位之下。`r` 是端点距离的一半，所以高度等于跨度 × 间距 / 2：邻居戴不上跳层的弧。
- **跨度就是座位数。** `data-span` 是轨道上的 `|i−j|`。跳五个座位就是邻居的五倍，不是一条装饰性的更高弧线。
- **从后往前画：** 先画长弧，再画邻居，最后画焦点跳层，让它成为眼睛最先撞上的那条线。
- **4px 网格**只约束设计常量：基线、标签基线、图例行、节点半径。轨道上的位置按间距缩放，豁免。

#### 颜色

- **一条 accent 弧，其余一律 muted 处理。** 交付示例 accent 的是 Checkout → Auth：那条会在拆分时最痛的跳层，不是边最多的 package。
- **描边，不是填充。** 弧是线。填充会把一次跳层变成一块楔形。
- **节点保持 ink。** accent 落在跳层上，与父级图的规则一致：环是 accent，它触碰的节点不是。

#### 诚实数据规则

**弧高就是座位数，共享同一条间距。** `scripts/verify-arc-diagram.py` 为此把关。

- **一条基线，一个间距。** 节点偏离轨道，或一个座位和邻居宽度不同，会让同一数量的两个跨度画在两个高度上。
- **`data-span` 等于 `|i−j|`。** 五个座位的跳层声明成 2，或把邻居画到跳层的半径，是这个类型不可饶恕的错误。
- **端点就是那些具名节点。** 一条路径点名 Auth 和 Checkout 却落在 Catalog 上，那是另一条 import。
- **方向沿轨道读。** 每条 muted 弧都从左到右：左边的座位 import 右边的，所以按 import 方向排轨道，并在 caption 里说明。唯一逆着轨道的 import 是 accent 弧，在它 import 的 package 上带一个小 accent 箭头。每条弧都上箭头会在共享座位处堆叠，因为每条弧都竖直落地。

#### 声明这些值

**每条弧都绑定到它连接的两个节点和它编码的跨度。** `<path>` 上的 `data-span` 是弧线图契约，刻意不用 `<circle>` 上的 `data-value`（beeswarm）、`data-size`（bubble）、`data-series`（slopegraph）或 `data-ranks`（bump），这样兄弟检查器不会认领弧线图文件，这个检查器也不认领它们的。

```svg
<!-- Seat rail at y=400, pitch 140. Auth is seat 1, Checkout is seat 6. -->
<circle data-name="Auth" cx="220" cy="400" r="6"/>
<circle data-name="Checkout" cx="920" cy="400" r="6"/>
<path data-from="Checkout" data-to="Auth" data-span="5"
      d="M 220,400 A 350,350 0 0 1 920,400"
      fill="none" stroke="{accent}" stroke-width="1.6"/>
```

每个绑定买到什么，漏掉它付出什么：

| 绑定 | 没有它 |
|---|---|
| path 上的 `data-span` | 邻居上一条装饰性高弧抓不到：画出来的半径就是对跳层的唯一陈述。 |
| `data-from` / `data-to` | 一条点名两个 package 却落在另外两个上的路径，看起来仍像它们的 import。 |
| 节点圆及其标签上的 `data-name` | 沿轨道交换两个标签就给两个 package 改了名，而每个跨度在孤立看时仍然正确。 |

`scripts/verify-arc-diagram.py` 从节点推导间距，要求一个半径同时匹配端点距离和 `pitch · span / 2` 的上凸半圆，拒绝第二条 accent 弧或向左 import 的 muted 弧，并逐个核对绑定标签与它点名的节点；`scripts/test-verify-arc-diagram.py` 以两种极性证明每项检查，并在两个方向上钉住兄弟作用域条约。

**除了自己的属性，任何东西不得给标记定位。** 检查器读原始 `cx`/`d`/`x`，事后施加的任何东西都会让已通过的检查失效。所有载体都被拒绝（`transform` 属性、行内 `style="…"`、`<style>` 块里的一条规则），无论在节点、弧、绑定标签还是祖先 `<g>`/`<svg>` 上。把偏移直接烘进坐标。

**除了自己的属性，任何东西不得给标记上色或隐藏。** `<style>` 规则高于一切表现属性，所以检查器拒绝设置 `stroke` 或 `fill` 的规则，也拒绝隐藏或重置（display、visibility、零 opacity、零描边宽或 `all`）图中 `<svg>`、其内部任何元素或其周边元素的规则。只管页面 chrome 的规则没问题，比如 `.footer{display:none}` 或一个 logo。accent 弧读作交付示例的橙色，或由一条触达图的规则设置的现行 `--color-accent`。给每条 import 它自己的字面 `stroke`。

#### 反模式

- 把邻居画到跳层的高度：这个类型唯一不可饶恕的错误。
- 排序布局、绕开节点堆的环、或扇入徽标（那些是父级图的）。
- 填充弧，或用 sweep 0 让 import 挂在座位之下。
- 间距不均，高度不再等于跨度。
- 每条边一个色相，而不是统一 muted 加单一 accent。
- 从 CSS 给标记、绑定标签或祖先组定位。

## 示例

- `assets/example-dependency.html` — 极简浅色
- `assets/example-dependency-dark.html` — 极简深色
- `assets/example-dependency-full.html` — 完整编辑风
- `assets/example-arc-diagram.html` — 弧线图，极简浅色
- `assets/example-arc-diagram-dark.html` — 弧线图，极简深色
- `assets/example-arc-diagram-full.html` — 弧线图，完整编辑风
