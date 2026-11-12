<!-- AUTO-GENERATED from flake.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`investigate/sections/flake.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Flake 配方

flake 是一个判定取决于它所守护代码之外因素的测试。铁律在此同样成立：
原因没被点名并探测之前，不重跑、不放宽超时、不重试、不跳过。

1. **在 main 上复现。** 在 worktree 里检出 `origin/<base>`
   （`git worktree add <dir> origin/<base>`），单独运行失败文件 N 次
   （N ≥ 10）。gstack 上用
   `bun --no-env-file --config=/dev/null run scripts/ship-measure.ts free --files <file> --reruns N`；
   其他项目就循环其单文件测试命令。先记录 main 上的 `failed/N`，再
   记录分支上的同一数字。在 main 上也复现的失败不属于本 PR；只在
   分支上出现的才属于它。
2. **原因在 PR 内还是外。** 对比两次运行的日志，从第一处分歧点命名
   依赖：时序、文件顺序、共享状态、网络、时钟、资源限额。"Flaky"
   是症状，从来不是原因。
3. **与最近 N 次绿色运行比指标。** 对 `<base>` 与分支各跑一次
   （`--branch <branch-name>`），针对跑失败分片的那个工作流；读测试
   旁边的时长或重试 token：
   ```bash
   gh run list --branch <base> --workflow free-tests.yml --status success --limit 20 --json databaseId,headSha,createdAt,updatedAt
   gh run view <run-id> --log | grep -F -- "<failing-test-file>"
   ```
   时长、重试数或失败测试第一次移动的那次运行给回归定日期；引用其
   `headSha`。
4. **强制探针。** 构造一个让测试按所述原因确定性失败的最小改动
   （注入延迟、钉死文件顺序、冻结时钟、耗尽资源）。展示探针输出在
   修复前失败、修复后通过。没有探针，就没有原因。
5. **绝不放松。** 放宽超时、加重试、放松断言或跳过都是门控放松
   （评审标签 RH-15）；修复在代码里或测试的隔离里，不在阈值里。
   **Flake 修复的数字。** 只动测试的修复（放宽超时、加重试、放松
   断言、跳过）必须给出 `P(fail | regression)`：当它守护的行为回归
   时，测试仍然失败的概率，改动前后各一个。从强制探针推导（故意
   破坏行为，跑 N 次，数失败），把两个数字写进 `## Flake evidence`。
   数字下降就是门控放松（评审标签 RH-15），需要 owner 决策，不是
   合并。
6. **只有原因已知且在 PR 之外才重跑**（基础设施、main 上已修复的
   污染者、服务方故障），并在 PR 正文说明。重跑遵循
   `ship-measure` 的纪律：有界、计数、记录日志、`flaky retry off`；
   免费重跑是诊断手段，从来不是绿灯。付费评测绝不重试
   （`test/helpers/periodic-exclude-data.ts` 的 `EVAL_POLICY`）。
7. **PR 正文的 `## Flake evidence`（任何 flake 修复必附）。** 探针的
   前后输出、main 与分支上的 `failed/N`、带首个移动 `headSha` 的
   `gh run list` 对比，以及给 owner 的路由注记：`fix in this PR` |
   `rerun; cause outside the PR: <what>` | `owner decision needed:
   <the relaxation and its P(fail | regression) before/after>`。

### 时序 flake（`TIMING_ASSERTION`）

失败行把流逝时间与界限比较，或先 sleep 再断言时（`gstack-pregate` 的
`timing` 检查打印为
`TIMING_ASSERTION: <file>:<line> <pattern>`）：

1. **同负载分布。** 每次运行都记录被断言的值，在 `origin/<base>` 与
   PR head 上以相同负载（同机、同并发、同一分片旁）各跑 N ≥ 20 次。
   报告两者的 min、p50、p95、max 与对界限的失败次数。PR head 上
   分布移动了，是 PR 内的回归；两边分布相同，是测试依赖机器负载。
2. **强制探针。** 注入负载造成的那份延迟（测量区间内经测试专用
   hook 的 sleep，或饿死 CPU），展示断言每次都失败。
3. **修测量，绝不修界限。** 改为断言结果、注入时钟、强制 deadline
   或带 deadline 的轮询，替代固定 sleep；复杂度界限对同次运行的
   基线测线程 CPU 时间。某个界限确实是契约时，该行携带
   `gstack-timing-ok: <reason>`。抬高界限不是修复。
4. **仅在持有外因证据时重跑：** 同负载分布显示 PR 无回归，且失败
   那次运行的负载有据可查（CI 日志、runner 指标）。两者都放进
   `## Flake evidence`。
