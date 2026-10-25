<!-- AUTO-GENERATED from measure.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`ship/sections/measure.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## 先测量后修复循环（付费评测变红，或免费套件分片失败）

这里的每次重跑都是**诊断，不是判定**：它绝不改变那次失败运行的已记录
判定，其产物在 `.context/ship-measure/` 下标为 `diagnostic`（绝不进
评测历史），lane 的判定只来自最后那次完整门控运行。绝不为拿到通过而
提预算、降阈值、加判定重试或跳过 case。
下文 `ship-measure` 指
`bun --no-env-file --config=/dev/null run ~/.claude/skills/gstack/scripts/ship-measure.ts`。

**免费套件分片失败（Step 5）。** 在断言失败是既有问题或推送之前，用
`ship-measure free --files <f1,f2,...>` 按运行顺序重跑该分片的精确文件
清单（gstack 本地运行用 `--shard <i>`）：重跑 10 次，第 1 次单独跑作
基线、其余标记 parallel，各自独立 HOME 与状态根，关闭 flaky 重试，
10 分钟上限。设置了 `UBICLOUD_API_KEY` 的
`ship_rerun_backend=ubicloud` 会把它们跑在一台 Ubicloud VM 上。runner
不支持文件清单时，把整条失败命令重跑 10 次。报告通过率、完成计数
（例如 10 个在上限内完成 6 个）与一份失败捕获，然后继续分诊。

**付费评测变红（Step 6）。** 对每个红 case：

1. **分类。** 读红行的原因、证据与 Expected/Received
   （`failure_cause`、`failure_detail`；gstack：
   `bun run eval:pass-rates --run <run> --case <id>`）。点名它：本分支
   的产品变更、检测器或执行器缺陷、fixture 缺陷、提供方事件，或模型
   未命中。检测器修复先做一次免费回放测试再谈付费尝试。基础设施性质
   的红（提供方故障、runner 丢失）可跳过测量：
   `ship-measure skip --case <id> --reason "<why>"` 在 PR 正文里把它标
   为 `unmeasured`。它绝不算通过。
2. **展示计划。** 打印 `ship-measure table`（尝试数、按类别的门槛与
   预算，来自 `ship_measure_*` gstack 配置键）与估算：按通过率历史乘
   尝试数的单次成本，或"估算未知"。
3. **测量。** `ship-measure measure --case <id> --round baseline [--cost-per-trial <usd>]`
   在当前 head 上按其类别的次数并行单独跑该 case，走项目文档化的单
   case 评测命令 `--command '<command> {case}'`（以 Step 4 找测试命令
   的方式找到；gstack 不需要且接受 judge id）。没有文档化命令时问
   一次并把答案记进报告。exit 2 需要批准：带其理由问一次，然后加
   `--approved` 重跑。
4. **按 exit code 决策**（MEETS 9/10，MEETS-qualified 8/10 且每个红
   都符合豁免，EXTEND 7/10；behavior 11/12、10/12、9/12）：
   - 0：MEETS 或 MEETS-qualified；完成。
   - 5：需要分类。从捕获逐条记录所列的红：
     `ship-measure classify --case <id> --round <r> --trials <2,5> --class <class> --evidence "<path:line>"`。
     豁免类：`provider`（仅限该尝试自身的提供方错误）、`judge-noise`、
     `model-miss`（引用行号）。修复轮：`timeout`、`hang`、
     `regression`、`fixable`。`unclassified`：已复核、无证据。
   - 6：EXTEND。`ship-measure extend --case <id> --round <r>` 一次，
     在未改动的树上；绝无第三批。
   - 1：BELOW，进入修复轮。
5. **在原因处修。** 从 `.context/ship-measure/<case>/<round>/tNN/` 的
   捕获对失败尝试做根因分析，改动那个原因。
6. **重测。** `ship-measure measure --case <id> --round round-<n> --fix "<cause and change>"`，
   然后回到第 4 条。只有点名了因果变更、且收尾测量中的每次失败都有
   解释，才能宣告 case 修复；报告"修复后在 <cause> 处实测 k/n"，
   绝不说成已证实的比率。
7. **停止。** exit 3 是点名的红（轮数上限、预算、或两批作废）：停止、
   不推送，用 `ship-measure report` 带全部尝试报告。

**门控只跑一次。** 每个红 case 都测到目标及以上时，完整门控只跑一次
（Step 6 第 2 条）。项目的 CI 在 push 时跑该门控（gstack：PR 的
`evals` 工作流）时，这次 push 就是门控运行：push 并读那次运行，不要
再启动门控命令（gstack 的 `bun run eval:bg:pr` 在已推送 head 上会派出
第二次付费运行）。把 `ship-measure report` 表（每 case 估算与实际花
费）放进 PR 正文。
