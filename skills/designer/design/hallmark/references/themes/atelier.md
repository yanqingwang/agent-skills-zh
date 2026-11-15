---
name: Atelier
slug: atelier
genre: editorial
paper: light 94.5 76
display: roman-serif Sentient
accent: cool 248
posture: restrained
keywords: fashion, atelier, couture, fragrance, gallery, exhibition, museum, ceramics, furniture, homeware, architecture, design studio, lookbook, collection, craft, small-batch, made by hand, brand story, luxury, object, hotel, boutique hotel, hospitality, stay
material: limewash paper under a slow luminous air, deep umber ink, Sentient light over Hanken Grotesk, cotton card stock with fibre and pressed type, hairlines, matted prints in warm daylight, one cool slate signal
photo: warm con=-6 vib=-10
pictured: Gallery Hang, Diffusion hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/atelier.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Atelier

静止空气里一册匠人目录的语域：石灰水纸面，一层缓慢、发亮的光晕在其后移动，深棕墨色，Sentient light 做标题与陈述，Hanken Grotesk 做阅读文字，发丝线，一个几乎与墨色一样深的石板蓝信号色。这间房子递给你的东西（一条样品、一张卡片、一张编号的版画）都建在棉质卡纸上，从左上打光，带压印文字与纤维。不是细衬线的奶油色奢华页，不是蓝色按钮的商品页。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(94.5% 0.010 76); --color-paper-2: oklch(91.8% 0.013 74); --color-paper-3: oklch(88% 0.015 72);
  --color-ink: oklch(19% 0.024 52); --color-ink-2: oklch(31% 0.018 54); --color-muted: oklch(47% 0.014 60);
  --color-rule: oklch(81% 0.011 70);
  --color-accent: oklch(41% 0.075 248); --color-accent-ink: oklch(96% 0.008 76); --color-focus: oklch(50% 0.095 248);
  --color-card: oklch(97.6% 0.007 82); --color-card-edge: oklch(86% 0.012 72); --color-pencil: oklch(52% 0.010 62);
  --card-lit: oklch(98.4% 0.006 84); --card-shade: oklch(96.4% 0.008 78); --lit: oklch(99.6% 0.004 85 / 0.9);
  --stain-1: oklch(70% 0.075 14); --stain-2: oklch(66% 0.055 132); --stain-3: oklch(60% 0.080 58); --stain-4: oklch(68% 0.045 206);
  --font-display: "Sentient", Georgia, serif; --font-body: "Hanken Grotesk", system-ui, sans-serif;
  --font-outlier: var(--font-body);
  --radius-card: 0; --radius-pill: 3px; --rule-hair: 1px; --rule-head: 1px;
  --shadow-card: 0 0 0 1px oklch(30% 0.03 55 / 0.05), 0.5px 1px 1px oklch(30% 0.03 55 / 0.08), 3px 8px 14px -6px oklch(30% 0.03 55 / 0.14), 14px 36px 64px -28px oklch(30% 0.03 55 / 0.3);
  --tracking-display: -0.018em; --tracking-statement: -0.022em; --display-weight: 300; --statement-weight: 300; --serif-small: 400;
}
```

## 字体（Type）

- **展示与陈述：**每个标题、以及 `--text-display-s` 及以上的一句话或一个数字，用 Sentient 300，行高 1.02 至 1.1，句首大写，正体。一个标题一个字重、一种颜色。
- **小衬线：**`h3`、卡上的名字、一个日期、一条目的编号用 Sentient 400；绝不小于 16px，绝不做段落。
- **正文：**Hanken Grotesk 400，行高 1.6，用 `--color-ink-2`。每页三个字重：Sentient 300 与 400，Hanken 400。
- **标签：**墙面标签：Hanken 400 小一档，句首大写，不加字距；物件名用墨色，材质或编号用 `--color-muted`。编号版次用铅笔字：留一条空白横线给手写，之后是印数，用 `--color-pencil`。

## 表面（Surfaces）

- 空气：页面之后一层固定的 WebGL 场，域扭曲噪声以奶油与淡琥珀色的薄纱向上漂移，以 linear light 混合，半尺寸渲染；指针最近的路径会拨开它，选中的物体会给它染色。它透过 Hero 与一两个区域显露；纸面章节盖住它。同一场景的静帧是降级方案。绝不是渐变色块，绝不是照片。
- 纹理生成为 feTurbulence data URI：`--grain`（180px，1.15）以 0.16 multiply 铺在空气上，`--fibre`（220px，0.85）铺在所有棉质卡纸上。
- 卡纸：`--color-card` 的棉白，2px 圆角，`--shadow-card`，左上一圈内嵌受光边缘，内缩 14px 的发丝线内框用 `--color-card-edge`；上面的文字是压印的（下方一条 1px 受光文字阴影）。
- 样品条：窄长的棉质吸墨纸，尖端收尖，物品的染渍从尖端向上洇开，名字小小地竖排。它们从标题旁的一颗铆钉展开成扇形，作为标签挂在横杆上（选中的那根沿细线放下），或塞在卡片后面。
- 行间发丝线；表格或列表以墨色 `--rule-head` 线起头。照片：暖调日光下的静物与房间，端正悬挂并配墙面标签；主图是一张版画，压在细棉卡纸上，边缘细斜切，版号铅笔字在下方。

## 版式（Range）

- **陈述：**提示词的一句话用 Sentient 300 横跨九或十列，铅笔版次行与一段展墙文字以石板蓝首字下沉开头。
- **选择化作样品条：**系列做成横杆上的吸墨纸，每条都是真的标签页；选中的放下，其照片与墙面标签在旁。
- **时刻表：**日期或钟点排成墨线之下的划线表格，名字用 Sentient 400，关闭的行压淡，绝不划线删除。
- **预订化作卡片：**表单做成棉纸上的凸版卡：房子名压印，带圆环的日期选择器（选中日期周围一圈盲压印），雕刻感的时间 chip，可书写的划线，样品条塞在卡后。

## 控件（Controls）

- 一个发丝线描边、墨色的控件，3px 圆角（悬停填墨、纸色文字），旁边是带石板蓝下划线的链接。没有颜色填充的控件。
- 卡纸上的选择是压进去的：左上内嵌阴影，下方受光边缘；选中的套 1px 墨色圆环。卡上的字段是划线之上的标签。
- 石板蓝不超过一块屏幕的 4%：下划线、首字下沉、焦点环。

## 动效（Motion）

字体就绪后淡入；样品条以 `--ease-out`、`--dur-long` 展开一次；空气漂移、拨开、染色，屏幕外暂停。Reduced motion（减少动效）与无脚本时：静止的空气，第一件物品已选中。

## 语气（Voice）

手工排版、对物精确：物件、材质、做的数量、开门的日子。不用最高级，绝不说"立即选购"或"探索发现"。

## 禁止事项（Do-nots）

- 绝不用暖色强调；信号色是彩度 0.09 以下的冷石板蓝。
- 绝不用加粗或高对比标题；Sentient light 承担语气。
- 绝不用衬线做行文。
- 绝不用纯白平卡或磨砂玻璃面板；卡纸有纤维、受光边缘与来自左上的一盏光。
- 绝不让两幅同尺寸的静物并排。

## 构建提示（Build hint）

```html
<link href="https://api.fontshare.com/v2/css?f[]=sentient@300,400&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400&display=swap" rel="stylesheet">
```

```css
body { color: var(--color-ink-2); line-height: 1.6; }
h1, h2 { font-weight: var(--display-weight); color: var(--color-ink); } h3 { font-weight: var(--serif-small); }
.ruled { border-top: var(--rule-head) solid var(--color-ink); } .ruled > * + * { border-top: var(--rule-hair) solid var(--color-rule); }
.dropcap::first-letter { float: left; font: var(--serif-small) 3.3em/0.8 var(--font-display); padding: 0.1em 0.1em 0 0; color: var(--color-accent); }
.btn { min-height: 52px; border: var(--rule-hair) solid var(--color-ink); border-radius: var(--radius-pill); padding: 0 var(--space-lg); color: var(--color-ink); background: transparent; transition: background-color var(--dur-short) var(--ease-out), color var(--dur-short) var(--ease-out); }
.btn:hover { background: var(--color-ink); color: var(--color-paper); }
.stock { border-radius: 2px; background: var(--fibre) 0 0 / 220px, linear-gradient(160deg, var(--card-lit), var(--color-card) 55%, var(--card-shade)); box-shadow: var(--shadow-card), inset 1px 1px 0 var(--lit); text-shadow: 0 1px 0 var(--lit); }
.stock::before { content: ""; position: absolute; inset: 0.875rem; border: var(--rule-hair) solid var(--color-card-edge); }
.air::after { content: ""; position: absolute; inset: 0; background-image: var(--grain); background-size: 180px; opacity: 0.16; mix-blend-mode: multiply; }
```
