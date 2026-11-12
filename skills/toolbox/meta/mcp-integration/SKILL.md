---
name: mcp-integration
description: 当用户要求 "add MCP server"、"integrate MCP"、"configure MCP in plugin"、"use .mcp.json"、"set up Model Context Protocol"、"connect external service"，提到 "${CLAUDE_PLUGIN_ROOT} with MCP"，或讨论 MCP 服务器类型（SSE、stdio、HTTP、WebSocket）时，应使用本 Skill。为把 Model Context Protocol 服务器集成到 Claude Code plugin 以实现外部工具与服务集成提供全面指导。
version: 0.1.0
---

> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/plugin-dev/skills/mcp-integration/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 面向 Claude Code plugin 的 MCP 集成

## 概述

Model Context Protocol（MCP）通过提供结构化的工具访问能力，让 Claude Code plugin 能够集成外部服务与 API。使用 MCP 集成，把外部服务的能力作为工具暴露在 Claude Code 中。

**核心能力：**
- 连接外部服务（数据库、API、文件系统）
- 从单一服务提供 10 个以上相关工具
- 处理 OAuth 和复杂的认证流程
- 将 MCP 服务器与 plugin 捆绑以实现自动配置

## MCP 服务器配置方式

plugin 可以通过两种方式捆绑 MCP 服务器：

### 方式 1：专用 .mcp.json（推荐）

在 plugin 根目录创建 `.mcp.json`：


```json
{
  "database-tools": {
    "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
    "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
    "env": {
      "DB_URL": "${DB_URL}"
    }
  }
}
```


**优点：**
- 关注点清晰分离
- 更易维护
- 更适合多个服务器

### 方式 2：内联在 plugin.json 中

在 plugin.json 中添加 `mcpServers` 字段：


```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "mcpServers": {
    "plugin-api": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/api-server",
      "args": ["--port", "8080"]
    }
  }
}
```


**优点：**
- 单一配置文件
- 适合简单的单服务器 plugin

## MCP 服务器类型

### stdio（本地进程）

将本地 MCP 服务器作为子进程执行。最适合本地工具和自定义服务器。

**配置：**

```json
{
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/path"],
    "env": {
      "LOG_LEVEL": "debug"
    }
  }
}
```


**使用场景：**
- 文件系统访问
- 本地数据库连接
- 自定义 MCP 服务器
- NPM 打包的 MCP 服务器

**进程管理：**
- Claude Code 启动并管理该进程
- 通过 stdin/stdout 通信
- Claude Code 退出时终止

### SSE（Server-Sent Events）

连接到支持 OAuth 的托管 MCP 服务器。最适合云服务。

**配置：**

```json
{
  "hosted-service": {
    "type": "sse",
    "url": "https://mcp.example.com/sse"
  }
}
```


**使用场景：**
- 官方托管 MCP 服务器（Asana、GitHub 等）
- 带 MCP 端点的云服务
- 基于 OAuth 的认证
- 无需本地安装

**认证：**
- OAuth 流程自动处理
- 首次使用时提示用户
- token 由 Claude Code 管理

### HTTP（REST API）

连接到使用 token 认证的 RESTful MCP 服务器。

**配置：**

```json
{
  "api-service": {
    "type": "http",
    "url": "https://api.example.com/mcp",
    "headers": {
      "Authorization": "Bearer ${API_TOKEN}",
      "X-Custom-Header": "value"
    }
  }
}
```


**使用场景：**
- 基于 REST API 的 MCP 服务器
- 基于 token 的认证
- 自定义 API 后端
- 无状态交互

### WebSocket（实时）

连接到 WebSocket MCP 服务器，实现实时双向通信。

**配置：**

```json
{
  "realtime-service": {
    "type": "ws",
    "url": "wss://mcp.example.com/ws",
    "headers": {
      "Authorization": "Bearer ${TOKEN}"
    }
  }
}
```


**使用场景：**
- 实时数据流
- 持久连接
- 来自服务器的推送通知
- 低延迟要求

## 环境变量展开

所有 MCP 配置都支持环境变量替换：

**${CLAUDE_PLUGIN_ROOT}** - plugin 目录（为保证可移植性请始终使用）：

```json
{
  "command": "${CLAUDE_PLUGIN_ROOT}/servers/my-server"
}
```


**用户环境变量** - 来自用户 shell：

```json
{
  "env": {
    "API_KEY": "${MY_API_KEY}",
    "DATABASE_URL": "${DB_URL}"
  }
}
```


**最佳实践：** 在 plugin README 中记录所有必需的环境变量。

## MCP 工具命名

当 MCP 服务器提供工具时，会自动加上前缀：

