> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/taste-skill/references/motion.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 动效

每个页面都要加载微交互层：`<html data-motion>`，`assets/motion/motion.css` 紧跟 `ui/cards.css` 之后，
`assets/motion/motion.js`（module）紧跟 `system.js` 之后（`starter.html` 已备齐三者）。**这不是可选项：**
绝不删除、跳过或覆盖它；检查项对它有意见时，改标记结构，而不是改这一层。
悬停层缺失或不可见，在任何品类都是扣分项（C 轮：一个金融科技页、一个咖啡馆页和一个民宿页
都因悬停卡片或按钮毫无变化丢了动效分），自 2.5.1 起缺首屏入场或缺派发时刻（dealt moment）的页面同样扣分。
给它可作用的标记结构：带链接的卡片是包住链接的 `.card`（绝不用 `.m-nolift`），
会带人去别处的照片用 `<a class="m-zoom">` 包住它的 `<img>`（或在已链接的 frame 里用 `img.frame__img`），
按钮是 `.btn`，正文里的链接是 `.link`。
在 1440 下截一张悬停中的卡片和一张悬停中的照片，确认它们变了：卡片上移 2px，照片 1.03。
`assets/motion/demo.html` 演示了所有交互。
本文件收录全部悬停、按压、循环与 reduced motion 数值；其他文件都指向这里。

## 规则：每个页面都动，只在这三处

每个页面、每个品类，都有同样的三层动效，此外什么都不动：

1. **首屏入场**：加载时播放一次（见下文）：h1 逐行出现，随后是导语和按钮，
   图片落定。约 1.1 秒，之后首屏静止。
2. **一个派发时刻**，放在一个专属区块里（长页面上两个：八个区块及以上），
   要大到让人记得住：由 `moments.mjs pick --page <kind>` 派发（`moments.md`）。
   place、product、service 页面上以照片或文字为主
   （照片原地变化、一张照片逐渐显影、一句宣言亮起）；
   shader 与 WebGL 效果只留给 tech、gaming、software
   （本库规约 8：咖啡馆、烘焙店、民宿或商店用照片，不用 shader）。
3. 下文的**悬停与按压层**，作用于每个链接、按钮、带链接的卡片和带链接的照片，
   以及点击或轻触引发的切换（software 页的标签页、peek-list 的照片）。

tech、gaming、software 页面另加：卡片视觉内的循环（含示意图脉冲）、
首屏或 `[data-visual]` frame 里的一个定时循环、一个计数，
以及 `effects-usage.md` 派发的效果与场景。其他页面一概没有：
没有跑马灯（ticker）、走马灯（marquee）、幻灯片、循环图片、脉动圆点或计数。
“营业中”一行可以在加载时点亮一次；没有它，面板照样读得通。
产品渲染图默认是静帧；只有被要求时才动（`data-product-mode="live"`），
至多一个动态场景，角落配暂停按钮，手机端与 reduced motion 下仍为静帧（`effects-objects.md`）。

**滚动只动派发时刻，别的什么都不动。** 没有任何卡片、行或方块随页面滚动淡入、升起或错落入场
（套路 reveal），没有任何文字以不同于页面的速度移动（文字视差），
页面也绝不被脚本按住或操纵（scroll-jacking、平滑滚动库）。
某个时刻可以用 `position: sticky` 把自己的区块按在屏幕上，页面本身照常原生滚动。

**为什么动。** 计划里为每个动效写明用途，一行一条：“首屏入场：名字先到，再告诉访客做什么”；
“Rooms 照片章节：一屏空间看三间房”；“悬停：每个链接都有回应”。
没有用途的动效砍掉。
内容在静止时、无脚本时、reduced motion 下都必须可读：
动效只给一个本来就完整的页面做加法。

## Token

