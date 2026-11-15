> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/HUNTING.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 漏洞狩猎

### Phase 2: 运行以覆盖为导向的狩猎波次

父代理把 `planned` 状态的台账单元分配给 `general` 子代理。安排足够多的专注猎手覆盖这些单元，不要把不相关的边界合并进同一单元。一个猎手可以负责同一子系统中紧密相关的多个单元；任何单元都不得因子代理数量上限而被静默搁置，预算够不到的单元必须显式标记为 `deferred`，理由为 `budget_cannot_reserve_critics_and_validation`。

当预算或 profile 限制猎手数量时，按优先级顺序分配单元，并在台账中记录排序理由。排序依据：(1) 未认证或信任级别最低的入口面优先于已认证入口面；(2) 保护最有价值资源（凭证、跨租户数据、代码执行、发布权限）的边界；(3) 既往运行的缺口、待复验目标与已变更的源码，优先于同源码的重复扫描；(4) 其攻击类别在该目标类型上历史上产出过 `confirmed` 发现的单元，优先于偏推测的单元。平局时按 `coverage_id` 字典序打破，保证运行可确定。

启动前，父代理把已分配单元改为 `in_progress`，设定规范的小写 `agent_id`，并创建该代理的 `scratch/` 目录与父代理持有的 `artifacts/` 目录。猎手阅读源码与父代理提供的上下文，只写入自己专属的 `scratch/`，并通过 Task 工具返回一个结构化结果。它们绝不写入保留产物，也绝不修改目标源码、`architecture.md`、`coverage-ledger.json`、`findings.json` 或其他代理的文件。

## 必需的猎手提示词

每份猎手提示词按此顺序包含以下部分：

1. 两句话的角色开场：猎手的目标是在其被分配的单元中找到有源码依据的安全不变量失效，且必须返回恰好一个 JSON 对象，符合本提示词末尾的结构化结果契约。
2. `architecture.md` 原文照录。
3. 已分配的 coverage ID、子系统、边界、仓库相对起始路径，以及来自 `coverage-ledger.json` 的每个单元的 assignment 块映射。
4. 精确选中的块，逐字复制：来自 `ATTACK-CLASSES.md` 的每个选中的普通攻击类块，以及每个选中的伴生块的 `Core discipline`、所选攻击类小节、`Universal moves` 和 `Validation rules`。普通块自成一体，不带伴生块式的 `Core discipline`、`Universal moves` 或 `Validation rules` 小节。不要只发送块名或伴生块名。
5. 明确列出的被排除普通块与伴生块，每项排除附理由。
6. 下方的核心狩猎方法，随后是提升流程块。
7. 下方的核心验证规则。
8. 携带的同源既往已确认排除项，每项仅限指纹、标题与根因，以及本猎手不得重复的其他代理名下的当前 coverage ID。
9. 专属的 scratch/产物路径、安全代理 ID、预声明的提升允许清单与字节上限，以及结构化结果契约，包括下方的"结构化猎手结果"块，以及逐字复制的 `report-schema.json` 的 `confirmed` 与 `needs_validation` 分支。

同一条路径跨越多个领域时，提示词可以选择多个伴生块。要把它们的约束放在一起传达。范围是猎手的覆盖义务，不是重复已排除工作的许可。出现意外的不同边界时，把它放进 `uncovered` 返回，由父代理创建稳定的台账单元并在下一波次分配。

#### 核心狩猎方法（放进每份猎手提示词）

