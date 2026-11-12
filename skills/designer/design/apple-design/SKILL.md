---
name: apple-design
description: Apple 的界面设计方法与流畅、带物理感的动效，已翻译到 Web 平台。Use when：构建或评审手势驱动 UI、弹簧动画（spring animation）、拖拽/滑动/面板（sheet）交互、动量与可中断过渡、半透明材质与深度、排版（optical sizing、tracking、leading）、减弱动态（reduced-motion），或 Apple 风格界面背后的设计基础（反馈、空间一致性、克制）时。
---

> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/apple-design/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Apple 设计

## 初始响应

当这个 skill 在没有具体问题的情况下首次被调用时，只回应：

> 我已准备好帮你在 Web 上构建流畅的 Apple 风格界面，我的知识来自 Apple 的 WWDC 设计演讲，已翻译到 Web 平台。

在用户提问之前，不要提供任何其他信息。

Apple 如何造出不再像计算机、开始像你身体延伸的界面。这些知识来自 Apple 的 WWDC 设计演讲，主要是 *Designing Fluid Interfaces*（WWDC 2018），经蒸馏后翻译到 Web 平台（CSS、Pointer Events、`requestAnimationFrame`、Motion/Framer Motion 这类弹簧库）。

主线：**当动效从当前屏幕值起步、继承用户的速度、把动量向前投射、并且能在任何瞬间被抓住和反转时，界面才有活的感觉。**弹簧是让这一切自然发生的工具，因为它天生可中断、感知速度。

## 核心思想

> "当我们把界面对齐到我们思考和移动的方式，神奇的事就发生了——它不再像一台计算机，开始像我们自身无缝的延伸。"

界面的"流畅"来自它像物理世界一样行事：东西立即响应、连续移动、携带动量、在边界处产生阻力、并且能在运动中途被改向。下面的一切都是靠近这个目标的方法。

Apple 把设计框定为服务四种人的需求：**安全/可预测、理解、成就、愉悦。**这里的每条规则都在服务其中之一。

## 1. 响应：消灭延迟

延迟一出现，直接操纵的感觉就"断崖式下跌"。响应是其余一切的地基。

- **在 pointer-down 时响应，而不是抬起时。**按钮被按下的瞬间就高亮。等 `click`/抬手才给反馈，感觉是死的。
- **警惕每一处延迟。**审计防抖、人造定时器、过渡等待，还有约 300ms 的点按延迟。输入路径上任何非必需的东西都是回归。
- **反馈必须在交互 *过程中* 连续，不能只在结束时。**拖拽、滑块、抽屉，全程让 UI 与指针 1:1 同步——绝不要只在手势完成时才动。

```css
/* Feedback lives on the press, and it's instant */
.button:active {
  transform: scale(0.97);
  transition: transform 100ms ease-out;
}
```

## 2. 直接操纵：1:1 跟踪

> "触摸和内容应该一起移动。"

用户拖动某个东西时，它必须粘在手指上，并且尊重 *抓取位置* 的偏移。一抓就吸附到元素中心，错觉立刻破灭。

- 用 Pointer Events 加 `setPointerCapture`，指针离开元素边界后跟踪也不中断。
- 跟踪一小段 **速度/位置历史**（最近几次 `pointermove` 事件），而不只是当前点，因为松手时你会需要速度。

```js
el.addEventListener('pointerdown', (e) => {
  el.setPointerCapture(e.pointerId);
  const grabOffset = e.clientY - el.getBoundingClientRect().top; // respect where they grabbed
  // ...track position + timestamp history for velocity
});
```

## 3. 可中断性：最重要的原则

> "想法和手势并行发生。"

每个动画都必须能在任何时刻被中断和改向。用户必须能在元素运动途中抓住它并反转，不用等动画跑完。被用户再次抓住的正在关闭的模态框应该跟着手指走，而不是先关完再重新打开。

