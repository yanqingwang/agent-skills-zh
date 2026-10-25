---
name: vibe
description: Vibe Code Orchestrator（VCO）是一个受治理的运行时入口，用于冻结需求、约束执行边界，并强制执行验证与阶段清理。
---

> **中文汉化版** · 上游：[foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) · 原文件：`SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Vibe 受治理运行时入口

本文件是面向宿主的、进入规范 `vibe` 的标准操作流程（SOP）。保持精简：运行时细节属于 `protocols/runtime.md`，执行纪律属于 `protocols/do.md`，宿主 wrapper 配方属于安装器生成的 wrapper 文档。

## 触发契约

当用户显式调用 `$vibe`、`/vibe` 或 `vibe` Skill 时，或当宿主针对复杂任务有意选择受治理的需求/计划/执行闭环时，应在普通执行之前进入规范 `vibe`。

不要把所有松散相关的任务都路由进 `vibe`。轻量级提问、
单命令检查，或更适合由另一个被显式请求的 Skill 处理的任务，
可以在 `vibe` 之外进行，除非用户显式调用了本入口。

已安装副本的更新在同一受管目录上使用 `update --skills-dir <skills-dir>`。

用户指令，包括 CLAUDE.md、GEMINI.md、AGENTS.md 以及 TDD 例外等直接工作流限制，始终保持最高优先级。在这些限制内保留规范的启动与证明规则。

## 规范引导（Canonical Bootstrap）

`vibe` 是一份与宿主语法无关的 Skill 契约。在规范启动之前，只做启动所需的最少工作：

- 解析 `skill_root` 与 `workspace_root`。
- 将当前用户任务逐字作为任务规格传入；不相关的聊天历史可以排除。不要总结、改写或将其简化为关键词。保留确切的输入路径、输入不可变性约束、确切的输出根目录、合成数据证据边界、模块依赖与安全并行边界，以及验收标准。

启动前不要在当前工作区、仓库或安装根目录中搜索规范证明文件。
在规范启动返回之前，不要检查仓库、协议文档或先前运行输出。
不要模拟各阶段，不要凭阅读本文件或 wrapper 文本就宣称已进入规范入口，也不要把 wrapper 或 AGENTS 文本当作证明。
不要手动创建 `outputs/runtime/vibe-sessions/<run-id>/`。
不要把 Vibe 安装根目录当作受治理的产物根目录。

本地 Skill 候选审计：语义所有者为 `packages/runtime-core/src/vgo_runtime/router_contract_runtime.py`；兼容桥接为 `scripts/router/resolve-pack-route.ps1`

该审计在规范 `vibe` 内部运行，并暴露候选供检查。续接时需包含工作类型、领域/技术、交付物、显式约束以及已验证的冻结事实。其输出仅作为兼容性证据；Skill 选择、绑定与阶段推进由 Agent 负责。

规范入口命令形态：

```powershell
$env:PYTHONPATH = "<skill_root>/apps/vgo-cli/src"
py -3 -m vgo_cli.main canonical-entry --repo-root "<skill_root>" --artifact-root "<workspace_root>" --prompt "<current user task, verbatim>"
```

对于 PowerShell，不要把 `$env:PYTHONPATH=...` 放在双引号包裹的 `-Command` 字符串内；宿主插值可能将其破坏为 `:PYTHONPATH`。

类 Bash 宿主（包括 Claude Code）在外层 shell 设置 `PYTHONPATH` 并直接调用 Python。按可用性依次尝试 `py -3`、`python`、`python3`。

```bash
REPO_ROOT='<skill_root>'
WORKSPACE_ROOT="${WORKSPACE_ROOT:-$PWD}"
PYTHONPATH="$REPO_ROOT/apps/vgo-cli/src" python -m vgo_cli.main canonical-entry --repo-root "$REPO_ROOT" --artifact-root "$WORKSPACE_ROOT" --prompt "<current user task, verbatim>"
```

`--host-id` 与 `--entry-id` 仅为兼容 wrapper 或旧自动化而保留；正常启动时应省略它们。

只有当 canonical-entry 返回 `session_root` 之后，才验证规范证明产物。
`check` 证明的是 `installed locally`；运行时一致性与交付验收需要各自的证据。
规范启动的证明是启动后产物，要求在返回的 `session_root` 下存在：`host-launch-receipt.json`、`runtime-input-packet.json`、`governance-capsule.json` 与 `stage-lineage.json`。
`local-agent-kernel` 遵循同一证明规则。若它无法产出这些真相产物，它可以产出本地工作脚手架，但不得被视为 `canonical verified`。
若规范启动失败，报告 `blocked` 并给出具体失败原因，而不是模拟缺失的阶段或证明产物。

## 共识与任务演化

使用 `deep_interview`，直到用户与 Agent 就目标、范围、约束、交付物、相关未知项以及完成标准达成一致。在该任务专属摘要获得确认后冻结需求；第一次澄清是对话的一项输入。

把共识保存在已有的 TaskCard 中。追加被接受的修订，更新受影响的工作与检查，并且仅在其输入与验收仍然有效时复用结果。对会改变已约定结果、范围、风险或所需人工判断的决策，要显式呈现。

## 硬停止与重入

渐进式的受治理停止点是 `requirement_doc`、`xl_plan` 与 `phase_cleanup`。

当 `bounded_return_control.explicit_user_reentry_required = true` 时，停止
当前助手回合。在后续用户消息批准或修订当前边界之前，不要消耗重入
凭证。

这是硬性运行时边界，不是建议。它覆盖"持续执行直到完成"之类的普通
宿主自主规则。一份详细的原始请求并不等于对冻结需求或冻结计划的
批准。硬停止之后，不要在受治理重入之外执行等价的手工工作：同一
助手回合内不得进行计划编写、任务执行、手工变通交付，
也不得进行最终产物交付。

重入时，检查 `runtime-summary.json ->
bounded_return_control.host_decision_contract`，推断用户意图，
并写一个结构化的宿主决策 JSON 文件。使用相同的 `run_id`、
`bounded_reentry_token` 与稳定的 `workspace_root`：

在需求停止点，直接从 `agent_skill_organization_contract` 构建 `agent_skill_organization`；在此之前 `preferred_payload` 尚不完整，且不得通过失败重试或运行时源码检查来学习该 schema。使用引导阶段相同的 `REPO_ROOT` 与 `WORKSPACE_ROOT`：
```bash
DECISION_JSON="$WORKSPACE_ROOT/.vibeskills/tmp/host-decision.json"
mkdir -p "$(dirname "$DECISION_JSON")"

