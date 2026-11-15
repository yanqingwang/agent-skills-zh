> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/plugin-dev/skills/mcp-integration/references/server-types.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# MCP 服务器类型详解

完整参考：Claude Code plugin 支持的所有 MCP 服务器类型。

## stdio（标准输入/输出）

### 概述

以子进程方式运行本地 MCP 服务器，通过 stdin/stdout 通信。本地工具、自定义服务器和 NPM 包的最佳选择。

### 配置

**基础：**
```json
{
  "my-server": {
    "command": "node",
    "args": ["${CLAUDE_PLUGIN_ROOT}/servers/my-server.js"]
  }
}
```

**带环境变量：**
```json
{
  "my-server": {
    "command": "${CLAUDE_PLUGIN_ROOT}/servers/custom-server",
    "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
    "env": {
      "API_KEY": "${MY_API_KEY}",
      "LOG_LEVEL": "debug",
      "DATABASE_URL": "${DB_URL}"
    }
  }
}
```

### 进程生命周期

1. **启动**：Claude Code 用 `command` 和 `args` 启动进程
2. **通信**：通过 stdin/stdout 传输 JSON-RPC 消息
3. **生命周期**：进程在整个 Claude Code 会话期间运行
4. **关闭**：Claude Code 退出时终止进程

### 适用场景

**NPM 包：**
```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
  }
}
```

**自定义脚本：**
```json
{
  "custom": {
    "command": "${CLAUDE_PLUGIN_ROOT}/servers/my-server.js",
    "args": ["--verbose"]
  }
}
```

**Python 服务器：**
```json
{
  "python-server": {
    "command": "python",
    "args": ["-m", "my_mcp_server"],
    "env": {
      "PYTHONUNBUFFERED": "1"
    }
  }
}
```

### 最佳实践

1. **使用绝对路径或 ${CLAUDE_PLUGIN_ROOT}**
2. **为 Python 服务器设置 PYTHONUNBUFFERED**
3. **通过 args 或 env 传配置，不要走 stdin**
4. **妥善处理服务器崩溃**
5. **日志写到 stderr，不要写 stdout（stdout 留给 MCP 协议）**

### 排障

**服务器无法启动：**
- 检查命令存在且可执行
- 确认文件路径正确
- 检查权限
- 查看 `claude --debug` 日志

**通信失败：**
- 确保服务器正确使用 stdin/stdout
- 检查有无多余的 print/console.log 语句
- 核对 JSON-RPC 格式

## SSE（Server-Sent Events）

### 概述

通过 HTTP 连接托管 MCP 服务器，用 server-sent events 做流式传输。最适合云服务和 OAuth 认证。

### 配置

**基础：**
```json
{
  "hosted-service": {
    "type": "sse",
    "url": "https://mcp.example.com/sse"
  }
}
```

**带 header：**
```json
{
  "service": {
    "type": "sse",
    "url": "https://mcp.example.com/sse",
    "headers": {
      "X-API-Version": "v1",
      "X-Client-ID": "${CLIENT_ID}"
    }
  }
}
```

### 连接生命周期

1. **初始化**：与 URL 建立 HTTP 连接
2. **握手**：MCP 协议协商
3. **流式传输**：服务器通过 SSE 发送事件
4. **请求**：客户端用 HTTP POST 发起工具调用
5. **重连**：断开后自动重连

### 认证

**OAuth（自动）：**
```json
{
  "hosted-service": {
    "type": "sse",
    "url": "https://mcp.example.com/sse"
  }
}
```

Claude Code 处理 OAuth 流程：
1. 首次使用时提示用户认证
2. 打开浏览器完成 OAuth 流程
3. 安全存储 token
4. 自动刷新 token

**自定义 Header：**
```json
{
  "service": {
    "type": "sse",
    "url": "https://mcp.example.com/sse",
    "headers": {
      "Authorization": "Bearer ${API_TOKEN}"
    }
  }
}
```

### 适用场景

**官方服务：**
- GitHub: `https://mcp.github.com/sse`
- 其他托管 MCP 服务器

