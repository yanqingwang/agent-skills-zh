> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-swimlane.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 泳道图

**适用场景：** 跨职能流程、RACI 式流转、供应商交接、多团队发布上线流程。

**不适用本类型：** 客户可见的部分与保持隐藏的部分放在同一张共享舞台网格上 → **服务蓝图**（`type-service-blueprint.md`）。蓝图没有箭头，阶段顺序本身就是先后次序。

## 布局约定
- 水平泳道（或垂直列），每个参与者/团队一条。每条泳道在左侧留白（或顶部）用 `eyebrow` 角色标签命名。
- 泳道分隔线：1px 细线。
- 流程步骤是矩形，放在执行该步骤的参与者所在泳道内；箭头表示流向。
- 交接（跨越泳道边界的箭头）是最重要的边：给引入最多耦合或延迟的那条交接考虑用 coral。
- 不要强求每条泳道步骤数相同；只有一步的泳道也没问题。

## 反模式
- 泳道没有标签。
- 一个步骤横跨两条泳道（选一个归属）。
- 箭头来回穿行，重排步骤，让流向大体走直线。

## 示例
- `assets/example-swimlane.html` — 极简浅色
- `assets/example-swimlane-dark.html` — 极简深色
- `assets/example-swimlane-full.html` — 完整编辑排版
