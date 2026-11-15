---
name: Kiln
slug: kiln
genre: atmospheric
paper: dark 13 40
display: high-contrast-serif Boska
accent: warm 45
posture: full-palette
keywords: kiln, ceramics, pottery, firing, glaze, heat, temperature, ceramics studio, craft, sensor, monitor, hardware, iot, warmth, dark, glow, schedule, workshop
material: near-black ground, cream ink, Boska over Geist, smoked wells, photographs lit by the work, a heat ramp that marks temperature, one ember signal
photo: warm sepia=50 sat=-12 con=8 exp=-6
pictured: Workbench, Stage hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/kiln.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Kiln

一间窑门半开的幽暗工坊：近黑的底色、奶白的墨色，Boska 的高反差衬线压在朴素的 Geist 之上，热度只出现在真正灼热的地方。照片承载火：一条从灰烬经牛血红、余烬与琥珀到白热的色阶，随温度攀升给温度着色。一处温热，其余皆冷。它不是带橙色按钮的暗色奢华页，也不是发光的渐变海报。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(13% 0.012 40); --color-paper-2: oklch(17.5% 0.016 40); --color-paper-3: oklch(22% 0.018 40);
  --color-ink: oklch(94% 0.02 80); --color-ink-2: oklch(84% 0.025 70); --color-muted: oklch(72% 0.03 60);
  --color-rule: oklch(96% 0.01 80 / 0.12);
  --color-accent: oklch(70% 0.2 45); --color-accent-ink: oklch(14% 0.02 40); --color-focus: oklch(76% 0.19 56);
  --heat-0: oklch(12% 0.012 40); --heat-1: oklch(22% 0.07 22); --heat-2: oklch(40% 0.16 27); --heat-3: oklch(60% 0.21 36);
  --heat-4: oklch(76% 0.19 56); --heat-5: oklch(89% 0.14 78); --heat-6: oklch(98% 0.04 95);
  --font-display: "Boska", "Iowan Old Style", Georgia, serif; --font-body: "Geist", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "Geist Mono", ui-monospace, monospace;
  --radius-card: 28px; --radius-well: 16px; --radius-pill: 999px; --rule-hair: 1px;
  --shadow-card: 0 50px 90px -30px oklch(8% 0.01 40 / 0.5);
  --tracking-display: -0.02em; --display-weight: 500;
}
```

三种配色，写入 stamp（印记）：`kiln: ember`。

| 配色 | 底色、墨色、强调色 |
| --- | --- |
| `ember`（默认） | 上面的代码块 |
| `bisque` | 底色 `oklch(96.5% 0.014 80)`，墨色 `oklch(20% 0.02 40)`，强调色 `oklch(54% 0.17 62)` 并以底色作其文字色；色阶从 `oklch(90% 0.035 75)` 起步；内嵌面板转为骨白色 |
| `reduction` | 底色 `oklch(21% 0.06 22)`，墨色 `oklch(95% 0.02 85)`，强调色 `oklch(84% 0.12 62)`；色阶从底色开始 |

## 字体（Type）

- **展示字体：**Boska 500，`--tracking-display`，行高 1.04，句首大写，正体，每个标题一种颜色；用它排的大字陈述可以放到 `--text-display`，行高 1.0。
- **数字：**承载叙事的温度、烧成时长或价格用 Boska 500，等高数字与表格数字，字距 -0.03em，单位（°C、h、£）用同一字体；孤立的大数字可以放到 Hero 标题的两倍。
- **正文：**Geist 400 与 500，16 至 18px，行高 1.55。
- **标签、图注、坐标轴刻度、表头：**Geist 500，小一号，句首大写，不加字距，用 `--color-muted`。Geist Mono 只出现在代码里。

## 表面（Surfaces）

- 行与行、内嵌面板边缘、图表网格线都用 1px 的 `--color-rule`；任何线都不比这更亮。
- 照片与成品界面圆角 28px，随视口缩小；内嵌面板与输入框用 `--radius-well`；控件用胶囊形。
- 内嵌面板是烟熏色的：`--color-paper-2`，比底色亮出清晰的一档，1px 细线描边，无阴影，绝不模糊，绝不嵌套。`--shadow-card` 是一道深而低的投影，只允许立在底色或照片之上的成品界面使用，绝不与描边环同用。
- 热度只标记温度，别无他用：色阶按段给烧成曲线上色，每一档温度一种颜色，低处牛血红、峰值白热，另加一条范围轨道（三个停靠点）。它绝不填充任何盒子、色带、槽位或底色，其上也不得压任何文字。
- 色带：`--color-paper-2` 色带，每页至多两条。
- 照片：作品本身，特写、弱光：达到温度的窑、装满的窑、釉、架上的器物、揉泥的手，由窑火、工作台灯或窗户照明，阴影沉入底色。28px 圆角边框，内嵌 1px 的奶白描边环，透明度 8%；压在照片上的文字只能落在暗面，底下垫 40 至 65% 的纸色蒙版。

## 版式（Range）

- 烧成制度排成行：每段的升温速率与目标温度用 Boska 数字，目标所在色阶档位以一小段色条标示。
- 读数或警示排成大字陈述：Boska、`--text-display`，横贯十列，奶白字压底色，旁边用 Geist 标钟点与窑号；屏幕上别无他物。
- 记录表横贯全宽：日期、窑次与测温锥用 Geist，峰值用 Boska 并对应其色阶档位，每行一条整段曲线的 sparkline，用 `--color-ink-2`。
- 价格或温度作为单个数字放在烟熏色色带上，操作按钮在其旁。

## 控件（Controls）

- 控件对：余烬色胶囊按钮（`--color-accent` 底、`--color-accent-ink` 字，Geist 500），高 50px，旁边是幽灵胶囊按钮，带 1px 内嵌 `--color-rule` 描边环，奶白文字。
- 输入框是 16px 圆角的烟熏色内嵌面板；滑杆（range）用 2px 轨道，沿色阶填充，滑块为 28px 余烬色圆点。
- 余烬色只作填充：主按钮、滑块、曲线上的实时点、`--color-focus` 的焦点环。所有文字保持奶白。

## 动效（Motion）

缓慢而有热度：颜色变化用 `--ease-out` 跑满 `--dur-long`，控件在 `--dur-short` 内响应。悬停时不脉动、不闪烁、不发光。

## 语气（Voice）

平静而具体，用陶艺师的话说：测温锥、温度、钟点、装窑量。说烧成，不说感受。

## 禁止事项（Do-nots）

- 绝不把色阶当填充：文字背后、底色上、槽位里、色带横跨处都不出现热渐变。
- 绝不出现橙色文字；余烬色只是填充，文字永远是奶白。
- 绝不让底色发棕或偏暖光；底色保持近黑，热度才有升腾之处。
- 绝不用明亮平光的照片，也不用白背景棚拍的器物。
- 色阶之外绝无第三种色相。
- 绝不每屏都是照片：火也活在曲线与数字里。

## 构建提示（Build hint）

```html
<link href="https://api.fontshare.com/v2/css?f[]=boska@500&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: var(--display-weight); line-height: 1.04; }
.btn { display: inline-flex; align-items: center; min-height: 50px; padding: 0 var(--space-lg); border-radius: var(--radius-pill); font-weight: 500; transition: background-color var(--dur-short) var(--ease-out); }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.btn--ghost { background: transparent; color: var(--color-ink); box-shadow: inset 0 0 0 var(--rule-hair) var(--color-rule); }
.well { background: var(--color-paper-2); border: var(--rule-hair) solid var(--color-rule); border-radius: var(--radius-well); }
.figure { font-family: var(--font-display); font-weight: var(--display-weight); letter-spacing: -0.03em; font-variant-numeric: lining-nums tabular-nums; }
.photo { border-radius: min(2vw, var(--radius-card)); outline: var(--rule-hair) solid color-mix(in oklab, var(--color-ink) 8%, transparent); outline-offset: -1px; }
.scrim { background: linear-gradient(to top, color-mix(in oklab, var(--color-paper) 65%, transparent), transparent 55%); }
.range-track { background: linear-gradient(to right, var(--heat-2), var(--heat-4), var(--heat-6)); }
::selection { background: color-mix(in oklab, var(--color-accent) 35%, transparent); }
```
