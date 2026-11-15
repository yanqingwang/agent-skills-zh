---
name: Dusk
slug: dusk
genre: modern-minimal
paper: dark 17.5 268
display: grotesk-sans Wix Madefor Display
accent: cool 274
posture: committed
keywords: treasury, banking, fintech, payments, reconciliation, ledger, accounting, close, month end, audit, balance, cash management, payouts, settlement, compliance, controller, bookkeeping, finance team, invoicing, payroll, overnight, automation
material: a real landscape at the turn of the light behind the hero, slate below it, the product in smoked glass with a lit top edge, Wix Madefor Display at a quiet weight over Wix Madefor Text, bone wells for light surfaces, one periwinkle signal and one apricot
photo: natural con=4 vib=6
pictured: Narrative Workflow, Stage hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/dusk.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Dusk

一天将尽时分的资金软件：Hero 背后是一张真实的暮色大地照片，标题以深色压在照片最亮的部分，产品在旁边以烟熏玻璃呈现。往下，页面转入板岩色，浅色表面是骨白色内嵌面板。它读起来贵气而不慌不忙，绝不是霓虹交易屏，也不是方块瓷砖仪表盘。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(17.5% 0.014 268); --color-paper-2: oklch(21% 0.016 268); --color-paper-3: oklch(25% 0.017 268);
  --color-ink: oklch(96% 0.006 75); --color-ink-2: oklch(85% 0.010 262); --color-muted: oklch(70% 0.016 262);
  --color-rule: oklch(30% 0.016 266); --color-light: oklch(100% 0 0); --color-shade: oklch(10% 0.022 268);
  --color-accent: oklch(77% 0.10 274); --color-accent-ink: oklch(19% 0.035 274); --color-accent-hi: oklch(84% 0.085 274);
  --color-accent-deep: oklch(44% 0.13 274); --color-accent-soft: oklch(91% 0.038 274); --color-focus: oklch(80% 0.10 274);
  --color-accent-2: oklch(83% 0.095 62); --color-dusk: oklch(70% 0.12 330);
  --color-day-ink: oklch(22% 0.022 268); --color-day-muted: oklch(38% 0.022 266); --color-fog: oklch(94% 0.012 70);
  --color-well: oklch(95.5% 0.008 75); --color-well-2: oklch(92% 0.010 75); --color-well-ink: oklch(21% 0.016 268); --color-well-muted: oklch(47% 0.016 265); --color-well-rule: oklch(87.5% 0.009 75); --color-card: oklch(99.5% 0.003 75);
  --glass: oklch(22% 0.018 268 / 0.58); --glass-blur: 22px;
  --glass-hi: inset 0 1px 0 oklch(100% 0 0 / 0.10), inset 0 0 0 1px oklch(100% 0 0 / 0.06);
  --shadow-card: 0 1px 0 oklch(100% 0 0 / 0.06) inset, 0 40px 80px -32px oklch(8% 0.02 268 / 0.7);
  --font-display: "Wix Madefor Display", ui-sans-serif, system-ui, sans-serif; --font-body: "Wix Madefor Text", ui-sans-serif, system-ui, sans-serif;
  --radius-card: 18px; --radius-inner: 10px; --radius-pill: 999px; --rule-hair: 1px;
  --tracking-display: -0.022em; --display-weight: 500;
}
```

三个拨盘，各自写入 stamp（印记）：`dusk: fog/periwinkle-apricot/glass`；同一次运行中的两个 Dusk 页面在其中两处不同。

| 拨盘 | 选项 |
| --- | --- |
| **钟点**（Hero 照片） | `fog`（默认）：杏色天空下的雾谷。`shore`：暮色水面，小船或码头。`ridge`：破晓薄雾中的山脊 |
| **信号色**（先成对，后开放） | `periwinkle-apricot`（默认）。`sage-apricot`：以 `oklch(80% 0.07 160)` 作第一信号色 |
| **产品表面** | `glass`（默认）：板岩上的烟熏玻璃。`well`：骨白内嵌面板也承载 Hero 产品，玻璃只出现在照片之上 |

## 字体（Type）

- **展示字体：**Wix Madefor Display 500，`--tracking-display`，行高 1.02 至 1.1，句首大写。标题保持克制；照片与产品才是响亮的部分。
- **正文：**Wix Madefor Text 400 与 500，17px，行高 1.55；导语用 `--color-ink-2` 或 `--color-muted`。
- **数字：**同样的字体，`tabular-nums`；分位（cents）用 `--color-muted`、同字号，绝不上标。排成陈述的数字用 Display 500，34 至 44px，分位取 0.6em。
- **标签、列头、状态：**Text 500，小一号，句首大写，用 `--color-muted`。绝不用等宽字体，绝不用加字距的大写。

## 表面（Surfaces）

- **钟点：**一张暮色转换时分的图库大地照片铺满 Hero，标题用 `--color-day-ink` 压在照片最亮处，文字之下只垫雾面蒙版（`--color-fog` 取 40 至 78%，径向），产品以玻璃质感放在照片较暗一侧，页脚淡出到 `--color-paper`。同一钟点的第二张照片可以在表单背后收尾页面；至多两张。
- **玻璃：**产品表面，`--glass` 加模糊，`--glass-hi` 作受光边缘，`--shadow-card` 投影。内部行以 7% 的 `--color-light` 分隔；内部部件以 4 至 6% 叠在其上，圆角 `--radius-inner`。
- **内嵌面板：**浅色表面是一块 5:4 的骨白内嵌面板，承载一张白色 `--color-card`；图注放在其下，一个标题加一行弱化文字。
- **板岩：**Hero 之下每条色带都是 `--color-paper`；导航一旦离开照片就转为板岩色玻璃。

## 版式（Range）

- **一次运行排成账户列表：**账户带圆形首字母，行数用弱化色，状态词配图标，余额右对齐、分位弱化；待办项以杏色横条收尾列表，带它的操作按钮。
- **导览排成列表加单窗格：**四项任务排成划线列表，选中项以长春花色圆点标记并展开一行，旁边一个玻璃窗格随之切换。
- **一个月排成夜晚条带：**每天一条细圆角条，长春花色，高度即完成的工作量；被标记的日子在其条上方加一颗杏色圆点，打开的一天用杏色，未到的日子画斜线阴影；下方一条划线合计，含四个数字。
- **交接放进内嵌面板：**产品发出的便签或消息，排成骨白底上的那张真实卡片。

## 控件（Controls）

- 一枚长春花色胶囊（`--color-accent` 底、`--color-accent-ink` 字，顶部一条浅色内嵌高光边）；悬停提亮为 `--color-accent-hi`，加柔和长春花色描边环。旁边一枚幽灵胶囊，`--color-light` 取 4%。
- 邮箱输入框与它的按钮合用一个胶囊：照片上为磨砂雾面，板岩上为烟熏玻璃。
- 标签页是带圆点的划线列表，绝不是分格盒。开关开启时为长春花色。
- 两种信号色，两种职责：长春花色表示已完成、已对平、开启与聚焦；杏色表示待办、等待或欠付。两者都不作大面积填充。

## 动效（Motion）

Hero 照片在 48 秒内漂移 6%；产品的行错峰上升一次；打开状态的圆点呼吸；窗格交叉淡切；条带被看到时从底部生长。减弱动效：全部静止。

## 语气（Voice）

平静而精确：跑了什么、何时、还剩什么。

## 禁止事项（Do-nots）

- 绝不用手绘或生成的天空，文字也绝不压在照片繁杂的部分。
- 绝不用渐变按钮、第三种信号色或红色的借记。
- 绝不用统计瓦片网格；数字活在行、列表与那条划线合计里。
- 玻璃绝不叠玻璃，玻璃背后绝无辉光，玻璃绝不能没有受光边缘。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Wix+Madefor+Display:wght@400;500;600&family=Wix+Madefor+Text:wght@400;500;600&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: var(--display-weight); letter-spacing: var(--tracking-display); }
.num { font-variant-numeric: tabular-nums; } .num .c { color: var(--color-muted); }
.glass { background: var(--glass); border-radius: var(--radius-card); -webkit-backdrop-filter: blur(var(--glass-blur)) saturate(1.35); backdrop-filter: blur(var(--glass-blur)) saturate(1.35); box-shadow: var(--glass-hi), var(--shadow-card); }
.btn { min-height: 48px; padding: 0 var(--space-lg); border: 0; border-radius: var(--radius-pill); background: var(--color-accent); color: var(--color-accent-ink); font: 600 0.9375rem/1 var(--font-body); box-shadow: inset 0 1px 0 color-mix(in oklab, var(--color-light) 35%, transparent); }
.btn:hover { background: var(--color-accent-hi); }
.hero__photo { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.hero__scrim { position: absolute; inset: 0; background: radial-gradient(ellipse 50% 58% at 20% 56%, color-mix(in oklab, var(--color-fog) 78%, transparent), transparent 78%), linear-gradient(to bottom, transparent 72%, var(--color-paper)); }
```
