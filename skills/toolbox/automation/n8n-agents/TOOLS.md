> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-agents/TOOLS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Agent 工具

Agent 选择工具只靠读**名称**和**描述**，没有别的。两者都是提示词的一部分。把工具设计当 API 设计来做：它做什么、何时用、每个参数什么含义、失败时什么样。

---

## 四种工具类型

### 1. 原生工具节点

常规节点的预制工具版：`slackTool`、`gmailTool`、`googleSheetsTool`、`toolCalculator`、`notionTool`、`httpRequestTool` 等。与非工具版完全一样，区别只是参数可以经 `$fromAI()` 由 Agent 填。

- **优点**：配置最少、经过充分测试、体验原生。
- **缺点**：一个节点 = 一个操作。多步逻辑放不下。
- **适用**：能力能干净地对应到一个节点、一个操作。

原生节点缺某个操作、或需要非标准参数形状时，把 **HTTP Request Tool** 指向该服务的 API，并用该服务的*预定义凭据类型*：复用已有的 OAuth/API-key 凭据，拿到完整 API。

### 2. 子工作流作工具（`@n8n/n8n-nodes-langchain.toolWorkflow`）

超过一个节点时的默认选择。任何工作流都变成带类型 `$fromAI()` 输入的工具。

- **优点**：工具里可用 n8n 的全部能力：分支、错误处理、子子工作流、原生节点、自定义逻辑。跨 Agent 复用。可独立测试。
- **缺点**：多一层工作流边界，略增延迟。
- **适用**：超过一个节点、逻辑可能被复用，或需要可测试性。

构建 Agent 能力的 n8n 正统做法。→ **SUBWORKFLOW_AS_TOOL.md**

### 3. HTTP Request Tool（`@n8n/n8n-nodes-langchain.toolHttpRequest`）

HTTP Request 节点的包装，把它的参数暴露给 Agent。

- **优点**：一个节点让任何 HTTP API 变成工具。
- **缺点**：仅限 HTTP。鉴权/重试/错误处理要自己接线。
- **适用**：调用一个需要 Agent 直接编排的单一外部 API。

一点须知：HTTP Request 有自己的 HTTP 层超时（默认 5 分钟），慢端点要调高 `options.timeout`。Agent 工具本身没有超时，工具跑多久 Agent 就等多久。把它指向比如 Notion API（用 Notion 预定义凭据），Agent 就能自己拼路径、方法和请求体，覆盖原生节点没暴露的操作。代价是 Agent 开始亲自写 API 请求，更容易出错，需要足够强的模型，以及描述里清晰的端点指导。影响面随之扩大：确保用户理解这一点。

### 4. MCP Client Tool（`@n8n/n8n-nodes-langchain.mcpClientTool`）

把 Agent 接到任何 MCP 服务器。两种形态：

- **外部 MCP 服务器**：任何第三方或自托管 MCP（GitHub、Linear、Notion、内部自建）。一个节点暴露该服务器提供的全部工具。
- **n8n 托管 MCP**：同一实例上开启 MCP 访问并发布的工作流。同一个客户端节点，指向 n8n MCP 触发器 URL。让一个工作流服务多个 Agent。

- **缺点**：工具描述与形状来自服务器，质量参差，也不好调。鉴权与可达性自己负责。
- **适用**：已有维护良好的 MCP 服务器覆盖该能力，或想让一个发布的工作流服务多个 Agent。

### 另外：Custom Code Tool（`@n8n/n8n-nodes-langchain.toolCode`）

纯内联计算（数学、解析、格式化）。它的运行时契约是**字符串进 / 字符串出，不能用 `$fromAI`，不能用 `$helpers`**，归 **n8n-code-tool** 这个 Skill 管：写之前先读它。经验法则：想在代码里用 `$fromAI()`，说明你想要的其实是 `.toolWorkflow`。

---

## 决策：用哪种工具类型？

```
Capability the agent needs?
├── One native node + one operation does it
│     → native tool node
├── Native node missing an op / needs custom params for ONE API
│     → HTTP Request Tool (with the service's predefined credential)
├── More than one node, or logic that might be reused
│     → Sub-workflow as tool (.toolWorkflow)   ← default when in doubt
├── Pure deterministic computation, one-off, inline
│     → Custom Code Tool (.toolCode)            ← see n8n-code-tool
└── A maintained MCP server covers it / publish n8n logic to many agents
      → MCP Client Tool
```

---

## `$fromAI()`：Agent 如何填工具参数

`$fromAI()` 是**真实的 n8n 表达式助手**，写在工具节点的参数表达式里。该由 Agent 决定的参数就用它包起来：

```
sendTo:  ={{ $fromAI('recipient', 'Email address of the recipient', 'string') }}
subject: ={{ $fromAI('subject', 'Email subject line, concise and informative', 'string') }}
body:    ={{ $fromAI('body', 'Email body in plain text, professional tone', 'string') }}
```

形态：`$fromAI(paramName, description, type?, defaultValue?)`

- **paramName**：模型内部使用的名称。snake_case 或 camelCase，保持一致。
- **description**：要产生什么值。**提示词的一部分。**写具体：格式、范围、示例。
- **type**：`'string'`（默认）、`'number'`、`'boolean'`、`'json'`。有强制校验：类型不对的值会让调用失败。
- **defaultValue**：模型省略该参数时使用。

它只能携带 **JSON**：不能携带二进制（没有 base64、没有文件字节），即使经非 AI 绑定也不行。二进制请传存储键字符串，让工具自己去取（→ **n8n-binary-and-data**）。

好描述与无用描述对比：

