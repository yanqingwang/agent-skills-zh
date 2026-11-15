> **中文汉化版** · 上游：[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) · 原文件：`references/webgl.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 绘图中的 WebGL（WebGL inside the drawing）

如何把 shader 效果（火、水、光、辉光）放进等距（isometric）图形内部，让它读起来是同一物体的一部分、透过同一台相机看到。两个已发布的示例做到了这一点：`examples/raptor-engine/`（火箭引擎下方的羽流、激波、水花与蒸汽）和 `examples/ripple-tank/`（焦散、阴影与波纹水面）。阅读本文时对照它们的 `live.js`。

用户喜欢第一张 shader 图，但注意到各相位之间颜色瞬间切换，仿佛效果被切过。所以标准是：**没有任何东西突跳，没有任何东西被切，一切都处在图形的透视之中。** 下面的每条规则都来自一个打破该标准的 bug。

## 目录
1. 什么时候值得用 shader
2. 图层堆叠
3. 相机契约
4. iso 相机中的光线步进
5. 把 shader 内容对准 SVG
6. API 与最小页面
7. 工艺规则，每条都附上教会它的 bug
8. 浅色主题（8b. 转动组上的 shader）
9. 验证
10. 性能

## 1. 什么时候值得用 shader

线条画不出来的东西才用 shader：发光与辉光、火焰与尾焰、水面、焦散、真实灯具的软阴影、烟与蒸汽。它们是连续场，而且是主体本身或主体做的事。

不要用于：
- **实体件。** 零件、边、刻度与螺丝保留用套件画的 SVG。shader 永不绘制 SVG 能画的零件。
- **装饰。** 微光、背景渐变、每条边都加 bloom，或为了让图显得"丰富"而加的噪声。如果删掉这个效果解释依然成立，就删掉它。
- **SVG 已经能表现好的东西。** 发光的 LED 是一个 `lit` 点，不是 shader。

SVG 必须仍能独立读。没有 WebGL 时 Raptor 依然显示引擎，带轮廓光与 CSS 台面辉光。涟漪水槽把波峰与波节线画成 SVG 线（`model.mjs` 里的 `patternOf`），裁剪到水槽在纸上的投影轮廓内，并在 WebGL 运行后用 `.rt-stage[data-gl] .rt-fallback { display: none }` 隐藏它们。

## 2. 图层堆叠

shader 无法与 SVG 做深度测试，所以只能靠排图层。基本堆叠是一个 `position: relative` stage 里的三层，viewBox 全部相同：

```
back SVG     what the effect covers        (k.figureSvg: role="img" and the label)
canvas       the effect                     (position:absolute; inset:0; pointer-events:none)
front SVG    what covers the effect        (aria-hidden)
```

对每个部件问一个问题：**它是否会被效果盖住，或者它是否盖住效果？** 被盖住的部件放后层 SVG，盖住效果的部件放前层 SVG。如果一个部件两者都占，你有三个选择：

- **拆分画面。** 把该部件切成几段，每段送进它所属的图层和该层中的槽位。涟漪水槽的电机线缆是三组 `tubePieces`：过桥的一段放在前层 SVG 的 bar 之前，沿近侧边缘的一段放在前层 SVG 的近侧端盖之后，沿左腿下行到控制盒的一段放在中层 SVG。
- **在 shader 里建模。** 如果该部件是简单形状（盒、圆柱、环面）并留在后层 SVG，就把这个形状作为遮挡物交给 shader。Raptor 的立柱是不透明盒（`columnNear`），所以每段空气积分从 `max(tGround, tColumn)` 开始。喷淋环是 `groundHit` 内的一个环面，所以水花照亮它的内侧、外侧保持暗。
- **拆分效果。** 当效果跑到前层 SVG 部件之前时，在前层 SVG 之上再加一块 canvas。被遮挡部件的解析代理决定每个样本去后层 canvas（权重 `1 − f`）还是前层 canvas（权重 `f`）。每个样本只画一次，所以没有接缝。代理要宽松：在真实轮廓之外，两层看起来一样。

### 实例：Raptor
```
back SVG    deck, feet, flame cone, deluge ring, columns, ladder, cable tray
canvas      .rp-plume: plume volume, shock (back half), flash, splash, ground ring, steam behind the engine
front SVG   every engine item (depth-sorted .it groups), pipes, harness, crosshead
glow SVG    .rp-glow: the two nozzle-lip rims, screen-blended so they can only add light
canvas      .rp-veil: steam and shock samples that lie in front of the engine
div         .rp-flash: a CSS radial gradient (closest-side) for the ignition flash
```
引擎代理是 `engineR(z)`，钟形喷管、燃烧室与泵的半径函数。`inFront(p, V)` 判断样本 `p` 是否位于引擎与观察者之间。`side(front, veil)` 把样本送去其中一个 canvas。

### 实例：涟漪水槽
```
back SVG    base plate, feet, ruler, label plate, paper sheet with tape, lamp cable over the base edge, SVG fallback pattern
canvas      .rt-paper-gl: lamp light on the paper and base, caustics, shadows of the legs, post, bridge, motor, control box and foam beach, refraction
middle SVG  post, arm, lamp and its cables, control box, motor cable down the left leg in clips, legs with levelling screws,
            far rails, three corner posts, far glass, foam beach, plain-water fill
canvas      .rt-water-gl: window reflection and room-light glints, meniscus tilt at the walls, dipper contact rings,
            the water band behind the near glass, glass tint, the lamp's beam (dark only)
front SVG   far caps, motor cable over the bridge, far pillar and spring, bar, dippers, motor, near spring, near rails,
            glass bottom, water lines, near glass, near caps, motor cable on the rim, near corner post, near pillar, beam
```
两块 canvas 处于两个深度，因为有两个处于两个高度的效果：纸上的光（腿下）与水面（槽内）。控制盒立在水槽旁的底座上，位于水 canvas 之下，所以它放在中层 SVG；近侧角柱画在它所立的端盖之后。

堆叠的 CSS（改自 `ripple.css`）：
```css
.fx-stage { position: relative; touch-action: pan-y; }
.fx-stage > svg, .fx-stage > canvas { display: block; width: 100%; height: auto; }
.fx-stage > .fx-layer { position: absolute; inset: 0; height: 100% !important; pointer-events: none; }
.iso:not([data-theme="light"]) .fx-gl { mix-blend-mode: screen; }
```
screen 混合只能提亮。必须同时压暗所盖内容的 canvas（涟漪水槽的水，它会给透过它看到的纸染色）在深色下也保持普通预乘混合：只有 `.rt-paper-gl` 用 screen 混合。
如果前层 SVG 要接收 hover（Raptor 的部件需要），给它 `pointer-events: none`，给它的元素 `pointer-events: visiblePainted`，这样 canvas 和空白区域永远不会捕获指针。

## 3. 相机契约

`kit/gl.mjs` 把 `GLSL_ISO` 前置到你的 fragment。它声明的 uniform 与函数让 shader 看到与 `iso()` 相同的相机：

| 名称 | 是什么 |
|---|---|
| `uCanvas` | 画布尺寸，单位为设备像素。 |
| `uView` | viewBox 尺寸 `[W, H]`。 |
| `uOrigin`、`uK` | 投影原点，以及每个世界单位对应的屏幕单位数（`glCamera(P).k`，等于 `scaleOf(P)`）。 |
| `uCam` | 方位角与仰角的 `(sinA, cosA, sinE, cosE)`。 |
| `uTime` | 你传给 `draw` 的时间。 |
| `viewOf(gl_FragCoord.xy)` | 设备像素转 viewBox 点（会翻转 y）。 |
| `project(vec3 p)` | 世界坐标转 viewBox，与套件的 `iso()` 完全一致。 |
| `towardViewer()` | 单位 3D 视线方向，`(cosA·cosE, sinA·cosE, sinE)`。每个 `p + t·towardViewer()` 都落在同一像素。与套件的 JS 版 `towardViewer(P)` 不同，后者返回 2D 地面方向。 |
| `rayOf(vb)` | `vb` 下方、过原点且朝向相机的竖直平面上的世界点，因此 `rayOf(vb) + t·towardViewer()` 就是该像素的光线。 |
| `pixelOf()` | 屏幕上每个 canvas 像素对应的世界单位数，`(uView.x / uCanvas.x) / uK`。 |
| `lightDir()` | 套件的光照，等于 `lightOf(P)`，因此 shader 的明暗与 SVG 色调一致。 |
| `onFloor(vb, z)` | 该像素下方、高度 `z` 的水平面上的世界点。 |
| `onWallX(vb, x)`、`onWallY(vb, y)` | 该像素下方、竖直平面 `x = const` 或 `y = const` 上的世界点。 |
| `hash12`、`hash13`、`noise2`、`noise3`、`fbm2`、`fbm3` | 哈希与值噪声，外加 4 倍频 fbm。 |
| `window(x, a, b, soft)` | 在 `[a + soft, b − soft]` 内为 1，在 `[a − soft, b + soft]` 外为 0：以每个边界为中心、宽 `2·soft` 的 smoothstep，所以在 `a` 与 `b` 处为 0.5。 |
| `tonemap(c, exposure)` | `1 − exp(−c·exposure)`。用它代替 `clamp`。 |

`onFloor` 与墙面函数和 `iso()` 精确往返：`project(onFloor(vb, z)) == vb`。这就是 shader 内容能与 SVG 线对准的原因。

**为什么用世界空间。** 图形的透视就是投影。如果你在屏幕空间画效果（目测尺寸的椭圆、以像素计的辉光柱），它不可能与图形一致。它会浮在地面之上、穿过台面，或者在相机变化时保持同样形状。一切都从世界点与世界尺寸构建。屏幕尺寸只来自世界单位乘 `uK`。

以世界单位做抗锯齿：`pixelOf()` 是屏幕上每个设备像素对应的世界单位。在深度方向的地面处，把它除以 `uCam.z`（sinE）；在墙面上则除以 `uCam.w`（cosE）。把对准过的边缘软化约 `0.7 * px`，这样边缘出来正好一个像素的柔度：像 SVG 一样清晰，但不锯齿。折射拉伸图像的地方，固定柔度会阶梯化；涟漪水槽启用 `GL_OES_standard_derivatives`，用 `length(fwidth(q.xy)) / length(fwidth(rest))`（移位点的足迹除以未移位足迹，静止时恰为 1）加宽其阴影半影，并以 `#ifdef GL_OES_standard_derivatives` 作回退。

