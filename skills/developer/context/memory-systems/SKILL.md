---
name: memory-systems
description: "本 Skill 用于 Agent 系统中的持久化语义记忆：跨会话知识留存、实体追踪、时间有效性、图或向量检索、记忆整合，以及记忆基准选型。文件支撑的 scratchpad 路由到 filesystem-context，交接摘要路由到 context-compression，token 效率战术路由到 context-optimization。"
---

> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/memory-systems/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 记忆系统设计

记忆为 Agent 提供持久化层，使其能够跨会话保持连续性，并对积累的知识进行推理。简单的 Agent 完全依赖上下文充当记忆，会话结束即丢失全部状态。成熟的 Agent 则实现分层记忆架构，在即时上下文需求与长期知识留存之间取得平衡。从向量存储到知识图谱、再到时序知识图谱的演进，代表着为提升检索与推理而对结构化记忆不断加大的投入。

## 何时启用

在以下情况启用本 Skill：
- 构建必须跨会话持久化知识的 Agent
- 在多个记忆框架（Mem0、Zep/Graphiti、Letta、LangMem、Cognee）之间做选型
- 需要在多次对话间保持实体一致性
- 实现对积累知识的推理
- 设计能在生产环境中扩展的记忆架构
- 用基准（LoCoMo、LongMemEval、DMR）评估记忆系统
- 构建具备自动实体/关系抽取与自我改进能力的动态记忆（Cognee）

以下属于其他 Skill 负责的相邻工作，不要启用本 Skill：
- 文件支撑的 scratchpad、运行日志与工具输出卸载：`filesystem-context`。
- 对话压缩整理（compaction）或人类可读的交接摘要：`context-compression`。
- 单条轨迹内的掩码、前缀缓存、token 预算或检索范围限定：`context-optimization`。
- 基于 RDF 状态的形式化信念/愿望/意图模型：`bdi-mental-states`。

## 核心概念

把记忆看作从易失的 context window 到持久化存储的一条光谱。默认选择满足检索需求的最简单一层，因为基准证据表明，对某些记忆工作负载而言，工具复杂度的重要性不及可靠检索（claim-memory-locomo-filesystem-baseline）。只有当检索质量退化，或 Agent 需要多跳推理、关系遍历或时间回溯（time-travel）查询时，才增加结构（图、时间有效性）。

## 详细主题

### 生产框架全景

根据 Agent 所需的主导检索模式来选择框架。先用下表缩小候选名单，再用下文的基准数据验证。

| 框架 | 架构 | 最适合 | 权衡 |
|------|------|--------|------|
| **Mem0** | 向量存储 + 图记忆，后端可插拔 | 多租户系统、广泛集成 | 对多 Agent 场景不够专精 |
| **Zep/Graphiti** | 时序知识图谱，双时间轴（bi-temporal）模型 | 需要关系建模 + 时序推理的企业 | 高级功能锁定在云端 |
| **Letta** | 具备分层存储（in-context/core/archival）的自编辑记忆 | 完整的 Agent 自省、有状态服务 | 对简单用例而言过于复杂 |
| **Cognee** | 通过可定制 ECL 管线与可定制 Tasks 构建的多层语义图 | 需要自适应、自学习的演进式 Agent 记忆；多跳推理 | 摄取期处理更重 |
| **LangMem** | 面向 LangGraph 工作流的记忆工具 | 已在使用 LangGraph 的团队 | 与 LangGraph 紧耦合 |
| **文件系统** | 带命名约定的普通文件 | 简单 Agent、原型验证 | 无语义搜索、无关系 |

当 Agent 需要双时间轴建模（同时追踪事件发生的时间与被摄取的时间）时，选择 Zep/Graphiti，因为其三层知识图谱（episode、语义实体、community 子图）擅长时序查询。当优先考虑借助托管基础设施快速投产时，选择 Mem0。当 Agent 需要通过其 Agent Development Environment 进行深度自省时，选择 Letta。当 Agent 必须构建密集的多层语义图时，选择 Cognee——它把文本块与实体类型作为节点分层组织，并带有细粒度的关系边，且每个核心环节（摄取、实体抽取、后处理、检索）均可定制。

