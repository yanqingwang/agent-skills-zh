> **中文汉化版** · 上游：[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) · 原文件：`references/verify.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 验证

以一位严苛评审的眼光审视图形，赶在任何人之前。渲染很便宜，猜测很昂贵。

## 截图
`scripts/capture.mjs` 会启动自己的无头 Chrome（找不到时设置 `CHROME_PATH`），加载文件或 URL，默认裁剪到 `.iso-plate`。它还打印读数区、任何控制台错误或异常，以及页面是否横向滚动。

```sh
node scripts/capture.mjs page.html --out shots/desk.png                         # desktop 1440, dpr 2
node scripts/capture.mjs page.html --out shots/phone.png --width 390            # phone
node scripts/capture.mjs page.html --out shots/hover.png --hover 0.7,0.5        # pointer at 70% across
node scripts/capture.mjs page.html --out shots/tour.png --times 1200,2400,3600  # motion: extra shots over time
node scripts/capture.mjs page.html --out shots/keys.png --key ArrowRight,ArrowRight
node scripts/capture.mjs page.html --out shots/joint.png --zoom 200,80,220,170  # close-up at 4x, in card px
node scripts/capture.mjs page.html --out shots/still.png --reduced              # reduced motion
node scripts/capture.mjs http://localhost:3000/docs --select "figure:nth-of-type(3) .iso-plate"   # one figure on a dev-server page
```
`--select` 接受任意 CSS 选择器；默认裁剪到第一个 `.iso-plate`。每个 `--times` 延迟从第一张截图起算，所以 `1200,2400,3600` 会在其后约 1.2、2.4 和 3.6 秒截图（单次截图耗时 60–200 ms，间距更近的延迟会偏晚），保存为 `name-<ms>.png`。`--key` 发送的键码与 `drive.mjs` 相同（`7` 作 `Digit7`，`.` 作 `Period`；逗号要写成 `Comma`，因为列表本身用逗号分隔）。其余选项：`--height`（1000）、`--scale`（2）、`--wait`（首张截图前 2500 ms）、`--zoom-scale`（4）和 `--theme dark|light`。你生成的每张 PNG 都要看：打开它，用眼睛检查。

两个脚本都开启 WebGL 启动 Chrome（`--enable-unsafe-swiftshader --ignore-gpu-blocklist`），所以着色器也会出现在 `capture.mjs` 的静帧里。凡是需要计时或放慢的东西都用 `drive.mjs`。

## 驱动
`scripts/drive.mjs` 在开启 WebGL 的无头 Chrome 里运行脚本化会话。用于序列操作：悬停、点击、输入、等待某个阶段。也用于放慢速度、捕捉突变的连拍拼图，以及无 WebGL 后备。每次截图后打印读数区，然后是任何控制台错误与异常。

```sh
node scripts/drive.mjs page.html '[["wait",1500],["move",".rt-stage",0.7,0.4],["wait",600],["shot","shots/hover.png"]]'
node scripts/drive.mjs page.html --actions steps.json --height 1300
node scripts/drive.mjs page.html --actions steps.json --width 390
node scripts/drive.mjs page-light.html --actions steps.json --reduced
node scripts/drive.mjs page.html --actions steps.json --no-webgl
node scripts/drive.mjs page-light.html --actions steps.json --preload slow.js
```
选项：`--width`（1440）、`--height`（1100）、`--scale`（1）、`--reduced`、`--theme dark|light`、`--no-webgl`（让每次 `getContext("webgl")` 或 `"webgl2"` 都返回 `null`，用来检查 SVG 后备）、`--preload file.js`（在页面自身脚本之前运行的脚本：计数器、stub、钩子，或用 `window.__driveSpeed=0.04` 让页面从第一帧就慢放）和 `--actions file.json`。选择器默认第一个 `.iso-plate`，分数在元素上取 0..1。

`--theme`（两个脚本都有）只模拟 `prefers-color-scheme`。kit 页面在构建时就选定了主题（`<body>` 上的 `data-theme`），无视该 media query，所以要检查浅色主题：用 `--light` 构建，驱动 `-light.html` 文件。

| 动作 | 作用 |
|---|---|
| `["scroll", sel]` | 把元素滚动到视口中部。 |
| `["wait", ms]` | 等待。 |
| `["move", sel, fx, fy]` | 分 10 步把鼠标滑到该处，触发 `pointermove`。 |
| `["click", sel, fx?, fy?]` | 点击，默认在中心。 |
| `["drag", sel, fx0, fy0, fx1, fy1, steps?]` | 在一点按下，以每帧一步、共 `steps`（20）步滑到另一点，松开。这些是真实输入事件（pointer id 1），所以调用 `setPointerCapture` 的处理器能正常工作。用它测试拖动转动：从 `eval` 派发的 `PointerEvent` 没有活动指针，`setPointerCapture` 会抛 `NotFoundError` 并中断处理器。 |
| `["key", key, sel?, code?]` | 聚焦 `sel`（默认 `[tabindex="0"]`）并按键：`"i"`、`"Escape"`、`"ArrowRight"`、`" "`、`"7"`。数字发送 `DigitN`，字母发送 `KeyX`，标点发送其正确的码（`Space`、`Minus`、`Comma`…）。同名键要传 `code`：`["key", "Shift", null, "ShiftRight"]`、`["key", "Enter", null, "NumpadEnter"]`。 |
| `["slow", factor]` | 以 `factor` × 实时速度运行页面的 `requestAnimationFrame` 时间戳和 `performance.now`：`["slow", 0.05]` 是 20 倍慢放，拼图能在很多帧里捕捉到一个 100 ms 的事件。`["slow", 1]` 恢复实时。 |
| `["until", js, timeoutMs?]` | 每 25 ms 轮询一个 JS 表达式，直到为真（默认 10 秒），超时则打印一行。 |
| `["eval", js]` | 在页面里运行 JS 并打印结果。Promise 会被等待。 |
| `["shot", out, sel?, scale?, [x,y,w,h]?]` | 截图一个元素，或它内部以 CSS px 计的区域。 |
| `["sheet", out, every, count, sel?, scale?, [x,y,w,h]?, columns?]` | 每隔 `every` ms 拍 `count` 帧，拼成一张带编号的 PNG。 |
| `["turn", value, group?]` | 3D 图形：设置 `window.__isoTurn`（数字作用于第一个转组，`group` 指定另一组，对象一次设多个）并等两帧。 |
| `["orbit", out, from, to, step, sel?, scale?, [x,y,w,h]?, columns?]` | 3D 图形：跨第一个转组各角度的连拍拼图，每帧带标注。`["orbit", "swap.png", 129.7, 130.2, 0.1, null, 6, [x, y, w, h]]` 是一次顺序变化的 6× 特写。 |
| `["lines", out?, sel?, { tolerance }?]` | 下文的线端检查，在前面动作留下的任何位姿（分离态、行程中途）下运行。`out` 输出卡面图，把每个悬空端圈出来。失败会让运行以退出码 1 结束。 |

陷阱：
- **`scroll` 之后截图是正确的**，所以可以滚到页面更下方去看某个图形。给整个卡面足够高的视口（`--height 1300`）仍是最简单的做法：滚动位置 0 时图形可见，它的 `IntersectionObserver` 启动它。
- **拼图内的帧距是 `every` 加上截图耗时**（60–200 ms，重 WebGL 页面更久，因为截图还会卡住动画帧）。更快的过渡：在拼图之前放 `["slow", 0.05]`，之后放 `["slow", 1]`。`wait`、`every` 与页面的 `setTimeout` 定时器保持实时，所以 0.05 慢放下每 100 ms 一张的拼图在页面时间里相隔 5 ms，而空闲导览的恢复定时器仍按挂钟触发：一次按键只能把它推迟约 3.6 s 实时，所以每张慢速拼图之前再按一个无害的键。加载即开始的事件需要页面从第一帧就慢放：用 `--preload` 挂一个含 `window.__driveSpeed=0.04` 的文件。
- **慢放模式不慢放定时器。** `setTimeout` 走挂钟，所以一次很长的慢速截图期间，空闲导览的恢复定时器（Raptor 的 3.6 s `quietTour`）可能重启导览，在拼图中途关上引擎。每张慢速拼图之前先停掉导览、等待静止：预加载一个针对该定时器的 stub（`const st = window.setTimeout; window.setTimeout = (f, d, ...a) => (d === 3600 ? 0 : st(f, d, ...a));`），按 `Escape`，跑 `["until", "document.querySelector('[data-readout]').textContent.includes('cold')"]`，然后才按开启过渡的键。标注 "opening" 却从一个已经打开的导览开始的拼图，拍到的是关闭。
- **等待阶段，不要猜。** `["until", "document.querySelector('[data-readout]').textContent.includes('main stage')", 8000]` 在读数区到达该阶段时立刻返回。
- **`null` 选择器就是默认值。** 每个动作里缺失或 `null` 的选择器都指第一个 `.iso-plate`（`key` 用可聚焦的 `[tabindex="0"]`），所以 `["sheet", "s.png", 200, 16, null, 0.5]` 拍的是卡面。
- **长 eval 字符串会破坏行内 JSON 引号。** 带 `eval` 或 `until` 的东西放进 `--actions steps.json`。
- **页面把实时代码内联为 `<script type="module">`**，所以顶层变量对 `eval` 不可见。改从 DOM 读状态：读数区文本、`aria-valuetext`、`data-*` 属性。要数帧或每帧读值，用 `--preload` 装一个钩子（它先于页面运行，所以能包住 `requestAnimationFrame` 或 `HTMLCanvasElement.prototype.getContext`）。

## 线端
审计只看记录的形状，从不看线标记，所以它看不见停在面中间的接缝、刻度线、rib 或刻度。`scripts/lines.mjs` 直接检查图画本身，在无头 Chrome 里：

```sh
node scripts/lines.mjs page.html --out shots/lines.png
node scripts/lines.mjs page-light.html --out shots/lines-light.png --reduced
node scripts/drive.mjs page.html '[["key"," "],["wait",2000],["lines","shots/lines-apart.png"]]'
```
```
line ends: 3 of 1148 ends on 295 lines float
  iso-line faint in it k -0.080  end  7.25 px from anything   at card 507.4,407.2   length 75.7   d M392.1 381.7L507.4 407.2…
