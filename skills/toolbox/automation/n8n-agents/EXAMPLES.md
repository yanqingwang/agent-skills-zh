> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-agents/EXAMPLES.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 示例

三个实用的节点对象（node-object）片段，对应 shell + 核心 + 子代理 的拓扑。这些是**社区 n8n JSON 片段**，供改造使用，不是可直接导入的完整导出：凭据 ID、工作流 ID、频道/机器人 ID 都是占位符。用 `n8n_update_partial_workflow` 搭建（在 `ai_*` 输出上执行 `addNode` + `addConnection`），再用 `n8n_get_workflow` 和 `validate_workflow` 验证。

这些片段所属的架构见 **CHAT_AGENT_PATTERNS.md**。

---

## 1. 无状态 Agent 核心

一个可复用的 Agent 子工作流：输入 `chatInput` + `threadId`，输出 Agent 结果。记忆以 `threadId` 为键，带原生工具、一个子代理工具，以及带 autoFix 修正模型的 Block Kit 结构化输出。这就是被 shell 调用的"大脑"。

```json
{
  "name": "Chat agent core",
  "nodes": [
    {
      "parameters": {
        "workflowInputs": {
          "values": [{ "name": "chatInput" }, { "name": "threadId" }]
        }
      },
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "typeVersion": 1.1,
      "position": [-480, -96],
      "id": "core-trigger",
      "name": "When Executed by Another Workflow"
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "={{ $json.chatInput }}",
        "hasOutputParser": true,
        "options": {
          "systemMessage": "=You are a concise, direct assistant. Be a thinking partner, not an answer machine.\n\nCurrent date: {{ $now.format('DDDD') }}\n\n## Output\nYou are replying in Slack using Block Kit. Your entire response must be valid JSON with a 'blocks' array at the root. Bold is *single asterisks*. Links are <https://url|text>. Max 10 blocks.\n\n## Tool usage\nFact-check verifiable claims with the web search tool before answering. Use the idea database manager for anything about content ideas.",
          "maxIterations": 50
        }
      },
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 3.1,
      "position": [-48, -96],
      "id": "core-agent",
      "name": "AI Agent"
    },
    {
      "parameters": { "model": "anthropic/claude-opus-4.6", "options": { "temperature": 0.1 } },
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
      "typeVersion": 1,
      "position": [-288, 192],
      "id": "core-main-llm",
      "name": "Main LLM",
      "credentials": { "openRouterApi": { "id": "REPLACE_OPENROUTER_CRED", "name": "OpenRouter" } }
    },
    {
      "parameters": {
        "sessionIdType": "customKey",
        "sessionKey": "={{ $json.threadId }}",
        "contextWindowLength": 50
      },
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "typeVersion": 1.3,
      "position": [-128, 192],
      "id": "core-memory",
      "name": "Simple Memory"
    },
    {
      "parameters": {
        "descriptionType": "manual",
        "toolDescription": "Search the web fast to fact-check a claim or find a source. Use for verifying anything from training data.",
        "query": "={{ $fromAI('query', 'The search query, phrased to match relevant sources', 'string') }}",
        "options": { "search_depth": "fast" }
      },
      "type": "@tavily/n8n-nodes-tavily.tavilyTool",
      "typeVersion": 1,
      "position": [32, 192],
      "id": "core-web-search",
      "name": "Search the web",
      "credentials": { "tavilyApi": { "id": "REPLACE_TAVILY_CRED", "name": "Tavily" } }
    },
    {
      "parameters": {},
      "type": "@n8n/n8n-nodes-langchain.toolCalculator",
      "typeVersion": 1,
      "position": [192, 192],
      "id": "core-calc",
      "name": "Calculator"
    },
    {
      "parameters": {
        "description": "Manages the content-ideas database. Use for ANY task about content ideas: querying, creating, dedupe-checks.\n\nIMPORTANT: This tool is stateless. Send all relevant context in a single message. If creating, include ALL required fields upfront. Returns the page URL for anything referenced or created.",
        "workflowId": { "__rl": true, "value": "REPLACE_SUBAGENT_WF_ID", "mode": "list", "cachedResultName": "Notion ideas sub-agent" },
        "workflowInputs": {
          "mappingMode": "defineBelow",
          "value": { "chatInput": "={{ $fromAI('chatInput', 'The full request to the ideas database, with all context', 'string') }}" },
          "schema": [
            { "id": "chatInput", "displayName": "chatInput", "type": "string", "display": true, "canBeUsedToMatch": true }
          ]
        }
      },
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "typeVersion": 2.2,
      "position": [352, 192],
      "id": "core-idea-tool",
      "name": "Idea database manager"
    },
    {
      "parameters": {
        "schemaType": "manual",
        "inputSchema": "{ \"type\": \"object\", \"properties\": { \"text\": { \"type\": \"string\" }, \"blocks\": { \"type\": \"array\", \"items\": { \"oneOf\": [ { \"type\": \"object\", \"properties\": { \"type\": { \"const\": \"header\" }, \"text\": { \"type\": \"object\" } }, \"required\": [\"type\", \"text\"] }, { \"type\": \"object\", \"properties\": { \"type\": { \"const\": \"section\" }, \"text\": { \"type\": \"object\" } }, \"required\": [\"type\", \"text\"] }, { \"type\": \"object\", \"properties\": { \"type\": { \"const\": \"divider\" } }, \"required\": [\"type\"] } ] } } }, \"required\": [\"text\", \"blocks\"] }",
        "autoFix": true
      },
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "typeVersion": 1.3,
      "position": [560, 176],
      "id": "core-parser",
      "name": "Structured Output Parser (Block Kit)"
    },
    {
      "parameters": { "model": "anthropic/claude-sonnet-4.6", "options": { "temperature": 0 } },
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
      "typeVersion": 1,
      "position": [620, 336],
      "id": "core-fixer-llm",
      "name": "Fixer LLM (coding-capable)",
      "credentials": { "openRouterApi": { "id": "REPLACE_OPENROUTER_CRED", "name": "OpenRouter" } }
    }
  ],
  "connections": {
    "When Executed by Another Workflow": { "main": [[{ "node": "AI Agent", "type": "main", "index": 0 }]] },
    "Main LLM": { "ai_languageModel": [[{ "node": "AI Agent", "type": "ai_languageModel", "index": 0 }]] },
    "Simple Memory": { "ai_memory": [[{ "node": "AI Agent", "type": "ai_memory", "index": 0 }]] },
    "Search the web": { "ai_tool": [[{ "node": "AI Agent", "type": "ai_tool", "index": 0 }]] },
    "Calculator": { "ai_tool": [[{ "node": "AI Agent", "type": "ai_tool", "index": 0 }]] },
    "Idea database manager": { "ai_tool": [[{ "node": "AI Agent", "type": "ai_tool", "index": 0 }]] },
    "Structured Output Parser (Block Kit)": { "ai_outputParser": [[{ "node": "AI Agent", "type": "ai_outputParser", "index": 0 }]] },
    "Fixer LLM (coding-capable)": { "ai_languageModel": [[{ "node": "Structured Output Parser (Block Kit)", "type": "ai_languageModel", "index": 0 }]] }
  }
}
```

