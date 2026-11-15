---
name: Loom
slug: loom
genre: editorial
paper: light 95 85
display: roman-serif Libre Caslon Display
accent: cool 266
posture: committed
keywords: weaving, textile, linen, wool, weaving studio, cloth, craft, atelier, handmade, natural, indigo, fabric, by the metre, workshop, maker, slow, commission, interiors, samples
material: ecru paper with sand steps, warm near-black ink, Libre Caslon Display heads and prices over Hanken Grotesk, thin rules and one ink rule, cloth photographed close in window light, one deep indigo
photo: natural sat=-12 con=-4
pictured: Narrative Workflow, Poster hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/loom.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Loom

一间安静说话的织造工作室：米白纸、为展示而裁的 Caslon，带着书籍的沉静，压在朴素的 Hanken Grotesk 之上，细线横线，外加一处深靛蓝，即染好的纱线的颜色，只以色带或按钮出现，绝不做罩染。布料在窗光下近拍；绝不画任何东西来代替它。页面像花样册一样划线，所以读起来有手作感。它不是奶油配红陶的手工页，也不是在一切背后垫亚麻照片的页面。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(95.5% 0.014 85); --color-paper-2: oklch(92% 0.022 84); --color-paper-3: oklch(85% 0.032 80);
  --color-ink: oklch(21% 0.012 60); --color-ink-2: oklch(31% 0.012 60); --color-muted: oklch(46% 0.014 62);
  --color-rule: oklch(83% 0.022 84); --color-rule-ink: oklch(21% 0.012 60);
  --color-accent: oklch(34% 0.115 267); --color-accent-2: oklch(43% 0.125 267); --color-accent-ink: oklch(95.5% 0.014 85); --color-focus: oklch(43% 0.15 267);
  --font-display: "Libre Caslon Display", "Libre Caslon Text", ui-serif, Georgia, serif; --font-body: "Hanken Grotesk", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "DM Mono", ui-monospace, monospace;
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --rule-ink: 2px;
  --shadow-card: none;
  --tracking-display: -0.01em; --display-weight: 400;
}
```

三种配色，写入 stamp（印记）：`loom: ecru`。

| 配色 | 纸、墨、靛蓝 |
| --- | --- |
| `ecru`（默认） | 上面的代码块 |
| `indigo` | 纸 `oklch(34% 0.10 266)`，墨用米白 `oklch(95% 0.015 85)`，横线 `oklch(50% 0.09 266)`；按钮转为米白底靛蓝字 |
| `oat` | 纸 `oklch(88% 0.04 80)`，墨 `oklch(15% 0.01 60)`，横线用墨色 1px，靛蓝 `oklch(38% 0.10 266)` 只用于一条线和一个按钮 |

## 字体（Type）

- **展示字体：**Libre Caslon Display 400 用于 h1、每个 h2，以及 40px 以上的价格或数字，`--tracking-display`，行高 1.04（两行的 Hero 标题用 1.0），句首大写，正体。这款字只有一个字重、无斜体；绝不仿造两者，也绝不用在 32px 以下，那时它的发丝笔画会断裂。
- **条目标题（h3）：**Hanken Grotesk 500，`--text-title`，行高 1.25，用墨色。
- **正文：**Hanken Grotesk 400 与 500，16 至 18px，行高 1.5；导语用 `--color-muted`。
- **标签、图注、标记、表头：**Hanken Grotesk 500，小一号，句首大写，不加字距，用 `--color-muted`。DM Mono 只用于行内比较的数字（厘米计的幅宽、每米克重、织轴上的米数）和代码。

## 表面（Surfaces）

- 1px 横线：行间用 `--color-rule`；列表首行之上、表头之下、导航之下各压一条墨色 `--rule-ink`；内嵌面板无边框。
- 到处直角：内嵌面板、照片、输入框与控件圆角均为 0。
- 平坦：深度靠纸色分档，`--color-paper-2` 作色带或内嵌面板，沙色（`--color-paper-3`）作更深的内嵌面板；任何东西都不投影。
- 色带：`--color-paper-2` 色带，或一条靛蓝色带（`--color-accent` 底、`--color-accent-ink` 字）。每页至多两条。
- 照片：布与织机，近拍、窗侧光：织纹撑满画框、织轴上的经线、叠好的布匹、锥筒上的纱线；工作室全景只出现一次。颜色保持真实并稍作柔化（`photo:` 一行）。直角，向内 8% 的墨色描边，无阴影；下方图注用标签样式、承载一个事实（纤维、每米价格）；文字压在照片上时，必须垫在照片最平静一侧边缘的墨色蒙版之上。
- 无纹理：织纹交给照片。

## 版式（Range）

- **规格排成划线行：**纤维、幅宽、克重、交期与价格排成花样册单页，左侧标签用 Hanken，右侧值用 Caslon、标题字号起步，价格行排最大；首行之上压一条墨线。
- **价格作为数字：**每米价格用 Caslon 排展示字号，旁边是逐行算出的合计（米数、单价、总额），放在沙色内嵌面板上，或放在下单所在的靛蓝色带上。
- **时间排成刻度尺：**交期以周为单位画在 DM Mono 的发丝刻度上，布在机上的时段画成沙色横条，交付窗口画成靛蓝线；图表用提示词自己的周数，绝不画一根线头来代替。
- **两列对比：**亚麻对羊毛，中间一条墨线分隔，行对齐。

## 控件（Controls）

- 控件对：靛蓝填充的直角按钮，Hanken Grotesk 500，米白字；旁边是文字链接，带 2px 文字色底边框。在靛蓝底上，按钮转为米白底靛蓝字。
- 链接悬停时 2px 下划线转为 `--color-accent`；输入框直角，1px `--color-rule` 边框，靛蓝焦点环，靛蓝色带上为米白。
- 靛蓝只作填充或线条：主按钮、一条色带、悬停下划线、焦点环。

## 动效（Motion）

除状态外皆不动：下划线转靛蓝、主按钮变亮为 `--color-accent-2`，`--ease-out` 配 `--dur-short`，只此一次。

## 语气（Voice）

织工在织机旁平实地说话：纤维、米数、周数、布要去的那个房间。价格与时间只说一次，绝不硬卖。

## 禁止事项（Do-nots）

- ecru 配色下绝不用靛蓝做整页罩染或淡色调；它只能是色带、线条或填充。
- 标签绝不用等宽腔；幅宽与克重配得上等宽字，图注配不上。
- 绝不在页面上画尺子、经线或纱线图案；布靠照片，米数靠字体标价。
- 米白旁边绝不用暖色强调（铁锈、陶土、红陶）；沙色是纸，不是强调色。
- 绝无圆角、阴影或软卡片；Loom 只有横线、直角与纸色分档。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Hanken+Grotesk:wght@400;500&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: 400; line-height: 1.04; font-synthesis: none; }
.num { font-family: var(--font-outlier); font-variant-numeric: tabular-nums; }
.btn { display: inline-flex; align-items: center; padding: var(--space-md) var(--space-lg); font: 500 var(--text-sm)/1 var(--font-body); background: var(--color-accent); color: var(--color-accent-ink); transition: background-color var(--dur-short) var(--ease-out); }
.btn:hover { background: var(--color-accent-2); }
.link { font-weight: 500; padding-block: var(--space-2xs); border-bottom: 2px solid currentColor; text-decoration: none; transition: border-color var(--dur-short) var(--ease-out); }
.link:hover { border-color: var(--color-accent); }
.photo img { outline: 1px solid color-mix(in oklab, var(--color-ink) 8%, transparent); outline-offset: -1px; }
.photo figcaption { margin-top: var(--space-sm); font: 500 var(--text-sm)/1.4 var(--font-body); color: var(--color-muted); }
.band--indigo { background: var(--color-accent); color: var(--color-accent-ink); }
.band--indigo .btn { background: var(--color-paper); color: var(--color-accent); }
.band--indigo :focus-visible { outline-color: var(--color-accent-ink); }
```
