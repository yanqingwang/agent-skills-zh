---
name: multi-agent-patterns
description: "本 Skill 用于设计需要上下文隔离、监督者或 swarm 协调、显式交接、并行执行，或需要判断是否值得使用多个 Agent 的多代理系统。"
---

> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/multi-agent-patterns/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 多代理架构模式

多代理架构把工作分发到多个语言模型实例上，每个实例拥有自己的 context window。设计得当，这种分发能带来超越单 Agent 极限的能力；设计不当，则会引入抵消收益的协调开销。关键洞见在于：子代理（Subagent）存在的首要目的是隔离上下文，而不是把角色分工拟人化。

## 何时启用

在以下情况启用本 Skill：

- 单 Agent 的上下文限制约束了任务复杂度
- 任务可自然分解为并行的子任务
- 不同子任务需要不同的工具集或系统提示词
- 构建必须同时处理多个领域的系统
- 将 Agent 能力扩展到单上下文极限之外
- 设计包含多个专门组件的生产级 Agent 系统

以下属于其他 Skill 负责的相邻工作，不要启用本 Skill：

- 在拓扑确定之前判断任务与模型的匹配、管线形态或项目级成本：`project-development`。
- 设计托管沙箱、预热池、远程会话或后台运行时基础设施：`hosted-agents`。
- 在受控运行时中通过 KV-cache 压缩共享编排者（orchestrator）状态：`latent-briefing`。
- 设计每个 Agent 暴露的工具：`tool-design`。

## 核心概念

当单个 Agent 的 context window 无法容纳所有与任务相关的信息时，使用多代理模式。上下文隔离是首要收益——每个 Agent 都在干净的上下文中运行，不携带其他子任务累积的噪声，从而避免信息在反复摘要中不断失真的传话游戏（telephone game）问题。

根据协调需求而非组织隐喻，在三种主导模式之间做出选择：

- **监督者/编排者（Supervisor/Orchestrator）**：当任务分解清晰且人工监督重要时，用于集中式控制。由单一协调者把工作委托给各专家并汇总结果。
- **对等/群体（Peer-to-Peer/Swarm）**：当僵化的计划适得其反时，用于灵活探索。任何 Agent 都能通过显式交接机制把控制权转移给任何其他 Agent。
- **分层（Hierarchical）**：用于具有分层抽象（战略、计划、执行）的大型项目。每一层以不同的细节层级运作，并拥有各自的上下文结构。

每个多代理系统都要围绕显式的协调协议、能抵御谄媚（sycophancy）倾向的共识机制，以及能防止错误传播级联的失效处理来设计。

## 详细主题

### 为什么选择多代理架构

**上下文瓶颈**
当单个 Agent 的上下文被累积的历史、检索到的文档和工具输出填满，以致性能开始退化时，就该启用多代理架构。识别三种退化信号：迷失在中部（lost-in-middle）效应（中段内容的注意力减弱）、注意力稀缺（竞争注意力的条目过多）和上下文污染（无关内容挤占了有用内容）。

将工作划分到多个 context window，让每个 Agent 都在专注于自身子任务的干净上下文中运行。在协调层汇总结果，不让任何单一上下文承担全部负担。

**Token 经济学现实**
为显著更高的 token 成本做预算。生产数据显示，多代理系统消耗的 token 可能远多于单 Agent 对话（claim-multi-agent-token-multiplier）：

| 架构 | Token 乘数 | 用例 |
|--------------|------------------|----------|
| 单 Agent 对话 | 基线 | 简单查询 |
| 带工具的单 Agent | 高于基线 | 使用工具的任务 |
| 多代理系统 | 远高于基线 | 复杂研究/协调 |

浏览型 Agent 的评估研究表明，token 用量、工具调用次数与模型选择主导了性能方差（claim-evaluation-browsecomp-variance）。这支持以单 Agent 基线来衡量多代理配置的实际效果，而不是想当然地认为多加 Agent 就有帮助。

在架构设计的同时优先考虑模型选型——升级到更好的模型往往比把 token 预算翻倍带来更大的性能提升。BrowseComp 数据显示，模型质量的改进常常胜过单纯的 token 增加。把模型选型与多代理架构当作互补策略。

