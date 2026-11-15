> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/plugin-dev/skills/mcp-integration/references/tool-usage.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 在命令与 Agent 中使用 MCP 工具

完整指南：如何在 Claude Code plugin 的命令与 Agent 中高效使用 MCP 工具。

## 概述

MCP 服务器配置完成后，其工具即可用，前缀为 `mcp__plugin_<plugin-name>_<server-name>__<tool-name>`。在命令和 Agent 中使用这些工具，方式与内置 Claude Code 工具相同。

## 工具命名规则

### 格式

```
mcp__plugin_<plugin-name>_<server-name>__<tool-name>
```

### 示例

**Asana plugin 配 asana 服务器：**
- `mcp__plugin_asana_asana__asana_create_task`
- `mcp__plugin_asana_asana__asana_search_tasks`
- `mcp__plugin_asana_asana__asana_get_project`

**自定义 plugin 配 database 服务器：**
- `mcp__plugin_myplug_database__query`
- `mcp__plugin_myplug_database__execute`
- `mcp__plugin_myplug_database__list_tables`

### 发现工具名称

**使用 `/mcp` 命令：**
```bash
/mcp
```

它会显示：
- 所有可用的 MCP 服务器
- 每个服务器提供的工具
- 工具 schema 与描述
- 可用于配置的完整工具名

## 在命令中使用工具

### 预授权工具

在命令的 frontmatter 中指定 MCP 工具：

```markdown
---
description: Create a new Asana task
allowed-tools: [
  "mcp__plugin_asana_asana__asana_create_task"
]
---

# Create Task Command

To create a task:
1. Gather task details from user
2. Use mcp__plugin_asana_asana__asana_create_task with the details
3. Confirm creation to user
```

### 多个工具

```markdown
---
allowed-tools: [
  "mcp__plugin_asana_asana__asana_create_task",
  "mcp__plugin_asana_asana__asana_search_tasks",
  "mcp__plugin_asana_asana__asana_get_project"
]
---
```

### 通配符（慎用）

```markdown
---
allowed-tools: ["mcp__plugin_asana_asana__*"]
---
```

**注意：** 只有当命令确实需要访问某服务器的全部工具时，才使用通配符。

### 命令指令中的工具用法

**命令示例：**
```markdown
---
description: Search and create Asana tasks
allowed-tools: [
  "mcp__plugin_asana_asana__asana_search_tasks",
  "mcp__plugin_asana_asana__asana_create_task"
]
---

# Asana Task Management

## Searching Tasks

To search for tasks:
1. Use mcp__plugin_asana_asana__asana_search_tasks
2. Provide search filters (assignee, project, etc.)
3. Display results to user

## Creating Tasks

To create a task:
1. Gather task details:
   - Title (required)
   - Description
   - Project
   - Assignee
   - Due date
2. Use mcp__plugin_asana_asana__asana_create_task
3. Show confirmation with task link
```

## 在 Agent 中使用工具

### Agent 配置

Agent 可以自主使用 MCP 工具，无需预先授权：

```markdown
---
name: asana-status-updater
description: This agent should be used when the user asks to "update Asana status", "generate project report", or "sync Asana tasks"
model: inherit
color: blue
---

## Role

Autonomous agent for generating Asana project status reports.

## Process

1. **Query tasks**: Use mcp__plugin_asana_asana__asana_search_tasks to get all tasks
2. **Analyze progress**: Calculate completion rates and identify blockers
3. **Generate report**: Create formatted status update
4. **Update Asana**: Use mcp__plugin_asana_asana__asana_create_comment to post report

## Available Tools

The agent has access to all Asana MCP tools without pre-approval.
```

### Agent 工具权限

Agent 的工具权限比命令更宽：
- 可以使用 Claude 认为必要的任何工具
- 不需要预授权清单
- 应写明自己通常使用哪些工具

## 工具调用模式

### 模式 1：简单工具调用

单次工具调用，带校验：

