---
name: Rim
slug: rim
genre: modern-minimal
paper: dark 9 75
display: grotesk-sans Switzer
accent: warm 45
posture: committed
keywords: space, satellite, earth observation, orbit, imagery, ground station, telemetry, hardware, schedule, utc, infrastructure, mission, sensor, monitoring, instrument, night, dark, measured
material: 暖黑纸张，暖米白墨色，Switzer 500 配 Geist Mono 用于所有度量值，方正的发丝线表面，正上方俯拍地球照片，橙色信号与天蓝次色
photo: natural sat=-20 con=10
pictured: Map / Diagram, Ledge hero
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/themes/rim.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Rim

夜间的仪器：暖黑纸张，暖米白墨色，每个标题用中等字重的 Switzer，每个度量数字用 Geist Mono，方正表面由发丝线分隔，一抹橙色信号与天蓝次色，地球以仪器的方式呈现：正上方俯视。它读起来精确，因为每条边都硬朗，每个时间都带时区。它不是星光与光晕的科幻发光页面，也不是霓虹仪表盘。

## 令牌

```css
:root {
  --color-paper: oklch(9% 0.008 75); --color-paper-2: oklch(12.5% 0.009 75); --color-paper-3: oklch(6.5% 0.007 75);
  --color-ink: oklch(94% 0.010 80); --color-ink-2: oklch(84% 0.011 80); --color-muted: oklch(68% 0.012 80); --color-muted-2: oklch(50% 0.010 80);
  --color-rule: oklch(25% 0.010 78); --color-rule-2: oklch(16% 0.009 78);
  --color-accent: oklch(72% 0.17 45); --color-accent-ink: oklch(10% 0.02 45); --color-accent-2: oklch(74% 0.12 250); --color-focus: oklch(78% 0.15 45);
  --font-display: "Switzer", ui-sans-serif, system-ui, sans-serif; --font-body: var(--font-display);
  --font-outlier: "Geist Mono", ui-monospace, monospace;
  --radius-card: 0; --radius-pill: 0; --rule-hair: 1px; --shadow-card: none;
  --tracking-display: -0.04em; --display-weight: 500;
}
```

两种配色，均为暗色，由 stamp 声明：`rim: night`（上面的区块）或 `rim: station`（海军蓝 `oklch(19% 0.055 262)`，分隔线 `oklch(32% 0.060 262)`，信号色换成冰蓝 `oklch(84% 0.10 200)` 与琥珀 `oklch(76% 0.14 55)`）。

## 字体

- **标题字：**Switzer 500，首屏标题用 `--tracking-display`，区块标题用 -0.03em，行高 1.02，句首大写，正体。中等字重，绝不用粗体；每个标题只用一种颜色。
- **正文字：**Switzer 400，16 到 17px，行高 1.55，用 `--color-ink-2`；标签、图注与表头用小一档的 500 与 `--color-muted`，句首大写，不加字距，绝不用等宽。
- **度量值（等宽即材质）：**Geist Mono 400，表列数字，用于每个时间、坐标、面积、价格与时长。时间永远带时区，默认 UTC。作为主角的度量值排在 `--text-display-s` 到 `--text-display`，字距 -0.03em，其单位或时区用一半字号与 `--color-muted`。等宽绝不排标题、标签或段落。

## 表面

- 分隔全靠发丝线：每个区块标题上方 1px `--color-rule`，井格四周与表头下方也是；行与行之间用 `--color-rule-2`。
- 一切零圆角；页面上没有任何圆形。深度只靠明度：`--color-paper-2` 抬升一个井格，`--color-paper-3` 下沉一个。无阴影、无玻璃、无模糊、无光晕。
- 井格或照片可以去掉边框，换成两个 12px 的角标：1px 的 L 形，用 `--color-muted`，位于对角，落在画框外侧一点。
- 色带：`--color-paper-2` 或 `--color-paper-3`，以发丝线镶边；一页最多两条，绝不用浅色带。
- 照片：正上方俯视的地球，清晰度以原始捕捉为准：一片田、一条海岸线、屋顶、河口，边缘到边缘锐利，无地平线、无天空、无星球轮廓。方形，1px 内缩墨环，8% 透明度。它的度量值（地点、过境时刻、交付）落在底部一条 78% 透明度的 `--color-paper` 横带上，用 Geist Mono 加时区。

## 适用手法

- **度量值作大数字：**两到四个真实量值，Geist Mono，展示级字号，横跨十二列，由竖向发丝线分隔，单位用一半字号的 muted：一个量程、一个时间窗、一个价格。
- **真实时间的图示：**一条水平 UTC 轴，发丝线加刻度，时间窗是 10px 天蓝色带，每个事件是一根 1px 信号色别针，时间用等宽字排在其旁；这是系统的图表，绝不是装饰。
- **已建成的产品：**订单或队列放在 `--color-paper-2` 井格上并配角标，字段用等宽，选中行落在 `--color-paper-3` 上带一个橙色方块。
- **刻线行与表单优先的收尾：**发丝线行，左侧 Switzer 标题，右侧一行说明；纸-2 上的表单，其值用等宽输入。

## 控件

- 成对出现：方形橙色实心主按钮配 `--color-accent-ink` 文字，旁边是 1px `--color-rule` 描边的方形次级按钮，都用 Switzer 500。
- 链接用墨色，悬停加下划线；输入框方正在 `--color-paper` 上，1px `--color-muted` 边框，需要度量的值用 Geist Mono 输入。
- 橙色标记动作与当前状态，天蓝标记第二状态或时间窗；其余不着色。

## 动效

稳定而精确：状态在 `--dur-short` 配 `--ease-out` 内切换；实时时间每分钟跳一次。无脉冲、无循环、无入场。

## 语气

克制而精确：地点、过境时刻、UTC 时间、以平方公里计的面积。不惊叹，不谈前沿。

## 禁忌

- 绝无任何圆形：无胶囊、无圆形头像、无圆角按钮或画框。
- 绝无裸时间；不带时区的 `09:30` 是主题在撒谎。
- 绝不用粗体标题；Switzer 500 就是上限，重量感由黑色地面承担。
- 绝不从太空看星球、绝无星野、绝无光晕、绝不绕地球画轨道线。

## 构建提示

```html
<link href="https://api.fontshare.com/v2/css?f[]=switzer@400,500&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
```

```css
h1, h2, h3 { font-weight: var(--display-weight); line-height: 1.02; }
h2 { letter-spacing: -0.03em; }
.measure { font-family: var(--font-outlier); font-variant-numeric: tabular-nums; }
.btn { border-radius: 0; padding: var(--space-sm) var(--space-md); border: var(--rule-hair) solid var(--color-rule); background: none; color: var(--color-ink); font-weight: 500; }
.btn--primary { background: var(--color-accent); border-color: var(--color-accent); color: var(--color-accent-ink); }
.well { position: relative; background: var(--color-paper-2); }
.photo { outline: var(--rule-hair) solid color-mix(in oklab, var(--color-ink) 8%, transparent); outline-offset: -1px; }
.ticks::before, .ticks::after { content: ""; position: absolute; width: 12px; height: 12px; border: 0 solid var(--color-muted); pointer-events: none; z-index: var(--z-raised); }
.ticks::before { top: calc(-1 * var(--space-xs)); left: calc(-1 * var(--space-xs)); border-width: 1px 0 0 1px; }
.ticks::after { right: calc(-1 * var(--space-xs)); bottom: calc(-1 * var(--space-xs)); border-width: 0 1px 1px 0; }
::selection { background: color-mix(in oklab, var(--color-accent) 35%, transparent); color: var(--color-ink); }
```