**并行化论证**
把可并行的子任务分配给拥有全新上下文的专职 Agent，而不是在单个 Agent 中按顺序处理。需要在多个独立来源间搜索、分析不同文档或比较相互竞争方案的研究任务，都能从并行执行中获益。总的真实耗时接近最长子任务的时长，而不是所有子任务时长之和。

**专业化论证**
为每个 Agent 只配置其特定子任务所需的系统提示词、工具和上下文。通用 Agent 必须在上下文中携带所有可能的配置，从而稀释注意力。专职 Agent 只携带所需内容，以针对其领域优化的精简上下文运行。由协调者路由到专职 Agent，即可在不引发组合爆炸的情况下实现专业化。

### 架构模式

**模式 1：监督者/编排者（Supervisor/Orchestrator）**
部署一个维护全局状态与轨迹、把用户目标分解为子任务并路由给合适工作者（worker）的中心 Agent。

```
User Query -> Supervisor -> [Specialist, Specialist, Specialist] -> Aggregation -> Final Output
```

在以下情况选择此模式：任务分解清晰、需要跨领域协调，或人工监督很重要。

预期这些权衡：工作流控制严格、人在回路（human-in-the-loop）干预更容易，但监督者的上下文会成为瓶颈，监督者失效会级联到所有工作者，而且会出现"传话游戏"问题——监督者转述子代理响应时出现偏差。

**传话游戏问题及其解决方案**
预期监督者架构在初始阶段会比优化后的版本表现差约 50%，原因正是传话游戏问题（LangGraph 基准）。监督者转述子代理响应，每转述一次就损失一分保真度。

通过实现 `forward_message` 工具来修复，该工具允许子代理把响应直接传给用户：

```python
def forward_message(message: str, to_user: bool = True):
    """
    Forward sub-agent response directly to user without supervisor synthesis.

    Use when:
    - Sub-agent response is final and complete
    - Supervisor synthesis would lose important details
    - Response format must be preserved exactly
    """
    if to_user:
        return {"type": "direct_response", "content": message}
    return {"type": "supervisor_input", "content": message}
```

当子代理可以直接回应用户时，优先选择 swarm 架构而非监督者，因为这能彻底消除转译错误。

**模式 2：对等/群体（Peer-to-Peer/Swarm）**
移除中心控制，允许 Agent 基于预定义协议直接通信。任何 Agent 都通过显式交接机制把控制权转移给其他任何 Agent。

```python
def transfer_to_agent_b():
    return agent_b  # Handoff via function return

agent_a = Agent(
    name="Agent A",
    functions=[transfer_to_agent_b]
)
```

在以下情况选择此模式：任务需要灵活探索、僵化的计划适得其反，或需求动态涌现、无法预先分解。

预期这些权衡：没有单点故障、广度优先扩展有效，但协调复杂度随 Agent 数量增加而上升，没有中心状态维护者时分岔风险升高，稳健的收敛约束变得不可或缺。

定义带状态传递的显式交接协议。确保 Agent 把自己的上下文需求告知接收方。

**模式 3：分层（Hierarchical）**
把 Agent 组织成抽象层：战略（目标定义）、计划（任务分解）和执行（原子任务）。

```
Strategy Layer (Goal Definition) -> Planning Layer (Task Decomposition) -> Execution Layer (Atomic Tasks)
```

在以下情况选择此模式：项目有清晰的层级结构、工作流包含管理层，或任务既需要高层计划又需要细节执行。

预期这些权衡：关注点分离清晰、不同层级可支持不同的上下文结构，但层间存在协调开销、战略与执行可能错位、错误传播路径复杂。

### 上下文隔离作为设计原则

把上下文隔离当作多代理架构的首要目的。每个子代理都应在专注于自身子任务的干净 context window 中运行，不携带其他子任务累积的上下文。

**隔离机制**
为每个子任务选择合适的隔离机制：

