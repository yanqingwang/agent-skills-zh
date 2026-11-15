---
name: Hum
slug: hum
genre: playful
paper: light 97 95
display: rounded-sans Chillax
accent: chromatic-yellow 95
posture: full-palette
keywords: daily, habit, streak, practice, learning, reading, curiosity, mood, energy, friendship, community, kids, family, parents, school, game, puzzle, creative, playful, alive
material: grained cream paper pulled toward pear-yellow, torn paper edges with a pale fibre core, card-stock controls that press down, blue-black ink, Chillax throughout, three accents that never blend and a mint for growth
photo: natural vib=12 exp=4
pictured: Workbench, Settled hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/hum.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Hum

手工剪出的纸，欢快而不幼稚：可见纹理与纤维的奶油纸，纸页沿边缘撕开、露出浅色纸芯，可以按下去的卡纸控件，全部从左上方打光。Chillax 从标题一路用到标签（它的单层 a 与 g 读起来像启蒙读物的一页），墨水是蓝黑。三个强调色绝不混色：梨黄给动作，蓝给链接，珊瑚红给一个响亮的时刻；薄荷绿是成长。不是粉彩育儿模板，不是彩虹页，也不是剪贴画图库。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(97% 0.012 95); --color-paper-2: oklch(94.5% 0.018 95); --color-paper-3: oklch(91% 0.022 95);
  --color-ink: oklch(20% 0.014 255); --color-ink-2: oklch(29% 0.014 255); --color-muted: oklch(47% 0.014 255);
  --color-rule: oklch(87% 0.016 95);
  --color-accent: oklch(87% 0.175 96); --color-accent-deep: oklch(72% 0.16 92); --color-accent-ink: oklch(20% 0.014 255);
  --color-accent-2: oklch(50% 0.17 250); --color-accent-3: oklch(70% 0.2 22);
  --color-mint: oklch(82% 0.15 152); --color-mint-deep: oklch(48% 0.12 155); --color-focus: oklch(50% 0.17 250);
  --color-card: oklch(98.8% 0.007 95); --color-edge: oklch(83% 0.04 88); --color-fringe: oklch(99.2% 0.006 95);
  --color-kraft: oklch(63% 0.085 62); --color-sand: oklch(77% 0.1 76); --color-sugar: oklch(89% 0.035 236);
  --color-hill-1: oklch(94.5% 0.03 118); --color-hill-2: oklch(91.5% 0.045 135); --color-leaf: oklch(64% 0.15 150);
  --font-display: "Chillax", ui-rounded, ui-sans-serif, sans-serif; --font-body: var(--font-display);
  --font-outlier: "Geist Mono", ui-monospace, monospace;
  --radius-card: 24px; --radius-stock: 16px; --radius-input: 14px; --radius-pill: 999px; --rule-hair: 1px;
  --shadow-card: 0 1px 2px oklch(20% 0.014 255 / 0.06), 0 12px 28px -14px oklch(20% 0.014 255 / 0.22);
  --shadow-paper: drop-shadow(0 0 0.6px oklch(20% 0.014 255 / 0.32)) drop-shadow(1.5px 2.5px 1.5px oklch(20% 0.014 255 / 0.1)) drop-shadow(6px 14px 16px oklch(20% 0.014 255 / 0.13));
  --tracking-display: -0.03em; --display-weight: 600;
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1); --ease-snap: cubic-bezier(0.22, 1, 0.36, 1);
}
```

## 字体（Type）

- **展示字体：**Chillax 600，`--tracking-display`，行高 1.02 至 1.05，句首大写。数字排到 `--text-display` 或更大，其单位用 `--text-title`。
- **正文：**Chillax 500，17 至 19px，行高 1.5；强调是文字背后一条梨黄荧光笔带，绝不放进标题。两个字重，500 与 600。
- **标签、图注、单位：**Chillax 500 小一档，句首大写，用 `--color-muted`。Geist Mono 只在代码里。

## 表面（Surfaces）

- 纸是生成的，绝不是图片：两条 `feTurbulence` data URI，细颗粒 fractal grain（`--grain`）与长条湍流纤维（`--fibre`），垫在每张纸、每张卡与每个强调填色之下。
- 撕边：一条色带、一条导航栏、一张照片或一张纸，以带种子的值噪声 `clip-path` 多边形收边，其纤维孪生（`--color-fringe`）在下方凸出一像素。地面可以分层：远山用 `--color-hill-*`，土壤用 `--color-leaf`，一条牛皮纸条，一张蓝色糖纸垫。
- 光从左上来：层叠的 `--shadow-paper` 投影在每个剪出的纸面上向右下落；一张卡可以掀起一角，像卷页。
- 处处圆：24px 表面（儿童场景 28 至 32px），16px 卡纸，没有直角。
- 色带：paper-2、撕开的墨色纸配纸色文字，或一块梨黄色场。每页至多两条。
- 照片：儿童高度取景的明亮日光，绝不正对镜头的脸；一边撕边，每页一或两张。

## 版式（Range）

- **产品化作卡纸：**应用自己的时刻放大呈现，文字做成卡纸贴片压在撕开的牛皮纸条上，每按一下弹进自己的强调色。
- **成长用文字表现：**一片由 Chillax 字形组成的植物（茎是 l、叶是括号、字头是花）长在撕开的土壤上，随提示词的数字长满，一排胶囊按钮切换它的状态。
- **梨黄色场上的数字：**提示词的三四个数字排展示字号，墨色印在一张梨黄纸上，每个单位在下方用 500。
- **选择化作卡纸胶囊：**提示词事实之上的可用控件，结果是一句话，其关键值压在梨黄荧光笔带里。

## 控件（Controls）

- 卡纸：54px 控件、`--radius-stock` 圆角，填色带颗粒与纤维，顶部一圈内嵌高光、底部一圈实心 5px 边（梨黄主按钮用 `--color-accent-deep`，次卡用 `--color-edge`）；悬停把边抬到 7px，按下压到 1px。弹簧缓动只用在主按钮上。
- 每个强调色只管一件事：梨黄管主按钮与唯一一块梨黄色场；蓝管链接与焦点环；珊瑚红管一次响亮的填色；薄荷绿管成长。选中的胶囊是墨色配纸色文字。一枚模切贴纸可以承载报价。
- 输入框：14px 圆角，52px 高，1px `--color-muted` 边框，蓝色焦点环。

## 动效（Motion）

声明弹簧姿态（gate 12）：`--ease-spring` 只用在主控件；其余全部 `--ease-snap`，绝不用 `scale()`。一个词弹进自己的强调色，一棵植物生长；计时器运行时可以撕下一角纸，暂停在屏幕之外。Reduced motion（减少动效）或无脚本：呈现最终状态。

## 语气（Voice）

温暖、聪明、随意、直接，写给孩子身边的大人。句首大写，动词优先于名词，只用诚实的数字。

## 禁止事项（Do-nots）

- 绝不用衬线，绝不用纯白纸，绝不用直角。
- 绝不给剪出的纸用干净的矢量边，也绝不让影子向上或向左落。
- 绝不在两个强调色之间做渐变，绝不用彩虹地面。
- 绝不用 emoji、素材图标或画出来的角色；文字、纸与产品自己承担。

## 构建提示（Build hint）

```html
<link href="https://api.fontshare.com/v2/css?f[]=chillax@500,600&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: var(--display-weight); }
.btn { --edge: 5px; border: 0; border-radius: var(--radius-stock); min-height: 54px; padding: 0 var(--space-lg); font-weight: 600; background: var(--grain), var(--fibre), var(--color-card); box-shadow: inset 0 0 0 1px var(--color-rule), 0 var(--edge) 0 0 var(--color-edge); transition: translate var(--dur-micro) var(--ease-snap), box-shadow var(--dur-micro) var(--ease-snap); }
.btn--primary { background: var(--grain), var(--fibre), var(--color-accent); color: var(--color-accent-ink); box-shadow: 0 var(--edge) 0 0 var(--color-accent-deep), 2px calc(var(--edge) + 4px) 10px -3px color-mix(in oklab, var(--color-ink) 32%, transparent); transition-timing-function: var(--ease-spring); }
.btn:hover { --edge: 7px; translate: 0 -2px; } .btn:active { --edge: 1px; translate: 0 4px; }
.sheet { position: absolute; filter: var(--shadow-paper); } .sheet > i { position: absolute; inset: 0; background: var(--grain), var(--fibre), var(--sheet-c, var(--color-paper-3)); }
mark { background: color-mix(in oklab, var(--color-accent) 55%, transparent); color: inherit; box-decoration-break: clone; }
a { color: var(--color-accent-2); }
```
