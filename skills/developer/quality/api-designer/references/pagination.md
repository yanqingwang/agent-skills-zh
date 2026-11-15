> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/api-designer/references/pagination.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 分页模式

## 为什么要分页？

大型集合无法一次性全部返回，原因如下：
- 性能（查询慢、载荷大）
- 内存限制（服务器端和客户端）
- 网络超时
- 用户体验差

集合端点一律分页。

## 分页策略

### 1. 基于偏移量的分页

最常见、最直观。使用 `offset`（跳过多少条）和 `limit`（每页条数）。

**请求：**
```http
GET /users?offset=20&limit=10
```

**响应：**
```json
{
  "data": [
    {"id": 21, "name": "User 21"},
    {"id": 22, "name": "User 22"}
  ],
  "pagination": {
    "offset": 20,
    "limit": 10,
    "total": 150,
    "has_more": true
  },
  "links": {
    "first": "/users?offset=0&limit=10",
    "prev": "/users?offset=10&limit=10",
    "next": "/users?offset=30&limit=10",
    "last": "/users?offset=140&limit=10"
  }
}
```

**优点：**
- 实现简单
- 容易理解
- 支持随机访问（跳到任意一页）
- 显示总数

**缺点：**
- 大偏移量下性能下降（数据库要扫描大量行）
- 翻页期间数据发生变化会导致结果不一致
- 对实时数据效率低
- 数据库必须统计总行数（开销大）

**适用场景：**
- 中小规模数据集
- 数据变化不频繁
- 需要随机跳页
- 需要总数

### 2. 基于页码的分页

用页码简化偏移量分页。

**请求：**
```http
GET /users?page=3&per_page=10
```

**响应：**
```json
{
  "data": [...],
  "pagination": {
    "page": 3,
    "per_page": 10,
    "total_pages": 15,
    "total_count": 150
  },
  "links": {
    "first": "/users?page=1&per_page=10",
    "prev": "/users?page=2&per_page=10",
    "next": "/users?page=4&per_page=10",
    "last": "/users?page=15&per_page=10"
  }
}
```

**计算：**
- `offset = (page - 1) * per_page`
- `total_pages = ceil(total_count / per_page)`

**优缺点与偏移量分页相同，但：**
- 对用户更直观（第 1 页、第 2 页）
- 在 Web 应用中常见

### 3. 基于游标的分页

使用不透明游标（指针）指向下一批结果。

**请求：**
```http
GET /users?limit=10
GET /users?cursor=<cursor>&limit=10
```

**响应：**
```json
{
  "data": [
    {"id": 21, "name": "User 21"},
    {"id": 22, "name": "User 22"}
  ],
  "pagination": {
    "next_cursor": "<next-cursor>",
    "prev_cursor": "<prev-cursor>",
    "has_more": true
  },
  "links": {
    "next": "/users?cursor=<next-cursor>&limit=10",
    "prev": "/users?cursor=<prev-cursor>&limit=10"
  }
}
```

**游标结构（base64 编码）：**
```json
{"id": 30, "sort": "created_at"}
```

**实现：**
```sql
-- First page
SELECT * FROM users ORDER BY created_at DESC LIMIT 10;

-- Next page (cursor points to last item)
SELECT * FROM users
WHERE created_at < '2024-01-15T10:30:00Z'
ORDER BY created_at DESC
LIMIT 10;
```

**优点：**
- 结果一致（不漏项、不重复）
- 大数据集下高效
- 与实时数据配合良好
- 无需昂贵的 COUNT 查询
- 数据库性能更好

**缺点：**
- 无法随机访问（不能跳到第 10 页）
- 没有总数
- 实现更复杂
- 游标不透明（用户无法修改）

**适用场景：**
- 大型数据集
- 数据变化频繁
- 无限滚动 UI
- 实时信息流
- 性能要求高

### 4. 键集分页

与游标分页类似，但使用实际字段值而非不透明游标。

**请求：**
```http
GET /users?after_id=20&limit=10
GET /users?after_created_at=2024-01-15T10:30:00Z&limit=10
```

**响应：**
```json
{
  "data": [
    {"id": 21, "name": "User 21", "created_at": "2024-01-15T11:00:00Z"},
    {"id": 22, "name": "User 22", "created_at": "2024-01-15T11:30:00Z"}
  ],
  "pagination": {
    "after_id": 30,
    "limit": 10,
    "has_more": true
  },
  "links": {
    "next": "/users?after_id=30&limit=10"
  }
}
```

**实现：**
```sql
SELECT * FROM users
WHERE id > 20
ORDER BY id ASC
LIMIT 10;
```

**优点：**
- 非常高效（走索引）
- 游标透明（人类可读）
- 结果一致
- 实现简单

**缺点：**
- 需要有索引的列
- 无法随机访问
- 排序仅限游标字段
- 多字段排序时复杂

**适用场景：**
- 简单排序（按 ID、时间戳）
- 需要高效分页
- 希望游标透明
- 已有合适的索引

### 5. Seek 分页（基于时间）

面向时间序列数据的特化键集分页。

**请求：**
```http
GET /events?since=2024-01-15T10:00:00Z&until=2024-01-15T11:00:00Z&limit=100
```

**响应：**
```json
{
  "data": [...],
  "pagination": {
    "since": "2024-01-15T10:00:00Z",
    "until": "2024-01-15T11:00:00Z",
    "limit": 100,
    "has_more": true
  },
  "links": {
    "next": "/events?since=2024-01-15T11:00:00Z&until=2024-01-15T12:00:00Z&limit=100"
  }
}
```

