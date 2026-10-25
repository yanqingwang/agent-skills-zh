---
name: guard
version: 0.1.0
description: "全面安全模式：破坏性命令警告 + 目录级编辑限制。（gstack）"
triggers:
  - full safety mode
  - guard against mistakes
  - maximum safety
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: 'bash -c "exec bash \"$HOME/.claude/skills/gstack/careful/bin/check-careful.sh\""'
          statusMessage: "Checking for destructive commands..."
    - matcher: "PowerShell"
      hooks:
        - type: command
          command: 'bash -c "exec bash \"$HOME/.claude/skills/gstack/careful/bin/check-careful.sh\""'
          statusMessage: "Checking for destructive commands..."
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

> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`guard/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

<!-- AUTO-GENERATED from SKILL.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->

# /guard — 全面安全模式

同时启用破坏性命令警告与目录级编辑限制。这是把 `/careful` + `/freeze` 合并为
一条命令的组合。

**依赖说明：** 本 Skill 引用兄弟目录 `/careful` 与 `/freeze` 中的 hook 脚本。两者都必须已安装
（gstack 的 setup 脚本会将它们一并安装）。

```bash
GSTACK_STATE_ROOT=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT); : "${GSTACK_STATE_ROOT:?gstack-paths failed; reinstall with ./setup or /gstack-upgrade}"
mkdir -p "$GSTACK_STATE_ROOT"/analytics
echo '{"skill":"guard","ts":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","repo":"'$(basename "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || echo "unknown")'"}'  >> "$GSTACK_STATE_ROOT"/analytics/skill-usage.jsonl 2>/dev/null || true
```

## 设置

询问用户要把编辑限制到哪个目录。使用 AskUserQuestion：

- 问题："Guard 模式：要把编辑限制到哪个目录？破坏性命令警告始终开启。所选路径之外的文件将被禁止编辑。"
- 文本输入（而非多选），由用户输入路径。

一旦用户提供了目录路径：

用共享写入器设置用户选定的边界；它会解析物理绝对路径，并将替换与调查清理串行化：
```bash
bash "$HOME/.claude/skills/gstack/freeze/bin/freeze-state.sh" set "<user-provided-path>"
```

helper 失败时，不要宣称边界已生效。保持状态并报告恢复方式；绝不用直接写入或删除绕过共享写入器。

告诉用户：
- "**Guard 模式已激活。** 现在同时运行两重保护："
- "1. **破坏性命令守卫** ， rm -rf、DROP TABLE、force-push 等在执行前警告（可覆盖继续）；灾难性形态（递归删除 / 或 ~、向默认分支 force-push）会被硬拒绝"
- "2. **编辑边界** ， 文件编辑被限制在 `<path>/` 内。该目录之外的编辑将被阻止。"
- "要移除持久的编辑边界，运行 `/unfreeze`。结束会话会停止其 hook，但不会删除该边界。"

## 保护范围

完整的破坏性命令模式清单与安全例外见 `/careful`。
编辑边界的执行机制见 `/freeze`。
