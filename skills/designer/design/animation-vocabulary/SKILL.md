---
name: animation-vocabulary
description: 反向查询术语表：把对网页动画或动效的模糊描述转换成准确的术语（"popover 打开时弹一下的那个东西" → Pop in；"iOS 那种橡皮筋滚动" → Rubber-banding）。当用户问"……的时候叫什么"，或描述了一个动效却不知道名字、想要一个准确的词去提示 AI 或设计师时使用。用于给效果命名，不是设计或实现效果。
---

> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/animation-vocabulary/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 动画术语表

## 初始回应

当本 Skill 首次被调用且没有具体问题时，只回应以下内容：

> 我已准备好为你描述的任何动效起名，我的知识来自 Emil Kowalski 的动画哲学。

在用户提问之前，不要提供任何其他信息。

把对运动或效果的模糊描述变成准确的术语，让用户知道自己该要什么。

## 快速上手

用户笼统地描述一个效果。你按下面的格式返回匹配的术语：

```
**Stagger** — Animate several items one after another with a small delay between each, creating a cascade.
```

如果多个术语都可能符合，最佳匹配排第一，随后给 1–2 个备选，各附一行说明区别。

## 指令

1. **读意图，不是读关键词。** 用户描述的是他们*看到*或*感觉到*的东西（"弹弹的"、"滑出去的"、"自己画出来的"），不是技术名词。把这种感觉映射到下面的术语表上。
2. **逐字引用术语表。** 它的描述是权威的：原样使用，不要改写。
3. **区分相近术语。** 当两个术语不相上下时（*Clip-path* vs *Mask*、*Pop in* vs *Bounce*、*Shared element transition* vs *Layout animation*），给出对比，让用户能选。
4. **没有完全匹配时，** 说出最接近的术语并明说它只是近似，或者用术语表的词汇描述这个效果（例如"那是 *scale-in* 入场组成的 *stagger*"）。
5. **不超出这份术语表。** 如果某个术语确实不在其中，直说，不要编造；但可以用这些词去解释概念。
6. **保持简短。** 命名问题要的是名字，不是文章。先给术语；被问到再展开。

## 示例

**示例 1 — 按感觉描述**
用户："popover 好像是从你点击的那个按钮里长出来的，而不是从它自己的中心长出来，这个叫什么？"
输出：
```
**Origin-aware animation** — An element animates out of its trigger, like a popover growing from the button that opened it instead of from its own center which is the default in CSS.
```

**示例 2 — 消歧**
用户："一张图变成另一张图的那个东西。"
输出：
```
**Morph** — One shape smoothly turns into another shape, e.g. Dynamic Island.

Close alternates:
- **Crossfade** — if they simply fade over each other in the same spot.
- **Shared element transition** — if an element travels and transforms from one position into another.
```

**示例 3 — 物理手感**
用户："iOS 那种滚动手感：拉得太远会有阻力，然后弹回来。"
输出：
```
**Rubber-banding** — Resistance and snap-back when you drag past a boundary (the iOS overscroll feel).
```

## 术语表

_精选快照，与本项目的 `/vocabulary` 页面互为镜像；任何一方变更时，保持两者同步。_

### Entrances & Exits — 元素如何出现和消失
- **Fade in / Fade out（淡入 / 淡出）** — 通过改变 opacity 让元素出现或消失。
- **Slide in（滑入）** — 元素从屏幕外（左、右、上或下）滑入进场。
- **Scale in（缩放入场）** — 元素出现时从小长到完整尺寸，常与 fade 搭配。
- **Pop in（弹出）** — 元素带轻微 overshoot 出现，像弹跳着落到位。
- **Reveal（揭示）** — 内容被逐渐揭开，通常靠动画化 clip-path 或 mask。
- **Enter / Exit（入场 / 退场）** — 元素被加入或移出屏幕时播放的动画。

### Sequencing & Timing — 协调多个元素或多个时刻
- **Keyframes（关键帧）** — 动画中定义的点（0%、50%、100%），浏览器负责填补点与点之间的空隙。
- **Interpolation / Tween（插值 / 补间）** — 在起始值和结束值之间生成全部中间帧，让运动连续。
- **Stagger（错峰）** — 多个条目依次出现，彼此之间隔一个小 delay，形成级联。
- **Orchestration（编排）** — 刻意安排多个动画的时机，让它们感觉像一次协调的运动。
- **Delay（延迟）** — 动画开始之前的时间。
- **Duration（时长）** — 动画持续多久。
- **Fill mode（填充模式）** — 元素在动画开始前或结束后，是否保持首帧或末帧的样式（例如 forwards）。
- **Stepped animation（步进动画）** — 被分成离散步骤的动画，比如倒计时。

