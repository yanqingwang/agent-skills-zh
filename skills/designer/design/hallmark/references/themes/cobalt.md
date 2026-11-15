---
name: Cobalt
slug: cobalt
genre: modern-minimal
paper: light 98.5 250
display: grotesk-sans Familjen Grotesk
accent: cool 256
posture: restrained
keywords: api, sdk, cli, dev tool, developer platform, docs, documentation, infrastructure, backend, database, observability, webhooks, events, type-safe, open source, ship, deploy, developer experience, technical
material: 冷调近白纸张、蓝灰墨色与细线、IBM Plex Sans 上压 Familjen Grotesk、8×16 单元格上的生成 ASCII 场、键帽与切角面板、石墨底上的 JetBrains Mono、一个电光钴蓝信号
photo: duotone graphite paper
pictured: Feature Ledger, Field hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/cobalt.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Cobalt

精确的技术腔调：冷调近白纸张划满细线、IBM Plex Sans 上压 Familjen Grotesk 标题，底面由字符构成，一片生成 ASCII 场吸附到 8×16 的单元格上，用钴蓝浓淡显示产品自己的流量。面板在两个对角切角，按钮是带真实底边的键帽，代码跑在石墨底上。它精确，因为每条边要么是细线要么是切口，每个字符都有含义；它不是深色开发者页面，也不是终端戏服。

## Tokens

```css
:root {
  --color-paper: oklch(98.6% 0.005 250); --color-paper-2: oklch(96.2% 0.008 252); --color-paper-3: oklch(93% 0.011 252);
  --color-ink: oklch(21% 0.028 262); --color-ink-2: oklch(36% 0.022 260); --color-muted: oklch(50% 0.018 258);
  --color-rule: oklch(90% 0.009 252); --color-rule-2: oklch(83% 0.012 252);
  --color-graphite: oklch(21% 0.024 262); --color-graphite-2: oklch(26.5% 0.026 262); --color-graphite-ink: oklch(93% 0.010 250); --color-graphite-muted: oklch(69% 0.022 256);
  --color-accent: oklch(52% 0.19 258); --color-accent-2: oklch(76% 0.13 254); --color-accent-wash: oklch(95% 0.028 256); --color-accent-ink: oklch(98.6% 0.005 250); --color-focus: oklch(52% 0.19 258);
  --color-accent-deep: oklch(43% 0.2 262); --color-accent-edge: oklch(39% 0.16 260);
  --color-glyph-1: oklch(89% 0.025 254); --color-glyph-2: oklch(81% 0.045 255); --color-glyph-3: oklch(70% 0.085 256); --color-glyph-4: oklch(60% 0.13 257);
  --color-graphite-glyph-1: oklch(33% 0.03 262); --color-graphite-glyph-2: oklch(41% 0.05 260); --color-graphite-glyph-3: oklch(53% 0.1 258);
  --color-key-face: oklch(99.4% 0.003 250); --color-key-edge: oklch(80% 0.016 254);
  --font-display: "Familjen Grotesk", system-ui, sans-serif; --font-body: "IBM Plex Sans", system-ui, sans-serif;
  --font-outlier: "JetBrains Mono", ui-monospace, monospace;
  --radius-card: 8px; --radius-input: 6px; --radius-pill: 999px;
  --cell-w: 8px; --cell-h: 16px; --cut: 8px; --cut-l: 16px;
  --rule-hair: 1px; --shadow-card: 0 1px 2px oklch(21% 0.028 262 / 0.06);
  --shadow-key: 0 3px 0 0 var(--color-key-edge), 0 6px 8px -4px oklch(21% 0.028 262 / 0.28), inset 0 1px 0 oklch(100% 0 0 / 0.9);
  --shadow-key-accent: 0 3px 0 0 var(--color-accent-edge), 0 6px 8px -4px oklch(30% 0.12 260 / 0.45), inset 0 1px 0 oklch(100% 0 0 / 0.22);
  --shadow-key-press: inset 0 1px 2px oklch(21% 0.028 262 / 0.14);
  --tracking-display: -0.028em; --display-weight: 600;
}
```

## 字体

- **展示字体：**标题与数字用 Familjen Grotesk 600，条目标题用 500，`--tracking-display`、行高 1.02、句首大写、tabular 数字；60px 以上的计数是最响的字。
- **正文：**IBM Plex Sans 400 与 500。
- **标签、表头、状态：**Familjen Grotesk 500 小一档，用 `--color-muted`。绝不用等宽。
- **代码与字符：**JetBrains Mono 用于代码、机器值和字符场；绝不做标签、标题或 chip。

