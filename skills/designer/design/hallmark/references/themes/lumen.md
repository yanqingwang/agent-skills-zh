---
name: Lumen
slug: lumen
genre: atmospheric
paper: dark 12.5 290
display: roman-serif Instrument Serif
accent: warm 62
posture: restrained
keywords: inference, model, llm, ai tool, agent, voice, synthesis, api, gpu, serverless, runtime, tokens, latency, open models, developer, research lab, ml platform, dev tools, premium
material: 紫黑底色、近白墨色、Geist 与 Geist Mono 上压小写且大一号的 Instrument Serif 标题、细线 well、淡淡的制图网格、一个熔融黄铜信号色与一个玫瑰色动词
photo: duotone paper ink-2
pictured: Map / Diagram, Settled hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/lumen.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Lumen

一台夜里的控制台，带着文学腔：紫黑底色、近白墨色、Instrument Serif 全小写、比 Geist 大一档、细线 well，以及一个熔融黄铜信号色。冷的暗、暖的光：暖意只配给黄铜与一个玫瑰色动词，于是页面同时读起来像工程产物和一盏安静的灯。产品就是画面。它不是霓虹深色模式、黑底上的光球、发光物体、紫色海报，也不是衬线杂志。

## Tokens

```css
:root {
  --color-paper: oklch(12.5% 0.027 290); --color-paper-2: oklch(16% 0.03 290); --color-paper-3: oklch(20% 0.032 290);
  --color-ink: oklch(96% 0.01 300); --color-ink-2: oklch(85% 0.017 298); --color-muted: oklch(69% 0.026 295);
  --color-rule: oklch(27% 0.034 290); --color-rule-2: oklch(36% 0.04 292); --rule-blueprint: oklch(96% 0.01 300 / 0.05);
  --color-accent: oklch(80% 0.15 62); --color-accent-2: oklch(72% 0.15 12); --color-accent-ink: oklch(14% 0.028 290);
  --color-live: oklch(80% 0.13 155); --color-focus: oklch(80% 0.15 62);
  --font-display: "Instrument Serif", ui-serif, Georgia, serif; --font-body: "Geist", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "Geist Mono", ui-monospace, monospace;
  --radius-card: 10px; --radius-pill: 999px; --rule-hair: 1px;
  --shadow-card: 0 28px 64px -30px oklch(4% 0.02 290 / 0.8);
  --tracking-display: -0.015em; --display-weight: 400;
}
```

第二个变体 `day`：骨白 `oklch(97% 0.008 290)` 垫在 `oklch(18% 0.02 290)` 之下，靛蓝 `oklch(46% 0.24 268)` 信号色配骨白文字，动词用 `oklch(56% 0.16 18)`。stamp 写明变体（`lumen: night`）。

## 字体

- **展示字体：**Instrument Serif 400、正体、全小写、`--tracking-display`、行高 0.95 到 1.02。这个字体窄而细，所以放大一档使用：区块标题用 `--text-display-s`，hero 标题用上限甚至更大。小写是标题、导航、控件与标签的语域；正文保持句首大写，模型名才留得住。
- **正文：**Geist 400 与 500，凡出现数字处用 `tabular-nums`。
- **标签、题注、表头：**Geist 400 小一档，小写，不加字距，用 `--color-muted`。
- **读数与代码：**Geist Mono 400、13px、小写、不加字距：带单位的测量值、状态、模型 id、代码。等宽字是机器在说话，绝不是标签腔。
- **动词：**页面上唯一带强调色的词，只出现在 hero 标题里，永远是动词，用 `--color-accent-2` 加一条会画入的 1px 下划线（stamp `waive 38iii`）。

## 表面

