> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/plugin-dev/skills/hook-development/references/migration.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 从基础 Hook 迁移到高级 Hook

本指南演示如何从基础 command Hook 迁移到高级 prompt 型 Hook，获得更好的可维护性与灵活性。

## 为什么要迁移？

prompt 型 Hook 有多项优势：

- **自然语言推理**：LLM 理解上下文与意图
- **更好的边界情况处理**：能应对意外场景
- **无需编写 bash 脚本**：编写与维护更简单
- **更灵活的验证**：无需编码即可处理复杂逻辑

## 迁移示例：Bash 命令验证

### 迁移前（基础 command Hook）

**配置：**
```json
{
  "PreToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "command",
          "command": "bash validate-bash.sh"
        }
      ]
    }
  ]
}
```

**脚本（validate-bash.sh）：**
```bash
#!/bin/bash
input=$(cat)
command=$(echo "$input" | jq -r '.tool_input.command')

# Hard-coded validation logic
if [[ "$command" == *"rm -rf"* ]]; then
  echo "Dangerous command detected" >&2
  exit 2
fi
```

**问题：**
- 只检查精确的 "rm -rf" 模式
- 抓不住 `rm -fr`、`rm -r -f` 这类变体
- 漏掉其他危险命令（`dd`、`mkfs` 等）
- 无上下文感知
- 需要 bash 脚本知识

### 迁移后（高级 prompt Hook）

**配置：**
```json
{
  "PreToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Command: $TOOL_INPUT.command. Analyze for: 1) Destructive operations (rm -rf, dd, mkfs, etc) 2) Privilege escalation (sudo) 3) Network operations without user consent. Return 'approve' or 'deny' with explanation.",
          "timeout": 15
        }
      ]
    }
  ]
}
```

**收益：**
- 抓住所有变体与模式
- 理解意图，而不只是字面字符串
- 无需脚本文件
- 易于扩展新判据
- 上下文感知的决策
- 拒绝时给出自然语言解释

## 迁移示例：文件写入验证

### 迁移前（基础 command Hook）

**配置：**
```json
{
  "PreToolUse": [
    {
      "matcher": "Write",
      "hooks": [
        {
          "type": "command",
          "command": "bash validate-write.sh"
        }
      ]
    }
  ]
}
```

**脚本（validate-write.sh）：**
```bash
#!/bin/bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

# Check for path traversal
if [[ "$file_path" == *".."* ]]; then
  echo '{"decision": "deny", "reason": "Path traversal detected"}' >&2
  exit 2
fi

# Check for system paths
if [[ "$file_path" == "/etc/"* ]] || [[ "$file_path" == "/sys/"* ]]; then
  echo '{"decision": "deny", "reason": "System file"}' >&2
  exit 2
fi
```

**问题：**
- 路径模式硬编码
- 不理解符号链接
- 漏掉边界情况（如 `/etc` 与 `/etc/`）
- 不考虑文件内容

### 迁移后（高级 prompt Hook）

**配置：**
```json
{
  "PreToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "File path: $TOOL_INPUT.file_path. Content preview: $TOOL_INPUT.content (first 200 chars). Verify: 1) Not system directories (/etc, /sys, /usr) 2) Not credentials (.env, tokens, secrets) 3) No path traversal 4) Content doesn't expose secrets. Return 'approve' or 'deny'."
        }
      ]
    }
  ]
}
```

**收益：**
- 上下文感知（连内容也一并考虑）
- 能处理符号链接与边界情况
- 自然理解"系统目录"概念
- 能检测内容中的秘密信息
- 判据易于扩展

## 何时保留 command Hook

command Hook 仍有用武之地：

### 1. 确定性的性能检查

```bash
#!/bin/bash
# Check file size quickly
file_path=$(echo "$input" | jq -r '.tool_input.file_path')
size=$(stat -f%z "$file_path" 2>/dev/null || stat -c%s "$file_path" 2>/dev/null)

if [ "$size" -gt 10000000 ]; then
  echo '{"decision": "deny", "reason": "File too large"}' >&2
  exit 2
fi
```

**何时用 command Hook：** 校验是纯数学或确定性的。

### 2. 外部工具集成

