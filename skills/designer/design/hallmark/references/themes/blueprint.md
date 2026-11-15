---
name: Blueprint
slug: blueprint
genre: modern-minimal
paper: mid 35 256
display: geometric-sans Chakra Petch
accent: neutral 240
posture: drenched
keywords: architecture, architect, engineering, construction, structural, interiors, planning, surveying, cad, drafting, fabrication, prefab, developer, technical, spec, permit, renovation, build, drawings, architecture studio, timber
material: 普鲁士蓝图纸、白色线条墨色、IBM Plex Sans 上压 Chakra Petch 大写、等宽字测量值、方形双细线框与尺寸标注串、照片印成蓝晒图、白色线条是唯一信号
photo: duotone paper-3 ink con=30 exp=-10
pictured: Bento Grid, Poster hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/blueprint.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Blueprint

把制图纸当材质用：普鲁士蓝纸张、白色线条充当墨色、IBM Plex Sans 上压 Chakra Petch 制图大写、带单位的等宽测量值、细线框代替卡片、照片印成蓝晒图，阴影里是图纸的蓝、亮部是纸的白。它读起来是技术图纸，因为一切都是同一个底上的线、尺寸或印刷，而线是唯一信号。它不是带蓝色渐变的深色产品页，也不是霓虹线框。

## Tokens

```css
:root {
  --color-paper: oklch(35% 0.105 256); --color-paper-2: oklch(31% 0.10 257); --color-paper-3: oklch(26.5% 0.095 258);
  --color-ink: oklch(97% 0.012 240); --color-ink-2: oklch(90% 0.025 242); --color-muted: oklch(80% 0.045 244);
  --color-rule: oklch(93% 0.02 240 / 0.85); --color-rule-2: oklch(93% 0.02 240 / 0.32);
  --color-grid: oklch(97% 0.01 240 / 0.09); --color-grid-2: oklch(97% 0.01 240 / 0.2);
  --color-accent: oklch(97% 0.012 240); --color-accent-ink: oklch(33% 0.105 256); --color-focus: oklch(97% 0.012 240);
  --font-display: "Chakra Petch", ui-sans-serif, sans-serif; --font-body: "IBM Plex Sans", ui-sans-serif, sans-serif;
  --font-outlier: "IBM Plex Mono", ui-monospace, monospace;
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --rule-heavy: 2px; --shadow-card: none;
  --tracking-display: -0.012em; --display-weight: 600; --sheet-inset: 20px; --tick: 14px;
}
```

三种图纸，写进 stamp（`blueprint: cyanotype`）。

| 图纸 | 底色、线条、muted |
| --- | --- |
| **cyanotype**（默认） | 上面的 token |
| **whiteprint** | 底色 `oklch(97.5% 0.006 240)`，墨色 `oklch(35% 0.105 256)`，muted `oklch(52% 0.07 255)` |
| **brownline** | 底色 `oklch(86% 0.045 80)`，墨色 `oklch(28% 0.05 50)`，muted `oklch(45% 0.05 55)`，一支仅用于批注的红铅笔 `oklch(45% 0.19 28)` |

## 字体

- **展示字体：**所有标题用 Chakra Petch 600、`--tracking-display`、正体，每个标题一种字重：h1 与 h2 大写、行高 1.02（55a），h3 句首大写。
- **正文：**散文用 IBM Plex Sans 400，标签与控件用 500；浅色图纸上反转使用，最细不低于 400。
- **标签、题注、表头、元信息：**IBM Plex Sans 500 小一档，句首大写。IBM Plex Mono 500 只排带单位的测量值、阶段或图号、尺寸标注串上的年份和代码，别的什么都不排。

## 表面

