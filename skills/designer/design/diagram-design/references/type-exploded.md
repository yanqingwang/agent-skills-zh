> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-exploded.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 爆炸轴测图（Exploded axonometric）

**适用场景：** 单个物体或系统以平行投影绘制，部件沿一条轴拉开并加注标签。设备拆解（手机里有什么）、开箱（盖、产品、衬垫、箱）、装配顺序，或一个堆叠的各层：当读者应把它们看作同一物体的实体部件时使用。

**不适合本类型：**

- 带逐行注释的有序抽象层级 → **分层堆叠**（`type-layers.md`）。分层堆叠是扁平的文字条带；爆炸图是一个物体的部件。图里没有任何东西有占地面积或厚度时，用分层堆叠。
- 组件及组件之间的连接 → **架构图**（`type-architecture.md`）。爆炸图没有箭头；沿轴的位置是唯一的关系。
- 没有顺序的包含 → **嵌套**（`type-nested.md`）。
- 软件跑在哪里 → **部署图**（`type-deployment.md`）。

## 投影

2:1 dimetric。地面轴与水平线成 26.565 度，因此模型单位是 4 的倍数时，每条边都落在整数像素上。世界坐标 x 向右下，y 向左下，z 向上。所有点都用同一个函数投影，绝不手工摆坐标：

```python
from math import sqrt

def iso(x, y, z, ox, oy):
    """Model point to SVG point. (ox, oy) is where model (0, 0, 0) lands."""
    return ox + x - y, oy + (x + y) / 2 - z
```

角半径为 `r` 的圆角矩形足印投影为直边，衔接同一椭圆上的四分之一弧：`rx = r * sqrt(2)`、`ry = r / sqrt(2)`。一切轮廓都用这一个形状：`r = 0` 是方箱或板，小 `r` 是产品圆角，`r = w / 2 = d / 2` 是圆柱。收缩轮廓时角心保持不动，所以内沿就是同样四个角心配更小的半径。

面用普通 SVG `<path>` 与 `<polygon>` 元素绘制，投影点直接写进路径数据。不用 CSS 3D、不用 canvas、不用 WebGL，也不用 `transform` 摆几何。内容确实需要平贴在某个面上时，与 `iso()` 一致的矩阵是：顶面 `matrix(1,0.5,-1,0.5,tx,ty)`，左面 `matrix(1,0.5,0,-1,tx,ty)`，右面 `matrix(-1,0.5,0,-1,tx,ty)`。标签绝不用它们：标签保持水平。

仓库中的 `scripts/build-exploded-examples.py` 用这个函数构建全部随附示例，也是下方辅助函数的实操参考。

## 版式约定

- **部件：** 2 到 5 个，自下而上列出。每个部件是一个圆角棱柱（`rect`，厚度 `t`），顶面上最多两级细节，因为顶面是读者看到的那一面。
- **爆炸轴：** 默认竖直。部件笔直上升，无旋转，最底部部件保持 `z = 0`。
- **层级：** 装配状态下并排的部件属于同一层，一起拉开。手机的逻辑板与电池在壳内相邻，所以它们作为同一层抬起，而不是隔一个间隙叠两层。
- **间隙：** 每对相邻层之间一个间隙，`gap = max(k x top-face height, 3 x thickness of the thickest solid part)`，向上取整到 4 的倍数。`k = 0.5` 是下限；高部件会遮住其下方的焦点部件时提到 `0.75`。顶面高度取最大足印的 `(w + d) / 2`。容器（壳、箱）不计入厚度。
- **净空：** 引线会穿过另一部件、或两条标签相距不足 36px 时，按步长 4 提高间隙，直到两者都不发生。同一层上相互碰撞的两个部件无法靠间隙解决：在平面图上挪走其中一个。
- **绘制顺序：** 最底层先画。同一层内，越靠后（`x + y` 越小）的部件越先画。容器是拆开的：它的后半（轮廓、沿口、腔体、底面）在住进它的部件之前绘制，外壁与前沿口在它们之后绘制。这是让装配帧正确显示托盘内部件的唯一办法，并且在爆炸全程保持正确。
- **画框：** 画布宽 1000。物体与 240px 标签列整体居中；viewBox 高度跟随爆炸后的物体加 40px 顶部边距。闭合帧同样不裁切任何东西，因为闭合后的物体装得进爆炸后的范围。

### 面与线

| 元素 | Light | Dark |
|---|---|---|
| 面基色（不透明，衬在所有面之下） | `#ffffff` | `paper-2` |
| 顶面 | base | base + `ink @ 0.10` |
| 左面（受光侧） | base + `ink @ 0.07` | base |
| 右面（背光侧） | base + `ink @ 0.15` | base + `paper @ 0.45` |
| 焦点部件，顶/左/右 | base 之上 `accent` 的 0.10 / 0.20 / 0.32 | 顶 `accent` 0.18，侧面保持中性 |
| 轮廓 | `ink`，1.2（`stroke-strong`） | `ink`，1.2 |
| 内边（顶面前沿、前角） | `ink` 的 0.55，0.8（`stroke-thin`） | `ink` 的 0.45，0.8 |
| 面上的细节线 | `ink` 的 0.55，0.6 到 0.8 | 相同 |
| 迹线 | `ink` 的 0.30，0.8，虚线 `4,3` | `ink` 的 0.30，0.8，虚线 `4,3` |

光从左上来，所以左面比右面亮。一定要着色：只描轮廓的方框会像 Necker 立方体一样在两种读法之间翻转。面是不透明基色加 `ink` 覆盖层，绝不用单独的半透明填充，这样后面的部件不会透出来。迹线从最底部部件轮廓的左右极点笔直向上，直达顶部部件的底面，并在所有部件之前绘制，让部件盖住它们。

