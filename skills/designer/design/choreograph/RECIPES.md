> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/choreograph/RECIPES.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 编排配方

[SKILL.md](SKILL.md) 中各种关系的拿来即用模式。这些数值只是起点，请对着录像调到合适为止。

## Overlap：用索引变量做 CSS stagger

用于一次性入场（hero 区、个人网站首页）。每个元素的 delay 由 custom property 计算得出，所以不需要每个条目单独一个类。

```tsx
<div className="stagger">
  <h1 style={{ "--i": 0 }}>Title</h1>
  <p style={{ "--i": 0 }}>First paragraph, same beat as the title</p>
  <p style={{ "--i": 1 }}>Supporting paragraph</p>
  <div style={{ "--i": 2 }}>CTAs</div>
</div>
```

```css
.stagger > * {
  --step: 120ms;
  animation: enter 0.6s ease both;
  animation-delay: calc(var(--step) * var(--i));
}

@keyframes enter {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .stagger > * {
    animation-name: fade;
    animation-delay: 0ms;
  }
  @keyframes fade {
    from { opacity: 0; }
  }
}
```

- 必须用 `both`。`backwards` 让第一帧 keyframe 在 delay 期间就生效，后面的条目才不会在动画开始前闪现最终状态。`forwards` 保留结束状态。
- 省略 `to` 会让 keyframe 动画到元素自身的样式。
- 在父元素上改 custom property 会让每个后代重算样式。一次性入场没问题，但不要在大树上通过继承变量驱动逐帧变化的值（比如拖拽）。

## Overlap：用 Motion variants 做非均匀 stagger

```tsx
import { motion, stagger } from "motion/react";

const list = {
  hidden: {},
  show: {
    transition: {
      // Delays shrink as the group goes on, so it reads as a wave, not a metronome
      delayChildren: stagger(0.06, { ease: "easeOut" }),
    },
  },
};

const lead = {
  hidden: { opacity: 0, y: 12 },
  show: { opacity: 1, y: 0, transition: { duration: 0.5, ease: [0.23, 1, 0.32, 1] } },
};

const support = {
  hidden: { opacity: 0, y: 6 },
  show: { opacity: 1, y: 0, transition: { duration: 0.4, ease: [0.23, 1, 0.32, 1] } },
};

const decoration = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { duration: 0.3 } },
};

<motion.section variants={list} initial="hidden" animate="show">
  <motion.span variants={decoration}>New</motion.span>
  <motion.h1 variants={lead}>Title</motion.h1>
  <motion.p variants={support}>Subtitle</motion.p>
  <motion.div variants={support}>CTAs</motion.div>
</motion.section>
```

- 每个角色有自己的 variant（距离、时长）。stagger 只决定每个角色*何时*开始。
- `stagger(0.05, { from: "center" })` 从中间向外辐射。传入数字索引，就能从用户交互的那个条目向外辐射。
- 旧版 Motion 用 `staggerChildren: 0.06` 代替 `delayChildren: stagger(...)`。
- 长列表里，前 ~6 个之后的条目沿用第 6 个的 delay，整组就不会超过 ~300ms。

## Together：把退场元素从文档流里拿出来

被移除的条目 fade 的*同时*，兄弟元素就在补上空缺，而不是等它结束。

```tsx
<ul>
  <AnimatePresence mode="popLayout" initial={false}>
    {chips.map((chip) => (
      <motion.li
        key={chip.id}
        layout
        exit={{ opacity: 0, scale: 0.95 }}
        transition={{ duration: 0.2, ease: [0.23, 1, 0.32, 1] }}
      >
        {chip.label}
      </motion.li>
    ))}
  </AnimatePresence>
</ul>
```

不用库的做法：执行退场之前，先读出元素的 offset，把它设为 `position: absolute` 并赋上对应的 `top`/`left`（父元素需要 `position: relative`），然后把它动画移出。兄弟元素可以用 FLIP 做动画，或者直接让它们回流。

## Together：在变尺寸的容器里 crossfade 视图

容器的高度与内容切换是同一个整体：相同时长，同一个 easing family。

```tsx
import useMeasure from "react-use-measure";

const [ref, bounds] = useMeasure();
const prevHeight = useRef<number>();

// The fade duration scales with how far the container moves
const fadeDuration = useMemo(() => {
  const MIN = 0.15;
  const MAX = 0.27;
  if (!prevHeight.current) {
    prevHeight.current = bounds.height;
    return MIN;
  }
  const delta = Math.abs(bounds.height - prevHeight.current);
  prevHeight.current = bounds.height;
  return Math.min(Math.max(delta / 500, MIN), MAX);
}, [bounds.height]);

<motion.div
  animate={{ height: bounds.height }}
  transition={{ duration: 0.27, ease: [0.25, 1, 0.5, 1] }}
  style={{ overflow: "hidden" }}
>
  <div ref={ref}>
    <AnimatePresence initial={false} mode="popLayout">
      <motion.div
        key={view}
        initial={{ opacity: 0, scale: 0.96 }}
        animate={{ opacity: 1, scale: 1 }}
        exit={{ opacity: 0, scale: 0.96 }}
        transition={{ duration: fadeDuration, ease: [0.26, 0.08, 0.25, 1] }}
      >
        {content}
      </motion.div>
    </AnimatePresence>
  </div>
</motion.div>
```

