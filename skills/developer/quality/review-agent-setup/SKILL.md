---
name: review-agent-setup
description: 在 Claude Code 中为 AI agent 的审查操作配置人工介入式门禁。适用于搭建如下项目：agent 可能发布 PR 审查、评论、合并，或修改 CI 配置，而你希望借助 Cedar 强制执行的门禁获得可密码学审计的审批留痕。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/review-agent-governance/skills/review-agent-setup/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# review-agent-governance：安装配置

将 AI agent 的审查操作（PR 审查、评论、合并、CI 编辑）置于明确的人工批准之后。每一次尝试，无论批准还是拒绝，都会生成一份经 Ed25519 签名的回执。

## 何时使用本 Plugin

在 Claude Code agent 会执行以下操作的项目中安装本 Plugin：

- 审查、评论或合并 PR（`gh pr review`、`gh pr merge`）
- 分诊工单（`gh issue comment`、`gh issue close`）
- 发布版本（`gh release create`）
- 修改 CI 配置（`.github/workflows/`、`.gitlab-ci.yml`）
- 向受保护分支推送（`main`、`master`、`release`、`production`）
- 向外部通知渠道发布消息（Slack webhooks、Discord），前提是你为发出该通知的命令添加了规则（默认策略不会对其设门禁）

如果 agent 只进行本地文件编辑与运行测试，本 Plugin 便没有必要。通用的工具调用策略强制交给 `protect-mcp` 即可，跳过本 Plugin。

## 一次性设置

### 1. 安装 Plugin

```bash
claude plugin install wshobson/agents/review-agent-governance
```

### 2. 将默认策略复制到你的项目

```bash
cp .claude/plugins/review-agent-governance/policies/review-agent-governance.cedar \
   ./review-governance.cedar
```

你可以编辑该文件以契合项目自身的规则。编写审查策略的指引见 `../agents/review-policy-author.md`。

### 3. 创建回执目录与签名密钥

```bash
mkdir -p ./review-receipts
echo "/review-receipts/" >> .gitignore
echo "/review-governance.key" >> .gitignore
echo "/.review-approved" >> .gitignore
if [ ! -e ./review-governance.key ]; then
  d=$(mktemp -d) && npx protect-mcp@0.32.4 init --dir "$d" && mv "$d/keys/gateway.json" ./review-governance.key
fi
chmod 600 ./review-governance.key
```

protect-mcp 0.7.4 的 `sign` 不会创建密钥，因此由最后一条命令来创建，且它绝不会覆盖已有密钥。没有密钥时，回执就是未签名的。要轮换密钥，先归档 `./review-governance.key` 与 `./review-receipts/receipts.jsonl`，再重新运行该命令。把 `./review-governance.key` 中的 `publicKey` 值交给审计人员。请勿提交该文件，因为它同时含有私钥。

## 每次会话的工作流

Cedar 策略会无条件拒绝所有审查相关操作。要批准某一具体操作，需在操作前开启批准窗口，操作后关闭。

### 标志文件（最简单）

```bash
# Before the action you want to approve
touch ./.review-approved

# Let Claude Code run the review / comment / merge

# Immediately after
rm ./.review-approved
```

### 斜杠命令（在 Claude Code 内使用）

```
/approve-review "Reviewing PR #123 authored by contributor X"
```

这会创建 `./.review-approved`，将给定理由作为备注嵌入其中，并把理由记录到 `./review-receipts/approvals/` 下未签名的批准日志里。仍需随后执行 `rm` 来关闭窗口。

### 全部空跑（强制完整策略求值）

如果希望每次工具调用都经过 Cedar、不允许任何批准绕过：

```bash
export REVIEW_APPROVAL_FLAG=./.never-approve
```

策略会拒绝任何命中 forbid 规则的工具调用，批准窗口此时不再生效。适用于 CI 或锁定式的审计运行。

## 验证回执

列出所有回执：

```bash
ls -la ./review-receipts/
```

用公钥离线验证每一份回执：

```bash
PUB=$(node -p 'JSON.parse(require("fs").readFileSync("./review-governance.key")).publicKey')
npx @veritasacta/verify@0.9.2 --replay-chain ./review-receipts/receipts.jsonl --key "$PUB"
```

退出码 0 表示所有回执均通过验证。退出码 1 表示某份回执验证失败，原因在于遭到篡改、密钥不对，或某一行格式有误。退出码 2 表示无法读取回执文件。

遭拒的调用根本不会执行，因此没有回执。要查看策略拦截了什么，在 Claude Code 内运行：

```
/list-pending
```

它列出本次会话中 PreToolUse hook 拦截的工具调用，并附上工具名称以及命令或路径。

## 示例：批准一次 PR 审查

```bash
# 1. Human reviews the agent's proposed comment
$ /list-pending
  Blocked in this session:
  - Bash "gh pr review 42 --approve --body 'LGTM'"
  - Bash "gh pr comment 42 --body 'Looking good'"

# 2. Human decides the first one is appropriate, approves it
$ /approve-review "Approving LGTM on PR 42 after visual inspection"
  ./.review-approved created

# 3. Agent retries the action; this time it succeeds
$ agent: gh pr review 42 --approve --body "LGTM"
  [receipt appended to ./review-receipts/receipts.jsonl, decision=allow]

# 4. Human closes the window
$ rm ./.review-approved
```

获准的调用带有一份签名回执，任何持有公钥的人都能离线验证。遭拒的尝试没有回执，且批准日志未签名，向审计人员展示留痕时请把这两点都考虑在内。

## 与 protect-mcp 组合使用

如果两个 Plugin 都安装了，各自的 `hooks/hooks.json` 会注册自己的 PreToolUse hook，Claude Code 在每次工具调用时都会运行两者：

```json
{ "type": "command", "command": "\"${CLAUDE_PLUGIN_ROOT}\"/hooks/evaluate.sh" }
```

每个 `evaluate.sh` 从 stdin 上的 hook payload 读取 `tool_name` 与 `tool_input`（Claude Code 不设置 `TOOL_NAME` 变量），并对各自的策略求值：protect-mcp 用 `./protect.cedar`，本 Plugin 用 `./review-governance.cedar`。

两个 hook 都必须放行，工具调用才能继续。任一策略中的 Cedar deny 都会拦下它。

## 规范

- **Ed25519**：RFC 8032（数字签名）
- **JCS**：RFC 8785（确定性 JSON 规范化）
- **Cedar**：AWS 的开放授权策略语言
- **IETF 草案**：[draft-farley-acta-signed-receipts](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/)
