> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-loop.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Loop（循环图）

**最适用于：**增强回路、飞轮、反馈环与运营循环：凡是最后一步喂给第一步、且共享中枢累积状态的东西。当读者必须同时看到两种运动时用 Loop：工作沿环顺时针推进，而每一圈都把持久状态写回同一个共同中心。

路径有终点、分叉走向某个结果、或从不真正回到第一步时，改用 **Flowchart**。中心不累积共享状态时，改用 **Cycle**。虚线回写辐条是这里的定义性信号：去掉它们，这张图就只是一个环形过程。

该类型是**参数化的**。§1 的输入决定站点数、角度、边交点、连线路径与 viewBox 边界。相同输入应产出相同几何。

---

## 1. 输入：参数契约

```yaml
title: "The self-improving loop"
subtitle: "Every pass improves the shared operating record"

hub:                                  # exactly one
  name: "Shared memory"
  sublabel: "one record, every loop"

stations:                             # 5..8, clockwise from top
  - { name: "Capture",  sublabel: "signals in",       spoke_label: "SIGNALS" }
  - { name: "Research", sublabel: "evidence pulled" }
  - { name: "Decide",   sublabel: "human approves",   focal: true }
  - { name: "Act",      sublabel: "work ships",        spoke_label: "OUTCOMES" }
  - { name: "Measure",  sublabel: "outcomes logged" }
  - { name: "Learn",    sublabel: "playbook updated" }

station_w: 160
station_h: 64
hub_w: 200
hub_h: 104
radius: 240
margin: 64
dark: false
```

**预算（硬性）：****5–8 个站点，外加恰好一个中枢。**超过 8 个站点，把主题拆成一张总览 Loop 加一张或多张细节图。中枢恰好一个：两个中枢的环就是两张图。至多一个站点可设 `focal: true`；没有值得强调的编辑门时，零个也允许。

站点顺序是语义的。`stations[0]` 是顶部站点，之后条目按顺时针排布。最后一个站点总会连回站点 0；如果这个"回连"是假的，改用 Flowchart。

---

## 2. 布局数学：确定性几何

使用 SVG 坐标，y 正方向朝下。设中枢中心为 `C = (cx, cy)`，站点数为 `N`，站点环半径为 `R`，站点半尺寸为 `a = station_w/2`、`b = station_h/2`，中枢半尺寸为 `A = hub_w/2`、`B = hub_h/2`。

### 2.1 站点中心

对从 0 起计的站点 `k`：

```text
theta_k = -90deg + k * (360deg / N)
u_k     = (cos(theta_k), sin(theta_k))
P_k     = C + R * u_k

station_center_x(k) = cx + R * cos(theta_k)
station_center_y(k) = cy + R * sin(theta_k)
station_x(k)        = station_center_x(k) - station_w/2
station_y(k)        = station_center_y(k) - station_h/2
```

于是站点 0 位于顶部，`k` 增大沿顺时针走。先算理想几何，再把站点矩形取整到最近的 4px 网格点；成对站点取整时保持对称。环圆交点保留三位小数，让每条弧都留在同一个圆上。

### 2.2 实线环流端点

环连线从站点 `k` 走到站点 `j = (k + 1) mod N`，用的是站点圆上的 SVG 圆弧。每段都用同一中心 `C`、同一半径 `R`、顺时针扫掠。站点框打断圆：连线从圆沿顺时针离开源框处开始，到圆逆时针进入目标框之前结束，marker 尖端正好落在目标框的描边上。

对站点 `k` 的四条边求圆/矩形交点。竖直边 `x = x_e`：

```text
y = cy +/- sqrt(R^2 - (x_e - cx)^2)
```

只保留 `y` 落在该边内的候选。水平边 `y = y_e`：

```text
x = cx +/- sqrt(R^2 - (y_e - cy)^2)
```

只保留 `x` 落在该边内的候选。幸存的两点按其绕 `C` 的归一化极角分类：

```text
q_entry(k) = circle/box intersection immediately before theta_k clockwise
q_exit(k)  = circle/box intersection immediately after  theta_k clockwise
```

输出目标端点前先补偿 marker 尖端。规范 marker（`refX=7`，polygon 尖端在 `x=8`）加环描边宽 `1.2` 时，`marker_overhang = 1.2`：

