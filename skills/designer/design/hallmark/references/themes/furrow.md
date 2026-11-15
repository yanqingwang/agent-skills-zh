---
name: Furrow
slug: furrow
genre: modern-minimal
paper: light 96 85
display: grotesk-sans Red Hat Display
accent: warm 40
posture: committed
keywords: farm, agriculture, land, field, livestock, sheep, cattle, crop, records, compliance, inspection, fleet, field service, rural, contractor, hectares, yard, outdoors, seasonal, working, units
material: warm manila paper, near-black ink in rules, a generated survey map in sienna contours and slate water, Red Hat Display 600 over Red Hat Text with Red Hat Mono figures, moulded 6px keys, a waterproof notebook card, one tangerine signal and a grass green for what is in date
photo: natural con=8 sat=-6
pictured: Field Record, Map hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/furrow.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Furrow

画在土地本身上的耕作记录之声：暖调牛皮纸、近黑墨色，工作发生的地方生成为一张测绘图（等高线、灌木篱、石墙、水，地块边缘描着像地籍图一样的橘色界线），记录钉在它们发生的位置。条目以防水笔记本页面展开；其余是划线列表、带单位的数字与模压按键。橘色是耳标与打捆绳；绿色是仍在有效期内的。它不是田园生活方式页，不是光鲜仪表盘，也不是车载导航。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(96% 0.011 85); --color-paper-2: oklch(99.5% 0.005 85); --color-paper-3: oklch(92% 0.016 85);
  --color-ink: oklch(18% 0.006 60); --color-ink-2: oklch(28% 0.008 60); --color-muted: oklch(44% 0.012 60); --color-rule: oklch(88% 0.013 85);
  --color-accent: oklch(70% 0.19 40); --color-accent-ink: oklch(18% 0.006 60); --color-accent-soft: oklch(91% 0.05 50); --color-focus: oklch(60% 0.19 40);
  --color-green: oklch(48% 0.11 150); --color-green-soft: oklch(92% 0.04 150);
  --color-contour: oklch(62% 0.07 58); --color-water: oklch(60% 0.05 232); --color-hedge: oklch(50% 0.1 150);
  --color-grid: oklch(90% 0.014 85); --color-grid-strong: oklch(85% 0.018 85); --color-sheet: oklch(99.3% 0.004 85);
  --font-display: "Red Hat Display", "Red Hat Text", ui-sans-serif, sans-serif; --font-body: "Red Hat Text", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "Red Hat Mono", ui-monospace, monospace;
  --radius-card: 10px; --radius-entry: 14px; --radius-pill: 6px; --rule-hair: 1px;
  --shadow-card: 0 1px 2px oklch(18% 0.006 60 / 0.08), 0 14px 28px -16px oklch(18% 0.006 60 / 0.28);
  --shadow-lift: 0 1px 1px oklch(18% 0.006 60 / 0.1), 0 2px 4px -1px oklch(18% 0.006 60 / 0.1), 0 24px 44px -20px oklch(18% 0.006 60 / 0.42);
  --tracking-display: -0.035em; --display-weight: 600;
}
```

## 字体（Type）

- **展示字体：**Red Hat Display 600，`--tracking-display`，行高 1.0，句首大写；作为报价的价格用它排展示字号；条目的钟点用它排 44px，表格数字。
- **正文：**Red Hat Text 400，行高 1.55，用 `--color-muted`；行的标题用 500。
- **标签、chips、标签页：**Red Hat Text 500 小一档，句首大写，不加字距。绝不用等宽，绝不用大写。
- **数字（等宽即材料）：**Red Hat Mono 400 与 500，表格数字，比旁边文字小一档，只给要誊到表格上的东西：日期、钟点、耳标号、剂量、批次、公顷。地图上的地名用 Red Hat Text 500，句首大写，沿田块排布，像测绘员那样。

## 表面（Surfaces）

- 测绘图在加载与缩放时生成于画布上，绝不是图片：等高线用 marching squares 从噪声描出、`--color-contour` 色，每五条加重并标注；灌木篱用 `--color-hedge` 点线，石墙实线墨色，水用 `--color-water`，建筑画阴影线，一条小路与一道门；地块边缘描橘色。纸面颗粒、纤维与两道折痕只画进地图里。它的静帧是无脚本时的降级。
- 图上：三种形状的图钉（圆片、菱形、三角）区分记录种类，每枚旁一枚墨色小牌写它的钟点；打开的那枚转橘色；一次移动画成虚线路线。一枚地图放大镜（1.9x，细环，十字线）停在一处地标上，滑向指针。
- 笔记本卡：`--color-paper-2`、`--radius-entry` 圆角，1px 墨色圆环与 `--shadow-lift`，墨色标题写种类与钟点，之后是 8px `--color-grid` 笔记本网格上的格子、以 1px 墨线分隔，脚底 56px 步进键。
- 导出的记录是一张三折信纸摊平：`--color-sheet`，3px 圆角，两道折痕从上方受光。
- 横线：列表之上 1px 墨线，行间 `--color-rule` 发丝线，合计之上 2px 墨线。只有卡与白纸抬起。
- 照片：平常天气里中距的这块地；自然，绝不是黄金时刻；10px 圆角，或墨色暗化层下通栏。

## 版式（Range）

- **地图上的一天：**条目钉在它们发生的位置，其中一条打开为笔记本卡。
- **台账化作索引：**白纸上的划线表格，上方日志的分段过滤器，chips 标注在有效期内与停药期中。
- **一天按钟点：**日志对钟点排成行，每条是一个带小牌的图钉。
- **土地上的账单：**价格作为划线写在橘色色场上，一片等高线残片、一道篱、一扇门与一枚图钉垫在后面。

## 控件（Controls）

- 模压按键 6px 圆角、48px 高：主按钮橘色配墨色文字，顶部一圈受光内嵌边、底部一圈阴影内嵌边；次按钮白色，1px `--color-rule` 边框与同款受光边。按下下沉 1px。
- 字段把标签收在框内，左上小字压淡，其下是值；白色，52px，1px `--color-muted` 边框；数字字段用等宽排。
- 橘色是压着墨色的填色：主按钮、选中的标签页、打开的图钉、地块界线、色场色带、焦点环。

## 动效（Motion）

一次，在视野内：图钉按时间顺序落下，路线画出，卡片打开，放大镜落定。只用变换与透明度，`--ease-out`，屏幕外暂停。Reduced motion（减少动效）或无脚本：图钉已落，一条条目打开。

## 语气（Voice）

平实、带单位：3.6 ha、10 ml、28 天，价格带镑号。绝没有不带单位的数字，绝不用田园形容词。

## 禁止事项（Do-nots）

- 绝不用橘色做文字；它是压着墨色的填色。
- 绝不用地图瓦片、卫星照片或落钉图标；土地是生成的测绘图。
- 颗粒与折痕绝不走出地图。
- 绝不在标签、chip 或标题上用等宽。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@600&family=Red+Hat+Text:wght@400;500&family=Red+Hat+Mono:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: var(--display-weight); line-height: 1; }
.btn { min-height: 48px; border: var(--rule-hair) solid var(--color-rule); border-radius: var(--radius-pill); padding: 0 var(--space-lg); font-weight: 500; background: var(--color-paper-2); color: var(--color-ink); box-shadow: inset 0 1px 0 var(--color-sheet), 0 1px 1px var(--color-rule); }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); border-color: color-mix(in oklab, var(--color-accent) 78%, var(--color-ink)); box-shadow: inset 0 1px 0 color-mix(in oklab, var(--color-sheet) 32%, transparent), inset 0 -1px 0 color-mix(in oklab, var(--color-ink) 10%, transparent); }
.btn:active { transform: translateY(1px); }
.ruled { border-top: var(--rule-hair) solid var(--color-ink); } .ruled > * { border-bottom: var(--rule-hair) solid var(--color-rule); }
.entry { border-radius: var(--radius-entry); background: var(--color-paper-2); box-shadow: 0 0 0 1px var(--color-ink), var(--shadow-lift); overflow: hidden; }
.notebook { background: linear-gradient(var(--color-grid) 1px, transparent 1px) 0 0 / 8px 8px, linear-gradient(90deg, var(--color-grid) 1px, transparent 1px) 0 0 / 8px 8px, var(--color-paper-2); }
.field label { position: absolute; left: var(--space-md); top: var(--space-xs); font-size: 0.75rem; font-weight: 500; color: var(--color-muted); }
.num { font-family: var(--font-outlier); font-variant-numeric: tabular-nums; }
```
