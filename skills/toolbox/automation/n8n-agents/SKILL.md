---
name: n8n-agents
description: 以正确方式设计 n8n AI Agent。适用于构建或编辑任何 @n8n/n8n-nodes-langchain.* AI 节点（AI Agent、LLM chain、Text Classifier、Information Extractor），以及用户提到 AI agents、LLM with tools、tool calling、$fromAI、系统提示词、Agent 记忆、sessionId、结构化/JSON 输出、输出解析器、RAG、向量存储、聊天助手/机器人或人工审核时。涵盖 Agent、chain、classifier 之间的取舍，model/memory/tools/outputParser 插槽，工具名称/描述作为提示词，带 autoFix 的结构化输出，memory、RAG、人工审核与聊天拓扑。
---

> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-agents/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# n8n Agents

n8n AI Agent 节点（`@n8n/n8n-nodes-langchain.agent`）是一个多轮 LLM 驱动器，带有用于 model、memory、tools 以及可选 output parser 的子节点。本 Skill 是设计 Agent 及其周边 LangChain 系列节点的**深度**指南。若想了解「Agent 在工作流中处于什么位置」的宏观视图，参见 **n8n-workflow-patterns** 的 `ai_agent_workflow.md`；本 Skill 则再深入一层，讲*如何把它做好*。

关于节点类型格式：在 workflow JSON 中，LangChain 节点使用长格式 `@n8n/n8n-nodes-langchain.*`（`.agent`、`.lmChatOpenAi`、`.memoryBufferWindow`、`.outputParserStructured`、`.toolWorkflow`、`.toolHttpRequest`、`.toolCode`）。调用 `get_node` / `validate_node` 时，使用**短**格式（`nodes-langchain.agent`）。格式规则参见 **n8n-mcp-tools-expert**。

---

## 先选对节点

任务只是一次性分类或抽取时却搬出 Agent，是最常见的过度设计。在接线之前先做决定：

| 你的需求… | 使用 | 原因 |
|---|---|---|
| 调用工具、跨多轮推理，或保存记忆 | **AI Agent**（`.agent`） | 完整循环：model + tools + memory + 可选 parser。想统一标准时也是稳妥的默认选择。 |
| 一次性文本进 → 文本出，不需工具 | **Basic LLM Chain**（`.chainLlm`） | 没有 Agent 循环，更易调试。仍可挂一个 `outputParserStructured` 子节点。 |
| 把自然语言输入路由到 **N 个分支**之一 | **Text Classifier**（`.textClassifier`） | 单个节点、N 个输出句柄，下游直接接入各分支。别用 Agent + Switch。 |
| 从自由文本中抽取结构化字段 | **Information Extractor**（`.informationExtractor`） | 借助 schema 专门做字段抽取。 |
| 正面/中性/负面三向划分 | **Sentiment Analysis**（`.sentimentAnalysis`） | 内置分支输出。 |
| 压缩长文档 | **Summarization Chain**（`.chainSummarization`） | 内置 Map-reduce 摘要。 |
| 生成图像 / 音频 / 视频 | **服务商的原生单次调用节点**（OpenAI、Gemini、ElevenLabs…） | 媒体生成绝不套进 Agent，参见「二进制数据与 Agent 边界」。 |

**Text Classifier 细节（Agent + Switch 反模式）：** 每个类别都必须同时有**名称**和**描述**。模型依据*描述*而非名称来路由，缺少描述的类别只能靠抛硬币被选中。设置 `options.enableAutoFixing: true` 以增强对边界输入的健壮性。一个节点、N 个分支，搞定。用一个「决定」的 Agent 再接一个「路由」的 Switch，等于为本可由 Text Classifier 原生完成的事付出两个节点外加提示词样板代码。

聊天模型节点（`.lmChatOpenAi`、`.lmChatAnthropic`、`.lmChatOpenRouter` …）是**子节点**，不能独立运行。它们通过 `ai_languageModel` 连接接入 chain、agent、classifier 或 extractor。

---

## 子节点模式

Agent 有一个**主输入**（提示词 / 用户消息），以及最多四个**子节点插槽**，每个插槽由各自的 `ai_*` 连接类型接入：

