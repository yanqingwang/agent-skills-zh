---
description: 测试编队：把测试套件拆分给并行的 tester worker，并汇总出统一结论
allowed-tools: Bash(node:*), Read(*), Bash(npm:*)
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`engineering/hivemind/assets/commands/test-fleet.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

你是并行测试运行的编排者（ORCHESTRATOR）。目标：$ARGUMENTS（模块、路径或 "full suite"）

PLAN（计划）
1. 摸清测试布局（框架、测试文件/glob、调用方式）。
2. 把测试划成 2-4 个独立分组（按目录/模块）。预估各组运行时长是否均衡。
3. SAFETY CHECK（安全检查）：如果测试会绑定端口、写共享产物（缓存、快照、数据库）、
   或修改全局状态 -> 它们绝不能在同一目录里并发运行。这时改为每组建一个
   worktree（git worktree add ../<repo>-tf-N -b swarm/tf-N），或者退回顺序执行。
   拿不准就用 worktree。

SPAWN（在安全约束内并行派生）：
node "$HIVEMIND_HOME/scripts/oc-worker.mjs" --agent tester --run hive-<ts> --label tf-N [--dir <worktree-N>] --timeout 900 "<test invocation for group N>. Report PASS/FAIL line 1, then failures."

AGGREGATE: 把所有 JSON 行通过 oc-aggregate.mjs 汇总；合并成单一结论：
总 pass/fail 计数 = 各分组之和。任何一组出现失败 = 整个套件 FAIL。

FALLBACK: 编队不可用 -> 亲自完整跑一遍套件，按常规方式报告。
REPORT: 套件结论、分组表（group | tests | pass/fail | tokens）、失败详情。
