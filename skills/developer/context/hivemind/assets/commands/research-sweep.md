---
description: 并行调研扫描：N 个 scout 同时调查同一个问题的不同角度
allowed-tools: Bash(node:*), Read(*)
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`engineering/hivemind/assets/commands/research-sweep.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

你是调研扫描（research sweep）的编排者（ORCHESTRATOR）。问题：$ARGUMENTS

PLAN（计划）
把问题拆成 3-5 个相互独立（INDEPENDENT）的角度，例如：current-state-of-codebase
（代码库现状）、how-it-works-internals（内部工作机制）、alternatives-and-comparisons
（替代方案与对比）、known-pitfalls-and-bugs（已知坑与 bug）、docs-and-external-context
（文档与外部背景）。生成 run id：hive-<timestamp>。

SPAWN（并行派生；所有 Bash 调用放在同一条消息里）：
node "$HIVEMIND_HOME/scripts/oc-worker.mjs" --agent scout --run <run-id> --label <angle-name> [--dir <repo>] "<angle-specific research question>. Cite file:line or URLs for every claim. Max 150 words."

scout 可以用 webfetch 获取外部文档；它们不能编辑任何内容。

如果任何调用报错，在两波之间 CHECK PROGRESS（检查进度）：
node "$HIVEMIND_HOME/scripts/oc-status.mjs" <run-id>

SYNTHESIZE（综合），由你亲自完成（不要只是拼接）：合并成一个连贯的答案，
显式化解矛盾（同时列出两种说法 + 各自来源），列出没有任何 scout 能回答的开放问题。

FALLBACK: worker 失败两次 -> 亲自内联调研该角度，并标记 [orchestrator-sourced]。
REPORT: 先给综合后的答案，然后是证据表（claim | source | confidence），最后是尚存的空白。
