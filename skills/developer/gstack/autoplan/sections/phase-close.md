<!-- AUTO-GENERATED from phase-close.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`autoplan/sections/phase-close.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

当前阶段的评审工作结束时重新读本节。使用该阶段退出时绑定的阶段、修订
检查点与方法论路径。本流程把回读、验证与发布作为三个独立操作。在内联
sections 的宿主上，每次退出都重读已安装 Autoplan SKILL.md 中的这个
close 块；它们没有单独的 phase-close.md 文件。

1. **完成并保存评审。** 要求该阶段完整的方法论/section Read、必需输出、
   成功写入与评审者终局结果。把已完成原生评审的 INPUT 与其 voice
   快照相匹配。评审者未完成则该阶段保持开放。对失败的原生尝试应用该
   阶段的失败策略；不可用/禁用的声音拿不到完成分。记录耗时：
   `~/.claude/skills/gstack/bin/gstack-autoplan-timing close --run <RUN_ID>
   --phase <PHASE> --out "$_AP" --outside-s <N> --native-s <N>`
   （timing.json；临时状态根会跳过 analytics 追加并打印一行说明）。
2. **对账已接受要求。** 把本阶段接受的每个行为、条件、测试与手工清单
   记入该阶段的 accepted 块。品味类保持暂定；用户挑战保留原始要求。
   `None` 记录必须解释实现为何保持不变。本次调用的修订检查点保持固定，
   压缩之后也一样。
3. **准备本阶段的 close packet。** 用退出时的 phase/checkpoint 运行：
```bash
bun "<SNAPSHOT_TOOL>" prepare-close "<PHASE>" "<ACTIVE_PLAN>" "<AMENDMENT_CHECKPOINT>" "<RESTORE_PATH>" "<methodologyPath>"
```
这会应用已接受要求，导出一个不可变 packet，含完整当前实现、固定检查
点、哈希与阶段专属的 `report` 字段。盲评输入保持不变。这些是下方第
4-6 步的输入；准备本身不执行它们。
4. **读完整的当前 packet。** 对返回的每个 `readRanges` 条目，用该条目
   精确的 `offset` 与 `limit` 对 `closePacketPath` 发起 Read。全部范围
   读完直到 EOF。只读被编辑的尾部不满足本步；以前的快照同样不行。某
   个结果被截断就读缺失的范围。某次 Read 失败就修复它并读完全部缺失
   范围。没有拿到结果的请求不得推进。最后一次成功 Read 之后，就地执行
   第 5 步。
5. **验证当前实现。** 把完整当前实现与已接受决策、来源要求、条件、
   测试及必需输出逐项比对。保留性检查只证明字节；计数、哈希、关键词
   探测和一句存下的"Read-back"都替代不了这项语义评审。评审历史留在
   Review record。复查第 1 步的前提。任何前提不完整就保持该阶段开放，
   补齐缺失工作。发现遗漏先修复，然后用同一检查点重新生成 packet，
   发布前读完整的新 packet。之后任何实现或已接受决策的编辑都回到
   第 3 步，压缩之后也一样。
6. **发布父级报告。** 验证成功后，立即把下方填好的报告作为可见的父级
   assistant 文本发出，用真实的发现与声音状态，单独成一条消息，其
   唯一的工具调用是 Bash 空操作 `true autoplan-published <PHASE>`
   （无输出）。守卫只在报告之后跟着后续记录时才计数，所以这条消息是
   任何下一阶段工具调用之前的下一个操作。用 packet 的 `report` 字段、
   实际宿主的评审者名字；任一评审声音缺失时填 N/A；确认计数需要两个
   声音。仅当 `report.includeDxMetrics` 为 true 时才包含 DX 指标行。
   用 driver 的适用 scope/skip 规则解析 `report.next`。

**Phase <report.number> complete.**
[DX only: DX overall: <score>/10. TTHW: <observed> min → <target> min.]
Outside review: <completed: N concerns / unavailable / disabled>. Native subagent: <completed: N issues / unavailable>.
Consensus: <N/A (voice coverage missing) | X/<report.total> native+outside confirmed; Y disagreements → gate>.
Passing to <applicable report.next>.

7. **回到 driver。** 发出实际父级报告后，同一回合继续 driver。在稍后的
   消息里发起下一次受守卫的 `Read` 或 `Agent` 调用（下一阶段的 driver，
   或跳过消息之后的 Phase 4 任务聚合器）。只有 driver 推进阶段并发出
   适用的跳过消息；跳过绝不等于完成。不要等"继续"的答复。

已发出的会话消息才是第 6 步的产出。把它存进 ACTIVE_PLAN 或经 Bash
打印都不算发布。压缩之后，对账绑定的 packet 与实际发出的消息：已验证
但缺公告的阶段从第 6 步恢复；输入过期则回到第 3 步。helper 结果或
Read 既不完成验证也不完成发布。
