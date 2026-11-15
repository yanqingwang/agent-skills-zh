---
name: Terminal
slug: terminal
genre: atmospheric
paper: dark 12.5 150
display: mono Martian Mono
accent: chromatic-green 142
posture: committed
keywords: cli, terminal, shell, command-line, tui, self-hosted, open-source, binary, ssh, sysadmin, devops, homelab, install script, package manager, repl, dotfiles, developer tool, phosphor
material: 近黑偏绿的地面分三级明度，淡荧光墨色与一抹亮荧光信号色（自身另有暗色薄染），每个字形都是 Martian Mono，标题宽、正文窄，图片用页面自身的字形打印：照片渲染成取自产品文本的字符网格，暗格小、亮格满，随光标而动
photo: duotone paper accent con=20
pictured: Session, Split hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/terminal.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Terminal

页面就是终端表面，图片用文字打印。近黑偏绿的地面，淡荧光墨色，一抹亮荧光绿及其暗色薄染用于标记新增或选中，每个字形都是 Martian Mono：标题宽，正文窄。一幅图片被打印成取自产品文本的字符网格。整个页面读起来像住在 shell 里的人做出来的工具。它不是 CRT 复古装扮，也不是塞着终端截图的暗色产品页。

## 令牌

```css
:root {
  --color-paper: oklch(12.5% 0.012 150); --color-paper-2: oklch(16% 0.016 150); --color-paper-3: oklch(20.5% 0.022 150);
  --color-ink: oklch(94% 0.03 140); --color-ink-2: oklch(82% 0.05 142); --color-muted: oklch(64% 0.06 145);
  --color-rule: oklch(27% 0.028 148); --color-rule-2: oklch(38% 0.045 146);
  --color-accent: oklch(87% 0.2 142); --color-accent-ink: oklch(14% 0.02 150); --color-focus: oklch(87% 0.2 142);
  --color-accent-wash: oklch(23% 0.06 145);
  --glyph-0: oklch(30% 0.06 146); --glyph-1: oklch(38% 0.08 145); --glyph-2: oklch(47% 0.11 144); --glyph-3: oklch(57% 0.14 143);
  --glyph-4: oklch(67% 0.17 142); --glyph-5: oklch(77% 0.19 142); --glyph-6: oklch(86% 0.2 141); --glyph-7: oklch(94% 0.12 138);
  --font-display: "Martian Mono", ui-monospace, monospace; --font-body: var(--font-display); --font-outlier: var(--font-display);
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --shadow-card: none;
  --tracking-display: -0.02em; --display-weight: 500; --stretch-display: 112.5%; --stretch-body: 87.5%;
}
```

## 字体

- **每个字形都是 Martian Mono，**最多三个字重：400、500、700。展示 500 配 `--stretch-display`，行高 1.12，`h1` 最多 3.75rem，两三行排完。正文 400 配 `--stretch-body`，15 到 16px，行高 1.65。标签与元信息小一档，用 `--color-muted`，句首大写，不加字距。
- **数字**用宽而轻的形态对比窄正文：400 配 `--stretch-display`，从 `--text-display-s` 起，表列体，其下用 `--color-muted` 排单位或 `#` 注释。
- 提示符字形（`$`、`~ $`）用 `--color-muted`，只标记真实命令，且仅限于此；参考文档中的参数用强调色。
- Martian Mono 没有制表（box-drawing）或块状字形。图示用 `+ - |` 打出，字标（wordmark）印成字形图，确保没有任何回退字体混进一行。

## 表面

- 一个色相，一列明度坡：地面，会话或安装井格用 `--color-paper-2`，悬停与选中用 `--color-paper-3`。抬升表面用 1px `--color-rule` 边框，方正，绝不用阴影；`--color-rule-2` 是表头或 diff 文件头下方更实的一条线。
- 分隔线：区块、行、标签页之间用 1px `--color-rule`。
- **字形即图片：**黑底上轮廓强烈的图片，降为明度等级网格（约 130 列，格高约为格宽的 1.85 倍），画在 canvas 上，每个点亮格是产品文本按序取出的一个字符，用 `--glyph-0` 到 `--glyph-7`，暗格缩到 62% 大小；没有脚本时用静态 `<pre>` 代替。一页一到两幅，要大。
- 无法生成字形网格时，用一张照片顶替，按 `photo:` 双色调处理并加 1px `--color-rule` 边框：机器本身，绝不是显示界面的屏幕。
- 无扫描线、无光晕、无外壳边框、无标题栏、无红绿灯。

