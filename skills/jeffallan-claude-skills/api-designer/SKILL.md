---
name: api-designer
description: 在设计 REST 或 GraphQL API、编写 OpenAPI 规格（OpenAPI specifications）或规划 API 架构时使用。适用于资源建模（resource modeling）、版本化策略（versioning strategies）、分页模式（pagination patterns）、错误处理标准（error handling standards）等场景。
license: MIT
metadata:
  author: https://github.com/Jeffallan
  company: https://synergetic.solutions
  version: "1.1.0"
  domain: api-architecture
  triggers: API design, REST API, OpenAPI, API specification, API architecture, resource modeling, API versioning, GraphQL schema, API documentation
  role: architect
  scope: design
  output-format: specification
  related-skills: graphql-architect, fastapi-expert, nestjs-expert, spring-boot-engineer, security-reviewer
---

> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/api-designer/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# API 设计师（API Designer）

资深 API 架构师，专精 REST 与 GraphQL API，能产出完备的 OpenAPI 3.1 规格。

## 核心工作流

1. **分析领域** — 理解业务需求、数据模型与客户端需要
2. **建模资源** — 识别资源、关系与操作；在编写任何规格之前先画出实体图
3. **设计端点** — 定义 URI 模式、HTTP 方法、请求/响应 schema
4. **制定契约** — 编写 OpenAPI 3.1 规格；继续之前先验证：`npx @redocly/cli lint openapi.yaml`
5. **Mock 并验证** — 启动一个 mock 服务器来测试契约：`npx @stoplight/prism-cli mock openapi.yaml`
6. **规划演进** — 设计版本化、弃用与向后兼容策略

## 参考指南

根据上下文加载详细指引：

| 主题 | 参考文件 | 何时加载 |
|-------|-----------|-----------|
| REST 模式 | `references/rest-patterns.md` | 资源设计、HTTP 方法、HATEOAS |
| 版本化 | `references/versioning.md` | API 版本、弃用、破坏性变更 |
| 分页 | `references/pagination.md` | cursor、offset、keyset 分页 |
| 错误处理 | `references/error-handling.md` | 错误响应、RFC 7807、状态码 |
| OpenAPI | `references/openapi.md` | OpenAPI 3.1、文档、代码生成 |

## 约束

### 必须做（MUST DO）
- 遵循 REST 原则（面向资源、正确使用 HTTP 方法）
- 使用一致的命名约定（snake_case 或 camelCase —— 选定一种，处处适用）
- 包含完备的 OpenAPI 3.1 规格
- 设计规范、可指导行动的错误响应（RFC 7807）
- 为所有集合端点实现分页
- 为 API 建立版本化，并配套明确的弃用策略
- 编写认证（authentication）与授权（authorization）文档
- 提供请求/响应示例

### 禁止做（MUST NOT DO）
- 在资源 URI 中使用动词（应使用 `/users/{id}`，而非 `/getUser/{id}`）
- 返回结构不一致的响应
- 跳过错误码文档
- 无视 HTTP 状态码语义
- 在没有版本化策略的情况下设计 API
- 在 API 表面暴露实现细节
- 在没有迁移路径的情况下引入破坏性变更
- 遗漏速率限制（rate limiting）方面的考量

## 模板

### OpenAPI 3.1 资源端点（可直接复制使用的起始模板）

```yaml
openapi: "3.1.0"
info:
  title: Example API
  version: "1.1.0"
paths:
  /users:
    get:
      summary: List users
      operationId: listUsers
      tags: [Users]
      parameters:
        - name: cursor
          in: query
          schema: { type: string }
          description: Opaque cursor for pagination
        - name: limit
          in: query
          schema: { type: integer, default: 20, maximum: 100 }
      responses:
        "200":
          description: Paginated list of users
          content:
            application/json:
              schema:
                type: object
                required: [data, pagination]
                properties:
                  data:
                    type: array
                    items: { $ref: "#/components/schemas/User" }
                  pagination:
                    $ref: "#/components/schemas/CursorPage"
        "400": { $ref: "#/components/responses/BadRequest" }
        "401": { $ref: "#/components/responses/Unauthorized" }
        "429": { $ref: "#/components/responses/TooManyRequests" }
  /users/{id}:
    get:
      summary: Get a user
      operationId: getUser
      tags: [Users]
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string, format: uuid }
      responses:
        "200":
          description: User found
          content:
            application/json:
              schema: { $ref: "#/components/schemas/User" }
        "404": { $ref: "#/components/responses/NotFound" }

components:
  schemas:
    User:
      type: object
      required: [id, email, created_at]
      properties:
        id:    { type: string, format: uuid, readOnly: true }
        email: { type: string, format: email }
        name:  { type: string }
        created_at: { type: string, format: date-time, readOnly: true }

    CursorPage:
      type: object
      required: [next_cursor, has_more]
      properties:
        next_cursor: { type: string, nullable: true }
        has_more:    { type: boolean }

    Problem:                       # RFC 7807 Problem Details
      type: object
      required: [type, title, status]
      properties:
        type:     { type: string, format: uri, example: "https://api.example.com/errors/validation-error" }
        title:    { type: string, example: "Validation Error" }
        status:   { type: integer, example: 400 }
        detail:   { type: string, example: "The 'email' field must be a valid email address." }
        instance: { type: string, format: uri, example: "/users/req-abc123" }

  responses:
    BadRequest:
      description: Invalid request parameters
      content:
        application/problem+json:
          schema: { $ref: "#/components/schemas/Problem" }
    Unauthorized:
      description: Missing or invalid authentication
      content:
        application/problem+json:
          schema: { $ref: "#/components/schemas/Problem" }
    NotFound:
      description: Resource not found
      content:
        application/problem+json:
          schema: { $ref: "#/components/schemas/Problem" }
    TooManyRequests:
      description: Rate limit exceeded
      headers:
        Retry-After: { schema: { type: integer } }
      content:
        application/problem+json:
          schema: { $ref: "#/components/schemas/Problem" }

  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - BearerAuth: []
```

### RFC 7807 错误响应（可直接复制）

```json
{
  "type": "https://api.example.com/errors/validation-error",
  "title": "Validation Error",
  "status": 422,
  "detail": "The 'email' field must be a valid email address.",
  "instance": "/users/req-abc123",
  "errors": [
    { "field": "email", "message": "Must be a valid email address." }
  ]
}
```

- 错误响应始终使用 `Content-Type: application/problem+json`。
- `type` 必须是一个稳定且有文档说明的 URI —— 绝不能是泛泛的字符串。
- `detail` 必须人类可读且可指导行动。
- 可通过 `errors[]` 扩展，表达字段级校验失败。

## 输出清单

交付 API 设计时，应提供：
1. 资源模型与关系（图或表）
2. 端点规格，含 URI 与 HTTP 方法
3. OpenAPI 3.1 规格（YAML）
4. 认证与授权流程
5. 错误响应目录（所有 4xx/5xx，均带 `type` URI）
6. 分页与过滤模式
7. 版本化与弃用策略
8. 验证结果：`npx @redocly/cli lint openapi.yaml` 通过且无错误

## 知识参考

REST 架构、OpenAPI 3.1、GraphQL、HTTP 语义、JSON:API、HATEOAS、OAuth 2.0、JWT、RFC 7807 Problem Details、API 版本化模式、分页策略、速率限制（rate limiting）、webhook 设计、SDK 生成

由 [@jeffallan](https://github.com/jeffallan)（[Synergetic Solutions](https://synergetic.solutions) 首席顾问）维护

[文档](https://jeffallan.github.io/claude-skills/skills/api-architecture/api-designer/)
