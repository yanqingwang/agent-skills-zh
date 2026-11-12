---
name: hook-development
description: 当用户要求"创建 Hook"、"添加 PreToolUse/PostToolUse/Stop Hook"、"验证工具调用"、"实现基于提示词的 Hook"、"使用 ${CLAUDE_PLUGIN_ROOT}"、"搭建事件驱动自动化"、"拦截危险命令"，或提及 Hook 事件（PreToolUse、PostToolUse、Stop、SubagentStop、SessionStart、SessionEnd、UserPromptSubmit、PreCompact、Notification）时，应使用本 Skill。为创建和实现 Claude Code 插件 Hook 提供全面指导，重点介绍高级的基于提示词 Hook API。
version: 0.1.0
---

> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/plugin-dev/skills/hook-development/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 面向 Claude Code 插件的 Hook 开发

## 概述

Hook 是响应 Claude Code 事件而执行的事件驱动自动化脚本。使用 Hook 可以验证操作、强制执行策略、补充上下文，并将外部工具集成到工作流中。

**核心能力：**
- 在执行前验证工具调用（PreToolUse）
- 对工具结果作出响应（PostToolUse）
- 强制执行完成标准（Stop、SubagentStop）
- 加载项目上下文（SessionStart）
- 在整个开发生命周期中自动化工作流

## Hook 类型

### 基于提示词的 Hook（推荐）

使用 LLM 驱动的决策来实现上下文感知的验证：


```json
{
  "type": "prompt",
  "prompt": "Evaluate if this tool use is appropriate: $TOOL_INPUT",
  "timeout": 30
}
```


**支持的事件：** Stop、SubagentStop、UserPromptSubmit、PreToolUse

**优势：**
- 基于自然语言推理的上下文感知决策
- 无需 bash 脚本即可实现灵活的评估逻辑
- 更好地处理边界情况
- 更易维护和扩展

### 命令 Hook

执行 bash 命令以进行确定性检查：


```json
{
  "type": "command",
  "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh",
  "timeout": 60
}
```


**适用场景：**
- 快速的确定性验证
- 文件系统操作
- 外部工具集成
- 对性能要求很高的检查

## Hook 配置格式

### 插件 hooks.json 格式

**对于插件 Hook**，在 `hooks/hooks.json` 中使用包装格式：


```json
{
  "description": "Brief explanation of hooks (optional)",
  "hooks": {
    "PreToolUse": [...],
    "Stop": [...],
    "SessionStart": [...]
  }
}
```


**要点：**
- `description` 字段可选
- `hooks` 字段是必需的包装层，包含实际的 Hook 事件
- 这是**插件专用格式**

**示例：**

```json
{
  "description": "Validation hooks for code quality",
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/hooks/validate.sh"
          }
        ]
      }
    ]
  }
}
```


### 设置格式（直接）

**对于用户设置**，在 `.claude/settings.json` 中使用直接格式：


```json
{
  "PreToolUse": [...],
  "Stop": [...],
  "SessionStart": [...]
}
```


**要点：**
- 没有包装层，事件直接位于顶层
- 没有 description 字段
- 这是**设置格式**

**重要：** 下面的示例展示了放入这两种格式的 Hook 事件结构。对于插件 hooks.json，请用 `{"hooks": {...}}` 将其包装起来。

## Hook 事件

### PreToolUse

在任何工具运行之前执行。用于批准、拒绝或修改工具调用。

**示例（基于提示词）：**

```json
{
  "PreToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Validate file write safety. Check: system paths, credentials, path traversal, sensitive content. Return 'approve' or 'deny'."
        }
      ]
    }
  ]
}
```


**PreToolUse 的输出：**

```json
{
  "hookSpecificOutput": {
    "permissionDecision": "allow|deny|ask",
    "updatedInput": {"field": "modified_value"}
  },
  "systemMessage": "Explanation for Claude"
}
```


### PostToolUse

在工具完成后执行。用于对结果作出响应、提供反馈或记录日志。

**示例：**

```json
{
  "PostToolUse": [
    {
      "matcher": "Edit",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Analyze edit result for potential issues: syntax errors, security vulnerabilities, breaking changes. Provide feedback."
        }
      ]
    }
  ]
}
```


**输出行为：**
- 退出码 0：stdout 显示在记录中
- 退出码 2：stderr 反馈给 Claude
- systemMessage 纳入上下文

