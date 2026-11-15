---
name: Piste
slug: piste
genre: playful
paper: light 98.5 260
display: display-condensed Barlow Condensed
accent: cool 265
posture: committed
keywords: ski, mountain, resort, snow, winter, outdoor, sport, trail, lift, race, alpine, tickets, season pass, conditions, weather, club, active, bold
material: snow-white paper, cold near-black ink, Barlow Condensed 800 caps over Barlow, square edges on 2px ink rules, one cobalt for signal and field
photo: natural con=10 vib=15
pictured: Morning Report, Poster hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/piste.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Piste

印在纸上的山间清晨：雪白纸面、冷调近黑墨色，每个标题与数字都用 Barlow Condensed 800 大写，2px 墨线收出方正边缘，一个钴蓝承担所有颜色工作，从主控件到整面色场。照片把山带进来，清晰、全彩、方正裁切，纸面就是它们展开其上的雪原。它显得大胆，因为字大声、颜色只有一种冷蓝；它不是带镜头光晕的度假区手册，不是运动感渐变，也不是圆润的应用。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(98.5% 0.005 260); --color-paper-2: oklch(95.5% 0.008 260); --color-paper-3: oklch(91% 0.01 260);
  --color-ink: oklch(16% 0.012 260); --color-ink-2: oklch(30% 0.014 260); --color-muted: oklch(48% 0.016 260);
  --color-rule: oklch(88% 0.01 260);
  --color-accent: oklch(52% 0.25 265); --color-accent-deep: oklch(40% 0.2 266); --color-accent-ink: oklch(98.5% 0.004 260); --color-focus: oklch(58% 0.22 28);
  --color-field: var(--color-accent);
  --font-display: "Barlow Condensed", ui-sans-serif, sans-serif; --font-body: "Barlow", ui-sans-serif, sans-serif; --font-outlier: var(--font-display);
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --rule-bar: 2px;
  --shadow-card: none;
  --tracking-display: -0.005em; --display-weight: 800;
}
```

committed（全力以赴）：钴蓝即 `--color-field`，可以灌满一条色带；在控件与链接上它是信号色，`--color-accent-deep` 是它的悬停与按压阶。三种地面，写入 stamp（印记）：`piste: snow` 为 `snow`（上面的代码块）、`blue-run`（页面即钴蓝色场、覆白墨；白色承担控件与焦点）与 `night-piste`（`oklch(14% 0.01 260)` 之上覆白墨，2px 白线，钴蓝 56%，焦点红 60%）。

## 字体（Type）

- **展示字体：**Barlow Condensed 800，全大写，正体，`--tracking-display`；任何可能换行的标题行高 1.0，不能换行的单行才用 0.9。窄体，所以比共享字阶大一级排：章节标题从 `--text-display-s` 起，Hero 标题到 8rem。
- **数字：**展示字面 800，表格数字，从 `--text-display` 到两倍；纸上的数字用钴蓝，色场上的数字用纸色。下方标签用 Barlow 500。
- **正文：**Barlow 400 与 500，17 至 19px，行高 1.5；要在户外读，绝不变浅。
- **按钮：**Barlow Condensed 800 大写，18px，不加字距（大写展示之下 67 条允许）。导航链接、表头、图注：Barlow 500 小一档，句首大写。

## 表面（Surfaces）

- 横线：`--rule-bar` 墨线压在列表、数字行或表头之上，以及浮动条之下；行间用 `--color-rule` 的 `--rule-hair`。划线，绝不装框。
- 一切圆角 0：凹槽、照片、输入框、控件与标签都方正裁切。深度是平的：抬起的表面是一档纸面或钴蓝色场，绝不靠阴影。
- 色带：`--color-accent-ink` 文字的钴蓝色场，或表单与密表之下的 `--color-paper-2`；每页至多两条。
- 照片：日光与全彩下的山：背影中的一群人坡上同行、教练身后排队的孩子、立在新雪里的雪板、衬着天空的缆车；清晰高调，绝不用黄昏调或光晕。方正裁切，8% 内嵌墨色发丝线。墨色直接压在亮雪上；纸色只许压在天空上，且必须隔着冷调墨色暗化层。
- 无纹理，除暗化层外无渐变，无模糊。

## 版式（Range）

- **数字行化作吊椅告示板：**提示词的数字用窄体字面排到两倍 `--text-display`，雪上钴蓝，压在 `--rule-bar` 墨线之下、发丝线分隔，各配一行 Barlow。
- **色场上的宣言：**一行短句用窄体大写排展示字号及以上，纸色钴蓝铺满边到边，那是晨报会喊出来的话。
- **步骤或时刻表：**`<ol>` 的每个数字用窄体字面排 `--text-display`、钴蓝压在 2px 墨线之上，配大写标题与一行文字；或一张划线表格，时间与队伍分组，表头横线用墨色。
- **表单化作售票窗口：**方正 52px 输入框与墨色步进器压在 paper-2 上，钴蓝主按钮是色带上唯一的颜色。

## 控件（Controls）

- 一对：钴蓝填充配 `--color-accent-ink` 文字，旁边是 2px 内嵌墨色描边，两者方正，用窄体大写；在暗化层或色场上描边转纸色。悬停取 `--color-accent-deep`；按下取墨色。
- 链接用墨色带下划线，悬停转钴蓝；输入框方正，52px，1px 墨色边框；步进器是两个方正墨边按钮夹着一个表格数字。
- 钴蓝落在主按钮、链接悬停、色场色带与数字上；红色是焦点环，此外什么都不是。

## 动效（Motion）

静止。控件悬停时深一档，时长 `--dur-micro`、缓动 `--ease-out`；无描画、无循环、不跟随滚动。

## 语气（Voice）

晨报：钟点、队伍、预订的那一周，隔着雪地喊过来。绝不说关于自由或粉雪的口号。

## 禁止事项（Do-nots）

- 绝不用小写展示字体或细的窄体；Barlow Condensed 就是 800。
- 绝不用圆角、胶囊或软卡片。
- 绝不用第二种强调色相，绝不把钴蓝压在正文上、或作为雪白纸上的卡片填色。
- 绝不用天空渐变、日落调，也绝不画山、雪花或雪道图。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@800&family=Barlow:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: 800; text-transform: uppercase; line-height: 1; }
h2 { font-size: var(--text-display-s); }
.fig { font: 800 var(--text-display)/0.9 var(--font-display); color: var(--color-accent); font-variant-numeric: tabular-nums; }
.btn { display: inline-flex; align-items: center; min-height: 52px; padding: 0 var(--space-lg); border: 0; font: 800 var(--text-lg)/1 var(--font-display); text-transform: uppercase; }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.btn--primary:hover { background: var(--color-accent-deep); }
.btn--secondary { background: none; box-shadow: inset 0 0 0 var(--rule-bar) var(--color-ink); color: var(--color-ink); }
.band--field { background: var(--color-field); color: var(--color-accent-ink); }
.photo { outline: 1px solid color-mix(in oklab, var(--color-ink) 8%, transparent); outline-offset: -1px; }
th { border-bottom: var(--rule-bar) solid var(--color-ink); font: 500 var(--text-sm) var(--font-body); text-align: left; }
td { border-bottom: var(--rule-hair) solid var(--color-rule); }
::selection { background: color-mix(in oklab, var(--color-accent) 30%, transparent); }
```
