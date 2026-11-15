> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/qa/templates/functional-report-template.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 功能 QA 报告：{TARGET}

| 字段 | 值 |
|---|---|
| 日期 / 分支 / 修订 | {DATE / BRANCH / COMMIT AND WORKING-TREE INPUTS} |
| 调用方 / 权限 / 深度 | {qa-only, qa, review or ship; permitted writes; bound} |
| 面 / 范围 | {API, CLI, job, worker, webhook; changed and adjacent contracts} |
| 运行时 / 原生工具 | {VERSIONS AND REPOSITORY-SUPPORTED COMMANDS} |
| Fixture 归属 / 目的地 | {ISOLATED ROOT, STORES, DOWNSTREAM TARGETS} |
| 探测预算 / 受守卫命令时长 / 停止原因 | {CONFIGURED LIMIT / SUM OF CAPTURE durationMs / COMPLETE OR BOUND/BLOCKER} |

## 契约结果

| 契约与来源 | 精确探测 / 证据 | 预期 → 实测 | 结果 |
|---|---|---|---|
| {CONTRACT, DOC/TEST/USER SOURCE} | {COMMAND OR REQUEST, EVIDENCE PATH} | {OUTPUT AND DURABLE EFFECT} | pass / fail / blocked / not run / inconclusive / not applicable (reason) |

本功能小节不适用视觉分。混合报告中，浏览器小节的分数与证据要分开保留，并链接两个面的
replay 证据与回归基线。不得合并两者的分数或结果。

## 发现

### ISSUE-NNN: {Reproduced defect or setup blocker}

- 分类 / 严重级别：{PRODUCT DEFECT / SETUP / INCONCLUSIVE; IMPACT}。
- 预期契约与来源：{EXPECTED BEHAVIOR, NOT MERELY CURRENT IMPLEMENTATION}。
- 复现：{WORKING DIRECTORY; SAFE SETUP/RESET; ENVIRONMENT NAMES ONLY; EXACT COMMAND OR METHOD/PATH/HEADERS/BODY USING SYNTHETIC VALUES}。
- 实测：{EXIT/STATUS; STDOUT; STDERR; INITIAL/FINAL DURABLE STATE; REPLAY/RETRY ORDER}。
- 证据：{EXACT SAFE OUTPUT AND STATE PATHS; REVISION/RUNTIME; REDACTION AND REPRODUCIBILITY LIMITS}。
- 诊断 / 下一步：{CAUSAL EVIDENCE OR SPECIFIC PREREQUISITE; NO SPECULATIVE FIX}。

## 发现与永久测试

在本报告中链接每个 `exploration-NNN.json` 检查点，检查点在其下一次探测之前保存。
每个检查点收据会打印其 `link`；`.qa-evidence/NNN` 捕获文件夹不是检查点。
每个检查点用一条 Markdown 条目，例如：

- [checkpoint 001](exploration-001.json)：这条观察如何塑造了下一次探测。

使用真实文件名，以及相对本报告的路径（或其所属的绝对路径）；裸文件名或反引号文件名
不是链接。被取代的检查点作为历史收录，不作为当前通过的证据。
这些原始笔记随报告一起保留。

| 假设 / 发现 | 原生测试或提案用例 | 修复前的红证据 | 绿色 + 原有 + 相邻证据 | 父代理处置 |
|---|---|---|---|---|
| {OBSERVATION THAT CHANGED THE NEXT PROBE} | {UNIT / INTEGRATION / E2E; PATH OR REPORT-ONLY PROPOSAL} | {EXACT DEFECT FAILURE OR HEALTHY CONTRACT} | {ACTUAL RESULTS OR NOT RUN} | {AUTHORIZED CHANGE / SUGGESTION / DEFERRED} |

## 覆盖限制与清理

列出未执行的 charter、不可用的前置条件、被拒绝的影响、含糊的契约、不完整的观察与剩余
风险。不得把它们计为通过。写明已清理的受管进程/状态与遗留物。说明后续变更是否使证据
失效。Report-only 必须把提案与实际创建的测试分开标识。
