> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/VALIDATION-AND-REPORTING.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 校验、结构化输出、验证与报告

### Phase 3: 独立校验每个候选

在干净的覆盖评审者（coverage-critic）环节或明确记录的提前停止之后，按稳定指纹与根因合并 Phase 2 候选和携带的同源先前确认。把每个去重后的 `confirmed` 与 `needs_validation` 候选交给一位没有参与猎取的全新 `general` 验证者。携带的先前确认走同样的当前验证路径，即使猎手把那个未变化的根因排除在外。验证者可以读猎手或先前的产物，但必须重读每一个被引用的当前源码位置，并能安全复现时独立运行任何决定性检查。

给每个验证者分配一个规范的小写唯一 ID，以及 `<output-dir>/agents/<verifier-id>/scratch/` 和 Parent 持有的 `artifacts/`。验证者只写 `scratch/`，绝不写保留产物。它只接收：该候选、与之关联的台账单元检查与产物路径、解读路径所需的架构事实、精确相关的配套校验块、下方的提升流程块、源码/本地执行边界、逐字复制的 `report-schema.json` 的 `confirmed`、`needs_validation` 与 `rejected` 分支，以及同指纹的先前记录。它不得收到另一个验证者的结论。

#### 候选-验证者提示词

```text
You did not write this candidate. Try to refute it from repository source and bounded
local evidence. Do not contact deployed endpoints or external/shared services. Run
target-controlled code only inside the approved OS-enforced sandbox: no external
network, empty allowlisted environment, read-only target and tools, scratch-only
writes, and explicit low resource and wall-clock limits. If any control is unavailable,
do not execute; retain the exact missing capability as a needs_validation blocker.
Treat every scratch entry as target-controlled after execution. After the sandbox and
all its processes terminate, only trusted parent-side code may promote a predeclared
scratch-relative file, following the promotion procedure block included verbatim in
this prompt. You and target code never write retained artifacts. If promotion is
unavailable or fails, do not use that file as evidence.

1. Verify every trace and evidence file, positive line number, scope, and description.
   Confirm the first entry is a real lower-trust entrypoint and the last is the
   claimed sink or boundary effect.
2. Reconstruct the strongest source-visible validation, identity, authorization,
   normalization, lifecycle, framework, and containment controls on the path.
   Where the architecture summary names a comparable baseline, note whether it
   shares the pattern — as calibration, never as grounds to dismiss.
3. For a proposed confirmed candidate, independently reproduce the minimum observed
   result when possible. Verify inputs, interface shape, conditions, and affected
   dummy principal/resource. Do not infer a stronger result or continue after it.
4. Verify that likelihood, impact, confidence, and the proposed source fix match only
   what the evidence establishes.
5. For a proposed needs_validation candidate, decide whether the blocker is genuinely
   outside source/local observation. If source refutes the trace, reject it. If the
   missing fact remains decisive, keep needs_validation and make the local and
   owner-observed plans exact and non-destructive.
6. Preserve the fingerprint for the same source-derived root cause across every state.

Return exactly one JSON object and no surrounding prose:
{"decision": "confirmed|needs_validation|rejected", "record": { ... }}
where record exactly matches the decision's verdict branch of the schema included
in this prompt. A corrected record replaces the hunter's wording.
```

把以下提升流程逐字复制进每个候选-验证者提示词：

