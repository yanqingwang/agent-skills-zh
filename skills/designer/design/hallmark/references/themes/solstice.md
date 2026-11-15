---
name: Solstice
slug: solstice
genre: editorial
paper: light 94 80
display: high-contrast-serif Yeseva One
accent: warm 24
posture: restrained
keywords: farm, orchard, cider, perry, winery, harvest, seasonal, food, almanac, produce, vineyard, calendar, market, craft drink, label, bottle, rural, slow, sun, midsummer
material: 奶油色纸张、暖棕墨色、Archivo 与 Archivo Narrow 上压 Yeseva One、金色细线与硬朗纸影、低照暖光照片、一个朱红色信号
photo: warm high=-12
pictured: Midsummer, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/solstice.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Solstice

年鉴式的温暖：奶油色纸张、暖棕墨色、Yeseva One 标题、正文用 Archivo、小字用 Archivo Narrow、金色细线负责划线、方形表面配硬纸影、傍晚低照光下的照片，以及一个朱红色信号。季节感与乡土感来自墨色、金色、一颗饱满的衬线和照片里的光线，绝不来自画出来的农产品。它不是农舍手写体页面，也不是奶油底陶土色模板。

## Tokens

```css
:root {
  --color-paper: oklch(94% 0.03 80); --color-paper-2: oklch(97% 0.02 85); --color-paper-3: oklch(89% 0.05 80);
  --color-ink: oklch(27% 0.05 50); --color-ink-2: oklch(36% 0.05 50); --color-muted: oklch(48% 0.06 55);
  --color-rule: oklch(84% 0.06 78);
  --color-accent: oklch(54% 0.20 24); --color-accent-ink: oklch(97% 0.02 85); --color-focus: oklch(54% 0.20 24);
  --color-gold: oklch(74% 0.14 75); --color-gold-2: oklch(84% 0.11 80); --color-slot: var(--color-gold);
  --font-display: "Yeseva One", ui-serif, Georgia, serif; --font-body: "Archivo", ui-sans-serif, sans-serif;
  --font-outlier: "Archivo Narrow", ui-sans-serif, sans-serif;
  --radius-card: 0; --radius-pill: 999px; --rule-hair: 1px; --rule-bar: 2px;
  --shadow-card: 10px 10px 0 var(--color-paper-3);
  --tracking-display: -0.005em; --display-weight: 400;
}
```

信号色是色相 24 的朱红，一种带暖意的红，与金色、棕色相处融洽，绝不是陶土色；金色只划线，绝不填充。三种光线，写进 stamp（`solstice: long-light`）。

| 光线 | 纸与墨 | 信号与金 |
| --- | --- | --- |
| `long-light`（默认） | 奶油色 `oklch(94% 0.03 80)` 垫在棕色 `oklch(27% 0.05 50)` 之下 | 朱红 `oklch(54% 0.20 24)`，金色 `oklch(74% 0.14 75)` |
| `dusk` | 奶油色墨色垫在李子棕 `oklch(27% 0.05 40)` 之下；凸起 well 保持奶油色 | 朱红保持 `oklch(54% 0.20 24)` 配奶油色文字，金色 `oklch(78% 0.14 80)` |
| `midwinter` | 霜白 `oklch(95% 0.012 230)` 垫在冷棕 `oklch(28% 0.03 260)` 之下 | 朱红保持色相，金色变淡 `oklch(80% 0.06 230)` |

## 字体

- **展示字体：**Yeseva One 400、正体、行高 1.0、`--tracking-display`，每个标题只用一种颜色；大数字也用它。
- **正文：**Archivo 400 与 500，16 到 17px，行高 1.55，用 `--color-ink-2`。
- **小字：**Archivo Narrow 600、12.5 到 13.5px、句首大写、不加字距，是 outlier 字体，用于日期、月份、照片下的题注和坐标轴标签。元信息与表头：Archivo 500 小一档，句首大写。不用等宽。

## 表面

