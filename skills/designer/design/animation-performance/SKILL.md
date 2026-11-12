---
name: animation-performance
description: 让网页动画守住帧预算：只动画 composite 专属属性，页面繁忙时让运动离开主线程，并在动画掉帧时找出原因。涵盖 layout/paint/composite 流水线、更省的属性替换、CSS vs WAAPI vs requestAnimationFrame、Motion 的硬件加速路径、React 每帧重渲染、继承 CSS 变量引发的重算、blur 的开销，以及 `will-change` 何时真正有用。当动画卡顿（janky、choppy、stutters、drops frames）时使用；当挑选要动画的属性时；当出于性能在 CSS 和 JS 动画之间做选择时；或当想上 `will-change` 或 GPU 层时。选 easing、时长或要不要动画，用 animate；整体审查动效，用 review-animations。
---

> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/animation-performance/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 动画性能

## 初始回应

当本 Skill 首次被调用且没有具体问题时，只回应以下内容：

> 我已准备好查明你的动画为什么掉帧并让它恢复流畅，我的知识来自 Emil Kowalski 的设计工程哲学。

在用户提问之前，不要提供任何其他信息。

一个诊断型 Skill。它只做一件事：让运动每一帧都按时落地。它不挑 easing 或时长（那是 `animate` 的事），不判断运动该不该存在（那是 `review-animations` 的事），也不处理 React Native 的线程（那是 `animate-expo` 的事）。这里的问题从来不是"看起来对不对"，而是"每一帧是否按时完成"。

## 为什么这很重要