**格式：** `mcp__plugin_<plugin-name>_<server-name>__<tool-name>`

**示例：**
- Plugin：`asana`
- 服务器：`asana`
- 工具：`create_task`
- **全名：** `mcp__plugin_asana_asana__asana_create_task`

### 在命令中使用 MCP 工具

在命令 frontmatter 中预授权特定 MCP 工具：


```markdown
---
allowed-tools: [
  "mcp__plugin_asana_asana__asana_create_task",
  "mcp__plugin_asana_asana__asana_search_tasks"
]
---
```


**通配符（谨慎使用）：**

```markdown
---
allowed-tools: ["mcp__plugin_asana_asana__*"]
---
```


**最佳实践：** 出于安全考虑，预授权具体工具，而非通配符。

## 生命周期管理

**自动启动：**
- plugin 启用时启动 MCP 服务器
- 首次使用工具前建立连接
- 配置变更需要重启

**生命周期：**
1. plugin 加载
2. 解析 MCP 配置
3. 启动服务器进程（stdio）或建立连接（SSE/HTTP/WS）
4. 发现并注册工具
5. 工具以 `mcp__plugin_...__...` 形式提供

**查看服务器：**
使用 `/mcp` 命令查看所有服务器，包括由 plugin 提供的服务器。

## 认证模式

### OAuth（SSE/HTTP）

OAuth 由 Claude Code 自动处理：


```json
{
  "type": "sse",
  "url": "https://mcp.example.com/sse"
}
```


用户首次使用时在浏览器中完成认证，无需额外配置。

### 基于 token（请求头）

静态或来自环境变量的 token：


```json
{
  "type": "http",
  "url": "https://api.example.com",
  "headers": {
    "Authorization": "Bearer ${API_TOKEN}"
  }
}
```


在 README 中记录所需环境变量。

### 环境变量（stdio）

向 MCP 服务器传递配置：


```json
{
  "command": "python",
  "args": ["-m", "my_mcp_server"],
  "env": {
    "DATABASE_URL": "${DB_URL}",
    "API_KEY": "${API_KEY}",
    "LOG_LEVEL": "info"
  }
}
```


## 集成模式

### 模式 1：简单工具封装

命令在用户交互中使用 MCP 工具：


```markdown
# Command: create-item.md
---
allowed-tools: ["mcp__plugin_name_server__create_item"]
---

Steps:
1. Gather item details from user
2. Use mcp__plugin_name_server__create_item
3. Confirm creation
```


**适用于：** 在 MCP 调用前加入校验或预处理。

### 模式 2：自主 Agent

Agent 自主使用 MCP 工具：


```markdown
# Agent: data-analyzer.md

Analysis Process:
1. Query data via mcp__plugin_db_server__query
2. Process and analyze results
3. Generate insights report
```


**适用于：** 无需用户交互的多步 MCP 工作流。

### 模式 3：多服务器 Plugin

集成多个 MCP 服务器：


```json
{
  "github": {
    "type": "sse",
    "url": "https://mcp.github.com/sse"
  },
  "jira": {
    "type": "sse",
    "url": "https://mcp.jira.com/sse"
  }
}
```


**适用于：** 跨多个服务的工作流。

## 安全最佳实践

### 使用 HTTPS/WSS

始终使用安全连接：


```json
✅ "url": "https://mcp.example.com/sse"
❌ "url": "http://mcp.example.com/sse"
```


### token 管理

**应做：**
- ✅ 用环境变量存放 token
- ✅ 在 README 中记录所需环境变量
- ✅ 让 OAuth 流程处理认证

**不应做：**
- ❌ 在配置中硬编码 token
- ❌ 把 token commit 到 git
- ❌ 在文档中分享 token

### 权限范围

仅预授权必要的 MCP 工具：


```markdown
✅ allowed-tools: [
  "mcp__plugin_api_server__read_data",
  "mcp__plugin_api_server__create_item"
]

❌ allowed-tools: ["mcp__plugin_api_server__*"]
```


## 错误处理

### 连接失败

处理 MCP 服务器不可用的情况：
- 在命令中提供回退行为
- 向用户提示连接问题
- 检查服务器 URL 与配置

### 工具调用错误

处理失败的 MCP 操作：
- 调用 MCP 工具前校验输入
- 给出清晰的错误信息
- 检查速率限制与配额

### 配置错误

校验 MCP 配置：
- 开发期间测试服务器连通性
- 校验 JSON 语法
- 检查必需的环境变量

## 性能注意事项

### 延迟加载

MCP 服务器按需连接：
- 并非所有服务器都在启动时连接
- 首次使用工具时触发连接
- 连接池自动管理

