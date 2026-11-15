> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/review/specialists/state-machines.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# State Machine Round-Trip Specialist 评审清单

范围：当 SCOPE_STATE_MACHINE=true 时（`gstack-state-matrix detect`：diff 新增或修改了 proposal、hold 或 approval 状态机）
输出：每个状态机先输出一条 matrix 记录，然后每个缺口一条发现，每条为独立一行的 JSON 对象。

Matrix 记录（不是发现；父代理用 `gstack-state-matrix check` 检查它）：
{"specialist":"state-machines","matrix":{"machine":"name (path)","kinds":["kind",...],"actions":["accept","drop",...],"cells":[{"kind":"kind","action":"accept","row":"the resulting rows after the action","test":"path/to/test:LINE"}]}}
没有测试覆盖的 cell 用 `"test":null`。

发现 schema：
{"severity":"CRITICAL","confidence":N,"path":"file","line":N,"category":"state-matrix","summary":"untested cell: <kind> × <action> → <row>","fix":"...","fingerprint":"path:state-matrix:<kind>:<action>","specialist":"state-machines","cell":{"kind":"<kind>","action":"<action>"}}
可选字段：test_stub、evidence。
若 diff 未新增或修改任何 proposal、hold 或 approval 状态机：只输出 `NO FINDINGS`，不输出任何其他内容。

---

## 本 specialist 为何存在

一个通过了完整 gate 的变更删除了用户数据：接受一条 "deactivate" 或同 claim 的 "replace" proposal 走进了 "remove" 路径，因为只有 remove 被测过。共用同一分支的多个 kind，只要其中之一被测过就显得有覆盖。本评审把每个 kind × owner action、每个组合应留下的行、以及证明它的测试全部写下来，让未测的 cell 在合并前就被点名。

## 构建矩阵

1. **找到状态机。** 一个带有 kind（type、enum、tag）和 pending 状态、由 owner action 结算的记录：proposals、holds、approvals、moderation 或 review 队列、invitations。读 diff 之后的完整代码，而不只是 hunk。
2. **列出 settle 路径在 diff 之后处理的每个 kind**：该 type 或 enum、每个 `case`、每个 dispatch-table key。落入相邻分支的 `case` 自成一个 kind。当 diff 改动了共享路径时，也要包含 diff 未新增的 kind。
3. **列出结算 pending 记录的每个 owner action**：accept 或 approve、drop 或 reject，以及任何其他（expire、withdraw、release、hold）。
4. **为每个 kind × action 写出结果行**，依据是 kind 的含义、owner 的期望，而不是代码的实际行为：目标记录（删除、保留、停用、重写）与 proposal 自身的状态。Deactivate 保留记录并关闭其标志；same-claim replace 保留它；只有 remove 才删除；drop 不动目标。
5. **把每个 cell 映射到一个测试**，该测试要恰好执行该 kind 与 action，并断言结果行，写成本次 checkout 中的 `path:line`。相邻 kind 的测试、只检查 status 字段的测试、或 mock 掉 store 的测试都不覆盖该 cell。没有覆盖时写 `null`。绝不编造路径。

## 发现

- **未测 cell（CRITICAL；本规则的 High 档）。** 每个 `"test":null` 的 cell 一条发现，携带 `cell`、写在 `summary` 里的期望行，以及一个先结算该 kind 的 pending 记录、再断言该行的 `test_stub`。
- **行不符（CRITICAL）。** 当代码留下的行与第 4 步不同（例如 deactivate 却删除了记录）时，单独报告一条发现，携带同一 `cell` 与走进错误路径的那一行。
- **kind 合并（CRITICAL）。** 把多个 kind 送进同一条破坏性路径的分支，即使某个 kind 有测试覆盖，也要在该行报告一条发现。

## 绝不

- 绝不因为相邻 kind 的测试经过同一个函数就标记 cell 已覆盖。
- 绝不从清单中删掉 kind 或 action 来缩小矩阵。
- 绝不输出散文；父代理只解析 JSON 行。