```text
## Defensive vulnerability-finding method

Your goal is to find source-grounded security invariant failures and the smallest fix,
not to expand harm beyond the boundary result. Stay within source review and bounded local execution.
Do not contact deployed endpoints, provider APIs, registries, identity systems,
message brokers, shared services, or other users. Use local dummy data only.

READ THE CODE AT DEPTH. Follow each assigned input through parsing, identity,
authorization, normalization, state, derived copies, and the final sink. Read sibling,
legacy, batch, retry, cancellation, migration, and error paths that produce the same
effect. Compare sibling controls for equivalence, not only presence, and compare what
one component guarantees with what the next component assumes.

WORK FROM A CONCRETE INVARIANT:
1. Name the lower-trust principal and starting capability.
2. Name the accepted value, action, state transition, or resource selector.
3. Locate the control that should reject, bind, isolate, limit, or revoke it.
4. Trace the exact source path after that decision.
5. Stop at the smallest affected dummy record, wrong return value, process-integrity
   effect, or locally observable shared-resource effect.
6. State a source-level change and regression case that enforce the invariant.

DEPTH BOUND: trace only paths that can reach your assigned boundary or whose
guarantees that boundary relies on. Stop a line of investigation as soon as the
invariant is settled either way, and record the result in your structured output —
a covered, candidate, or blocked disposition, or an `uncovered` entry — instead of
continuing to search.

TEST SAD PATHS AND DISAGREEMENTS. Check absent, empty, zero, negative, maximum,
over-limit, duplicate, mixed encoding, stale, revoked, reordered, concurrent,
partially migrated, failed dependency, and rollback state only where the interface
accepts them. Compare canonicalization and units at every parser or policy handoff.
For multi-step issues, treat each output as a prerequisite and do not assume a later
boundary. If any prerequisite is not established, record a blocker.

When a proposed high or critical candidate reveals a reusable root cause, search paths
owned by the assigned coverage IDs for lexical, structural, and logical variants.
Consolidate the same root cause, but establish each variant's conditions and impact
independently. Do not investigate peer-owned units. Return a variant with no current
coverage unit as `uncovered`.

USE THE NARROWEST LOCAL CHECK THAT SETTLES THE CLAIM. Target-controlled builds,
tests, processes, browsers, emulators, fuzzers, and fixture processing may run only
inside the parent-approved OS-enforced sandbox. It must disable external networking,
start from an empty allowlisted environment, expose target and tools read-only, permit
writes only to your scratch directory, and apply low CPU, memory, process, file-size,
disk, and wall-clock limits. Isolated loopback is allowed only for a local fixture.
If any control is unavailable, do not execute: return needs_validation with that exact
blocker. Prefer an existing unit test, minimal function harness, dummy-tenant service
call, small malformed fixture, deterministic race schedule, or locally rendered policy.
Do not install or fetch tools.

Record the exact input, command, limits, and minimum result. For the environment,
record only allowlisted variable names and safe non-secret values needed to reproduce
the check. Never capture the ambient environment, inherited variables, credentials,
authentication state, or unrelated host paths. The target-controlled process writes
only in scratch. After the sandbox and all its processes terminate, only trusted
parent-side code may promote predeclared scratch-relative files, following the
promotion procedure block included verbatim in this prompt. You and target code never
write retained artifacts. If promotion is unavailable or fails for decisive evidence,
return needs_validation with the exact promotion blocker.
Never stress availability, invoke a live target, use a real credential, publish an
artifact, or continue past the minimum observed effect.

A deployment, browser, provider, broker, OS, proxy, package, secret, or identity fact
outside source is not proof either way. If one such fact is decisive, return a
needs_validation record with the exact missing observation and safe owner-observed check.
```

#### 提升流程（把本提升流程逐字复制进每份猎手提示词）

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

#### 核心验证规则（放进每份猎手提示词）

```text
## Candidate gate

1. A candidate needs a complete repository-relative source trace and evidence for the
   claimed root cause, including the strongest source-visible control.
2. A proposed confirmed record needs a bounded local observed result, meaningful impact
   across a stated boundary, complete conditions, and no visible preventing layer.
3. Do not strengthen a crash into code execution, ordinary work into shared availability,
   or a same-principal action into privilege gain.
4. If a required fact is not source-visible or locally observable, use
   needs_validation. Name exact blockers; do not give it severity or speculative completion.
5. A missing best practice with no affected principal/resource is excluded or hardening,
   not a finding. A candidate disproved by source is not needs_validation.
6. Use the same source-derived fingerprint for the same root cause in every state.
   It must match `^[A-Za-z0-9][A-Za-z0-9._:/@+-]*$` and must not include a line,
   wave, agent, severity, or verdict.
7. Return an empty candidate array when nothing survives these gates.
```

## 本地验证边界

本地执行用于确认，不用于扩大影响面：

- **仅限在必需的 OS 沙箱内进行：** 使用现有依赖的离线构建；使用假数据的隔离环回进程；单元与集成测试；小型 fixture 处理；sanitizer；有界 fuzz/回归测试；确定性并发检查；使用假账户的本地浏览器/模拟器测试；使用假身份的清单渲染与策略求值；mock 的外部或付费调用。
- **禁止：** 真实或已部署流量；向未为本隔离检查启动的服务发请求；联网安装依赖；真实账户或凭证；生产数据；共享队列、云资源、runner、镜像仓库、签名或发布服务；对外发布；压力、饱和或成本制造；在得到最小假数据边界结果之后的任何后续工作。

沙箱以空环境启动，不给目标代码任何外部网络或宿主机可写路径，并为每次检查强制施加明确偏低的资源与时间限制，而不只对预期昂贵的检查。退出后，scratch 输出仍受目标代码控制。只能用 `SKILL.md` 中那个 no-follow、路径受限、仅普通文件、有界大小的宿主机流程来提升它。缺少任何沙箱或提升能力都不会抹掉有源码依据的候选；把确切的阻塞项写进 `needs_validation`。