## 4. iso 相机中的光线步进

相机是正交投影且比例均匀：投影的两行都是标准正交的。由此得到三件事。

- **每个像素都是一条直线** `p(t) = p0 + t·V`，其中 `V = towardViewer()`，`p0` 是该像素下任意世界点。取 `p0 = onFloor(vb, h)`，或套件的 `rayOf(vb)`，即过原点且朝向相机的竖直平面上的点（Raptor 的光线状态从那里开始：`S.g0 = rayOf(vb)`）。`t` 越大越靠近观察者。
- **到点的距离就是屏幕距离。** 屏幕距离除以 `uK` 就是从像素光线到世界点的精确垂直距离。球状闪光、冲击壳或辉光球可以用该距离计算，且仍然是世界正确的。最近接近参数是 `tc = dot(C − p0, V)`。
- **遮挡物之后的可见比例。** 若沿光线的第一个不透明表面在 `tLow`，以 `tc` 为中心、宽 `sigma` 的高斯的可见度为 `1/(1 + exp(2.41·(tLow − tc)/sigma))`（Raptor 的 `beyond`）。这给出一个柔和的切分，但仍是几何意义上的。

对一个体积步进：
1. **找到第一个不透明命中**：沿光线找地面，加上 SVG 画的任何高度场。Raptor 从火焰锥尖上方下行步进 28 次到台面，然后在 `ground(r)` 高度场上二分 7 次，该高度场由与 SVG 车削轮廓相同的数字构成。只有命中之前的光线部分（`t > tLow`）是空气。
2. **用简单形状限定步进范围**（Raptor 用一个半径 132 的圆柱，从地面命中到出射平面）。在该界之前把每一项窗口化到恰好为零，这样这个界只是一种优化。
3. **带抖动采样。** 用 `t = ta + (i + hash12(gl_FragCoord.xy))·dt`，28 个采样才不会成带。
4. **按弦长归一每一项**，这样无论步数多少，中心像素都得到预期亮度。对竖直轴体积，`r² = u² + (t·cosE)²`，半径 `σ` 的高斯沿光线积分为 `σ√π / cosE`：每个样本按 `dt·cosE/(σ·1.772)` 加权。
5. **预期均匀圆柱看起来更柔。** 其投影轮廓是 sqrt 形，失去了平面图那种明确的边。深色下加一个边缘壳（Raptor 在 `0.9·Re` 处的橙色剪切层）把边找回来。浅色下同样的壳会给空心火焰描轮廓，所以浅色下改为把主体向轴加权（见 8.4 节）。

有些项不需要步进：
- 沿光线看去，薄的水平圆盘就是精确的椭圆。Raptor 的马赫盘保持解析式：`u² + ((s0 − sc)/tanE)² < rm²`。
- 薄球壳沿光线积分会出现边缘增亮：亮度正比于 `rs·w / sqrt(rs² − d² + 2·rs·w)`。把归一化轮廓平方，否则内部读起来像乳白泡泡。

## 5. 把 shader 内容对准 SVG

凡位于某个平面上的东西，都必须与该平面的 SVG 线精确对齐。
- **同样的数字。** 通过 `DATA` 把 SVG 的平面图与高度传给 shader（涟漪水槽传 `inside`、`outside`、`paper`、`base`、`round`、`z` 以及所有投影物的平面图），并在创建时一次性作为 `fixed` uniform 交给 `glLayer`（即其 `FIXED`）。用带符号距离的 `sdRect` 对同样的圆角矩形测试，让被照亮的纸角正好落在画出的圆角半径上。
- **同一个平面。** 涟漪水槽对玻璃后面的水带使用 `onFloor(vb, uZ.x)`（纸）、`onFloor(vb, uZ.z)`（水），以及 `onWallX(vb, uNear.x)` 与 `onWallY(vb, uNear.y)`（两面近侧玻璃墙）。绝不用屏幕偏移。
- **透过开口看的内容要做双重遮罩。** 位于更近平面上开口之后的内容（观察窗、窗户、凹槽、表盘面），由其自身平面（`onWallY(vb, back)`）与在开口平面内测试的开口（`onWallY(vb, face)`）双重遮罩，两个软遮罩相乘。只做背面遮罩时，盲测中的观察窗把油和玻璃溢出顶沿约 0.4 px 到机体面上，底部则因偏移露出开口内一条裸露机体。凹槽的内壁画在前层 SVG，按朝向着色（`craft.md` 第 10 节），这样两个平面的偏移读起来是墙，而不是裸面。
- **只移动偏差。** 如果效果会位移所见内容（透过波纹的折射），只应用与静止状态不同的部分。涟漪水槽分别计算被波面弯折与被平水面弯折的视线，只应用两者之差。静止时，水下的纸与 SVG 的纸对齐。当看向纸的视线经过离腿几单位以内时（`legClear`），位移也淡化为零，这样折射出的纸绝不会从中层 SVG 所画、盖在它上面的腿后面滑出来。
- **高度场与车削轮廓一致。** Raptor 的 `ground(r)` 是台面圆盘加火焰锥轮廓，半径与高度与 `build.mjs` 里 `G.solidOf` 的轮廓相同。锥后的流动被几何隐藏，硬边只出现在 SVG 画出真实轮廓的地方。

用 4× 检查对准（第 9 节）。

## 6. API 与最小页面

```js
import { GLSL_ISO, glCamera, glLayer, smooth, burst, settle } from "../../kit/gl.mjs";
import { kitScript, glScript } from "../../scripts/inline-kit.mjs";
```

