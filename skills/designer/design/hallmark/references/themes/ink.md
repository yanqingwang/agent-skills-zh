---
name: Ink
slug: ink
genre: editorial
paper: light 99.5 100
display: grotesk-sans Epilogue
accent: chromatic-teal 190
posture: restrained
keywords: library, lending, community, civic, notice board, catalogue, rota, volunteer, non-profit, neighbourhood, borrow, tools, repair, membership, events, local, competent, monochrome
material: white paper, a black with no hue, Epilogue 700 over Epilogue 400, hairline rules and state pills, one teal that means in
photo: muted
pictured: Catalogue, Settled hero
---

> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/themes/ink.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Ink

一张纯黑印刷的告示：白纸、无色相的黑，Epilogue 700 作标题、400 作一切阅读文字，发丝线，外加一个表示"在库/开放"的青绿。照片拍摄架上的物品，日光下压低色彩。它干练、本地、友善，像一个运转良好的社区服务台。它不是冷峻的企业单色页，也不是温暖的奶油色编辑页。

## Token（设计令牌）

```css
:root {
  --color-paper: oklch(99.5% 0.003 100); --color-paper-2: oklch(97% 0.004 100); --color-paper-3: oklch(94% 0.006 100);
  --color-ink: oklch(16% 0 0); --color-ink-2: oklch(28% 0 0); --color-muted: oklch(44% 0 0);
  --color-rule: oklch(89% 0.004 100); --color-rule-2: oklch(93.5% 0.003 100);
  --color-accent: oklch(50% 0.095 188); --color-accent-ink: oklch(99.5% 0.003 100); --color-accent-soft: oklch(93% 0.05 190); --color-accent-soft-ink: oklch(27% 0.045 190);
  --color-focus: oklch(50% 0.095 188);
  --font-display: "Epilogue", ui-sans-serif, system-ui, sans-serif; --font-body: var(--font-display);
  --font-outlier: "IBM Plex Mono", ui-monospace, monospace;
  --radius-card: 12px; --radius-pill: 999px; --rule-hair: 1px;
  --shadow-card: 0 20px 40px oklch(20% 0 0 / 0.16);
  --tracking-display: -0.04em; --display-weight: 700;
}
```

两种配色，都是浅色，写入 stamp（印记）：`ink: paper` 或 `ink: board`。

| 配色 | 底色与青绿 |
| --- | --- |
| `paper`（默认） | 上面的代码块：白、无色相的黑、50% 的青绿 |
| `board` | 公告板黄 `oklch(93% 0.10 95)`，横线用 `oklch(84% 0.10 92)`，墨色 `oklch(20% 0.02 80)`，青绿加深为 `oklch(46% 0.078 190)`；内嵌面板与标记转为白色 |

## 字体（Type）

- **展示字体：**Epilogue 700，`--tracking-display`，Hero 字号行高 1.0、以下 1.05，句首大写，正体；数字（计数、价格、钟点）用同样设置，比旁边的标题大一档。
- **正文：**Epilogue 400，16 至 17px，行高 1.55，用 `--color-ink-2`（白底上灰字容易疲劳）；行内名称、链接与标记用 600。
- **标签、图注、表头、元信息：**Epilogue 400，小一号，句首大写，不加字距；绝不用等宽字体。
- **Outlier 字体：**IBM Plex Mono 只用于代码和纵向比较的数字（借出次数、证卡号、值班时刻）。大数字与价格用 Epilogue 700 的墨色；青绿只标记在库或开放。

## 表面（Surfaces）

- 横线：列表或表格以 1px 的 `--color-ink` 起头，行间续用 `--color-rule` 发丝线；更安静的行用 `--color-rule-2` 分隔。
- 内嵌面板与照片圆角 12px，控件与输入框 10px，标记用胶囊。
- 平坦纸面：内嵌面板是 `--color-paper-2` 加 1px `--color-rule` 边缘；`--shadow-card` 只允许浮在页面之上的东西使用（菜单、对话框），静止的表面绝不使用。
- 色带：`--color-paper-2` 色带，或墨色色带配纸色文字。每页至多两条；绝无青绿色场。
- 照片：物品与共享它们的街道，平实日光、臂距拍摄：挂满工具的洞洞板、靠墙的梯子、抱着东西回家的邻居，只拍背影；没有正对镜头的脸，没有正对相机的品牌标。色彩压低（`photo:` 的 muted），青绿因此保持唯一有含义的颜色；12px 圆角，1px `--color-rule` 发丝线，无阴影。物品的名称与状态标记放在照片下方，绝不压在照片上。
- 无纹理。

