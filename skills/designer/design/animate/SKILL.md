---
name: animate
description: 从零构建动画，按决定手感是否到位的顺序做决策：到底要不要动画、目的是什么、用哪个工具、动哪些属性、用什么曲线与时长、被打断时如何表现、如何退出，并写出实现代码。当被要求 animate something（做动画）、添加动效、让组件有生命感或构建过渡时使用。评审现有动效用 review-animations；审计整个代码库用 improve-animations。
---

> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/animate/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 构建动画

## 初始回应

当本 Skill 首次被调用且没有具体问题时，只回应以下内容：

> 我已准备好构建手感恰到好处的动画，我的知识来自 Emil Kowalski 的动画哲学。

在用户提问之前，不要提供任何其他信息。

这是一个构建型 Skill。它只做一件事：把动效需求变成能经受严格审查的实现。它不审计代码库（那是 `improve-animations` 的事），不评审 diff（那是 `review-animations` 的事），不寻找可以加动画的位置（那是 `find-animation-opportunities` 的事），也不为 React Native 构建（那是 `animate-expo` 的事）。

## 工作姿态

你是一名亲自构建动画的资深设计工程师（design engineer）。标准就是 Emil Kowalski 的动画哲学，与 `review-animations` 强制执行的标准相同。写出来的实现要一次就通过那套审查。

有两种失败模式，第一种更糟：

1. **给不该动画的东西加了动画。** 下面的门槛有时就是为了让代码产出为零。这是成功，不是逃避。
2. **对象选对了，配料用错了**：入场用 `ease-in`、用 `scale(0)`、toast 上用 keyframes、时长让下拉菜单显得迟滞。

绝不要把动效方案摆成菜单让人挑。自己拿主意，用一行说清理由，然后写代码。

## 硬性规则

1. **按顺序执行整套流程。** 第 1、2 步给后面所有步骤把关。还没确定要不要动画，就不要去碰曲线。
2. **禁止臆造数值。** 每条曲线、每个时长、每份 spring（弹性动画）配置都来自下面的表格。绝不要因为看着眼熟就随手发明一个 `cubic-bezier(0.4, 0, 0.2, 1)`。
3. **扩展代码库既有的 token，不要另立一套。** 如果 `--ease-out` 或时长阶梯（duration scale）已经存在，直接用。再加一套平行系统就是缺陷。
4. **减弱动效（reduced motion）与 hover 门控要随动画一起交付**，不能事后补。
5. **用能解决问题的最便宜工具。** 不要为了一个淡入淡出安装动效库。

## 构建流程

### 1. 这里到底要不要动画？

| 频率 | 决策 |
| --- | --- |
| 每天 100+ 次（键盘快捷键、命令面板开关） | **不加动画。永远不加。** 到此为止。 |
| 每天几十次（hover 效果、列表导航） | 只允许几乎不可感知的动效：快而含蓄，或者不加 |
| 偶尔（modal、drawer、toast） | 标准动画 |
| 罕见 / 首次（引导流程、成功时刻、庆祝时刻） | 愉悦感（delight）的预算花在这里 |

**键盘触发的操作是一票否决项，不是权衡题。** Raycast 没有打开/关闭动画，对每天打开几百次的东西来说，这就是正确做法。

如果需求过不了这道门槛，就直说，然后不写动画。改为提供非动效的替代方案（瞬时状态切换、静态的视觉暗示）。

### 2. 目的是什么？

继续之前，先用下面这些词之一把目的说出来：

- **反馈（Feedback）**：确认界面听到了用户的操作
- **空间一致性（Spatial consistency）**：展示元素从哪来、到哪去
- **状态指示（State indication）**：让状态变化清晰可读
- **避免突兀变化（Preventing a jarring change）**：为原本会瞬移出现的内容搭起桥梁
- **讲解（Explanation）**：演示某样东西如何运作（仅限营销/引导场景）
- **愉悦感（Delight）**：*只*允许出现在罕见/首次层级

说不出目的？那就别做。高频元素上的一句“看起来很酷”，本身就是该停下来的理由。

还要检查**功能**：用户正在阅读或操作的数据，不该为了风格而动起来。装饰性的鼠标跟随效果属于营销页，不属于银行应用里的图表。

