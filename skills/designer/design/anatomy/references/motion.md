> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/anatomy/references/motion.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 动效与交互

当图形的机构像真实物体那样运动时，它才是活的：滑架滑动后平稳停住，弹簧只回弹一次，指针摆向新的读数。动效要平静到能跟上，又要忠实于模型。

## 原则
- **基于时间。** 从 `requestAnimationFrame` 时间戳取 `dt`，并钳制到 1/30 s，这样后台标签页恢复时不会跳变。绝不按帧步进固定量。
- **向目标缓动。** 指针和键盘设定的是一个*目标值*，部件用指数缓动（`x += (target − x)·(1 − e^(−dt/τ))`，τ = 0.1–0.3 s）或弹簧跟随。部件绝不直接吸附到光标位置。
- **主体有弹性就用真实的弹簧。** 刚度和阻尼取自真实模型，为稳定起见每秒子步进约 240 次。误差和速度都低于 5e-4 后直接吸附到目标值。
- **每个图形一个循环。** 单个 `tick(dt)` 更新模型，再通过 ref 写 DOM：`setAttribute("transform" | "d")`、`textContent`、`dataset`。不要每帧重渲染 React。
- **到位或离开视口就停。** 用 `IntersectionObserver`，rootMargin 设 `120px 0px`，并读取最新一条 entry（`entries[entries.length - 1]`）：当舞台在两次回调之间离开又回来，一次回调会按从旧到新交付两条 entry，若读第一条，图形会冻在屏幕上。所有东西到达目标后就停掉循环。
- **减少动效。** 设置了 `prefers-reduced-motion: reduce` 时，直接跳到目标值，不做导览、流动或脉冲。图形仍必须响应输入。
- **空闲导览。** 无人交互约 1.4 s 后，播放一段脚本化循环，展示图形的要点。悬停、聚焦或按下时暂停，最后一次交互约 3.6 s 后恢复。导览驱动的是用户会驱动的同一批目标。
- **读数实时更新**，来自同一个模型，用真实单位且简短：`block 2 · reads 14.0 px`、`120.0 × 32.0 · lean 10.6 px`。读数取自部件实际所在处，而不是目标值：只要任何弹簧在动或有待办，Raptor 就显示 `taking apart` 或 `closing up`，之后才显示 `apart · 11 assemblies` 或 `1,630 kg · cold`。阶段词和它旁边的数字要取自同一时刻、同一来源：盲测台架打印出 `end of stroke · relief 85 bar`（词来自模型，数字来自滞后 0.25 s 的表针），而它的泄压阀实际在 92 才开启；回缩后紧接着又打印 `idle · 44 bar`。

## 指针
- 用某条轴的屏幕向量把指针映射到世界坐标。沿 x 方向的运动用 `axisVector(P, [1, 0, 0])`，或者把图形的宽度比例映射到部件的行程范围。行程短的时候，范围映射更简单、手感也更好。
- 悬停预览、按下提交。触屏没有悬停，所以让点击直接生效，并保留 `touch-action: pan-y`，页面才能继续滚动。
- 拖拽期间使用 pointer capture，在 `pointerup` 或 `pointercancel` 时释放。

## 键盘与可访问性
- 图形根节点可聚焦（`tabIndex=0`），带 `role="slider"`（若有离散选项则用 `"group"` 加按钮）、解释控件的 `aria-label`，以及用文字表述的 `aria-valuenow`/`aria-valuetext`，比如 "Pressed: 129.6 by 34.6 pixels, leaning 10.6 px"。值文本在读者的选择变化时写入（选中了部件、分解或装配、点火或冷态），而不是在循环里写：屏幕阅读器会播报聚焦滑杆值文本的每一次变化，每帧都变的读数（"Pc 290 bar · 222 tf"）会变成一串数字流。可视读数与无障碍值分开维护（Raptor 的 `say()` 只写读数，`describe()` 写值文本）；live region 承载阶段。
- 按键：方向键按合理单位步进（Shift 为大步长），Home 和 End 到两端，Space 或 Enter 按下或切换，Escape 释放。
- 显示焦点环：`outline: 1px solid var(--anatomy-muted); outline-offset: 6px`。
- `<svg>` 带 `role="img"` 和描述对象及其内容的 `aria-label`。

