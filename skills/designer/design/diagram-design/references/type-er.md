> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-er.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# ER 图 / 数据模型

**适用场景：** 概念与逻辑数据模型、API 资源关系、领域模型：任何故事是*实体和基数*的场合。

**不用于物理模式。** ER 是实体层面的：关系线连接*盒子*并在两端承载基数。当重点是带 SQL 类型、约束芯片、索引、以及**列对列**锚定的外键的真实表时，改用 [`type-db-schema.md`](type-db-schema.md)。

## 布局约定
- 每个实体是一个两段式盒子：
  - **头部**：类型标签（`ENTITY`）+ `node-name` 角色的实体名。
  - **主体**：`sublabel` 角色的字段列表，每行一条。PK 前缀 `#`，FK 前缀 `→`。
- 关系：实体之间的线，两端标基数：
  - `1`、`N`、`0..1`、`1..*` 用 `arrow-label` 角色 8px，离实体边 10–12px。
  - 可选的关系标签（"has"、"belongs to"）居中放在线上。
- 相关实体排得近一些；让大多数关系落在直线上，不缠结。
- coral 用在模型的聚合根或中心实体上。

## 反模式
- 模型上有几十个外键时，每个外键都画一条箭头：改按簇排布。
- 同一关系两端的基数记法不一致。
- 字段垫成等高盒：按内容取自然高度即可。

## 示例
- `assets/example-er.html` — 极简浅色
- `assets/example-er-dark.html` — 极简深色
- `assets/example-er-full.html` — 完整编辑排版
