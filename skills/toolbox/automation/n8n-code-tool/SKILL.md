---
name: n8n-code-tool
description: "为 n8n 自定义代码工具（@n8n/n8n-nodes-langchain.toolCode）编写 JavaScript 或 Python，即 AI Agent 可调用的工具，而非工作流里的 Code node。适用于给 AI Agent 挂载代码工具、编写供 LLM 调用的代码、解析 `query` 输入、返回字符串结果、为结构化参数定义输入 schema（specifyInputSchema、jsonSchemaExample、DynamicStructuredTool），或排查诸如 \"Wrong output type returned\"、\"No execution data available\"、\"The response property should be a string, but it is an object\"、\"Cannot assign to read only property 'name'\" 之类的错误，以及 AI agent 拒绝调用该工具的情况。涵盖 Code node 与 Code Tool 之间的关键差异：返回格式（字符串 vs `[{json:{...}}]`）、Code Tool 沙箱中 `$fromAI`/`$input`/`$helpers` 不可用、供 AI 调用时的命名规则，以及何时改用 `toolWorkflow`/HTTP Request Tool。"
---

> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-code-tool/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# n8n Custom Code Tool

在 `@n8n/n8n-nodes-langchain.toolCode` 内编写代码的专业指南，该工具供 AI Agent 调用，**并非**常规工作流里的 Code node。

---

## ⚠️ 这不是 Code node

Custom Code Tool 在编辑器里看起来像 Code node：同样的 JavaScript 编辑器、相近的布局，但它来自不同的包，是一个**完全不同的节点**，有着**不同的运行时契约**。

| | Code node | Custom Code Tool |
|---|---|---|
| **节点类型** | `n8n-nodes-base.code` | `@n8n/n8n-nodes-langchain.toolCode` |
| **包** | `n8n-nodes-base` | `@n8n/n8n-nodes-langchain` |
| **调用方** | 上一个节点（工作流流程） | AI Agent（LangChain） |
| **输入** | `$input.all()`：条目流 | `query`：来自 LLM 的字符串或对象 |
| **返回值** | `[{json: {...}}]`（条目数组） | **一个字符串** |
| **`$fromAI()`** | N/A | **不可用**（见错误部分） |
| **HTTP 辅助** | `this.helpers.httpRequest`（鉴权辅助不可用） | 未向工具沙箱暴露 |
| **状态** | 每次运行的执行数据 | 无 `getContext`、无 `$getWorkflowStaticData` |

**若把它当成 Code node 来用，就会失败。** 本 Skill 余下部分讲解 Code Tool 的真实契约。

---

## 快速开始

### 最简 JavaScript Code Tool

```javascript
// `query` is whatever the AI sent (a string by default)
return `You asked: ${query}`;
```

### 最简 Python Code Tool

```python
# `_query` is whatever the AI sent (a string by default)
return f"You asked: {_query}"
```

### 核心规则

1. **返回字符串。** 数字会自动转换。其他任何类型都会抛出 `"The response property should be a string, but it is an object"`。
2. **输入变量是固定的**：`query`（JS）、`_query`（Python）。无法重命名。
3. **不要在 Code Tool 沙箱内使用 `$fromAI()`**，否则会抛出 `"No execution data available"`。
4. **不要使用 `[{json: {...}}]` 这种返回格式**，那是 Code node 用的。会抛出 `"Wrong output type returned"`。
5. **使用有描述性的工具名**（字母/数字/下划线，v1.1+）。Agent 按名称调用该工具。
6. **编写精确的描述**：LLM 据此决定是否调用该工具。

---

## 两种输入模式

Code Tool 有两种输入形态，由 `specifyInputSchema` 控制：

### 模式 1：非结构化（默认，`specifyInputSchema: false`）

AI 会以 `query` 传入**单个字符串**。如果需要多个字段，AI 只能把它们塞进这一个字符串，再由你解析出来。实际上，只要描述里写明，LLM 会很乐意传入一个 JSON 字符串。

```javascript
// Parse a JSON string the AI sent
let params;
try {
  params = typeof query === 'string' ? JSON.parse(query) : query;
} catch (e) {
  throw new Error('Expected a JSON object. Parser said: ' + e.message);
}
const price = Number(params.price);
const months = Number(params.months);
// ...
return JSON.stringify({ monthly_payment: /* ... */ });
```

**优点**：设置最简单，只需描述一个字段。
**缺点**：没有 schema 校验；如果 LLM 漏掉某个字段，工具会在运行时抛错。

