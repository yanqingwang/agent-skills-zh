> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-code-tool/ERROR_PATTERNS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Code Tool 报错模式

`@n8n/n8n-nodes-langchain.toolCode` 最常见的失败模式，附确切的报错字符串、根因与修法。

---

## 错误 1：`"Cannot assign to read only property 'name' of object: Error: No execution data available"`

**完整消息（由 n8n 包装）：**
> There was an error: "Cannot assign to read only property 'name' of object 'Error: No execution data available'"

**根因**：在 Code Tool 沙箱里调用 `$fromAI()`。`$fromAI()` 是为*其他*支持工具的节点（HTTP Request Tool、SendGrid Tool、`toolWorkflow`）准备的辅助函数，那些节点里 AI 提供的值经由工作流执行数据流入。Code Tool 沙箱没有执行数据，输入直接经 `query` 进入。该辅助函数抛错，n8n 尝试给错误对象的 `name` 属性附加信息，但错误对象被冻结，赋值失败。

**修法**：移除 `$fromAI()`。改从 `query` 读取（或定义输入 schema，见 [INPUT_SCHEMA.md](INPUT_SCHEMA.md)）。

```javascript
// ❌ Broken
const price = $fromAI('price', 'Car price in SEK', 'number');

// ✅ Unstructured — parse a JSON string
const params = JSON.parse(query);
const price = Number(params.price);

// ✅ Structured — with specifyInputSchema: true
const { price } = query;
```

---

## 错误 2：`"Wrong output type returned"`

**根因**：你从 Code Tool 返回了工作流条目格式（`[{json: {...}}]`）。该格式属于普通 Code **节点**；工具遵循 LangChain 契约，必须返回字符串。

**修法**：返回字符串。要结构化输出就做字符串化：

```javascript
// ❌ Broken
return [{ json: { monthly_payment: 5405 } }];

// ✅ Fixed
return JSON.stringify({ monthly_payment: 5405 });
```

---

## 错误 3：`"The response property should be a string, but it is an <type>"`

其中 `<type>` 可以是 `object`、`undefined`、`function` 等。

**根因**：你返回了裸对象、数组，或者什么都没返回。

| 返回的值 | 报错说 | 修法 |
|---|---|---|
| `{ result: 42 }` | `...is an object` | `JSON.stringify({ result: 42 })` |
| `[1, 2, 3]` | `...is an object` | `JSON.stringify([1, 2, 3])` |
| *（没有 `return`）* | `...is an undefined` | 加一个 `return` |
| `undefined` | `...is an undefined` | 返回点东西 |

**数字没问题**，n8n 会自动把它们转成字符串：
```javascript
return 42;  // ✅ becomes "42"
```

**布尔值不会自动转换**，要显式字符串化：
```javascript
return String(someBoolean);  // ✅
return JSON.stringify(someBoolean);  // ✅
```

---

## 错误 4：AI 从不调用工具

**症状**：Agent 靠自己的推理作答，无视工具。执行轨迹里看不到任何工具调用。

**常见根因与修法**：

1. **名字太泛。** `Code Tool`、`My Tool` 这类默认名对 LLM 没有任何信号。
   - 修法：改成动词开头、领域相关的 snake_case：`calculate_car_loan`、`search_orders`、`lookup_customer`。

2. **描述没说清触发条件。** "Calculates things"（算各种东西）太含糊。
   - 修法：明确列出应触发该工具的用户意图。`"Use this whenever the user asks about monthly cost, loan breakdown, or total interest."`

3. **工具没接线。** 节点摆在画布上，但没连到 AI Agent 的 `ai_tool` 输入。
   - 修法：连上它。检查工作流 JSON 的 `connections` 块里有 `"<tool_name>": { "ai_tool": [[{ "node": "AI Agent", "type": "ai_tool", "index": 0 }]] }`。

4. **名字违反 `[A-Za-z0-9_]+`。** 工具名里带空格、连字符或 emoji，在 v1.1+ 上会导致静默跳过。
   - 修法：改名，只用 `snake_case_only`。

---

## 错误 5：LLM 发来的 `query` 格式不对

**症状**：`JSON.parse(query)` 抛错，或字段过来的类型不对。

**根因**：
- 你在无结构模式，描述含糊，LLM 就自创格式。
- 你要的是 JSON 字符串，LLM 却发来自然语言句子。
- 数值字段成了字符串，因为 LLM 序列化时就是这么发的。

**修法**，按优先级排序：

1. **切换到结构化模式。** 设 `specifyInputSchema: true` 并定义字段。LLM 拿到带类型的 schema，n8n 在你的代码运行前先做校验。

2. **在描述里给一个具体示例。** LLM 很会模仿示例：
   ```
   Call with a single JSON string. Example:
   {"price":439900,"down_payment":87980,"interest_rate":6.95}
   ```

3. **防御性类型转换**：
   ```javascript
   const params = JSON.parse(query);
   const price = Number(params.price);
   if (!isFinite(price)) throw new Error('price must be numeric');
   ```

---

## 错误 6：`"$helpers is not defined"` / `"$input is not defined"`

**根因**：你以为 Code Tool 沙箱暴露的辅助函数和 Code 节点一样。并不是。

**Code Tool 里不可用**：
- `$input`、`$json`、`$binary`
- `$node["OtherNode"]`
- `$helpers.httpRequest()`
- `$jmespath()`
- `this.getContext(...)`、`$getWorkflowStaticData(...)`
- `$fromAI()`

**修法**：
- 纯计算？留在 Code Tool，用普通 JS。
- 要 HTTP？改用 **HTTP Request Tool**（在 URL/body 里用 `$fromAI()`）。
- 要其他节点的数据或凭据？改用 **Call Sub-workflow Tool（`toolWorkflow`）**，它的子工作流有完整的 Code 节点沙箱。
- 要跨调用保持状态？Code Tool 做不到。用一个子工作流读写 Data Table、Redis 等。

---

## 错误 7：Python 特有的 `"name 'query' is not defined"`

**根因**：Python 里输入变量是 `_query`（带下划线前缀），不是 `query`。

```python
# ❌ Broken
result = process(query)

# ✅ Fixed
result = process(_query)
```

---

## 报错预防清单

保存 Code Tool 之前：

- [ ] 工具**名称**为 snake_case、见名知义且唯一
- [ ] **描述**告诉 LLM 何时调用它；无结构模式则附一个示例
- [ ] 代码体里**没有 `$fromAI()`**
- [ ] **没有 `$input`、`$json`、`$helpers`**（这个沙箱里没有）
- [ ] 输入从 `query`（JS）或 `_query`（Python）读取
- [ ] 所有代码路径都 `return` 一个字符串（或会自动转换的数字）
- [ ] 返回结构化数据时用 `JSON.stringify(...)` 包一层
- [ ] 通过 `ai_tool` 连接连到某个 AI Agent
- [ ] 多字段输入：要么在描述里给示例 JSON，要么 `specifyInputSchema: true`

---

## 调试技巧

- **用 Execution 视图**，别只看测试输出。Agent 的工具调用和原始输入/输出都在那里，能看清 LLM 发来的 `query` 到底是什么。
- **在工具内部留日志**，把字段放进返回的 JSON：
  ```javascript
  return JSON.stringify({ received_query: query, result: /* ... */ });
  ```
  LLM 能看到回显，你也能发现格式错误的输入。
- **脱离 LLM 单测工具**：临时把工具节点改成一个独立 Code 节点、写死 `query`，手动跑一遍，然后再改回去。