## 原生循环（无框架）
```js
let frame = 0, last = 0, visible = false, touring = !still.matches, clock = 0;
function tick(now) {
  const dt = last ? Math.min((now - last) / 1000, 1 / 30) : 1 / 60;
  last = now;
  const calm = still.matches;
  if (touring) { clock += dt; target = tourAt(clock); }
  x = calm ? target : x + (target - x) * (1 - Math.exp(-dt / 0.28));
  springTo(tip, heightUnder(x), dt, 420, 26, calm);
  draw();                                   // setAttribute on refs, readout.textContent = …
  const settled = !touring && x === target && tip.rate === 0;
  frame = visible && !settled ? requestAnimationFrame(tick) : 0;
}
const run = () => { if (!frame && visible) { last = 0; frame = requestAnimationFrame(tick); } };
new IntersectionObserver((entries) => { visible = entries[entries.length - 1].isIntersecting; if (visible) run(); }, { rootMargin: "120px 0px" }).observe(stage);
```
`examples/dial-indicator/build.mjs` 有完整版本，包含导览、指针映射和键盘停止逻辑。

## React 循环
把静态图稿放在服务端构建的 props 里，只移动 `<g>` 包裹层和改变形状的 path：

```tsx
"use client";
export function RigLive(props: { base: React.ReactNode; carriage: React.ReactNode; dial: React.ReactNode }) {
  const { anchor, say } = useReadout<HTMLDivElement>();
  const car = React.useRef<SVGGElement>(null);
  const needle = React.useRef<SVGPathElement>(null);
  const state = React.useRef({ x: REST, target: REST, tip: { at: 0, rate: 0 } });
  const visible = useInView(anchor);
  const kick = useLoop((dt, calm) => {
    const s = state.current;
    s.x = follow(s.x, s.target, dt, 0.28, calm);
    const settled = spring(s.tip, heightUnder(s.x), dt, 420, 26, calm);
    car.current?.setAttribute("transform", translateAlong(P, [s.x, 0, 0]));
    needle.current?.setAttribute("d", needleAt(s.tip.at));
    say(readoutOf(s));
    return !(settled && s.x === s.target);
  }, visible);
  return (
    <div ref={anchor} tabIndex={0} role="slider" onPointerMove={(e) => { state.current.target = toWorld(e); kick(); }}>
      <IsoFigure width={W} height={H} label={LABEL}>
        {props.base}
        <g ref={car}>{props.carriage}</g>
        {props.dial}
        <path ref={needle} className="iso-line" data-tone="lit" d={NEEDLE_REST} />
      </IsoFigure>
    </div>
  );
}
```
`examples/test-rig/live.tsx` 是完整的正式版本，带弹簧、导览、按压与拉动、键盘处理和 aria。

## 会变形的部件
当部件变的是形状而不是位置（膨胀的胶囊、压缩的弹簧、转动的指针）时，每帧只用工具包重建它的 path，用 `slabOf`、`coil` 或 `lineOnTop`，并写回它的各条 path：`fill`、`shades[0..3]`、`top`、`crease`、`bevel`、`outline`。单个实体远低于 0.1 ms。要实测：每帧脚本耗时应保持在约 1 ms 以内。
- **预烘焙帧会跳步。** 用 ±15° 范围内 41 帧预建帧绘制的杠杆，每帧让旋钮移动约 0.8 px，慢放时可见。旋转部件要么每帧重建，要么预烘焙足够多的帧，使单步移动不超过 0.25 px。
- **从填料函（gland）里滑出的杆**不改变形状：它是一根全长杆在移动，在填料函端面被一个不动的 clip 裁剪（`G.rodOut`、`holdStill`，见 `craft.md` 第 3 节）。绝不要画成多个重叠副本。

## 一次性事件的包络
闪光、咔哒、弹跳、抖动或冲击是带时间年龄的事件，不是你设定的一个值。用带 attack（起振）和 decay（衰减）的包络驱动它。`kit/gl.mjs` 导出 `smooth(a, b, x)`（smoothstep）和 `burst(age, rise, fall)`，后者在峰值后等于 `smooth(0, rise, age)` 乘以 `exp(−(age − rise)/fall)`，事件前为 0：
```js
import { smooth, burst, settle } from "../../kit/gl.mjs";
const flash = calm ? 0 : burst(clock - mainAt, 0.08, 0.13);
```
在独立页面上，`glScript()` 已内联这三者，直接使用即可，不要自己再声明：同一个 module script 里出现第二个 `const smooth` 是 SyntaxError。
- attack 为 40–120 ms，smoothstep 保证起振点斜率为零。一帧内把值设到 1 就是爆点。
- 记下事件的起始时间（`mainAt = clock`），每帧按其年龄计算所有包络。两个事件重叠时直接相加即可。
- 每个事件有自己的标志（`popped`），这样快速重启不会吞掉下一个事件，也不会掐断还在衰减中的那个。
- 减少动效时，所有事件包络为 0。

