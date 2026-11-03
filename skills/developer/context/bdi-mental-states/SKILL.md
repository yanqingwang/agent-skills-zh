---
name: bdi-mental-states
description: "本 Skill 用于以 BDI 概念对 Agent 心理状态建模：信念（beliefs）、愿望（desires）、意图（intentions）、RDF 到信念的转换、理性行为轨迹、认知 Agent、BDI 本体（ontology），以及神经符号 AI 集成。"
---

> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/bdi-mental-states/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# BDI 心理状态建模

使用形式化的 BDI 本体（ontology）模式，把外部 RDF 上下文转换为 Agent 心理状态（信念 beliefs、愿望 desires、意图 intentions）。本 Skill 让 Agent 能够通过认知架构对上下文进行推理，支持慎思推理（deliberative reasoning）、可解释性以及多代理系统内的语义互操作。

## 何时启用

在以下情况启用本 Skill：

- 将外部 RDF 上下文处理为 Agent 关于世界状态的信念
- 以感知、慎思、行动循环对理性行为（rational agency）建模
- 通过可追溯的推理链实现可解释性
- 实现 BDI 框架（SEMAS、JADE、JADEX）
- 用形式化认知结构增强 LLM（逻辑增强生成，Logic Augmented Generation）
- 跨多代理平台协调心理状态
- 追踪信念、愿望与意图的时间演化
- 把动机状态与行动计划关联起来

以下属于其他 Skill 负责的相邻工作，不要启用本 Skill：

- 一般性的 context window 解释或注意力机制：`context-fundamentals`。
- 不含形式化 BDI 状态的持久用户、实体或会话记忆：`memory-systems`。
- 监督者、swarm 或交接拓扑决策：`multi-agent-patterns`。
- 一般性的 Agent 评估标准或质量门：`evaluation`。

## 核心概念

### 心理实在架构（Mental Reality Architecture）

把心理状态划分为两个本体论范畴，因为 BDI 推理需要区分什么是持续存在的、什么是发生的：

**心理状态（Endurants，持续体）**——将其建模为在时间区间上持续成立的持久认知属性：

- `Belief`：表示 Agent 认定为真的世界情况。每条信念都要锚定到一个世界状态引用上。
- `Desire`：表示 Agent 希望促成的状态。把每条愿望回链到激发它的信念上。
- `Intention`：表示 Agent 承诺要实现的目标。意图必须满足一条愿望并指定一个计划。

**心理过程（Perdurants，时存过程）**——将其建模为创建或修改心理状态的事件，因为追踪因果转换才能实现可解释性：

- `BeliefProcess`：由感知触发信念的形成/更新。始终连接到产生它的世界状态。
- `DesireProcess`：从既有信念生成愿望。保持动机链完整。
- `IntentionProcess`：把选定的愿望承诺为可执行的意图。

### 认知链模式（Cognitive Chain Pattern）

使用双向属性对（`motivates`/`isMotivatedBy`、`fulfils`/`isFulfilledBy`）把信念、愿望和意图接成有向链，因为这同时支持前向推理（Agent 应该做什么？）与反向追溯（Agent 为什么这样做？）：

```turtle
:Belief_store_open a bdi:Belief ;
    rdfs:comment "Store is open" ;
    bdi:motivates :Desire_buy_groceries .

:Desire_buy_groceries a bdi:Desire ;
    rdfs:comment "I desire to buy groceries" ;
    bdi:isMotivatedBy :Belief_store_open .

:Intention_go_shopping a bdi:Intention ;
    rdfs:comment "I will buy groceries" ;
    bdi:fulfils :Desire_buy_groceries ;
    bdi:isSupportedBy :Belief_store_open ;
    bdi:specifies :Plan_shopping .
```

### 世界状态锚定（World State Grounding）

始终把心理状态锚定（ground）在世界状态引用上，而不是自由文本描述，因为未锚定的信念会破坏语义查询与跨 Agent 互操作：

```turtle
:Agent_A a bdi:Agent ;
    bdi:perceives :WorldState_WS1 ;
    bdi:hasMentalState :Belief_B1 .

:WorldState_WS1 a bdi:WorldState ;
    rdfs:comment "Meeting scheduled at 10am in Room 5" ;
    bdi:atTime :TimeInstant_10am .

:Belief_B1 a bdi:Belief ;
    bdi:refersTo :WorldState_WS1 .
```

### 目标导向规划（Goal-Directed Planning）

通过 `bdi:specifies` 把意图连接到计划，并用 `bdi:precedes` 把计划分解为有序的任务序列，因为这种分离让计划可以在不同意图间复用，同时保持执行顺序显式可见：

