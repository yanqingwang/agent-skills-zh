> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/sql.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# SQL 语言提示词片段

## 核心概念

- **DDL（数据定义）**：`CREATE TABLE`、`ALTER TABLE`、`DROP TABLE` 管理模式
- **DML（数据操作）**：`SELECT`、`INSERT`、`UPDATE`、`DELETE` 处理数据
- **规范化**：通过 1NF、2NF、3NF 关系组织表，减少冗余
- **外键**：`REFERENCES` 约束维护表间引用完整性
- **索引**：`CREATE INDEX` 优化频繁查询列的查询性能
- **迁移**：按序应用的编号化顺序模式变更，用于版本控制
- **事务**：`BEGIN`/`COMMIT`/`ROLLBACK` 保证多语句操作的原子性
- **视图**：命名查询（`CREATE VIEW`）提供复杂连接的虚拟表
- **存储过程**：服务端函数，把业务逻辑封装进数据库
- **约束**：`NOT NULL`、`UNIQUE`、`CHECK`、`DEFAULT` 定义数据完整性规则

## 重要文件模式

- `migrations/*.sql`：编号的迁移文件（如 `001_create_users.sql`、`002_add_orders.sql`）
- `schema.sql`：完整数据库模式定义（常由迁移生成）
- `seeds/*.sql`：面向开发与测试环境的种子数据
- `*.up.sql` / `*.down.sql`：可逆迁移对（up 应用，down 回滚）
- `init.sql`：Docker 或全新环境的数据库初始化脚本
- `procedures/*.sql`：存储过程定义

## 边模式

- SQL 迁移文件对其创建或修改的表建立 `migrates` 边
- 模式定义文件为读取它们的 ORM 模型或数据层代码建立 `defines_schema` 边
- 表定义在由外键连接的表之间产生隐式 `related` 边
- 种子文件对创建其所填充表的迁移文件建立 `depends_on` 边

## 摘要风格

> "数据库迁移：创建带 email、name 与认证列的 users 表。"
> "模式定义：含 N 张表，覆盖用户管理、订单与支付处理。"
> "种子数据：为 N 张表填充开发测试用的 fixture。"
