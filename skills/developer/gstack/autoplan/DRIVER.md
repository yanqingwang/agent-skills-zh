> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/autoplan/DRIVER.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

<!-- AUTO-GENERATED from autoplan/DRIVER.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
# /autoplan driver：由父代理运行评审循环

当你（任意宿主上的父代理）通过 `gstack-autoplan` 驱动一次无人值守的 /autoplan 运行时，读本文件而不是
`autoplan/SKILL.md`：评审人是你要派发的 subagent，runner 负责保存状态。命令位于 `<root>/bin/`，其中 `<root>` 是
容纳本 `autoplan/` 目录的文件夹；`gstack-autoplan --help` 与第一次 `next` 会打印 `DRIVER: <root>/autoplan/DRIVER.md`。执行每条命令时都要带上安装器打印的 `GSTACK_LAUNCH` 赋值：在运行命令的 shell 里 `. <它打印出的 GSTACK_LAUNCH_FILE>`，
绝不用 `export $(...)`、`env`、`printenv`，也不在工具围栏里裸用 `set`（裸 `export` 会打印所有变量，包括凭据）。只读打印行和文件，不读散文：每条工作流
命令以 `GSTACK_RESULT: skill=autoplan status=<s> run=<dir>` 结尾，每条错误行以 `(<CODE>)` 结尾。

## 阶段与范围

