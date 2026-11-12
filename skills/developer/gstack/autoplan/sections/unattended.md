<!-- AUTO-GENERATED from unattended.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`autoplan/sections/unattended.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Unattended 画像

`SESSION_KIND: unattended`：由父级经
`~/.claude/skills/gstack/bin/gstack-autoplan` 驱动运行（`next`/`submit`/
`answer --gate-rev`/`export`；见 docs/unattended.md），只读产物，不读
散文。各阶段自行关闭，Eng 最后跑，外部声音经 `gstack-outside-voice`
运行，运行停在 `status=gate_pending`：绝不批准。完成检查是
`gstack-artifact validate <dir>/run.json`。以
`GSTACK_RESULT: skill=autoplan status=<status> run=<dir>` 收尾。