`--m-in` 150ms（悬停进入），`--m-out` 120ms（悬停离开），`--m-press` 90ms，`--m-panel` 200ms（菜单展开），
`--m-close` 120ms，`--m-slide` 240ms（指示器移动），`--m-image` 进入 600ms、`--m-image-out` 400ms，
`--m-cycle` 3.2s；tech 循环 token：`--m-roll` 700ms，`--m-count` 1000ms，`--m-level` .6s，`--m-bob` 3.2s。
曲线：UI 只用一个 ease-out，`system.css` 的 `--ease` = cubic-bezier(.2,.8,.2,1)（`--m-ease` 与
fragments 的 `--u-ease` 都读它），用于每个 UI 步骤；
`--m-ease-enter` cubic-bezier(.22,1,.36,1) 用于入场落定
（首屏、派发时刻、数字滚动；`ui/base.css` 的 `--u-spring` 是同一条曲线）；
`--m-ease-io` cubic-bezier(.65,0,.35,1) 只用于位移；循环与漂移用 linear。
任何曲线都不过冲：不回弹、不越过目标。动效层只动 transform、scale 和 opacity
（悬停还可改颜色），绝不给 width、height、top、left、margin、padding 加动画。
派发时刻内部另有几个廉价属性可动，逐一写进各自的 `meta.json`：
clip-path（擦除）、filter（照片显影）、文字颜色（宣言亮起），
以及仅 tech 可用的 background position（照片从文字中穿过）。距离：卡片抬升 2px，
照片缩放 1.02 到 1.03，箭头 3px，菜单下落 6px，按钮上移 1px（`.btn--xl` 为 2px；`arrow` 与 `block` 两种按钮样式的文字链接次级按钮不动），
按压下沉 1px 并缩放 .985（那个次级按钮：只缩放）；其余一律不许（`assets/motion/motion.css`，buttons 节）。

## 悬停层

悬停动效只对精确指针生效（`(hover: hover) and (pointer: fine)`；键盘焦点在任何地方都呈现同一状态）；
每个悬停控件同样支持轻触与键盘，并有焦点态；任何东西都不改变尺寸、不推挤邻居；
不许 rotate、skew、发光、扫光或标签滑行。

| 部件 | 动效 | 时长 |
|---|---|---|
| 按钮 | 悬停时底色向墨色推进 14%（outline 按钮获得淡底色和更深的边框），盒子整体上移 1px（`.btn--xl` 为 2px）；按压下沉到静止位以下 1px 并缩放 .985，这样悬停截图与按压截图各有一处变化；`arrow` 与 `block` 两种按钮样式的文字链接次级按钮保留下划线、不位移（其按压只缩放 .985）；仅限精确指针；页面 CSS 绝不设置 `.btn` 的 `transform` 或 `transition` | 150ms 进入，120ms 离开，90ms 按压 |
| 箭头 | `svg.m-arrow` 右移 3px 后回落；全页只用一种箭头样式 | 150 / 120ms |
| 链接 | 常规字重只一种下划线样式：正文与 `.link` 静止时压一条淡 1px 发丝线，悬停时一条墨色线从左向右画出、离开时向右收回；导航和页脚的字静止时无线，悬停变深并在字下 4px 画出 1px 线 | 150 / 120ms |
| 导航 | 文字使用画出的下划线（任何品类都不用滑动胶囊）；悬停意图满 150ms 后面板才展开，以 6px 下落淡入，各栏一起出现（一个表面，绝不一栏接一栏），120ms 收起；一个面板开着时，下一个词立即切换；tech 上箭头旋转 180 度，其他品类立即翻转 | 200ms，120ms |
| 当前页 | 导航词下方一条 2px 短杠（`aria-current="page"`） | 静止 |
| 标签页（software，仅点击触发） | 指示器仅靠 transform 滑到被点的标签页（尺寸立即变成新标签页的，起始缩放成旧标签页的形状，然后落回 scale 1）：墨色胶囊由 `system.css` 画出，标签文字用底色；面板切换（至多 200ms）；每个面板高度固定；其他品类没有标签页 | 240ms |
| 带链接的卡片 | 抬升 2px，边框加深一档，可选柔和阴影（模糊 24px，墨色不超过 10%，仅悬停时） | 180ms 进入，120ms 离开 |
| 不带链接的卡片 | 无动效（`.m-nolift`） | |
| 带链接的卡片或链接里的照片 | 在其 frame 内缩放 1.02 到 1.03（frame 设 `overflow: hidden`）；frame、卡片和盒子绝不变大；绝不变暗、淡出或加盖遮罩；产品卡片的名字随之下划线（其他包裹用 `.m-zoom`） | 600ms 进入，400ms 离开 |
| 焦点 | 行动色 2px 焦点环，距控件 2px，焦点落下的那一帧就完整画出；无过渡 | 无 |
| 输入框 | 行动色边框加 3px 柔和焦点环 | 140ms |
| `.m-switch`、`.m-check`（tech） | 按住时滑块位移 16px 并拉伸 4px，都靠 transform；对勾从 70% 长到全尺寸时淡入；其他品类直接跳变 | 180, 90, 160ms |
| 复制按钮（tech） | 图标原地换成对勾，停留 1.5 到 2 秒，再换回来 | 150ms |