**自定义托管服务器：**
部署自己的 MCP 服务器，通过 HTTPS + SSE 对外提供。

### 最佳实践

1. **始终用 HTTPS，绝不用 HTTP**
2. **可用时让 OAuth 处理认证**
3. **token 放环境变量**
4. **妥善处理连接失败**
5. **写明所需的 OAuth scope**

### 排障

**连接被拒：**
- 检查 URL 正确且可访问
- 确认 HTTPS 证书有效
- 检查网络连通性
- 检查防火墙设置

**OAuth 失败：**
- 清除缓存的 token
- 检查 OAuth scope
- 核对重定向 URL
- 重新认证

## HTTP（REST API）

### 概述

通过标准 HTTP 请求连接 RESTful MCP 服务器。最适合基于 token 的认证和无状态交互。

### 配置

**基础：**
```json
{
  "api": {
    "type": "http",
    "url": "https://api.example.com/mcp"
  }
}
```

**带认证：**
```json
{
  "api": {
    "type": "http",
    "url": "https://api.example.com/mcp",
    "headers": {
      "Authorization": "Bearer ${API_TOKEN}",
      "Content-Type": "application/json",
      "X-API-Version": "2024-01-01"
    }
  }
}
```

### 请求/响应流程

1. **工具发现**：用 GET 发现可用工具
2. **工具调用**：用 POST 传工具名和参数
3. **响应**：JSON 返回结果或错误
4. **无状态**：每个请求相互独立

### 认证

**基于 Token：**
```json
{
  "headers": {
    "Authorization": "Bearer ${API_TOKEN}"
  }
}
```

**API Key：**
```json
{
  "headers": {
    "X-API-Key": "${API_KEY}"
  }
}
```

**自定义认证：**
```json
{
  "headers": {
    "X-Auth-Token": "${AUTH_TOKEN}",
    "X-User-ID": "${USER_ID}"
  }
}
```

### 适用场景

- REST API 后端
- 内部服务
- 微服务
- Serverless 函数

### 最佳实践

1. **所有连接都用 HTTPS**
2. **token 存在环境变量里**
3. **对瞬时失败实现重试逻辑**
4. **处理限流**
5. **设置合理的超时**

### 排障

**HTTP 错误：**
- 401：检查认证 header
- 403：确认权限
- 429：实现限流处理
- 500：查看服务器日志

**超时问题：**
- 必要时调大超时
- 检查服务器性能
- 优化工具实现

## WebSocket（实时）

### 概述

通过 WebSocket 连接 MCP 服务器，实现实时双向通信。最适合流式和低延迟应用。

### 配置

**基础：**
```json
{
  "realtime": {
    "type": "ws",
    "url": "wss://mcp.example.com/ws"
  }
}
```

**带认证：**
```json
{
  "realtime": {
    "type": "ws",
    "url": "wss://mcp.example.com/ws",
    "headers": {
      "Authorization": "Bearer ${TOKEN}",
      "X-Client-ID": "${CLIENT_ID}"
    }
  }
}
```

### 连接生命周期

1. **握手**：WebSocket 升级请求
2. **连接**：持久的双向通道
3. **消息**：WebSocket 上的 JSON-RPC
4. **心跳**：保活消息
5. **重连**：断开时自动进行

### 适用场景

- 实时数据流
- 实时更新与通知
- 协同编辑
- 低延迟工具调用
- 服务器推送通知

### 最佳实践

1. **用 WSS（加密 WebSocket），绝不用 WS**
2. **实现心跳/ping-pong**
3. **实现重连逻辑**
4. **断连期间缓冲消息**
5. **设置连接超时**

### 排障

**连接掉线：**
- 实现重连逻辑
- 检查网络稳定性
- 确认服务器支持 WebSocket
- 检查防火墙设置

**消息送达：**
- 实现消息确认
- 处理乱序消息
- 断连期间缓冲

## 对比矩阵