| 插槽 | 连接类型 | 是否必需 | 节点示例 |
|---|---|---|---|
| **model** | `ai_languageModel` | 是 | `.lmChatOpenAi`、`.lmChatAnthropic`、`.lmChatOpenRouter` |
| **memory** | `ai_memory` | 可选 | `.memoryBufferWindow`、`.memoryPostgresChat` |
| **tools** | `ai_tool` | 可选（却是 Agent 的意义所在） | `slackTool`、`.toolWorkflow`、`.toolHttpRequest`、`.toolCode` |
| **outputParser** | `ai_outputParser` | 可选 | `.outputParserStructured` |

子节点从自身连向 Agent。在 workflow JSON 中，连接记录在**子节点**上，以 `ai_*` 类型为键：


```json
"Main LLM": {
  "ai_languageModel": [[{ "node": "AI Agent", "type": "ai_languageModel", "index": 0 }]]
},
"Simple Memory": {
  "ai_memory": [[{ "node": "AI Agent", "type": "ai_memory", "index": 0 }]]
},
"Search customer DB": {
  "ai_tool": [[{ "node": "AI Agent", "type": "ai_tool", "index": 0 }]]
}
```


多个工具都接入同一个 `ai_tool` 索引 0，它们层层叠加，不会分散到不同索引。用 `n8n_update_partial_workflow` 时，通过 `sourceOutput: "ai_tool"` 的 `addConnection` 操作逐个接线。Agent 把最终答案放进 **`$json.output`**（不是 `.text`，也不是 `.response`），下游节点读取 `{{ $json.output }}`。

完整的无状态 Agent 核心节点对象片段参见 **EXAMPLES.md**。

---

## 两条不可妥协的规则

1. **工具名称与描述本就是提示词的一部分。** 模型只靠读取工具的名称和描述来挑选工具，别无其他依据。一个名为 `tool1`、描述为空的工具对模型而言不可见：模型会跳过它、选错它，或凭空臆造参数。通常不会报错，只留下一个「就是不用我的工具」的 Agent。把这两者当作 API 设计来对待。 → **TOOLS.md**
2. **结构化输出必须既能解析又能 autoFix。** `outputParserStructured` 配上 `autoFix: true` 和一个**具备代码能力的修复模型**，才是生产级做法。没有 autoFix，一次格式错误的 JSON 响应就会让整个工作流停摆。 → **STRUCTURED_OUTPUT.md**

---

## 稳妥的默认做法

- **每个工具的用法写进工具描述，而不是系统提示词。** 凡是关于*如何调用这个具体工具*的内容都归属于该工具，这样它能随 Agent 复用，也让系统提示词保持聚焦。 → **SYSTEM_PROMPT.md**
- **多步骤任务一律用子工作流工具（`.toolWorkflow`）。** 任何工作流都能变成带类型化 `$fromAI()` 输入的工具，并与分支、错误处理、复用组合。拿不准时默认选它。 → **SUBWORKFLOW_AS_TOOL.md** 与 **n8n-subworkflows**。
- **有用户可见副作用的工具要包一层人工审核。** 发送、付款、退款、账户变更都要挡在审批节点之后，由人工签字确认后工具才触发。 → **HUMAN_REVIEW.md**
- **调高 `maxIterations`。** 默认的工具调用上限**很低**（多数版本只有个位数），单工具 Agent 尚可，对每轮要串联多次调用的多工具 Agent 就远远不够。表现为「max iterations reached」或空输出。把 `options.maxIterations` 设为符合实际的上限（专注型子 Agent 用 15，宽泛的编排器用 50-200）。
- **把当前日期放进系统提示词**，用 `{{ $now }}`（或 `{{ $now.format('DDDD') }}`）。硬编码的日期立刻就会过时。

---

## 四种工具类型

选能完成任务的最轻量方案：

| 工具类型 | 节点 | 适用场景 |
|---|---|---|
| **原生工具节点** | `slackTool`、`gmailTool`、`toolCalculator` … | 能力对应「一个现成节点 + 一项操作」。开销最低。 |
| **子工作流即工具** | `.toolWorkflow` | 不止一个节点、逻辑要复用，或希望可独立测试。n8n 的标准做法，**拿不准时默认选它**。 |
| **HTTP Request Tool** | `.toolHttpRequest` | Agent 需直接编排的单个外部 HTTP API。复用服务商预定义的 credential，覆盖原生节点未暴露的操作。 |
| **MCP Client Tool** | `.mcpClientTool` | 已有维护良好的 MCP server 覆盖该需求，或希望一个已发布的工作流服务多个 Agent。 |

