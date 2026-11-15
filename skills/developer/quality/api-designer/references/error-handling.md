> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/api-designer/references/error-handling.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# API 错误处理

## 错误响应设计

一致且信息充分的错误响应，对 API 可用性至关重要。

## 标准错误格式

### 基础错误响应

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "User with ID 123 not found",
    "details": null
  }
}
```

### RFC 7807 Problem Details

标准化错误格式（application/problem+json）：

```http
HTTP/1.1 404 Not Found
Content-Type: application/problem+json

{
  "type": "https://api.example.com/errors/resource-not-found",
  "title": "Resource Not Found",
  "status": 404,
  "detail": "User with ID 123 does not exist",
  "instance": "/users/123"
}
```

**字段：**
- `type` - 标识错误类型的 URI 引用
- `title` - 简短、人类可读的摘要
- `status` - HTTP 状态码
- `detail` - 针对本次错误的人类可读说明
- `instance` - 本次具体错误的 URI 引用

### 扩展错误响应

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      {
        "field": "email",
        "code": "INVALID_FORMAT",
        "message": "Email must be a valid email address"
      },
      {
        "field": "age",
        "code": "OUT_OF_RANGE",
        "message": "Age must be between 18 and 120"
      }
    ],
    "request_id": "req_123456",
    "timestamp": "2024-01-15T10:30:00Z",
    "documentation_url": "https://api.example.com/docs/errors#validation-error"
  }
}
```

## 错误分类

### 1. 验证错误（400 Bad Request）

客户端发送了无效数据。

```http
POST /users
Content-Type: application/json

{
  "name": "",
  "email": "invalid-email",
  "age": 15
}

Response: 400 Bad Request
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      {
        "field": "name",
        "code": "REQUIRED",
        "message": "Name is required"
      },
      {
        "field": "email",
        "code": "INVALID_FORMAT",
        "message": "Email must be a valid email address"
      },
      {
        "field": "age",
        "code": "OUT_OF_RANGE",
        "message": "Age must be at least 18",
        "constraints": {
          "min": 18,
          "max": 120
        }
      }
    ]
  }
}
```

### 2. 认证错误（401 Unauthorized）

认证凭据缺失或无效。

```http
GET /users/123
Authorization: Bearer <invalid-access-token>

Response: 401 Unauthorized
WWW-Authenticate: Bearer realm="api", error="invalid_token"

{
  "error": {
    "code": "INVALID_TOKEN",
    "message": "The access token is invalid or has expired",
    "details": {
      "reason": "token_expired",
      "expired_at": "2024-01-15T10:00:00Z"
    }
  }
}
```

**常见认证错误码：**
- `MISSING_TOKEN` - 未提供认证令牌
- `INVALID_TOKEN` - 令牌格式错误或无效
- `EXPIRED_TOKEN` - 令牌已过期
- `REVOKED_TOKEN` - 令牌已被吊销

### 3. 授权错误（403 Forbidden）

已认证，但无权执行该操作。

```http
DELETE /users/123
Authorization: Bearer <access-token>

Response: 403 Forbidden
{
  "error": {
    "code": "INSUFFICIENT_PERMISSIONS",
    "message": "You do not have permission to delete this user",
    "details": {
      "required_permission": "users:delete",
      "your_permissions": ["users:read", "users:update"]
    }
  }
}
```

### 4. 未找到错误（404 Not Found）

资源不存在。

```http
GET /users/99999

Response: 404 Not Found
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "User with ID 99999 not found",
    "details": {
      "resource_type": "User",
      "resource_id": "99999"
    }
  }
}
```

### 5. 冲突错误（409 Conflict）

请求与当前状态冲突。

```http
POST /users
Content-Type: application/json

{
  "email": "existing@example.com",
  "name": "John Doe"
}

Response: 409 Conflict
{
  "error": {
    "code": "RESOURCE_ALREADY_EXISTS",
    "message": "User with email 'existing@example.com' already exists",
    "details": {
      "field": "email",
      "value": "existing@example.com",
      "existing_resource": "/users/123"
    }
  }
}
```

### 6. 速率限制（429 Too Many Requests）

客户端超出了速率限制。

```http
GET /users

Response: 429 Too Many Requests
Retry-After: 60
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1705320000

{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "You have exceeded the rate limit",
    "details": {
      "limit": 100,
      "window": "1 hour",
      "retry_after": 60,
      "reset_at": "2024-01-15T11:00:00Z"
    }
  }
}
```

### 7. 服务器错误（500 Internal Server Error）

意外的服务器错误。

```http
GET /users/123

Response: 500 Internal Server Error
{
  "error": {
    "code": "INTERNAL_SERVER_ERROR",
    "message": "An unexpected error occurred. Please try again later.",
    "request_id": "req_123456",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

**绝不暴露：**
- 堆栈跟踪
- 数据库错误
- 内部路径
- 敏感配置

### 8. 服务不可用（503 Service Unavailable）

服务暂时不可用。

```http
GET /users

Response: 503 Service Unavailable
Retry-After: 300