| 函数 | 作用 |
|---|---|
| `glCamera(P)` | 为套件投影给出 `{ origin, k, cam }`。在 Node 和浏览器中都可用。放进页面 `DATA`。 |
| `glLayer({ canvas, fragment, view, camera, uniforms = [], fixed = {}, extensions = [], maxRatio = 1.5, onError })` | 在 `canvas` 上用预乘 alpha 的 WebGL1 上下文编译 `GLSL_ISO + fragment`。`view` 是 viewBox 的 `[W, H]`，`camera` 是 `glCamera(P)`，`uniforms` 列出每帧发送的 uniform 名。`fixed` 是 `{ name: value }`，为创建时一次性设置的 uniform（几何、主题常量）。`extensions` 列出 GLSL 扩展（`["GL_OES_standard_derivatives"]`）；上下文支持的会被启用并前置为 `#extension` 指令。返回 `{ gl, extensions, set(values), draw(values, time), clear() }`，其中 `extensions` 列出实际启用的扩展；WebGL 缺失或 shader 编译失败时返回 `null`（`onError` 默认为 `console.error`，接收日志）。 |
| `set(values)` | 只设置 uniform，不绘制。 |
| `draw(values, time)` | 把 canvas 调整为其 CSS 盒 × `min(maxRatio, devicePixelRatio)`，设置相机 uniform，设置 `uTime = time`，设置 `values` 中每个值，并画一个全屏三角形。 |
| `clear()` | 清为透明，仅当画过东西时。 |
| `smooth(a, b, x)`、`burst(age, rise, fall)`、`settle(state, target, dt, seconds, calm)` | 每个 shader uniform 都应骑在上面的 JS 包络（第 7 节与 `motion.md`）。`settle` 在仍在运动时返回 true。 |
| `glScript()` | `kit/gl.mjs` 的源码，剥掉 `export`，用于在 `kitScript()` 之后内联进独立页面。该页面的 live 代码直接使用 `glLayer`、`smooth`、`burst` 与 `settle`，不得自己声明。 |

uniform 值（在 `fixed`、`set` 或 `draw` 中）可以是数字（float）、长度 2–4 的数组（`vec2`–`vec4`），或长度超过 4 的数组或 `Float32Array`，用 `uniform1fv` 发给 `uniform float name[N]`：24 个采样的历史就是一个 `uH[24]`。这些调用不支持 int、矩阵或采样器。超过 uniform 数组容量的数据用纹理：`sampler2D` 默认读 0 号单元，所以在 `layer.gl` 上创建并更新它。涟漪水槽把 32 × 2 的历史打包进一张 RGBA8 纹理，每值 16 位（`PACK`、`put`、`unpack`），每层一张纹理，因为每层有自己的上下文。未知名字与被编译器优化掉的 uniform 会被跳过。

你的 fragment 声明自己的额外 uniform，以及一个写入**预乘** `gl_FragColor` 的 `main()`。canvas 必须与各 SVG 覆盖完全相同的盒子、相同的纵横比，因为 `viewOf` 假设比例均匀。

最小页面：方形台面上方一块发热板发光。板与半径 40 的 SVG 圆环对准（`k.ring(0, 0, 40, 0, P, 72)`），辉光止于台面圆角边缘，因为之外没有东西可照亮。

`build.mjs`：
```js
const P = k.fitProjection(points, W, H, { pad: 28, azimuth: 40 });
const DECK = { x: -90, y: -90, w: 180, d: 180, r: 8 };
const DATA = { W, H, camera: glCamera(P), plateR: 40, deck: [DECK.w / 2, DECK.r] };
const backSvg = k.figureSvg({ width: W, height: H, label: LABEL, body: back });
const frontSvg = `<svg xmlns="http://www.w3.org/2000/svg" class="iso-svg fx-layer" viewBox="0 0 ${W} ${H}" aria-hidden="true">${front.join("")}</svg>`;
const stage = `<div class="fx-stage" tabindex="0">${backSvg}<canvas class="fx-layer fx-gl" aria-hidden="true"></canvas>${frontSvg}</div>`;
const page = k.pageHtml({ title, theme, body: `<style>${CSS}</style>${k.plateHtml({ ...card, body: stage })}`, script: kitScript() + glScript() + LIVE.replace("__DATA__", JSON.stringify(DATA)) });
```

`live.js`：
```js
const D = __DATA__;
const stage = document.querySelector(".fx-stage");
const still = matchMedia("(prefers-reduced-motion: reduce)");
const LIGHT = document.body.dataset.theme === "light" ? 1 : 0;
const FRAGMENT = `
uniform float uHeat;
uniform float uLight;
const float R=${D.plateR.toFixed(1)};
const vec2 DECK=vec2(${D.deck[0].toFixed(1)},${D.deck[1].toFixed(1)});
float deckDist(vec2 p){vec2 q=abs(p)-DECK.x+DECK.y;return length(max(q,0.))+min(max(q.x,q.y),0.)-DECK.y;}
void main(){
  vec2 vb=viewOf(gl_FragCoord.xy);
  float px=pixelOf()/uCam.z;
  vec3 p=onFloor(vb,0.);
  float r=length(p.xy);
  float disc=1.-smoothstep(R-.7*px,R+.7*px,r);
  float onDeck=1.-smoothstep(-.7*px,.7*px,deckDist(p.xy));
  float halo=exp(-pow(r/(R*1.6),2.))*onDeck;
  vec3 col=tonemap(vec3(1.,.42,.12)*(disc*.9+halo*.35)*uHeat,1.2);
  float a=max(col.r,max(col.g,col.b));
  vec4 dark=vec4(col,a);
  vec4 light=vec4(vec3(.62,.24,.08)*a*.8,a*.8);
  gl_FragColor=mix(dark,light,uLight);
}`;
const layer = glLayer({ canvas: stage.querySelector(".fx-gl"), fragment: FRAGMENT, view: [D.W, D.H], camera: D.camera, uniforms: ["uHeat"], fixed: { uLight: LIGHT } });
if (layer) stage.setAttribute("data-gl", "");
const heat = { x: 0, v: 0 };
let target = 1, clock = 0, last = 0, frame = 0, visible = false;
function tick(now) {
  const dt = last ? Math.min((now - last) / 1000, 1 / 30) : 1 / 60;
  last = now;
  clock += dt;
  const moving = settle(heat, target, dt, 0.35, still.matches);
  if (layer) heat.x > 1e-3 ? layer.draw({ uHeat: heat.x }, still.matches ? 0.8 : clock) : layer.clear();
  frame = visible && moving ? requestAnimationFrame(tick) : 0;
}
const run = () => { if (!frame && visible) { last = 0; frame = requestAnimationFrame(tick); } };
new IntersectionObserver((entries) => { visible = entries[entries.length - 1].isIntersecting; if (visible) run(); }, { rootMargin: "120px 0px" }).observe(stage);
```
没有 `uTime` 动画时，这个循环在热量稳定后就停止。有动画场（闪烁、流动）时，效果高于其活动阈值且可见就保持运行，否则停止。

## 7. 工艺规则，每条都附上教会它的 bug

### 没有任何东西突跳
每个 uniform 都沿时间上的平滑包络运动，有起振和衰减。绝不在单帧内把值设为 1。

- **一次性事件用 `burst`。** 第一版点火闪光在单帧内从 0 冲到满，把卡片闪成全白。现在每个事件（闪光、冲击、地面环、关机噗声、卡片抖动）都用 `kit/gl.mjs` 里套件的 `burst(age, rise, fall)`，smoothstep 起振加指数衰减：
  ```js
  const flash = calm ? 0 : burst(sinceMain, 0.08, 0.13);
  ```
  起振 50–90 ms（起始斜率为零）。alpha 函数 `t·e^(−t)` 把衰减与起振绑在一起，全白时间太长。整卡闪光也要压低：一次闪光加 0.9 不透明度的 CSS 遮罩曾把整张卡片闪白六帧，所以遮罩现在是 `flash × 0.32`。
- **相位变化是由物理量驱动的交叉淡化。** 一个随主羽流增长而消失的独立预燃项读起来像瞬间变色。现在颜色、亮度、毛糙度、火舌长度与水花都是燃烧室压强的函数，压强在弹簧上朝每个相位的目标移动。
- **颜色有自己的慢包络。** 即使由压强驱动，橙变紫在快弹簧上约 0.23 s 就穿过了 smoothstep 窗口，亮度在 130 ms 闪光内跌了 33% 又回来：一个被闪光藏住的切换。修复：
  - 色相有自己的临界阻尼包络，套件的 `settle`：`settle(burn.hue, lit && burn.pc > 0.2 ? 1 : 0, dt, lit ? 0.32 : 0.5, calm)`，以 `uHue` 发送。
  - 亮度是单独的 `uGlow`，在 JS 里计算，色相上升时它从 1.15 单调降到 1.0。
  - 压强弹簧是临界阻尼的（刚度 20，阻尼 2√20），不会过冲到 318 bar。