还有用于纯内联计算的 **Custom Code Tool**（`.toolCode`），但它的运行时契约（字符串进 / 字符串出，无 `$fromAI`，无 `$helpers`）由 **n8n-code-tool** Skill 负责。编写之前先读那份文档。经验法则：如果你发现自己在代码里想用 `$fromAI()`，那就该改用 `.toolWorkflow`。

### `$fromAI()`：Agent 如何填充工具参数

需要 Agent 自行决定的工具参数用 `$fromAI()` 包裹。它是**真正的 n8n 表达式辅助函数**，用在工具节点的参数表达式里：


```
={{ $fromAI('paramName', 'what to put here — be specific: format, range, example', 'string') }}
```


- **paramName**：模型内部使用的名称（snake_case 或 camelCase，保持一致）。
- **description**：告诉模型要生成什么值。**它是提示词的一部分**，要像写 JSDoc 那样写。
- **type**（可选）：`'string'`（默认）、`'number'`、`'boolean'`、`'json'`。类型不符的值会导致调用失败。
- **defaultValue**（可选）：模型省略该参数时使用。

`$fromAI()` 只承载 JSON，**不能承载二进制**（不能传 base64，也不能传文件字节）。也并非每个参数都得用 `$fromAI`：身份、权限上限、关联 ID（`userId`、退款上限、`sessionId`）应从工作流上下文确定性地接入，让 Agent 既拿不错、甚至看不到它们。完整结构以及「给 Agent 一个按钮，而不是方向盘」的模式 → **TOOLS.md**。

---

## 系统提示词与工具描述

| 归入**系统提示词** | 归入**工具描述** |
|---|---|
| 人设、角色、语气 | 这个具体工具做什么 |
| 全局输出/格式规则（"respond in markdown"） | 何时用它、何时用别的工具 |
| 拒答 / 安全行为 | 每个参数的含义与形态 |
| 展示约定（图片用 `![]()`） | 好调用与坏调用的示例 |
| 通用上下文（通过 `$now` 取当前日期、用户角色） | 工具专属的坑（速率限制、边界情况） |
| 工具间流程（"after generating, always display"） | 工具专属的输入转换 |

为什么这样拆分：描述完善的工具在**任何**放入它的 Agent 里都能用；工具细节只在模型考虑该工具时才「加载」（token 效率）；你只需改一处工具描述，而不必翻动埋在 5000-token 提示词里的段落。 → **SYSTEM_PROMPT.md**

---

## 结构化输出：何时用、怎么用

当下游需要严格 JSON 而非自由文本时，加一个 `outputParserStructured` 子节点（接 `ai_outputParser`）。两条规则：

1. **用 `schemaType: 'manual'` 搭配真正的 JSON Schema，别用 `jsonSchemaExample`。** 示例无法表达必填与可选、枚举、数值范围或数组约束，形状一旦稍复杂就不够用。只有临时用完即弃的形状才用 `fromJson` + 示例。
2. **`autoFix: true` 搭配具备代码能力的修复模型。** 把*第二个*模型接入解析器的 `ai_languageModel` 插槽。按 schema 修复残缺 JSON 是写代码的任务，弱修复模型只会再产出一次格式错误的重试并白白烧掉 token。

→ **STRUCTURED_OUTPUT.md**：schema 模式、那句起决定作用的 "DO NOT wrap in markdown" 重试行，以及解析失败的处理手册。

---

## 记忆：简要心智模型

记忆是一个子节点（`ai_memory`）。没有它，每次调用都是无状态的，这对一次性任务（分类、摘要）正合适。有了它，Agent 就能维持对话，键取自你绑定到 `sessionKey` 的表达式。

- **`memoryBufferWindow`**：按 key 保留最近 N 轮交互，并通过 n8n 的存储跨执行持久化。聊天的默认选择。**`contextWindowLength` 默认只有 5，偏低**，50 才是更合理的起点。超出窗口的消息会彻底消失。
- **`memoryPostgresChat` / `memoryRedisChat`**：仅在记忆必须到 Agent *外部*被读取时使用（自有 UI、分析、跨系统）。仅为扛住重启并不需要它们，BufferWindow 已经能做到。

