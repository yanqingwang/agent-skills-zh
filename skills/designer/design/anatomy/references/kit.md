> **中文汉化版** · 上游：[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) · 原文件：`references/kit.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Kit API

一切都在 `kit/iso-kit.ts`，`kit/iso-kit.mjs` 提供相同 API。世界坐标为 `[x, y, z]`，x 和 y 在地面、z 向上，单位约 1 px。屏幕坐标为 SVG viewBox 中的 `[sx, sy]`。路径以 SVG `d` 字符串返回，四舍五入到 0.1。

## 目录
1. 类型
2. 相机
3. 实体
4. 面上的线
5. 零件库
6. 移动物体
7. SVG 字符串（不依赖框架）
8. 卡片与页面
9. React 组件
10. 任意轴上的回转件（`kit/lathe.mjs`）
11. 管道、管路与线缆（`kit/tube.mjs`）
12. 审计（`kit/audit.mjs`）
13. WebGL 层（`kit/gl.mjs`）
14. 工具
15. 旋转组（`kit/turn.mjs`、`turn-build.mjs`、`turn-audit.mjs`）

## 1. 类型
```ts
type Flat = [number, number];            // screen point
type Point3 = [number, number, number];  // world point
type Plane = [number, number];           // floor point (x, y)
interface Plan { x: number; y: number; w: number; d: number; r: number }   // rounded rectangle on the floor
interface Projection { origin: Flat; scale: number; azimuth?: number; elevation?: number }
interface SolidPaths { fill; outline; crease; top; shades: string[4]; bevel?; seamless? }
type Tone = "hi" | "mid" | "lo" | "faint";
type LineTone = Tone | "lit" | "red" | "green" | "blue";
```

## 2. 相机
| 函数 | 作用 |
|---|---|
| `fitProjection(points: Point3[], width, height, { pad = 24, headroom = 0, azimuth = 45, elevation = 30 })` | 一个把这组点在 viewBox 内居中并适配的投影。传入每个极值点，例如 `boxCorners(plan, z0, z1)` 和最高的尖端。 |
| `iso(point, P)` | 世界坐标转屏幕坐标。 |
| `depthOf(point, P)` | 数值越大离观察者越近。升序排序即可从后往前绘制。 |
| `towardViewer(P)` | 指向观察者的地面方向，`[cos a, sin a]`。法线朝此方向的面可见。 |
| `screenRise(h, P)` | 高度 `h` 覆盖多少屏幕像素。 |
| `cameraOf(P)` | 原始的正弦与余弦值。 |

## 3. 实体
所有实体都是棱柱：地面轮廓竖直向上拉伸。

| 函数 | 作用 |
|---|---|
| `slabOf(plan, z, h, P, steps = 8, bevel = 0)` | 一个圆角盒子。`steps` 是每个角的采样点数（小零件用 2–4，大圆角件用 8–10）。`bevel`（0.3–1.6）在顶面沿可见边向内加一条高光线，一直延伸到轮廓角。 |
| `cylinder(cx, cy, r, z, h, P, steps = 32, bevel = 0)` | 圆柱立柱、圆饼、底脚、旋钮或垫片。小件用 16–20 steps，大圆盘用 56–72。 |
| `extrude(ring: Plane[], z, h, P, { convex = true, bevel })` | 任意地面轮廓。凹轮廓传 `convex: false`（填充变成一个个面而非凸包）。 |
| `ringOf(plan, steps)` | 以点表示的圆角矩形轮廓。 |
| `roundedPlan(plan, steps)` | 同一件事。 |
| `circleRing(cx, cy, r, steps)` | 以点表示的圆形轮廓。 |
| `insetPlan(plan, by)` | 收缩一个 plan（`by` 为负则放大）。半径会保持合理。 |
| `corners(plan, inset)` | 从四角向内缩进的四个地面点，用于底脚和螺钉。 |
| `boxCorners(plan, z0, z1)` | 八个角点，供 `fitProjection` 使用。 |
| `haloOf(plan, z, h, P)` | 用于软阴影的填充路径：`<path class="iso-halo" d=…>`。 |

`SolidPaths` 包含的内容：
- `fill`：纸色，遮住背后的一切。
- `shades[0..3]`：可见侧面，按朝光方向分档。
- `top`：顶面，更亮。
- `crease`：顶面与可见侧面相交处。
- `bevel`：可选。
- `outline`：轮廓线。

`solidSvg` 和 `<Solid>` 按此顺序绘制它们。

## 4. 面上的线
| 函数 | 绘制内容 |
|---|---|
| `onTop(points: Plane[], z, P, closed?)` | 水平面上的折线。 |
| `lineOnTop(a, b, z, P)` | 水平面上的一条线段。 |
| `planOutline(plan, z, P, steps)` | 面上的圆角矩形轮廓，用于凹槽和镶嵌（`insetPlan`）。 |
| `ring(cx, cy, r, z, P, steps)` | 面上的圆，用于螺钉环、边圈和座圈。 |
| `segment(a, b, P)` | 任意 3D 线段。 |
| `rise(at, z0, z1, P)` | 竖直线段。 |
| `pointsAt(points, P)` | 投影一组点，用于螺钉和铆钉圆点。 |
| `dotGrid(x, y, cols, rows, gap, z, P)` | 投影后的孔点阵。 |
| `topMatrix(at, z, P, along = "x")` | 把文字平铺在顶面上的变换，供 `faceTextSvg`/`FaceText` 使用。 |
| `sideMatrix(at, z, P, "left" \| "right")` | 同上，用于垂直面。 |

## 5. 零件库
| 函数 | 返回 |
|---|---|
| `knurl(cx, cy, r, z0, z1, count, P, inset = 0.4)` | 圆柱可见半面上的竖线。 |
| `sideArc(cx, cy, r, z, P, steps)` | 圆柱侧面上水平圆的可见前半段：接缝与环带。 |
| `sideSeam(plan, z, P, steps = 8)` | 盒子的对应版本：高度 `z` 处圆角轮廓的可见近半段，包住各角并正好终止于盒体的竖直轮廓边。传入盒体自己的 `steps`，并把它画成盒体的 `inner`。在盒子上画焊缝、环带、盖沿接缝或饰条就该用它：绝不要用从角点内缩的 `segment`。 |
| `ringSeam(ring, z, P)` | 任意地面轮廓版的 `sideSeam`（即传给 `extrude` 的那个 ring）。 |
| `sideRing(center: Point3, r, "x" \| "y", P)` | 垂直面上的圆：孔口、杆端、透镜。 |
| `coil(from, to, [cy, cz], r, turns, "x" \| "y", P)` | `{ back, front }` 两半弹簧，按 back → rod → front 的顺序绘制。 |
| `topTicks(from, to, step, every, edge, z, [minor, major], P, axis)` | 顶面上的 `{ minor, major }` 刻度线，从 `edge` 线沿 +y（或 +x）生长。 |
| `sideTicks(from, to, step, every, face, top, [minor, major], P, axis)` | 沿垂直面向下垂挂的刻度线。 |
| `radialTicks(cx, cy, r, count, every, z, [minor, major], P, from = 0, span = 2π)` | 表盘和转台刻度。角度 0 指向 −y，从上往下看顺时针增大。 |

## 6. 移动物体
| 函数 | 作用 |
|---|---|
| `translateAlong(P, [dx, dy, dz])` | 一个 `"translate(x y)"` 字符串，把预先构建的组按世界坐标偏移移动。用于滑座、抽屉、柱塞和升降件。 |
| `holdStill(element, [dx, dy])` | 给 `element` 内每个 `[data-hold]` 元素一个反向 translate，这样当它所在的组移动 `[dx, dy]` 屏幕单位时，裁剪保持原位。移动带有 `G.rodOut` 裁剪的条目时，都要用相同偏移调用它。 |
| `axisVector(P, [1, 0, 0])` | 一个世界单位对应的屏幕向量。用它把指针移动换算成世界移动。 |

绕 z 轴的旋转无法用屏幕变换完成：每帧或每步重建旋转后的路径。对表针、指针或小零件来说这样开销很小。

## 7. SVG 字符串（不依赖框架）
| 函数 | 说明 |
|---|---|
| `solidSvg(paths, { tone = "hi", crease = "faint", halo, lit, flat, className, inner })` | 设置了 `paths.seamless`（平滑回转着色、`sphereOf`）时，组会带上 `data-seamless`，`ISO_CSS` 以各自的颜色、宽 0.4 描每个色调区域，使众多相邻的色调面片之间不出现发丝缝。`inner` 是放在轮廓（`iso-edge`）之前的额外线条标记，用于必须压在轮廓描边之下的接缝、焊缝和环带线；React 的 `Solid` 以 prop 接收它。 |
| `lineSvg(d, { tone = "lo", dotted, dashed, flow, className, free })` | `flow` 让虚线动起来；用于沿路径移动的东西。`free: true`（或 `"start"`、`"end"`）写入 `data-free`，告诉 `scripts/lines.mjs` 这一端是有意停在裸面上的：代表印刷文字的标尺线、表针尾、指针尖。其余所有线端必须落在某个对象上。 |
| `dotsSvg(points, { size = 0.5, tone = "mid", pulse })` | 点可以带第三个值，即不透明度（`[x, y, 0.4]`），`dotsOf(..., { fade })` 就是这样让螺栓圆渐隐而不是中途截断。 |
| `fadedSvg(list, style)` | 绘制一组各自带不透明度的线，`[{ d, alpha }]` 或 `[d, alpha]`，即 `ribsOf(..., { fade })` 的返回值。按 0.05 步长把线按不透明度分组，每组放进一个 `<g opacity>`，低于 0.02 的丢弃。用于成员朝轮廓边缘逐个渐隐的纹理：棱肋、鳍片、滚花、标尺线。 |
| `fadeLineSvg(points, { fade = [start, end], tone = "lo", className, stops = 6 })` | 一条（屏幕坐标点的）线，在开头 `start` 像素和结尾 `end` 像素内渐隐而不是戛然而止（每段渐变端带 `data-free`，因此线端检查会放行）。每段渐变用沿自身弦线的 `userSpaceOnUse` 线性渐变描边（按 `stops` 步数的 smoothstep，颜色取自 `var(--anatomy-<tone>)`，两种主题都适用），中间部分是普通 `lineSvg`，因此不会出现重叠的端帽、圆珠或接缝。用于终止在面中间的纹理线：跑完即消失的凹槽、止步于角前的焊缝、曲面平板上的标尺线。渐变段要保持短于线的四分之一转，因为线性渐变沿弦线走。渐变 id 是路径的哈希，同一条线画两次共用一个。 |
| `wireSvg(from, to, { via = [], tone = "lo", dotted, dashed, flow, ends: "both" \| "from" \| "to" \| "none", size = 1.2 })` | 带端点的连接线。 |
| `faceTextSvg(transform, text, { size = 3, tone = "mid", anchor })` | |
| `groupSvg(children, { class, transform, "data-part": … })` | |
| `figureSvg({ width, height, label, body, standalone: false \| "dark" \| "light", className })` | 这个 `<svg>`。`label` 是无障碍描述：说明物体是什么、展示了什么。`className` 会附加到它的 class 上，把图形叠在 canvas 之下时有用（`rt-back`、`rp-back`）。 |

## 8. 卡片与页面
| 函数 | 说明 |
|---|---|
| `plateHtml({ fig, title, hint, readout, keys: [{ mark, label }], caption, body })` | 卡片本体。`mark` 取 `raised`、`flat`、`lit`、`edge`、`dim`、`dotted`、`dashed`、`red`、`green`、`blue` 之一。读数元素带 `data-readout`，实时代码可直接写入。 |
| `pageHtml({ title, theme = "dark", body, script, width = 650 })` | 内联了 `ISO_CSS` 的独立文档。 |
| `kitScript()` | 来自 `scripts/inline-kit.mjs`。把它放在 `script` 前面，页面动画时就能调用 `lineOnTop`、`translateAlong` 等 kit 函数。 |
| `glScript()` | 来自 `scripts/inline-kit.mjs`。`kit/gl.mjs` 的源码（`GLSL_ISO`、`glCamera`、`glLayer`、`smooth`、`burst`、`settle`），在带 shader 的页面上内联在 `kitScript()` 之后：`script: kitScript() + glScript() + live`。它不依赖 kit，实时代码不调用 kit 函数的页面可以只内联它（Raptor 用的是 `glScript() + LIVE`）。它们都在同一个模块脚本里，因此实时代码不得重复声明 `smooth`、`burst` 或 `settle`：第二个 `const smooth` 是会让页面挂掉的 SyntaxError。 |
| `turnScript()` | 来自 `scripts/inline-kit.mjs`。去掉 `export` 的 3D 运行时（`TURN`、`TURN_CSS`），供带实时部件的页面使用：`script: turnScript() + glScript() + live`。其内部标识符以 `t3`/`T3_` 为前缀，因此能与 kit 和 WebGL 层并排内联。 |
| `ISO_CSS` | 全部样式。`kit/iso.css` 是同样的内容。 |

## 9. React 组件
来自 `kit/react/draw.tsx`，服务端安全：

- `<Solid paths tone crease halo lit flat className inner />`（`inner` 是放在轮廓之下的线条标记，同 `solidSvg`）
- `<Line d tone dotted dashed flow free />`
- `<Wire from to via tone dotted dashed flow ends size />`
- `<Dots points size tone pulse />`（点可以带不透明度 `[x, y, alpha]`，同 `dotsSvg`）
- `<FaceText transform size tone anchor>text</FaceText>`
- `<IsoFigure width height label>` …svg 子元素… `</IsoFigure>`
- `<Plate fig title hint readout keys caption>` …图形… `</Plate>`

来自 `kit/react/live.tsx`，带 `"use client"`：

- `useReadout()` 返回 `{ anchor, say }`。把 `anchor` 放在根元素上；`say(text)` 写入卡片读数。
- `useLoop(tick: (dt, calm) => keepGoing, running)` 在 `running` 为真且 `tick` 返回真时运行帧循环。返回 `kick()` 可重新启动。
- `follow(current, target, dt, seconds, calm)` 是指数缓动。
- `spring(state, target, dt, stiffness, damping, calm)` 是分步弹簧。稳定后返回 true。
- `useEased(target, seconds)` 以 React state 返回缓动后的数值。小图形够用。
- `useInView(ref)`、`useStillness()`、`asksForStillness()`。
- `Stage` 是 `IsoFigure` 用的包装器。它加 `data-inview` 以支持 CSS 动画。

## 10. 任意轴上的回转件（`kit/lathe.mjs`）
`kit/iso-kit.mjs` 构建立在地面的棱柱。`kit/lathe.mjs` 把轮廓绕**任意**轴回转，用于钟形件、腔体、法兰、阀体、泵蜗壳、管接头、斜置的执行器和垂直面上的接头。它返回与 `slabOf` 相同的 `SolidPaths`，因此 `solidSvg` 可以直接绘制。引入方式：`import * as G from "../../kit/lathe.mjs"`。

**坐标系（Frame）。** Frame 是 `{ o, a, u, v }`：一个原点、单位轴向和两个单位径向方向。零件上的点表示为 `(s, r, angle)`：`s` 沿轴离开 `o`，`r` 是离轴距离，`angle` 从 `u` 转向 `v`。

| 函数 | 作用 |
|---|---|
| `frameAlong(o, a)` | 过 `o`、沿轴 `a` 的 frame，`u`、`v` 自动选好。任意角度的管子、凸台和法兰都用它。 |
| `frameOf(o, a, u, v)` | 显式指定径向方向的 frame，角度因此有确定含义：`G.frameOf([0, 0, z], [0, 0, 1], [1, 0, 0], [0, 1, 0])` 让角度 0 指向 +x。 |
| `pointOf(F, s, r, angle)` | 对应的世界坐标点。 |
| `radialOf(F, angle)`、`tangentOf(F, angle)`、`angleToward(F, direction)` | frame 内的方向，以及面向某方向的角度。 |

**实体。** 子午线是沿轴排列的 `[s, r]` 点列。加第三个元素（`[s, r, 1]`）把该环标记为平滑，该处就不画折痕线。钟形、穹顶这类曲线轮廓用它。子午线只要含任一平滑顶点就自动平滑着色（`smooth` 默认 `"auto"`，即 `softOf(meridian)`）；传 `smooth: false` 关闭，传 `true` 或 `{ rows }` 可在无平滑顶点的轮廓上强制开启，传 `{ slope }` 或 `{ slope, radius }` 则用解析曲线。

**平滑着色。** 不开平滑时每个面片行只有一个平色，曲线轮廓会呈现色块阶梯（最初的 Raptor 钟形件和喉管就是这样，评审一眼就看出来了）。开 `smooth` 后，每段子午线的侧面按插值法线着色：色调边界变成真实的等照度曲线，按 `rows` 层采样、每个色调区域输出为一个多边形，因此它们以干净的曲线贯穿整个零件。
- `smooth: true` 用单调三次 Hermite 曲线插值每段连续的平滑顶点（`[s, r, 1]`）（Fritsch–Carlson 斜率：轮廓转折处为零，其余取加权调和平均），并把这条曲线同时用于法线、色调面、轮廓和凸包，重采样直到与弦线误差不超过 0.2 px。着色与轮廓因此描述同一个形状，法线也只能在轮廓转折处变号。任何含平滑顶点的轮廓都用它：穹顶、喉管、锥体、阀鼓包、火焰锥。（自然样条在峰值附近会过冲；在阀鼓包上它曾让色带在躯体上锯齿状扭动。）
- `smooth: { slope }` 的法线取自解析 `dr/ds`，分带的躯体共享同一个法线场，色调曲线跨带缝不出现台阶。只用 `slope` 时轮廓点之间直线相连，所以要密集采样解析 `r(s)`（喉管上 20–30 个节点），束腰躯体的轮廓也用同一个 `slope`，因此外形同样贴合真实曲线。
- `smooth: { slope, radius }` 连曲面也取自解析 `r(s)`：色调面、凸包和轮廓在节点之间都跟随 `radius`，因此一条环带两个节点就够。`bandsOf` 给每条带传的就是它。
- **手敲节点不是曲线。** 单调 Hermite 只有 C1 连续：它的 `dr/ds` 是分段二次函数，在每个节点处趋平、节点间过冲，色带于是走走停停，形成扇贝状阶梯。Raptor 喉管（`[128, 31, 1], [134, 27.6, 1], …`）在 5× 放大下暴露了这一点。任何大于一个接头的曲面体都用解析轮廓加 `smooth: { slope }`：喉管是 `r = √(24.2² + (c·(s − 146))²)`，火焰锥是 `r = 48·(1 − x)^0.8` 并在尖端闭合到 `r = 0`，阀鼓包是椭圆，万向节圆饼是 `18.4 − a·|s − 297.5|⁴`。审计的 `wobble` 会列出每个开了平滑却没给 `slope`、且 `dr/ds` 在两端之间转向的轮廓。
- `rows`（默认 6）是每段的初始采样数。随后不断拆分行，直到每个色调边界与直弦的偏差都在 `error`（0.35 px）以内，并且凡带数发生变化处，细分持续到 `depth`（8）层或屏幕上的 `fineness`（0.1 px），以先到者为准，这样出现或消失的环带以零宽度的细条形式诞生，而不是终止于一条平直切口。只要某个色调自身的区域数保持不变，它就贯穿躯体的每段子午线和每个平滑节点、输出为一个多边形；区域数变化处只对该色调做桥接，时有时无的环带不再把其他色调切成一行行。这让一个小回转球的体积缩小约一半，并消除了行缝。可见性按绘制面片的法线计算，色调总能到达轮廓；每个色调多边形环绕方向一致，同一色调的重叠部分绝不会相消成洞。
- 结果标记为 `seamless`（见 `solidSvg`）。平端盖（`s` 不变的环）保留面片着色。

| 函数 | 作用 |
|---|---|
| `lathe(meridian, F, P, { steps = stepsFor(rMax, 32, 160, scaleOf(P)), fill = "auto", hole = null, bevel = 0, rims = "all", smooth = "auto", waist = 0.5 })` | 通用的回转体。面片按 kit 的光照分四档着色，分档方式同 `extrude`。`fill: "auto"` 用各环的凸包填充，除非真实轮廓比凸包内缩超过 `waist` px（喉管、线轴），这时改用两侧的 `silhouettePoints` 加可见端弧连接来填充并描轮廓（仅当轮廓沿整个侧面连续不断：表面在某个位置正对观察者的躯体，比如以直角离开颈部的阀鼓包，会退回凸包，因为拼接断开会画出杂散三角形）；`"surface"` 强制前者，`"hull"` 强制凸包；`fill: "facets"` 只填充可见面片、不画轮廓，从内部看的凹形或开放形体需要它。`hole: [s, r]` 在填充和轮廓上切一个圆孔，用于管口。`bevel` 从闭合端盖（`r = 0` 处的子午线端）向内加高光线。`rims` 控制端环上的轮廓：`"all"`、`"none"`、`"first"`、`"last"` 或 `"ends"`。只有沿第一或最后一个环的凸包边会被丢弃；内部环上的边始终保留，因此侧面轮廓完整。 |
| `solidOf(profile, F, P, options)` | 把轮廓在两端闭合到轴上，并按最大半径选 `steps`。这是做回转件的常规方式：`G.solidOf([[0, 12], [6, 12], [8, 9, 1], [20, 9]], F, P)`。 |
| `bandOfProfile(profile, F, P, options)` | 无端盖的开口带，用于被拆成深度排序多段的长躯体中的一段。优先用 `bandsOf`，它一次性切分整个躯体。 |
| `bandsOf(profile, cuts, F, P, { slope, radius, steps, rows = 6, rims = "none", fill = "auto", samples = 72 })` | 一条曲面体（`s` 沿 `profile` 递增）按 `cuts` 中的 `s` 值切成可深度排序的环带，各带共享同一法线场、同一曲面和同一面片数。传入解析 `slope` 和 `radius`，或者都不传：后者由 `profileCurve(profile)` 从轮廓推导（平滑节点段走单调 Hermite，其余走直线），因此没有任何一条带会自带端部斜率。返回 `{ bands, sidesOf, radius, slope, steps, s0, s1 }`。每条带是 `{ s0, s1, profile, paths, outline, seam }`：`paths` 已清掉自身轮廓、可直接给 `solidSvg`；`outline` 是该带自己的弦线轮廓，需要时可用（Raptor 裙部的最后一条带保留了它）；`seam` 是它与下一条带相接的可见弧（放进 `inner`）；`profile` 是给审计记录用的（`A.solid(F, band.profile, { radius })`）。`sidesOf(from = s0, to = s1, { ends = false \| true \| "first" \| "last", count = samples })` 返回 `{ d, points }`：该区间内躯体两条解析侧边合成的一条路径，可选带上两端可见的边弧，以及用于记录的 3D 点（`points.map((list) => A.tube(list, 0.4 / scale))`）。把 `d` 作为一个条目、带小的深度偏移画在环带之上，轮廓就是一条连续曲线。 |
| `profileCurve(profile, { slope, radius })` | 面向 `s` 递增轮廓的 `{ s0, s1, radius(s), slope(s) }`：即 `smooth` 穿过它画的曲线。`s` 不递增就抛错，因为轮廓上的台阶是折痕，属于另一个实体。 |
| `outlineOf(meridian, F, P, { steps, fill, hole, rims, smooth, waist })` | 只有 `lathe` 的 `fill` 和 `outline`、不含着色，供自行绘制轮廓的躯体使用。 |
| `softOf(meridian)` | 任一顶点标记为平滑时为真。 |
| `disc(s0, s1, r, F, P, options)` | 轴上的短圆柱：圆饼、法兰、凸台、销、塞。 |
| `ringBand(s0, s1, rIn, rOut, F, P, options)` | 有厚度的圆环：套在别的东西外面的法兰或箍环。 |
| `stepsFor(radius, least = 16, most = 112, scale = 0)` | 面片数量。给 `scale`（每世界单位对应的屏幕像素，`scaleOf(P)`）时，它让每个面片在屏幕上约 3 px 长；不传 `steps` 时 `disc`、`ringBand`、`solidOf`、`bandOfProfile` 和 `lathe` 都用它（32–160）。面片只决定色调填充：轮廓、边圈、折痕和倒角按约 1.5 px 从真实圆采样，并正好终止在面转向背面的位置。 |
| `saddleOf(F, a, start, s1, P, { steps })` | 鞍座垫：半径 `a`、沿 `F.a` 的圆柱，从曲面宿主表面延伸到 `s1` 处的平面。`start(angle)` 给出每条母线离开宿主的位置（用宿主 `sdf` 二分求得），或传数字 `R` 表示宿主是垂直于 `F.a` 的圆柱（此时 `saddleStart(R, a, angle)` 给出每条母线的起点）。填充是可见面片与端面的并集，轮廓是两条侧母线、鞍曲线的可见部分和端面边圈，因此它与宿主沿真实相交线贴合。曲面上装平法兰会留下边圈缝隙的地方，都用它来装法兰。 |
| `prismOf(F, polygon, s0, s1, P)` 与 `stadium(r0, r1, offset)` | 在 frame 的 `u`、`v` 平面内取任意凸 `[x, y]` 多边形、沿 `F.a` 拉伸的棱柱，带面片色调、凸包作填充和轮廓，只在尖角处有折痕。`stadium` 是两个圆的凸包，用于连接电机与执行器的变速箱板。 |
| `sphereOf(centre, r, P, { steps = 48 })` | 带精确平滑色调的球：每个色调区域是球冠的投影凸包，因此只需四个小多边形，不用回转轮廓。用于杆端轴承、三通接头和旋钮。它是 `seamless` 的。 |
| `silhouettePoints(profile, F, P, { samples = 72, slope, radius })` | `silhouetteOf` 的两条侧边，以 3D 点列表示，用于给审计记录轮廓形状。 |
| `silhouetteOf(profile, F, P, { samples = 72, slope, radius })` | 穿过 `profile`（`[s, r]` 点列，线性插值）的回转面的两条解析侧边，合并为一条含两段折线的路径：即曲面转向背对观察者处的点（`cos(θ − φ) = r′·aV/|V⊥|`）。用于在分带构建的躯体上画一条连续轮廓。表面正对观察者处（`|c| > 1`）跳过采样。传入解析 `slope`（与环带着色用的相同），边缘才不会在每个轮廓点处打结。 |

**曲面上的线与点。** 它们只画朝向观察者的部分。`slope` 是该环处曲面的 `dr/ds`，锥面或钟形面上的线因此会在真实曲面转走的地方隐藏。

| 函数 | 作用 |
|---|---|
| `arcOf(F, s, r, P, { slope = 0, steps, least = 0.02, inward = false, from = 0, to = 2π, trim = 0.3 })` | 面上圆环的可见弧：接缝、环带、焊缝、口沿。轮廓角精确求解（`t = φ ± acos(c)`），止于轮廓角的每一端都缩短 `trim` px，使圆头端帽留在轮廓描边之内。`inward: true` 画内表面上看到的弧，例如喷管内壁。`least: -1` 给出整圆。接缝画在轮廓*之下*：`solidSvg(paths, { inner: lineSvg(arcOf(…), { tone: "faint" }) })`。若追加在实体之后，浅色接缝端帽会盖住边缘描边，并在每个接缝处把轮廓切出缺口。 |
| `circleOf(F, s, r, P, steps)` | 完整闭合的圆，如端面环、孔口或待填充的空腔。 |
| `ribsOf(F, s0, s1, r, count, P, { phase, twist, least = 0.12, r1 = r, fade, seams })` | 可见的轴向线：沿任意轴的滚花、棱条或鳍片。`twist` 让它们成螺旋，`r1` 让它们沿锥面走。给 `fade: [lo, hi]` 时返回 `[{ d, alpha }]`，每条棱的不透明度是其朝向程度的 smoothstep，整组朝转折处渐隐而不是止于 `least`。用 `fadedSvg` 绘制。`seams: true`（或 `"first"`、`"last"`）把 `s0`、`s1` 处的接缝弧加进结果（全不透明度），棱条行与其终止的接缝因此共享同一个 `s`；只有棱条终止在台阶或已画出的带端时才可省略。 |
| `rodOut(F, from, to, r, P, { stroke, ...latheOptions })` | 从 `s = from` 处的密封函滑出的杆（`F.a` 指向函外），静止时杆端在 `to`，最多再伸出 `stroke`，或同一根杆缩回去。返回 `{ paths, clip, from, to, stroke, reach }`：`paths` 是从 `from − stroke` 到 `to` 的一根杆，`clip` 是覆盖从密封函面到 `to + stroke` 这段杆的路径。按 `<clipPath id><path data-hold d=clip/></clipPath><g clip-path=url(#id)>solidSvg(paths)</g>` 绘制，移动条目，调用 `holdStill`，并记录 `A.slide(F, from, to, r)`（`craft.md` 第 3 节）。 |
| `spokesOf(F, s, r0, r1, count, P, { phase, sweep, from, to })` | 面上的径向线，用于叶片和涡轮桨叶。 |
| `dotsOf(F, s, r, count, P, { phase, slope, least = 0.08, all = false, fade })` | 可见侧螺栓圆的屏幕坐标点。传给 `dotsSvg`。正对观察者的面用 `all: true`。`least` 明显大于 0 会让圆停在曲面中间；改传 `fade: [0.04, 0.42]`，圆点会带递减的不透明度。 |
| `fadeOf(value, [lo, hi])` | 两种渐隐共用的 smoothstep。 |
| `facingOf(F, angle, P, slope)` | 该角度的表面朝向观察者的程度。正值表示可见。 |

**3D 路径**，用于管道和线缆。

| 函数 | 作用 |
|---|---|
| `fillet(points, radius, perArc = 7, { P, tube, margin = 1.3 })` | 用 `radius` 大小的弯把折线的每个角变圆，上限是可用空间（短边的 0.48）。先把管道布置成几段直边，再做圆角。给 `P` 和 `tube`（管道半径）时，每个角的弯会放大到 `margin · tube / (0.7 · f²)`，其中 `f = |n · V|` 表示弯所在平面正对观察者的程度：侧向看的弯投影半径是 `R·f²`，低于管道自身半径时轮廓会自折叠。直边仍会封顶，因此紧邻朝向你的接口的转弯需要长直边或弯头接头。 |
| `resample(points, spacing)`、`pathLength(points)`、`cut(points, from, to)` | 等距重采样、总长度，以及按弧长截取的子路径。 |
| `pointAlong(points, at)`、`tangentAlong(points, at)` | 给定弧长处的位置与方向。用于在管线上放置法兰、环带、阀门和卡箍。 |
| `spiral(F, s, r0, r1, a0, a1, steps = 28)` | 渐宽螺线的 3D 点，例如泵蜗壳。连同半径函数一起喂给 `tubePieces`。 |
| `arcPoints(F, s, r, a0, a1, steps = 24)` | 绕环一周的 3D 点，例如歧管、喷淋环或线束通道。 |

**相机与向量。**
- `viewOf(P)` 是指向观察者的单位方向，因此 `dot3(p, viewOf(P))` 等于 `depthOf(p, P)`。
- `lightOf(P)` 是 kit 的光源。
- `scaleOf(P)` 是每世界单位对应的屏幕单位数。
- `toneOf(normal, P)` 和 `bandOf(score)` 给出四档色调。
- `hullOf(points)` 和 `runsOf(flags)` 是模块自己也在用的凸包与游程辅助函数。
- 向量辅助函数有 `dot3`、`add3`、`sub3`、`mul3`、`len3`、`unit3`、`cross3` 和 `lerp3`。

**分带的长曲面体。** 用 `bandsOf` 切分，让每条带与缠绕其上的管道正确深度排序。每条带共享躯体的 `steps`、法线场和曲面，色调曲线跨每个接缝无缝，轮廓来自 `sidesOf` 的一条曲线，而不是每带一段弦线、在每个接缝处打结。Raptor 钟形件：
```js
const BELL = G.bandsOf([[3.2, bell(3.2)], [116, bell(116)]], [14, 28, 44, 60, 76, 92, 106], ENGINE, P, { radius: bell, slope: bellSlope, steps: 96, rows: 8 });
BELL.bands.forEach((band, index) => put("nozzle", ex(ENGINE, (band.s0 + band.s1) / 2), S(band.paths, { tone: "hi", inner: index === 2 ? Ln(band.seam, { tone: "faint" }) : "" }), { shapes: [record(A.solid(ENGINE, band.profile, { radius: bell }))] }));
const SIDES = BELL.sidesOf(3.2, 106, { ends: "first" });
put("nozzle", ex(ENGINE, 105), Ln(SIDES.d, { tone: "hi" }), { bias: 0.2, shapes: SIDES.points.map((points) => A.tube(points, 0.4 / KS)) });
```
不要用多次 `bandOfProfile` 手工拼带、每段在两个节点的弦上各自做 Hermite 拟合：这样每条带都有自己的端部斜率，色调在每个接缝处跳变，弦线轮廓也会打结。

**已知的坑。**
- **躯体不开平滑时，四档量化会跟随每个面片行的斜率。** 把每个曲线节点都标记为平滑（`[s, r, 1]`），着色自然跟上；硬节点但仍描述曲线的轮廓需要 `smooth: true`。分带的躯体用 `bandsOf`。
- **平滑着色更重。** 开 `smooth` 的小回转球约 9 KB；`sphereOf` 不到 3 KB。球体用 `sphereOf`，小零件把 `rows` 保持低位。

## 11. 管道、管路与线缆（`kit/tube.mjs`）
```js
import { tubePieces, tubeSvg, runsOf, crossingsOf } from "../../kit/tube.mjs";
```
| 函数 | 作用 |
|---|---|
| `tubePieces(points3, radius, P, { maxLength = 30, spacing = 2.2, closed = false, breaks = [], gaps = [], caps = true, stripes = "auto" })` | 把 3D 路线切成每段至多 `maxLength` 世界单位的小段。每段画成 2D 丝带：纸色主体、朝光的高光带、背光的阴影带和两条边线。相邻段重叠 0.5 单位，边线与主体从同一段重叠区间裁出，接缝处既不露缝也不缺轮廓。每个开放端上，高光和阴影比主体多延伸 0.5，让条纹盖住下层主体的抗锯齿切口，而自己的切口落在邻段相同的条纹上；每帧法线都取整条路线上的中心差分，两段的条纹在重叠处精确重合（此前两边各按一条线裁切，蜗壳的阴影带在每个接缝处都有一条发丝线）。`radius` 是数字或 `t` 的函数（沿路线 0 到 1），用于锥度和蜗壳。`breaks` 是段必须终止的弧长位置（交叉处，或管道绕回经过零件处）。`gaps` 是不绘制的 `[from, to]` 弧长区间，因为有箍环、卡箍、阀门或接头盖住；管口在 gap 两侧平齐截断。每个紧邻 gap 的端部都加椭圆端盖（投影截面，外半弧作为边线），路线自身的两端也一样，除非传 `caps: false`（或 `[start, end]`，例如起始端藏进三通箍环的支管用 `[false, true]`），这样管道沿正确曲线贴合法兰面而不是一条平直切口。高光与阴影条纹跟随端盖：端面背向你时延伸到椭圆外侧半边，端面朝向你时延伸到内沿（画为边线），条纹不会提前止步。无 gap 的闭合路线首尾两段互相包裹。返回 `[{ mid, body, shine, shade, edges, wide, points, radii, ends, from, to }]`：`mid` 是该段世界空间中心，用于深度排序；`wide` 表示路线在屏幕上足够宽、可以画出高光和阴影带（按路线最宽处一次性判定，锥度管不会在某个接缝掉条纹；`stripes: true` 或 `false` 可强制覆盖）；`points` 和 `radii` 是该段的 3D 中心线与半径（记录下来供审计）；`ends` 指明哪些端是真实端点而非与邻段的接缝。 |
| `tubeSvg(piece, { tone = "hi" })` | 单段输出为 `<g class="tb">`。高光和阴影只出现在 `wide` 段上，然后是该段的环（`.tb-ring`），最后是边线。 |
| `tubePieces(…, { rings: { pitch = 3, twist = 0, cross = false, fade = [0.1, 0.55], phase = 0, steps = 16, tone = "lo" } })` | 跟随管道截面的纹理：编织、波纹、缠带或铠装。截面站点从路线起点起每 `pitch` 个 3D 弧长单位放一个（`phase` 可平移），图案因此在每个分段接缝处连续；每个站点画成该处截面的可见前弧，切成短段，不透明度取 `fadeOf(facing, fade)`，纹理朝两侧轮廓渐隐而不是止于硬边。`twist`（以半径计）把每个环变成螺旋，从一侧轮廓到另一侧前进那么多，`cross: true` 再加另一旋向，即编织。环会越过每段的条纹外延，接缝处后画的段在自己主体的切口上画出完全相同的一段；在真实端点和 gap 面上停止（环与端面保持三分之一 pitch，螺旋终止在端面上）。每段带 `rings: [{ d, alpha }]`；`ringsSvg(rings, tone)` 单独绘制它们。 |
| `runsOf(total, gaps)` | 长度 `total` 的路线去掉 `gaps` 后实际绘制的 `[from, to]` 区间。每个 run 各自记为一条 tube 供审计。 |
| `crossingsOf(points, centre, axis, radius)` | 路线穿过卡箍或箍环圆盘（过 `centre`、法向 `axis`、半径 `radius` 内）的弧长位置。每个位置都换成卡箍厚度的 gap。 |

`.tb-body`、`.tb-shine` 和 `.tb-shade` 的填充属于 `ISO_CSS`（以及 `kit/iso.css`），因此 `tubeSvg` 在任何 kit 页面上无需额外 CSS 即可工作。只有在页面 CSS 里重新设计管子样式时才覆盖它们，Raptor 对选中部件就是这么做的（`.it[data-on] .tb-body`）。

**管子深度排序。** 管道在多个深度之间穿行，所以每段按自己的深度绘制：以 `G.dot3(piece.mid, G.viewOf(P))` 为键放进条目列表，紧挨它经过的实体。管道在邻近部件间穿行的地方用短段（`maxLength` 6–18），平躺在地面上的环用长段（400）。要把管道拆到不同 SVG 层，就按 `piece.mid` 判断。涟漪水箱的电机电缆分三路：桥上方的段（`piece.mid[2] > Z.top - 1 && piece.mid[1] < IN.y + IN.d - 10`）归入前层 SVG、排在横杆之前；其余在缸沿上方的段归入前层 SVG、排在近端端盖之后；沿支腿下行到控制盒的一段归入中层 SVG。它的灯电缆把悬出底座边缘的段（`piece.mid[1] < BASE.y - 0.2`）送去后层 SVG。在 Raptor 这种密集图形里不要靠眼睛调这些键：记录这些段，交给 `orderKeys`（第 12 节）处理。

**任何包住管道的东西都要把它切开。** 箍环、环带、波纹管盘、卡箍或阀体都比所套的管道宽。如果管道作为一整段穿过它，这段既在箍环后面又在前面，任何键都无法排序：要么箍环挡住管道近侧，要么管道盖住箍环面。在箍环处给管道开 gap（`gaps: [[at - t/2, at + t/2]]`）：远侧段终止于箍环背面，近侧段从箍环正面开始，两者都能干净排序。Raptor 的 `pipe()` 对自己的端法兰、环带、波纹管和阀门这么做，`cable()` 则通过 `crossingsOf` 处理线束卡箍。

Raptor 的 `pipe()` 辅助函数是个好范式：
1. 对控制点做 `fillet`，弯半径 2.6 × r（至少 3）。阀门或波纹管需要至少与自身长度加两侧圆角切除（各 `r_bend · tan(turn / 2)`）等长的直边；把它放在弯上，两端就会切进管道。
2. 先算好各箍环（端法兰、环带、波纹管盘、阀体），把它们的区间作为 `gaps` 传入。
3. 对路线跑 `tubePieces`，记录每段的 `points` 和 `radii`，每个绘制 run 作为一条 tube 供审计。
4. 绘制箍环并归属给管道（`owner`），审计就不会把管道自己的法兰算成碰撞。

`cable()` 在随自身组件保留的端部加端点圆点，在接到另一组件的端部加连接器外壳（`shells: [start, end]`），这样图形拆开时每根线缆仍终止在某个对象上。两个辅助函数都接受 `free: [start, end]`，表示拆开时脱离安装座的端部；圆角都用 `{ P, tube: r }`（见 `fillet`）。必须朝向观察者离开接口的线从 `elbow`（凸台上的球，两个接合处都是球面贴合，线从球出发指向下一点）出发，转弯发生在接头内部。`pipe()` 把每个端法兰的背面放在路线端点上，也可以让线终止于 `coupling`（快接接头处的活接螺母）而不是法兰。

## 12. 审计（`kit/audit.mjs`）
```js
import * as A from "../../kit/audit.mjs";
```
**一行接入。** 建一个记录器，让每个绘制辅助函数把条目放进它、把形状记录进去，用 settle 算好键，最后以 `auditOrExit` 结束构建：
```js
const R = A.recorder(P, { order: STAGGER, spring: SPRING });
R.put({ piece: "base", at: centre, bias: 0.1, svg, shapes: [R.solid(A.slab(plan, 0, 6, { name: "base.plate" }))] });
R.route("base.cable", route, 0.6, { piece: "base", gaps, limp: true });
A.settle(R, P);
R.items.sort((a, b) => a.key - b.key);
A.auditOrExit(R, P, { crowd: [] });
```
之后 `node build.mjs --audit` 会打印报告，任一行失败即以非零码退出；不带 flag 时 `auditOrExit` 立即返回。不拆解的图形不传 `order`，每个拆解检查都退化为静置姿态。

| 函数 | 作用 |
|---|---|
| `recorder(P, { order = [], spring = {}, ground = grounded })` | `{ items, solids, tubes, routes, put, solid, route, nameFor }`。`put({ at, bias, key, name, piece, move, ride, shapes, ...rest })` 添加一个绘制条目（不传 `key` 时键为 `dot3(at, V) + bias`；其余字段如 `svg`、`route`、`chunk` 会保留在条目上），并把条目的 `move`、`ride`、`piece` 盖到其形状上。`solid(shape)` 记录一个形状并返回它，用于条目的 `shapes` 或排序层之外绘制的静态部件。`route(name, points, radius, { owner, touch, bundle, limp, gaps, closed, ends, rims, free, piece, move, ride })` 记录管道或线缆：`gaps` 之间每个绘制 run 一条 tube，带上它的 `tips`、`tipAxes`、`tipRims` 和 `free` 端，另记录路线本身供 `folds` 和 `crowding` 用。`nameFor(base)` 给重复名字编号（`base`、`base#2`、…）。`order` 和 `spring` 是实时页面的错峰与弹簧参数。 |
| `explodeStates(order, spring, { uniform = 10, stride = 4 })` | `{ depth, frames, apart }`：深度求解状态（均分份额、每个错峰边界带反转的重放帧中每 `stride` 帧、前缀状态）与间隙检查帧（所有重放帧加前缀状态）。什么都不拆开时是 `{ depth: [0], frames: [] }`。 |
| `settle(R, P, { states, skip = sameRun, ...overlapOptions })` | 运行 `overlapsOf` 和 `orderKeys` 并把键写回条目。它保持条目原有顺序，因此之后可以自行排序 `R.items`。每次构建都要跑。 |
| `audit(R, P, { allow, crowd, cover, ground, frames, apart })` | 对记录的形状跑下面所有检查，汇总为 `report` 和 `failures` 两项结果：静置、拆开和每帧的间隙，实体间隙，静置与拆开的拥挤（也含细长实体），替身形状，端接，悬空端，折返，自重叠，wobble，坐合，支撑与深度顺序。`allow` 豁免深度对，`crowd` 豁免拥挤对，`cover` 豁免替身条目。它看不到线条标记：那要对该页面跑 `scripts/lines.mjs`。 |
| `auditOrExit(R, P, { flag = "--audit", argv, ...auditOptions })` | 带 flag 时：执行 `audit`，打印报告和一行摘要，任何失败则设 `process.exitCode = 1`。 |
| `sameRun(a, b)`、`grounded(shape)` | 同一路线的相邻段（重叠检查会跳过），以及默认地面（meta 里带 `ground: true` 的形状，或名字以 `stand.` 开头）。 |
| `keyAt(item, state, V)`、`labelOf(state)`、`cameraBasis(P)` | 条目在拆解状态下的排序键（`key + lift · share`）、状态的打印标签，以及相机的屏幕右、屏幕下与朝向观察者的单位向量 `{ R, D, V }`，供自建探针使用。 |

精细图形的失败方式肉眼难以察觉，评审放大才看得见：管道或线缆穿过别的东西（静置或拆解的任何一帧）、法兰悬离安装座、零件悬空或陷入邻件、路线在屏幕上折返或收缩成一点、弯或端头压在另一条线的轮廓上、拆开时线缆端头悬空、以及重叠处两件绘制顺序颠倒。审计从真实几何测量全部这些。Raptor 上（478 个条目、1,119 个深度状态、约 4,400 个重放与前缀帧的间隙检查）键值计算每次构建约一分钟，完整 `--audit` 共约三分钟，大头是逐帧间隙。

**形状。** 构建时给绘制的每样东西记录一个形状，用世界单位：

| 构造器 | 形状 |
|---|---|
| `solid(F, profile, { radius, ...meta })` | 回转件：轮廓在两端闭合到轴上，即传给 `solidOf` 的同一份 `[s, r]` 列表。平滑节点段沿绘制所用的同一条 Hermite 曲线描迹（或沿 `radius(s)`，如 `bandsOf` 的带），因此记录的曲面就是画出来的那个，不是它的弦线。 |
| `lathe(F, meridian, { radius, ...meta })` | `G.lathe(meridian, F, P)` 的形状，描迹方式相同：任意闭合子午线（圆环、阀体、罐体）。 |
| `body(F, polygon, meta)` | 绕 `F` 回转的任意闭合 `[s, r]` 多边形，按原样处理。位于轴上的边不是表面，因此圆盘深处一点的深度是真实深度。 |
| `disc(F, s0, s1, r, meta)`、`ring(F, s0, s1, rIn, rOut, meta)` | 法兰、凸台、销、箍环。 |
| `box(min, max, meta)`、`orientedBox(centre, axes, half, meta)` | 方块；45° 的梁。 |
| `slab(plan, z, height, meta, steps = 8)`、`extruded(ring, z, height, meta)`、`cylinder(cx, cy, r, z, height, meta)` | `slabOf`、`extrude` 和 `cylinder` 的形状：同一份圆角 plan 或任意多边形环（凸凹皆可）立在地面上，圆角甲板角或 L 形支架都会按绘制原样检查。 |
| `prism(F, polygon, s0, s1, meta)` | `G.prismOf` 的形状：frame 的 `u`、`v` 平面内任意多边形沿 `F.a` 拉伸。 |
| `traced(meridian, { radius, error = 0.02, depth = 6 })` | `solid` 和 `lathe` 记录的多边形。 |
| `ball(at, r, meta)` | 球与端点圆点（`size / scale` 世界单位）。`meta.flats: [[nx, ny, nz, d]]` 切平面（保留半空间 n·(p − c) ≤ d）：`sdf` 为 `max(\|p − c\| − r, n·(p − c) − d …)`，表面采样包含平面的边圈，`boundsOf` 不变（保守）。3D 模式的关节球就记录这个。 |
| `tube(points, radius, meta)` | 带半径的管道或线缆中心线（数字、0..1 的函数，或逐点列表）。 |
| `slide(F, from, to, r, meta)` | 从 `from` 处密封函滑出的杆（一个从 `from` 到 `to` 的 `disc`）。在拆解或行程状态下摆放时，它从密封函面拉伸到 `to + offset · F.a` 而不是整体平移，因此每个检查看到的就是画出来的那根杆。放在移动条目上（带行程 `move` 的那个）。 |
| `moved(shape, offset)`、`sdf(shape, p)`、`boundsOf(shape)` | 辅助函数：平移、带符号距离（内部为负）、世界包围盒。 |

`meta` 携带 `name`（用于报告，按前缀匹配：`"nozzle.bell*"`）、`owner`（管道自己的法兰、环带和阀门）、`touch`（允许 tube 有意接触的对象名，如线束周围的卡箍）、`bundle`（同一线束的线缆可以并排，卡箍继承其线束的 bundle）、`joined`（一条开了 gap 的管道的各 run）、`limp`（线缆：不承重）、`anchor: false`（卡箍：端点不得把它当作安装座）、`fitting`（中心会被 `crowding` 与其他线检查的卡箍或箍环）、`seated`（按设计陷进宿主的垫片或球面贴合接头）、`cut`（从本形状中减去的形状或形状列表：鞍座垫就是被宿主切过的盘）以及 `curve`（无解析斜率的回转件的平滑轮廓，供 `wobble` 用）。Tube run 还携带 `tips`（路线的真实端点；端部并入躯体时为 `null`，如蜗壳起点）、`tipAxes`、`tipRims`（每端的法兰或接头半径）、`free`（拆开时有意脱离安装座的端部）、`offset` 和 `total`（run 在路线上的位置）。每个形状都带着绘制它的条目的 `move`、`ride` 和 `piece`，因此可在任意拆解状态下摆放。

**状态。** 拆解状态是一个数字（所有组件处于该份额）或 `{ label, shares }`（每个组件一个份额）。`uniformStates(10)` 给出 0, 0.1 … 1；它们不是任何人都看到的帧，只供键求解器使用。`springStates(order, { stagger, stiffness, damping, substeps, fps = 60, settle = 1e-3, stride = 1, reversals = [] })` 按实时页面自己的弹簧与错峰重放：从静置展开、从拆开收拢，每 `fps` 一帧，直到每个弹簧与目标差距小于 `settle`（Raptor 上单程约 1.2 s，因此每次收拢的慢尾巴也会被检查）。`stride: 4` 每 4 帧保留一帧，供深度栅格。`reversals` 加上快速悬停产生的路径：先展开，隔那么多秒再收拢（以及反向），调度与页面一致：反转时只重新调度目标变化的组件，它们之间互相错峰，刚出发的直接折返，还在等待的原地不动。**`reversalsOf(order, stagger)`** 在每个错峰边界两侧 8 ms 各给一个反转：坏窗口就在那里（下一次启动前 15 ms 的反转曾让热气管路飞进还停在家里的甲烷泵），三个手挑的时刻一个都没碰上。**`prefixStates(order, { shares = [0.25, 0.5, 0.75, 1] })`** 加上前缀规则背后的静态状态：前 `k − 1` 个组件全部伸出，第 `k` 个处于各份额，其余在家。沿错峰方向的份额始终不增（展开、收拢、反转时都是前面的组件领先），因此每个可达帧都落在这些静态状态之间。40 ms 采样曾漏掉整段穿越：两个采样点之间喷管移动了 15 个单位，是最宽管道的两倍多。`shareOf(item, state)` 从条目的 `ride`（或 `piece`）读取它的份额，`offsetOf(item, state)` 是其位移乘该份额。

**`overlapsOf(items, P, { step = 0.25, tolerance = 0.3, least = 0.25, states = [0], skip })`** 找每个状态下屏幕投影重叠的每一对绘制条目，在重叠区域按 `step` viewBox 单位的网格上沿相机射线对两个形状做 ray-cast。一个表面比另一个近 `tolerance` 以上时该格计为有效。每侧被标记的格子做闭运算（一次膨胀、一次腐蚀，锯齿细条变成实心），再腐蚀一次（真实接触处沿线的发丝随之消失），取最大连通块按 px² 度量；面积至少 `least` 的一侧算"在前面"。旧的 0.5 步长加 4 邻域核数时，整个法兰陷进泵壳、每条线缆交叉（0.5 的线缆不足三格宽）都被当成噪声。每个条目只在其静置位置 ray-cast 一次；任何状态下它的栅格就是那一份在屏幕上按偏移平移（对齐到网格）、深度上加 `offset · V`，对平移这是精确的。配对结果按两件的相对位移缓存，一起移动的对只测一次。Raptor 上 1,119 个状态（均分、每条重放路径每四帧、前缀状态）比旧的 61 个还便宜。`skip(a, b)` 排除某些对，例如同一管道的相邻段。

**`orderKeys(items, overlaps, { gap = 0.02 })`** 把每个单向重叠对变成该对所处状态下的规则：`keyFront − keyBack ≥ gap + shareBack · liftBack − shareFront · liftFront`。它对键是线性的，一次最长路径松弛就能同时解出所有状态，且只会把条目往后挪。无法满足的环会丢弃其最弱规则（`dropped`）。在不同位置互为前后的是 `cycles`。

**`depthOrder(items, P, { overlaps, solved, rest, allow })`** 检查每个状态下的最终顺序。静置（`rest`，默认状态 0 和 1）与每个重放弹簧帧中，每个错误对都是问题：干净颠倒、互锁、以及任何 `k + lift · share` 形式的键都无法维持的对，都会出现在屏幕上。均分状态里只算干净颠倒；那里的互锁列为通过。`allow` 接受显式豁免的 `[patternA, patternB]` 对。

**`clearances(tubes, solids, { ratio = 0.5, least = 0.2, state, only, mounts })`** 对每条 tube 采样，列出它距实体或另一 tube 小于 `max(least, ratio · r)` 的所有位置。在 run 的平端附近量的是端环，而不是会悬出切口的球。只有端部自己的安装座（边圈落在其上的形状，见 `mountsOf`）、该安装座的管道，以及共享该安装座或落到本 tube 的那条线的接头可以豁免，且只在端部 `r + gap + 1` 范围内；端部附近其他任何东西侵入都不得超过 0.1。传 `state` 摆放一切（豁免只在 tube 与安装座保持相对位置 0.05 以内时成立），传 `only: "through"` 只列穿透。tube 之间的距离是真实的截头圆柱距离，因此平端终止于法兰下方的 run 不会长出幻影圆头、让下一段看似穿入。

**`mountsOf(tubes, solids)`** 与 **`terminals(tubes, solids)`** 对每个管端找出距其端圈（按法兰或接头半径取 12 个点）最近的锚定形状，并列出端圈与其距离超过 0.15 的每个端：悬离接口的法兰、曲面躯体上的平法兰（边圈缝隙）、停在束旁或卡箍里的线缆。

**`looseEnds(tubes, solids, { state = 1 })`** 列出在该拆解状态下没有接触任何随其移动的其他归属实体的每个管端。它自己的法兰、活接或连接器外壳不算（算上的话这个检查永远不会失败：Raptor 有 25 个端只搭在自己的接头上）。标记为 `free` 的端单独作为有意为之的清单报告；其余全部算失败。

**`supports(solids, tubes, { ground, touch = 0.15, sunk = 0.5 })`** 构建实体与刚性 tube 的接触图，列出每个未连到 `ground`（默认：名字以 `stand.` 开头）的实体，以及每对相互陷入超过 `sunk` 的实体，除非它们同属一个 owner 或一方 `seated` 在另一方上（在其 `cut` 中指名）。坐合的垫片只对宿主豁免：Raptor 的点火器法兰陷入另一组件的热气垫 0.5，曾藏在一个一刀切的 `seated` 标记后面。`hanging` 列出没有连接到任何被支撑物的刚性 tube，同样算失败。

**`solidClearances(solids, { state, sunk = 0.5 })`** 摆放各实体，对该状态下偏移不同的每一对，把一方的表面点对另一方的 `sdf` 检测；陷入超过 `sunk` 即失败（坐合的垫片与宿主豁免）。在状态 1 和每个重放、前缀状态都跑：一个组件的壳体、垫片或法兰扫过另一组件躯体，tube 检查是看不见的。

**`seats(solids)`** 列出每个 `seated` 且被切给随另一组件移动的宿主的形状。拆开时它的切口底面暴露在外：热气管路的鞍座，切到甲烷泵的涡轮和圆环上，曾作为一个带尖尾的锯齿碎片飞出去。鞍座属于其宿主的组件；移动的管线在其平面上相接。

**`selfOverlaps(items, P, { fold = 0.25, least = 0.5 })`** 检查每个绘制的 tube 段自身：屏幕中心线转弯半径小于管子屏幕半宽处，丝带内缘倒行，单段轮廓自交（一个结，隐腿的边缘透出来）。该折返至少 `least` px 且该处未被其他条目盖住时失败。指向观察者、在接口一两个半径内转弯的支腿是常见原因。

**`wobble(solids, { samples = 20 })`** 对每条记录的 `curve` 每段采样 20 点的 `dr/ds`，列出 run 两端之间转向的 `s` 值。

**`folds(routes, P, { fold = 140, turn = 110, pinch = 2, items })`** 列出每个（`{ name, points, r }`）路线：屏幕方向在四个半径内转角超过 `fold` 度而实际转角小于 `turn`（背离观察者然后坠落的管道尖点），以及屏幕上绕小于 `pinch` × 管子屏幕半径的圆转过 90° 以上的每个弯，度量跨度取 1.5、3 和 6 个半径（侧看的圆角：指向观察者然后爬升的支腿形成的 V）。端部三个管宽内的 pinch 是正对观察者的短截，不计。给 `items` 时只算看得见的弯：每个都对着所有绘制形状 ray-cast。

**`crowding(routes, P, { gap = 1, bend = 30, links, items, allow, state, clear = 2 })`** 列出每处路线的弯（±2 半径内转角超过 `bend` 度的 3D 转弯）或端头在屏幕上压到另一条路线轮廓的位置：轮廓间距小于 `gap` px 或重叠，且两条线在该处都可见（对 `items` ray-cast；路线自己的法兰、外壳和卡箍算作该路线）。无论真实深度如何，这些都会被看成接头或一条线穿进另一条。弯绝不因重叠很深而豁免；端头只有当另一条线在该处是直线、且端头本身离它有余量时才豁免。每个 `fitting`（线束卡箍）也检查：轮廓落在另一条线 `clear` px 内的卡箍，会被看成那条线从卡箍里长出来，Raptor 的线束卡箍在拆开姿态里就压在氧气到预燃室的管线上。`links`（来自 **`linksOf(tubes, mounts)`**）豁免真正相接的线：一条装在另一条上，或两者共有一个安装座。`state` 把路线和条目摆到某个拆解状态，因此拆开姿态也会检查（路线带 `move`、`ride`、`piece`）。`allow` 接受你已查看并判定无碍的 `[patternA, patternB]` 对。

**`slenderOf(solids, { ratio = 4, least = 0.3 })`** 把每个细长的记录实体（长于 `ratio` × 其半径或半宽的回转件、棱柱或方块：拉杆、活塞杆、立柱、导轨、把手）变成伪路线，`audit` 以 `rods` 传给 `crowding`。tube 的弯或端头压上去就像压在另一条 tube 上一样失败（`crowding: hose.B end × cyl.tie-rod (rod)`），除非该 tube 装在它上面或装在与它相连的东西上。杆只充当被压的线：它们自己的端不检查。

**`coverage(items, P, { least = 0.6, pad = 1, allow })`** 对每个带 `svg` 字符串的条目，比较它绘制内容的屏幕包围盒（`markupBox(svg)`：每个 path、circle、line、rect 和 polyline，穿过 `transform` 和 `clip-path`，不含 halo、文本和 defs）与其记录形状的屏幕包围盒（`footprintOf(shape, cameraBasis(P))`），列出形状覆盖不足绘制 `least` 的每个条目：`stand-in shapes: rod.rod  its shapes cover 4% of its drawing`。为长杆只记录一条细条，或画三个部件的条目只记一个形状，会让其他所有检查对其余部分失明。`audit` 接受 `cover: [names]` 豁免绘制确实超出本体的条目；每个都要先看过。

**`report(result)`** 格式化全部内容；**`failures(result)`** 统计应当让构建失败的数量。

Raptor 这样接线（`examples/raptor-engine/build.mjs`）：它的 `put`、`tubeItems` 和 `record` 是 `R.put`、`R.route` 和 `R.solid` 的薄封装，构建结尾是
```js
A.settle(R, P);
items.sort((a, b) => a.key - b.key);
A.auditOrExit(R, P, { crowd: CROWD_OK });
```
实时页面从数据里读同一份 `STAGGER` 和 `SPRING`，审计与页面因此不会漂移。每个辅助函数（`turned`、`band`、`flangeAt`、`boss`、`padOn`、`boxAt`、`valveOn`、`pipe`、`cable`、`clampAt`、`strut`，以及各执行器）放入条目的同时记录形状；后层绘制的静态底座（甲板、火焰锥、喷淋环与供给、立柱、拼接件）记录为归属 `stand.frame` 的固定形状，因此把零件推进底座的拆解向量也会失败。没有东西能逃过检查。

## 13. WebGL 层（`kit/gl.mjs`）
| 导出 | 是什么 |
|---|---|
| `GLSL_ISO` | `glLayer` 前置的 GLSL 序言。包含相机 uniform（`uCanvas`、`uView`、`uOrigin`、`uK`、`uCam`、`uTime`）和函数 `viewOf`、`project`、`towardViewer`、`rayOf`、`pixelOf`、`lightDir`、`onFloor`、`onWallX`、`onWallY`、`hash12`、`hash13`、`noise2`、`noise3`、`fbm2`、`fbm3`、`window` 和 `tonemap`。不要在 fragment 里重定义任何一个：GLSL 拒绝第二个 `rayOf`。 |
| `rayOf(vb)` (GLSL) | 过原点、朝向相机的竖直平面上，viewBox 点 `vb` 下方的世界点。`rayOf(vb) + t·towardViewer()` 是该像素的完整射线；`t` 越大越靠近观察者。 |
| `pixelOf()` (GLSL) | 每个 canvas 像素对应的世界单位，`(uView.x / uCanvas.x) / uK`。除以 `uCam.z` 得地面深度方向，除以 `uCam.w` 得沿墙方向。 |
| `glCamera(P)` | 给定投影的 `{ origin, k, cam }`。可在 Node 中运行，因此放进页面 `DATA`。 |
| `glLayer({ canvas, fragment, view, camera, uniforms = [], fixed = {}, extensions = [], maxRatio = 1.5, onError })` | 返回 `{ gl, extensions, set(values), draw(values, time), clear() }`；无 WebGL 或编译出错时返回 `null`。`uniforms` 列出你每帧要传的 uniform 名。`fixed` 是 `{ name: value }`，创建时设置一次，用于一切不变的量（plan、高度、主题常量）。`extensions` 列出 GLSL 扩展，如 `"GL_OES_standard_derivatives"`；上下文支持的每个都会启用并以 `#extension … : enable` 前置，返回的 `extensions` 列出已启用的那些。 |
| `set(values)` | 只设 uniform 不绘制，用于很少变化的值。 |
| `draw(values, time)` | 适配 canvas，设置相机 uniform 和 `uTime`，再设 `values`，然后绘制。 |
| `clear()` | 清为透明，仅当画过东西。 |
| `smooth(a, b, x)` | JS 版 smoothstep。 |
| `burst(age, rise, fall)` | 事件包络：`rise` 秒的 smoothstep 起振，然后按时间常数 `fall` 指数衰减。`age ≤ 0` 时为 0。 |
| `settle(state, target, dt, seconds, calm = false)` | 作用于 `state = { x, v }` 的临界阻尼弹簧，时间常数 `seconds`，四个子步。误差与速度都低于 1e-4 即吸附到目标。仍在运动时返回 true。`calm` 直接跳到目标。 |

| `GLSL_TURN` | 3D 图形可选的 GLSL，由图形前置到自己的 fragment：`uGroupX/Y/Z/T`、`toGroup(p)`（世界 → 组的静置世界坐标）、`toWorld(g)`、`dirToGroup(d)`、`dirToWorld(d)`，以及遮盖掩码 `uCoverEdge[60]`、`uCoverCount[6]`、`coverOf(vb, soft)`（在效果之后绘制的部件内部为 1）。它定义了 `toWorld`：不要前置到自行声明 `toWorld` 的 fragment。该代码块用 70 个 uniform 向量。 |
| `glslPose(Name, prefix = "uName")` | 任意 group 的同样四个函数：基于 `prefixX/Y/Z/T` 的 `toName`、`fromName`、`dirToName`、`dirFromName`，一个 shader 可跟随多个 group。喂给它 `TURN.poseUniforms(controller, group, prefix)`。 |

`fixed`、`set` 或 `draw` 的值可以是数字（float）、长度 2–4 的数组（`vec2`–`vec4`），或长度大于 4 的数组或 `Float32Array`，后者按声明类型送入 uniform 数组：`uniform vec3 name[N]` 用 `uniform3fv`（遮盖边、火花位置），`uniform2fv`/`uniform4fv` 类推，`uniform float name[N]` 用 `uniform1fv`。这些调用不支持 int、矩阵或采样器；`sampler2D` 默认纹理单元 0，要用 `layer.gl` 绑定纹理（涟漪水箱的历史纹理）。不在 `uniforms` 或 `fixed` 里的名字，以及被编译器优化掉的 uniform，都会跳过。

`smooth`、`burst` 和 `settle` 是纯 JS：在模块里从 `kit/gl.mjs` 引入，或在内联了 `glScript()` 的页面上直接可用。`references/webgl.md` 有完整契约、最小页面和工艺规则。

## 14. 工具
| 脚本 | 用途 |
|---|---|
| `scripts/capture.mjs` | 一次性截图：桌面、手机、悬停、按键、定时截图、4× 放大、减弱动态、控制台检查。Chrome 启动即开 WebGL（允许 SwiftShader），shader 能显示。`--times` 的延迟从第一张截图算起；`--key` 发送与 `drive.mjs` 相同的键码（`7` 是 `Digit7`，`Comma` 发送 `,`）。 |
| `scripts/drive.mjs` | 无头 Chrome 中开启 WebGL 的脚本化会话：滚动、移动、点击、按键、慢放、等待、eval、截图与拼图。`--no-webgl` 检查 SVG 回退，`--preload file.js` 在页面自身脚本之前先跑一个脚本。shader 过渡和一切有序列的东西都用它。见 `references/verify.md`。 |
| `scripts/lines.mjs` | 线端检查：卡片中每条纹理线必须终止于描边、圆点或轮廓，或压在更晚的填充之下。`--out` 圈出失败项；有任何失败即以 1 退出。同一检查也是 `drive.mjs` 的 `["lines"]` 动作。见 `references/verify.md` 的 "Line ends"。 |
| `scripts/inline-kit.mjs` | `kitScript()`、`glScript()` 和 `turnScript()` 把 kit、WebGL 层和 3D 运行时作为纯脚本返回，供内联进独立页面。 |
| `scripts/drive.mjs` `["turn", value, group?]` | 3D 图形：通过 `window.__isoTurn` 设置第一个旋转组（或 `group`，或一个值对象），然后等两帧。 |
| `scripts/drive.mjs` `["orbit", out.png, from, to, step, sel?, scale?, [x,y,w,h]?, columns?]` | 3D 图形：跨角度的拼图，每帧标注 θ°。整圈用 15°；顺序变化处用 0.1°；易折弯处用 1°。 |
| `scripts/turn-check.mjs` | 3D 图形。`build.mjs --fidelity`（Node：棱柱、圆角件、回转件与 tube 对照 kit 构建器在 P′(θ)）；`page.html --order`（需要 `--verify` 构建）、`--pops`、`--lines`、`--perf`、`--states file.json`、`--part name`、`--out dir`。每项检查先跑它埋设的对照。`references/3d.md` 第 14 节。 |
| `scripts/turn-bench.mjs` | 3D 图形：Node 中跨 360 角度的 `emit` 与 `order` CPU 时间，按部件种类（7 次取中位数）。 |

## 15. 旋转组（`kit/turn.mjs`、`turn-build.mjs`、`turn-audit.mjs`）
可选的 3D 模式。`references/3d.md` 是指南；这里是参考。
```js
import { turning, separate, gjk } from "../../kit/turn-build.mjs";
import { TURN, TURN_CSS } from "../../kit/turn.mjs";
import * as TA from "../../kit/turn-audit.mjs";
```

### `turning(P, { recorder, scale = 1 })` → `T`
| 成员 | 作用 |
|---|---|
| `T.group(name, { parent?, turn: { pivot } \| slide: { direction, travel } \| hinge: { point, axis, range } \| free: { origin } })` | 刚性组。取值：角度（turn、hinge）、世界单位（slide）、`{ R \| q \| axis+angle, t, world? }` 或 `null`（free）。 |
| `T.layer(name)`、`T.stack(names)` | 实时层，以及实时与静态层名完整的由后至前栈。 |
| `T.prism`、`T.round`、`T.lathe`、`T.ball`、`T.tube`、`T.fixed`、`T.plane`、`T.billboard`、`T.split` | 部件，静置时用世界坐标。常用选项 `{ name, group, layer, tone, crease, lit, material, owner, details }`。签名见 `3d.md` 第 4 节。 |
| `T.build({ statics, poses, verify, strict })` | `{ svg, data, css, report, layerSvg(name, { width, height }), verify, planesByName }`。 |
| `T.parts`、`T.groups`、`T.layers`、`T.routes`、`T.data`、`T.built` | 场景数据，供审计和各项检查使用。 |

`details`：`seams`、`ribs: { s0, s1, count, phase, twist, fade, seams, tone }`、`bolts: [{ s, r, count, phase, size, tone, fade }]`、`dots: [{ at, normal, size, tone }]`、`rings: [{ at, normal, r, tone }]`、`rules: [{ points, tone, free }]`、`bevel`。每个构造器只取自己 frame 内的子集（球的 `s` 沿其第一个平面的法线；棱柱只接受 dots、seams 和 bevel）：见 `3d.md` 第 4 节的表。材质：`gold`、`chrome`、`steel`、`gunmetal`、`rubber`、`brass`、`copper`。

`separate(A, B, hints)` 和 `gjk(A, B, warm)` 对两个点集返回 `{ n, d, margin }`（构建时的平面求解器）。

### `TURN`（运行时）
| 成员 | 作用 |
|---|---|
| `TURN.mount(stage, data, { onHold, onFrame, follow })` | 控制器：`set(values \| θ, { detail })`、`render()`、`angleAt(x, y, z, group)`、`values`、`pose(name)`、`detach(name)`、`anchor(group, restPoint, restDir?)`、`cover(names, options)`、`order(layer)`、`orderIndex(layer)`、`events()`、`stats()`、`frames()`、`cams()`、`scene()`、`destroy()`。安装 `window.__isoTurn`。 |
| `TURN.cover(controller, names \| [names…], { polygons = 6, edges = 10, pad = 0.3, layers })` | 供 `coverOf` 用的 `{ uCoverEdge, uCoverCount, dropped, parts }`。 |
| `TURN.poseUniforms(controller, group, prefix = "uGroup")` | 供 `GLSL_TURN` 或 `glslPose` 用的四个 `vec3`。 |
| `TURN.anchor(scene, cams, group, point, dir)`、`TURN.floorOf(scene, group, R)` | 控制器之外的锚定；旋转下组的最低 z。 |
| `TURN.rotation(axis, deg)`、`TURN.quat(q)`、`TURN.compose(A, B)` | 以 `[9]` 表示的旋转，用于自由姿态。 |
| `TURN.materials`、`TURN.materialCss()`、`TURN.css()`、`TURN_CSS` | 材质名；CSS。 |
| `TURN.camera`、`TURN.poses`、`TURN.cams`、`TURN.prepare`、`TURN.emit`、`TURN.order`、`TURN.frame`、`TURN.gjk`、`TURN.disjoint`、`TURN.q`、`TURN.levels` | 供工具使用的流水线：每个 group 的相机、预备好的场景、单个部件的 frame、一个层的顺序。 |

### 轨道审计（`kit/turn-audit.mjs`）
| 导出 | 作用 |
|---|---|
| `orbitOrExit(T, R, P, { flag = "--audit", argv, sweep, clips, poses, crowd, cover, fittings, quick, only, log })` | flag 存在时运行 `orbit`，打印报告，任何失败设退出码 1。只有完整运行才以 `turn audit passed` 结束；带 `only` 以 `turn audit partial` 结束，带 `quick` 以 `turn audit quick` 结束（`3d.md` 第 13 节）。 |
| `orbit(T, R, P, options)`、`orbitReport(result)`、`orbitFailures(result)` | 检查、报告文本、失败数。`result.skipped` 列出 `only` 略过的检查线（打印为 `skipped`）；`result.quick` 在快速运行时设置。 |
| `posed(shape, pose)`、`eventsOf(T, layer)` | 被组姿态移动后的记录形状；一个层的侧视角度。 |
