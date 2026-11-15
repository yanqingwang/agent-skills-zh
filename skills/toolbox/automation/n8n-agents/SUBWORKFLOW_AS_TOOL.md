> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-agents/SUBWORKFLOW_AS_TOOL.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 子工作流作 Agent 工具

超过一个节点的工具，默认形态是 Tool Workflow 节点（`@n8n/n8n-nodes-langchain.toolWorkflow`）。任何子工作流都变成 Agent 可调用的工具，带类型的输入由 `$fromAI()` 填充。它能与 n8n 的所有优点组合：分支、错误处理、子工作流复用、原生节点、自定义逻辑。

子工作流原语本身（Execute Workflow Trigger 的输入输出、无状态设计、命名、先搜索再建）见 **n8n-subworkflows**；本参考只讲 *Agent 工具* 这个角度。

---

## 为什么这是 n8n 的默认选择

在原生 LangChain 里，工具是一个函数。在 n8n 里，工具可以是一整个工作流，因此它可以：

- 按输入分支（IF / Switch）。
- 调用多个 API 并聚合。
- 有自己的重试、兜底、错误处理。
- 调用其它子工作流。
- 读写 Data Table。
- 用 `n8n_test_workflow` 加 pinned 数据独立测试。
- 跨 Agent 和非 Agent 工作流复用。

函数式工具要做到这些，迟早也得长成工作流。n8n 直接把工作流原语给你。

---

## 形态：两半

### 1. 子工作流一侧：带类型输入的 Execute Workflow Trigger

```json
{
  "parameters": {
    "workflowInputs": {
      "values": [
        { "name": "imagePrompt", "type": "string" },
        { "name": "imageName",   "type": "string" },
        { "name": "sessionId",   "type": "string" }
      ]
    }
  },
  "type": "n8n-nodes-base.executeWorkflowTrigger",
  "typeVersion": 1.1,
  "name": "When Executed by Another Workflow"
}
```

每个声明过的输入都成为调用方可填的参数。**触发器必须用 "Define Below" 模式（带类型字段），不能用 passthrough**：passthrough 没有 schema，Agent 就没有可用 `$fromAI` 填的东西。两个例外：(a) 子工作流需要二进制数据（它不能直接当 Agent 工具：先落存储，把存储键作为带类型的字符串字段传递，见 **n8n-binary-and-data**）；(b) 工具完全不需要输入（passthrough 是唯一选项，工具唯一的决策是要不要调用）。

类型校验发生在 **Agent 一侧**，靠 `$fromAI` 的 `type` 参数，不在触发器。允许的类型：`string`、`number`、`boolean`、`json`。两边要匹配。

### 2. Tool Workflow 一侧：指向子工作流，绑定参数

```json
{
  "parameters": {
    "description": "Use to create a new image from a prompt OR edit an existing image. Pass imageName as the storage key (e.g. \"abc123.png\") to edit; leave empty to generate from scratch. Returns { imageUrl, imageKey }.",
    "workflowId": { "__rl": true, "value": "<sub-workflow-id>", "mode": "list" },
    "workflowInputs": {
      "mappingMode": "defineBelow",
      "value": {
        "imagePrompt": "={{ $fromAI('imagePrompt', 'Detailed prompt describing the desired image', 'string') }}",
        "imageName":   "={{ $fromAI('imageName', 'Storage key of an existing image to edit, or empty for new generation', 'string') }}",
        "sessionId":   "={{ $('Chat Trigger').first().json.sessionId }}"
      },
      "schema": [
        { "id": "imagePrompt", "displayName": "imagePrompt", "type": "string", "display": true },
        { "id": "imageName",   "displayName": "imageName",   "type": "string", "display": true },
        { "id": "sessionId",   "displayName": "sessionId",   "type": "string", "display": true }
      ]
    }
  },
  "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
  "typeVersion": 2.2,
  "name": "Generate or edit image"
}
```

用 `ai_tool` 接进 Agent：

```json
"Generate or edit image": {
  "ai_tool": [[{ "node": "AI Agent", "type": "ai_tool", "index": 0 }]]
}
```

映射按输入逐个来：

- **Agent 填**：`={{ $fromAI('paramName', 'description', 'string') }}`，由 Agent 决定。
- **管道传入**：`={{ $('SourceNode').first().json.field }}`，由你的工作流填。

`sessionId` 那一行是关键：它**不是** Agent 的决策。从触发器管道传入，让记忆和按会话键的工作保持一致。**绝不要把 `sessionId` 放进 `$fromAI`**：Agent 会编造一个 UUID。

---

## Agent 看到什么（以及看不到什么）

Agent 看到工具的**名称**（Tool Workflow 节点名）和**描述**（节点上的一个参数）：两者都遵循 **TOOLS.md** 的规则，具体、API 文档风格、当作提示词对待。

