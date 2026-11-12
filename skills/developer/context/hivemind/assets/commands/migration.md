---
description: 迁移协调器：并行的逐文件/分块 worker，按顺序合并并验证
allowed-tools: Bash(git:*), Bash(node:*), Read(*), Edit(*)
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`engineering/hivemind/assets/commands/migration.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

你是本次迁移的编排者（ORCHESTRATOR）。任务：$ARGUMENTS

PLAN（计划）
1. 确定文件集或分块（例如：所有 import 旧 API 的文件）。worker 数量上限 5 个；
   文件更多时，按依赖/相似度分成 <=5 批。
2. 生成 run id：hive-<timestamp>。
3. 每批创建一个 worktree + 分支：git worktree add ../<repo>-mig-N -b swarm/mig-N

SPAWN（并行派生；每批一个 Bash 调用，全部放在同一条消息里）：
node "$HIVEMIND_HOME/scripts/oc-worker.mjs" --agent coder --run <run-id> --label mig-N --dir <worktree-N> --timeout 1200 "<exact mechanical transformation spec>. Touch ONLY these files: <list>. Do not commit."

除文件清单外，变换规格（transformation spec）必须对所有 worker 完全一致（IDENTICAL）：一致性胜过聪明。

MERGE（合并；按顺序执行，只能由你完成）：
按 N 的顺序逐个进行：亲自审查 git diff main...swarm/mig-N -> 合并 -> 亲自解决
全部冲突（解决冲突绝不委托他人）-> 删除 worktree。

VALIDATE（验证；全部合并完成后，由单个 tester worker 执行）：
node "...\oc-worker.mjs" --agent tester --run <run-id> --label validate --dir <repo> "Run <test command>. Report PASS/FAIL + failures."

FALLBACK: 某一批失败两次 -> 亲自内联完成该批迁移。
REPORT: 表格（batch | files | tokens | outcome）、你解决的冲突、测试结论。