**基准性能对比**

参考这些基准以设定预期，但要把它们视为针对检索维度、随来源而异的信号，而不是绝对排名。没有任何单一基准是定论。

| 系统 | DMR 准确率 | LoCoMo | HotPotQA（多跳） | 延迟 |
|------|-----------|--------|-----------------|------|
| Cognee | — | — | 公开高分 | 不定 |
| Zep（时序 KG） | 公开高分 | — | 各指标居中 | 有低延迟报告 |
| Letta（文件系统） | — | 公开的文件系统基线 | — | — |
| Mem0 | — | 公开的专用工具基线 | 在一次对比中较低 | — |
| MemGPT | 公开高分 | — | — | 不定 |
| GraphRAG | 公开中/高区间 | — | — | 不定 |
| 向量 RAG 基线 | 公开较低区间 | — | — | 快 |

关键要点：按检索形态而非品牌来比较记忆系统。把基准数字当作有时效的证据，在做出产品宣称之前必须重新核实；稳定的设计规则是：从浅层开始，度量检索质量，只有在更简单的一层失效时才增加语义或图结构。

### 记忆分层（决策点）

选择满足持久化要求的最浅记忆层。每加深一层都会增加基础设施成本与运维复杂度，因此只有当更浅一层无法满足检索或持久性需求时才升级。

| 层 | 持久化范围 | 实现 | 何时使用 |
|----|-----------|------|----------|
| **工作记忆（Working）** | 仅 context window | 系统提示词中的 scratchpad | 始终使用——利用注意力优势位置优化 |
| **短期（Short-term）** | 会话范围内 | 文件系统、内存缓存 | 中间工具结果、对话状态 |
| **长期（Long-term）** | 跨会话 | 键值存储 → 图数据库 | 用户偏好、领域知识、实体注册表 |
| **实体（Entity）** | 跨会话 | 实体注册表 + 属性 | 维持身份（“John Doe” 在多次对话中是同一个人） |
| **时序 KG（Temporal KG）** | 跨会话 + 历史 | 带有效期区间的图 | 随时间变化的事实、时间回溯查询、防止上下文冲突 |

### 检索策略

让检索策略与查询形态相匹配。语义搜索擅长直接的事实查找，但在多跳推理上会退化；基于实体的遍历能处理“关于 X 的一切”这类查询，但需要图结构；时间过滤能处理变化的事实，但需要有效期元数据。当准确率至关重要且基础设施预算允许时，将多种策略组合为混合检索。

| 策略 | 适用场景 | 局限 |
|------|----------|------|
| **语义**（embedding 相似度） | 直接事实查询 | 多跳推理上退化 |
| **基于实体**（图遍历） | “告诉我关于 X 的一切” | 需要图结构 |
| **时间**（有效期过滤） | 事实随时间变化 | 需要有效期元数据 |
| **混合**（语义 + 关键词 + 图） | 综合准确率最佳 | 基础设施最重 |

混合方法只检索相关的子图或记忆，从而缩减活跃上下文。Cognee 通过跨图、向量与关系存储的多种搜索模式实现混合检索，让 Agent 选择适合查询类型的检索策略，而不是一刀切。

### 记忆整合

定期运行整合以防止无限增长，因为不加约束的记忆积累会随时间推移降低检索质量。**使其失效但不要丢弃**——保留历史对需要重建过去状态的时序查询很重要。以记忆数量阈值、检索质量退化或计划间隔来触发整合。可运行的整合代码见 [实现参考](./references/implementation.md)。

## 实用指南

### 选择记忆架构

**从最简单的可行层开始，只有当检索质量退化时才增加复杂度。** 大多数 Agent 在第一天并不需要时序知识图谱。遵循以下升级路径：

