> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/bdi-mental-states/references/bdi-ontology-core.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# BDI 本体核心模式

用于"信念-愿望-意图"（Belief-Desire-Intention）心智状态建模的核心本体设计模式。

## 类层次结构

### 心智实体（Endurants，持续体）

```
bdi:MentalEntity
├── bdi:Belief          # Informational dimension
├── bdi:Desire          # Motivational dimension  
├── bdi:Intention       # Deliberative dimension
├── bdi:Goal            # Description of desired end state
└── bdi:Plan            # Structured action sequence
```

### 心智过程（Perdurants，持久过程）

```
bdi:MentalProcess
├── bdi:BeliefProcess      # Forms/updates beliefs from perception
├── bdi:DesireProcess      # Generates desires from beliefs
├── bdi:IntentionProcess   # Commits to desires as intentions
├── bdi:Planning           # Transforms intentions into plans
└── bdi:PlanExecution      # Executes plan actions
```

### 辅助实体

```
bdi:WorldState        # Configuration of environment
bdi:Justification     # Evidential basis for mental states
bdi:Task              # Atomic unit of planned action
bdi:Action            # Execution of a task
bdi:TimeInterval      # Temporal validity bounds
bdi:TimeInstant       # Point in time reference
```

## 对象属性

### 动机关系

| 属性 | 定义域 | 值域 | 描述 |
|----------|--------|-------|-------------|
| `motivates` | Belief | Desire | 信念为愿望提供理由 |
| `isMotivatedBy` | Desire | Belief | motivates 的逆 |
| `fulfils` | Intention | Desire | 意图承诺实现该愿望 |
| `isFulfilledBy` | Desire | Intention | fulfils 的逆 |
| `isSupportedBy` | Intention | Belief | 支撑意图可行性的信念 |

### 生成关系

| 属性 | 定义域 | 值域 | 描述 |
|----------|--------|-------|-------------|
| `generates` | MentalProcess | MentalEntity | 过程创造出心智状态 |
| `isGeneratedBy` | MentalEntity | MentalProcess | generates 的逆 |
| `modifies` | MentalProcess | MentalEntity | 过程更新既有状态 |
| `suppresses` | MentalProcess | MentalEntity | 过程使状态失效 |
| `isTriggeredBy` | MentalProcess | MentalEntity | 状态触发过程 |

### 指称关系

| 属性 | 定义域 | 值域 | 描述 |
|----------|--------|-------|-------------|
| `refersTo` | MentalEntity | WorldState | 关于世界的心智状态 |
| `perceives` | Agent | WorldState | Agent 观察世界 |
| `bringsAbout` | Action | WorldState | 动作引发世界变化 |
| `reasonsUpon` | MentalProcess | MentalEntity | 推理所依据的输入 |

### 结构关系

| 属性 | 定义域 | 值域 | 描述 |
|----------|--------|-------|-------------|
| `hasPart` | MentalEntity | MentalEntity | 部分-整体构成 |
| `specifies` | Intention | Plan | 意图定义计划 |
| `addresses` | Plan | Goal | 计划达成目标 |
| `hasComponent` | Plan | Task | 计划包含任务 |
| `precedes` | Task | Task | 任务排序 |

### 时间关系

| 属性 | 定义域 | 值域 | 描述 |
|----------|--------|-------|-------------|
| `atTime` | Entity | TimeInstant | 时间点上的发生 |
| `hasValidity` | MentalEntity | TimeInterval | 持续存在的时间界 |
| `hasStartTime` | TimeInterval | TimeInstant | 区间起点 |
| `hasEndTime` | TimeInterval | TimeInstant | 区间终点 |

### 证成关系

| 属性 | 定义域 | 值域 | 描述 |
|----------|--------|-------|-------------|
| `isJustifiedBy` | MentalEntity | Justification | 证据支撑 |
| `justifies` | Justification | MentalEntity | 逆关系 |

## 本体约束

### Belief 的约束

```turtle
bdi:Belief rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty bdi:refersTo ;
    owl:someValuesFrom bdi:WorldState
] .

bdi:Belief rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty bdi:hasValidity ;
    owl:maxCardinality 1
] .
```

### Desire 的约束

```turtle
bdi:Desire rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty bdi:isMotivatedBy ;
    owl:someValuesFrom bdi:Belief
] .
```

### Intention 的约束

```turtle
bdi:Intention rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty bdi:fulfils ;
    owl:cardinality 1
] .

bdi:Intention rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty bdi:isSupportedBy ;
    owl:someValuesFrom bdi:Belief
] .
```

### 心智过程的约束

```turtle
bdi:BeliefProcess rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty bdi:generates ;
    owl:allValuesFrom bdi:Belief
] .

bdi:DesireProcess rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty bdi:generates ;
    owl:allValuesFrom bdi:Desire
] .

bdi:IntentionProcess rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty bdi:generates ;
    owl:allValuesFrom bdi:Intention
] .
```

## 与 DOLCE 对齐

BDI 本体与 DOLCE Ultra Lite（DUL）基础本体对齐：

| BDI 类 | DUL 超类 | 理由 |
|-----------|----------------|-----------|
| `Agent` | `dul:Agent` | 能够行动的意向性实体 |
| `Belief` | `dul:InformationObject` | 承载信息的实体 |
| `Desire` | `dul:Description` | 描述期望的状态 |
| `Intention` | `dul:Description` | 描述已承诺的行动路线 |
| `Goal` | `dul:Goal` | 期望终态的描述 |
| `Plan` | `dul:Plan` | 有组织的行动序列 |
| `WorldState` | `dul:Situation` | 实体的配置 |
| `MentalProcess` | `dul:Event` | 在时间中延展的发生 |
| `Task` | `dul:Task` | 计划中的工作单元 |
| `Action` | `dul:Action` | 已执行的任务实例 |

## 复用的本体设计模式

### EventCore 模式
用于具有时间维度和参与者角色的心智过程。

### Situation 模式
用于心智状态所指涉的世界状态配置。

### TimeIndexedSituation 模式
用于把心智状态与有效期区间关联起来。

### BasicPlan 模式
用于把意图连接到动作的"目标-计划-任务"结构。

### Provenance 模式
用于证成（justification）追踪与证据链。

## 命名空间声明

```turtle
@prefix bdi: <https://w3id.org/fossr/ontology/bdi/> .
@prefix dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```
