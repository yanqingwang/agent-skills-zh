> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-timeline.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 时间线

**适用场景：** 发布历史、项目里程碑、事故时间线、路线图、changelog 可视化。

## 布局约定
- 横贯中部的水平细线基线（`stroke-width=1`）。
- 在时间边界（季度、月份、冲刺）画刻度，日期标签置于其下方，用 `arrow-label` 角色。
- 事件：基线上的小实心圆（`r=4`）。标签上下交替排布以避免碰撞，用 1px 细线垂线连接到圆点。
- 重大里程碑：`accent` 圆（`r=6`）+ 加粗的 `node-name` 角色标签。
- 时间刻度必须诚实：间隔不相等，圆点间距就不要相等。不要为了美观假装线性等距。某个区域过密时，用可见的方式断开坐标轴。

## 反模式
- 时间上不等距的事件画成等距。
- 缺坐标轴标签（"这是什么单位？"）。
- 标签拥挤又没有垂直错位，无法辨读。

## 示例
- `assets/example-timeline.html` — 极简浅色
- `assets/example-timeline-dark.html` — 极简深色
- `assets/example-timeline-full.html` — 完整编辑排版
