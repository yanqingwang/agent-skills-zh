---
version: alpha
name: Pink Script (After Hours)
description: A nocturnal couture editorial system rendered in hot fuchsia ink on dim warm-black paper, with a soft film-grain overlay and a hairline interior frame. DM Serif Display carries every script and editorial moment at sizes up to 600px; Inter at weight 300 carries the body voice; JetBrains Mono carries the boutique-catalog metadata. The aesthetic borrows from glossy fashion magazine spreads, late-night perfume advertising, and the editorial pages of high-end zines — closer to a Maison's seasonal lookbook than a startup deck.

colors:
  ink-deep: "#060507"
  ink-violet: "#0F0D11"
  paper-blush: "#F5EDF1"
  pink: "#ED3D8C"
  pink-light: "#FF66A8"
  pink-deep: "#B81D67"
  line-pink: "rgba(237, 61, 140, 0.32)"
  mute-paper: "rgba(245, 237, 241, 0.55)"
  hair-paper: "rgba(245, 237, 241, 0.14)"

color-aliases:
  c-bg: ink-deep
  c-fg: paper-blush
  c-accent: pink
  c-line: line-pink

typography:
  script-huge:
    fontFamily: "DM Serif Display, serif"
    fontSize: 540px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.01em
    color: "{colors.pink}"
  script-section:
    fontFamily: "DM Serif Display, serif"
    fontSize: 600px
    fontWeight: 400
    lineHeight: 0.82
    letterSpacing: -0.02em
    color: "{colors.pink}"
  script-giant:
    fontFamily: "DM Serif Display, serif"
    fontSize: 360px
    fontWeight: 400
    lineHeight: 1.05
    color: "{colors.pink}"
  script-cover:
    fontFamily: "DM Serif Display, serif"
    fontSize: 280px
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: -0.015em
    color: "{colors.pink}"
  script-large:
    fontFamily: "DM Serif Display, serif"
    fontSize: 220px
    fontWeight: 400
    lineHeight: 1.04
    color: "{colors.pink}"
  script-med:
    fontFamily: "DM Serif Display, serif"
    fontSize: 156px
    fontWeight: 400
    lineHeight: 1.04
    color: "{colors.pink}"
  script-sm:
    fontFamily: "DM Serif Display, serif"
    fontSize: 132px
    fontWeight: 400
    lineHeight: 1.06
    color: "{colors.pink}"
  serif-cta:
    fontFamily: "DM Serif Display, serif"
    fontSize: 140px
    fontWeight: 400
    lineHeight: 1.04
    letterSpacing: -0.015em
    color: "{colors.paper-blush}"
  serif-h2:
    fontFamily: "DM Serif Display, serif"
    fontSize: 132px
    fontWeight: 400
    lineHeight: 1.06
    color: "{colors.paper-blush}"
  serif-quote:
    fontFamily: "DM Serif Display, serif"
    fontSize: 92px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.005em
    color: "{colors.paper-blush}"
  serif-chart-h:
    fontFamily: "DM Serif Display, serif"
    fontSize: 90px
    fontWeight: 400
    lineHeight: 1.06
    color: "{colors.paper-blush}"
  serif-section-h:
    fontFamily: "DM Serif Display, serif"
    fontSize: 88px
    fontWeight: 400
    lineHeight: 1.06
    color: "{colors.paper-blush}"
  serif-stat:
    fontFamily: "DM Serif Display, serif"
    fontSize: 116px
    fontWeight: 400
    lineHeight: 0.9
    color: "{colors.pink}"
  serif-toc-num:
    fontFamily: "DM Serif Display, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.0
    color: "{colors.pink}"
  serif-toc-title:
    fontFamily: "DM Serif Display, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.05
    color: "{colors.paper-blush}"
  serif-quote-attr:
    fontFamily: "DM Serif Display, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.05
    color: "{colors.paper-blush}"
  serif-process-h:
    fontFamily: "DM Serif Display, serif"
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.05
    color: "{colors.paper-blush}"
  serif-matrix-label:
    fontFamily: "DM Serif Display, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    color: "{colors.paper-blush}"
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.55
    color: "{colors.paper-blush}"
  body-muted:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.5
    color: "{colors.mute-paper}"
  body-toc-desc:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.4
    color: "{colors.mute-paper}"
  mono-runner:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    letterSpacing: 0.14em
    textTransform: uppercase
  mono-kicker:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 22px
    fontWeight: 400
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.pink}"
  mono-label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 22px
    fontWeight: 400
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.paper-blush}"
  mono-cover-pre:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 28px
    fontWeight: 400
    letterSpacing: 0.42em
    textTransform: uppercase
    color: "{colors.paper-blush}"
  mono-pill:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 16px
    fontWeight: 400
    letterSpacing: 0.08em
    textTransform: uppercase

spacing:
  edge-x: 60px
  edge-top-chrome: 60px
  edge-bottom-chrome: 60px
  content-top: 140px
  content-bottom: 140px
  inner-frame-inset: 36px

canvas:
  width: 1920px
  height: 1080px

