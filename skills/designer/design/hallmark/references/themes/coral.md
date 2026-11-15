---
name: Coral
slug: coral
genre: modern-minimal
paper: light 97 55
display: grotesk-sans General Sans
accent: warm 30
posture: restrained
keywords: saas, platform, billing, payments, invoicing, dashboard, b2b, startup, product, pricing, analytics, fintech, workflow, team, onboarding, trust, warm, human, calm
material: 暖灰纸张与毛毡桌面、左侧受光的棉质文具、通篇 General Sans 配 Geist Mono 数字、凸版印刷卡片控件、珊瑚色压进纸材标记唯一的落定状态
photo: muted sepia=8
pictured: Conversational FAQ, Desk hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/coral.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Coral

一个温暖、平实的产品声音被做成实体：毛毡桌上摆着精致文具，俯视、左侧来的一道日光。记录是带真实边缘的棉纸、信封和索引卡；控件是凸版印刷卡片；一件事落定的地方，压入一种珊瑚色墨。通篇 General Sans。不是奶油色编辑部页面，不是拟物玩具，也不是蓝色 SaaS 模板。

## Tokens

```css
:root {
  --color-paper: oklch(97% 0.006 55); --color-paper-2: oklch(94.5% 0.007 55); --color-paper-3: oklch(91.5% 0.009 55);
  --color-ink: oklch(21% 0.012 38); --color-ink-2: oklch(29% 0.013 40); --color-muted: oklch(47% 0.013 45);
  --color-rule: oklch(87% 0.009 55); --color-rule-2: oklch(81% 0.011 55);
  --color-accent: oklch(74% 0.125 30); --color-accent-ink: oklch(21% 0.012 38); --color-accent-2: oklch(54% 0.165 29); --color-focus: oklch(54% 0.17 30);
  --color-cotton: oklch(98.8% 0.0045 80); --color-desk: oklch(94.3% 0.008 64); --color-print: oklch(23% 0.012 38);
  --color-board: oklch(22% 0.011 40); --color-board-type: oklch(96.5% 0.006 70); --color-paid: oklch(55.5% 0.15 33);
  --tex-cotton: url("cotton.svg"); --tex-desk: url("felt.svg");
  --shade: 32% 0.03 50; --lit: 100% 0.005 80; --deep: 7% 0.01 40;
  --font-display: "General Sans", ui-sans-serif, system-ui, sans-serif; --font-body: var(--font-display);
  --font-outlier: "Geist Mono", ui-monospace, monospace;
  --radius-card: 8px; --radius-input: 6px; --radius-pill: 999px; --radius-stock: 8px; --rule-hair: 1px;
  --shadow-card: 0 1px 2px oklch(20% 0.01 35 / 0.05);
  --edge-stock: inset 0 1px 0 oklch(var(--lit) / 0.9), inset 0 -1px 0 oklch(var(--shade) / 0.07), 0 0 0 0.5px oklch(var(--shade) / 0.22), 0 1px 0 oklch(var(--shade) / 0.12);
  --cast-stock: 6px 5px 10px -6px oklch(var(--shade) / 0.3); --cast-stock-lift: 12px 10px 18px -8px oklch(var(--shade) / 0.3);
  --press-groove: inset 1px 1.5px 2px oklch(var(--shade) / 0.16), inset -1px -1px 0 oklch(var(--lit) / 0.9), 0 0 0 0.5px oklch(var(--shade) / 0.2);
  --tracking-display: -0.03em; --display-weight: 600;
}
```

## 字体

- **展示字体：**General Sans 600、`--tracking-display`、行高 1.02 到 1.08、句首大写、正体。单独的价格以两到三倍 `--text-display` 排，字距 -0.05em、行高 0.85，单位在旁用 `--text-title` 的 500。
- **正文：**General Sans 400 与 500。纸材上用 `--color-print`；墨板（board）上用 `--color-board-type`。
- **标签：**General Sans 500 小一档，句首大写，用 `--color-muted`。
- **栏内的数字：**Geist Mono 400（General Sans 没有 tabular 数字）。句中或标题里的价格仍用 General Sans。

## 表面

