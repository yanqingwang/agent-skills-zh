---
name: Grid
slug: grid
genre: editorial
paper: light 97.5 90
display: grotesk-sans Radio Canada Big
accent: cool 266
posture: full-palette
keywords: identity, brand system, wayfinding, signage, design studio, type specimen, editorial grid, institution, museum, archive, index, directory, systems, modular, swiss, grotesque, manual, programme, poster, collection
material: 白色海报纸、蓝黑墨色、Radio Canada 上压句首大写的 Radio Canada Big 700、群青色平涂场域与一个瑞士红标记、无描边
pictured: Poster Sequence, Poster hero
photo: duotone ink paper-2 con=12
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/grid.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Grid

当下实践的瑞士国际主义风格：一张白纸、一种蓝黑墨色、一款带两个光学字号的新怪诞体、两种分工明确的平涂色，一片漫过场域的群青，和一个标记唯一被选中之物的瑞士红。结构来自栏系统本身：文字挂在栏线上，场域在栏线上起止，字号三级四级地跳，留白是有意守住的。没有线条分隔区块，没有任何东西装盒；一页读起来是一连串排好的版面。它不是怀旧海报的仿作，不是红黑模板，也不是极简产品页。

## Tokens

```css
:root {
  --color-paper: oklch(97.5% 0.005 90); --color-paper-2: oklch(94.2% 0.006 90); --color-paper-3: oklch(90.5% 0.008 90);
  --color-ink: oklch(19% 0.022 266); --color-ink-2: oklch(31% 0.02 266); --color-muted: oklch(47% 0.016 266);
  --color-rule: oklch(87.5% 0.008 90);
  --color-accent: oklch(44% 0.2 266); --color-accent-ink: oklch(97.5% 0.005 90); --color-focus: oklch(46% 0.2 266);
  --color-field: oklch(44% 0.2 266); --color-field-ink: oklch(97.5% 0.005 90);
  --color-mark: oklch(57% 0.215 29); --color-mark-ink: oklch(97.5% 0.005 90);
  --font-display: "Radio Canada Big", ui-sans-serif, system-ui, sans-serif; --font-body: "Radio Canada", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: var(--font-display);
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --shadow-card: none;
  --tracking-display: -0.035em; --display-weight: 700;
}
```

三个角色加纸张，各司一职。**Field**，群青：版面印在其上的那片漫色，通栏或从某条栏线延伸到出血。**Mark**，瑞士红：被选中或当前之物（一个字母、一个年份、一个 hover 的链接），每页至多一片红色场域。**Ink**：纸上的文字和主控件。红绝不压在群青上，两片场域绝不相触。

## 字体

- **展示字体：**Radio Canada Big 700、句首大写（首字母大写加专有名词，仅此而已）、`--tracking-display`，海报字号行高 0.9、区块字号 1.0。行从栏线起、左齐右参差；绝不居中。每个标题一种字重、一种颜色；标题从纸上越过到场域上时，在场域边缘切换为 field-ink，像叠印那样，这是它唯一允许的变化。
- **海报字号：**海报标题随屏幕缩放，`clamp(4.5rem, 10.2vw, 10rem)`，字距 -0.045em，到 1920 封顶。数字与索引字母用 display 切片，可以排得比旁边的任何标题都大；宣言用 display 的 400。
- **正文：**Radio Canada 400、17px、行高 1.5。标签、字段名、题注与导航链接用 Radio Canada 500 小一档，句首大写，不加字距，纸上用 `--color-muted`、场域上用 field-ink。不用等宽，标签里不用大写。
- **字标：**名字排两行、同一字号，第一个词用 display 700，第二个词用 400，行距 0.92；它旁边可以挂一个恰好两行高的 mark 红方块。

## 表面

