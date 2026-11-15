> **中文汉化版** · 上游：[foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) · 原文件：`protocols/retro.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# vibe-retro 协议

> **本协议的作用（通俗概述）**
>
> 这是复盘协议。它定义 VibeSkills 如何审查已完成的工作、识别反复出现的问题，并为你的工作流提出改进。
>
> 使用 VibeSkills 不需要读本文件。它在 `phase_cleanup` 之后激活，用于你想复盘发生了什么、并为下次改进的时候。
>
> **下文用到的关键术语：**
> - **CER（Context Evidence Report，上下文证据报告）**：一种结构化输出格式，描述出了什么问题以及如何预防。结构：Pattern -> Evidence -> Root Cause -> Intervention -> Guardrail -> Confidence。
> - **CF-1 到 CF-6（上下文失败类别）**：
>   CF-1 = 注意力稀释（AI 在长会话中丢失早期上下文）；
>   CF-2 = 上下文污染（过期或矛盾的状态）；
>   CF-3 = 观察膨胀（工具输出挤占有用的上下文 token）；
>   CF-4 = 记忆失配（检索到错误内容）；
>   CF-5 = 工具契约歧义（工具输入/输出预期不匹配）；
>   CF-6 = 评估盲区（没有评分标准或验证薄弱）。
> - **Proxy-goal drift（代理目标漂移）**：系统优化一个可见指标（代理指标）而不是真实目标。例如：删掉失败的测试来让全部测试通过。
> - **report_only**：仅为审查目的记录的警告，其本身不会自动阻塞任何动作。
> - **Context Retro Advisor**：一个顾问性质的子系统，负责对上下文失败分类并推荐干预措施。它可以建议，但未经用户明确批准不能更改配置。


结构化复盘协议：对近期项目做协作分析、优化工作流、检测错误模式、诊断上下文，并规划未来改进。

## 适用范围
当用户想要以下动作时激活：
- 审查并反思近期项目工作
- 识别工作流优化机会
- 检测反复出现的错误模式并设计预防性 Hook
- 诊断长任务中的上下文质量失败
- 发现可复用于未来项目的模式
- 决定是否创建新的 skill、Agent、MCP 或 Hook
- 开展一次协作式改进讨论

## 治理运行时定位

本协议是复盘与学习表面，不是主用户入口。
它可以在治理执行完成之后调用，也可以作为运行时第 6 阶段 `phase_cleanup` 之后清理与学习环节的一部分。

固定的运行时路径保持不变：

1. `skeleton_check`
2. `deep_interview`
3. `requirement_doc`
4. `xl_plan`
5. `plan_execute`
6. `phase_cleanup`

`retro.md` 绝不替代这些阶段。
它消费这些阶段的回执与产物，以改进未来的运行。

## 反代理目标漂移复盘视角

复盘把代理目标漂移当作一等学习失败模式。
目的不是事后惩罚工作。
目的是保住诚实的完成措辞，防止目标/代理指标替换被常态化，并让专门化与虚假泛化保持区分。

在官方 `report_only` 模式下：
- 记录警告代码、完成措辞纠正与专门化发现，
- 不得把这些发现静默转换成新的硬门禁，
- 如果违反了另一个已批准的阻塞策略，直接引用那个策略。

核心复盘问题：
1. 工作声称服务的目标是什么？
2. 实际被优化的是哪些代理信号？
3. 验证材料是否保持在实现真相之外？
4. 修复是否做在预期的抽象层？
5. 最终完成状态对实际范围与证据是否诚实？
6. 有界专门化是被诚实保留，还是被抹平成了泛化声明？

## Context Retro Advisor（Agent-Skills 引导）

VCO 在复盘模式中使用 Agent-Skills-for-Context-Engineering 作为专家顾问。
该顾问只提供指导，绝不自动修改运行时配置。

### 知识来源（优先）
- context-fundamentals
- context-degradation
- context-compression
- context-optimization
- multi-agent-patterns
- memory-systems
- tool-design
- filesystem-context
- evaluation
- advanced-evaluation
- project-development

### 顾问边界
- 顾问可以分类失败模式并推荐干预措施。
- 顾问不能直接更改 router 阈值、pack manifest 或冲突规则。
- 任何配置或策略变更仍需在 Phase 4 获得用户明确批准。

### Skills 缺失时的回退
- 回退到本协议内置的 VCO 启发式。
- 用可用的会话/工具数据继续做有证据支撑的诊断。

## 5 阶段架构

Phase 1: GATHER -> Phase 2: ANALYZE -> Phase 3: DISCUSS -> Phase 4: DECIDE -> Phase 5: ACT

每个阶段使用已集成插件中的现有工具。

---

## Phase 1: GATHER（数据收集）

### 1.1 对话历史检索
工具：Cognee 图检索（可选）+ 会话文件扫描
- 查询长期关系图谱以获取目标项目/主题上下文（如 Cognee 可用）
- 读取近期会话文件获取短期执行轨迹
- 回退：仅用会话文件（VCO 治理模式下不使用 episodic-memory）

### 1.2 会话活动审查
工具：读取 ~/.claude/sessions/ 文件
- 读取近期会话文件
- 提取：执行过的任务、修改过的文件、使用过的工具

### 1.3 Instinct 状态检查
工具：everything-claude-code:instinct-status
- 按领域分组展示已学习的 instinct
- 检查置信分数与近期更新
- 回退：instinct 系统未激活则跳过

### 1.4 项目记忆检索
工具：Serena MCP list_memories + read_memory
- 列出项目相关记忆
- 读取关键决策与架构笔记
- 回退：Serena 不可用则跳过

### 1.5 错误日志收集
工具：git log + 会话/ruflo 轨迹综合
- git log --oneline -20（近期提交，尤其是 fix/revert）
- 在会话轨迹/ruflo 记忆中搜索 error、fix、bug、revert

### 1.6 上下文信号收集
工具：会话/工具轨迹综合
- 统计重试次数、回退频率与 compaction 事件
- 度量大型输出的工具调用与重复的低价值观察
- 检测路由不稳定（同一意图，不同路由结果）
- 收集审查措辞、收尾措辞，以及执行期间发出的任何 report-only 防漂警告

#### 默认触发阈值

除非项目策略定义了更严格的阈值，否则使用以下默认值：

| 信号 | 指标 | 默认阈值 | 触发含义 |
|--------|--------|-------------------|-----------------|
| 重试尖峰 | `retry_count_10m` | `>= 3` | 执行卡在重试循环 |
| 回退频率 | `fallback_rate` | `>= 0.20` | 主路径可靠性下降 |
| 上下文压力 | `context_pressure` | `>= 0.75` | 上下文预算面临风险 |
| 路由不稳定（pack） | `route_stability_pack` | `< 0.80` | 同一意图路由到不同 pack |
| 路由不稳定（skill） | `route_stability_skill` | `< 0.70` | pack 内 skill 选择抖动 |
| 路由歧义 | `top1_top2_gap` | `< 0.03` | 路由可分性弱 |

其中：
- `fallback_rate = fallback_count / total_attempts`
- `context_pressure = observation_chars_total / context_budget_chars`
- `route_stability_pack = most_common_pack / total_probe_runs`
- `route_stability_skill = most_common_skill / total_probe_runs`

继续之前先呈现结构化的数据收集报告。

---

## Phase 2: ANALYZE（结构化分析）

### 2.1 会话反思
工具：claude-code-settings:reflection-harder（或 everything-claude-code:deep-reflector agent）
回退：claude-code-settings:think-harder
- 分析近期会话中解决了哪些问题、形成了哪些模式

### 2.2 问题模式检测
工具：hookify:conversation-analyzer agent
回退：人工扫描会话轨迹与提交历史
- 扫描用户挫败信号、重复错误、工具误用
- 严重度分级（high/medium/low）

### 2.3 工作流频率分析
工具：分析会话文件 + ruflo 短期记忆
- 最常用的工具组合
- 重复的多步工作流（自动化候选）

### 2.4 跨会话趋势分析
工具：claude-code-settings:think-ultra（7 阶段分析），M 级用 think-harder（4 阶段）
回退：Claude 直接推理综合
- 综合 2.1-2.3 的数据
- 错误趋势、活动领域、时间黑洞

### 2.5 上下文失败分型（Context Retro Advisor）
把失败归入一个或多个类别：
- CF-1 注意力稀释 / lost-in-middle
- CF-2 上下文污染（过期或矛盾状态）
- CF-3 观察膨胀（工具输出挤占有用 token）
- CF-4 记忆失配（检索不相关/缺失）
- CF-5 工具契约歧义（工具 schema/意图不匹配）
- CF-6 评估盲区（无评分标准，验证薄弱）

### 2.6 干预设计
把每个失败类别映射到干预措施：
- 更新 compaction 策略（压缩什么、何时压缩）
- 观察掩蔽规则（保留什么、引用什么）
- XL 任务的上下文分区（细化 Agent 边界）
- 调整记忆索引/持久化策略
- 强化评估评分标准与验证门禁

### 2.7 防漂分类
治理复盘还要分类本次运行是否出现：
- 目标/代理指标替换，
- 验证材料污染，
- 抽象层错配，
- 完成状态过度声明，
- 专门化被抹除。

每项分类必须以以下处置之一收尾：
- `aligned`
- `report_only_warning`
- `completion_language_corrected`
- `specialization_confirmed`
- `escalate_via_existing_policy`

---

## Phase 3: DISCUSS（交互式讨论）

### 交互风格：教学式顾问

**主动介入：**
- 主动识别改进机会
- 用引导性问题带出洞察
- 对每项发现给出具体改进路径

**数据支撑的建议：**
- 每条建议都引用 Phase 2 中的具体证据
- 不确定时明确承认不确定性

**讨论主题：**
- 工作流审查：自动化候选、效率改进
- 错误预防：Hook、pre-commit 检查
- 上下文质量：压缩策略、掩蔽策略、分区策略
- 工具有效性：路由准确度、回退频率
- 未来规划：模板、skill、新工具
- 完成诚实度：报告的最终状态是否与目标、范围和证明相符
- 专门化边界：有界成果是被诚实保留，还是被习惯性泛化

**尊重自主权：**
- 所有最终决定由用户做出
- Phase 4 之前显式请求确认

---

## Phase 4: DECIDE（决策）

### 决策类别

| 类别 | 动作类型 | 工具 |
|----------|------------|------|
| 重复性工作流 | 创建 skill | superpowers:writing-skills |
| 重复性工作流 | 创建命令 | claude-code-settings:command-creator |
| 错误预防 | 创建 Hook | hookify:hookify |
| 行为模式 | 创建/更新 instinct | continuous-learning-v2 |
| 上下文质量 | 更新复盘策略/手册 | 编辑 protocols/retro.md + docs |
| 完成诚实度纠正 | 更新审查 / CER / 收尾措辞 | 编辑 protocols/templates/docs |
| 路由改进 | 更新 VCO 配置 | 编辑 SKILL.md / config/*.json |
| 知识沉淀 | 持久化记忆 | Serena write_memory + Cognee ingest（可选） |
| 复杂自动化 | 创建 Agent | 人工设计 + writing-skills |

### 用户确认门
以优先级列表呈现全部决策。
Phase 5 之前，用户逐项批准、修改或拒绝。

---

## Phase 5: ACT（执行改进）

### 5.1 创建 Hook
工具：hookify:hookify
- 定义触发器、匹配器、动作
- 创建 .local.md 规则文件

### 5.2 创建 Skill/命令
工具：superpowers:writing-skills 或 claude-code-settings:command-creator
- 定义 skill 名称、描述、触发器
- 写出带正确 frontmatter 的 SKILL.md

### 5.3 创建/更新 Instinct
工具：everything-claude-code:continuous-learning-v2
- 在 ~/.claude/homunculus/instincts/personal/ 创建 .md
- 设置置信分数（从 0.5 起步）

### 5.4 更新 VCO 配置
工具：直接编辑 SKILL.md、conflict-rules.md、fallback-chains.md、router 配置文件

### 5.5 沉淀知识
工具：Serena write_memory + Cognee ingest（可选）+ 全局适用时更新 CLAUDE.md
- Serena：只持久化明确的项目决策
- Cognee：持久化长期实体/关系以供跨会话检索

### 5.6 生成 CER 报告（Markdown + JSON）
用模板生成两份产物：
- `templates/cer-report.md.template`
- `templates/cer-report.json.template`

输出存放于：
- `outputs/retro/YYYY-MM-DD-<topic>-cer.md`
- `outputs/retro/YYYY-MM-DD-<topic>-cer.json`

### 5.7 持久化 CER 以便对比
通过 Serena write_memory 存储摘要：
- key: `retro/YYYY-MM-DD/<topic>/cer-summary`
- 包含：失败类别、关键干预、护栏、置信度

可选：把完整 JSON 留在本地产物库中以做趋势分析。

### 5.8 更新上下文手册（可选）
接受了策略级变更时，更新 docs/design/context-retro-advisor-design.md。

### 5.9 运行复盘回归检查（可选但推荐）
工具：`scripts/verify/vibe-retro-context-regression-matrix.ps1`
- 用固定指标用例验证触发阈值逻辑
- 用双语固定证据用例验证 CF-1..CF-6 分型稳定性

### 5.10 跨迭代对比 CER（可选但推荐）
工具：`scripts/verify/cer-compare.ps1`
- 对比基线与当前 CER JSON 报告
- 输出机器可读与人类可读的差异摘要
- 跟踪趋势字段：pattern delta、fallback_rate delta、stability delta、context_pressure delta

---

## 上下文证据报告（CER）输出契约

每次 Context Retro Advisor 分析必须输出以下模式：

1. Pattern：失败类别标签（CF-1..CF-6）
2. Evidence：具体观察（命令、输出、事件）
3. Root Cause：模式为何发生
4. Intervention：具体变更提案
5. Guardrail：防止复发的验证检查
6. Confidence：high/medium/low 并附范围限制

没有 Evidence 就不得发出任何建议。

每份治理 CER 还应保留共享的防漂词汇：
- `governance_mode`
- `anti_proxy_goal_drift_tier`
- `completion_state`
- `primary_objective`
- `non_objective_proxy_signals`
- `validation_material_role`
- `intended_scope`
- `specialization_assessment`
- `generalization_evidence_bundle`
- `report_only_warning_codes`
- `completion_honesty_notes`

`report_only_warning_codes` 是治理证据，不是隐藏的硬停止。
如果复盘建议采取阻塞动作，必须指名那个支持阻塞的独立已批准策略或硬门禁。

### CER JSON 校验
- 可用时，用 `templates/cer-report.schema.json` 校验生成的 JSON。
- schema 校验失败时，把报告状态标记为 `invalid`，且不得用于趋势对比。

---

## 工具组合地图

| 阶段 | 主工具 | 来源插件 | 回退 |
|-------|-------------|--------------|----------|
| 1.1 历史 | Cognee 图检索 + 会话文件 | Cognee + runtime | 读取会话文件 |
| 1.2 活动 | 读取 ~/.claude/sessions/ | Everything-CC | git log |
| 1.3 Instinct | instinct-status | Everything-CC | 跳过 |
| 1.4 记忆 | Serena list/read_memory | Serena MCP | 跳过 |
| 1.5 错误 | git log + 会话/ruflo 轨迹搜索 | Git + ruflo | 人工审查 |
| 1.6 上下文信号 | 会话/工具轨迹综合 | Runtime-neutral | 人工综合 |
| 2.1 反思 | reflection-harder | Claude-code-settings | deep-reflector agent / think-harder |
| 2.2 问题 | conversation-analyzer | Hookify | 人工扫描 |
| 2.3 工作流 | 会话文件 + ruflo 分析 | Everything-CC + ruflo | 仅会话分析 |
| 2.4 趋势 | think-ultra / think-harder | Claude-code-settings | 直接推理 |
| 2.5 上下文分型 | Agent-Skills context guidance | Agent-Skills | VCO 启发式 |
| 3.x 讨论 | 头脑风暴方法论 | Superpowers | 直接对话 |
| 4.x 决策 | user_confirm 接口 | Runtime-neutral | 直接对话 |
| 5.1 Hook | hookify | Hookify | 人工创建 |
| 5.2 Skill | writing-skills | Superpowers | 人工创建 |
| 5.3 Instinct | continuous-learning-v2 | Everything-CC | 人工创建 |
| 5.4 配置 | 直接编辑 | VCO | 人工编辑 |
| 5.5 知识 | Serena write_memory + Cognee ingest | Serena MCP + Cognee | state_store 决策日志 |
| 5.6 CER 输出 | CER 模板 | VCO templates | 人工结构 |
| 5.9 回归检查 | vibe-retro-context-regression-matrix.ps1 | VCO verify | 人工清单 |
| 5.10 CER 对比 | cer-compare.ps1 | VCO verify | 人工对比 |

---

## 级别适配

| 级别 | 范围 | 使用阶段 | 深度 |
|-------|-------|-------------|-------|
| M | 单项目复盘 | 1 + 2 + 3 + 4 | 完整分析，选择性执行 |
| L | 多项目复盘 | 全部 5 个阶段 | 完整分析 + 实施 |
| XL | 全系统复盘 | 全部 5 个 + 并行 Agent | 深度分析 + 重大变更 |

## 冲突规避
- Phase 2 分析 Agent 顺序运行以避免互斥。
- 例外：XL 级用 Codex 原生团队做并行分析。
- hookify conversation-analyzer 是分析工具，任何级别都安全。
- deep-reflector 是诊断 Agent，不受规则 1 约束。
- Context Retro Advisor 是顾问性质，可在任何级别运行。
- Phase 5 动作按顺序执行：先 Hook，再 skill，最后配置。
- router 或阈值变更需要用户显式确认。
