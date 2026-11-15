> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/architecture-designer/references/database-selection.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 数据库选型

## 数据库类型

| 类型 | 示例 | 最适合 |
|------|----------|----------|
| **关系型** | PostgreSQL、MySQL | 事务、复杂查询、关系 |
| **文档型** | MongoDB、Firestore | 灵活 schema、快速迭代 |
| **键值型** | Redis、DynamoDB | 缓存、session、高吞吐 |
| **时序型** | TimescaleDB、InfluxDB | 指标、IoT、分析 |
| **图数据库** | Neo4j、Neptune | 关系、社交网络 |
| **搜索型** | Elasticsearch、Meilisearch | 全文检索、日志 |

## 关系型（PostgreSQL、MySQL）

```
Best For:
- Financial transactions (ACID compliance)
- Complex queries with joins
- Data integrity requirements
- Structured, predictable schemas

When to Avoid:
- Highly variable schemas
- Massive horizontal scaling needs
- Simple key-value access patterns
```

| 特性 | PostgreSQL | MySQL |
|---------|------------|-------|
| JSON 支持 | 优秀（JSONB） | 良好（JSON） |
| 全文检索 | 内置 | 基础 |
| 扩展 | 生态丰富 | 有限 |
| 复制 | 流复制、逻辑复制 | 语句、行级 |

## 文档型（MongoDB、Firestore）

```
Best For:
- Flexible, evolving schemas
- Hierarchical data (nested documents)
- Rapid prototyping
- Content management

When to Avoid:
- Complex transactions across documents
- Heavy relational queries
- Strict schema requirements
```

## 键值型（Redis、DynamoDB）

```
Best For:
- Session storage
- Caching layer
- Real-time leaderboards
- Rate limiting counters

When to Avoid:
- Complex queries
- Relational data
- Large value sizes (>1MB)
```

## 时序型（TimescaleDB、InfluxDB）

```
Best For:
- Metrics and monitoring
- IoT sensor data
- Financial tick data
- Event logging with timestamps

When to Avoid:
- Frequent updates to existing records
- Complex relational queries
- Non-time-based access patterns
```

## 决策矩阵

| 需求 | 推荐 |
|-------------|-------------|
| ACID 事务 | PostgreSQL、MySQL |
| 灵活 schema | MongoDB、Firestore |
| 高速缓存 | Redis |
| 时序数据 | TimescaleDB、InfluxDB |
| 社交关系 | Neo4j |
| 全文检索 | Elasticsearch |
| Serverless 规模 | DynamoDB、Firestore |

## 快速参考

| 问题 | 是 → |
|----------|----------|
| 需要 ACID 事务？ | 关系型（PostgreSQL） |
| schema 频繁变更？ | 文档型（MongoDB） |
| 亚毫秒级读取？ | 键值型（Redis） |
| 基于时间的查询？ | 时序型 |
| 遍历关系？ | 图数据库（Neo4j） |
| 全文检索为主？ | Elasticsearch |
