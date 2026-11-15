---
name: Vellum
slug: vellum
genre: editorial
paper: light 94 82
display: blackletter Grenze Gotisch
accent: cool 268
posture: committed
keywords: roastery, coffee, bakery, wine, cellar, apothecary, bookshop, press, letterpress, guild, heritage, artisan, manuscript, parchment, edition, tasting, vintage, craft, old world, slow
material: parchment paper, a long tan fibre wash on bands, umber ink, Grenze Gotisch heads over Hanken Grotesk with Grenze roman for statements, hairline and double rules, one ultramarine pigment
photo: warm con=6
pictured: Trade Ledger, Poster hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/vellum.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Vellum

一间老印刷所：羊皮纸底色、赭褐墨色，Grenze Gotisch 作标题，它的正体同胞 Grenze 用于放大的句子，朴素的 Hanken Grotesk 承担一切阅读文字，发丝线与双线，群青是唯一的颜料。哥特字体承载年代感，其余一切不加装饰：没有小酒馆，没有做旧仿古，也没有奶油配衬线的编辑页。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(94% 0.024 82); --color-paper-2: oklch(90% 0.032 80); --color-paper-3: oklch(86% 0.036 78);
  --color-ink: oklch(23% 0.025 55); --color-ink-2: oklch(31% 0.024 58); --color-muted: oklch(46% 0.024 64);
  --color-rule: oklch(75% 0.035 72);
  --color-accent: oklch(43% 0.17 268); --color-accent-deep: oklch(35% 0.15 268); --color-accent-soft: oklch(89% 0.035 268); --color-accent-ink: oklch(95% 0.02 82);
  --color-focus: oklch(50% 0.18 268); --color-field: var(--color-accent);
  --font-display: "Grenze Gotisch", ui-serif, Georgia, serif; --font-body: "Hanken Grotesk", ui-sans-serif, sans-serif;
  --font-outlier: "Grenze", ui-serif, Georgia, serif;
  --radius-card: 2px; --radius-pill: 2px; --rule-hair: 1px; --rule-double: 4px; --shadow-card: none;
  --tracking-display: -0.01em; --display-weight: 600; --fibre: 0.5;
}
```

三种配色，写入 stamp（印记）：`vellum: parchment`。

| 配色 | 底色、墨色、颜料 |
| --- | --- |
| **parchment**（默认） | 上面的 token |
| **oxblood, reversed** | 底 `oklch(27% 0.09 20)`，墨 `oklch(94% 0.02 80)`，颜料为金色 `oklch(84% 0.11 85)` 压底色之上，横线 `oklch(44% 0.08 20)`，纤维强度 0.25 |
| **indigo, the ledger** | 底 `oklch(93% 0.012 240)`，墨 `oklch(24% 0.035 265)`，同一群青，横线 `oklch(76% 0.02 250)`，纤维强度 0.14 |

## 字体（Type）

- **展示字体：**Grenze Gotisch 600 用于 `h1` 与 `h2`，行高 0.92，`--tracking-display`，句首大写。它在 30px 以下会挤作一团，所以 `h3` 及更小字号改用 Hanken Grotesk 600。
- **Outlier 字体，Grenze 400：**正体同胞，用于一句话排到 `--text-display-s`，以及展示字号的数字，行高 1.02。绝不用于正文。
- **正文：**Hanken Grotesk 400 与 500，行高 1.55；导航链接用 600。每页至多三种字重：400、500、600。
- **标签、图注、表头、元信息：**Hanken Grotesk 500，小一号，句首大写，不加字距。表格中互相比较的数字（重量、批号、日期）用 Hanken 的表格数字，右对齐。

## 表面（Surfaces）

- 横线：行间 1px `--color-rule` 发丝线，区块顶端 1px 墨线，以及印刷工会加双线的地方用 `--rule-double` 双墨线：表头之上、报头之下、色带顶端。
- 圆角处处 2px，无胶囊，无阴影：页面是平版印刷的。
- 色带：一条带纤维罩染的 `--color-paper-2` 色带，和一条群青 `--color-field`；每页至多两条，绝不相连。
- 照片：这门手艺自己的光（烘焙滚筒、冷却盘、麻袋、柜台、工作台前的双手），近拍，没有正对镜头的脸；偏暖，2px 圆角，1px `--color-rule` 边缘。图注在下、承载一个事实；标题压在照片上时必须垫赭褐蒙版。
- 纹理，纤维罩染：SVG turbulence 生成的长条棕褐纤维，拼接处理使它永不平铺，以 `--fibre` 正片叠底（`texture.md` 的低频罩染），只用于色带或内嵌面板。

## 版式（Range）

- **表格当日记账簿：**本周清单排成横贯全宽的划线表格，压在双线之下，颜料色数字为行编序，名称用 Hanken 600 标题字号，数值用表格数字；悬停行取 `--color-accent-soft`。
- **陈述配数字：**提示词中的一句话用 Grenze 400 横跨九或十列，排在纤维色带上；其下以一条发丝线分隔，提示词自己的数字用 Grenze Gotisch 排展示字号、颜料色，每个数字下配一个朴素的标签。
- **色场上的表单：**群青色带承载一个可用的选择（尺寸、频率），作边贴边的直角单元格，当前答案用 Grenze Gotisch 排区块字号。
- **行作索引：**三到五行划线行，标题用 Grenze Gotisch 排区块字号，旁边一行 Hanken：条款、到访、购买方式。

## 控件（Controls）

- 颜料色填充主按钮（`--color-accent` 底、`--color-accent-ink` 字），悬停加深为 `--color-accent-deep`，旁边是 1px 墨色边框的幽灵按钮；两者 2px 圆角，Hanken Grotesk 500。
- 链接悬停时下划线转颜料色；输入框 2px 圆角，1px 墨色边框。
- 群青是唯一的颜料：主按钮、链接悬停、焦点环、为列表编序的数字、大数字，以及那一条色带。

## 动效（Motion）

静止。悬停下划线转颜料色、行的柔和罩染与主按钮加深在 `--dur-micro` 内完成；无显现动效，无视差。

## 语气（Voice）

账簿式的平实并注明日期：品项、重量、年份、城镇，如书记员录入。绝不用 *artisanal*、*curated*，也绝不讲提示词没有给出的故事。

## 禁止事项（Do-nots）

- parchment 配色下绝不用陶土、红陶或牛血红作颜料；牛血红只能是底色。
- Grenze Gotisch 绝不用在 30px 以下、段落长度，或让标题以大写 I 开头，它会被读成 J。
- 绝不用毛边、暗角、咖啡渍、烧痕或第二种纹理。
- 绝不把创立年份单独作 Hero 标题；它要待在句子里、一行里，或作为带标签的数字。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Grenze+Gotisch:wght@600&family=Grenze:wght@400&family=Hanken+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">
```

