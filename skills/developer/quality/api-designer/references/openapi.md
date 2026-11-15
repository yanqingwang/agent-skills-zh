> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/api-designer/references/openapi.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# OpenAPI 3.1 规格

## 什么是 OpenAPI？

OpenAPI（前身为 Swagger）是描述 REST API 的标准。它支持：
- 交互式文档
- 代码生成（SDK、客户端、服务端）
- API 测试工具
- 契约校验
- mock 服务器

## 基本结构

### 最小 OpenAPI 3.1 规格

```yaml
openapi: 3.1.0
info:
  title: My API
  version: 1.0.0
  description: A sample API
  contact:
    name: API Support
    email: support@example.com
    url: https://example.com/support
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html

servers:
  - url: https://api.example.com/v1
    description: Production server
  - url: https://staging-api.example.com/v1
    description: Staging server
  - url: http://localhost:3000/v1
    description: Local development

paths:
  /users:
    get:
      summary: List users
      description: Retrieve a paginated list of users
      operationId: listUsers
      tags:
        - Users
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'

components:
  schemas:
    User:
      type: object
      required:
        - id
        - email
      properties:
        id:
          type: integer
          format: int64
          example: 123
        email:
          type: string
          format: email
          example: john@example.com
        name:
          type: string
          example: John Doe
```

## Info 对象

API 的元数据：

```yaml
info:
  title: Users API
  version: 1.0.0
  description: |
    # Users API

    This API manages user accounts and profiles.

    ## Features
    - User CRUD operations
    - Authentication with JWT
    - Role-based authorization

  termsOfService: https://example.com/terms

  contact:
    name: API Support Team
    email: api-support@example.com
    url: https://example.com/support

  license:
    name: MIT
    url: https://opensource.org/licenses/MIT

  x-api-id: users-api-v1
  x-audience: external
```

## 服务器（Servers）

定义 API 基础 URL：

```yaml
servers:
  - url: https://api.example.com/v1
    description: Production
    variables:
      version:
        default: v1
        enum:
          - v1
          - v2

  - url: https://{environment}.example.com/v1
    description: Dynamic environment
    variables:
      environment:
        default: api
        enum:
          - api
          - staging
          - dev
```

## 路径与操作

### 完整端点示例

```yaml
paths:
  /users:
    get:
      summary: List users
      description: Retrieve a paginated list of users with optional filtering
      operationId: listUsers
      tags:
        - Users

      parameters:
        - name: offset
          in: query
          description: Number of items to skip
          required: false
          schema:
            type: integer
            minimum: 0
            default: 0

        - name: limit
          in: query
          description: Maximum number of items to return
          required: false
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20

        - name: status
          in: query
          description: Filter by user status
          required: false
          schema:
            type: string
            enum:
              - active
              - inactive
              - suspended

      security:
        - bearerAuth: []

      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserListResponse'
              examples:
                success:
                  $ref: '#/components/examples/UserListSuccess'

        '401':
          $ref: '#/components/responses/Unauthorized'

        '429':
          $ref: '#/components/responses/RateLimitExceeded'

    post:
      summary: Create user
      description: Create a new user account
      operationId: createUser
      tags:
        - Users

      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
            examples:
              basic:
                $ref: '#/components/examples/CreateUserBasic'

      responses:
        '201':
          description: User created successfully
          headers:
            Location:
              description: URL of the created user
              schema:
                type: string
                format: uri
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'

        '400':
          $ref: '#/components/responses/ValidationError'

        '409':
          description: User already exists
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /users/{userId}:
    parameters:
      - name: userId
        in: path
        description: User ID
        required: true
        schema:
          type: integer
          format: int64

    get:
      summary: Get user
      description: Retrieve a specific user by ID
      operationId: getUser
      tags:
        - Users

      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'

        '404':
          $ref: '#/components/responses/NotFound'

    put:
      summary: Update user
      description: Replace user data
      operationId: updateUser
      tags:
        - Users

      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateUserRequest'

      responses:
        '200':
          description: User updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'

        '404':
          $ref: '#/components/responses/NotFound'

    delete:
      summary: Delete user
      description: Delete a user account
      operationId: deleteUser
      tags:
        - Users

      responses:
        '204':
          description: User deleted successfully

        '404':
          $ref: '#/components/responses/NotFound'
```