### 标签

- 每个部件一条标签，集中排在物体右侧的一列。标签是部件名（`node-name` 角色，600，16px，一到两个词）加上其下的技术副标签（`sublabel` 角色，10px，`muted`，字距 0.08em）。
- 一条水平引线（0.8px，`ink` 的 0.40）从部件右极点上的 2px 圆点右侧 6px 处、取中厚度，连到标签列左侧 12px 处。引线不打弯、不穿部件、互不交叉；来自不同高度的水平引线天然不会交叉，上方间隙规则又保证它们避开部件。
- 焦点部件的圆点、引线与副标签用 accent。名称保持 `ink`。
- 不要编号标注，也不要图例。标签就在它命名的部件上。

### 细节

至多三级：形体（圆角棱柱）、其顶面上的内嵌（屏幕、电池轮廓、模压凹槽）、以及微细节（芯片、镜头、logo 标记）。由许多相同小件组成的部件（键帽、开关）声明其网格的包络作为方箱，逐件画一个小棱柱而不是画包络；轮廓路径仍保留给校验器，无填充。可能够到面边缘的内嵌按该面裁剪，保持在边缘以内 4 个单位以上，停在三级。不要接触阴影：本皮肤不收阴影（SKILL.md §4）。物体需要接地时，最底部部件已经提供了。

### 焦点部件

至多一个部件用 accent，遵循 SKILL.md 的 1 到 2 个焦点元素规则。其余部件保持中性；不要用 opacity 把它们淡化，半透明的部件会露出背后的边。

## 可选动效

爆炸图可以从装配状态打开、爆炸一次，因为看着部件抬升最能说明它们如何咬合。按 `animation.md`，使用 `assets/template-motion.html` 的钉定控制器、`reveal` 模式：

- 源文件就是爆炸帧。每个部件分组带 `data-motion-item`、从顶层向下计数的 `data-step`（顶层先抬），以及 `style="--lift:Npx"`，N 为该部件爆炸 z 减装配 z。在此投影下，模型空间中的竖直移动就是屏幕上的竖直移动，所以一次 `translateY(var(--lift))` 就是整个爆炸。
- 最底层不动。其标签与迹线在最后一步一起出现。
- 每个部件的标签在闭合帧隐藏、在其部件落位后淡入。立即隐藏、只延迟显现，否则前半秒标签会堆在闭合物体上。
- 无 JavaScript、`prefers-reduced-motion: reduce`、打印、`?motion=static` 与导出全都显示爆炸帧。
- 这次抬升是 `animation.md` 24px 位移限制的唯一限定范围例外，在仓库中记录为 ADR 0013。图中其他任何东西都不动。

## 元数据契约

`scripts/verify-exploded.py` 按各部件的声明重新投影：

- 图：一个 `<g data-exploded data-origin="ox oy" data-gap="g">` 包住全部部件。
- 每个部件：一个 `<g>`，带 `data-part`（键）、`data-name`（标签文字）、`data-rect="x0 y0 x1 y1 r"`、`data-z`、`data-t`、`data-level`，容器可选 `data-kind="housing"`，焦点部件可选 `data-focal`。参与动画的部件加 `data-closed-z`。
- 部件内部：第一个 `<path data-role="silhouette">` 是部件按其声明方箱的轮廓；`<g data-role="label">` 内含一个 `<line data-role="leader">` 与一个 `<text data-role="name">`。后者的完整文字（含行内 `<tspan>` 后代）必须与部件的 `data-name` 一致。
- 迹线带 `data-role="trace"`。

轮廓校验器接受既有绝对 M/L/A/Z 路径契约内的带符号十进制与科学记数法坐标。每个操作数必须有限；投影顶点、角半径与弧 flag 仍被检查。这不引入相对路径命令。

## 反模式

- 手摆坐标，或用 CSS `transform` 顶替几何。
- 只有轮廓、没有面着色的部件。
- 部件旋转、横滑，或在同一张图里沿两条轴爆炸。
- 间隙不等，或为迁就画布压缩间隙。要么提高 `k`，要么砍掉一个部件。
- 标签放在部件上、贴着某个面倾斜，或摊在两列里。
- 编号标注加下方对照表。
- 不止一个部件用 accent，或把其他部件淡化以衬托重点。
- 模糊的接触阴影、实体面上的渐变，或发光。
- 对没有实体部件感的东西做爆炸图。所谓各层只是一份清单时，用分层堆叠。

## 示例

- `assets/example-exploded.html`：应用栈，极简 light
- `assets/example-exploded-dark.html`：应用栈，极简 dark
- `assets/example-exploded-full.html`：应用栈，完整编辑版
- `assets/example-exploded-phone.html`、`-dark`、`-full`：手机拆解，带外壳、共享的主板与电池层、屏幕
- `assets/example-exploded-unboxing.html`、`-dark`、`-full`：包装盒，伸缩式盒盖，产品与线缆同层，衬垫，箱体
- `assets/example-exploded-ai-stack.html`、`-dark`、`-full`：AI agent 栈，带密钥库、工具、作为单层小卡片的 skills、包住模型的 agent harness，以及界面
- `assets/example-exploded-keyboard.html`、`-dark`、`-full`：机械键盘，带底座托盘、PCB、定位板、开关阵列与键帽阵列
- `assets/example-exploded-phone-animated.html`：手机先装配，再爆炸一次
- `assets/example-exploded-unboxing-animated.html`：箱子先闭合，再开箱一次
- `assets/example-exploded-ai-stack-animated.html`、`assets/example-exploded-keyboard-animated.html`：栈与键盘先装配，再爆炸一次
