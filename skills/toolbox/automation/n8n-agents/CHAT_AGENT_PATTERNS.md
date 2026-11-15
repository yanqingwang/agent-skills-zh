> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-agents/CHAT_AGENT_PATTERNS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 聊天 Agent 模式：shell + 核心 + 子代理

面向外部聊天渠道：Slack、Discord、Microsoft Teams、Telegram、嵌入式 webhook 聊天。基础构件（记忆、工具、子工作流作工具、结构化输出）在各自的参考文档里；本文件讲生产级聊天 Agent 最终演化成的**多工作流组合**，以及其它参考文档没写的聊天渠道坑。

---

## 唯一不可妥协的事：防循环过滤

**任何会回复消息的聊天触发工作流，必须在触发器之后立刻过滤掉机器人自己的用户 ID，否则它会永远触发自己**：每条回复都会再触发一次运行，直到被速率限制或 n8n 并发上限拦住（还可能把 n8n 一起拖垮）。这是**每一个**机器人的最低要求，无论简单还是复杂。

**触发器支持的话，优先在触发器层过滤**：这样循环在任何下游节点运行之前就被切断。各渠道语义不同，请对照你的版本核实：

- **Slack**（`n8n-nodes-base.slackTrigger`）：`options.userIds` 是**排除列表**，列出的用户在工作流运行前就被丢弃。把机器人的用户 ID 放这里。（已核对触发器源码：命中时经 `if (userIds.includes(event.user))` 提前返回。）
- **Telegram**（`n8n-nodes-base.telegramTrigger`）：`additionalFields.userIds` 是**包含 / 白名单**（只有列出的用户才触发）。它不是机器人排除过滤器；而且 Telegram 机器人默认看不到自己的消息，所以通常不需要防循环。白名单用来把私用机器人限制给特定的人。
- **Discord、Teams**：没有原生的用户级触发器过滤，用下游 Filter 节点。

Slack 触发器级示例：

```json
{
  "parameters": {
    "trigger": ["message"],
    "channelId": { "__rl": true, "mode": "list", "value": "<CHANNEL_ID>" },
    "options": { "userIds": "={{ [\"<BOT_USER_ID>\"] }}" }
  },
  "type": "n8n-nodes-base.slackTrigger"
}
```

触发器没有可用的排除过滤时，触发器之后的第一个节点必须丢弃机器人自己的 ID：

```json
{
  "parameters": {
    "conditions": {
      "conditions": [
        {
          "leftValue": "={{ $json.user }}",
          "rightValue": "<BOT_USER_ID>",
          "operator": { "type": "string", "operation": "notEquals" }
        }
      ]
    }
  },
  "type": "n8n-nodes-base.filter"
}
```

机器人用户 ID 来自机器人授权信息里的 API ID（Slack 的 `bot_user_id`、Discord 的 application ID、Teams 的 `botId`）。

---

## 什么时候拆成 shell + 核心 + 子代理

除了防循环过滤，**简单机器人（一个触发器 → 一个 Agent → 一条回复，加上过滤）**放在单个工作流里完全没问题。shell + 核心 + 子代理的拆分是为生产健壮性服务的，满足以下任一条才算值回成本：

- 机器人需要加载状态 UX（输入中提示、reaction、占位消息），以及超出单条消息的优雅错误处理。
- 它从不止一个渠道被调用（Slack 和 Discord）。
- 有些专属领域不该由 Agent 内联承担（Notion 数据库 schema、CRM 自定义字段、Linear 标签）。
- Agent 或其工具会跨工作流复用。

都不满足就留在单个工作流（过滤照旧）。确定要拆时的形状：

```
[chat-surface workflow]  ──►  [agent core workflow]  ──►  [sub-agent workflows]
("the shell")                 ("the brain")               ("specialists")

- Trigger from the surface    - Stateless                 - One narrow domain each
- Anti-loop filter            - chatInput + threadId       - chatInput only
- Routing / event types       - Memory keyed on threadId   - Their own tools + model
- Loading + error UX          - Tools, sub-agents
- Render the reply            - No surface concerns
```

Slack 路由 shell 和领域子代理片段见 **EXAMPLES.md**。

---

## shell

接收聊天事件，决定是否回应，管理 UX，调用核心，渲染回复。不做推理，没有 LLM。

### 按事件类型 Switch

同一个触发器会收到消息、reaction、提及、斜杠命令、按钮点击。在防循环过滤之后放一个 Switch，把每类事件路由到对应处理：