## 版式（Range）

- **架子排成划线列表：**每件物品一行，压在墨线之下，名称用 600 字重，一句话说明它是什么，状态胶囊放在行尾，过滤框随输入收窄行数。
- **步骤排成告示：**使用方法分三四段编号，横跨各列，每个数字用 Epilogue 700 排展示字号、压在发丝线之上，表示"在库"的阶段带浅青绿胶囊。
- **开放日时刻表：**接下来的日期排成行，各配钟点，最近的一次用墨色标出；日期取自系统时钟，绝不手填。
- **纯黑大数字：**计数、费用与钟点用 Epilogue 700 排大，放在 `--color-paper-2` 内嵌面板上，表示"开放"的那个用青绿。

## 控件（Controls）

- 控件对：墨色填充按钮配纸色文字，旁边是 1px `--color-rule` 边框的按钮、底 `--color-paper-2`；两者都 10px 圆角、Epilogue 600。
- 标记只承载状态，别无他用：在库用浅青绿（`--color-accent-soft`）配 `--color-accent-soft-ink`，已借出用线色描边，使用中用墨色填充。
- 青绿表示在库或开放：一个标记、一个大数字、链接悬停、焦点环。链接用 600 字重的墨色、带下划线，悬停转青绿。

## 动效（Motion）

除状态外皆不动：过滤随输入生效，标记点击即切换状态，下划线在 `--dur-micro` 内转青绿。无跑马灯，无显现动效，无计数动画。

## 语气（Voice）

服务台志愿者的话：什么东西在库、何时归还、周六谁值班。短、友善、准确，绝无官腔。

## 禁止事项（Do-nots）

- 绝无第二种颜色：青绿表示在库，借出用描边表示，绝不用红色。
- 绝不用偏暖的黑。墨色没有色相，页面也这样声明：`waive 22 · ink and greys at zero chroma · a notice board is printed in plain black`。
- 绝无青绿色场或青绿正文；青绿是状态，不是表面。
- 绝无静止阴影；纸面保持平坦。

## 构建提示（Build hint）

```html
<link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@400;600;700&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: var(--display-weight); line-height: 1.02; }
.btn { border: var(--rule-hair) solid var(--color-rule); border-radius: 10px; padding: var(--space-sm) var(--space-md); font-weight: 600; background: var(--color-paper-2); color: var(--color-ink); }
.btn--primary { background: var(--color-ink); border-color: var(--color-ink); color: var(--color-paper); }
.tag { display: inline-flex; padding: var(--space-2xs) var(--space-sm); border-radius: var(--radius-pill); font-size: var(--text-xs); font-weight: 600; background: var(--color-paper-3); }
.tag--in { background: var(--color-accent-soft); color: var(--color-accent-soft-ink); }
.tag--out { background: transparent; box-shadow: inset 0 0 0 var(--rule-hair) var(--color-rule); color: var(--color-muted); }
.tag--on { background: var(--color-ink); color: var(--color-paper); }
.ruled { border-top: var(--rule-hair) solid var(--color-ink); } .ruled > * { border-bottom: var(--rule-hair) solid var(--color-rule); }
.well { background: var(--color-paper-2); border: var(--rule-hair) solid var(--color-rule); border-radius: var(--radius-card); }
.photo { border-radius: var(--radius-card); outline: var(--rule-hair) solid var(--color-rule); outline-offset: -1px; }
a { font-weight: 600; } a:hover { text-decoration-color: var(--color-accent); }
::selection { background: var(--color-accent-soft); color: var(--color-accent-soft-ink); }
```
