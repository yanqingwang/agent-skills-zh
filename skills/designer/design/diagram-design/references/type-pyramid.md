> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-pyramid.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 金字塔图 / 漏斗图

**适用场景：** 需求层级、优先级排序、价值金字塔、转化漏斗、内容重要性堆叠。

## 两种朝向：二选一
- **金字塔**（尖朝上）：窄的顶 = 最重要 / 最稀有 / 最有价值。底最宽 / 最基础。
- **漏斗**（尖朝下）：窄的一端 = 转化（最小的群体）。顶部最宽 / 受众。

一张图上不要混两种朝向。

## 布局约定
- 4–6 层。每层是一个由 4 个点构成的 SVG `<polygon>` 梯形。
- 层高一致（56–72px）。
- 宽度从底到顶（金字塔）或从顶到底（漏斗）线性递减。展示真实漏斗数据时，宽度必须诚实（与数量/百分比成比例）。
- 每层有：
  - **名称标签** 居中放在梯形内：`node-name` 角色，12–14px 600。
  - **副标签** 在名称下方或旁边：`sublabel` 角色，9–10px。
  - **侧注**（右或左）：可选。漏斗图把流失百分比放在这里（`−40%`）。
- 填充：细微的分级色调，或全部 paper-2 加发丝线分隔（更干净）。二选一。
- 描边：层与层之间 1px 发丝线；外轮廓 1px muted 或 ink。
- **coral 只用于一层**：金字塔的顶、漏斗的转化层，或关键瓶颈。
- 可选：左边距轴箭头 + `eyebrow` 角色标签（`rarer ↑`、`drop-off ↓`）。

## 反模式
- 7 层以上（不可读：压缩或拆分）。
- 非层级数据用金字塔（改用树或柱状图）。
- 不诚实的宽度（流失不均却画成等宽）。
- coral 用在底层（稀释"顶 = 稀有"的信号）。

## 示例
- `assets/example-pyramid.html` — 极简浅色
- `assets/example-pyramid-dark.html` — 极简深色
- `assets/example-pyramid-full.html` — 完整编辑排版