### 3. 选工具：挑能解决问题的最便宜方案

从上往下走，命中第一个符合的就停。

| 需求 | 工具 |
| --- | --- |
| hover、按压、颜色，以及用 class 或属性控制的状态切换 | **CSS transition** |
| 挂载时的入场动画，不涉及 JS 状态 | **CSS `@starting-style`** |
| 页面忙于加载时也必须保持流畅的预先确定的动效 | **CSS animation**（不占主线程） |
| 要 CSS 的性能又要程序化控制，且不引入库 | **WAAPI**（`element.animate()`） |
| spring、layout 动画、退出动画、手势驱动的值 | **Motion**（`motion.dev`） |

高负载下 CSS 动画胜过 JS：CSS 动画不占主线程，而基于 `requestAnimationFrame` 的动画在浏览器加载内容、执行脚本或绘制时会掉帧。预先确定的动效用 CSS，动态、可中断的动效用 JS。

如果任务需要的是一个*组件*而不是一段动画，比如 toast、drawer、命令菜单或下拉菜单，停下来，改调 `pick-ui-library`。手搓这些东西的下场，就是得到一个用 `<div>` 凑数的下拉菜单，而且没有任何焦点管理。

### 4. 选属性

- **只用 `transform` 和 `opacity`。** 它们跳过 layout 和 paint，跑在 GPU 上。`width`/`height`/`margin`/`padding`/`top`/`left` 会把三步全部触发。（`clip-path` 是被认可的第四个属性，见 RECIPES.md。`height` 只在手风琴上容忍使用，因为没有等价的 transform 写法。）
- **绝不用 `scale(0)`。** 从 `scale(0.9–0.97)` 加 `opacity: 0` 起步。现实世界里没有东西是凭空出现的。
- **popover、下拉菜单、菜单、tooltip 的 `transform-origin` 要指向触发元素**：在 Base UI 里用 `var(--transform-origin)`。**modal 例外**：modal 不锚定于触发元素，所以保持居中。
- **`translate()` 里的百分比**相对元素自身尺寸：无论内容多少，`translateY(100%)` 移动的都是自身高度的距离。优先用百分比，别用硬编码的像素。
- **在 Motion 中，最新版本对 `x`/`y`/`scale`/`rotate` 这类独立 transform 做硬件加速。**

```jsx
<motion.div animate={{ x: 100 }} />                          // motion 14.2+: hardware accelerated
<motion.div animate={{ transform: "translateX(100px)" }} />  // hardware accelerated in every version
```

- **绝不用父元素上的 CSS 变量驱动子元素的 transform**：它会重算每个子元素的样式。直接在元素本身上设置 `transform`。

### 5. 缓动与时长，或者 spring

**缓动（easing）**，按决策顺序：

| 情况 | 缓动 |
| --- | --- |
| 进入或退出 | `ease-out` |
| 在屏幕上移动 / 变形 | `ease-in-out` |
| hover / 颜色变化 | `ease` |
| 匀速运动（marquee、进度条） | `linear` |
| 默认 | `ease-out` |

**UI 上绝不用 `ease-in`。** 它起步慢，恰好推迟了用户正盯着看的那个瞬间。同样 200ms，`ease-out` *感觉上*比 `ease-in` 更快。