## 表面

- 每个表面 1px `--color-rule` 收边，每行用细线分开；中性色偏向色相 250 到 260。
- 面板、chip 与输入域在两个对角切角：`@supports` 内用 `border-radius: var(--cut-l) 4px` 加 `corner-shape: bevel round bevel round`，小部件用 `--cut`，回退为普通 8px 与 6px 圆角。纵深靠 `--shadow-card` 和一档纸色；只有键帽有边。
- 底面是一块画布上的生成 ASCII 场，绝不是图片：按 8×16 单元格采样噪声映射到字符梯度，从 `--color-glyph-1` 到 `-4` 着色，最密的单元格用 `--color-accent-deep`，形状由产品自己的流量决定（一侧是原始请求，另一侧是已解析）。它垫在 hero 之后；一条分隔行与一块石墨面板（石墨字符浓淡）可以复现它，至多四处；无脚本时由单元格上的点阵顶替。
- 石墨是深色材料：`--color-graphite` 底、`--color-graphite-ink` 文字，选中行或头条用 `--color-graphite-2`，注释用 `--color-graphite-muted`。语法高亮用 `--color-accent-2`，绝不搞彩虹。每页色带至多两条，其中一条石墨。
- 照片罕用：至多一张，远处看真实系统，双色调，上面不压文字。

## Range

- **一张表就是 API：**通栏划线，机器值用等宽字，一行压在钴蓝淡洗色上。
- **一张映射图：**两块石墨面板，输入与输出，对应的行用细线直角弯相连。
- **时间线当标尺：**一条细线上标真实秒数，尝试是带缺口的刻度、状态用 Familjen 600 display 字号，等待是尺寸标注线，失败用错误色。
- **作用于 prompt 数字的可用控件：**结果是一个大数字，压在由五十个等宽单元格组成的量表上。

## 控件

- 键帽：键面按钮带 3px 底边，hover 抬起 1px、按下下沉；唯一的主按钮是一枚实心钴蓝键。选项是沉陷的 paper-3 托盘上的按键，选中的那枚呈按下态。
- 命令是一枚切角 chip，带一个能用的复制键。链接 hover 时出钴蓝下划线。输入框切角、`--color-muted` 边框、钴蓝焦点。
- 状态是一行字加一个图标，绝不是填充 chip。场之外，钴蓝保持在一屏 5% 以内。

## 动效

字符场以 30 fps 运行、带指针透镜，离屏即暂停；reduced motion 下呈现为一帧合成静帧。键帽移动用 `--dur-micro`；连接线画入一次。无回弹、无视差。

## 语气

陈述式、具体，像一份好的 changelog：事件、端点、状态码。不用炒作形容词。

## 禁止事项

- 绝不用暖调强调色、胶囊按钮或渐变按钮。
- 绝不无病呻吟：字符场映射的是产品真实拥有的流量或状态，最密的单元格上不压任何文字。
- 绝不造假代码：代码片段要么能编译要么有返回；prompt 里没有宿主时，调用 `example.com`。

## 构建提示

```html
<link href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@500;600&family=IBM+Plex+Sans:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-family: var(--font-display); font-weight: 600; letter-spacing: var(--tracking-display); color: var(--color-ink); } h3 { font-weight: 500; }
.key { border: var(--rule-hair) solid var(--color-rule-2); border-radius: var(--radius-input); padding: 0 var(--space-lg); min-height: 48px; background: var(--color-key-face); color: var(--color-ink); font: 500 var(--text-md)/1 var(--font-display); box-shadow: var(--shadow-key); transition: transform var(--dur-micro) var(--ease-out), box-shadow var(--dur-micro) var(--ease-out); }
.key:hover { transform: translateY(-1px); } .key:active { transform: translateY(3px); box-shadow: var(--shadow-key-press); }
.key--primary { background: var(--color-accent); border-color: var(--color-accent-edge); color: var(--color-accent-ink); box-shadow: var(--shadow-key-accent); }
.cut { border: var(--rule-hair) solid var(--color-rule); border-radius: var(--radius-card); background: var(--color-paper); }
@supports (corner-shape: bevel) { .cut { border-radius: var(--cut-l) 4px var(--cut-l) 4px; corner-shape: bevel round bevel round; } }
.graphite { background: var(--color-graphite); color: var(--color-graphite-ink); } .graphite .token { color: var(--color-accent-2); }
a { text-decoration-color: var(--color-rule-2); text-underline-offset: 0.2em; } a:hover { text-decoration-color: var(--color-accent); }
```