cat > "$DECISION_JSON" <<'JSON'
{
  "decision_kind": "approval_response",
  "decision_action": "approve_requirement",
  "approval_decision": "approve",
  "agent_skill_organization": {
    "schema_version": "agent_skill_organization_v1", "derived_by": "agent", "workflow_level": "L",
    "modules": [{"module_id": "module-a", "goal": "...", "candidate_skill_ids": ["skill-a"], "depends_on": [], "execution_mode": "skill_assigned", "acceptance_criteria": [{"criterion_id": "module-a-result", "description": "The module result satisfies the frozen requirement.", "verification_mode": "automated"}]}],
    "selected_skills": [{"skill_id": "skill-a", "module_ids": ["module-a"], "responsibility": "...", "reason": "..."}],
    "uncovered_modules": [],
    "workflow_level_contract": {"L": "smallest complete organization", "XL": "bounded multi-lane organization"}
  }
}
JSON

PYTHONPATH="$REPO_ROOT/apps/vgo-cli/src" py -3 -m vgo_cli.main canonical-entry \
  --repo-root "$REPO_ROOT" \
  --artifact-root "$WORKSPACE_ROOT" \
  --prompt "<current user task, verbatim>" \
  --continue-from-run-id "<source_run_id>" \
  --bounded-reentry-token "<reentry_token>" \
  --host-decision-json-file "$DECISION_JSON"
