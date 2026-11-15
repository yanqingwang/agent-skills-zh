> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/review-animations/STANDARDS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 动效标准参考（Animation Standards Reference）

评审背后的精确数值、曲线与规则。写审查结论时直接引用这些值，不要凭感觉给约数。蒸馏自 Emil Kowalski 的设计工程哲学。

## 该不该动？（频率表）

| 使用频率 | 决定 |
| --- | --- |
| 每天 100+ 次（快捷键、命令面板开关） | 不加动画。永远不加。 |
| 每天数十次（hover 效果、列表导航） | 移除或大幅缩减 |
| 偶尔一次（模态框、抽屉、toast） | 标准动画 |
| 罕见 / 首次（引导、反馈、庆祝） | 可以加点愉悦感 |

**绝不动键盘触发的操作**：它们每天重复数百次；动画让人觉得又慢又脱节。（Raycast 没有开合动画，对每天用几百次的东西来说这是正确选择。）

动效的正当目的：空间一致性、状态指示、解释、反馈、避免生硬突变。高频出现的元素上拿"看起来很酷"当理由，不成立。

## 缓动（Easing）

判定顺序：
- 进场或出场 → **`ease-out`**（起步快，感觉响应迅速）
- 屏幕内移动 / 形变 → **`ease-in-out`**
- hover / 颜色变化 → **`ease`**
- 匀速运动（跑马灯、进度）→ **`linear`**
- 默认 → **`ease-out`**

**UI 上绝不用 `ease-in`。** 它起步慢，恰好拖慢用户盯着看的那一刻。同样 200ms，`ease-out` *感觉*比 `ease-in` 快。

CSS 内置缓动太弱。用更强的自定义曲线：

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);        /* strong ease-out for UI */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);    /* strong ease-in-out for on-screen movement */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);     /* iOS-like drawer curve (Ionic) */
```

曲线可到 [easing.dev](https://easing.dev/) 或 [easings.co](https://easings.co/) 找，不要从零手搓。

## 时长（Duration）

| 元素 | 时长 |
| --- | --- |
| 按钮按压反馈 | 100–160ms |
| Tooltip、小型 popover | 125–200ms |
| 下拉菜单、select | 150–250ms |
| 模态框、抽屉 | 200–500ms |
| 营销 / 讲解类 | 可以更长 |

**规则：UI 动画控制在 300ms 以内。** 180ms 的下拉比 400ms 的更有响应感。更快的 spinner 让加载显得更快（实际时间相同）。第一个 tooltip 之后的都即时出现（跳过延迟加动画），工具栏就显得更快。

## 物理感（Physicality）

- **绝不用 `scale(0)`。** 从 `scale(0.9–0.97)` 加 `opacity: 0` 起步。现实世界没有东西是无中生有的。
- **popover 要感知出发点。** 从触发元素缩放，而不是从中心：
  ```css
  .popover { transform-origin: var(--transform-origin); } /* Base UI */
  ```
  **模态框例外**，它在视口居中出现，保持 `transform-origin: center`。
- **按钮按压反馈。** `:active` 时 `transform: scale(0.97)`，配 `transition: transform 160ms ease-out`。幅度要小（0.95–0.98）。适用于任何可按压元素。

## 弹簧（Springs）

弹簧之所以自然，是因为它模拟物理；没有固定时长，按参数收敛。用于：带动量的拖拽、"有生命"的元素（灵动岛）、可中断手势、装饰性鼠标跟随。

```js
// Apple-style (easier to reason about) — recommended
{ type: "spring", duration: 0.5, bounce: 0.2 }

// Traditional physics (more control)
{ type: "spring", mass: 1, stiffness: 100, damping: 10 }
```

bounce 保持克制（0.1–0.3）；多数 UI 避免弹跳，留给拖拽关闭和趣味交互。弹簧被打断时保留速度（keyframes 会从零重跑），因此适合用户可能在半途反悔的手势。

鼠标交互：用 `useSpring` 插值，别把值直接绑到鼠标位置（直连显得生硬、没有惯性）。只在动效属于装饰时这么做。

## 可中断性（Interruptibility）

CSS **transition** 可以在动画中途被打断并改道；**keyframes** 会从零重跑。频繁触发的东西（不断加入的 toast、开关切换）用 transition 更顺滑。

```css
/* Interruptible — good for dynamic UI */
.toast { transition: transform 400ms ease; }