顺序：ceo → design → dx → eng。Design 仅在 UI 范围下运行，DX 仅在 DX 范围下运行，Eng 总是运行且最后。
第一次 `next` 接受范围标志：`--ui`、`--no-ui`、`--no-dx`、`--developer-tool`、`--agent-primary`、`--docs-only`。`--developer-tool` 与 `--agent-primary` 只启用 DX。
第一次 `next` 会打印 `SCOPE: ui=… (terms; visual; files) dx=… (detected) docs_only=yes|no (<s>) source=ui:<s>,dx:<s>`
（每项取值为 `flag`、`marker` 或 `detected`）。Docs-only 模式（`--docs-only`，或 Implementation plan 的每个路径都是 README*、CHANGELOG*、
TODOS*、docs/**（不含 docs/*-policy.md），或 skill 目录之外的其他 markdown）只以 native voice 运行 CEO，然后运行 Eng。UI 需要 Implementation plan 中出现渲染文件路径（包括一个具名的非测试 `.ts`/`.js` 文件，其中含有带标签的 `html`、`css` 或 `svg` 模板，如 Lit 或 htm），或 UI 术语紧邻
视觉名词。要在同一计划的后续运行中沿用标志，需由你自己把它打印的 `SCOPE_PIN:` 标记
（`<!-- gstack-autoplan-scope: … -->`）加为计划的第一行；gstack 从不写计划。**Kinds（R65），仅第一次 `next` 生效。** `--kind fix` 不评审任何东西：它打印 `AUTOPLAN: not needed (bug fix; R65)`、一行 `PROOF:` 和 `GSTACK_RESULT: skill=autoplan status=skipped run=-`，不写任何文件，也不需要 `--out` 或 `--plan`；PR 仍然要带上该 bug 的证据，即在当前 main 上的复现，或先写好的失败测试。`--kind feature` 是 Capy 上（`GSTACK_CAPY=1`）未指明 kind 的无人值守运行的默认值，即精简运行。它的 `phase_order` 只含 `eng`，配一个 native 评审人，其提示词合并了 CEO 与 Eng 视角（仅当范围检测到时才加 Design 或 DX），每部分是简短角色或简报加上该评审 skill 的清单，绝不用该 skill 自己的方法，总是询问"是否涉及外部条款、许可或权利？"并展示草稿代码。草稿是从 merge base 用 `--base <ref>` 计算的 `git diff`（默认：`gstack-diff-scope` 的 base，绝不使用指向已检出分支的 `origin/HEAD`），包含未跟踪文件、排除运行目录，写入快照为 `draft.diff` 并做哈希；尚无代码时打印 `DRAFT: none (<why>)`。第一次 `next` 打印 `LEAN:`，每个开启的阶段打印 `DRAFT:`；评审人 INPUT 之后的那一行必须是 `DRAFT: <sha256>` 或 `DRAFT: none`，否则 submit 拒绝它（`RESULT_RECEIPT_MISSING`）。精简运行没有外部 voice，`--max-rounds 1`，无 carry 检查，门限修订仅一轮：`revise --incorporates` 应用已接受的变更而不重新评审并予以批准。`--full` 恢复所有阶段和两种 voice：每个 native 评审人拿到五问简报和其阶段的清单，每个外部评审人拿到单段角色描述，两者都不使用该 skill 自己的方法。不在 Capy 上，或处于交互会话时，默认仍是 full。

## 循环

1. `next` 按每个 voice 打印一行 `ATTEMPT: <id> phase=<p> voice=native|outside prompt=<file> result=<file>`。
   把 native 提示词派发给你的模型上的一个 subagent，把外部提示词派发给另一模型族上的一个 subagent（或运行 `gstack-outside-voice run`）。各自写入 `result=`。第一次 `next` 还会打印 `REVIEW_ESTIMATE:`（评审最多可用的尝试次数与预留额度）。
2. 每个 voice 恰好提交一次（`BOUND:`）。两个 voice 都提交即关闭该阶段（`PHASE_CLOSED:`）。
3. 重复 `next` 直到 `status=gate_pending`（`GATE: gate_rev=<n>`）；用 `gstack-gate render <dir>/gate.json --all` 渲染并转发每一页，包括 `GATE:` 下打印的两行成本信息：`GATE_SPEND:`（已花费、最坏情况、上限、余量、尝试次数；宿主 subagent 的尝试按 unknown 计价并按其预留额度入账，因此要从宿主的成本视图引用其真实数字）和 `GATE_REC_COST:`（`rec` 可重开的阶段及其估算值，为上界；`--json` 中的 `gate_cost`）。
   你绝不替所有者批准门限。默认提供 `rec`（每条建议，包括计划变更）。
4. 用 `answer` 携带所有者的回复作答，并加 `--by human`（所有者亲自键入了这些 token）或 `--by agent:<id> --owner-reply "<他们的话>"`（你转述）；缺 `--by` 时无人值守运行会拒绝（`ANSWER_BY_REQUIRED`）。`APPLY: <id> <title> -> <change>` 行是被接受的计划变更（状态 `amend_pending`）：编辑计划，然后 `revise`（打印的 `NEXT:` 会指明），或当该行表明无需编辑计划时用 `revise --settle <id>`。在此之前 `next` 以 `PLAN_AMEND_PENDING` 拒绝，且 `export` 不会把运行标记为完成。
5. `REOPENED: <phases>` 表示再次循环 `next`（Eng 最后）。`APPROVED:` 表示执行 `export`（`DISPATCHES: <n> est_input_tokens=<k>`，为相对值）。
6. 轮次：默认一轮；仅 High 或 Critical 发现才允许第二轮；上限 2（`--max-rounds`）。某次 `revise` 的所有决定都低于 High 时，打印 `APPLIED: <ids> without re-review (below High)`。到达上限且仍有 High 未决时，打印 `ESCALATE: evidence sufficient, decision needed`：转发它，绝不再索要一轮评审。
7. Carry-forward（[docs/unattended.md#carry-forward](../docs/unattended.md#carry-forward)；第一次 `next` 用 `--no-carry-forward` 退出）：后续门限若没有提出新问题，则沿用前一门限中所有者的话（`CARRIED:`，然后 `APPROVED:`）；只添加平实 ELI5 行的计划编辑按 K1 的 `autoplan-regate` 免停通行（`NO_STOP:`；在 /ship 之前运行 `gstack-no-stop import --from <dir>/no-stop.json`）；`CARRY: no (<why>)` 留给所有者处理；`CARRY_CHECK:` 表示由另一模型族的一名评审人读取打印出的 delta 提示词，然后 `check --out <dir> --attempt <id> --result <file> --model <id>`（或 `--unavailable "<reason>"`）。

### 在 Capy 上

- 始终驱动 `gstack-autoplan`；绝不手工改编 `autoplan/SKILL.md`。你手工评审过的计划不是一次 autoplan 运行：不要那样呈现它。
- 每个提示词以 `GSTACK TRAILER` 块结尾：评审人在自己的机器上运行 `--for review-voice` 安装（无需 ./setup，无需 skills；已缓存时只需几秒），并以 `gstack:` 行开始其回复。绝不要告诉评审人无需安装；把每位评审人的行连同其结果一起转发，缺失的行按 `gstack: fail not-installed` 处理。
- 把 `GSTACK_AUTOPLAN_CHECKPOINT_DIR` 设为私有的 project-user Drive 文件夹（或用 `gstack-config set autoplan_checkpoint drive` 为每次运行启用），使运行能在换机后存活：静止时、每次绑定 voice 后、每次阶段转换后都会发布一个世代；用 `resume --out <新目录> --from <dir>/<run>` 恢复，它绝不重新派发已绑定的 voice。
- 计划要带 `## ELI5`（5-10 句平实陈述）、`## Before → after`、`## Why it matters`、`## What caused this work`、`## Big decisions`；把打印出的 `RELAY: gstack-owner-brief render --captain` 输出转发给你的 Captain（或本人），然后在 `answer` 之后运行 `gstack-approvals import --autoplan <dir>`（堆叠式计划用 `--stack <b1,b2,...>`；见 `capy/skill/gstack/captain.md`）。

### 命令

- `gstack-autoplan next --out <dir> --plan <plan.md> [--kind feature|--full] [--base <ref>] [scope flags] [--light] [--spend-cap <usd>] [--max-rounds <n>] [--estimate-usd <n>] [--scaffold] [--ceo-only]`
  首次调用：初始化运行，打印 PHASE:、SCOPE:、DRIVER: 和每个 voice 一条 ATTEMPT:；--kind feature（无人值守 Capy 运行的默认值）即上述精简运行，打印 LEAN: 和 DRAFT:；--full 保留所有阶段和两种 voice；单独的 `next --kind fix`（不带 --out 或 --plan）不评审任何东西并以 `status=skipped run=-` 结束；--max-rounds 限制每阶段的评审轮数（无人值守默认 2）；带 --spend-cap 的运行（无论何种会话类型，或任何无人值守 Capy 运行）为每次尝试给每个 voice 预留 5.00，因此上限会生效；--estimate-usd <n> 设定该预留额度，运行会将其保留给后续阶段；--ceo-only（仅限命令行，绝不作为范围标记）单独评审 CEO，并以 `<dir>/ceo-review.md` 结束于 `status=reviewed`（`REVIEWED:`）：没有门限，且门限动词会拒绝它（`CEO_ONLY_NO_GATE`）。
- `gstack-autoplan run --out <dir> --plan <plan.md> --native-model <id> --outside-model <id> --native-runner api --runner api [--max-tokens <n>] [--spend-cap <usd>]`
  面向没有 subagent 的宿主：一条命令直接调用两个模型（ANTHROPIC_API_KEY、OPENAI_API_KEY）并循环 next/submit 直到门限；响应在输出上限处被截断时会报告为截断，此时调高 --max-tokens（两个提供方默认均为 16384；OpenAI 会把推理 token 计入其中）；每次 api 调用按其计价的最坏情况预留（有上限时，无价格模型按每 voice 默认值预留）；已发出但未绑定结果的 native 调用按其实际用量结算，用量未知时按全额预留结算；失败的外部调用保持按其预留额度入账。
- `gstack-autoplan next --out <dir> [--redispatch <attempt>]`
  后续调用：开启下一阶段，或重印未决尝试；绝不自行重新派发。
- `gstack-autoplan submit --out <dir> --phase <p> --voice native|outside --record <file.md> --model <id> [--attempt <id>]`
  绑定一份自由格式的评审记录（规范围栏、一个发现表格或列表，或 `No findings.`）。
- `gstack-autoplan submit ... --record <file.md> --attest "<reason>" --attempt <id>`
  把没有 INPUT: 行的记录作为收据绑定：视为已证（INPUT: 错误时一律拒绝）。
- `gstack-autoplan submit --out <dir> --phase <p> --voice native|outside --result <file> --model <id> --attempt <id> [--usage-usd <n>] [--reconcile <jsonl>]`
  绑定一份规范结果（见下方 RESULT FORMAT）；`--usage-usd` 按评审人的实际成本结算该尝试（否则保持按预留额度的 unknown 计价）；在关闭阶段的那个 submit 上，`--reconcile` 接受你自己对两个 voice 都提出的发现所做的配对，每对一行 `{"outside_id","native_id","disposition","resolution"}`，用以替代结构性配对。
- `gstack-autoplan submit --out <dir> --phase <p> --voice outside --unavailable|--failed "<reason>"`
  当没有任何外部 voice 可运行时，以仅 native 关闭该阶段。
- `gstack-autoplan answer --out <dir> --gate-rev <n> --reply "<reply>" --by human|agent:<id> [--owner-reply <text>|-] [--words-by agent:<id>] [--rec-hash <h>]`
  按下方的回复语法回答门限；agent 作答会逐字保存所有者的话，且当这些话是其本人所写时传 --words-by agent:<id>（默认按所有者处理）。
- `gstack-autoplan recommend --out <dir> --gate-rev <n> --item <id> --option <k> --basis "<why>"`
  在转发前修改一条建议；然后重新渲染并再次转发（`rec` 需要新的 `--rec-hash`）。
- `gstack-autoplan revise --out <dir> --plan <plan v2> --incorporates <decision ids>`
  绑定修订后的计划；重开每个被评审计划发生变化的阶段，Eng 最后。
- `gstack-autoplan revise --out <dir> --settle <decision id|d4> | --withdraw <decision id>`
  --settle 为打包或顺序变更做结算而无需编辑计划，且不重开任何阶段；--withdraw 撤回一项待处理修订而不是应用它。
- `gstack-autoplan close --out <dir> --phase <p> --deferred "<reason>" --by human|agent:<id>`
  以"接受但有发现"关闭一个阶段：其未决发现进入 tasks.jsonl，而 Critical、紧急或 user-challenge 发现成为门限条目；这也是从 `STOP: reason=budget_exhausted` 恢复的方式。
- `gstack-autoplan budget --out <dir> [--spend-cap <usd>] [--max-rounds <n>] --by human|agent:<id>`
  所有者记入日志的上限提升；预算停止后，`resume` 继续该运行。
- `gstack-autoplan export --out <dir>`
  写出工件集；然后运行 `gstack-artifact validate <dir>/run.json`。
- `gstack-autoplan export --out <dir> --public <pub>`
  一份无机器路径的副本，用于提交或分享（重写记录的根路径、保留 plan.md 代码、附来源摘要），且不含所有者本人的话（运行记录的每条 owner_reply、沿用的话、以及人工的延后原因都被丢弃，相关引述及 gstack 对它们的呈现被涂黑；若有一条位于 plan.md 代码中则拒绝导出）；私有运行不受影响；然后在本机运行 `gstack-artifact validate --public <pub> --private <dir>/run.json`。
- `gstack-autoplan status|resume --out <dir>`
  读取清单（PENDING: 行列出未决尝试）；崩溃后接管所有权（EXECUTION_UNKNOWN 列出未完成的尝试）。
- `gstack-autoplan resume --out <new dir> --from <checkpoint>`
  把最新的有效检查点世代（GSTACK_AUTOPLAN_CHECKPOINT_DIR）恢复到空目录并接管所有权；`checkpoints --from <dir>` 列出各世代。

## 评审人结果格式

每个提示词都以这份契约结尾；`submit --result` 强制执行它，`submit --record` 接受上文较宽松的形态。

RESULT FORMAT（gstack-autoplan 必需；父代理按此契约绑定你的文件）：
1. 结果的第一行必须恰好是：INPUT: <phase> <snapshot sha256>
2. 以散文写出完整评审，然后以一个规范围栏块收尾，内含规范化发现，每行一个 JSON 对象：
```gstack-findings
{"id":"F1","severity":"High","title":"<one line>","file":"<path or omit>","line":12,"fix":"<the fix>"}
```
   severity 为 Critical | High | Medium | Low | Informational. 仅当你建议改变计划所述方向且该变更会改动其范围、成本或方向时，才加 "user_challenge": true（此时另加 "changes": "scope" | "cost" | "direction"）；或当它只改动交付打包或顺序、不编辑 Implementation plan 时（此时 "changes": "packaging" | "ordering"）。命名及其他可逆选择是普通发现，不是 user challenge。对不属于本计划负责的安全或数据丢失发现，加 "urgent": true 和 "suggested_owner": "<who>"。空围栏表示无发现；缺失围栏会被拒绝。
3. 把整个结果写入此文件：<result file>

## 门限回复

回复绑定到你读到的那个 `gate_rev`（`--gate-rev`）。裸 `yes`/`no` 不做解析，绝不猜测。

- `rec`：每一项都采纳其建议，包括计划变更（每条打印 APPLY:）；`all` 与 `do it` 是别名。
- `as-is`：保留每个方向；不改计划。
- `d3b uc1a`：你设定的每一项各一个 <id><option> token；未应答的 auto 项取其默认值（finding 项保持计划原文；`p1b` 应用它）。
- `rec except d3b`：按建议执行，但以所列覆盖项为准。

## 运行目录

Runner 状态：`run.json`、`attempts.jsonl`、`run.lock`、`spend.json`、`plan-active.md`、`restore.md`、`plan-source.md`。评审人文件：`<phase>-native-prompt.md`、
`<phase>-outside-prompt.md`、`<phase>-<voice>.<attempt>.md`（由评审人写入）、其封存副本
`<phase>-<voice>.<attempt>.bound.md`（submit 所绑定的内容）、`<phase>-consensus.{json,md}`、
`gate.json`、`decisions.jsonl`。`export` 写出 `plan.md`、`review-record.md`、`findings.jsonl`、
`tasks.jsonl`、`timing.json` 并重算 `run.json` 的哈希；`gstack-artifact validate <dir>/run.json`
是完成检查。复制整个目录，绝不只复制单个文件。

## 结果码

- `RUN_NOT_INITIALIZED`：从 `gstack-autoplan next --plan <file> --out <dir>` 开始（首次调用即初始化运行）
- `PLAN_SECTIONS_INVALID`：补上缺失的标题，或带 --scaffold 重跑第一次 `gstack-autoplan next` 以评审一份脚手架副本（你的计划文件绝不会被编辑）；重复、颠倒或空缺的小节需手工修复
- `RUN_LOCKED`：等待其退出，或在其 pid 已消失时运行 `gstack-autoplan resume --out <dir>` 接管所有权
- `EXECUTION_UNKNOWN`：若评审人已完成，提交结果文件（`gstack-autoplan submit ... --attempt <id>`），或用 `gstack-autoplan next --redispatch <id>` 显式重新派发；任何东西都不会被自动重新派发
- `SPEND_CAP_EXCEEDED`：调高 `--spend-cap`、结算或释放未结算的尝试，或停止；未知花费按其预留额度计
- `PHASE_NOT_AWAITING`：运行 `gstack-autoplan status --out <dir>`，并针对 `next` 打印的那个尝试提交
- `ATTEMPT_MISMATCH`：传入 `next` 为该 voice 打印的尝试 id；一个结果只绑定一次
- `RESULT_RECEIPT_MISSING`：评审人必须把提示词文件读到 EOF，并以提示词所指明的 INPUT 行开始其结果；针对其他快照的结果会被拒绝
- `RESULT_FINDINGS_MISSING`：以一个 ```gstack-findings 围栏结束评审，每行一个 JSON 对象，至少含 severity 和 title；`[]` 行不算发现，空围栏表示无发现
- `MODEL_FAMILY_CONFLICT`：传入不同模型族的 `--model <id>`（anthropic、openai、google、xai、deepseek、qwen、zai、moonshot、meta、mistral）；同族结果不算外部 voice
- `CONSENSUS_MISSING`：恢复运行，使该阶段通过调和关闭；在每个先前阶段摘要齐备之前，绝不发送 Eng 提示词
- `GATE_REV_STALE`：渲染当前门限列表，读取它，并以其 gate_rev 作答
- `GATE_REPLY_UNPARSED`：用 `rec`、`as-is`、`<id><option>` token（例如 `d3b uc1a`）或 `rec except <tokens>` 作答；裸 yes/no 有歧义
- `GATE_REC_STALE`：重新渲染门限（`gstack-gate render <dir>/gate.json --all`）、转发它，并以打印出的 `--rec-hash` 作答
- `OWNER_REPLY_REQUIRED`：用 `--owner-reply "<text>"`、`--owner-reply -`（stdin）或 `--owner-reply-file <path>` 原样传入所有者的话
- `GATE_OWNER_REPLY_MISMATCH`：原样转发所有者所选择的内容（或其回复本身，如 `--reply rec`）；当所有者的话与 token 不一致时，询问所有者
- `PLAN_AMEND_PENDING`：编辑计划，然后 `gstack-autoplan revise --out <dir> --plan <file> --incorporates <decision id,...>`；打包或顺序变更用 `gstack-autoplan revise --out <dir> --settle <id>` 结算；或用 `gstack-autoplan revise --out <dir> --withdraw <decision id>` 撤回
- `AMENDMENT_NOT_SETTLEABLE`：编辑计划，然后 `gstack-autoplan revise --out <dir> --plan <file> --incorporates <decision id>`（在同一调用中加 `--settle <id>` 以结算打包/顺序变更）；仅当运行已评审该计划时才可单独 settle
- `CHECKPOINT_INVALID`：运行 `gstack-autoplan checkpoints --from <dir>` 查看每个世代的哈希状态，并恢复一个完好的世代；--out 未写入任何内容
- `GSTACK_VERSION_CHANGED`：较旧的运行无需处理（已执行记入日志的前向迁移）；由更新版 gstack 写出的运行需要那个 gstack：用 bin/gstack-upgrade 升级

## 协调者契约（由每条 lane 继承）

合并条件。一条 lane 的 PR 仅在以下条件同时满足时合并：所需的门限 lane 在盖章树上为绿，或树收据显示 `gate-reuse: eligible`；`gstack-lane-check` 就其计划内文件对照所有其他开放 lane 报告 `clear`；PR 正文在其 Agent notes 小节携带 `gstack-ship-receipt` 块；且由协调者（而不是 lane）宣布合并。lane 绝不自行合并、rebase 另一条 lane，或 force-push。

行为变更通知。评审开始之前，计划自身条目之外的每一处用户可见行为变更都要在 PR 正文的 `## Behavior changes` 下列出，含文件、旧行为与新行为。评审中发现的遗漏变更即 CRITICAL 发现，无论其大小。

花费上限。每条 lane 在协调者指定的 `--spend-cap` 下运行；触及上限的 lane 以 `incomplete` 停止（`STOP: reason=budget_exhausted`），并报告已花费、已预留与未知花费。付费 eval 绝不为了改变结论而重跑；重跑需要指明修复项。宿主 subagent 的花费报告为 `unknown`，绝不报告为零。

完成之前。lane 在每步之后向其分支推送一个 WIP commit，并对已推送的 SHA 做门限检查。只有当 `gstack-pregate run --allow-repo-commands` 通过时才算完成；`requires-remote` 需要 `--stage tests --remote --spend-cap <cap>`。当 `.gstack/pregate.json` 含有 `sealed` 键时，在任何推送或创建 PR 之前先运行 `gstack-pregate sealed`；拒绝即中止推送。

交接格式。lane 按此顺序报告，标识符在前：PR URL（或带分支与 SHA 的 `no PR`）、`GSTACK_RESULT` 行、`gstack: ok|fail <rev>` 行、`PREGATE:` 行、门限摘要（lane 通过/失败/跳过）、行为变更（或 `none`）、花费（已花费/已预留/未知），最后是无法验证的内容。每条跨线程消息都使用完整线程 id（`jam_…`），绝不用短码。标识符之后的散文可截断；其之前的任何内容都不可截断。

决策轨迹。lane 通过 `gstack-decision-trail <file> <phase> <decision> <why> <evidence> <result>` 维护 `<run dir>/decisions.tsv`（每个 fork、单测、回退或阻塞各一行；evidence 为可解析的指针）；当该文件先由另一次运行写出时，用 `gstack-decision-trail start <file> <run id>` 接手。完成之前，它对照会话记录审计该轨迹，用新行取代错误行而不是编辑原行，让另一模型族的一名评审人读取该轨迹，并以 `Attention` 小节结束其报告（`reviewed by <model>`，然后是标记项，或 `No flags`）。完整规则见 [docs/unattended.md](../docs/unattended.md#the-decision-trail)。
