> **中文汉化版** · 上游：[foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) · 原文件：`protocols/runtime.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# vibe-runtime 协议

> **本协议的作用（通俗概述）**
>
> 每次调用 `/vibe` 或 `$vibe`，系统都会运行这个 6 阶段流程。使用 VibeSkills 不需要读这份文档，它是参考材料，面向想了解运行时内部机制的贡献者与高级用户。
>
> **用大白话说，这 6 个阶段是：**
>
> | 阶段 | 内部名称 | 发生什么 |
> |:---:|:---|:---|
> | 1 | `skeleton_check` | 开工前检查仓库里已有什么 |
> | 2 | `deep_interview` | 澄清你真正想要什么（提问或推断） |
> | 3 | `requirement_doc` | 把达成一致的需求锁定成文档 |
> | 4 | `xl_plan` | 编写执行计划 |
> | 5 | `plan_execute` | 把已批准的模块计划交给当前 Agent |
> | 6 | `phase_cleanup` | 清理临时产物并产出最终报告 |
>
> **下文用到的关键术语：**
> - **Agent skill organization**：Agent 把已批准的工作拆成模块，搜索已声明的本地根目录，读取候选 `SKILL.md`，并在规划前冻结 `agent_skill_organization`。
> - **Local skill candidate audit**：语义所有者为 `packages/runtime-core/src/vgo_runtime/router_contract_runtime.py`；兼容桥为 `scripts/router/resolve-pack-route.ps1`。它只提供审计证据，不是任务-skill 真相。
> - **Root/Child lane（根通道/子通道）**：多智能体任务中，"root" 是协调者；"child" 通道是工作者。只有 root 能做最终完成声明。
> - **Frozen requirement/plan（冻结的需求/计划）**：一旦你批准需求或计划，它们就被锁定，系统不会悄悄改变范围。
> - **Proof bundle（证据包）**：任务确实完成的证据：测试结果、输出日志、验证命令。
> - **Silent fallback（静默回退）**：不告知用户就悄悄切换到降级路径。这是明确禁止的。


`vibe` 的治理运行时契约。

本协议定义所有宿主语法共享的用户可见运行时路径。
它不创建第二个 router 或第二个运行时表面。
它定义 `$vibe` 进入治理运行时之后必须发生什么。

需要解释一次运行或检查产物时，按以下阅读顺序：

1. 先读 `current-runtime-field-contract.md`，加上本次运行的工作产物，如 `work_dossier`、`module_assignments`、`work_results`、`verification`
2. 大多数正常运行到此为止，读工作真相而不是兼容链
3. 用本协议理解阶段顺序与运行时生命周期
4. 只有仍需要兼容性候选审计链时才读 `current-routing-contract.md`

围绕本协议的公开证明层保持很窄：

- `installed locally` 属于安装回执 / `check`，在本协议之外。
- `runtime coherent` 只有在规范入口返回 `session_root` 且运行时真相产物存在之后才开始。
- `delivery accepted` 由清理期间写出的交付验收报告决定。

## 运行时身份

`vibe` 在所有宿主上是同一个 skill 契约：

- `/vibe`
- `$vibe`
- Agent 调用的 `vibe`

这些是同一个治理运行时的语法变体，不是独立入口。

## 契约优先级

1. `vibe` 运行时权威保持完整。
2. 用户可见运行时路径保持固定。
3. `M`、`L`、`XL` 不是独立的公开入口命令；在交互式治理工作中，L/XL 工作流级别是执行规划之前的一次用户可见确认。
4. 需求冻结发生在计划执行之前。
5. 阶段被视为完成之前必须清理。
6. 禁止静默回退与静默降级。
7. 回退成功不具权威性，除非需求明确批准例外。
8. 禁止假成功行为：主路径失败时，运行时不得吞掉错误、发出 mock 完成或模板化一个通过结果。
9. 新的回退或边界行为只有在现行需求明确批准时才允许存在，且必须保持显式、可追溯、易于禁用。
10. `L` 串行移交模块单元；`XL` 只能对写入范围互不相交且依赖就绪的单元分组。

## 官方运行时模式

### `interactive_governed`

唯一支持的模式。

- 需要时直接提出高价值问题
- 冻结一份带用户可见假设的需求文档
- 允许在执行之前设置批准边界

## 运行时谱系产物

官方治理入口通过运行时校验并有产物支撑的谱系：

- `governance-capsule.json`：由 root 撰写的本次治理运行的运行时权威胶囊
- `stage-lineage.json`：本次运行的有序阶段迁移台账
- `host-launch-receipt.json`：面向宿主的规范入口回执，必须先为 `verified` 才能声称规范 vibe 入口
- `host-stage-disclosure.json`：仅追加的宿主消费事件流，记录讨论、规划与 Agent 工作中确认的模块与 Skill 组织
- `delegation-envelope.json`：由 root 撰写的子启动契约，携带继承的需求/计划真相
- `delegation-validation-receipt.json`：子代理证明 envelope 校验已在有界执行之前通过

这些产物只强化官方治理路径。
它们不声称操作系统级或任意 shell 会话级的强制。

只读 `SKILL.md`、包装 markdown 或引导文本并不构成规范 vibe 入口的证明。
规范声明需要 `host-launch-receipt.json`、`runtime-input-packet.json`、`governance-capsule.json` 与 `stage-lineage.json`。

## 固定 6 阶段状态机

### Stage 1: `skeleton_check`

目的：

- 校验仓库骨架与治理运行时前置条件
- 发现在生效的需求或计划产物
- 检测相互冲突的脏状态

必需输出：

- 骨架回执
- 仓库状态摘要

### Stage 2: `deep_interview`

目的：

- 把原始任务文本转换成结构化意图契约

必需字段：

- goal
- deliverable
- constraints
- acceptance criteria
- product acceptance criteria
- manual spot checks
- completion language policy
- delivery truth contract
- non-goals
- autonomy mode
- open questions
- inference notes

L/XL 工作必需的用户可见确认门：

- `workflow_level_confirmation`：用通俗语言解释 L 与 XL 的区别，推荐其中一个级别；在两个选项都展示任务专属工作流、候选 skill 名称及每个候选的职责之前，不要让用户选择。候选名称必须标注为尚未被选中或使用；正式选择仍在需求批准之后的 `agent_skill_organization` 中进行。
- `skill_use_confirmation`：在候选 Skill 被推荐之后、成为已批准模块指派之前，告诉用户"我将会在接下来的工作中使用这些 skills，你觉得 OK 吗？"，然后停下来等待批准、拒绝或修订。

这些门不创建新的运行时入口。它们是单一 `vibe` 运行时内部的子门。

### Stage 3: `requirement_doc`

目的：

- 冻结本次运行的唯一需求来源

规则：

- 写在 `docs/requirements/` 之下
- 执行与审查都能回溯到这份文档
- 在这里冻结下游交付语义，包括产品验收标准、人工抽查与完成措辞限制
- 当规范的防代理目标漂移策略激活时，治理需求包必须携带其声明的目标、代理信号、范围、抽象层、完成与证据字段

### Stage 4: `xl_plan`

目的：

- 在 `docs/plans/` 之下生成执行计划

必需内容：

- 内部执行级别
- 冻结的 `agent_skill_organization`
- 任务模块与每模块候选 skill
- 最终选定的 skill 及其职责与理由
- 未覆盖模块
- 已批准的模块依赖、执行模式、工作单元、写入范围与验收标准
- 每个模块至少冻结一个验收标准对象，具有唯一的
  `criterion_id`、非空 `description`，以及 `automated` 或 `manual` 的
  `verification_mode`
- L / XL 组织差异
- 波次或批次结构
- 所有权映射
- 验证命令
- 交付验收计划
- 完成措辞降级规则
- 回滚策略
- 清理预期
- 当规范的防代理目标漂移策略激活时，治理计划必须包含规范模板所使用的防漂控制面

### Stage 5: `plan_execute`

目的：

- 把冻结的模块计划编译成当前 Agent 可执行的工作
- 停下来把控制权交给 Agent，直到完整模块结果通过规范 `vibe` 返回

规则：

- 已批准的 `module-work-plan.json` 工作流级别控制拓扑，是计划批准之后唯一的工作权威
- `plan_execute` 把 `module-work-plan.json` 编译成 `agent-execution-handoff.json`，把移交标记为 `agent_action_required`，并把控制权交给当前 Agent
- 每个移交单元都要写明其单元、模块、被指派的 Skill、`skill_entrypoint`、职责、预期输出、验证、依赖与写入范围
- 当前 Agent 串行执行 `L` 单元；对 `XL`，只能对依赖就绪且写入范围互不相交的单元分组
- 官方入口在 stage-lineage 校验继续之前写入治理胶囊
- 后续阶段必须为同一治理运行追加匹配的谱系条目
- 派生的子代理提示词必须以 `$vibe` 结尾
- 里程碑证据必须在阶段完成之前写出
- 移交只能包含来自已批准 `module-work-plan.json` 的工作单元；packet 投影与 route 审计字段不能增加工作
- route 候选只是兼容性审计证据；它们不得自动晋升为已批准移交单元，也不得阻塞治理阶段推进
- Vibe 不代替 Agent 执行模块 Skill，也不代替它创建完成结果、stdout/stderr 或成功回执
- `agent-execution-handoff.json.result_contract` 只是 `module_execution_v1` 的确切提交 schema，以及冻结的源运行、计划摘要、单元绑定与模块绑定契约；它不是执行证据，也不是模块结果
- Agent 必须复制 `result_contract.submission_template`，保留每个冻结绑定，填写单元与模块结果字段，并保持确切的计划 criterion id；`criterion_results` 状态只能是 `passing`、`failing` 或 `blocked`
- 移交包含代码任务的 `tdd_evidence` 契约时，Agent 在同一份 `module-execution.json` 内填写它；单独的 `tdd-evidence.json` sidecar 不属于 Agent 返回契约
- 当前 Agent 读取每个被指派的 `skill_entrypoint`，遵循那份 `SKILL.md`，做真正的模块工作，把完整结果写入 `module-execution.json`，并通过规范 `vibe` 重入返回以供验收
- 规范重入在 `phase_cleanup` 之前校验源运行、已批准计划摘要、完整的工作单元与模块绑定、criterion 结果集与终止状态；格式被拒时运行停留在 `plan_execute`，Agent 修正同一份 `module-execution.json` 并复用同一返回命令，而不是另建移交
- 每个返回单元保留其模块 id、工作单元 id、角色、依赖阶段、写入范围与审查模式
- `blocked_gap` 模块必须保留其已批准的 `gap_reason`；清理必须同时点名被阻塞模块与该原因
- 运行时选择的 skill 保持为 `vibe`；任务-skill 真相来自 Agent 确认的组织，而不是 route 输出
- 只有当被指派的工作单元在 `module-execution.json` 中完成时，Skill 才算被使用；选择、规划、移交与泛化清单都不能证明使用
- 未完成、失败或被阻塞的必需模块不能进入成功清理，也不能支撑完成声明
- child-governed 通道继承 root 冻结的需求/计划上下文，不得打开第二个规范需求或计划真相表面
- child-governed 启动需要 root 撰写的 `delegation-envelope.json`
- child-governed 启动必须在有界工作之前发出 `delegation-validation-receipt.json`
- 治理执行期间，默认禁止对受管根目录使用危险的批量删除与盲目递归清空命令
- 破坏性删除必须收窄到显式唯一路径，以独立 hazard alert 呈现，并记录在回执中，而不是藏在便利性清理背后
- 运行必须在收尾期间发出下游交付验收报告，避免过程成功被悄悄改标为项目交付成功

### Stage 6: `phase_cleanup`

目的：

- 以干净、可审计的方式关闭阶段

最低动作：

- 成功清理之前先接受完整且与计划匹配的 `module-execution.json`
- 临时产物清理
- 仓库卫生检查
- node 审计或清理
- 写出清理回执
- 极端情况下允许的破坏性清理必须保持路径有界且有回执支撑；不得对受管根目录做一刀切递归清空
- 写出交付验收报告，附完成措辞许可或降级

## 协议委托

运行时可以把阶段内部工作委托给现有协议：

- `think.md` 负责分析、计划与研究
- `do.md` 负责执行、调试与验证
- `review.md` 负责质量审查
- `team.md` 负责 XL 编排
- `retro.md` 负责工作收尾后的复盘学习

委托不得绕过固定阶段顺序。

## 本地 Skill 候选审计规则

- 候选审计语义所有者仍是 `packages/runtime-core/src/vgo_runtime/router_contract_runtime.py`
- Python 直接优先是当前本地已安装候选发现的路径
- 保留的 PowerShell 调用方仍通过兼容桥 `scripts/router/resolve-pack-route.ps1` 进入
- 候选分数、排名与 `confirm_required` 只是兼容性审计元数据
- 候选审计不得填充 `agent_skill_organization`、增加已批准工作或阻塞阶段推进
- provider 支撑的智能仅作建议
- 回退或降级路径必须发出显式 hazard alert，而不是静默警告
- 回退或降级路径必须把运行时真相降级为 `non_authoritative`

## 权威边界契约

生态可以携带多个有益层次，但运行时权威必须保持单一所有者。

层次所有权如下：

- VCO 治理运行时：公开入口、阶段顺序、需求冻结、计划可追溯性、Agent 移交、模块结果验收、清理回执
- 本地 skill 候选审计：治理运行时内部的兼容性证据
- 宿主桥：仅做隐藏治理上下文附着与宿主 Hook 接线
- 过程方法层：只做工作流纪律，绝不是第二个运行时表面

明确禁止：

- 第二个可见运行时入口仪式
- 第二个路由权威层
- 第二个需求真相表面
- 第二个计划真相表面

过程纪律层可以要求遵循某个工作流。
它们不得替换、遮蔽或复制治理运行时真相。

## Root/Child 层级契约

XL Agent 工作期间，委派是层级式的，而不是递归的顶层治理：

- `root_governed` 通道：
  - 拥有规范需求冻结
  - 拥有规范计划冻结
  - 拥有冻结的 `agent_skill_organization` 及其 Agent 移交投影
  - 拥有整个任务的最终完成声明
- `child_governed` 通道：
  - 继承 root 冻结的需求与计划上下文
  - 执行有界的被委派单元
  - 只返回有界模块结果与升级请求

child-governed 通道必须保持 `$vibe` 纪律，但禁止创建第二个规范真相表面。

child-governed 通道明确禁止：

- 在 `docs/requirements/` 之下写第二个规范需求文档
- 在 `docs/plans/` 之下写第二个规范执行计划
- 为 root-governed 任务发出最终完成声明
- 未经 root 批准更改冻结的 `agent_skill_organization`

层级下的 Agent 移交语义：

- `agent-execution-handoff.json`：把来自 root 批准模块计划的 Skill 指派工作单元带给当前 Agent
- 子模块工作必须保留模块 id、工作单元依赖、写入范围与审查模式
- 子代理提出的候选建议在用户批准的计划修订冻结新组织之前，始终只是审计或升级证据

## 产物契约

预期运行时产物：

- `outputs/runtime/vibe-sessions/<run-id>/skeleton-receipt.json`
- `outputs/runtime/vibe-sessions/<run-id>/intent-contract.json`
- `outputs/runtime/vibe-sessions/<run-id>/runtime-input-packet.json`，存在有界 skill 帮助时携带一等 `agent_skill_organization` 及其 `module_assignments` 投影
- 需求文档
- 执行计划
- `outputs/runtime/vibe-sessions/<run-id>/module-work-plan.json`
- `outputs/runtime/vibe-sessions/<run-id>/agent-execution-handoff.json`（Agent 工作进行期间）
- `outputs/runtime/vibe-sessions/<run-id>/module-execution.json`（Agent 返回终止模块结果之后）
- 阶段回执
- 清理回执
- runtime-input packet 中 Agent 确认的 skill 组织（存在有界 skill 帮助时）
- 冻结 Agent 组织的工作流级别确认与计划批准记录
- 标明 `root_governed` 与 `child_governed` 通道的层级范围权威标记
- child-governed 通道提出未批准模块工作时的显式升级产物
- 证明是否允许完整下游完成措辞的交付验收报告

## 成功标准

只有满足以下条件才认为治理运行时健康：

- 6 阶段顺序得到保持
- 需求与计划产物存在
- 被接受的 Agent 模块结果能回溯到已批准计划与移交
- 清理有记录
- 没有验证证据就不做成功声明
- 治理包中的防代理目标漂移完成语义未被静默绕过
- 在允许完整完成措辞之前，下游交付真相与运行时/过程真相分开评估
- 任何回退或降级路径都不得呈现为等价成功
- 任何回退或降级路径都发出独立 hazard alert
- 没有经校验的 `host-launch-receipt.json`、`runtime-input-packet.json`、`governance-capsule.json` 与 `stage-lineage.json`，任何运行都不得声称规范 vibe 入口
- 计划批准后的移交停止需要摘要绑定的 `module-work-plan.json` 加 `agent-execution-handoff.json`；成功收尾还需要被接受的 `module-execution.json`
