---
name: Manifesto
slug: manifesto
genre: editorial
paper: dark 13 60
display: display-condensed Anton
accent: warm 28
posture: committed
keywords: manifesto, statement, declaration, principles, beliefs, mission, movement, protest, cause, campaign, petition, activism, advocacy, rights, values, take a stand, bold launch, defiant, punk, record label
material: 暖调近黑底色、暖调米白墨色、Public Sans 低调正文上压海报字号紧排的 Anton 大写、细线、一条重磅墨色条与方形边缘、一个战斗红
photo: duotone paper ink con=24
pictured: Manifesto, Ledge hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/manifesto.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Manifesto

印在深色纸上的宣言：暖调近黑底色、暖调米白墨色、Anton 大写排到宽度允许的最大并紧排、低调的小号 Public Sans 正文、细线、一条重磅墨色条、方形边缘和一个战斗红。力量来自海报字号大写与安静正文的反差，以及省着用的红色；照片以米白墨印刷，硬朗、凑近，像贴上墙的传单。没有任何装饰。它不是贴纸与撕纸堆出来的抗议海报仿作，也不是带红色按钮的深色产品页。

## Tokens

```css
:root {
  --color-paper: oklch(13% 0.01 60); --color-paper-2: oklch(17% 0.011 60); --color-paper-3: oklch(22% 0.012 60);
  --color-ink: oklch(95% 0.014 85); --color-ink-2: oklch(84% 0.012 80); --color-muted: oklch(64% 0.016 65);
  --color-rule: oklch(31% 0.014 60);
  --color-accent: oklch(56% 0.228 28); --color-accent-deep: oklch(49% 0.2 28); --color-accent-text: oklch(64% 0.22 28); --color-accent-ink: oklch(98.5% 0.004 90);
  --color-focus: oklch(64% 0.22 28);
  --font-display: "Anton", "Impact", sans-serif; --font-body: "Public Sans", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: var(--font-body);
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --rule-bar: 4px; --shadow-card: none;
  --tracking-display: 0.004em; --display-weight: 400; --lh-tight: 0.9; --text-display: clamp(4.5rem, 12vw, 13rem);
}
```

## 字体

- **展示字体：**Anton 400、唯一字重、只限大写、`--tracking-display`。窄体大写放大一档：Ledge 或 Corridor 的 hero 标题用主题自己的 `--text-display`（到 13rem），宣言排到最长一行在十二栏内允许的最大字号，其他标题比共享字号阶梯大一级。每行各自成元素、绝不换行的标题（`white-space: nowrap`、以 `cqi` 定字号，stamp `waive 55b`）行高用 `--lh-tight`；任何可换行的标题行高用 1.02（55a）。
- **红词：**整页只有一个词，在 hero 标题内，用 `--color-accent-text`（stamp `waive 38iii`）。其余每个标题只用一种颜色。
- **正文：**Public Sans 400 与 600，朴素，用 `--color-ink-2`；21px 的导语已是它的上限。
- **标签、题注、表头、元信息、日期：**Public Sans 500 小一档，句首大写，不加字距，用 `--color-muted`。不用等宽。

## 表面

- 细线分隔：`--color-rule` 的 `--rule-hair` 用于行间与标题下方，像大报那样；导航下方或记录之上有一条墨色 `--rule-bar`；红色线条每页至多一次。
- 圆角 0、任何地方无阴影：不做盒装卡片、不做浮起。well 是细线之下的 `--color-paper-2` 场域。
- 色带：`--color-paper-2`，或全页唯一一块红反白表面，红色场域配 `--color-accent-ink` 文字；每页至多两条。
- 照片：凑近、硬光，拍页面为之声张的东西（一块板、一件工具、一双修理中的手），锐利、无面孔、裁得紧让边缘没入暗部。它们以米白墨印刷（`photo:` 双色调），方形，加 1px `--color-rule` 圈，要么通版要么不用。标题跨过照片时，只允许压在其最暗的三分之一上，且要垫一块 `--color-paper` 底板；红绝不碰照片。
- 一切都带暖调（色相 60 到 90），绝不用中性灰；无纹理、无装饰。

## Range

- **记录：**诉求、原则或条款做成细线之下的通栏行，每个序号用 Anton、区块字号、muted 墨色，条款用 Anton、标题字号，旁边一行朴素说明。
- **海报行：**一个日期、数字或口号用 Anton 横跨全部十二栏，排到这一行允许的最大，下方配 Steps 或一行短字；字号本身就是论点。
- **叠起来的信条：**三行短的 Anton 锁定在 `--lh-tight`，每行各自 nowrap，在纸上左齐排开，旁边什么都不放。
- **誓约：**一句 Anton 的话、名字空位嵌在其中，放在那片红色场域上，下方是邮箱与按钮。

## 控件

- 方形、尺规画出的控件：扁平红色块、`--color-accent-ink` 文字（hover 时 `--color-accent-deep`），旁边一枚 `--color-ink-2` 细线块、hover 反转为红。红场域上主按钮转为底色配墨色文字。
- 链接墨色、1px 下划线、hover 转 `--color-accent-text`；输入框方形、细线边框，坐在 `--color-paper-2` 上。
- 红场域之外，红色保持在一屏 5% 以内：红词、主控件、焦点圈、一条红线。

## 动效

唯一一个 clip 显现：hero 标题向上擦除一次（`clip-path: inset()`，绝不软淡入），时长 `--dur-long`、缓动 `--ease-out`。其余什么都不动；无回弹、无视差、无红色脉冲。

## 语气

命令式、短促、陈述：用战斗的语言，动词多于形容词，诉求用读者自己的名词说出来。不含糊；说出来，并站在它后面。

## 禁止事项

- 绝不要第二个强调色；红是唯一的颜色。
- 红色绝不漫过那唯一一块反白表面；红是信号，不是背景。
- 绝不用浅色底；这张纸保持深色。
- 绝无装饰：不要花饰、贴纸、撕边、硬偏移阴影，也不要彩色或调成红色的照片。
- 展示字体绝不用衬线、小写或词首大写式，标题绝不怯声怯气：Anton 在 1440 下低于 64px，就等于不再呐喊了。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Public+Sans:wght@400;500;600&display=swap" rel="stylesheet">
```

```css
body { color: var(--color-ink-2); }
h1, h2, h3 { font-weight: 400; text-transform: uppercase; line-height: 1.02; color: var(--color-ink); }
.display { line-height: var(--lh-tight); container-type: inline-size; }
.display > span { display: block; white-space: nowrap; }
.display .hot { color: var(--color-accent-text); }
.bar { border-bottom: var(--rule-bar) solid var(--color-ink); }
.btn { border: var(--rule-hair) solid transparent; background: none; border-radius: 0; padding: var(--space-sm) var(--space-lg); font-weight: 600; }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.btn--primary:hover { background: var(--color-accent-deep); }
.btn--secondary { border-color: var(--color-ink-2); color: var(--color-ink); }
.btn--secondary:hover { background: var(--color-accent); border-color: var(--color-accent); color: var(--color-accent-ink); }
.band--red { background: var(--color-accent); color: var(--color-accent-ink); }
.reveal { animation: wipe var(--dur-long) var(--ease-out) both; }
@keyframes wipe { from { clip-path: inset(100% 0 0 0); } to { clip-path: inset(0); } }
::selection { background: var(--color-accent); color: var(--color-accent-ink); }
```
