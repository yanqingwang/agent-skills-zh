> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/plugin-dev/skills/mcp-integration/references/authentication.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# MCP 认证模式

完整指南：Claude Code plugin 中 MCP 服务器的各种认证方式。

## 概述

MCP 服务器支持多种认证方式，取决于服务器类型和服务要求。请选择最贴合你的使用场景与安全要求的方案。

## OAuth（自动）

### 工作原理

对 SSE 和 HTTP 服务器，Claude Code 会自动处理完整的 OAuth 2.0 流程：

1. 用户尝试使用 MCP 工具
2. Claude Code 检测到需要认证
3. 打开浏览器进行 OAuth 同意
4. 用户在浏览器中完成授权
5. Claude Code 安全存储 token
6. 自动刷新 token

### 配置

```json
{
  "service": {
    "type": "sse",
    "url": "https://mcp.example.com/sse"
  }
}
```

无需额外的认证配置！Claude Code 全部搞定。

### 支持的服务

**已知的支持 OAuth 的 MCP 服务器：**
- GitHub（如可用）
- Google 服务（如可用）
- 自定义 OAuth 服务器

### OAuth Scope

OAuth scope 由 MCP 服务器决定。用户会在同意流程中看到所需的 scope。

**在 README 中写明所需的 scope：**
```markdown
## Authentication

This plugin requires the following Asana permissions:
- Read tasks and projects
- Create and update tasks
- Access workspace data
```

### Token 存储

Claude Code 安全地存储 token：
- plugin 无法访问
- 静态加密存储
- 自动刷新
- 登出时清除

### OAuth 排障

**认证死循环：**
- 清除缓存的 token（登出后重新登录）
- 检查 OAuth 重定向 URL
- 核对服务器的 OAuth 配置

**Scope 问题：**
- 新增 scope 时用户可能需要重新授权
- 查阅服务器文档确认所需的 scope

**Token 过期：**
- Claude Code 会自动刷新
- 刷新失败时会提示重新认证

## 基于 Token 的认证

### Bearer Token

HTTP 和 WebSocket 服务器最常用这种方式。

**配置：**
```json
{
  "api": {
    "type": "http",
    "url": "https://api.example.com/mcp",
    "headers": {
      "Authorization": "Bearer ${API_TOKEN}"
    }
  }
}
```

**环境变量：**
```bash
export API_TOKEN="your-secret-token-here"
```

### API Key

Bearer token 的替代方案，通常放在自定义 header 中。

**配置：**
```json
{
  "api": {
    "type": "http",
    "url": "https://api.example.com/mcp",
    "headers": {
      "X-API-Key": "${API_KEY}",
      "X-API-Secret": "${API_SECRET}"
    }
  }
}
```

### 自定义 Header

有些服务会使用自定义认证 header。

**配置：**
```json
{
  "service": {
    "type": "sse",
    "url": "https://mcp.example.com/sse",
    "headers": {
      "X-Auth-Token": "${AUTH_TOKEN}",
      "X-User-ID": "${USER_ID}",
      "X-Tenant-ID": "${TENANT_ID}"
    }
  }
}
```

### 编写 Token 要求文档

务必在 README 中写明：

```markdown
## Setup

### Required Environment Variables

Set these environment variables before using the plugin:

\`\`\`bash
export API_TOKEN="your-token-here"
export API_SECRET="your-secret-here"
\`\`\`

### Obtaining Tokens

1. Visit https://api.example.com/tokens
2. Create a new API token
3. Copy the token and secret
4. Set environment variables as shown above

### Token Permissions

The API token needs the following permissions:
- Read access to resources
- Write access for creating items
- Delete access (optional, for cleanup operations)
\`\`\`
```

## 环境变量认证（stdio）

### 向服务器传递凭证

stdio 服务器通过环境变量传递凭证：

```json
{
  "database": {
    "command": "python",
    "args": ["-m", "mcp_server_db"],
    "env": {
      "DATABASE_URL": "${DATABASE_URL}",
      "DB_USER": "${DB_USER}",
      "DB_PASSWORD": "${DB_PASSWORD}"
    }
  }
}
```

### 用户环境变量

```bash
# User sets these in their shell
export DATABASE_URL="postgresql://localhost/mydb"
export DB_USER="myuser"
export DB_PASSWORD="mypassword"
```

### 文档模板

```markdown
## Database Configuration

Set these environment variables:

\`\`\`bash
export DATABASE_URL="postgresql://host:port/database"
export DB_USER="username"
export DB_PASSWORD="password"
\`\`\`

Or create a `.env` file (add to `.gitignore`):

\`\`\`
DATABASE_URL=postgresql://localhost:5432/mydb
DB_USER=myuser
DB_PASSWORD=mypassword
\`\`\`

Load with: \`source .env\` or \`export $(cat .env | xargs)\`
\`\`\`
```

## 动态 Header

### Headers 辅助脚本

token 会变化或会过期时，使用辅助脚本：

```json
{
  "api": {
    "type": "sse",
    "url": "https://api.example.com",
    "headersHelper": "${CLAUDE_PLUGIN_ROOT}/scripts/get-headers.sh"
  }
}
```

**脚本（get-headers.sh）：**
```bash
#!/bin/bash
# Generate dynamic authentication headers

# Fetch fresh token
TOKEN=$(get-fresh-token-from-somewhere)

# Output JSON headers
cat <<EOF
{
  "Authorization": "Bearer $TOKEN",
  "X-Timestamp": "$(date -Iseconds)"
}
EOF
```

### 动态 Header 的适用场景

- 需要刷新的短时效 token
- 带 HMAC 签名的 token
- 基于时间的认证
- 动态选择租户/工作区

## 安全最佳实践

### 应该做