components:
  slide-surface:
    background: "radial-gradient(ellipse 90% 70% at 30% 30%, #1A1218 0%, #0A0709 55%, #050306 100%)"
    description: "Universal dark surface — radial ellipse from a slightly warmer #1A1218 in the upper-left fading to near-black in the lower-right. The off-center light source is part of the system's identity."
  film-grain:
    selector: ".slide::before"
    background: "fractalNoise SVG via data URI, baseFrequency=0.9, octaves=2"
    opacity: 0.08
    mixBlendMode: screen
    description: "Subtle film grain overlay on every slide via ::before. Opacity 0.08 with screen blend — barely visible but reads as photographic grain rather than digital flatness."
  hairline-frame:
    selector: ".slide::after"
    position: "absolute; inset: 36px"
    border: "1px solid {colors.hair-paper}"
    description: "1px paper-blush-at-14%-opacity interior frame inset 36px from each slide edge. Always present. Functions as the editorial border of the magazine page."
  runner:
    position: "absolute; top: 60px; left: 60px; right: 60px"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.14em
    textTransform: uppercase
    description: "Top metadata runner — brand name on left (colored pink), section / chapter tag on right (muted paper-blush)."
  footer:
    position: "absolute; bottom: 60px; left: 60px; right: 60px"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.14em
    textTransform: uppercase
    description: "Bottom metadata runner — source / confidentiality on left, page-position (e.g. '03 / 09') on right. Page-position has paper-blush base text with a pink ::em for the current number."
  pink-rule:
    height: 1px
    background: "{colors.pink}"
    opacity: 0.45
    description: "Hairline pink rule for soft section separators."
  hair-rule:
    height: 1px
    background: "{colors.paper-blush}"
    opacity: 0.25
    description: "Hairline paper rule for muted section separators."
  pink-glow:
    textShadow: "0 0 80px rgba(237, 61, 140, 0.18)"
    description: "Soft pink halo behind large script titles. Applied via text-shadow on hero serif text only."
  pink-glow-mega:
    textShadow: "0 0 120px rgba(237, 61, 140, 0.22)"
    description: "Stronger pink halo for section-divider mega numerals."
  callout-rail:
    borderLeft: "1px solid {colors.pink}"
    paddingLeft: 24px
    description: "Pink left rule with right-aligned content — used as a callout container beside a chart, beside a chapter explanation."
  matrix-cell:
    padding: "16px 24px"
    borderBottom: "1px solid {colors.line-pink}"
    fontFamily: "Inter, sans-serif"
    fontSize: 22px
    fontWeight: 300
    color: "{colors.paper-blush}"
    description: "Comparison matrix cell. Rows are separated by hairline pink-at-32% rules; columns are gap-separated, no vertical borders."
  matrix-cell-us:
    background: "rgba(237, 61, 140, 0.08)"
    description: "Highlighted matrix row variant — soft pink wash to mark the 'our' column."
  pill-outline:
    border: "1px solid {colors.pink}"
    color: "{colors.pink}"
    padding: "6px 14px"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 16px
    letterSpacing: 0.08em
    textTransform: uppercase
    description: "Hollow pink pill — 1px pink border with pink mono text. The default pill state."
  pill-solid:
    background: "{colors.pink}"
    color: "{colors.ink-deep}"
    border: "1px solid {colors.pink}"
    fontWeight: 500
    description: "Solid pink pill — pink fill, deep-ink text. Affirmative / featured state."
  pill-dim:
    borderColor: "{colors.hair-paper}"
    color: "{colors.mute-paper}"
    description: "Dim pill — muted paper border, muted paper text. The de-emphasized state."
  qr-tile:
    width: 180px
    height: 180px
    background: "{colors.paper-blush}"
    padding: 12px
    description: "QR-code container — solid paper-blush square with 12px white padding around the SVG QR. The only large light-surface element in the system."
  stat-row:
    display: "grid; columns: 240px 1fr"
    borderBottom: "1px solid {colors.hair-paper}"
    paddingBottom: 16px
    description: "Stat row pattern — large pink serif figure on the left (with a paper-blush superscript unit) paired with a mono label and Inter description on the right. Rows are separated by 1px paper hairline."
  callout-num:
    fontFamily: "DM Serif Display, serif"
    fontSize: 120px
    lineHeight: 0.9
    color: "{colors.pink}"
    description: "Chart callout number — large pink serif numeral with smaller paper-colored unit suffix."
  arrow-glyph:
    width: 24px
    height: 24px
    color: "{colors.pink}"
    description: "Small pink right-arrow SVG used between process steps."
---

