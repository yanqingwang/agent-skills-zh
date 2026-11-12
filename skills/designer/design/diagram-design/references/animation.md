> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/animation.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 可选动画

动画是解释一张完整的静态图；它绝不补足缺失的含义。仅当动效被明确要求、或能实质澄清顺序、累积、评估、包含或传播时才加载本参考。否则使用 `none` 模式，交付静态 HTML。

## 模式

每张图用 `data-motion-mode="none|reveal|step|loop"` 选定一种模式。

| 模式 | 行为 | 控制 / 实现 | 用途 |
|---|---|---|---|
| `none` | 完整稳定的图 | 无 JavaScript | 默认、打印、截图、导出，以及播放控件不可用时的 reduced-motion 回退 |
| `reveal` | 一次确定性的自动播放，结束时完整 | ≤5s 用纯 CSS；否则用受控的控制器 | 短的有序讲解；绝不自动重播 |
| `step` | 暂停的语义状态 | 极少量内联 JS，提供 Play、Pause、Replay、Previous、Next | 教学、对比、策略轨迹 |
| `loop` | 一个装饰性 token 重复，不改变含义 | 默认纯 CSS | 轻缓的流动暗示；周期 ≥3s |

只有 `loop` 会重复。队列状态、打字、字段值、策略结果、包含关系、审计条目都用 `reveal` 或 `step`，且播完即完整。

`reveal` 是唯一获准的自动播放模式：动效被明确要求时，可在初次加载时运行一次，然后保持完整。视口再次进入或不经显式 Replay 操作时绝不重启。

## 静态优先的增强契约

1. **来源是完整的。** 每个语义节点、标签、连接线、状态与结果，在增强之前就在 HTML/SVG 中可见。只有 `.motion-ready` 以下的选择器可以隐藏或变换它们。
2. **稳定的捕获。** 初始 `data-frame="static"`、`?motion=static`、打印、无 JS 与独立 SVG 导出都暴露完整帧并隐藏控件/装饰性 token。不要在任意延迟之后捕获。
3. **CSS 负责表现。** 出现与移动用 CSS transitions/keyframes。极少量内联 JavaScript 只允许用于绑定显式控件、更新 step/state 属性、调度确定性步骤、更新专用 live-status 区域。不许 fetch、注入标记、测量路径，也不许改写语义图表标签或取值。
4. **一个时钟。** 使用 `--motion-fast: 160ms`、`--motion-step: 480ms`、`--motion-hold: 720ms` 与 `--motion-total` ≤ `8000ms`；延迟从整数步推导。不许随机、弹性或依赖 transition 事件的时序。
5. **显式顺序。** 条目标记为 `data-motion-item data-step="N"`，N 为 1–8 的整数步。DOM 顺序跟随叙事顺序。每步最多两个条目进入。
6. **稳定的终态。** 完成时暴露全部条目并置 `data-frame="end"`。Replay 先重置到第 0 步。Pause 清除挂起计时器，恢复时从同一步继续。
7. **作用域状态。** 控件只作用于最近的 `[data-motion-root]`；ID、计时器、live region 与 step 状态绝不跨图。
8. **失败安全的启动。** JavaScript 只有在控件绑定完成且初始渲染成功之后才添加 `.motion-ready`。在此之前发生脚本错误，完整的来源保持可见。

## 语义基元

每个基元除颜色外都有文字、计数、符号、图案或轮廓。

| 基元 | 机制 | 静态 / reduced-motion 结果 | 限制 |
|---|---|---|---|
| **Path draw** | 带装饰性的复制路径，`pathLength="1"` 加动画虚线偏移 | 带标签的基础连接线保持可见 | ≤2 条路径；同时一条活动 |
| **Staggered reveal**（阶段揭示） | `data-motion-item` + opacity/translate ≤8px | 所有阶段可见 | ≤8 步、12 项 |
| **Queue counter**（队列累积） | 稳定槽位；条目揭示加可见的数字计数 | 最终队列与计数可见 | ≤5 项；不重排 |
| **Typing / field population** | 完整可访问字符串；裁切的装饰性覆盖层或带标签的行揭示 | 完整文字/字段显示一次 | ≤32 个键入字符或 6 个字段 |
| **Policy evaluation**（规则评估） | 有序规则行，带文字状态与当前行轮廓 | 每个状态与结果可见 | 3–6 条规则；2 条轨迹 |
| **Flow token** | 固定路径上的 `aria-hidden` token | token 隐藏；连接线保留 | 一个 token；周期 ≥3s |
| **Containment** | 先揭示子级，再显示持久的带标签边界 | 子级与边界可见 | 一次边界过渡 |
| **Audit append** | 按时间顺序揭示的行；稳定的时间戳/序号 | 完整有序日志可见 | ≤5 追加行 |