**始终从触发器向记忆接入一个稳定的 key。** 聊天触发器会自动填入 `sessionId`；其他入口则自行推导（Slack `thread_ts`、webhook 的会话 ID）。绝不硬编码 `sessionId: 'default'`，也绝不把 `sessionId` 放到 `$fromAI` 后面（模型会凭空编一个 UUID）。 → **MEMORY.md**

---

## 二进制数据与 Agent 边界

这是最容易让人栽跟头的接缝：

- **模型能看到上传的图片**（视觉），途径是 Agent 上的 `options.passthroughBinaryImages: true`。
- **工具不能接收二进制。** `$fromAI()` 只传 JSON，不能传 base64，也不能传字节，即便经由非 AI 绑定也一样。
- **Agent 的输出是文本形态**（或经解析器的结构化文本）。当模型返回图像/音频/视频字节时，Agent 根本不会把它们呈现出来，下游无从找回。

**变通办法：** 在 Agent 运行前把上传文件预先暂存到存储，把存储 key 注入系统提示词，让工具以字符串参数接收该 key 并在内部重新取回。一次性媒体生成则跳过 Agent，直接调用服务商的原生单次调用节点。

二进制的具体机制（用哪个存储、如何暂存、如何重新取回）由 **n8n-binary-and-data** 负责，参见它的 Agent 工具二进制参考。本 Skill 只标出边界，机制不在此重新推导。

---

## 人工审核（为破坏性工具加闸门）

当工具的效果需要在执行前由人工签字确认时（发送、付款、退款、账户变更），用审核工具节点把它包起来：`slackHitlTool`、`discordHitlTool`、`telegramHitlTool`、`gmailHitlTool` 等（n8n 称这些为 "Hitl" / human-in-the-loop）。审核节点在 `ai_tool` 连接上位于包装工具与 Agent **之间**：包装工具 → 审核节点 → Agent。

是否需要签字确认属于产品/策略决策，**把问题摆到用户面前**，依据影响范围给出建议，由用户拍板。

**关键规则：展示包装工具将收到的真实参数。** 在审批消息里使用字面量 `{{ $tool.parameters.<name> }}`，绝不用 `$fromAI()` 的转述，否则人工批准的是模型编造的文字，而非即将触发的调用。 → **HUMAN_REVIEW.md**

---

## 聊天 Agent（Slack、Discord、Teams、Telegram）

**无论复杂度如何，唯一不可妥协的一条：** 任何会发回复、由聊天触发的工作流都必须**过滤掉机器人自身的用户 ID**，否则它自己的回复会再次触发自身，陷入无限循环，白白消耗运行次数和 token。触发器支持过滤时优先用触发器级过滤（Slack Trigger 的 `options.userIds` 是**排除列表**，把机器人 ID 放进去）；否则在触发器后的第一个节点里过滤 `$json.user !== '<BOT_USER_ID>'`。

除过滤之外，简单机器人（触发器 → Agent → 回复）放在一个工作流里就够了。只有当需要加载态体验、子 Agent、多入口复用或健壮的错误处理时，才拆成 **shell + core + sub-agents**：

- **Shell**：触发器、防循环过滤、事件类型 Switch、加载/错误体验、渲染回复。不含 LLM。
- **Core**：无状态 Agent，`chatInput` + `threadId` 输入，记忆以 `threadId` 为键，外加工具与子 Agent。
- **Sub-agents**：各自负责一个窄领域，通过 `.toolWorkflow` 调用，**无状态**（完整上下文放在 `chatInput` 里）。

→ **CHAT_AGENT_PATTERNS.md**：各入口语义、以 thread 为 session，以及完整拓扑。

---

## 持久化 n8n Agent（n8n_manage_agents）

**持久化 n8n Agent** 与上文讲的 AI Agent 节点是两种不同的产物：它是一条独立的助手记录，包含 model、instructions、tools、skills、tasks、memory、channels，由 n8n 自身存储并做版本管理，通过 `n8n_manage_agents`（n8n 的实例级 MCP server）管理，而不是工作流 JSON 里的某个节点。

