---
name: tool-design
description: "本 Skill 专用于 Agent 系统的工具接口层：编写可供 Agent 据以路由的工具描述，设计工具 schema 与响应格式，命名约定，可操作的错误恢复信息，MCP 服务器设计，工具集整合，以及决定何时新增或移除单个工具。当工作单元是单个工具或一组工具时使用本 Skill。项目形态、管线架构与任务-模型匹配决策路由到 project-development；是否引入子代理的决策路由到 multi-agent-patterns。"
---

> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/tool-design/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 面向 Agent 的工具设计

把每个工具都设计为确定性系统与非确定性 Agent 之间的一份契约。与面向人类的 API 不同，面向 Agent 的工具必须仅凭工具描述就让契约毫无歧义：Agent 从描述中推断意图，并生成必须匹配预期格式的调用。任何歧义都会成为潜在的失效模式，再多的提示词工程也无法修复。

本 Skill 的工作单元是单个工具或一个工具目录。项目形态、管线架构、任务-模型匹配与项目级成本决策属于 `project-development`。是否引入子代理（Subagent）的决策属于 `multi-agent-patterns`。本 Skill 负责的是连接确定性代码与 Agent 的接口层。

## 何时启用

当工作单元是工具时，在以下情况启用本 Skill：

- 编写新的工具描述、schema 或响应格式。
- 调试 Agent 选错工具或生成畸形调用的案例。
- 整合存在功能重叠的工具目录（经典场景：“我们有 17 个工具，Agent 一半时间都选错”）。
- 设计可操作的错误信息，让 Agent 能自我纠正。
- 在整个工具目录内一致地命名工具与参数（MCP 命名空间、动词-名词命名）。
- 在新增第三方工具之前，依据整合原则对其进行评估。

以下属于其他 Skill 负责的相邻工作，不要启用本 Skill：

- 决定项目是否应该使用 LLM，或管线阶段应如何划分：`project-development`。
- 决定是否把工作拆分给子代理，或让单个 Agent 携带更多工具：`multi-agent-patterns`。
- 在轨迹层面降低工具输出的 token 权重（观察掩码、规模化场景下的格式选项选择）：`context-optimization`。

## 核心概念

围绕整合原则设计工具：如果人类工程师都无法明确说出给定情况下应该使用哪个工具，就不能指望 Agent 做得更好。持续精简工具集，直到每个工具都有唯一明确的用途，因为 Agent 通过比较描述来选择工具，任何重叠都会引入选择错误。

把每条工具描述都当作塑造 Agent 行为的提示词工程来对待。描述不是写给人类看的文档——它会被注入 Agent 的上下文，直接引导推理。编写的描述应回答工具做什么、何时使用、返回什么，因为这三个问题正是 Agent 在工具选择过程中评估的内容。

## 详细主题

### 工具-Agent 接口

**工具即契约**
把每个工具设计为自包含的契约。人类调用 API 时会阅读文档、理解约定，然后发出合适的请求。Agent 则必须从单一描述块推断出完整契约。通过纳入格式示例、预期模式与显式约束来消除契约歧义。调用方需要知道的信息一概不可省略，因为 Agent 在发起调用之前无法提出澄清问题。

**工具描述即提示词**
编写工具描述时要知道，它们会直接载入 Agent 上下文并共同引导行为。像“搜索数据库”这样含糊的描述配上隐晦的参数名，会迫使 Agent 去猜——而猜测会产生错误的调用。正确的做法是纳入使用场景、参数格式示例与合理的默认值。描述中的每个字都在帮助或损害工具选择的准确性。

**命名空间与组织**
随着工具集合增长，用公共前缀为工具划分命名空间，因为层级分组对 Agent 有益。当 Agent 需要数据库操作时，它路由到 `db_*` 命名空间；需要 Web 交互时，路由到 `web_*`。没有命名空间，Agent 就必须在扁平列表中评估每个工具，随着数量增长，选择准确性会退化。

### 整合原则

**单个综合工具**
构建单个综合工具，而不是多个相互重叠的狭窄工具。与其分别实现 `list_users`、`list_events` 与 `create_event`，不如实现一个 `schedule_event`，在一次调用中完成查找空闲时段并安排日程。综合工具在内部处理完整工作流，免去 Agent 按正确顺序串联调用的负担。

