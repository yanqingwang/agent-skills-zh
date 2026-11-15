> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/api-designer/references/versioning.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# API 版本控制策略

## 为什么要做 API 版本控制？

API 版本控制让你在为现有客户端保持向后兼容的同时演进 API。破坏性变更必须引入新版本。

### 破坏性变更

需要新版本的变更：
- 删除或重命名字段
- 修改字段类型（字符串改为整数）
- 向请求添加必填字段
- 修改响应结构
- 删除端点
- 同一场景下修改 HTTP 状态码
- 修改认证机制

### 非破坏性变更

不需要新版本的安全变更：
- 添加新端点
- 添加可选的请求字段
- 向响应添加新字段（客户端应忽略未知字段）
- 修复 bug
- 性能改进
- 向现有资源添加新的 HTTP 方法

## 版本控制策略

### 1. URI 版本控制

最常见、最直观的方式。版本号是 URL 路径的一部分。

```http
GET /v1/users/123
GET /v2/users/123
```

**优点：**
- 清晰，在 URL 中可见
- 易于理解和实现
- 路由和缓存简单
- 可以同时运行多个版本

**缺点：**
- 违背 REST 原则（同一资源、不同 URI）
- 切换版本需要更新客户端代码
- 可能导致 URI 膨胀

**实现方式：**
```
/v1/users
/v1/products
/v2/users      # New version with breaking changes
/v2/products
```

### 2. 请求头版本控制

版本号在 HTTP 请求头中指定（Accept 头或自定义头）。

**Accept 头：**
```http
GET /users/123
Accept: application/vnd.myapi.v1+json

GET /users/123
Accept: application/vnd.myapi.v2+json
```

**自定义请求头：**
```http
GET /users/123
API-Version: 1

GET /users/123
API-Version: 2
```

**优点：**
- URI 保持稳定
- 更符合 REST（同一资源、同一 URI）
- 把版本控制与资源标识分离

**缺点：**
- 不可见（更难调试）
- 路由更复杂
- 难以在浏览器中测试
- 缓存复杂

### 3. 查询参数版本控制

版本号通过查询参数指定。

```http
GET /users/123?version=1
GET /users/123?version=2

# or
GET /users/123?api-version=1
GET /users/123?api-version=2
```

**优点：**
- 实现简单
- 易于测试
- 在 URL 中可见

**缺点：**
- 污染查询字符串
- 不符合语义（版本不是过滤器）
- 可能与其他查询参数冲突

### 4. 内容协商

客户端通过内容协商指定所需版本。

```http
GET /users/123
Accept: application/vnd.myapi+json; version=1

GET /users/123
Accept: application/vnd.myapi+json; version=2
```

**优点：**
- 非常符合 REST
- 内容类型协商灵活
- URI 稳定

**缺点：**
- 实现复杂
- 对开发者不够直观
- 更难测试

## 推荐方案

**对大多数 API，推荐使用 URI 版本控制**，因为：
- 最显式、最容易发现
- 易于理解和调试
- 实现和维护简单
- 版本之间界限清晰

```
/v1/users
/v2/users
/v3/users
```

## 版本格式

### 仅用主版本号

公共 API 使用简单的主版本号（v1、v2、v3）：
```
/v1/users
/v2/users
```

**优点：**
- 简单清晰
- 易于传达
- 迫使团队慎重对待破坏性变更

### 基于日期的版本

一些 API 用日期做版本号：
```
/2024-01-01/users
/2024-06-15/users
```

**使用者：** Stripe、GitHub API

**优点：**
- 清楚版本何时发布
- 时间线易于理解
- 不必纠结主/次版本

**缺点：**
- 对客户端不够直观
- 更难了解具体改了什么

## 版本生命周期

### 1. 引入阶段

新版本与现有版本并行发布：
```
/v1/users  # Still supported
/v2/users  # New version available
```

为新版本发布公告：
- 说明变更的博客文章
- 迁移指南
- 破坏性变更清单
- v1 弃用时间表

### 2. 弃用阶段

把旧版本标记为弃用，但保持运行：

