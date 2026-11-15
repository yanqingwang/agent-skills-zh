---
name: Formwork
slug: formwork
genre: editorial
paper: mid 74 80
display: display-condensed Oswald
accent: warm 38
posture: restrained
keywords: construction, concrete, skatepark, contractor, civil, landscape, foundry, industrial, fabrication, workshop, engineering, cast, welded, builders, hardware, tools, site, heavy
material: warm grey concrete paper with a speck grain, near-black ink, Oswald capitals over Archivo, square cast edges and hard shadows, hard black-and-white photographs of poured concrete, one safety orange signal
photo: natural sat=-100 con=35 exp=8
pictured: Site Board, Poster hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/formwork.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Formwork

工地办公室的口吻：暖灰混凝土作纸、近黑的墨色、Oswald 700 大写压在 Archivo 之上、浇筑出来的直角边缘、硬阴影，外加一处安全橙。它厚重而精确，因为表面是浇筑的，每条边都笔直，照片用黑白呈现混凝土本身，于是橙色成了页面上唯一的颜色。它不是黑黄相间的警示页，也不是光鲜的建筑作品集。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(74% 0.008 80); --color-paper-2: oklch(69% 0.009 80); --color-paper-3: oklch(64% 0.01 80);
  --color-plate: oklch(82% 0.007 80); --color-plate-ink: oklch(95% 0.006 80);
  --color-ink: oklch(18% 0.005 270); --color-ink-2: oklch(28% 0.006 80); --color-muted: oklch(31.5% 0.008 80);
  --color-rule: oklch(64% 0.01 80);
  --color-accent: oklch(66% 0.21 38); --color-accent-ink: oklch(18% 0.005 270); --color-focus: oklch(42% 0.15 38);
  --color-accent-deep: oklch(48% 0.17 38);
  --texture-opacity: 0.05;
  --font-display: "Oswald", ui-sans-serif, sans-serif; --font-body: "Archivo", ui-sans-serif, sans-serif;
  --font-outlier: "Archivo Narrow", ui-sans-serif, sans-serif;
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --rule-bar: 3px;
  --shadow-card: 6px 6px 0 var(--color-ink);
  --tracking-display: -0.005em; --display-weight: 700;
}
```

三种浇筑（配色），写入 stamp（印记）：`formwork: cast`。Muted 色只落在 paper 与 paper-2 之上；更深的底面上文字用墨色。

| 浇筑 | 墙面与墨色 | 橙色 |
| --- | --- | --- |
| **Cast**（默认） | 混凝土 `oklch(74% 0.008 80)` 压在近黑之上，颗粒以正片叠底铺满 | `oklch(66% 0.21 38)` |
| **Night pour** | 底 `oklch(27% 0.006 270)`，上覆 `oklch(95% 0.006 80)`，颗粒滤色 | `oklch(70% 0.21 40)` |
| **Drawing** | 描图纸 `oklch(95% 0.012 85)` 压蓝黑墨 `oklch(22% 0.02 260)`，无颗粒 | 一支红 `oklch(58% 0.21 30)` |

## 字体（Type）

- **展示字体：**Oswald 700，大写，`--tracking-display`，正体；行高 1.0 至 1.05（55a），只有不可换行的行才用 0.9。每个标题一种颜色。窄体，区块标题升一档（`--text-display-s` 及以上），孤立大数字可放到 20rem。
- **正文：**Archivo 400 与 500，16 至 17px，行高 1.5，用 `--color-ink-2`。
- **数字（outlier 字体）：**Archivo Narrow 500，表格数字，句首大写，用于测量与计数：毫米计的半径、深度、周数、公园编号。
- **标签、图注、表头、元信息：**Archivo 500，小一号，句首大写，不加字距。页面不出现等宽字体。

## 表面（Surfaces）

- 横线：区块或表格顶端压墨色 `--rule-bar`，行间用 `--color-paper-3` 的 `--rule-hair`。
- 一切圆角为 0；混凝土是贴着直木板浇筑的。
- 深度是浇筑出来的，绝不柔软：卡板用 `--color-plate`，加 `--rule-bar` 墨色边框与墨色的硬 `--shadow-card`，每页一两块；任何东西都不模糊。
- 色带：`--color-paper-2`（更深一档的浇筑）或一条墨色色带配 `--color-paper` 文字；绝不用橙色色场。每页至多两条。
- 照片：硬日光下近拍的作业中的混凝土：碗池与台面的交接、木板纹墙面、压顶与边缘、浇筑与抹平，滑手只从背后或远景入镜。硬朗的黑白，白要干净、黑要深沉（即 `photo:` 一行），照片因此从灰纸面上跳出来，橙色保持唯一颜色。直角，2px 墨色边框，无阴影；下方图注用标签样式；压在照片上的文字必须垫从边缘起的墨色蒙版。
- 纹理，即颗粒：`texture.md` § 1 以 `--texture-opacity`（0.05，因此可垫在正文之下）铺满整张纸，正片叠底，夜间浇筑改滤色；纸面读起来像浇筑物，靠的就是它。

## 版式（Range）

- **浇筑成卡板的数字：**提示词中那个真实计数用 Oswald 排到 14 至 20rem，放在带硬阴影的卡板上，单位与计数对象用 Archivo 写在旁边。
- **步骤排成浇筑顺序：**三四个阶段横跨十二列，压在 `--rule-bar` 之下，每段一个 Oswald 数字（`--text-display-s`）、一个单词的阶段名与一句平实说明，列间用 `--color-paper-3` 竖线分隔。
- **对比排成两块卡板：**两类受众或两件事并排，各一块卡板，行间发丝线；橙色只落在唯一的那一个动作上。
- **墨色色带上的陈述：**一行 Oswald 大写、展示字号，`--color-plate-ink` 色压在 `--color-ink` 上，颗粒改滤色。

## 控件（Controls）

- 控件对：橙色主按钮由硬 `0 3px 0` 的 `--color-accent-deep` 阴影抬起，`:active` 时下压 3px；旁边是凹陷式次按钮（`inset 0 2px 3px`，2px 墨色边框）。两者都用 Oswald 700 大写，不加字距，跟随展示字体；单选的标签就是普通标签，Archivo 句首大写。
- 链接用墨色、带下划线，悬停转橙；输入框像次按钮一样凹陷。
- 橙色保持在一屏的 5% 以内：主按钮、一个数字、焦点环。

## 动效（Motion）

混凝土不动。控件在 `--dur-micro` 内以 `--ease-out` 按下；状态即时落定。滚动无事发生，也无环境动效。

## 语气（Voice）

工长的白话：浇筑了什么、在哪里、给谁用、何时开放。句子短，每个数字带单位。

## 禁止事项（Do-nots）

- 绝无圆角、模糊阴影或第二种强调色；硬阴影与橙色就是材质本身。
- 绝不手绘混凝土（板缝、对拉螺栓孔、裂缝、警示条纹）；拍照。
- 橙色在侧时绝不用彩色照片；照片一律黑白。
- 绝不用小写或细字重的 Oswald；它就是 700 大写。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Archivo:wght@400;500&family=Archivo+Narrow:wght@500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: 700; text-transform: uppercase; }
.btn { border-radius: 0; padding: var(--space-sm) var(--space-xl); font: 700 var(--text-sm)/1.6 var(--font-display); text-transform: uppercase; }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); box-shadow: 0 3px 0 var(--color-accent-deep);
  transition: translate var(--dur-micro) var(--ease-out), box-shadow var(--dur-micro) var(--ease-out); }
.btn--primary:active { translate: 0 3px; box-shadow: 0 0 0 var(--color-accent-deep); }
.btn--secondary { background: var(--color-paper-2); color: var(--color-ink); border: 2px solid var(--color-ink); box-shadow: inset 0 2px 3px color-mix(in oklab, var(--color-ink) 30%, transparent); }
.card { background: var(--color-plate); border: var(--rule-bar) solid var(--color-ink); box-shadow: var(--shadow-card); }
.photo img { outline: 2px solid var(--color-ink); outline-offset: -2px; }
.band--cast { position: relative; isolation: isolate; background: var(--color-paper-2); }
::selection { background: color-mix(in oklab, var(--color-accent) 35%, transparent); }
```
