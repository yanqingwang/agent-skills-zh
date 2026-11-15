---
name: Almanac
slug: almanac
genre: editorial
paper: mid 84 245
display: grotesk-sans Hanken Grotesk
accent: chromatic-magenta 350
posture: restrained
keywords: almanac, yearbook, field guide, reference, handbook, manual, index, catalogue, encyclopedia, data, figures, tables, statistics, research, dataset, records, directory, glossary, specifications
material: 冷调石板灰底纸上铺一张浅色印刷页、蓝黑墨色、Newsreader 散文上压 Hanken Grotesk 标题、等宽字数字、两种线宽与直角、一个图表品红
photo: muted
pictured: Workbench, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/almanac.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Almanac

参考书的腔调：冷调石板灰底纸、蓝黑墨色、Newsreader 散文上压 Hanken Grotesk 标题、等宽字数字对齐到小数位、两种线宽的线条，以及一个深品红，海图印刷灯标所用的颜色，用量很小。它读起来精确，因为权威在线条与数字手里，不在颜色或装饰手里。它不是灰色底上的仪表盘，也不是暖调编辑部页面。

## Tokens

```css
:root {
  --color-paper: oklch(84% 0.012 245); --color-paper-2: oklch(81% 0.012 245); --color-paper-3: oklch(77% 0.012 245);
  --color-ink: oklch(16% 0.020 245); --color-ink-2: oklch(24% 0.018 245); --color-muted: oklch(38% 0.016 245);
  --color-rule: oklch(73% 0.013 240); --color-rule-2: oklch(32% 0.018 240);
  --color-accent: oklch(45% 0.180 350); --color-accent-2: oklch(37% 0.160 350); --color-accent-ink: oklch(97% 0.006 245); --color-focus: oklch(46% 0.190 350);
  --color-sheet: oklch(93.5% 0.008 245);
  --font-display: "Hanken Grotesk", ui-sans-serif, system-ui, sans-serif;
  --font-body: "Newsreader", ui-serif, Georgia, serif;
  --font-outlier: "IBM Plex Mono", ui-monospace, monospace;
  --radius-card: 0; --radius-pill: 2px; --rule-hair: 1px; --rule-bar: 2px; --shadow-card: none;
  --tracking-display: -0.02em; --display-weight: 600;
}
```

## 字体

- **展示字体：**所有标题用 Hanken Grotesk 600、`--tracking-display`、行高 1.05、句首大写、正体；hero 标题收紧到 -0.035em、行高 0.95。结构由 grotesk 排，衬线体绝不排标题。
- **正文：**Newsreader 400 与 500，开视觉字号（optical sizing），行高 1.55；斜体只作段内强调。
- **标签、题注、表头、元信息：**Newsreader 500 小一档，句首大写，用 `--color-muted`。绝不用等宽。
- **数字：**IBM Plex Mono 400 与 500，带 `tabular-nums`，栏内右对齐，小数点对齐。等宽字只排数字，别的什么都不排；单独一个数字（价格、数量）可用 Plex Mono 500、-0.04em 排到 `--text-display`。

## 表面

- 两种线宽：`--color-rule` 的 `--rule-hair` 分隔行与分区；`--color-rule-2` 的 `--rule-bar` 在标题或表头下画一条坚定的线。再无更重的。
- 每个表面都直角，控件至多 2px。不做盒装卡片、不做阴影：纵深是一条线加一档纸色（well 或隔行用 `--color-paper-2`）。
- 印刷页：`--color-sheet` 是那页印刷品，一张浅色纸铺在石板灰上，顶部一条 2px 墨线、内部细线；产品的页面与表格坐在它上面，段落绝不。
- 色带：`--color-paper-2` 色带，或一条 `--color-ink` 色带配纸张色文字、等宽字用印刷页颜色。每页至多两条；绝不做品红大片。
- 照片：工作距离下的题材（低潮的海港、滑道、坏天气下的海），中景到远景，阴天平光或晨光初照，没有面孔对着镜头。方形，内缩 1px `--color-rule-2` 描边，通版或横跨十栏；下方题注带一个事实；文字绝不压在照片上。
- 不用纹理：划线的纸，绝不是卡片表面。