**用于：**
- 时间序列数据
- 日志与事件
- 活动流
- 分析数据

## 默认限制

始终设置合理的默认值和上限：

```json
{
  "default_limit": 20,
  "max_limit": 100,
  "min_limit": 1
}
```

**校验：**
```http
GET /users?limit=1000

Response: 400 Bad Request
{
  "error": {
    "code": "INVALID_LIMIT",
    "message": "Limit must be between 1 and 100. Default is 20."
  }
}
```

## 响应格式

### 标准分页对象

```json
{
  "data": [...],
  "pagination": {
    "limit": 10,
    "offset": 20,
    "total": 150,
    "has_more": true,
    "has_previous": true
  }
}
```

### Link 头（RFC 5988）

```http
Link: </users?offset=0&limit=10>; rel="first",
      </users?offset=10&limit=10>; rel="prev",
      </users?offset=30&limit=10>; rel="next",
      </users?offset=140&limit=10>; rel="last"
```

**使用者：** GitHub API

### 内嵌链接

```json
{
  "data": [...],
  "_links": {
    "self": { "href": "/users?offset=20&limit=10" },
    "first": { "href": "/users?offset=0&limit=10" },
    "prev": { "href": "/users?offset=10&limit=10" },
    "next": { "href": "/users?offset=30&limit=10" },
    "last": { "href": "/users?offset=140&limit=10" }
  }
}
```

## 分页与排序

分页时始终支持排序：

```http
GET /users?sort=created_at&order=desc&limit=10
GET /users?sort=-created_at&limit=10                    # Descending
GET /users?sort=last_name,first_name&limit=10           # Multi-field
```

**游标分页时，游标必须包含排序字段：**
```json
{
  "cursor": {
    "id": 123,
    "created_at": "2024-01-15T10:30:00Z",
    "sort_fields": ["created_at", "id"]
  }
}
```

## 分页与过滤

把过滤与分页结合使用：

```http
GET /users?status=active&role=admin&offset=0&limit=10
```

**重要：** 先过滤，后分页：
1. 过滤记录
2. 统计过滤后的结果
3. 应用分页
4. 返回分页后的子集

## 总数

### 返回总数

```json
{
  "data": [...],
  "pagination": {
    "total": 1523,
    "limit": 10,
    "offset": 20
  }
}
```

**优点：**
- 客户端知道结果总量
- 可计算总页数
- 体验更好（显示"第 3 页，共 153 页"）

**缺点：**
- COUNT 查询开销大
- 拖慢响应
- 大型或频繁变化的数据集下不准确

### 省略总数

```json
{
  "data": [...],
  "pagination": {
    "has_more": true,
    "limit": 10
  }
}
```

**适用场景：**
- 大型数据集（COUNT 太慢）
- 实时数据（总数不断变化）
- 游标分页
- 无限滚动 UI

### 可选总数

让客户端按需请求总数：

```http
GET /users?limit=10&include_total=true
```

## 边界情况

### 空结果

```json
{
  "data": [],
  "pagination": {
    "offset": 0,
    "limit": 10,
    "total": 0,
    "has_more": false
  }
}
```

### 最后一页

```json
{
  "data": [{"id": 150, "name": "Last User"}],
  "pagination": {
    "offset": 140,
    "limit": 10,
    "total": 150,
    "has_more": false
  },
  "links": {
    "first": "/users?offset=0&limit=10",
    "prev": "/users?offset=130&limit=10",
    "next": null
  }
}
```

### 超出范围

```http
GET /users?offset=10000&limit=10

Response: 200 OK (empty results)
{
  "data": [],
  "pagination": {
    "offset": 10000,
    "limit": 10,
    "total": 150,
    "has_more": false
  }
}
```

或者对不存在的页返回 404：
```http
GET /users?page=1000&per_page=10

Response: 404 Not Found
{
  "error": {
    "code": "PAGE_NOT_FOUND",
    "message": "Page 1000 does not exist. Total pages: 15"
  }
}
```

## 最佳实践

1. **集合一律分页** - 绝不返回无上限的列表
2. **设置合理默认值** - 默认 limit 取 20-50 条
3. **强制最大上限** - 防止过载（最大 100-1000）
4. **包含 has_more 标志** - 告知客户端是否还有更多结果
5. **提供导航链接** - 让获取上一页/下一页更容易
6. **把分页写进文档** - 说明游标格式、限制、默认值
7. **保持一致** - 所有端点使用同一分页模式
8. **考虑性能** - 按数据规模/类型选择策略
9. **支持排序** - 让客户端控制结果顺序
10. **处理边界情况** - 空结果、最后一页、无效游标

## 对比矩阵

| 特性 | 偏移量 | 页码 | 游标 | 键集 |
|---------|--------|------|--------|--------|
| 性能 | 大偏移量下差 | 差 | 优 | 优 |
| 随机访问 | 是 | 是 | 否 | 否 |
| 总数 | 是 | 是 | 否 | 可选 |
| 一致性 | 差 | 差 | 优 | 优 |
| 复杂度 | 简单 | 简单 | 中等 | 中等 |
| 实时数据 | 差 | 差 | 优 | 优 |
| 数据库负载 | 高 | 高 | 低 | 低 |
| 使用场景 | 小数据集 | Web UI | 信息流/流 | 大数据集 |