**整合为何有效**
采用整合是因为 Agent 的上下文与注意力有限。集合中的每个工具都会在工具选择时争夺注意力，每条描述都消耗上下文预算的 token，而重叠的功能会制造歧义。整合消除冗余描述、移除选择歧义并缩减有效工具集。Vercel 的 d0 案例研究是一个具体例子：把专用工具缩减为更小的原语工具集，实测结果反而更好（claim-tool-design-vercel-d0-reduction）。

**何时不要整合**
当工具具有根本不同的行为、服务于不同场景、或必须能独立调用时，保持它们相互分离。过度整合会制造另一个问题：单个工具若参数与模式过多，Agent 就难以正确参数化。

### 架构级精简

把整合原则推向其逻辑极端：移除大部分专用工具，改用原语的、通用的能力。生产证据表明，这种做法可以胜过精密的多工具架构。

**文件系统 Agent 模式**
通过单个命令执行工具提供直接的文件系统访问，而不是为数据探索、schema 查找与查询校验各自构建定制工具。Agent 使用标准 Unix 工具（grep、cat、find、ls）来探索并操作系统。这之所以可行，是因为：文件系统是被模型深刻理解的成熟抽象；标准工具行为可预测；Agent 可以灵活串联原语，而不受预定义工作流约束；文件中的优质文档可以取代摘要工具。

**精简何时胜过复杂**
当数据层文档完善且结构一致、模型具备足够的推理能力、专用工具在束缚而非赋能模型、或维护脚手架耗费的时间多于改进成果时，选择精简。当底层数据混乱或文档不佳、领域需要模型不具备的专业知识、安全约束必须限制 Agent 行为、或操作确实受益于结构化工作流时，避免精简。

**为未来的模型而构建**
设计能从模型进步中获益的最小化架构，而不是把当前局限固化下来的精密架构。追问每个工具是在开启新能力，还是在约束模型本可自行完成的推理——作为“护栏”构建的工具，往往随着模型进步变成负资产。

生产证据见 [架构级精简案例研究](./references/architectural_reduction.md)。

### 工具描述工程

**描述结构**
让每条工具描述回答四个问题：

1. 工具做什么？准确说明工具完成的任务——避免“有助于”或“可用于”这类含糊措辞。
2. 何时使用？写明直接触发条件（“用户询问价格”）与间接信号（“需要当前市场汇率”）。
3. 接受哪些输入？为每个参数写明类型、约束、默认值与格式示例。
4. 返回什么？写明输出格式、结构、成功响应示例与错误条件。

**默认参数选择**
让默认值反映常见用例。默认值免去不必要的参数指定，从而减轻 Agent 负担，并防止因遗漏参数而出错。选择的默认值应能产出有用结果，而不要求 Agent 理解每个选项。

### 响应格式优化

提供响应格式选项（简洁 vs. 详细），因为工具响应大小显著影响上下文占用。简洁格式只返回关键字段，适合确认类操作。详细格式返回完整对象，适合需要完整上下文驱动决策的场景。在工具描述中写明每种格式的适用时机，让 Agent 学会恰当选择。

### 错误信息设计

为两类受众设计错误信息：调试问题的开发者，以及从失败中恢复的 Agent。对 Agent 而言，每条错误信息都必须可操作——必须说明哪里出了错、如何纠正。对可重试错误给出重试指引，对输入错误给出纠正后的格式示例，对不完整请求给出具体缺失字段。只说“失败”的错误提供零恢复信号。

### 工具定义 schema

在所有工具间建立一致的 schema。工具名使用动词-名词模式（`get_customer`、`create_order`），参数名跨工具保持一致（始终用 `customer_id`，绝不要时而 `id` 时而 `identifier`），返回字段名也保持一致。一致性降低 Agent 的认知负担，并提升跨工具的泛化能力。

### 工具集合设计

把工具集合限制在用途互不重叠的最小集合，因为描述重叠会导致模型混乱，且更多工具并不总是带来更好的结果。当确实需要更多工具时，用命名空间创建逻辑分组。实现选择机制：按领域对工具分组、基于示例的选择提示，以及路由到专用子工具的伞状工具。

### MCP 工具命名要求

在 MCP（Model Context Protocol）下，始终使用完全限定的工具名，以避免“找不到工具”（tool not found）错误。

格式：`ServerName:tool_name`

