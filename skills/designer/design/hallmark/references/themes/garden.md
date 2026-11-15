---
name: Garden
slug: garden
genre: editorial
paper: light 95.8 90
display: roman-serif Vollkorn
accent: chromatic-green 140
posture: committed
keywords: farm, apiary, honey, cidery, orchard, pick your own, apples, seed, nursery, herbalist, botanical, tea, preserves, single-origin, seasonal, harvest, small-maker, csa, provenance, grown, field, homestead
material: 暖燕麦色纸张，深绿墨色，Vollkorn 600 旧式数字叠在 Hanken Grotesk 之上，发丝线与柔和的苔绿、陶土色调，日光下真色照片，唯一一抹叶绿
photo: natural con=6 sat=-6
pictured: Field Guide, Stage hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/garden.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Garden

种植者的语气：暖燕麦色纸张、近黑的绿墨、Vollkorn 标题与旧式数字叠在 Hanken Grotesk 之上、发丝线、柔和的苔绿与陶土色调、日光下的实景照片、唯一一抹叶绿。整体显得诚实而有季节感：每个中性色都偏绿，果实保留本色，没有任何东西被装盒、抛光或灰化。它不是鼠尾草配石板的养生页面，也不是奶油底色配赤陶点缀的书店。

## 令牌

```css
:root {
  --color-paper: oklch(95.8% 0.024 90); --color-paper-2: oklch(92.6% 0.030 90); --color-paper-3: oklch(89% 0.034 90);
  --color-ink: oklch(23% 0.050 152); --color-ink-2: oklch(33% 0.048 150); --color-muted: oklch(46% 0.034 142);
  --color-rule: oklch(83% 0.024 112); --color-rule-2: oklch(68% 0.042 138);
  --color-accent: oklch(46% 0.135 142); --color-accent-2: oklch(86% 0.075 128); --color-accent-ink: oklch(97% 0.015 95);
  --color-focus: oklch(46% 0.135 142); --tint-moss: oklch(46% 0.135 142 / 0.11); --tint-clay: oklch(54% 0.140 46 / 0.10);
  --font-display: "Vollkorn", ui-serif, Georgia, serif; --font-body: "Hanken Grotesk", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "Newsreader", ui-serif, Georgia, serif;
  --radius-card: 4px; --radius-pill: 999px; --rule-hair: 1px; --shadow-card: none;
  --tracking-display: -0.012em; --display-weight: 600;
}
```

## 字体

- **标题字：**Vollkorn 600，正体，句首大写，`--tracking-display`，行高 1.04；所有标题只用这一个字重，从不用斜体。稳固但不带 700 的粗厚，52px 的标题读起来是沉稳，不是喊叫。它的旧式数字是全主题最好的数字：英亩数或件数用 Vollkorn 排到 160px 以上，数字下探过基线，不需要任何其他配图。
- **正文字：**Hanken Grotesk 400 与 500，开启 `oldstyle-nums`；表格用等高的表列数字，展示数字保留 Vollkorn 的旧式风格。
- **照片下方的图注（例外字）：**Newsreader 400，标签字号，句首大写，用 `--color-muted`，一行一个事实，像苗圃的标牌。Vollkorn 从不作正文。
- **标签、表头、元信息、批号、日期：**Hanken Grotesk 500，小一档，句首大写，不加字距，用 `--color-muted`。页面上不用等宽字体。

## 表面

- 分隔线：1px `--color-rule` 发丝线分隔行与区块；`--color-rule-2` 用作表格顶线或控件描边。井格与照片圆角 4px，控件用胶囊形。
- 深度就是平面纸感：无阴影，无投影盒子；井格用 `--color-paper-2` 或色染，绝不做带边框的卡片。
- 色带：整幅的 `--tint-moss` 或 `--tint-clay` 薄染、`--color-paper-2`，或绿墨底配燕麦色文字（此时由 `--color-accent-2` 淡叶色充当强调色）；绝不做纯叶绿色块。一页最多两条。
- 照片：场所本季的样子，日光、真色：伸手可及的枝头果实、从草间看去的田垄、劳作中的手与筐、谷仓里的木箱；柔和阴天或低角度太阳，果实颜色绝不过饱和。4px 圆角，1px `--color-rule` 发丝线，无阴影。标题叠在照片上时，必须落在 40% 到 60% 的墨色遮罩上。
- 每个中性色都带绿或燕麦的偏色（色相 90 到 152），绝不用纯灰。无纹理。