| 特性 | stdio | SSE | HTTP | WebSocket |
|---------|-------|-----|------|-----------|
| **传输方式** | 进程 | HTTP/SSE | HTTP | WebSocket |
| **方向** | 双向 | 服务器→客户端 | 请求/响应 | 双向 |
| **状态** | 有状态 | 有状态 | 无状态 | 有状态 |
| **认证** | 环境变量 | OAuth/Header | Header | Header |
| **适用场景** | 本地工具 | 云服务 | REST API | 实时 |
| **延迟** | 最低 | 中 | 中 | 低 |
| **配置难度** | 简单 | 中等 | 简单 | 中等 |
| **重连** | 进程重启 | 自动 | 不适用 | 自动 |

## 如何选择类型

**以下情况用 stdio：**
- 运行本地工具或自定义服务器
- 需要最低延迟
- 操作文件系统或本地数据库
- 随 plugin 分发服务器

**以下情况用 SSE：**
- 连接托管服务
- 需要 OAuth 认证
- 使用官方 MCP 服务器（Asana、GitHub）
- 想要自动重连

**以下情况用 HTTP：**
- 集成 REST API
- 需要无状态交互
- 使用基于 token 的认证
- 简单的请求/响应模式

**以下情况用 WebSocket：**
- 需要实时更新
- 构建协同功能
- 低延迟至关重要
- 需要双向流式传输

## 类型间迁移

### 从 stdio 迁移到 SSE

**之前（stdio）：**
```json
{
  "local-server": {
    "command": "node",
    "args": ["server.js"]
  }
}
```

**之后（SSE，先部署服务器）：**
```json
{
  "hosted-server": {
    "type": "sse",
    "url": "https://mcp.example.com/sse"
  }
}
```

### 从 HTTP 迁移到 WebSocket

**之前（HTTP）：**
```json
{
  "api": {
    "type": "http",
    "url": "https://api.example.com/mcp"
  }
}
```

**之后（WebSocket）：**
```json
{
  "realtime": {
    "type": "ws",
    "url": "wss://api.example.com/ws"
  }
}
```

收益：实时更新、更低延迟、双向通信。

## 高级配置

### 多个服务器

组合不同类型：

```json
{
  "local-db": {
    "command": "node",
    "args": ["${CLAUDE_PLUGIN_ROOT}/servers/local-db.js", "--db-path", "${CLAUDE_PLUGIN_DATA}/data.db"]
  },
  "cloud-api": {
    "type": "sse",
    "url": "https://mcp.example.com/sse"
  },
  "internal-service": {
    "type": "http",
    "url": "https://api.example.com/mcp",
    "headers": {
      "Authorization": "Bearer ${API_TOKEN}"
    }
  }
}
```

`${CLAUDE_PLUGIN_DATA}` 是每个 plugin 独立一个文件夹，所有项目共享。plugin 更新后它仍然保留；`${CLAUDE_PLUGIN_ROOT}` 则不会，所以不要把数据存在那里。

### 条件配置

用环境变量切换服务器：

```json
{
  "api": {
    "type": "http",
    "url": "${API_URL}",
    "headers": {
      "Authorization": "Bearer ${API_TOKEN}"
    }
  }
}
```

为开发/生产设置不同的值：
- 开发：`API_URL=http://localhost:8080/mcp`
- 生产：`API_URL=https://api.example.com/mcp`

## 安全注意事项

### stdio 安全

- 校验命令路径
- 不要执行用户提供的命令
- 限制环境变量访问
- 限制文件系统访问

### 网络安全

- 始终使用 HTTPS/WSS
- 校验 SSL 证书
- 不要跳过证书校验
- 安全存储 token

### Token 管理

- 绝不硬编码 token
- 使用环境变量
- 定期轮换 token
- 实现 token 刷新
- 写明所需 scope

## 结语

根据使用场景选择 MCP 服务器类型：
- 本地、自定义或 NPM 打包的服务器用 **stdio**
- 需要 OAuth 的托管服务用 **SSE**
- 带 token 认证的 REST API 用 **HTTP**
- 实时双向通信用 **WebSocket**

充分测试、妥善处理错误，才能实现稳健的 MCP 集成。