- **淡出期间亮度只降不升。** 关机时羽流又窜成橙色火焰，因为 `b < a` 时 `mix(a, b, hue)` 会随 hue 衰减而回升。现在关机一开始辉光级别就冻结，之后只被下降的量缩放。
- **改弹簧后要复查邻居。** 压强弹簧改成临界阻尼后，预燃火舌几乎消失。那条腿需要自己更硬的临界弹簧（刚度 64）。
- **一次性标志属于事件本身。** 关机后 2 s 内重新点火会丢失下一次关机噗声，因为噗声的时钟只在安静期后重置。现在由每次燃烧的 `popped` 标志决定。在 `ignite()` 里重置时钟会截断还在淡出的噗声。
- **变化在介质中传播。** 涟漪水槽的频率改变时，新波长不会一次重铺整个场。页面每帧记录源的真实相位、ω、k、每毫米阻尼与 1/群速度，保留间隔 50 ms 的 32 个采样，并以 32 × 2 纹理上传给两个 shader。每个点用一次定点步进在自己的历史的群速度上求出年龄 `r / groupSpeed`，并从该年龄读 k 与阻尼，这样新波长就像真实情况一样从点水器向外扩散。
- **变化期间保持相位连续。** 第一版用 `θ = k(age)·r − φ(t)`。扫频时 `r·dk/dt` 项让远处的波峰竞速并混叠，频率移动时阻尼振幅（`calm`）又把图案抹掉：纸张平均亮度跌了 17%。现在用 `θ = kE·r − uPhase + Ψ(age)`，其中 `Ψ` 是该采样自来源起、超出其 ω 预测所积累的相位（`packHistory` 中的 `lag`）。在固定点，波峰只随 ω 的变化速度移动，因此不需要振幅阻尼，再配一个小的运动模糊项（`gMove`，每帧波峰移动多远）在快速变化时柔化焦散。
- **点亮淡入，且在浅色下只变亮。** 涟漪灯在首次可见时用 0.9 s 淡入（`smooth(0, 1, (lampClock − 0.15) / 0.9)`）。深色下 SVG 素水填充通过 CSS 变量（`--rt-lamp`）随同一值淡出。浅色下第一版从裸纸开始，波谷的墨让水槽随灯亮起反而变暗，素水填充又进一步加深。现在只要 WebGL 运行就隐藏水填充，纸从第一帧（灯为 0）就以未点亮灰（`off`）绘制，再由 `uLight` 向点亮后的墨色混合，所以点亮只会变亮。对纸上的发光体，同一条规则反过来读：光进来时它的墨只增不减，画面绝不先变淡或先变暗（见 8.2 节）。

### 没有硬性的空间截断
每一项都在任何边界之前归零：`if`、包围形状、平面或画布边缘。`if` 只在该项可证明接近零时作为优化使用。
- 一项珠状项曾被 `if` 在其区间两端硬切。现在用 smoothstep 淡入淡出。
- 羽流曾有 `if` 盒、`s < .01 continue` 和 `step(ax, R0)` 辉光遮罩。三者都显示为接缝。
- 一根屏幕空间辉光柱从喷管延伸到画布底部。画布最后几行仍有 alpha 11–19/255，所以它在台面下方以一条水平直线结束。现在是受地面约束的世界空间辉光，最后 10 行和列精确读 0。
- 宽的 `exp()` 闪光与以地面坐标写的蒸汽在画布边缘仍可见。现在两者都在画布内降到零。
- 单元噪声只看自己的单元，所以偏移加半径加柔尾越过单元半宽的特征会在单元边缘被削平。保持 `offset + wobble + radius + tail` 小于半个单元，或测试 3 × 3 邻居单元。盲测中的泡泡场曾让中心偏移 0.31 个单元、触及 0.86 而半宽只有 0.85。
- 用 `atan` 的径向噪声沿一个角度有接缝。改用方向向量的 `noise3(vec3(dir, r·k − t))`。
- 带百分比停靠点的 CSS `radial-gradient` 结束在其元素之外。改用 `circle closest-side`，让渐变在元素内结束。

### 世界空间，处于相机之中
- 点火冲击曾是围绕投影出口的 2D 圆。它的下弧跨越台面上下、把两根立柱都盖住。现在是真实球体：每个像素光线在两个根处命中它，地面以下的根被柔和隐藏，每个根按边缘加权，并按引擎代理送入前或后 canvas。
- 地面水花曾平铺在喷淋环上，管子失去了体积。环现在是环面遮挡物，用 `max(dot(n, toPlume), 0.)` 照亮。
- 近侧立柱后面的雾曾画在其正面之上。立柱现在是 shader 里的不透明盒。

### 图层与混合
- 深色主题下，只发光的 canvas 用 `mix-blend-mode: screen`，写预乘颜色且 alpha = 最大通道。还要压暗所盖内容的 canvas 保持普通混合：涟漪水槽的水给透过它看到的纸染色，screen 混合会无声丢掉这一点。浅色主题下每个 canvas 都是普通混合，其墨从纸应显示的颜色解出（第 8 节），而不是从深色主题颜色压暗。
- 以普通混合画在白热核心之上的模糊橙边读起来像喷管唇下的一圈暗棕领，画得稍离唇线又变成双弧。盖在 shader 之上的辉光轮廓现在放进单独的覆盖 SVG（`.rp-glow`），深色下用 screen 混合，位置在唇线正处。浅色下没有东西能加光，所以边缘是墨本身的一部分：围绕淡色核心、在主体边缘的一条饱和带（见 8.1 节）。
- 本应在钟形喷管之前的蒸汽总在它后面。现在用引擎代理把蒸汽拆到两块 canvas（第 2 节）。

### Tonemap 与抖动
- 用 `tonemap()`，绝不用 `clamp`，让亮核心滚降而不是削平。
- 没有输出抖动时，大的柔和项变成 8 位阶梯（每级连续 18–34 px），screen 混合让它们更糟。在 tonemap 之后抖动，用约 ±1 LSB 的动态三角噪声，并加门控让空像素保持精确 0（Raptor 的 `inkOf`）：
  ```glsl
  col=tonemap(col,1.15);
  float m=max(col.r,max(col.g,col.b));
  float n=(hash12(gl_FragCoord.xy+fract(uTime*.61)*91.)+hash12(gl_FragCoord.yx*1.37+fract(uTime*.37)*57.)-1.)/255.;
  col=max(col+n*smoothstep(0.,1.5/255.,m),0.);
  ```
- 对精细细节做带限。涟漪水槽把投影波长低于 2.5–5 设备像素的波淡出（其 `fine` 项）。否则 28 Hz 图案会变成摩尔纹。

### 只在有意义时渲染
- 设备比上限 1.5（`maxRatio` 默认值）。只在效果活动时绘制：Raptor 清空两块 canvas，所有包络低于 1e-3 后让循环停止。用与图形其他部分相同的 `IntersectionObserver` 在屏幕外停止，并在 `resize` 时重绘。
- 永不静止的效果（回流中的泡泡、长明小火）让 shader 在空闲时继续绘制，但图形其余部分不必：拆分循环，让 SVG 工作（深度排序、仪表、读数）只在其内容变化时运行，效果单独跑，太慢就降频。盲测中一台台面因一个包络停在 0.54 而不是 0，整个 tick 永远保持 60 fps。
- 用 uniform 检查门控昂贵项（`if(uSmoke<.0004&&uVent<.0004)return vec3(0.);`）。它们对整次绘制取值相同，关闭时不产生开销。

### 减少动态
直接跳到有代表性的稳态（Raptor 跳到主阶段，涟漪水槽跳到其当前 f 与 d），冻结 `uTime`（Raptor 用 0.8），事件包络全部归零（无闪光、冲击或抖动），只在 uniform 的 JSON 变化时重绘。图形仍须响应输入。