```bash
#!/bin/bash
# Run security scanner
file_path=$(echo "$input" | jq -r '.tool_input.file_path')
scan_result=$(security-scanner "$file_path")

if [ "$?" -ne 0 ]; then
  echo "Security scan failed: $scan_result" >&2
  exit 2
fi
```

**何时用 command Hook：** 集成只给是/否答案的外部工具。

### 3. 极快检查（< 50ms）

```bash
#!/bin/bash
# Quick regex check
command=$(echo "$input" | jq -r '.tool_input.command')

if [[ "$command" =~ ^(ls|pwd|echo)$ ]]; then
  exit 0  # Safe commands
fi
```

**何时用 command Hook：** 性能关键且逻辑简单。

## 混合方案

两者结合做多阶段验证：

```json
{
  "PreToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "command",
          "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/quick-check.sh",
          "timeout": 5
        },
        {
          "type": "prompt",
          "prompt": "Deep analysis of bash command: $TOOL_INPUT",
          "timeout": 15
        }
      ]
    }
  ]
}
```

command Hook 负责快速确定性检查，prompt Hook 负责复杂推理。

## 迁移检查清单

迁移 Hook 时：

- [ ] 找出 command Hook 中的校验逻辑
- [ ] 把硬编码模式改写为自然语言判据
- [ ] 用旧 Hook 漏掉的边界情况做测试
- [ ] 确认 LLM 理解意图
- [ ] 设置合适的超时（prompt Hook 通常 15-30 秒）
- [ ] 在 README 中记录新 Hook
- [ ] 移除或归档旧脚本文件

## 迁移建议

1. **从单个 Hook 开始**：不要一次迁移全部
2. **充分测试**：确认 prompt Hook 能抓住 command Hook 抓到的一切
3. **顺手改进**：把迁移当作增强校验的机会
4. **保留脚本备查**：归档旧脚本，日后需要参考逻辑时用得上
5. **记录理由**：在 README 中说明 prompt Hook 为什么更好

## 完整迁移示例

### 原始插件结构

```
my-plugin/
├── .claude-plugin/plugin.json
├── hooks/hooks.json
└── scripts/
    ├── validate-bash.sh
    ├── validate-write.sh
    └── check-tests.sh
```

### 迁移后

```
my-plugin/
├── .claude-plugin/plugin.json
├── hooks/hooks.json      # Now uses prompt hooks
└── scripts/              # Archive or delete
    └── archive/
        ├── validate-bash.sh
        ├── validate-write.sh
        └── check-tests.sh
```

### 更新后的 hooks.json

```json
{
  "PreToolUse": [
    {
      "matcher": "Bash",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Validate bash command safety: destructive ops, privilege escalation, network access"
        }
      ]
    },
    {
      "matcher": "Write|Edit",
      "hooks": [
        {
          "type": "prompt",
          "prompt": "Validate file write safety: system paths, credentials, path traversal, content secrets"
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
          "prompt": "Verify tests were run if code was modified"
        }
      ]
    }
  ]
}
```

**结果：** 更简单、更易维护、更强大。

## 常见迁移模式

### 模式：字符串包含 → 自然语言

**迁移前：**
```bash
if [[ "$command" == *"sudo"* ]]; then
  echo "Privilege escalation" >&2
  exit 2
fi
```

**迁移后：**
```
"Check for privilege escalation (sudo, su, etc)"
```

### 模式：正则 → 意图

**迁移前：**
```bash
if [[ "$file" =~ \.(env|secret|key|token)$ ]]; then
  echo "Credential file" >&2
  exit 2
fi
```

**迁移后：**
```
"Verify not writing to credential files (.env, secrets, keys, tokens)"
```

### 模式：多条件 → 判据清单

**迁移前：**
```bash
if [ condition1 ] || [ condition2 ] || [ condition3 ]; then
  echo "Invalid" >&2
  exit 2
fi
```

**迁移后：**
```
"Check: 1) condition1 2) condition2 3) condition3. Deny if any fail."
```

## 结语

迁移到 prompt 型 Hook 能让插件更易维护、更灵活、更强大。command Hook 留给确定性检查与外部工具集成。
