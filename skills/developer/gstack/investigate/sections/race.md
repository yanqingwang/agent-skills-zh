<!-- AUTO-GENERATED from race.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`investigate/sections/race.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## 竞态配方

竞态是两个执行者在触碰共享状态，而顺序没人保证。修复之前先让它变得
确定。

1. **时序探针。** 在共享状态（文件、行、map、锁）的每次读写处记录
   单调时间戳（`performance.now()`）与执行者 id。竞态表现为交错写入，
   或一个执行者在另一个执行者的检查与写入之间读到了中间值。探针
   输出留作证据。
2. **强制交错。** 在疑似时点给其中一个执行者注入 `await` 或 sleep
   （经测试专用 hook 或环境变量），让另一个执行者跑进这个窗口。此后
   bug 必然每次复现；若不是，窗口在别处。
3. **并发写模板。** 同时驱动 N 个写者，断言的是不变量，不是"没有
   报错"：
   ```ts
   const results = await Promise.allSettled(Array.from({ length: N }, (_, i) => writer(i)));
   // exactly one winner | all N applied | file or row intact | lock released and owner recorded
   ```
   在强制交错下以 N ≥ 8 运行；保留注入的交错，这个模板就是回归
   测试。
4. **修复形状。** 用原子原语：`wx` 创建、compare-and-swap、
   `UPDATE … WHERE old_value = ?`、带 owner token 与过期 owner 规则的
   锁。把 check-then-act 的窗口缩小一点不算修复。改动之后重跑第 3
   步，贴出两份输出。