### Stop

在主 Agent 考虑停止时执行。用于验证完整性。

**示例：**

```json
{
  "Stop": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Verify task completion: tests run, build succeeded, questions answered. Return 'approve' to stop or 'block' with reason to continue."
        }
      ]
    }
  ]
}
```


**决策输出：**

```json
{
  "decision": "approve|block",
  "reason": "Explanation",
  "systemMessage": "Additional context"
}
```


### SubagentStop

在子 Agent 考虑停止时执行。用于确保子 Agent 已完成其任务。

与 Stop Hook 类似，但面向子 Agent。

### UserPromptSubmit

在用户提交提示词时执行。用于补充上下文、验证或拦截提示词。

**示例：**

```json
{
  "UserPromptSubmit": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Check if prompt requires security guidance. If discussing auth, permissions, or API security, return relevant warnings."
        }
      ]
    }
  ]
}
```


### SessionStart

在 Claude Code 会话开始时执行。用于加载上下文并设置环境。

**示例：**

```json
{
  "SessionStart": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "command",
          "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/load-context.sh"
        }
      ]
    }
  ]
}
```


**特殊能力：** 使用 `$CLAUDE_ENV_FILE` 持久化环境变量：

```bash
echo "export PROJECT_TYPE=nodejs" >> "$CLAUDE_ENV_FILE"
```


完整示例参见 `examples/load-context.sh`。

### SessionEnd

在会话结束时执行。用于清理、记录日志和保存状态。

### PreCompact

在上下文压缩之前执行。用于补充需要保留的关键信息。

### Notification

在 Claude 发送通知时执行。用于响应用户通知。

## Hook 输出格式

### 标准输出（所有 Hook）


```json
{
  "continue": true,
  "suppressOutput": false,
  "systemMessage": "Message for Claude"
}
```


- `continue`：为 false 时停止处理（默认 true）
- `suppressOutput`：对记录隐藏输出（默认 false）
- `systemMessage`：展示给 Claude 的消息

### 退出码

- `0` - 成功（stdout 显示在记录中）
- `2` - 阻塞性错误（stderr 反馈给 Claude）
- 其他 - 非阻塞性错误

## Hook 输入格式

所有 Hook 都通过 stdin 接收带有通用字段的 JSON：


```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.txt",
  "cwd": "/current/working/dir",
  "permission_mode": "ask|allow",
  "hook_event_name": "PreToolUse"
}
```


**特定于事件的字段：**

- **PreToolUse/PostToolUse：** `tool_name`、`tool_input`、`tool_result`
- **UserPromptSubmit：** `user_prompt`
- **Stop/SubagentStop：** `reason`

在提示词中使用 `$TOOL_INPUT`、`$TOOL_RESULT`、`$USER_PROMPT` 等访问字段。

## 环境变量

在所有命令 Hook 中可用：

- `$CLAUDE_PROJECT_DIR` - 项目根目录路径
- `$CLAUDE_PLUGIN_ROOT` - 插件目录（用于可移植路径）
- `$CLAUDE_ENV_FILE` - 仅 SessionStart：在此持久化环境变量
- `$CLAUDE_CODE_REMOTE` - 在远程上下文中运行时设置

**为保证可移植性，务必在 Hook 命令中使用 ${CLAUDE_PLUGIN_ROOT}：**


```json
{
  "type": "command",
  "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh"
}
```


## 插件 Hook 配置

在插件中，于 `hooks/hooks.json` 定义 Hook：


```json
{
  "PreToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Validate file write safety"
        }
      ]
    }
  ],
  "Stop": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Verify task completion"
        }
      ]
    }
  ],
  "SessionStart": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "command",
          "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/load-context.sh",
          "timeout": 10
        }
      ]
    }
  ]
}
```


插件 Hook 会与用户的 Hook 合并后并行运行。

## 匹配器

### 工具名称匹配

**精确匹配：**

```json
"matcher": "Write"
```


**多个工具：**

```json
"matcher": "Read|Write|Edit"
```


**通配符（所有工具）：**

```json
"matcher": "*"
```


**正则模式：**

```json
"matcher": "mcp__.*__delete.*"  // All MCP delete tools
```


**注意：** 匹配器区分大小写。

### 常见模式


