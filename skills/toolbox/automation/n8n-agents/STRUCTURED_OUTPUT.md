> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-agents/STRUCTURED_OUTPUT.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 结构化输出

没有商量余地：输出解析器必须**解析并且在失败时重试**。没有重试，一条格式错误的模型响应就能让整个工作流停摆。

解析器是 `@n8n/n8n-nodes-langchain.outputParserStructured` 节点，通过 `ai_outputParser` 连接接入 Agent（或 Basic LLM Chain）。

---

## 模式（节点对象）

解析器节点，带 `autoFix` 和它自己的修复模型：

```json
{
  "parameters": {
    "schemaType": "manual",
    "inputSchema": "{ \"type\": \"object\", \"properties\": { \"score\": { \"type\": \"integer\", \"minimum\": 1, \"maximum\": 5 }, \"reason\": { \"type\": \"string\" } }, \"required\": [\"score\", \"reason\"] }",
    "autoFix": true
  },
  "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
  "typeVersion": 1.3,
  "name": "Structured Output Parser"
}
```

解析器接到 Agent，再把**有编码能力的修复模型**接到解析器：

```json
"Structured Output Parser": {
  "ai_outputParser": [[{ "node": "AI Agent", "type": "ai_outputParser", "index": 0 }]]
},
"Fixer LLM": {
  "ai_languageModel": [[{ "node": "Structured Output Parser", "type": "ai_languageModel", "index": 0 }]]
}
```

在 Agent 上设 `hasOutputParser: true`，让该插槽生效。

---

## 为什么用 schema 而不是示例

`schemaType: 'manual'` 配一份真实 JSON Schema 是默认做法。`jsonSchemaExample`（`schemaType: 'fromJson'`）看着更简单，但示例**表达不了**：

- **必填与可选字段**，示例只是单个快照，解析器判断不了哪些键是必需的。
- **枚举**，`"category": "compliance"` 约束不了模型只能输出 `compliance | history | risk`，它会发明新类别。
- **数值范围**，`"score": 3` 说不了 `1-5`；模型返回 `7` 或 `0.85` 也照样通过。
- **数组约束**，最小/最大条数、条目类型一致性。
- **字符串格式**，邮箱、UUID、ISO 日期、正则。

schema 给模型更明确的规则，给解析器真正的校验：

```json
{
  "type": "object",
  "properties": {
    "decision":   { "type": "string", "enum": ["approve", "reject", "escalate"] },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "reasons": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "category": { "type": "string", "enum": ["compliance", "history", "risk"] },
          "weight":   { "type": "number", "minimum": 0, "maximum": 1 },
          "note":     { "type": "string" }
        },
        "required": ["category", "weight"]
      }
    },
    "follow_up_required": { "type": "boolean" }
  },
  "required": ["decision", "confidence", "reasons", "follow_up_required"]
}
```

只有在确定永远不会增加约束的一次性场景里才用 `fromJson` + `jsonSchemaExample`。一旦某个字段要变可选、加枚举或限范围，反正都得重写解析器，一开始就用 schema。

---

## `autoFix: true` 与修复模型

模型可能产出几乎对但不完全合法的 JSON：尾逗号、缺字段、类型错，或 JSON 被包进 markdown 代码块。没有 `autoFix`，工作流停摆。有了它，解析器把坏输出发给一个模型并附上"修一下"的提示词，重试后继续。

修复模型作为**独立的**子节点接进解析器的 `ai_languageModel` 插槽。**用有编码能力的模型**（Sonnet 级或更好）。对照带枚举、范围和必填字段的 schema 修补坏 JSON 是结构化输出/编码任务，弱模型或通用模型经常再产出一次格式错误的输出，白费力气还烧 token。

要自定义重试提示词时，设 `customizeRetryPrompt: true` 并提供 `prompt`。占位符 `{instructions}`、`{completion}`、`{error}` 在重试时填充：

```
Instructions:
--------------
{instructions}
--------------
Completion:
--------------
{completion}
--------------
Above, the Completion did not satisfy the constraints in the Instructions.
Error:
--------------
{error}
--------------
Please try again with an answer that satisfies the constraints.
This is a structured output parser tool in n8n. Ensure the output format is correct to pass parsing.
DO NOT wrap the output in a markdown code block.
```

一般保持重试提示词为默认，除非你有明确理由覆盖它。

---

## "DO NOT wrap the output in a markdown code block"

这一行是**承重的**。模型默认把 JSON 包进三反引号的 `json` 围栏，这会让解析器挂掉。如果你看到明显合法的 JSON 被包在代码块里导致解析失败，修法就是这句指令：重试提示词里要加，主模型若包装成瘾，**主**系统提示词里也要加：

> 当以结构化输出响应时，只返回裸 JSON。不要包进 markdown 代码块。JSON 前后不要带任何说明文字。

---

## 系统提示词 + 解析器：双保险

解析器告诉模型 schema；系统提示词也应当写明输出形状：

```
## Output Format
Respond with a JSON object matching this exact shape:
{ "score": 1-5 integer, "reason": "brief explanation" }

ONLY output the JSON. No prose, no markdown wrapping.
```

这是重复，但模型对系统提示词很当真，强化有用。漏网的由解析器兜住。

---

## 常见解析失败与修法

| 症状 | 可能根因 | 修法 |
|---|---|---|
| "Failed to parse output"，但文本看着像 JSON | 被包进 markdown 代码块 | 在重试提示词和系统提示词里加 "DO NOT wrap in markdown" |
| schema 期望有值的地方是空字段 | 模型以为未知字段可以省略 | 提示词写明："未知字段用空字符串 '' 或 null，绝不省略" |
| 类型不对（数字成了字符串） | schema/示例没有把类型写清 | 在 schema 里用真数字，不要用字符串 |
| JSON 被截断（花括号没闭合） | 响应中途达到 max tokens | 调大 max tokens，收紧提示词让输出更短 |
| 字段名被改写（"Score" vs "score"） | schema 没有钉死字段名 | 在系统提示词里写"字段名与所示完全一致" |
| `autoFix` 无限重试 | 修复模型对这份 schema 太弱 | 换成有编码能力的（Sonnet 级）修复模型；收紧重试提示词 |

---

## 什么时候不要用解析器

- **面向用户的自由聊天回复**，会话文本不需要解析。
- **只有工具调用、没有最终结构化输出**，用户可见的输出是文本时就跳过。
- **琐碎的键值提取**，一个 Set 节点加 `JSON.parse($json.output)` 就够。

解析器用于下游节点必须消费严格 JSON 的场合。

---

## 交叉引用

- 为什么用 Agent、在哪用 → 父级 **SKILL.md**
- 结构化输出的系统提示词那一半 → **SYSTEM_PROMPT.md**
- Block Kit / adaptive cards 更需要手写 schema（联合类型）→ **CHAT_AGENT_PATTERNS.md**