- **过渡期间绝不锁输入。**
- **永远从 *呈现*（当前）值开始动画，绝不要从目标值开始。**被中断时，读取元素实时的屏幕 transform，从那里启动新动画。从逻辑值/目标值起步会造成可见的跳变。
- **手势驱动的东西避开 CSS transition 和 `@keyframes`**：它们无法在半途被平滑抓住和反转。弹簧默认从当前值开始动画，这正是中断需要的。
- **手势反向时混合速度，不要硬切。**反转瞬间直接换动画会造成速度不连续，一面"砖墙"。能在改目标时带着速度走的弹簧库可以避开。（iOS 的 *additive animations* 原生就是这么做的；Web 上选一个能从当前速度改目标的弹簧库。）
- **把 2D 运动拆成独立的 X 和 Y 弹簧。**单个弹簧管 2D 距离，在 X 和 Y 速度不同时会失步。

## 4. 行为优先于动画：用弹簧

> "把动画想成你和物体之间的对话，而不是界面规定好的剧本。"

写死时长的预设动画无法响应新输入。弹簧可以：新输入只是改目标，运动保持连续。用户摸得到的东西都用弹簧。

Apple 有意用两个对设计者友好的参数取代了物理三元组（质量/刚度/阻尼）。用这两个思考：

- **阻尼比（damping ratio）**：控制过冲。`1.0` = 临界阻尼，无回弹，平滑落定。`< 1.0` = 过冲并振荡。越低越弹。
- **Response**：值多快到达目标，以秒计。越低越利落。**这不是"时长"**，弹簧没有固定时长；落定时间由参数涌现。

**默认值：**
- 大多数 UI 从**阻尼 `1.0`**（临界阻尼）起步：优雅、不抢戏。
- **只有手势本身携带动量时**（轻扫、抛掷、拖拽松手）才加回弹（**阻尼约 `0.8`**）。刚淡入的菜单过冲很怪；被你轻扫的卡片过冲就对。

**Apple 实际在用的具体值：**

| 交互 | 阻尼 | Response |
| --- | --- | --- |
| 移动 / 重新定位（如画中画） | `1.0` | `0.4` |
| 旋转 | `0.8` | `0.4` |
| 抽屉 / 面板（sheet） | `0.8` | `0.3` |

**Web 对应（Motion / Framer Motion）：**`bounce` + `duration` 弹簧 API 与 Apple 的阻尼 + response 对应得很好。稳妥的团队风格是默认全用 `damping: 1.0` 的弹簧；bounce 留给有动量的物理交互。

```js
import { animate } from 'motion';

// Critically damped default (no overshoot)
animate(el, { y: 0 }, { type: 'spring', bounce: 0, duration: 0.4 });

// Momentum interaction — a little bounce, only because a flick preceded it
animate(el, { y: target }, { type: 'spring', bounce: 0.2, duration: 0.4 });
```

## 5. 速度交接：拖拽与动画之间的接缝

手势结束时，动画必须**以手指的精确速度继续**，拖拽和动画之间才没有可见接缝。这是"流畅"与"还行"之间最大的差别所在。

把指针的松手速度作为弹簧初速度传入。有些弹簧 API 要 **相对** 速度，用剩余距离归一化：

```
relativeVelocity = gestureVelocity / (targetValue − currentValue)
```

例子：元素在 `y=50`，目标 `y=150`（还差 100px），手指以 50px/s 移动，弹簧初速度 = `50 / 100 = 0.5`。Framer Motion / Motion 直接接受绝对 px/s 速度（`velocity` 选项），所以通常直接给原始值。

## 6. 动量投射：动画到手势 *要去* 的地方

> "小输入，大输出。"

不要从 *松手点* 直接吸附到最近边界。用速度**投射静止位置**（与滚动减速完全一样），然后吸附到离投射点最近的目标。轻扫像把元素"扔"出去，靠的就是这个。

Apple 确切的投射函数（出自 *Designing Fluid Interfaces* 示例代码）：

```js
// decelerationRate ≈ 0.998 for normal scroll feel; 0.99 for snappier
function project(initialVelocity /* px/s */, decelerationRate = 0.998) {
  return (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate);
}

const projectedEndpoint = currentPosition + project(releaseVelocity);
const target = nearestSnapPoint(projectedEndpoint);   // choose target from the projection
animateSpringTo(target, { velocity: releaseVelocity }); // then hand off velocity (§5)
```

注意：物理课本上的 `v²/(2·decel)` *不是* Apple 实际在用的，用上面的指数衰减式。这是优秀底部面板和轮播（Vaul、Embla）的标准行为。

## 7. 空间一致性：对称路径、锚定原点