### 批量处理

尽可能批量处理相似请求：


```
# Good: Single query with filters
tasks = search_tasks(project="X", assignee="me", limit=50)

# Avoid: Many individual queries
for id in task_ids:
    task = get_task(id)
```


## 测试 MCP 集成

### 本地测试

1. 在 `.mcp.json` 中配置 MCP 服务器
2. 本地安装 plugin（`.claude-plugin/`）
3. 运行 `/mcp` 验证服务器出现
4. 在命令中测试工具调用
5. 查看 `claude --debug` 日志排查连接问题

### 验证清单

- [ ] MCP 配置是合法的 JSON
- [ ] 服务器 URL 正确且可访问
- [ ] 已记录所需环境变量
- [ ] 工具出现在 `/mcp` 输出中
- [ ] 认证正常（OAuth 或 token）
- [ ] 命令中的工具调用成功
- [ ] 妥善处理错误情况

## 调试

### 启用调试日志


```bash
claude --debug
```


关注以下内容：
- MCP 服务器连接尝试
- 工具发现日志
- 认证流程
- 工具调用错误

### 常见问题

**服务器无法连接：**
- 检查 URL 是否正确
- 确认服务器正在运行（stdio）
- 检查网络连通性
- 检查认证配置

**工具不可用：**
- 确认服务器已成功连接
- 检查工具名称是否完全匹配
- 运行 `/mcp` 查看可用工具
- 配置变更后重启 Claude Code

**认证失败：**
- 清除缓存的认证 token
- 重新认证
- 检查 token 作用域与权限
- 确认环境变量已设置

## 快速参考

### MCP 服务器类型

| 类型 | 传输方式 | 适用场景 | 认证 |
|------|-----------|----------|------|
| stdio | 进程 | 本地工具、自定义服务器 | 环境变量 |
| SSE | HTTP | 托管服务、云端 API | OAuth |
| HTTP | REST | API 后端、token 认证 | token |
| ws | WebSocket | 实时、流式传输 | token |

### 配置清单

- [ ] 已指定服务器类型（stdio/SSE/HTTP/ws）
- [ ] 类型相关字段齐全（command 或 url）
- [ ] 已配置认证
- [ ] 已记录环境变量
- [ ] 使用 HTTPS/WSS（而非 HTTP/WS）
- [ ] 路径中使用 ${CLAUDE_PLUGIN_ROOT}

### 最佳实践

**应做：**
- ✅ 使用 ${CLAUDE_PLUGIN_ROOT} 保证路径可移植
- ✅ 记录所需环境变量
- ✅ 使用安全连接（HTTPS/WSS）
- ✅ 在命令中预授权特定 MCP 工具
- ✅ 发布上线前测试 MCP 集成
- ✅ 妥善处理连接与工具错误

**不应做：**
- ❌ 硬编码绝对路径
- ❌ 把凭证 commit 到 git
- ❌ 用 HTTP 代替 HTTPS
- ❌ 用通配符预授权所有工具
- ❌ 忽略错误处理
- ❌ 忘记记录配置说明

## 其他资源

### 参考文件

更多信息请参阅：

- **`references/server-types.md`** - 深入讲解每种服务器类型
- **`references/authentication.md`** - 认证模式与 OAuth
- **`references/tool-usage.md`** - 在命令与 Agent 中使用 MCP 工具

### 配置示例

可运行示例位于 `examples/`：

- **`stdio-server.json`** - 本地 stdio MCP 服务器
- **`sse-server.json`** - 带 OAuth 的托管 SSE 服务器
- **`http-server.json`** - 带 token 认证的 REST API

### 外部资源

- **官方 MCP 文档**: https://modelcontextprotocol.io/
- **Claude Code MCP 文档**: https://docs.claude.com/en/docs/claude-code/mcp
- **MCP SDK**: @modelcontextprotocol/sdk
- **测试**: 使用 `claude --debug` 和 `/mcp` 命令

## 实施流程

为 plugin 添加 MCP 集成：

1. 选择 MCP 服务器类型（stdio、SSE、HTTP、ws）
2. 在 plugin 根目录创建带配置的 `.mcp.json`
3. 所有文件引用使用 ${CLAUDE_PLUGIN_ROOT}
4. 在 README 中记录所需环境变量
5. 用 `/mcp` 命令本地测试
6. 在相关命令中预授权 MCP 工具
7. 处理认证（OAuth 或 token）
8. 测试错误情况（连接失败、认证错误）
9. 在 plugin README 中记录 MCP 集成

自定义/本地服务器优先使用 stdio，带 OAuth 的托管服务优先使用 SSE。
