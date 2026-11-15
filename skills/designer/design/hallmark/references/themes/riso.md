---
name: Riso
slug: riso
genre: editorial
paper: light 97 90
display: grotesk-heavy Cabinet Grotesk
accent: chromatic-pink 356
posture: committed
keywords: risograph, riso, print studio, print fair, zine, small press, poster, art book, spot colour, two colour, indie press, diy, handmade, prints, open studio
material: bright uncoated stock and no black, a medium blue drum for every word, a fluorescent pink drum for the fills, purple where they cross, Cabinet Grotesk 800 over Literata, grain, one word a hair out of register
photo: duotone ink paper-2 con=14
pictured: Job Sheet, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/riso.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Riso

两只滚筒印出的一趟小印量活，再无其他：明亮的非涂布纸，一只中蓝滚筒排下每一个字、一只荧光粉滚筒印所有填色，交叠处是一种没人调过的紫。Cabinet Grotesk 800 标题压 Literata 正文，油墨跳断处有颗粒，一个词稍稍脱版一丝。它读起来是手工的，因为不完美住在油墨里，不在胶带与涂鸦。它不是干净的矢量平涂，不是霓虹 zine，而且永远没有黑。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(97% 0.011 90); --color-paper-2: oklch(93.5% 0.034 356); --color-paper-3: oklch(84% 0.11 356);
  --color-ink: oklch(40% 0.165 265); --color-ink-2: oklch(45% 0.15 265); --color-muted: oklch(50% 0.115 265);
  --color-rule: oklch(85% 0.045 265);
  --color-accent: oklch(68% 0.235 356); --color-accent-ink: oklch(27% 0.13 265); --color-focus: oklch(44% 0.2 265);
  --font-display: "Cabinet Grotesk", ui-sans-serif, sans-serif; --font-body: "Literata", ui-serif, Georgia, serif;
  --radius-card: 2px; --radius-pill: 2px; --rule-hair: 1px;
  --shadow-card: none; --texture-opacity: 0.08;
  --tracking-display: -0.025em; --display-weight: 800;
}
```

## 字体（Type）

- **展示字体：**Cabinet Grotesk 800，`--tracking-display`，句首大写，印在蓝色里；`h1` 行高 0.92，`h2` 0.98。一个标题一个字重、一种颜色。作为报价的数字用它排，表格数字。
- **错版的那个词**（stamp `waive 38iii`）：Hero 标题里一个焦点词经两只滚筒各印一次，粉色副本藏在蓝色后面、向右下挪 2 至 3px，只露出边缘（`texture.md` § 3）。每页一次。
- **正文与导语：**Literata 400，opsz 随字号，印在蓝色里。
- **标签、图注、表头、导航：**Literata 500 小一档，句首大写，用 `--color-muted` 或蓝色。不用等宽：数字用 Literata 的表格数字。

## 表面（Surfaces）

- 无黑：每个字、每条线、每个图标都由蓝滚筒印，所有填色由粉滚筒印；粉色叠印蓝色之处（`mix-blend-mode: multiply`）紫就显形，没人去画它。
- 粉滚筒的网屏就是纸面：`--color-paper-2`（浅网屏）垫在任何文字下，`--color-paper-3`（半强度）只垫展示文字，实心粉配 `--color-accent-ink`。蓝滚筒可以实心印，文字镂空到纸底。每页两条色带。
- 发丝线用 `--color-rule`，框住数字的线用 1.5px 蓝，2px 圆角，无阴影；深度就是叠印。
- 照片：作品与房间在均匀光下，裁切紧凑，保留真实影调范围。每张经两只滚筒印，蓝暗部落进浅粉网屏（`photo:` 双色调），2px 圆角，上面盖颗粒，图注在下方用 Literata。
- 颗粒，声明在先：油墨跳断处的纸面斑点（`texture.md` § 1，浅斑）以 `--texture-opacity` 铺在填色、色带与照片上，绝不压正文；颗粒与错版是同一滚筒家族。

## 版式（Range）

- **数字**排成两色叠印：数字用蓝色 Cabinet 800 排展示字号，一块实心粉形状以 multiply 压过它的一部分，紫色只在滚筒交叠处印出。一个价格或日期就这样带一层网屏。
- **步骤**化作分色：同一幅图先只看蓝色版，再只看粉色版，然后看双版齐全的成品，三块印版收在发丝线框里压在纸底上；流程就是那幅画。
- **行与表单**压在浅粉网屏上：价目表或订单是 Literata 表格数字的蓝色发丝线行，实时合计用展示字面，选中的行压在半强度网屏上。
- **色带**满强度只用一只滚筒：实心蓝配镂空到纸底的宣言和压在其上的粉色主按钮，或实心粉配深蓝文字；展示字号的宣言是这种材料能发出的最响的声音。

## 控件（Controls）

- 一对：粉色填充矩形配 `--color-accent-ink` 文字，旁边是 1.5px 蓝描边的另一个，两者 2px 圆角、Cabinet Grotesk 800、15px；按下时控件向右下沉 1px，像一张纸落定。
- 链接粉色下划线，悬停加粗；输入框 48px 高、2px 圆角，纸底上 1.5px 蓝边框，值用 Cabinet 800。
- 粉落在主按钮、链接下划线与每屏一个填色上；焦点环是蓝。

## 动效（Motion）

一次显现：加载时粉滚筒以 `--ease-out`、`--dur-long` 落进它的错位一次，绝不循环。控件以 `--dur-short` 变色；其余一律不动。

## 语气（Voice）

具体、手工排版：说出油墨、纸、滚筒与价格；动词优先于形容词。不完美是故意的。

## 禁止事项（Do-nots）

- 绝不用黑墨或灰色；唯一的第三色是滚筒交叠出来的紫。
- 绝不用套准精确、无颗粒的平涂渐变；那是矢量，不是 riso。
- 绝不在纸底上用粉色文字；粉滚筒管填色，蓝滚筒管写字。
- 绝不让错版出现在第二个标题上；一个词，其余安分。
- 绝不让双色调照片页连排；两次拉纸之间，滚筒需要一页自己的。

## 构建提示（Build hint）

```html
<link href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,400;7..72,500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: var(--display-weight); } h1 { line-height: 0.92; } h2 { line-height: 0.98; }
.misreg { position: relative; display: inline-block; isolation: isolate; }
.misreg::after { content: attr(data-text); position: absolute; inset: 0; z-index: -1; white-space: nowrap; pointer-events: none; color: var(--color-accent); transform: translate(2px, 3px); }
.overprint { background: var(--color-accent); mix-blend-mode: multiply; }
a { text-decoration-color: var(--color-accent); text-decoration-thickness: 2px; } a:hover { text-decoration-thickness: 4px; }
.btn { display: inline-flex; align-items: center; min-height: 48px; padding: 0 var(--space-lg); border: 1.5px solid transparent; border-radius: var(--radius-card); font: var(--display-weight) 0.9375rem/1 var(--font-display); transition: background-color var(--dur-short) var(--ease-out), transform var(--dur-micro) var(--ease-out); }
.btn:active { transform: translate(1px, 1px); }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.btn--secondary { border-color: var(--color-ink); color: var(--color-ink); }
.band--solid { background: var(--color-ink); color: var(--color-paper); }
.grained { position: relative; isolation: isolate; }
.grained::after { content: ""; position: absolute; inset: 0; z-index: 1; pointer-events: none; opacity: var(--texture-opacity); background-size: 200px 200px;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 9 -4'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E"); }
```
