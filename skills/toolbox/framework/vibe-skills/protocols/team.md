> **中文汉化版** · 上游：[foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) · 原文件：`protocols/team.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# vibe-team 协议

> **本协议的作用（通俗概述）**
>
> 这是多智能体编排协议。它规定 VibeSkills 如何协调多个 AI Agent，共同完成大型（XL 级）任务。
>
> 使用 VibeSkills 不需要读本文件。它是参考材料，面向在 VibeSkills 上构建的贡献者与高级用户，或想了解大型任务在内部如何协调的人。
>
> **下文用到的关键术语：**
> - **Root/Child lane（根通道/子通道）**：一个协调者（root lane）加多个工作者（child lanes）。只有 root 能对整个任务做出最终完成声明。
> - **Wave-sequential execution（波次顺序执行）**：大任务拆分为顺序的"波次"（wave）。同一波次内，相互独立的子任务可以并行。
> - **Scatter-gather（发散-汇聚）**：先扇出（把任务变体并行分派给多个 Agent），再扇入（收集全部结果并综合成一份输出）。
> - **Agent Skill 工作**：当前 Agent 在完成一个有界模块时遵循被指派的 skill（例如 `tdd-guide` 或 `code-review`）。Vibe 负责指派并校验工作，它自己不运行 skill。
> - **Dialectic mode（辩证模式）**：一种结构化设计分析，两组 Agent 分别从不同视角论证，随后由协调者综合双方的最优想法。
> - **ruflo**：可选的记忆与工作流编排组件，提供向量记忆、会话持久化与正式共识。
> - **spawn_agent / send_input / wait / close_agent**：内部 XL 编排 API 调用。用户不直接调用它们。


用于需要协调的 XL 级多智能体任务的协议。

## 治理运行时定位

本协议描述在运行时第 5 阶段 `plan_execute` 发出 `agent-execution-handoff.json` 之后，
当前 Agent 可以如何协调 XL 工作。
它不是独立的用户入口。

固定的用户可见运行时路径保持不变：

1. `skeleton_check`
2. `deep_interview`
3. `requirement_doc`
4. `xl_plan`
5. `plan_execute`
6. `phase_cleanup`

本协议只在需求与计划均已冻结之后激活。
现行工作契约是 `module-work-plan.json -> agent-execution-handoff.json
-> module-execution.json`。
`plan_execute` 不执行被指派的工作。它把已批准的模块交给当前 Agent，
后者通过规范 `vibe` 重入返回一份完整的 `module-execution.json`，然后 `phase_cleanup` 才能开始。

subagent-driven-development 在这里被视为一种被吸收的方法，而不是拥有路由的专家。是否使用 child lane 由 `vibe.plan_execute` 决定，且必须遵循已冻结的 M/L/XL 计划。

## 适用范围
在需要以下能力的 XL 级任务上激活：
- 具备依赖感知波次的多智能体协调
- 针对独立单元的步骤级有界并行（不是一刀切的常开并发）
- 按阶段的工作流式执行
- Swarm 或 hive-mind 协调
- 长时间运行的迭代任务

## 混合架构：Codex 原生团队 + ruflo 协作

Codex 原生 Agent API 负责生命周期与任务指派（主路径）。
ruflo 保持可选，用于工作流/记忆增强。

所有派生的子代理提示词必须以 `$vibe` 结尾，从而让治理运行时在被委派工作中始终是生效契约。

## Root/Child 权限模型

XL 委派使用两个治理范围：

- `root_governed`：每个用户任务一条通道；拥有规范的需求/计划真相与最终完成声明
- `child_governed`：被委派的通道；继承冻结的上下文，并产出本地执行证据

child-governed 通道保持 `vibe` 纪律，但不是新的顶层治理者。

child lane 的运行时强制：

- root 在被委派的子执行开始前发出 `delegation-envelope.json`
- 子代理启动时对照该 envelope 校验继承的需求/计划真相
- 子代理在开始有界单元之前记录委派校验

child-governed 通道不得：

- 创建第二个规范需求表面
- 创建第二个规范执行计划表面
- 为整个 root 任务发出最终完成声明
- 更改 root 冻结的 `agent_skill_organization`

## Agent 工作协调事实

- `L` 工作由当前 Agent 串行完成；本协议覆盖的是 XL 协调场景。
- `XL` 执行按依赖以波次顺序进行。
- `XL` 中的并行工作以步骤为范围，且仅限于独立单元。
- Agent 确认的 `agent_skill_organization` 在 XL 规划之前冻结；route 候选始终只是兼容性审计证据，而不是执行权威。
- 模块 skill 工作绑定到阶段：`pre_execution`、`in_execution`、`post_execution`、`verification`。
- 在 `XL` 中，模块工作单元通道只有在其写入范围互不相交且通道策略允许时才能进入有界并行窗口。

### 角色分工

| 关注点 | 提供方 | 工具 |
|---------|----------|------|
| Agent 派生 | Codex 原生 | `spawn_agent` |
| 任务指派与跟进 | Codex 原生 | `send_input` |
| Agent 同步 | Codex 原生 | `wait` |
| Agent 关闭 | Codex 原生 | `close_agent` |
| 工作流定义（可选） | ruflo | `workflow_create`, `workflow_execute` |
| 向量记忆（可选） | ruflo | `memory_store`, `memory_search` |
| 会话持久化（可选） | ruflo | `session_save`, `session_restore` |
| 共识算法（可选） | ruflo | `hive-mind_consensus` |

## 防漂移交契约

每次 XL 子任务移交都应保留：

- 首要目标，
- 声明的范围，
- 当前的完成状态目标，
- 任何已知的 report-only 防漂警告，
- 该工作是有界的专门化，还是泛化能力声明。

Lead Agent 规则：
- 子代理可以提出 report-only 警告，但不得发明新的硬门禁，
- 如果某个已批准策略或已失败门禁确实阻塞了进展，必须引用那个确切的表面，
- 聚合不得把有界专门化的输出抹平成泛化完成声明。
- 指派 Skill 时，保留其 `SKILL.md` 中的相关指令，而不是用泛泛的 lead Agent 文字替换它们。
- 只有 root-governed 聚合可以发布整个任务的最终完成声明。

## Agent Skill 工作

被选中的 Skill 指导一个有界模块。Vibe 组织工作并检查返回结果；它不直接运行 Skill。

先读有界工作：

- `agent_skill_organization` 是 root 冻结的任务-skill 真相
- `module_assignments` 是该组织经校验的工作投影
- `agent-execution-handoff.json` 把这些 root 批准的工作单元带给当前 Agent
- child lane 应继承有界工作契约，而不是即兴编造第二套 skill 选择叙事

规则：

- `vibe` 保持对阶段顺序、计划权威与完成声明的最终控制
- route 候选可以作为兼容性审计证据呈现，但它们绝不会自动晋升为已批准的模块工作单元
- 存在模块 Skill 工作时，`plan_execute` 必须发出一份 `agent-execution-handoff.json`，逐项写明每个模块、工作单元角色、被指派的 Skill 与 `skill_entrypoint`
- 当前 Agent 读取每份被指派的 `SKILL.md`，在冻结的需求上下文下完成其有界工作
- Agent 在一份 `module-execution.json` 中返回预期输出、结果摘要、失败、阻塞原因与模块状态
- 每个工作单元还携带阶段绑定、通道策略、写入范围与审查模式
- lead 聚合可以汇总模块结果，但不得抹掉 Skill 特定的验证记录
- 新 skill 只能通过用户批准的计划修订进入执行，该修订冻结更新后的 `agent_skill_organization`

层级特定的工作语义：

- `agent-execution-handoff.json`：来自 `module_assignments` 的 root 批准有界工作；child lane 只能接收这些继承单元
- `local_suggestion`：child lane 残留的 skill 建议，在 root 治理冻结已批准修订之前，它始终只是审计或升级证据

升级规则：

- 需要未批准 Skill 的 child lane 必须向 root 返回一次显式升级
- child lane 不允许静默激活 skill

## 编排选项

### 选项 A：Codex 原生团队 + ruflo 协作（首选）
1. 定义分解计划（负责人 + 接口 + 交付物）
2. 通过 `spawn_agent` 用角色专属提示词派生 Agent
3. 通过 `send_input` 指派工作与澄清
4. 通过 ruflo `memory_store` 存储中间状态（里程碑摘要、移交产物）
5. 需要显式步骤编排时使用 ruflo `workflow_create` / `workflow_execute`
6. 在每个里程碑通过 `wait` 同步
7. 需要正式共识时使用 ruflo `hive-mind_consensus`
8. 在 lead Agent/上下文中聚合并对齐输出
9. 通过 `close_agent` 关闭 Agent

### 选项 B：仅用 Codex 原生团队（ruflo 不可用时）
1. 只跑原生生命周期：`spawn_agent` → `send_input` → `wait` → `close_agent`
2. 用运行时中立的 state_store + 会话上下文保存里程碑状态
3. 保持同样的分阶段确认与验证门禁

### 选项 C：Ralph-loop（迭代任务）
当任务需要对同一提示词反复迭代时：
1. 用户显式调用 /ralph-loop
2. 选择引擎：
   - `compat`（默认）：本地状态循环，手动 `--next`，稳定且低依赖
   - `open`：委托外部 open-ralph-wiggum CLI 自动迭代
3. 定义完成承诺（退出条件）
4. 设置最大迭代次数（安全上限）
5. 对 `open` 引擎，活动循环期间优先使用 no-commit 模式，并在任何手动提交之前运行 VCO 质量门禁

重要：Ralph-loop 与活跃的团队编排互斥。

## Agent 类型选择

| 角色 | 原生 Agent 类型 | 说明 |
|------|-------------------|-------|
| 研究者 | `explorer` | 以读取/搜索为主的调查 |
| 规划者 | `default` | 计划 + 分解 |
| 实现者 | `worker` | 拥有实现所有权且范围隔离 |
| 审查者 | `worker` 或 `default` | 审查提示词强制先输出 bug/风险 |
| 安全 | `worker` 或 `default` | 安全聚焦的提示词与检查清单 |

## 团队模板
预定义组合见 references/team-templates.md：
- feature-team, debug-team, research-team, review-team, full-stack-team
- supervisor-scatter-gather（Agent-Squad 风格的 Supervisor + Specialists）
- dialectic-design

如果安装了 `local-vco-roles`，还可以使用：
- local-vco-dialectic-review（模板 7）
- 角色提示词来自已安装 skills 根目录：设置了 `CODEX_HOME` 时从其解析，否则用宿主默认 Codex home（通常为 `~/.codex`）

## Supervisor 式派发模式（Agent 即工具）

Agent Squad 的 `SupervisorAgent` 采用"agent-as-tools"模型：lead Agent 并行扇出任务，然后用一个有界共享内存（`<agents_memory>`）融合结果。

在 VCO XL 中，等价原语是：

```
spawn_agent × N → send_input (fan-out) → wait (fan-in) → close_agent
```

### Scatter-Gather 扇出/扇入（Agent Squad `send_messages`）

Agent Squad 提供一个内置工具（`send_messages`），接受 `{recipient, content}` 数组并并行执行扇出，然后返回汇聚的响应。

在 VCO XL 中，保持同样的*契约形状*，但用原生团队原语实现：
- **扇出**：对每个 Agent 执行 `send_input`（每个角色/Agent 一个子任务）
- **扇入**：每个里程碑一个 `wait` 屏障
- **汇聚**：Lead 每个里程碑更新一次 `<agents_memory>`（而不是持续更新）

经验法则：**一个里程碑 == 一轮 scatter-gather**。

### 派发信封（推荐）

使用 `send_input` 时，把每个子任务包进一个小信封，让可靠性 + 记忆变成机械动作（而不是临时即兴）。

```yaml
run_id: "{yyyy-mm-dd}#{short}"
phase: "plan|investigate|implement|verify"
owner: "{role_name}"
deadline_minutes: 15
retry_budget: 1
deliverable:
  format: "markdown"
  sections: ["summary", "evidence", "risks", "next_steps"]