- 无描边：区块之间靠留白、换纸或一片场域分隔，绝不用线条。仅有的线是表格行间的 1px 细线和输入框下的一条。
- 圆角 0、任何地方无阴影；纵深靠字号层级与颜色。well 是无边框的 `--color-paper-2`。
- 场域：一页两到三片，其中一片可以是红的；每片要么通到边，要么从一条栏线延伸出页外，并与白色相接。
- 照片：均匀光下的客观正面视角，拍印刷及其工具（活字、印刷机、纸张、字盘抽屉），以蓝黑印在 `--color-paper-2` 上（`photo:` 双色调），于是画框是一档色调，绝不是一条线。方形，两条边都落在栏线上；绝不在图片上压文字。
- 纹理：没有。白色就是材质。

## Range

- **叠印版面：**海报字号的标题从第 1 栏挂下，横越过一片从更靠后的栏线开始的场域，字母交叉处转为 field-ink，场域脚下排一个真实的大数字。
- **索引当字体样张：**字母、年代或名字用 display 字号排成一排参差的按钮，选中的那个用 mark 红，并在这排按钮旁以通高重复出现，作为大数字。
- **装着控件的场域：**群青或红上放一个区间、一个选择或一组输入，数值用 field-ink、海报字号，随操作即时变化；场域上的输入是 `--text-3xl` 的文字压在一条细线上。
- **不对称悬挂的宣言：**一句话用宣言字号从第 3 或第 4 栏起，左边各栏留白，关键名词做成链接。

## 控件

- 主按钮：墨色方块、纸张色文字，52px 高，在纸上与任何场域上都一样。次级：文字带 1px 下划线，hover 转 mark 红。
- 输入框：方形、无外框；纸上下方一条 1px `--color-muted` 线，场域上用 60% 的 field-ink。焦点圈是 2px `--color-focus`，群青上为 field-ink、红上为墨色。
- `::selection` 是 mark 红配纸张色文字。除此之外，红只标记选中的值、一次 hover 和它那一片场域。

## 动效

只有状态，`--dur-short` 时长、`--ease-out` 缓动：一个字母或链接转红，海报字号的数值原位切换。无滚动显现、无视差。

## 语气

精确、平实、句首大写：按目录条目的顺序说出记录、字段、年份与印刷厂，形容词一律省去。

## 禁止事项

- 区块上方绝不用线，控件四周绝不用黑描边，绝不做盒装卡片。
- 红绝不压群青，两片场域绝不相触，绝不引入第二种蓝。
- 标题绝不全小写，也绝不全大写。
- 照片绝不用彩色、绝不用场域色调色、绝不加框，也绝不压文字。
- 标题绝不居中，文本块绝不居中。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Radio+Canada+Big:wght@400;700&family=Radio+Canada:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: var(--display-weight); line-height: 1; text-align: start; }
.btn { min-height: 52px; padding-inline: var(--space-lg); border: 0; border-radius: 0; font-weight: 500; transition: background-color var(--dur-short) var(--ease-out); }
.btn--primary { background: var(--color-ink); color: var(--color-paper); }
.btn--primary:hover { background: var(--color-ink-2); }
.btn--secondary { background: none; color: currentColor; text-decoration: underline var(--rule-hair); text-underline-offset: 0.32em; }
.btn--secondary:hover { color: var(--color-mark); }
.field { background: var(--color-field); color: var(--color-field-ink); --color-focus: var(--color-field-ink); }
.field--mark { background: var(--color-mark); color: var(--color-mark-ink); --color-focus: var(--color-ink); }
.overprint { color: var(--color-field-ink); clip-path: inset(0 0 0 calc(7 * (100% + var(--gap-columns)) / 12 - var(--gap-columns))); }
.wordmark { display: inline-grid; grid-template-columns: auto auto; column-gap: var(--space-sm); font: var(--display-weight) var(--text-md)/0.92 var(--font-display); }
.wordmark::before { content: ""; grid-row: span 2; aspect-ratio: 1; background: var(--color-mark); }
::selection { background: var(--color-mark); color: var(--color-mark-ink); }
```