- 高度用强的 `ease-out`，内容用同族更轻的曲线，切换既能被看见，又不会失去同步。
- 子元素上的 `key` 是告诉 `AnimatePresence` 有视图离开的依据。退场没播放时，第一个要查的就是缺 `key`。
- 如果容器是更大组件的一部分（比如 drawer），把那个组件自身的打开时长对齐到这里，让整体读作一个实体。

## 感知方向的步进切换

```tsx
const [[step, direction], setStep] = useState([0, 0]);
const go = (d: 1 | -1) => setStep(([s]) => [s + d, d]);

const variants = {
  initial: (d: number) => ({ x: `${110 * d}%`, opacity: 0 }),
  active: { x: "0%", opacity: 1 },
  exit: (d: number) => ({ x: `${-110 * d}%`, opacity: 0 }),
};

<MotionConfig transition={{ type: "spring", duration: 0.5, bounce: 0 }}>
  <AnimatePresence mode="popLayout" initial={false} custom={direction}>
    <motion.div
      key={step}
      custom={direction}
      variants={variants}
      initial="initial"
      animate="active"
      exit="exit"
    >
      {content}
    </motion.div>
  </AnimatePresence>
  <motion.div layout>{/* Back / Continue follow the height change */}</motion.div>
</MotionConfig>
```

`custom` 要同时加在 **`AnimatePresence` 和子元素**两处。退场的子元素从 `AnimatePresence` 读取最新方向。不加的话，它用的是自己挂载时的方向。

小容器或内容相近的视图，把 110% 的滑动换成带 8px 位移和轻微模糊的 crossfade。眼睛几乎不用动，变化照样读得出来。

## Sequence：一笔接一笔

```css
.square {
  animation: draw 0.6s cubic-bezier(0.645, 0.045, 0.355, 1) forwards;
}

.checkmark {
  animation: draw 0.4s cubic-bezier(0.645, 0.045, 0.355, 1) forwards;
  animation-delay: 0.6s; /* = the square's duration */
}

@keyframes draw {
  to { stroke-dashoffset: 0; }
}
```

两条路径都设 `pathLength="100"` 之后，`stroke-dasharray: 100; stroke-dashoffset: 100` 用整数就能把各自藏起来。要让交接读作同一个手势，让对勾在方块结束前一点点启动（比如 0.5s）。

## Sequence：用 crossfade 在两个富状态之间 morph

容器在信息密集的视图之间同时改变宽度和高度时，`mode="wait"` 是稳妥的默认选择。如果仍想用 crossfade：

1. 把激活视图渲染两份。副本 A 只做**入场**动画。副本 B 是 `position: absolute`，常态 `opacity: 0`，只在**退场**时可见：它的退场是一个从 `opacity: 1` 开始淡出的 keyframe。
2. 按容器的去向给退场副本单独的 transform。下一个状态更大就放大，更小就缩小；容器变窄时用 `scaleX` 把它往中心收，免得溢出边缘。
3. 状态不多时，把这些值（以及 spring 的 bounce）按状态对硬编码，通过 `custom` 传入。状态越小，bounce 越多。

## Carry：通过父元素引导 shared layout 动画

你无法自定义 `layoutId` 动画走过的路径，但可以移动它最终落入的容器。

```tsx
<motion.div
  animate={{ y: 73 }}
  transition={{ delay: 0.13, duration: 0.3, ease: [0.23, 1, 0.32, 1] }}
>
  {selected.map((img) => (
    <motion.img key={img.id} layoutId={img.id} src={img.src} />
  ))}
</motion.div>
```

图片在 morph 进垃圾桶*的同时*跟着它一起下落。垃圾桶的正面带 delay 显示，时机对准图片即将落定的瞬间，图片就不会在视觉上穿过它。

## 命令式编排（`useAnimate`）

只有当多个元素要跨多个事件协同、而且你需要 await 完成时才用它。

```tsx
const [scope, animate] = useAnimate();
const running = useRef<ReturnType<typeof animate>[]>([]);
const ready = useRef(false); // a flag that never renders, so no useState

function play(steps: ReturnType<typeof animate>[]) {
  running.current.forEach((a) => a.stop()); // never stack sequences
  running.current = steps;
  return Promise.all(steps);
}

const onEnter = async () => {
  ready.current = false;
  await play([
    animate("[data-animate='icon']", { y: -4 }, { duration: 0.3 }),
    ...[...scope.current.querySelectorAll("[data-animate='line']")].map((el, i) =>
      animate(
        el,
        { strokeDashoffset: [1.05, 0] },
        { duration: 0.5, times: [0.7, 0.9], delay: i === 1 ? 0 : 0.04 },
      ),
    ),
  ]);
  ready.current = true;
};

const onClick = () => {
  if (!ready.current) return;
  // A repeat action skips the buildup: the same proportions, earlier in the timeline
  play([animate("[data-animate='bg']", { scale: [1, 0.96, 1.02, 1] }, { duration: 0.4 })]);
};

const onLeave = async () => {
  await play([/* reset every element */]);
  startIdle(); // only once the reset has finished
};

function startIdle() {
  // Tracked in `running`, so the next onEnter stops the loop
  running.current = [
    animate("[data-animate='icon']", { y: [0, -3, 0] }, {
      delay: 2.5,
      repeat: Infinity,
      repeatDelay: 6,
    }),
  ];
}
```

- 在 `scope` 里用 `data-animate` 选择器定位元素，而不是每个元素存一个 ref。
- 时长不一致时要 await `Promise.all`。只 await 单个动画，只有在所有动画时长相同时才安全。