```
✅ ={{ $fromAI('imageName', 'Storage key for an existing image to edit, or empty for a new generation. Use the exact key shown in the system prompt; do not reconstruct or guess.', 'string') }}

❌ ={{ $fromAI('imageName', 'image name', 'string') }}   // useless to the model
```

把 `$fromAI` 描述当 JSDoc 对待：模型靠它们弄清该传什么。

---

## 管道参数：Agent 不该决定的东西藏起来

不是每个参数都得用 `$fromAI`。任何参数都可以从工作流上下文确定性填充，而且**管道传入的值对 Agent 不可见**：不在工具 schema 里，也不受模型产出的任何内容影响：

```
reason:        ={{ $fromAI('reason', 'Why the user is requesting a refund', 'string') }}   // agent-filled
customerId:    ={{ $('Chat Trigger').first().json.user.id }}                                 // hidden
maxRefund:     ={{ $('Get user tier').first().json.refundLimit }}                            // hidden
idempotencyKey:={{ $('Chat Trigger').first().json.sessionId }}                               // hidden
```

凡是 Agent 不能搞错、也不该看到的，都用管道传入：

- **身份**：`userId`、`customerId`、已鉴权操作者、租户范围。
- **权限上限**：退款上限、等级标志、允许的地区。
- **关联 ID**：`sessionId`、幂等键、trace ID。

**给 Agent 一个按钮，而不是方向盘。**最强形态是一个**零 `$fromAI` 参数**的敏感工具："Refund order" 工具的 `orderId` 来自触发器，`amount` 来自取回的订单记录，`actor` 来自会话，全部管道传入。Agent 在物理上不可能退错订单，它只决定是否按下。需要确定性参数加人工签核的操作，配合 **HUMAN_REVIEW.md** 使用。

---

## 工具名与描述即提示词

模型每一轮都在跑的选择流程：

1. 拿到系统提示词、对话和工具列表。
2. 对每个工具读名称 + 描述 + 参数 schema（含 `$fromAI` 描述）。
3. 挑出描述与它要做的事最匹配的工具。

**差的名字和描述导致差的选择，而且通常无声。**模型就是不调你的工具，或者调了别的工具、参数一塌糊涂。没有报错。

### 命名：动词开头，足够具体

| 好 | 差 | 原因 |
|---|---|---|
| `Search customer database` | `query` / `tool1` | 泛化名字什么都没说 |
| `Generate image with Veo` | `imageGen` | 哪个生成器？ |
| `Edit existing image` | `edit` | 编辑什么？ |
| `Send Slack message to channel` | `slack` | 说出动作，不只说渠道 |
| `Lookup user by email` | `getUser` | 怎么查？ |

### 描述：三个部分

1. **它做什么**（一句话）。
2. **何时用它**（一两句，带边界 / 示例）。
3. **参数说明**（只在 `$fromAI` 描述没覆盖时写）。

```
Edit existing image: Modifies an image the user already uploaded, based on a prompt.
Use when the user uploaded an image and asks for changes (color, style, composition, content).
Do NOT use for generating new images from scratch — use Generate Image for that.
The imageName parameter must be the storage key of the existing image as listed in your
available files; do not pass the original filename or a URL.
```

这段描述承担了本会撑大系统提示词的工作：这正是它的意义。

---

## 工具描述即模块化提示词

凡是关于*如何调用这个工具*的具体内容，都放进工具描述，不放进系统提示词：

| 在系统提示词里（移出去） | 更该放在工具描述里 |
|---|---|
| "When generating images, prefer realistic photography over `8k cinematic`" | `Generate Image`: "Default to realistic photography aesthetics…" |
| "If the search tool returns nothing, summarize politely" | `Search`: "Returns up to 10 results; if empty, report 'no matches' rather than retrying broader" |
| "Use 9:16 for video tools" | `Generate Video`: "Defaults to 9:16; pass `aspectRatio: '16:9'` for landscape" |

三个理由：**可复用**（工具自己教会每个新 Agent 怎么用它）、**token 效率**（每工具的指导只在模型考虑该工具时加载，不是每轮都加载）、**可维护**（一份描述，而不是一段埋没的段落）。

---

## 粒度：一个带分支的工具，而不是两个几乎相同的工具

在几乎相同的工具之间做选择，模型会犯迷糊。如果两个工具内部约 80% 相同：

- **一个工具加一个分支参数。**`Generate Image` 与 `Edit Image` 共享大部分逻辑 → 合并成一个，用 `imageName` 参数区分（空 = 生成，有值 = 编辑）。
- **只有真正不同且描述能明确区分时才用两个工具。**`Send DM` 与 `Send Channel Message` 是不同的。

---

## 运维注意事项

- **maxIterations。**Agent 有可配置的工具调用上限（`options.maxIterations`），默认值**很低**。串联调用的多工具 Agent 会撞上限，表现为 "max iterations reached" 或空输出。调高它，并准备兜底：不要指望优雅恢复。
- **工具调用成本。**每次调用至少多一次模型往返。高频工具应返回**精简**结果：臃肿的返回烧 token 很快。
- **工具失败处理。**希望 Agent 收到错误字符串而不是中断的，在工具子工作流上设置 `onError: 'continueErrorOutput'`；Agent 可以重试、换工具或上报。→ **n8n-error-handling**。

---

## 交叉引用

- 子工作流工具模式详解 → **SUBWORKFLOW_AS_TOOL.md**
- 系统提示词与工具描述的分工 → **SYSTEM_PROMPT.md**
- 给工具传二进制 → **n8n-binary-and-data**
- Custom Code Tool 的契约 → **n8n-code-tool**
