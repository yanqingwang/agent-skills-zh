> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/animate/RECIPES.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 动画配方

最常见的场景，拿来即用的实现。从配方起步再做适配，不要从零重建。

曲线指 SKILL.md 里定义的 `--ease-out`、`--ease-in-out`、`--ease-drawer` token。

---

## 按钮按压

任何可按压的元素。即时反馈，让界面"听到"用户的操作。

```css
.button {
  transition: transform 160ms var(--ease-out);
}

.button:active {
  transform: scale(0.97);
}
```

`scale()` 会连同子元素一起缩放：标签和图标跟着变小，这正是它读起来像物理按压的原因。

这里不需要 hover 门控：`:active` 在触屏上就是真实的按压。任何 `:hover` 样式要单独做门控。

---

## 下拉菜单、popover、菜单、select

从触发元素里长出来，而不是凭空出现。

```css
.popover {
  transform-origin: var(--transform-origin); /* Base UI supplies this */
  transition:
    opacity 200ms var(--ease-out),
    transform 200ms var(--ease-out);
}

.popover[data-starting-style],
.popover[data-ending-style] {
  opacity: 0;
  transform: scale(0.95);
}
```

`transform-origin` 是全部重点：面板必须看起来像是从你点击的那个东西里出来的。

---

## tooltip

形态与 popover 相同，更快，外加一个大多数实现都会漏掉的细节。

```css
.tooltip {
  transform-origin: var(--transform-origin);
  transition:
    transform 125ms var(--ease-out),
    opacity 125ms var(--ease-out);
}

.tooltip[data-starting-style],
.tooltip[data-ending-style] {
  opacity: 0;
  transform: scale(0.97);
}

/* Once one tooltip is open, neighbours open instantly */
.tooltip[data-instant] {
  transition-duration: 0ms;
}
```

初始延迟防止误触发。在此之后，同时跳过延迟和动画，会让整条工具栏感觉更快。

---

## modal

唯一保持居中的 popover。

```css
.modal {
  transform-origin: center; /* exempt — not anchored to a trigger */
  transition:
    opacity 250ms var(--ease-out),
    transform 250ms var(--ease-out);
}

.modal[data-starting-style],
.modal[data-ending-style] {
  opacity: 0;
  transform: scale(0.96);
}

.backdrop {
  transition: opacity 250ms var(--ease-out);
}
```

让遮罩层的透明度与它同步动画，两者才读作一个整体表面。

---

## drawer / sheet

```css
.drawer {
  transform: translateY(0);
  transition: transform 500ms var(--ease-drawer);
}

.drawer[data-closed] {
  transform: translateY(100%);
}
```

Vaul 就是先用这个把 drawer 藏起来，再播放入场动画。

再加上拖拽，它就变成手势问题，见下文**拖拽关闭（drag-to-dismiss）**。

---

## toast

```css
.toast {
  opacity: 1;
  transform: translateY(0);
  transition:
    opacity 400ms ease,
    transform 400ms ease;

  @starting-style {
    opacity: 0;
    transform: translateY(100%);
  }
}
```

- 用 `ease` 而不是 `ease-out`，比典型 UI 稍慢：Sonner 读起来优雅，部分原因就是它的动效按组件自身的性格来调，而不是套用通用 UI 的时间预算。
- 如果 `@starting-style` 不可用，退回到挂载标记：

```jsx
useEffect(() => { setMounted(true); }, []);
// <div data-mounted={mounted}>
```

多条 toast 堆叠、列表回流时，透明度变化要和高度变化相互配合。这一对没有公式可套：调到感觉对了为止，第二天再复查一遍。

---

## accordion / collapse

```css
.content {
  overflow: hidden;
  transition:
    height 200ms var(--ease-out),
    opacity 200ms var(--ease-out);
}
```

保持简短：这是少数每一帧都要付出 layout 代价的动画之一，时长一长，又贵又拖沓。在 JS 里测量内容高度（或使用能提供高度的无头组件），不要把动画目标写成 `auto`。

---

## 给一组元素做 stagger（错峰）

适合用户偶尔看到的列表或网格，不适合用户整天滚动划过的列表。

