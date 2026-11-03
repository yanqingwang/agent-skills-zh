---
name: gsap-performance
description: GSAP 官方性能 Skill — 优先使用 transform、避免布局抖动（layout thrashing）、will-change、批量处理。当优化 GSAP 动画、减少卡顿（jank），或用户询问动画性能、FPS 或流畅 60fps 时使用。
license: MIT
---

> **中文汉化版** · 上游：[greensock/gsap-skills](https://github.com/greensock/gsap-skills) · 原文件：`skills/gsap-performance/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# GSAP 性能

## 何时使用本 Skill

在优化 GSAP 动画以实现流畅 60fps、降低布局/绘制开销时适用；当用户询问动画性能、卡顿（jank）或快速动画的最佳实践时也适用。

**相关 Skill：** 使用 **gsap-core**（transform、autoAlpha）与 **gsap-timeline** 构建动画；ScrollTrigger 性能参见 **gsap-scrolltrigger**。

## 优先使用 Transform 和 Opacity

对 **transform**（`x`、`y`、`scaleX`、`scaleY`、`rotation`、`rotationX`、`rotationY`、`skewX`、`skewY`）和 **opacity** 制作动画，可以把工作留在合成器（compositor）上，避免布局重排和大部分绘制。当 transform 能实现同样效果时，避免对布局开销大的属性制作动画。

- ✅ 优先使用：**x**、**y**、**scale**、**rotation**、**opacity**。
- ❌ 尽量避免：**width**、**height**、**top**、**left**、**margin**、**padding**（它们会触发布局重排，可能导致卡顿）。

GSAP 的 **x** 和 **y** 默认基于 transform（translate）；移动元素时请用它们代替 **left**/**top**。

## will-change

在 CSS 中对将要制作动画的元素使用 **will-change**。它会提示浏览器将该元素提升为独立图层。

```css
will-change: transform;
```

## 批量读写

GSAP 内部会批量处理更新。当把 GSAP 与直接的 DOM 读写或依赖布局的代码混用时，避免以导致反复布局抖动（layout thrashing）的方式交错进行读取和写入。优先先完成所有读取，再进行所有写入（或让 GSAP 一次性处理写入）。

## 大量元素（Stagger、列表）

- 当动画相同时，使用 **stagger** 代替大量带手动 delay 的独立补间，效率更高。
- 对于长列表，考虑**虚拟化**或只对可见项制作动画；如果会造成卡顿，避免同时创建数百个补间。
- 尽可能复用时间线；避免每帧都创建新的时间线。

## 高频更新的属性（如鼠标跟随）

对频繁更新的属性（如鼠标跟随的 x/y），优先使用 **gsap.quickTo()**。它复用单个补间，而不是每次更新都创建新补间。

```javascript
let xTo = gsap.quickTo("#id", "x", { duration: 0.4, ease: "power3" }),
    yTo = gsap.quickTo("#id", "y", { duration: 0.4, ease: "power3" });

document.querySelector("#container").addEventListener("mousemove", (e) => {
  xTo(e.pageX);
  yTo(e.pageY);
});
```

## ScrollTrigger 与性能

- **pin: true** 会提升被固定（pin）的元素；只对必要的元素使用 pin。
- **scrub** 配合较小的值（如 `scrub: 1`）可以减少滚动期间的工作量；请在低端设备上测试。
- 仅在布局确实发生变化时（如内容加载后）才调用 **ScrollTrigger.refresh()**，而不是每次 resize 都调用；尽可能做防抖（debounce）。

## 减少同时进行的工作

- 当动画不可见或处于非活动状态时（如用户离开页面），暂停或终止（kill）它们。
- 避免同时对大量元素上的大量属性制作动画；必要时进行简化或改为顺序执行。

## 最佳实践

- ✅ 对 **transform** 和 **opacity** 制作动画；仅在真正制作动画的元素上使用 CSS **will-change**。
- ✅ 当动画相同时，使用 **stagger** 代替大量带手动 delay 的独立补间。
- ✅ 对高频更新的属性（如鼠标跟随）使用 **gsap.quickTo()**。
- ✅ 清理或终止离屏动画；在布局变化时调用 **ScrollTrigger.refresh()**，并尽可能做防抖。

## 禁止事项

- ❌ 当 **x**/**y**/**scale** 能实现相同视觉效果时，不要用 **width**/**height**/**top**/**left** 实现位移。
- ❌ 不要“以防万一”地对每个元素都设置 **will-change** 或 **force3D**；只对真正制作动画的元素使用。
- ❌ 不要在未于低端设备上测试的情况下创建数百个重叠的补间或 ScrollTrigger。
- ❌ 不要忽略清理；游离（stray）的补间和 ScrollTrigger 会持续运行，损害性能和正确性。