```
"owner message"            → Execute Workflow: agent-core
"owner reaction"           → no-op (or a reaction handler)
"unknown user"             → canned reply
"slash command: /summary"  → Execute Workflow: summary-command
"button click"             → Execute Workflow: interaction-handler
```

每个分支是独立的子工作流，因为路由决策和具体工作是不同的关注点（不同模型、超时、记忆形态）。加一个斜杠命令意味着一个 Switch 输出 + 一个子工作流，而不是新的顶层触发器。

Slack 专属说明（payload 形状会变：硬编码取值路径前先用真实事件核实）：reaction/提及作为 Events API 事件流经 Slack Trigger；**斜杠命令和 Block Kit 按钮点击通常不会**（Slack 把它们投递到单独的 Request URL）。用一个喂给同一个 Switch 的第二个 Webhook 节点接入，或用社区的 Socket Mode 节点。斜杠命令带 `command` 字段；Block Kit 交互以 `type === 'block_actions'` 和 `actions` 数组到达。

### 加载状态 UX

没有反馈时，用户会以为什么都没发生。模式：**在调用 Agent 前加加载指示，并在每条退出路径上移除它，包括错误路径。**

```
[Trigger] → [Filter bot] → [Switch]
   → (owner message)
   → [Add loading reaction]                  (:spinner:, etc.)
   → [Execute Workflow: Agent core]   onError: 'continueErrorOutput'
        ├── (success) → [Remove reaction] → [Send reply]
        └── (error)   → [Remove reaction] → [Send error message with link]
```

错误路径最容易忘：没有它，指示会永远挂着，用户以为机器人还在干活。Execute Workflow 节点上的 `onError: 'continueErrorOutput'` 启用第二个分支（→ **n8n-error-handling**）。Discord/Telegram 的输入中提示有时限；长时间运行的 Agent 先发一条占位消息，再编辑它。

### 用 thread 做会话延续

把渠道的 thread 原语用作记忆的 `sessionKey`：

```json
"workflowInputs": {
  "value": {
    "chatInput": "={{ $('Filter bot').item.json.text }}",
    "threadId":  "={{ $('Filter bot').item.json.thread_ts || $('Filter bot').item.json.ts }}"
  }
}
```

`thread_ts || ts` 是 Slack 的标准写法：thread 里的回复带 `thread_ts`（指向父消息），父消息本身只有 `ts`。回退到 `ts` 让父消息成为其 thread 的会话键，于是每个 thread 都是新会话，记忆不会跨 thread 串线。**单用用户 ID、频道 ID 或工作区 ID 都是错的：它们会跨会话。**发送回复时指向同一个 thread（`otherOptions.thread_ts.replyValues.thread_ts` = 同一个 `thread_ts || ts`）。

### 错误 UX：告知用户，不要挂死

错误分支发送一条短消息，附失败执行的链接：

```
There was a workflow error. https://<n8n-host>/workflow/<id>/executions/{{ $execution.id }}
```

`$execution.id` 是错误触发那一刻的实时执行 ID。主机名要按环境参数化。

---

## Agent 核心

一个子工作流，声明两个输入：`chatInput`（用户消息）和 `threadId`（渠道的 thread/会话 ID）。返回 Agent 的最终输出：字符串、结构化对象，或渠道专属信封（Block Kit、adaptive card）。

除了 **MEMORY.md** 之外，聊天场景唯一的特殊接线是把 `threadId` 直接接到 `sessionKey`：

```json
"sessionIdType": "customKey",
"sessionKey": "={{ $json.threadId }}"
```

`threadId` 从触发器 →（透传节点）→ 记忆一路流动。不要把它放进 `$fromAI`。

按执行变化的上下文（用户身份、附件文件）放进 Agent 前面的 Set 节点，并模板进系统提示词（→ **SYSTEM_PROMPT.md** 的 "file-handling injection" 和 "piecing"）。不要凭猜测加 Set 节点：在 `systemMessage` 里内联就够了，直到真的出现复用。

**Block Kit / adaptive cards：给 Agent 配上 `outputParserStructured`**（→ **STRUCTURED_OUTPUT.md**）。“用 `schemaType: 'manual'` 配真实 JSON Schema”的指导在这里更要紧：Block Kit 和 adaptive cards 依赖跨块类型的 `oneOf` 联合类型，外加每个块自己的枚举（`style` 等），`jsonSchemaExample` 一个都表达不了，会生成看似笃定却错误的块树，被渠道拒收。

### Block Kit 信封的坑（Slack）

Agent 返回 Block Kit 并通过 Slack 节点的 `blocksUi` 发送时，值必须是 `{ "blocks": [...] }` 形状的对象，其中是**真数组**：不能只传数组，也不能传字符串化后的：

