> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-code-tool/INPUT_SCHEMA.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Code Tool 的输入 Schema（结构化模式）

如何把 `@n8n/n8n-nodes-langchain.toolCode` 变成 **DynamicStructuredTool**，让 LLM 传带类型的参数，而不是自由格式的字符串。

---

## 为什么要用 schema？

没有 schema 时，Code Tool 是 LangChain 的 `DynamicTool`：
- LLM 看到的是："一个叫 query 的字符串参数"
- LLM 发来什么你都得自己解析
- 拼错、缺字段、类型错，都成了你运行时的问题

有 schema 时，Code Tool 变成 `DynamicStructuredTool`：
- LLM 看到的是：带命名字段和描述的带类型对象
- 运行时在你的代码跑之前就拒绝无效调用
- 数值字段保持数值（不用再对每个字段写 `Number(params.price)`）
- 工具调用更可靠——多数现代 LLM 处理结构化工具，比"给你个 JSON 字符串自己看着办"更在行

**代价**：定义 schema 要一点配置，且节点版本必须支持该功能。

---

## 启用 schema

在 `toolCode` 参数上设 `specifyInputSchema: true`。两种 schema 定义风格：

### 风格 A：`fromJson`（粘一个代表性示例，v≥1.3，推荐）

最简单。给 n8n 一个示例 JSON，它替你推断 schema。

```json
{
  "parameters": {
    "name": "calculate_car_loan",
    "description": "Computes monthly car-loan payment using an annuity formula with optional balloon.",
    "language": "javaScript",
    "specifyInputSchema": true,
    "schemaType": "fromJson",
    "jsonSchemaExample": "{\n  \"price\": 439900,\n  \"down_payment\": 87980,\n  \"interest_rate\": 6.95,\n  \"months\": 36,\n  \"residual_percent\": 50,\n  \"setup_fee\": 695,\n  \"monthly_admin_fee\": 59\n}",
    "jsCode": "// query is now a validated OBJECT, not a string\nconst { price, down_payment, interest_rate, months, residual_percent, setup_fee = 0, monthly_admin_fee = 0 } = query;\n\nconst principal = price - down_payment;\nconst residual  = price * (residual_percent / 100);\nconst r = interest_rate / 100 / 12;\nconst growth = Math.pow(1 + r, months);\nconst base = r === 0\n  ? (principal - residual) / months\n  : (principal - residual / growth) * r / (1 - 1 / growth);\nconst monthly_payment = base + monthly_admin_fee;\n\nreturn JSON.stringify({\n  monthly_payment_sek: Math.round(monthly_payment),\n  loan_amount: Math.round(principal)\n});"
  },
  "type": "@n8n/n8n-nodes-langchain.toolCode",
  "typeVersion": 1.3,
  "name": "calculate_car_loan"
}
```

**工作原理**：n8n 看示例，推断出 `{price: number, down_payment: number, ...}`，生成一份 JSON Schema。LLM 看到这份 schema，传过来的是校验过的对象。

### 风格 B：`manual`（自己写 JSON Schema）

需要逐字段描述、枚举、min/max 约束或可选字段时用它。

```json
{
  "parameters": {
    "name": "calculate_car_loan",
    "description": "Computes monthly car-loan payment.",
    "language": "javaScript",
    "specifyInputSchema": true,
    "schemaType": "manual",
    "inputSchema": "{\n  \"type\": \"object\",\n  \"required\": [\"price\", \"down_payment\", \"interest_rate\", \"months\", \"residual_percent\"],\n  \"properties\": {\n    \"price\": { \"type\": \"number\", \"description\": \"Car price in SEK\" },\n    \"down_payment\": { \"type\": \"number\", \"description\": \"Down payment in SEK\" },\n    \"interest_rate\": { \"type\": \"number\", \"description\": \"Annual nominal rate in percent, e.g. 6.95\" },\n    \"months\": { \"type\": \"integer\", \"minimum\": 1, \"description\": \"Loan term in months\" },\n    \"residual_percent\": { \"type\": \"number\", \"minimum\": 0, \"maximum\": 99, \"description\": \"Balloon as % of price\" },\n    \"setup_fee\": { \"type\": \"number\", \"default\": 0 },\n    \"monthly_admin_fee\": { \"type\": \"number\", \"default\": 0 }\n  }\n}",
    "jsCode": "const { price, down_payment, interest_rate, months, residual_percent, setup_fee = 0, monthly_admin_fee = 0 } = query;\n// ... same computation as above ...\nreturn JSON.stringify({ monthly_payment_sek: /*...*/ });"
  },
  "type": "@n8n/n8n-nodes-langchain.toolCode",
  "typeVersion": 1.3,
  "name": "calculate_car_loan"
}
```

**什么时候值得用 `manual`**：
- 想要逐字段的 `description` 字符串（LLM 会读）
- 需要 `enum` 取值（如币种：`["SEK", "EUR", "USD"]`）
- 需要数值约束（`minimum`、`maximum`）
- 想干净地标记可选字段

---

## 有 schema 时 `query` 的行为

来自 ToolCode 沙箱的原始依据：

```typescript
const sandbox = new JsTaskRunnerSandbox(workflowMode, ctx, undefined, { query });
```

沙箱总是收到 `{ query }`。区别在于 `query` 里装的是什么：

| 模式 | `query` 的类型 | 怎么用 |
|---|---|---|
| 无 schema | `string` | 想要结构就 `JSON.parse(query)` |
| 有 schema | `object`（已校验） | 解构：`const { price, months } = query;` |

Python 同理：无 schema 时 `_query` 是字符串，有 schema 时是 dict。

---

## schema 的版本兼容性

- `specifyInputSchema` 与 `schemaType: "manual"` 加 `inputSchema`：v1.2 起可用
- `schemaType: "fromJson"` 加 `jsonSchemaExample`：需要 v≥1.3

要用 `fromJson` 就把节点设为 `typeVersion: 1.3`。旧安装请用 `manual`。

---

## 怎么选

```
Does your tool need more than one input field?
├─ No (just a URL, question, text blob)
│  └─ Unstructured — skip the schema
├─ Yes, and fields are all typed (numbers, bools, enums)
│  └─ Structured with fromJson (easiest)
├─ Yes, and you need constraints or rich descriptions
│  └─ Structured with manual
└─ Yes, and fields are complex / reusable across agents
   └─ Use toolWorkflow (sub-workflow tool) instead of toolCode
```

---

## 坑：schema 必须是合法 JSON

`jsonSchemaExample` 和 `inputSchema` 是**含 JSON 的字符串**，不是对象。粘进工作流 JSON 时小心转义。如果节点保存不了或 LLM 看不到字段，先单独校验一遍 JSON。

---

## 坑：改 schema 不会追溯修复旧的 Agent 运行

如果 Agent 已经带着无结构工具跑起来，你再切成结构化，Agent 的系统提示词在重新加载之前可能还反映旧契约。改完 schema 设置后，强制重跑 / 重开 Agent 节点。