> "如果一个东西从某条路消失，我们预期它从原路回来。"

- **沿同一条路径进出。**从右侧滑入的面板必须向右侧关闭。右进底出感觉断裂、令人困惑。
- **把交互锚定到源头。**菜单、popover、面板应从触发它的元素长出来：把 `transform-origin` 设到触发元素上，按钮和内容的空间关系一目了然。（和 popover 从触发元素而非中心缩放是同一个原点意识。）
- **可逆过渡镜像缓动**，让去程与回程一致（两个方向用互逆的三次贝塞尔控制点）。

## 8. 沿手势的方向暗示

人从轨迹预测最终状态。中间运动应该预告走向，控制中心模块"朝着你的手指向上向外生长"。让中间帧指向结局，而不是盲目插值。

## 9. 橡皮筋：软边界

到边界处渐进地产生阻力，而不是硬停。硬停读作"冻住了"；连续阻力读作"有响应，但后面没有了"。用户拖得越过头，阻尼越大。

```js
// The further past the bound, the less the element follows — real things slow before they stop
function rubberband(overshoot, dimension, constant = 0.55) {
  return (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot));
}
```

## 10. 手势设计细节（"手感"清单）

- **点按：**touch-*down*（瞬间）高亮，touch-*up* 提交。目标周围加约 10px 的迟滞/命中内边距，允许拖远取消再拖回。
- **拖拽/滑动：**先要求一个小的移动阈值（迟滞，约 10px）再确定方向，然后 1:1 跟踪。
- **从第一次移动起并行探测所有说得通的手势**，意图一明确就果断取消落选者。避开只报告 *最终* 状态的识别器（`swipeleft` 这类事件）：它们丢掉了反馈所需的连续跟踪。
- **把消歧延迟压到最小。**双击检测不可避免地拖慢单击；只在双击真的存在的地方付这个成本。

## 11. 帧级流畅

流畅关乎 *帧里画了什么*，而不只是帧率。

- 让每帧位置变化低于感知阈值，避免频闪。
- 极快的运动用轻微的 **运动模糊/拉伸** 编码速度，比生硬的锐利拖影观感更好。
- `requestAnimationFrame` 是 Web 上与显示器同步的时钟（Apple 用 `CADisplayLink`）。只动画合成器友好的属性，即 `transform` 和 `opacity`，运动将至时用 `will-change` 提示。

## 12. 材质与深度：半透明传达层级

Apple 把半透明材质用作悬浮的功能层，带来结构而不抢焦点。Web 上用 `backdrop-filter` 近似。

- **把导航/工具栏/面板做成半透明层**（`backdrop-filter: blur()` + 半透明背景），内容从下面滚过，而不是占掉一条固定带的实心栏。
- **材质重量编码层级：**更深/更重的材质划分结构区域（侧栏）；更轻的材质把注意力引向可交互元素（按钮）。**绝不要把轻的半透明面叠在另一个上**，可读性会崩。
- **更大的面应该显得更厚：**比小组件更强的模糊 + 更深的阴影。考虑随上下文调整阴影：在密集/文字内容上加重以求分离，在纯色背景上减轻。
- **压暗以聚焦，分离以保流。**模态任务把面板和压暗遮罩配对，把背景往后/往下推。并行、不阻塞的面板用半透明和偏移而 *不* 加遮罩，流程才不断。堆叠面板时，逐层压暗并后推每一层父级。
- **鲜活性（vibrancy）让文字在多变的背景上保持可读。**在模糊/半透明面上，别用平板的灰色文字：提高对比度、字重略加、字距微调。颜色放在实心层上，不要放在半透明前景上。
- **滚动边缘效果，而不是硬分隔线。**别在吸顶头部下画 1px 边框，在内容与悬浮 chrome 相接处淡入一小段模糊/渐变遮罩，且只用在悬浮 UI 真正压住内容的地方。
- **材质化，不要只是淡入。**玻璃/模糊面在进出时同时动画模糊半径和缩放，这个面才像一种真实材料到场，而不只是一次普通的不透明度渐变。

```css
.toolbar {
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  border-top: 1px solid rgba(255, 255, 255, 0.4); /* bright top edge = light catching the material */
}
```

## 13. 多通道反馈：动效 + 声音 + 触感