## Range

- **页面本身就是主角：**一张表按印刷书的排法放在印刷页上：带日期的标题压在 2px 线上，行名用 Newsreader，时刻与高度用 Plex Mono 右对齐，页面所指的那一行用品红；它自己就能撑起一个 hero 或 split。
- **一张图表，排大：**单一系列用品红、2px、横跨十二栏，夜间或非营业时段用纸色档位压暗，每个转折点用等宽字标注；配上一个控件，它就是页面上唯一能操作的东西。
- **墨色带上的文件：**表头行加几行示例，Plex Mono、印刷页颜色，列名用品红，题注说明完整文件里有什么。
- **版本或套餐对比：**一张两三列的 Table，表头下压那条坚定的线，价格用等宽数字，操作放在最后一行。

## 控件

- 一个品红填充控件（`--color-accent` 底、`--color-accent-ink` 文字）旁边一个墨色细线描边控件，两者都用 Hanken Grotesk 500、2px 圆角。
- 链接墨色、1px 品红下划线、偏移 0.15em，hover 变粗；输入框方形，1px `--color-muted` 边。
- 品红保持在一屏的 5% 以内：填充控件、链接下划线，以及图表用来论证的那一个系列。

## 动效

除状态外什么都不动：可点击的行在 hover 时着色，链接下划线变粗。无显现、无数字滚动、无走马灯。

## 语气

陈述式、带日期、精确：引用数字、版本、来源、单位。绝不用炒作形容词。

## 禁止事项

- 绝不用艳粉或紫；品红守在 L 44、色相 350，深到读起来像图表的印刷色。
- 绝不用暖纸或白纸；色相 245 的石板灰，永远带色调。
- 绝不用盒装卡片或投影；两种线宽撑起每个表面。
- 绝不用巨大计数当 hero、满页小图表，或每天每个港口一个标记：一张排大的图承载全部数据。
- 绝不在文字背后飘装饰性波浪或线条；曲线只以带坐标轴的图表出现。
- 栏内绝不用比例数字（proportional figures）；要比较的数字用 Plex Mono、tabular、右对齐。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
```

```css
body { color: var(--color-ink-2); }
h1, h2, h3 { font-weight: 600; color: var(--color-ink); }
.num, td.num { font-family: var(--font-outlier); font-variant-numeric: tabular-nums; text-align: right; }
thead th, .rule-firm { border-bottom: var(--rule-bar) solid var(--color-rule-2); }
th { font: 500 var(--text-sm)/1.3 var(--font-body); color: var(--color-muted); text-align: left; }
td { border-top: var(--rule-hair) solid var(--color-rule); }
.btn { border: var(--rule-hair) solid var(--color-ink); border-radius: var(--radius-pill); padding: var(--space-sm) var(--space-lg); font: 500 var(--text-sm)/1 var(--font-display); color: var(--color-ink); background: transparent; }
.btn--primary { background: var(--color-accent); border-color: var(--color-accent); color: var(--color-accent-ink); } .btn--primary:hover { background: var(--color-accent-2); }
.well { background: var(--color-paper-2); border-top: var(--rule-bar) solid var(--color-rule-2); }
.sheet { background: var(--color-sheet); border-top: var(--rule-bar) solid var(--color-ink); }
.band--ink { background: var(--color-ink); color: var(--color-paper); }
.chart .series { fill: none; stroke: var(--color-accent); stroke-width: 2; }
.photo > img { outline: var(--rule-hair) solid var(--color-rule-2); outline-offset: -1px; }
a { color: var(--color-ink); text-decoration-color: var(--color-accent); text-underline-offset: 0.15em; } a:hover { text-decoration-thickness: 2px; }
```
