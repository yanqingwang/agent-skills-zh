---
name: Newsprint
slug: newsprint
genre: editorial
paper: light 94 92
display: slab-serif Zilla Slab
accent: warm 32
posture: restrained
keywords: newspaper, broadsheet, journalism, publication, magazine, newsletter, local news, op-ed, opinion, essay, longform, column, reportage, press, gazette, review, dispatch, literary
material: 浅色新闻纸、暖黑墨色、Spectral 正文上压 Zilla Slab 标题、Libre Franklin agate 排列表数字、细栏线下的两端对齐分栏、一条双线、一个干砖色信号
photo: mono
pictured: Broadsheet Front, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/newsprint.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Newsprint

浏览器里的一份大报：浅色新闻纸、暖黑墨色、平静的 Spectral 书卷衬线上压一颗钝感的 Zilla Slab 标题、细线与栏线管普通的分隔、双线管重要的分隔，以及一个干砖色信号，它绝不填充任何东西。照片黑白、带题注，像报纸印的那样。它读起来是报道与编辑出来的，不是装饰出来的。它不是圆角卡片的杂志，不是无衬线博客，也不是带陶土色按钮的奶油色编辑部模板。

## Tokens

```css
:root {
  --color-paper: oklch(94% 0.011 92); --color-paper-2: oklch(90.5% 0.015 88); --color-paper-3: oklch(87% 0.017 86);
  --color-ink: oklch(17% 0.012 60); --color-ink-2: oklch(27% 0.012 58); --color-muted: oklch(46% 0.014 60);
  --color-rule: oklch(68% 0.016 75); --color-rule-2: oklch(34% 0.012 60);
  --color-accent: oklch(44% 0.13 32); --color-accent-ink: oklch(95% 0.012 90); --color-focus: oklch(48% 0.17 32);
  --font-display: "Zilla Slab", ui-serif, Georgia, serif; --font-body: "Spectral", ui-serif, Georgia, serif;
  --font-outlier: "Libre Franklin", ui-sans-serif, sans-serif;
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px;
  --shadow-card: none;
  --tracking-display: -0.02em; --display-weight: 700;
}
```

## 字体

- **展示字体：**Zilla Slab 700、`--tracking-display`、行高 1.05、句首大写、正体，用于标题、导语（deck）和报头。括弧形衬线几乎与主干同重：守住这一个字重，让共享的字号阶梯去制造层级。
- **正文：**Spectral 400 与 500、1.0625rem、行高 1.55。钝感的粗衬线压在平静的书卷衬线上，这就是语气；Spectral 斜体只作行文中的强调。
- **署名、日期栏、题注、表头、元信息：**Spectral 500 小一档，句首大写，不加字距，用 `--color-muted`。
- **Agate，Libre Franklin 500：**报纸的分类栏字体，只用于划线列表或表格里的数字（时刻、价格、数量、结果），tabular、右对齐，字号与旁边正文一致。绝不做标签、标题或正文。每页三个字重：400、500、700。
- **分栏：**超过一段的行文可排成两或三栏两端对齐，用 `hyphens: auto` 和细栏线，每栏 28 到 40ch。
- **首字下沉：**可以给一段长文开头用，Zilla Slab 首字母约三行高，墨色或砖色，每页至多一次。

## 表面

- `--color-rule` 的细线承担普通分隔，分栏的行文带一条细栏线；双线，两条相距 2px 的 `--color-rule-2` 1px 线，是主题拥有的最重分隔，标记大的断裂处。
- 用线，绝不用盒子：圆角 0、任何地方无阴影。well 是上下划线的 `--color-paper-2` 场域，绝不是带边框的卡片。
- 色带：`--color-paper-2`，或一条 `--color-ink` 色带配纸张色文字；每页至多两条，绝不做砖色场域。
- 照片：黑白纪实，地点与它的人们，工作距离或背影，自然光，色调从纸白走向墨黑；头图宽幅，其余按报道裁切。方形，1px `--color-rule` 边框，无阴影。每张照片下方一行题注、署名腔，写一个事实；文字绝不压在照片上。
- 纹理，若用：一条色带上极淡的纤维颗粒（`texture.md` § 1），默认关闭，绝不垫在正文下。