```json
// All MCP tools
"matcher": "mcp__.*"

// Specific plugin's MCP tools
"matcher": "mcp__plugin_asana_.*"

// All file operations
"matcher": "Read|Write|Edit"

// Bash commands only
"matcher": "Bash"
```


## 安全最佳实践

### 输入验证

务必在命令 Hook 中验证输入：


```bash
#!/bin/bash
set -euo pipefail

input=$(cat)
tool_name=$(echo "$input" | jq -r '.tool_name')

# Validate tool name format
if [[ ! "$tool_name" =~ ^[a-zA-Z0-9_]+$ ]]; then
  echo '{"decision": "deny", "reason": "Invalid tool name"}' >&2
  exit 2
fi
```


### 路径安全

检查路径穿越和敏感文件：


```bash
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

# Deny path traversal
if [[ "$file_path" == *".."* ]]; then
  echo '{"decision": "deny", "reason": "Path traversal detected"}' >&2
  exit 2
fi

# Deny sensitive files
if [[ "$file_path" == *".env"* ]]; then
  echo '{"decision": "deny", "reason": "Sensitive file"}' >&2
  exit 2
fi
```


完整示例参见 `examples/validate-write.sh` 和 `examples/validate-bash.sh`。

### 为所有变量加引号


```bash
# GOOD: Quoted
echo "$file_path"
cd "$CLAUDE_PROJECT_DIR"

# BAD: Unquoted (injection risk)
echo $file_path
cd $CLAUDE_PROJECT_DIR
```


### 设置合适的超时


```json
{
  "type": "command",
  "command": "bash script.sh",
  "timeout": 10
}
```


**默认值：** 命令 Hook（60s），提示词 Hook（30s）

## 性能注意事项

### 并行执行

所有匹配的 Hook 都**并行运行**：


```json
{
  "PreToolUse": [
    {
      "matcher": "Write",
      "hooks": [
        {"type": "command", "command": "check1.sh"},  // Parallel
        {"type": "command", "command": "check2.sh"},  // Parallel
        {"type": "prompt", "prompt": "Validate..."}   // Parallel
      ]
    }
  ]
}
```


**设计含义：**
- Hook 之间看不到彼此的输出
- 顺序不确定
- 按相互独立来设计

### 优化

1. 对快速的确定性检查使用命令 Hook
2. 对复杂推理使用提示词 Hook
3. 将验证结果缓存到临时文件
4. 减少热路径中的 I/O

## 临时启用的 Hook

通过检查标志文件或配置，创建按条件启用的 Hook：

**模式：标志文件启用**

```bash
#!/bin/bash
# Only active when flag file exists
FLAG_FILE="$CLAUDE_PROJECT_DIR/.enable-strict-validation"

if [ ! -f "$FLAG_FILE" ]; then
  # Flag not present, skip validation
  exit 0
fi

# Flag present, run validation
input=$(cat)
# ... validation logic ...
```


**模式：基于配置启用**

```bash
#!/bin/bash
# Check configuration for activation
CONFIG_FILE="$CLAUDE_PROJECT_DIR/.claude/plugin-config.json"

if [ -f "$CONFIG_FILE" ]; then
  enabled=$(jq -r '.strictMode // false' "$CONFIG_FILE")
  if [ "$enabled" != "true" ]; then
    exit 0  # Not enabled, skip
  fi
fi

# Enabled, run hook logic
input=$(cat)
# ... hook logic ...
```


**使用场景：**
- 仅在需要时启用严格验证
- 临时调试用 Hook
- 特定于项目的 Hook 行为
- Hook 的功能开关

**最佳实践：** 在插件 README 中记录启用机制，让用户知道如何启用或禁用临时 Hook。

## Hook 生命周期与限制

### Hook 在会话启动时加载

**重要：** Hook 在 Claude Code 会话启动时加载。修改 Hook 配置后需要重启 Claude Code。

**无法热替换 Hook：**
- 编辑 `hooks/hooks.json` 不会影响当前会话
- 新增的 Hook 脚本不会被识别
- 修改 Hook 命令或提示词不会更新
- 必须重启 Claude Code：退出后重新运行 `claude`

**测试 Hook 改动：**
1. 编辑 Hook 配置或脚本
2. 退出 Claude Code 会话
3. 重启：`claude` 或 `cc`
4. 加载新的 Hook 配置
5. 用 `claude --debug` 测试 Hook

