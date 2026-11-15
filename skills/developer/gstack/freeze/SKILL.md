---
name: freeze
version: 0.1.0
description: 在会话期间将文件编辑限制到指定目录。（gstack）
triggers:
  - freeze edits to directory
  - lock editing scope
  - restrict file changes
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
hooks:
  PreToolUse:
    - matcher: "Edit"
      hooks:
        - type: command
          command: 'bash -c "exec bash \"$HOME/.claude/skills/gstack/freeze/bin/check-freeze.sh\""'
          statusMessage: "Checking freeze boundary..."
    - matcher: "Write"
      hooks:
        - type: command
          command: 'bash -c "exec bash \"$HOME/.claude/skills/gstack/freeze/bin/check-freeze.sh\""'
          statusMessage: "Checking freeze boundary..."
    - matcher: "NotebookEdit"
      hooks:
        - type: command
          command: 'bash -c "exec bash \"$HOME/.claude/skills/gstack/freeze/bin/check-freeze.sh\""'
          statusMessage: "Checking freeze boundary..."
---

> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`freeze/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

<!-- AUTO-GENERATED from SKILL.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->

# /freeze — 将编辑限制到某个目录

把文件编辑锁定到指定目录。任何针对允许路径之外文件的 Edit、Write 或
NotebookEdit 操作都会被**阻止**（不只是
警告）。

```bash
GSTACK_STATE_ROOT=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT); : "${GSTACK_STATE_ROOT:?gstack-paths failed; reinstall with ./setup or /gstack-upgrade}"
mkdir -p "$GSTACK_STATE_ROOT"/analytics
echo '{"skill":"freeze","ts":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","repo":"'$(basename "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || echo "unknown")'"}'  >> "$GSTACK_STATE_ROOT"/analytics/skill-usage.jsonl 2>/dev/null || true
```

## 设置

询问用户要把编辑限制到哪个目录。使用 AskUserQuestion：

- 问题："要把编辑限制到哪个目录？该路径之外的文件将被禁止编辑。"
- 文本输入（而非多选），由用户输入路径。

一旦用户提供了目录路径：

用共享状态写入器设置用户选定的边界。它会解析物理绝对路径，并将替换与调查清理串行化：
```bash
bash "$HOME/.claude/skills/gstack/freeze/bin/freeze-state.sh" set "<user-provided-path>"
```

仅在 helper 成功时才报告成功。遇到 `FREEZE_BUSY` 或意外状态时，保持原样，并请用户在活跃写入器结束后再检查恢复；绝不直接写入或删除状态文件。

告诉用户："编辑现在被限制在 `<path>/` 内。该目录之外的任何 Edit、Write 或
NotebookEdit 都将被阻止。要更改边界，再次运行 `/freeze`。
要移除它，运行 `/unfreeze`。"

## 工作原理

hook 从 Edit/Write 工具的输入 JSON 中读取 `file_path`，或从
NotebookEdit（Jupyter notebook）调用中读取 `notebook_path`（与 /careful
共享同一个真实 JSON 提取器，一份拷贝，两个 hook 共同引用），
然后检查该路径是否以冻结目录开头。若不是，它会返回一个带
`permissionDecision: "deny"` 的 `hookSpecificOutput` 载荷来阻止该操作
（必须嵌套在 `hookSpecificOutput` 之下，Claude Code 会忽略
顶层的 `permissionDecision`）。

极性为 fail-closed（默认拒绝）：hook 无法解析的工具载荷会被拒绝而不是
放行，fail-open 的边界不是边界。可以解析但两个路径字段都不存在的载荷
（非文件工具）会被放行。拒绝时会点名工具、路径字段、边界
和 `/unfreeze`。符号链接会解析到其最终（FINAL）分量，因此位于边界
之内、指向边界之外的符号链接会按其
目标接受检查。

冻结边界会一直存在，直到通过状态文件被显式移除。hook 脚本在每次
Edit/Write/NotebookEdit 调用时都会读取它。
支持包含空格的边界。

## 说明

- 冻结目录末尾的 `/` 可防止 `/src` 匹配到 `/src-old`
- 冻结只作用于 Edit、Write 和 NotebookEdit，Read、Bash、PowerShell、Glob、Grep 不受影响
- 它防止的是误编辑，而不是安全边界，`sed` 或 `Set-Content` 之类的 Bash/PowerShell 命令仍能修改边界之外的文件
- 要停用，运行 `/unfreeze`；结束或终止会话不会移除已持久化的状态