```text
Artifact promotion procedure (trusted parent-side code only):
Reference only for you: the parent performs these steps; you never perform them.

Before execution, the parent opens and retains trusted, non-inheritable directory
descriptors for the agent's scratch/ and artifacts/ roots, and records an allowlist
of expected scratch-relative artifact files plus explicit per-file and cumulative
byte limits. Never pass those descriptors to the agent or sandbox. After the sandbox
and all its processes terminate, trusted parent-side code promotes each allowlisted
file separately:

1. Validate the declared relative path: reject absolute, empty, `.`, `..`, or
   symlinked components.
2. Walk each parent component from the retained scratch-root descriptor with
   no-follow directory-relative operations; never reopen by path.
3. Open the leaf no-follow and nonblocking.
4. Verify with `fstat` that it is a regular file with link count exactly one and
   within the recorded per-file and cumulative byte limits.
5. Enforce those limits again while reading from that descriptor.
6. Copy exactly the verified size, repeat `fstat`, and reject a changed identity,
   type, link count, or size.
7. For the destination, walk every parent component from the retained
   artifacts-root descriptor with no-follow directory-relative operations; require
   each existing component to be a real directory, and create any missing directory
   exclusively before reopening and verifying it no-follow.
8. Create the leaf exclusively without following links, verify that the opened
   destination is a regular file with link count exactly one, and copy from the
   verified source descriptor without reopening either path.
9. Use equivalent race-safe APIs on non-POSIX systems.
10. Never recursively copy or glob scratch, extract an archive into artifacts, or
    open or promote a symlink, FIFO, socket, device, directory, hard-linked file,
    changing file, or file that exceeds its bound.
11. If any check is unavailable, cannot be enforced, or fails, discard the scratch
    entry; if it is decisive evidence, retain `needs_validation` with the exact
    promotion blocker.
```

验证者只有在独立确立完整路径和有边界的观察结果之后，才能把 `needs_validation` 提升为 `confirmed`。当某个具体的部署或运行时事实仍然未知时，把拟议的确认降级为 `needs_validation`。当源码、本地行为、可见控制、缺少实质影响或不可满足的前置条件驳倒了断言时，使用 `rejected`。`needs_validation` 绝不是投机想法的停车场。

Parent 检查每个验证者返回的指纹是否一致，除非它识别出了真正不同的根因。合并修正，把决策记录进每个关联的台账单元，并确保每个指纹只有一条最终记录。格式错误或被散文包裹的验证者结果直接丢弃，不做修复；预算允许时用新验证者重跑该候选，否则它按不完整运行规则保留为未校验的台账候选。

当验证者证据更新台账检查时，把该检查的 `agent_id` 设为验证者的规范 ID，并列出其非空的仓库相对 `reviewed_paths`。单元级 `reviewed_paths` 保持为各检查的并集。纯源码审查用 `method: "source"` 且 `artifact: null`。`method: "local"` 只用于由可信父端代码成功提升到 `agents/<check.agent_id>/artifacts/` 之下的文件。单元保留其原始分配所有者，因此独立所有的猎手检查与验证者检查可以共存。携带先前记录所播种的 `planned` 单元没有先前所有者：复查它的验证者成为该单元的分配所有者，其复查就是该单元的第一次检查，并把单元带着携带的指纹移入 `candidate`。

如果严格的总 Agent 预算覆盖不了每个候选，把运行状态设为 incomplete，并遵循 `SKILL.md` 中的确定性预算规则。未校验的候选只保留在台账里，不以任何判定进入 `findings.json`。

### Phase 4: 写入并校验 `findings.json`

Parent 把所有独立裁决的记录写入 `<output-dir>/findings.json`，按指纹排序。包括：

- `confirmed`：以源码为据的漏洞，带有完整的本地执行证据、条件、具体修复方案、可能性/影响/总体严重程度，以及置信度。
- `needs_validation`：以源码为据的候选，带有精确的未解决阻塞项，以及至少一个适用的本地或所有者观察式部署计划。
- `rejected`：在校验中被驳倒的以源码为据的候选；保留它们，是为了让未来运行在没有新证据时不重复这条不成立的断言。

写入之前立即读一遍 `report-schema.json`。它使用 `additionalProperties: false`；不要把猎手的包装字段带进记录。保持这些判定契约互不混用：