## 组件（Components）

API 规格中可复用的组件。

### Schema（Schemas）

```yaml
components:
  schemas:
    User:
      type: object
      required:
        - id
        - email
        - name
      properties:
        id:
          type: integer
          format: int64
          readOnly: true
          example: 123
        email:
          type: string
          format: email
          example: john@example.com
        name:
          type: string
          minLength: 1
          maxLength: 100
          example: John Doe
        status:
          type: string
          enum:
            - active
            - inactive
            - suspended
          default: active
        created_at:
          type: string
          format: date-time
          readOnly: true
          example: "2024-01-15T10:30:00Z"
        metadata:
          type: object
          additionalProperties:
            type: string

    CreateUserRequest:
      type: object
      required:
        - email
        - name
      properties:
        email:
          type: string
          format: email
        name:
          type: string
          minLength: 1
          maxLength: 100
        metadata:
          type: object
          additionalProperties:
            type: string

    UserListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/User'
        pagination:
          $ref: '#/components/schemas/Pagination'

    Pagination:
      type: object
      properties:
        offset:
          type: integer
          minimum: 0
        limit:
          type: integer
          minimum: 1
        total:
          type: integer
          minimum: 0
        has_more:
          type: boolean

    Error:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          required:
            - code
            - message
          properties:
            code:
              type: string
              example: RESOURCE_NOT_FOUND
            message:
              type: string
              example: User with ID 123 not found
            details:
              type: object
            request_id:
              type: string
              example: req_abc123
```

### 安全方案（Security Schemes）

```yaml
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: JWT access token

    apiKey:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key for authentication

    oauth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://auth.example.com/oauth/authorize
          tokenUrl: https://auth.example.com/oauth/token
          scopes:
            users:read: Read user data
            users:write: Create and update users
            users:delete: Delete users
```

全局或按操作应用安全设置：

```yaml
# Global security
security:
  - bearerAuth: []

# Or per-operation
paths:
  /users:
    get:
      security:
        - bearerAuth: []
        - apiKey: []  # Alternative auth method
```

### 响应（Responses）

可复用的响应定义：

```yaml
components:
  responses:
    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error:
              code: RESOURCE_NOT_FOUND
              message: The requested resource was not found

    Unauthorized:
      description: Authentication required
      headers:
        WWW-Authenticate:
          schema:
            type: string
          description: Authentication method
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'

    ValidationError:
      description: Validation failed
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error:
              code: VALIDATION_ERROR
              message: Request validation failed
              details:
                - field: email
                  code: INVALID_FORMAT
                  message: Email must be a valid email address

    RateLimitExceeded:
      description: Rate limit exceeded
      headers:
        X-RateLimit-Limit:
          schema:
            type: integer
          description: Request limit per hour
        X-RateLimit-Remaining:
          schema:
            type: integer
          description: Remaining requests
        X-RateLimit-Reset:
          schema:
            type: integer
            format: int64
          description: Time when limit resets (Unix timestamp)
        Retry-After:
          schema:
            type: integer
          description: Seconds to wait before retry
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
```

### 示例（Examples）

```yaml
components:
  examples:
    UserListSuccess:
      summary: Successful user list response
      value:
        data:
          - id: 1
            email: john@example.com
            name: John Doe
            status: active
            created_at: "2024-01-15T10:30:00Z"
          - id: 2
            email: jane@example.com
            name: Jane Smith
            status: active
            created_at: "2024-01-16T14:20:00Z"
        pagination:
          offset: 0
          limit: 20
          total: 150
          has_more: true

    CreateUserBasic:
      summary: Create user with minimal fields
      value:
        email: newuser@example.com
        name: New User
```

## 数据类型

### 基本类型