> **中文汉化版** · 上游：[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 原文件：`skills/creator/slides/frontend-slides/bold-template-pack/templates/pink-script/design.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## Frontend Slides 固定舞台策略

当本设计系统被 `frontend-slides` Skill 使用时，请把最终演示文稿生成为**固定 1920×1080 舞台**，整体等比缩放以适配浏览器视口。演示文稿在所有屏幕（含手机）上都应保持 16:9 幻灯片画布；可以留黑边（letterbox）或留白边（pillarbox），但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后面描述的任何源模板响应式行为。如果后文说原模板是视口流式（viewport-fluid），那只当作源历史，不视为 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流式 CSS 实现，本策略同样适用。把这些数值当作要换算进 1920×1080 舞台坐标的设计比例，而不是生成文稿里实际生效的响应式规则。

最终输出请使用 `deck-stage.js` 或等效的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图，检查文字溢出与面板重叠。


## 概述

Pink Script 是一套**夜色高级时装编辑系统**，建立在单一氛围前提上：一块深暖黑表面，被左上方略暖的 #1A1218 椭圆照亮，向右下渐隐到近黑。偏轴光源读作影棚柔光箱扫到杂志跨页的一角。其上一层 8% 不透明度、screen 混合的细微胶片颗粒，添上深夜编辑摄影的颗粒感。表面里嵌一道 1px 细线内框（paper-blush 14% 不透明度，距每边内缩 36px），是每页的编辑边框。没有打光渐变、胶片颗粒、内框这三者，系统就塌成扁平深色 UI。

字体栈是刻意的三声部编辑搭配。**DM Serif Display** 承载每个编辑瞬间：脚本标题（被当作系统的 "pink script"）、衬线标题、统计数字、引文文字。它只跑字重 400，这款字面就一个字重，也正是系统的展示声部。衬线尺寸自由伸缩，从 32px（表格标签）一路到 600px（分节断口数字）。**Inter** 字重 300 承载每段正文、导语、描述、图注，极轻几何无衬线是系统平静的散文声部。**JetBrains Mono** 字重 400 承载每个标签、眉题、页码、坐标轴标记、跑马条、页脚串，始终全大写、至少 0.08em 正字距。

配色锚定在单一招牌上：深暖黑（`{colors.ink-deep}` — #060507）上的**热粉洋红**（`{colors.pink}` — #ED3D8C）。粉色就是整套编辑强调系统，它作脚本标题色、眉题色、图表线色、胶囊边框、paper-blush 标题里的行内 `<em>` 切换、标注数字、线色，以及英雄脚本标题背后柔和的光晕（text-shadow 辉光）。**Paper-blush**（`{colors.paper-blush}` — #F5EDF1）是次级文字色，用于编辑无衬线标题、段落文案，以及一切该读作墨而非高亮的瞬间。55% 不透明度的柔化 paper 处理次级文字，14% 的细线 paper 处理分隔与内框。

纵深由三层叠置机制建立：**偏轴径向渐变表面**（左上打光）、**细微胶片颗粒叠层**（8% 不透明度、screen 混合、添摄影纹理）、**英雄脚本标题上的粉色光晕 text-shadow**（柔和 80–120px 辉光，模拟大号霓虹饱和字在相纸上的漏光）。任何元素都没有投影，纵深是氛围的、摄影的，不是结构的。

**密度取向：偏疏，带一个英雄瞬间。** 一条超大脚本锚定页面、其余是宽裕负空间、点缀 2–4 个小编辑碎片（跑马条、眉题、一段、页脚）时，Pink Script 才显得优雅。英雄脚本占画布 60–70%、辅助文案安静绕在余下页边，是对的。把画布塞进多个等权区域会破掉深夜杂志感。例外是统计页（5 行统计并排）、比较矩阵（满网格表）、系统页（多面板），这些页按设计更密，因为编辑目的是查阅而非诗。流程页与目录页填得满，但始终有层级：一个巨型脚本头主导，较小的卡片行绕在下面。

**关键特征：**
- 深暖黑表面（`{components.slide-surface}`），由径向渐变椭圆从左上打光。
- 每页一层细微胶片颗粒（`{components.film-grain}`），不透明度 0.08、screen 混合。
- 1px paper-blush 内框（`{components.hairline-frame}`），距每边内缩 36px，每页都有。
- 热洋红粉（`{colors.pink}`）是唯一彩色强调，作脚本色、眉题色、线色、胶囊描边、行内强调、英雄脚本背后的柔光晕。
- DM Serif Display 承载每个编辑瞬间，尺寸从 32px 到 600px。没有第二款展示字面。
- Inter 字重 300 承载每段正文，极轻无衬线是系统的散文声部。
- JetBrains Mono 全大写、0.08em+ 字距承载每个标签、页码、跑马条串。
- 顶部跑马条与底部页脚外壳出现在每页，跑马条品牌文字是粉色，外壳里其余是柔化 paper-blush。
- 行内 `<em>` 元素把 paper-blush 衬线标题切成粉色，是系统的编辑强调机制。

## 颜色

### 调色板

- **深墨**（`{colors.ink-deep}` — #060507）：基底表面色。带一丝暖调的近黑。配上径向渐变，锚住深色编辑表面。
- **紫墨**（`{colors.ink-violet}` — #0F0D11）：略抬起的深、带紫调。保留的备选深色，可用但当前页型很少用。
- **Paper Blush**（`{colors.paper-blush}` — #F5EDF1）：带一丝粉底的暖米白。主编辑文字色、QR 片背景、次级高亮表面。读作纸而非纯白。
- **粉**（`{colors.pink}` — #ED3D8C）：热洋红。系统唯一彩色强调。用作脚本标题色、眉题色、行内 `<em>` 色、标注数字色、线色、图表线色、胶囊描边色，也是光晕 text-shadow 的源色。
- **浅粉**（`{colors.pink-light}` — #FF66A8）：更亮的粉。有定义，当前页型未用。
- **深粉**（`{colors.pink-deep}` — #B81D67）：更深的粉。有定义，当前页型未用。
- **线粉**（`{colors.line-pink}` — rgba(237,61,140,0.32)）：32% 不透明度的粉，用于表格行分隔与图表轴线。
- **柔 Paper**（`{colors.mute-paper}` — rgba(245,237,241,0.55)）：55% 的 paper-blush，用于柔化正文与元数据。
- **细 Paper**（`{colors.hair-paper}` — rgba(245,237,241,0.14)）：14% 的 paper-blush，用于内细线框、暗胶囊边框、目录行分隔。

### 默认值

- **默认页面表面**：`{components.slide-surface}`，打光的暖黑径向渐变。始终如此。
- **默认胶片颗粒**：`{components.film-grain}`，不透明度 0.08、screen 混合。不可省略。
- **默认内框**：`{components.hairline-frame}`，1px paper-blush 14%。不可省略。
- **默认主标题色**：英雄脚本瞬间用 `{colors.pink}`；该读作墨而非高亮的编辑标题用 `{colors.paper-blush}`。
- **默认正文色**：主文案 `{colors.paper-blush}`，柔化导语与描述 `{colors.mute-paper}`。
- **默认眉题色**：`{colors.pink}`。eyebrow 标签始终是粉。
- **默认标签 / 元数据色**：跑马条、页脚、元数据用 `{colors.mute-paper}`。
- **默认线 / 分隔色**：柔和粉线用 45% 不透明度的 `{colors.pink}`，柔化细线用 `{colors.hair-paper}`。
- **paper-blush 标题内默认强调机制**：用 `<em>` 包住，把那个词切到 `{colors.pink}`（font-style 保持直立）。
- **默认胶囊态**：描边（`{components.pill-outline}`），粉边框、粉文字。
- **默认图表系列**：主线粉实线，次线柔化 paper-blush 虚线。

粉是常规使用中唯一的彩色，其余粉变体（Pink Light、Pink Deep）保留。不要引入第二种彩色强调，Pink Script 的身份就是单色地粉。

## 排印

### 字族

系统加载三款网络字体：**DM Serif Display**（字重 400，仅 italic 0）承载从 32px 到 600px 的每个编辑 / 展示瞬间；**Inter**（字重 300、400、500、600）承载每段正文与导语；**JetBrains Mono**（字重 400、500）承载每个标签、跑马条、页脚、元数据串。

每款字面的情绪语域各自分明：
- DM Serif Display 读作**编辑、香水杂志、深夜高级时装**，笔画对比优雅，系统把一切该有文学或杂志排印感的瞬间交给它。
- Inter 字重 300 读作**平静、当代、中性优雅**，极轻字重贴合编辑调性又不与衬线抢。
- JetBrains Mono 读作**档案、精品目录、带版次号**，等宽全大写声部处理版次号、页位置、跑马条品牌文字、分节标签。

一条关键行内混排规则：**DM Serif Display 标题里的 `<em>` 元素切到 `{colors.pink}` 色**（font-style 归一为直立）。这是系统的主标题强调，paper-blush 衬线文字里的粉色墨。

第二条行内混排规则：**统计数字里的 `<sup>` 元素以约 36px 渲染成 `{colors.paper-blush}`**，带一点顶部内边距偏移，用于单位后缀（%、×、M）。

### 排印比例

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.script-section}` | 600px | DM Serif Display | 400 | 分节断口超大数字 |
| `{typography.script-huge}` | 540px | DM Serif Display | 400 | 特性展示位里的英雄脚本 |
| `{typography.script-giant}` | 360px | DM Serif Display | 400 | 大号编辑脚本标题 |
| `{typography.script-cover}` | 280px | DM Serif Display | 400 | 封面脚本标题 |
| `{typography.script-large}` | 220px | DM Serif Display | 400 | 目录主脚本 |
| `{typography.script-med}` | 156px | DM Serif Display | 400 | 流程页主标题 |
| `{typography.serif-cta}` | 140px | DM Serif Display | 400 | 收尾 CTA 标题（paper-blush 色） |
| `{typography.script-sm}` | 132px | DM Serif Display | 400 | 统计页标题、矩阵标题 |
| `{typography.serif-stat}` | 116px | DM Serif Display | 400 | 统计行数字 |
| `{typography.callout-num}` | 120px | DM Serif Display | 400 | 图表标注数字 |
| `{typography.serif-quote}` | 92px | DM Serif Display | 400 | 引文页正文 |
| `{typography.serif-chart-h}` | 90px | DM Serif Display | 400 | 图表页标题 |
| `{typography.serif-section-h}` | 88px | DM Serif Display | 400 | 分节断口辅助标题 |
| `{typography.serif-toc-num}` | 64px | DM Serif Display | 400 | 目录行数字 |
| `{typography.serif-toc-title}` | 56px | DM Serif Display | 400 | 目录行标题 |
| `{typography.serif-quote-attr}` | 48px | DM Serif Display | 400 | 引文署名 |
| `{typography.serif-process-h}` | 38px | DM Serif Display | 400 | 流程步骤标题 |
| `{typography.serif-matrix-label}` | 32px | DM Serif Display | 400 | 矩阵行标签 |
| `{typography.body}` | 24px | Inter | 300 | 标准正文段落 |
| `{typography.body-muted}` | 22px | Inter | 300 | 柔化导语与描述 |
| `{typography.body-toc-desc}` | 24px | Inter | 300 | 目录行描述 |
| `{typography.mono-runner}` | 24px | JetBrains Mono | 400 | 顶部跑马条与底部页脚 |
| `{typography.mono-kicker}` | 22px | JetBrains Mono | 400 | 粉色眉题 eyebrow |
| `{typography.mono-label}` | 22px | JetBrains Mono | 400 | 标准 paper-blush 标签 |
| `{typography.mono-cover-pre}` | 28px | JetBrains Mono | 400 | 封面引导行（0.42em 宽字距） |
| `{typography.mono-pill}` | 16px | JetBrains Mono | 400 | 胶囊文字 |

### 默认值

- **默认主内容标题**：`{typography.script-sm}`（132px），用于带强标题的内容瞬间。
- **默认封面 / 开场标题**：`{typography.script-cover}`（280px），封面脚本锁定。
- **默认分节断口超大数字**：`{typography.script-section}`（600px）。
- **默认正文段落**：`{typography.body}`（24px Inter 300）。
- **默认柔化导语 / 描述**：`{typography.body-muted}`（22px Inter 300，mute-paper 色）。
- **默认标签 / 眉题**：`{typography.mono-kicker}`（22px JetBrains Mono，粉）。
- **默认页脚 / 跑马条**：`{typography.mono-runner}`（24px JetBrains Mono）。
- **默认统计数字**：`{typography.serif-stat}`（116px），配 36px paper-blush `<sup>` 作单位。
- **任何展示元素默认字重**：400（DM Serif Display 只有一个字重）。
- **正文默认字重**：300。

拿不准时，标准式样是：22px 粉眉题 + 132–156px DM Serif Display 标题（需额外强调时把一个词包进 `<em>` 成粉）+ 22–24px Inter 300 段落、柔化 paper-blush。这三元素式样是系统最稳的节奏。

### 招牌处理

以下处理**只要用到对应元素类型就不可省略**：

- **每页都带径向渐变表面、胶片颗粒叠层，以及 1px paper-blush 内框。** 三者齐备。去掉任一个都会塌掉编辑杂志读感。
- **每个英雄脚本元素（280px 及以上）都带粉色光晕 text-shadow。** 英雄脚本用 `{components.pink-glow}`（80px 模糊），分节断口超大数字用 `{components.pink-glow-mega}`（120px 模糊）。光晕模拟霓虹饱和印刷的漏光。
- **每个脚本颜色都是 `{colors.pink}`。** 别种颜色的 DM Serif Display 不算"脚本"，会变成"衬线标题"。在本系统里，粉色正是区分脚本与标题的东西。
- **paper-blush 衬线标题可用 `<em>` 把一个词切成粉**，这是系统的标题强调机制。`<em>` 保持直立（font-style: normal）。
- **DM Serif Display 标题始终带 `padding-bottom: .1em`**（最大脚本用 `.12em`）。这补偿衬线下伸部，让视觉基线读起来对齐。
- **所有 JetBrains Mono 都全大写、至少 0.08em 正字距**（多数外壳与标签 0.12–0.18em，封面引导行 0.42em）。
- **正文始终是 Inter 字重 300。** 别种字重的 Inter 不是正文，换成 400 读作另一种调性。
- **眉题始终是 `{colors.pink}` 粉。** eyebrow 颜色不可商量。
- **跑马条左侧品牌文字始终粉，右侧元数据始终柔化 paper-blush。** 粉品牌文字是系统常驻的身份信号。
- **页位置页脚用 paper-blush 底文字配粉色 `<em>` 标当前数字。** 格式：`<span>03 / 09</span>`，其中 `03` 包进 `<em>` 渲染成粉。

### 排印原则

Pink Script 的节奏是**超大粉脚本 + paper-blush 衬线段落标题 + 柔化 Inter 散文 + 小号等宽编辑标签**。换掉任一声音（例如把脚本排成 Inter，或把正文排成 DM Serif）都会塌掉系统的编辑语域。衬线从 32px 到 600px 自由伸缩，按页面的英雄瞬间挑尺寸，不按固定比例。

斜体字形不用（DM Serif Display 确有斜体，但模板没加载）。`<em>` 标签被改作粉色换色开关。下划线不用。DM Serif Display 没有粗体字重，用粗 Inter 排正文会破掉平静的散文声部。

## 布局

### 画布系统

系统以**固定 1920×1080 画布**为目标，渲染在 `<deck-stage>` web component 内。所有尺寸像素固定，stage 负责等比缩放。

多数页用**绝对定位**配贴边元素。标准内容区是 `inset: 140px 60px 140px 60px`，顶部留 140px 给跑马条 + 标题区，底部留 140px 给页脚，左右 60px 页边距。

### 内边距与锚定

| 锚点 | 值 | 用途 |
|---|---|---|
| `edge-x` | 60px | 内容左右页边距 |
| `edge-top-chrome` | 60px | 跑马条外壳顶部内缩 |
| `edge-bottom-chrome` | 60px | 页脚外壳底部内缩 |
| `content-top` | 140px | 页正文内容顶部内缩（跑马条之下） |
| `content-bottom` | 140px | 页正文内容底部内缩（页脚之上） |
| `inner-frame-inset` | 36px | 细线内框内缩 |

### 外壳画框

每页带 **top runner**，顶部 60px / 两侧 60px，左侧品牌名（始终粉）、右侧分节 / 章节标签（柔化 paper-blush）。跑马条是 24px JetBrains Mono 全大写、0.14em 字距。

每页还带 **bottom footer**，底部 60px / 两侧 60px，通常左侧来源或保密串、右侧页位置标记。页位置用 paper-blush 底配粉色 `<em>` 标当前数字（如 `01 / 09`）。

**细线内框** 1px paper-blush 14% 落在每页 `inset: 36px`。它是杂志页的编辑边框，无条件存在。

## 纵深与层级

### 无 box-shadow，只有氛围纵深

系统在任何结构元素上**零 box-shadow 声明**。纵深来自三层氛围：

1. **径向渐变表面**（`{components.slide-surface}`），左上方暖深椭圆打光、向右下渐隐到近黑。造出影棚柔光箱扫到页面一角的印象。
2. **胶片颗粒叠层**（`{components.film-grain}`），8% 不透明度、screen 混合，给表面添摄影颗粒感。
3. **英雄脚本标题上的粉色光晕 text-shadow**，低 alpha 的粉色柔和 80–120px 模糊，模拟大号霓虹饱和字在相纸上的漏光。

### 卡片或面板上无投影

卡片、表格、面板不带阴影。系统的"卡片"式样是结构的而非抬升的：由一条边框或左线定义的区域，平躺在表面上。

### 细线作结构纵深

系统要分隔区域时用：
- 45% 不透明度的 1px 粉（`{components.pink-rule}`）作柔和粉线。
- 14% 的 1px paper-blush（`{components.hair-paper}`）作柔化细线分隔。
- 32% 的 1px 粉（`{colors.line-pink}`）作表格行分隔与图表轴线。

绝不用 2px 或更粗的线。绝不用粉与 paper 之外的彩色线。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0px | 卡片、面板、表格单元、QR 片、跑马条 / 页脚文字 |
| 999px | 无，这里的胶囊明确是矩形 |

系统在任何结构元素上**零 border-radius**。胶囊是 0 圆角矩形（尽管沿用 "pill" 命名）。唯一的圆元素是图表标注的小圆标记（标拐点的 SVG `<circle>`）。

### 边框粗细

- **1px 实 paper-blush 14%**：通用内细线框。
- **1px 实粉**（`{colors.pink}`）：胶囊描边。
- **1px 实粉 32%**（`{colors.line-pink}`）：表格分隔、图表轴。
- **1px 实 paper-blush 14%**：目录行分隔、页脚分隔。
- **全不透明度 1px 实粉**：标注轨左边框、流程页步骤顶边。
- **1px 虚线粉 18%**：图表网格线。

没有别的边框粗细。系统里任何地方都没有 2px、3px 或更粗的边框。

### 装饰元素类型

**英雄脚本标题**：220–600px 的粉色 DM Serif Display 标题，带光晕 text-shadow。用到它的任何页面的定义性瞬间。始终粉、始终带辉光、始终带 `padding-bottom: .1em` 补偿下伸部。

**paper-blush 衬线标题**：88–140px 的 paper-blush DM Serif Display 标题。用于该读作墨而非高亮的瞬间。可含 `<em>` 把一个词切成粉。

**粉眉题**：22px JetBrains Mono 全大写 eyebrow，`{colors.pink}` 色，放在标题上方。系统里粉与英雄脚本并立时最稳定的出现方式。

**等宽跑马条 / 页脚**：标准 JetBrains Mono 外壳，24px / 0.14em 字距。跑马条上品牌始终粉，其余柔化 paper-blush。

**粉线（`{components.pink-rule}`）**：45% 不透明度的 1px 粉。作柔和分隔。

**细线（`{components.hair-rule}`）**：14% 不透明度的 1px paper-blush。作柔化分隔与目录行分隔。

**标注轨（`{components.callout-rail}`）**：1px 粉左边框，右对齐内容配 padding-left 24px。作竖直标注容器，贴在图表旁或章节说明旁。

**统计行（`{components.stat-row}`）**：240px 衬线数字配一条等宽标签 + 一段 Inter 描述，与下一行由 1px paper 细线隔开。统计数字是粉，描述是柔化 paper-blush。

**胶囊（`{components.pill-outline}`、`{components.pill-solid}`、`{components.pill-dim}`）**：三种胶囊态，空心粉（默认）、实粉配深墨文字（肯定 / 精选）、暗细线（弱化）。全是 0 圆角矩形。

**QR 片（`{components.qr-tile}`）**：180×180 的 paper-blush 方块，12px 白内边距，内含 SVG QR。系统里唯一的大块浅表面元素，在 CTA 页上充当"票券"物件。

**图表标注**：120px 粉衬线数字，配 0.5em paper 色单位后缀，加一条小等宽标签与 22px 柔化 Inter 描述，由 1px 粉标注轨锚在图表右侧。

**图表线**：主系列 3px 实粉线，次系列 2px paper-blush 虚线。主线拐点带 9px 实粉圆、50% 不透明度的 18px 空心环，以及一条落到轴的竖向虚线。

**流程步骤**：一根竖列，由 1px 实粉顶边锚定，配 96px 粉衬线数字、38px paper-blush 衬线标题、一段 Inter 描述。步骤间 24px 间隙，由一枚小粉箭头字形连接。

**矩阵表**：4 列网格，首列是 32px paper-blush 衬线标签，表头行着粉色，"our column" 行以 `rgba(237, 61, 140, 0.08)` 着色标记。

## 该做与不该做

### 该做
- 给每页套径向渐变表面、胶片颗粒叠层、1px paper-blush 内框。三者都不可省略。
- 英雄脚本标题设 `{colors.pink}` 配光晕 text-shadow。辉光属于脚本身份的一部分。
- 每个编辑 / 展示瞬间都用 DM Serif Display。衬线是系统唯一的编辑字面，别换成第二款。
- 正文段落设 Inter 字重 300。极轻字重是系统平静的散文声部。
- 每个标签、页码、跑马条、页脚串都用 JetBrains Mono 全大写、至少 0.08em 字距。
- 在 paper-blush 衬线标题里用 `<em>` 把一个词切成粉，系统的主标题强调。
- 每个主标题上方放一条粉眉题。粉 eyebrow 是系统的编辑信号。
- 用粉色左线标注（`{components.callout-rail}`）把一个统计、标注或章节说明锚在图表或内容区右侧。
- 给每个 DM Serif Display 标题加 `padding-bottom: .1em`。衬线下伸部需要补偿。
- 页位置页脚用粉 `<em>` 标当前数字的式样：`<em>03</em> / 09`。

### 不该做
- 不要省掉胶片颗粒或内细线框。系统的编辑氛围靠这两者。
- 不要给任何面板或卡片用 box-shadow。纵深是氛围的，不是结构的。
- 不要引入第二种彩色强调。粉是唯一强调，加红、蓝、绿都会破掉系统。
- 不要把粉洋红当文字放在 paper-blush 表面上，对比反转，看着像排印错误。
- 不要用 DM Serif Display 排正文。衬线留给编辑瞬间，不留给段落。
- 不要用 Inter 排展示标题。无衬线是正文声部，不是标题声部。
- 不要给任何元素加圆角。卡片、胶囊、表格、QR 片，都是严格矩形。
- 不要给任何元素用模糊阴影。系统里唯一的"阴影"是英雄脚本上的粉色光晕 text-shadow，而那是辉光，不是投影。
- 不要用斜体字形。`<em>` 标签被改作粉色换色开关。
- 不要用多个等权区域挤满页面。一个英雄瞬间主导时系统才显得优雅。

## 响应式行为

系统以**固定 1920×1080 画布**为目标，渲染在 `<deck-stage>` web component 内。stage 负责等比缩放适配浏览器视口，画布内所有像素固定尺寸统一缩放。

### 放映行为
- 导航、缩放、放映外壳由 `<deck-stage>` 组件处理。
- 键盘、触屏、鼠标滚轮导航由 stage 管理。
- 画布恒定 1920×1080，与视口无关。

### 打印行为
打印导出取决于 deck-stage 组件的打印处理。粉色光晕 text-shadow 与胶片颗粒叠层在 PDF 导出里可能渲染不一致，别假定视觉对等，先测试。

## CJK 与国际化内容

### 推荐中文搭配

| 角色 | 拉丁字面 | 中文字面（推荐） | 字重 | 说明 |
|---|---|---|---|---|
| 脚本 / 展示（DM Serif Display） | DM Serif Display | **思源宋体 Noto Serif SC** | **900** | 深底上撑得住视觉分量的重衬线。默认选择。 |
| 展示备选（纤巧瞬间） | DM Serif Display | 站酷小薇体 ZCOOL XiaoWei | 400 | 高级时装式纤细展示字面，只在极大尺寸（400px+）下用，那里纤细才读作刻意。在典型标题尺寸（40–200px）的深底上太细。 |
| 正文（Inter 300） | Inter | Noto Serif SC（思源宋体） | 400 | 衬线正文让编辑语域与厚重展示保持一致。 |
| 标签 / 跑马条（JetBrains Mono 全大写加字距） | JetBrains Mono | Noto Sans SC | 400（别强给 CJK 套等宽） | |

### 混排策略

策略 A：把每个 token 的 `fontFamily` 扩展成拉丁字面之后跟中文字面。DM Serif Display token 变 `"DM Serif Display, 'Noto Serif SC', serif"` 且中文段设 `font-weight: 900`；Inter 正文 token 变 `"Inter, 'Noto Serif SC', system-ui, sans-serif"`；JetBrains Mono token 变 `"JetBrains Mono, 'Noto Sans SC', monospace"`。拉丁字形用原字面渲染，CJK 自动落下。

**关键**：中文文字用展示角色时，显式设 `font-weight: 900`。DM Serif Display 的"单字重"因是高对比展示衬线，看起来本就厚重，对应的中文厚重在 Noto Serif SC 的 900 字重，不在 400。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&family=Noto+Serif+SC:wght@400;500;700;900&family=Noto+Sans+SC:wght@400;500;700&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 设 0
- 文字变换：CJK 不用 uppercase
- 全角标点（，。：；！？「」（））
- 展示标题不加句号（中文排印惯例）
- 盘古之白（CJK 与拉丁之间加空格：`使用 Claude` 而非 `使用Claude`）
- 一句一款字体

### 本系统的美学提示

Pink Script（After Hours）是夜色高级时装系统，整个编辑身份都架在暗暖黑纸上、最大 600px 的热洋红粉 DM Serif Display 上。DM Serif Display 任何尺寸的视觉分量都很足：高对比笔画、衬线终端，以及能在深底上立住的排印质量。

推荐的中文对应是 **思源宋体 Noto Serif SC 字重 900**。它承载与 DM Serif Display 相同的视觉分量：粗衬线终端、足以在深表面上清晰读出的笔画密度，以及定义系统的编辑语域。展示瞬间字重 900 不可商量，任何更轻（400、500、哪怕 700）都会在粉辉光 + 深纸组合里视觉消失，破掉整条高级时装语域。

**站酷小薇体 ZCOOL XiaoWei** 是次选，适合极端纤巧读作刻意的瞬间：一条 400px+ 的引文、细线分节断口标题、封面最顶端的品牌字标。它单字重 400 配极端笔画对比，带另一种感觉：更盛装、更气若游丝、更像旧版 Vogue 而非现代时装编辑。多数展示工作选 Noto Serif SC 900，只有瞬间真是极大尺寸下的纤巧点缀时才取 XiaoWei。

粉色光晕 text-shadow（`{components.pink-glow}`，80–120px 模糊）无论选哪款展示字面，都完美迁移到汉字。**给每个粉色中文展示瞬间套同样的辉光**，霓虹漏光效果与文字无关，深夜杂志氛围能完整跨文字存活。

粉色（`{colors.pink}` — #ED3D8C）作为唯一彩色强调原样成立。行内 `<em>` 换色（paper-blush 标题里一个词成粉）干净迁移到中文，把一个汉字或一个短语包进 `<em>`，粉墨切换读起来完全一样。

**正文用 Inter 字重 300** 不能直接迁移。推荐正文字面是 Noto Serif SC 字重 400，它的高对比衬线笔画贴合系统整体高级时装语域。正文色保持 paper-blush（`{colors.paper-blush}`），极轻语域靠尺寸、paper-blush 色与 55% 不透明度的柔化导语达成，不靠字重。

JetBrains Mono 全大写加字距标签（跑马条品牌、页码、页脚外壳）迁移不到 CJK。纯拉丁外壳串（品牌名本身、`01 / 09` 之类版次号）保留 JetBrains Mono。中文外壳文字（右上分节 / 章节标签）用同样 24px 的 Noto Sans SC 400，字距归 0、不用 uppercase。

径向渐变表面、胶片颗粒叠层、1px paper-blush 内框，都与文字无关。粉辉光、眉题、标注轨、统计行式样、矩阵单元，全都原样迁移。

### 已知 CJK 缺口

DM Serif Display 的"单字重"有误导性：它是高对比展示衬线，任何尺寸都读起来视觉厚重。对等的中文厚重在 Noto Serif SC **字重 900**，不在 400；展示用 400 会让中文标题显得软塌，与粗粉标注脱节。系统靠尺寸建立层级在中文里仍成立，但必须把展示字重锁在 900 才能保住视觉分量。

ZCOOL XiaoWei 是唯一可 CDN 加载、在比例上捕捉到"高对比高级时装衬线"性格的中文字面，但它单字重 400 在本模板深底上的多数展示尺寸下太细。把 XiaoWei 当小众选项，别当默认。

## 迭代指南

1. 每张新页背景都是打光的径向渐变（`{components.slide-surface}`），配胶片颗粒与内细线框。三层一层都别跳。
2. 每条新英雄脚本标题都是 `{colors.pink}` 色的 DM Serif Display，配 80–120px 模糊的光晕 text-shadow。
3. 每条该读作墨（而非高亮）的新编辑标题都是 `{colors.paper-blush}` 色 DM Serif Display。用 `<em>` 把一个词切成粉。
4. 每段新正文都是 Inter 字重 300，paper-blush（全）或 mute-paper（柔化）。
5. 每个新标签、跑马条、页脚、元数据标记都是 JetBrains Mono 全大写、0.08em+ 字距。
6. 每个新眉题 eyebrow 都是粉。别把眉题渲染成别的颜色。
7. 每个新胶囊都是 0 圆角矩形。在描边（默认）、实色（肯定）、暗态（弱化）里挑。
8. 每张新表或矩阵都用 32% 粉的 1px 行分隔、不用竖边框。
9. 每张图表主线用 3px 实粉、次线用 2px paper-blush 虚线。不要引入第三种颜色。
10. 跑马条品牌文字始终粉，右侧元数据始终柔化 paper-blush。别对调。

## 已知缺口

- 系统依赖经 `deck-stage.js` 加载的 `<deck-stage>` web component。缺它，1920×1080 画布不会缩放，页会按原生像素尺寸渲染。
- 胶片颗粒叠层用带 `feTurbulence` 的 data-URI SVG。某些浏览器（较旧 Safari）会不一致地渲染噪声，或在 PDF 导出时跳过。
- DM Serif Display 只有字重 400。没有粗体或斜体变体可用，系统没有回退字重阶梯，只靠尺寸建立层级。
- 粉色光晕 text-shadow 用固定的 80px 与 120px 模糊值。视口缩得极小时辉光可能盖过文字，放得极大时辉光可能显弱。
- `{colors.pink-light}`、`{colors.pink-deep}`、`{colors.ink-violet}` token 有定义，当前页型里未启用。预留给未来变化。
- CTA 页里的 QR 片 SVG 是手工编码的 `<rect>` 图案，不编码真能扫的码。真 QR 码需外部生成。
- 图表线点与拐点标记是需手工计算的 SVG `<polyline>` 坐标。没有数据绑定层。
- 封面脚本锁定在第二行用 `padding-left: 180px` 造悬挂缩进效果。这是硬编码布局决策，不能推广到别的词长，很长的第二行可能破掉居中。
- 跑马条与页脚靠 `white-space: nowrap` 防止折行。极长的品牌名或页位置串可能溢出 60px 页边距。
- 矩阵的 `cell.us` 列高亮是硬编码的 `rgba(237, 61, 140, 0.08)` 铺色。给别的列着色需逐列加类。