**最适用于**：快速原型、只有单一自然输入的工具（一个问题、一个 URL、一段文本）。

### 模式 2：结构化（`specifyInputSchema: true`）

该工具会变成 LangChain 的 `DynamicStructuredTool`。LLM 看到的是带类型的参数 schema，并会以 `query` 传入一个**经过校验的对象**。你可以直接访问各字段。

```javascript
// query is now an object matching your schema
const price = query.price;
const months = query.months;
const residual_percent = query.residual_percent;

const monthly = computeAnnuity(price, months, residual_percent);
return JSON.stringify({ monthly_payment: monthly });
```

schema 通过以下任一方式定义：
- `schemaType: "fromJson"` + `jsonSchemaExample`（n8n v≥1.3）：粘贴一段示例 JSON，由 n8n 推断 schema
- `schemaType: "manual"` + `inputSchema`：自行编写完整的 JSON Schema

**优点**：LLM 能获得类型提示，无效调用会在代码运行前被拦截，代码更干净。
**缺点**：设置稍多一些；要求 n8n 版本支持 schema。

**最适用于**：带多个带类型参数的生产级工具（计算器、API 封装，以及任何含 LLM 容易转成字符串的数值字段的工具）。

**参见**：[INPUT_SCHEMA.md](INPUT_SCHEMA.md) 了解完整的 schema 配置。

---

## 返回格式

**返回值必须是字符串。** LLM 会把它当作工具的观察结果来读取。

```javascript
// ✅ String
return "42";

// ✅ Number (auto-converted to string by n8n)
return 42;

// ✅ JSON-encoded structured result (recommended for rich output)
return JSON.stringify({ result: 42, currency: "SEK" });

// ❌ Raw object → "The response property should be a string, but it is an object"
return { result: 42 };

// ❌ Workflow item format → "Wrong output type returned"
return [{ json: { result: 42 } }];

// ❌ Array → "The response property should be a string, but it is an object"
return [1, 2, 3];
```

### 最佳实践：对结构化结果做 JSON 字符串化

当工具的输出不只是简单的标量时，请返回 JSON 字符串：

```javascript
return JSON.stringify({
  monthly_payment_sek: 5405,
  loan_amount: 351920,
  total_cost_of_credit: 63295
});
```

LLM 能可靠地解析 JSON，并挑出需要展示给用户的字段。

### 错误处理：Agent 会读取你的失败信息

错误不只是让工作流停下来，它们还会返回给 LLM，后者通常会修正调用并重试。善加利用这一点：

```javascript
// Option A: throw — n8n surfaces the message to the agent
if (!isFinite(price)) throw new Error('price must be a number, e.g. 439900');

// Option B: return an error string — agent reads it like any tool result
if (!isFinite(price)) return JSON.stringify({ error: 'price must be a number, e.g. 439900' });
```

无论哪种方式，错误信息都要**写给 LLM 看**：说明哪里出错，以及一次合法调用应该是什么样。一句干巴巴的 `throw new Error('invalid input')` 会浪费这次重试；有指导性的信息通常能让下一次调用成功。

---

## 工具名称与描述

这些字段不是文档，而是 **LLM 所看到的工具契约**。请把它们当作提示词工程来对待。

### 名称
- 必须匹配 `[A-Za-z0-9_]+`（v1.1+）。不能有空格、连字符或 emoji。
- 使用带动词意味的描述性名称：`calculate_car_loan`、`get_weather`、`search_orders`。
- Agent 按这个名称调用工具。默认的 `Code Tool` 毫无用处，Agent 不知道该在何时调用它。

### 描述
- 说明**何时**使用以及**要发送什么**。
- 非结构化模式下，**附上 LLM 应发送的那段 JSON 字符串示例**。
- 结构化模式下，schema 自会说明一切，只需描述用途即可。

**非结构化示例（字符串内嵌 JSON 模式）：**
```
Deterministiskt beräknar månadskostnad för billån. Anropa med EN JSON-sträng:
{"price":439900,"down_payment":87980,"interest_rate":6.95,"months":36,"residual_percent":50}
Fält: price (SEK), down_payment (SEK), interest_rate (% per år), months, residual_percent (0-99).
```

**结构化示例（由 schema 定义）：**
```
Deterministically computes the monthly car-loan payment given price, down payment, 
annual interest rate, term, and residual percent. Use whenever the user asks for 
monthly cost, total credit cost, or loan breakdown.
```

---

## 常见错误与修复