不要给布局坐标、连接线路由、`viewBox`、节点尺寸或语义文字加动画。避免缩放、视差、弹跳、抖动、发光、粒子与无限闪烁。

```css
:root {
  --motion-fast: 160ms;
  --motion-step: 480ms;
  --motion-hold: 720ms;
  --motion-total: 3600ms; /* five steps × hold; set this per diagram */
  --motion-ease: cubic-bezier(.2,.8,.2,1);
}
.motion-ready [data-motion-item] {
  opacity: .12;
  transform: translateY(8px);
  transition: opacity var(--motion-step) var(--motion-ease),
              transform var(--motion-step) var(--motion-ease);
}
.motion-ready [data-motion-item].is-visible,
.motion-ready[data-frame="end"] [data-motion-item] {
  opacity: 1;
  transform: none;
}
[data-motion-controls][hidden] { display: none !important; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
    scroll-behavior: auto !important;
  }
  [data-motion-item] { opacity: 1 !important; transform: none !important; }
  [data-motion-decorative] { display: none !important; }
  [data-motion-controls] { display: none !important; }
}
@media print {
  [data-motion-controls], [data-motion-decorative] { display: none !important; }
  [data-motion-item] { opacity: 1 !important; transform: none !important; }
}
```

## 交互控件与键盘

每个交互式 `step` 图都在 SVG 之外提供原生按钮：**Play、Pause、Replay、Previous、Next**。使用 `data-motion-action="play|pause|replay|prev|next"`、≥44×44px 的点击区、可见焦点、不可用动作的禁用态，以及 play/pause 状态的 `aria-pressed`。

焦点在 motion root 内时：`ArrowRight` 前进，`ArrowLeft` 后退，`Home` 重置，`End` 快进到末尾，焦点不在原生控件上时 `Space` 切换播放/暂停，不加修饰键的 `R` 重播。按住 Control、Command 或 Alt 时绝不拦截 `R`。不捕获来自输入框、链接或无关区域的按键。帧切换时绝不移动焦点。

提供可见说明，以及一个限定作用域的 `role="status" aria-live="polite" aria-atomic="true"`。live region 放在 motion root 内、`[data-motion-controls]` 之外，这样 reduced/static 状态隐藏控件时不会连带隐藏播报。播报用户动作，如"第 3 步，共 5 步：首次分歧"；自动播放的每一帧不必播报。控件只作用于最近的 `[data-motion-root]`。

用 [`assets/template-motion.html`](../assets/template-motion.html)，不要另造控制器。其内联控制器就是可执行的实施契约：逐字复制该脚本主体。皮肤 linter 会拒绝被修改或额外添加的控制器，即使它们带 `data-diagram-controls`。可以替换图表内容与带 slug 前缀的 ID，但控制器与其状态/控件属性必须原样保留。

## Reduced motion、颜色与可访问性

- `prefers-reduced-motion: reduce` 以完整静态帧初始化，禁用并隐藏所有播放控件，隐藏装饰性移动，并暴露 `data-motion-state="reduced"` 加上"播放不可用"的状态文字。绝不在完整帧旁边呈现半截步骤的播报。
- SVG 的 `<title>` 与 `<desc>` 描述完整含义，不描述动画。操作说明保留为可见的 HTML 文字。
- 装饰性覆盖层带 `aria-hidden="true" focusable="false"`。语义文字在无障碍树中只存在一份。
- 状态绝不仅用颜色：策略用符号 + `PASS/FAIL/SKIPPED/NOT REACHED`；队列显示计数；活动阶段用数字/标签/轮廓。
- 每秒闪光或亮度变化不超过三次。

