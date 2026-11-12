---
name: block-no-verify-hook
description: 配置 PreToolUse Hook，阻止 AI Agent 用 --no-verify 及其他绕过标志跳过 git pre-commit hooks。在搭建强制执行 commit 质量门禁的 Claude Code 项目时使用。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/block-no-verify/skills/block-no-verify-hook/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 拦截 no-verify 的 Hook

一种 PreToolUse Hook 配置，在执行前拦截并阻止绕过标志的使用，确保 AI Agent 无法跳过 pre-commit hooks、GPG 签名或其他 git 安全机制。

## 概述

AI 编码 Agent（Claude Code、Codex 等）可能运行带 `--no-verify` 之类标志的 shell 命令，绕过 pre-commit hooks。这会让配置在 pre-commit hooks 中的 lint、格式化、测试和安全检查形同虚设。block-no-verify Hook 加入一道 PreToolUse 防护，在执行前拒绝任何含绕过标志的工具调用。

## 问题

AI Agent 提交代码时，可能会用绕过标志来躲开 Hook 报错：


```bash
# These commands skip pre-commit hooks entirely
git commit --no-verify -m "quick fix"
git push --no-verify
git commit --no-gpg-sign -m "unsigned commit"
git merge --no-verify feature-branch
```


这会带来：
- 未格式化的代码进入仓库
- lint 错误绕过检查
- 跳过安全扫描
- 未签名的 commit 绕过签名策略
- 规避测试套件

## 解决方案

在 `.claude/settings.json` 中添加一个 `PreToolUse` Hook，检查每一次 Bash 工具调用，拦截含绕过标志的命令。

### 配置

把以下内容加入项目的 `.claude/settings.json`：


```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "if grep -qE '\"command\"[[:space:]]*:[[:space:]]*\"([^\"\\\\]|\\\\.)*(--no-(ver|g)|commit([^\"\\\\]|\\\\.)*([[:space:]]|\\\\[tn])-[a-zA-Z]*n)'; then echo 'BLOCKED: --no-verify and --no-gpg-sign flags are not allowed. Run the commit without bypass flags so that pre-commit hooks execute properly.' >&2; exit 2; fi"
          }
        ]
      }
    ]
  }
}
```


### 工作原理

1. **匹配**：该 Hook 只针对 `Bash` 工具调用，不会干扰 Read、Edit、Grep 等其他工具。
2. **检查**：Claude Code 把工具调用以 JSON 形式通过 stdin 发给该 Hook，且不设置 `$TOOL_INPUT` 变量。该 Hook 用 `grep -E` 在这份 JSON 里搜索 `command` 的值，因此不需要 `jq` 或 `node`，而 `cwd`、工具调用描述等其他字段里的文本也不会触发它。它拦截 `--no-verify`、`--no-gpg-sign`，以及 git 能接受的更短前缀，例如 `--no-veri`。它还会拦截同一条命令中跟在 `commit` 之后、含 `n` 的短选项组合，例如 `-n` 或 `-nm`，因为 `-n` 是 `--no-verify` 的简写形式。该 Hook 不查找 `git` 这个词，因此也能拦住 `if git ...`、`sudo git ...` 和 `g=git; $g commit --no-verify`。误匹配（比如提交信息里提到了某个标志）也会拦下该调用，这是更安全的失败方式。
3. **拦截**：如果在 git 命令里发现绕过标志，该 Hook 就以退出码 2 结束并打印一条错误信息。退出码 2 会让 Claude Code 整个拒绝该工具调用。
4. **放行**：如果没有发现绕过标志，该 Hook 以退出码 0 结束，命令正常执行。
5. **局限**：该 Hook 检查的是文本，因此能拦住出于习惯顺手加绕过标志的 Agent；但挡不住一心想绕开它的 Agent，例如把标志拆开拼出来，或者运行 `git -c core.hooksPath=/dev/null commit`。

### 退出码

