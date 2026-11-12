---
description: 多视角代码审查小组：N 个并行审查者审查同一个 diff，按共识过滤
allowed-tools: Bash(git:*), Bash(node:*), Read(*)
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`engineering/hivemind/assets/commands/review-panel.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

你是代码审查小组（review panel）的编排者（ORCHESTRATOR）。审查对象：$ARGUMENTS

SETUP（准备）
1. 抓取 diff：git diff（或 `git diff main...<branch>`，或用户点名的 PR/commit）。
   存进一个临时文件，并记录其统计信息（文件数、新增行数、删除行数）。
2. 生成 run id：hive-<timestamp>。

PANEL（并行评审；所有 Bash 调用放在同一条消息里，只读，不需要 worktree）：
node "$HIVEMIND_HOME/scripts/oc-worker.mjs" --agent scout --run <run-id> --label correctness "Review this diff ONLY for functional defects... <paste diff under 8k chars, else instruct worker to run git diff itself>"
再以 --label security 发起一次（注入、授权、密钥、不安全的反序列化），
以 --label performance 发起一次（N+1 查询、热点循环、内存分配、无界查询），
以 --label style 发起一次（约定漂移、命名、死代码）。

每个视角的提示词都以这句话收尾："Report ONLY defects as bullet lines 'file:line - issue'. No praise, no summaries."

AGGREGATE（汇总）
把所有评审 JSON 行通过管道送入：
node "$HIVEMIND_HOME/scripts/oc-aggregate.mjs" --findings-only
共识发现（多个视角同时指出）= 高置信度。先报告这些。

FALLBACK: opencode worker 失败两次（exec/api 阶段）时，亲自直接审查这个 diff，并明确说明。
REPORT: 结论行（SHIP / FIX FIRST / BLOCK）、共识问题表、仅单一视角发现的问题、消耗的 tokens。