## 复杂度与确定性时序

动效不抬高静态图预算：≤8 个语义步（目标 3–6）、≤12 个标记条目、≤2 个同时揭示、≤2 条绘制路径、一个 flow-token 循环、160–600ms 过渡、400–1200ms 停留、≤24px 位移、3–8s 自动播放总时长。

位移限制有一个限定范围的例外：爆炸轴测图中的部件可以沿竖直方向恰好抬升其爆炸距离，即声明为 `--lift` 的值，`scripts/verify-exploded.py` 会对照其几何检查它（`type-exploded.md`）。该图中其他任何东西的位移都不超过 24px，其他所有类型都维持原限。

声明 `data-step-count`；不要从 transition 事件推断步数。把 `--motion-total` 设为步数 × `--motion-hold`，并保持在 8 秒预算内。每个 root 一条 `setTimeout` 链，停留时长从 `--motion-hold` 取，Pause/Replay/页面隐藏时以及渲染完最后一步后立即清除，语义播放绝不使用 `setInterval`。`document.visibilityState` 变为 hidden 时暂停，回来后不追帧。`?motion=step&step=N` 可暴露精确的零时长帧，仅供视觉回归使用，且 N 必须是 0 到 `data-step-count` 之间的非负十进制整数；缺失、带小数、负数或超预算的值都维持正常播放。

终态捕获契约是同步的：`?motion=static`、`<html data-motion="static">` 或 `none` 模式暴露每个语义条目、隐藏控件与装饰性覆盖层，并置 `data-frame="static"`。捕获前等待 `document.fonts.ready`。渲染裁切校验器在对比授权绘制与溢出释放绘制之前，也使用同一个静态 URL。同一 URL、视口、字体与设备缩放下的两次捕获必须逐像素一致；随机延迟、生成的 ID、时钟与运行时路径测量都被禁止。

## 导出与校验

PNG 与 SVG 导出是静态终态产物，除非用户明确要求某个命名步骤。捕获前打开 `?motion=static`，等待 `document.fonts.ready`，并断言 `data-frame="static"`。SVG 提取会略去 HTML 控件与脚本；来源可见的语义标记保证结果完整。

运行：

```bash
python3 scripts/verify-motion.py path/to/animated-diagram.html
python3 scripts/test-verify-motion.py
python3 scripts/lint-skin.py path/to/animated-diagram.html
```

校验器检查模式/状态声明、连续步、动效预算、完整的 SVG 命名、无 JS 来源可见性、装饰性可访问性、完整控件集、live status、reduced-motion/print CSS、键盘处理、页面隐藏暂停、有界的 static/test 覆盖、最后一步立即停止，以及与规范控制器完全一致的身份。标记 `aria-hidden="true"` 的根级 SVG 图标豁免于图表命名检查，但文档仍需要一个可访问的 SVG（policy-trace 示例恰好一个）。其对抗性测试会改动规范模板，证明每种失败都会被拒绝。

然后在浏览器中核验：

1. 禁用 JavaScript：完整图表仍然可见且有意义。
2. 模拟 `prefers-reduced-motion: reduce`：终态完整，播放控件隐藏且禁用，DOM 状态显示播放不可用。
3. 仅用键盘：Tab 到达每个原生控件；Enter/Space 操作它；Left/Right/Home/End 切步而不移动焦点。
4. 暂停、恢复并重播两次：顺序与终态完全一致。
5. 在 `document.fonts.ready` 之后捕获 `?motion=static` 两次：像素稳定。
6. 打印预览加 PNG/SVG 导出：控件与装饰性 token 不存在，全部语义标签与关系保留。

## 反模式

- 未经要求的自动播放、`reveal` 唯一获准运行之外的自动播放、视口再进入、或无休止的语义循环。
- 无 JS 或 reduced-motion 下出现空白/残缺帧。
- 用动效挽救过密或无标签的静态图。
- 只用色相编码 pass/fail、队列满度或结果。
- 远程脚本、通用应用逻辑、运行时几何，或重复的语义文字。
- 按墙钟延迟捕获，而不是用显式的静态覆盖。