✅ **使用环境变量：**
```json
{
  "headers": {
    "Authorization": "Bearer ${API_TOKEN}"
  }
}
```

✅ **在 README 中写明所需的变量**

✅ **始终使用 HTTPS/WSS**

✅ **实现 token 轮换**

✅ **安全存储 token（用环境变量，不要用文件）**

✅ **可用时让 OAuth 处理认证**

### 不要做

❌ **硬编码 token：**
```json
{
  "headers": {
    "Authorization": "Bearer sk-abc123..."  // NEVER!
  }
}
```

❌ **把 token 提交到 git**

❌ **在文档中分享 token**

❌ **用 HTTP 代替 HTTPS**

❌ **把 token 存进 plugin 文件**

❌ **在日志中输出 token 或敏感 header**

## 多租户模式

### 工作区/租户选择

**通过环境变量：**
```json
{
  "api": {
    "type": "http",
    "url": "https://api.example.com/mcp",
    "headers": {
      "Authorization": "Bearer ${API_TOKEN}",
      "X-Workspace-ID": "${WORKSPACE_ID}"
    }
  }
}
```

**通过 URL：**
```json
{
  "api": {
    "type": "http",
    "url": "https://${TENANT_ID}.api.example.com/mcp"
  }
}
```

### 每用户配置

用户各自设置自己的工作区：

```bash
export WORKSPACE_ID="my-workspace-123"
export TENANT_ID="my-company"
```

## 认证排障

### 常见问题

**401 Unauthorized：**
- 检查 token 是否设置正确
- 确认 token 未过期
- 检查 token 是否具备所需权限
- 确认 header 格式正确

**403 Forbidden：**
- token 有效但缺少权限
- 检查 scope/权限
- 核对工作区/租户 ID
- 可能需要管理员批准

**找不到 token：**
```bash
# Check environment variable is set
echo $API_TOKEN

# If empty, set it
export API_TOKEN="your-token"
```

**Token 格式错误：**
```json
// Correct
"Authorization": "Bearer sk-abc123"

// Wrong
"Authorization": "sk-abc123"
```

### 调试认证

**启用调试模式：**
```bash
claude --debug
```

关注以下输出：
- 认证 header 的值（已脱敏）
- OAuth 流程进度
- token 刷新尝试
- 认证错误

**单独测试认证：**
```bash
# Test HTTP endpoint
curl -H "Authorization: Bearer $API_TOKEN" \
     https://api.example.com/mcp/health

# Should return 200 OK
```

## 迁移模式

### 从硬编码迁移到环境变量

**之前：**
```json
{
  "headers": {
    "Authorization": "Bearer sk-hardcoded-token"
  }
}
```

**之后：**
```json
{
  "headers": {
    "Authorization": "Bearer ${API_TOKEN}"
  }
}
```

**迁移步骤：**
1. 在 plugin README 中添加环境变量说明
2. 更新配置，改用 ${VAR}
3. 设置变量后测试
4. 移除硬编码的值
5. 提交变更

### 从 Basic Auth 迁移到 OAuth

**之前：**
```json
{
  "headers": {
    "Authorization": "Basic ${BASE64_CREDENTIALS}"
  }
}
```

**之后：**
```json
{
  "type": "sse",
  "url": "https://mcp.example.com/sse"
}
```

**收益：**
- 安全性更好
- 无需管理凭证
- 自动刷新 token
- 权限按 scope 限定

## 高级认证

### 双向 TLS（mTLS）

有些企业服务要求客户端证书。

**MCP 配置不直接支持。**

**变通方案：** 用一个处理 mTLS 的 stdio 服务器包装：

```json
{
  "secure-api": {
    "command": "${CLAUDE_PLUGIN_ROOT}/servers/mtls-wrapper",
    "args": ["--cert", "${CLIENT_CERT}", "--key", "${CLIENT_KEY}"],
    "env": {
      "API_URL": "https://secure.example.com"
    }
  }
}
```

### JWT Token

用 headers helper 动态生成 JWT token：

```bash
#!/bin/bash
# generate-jwt.sh

# Generate JWT (using library or API call)
JWT=$(generate-jwt-token)

echo "{\"Authorization\": \"Bearer $JWT\"}"
```

```json
{
  "headersHelper": "${CLAUDE_PLUGIN_ROOT}/scripts/generate-jwt.sh"
}
```

### HMAC 签名

对要求请求签名的 API：

```bash
#!/bin/bash
# generate-hmac.sh

TIMESTAMP=$(date -Iseconds)
SIGNATURE=$(echo -n "$TIMESTAMP" | openssl dgst -sha256 -hmac "$SECRET_KEY" | cut -d' ' -f2)

cat <<EOF
{
  "X-Timestamp": "$TIMESTAMP",
  "X-Signature": "$SIGNATURE",
  "X-API-Key": "$API_KEY"
}
EOF
```

## 最佳实践小结

### 面向 plugin 开发者

1. 服务支持时**优先用 OAuth**
2. token 用**环境变量**
3. 在 README 中**写明所有必需变量**
4. **提供配置说明**并附示例
5. **绝不提交凭证**
6. **只用 HTTPS/WSS**
7. **充分测试认证**

### 面向 plugin 用户

1. 使用 plugin 前**先设置环境变量**
2. **妥善保管 token**，不要外泄
3. **定期轮换 token**
4. 开发/生产**使用不同的 token**
5. **不要把 .env 文件提交**到 git
6. 授权前**审查 OAuth scope**

## 结语

根据你的 MCP 服务器要求选择认证方式：
- 云服务用 **OAuth**（对用户最省事）
- API 服务用 **Bearer token**
- stdio 服务器用**环境变量**
- 复杂认证流程用**动态 header**

始终把安全放在首位，并为用户提供清晰的配置文档。
