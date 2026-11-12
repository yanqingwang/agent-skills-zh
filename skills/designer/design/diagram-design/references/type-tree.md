> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-tree.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 树 / 层级

**适用场景：** 组织架构、依赖树、分类法、文件树、决策拆解、技能树。要做"层级化的、可按 ID 寻址的块分解，且每块带 I/O、约束与实现可追溯性"时，先加载 [`semantic-patterns.md`](semantic-patterns.md) § Traceable block decomposition：它特化这个布局而不改变它。

## 布局约定
- 根在顶部，子节点向下展开（或根在左侧，子节点向右）。
- 节点是小号带标签矩形（`rx=6`），`node-name` 角色 12px 600 名称 + 可选 `sublabel` 角色 9px。宽 120–180px，高 40–52px。
- **连接线是正交的（拐弯式），绝不用斜线。** 父节点垂下一小段竖线，然后一条水平总线连接各兄弟，然后每个子节点再垂一小段竖线进入其顶边。1px muted 描边。
- 叶子指示：更细的描边（0.8）或不同的填充，或者让末端位置本身说明问题。
- 最大深度：4（根 + 3 层）。每层最大宽度：5。
- coral 只用于**一个**节点：根或关键叶子。不两者都用。
- 先画连接线，再画节点。

## 反模式
- 单页树超过 5 层深（不可读：拆分）。
- 节点宽度差异悬殊：最多选 2 种宽度。
- 斜的连接线。
- 跳层（父节点直接连到孙节点，中间无人）。
- coral 同时用在根和某片叶子上。

## 示例
- `assets/example-tree.html` — 极简浅色
- `assets/example-tree-dark.html` — 极简深色
- `assets/example-tree-full.html` — 完整编辑排版