组合多种感官的三条规则（出自 *Designing Audio-Haptic Experiences*）：

1. **因果**：反馈的起因必须显而易见。在真正的因果事件上触发（开关翻转、元素吸附归位），并让反馈的性质匹配动作的物理感。
2. **和谐**：视觉、声音、触感必须在 **同一帧** 触发。它们之间的延迟会摧毁错觉。别让 CSS transition 拖在音频/触感（Vibration API）后面。
3. **效用**：只在值得的地方加反馈。触感/声音留给有意义的时刻（成功、出错、提交、吸附）。反馈过量会训练用户无视所有反馈。

## 14. 减弱动态与无障碍

减弱动态不是 *没有* 反馈，而是换成更温和、不刺激前庭的等价物。响应三个独立信号并内建进组件：

- **`prefers-reduced-motion: reduce`**：用短暂的不透明度 **交叉淡化或静态过渡** 取代滑动/弹簧/视差。去掉弹性/过冲。保留有助于理解的透明度/颜色变化。
- **`prefers-reduced-transparency: reduce`**：让半透明面更磨砂/实心：提高背景不透明度，去掉模糊。
- **`prefers-contrast: more`**：接近实心的背景加清晰、有对比的边框。

另外：避开全屏移动背景、缓慢的循环振荡（约 0.2 Hz，每 5 秒一个周期）和亮度突变（深↔浅主题切换要平缓）。大的移动物体在飞行途中设为半透明，大幅重定位时先淡出大面、落定后再淡入。

```css
@media (prefers-reduced-motion: reduce) {
  .sheet { transition: opacity 200ms ease; transform: none !important; }
}
@media (prefers-reduced-transparency: reduce) {
  .toolbar { background: white; backdrop-filter: none; }
}
```

## 15. 排版：optical sizing、tracking、leading

Apple 让字体随字号改变形状；同样的纪律适用于 Web。（出自 *The Details of UI Typography*，WWDC 2020。）

- **Tracking（字距）随字号而定，绝不要所有字号一个值。**大号展示文字要 *负* 字距（字变大后间距显得过宽）；小文字要略微 *正* 字距以保证可读。固定的 `letter-spacing` 总在某处出错。标题收紧，正文保持在 `0` 附近。
- **Leading（行高）与字号反向。**大标题紧，正文松。上伸部/下伸部较高的文字加大行高；密集、信息量大的 UI 收紧行高。
- **用字重 + 字号 + 行高作为一组来构建层级**，而不是只靠字号。用字重强调：增加存在感而不多占空间。
- **尊重用户的字号设置**（Dynamic Type）。布局 *随* 文字缩放：间距用 `rem`/`em`，不用固定 px，更大的字体才不会破坏布局。
- **先默认用平台的系统字体**，再考虑自定义字体；它自带 optical sizing、字距表和可读性调优。有理由才覆盖。

```css
:root { font: 100%/1.5 system-ui, sans-serif; } /* body: system font, comfortable leading */

.display {
  font-size: clamp(2rem, 5vw, 4rem);
  line-height: 1.05;        /* tight leading for large text */
  letter-spacing: -0.02em;  /* negative tracking as it grows */
  font-optical-sizing: auto;
}
```

## 16. 设计基础：八条原则

上面的动效与手艺服务于 Apple 的八条设计原则（*Principles of Great Design*，WWDC 2026）。把它们当作你推理用的名词：

