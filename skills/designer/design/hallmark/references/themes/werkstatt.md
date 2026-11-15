---
name: Werkstatt
slug: werkstatt
genre: playful
paper: mid 84 82
display: geometric-sans Jost
accent: cool 264
posture: full-palette
keywords: school, programme, workshop, maker, course, bootcamp, academy, apply, admissions, tuition, timetable, bauhaus, craft, design education, design school, residency, cohort, prospectus
material: warm putty ground with a lighter well, near-black ink, Jost 700 capitals and numerals over Karla, square 2px and 3px ink rules that box cells, flat ultramarine, vermilion and yellow primaries
photo: mono
pictured: Catalogue, Settled hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/werkstatt.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Werkstatt

设计学校的印刷招生简章：暖调腻子色底、近黑墨色，厚重的 Jost 大写压在朴素的 Karla 正文之上，直角的 2px 与 3px 墨线，三种平涂原色（蓝、红、黄），各司一职。照片是各工坊作业的黑白记录。它读起来像上了课、有底气，像钉在工坊墙上的一份课程表：事实装进划线格子里，日期与数字排得和标题一样大。它不是玩具盒配色，也不是彩纸屑图案。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(84% 0.024 82); --color-paper-2: oklch(79.5% 0.028 80); --color-paper-3: oklch(89.5% 0.018 84);
  --color-ink: oklch(18% 0.008 60); --color-ink-2: oklch(27% 0.01 60); --color-muted: oklch(39% 0.014 62);
  --color-rule: oklch(58% 0.022 72);
  --color-accent: oklch(46% 0.2 264); --color-accent-2: oklch(58% 0.205 33); --color-accent-2-deep: oklch(50% 0.19 31); --color-accent-3: oklch(85% 0.165 92);
  --color-accent-ink: oklch(96% 0.012 82); --color-focus: oklch(46% 0.2 264);
  --font-display: "Jost", "Futura", sans-serif; --font-body: "Karla", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "JetBrains Mono", ui-monospace, monospace;
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --rule-bar: 2px; --rule-box: 3px;
  --shadow-card: none;
  --tracking-display: -0.005em; --display-weight: 700;
}
```

三种配色，每页设定一次，写入 stamp（印记）：`werkstatt: putty`。

| 配色 | 底色、墨色、原色 |
| --- | --- |
| `putty`（默认） | 上面的代码块 |
| `blackboard` | 底 `oklch(17% 0.005 60)`，墨 `oklch(90% 0.015 80)`，横线 `oklch(38% 0.01 60)`，原色整体提亮一档；腻子色回归作内嵌面板色 |
| `blue` | 底 `oklch(50% 0.22 265)`，墨 `oklch(93% 0.02 85)`，横线 `oklch(64% 0.14 265)`；黄色承担强调色的职责 |

## 字体（Type）

- **展示字体：**Jost 700，大写，`--tracking-display`，行高 1.02，使用共享的字号阶梯。大写就是材质：每个标题都用大写排。数字与日期也用同一字体，展示字号起步，表格数字，待在自己的格子里。
- **正文：**Karla 400，行高 1.5。
- **标签、图注、标记、表头：**Karla 600，小一号，句首大写，不加字距，用 `--color-muted`。小号数字与价格用 Karla 加 `tabular-nums`；等宽字体只出现在代码里。
- **控件：**Karla 600 大写，跟随展示字体（大写页面下 67 号大小写闸门允许），不加字距。

## 表面（Surfaces）

- 横线：`--rule-box` 墨线把网格框住并交叉分割，`--rule-bar` 墨线压在导航之下与每张表格之上，行间用 `--color-rule` 的 `--rule-hair`。卡片没有背景；格子就是横线圈出的东西。
- 圆角为零、阴影为零，处处如此。
- 色带：`--color-paper-2` 色带，或 `blackboard` 配色下一条纸色文字的 `--color-ink` 色带，或一块 `--color-accent-ink` 文字的蓝色色场；每页至多两条色带。`--color-paper-3` 是划线格内的内嵌面板，绝不是色带。
- 照片：各工坊作业中，纪实而平实，台面高度或略高于台面：工作台与它的工具、刨木的手、印刷机或陶轮，木料、铅字与陶土近到能看清纹理；日光，无人正对镜头。印成黑白（`photo:` 的 mono），原色因此保持唯一颜色；直角，`--rule-bar` 墨色边框，与周围格子齐平。工坊的原色作平涂格或色条，放在照片旁边或下方并承载图注；它绝不给照片加色罩，文字也绝不压在照片上。
- 无纹理，任何地方都无渐变。

## 版式（Range）

- **数字装进格子里：**提示词的真实数字用 Jost 700 排展示字号，各自待在十二列中自己的 `--rule-box` 格里，标签用 Karla 放在下方；不用原色，因为同类成组不取色。
- **日期排成划线日程：**截止日与学期排成大写字母的行，与区块标题一样大，日期在左，事项在右，首行之上压 `--rule-bar`。
- **类别排成编码网格：**每个工坊、方向或教室占自己的原色格，与相邻格齐平，填充之上放一张黑白照片或一份内容清单。
- **表单排成划线单张：**字段装进像报名表一样的格子网格，类别选择用它的原色，提交按钮是页脚的墨色块。

## 控件（Controls）

- 透明 `--rule-bar` 墨色边框按钮，旁边是墨色填充按钮，两者直角；墨色色带上这一对反转：填充者转为腻子色底墨色字，绝不用原色，因为原色编码类别。
- 链接带 2px 墨色下划线，悬停加粗到 3px；输入框直角，`--rule-bar` 墨色边框。
- 原色是平涂填充，绝不当文字色，也绝不做淡色调。每种原色编码一个类别，出现在哪里（格子、标记、色带、导航链接）都是同一类别，且同类成组不取色。蓝与红填充用 `--color-accent-ink` 文字，红加深为 `--color-accent-2-deep`；黄填充用墨色文字。蓝还负责焦点环。

## 动效（Motion）

静态，如印刷的招生简章：链接下划线悬停加粗，其余一切不动、不显现、不循环。

## 语气（Voice）

朴素的学校文体：工坊、周数、学费、截止日，每样只说一次，说得平实。

## 禁止事项（Do-nots）

- 绝无第四种颜色、原色的淡色调、当作文字色的原色，或彩色照片。
- 容器、按钮、图片上绝无圆角；Werkstatt 是直角的。
- 展示字体绝不用大小写混排；这里的 Jost 只用大写。
- 原色绝不当彩纸屑或图案用；每一块填充都指一个类别。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@700&family=Karla:wght@400;600&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: 700; line-height: 1.02; text-transform: uppercase; }
small, th, figcaption { font-weight: 600; color: var(--color-muted); }
.btn { display: inline-flex; align-items: center; gap: var(--space-xs); padding: var(--space-md) var(--space-lg); border: var(--rule-bar) solid currentColor; font: 600 var(--text-sm)/1 var(--font-body); text-transform: uppercase; color: inherit; background: transparent; }
.btn--primary { background: var(--color-ink); border-color: var(--color-ink); color: var(--color-paper); }
.band--ink { background: var(--color-ink); color: var(--color-paper); }
.band--ink .btn--primary { background: var(--color-paper); border-color: var(--color-paper); color: var(--color-ink); }
.ruled { border-block: var(--rule-box) solid var(--color-ink); }
.photo { border: var(--rule-bar) solid var(--color-ink); border-radius: 0; }
table { border-top: var(--rule-bar) solid var(--color-ink); } td { border-bottom: var(--rule-hair) solid var(--color-rule); }
a { text-decoration-thickness: 2px; } a:hover { text-decoration-thickness: 3px; }
::selection { background: var(--color-accent-3); color: var(--color-ink); }
```
