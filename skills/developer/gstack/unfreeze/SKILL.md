---
name: unfreeze
version: 0.1.0
description: 清除 /freeze 设置的冻结边界，重新允许编辑所有目录。（gstack）
triggers:
  - unfreeze edits
  - unlock all directories
  - remove edit restrictions
allowed-tools:
  - Bash
  - Read
---

> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`unfreeze/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

<!-- AUTO-GENERATED from SKILL.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->

# /unfreeze — 清除冻结边界

移除 `/freeze` 设置的编辑限制，重新允许编辑所有目录。

```bash
GSTACK_STATE_ROOT=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT); : "${GSTACK_STATE_ROOT:?gstack-paths failed; reinstall with ./setup or /gstack-upgrade}"
mkdir -p "$GSTACK_STATE_ROOT"/analytics
echo '{"skill":"unfreeze","ts":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","repo":"'$(basename "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || echo "unknown")'"}'  >> "$GSTACK_STATE_ROOT"/analytics/skill-usage.jsonl 2>/dev/null || true
```

## 清除边界

```bash
bash "$HOME/.claude/skills/gstack/freeze/bin/freeze-state.sh" clear
```

这是用户明确请求的移除操作，不是调查清理。共享写入器会将其与获取、替换以及属主校验的释放串行化。遇到 `FREEZE_BUSY` 或意外状态时，保持一切原样并报告恢复方式；绝不直接删除状态或可能仍活跃的变更锁。

把结果告诉用户。注意，`/freeze` 的 hook 在本会话中仍处于注册状态——由于
状态文件已不存在，它们只会放行所有操作。要重新冻结，
请再次运行 `/freeze`。
