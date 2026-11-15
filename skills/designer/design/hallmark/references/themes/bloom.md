---
name: Bloom
slug: bloom
genre: atmospheric
paper: light 97 72
display: grotesk-sans Ranade
accent: warm 36
posture: committed
keywords: generative, ai creative, music, song, video, image, voice, art, make, create, compose, render, imagine, prompt, creative studio, playground, expressive, warm, daylight, consumer creative, portrait, headshot, selfie, retouch
material: 带颗粒与生成工作网格的暖调米白纸张、两处安静的陶土色光晕、暖赭墨色、Ranade 配一处正体 Gambarino 数字、俯光照明的橡胶与盒装部件、圆角 clip 上的声部色调
photo: warm exp=4
pictured: Workbench, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/bloom.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Bloom

日光落在工作纸上：带微弱颗粒的暖调米白纸张、媒介自己的网格（钢琴卷帘、时间线、标尺）印进底色并从主舞台向外淡出、赭色墨水、Ranade 配一处正体 Gambarino 时刻。创作发生在网格上的圆角 clip 里；你摸到的部件是实体的：嵌在金属圈里的橡胶帽、从一摞盒子里滑出的那一盒。它不是带霓虹辉光的深色生成画布，不是奶油色编辑部页面，也不是陶土色海报。

## Tokens

```css
:root {
  --color-paper: oklch(97% 0.010 72); --color-paper-2: oklch(94.6% 0.013 70); --color-paper-3: oklch(91.5% 0.016 66);
  --color-ink: oklch(21% 0.024 40); --color-ink-2: oklch(31% 0.022 46); --color-muted: oklch(49% 0.02 56);
  --color-rule: oklch(88% 0.014 64); --color-sheet: oklch(98.7% 0.007 78);
  --color-accent: oklch(53% 0.145 36); --color-accent-2: oklch(66% 0.10 55); --color-accent-soft: oklch(53% 0.145 36 / 0.11);
  --color-accent-ink: oklch(98.5% 0.008 72); --color-focus: oklch(53% 0.145 36);
  --lane-1: oklch(50% 0.04 55); --lane-2: oklch(48% 0.105 28); --lane-3: oklch(70% 0.115 72); --lane-4: oklch(65% 0.085 12);
  --grid-16: oklch(21% 0.024 40 / 0.035); --grid-beat: oklch(21% 0.024 40 / 0.075); --grid-bar: oklch(21% 0.024 40 / 0.15); --grid-row: oklch(21% 0.024 40 / 0.045);
  --rubber: oklch(55% 0.15 34); --rubber-hi: oklch(66% 0.125 42); --rubber-lo: oklch(43% 0.125 31);
  --umber: oklch(30% 0.03 45); --bezel: oklch(92.5% 0.014 68); --case: oklch(93.5% 0.012 70);
  --hi: oklch(99.6% 0.006 80 / 0.75); --shade-1: oklch(21% 0.024 40 / 0.08); --shade-2: oklch(21% 0.024 40 / 0.16); --shade-3: oklch(30% 0.06 40 / 0.28);
  --font-display: "Ranade", ui-sans-serif, system-ui, sans-serif; --font-body: var(--font-display);
  --font-outlier: "Gambarino", Georgia, serif; --font-code: "Geist Mono", ui-monospace, monospace;
  --radius-card: 18px; --radius-inner: 10px; --radius-clip: 6px; --radius-pill: 999px; --rule-hair: 1px;
  --shadow-card: 0 1px 2px oklch(21% 0.024 40 / 0.06), 0 18px 36px -18px oklch(21% 0.024 40 / 0.26);
  --shadow-lift: 0 2px 4px oklch(21% 0.024 40 / 0.07), 0 36px 72px -32px oklch(45% 0.1 40 / 0.34);
  --tracking-display: -0.024em; --display-weight: 600;
}
```

## 字体

- **展示字体：**所有标题用 Ranade 600、`--tracking-display`、行高 1.04 到 1.08、句首大写、只用一种颜色：墨色。
- **正文：**Ranade 400、17 到 18px、行高 1.55；标签与控件用 500。总共三个字重。
- **衬线时刻：**Gambarino 400、正体、每页一次：一个 160px 以上的数字，或一段导语。绝不当标题，绝不用斜体。
- **标签：**Ranade 500 小一档，句首大写，用 `--color-muted`。Geist Mono 只用于标尺的细小数字和成品内部的时间码。

## 表面