FAQ 全部答案默认展开（`system.css`）：不做手风琴，
绝不给 height、max-height 或 padding 加动画。
钩子：`[data-m-loop]`（自己的 CSS 循环，tech）、
`data-ui-loop`（一个卡片组的一个 fragment 循环，tech）、`data-m-count`（仅 tech 首屏）、`.m-link`、`.m-zoom`、`.m-nolift`。

## 首屏入场（所有品类）

加载时入场一次，之后首屏就静止：h1 从词遮罩中逐行升起
（每行 700ms，各行间隔 80ms，首行到末行至多 240ms；每个词起初完整藏在遮罩下），
随后它所在列里其余内容（导语、每个按钮、事实信息）各上浮 12px、各 520ms、间隔 60ms，
从末行升到一半时开始；h1 之上的一行（通知、胶囊标签）随第一行一起出现。
首屏图片绝不隐藏、绝不淡入：照片在 frame 内用 1.1 秒从 1.05 落到 1（首屏内的通栏照片也是），
窗口、物件或拼贴用 900ms 从 .98 落定，各作为一个整块出现
（菜单卡片上的字或其中的便签绝不自行分步出现）；
文字所在的面板从首帧绘制起就立在那。全部约 1.1 秒，ease-out（`--m-ease-enter`），
只用 transform、scale 和 opacity，每次访问一次，滚动时绝不重播。
被 `layout.js` 改造过的 h1（live word、响应指针的字母、行内嵌图）整块升起，不逐行。

构建者只写两处，别的都不写（`starter.html` 两处都有）：

```html
<!-- in <head>, after the stylesheets (where starter.html has it): the words wait for motion.js instead of flashing -->
<script>document.documentElement.classList.add('m-enter');setTimeout(()=>document.documentElement.classList.add('m-enter-done'),700)</script>
<!-- on the dealt hero's section -->
<section class="hero hero--split" data-enter aria-labelledby="hero-h">
```

可选：首屏图片不属于任何布局自带类（`.hero__bg`、`.hero__media`、`.hero__stage`、`.hero__art`、
`.hero__window`、`.hero-visual`、`.ly-collage`）时，给它加 `data-enter-media`；
必须整体升起的 h1 加 `data-enter-whole`；
自带大场景加载动效的首屏加 `data-enter="off"`
（检查器把该场景当作入场，且只认这类首屏内部的场景）。
其余交给 `motion.js`（`enter()`）：入场期间借给 h1 词遮罩，
结束后把 h1 自己的节点还回去（运行中加 `.is-entering`，结束后 `.is-entered`）。
只有文字被隐藏，且只在 `html.m-enter` 开着、`motion.js` 接管之前或 700ms 期限未过时：
无脚本、reduced motion、打印和 `data-motion="off"` 时，首屏按写好的样子静止显示；
脚本晚于期限时，文字用 400ms 淡入，图片仅靠 CSS 落定。
无头截图看到的是静止的首屏（正如它看到计数的最终数字），除非 `<html data-motion="live">`。
绝不放加载器、门禁、阅读前的延迟，也不做第二次入场（`headline-arrives` 因此退役）。

## 卡片视觉内的循环（tech）

本库规约：节奏稍快，且重复播放。