```text
phi_entry = atan2(q_entry(j).y - cy, q_entry(j).x - cx)
phi_end   = phi_entry - marker_overhang / R
q_end     = C + R * (cos(phi_end), sin(phi_end))

M q_exit(k).x q_exit(k).y
A R R 0 0 1 q_end.x q_end.y
```

large-arc 标志为 `0`，因为相邻站点间隙小于 180 度；SVG 坐标里顺时针运动的 sweep 标志永远是 `1`。箭头伸出量补上到 `q_entry(j)` 的最后 1.2px，落在框边上而不越过其描边。从站点 `N-1` 到站点 0 的闭合连线用同一公式。

Loop 的圆弧环线是 SKILL.md §6 规则 1 有案可查的类型专属例外，沿用 Medallion 晋升弧的先例。Loop 的环绝不混入三次曲线、直线或圆角正交段：六个可见缺口必须读作同一个连续圆的组成部分。

### 2.3 虚线回写辐条端点

每根辐条从站点边向内走向中枢。用同一套射线/框交点公式，这次作用在径向向量 `u_k` 上：

```text
box_distance(v, half_w, half_h) = min(half_w / abs(v.x), half_h / abs(v.y))
                                        # ignore a term whose denominator is zero

d_station = box_distance(u_k, a, b)
d_hub     = box_distance(u_k, A, B)
marker_gap = 6                         # 4..8px; 6px canonical

spoke_start(k) = P_k - d_station * u_k
hub_edge(k)    = C   + d_hub     * u_k
spoke_end(k)   = C   + (d_hub + marker_gap) * u_k
```

因为箭头从站点走向 `C`，加上 `marker_gap` 让端点恰好停在中枢边界之外。较轻的箭头停在中枢描边之前，而不是撞上去。径向辐条是斜直连线总禁令的类型专属例外：它们必须保持为真半径，彼此不得交叉，且只能触及自己的源站点与中枢。

站点子标签已说明回写内容时，辐条标签可选。使用时按 `arrow-label` 角色，贴辐条一侧，配不透明 `paper` 遮罩，与笔画保持可见的 6–10px 间隙。挑选值得标的一小部分，不要把六个标签硬塞进中枢光环。

### 2.4 viewBox 尺寸

viewBox 必须容纳完整的站点矩形、外环曲线、箭头，以及至少 `margin` 的呼吸空间：

```text
left   <= cx - R - station_w/2 - margin
right  >= cx + R + station_w/2 + margin
top    <= cy - R - station_h/2 - margin
bottom >= cy + R + station_h/2 + margin

viewBox_w = right - left
viewBox_h = bottom - top
```

检查这些边界时，把圆的全部极值 `cx +/- R`、`cy +/- R` 连同站点边界与 marker 余量都算进去。绝不缩小画布到任何站点描边、marker 或环弧被裁。六站点规范示例中，`viewBox="0 0 1040 680"`、`C=(520,340)`、`R=240`、站点尺寸 `160×64`、中枢尺寸 `200×104`，外侧余量充裕。

---

## 3. 视觉文法

| 元素 | 处理 |
|---|---|
| 站点 | 标准节点：`paper` 填充、`ink` 描边、`radius-md`；名称用 `node-name`，子标签用 `sublabel` |
| 中枢 | 唯一的深色元素：`ink` 填充、`paper` 文字；比站点略大 |
| 焦点站点 | 至多一个：`accent-tint` 填充、`accent` 描边；站点名可用 `accent` |
| 环流 | 站点圆上的 `A R R 0 0 1` 圆弧，实线 `muted` 描边，目标端用默认箭头；只许顺时针 |
| 回写辐条 | 降调的 `soft` 虚线描边，`stroke-dasharray="5,4"`，配 `soft` 箭头 |
| 辐条标签 | `arrow-label` 角色、`soft`、全大写、paper 遮罩、与连线保持 6–10px 间隙 |

按此顺序绘制：paper 或可选点纹网格 → 环箭头 → 虚线辐条 → 辐条标签遮罩与标签 → 站点框 → 中枢 → 文字。节点遮住连线的微米级出头，而每个有意的端点仍落在边上。

