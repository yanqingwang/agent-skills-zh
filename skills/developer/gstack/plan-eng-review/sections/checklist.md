<!-- AUTO-GENERATED from checklist.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/plan-eng-review/sections/checklist.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Checklist（runner 画像）

供 `bin/gstack-autoplan`（无人值守或 `light` 运行）使用的工程阶段步骤
与必需输出；交互式运行完整读 `sections/review-sections.md`。

### 步骤
1. 范围挑战（A 评估、B 选择器、C 发现）配决策流程；每个既往阶段的
   共识都在评审前进 prompt。A 以 reality 行收尾：每个适用行一条
   `REALITY:` 行（`gstack-plan-reality rows --phase eng`），各带
   file:line 回执。
2. 按序跑第 1-4 节：架构、代码质量、测试、性能（`perf` 范围）。外部
   声音之后继续。
3. 最终规划决策，然后按序执行下方的收尾序列。

### 必需输出 → 产出节

| 输出 | 产出者 | 范围 |
|---|---|---|
| Review body | Output reference — review body | always |
| Reality rows（`REALITY:` 行、`PLAN_REALITY` 检查） | Reality rows (why each exists) | always |
| NOT in scope | "NOT in scope" section | always |
| What already exists | "What already exists" section | always |
| Diagrams | Diagrams | always |
| Failure modes | Failure modes | always |
| Worktree parallelization strategy | Worktree parallelization strategy | always |
| Test Plan | 3. Test review | always |
| Performance findings | 4. Performance review | perf |
| Unresolved decisions | Unresolved decisions | always |
| Completion summary | Completion summary | always |
| Review log row | Review Log | always |
| Next-skill handoff | Next Steps — Review Chaining | always |
| Learnings | Learning hooks | always |
