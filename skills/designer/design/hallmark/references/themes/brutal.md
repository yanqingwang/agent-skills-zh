---
name: Brutal
slug: brutal
genre: editorial
paper: light 97.5 95
display: grotesk-heavy Libre Franklin
accent: chromatic-yellow 105
posture: committed
keywords: brutalist, raw, bold, high-contrast, statement, agency, design studio, portfolio, streetwear, drop, zine, type-forward, graphic design, poster, festival, collective, no-nonsense, uncompromising
material: 近白海报纸，近黑墨色化作 3px 线，格子单元与实心填充，全大写 Libre Franklin 900 叠在其 400 之上，零圆角，一抹酸性黄填充
photo: duotone ink paper con=24
pictured: Marquee Hero, Poster hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/brutal.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Brutal

一张粗粝、工程感的纸：近白海报纸，近黑墨色以 3px 线到场，格子单元与实心填充，Libre Franklin 用到最黑的字重配紧排大写，零圆角，唯一的酸性黄只用于填充。网格是画出来的，不是暗示的：单元格共享线框，装在盒子里的一个大号数字或单词就是页面的装饰。照片以墨色硬印。它不是暗黑黑客页面，不是装饰化的 zine，也不是错位阴影贴纸堆。

## 令牌

```css
:root {
  --color-paper: oklch(97.5% 0.006 95); --color-paper-2: oklch(94% 0.007 95); --color-paper-3: oklch(89.5% 0.008 95);
  --color-ink: oklch(10% 0.006 95); --color-ink-2: oklch(16% 0.006 95); --color-muted: oklch(40% 0.008 95);
  --color-rule: oklch(10% 0.006 95);
  --color-accent: oklch(90% 0.19 105); --color-accent-ink: oklch(10% 0.006 95); --color-focus: oklch(48% 0.1 110);
  --font-display: "Libre Franklin", ui-sans-serif, system-ui, sans-serif; --font-body: var(--font-display);
  --font-outlier: var(--font-display);
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --rule-bar: 3px; --shadow-card: none;
  --tracking-display: -0.03em; --display-weight: 900;
}
```

## 字体

- **标题字：**Libre Franklin 900，全大写，`--tracking-display`，行高 1.0（大写换行的下限），每个标题一个字重。宣言句或首屏标题可以冲到展示上限甚至更远；按行宽排满，而不是礼貌地缩在行宽里。大写属于标题、字标，以及作为单元格全部内容的单词或数字。
- **正文字：**Libre Franklin 400，17 到 18px，行高 1.5，句首大写，用墨色；条目标题与控件用 700，句首大写。总共三个字重：400、700、900。
- **数字：**序号、计数与日期用 900 配 `tabular-nums`，承载一行时用 `--text-section` 或更大。
- **标签、图注、表头：**Libre Franklin 400，小一档，句首大写，用 `--color-muted`；等宽只出现在代码里。

## 表面

- 只有两个线宽，再无其他：`--rule-bar` 用 `--color-rule` 给井格、表格、单元格或照片画框；`--rule-hair` 分隔其内的行。相邻单元格共享一条 3px 线，绝不用两条。
- 一切零圆角。深度是填充与边框，绝不是阴影：带边框的纸、墨色填充配纸色文字，或墨色之下的那一个黄色填充；没有任何东西浮在纸面之上。
- 色带：`--color-ink` 色带配纸色文字，或上下用 `--rule-bar` 划线的 `--color-paper-2` 色带；一页最多两条。黄色绝不做色带。
- 照片：事物使用中的原始纪实，光源就是现场有的（舞台灯、闪光灯、夜晚的街道）：人群内部拍的人群、开门前的房间、舞台屏；绝不要摆拍面孔。以墨色硬印（`photo:` 双色调），紧凑裁切、平齐嵌入 `--rule-bar` 画框，或页面最响亮处整幅出血。文字只在与画框平齐的实心墨块或纸块上接触照片；绝不用遮罩。
- 无纹理、无装饰、无渐变。

## 适用手法

- **索引排成带框表格：**行装在一个 3px 盒子里，行间发丝线，数字用 900、区块级字号、独占一格，条目用 700、标题级字号，一行 400；悬停或当前行以黄填充、其上覆墨。
- **宣言句：**一句直白的话，900 大写，横跨全部十二列，展示级字号或更大，坐在一条 3px 线上，屏上除署名外别无他物。
- **单元格拼 bento：**事实作为 900 大写的单词或数字装进共享线框的盒式单元格，一个两倍大的主格，一个做对比的墨格，一格嵌一张照片。
- **表单即网格：**字段作为共享线框的盒式单元格，选项是两个大号单词格，选中时填黄，发送按钮是一个墨格。

## 控件

- 成对出现：`--rule-bar` 描边纸面按钮，旁边是实心墨色按钮配纸色文字，Libre Franklin 700 句首大写，48 到 52px；悬停一帧内反转任意一个。
- 链接用墨色加下划线；悬停在墨色之下填黄。输入框：零圆角，`--rule-bar` 边框，纸上墨字，52px。
- 黄色是填充，绝不是文字、线条或圆环：选中的选项、行文中的 `mark`、悬停的行或链接。永远垫在墨色之下，绝不在照片之上，占屏 5% 以下。焦点用深橄榄 `--color-focus`。

## 动效

没有任何滑动。状态一帧内翻转：表面反转成墨底纸字，或在墨色之下填黄。无入场、无弹跳、无视差。

## 语气

直白、陈述式：标题用大写，其余句首大写；用行业自己的话，不含糊其辞，不夸大。把事情平平地说出来。

## 禁忌

- 绝不用圆角或阴影（模糊的或硬偏移的）；深度靠边框与填充。
- 绝不用装饰、花饰或叠层错位堆；Brutal 是粗粝，不是装饰。
- 绝不用黑纸；这是带黑色结构的浅色纸面。
- 绝不引入第二颜色：照片以墨色印刷，黄色只做填充。
- 单元格相接处绝不用两条线；加倍的 6px 接缝读起来是错误，不是结构。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@400;700;900&display=swap" rel="stylesheet">
```

```css
h1, h2, .display { font-family: var(--font-display); font-weight: var(--display-weight); text-transform: uppercase; letter-spacing: var(--tracking-display); line-height: 1; }
h3 { font-family: var(--font-display); font-weight: 700; }
.btn { border: var(--rule-bar) solid var(--color-rule); border-radius: 0; padding: var(--space-xs) var(--space-lg); background: var(--color-paper); color: var(--color-ink); font-weight: 700; transition: none; }
.btn:hover, .btn--ink { background: var(--color-ink); color: var(--color-paper); } .btn--ink:hover { background: var(--color-paper); color: var(--color-ink); }
.cells { display: grid; gap: 0; border: var(--rule-bar) solid var(--color-rule); }
.cells > * { margin: calc(var(--rule-bar) * -1) 0 0 calc(var(--rule-bar) * -1); border: var(--rule-bar) solid var(--color-rule); }
.well--ink, .band--ink { background: var(--color-ink); color: var(--color-paper); }
.is-chosen, p mark, a:hover { background: var(--color-accent); color: var(--color-accent-ink); }
.photo { display: block; border: var(--rule-bar) solid var(--color-rule); border-radius: 0; }
::selection { background: var(--color-accent); color: var(--color-accent-ink); }
```
