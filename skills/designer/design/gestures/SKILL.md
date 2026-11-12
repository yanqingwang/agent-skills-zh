---
name: gestures
description: 构建能 1:1 跟随手指、始终可中断的拖拽、滑动和 sheet 交互。适用于构建或修复用户用手势拖动、滑动、甩动、长按或关闭的任何东西：drawer、sheet、滑动关闭的 toast 和卡片、拖拽排序、下拉刷新、长按确认；也适用于手势显得迟滞、与手指脱节、松手时跳变、或动画中途抓不住的情况。触发词：gesture、drag、draggable、swipe、swipe to dismiss、fling、momentum、velocity、drawer、sheet、bottom sheet、snap points、Vaul、dragConstraints、dragElastic、dragMomentum、onDragEnd、whileDrag、useMotionValue、rubber-band、overscroll、pull to refresh、hold to delete、press and hold、touch-action、dismiss threshold、"doesn't follow my finger"、"jumps when I let go"、"can't grab it mid-animation"。
---

> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/gestures/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 手势驱动的 UI

如何构建有物理感的手势。手势就是直接操纵：手指按下的期间，UI 就是手指；抬起的瞬间，物理接管。下面每条规则都源自这个分界。

## 第一个决定：自己写，还是用现成方案？

把 drawer 手势做*对*，意味着基于动量的拖拽、与拖拽进度联动的 overlay opacity、感知速度的关闭判定、焦点陷阱、Esc 关闭。这是以周计的边界情况，不是一个下午。**底部 sheet / drawer 默认用 [Vaul](https://vaul.emilkowal.ski/)**：它存在的理由正是这事很难手搓。只有当没有库覆盖该交互时（自定义滑动卡片、定制的拖拽交互）才自己写。拿不准就用 `pick-ui-library` 这个 Skill。

## 每个手势的两个阶段

你构建的任何手势都要走过这个分叉。混淆两个阶段是手势手感不对的头号原因。

```
指针当前是否按下？
├── 是 → 跟随（TRACK）阶段：位置 1:1 映射到指针。
│         无缓动。无时长。无 spring。元素就是手指。
└── 否 → 释放（RELEASE）阶段：物理完成剩余运动。
          用释放速度作初速的 spring。绝不用 keyframe。
```

### 跟随阶段规则

- **1:1 就是 1:1。** 位置由 `useMotionValue`（或直接写 `transform`）驱动，绝不用 spring 或 transition：跟随期间用 spring 会让元素拖在手指后面、感觉脱节，像在糖浆里拖东西。
- **在被拖元素上直接写 `transform`。** 绝不在父元素上更新 CSS 变量来移动子元素：CSS 变量可继承，每次变更都会重算所有后代的样式。正是这个 bug 让 Vaul 的拖拽在超过约 20 个列表项后变卡；把 `transform` 写到元素上才修好。
- **每个 move 事件不要走 React state。** 每次 pointermove 都重渲染会掉帧。Motion value 和直接写样式绕开渲染周期。
- **边界处橡皮筋。** 拖过边界时，元素应只移动一小部分距离（Motion：`dragElastic` ≈ 0.2），而不是戛然而止：硬停像撞墙；阻尼用物理方式传达"再往外就没有了"。

### 释放阶段规则

- **用 spring 收尾，并以手势速度作初速。** 元素应以它正在移动的速度离开手指。这里用固定时长的 ease 会让每次甩动都以同样的方式落定，看起来是假的。
- **距离或速度任一达标即关闭。** 距离超过阈值（约行程的 40–50%）就关闭，短距离的快速轻扫同样应关闭。在 Motion 里，两者都从 `onDragEnd` 的 `info.offset` 和 `info.velocity` 读取。只看距离的阈值会让轻扫感觉被无视。
- **bounce 只属于拖拽的结尾。** 拖拽施加了力（如同把球扔向墙），所以松手时轻微回弹才显得物理。同一个元素改由按钮关闭就应是**零** bounce：没有力被施加。数值保持小，并记住 bounce 与元素尺寸成反比（元素越小，需要越大的 bounce 才能传达同等感觉）。
- **弹回要快。** 手势没过阈值时，用 spring 快速弹回：慢吞吞的弹回像是 UI 在用慢动作反驳用户。

## 可中断性不容妥协

用户必须能在 sheet 关闭到一半时抓住它拖回去。Spring 做得到：中途改换目标时保留当前速度，转向无缝。CSS `@keyframes` 从零重启、无法中途接住：这正是 Sonner 早期的 CSS 入场动画在第二个 toast 到达时让 toast 跳变的原因。**凡是手势可能触碰的东西，绝不用 keyframe 动画。** 只用 CSS transition 和 spring。

## 联动值

被拖元素很少单独存在：overlay 在淡出，背后的页面在缩放。从拖拽进度派生它们，不要各自单独做动画：

```jsx
const y = useMotionValue(0);
const overlayOpacity = useTransform(y, [0, drawerHeight], [1, 0]);
```

单一数据源意味着 overlay 的淡出程度永远精确对应 drawer 的关闭进度：手势进行中如此，用户反向拖时也如此。两个独立动画在手势被打断的那一刻就会各走各的。

## Motion 拖拽属性

```jsx
<motion.div
  drag="y"
  dragConstraints={{ top: 0 }}
  dragElastic={0.2}
  onDragEnd={(e, info) => {
    if (info.offset.y > threshold || info.velocity.y > 500) dismiss();
  }}
/>
```

`dragMomentum` 默认开启：对被甩出的卡片是对的，对简单的挪位是错的；当元素应该停在手指停下的位置时，把它关掉。`dragConstraints` 接收 ref 或边界对象。

## 不用 spring 的 sheet：Vaul 曲线

Vaul 用纯 CSS 模仿 iOS sheet 以保持轻量：`cubic-bezier(0.32, 0.72, 0, 1)`，时长 **500ms**。这条曲线起步极其陡峭：正因如此，500ms 的时长依然显得利索，落定时又带着 spring 般的柔和。由此得到两条规则：

- **小型悬浮 drawer**（不贴屏幕边缘）应覆写为约 200ms：500ms 的 iOS 时序只有在全宽、贴边的 sheet 上才显得对：
  ```css
  [vaul-drawer]  { transition: transform 0.2s cubic-bezier(0.165, 0.84, 0.44, 1); }
  [vaul-overlay] { transition: opacity  0.2s cubic-bezier(0.165, 0.84, 0.44, 1); }
  ```
- **组件必须感觉像一个整体。** 如果 drawer 200ms 打开，其高度变化和内容 crossfade 必须属于同一时序家族：一个慢半拍的子动画会让整体感觉是散的。

给交互式子元素标上 `data-vaul-no-drag`，这样按 drawer 内的按钮不会触发拖拽。

## 空间一致性

**元素沿进入的方向退出。** Sonner 的 toast 从底部滑入，所以向下滑动即可关闭：进与出共用一根轴，这正是手势无需教学就显得可发现、符合直觉的原因。沿元素从未移动过的轴去关闭的手势必须学习才会用；反转入场方向的手势则是*被直接感知*的。

## 长按手势是非对称的

长按删除等按住类交互在按住期间用 **`linear`**：动画在可视化时间的流逝，而时间线性流逝；任何其他曲线都在谎报剩余时长。完成前松手时，用 `ease-out` 快速弹回。刻意的阶段缓慢而诚实；取消是瞬间的。这里的对称时序是 bug。

## 触屏检查清单

你交付的每个手势都过一遍这份清单：

- **在真机上测试**：通过本地 IP 访问开发服务器。触控板模拟在触控上会骗人，60Hz 桌面显示器会掩盖 120Hz 手机上看得见的 opacity 过渡毛糙感。
- **点击目标 ≥ 44×44px。** 用不可见的 `::before` 热区放大小的视觉目标，而不是撑大布局。
- **在拖拽轴上设置 `touch-action`**（垂直拖拽用 `touch-action: pan-x` 等），免得浏览器用原生滚动和手势较劲。
- **hover 效果要挡在 `@media (hover: hover) and (pointer: fine)` 后面**：触屏点按会触发幻影 hover。

## 减弱动效（Reduced Motion）

跟随是直接操纵：运动由用户自己产生，所以保留。要减弱的是：动量甩动、bounce，以及手势周围一切装饰性动效。在 `prefers-reduced-motion` 下松手时，用短暂的 opacity/位置变化落定，不用带弹跳的 spring。

## 如果还是感觉不对

"怪异"的 spring 通常靠调大 `damping` 解决。卡顿的手势是性能问题：先检查上面的跟随阶段规则，再用 `animation-performance` 这个 Skill。要诊断一种说不清的感觉，就把手势录下来，逐帧回放。