```http
GET /v1/users/123

Response:
Deprecation: true
Sunset: Wed, 15 Jan 2025 00:00:00 GMT
Link: </v2/users/123>; rel="successor-version"

{
  "id": 123,
  "name": "John Doe"
}
```

**弃用响应头：**
- `Deprecation: true` - 表示该版本已弃用
- `Sunset: <date>` - 版本将被移除的时间（RFC 8594）
- `Link: <url>; rel="successor-version"` - 指向新版本

### 3. 下线阶段

旧版本在公告的日期关闭。

对已弃用的端点返回 410 Gone：
```http
GET /v1/users/123

Response: 410 Gone
{
  "error": {
    "code": "VERSION_SUNSET",
    "message": "API v1 was sunset on 2025-01-15. Please use v2.",
    "documentation_url": "https://api.example.com/docs/migration-v1-to-v2"
  }
}
```

## 弃用策略

### 推荐时间表

1. **宣布弃用** - 至少在下线前 6 个月
2. **支持期** - 两个版本并行运行 6-12 个月
3. **下线日期** - 提前明确公布日期
4. **宽限期** - 完全关闭前 30 天返回 410 Gone

### 沟通渠道

- API 响应头
- 发给注册开发者的邮件
- 博客文章与变更日志
- 控制台通知
- 文档更新
- 状态页公告

## 迁移策略

### 提供迁移指南

```markdown
# Migrating from v1 to v2

## Breaking Changes

### User Resource Changes

**v1:**
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}
```

**v2:**
```json
{
  "id": 123,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com"
}
```

**Migration:**
- Split `name` field into `first_name` and `last_name`
- Update client code to use new fields
```

### 提供工具

- 迁移脚本
- SDK 更新
- API diff 查看器
- 兼容层（临时）

## 版本发现

### 根端点

```http
GET /

Response:
{
  "versions": {
    "v1": {
      "status": "deprecated",
      "sunset_date": "2025-01-15",
      "documentation_url": "https://api.example.com/docs/v1"
    },
    "v2": {
      "status": "current",
      "documentation_url": "https://api.example.com/docs/v2"
    },
    "v3": {
      "status": "beta",
      "documentation_url": "https://api.example.com/docs/v3"
    }
  }
}
```

### 版本信息端点

```http
GET /v2/version

Response:
{
  "version": "v2",
  "released": "2024-01-15",
  "status": "stable",
  "sunset_date": null
}
```

## OpenAPI 版本控制

### 每个版本一份独立规格

```
openapi-v1.yaml
openapi-v2.yaml
openapi-v3.yaml
```

每份规格都完整且独立。

### 单一规格加 servers

```yaml
openapi: 3.1.0
info:
  title: My API
  version: 2.0.0
servers:
  - url: https://api.example.com/v1
    description: Version 1 (deprecated)
  - url: https://api.example.com/v2
    description: Version 2 (current)
```

## 最佳实践

1. **从第一天起就用版本** - 以 /v1 开头，而不是 /api
2. **只用主版本号** - 使用 v1、v2、v3（不要 v1.1、v1.2）
3. **较长的弃用期** - 给客户端留出迁移时间（6-12 个月）
4. **沟通清晰** - 使用响应头、文档、邮件
5. **维护旧版本** - 至少同时支持 2 个版本
6. **记录变更** - 提供详细的迁移指南
7. **使用语义化版本** - 用于内部/SDK 版本号
8. **绝不无预警地破坏** - 破坏性变更必须提前公告
9. **提供工具** - 迁移脚本、更新后的 SDK
10. **监控用量** - 跟踪各版本的使用情况

## 反模式

避免这些错误：

- **不升版本就引入破坏性变更** - 会破坏现有客户端
- **版本过多** - 维护负担（最多 2-3 个活跃版本）
- **弃用期太短** - 让开发者恼火
- **没有迁移路径** - 升级痛苦
- **突然下线** - 无预警打挂生产应用
- **版本策略不一致** - 不同端点采用不同策略
- **只给单个端点做版本** - 整个 API 用一致的版本