### 回退
`glLayer` 会返回 `null`，所以每次调用都要判空。WebGL 运行时给 stage 打标（`data-gl`），CSS 才能在 SVG 回退与 shader 之间切换。用 stub 掉 WebGL 来测试（第 9 节）。

## 8. 浅色主题

浅色是发布主题。浅色页面拿到的是为纸面设计的 shader，而不是最后才转换的深色板辉光。isometrics 站点上有七张图先建在深色板上再转换：池式反应堆、铸造浇注、加力燃烧室、烧口（glory hole）、托卡马克、等离子切割器与锻炉。每次转换都经过三轮评审，本节的每条规则都来自其中一条发现。

Raptor 的浅色羽流（`examples/raptor-engine/live.js` 里的 `inkOf`）是反面教材。它把每个色相乘一个固定暗红 `vec3(.62,.34,.3)`，alpha 设为亮度，结果最热的气体最暗、最不透明。评审者称它为"红墨烟"。不要照抄。涟漪水槽的灰墨（`uPale`）对非辉光的光仍是好模型：一条色调曲线 `1 − uExpo.x/(1 + (e/uExpo.y)^uExpo.z)` 把波峰带到近纸白、把波谷带到套件的灰色，它的水只写与平水面的差异。

### 8.1 纸上的墨
在白色之上，canvas 是普通混合、预乘的，绝不用 `screen`，因为 screen 叠在白上还是白。任何像素都不可能比纸更亮，所以光必须靠**饱和度与局部对比**来读：
- **辉光是饱和的主体、一个近白的淡色核心与一圈彩色边缘。** 淡色核心之所以读作热，只是因为它周围是饱和主体、更外面是更暗的地面。
- **被光照到的东西获得色调**（类似乘法，alpha 有上限）。它不变亮。
- **容纳光的体积更暗，且有物理原因：** 烟灰、耐火材料、深水或阴影（见 8.3 节）。它绝不是黑盒子。

**先设计纸面应显示的颜色，再反解出墨。** 写一条从光能量映射到读者在白上应见颜色的 ramp。然后反解白底上的普通合成，其结果为 `rgb + (1 − a)`：
```glsl
vec4 inkFor(vec3 seen,float cover){
  vec3 absorbed=1.-seen;
  float a=max(max(absorbed.r,max(absorbed.g,absorbed.b)),cover);
  return vec4(vec3(a)-absorbed,a);
}
```
在白上，这合成结果精确等于 `seen`。
- **反应堆。** `inkOf` 用它的 `paperOf(e)` ramp 做这件事，其中 `e = 1 − exp(−2.3·max(lin))`。ramp 依次是白 → `TINT (.85,.93,1)` → `BODY (.2,.46,.94)`（e 在 .12–.5 区间）→ `RIM (.2,.68,1)`（.4–.65）→ `ICE (.9,.98,1)`（.6–.9）。
- **加力燃烧室。** 它的 `paperOf` 把白 → 主体 → 淡色核心混合，然后同样方式反解。
- **`cover` 是热端的 alpha 下限：** 反应堆用 `WASH·smoothstep(.6,.9,e)`，WASH 为 .52；加力燃烧室用 `COVER·smoothstep(.45,.92,m)`，COVER 为 .94。没有它，近白核心的 alpha 接近 0，它后面的 SVG 线直接透出，读起来像洞，不像光。

其他图形用 `vec4(colour·a, a)` 形式：`colour` 来自 ramp，`a` 来自能量的饱和曲线。托卡马克的 `glowInk` 就是一例。两种形式都可行；`inkFor` 还保证读者看到的颜色。

**每种光一种墨，在 shader 内合成。** 各自保留累加器，每种有自己的墨，从后往前堆叠，用 `vec4 over(vec4 top,vec4 under){return top+under*(1.-top.a);}`：

| 项 | 墨 | 见于 |
|---|---|---|
| 发光，热体本身 | ramp 主体加淡色核心，alpha 到 .96–.97 | 等离子切割器 `bodyInk`、锻炉 `barInk`、托卡马克 `glowInk` |
| 落在表面上的光 | 色相偏暖或偏冷，alpha 上限 .5–.8 | 铸造 `castInk` 与 `tintInk`、托卡马克 `tintInk`（.5）、等离子切割器 `tintInk`（.75–.8） |
| 雾：蒸汽、烟、烟气、击穿气体 | 灰或轻微着色，alpha `1 − exp(−density·k)` | 等离子切割器 `hazeInk`、托卡马克 `gasInk`、锻炉蒸汽 |
| 火花与光痕 | 叠在最上层 | 铸造与锻炉 `sparks` |

等离子切割器的 `lightInkOf` 是最清晰的例子：`over(arcCore, over(bodyInk(body), over(arc, over(fumeInk, over(steamInk, tintInk(tint))))))`。若先求能量之和再上墨，所有东西都变成一个色相，淡色核心就丢了。

**收尾。**
- 每次求和后钳制 `rgb ≤ a`：加力燃烧室出现过 1 LSB 的预乘溢出。
- 抖动最终预乘值，rgb 与 alpha 都要，门控用 `smoothstep(0.,1.5/255.,a)`（玻璃熔炉的 `paperOut`、铸造的 `dithered`）。
- 画布边缘保持精确 0。
- 能量进入 ramp 之前先 tonemap（用 `tonemap`，或 `1 − exp(−k·e)`），绝不用 `clamp`。

### 8.2 墨随光增长
深色下，光更多只是加量。在纸上，光更多意味着墨更多，粗心的公式会在光下降时加墨，或在光上升时减墨。以下是评审者发现最多的问题：
- **对完成的墨只淡一次。** 把预乘墨乘以 `u` 是从裸纸到完整画面的精确线性交叉淡化，每个像素都单调：反应堆的 `ink*=uFirst`，玻璃熔炉的 `paperOut(overInk(gas, ink)*uLit)`。烧口曾先淡每一项再上墨（`holeOf`、炉口孔道与球中的 `*uLit`）。淡色核心先到，饱和主体后到，然后地面又变暗，所以点灯先变淡后变暗。每种浅色墨都用未淡化的色调构建（其 `litOf()` 在浅色下返回 1），只淡化最终结果。
- **按能量与 alpha 一起淡化辉光。** 只淡 alpha，淡色核心保持淡、变细的辉光变成乳灰：托卡马克的接触带就是这样。只淡能量，辉光沿其 ramp 退回。托卡马克现在把能量降到下限、其余路程降 alpha：`hot+=glowInk(c*level*(.3+.7*hold))*hold*(1.-hot.a)`。色带淡出过程保持粉紫。
- **在稳定亮度下取色相。** 能量下降时 tonemap 会让色相变红变暗，而 alpha 接近上限时墨反而加重：火焰熄灭时加力燃烧室的腔变重了 55%。修复：
  - 取色相前把燃烧除以局部光强（`burn/lit`，`lit = la.x·glowOf(la.y)/LIT_GLOW`）。
  - 按各部分能量占比混合色相。
  - alpha 绑定能量：`cap·(1 − exp(−1.6·e/cap))`。
  - 低覆盖时把色相向 `EMBER` 加暖，alpha 按 `inkOf(hue)/inkOf(ember)` 缩放，墨量保持不变。

  这样，窗口的墨在熄灭切换时从 1894 单调降到 155。
- **交接就是普通预乘混合。** 加力燃烧室的尾喷有两份拷贝：干燥蓝与点亮暖色，用 `mix(blue, warm, lift)` 交叉淡化。在那里用 `max(alpha)` 覆盖让干燥尾喷的墨翻倍。还要分别门控每份拷贝，避免它捡到另一份的项：干燥冲击盘曾漏进暖色拷贝，成为一块奶油色斑。
- **相乘的包络会在淡出期间上升。** 若点灯包络还在上升而效果自身的边缘在下降，淡出反而变亮：托卡马克在按下 Home 后的前半秒出现过。效果下降期间冻结点灯包络的增长。
- **从 SVG 回退的交接必须精确，** 否则 shader 接入时画面会下陷（见 8.5 节）。