memory:
  private_key: "team/{run_id}/agent/{owner}/notes"
  shared_key: "team/{run_id}/shared/agents_memory"
```

说明：
- 保持 `deliverable.sections` 稳定，Lead 才能快速聚合。
- `private_key` 是每个 Agent 私有的；`shared_key` 是唯一的跨 Agent 记忆。

### 任务契约（子任务接口 / DoD）

派发信封是*传输*。任务契约是*正确性*。

扇出之前，每个子任务应当（SHOULD）包含一份紧凑契约，避免专家跑偏或瞎猜：

```yaml
task_id: "T-1"
goal: "One-sentence, testable outcome"
scope:
  in: ["Allowed modules/files/APIs"]
  out: ["Explicit non-goals"]
inputs:
  - "Facts, constraints, and required context"
outputs:
  - "Artifacts (file paths) or result shape"
definition_of_done:
  - "Acceptance criteria (verifiable)"
verification:
  - "Commands/tests/checks to run"
handoff_questions:
  - "Missing info that must be confirmed by user/lead"
status: "todo|doing|blocked|done"
```

契约规则：
- 优先选择命令形态的 `verification`（可直接复制粘贴运行）。
- 缺少必要信息时，返回 `status=blocked` 并附 `handoff_questions`（不要瞎猜）。
- 同一份契约可干净映射到 GSD 波次契约（`entry_criteria`/`exit_criteria`/`verify_commands`）。
- 子任务已指派 Skill 时，契约要足够窄，让 child 能照着那份 `SKILL.md` 执行而无需即兴发明新方法。

## 共享内存契约（3 层）

为了让 XL 协调保持连贯同时避免上下文膨胀，把记忆分为三层：

1. **User ↔ Lead 记忆**：主对话（用户意图 + 决策的真相来源）。
2. **Lead ↔ Agent 私有记忆**：每个 Agent 的工作笔记（默认不广播）。
3. **共享 Agent 记忆**：由 Lead 拥有的有界、持续刷新的"目前已知信息"块。

对应到 Agent Squad 术语：
- **User ↔ Lead 记忆** ≈ User-Supervisor Memory
- **Lead ↔ Agent 私有记忆** ≈ Supervisor-Team Memory
- **共享 Agent 记忆** ≈ Combined Memory（`<agents_memory>`）

有界历史规则（成对安全）：
- 限制每个 Agent 的私有历史上限（例如最近 10–20 对消息）。
- 裁剪时保留完整的 user/assistant 消息对（避免出现孤儿半轮）。

### 共享内存格式（Supervisor 式）

Lead 维护一个滚动块（放在会话上下文中，可用时也可通过 ruflo `memory_store`）：

```text
<agents_memory>
[run_id] phase=investigate
- (Investigator-1) key finding: ...
- (Implementer-2) patch plan: ...
- Open questions: ...
- Next milestone: ...
</agents_memory>
```

规则：
- 只在里程碑边界（`wait` 之后）更新，不是每条消息都更新。
- 优先事实 + 产物，少写散文。适用时链接到文件路径或命令。
- 硬上限：一旦增长到上下文里放不下，就摘要并覆盖（不要无限追加）。

## 可靠性与失败处理（超时 + 重试预算）

借鉴 Agent Squad 的编排模式（有界历史、显式错误信息），XL 团队应把失败当作一等公民：

1. **超时**
   - 某个 Agent 错过 `deadline_minutes` 时，通过 `send_input` 发送一次提醒。
   - 仍无响应：带着部分结果继续，并在 `<agents_memory>` 中记录缺失的交付物。

2. **重试**
   - 遵守 `retry_budget`。每次重试必须改变*某些东西*（提示词约束、更窄的范围、更多上下文，或换一个角色）。
   - 重试预算耗尽时：要么缩小范围，要么用简化任务重生一个替补 Agent，但必须伴随显式 hazard alert，并把状态标记为 non-authoritative。

3. **矛盾**
   - 两个 Agent 意见相左时，Lead 执行 V2/V6：先要求具体证据（文件路径、日志行、命令输出），再做选择。

4. **降级模式**
   - 多个 Agent 失败或输出质量低时，不得静默回退到选项 B（仅原生）。任何降级路径都必须发出独立的 hazard alert，有意降低并行度，并在主路径恢复之前把结果标记为 non-authoritative。

## 分阶段确认
在以下节点必须与用户确认：
1. 工作流定义之后（派生 Agent 之前）
2. 每个主要阶段完成之后
3. 结果最终集成之前
4. 提交变更之前

模式感知的解释：
- `interactive_governed`：上述四个确认点默认保持用户可见

## GSD-Lite 波次契约钩子（可选）

策略来源：`config/gsd-overlay.json`

当 `enabled=true`、`mode != off` 且 `wave_contract.enabled=true` 时应用此钩子，但仅作为编排元数据。

激活条件：
- XL 规划：默认启用
- XL 编码：lead 预期会出现依赖敏感的多波次执行时启用
- 若 `wave_contract.xl_only=true`，M/L 绝不运行

契约输出：
- 生成 `waves.json`（或配置的产物），包含：
  - `wave_id`
  - `units`（任务 id / 负责人）
  - `depends_on`
  - `entry_criteria`
  - `exit_criteria`
  - `verify_commands`

执行语义：
1. 同一波次内，独立单元可以在有界并行中运行。
2. 波次按依赖顺序执行。
3. 验证门禁必须全部通过才能进入下一波次。
4. 此契约不改变级别/任务指派。

失败语义：
- 波次契约生成失败或不完整时，不得静默回退到标准选项 A/B 编排。若使用了降级路径，必须发出独立的 hazard alert，并记录由此产生的执行为 non-authoritative。
- 除非 strict 策略明确要求重新生成契约，否则不要阻塞整个 XL 流程。

## 质量注入：增强层（XL 默认）

在核心层（P5、V2、V7 + 来自 vibe-do 的任务类型专属模式）之外：

### 附加增强模式
- **P2**：投入分配。验证阶段的投入应与执行阶段相当，不可跳过。顺序：理解 → 规划 → 执行 → 验证，每阶段都应有明确产出。
- **P6**：PDCA 循环。Plan -> Do -> Check -> Act。不理解为何失败就绝不重试。
- **V4**：危险信号自查。拒绝："先临时修一下"、"试试改改 X"、"也许能行"。
- **V5**：合理化阻断。"现在应该能行" -> 要求验证。"我有信心" -> 信心 != 证据。
- **V6**：Agent 信任但要验证。Agent 返回后：独立检查 VCS diff，运行验证，对比声明与证据。

### XL 注入矩阵

| 任务类型 | 注入前 | 验证后 |
|-----------|--------------|-----------------|
| 计划 | P3, P5, P6 | V2, V5, V6, V7 |
| 编码 | P5, P6 | V2, V3, V5, V6, V7 |
| 审查 | P3, P5 | V2, V5, V6, V7 |
| 调试 | P1, P4, P5, P6 | V2, V4, V5, V6, V7 |
| 研究 | P2, P3, P5, P6 | V1, V2, V5, V6, V7 |

## 辩证模式

结构化多视角设计分析。仅在用户显式请求辩证智囊团模式时激活（`dialectic_team_requested = true`）。

### 适用场景

- 存在多个可行的架构方案但权衡不明
- 盲区代价高昂的高风险设计决策
- 用户显式请求"使用辩证智囊团"、"启用辩证智囊团"、"`$vibe dialectic`" 或 "dialectic-design"

### 不适用场景

- 实现任务（用标准编码流程）
- 单一正确答案的问题（用 sc:research）
- 琐碎设计选择（改用 think.md B2 Self-Check）
- 调试（用 debug-team 模板）

### XL 执行（Codex 原生团队）

使用 team-templates.md 中的 dialectic-design 模板。

**Step 1 — 准备上下文**
Lead 阅读相关代码/文档，拟定设计问题，并从 team-templates.md 的 Perspective Assignment 表中选择视角配对。

**Step 2 — 创建团队**
```
spawn_agent × 4: one per thinker agent
```

**Step 3 — 发送角色提示词模板**
每个 Agent 收到这段提示词（`{placeholders}` 由 Lead 填写）：

```
你是 {role} ({group} 组)。

