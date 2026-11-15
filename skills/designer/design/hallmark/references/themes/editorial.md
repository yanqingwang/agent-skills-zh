---
name: Editorial
slug: editorial
genre: editorial
paper: light 97 86
display: display-condensed Bricolage Grotesque
accent: chromatic-green 152
posture: restrained
keywords: magazine, editorial, feature, culture, fashion, design annual, interview, longform, publication, issue, contemporary, art direction, profile, lookbook, brand story, journal, considered, travel, city guide, guide
material: warm white uncoated stock, printed black ink with a cool tilt, Bricolage Grotesque condensed at 800 over Source Serif 4, square corners, a heavy ink rule over 1px hairlines, one printer's green
photo: natural sat=-10 con=4
pictured: Marquee Hero, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/editorial.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Editorial

一本当代杂志的声音：暖白非涂布纸、微微偏冷的印刷黑（行文同样用它）、Bricolage Grotesque 挤到宽度 75 的 800 作每个标题、Source Serif 4 做阅读与导语、方正的角、1px 发丝线上的重磅墨线、一种印刷绿。窄体标题、衬线导语与那条线承担一切，不靠装饰。它不是衬线文学期刊，不是奶油底陶土色，也不是带图注照片的画廊。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(97% 0.007 86); --color-paper-2: oklch(94% 0.010 86); --color-paper-3: oklch(91% 0.012 84);
  --color-ink: oklch(16% 0.012 280); --color-ink-2: oklch(29% 0.011 280); --color-muted: oklch(48% 0.010 75);
  --color-rule: oklch(85% 0.009 85); --color-rule-2: oklch(64% 0.010 80);
  --color-accent: oklch(49% 0.130 152); --color-accent-ink: oklch(98% 0.005 88); --color-focus: oklch(52% 0.135 152);
  --font-display: "Bricolage Grotesque", ui-sans-serif, sans-serif; --font-body: "Source Serif 4", ui-serif, Georgia, serif;
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --rule-heavy: 4px; --shadow-card: none;
  --tracking-display: -0.012em; --display-weight: 800;
}
```

## 字体（Type）

- **展示字体：**Bricolage Grotesque 800 加 `"wdth" 75, "opsz" 96`，`--tracking-display`，句首大写，正体。Hero 字号行高 0.92，标题 1.0。窄体，所以升一档：章节标题可以排到 `--text-display-s`，独词 Hero 可以到两倍 `--text-display`。一个标题一个字重、一种颜色。
- **正文：**Source Serif 4 400 及其斜体，18px，光学字号自动，行高 1.55，行文用旧式数字，用 `--color-ink-2`。导语（标题下那行，或一句陈述）用同一字面，`--text-lead` 到 `--text-display-s`，墨色，大字号端行高 1.2。引语用斜体；斜体绝不进标题。
- **标签、图注、导航链接、控件、表头、署名：**Bricolage Grotesque 500，`"opsz" 12`，全宽，小一档，句首大写，不加字距；图注用 `--color-muted`。用展示字面排的数字用等高表格数字。页面上没有等宽。

## 表面（Surfaces）

- 两种线宽：`--rule-heavy` 墨线为一节或一张表起头，表头紧贴其下；1px `--color-rule` 发丝线分隔行、列与数字，表头之下用 `--color-rule-2`。什么都不装框，什么都不投影。
- 一切圆角 0：控件、标签、输入框、凹槽与照片都是锋利的矩形。
- 深度是一档纸面：凹槽是 `--color-rule-2` 发丝线之下的 `--color-paper-2`，绝不是抬起的卡片。
- 色带：一个 `--color-paper-2` 凹槽与一条 `--color-ink` 色带配 `--color-paper` 文字，每页至多两条；绝不用绿色色带。
- 照片：近看：工作的手、案上的物件、日光下的房间、印出来的页面。柔和窗光，人物从背后，绝不正对镜头的脸；比生活安静一点，方正，8% 内嵌墨色描边，通栏或齐列边裁切。标题只在作为封面语时横过照片，每页一次，压一层墨色暗化。首屏之下两三张大图；其余交给材料。
- 无纹理、无颗粒、无网格。

## 版式（Range）

- **目录化作行：**重磅墨线之下三到六行发丝线行，左侧窄体标题约 40px，右侧衬线导语，最边上展示字面的页码或日期。
- **导语化作陈述：**一或两句 Source Serif，`--text-display-s` 字号，墨色横跨十列压在重磅墨线之下；衬线在那个字号上与标题同为这个主题的骨血。
- **数字反白：**墨色色带上，提示词的三四个数字用窄体标题排 `--text-display`，发丝线分隔，下方配标签。
- **订单化作规格单：**表单压在 paper-2 凹槽上，事实排成字段旁的划线表格，合计用展示字面，随数量变化原位更新。

## 控件（Controls）

- 墨色填充的方块（`--color-paper` 压 `--color-ink`）旁边是 1px 墨色描边的方块，两者都用标签字体，48px 高；标签可以是唯一的绿色填充矩形。
- 链接带发丝线下划线，悬停转绿；输入框与下拉方正，52px 高，1px `--color-rule-2` 边框，聚焦转墨色。
- 绿不超过一块屏幕的 5%：一次悬停、一个标签、焦点环。

## 动效（Motion）

只动状态：链接之下一条绿色下划线以 `--dur-short`、`--ease-out` 长出，一个方块深一档，合计原位变化。无显现，滚动时无动作。

## 语气（Voice）

当代、略带文学气、精确。说出期号、页数、日期；标题读起来像封面语，导语一口气说完论点。

## 禁止事项（Do-nots）

- 绝不用衬线标题；Source Serif 4 只排阅读文字、导语与引语，绝不排 `h1` 到 `h3`。
- 绝不让 Bricolage 用默认宽度；没有 `"wdth" 75`，标题就丢了杂志的比例。
- 绝不用圆角、胶囊、阴影或绿色横线。
- 绝不让两个图片区块相邻；每个之后接行、导语或数字。
- 绝不全大写喊叫；句首大写、紧凑、杂志式的当代。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,500..800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;1,8..60,400&display=swap" rel="stylesheet">
```

