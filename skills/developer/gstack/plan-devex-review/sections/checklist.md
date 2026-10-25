<!-- AUTO-GENERATED from checklist.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/plan-devex-review/sections/checklist.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Checklist（runner 画像）

供 `bin/gstack-autoplan`（无人值守或 `light` 运行）使用的 DX 阶段步骤
与必需输出；交互式运行完整读 `sections/review-sections.md`。

### 步骤
1. Step 0 完成（persona、叙事、基准、魔法时刻、旅程、困惑角色扮演）；
   跑 DX Trend Check。
2. 按序运行 Pass 1-8：getting started、API/CLI/SDK 设计、错误与调试
   （Pass 3 的 agent-ready 错误契约：CAP4 Critical 与 CAP6 High 发现把
   分数钳在 4 与 6）、文档、升级路径、环境与工具链、社区、度量。
   Appendix 仅适用于 Claude Code Skill。
3. 每个未决发现一个决策循环；然后是下方的必需输出。

### 必需输出 → 产出节

| 输出 | 产出者 | 范围 |
|---|---|---|
| Developer Persona Card | Developer Persona Card | dx |
| Developer Empathy Narrative | Developer Empathy Narrative | dx |
| Competitive DX Benchmark | Competitive DX Benchmark | dx |
| Magical Moment Specification | Magical Moment Specification | dx |
| Developer Journey Map | Developer Journey Map | dx |
| First-Time Developer Confusion Report | First-Time Developer Confusion Report | dx |
| NOT in scope | "NOT in scope" section | dx |
| What already exists | "What already exists" section | dx |
| TODOS.md updates | TODOS.md updates | dx |
| DX Scorecard | DX Scorecard | dx |
| DX Implementation Checklist | DX Implementation Checklist | dx |
| Unresolved Decisions | Unresolved Decisions | dx |
| Review log row | Review Log | dx |
| Next-skill handoff | Next Steps — Review Chaining | dx |