{
  "error": {
    "code": "SERVICE_UNAVAILABLE",
    "message": "Service is temporarily unavailable due to maintenance",
    "details": {
      "retry_after": 300,
      "maintenance_end": "2024-01-15T12:00:00Z"
    }
  }
}
```

## 错误码目录

为你的 API 定义标准错误码：

```json
{
  "VALIDATION_ERROR": {
    "status": 400,
    "description": "Request validation failed",
    "subcodes": {
      "REQUIRED": "Required field is missing",
      "INVALID_FORMAT": "Field has invalid format",
      "OUT_OF_RANGE": "Value is out of allowed range",
      "INVALID_ENUM": "Value is not in allowed set"
    }
  },
  "AUTHENTICATION_ERROR": {
    "status": 401,
    "description": "Authentication failed",
    "subcodes": {
      "MISSING_TOKEN": "No authentication token provided",
      "INVALID_TOKEN": "Token is invalid",
      "EXPIRED_TOKEN": "Token has expired"
    }
  },
  "AUTHORIZATION_ERROR": {
    "status": 403,
    "description": "Insufficient permissions",
    "subcodes": {
      "INSUFFICIENT_PERMISSIONS": "Missing required permission",
      "RESOURCE_FORBIDDEN": "Access to resource is forbidden"
    }
  },
  "RESOURCE_NOT_FOUND": {
    "status": 404,
    "description": "Resource not found"
  },
  "CONFLICT_ERROR": {
    "status": 409,
    "description": "Request conflicts with current state",
    "subcodes": {
      "RESOURCE_ALREADY_EXISTS": "Resource already exists",
      "CONCURRENT_MODIFICATION": "Resource was modified by another request"
    }
  },
  "RATE_LIMIT_EXCEEDED": {
    "status": 429,
    "description": "Rate limit exceeded"
  },
  "INTERNAL_SERVER_ERROR": {
    "status": 500,
    "description": "Internal server error"
  }
}
```

## 验证错误明细

### 字段级验证

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      {
        "field": "credit_card.number",
        "code": "INVALID_FORMAT",
        "message": "Credit card number must be 16 digits",
        "value_provided": "1234",
        "constraints": {
          "pattern": "^[0-9]{16}$"
        }
      },
      {
        "field": "items[0].quantity",
        "code": "OUT_OF_RANGE",
        "message": "Quantity must be at least 1",
        "value_provided": 0,
        "constraints": {
          "min": 1,
          "max": 1000
        }
      }
    ]
  }
}
```

### 跨字段验证

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      {
        "fields": ["start_date", "end_date"],
        "code": "INVALID_RANGE",
        "message": "End date must be after start date",
        "values_provided": {
          "start_date": "2024-01-20",
          "end_date": "2024-01-15"
        }
      }
    ]
  }
}
```

## 请求 ID 追踪

始终包含请求 ID，便于调试：

```http
Response Headers:
X-Request-ID: req_abc123

Response Body:
{
  "error": {
    "code": "INTERNAL_SERVER_ERROR",
    "message": "An unexpected error occurred",
    "request_id": "req_abc123"
  }
}
```

客户端可在支持工单中引用请求 ID。

## 错误文档

为每个端点记录所有可能的错误：

```yaml
/users/{id}:
  get:
    responses:
      '200':
        description: Success
      '401':
        description: Authentication failed
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Error'
            examples:
              missing_token:
                value:
                  error:
                    code: MISSING_TOKEN
                    message: No authentication token provided
              invalid_token:
                value:
                  error:
                    code: INVALID_TOKEN
                    message: Token is invalid or expired
      '404':
        description: User not found
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Error'
            examples:
              not_found:
                value:
                  error:
                    code: RESOURCE_NOT_FOUND
                    message: User with ID 123 not found
```

## 重试指引

帮助客户端判断是否应该重试：

```json
{
  "error": {
    "code": "SERVICE_UNAVAILABLE",
    "message": "Service temporarily unavailable",
    "retry": {
      "retryable": true,
      "retry_after": 60,
      "max_retries": 3,
      "backoff": "exponential"
    }
  }
}
```

### 可重试错误

- 408 Request Timeout
- 429 Too Many Requests（带 Retry-After）
- 500 Internal Server Error（某些情况下）
- 502 Bad Gateway
- 503 Service Unavailable
- 504 Gateway Timeout

### 不可重试错误

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Unprocessable Entity

## 多语言支持

支持多语言的错误消息：

```http
GET /users/invalid
Accept-Language: es

Response: 404 Not Found
Content-Language: es
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Usuario con ID 'invalid' no encontrado"
  }
}
```

始终返回 `code` 字段，客户端可据此自行实现翻译。

## 最佳实践

1. **使用标准 HTTP 状态码** - 不要对错误返回 200
2. **提供机器可读的错误码** - 供客户端逻辑判断
3. **提供人类可读的消息** - 说明清晰
4. **具体但安全** - 不暴露敏感信息
5. **带上请求 ID** - 用于追踪与调试
6. **记录所有错误** - 每个端点的每种可能错误
7. **保持一致** - 所有端点用同一格式
8. **帮助客户端重试** - 指明错误是否可重试
9. **尽早验证** - 立即返回验证错误
10. **在服务端记录错误日志** - 用于监控追踪

## 反模式

避免这些错误：

- **笼统的错误消息** - 只说"发生错误"而没有细节
- **暴露堆栈跟踪** - 安全风险
- **错误格式不一致** - 每个端点结构不同
- **缺少错误码** - 只有人类可读消息
- **状态码错误** - 返回 200 却在 body 里报错
- **没有请求 ID** - 让调试无从下手
- **错误未写入文档** - 客户端不知道会发生什么
- **信息过多** - 暴露内部实现
