---
description: 就一个任务编排并行 opencode worker 蜂群（worktree 隔离，合并由你完成）
allowed-tools: Bash(git:*), Bash(node:*), Read(*), Edit(*), Grep(*), Glob(*)
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`engineering/hivemind/assets/commands/swarm.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

你是免费 opencode worker 蜂群（swarm）的编排者（ORCHESTRATOR）。任务：$ARGUMENTS

PHASE 1 - PLAN（计划）
把任务拆成 2-5 个不碰相同文件的独立（INDEPENDENT）子任务。
为每个子任务选择一种 agent：scout（只读调研）、coder（写代码）、tester（只跑测试）。

PHASE 2 - ISOLATE（隔离）
只要有子任务要写文件：为每个写文件的 worker 各建一个 git worktree：
git worktree add "../<repo-name>-wt-N" -b swarm/N
记录每个 worktree 的路径。没有子任务写文件就跳过 worktree。

PHASE 3 - SPAWN（并行派生）
把所有 worker 调用作为并行 Bash 工具调用，在同一条消息里发出。
每次调用：

node "$HIVEMIND_HOME/scripts/oc-worker.mjs" --agent <agent> --dir <worktree-or-cwd> --timeout 900 "<SUBTASK>"

注意：
- scout worker 可以省略 --dir 以读取本仓库。
- coder/tester worker 必须各自带 --dir（worktree 路径）。
- 绝不让两个写文件的 worker 指向同一目录。

PHASE 4 - REVIEW（你亲自审查）
每行输出包含 {result, tokens}。对每个写文件的 worker 运行：
git diff main...swarm/N
逐行亲自审查这个 diff。你是唯一的合并者。

PHASE 5 - INTEGRATE（整合）
- 合并通过审查的分支：git merge swarm/N
- 拒绝：删除分支 + git worktree remove。
- 所有合并完成后运行测试套件。

PHASE 6 - REPORT（报告）
输出一张表：subtask | agent | tokens | outcome，然后给出所有 worker 的 tokens 总数，
以及你在审查期间做出的改动。标出你拒绝其输出的 worker 以及原因。

HARD RULES（硬性规则）：
- worker 的输出只能通过脚本输出的单行紧凑 JSON 进入你的上下文。
- worker 返回 ok:false 时，对同一目录重新调用一次；仍失败就放弃并报告。
- 绝不让原始 opencode NDJSON 流进入本对话。
- worker 之间永不共享目录。合并与审查永不委托他人。