- 细线做围合：well、行与输入框 1px `--color-rule`，控件边缘 `--color-rule-2`；表面 10px 圆角，控件与标签用胶囊。
- 纵深是 paper 到 paper-3 的明度一档；必须浮起的表面，用底色自己的黑把细线换成 `--shadow-card`。绝不辉光、绝不光晕、绝不彩色阴影。
- 色带：`--color-paper-2`，每页至多两条；不用强调色场域，night 页面绝不取骨白色带。
- 照片：至多一张，21:9 的一条，拍的是工作跑在其上的机器（一排机架的过道、布线、亮着的机架面板），用底色的紫印刷，10px 圆角加 1px 线，下方题注写出硬件名；上面不压标题。
- 纹理：制图网格，1px `--rule-blueprint` 线、48px 间距，只在一个 well 或色带内部，绝不垫在正文下（stamp `waive 47c`）。不用玻璃、不用模糊、不用生成的物件顶替产品。

## Range

- **把一条路径画成图：**真实系统用细线节点与连接线画：慢路径用 muted 等宽字，产品的路径用黄铜线，每个节点都是请求真实经过的一步。
- **产品自己的界面：**一个 well 内用细线分开请求与响应，小写 tab，下方状态用 Geist Mono 读数；或全尺寸的控制台屏幕，live 状态用 `--color-live`。
- **well 里的一张图表：**铺在制图网格上，变量用 `--color-ink-2` 半强度，产品保持不变的那一个东西画成黄铜线，坐标轴用等宽字。
- **数字或价目卡：**一个测量值用 Instrument Serif、display 字号，单位用等宽字；或价目排成细线行、tabular 数字，上方小写标题。

## 控件

- 控件对：实心黄铜胶囊、`--color-accent-ink` 文字，旁边 `--color-rule-2` 细线胶囊，都小写，44 到 48px。
- 链接 hover 时出黄铜下划线；输入框坐在色带内的 `--color-paper` 上，1px `--color-rule-2`，10px 圆角，黄铜焦点圈。
- 黄铜保持在一屏 5% 以内：主按钮填充、焦点圈、链接 hover、一行字或一个读数。玫瑰色属于动词；`--color-live` 只属于 live 状态。

## 动效

唯一一个显现：动词下划线在 `--dur-long` 内画入一次。其余只有状态：细线胶囊 hover 取 `--color-paper-2`，流式回答打字一次。无环境循环、无呼吸灯、无 stagger。

## 语气

工程感、平实、具体：模型、状态、单位、价格。小写标题读起来像实验记录本里的一行字，绝不卖萌。不用感叹号。

## 禁止事项

- 绝不画或生成光源：标题后与旁不出现光球、灯、圆环、光晕或发光物体。
- 绝不让紫爬升：紫色场域或紫到蓝的渐变，就是那种"生成感"。
- 绝不给名词上色，绝不要第二个强调词；一个动词，在 hero 里。
- 标题绝不句首大写式，标题绝不用普通区块字号；这个字体在那个字号下显得单薄。
- 绝不用暖底色或第三个暖色；黄铜与玫瑰动词承担全部暖意。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif&family=Geist:wght@400;500&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
```

```css
body { font-variant-numeric: tabular-nums; }
h1, h2, h3, nav, label, th, figcaption, .btn { text-transform: lowercase; }
h1, h2, h3 { font-weight: 400; } h2 { font-size: var(--text-display-s); line-height: 0.98; }
.verb { display: inline-block; color: var(--color-accent-2); }
.verb::after { content: ""; display: block; height: var(--rule-hair); background: currentColor; transform-origin: left; animation: draw var(--dur-long) var(--ease-out) both; }
@keyframes draw { from { transform: scaleX(0); } }
.btn { border-radius: var(--radius-pill); padding: var(--space-sm) var(--space-lg); font-weight: 500; }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.btn--secondary { box-shadow: inset 0 0 0 var(--rule-hair) var(--color-rule-2); color: var(--color-ink); }
.btn--secondary:hover { background: var(--color-paper-2); }
.well { background: var(--color-paper-2); border: var(--rule-hair) solid var(--color-rule); border-radius: var(--radius-card); }
.blueprint { background-image: linear-gradient(var(--rule-blueprint) 1px, transparent 1px), linear-gradient(90deg, var(--rule-blueprint) 1px, transparent 1px); background-size: 48px 48px; }
.readout { font: 400 0.8125rem/1.5 var(--font-outlier); color: var(--color-ink-2); }
```