- **完整上下文委托**：把规划者的全部上下文共享给子代理。用于子代理需要完整理解的复杂任务。子代理有自己的工具和指令，但接收完整上下文来做决策。注意：这在一定程度上背离了上下文隔离的初衷。
- **指令传递**：通过函数调用创建指令，子代理只接收所需内容。用于简单、定义明确的子任务。保持隔离，但限制了子代理的灵活性。
- **文件系统记忆**：Agent 对持久存储进行读写。用于需要共享状态的复杂任务。文件系统充当协调机制，避免共享状态传递导致的上下文膨胀。会引入延迟与一致性挑战，但比消息传递更可扩展。

根据任务复杂度、协调需求和可接受的延迟来选择。默认使用指令传递，需要共享状态时升级到文件系统记忆。除非子任务确实需要，否则避免完整上下文委托。

### 共识与协调

**投票问题**
避免简单多数投票——它把弱模型的幻觉等同于强模型的推理。若不加干预，多代理讨论会由于天然的求同偏向而退化为对错误前提的共识。

**加权投票**
按置信度或专业度给 Agent 的投票加权。置信度更高或具备领域专长的 Agent 在最终决策中应占更大权重。

**辩论协议**
让 Agent 在多轮中相互批判对方的输出。对抗式批判在复杂推理上往往比协作式共识产出更高的准确率。警惕谄媚式趋同——Agent 为了显得好相处而达成一致，而不是为了正确。

**基于触发器的干预**
监测多代理交互中的行为标记。讨论毫无进展时触发停滞触发器；Agent 互相模仿答案而缺乏独立推理时，检测谄媚信号。

### 框架考量

不同框架以不同理念实现这些模式。LangGraph 使用带显式节点与边的基于图的状态机。AutoGen 通过 GroupChat 使用对话式/事件驱动模式。CrewAI 使用带层级 crew 结构的基于角色的流程。

## 实用指南

### 失效模式与缓解

**失效：监督者瓶颈**
监督者累积所有工作者的上下文，容易走向饱和与退化。

缓解方式：约束工作者的输出 schema，让工作者只返回蒸馏后的摘要。使用检查点机制持久化监督者状态，而不必在上下文中携带完整历史。

**失效：协调开销**
Agent 之间的通信消耗 token 并引入延迟。复杂的协调可能抵消并行化的收益。

缓解方式：通过清晰的交接协议最小化通信。尽可能批量汇总结果。使用异步通信模式。实测多代理协调相比拥有更长上下文的单个 Agent 是否真的节省时间。

**失效：分岔（Divergence）**
没有中心协调的各 Agent 追逐不同目标，逐渐偏离预期目的。

缓解方式：为每个 Agent 定义清晰的目标边界。实现验证共享目标进展的收敛检查。为 Agent 执行设置生存时间（time-to-live）限制，防止无界探索。

**失效：错误传播**
某个 Agent 输出中的错误会传播给消费该输出的下游 Agent，复合成越来越离谱的错误结果。

缓解方式：在传递给消费方之前校验 Agent 输出。实现带熔断器的重试逻辑。尽可能使用幂等操作。考虑增加一个校验 Agent，在关键输出进入管线之前交叉检查。

## 示例

**示例 1：研究团队架构**
```text
Supervisor
├── Researcher (web search, document retrieval)
├── Analyzer (data analysis, statistics)
├── Fact-checker (verification, validation)
└── Writer (report generation, formatting)
```

**示例 2：交接协议**
```python
def handle_customer_request(request):
    if request.type == "billing":
        return transfer_to(billing_agent)
    elif request.type == "technical":
        return transfer_to(technical_agent)
    elif request.type == "sales":
        return transfer_to(sales_agent)
    else:
        return handle_general(request)
```

## 准则

1. 把上下文隔离作为多代理系统的首要收益来设计
2. 根据协调需求而非组织隐喻选择架构模式
3. 实现带状态传递的显式交接协议
4. 使用加权投票或辩论协议达成共识
5. 监测监督者瓶颈并实现检查点机制
6. 在 Agent 之间传递输出前先校验
7. 设置生存时间限制以防止无限循环
8. 显式测试失效场景

## 常见陷阱

