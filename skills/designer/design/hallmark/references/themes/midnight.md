---
name: Midnight
slug: midnight
genre: atmospheric
paper: dark 14 264
display: grotesk-sans Mona Sans
accent: cool 230
posture: committed
keywords: render, 3d, animation, vfx, film, video, frames, pipeline, generative, ai tool, model playground, dark mode, nocturnal, late-night, after-hours, overnight, moody, cinematic, cerebral, calm, technical, midnight
material: 午夜蓝铺满到每条边，冷白墨色，Mona Sans 加宽 300 叠在其正常宽度之上，以明度分级切方的表面，月光质感照片，唯一一抹蔚蓝
photo: duotone paper ink-2
pictured: Narrative Workflow, Settled hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/midnight.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Midnight

一件冷而安静的夜间仪器，蓝就是地面本身：深午夜蓝铺满到每条边，冷白墨色，标题用加宽 300 的 Mona Sans，像电影的片名字幕；阅读用同一家族的正常宽度；表面以更浅的蓝色分级、切方；唯一的信号色是蔚蓝。照片如月光降临，阴影落在地面的蓝里，高光落在墨色里。它不是霓虹暗色模式，不是磨砂玻璃，也不是黑底蓝按钮的页面。

## 令牌

```css
:root {
  --color-paper: oklch(14% 0.048 264); --color-paper-2: oklch(18.5% 0.052 264); --color-paper-3: oklch(23% 0.055 264);
  --color-ink: oklch(95% 0.016 250); --color-ink-2: oklch(88% 0.05 245); --color-muted: oklch(73% 0.04 256);
  --color-rule: oklch(29% 0.058 264); --color-rule-2: oklch(40% 0.06 262);
  --color-accent: oklch(80% 0.11 230); --color-accent-2: oklch(58% 0.1 236); --color-accent-ink: oklch(16% 0.05 264); --color-focus: oklch(84% 0.12 228);
  --font-display: "Mona Sans", ui-sans-serif, system-ui, sans-serif; --font-body: var(--font-display); --font-outlier: var(--font-display);
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px;
  --shadow-card: 0 24px 48px -24px oklch(6% 0.04 264 / 0.7);
  --tracking-display: -0.015em; --display-weight: 300; --display-stretch: 125%;
}
```

## 字体

- **标题字：**Mona Sans 300 加宽宽度用在 `h1` 与 `h2`，`--tracking-display`，行高 1.04，句首大写，正体。宽而轻的字重就是本主题的声音；长标题降到 `--text-display-s`，而不是收紧排版。条目标题用正常宽度的 500。
- **作为主角的数字：**展示字重 300，表列数字，从 `--text-display` 起最高到它的两倍，字距 -0.03em，单位在旁边用正常宽度 400 与 `--color-ink-2`。
- **正文字：**Mona Sans 400，正常宽度，行高 1.6。一个家族、两种宽度：冷感来自地面与墨色，绝不来自第二字体。
- **标签、表头、元信息、状态：**500，小一档，句首大写，不加字距，`--color-muted`。数字需要对比处一律用表列数字；任何地方不用等宽字体。

## 表面

- 深度是纸、纸-2、纸-3 之间的明度阶梯，半径 0 切方，像画框；抬升的表面用地面自身深色的 `--shadow-card`。表面不加描边；1px `--color-rule` 只用于分隔表格或列表中的行，其余一概不用。
- 色带：`--color-paper-2` 或 `--color-paper-3`，一页最多两条；绝不做蔚蓝色块，也绝不用浅色带。
- 照片：入夜后的低调光，夜里的建筑、亮灯的楼梯间、长长的走廊；单一主体保持静止，横裁或竖裁。双色调从纸色到墨-2，所以日光照片会变成一张泛白的纸：请选夜景。方形画框，1px 内缩描边用 8% 透明度的墨色，图注用标签体给出时刻或帧号。
- 无纹理、无玻璃、无模糊、无光晕。

## 适用手法

- **数字即宣言：**一个真实数字，展示字重，最高到 `--text-display` 的两倍，独自立在地面上，配单位与一行说明；加宽的轻字重让一个价格读起来像片名字幕。
- **换个角度看产品：**界面局部放大裁切，放在纸-2 井格上（作业单、仪表、联系表），以明度分级，绝不做画出来的窗口框。
- **步骤或夜班日志：**用 `<ol>` 排阶段或小时，每级标题用加宽字重，数字用表列体，当前项用墨色，其余用 muted；仪表（2px `--color-rule-2` 轨道，`--color-accent-2` 或蔚蓝填充）是唯一会动的线。
- **地面上的行与表单：**发丝线行，左侧加宽标题，右侧正常宽度；纸-2 色带上的计算器，答案是一个展示字重的数字。

## 控件

- 成对出现：实心蔚蓝矩形配 `--color-accent-ink` 文字，旁边是 `--color-rule-2` 描边的次级按钮，两者都方正、500 字重。分段选择用同一种方块，选中时填墨色。
- 链接悬停出现蔚蓝下划线；输入框落在纸面上，1px `--color-muted` 边缘，方正。
- 蔚蓝不超过 5%：唯一的主控件、链接悬停、一处仪表数值或一处大数字。绝不做色块、渐变或第二种光源。

## 动效

一次落定：首屏文字在 `--dur-long` 配 `--ease-out` 下从 0.6 渐入到 1，只播一次，从可见的默认状态出发。悬停让表面明度升一档。数值随其来源变化而变；任何东西都不滑动、不循环、不跟随光标。

## 语气

冷静、简省，夜班的语域：时刻、计数、成本。短陈述句；数字永远带上单位或时间。绝不夸张。

## 禁忌

- 绝不用暖色强调；这里的光是冷的。
- 绝不用重的标题字重，也绝不用正常宽度的标题；加宽的 300 就是这张脸。
- 绝不做灯：无径向光晕、无光圈、卡片上无亮边。
- 绝不用圆角，也绝不用浅色区块；从头到尾又暗又方。
- 绝不让原色照片与双色调并存，绝不用日光场景。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Mona+Sans:wdth,wght@100,400;100,500;125,300&display=swap" rel="stylesheet">
```

```css
h1, h2 { font-weight: var(--display-weight); font-stretch: var(--display-stretch); line-height: 1.04; }
h3 { font-weight: 500; }
.fig { font-weight: var(--display-weight); font-stretch: var(--display-stretch); letter-spacing: -0.03em; line-height: 0.9; font-variant-numeric: tabular-nums; }
.well { background: var(--color-paper-2); border-radius: var(--radius-card); }
.well--raised { background: var(--color-paper-3); box-shadow: var(--shadow-card); }
.btn { border: var(--rule-hair) solid transparent; background: none; border-radius: var(--radius-pill); padding: var(--space-sm) var(--space-lg); font-weight: 500; color: var(--color-ink); transition: background-color var(--dur-short) var(--ease-out); }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.btn--secondary { border-color: var(--color-rule-2); }
.btn--secondary:hover { background: var(--color-paper-2); }
.meter { height: 2px; background: var(--color-rule-2); } .meter > span { display: block; height: 100%; background: var(--color-accent); }
a:hover { text-decoration-color: var(--color-accent); }
.settle { animation: settle var(--dur-long) var(--ease-out) both; }
@keyframes settle { from { opacity: 0.6; } }
```
