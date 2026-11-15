---
name: Terrazzo
slug: terrazzo
genre: modern-minimal
paper: light 96 82
display: geometric-sans Syne
accent: warm 38
posture: restrained
keywords: materials, library, architects, samples, catalogue, surfaces, stone, timber, terrazzo, ceramic, tile, interiors, interiors studio, showroom, specification, swatches, supplier, drawer, photography, tactile
material: off-white paper, white card surfaces ruled in ink over a hard offset, wide Syne heads over Onest, JetBrains Mono for codes and millimetres, surfaces photographed flat-on in true colour, rust the one signal
photo: natural con=4
pictured: Sample Drawer, Ledge hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/terrazzo.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Terrazzo

材料库的规格口吻：米白纸、近黑墨色，宽体 Syne 标题压在朴素的 Onest 正文之上，JetBrains Mono 负责编号与毫米数，白色卡板表面以 2px 墨线划格、压在硬偏移阴影上，装着平拍特写的材料本身。控件用墨色；颜色只以集合的方式出现，在照片呈现的石材、木材、水磨石与釉面里，铁锈色是唯一的信号。它像样品抽屉一样整理，像规格表一样阅读。它不是粉彩生活方式页，也不是五彩纸屑。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(96% 0.009 82); --color-paper-2: oklch(92% 0.012 82); --color-paper-3: oklch(87.5% 0.014 80);
  --color-plate: oklch(99.5% 0.003 82);
  --color-ink: oklch(16% 0.006 60); --color-ink-2: oklch(27% 0.006 60); --color-muted: oklch(46% 0.01 60);
  --color-rule: oklch(81% 0.012 80);
  --color-accent: oklch(53% 0.15 38); --color-accent-soft: oklch(91% 0.035 45); --color-accent-ink: oklch(99.5% 0.003 82); --color-focus: oklch(50% 0.16 38);
  --font-display: "Syne", ui-sans-serif, sans-serif; --font-body: "Onest", ui-sans-serif, sans-serif;
  --font-outlier: "JetBrains Mono", ui-monospace, monospace;
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --rule-bar: 2px;
  --shadow-card: 14px 14px 0 var(--color-paper-3); --shadow-card-hover: 14px 14px 0 var(--color-ink);
  --tracking-display: -0.025em; --display-weight: 700;
}
```

三种配色，写入 stamp（印记）：`terrazzo: off-white`。

| 配色 | 纸与墨 | 信号色与控件 |
| --- | --- | --- |
| **Off-white**（默认） | 上面的 token | 铁锈色；墨色控件 |
| **Black** | 底 `oklch(14% 0.005 60)`，上覆骨白墨 `oklch(96% 0.01 80)`；卡片保持白色 | 铁锈色提亮为 `oklch(68% 0.14 40)`；骨白控件配墨色文字 |
| **Stone** | 暖灰 `oklch(85% 0.012 80)` 底，墨色同上 | 铁锈色；墨色控件 |

## 字体（Type）

- **展示字体：**Syne 700，`--tracking-display`，行高 1.0，句首大写。这款字排出来很宽，所以标题宁可短也不降档；800 会显得笨拙，永不使用。展示字号的数字字距取 -0.04em。
- **正文：**Onest 400 与 500，行高 1.5。每页三种字重：400、500、700。
- **标签、图注、表头：**Onest 500，小一号，句首大写，不加字距。
- **编号与尺寸：**JetBrains Mono 500 用于样品编号（`ST-0412`）、毫米尺寸、表格中的计数；字号与旁边正文一致，绝不用作标签或标题。

## 表面（Surfaces）

- 横线：表格顶端、色带边缘、卡片四周压墨色 `--rule-bar`；行间用 `--color-rule` 的 `--rule-hair`。圆角处处为 0。
- 卡片：`--color-plate` 装在 `--rule-bar` 墨色边框里，压着硬 `--shadow-card`（paper-3 色，无模糊），是页面上唯一的容器；其余东西一律不投影。可点击卡片悬停时把偏移换成墨色。
- 色带：墨色色带配纸色文字，或 `--color-paper-2` 色带；绝无彩色色场，每页至多两条。
- 照片：材料表面本身，均匀日光下平拍特写，颗粒、缺口、纹理与接缝接近一比一可读；一组四张按同一比例成套。真彩，略加锐化。每张装进卡片，边贴边，下方图注写明类别与饰面；文字绝不压在照片上。
- 纸面上无纹理、无任何手绘：照片里的材料表面就是图案。

## 版式（Range）

- **规格表：**库存排成横贯全宽的表格，压在 `--rule-bar` 墨线之下：编号与尺寸用等宽字，表面名称用 Onest 500 的标题字号，类别与饰面用弱化色；悬停或选中行取 `--color-accent-soft`，编号转铁锈色。
- **墨色色带上的数字：**库里那个大数字用 Syne 排两倍 `--text-display`，纸色压墨色，旁边把类别或条款排成一小段划线列表。
- **步骤挂在横线上：**货真价实的有序列表，挂在发丝线上，每个数字用 Syne 排区块字号，阶段名用 Onest 500，旁边一句话。
- **表单作申请卡：**预约放在带硬偏移阴影的白色卡片上，输入框为直角、置于卡板色上，选项是边贴边的直角单元格，选中格墨色填充配纸色文字。

## 控件（Controls）

- 墨色填充主按钮配纸色文字，旁边是 `--rule-bar` 内嵌墨色描边按钮；两者都直角，Onest 500。墨色色带上主按钮转为卡板色底墨色字。
- 链接用墨色，发丝线下划线悬停转铁锈色；输入框直角，置于 `--color-plate`，1px 墨色边框。
- 铁锈色只落在编号、选中行或 chip、悬停下划线与焦点环上；其余颜色只来自照片。

## 动效（Motion）

静止。可点击卡片在 `--dur-micro` 内把偏移从 paper-3 换成墨色；被过滤掉的行离场无动画。

## 语气（Voice）

产品目录的平实：类别、饰面、编号、一比一的尺寸。绝不贩卖石材的氛围感。

## 禁止事项（Do-nots）

- 绝不手绘碎屑、斑点或彩纸；表面的颜色来自它的照片。
- 绝不用照片作背景或垫在文字下；它只活在卡片里。
- 米白纸上绝不用彩色主按钮；控件是墨色。
- 卡片、控件、照片上绝无圆角。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700&family=Onest:wght@400;500&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: 700; line-height: 1; }
.btn { border-radius: 0; padding: var(--space-md) var(--space-lg); font-weight: 500; color: inherit; }
.btn--primary { background: var(--color-ink); color: var(--color-paper); }
.btn--secondary { box-shadow: inset 0 0 0 var(--rule-bar) currentColor; }
.card { background: var(--color-plate); border: var(--rule-bar) solid var(--color-ink); box-shadow: var(--shadow-card); }
a.card { transition: box-shadow var(--dur-micro) var(--ease-out); }
a.card:hover { box-shadow: var(--shadow-card-hover); }
.band--ink { background: var(--color-ink); color: var(--color-paper); }
.band--ink .btn--primary { background: var(--color-plate); color: var(--color-ink); }
.spec { border-top: var(--rule-bar) solid var(--color-ink); } .spec tr:hover { background: var(--color-accent-soft); }
.code { font-family: var(--font-outlier); font-weight: 500; font-variant-numeric: tabular-nums; }
::selection { background: color-mix(in oklab, var(--color-accent) 25%, transparent); }
```