### 错误 1：`"There was an error: 'Cannot assign to read only property \"name\" of object: Error: No execution data available'"`

**原因**：你在 Code Tool 沙箱内调用了 `$fromAI()`。

**修复**：`$fromAI()` 是供**其他**支持工具的节点（HTTP Request Tool、SendGrid Tool、`toolWorkflow` 等）使用的辅助函数，并未在 `toolCode` 内暴露。请直接从 `query` 读取 AI 的输入（或使用 `specifyInputSchema` 定义结构化字段）。

### 错误 2：`"Wrong output type returned"`

**原因**：你返回了工作流风格的数组，如 `[{ json: { ... } }]`。那是 Code **node** 的契约，不是 Code **Tool** 的契约。

**修复**：返回字符串。结构化数据请用 `return JSON.stringify(output)`。

### 错误 3：`"The response property should be a string, but it is an object"`

**原因**：你返回了普通对象或数组。

**修复**：对结果调用 `JSON.stringify()`，或强制转换为字符串。

### 错误 4：AI 从不调用该工具

**原因**：工具名过于笼统（`Code Tool`、`My Tool`），或描述没有清楚说明何时使用。

**修复**：改成带动词意味的名称（`calculate_car_loan`），并重写描述，明确写出触发条件（例如「用户询问月度费用时使用本工具」）。

### 错误 5：AI 往 `query` 里塞入垃圾数据

**原因**：非结构化工具的描述含糊，LLM 只能猜测格式。

**修复**：要么 (a) 在描述中给出具体的 JSON 示例，要么 (b) 切换到 `specifyInputSchema: true`，让 LLM 获得带类型的 schema。

**参见**：[ERROR_PATTERNS.md](ERROR_PATTERNS.md) 查看含复现步骤的完整清单。

---

## 沙箱中不可用的能力

Code Tool 沙箱比 Code node 沙箱**更窄**。不要想当然地认为辅助函数会一并带过来：

| 辅助函数 | Code node | Code Tool |
|---|---|---|
| `$input.all()`、`$input.first()`、`$input.item` | ✅ | ❌ |
| `$node["NodeName"]` | ✅ | ❌ |
| `$json`、`$binary` | ✅ | ❌ |
| `$fromAI()` | ❌ | ❌（尽管紧挨着 AI agent） |
| `this.helpers.httpRequest()` | ✅ | ❌ |
| `DateTime`（Luxon） | ✅ | ✅（JS 沙箱中标准可用） |
| `$jmespath()` | ✅ | ❌ |
| `this.getContext(...)` | ✅ | ❌ |
| `$getWorkflowStaticData(...)` | ✅ | ❌ |

**推论**：Code Tool 只适用于**纯计算**。如果需要 HTTP 调用、API 查询或跨调用的状态，请换用其他工具节点：
- HTTP Request Tool 用于外部 API 调用
- `toolWorkflow`（调用子工作流工具）用于多步逻辑，并可访问完整的 Code node 沙箱
- MCP / 数据库工具用于持久化状态

---

## 何时使用 Code Tool 与替代方案

在以下情况使用 **Code Tool**：
- ✅ 纯确定性计算（数学、解析、格式化、验证）
- ✅ 不该由 LLM 自己完成的轻量转换（精确运算、正则）
- ✅ 希望代码内联在工作流里，而不是放在单独的子工作流中

在以下情况使用 **`toolWorkflow`**（调用子工作流工具）：
- ✅ 需要多个参数，并用清晰的 `$fromAI()` 类型标注
- ✅ 需要访问 `this.helpers`、凭据或其他节点
- ✅ 逻辑要在多个 Agent 间复用
- ✅ 想要结构化的带类型输入，又不想手写 JSON Schema

在以下情况使用 **HTTP Request Tool**：
- ✅ 该工具本质上就是一次单独的 API 调用
- ✅ 希望在 URL、query、body 中对各参数使用 `$fromAI()` 绑定

**经验法则**：如果你发现自己想用 `$fromAI()`，多半应该改用 `toolWorkflow`，而不是 `toolCode`。

---

## 完整可运行示例

一个生产级的计算器工具（非结构化，字符串内嵌 JSON 模式）：