```css
.item {
  opacity: 0;
  transform: translateY(8px);
  animation: fadeIn 300ms var(--ease-out) forwards;
}

.item:nth-child(2) { animation-delay: 50ms; }
.item:nth-child(3) { animation-delay: 100ms; }
.item:nth-child(4) { animation-delay: 150ms; }

@keyframes fadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

stagger 是装饰：播放期间绝不能阻塞交互。

---

## 按住确认（hold-to-confirm）

用于破坏性操作：普通点击太容易误触。

```css
.overlay {
  clip-path: inset(0 100% 0 0);
  transition: clip-path 200ms var(--ease-out); /* release: snappy */
}

.button:active .overlay {
  clip-path: inset(0 0 0 0);
  transition: clip-path 2s linear;             /* press: slow and deliberate */
}

.button:active {
  transform: scale(0.97);
}
```

这里用 `linear` 是对的：填充是进度指示器，而进度不该有缓动。

---

## 带颜色过渡的 tab 指示器

在整条 tab 列表上给每个颜色分别做过渡计时，效果总是不到位。改用裁切。

复制一份 tab 列表。把副本样式化成激活态：不同的背景、不同的文字颜色。对副本做裁切，只露出激活的那个 tab，切换时对裁切区域做动画：

```css
.tabs-active-copy {
  clip-path: inset(0 60% 0 20%); /* driven by the active tab's position */
  transition: clip-path 250ms var(--ease-in-out);
}
```

文字和背景一起变化，完美同步，因为这是同一个元素在被揭示，而不是两种颜色在插值。

---

## 滚动显现（scroll reveal）

只用于营销页面。不要对用户每天使用的功能性 UI 这么做。

```css
.reveal {
  clip-path: inset(0 0 100% 0);
  transition: clip-path 600ms var(--ease-in-out);
}

.reveal[data-visible] {
  clip-path: inset(0 0 0 0);
}
```

用 `IntersectionObserver` 触发，或用 Motion 的 `useInView` 加 `{ once: true, margin: "-100px" }`。只触发一次：每次滚动经过都重新播放动画，等于界面在和读者作对。

---

## 拖拽关闭（drag-to-dismiss）

手势配方。用 spring，不用固定时长，因为用户可以在动作中途反向操作。

```js
// Dismiss on a flick, not just on distance
const timeTaken = Date.now() - dragStartTime.current;
const velocity = Math.abs(swipeAmount) / timeTaken;

if (Math.abs(swipeAmount) >= SWIPE_THRESHOLD || velocity > 0.11) {
  dismiss();
}
```

```js
// Set transform on the dragged element directly.
// Driving it through a CSS variable on the parent recalcs styles for every child.
element.style.transform = `translateY(${distance}px)`;
```

四个细节决定拖拽手感的好坏：

- **指针捕获**：拖拽一开始就捕获指针，这样指针离开元素边界后拖拽仍会继续。
- **多点触控防护**：新触点进来时执行 `if (isDragging) return`，否则拖拽中途换手指会让元素跳变。
- **越界阻尼**：拖过自然边界后，拖得越远位移越小。真实物体停下来之前会先减速。
- **是摩擦力，不是一堵墙**：允许越界拖拽，用递增的阻力应对，而不是直接拒绝。

用 spring 收尾，被中断的拖拽能保留速度：

```js
{ type: "spring", duration: 0.5, bounce: 0.2 }
```

---

## 用遮罩补救收不住的 crossfade

两个状态在过渡期间明显重叠、怎么调 easing 和时长都修不好时，把接缝模糊掉：

```css
.content {
  transition:
    filter 200ms ease,
    opacity 200ms ease;
}

.content.transitioning {
  filter: blur(2px);
  opacity: 0.7;
}
```

不加模糊，眼睛看到的是两个不同的物体在互换。模糊把它们融成一次感知上的变换。模糊值控制在 20px 以内：重度模糊开销很大，Safari 尤其明显。

---

## 不用库的程序化方案

动效需要 JS 控制但不需要引入依赖时，WAAPI 能给你 CSS 级别的性能：

```js
element.animate(
  [{ clipPath: 'inset(0 0 100% 0)' }, { clipPath: 'inset(0 0 0 0)' }],
  { duration: 1000, fill: 'forwards', easing: 'cubic-bezier(0.77, 0, 0.175, 1)' }
);
```

硬件加速、可中断、零打包体积成本。