| 你的需求… | 使用 |
|---|---|
| 工作流内部的一个推理步骤，用 `ai_*` 子节点接线 | **AI Agent 节点**（本 Skill，见上文） |
| 拥有自身生命周期（草稿、验证、发布、版本、渠道）、独立于任何单个工作流的独立助手 | **持久化 Agent**（`n8n_manage_agents`） |

**前置条件：** 配好 `N8N_MCP_ACCESS_TOKEN`（与 Public API key 分开），且 n8n 为 **2.34+** 并启用 agents 模块。**每一项**操作都需要该 token，包括 `reference`/`search`，没有它什么都跑不起来。另外，`reference` 和 `search` 对**任何** Agent 都有效，不论其是否暴露给 MCP；其余所有操作都要求目标 Agent 已暴露给 MCP（通过此工具创建的 Agent 会自动暴露，暴露门槛只对本工具接触之前就已存在的 Agent 有影响）。

**构建顺序：**
1. `action: "reference"`：先读配置 schema 和确切的 mutate 操作，先于其他一切。
2. `action: "discover_assets"`：列出该 Agent 实际能接上的资源。接收 `projectId`（来自 `n8n_list_catalog({kind: "projects"})`）和 `kind`：`models`（带 `provider`）、`integrations`、`workflows`、`subagents` 或 `mcpServers`。每种 kind 各调一次。
3. `action: "create"`：`projectId`、`name`、`config`。
4. `action: "mutate"`：每次调用只改一种资源（`config.patch`、`skill.upsert`/`delete`、`task.upsert`/`delete`、`customTool.upsert`/`delete`），一律把**最新**的 hash 往后带。留意两个名字：n8n 以 `configHash` 返回它，却要求以 `args.baseConfigHash` 回传。`args` 原样转发给 n8n，任何字段名差一点都会返回 `INVALID_ARGS`，而不是给出有用的纠正，这正是第 1 步先读 schema 的原因。hash 过期会返回 `STALE_CONFIG`，重新 `get` 后用新的再试。
5. `action: "validate"`：在提供 `call` 或 `publish` 之前进行。
6. `action: "publish"`：**仅在用户明确要求时**执行，绝不主动发布。

`action: "call"` 用真实凭据和真实工具运行该 Agent，是一次真实执行，不是试跑。结果里可能带 `approvals[]`，对应需要人工决断的工具调用；**绝不替用户批准**，把它们摆出来，等用户决定后再继续。

**自定义工具是第三种代码运行时，别混用另外两种。** `customTool.upsert` 的正文是 **TypeScript**，且只允许导入 `@n8n/agents` 和 `zod`。它既不是 Code 节点（JavaScript/Python，返回 `[{json: …}]`），也不是 **n8n-code-tool** 所讲的 AI-agent Custom Code Tool（`@n8n/n8n-nodes-langchain.toolCode`，返回字符串，没有 `$fromAI()`）。这里最容易犯的错就是拿错契约，因为三者都是「写一段供 Agent 调用的代码」。动手之前先用 `action: "reference"` 读清结构；编译失败或未知的 `agentId` 都会以 `AGENT_TOOL_ERROR` 呈现。

**凭据注意：** 在 n8n 2.36.x 上，agents 运行时会拒绝 `azureOpenAiApi` 和 `aws` 凭据（报为 `missing: ["credential"]`）；响应的 `hint` 会列出可接受的类型。

**测试不留垃圾：** 临时 Agent 用 `[TEST] …` 命名，用完就 `delete` 掉。持久化 Agent 比创建它的会话活得更久，不像工作流可以留着不启用。

→ **n8n-mcp-tools-expert** `## Agents`：该工具的完整操作列表与错误码。

---

## RAG（检索增强生成）

n8n 自带 LangChain 的 RAG 基础组件（文档加载器、切分器、embeddings、向量存储、检索器）。有两点值得先讲明：

1. **先排除更省成本的查询方式。** 精确查找 → 数据库或 Data Table 查询，不用 RAG。要求新鲜度 → 实时搜索工具。文档集小且结构化 → 给 Agent 配 list/fetch 工具。只有当文档多到列不完、且查询是语义性的，才动用向量存储。
2. **把向量存储接成检索工具**（`mode: 'retrieve-as-tool'`、`ai_tool`），让 Agent 自行判断何时需要检索，并自己组织查询措辞。查询和文档用**同一个**模型做 embedding。

