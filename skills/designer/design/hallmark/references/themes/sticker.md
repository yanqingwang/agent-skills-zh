---
name: Sticker
slug: sticker
genre: playful
paper: light 95.7 82
display: display-heavy Bowlby One SC
accent: chromatic-magenta 2
posture: full-palette
keywords: stickers, print, merch, shop, maker, creator, diy, craft, vinyl, packaging, labels, small business, ecommerce, fun, loud, pink, cut, ship, order
material: warm off-white paper, warm black ink, Bowlby One SC over Sofia Sans, white die-cut borders on hard offset shadows, hot pink, lime and ink fills set with type
photo: natural vib=15 con=5
pictured: Bento Grid, Stage hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/sticker.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Sticker

印刷店的物料：暖调米白纸、暖调黑墨，Bowlby One SC 大写压在 Sofia Sans 之上，热粉与青柠色填充，每一块凸起的表面都以厚白模切边收口、压在硬偏移阴影上。它响亮而手工感十足，因为深度是印出来的，颜色都是实色填充，绝不做淡色调。它不是阴影柔和的粉彩小店，也不是卡通玩具页。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(95.7% 0.013 82); --color-paper-2: oklch(92.8% 0.021 79); --color-paper-3: oklch(99.4% 0.007 89);
  --color-ink: oklch(21% 0.011 81); --color-ink-2: oklch(30% 0.013 78); --color-muted: oklch(50% 0.017 64);
  --color-rule: oklch(89.7% 0.02 80); --color-white: oklch(99.5% 0.003 82);
  --color-accent: oklch(56% 0.225 2); --color-accent-deep: oklch(49% 0.205 2); --color-accent-2: oklch(87.6% 0.179 119); --color-slot: oklch(95% 0.021 355);
  --color-accent-ink: oklch(99.5% 0.003 82); --color-focus: oklch(56% 0.225 2);
  --font-display: "Bowlby One SC", "Arial Black", sans-serif; --font-body: "Sofia Sans", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "Sofia Sans", ui-sans-serif, system-ui, sans-serif;
  --radius-card: 18px; --radius-pill: 999px; --rule-hair: 1px; --rule-bar: 2px;
  --shadow-card: 5px 6px 0 var(--color-ink); --shadow-press: 1px 1px 0 var(--color-ink);
  --tracking-display: 0.005em; --display-weight: 400;
}
```

两种配色，写入 stamp（印记）：`sticker: sheet`。

| 配色 | 纸、墨、填充 |
| --- | --- |
| `sheet`（默认） | 上面的代码块 |
| `vinyl` | 底 `oklch(21% 0.011 81)`，卡片 `oklch(25.5% 0.013 72)`，墨 `oklch(95.7% 0.013 82)`，横线 `oklch(33% 0.016 75)`；粉与青柠不变，白边保持白色 |

## 字体（Type）

- **展示字体：**Bowlby One SC 400，设计上只有大写，`--tracking-display`，行高 1.02。它宽而重，所以 `h1` 封顶 4.5rem，区块标题 3.25rem。绝不用它排段落。
- **数字：**价格、计数与步骤编号用 Bowlby，填充面上的孤立大数字可放到 12rem；它是主题最响的东西，所以每屏只允许一个。
- **正文：**Sofia Sans 400 与 600，行高 1.5，`tabular-nums`。
- **标签、标记、图注、表头：**Sofia Sans 700，小一号，句首大写，不加字距，用 `--color-muted`。没有第三种字体：outlier token 也是 Sofia Sans。

## 表面（Surfaces）

- 模切：凸起的表面（卡片、承载事实的填充块、标记、照片、主控件）带 6px `--color-white` 边框与 `--shadow-card`，即无模糊的硬偏移阴影。本身就是纸面的表面（表格、色带）保持无边框，由虚线分隔。
- 凸起表面可在 -6 到 6 度之间倾斜，绝不全部倒向一边；表格与输入框保持端正。
- 圆角：卡片用 `--radius-card`，照片 22px，控件与标记用胶囊；`--rule-bar` 粗细的 `--color-rule` 虚线用作分隔线与投放区边缘。
- 色带：`--color-paper-2` 色带、墨色色带配纸色文字，或一块青柠色场配墨色文字；每页至多两条。
- 照片：产品在使用中或被举到镜头前，近拍，颜色保持浓烈；白色模切边内 22px 圆角，每屏一张，倾斜不超过 3 度。标记可以压住一角并带一个事实；文字绝不压在照片上。
- 无纹理，文字背后无渐变：深度只靠硬偏移阴影。

## 版式（Range）

- **事实作模切填充：**一个 Bento 网格，其瓦片是粉、青柠、墨与白的填充块，每块承载一个事实，Bowlby 大字配一行 Sofia，白边压在硬阴影上，交替方向倾斜一两度；头块承载那个孤立大数字。
- **步骤作贴住的卡片：**三四个 `<ol>` 卡片排成一行，数字用 Bowlby 放在青柠圆片上，卡片彼此反向倾斜，压住它们下方那条虚线。
- **青柠色场上的可用控件：**步进器、Bowlby 的累计金额，以及一条朝提示词给出的门槛填充的进度条，放在白色模切卡片上，旁边是虚线价格阶梯。
- **墨色色带上用 Bowlby 排陈述**，横跨十列，一枚粉或青柠标记斜贴在一角，写着它所主张的事实。

## 控件（Controls）

- 控件对：粉色胶囊带 5px 白环与 `--shadow-card`，旁边是幽灵胶囊，带 inset 2px 墨色边框。chip 是带 2px 内嵌线的胶囊，选中者墨色填充。
- 链接用墨色，悬停出现粉色下划线；输入框用 2px 墨色边缘，圆角 `--radius-card`。
- 颜色三等分工：粉给起动作的填充（主按钮、价格），青柠给起标记作用的填充（标记、计数、高亮），墨给文字。

## 动效（Motion）

贴纸物理：悬停把可点击的凸起表面抬起 2px 并转一度；按下则把它压进阴影里。`--ease-out` 配 `--dur-micro`，滚动无动效。

## 语气（Voice）

快活而精确：价格、数量、尺寸、发货日。听起来像模切机旁那个人。

## 禁止事项（Do-nots）

- 凸起表面下绝不用柔和模糊投影；要么硬偏移阴影，要么没有阴影。
- 模切边绝不薄于 4px，也绝不用白色以外的颜色。
- 纸面上绝不用粉色文字；粉是填充色，上面压白字。
- 绝不手绘贴纸、吉祥物或涂鸦；模切收口的是真实表面、事实或照片，绝不是代替设计的图形。
- 绝不用只在主体旁边摆拍的照片（一瓶东西、一台订书机、一个笔筒）；没有产品自己的照片时，靠填充块撑起页面。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Bowlby+One+SC&family=Sofia+Sans:wght@400;600;700&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: 400; letter-spacing: var(--tracking-display); line-height: 1.02; }
h1 { font-size: min(var(--text-display), 4.5rem); } h2 { font-size: min(var(--text-section), 3.25rem); }
.diecut { border: 6px solid var(--color-white); border-radius: var(--radius-card); box-shadow: var(--shadow-card); }
.diecut--photo { border-radius: 22px; overflow: hidden; background: var(--color-slot); }
.btn { display: inline-flex; align-items: center; height: 52px; padding: 0 var(--space-lg); border-radius: var(--radius-pill); font-weight: 700; font-size: var(--text-md); color: var(--color-ink); box-shadow: inset 0 0 0 2px var(--color-ink); }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); box-shadow: 0 0 0 5px var(--color-white), 5px 6px 0 var(--color-ink); transition: translate var(--dur-micro) var(--ease-out), box-shadow var(--dur-micro) var(--ease-out); }
.btn--primary:hover { background: var(--color-accent-deep); }
.btn--primary:active { translate: 4px 5px; box-shadow: 0 0 0 5px var(--color-white), var(--shadow-press); }
.fill { border: 6px solid var(--color-white); border-radius: var(--radius-card); box-shadow: var(--shadow-card); background: var(--color-accent); color: var(--color-accent-ink); }
.rule { border-top: var(--rule-bar) dashed var(--color-rule); }
::selection { background: var(--color-accent-2); color: var(--color-ink); }
```