/* Not interruptible — avoid for dynamic UI */
@keyframes slideIn { from { transform: translateY(100%); } to { transform: translateY(0); } }
```

用 `@starting-style` 实现免 JS 的进场：

```css
.toast {
  opacity: 1; transform: translateY(0);
  transition: opacity 400ms ease, transform 400ms ease;
  @starting-style { opacity: 0; transform: translateY(100%); }
}
```

旧式兜底：`useEffect(() => setMounted(true), [])` 加 `data-mounted` 属性。

## 非对称时长（Asymmetric timing）

用户做决定的地方放慢，系统响应的地方加快。

```css
.overlay { transition: clip-path 200ms ease-out; }            /* release: fast */
.button:active .overlay { transition: clip-path 2s linear; }  /* press: slow, deliberate */
```

## 性能（Performance）

- **只动 `transform` 和 `opacity`**，它们跳过布局/绘制、跑在 GPU 上。`padding`/`margin`/`height`/`width`/`top`/`left` 会触发全部三个渲染阶段。
- **不要通过父元素上的 CSS 变量驱动子元素的 transform**，那会触发所有子元素重算样式。把 `transform` 直接设在元素上。
  ```js
  element.style.setProperty('--swipe-amount', `${d}px`); // bad: recalc on all children
  element.style.transform = `translateY(${d}px)`;        // good: only this element
  ```
- **`motion` 从 14.2 起对简写属性做硬件加速。** 14.2 之前，`x`/`y`/`scale` 经 rAF 跑在主线程上，负载一高就掉帧，所以在这些版本要么升级，要么用完整的 transform 字符串。布局动画（`layout`、`layoutId`）在任何版本都跑在主线程：
  ```jsx
  <motion.div animate={{ x: 100 }} />                          // motion 14.2+: hardware accelerated
  <motion.div animate={{ transform: "translateX(100px)" }} />  // hardware accelerated in every version
  ```
- **高负载下 CSS 动画胜过 JS**，它们跑在主线程之外；基于 rAF 的动画在浏览器加载/执行脚本/绘制时会卡顿。预定动作交给 CSS，动态 / 可中断的交给 JS。
- **WAAPI** 用 CSS 的性能拿到 JS 的控制权（硬件加速、可中断、无需库）：
  ```js
  element.animate([{ clipPath: 'inset(0 0 100% 0)' }, { clipPath: 'inset(0 0 0 0)' }],
    { duration: 1000, fill: 'forwards', easing: 'cubic-bezier(0.77, 0, 0.175, 1)' });
  ```

## 变换与 clip-path（Transforms & clip-path）

- **`translate` 的百分比**相对元素自身尺寸，`translateY(100%)` 移动的距离就是元素高度，与具体尺寸无关（Sonner/Vaul 定位 toast/抽屉的方式）。优先于硬编码的 px。
- **`scale()` 会连带缩放子元素**（字体、图标、内容），按压反馈正可利用这一点。
- **3D**：`rotateX/Y` 加 `transform-style: preserve-3d`，不用 JS 就能做纵深 / 环绕 / 翻转。
- **`clip-path: inset(t r b l)`** 是很强的动画工具：每个值从对应方向往里吃。用途：滚动显现（`inset(0 0 100% 0)` → `inset(0 0 0 0)`）、长按删除遮罩、无缝的标签页颜色过渡（复制一份再裁切活动副本）、对比滑块。

## 手势与拖拽（Gestures & drag）

- **带惯性的关闭**：不要求越过距离阈值，算速度（`Math.abs(distance)/elapsedMs`），大于约 `0.11` 就关。轻扫一下就该够。
- **边界阻尼**：越过自然边界后，拖得越远位移越小（真实物体停下前会减速）。
- **指针捕获**：拖拽一开始就 capture，指针出了边界也继续。
- **多点触控防护**：拖拽开始后忽略多余的触点（`if (isDragging) return`），防止跳变。
- **要摩擦，不要硬停**：允许越界拖拽、阻力递增，而不是一堵看不见的墙。

## 遮掩不完美的交叉淡入（Masking imperfect crossfades）

调过缓动和时长后交叉淡入仍出现两个叠影状态时，在过渡期间加轻微的 `filter: blur(2px)`，把两者融成一次可感知的变化。blur 保持小于 20px（重模糊代价高，Safari 尤甚）。

## 错峰（Stagger）

成组进场用错峰，项与项之间 30–80ms。再长的延迟就显得慢了。错峰属于装饰，播放期间绝不阻塞交互。

```css
.item { opacity: 0; transform: translateY(8px); animation: fadeIn 300ms ease-out forwards; }
.item:nth-child(2) { animation-delay: 50ms; }
.item:nth-child(3) { animation-delay: 100ms; }
@keyframes fadeIn { to { opacity: 1; transform: translateY(0); } }
```

## 无障碍（Accessibility）

```css
@media (prefers-reduced-motion: reduce) {
  .element { animation: fade 0.2s ease; } /* keep opacity/color, drop transform-based motion */
}
@media (hover: hover) and (pointer: fine) {
  .element:hover { transform: scale(1.05); } /* gate hover motion — touch fires false hovers on tap */
}
```

```jsx
const reduce = useReducedMotion();
const closedX = reduce ? 0 : '-100%';
```

减少动效意味着更少、更温和的动画，而不是零：保留有助于理解的过渡，去掉位移 / 位置变化。

## 调试（手感拿不准时，在评审中推荐）

- **慢放**：时长放大 2–5 倍，或用 DevTools 的动画检查器。检查颜色交叉淡入是否干净、缓动是否戛然而止、`transform-origin` 是否正确、联动的属性是否同步。
- **逐帧**：Chrome DevTools 的 Animations 面板能看出联动属性之间的时序漂移。
- **真机**测手势（抽屉、滑动）：连上手机、用 IP 访问 dev server、用 Safari 远程调试。
- **隔天再看**，开发时看不见的瑕疵之后会浮出来。

## 一致性（Cohesion）

动效要匹配组件的性格：俏皮的可以更弹；专业的仪表盘就该利落、快。Sonner 觉得对味，部分原因在于缓动、时长、设计乃至名字都是和谐的：略微放慢、用 `ease` 而不是 `ease-out`，显得优雅。进出场列表里 opacity 加 height 靠试错，没有公式，调到手感对为止。