要点：

- **记忆以 `threadId` 为键**，不是用户/频道 ID（那会跨会话串线）。`threadId` 由 shell 提供。
- **`maxIterations: 50`**：比低默认值调高，因为这个 Agent 每轮要串联多个工具。
- **系统提示词里的 `$now.format('DDDD')`**：不硬编码日期。
- **两个模型**：主模型挂在 Agent 上，另一个可写代码的修正模型接到解析器。两者都走 `ai_languageModel`，但接到不同节点。
- Agent 上的 **`hasOutputParser: true`** 激活 `ai_outputParser` 槽位。
- 子代理工具的描述里重复强调 **"This tool is stateless"**（此工具无状态）：路由层不能依赖共享上下文。

---

## 2. Slack 路由 shell

"shell"：触发器、触发器级防循环过滤、事件类型 Switch、加载 reaction、带错误分支的 Agent 核心调用，以及 Block Kit 回复信封。这里没有 LLM。

```json
{
  "name": "Slack chat router",
  "nodes": [
    {
      "parameters": {
        "trigger": ["message"],
        "watchWorkspace": true,
        "options": { "userIds": "={{ [\"U00000000BOT\"] }}" }
      },
      "type": "n8n-nodes-base.slackTrigger",
      "typeVersion": 1,
      "position": [-288, 48],
      "id": "shell-trigger",
      "name": "Slack Trigger",
      "credentials": { "slackApi": { "id": "REPLACE_SLACK_CRED", "name": "Slack" } }
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": { "version": 3 },
                "conditions": [{ "leftValue": "={{ $json.user === \"U00000000OWNER\" && $json.type === \"message\" }}", "rightValue": "", "operator": { "type": "boolean", "operation": "true", "singleValue": true } }],
                "combinator": "and"
              },
              "renameOutput": true, "outputKey": "Owner message"
            },
            {
              "conditions": {
                "options": { "version": 3 },
                "conditions": [{ "leftValue": "={{ $json.user !== \"U00000000OWNER\" && $json.type === \"message\" }}", "rightValue": "", "operator": { "type": "boolean", "operation": "true", "singleValue": true } }],
                "combinator": "and"
              },
              "renameOutput": true, "outputKey": "Unknown user"
            }
          ]
        }
      },
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.4,
      "position": [-32, 48],
      "id": "shell-switch",
      "name": "Switch"
    },
    {
      "parameters": {
        "resource": "reaction",
        "channelId": { "__rl": true, "value": "={{ $json.channel }}", "mode": "id" },
        "timestamp": "={{ $json.ts }}",
        "name": "spinner"
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.4,
      "position": [240, -64],
      "id": "shell-add-reaction",
      "name": "Add Loading Reaction",
      "credentials": { "slackApi": { "id": "REPLACE_SLACK_CRED", "name": "Slack" } }
    },
    {
      "parameters": {
        "workflowId": { "__rl": true, "value": "REPLACE_AGENT_CORE_WF_ID", "mode": "list", "cachedResultName": "Chat agent core" },
        "workflowInputs": {
          "mappingMode": "defineBelow",
          "value": {
            "chatInput": "={{ $('Slack Trigger').item.json.text }}",
            "threadId": "={{ $('Slack Trigger').item.json.thread_ts || $('Slack Trigger').item.json.ts }}"
          },
          "schema": [
            { "id": "chatInput", "displayName": "chatInput", "type": "string", "display": true },
            { "id": "threadId", "displayName": "threadId", "type": "string", "display": true }
          ]
        }
      },
      "type": "n8n-nodes-base.executeWorkflow",
      "typeVersion": 1.3,
      "position": [480, -64],
      "id": "shell-call-core",
      "name": "Call Agent core",
      "retryOnFail": true,
      "maxTries": 2,
      "waitBetweenTries": 5000,
      "onError": "continueErrorOutput"
    },
    {
      "parameters": {
        "resource": "reaction",
        "operation": "remove",
        "channelId": { "__rl": true, "value": "={{ $('Switch').item.json.channel }}", "mode": "id" },
        "timestamp": "={{ $('Switch').item.json.ts }}",
        "name": "spinner"
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.4,
      "position": [720, -160],
      "id": "shell-remove-reaction-ok",
      "name": "Remove Loading Reaction (success)",
      "credentials": { "slackApi": { "id": "REPLACE_SLACK_CRED", "name": "Slack" } }
    },
    {
      "parameters": {
        "select": "user",
        "user": { "__rl": true, "value": "={{ $('Slack Trigger').item.json.user }}", "mode": "id" },
        "messageType": "block",
        "blocksUi": "={{ { \"blocks\": $('Call Agent core').item.json.output.blocks } }}",
        "otherOptions": {
          "thread_ts": { "replyValues": { "thread_ts": "={{ $('Slack Trigger').item.json.thread_ts || $('Slack Trigger').item.json.ts }}" } }
        }
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.4,
      "position": [960, -160],
      "id": "shell-send-reply",
      "name": "Send Block Kit reply",
      "credentials": { "slackApi": { "id": "REPLACE_SLACK_CRED", "name": "Slack" } }
    },
    {
      "parameters": {
        "select": "user",
        "user": { "__rl": true, "value": "={{ $('Slack Trigger').item.json.user }}", "mode": "id" },
        "text": "=There was a workflow error. https://<your-n8n-host>/workflow/<this-workflow-id>/executions/{{ $execution.id }}",
        "otherOptions": {
          "thread_ts": { "replyValues": { "thread_ts": "={{ $('Slack Trigger').item.json.thread_ts || $('Slack Trigger').item.json.ts }}" } }
        }
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.4,
      "position": [720, 64],
      "id": "shell-send-error",
      "name": "Send error message with execution link",
      "credentials": { "slackApi": { "id": "REPLACE_SLACK_CRED", "name": "Slack" } }
    }
  ],
  "connections": {
    "Slack Trigger": { "main": [[{ "node": "Switch", "type": "main", "index": 0 }]] },
    "Switch": { "main": [[{ "node": "Add Loading Reaction", "type": "main", "index": 0 }], []] },
    "Add Loading Reaction": { "main": [[{ "node": "Call Agent core", "type": "main", "index": 0 }]] },
    "Call Agent core": {
      "main": [
        [{ "node": "Remove Loading Reaction (success)", "type": "main", "index": 0 }],
        [{ "node": "Send error message with execution link", "type": "main", "index": 0 }]
      ]
    },
    "Remove Loading Reaction (success)": { "main": [[{ "node": "Send Block Kit reply", "type": "main", "index": 0 }]] }
  }
}
```