- 唯一光源，来自左侧：每个纸面物件顶边与左边受光、底边与右边落影，投影向右落下（`--edge-stock`、`--cast-stock`）。
- hero 底面是一张桌子：`--color-desk` 之上叠左侧日光径向渐变和生成的毛毡纹理。产品处理的记录做成桌上的文具：棉纸上的发票、信件与对账单、带玻璃纸显出地址的开窗信封、回函做成信函索引卡、卡片上压出的凹槽。每一件都是 `--color-cotton` 上的 CSS，从一个基准单位定尺寸，整体可缩放。
- 纹理是生成的，绝不是图片：构建过程写出 `cotton.svg`，一块 360px 的贴片，两层拼合的 feTurbulence（cloud 0.011、grain 0.92，暖而淡）加短纤维笔触，垫在每个纸面物件受光到落影的渐变之下；`felt.svg` 同样做法、0.018。区块保持素净。
- 落定状态（已付、已签、已订）压进纸材：那个词用 General Sans 600、`--color-paid`，经 SVG 滤镜把一面阴影墙偏移进字形，再让噪点遮罩留下不匀的墨，并倾斜几度。
- 一条 `--color-ink` 色带，即墨板；它上面的文具从 `--deep` 投影。
- 照片罕用：日光下一臂之遥的工作场景、低饱和；先用 CSS 搭的文具回答。

## Range

- **任务演成案头文书：**产品的任务用它自己在桌上的文件讲（一张纸装进信封、一张回函卡插进去、结果压进去），在 hero 里搭好，下方复用。
- **记录做成索引：**回函、预订或客户做成棉质索引卡，错位标签叠放，旁边整张纸上放着它们的记录。
- **墨板上的价格：**那个孤零零的数字以纸色排得巨大，旁边是划线的清单、说明它买什么；操作按钮坐在铺在色带上的文具上（一个信封盖、一张卡）。
- **另一侧：**收件人看到的样子，用棉纸搭出来，一个凹槽控件实时改写它。

## 控件

- 凸版卡片，不是胶囊：8px 圆角、48px 高、棉质纸材带 `--edge-stock` 与 `--cast-stock`，标签压进纸里（文字下方一道受光的阴影）；主按钮是墨色墨板，标签反方向压。Hover 抬起 1px、阴影换成 `--cast-stock-lift`；active 下压 1px。
- 两到四个的选项是一道压进棉纸的凹槽（`--press-groove`、12px 圆角），一张棉卡在槽里滑到选中的那档。
- 输入框 48px、6px 圆角、1px `--color-muted` 边框，深珊瑚色焦点。状态用墨色描边；珊瑚色只花在压印的落定状态、链接下划线和焦点上。

## 动效

一次，字体加载完成且进入视口后：任务在桌上演约六秒，只用 transform 与 opacity，离屏即暂停，然后静止。Reduced motion 与无脚本时直接呈现完成状态。

## 语气

平实、温暖的第二人称句子，讲工作与钱：谁、多少钱、什么时候、产品做了什么。绝不卖萌。

## 禁止事项

- 绝不用冷调纸、蓝色信号或第二个光源；每道影子都落在右边。
- 绝不用胶囊按钮或扁平方块按钮；控件是压印卡片。
- 绝不拍纸的照片；文具用 CSS 搭。
- 珊瑚色绝不做色带、文字背后的填充或标题；它是唯一落定状态的压印墨色。

## 构建提示

```html
<link href="https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: var(--display-weight); }
.desk { background-color: var(--color-desk); background-image: radial-gradient(90% 120% at 0% 30%, var(--color-cotton), transparent 62%), var(--tex-desk); }
.stock { background-color: var(--color-cotton); background-image: linear-gradient(100deg, var(--color-cotton), transparent 45%), var(--tex-cotton); color: var(--color-print); box-shadow: var(--edge-stock), var(--cast-stock); }
.btn { min-height: 48px; padding: 0 var(--space-lg); border: 0; border-radius: var(--radius-stock); font-weight: 500; transition: transform var(--dur-short) var(--ease-out); }
.btn--card { background-color: var(--color-cotton); background-image: var(--tex-cotton); color: var(--color-print); text-shadow: 0.5px 0.75px 0 var(--color-cotton); box-shadow: var(--edge-stock), var(--cast-stock); }
.btn--ink { background: var(--color-board); color: var(--color-board-type); text-shadow: 0 -0.75px 0 var(--color-ink); box-shadow: var(--cast-stock); }
.btn:hover { transform: translateY(-1px); box-shadow: var(--edge-stock), var(--cast-stock-lift); } .btn:active { transform: translateY(1px); }
.fig { font-family: var(--font-outlier); font-variant-numeric: tabular-nums; }
a:hover { text-decoration-color: var(--color-accent-2); }
```
