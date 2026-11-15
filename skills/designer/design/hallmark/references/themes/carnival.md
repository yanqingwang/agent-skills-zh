---
name: Carnival
slug: carnival
genre: editorial
paper: light 92 50
display: display-heavy Big Shoulders Display
accent: chromatic-yellow 95
posture: full-palette
keywords: record label, podcast, comedy, indie, zine, poster, illustrator, games, hot sauce, merch, streetwear, cassette, vinyl, live show, festival, loud, maximalist, scrappy
material: 着色纸张、深暖墨色、Golos Text 上压 Big Shoulders Display 800 大写标题、海报级大字号、2px 线条、硬朗的 4px 墨色阴影、两个互相较劲的大面积强调色
photo: natural vib=20 con=10
pictured: Label and Ledger, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/carnival.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Carnival

一种喧闹的丝网印刷腔调：着色纸张、深暖墨色、Golos Text 上压 Big Shoulders Display 大写、硬朗的墨色阴影，以及两个互相较劲的强调色。每个表面都是硬边的平面填充，像钉在墙上的印刷品；照片凑得近、色彩热，用同样的方式装框。页面上最响亮的东西是海报字号大写呈现的事实，不是图片。它不是粉彩游乐场、软阴影应用，也不是复古戏服。

## Tokens

```css
:root {
  --color-paper: oklch(92% 0.045 50); --color-paper-2: oklch(88% 0.050 45); --color-paper-3: oklch(82% 0.060 40);
  --color-ink: oklch(18% 0.080 20); --color-ink-2: oklch(28% 0.060 25); --color-muted: oklch(42% 0.050 30);
  --color-rule: oklch(40% 0.21 25); --color-accent: oklch(86% 0.18 95); --color-accent-2: oklch(40% 0.21 25);
  --color-accent-ink: oklch(18% 0.080 20); --color-focus: oklch(40% 0.21 25);
  --font-display: "Big Shoulders Display", Impact, sans-serif; --font-body: "Golos Text", system-ui, sans-serif;
  --font-outlier: var(--font-body);
  --radius-card: 2px; --radius-pill: 2px; --rule-hair: 1px; --rule-bar: 2px; --shadow-card: 4px 4px 0 var(--color-ink);
  --tracking-display: 0.015em; --display-weight: 800;
}
```

只有一个旋钮：配色变体（drop），写进 stamp（`carnival: diner-sign`）；第二强调色同时充当线条色与焦点色。`paper-2` 与 `paper-3` 在纸张色相上分别加深 4 与 10 个点，`ink-2` 与 `muted` 以同样方式调亮墨色，且墨色压在每个第一强调色之上。

| 变体 | 适用 | Paper | Ink | Accent | Accent 2 |
| --- | --- | --- | --- | --- | --- |
| cold-snap（默认） | 音乐、冬天、磁带、黑胶 | 92% 0.045 50 | 18% 0.080 20 | 芥末黄 86% 0.18 95 | 牛血红 40% 0.21 25 |
| citrus-riot | zine、滑板、夏日系列 | 94% 0.040 85 | 20% 0.07 145 | 青柠 82% 0.20 130 | 品红 28% 0.28 350 |
| diner-sign | 餐饮、招待业、公路沿途 | 95% 0.035 90 | 16% 0.04 30 | 樱桃红 60% 0.22 25 | 藏青 30% 0.16 250 |
| studio-night | 电台、播客、蓝调时刻 | 88% 0.05 25 | 20% 0.05 270 | 青色 78% 0.18 220 | 李子紫 24% 0.18 320 |
| aqua-park | 夏天、泳池、冲浪、汽车旅馆 | 94% 0.040 180 | 20% 0.06 200 | 青绿 72% 0.16 195 | 珊瑚色 36% 0.24 35 |
| pressroom | 新闻、newsletter、评论 | 89% 0.025 65 | 16% 0.02 60 | 琥珀 78% 0.18 75 | 石板灰 34% 0.10 240 |

## 字体

- **展示字体：**Big Shoulders Display 800、大写、`--tracking-display`，可换行的标题行高 1.0；单独一词的 nowrap 行可用 -0.005em 与 0.9。这个字体很窄，所以比标准档位大一档使用：hero 标题在 1440 下可达约 160px，区块标题用 `--text-display-s`，条目标题用 `--text-2xl`。
- **正文：**Golos Text 400 与 500，句首大写（sentence case），全墨色。
- **标签、题注、表头：**Golos Text 500 小一档，句首大写。绝不用等宽。
- **数字：**卖点类事实（价格、销量、数量）用展示字体、hero 同级字号排版，等宽数字，单位在旁用同样的大写；小数字用 Golos Text 加 `tabular-nums`。