## 临界阻尼 settle
对于应该无过冲到位的值（色相、亮度、灯、伸出量、频率），用工具包的 `settle(state, target, dt, seconds, calm)`：作用在 `state = { x, v }` 上的临界阻尼弹簧，时间常数为 `seconds`，`v += (w²·(target − x) − 2w·v)·dt`，其中 `w = 1/seconds`，分四个子步进。它比指数跟随更平滑，因为速度也连续。误差和速度都低于 1e-4 时直接吸附到目标，`calm` 时直接跳过去，仍在运动时返回 true，因此能维持循环：
```js
const moving = settle(freq, state.tf, dt, 0.625, calm);
```
涟漪水槽把频率（0.625 s）和拨水片间距（0.4 s）都走 `settle`，因此按键或指针移动绝不会让波长跳变。
- **把一个相位改变的东西分开。** 当一个物理量（比如燃烧室压力）同时驱动颜色、形状和亮度，对它加快速弹簧会让三者一起跳。给颜色单独一个更慢的 `settle`（0.3–1 s），亮度则算成在变化过程中单向移动。
- **淡出只会变暗。** 停机开始时，把亮度冻结在当前值，只用递减的量去缩放它。
- **改一个弹簧会牵连邻居。** 把一个弹簧调成临界阻尼，会让所有依赖它旧过冲的相位变慢，所以要逐一复查。

## 分解视图
悬停时把机器拆开，是展示其部件的有力手段（`examples/raptor-engine/`）：
- **每个零件都建在装配位置上**，打上总成名标签，并给每个总成一个世界坐标移动向量（`PIECES.nozzle.move = [0, 0, -120]`）。移动遵循真实装配关系：喷管下移最远，侧挂单元沿径向滑出（`out(deg, r, z)`），支架不动。
- **每个总成一个弹簧**，装配态为 0、拆开态为 1。Raptor 用刚度 64、阻尼 14.2，略低于临界值，部件到位时带一点重量感，每帧子步进 4 次。
- **给弹簧错峰。** 打开时，每个总成的目标值在前一个之后 35 ms 变化，顺序要保证任何东西都不会穿过任何东西（Raptor：`nozzle, downcomer, controller, plumbing, lox, ftp, hotgas, chamber, orpb, otp, gimbal, stand`，见下文"排定错峰顺序"）。关闭按相反顺序，机器从内向外折回。待处理目标存成 `{ value, at }`，`clock >= at` 时应用。
- **反向时只重排真正变化的。** 读者中途反向（快速悬停、Space、轻点）时，取消尚未离开的总成的待处理目标，只对目标值有变化的总成按其在更短列表中的序号错峰。这样最后出去的就是第一个回来的，立即返回。整表重排会让先出的总成朝拆开方向飞 0.3 s 而后出的还坐在原位，爆炸图之所以没出事，只是因为 35 ms 后下一个总成让开了路：在这个窗口内反向，会让燃气导管撞进尚未离开的甲烷泵。用了这条规则，错峰序列在各帧内保持有序（先出的总成永远领先），这正是下文前缀规则所依赖的。
- **用 transform 移动。** 每个元素的屏幕偏移是它的移动向量经投影后乘以弹簧值：`translate(tx ty)`。值为 0 时移除该属性，装配态图形就与静态图稿完全一致。
- **让连线始终有落点。** 连接两个总成的部件（机架与泵耳之间的作动器、盒子与插头之间的缆线）归属它们物理上贴着的那个总成，拆开时仍要落在某个东西上。缆线两端加端点圆点。
- **选择。** 悬停、键盘方向键和零件列表都能选中一个总成。被选中的部件成为唯一的 `lit` 高亮：`.it[data-on]` 上的 CSS 把 `hi` 换成 `lit`、`mid` 换成 `hi`，并把顶面和侧面切到 lit 填色。其余部件经 `[data-focus]` 的 CSS 各降一档（`hi` 降 `mid`，`mid` 降 `lo`），读数说明被选部件的功能。