1. **目的（Purpose）。**带着意图去造；决定 *不* 建什么。每个功能都在索取用户的时间、注意力和信任，这份预算只花在值得的地方。
2. **掌控（Agency）。**让人保持掌控：提供选择，不强塞唯一路径。配上宽容：失误能轻松撤销；确认对话框只留给真正破坏性、不可逆的操作（少用；滥用会训练人们无脑点过去）。
3. **责任（Responsibility）。**为用户的利益行动。隐私：在正确的时刻询问，只要必需的，保持透明。安全：预判误用与伤害，用 AI 时尤其如此（过敏感知的食谱应用绝不能建议有害配料）。加预览、确认、免责说明；砍掉风险大于价值的功能。
4. **熟悉（Familiarity）。**建在人们已知的东西上。用既不太直白也不太抽象的隐喻（废纸篓意味着删除），并尊重它们的物理。保持一致：看起来相同的东西必须行为相同、待在相同的位置（macOS 上关闭永远在左上角），人才预测得了接下来发生什么。只有在能证明更好时才打破熟悉模式，那就去测试，别想当然。
5. **灵活（Flexibility）。**为不同情境、设备和全部能力范围设计。适配平台（iPhone = 快速点触；桌面 = 精确指针控制下的深度工作流）和情境。包容设计（年龄、语言、专业度、无障碍）。没有一种布局适合所有人时，让人个性化：重排控件，藏起不用的。
6. **简单，而非极简。**剥掉不必要的，让核心目的发光；把一切都埋在一处看起来极简，其实并不简单。简洁（平实语言、无行话、更少步骤）且清晰（用层级：顺序、间距、对比，让最重要的东西最显眼）。每个元素都要挣得自己的位置；有时 *增加* 上下文反而更简单（显示剩余时间的视频进度条）。先展示常见路径，高级选项往下放一层。
7. **手艺（Craft）。**对细节的不妥协建立信任。漂亮的排版、适应深浅模式的颜色、清晰的图标、给出即时自然反馈的响应式动画。没有什么是随机的：每个间距、时序和对齐值都是你能为之辩护的深思熟虑的选择。抖动的滚动、错位的图标、旋转就崩的布局读作敷衍。手艺需要迭代与长寿：功能与硬件变了，设计就继续演化。
8. **愉悦（Delight）。**是把前七条做对的结果，不是顶上贴的彩纸。定下你想让人感受到的情绪（平静、自信、兴奋），在每个决定里强化它。

服务这些原则的战术规则：

- **反馈有四种：**状态、完成、警告、错误。确认有意义的操作，暴露进行中的状态，问题发生前警告，内联校验（不要等提交）。
- **寻路。**每个屏幕都要回答：我在哪？我能去哪？那里有什么？我怎么出去？绝不困住用户。
- **分组与映射。**邻近暗示关联；把控件放在它影响的东西旁边，控件的排布映照它们改变的东西。需要一个标签才能解释控件时，映射就是弱的。
- **直接、具体的标签胜过安全的泛称。**导航项按内容命名（"Progress"、"Library"），不用模糊的大伞（"Home"）。具体制造可预测。

## 17. 流程

- **做可交互的原型，一个可交互的 demo 价值"一百万张静态设计稿"。**你在搭建和把玩中发现界面；能跑的原型还立起一根具体的标杆，挡住平庸的最终实现。
- **交互与视觉一起设计。**"你不该分得清哪里是交互的终点、哪里是视觉的起点。"动效不是像素之后另加的一层。
- **在真实情境中和真人一起测试**，用新鲜的眼光评审动效：慢放 / 逐帧播放，抓出全速下看不见的问题。

## 速查表

| 需求 | 技术 | 具体值 |
| --- | --- | --- |
| 默认 UI 弹簧 | 临界阻尼，无过冲 | `damping 1.0`、`response 0.3–0.4` |
| 动量 / 轻扫弹簧 | 欠阻尼，轻微回弹 | `damping ~0.8`、`response 0.3–0.4` |
| 手势 → 弹簧速度 | 交接松手速度 | 归一化时用 `gestureVelocity / (target − current)` |
| 轻扫落点 | 投射动量 | `current + (v/1000)·d/(1−d)`，`d ≈ 0.998` |
| 干净中断 | 从呈现（实时）值起步 | 读取屏幕上的 transform |
| 避免反转"砖墙" | 改目标时带着速度 | 能混合速度的弹簧 |
| 可逆过渡 | 镜像缓动曲线 | 互逆三次贝塞尔 |
| 决定反转还是提交 | 用速度 **符号**，不是位置 | 松手时 |
| 1:1 拖拽 | Pointer Events + capture | 尊重抓取偏移 |
| 反馈 | pointer-down 时，连续 | 绝不只放在最后 |
| 边界 | 橡皮筋，不硬停 | 渐进阻力 |
| 半透明 chrome | `backdrop-filter` 层 | 内容从下面滚过 |
| 文字字距 | 随字号，从不固定 | 大文字收紧（`-0.02em`），正文近 `0` |
| 减弱动态 | 交叉淡化，不用滑动/弹簧 | `@media (prefers-reduced-motion)` |