## 适用手法

- **旧式数字大数字：**提示词给出的英亩数、品种数或罐数，用 Vollkorn 600 排到 160px 以上，三条一行架在发丝线上，每条下方一行 Hanken。
- **季节刻线带：**十二个月排成一行发丝线，开放月份落在苔绿色染上并标注当期事项，其余留纸色；其下用两栏行排出营业时间与地点。
- **价目表或产品清单：**纸-2 或绿墨底上的发丝线行，名称用条目级 Vollkorn，一条 Newsreader 说明，价格用等高数字靠右缘；缺失的信息保留带标签的占位符。
- **绿墨底宣言：**一句话，Vollkorn，区块级以上字号，燕麦色，动作词用淡叶色放在下方。

## 控件

- 一个平面的叶绿胶囊，配 `--color-accent-ink` 文字；旁边是一个用 `--color-rule-2` 描边的胶囊。
- 链接用墨色加下划线，悬停时下划线转为叶绿；输入框 4px 圆角，燕麦底上 1px `--color-muted` 边框。
- 叶绿占屏不超过 5%：主按钮、链接悬停、焦点环、一处大数字。陶土只出现在色染带里，绝不上控件、导航或标题。

## 动效

只做状态，`--dur-short` 配 `--ease-out`：胶囊加深一档，链接下划线生长。无入场动画、无错峰、无视差。

## 语气

温暖、诚实、有季节感、不慌不忙。只说提示词给出的田地、品种、月份、英亩数、罐数；绝不把"手作、精选、小批量"当作空洞徽章。

## 禁忌

- 绝不用灰鼠尾草色或石板色纸张；地面是暖燕麦，色相 92。
- 绝不用冷青色或企业翡翠绿；这里的绿是叶绿素，色相 140。
- 绝不用 Vollkorn 斜体或伪粗体；加载真正的 600，且同一页绝不与 700 混用。
- 陶土绝不上控件或标题，叶绿胶囊绝不用渐变。
- 绝不在白底上摆拍产品，也不做摆拍野餐；这是一个正在干活的地方。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Vollkorn:wght@600&family=Hanken+Grotesk:wght@400;500&family=Newsreader:opsz,wght@6..72,400&display=swap" rel="stylesheet">
```

```css
body { font-variant-numeric: oldstyle-nums; color: var(--color-ink-2); }
table, .num { font-variant-numeric: lining-nums tabular-nums; }
h1, h2, h3 { font-weight: var(--display-weight); color: var(--color-ink); }
.figure { font: 600 clamp(6rem, 12vw, 11rem)/0.86 var(--font-display); font-variant-numeric: oldstyle-nums proportional-nums; color: var(--color-ink); }
.btn { border-radius: var(--radius-pill); border: var(--rule-hair) solid var(--color-rule-2); padding: var(--space-sm) var(--space-lg); font-weight: 500; color: var(--color-ink); }
.btn--primary { background: var(--color-accent); border-color: var(--color-accent); color: var(--color-accent-ink); }
.band--moss { background: var(--tint-moss); }
.photo img { border-radius: var(--radius-card); outline: var(--rule-hair) solid var(--color-rule); outline-offset: -1px; }
.photo figcaption { font: 400 var(--text-sm)/1.4 var(--font-outlier); color: var(--color-muted); }
a:hover { text-decoration-color: var(--color-accent); }
::selection { background: color-mix(in oklab, var(--color-accent) 22%, transparent); }
```
