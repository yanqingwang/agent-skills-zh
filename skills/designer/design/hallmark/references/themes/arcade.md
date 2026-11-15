---
name: Arcade
slug: arcade
genre: playful
paper: dark 14 312
display: pixel Silkscreen and Bungee
accent: chromatic-ember 40
posture: full-palette
keywords: game, indie, game studio, launch party, demo night, hackathon, festival, meetup, retro, pixel, arcade, nostalgia, synth, lo-fi, toy, zine, club night, loud
material: 茄子色 CRT 底色、丁香白墨色、Chivo 上压 RGB 分离的 Bungee 大写、Silkscreen 数字、硬偏移阴影、ember 与 acid 信号色
photo: tint accent
pictured: Marquee Hero, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/arcade.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Arcade

深夜的街机柜：CRT 屏幕下的茄子色底、Chivo 上压 RGB 分离的 Bungee 大写、Silkscreen 数字、硬偏移阴影，还有两种喧闹的墨色像两个玩家轮流出招。照片像透过屏幕看进来，按主色着色。它靠颜色、字形、光与按压物理制造喧闹，绝不画道具；不是霓虹合成波海报，也不是像素游戏页。

## Tokens

```css
:root {
  --color-paper: oklch(14% 0.04 312); --color-paper-2: oklch(18.5% 0.042 312); --color-paper-3: oklch(23% 0.045 312);
  --color-ink: oklch(95% 0.014 315); --color-ink-2: oklch(87% 0.018 315); --color-muted: oklch(71% 0.024 315);
  --color-rule: oklch(34% 0.05 312);
  --color-accent: oklch(66% 0.215 40); --color-accent-2: oklch(88% 0.195 115); --color-accent-ink: oklch(14% 0.04 312);
  --color-focus: oklch(88% 0.195 115);
  --color-crt-r: oklch(63% 0.24 25); --color-crt-g: oklch(80% 0.25 140); --color-crt-b: oklch(60% 0.24 265); --color-crt-c: oklch(78% 0.14 200); --color-shade: oklch(8% 0.02 315);
  --font-display: "Bungee", "Impact", sans-serif; --font-body: "Chivo", ui-sans-serif, sans-serif; --font-outlier: "Silkscreen", monospace;
  --radius-card: 4px; --radius-pill: 0; --rule-hair: 1px; --rule-bar: 2px;
  --shadow-card: 6px 6px 0 var(--color-accent-2);
  --tracking-display: 0; --display-weight: 400;
}
```

两个旋钮，各自写进 stamp（`arcade: ember/grille`）。配色方案（主色压答色、置于底色之上）：`ember`（上面的块）、`sodium`（80% 0.165 72 压 60% 0.145 242，底 14% 0.030 300）或 `oxblood`（83% 0.150 90 压 58% 0.200 25，底 16% 0.028 330）。屏幕：`grille`（低透明度 1px 竖向 RGB 条纹）或 `mask`（3px 间距的三色点阵）。一页绝不混用两个。

## 字体

- **展示字体：**Bungee 400、大写、不加字距、行高 1.02，用于 h1、一句宣言和字标，每个不超过 28 个字符。它带 RGB 分离：`--color-crt-r` 向一侧偏 1 到 2px、`--color-crt-c` 向另一侧，零模糊，每屏一条分离线。
- **标题与正文：**Chivo；区块标题 900、-0.02em、行高 1，句首大写；散文 400、行高 1.6。
- **数字：**Silkscreen 700、不加字距、tabular，只在 40px 及以上使用（更小会糊），用两种墨色，单位在旁用 Chivo 700。Silkscreen 里绝不排单词，PM 这类单位除外。
- **标签：**Chivo 700 小一档，句首大写。

## 表面

- well 与一切可按压物用 `--rule-bar`，行之间用 `--color-rule` 的 `--rule-hair`；圆角 4px，标签与输入框方形。
- 纵深：可按压物上的零模糊 acid 偏移、well 的底色一档、光标行（一行填 ember、配 `--color-accent-ink` 文字，像选中的菜单行）用于列表里唯一要选中的那项。绝不模糊。
- 色带：屏幕层之下的 `--color-paper-2`，或一片 ember 场域配 `--color-accent-ink` 文字、无 RGB 分离。每页至多两条。
- 照片：从房间里看夜晚：握着摇杆的手、被下方光照亮的按键、玩家的背影，没有人面对镜头。着色、`--rule-bar` 边框、压屏幕层；大而少。
- 屏幕（`texture.md` § 4）：旋钮那一层加 `--color-shade` 扫描线，静态，用在色带、well 与照片上；绝不垫在正文下，绝不做外框。

