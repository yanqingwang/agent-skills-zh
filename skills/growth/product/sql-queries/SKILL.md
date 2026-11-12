---
name: sql-queries
description: "根据自然语言描述生成 SQL 查询。支持 BigQuery、PostgreSQL、MySQL 及其他方言。从上传的图表或文档中读取数据库 schema。适用于编写 SQL、构建数据报表、探索数据库，或将业务问题转化为查询的场景。"
---

> **中文汉化版** · 上游：[phuryn/pm-skills](https://github.com/phuryn/pm-skills) · 原文件：`pm-data-analytics/skills/sql-queries/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# SQL 查询生成器

## 用途
将自然语言需求转化为跨多种数据库平台的优化 SQL 查询。本 Skill 帮助产品经理、分析师和工程师生成准确的查询，无需手动处理语法。

## 工作原理

### 第 1 步：理解你的数据库 Schema
- 如果你提供 schema 文件（SQL、文档或图表描述），我会读取并分析它
- 提取表名、列定义、数据类型和关系
- 识别主键、外键和索引策略

### 第 2 步：处理你的请求
- 明确你需要检索或分析的确切数据
- 确认 SQL 方言（BigQuery、PostgreSQL、MySQL、Snowflake 等）
- 询问是否有额外要求（过滤、聚合、排序）

### 第 3 步：生成优化查询
- 编写充分利用数据库结构的高效 SQL
- 附上解释复杂逻辑的注释
- 加入针对大数据集的性能考量
- 适用时提供替代方案

### 第 4 步：解释与测试
- 用通俗的英语解释查询逻辑
- 建议如何测试或验证结果
- 给出性能优化建议
- 如需要，生成测试脚本或示例数据

## 使用示例

**示例 1：从 Schema 文件生成查询**

```
Upload your database_schema.sql file and say:
"Generate a query to find users who signed up in the last 30 days
and had at least 5 active sessions"
```


**示例 2：从图表描述生成查询**

```
"Here's my database: Users table (id, email, created_at), Sessions table
(id, user_id, timestamp, duration). Generate a query for average session
duration per user in January 2026."
```


**示例 3：复杂的分析查询**

```
"Create a BigQuery query to analyze our revenue by region and customer tier,
including year-over-year growth rates."
```


## 核心能力

- **多方言支持**：适用于 BigQuery、PostgreSQL、MySQL、Snowflake、SQL Server
- **文件读取**：读取 schema 文件、SQL 转储和数据文档
- **查询优化**：建议索引、分区和性能改进
- **解释**：拆解查询，便于学习和文档化
- **测试**：可生成测试查询和示例数据脚本
- **脚本执行**：为你的数据库创建可执行的 SQL 脚本

## 获得最佳效果的建议

1. **提供上下文**：分享你的数据库 schema 或结构
2. **描述具体**：清楚说明所需数据和任何过滤条件
3. **注明数据库**：指明你使用的 SQL 方言
4. **附上约束**：说明数据量、时间范围和性能需求
5. **指定格式**：如需特定输出，说明查询结果格式

## 输出格式

你将收到：
- **SQL 查询**：带注释、可用于生产的 SQL 代码
- **解释**：查询的作用与工作方式
- **性能说明**：优化建议与注意事项
- **测试脚本**（如需要）：示例数据和验证查询

---

### 延伸阅读

- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [How to Become a Technology-Literate PM](https://www.productcompass.pm/p/how-to-become-a-technology-literate)