## 运动部件的深度重排
朝向或远离观看者移动的部件，会随移动改变画家算法的绘制顺序。出现这种情况时，每帧都排序：
- 给每个元素一个静态键 `k = dot3(ref, viewOf(P)) + bias`，`ref` 是它的中心，`bias` 用于平息相触部件之间的并列。再给它一个抬升量：`lift = dot3(move, viewOf(P))`。
- 每帧，它的键是 `k + lift × spring`。按该键对索引排序，且**只在顺序真的变了时才重新挂载 DOM 节点**（用一个 `DocumentFragment`）。大多数帧什么都不会变。
- 把键和移动向量存在元素上（`data-k`、`data-m`），这样实时脚本不需要几何信息。
- 管子按段排序（`tubePieces` → `piece.mid`），这样管道可以在一个部件前经过、在另一个部件后经过。
- **静态键要依据运动来定，不能只看静止姿态。** 每个元素的键是 `k + lift × spring`，但弹簧错峰后，任何一帧里每个总成的份额都不同，所以装配态和拆开态顺序都对的两件东西，中间过程仍可能画反：初版 Raptor 里，一条增压管线在每个爆炸过程中有 40% 的时间躲在一根它本应在其前的作动器立柱后面。Raptor 对每个重叠对在 0、0.1 … 1 各点实测真实深度，采样点覆盖它自己的弹簧以实时错峰重放直到收敛的每第四帧、打开、关闭以及在每条错峰边界两侧的反向，以及前缀状态（`A.explodeStates(STAGGER, SPRING).depth`，即 `[...A.uniformStates(10), ...A.springStates(STAGGER, { ...SPRING, stride: 4, reversals: A.reversalsOf(STAGGER, SPRING.stagger) }), ...A.prefixStates(STAGGER)]`，共 1,119 个状态，也是用 `{ order: STAGGER, spring: SPRING }` 创建的 recorder 的 `A.settle(R, P)` 默认值），`orderKeys` 一次性解出全部（每条规则都用那一帧的份额）。只测打开和关闭，快速悬停产生的帧里仍会留下错对：一个应位于燃烧室环带之前的吹除法兰，在 0.20 s 处的一次反向中消失在它后面。静态以及每个重放帧中任何错对都会让审计失败；只有无人可见的 uniform 状态里才允许保留倒序对。
- **弹簧只有一个来源。** 错峰顺序和弹簧常数（`SPRING = { stagger, stiffness, damping, substeps }`）保存在构建里，并经数据传给页面，审计重放的才是观看者看到的同一份。
- **部件跟着它安装其上的东西动（`ride`）。** 装在燃烧室上的传感器以管路高亮，却跟燃烧室的弹簧走。每个元素在 `piece`（它跟随高亮的总成）旁边记录 `ride`（其移动向量对应的、驱动它弹簧的总成），页面读取 `data-ride`，`place()` 对平移和排序都用 `piece[node.ride].x`。借了别的总成的向量却保留自己弹簧的元素，会沿其安装座滑移并在半途陷进去。
- **前缀规则。** 在先出的已经离开、后出的还停在原位的帧里，每个总成的路径都必须避开每一个比它晚离开、仍停在原位的总成：这正是错峰边界处反向冻结的那一帧。`A.prefixStates(STAGGER)` 摆出的正是这些姿态（前 `k − 1` 个已出，第 `k` 个在 0.25 … 1，其余在原位），审计把它们与重放帧一起检查。在 Raptor 上，它把燃气歧管排到其所栓接的甲烷泵之后（其向量指向泵内），把控制器排到管路之前（氧到预燃室的管路被控制器的感测线包住，只能等它们之后离开）。
- **排定错峰顺序，让任何东西都不必穿过。** 弹簧是重叠的：起始间隔 35 ms、收敛耗时约一秒，所有总成同时都在动，相对运动是所有向量的混合。初版 Raptor 爆炸时 66 对零件在半途互相穿过。审计逐帧并在反向时检查、把它们归零的规则如下：
  - **在外者先出。** 每一侧，其他东西都收纳在其后或其下的部件先动：Raptor 的喷管最先下移（一切都装在它上面），而下行管（downcomer）走在通往甲烷泵的每条感测线和线束之外，第二个走。关闭时反过来，外侧部件也是最后回家的。
  - **当一个部件的爆炸向量指向另一个总成的某个面时，那个总成排在更前。** 下行管下落 84、落在喷管的端口三通上；喷管下落 120 且早 35 ms 出发，于是无论打开还是关闭，端口始终在法兰之下。
  - **在另一侧还在原位时，把每个向量指离该部件接触到的每一个面**，而不只是它栓接的那两个：穿行于燃烧室与泵之间的管线，必须沿两个安装面法线都允许的扇区移动（Raptor 的外套管线走 −120°、不下落，从两个垫板侧面滑出）；绕核心部件一圈的缆线，只能在其整段包覆都朝外的扇区内移动（包 90° 可走 90°；包超过 180° 则无处可走，只能缩短或让其在近侧终止）；会向下扫过其下方所栓部件的管线，不得下落。
  - **互相穿绕的东西共用一个弹簧。** 沿线束环上升进入接线块的感测线，与该块下方的线束，不能各用各的弹簧：错开 35 ms 它们就会互相剪切。Raptor 的感测线和接线块跟随控制器（`BLOCK_MOVE = PIECES.controller.move`，所以 `ride` 解析为 `controller`），高亮仍按管路。
  - **只安装在一个部件上的线，只取该部件的移动。**
  - **检查观看者能走出的每条路径**，而不只是从静止出发的那两条：快速悬停会让弹簧半途反向（`reversals`），回程迟的总成可能扫过已经到家的缆线。要在每条错峰边界处反向（`A.reversalsOf`），而不是挑几个整数时刻：坏窗口宽约 15 ms，0.15、0.3、0.5 s 一个都没碰到。这些帧既要喂给深度状态，也要喂给间隙检查，实体还要对实体测（`A.solidClearances`）：一个缩进宿主悬突下方的法兰，在回家路上撞上宿主弹簧的尾部，深度 0.67，而所有管路检查都是零。

