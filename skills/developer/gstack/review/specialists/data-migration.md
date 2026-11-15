> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/review/specialists/data-migration.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Data Migration Specialist 评审清单

范围：当 SCOPE_MIGRATIONS=true 时
输出：JSON 对象，每条发现一行。Schema：
{"severity":"CRITICAL|INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"data-migration","summary":"...","fix":"...","fingerprint":"path:line:data-migration","specialist":"data-migration"}
可选字段：line、fix、fingerprint、evidence、test_stub。
若无发现：只输出 `NO FINDINGS`，不输出任何其他内容。

---

## 类别

### 可回滚性
- 该 migration 能否在不丢数据的情况下回滚？
- 是否存在对应的 down/rollback migration？
- rollback 是否真的撤销了变更，还是只是 no-op？
- 回滚会不会破坏当前应用代码？

### 数据丢失风险
- 删除仍含数据的列（应先加弃用期）
- 更改会截断数据的列类型（varchar(255) → varchar(50)）
- 未验证没有代码引用就删除表
- 重命名列而未更新所有引用（ORM、裸 SQL、视图）
- 给已含 NULL 值的列加 NOT NULL 约束（需先回填）

### 锁时长
- 大表上不带 CONCURRENTLY 的 ALTER TABLE（PostgreSQL）
- 行数 >100K 的表上不带 CONCURRENTLY 地加索引
- 本可合并为一次锁获取的多条 ALTER TABLE
- 在流量高峰时段获取排他锁的 schema 变更

### 回填策略
- 无 DEFAULT 值的新 NOT NULL 列（加约束前需回填）
- 带计算默认值、需要批量填充的新列
- 存量记录缺少回填脚本或 rake task
- 一次性更新全部行而非分批的回填（会锁表）

### 索引创建
- 生产表上不带 CONCURRENTLY 的 CREATE INDEX
- 重复索引（新索引与既有索引覆盖相同列）
- 新外键列缺少索引
- 全量索引更有用时却建了部分索引（或相反）

### 多阶段安全
- 必须与应用代码按特定顺序部署的 migration
- 会破坏当前运行代码的 schema 变更（先部署代码，再迁移）
- 依赖部署边界的 migration（旧代码 + 新 schema = 崩溃）
- 滚动部署期间缺少处理新旧代码混合的 feature flag
