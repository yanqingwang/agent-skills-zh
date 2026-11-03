---
name: gsap-timeline
description: GSAP 官方时间线（timeline）Skill — gsap.timeline()、position 参数、嵌套、播放控制。当需要对动画排序、编排关键帧，或用户询问动画序列、时间线或动画顺序时使用（在 GSAP 中，或推荐支持时间线的库时）。
license: MIT
---

> **中文汉化版** · 上游：[greensock/gsap-skills](https://github.com/greensock/gsap-skills) · 原文件：`skills/gsap-timeline/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# GSAP 时间线

## 何时使用本 Skill

在构建多步骤动画、以顺序或并行方式协调多个补间，或用户询问 GSAP 中的时间线、动画排序或关键帧式动画时适用。

**相关 Skill：** 单个补间与缓动使用 **gsap-core**；滚动驱动的时间线使用 **gsap-scrolltrigger**；React 使用 **gsap-react**。

## 创建时间线

```javascript
const tl = gsap.timeline();
tl.to(".a", { x: 100, duration: 1 })
  .to(".b", { y: 50, duration: 0.5 })
  .to(".c", { opacity: 0, duration: 0.3 });
```

默认情况下，补间会**依次追加**。使用 **position 参数**可将补间放置在特定时间点，或相对于其他补间定位。

## Position 参数

第三个参数（或 vars 中的 position 属性）控制放置位置：

- **绝对值**：`1` — 在第 1 秒处开始。
- **相对值（默认）**：`"+=0.5"` — 结束后 0.5 秒；`"-=0.2"` — 结束前 0.2 秒。
- **标签**：`"labelName"` — 在该标签处；`"labelName+=0.3"` — 标签后 0.3 秒。
- **对齐放置**：`"<"` — 从最近添加的动画开始处开始；`">"` — 从最近添加的动画结束处开始（默认）；`"<0.2"` — 最近添加的动画开始后 0.2 秒。

示例：

```javascript
tl.to(".a", { x: 100 }, 0);           // at 0
tl.to(".b", { y: 50 }, "+=0.5");      // 0.5s after last end
tl.to(".c", { opacity: 0 }, "<");     // same start as previous
tl.to(".d", { scale: 2 }, "<0.2");    // 0.2s after previous start
```

## 时间线默认值

向时间线传入 defaults，所有子补间都会继承：

```javascript
const tl = gsap.timeline({ defaults: { duration: 0.5, ease: "power2.out" } });
tl.to(".a", { x: 100 }).to(".b", { y: 50 }); // both use 0.5s and power2.out
```

## 时间线选项（构造函数）

- **paused: true** — 创建时即处于暂停状态；调用 `.play()` 开始播放。
- **repeat**、**yoyo** — 与补间相同；作用于整个时间线。
- **onComplete**、**onStart**、**onUpdate** — 时间线级回调。
- **defaults** — 合并进每个子补间的 vars。

## 标签（Labels）

添加并使用标签，让动画序列易读、易维护：

```javascript
tl.addLabel("intro", 0);
tl.to(".a", { x: 100 }, "intro");
tl.addLabel("outro", "+=0.5");
tl.to(".b", { opacity: 0 }, "outro");
tl.play("outro");  // start from "outro"
tl.tweenFromTo("intro", "outro"); // pauses the timeline and returns a new Tween that animates the timeline's playhead from intro to outro with no ease.
```

## 嵌套时间线

时间线可以包含其他时间线。

```javascript
const master = gsap.timeline();
const child = gsap.timeline();
child.to(".a", { x: 100 }).to(".b", { y: 50 });
master.add(child, 0);
master.to(".c", { opacity: 0 }, "+=0.2");
```

## 控制播放

- **tl.play()** / **tl.pause()**
- **tl.reverse()** / **tl.progress(1)** 之后再 **tl.reverse()**
- **tl.restart()** — 从头开始。
- **tl.time(2)** — 跳转到第 2 秒。
- **tl.progress(0.5)** — 跳转到 50%。
- **tl.kill()** — 终止时间线，（默认情况下）连同其子动画一起终止。

## GSAP 官方最佳实践

- ✅ 序列编排优先使用时间线
- ✅ 使用 **position 参数**（第三个参数）将补间放置在特定时间点，或相对于标签定位。
- ✅ 用 `addLabel()` 添加**标签**，让动画序列易读、易维护。
- ✅ 向时间线构造函数传入 **defaults**，使子补间继承 duration、ease 等。
- ✅ 把 ScrollTrigger 放在时间线（或顶层补间）上，而不是放在时间线内部的补间上。

## 禁止事项

- ❌ 当**时间线**可以为动画排序时，不要用 **delay** 串联动画；多步骤动画请优先使用 `gsap.timeline()` 和 position 参数。
- ❌ 当多个子补间共享相同的 duration 或 ease 时，不要忘记传入 **defaults**（如 `defaults: { duration: 0.5, ease: "power2.out" }`）。
- ❌ 不要忘记时间线构造函数上的 **duration** 与补间的 duration 不是一回事；时间线的“duration”由其子动画决定。
- ❌ 不要嵌套包含 ScrollTrigger 的动画；ScrollTrigger 只应位于顶层的 Tween/Timeline 上。
