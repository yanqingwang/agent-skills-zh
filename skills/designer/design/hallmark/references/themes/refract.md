---
name: Refract
slug: refract
genre: atmospheric
paper: light 98.2 95
display: grotesk-sans Funnel Display
accent: cool 232
posture: restrained
keywords: pool, lido, swim, spa, hotel, resort, water, skincare, sunscreen, eyewear, glass, optics, light, daylight, architecture, interiors, studio, wellness, bathhouse, summer, clean, calm, product launch, hardware
material: sunlit white plaster with real light falling across it, water caustics or prism dispersion rendered live, deep pool-blue ink, Funnel Display at a light weight over Funnel Sans, clear surfaces that cast tinted shadows, one water signal
pictured: Timetable-led, Stage hero
photo: natural con=3 exp=4
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/refract.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Refract

烈日下的白色灰泥，由光来承担装饰：一层水波焦散在地面移动，或一枚棱镜把光谱和它的亮尖抛洒在页面上。其余一切安静：深池蓝墨色、轻字重的 Funnel Display、透明的表面，其阴影带着穿过它的光的色调。像热天午后一间凉爽的房间。它不是彩虹渐变，不是模糊底上的磨砂玻璃，也不是蓝色的科技落地页。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(98.2% 0.006 95); --color-paper-2: oklch(96.4% 0.006 95); --color-paper-3: oklch(93.6% 0.008 95);
  --color-ink: oklch(23% 0.035 245); --color-ink-2: oklch(36% 0.035 245); --color-muted: oklch(50% 0.025 240);
  --color-rule: oklch(89.5% 0.008 230); --color-rule-2: oklch(93.5% 0.006 230);
  --color-accent: oklch(50% 0.12 234); --color-accent-hi: oklch(44% 0.12 236); --color-accent-ink: oklch(99% 0.003 95); --color-accent-soft: oklch(94% 0.025 220); --color-focus: oklch(56% 0.14 234);
  --color-shade: oklch(86% 0.05 212); --color-shade-2: oklch(74% 0.07 220); --color-light: oklch(99.7% 0.004 95);
  --spec-1: oklch(78% 0.15 32); --spec-2: oklch(90% 0.15 105); --spec-3: oklch(82% 0.13 175); --spec-4: oklch(66% 0.15 270);
  --color-slot: oklch(86% 0.05 212);
  --edge-light: inset 0 1px 0 oklch(100% 0 0 / 0.9), inset 0 0 0 1px oklch(100% 0 0 / 0.55);
  --shadow-card: 18px 28px 48px -26px oklch(52% 0.09 220 / 0.38), 2px 3px 6px -2px oklch(40% 0.05 230 / 0.12);
  --shadow-cast: 28px 40px 70px -30px oklch(60% 0.11 212 / 0.45);
  --font-display: "Funnel Display", ui-sans-serif, system-ui, sans-serif; --font-body: "Funnel Sans", ui-sans-serif, system-ui, sans-serif;
  --radius-card: 22px; --radius-inner: 12px; --radius-pill: 999px; --rule-hair: 1px;
  --tracking-display: -0.032em; --display-weight: 400;
}
```

两个旋钮，写入 stamp（印记）：`refract: water/pool`。同一次运行里的两个 Refract 页面，两者都不同。

| 旋钮 | 选项 |
| --- | --- |
| **光**（生成的地面） | `water`（默认）：流动水面的焦散，青绿阴影上的一张亮网。`glass`：穿过玻璃窗的阳光，窗沿分成暖与冷两半，一柄棱镜扇面横过光斑，落在产品上也落在地面上，缓慢如太阳 |
| **配色** | `pool`（默认），如上。`noon`：墨色 `oklch(20% 0.01 260)`，强调色近黑，光谱是唯一的颜色 |

## 字体（Type）

- **展示字体：**Funnel Display 400（陈述字号的大数字用 300），`--tracking-display`，行高 1.02，句首大写，单色。标题保持平静；光才是大声的部分。
- **正文：**Funnel Sans 400，17px，行高 1.6，用 `--color-ink-2`；导语大一档，用 `--color-muted`。
- **标签、表头、钟点：**Funnel Sans 500，小一档，句首大写，所有数字加 `tabular-nums`。绝不用等宽字体，绝不用加字距的大写。

## 表面（Surfaces）

- **光：**一块生成的画布或着色器，绝不是纹理照片，也绝不是渐变色块。`water` 之下阴影为 `--color-shade`，亮网用 `--color-light`，最亮的接缝处微微分出 `--spec-*`；`glass` 之下地面保持纸色，几条 `--spec-*` 光带以低角度落下，一侧带白色亮尖。光落在 Hero 上远离标题的一侧，在文字下方淡出到纸色，标题永远坐在纯纸面上。
- **透明表面：**面板是在光之上 72 至 86% 的白色，加 `--edge-light`，绝不模糊；影子从一个太阳落下、偏向右下（`--shadow-card`），带水色的调子。更大的一片投影（`--shadow-cast`）只给页面上唯一的主角物体。
- **横线：**`--color-rule` 发丝线，只横向，用于表格与列表。面板圆角 `--radius-card`，其内部 `--radius-inner`，控件用胶囊。
- **色带：**paper 与 paper-2；一条色带可以再次承载光（收尾或一句宣言），每页受光的地面绝不超过两块。
- **照片：**明亮、阳光、硬影，水、白色建筑或阳光下的产品；没有摆拍的人。通栏处直角，容器内 `--radius-card`。不用双色调。

## 版式（Range）

- **可预订的钟点排成泳道：**访客挑选场次时，场次排成长长的划线行，时间用展示数字，状态胶囊在行尾，下一个可预订的行由其身后一条薄薄的光带点亮。
- **阳光下的数字：**一个数字用 Funnel Display 300 排成陈述字号，光落在它旁边的空间上，单位与出处一行淡色小字。
- **一天化作光：**一条小时条带，细条的高度是光的强度或需求量，当前小时用一个强调色圆点标记，其余用 `--color-shade`。
- **桌上的产品：**产品的真实屏幕作为一块透明面板躺在光里，投影带色调，一个能真正移动光的可用控件。

## 控件（Controls）

- 主胶囊：`--color-accent` 之上覆 `--color-accent-ink`，白色内嵌顶边，48px；悬停加深为 `--color-accent-hi`。次胶囊：80% 白色加 `--edge-light` 与发丝线。
- 输入框是白色凹槽，带发丝线与 `--radius-inner`；焦点环用 `--color-focus`。
- 强调色只落在主按钮、焦点、当前标记与悬停链接上；光谱只存在于光里。

## 动效（Motion）

水以泳池的速度移动（约 12 秒完成一轮图案变化）；玻璃随太阳漂移，一条光带 60 秒横过。面板悬停抬起 2px，影子随之拉长。光在屏幕之外暂停。Reduced motion（减少动效）时：光静止为一帧。

## 语气（Voice）

明亮而平实，带一点感官：温度、钟点、光在做什么。

## 禁止事项（Do-nots）

- 绝不在文字上放彩虹、渐变按钮，也绝不给多于一个物体加光谱边框。
- 绝不用磨砂玻璃或背景模糊；透明表面保持透明。
- 绝不让光落在正文之下，也绝不让两块受光的地面相邻。
- 绝不用灰色投影；每一片影子都带光的色调，且从一个太阳落下。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Funnel+Display:wght@300;400;500&family=Funnel+Sans:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: var(--display-weight); letter-spacing: var(--tracking-display); line-height: 1.02; }
.clear { background: color-mix(in oklab, var(--color-light) 80%, transparent); border-radius: var(--radius-card); box-shadow: var(--edge-light), var(--shadow-card); }
.btn { min-height: 48px; padding: 0 var(--space-lg); border: 0; border-radius: var(--radius-pill); background: var(--color-accent); color: var(--color-accent-ink); font: 500 var(--text-md)/1 var(--font-body); box-shadow: var(--shadow-card); transition: background var(--dur-short) var(--ease-out); }
.btn:hover { background: var(--color-accent-hi); }
.btn--clear { background: color-mix(in oklab, var(--color-light) 80%, transparent); color: var(--color-ink); box-shadow: var(--edge-light), var(--shadow-card); }
.light { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; -webkit-mask-image: linear-gradient(to right, transparent 30%, var(--color-ink) 62%); mask-image: linear-gradient(to right, transparent 30%, var(--color-ink) 62%); }
```