| 退出码 | 含义 |
|------|---------|
| 0 | 允许工具调用继续 |
| 1 | 错误（工具调用仍会继续，显示警告） |
| 2 | 完全阻止该工具调用 |

## 被拦截的标志

| 标志 | 作用 | 拦截原因 |
|------|---------|-------------|
| `--no-verify` | 跳过 pre-commit 与 commit-msg hooks | 绕过 lint、格式化、测试、安全检查 |
| `--no-gpg-sign` | 跳过 GPG commit 签名 | 绕过 commit 签名策略 |

## 安装

### 单项目配置

在项目根目录创建或更新 `.claude/settings.json`：


```bash
mkdir -p .claude
cat > .claude/settings.json << 'EOF'
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "if grep -qE '\"command\"[[:space:]]*:[[:space:]]*\"([^\"\\\\]|\\\\.)*(--no-(ver|g)|commit([^\"\\\\]|\\\\.)*([[:space:]]|\\\\[tn])-[a-zA-Z]*n)'; then echo 'BLOCKED: --no-verify and --no-gpg-sign flags are not allowed. Run the commit without bypass flags so that pre-commit hooks execute properly.' >&2; exit 2; fi"
          }
        ]
      }
    ]
  }
}
EOF
```


### 全局配置

要在所有项目中强制生效，把配置加入 `~/.claude/settings.json`：


```bash
mkdir -p ~/.claude
cat > ~/.claude/settings.json << 'EOF'
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "if grep -qE '\"command\"[[:space:]]*:[[:space:]]*\"([^\"\\\\]|\\\\.)*(--no-(ver|g)|commit([^\"\\\\]|\\\\.)*([[:space:]]|\\\\[tn])-[a-zA-Z]*n)'; then echo 'BLOCKED: --no-verify and --no-gpg-sign flags are not allowed. Run the commit without bypass flags so that pre-commit hooks execute properly.' >&2; exit 2; fi"
          }
        ]
      }
    ]
  }
}
EOF
```


## 验证

测试该 Hook 能拦截绕过标志：


```bash
# This should be blocked by the hook:
git commit --no-verify -m "test"

# This should succeed normally:
git commit -m "test"
```


## 扩展该 Hook

### 增加更多被拦截的标志

要拦截更多标志（例如 `--force`），扩展这条 grep 模式：


```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "if grep -qE '\"command\"[[:space:]]*:[[:space:]]*\"([^\"\\\\]|\\\\.)*(--no-(ver|g)|commit([^\"\\\\]|\\\\.)*([[:space:]]|\\\\[tn])-[a-zA-Z]*n|git([[:space:]]|\\\\t)([^\"\\\\]|\\\\.)*--force)'; then echo 'BLOCKED: Bypass flags are not allowed.' >&2; exit 2; fi"
          }
        ]
      }
    ]
  }
}
```


### 与其他 Hook 组合

block-no-verify Hook 可与其他 PreToolUse Hook 并存：


```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "if grep -qE '\"command\"[[:space:]]*:[[:space:]]*\"([^\"\\\\]|\\\\.)*(--no-(ver|g)|commit([^\"\\\\]|\\\\.)*([[:space:]]|\\\\[tn])-[a-zA-Z]*n)'; then echo 'BLOCKED: Bypass flags not allowed.' >&2; exit 2; fi"
          }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "if grep -qE 'rm[[:space:]]+-rf[[:space:]]+/'; then echo 'BLOCKED: Dangerous rm command.' >&2; exit 2; fi"
          }
        ]
      }
    ]
  }
}
```


## 最佳实践

1. **提交设置文件** -- 把 `.claude/settings.json` 加入版本控制，让所有团队成员都受该 Hook 保护。
2. **写进上手文档** -- 在项目的贡献指南里提到该 Hook，让开发者明白为何拦截绕过标志。
3. **配合 pre-commit hooks 使用** -- block-no-verify Hook 保证 pre-commit hooks 会运行；请确认你配置了真正有用的 pre-commit hooks。
4. **配置后验证** -- 在一次测试 commit 里故意触发它，确认该 Hook 生效。
