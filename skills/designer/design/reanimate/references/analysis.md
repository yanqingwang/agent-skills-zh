> **中文汉化版** · 上游：[NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate) · 原文件：`skills/designer/design/reanimate/references/analysis.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 读帧与编写动效规格

规格把「我看过了」变成可以逐行核对的表格。先写规格，再动手实现；验证中发现问题就更新它；用户问「匹配上了吗」时，先把这份东西给他看。

## spec.md 模板

```markdown
# <name> motion spec

Target: <url + selector | file + time range>   Viewport: 1440x900   Fps: 25
Destination: <path/Component.tsx> (<stack: React + Framer Motion | CSS | GSAP …>)
Fidelity: motion-faithful | pixel-faithful | mixed (additions: …)
Reference capture: .reanimate/<name>/ref  (command: …)

## Structure (static)
| element | role / selector (ref → clone) | box at rest (x,y,w,h) | notes (overflow, z-index, origin, clip) |

## Timeline (t=0 is the trigger)
| # | element | property | from → to | start ms | duration ms | easing | stagger / repeat | source |
| 1 | h1 | opacity | 0 → 1 | 200 | 700 | cubic-bezier(.16,1,.3,1) | – | inspect.json |
| 2 | h1 | translateY | 40px → 0 | 200 | 700 | same | – | inspect.json |
| 2b | canvas card | three:Card.rotation.x | 0 → 0.26 rad | 30 | 630 | ease-in-out (lag 0.004/ms) | follows pointer | gl-track.json + easing.ts --channel |
| 3 | p | opacity, translateY | 0→1, 30px→0 | 400 | 700 | same | +200 ms after h1 | track.json + easing.ts |
| 4 | .cta | opacity, translateY | 0→1, 24px→0 | 600 | 600 | same | +200 ms | frames #15–#30 |

Trigger: load | enters viewport (threshold ~25 %) | hover | click | scroll-linked (0–600px) | loop every N ms
Total length: <ms>   Last visible change: <ms>

## Style facts needed for the motion (and everything, if pixel-faithful)
fonts, sizes, colours, radii, shadows, gaps, assets (with URLs or where copied)

## Additions (mixed only)
what is new, where it lives, how it is kept out of the compared region or why it does not affect timing
```

## 数字从哪里来

1. **`inspect.json › animations`**（带有 CSS/WAAPI 动效的网站）：`timing.delay`、`timing.duration`、逐关键帧的 `easing`、`iterations`、`direction`。过渡会以 `CSSTransition` 出现，带 `transitionProperty`。照抄这些数值。
2. **`track.json` + `easing.ts`**（网站，任意技术栈）：按元素、按属性打印延迟、可见时长、过冲，以及拟合最好的具名缓动和它拟合出的时长。对每个运动元素、每个属性（`translateY`、`opacity`、`scale`、`x`、`w`…）都跑一遍。过冲 > 2 % 说明是弹簧或 back 缓动；记下过冲百分比和稳定时间，实现说明里讲了怎么映射。
3. **`gl-track.json` + `easing.ts --channel`**（canvas、WebGL、3D，用 `--gl` 抓取）：逐渲染帧的 uniform 和场景图数值（相机、对象变换、材质 uniform）。`gl.ts summary` 按类型（`clock`、`transition`、`there-and-back`、`oscillation`、`steps`）列出有动画的那些，附变化窗口；固定不变的 uniform 是常量，原样照抄。见 `references/webgl.md`。
4. **帧**（视频、gif，以及没有 trace 时的 canvas）：对每个元素找出它第一次变化的帧和最后一次变化的帧；`start = first/fps`，`duration = (last − first + 1)/fps`。从中点落在哪里判断缓动：若在时长的三分之一处元素已走过一半以上距离，就是 ease-out；不到四分之一，是 ease-in；对称，是 ease-in-out；等距台阶，是 linear。越过终点再回弹：back/spring。即使没有 track，`compare.ts` 也会逐组打印活动曲线，用条形把这些形状显示出来。
5. **Stagger**：兄弟元素起始帧之间的间隔。记下它是常量（每个 +80 ms）、递增（stagger 上带缓动），还是逐字符/逐词（文字揭示）。

## 值得认出来的模式

落地页动效大多逃不出这些；叫出名字能省下好几轮。

| 模式 | 特征帧 | 典型数值 |
|---|---|---|
| fade-up stagger | 兄弟元素一边淡入一边上移 16–48 px，逐个稍晚 | 500–800 ms，ease-out-expo/quint，stagger 60–150 ms |
| text reveal（行、词、字符） | 各片段按顺序出现，常被行盒裁切（`overflow: hidden` 包裹层） | 600–1000 ms，逐片段 stagger 20–50 ms |
| clip/mask reveal | 内容沿一条边揭开，没有淡入 | 800–1200 ms，ease-in-out，`clip-path: inset()` |
| scale-in（弹窗、菜单、卡片） | 从 0.9–0.96 放大并淡入，transform-origin 在锚点 | 150–250 ms，ease-out |
| hover lift | 卡片上移 2–8 px，阴影变大 | 150–300 ms，ease-out；反向用更短或相同时间 |
| marquee | 复制一行的连续 translateX | linear，周期 10–40 s，循环；量周期，不要量缓动 |
| scroll-linked | 只在滚动时变化，停下就停 | 绑定 `scrollY` 区间；读 `track.json` 里的 scrollY 对 value |
| pinned section | 页面滚过时元素保持固定 | 某段滚动范围内 `y` 恒定 |
| parallax | 各层按滚动增量的不同比例移动 | 形如 0.2 / 0.5 / 1 的比例 |
| count-up / typewriter | 数字或字符逐帧变化 | 时长加上作用在值上的缓动 |
| spring | 过冲后稳定，有时两次 | 刚度/阻尼；见实现说明 |
| loader / skeleton pulse | opacity 或渐变位置来回振荡 | 周期 1–2 s，ease-in-out，infinite alternate |
| page transition | 旧视图退出、新视图进入，常带共享元素 | 300–600 ms，退出比进入短 |
| shader clock | 一块永不静止的 canvas；`u_time` 之类的 `clock` 通道 | 它的速率（+1000/s = ms，+1/s = 秒）和使用它的着色器 |
| uniform tween | 某个 uniform（`u_hover`、`u_progress`）上的 `transition` 通道 | 时长和缓动同普通 tween；着色器把 0→1 映射到像素 |
| pointer lag（WebGL） | 某个值追着指针跑，移动越长越慢 | 逐帧或逐 ms 速率 `k`；`x += (target − x)·k` |
| keyframed model（glTF） | `gl.ts summary` 里的一个 `AnimationMixer` | clip 名、时长、loop、timeScale：播放同一段 clip |

## 怎么读一张帧表

- 顺着时间戳标签逐行看。逐个元素记下它第一次动的帧和停下来的帧。每个元素都要做，不能只挑最大的那个。
- 比较相邻帧：前面跳一大截、后面小变化 = ease-out；先小后大 = ease-in。
- 留意容易漏掉的东西：淡入的背景、变大的阴影、收紧的字距、消掉的模糊、出现的边框、旋转的图标。它们都是动效的一部分。
- 记下**不动**的东西。参考里保持静止的元素，克隆里给它加了动画，一样算失败。