### Movement & Transforms — 改变元素的位置、尺寸或角度
- **Translate（平移）** — 沿 X 轴或 Y 轴移动元素。
- **Scale（缩放）** — 把元素变大或变小。
- **Rotate（旋转）** — 让元素绕某个点旋转。
- **Skew（倾斜）** — 沿 X 轴或 Y 轴斜切元素，把它从矩形拉成平行四边形。
- **3D tilt / Flip（3D 倾斜 / 翻转）** — 在 3D 空间中旋转（rotateX / rotateY）以增加纵深。
- **Perspective（透视）** — 3D 效果看起来的强弱：值越小纵深越夸张，像观看者凑得更近。
- **Transform origin（变换原点）** — scale 或 rotation 生长或旋转所围绕的锚点。
- **Origin-aware animation（感知原点的动画）** — 元素从它的触发处开始动画，比如 popover 从打开它的按钮处长出来，而不是从自己的中心（CSS 的默认行为）。

### Transitions Between States — 把一个状态、视图或元素连接到另一个
- **Crossfade（交叉淡化）** — 一个元素 fade out 的同时另一个 fade in，位置相同。
- **Continuity transition（连续性过渡）** — 通过在视觉上连接前后状态、让用户保持定向的变化。比如把同一个矩形变大再变小。
- **Morph（形变）** — 一个形状平滑地变成另一个形状，如 Dynamic Island。
- **Shared element transition（共享元素过渡）** — 元素从一个位置移动并变换到另一个位置，如缩略图展开成卡片。
- **Layout animation（布局动画）** — 元素的尺寸或位置变化时，动画过渡到新位置，而不是瞬间跳过去。
- **Accordion / Collapse（手风琴 / 折叠）** — 区块平滑地展开和收起高度，以显示或隐藏内容。
- **Direction-aware transition（方向感知过渡）** — 前进时内容向一侧滑，后退时向另一侧滑，让导航有方向感。

### Scroll — 与滚动或视图间导航绑定的运动
- **Scroll reveal（滚动显现）** — 元素进入 viewport 时 fade 或滑入到位。
- **Scroll-driven animation（滚动驱动动画）** — 进度直接绑定滚动位置的动画。
- **Parallax（视差）** — 滚动时背景和前景以不同速度移动，制造纵深。
- **Page transition（页面过渡）** — 从一个页面或路由导航到另一个时播放的动画。
- **View transition（视图过渡）** — 浏览器在两个状态或页面之间做 morph，把共享元素连接起来。

### Feedback & Interaction — 响应用户的操作
- **Hover effect（悬停效果）** — 光标移到元素上时的视觉变化。
- **Press / Tap feedback（按压反馈）** — 元素被点击时轻微缩小，让它有实体感。
- **Hold to confirm（按住确认）** — 用户按住按钮时逐渐填满的进度效果。
- **Drag（拖拽）** — 抓住元素移动，松手时常带惯性。
- **Drag to reorder（拖拽排序）** — 拖动列表中的条目重新排列，其他条目移位让出空间。
- **Swipe to dismiss（滑动关闭）** — 把元素拖出屏幕来关闭它，如 drawer 或 toast。
- **Rubber-banding（橡皮筋效应）** — 拖过边界时的阻力和回弹（iOS 的 overscroll 手感）。
- **Shake / Wiggle（抖动）** — 快速的左右颤动，表示出错或输入被拒绝。
- **Ripple（涟漪）** — 从点按位置扩散开的一个圆，确认这次按压。

### Easing — 动画中速度如何变化
- **Easing（缓动）** — 动画加速或减速的速率。
- **Ease-out** — 起步快，结束慢。大多数 UI 和一切响应用户的操作的默认选择。
- **Ease-in** — 起步慢，结束快。通常要避免，会显得迟滞。
- **Ease-in-out** — 慢、快、慢。适合已经在屏幕上、从 A 移到 B 的元素。
- **Linear** — 匀速。UI 里避免使用；留给 spinner 或 marquee。
- **Cubic-bezier** — 自定义缓动曲线，用于精确控制。
- **Asymmetric easing（非对称缓动）** — 加速和减速速率不同的曲线。比对称的更有生命力。

