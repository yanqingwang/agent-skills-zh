> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/layout-budget.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 布局网格、各类型预算、页面布局与摘要卡片

从 SKILL.md §7 与 §8 路由到本文件。SKILL.md 只保留一行网格规则、通用复杂度上限与拆分规则。本文件承载完整网格表、每条类型预算、页面布局与摘要卡片模式。

## 布局与间距

### 4px 网格

**结构几何，可被 4 整除：**节点原点、宽、高、间距、padding。有意不入网格的：字号（角色阶梯见 `references/output-spec.md`）、圆角、数据推导的位置、文本基线、箭头 marker、让 1px 描边保持锐利的 `.5` 偏移、描边宽度、透明度，以及 22×22 点阵图案。

| 类别 | 允许的值 |
|---|---|
| 节点宽 / 高 | 80, 96, 112, 120, 128, 140, 144, 160, 180, 200, 240, 320 |
| 节点间距 | 20, 24, 32, 40, 48 |
| 盒内 padding | 8, 12, 16 |
| 边框圆角 | 4, 6, 8 |

### 复杂度预算（每张图）

以下是各类型的上限。SKILL.md §7 的通用行（9 个节点、12 条箭头或转移、2 个 coral 元素、2 个注释标注，以及动效上限）在它们之上适用于所有类型；[semantic-patterns.md](semantic-patterns.md) 中某个语义模式自己的预算只能收紧这些值。一个类型是例外：SBGN 用下表自己的天花板替换 9 节点与 12 箭头两行，因为 process square 是反应标记而非节点，且每个反应都需要它的消耗弧与生成弧。它的其他通用行仍然适用，其他任何类型也不得类推突破 9 节点或 12 箭头。

| 上限 | 规则 |
|---|---|
| 唯一组件 / 关系 / 台账条目上限（architecture delta） | 8 / 10 / 8 |
| 管理带 / 流量范围 / 节点上限（architecture containment） | 2 / 4 / 8 |
| 生命线上限（sequence） | 5 |
| 组合片段上限（sequence） | 1（默认）；每片均为单区域 `opt`/`loop` 时才可为 2 |
| `alt` 区域上限（sequence） | 2 |
| 片段嵌套上限（sequence） | 1 |
| 泳道上限（swimlane） | 5 |
| 条目上限（quadrant） | 12 |
| 实体上限（ER） | 8 |
| 嵌套层级上限（nested） | 6 |
| 树深度上限 | 4 |
| 组织架构图深度上限 | 4 |
| 组织架构图节点上限 | 12 |
| 层数上限（layer stack） | 6 |
| 部件 / 层级 / 焦点部件上限（exploded axonometric） | 5 / 5 / 1，三个细节层级 |
| 标记房间或建筑 / 盒子 / 焦点上限（axonometric plan） | 8 / 40 / 1 |
| 圆上限（venn） | 3 |
| 层数上限（pyramid） | 6 |
| 雷达轴上限 | 5 |
| 雷达系列上限 | 5 |
| 焦点雷达系列上限 | 1 |
| 极坐标类目上限 | 8 |
| 极坐标系列上限 | 1 |
| 焦点极坐标类目上限 | 1 |
| 柱数上限（bar chart） | 8 |
| 柱数上限（waterfall） | 8 含总计，1 个小计 |
| 单元格上限（treemap） | 8 |
| 系列上限（line chart） | 5 |
| 任务上限（Gantt） | 12 |
| 阶段上限（steps） | 7，恰好 1 个焦点阶段 |
| 点数上限（scatter plot） | 30 |
| 系列 / 离群值上限（box plot） | 8 / 8，1 个焦点系列 |
| 阶段 / 节点 / 流上限（sankey） | 3 / 8 / 12 |
| 类目上限（fishbone） | 6 根骨，每根 3 个子因 |
| 组件 / 链接上限（wardley） | 9 / 12，2 条移动箭头 |
| 列 / 卡片上限（kanban） | 5 / 共 12，每列 4 |
| 阶段 / 行上限（user journey） | 6 / 3，2 个痛点标记 |
| 阶段 / 层上限（service blueprint） | 6 个阶段；customer / frontstage / backstage 必需；evidence / support 可选；1 个焦点单元格 |
| Unit Grid | 100 个等分格；10 × 10；4px 沟槽；1 个计数；至多 1 个焦点已完成格 |
| 区域 / 节点 / 路径上限（deployment） | 3 / 6 / 8，9 个产物 |
| 节点 / 边上限（dependency） | 9 / 14，4 个层级，1 个环 |
| 节点 / 弧上限（arc diagram） | 9 / 14，1 条焦点弧 |
| 需求行 / 主设计链接 / 主验证链接上限（requirement traceability） | 6 / 每行 1 / 每行 1，1 个焦点行 |
| 阶段 / 命令 / 事件 / 读模型上限（event modeling） | 6 / 每阶段 1 / 每阶段 1 / 每阶段 1，2 处强调色 |
| 类 / 关系上限（UML class） | 7 / 8，每个隔间 5 个成员 |
| 活动 / 切片 / 卡片上限（story map） | 5 / 3 / 12 |
| 表 / 列 / 外键上限（db schema） | 5 / 显示 8 / 6 |
| 大分子 / 过程 / 隔室 / 源汇 / 弧上限（SBGN） | 7 / 6 / 1 / 2 / 16；替换 9 节点与 12 箭头两行 |

超出就拆成两张图（总览 + 细节）。

### 页面布局

1. **头部** — `eyebrow` 角色、`title` 角色、可选副标题（`node-name` 字族，`muted`）。
2. **图容器** — 默认：**干净、无边框**、无背景，SVG 直接坐在页面纸面上。可选*带框*变体（卡片密集布局或 hero 位使用）：`paper-2` 背景 + 1px `rule` 边框 + 8px 圆角 + `1.5rem` padding + `overflow-x: auto`。
3. **摘要卡片** — 2–3 列网格、*不等*宽（如 `1.1fr 1fr 0.9fr`）。
4. **页脚** — colophon 用 `sublabel` 角色、`muted`、顶部细线边框。

## 摘要卡片模式

不要用 3 张一模一样的通用卡片。处理方式要有变化：

```html
<div class="card">
  <p class="eyebrow">SECTION LABEL</p>
  <div class="card-header">
    <span class="card-dot coral"></span>
    <h3>Card Title</h3>
  </div>
  <ul><li>Item</li></ul>
</div>
```

规则：

- `background: #ffffff`（不用 paper 色 —— 不加阴影的轻微抬升）
- `border: 1px solid`，颜色用 `rule`
- `border-radius: 6px`, `padding: 1.25rem`
- **不用 `box-shadow`**
- 卡片圆点：7px，`border-radius: 50%`（ink / muted / coral / link / soft 变体）
