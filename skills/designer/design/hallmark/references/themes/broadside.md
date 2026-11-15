---
name: Broadside
slug: broadside
genre: editorial
paper: light 92 88
display: display-condensed Six Caps
accent: warm 33
posture: committed
keywords: auction, sale, market, fair, event, one night, announcement, town, notice, poster, bill, lots, machinery, tools, festival, fete, hammer, date, venue, tickets
material: grained buff stock, near-black ink, Six Caps and Bevan wood capitals over Archivo Narrow, ink rules at one point or five, one vermilion
photo: duotone ink paper con=20
pictured: Marquee Hero, Settled hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/broadside.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Broadside

一张印刷商的告示单：带颗粒纹理的米黄纸、近黑的墨色、撑满版心宽的 Six Caps 压在 Bevan 之上，Archivo Narrow 排小字，横线只有一点或五点两种粗细，外加一处朱红。它响亮，是因为大写字母够高、横线够重，绝不是因为画了什么东西；照片以墨色平实印刷，就像拍卖告示单上的那块印版。不是西部片仿古，也不是柔软的奶油色编辑页。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(92% 0.028 88); --color-paper-2: oklch(88.5% 0.032 88); --color-paper-3: oklch(85% 0.036 86);
  --color-ink: oklch(18% 0.01 50); --color-ink-2: oklch(30% 0.012 50); --color-muted: oklch(43% 0.02 62);
  --color-rule: oklch(75% 0.028 82);
  --color-accent: oklch(53% 0.19 33); --color-accent-ink: oklch(95.5% 0.018 88); --color-focus: oklch(53% 0.19 33);
  --font-display: "Six Caps", "Impact", sans-serif; --font-display-2: "Bevan", Georgia, serif;
  --font-body: "Archivo Narrow", "Arial Narrow", ui-sans-serif, sans-serif;
  --font-outlier: var(--font-body);
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --rule-bar: 5px; --rule-frame: 3px;
  --shadow-card: none;
  --tracking-display: 0.02em; --display-weight: 400;
  --grain: 0.08;
}
```

只有一个拨盘，即配色，写入 stamp（印记）：`broadside: bill`。

| 配色 | 纸张 | 墨色 | 强调色 |
| --- | --- | --- | --- |
| `bill`（默认） | 上面的代码块 | 墨色 | 朱红 |
| `inked` | oklch(17% 0.01 60)，颗粒改为滤色 | 米黄 oklch(92% 0.028 88) | 朱红提亮为 oklch(63% 0.19 33)；纸色横带转暗 |
| `red-bill` | 以朱红作纸 | 米黄 oklch(95.5% 0.018 88)，对比 5.5:1 | 米黄；姿态取 Drenched |

## 字体（Type）

- **Six Caps** 400，大写，行高 0.88，`--tracking-display`，用于 h1、大数字与撑满版心的行。它是撑排（fitted）而非阶梯字号：每一行是独立的元素且绝不换行（`white-space: nowrap`，55b 闸门），其字号由 `cqi` 度量出的行宽决定，恰好填满所在列；同一块内堆叠的行字号各不相同，正如手工排字。
- **Bevan** 400 用于区块标题、条目标题、字标与简短的事实句；大写，不加字距，行高 1。
- **Archivo Narrow** 400 与 600，行高 1.5，用于一切供阅读的文字；标签、表头、图注与元信息用它的 500，小一号，句首大写，不加字距，`--color-muted`。数字用 Six Caps，或一行之内用 Archivo Narrow 的表格数字。
- 三个字族，无 outlier（异类字体）：一副木活字，哥特体管尺度，粗衬线体担分量。

## 表面（Surfaces）

- 横线：区块、表格之上或告示单两列之间压墨色 `--rule-bar`，页眉（running head）之下压墨色 `--rule-hair`，行与行之间用 `--color-rule` 的 `--rule-hair`。一点与五点之间没有其他粗细。
- 到处直角，无阴影。边框即双线：`--rule-frame` 的墨色边框，向内 3px 处再压一条 1px 墨色细线，围住内嵌面板或照片。
- 色带：`--color-paper-2`、墨底米黄字，或一条米黄字的朱红色带；每页至多两条。
- 照片：平实的日光纪实、平视角度，待售之物完整侧面入镜，细节在臂距之内拍摄；没有人正对镜头。以墨色印在纸面上（`photo:` 的 duotone 双色调），直角，装在双线边框里；文字绝不压在照片上，照片下方的图注要承载一个事实。
- 颗粒，唯一的纹理：斑点层（`texture.md` § 1）以 `--grain` 应用，米黄上正片叠底、墨色上滤色，用在色带、内嵌面板与照片边框上，绝不压在正文之下。

## 版式（Range）

- 排成告示单的时刻表：每一天一列，列顶压一条五点横线，列名用 Six Caps 撑满列宽，钟点用 Bevan，小字压在 1 点横线之下；列与列之间用五点竖线分隔。
- 一个数字或日期用 Six Caps 撑满整个版心，作为它所在屏幕唯一的一行朱红，小字缀于其下。
- 细目作行：左侧 Bevan 标签，右侧 Archivo Narrow 600 的事实，行间发丝线，首行之上压一条五点横线；尚未得知的事实印作弱化的占位，绝不编造。
- 朱红色带上放表单：米黄底色字段加墨色细线，墨色块作提交动作，标题用 Bevan。

## 控件（Controls）

- 墨色填充块，Archivo Narrow 600，不加字距的大写（在大写展示字体之下是合法的），旁边是同样的块但作未填充的双线边框样式；直角，48px，每页只允许一处填充。
- 链接用墨色、带下划线，悬停转朱红；输入框直角，48px，1px 墨色边框。
- 朱红只用于一整行展示文字（独立元素，绝不作标题的一部分），或每屏一个数字，底为米黄或 `--color-paper-2`。

## 动效（Motion）

印刷品，所以是静的：实时数字原地更新，撑排行在字体加载完成时撑一次。没有跑马灯，没有悬停放大，没有显现动效。

## 语气（Voice）

像朗读一张拍卖告示：日期、地点、拍品与钟点，每样只说一次。用大写字母喊，用小字解释，说的是它所面向行业的行话。

## 禁止事项（Do-nots）

- 绝不让大字行参差不齐；填不满版心的 Six Caps 行要么撑满，要么删掉。
- 代码之外绝无第四种字体：排字盘里只有 Six Caps、Bevan 和窄体。
- 绝无圆角；边框、控件与照片都是直角。
- 绝无第二种颜色，文字与照片皆然；照片以墨色印刷。
- 绝不画法槌、星形或纹饰；大写字母与照片才是响亮的东西。
- 绝不每一屏都是照片；告示单有一半是文字，文字正是响亮的那一半。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Six+Caps&family=Bevan&family=Archivo+Narrow:wght@400;500;600&display=swap" rel="stylesheet">
```