```turtle
:Intention_I1 bdi:specifies :Plan_P1 .

:Plan_P1 a bdi:Plan ;
    bdi:addresses :Goal_G1 ;
    bdi:beginsWith :Task_T1 ;
    bdi:endsWith :Task_T3 .

:Task_T1 bdi:precedes :Task_T2 .
:Task_T2 bdi:precedes :Task_T3 .
```

### T2B2T 范式

将 T2B2T（Triples-to-Beliefs-to-Triples，三元组→信念→三元组）实现为双向管线，因为 Agent 既要消费外部 RDF 上下文，也要产出新的 RDF 断言。每个 T2B2T 实现都组织为两个显式阶段：

**阶段 1：三元组到信念（Triples-to-Beliefs）**——把传入的 RDF 三元组转换为信念实例。用 `bdi:triggers` 把外部世界状态连接到 `BeliefProcess`，用 `bdi:generates` 产出最终的信念。这保留了从源数据到内部认知的出处（provenance）：

```turtle
:WorldState_notification a bdi:WorldState ;
    rdfs:comment "Push notification: Payment request $250" ;
    bdi:triggers :BeliefProcess_BP1 .

:BeliefProcess_BP1 a bdi:BeliefProcess ;
    bdi:generates :Belief_payment_request .
```

**阶段 2：信念到三元组（Beliefs-to-Triples）**——在 BDI 慎思选定意图并执行计划之后，用 `bdi:bringsAbout` 把结果投影回 RDF。这闭合了循环，使下游系统可以把 Agent 输出作为标准关联数据（linked data）消费：

```turtle
:Intention_pay a bdi:Intention ;
    bdi:specifies :Plan_payment .

:PlanExecution_PE1 a bdi:PlanExecution ;
    bdi:satisfies :Plan_payment ;
    bdi:bringsAbout :WorldState_payment_complete .
```

### 按层级选择表示法（Notation Selection by Level）

根据所建模的 C4 抽象层级选择表示法，因为在错误的层级混用表示法只会模糊而非澄清认知架构：

| C4 层级 | 表示法 | 心理状态表示 |
|----------|----------|----------------------------|
| L1 Context | ArchiMate | Agent 边界、外部感知来源 |
| L2 Container | ArchiMate | BDI 推理引擎、信念库、计划执行器 |
| L3 Component | UML | 心理状态管理器、过程处理器 |
| L4 Code | UML/RDF | Belief/Desire/Intention 类、本体实例 |

### 论证与可解释性（Justification and Explainability）

用 `bdi:isJustifiedBy` 为每个心理实体附加 `bdi:Justification` 实例，因为缺乏论证的心理状态让 Agent 推理变得不透明、不可追溯。每个论证都应记录产生该心理状态的证据或规则：

```turtle
:Belief_B1 a bdi:Belief ;
    bdi:isJustifiedBy :Justification_J1 .

:Justification_J1 a bdi:Justification ;
    rdfs:comment "Official announcement received via email" .

:Intention_I1 a bdi:Intention ;
    bdi:isJustifiedBy :Justification_J2 .

:Justification_J2 a bdi:Justification ;
    rdfs:comment "Location precondition satisfied" .
```

### 时间维度（Temporal Dimensions）

用 `bdi:hasValidity` 搭配 `TimeInterval` 实例为每个心理状态指定有效区间，因为没有时间边界的信念在历时推理（diachronic reasoning）中既无法被垃圾回收，也无法做冲突检查：

```turtle
:Belief_B1 a bdi:Belief ;
    bdi:hasValidity :TimeInterval_TI1 .

:TimeInterval_TI1 a bdi:TimeInterval ;
    bdi:hasStartTime :TimeInstant_9am ;
    bdi:hasEndTime :TimeInstant_11am .
```

使用 SPARQL 时间过滤器查询在特定时刻处于活跃状态的心理状态。当关于同一世界状态的多条信念在时间上重叠时，用此模式化解冲突：

```sparql
SELECT ?mentalState WHERE {
    ?mentalState bdi:hasValidity ?interval .
    ?interval bdi:hasStartTime ?start ;
              bdi:hasEndTime ?end .
    FILTER(?start <= "2025-01-04T10:00:00"^^xsd:dateTime &&
           ?end >= "2025-01-04T10:00:00"^^xsd:dateTime)
}
```

### 可组合的心理实体（Compositional Mental Entities）

用 `bdi:hasPart` 关系把复杂信念分解为组成部分，因为单体式信念在部分更新时会被迫整体替换。构造复合信念时，让每个子信念都可以被独立更新、查询或置为失效：

```turtle
:Belief_meeting a bdi:Belief ;
    rdfs:comment "Meeting at 10am in Room 5" ;
    bdi:hasPart :Belief_meeting_time , :Belief_meeting_location .

# Update only location component without touching time
:BeliefProcess_update a bdi:BeliefProcess ;
    bdi:modifies :Belief_meeting_location .
```

