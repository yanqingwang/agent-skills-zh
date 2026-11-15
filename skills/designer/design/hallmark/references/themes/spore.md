---
name: Spore
slug: spore
genre: atmospheric
paper: dark 15 60
display: roman-serif Young Serif
accent: warm 30
posture: committed
keywords: grower, mushroom, fungi, farm, food, producer, fermentation, wine, natural wine, wine bar, bottle shop, cellar, preserves, dark, culture, night market, harvest, subscription, small batch
material: 带暖色颗粒的咖啡渣黑、羊皮纸色墨色、Instrument Sans 上压 Young Serif、柔和胶囊与带颗粒的 well、灯光与烛光下的照片、一个平菇粉
photo: warm con=6 exp=-4
pictured: Photographic, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/spore.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Spore

深夜的酒窖：咖啡渣黑向棕暖去、well 上带暖色颗粒、Instrument Sans 上压羊皮纸色的 Young Serif、柔和胶囊、只被灯光与烛光照亮的照片，以及一个平菇粉。它显得亲近而手工，因为暖意落在底色、颗粒、数字和一种柔和的颜色里，绝不落在画出来的光上。它不是带辉光的深色模式模板，也不是养生标签。

## Tokens

```css
:root {
  --color-paper: oklch(15% 0.012 60); --color-paper-2: oklch(19% 0.014 58); --color-paper-3: oklch(24% 0.02 50);
  --color-ink: oklch(93% 0.022 85); --color-ink-2: oklch(84% 0.022 78); --color-muted: oklch(67% 0.02 70);
  --color-rule: oklch(31% 0.016 60);
  --color-accent: oklch(77% 0.09 30); --color-accent-2: oklch(86% 0.06 30); --color-accent-ink: oklch(15% 0.012 60); --color-focus: oklch(86% 0.06 30);
  --font-display: "Young Serif", Georgia, serif; --font-body: "Instrument Sans", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "Instrument Sans", ui-sans-serif, system-ui, sans-serif;
  --radius-card: 14px; --radius-pill: 999px; --rule-hair: 1px;
  --shadow-card: 0 16px 40px oklch(8% 0.01 60 / 0.4);
  --tracking-display: -0.012em;
  --grain: 0.15; --display-weight: 400;
}
```

只有一个旋钮：配色方案（colourway），写进 stamp（`spore: cellar`）。

| 配色方案 | 底色 | 墨色 | 强调色 |
| --- | --- | --- | --- |
| `cellar`（默认） | `oklch(15% 0.012 60)`，颗粒以 screen 混合、15% | 羊皮纸色 `oklch(93% 0.022 85)` | 粉色 `oklch(77% 0.09 30)` |
| `lab` | 奶油色 `oklch(94% 0.02 85)`，颗粒以 multiply 混合、6% | `oklch(17% 0.015 60)` | 粉色 `oklch(62% 0.13 30)` |
| `head-torch` | `oklch(12% 0.008 60)`，颗粒 15% | `oklch(93% 0.03 85)` | 赭色 `oklch(74% 0.13 80)` |

## 字体

- **展示字体：**Young Serif 400、`--tracking-display`、行高 1.02、句首大写、正体，每个标题只用一种颜色。它唯一的字重就是语气：层级靠字号，绝不靠加粗。
- **数字：**价格、天数、钟点与数量用 Young Serif、等高数字（lining）；当某个数字就是区块存在的理由时，可以超过 `--text-display`；价格是唯一可用粉色的数字。
- **正文：**Instrument Sans 400 与 500，行高 1.55，用 `--color-ink-2`。产品名之后的第二个名字（葡萄品种、年份、拉丁名）用 Instrument Sans 斜体，是 outlier 字体，也是唯一的斜体。
- **标签、题注、表头：**Instrument Sans 500 小一档，句首大写，用 `--color-muted`。

## 表面

