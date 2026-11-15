---
name: Studio
slug: studio
genre: editorial
paper: light 97.2 215
display: roman-serif Hedvig Letters Serif
accent: warm 52
posture: restrained
keywords: design studio, creative studio, branding, brand identity, art direction, agency, portfolio, case study, selected work, editorial design, typography, creative direction, graphic design, considered, curatorial
material: cool studio-white proof paper with an ink dot grid and grain, blue-black ink, Hedvig Letters Serif heads over Geist, crop marks on every printed piece, orange construction guides, the work photographed in true colour, one cadmium-orange signal
photo: natural
pictured: Portfolio Index, Ledge hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/studio.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Studio

一张设计工作室的打样纸，逮住搭建中途的样子：冷调工作室白纸、墨点网格与细颗粒、蓝黑墨色、Hedvig Letters Serif 作标题（一款当代衬线、接笔处带书法手迹）、干净的 Geist 正文、每件印出的作品四角带角线，以及一个既填满动作又画施工图的镉橙：字体度量参考线、留白框、红线标注。它读起来考究，因为字体正在被测量给你看。它不是带陶土色强调的暖奶油作品集，也不是灰色极简模板。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(97.2% 0.006 215); --color-paper-2: oklch(94% 0.009 215); --color-paper-3: oklch(90.5% 0.011 215); --color-paper-hi: oklch(99% 0.004 215);
  --color-ink: oklch(16% 0.032 250); --color-ink-2: oklch(34% 0.022 245); --color-muted: oklch(49% 0.018 240);
  --color-rule: oklch(84% 0.010 225);
  --color-accent: oklch(68% 0.172 50); --color-accent-ink: oklch(16% 0.032 250); --color-focus: oklch(52% 0.15 48);
  --color-dot: color-mix(in oklab, var(--color-ink) 20%, transparent); --color-mark: color-mix(in oklab, var(--color-ink) 72%, transparent);
  --font-display: "Hedvig Letters Serif", ui-serif, Georgia, serif; --font-body: "Geist", ui-sans-serif, system-ui, sans-serif;
  --font-outlier: "Sofia Sans Extra Condensed", "Arial Narrow", ui-sans-serif, sans-serif;
  --radius-card: 3px; --radius-pill: 3px; --rule-hair: 1px;
  --shadow-card: none;
  --shadow-sheet: 1px 2px 0 color-mix(in oklab, var(--color-ink) 7%, transparent), 10px 18px 36px -14px color-mix(in oklab, var(--color-ink) 32%, transparent);
  --tracking-display: -0.022em; --display-weight: 400;
}
```

## 字体（Type）

- **展示字体：**Hedvig Letters Serif 400，它唯一的字重，`--tracking-display`，行高 0.98 至 1.04，句首大写，`font-optical-sizing: auto`。书法手迹从 200px 的字标一直保持到 25px 的条目标题（那里字距 -0.005em）。只用于标题、数字与字标。
- **正文：**Geist 400 与 500，行高 1.55，行文用 ink-2。
- **标签、图注、辅助线读数：**Geist 500 小一档，句首大写，`--color-muted`，任何测量数字用表格数字。不用等宽字体。
- **字例字体：**Sofia Sans Extra Condensed 500，只出现在展示另一套系统的字例里；绝不做页面自己的标题或标签。

## 表面（Surfaces）

- 地面是生成的打样，绝不是图片：`feTurbulence` 颗粒（`--grain`）之上一层 24px 径向渐变墨点网格（`--color-dot`），铺在 Hero、导航与页脚上，蒙版淡出、在下一节开始前消失；页面其余是干净纸面。
- 每件印出的东西（一张纸、一张照片、一张卡、一个控件、聚焦的字段）四角带角线：八个 1px `--color-mark` 刻度，用背景渐变画在 `::before` 上，离角留一个小空隙，纸张上的更大。套准靶可以放在纸张两侧。
- 橙色画施工：1px `--color-accent` 辅助线标在字体的真实 ascender、大写字高、x 字高、基线与 descender 上，读数用标签语气；一个以 x 为单位的留白框；带尺寸的红线标注。只有线，绝无橙色文字。
- 两种线：行间 1px `--color-rule`；一组内容的开头 1px `--color-ink`。圆角 3px。
- 唯一的阴影，只给纸做的物体（一张卡、一张纸），从左上打光：`--shadow-sheet`。其余一律平放。
- 色带：paper-2，或一条墨色色带配纸色文字；绝不用橙色场。
- 照片：作品在它被使用的地方，水平、日光、垂直线笔直、真实色彩、带角线，旁边一条比例红线；绝不用样机。

## 版式（Range）

- **施工中的字标：**名字用 Hedvig 排到巨大，度量参考线、留白框与读数都在墨点网格上；指针以字体单位测量一个字母的字宽。
- **系统化作字例卡：**两三个备选方案做成带角线的卡（字体行、`Aa Gg Rr 0123456789`、hex 色样），按字体、颜色或网格切换一块展示板。
- **会展开的索引：**墨线之下的行，Hedvig 条目字号，每行展开成一个案例，其照片锁定在给定比例。
- **一次字号测试：**一行字逐级缩小（横幅、海报、票券），各自压在自己的橙色辅助线上，旁边是它的实时字号。

## 控件（Controls）

- 印出来的控件：1px 墨色边框、2px 圆角，内侧 2px 再嵌一条线，四角带角线、悬停时微微张开；主按钮橙色填充配墨色文字。Geist 500，48px。
- 字段：3px 圆角，1px `--color-muted` 边框，聚焦时出现角线。链接悬停出现橙色下划线。
- 橙色填色只给那一个动作；橙线是施工，可以多，但要细。

## 动效（Motion）

辅助线沿自身长度画入一次。在视野内时，一组系统可以每几秒轮换一次，一旦选择即停。状态变化时长 `--dur-short`、缓动 `--ease-out`。Reduced motion（减少动效）：整套施工图静止呈现。

## 语气（Voice）

克制而精确，略带文学气。动词优先于形容词；说出作品、机构、它所在的表面、那个度量。绝不说"创意解决方案"或"让品牌活起来"。

## 禁止事项（Do-nots）

- 绝不让 Hedvig 进入行文，绝不让字例字体走出字例。
- 绝不用橙色泛滥、橙色文字或第二种暖色。
- 绝不用暖调纸面；地面是冷调，色相 215。
- 绝不用与字体度量不符的辅助线，也绝不用不真实的尺寸。
- 绝不让墨点网格铺满整页或压在正文之下。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Hedvig+Letters+Serif:opsz@12..24&family=Geist:wght@400;500&family=Sofia+Sans+Extra+Condensed:wght@500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: var(--display-weight); letter-spacing: var(--tracking-display); color: var(--color-ink); font-optical-sizing: auto; line-height: 1.0; }
.proof { background-image: var(--grain), radial-gradient(circle at 1px 1px, var(--color-dot) 1px, transparent 1.4px); background-size: 160px 160px, 24px 24px; }
.crop { position: relative; --l: 8px; --o: 12px; }
.crop::before { content: ""; position: absolute; inset: calc(-1 * var(--o)); pointer-events: none; background: linear-gradient(var(--color-mark), var(--color-mark)) 0 var(--o) / var(--l) 1px no-repeat, linear-gradient(var(--color-mark), var(--color-mark)) var(--o) 0 / 1px var(--l) no-repeat; }
.btn { border: var(--rule-hair) solid var(--color-ink); border-radius: 2px; min-height: 48px; padding: 0 var(--space-lg); font-weight: 500; color: var(--color-ink); }
.btn::after { content: ""; position: absolute; inset: 2px; border: var(--rule-hair) solid var(--color-mark); }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.guide { height: var(--rule-hair); background: var(--color-accent); }
.set { border-top: var(--rule-hair) solid var(--color-ink); } .set > * { border-bottom: var(--rule-hair) solid var(--color-rule); }
```
