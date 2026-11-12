> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-polar.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 极坐标图（Polar Chart）

**适用场景：** 4–8 个类目上的单个定量系列，且顺时针顺序本身有意义。

## 输入契约

```yaml
title: "Request demand by UTC window"
unit: "% of daily peak"
scale:
  min: 0
  max: 100
categories:
  - { label: "00–03", value: 32 }
  - { label: "03–06", value: 18 }
  - { label: "06–09", value: 24 }
  - { label: "09–12", value: 58 }
  - { label: "12–15", value: 100, focal: true }
  - { label: "15–18", value: 82 }
  - { label: "18–21", value: 76 }
  - { label: "21–24", value: 45 }
start_angle: -90
clockwise: true
source_note: "Illustrative normalized workload profile"
```

校验规则：

1. `scale.min` 恰为 `0`；截断的径向刻度无效。
2. `scale.max` 为有限且大于 `0`。
3. 每个值有限且满足 `0 <= value <= scale.max`。
4. 类目标签在去首尾空白后唯一，类目数为 4–8。
5. 至多一个类目为 focal。
6. 类目保持输入顺序；按值排序会摧毁环形含义。

缺失值不在第一版范围内。Agent 必须停下来询问是省略该类目还是补一个值；不得把缺失数据强转为零。

## 定量编码

对第 `i` 个类目（共 `N` 个）、值 `v`、圆心 `(cx, cy)` 与外半径 `R`：

```text
theta_i = start_angle + clockwise_sign * 2π * i / N
radius_i = R * v / scale.max
x_i = cx + radius_i * cos(theta_i)
y_i = cy + radius_i * sin(theta_i)
```

计算时角度以弧度表示；`start_angle` 以度数提供，默认 `-90`，把第一个类目放在十二点位置。`clockwise_sign` 在默认顺时针时为 `+1`，否则为 `-1`。

值射线是从 `(cx, cy)` 到 `(x_i, y_i)` 的线段。其可见长度严格正比于 `v`。端点圆半径恒定，不编码任何附加量。任何填充扇区都不得落在值射线之后或之下，因为其面积会与声明的半径编码竞争。

携带 `data-polar-chart` 的元素必须是图表的根 `<svg>`。其后代只允许 `<g>`、`<line>`、`<circle>`、`<rect>`、`<text>`、`<title>` 与 `<desc>`；嵌套 SVG、path、polygon、外部引用、图像与其他一切元素都被拒绝。重复属性、不匹配的标记、URL 值的 SVG 引用、transform、经 `@import`/`url()` 加载的 CSS、影响几何的 CSS 都被禁止。图表元素既不带 `class` 也不带行内 `style`；文档样式不得使用可能匹配图表的选择器，规范的根 `svg` 布局规则除外。唯一允许的外部样式表是 Google Fonts。每条线恰好携带 `data-polar-spoke`、`data-polar-ray`、`data-polar-rule` 三者之一，并使用该角色声明的描边宽度；spoke 与 ray 的几何在 `min(0.75 px, R 的 5%)` 内校验。五个网格圆携带 `data-polar-ring`，使用 `fill="none"`、0.8 px 描边、图表圆心，以及 20% 到 100% 的半径区间各恰好一次。每个端点圆携带 `data-polar-marker`，使用声明的 4 px 半径（focal 类目为 5 px），配 1.2 px 描边。可选的满幅背景是唯一的矩形，携带 `data-polar-background`。这份判负即拒的白名单，防止贡献者用未标注或伪标注的填充形状绕过纯半径编码。

### 零值

`v = 0` 时 `radius_i = 0`。不渲染值射线，也不渲染端点标记。保留淡的全半径类目 spoke，并把该类目的数值标签渲染为 `0`。圆心处的一个刻度标签同样标记共享的零基线。不要添加最小轮毂、最小射线长度、偏移的标记或其他可见量级。

## 版式约定

第 1 版支持：

