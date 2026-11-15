> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/improve-animations/AUDIT.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 动效审计手册

八个审计类别、各自要看什么、以及发现和计划里要引用的精确目标值。蒸馏自 Emil Kowalski 的设计工程哲学（[emilkowal.ski](https://emilkowal.ski/)）。这里出现过的值绝不取近似：照抄。

## 1. 目的与频率

每个动画都要回答"它为什么动？"：空间一致性、状态指示、反馈、解释，或避免一次生硬的变化。高频元素上的一句"看起来酷"不是目的。

| 频率 | 决定 |
| --- | --- |
| 每天 100+ 次（键盘快捷键、命令面板开关） | 不做动画。永远不做。 |
| 每天几十次（hover 效果、列表导航） | 删掉或大幅削弱 |
| 偶尔（modal、drawer、toast） | 标准动画 |
| 罕见 / 首次（引导、反馈、庆祝） | 可以加愉悦感 |

排查要点：键盘触发的动作上的动画、带开合转场的命令面板（Raycast 没有，这才是对的）、被高频命中的列表项或 hover 态上的装饰性动效。最有力的修法往往是**直接删掉动画**。

## 2. 缓动与时长

缓动的决策顺序：

- 进入或退出 → **`ease-out`**（起步快，感觉跟手）
- 屏上移动 / 变形 → **`ease-in-out`**
- hover / 变色 → **`ease`**
- 匀速运动（marquee、进度） → **`linear`**
- 默认 → **`ease-out`**

**UI 上的 `ease-in` 永远是一条发现**：它起步慢，恰好拖慢用户正盯着的那一刻。内置 CSS 缓动对有意图的运动太弱；计划里应引入有力的自定义曲线（做成 token，跟随仓库惯例）：

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);        /* strong ease-out for UI */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);    /* strong ease-in-out for on-screen movement */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);     /* iOS-like drawer curve */
```

时长预算：**UI 动画控制在 300ms 以内**：

| 元素 | 时长 |
| --- | --- |
| 按钮按压反馈 | 100–160ms |
| tooltip、小型 popover | 125–200ms |
| dropdown、select | 150–250ms |
| modal、drawer | 200–500ms |
| 营销 / 解释性 | 可以更长 |

排查要点：任何地方的 `ease-in`、入场用裸 `ease`/`linear`、UI 元素时长 > 300ms、工具栏里每个 tooltip 都带延迟加动画（第一个之后应当即时）。

## 3. 物理性与出发点

- **绝不 `scale(0)`**：现实世界没有东西从虚无中出现。目标：`scale(0.9–0.97)` + `opacity: 0`。
- **popover/dropdown/tooltip 从触发器缩放**，不是从中心：
  ```css
  .popover { transform-origin: var(--transform-origin); } /* Base UI */
  ```
  **modal 豁免**：它们居中出现；那里 `transform-origin: center` 是对的。不要上报。
- **按压反馈**：`:active` 上 `transform: scale(0.97)` 配 `transition: transform 160ms ease-out`。保持克制（0.95–0.98）。

排查要点：`scale(0)`、没有初始 transform 的纯淡入、触发器锚定元素上的 `transform-origin: center`（或缺失）、没有按压反馈的可按压元素。

## 4. 可打断性

CSS **transition** 会在动画中途从当前状态重新定向；**keyframes** 从零重启。任何会被快速触发或运动中途可逆的东西（toast 堆叠、开关、拖拽、展开/收起）必须用 transition 或弹簧。

- 无 JS 的入场：`@starting-style`（旧式后备：`useEffect` 里设置的 `data-mounted` 属性）。
- 手势驱动的运动应该用弹簧：被打断时携带速度。
- 弹簧配置，Apple 风（推荐）：`{ type: "spring", duration: 0.5, bounce: 0.2 }`。bounce 保持克制（0.1–0.3）；明显的弹跳只留给拖拽关闭和俏皮时刻。
- **非对称时序**：有意图的阶段（按压、长按、破坏性确认）动得慢；系统的响应要干脆。按压-释放用对称时序是一条发现。

排查要点：toast/开关/快速触发 UI 上的 `@keyframes`、用固定时长 keyframes 补间的手势处理器、没有基于速度的关闭判定的拖拽（关闭判定用 `Math.abs(distance)/elapsedMs > ~0.11`，不能只看距离阈值）、拖到边界硬停而不是摩擦渐增。

## 5. 性能

- **只动 `transform` 和 `opacity`。** `width`/`height`/`margin`/`padding`/`top`/`left` 触发 layout + paint + composite。
- **`transition: all`** 会把意外属性拖下 GPU：永远是一条发现。
- **`motion` 14.2 之前，`x`/`y`/`scale` 简写不走硬件加速**：它们跑在主线程上，高负载下掉帧。目标：升级到 `motion` 14.2+，HTML 元素上它们是加速的；旧版本写完整 transform 字符串，`animate={{ transform: "translateX(100px)" }}`。布局动画（`layout`、`layoutId`）在所有版本里都跑主线程。
- **不要经父元素上的 CSS 变量驱动子元素 transform**：它会给所有子元素重算样式。直接在元素上设 `transform`。
- 高负载下 CSS（和 WAAPI）胜过基于 rAF 的 JS：预定的运动用 CSS，动态与手势驱动的运动用 JS/弹簧。
- transition 期间的 `filter: blur()` 控制在 20px 以内：重模糊代价高，Safari 尤甚。

排查要点：`transition: all`、动画化布局属性、繁忙页面上的 Motion 简写属性（14.2 之前的版本）、繁忙页面上的布局动画、`setProperty('--x', …)` 驱动子元素 transform、rAF 循环干 CSS 能干的活。

## 6. 无障碍

```css
@media (prefers-reduced-motion: reduce) {
  .element { animation: fade 0.2s ease; } /* keep opacity/color, drop movement */
}
@media (hover: hover) and (pointer: fine) {
  .element:hover { transform: scale(1.05); } /* touch fires false hovers on tap */
}
```

Reduced motion 的意思是更少、更柔，**不是零**：保留帮助理解的过渡，去掉位置变化。JS 里用 `useReducedMotion()` 分支 transform 值。

排查要点：没有 `prefers-reduced-motion` 处理的位移、不加门控的 `:hover` 动效、把所有反馈一并核掉的 reduced-motion 实现。

## 7. 一致性与 token

- 动效要匹配产品性格：俏皮可以更弹，仪表盘保持干脆。组件之间性格错位是一条发现。
- 曲线和时长应作为共享 token 存放。五个几乎相同的手打 cubic-bezier 是一条待合并的发现。
- 本该有 **30–80ms stagger** 的地方做了一次到位的成组入场。stagger 是装饰：绝不能阻塞交互。
- 会露出两个叠印状态的生硬 crossfade，可以在过渡期间用轻微的 `filter: blur(2px)` 遮一下。

排查要点：近乎重复的缓动/时长、干脆应用里一个爱弹的组件、没有 stagger 的列表/网格入场、明显双重曝光的 crossfade。

## 8. 错失的机会

加法类：该动而没动的地方：

- 瞬移式状态变化（内容替换、布局跳动），一段短过渡本可避免那次生硬。
- 空间上相连的 UI（从触发器出现的面板）没有动效解释它从哪来。
- 罕见的高情绪时刻（首次运行、成功、庆祝）没花掉它们被允许的愉悦预算。
- 用 `translate` 百分比（`translateY(100%)` = 元素自身高度）和 `clip-path: inset()` 揭示来做这些：不写死像素偏移。

最多报几条，落在你实际观察到的 UX 接缝上：不是愿望清单。
