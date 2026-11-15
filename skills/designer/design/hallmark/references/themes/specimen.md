---
name: Specimen
slug: specimen
genre: editorial
paper: light 96.5 82
display: high-contrast-serif Bodoni Moda
accent: cool 262
posture: restrained
keywords: typography, type specimen, foundry, letterform, portfolio, editorial, magazine, essay, type studio, agency, brand story, print, publication, craft, considered, literary
material: warm oat paper, warm near-black ink, razor-hairline Bodoni Moda over Geist, square 1px rules, one ink-blue signal that also draws the metric guides
photo: duotone ink paper con=8
pictured: Specimen Book, Poster hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/specimen.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Specimen

一家字库的材料：暖调燕麦纸、暖调近黑墨色、钉在最大光学字号上的 Bodoni Moda 400，发丝线在主笔画旁细到刀锋，之下是 Geist 正文，方正的 1px 横线与一个墨蓝信号色。它读起来像手工排版、精确无误，因为所有对比都住在字母内部，颜色与深度里没有一点。它不是带陶土色强调的奶油色奢华页，也不是粗壮 Didone 的时尚刊头。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(96.5% 0.016 82); --color-paper-2: oklch(93.5% 0.02 80); --color-paper-3: oklch(89% 0.024 78);
  --color-ink: oklch(17% 0.012 60); --color-ink-2: oklch(28% 0.014 60); --color-muted: oklch(49% 0.014 65);
  --color-rule: oklch(80% 0.018 75); --color-rule-2: oklch(66% 0.02 72);
  --color-accent: oklch(45% 0.18 262); --color-accent-ink: oklch(97% 0.012 82); --color-focus: oklch(50% 0.18 262);
  --color-guide: oklch(55% 0.16 262 / 0.5);
  --font-display: "Bodoni Moda", ui-serif, Georgia, serif; --font-body: "Geist", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "Geist Mono", ui-monospace, monospace;
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px;
  --shadow-card: none;
  --tracking-display: -0.02em; --display-weight: 400; --display-optical: 96;
}
```

`--color-guide` 是蓝色的第二档强度：一条半透明发丝线，作字高参考线（大写字高、x 字高、基线）画在词下，绝不做填色。`--color-rule-2` 是更深的发丝线，用于控件的滑轨或表格的表头。

## 字体（Type）

- **展示字体：**Bodoni Moda 400，`--tracking-display`，行高 1.02，句首大写，正体。`h1` 与 `h2` 取 `"opsz" 96`，发丝线在主笔画旁几乎消失，这组对比就是图形本身；`h3` 让光学轴随字号走，因为刀锋发丝线在 25px 会断。排成海报的一个词可以到 20vw。
- **正文：**Geist 400，17px，行高 1.55；Didone 之下的朴素无衬线就是张力所在。Bodoni Moda 斜体只留在行文或字例里，绝不做标题。
- **标签、图注、表头：**Geist 500 小一档，句首大写，用 `--color-muted`。Geist Mono 只用于相互比较的数字（字号、字重、码点），用表格数字。

## 表面（Surfaces）

- 分界、表格行与单元格之间用 1px `--color-rule` 发丝线；3px `double` 双线为页面上唯一重要的那张表起头，每页一次。
- 无深度：无浮起、无投影、无圆角。凹槽是发丝线内的一档纸面（`--color-paper-2`）。
- 色带：`--color-paper-2` 色带，或一条 `--color-ink` 色带配燕麦色文字，Didone 在其上最锐利；每页至多两条，绝不用蓝色。
- 照片：至多一张，字面的世界：阅览室、摊开在桌上的书、字盘里的金属活字；以墨色印在燕麦色上（双色调），如一块印版，方正，收在发丝线内，八列或整个容器。图注在其下方说明场景；文字绝不压在照片上。
- 无纹理、无网格、文字之后无渐变：燕麦是一种颜色，不是纸张扫描。

## 版式（Range）

- **带参考线的宣言：**一个词或一行排成海报字号，`--color-guide` 发丝线画在它真实的大写字高、x 字高与基线上，各以标签字体命名。
- **行排成瀑布：**一行字逐级坠落字号，每行左侧用 Geist Mono 标出它的字号，行间发丝线，每一行都裁到贴合所在行。
- **网格化作字符集：**发丝线单元格横跨十二列，一个四格宽的主格放一个展示字号的字形；当前格填墨色。
- **对比与价目：**墨色色带上正体与斜体并排，各排一段阅读字号；许可条款作为划线表格压在双线之下，价格用 Didone 排 `--text-display-s`。

## 控件（Controls）

- 一对：墨色填充的矩形配燕麦色文字，旁边是 1px 墨色描边的另一个，两者方正，Geist 500，48px 高。
- 滑杆是 1px `--color-rule-2` 滑轨配方形墨色滑块；开关是一根墨色发丝线里的两格方格，按下的那格用纸色、底下压一条 2px 墨线，墨色填色留给主按钮。输入框方正，焦点环用 `--color-focus`。
- 链接带 1px 墨蓝下划线，偏移 0.18em，悬停加粗。蓝色不超过一块屏幕的 5%：一个链接、焦点环、参考线、一个数字。

## 动效（Motion）

除状态外皆不动：下划线加粗，一格填色，字例接受给定的字号与字重。无显现，无循环，到来时无动作。

## 语气（Voice）

编辑腔、手工排版、略带文学气。动词优先于形容词；说出字面、字号、数字。

## 禁止事项（Do-nots）

- 绝不用重磅展示标题；加粗会把 Didone 变成时尚刊头。更重的字重只作为字族的字例出现。
- 绝不让 `h1` 或 `h2` 的光学字号低于 72；发丝线变胖是本主题最常见的失败。
- 绝不用暖色强调，也绝不用冷调纸面：信号色是墨蓝，暖意来自燕麦。
- 绝不画书、页面或设备来展示文字；把文字本身按它的字号排出来。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400&family=Geist:wght@400;500&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: var(--display-weight); letter-spacing: var(--tracking-display); line-height: 1.02; }
h1, h2 { font-variation-settings: "opsz" var(--display-optical); }
h3 { font-optical-sizing: auto; line-height: 1.15; }
.btn { min-height: 48px; border: var(--rule-hair) solid var(--color-ink); border-radius: var(--radius-card); padding: 0 var(--space-lg); font-weight: 500; }
.btn--primary { background: var(--color-ink); color: var(--color-paper); }
.btn--secondary { background: transparent; color: var(--color-ink); }
.guide { border-top: var(--rule-hair) solid var(--color-guide); }
.rule--double { border: 0; border-top: 3px double var(--color-rule-2); }
input[type="range"] { appearance: none; height: 1px; background: var(--color-rule-2); }
input[type="range"]::-webkit-slider-thumb { appearance: none; width: 16px; height: 16px; background: var(--color-ink); border-radius: 0; }
.photo > img { outline: var(--rule-hair) solid var(--color-rule); outline-offset: -1px; }
a { text-decoration-color: var(--color-accent); text-underline-offset: 0.18em; }
a:hover { text-decoration-thickness: 2px; }
```
