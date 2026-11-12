> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-kanban.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 看板

**适用场景：** 按状态给在制工作做快照：什么在排队，什么在推进，什么卡住了，哪里突破了 WIP 上限。这是一次*状态清点*，不是一条流：看板**完全没有连接线**。这正是它区别于泳道图（有泳道加一条穿过它们的流，交接是承重边）和流程图（有序步骤加方向性交接）的地方。如果图上任何地方需要箭头，它就不再是看板：改用泳道或流程。

## 布局约定

- **至多 5 列等宽竖列（240px），32px 侧沟。** 列背景 `ink @ 0.02`；列无边框。
- **每列的头部带：** 列名用 `node-name` 角色，12px，字重 600，左对齐。右侧对齐一个 **WIP 芯片**：矩形标签（`rx=2`，**绝不**做成胶囊），内放 `eyebrow` 角色 8px 的 `n/limit`；或在无上限的队列列/终结列上只放裸 `n`。每个在制列都必须写。头部带正下方一条横贯整列宽度的 `rule` 发丝线分隔。
- **卡片：** §6 的节点盒模式（[primitives-core.md](primitives-core.md#node-box--full-pattern)），`rx=6`，宽度为列宽减去两侧各 16px 内边距，高 56px，卡片间纵向间距 12px。内容：标题用 `node-name` 角色，12px，字重 600；下面一行 `sublabel` 角色 9px `muted` 的副标签写 `TICKET-ID · owner`（如 `AVA-214 · nadia`）。
- **绘制顺序：** 背景 → 列填充 → 头部文字 + WIP 芯片 → 头部细线 → 卡片（每张：盒、然后左 accent 条（若阻塞）、然后标题、然后副标签）→ 图例。

## 卡片状态：这个类型的语义词汇

每张卡片只以四种状态之一渲染。当看板上的卡片足以展示它们时，四种都要用上并写进文档：

| 状态 | 填充 | 描边 | 附加 |
|---|---|---|---|
| `default` | white | `ink` | — |
| `blocked` | `accent @ 0.05` | `accent`（全透明度）虚线 `4,4` | 卡片左缘 4px `accent` 条 |
| `waiting / external` | `ink @ 0.02` | `ink @ 0.20` 虚线 `4,3` | — |
| `done` | `ink @ 0.05` | `muted` | — |

这些状态直接映射 [style-guide.md](style-guide.md#node-type--treatment) 的节点处理表（`security` → blocked，`optional` → waiting/external，`store` → done）：看板复用系统已有的语义填充，不发明新填充。

## 超限列

当一列的卡片数 `n` 超过它声明的 `limit`，WIP 芯片的描边和文字改为 `accent`。它加上一张阻塞卡片，就是这张图全部 2 个 accent 预算：预算不要花在别处。

## 复杂度预算

- 最多 5 列，每列最多 4 张卡，总共最多 12 张。
- 最多 2 个 accent 元素（超限芯片算一个；阻塞卡算一个）。
- 单列超预算 → 把积压聚合成一张计数卡（`+14 more`），而不是逐项列出。

## 反模式

- **在卡片之间画箭头。** 看板展示状态，不是流：如果流本身需要可见，改用泳道或流程。
- **一列超过 4 张卡。** 聚合成计数卡；不要让一列滚出画布。
- **一人一张卡。** 那是披着看板皮肤的组织架构图。
- **在制列不写 WIP 上限。** 上限是这个类型的半条命：一条工作流*穿过*的在制列若不写上限，就无法显示它已超限。入口队列和终结列是例外：容纳更多已完成的工作不受约束，所以它们显示裸计数。
- **每张阻塞卡都上 accent。** 一两张阻塞卡读起来是信号；满列 accent 读起来是噪音，还抹掉了焦点规则。
- **无上限增长的 "Done" 列。** 设个上限，在副标签或脚注里注明归档点：无界的 Done 列只会变成第二个 Backlog。
- **胶囊形 WIP 标签。** 芯片是 `rx=2` 的矩形，与 §6 节点盒中的类型标签原语一致（[primitives-core.md](primitives-core.md#node-box--full-pattern)）：胶囊看起来像来自另一套设计语言的状态徽章。

## 示例

- `assets/example-kanban.html` — 极简浅色。平台团队看板：Backlog（3）、In progress（4/3，超限）、Review（2/3）、Done（2），一张阻塞卡。
- `assets/example-kanban-dark.html` — 极简深色，同一数据。
- `assets/example-kanban-full.html` — 完整编辑排版：容器框 + 3 张宽度不均的摘要卡 + 页脚。
