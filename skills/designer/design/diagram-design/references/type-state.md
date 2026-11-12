> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-state.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 状态机

**适用场景：** 有限状态逻辑：订单状态、认证状态、连接生命周期、表单向导、任务队列状态；以及 [`Lifecycle phase map`](semantic-patterns.md#9-lifecycle-phase-map) 模式：当一个主体的推进、等待、重试、取消和结局就是故事本身时。

## 路由区分

- 动作之间按时间排序的消息，包括请求/消息生命周期 → 用 **Sequence**。
- 事件、守卫和合法迁移占主导的稠密迁移逻辑 → 用普通**状态机**。
- 一个主体穿过 4–5 个主要阶段、带独立的等待/恢复带与结局带 → 用 **Lifecycle phase map** 语义模式。

## 布局约定
- 状态是圆角矩形（`rx=8`），标签用 `node-name` 角色。
- **起点**：实心 ink 圆点（`r=6`）。**终点**：带环圆点（外环 `r=8` 轮廓，内实心 `r=5`）。
- 迁移：带标签的曲线箭头，标签用 `arrow-label` 角色，格式 `event [guard] / action`（用不到的部分可省略）。
- 自环从状态上方弯出。
- 沿主导流向定向（左→右或上→下）；出现交叉迁移时先重排。
- coral 用在读者应当注意的状态上：通常是错误状态，或"顺利完结"。

## 反模式
- 迁移数超过 状态数 × 2 → 很可能是两台状态机。
- "从任意状态"的迁移从每个状态各画一条：用单条标注代替（`* → Error on timeout`）。
- 迁移无标签（这个类型的全部意义就在于*什么触发了它*）。

## 示例
- `assets/example-state.html` — 极简浅色
- `assets/example-state-dark.html` — 极简深色
- `assets/example-state-full.html` — 完整编辑排版
- `assets/example-state-lifecycle.html` — 生命周期阶段图，极简浅色
- `assets/example-state-lifecycle-dark.html` — 生命周期阶段图，极简深色
- `assets/example-state-lifecycle-full.html` — 生命周期阶段图，完整编辑排版