设计问题：{question}

你的分析视角：{perspective}
上下文材料：{context_slice}

执行 6 阶段工作流：
1. Propose: 基于你的视角，独立提出一个完整方案（含架构、关键决策、风险）
2. Reflect: 列出你方案的 3 个最可能的生产环境失败模式
3. Synthesize: 基于自我批判改进方案 → 通过 send_input 发给组内伙伴
4. Compare: 收到伙伴方案后，分析两个方案的核心分歧点
5. Reflect on comparison: 伙伴看到了什么你遗漏的？为什么会产生分歧？
6. Final synthesis: 整合伙伴洞察，产出最终方案 → 通过 send_input 发给 Lead

输出格式（Phase 6）：
- 方案摘要（≤200字）
- 关键决策 + 理由（列表）
- 已知风险 + 缓解策略
- 从伙伴方案吸收的要素
```

**Step 4 — 上下文隔离**
A 组收到强调视角 A 关注点的上下文切片。
B 组收到强调视角 B 关注点的上下文切片。
两组不共享上下文，也不跨组通信。

**记忆注意事项（保持隔离真实）**
- 两组执行期间不要维护单一的共享 `<agents_memory>`。
- 如果需要汇总，由 Lead 维护**两个独立块**（仅 A 组 / 仅 B 组），并且只在 Step 6 之后合并。

**Step 5 — 执行**
4 个 Agent 运行 6 阶段工作流。组内通信通过 `send_input`（A1↔A2、B1↔B2）。最多 1 轮。

**Step 6 — 收集**
Lead 等待 4 份 Phase-6 输出。

**Step 7 — 超时处理**
任一 Agent 在合理时间内未响应时：
- 通过 `send_input` 发送提醒
- 仍无响应：用现有输出继续（至少 2 份，且来自不同组）
- 不足 2 份：中止辩证，回退到 think.md B2 Self-Check

**Step 8 — 输出处理**
Lead 分析 4 份最终综合：

```
1. Extract consensus: 所有方案一致同意的决策点
2. Extract divergence: 方案间的核心分歧 + 每方的论据
3. Identify blind spots: 某组发现而另一组完全未提及的风险/机会
4. Synthesize: 产出综合方案（consensus 为基础 + divergence 中选择最优 + blind spots 纳入风险清单）
5. Present to user:
   - 综合方案
   - 关键分歧点 + 各方论据（供用户决策）
   - 风险清单（含 blind spot 来源标注）
