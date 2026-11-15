> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/dark-mode.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 深色模式：对等，绝不反相

只在用户要求双模式（"dark mode too"、"light and dark"）或预检发现需要尊重的既有模式系统时加载。深色主题（Midnight、Dusk、Kiln）不是双模式页面；本文件针对从同一 token 系统同时交付两种模式的页面。绝不在无人要求时自行产出双模式。

## 立场

深色模式是同一系统的第二次、同等投入设计的渲染：不是 `filter: invert()`，不是"把灰阶翻个面"。每个 token 都按配方重新推导；每个对比目标在两种模式下同等地成立；锚定色相绝不移动。某个 token 在重新推导后达不到它的对比配对时，修配方，绝不修要求。

## Token 重新推导（逐 token，从浅色值出发）

| Token | 深色推导 |
| --- | --- |
| `--color-paper` | L 12-18%，带锚定色调（chroma 0.008-0.015）。绝不用 `#000`。 |
| `--color-paper-2/3` | 抬升更亮：比 paper 每高一级 L +3%（浅色模式逐级变暗；深色模式逐级变亮）。 |
| `--color-ink` | L 92-96%，带锚定色调。绝不用 `#fff`。 |
| `--color-ink-2` / muted / neutral | 在新 paper 与 ink 之间重新排布 L 档位，让字排深度读起来均匀；保留每种 chroma 色调。 |
| `--color-rule` | L 约 26-34%；发丝线必须在深色底上存活（对照 paper-2 检查，不只对照 paper）。 |
| `--color-accent` | chroma -0.02 至 -0.04，L +5-10%（饱和的浅色强调色在深色下刺眼）。 |
| `--color-accent-ink` | 重新验证：在新强调色填充上正文 >= 4.5:1 / 大字 3:1。 |
| `--color-focus` | 遵循强调色的推导；环的对比对两种 paper 都达到 3:1 或更高。 |
| hue | 在任何 token 上都不随模式移动。 |

另加一个非 token 的动作：深色下正文字重减 50（400 降到 350）；深底亮字在视觉上偏重。

## 产出

`tokens.css` 原样保留浅色块，然后恰好两处新增：

```css
[data-mode="dark"] { /* only the tokens that move, re-derived per the table */ }

@media (prefers-color-scheme: dark) {
  :root:not([data-mode]) { /* the same overrides, for OS-preference auto mode */ }
}
```

按构造，`[data-mode]` 属性压过媒体查询（媒体块只在未设显式模式时生效）。切换：一个按钮设置 `document.documentElement.dataset.mode`，持久化到 `localStorage`，在首次绘制前由 4 行内联脚本读取，页面绝不闪现错误的模式。`:root` 上设 `color-scheme: light dark`，让表单控件与滚动条跟随。

## 深色纪律（会变化的规则）

- **阴影关闭。** 抬升靠亮度（+3% 阶梯）或内嵌发丝环（`box-shadow: inset 0 0 0 1px var(--color-rule)`）。深色上的投影读作光晕；光晕只在 atmospheric genre 的特例下合法（`genres/atmospheric.md` § Allowed here: two fixed blooms），那是主题行为，不是模式行为。
- **卡片比画布亮。** `paper` 上放 `paper-2`，永远如此；比底色更暗的卡片读作一个洞。
- **标题只有一种颜色。** 标题一律用 `--color-ink`；浅色下成立的逐标题变色，在深色下会散架。
- **图片。** 绝不对位图用 CSS `invert`/`brightness`。挑选在深色底上站得住的照片（库里的 `dark` 与 `mid` 色调），或把浅色图放进 `paper-2` 的凹槽里让它读作一块图版。主题的 multiply 图版（双色调处理、纹理）需要自己的深色配对；texture.md 记录了颗粒的覆盖层替换。
- **图表。** 数据标记像强调色一样重新推导（chroma 降，L 升）；网格线用深色的 `--color-rule`；见 data-viz.md § Dark。

## 验证

两种模式都跑完整的闸门清扫：对比闸门 40-41 在两种模式下对每一处配对（渲染层只看默认模式；深色配对用数值检查），闸门 7a 与 7b（不许纯黑或纯白）对深色块同样生效，stamp 记录 `modes: light+dark` 让日志知道。