### 8.3 给光一个底
白底上的辉光如果周围什么都没有，读起来像一块污渍。给它真实拥有的底：
- **SVG 里的腔体使用更暗的 token 集。** 一个组 class 为其中所有东西重定义套件 token：
  - 加力燃烧室的 `.ab-inside`：纸 `#4a453f`，阴影 `#3c3833` 到 `#544e47`，线 `#5e5952` 到 `#9b958b`；
  - 托卡马克的 `.tk-cavity`：`#66646e` 到 `#8b8992`；
  - 铸造的积灰孔道色调（`--fd-bore-*-sooted`，`--anatomy-shade-0` 与 `--fd-soot-ink: #2f2a25` 的 `color-mix`）；
  - 烧口的 `--gf-void` 与 `--gf-bore`；
  - 反应堆的水柱渐变（`--rx-water-top`、`-mid`、`-deep`，从 `#edf2f4` 到 `#c9d7e0`）。

  深色下同样的 token 设为 `inherit`。四个阴影色调全部保留，所以内部仍有形体，读起来是耐火材料、烟灰或深水，而不是一个洞。
- **底实时接受光的色调。** 同样的 token 由循环写入的变量 `color-mix` 向光的色相偏移：面用 30% 的 `--ab-flame`，线与背板用 55%；击穿紫色用 `--tk-cold-mix`。这样即使没有 WebGL，SVG 底也会随火焰变暖。
- **shader 的底等于 SVG 的底。** shader 画不透明腔体时（烧口的 `holeOf = overInk(emberInk(t,1.), vec4(SOOT,1.))`），读取 token 而不是重新输入。铸造加一条探针 path，把 fill 设为每个 `var(--fd-…)`，读 `getComputedStyle(probe).fill`，把结果作为 `fixed` uniform 传入（其 `mount.ts` 里的 `paintOf`）。
- **源周围的光是长尾的色调。** 托卡马克的容器在顶平面时读起来是灰的，直到加了一个长程冲刷（`skin*(.14*exp(-gap/(.22*U))+.17*exp(-gap/(.9*U)))`）把壁染成品红。在柱上实测：等离子关闭时 `#6e6c76`，冲刷 .17 时 `#786778`，读作被照亮。.1 时仍是灰。
- **空中不放 bloom。** 浅色下，悬空流束或薄板周围的晕就是纸上的一团污迹（铸造的流束与缺口辉光曾是）。浅色下去掉空中晕。边缘光留在体内，色调放在光照到的表面上。
- **光只落在源能看见的地方。** 反应堆的表面光曾泄漏到屏蔽的切割面与压顶上，直到其密封测试改用水箱唇的真实顶部（`RIMZ`）而不是台面。等离子切割器曾点亮尾焰下端所在格之外的格，而尾焰明显在下一格；现在其 `bayLight` 按各格占尾焰柱的比例照明，尾焰移动时光在格间交叉淡化。

### 8.4 按现象给的配方
热体按暗红 → 橙 → 黄 → 近白的顺序变化，只有这个顺序。在模型里保留一张停靠点表，编译成 GLSL，回退也用同一张表：铸造的 `INK_STOPS`（`inkRampGlsl`，SVG 侧用 `glowInk`），锻炉的 `STEEL_INK`（`steelInk`、`steelInkOf`）。
- **熔融金属、锻钢、坯料、切缝。**
  - 以亮度温度为表编制索引，暗的远墙与亮的浇注读同一张表。铸造的 `brightOf` 从绿通道反解 Wien。
  - 锻炉的停靠点：560 °C `(.45,.09,.05)`、680 `(.56,.07,.04)`、780 `(.78,.10,.03)`、950 `(.95,.38,.06)`、1150 `(1,.78,.12)`、1260 `(1,.93,.78)`。
  - alpha 从可见辉光开始：`steelGlows` 在 560–820 °C，或铸造的 `INK_FROM`/`INK_FULL` 在 470–590 °C，从金属自身底色交叉淡化。
  - 边缘更冷更暗（`steelInk(t − 140)`，铸造的 150 K 边缘下降）。奶油色核心只出现在最热的中心（`steelPale` 在 1050–1280 °C，取 .8）。
  - 辉光之下有一层暗皮，随金属冷却而增厚：锻炉的 `barInk` 从氧化色 `(.28,.29,.32)` 到皮色 `(.24,.22,.23)`，覆盖最多 .86。
  - 评审者对铸造流束的描述："奶油核心带橙色皮"。
- **玻璃聚光。**
  - alpha 是亮度门：`GLOW_SEEN` .008–.028，约 600–710 °C。
  - 颜色是 `pow(hue, mix(1.6,.8,warm))*mix(.62,1.,warm)`，依次为深樱桃 → 红 → 橙。
  - 淡色核心（`CORE_PALE (1,.88,.62)`）放在该像素自身发光最亮处（`cored`，亮度 .14–.24），不在固定半径。
  - 冷皮（`SKIN_COOL (.3,.11,.07)`）只后退。
  - 第一版有一个 salmon（橙红偏粉）阶段。红向白混合就成了 salmon 色，没有任何温度是这个颜色：任何东西变淡之前都要经过橙和黄。
- **火花。**
  - 饱和的头部，更暗更冷的尾部。等离子切割器的 `tailCooling` 把尾部设在头部温度的 0.62；锻炉尾部墨是 `(.42,.07,.02)`，alpha .75、上限 .8。火花最年轻的三分之一才有淡色核心（`u < .35`）。
  - 光痕宽度至少约 1.25 设备像素（`max(.35+.6px, 1.25px)`），否则斜向光痕在 10–24× 放大下会串珠。
  - 在白底上火花就是墨，所以遇到更热的发光体它必须消失。铸造把火花墨乘以 `1 − cover·smoothstep(sparkT−60, sparkT+60, tb)`，对金属与发光孔道都生效。
  - 穿过尾焰后面的火花按深度淡出：`cover*smoothstep(-.4,.4,tJet-tS)`。
- **火焰与尾焰。**
  - 饱和的橙黄主体带半透明边缘，浅色下向轴加权：`mix(1.,1.3-.6*smoothstep(0.,rf,r),uLight)`。
  - 去掉边缘包层（`mix(.8,.3,uLight)`）。给深色羽流带来边缘的边缘壳（第 4 节）会在纸上画轮廓，让火焰空心。
  - 毛糙度留给外层，加宽热轴，淡色核心放在喷管处，在长度的 .4–.9 内淡出。
  - 检查一个横截面。加力燃烧室最终火焰从边到边的墨读数是 `0 2 13 33 31 49 78 72 78 52 40 32 8`。
  - 干燥尾喷是一道淡蓝柱。马赫盘是淡奶油色圆盘（`CREAM (1,.95,.86)`），带暖色边缘与柔边（约盘半径的 .65）。推强之后，第二个马赫盘读起来像旋钮或垫圈，所以它保持为淡透镜。
- **烟与蒸汽。**
  - 浅灰，绝不在其上叠暗的辉光墨。边缘 `(.84,.87,.90)`、顶部 `(.97,.975,.98)`、底面随云自身自阴影取 `(.72,.76,.81)`；alpha 为 `1 − exp(−density·k)`。
  - 靠近热源时，把云向淡琥珀加暖（`mix(steelInk(T), CREAM, .5)`）。锻炉最初把辉光墨叠在云上，评审者看到一团 salmon 斑块。
  - 淬火喷团是一个离开水槽的 `burst`：从水面上 4 升到约 40 单位，途中减速（锻炉 `shader.ts` 里的 `PUFF`），约 0.15 s 内越过沿口，宽度从 7 扩到 13，长大时变薄，并与立柱共享高度窗口，因此永不截断。
- **等离子体（托卡马克）。**
  - 饱和的品红-紫色：`inkBody(chroma)=pow(chroma,vec3(1.8))*vec3(.93,.86,.97)`。
  - m 超过 .55 后核心变淡，向白色靠近并保留 8% 色度。
  - alpha：`.97*smoothstep(.02,.42,m)*(1.-exp(-2.6*(m+2.*m*m)))`。
  - 击穿气体是紫色雾，`(.52,.44,1)` 到 `(.74,.68,1)`，alpha 最多 .64。透过剖面看，容器内部使用腔体 token 集。