## Range

- **分栏的头版：**一个 `--text-display-s` 的标题横跨整个版心，压在三栏两端对齐的 Spectral 之上，一个首字下沉、一条署名腔的日期栏；栏间 1px 栏线，上方一条双线。
- **分类信息用 agate：**一周日程、节目单或价目表排成划线行，日期或条目用 Zilla Slab、标题字号，那行说明用 Spectral，数字用 Franklin agate 靠右缘。
- **数字做成比分栏：**刊物自己的数字用 Zilla Slab、display 字号，夹在两条双线之间，每个下面一行 Spectral，栏线分隔。
- **墨色带：**一条公告在 `--color-ink` 上反白成纸张色（一个价格、一次订阅邀请），带它的表单；砖色在它上面只作细线，绝不作填充。

## 控件

- 控件对：一枚墨色填充矩形配纸张色文字，旁边一枚上下墨色划线的，两者方形，用 Zilla Slab 700、小一档。
- 链接砖色、1px 砖色下划线、hover 变粗；输入框方形，`--color-paper-2` 底上 1px `--color-rule-2` 边框。
- 砖色保持在 5% 以内：链接、焦点圈、线条上的一小段刻度；绝不作填充。

## 动效

只有状态：链接下划线 hover 变粗。无显现、无计数器，没有任何自动打字或自动滚动的东西。

## 语气

具体、陈述式，带干燥的编辑幽默：点名地点、日期与事实，标题要写得过得了版面编辑那一关，句首大写、句号结尾。

## 禁止事项

- 正文绝不用无衬线，标签也绝不用无衬线腔；细活全归 Spectral。
- 绝不用冷调或鲜艳的强调色；干砖色是家具，不是呐喊。
- 绝不用盒装卡片、阴影或圆角；结构由线条承担。
- Zilla Slab 绝不低于 700，也绝不用斜体；就一个钝感的正体字重。
- 绝不用彩色、调色或染色照片，也绝不用没有题注的照片。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@700&family=Spectral:ital,wght@0,400;0,500;1,400&family=Libre+Franklin:wght@500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: var(--display-weight); }
.rule--double { box-sizing: content-box; height: 2px; border: 0; border-block: var(--rule-hair) solid var(--color-rule-2); }
.cols { columns: 3 18rem; column-gap: var(--space-xl); column-rule: var(--rule-hair) solid var(--color-rule); text-align: justify; hyphens: auto; }
.agate { font: 500 1em/1 var(--font-outlier); font-variant-numeric: tabular-nums; }
.dropcap::first-letter { float: left; font: 700 3.4em/0.8 var(--font-display); padding-right: 0.06em; }
.btn { border: 0; background: none; border-radius: 0; padding: var(--space-md) var(--space-lg); font: 700 0.9375rem/1 var(--font-display); }
.btn--primary { background: var(--color-ink); color: var(--color-paper); }
.btn--secondary { border-block: var(--rule-hair) solid var(--color-ink); color: var(--color-ink); }
.well { background: var(--color-paper-2); border-block: var(--rule-hair) solid var(--color-rule); }
figure img { border: var(--rule-hair) solid var(--color-rule); }
figcaption { font: 500 var(--text-sm)/1.4 var(--font-body); color: var(--color-muted); padding-top: var(--space-xs); }
a { color: var(--color-accent); text-decoration-color: var(--color-accent); text-underline-offset: 0.16em; }
a:hover { text-decoration-thickness: 2px; }
::selection { background: color-mix(in oklab, var(--color-accent) 20%, transparent); }
```