要点：

- **触发器级防循环**：`options.userIds: ["U00000000BOT"]` 是排除列表，机器人自己发的消息根本进不了工作流。不需要单独的过滤节点。
- **`Call Agent core`** 设置了 `onError: 'continueErrorOutput'`，所以 `main[1]` 承载错误分支（→ **n8n-error-handling**）。加载 reaction 在成功路径移除；错误分支给出一个链接，而不是永远挂着。
- **`threadId`** = `thread_ts || ts`，直接管道传入核心（核心以它作记忆键）。
- **`blocksUi`** 是 `{ "blocks": [...] }` 信封，不是裸数组：裸数组会静默失败。

---

## 3. 领域子代理（Notion ideas）

由核心经 `.toolWorkflow` 调用的专职子代理。它每次调用都重新拉取数据库 schema，运行在比路由层更便宜的模型上。

```json
{
  "name": "Notion ideas sub-agent",
  "nodes": [
    {
      "parameters": { "workflowInputs": { "values": [{ "name": "chatInput" }] } },
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "typeVersion": 1.1,
      "position": [-240, 0],
      "id": "sub-trigger",
      "name": "When Executed by Another Workflow"
    },
    {
      "parameters": {
        "resource": "database",
        "databaseId": { "__rl": true, "value": "REPLACE_NOTION_DB_ID", "mode": "id" },
        "simple": false
      },
      "type": "n8n-nodes-base.notion",
      "typeVersion": 2.2,
      "position": [-32, 0],
      "id": "sub-get-db",
      "name": "Get a database",
      "credentials": { "notionApi": { "id": "REPLACE_NOTION_CRED", "name": "Notion" } }
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "={{ $('When Executed by Another Workflow').item.json.chatInput }}",
        "options": {
          "systemMessage": "=You manage a Notion ideas database. Query and create idea entries.\n\n## Database schema (fetched fresh this call)\n{{ $('Get a database').first().json.properties.toJsonString() }}\n\n## Rules\n1. Always respond in chat with the result.\n2. Always return the Notion URL for any page created or referenced.\n3. Select/multi-select values must EXACTLY match an existing schema option.\n4. IMPORTANT: you are stateless. If information is missing, list exactly what's needed and remind the caller to resend the complete request with all details.",
          "maxIterations": 15
        }
      },
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 3.1,
      "position": [208, 0],
      "id": "sub-agent",
      "name": "AI Agent"
    },
    {
      "parameters": { "model": "anthropic/claude-haiku-4.6", "options": { "temperature": 0.1 } },
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
      "typeVersion": 1,
      "position": [112, 256],
      "id": "sub-llm",
      "name": "Sub-agent LLM (cheaper than router)",
      "credentials": { "openRouterApi": { "id": "REPLACE_OPENROUTER_CRED", "name": "OpenRouter" } }
    },
    {
      "parameters": {
        "descriptionType": "manual",
        "toolDescription": "Returns all ideas that are still active (not rejected, cancelled, or started).",
        "resource": "databasePage",
        "operation": "getAll",
        "databaseId": { "__rl": true, "value": "REPLACE_NOTION_DB_ID", "mode": "id" },
        "returnAll": true,
        "filterType": "manual",
        "filters": { "conditions": [{ "key": "Status|status", "condition": "does_not_equal", "statusValue": "Rejected" }] }
      },
      "type": "n8n-nodes-base.notionTool",
      "typeVersion": 2.2,
      "position": [304, 256],
      "id": "sub-get-active",
      "name": "Get active ideas",
      "credentials": { "notionApi": { "id": "REPLACE_NOTION_CRED", "name": "Notion" } }
    },
    {
      "parameters": {
        "descriptionType": "manual",
        "toolDescription": "Creates an idea entry. Always enters as status 'Idea'. Select fields must match schema options exactly.",
        "resource": "databasePage",
        "databaseId": { "__rl": true, "value": "REPLACE_NOTION_DB_ID", "mode": "id" },
        "title": "={{ $fromAI('Title', 'Short title of the idea', 'string') }}",
        "propertiesUi": {
          "propertyValues": [
            { "key": "Status|status", "statusValue": "Idea" },
            { "key": "Type|select", "selectValue": "={{ $fromAI('type', 'Type column; must EXACTLY match a schema option', 'string') }}" }
          ]
        }
      },
      "type": "n8n-nodes-base.notionTool",
      "typeVersion": 2.2,
      "position": [480, 256],
      "id": "sub-create",
      "name": "Create idea",
      "credentials": { "notionApi": { "id": "REPLACE_NOTION_CRED", "name": "Notion" } }
    }
  ],
  "connections": {
    "When Executed by Another Workflow": { "main": [[{ "node": "Get a database", "type": "main", "index": 0 }]] },
    "Get a database": { "main": [[{ "node": "AI Agent", "type": "main", "index": 0 }]] },
    "Sub-agent LLM (cheaper than router)": { "ai_languageModel": [[{ "node": "AI Agent", "type": "ai_languageModel", "index": 0 }]] },
    "Get active ideas": { "ai_tool": [[{ "node": "AI Agent", "type": "ai_tool", "index": 0 }]] },
    "Create idea": { "ai_tool": [[{ "node": "AI Agent", "type": "ai_tool", "index": 0 }]] }
  }
}
```

要点：

- **新鲜 schema 注入**：`Get a database` 在 Agent **之前**运行（在 `main` 上），其 `properties` 经 `.toJsonString()` 模板进系统提示词。子代理从不在过期 schema 上工作，因此选不到上周刚改名的 select 选项。
- **更便宜的模型**（`claude-haiku-4.6`），低于路由层：专注单一领域的子代理用不着编排者的模型。
- **无状态契约**在系统提示词里重申，与核心侧的工具描述对应。
- **`maxIterations: 15`**：对专注的子代理够用（对比宽泛路由层的 50）。
- `Status|status` / `Type|select` 的键形如 Notion 的 `Name|type` 约定；以线上实际 schema 为准。

---

## 交叉引用

- 这些片段适配的拓扑 → **CHAT_AGENT_PATTERNS.md**
- `.toolWorkflow` 映射 → **SUBWORKFLOW_AS_TOOL.md**
- Block Kit schema 与 autoFix → **STRUCTURED_OUTPUT.md**
- 核心调用上的错误分支 → **n8n-error-handling**