- 只有线：每个表面 1px `--color-rule` 细线框，figure 或照片内部 5px 处再加一圈 `--color-rule-2` 细线框。圆角 0，无阴影；纵深是第二条线、一条 `--rule-heavy` 线，或深一档的底色。
- 尺寸标注串：一条细线，两端各有一个 45° 刻度（长 `--tick`）加短延长线，数值排在它上方。它量的是真实的东西，绝不是装饰。
- 网格：24px 小格线用 `--color-grid`，120px 大格线用 `--color-grid-2`，按 `--sheet-inset` 内缩，只垫在图纸、进度表或真实数据图表之下。
- 色带：`--color-paper-2` 或 `--color-paper-3`，每页至多两条；图纸本身就是颜色（drenched），没有别的场域。
- 照片：建成与在建的结构，正面平拍让它们读起来像图纸（正在升起的框架、从下方看的屋架、桌上的模型），在双细线框内印成蓝晒图；挑有真实白色与真实阴影的画面，灰色印出来是平的。照片上的文字从边缘起坐在 `--color-paper-3` 压暗层上。

## Range

- **数字当尺寸标注：**prompt 的那一个数字用 Chakra Petch、display 字号，排在一个横跨十或十二栏的尺寸标注串上，两端是它的两个真实端点（起始年份与现在、最小与最大跨度），端点用等宽字。
- **表格当图纸目录：**阶段进度表、交付物清单或价目表排成细线框表格，阶段号用等宽字单列一栏，行标题字重加一档，表头行下一条 `--rule-heavy` 线；放在 `--color-paper-2` 上读起来就是整套图的目录页。
- **表单当图签栏（title block）：**字段排成细线框块的单元格，每个标签在单元格左上，单元格大小由内容决定，提交按钮用墨色填充放在块底。
- **对比与步骤当立面图：**两个选项并排成列、中间一条重线分隔；或步骤沿一条长尺寸标注串排开、每步一个刻度，每步含数字、标题和一行字。

## 控件

- 主按钮墨色填充、图纸色文字，旁边次级按钮墨色 1px 描边，两者方形、48px、IBM Plex Sans 500。
- 链接墨色、1px 下划线、hover 时消失；输入框方形、48px，`--color-paper-2` 底上加 1px `--color-rule` 细线框，焦点圈用白色，绝不用辉光。
- 线就是强调色：蓝底上的白，用在线条、主按钮填充和焦点圈上。

## 动效

静态，制图感。一条线或一个尺寸标注串每页可自绘一次（scaleX 从左侧刻度起，时长 `--dur-long`、缓动 `--ease-out`）；可点击的细线框表面 hover 时底色加深一档。

## 语气

规格说明的语气：建筑类型、阶段、年份、格式，每个数字带单位；图纸注记装不下的东西一概不写。

## 禁止事项

- 绝不用填充卡片、模糊或浮起的面板；图纸只有线，没有层。
- cyanotype 上绝无第二种颜色，文字与照片都是；红铅笔只属于 brownline 图纸。
- 绝不用画出来的建筑、框架或剖面顶替真实项目，绝不用编造数值的尺寸标注串；图纸要么是真实项目数据，要么不出现。
- 绝不把网格当正文背后的壁纸；h1 与 h2 绝不小写。
- 绝无圆角，任何地方。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@600&family=IBM+Plex+Sans:wght@400;500&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: 600; }
h1, h2 { text-transform: uppercase; line-height: 1.02; }
.num { font-family: var(--font-outlier); font-weight: 500; }
.fig { position: relative; border: var(--rule-hair) solid var(--color-rule); }
.fig::after { content: ""; position: absolute; inset: 5px; z-index: 2; border: var(--rule-hair) solid var(--color-rule-2); pointer-events: none; }
.dim { position: relative; height: var(--rule-hair); background: var(--color-rule); }
.dim::before, .dim::after { content: ""; position: absolute; top: calc(var(--tick) / -2); width: var(--rule-hair); height: var(--tick); background: var(--color-rule); transform: rotate(45deg); }
.dim::before { left: 0; } .dim::after { right: 0; }
.btn { border: var(--rule-hair) solid var(--color-rule); border-radius: 0; background: transparent; color: var(--color-ink); padding: var(--space-sm) var(--space-lg); font-weight: 500; }
.btn--primary { background: var(--color-ink); border-color: var(--color-ink); color: var(--color-accent-ink); }
```