## 适用手法

- **对比呈现为 diff：**统一 diff 横跨十到十二列，`--- a/` 与 `+++ b/` 头行压在 `--color-rule-2` 线上，删除行用 `--color-muted` 且前缀 `-`，新增行用墨色落在 `--color-accent-wash` 上且前缀绿色 `+`，行号槽用 `--color-rule-2`。
- **数字如工具输出：**提示词的三到四个数字，展示级字号，宽而轻，由竖向分隔线分开，每个下方用 `# 注释` 标注，像 `wc` 或 `du` 打印出来的样子。
- **会话按尺寸呈现：**一个会话装在 `--color-paper-2` 井格里横跨八列以上，一次性打出，其输出点亮旁边的 `+ - |` 图示。
- **参考文档排成行：**一行一个命令，`--text-title` 字号，宽体，参数用强调色，说明在右侧，像 man page 的概要（synopsis）；或者一张主机、标志或退出码的表格。

## 控件

- 主按钮：强调色块配 `--color-accent-ink` 文字，方正。次按钮：1px `--color-ink-2` 边框。悬停与状态切换用 `steps(1)`。
- 安装行：`--color-paper-2` 井格带标签页（brew、cargo、curl），下划线用强调色，命令用 `--text-lg`，右缘一个 16px 复制图标，点击后变成强调色的对勾，停留 1.4s。
- 链接用 `--color-ink-2`，点状下划线，悬停转强调色；选中的行或标签页用 `--color-accent-wash`。

## 动效

状态处用阶梯，图片处保持鲜活：字形图从噪声中逐行显影约 1.5s，只播一次；光标之下其格子闪到强调色再落回。会话进入视口时自动打字一次。光标闪烁五次后停住。开启减少动效时直接显示每个最终状态。

## 语气

命令、标志、路径、退出码。陈述式且简短：只说命令名，不说形容词。

## 禁忌

- 绝不用比例字体，也绝不让回退字体的制表字形混入。
- 绝不引入第二色相：无琥珀、无青色，删除行也不用红。
- 绝不用圆角、胶囊或柔和卡片，绝不用浅色区块。
- 照片绝不多于一张，且只在无法生成字形时使用。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Martian+Mono:wdth,wght@75..112.5,400..700&display=swap" rel="stylesheet">
```

```css
body { font-stretch: var(--stretch-body); font-variant-numeric: tabular-nums; }
h1, h2, h3 { font-weight: var(--display-weight); font-stretch: var(--stretch-display); letter-spacing: var(--tracking-display); line-height: 1.12; }
.figure { font-weight: 400; font-stretch: var(--stretch-display); font-size: var(--text-display); line-height: 1; }
.art { position: relative; } .art canvas { position: absolute; inset: 0; }
.btn--primary { background: var(--color-accent); color: var(--color-accent-ink); border-radius: 0; transition: background-color var(--dur-micro) steps(1); }
.well { background: var(--color-paper-2); border: var(--rule-hair) solid var(--color-rule); }
.diff .add { background: var(--color-accent-wash); color: var(--color-ink); } .diff .add::before { content: "+"; color: var(--color-accent); }
.diff .del { color: var(--color-muted); } .diff .del::before { content: "-"; }
```

制作字形图：裁出主体，autocontrast（自动对比度），缩放到 `cols` 列、`round(cols * h / w / 1.85)` 行，把亮度量化为 0 到 8 级（0 为空白），再把各行作为字符串交付；canvas 依序从产品文本为每个点亮格取字形，其颜色取自 `--glyph-(level - 1)`。
