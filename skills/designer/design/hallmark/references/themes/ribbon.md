---
name: Ribbon
slug: ribbon
genre: atmospheric
paper: light 98.5 85
display: grotesk-sans Instrument Sans
accent: chromatic-teal 190
posture: committed
keywords: sleep, sound, soundscape, audio, night, rest, calm, wellness, meditation, white noise, ambient, listen, headphones, wind down, bedtime, quiet, breathing, app, subscription
material: warm off-white or blue-black night, Instrument Sans at a quiet weight over Figtree, machined parts lit from above, the hour drawn as light on a generated canvas, one signal
photo: muted sepia=14
pictured: Night Notes, Stage hero, in the two-in-the-morning colourway
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/ribbon.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Ribbon

睡前的一小时，安静排布：每个标题都用 Instrument Sans 400，正体、紧凑字距；阅读用软灰色的 Figtree；用发丝线代替盒子；夜色本身画成缓慢的光，垫在一台真正能调电平的金属机件之后。平静来自轻盈的字、缓慢的光与做工扎实的部件。它不是光鲜的 wellness 应用，也不是满天星月的页面。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(98.2% 0.008 82); --color-paper-2: oklch(95.8% 0.011 82); --color-paper-3: oklch(92.3% 0.014 82);
  --color-ink: oklch(18% 0.006 80); --color-ink-2: oklch(30% 0.008 80); --color-muted: oklch(47% 0.012 80);
  --color-rule: oklch(89.5% 0.011 82); --color-rule-2: oklch(93.5% 0.009 82);
  --color-accent: oklch(44% 0.075 190); --color-accent-soft: oklch(92% 0.028 190); --color-accent-ink: oklch(98% 0.006 85); --color-focus: oklch(52% 0.09 190);
  --color-band: oklch(26% 0.045 195); --color-band-ink: oklch(94% 0.012 85);
  --color-slot: oklch(69% 0.07 80);
  --metal-hi: oklch(97% 0.006 85); --metal-lo: oklch(85% 0.01 85);
  --edge-light: inset 0 1px 0 oklch(100% 0 0 / 0.5);
  --shadow-part: 0 1px 0 oklch(20% 0.01 80 / 0.25), 0 10px 18px -6px oklch(20% 0.01 80 / 0.3);
  --shadow-panel: 0 1px 0 oklch(20% 0.01 80 / 0.2), 0 24px 48px -16px oklch(20% 0.02 80 / 0.35);
  --font-display: "Instrument Sans", ui-sans-serif, system-ui, sans-serif; --font-body: "Figtree", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "JetBrains Mono", ui-monospace, monospace;
  --radius-card: 20px; --radius-part: 6px; --radius-pill: 999px; --rule-hair: 1px;
  --shadow-card: none;
  --tracking-display: -0.035em; --display-weight: 400;
}
```

一个拨盘，即配色，写入 stamp（印记）：`ribbon: two-in-the-morning`。强调色是唯一被点亮的东西；`--color-slot` 是照片罩色；`--color-accent-soft` 是推子轨道或按下状态的胶囊，绝不作文字色。

| 配色 | 纸 | 墨 | 强调色、金属 |
| --- | --- | --- | --- |
| `dawn`（默认） | `oklch(98.2% 0.008 82)` | `oklch(18% 0.006 80)` | 青绿 `oklch(44% 0.075 190)`；铝金属如上，夜色画在 `--color-band` 上 |
| `two-in-the-morning` | 蓝黑 `oklch(13.2% 0.022 258)`，paper-2 取 16.4%，横线取 27% | `oklch(93.5% 0.012 85)`，muted 用 `oklch(72% 0.02 255)` | 一扇亮着的窗，琥珀 `oklch(82% 0.095 68)` 配 `oklch(20% 0.03 62)` 文字；金属 `oklch(44% 0.012 255)` 到 `oklch(25% 0.014 255)`，阴影取自黑 |
| `moss` | 鼠尾草绿 `oklch(89% 0.034 140)` | `oklch(22% 0.03 150)` | 赭黄 `oklch(48% 0.115 70)`；罩色用深青绿 `oklch(46% 0.07 195)` |

## 字体（Type）

- **展示字体：**Instrument Sans 400，正体，`--tracking-display`，行高 1.04，句首大写，单一颜色；小标题（面板名、字标）用 500。大数字与电平值也用展示字体，等高表格数字。
- **正文：**Figtree 400，17px，行高 1.6，用 `--color-muted`；部件名称与读数用 Figtree 500。
- **标签：**Figtree 500，小一号，句首大写，不加字距，用 `--color-muted`，读数用表格数字。

## 表面（Surfaces）

- Hero 底图是把这一小时画成光的单张生成画布（dawn 配色画在 `--color-band` 上）：雨用细而慢的划痕，风用长而柔的线条，低垂的地平线上远远一排亮点，提示词里的声响是什么就画什么，底下垫 CSS 的天空渐入地面的渐变。标题背后绝不放照片，绝无星星或月亮。
- 自上而下受光的金属机件：面板用上下渐变，加 `--edge-light` 与 `--shadow-panel`；一块内凹底座（inset 阴影）承载带滚花旋钮的竖直推子（`--metal-hi` 到 `--metal-lo`，细条纹握持面，一条点亮的强调色指示线），一条下凹槽，其辉光填充到电平位置，两侧刻度；一切与时间相关的东西用可拖拽曲线，配金属手柄。
- 纹理由脚本生成：160px 画布噪点贴片写入 `--grain`，`soft-light` 混合、透明度 0.35 至 0.55，只用于夜色与面板。
- 阅读区用横线不用盒子：1px `--color-rule` 发丝线。圆角：控件用胶囊，机件用 `--radius-part`，面板用 `--radius-card`。
- 照片：安静而贴近的夜（一扇窗、一盏灯、远处一列火车）；弱光，无人。`--radius-card`，无边框。

## 版式（Range）

- **乐器即 Hero：**产品控件做成真正可用的金属面板，旁边一行标题，底下是画出来的夜。
- **行即电平列表：**每个部件的名称用展示字体压在发丝线上，说明用 Figtree，电平值用展示字号数字；旁边并排放 app 框内的同一面板，实时同步。
- **时间画成曲线：**一夜之间的变化画成横贯全宽、彼此交叠落下的线条，竖列标记时刻，下方用 Figtree 表格数字标电平。
- **价格落在地平线下：**数字用展示字体排 8 至 10rem，压在同一片大地与亮着的横排之上，配一行 Figtree 文字与点亮的胶囊按钮。

## 控件（Controls）

- 金属胶囊按钮，高 52px：上下渐变加 `--edge-light` 与 `--shadow-part`，1px 边框；主按钮用强调色，inset 高光从内部点亮。按下时下沉 1px。开关是胶囊轨道配金属旋钮，开启时点亮强调色。
- 推子与曲线是真实输入控件（`role="slider"`，支持键盘步进）。声音只在按下 Listen 之后播放，Stop 或 Esc 结束。
- 强调色落在主按钮、焦点环、推子辉光、指示线与一个数字上。

## 动效（Motion）

缓慢而有呼吸感，`--ease-in-out` 配 `--dur-long`。环境画布与 CSS 循环各至多一个，离开屏幕即暂停；电平缓动，绝不跳变。减弱动效或无脚本时：一夜静止，每个机件停在其示例电平上。

## 语气（Voice）

平静而具体：几点、什么声、多响。绝不许诺完美睡眠。

## 禁止事项（Do-nots）

- 绝不用斜体或粗重标题；展示字体保持正体的 400 与 500。
- 绝不用星空、月亮、藏青到紫的渐变或图库睡者照片。
- 乐器上绝不用塑料感或扁平控件；机件是金属加工的，自上而下受光，光源唯一。
- 绝不画波形或均衡器；电平活在推子与线条上。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500&family=Figtree:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: 400; font-synthesis: none; line-height: 1.04; }
.btn { min-height: 52px; padding: 0 var(--space-lg); border: var(--rule-hair) solid var(--color-rule); border-radius: var(--radius-pill); background: linear-gradient(var(--color-paper-2), var(--color-paper-3)); box-shadow: var(--edge-light), var(--shadow-part); color: var(--color-ink); font: 500 var(--text-md)/1 var(--font-body); }
.btn--primary { background: var(--color-accent); border-color: var(--color-accent); color: var(--color-accent-ink); }
.btn:active { transform: translateY(1px); }
.panel { border-radius: var(--radius-card); background: linear-gradient(var(--color-paper-2), var(--color-paper-3)); box-shadow: var(--edge-light), var(--shadow-panel); }
.cap { border-radius: var(--radius-part); background: linear-gradient(var(--metal-hi), var(--metal-lo)); box-shadow: var(--edge-light), var(--shadow-part); }
.grain { background-image: var(--grain); background-size: 160px; mix-blend-mode: soft-light; opacity: 0.4; }
a:hover { text-decoration-color: var(--color-accent); }
```