```json
{
  "parameters": {
    "name": "calculate_car_loan",
    "description": "Computes monthly car-loan payment using an annuity formula with residual/balloon. Call with a single JSON string. Example: {\"price\":439900,\"down_payment\":87980,\"interest_rate\":6.95,\"months\":36,\"residual_percent\":50,\"setup_fee\":695,\"monthly_admin_fee\":59}. Required: price, down_payment, interest_rate, months, residual_percent. Optional: setup_fee, monthly_admin_fee (default 0).",
    "language": "javaScript",
    "jsCode": "let params;\ntry {\n  params = typeof query === 'string' ? JSON.parse(query) : query;\n} catch (e) {\n  throw new Error('Invalid JSON: ' + e.message);\n}\n\nconst price           = Number(params.price);\nconst down_payment    = Number(params.down_payment);\nconst interest_rate   = Number(params.interest_rate);\nconst months          = Number(params.months);\nconst residual_percent= Number(params.residual_percent);\nconst setup_fee       = Number(params.setup_fee ?? 0) || 0;\nconst monthly_admin_fee = Number(params.monthly_admin_fee ?? 0) || 0;\n\nif (!isFinite(price) || price <= 0) throw new Error('price must be > 0');\nif (down_payment < 0 || down_payment >= price) throw new Error('down_payment must be in [0, price)');\n\nconst principal = price - down_payment;\nconst residual  = price * (residual_percent / 100);\nconst r = interest_rate / 100 / 12;\nconst growth = Math.pow(1 + r, months);\nconst base = r === 0\n  ? (principal - residual) / months\n  : (principal - residual / growth) * r / (1 - 1 / growth);\nconst monthly_payment = base + monthly_admin_fee;\n\nreturn JSON.stringify({\n  monthly_payment_sek: Math.round(monthly_payment),\n  loan_amount: Math.round(principal),\n  residual_value_sek: Math.round(residual),\n  total_cost_of_credit: Math.round(monthly_payment * months + residual + setup_fee - principal)\n});"
  },
  "type": "@n8n/n8n-nodes-langchain.toolCode",
  "typeVersion": 1.3,
  "name": "calculate_car_loan"
}
```

通过 `ai_tool` 连接类型把它接入 AI Agent。

---

## 与其他 Skill 的集成

**n8n-code-javascript**：针对 Code **node** 的 Skill。大多数 JavaScript 模式（数组、map/filter、DateTime）可以迁移，但 I/O 契约不同。不要照搬数据访问代码。

**n8n-node-configuration**：`specifyInputSchema` 是典型的由 displayOptions 驱动的条件字段。对 `@n8n/n8n-nodes-langchain.toolCode` 使用 `get_node({detail: "standard"})` 可查看与 schema 相关的属性。

**n8n-workflow-patterns**：Code Tool 位于「带工具的 AI Agent」模式之中。一个 Agent 通常挂有多个工具，Code Tool 属于「本地计算」那一种。

**n8n-validation-expert**：上文列出的三种 Code Tool 错误特征鲜明，一旦验证报出 "Wrong output type returned"，就知道要从条目数组改成字符串。

---

## 快速参考清单

部署 Code Tool 之前：

- [ ] **节点类型**为 `@n8n/n8n-nodes-langchain.toolCode`（不是 `nodes-base.code`）
- [ ] **工具名称**有描述性、带动词意味、snake_case（例如 `calculate_car_loan`）
- [ ] **描述**写明何时使用该工具，且（若为非结构化）给出 JSON 示例
- [ ] **输入**从 `query`（JS）或 `_query`（Python）读取
- [ ] 代码体中**没有 `$fromAI()`**
- [ ] **没有 `$input` / `$json` / `$helpers`**，这些不在沙箱里
- [ ] **返回值**是字符串（结构化输出用 `JSON.stringify()`）
- [ ] 通过 `ai_tool` 连接**接入** AI Agent
- [ ] 用 LLM 实际会发送的那类输入**测试**过（字符串里的 JSON，或经 schema 校验的对象）

---

## 补充资源

- [INPUT_SCHEMA.md](INPUT_SCHEMA.md)：深入讲解结构化输入（DynamicStructuredTool）
- [ERROR_PATTERNS.md](ERROR_PATTERNS.md)：完整的错误清单，含原因与修复

### 官方来源
- [n8n Custom Code Tool 文档](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode/)
- [ToolCode 源码](https://github.com/n8n-io/n8n/blob/master/packages/%40n8n/nodes-langchain/nodes/tools/ToolCode/ToolCode.node.ts)：沙箱契约
- [LangChain 工具文档](https://js.langchain.com/docs/modules/agents/tools/)：DynamicTool / DynamicStructuredTool

---

**记住**：Code Tool 是披着 Code node 界面的 LangChain 工具。其契约是：**字符串进，字符串出**。其余一切都由此衍生。