- 一个周期 2.5 到 4 秒（`--m-cycle`，默认 3.2 秒），然后重新开始。循环以成品画面为种子，绝不出现空窗口：
ui.js fragment 在第一个周期前先在成品画面上停 600ms；`[data-m-loop]` 立即开始；
每个周期的最后 10% 到 15% 固定显示成品画面，重置时变暗重写，绝不留白。
- 指针或键盘焦点进入卡片时，循环从头重放（进入后前 800ms 内除外）。已暂停的循环保持暂停。
卡片、它的面板和窗口绝不移动：窗口内不缩放、不倾斜、不运镜。
- 每周期一个主题（指针点击、状态翻转、进度条充满、写出一条线）：每 1 到 2 秒一个变化，
每个变化不超过 300ms。主题有多个时，每周期推进到下一个。
变化中的标签绝不同时显示两个词。
- 每个卡片组一个 fragment 循环（`data-ui-loop`）；组内其他 fragment 保持成品画面，
指针停在各自卡片上时才播放。小示意图卡的脉冲是该卡自己的循环，
遵守同样的周期、重放与暂停规则（本库规约：脉冲沿线跑）；
system.js 绝不替它暂停（`data-ui-still` 管不到示意图）。
首屏之下，一块屏幕上绝不同时出现两个循环：
带脉冲示意图的组，给其余 fragment 也加 `data-ui-still`，
或用 `data-dg-still` 按住示意图（此时指针悬停才播放）。
- 页面自己的 CSS 循环放进 `[data-m-loop]`，所有关键帧以 `var(--m-cycle)` 计时，
`--m-still`（0 到 1）为成品帧，留出一条 48px 的带（`--m-safe`）给暂停按钮。
- 活动迹象只出现在循环视觉内部：spinner 1 秒（12 到 16px，完成后变对勾）、
live dot 2.4 秒（点不动，环长出又消散）、输入框内 1 秒硬切换的光标、进度条 .6 秒。
不要打字圆点、其他位置不要孤零零的脉动圆点、标题后不要方块光标。
- 卡片故事的种类（各自装在固定高度的盒子里）：提示词以每秒 12 到 20 字符打出后停住；
回答约每秒流出一个气泡；新通知从顶部进入，最旧的经淡出离开；
清单约每秒勾一项；日历事件逐个淡入；
指针约 1 秒滑行 200px，按下（scale 至少 .96，配 28px 圆环）并保持。
发言人或头像前排条目至多每 3 秒换一次。图表保持静止。
- 尚未落地、因此不用的：步进的槽位条、前后对比分隔条、沿路径行进的元素、
会变宽的 dock 标签、跟随指针的吉祥物、沿首屏线条跑的彗星。

## Tech 预算

- **一个定时循环**：每页一个，放在首屏或 `[data-visual]` frame，形式不限
（故事、胶片卷、发光边框、动态底景、旋转物件、走马灯）；
它的活动迹象算作它的一部分。一个定时循环至多再配一个效果；
首屏里有动态效果时，不再跑其他定时循环。
一个 900px 窗口内绝不出现两个自行动的东西，一个面板内绝不出现两个循环。
卡片循环（每组一个）、示意图脉冲（每张示意图卡一个）和派发时刻不在此计数内。
- **一个计数**：每页一次（`data-m-count` 或 `counter-rolls` 时刻，二者绝不并用）：
加载时在首屏（1000ms，至多 1.2 秒），或作为派发的计数时刻放在专属区块。
放在开放地面上，绝不放进卡片、面板或 `[data-visual]`；预留宽度；
最终数字写进 HTML，reduced motion、无脚本和手机端都直接显示；
绝不用年份、价格或电话号码。动态计数器只变换最后一位到三位数字。
- **加载：**所有品类都有上文的首屏入场。tech 另允许 `[data-visual]` frame 内至多一个一次性加载动效
（视觉组装起来，600 到 1200ms），1.5 秒内落定；
点击切换 400 到 600ms。不做门禁、加载器或片头。
- **暂停：**出现 5 秒后仍在动的东西，每个面板配一个圆形暂停按钮：
实心 32px 圆盘，距右下角 12px（卡片里放在标题旁），
常显或悬停与聚焦时淡入，每张卡片同尺寸同位置，
绝不压住文字，静止物上不放。
点击即冻结画面并换成播放图标（自己的运动体用 `ui.pausable(panel, ctrl)`）。滚动驱动的时刻不需要。
- **定时循环随加载启动**，绝不因滚动启动、停止或恢复；IntersectionObserver 只用于懒挂载。
canvas 只能按加载起点的时钟跳过屏幕外的绘制，返回视口时不得露出可见的启动过程。
隐藏标签页可以全部暂停。