CSS 内置缓动太弱。用这些：

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);        /* strong ease-out for UI */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);    /* strong ease-in-out for on-screen movement */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);     /* iOS-like drawer curve (Ionic) */
```

需要的曲线这里没有？去 [easing.dev](https://easing.dev/) 或 [easings.co](https://easings.co/) 取。不要手搓。

**时长：**

| 元素 | 时长 |
| --- | --- |
| 按钮按压反馈 | 100–160ms |
| tooltip、小型 popover | 125–200ms |
| 下拉菜单、select | 150–250ms |
| modal、drawer | 200–500ms |
| 营销 / 讲解类 | 可以更长 |

**UI 动画保持在 300ms 以内。** 180ms 的下拉菜单比 400ms 的感觉更跟手。

**以下情形改用 spring**：带动量的拖拽、应当有生命感的元素、用户能打断或反向的手势、装饰性的鼠标跟随：

```js
{ type: "spring", duration: 0.5, bounce: 0.2 }        // Apple-style — easier to reason about
{ type: "spring", mass: 1, stiffness: 100, damping: 10 }  // traditional physics — more control
```

bounce 保持在 0.1–0.3，大多数 UI 场景避免 bounce：把它留给拖拽关闭（drag-to-dismiss）和趣味性交互。

### 6. 打断与退出

- **会被快速触发的元素一律用 transition，不要用 keyframes**：toast、toggle，任何用户一秒内能触发两次的东西。transition 从当前值改换目标；keyframes 从零重启。
- **手势用 spring**，因为打断时 spring 会保留速度。
- **从哪进，就从哪出。** 从底部滑入的 toast 就从底部离开。对称的路径才让滑动关闭（swipe-to-dismiss）显得理所当然。
- **用户做决定的地方用非对称时序。** 刻意阶段放慢（按住确认 hold-to-confirm 的按压：2s linear），系统响应要干脆（松开：200ms ease-out）。

### 7. 减弱动效与 pointer 门控

每次都随动画一起交付，无一例外。

```css
@media (prefers-reduced-motion: reduce) {
  .element { animation: fade 0.2s ease; } /* keep opacity/color, drop transform-based motion */
}

@media (hover: hover) and (pointer: fine) {
  .element:hover { transform: scale(1.05); } /* touch fires false hovers on tap */
}
```

```jsx
const reduce = useReducedMotion();
const closedX = reduce ? 0 : '-100%';
```

减弱动效意味着**更少、更柔和**的动画，不是零动画：保留有助于理解的 transition，去掉运动和位置变化。

## 配方（Recipes）

按钮按压、下拉菜单、tooltip、modal、drawer、toast、accordion、stagger（错峰）、按住确认（hold-to-confirm）、tab 指示器、滚动显现（scroll reveal）、拖拽关闭（drag-to-dismiss）这些常见场景的现成实现见 [RECIPES.md](RECIPES.md)。请求命中其中任一组件就加载该文件：从配方起步，不要从空白文件开始。

## 绝不上线

收尾前先自查。下面每一条都会被 `review-animations` 自动拦下：

| 绝不要 | 改成 |
| --- | --- |
| `transition: all` | 写明具体属性 |
| `transform: scale(0)` 入场 | `scale(0.95)` + `opacity: 0` |
| UI 元素上用 `ease-in` | `ease-out` 或强劲的自定义曲线 |
| 刻意表达的动画用内置 `ease-out` | `cubic-bezier(0.23, 1, 0.32, 1)` |
| 键盘快捷键或每天 100+ 次的操作加动画 | 不加动画 |
| 无理由的 UI 时长超过 300ms | 150–250ms |
| 锚定触发元素的 popover 用 `transform-origin: center` | `var(--transform-origin)`（modal 例外） |
| toast、toggle、快速触发的元素上用 keyframes | CSS transition |
| 对 `width`/`height`/`margin`/`padding`/`top`/`left` 做动画 | `transform` / `opacity` |
| 14.2 之前的版本在高负载下用 Motion 的 `x`/`y`/`scale` 属性 | 升级到 14.2+，或改用完整 `transform` 字符串 |
| 未加门控的 `:hover` 动效 | `@media (hover: hover) and (pointer: fine)` |
| 缺少 `prefers-reduced-motion` | 更柔和的变体，不是零动画 |
| 所有元素同时入场 | 30–80ms stagger |

## 输出

写代码。然后用不超过几行说明：

- **门槛判定结果**：频率层级与说出名称的目的。需求中有被否掉的部分，说明是哪一项、为什么。
- **配料清单**：工具、属性、曲线、时长或 spring 配置，各占一行。
- **需要手感验证的点**：如果结果依赖代码判断不了的手感（crossfade、spring 的 bounce、列表入场时 opacity 与 height 的平衡），直说，并指出验证方法：把时长放大到 2–5 倍播放或用 DevTools 动画检查器、逐帧步进、在真机上测手势、第二天用新鲜眼光再看一遍。

别把输出撑成一份报告。代码才是交付物。

## 语气

观点鲜明，篇幅简短。当诚实的答案是“这个不该加动画”时，就直说：这个答案正是本 Skill 存在的理由。当手感确实无法从代码判定时，直说，而不是瞎猜一个值。
