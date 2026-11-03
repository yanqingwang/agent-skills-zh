---
name: gsap-plugins
description: GSAP 官方插件 Skill — 插件注册、ScrollToPlugin、ScrollSmoother、Flip、Draggable、Inertia、Observer、SplitText、ScrambleText、SVG 与物理插件、CustomEase、EasePack、CustomWiggle、CustomBounce、GSDevTools。当用户询问某个 GSAP 插件、scroll-to、flip 动画、draggable、SVG 描绘或插件注册时使用。
license: MIT
---

> **中文汉化版** · 上游：[greensock/gsap-skills](https://github.com/greensock/gsap-skills) · 原文件：`skills/gsap-plugins/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# GSAP 插件

## 何时使用本 Skill

在使用或审查涉及 GSAP 插件的代码时适用：插件注册、scroll-to、flip/FLIP 动画、可拖拽元素、SVG（DrawSVG、MorphSVG、MotionPath）、文本（SplitText、ScrambleText）、物理、缓动插件（CustomEase、EasePack、CustomWiggle、CustomBounce），以及 GSDevTools。ScrollTrigger 有独立的 Skill（gsap-scrolltrigger）。

**相关 Skill：** 核心补间（tween）使用 **gsap-core**；ScrollTrigger 使用 **gsap-scrolltrigger**；React 使用 **gsap-react**。

## 许可与安装（重要）

所有 GSAP 插件均**免费**，包括商业用途。自 [Webflow 收购 GSAP](https://gsap.com/blog/webflow-GSAP/) 起，Club GSAP 不再是付费层级，**任何插件都不需要会员资格、许可证密钥或授权 token** — 包括曾经的 Club 专属插件（**SplitText**、**MorphSVG** 等）。

- ✅ 一律从公开的 `gsap` npm 包安装：`npm install gsap`。所有插件都包含在内 — 以 `gsap/SplitText`、`gsap/MorphSVGPlugin` 等方式导入。
- ❌ **不要**生成带 GreenSock auth token 的 `.npmrc`，不要建议使用私有的 `npm.greensock.com` registry，也不要让用户注册 Club GSAP 来获取某个插件。那些做法已过时。

## 注册插件

每个插件只注册一次，让 GSAP（和打包器）知道要将其包含进来。对项目中用到的每个插件使用 **gsap.registerPlugin()**：

```javascript
import gsap from "gsap";
import { ScrollToPlugin } from "gsap/ScrollToPlugin";
import { Flip } from "gsap/Flip";
import { Draggable } from "gsap/Draggable";

gsap.registerPlugin(ScrollToPlugin, Flip, Draggable);
```

- ✅ 在任何补间或 API 调用中使用插件之前先注册。
- ✅ 在 React 中，在顶层或应用级别注册一次（如首次使用 useGSAP 之前）；不要在会重新渲染的组件内部注册。useGSAP 本身是一个插件，使用前需要注册。

## 滚动

### ScrollToPlugin

对滚动位置制作动画（window 或可滚动元素）。用于在不使用 ScrollTrigger 的情况下实现“滚动到元素”或“滚动到位置”。

```javascript
gsap.registerPlugin(ScrollToPlugin);

gsap.to(window, { duration: 1, scrollTo: { y: 500 } });
gsap.to(window, { duration: 1, scrollTo: { y: "#section", offsetY: 50 } });
gsap.to(scrollContainer, { duration: 1, scrollTo: { x: "max" } });
```

**ScrollToPlugin — 关键配置（scrollTo 对象）：**

| 选项 | 说明 |
|--------|-------------|
| `x`、`y` | 目标滚动位置（数字），或 `"max"` 表示最大值 |
| `element` | 要滚动到的选择器或元素（用于滚动进入视野） |
| `offsetX`、`offsetY` | 相对目标位置的像素偏移量 |

### ScrollSmoother

平滑滚动包装器（平滑原生滚动）。需要 ScrollTrigger 和特定的 DOM 结构（内容包装器 + 平滑包装器）。当需要平滑、惯性风格的滚动时使用。设置方式见 GSAP 文档；在 ScrollTrigger 之后注册。DOM 结构如下：

```html
<body>
	<div id="smooth-wrapper">
		<div id="smooth-content">
			<!--- ALL YOUR CONTENT HERE --->
		</div>
	</div>
	<!-- position: fixed elements can go outside --->
</body>
```

## DOM / UI

### Flip

用 `Flip.getState()` 捕获状态，然后应用变更（如布局或 class 变更），再用 `Flip.from()` 从先前状态动画到新状态（FLIP：First、Last、Invert、Play）。在两种布局状态之间制作动画时使用（列表、网格、展开/收起）。

```javascript
gsap.registerPlugin(Flip);

const state = Flip.getState(".item");
// change DOM (reorder, add/remove, change classes)
Flip.from(state, { duration: 0.5, ease: "power2.inOut" });
```

**Flip — 关键配置（Flip.from 的 vars）：**

| 选项 | 说明 |
|--------|-------------|
| `absolute` | flip 期间使用 `position: absolute`（默认：`false`） |
| `nested` | 为 true 时只测量第一层子元素（对嵌套 transform 更友好） |
| `scale` | 为 true 时缩放元素以适配（避免拉伸）；默认 `true` |
| `simple` | 为 true 时只动画位置/缩放（更快，精度较低） |
| `duration`、`ease` | 标准补间选项 |

#### 更多信息

https://gsap.com/docs/v3/Plugins/Flip

### Draggable

使元素可通过鼠标/触摸拖拽、旋转（spin）或甩动（throw）。用于滑块、卡片、可重排列表或任何拖拽交互。

```javascript
gsap.registerPlugin(Draggable, InertiaPlugin);

Draggable.create(".box", { type: "x,y", bounds: "#container", inertia: true });
Draggable.create(".knob", { type: "rotation" });
```

**Draggable — 关键配置选项：**

| 选项 | 说明 |
|--------|-------------|
| `type` | `"x"`、`"y"`、`"x,y"`、`"rotation"`、`"scroll"` |
| `bounds` | 限制拖拽范围的元素、选择器或 `{ minX, maxX, minY, maxY }` |
| `inertia` | `true` 启用甩动/惯性（需要 InertiaPlugin） |
| `edgeResistance` | 0–1；拖出边界时的阻力 |
| `cursor` | 拖拽期间的 CSS 光标 |
| `onDragStart`、`onDrag`、`onDragEnd` | 回调；接收 event 与 target |
| `onThrowUpdate`、`onThrowComplete` | 惯性生效期间的回调 |

### Inertia（InertiaPlugin）

与 Draggable 配合实现松手后的惯性运动；也可跟踪任意对象任意属性的惯性/速度，随后用一个简单补间让它无缝滑行到停止。使用 `inertia: true` 时与 Draggable 一起注册：

```javascript
gsap.registerPlugin(Draggable, InertiaPlugin);
Draggable.create(".box", { type: "x,y", inertia: true });
```

或者跟踪某个属性的速度：
```javascript
InertiaPlugin.track(".box", "x");
```

然后用 `"auto"` 延续当前速度并滑行到停止：

```javascript
gsap.to(obj, { inertia: { x: "auto" } });
```

### Observer

统一各设备上的指针与滚动输入。用于滑动手势、滚动方向或自定义手势逻辑，而无需像 ScrollTrigger 那样直接绑定滚动位置。

```javascript
gsap.registerPlugin(Observer);

Observer.create({
  target: "#area",
  onUp: () => {},
  onDown: () => {},
  onLeft: () => {},
  onRight: () => {},
  tolerance: 10
});
```

**Observer — 关键配置选项：**

| 选项 | 说明 |
|--------|-------------|
| `target` | 要观察的元素或选择器 |
| `onUp`、`onDown`、`onLeft`、`onRight` | 滑动/滚动在该方向超过容差时的回调 |
| `tolerance` | 判定方向前所需的像素数；默认 10 |
| `type` | `"touch"`、`"pointer"` 或 `"wheel"`（默认：`"touch,pointer"`） |

## 文本

### SplitText

将元素的文本拆分为字符、单词和/或行（各自包在独立元素中），用于交错（stagger）或逐单元动画。当需要按字符、按单词或按行动画文本时使用。返回一个包含 **chars**、**words**、**lines**（设置了 `mask` 时还有 **masks**）的实例。用 **revert()** 恢复原始标记，或交给 **gsap.context()** 还原。与 **gsap.context()**、**matchMedia()**、**useGSAP()** 集成。API：**SplitText.create(target, vars)**（target = 选择器、元素或数组）。

```javascript
gsap.registerPlugin(SplitText);

const split = SplitText.create(".heading", { type: "words, chars" });
gsap.from(split.chars, { opacity: 0, y: 20, stagger: 0.03, duration: 0.4 });
// later: split.revert() or let gsap.context() cleanup revert
```

使用 **onSplit()**（v3.13.0+）时，动画会在每次拆分时运行，使用 **autoSplit** 时在重新拆分时也会运行；从 **onSplit()** 返回补间/时间线可让 SplitText 在重新拆分时完成清理并同步进度：

```javascript
SplitText.create(".split", {
  type: "lines",
  autoSplit: true,
  onSplit(self) {
    return gsap.from(self.lines, { y: 100, opacity: 0, stagger: 0.05, duration: 0.5 });
  }
});
```

**SplitText — 关键配置（SplitText.create 的 vars）：**

| 选项 | 说明 |
|--------|-------------|
| **type** | 逗号分隔：`"chars"`、`"words"`、`"lines"`。默认 `"chars,words,lines"`。出于性能考虑，只拆分需要的部分（如不使用行时用 `"words, chars"`）。避免只拆 chars 而不含 words/lines，或使用 **smartWrap: true** 防止奇怪的换行。 |
| **charsClass**、**wordsClass**、**linesClass** | 每个拆分元素上的 CSS class。追加 `"++"` 可添加自增编号的 class（如 `linesClass: "line++"` → `line1`、`line2`、…）。 |
| **aria** | `"auto"`（默认）、`"hidden"` 或 `"none"`。无障碍：`"auto"` 会在拆分元素上添加 `aria-label`，并在行/单词/字符元素上添加 `aria-hidden`，使屏幕阅读器朗读该标签；`"hidden"` 对阅读器隐藏全部内容；`"none"` 不改动 aria。若必须暴露嵌套链接/语义，用 `"none"` 并配一份仅供屏幕阅读器的副本。 |
| **autoSplit** | 为 `true` 时，在字体加载完成或元素宽度变化（且拆分了行）时还原并重新拆分，避免错误的换行。**动画必须在 onSplit() 内创建**，以作用于新拆分出的元素；从 **onSplit()** 中 **return** 该动画，可在重新拆分时自动清理并同步时间。 |
| **onSplit(self)** | 拆分完成时（若 **autoSplit** 为 `true`，则每次重新拆分时）触发的回调。接收 SplitText 实例。返回 GSAP 补间或时间线，可在重新拆分时自动还原/同步该动画。 |
| **mask** | `"lines"`、`"words"` 或 `"chars"`。将每个单元包进一个带 `overflow: clip` 的额外元素，用于遮罩/揭示效果。只能选一种类型；通过实例的 **masks** 数组访问包装元素（若设置了 class，也可使用对应的 `-mask` class）。 |
| **tag** | 包装元素的标签；默认 `"div"`。内联场景用 `"span"`（注意：在某些浏览器中，旋转/缩放等 transform 可能无法在行内元素上渲染）。 |
| **deepSlice** | 为 `true`（默认）时，跨多行的嵌套元素（如 `<strong>`）会被进一步细分，避免行在垂直方向被拉伸。仅在拆分行时生效。 |
| **ignore** | 不参与拆分的选择器或元素（如 `ignore: "sup"`）。 |
| **smartWrap** | 仅拆分 **chars** 时，把单词包进 `white-space: nowrap` 的 span，避免单词中间断行。若同时拆分 words 或 lines 则被忽略。默认 `false`。 |
| **wordDelimiter** | 单词边界：字符串（默认 `" "`）、RegExp，或 `{ delimiter: RegExp, replaceWith: string }` 用于自定义拆分（如话题标签的零宽连接符，或非拉丁文字）。 |
| **prepareText(text, parent)** | 接收原始文本与父元素的函数；在拆分前返回修改后的文本（如为无空格语言插入断行标记）。 |
| **propIndex** | 为 `true` 时，在每个拆分元素上添加带索引的 CSS 变量（如 `--word: 1`、`--char: 2`）。 |
| **reduceWhiteSpace** | 合并连续空格；默认 `true`。自 v3.13.0 起也处理换行符，并可为 `<pre>` 插入 `<br>`。 |
| **onRevert** | 实例被还原时的回调。 |

**提示：** 只拆分要动画的部分（如只动画单词时跳过字符）。自定义字体要在加载完成后再拆分（如 `document.fonts.ready.then(...)`），或使用 **autoSplit: true** 配合 **onSplit()**。为避免拆分字符时字距偏移，使用 CSS `font-kerning: none; text-rendering: optimizeSpeed;`。避免 `text-wrap: balance`，它会干扰拆分。SplitText 不支持 SVG `<text>`。

**了解更多：** [SplitText](https://gsap.com/docs/v3/Plugins/SplitText/)

### ScrambleText

以打乱/故障效果为文本制作动画。在用打乱效果揭示或过渡文本时使用。

```javascript
gsap.registerPlugin(ScrambleTextPlugin);

gsap.to(".text", {
  duration: 1,
  scrambleText: { text: "New message", chars: "01", revealDelay: 0.5 }
});
```

## SVG

### DrawSVG（DrawSVGPlugin）

通过对 `stroke-dashoffset` / `stroke-dasharray` 制作动画来显示或隐藏 SVG 元素的描边。作用于 `<path>`、`<line>`、`<polyline>`、`<polygon>`、`<rect>`、`<ellipse>`。在需要“描绘”或“擦除”描边时使用。

**drawSVG 值：** 描述的是描边沿路径的**可见区段**（起点与终点位置），而不是“随时间从 A 动画到 B”。格式为 `"start end"`，用百分比或长度表示。示例：`"0% 100%"` = 完整描边；`"20% 80%"` = 仅 20% 到 80% 之间的描边（两端留空）。补间会把元素从**当前**区段动画到**目标**区段 — 例如 `gsap.to("#path", { drawSVG: "0% 100%" })` 从当前状态动画到完整描边。单值（如 `0`、`"100%"`）表示起点为 0：`"100%"` 等价于 `"0% 100%"`。

**必要条件：** 元素必须有可见描边 — 在 CSS 中或以 SVG 属性设置 `stroke` 与 `stroke-width`；否则什么都画不出来。

```javascript
gsap.registerPlugin(DrawSVGPlugin);

// draw from nothing to full stroke
gsap.from("#path", { duration: 1, drawSVG: 0 });
// or explicit segment: from 0–0 to 0–100%
gsap.fromTo("#path", { drawSVG: "0% 0%" }, { drawSVG: "0% 100%", duration: 1 });
// stroke only in the middle (gaps at ends)
gsap.to("#path", { duration: 1, drawSVG: "20% 80%" });
```

**注意事项：** 只影响描边（不影响填充）。优先使用单区段 `<path>` 元素；多区段路径在某些浏览器中渲染可能异常。`<use>` 的内容无法在视觉上改变。**DrawSVGPlugin.getLength(element)** 与 **DrawSVGPlugin.getPosition(element)** 返回描边长度和当前位置。

**了解更多：** [DrawSVG](https://gsap.com/docs/v3/Plugins/DrawSVGPlugin)

### MorphSVG（MorphSVGPlugin）

通过对 `d` 属性（路径数据）制作动画，把一个 SVG 形状变形（morph）为另一个。起点和终点形状不需要相同数量的点 — MorphSVG 会转换为三次贝塞尔曲线并按需加点。用于图标之间的变形、形状过渡或基于路径的动画。作用于 `<path>`、`<polyline>` 与 `<polygon>`；`<circle>`、`<rect>`、`<ellipse>`、`<line>` 会被内部转换，或通过 **MorphSVGPlugin.convertToPath(selector | element)** 转换（用 `<path>` 替换 DOM 中的该元素）。

**morphSVG 值：** 可以是**选择器**（如 `"#lightning"`）、**元素**、**原始路径数据**（如 `"M47.1,0.8 73.3,0.8..."`），对 polygon/polyline 也可以是 **points 字符串**（如 `"240,220 240,70 70,70 70,220"`）。完整配置使用**对象形式**，其中 **shape** 是唯一必需属性。

```javascript
gsap.registerPlugin(MorphSVGPlugin);

// convert primitives to path first if needed:
MorphSVGPlugin.convertToPath("circle, rect, ellipse, line");

gsap.to("#diamond", { duration: 1, morphSVG: "#lightning", ease: "power2.inOut" });
// object form:
gsap.to("#diamond", {
  duration: 1,
  morphSVG: { shape: "#lightning", type: "rotational", shapeIndex: 2 }
});

```

**MorphSVG — 关键配置（morphSVG 对象）：**

| 选项 | 说明 |
|--------|-------------|
| **shape** | _（必需。）_ 目标形状：选择器、元素或原始路径字符串。 |
| **type** | `"linear"`（默认）或 `"rotational"`。rotational 使用角度/长度插值，可避免变形中途出现折痕；当 linear 效果不对时可以尝试。 |
| **map** | 区段的匹配方式：`"size"`（默认）、`"position"` 或 `"complexity"`。当起点/终点区段对不上时使用；若都不行，则拆成多条路径分别变形。 |
| **shapeIndex** | 偏移起点路径中哪个点映射到终点路径的第一个点（避免形状“交叉”或翻转）。单区段路径用数字；多区段用**数组**（如 `[5, 1, -8]`）。负值会反转该区段。先用一次 **shapeIndex: "log"** 在控制台记录自动计算的值，再把数字/数组粘贴进补间。**findShapeIndex(start, end)**（独立工具）提供交互式 UI 帮助找到合适的值。仅适用于闭合路径。 |
| **smooth** | （v3.14+）。添加平滑点。数字（如 `80`）、`"auto"`，或对象：`{ points: 40 \| "auto", redraw: true \| false, persist: true \| false }`。`redraw: false` 保留原始锚点（完全保真，间距较不均匀）。`persist: false` 在补间结束时移除添加的点。当默认变形看起来参差不齐或不自然时使用。 |
| **curveMode** | 布尔值（v3.14+）。对控制柄的角度/长度而非原始 x/y 做插值，以避免曲线上的折痕。当变形中途出现折痕时尝试。 |
| **origin** | **type: "rotational"** 的旋转原点。字符串：`"50% 50%"`（默认），或用 `"20% 60%, 35% 90%"` 为起点/终点指定不同原点。 |
| **precision** | 输出路径数据的小数位数；默认 `2`。 |
| **precompile** | 预计算路径字符串的数组（或先用一次 **precompile: "log"**，再从控制台复制）。跳过开销大的启动计算；用于非常复杂的变形。仅适用于 `<path>`（先转换 polygon/polyline）。 |
| **render** | 每次更新时调用的 Function(rawPath, target) — 例如绘制到 canvas。RawPath 是区段数组（每个区段 = 由交替的 x,y 三次贝塞尔坐标组成的数组）。 |
| **updateTarget** | 使用 **render** 时（如仅 canvas），设置 **updateTarget: false** 以免更新原始 `<path>`。**MorphSVGPlugin.defaultUpdateTarget** 设置默认值。 |

**工具函数：** **MorphSVGPlugin.convertToPath(selector | element)** 将 circle/rect/ellipse/line/polygon/polyline 转换为 DOM 中的 `<path>`。**MorphSVGPlugin.rawPathToString(rawPath)** 与 **stringToRawPath(d)** 在路径字符串与原始数组之间互转。插件会把原始 `d` 存储在目标上（例如用于反向补间：`morphSVG: "#originalId"` 或同一个元素）。

**提示：** 变形出现扭转或翻转时，设置 **shapeIndex**（用 `"log"` 或 findShapeIndex()）。多区段路径的 **shapeIndex** 是数组（每个区段一个值）。仅当第一帧很慢时才使用预编译；它无法解决补间过程中的卡顿（必要时简化 SVG 或减小体积）。

**了解更多：** [MorphSVG](https://gsap.com/docs/v3/Plugins/MorphSVGPlugin)

### MotionPath（MotionPathPlugin）

让元素沿 SVG 路径运动。在让物体沿路径移动（如曲线或自定义路线）时使用。

```javascript
gsap.registerPlugin(MotionPathPlugin);

gsap.to(".dot", {
  duration: 2,
  motionPath: { path: "#path", align: "#path", alignOrigin: [0.5, 0.5] }
});
```

**MotionPath — 关键配置（motionPath 对象）：**

| 选项 | 说明 |
|--------|-------------|
| `path` | SVG path 元素、选择器或路径数据字符串 |
| `align` | 用于对齐目标的路径元素或选择器 |
| `alignOrigin` | `[x, y]` 原点（0–1）；默认 `[0.5, 0.5]` |
| `autoRotate` | 让元素旋转以跟随路径切线 |
| `curviness` | 0–2；路径平滑度 |

### MotionPathHelper

MotionPath 的可视化编辑器（对齐、偏移）。开发期间用于调整路径对齐。

```javascript
gsap.registerPlugin(MotionPathPlugin, MotionPathHelperPlugin);

const helper = MotionPathHelper.create(".dot", "#path", { end: 0.5 });
// adjust in UI, then use helper.path or helper.getProgress() in your animation
```

## 缓动

### CustomEase

自定义缓动曲线（cubic-bezier 或 SVG path）。当内置 ease 不够用时使用。基础用法见 gsap-core；使用时先注册：

```javascript
gsap.registerPlugin(CustomEase);
const ease = CustomEase.create("name", ".17,.67,.83,.67");
gsap.to(".el", { x: 100, ease: ease, duration: 1 });
```

### EasePack

提供更多具名 ease（如 SlowMo、RoughEase、ExpoScaleEase）。注册后在补间中使用这些 ease 名称。

### CustomWiggle

摆动/抖动缓动。当某个值需要“摆动”（多次往复振荡）时使用。

### CustomBounce

可配置强度的弹跳（bounce）风格缓动。

## 物理

### Physics2D（Physics2DPlugin）

2D 物理（速度、角度、重力）。用简单物理效果制作动画时使用（如抛射物、弹跳）。

```javascript
gsap.registerPlugin(Physics2DPlugin);

gsap.to(".ball", {
  duration: 2,
  physics2D: {
    velocity: 250,
    angle: 80,
    gravity: 500
  }
});
```

### PhysicsProps（PhysicsPropsPlugin）

将物理应用于属性值。用于物理驱动的属性动画。

```javascript
gsap.registerPlugin(PhysicsPropsPlugin);

gsap.to(".obj", {
  duration: 2,
  physicsProps: {
    x: { velocity: 100, end: 300 },
    y: { velocity: -50, acceleration: 200 }
  }
});
```

## 开发

### GSDevTools

用于 scrub 时间线（拖动进度）、开关动画与调试的 UI。仅在开发期间使用；不要发布上线。注册后传入时间线引用创建实例。

```javascript
gsap.registerPlugin(GSDevTools);
GSDevTools.create({ animation: tl });
```

## 其他

### Pixi（PixiPlugin）

将 GSAP 与 PixiJS 集成，为 Pixi 显示对象制作动画。用 GSAP 动画化 Pixi 对象时注册。

```javascript
gsap.registerPlugin(PixiPlugin);

const sprite = new PIXI.Sprite(texture);
gsap.to(sprite, { pixi: { x: 200, y: 100, scale: 1.5 }, duration: 1 });
```

## 最佳实践

- ✅ 项目中用到的每个插件都在首次使用前用 **gsap.registerPlugin()** 注册。
- ✅ 布局过渡使用 **Flip.getState()** → DOM 变更 → **Flip.from()**；带惯性的拖拽使用 **Draggable** + **InertiaPlugin**。
- ✅ 组件卸载或元素移除时还原插件实例（如 `SplitTextInstance.revert()`）。

## 禁止事项

- ❌ 在补间或 API 中使用未经注册的插件（应先用 **gsap.registerPlugin()**）。
- ❌ 将 GSDevTools 或仅开发用的插件发布到生产环境。

### 了解更多

https://gsap.com/docs/v3/Plugins/
