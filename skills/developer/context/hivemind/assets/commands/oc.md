---
description: 把单个任务委托给一个 headless opencode worker（免费模型）
allowed-tools: Bash(node:*)
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`engineering/hivemind/assets/commands/oc.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

把这个任务委托给一个（ONE）opencode worker。任务：$ARGUMENTS

原样运行以下命令：

node "$HIVEMIND_HOME/scripts/oc-worker.mjs" --timeout 600 "$ARGUMENTS"

然后：
1. 解析输出的单行 JSON：字段为 {ok, result, tokens, cost_usd, duration_ms}。
2. 若 ok:false，用一句话向我报告 stage + error，然后停止。
3. 若任务是只读的，为我简洁地总结结果。
4. 若任务写了文件，在我提交任何内容之前，先运行 git diff 并向我展示改了什么。

不要自己重跑 opencode，不要解析原始流，不要再派生 worker。
多 agent 工作请改用 /swarm。
