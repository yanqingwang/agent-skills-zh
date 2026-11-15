---
name: Overprint
slug: overprint
genre: playful
paper: light 91.5 92
display: grotesk-heavy Anybody
accent: cool 212
posture: full-palette
keywords: venue, gigs, live music, festival, music, label, print studio, bar, club, poster, tickets, events, nightlife, two-colour, screenprint, punk, zine, loud, listings, door
material: grey newsprint stock, near-black ink, wide heavy Anybody capitals over Archivo, flat square fills, a teal pass and an orange pass that print moss where they cross, photographs pulled through one pass
photo: mono con=30
pictured: Marquee Hero, Poster hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/overprint.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Overprint

廉价纸面上的双色丝网印刷：灰色新闻纸、近黑的油墨、宽而重的 Anybody 大写字母压在朴素的 Archivo 正文之上，再加青绿与橙两版透明平涂油墨，交叠处印出深苔绿。照片只经一版硬印，如同演出账单印出来的那样。全部套准，平整方正：画面的噪音来自字号与两版油墨，绝不来自特效。它不是复古海报的仿作，不是套印错位的次品，也不是霓虹传单。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(91.5% 0.014 92); --color-paper-2: oklch(87.5% 0.018 90); --color-paper-3: oklch(83% 0.021 88);
  --color-ink: oklch(17% 0.008 60); --color-ink-2: oklch(29% 0.01 60); --color-muted: oklch(42% 0.012 70);
  --color-rule: oklch(78% 0.02 85);
  --color-accent: oklch(65% 0.12 212); --color-accent-ink: oklch(17% 0.008 60); --color-focus: oklch(44% 0.1 220);
  --color-accent-2: oklch(71% 0.19 50); --color-accent-2-ink: oklch(17% 0.008 60);
  --color-mix: oklch(35.5% 0.121 142);
  --blend: multiply; --texture-opacity: 0.06;
  --font-display: "Anybody", ui-sans-serif, sans-serif; --font-body: "Archivo", ui-sans-serif, sans-serif;
  --font-outlier: "Archivo Narrow", ui-sans-serif, sans-serif;
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --rule-bar: 4px;
  --shadow-card: none;
  --tracking-display: -0.01em; --display-weight: 900; --display-stretch: 140%;
}
```

两版油墨永远是墨字之下的平涂填色，绝不是文字本身；苔绿是 multiply（正片叠底）在两版交叠处印出的结果，绝不手绘。两种纸面，写入 stamp（印记）：`overprint: newsprint` 为新闻纸，即上面的 Token；或黑色纸面，`oklch(20% 0.01 280)` 之上覆 `oklch(95% 0.01 90)`，混合模式翻转为 screen（滤色），交叠处变浅，两版分别用黄 `oklch(88% 0.17 95)` 与水色 `oklch(78% 0.13 200)`，焦点用水色。

## 字体（Type）

- **展示字体：**Anybody 900，加宽排版（`--display-stretch`，130 至 150%），全大写，行高 1.0 至 1.02，`--tracking-display`。数字、钟点与价格用同一设置排到 150% 宽，并加 `tabular-nums`。
- **正文：**Archivo 400 与 600，16 至 17px，行高 1.5，用墨色。
- **小字：**Archivo Narrow 600，再小一档，句首大写，不加字距，用于日期、钟点与表头：即标签字体。图注用 Archivo。不用等宽字体。

## 表面（Surfaces）

- 两版油墨：所有带颜色的东西要么是第 1 版、要么是第 2 版，以 `mix-blend-mode: var(--blend)` 平涂填色，两版交叠处纸面印出 `--color-mix`；文字绝不落在苔绿上。
- 横线：4px 墨色 `--rule-bar` 压在列表、表格、图片行或导航的顶部；行间用 `--color-rule` 的 `--rule-hair`。
- 圆角 0，无阴影；除照片的压暗层外无渐变：深度来自叠印，绝不来自浮起。
- 色带：`--color-paper-2` 色带、墨色色带配纸色文字，或单版色场配墨色文字；每页两条。
- 照片：夜晚，近景或背影，在被演出的那束光下拍摄（同一片光下的人群、按在指板上的手、开门时的吧台）；绝不摆拍，绝无正对镜头的脸。灰调、硬朗，以 multiply 压到一版色场上，灯光因此印成青绿或橙、暗部印成墨色；方正，通栏或齐列边，无框。文字放在图片旁边，或压一层墨色暗化、在图片最暗处镂空出纸色。
- 纹理：颗粒（`texture.md` § 1）以 `--texture-opacity` 用在色带、单版色场或照片上，绝不压在正文之下。

## 版式（Range）

- **数字排成演出账单：**提示词自带的钟点、容量或价格，用宽体 Anybody 排成海报字号，每个数字独占一版色场；两场隔列交叠，交叠处印出苔绿，任何字母都不落进去。
- **节目单排成划线表格：**4px 墨线之下，表头用 Archivo Narrow，乐队名用标题字号的大写宽体，日期与价格用表格数字；开票单元格用第 1 版，售罄单元格用第 2 版。
- **步骤排成编号票券：**流程分为三四格压在墨线之下，每个数字宽而重，每格交替灌满一版油墨。
- **一条墨色色带：**黑场配纸面文字与颗粒，承载一句宽体大写的宣言，或一个带第 1 版控件的表单。

## 控件（Controls）

- 控件对：第 1 版填充配 `--color-accent-ink` 文字，Archivo Narrow 600 大写、不加字距（67 允许在大写展示之下这样用），旁边是 2px 内嵌墨色描边（墨底上用纸色）。
- 第 1 版用于主按钮与展开态；第 2 版用于收起态（售罄）。链接用墨色加 2px 第 1 版下划线，悬停转墨色；输入框方正，用 2px 内嵌墨色描边。

## 动效（Motion）

印刷机不做补间：悬停时主按钮瞬间换到另一版油墨（青绿换橙），按下加深一个墨阶，其余一律不做：无显现、无悬浮、无循环。

## 语气（Voice）

墙上的演出账单：谁演出、哪一晚、几点开门、票价多少、卖完了没有。

## 禁止事项（Do-nots）

- 绝无第三种油墨：苔绿只由交叠印出，绝不混进任何填色、控件或字母。
- 绝不脱版或错位排布：无回声、无偏移副本、无重新着色的词、无幻影副标题。
- 绝不用彩色照片，也绝不让照片经两版印刷。
- 绝不为炫耀叠印而画形状；两版油墨印的是页面本就有的表面。
- 绝不用小写或窄体展示字体；重型怪诞体就是大声、加宽的。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Anybody:wdth,wght@100..150,900&family=Archivo:wght@400;600&family=Archivo+Narrow:wght@600&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: 900; font-stretch: var(--display-stretch); text-transform: uppercase; line-height: 1.02; }
.btn { border: 0; border-radius: 0; padding: var(--space-md) var(--space-lg); font: 600 var(--text-sm) var(--font-outlier); text-transform: uppercase; }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); } .btn--primary:hover { background: var(--color-accent-2); }
.btn--secondary { box-shadow: inset 0 0 0 2px var(--color-ink); color: var(--color-ink); }
.pass-1 { background: var(--color-accent); color: var(--color-accent-ink); mix-blend-mode: var(--blend); }
.pass-2 { background: var(--color-accent-2); color: var(--color-accent-2-ink); mix-blend-mode: var(--blend); }
.pass-1 > img, .pass-2 > img { filter: grayscale(1) contrast(1.3); mix-blend-mode: var(--blend); }
.figure { font: 900 var(--text-display)/1 var(--font-display); font-stretch: 150%; font-variant-numeric: tabular-nums; }
.grain { position: relative; isolation: isolate; }
.grain::after { content: ""; position: absolute; inset: 0; pointer-events: none; opacity: var(--texture-opacity); background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 -4'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E") 0 0 / 200px; }
::selection { background: color-mix(in oklab, var(--color-accent-2) 40%, transparent); }
```