它**看不到**：子工作流内部、子工作流自己的名称，以及 `sessionId` 这类管道传入的值。只有 `$fromAI` 参数出现在工具 schema 里。因此你可以大幅重构子工作流，而不改变 Agent 看到的东西。

---

## 完整示例：一个工具，两种模式

目标：一个能生成或编辑图片的 Agent。两者共享大部分逻辑，唯一差别是要不要先下载已有图片。

```
[Execute Workflow Trigger: { imagePrompt, imageName, sessionId }]
   ↓
[Crypto: hash for new filename]
   ↓
[IF: imageName empty?]
   ├── empty (generate)     → [Gemini: generate] ──┐
   └── not empty (edit):                            │
       [S3: Download by imageName]                  │
          ↓                                         │
       [Gemini: edit with downloaded binary] ───────┤
                                                     ↓
                                            [S3: Upload result]
                                                     ↓
                                            [Set: { imageUrl, imageKey }]
```

Agent 通过往 `imageName` 里放什么来选模式。两个几乎相同的工具会让选择更难：合并成一个。

---

## 子工作流内部的模式

### 返回稳定形状（这是契约）

调用方收到的是最后一个节点的输出。选定一种形状，跨模式保持不变：

```json
{ "imageUrl": "https://...", "imageKey": "abc123.png" }
```

不要有时返回 `{ url, key }`，有时返回 `{ result: { url, key } }`。输出形状是每个调用方依赖的契约：Agent 把它当作提示词的一部分来读，确定性调用方把下游节点接到具体路径上。形状漂移会静默弄坏调用方。

对"预期内"的失败（搜索无结果），返回可分支的形状：

```json
{ "ok": false, "error": "no_results", "message": "No matches found for query" }
```

### 什么时候改为抛错：Stop and Error

对意外但需处理的错误（鉴权失败、上游宕机、不可恢复的输入），用带详细信息的 `Stop and Error` 节点。它以抛错的方式传播：Agent 看到工具错误，可以重试/换工具/上报；确定性调用方用 `onError: 'continueErrorOutput'` 接住。当结果是真错误而不是正常分支时，选它而不是 `{ ok: false }`。完整的错误处理体系（4xx/5xx 映射、重试、错误工作流）→ **n8n-error-handling**。

### 给易失败节点接上 `onError: 'continueErrorOutput'`

子工作流内部，易失败节点（HTTP、S3、DB）应设置 `onError: 'continueErrorOutput'` 并路由到干净错误响应，这样 Agent 和确定性调用方收到的都是结构化错误，而不是静默中断。

### 把输入契约当 API，写好文档

Execute Workflow Trigger 声明的输入就是这个工具的 API。写进子工作流的 `description`：

```
Generates or edits an image.
Inputs:
  imagePrompt (string, required): detailed image description.
  imageName   (string, optional): storage key of existing image to edit. Empty = new generation.
  sessionId   (string, required): chat session ID, used for storage keying.
Returns:
  { imageUrl, imageKey }
```

### 让工具子工作流可被找到

用统一前缀命名（`Subworkflow:` 或领域前缀）。Tool Workflow 节点按 ID（稳定）引用它们，但人是在 UI 里按名字找的。

---

## 独立测试子工作流

子工作流工具可以脱离 Agent 测试：

1. `n8n_test_workflow({workflowId, method: "prepare"})`：弄清哪些节点需要 pinned 数据。
2. 每个节点造一个样例 item，按节点**名称**为键，每个都包成 `{json: {...}}`。
3. `n8n_test_workflow({workflowId, method: "pinned", pinData})` 用这批数据运行并等待。
4. 确认输出形状与 Agent 将收到的一致。

routed 方法需要 `N8N_MCP_ACCESS_TOKEN` 和工作流的 "Available in MCP" 设置；默认的 `method: "auto"` 跑不了子工作流，它没有 HTTP 触发器。

---

## 什么时候不要用子工作流作工具

- **简单的单节点包装**："调用这个端点然后返回"用 HTTP Request Tool 更短。
- **只属于这个 Agent 的一次性纯代码逻辑**：几行别处不存在的纯 JS/Python，用 Custom Code Tool（`.toolCode`，见 **n8n-code-tool**）就够了。决策规则：可复用的业务逻辑 → 子工作流；一次性的 Agent 专属变换 → Code Tool。
- **已有原生工具节点的能力**：不要把 `slackTool` 包进子工作流。

其余情况，子工作流作工具就是默认选择。

---

## 交叉引用

- 四种工具类型概览 → **TOOLS.md**
- `$fromAI` 描述如何影响行为 → **TOOLS.md** 的 "`$fromAI()`"
- 子工作流原语（无状态设计、命名、I/O）→ **n8n-subworkflows**
- 给工具传二进制 → **n8n-binary-and-data**
- Custom Code Tool 的例外 → **n8n-code-tool**
