---
name: Hedgerow
slug: hedgerow
genre: editorial
paper: dark 24 158
display: high-contrast-serif Prata
accent: chromatic-green 118
posture: drenched
keywords: distillery, gin, brewery, forager, botanicals, nature reserve, walking, trail, seeds, plants, nursery, hedge, countryside, field guide, provenance, harvest, batch, seasonal, map, miles
material: 深叶绿纸张、奶油色墨色、Manrope 上压 Prata 标题、真色调低照度照片、方形平面配胶囊控件、一个黄绿信号色并带一个奶油底上可用的苔藓强度
photo: natural sat=-10 con=8 exp=-8
pictured: Field Guide, Poster hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/hedgerow.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Hedgerow

一个读起来是绿色而非黑夜的深色页面：深叶绿底色、奶油色墨色、安静的 Manrope 上压 Prata 锐利的高对比标题、荫蔽处凑近拍摄的植物，以及一个黄绿色，用来标记控件和页面画出的少数几条线。感觉是植物学的、精确的、新鲜的，像摊开在长椅上的一本野外图鉴。它不是金色点缀的黑色奢华，也不是质朴的牛皮纸页面。

## Tokens

```css
:root {
  --color-paper: oklch(24% 0.052 158); --color-paper-2: oklch(19.5% 0.045 158); --color-paper-3: oklch(29.5% 0.05 158);
  --color-ink: oklch(93% 0.022 88); --color-ink-2: oklch(81% 0.035 150); --color-muted: oklch(69% 0.045 150);
  --color-rule: oklch(35% 0.05 158);
  --color-accent: oklch(87% 0.19 118); --color-accent-2: oklch(92% 0.13 118); --color-accent-deep: oklch(46% 0.12 128); --color-accent-ink: oklch(22% 0.05 158); --color-focus: oklch(92% 0.13 118);
  --font-display: "Prata", Georgia, serif; --font-body: "Manrope", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "IBM Plex Mono", ui-monospace, monospace;
  --radius-card: 0; --radius-pill: 999px; --rule-hair: 1px;
  --shadow-card: none;
  --tracking-display: -0.005em; --display-weight: 400;
}
```

只有一个旋钮：配色方案（colourway），写进 stamp（`hedgerow: hedge`）。`--color-accent-deep` 是信号色的苔藓强度：在黄绿色会消失的奶油色带上，由它顶替黄绿色。

| 配色方案 | 底色 | 墨色 | 强调色 |
| --- | --- | --- | --- |
| `hedge`（默认） | oklch(24% 0.052 158) | 奶油色 oklch(93% 0.022 88) | 黄绿色 oklch(87% 0.19 118) |
| `sloe` | 李子紫 oklch(25% 0.06 320) | oklch(94% 0.02 80) | 麦秆黄 oklch(88% 0.15 95) |

## 字体

- **展示字体：**Prata 400（它唯一的字重），`font-synthesis: none`；行高 1.08，句首大写（sentence case），正体。条目标题也用 Prata，绝不小于 22px，再小其细线就发虚。宣言级数字用 Prata、等高数字（lining）。
- **正文：**Manrope 400、17px、行高 1.6，用 `--color-ink-2`；标签用 500，700 只出现在控件上。
- **标签、题注、表头：**Manrope 500 小一档，句首大写，不加字距，用 `--color-muted`。植物的拉丁名以这种样式放在俗名旁，正体。IBM Plex Mono 只出现在代码里。

## 表面

