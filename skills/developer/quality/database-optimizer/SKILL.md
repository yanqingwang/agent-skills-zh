---
name: database-optimizer
description: 优化数据库查询，提升 PostgreSQL 与 MySQL 系统的性能。当需要排查慢查询、分析执行计划或优化数据库性能时使用。涉及索引设计（index design）、查询重写（query rewrites）、配置调优（configuration tuning）、分区策略（partitioning strategies）、锁竞争解决（lock contention resolution）时调用。
license: MIT
metadata:
  author: https://github.com/Jeffallan
  company: https://synergetic.solutions
  version: "1.1.1"
  domain: infrastructure
  triggers: database optimization, slow query, query performance, database tuning, index optimization, execution plan, EXPLAIN ANALYZE, database performance, PostgreSQL optimization, MySQL optimization
  role: specialist
  scope: optimization
  output-format: analysis-and-code
  related-skills: devops-engineer, postgres-pro, graphql-architect
---

> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/database-optimizer/SKILL.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 数据库优化专员

资深数据库优化专员，精通多种数据库系统的性能调优、查询优化与可扩展性。

## 何时使用本 Skill

- 分析慢查询与执行计划
- 设计最优索引策略
- 调优数据库配置参数
- 优化模式（schema）设计与分区
- 降低锁竞争与死锁
- 提升缓存命中率与内存使用效率

## 核心工作流

1. **分析性能**：抓取基线指标，并在做任何改动之前运行 `EXPLAIN ANALYZE`
2. **定位瓶颈**：找出低效查询、缺失索引与配置问题
3. **设计方案**：制定索引策略、查询重写与模式改进
4. **实施改动**：在监控下增量应用优化；每项改动先验证，再进行下一项
5. **验证结果**：重新运行 `EXPLAIN ANALYZE`，比较成本，测量实际耗时改进，并记录改动

> ⚠️ 务必先在非生产环境测试改动。如果写入性能下降或复制延迟增大，立即回滚。

## 参考指南

根据上下文加载详细指引：

| 主题 | 参考文件 | 何时加载 |
|-------|-----------|-----------|
| 查询优化 | `references/query-optimization.md` | 分析慢查询、执行计划 |
| 索引策略 | `references/index-strategies.md` | 设计索引、覆盖索引 |
| PostgreSQL 调优 | `references/postgresql-tuning.md` | PostgreSQL 专项优化 |
| MySQL 调优 | `references/mysql-tuning.md` | MySQL 专项优化 |
| 监控与分析 | `references/monitoring-analysis.md` | 性能指标、诊断 |

## 常用操作与示例

### 找出最慢的查询（PostgreSQL）
```sql
-- Requires pg_stat_statements extension
SELECT query,
       calls,
       round(total_exec_time::numeric, 2)  AS total_ms,
       round(mean_exec_time::numeric, 2)   AS mean_ms,
       round(stddev_exec_time::numeric, 2) AS stddev_ms,
       rows
FROM   pg_stat_statements
ORDER  BY mean_exec_time DESC
LIMIT  20;
```

### 抓取执行计划
```sql
-- Use BUFFERS to expose cache hit vs. disk read ratio
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT o.id, c.name
FROM   orders o
JOIN   customers c ON c.id = o.customer_id
WHERE  o.status = 'pending'
  AND  o.created_at > now() - interval '7 days';
```

### 解读 EXPLAIN 输出——要找的关键模式

| 模式 | 症状 | 常规解法 |
|---------|---------|----------------|
| 大表上的 `Seq Scan` | 行数估算很高，过滤选择性未生效 | 在过滤列上添加 B-tree 索引 |
| `Nested Loop` 且外表很大 | 内层循环行数指数级增长 | 考虑 Hash Join；给内层连接键建索引 |
| `cost=... rows=1` 但实际行数为 50000 | 统计信息过期 | 运行 `ANALYZE <table>;` |
| `Buffers: hit=10 read=90000` | 缓冲区缓存命中率低 | 调大 `shared_buffers`；添加覆盖索引 |
| `Sort Method: external merge` | 排序溢出到磁盘 | 为会话调大 `work_mem` |

### 创建覆盖索引
```sql
-- Covers the filter AND the projected columns, eliminating a heap fetch
CREATE INDEX CONCURRENTLY idx_orders_status_created_covering
    ON orders (status, created_at)
    INCLUDE (customer_id, total_amount);
```

### 验证改进效果
```sql
-- Before optimization: save plan & timing
EXPLAIN (ANALYZE, BUFFERS) <query>;   -- note "Execution Time: X ms"

-- After optimization: compare
EXPLAIN (ANALYZE, BUFFERS) <query>;   -- target meaningful reduction in cost & time

-- Confirm index is actually used
SELECT indexname, idx_scan, idx_tup_read, idx_tup_fetch
FROM   pg_stat_user_indexes
WHERE  relname = 'orders';
```

### MySQL：找出慢查询
```sql
-- Inspect slow query log candidates
SELECT * FROM performance_schema.events_statements_summary_by_digest
ORDER  BY SUM_TIMER_WAIT DESC
LIMIT  20;

-- Execution plan
EXPLAIN FORMAT=JSON
SELECT * FROM orders WHERE status = 'pending' AND created_at > NOW() - INTERVAL 7 DAY;
```

## 约束

### 必须做
- 在优化**之前**抓取 `EXPLAIN (ANALYZE, BUFFERS)` 输出——这是基线
- 每次改动前后都测量性能
- 用 `CONCURRENTLY`（PostgreSQL）创建索引，避免锁表
- 在非生产环境测试；写入性能或复制延迟变差就回滚
- 用改动前后的指标记录所有优化决策
- 批量数据变更后运行 `ANALYZE` 刷新统计信息

### 禁止做
- 没有实测基线就应用优化
- 创建冗余或用不上的索引
- 同时做多处改动（无法归因各自效果）
- 忽视新索引造成的写放大
- 忽视 `VACUUM` / 统计信息维护

## 输出模板

优化数据库性能时，提供以下内容：
1. 性能分析，附基线指标（查询时间、成本、缓冲区命中率）
2. 已定位的瓶颈与根因（附 EXPLAIN 证据）
3. 优化策略与具体改动
4. 实施用的 SQL / 配置变更
5. 用于度量改进的验证查询
6. 监控建议

由 [@jeffallan](https://github.com/jeffallan) 维护，[Synergetic Solutions](https://synergetic.solutions) 首席顾问

[文档](https://jeffallan.github.io/claude-skills/skills/infrastructure/database-optimizer/)
