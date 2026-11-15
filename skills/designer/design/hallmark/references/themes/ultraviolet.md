---
name: Ultraviolet
slug: ultraviolet
genre: modern-minimal
paper: light 95 300
display: geometric-sans Outfit
accent: cool 290
posture: committed
keywords: music, audio, stems, remix, dj, producer, player, streaming, tempo, playlist, creator, app, consumer, lowercase, violet, sound, beats, recording studio
material: lavender paper or a violet-black night, Outfit set lowercase over Onest, hairline pills, one saturated violet in two strengths, photographs pulled into the violet
photo: tint accent con=10
pictured: Workbench, Stage hero, in the night colourway
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/ultraviolet.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Ultraviolet

单色颜料里的制作人工具：纸与墨取同一色相的浅染，一种饱和紫以两档深浅出现，Outfit 以小写排每个标题与控件，处处胶囊形，深度收在发丝线内，照片被拉进紫色里。它读起来快、准、年轻，却不提高嗓门。它不是紫渐变创业页，也不是霓虹夜店传单。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(95% 0.02 300); --color-paper-2: oklch(92% 0.03 300); --color-paper-3: oklch(89% 0.035 300);
  --color-ink: oklch(18% 0.02 300); --color-ink-2: oklch(28% 0.03 300); --color-muted: oklch(46% 0.05 300);
  --color-rule: oklch(84% 0.04 300); --color-rule-2: oklch(70% 0.08 295);
  --color-accent: oklch(50% 0.25 290); --color-accent-deep: oklch(43% 0.22 290); --color-accent-soft: oklch(86% 0.08 295);
  --color-accent-ink: oklch(97% 0.01 300); --color-focus: oklch(50% 0.25 290);
  --font-display: "Outfit", ui-sans-serif, system-ui, sans-serif; --font-body: "Onest", ui-sans-serif, sans-serif;
  --font-outlier: "JetBrains Mono", ui-monospace, monospace;
  --radius-card: 16px; --radius-pill: 999px; --rule-hair: 1px;
  --shadow-card: 0 1px 2px oklch(18% 0.02 300 / 0.06);
  --tracking-display: -0.03em; --display-weight: 500;
}
```

三种配色，每页设定一次，写入 stamp（印记）：`ultraviolet: lavender`。夜感提示词取 `night`，它可携带一条 `record` 配色的色带。

| 配色 | 纸、墨、强调色 |
| --- | --- |
| `lavender`（默认） | 上面的代码块 |
| `record` | 底 `oklch(50% 0.25 290)`，墨 `oklch(95% 0.02 300)`，强调色转为白色 `oklch(99% 0.005 300)`，其上压紫字，横线 `oklch(72% 0.14 292)` |
| `night` | 底 `oklch(14% 0.02 290)`，paper-2 `17.5% 0.025 290`，paper-3 `21% 0.03 290`，墨 `92% 0.04 300`，ink-2 `80% 0.05 300`，muted `68% 0.06 300`，横线 `28% 0.04 290`，rule-2 `44% 0.07 292`，强调色 `55% 0.25 290`，deep `48% 0.24 290`，soft `36% 0.09 293`，focus `62% 0.22 290` |

## 字体（Type）

- **展示字体：**Outfit 500，小写，`--tracking-display`，行高 1。小写就是材质：标题、导航链接、按钮与胶囊绝不含大写字母。
- **数字：**Outfit 300，`--text-display` 起步，单位以标签语气小写缀旁，表格数字；细几何数字是展示字体唯一变轻的地方。
- **正文：**Onest 400，句首大写，行高 1.55。正文是全页唯一出现大写字母的地方。
- **标签、图注、表头：**Outfit 500，小一号，小写，不加字距，用 `--color-muted`。等宽字体只出现在代码里。

## 表面（Surfaces）

- 发丝线：行间 1px `--color-rule`；胶囊与描边控件带 1.5px 的 `--color-rule-2`。卡片无边框；表面就是向 `--color-paper-2` 退一档。
- 圆角：一切控件与标记用 `--radius-pill`，表面、界面与照片 16px；没有直角。
- 深度：纸面无深度，凸起表面下只有耳语般的 `--shadow-card`。无模糊，无辉光，无渐变。
- 色带：`--color-paper-2` 色带、墨色色带，或 `record` 配色下的一条紫色色场；每页至多两条。
- 产品平放在 `--color-paper-2` 上或出血到边缘，绝不装进边框壳；波形是真实的线条绘制，已播放段用紫色，未播段用 `--color-accent-soft`。
- 照片：音乐周遭的夜（调音台上的手、台上的隔间、被舞台照亮的人群背影），染紫，16px 圆角，向内 1px 8% 墨色描边环；压在照片上的文字必须垫墨色蒙版。绝不以人脸为主角。无纹理。

## 版式（Range）

- **音轨即画面：**产品自己的波形横跨十到十二列，每行一条分轨（stem），压在发丝线下，上方一条小节标尺用标签语气；已播段紫色，其余用 soft。它独自撑起一个区块，无照片也无边框。
- **细体 Outfit 数字：**提示词的真实数字用 300 字重排展示字号，发丝线分隔，其中一个用紫色，单位以小写缀旁。
- **用途表：**横贯全宽的表格全用小写，用途排标题字号，所需分轨（stem）作小胶囊，一句话说明听到的内容；价目表沿用同样的行。
- **record 色场：**一条紫色色带，装一个真正可用的投放区或表单，白色胶囊是它唯一的填充。

## 控件（Controls）

- 紫色填充胶囊（`--color-accent` 底 `--color-accent-ink` 字，悬停转 `--color-accent-deep`），旁边是内嵌描边胶囊（1.5px 的 `--color-ink`）；两者都 Outfit 500 小写。紫色色场内，填充胶囊转为白底紫字。
- 链接悬停时下划线转紫；输入框是胶囊，带 1.5px `--color-rule-2` 内嵌环，聚焦转墨色。开关（solo、mute）是小胶囊，按下时紫色填充。
- 紫是一种颜料：一个填充控件、焦点环、链接悬停、进度填充、已播波形、一个数字。

## 动效（Motion）

快而干脆：胶囊的颜色过渡用 `--ease-out` 配 `--dur-micro`，开关切换时音轨变暗或点亮，加载时至多一次收尾，从已可见的默认态以 `--dur-long` 过渡。无旋转，无循环。

## 语气（Voice）

小写、短、准：分轨、小节、分钟、曲目数。说话像制作人，不像唱片公司。

## 禁止事项（Do-nots）

- 标题、导航链接、按钮里绝无大写字母。
- 绝无第二种彩色，照片里也一样；紫是唯一。
- 绝不用紫到粉的渐变、文字背后的网格光晕或辉光。
- 绝不用直角控件或 4px 圆角；Ultraviolet 是圆的。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;500&family=Onest:wght@400&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: 500; line-height: 1; text-transform: lowercase; letter-spacing: var(--tracking-display); }
.figure { font: 300 var(--text-display)/0.9 var(--font-display); font-variant-numeric: tabular-nums; }
.btn, .pill { display: inline-flex; align-items: center; border-radius: var(--radius-pill); font: 500 var(--text-sm)/1 var(--font-display); text-transform: lowercase; transition: background-color var(--dur-micro) var(--ease-out); }
.btn { min-height: 48px; padding: 0 var(--space-lg); } .pill { padding: var(--space-xs) var(--space-md); box-shadow: inset 0 0 0 1.5px var(--color-rule-2); }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); }
.btn--primary:hover { background: var(--color-accent-deep); }
.btn--secondary { box-shadow: inset 0 0 0 1.5px currentColor; color: inherit; }
.well { background: var(--color-paper-2); border-radius: var(--radius-card); }
.band--violet { background: var(--color-accent); color: var(--color-accent-ink); }
.wave__rest { fill: var(--color-accent-soft); } .wave__played { fill: var(--color-accent); }
::selection { background: color-mix(in oklab, var(--color-accent) 25%, transparent); }
```