- 1px 线条：行之间用 `--color-rule`，两个区块分开处用 `--color-muted`，最重要的那一个列表顶部用 1.5px 黄绿线。
- 方形且平面：well、照片和输入框圆角为 0；无阴影、无模糊、无渐变，照片的压暗层（scrim）除外。纵深靠纸张一档：well 用 `--color-paper-3`，色带用 `--color-paper-2`。
- 色带：一条 `--color-paper-2` 色带，外加一条奶油色带（`--color-ink` 底、`--color-paper` 文字、苔藓色线条、树篱绿控件）用于最致密的区块。每页至多两条。
- 照片：像采药人看到的那样拍植物，凑近、低照度：荫蔽处一臂之遥的一株植物、小径旁的树篱、晨光初照的土地、蒸馏器、暗长椅上的一只杯子。方形，加 8% 的 1px 奶油色圈，色彩保持真实，绝不调成绿色调。画框下方用题注写出植物名；照片上压文字只允许在 45% 到 70% 的树篱绿压暗层上。
- 线条只用于图表或真实地点的地图，1.2px 黄绿描边，不填充。不用纹理。

## Range

- **Index 做成野外图鉴：**Rows 里俗名用 Prata、`--text-2xl` 或更大，拉丁名用标签样式，然后一行字，都在黄绿线之下；植物能撑起一个没有图片的区块。
- **Figures 做成瓶身标签：**批次、数量、价格、距离用 Prata、`--text-display-s` 起步，`--color-rule` 竖线分隔，放在 `--color-paper-2` 色带上；其中一个数字用黄绿色。
- **Statement 用奶油色：**绿色底上一句 display 字号的 Prata 句子；或奶油色带上放一个能用的控件（数量及其累计总额，用 Prata），配苔藓色线条。
- **Table 做成蒸馏日志：**批次、灌装日期、数量与价格排成划线的行，数字等宽，当前行的线条用黄绿色。

## 控件

- 按钮对：黄绿胶囊、Manrope 700、`--color-accent-ink` 文字，旁边一枚 1.5px 黄绿描边胶囊。主按钮 hover 时变亮为 `--color-accent-2`。在奶油色带上，两者都变成树篱绿。
- 链接用奶油色、1px 黄绿下划线；输入框为方形，`--color-paper-2` 底上加 1px `--color-muted` 边框，焦点圈用 `--color-focus`。

## 动效

静止。只有状态变化，`--dur-short` 时长、`--ease-out` 缓动：主按钮变亮、下划线变粗、某行的线条转黄绿。不生长、不漂移、无滚动显现。

## 语气

野外图鉴的语气：植物与它长在哪里，然后是距离与时间，且只写 prompt 确知的；绝不编造距离或月份。产地写成一句话，绝不做徽章。

## 禁止事项

- 绝不引入第二个强调色；售罄用 muted 表达，不用红色。
- 绝不用黑色或蓝黑底色；深色是叶绿，`sloe` 下是李子紫。
- 绝不用明亮高调的照片：白底上的浆果或阳光下的草地，会在绿色里读成一个洞。
- 正文绝不用黄绿色，绝不做黄绿色带，黄绿绝不上奶油色。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Prata&family=Manrope:wght@400;500;700&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: 400; line-height: 1.08; font-synthesis: none; }
.btn { border: 1.5px solid var(--color-accent); border-radius: var(--radius-pill); padding: var(--space-sm) var(--space-lg); font-size: var(--text-sm); font-weight: 700; transition: background-color var(--dur-short) var(--ease-out); }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.btn--primary:hover { background: var(--color-accent-2); border-color: var(--color-accent-2); }
.btn--secondary { background: transparent; color: var(--color-accent); }
.band--cream { background: var(--color-ink); color: var(--color-paper); --color-rule: color-mix(in oklab, var(--color-paper) 22%, var(--color-ink)); }
.band--cream .btn { border-color: var(--color-paper); color: var(--color-paper); }
.band--cream .btn--primary { background: var(--color-paper); color: var(--color-ink); }
.band--cream .figure { color: var(--color-accent-deep); }
.index { border-top: 1.5px solid var(--color-accent); }
.index > li { border-bottom: var(--rule-hair) solid var(--color-rule); }
.photo img { outline: var(--rule-hair) solid color-mix(in oklab, var(--color-ink) 8%, transparent); outline-offset: -1px; }
.figure { font-family: var(--font-display); font-variant-numeric: lining-nums tabular-nums; }
a { text-decoration-color: var(--color-accent); }
```