- `confirmed` 记录使用 `root_cause`、`intended_behavior`、`conditions`、`execution`、`remediation`、`severity` 和 `confidence`。不得使用 `claimed_root_cause`、`blockers`、`validation_plan` 或 `reason`。`execution` 与目标无关，使用目标的原生接口：API/HTTP 输入、CLI 调用、库调用、消息、文件 fixture、浏览器操作、渲染出的策略，或适用的本地 harness。`observed_result` 非空且符合事实。
- `needs_validation` 记录使用 `claimed_root_cause`、`trace`、`evidence`、`blockers`，以及至少一个非空的 `validation_plan.local` 或 `validation_plan.deployment` 字段。只有当两种上下文能分别解决不同的事实时才同时包含两者。不得使用严重程度、execution、修复方案、reason 或确认的根因。
- `rejected` 记录使用 `claimed_root_cause`、`trace`、`evidence` 和 `reason`。不得使用严重程度、execution、修复方案、blockers、验证计划或确认的根因。

每条记录都有稳定指纹、标题、描述和仓库相对源码路径。多步 trace 以 `entrypoint` 开始、以 `sink` 结束，`propagation` 只用于两者之间。单步 trace 只用 `entrypoint` 或 `sink`。总体严重程度不得超过已论证的影响。

运行：

```sh
node <skill-dir>/validate-findings.cjs <output-dir>/findings.json
node <skill-dir>/validate-coverage-ledger.cjs <output-dir>/coverage-ledger.json
```

继续之前修掉所有结构与语义错误。findings 校验器拒绝超过 5 MiB、1,000 条顶层发现或 64 层嵌套的输入，并把报告的错误输出截在 100 条。校验器通过只证明格式与台账一致性。

### Phase 5: 用新的眼光验证最终记录

为每条最终 `confirmed` 与 `needs_validation` 记录并行启动一个全新的 `research` 验证者。该验证者检查的是结构化记录，不是猎手的文字稿，并且留在源码/本地边界之内。

在 `quick` 运行中，Phase 3 与 Phase 5 合并：Phase 3 验证者同时执行这些记录检查并返回最终 schema 形状的记录，每个候选得到一个全新的独立复核者而不是两个。其他所有档位保持两个环节分离。任何档位都绝不跳过对 `confirmed` 记录的独立复核。

对 `confirmed`，要求它检查：

1. 每个仓库相对的 trace/证据路径、行号、范围和所描述的操作。
2. 真实的入口接口和精确的本地输入形状。
3. 每个条件、解析器/策略步骤、源码可见的阻断层，以及观察到的本地结果。
4. 受影响的主体/资源，以及已论证的影响。
5. 严重程度的区分：现实的可能性、已论证的影响，总体不超过影响。
6. 修复策略和任何 `code_changes`，包括修复是否真正强化了不变量，而不是仅仅移动了信任位置。

对 `needs_validation`，要求它检查：

1. 源码路径真实存在，且只支持所陈述的 `claimed_root_cause`。
2. 列出的每个阻塞项都是决定性的，且并非本地已经可以回答。
3. 候选指出了一个边界和一个可能的具体结果，而不是泛泛的担忧。
4. 至少一个验证计划字段存在且精确。`local` 使用有边界的 fixture；`deployment` 请所有者观察某项配置、身份、路由、策略或运行时事实。不要为不适用的上下文编造计划，绝不向部署环境发送审计流量。
5. 指纹与同一根因的先前/当前记录匹配。

每个验证者只返回一个 JSON 对象：`{"decision":"verified","fingerprint":"..."}` 或 `{"decision":"replace","reason":"...","record":{...}}`，不带任何外层散文。替换记录必须符合其 `confirmed`、`needs_validation` 或 `rejected` schema 分支。Phase 5 结果若格式错误或被散文包裹，按 Phase 3 的方式处理：直接丢弃不做修复，预算允许时用新验证者重跑。

当 Phase 5 的替换把记录提升到更强的判定（包括任何对 `confirmed` 的提升），或实质性改变根因、trace、execution 输入或观察结果、已论证影响或严重程度时，不要将其直接作为最终结果。把这份完整替换交给一个新的独立验证者，它没有猎取过、没有做过 Phase 3 校验、也没有提出过这份 Phase 5 替换。新验证者在执行边界内复查当前源码，并独立复现任何决定性的本地结果，然后返回 `verified` 或又一份替换。实质性替换只有在这轮全新验证之后才可采纳。如果又出现实质性替换，用新验证者重复此流程。如果预算或独立性不可得，把有争议的记录从 `findings.json` 移除，其台账单元保留为未解决候选，并把 `run_status: "incomplete"` 连同精确的 `incomplete_reason` 一起设置。非实质性的措辞或仓库行号修正，只要不改变含义或证据，可以直接采纳。