- 底色就是用 CSS 画的媒介网格：叠加的 linear-gradient 画出小节、拍、十六分与行（钢琴卷帘每隔一个八度给黑键行着色），铺在主舞台之后的 `--color-sheet` 上，再淡淡延伸过它，并用遮罩径向淡出。网格会在步骤旁和收尾处小幅回访。
- 网格上是作品：四个声部轨用 `--lane-*` 色调做成圆角 clip（`--radius-clip`、一层着色渐变、声部色调的内嵌细线、一条受光的顶边），承载小节波形或音符；一条细线播放头；一条琴键条和一条细数字标尺。
- 纹理是生成的：纸张上盖 180px feTurbulence 颗粒、强度 5%；橡胶上 30%、soft-light。
- 每个部件都有来自上方的光。两处暖色光晕保留、更安静：`--color-accent` 约 8%、右上，`--color-accent-2` 约 5%、左下，固定不动。
- 浮起的暖表面，绝不做细线盒子：用 `--shadow-card`，最重要的那块用 `--shadow-lift`。色带至多两条，绝不用陶土色。
- 照片：家里的日光、手、窗边的乐器；绝不用深夜的摄影棚。

## Range

- **输入在同一张网格上变成输出：**用户给的东西（一段哼唱、一张草图、一行字）画成一道轨迹落定到网格上，结果在下方的声部轨里长出来，按下 Play 就真的会播放。
- **选项做成盒脊：**选项是一摞盒子（带光条纹的色带、卡片标签、部件的小圆点）；选中的那盒滑出，网格重新排列。
- **一个衬线数字**旁边三步，每步配一小块网格特写。
- **结果作为一个 clip** 收尾时放在网格上，可下载。

## 控件

- 主按钮是嵌在凹陷金属圈里的橡胶帽：拱顶的 `--rubber` 径向渐变、从顶部受光、带颗粒，装在 `--bezel` 的 well 里带内阴影；它坐在一枚 `--color-sheet` 胶囊的左侧、旁边是它的标签，产品聆听时它的光圈呼吸。按下时下沉 1px。
- 次级：带阴影圈与受光顶边的纸面胶囊，或一枚 `--umber` 胶囊。
- 链接陶土色，hover 加下划线；输入框 52px 胶囊，1px `--color-muted` 边。

## 动效

一次，进入视口时：输入画入（约 3 秒）、音符落定、播放头滑回起点、声部轨长出来。只用 transform 与 opacity，离屏即暂停。Reduced motion 或无脚本时：直接呈现完成后的排布，播放头在起点。光晕绝不动。

## 语气

温暖、日光感、具体：动词（哼唱、制作、聆听）、产出（歌曲、声部、场景），以及在哪里。

## 禁止事项

- 绝不用深色画布、霓虹辉光或第三处光晕。
- 绝不用陶土色场域或卡片；陶土色是橡胶、是链接、是声部轨。
- 绝不让网格以全强度铺满整个区块；它从主舞台向外淡出。
- 绝不用斜体衬线，衬线绝不进标题、也绝不出现在两处。

## 构建提示

```html
<link href="https://api.fontshare.com/v2/css?f[]=ranade@400,500,600&display=swap" rel="stylesheet">
<link href="https://api.fontshare.com/v2/css?f[]=gambarino@400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: var(--display-weight); color: var(--color-ink); }
.roll { --beat: 40px; --row: 14px; background-color: var(--color-sheet); background-image: linear-gradient(to right, var(--grid-bar) 1px, transparent 1px), linear-gradient(to right, var(--grid-beat) 1px, transparent 1px), linear-gradient(to right, var(--grid-16) 1px, transparent 1px), linear-gradient(to bottom, var(--grid-row) 1px, transparent 1px); background-size: calc(var(--beat) * 4) 100%, var(--beat) 100%, calc(var(--beat) / 4) 100%, 100% var(--row); }
.clip { --c: var(--lane-1); border-radius: var(--radius-clip); background: linear-gradient(color-mix(in oklab, var(--c) 18%, var(--color-sheet)), color-mix(in oklab, var(--c) 28%, var(--color-sheet))); box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--c) 42%, transparent), inset 0 1px 0 var(--hi); }
.rec { border-radius: 50%; background: radial-gradient(circle at 50% 30%, var(--bezel), var(--color-paper-3)); box-shadow: inset 0 2px 3px var(--shade-2), 0 1px 0 var(--hi); }
.rec__cap { border-radius: 50%; background: radial-gradient(120% 110% at 50% 18%, var(--rubber-hi), var(--rubber) 48%, var(--rubber-lo)); box-shadow: inset 0 1px 0.5px var(--hi), 0 5px 9px -3px var(--shade-3); }
.pill { border-radius: var(--radius-pill); background: var(--color-sheet); box-shadow: 0 0 0 1px var(--shade-1), 0 8px 18px -10px var(--shade-2), inset 0 1px 0 var(--hi); font-weight: 500; }
a { color: var(--color-accent); text-underline-offset: 0.2em; }
```