→ **RAG.md**（刻意写得薄，默认做法取决于数据形态与规模）。

---

## 参考文件

| 文件 | 何时阅读 |
|---|---|
| **TOOLS.md** | 新增工具、在四种类型间取舍、编写名称/描述、`$fromAI` 结构剖析 |
| **SUBWORKFLOW_AS_TOOL.md** | 通过 `.toolWorkflow` 把子工作流接成工具，区分由 Agent 填充的参数与确定性接入的参数 |
| **SYSTEM_PROMPT.md** | 编写/重构系统提示词，系统提示词与工具描述的拆分 |
| **STRUCTURED_OUTPUT.md** | 强制 JSON 输出、配置 autoFix、修复模型、解析失败的修复 |
| **MEMORY.md** | 选择记忆类型、持久化、sessionId 处理 |
| **HUMAN_REVIEW.md** | 加入人工审批、审批消息内容、多通道审批人 |
| **CHAT_AGENT_PATTERNS.md** | 构建 Slack/Discord/Teams/Telegram 机器人、shell + core + sub-agents 拓扑 |
| **RAG.md** | 检索增强型 Agent（刻意从简） |
| **EXAMPLES.md** | 具体节点对象片段：无状态 Agent 核心、Slack 路由 shell、领域子 Agent |

---

## 反模式

| 反模式 | 问题所在 | 修复 |
|---|---|---|
| 泛泛的工具名（`tool1`、`doStuff`、`runQuery`） | 模型分不清该选哪个工具，跳过它们或臆造参数 | 用动词开头、具体的名字：`Search customer database`、`Generate image with Veo` |
| 空描述或只有一行的工具描述 | 模型不知道何时调用，选错却不报错 | 写真正的描述：做什么、何时用、每个参数什么意思 |
| 把每个工具的说明都塞进系统提示词 | 提示词膨胀、无法复用、工具说明被埋没 | 把工具专属说明挪进工具描述 |
| 用 Agent + Switch 对自然语言做路由 | 本该 Text Classifier 一个节点搞定，却用了两个节点加提示词样板代码 | 改用 Text Classifier，每个类别都有独立的输出句柄（名称**和**描述都要有） |
| 把图像/音频/视频生成套进 Agent | 二进制既穿不过工具，也到不了 Agent 输出 | 直接调用服务商的原生单次调用节点 |
| `outputParserStructured` 不带 `autoFix` | 一次格式错误的响应就让工作流停摆 | `autoFix: true` + 具备代码能力的修复模型 |
| 把二进制直接传给工具 | 行不通，二进制无法跨越工具边界 | 预先暂存到存储，只传 key；参见 **n8n-binary-and-data** |
| 硬编码 `sessionId` / 没有 sessionId / 把 `sessionId` 放到 `$fromAI` 后 | 对话串线，或模型凭空编造 UUID | 从触发器向记忆和工具接入稳定的 key |
| 两个几乎一样的工具 | 选择结果不确定，模型容易混淆 | 合成一个工具，由参数驱动内部分支 |
| 聊天机器人没有机器人用户过滤 | 自己的回复会再次触发自身 → 无限循环 | 在触发器或第一个节点排除机器人用户 ID |
| 多工具 Agent 把 `maxIterations` 留在很低的默认值 | 「Max iterations reached」/ 空输出 | 调高 `options.maxIterations` |
| 用 `$fromAI()` 填人工审核消息 | 审批人签字确认的是转述，而非真实调用 | 使用字面量 `{{ $tool.parameters.<name> }}` |

---

## 社区版 MCP 做不到的事

| 想做的事 | 实际情况 |
|---|---|
| 以交互方式端到端聊天测试工作流里的 AI Agent 节点 | `n8n_test_workflow` 能运行工作流，但针对该节点做真正的多轮聊天会话是 UI 操作（canvas chat tester）。相比之下，持久化 Agent 可以通过 `n8n_manage_agents` 的 `call` 实时运行，见上文「持久化 n8n Agent」。 |
| 设置凭据的真实密钥值 | `n8n_manage_credentials` 能创建/更新凭据记录，但服务商的密钥本身要在 UI 里录入和验证。 |
| 指定工作流的 Error Workflow | 仅限 UI，参见 **n8n-error-handling**。把兜底流程建好，再把 UI 步骤交给用户。 |
| 锁定每个实例确切可用的模型 | 模型列表随版本变动，`search_nodes`/`get_node` 反映的是已安装的内容。到目标实例上核实。 |

