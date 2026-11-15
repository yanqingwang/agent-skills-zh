---
name: Sport
slug: sport
genre: editorial
paper: light 98 250
display: display-condensed Saira Condensed
accent: chromatic-volt 120
posture: restrained
keywords: running, marathon, race, training, fitness, gym, team, league, fixtures, standings, scoreboard, athletics, performance, splits, sportswear, club, match, tournament
material: cool concrete paper, blue-black ink, uppercase Saira Condensed over Albert Sans, condensed figures and mono times, two-weight rules, one volt fill
photo: duotone ink paper con=20
pictured: Stat-Led, Poster hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/sport.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Sport

一张成绩单式的材料：冷调混凝土纸面、蓝黑墨色、大写 Saira Condensed 800 压在 Albert Sans 正文之上，大号窄体数字与 JetBrains Mono 计时，发丝线加一条更重的墨线，唯一颜色是电光黄绿（volt）。volt 是填色：墨字压在它上面，它绝不做纸面上的文字。照片印在墨色里，像一本秩序册。它读得快，靠的是窄体大写、数字与动作，绝不靠倾斜或渐变；它不是运动服广告，也不是霓虹电竞页。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(98% 0.005 250); --color-paper-2: oklch(95% 0.006 250); --color-paper-3: oklch(91.5% 0.007 250);
  --color-ink: oklch(16% 0.080 260); --color-ink-2: oklch(22% 0.060 258); --color-muted: oklch(50% 0.020 250);
  --color-rule: oklch(78% 0.008 250); --color-rule-2: oklch(36% 0.060 255);
  --color-accent: oklch(88% 0.200 120); --color-accent-ink: oklch(16% 0.080 260); --color-accent-deep: oklch(58% 0.145 125);
  --color-focus: oklch(58% 0.145 125); --color-slot: oklch(76% 0.07 258);
  --font-display: "Saira Condensed", sans-serif; --font-body: "Albert Sans", ui-sans-serif, sans-serif;
  --font-outlier: "JetBrains Mono", ui-monospace, monospace;
  --radius-card: 4px; --radius-pill: 4px; --rule-hair: 1px; --rule-bar: 2px;
  --shadow-card: none;
  --tracking-display: -0.015em; --display-weight: 800;
}
```

## 字体（Type）

- **展示字体：**Saira Condensed 800，全大写，`--tracking-display`，行高 1.02，正体、不倾斜。真正的窄体设计，大写叠排也不拥挤，海报字号压在照片上也成立；速度感在大写里，绝不靠倾斜。
- **正文：**Albert Sans 400 与 500，句首大写。
- **数字：**陈述字号（一段距离、一块场地、一个价格、一个日期）用 Saira Condensed 800 加 `tabular-nums`，从 `--text-display-s` 起，下方配一行 Albert Sans 标签。分栏与实时数据（计时、分段、号码布）用 JetBrains Mono 500，比其标签大至少一档。等宽字体是秒表，绝不做标签或标题。
- **标签、图注、表头、单位：**Albert Sans 500 小一档，句首大写，不加字距，用 `--color-muted`；volt 填色之上每个字都用墨色。

## 表面（Surfaces）

- 两种线宽，绝不用装框卡片：`--color-rule` 的 `--rule-hair` 划分行与网格；`--color-rule-2` 的 `--rule-bar` 开合一张表、切分一个章节。
- 控件、输入框与照片圆角 4px；不用胶囊。
- 深度来自线条与纸面分层，绝不来自阴影：凹槽是墨线之下的 `--color-paper-2`。
- 色带：`--color-paper-2` 色带，或一条 `--color-ink` 色带配纸色文字；每页至多两条，绝不用 volt 色带。
- 照片：以跑者视线或更低的角度拍比赛：步频中段的一群人、沥青上的腿与鞋、爬上山谷一侧的公路、正被别上的号码布；硬朗日光、动作清晰、裁切紧凑，无人摆拍。以墨色印在纸面上（`photo:` 双色调），4px 圆角，8% 的内嵌墨色发丝线。照片上的文字用纸色、从边缘压一层墨色暗化；一个 volt 数字可以带着一个事实压住画框一角（那一英里、那个计时）。
- 无纹理，除照片暗化层外无渐变，无硬偏移阴影。

## 版式（Range）

- **比赛化作数字：**提示词的三四个数字用窄体大写排成展示字号，压在墨线之下，发丝线分隔，至多一个落在 volt 填色上。
- **比赛事实之上的可用控件：**墨色色带上的配速或计时规划器，选定的时间用等宽字体排展示字号，每一英里都在划线网格中原位变化，终点格用 volt。
- **成绩排成一张单子：**墨线开合一张号码布与计时的表格，数字用等宽字体；被关注跑者的行抬高一档纸面，其最新分段用 volt。
- **赛道化作赛段：**起点到终点排成一条墨线上的编号赛段，各配一个窄体大写标题与一行文字，进行中的赛段用 volt。

## 控件（Controls）

- 控件对：volt 填充的方块配墨色文字，旁边是 2px 墨色描边的另一个，两者 4px，用展示字面的大写、不另加字距；照片上的次按钮取纸色。
- 链接悬停时长出 `--color-accent-deep` 下划线（纸上 3:1）；输入框 4px，1px `--color-rule` 边框，焦点环用 `--color-focus`。
- volt 永远是墨字之下的填色，且不超过一块屏幕的 5%：主控件、活动行、一个高亮数字。

## 动效（Motion）

除状态与实时数据外皆不动：链接悬停时一条深 volt 下划线长出，一行抬高一档纸面，实时分段原位变化，绝不计数上跳。无显现，无视差。

## 语气（Voice）

赛道广播的平实：距离、计时、地点，像裁判长喊出来那样。标题用大写祈使句，其下句首大写，数字优先于文字，动词优先于形容词。

## 禁止事项（Do-nots）

- 绝不倾斜或斜体化展示字体；正体的窄体大写就是速度感。
- 绝不把展示字距放宽过零，也不收紧到两个大写字母相碰。
- 绝不用偏暖的纸面；地面是冷调混凝土，色相 250。
- 绝不用 volt 文字、纸面上的 volt 发丝线或第二种强调色；照片印在墨色里，绝不保留自己的颜色。
- 绝不要奖牌、奖杯、领奖台或球衣纹理，画的拍的都不要；比赛就是公路与跑者。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@800&family=Albert+Sans:wght@400;500&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: var(--display-weight); letter-spacing: var(--tracking-display); text-transform: uppercase; line-height: 1.02; }
.figure { font: var(--display-weight) var(--text-display)/0.9 var(--font-display); font-variant-numeric: tabular-nums; }
.time { font: 500 var(--text-2xl)/1 var(--font-outlier); font-variant-numeric: tabular-nums; }
.btn { border: var(--rule-bar) solid transparent; border-radius: var(--radius-card); padding: var(--space-sm) var(--space-lg); font: var(--display-weight) var(--text-md)/1.25 var(--font-display); text-transform: uppercase; }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.btn--secondary { border-color: var(--color-ink); color: var(--color-ink); }
.well { background: var(--color-paper-2); border-top: var(--rule-bar) solid var(--color-rule-2); }
.rule { border-top: var(--rule-bar) solid var(--color-rule-2); }
th, td { border-top: var(--rule-hair) solid var(--color-rule); }
.photo { border-radius: var(--radius-card); outline: 1px solid color-mix(in oklab, var(--color-ink) 8%, transparent); outline-offset: -1px; }
.scrim { background: linear-gradient(to top, color-mix(in oklab, var(--color-ink) 70%, transparent), transparent 60%); color: var(--color-paper); }
a:hover { text-decoration-color: var(--color-accent-deep); }
::selection { background: var(--color-accent); color: var(--color-ink); }
```