## 手动转动
对 3D 图形（`references/3d.md`）：
- **拖拽。** `controller.angleAt(clientX, clientY, zFace, "dial")` 是指针在该面平面上的角度，跨圈不回卷。pointer down 时记下它和当前目标值。move 时设 target = start + Δ，移动超过约 1.5° 后捕获指针。组用指数跟随（τ = 0.12 s）。舞台保持 `touch-action: pan-y`。
- **按键。** 方向键步进一格，Shift 一次十格，Home 回到基准位。
- **联动组。** 从一个值经 `follow(values)` 驱动（表盘四分之一处的轮子、由单个 `lift` 带出的指链），工具、拖拽和导览才会一致。
- **手势与剪辑是时间的纯函数**（`tapAt(t)`、`breakAt(t)`）：构建对它们采样，审计逐帧走查，页面可以倒放它们来实现无跳变的重置。
- **钩子接管。** 任何 `window.__isoTurn` 调用都会触发 `onHold`：停掉导览，并保留工具设定的值，直到读者再次操作。
- **半帧率。** 稠密图形维持 `controller.set` 的平均耗时，14 ms 以上隔帧渲染，9 ms 以下逐帧渲染，基于时间的运动不变。
- 减少动效时只给一帧静止画面。离开视口时循环停止（IntersectionObserver）。

## 待发
如果一个动作需要机器处于特定状态（点火前装配到位、旋转前舱门关闭），先进入待发：
1. 设定让它进入该状态的目标值（`setApart(false)`、`select(null)`）。
2. 标记为待发：按钮显示 `data-state="armed"`，读数显示 `closing up · arming`。
3. 只有每个弹簧都到位、没有待办时，才启动该动作的时钟。

绝不要在半拆开的机器上运行动作，也绝不要为省时间把零件直接吸附归位。

## 从导览手中接管
用户在空闲导览中操作时，停掉导览，状态留在原地。如果你的接管辅助函数会重置某个东西（比如强制开机），而用户的操作本身就是对这个东西的切换，两者会在同一帧里互相抵消并重放一段动画。给辅助函数传一个标志（`takeOver(switching)`），并在导览的每个阶段测试每个切换开关，而不只测默认阶段。

导览期间按下的步进键必须从读者看到的值出发，而不是从可能遥遥领先于前的导览目标值出发。涟漪水槽的按键在导览中从 `freq.x` 和 `gap.x` 起步（其余情况用 `state.tf` 和 `state.td`），`steer()` 接管时把两个弹簧的速度清零，值就只会朝按键的方向移动。

## 播报阶段
有阶段的机器，加一个视觉隐藏的 `aria-live="polite"` 元素，只把阶段变化写进去：`arming`、`chill-down, venting`、`preburners lit`、`main stage`、`shutdown`、`cold`。绝不要往里写逐帧数字。连续控制要等输入安静约 700 ms 后再播报（涟漪水槽的 `announce`）。加载时让 live region 为空，在 `focus` 时填入当前状态，屏幕阅读器听到的是它到达时的状态，而不是一行过期文本。标签会变化的按钮（"Ignite" 换成 "Shut down"）不需要再加 `aria-pressed`。

## CSS 动效
- `.iso-line[data-flow]` 让虚线动起来，用于沿路径行进的东西。
- `.iso-dots circle[data-pulse]` 缓慢闪烁点阵，用于"激活中"的表面。
- 悬停抬升：给组包一层 `transition: transform 700ms var(--anatomy-ease)`，悬停时向上平移。

以上全部在 `ISO_CSS` 的减少动效模式下关闭。