- 单个定量系列；
- 4–8 个等距类目，顺时针顺序有意义；
- `min = 0` 且 `max > 0` 的共享线性刻度；
- 20%、40%、60%、80%、100% 处的五条环形网格线；
- 一个可选的 focal 类目，以 accent token 渲染；
- 极简 light、极简 dark 与完整编辑版示例；
- 外环之外水平、正立的类目标签；
- 每个类目一个数值标签。

第 1 版排除：

- DISC、性格、能力素质与角色画像轮盘，其扇区是定性的；
- 扇区内任意布点；
- 填充定量楔形、渐变色带或甜甜圈轮毂；
- 多系列、负值、对数刻度、不等扇区角与超过八个类目；
- 动画或交互。

多个实体在共同标准上打分用 Radar；超过八个有序时间段用 Line；环形顺序不增添含义时用 Bar。

## 几何

三个示例都用 `viewBox="0 0 1000 520"`、圆心 `(500, 230)`、`R = 160`。

- 网格环：`r = 32, 64, 96, 128, 160`。
- 类目 spoke：从圆心到 `R`，0.8 px 规则线描边，无箭头。
- 非 focal 值射线：2 px muted 描边；端点标记半径 4。
- focal 值射线：2.4 px accent 描边；端点标记半径 5。
- 环标签：`0.2 × max` 到 `1.0 × max`，只标在第一条轴上，`arrow-label` 角色 8 px；因此示例显示 `20, 40, 60, 80, 100`。
- 类目标签：在 `R + 28`，`node-name` 角色 11 px semibold，水平正立。
- 数值标签：在 `R + 44`，`arrow-label` 角色 8 px；单位放在图表副标题里，不重复八次。
- 标签锚点：垂直 15 度以内用 `middle`，右半边用 `start`，左半边用 `end`。
- 绘制顺序：背景、环、spoke、刻度标签、非 focal 射线、focal 射线、端点标记、类目标签、数值标签、图例/来源注记。

极简示例使用完整的 1000×520 画布。完整编辑版把同一张图放进既有编辑框架，添加摘要卡片而不改变图表几何。

## 视觉处理

- accent 类目至多一个。其余值射线用 muted token。
- 环与 spoke 是结构网格标记，绝不是类目颜色。
- 端点标记是恒定大小的棒棒糖头，不是气泡。
- 类目标签保持水平；切向旋转被有意排除，因为它降低可扫读性，属于被否决的定性轮盘方向。
- 图表必须在灰度下可理解：位置与数值标签承载数据；accent 只负责引导注意。
- SVG 可访问描述要点名峰值类目、刻度与顺时针类目顺序，不叙述几何。

## 复杂度预算

- 4–8 个类目。
- 恰好一个定量系列。
- 至多一个 focal 类目。
- 五条网格环，每类目一个数值标签。数值标签必须透过祖先可见：祖先 `display="none"` 与零 opacity 会压制后代，显式的子级 `visibility="visible"` 可以恢复被继承的隐藏可见性。
- 只输出静态；宁可拆分或换类型，也不加交互或第二重编码。

## 何时不使用

- 多个系列 → 用 Radar。
- 非环形类目 → 用 Bar。
- 超过八个有序时间段 → 用 Line。
- 定性画像、任意扇区布点、负值或对数刻度 → 选一个诚实的非极坐标表达。

## 反模式

- 甜甜圈轮毂或任何非零内基线。
- 填充楔形、扇区或渐变色带，暗示面积编码量级。
- 切向或旋转的类目标签。
- 同一张极坐标图上放多个系列。
- 最小值不为零的截断刻度。
- 按值排序类目，而不是保留有意义的环形顺序。
- 把缺失值当零。

## 示例

- `assets/example-polar.html`：极简 light。
- `assets/example-polar-dark.html`：极简 dark，同一数据集与几何。
- `assets/example-polar-full.html`：完整编辑版，三张不等宽摘要卡片，图表几何不变。