- **切伦科夫（反应堆）。**
  - 蓝调水柱中的鲜明青蓝：用 8.1 节的纸 ramp，叠在 SVG 水渐变之上，热端由 `WASH` 给出下限，核心盖住其后的燃料管线。
  - 超临界时压缩脉冲（`1.+.75*log(level)`），让 1.5 GW 脉冲照亮池水而不淹没卡片。
  - 大厅墙上的辉光用单独的、更弱的墨（`HALL_INK` .35）。
- **等离子弧（等离子切割器）。**
  - 紫色弧 `vec3(.6,.34,1.)`，带淡色核心 `vec3(.96,.95,1.)`。
  - 板与水上的暖色调墨：`mix(vec3(1.,.5,.08),vec3(1.,.68,.3),…)`，alpha 为 `.75*(1.-exp(-3.2*sqrt(m)))`。

### 8.5 浅色下的 SVG 与回退
- **只读一次主题。** 在构建时选定主题（`pageHtml({ theme })`，或 React 包装器上的 `data-theme`；isometrics 站点上图形的 build 返回 `theme`，`LivePlate` 把深色板包在自己的 `.iso[data-theme="dark"]` 里）。live 代码从最近的 `[data-theme]` 读取（`root.closest("[data-theme]")?.getAttribute("data-theme") !== "dark"`），并把 `uLight` 作为 `fixed` 传入。每个仅浅色的改动都用 `uLight` 门控（`mix(dark, light, uLight)`，或按 uniform 分支），深色输出保持原样。代价不大时保留深色可用。
- **不用颜色字面量。** 如果图形在 CSS 里硬编码深色，转成带深色覆盖的 token：`.x { --x: light }`，然后 `.iso[data-theme="dark"] .x { --x: dark }`。必须与 token 匹配的 shader 常量从探针取（8.3 节）。
- **嵌套主题。** `.iso:not([data-theme="dark"]) .x` 也会透过包裹深色板的浅色页面命中。反应堆的深色回退就是这样被乘成黑色的。把深色规则放在浅色规则之后、同等特异性，或以板自身主题为键：锻炉用 `.iso-plate[data-plate="light"]`。
- **回退如何混合。** 饱和色调用 multiply，它能压暗且其下的线仍可见。淡色核心用普通混合，因为 multiply 不能提亮：反应堆无 WebGL 的核心是从 .85 的 `#fff` 到 .3 的 `#dcefff` 的径向渐变，普通混合。
  - 回退颜色与 shader 来自同一条 ramp：铸造的 `glowLightCss`，玻璃熔炉的 `gatherInk` 与 shader 的聚光墨完全一致。
  - 淡色 token 上加不透明度会淡成灰，所以回退要用饱和色相：托卡马克的回退环设 `--anatomy-lit: #e0409c` 与 `--anatomy-hi: #f27ec0`。
- **回退形状变化要交叉淡化。** 托卡马克无 WebGL 的等离子环是 11 个预计算环（`LIMITED_RINGS`）。相邻环以和为 1 的线性权重交叉淡化，半径缓动与 shader 相同。用 6 个环时，淡化中途出现过双轮廓。
- **带空隙的东西不放在半透明墨之下。** SVG 画的任何东西都会透过不完全不透明的墨显出来。锻炉的热带曾是一组笔画、笔画间露纸，透过 14% 透明的条压出灰色条纹。现在是一条用热渐变填充的面。
- **从回退到 shader 的交接是精确的。** 点灯时 canvas 墨按 `u` 上升，其下的回退随之退场。回退用线性 `1 − u` 会让淡化中段比两端更淡。要精确线性交叉淡化，把回退的不透明度设为 `(1 − u)/(1 − u·α)`，其中 α 是 canvas 墨在关键处的 alpha：玻璃熔炉的 `--gf-gather-fade`，α 取聚光的中心停靠点。其余回退在 shader 接近接入前保持全强度：`clamp(0, calc(var(--gf-fallback, 1) * 12), 1)`。
- **shader 画的每个物体都要有回退。** 铸造的出铁流原来没有，无 WebGL 时就缺失。现在是用 shader 所读同一份历史逐帧重建的 SVG 轮廓。

### 8.6 墨与线相交之处
canvas 叠在后层 SVG 的 0.6 px 描边之上。浅色下，未对准的边缘表现为描边上的淡色缝隙或彩色线，而不是深色接缝。
- **止于描边的内缘。** 面的墨在描边之下加满，并止于描边内缘，即线宽的一半处：套件 0.6 px 线为 0.3 vb。实测计算出的描边宽度；锻炉的评审者猜的是 1.1。例子：反应堆的 `cutFade=smoothstep(-SEAM-.5*px,-SEAM+.5*px,gap)`，`SEAM=.3`；锻炉的 `strokeMeet`。色调加同样的半个描边内边距（铸造的 `ringLight`），这样它绝不画到线上，也不会在里面留下淡色带。
- **没有描边的地方不要清墨。** 锻炉的遮罩在两个面共享的折痕处清了墨，而 SVG 不描这条线，条上出现了白色接缝。这种折痕改画在墨里：×0.72，至少 0.8 canvas px 宽（更锐会出成点线）。
- **相邻光线不一致处做超采样。** 反应堆追踪四条亚像素光线，当命中、深度、种类、法线或切割面不同（`apart`）时取 16 个采样，切割面边缘因此不出阶梯。dpr 1 时一个 canvas 像素约与描边同宽，所以仍留一个像素的柔度。
- **从画面外进入的物体**可以在屏幕空间从画布边缘淡入。铸造的出铁流在 11 vb 内淡入，起点在画布顶下 10.5 设备像素，边缘仍读 0，流读起来从上方来。

### 8.7 评审者看到的现象与修复

| 浅色下的现象 | 原因 | 修复 |
|---|---|---|
| 红棕色"墨烟"羽流 | 色相 × 暗色乘数，alpha 设为亮度 | 纸 ramp：饱和主体、淡色核心、alpha 下限（8.1） |
| 火焰画成轮廓、内部空心 | 深色的边缘包层 | 主体向轴加权、去掉包层（8.4） |
| 点灯先变淡后变暗 | 各项在上墨前逐个淡化 | 完成的预乘墨只淡一次（8.2） |
| 辉光经乳灰淡出 | 只淡 alpha 的淡色墨 | 能量与 alpha 一起压暗（8.2） |
| 火熄灭时腔体变暗 | alpha 保持不变时 tonemap 使色相变红 | 稳定亮度下取色相、alpha 由能量决定、向 EMBER 匹配（8.2） |
| 玻璃或钢冷却时出现 salmon 阶段 | 红向白混合 | 黑体顺序的 ramp、过黄才变淡、核心放在发光峰处（8.4） |
| 火花像金属上的脏东西 | 更热发光体上的暗墨 | 更热物体上淹没火花；饱和头部、更暗尾部（8.4） |
| 缩放时火花光痕串珠 | 尾部太细 | 至少约 1.25 px 宽；尾部别削太细（8.4） |
| 火花透过尾焰显出 | 对尾焰没有深度测试 | 尾焰后面按深度淡出（8.4） |
| 流束周围纸上有晕渍 | 空中的深色主题 bloom | 浅色下空中不放晕（8.3） |
| 蒸汽里的 salmon 斑块 | 云上叠了辉光墨 | 云向淡琥珀加色调（8.4） |
| 等离子开启时容器仍读灰 | 色调衰减太快 | 长程冲刷项（8.3） |
| 边缘出现淡色镶边或白色接缝 | 墨停在描边之前，或清掉未描边折痕 | 墨止于描边内缘；折痕画进墨里（8.6） |
| 尾喷中出现奶油色斑 | 一份拷贝捡到另一份的项 | 各拷贝分别门控（8.2） |
| 深色板的回退不可见 | `:not([data-theme="dark"])` 规则透过浅色页命中 | 深色规则放在最后，或以板为键（8.5） |
| 回退辉光发灰发淡 | 淡色 token 上加不透明度 | 饱和 token；色调用 multiply、淡核心用普通混合（8.5） |
| 热面透出灰色条纹 | 半透明墨之下有带空隙的 SVG 描边 | 用面填充（8.5） |
| 源看不见的面上有光 | 表面光没有用真实遮挡物 | 使用与 SVG 相同的几何（8.3） |

