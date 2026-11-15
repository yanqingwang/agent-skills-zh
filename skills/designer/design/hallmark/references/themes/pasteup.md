---
name: Paste-up
slug: pasteup
genre: playful
paper: mid 73 70
display: display-condensed League Gothic
accent: chromatic-yellow 112
posture: committed
keywords: zine, fair, market, festival, print fair, book fair, exhibitors, punk, diy, collective, gig, poster, workshop, night market, flea, indie, community, launch, loud, photocopy, flyer
material: kraft board, a fibre wash, near-black toner, League Gothic capitals over a Newsreader galley, white copy paper on paper lifts, hard ink offsets, one sheet of fluorescent yellow
photo: mono con=45
pictured: Bento Grid, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/pasteup.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Paste-up

一张手工传单：牛皮纸板、近黑碳粉、海报字号的 League Gothic 大写压在 Newsreader 长条校样上，真实的纸张投影托着白色复印纸，控件压在硬质油墨偏移上，一张荧光黄纸。照片从复印机里出来，黑白，灰阶压死。拼贴感活在纸面、倾角与浮起里，绝不在道具里。它不是一套脏污纹理素材包，不是贴纸与胶带的剪贴簿，也不是干净的现代海报。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(73% 0.068 70); --color-paper-2: oklch(66% 0.072 68); --color-paper-3: oklch(97% 0.008 90);
  --color-ink: oklch(17% 0.01 60); --color-ink-2: oklch(24% 0.014 60); --color-muted: oklch(28% 0.026 62);
  --color-rule: oklch(50% 0.055 68); --color-rule-2: oklch(84% 0.012 85);
  --color-accent: oklch(93% 0.2 112); --color-accent-ink: oklch(17% 0.01 60); --color-focus: oklch(17% 0.01 60);
  --font-display: "League Gothic", Impact, sans-serif; --font-body: "Newsreader", Georgia, serif;
  --radius-card: 0; --radius-pill: 999px; --rule-hair: 1px;
  --shadow-card: 0 1px 0 oklch(18% 0.01 60 / 0.2), 0 4px 10px oklch(18% 0.01 60 / 0.12);
  --shadow-sheet: 0 14px 30px oklch(18% 0.01 60 / 0.26), 0 2px 4px oklch(18% 0.01 60 / 0.14);
  --tracking-display: 0.01em; --display-weight: 400;
}
```

荧光纸是一种纸，不是一种墨：它承载碳粉文字，自己绝不做文字。三种纸板，写入 stamp（印记）：`pasteup: kraft` 为牛皮纸板，即上面的 Token，纤维晕染 0.5、multiply；黑板墙，底 `oklch(21% 0.012 60)`，碳粉 `oklch(94% 0.012 90)`，淡色 `oklch(70% 0.015 80)`，纤维晕染 0.35、screen；糖纸，底 `oklch(84% 0.035 150)`，碳粉 `oklch(22% 0.02 160)`，淡色 `oklch(42% 0.03 160)`，纤维晕染 0.4、multiply。

## 字体（Type）

- **展示字体：**League Gothic 400，全大写，`--tracking-display`，绝不低于 28px，因此条目标题（`h3`）改用 Newsreader 500。它是海报字体：传单标题或大数字可达两倍 `--text-display`，行高 0.92；章节标题比 `--text-section` 大一档，行高 1.0。
- **正文：**Newsreader 400 与 500，18px，行高 1.5；斜体只作行文中的强调。纸上文字压在复印纸的白底上；在纸板上用 `--color-ink`，18px 以下绝不用 `--color-muted`。
- **标签、图注、表头、元信息、控件：**Newsreader 500 小一档，句首大写，不加字距。不用等宽字体。

## 表面（Surfaces）

- 纸张浮起，不是盒子：凹槽是一张复印纸（`--color-paper-3`）压着 `--shadow-card`，浮起的纸用 `--shadow-sheet`。圆角 0；`--color-rule` 发丝线在纸板上分行，纸上用 `--color-rule-2`。
- 倾斜就是浆糊：一张纸或一张照片可以偏转 0.5° 到 2°，一块屏幕上倾斜的表面至多三处；输入框、表格与长文阅读保持端正。
- 荧光纸承载主控件，且一块屏幕至多一张，上面压碳粉文字；绝不做色带、标题，也绝不在纸板上单做一个词。
- 色带：`--color-paper-2`（更深的牛皮色）或碳粉配纸板色文字；每页至多两条。
- 照片：zine、手、复印机、订书机与市集摊位，近景、平光，至多一个背影人群；过一遍复印机（`photo:` 一行），硬朗黑白。以 multiply 印在复印纸上，留 10 至 16px 边距并浮起；或直接印上纸板，让牛皮色从白色里透出来；绝不用彩色，绝不通栏。图注压在纸脚上。
- 纹理：纤维晕染（`texture.md` § 1，低频黄褐色调）以纸板的不透明度与混合模式铺在牛皮色带上，绝不上纸面，也绝不压正文。

## 版式（Range）

- **事实排成一墙传单：**提示词的日期、数量、价格与截止日各占一张纸，League Gothic 海报字号，跨度与高度错落，重叠几个像素，两三张带倾角，一张用荧光纸；中间不放照片。
- **一张排印的纸：**时刻表、价目表或时间地点，作为划线表格放在一张微微倾斜的复印纸上，左列 League Gothic，其余 Newsreader。
- **碳粉色带：**一行 League Gothic，`--text-display` 或更大，碳粉底上纸板色文字，横跨十列。
- **表单化作一张纸：**字段在复印纸上，方正，压硬偏移，旁边的纸板上放着大字排印的标题与截止日。

## 控件（Controls）

- 控件对：荧光主按钮压碳粉文字，垫在硬质 `4px 4px 0` 墨色偏移上；旁边是同一偏移上的复印纸次按钮，两者 Newsreader 500、15px。
- 链接用碳粉加 1px 下划线，悬停加粗；输入框是复印纸，方正，1px 墨色边框；焦点环用碳粉。

## 动效（Motion）

只有纸张物理：悬停时按钮向偏移里陷落 1px，按下陷落 4px，时长 `--dur-micro`。无悬浮，无显现。

## 语气（Voice）

传单语气：日期、开门、价格、桌号。

## 禁止事项（Do-nots）

- 绝不用拼贴道具：无胶带、贴纸、印章或涂鸦便签。
- 绝不在标题里单挑一个词：无剪出来的词、无黄色的词、无斜体的词。
- 绝不给控件加软阴影；控件压在硬质墨色偏移上。
- 绝不用脏污叠层、撕边或彩色照片。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=League+Gothic&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">
```

