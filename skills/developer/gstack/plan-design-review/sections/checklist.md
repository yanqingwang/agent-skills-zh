<!-- AUTO-GENERATED from checklist.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`plan-design-review/sections/checklist.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Checklist（runner 画像）

供 `bin/gstack-autoplan`（无人值守或 `light` 运行）使用的设计阶段步骤
与必需输出；交互式运行完整读 `sections/review-sections.md`。

### 步骤
1. 范围已确认，DESIGN.md（存在时）已读；延续既往决策。
2. 按序运行 Pass 1-7，绝不压缩：信息架构、交互状态、旅程与情绪弧、
   AI slop 风险、设计系统对齐、响应式与可访问性、未决设计决策。
3. pass 之后：存在生成 mockup 时更新之。
4. 每个未决发现一个决策循环；然后是下方的必需输出。

### 必需输出 → 产出节

| 输出 | 产出者 | 范围 |
|---|---|---|
| NOT in scope | "NOT in scope" section | ui |
| What already exists | "What already exists" section | ui |
| TODOS.md updates | TODOS.md updates | ui |
| Completion Summary (lowest pass score) | Completion Summary | ui |
| Unresolved Decisions | Unresolved Decisions | ui |
| Approved Mockups | Approved Mockups | ui |
| Review log row | Review Log | ui |
| Next-skill handoff | Next Steps — Review Chaining | ui |