## 结构化猎手结果

返回恰好一个 JSON 对象，除它以外不带任何文字：

```json
{
  "units": [
    {
      "coverage_id": "one assigned ID",
      "disposition": "covered|candidate|blocked",
      "reviewed_paths": ["repo/relative/path"],
      "checks": [
        {
          "agent_id": "canonical owner of this check",
          "reviewed_paths": ["repo/relative/path owned by this check"],
          "invariant": "specific control checked for this unit",
          "method": "source|local",
          "result": "what source or the bounded check established",
          "artifact": "agents/<agent-id>/artifacts/file for local, null for source"
        }
      ],
      "candidate_fingerprints": [],
      "unresolved": []
    }
  ],
  "candidates": [],
  "hardening": ["concrete non-finding note"],
  "uncovered": [
    {
      "surface": "...",
      "boundary": "...",
      "subsystem": "...",
      "attack_class": "...",
      "starting_paths": ["repo/relative/path"],
      "reason": "why this needs its own deterministic coverage unit"
    }
  ]
}
```

每个 `candidates` 条目都符合 schema 结构，只是用 `proposed_verdict` 代替 `verdict`：

- `proposed_verdict: "confirmed"`：包含 `report-schema.json` 的 `confirmed` 分支要求的除 `verdict` 外的每个字段：`fingerprint`、标题、描述、`root_cause`、`intended_behavior`、有序的 `trace`、`evidence`、`conditions`、目标中立的 `execution`、`remediation`、`severity` 与 `confidence`。execution 说明只描述已执行过的那次有界本地检查。`payloads` 保存最小测试输入、fixture 或原生调用。`observed_result` 记录实际本地输出。总体严重度不得超过观察到的 impact（影响）。
- `proposed_verdict: "needs_validation"`：包含该 schema 分支要求的除 `verdict` 外的每个字段：`fingerprint`、标题、描述、`claimed_root_cause`、有序的 `trace`、`evidence`、非空的 `blockers`，以及 `validation_plan`（至少包含一个适用的 `local` 或 `deployment` 步骤）。不要编造不适用的上下文。不要包含 severity、execution、remediation、reason 或已确认的 `root_cause`。`deployment` 是由资产所有者观察的检查，不是探测真实目标的请求。

每个已分配的 coverage ID 在 `units` 中恰好出现一次。`covered` 单元需要有归属者、非空的 `reviewed_paths` 与 `checks`、没有未决事实，且没有候选。`candidate` 单元拥有同样的归属证据，并且是唯一携带关联指纹的状态。`blocked` 单元是一次有归属的部分审查，有非空的 paths、checks 与未决事实，但没有指纹。所有源码路径都是仓库相对路径，绝不使用绝对路径或带目录遍历的路径。含多个条目的 trace 从 `entrypoint` 开始、到 `sink` 结束，中间步骤标为 `propagation`。每个 check 都有自己的规范小写 `agent_id` 和非空的 `reviewed_paths`；单元级列表恰好是这些归属路径的并集。`source` check 使用 `artifact: null`。`local` check 使用一个由父代理成功提升到 `agents/<check.agent_id>/artifacts/` 之下的普通文件；这允许验证者补充独立归属的证据，而不从猎手手中夺走归属。绝不链接 scratch、输出根目录下的文件或其他 check 归属者的产物。

## 父代理合并与台账更新

父代理验证每个单元结果，把它映射到恰好一个已分配的 `coverage_id`，并只更新那个台账单元。拒绝重复或缺席的 ID、不安全的单元或 check 代理 ID、带产物的 source check，以及未经可信父代理侧代码提升进 check 归属者 artifacts 子树的本地产物。把单元的 `reviewed_paths`、其 `checks`（写入单元的 `local_checks`）、关联产物路径、候选指纹和未决事实复制进台账。把每个猎手的 `hardening` 列表保留在相关单元的父代理记账字段中（语义字段之外），以便 Phase 6 汇报。失败、畸形或无依据的结论会让该单元保持 `planned`，等待重新分配。预算/profile 未触及的单元变为未分配的 `deferred` 单元，证据为空并附理由；不要把部分证据藏进 `deferred`。更新后运行 `validate-coverage-ledger.cjs`；无效的台账不能驱动下一次分配。这个按单元契约允许一个猎手关闭一个单元，同时为另一个单元返回候选或阻塞项。

先按指纹、再按根因合并候选条目。暴露多个入口路径或效果的同一条根因是一个候选，取最强的完整 trace。相关但相互独立的缺失控制使用不同指纹。把重复指纹记录在相关台账单元中，不要把重复候选送进验证。

## 覆盖评审者波次