## 滚动

- **派发时刻所在区块（及 tech 页的大场景）之外，所有品类：**滚动不触发任何动画。
没有任何卡片、行或方块的 reveal（淡入、升起、错落、遮罩擦除），
没有视差或漂移，没有 scroll-snap、随滚动变色的底景、
进度线、scroll-spy 标记或入视口计数。
- **所有品类：**那一两个派发时刻可以跟随滚动，各自放在专属区块里（`data-moment`；
tech 上大场景也算，`data-big-scene` 配 `{"hold": 1}`），
区块保持 1H 或 2H 高（`scenes.md`，Its height 一节；`photo-chapters` 动态时为 3H 或 4H，
每章约占三分之二屏，`moments.md`），只在该盒内用 `position: sticky` 钉住。
滚动时刻被滚动条擦洗（向上滚会倒放），两端都呈现完成态；
入场时刻（`picture-develops`）只播一次，1.6 到 1.8 秒。
它的文字在无动效时也实时可见（opacity 1，每一步都保持 4.5:1）；
reduced motion 与无脚本时显示成品静帧；
手机跑轻量款（`word-highlight`、胶片显影、`photo-chapters`：只用 transform、clip、filter 或颜色，
不用 WebGL），其余拿到静帧；`perf.mjs` 通过。
它绝不移动卡片、照片、定价、FAQ、引述块或页脚。
驱动方式用原生 `animation-timeline`、每帧把被动读取的滚动值写入自定义属性，
或把 GSAP ScrollTrigger 限定在该区块且不用 pin（仅 tech）。
任何页面都不用平滑滚动库（Lenis、Locomotive、ScrollSmoother），其他品类连动画库都不用：套件里的时刻不需要。
- 头部与手机底栏在任何滚动位置都长一个样；
底栏只在首屏按钮滚出屏幕后升起，屏幕停在它的某个动作上时又落下去
（system.js，240ms，reduced motion 下即时切换）。

## Reduced motion、无脚本、手机

颜色照常变化；菜单淡入淡出；按压表现为颜色加深而不是位移；
标签页指示器与开关滑块直接跳到位；对勾以全尺寸出现；下划线直接出现、不滑动
（`motion.css` 的 reduced motion 部分：链接、`.m-tab-ind`、`.m-switch::before`、
`.m-check::before` 的 `transition-property` 只限 opacity 和颜色）。
首屏按写好的样子静止。
每个循环、效果、时刻和场景显示成品帧，走马灯停成一排静帧，数字显示最终文本，暂停按钮隐藏。
手机上卡片循环与效果保持成品画面或海报帧，重型 canvas 变成静帧，
没有悬停态、没有指针模拟；首屏仍然入场，
足够轻的手机款时刻照常运行（`moments.md`，The still rule 一节），
因此手机页面同样在两处动。

## 永不

- 随页面滚动 reveal、错落、滑入或淡入的卡片、行或方块；文字视差；
派发时刻区块（及 tech 页场景）之外的滚动擦洗；
place、product、service 页面上的 shader 或 WebGL 时刻。
- 每个区块标题都升起；第二次首屏入场；超过约 1.1 秒的入场；
或把访客本已在读的文字藏起来的入场。
- 倾斜、翻转、缩放、跟随指针或在光标处发光的卡片；磁吸按钮。
- 轮播（carousel）、自动前进的滑块、定时切换的标签页、轮转公告、logo 走马灯。
- 随机闪烁：闪烁圆点、亮片、频闪、色相循环、乱码文字；
每次变化都必须呈现一个状态、一个步骤或真实数据。
- 只播一次的循环（卡片故事的重放除外）；卡片循环周期超过 4 秒；
一个面板里两个循环。
- 比其 token 更慢的悬停；过冲缓动；按钮反应前的延迟；带动画的焦点环；
第二种下划线或指示器样式；带动画的 width、height 或 margin。