```markdown
Steps:
1. Validate user provided required fields
2. Call mcp__plugin_api_server__create_item with validated data
3. Check for errors
4. Display confirmation
```

### 模式 2：顺序工具调用

串联多次工具调用：

```markdown
Steps:
1. Search for existing items: mcp__plugin_api_server__search
2. If not found, create new: mcp__plugin_api_server__create
3. Add metadata: mcp__plugin_api_server__update_metadata
4. Return final item ID
```

### 模式 3：批量操作

用同一工具多次调用：

```markdown
Steps:
1. Get list of items to process
2. For each item:
   - Call mcp__plugin_api_server__update_item
   - Track success/failure
3. Report results summary
```

### 模式 4：错误处理

优雅地处理错误：

```markdown
Steps:
1. Try to call mcp__plugin_api_server__get_data
2. If error (rate limit, network, etc.):
   - Wait and retry (max 3 attempts)
   - If still failing, inform user
   - Suggest checking configuration
3. On success, process data
```

## 工具参数

### 理解工具 Schema

每个 MCP 工具都有定义其参数的 schema。用 `/mcp` 查看。

**Schema 示例：**
```json
{
  "name": "asana_create_task",
  "description": "Create a new Asana task",
  "inputSchema": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "Task title"
      },
      "notes": {
        "type": "string",
        "description": "Task description"
      },
      "workspace": {
        "type": "string",
        "description": "Workspace GID"
      }
    },
    "required": ["name", "workspace"]
  }
}
```

### 带参数调用工具

Claude 会根据 schema 自动组织工具调用：

```typescript
// Claude generates this internally
{
  toolName: "mcp__plugin_asana_asana__asana_create_task",
  input: {
    name: "Review PR #123",
    notes: "Code review for new feature",
    workspace: "12345",
    assignee: "67890",
    due_on: "2025-01-15"
  }
}
```

### 参数校验

**在命令中，调用前先校验：**

```markdown
Steps:
1. Check required parameters:
   - Title is not empty
   - Workspace ID is provided
   - Due date is valid format (YYYY-MM-DD)
2. If validation fails, ask user to provide missing data
3. If validation passes, call MCP tool
4. Handle tool errors gracefully
```

## 响应处理

### 成功响应

```markdown
Steps:
1. Call MCP tool
2. On success:
   - Extract relevant data from response
   - Format for user display
   - Provide confirmation message
   - Include relevant links or IDs
```

### 错误响应

```markdown
Steps:
1. Call MCP tool
2. On error:
   - Check error type (auth, rate limit, validation, etc.)
   - Provide helpful error message
   - Suggest remediation steps
   - Don't expose internal error details to user
```

### 部分成功

```markdown
Steps:
1. Batch operation with multiple MCP calls
2. Track successes and failures separately
3. Report summary:
   - "Successfully processed 8 of 10 items"
   - "Failed items: [item1, item2] due to [reason]"
   - Suggest retry or manual intervention
```

## 性能优化

### 合并请求

**推荐：带过滤条件的单次查询**
```markdown
Steps:
1. Call mcp__plugin_api_server__search with filters:
   - project_id: "123"
   - status: "active"
   - limit: 100
2. Process all results
```

**避免：大量逐条查询**
```markdown
Steps:
1. For each item ID:
   - Call mcp__plugin_api_server__get_item
   - Process item
```

### 缓存结果

```markdown
Steps:
1. Call expensive MCP operation: mcp__plugin_api_server__analyze
2. Store results in variable for reuse
3. Use cached results for subsequent operations
4. Only re-fetch if data changes
```

### 并行工具调用

工具之间没有依赖时，并行调用：

```markdown
Steps:
1. Make parallel calls (Claude handles this automatically):
   - mcp__plugin_api_server__get_project
   - mcp__plugin_api_server__get_users
   - mcp__plugin_api_server__get_tags
2. Wait for all to complete
3. Combine results
```

## 集成最佳实践

### 用户体验

