---
name: Squeeze
slug: squeeze
genre: playful
paper: mid 41 154
display: geometric-sans Gabarito
accent: warm 56
posture: drenched
keywords: fruit, food box, grocer, market, delivery, weekly, seasonal, farm shop, subscription, produce, veg box, cheerful, family, treats, stall, orchard, local, fresh
material: forest-green paper with real chroma, warm white ink, Gabarito 800 heads and figures over Manrope, soft rounded tiles a step lighter or deeper, fruit photographed bright and close, juicy peach controls
photo: natural vib=12 con=4
pictured: Bento Grid, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/squeeze.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Squeeze

一摊色彩里的市集果摊：带真实彩度的森林绿底、暖白墨色、Gabarito 圆润厚重的标题与数字压在结实的 Manrope 上、浅一档或深一档的软贴片、明亮近摄的水果、多汁的蜜桃色控件与一张暖白卡片。它欢快，因为绿是整个表面、水果是它身上的颜色；一个用 Gabarito 排到巨大的价格或日子，与一筐水果同样是材料本身。它不是带绿色按钮的中性生鲜模板，也不是衬线加牛皮纸的有机标签。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(41% 0.100 154); --color-paper-2: oklch(47% 0.105 154); --color-paper-3: oklch(34% 0.090 156);
  --color-ink: oklch(99% 0.005 90); --color-ink-2: oklch(94% 0.020 120); --color-muted: oklch(90% 0.030 150); --color-rule: oklch(55% 0.100 154);
  --color-accent: oklch(83% 0.115 56); --color-accent-2: oklch(74% 0.150 46); --color-accent-ink: oklch(30% 0.070 40); --color-focus: oklch(88% 0.14 85);
  --color-card: oklch(97% 0.012 85); --color-card-ink: oklch(24% 0.05 160);
  --font-display: "Gabarito", ui-sans-serif, system-ui, sans-serif; --font-body: "Manrope", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: var(--font-display);
  --radius-card: 24px; --radius-control: 16px; --radius-pill: 999px; --rule-hair: 1px; --rule-bar: 2px;
  --shadow-card: 0 14px 32px -16px oklch(22% 0.05 160 / 0.5);
  --tracking-display: -0.025em; --display-weight: 800;
}
```

## 字体（Type）

- **展示字体：**Gabarito 800，`--tracking-display`，行高 1.0，句首大写，每个标题单色。圆、紧、重，所以共享展示字阶不必封顶；绝不低于 700。
- **数字：**价格、日期与星期用 Gabarito 800、表格数字、等高数字；单个数字可以到章节标题的三四倍，字距收到 -0.04em，单位用同字重。
- **正文：**Manrope 500，行高 1.55，用 `--color-muted`；链接与行标题用 700。总共三个字重：800、700、500。
- **标签、图注、表头、元信息：**Manrope 700 小一档，句首大写，不加字距。绝不用等宽，绝不用大写。

## 表面（Surfaces）

- 贴片，不是卡片：贴片是比地面浅一档的 `--color-paper-2`，`--radius-card` 圆角，无边框，无阴影；下陷的凹槽用 `--color-paper-3`。访客可以选的贴片，选中时沉到 `--color-paper-3` 并套上 3px `--color-accent` 圆环。
- 唯一抬起的表面是暖白卡片（`--color-card`、`--color-card-ink` 文字、`--shadow-card`），每页一次，给访客要付钱的东西；卡片内部焦点环用 `--color-card-ink`。
- 横线用 `--color-rule` 的 `--rule-bar`；只有列表行之间的线用 `--rule-hair`。
- 色带：页面已是绿色，所以色带用浅一档或深一档的绿（`--color-paper-2`、`--color-paper-3`）；每页至多两条，绝不用白、灰或蜜桃色带。
- 照片：日光下近摄的水果、俯拍的一筐、递到镜头前的水果、摊上的一堆；明亮，水果撑满画框。`--radius-card` 圆角，无环，无阴影；图注在下方、用标签字体；照片上的文字压一层 45 至 65% 的 `--color-paper-3` 暗化。
- 无纹理：绿是一块平涂颜色。

## 版式（Range）

- 一个价格、一个尺寸或一个日子，作为陈述字号的单个数字：Gabarito 800 墨色直接压在绿上，单位全字重，标题与一行文字排在旁边剩下的列里。绿与数字自己撑起整块屏幕。
- 真实日期排成贴片或通栏行的时刻表：每个日期 Gabarito 大字，星期用标签字体，选中的沉到 `--color-paper-3` 并套上蜜桃色圆环；一块能当控件用的摊位黑板。
- 一句承诺作为陈述压在更深的绿色带上，Gabarito 展示字号横跨十列，下方一个动作。
- 问题或平实的条款排成行：左侧 Gabarito 标题，右侧 Manrope 回答，之间 `--color-rule` 发丝线。

## 控件（Controls）

- 控件对：蜜桃填充的主按钮配 `--color-accent-ink` 文字，旁边是 2px 墨色描边的次按钮，两者 `--radius-control` 圆角，Manrope 700。标签与 chips 用胶囊；导航链接可以是 `--color-paper-2` 胶囊。
- 链接用墨色 700，下划线悬停转蜜桃；输入框 2px `--color-rule` 边框、`--radius-control` 圆角、`--color-focus` 焦点环。
- 蜜桃只落在控件上：主按钮、选中的 chip 或贴片圆环、链接悬停；`--color-accent-2` 只作主按钮的按压与悬停阶。绝不用蜜桃文字，绝不用蜜桃色场。

## 动效（Motion）

欢快而快，只动状态：控件以 `--dur-micro` 按下 1px，选中的贴片以 `--dur-short`、`--ease-out` 套上圆环，可选贴片悬停时绿浅一档。无显现、无视差、无循环；按不动的东西不作反应。

## 语气（Voice）

摊主的声音，周四早晨大声说出来：什么水果、哪天到、熟在手里是什么手感。句子短而暖，价格直说；绝不美食腔，绝不养生推销。

## 禁止事项（Do-nots）

- 绝不用中性底色。白色只给那一张卡；灰色不存在。页面就是绿。
- 绝不用发暗或发灰的绿；底色保持彩度，否则就成了军需库。
- 绝不用低于 500 的字重、衬线或等宽数字：数字就是 Gabarito。
- 绝不用发丝线边框；1px 线只活在列表行之间。
- 绝不用暗调照片，也绝不每屏都放照片：当绿与文字各有自己的屏幕时，水果才最亮。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Gabarito:wght@800&family=Manrope:wght@500;700&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: var(--display-weight); letter-spacing: var(--tracking-display); }
h1, h2 { line-height: 1; }
.figure { font: var(--display-weight) clamp(7rem, 16vw, 15rem)/0.85 var(--font-display); letter-spacing: -0.04em; font-variant-numeric: lining-nums tabular-nums; }
.tile { background: var(--color-paper-2); border-radius: var(--radius-card); }
.tile:has(:checked) { background: var(--color-paper-3); box-shadow: inset 0 0 0 3px var(--color-accent); }
.card { background: var(--color-card); color: var(--color-card-ink); border-radius: var(--radius-card); box-shadow: var(--shadow-card); }
.btn { border: var(--rule-bar) solid var(--color-ink); border-radius: var(--radius-control); padding: var(--space-sm) var(--space-lg); font: 700 var(--text-md)/1.25 var(--font-body); color: var(--color-ink); transition: translate var(--dur-micro) var(--ease-out), background-color var(--dur-micro) var(--ease-out); }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); border-color: var(--color-accent); }
.btn--primary:hover { background: var(--color-accent-2); border-color: var(--color-accent-2); }
.btn:active { translate: 0 1px; }
.photo img { border-radius: var(--radius-card); }
::selection { background: color-mix(in oklab, var(--color-accent) 45%, transparent); color: var(--color-card-ink); }
```