### 启动时的 Hook 校验

Claude Code 启动时会对 Hook 进行校验：
- hooks.json 中的无效 JSON 会导致加载失败
- 缺失脚本会引发警告
- 语法错误在调试模式下报告

使用 `/hooks` 命令查看当前会话中已加载的 Hook。

## 调试 Hook

### 启用调试模式


```bash
claude --debug
```


查看 Hook 注册、执行日志、输入/输出 JSON 以及耗时信息。

### 测试 Hook 脚本

直接测试命令 Hook：


```bash
echo '{"tool_name": "Write", "tool_input": {"file_path": "/test"}}' | \
  bash ${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh

echo "Exit code: $?"
```


### 校验 JSON 输出

确保 Hook 输出有效的 JSON：


```bash
output=$(./your-hook.sh < test-input.json)
echo "$output" | jq .
```


## 快速参考

### Hook 事件汇总

| 事件 | 时机 | 用途 |
|-------|------|---------|
| PreToolUse | 工具运行前 | 验证、修改 |
| PostToolUse | 工具运行后 | 反馈、记录日志 |
| UserPromptSubmit | 用户输入时 | 上下文、验证 |
| Stop | Agent 停止时 | 完整性检查 |
| SubagentStop | 子 Agent 完成时 | 任务验证 |
| SessionStart | 会话开始时 | 加载上下文 |
| SessionEnd | 会话结束时 | 清理、记录日志 |
| PreCompact | 上下文压缩前 | 保留上下文 |
| Notification | 收到用户通知时 | 记录日志、响应 |

### 最佳实践

**应当：**
- ✅ 对复杂逻辑使用基于提示词的 Hook
- ✅ 使用 ${CLAUDE_PLUGIN_ROOT} 保证可移植性
- ✅ 验证命令 Hook 中的所有输入
- ✅ 为所有 bash 变量加引号
- ✅ 设置合适的超时
- ✅ 返回结构化的 JSON 输出
- ✅ 全面测试 Hook

**不应：**
- ❌ 使用硬编码路径
- ❌ 未经验证就信任用户输入
- ❌ 创建长时间运行的 Hook
- ❌ 依赖 Hook 的执行顺序
- ❌ 不可预测地修改全局状态
- ❌ 记录敏感信息

## 其他资源

### 参考文件

有关详细模式和高级技巧，请参阅：

- **`references/patterns.md`** - 常见 Hook 模式（8+ 种经过验证的模式）
- **`references/migration.md`** - 从基础 Hook 迁移到高级 Hook
- **`references/advanced.md`** - 高级用例与技巧

### 示例 Hook 脚本

`examples/` 中的可用示例：

- **`validate-write.sh`** - 文件写入验证示例
- **`validate-bash.sh`** - Bash 命令验证示例
- **`load-context.sh`** - SessionStart 上下文加载示例

### 实用脚本

`scripts/` 中的开发工具：

- **`validate-hook-schema.sh`** - 校验 hooks.json 的结构和语法
- **`test-hook.sh`** - 部署前用示例输入测试 Hook
- **`hook-linter.sh`** - 检查 Hook 脚本中的常见问题和最佳实践

### 外部资源

- **官方文档**：https://docs.claude.com/en/docs/claude-code/hooks
- **示例**：参见市场中的 security-guidance 插件
- **测试**：使用 `claude --debug` 获取详细日志
- **验证**：使用 `jq` 校验 Hook 的 JSON 输出

## 实现工作流

在插件中实现 Hook：

1. 确定要挂载的事件（PreToolUse、Stop、SessionStart 等）
2. 在基于提示词的（灵活）Hook 与命令（确定性）Hook 之间做出选择
3. 在 `hooks/hooks.json` 中编写 Hook 配置
4. 对于命令 Hook，创建 Hook 脚本
5. 所有文件引用都使用 ${CLAUDE_PLUGIN_ROOT}
6. 用 `scripts/validate-hook-schema.sh hooks/hooks.json` 校验配置
7. 部署前用 `scripts/test-hook.sh` 测试 Hook
8. 在 Claude Code 中用 `claude --debug` 测试
9. 在插件 README 中记录 Hook

多数用例优先采用基于提示词的 Hook。将命令 Hook 留作对性能要求很高或需要确定性检查的场景。
