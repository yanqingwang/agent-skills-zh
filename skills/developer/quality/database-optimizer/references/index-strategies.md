> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/developer/quality/database-optimizer/references/index-strategies.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 索引策略

## 索引选择方法

### 找出索引候选

```sql
-- PostgreSQL: Find queries missing indexes
SELECT query, calls, total_exec_time, mean_exec_time
FROM pg_stat_statements
WHERE mean_exec_time > 100
ORDER BY total_exec_time DESC
LIMIT 20;

-- PostgreSQL: Find sequential scans on large tables
SELECT schemaname, tablename, seq_scan, seq_tup_read,
       idx_scan, seq_tup_read / seq_scan as avg_seq_tup_read
FROM pg_stat_user_tables
WHERE seq_scan > 0
  AND seq_tup_read / seq_scan > 10000
ORDER BY seq_tup_read DESC;

-- MySQL: Check table scans
SELECT * FROM sys.statements_with_full_table_scans
WHERE db = 'your_database'
ORDER BY exec_count DESC;
```

## B-Tree 索引（默认）

### 单列索引

```sql
-- Create index for WHERE clauses
CREATE INDEX idx_users_email ON users(email);

-- Create index for JOIN conditions
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Create index for ORDER BY
CREATE INDEX idx_products_price ON products(price);

-- Unique constraint as index
CREATE UNIQUE INDEX idx_users_username ON users(username);
```

### 多列索引

```sql
-- Order matters: most selective column first
CREATE INDEX idx_orders_status_created
ON orders(status, created_at);

-- Good for queries:
-- WHERE status = 'pending'
-- WHERE status = 'pending' AND created_at > '2024-01-01'
-- WHERE status = 'pending' ORDER BY created_at

-- NOT good for:
-- WHERE created_at > '2024-01-01' (status not specified)

-- Include commonly queried columns
CREATE INDEX idx_users_active_email_name
ON users(active, email) INCLUDE (name);
```

### 列顺序准则

```sql
-- Rule 1: Equality before range
CREATE INDEX idx_events_type_timestamp
ON events(type, timestamp);  -- type = 'click' AND timestamp > ...

-- Rule 2: High selectivity first
CREATE INDEX idx_orders_user_status
ON orders(user_id, status);  -- user_id is more selective than status

-- Rule 3: Match query patterns
-- Query: WHERE country = 'US' AND city = 'NYC' AND zip = '10001'
CREATE INDEX idx_locations_country_city_zip
ON locations(country, city, zip);
```

## 覆盖索引

### PostgreSQL INCLUDE 子句

```sql
-- Include non-key columns for index-only scans
CREATE INDEX idx_users_email_covering
ON users(email) INCLUDE (name, created_at);

-- Query can be satisfied entirely from index
EXPLAIN (ANALYZE, BUFFERS)
SELECT name, created_at
FROM users
WHERE email = 'user@example.com';
-- Should show "Index Only Scan"
```

### MySQL 覆盖索引

```sql
-- MySQL: Add columns to end of index
CREATE INDEX idx_orders_user_covering
ON orders(user_id, status, created_at, total);

-- Query uses covering index
EXPLAIN
SELECT status, created_at, total
FROM orders
WHERE user_id = 123;
-- Should show "Using index" in Extra column
```

## 部分索引

### PostgreSQL 部分索引

```sql
-- Index only active users
CREATE INDEX idx_users_active_email
ON users(email)
WHERE active = true;

-- Index only recent orders
CREATE INDEX idx_orders_recent
ON orders(user_id, created_at)
WHERE created_at > NOW() - INTERVAL '30 days';

-- Index only pending/processing orders (ignore completed)
CREATE INDEX idx_orders_active
ON orders(status, user_id)
WHERE status IN ('pending', 'processing');

-- Smaller index = better performance + less storage
```

### MySQL 过滤索引（8.0+）

```sql
-- MySQL 8.0+ supports functional indexes for similar effect
CREATE INDEX idx_users_active
ON users((CASE WHEN active = 1 THEN email END));
```

## 表达式索引

### PostgreSQL 函数索引

```sql
-- Index for case-insensitive search
CREATE INDEX idx_users_email_lower
ON users(LOWER(email));

-- Query must match expression
SELECT * FROM users
WHERE LOWER(email) = LOWER('User@Example.com');

-- Index for JSONB queries
CREATE INDEX idx_users_settings_theme
ON users((settings->>'theme'));

SELECT * FROM users
WHERE settings->>'theme' = 'dark';

-- Index for date truncation
CREATE INDEX idx_orders_date
ON orders(DATE(created_at));
```

### MySQL 生成列索引