## 实用指南

### 六步构建 BDI 模型

把外部语义上下文转换为 BDI 表示时，使用以下工作流：

1. **定义世界状态基底**：识别 Agent 可感知的外部事实或事件。在创建信念之前，先把它们建模为世界状态。
2. **创建信念实例**：把每个相关的世界状态转换为一条带出处、时间有效性与论证引用的信念。
3. **从信念推导愿望**：只有当某条信念产生了与目标相关的动机时才添加愿望。把每条愿望回链到激发它的信念。
4. **审慎承诺意图**：只有当 Agent 承诺了某个计划时，才把愿望提升为意图。记录所选计划与前置条件。
5. **把行动结果投影回三元组**：执行完成后，把产生的世界状态以 RDF 发出，让下游系统能消费新状态。
6. **用能力问题（competency questions）验证**：在信任模型之前，先针对出处、动机、计划序列与活跃有效时间窗做查询验证。

### 保持本体精简（Keep the Ontology Small）

从 `Agent`、`WorldState`、`Belief`、`Desire`、`Intention`、`Plan`、`Task`、`Justification` 和 `TimeInterval` 起步。只有当能力问题证明核心模型无法回答所需查询时，才添加专门的类。精简的本体更容易序列化进提示词、更容易验证，也不容易产生脆弱的推理链。

### 只在心理状态语义真正重要时使用 BDI（Use BDI Only When Mental-State Semantics Matter）

当系统需要可解释的主体行为时，BDI 建模才有价值：Agent 为什么相信某事、该信念催生了什么愿望、选定了哪个意图、执行了什么计划。如果系统只需要跨会话记住事实，用 `memory-systems`。如果只需要在 Agent 之间拆分工作，用 `multi-agent-patterns`。

## 详细主题

### 集成模式（Integration Patterns）

### 逻辑增强生成（LAG，Logic Augmented Generation）

使用 LAG 以本体结构约束 LLM 输出，因为不受约束的生成会产出违反 BDI 类约束的三元组。把本体序列化进提示词上下文，在接受生成的三元组之前先对照本体校验：

```python
def augment_llm_with_bdi_ontology(prompt, ontology_graph):
    ontology_context = serialize_ontology(ontology_graph, format='turtle')
    augmented_prompt = f"{ontology_context}\n\n{prompt}"

    response = llm.generate(augmented_prompt)
    triples = extract_rdf_triples(response)

    is_consistent = validate_triples(triples, ontology_graph)
    return triples if is_consistent else retry_with_feedback()
```

### SEMAS 规则翻译（SEMAS Rule Translation）

部署到基于规则的代理平台时，把 BDI 本体模式翻译为可执行的产生式规则。把认知链的每一环（信念到愿望、愿望到意图）映射为一条 HEAD/CONDITIONALS/TAIL 规则，因为这既保留慎思语义，又支持运行时执行：

```prolog
% Belief triggers desire formation
[HEAD: belief(agent_a, store_open)] /
[CONDITIONALS: time(weekday_afternoon)] »
[TAIL: generate_desire(agent_a, buy_groceries)].

% Desire triggers intention commitment
[HEAD: desire(agent_a, buy_groceries)] /
[CONDITIONALS: belief(agent_a, has_shopping_list)] »
[TAIL: commit_intention(agent_a, buy_groceries)].
```

## 准则

1. 将世界状态建模为独立于 Agent 视角的配置，为心理状态提供引用基底。

2. 区分持续体（endurants，持续存在的心理状态）与时存过程（perdurants，时间性的心理过程），与 DOLCE 本体保持一致。

3. 将目标视为描述（description）而非心理状态，保持认知层与规划层的分离。

4. 使用 `hasPart` 关系表达部分-整体（meronymic）结构，以支持选择性信念更新。

5. 通过 `atTime` 或 `hasValidity` 把每个心理实体与时间构造关联。

6. 使用双向属性对（`motivates`/`isMotivatedBy`、`generates`/`isGeneratedBy`）以便灵活查询。

7. 把心理实体链接到 `Justification` 实例，以获得可解释性与可信度。

8. 通过以下步骤实现 T2B2T：（1）把 RDF 转换为信念，（2）执行 BDI 推理，（3）把心理状态投影回 RDF。

9. 为心理过程定义存在限制（existential restrictions），例如 `BeliefProcess ⊑ ∃generates.Belief`。

10. 复用既有的 ODP（本体设计模式：EventCore、Situation、TimeIndexedSituation、BasicPlan、Provenance）以保证互操作性。

## 能力问题（Competency Questions）

用以下 SPARQL 查询验证实现：