```python
# Correct: Fully qualified names
"Use the BigQuery:bigquery_schema tool to retrieve table schemas."
"Use the GitHub:create_issue tool to create issues."

# Incorrect: Unqualified names
"Use the bigquery_schema tool..."  # May fail with multiple servers
```

没有服务器前缀时，当多个 MCP 服务器可用，Agent 可能无法定位工具。建立命名约定，在所有工具引用中包含服务器上下文。

### 用 Agent 优化工具

把观察到的工具失败反馈给 Agent，以诊断问题并改进描述。在目标工具目录上复现之前，把所报告的效率提升视为特定于工作负载的结论。

**工具测试 Agent 模式**：

```python
def optimize_tool_description(tool_spec, failure_examples):
    """
    Use an agent to analyze tool failures and improve descriptions.

    Process:
    1. Agent attempts to use tool across diverse tasks
    2. Collect failure modes and friction points
    3. Agent analyzes failures and proposes improvements
    4. Test improved descriptions against same tasks
    """
    prompt = f"""
    Analyze this tool specification and the observed failures.

    Tool: {tool_spec}

    Failures observed:
    {failure_examples}

    Identify:
    1. Why agents are failing with this tool
    2. What information is missing from the description
    3. What ambiguities cause incorrect usage

    Propose an improved tool description that addresses these issues.
    """

    return get_agent_response(prompt)
```

这就形成了反馈回路：使用工具的 Agent 产生失败数据，Agent 再利用这些数据改进工具描述，进而减少未来的失败。

### 测试工具设计

依据五项标准评估工具设计：无歧义性、完整性、可恢复性、效率与一致性。测试方法是呈现有代表性的 Agent 请求，并对照预期行为评估由此产生的工具调用。

## 实用指南

### 工具选择框架

设计工具集合时：
1. 识别 Agent 必须完成的各类工作流
2. 把相关操作归入综合工具
3. 确保每个工具用途清晰、无歧义
4. 写明错误情况与恢复路径
5. 用真实的 Agent 交互进行测试

### 工具审计清单

把工具加入 Agent 之前，用这份清单逐项检查：

1. **名称**：动词-名词式；若目录包含多个领域则加命名空间。
2. **描述**：说明工具做什么、何时使用、返回什么。
3. **Schema**：每个参数都有类型、约束、默认值与示例值。
4. **返回结构**：成功与错误载荷均有文档且机器可读。
5. **恢复**：每条错误都告诉 Agent 重试前应改什么。
6. **重叠**：没有其他工具具有相同的激活场景。
7. **整合决策**：相邻的狭窄工具已合并，除非需要独立调用。
8. **token 影响**：大响应支持简洁模式或文件引用模式。

## 示例

**示例 1：设计良好的工具**
```python
def get_customer(customer_id: str, format: str = "concise"):
    """
    Retrieve customer information by ID.

    Use when:
    - User asks about specific customer details
    - Need customer context for decision-making
    - Verifying customer identity

    Args:
        customer_id: Format "CUST-######" (e.g., "CUST-000001")
        format: "concise" for key fields, "detailed" for complete record

    Returns:
        Customer object with requested fields

    Errors:
        NOT_FOUND: Customer ID not found
        INVALID_FORMAT: ID must match CUST-###### pattern
    """
```

**示例 2：糟糕的工具设计**

本示例展示了若干工具设计反模式：

```python
def search(query):
    """Search the database."""
    pass
```

**该设计的问题：**

1. **名称含糊**：“search”含混不清——搜索什么？出于什么目的？
2. **参数缺失**：哪个数据库？query 应采用什么格式？
3. **无返回说明**：这个函数返回什么？列表？字符串？错误处理呢？
4. **无使用场景**：Agent 何时该用这个工具而不是其他工具？
5. **无错误处理**：数据库不可用时会发生什么？

**失效模式：**
- Agent 可能在应该使用更具体工具时调用了它
- Agent 无法确定正确的查询格式
- Agent 无法解读结果
- Agent 无法从失败中恢复

## 准则