- 线条：区块顶部一条墨色 `--rule-bar`，行之间用 `--color-rule` 的 `--rule-hair`，well 内标题下一条金色细线。
- 除按钮对外处处方形：well、照片、输入框一律无圆角；按钮与步进器（stepper）用 `--radius-pill`。
- 纵深：凸起的 well 带 `--rule-bar` 墨色边框、内缩 6px 的 1px 金色线，以及硬朗的 `--shadow-card`（paper-3 色偏移、无模糊）；绝不软阴影。
- 色带：`--color-paper-2` 色带，或一条暖棕墨色带配奶油文字；每页至多两条，绝不做朱红大片。
- 照片：低角度晚光里的季节：枝头的果实、长草、室外桌上的杯子或瓶子、黄昏的果园；暖、微朦胧、影子长。方形，10% 的 1px 墨色细线，无阴影。题注在画框下方用小字，写一个事实（地点、月份、瓶子）；照片上的文字放在背光一侧，压在 40% 到 60% 的棕色压暗层上。
- 不用纹理：奶油色保持干净。

## Range

- **造出来的产品立在光里：**瓶子整高抠出，标签用真实排版呈现（名字用 Yeseva、品类用朱红小字、一条金色细线、批号），背景天空从奶油色渐入黄昏再到深色场域，瓶后一圈低暖光晕。
- **标签做成划线列表：**paper-2 的 well 内缩金色细线，事实排成行（风格、瓶型、批号、价格、发布），左侧小字标签、右侧 Yeseva 数值，中间点状金线。
- **一年排成一行：**从开花到装瓶的各季作为细线上的节点横跨棕色带，月份用金色小字，阶段用奶油色 Yeseva，当下那个用太阳的颜色标记。
- **会算数的下单：**一个胶囊步进器挨着唯一的朱红按钮，按钮标签上带累计数量，上方是 display 字号的宣言标题，底色从奶油色渐入黄昏。

## 控件

- 按钮对：朱红填充胶囊、Archivo Narrow 600、`--color-accent-ink` 文字，旁边一枚朴素的墨色文字按钮，压在 2px 墨色下划线上，无外框。
- 链接墨色下划线，hover 转朱红；输入框方形，`--color-paper-2` 底、1px 墨色边框。
- 克制：朱红只出现在主按钮、焦点圈和一个数字上，不足一屏的 5%；金色从不给文字上色。

## 动效

安静：标签页切换面板、某行在 hover 时点亮，时长 `--dur-short`、缓动 `--ease-out`。无显现动画、无计数器、无循环。

## 语气

年鉴的语气：日照的钟点、压榨的日子、果园的名字。绝不为美好生活举杯。

## 禁止事项

- 绝不引入第二个暖色；第二个橙色会让页面变成水果摊。
- 绝不用中性墨色；灰黑会杀死奶油色。
- 绝不用圆角卡片或软阴影；凸起的 well 是方形、划线、硬阴影的。
- 绝不用冷调或平光照片：蓝色正午天空或闪光会让奶油色发闷。
- 绝不用陶土色或赤陶色顶替朱红；色相一过 28，主题就变成每个生成器都会产出的那种"奶油色加衬线加陶土色"页面。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Yeseva+One&family=Archivo:wght@400;500&family=Archivo+Narrow:wght@600&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: 400; line-height: 1; }
.small, figcaption { font: 600 12.5px var(--font-outlier); color: var(--color-muted); }
.btn { display: inline-flex; padding: var(--space-md) var(--space-xl); border: 0; font: 600 var(--text-sm)/1 var(--font-outlier); background: var(--color-accent); color: var(--color-accent-ink); }
.btn--secondary { background: none; color: var(--color-ink); padding: var(--space-lg) 0 var(--space-xs); border-bottom: var(--rule-bar) solid var(--color-ink); }
.well { background: var(--color-paper-2); border: var(--rule-bar) solid var(--color-ink); outline: var(--rule-hair) solid var(--color-gold); outline-offset: -7px; box-shadow: var(--shadow-card); }
.band--ink { background: var(--color-ink); color: var(--color-paper); }
.photo img { outline: var(--rule-hair) solid color-mix(in oklab, var(--color-ink) 10%, transparent); outline-offset: -1px; }
a:hover { text-decoration-color: var(--color-accent); }
::selection { background: color-mix(in oklab, var(--color-gold) 40%, transparent); }
```
