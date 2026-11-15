> **中文汉化版** · 上游：[foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) · 原文件：`protocols/think.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# vibe-think 协议

> **本协议的作用（通俗概述）**
>
> 这是计划与分析协议。它规定 VibeSkills 如何澄清需求、设计架构、编写执行计划，主要覆盖运行时的 Stage 2-4。
>
> 使用 VibeSkills 不需要读本文件。它供想了解系统在行动之前如何思考的人参考。
>
> **下文用到的关键术语：**
> - **Phase A / Phase B**：协议内部阶段。Phase A = 执行前分析（给任务分类）；Phase B = 计划与设计执行（写计划）。
> - **Proxy-goal drift（代理目标漂移）**：系统优化可见指标而不是真实目标。计划阶段是预防它成本最低的地方。
> - **GSD-Lite Preflight Hook**：可选的规划增强，在写计划之前加入棕地上下文快照与假设验证步骤。
> - **Brownfield context（棕地上下文）**：已有自身架构与约定的现存代码库，与白板新项目相对。
> - **Dialectic mode（辩证模式）**：结构化多视角设计分析：两组 Agent 分别论证不同观点，随后由协调者综合双方最优想法。


路由前分析与路由后计划/设计/研究协议。

## 治理运行时定位

本协议不是独立的用户入口。
它是 `protocols/runtime.md` 定义的治理 `vibe` 运行时内部使用的计划与分析表面。

用户可见运行时路径保持固定：

1. `skeleton_check`
2. `deep_interview`
3. `requirement_doc`
4. `xl_plan`
5. `plan_execute`
6. `phase_cleanup`

`think.md` 主要负责阶段 2 到 4：

- `deep_interview`：澄清意图或推断假设
- `requirement_doc`：冻结需求契约
- `xl_plan`：生成可执行计划

`M`、`L`、`XL` 仍然是同一个运行时策略表面，而不是分开的
入口分支。在 `interactive_governed` 运行中，L/XL 选择也是
需求与计划冻结之前的一次用户可见工作流级别确认。

## 运行时模式行为

### `interactive_governed`

治理规划模式。

- 歧义阻碍规划质量时提出高价值问题
- 执行之前要求一次用户可见的需求冻结
- 允许在执行开始之前设置批准暂停

本协议交给执行时必须带有一份冻结需求产物和一份计划产物。

## 防漂规划护栏

计划是预防代理目标漂移成本最低的第一道关口。

防漂策略激活时：
- 先冻结首要目标，再讨论实现便利性，
- 显式点名非目标的代理信号，
- 让验证材料保持验证角色，而不是让示例变成需求，
- 诚实地声明预期范围与完成状态，
- 泛化尚未被证明时，把有界专门化保留为有效结果。

这条规划指导是提升需求质量的顾问支撑。
它不会在已批准的需求与计划契约之外创建隐藏硬门禁。

## 先闭环预检（2 次探测 + 1 次验证）

即使在做计划/研究，主要失败模式也是**停摆**（dead-air）。
所以要尽早就跑一个最小闭环：探测上下文 → 定位证据 → 验证假设。

### 契约（不写代码）
在前 3 个动作内完成：
1. **Probe #1（glob，快）：**查看仓库形态 / 可用文档。
   - 示例：`Get-ChildItem -Force | Select-Object Name`
2. **Probe #2（rg，定向）：**搜索最相关关键词与现有计划/规格。
   - 示例：`rg -n -F -e '<keyword>' docs .`
3. **Verify #1：**给出最终建议之前，至少用 1 份产物验证 1 个关键假设：
   - 仓库证据（README/配置/代码），或
   - 事实性声明用 2 个独立外部来源（研究）。

### Router 提示（可用时）
VCO router 输出包含以下内容时：
- `closure_advice`：遵循 `closure_advice.contract.probes` + `closure_advice.contract.verify`（尽量逐字采用）。
- `exploration_advice`：用 `exploration_advice.recommended_execution_mode` 控制分析节奏，但**仍要尽早做探测**。

## 适用范围

### Phase A: 执行前分析（L 级，实现之前）

L 级任务在执行前需要结构化分析时激活：
- 任务可归入多种类型 → 通过分析澄清
- 用户显式要求"分析"、"想清楚"或"评估"
- 复合任务需要拆分为阶段

### Phase B: 计划与设计执行（L 级）

L 级计划、设计与研究任务激活：
- 需求分析与发现
- 架构与系统设计
- 研究与调查
- 方案评估与对比

## Phase A: 执行前分析

### A1: 问题界定
工具：无（Claude 原生推理）
- 到底要求的是什么？约束是什么？
- 这是单一任务还是复合任务？

### A2: 结构化分析（按预估级别）

| 预估级别 | Vibe 原生方法 | 阶段 |
|----------------|--------------------|-------|
| M | 简洁的风险与目标检查 | `deep_interview` |
| L | 结构化的方案、约束与验收标准 | `deep_interview` -> `requirement_doc` |
| XL | 苏格拉底式澄清加显式权衡对比 | `deep_interview` -> `xl_plan` |
| 任何重代码场景 | 计划文本之前先做仓库证据探测 | `skeleton_check` -> `xl_plan` |

### A3: 分类决策
基于分析输出确定：
- 最终级别（可能与初始预估不同）
- 任务类型（plan/code/review/debug/research）
- 复合任务？ -> 拆分（见下）
- 运行时模式匹配：
  - 治理计划与执行用 `interactive_governed`

### 复合任务分解

| 级别 | Vibe 原生方法 | 阶段 |
|-------|--------------------|-------|
| M | 简短串行清单 | `xl_plan` |
| L | 带负责人、验证与回滚说明的阶段计划 | `xl_plan` |
| XL | 带有界并行窗口的波次顺序计划 | `xl_plan` -> `plan_execute` |

输出：有序阶段，每个阶段带协议、质量门与移交上下文。

### 示例："设计并实现用户认证"

```
Phase 1: Requirements (vibe-think)
  Native method: vibe.deep_interview
  Gate: Requirements document approved by user