1. 编写能回答“做什么、何时用、返回什么”的描述
2. 使用整合来减少歧义
3. 实现响应格式选项以提升 token 效率
4. 为 Agent 恢复而设计错误信息
5. 建立并遵循一致的命名约定
6. 限制工具数量并用命名空间组织
7. 用真实的 Agent 交互测试工具设计
8. 依据观察到的失效模式迭代
9. 追问每个工具是在赋能还是束缚模型
10. 相比专用包装器，优先使用原语的通用工具
11. 把投入放在文档质量而非工具的精密程度上
12. 构建能从模型进步中获益的最小化架构

## 常见陷阱

1. **描述含糊**：像“在数据库中搜索客户信息”这样的描述留下太多未回答的问题。应写明确切的数据库、查询格式与返回结构。
2. **隐晦的参数名**：名为 `x`、`val` 或 `param1` 的参数迫使 Agent 猜测含义。应使用无需阅读更多文档就能传达用途的描述性名称。
3. **缺失错误恢复指引**：用“发生了错误”这类笼统信息报错的工具不提供任何恢复信号。每条错误响应都必须告诉 Agent 出了什么错、接下来尝试什么。
4. **跨工具命名不一致**：一个工具用 `id`，另一个用 `identifier`，第三个用 `customer_id`，会造成混乱。在整个工具集合中统一参数名。
5. **MCP 命名空间冲突**：当多个 MCP 工具提供方注册了名称相似的工具（例如两台服务器都暴露 `search`），Agent 无法消歧。始终使用完全限定的 `ServerName:tool_name` 格式，并在新增提供方时审计冲突。
6. **工具描述腐化**：随着底层 API 演进，描述会变得不准确——参数被新增、返回格式变化、错误码变动。把描述当代码对待：纳入版本管理，在 API 变更时评审，并对照当前行为测试。
7. **过度整合**：让单个工具处理太多工作流，会产生庞大的参数列表，Agent 难以选出正确的组合。如果工具需要超过 8-10 个参数，或服务根本不同的用例，就拆分它。
8. **参数爆炸**：过多可选参数会让 Agent 决策不堪重负。Agent 必须评估的每个参数都增加认知负担。提供合理默认值，把相关选项归入格式预设，并把很少使用的参数移入 `options` 对象。
9. **缺失错误上下文**：只说“失败”或“输入无效”、却不说明是哪个输入、为何失败、或合法输入长什么样，会让 Agent 无法自我纠正。每条错误响应都应包含无效值、期望格式与一个具体示例。

## 集成

本 Skill 负责工具接口层。相邻决策由其他 Skill 负责：

- `project-development`：项目形态、管线阶段选择、任务-模型匹配、项目级成本估算。如果问题是“什么是正确的管线架构”而非“什么是正确的工具 API”，路由到那里。
- `multi-agent-patterns`：决定一个携带更多工具的 Agent 是否优于两个携带更小工具目录的 Agent。如果问题是“是否应拆分为子代理”，路由到那里。
- `context-optimization`：轨迹级 token 效率、观察掩码、跨大量工具调用的响应格式选项选择。如果问题是“如何降低累积工具输出的 token 权重”，路由到那里。
- `context-fundamentals`：工具定义如何消耗注意力预算的概念性问题。如果问题是“为什么增加工具会降低路由准确性”，从这里开始。
- `evaluation`：评判工具集是否整体改善了 Agent 的成果。

## 参考资料

内部参考：
- [最佳实践参考](./references/best_practices.md) - 阅读时机：从零设计新工具，或审计现有工具集合的质量缺口时
- [架构级精简案例研究](./references/architectural_reduction.md) - 阅读时机：考虑移除专用工具改用原语，或评估复杂工具架构是否站得住脚时

本技能集中的相关 Skill：
- context-fundamentals - 工具与上下文的交互
- evaluation - 工具测试模式

外部资源：
- MCP（Model Context Protocol）文档 - 阅读时机：为多服务器 Agent 环境实现工具，或调试工具路由失败时
- 框架工具约定 - 阅读时机：采用新的 Agent 框架、需要把工具设计原则映射到框架特有 API 时
- 面向 Agent 的 API 设计最佳实践 - 阅读时机：把现有的面向人类的 API 转化为面向 Agent 的工具接口时
- Vercel d0 Agent 架构案例研究 - 阅读时机：评估是否整合工具，或为架构级精简寻找生产证据时

---

## Skill 元数据

**创建**：2025-12-20
**最后更新**：2026-05-15
**作者**：Agent Skills for Context Engineering Contributors
**版本**：2.2.0
