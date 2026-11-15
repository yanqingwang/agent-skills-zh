> **中文汉化版** · 上游：[foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) · 原文件：`core/skills/vibe/instruction.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# vibe 规范指令

当任务需要跨计划、编码、调试、审查或多智能体执行的治理运行时时，使用 `vibe`。

规范规则：

- 把当前用户任务逐字传给 canonical-entry 作为任务规格；无关的聊天历史可以排除。不要总结、改写或压缩成关键词。保留确切的输入路径、输入不可变约束、确切的输出根目录、合成数据证据边界、模块依赖与安全并行边界，以及验收标准
- `vibe` 保持运行时权威；内部专家推荐器只建议有界的专家帮助
- 用户可见运行时路径固定为 skeleton_check -> deep_interview -> requirement_doc -> xl_plan -> plan_execute -> phase_cleanup
- `/vibe`、`$vibe` 与 Agent 调用的 `vibe` 是同一个运行时契约
- 可发现的包装标签可以请求更早的终止阶段，但它们绝不创建第二个运行时权威
- `M`、`L`、`XL` 是内部执行级别，不是用户可见入口分支
- provider 辅助智能可以建议，但不得替代 `vibe` 运行时权威
- 用户显式工具选择覆盖路由
- 在 `requirement_doc`，宿主必须按相同字段顺序复用来自 `host_user_briefing` 的运行时 skill 搜索指南与工作流级别确认：说明 Agent 将把任务拆成模块、按模块搜索本地 skill、读取候选 `SKILL.md`、同时组织 L/XL 两套计划、诚实披露未覆盖模块，并且不展示入围清单或选定 skill 排名
- 在为两个选项分别解释任务专属工作流、说出任务专属候选 skill 名称并明确说明这些 skill 尚未被选中或使用之前，宿主不得让用户选择 L 或 XL
- 需求批准之后，Agent 必须把已批准工作拆成模块，为每个模块搜索每个已声明的本地 skill 根目录，并读取每个保留候选的 `SKILL.md`
- 一个选定 Skill 拥有多个模块时，每个模块都要有一条 `module_assignments` 条目，写明确切模块 id、`owner`、`support` 或 `verifier` 角色、模块专属职责、一个具体写入范围、预期输出与验证
- 角色顺序是可执行的：`support` 在 `owner` 之前运行并为其供料；`verifier` 只在 `owner` 之后运行。owner 之后的审查或最小化检查必须用 `verifier`，不能用 `support`
- `agent_direct` 模块必须声明自己的具体 `write_scope`、`expected_outputs` 与 `verification`；运行时不得用泛化模块标签或复述目标替换它们。任务工作范围不得声称规范运行时产物（如 `module-execution.json`）；只读工作使用稳定的任务自有输出范围或 `no task-file writes`
- 更改模块、Skill、角色、依赖、写入范围、输出、验证或工作流级别的计划修订，必须重新提交完整更新后的 `agent_skill_organization`；单独的 `revision_delta` 只记录文本，不会改动冻结组织
- 进入 `xl_plan` 之前，宿主必须把校验通过的组织放进 `HostDecisionJson.agent_skill_organization`；兼容性 route 候选不得填充它
- 模块验收标准必须在规范模块结果重入之前可满足。它们不得要求清理回执、交付验收或完成措辞许可，因为规范 `phase_cleanup` 只有在 `module-execution.json` 被接受之后才创建这些
- 普通模块从其实际交付物与正常命令或测试输出验证。不要为了证明执行顺序、Skill 使用或文件范围而发明任务专属哈希、回执、台账、矩阵、扫描或证明文件。只有用户或领域契约需要那个产物时，才要求额外的证据产物
- 计划批准之后，复用冻结的 `agent_skill_organization`，把 `module-work-plan.json` 当作唯一派发权威，并把每条执行结果在 `module-execution.json` 中绑定到其摘要；复制 `result_contract.submission_template`，保留每个冻结绑定，只填结果字段。`criterion_results` 状态必须严格为 `passing`、`failing` 或 `blocked`；清理前格式被规范拒绝时，修正同一份 `module-execution.json` 并复用同一返回命令，而不是另建移交；不要重跑程序性 skill 选择、悄悄添加 skill 或隐藏已声明的缺口
- 移交模板包含 `tdd_evidence` 时，代码任务的 TDD 证据属于同一份 `module-execution.json` 内部；在规范返回之前填写该结构化小节，不要另建 `tdd-evidence.json` sidecar
- `stage_order` 记录依赖深度，不是并行运行许可；即使独立单元共享依赖阶段，L 仍然发出单单元顺序波次。XL 一个波次最多放两个依赖就绪单元，嵌套或重叠的写入范围必须保持串行
- 先按模块报告进度与清理；必需模块失败、阻塞、缺证据或待人工审查时，必须阻止完整任务措辞
- 把 selected、loaded、executed、contributed、accepted 保持为不同状态；只有模块绑定的可观察贡献证据才能确立实际 skill 使用
- XL 执行可以使用多智能体编排，但必须保持需求冻结、审查、清理与无回归纪律
