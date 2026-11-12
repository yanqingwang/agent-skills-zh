> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-axonometric-plan.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 轴测平面图

**适用场景：** 以一个角度俯瞰单层楼面或单块场地，并看到上面立着的东西。带房间与家具的办公楼层、带建筑与道路的园区、带库区的仓库、商店平面。当读者需要在单一视图中看到房间或建筑彼此的位置关系及各自用途时使用。

**不是这个类型：**

- 把一个物体的部件沿轴拉开 → **爆炸轴测图**（`type-exploded.md`）。平面图只有一块板，没有任何东西被拉开。
- 没有地理含义的包含关系 → **嵌套图**（`type-nested.md`）。
- 软件运行在哪里 → **部署图**（`type-deployment.md`）。
- 房间与容量的清单 → 一张表格。

## 投影

与爆炸轴测图相同的 2:1 二测投影，来自同一个函数：

```python
def iso(x, y, z, ox, oy):
    """Model point to SVG point. (ox, oy) is where model (0, 0, 0) lands."""
    return ox + x - y, oy + (x + y) / 2 - z
```

每个元素都是立在板上的圆角棱柱：墙体、家具和建筑 `r = 0`，树冠 `r = w / 2`。`type-exploded.md` § Projection 覆盖角椭圆与各面矩阵；仓库中的 `scripts/build-axonometric-plan-examples.py` 用同一组辅助函数构建所有随附示例。

## 布局约定

- **板（Plate）：** 一块楼板（6 units）或一块场地（8 units，小圆角）。所有东西都立在它上面，且不超出它的边缘。
- **墙：** 厚 6 units，在桌面高度（约 22 units）处截断，这样没有墙会挡住房间。门是墙上的缺口。墙相交时不重叠：让一面墙穿过交点，另一面墙停在它的面上。
- **家具与建筑：** 立在板上的盒子，采用 house 面着色（`type-exploded.md` § Faces and lines）。高度彼此成比例。任意两个占地轮廓互不重叠。
- **平面标记：** 道路、小径和地面色调以平面填充的形式放在板顶面上（`ink` 0.07），没有厚度。道路可用虚线中线标记（`ink` 0.25，`6,5`）。
- **货架：** 高货架是一个 `rack` 类型的盒子，用 house 着色，每 14 units 一条搁板线，每 30 units 一根立柱。货架排沿 x 方向布置，让读者看到受光面和排间通道。
- **树：** 冠是圆柱，架在 8 units 高的短树干上，冠顶用 `rule-solid` 浅色或 `soft` 深色。树是绿化，保持小尺寸并避开一切占地轮廓。
- **绘制顺序：** 先板，再平面标记，然后每个盒子按从后到前排序。用拓扑序：当 A 完全位于 B 之后（`A.x1 <= B.x0` 或 `A.y1 <= B.y0`）且两者的屏幕轮廓重叠时，A 先于 B 绘制。朴素的 `x + y` 排序在长墙上会出错。
- **画框：** 画布宽 1000，板居中。viewBox 高度跟随板与最高的盒子，外加 48px 顶部留白。

### 标签

- 房间和建筑用水平标签命名：名称用 `node-name` 角色，600，12px，下方是 `sublabel` 角色的 8px 副标签，衬在不透明 `paper` 底上，带 `rule` 发丝线，总高 32px，宽度向上取整到 4 的倍数。
- 房间的标签放在房间内开阔的地面上。建筑的标签放在屋顶上。标签在所有盒子之后绘制，墙永远不会切到它们。
- 标签彼此不重叠。宁可把标签挪到开阔地面，也不要缩短名称。
- 每个名称一到两个词。不用引线，也不用编号图例。

### 焦点元素

一个房间或一栋建筑带强调色。焦点房间在地面加 `accent` 色调并配 accent 标签；焦点建筑用 accent 面阶梯和 accent 标签。焦点房间内的家具保持中性，这样强调只指向一件事。

## 可选动效

分期建设的场地可以用 `assets/template-motion.html` 的固定控制器以 `reveal` 模式逐期显现建筑。每栋建筑与其标签组成一个 `data-motion-item`，其 `data-step` 即所在期数，每步最多两个。建筑下落 16px 到位并淡入，在 `animation.md` 的 24px 限额之内。

楼层平面可以同样按区域显现。给每个区域的家具一个 `step`，构建器把每一期绘制为一组连续的盒子（它把一期收缩为深度排序中的一个节点，因此若某一期必须绘制在静态墙的两侧，构建会失败），再在所有盒子之后附上该期的一组房间标签。每期两个动效项，在每步两个的限额之内。墙和未分期的房间保持静态。静态、无 JavaScript、减弱动效、打印与导出状态显示完工后的场地。

## 元数据契约

`scripts/verify-axonometric-plan.py` 根据每个元素的声明做重投影校验：

- 图形：一个 `<g data-axo-plan data-origin="ox oy">`。
- 板：一个 `<g data-plate data-rect="x0 y0 x1 y1 r" data-z="0" data-t="t">`。
- 每个盒子：一个 `<g data-box>`，带 `data-rect`、`data-z`（板顶，或树冠为其上方 8）、`data-h`、`data-kind`（`wall`、`furniture`、`building`、`tree`、`rack`），建筑另有 `data-name`。其首个 path 是 `data-role="silhouette"`。
- 每个房间：一个 `<g data-room data-name data-rect>`。
- 每个标签：一个 `<g data-role="tag" data-name data-at="x y z">`，带一个底衬 `<rect>` 和一个 `<text data-role="name">`。标签的完整文本（包括内联 `<tspan>` 后代）必须与该标签的 `data-name` 一致。该点位于它所命名的房间内的板顶处，或建筑屋顶上。
- 焦点房间或建筑带 `data-focal`。

轮廓校验器接受现有绝对 M/L/A/Z 路径契约内的带符号十进制与科学计数法坐标。每个操作数必须是有限数；投影顶点、角半径和弧旗标仍然校验。这不增加相对路径命令。

## 反模式

- 全高墙挡住后面的房间。
- 盒子在板上重叠，或盒子悬挂出板边。
- 仅按 `x + y` 排序绘制，长墙会画到它前面的家具之上。
- 标签倾斜到地面平面上、标签互相重叠，或图下方出现编号图例。
- 焦点房间带了强调色，它的家具也带了强调色。
- 板或盒子上出现渐变、阴影或光晕。

## 示例

- `assets/example-axonometric-plan.html`：办公楼层，极简浅色
- `assets/example-axonometric-plan-dark.html`：办公楼层，极简深色
- `assets/example-axonometric-plan-full.html`：办公楼层，完整编辑排版
- `assets/example-axonometric-plan-campus.html`、`-dark`、`-full`：园区场地平面，带道路、树木和按期标注的建筑
- `assets/example-axonometric-plan-coffee-shop.html`、`-dark`、`-full`：一家咖啡店，含入口与排队柱、意式咖啡吧、圆桌、厨房和洗手间
- `assets/example-axonometric-plan-warehouse.html`、`-dark`、`-full`：履约作业层，含月台门、高架仓储货架、拣货区、打包工位和出货月台
- `assets/example-axonometric-plan-campus-animated.html`：园区逐期建成
- `assets/example-axonometric-plan-coffee-shop-animated.html`、`assets/example-axonometric-plan-warehouse-animated.html`：每层按区域分三期显现