```
卡面里每个 `.iso-line` 的每条开子路径（接缝、凹槽、来自 `fadedSvg` 的 rib、刻度线、刻度、指针、导线）必须终止在另一条描边、一个圆点或一条外轮廓的 1 viewBox px 之内，或被绘制顺序在其后的填充盖住。短直标线（7 px 以内：一根刻度）需要一端在 2 px 内生根；两端都悬空即失败。kit 自身的外轮廓、折线、bevel 和管边不检查，被 `fadeLineSvg` 渐变淡出的端点也不检查。`lineSvg(d, { free: true })`（或 `"start"`、`"end"`）标记一个有意停住的端点：代表印刷文本的刻度线、指针尾部、指针尖端。除此之外不得使用。它以卡面像素打印每个悬空端，可直接用于 `capture.mjs --zoom`，并给出 `d` 的开头方便你在构建里找到它；`--out` 在 2× 的卡面截图上把它们圈出来。两个主题都要跑，图形静止的每个位姿都要跑，修到它打印 0 为止：

| 你看到 | 修法 |
|---|---|
| 盒面上从角落缩进的接缝或焊线 | 用 `k.sideSeam(plan, z, P, steps)` 作为平板的 `inner`：它包住角落、终止在外轮廓上（`craft.md`，第 3 节）。 |
| 一个面上两端缩进的加强筋或面板线 | 让它贯穿整面：从面的底到顶，或从端到端。 |
| 停在接缝之前的 rib | `ribsOf(…, { seams: true })`，或把 `s0`、`s1` 设在带的两端。 |
| 悬空在光板上的刻度，或挂在边下方的刻度 | 放到刻度条上，在其边上生根（`topTicks` 的 `edge`，`sideTicks` 的 `top` 放在面的顶边）。 |
| 通风或格栅线 | 闭合槽：细圆角外轮廓，不是线。 |
| 穿到部件下方、刚过它就停住的线 | 先画线、画全长，让部件盖住它。 |
| 标签牌上的刻度线 | `free: true`。它们代表文本。 |

## 审计
截图只能抓到你想到要看的东西。带管道、电缆和圆形部件的图形还需要几何检查，因为穿过管道的电缆、或画在前面物体之上的部件，在 1× 下看不见，在 4× 下很明显。把 `kit/audit.mjs` 接进构建（`kit.md`，第 12 节）：helper 写入同一个 `A.recorder(P, { order, spring })`，构建调用 `A.settle(R, P)` 并以 `A.auditOrExit(R, P)` 结尾，然后运行：

```sh
node examples/raptor-engine/build.mjs --audit
```
```
clearance: 0 problems
clearance apart: 0 problems
terminals: 0 ends not on a mount
loose ends: 0
screen folds: 0
support: 0 unsupported solids · 0 hanging tubes · 0 sunk pairs
depth order: 0 problems
through in mid-flight: 0 pairs
self-overlap: 0 chunks whose outline crosses itself on screen
wobble: 0 smoothed profiles whose slope turns between its ends
saddles off their host apart: 0
stand-in shapes: 0 items whose recorded shape covers too little of what it draws
crowding: 0 pairs where a bend or end touches another line on screen
free ends apart (marked free, not failing): 35
audit · 80 tubes · 267 solids · 478 items · 1119 depth states · 1707702 overlaps · 4292 order rules · 151.9 s
audit passed
```
它打印 `audit passed` 或 `audit failed: n problems`，任何失败都以非零退出码结束。每一行都算数，包括运动中途发生的事和 `items with no shape`，只有两个供人阅读的清单除外：`in passing` 与 `free ends apart`。深度顺序与穿透（tube 对万物、实体对实体）在同一批回放帧上检查：弹簧开合至静止的每一帧、每个错峰边界两侧 8 ms 内反转的每一帧（`reversalsOf`：Raptor 的 35 ms 错峰上为 0.027、0.043、0.062、0.078 … 0.393 s），以及前缀状态（`prefixStates`）。深度用这些帧的每四帧之一。如何解读与修复每一行：

| 行 | 含义 | 修法 |
|---|---|---|
| `through A × B  clearance -2.4` | 管 A 在该弧长范围内与 B 相交。 | 让 A 绕开 B 重新布线，留约 1.5 个半径余量，或移动 B。只有 A 端缘落在其上的那个形状可豁免，且仅在该端一个半径左右范围内。 |
| `close A × B  clearance 0.2 < 0.6` | A 经过 B 时余量不足其半径一半。 | 微调 route；加宽线束通道间距。 |
| `clearance apart: through share 1 …` | 分离态下某根管穿过了某个东西。 | 改那个装配体的爆炸向量。 |
| `terminals: A end 1.40 from B (rim -1.1…1.3)` | A 的端点，或其端法兰的轮缘，没有落在安装座上：悬空、倾斜，或法兰比下面的凸台宽。 | 让 route 恰好沿表面法向终止在表面上；把凸台做得至少与法兰一样宽；在曲面上把法兰安在鞍形垫块上。电缆绝不停在夹箍上。 |
| `loose ends: share 1 A end touches nothing that moves with it` | 分离后端点悬在空中：没有任何属于其他所有者且随之移动的东西（它自己的法兰或外壳不算）。 | 给它一个随之移动的安装座；或者，如果它本就该脱落（带法兰的管道、另一装配体上的连接器），标记 `free`，让它以可选形式列在 "free ends" 下。 |
| `self-overlap: A:3 its outline folds back on screen` | 某分段的外轮廓自交：线以小于自身半宽的屏幕半径转弯（指向观察者、又在端口附近转弯的一条腿）。 | 经弯头球离开端口（Raptor 的 `elbow`），给转弯更多直腿，或在朝向观察者的平面内弯（Raptor 的 `sideOn`，`craft.md`，第 8 节）。 |
| `wobble: A dr/ds turns at s = …` | 由手打节点平滑出的轮廓，坡度出现平台与反转，于是色带呈阶梯。 | 给它解析的 `r(s)` 并传 `smooth: { slope }`。 |
| `saddles off their host apart: A (piece) is cut to B (host piece)` | 鞍形垫块随另一装配体飞走，露出被切的底面。 | 把垫块归给宿主的装配体；移动的管道离开它的平面。 |
| `solid  state  A × B  sunk 1.81 deep` | 两个不同装配体的实体在该帧互相穿过。 | 同管：修顺序或向量，或在外挑物下打开间隙。 |
| `screen folds: A turns 150° on screen for 78° in 3D` | route 在屏幕上折返，读作尖角。 | 在转弯之前让腿在屏幕上走侧向。 |
| `screen folds: A turns 110° on screen round a 0.4 px bend` | 可见的弯收缩成一点：圆角被侧看，两条腿交成 V。 | 在接头件内转弯（球三通、线以 45° 离开）、在朝向观察者的平面内弯，或移动端口使其法向横过屏幕。 |
| `through in mid-flight: apart 0.233 s A × B clearance -1.6` | 在该回放帧中 A 穿过了 B。 | 修顺序或向量（`motion.md`，"Order the stagger"）：外侧部件先走；指向另一装配体表面的向量需要那个装配体更早出发；螺纹件共用一根弹簧。 |
| `crowding: A bend × B outlines overlap 0.05 px` | A 的弯或端在屏幕上落在 B 的外轮廓上，读作接头或穿入 B 的线。 | 重新布线，让相遇成为两条直线的一次清晰交叉，或留下可见间隙。豁免某对（`allow`）之前必须先用 8× 看过。 |
| `crowding: A end × B (rod)` | A 的端或弯落在细长实体的外轮廓上：连杆、活塞杆、立柱、导轨或把手（任何长于其半径或半宽 4 倍的实体）。读作杆插进了 A 的接头件。 | 从杆的侧面横向接近端口，或转动弯头让最后一腿横过屏幕。 |
| `stand-in shapes: A its shapes cover 4% of its drawing` | A 记录的形状远小于它实际画的屏幕面积，审计只检查一条细缝，对其余部分一言不发。 | 记录你所画的真实形状（滑出密封套的杆用 `A.slide`）。豁免某项（`cover: [name]`）仅当其绘制确实延伸到本体之外，且看过之后。 |
| `crowding: C fitting × B` | 夹箍落在另一条线的 2 px 之内，读作那条线从它上面长出来。 | 改爆炸向量或夹箍角度。 |
| `support: loose A` / `hanging A` / `sunk A × B 1.2 deep` | 某实体或刚性管没有接触任何通向底座的东西，或埋在 B 中。 | 加上承载它的支架、螺柱或板；下沉件修接触（轮缘落表面，被宿主切割的垫块标 `seated`；`seated` 只豁免其 `cut` 内的宿主）。 |
| `order  A is in front of B but drawn first` | 重叠处 A 的表面更近，但 B 画在它之上，静止或运动中途帧皆然。 | `orderKeys` 通常能修掉；剩下的意味着某条规则从循环里掉了，去那个循环里找互锁对。 |
| `cycle  A … (n the other way)` | A 与 B 各自在某处位于对方之前：屏幕上互相穿透。 | 改几何：管在套环处留隙、带在环处切开、杆终止在球上、蜗壳改相切、阀门移到直段、垫块避开宿主的外轮廓。 |
| `in passing` | 仅在均匀状态（所有装配体处于同一 share，页面从不显示）下互锁，或无法用任何 `k + lift · share` 排序。 | 不是失败。同样的事出现在回放帧里就是 `depth order` 问题。 |
| `items with no shape` | 某物被画出但没有记录形状，因此没有任何检查覆盖它。 | 在画它的 helper 里记录。 |

零审计是必要条件，不是充分条件：它看不见接缝、阶梯状色调或停住的纹理，而且只检查你记录过的东西。用一个替身形状让它闭嘴是 bug，这正是它会因此失败的原因。先跑线端检查，然后用眼睛看。

## 环绕（3D 图形）
带转组的图形（`references/3d.md`）要加跑环绕审计和浏览器检查。浅色页面与深色页面都要跑。
```sh
node build.mjs --light --audit > audit.txt 2>&1 &   # the full run, in the background: ends "turn audit passed"
node build.mjs --light --audit --quick    # ≈ 10× fewer states while iterating: ends "turn audit quick"
node build.mjs --light --audit --quick --only=order,continuity   # a subset: the rest print "skipped", ends "turn audit partial"
node build.mjs --light --verify           # a page with window.__isoVerify (recorded shapes) for --order
node ../../scripts/turn-check.mjs build.mjs --fidelity
node ../../scripts/turn-check.mjs page-verify-light.html --order --step 1
node ../../scripts/turn-check.mjs page-verify-light.html --order --states clip.json     # hinges and clips: --step turns the first turn group only
node ../../scripts/turn-check.mjs page-light.html --pops --no-webgl --states tilt-path.json   # one hinge as a continuous path at 0.02°
node ../../scripts/turn-check.mjs page-light.html --pops --no-webgl --step 1 --out shots/pops
node ../../scripts/turn-check.mjs page-light.html --lines
node ../../scripts/turn-check.mjs page-light.html --perf --width 1440
node ../../scripts/turn-check.mjs page-light.html --perf --width 390 --throttle 4
node ../../scripts/drive.mjs page-light.html '[["orbit", "shots/orbit.png", 0, 345, 15]]'
```
**耗时。** 一个 28 部件、一个转组、一个铰链、一个剪辑的图形，快速跑 85 秒、完整跑 17 分钟，超出 10 分钟 shell 超时：完整审计放后台跑。快速运行欠采样（`continuity` 只查 100 个减半候选而非 800 个，顺序扫描只查十分之一状态），所以只作参考，只有完整运行的 `turn audit passed` 算数。带 `--only` 的运行以 `turn audit partial` 结束，绝不是 `passed`。

**状态。** 审计以 0.3°（order）和 0.05°（continuity）扫掠每个转组，外加 2000 个随机状态和每个顺序变化事件 ± 0.001°。运动剪辑（`clips: [{ name, at(t), from, to, frame }]`）逐帧走：一个手势、一次抓取、一次脱落。自由组与铰链组只在你给的状态上证明，所以每段剪辑都要给，且给多个转角。

**各检查行。** `separation`、`unseparated`、`cycles`、`forced`、`swaps`、`layers`、`rigid`、`swept`、`posed`、`folds`、`self`、`crowding`、`endon`、`coverage`、`depth`、`continuity`。`3d.md` 第 13 节列出每行的失败情形与修法。每行都有一个植入故障：下沉的垫块（`separation`）、三根倾斜短棍的风车（`cycles`）、竖直平面内弯折的纤维（`folds`）、30° 的导管（`endon`）、停住的 rib 行（`continuity`）。

**浏览器检查**（每项先跑对照组；对照组不失败说明检查本身坏了）：
- `--order`：把记录的形状放进 WebGL z-buffer 对照 DOM 填充：每个角度与剪辑状态下，内部像素 ≥ 4 的动态对为 0。
- `--pops`：一整圈上每度一阶差分（θ → θ + 0.02°）、0.1° 二阶差分：存活区域 0，6+ px 核心 0。它列出的 1–5 px 核心要逐个读。
- `--lines`：24 个角度下悬空端为 0。
- `--perf`：`3d.md` 第 15 节的预算，1440 与 390 加 4× CPU。

**环绕图。** 0–345° 步长 15°，然后在三个最大的顺序变化处以 0.1° 步长（审计在 "order changes" 下列出它们），再放慢跑每段剪辑（`["slow", 0.05]`）。读图要找：蜘蛛状角度（一只手从某侧看像腿）、消失在其他部件背后的部件、终止在另一部件外轮廓上的线。

### 3D 图形检查清单
- [ ] 完整状态集（非 `--quick`，非 `--only`）下 `turn audit passed`，含剪辑。
- [ ] 每个铰链与剪辑都用 `--states` 跑 `--order`，每个铰链都跑 0.02° 路径的 `--pops`（`3d.md`，第 14 节）。
- [ ] `turn-check` 的 order、pops 与 lines 为 0，fidelity 通过，每个对照组按设计失败。
- [ ] 15° 环绕图逐张读过；每个铰接圆盘、交叉与纹理端点在 8 个角度下 8× 裁剪，浅色深色都要。
- [ ] 浅色页面上材质读作金属：高光带随转动移动，色调交叉淡变处无突变。
- [ ] 每个锚定到组的着色器以 0.1° 步长跟随；世界空间效果不随转；墨停在遮挡描边（遮罩与部件相遇处 8× 裁剪）。
- [ ] 预算在 1440 与 390 × 4 下实测，密集图形需要时用半帧率杠杆。

## 特写
拥有者是在浅色主题的一张特写里发现 Raptor 的毛病的：盖在主管道上的电缆、呈阶梯状的钟形件、戛然而止的螺栓行。抢在任何人之前，自己把这样的特写拍遍每个角落。

1. **构建两个主题**（`node build.mjs` 与 `node build.mjs --light`）并清点接头处：每个法兰、三通、弯头、球接头、夹箍、阀门、波纹管、带、鞍形垫块与交叉，每个曲面体（钟形件、喉部、穹顶、锥体、阀门鼓包、球），每个被 `bandsOf` 切开的身体的带接缝，以及每处纹理结束的地方。平面上也一样：盒面上每条接缝、焊线、加强筋与装饰线（够到两个角了吗？）、板上每行刻度或标线（在刻度条上吗？）、每行 rib 沿轴的两端、每根带纹理的软管在分段接头与卡套处、每根滑动的杆（静止、行程中途、满行程），以及每个带文本或着色器内容的窗口或屏幕。
2. **装配态下在两个主题中以 4× 拍摄每个区域。** `--zoom x,y,w,h` 以卡面像素取区域并按 `--zoom-scale`（4）放大：
   ```sh
   node scripts/capture.mjs page.html --out shots/joint-dark.png --zoom 200,80,220,170
   node scripts/capture.mjs page-light.html --out shots/joint-light.png --zoom 200,80,220,170
   ```
3. **还要拍分离态**，如果图形可以拆开。驱动到那里，等静止，再以 4 倍拍一个区域。Raptor 用 Space 切换分离，其读数区只有在每根弹簧都到位后才开始 `apart ·`，所以 `apart.json` 是
   ```json
   [["key", " "], ["until", "document.querySelector('[data-readout]').textContent.startsWith('apart')"], ["wait", 400],
    ["shot", "shots/apart-joint.png", null, 4, [200, 80, 220, 170]]]
   ```
   用 `node scripts/drive.mjs page.html --actions apart.json` 运行，然后在 `page-light.html` 上再来一遍。
4. **按此顺序在每张 PNG 里找这些毛病：** 穿过或钻进某物的线；近处的线被画在后面的交叉；落在另一条线外轮廓上的弯、端或夹箍；立在端口之外或陷进端口的法兰；曲面上跨过的阶梯色块、扇贝状边缘或浅色楔形；终止在直线切口上的色带；停在表面中间的一行 rib、圆点或刻度线；分段接头处横过管子亮带或暗带的发丝线；在外轮廓上留下缺口的接缝；没够到应有边缘的接缝、加强筋或 rib；顶面上无所依附的短线；边缘笔直生硬的软管纹理，或在分段接头处重新开始或被切断的纹理；运动中外轮廓断裂的杆；越过窗口的文本；溢出开口边缘的着色器内容。与上一轮同一区域的截图对比。
5. **着色器：** 同样区域在效果运行期间拍摄，外加用 `["slow", 0.05]` 放慢的连拍拼图（`webgl.md`，第 9 节）。

**细节巡检。** 最后，以 4× 在裁剪网格里扫一遍（Figure 拍主体与机构，Hero 或 Epic 拍整幅图；`SKILL.md`，工作流第 1 步），找任何上面没有真实东西的面、角或底座区域。每个图形都要求高细节（`SKILL.md`，"Every creation is highly detailed"）：加上本就该在那里的真实部件（螺钉、接缝、倒角、标签牌、刻度、承载物的支架），绝不加不属于任何部件的装饰。

## 浅色主题的着色器
浅色是发布主题，纸上辉光就是墨。迄今每次浅色转换首先在单帧截图看不见的东西上失败：光落下去墨却升起来、辉光之前的浅色闪现、橙红阶段、描边旁边的毛边。所以除了看，还要量墨（`webgl.md`，第 8 节）。

**每帧墨量。** 把这段存成 `ink.js`，用 `--preload` 传入。页面画的每一帧，它记录一个 canvas 区域压在白底上的平均墨量，`255 − lum(rgb + 255 − a)`，与绘制在同一任务里回读：
```js
const get = HTMLCanvasElement.prototype.getContext;
HTMLCanvasElement.prototype.getContext = function (kind, ...rest) {
  const gl = get.call(this, kind, ...rest);
  if (gl && String(kind).startsWith("webgl") && !this.__gl) {
    this.__gl = gl;
    for (const name of ["drawArrays", "clear"]) {
      const call = gl[name].bind(gl);
      gl[name] = (...args) => { gl.__drew = true; return call(...args); };
    }
  }
  return gl;
};
const raf = window.requestAnimationFrame.bind(window);
window.__ink = [];
window.requestAnimationFrame = (callback) => raf((now) => {
  callback(now);
  const canvas = document.querySelector(window.__inkCanvas || "canvas");
  const gl = canvas && canvas.__gl;
  if (!gl || !gl.__drew) return;
  gl.__drew = false;
  const [x, y, w, h] = window.__inkBox || [0, 0, canvas.width, canvas.height];
  const px = new Uint8Array(w * h * 4);
  gl.readPixels(x, y, w, h, gl.RGBA, gl.UNSIGNED_BYTE, px);
  let ink = 0;
  for (let i = 0; i < px.length; i += 4) {
    const bare = 255 - px[i + 3];
    ink += 255 - (0.2126 * (px[i] + bare) + 0.7152 * (px[i + 1] + bare) + 0.0722 * (px[i + 2] + bare));
  }
  window.__ink.push(Math.round((ink / (w * h)) * 100) / 100);
});
```
- **选好测量对象。** 过渡之前，用 `eval` 设置 `window.__inkCanvas`（选择器）和 `window.__inkBox`（canvas 设备像素中的 `[x, y, w, h]`，从左下角量起；CSS px 乘 `canvas.width / canvas.clientWidth` 换算）。之后用 `["eval", "window.__ink.join(' ')"]` 读取各行数据。
- **每个重要区域做一次：** 一个腔体、核心、只有后备覆盖的区域。放慢运行，覆盖首次来光（`--preload` 再挂一个含 `window.__driveSpeed=0.04` 的文件）、每次相位变化与淡出。
- **看什么。** 墨随物理量单调变化：光进来时升，光退去时降。交接处没有驼峰，首次来光时没有凹陷。
- **它抓到了什么。** 修复之前，加力燃烧室腔体在切换瞬间峰值 3600；修复后从 1894 单调降到 155。那些行是该图形自己的单位，是其窗口区域上的求和，不是本钩子的均值。水波槽的浅色页面上，钩子读数静止时 14.2，随灯亮而下降，因为那个页面的光照亮纸张。

**沿色阶的颜色。** 凡发热或冷却的东西，`eval` 读取中心与边缘像素在若干温度下的值（或放慢运行中若干温度段的值），记下来。顺序必须是暗红 → 橙 → 黄 → 近白，边缘比中心冷，中途不得出现橙红或灰色阶段。

**横截面。** 读一行横过火焰、射流或水流的墨量。它在轴线上达峰，向半透明边缘下降。边缘偏重的剖面是空心的、只剩描边的火焰。

**8–16× 下的描边。** 浅色下以 8–16× 裁剪每处墨与 SVG 描边相遇的地方（切面、轮缘、口部、折线、有实体进入的 canvas 边缘）。找：墨与线之间的浅色缝隙、墨盖过线、或被墨清空的描边。

**两条路径，以及嵌套。** 深色构建应与基线一致，因为每处浅色变化都以 `uLight` 为闸。渲染浅色页面上的深色底板与独立渲染的浅色底板，各自都跑有 WebGL 与无 WebGL：一条 `:not([data-theme="dark"])` 规则可能穿过页面打进深色底板。

## 评审检查清单
**它是一个实物**
- [ ] 一眼看去它读作一件真实、做工良好的东西，而且你能叫出它的名字。
- [ ] 它的机构对应概念：什么在动、那意味着什么，一句话能说完。
- [ ] 它不是一堆抽象板片，也不是一整块光板。

**部件与体积**
- [ ] 行内图形 30–60 个实体；真正部件更多的主角主体可以远超此数（Raptor 约 270）。每个部件都搭在另一部件上，各有职责。
- [ ] 侧面有明暗、顶面更浅；主平板有倒角；基座下方与抬起部件下方有光晕。
- [ ] 小细节从属于部件：板角螺钉、凹槽、刻度尺、滚花、标签牌。

**线条**
- [ ] 4× 下每条线终止在一个面、另一条线或一个端点圆上。没有东西停在空中。
- [ ] 没有引出线、编号气泡、尺寸箭头或漂浮标签；至多一个镌刻标签。
- [ ] 画家序处处正确：背后没有东西透出来，弹簧与框架已拆分。
- [ ] **审计归零。** 图形含管道、电缆或圆形部件时，`node build.mjs --audit` 以 `audit passed` 结束：每一失败行都为零，装配态、分离态、回放爆炸的每一帧（打开、关闭与中途反转）都为零。没有互锁被键偏置藏起来，每个被豁免的对（`allow`、`crowd`）都用 8× 看过。
- [ ] 没有管道或电缆穿过另一管道、电缆或实体，每个交叉都按深度顺序画：近处的线在上、在直段交叉、深度上分得足够开。
- [ ] 没有线横穿主体表面（明明可以沿结构走）；没有弯在屏幕上收缩成 V；装配态与分离态下，没有弯、端或夹箍落在另一条线的外轮廓上。
- [ ] 每个法兰都坐在自己的端口上（端口为曲面时坐在鞍形垫块上）；每个套环、夹箍、带、波纹管与阀门都在所包裹的管道上留隙；每个阀门与波纹管都在直段上；没有 route 在屏幕上折返；每个端点（分离态也一样）都终止在法兰、接头、连接器或端点圆上。
- [ ] **接头特写。** 每个接头区域都在两个主题、装配态与分离态下以 4× 拍摄（见"特写"），每张 PNG 都读过。
- [ ] **无阶梯。** 每个曲面在 4× 下都是平滑着色：没有阶梯色块、没有扇贝状梯田、没有浅色楔形、没有终止在直线切口上的色带、带接缝处没有拐折；收腰体沿真实轮廓；接缝与外轮廓相接处无缺口。
- [ ] **线端归零。** `node scripts/lines.mjs` 在两个主题与每个静止位姿下都打印 `line ends: 0`；每个 `free` 端都是代表文本的刻度线、指针尾或指针尖。
- [ ] **形状为真。** 没有替身形状：记录的就是画出的，包括滑动的杆。
- [ ] **纹理端点不突兀。** 每行 rib、螺栓圆点、刻度线或凹槽都终止在真实边缘上或淡出；没有任何一行以全强度停在表面中间，平面也不例外。盒面接缝包住角落，rib 行终止在自己的接缝上，刻度坐在刻度条上，软管纹理沿其横截面并穿过每个分段接头。管道条纹延续到端盖上，在任何分段接头处都不出现发丝线，强弯锥管（蜗壳）上也是如此。

**色调与颜色**
- [ ] 基座 `lo`、结构 `mid`、主体 `hi`，恰好一个 `lit` 强调。
- [ ] 单色，除非颜色本身是主题。

**卡面与文字**
- [ ] `Fig n` / 标题 / 提示 / 实时读数区在角落，卡面下方有图例键与图注。
- [ ] 每个数字都真实、来自模型。读数随物体运动变化，其文字与数字来自同一时刻：模型给出的阶段词配上滞后仪表给出的数字，会在阀门还没开的时候读出 `relief 85 bar`。
- [ ] 机器显示的文本以其最宽字符串适配窗口，并被裁剪在窗口内。

**运动与无障碍**
- [ ] 缓动、平静、无吸附；有空闲导览；交互时暂停。
- [ ] 离屏即停；`--reduced` 下仍正常；无控制台错误（包括 React key 警告）。
- [ ] 键盘可用、焦点环显示、`aria-valuetext` 以文字读出状态。

**着色器（若图形有；`references/webgl.md`）**
- [ ] 每个过渡（开始、每次相位变化、稳定、停止）都有一张连拍拼图，用 `["slow", 0.05]` 放慢（加载即开始的效果用 `--preload` 挂 `window.__driveSpeed=0.04`），让每次交叉淡变的每一帧都可见：无突然变色、无单帧闪现、无被裁切的东西、淡出期间亮度绝不上升。
- [ ] 效果与 SVG 相接处以 2× 与 4× 裁剪：无接缝、硬边、色带、暗色项圈或双线；平面上的东西与该平面的线对齐。
- [ ] canvas 外围行列在每个相位下 alpha 均为 0。
- [ ] 无 WebGL（`--no-webgl`）时仅 SVG 也读得通；减弱动效下得到一帧有代表性的静帧；空闲与离屏时循环停止。
- [ ] **浅色主题**（`webgl.md`，第 8 节；上文"浅色主题的着色器"）：
  - 辉光靠饱和度表达：饱和主体、浅色核心、彩色边缘，绝不是深色或棕色墨。
  - 光照到的地方被着色，容纳光的腔体是更深的物理底色。
  - 热体按黑体顺序变色，没有橙红阶段。
  - 烟与蒸汽是浅灰。
  - 空气中没有光晕。
  - 每帧墨量随光单调变化，覆盖首次来光、每次交接与淡出。
  - 8–16× 下墨停在每条描边的内缘。
  - 后备显示同样的墨与底色，交接给着色器时无凹陷。
  - 深色不变，浅色页面上的深色底板仍正常。

**构图**
- [ ] 居中，约占卡面 55–65%；不触碰角落标签。
- [ ] 390 px 下仍可读、无横向滚动，选中某部件时与点火过程中也一样，不只静止时：最长的读数不得跑到控件下方。

## 常见毛病与修法
| 你看到 | 修法 |
|---|---|
| 某部件透过前方物体显形 | 它画得太晚。把它提前，或拆分前方部件。 |
| 立柱与面相接处横着一个椭圆 | 给连续圆柱画的整圆 `ring` 露出了后半。用 `sideArc`（只画前半），或让圆柱自己的外轮廓形成这条边。 |
| 立柱看起来贴在它穿过的块体上 | 分两段画：下方一段、上方一段，块体画在中间。 |
| 折线或倒角停在角落之前 | 在 `slabOf`/`cylinder` 上用 `bevel`。它本来就终止在外轮廓上。不要手画边线。 |
| 平坦死板的侧面 | 你传了 `flat`，或实体高度为 0。给它厚度。 |
| 太空 | 加结构，不加纹理：支脚、带刻度尺和限位块的导轨、标签牌、螺钉、旋钮、第二级。 |
| 太挤 | 把类纹理的重复与色调凹槽降到 `faint`；保留一个 lit 强调。 |
| 图形在卡面里太小 | 用更小的 `pad` 适配，或收紧传给 `fitProjection` 的点。 |
| 标签页恢复焦点时跳变 | 把 `dt` 钳制到 1/30 s。 |
| 只有主页面上有 key 警告 | 见 `react.md`：给元素 props 的根设 key。 |
| 相位变化处着色器颜色跳变 | 给颜色自己的慢包络，由物理量驱动，不由相位标志驱动。见 `webgl.md`，第 7 节。 |
| 辉光里出现直边，常在 canvas 边界 | 某个项在边界上不为零。在每个 `if`、边界与 canvas 边之前把它窗口化为零。 |
| 辉光穿过地面或越过立柱 | 它在屏幕空间。用射线与地面命中点在世界空间重建，并把简单部件交给着色器作遮挡物。 |
| 发光轮缘下方有暗色项圈 | 轮缘以普通混合叠在着色器上。把它移到 `mix-blend-mode: screen` 的叠加 SVG。 |
| 柔和辉光里的平坦色带 | 在 `tonemap` 之后加门控三角抖动。 |
| 浅色下辉光读作深红或棕色烟雾 | 它是深色再加深、alpha 当亮度用。从纸面色阶求解墨：饱和主体、浅色核心、alpha 下限（`webgl.md`，第 8.1 节）。 |
| 浅色下首次来光先变浅再变深，或淡出发灰、变重 | 逐项淡出、只淡 alpha，或色相在固定 alpha 下变红。对成品墨只淡一次，能量与 alpha 一起变暗，色相取稳定亮度时的值（`webgl.md`，第 8.2 节）。 |
| 浅色下边缘出现浅色毛边或白色缝 | 墨停在描边之前，或清空了没人描边的折线。让它终止在描边内缘（0.3 vb），折线用墨画（`webgl.md`，第 8.6 节）。 |
| 深色底板的后备在浅色页面上消失 | `.iso:not([data-theme="dark"])` 规则穿过页面命中了它。把深色规则放最后，或以底板自身主题为键（`webgl.md`，第 8.5 节）。 |
| 管道或电缆看起来贴在某部件上或切断它 | 它的分段在同一层。按 `mid` 对每个 `tubePieces` 分段做深度排序，穿插处用更短的段。若真的穿过了部件，重新布线；`--audit` 会列出每种情况。 |
| 电缆或传感线扇形横过主体表面并越过主管道 | 它们被逐点布线。沿结构重布：沿管道一侧上行、以夹箍通道绕体、绕到侧面去远端端口（`craft.md`，"Choosing waypoints"）。 |
| 修好一个交叉的顺序，另一个或分离位姿就坏 | 键是手调的。记录形状，让 `A.settle` 定键，把它报告为互锁的东西在几何里修掉。 |
| 套环、带或夹箍盖住管道近侧，或管道画在套环表面之上 | 管道以一整段穿过它。在套环处给管道留隙（`gaps`），让一段终止在每个面上。 |
| 体上的环在体上方露出后半 | 体在环下是一整条带。在环处切开。 |
| 阀门或波纹管在两端切进管道 | 它坐在弯上。移到直段，至少自身长度加两处圆角切口。 |
| 钟形件、穹顶或锥体上出现阶梯色块 | 分面着色。把曲线节点标为 smooth（`[s, r, 1]`，默认平滑着色）或传 `smooth: true`；用 `G.bandsOf` 把体切成带。 |
| 喉部、锥体或圆饼上的色带停滞并在扇贝中突跳 | 手打节点平滑出的轮廓：坡度在每个节点出现平台。把轮廓写成解析 `r(s)`，把导数以 `smooth: { slope }` 传入（`wobble` 会列出它们）。 |
| 平滑着色部件内部出现发丝缝 | 色调面相邻相接。用 kit 的 `solidSvg` 与 `seamless` 路径（smooth lathe 和 `sphereOf` 会设置它）及 `ISO_CSS`。 |
| 一行 rib 或螺栓圆点停在表面中间 | 硬性 `least` 截断。在 `ribsOf` 或 `dotsOf` 上用 `fade: [lo, hi]`。 |
| 平滑着色锥体或钟形件上带直边的浅色楔形 | 色调块之间的裸填充：同一色调的块反向绕行在 nonzero 规则下抵消，或色带终止时没有收窄。kit 会定向每个色调多边形并让色带收窄；自己构建色调路径时要定向。 |
| 收窄体看起来像带浅色条的直锥 | 它被取了包络。让 `lathe` 选 `fill: "auto"`（或传 `"surface"`）。 |
| 发丝线横过导管的亮带或暗带 | 分段接头处体与条纹在同一线上切断。`tubePieces` 让条纹越过体；改动时保持这一点。 |
| 接缝与外轮廓相接处外轮廓呈虚线 | 接缝画在实体之后。把它们作为 `inner` 传入。 |
| 管道条纹停在端头之前 | 没有端盖的端。`tubePieces` 默认给每个端加盖；可见的端不要传 `caps: false`。 |
| 图形分离时部件沿安装座滑动 | 它们以一个装配体的向量在另一个的弹簧上移动。给该件那个装配体的 `ride`。 |
| 长回转体在带接缝处外轮廓拐折 | 用 `G.bandsOf` 构建，用它的 `sidesOf` 一次画出侧面（`kit.md`，第 10 节）。 |
| 纹理线停在面中间 | 终止在真实边缘，或用 `fadeLineSvg(points, { fade })` 画让它渐隐。`scripts/lines.mjs` 会逐个列出。 |
| 盒面接缝停在角落之前 | 用 `k.sideSeam(plan, z, P, steps)` 作 `inner`。 |
| 软管编织或波纹边缘笔直生硬，或在分段接头断裂 | `tubePieces(…, { rings: { pitch, twist, cross: true } })`。 |
| 杆滑动时外轮廓出现缺口 | 用 `G.rodOut` 的一根杆、在密封套处裁剪、以 `A.slide` 记录；绝不用重叠副本。 |
| LCD 或计数器数字越过窗口 | 让字形适配窗口高度与最宽字符串，并裁剪。 |
| 阀门或鼓包上出现零散轮廓三角形 | 旧 kit 拼接过断裂的轮廓；现在侧面轮廓有缺口时 kit 会回退到包络。用当前 `lathe.mjs` 重建。 |
