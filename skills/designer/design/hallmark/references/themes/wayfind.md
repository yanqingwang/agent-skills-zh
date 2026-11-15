---
name: Wayfind
slug: wayfind
genre: modern-minimal
paper: light 95.5 250
display: mono Chivo Mono
accent: cool 264
posture: committed
keywords: transit, metro, rail, station, wayfinding, departures, timetable, live, map, commute, city, platform, signage, logistics, status, operations, schedule, mobility, travel, trip, journey, itinerary, booking, flights, airport
material: cool grey paper, blue-black ink, Chivo Mono throughout, square 2px ink borders, ink plates, cobalt for what is live, amber for figures on ink
photo: natural sat=-12 con=10
pictured: Station Sequence, Stage hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/wayfind.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Wayfind

公共导视排成页面：冷灰纸、蓝黑墨色，每个字形都用 Chivo Mono（一种克制的怪诞体，按发车板的固定字格裁切），直角 2px 墨色边框，承载标牌的墨色牌面，钴蓝给实时信息，琥珀给数字。等宽字是那块牌子的字面，边框标出路线。它在日光下三米外一眼可读；它不是开发者工具，不是暗色终端，也不是复古发车板仿古。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(95.5% 0.006 250); --color-paper-2: oklch(91% 0.009 250); --color-paper-3: oklch(99.5% 0.005 250);
  --color-ink: oklch(16% 0.014 262); --color-ink-2: oklch(29% 0.014 262); --color-muted: oklch(47% 0.016 260);
  --color-rule: oklch(80% 0.011 250); --color-ink-rule: oklch(34% 0.014 262);
  --color-accent: oklch(51% 0.22 264); --color-accent-2: oklch(81% 0.16 82); --color-accent-ink: oklch(99.5% 0.003 250); --color-focus: oklch(51% 0.22 264);
  --font-display: "Chivo Mono", ui-monospace, monospace; --font-body: var(--font-display); --font-outlier: var(--font-body);
  --radius-card: 0; --radius-pill: 999px; --rule-hair: 1px; --rule-bar: 2px;
  --shadow-card: 0 24px 40px -24px oklch(8% 0.01 260 / 0.6);
  --tracking-display: -0.03em; --display-weight: 800;
}
```

三种配色，每页设定一次，写入 stamp（印记）：`wayfind: platform`。

| 配色 | 纸、墨、横线 |
| --- | --- |
| `platform`（默认） | 上面的代码块 |
| `night` | 纸 `oklch(15% 0.012 262)`，墨 `oklch(96% 0.005 250)`，横线 `oklch(31% 0.014 262)`，钴蓝提亮为 `oklch(62% 0.2 264)` |
| `signal` | 纸取钴蓝 `oklch(51% 0.22 264)`，墨为白色，横线 `oklch(75% 0.12 264)`；钴蓝按钮转为墨色按钮 |

## 字体（Type）

- **展示字体：**Chivo Mono 800，`--tracking-display`，行高 0.98，句首大写。等宽一行占宽很多，所以 `h1` 封顶 4.75rem，标题保持一眼读完的长度。
- **正文：**Chivo Mono 400，行高 1.55，一切数字用 `tabular-nums`。等宽字在这里就是材质（waive 64）：发车板的字面定了整页的调。三种字重：400、500、800。
- **数字：**分钟、站台与出口用 800，当数字是区块存在的理由时排到 `--text-display-s` 或更大；墨底上用琥珀，纸面上用墨色。
- **标签、表头、胶囊、按钮：**Chivo Mono 500，小一号（按钮用 800），句首大写，不加字距；导视靠等宽字与边框读懂，绝不靠大写字母。

## 表面（Surfaces）

- 横线：每个表面都用 `--rule-bar` 墨色边框（内嵌面板、牌面、按钮、导航下沿、表头线）；行分隔用 `--color-rule` 的 `--rule-hair`，墨底上用 `--color-ink-rule`。
- 圆角除胶囊外处处为 0。深度靠边框；`--shadow-card` 只允许浮在其他表面之上的表面使用。
- 牌面：2px 边框内一块方形墨色色场（或琥珀色场压墨色文字），承载一条指令与它的数字，就像标牌承载站台号。
- 色带：`--color-paper-2`，一条数字转琥珀的 `--color-ink` 色带，或 `signal` 配色下的一块钴蓝色场；每页至多两条色带。
- 照片：平视看到的路网：站台、瓷砖墙、进站的列车、通向日光的楼梯；人物只从背后拍且在移动中。直角，装进 2px 墨色边框；文字绝不压在照片上，只压在画框内的牌面上。图注写明车站或线路。用产品搭建的手机屏幕按 9:19.5 装进同款边框，绝不用手绘手机壳。
- 无纹理，无渐变。

## 版式（Range）

- **发车板排成表格**，放在墨色色带上：目的地用 500，线路画成路网自身颜色的小方块，分钟用 800 琥珀、标题字号起步，晚点行以琥珀填充压墨色文字，表头线为 2px 纸色。
- **路线排成步骤：**出去的路是排成一行的三四块牌面，每块是 2px 边框的方形，承载一条指令（车厢、楼梯、出口）与它的数字，块间以 2px 墨线相连，如走廊指示牌。
- **状态排成行：**每条线路或班次一整行，色样、名称用 800、起讫用 400、状态放在右端；刚更新的那一行加一颗钴蓝实时圆点。
- **数字作标牌：**一个数字用 800 排展示字号，装在带边框的牌面里，单位缀旁，下方是边贴边直角单元格的车站选择器，可切换它。

## 控件（Controls）

- 钴蓝填充按钮，旁边是透明按钮加 `--rule-bar` 墨色边框；两者直角，Chivo Mono 800，句首大写，高 48 至 52px。
- 选项组是共享 2px 边框的直角单元格；选中格墨色填充配纸色文字。链接用墨色、带下划线，悬停转钴蓝；输入框直角，2px 墨色边框，置于 `--color-paper-3`。
- 钴蓝只给实时之物（当前站点、时钟、主操作）；琥珀只给墨底上的数字，或作压墨色文字的填充。

## 动效（Motion）

发车板式的硬朗：颜色变化用 `steps(1)` 配 `--dur-micro`，行原地更新，滚动无显现动效。行更新时实时圆点闪一次；它绝不循环。

## 语气（Voice）

导视口吻：站台、出口、分钟、车厢。祈使句，短；标题一眼读完。

## 禁止事项（Do-nots）

- 任何地方绝不用比例字体，正文也不行。
- 纸面上绝不用琥珀作文字色；它只出现在墨底上，或作压墨色文字的填充。
- 绝无第三种亮色，除非是路网自身的线路色，作名称旁的小方块。
- 绝不用圆角卡片或卡片柔影；Wayfind 靠边框说话。
- 绝不手绘站台、列车或车厢序列来顶替真实场所；车站靠照片，屏幕靠搭建。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Chivo+Mono:wght@400;500;800&display=swap" rel="stylesheet">
```

```css
body { font-variant-numeric: tabular-nums; }
h1, h2, h3 { font-weight: 800; line-height: 0.98; }
h1 { font-size: min(var(--text-display), 4.75rem); }
small, th, figcaption { font-weight: 500; color: var(--color-muted); }
.btn { display: inline-flex; align-items: center; gap: var(--space-xs); padding: var(--space-md) var(--space-lg); border: var(--rule-bar) solid currentColor; font: 800 var(--text-sm)/1 var(--font-body); color: inherit; transition: background-color var(--dur-micro) steps(1); }
.btn--primary { background: var(--color-accent); border-color: var(--color-accent); color: var(--color-accent-ink); }
.plate { border: var(--rule-bar) solid var(--color-ink); background: var(--color-ink); color: var(--color-paper); }
.plate .figure { font-weight: 800; color: var(--color-accent-2); }
.band--ink { background: var(--color-ink); color: var(--color-paper); }
th { border-bottom: var(--rule-bar) solid currentColor; } td { border-bottom: var(--rule-hair) solid var(--color-rule); }
::selection { background: var(--color-accent-2); color: var(--color-ink); }
```