想象 [Sonner](https://sonner.emilkowal.ski/) 以 30fps 运行。同样的 easing、同样的时长、同样的代码。没人会再在意它。性能不是运动做好之后补上去的一道抛光；它决定了好的运动能不能被感知到。

## 工作姿态

你是一名设计工程师，把 drawer、toast 和 dashboard 发布上线到过真实设备，下面列的每个坑都在生产环境里咬过你。你知道开发者的 MacBook 是这个动画将要运行的所有设备里最不具代表性的一台。

两种失败模式，第一种更糟：

1. **"在我的机器上很流畅。"** 一台快的笔记本几乎能藏住本 Skill 里的所有问题。及格线是一台中端手机；而在 120Hz 屏幕上，预算只有你以为的一半。
2. **撒一把 `will-change` 然后宣称修好。** 这是最后一步，不是第一步。大多数卡顿是属性选错或主线程繁忙，`will-change` 哪个都治不了。

## 硬性规则

1. **默认只动画 `transform` 和 `opacity`。** 其他任何属性都得有理由。如果更便宜的属性能产生相同的视觉效果，就用它，哪怕贵的那个"看起来也没事"。
2. **改代码之前先指明原因。** 你提出的每个修复都要说明它对应下面的哪条原因。"加了 `will-change`，好像顺了一点"不是诊断。
3. **绝不在快机器上得出"没问题"的结论。** 说明哪些结论是从代码验证的，哪些需要在真机上录屏确认。
4. **绝不用 `transition: all`。** 列出确切的属性。`all` 会把接下来任何变化都做成动画，包括没人打算动画的 layout 属性。
5. **不要拿正确性换尽力而为的优化。** 硬件加速是浏览器可能给、也可能不给的东西；动画哪些属性是你能控制的。把精力花在后者。

## 症状表

从这里开始。对上用户看到的现象，再读对应的章节。

| 问题 | 解决方案 |
| --- | --- |
| 动画卡顿 | 动画 `transform`/`opacity`，而不是 `width`/`height`/`top`/`margin` |
| 阴影动画不流畅 | `filter: drop-shadow()` |
| 只在导航或加载时卡顿 | 把动画移到 CSS 或 WAAPI，让它离开主线程 |
| Motion `x`/`y` 掉帧 | 升级到 `motion` 14.2+，或动画完整的 `transform` 字符串 |
| React 里手写的动画掉帧 | 写 `ref.current.style`，而不是 state |
| 列表变长后拖拽越来越卡 | 别再动画继承的 CSS 变量；直接设置 `transform` |
| blur 过渡滞后（Safari 尤其明显） | 动画用的 `blur()` 保持在 20px 以下 |
| 意料之外的属性也被动画了 | 用显式属性替换 `transition: all` |
| 运动开始或结束时元素偏移 1px | `will-change: transform`，只在亲眼见到时才加 |

## 帧预算

60fps 是大脑认作流畅运动的频率，也匹配大多数屏幕的刷新率。它给浏览器每帧 **16.7ms**（1000/60）。在 120Hz 屏幕上（如今的大多数手机和许多笔记本），是 **8ms**。按更小的那个数做设计。

给个尺度感：复杂页面上一次 layout 重算可能超过 100ms。那不是错过一帧，是十几帧。

两件事决定你是否守得住预算：

1. **你动画什么**：每帧的工作量有多大。
2. **它在哪里运行**：这些工作会不会被页面正在做的其他一切阻塞。

## 你动画什么

要呈现一次视觉变化，浏览器最多跑三步：

- **Layout**：计算每个元素的尺寸和位置。
- **Paint**：把页面绘制进各个层。
- **Composite**：把这些层放到屏幕上。

每个属性从三个入口之一进入这条流水线，代价相差一个数量级：

| 层级 | 属性 | 代价 |
| --- | --- | --- |
| 仅 Composite | `transform`、`opacity`，当前的 Chrome/Firefox 里还有 `filter`、`clip-path`、`background-color` | 最便宜。浏览器会把它们提升到自己的层。 |
| Paint + composite | `box-shadow`、`border-radius`、`color` | 不用重新测量，但每帧都要重绘。 |
| Layout + paint + composite | `width`、`height`、`padding`、`margin`、`top`、`left`、`border-width` | 最贵。一个变大的元素能挤动它周围的一切。 |

`transform` 和 `opacity` 改变元素看起来的样子，不改变它在文档流里的位置，所以什么都不用重新测量。composite 层级里的其他属性需要在浏览器和设备之间实测；支持程度参差不齐。

**向下降级替换：**

| 与其用 | 不如动画 |
| --- | --- |
| `width` / `height` / `padding` 来变大变小 | `scale()` |
| `top` / `left` / `margin` 来移动 | `translate()`（百分比相对元素自身尺寸） |
| `display` / `visibility` 切换 | `opacity` |
| `box-shadow` | `filter: drop-shadow(…)` |

最后一个最容易被漏掉。动画化的阴影看起来无害，但每帧都在重绘元素。

由此有两条推论：

- **Layout 动画不一定掉帧。** 绝对定位的元素、或子元素很少的元素，动画 `padding` 可能看不出代价。但 `padding` 动画和 `scale()` 动画看起来一样，而其中只有一个在更慢的设备上不会退化。选没有 downside 的那个。
- **Layout 属性还会带动不该动的东西。** 动画侧边栏的 `margin-left`，旁边的内容每帧都被推挤；`translateX` 不会。对一个挨着展开中侧边栏的 dashboard 来说，那就是整页每秒被重新 layout 60 次。

## 它在哪里运行

**JavaScript 永远跑在主线程上。** 由 `requestAnimationFrame` 驱动的动画要和浏览器正在做的其他一切抢时间。主线程一忙，动画代码就跑不了，帧就迟了。

| 驱动方式 | 线程 |
| --- | --- |
| JS + `requestAnimationFrame`（GSAP、Motion 的 layout 动画） | 永远是主线程 |
| Web Animations API（`element.animate()`、Motion 的 `animate()` 和 `motion/react` 组件） | 可硬件加速 |
| CSS transition 和 keyframes | 可硬件加速 |

硬件加速意味着动画不在主线程上跑，所以无论 JavaScript 在忙什么它都保持流畅。"JS"和"主线程"不是同义词：把工作交给 WAAPI 的 JS 库可以被加速，rAF 循环不行。

能稳定加速的：`transform` 和 `opacity`。支持正在扩大：`filter`、`clip-path`、`background-color`。

**要盯住的模式是：页面正在干重活时还在跑的运动**：页面过渡、导航期间的 tab 指示器、任何和数据请求或 hydration 同时触发的东西。Vercel 的 dashboard 用 Framer Motion 的 shared layout 动画做激活 tab 的指示器。浏览器恰好在同一时刻加载下一页，于是掉帧。把它改成 CSS 动画后就修好了。

Motion 把 `opacity`、`transform`、`clip-path` 和 `filter` 交给 WAAPI，所以它们可以被加速。`x`、`y`、`scale`、`rotate` 这些简写取决于版本：

```jsx
<motion.div animate={{ x: 100 }} />                          // motion 14.2+: hardware-accelerated. Before: main thread, can jank
<motion.div animate={{ transform: "translateX(100px)" }} />  // hardware-accelerated in every version
```

从 `motion` 14.2 起，HTML 元素上的简写会被合并成一个加速的 `transform` 动画，所以可以继续用简写。旧版本上，如果动画必须在繁忙的主线程下也能存活，就换成字符串形式。任何版本里，这些都留在主线程上：layout 动画（`layout`、`layoutId`）、`onUpdate`、`transformTemplate`、inertia，以及每帧都由 motion value 驱动的值（drag、`useTransform`）。

**加速是渐进增强。** 浏览器会在某些条件下静默拒绝加速，而这些条件随版本变化；例如 Chrome 历史上不加速基于百分比的 transform。这构不成放弃 `translateY(100%)` 的理由。对尺寸未知的元素，百分比是正确做法（Sonner 和 Vaul 就是这样给 toast 和 drawer 定位的），正确性胜过尽力而为的优化。

## React：不要通过 state 做动画

动画库在 React 渲染周期之外做动画，所以没问题。陷阱是每帧调用 `setState` 的手写动画：组件每 16.7ms 重渲染一次，光是渲染就把预算烧穿了。

```jsx
// Drops frames: one re-render per frame
setY(nextY);

// Smooth: no re-render
ref.current.style.transform = `translateY(${nextY}px)`;
// or with a motion value: y.set(nextY)
```

在 `requestAnimationFrame`、`pointermove`、`scroll` 或拖拽 handler 里找 state 更新。

## 两个看起来没问题的陷阱

下面两个用的都是 `transform`，照样掉帧。

**继承的 CSS 变量。** Vaul 的拖拽在 drawer 装到 ~20 个条目以上后就开始变卡，全程没有重渲染。拖拽距离被写进了一个 `translateY()` 读取的 CSS 变量：

```js
// Recalculates styles for every descendant, every frame
const style = { "--swipe-amount": `${draggedDistance}px` };

// Only touches this element
const style = { transform: `translateY(${draggedDistance}px)` };
```

CSS 变量会继承，所以在父元素上改一个，会触发每个子元素的样式重算。内容越多，每帧越慢。只要一个 `transform` 动画随内容增长而变差，就先怀疑这个。

**Blur。** `filter: blur()` 的开销涨得很快，Safari 尤其明显。动画里的 blur 保持在 20px 以下；2–5px 就足以柔化 crossfade。

## `will-change`

浏览器可能在动画进行到一半时把它从 CPU 移交给 GPU，这个移交会让元素在开始或结束时偏移一个像素。`will-change` 提前完成提升，移交就不会发生：

```css
.drawer {
  will-change: transform;
}
```

**只在亲眼看到偏移、或实测到掉帧之后才加。** 浏览器本来就会提升动画 `transform` 或 `opacity` 的元素，所以在常见路径上它什么都不做，而每一个被提升的层都要占 GPU 内存。把它加在做动画的那个元素上，绝不加在 `*` 或大容器上。

它真正物有所值的场景是昂贵的 paint，比如大面积模糊或带滤镜的元素。提升它，并让层保持小；小层的合成代价比全屏层低。

## 该避开 JS 动画吗？

不需要。主线程动画只在动画期间页面恰好繁忙时受影响，这很少见，而且你现在知道怎么识别它了。

Framer Motion 能给你 CSS 给不了的东西：真正的 spring、shared layout 动画、已卸载组件的退场动画、带动量的手势。问题是你需不需要这些，而不是 JS 动画可不可以。

**可行的分工：** 简单运动、以及页面繁忙时播放的一切，用 CSS；复杂、可中断、手势驱动的运动，用 Framer Motion。

## 工作流

### 阶段 1：找出什么在做动画

列出范围内的每个动画，以及它的驱动方式和属性：

| 元素 | 驱动方式 | 属性 | 播放时机 |
| --- | --- | --- | --- |
| Tab 指示器 | `motion/react` `layoutId` | layout | 路由切换 |
| Drawer | CSS transition | `transform` | 用户拖拽 |
| 卡片 hover | CSS transition | `all` | hover |

把 `transition: all` 和 Motion 简写展开，看清它们实际动画的是什么。

### 阶段 2：诊断

顺着这份清单往下查。排序依据是每条原因出现的频率：

1. **动画的是哪些属性？** `transform`/`opacity` 之外的任何属性都是头号嫌疑：layout 属性排第一，然后是 `box-shadow` 和 `border-radius`，它们看着不像 layout，容易漏掉。
2. **卡顿是否和页面繁忙同时发生？** 导航、请求、hydration、长任务。把动画移到 CSS 或 WAAPI。
3. **React 是否每帧重渲染？** rAF、pointer 或 scroll handler 里的 state 更新。
4. **内容增多时是否变差？** 继承的 CSS 变量，或同时动画的节点太多。
5. **是否有 CSS 变量在被动画？** 或者 14.2 之前版本的 Motion `x`/`y`/`scale`？
6. **有没有超过 20px 的 `blur()` 在被动画？**
7. **还在偏移或顿挫？** 这时才给做动画的元素加 `will-change: transform`。

用录屏确认，不要凭感觉：DevTools 的 Performance 面板看掉帧和长任务，Animations 面板把运动放慢。通过远程调试在真实的中端手机上做 profile。桌面上的 CPU throttling 模拟的是慢 CPU，不是弱 GPU，也不是小内存预算。

### 阶段 3：报告

每条发现按这个格式：

```
**[Element]**: `file.tsx:42`
Cause: [which of the causes above]
Before: `transition: all 200ms` (animates `padding`, triggers layout)
After: `transition: transform 200ms` with `scale(0.97)`
Verified: from code / needs a device recording
```

发现按代价排序：layout 排在 paint 前面，繁忙主线程排在空闲前面。然后停手。被要求时才动手修。
