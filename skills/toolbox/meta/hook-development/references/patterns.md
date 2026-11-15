> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/plugin-dev/skills/hook-development/references/patterns.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 常见 Hook 模式

本参考提供实现 Claude Code Hook 的常用成熟模式。典型 Hook 用例可以直接以这些模式为起点。

## 模式 1：安全验证

用 prompt 型 Hook 拦截危险的文件写入：

```json
{
  "PreToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "File path: $TOOL_INPUT.file_path. Verify: 1) Not in /etc or system directories 2) Not .env or credentials 3) Path doesn't contain '..' traversal. Return 'approve' or 'deny'."
        }
      ]
    }
  ]
}
```

**适用场景：** 防止写入敏感文件或系统目录。

## 模式 2：测试强制执行

确保停止前跑过测试：

```json
{
  "Stop": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Review transcript. If code was modified (Write/Edit tools used), verify tests were executed. If no tests were run, block with reason 'Tests must be run after code changes'."
        }
      ]
    }
  ]
}
```

**适用场景：** 强制执行质量标准，防止工作未完成就收尾。

## 模式 3：上下文加载

会话开始时加载项目专属上下文：

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

**示例脚本（load-context.sh）：**
```bash
#!/bin/bash
cd "$CLAUDE_PROJECT_DIR" || exit 1

# Detect project type
if [ -f "package.json" ]; then
  echo "📦 Node.js project detected"
  echo "export PROJECT_TYPE=nodejs" >> "$CLAUDE_ENV_FILE"
elif [ -f "Cargo.toml" ]; then
  echo "🦀 Rust project detected"
  echo "export PROJECT_TYPE=rust" >> "$CLAUDE_ENV_FILE"
fi
```

**适用场景：** 自动检测并配置项目专属设置。

## 模式 4：通知记录

记录所有通知，用于审计或分析：

```json
{
  "Notification": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "command",
          "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/log-notification.sh"
        }
      ]
    }
  ]
}
```

**适用场景：** 跟踪用户通知，或对接外部日志系统。

## 模式 5：MCP 工具监控

监控并校验 MCP 工具使用：

```json
{
  "PreToolUse": [
    {
      "matcher": "mcp__.*__delete.*",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Deletion operation detected. Verify: Is this deletion intentional? Can it be undone? Are there backups? Return 'approve' only if safe."
        }
      ]
    }
  ]
}
```

**适用场景：** 防护破坏性 MCP 操作。

## 模式 6：构建验证

确保代码改动后项目完成构建：

```json
{
  "Stop": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Check if code was modified. If Write/Edit tools were used, verify the project was built (npm run build, cargo build, etc). If not built, block and request build."
        }
      ]
    }
  ]
}
```

**适用场景：** 在提交或收尾前发现构建错误。

## 模式 7：权限确认

危险操作前先询问用户：

```json
{
  "PreToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Command: $TOOL_INPUT.command. If command contains 'rm', 'delete', 'drop', or other destructive operations, return 'ask' to confirm with user. Otherwise 'approve'."
        }
      ]
    }
  ]
}
```

**适用场景：** 对潜在破坏性命令做用户确认。

## 模式 8：代码质量检查

文件编辑后运行 linter 或格式化工具：

```json
{
  "PostToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {
          "type": "command",
          "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/check-quality.sh"
        }
      ]
    }
  ]
}
```

**示例脚本（check-quality.sh）：**
```bash
#!/bin/bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

# Run linter if applicable
if [[ "$file_path" == *.js ]] || [[ "$file_path" == *.ts ]]; then
  npx eslint "$file_path" 2>&1 || true
fi
```

**适用场景：** 自动执行代码质量要求。

## 模式组合

组合多个模式实现全面防护：

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
    },
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Validate bash command safety"
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
          "prompt": "Verify tests run and build succeeded"
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
          "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/load-context.sh"
        }
      ]
    }
  ]
}
```

这样就能获得多层防护与自动化。

## 模式 9：临时启用的 Hook

创建仅在通过标志文件显式启用时才运行的 Hook：

```bash
#!/bin/bash
# Hook only active when flag file exists
FLAG_FILE="$CLAUDE_PROJECT_DIR/.enable-security-scan"

if [ ! -f "$FLAG_FILE" ]; then
  # Quick exit when disabled
  exit 0
fi

# Flag present, run validation
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

# Run security scan
security-scanner "$file_path"
```

**启用方式：**
```bash
# Enable the hook
touch .enable-security-scan

# Disable the hook
rm .enable-security-scan
```

**适用场景：**
- 临时调试 Hook
- 开发用功能开关
- 需显式开启的项目专属校验
- 只在需要时才做的高开销检查

**注意：** 创建或删除标志文件后必须重启 Claude Code，Hook 才能识别变更。

## 模式 10：配置驱动的 Hook

用 JSON 配置控制 Hook 行为：

```bash
#!/bin/bash
CONFIG_FILE="$CLAUDE_PROJECT_DIR/.claude/my-plugin.local.json"

# Read configuration
if [ -f "$CONFIG_FILE" ]; then
  strict_mode=$(jq -r '.strictMode // false' "$CONFIG_FILE")
  max_file_size=$(jq -r '.maxFileSize // 1000000' "$CONFIG_FILE")
else
  # Defaults
  strict_mode=false
  max_file_size=1000000
fi

# Skip if not in strict mode
if [ "$strict_mode" != "true" ]; then
  exit 0
fi

# Apply configured limits
input=$(cat)
file_size=$(echo "$input" | jq -r '.tool_input.content | length')

if [ "$file_size" -gt "$max_file_size" ]; then
  echo '{"decision": "deny", "reason": "File exceeds configured size limit"}' >&2
  exit 2
fi
```

**配置文件（.claude/my-plugin.local.json）：**
```json
{
  "strictMode": true,
  "maxFileSize": 500000,
  "allowedPaths": ["/tmp", "/home/user/projects"]
}
```

**适用场景：**
- 用户可配置的 Hook 行为
- 每项目独立设置
- 团队专属规则
- 动态校验判据