中枢不是第七个流程步骤。它是累积的状态：记忆、标准、证据、政策，或一份共享运营记录。它的文案保持一个名字加一个短子标签。

---

## 4. 连线规则（强制）

SKILL.md §6 全文适用，两个 Loop 专属连线原语除外：圆环弧（§2.2）与直的径向辐条（§2.3）。与 Medallion 的晋升弧一样，它们在此图类型中替代 §6 规则 1：

- 环箭头是同半径圆弧、实线、顺时针。每条 path 都用 `A R R 0 0 1`；目标 marker 落在站点边上，没有连线终止于中心点。
- 辐条是虚线、指向内侧。实线辐条会毁掉运营流与回写的视觉区分。
- 标签用不透明遮罩，与连线保持可见的 6–10px 间隙。绝不把文字放在笔画上。
- 任何环连线或辐条不得与其他连线重叠。环路径保持在中枢之外；辐条各占一条径向路线。
- 两根辐条必须离开同一条站点边时，按 §6 公式展开附着点，间距至少 12px。正常 Loop 每站一根辐条；语义无法合并时才用第二根。
- 环路线会穿过中枢时，加大 `R` 或拆图。不要让流程穿过共享状态，也不要用正交路线替代。

---

## 5. 暗色变体：token 置换

套用 style-guide 的反转规则；不要发明第二套调色板。

| 角色 | 浅色 | 暗色 |
|---|---|---|
| 画布与站点填充 | `paper` | 暗色 `paper` |
| 主要文字与站点描边 | `ink` | 反转 `ink` |
| 中枢填充 / 中枢文字 | `ink` / `paper` | 反转 `ink` / 暗色 `paper` |
| 环流 | `muted` | 暗色 `muted` |
| 回写辐条与标签 | `soft` | 暗色 `soft` |
| 焦点填充 / 描边 | `accent-tint` / `accent` | 暗色 `accent-tint` / 更亮的暗色 `accent` |
| 线与点纹网格 | `rule` | 同透明度的反转 `rule` |

语义关系在暗色模式下不变：一个 `ink` 填充的中枢、一个可选的 `accent` 站点、中性实线环箭头，以及更轻的虚线回写。

---

## 6. 可复现性检查清单

1. 站点数 5–8，中枢数恰好一。
2. 站点 0 在 `-90deg`；其余按顺时针等步 `360/N`。
3. 每条实线环箭头以 `A R R 0 0 1` 连接相邻站点，共用同一 `R`；最后一个连回第一个。
4. 每个环 marker 落在站点边上，不是中心。
5. 每根虚线辐条从站点内边开始，在中枢描边前 `marker_gap` 处停下。
6. 环连线保持在中枢之外；辐条不交叉、不重叠。
7. 至多一个站点用 `accent-tint` + `accent`；只有中枢用深色 `ink` 填充。
8. 辐条标签（若有）用 `arrow-label`、不透明遮罩、6–10px 间隙。
9. viewBox 容纳站点框、描边、曲线、marker 与边距，无裁切。

---

## 7. 反模式

| 反模式 | 为何失败 / 修正 |
|---|---|
| 两个中枢 | 两个累积状态就是两套系统。画两张图。 |
| 实线辐条 | 它们看起来像主流程，杀死虚线回传信号。改用 `soft` 虚线回写。 |
| 无理由的不均匀角度站点 | 环不再读作同一个运营节拍。除非有案可查的阶段分组要求有意留空，否则用等距 `360/N`。 |
| 弧线与正交段混用 | 环变成圆角矩形。每段都必须是同半径圆弧，环才读作一个连续的圆。 |
| 连线穿过中枢 | 流与状态混淆。把环布在中枢外，或加大半径。 |
| 多个站点用 accent | 编辑焦点消失。焦点站点至多一个。 |
| 超过 8 个站点 | 标签与辐条挤满中枢。拆成总览 + 细节。 |
| 从不真正回连的环 | 那是摆成圆形的 Flowchart。用 Flowchart，并画出真实的终点。 |

---

## 8. 示例

- `assets/example-loop.html`：极简浅色，六站点自我改进运营循环。
- `assets/example-loop-dark.html`：同一几何在暗色 token 反转下。
- `assets/example-loop-full.html`：编辑风页面，含旗舰循环、三张摘要卡片与版权页。
