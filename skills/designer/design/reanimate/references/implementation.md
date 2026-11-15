> **中文汉化版** · 上游：[NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate) · 原文件：`skills/designer/design/reanimate/references/implementation.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 在用户的技术栈里实现动效

对齐项目已经在用的东西。给一个用 CSS 做动画的项目塞 GSAP，或给 Vue 应用塞 Framer Motion，都是用户没要求过的改动。什么都没有时的优先顺序：CSS（keyframes/transitions，支持时用 scroll-driven animations）→ Web Animations API → 框架自带的动效库（React 用 Framer Motion/`motion`，Vue 用 `@vueuse/motion` 或 GSAP，Svelte transitions）→ 依赖很多的时间线用 GSAP。

## 缓动对照

| 参考 | CSS | Framer Motion / motion | GSAP |
|---|---|---|---|
| easeOutExpo `cubic-bezier(0.16,1,0.3,1)` | same | `ease: [0.16, 1, 0.3, 1]` | `"expo.out"` |
| easeOutQuint `cubic-bezier(0.22,1,0.36,1)` | same | `[0.22, 1, 0.36, 1]` | `"quint.out"` |
| easeOutCubic `cubic-bezier(0.33,1,0.68,1)` | same | `[0.33, 1, 0.68, 1]` 或 `"easeOut"` | `"power2.out"` |
| easeInOutCubic `cubic-bezier(0.65,0,0.35,1)` | same | `[0.65, 0, 0.35, 1]` | `"power2.inOut"` |
| material standard `cubic-bezier(0.4,0,0.2,1)` | same | `[0.4, 0, 0.2, 1]` | `"power1.inOut"` ≈ |
| easeOutBack `cubic-bezier(0.34,1.56,0.64,1)` | same | `[0.34, 1.56, 0.64, 1]` | `"back.out(1.7)"` |
| spring，过冲约 10 %，约 600 ms 稳定 | `linear(...)` 采样曲线，或带采样关键帧的 WAAPI | `type: "spring", stiffness: 300, damping: 20`（阻尼越小过冲越大；刚度越低越慢） | `"elastic.out(1, 0.5)"` 或 `gsap` + physics plugin |
| linear | `linear` | `"linear"` | `"none"` |

按测量值调弹簧：过冲 ≈ `exp(−π ζ / sqrt(1 − ζ²))`，其中 `ζ = damping / (2·sqrt(stiffness·mass))`。10 % 过冲 → ζ ≈ 0.59；5 % → 0.69；20 % → 0.46。稳定时间 ≈ `4 / (ζ·ω)`，`ω = sqrt(stiffness/mass)`。从 `mass: 1` 起步，按过冲定 ζ，再按稳定时间定刚度，最后用 `easing.ts` 验证。

## 模式

**Fade-up stagger（CSS）**
```css
.item { opacity: 0; transform: translateY(32px); animation: up 700ms cubic-bezier(.16,1,.3,1) forwards; animation-delay: calc(var(--i) * 90ms + 200ms); }
@keyframes up { to { opacity: 1; transform: none; } }
```
给每个子元素设 `--i`（`style="--i: 2"`），或写 `:nth-child` 规则。保留 `forwards`，让结束状态保持住。

**Framer Motion stagger**
```tsx
const parent = { hidden: {}, show: { transition: { staggerChildren: 0.09, delayChildren: 0.2 } } };
const child = { hidden: { opacity: 0, y: 32 }, show: { opacity: 1, y: 0, transition: { duration: 0.7, ease: [0.16, 1, 0.3, 1] } } };
<motion.ul variants={parent} initial="hidden" animate="show">{items.map(i => <motion.li key={i} variants={child} />)}</motion.ul>
```

**进入视口触发**：Framer 用 `whileInView` + `viewport={{ once: true, amount: 0.25 }}`；原生 JS 用 `IntersectionObserver`，`threshold` 设成参考开始运动时可见的比例（读 `track.json`：第一个运动采样处元素的 `y` 除以视口高度）。CSS scroll-driven：支持时用 `animation-timeline: view(); animation-range: entry 0% entry 40%`。

**Scroll-linked**：带 `animation-range` 的 CSS `animation-timeline: scroll()`、GSAP ScrollTrigger `scrub: true`，或 Framer `useScroll` + `useTransform([0, 600], [0, -120])`。映射是 scroll px → value，两个端点从 track 里取。

**按行/词做 text reveal**：拆成 span，每行套一个 `overflow: hidden` 包裹层，动 `translateY(110%) → 0`。保持无障碍文本完整（容器上 `aria-label`，span 上 `aria-hidden`）。

**Hover lift**：卡片上 `transition: transform 220ms cubic-bezier(.2,.8,.2,1), box-shadow 220ms`；动 `transform`，不要动 `top`。反向常用同样的时序；也要核对参考的 hover-out 帧。

**Marquee**：把内容复制一份，`animation: scroll Ns linear infinite`，从 `translateX(0)` 到 `translateX(-50%)`。`N` 是量出来的周期。只有参考才 hover 暂停。

**Clip/mask reveal**：`clip-path: inset(0 100% 0 0)` → `inset(0 0 0 0)`，或用带动态渐变位置的 `mask-image`。

**循环和空闲**：脉冲用 `animation-iteration-count: infinite; animation-direction: alternate`；从活动曲线量出一个周期。

**Canvas、WebGL、3D**：从 trace 重建，不要从像素重建（`references/webgl.md › Building`）。用同样的引擎和版本、renderer 设置和 context 属性，移植用户写的着色器连同其固定 uniform，把 trace 到的 blend 状态映射到材质，再按每个通道显示的时序和缓动驱动各自的动态 uniform。逐帧滞后 `x += (target − x) · k` 想保持与帧率无关，写成 `x += (target − x) · (1 − (1 − k) ** (dt / 16.67))`。

## 决定匹配成败的细节

- `transform-origin`：scale-in 从锚点长大（菜单从按钮角，弹窗从中心）。若 `inspect.json` 里 `nodes › transform-origin` 不是默认值，照它读。
- 在参考做了合成的元素上加 `will-change: transform` 或 `translateZ(0)`，避免对比视频里出现卡顿。
- `overflow: hidden` 包裹层决定滑动元素被裁掉还是露出盒子外；照抄。
- transform 顺序：`translate() scale()` ≠ `scale() translate()`。技术栈允许时用独立属性（`translate`、`scale`、`rotate`）。
- 填充模式和初始状态：在 CSS 里渲染运动前状态（opacity 0 等），让第一帧就匹配；别让 JS 执行前闪一下最终状态。
- `prefers-reduced-motion`：把非必要动效包进 `@media (prefers-reduced-motion: no-preference)` 或 Framer `useReducedMotion()`；参考忽略它时，除非用户说不要，仍要加上并说明。
- 字体（pixel-faithful）：抓克隆前先加载 `inspect.json › fonts` 列出的同一字族和字重（`document.fonts.ready`），否则每一帧都对不上。