## Range

- **数字当比分行：**prompt 的真实数字用 Silkscreen、`--text-display-s` 起步，ember 与 acid 交替，`--rule-bar` 竖线分隔，横跨十二栏。
- **双人对局对比：**两个 well 并排，一个以 ember 为基调、一个以 acid（顶栏与数字墨色），行在两者之间对应，服务两类受众或两个选项；墨色就是玩家，什么都不画。
- **时刻表或价目表当菜单：**Rows 里 Silkscreen 的时刻或价格对着 Chivo 900 标题，铺在细线上，一行光标行点亮 ember。
- **宣言与可用控件：**ember 场域上一行 display 字号的 Bungee；或按压面做成步进器，累计总数用 Silkscreen、display 字号。

## 控件

- 按压面：ember 填充、Chivo 700、`--rule-bar` 墨色边框加 acid 偏移，旁边一枚未填充的同款面。Hover 时远离阴影，active 时砸向阴影；步进器按钮就是同一按压面的方形版。
- 链接墨色、2px acid 下划线；输入框 52px、方形，`--color-muted` 的 `--rule-bar` 边框。
- 控件与数字里 ember 主导、acid 应答；绝不引入第三种墨色。

## 动效

按压物理用 `--dur-micro` 与 `--ease-out`。光标行以 `steps(1)` 点亮，无淡入；可点击的 display 行 RGB 分离可加宽 1px。

## 语气

投币机的平实，压过喧闹说出来：夜晚、钟点、门票价、机器。短句、动词开头，不怀旧。

## 禁止事项

- 绝不用品红配青做一对，绝不做星空；屏幕就是纹理。
- 绝不用软阴影、荧光辉光或按钮渐变。
- 绝不画精灵、摇杆、手柄或像素角色；夜晚是拍出来的。
- 绝不让着色照片一张挨一张：ember 图挨着 ember 图，就是一整面橙墙。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Bungee&family=Chivo:wght@400;700;900&family=Silkscreen:wght@700&display=swap" rel="stylesheet">
```

```css
h1, .display { font-family: var(--font-display); font-weight: 400; line-height: 1.02; text-transform: uppercase; text-shadow: -1.5px 0 0 var(--color-crt-r), 1.5px 0 0 var(--color-crt-c); }
h2, h3 { font-family: var(--font-body); font-weight: 900; letter-spacing: -0.02em; line-height: 1; }
.figure { font-family: var(--font-outlier); font-weight: 700; color: var(--color-accent-2); font-variant-numeric: tabular-nums; }
.btn { background: var(--color-accent); color: var(--color-accent-ink); border: var(--rule-bar) solid var(--color-ink); border-radius: var(--radius-card); padding: var(--space-sm) var(--space-lg); font-weight: 700;
  box-shadow: var(--shadow-card); transition: translate var(--dur-micro) var(--ease-out), box-shadow var(--dur-micro) var(--ease-out); }
.btn:active { translate: 3px 3px; box-shadow: 2px 2px 0 var(--color-accent-2); }
.btn--secondary { background: transparent; color: var(--color-ink); }
.row:hover, .row[aria-current] { background: var(--color-accent); color: var(--color-accent-ink); transition: background-color var(--dur-micro) steps(1); }
.well { background: var(--color-paper-2); border: var(--rule-bar) solid var(--color-rule); border-radius: var(--radius-card); }
.crt { position: relative; isolation: isolate; }
.crt::after { content: ""; position: absolute; inset: 0; pointer-events: none;
  background-image:
    repeating-linear-gradient(to right, color-mix(in oklab, var(--color-crt-r) 5%, transparent) 0 1px, color-mix(in oklab, var(--color-crt-g) 5%, transparent) 1px 2px, color-mix(in oklab, var(--color-crt-b) 5%, transparent) 2px 3px),
    repeating-linear-gradient(to bottom, transparent 0 2px, color-mix(in oklab, var(--color-shade) 16%, transparent) 2px 3px); }
```