1. **监督者瓶颈随规模扩大**：监督者的上下文压力随工作者数量非线性增长。工作者达到 5 个以上时，监督者花在处理摘要上的 token 比工作者花在实际任务上的还多。为每个监督者下的工作者数量设置硬上限（3-5 个），需要时增加第二层监督者，而不是让单个监督者过载。

2. **低估 token 成本**：多代理运行的成本约为基线的 15 倍。团队持续低估预算，因为他们按单个 Agent 估算成本，却没有计入协调开销、重试和共识轮次。按 15 倍做预算，把低于该值的部分视为盈余。

3. **谄媚式共识**：辩论模式中的 Agent 倾向于在讨人喜欢的答案上收敛，而不是在正确答案上收敛。LLM 天然偏向求同。对策是分配显式的对抗角色，并要求 Agent 在允许收敛之前先陈述分歧。

4. **Agent 蔓延（agent sprawl）**：Agent 数量超过 3-5 个后收益递减，协调开销增加。每新增一个 Agent 都会以平方级增加通信信道。从最小可行数量起步，只有当存在明确的上下文隔离收益时才增加。

5. **消息传递中的传话游戏**：信息在 Agent 之间经过反复摘要而不断失真。每个 Agent 转述一次就丢失一分细节。对需要多个 Agent 忠实访问的状态，使用文件系统协调而不是消息传递。

6. **错误传播级联**：一个 Agent 的幻觉会变成另一个 Agent 的"事实"。下游 Agent 无法区分上游幻觉与真实信息。在 Agent 之间加入校验检查点，绝不未经验证就信任上游输出。

7. **过度分解**：把任务切分得过细，产生的协调开销比任务本身还多。10 步管线配 10 个 Agent，花在交接上的 token 比实际工作还多。只有当子任务确实能从独立上下文中获益时才分解。

8. **缺失共享状态**：在没有共享文件系统或状态存储的情况下运行的 Agent 会重复工作、产出不一致的结果，并丢失对已完成事项的追踪。在构建多代理工作流之前先建立共享持久存储。

## 集成

本 Skill 负责代理拓扑与协调协议。相邻 Skill 负责项目形态、托管运行时与潜在状态传递：

- `project-development`：在拓扑细节之前的项目级"单 Agent 还是多 Agent"选择。
- `hosted-agents`：远程沙箱、会话、预热池与多人（multiplayer）基础设施。
- `memory-systems`：跨 Agent 的共享持久状态。
- `tool-design`：工具专业化以及 spawn/status 工具契约。
- `context-optimization`：作为 token 效率战术之一的分区策略。
- `latent-briefing`：模型匹配时，编排者与工作者之间的 KV-cache 轨迹交接。
- `evaluation`：在计入协调成本后衡量多个 Agent 是否改善结果。

## 参考资料

内部参考：

- [框架参考](./references/frameworks.md) - 阅读时机：正在 LangGraph、AutoGen 或 CrewAI 中实现具体的多代理模式，需要框架专属代码示例时

本技能集中的相关 Skill：

- context-fundamentals - 阅读时机：在设计代理分区之前需要理解 context window 机制时
- memory-systems - 阅读时机：Agent 需要跨上下文边界共享状态或在运行之间持久化信息时
- context-optimization - 阅读时机：单个 Agent 的上下文过大、需要分区或压缩策略时

外部资源：

- [LangGraph 文档](https://langchain-ai.github.io/langgraph/) - 阅读时机：构建带显式状态机的基于图的多代理工作流时
- [AutoGen 框架](https://microsoft.github.io/autogen/) - 阅读时机：实现对话式 GroupChat 模式或事件驱动的代理协调时
- [CrewAI 文档](https://docs.crewai.com/) - 阅读时机：设计基于角色的层级代理流程时
- [多代理协调研究](https://arxiv.org/abs/2308.00352) - 阅读时机：需要多代理系统理论与评估的学术支撑时

---

## Skill 元数据

**创建**：2025-12-20
**最后更新**：2026-05-15
**作者**：Agent Skills for Context Engineering Contributors
**版本**：2.1.0