1. **原型**：使用文件系统记忆。将事实连同时间戳存储为结构化 JSON。在投入基础设施之前先验证 Agent 行为。
2. **规模化**：当 Agent 需要语义搜索与多租户隔离时，迁移到 Mem0 或带元数据的向量存储，因为基于文件的查找无法处理相似度查询。
3. **复杂推理**：当 Agent 需要关系遍历、时间有效性或跨会话综合时，引入 Zep/Graphiti。Graphiti 使用带通用关系的结构化关联，保持图简单且易于推理；Cognee 构建更密集、带细粒度关系边的多层语义图——根据 Agent 需要的是时序双时间轴建模（Graphiti）还是更丰富的互联知识结构（Cognee）来选择。
4. **完全掌控**：当 Agent 必须以深度自省的方式自管理其记忆时，使用 Letta 或 Cognee，因为这些框架将记忆操作暴露为一等公民的 Agent 动作。

### 与上下文集成

即时（just-in-time）加载记忆，而不是预加载全部内容，因为庞大的上下文载荷代价高昂且会降低注意力质量。将检索到的记忆放在注意力优势位置（上下文的开头或结尾），以最大化其对生成的影响。

### 错误恢复

优雅地处理检索失败，因为记忆系统天然带有噪声。按顺序应用以下恢复策略：

- **检索为空**：回退到更宽泛的搜索（移除实体过滤、扩大时间范围）。若仍为空，提示用户澄清。
- **过期结果**：检查 `valid_until` 时间戳。若大多数结果已过期，先触发整合再重试。
- **事实冲突**：优先采用 `valid_from` 最近的事实。若置信度低，将冲突呈现给用户。
- **存储失败**：将写入排队等待重试。绝不因记忆写入而阻塞 Agent 的响应。

## 示例

**示例 1：Mem0 集成**
```python
from mem0 import Memory

m = Memory()
m.add("User prefers dark mode and Python 3.12", user_id="alice")
m.add("User switched to light mode", user_id="alice")

# Retrieves current preference (light mode), not outdated one
results = m.search("What theme does the user prefer?", user_id="alice")
```

**示例 2：时序查询**
```python
# Track entity with validity periods
graph.create_temporal_relationship(
    source_id=user_node,
    rel_type="LIVES_AT",
    target_id=address_node,
    valid_from=datetime(2024, 1, 15),
    valid_until=datetime(2024, 9, 1),  # moved out
)

# Query: Where did user live on March 1, 2024?
results = graph.query_at_time(
    {"type": "LIVES_AT", "source_label": "User"},
    query_time=datetime(2024, 3, 1)
)
```

**示例 3：Cognee 记忆摄取与搜索**
```python
import cognee
from cognee.modules.search.types import SearchType

# Ingest and build knowledge graph
await cognee.add("./docs/")
await cognee.add("any data")
await cognee.cognify()

# Enrich memory
await cognee.memify()

# Agent retrieves relationship-aware context
results = await cognee.search(
    query_text="Any query for your memory",
    query_type=SearchType.GRAPH_COMPLETION,
)
```

## 准则

1. 从文件系统记忆开始；只有检索质量提出要求时才增加复杂度
2. 为任何可能随时间变化的事实追踪时间有效性
3. 使用混合检索（语义 + 关键词 + 图）以获得最佳准确率
4. 定期整合记忆——使其失效但不要丢弃
5. 为检索失败而设计：记忆查找返回空时始终有回退方案
6. 考虑持久化记忆的隐私影响（留存策略、删除权）
7. 在变更前后用 LoCoMo 或 LongMemEval 对记忆系统做基准测试
8. 在生产环境中监控记忆增长与检索延迟

## 常见陷阱