Phase 2: Architecture (vibe-think)
  Tool: sc:design
  Gate: Architecture diagram approved

Phase 3: Implementation (vibe-do)
  Tool: native serial execution lane (bounded delegated units only when planned)
  Gate: All tests pass, code reviewed

Phase 4: Security Review (vibe-review)
  Tool: everything-claude-code:security-reviewer
  Gate: No CRITICAL findings
```

## Phase B: 计划与设计执行（L 级）

### B1: 需求发现
原生方法：`vibe.deep_interview`
- 歧义阻碍需求质量时提出一个高价值澄清问题
- 选定实现方向之前先比较方案
- 对 L/XL 级工作，先用通俗语言解释 L 与 XL 的区别，然后停下来等用户选级别
- 专家 skill 被推荐之后，询问"我将会在接下来的工作中使用这些 skills，你觉得 OK 吗？"，并在这些 skill 成为执行义务之前停下来
- 输出澄清后的需求、假设、验收标准与用户可见权衡

治理运行时要求：
- 持久化一份可落成 `docs/requirements/` 下文件的意图契约
- 不要把工作流级别确认、skill 使用确认与需求批准合并成一次性的提示

### B2: 架构设计（需要时）
工具：sc:design
- 认知人格（架构师、安全、前端、后端）
- 输出：架构图、组件设计、数据流

### B2 自查（所有设计任务）

通过 `vibe.deep_interview` 或 `sc:design` 生成初始设计之后：
1. 列出该设计在生产环境可能失败的 3 种方式
2. 任一失败模式暗示存在根本不同的方案 → 生成备选方案
3. 备选方案同样可行 → 把两个方案连同权衡对比一起呈现给用户
4. 没有可行备选 → 沿用原方案，并把失败模式记录为风险

注意：用户显式请求辩证智囊团模式时，跳过 B2 自查，改走
team.md 辩证模式。

### B3: 计划文档化
原生方法：`vibe.xl_plan`
- 在 docs/plans/YYYY-MM-DD-<topic>.md 生成计划
- 输出：可执行的分阶段实现计划

治理运行时最低内容：
- 内部级别决策
- 确认的用户可见工作流级别
- 已批准的选定 skill，与最终实际使用证据清晰分开
- 波次或批次结构
- 验证命令
- 回滚规则
- 阶段清理预期

### B4: 深度研究（需要时）
工具：claude-code-settings:deep-research
- 多智能体并行研究工作流
- 输出：带来源的研究发现

### B5: GSD-Lite 预检钩子（可选，仅 L/XL 计划）
策略来源：`config/gsd-overlay.json`

仅当所有条件满足时运行此钩子：
1. `enabled=true` 且 `mode != off`
2. 当前任务类型为 `planning`
3. 当前级别在 `grade_allow` 中（默认：`L`、`XL`）

硬边界：
- 只做路由后治理。绝不重跑级别/任务/pack 路由。
- 不引入 `/gsd:*` 命令流。
- 不创建第二棵真相状态树。

钩子步骤：
1. **棕地上下文快照**（当 `brownfield_context.enabled=true`）
   - 在 `docs/vco-context/` 下建立或刷新轻量快照：
     - `STACK.md`
     - `ARCHITECTURE.md`
     - `CONVENTIONS.md`
     - `CONCERNS.md`
   - 快照缺失或过期时不要静默继续。把运行标记为降级，发出 hazard alert，并在快照修复之前保持结果 non-authoritative。
2. **假设预检**
   - 写最终计划之前产出一份简明的假设清单。
   - 把假设持久化到现行计划产物（配置了 `assumptions.md` 时则写入该文件）。
3. **按模式确认策略**
   - `shadow`：只记录建议，不阻塞。
   - `soft`：只对 `assumption_gate.confirm_required_for` 中的级别要求确认。
   - `strict`：对所有范围内级别都要求确认。
4. **移交**
   - 把假设 + 棕地上下文带进 B3 输出。

钩子失败时不要静默降级。只在显式降级路径下遵循 `references/fallback-chains.md`，发出独立 hazard alert，并记录由此产生的规划流程在主路径恢复之前为 non-authoritative。

## 研究模式
任务纯研究（无实现）时：
1. 范围不清楚否则跳过 B1
2. 直接进入 B4（deep-research）
3. 可选：用 sc:research 做 web 研究
4. 把发现存入 ruflo 记忆（不可用时用 state_store）

## 冲突规避
- 本协议期间不写代码（遵守 HARD-GATE）
- 不要在活跃 `vibe` 会话之外创建第二个需求或计划表面
- 深度分析、方案对比与计划编写都是 `deep_interview` 与 `xl_plan` 内部的原生方法
- 分析（Phase A）在实现开始之前完成，不与执行并行
- superpowers 计划/过程 skill 只做纪律，VCO 产物冻结之后不得创建第二个需求或计划真相
- 任何非治理运行时的规划辅助都必须汇入规范的 `docs/requirements/` 与 `docs/plans/` 表面，而不是另造平行产物

## 转入实现
设计获得批准之后：
1. L 级：切到 vibe-do 串行原生执行（顺序优先；仅在显式计划时才有界委派）
2. XL 级：切到 vibe-team 协议（波次顺序执行 + 步骤级有界并行单元 + 可选 ruflo 协作）
3. 始终把计划文档作为上下文带下去
4. 执行必须移交进运行时第 5 阶段 `plan_execute`，不得直接绕进临时编码
5. 过程纪律辅助可以影响工作如何执行，但 VCO 仍是唯一的治理运行时骨架与产物权威