### Spring Animations — 以物理为基础的运动，作为固定时长 easing 的替代
- **Spring（弹簧）** — 由物理（张力、质量、阻尼）驱动、而非固定时长的运动。
- **Stiffness / Tension（刚度 / 张力）** — 弹簧拉向目标的力度。越高越干脆。
- **Damping（阻尼）** — 弹簧多快落定。阻尼越低，bounce 和振荡越多。
- **Mass（质量）** — 被动画的元素感觉有多重。质量越大越慢、越迟钝。
- **Bounce（回弹）** — 弹簧过冲再落定，增加俏皮感。
- **Perceptual duration（感知时长）** — 一个 spring 感觉上多久算结束，哪怕它底下还在持续微幅落定。
- **Momentum（动量）** — 带着速度的运动，尤其在拖拽或被打断之后。
- **Velocity（速度）** — 元素运动得多快、朝哪个方向。被打断时 spring 会把速度带进下一个动画，所以被轻甩的元素能保住速度。
- **Interruptible animation（可中断动画）** — 可以在半路被平滑改向、而不必先播完的动画。

### Looping & Ambient Motion — 自行运转的动画
- **Marquee（跑马灯）** — 循环连续滚动的文字或内容。
- **Loop（循环）** — 重复播放的动画，固定次数或无限。
- **Alternate (yoyo)（往复）** — 每轮先正放再倒放的循环，而不是跳回起点。
- **Orbit（环绕）** — 一个元素沿连续路径绕另一个元素转圈。
- **Pulse（脉动）** — 轻柔重复的 scale 或 opacity 变化，用来吸引注意。
- **Float（漂浮）** — 轻柔、连续的上下漂移，让静态元素显得有生命、没有重量。
- **Idle animation（待机动画）** — 元素静静等待交互时播放的细微运动。

### Polish & Effects — 把"良好"和"出色"区分开的小细节
- **Blur（模糊）** — 用来柔化元素或掩盖微小瑕疵的模糊滤镜。
- **Clip-path（裁剪路径）** — 把元素裁剪成某个形状，用于 reveal、mask 和前后对比滑块。
- **Mask（遮罩）** — 用形状或渐变隐藏或显示元素的局部，和 clip-path 类似，但边缘柔和、可淡出。
- **Before / after slider（前后对比滑块）** — 一条可拖动的分隔线，在两张叠放的图片之间擦动对比。
- **Line drawing（线条绘制）** — 自己画出来的 SVG path，像一支看不见的笔在描它。
- **Text morph（文字形变）** — 文字变化时逐字符做动画，把注意力引向新值。
- **Skeleton / Shimmer（骨架屏 / 微光）** — 内容加载时显示的占位符，带一道移动的光泽。
- **Number ticker（数字滚动）** — 数字滚动或累加到某个值。
- **Tabular numbers（等宽数字）** — 固定宽度的数字，变化时不会来回挪动。对 ticker、计时器和计数器必不可少。
- **Typewriter（打字机）** — 文字一次出现一个字符，像正在被敲出来。

### Performance — 让运动平滑而不是卡顿的关键
- **Frame rate (FPS)（帧率）** — 每秒绘制的帧数。60fps 是流畅运动的基线；较新的显示器是 120fps。
- **Jank（卡顿）** — 浏览器跟不上动画而丢帧时，肉眼可见的顿挫。
- **Dropped frame（掉帧）** — 浏览器错过绘制时限的一帧，在运动中造成一个微小的停顿。
- **Compositing（合成）** — 让 GPU 在元素自己的层上移动或淡化它，不必重做 layout 或 paint。
- **will-change** — 一个 CSS 提示，告诉浏览器某元素即将做动画，浏览器可以提前把它提升到自己的层。
- **Layout thrashing（布局抖动）** — 动画 width、height、top、left 这类属性，迫使浏览器每帧重新计算 layout，造成卡顿。

### Principles to Know — 指导何时动画、如何动画的概念
- **Purposeful animation（有目的的动画）** — 运动应当服务于功能：定向、给反馈、展示关系，而不只是装饰。
- **Anticipation（预备动作）** — 动作之前先向反方向小幅蓄力，暗示即将发生什么。
- **Follow-through（跟随）** — 主体运动停止后，元素的局部继续运动并轻轻落定，增加重量感。
- **Squash & stretch（挤压与拉伸）** — 元素运动时发生形变，传达重量、速度和柔韧。
- **Perceived performance（感知性能）** — 合适的动画让界面感觉更快，哪怕实际没有。
- **Frequency of use（使用频率）** — 用户看到一个动画的次数越多，它就该越短、越含蓄。
- **Spatial consistency（空间一致性）** — 通过动画让元素跨状态保持它的身份和位置，用户永远不会跟丢东西去了哪。
- **Hardware acceleration（硬件加速）** — 只动画 transform 和 opacity，让 GPU 保住运动的流畅。
- **Reduced motion（减弱动效）** — 尊重用户的 prefers-reduced-motion 设置，减弱或移除运动。
