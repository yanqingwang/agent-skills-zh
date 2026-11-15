---
name: Darkroom
slug: darkroom
genre: atmospheric
paper: dark 12.5 55
display: display-condensed Sofia Sans Extra Condensed
accent: chromatic-amber 58
posture: restrained
keywords: photographer, photography, film, analogue, darkroom, prints, portfolio, exhibition, gallery, edition, commission, cinematographer, negative, archive, monochrome, lab, moody, black and white, night, print shop, travel, places, landscape, portrait, photo studio
material: warm print-black ground, a fine light grain, fibre-white ink, hairline Sofia Sans Extra Condensed capitals over Barlow, zero radius, black-and-white photographs printed deeper than the ground, one amber safelight
photo: mono high=-20 shad=-12
pictured: Photographic, Poster hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/darkroom.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Darkroom

关了灯的冲印室：暖调黑底比印片自己的黑浅一档，照片因此作为一件物体坐在上面；纤维白墨色；发丝线极窄大写压在 Barlow 之上；一盏琥珀安全灯。照片黑白，印得深且大，其余交给文字。它不是胶片齿孔的戏服，不是情绪化渐变，不是平板屏幕的纯黑，也不是白卡纸装裱的画廊。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(12.5% 0.008 55); --color-paper-2: oklch(16% 0.009 55); --color-paper-3: oklch(20.5% 0.01 55);
  --color-ink: oklch(92% 0.012 78); --color-ink-2: oklch(80% 0.012 75); --color-muted: oklch(64% 0.012 65);
  --color-rule: oklch(29% 0.01 55);
  --color-accent: oklch(73% 0.15 58); --color-accent-deep: oklch(50% 0.11 52); --color-accent-ink: oklch(12.5% 0.008 55); --color-focus: oklch(73% 0.15 58);
  --font-display: "Sofia Sans Extra Condensed", ui-sans-serif, sans-serif; --font-body: "Barlow", ui-sans-serif, sans-serif;
  --font-outlier: var(--font-body);
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --shadow-card: none;
  --tracking-display: -0.005em; --display-weight: 200; --grain: 0.07;
}
```

三种配色，写入 stamp（印记）：`darkroom: amber`。

| 配色 | 底色、墨色、信号色 |
| --- | --- |
| **amber**（默认） | 上面的 Token |
| **red** | 信号 `oklch(62% 0.19 32)`，深色 `oklch(44% 0.16 32)` |
| **fibre paper** | 底 `oklch(95% 0.01 80)`，墨色 `oklch(14% 0.006 40)`，淡色 `oklch(46% 0.01 50)`，信号 `oklch(50% 0.2 30)`，横线 `oklch(80% 0.014 70)`；暗斑 0.12 |

## 字体（Type）

- **展示字体：**Sofia Sans Extra Condensed 大写，Hero、章节标题与数字用 200，条目标题与控件用 400，行高 1.0，`--tracking-display`，正体。放大后的发丝线就是那副样子：因为极窄，每个展示层级可以比共享字阶高出一档，Hero 标题横跨八列排到海报字号。
- **正文：**散文用 Barlow 400，17px、行高 1.6，让阅读文字在暗底上站稳；Barlow 300 只用于导语字号及以上。
- **标签、图注、表头：**Barlow 400 小一档，句首大写，不加字距，用 `--color-muted`；版号与月份就是这个语气。数字用表格数字。不用等宽字体。

## 表面（Surfaces）

- 深度是明度，不是光：底 12.5，凹槽 16，表面 20.5。无晕影、无辉光、无阴影；印片的黑色比底色更深，这正是页面读起来像一张印片的原因。
- 横线：1px `--color-rule`，在一张单子的行间通栏横过，并在数字之间作竖向发丝线；处处圆角 0。
- 色带：带颗粒的 `--color-paper-2` 凹槽，给不承载图片的章节；每页至多两条，绝不用琥珀色场。
- 照片：即作品本身。黑白，印得深（高光通透、黑部饱满、胶片的颗粒）；主体带留白的远景，或近景平拍。圆角 0，无框，无卡纸；通栏或收在栏内，绝不缩略图尺寸，下方配带版号的图注。文字只在照片最暗的三分之一上横过，压一层 40 至 70% 的底色暗化。
- 纹理：`texture.md` § 1 的斑点颗粒以 `--grain` 铺在凹槽上；绝不压在照片上。

## 版式（Range）

- **数字排成一个版次：**提示词的真实数字（版数、每种印数、印量）用 200 发丝线排在 12rem 及以上的颗粒凹槽上，之间竖向发丝线，各配一行淡色 Barlow；字号就是戏剧性，颜色保持墨色。
- **一张藏家单：**通栏发丝线下的行，左侧淡色 Barlow 标签，右侧展示大写的值排标题字号：系列、题材、底片、相纸、版次、尺寸。
- **流程化作试条：**步骤横跨十二列，每段是章节字号的一条发丝线数字压一行短句（曝光、显影、印相、成版），竖线分隔；不画任何东西。
- **选择组化作数字：**版数或尺寸的可用选择器，1px 线单元格，各是一个标题字号的展示数字，选中的那个被安全灯点亮，旁边是底色上的朴素表单。

## 控件（Controls）

- 一对：琥珀填充的主按钮配 `--color-accent-ink`，旁边是 1px 墨色描边的次按钮，两者展示大写 400，不加字距，圆角 0，48px 高。
- 链接用墨色，下划线用 `--color-rule`；悬停下划线转琥珀。输入框：圆角 0，底色上 1px `--color-muted` 边框，聚焦时一条稳定的描边。
- 安全灯稀缺：唯一的填充控件、选中的版号、悬停出现的图注；`--color-accent-deep` 是墨字之下更安静的填色。

## 动效（Motion）

静如印片。一张照片可以从底色之上升起一次，时长 `--dur-long`，像在显影盘里，从可见的默认态开始；悬停在有链接的版片上，其编号转琥珀。其余一律不动。

## 语气（Voice）

实验记录与藏家单：系列、版号、地点、月份、版次、相纸。数字精确，句子短，不说关于光或灵魂的形容词。

## 禁止事项（Do-nots）

- 绝不用琥珀色晕染、色带、辉光或琥珀标题；安全灯照亮一个控件或一个数字，绝不清一节。
- 绝不要齿孔、胶片条、蜡笔圈或画出来的框。
- 绝不让 Sofia Sans Extra Condensed 在标题上超过 400，数字绝不用 200 以外的字重。
- 绝不给照片加棕褐色、双色调或染色，也绝不让印片坐在平板屏幕的纯黑上。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Sofia+Sans+Extra+Condensed:wght@200;400&family=Barlow:wght@300;400&display=swap" rel="stylesheet">
```

```css
h1, h2, .figure { font-family: var(--font-display); font-weight: 200; text-transform: uppercase; line-height: 1; letter-spacing: var(--tracking-display); }
h3 { font-family: var(--font-display); font-weight: 400; text-transform: uppercase; line-height: 1; }
.btn { min-height: 48px; padding: 0 var(--space-lg); border: var(--rule-hair) solid var(--color-ink); border-radius: 0; background: transparent; color: var(--color-ink); font: 400 var(--text-lg)/1 var(--font-display); text-transform: uppercase; }
.btn--primary { background: var(--color-accent); border-color: var(--color-accent); color: var(--color-accent-ink); }
.well { background: var(--color-paper-2); }
.grained { position: relative; isolation: isolate; }
.grained::after { content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none; opacity: var(--grain); background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 9 -4'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E") 0 0 / 200px 200px; }
::selection { background: color-mix(in oklab, var(--color-accent) 35%, transparent); }
```