```css
body { color: var(--color-ink-2); font-optical-sizing: auto; font-variant-numeric: oldstyle-nums; }
h1, h2, h3 { font-weight: var(--display-weight); font-variation-settings: "wdth" 75, "opsz" 96; color: var(--color-ink); font-variant-numeric: lining-nums tabular-nums; }
small, figcaption, th, nav, label, .btn, .tag { font-family: var(--font-display); font-weight: 500; font-variation-settings: "opsz" 12; }
.standfirst { font: 400 var(--text-display-s)/1.2 var(--font-body); color: var(--color-ink); }
.opens { border-top: var(--rule-heavy) solid var(--color-ink); padding-top: var(--space-lg); }
.btn { border: var(--rule-hair) solid var(--color-ink); border-radius: 0; min-height: 48px; padding: 0 var(--space-lg); }
.btn--primary { background: var(--color-ink); color: var(--color-paper); }
.btn--secondary { background: none; color: var(--color-ink); }
.tag { background: var(--color-accent); color: var(--color-accent-ink); padding: var(--space-3xs) var(--space-xs); }
.well { background: var(--color-paper-2); border-top: var(--rule-hair) solid var(--color-rule-2); }
.photo > img { outline: 1px solid color-mix(in oklab, var(--color-ink) 8%, transparent); outline-offset: -1px; }
a { text-decoration-color: var(--color-rule-2); text-underline-offset: 0.2em; } a:hover { text-decoration-color: var(--color-accent); }
::selection { background: color-mix(in oklab, var(--color-accent) 22%, transparent); }
```
