> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/api-designer/references/rest-patterns.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# REST 设计模式

## 面向资源的架构

REST API 围绕资源构建，而不是围绕动作。资源是你 API 的名词。

### 资源标识

**好的资源 URI：**
```
GET    /users                  # Collection
GET    /users/{id}             # Individual resource
GET    /users/{id}/orders      # Nested collection
POST   /users                  # Create resource
PUT    /users/{id}             # Replace resource
PATCH  /users/{id}             # Update resource
DELETE /users/{id}             # Delete resource
```

**差的资源 URI：**
```
POST   /getUser                # Verb in URI
POST   /createUser             # Verb in URI
GET    /user?action=delete     # Action as query param
```

### 资源命名规范

- 集合用复数名词：`/users`、`/orders`、`/products`
- 小写加连字符，提高可读性：`/shipping-addresses`
- 避免过深嵌套（最多 2-3 层）：`/users/{id}/orders/{orderId}`
- 用查询参数做过滤：`/users?status=active&role=admin`

## HTTP 方法语义

### 安全与幂等方法

| 方法 | 安全 | 幂等 | 使用场景 |
|--------|------|------------|----------|
| GET | 是 | 是 | 获取资源 |
| POST | 否 | 否 | 创建资源、非幂等操作 |
| PUT | 否 | 是 | 替换整个资源 |
| PATCH | 否 | 否 | 部分更新 |
| DELETE | 否 | 是 | 删除资源 |
| HEAD | 是 | 是 | 仅获取元数据 |
| OPTIONS | 是 | 是 | 获取允许的方法 |

### 方法用法

**GET - 获取资源**
```http
GET /users/123
Accept: application/json

Response: 200 OK
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}
```

**POST - 创建资源**
```http
POST /users
Content-Type: application/json

{
  "name": "Jane Smith",
  "email": "jane@example.com"
}

Response: 201 Created
Location: /users/124
{
  "id": 124,
  "name": "Jane Smith",
  "email": "jane@example.com",
  "created_at": "2024-01-16T14:20:00Z"
}
```

**PUT - 替换资源**
```http
PUT /users/123
Content-Type: application/json

{
  "name": "John Doe Updated",
  "email": "john.new@example.com"
}

Response: 200 OK
{
  "id": 123,
  "name": "John Doe Updated",
  "email": "john.new@example.com",
  "updated_at": "2024-01-17T09:15:00Z"
}
```

**PATCH - 部分更新**
```http
PATCH /users/123
Content-Type: application/json

{
  "email": "john.updated@example.com"
}

Response: 200 OK
{
  "id": 123,
  "name": "John Doe",
  "email": "john.updated@example.com",
  "updated_at": "2024-01-17T10:00:00Z"
}
```

**DELETE - 删除资源**
```http
DELETE /users/123

Response: 204 No Content
```

## HTTP 状态码

### 成功状态码（2xx）

- **200 OK** - 请求成功（GET、PUT、PATCH）
- **201 Created** - 资源已创建（POST），包含 Location 响应头
- **202 Accepted** - 请求已接受，进入异步处理
- **204 No Content** - 成功但无响应体（DELETE）

### 重定向（3xx）

- **301 Moved Permanently** - 资源已永久移动
- **302 Found** - 临时重定向
- **304 Not Modified** - 缓存版本仍然有效

### 客户端错误（4xx）

- **400 Bad Request** - 请求语法无效或校验失败
- **401 Unauthorized** - 需要认证或认证失败
- **403 Forbidden** - 已认证但无权限
- **404 Not Found** - 资源不存在
- **405 Method Not Allowed** - 资源不支持该 HTTP 方法
- **409 Conflict** - 请求与当前状态冲突（如重复创建）
- **422 Unprocessable Entity** - 语法正确但语义错误
- **429 Too Many Requests** - 超出速率限制

### 服务器错误（5xx）

- **500 Internal Server Error** - 服务器意外错误
- **502 Bad Gateway** - 上游服务器返回无效响应
- **503 Service Unavailable** - 服务器暂时不可用
- **504 Gateway Timeout** - 上游服务器超时

## HATEOAS（超媒体）

### 超媒体驱动的 API

包含指向相关资源和可用操作的链接：

```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "_links": {
    "self": { "href": "/users/123" },
    "orders": { "href": "/users/123/orders" },
    "update": { "href": "/users/123", "method": "PATCH" },
    "delete": { "href": "/users/123", "method": "DELETE" }
  }
}
```

### HAL（Hypertext Application Language）

```json
{
  "id": 123,
  "name": "John Doe",
  "_links": {
    "self": { "href": "/users/123" }
  },
  "_embedded": {
    "orders": [
      {
        "id": 456,
        "total": 99.99,
        "_links": {
          "self": { "href": "/orders/456" }
        }
      }
    ]
  }
}
```

## 内容协商

### Accept 头

```http
GET /users/123
Accept: application/json

GET /users/123
Accept: application/xml

GET /users/123
Accept: application/hal+json
```

### 响应 Content-Type

```http
Content-Type: application/json; charset=utf-8
Content-Type: application/problem+json
Content-Type: application/hal+json
```

## 幂等性

### 幂等操作

**PUT - 始终幂等：**
多个相同的 PUT 请求与单个请求产生相同的结果。

**DELETE - 幂等：**
第一次 DELETE 返回 204，后续 DELETE 返回 404（最终状态相同）。

**POST - 默认不幂等：**
幂等的 POST 使用 `Idempotency-Key` 请求头：

```http
POST /payments
Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000
Content-Type: application/json

{
  "amount": 100.00,
  "currency": "USD"
}
```

服务器保存幂等键，对重复请求返回相同响应。

## 缓存控制

### 缓存头

```http
Cache-Control: public, max-age=3600
Cache-Control: private, no-cache
Cache-Control: no-store
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Wed, 15 Jan 2024 10:30:00 GMT
```

### 条件请求

```http
GET /users/123
If-None-Match: "33a64df551425fcc55e4d42a148795d9f25f89d4"

Response: 304 Not Modified
```

```http
PUT /users/123
If-Match: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Content-Type: application/json

{
  "name": "Updated Name"
}

Response: 412 Precondition Failed (if ETag doesn't match)
```

## URI 模式

### 一致的 URI 结构

```
/{version}/{resource}
/{version}/{resource}/{id}
/{version}/{resource}/{id}/{sub-resource}
/{version}/{resource}/{id}/{sub-resource}/{sub-id}
```

### 查询参数

**过滤：**
```
GET /users?status=active&role=admin
GET /products?category=electronics&price_min=100&price_max=500
```

**排序：**
```
GET /users?sort=created_at
GET /users?sort=-created_at          # Descending
GET /users?sort=name,created_at      # Multiple fields
```

**字段选择：**
```
GET /users?fields=id,name,email
GET /users?exclude=password,social_security_number
```

**搜索：**
```
GET /users?q=john
GET /products?search=laptop
```

## 最佳实践

1. **用名词，不用动词** - 资源是名词，方法是动词
2. **集合用复数** - 用 `/users` 而不是 `/user`
3. **命名一致** - 选定 snake_case 或 camelCase 并坚持使用
4. **状态码恰当** - 使用合适的 HTTP 状态码
5. **包含元数据** - 响应中带分页、过滤、排序信息
6. **为 API 做版本控制** - 从第一天起就规划演进
7. **文档覆盖一切** - OpenAPI 规格、示例、错误码
8. **默认安全** - HTTPS、认证、速率限制
9. **支持过滤** - 让客户端精确获取所需内容
10. **实现 HATEOAS** - 让 API 自文档化、可发现