```css
h1, h2 { font-weight: 600; line-height: 0.92; }
h3 { font-family: var(--font-body); font-weight: 600; }
.statement { font: 400 var(--text-display-s)/1.02 var(--font-outlier); }
.btn { border: var(--rule-hair) solid currentColor; border-radius: var(--radius-card); padding: var(--space-sm) var(--space-lg); font-weight: 500; color: inherit; background: transparent; transition: background-color var(--dur-micro) var(--ease-out); }
.btn--primary { background: var(--color-accent); border-color: var(--color-accent); color: var(--color-accent-ink); }
.btn--primary:hover { background: var(--color-accent-deep); border-color: var(--color-accent-deep); }
.band--pigment { background: var(--color-field); color: var(--color-accent-ink); }
.rule-double { border-top: var(--rule-double) double var(--color-ink); }
.ledger tbody tr:hover { background: var(--color-accent-soft); }
.fibre { position: relative; isolation: isolate; }
.fibre::before { content: ""; position: absolute; inset: 0; z-index: -1; opacity: var(--fibre); mix-blend-mode: multiply; pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='400'%3E%3Cfilter id='p' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.004 0.02' numOctaves='4' seed='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.62 0 0 0 0 0.52 0 0 0 0 0.36 0 0 0 0.3 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23p)'/%3E%3C/svg%3E"); }
```