MCP **能**做的事：搜索并查看每一个 LangChain 节点（`search_nodes`、`get_node`），校验节点配置与整张图（`validate_node`、`validate_workflow`），构建和修补 Agent 及其子节点（`n8n_update_partial_workflow`，在 `ai_*` 输出上用 `addConnection`），测试（`n8n_test_workflow`），以及拉取已保存的 JSON 核对接线（`n8n_get_workflow`）。深度 AI-agent 指南还放在 `tools_documentation({topic: "ai_agents_guide", depth: "full"})` 里。

---

## 与其他 Skill 的协作

- **n8n-workflow-patterns**（`ai_agent_workflow.md`）：「Agent 在工作流里」的宏观形态。本 Skill 是深入版；架构先看那份。
- **n8n-mcp-tools-expert**：节点类型格式（`get_node` 用短格式，JSON 里用长格式）与工具选择指引。任何 MCP 调用前先查阅。
- **n8n-node-configuration**：Agent 与子节点上由 `displayOptions` 驱动的字段；Slack/Block Kit 消息形态（`NODE_FAMILY_GOTCHAS.md` 的 Slack 小节）。
- **n8n-expression-syntax**：`{{ }}`、`$json.output`、`$now` 以及 `$fromAI`/`$tool.parameters` 都依赖正确的表达式语法。
- **n8n-code-tool**：Custom Code Tool 的运行时契约（字符串进/出，没有 `$fromAI`）。写 `.toolCode` 之前先读。
- **n8n-subworkflows**：`.toolWorkflow` 所依托的子工作流原语（Execute Workflow Trigger 的输入/输出、命名、先搜索再构建）。
- **n8n-binary-and-data**：负责 Agent 工具二进制边界的机制（暂存上传、返回生成的文件）。
- **n8n-validation-expert**：解读 `validate_workflow` 结果，包括 AI 连接问题（工具接进 `main` 而非 `ai_tool` 会被标成未连接）。
- **n8n-error-handling**：工具子工作流与 Agent 核心调用上的 `onError: 'continueErrorOutput'`；聊天 shell 的错误体验。
- **n8n-code-javascript / n8n-code-python**：用于工具子工作流*内部*的 Code 节点逻辑（与 Code Tool 的沙箱不同）。

---

## 速查清单

发布上线 Agent 之前：

- [ ] **选对节点**：工具/记忆/多轮用 Agent；路由用 Text Classifier；抽字段用 Information Extractor；媒体用原生节点
- [ ] **Model** 已通过 `ai_languageModel` 接入
- [ ] **每个工具**都有动词开头的具体名称，以及真正的描述
- [ ] **`$fromAI()` 的 description** 足够具体（格式、范围、示例）；身份/上限/sessionId 用确定性方式接入，不经过 `$fromAI`
- [ ] **每个工具的说明**放在工具描述里，而非系统提示词
- [ ] 系统提示词里用了 **`$now`**（不硬编码日期）
- [ ] 多工具 Agent 已调高 **`maxIterations`**
- [ ] **Memory** 以来自触发器的稳定 `sessionKey` 为键（不是 `'default'`，不经过 `$fromAI`）；`contextWindowLength` 从 5 调高
- [ ] **结构化输出**：`schemaType: 'manual'` + `autoFix: true` + 具备代码能力的修复模型
- [ ] **破坏性工具**已包进人工审核；审批消息用 `$tool.parameters`，不用 `$fromAI`
- [ ] **聊天机器人**过滤机器人自身的用户 ID（触发器级或第一个节点）
- [ ] **二进制**：模型视觉走 `passthroughBinaryImages`；工具只拿存储 key，绝不拿字节
- [ ] 已用 `validate_workflow` **校验**、用 `n8n_get_workflow` **核实**（子节点接在 `ai_*`，不是 `main`）

---

**记住**：Agent 的上限取决于它的工具名称、描述，以及对系统提示词的克制。模型看不到你的接线，它看到的只有一段系统提示词和一串带名称、带描述的工具。把这些当 API 来设计，「Agent 不听话」的问题大多就消失了。
