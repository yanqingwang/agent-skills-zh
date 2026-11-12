---
name: careful
version: 0.1.0
description: 针对破坏性命令的安全护栏。（gstack）
triggers:
  - be careful
  - warn before destructive
  - safety mode
allowed-tools:
  - Bash
  - Read
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
---

> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`careful/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

<!-- AUTO-GENERATED from SKILL.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->

# /careful — 破坏性命令护栏

安全模式现已**激活**。每条 Bash 和 PowerShell 命令在运行前
都会被检查是否含破坏性模式。一旦检测到破坏性命令，
你会收到警告，并可以选择继续
或取消。

```bash
GSTACK_STATE_ROOT=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT); : "${GSTACK_STATE_ROOT:?gstack-paths failed; reinstall with ./setup or /gstack-upgrade}"
mkdir -p "$GSTACK_STATE_ROOT"/analytics
echo '{"skill":"careful","ts":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","repo":"'$(basename "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || echo "unknown")'"}'  >> "$GSTACK_STATE_ROOT"/analytics/skill-usage.jsonl 2>/dev/null || true
```

## 保护范围

| 模式 | 示例 | 风险 |
|---------|---------|------|
| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/data` | 递归删除 |
| `DROP TABLE` / `DROP DATABASE` | `DROP TABLE users;` | 数据丢失 |
| `TRUNCATE` | `TRUNCATE orders;` | 数据丢失 |
| `git push --force` / `-f` | `git push -f origin main` | 改写历史 |
| `git reset --hard` | `git reset --hard HEAD~3` | 丢失未提交的工作 |
| `git checkout .` / `git restore .` | `git checkout .` | 丢失未提交的工作 |
| `kubectl delete` | `kubectl delete pod` | 影响生产 |
| `docker rm -f` / `docker system prune` | `docker system prune -a` | 丢失容器/镜像 |

## PowerShell 与 cmd（Windows）

hook 同样检查 PowerShell 工具（Claude Code 在 Windows 上的主 shell）以及从
Bash 启动的任何 `pwsh`/`powershell`/`cmd`。匹配不区分大小写，覆盖命令位置的
别名，接受参数前缀（`-r`、`-fo`），并剥离 cmd 的 `^` 转义。上表的所有
规则在那里同样适用。

| 模式 | 示例 |
|---------|---------|
| `Remove-Item`/`rm`/`ri`/`del`/`erase`/`rd`/`rmdir` + `-Recurse` or `-Force` | `gci \| ri -r -fo` |
| cmd `rd /s`, `rmdir /s`, `del /s`, `erase /s` | `cmd /c rd /s /q C:\proj` |
| `Format-Volume`, `Clear-Disk`, `Clear-Content`, `[IO.Directory]::Delete`, `[IO.File]::Delete` | `Clear-Disk -Number 1` |
| `-EncodedCommand`, `iex`, `Start-Process` of a shell, `& $cmd` (can't be inspected) | `irm $url \| iex` |

**PowerShell 上是尽力而为。** 字符串匹配看不到运行时拼接的命令。要硬阻止，
请添加 Claude Code 权限拒绝规则，它能解析 PowerShell 及其别名：在
`.claude/settings.json` 中写 `"deny": ["PowerShell(Remove-Item *)"]`。hook
通过 `bash` 运行，因此 Windows 需要 Git Bash。

## 安全例外

以下模式不加警告直接放行：
- `rm -rf node_modules` / `.next` / `dist` / `__pycache__` / `.cache` / `build` / `.turbo` / `coverage`

## 工作原理

hook 从工具输入 JSON 中读取 `tool_name` 和命令，对照
上面的模式检查，命中时返回一个带 `permissionDecision: "ask"`
与警告原因的 `hookSpecificOutput` 载荷（该决定必须嵌套在
`hookSpecificOutput` 之下——Claude Code 会忽略顶层的
`permissionDecision`）。你始终可以覆盖
MEDIUM 警告并继续。

## HIGH 档（硬拒绝）

两种灾难性形态会被**直接拒绝**而不是询问：对 `/`、`~` 或 `$HOME` 精确执行的
`rm -r`/`-R`，以及向仓库**默认分支**的 force-push。仅限 SIMPLE 命令（不含
`;`、`&&`、`||`、`|`、换行）——复合形态落入 MEDIUM 询问；
`--force-with-lease` 永远不算 HIGH。这是尽力而为的建议性硬停止，不是
策略边界：逃生口是结束这个自愿加入、会话级的 /careful 会话。

## 项目模式（只增不减）

在 `~/.gstack/careful-patterns.txt`（全局）或
`~/.gstack/projects/<slug>/careful-patterns.txt`（按项目）中添加警告规则——每行
一条 POSIX ERE，允许 `#` 注释。它们在内置模式族之后加载，因此配置
只能增加规则，绝不能压制基线警告。
无效的正则行会被跳过。

要停用，结束当前对话或开启新对话。hook 只作用于会话范围。
