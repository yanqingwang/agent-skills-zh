<!-- AUTO-GENERATED from browser-verify.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`qa/sections/browser-verify.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

# 浏览器缺陷修复验证

本节仅用于浏览器缺陷。重跑原始交互与一条相邻的 happy path。Phase 5
的证据是"修复前"（交互缺陷用 `issue-NNN-result.jpg`，静态缺陷用标注的
`issue-NNN.png`）；现在捕获"修复后"。

交互类 bug 用 qa-patterns 里 `flow = true` 的 Phase 3 读取/流程脚本，
把动作与等待设为原始复现。静态缺陷用 `flow = false`。保留错误 hook、
快照、console 输出与 `GSTACK_STEP_OK` 检查。每条流从受影响的 URL 起，
在单脚本内跑完；标签页活不过脚本。

截图用新名字，结果用 `issue-NNN-after.jpg`（已存在就加后缀）。从打印
的 `ASIDE_DIR` 拷到 `$REPORT_DIR/screenshots/`，然后 Read 拷贝后的
截图。把快照树、`DIFF` 与 `CONSOLE_ERRORS=` 与修复前证据对比。

兜底路径下，把 browser-setup 的 `$B` 映射套用到同样的检查上。
功能性修复不加载本节。