```sql
-- Create generated column, then index it
ALTER TABLE users
ADD COLUMN email_lower VARCHAR(255)
GENERATED ALWAYS AS (LOWER(email)) STORED;

CREATE INDEX idx_users_email_lower
ON users(email_lower);

-- Use in queries
SELECT * FROM users
WHERE email_lower = LOWER('User@Example.com');
```

## 专用索引类型

### PostgreSQL GIN 索引（全文、数组、JSONB）

```sql
-- Full-text search
CREATE INDEX idx_posts_search
ON posts USING GIN(to_tsvector('english', title || ' ' || content));

SELECT * FROM posts
WHERE to_tsvector('english', title || ' ' || content)
      @@ to_tsquery('english', 'database & optimization');

-- Array search
CREATE INDEX idx_products_tags
ON products USING GIN(tags);

SELECT * FROM products
WHERE tags @> ARRAY['electronics', 'sale'];

-- JSONB search
CREATE INDEX idx_users_metadata
ON users USING GIN(metadata);

SELECT * FROM users
WHERE metadata @> '{"plan": "premium"}';
```

### PostgreSQL GiST 索引（几何、范围）

```sql
-- Range types
CREATE INDEX idx_events_time_range
ON events USING GIST(time_range);

SELECT * FROM events
WHERE time_range && '[2024-01-01, 2024-01-31]'::tstzrange;

-- PostGIS geometric queries
CREATE INDEX idx_locations_coords
ON locations USING GIST(coordinates);
```

### MySQL 全文索引

```sql
-- Full-text search
CREATE FULLTEXT INDEX idx_posts_content
ON posts(title, content);

SELECT * FROM posts
WHERE MATCH(title, content)
      AGAINST('database optimization' IN NATURAL LANGUAGE MODE);

-- Boolean mode for complex searches
SELECT * FROM posts
WHERE MATCH(title, content)
      AGAINST('+database -mysql' IN BOOLEAN MODE);
```

## 索引维护

### PostgreSQL 维护

```sql
-- Update statistics for query planner
ANALYZE users;

-- Rebuild bloated index
REINDEX INDEX CONCURRENTLY idx_users_email;

-- Check index bloat
SELECT
    schemaname, tablename, indexname,
    pg_size_pretty(pg_relation_size(indexrelid)) as index_size,
    idx_scan as scans,
    idx_tup_read as tuples_read,
    idx_tup_fetch as tuples_fetched
FROM pg_stat_user_indexes
ORDER BY pg_relation_size(indexrelid) DESC;

-- Find unused indexes
SELECT
    schemaname, tablename, indexname,
    idx_scan,
    pg_size_pretty(pg_relation_size(indexrelid)) as index_size
FROM pg_stat_user_indexes
WHERE idx_scan = 0
  AND indexrelname NOT LIKE 'pg_toast%'
ORDER BY pg_relation_size(indexrelid) DESC;
```

### MySQL 维护

```sql
-- Update statistics
ANALYZE TABLE users;

-- Rebuild index
ALTER TABLE users DROP INDEX idx_users_email, ADD INDEX idx_users_email(email);

-- Check index usage
SELECT
    object_schema,
    object_name,
    index_name,
    count_star,
    count_read,
    count_fetch
FROM performance_schema.table_io_waits_summary_by_index_usage
WHERE object_schema = 'your_database'
ORDER BY count_star DESC;

-- Find unused indexes
SELECT
    object_schema,
    object_name,
    index_name
FROM performance_schema.table_io_waits_summary_by_index_usage
WHERE index_name IS NOT NULL
  AND count_star = 0
  AND object_schema = 'your_database';
```

## 索引反模式

| 反模式 | 问题 | 解决方案 |
|-------------|-------|----------|
| 每列都建索引 | 写入开销大、浪费存储 | 按查询模式建索引 |
| 冗余索引 | `(a)` + `(a,b)` | 只保留 `(a,b)` |
| 列顺序错误 | 对 `WHERE user_id = ?` 用 `(created_at, user_id)` | 把过滤列放前面 |
| 过度覆盖 | 纳入很少用到的列 | 只纳入频繁访问的列 |
| 忽略 WHERE 子句 | 为 5% 的数据建全量索引 | 改用部分索引 |
| 表达式不匹配 | 索引 `email`，查询 `LOWER(email)` | 建表达式索引 |

## 索引设计检查清单

1. **分析查询**：用 pg_stat_statements 或慢查询日志
2. **检查执行计划**：留意大表上的 Seq Scan
3. **设计索引**：等值 → 范围 → INCLUDE
4. **并发创建**：避免锁表（PostgreSQL）
5. **验证改进**：对比改动前后的 EXPLAIN
6. **监控使用情况**：30 天后删除未使用的索引
7. **定期维护**：按需执行 VACUUM、ANALYZE、REINDEX