1. **把所有东西塞进上下文**：将所有可用记忆加载进提示词代价高昂且降低注意力质量。应改用带相关性过滤的即时检索。
2. **忽视时间有效性**：事实会过时。没有有效期追踪，过时信息会污染上下文，Agent 会基于错误假设行动。
3. **过早过度工程化**：简单的文件系统记忆在某些基准上可以胜过更专业的工具（claim-memory-locomo-filesystem-baseline）。只有当简单方法被证明失效时才增加复杂度。
4. **没有整合策略**：无界的记忆增长会随时间降低检索质量。设置记忆数量阈值或计划间隔来触发整合。
5. **Embedding 模型不匹配**：用一种 embedding 模型写入、用另一种读取，会产生糟糕的检索效果，因为向量空间不可互换。为每个记忆存储固定单一 embedding 模型，若更换模型则对所有条目重新嵌入。
6. **图 schema 僵化**：过度结构化的图 schema（僵化的节点类型、固定的关系标签）会随领域演进而崩坏。优先使用通用关系类型与灵活的属性袋（property bag），使新实体类型无需 schema 迁移。
7. **过时记忆污染**：与当前状态矛盾的旧记忆会无声地腐蚀 Agent 行为。实现过期策略或置信度衰减，使 Agent 降低陈旧事实的优先级，并在检测到矛盾时显式呈现。
8. **记忆-上下文错配**：检索到主题相关但语境错误的记忆（例如 Agent 正在讨论 Python 语言，却检索到关于蟒蛇“Python”的记忆）。缓解方法是在记忆条目中纳入会话或领域元数据，并在检索时据此过滤。

## 集成

本 Skill 负责持久化语义记忆。相邻 Skill 负责草稿存储、压缩整理与上下文战术：

- `filesystem-context`：在需要语义检索之前，承担文件支撑的 scratchpad、日志与简单运行状态。
- `context-compression`：以文字形式保留会话状态的摘要与交接。
- `context-optimization`：活跃上下文预算内的即时记忆加载与检索范围限定。
- `context-degradation`：把过时或冲突的记忆当作上下文污染或上下文冲突来处理。
- `bdi-mental-states`：当信念、愿望、意图与出处（provenance）链条重要时，进行形式化心理状态建模。
- `multi-agent-patterns`：跨 Agent 的共享记忆。
- `evaluation`：记忆质量、检索正确性与基准选型。

## 参考资料

内部参考：
- [实现参考](./references/implementation.md) - 阅读时机：从零实现向量存储、属性图、时序查询或记忆整合逻辑时

本技能集中的相关 Skill：
- context-fundamentals - 阅读时机：设计记忆所汇入的上下文层时
- multi-agent-patterns - 阅读时机：多个 Agent 需要共享或协调记忆状态时

外部资源：
- Zep 时序知识图谱论文（arXiv:2501.13956） - 阅读时机：评估双时间轴建模或 Graphiti 架构时
- Mem0 生产架构论文（arXiv:2504.19413） - 阅读时机：评估托管记忆基础设施的权衡时
- Cognee 优化知识图谱 + LLM 推理论文（arXiv:2505.24478） - 阅读时机：比较多层语义图方法时
- LoCoMo 基准（Snap Research） - 阅读时机：评估长对话记忆留存时
- MemBench 评估框架（ACL 2025） - 阅读时机：设计记忆评估套件时
- Graphiti 开源时序 KG 引擎（github.com/getzep/graphiti） - 阅读时机：实现时序知识图谱时
- Cognee 开源知识图谱记忆（github.com/topoteretes/cognee） - 阅读时机：为记忆构建可定制 ECL 管线时
- [Cognee 对比：形态 vs. 功能](https://www.cognee.ai/blog/deep-dives/competition-comparison-form-vs-function) - 阅读时机：比较 Mem0、Graphiti、LightRAG、Cognee 的图结构时

---

## Skill 元数据

**创建**：2025-12-20
**最后更新**：2026-05-15
**作者**：Agent Skills for Context Engineering Contributors
**版本**：4.1.0