## 8b. 转动组上的 shader
3D 图形（`references/3d.md`）中部件作为刚体组移动，shader 必须跟随它们。
- **锚定到部件**：`controller.anchor(group, restPoint, restDir)` 每帧给出 `{ world, screen, direction }`。作为 uniform 传入。LED 骑在弯曲指尖上、火焰停在破裂线端点、火花源坐在关节上，都靠它。
- **锚定到表面**：前置 `glslPose("Dial")`（单组用 `GLSL_TURN`）并传 `TURN.poseUniforms(controller, "dial", "uDial")`。此时 `vec3 q = toDial(onFloor(vb, z))` 是组静止世界坐标中的表面点。转台上的油洼、被光照出的纹理与灼痕都随它转动。
- **世界空间保持世界空间。** 烟、离源后的火花与台面上的油绝不触碰组变换。在锚点的世界位置发射，然后在世界中积分。
- **活动部件的遮挡。** 前 canvas 位于活动层之上。用画在效果自身部件之后的部件遮罩其墨：`TURN.cover(controller, [partName])` → `uCoverEdge`、`uCoverCount`，然后 `ink *= 1. - coverOf(vb, .7 * px)`。遮罩是被推出 0.3 vb 的精确凸轮廓，墨止于遮挡物的描边。六个多边形、各十条边。读取 `MAX_FRAGMENT_UNIFORM_VECTORS`，SVG 回退保持在 128 以下。
- **夹在活动层之间的后 canvas** 不需要遮罩：把受光表面放进自己的活动层、排在覆盖它的部件之下（转动的表盘面排在手之下）。
- 向量 uniform 数组（`uniform vec3 uSpark[24]`）通过 `draw` 接收 `Float32Array`。
- **活动部件上的 SVG 回退**是 `T.billboard({ part, at, normal, svg })`。其标记以投影点为中心、以 viewBox px 为单位，不是世界单位，所以世界尺寸要乘 `G.scaleOf(P)`：为半径 1.1 的透镜设计的辉光是 `<circle r="${(1.1 * G.scaleOf(P)).toFixed(2)}"/>`。写成 `r="1.1"` 画出的是约为透镜三分之一大的针点。用 `--no-webgl` 与 4× 放大检查。

## 9. 验证

会动的东西用 `scripts/drive.mjs`；`capture.mjs` 现在也支持 WebGL，拍摄 shader 页面的静态截图没问题。用法见 `references/verify.md`。在常规清单之上：

- **覆盖每次过渡的连拍表：** 开始、每次相位变化、稳态与停止。重型 WebGL 页面上的实时连拍太稀疏，因为无头捕获耗时 60–200 ms 并阻塞动画帧。先用 `["slow", 0.05]` 放慢页面时钟（对 `requestAnimationFrame` 与 `performance.now` 慢 20 倍），拍表，然后 `["slow", 1]`。要捕捉第一帧就开始的东西（如点灯淡入），用 `--preload` 传一个包含 `window.__driveSpeed=0.04` 的文件，让页面从第一帧就慢跑。用 `["until", "document.querySelector('[data-readout]').textContent.includes('main stage')", 8000]` 等相位，而不是猜一个 `wait`。每张表之前都要按住空闲巡游：它的恢复定时器走的是墙上时钟而不是放慢的时钟，会在表中途把目标拉回去。一次按键能让它停几真实秒；长的放慢连拍要用 `--preload` stub 定时器并先等静止（`verify.md`，"Slow mode doesn't slow timers"）。
- **数字，不只是图。** `canvas.getContext("webgl")` 返回页面自己的上下文。在 `requestAnimationFrame` 回调里，用 `gl.getUniform(gl.getParameter(gl.CURRENT_PROGRAM), location)` 读 uniform，用 `gl.readPixels` 读画布平均 RGB。回读只在与绘制相同的任务里有效，因为 `preserveDrawingBuffer` 是关的：来自单独任务的全零帧是测试伪影。整次运行每帧记一行。色相与平均亮度在相位变化中都应单调移动，有意的爆发除外。
- **边缘读 0。** 每个相位都回读画布最后 10 行与列。任何大于 0 的值都是会在 screen 混合下显形的截断。
- **浅色下记录墨，而不是亮度。** 每帧记录一个区域铺在白上的墨，`1 − lum(rgb + 1 − a)`，钩子见 `verify.md`（"Light-theme shaders"）。对每个关键区域（腔体、核心、仅回退区域）在点灯、每次相位变化与淡出期间都做。墨必须跟随物理量：光进来时升，光退去时降，没有鼓包也没有凹陷。用数字说：加力燃烧室的熄灭窗口从 1894 降到 155，其灭灯从 154 升到 1959 并稳定在 1914。
- **浅色下沿物理 ramp 探测颜色。** 对加热或冷却的东西，在若干温度读中心与边缘像素。它们必须按暗红 → 橙 → 黄 → 近白变化，边缘比中心冷，没有 salmon 或灰的阶段。烧口的表从 930 °C 的中心 255/179/99、边缘 252/114/25，经约 620 °C 的 211/63/6 与 165/28/1，到 465 °C 时成为透明玻璃。对体积，从边到边读一行墨的横截面：峰值应在轴上。
- **浅色下也要查深色路径。** 每个浅色改动都在 `uLight` 之后，所以深色构建的帧应与其基线一致。另外渲染一张浅色页面里的深色板，分别带与不带 WebGL（嵌套主题陷阱，第 8.5 节）。
- **效果与 SVG 相交处的 2× 与 4× 裁片：** 边缘、唇线、台面边、墙带、纸角、遮挡物，以及效果被透过来看的每个开口（它是否在四侧都止于沿口、其下露出凹槽壁？）。找接缝、硬边、成带、暗领、双线或突然变色。浅色下，凡墨与描边相遇处（切割面、边缘、口部、折痕）也拍 8–16× 裁片，找墨与线之间的淡色缝隙、墨压过线、或被墨清掉的描边。同一裁片分别在前层 SVG 隐藏与 canvas 隐藏下再比一次（用 `eval` 设 `style.display="none"`）。
- **回退。** 用 `--no-webgl` 跑 `drive.mjs`（每个 `getContext("webgl")` 返回 `null`），检查 `data-gl` 不存在、两种主题下仅靠 SVG 仍可读。浅色下，回退应显示与 shader 相同的墨、相同的暗底，shader 画的每个物体都在。用 `--preload` 让页面从第一帧就放慢，连拍记录点灯：从回退到 shader 的交接不得下陷（第 8.5 节）。
- **减少动态**（`--reduced`）：一张静止的代表性帧。
- **控制台干净。** shader 编译错误经 `onError` 以 `console.error` 到达。

## 10. 性能

- 成本约等于像素 × 采样。Raptor 跑 28 个体积采样，每个带四项激波单元项，外加 28 步地面搜索（含 7 次二分）、8 采样辉光、10 采样水花幕与每 canvas 6 个蒸汽采样，设备比最高 1.5×。它在 SwiftShader 下能跑，但真实 GPU 上的帧时间未测过。发布更重的东西之前，先在真实浏览器的 Performance 面板里测量；太慢就先砍采样，再砍 `maxRatio`。
- 涟漪水槽的纸 shader 每像素求值双源场四次（一次为折射位移，三次为焦散的定点逆运算），每个源花六次纹理读取读其历史，而不是 24 步 uniform 循环。在笔记本 GPU 上测得每次绘制约 1 ms；手机成本未测。
- 要知道你测的是哪块 GPU。`drive.mjs` 与 `capture.mjs` 的无头 Chrome 能用时用真实 GPU，否则用 SwiftShader；相信帧时间之前先记 `gl.getParameter(gl.RENDERER)`。
- 采样只花在要紧处。给步进设界（圆柱或盒），从地面命中开始，整项用 uniform 门控。
- 两块 canvas 就是两次全屏 pass。清空没有东西可显示的那块（Raptor 的 veil 只在蒸汽、水汽或冲击存在时才绘制）。
- 场里没东西需要就不要动 `uTime`。涟漪水槽传 `draw(values, 0)`，只移动波相位，减少动态的帧因此真正静止。
- 空闲时停掉循环。一个没有任何动静却保持 60 fps 的 shader 页面是 bug。