```sparql
# CQ1: What beliefs motivated formation of a given desire?
SELECT ?belief WHERE {
    :Desire_D1 bdi:isMotivatedBy ?belief .
}

# CQ2: Which desire does a particular intention fulfill?
SELECT ?desire WHERE {
    :Intention_I1 bdi:fulfils ?desire .
}

# CQ3: Which mental process generated a belief?
SELECT ?process WHERE {
    ?process bdi:generates :Belief_B1 .
}

# CQ4: What is the ordered sequence of tasks in a plan?
SELECT ?task ?nextTask WHERE {
    :Plan_P1 bdi:hasComponent ?task .
    OPTIONAL { ?task bdi:precedes ?nextTask }
} ORDER BY ?task
```

## 示例

**示例 1：RDF 通知到 BDI 链**

输入的世界状态：

```turtle
:WorldState_invoice_due a bdi:WorldState ;
    rdfs:comment "Invoice INV-42 is due tomorrow" ;
    bdi:atTime :Time_2026_05_15 .
```

BDI 投影：

```turtle
:Belief_invoice_due a bdi:Belief ;
    bdi:refersTo :WorldState_invoice_due ;
    bdi:isJustifiedBy :Justification_billing_system ;
    bdi:motivates :Desire_avoid_late_fee .

:Desire_avoid_late_fee a bdi:Desire ;
    bdi:isMotivatedBy :Belief_invoice_due .

:Intention_pay_invoice a bdi:Intention ;
    bdi:fulfils :Desire_avoid_late_fee ;
    bdi:specifies :Plan_pay_invoice .
```

**示例 2：边界决策**

如果任务是"记住 Alice 偏好简洁摘要"，用 `memory-systems`。如果任务是"表示 Agent 为什么相信 Alice 需要摘要、这催生了什么目标、它承诺了哪个计划"，用本 Skill。

## 常见陷阱

1. **把心理状态与世界状态混为一谈**：心理状态通过 `bdi:refersTo` 引用世界状态，其本身并不是世界状态。混淆二者会坍塌感知-认知边界，并破坏按类型过滤的 SPARQL 查询。

2. **缺失时间边界**：每个心理状态都需要有效区间才能进行历时推理。没有它们，过期信念会无限期存留，冲突检测也无从谈起。

3. **扁平的信念结构**：对复杂信念使用基于 `hasPart` 的组合建模。单体式信念在某一个属性变化时会被迫整体替换。

4. **隐式论证**：始终把心理实体链接到显式的 `Justification` 实例。缺乏论证的心理状态无法审计、无法追溯。

5. **意图直接映射到行动**：意图指定计划，计划包含任务；行动执行任务。跳过计划层会失去复用、重排或共享执行策略的能力。

6. **本体过度复杂**：从 5-10 个核心类和属性起步（Belief、Desire、Intention、WorldState、Plan，加上关键关系）。过早扩张本体只会膨胀提示词上下文、拖慢 SPARQL 查询，并不会提升推理质量。

7. **推理成本爆炸**：把信念链控制在 3 层以内（信念 -> 愿望 -> 意图）。更深的链对 LLM 推理来说成本高得离谱，而且相比更浅的方案很少改善决策质量。

## 集成

本 Skill 负责形式化心理状态建模。相邻 Skill 负责不同的层：

- `memory-systems`：不带 BDI 信念/愿望/意图语义的持久事实、实体记忆与时间性知识图谱。
- `multi-agent-patterns`：代理拓扑、交接协议与 Agent 间协调。
- `evaluation`：BDI 实现的能力问题、回归检查与质量门。
- `context-fundamentals`：为提示词构建提供依据的 context window 与注意力机制的概念性解释。
- `tool-design`：BDI 查询、校验或投影工具的 schema 与工具契约。

## 参考资料

内部参考：

- [BDI 本体核心](./references/bdi-ontology-core.md) - 阅读时机：实现 BDI 类层次结构或从零定义本体属性时
- [RDF 示例](./references/rdf-examples.md) - 阅读时机：编写心理状态的 Turtle 序列化或调试三元组结构时
- [SPARQL 能力查询](./references/sparql-competency.md) - 阅读时机：用能力问题验证实现或构建自定义查询时
- [框架集成](./references/framework-integration.md) - 阅读时机：把 BDI 模型部署到 SEMAS、JADE 或 LAG 管线时

主要来源：

- Zuppiroli et al. "The Belief-Desire-Intention Ontology" (2025) — 阅读时机：实现形式化 BDI 类层次结构或验证本体对齐时
- Rao & Georgeff "BDI agents: From theory to practice" (1995) — 阅读时机：理解实用推理 Agent 的理论基础时
- Bratman "Intention, plans, and practical reason" (1987) — 阅读时机：为实现决策寻找意向性（intentionality）的哲学依据时

---

## Skill 元数据

**创建**：2026-01-07
**最后更新**：2026-05-15
**作者**：Agent Skills for Context Engineering Contributors
**版本**：2.1.0
