<!-- AUTO-GENERATED from handoff.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`ship/sections/handoff.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Step 18-H：不开 PR 的移交（自动化 lane）

运行不得开 PR 时（`--no-pr`、自动化 lane、或无人值守的父级如此指示），
以本节替代 pr-body 节。这里的任何东西都不发布。

1. 仅验证检查：像 pr-body 节那样，把 Step 16 的逐 lane
   pass/fail/skip 计数（点名 `requires-remote` lane）写入
   `.gstack/tmp/ship-gate.json`，然后（带其 Issue links flags；不发
   问）：
   ```bash
   ~/.claude/skills/gstack/bin/gstack-issue-links --base <base> --out .gstack/tmp/issues.json
   ~/.claude/skills/gstack/bin/gstack-ship-receipt write --base <base> --gate @.gstack/tmp/ship-gate.json --issues @.gstack/tmp/issues.json
   ```
2. 发送完成消息，标识符在前，按此顺序：`SHIP_RECEIPT:` 行与回执块
   （`pr: none`）；`branch:` 与 `sha:`（`git rev-parse HEAD`）、已推送
   或 `not pushed`；`inputs:` 计划或 issue、基础 SHA 与花费上限；
   `before/after:` 每个声称的指标一行，在 base 与本 SHA 上实测并附
   所用命令；`escalation:` 阻止合并的那一个条件（一个
   `requires-remote` lane、一条开放的门控发现、一个未验证的主张）或
   `none`。`issues:` 其各行、未晋升的候选与查询失败。
   完整线程 id（`jam_…`）可跨线程；标识符之前没有任何内容。
3. 跳过 Step 19 与 21。NO_VERSION 生效时以 `"version":null` 跑
   Step 20。

### 多 lane 运行

各 lane 在每步之后推一个 WIP commit，并对已推送的 SHA 设门。