```yaml
# String
type: string
example: "Hello World"

# String with format
type: string
format: email
example: "user@example.com"

# Integer
type: integer
format: int64
example: 123

# Number (float)
type: number
format: double
example: 99.99

# Boolean
type: boolean
example: true

# Date-time
type: string
format: date-time
example: "2024-01-15T10:30:00Z"

# Date
type: string
format: date
example: "2024-01-15"

# UUID
type: string
format: uuid
example: "550e8400-e29b-41d4-a716-446655440000"

# URI
type: string
format: uri
example: "https://example.com/users/123"
```

### 数组

```yaml
type: array
items:
  type: string
minItems: 1
maxItems: 10
uniqueItems: true
example: ["tag1", "tag2", "tag3"]

# Array of objects
type: array
items:
  $ref: '#/components/schemas/User'
```

### 对象

```yaml
type: object
required:
  - name
  - email
properties:
  name:
    type: string
  email:
    type: string
    format: email
  age:
    type: integer
    minimum: 0
    maximum: 120

# Additional properties
additionalProperties: false  # Strict - no extra properties
additionalProperties: true   # Allow any extra properties
additionalProperties:        # Extra properties must be strings
  type: string
```

### 枚举

```yaml
type: string
enum:
  - active
  - inactive
  - suspended
default: active
```

### OneOf / AnyOf / AllOf

```yaml
# OneOf - exactly one schema matches
oneOf:
  - $ref: '#/components/schemas/CreditCard'
  - $ref: '#/components/schemas/BankAccount'

# AnyOf - one or more schemas match
anyOf:
  - $ref: '#/components/schemas/User'
  - $ref: '#/components/schemas/Organization'

# AllOf - all schemas must match (inheritance)
allOf:
  - $ref: '#/components/schemas/BaseUser'
  - type: object
    properties:
      admin_level:
        type: integer
```

## 校验

### 字符串校验

```yaml
type: string
minLength: 1
maxLength: 100
pattern: "^[a-zA-Z0-9_-]+$"
format: email
```

### 数字校验

```yaml
type: integer
minimum: 0
maximum: 100
exclusiveMinimum: true  # > 0 instead of >= 0
multipleOf: 5
```

### 数组校验

```yaml
type: array
minItems: 1
maxItems: 10
uniqueItems: true
```

## 标签（Tags）

将端点组织为逻辑分组：

```yaml
tags:
  - name: Users
    description: User management operations
  - name: Orders
    description: Order management
  - name: Products
    description: Product catalog

paths:
  /users:
    get:
      tags:
        - Users
```

## 文档

### Markdown 支持

```yaml
description: |
  # User Management

  This endpoint allows you to manage users.

  ## Features
  - Create users
  - Update profiles
  - Delete accounts

  ## Authentication
  Requires JWT bearer token.

  ## Example
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```
```

## 代码生成

从 OpenAPI 规格生成 SDK：

```bash
# Generate TypeScript client
openapi-generator-cli generate \
  -i openapi.yaml \
  -g typescript-axios \
  -o ./client

# Generate Python client
openapi-generator-cli generate \
  -i openapi.yaml \
  -g python \
  -o ./python-client

# Generate server stub
openapi-generator-cli generate \
  -i openapi.yaml \
  -g nodejs-express-server \
  -o ./server
```

## 校验工具

校验 OpenAPI 规格：

```bash
# Using Swagger CLI
swagger-cli validate openapi.yaml

# Using Spectral (advanced linting)
spectral lint openapi.yaml
```

## 最佳实践

1. **使用组件** - 复用 Schema、响应与参数
2. **添加示例** - 为所有 Schema 提供贴近真实的示例
3. **充分编写文档** - 覆盖每个端点、参数、响应
4. **为规格做版本管理** - 跟踪规格文档的变更
5. **定期校验** - 用工具捕获错误
6. **使用 $ref** - 引用组件而非重复复制
7. **包含错误响应** - 记录所有可能的错误
8. **添加 operationId** - 为每个操作提供唯一 ID（供代码生成使用）
9. **为端点打标签** - 组织成逻辑分组
10. **提供安全方案** - 清晰记录认证方式