- 行之间 1px `--color-rule`；输入域上 1.5px `--color-ink-2` 边。其他任何东西都不带边框。
- 圆角：控件与 chip 用胶囊，well 与照片用 `--radius-card`；输入框方形。
- 纵深就是底色的三档：paper、带颗粒的 `--color-paper-2` well、`--color-paper-3` 色带。当下生效的状态（今晚、选中的行）抬升一档并挂一个粉色 chip。`--shadow-card` 只用在叠压照片的 well 下。
- 照片：天黑后的场所，凑近：酒架、倾倒的一杯、烛光吧台、一只杯子；低暖光没入阴影，绝不用闪光或日光。`--radius-card`，加 8% 的 1px 墨色圈；照片上的文字放在暗侧，压在 45% 到 65% 的纸张色压暗层上。
- 颗粒：`texture.md` § 1 的斑点颗粒，以 `--grain` 值做 screen 混合，只用在 well 与色带上；绝不垫在分栏正文之下，也绝不压在照片之上。

## Range

- **一个数字撑起区块：**Young Serif 的数量或价格，两到四倍 `--text-display`，放在带颗粒的 well 上，下方朴素标签，旁边两三行细线行说明这个数字的含义。
- **一周做成时刻表：**Rows 里星期名用 Young Serif、`--text-title`，钟点在旁，歇业日降为 muted，今晚那一行抬升到 paper-3 并挂粉色 chip；旁边第 1 到 4 栏放一个标题块。
- **列表或价目表：**划线行，名字用 Young Serif，第二个名字用斜体，价格右齐用粉色；排成三或五栏深，读起来就是酒架。
- **带颗粒、装着表单的色带：**paper-3 加斑点颗粒，粉色大号价格，旁边方形输入域和粉色胶囊；或一条 Young Serif 宣言、`--text-display` 字号横跨十栏。

## 控件

- 按钮对：粉色填充胶囊、`--color-accent-ink` 文字，hover 变亮为 `--color-accent-2`，旁边一枚 1.5px `--color-ink-2` 描边胶囊。Chip 就是胶囊；选中的那枚填粉色。
- 链接用羊皮纸色、下划线 hover 转粉；输入框方形，带 1.5px 边和 `--color-focus` 焦点圈。

## 动效

只有状态，一帧完成：chip 选中、某行抬升、胶囊变亮。无显现、无生长、无循环。

## 语气

酿造者的日志：名字、日子、钟点、年份、价格。不养生、不神秘、不说"甄选"。

## 禁止事项

- 绝不引入第二个色相；"有货"用绿色会让页面变成园艺中心。
- 绝不把画出来的光当氛围（一束光、一片光斑、标题后的辉光）；光只活在照片里。
- 绝不用中性或蓝黑底色；每个深色档都偏向色相 60。
- 正文绝不用粉色，绝不粉色描边；粉色是填充、是价格，或焦点。
- 绝不让照片一张接一张；两张照片之间放一个数字、一张时刻表或一份 Young Serif 列表。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Young+Serif&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: 400; letter-spacing: var(--tracking-display); line-height: 1.02; }
.btn { border-radius: var(--radius-pill); padding: var(--space-sm) var(--space-lg); font-weight: 600; transition: background-color var(--dur-micro) var(--ease-out); }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.btn--primary:hover { background: var(--color-accent-2); }
.btn--secondary { background: transparent; color: var(--color-ink); box-shadow: inset 0 0 0 1.5px var(--color-ink-2); }
.well { background: var(--color-paper-2); border-radius: var(--radius-card); }
.figure { font-family: var(--font-display); font-variant-numeric: lining-nums; line-height: 0.86; }
.grained { position: relative; isolation: isolate; }
.grained::after { content: ""; position: absolute; inset: 0; z-index: var(--z-base); border-radius: inherit; pointer-events: none; opacity: var(--grain); mix-blend-mode: screen;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 0.6 0 0 0 0 0.55 0 0 0 0 0.45 0 0 0 0.35 0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E"); }
```