```css
h1, .display { font-family: var(--font-display); font-weight: 400; text-transform: uppercase; line-height: 0.88; letter-spacing: var(--tracking-display); }
.fit { display: block; white-space: nowrap; }
h2, h3, .wordmark { font-family: var(--font-display-2); font-weight: 400; text-transform: uppercase; line-height: 1; letter-spacing: 0; }
.rule-bar { border-top: var(--rule-bar) solid var(--color-ink); }
.frame, .btn--frame { border: var(--rule-frame) solid var(--color-ink); box-shadow: inset 0 0 0 3px var(--color-paper), inset 0 0 0 4px var(--color-ink); }
.frame { padding: var(--space-lg); } .frame--photo { padding: var(--space-2xs); }
.btn { display: inline-flex; align-items: center; min-height: 48px; padding: 0 var(--space-xl); border: 3px solid var(--color-ink); background: var(--color-ink); color: var(--color-paper); font: 600 var(--text-sm)/1 var(--font-body); text-transform: uppercase; }
.btn--frame { background: transparent; color: var(--color-ink); }
.grained { position: relative; isolation: isolate; }
.grained::after { content: ""; position: absolute; inset: 0; pointer-events: none; opacity: var(--grain); mix-blend-mode: multiply; } /* the speck SVG, texture.md § 1 */
::selection { background: color-mix(in oklab, var(--color-accent) 30%, transparent); }
```