```

**Step 9 — 用户决策**
把综合结果呈现给用户。用户可以：
- 原样接受综合方案 → 进入实现
- 选择某一组的方案 → 沿该方向推进
- 就某个具体分歧点要求更深入分析

**Step 10 — 关闭**
通过 `close_agent` 关闭全部 4 个 Agent。

### L 级适配

L 级不使用 XL 团队编排。顺序使用 2 个宿主 Agent：

```
1. Agent-A: spawn_agent(agent_type="default" or "worker", prompt="{question} 从 {perspective_A} 视角分析")
2. Agent-B: spawn_agent(agent_type="default" or "worker", prompt="{question} 从 {perspective_B} 视角分析")
3. Lead synthesizes both outputs using the same output processing algorithm (Step 8)
```

相比 XL 的局限：没有组内对话（每个视角仅 1 个 Agent），没有 Phase 3-5 精炼。适合中等复杂度的设计决策。

### 与 think.md 的集成

- 若 `dialectic_team_requested = true` 且级别 = L/XL → 跳过 think.md B2 Self-Check，改用辩证模式
- 若 `dialectic_team_requested = true` 且级别 = M → 使用 think.md B2 Self-Check（团队辩证对 M 级是杀鸡用牛刀）
- 辩证模式输出作为设计基础汇入 `vibe.xl_plan`

## 冲突规避
- 不要把 Everything-CC agents 当作 XL 主执行者（用 Codex 原生团队）
- XL 任务不要用 Superpowers subagent-driven-dev
- Ralph-loop 与活跃的团队编排互斥
- 每个项目同一时间只允许一个团队活跃
- Agent 间通信优先用 `send_input`
- 不要绕过规范重入；XL 工作必须在 `phase_cleanup` 之前返回完整的 `module-execution.json`

## BrowserOps / DesktopOps 治理钩子

在 Wave24–30 之后，XL 团队执行涉及真实浏览器或 open-world GUI 任务时，必须额外遵守以下边界：

- BrowserOps 只通过 provider policy 建议已允许的宿主能力，不得安装 MCP，
  也不得绕开 VCO 主路由。
- DesktopOps 只允许以 `shadow/advisory/contract` 形式吸收 `Agent-S` 思路，不得把任何外部桌面代理提升为默认执行 owner。
- 若 BrowserOps / DesktopOps 建议与主计划冲突，优先服从 `references/conflict-rules.md` 与 cross-plane conflict policy。
- 进入 soft/strict 之前，必须能提供对应 gate 与 rollback command。

相关资产：
- `docs/design/browserops-provider-integration.md`
- `docs/design/agent-s-shadow-integration.md`
- `docs/governance/cross-plane-conflict-governance.md`
- `docs/promotion-board-governance.md`

## Wave19-30 专项角色

在 XL 多智能体执行中，Wave19-30 新增以下"治理型角色"，它们提供建议与验证，不接管 VCO 总编排：

- **Memory Contract Steward**：检查 Memory Runtime v2、`mem0`、`Letta` 是否越权。
- **Prompt Intelligence Steward**：检查 prompt cards / risk checklist 是否只停留在 advisory 层。
- **BrowserOps Provider Steward**：负责 provider candidate 建议与 browser contract 校验。
- **DesktopOps Shadow Steward**：负责 ACI/open-world 合同化，不允许默认 takeover。
- **Promotion Board Steward**：负责 rollout evidence、blocking findings、rollback plan 汇总。

团队规则：
1. 治理型角色不能直接替代 implementer / reviewer / router。
2. 任何角色给出的 promote 建议都必须经过 promotion board gate。
3. 子代理的文件写入范围必须提前切分，避免互相覆盖。