**给出反馈：**
```markdown
Steps:
1. Inform user: "Searching Asana tasks..."
2. Call mcp__plugin_asana_asana__asana_search_tasks
3. Show progress: "Found 15 tasks, analyzing..."
4. Present results
```

**处理耗时操作：**
```markdown
Steps:
1. Warn user: "This may take a minute..."
2. Break into smaller steps with updates
3. Show incremental progress
4. Final summary when complete
```

### 错误信息

**好的错误信息：**
```
❌ "Could not create task. Please check:
   1. You're logged into Asana
   2. You have access to workspace 'Engineering'
   3. The project 'Q1 Goals' exists"
```

**差的错误信息：**
```
❌ "Error: MCP tool returned 403"
```

### 文档

**在命令中写明所用 MCP 工具：**
```markdown
## MCP Tools Used

This command uses the following Asana MCP tools:
- **asana_search_tasks**: Search for tasks matching criteria
- **asana_create_task**: Create new task with details
- **asana_update_task**: Update existing task properties

Ensure you're authenticated to Asana before running this command.
```

## 测试工具使用

### 本地测试

1. 在 `.mcp.json` 中**配置 MCP 服务器**
2. 在 `.claude-plugin/` 中**本地安装 plugin**
3. 用 `/mcp` **确认工具可用**
4. **测试**用到这些工具的命令
5. **检查调试输出**：`claude --debug`

### 测试场景

**测试成功调用：**
```markdown
Steps:
1. Create test data in external service
2. Run command that queries this data
3. Verify correct results returned
```

**测试错误场景：**
```markdown
Steps:
1. Test with missing authentication
2. Test with invalid parameters
3. Test with non-existent resources
4. Verify graceful error handling
```

**测试边界情况：**
```markdown
Steps:
1. Test with empty results
2. Test with maximum results
3. Test with special characters
4. Test with concurrent access
```

## 常见模式

### 模式：CRUD 操作

```markdown
---
allowed-tools: [
  "mcp__plugin_api_server__create_item",
  "mcp__plugin_api_server__read_item",
  "mcp__plugin_api_server__update_item",
  "mcp__plugin_api_server__delete_item"
]
---

# Item Management

## Create
Use create_item with required fields...

## Read
Use read_item with item ID...

## Update
Use update_item with item ID and changes...

## Delete
Use delete_item with item ID (ask for confirmation first)...
```

### 模式：搜索并处理

```markdown
Steps:
1. **Search**: mcp__plugin_api_server__search with filters
2. **Filter**: Apply additional local filtering if needed
3. **Transform**: Process each result
4. **Present**: Format and display to user
```

### 模式：多步骤工作流

```markdown
Steps:
1. **Setup**: Gather all required information
2. **Validate**: Check data completeness
3. **Execute**: Chain of MCP tool calls:
   - Create parent resource
   - Create child resources
   - Link resources together
   - Add metadata
4. **Verify**: Confirm all steps succeeded
5. **Report**: Provide summary to user
```

## 排障

### 工具不可用

**检查：**
- MCP 服务器配置正确
- 服务器已连接（用 `/mcp` 查看）
- 工具名完全匹配（区分大小写）
- 配置变更后重启 Claude Code

### 工具调用失败

**检查：**
- 认证有效
- 参数符合工具 schema
- 必需参数已提供
- 查看 `claude --debug` 日志

### 性能问题

**检查：**
- 合并查询，而不是逐条调用
- 适当缓存结果
- 不做多余的工具调用
- 可能时并行调用

## 结语

高效使用 MCP 工具需要：
1. 用 `/mcp` **理解工具 schema**
2. 在命令中**合理预授权工具**
3. **优雅地处理错误**
4. 用合并与缓存**优化性能**
5. 用反馈和清晰的错误信息**提供好的体验**
6. 上线前**充分测试**

在 plugin 命令与 Agent 中遵循这些模式，即可实现稳健的 MCP 工具集成。