```

来自后续用户消息的结构化批准会推进到下一个渐进停止点。结构化
修订必须包含非空的 `revision_delta`，并重新冻结同一个有界
阶段，而无需先向用户请求单独批准：

```json
{
  "decision_kind": "approval_response",
  "decision_action": "revise_requirement",
  "approval_decision": "revise",
  "revision_delta": ["Use the revised dataset and agreed output scope."]
}
```

有界批准或修订必须停留在已呈现的有界阶段行动契约之内。

在 `requirement_doc` 停止点，读取 `runtime-summary.json -> host_user_briefing`，并使用 `host_user_briefing.rendered_text` 作为用户回复的主干。保持相同的字段顺序。
围绕 Agent 主导的 Skill 搜索指南来组织该停止点的呈现：把任务拆分为模块，按模块搜索本地 Skill，阅读候选 `SKILL.md`，同时组织 `L` / `XL` 两套计划，并诚实披露未被覆盖的模块。在需求冻结时不要透露入围清单规模、已选 Skill 排名或原始路由排序。
在回复解释了每个任务专属工作流并给出该选项对应的任务专属候选 Skill 名称之前，不要让用户在 L 与 XL 之间做选择。每个被点名的 Skill 都要标注为尚未被选择或使用的候选；正式选择仍属于需求批准之后由 Agent 完成的组织工作。

需求批准后，Agent 必须把已批准的工作拆分为模块，为每个模块搜索每一个已声明的本地 Skill 根目录，并阅读每个保留候选的 `SKILL.md`。宿主必须在进入 `xl_plan` 之前，把校验通过的结果放入 `HostDecisionJson.agent_skill_organization`；路由输出只能作为候选审计证据，不能填充该字段。若一个已选 Skill 负责多个模块，则每个模块都要有一条 `module_assignments` 条目，包含确切的模块 id、`owner`、`support` 或 `verifier` 角色、模块专属职责、一个具体的写范围、预期输出与验证。角色顺序是可执行的：`support` 先于 `owner` 运行并向其供给；`verifier` 仅在 `owner` 之后运行。owner 之后的复查或最小化检查必须用 `verifier`，而非 `support`。`agent_direct` 模块必须声明自己的具体 `write_scope`、`expected_outputs` 与 `verification`；运行时不得用泛化的模块标签或复述目标来替代它们。任务工作范围不得声称拥有 `module-execution.json` 这类规范运行时产物；只读工作应使用稳定的任务自有输出范围或 `no task-file writes`。改变模块、Skill、角色、依赖、写范围、输出、验证或工作流级别的计划修订必须重新提交完整更新后的 `agent_skill_organization`；仅凭 `revision_delta` 只记录文本，不会变更已冻结的组织。
在 `candidate_skill_ids` 与 `selected_skills[].skill_id` 中，都使用直接容纳被保留 `SKILL.md` 的目录名作为确切的 `skill_id`。展示用的 Skill 名称或 frontmatter `name` 只是描述性的，不是执行标识符。嵌套的被保留 `SKILL.md` 使用其自身所在目录名。提交前先从候选路径解析出该标识符，而不是通过失败重试来学习它。
模块验收标准必须在规范模块结果重入之前即可满足。它们不得要求清理回执、交付验收或完成语言许可，因为规范 `phase_cleanup` 只有在 `module-execution.json` 被接受之后才会创建这些内容。对普通模块，从其实际交付物以及正常命令或测试输出进行验证。不要为了证明执行顺序、Skill 使用或文件范围而虚构任务专属的哈希、回执、台账、矩阵、扫描或证明文件。只有当用户或领域契约需要某个额外证据产物时才要求它。
计划批准后，在 `plan_execute` 与清理阶段复用已冻结的 `agent_skill_organization`，除非用户修订已冻结的需求或计划，否则不要重跑程序化的 Skill 选择、不要悄悄增加 Skill、也不要替换已声明的缺口。`stage_order` 记录的是依赖深度，不是并行运行的许可；即使独立单元共享同一依赖阶段，L 仍然按单元逐个发出顺序波次。XL 最多可以在一个波次中放入两个依赖就绪的单元，且嵌套或重叠的写范围必须保持串行。

在完成所要求的计划确认之后，继续推进依赖就绪的工作，不必在单元之间
请求例行许可。在有意义的边界处给出简明的进度更新。如果用户修订了
已约定的任务，记录该修订并只重新规划受影响的工作，然后继续。

## 统一运行时契约

规范 `vibe` 只有一个运行时权威和一个可见的需求/计划
界面。固定状态机为：

1. `skeleton_check`
2. `deep_interview`
3. `requirement_doc`
4. `xl_plan`
5. `plan_execute`
6. `phase_cleanup`

对简单工作，这些阶段可以很轻量，但不会被静默跳过。
完整的运行时契约、阶段归属、谱系规则、内部 `M`/`L`/`XL`
分级、用户可见的 L/XL 工作流确认、清理规则与输出清单，均定义于
`protocols/runtime.md`。

`vibe` 是唯一的公开 wrapper 入口。已安装副本的更新使用上文描述的命令路径。

兼容性阶段 wrapper 仅限内部使用。若旧调用方仍发送
了某个 wrapper，则在运行时启动之前将其折叠为规范 `vibe`，并将其排除在
宿主可见的 Skill 表面之外。

## Skill 执行

已冻结的 `agent_skill_organization` 是任务-Skill 对应关系的唯一真相。在计划
批准之前，披露模块、候选、已选 Skill 及其理由、缺口，以及 L / XL 的差异。

把每个确认的模块组织为一个可验证的工作单元。使用已声明的 Skill
输出识别归属，用 `plan_hints` 塑造工作步骤，用
`verify_hints` 扩展模块检查。保留显式的模块
依赖，并把 `agent_direct` 保留为没有合适 Skill 的模块的
可见回退。每个工作单元都必须在已有 WorkPlan 中保留其预期输出、检查、
绑定理由与依赖链接。每个已绑定的分派都必须把这些字段与所选 Skill 指南
投射进已有的 ModuleAssignments 产物。

只有被选中的 Skill 才会成为绑定到模块的执行单元。宿主不得
虚构 Skill、提升路由候选、隐藏 Skill 会话，也不得开启另一个
需求/计划/运行时界面。选择、加载、计划、分派或一份
通用清单都不是贡献证明；完成需要可观察的
模块结果以及 `protocols/runtime.md` 中定义的模块验收。
计划批准后，`module-work-plan.json` 是唯一的分派权威。
`agent-execution-handoff.json.result_contract` 冻结 `module_execution_v1` 提交绑定；交接之后，复制 `result_contract.submission_template`，保留每一个冻结绑定，只填写结果字段。`criterion_results` 状态必须是 `passing`、`failing` 或 `blocked`。若规范在清理前拒绝该格式，则修正同一个 `module-execution.json` 并复用同一条返回命令，而不是再创建一次交接。当交接模板包含 `tdd_evidence` 时，代码任务的 TDD 证据应放在同一个 `module-execution.json` 内；在规范返回之前填写该结构化小节，不要另建一个 `tdd-evidence.json` sidecar。契约不是执行证据。
Agent 仍然要做真正的工作并创建 `module-execution.json`；必需的失败、阻塞、
缺失证据或等待人工评审都会阻塞任务完成。

对于 XL 委派，根/子层级仍然受治理：只有 `root_governed`
可以冻结规范需求/计划或做出最终完成声明。
`child_governed` 泳道继承已冻结的上下文，停留在被分配的写
范围内，校验 `delegation-envelope.json`，并且只发出本地回执。

## 质量规则

绝不无证据地宣称成功。最低不变式：

- 完成之前先验证。
- 不要做出静默的"无回归"声明。
- 让需求与计划产物可追溯到所启动的那次运行。
- 在宣称阶段完成之前先发出清理回执。
- 显式暴露失败、回退、降级状态或受阻状态。
- 不要添加 mock 成功路径、被吞掉的错误或仅靠模板的通过结果。
- 把脚手架或草稿产物视为 `proof_ready = false` 的 `needs_execution`；不要称之为已完成的工作。
- 只有当有效任务输入、所选 Skill 内容、依赖输出与已交付产物哈希都保持不变时才复用已完成的工作。验证之前重跑受影响的依赖链；前置条件失败时阻塞其依赖方。
- 不要用回退或边界行为绕过真正的执行、
  验证或根因修复。
- 当检查在已确认范围内失败时，针对该失败
  最多做一次有针对性的修复并重跑受影响的检查。
  若修复失败、需要范围决策或缺少所需证据，
  报告剩余的阻塞项。

## 用户交付

使用已有的 WorkDossier 作为详细证据来源。给用户一份
简短的交付摘要，包含已验证的结果、它们的
位置、实际运行过的检查以及真实的阻塞项。把脚手架排除在
已完成结果之外。内部回执与
诊断细节保留在 dossier 中，除非它们有助于用户做决策。

## 协议地图

仅在规范启动之后或维护本仓库时才阅读以下参考：

- `protocols/runtime.md`：受治理运行时契约与阶段归属
- `protocols/think.md`：计划、研究与执行前分析
- `protocols/do.md`：编码、调试与验证
- `protocols/review.md`：审查与质量门
- `protocols/team.md`：XL 多 Agent 编排
- `protocols/retro.md`：回顾与有证据支撑的修正

## 维护

- 运行时家族：governed-runtime-first
- 版本：4.1.1
- 更新日期：2026-10-18
- 主契约元数据：`core/skill-contracts/v1/vibe.json`
