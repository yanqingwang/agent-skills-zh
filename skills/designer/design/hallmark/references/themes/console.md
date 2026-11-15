---
name: Console
slug: console
genre: modern-minimal
paper: dark 17 250
display: grotesk-sans Host Grotesk
accent: chromatic-amber 80
posture: restrained
keywords: lab, laboratory, protocol, experiment, notebook, science, research, observability, monitoring, version control, audit, compliance, instruments, data, devtools, engineering, telemetry, record, operations, dark, developer
material: graphite ground in three lightness steps, pale ink, hairline panels cut from one surface, Host Grotesk 500 for reading, Atkinson Hyperlegible Mono for what was measured, amber for a person and cool blue for an instrument
photo: duotone paper-3 ink
pictured: Audit Trail, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/console.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Console

一件由细心的人保管的仪器：石墨底分三个明度阶梯，从一个表面切出的发丝线面板，人读的部分用 Host Grotesk，仪器测得的部分用 Atkinson Hyperlegible Mono，琥珀色代表人、冷蓝代表仪器。底色保持中性，两种含义以同等分量落在上面，且没有任何东西发光。它不是霓虹终端，不是玻璃质感仪表盘，也不是科幻控制室。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(17% 0.008 250); --color-paper-2: oklch(21% 0.009 250); --color-paper-3: oklch(13.5% 0.007 250);
  --color-ink: oklch(95% 0.005 250); --color-ink-2: oklch(83% 0.008 250); --color-muted: oklch(71% 0.01 250);
  --color-rule: oklch(31% 0.01 250); --color-rule-2: oklch(42% 0.012 250);
  --color-accent: oklch(82% 0.15 80); --color-accent-ink: oklch(18% 0.04 75); --color-accent-soft: oklch(29% 0.05 80); --color-focus: oklch(82% 0.15 80);
  --color-cool: oklch(77% 0.12 245); --color-cool-soft: oklch(29% 0.05 245);
  --color-ok: oklch(76% 0.15 150); --color-ok-soft: oklch(24.5% 0.03 150); --color-bad: oklch(70% 0.17 25); --color-bad-soft: oklch(24.5% 0.035 25);
  --font-display: "Host Grotesk", ui-sans-serif, system-ui, sans-serif; --font-body: var(--font-display);
  --font-outlier: "Atkinson Hyperlegible Mono", ui-monospace, monospace;
  --radius-card: 10px; --radius-pill: 6px; --rule-hair: 1px;
  --shadow-card: none;
  --tracking-display: -0.03em; --display-weight: 500;
}
```

一个旋钮，即配色，写入 stamp（印记）：`console: graphite` 为石墨，即上面的 Token；`paper`，底 oklch(98% 0.006 85) 之上覆墨色 oklch(19% 0.010 60)，琥珀 oklch(54% 0.14 70)、冷色 oklch(52% 0.14 250)，纸色色带转为浅色；`amber-room`，底 oklch(15% 0.022 70) 之上覆墨色 oklch(95% 0.012 85)，琥珀 oklch(82% 0.15 82)，冷色转为冰蓝 oklch(82% 0.08 200)。每一种配色里，琥珀都代表人，冷色都代表仪器。

## 字体（Type）

- **展示字体：**Host Grotesk 500，`--tracking-display`，行高 1.02 至 1.05，句首大写，正体；大字号下保持平静，绝不用 700。
- **正文：**Host Grotesk 400，16 至 17px，行高 1.55，用 `--color-muted`；导语用 `--color-ink-2`。
- **标签、图注、表头、chips：**Host Grotesk 500 小一档，句首大写，用 `--color-muted`。
- **测得的数据：**Atkinson Hyperlegible Mono 400 与 500，14 至 15px，用于仪器或系统写下的东西：一个读数连同单位、一个 id、一段 diff、一个时间戳，所有数字用表格数字。它的斜杠零与带尾一的 1 就是意义所在；排成展示字号时，它是本主题最响的东西。绝不做标签、标题或控件。

## 表面（Surfaces）

- 发丝线面板：一个表面是 1px `--color-rule`，内部 `--color-paper-2`，圆角 10px（控件 6px）。相邻的面板是被 1px 线切开的一个表面；`--color-rule-2` 标出选中行或轨迹的脊线。
- 三个阶梯，无灯：底色、抬高一档的面板、最深一档留给代码、日志、变更行与照片。无阴影、无光晕、无辉光、无聚光。
- 色带：`--color-paper-3` 或 `--color-paper-2` 色带，绝不用琥珀色场；每页至多两条。
- 照片：一或两张，拍实验台，绝不拍脸（持移液器的戴手套的手、一排试管），暗调近景，从最深一阶到墨色的黑白，圆角 10px，1px 线边缘，下方配图注。
- 表面无纹理、无渐变。

## 版式（Range）

- **Diff：**一次比较排成一个面板里的两个版本，加减符号的分栏用 ok 与 bad 色，变更行压在柔和色底上，旁边用人话写明原因。
- **读数：**单个数值用测量字体排展示字号，其上是被它替换的旧值，下方用琥珀、冷色与墨色写明谁、何时、为何；一条记录构成的一句陈述。
- **轨迹：**行排成 1px `--color-rule-2` 脊线上的审计轨迹，每条是一个版本，琥珀色是人，冷色是时间，墨色是原因；时刻表或更新日志也这样读。
- **面板：**bento 或对比版块从一个表面以 1px 接缝切出，一个面板领衔，每个面板以全保真承载产品本身，而不是它的图片。

## 控件（Controls）

- 一对：琥珀填色配 `--color-accent-ink`，旁边是 `--color-paper-2` 上的 1px `--color-rule-2` 描边，两者 6px 圆角，Host Grotesk 500。
- chip 只承载状态：1px 边框内 4px 圆角的标签字体，按含义染 `--color-accent-soft` 或 `--color-cool-soft`。版本选择器是一排这样的 chip，选中的一对压在冷色底上。输入框坐在 `--color-paper-3` 上，收在 1px 边框内、6px 圆角；链接下划线用 `--color-rule-2`，悬停转琥珀。
- 两种含义：琥珀是人（一位操作者、一次偏离、当前步骤、唯一的主控件）；冷色是仪器（一个读数、一条轨迹、一个版本）。ok 与 bad 只用于 diff 与状态。

## 动效（Motion）

数值随其来源变化，时长 `--dur-short`、缓动 `--ease-out`；一张图可以绘制一次。无显现、无视差、无悬停浮起。

## 语气（Voice）

细心之人的实验记录本：数值、单位、时间、签名的人。没有单位或时间的数字什么都不是。

## 禁止事项（Do-nots）

- 绝不调换含义；琥珀色的读数或冷色的偏离，是主题在说谎。
- 绝不用底下带阴影的浮动卡片。
- 绝不用第三种信号色，也绝不用彩色照片。
- 绝不在标签、标题或按钮上用等宽字体；等宽是仪器写下的东西。
- 绝不做整页小面板；每页有一个数值或一条记录排成大字。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Host+Grotesk:wght@400;500&family=Atkinson+Hyperlegible+Mono:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: 500; letter-spacing: var(--tracking-display); line-height: 1.04; }
.panels { display: grid; gap: var(--rule-hair); background: var(--color-rule); border: var(--rule-hair) solid var(--color-rule); border-radius: var(--radius-card); overflow: hidden; }
.panels > * { background: var(--color-paper-2); }
.measured { font-family: var(--font-outlier); font-size: var(--text-sm); font-variant-numeric: tabular-nums slashed-zero; }
.reading { font-family: var(--font-outlier); font-size: var(--text-display); font-weight: 400; letter-spacing: -0.04em; line-height: 1; color: var(--color-ink); }
.row--minus { background: var(--color-bad-soft); } .row--plus { background: var(--color-ok-soft); }
.btn { border: var(--rule-hair) solid var(--color-rule-2); border-radius: var(--radius-pill); padding: var(--space-sm) var(--space-md); background: var(--color-paper-2); color: var(--color-ink); font-weight: 500; transition: background-color var(--dur-short) var(--ease-out); }
.btn--primary { background: var(--color-accent); border-color: var(--color-accent); color: var(--color-accent-ink); }
::selection { background: color-mix(in oklab, var(--color-accent) 25%, transparent); }
```
