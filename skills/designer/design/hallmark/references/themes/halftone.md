---
name: Halftone
slug: halftone
genre: playful
paper: light 96.2 94
display: slab-serif Ultra
accent: warm 33
posture: committed
keywords: drinks, soda, food brand, print shop, zine, magazine, record label, packaging, campaign, label, bottle, can, screen print, bold, one colour, retail, craft, loud, fruit, snack
material: butter-cream stock, brown-black ink, Ultra over Chivo, three-pixel ink rules and square wells, one vermilion printed solid and through a dot screen, photographs in full colour
photo: natural vib=25 sat=10 con=6
pictured: Back of the Can, Settled hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/halftone.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Halftone

响亮的单色印刷口吻：奶油黄纸、棕黑墨色，肥厚的 Ultra 粗衬线作标题，Chivo 负责其余一切，3px 墨色横线，外加一处朱红：在控件上实地印刷，在色带或内嵌面板上则过网点。照片是唯一的全彩，近拍且明亮，像包装标签上的产品照。它有丝网印刷感，因为墨只有一种、网点从实到无渐隐，而不是因为画了什么。它不是漫画波普页，也不是马卡龙色零食品牌。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(96.2% 0.032 94); --color-paper-2: oklch(92.6% 0.046 92); --color-paper-3: oklch(87.5% 0.058 90);
  --color-ink: oklch(23% 0.040 38); --color-ink-2: oklch(33% 0.045 40); --color-muted: oklch(44% 0.048 44);
  --color-rule: oklch(82% 0.042 82);
  --color-accent: oklch(54.5% 0.215 33); --color-accent-deep: oklch(46% 0.19 31); --color-accent-ink: oklch(97% 0.022 94); --color-focus: oklch(46% 0.19 31);
  --color-dot: var(--color-accent); --halftone-size: 12px; --halftone-dot: 3px;
  --font-display: "Ultra", ui-serif, Georgia, serif; --font-body: "Chivo", ui-sans-serif, sans-serif;
  --radius-card: 0; --radius-input: 3px; --radius-pill: 999px; --rule-hair: 1px; --rule-bar: 3px;
  --shadow-card: none;
  --tracking-display: 0.005em; --display-weight: 400;
}
```

Committed 姿态：专色承担网点、控件与一条色场色带。三种纸张，写入 stamp（印记）：`halftone: cream`。

| 纸张 | 纸与墨 | 专色 |
| --- | --- | --- |
| **Cream and vermilion**（默认） | 上面的 token | `oklch(54.5% 0.215 33)` |
| **Lemon on black** | 底 `oklch(19% 0.01 60)`，上覆 `oklch(96% 0.02 90)` | 黄色 `oklch(88% 0.17 95)`，其上压深墨字 |
| **Blood orange** | 颜色进入纸里：底 `oklch(72% 0.17 45)`，上覆紫红 `oklch(24% 0.06 25)` | 紫红墨兼作专色，网点因此印成深色 |

## 字体（Type）

- **展示字体：**Ultra 400，唯一字重，正体，句首大写，行高 1.08（再紧 Ultra 的下降部就会碰到下一行），`--tracking-display`；每个标题一种颜色。Ultra 的数字是它最响的字母：200px 以上的数字可以在专色中实地印刷，字距 -0.02em，独占一行时行高 0.9。
- **正文：**Chivo 400，17px，行高 1.55，用 `--color-ink-2`；控件与标签面板中的名称用 Chivo 700。
- **标签、标记、表头、图注：**Chivo 500，小一号，句首大写，不加字距；3px 横线给它们撑腰。不用等宽字体。

## 表面（Surfaces）

- 横线代替边框工作：区块、表格或列表顶端压墨色 `--rule-bar`，行间用 `--color-rule` 的 `--rule-hair`。
- 内嵌面板是唯一的加框表面：`--color-paper-2` 装在 `--rule-bar` 墨色边框里，直角，内部不再套任何框。任何地方都无阴影。
- 圆角：按钮与输入框 3px，chip 用完整胶囊；内嵌面板、标记与照片都是直角。
- 色带：`--color-paper-2`、专色色场反白米黄字，或墨底米黄字。每页至多两条。`--color-accent-deep` 是压暗的专色：悬停、焦点环，以及一切小于 24px 的专色文字。
- 照片：产品与它的原料，近拍、明亮（切开的柠檬、一块姜、杯中的气泡），硬日光、素净浅底。页面上唯一的全彩；直角，1px 墨色发丝线，下方图注写明拍了什么。专色绝不给照片加色罩。
- 网点（`texture.md` § Halftone）：专色的 `--halftone-dot` 圆点落在 `--halftone-size` 网格上，用蒙版从实到无渐隐，用在色带或内嵌面板上；每个区块只允许一处网点色场，绝不压在文字或照片之下或之上。

## 版式（Range）

- **数字当海报：**一个真实数字（卡路里、容量、价格）用 Ultra 排到 240px 以上，米黄纸上实地专色，单位与它的一句话用墨色 Ultra 排区块标题字号，放在旁边。
- **标签排成面板：**一条 3px 墨线压在全宽行组之上，名称用 Chivo 700，数值用 Ultra 的条目字号，行间发丝线，就像罐身背标那样读；绝不缩进盒子里。
- **专色上下单：**专色色带反白米黄标题，步进器与累计金额用 Ultra，网点从空侧边缘向内渐显。
- **反白陈述：**一句直白话用 Ultra 排展示字号，米黄字从墨底或专色底里镂空出来，色场上除链接外别无他物。

## 控件（Controls）

- 专色填充按钮，Chivo 700，3px 圆角，旁边是无框的 `--rule-bar` 专色下划线。
- 链接用墨色配专色下划线；输入框 3px 圆角，1px 墨色边框。
- 专色只落在控件、网点、色场色带与焦点环上；绝不落在正文上。

## 动效（Motion）

只动状态，`--ease-out` 配 `--dur-short`：按钮加深一档。网点永不移动。

## 语气（Voice）

像标签说话：水果、卡路里、罐的容量、整箱的价钱。直白、甜、具体；绝不谈生活方式。

## 禁止事项（Do-nots）

- 绝无第二种墨色；一处专色包办网点、按钮与色场，米黄纸上的蓝色链接等于换了印刷厂。
- 绝不用非网点的渐变；淡出就是从实到无的网点。
- 网点绝不压在文字或照片之下或之上。
- 绝不用仿粗的 Ultra、柔和阴影或圆角内嵌面板。
- 米黄纸上绝不出现小于区块标题的专色文字；专色印小了会发虚，所以小号专色文字改用加深专色。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Ultra&family=Chivo:wght@400;500;700&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: var(--display-weight); line-height: 1.08; }
.poster { font: 400 clamp(10rem, 22vw, 20rem)/0.9 var(--font-display); letter-spacing: -0.02em; color: var(--color-accent); font-variant-numeric: tabular-nums; }
.btn { padding: var(--space-md) var(--space-lg); border-radius: var(--radius-input); font: 700 var(--text-sm) var(--font-body); background: var(--color-accent); color: var(--color-accent-ink); }
.btn--secondary { background: none; color: var(--color-ink); padding: var(--space-md) 0 var(--space-xs); border-radius: 0; border-bottom: var(--rule-bar) solid var(--color-accent); }
.well { border: var(--rule-bar) solid var(--color-ink); background: var(--color-paper-2); }
.ruled { border-top: var(--rule-bar) solid var(--color-ink); } .ruled > * { border-bottom: var(--rule-hair) solid var(--color-rule); }
.photo { outline: var(--rule-hair) solid var(--color-ink); outline-offset: calc(-1 * var(--rule-hair)); }
.halftone { position: relative; isolation: isolate; }
.halftone::before { content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background: radial-gradient(var(--color-dot) var(--halftone-dot), transparent calc(var(--halftone-dot) + 0.5px)) 0 0 / var(--halftone-size) var(--halftone-size);
  mask: linear-gradient(110deg, transparent 45%, var(--color-ink) 95%); }
::selection { background: color-mix(in oklab, var(--color-accent) 30%, transparent); }
```