每采纳一次替换之后，重跑两个校验器并更新关联台账的决策。如果最终验证者识别出另一个独立根因，为其分配新指纹，并在纳入之前送独立候选校验。只有当每个台账候选都有独立最终处置、且每条保留记录都通过 Phase 5 时，才设置 `run_status: "complete"`。

不要只验证 `confirmed` 记录。误导性的 `needs_validation` 交接浪费所有者时间，还可能保住一个错误前提。

### Phase 6: 从最终记录产出与目标无关的报告

只有当 `findings.json` 中保留的每条记录都通过 Phase 5 之后，才从最终记录、台账和台账簿记中保留的猎手 `hardening` 笔记派生散文内容。不完整的运行可以报告已独立验证的记录，但必须点出每个未解决的台账候选，且不得把它当作发现呈现。散文文件绝不改变判定、严重程度、阻塞项或已论证影响。

#### `REPORT.md`

写入：

1. 运行档位、范围、预算（如设定）及已用与计划的 Agent 数、源码 ref、沙箱化的仅源码加本地执行声明、对先前运行的使用，以及明确的推迟与范围外覆盖。写明携带的同源确认与变源重验。`quick`、限定范围、预算受限或不完整的运行要直说这是部分通过。如果候选校验耗尽了严格预算，要说明运行不完整，并列出每个未校验的指纹及关联单元；不要把这些候选描述为发现。如果预算导致某个强制性评审环节没有运行，要说明是哪个评审者未运行，且不得声称覆盖干净。
2. 一段简短的安全态势总结。
3. 一张已确认发现表：严重程度、标题、受影响边界，以及一行式的观察结果。
4. 每条已确认发现：仓库源码位置、低信任主体、与目标无关的有边界复现、条件、实际结果、影响、优先级依据，以及最小的源码修复。
5. 一张单独的 `NEEDS VALIDATION` 表。给出每条线索的标题、仓库 trace、精确阻塞项、有边界的本地下一步，以及安全的所有者观察式部署检查。不要赋严重程度，也不要称其为已确认漏洞。
6. 单列的加固说明与正面源码模式。
7. 来自台账的覆盖总结：covered、candidate、blocked 与 deferred 的数量，加上重要排除项和最终评审者结果。

不要把 rejected 记录描述为发现。只有当它们解释了先前的分歧或覆盖决策时，才提及它们的指纹。

#### `FINDINGS-DETAIL.md`

对每条已确认的 `medium`、`high` 或 `critical` 记录，复制完整的源码路径和与目标无关的本地复现：

- 按序排列的仓库相对 trace 与证据；
- 虚拟攻击者/主体与受影响的虚拟资源；
- 原生输入、调用或 fixture，以及精确的有边界操作说明；
- 观察到的输出及其证明的安全不变量；
- 条件与遏制手段；
- 源码级修复方案与回归用例。

#### `NEEDS-VALIDATION.md`

对每条未解决记录，复制源码 trace、已验证证据、精确阻塞项、受影响边界，以及每个适用的有边界本地或所有者观察式解决计划。把它们保持为不带严重程度的优先级线索。不要把它们变成实际测试指引，也不要假设那个缺失的部署事实。

HTTP 只是一种可能的原生接口，不是默认。库发现可以用函数调用，解析器用 fixture，CLI 用命令，桌面应用用 IPC 或文件操作，基础设施用本地渲染的策略。不要要求目标不具备的端点、外部账号或真实环境。

报告要与证据成比例。干净的运行可能零条已确认记录。如实陈述该结果和剩余的覆盖/校验限制，不要凭空造出 LOW 发现。