```
✅ ={{ { "blocks": $('Call Agent core').item.json.output.blocks } }}
❌ ={{ $('Call Agent core').item.json.output.blocks }}
```

只传数组会**静默**失败：Slack 节点接受输入，消息发出但没有任何富内容，也不报错或警告。→ **n8n-node-configuration** 的 `NODE_FAMILY_GOTCHAS.md`（Slack 一节）。

---

## 子代理（Agent 当工具用）

子代理是独立的工作流，有自己的 Agent 节点，由路由 Agent 经 `.toolWorkflow` 调用。满足以下条件时值得建一个：

- 领域里有一套路由层不该携带的 schema/枚举（Notion 数据库属性、Linear 标签、CRM 字段）。
- 领域工具超过 5 个，会塞满路由层的工具列表。
- 能力被不止一个路由层复用。
- 领域值得用与路由层不同（更便宜、更快）的模型。

**契约是无状态的。**路由层把完整请求放进 `chatInput`：不共享记忆，没有隐式上下文。在两侧同时强化：工具描述（路由层侧）和子代理的系统提示词（被调方侧）：

> IMPORTANT: This tool is stateless. Send all relevant context in a single message. If you need to create an entry, include ALL required fields upfront.

没有这句话，路由层会假设存在隐式上下文，子代理只能靠猜。子工作流作工具的其余接线内容 → **SUBWORKFLOW_AS_TOOL.md**。

### 新鲜 schema 注入

领域 schema 会在运行时变化时（Notion 数据库选项演进、Linear 团队加标签），每次子代理调用都重新拉取，而不是硬编码：

```
[Execute Workflow Trigger]
   ↓
[Notion: Get Database]                  # fetches the live schema
   ↓
[Agent]   system prompt template includes:
   ## Database Schema
   {{ $('Get a database').first().json.properties.toJsonString() }}
```

每次调用多一次 API 请求；换来的是子代理不会因为提示词过期而返回“该属性不存在”。对低频聊天助手值得。高频热点路径则把 schema 缓存进带 TTL 的 Data Table。

---

## 反模式

| 反模式 | 会出什么问题 | 修法 |
|---|---|---|
| shell 顶部没有机器人用户 ID 过滤 | 机器人自己的消息再次触发工作流，无限循环 | 触发器级排除（Slack 的 `options.userIds`），或先加一个 `$json.user !== '<BOT_USER_ID>'` 的 Filter |
| 把机器人 ID 放进 Telegram 的 `userIds` 并期待排除效果 | 它是**白名单**：只有机器人会触发，人类全被挡住；看似"修好了"，实则静默 | Telegram 机器人看不到自己的消息；`userIds` 只用来给人类设白名单 |
| 加载指示只在成功路径移除 | 任何出错之后，用户看到机器人永远卡在"思考中" | `onError: 'continueErrorOutput'` + 两条分支都移除 |
| 用用户/频道/工作区 ID 当会话键 | 同一频道里不同 thread 的对话互相串线 | 用 thread 原语（Slack 的 `thread_ts || ts`） |
| 已需要多渠道/子代理/复用时仍用单个工作流 | 无法复用，UX 混进推理逻辑，难以独立测试 | 拆成 shell + 核心 + 子代理（只在需求真实时才拆） |
| 子代理读写共享记忆 | 调用方无法推断行为，也不能安全重试 | 子代理必须无状态：完整上下文放进 `chatInput` |
| 子代理提示词里硬编码领域 schema | schema 会过时，子代理之后会选到失效选项 | 运行时重新拉取并模板进提示词 |
| 把裸 blocks 数组传给 `blocksUi` | Slack 发出空消息，无报错 | 包成 `{ "blocks": [...] }`，用真数组 |

---

## 交叉引用

- 工具命名、描述、`$fromAI` → **TOOLS.md**
- `.toolWorkflow` 形态与参数映射 → **SUBWORKFLOW_AS_TOOL.md**
- 按执行的上下文、文件注入、提示词存储 → **SYSTEM_PROMPT.md**
- 解析器配置、autoFix、修正模型 → **STRUCTURED_OUTPUT.md**
- 记忆类型、`sessionKey` 持久化 → **MEMORY.md**
- `onError: 'continueErrorOutput'` 与错误 UX → **n8n-error-handling**
- Slack 节点参数形状（Block Kit）→ **n8n-node-configuration** 的 `NODE_FAMILY_GOTCHAS.md`（Slack 一节）
- 各渠道接收上传文件 / 返回生成文件 → **n8n-binary-and-data**