每轮猎手波次结束后立即执行：把预留的一次调用用于一个全新的 `research` 波后覆盖评审者（coverage critic）。它接收 `architecture.md`、包含每个 assignment 块映射的完整覆盖台账、当前候选指纹与状态，以及既往台账的缺口摘要。它只读源码，不写入也不运行目标。要求它恰好返回这个 JSON：

```json
{
  "missing_units": [
    {
      "surface": "...",
      "boundary": "...",
      "subsystem": "...",
      "attack_class": "...",
      "starting_paths": ["repo/relative/path"],
      "selected_companion_blocks": ["FILE.md#section"],
      "excluded_blocks": [{"block": "FILE.md#section", "reason": "..."}],
      "reason": "source-backed coverage gap"
    }
  ],
  "reassign_ids": ["existing-id-that-did-not-close"],
  "resolved_prior_leads": ["fingerprint"],
  "stop": false
}
```

评审者检查未映射的入口点、未检查的并行路径、缺失的生命周期模式、选中了伴生类却没有对应单元、无理由的排除、关闭时没有 paths/checks 的单元，以及没有任何单元处理的既往 `needs_validation` 或已变更源码缺口。它提出的是覆盖建议，不是发现。`stop` 是评审者自己的判断：仅当它不接受任何 `missing_units` 也不接受任何 `reassign_ids` 时才为 `true`；是否再跑一波由下文的父代理循环条件决定，而不是只看 `stop`。对 `resolved_prior_leads` 中的每个指纹，父代理把关联单元或既往线索条目标记为已解决，并记录评审者给出的有源码依据的理由。

父代理拒绝超出审查范围或源码/本地边界的建议单元，为接受的单元推导规范 ID，并与当前单元去重。既往同源已完成单元可以提供证据；既往 `deferred`、`blocked`、`out_of_scope` 或已变更源码的单元变为当前工作，绝不压制已接受单元。出现规范 ID 冲突时宁可失败，也不要合并。对每个带活跃 `blocked`、`covered` 或 `candidate` 证据的合法 `reassign_id`，把该确切的终结记录连同评审者给出的有源码依据的 `reassignment_reason` 追加到单元的 `attempts`。把其归属者、checks、产物、指纹和未决事实保存在该归档中。递增活跃 `wave`；下一个猎手必须是新的归属者，并收到一个活跃证据为空的 `in_progress` 单元。猎手的终结结果只把其新证据写入活跃字段。绝不把归档归属者的 checks 或产物复制进新的活跃尝试。在下一次分配前对 ID 排序并验证台账。在 `standard` 与 `deep` 档位下，当波后评审者没有报告任何被接受的 `missing_units` 或合法 `reassign_ids`、也没有剩余 `planned` 单元时，把单独预留的那次调用用于一个独立的最终清洁评审者（final-clean critic）。只有该评审者也未返回被接受的工作时，覆盖才算完成。若它发现了工作，将其排队并重复"波次、波后评审、最终清洁"这一流程。若时间或资源迫使提前停止，把每个未触及单元标记为 `deferred`，保留评审者理由，并在报告中披露缺口。绝不把"静默的波次或代理数量上限"当作覆盖完整的证据。

运行 profile 限定这个循环。`quick` 运行恰好一轮猎手波次，随后恰好一次最终评审。把每个被接受的 `missing_unit` 加入当前台账，并标记为 `deferred`，理由为 `quick_profile_final_critic`。对每个带证据的合法 `reassign_id`，把活跃终结状态归档进 `attempts`，递增 `wave`，并把活跃状态设为未分配的 `deferred`，证据为空，理由为 `quick_profile_final_critic`。不再启动第二轮猎手波次或另一个评审者。在限定范围（scoped）的运行中，评审者仍会报告它注意到的范围外缺口，但父代理把它们连同评审者理由记录为 `out_of_scope`，而不分配。上文的提前停止规则是同一机制：`quick` 是预先声明的提前停止，不是覆盖完整的证据。

预算以同样方式限定这个循环。每轮波次分配前，把剩余预算与其猎手数量、验证预留、紧随其后的波后评审者以及保留的最终清洁评审者比较（`quick` 只预留其单个最终波后评审者）。压缩猎手波次以适配预算，按优先级顺序取单元。若这些强制预留放不下，该波次不启动任何猎手，并将其 planned 单元标记为 `deferred`，理由为 `budget_cannot_reserve_critics_and_validation`。评审者建议的单元进入同一个排序队列，而不是扩大预算。若存活候选超过验证预留，遵循 `SKILL.md` 中的不完整运行规则：停止狩猎，按指纹顺序验证，未验证单元保留为未决候选，绝不把它们当作 findings 呈现。