```css
h1, h2 { font-weight: 400; text-transform: uppercase; line-height: 1; } h1 { line-height: 0.92; }
h3 { font: 500 var(--text-title)/1.2 var(--font-body); }
.btn { border: 0; border-radius: 0; padding: var(--space-sm) var(--space-md); font: 500 15px/1.2 var(--font-body); color: var(--color-ink); box-shadow: 4px 4px 0 var(--color-ink); transition: translate var(--dur-micro) var(--ease-out), box-shadow var(--dur-micro) var(--ease-out); }
.btn:hover { translate: 1px 1px; box-shadow: 3px 3px 0 var(--color-ink); }
.btn:active { translate: 4px 4px; box-shadow: none; }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.btn--secondary { background: var(--color-paper-3); }
.sheet { background: var(--color-paper-3); box-shadow: var(--shadow-sheet); rotate: var(--r, 0deg); }
.sheet--fluoro { background: var(--color-accent); color: var(--color-accent-ink); }
.sheet img { mix-blend-mode: multiply; filter: grayscale(1) contrast(1.3); }
.fibre { position: relative; isolation: isolate; }
.fibre::before { content: ""; position: absolute; inset: 0; z-index: -1; opacity: 0.5; mix-blend-mode: multiply; pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='p'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.02 0.03' numOctaves='3' seed='7'/%3E%3CfeColorMatrix values='0 0 0 0 0.55 0 0 0 0 0.45 0 0 0 0 0.3 0 0 0 0.28 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23p)'/%3E%3C/svg%3E"); }
::selection { background: color-mix(in oklab, var(--color-accent) 70%, transparent); color: var(--color-ink); }
```
