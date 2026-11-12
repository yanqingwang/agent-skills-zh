<!-- AUTO-GENERATED from checklist.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/plan-ceo-review/sections/checklist.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Checklist（runner 画像）

供 `bin/gstack-autoplan`（无人值守或 `light` 运行）使用的 CEO 阶段步骤
与必需输出；交互式运行完整读 `sections/review-sections.md`。

### 步骤
1. 范围与模式已确认（Step 0）；带决策清单进场。0A/0B 以 reality 行
   收尾：每个适用行一条 `REALITY:` 行
   （`gstack-plan-reality rows --phase ceo`），各带 file:line 回执。
2. 按序跑第 1-10 节；第 11 节仅在 `ui` 范围时跑，否则记录无 UI 的
   跳过。第 3 与第 7 节带 `security` 与 `perf` 范围。
3. 外部声音按其集成规则跑；逐条对账发现。
4. 下方的每个必需输出，然后是报告、日志与链式交接。

### 必需输出 → 产出节

| 输出 | 产出者 | 范围 |
|---|---|---|
| Review facts | Review facts | always |
| Reality rows（`REALITY:` 行、`PLAN_REALITY` 检查） | Reality rows | always |
| NOT in scope | "NOT in scope" section | always |
| What already exists | "What already exists" section | always |
| Dream state delta | "Dream state delta" section | always |
| Error & Rescue Registry | Error & Rescue Registry (from Section 2) | always |
| Failure Modes Registry | Failure Modes Registry | always |
| Scope Expansion Decisions | Scope Expansion Decisions | always |
| Diagrams | Diagrams (mandatory, produce all that apply) | always |
| Stale Diagram Audit | Stale Diagram Audit | always |
| Completion Summary | Completion Summary | always |
| Unresolved Decisions | Unresolved Decisions | always |
| Saved terminal report | Stage 2 — Save and verify the terminal report | always |
| Published summary | Stage 3 — Publish the Completion Summary | always |
| Review log row | Review Log | always |
| Next-skill handoff | Next Steps — Review Chaining | always |
| Design & UX findings | Section 11: Design & UX Review | ui |