## 表面

- 两个互相较劲的强调色：一个填满一个表面，另一个填下一个，两者之间绝不渐变。
- 硬偏移阴影（`--shadow-card`，零模糊）用在 well、控件和照片上，绝不被 overflow 裁掉；除此之外任何东西都不制造纵深。
- 线条：区块与行之间用 `--color-accent-2` 的 `--rule-bar`，带阴影的表面四周用墨色；圆角至多 2px。
- 色带：任一强调色的一片场域（第二强调色上压纸张色文字），或 `--color-paper-2`；每页至多两条。
- 照片：事物本身，凑近，硬光或闪光，色彩推浓，一个主体占满画框：手里的瓶子、切开的水果、一张唱片套。照片带 `--rule-bar` 墨色边框加硬阴影，像贴上墙的印刷品，可以倾斜一两度；文字绝不压在照片上，但带事实的平面强调色块可以叠压一角。
- 纹理：墨色半调网点（`texture.md` § 2）用在 well 或色带上，绝不垫在正文之下，也绝不压在照片之上。

## Range

- **Figures** 铺满整片强调色场域：三四个事实用展示字体大写、海报字号，每个下面配一行 Golos，之间用 2px 墨色条分隔；半调网点放场域一角，绝不垫在数字下。
- **Rows** 用第二强调色的 `--rule-bar` 划线：左侧大写、条目标题字号的问题或名称，右侧 lead 字号的 Golos 答案；选中行反色为墨底纸张色文字。
- **Statements** 放在第二强调色上、压纸张色文字，那行字海报字号横跨十栏，旁边一个动作。
- **Forms** 做成硬阴影上的 well：选项是划线的行、选中即反色，实时总额用大写体呈现。

## 控件

- 按钮对：一枚第一强调色填充，旁边一枚纸张底、墨色描边的同款块，两者都带硬阴影、都用展示字体大写、不加字距。
- 链接用墨色、`--color-accent-2` 下划线；输入框在纸张底上加 `--rule-bar` 墨色边框、不带阴影。
- 第一强调色填充主控件、色带或 well；第二强调色承担线条、焦点、链接和另一种填充。

## 动效

基本静止。Hover 只换颜色，别的什么都不做；active 把偏移压到 1px；没有任何东西浮起。每页唯一可跑的循环是文字走马灯，8 秒一个周期或更慢。

## 语气

喧闹、短促、靠精确制造趣味：数量、价格、日期，每屏一个玩笑。标题用大写、六个词以内、以句号结尾；正文句首大写、现在时，数字优先于文字。

## 禁止事项

- 绝不软阴影；要么硬偏移，要么没有。
- 绝不把两个强调色放进同一表面；混色会毁掉双色腔调。
- 标题绝不用句首大写式（sentence case），字距绝不放松。
- 绝不用灰色或幽灵按钮；次级按钮就是描边墨色块。
- 绝不画吉祥物、火焰、骷髅或涂鸦；喧闹的东西要么拍出来，要么排成文字。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800&family=Golos+Text:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2 { font-family: var(--font-display); font-weight: 800; text-transform: uppercase; letter-spacing: var(--tracking-display); line-height: 1; }
.btn { border: var(--rule-bar) solid var(--color-ink); border-radius: var(--radius-pill); box-shadow: var(--shadow-card); padding: var(--space-sm) var(--space-lg); background: var(--color-paper); color: var(--color-ink); font: 800 var(--text-lg)/1 var(--font-display); text-transform: uppercase; }
.btn--primary, .band--a { background: var(--color-accent); color: var(--color-accent-ink); }
.btn:active { box-shadow: 1px 1px 0 var(--color-ink); }
.well, .photo { border: var(--rule-bar) solid var(--color-ink); border-radius: var(--radius-card); box-shadow: var(--shadow-card); background: var(--color-paper-2); }
.band--b { background: var(--color-accent-2); color: var(--color-paper); }
.halftone { background-image: radial-gradient(var(--color-ink) 1.5px, transparent 1.5px); background-size: 12px 12px; }
```
