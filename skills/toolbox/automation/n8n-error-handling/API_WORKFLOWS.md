> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-error-handling/API_WORKFLOWS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# API 工作流

当工作流本身就是 HTTP API，即以 Webhook 触发器开始、以 `Respond to Webhook` 结束的工作流时，错误处理就不再是可选项。调用方是一台等待响应的机器，失败模式毫不留情：悬挂分支会变成超时，错误的状态码会破坏调用方的错误处理，泄露的堆栈跟踪会变成安全问题。

本文件讲如何为这个模式接线，让它在失败时也表现正确，而不只是在正常路径上。逐节点机制见 **NODE_ERROR_OUTPUTS.md**；响应体约定与状态码见 **RESPONSE_SHAPES.md**。

---

## 结构

```
Webhook (responseMode: "responseNode")
  → validate input ──valid──→ process ──→ Respond (200, success body)
  │                └─invalid─→ Respond (400, validation_error body)
  └── (any fallible node's error output, sourceIndex 1)
            → Respond (5xx, structured error body)
            → optional: Log full error privately / notify
```

不可妥协的一条：**每条路径都以 Respond 节点结束。**成功、校验失败、执行失败，全都要。不到达 Respond 的路径就是悬挂分支，悬挂分支就是调用方超时。

在 Webhook 触发器上设置 `responseMode: "responseNode"`：没有它，触发器会立即确认（`onReceived`），调用方永远看不到你算出的响应。（Webhook/Respond 的坑见 **n8n-node-configuration** 的 NODE_FAMILY_GOTCHAS.md。）

---

## 给每个可能失败的节点接线

对每个可能失败的节点（HTTP、数据库、第三方、文件操作），按 NODE_ERROR_OUTPUTS.md 的两步设置：

1. 在节点上设 `onError: "continueErrorOutput"`。
2. 用 `addConnection` 把它的 `sourceIndex: 1` 连到你的错误 Respond（直连，或先经一个日志节点）。

一条两节点的处理链，两个都可能失败，都路由到同一个响应器：

```javascript
// Turn on error outputs
{ type: "updateNode", nodeName: "Fetch User",    changes: { onError: "continueErrorOutput" } }
{ type: "updateNode", nodeName: "Call External", changes: { onError: "continueErrorOutput" } }

// Success path
{ type: "addConnection", source: "Webhook",      target: "Fetch User",      sourceIndex: 0 }
{ type: "addConnection", source: "Fetch User",   target: "Call External",   sourceIndex: 0 }
{ type: "addConnection", source: "Call External",target: "Respond Success", sourceIndex: 0 }

// Error paths — both fan in to one responder
{ type: "addConnection", source: "Fetch User",   target: "Respond Error",   sourceIndex: 1 }
{ type: "addConnection", source: "Call External",target: "Respond Error",   sourceIndex: 1 }
```

三点要注意：

1. **多个来源共用一个 `Respond Error`。**汇入让画布保持可读。
2. **两个节点都设了 `onError`。**任何一边漏掉，该节点的失败就会中断工作流而不是走错误路由，调用方随之超时。
3. **如果要在响应体里暴露错误信息，先脱敏。**见下文"不要泄露内部细节"。

错误 Respond 节点的 JSON：

```json
{
  "type": "n8n-nodes-base.respondToWebhook",
  "name": "Respond Error",
  "parameters": {
    "respondWith": "json",
    "responseBody": "={{ { error: 'upstream_error', message: 'External service failed' } }}",
    "options": {
      "responseCode": 502,
      "responseHeaders": { "entries": [{ "name": "Content-Type", "value": "application/json" }] }
    }
  }
}
```

始终显式设置 `Content-Type: application/json`：默认值取决于响应体形状，不可靠。

---

## 4xx 在上游判定，5xx 从错误输出出来

这是让 API 语义可靠的结构性规则：

- **校验 / 鉴权 / 资源不存在这类失败是*有已知响应的预期结果*。**它们不是节点崩溃。在正式处理**之前**用 IF/Switch + 专门的 Respond 检查，直接返回正确的 4xx。不要把它们路由进错误输出。
- **执行失败（节点真的抛错）是*意外*。**它们从错误输出出来，表现为 5xx。

真实的 API 通常在处理阶段*之前*就需要多个上游检查，每个检查各配一组 IF/Switch + Respond：

```
Webhook
  → Auth present & valid?      ── no ──→ Respond 401 unauthorized
  → Input valid?               ── no ──→ Respond 400 validation_error (with details)
  → Caller allowed this op?    ── no ──→ Respond 403 forbidden
  → Target resource exists?    ── no ──→ Respond 404 not_found
  → Processing stage (HTTP / DB / etc.) ←── this is where 5xx errors originate
```

这不是过度设计：区别在于调用方拿到的是可操作的 `validation_error`，还是只能干瞪眼的笼统 500。

---

## 输入校验：条件摆上画布

把检查放进 **IF** 节点：每条规则一个条件，combinator 用 `and`。真 → 你的逻辑；假 → 一个 400 Respond。
每条规则都摆在画布上，加一条规则就是加一个条件。

```json
{
  "type": "n8n-nodes-base.if",
  "typeVersion": 2.3,
  "name": "Input valid?",
  "parameters": {
    "conditions": {
      "options": { "caseSensitive": true, "leftValue": "", "typeValidation": "strict", "version": 3 },
      "conditions": [
        { "leftValue": "={{ typeof $json.body.name === 'string' && $json.body.name.length > 0 }}", "rightValue": "", "operator": { "type": "boolean", "operation": "true", "singleValue": true } },
        { "leftValue": "={{ /^\\S+@\\S+\\.\\S+$/.test($json.body.email ?? '') }}", "rightValue": "", "operator": { "type": "boolean", "operation": "true", "singleValue": true } },
        { "leftValue": "={{ ['starter', 'pro', 'enterprise'].includes($json.body.plan) }}", "rightValue": "", "operator": { "type": "boolean", "operation": "true", "singleValue": true } },
        { "leftValue": "={{ Number.isInteger($json.body.seat_count) && $json.body.seat_count >= 1 && $json.body.seat_count <= 500 }}", "rightValue": "", "operator": { "type": "boolean", "operation": "true", "singleValue": true } }
      ],
      "combinator": "and"
    },
    "options": {}
  }
}
```

每条规则写成用 `is true` 测试的布尔表达式，而不是带类型的比较（`number` ≥ 1）。输入是不可信的：在严格类型校验下，对类型不对的值做带类型比较（`"seat_count": "five"`）会让节点抛错而不是返回 false，调用方拿到 500 而不是 400。

false 分支用一个静态响应体回显期望的 schema，让调用方（或驱动这次调用的 LLM）能修正请求：

```json
{
  "type": "n8n-nodes-base.respondToWebhook",
  "name": "Respond 400",
  "parameters": {
    "respondWith": "json",
    "options": { "responseCode": 400 },
    "responseBody": "={{ { error: 'validation_error', message: 'The request body does not match request_schema.', request_schema: { type: 'object', additionalProperties: false, required: ['name', 'email', 'plan', 'seat_count'], properties: { name: { type: 'string', minLength: 1 }, email: { type: 'string', format: 'email' }, plan: { type: 'string', enum: ['starter', 'pro', 'enterprise'] }, seat_count: { type: 'integer', minimum: 1, maximum: 500 } } } } }}"
  }
}
```

状态码在 `options.responseCode` 里；顶层的 `responseCode` 会被忽略，节点照样返回 200。响应体直接传对象：字符串体会先被当作 JSON 解析一遍，`JSON.stringify(...)` 只是多一步（见 **n8n-node-configuration** 的 NODE_FAMILY_GOTCHAS.md）。

### 例外：逐字段错误信息（Code 节点）

当调用方需要知道**哪个**字段失败、为什么失败时，IF 说不出来。把 IF 换成一个 Code 节点，遍历 schema 列表（这个循环就是"闭集理由"），再用一个 IF 对 `={{ $json.valid }}` 的结果分支。给节点写备注：`Why Code: IF considered — per-field messages need a loop over the schema`。

```javascript
// Run Once for All Items. Edit FIELDS for your endpoint; keep the output keys.
const body = $input.first().json.body ?? {};
const FIELDS = [
  { name: 'name', type: 'string', required: true, minLength: 1, description: 'Customer full name' },
  { name: 'email', type: 'string', required: true, pattern: '^\\S+@\\S+\\.\\S+$', description: 'Contact email address' },
  { name: 'plan', type: 'string', required: true, enum: ['starter', 'pro', 'enterprise'], description: 'Subscription plan' },
  { name: 'seat_count', type: 'integer', required: true, minimum: 1, maximum: 500, description: 'Number of licensed seats' },
];
const details = {};
for (const f of FIELDS) {
  const v = body[f.name];
  if (v === undefined) { if (f.required) details[f.name] = `Missing required field "${f.name}"`; continue; }
  const typeOk = f.type === 'integer' ? Number.isInteger(v) : typeof v === f.type;
  if (!typeOk) details[f.name] = `Expected type "${f.type}"`;
  else if (f.minLength !== undefined && v.length < f.minLength) details[f.name] = `Must be at least ${f.minLength} character(s)`;
  else if (f.pattern && !new RegExp(f.pattern).test(v)) details[f.name] = `"${v}" is not valid`;
  else if (f.enum && !f.enum.includes(v)) details[f.name] = `"${v}" is not allowed. Must be one of: ${f.enum.join(', ')}`;
  else if ((f.minimum !== undefined && v < f.minimum) || (f.maximum !== undefined && v > f.maximum)) details[f.name] = `Must be between ${f.minimum} and ${f.maximum}`;
}
for (const key of Object.keys(body)) if (!FIELDS.some(f => f.name === key)) details[key] = 'Unknown field';

const requiredSchema = {
  type: 'object', additionalProperties: false,
  required: FIELDS.filter(f => f.required).map(f => f.name),
  properties: Object.fromEntries(FIELDS.map(({ name, required, ...rule }) => [name, rule])),
};
const issues = Object.entries(details).map(([field, msg]) => `• ${field}: ${msg}`);
return [{ json: issues.length === 0
  ? { valid: true, validationError: null }
  : { valid: false, validationError: `Validation failed (${issues.length} issue${issues.length > 1 ? 's' : ''}):\n${issues.join('\n')}`, details, requiredSchema } }];
```

400 Respond 读取结果：

```
={{ { error: 'validation_error', message: $json.validationError, details: $json.details, request_schema: $json.requiredSchema } }}
```

输出契约（Respond 依赖这些键名）：

- 有效：`{ valid: true, validationError: null }`
- 无效：`{ valid: false, validationError: <概要字符串>, details: { <字段>: <信息> }, requiredSchema: <回显的 schema> }`

`FIELDS` 是唯一要编辑的地方：检查逻辑和回显 schema 都由它生成，两者不会漂移。
未知字段也会被报告，这正是回显 schema 里 `additionalProperties: false` 承诺的行为。

### 约束速查表

| 需求 | IF 规则（布尔表达式） | `FIELDS` 条目（Code 例外） |
|---|---|---|
| 必填、非空字符串 | `typeof $json.body.name === 'string' && $json.body.name.length > 0` | `type: 'string', required: true, minLength: 1` |
| 正则模式 | `/^\S+@\S+\.\S+$/.test($json.body.email ?? '')` | `pattern: '^\\S+@\\S+\\.\\S+$'` |
| 枚举 | `['a', 'b'].includes($json.body.plan)` | `enum: ['a', 'b']` |
| 范围内的整数 | `Number.isInteger($json.body.n) && $json.body.n >= 1 && $json.body.n <= 500` | `type: 'integer', minimum: 1, maximum: 500` |
| 带元素的数组 | `Array.isArray($json.body.tags) && $json.body.tags.length > 0` | 在类型检查里加一个 `array` 分支 |
| 条件规则 | 第一个 IF 之后再接一个 IF，或 `$json.body.type !== 'X' \|\| <rule>` | 一个由循环检查的 `when` 键 |

### workflow JSON 里的转义

IF 规则里，正则是表达式内的 JavaScript 字面量：`/^\S+@\S+\.\S+$/`。Code 节点里，它是传给 `new RegExp` 的字符串，每个反斜杠要写两遍（`'^\\S+@\\S+\\.\\S+$'`）。当其中任一种进入 workflow JSON（表达式字符串或 `jsCode`），每个反斜杠还要再翻一倍。如果邮件校验始终匹配不上，先数反斜杠。

---

## 5xx：按原因路由，每个状态码一个静态 Respond

多个易失败节点的错误输出可以汇入一个 **Switch**，由它给失败分类。每个输出接一个码固定、响应体固定的 Respond；兜底输出把其余情况全部接成 500。每个状态码都摆在画布上，加一种情况就是加一条规则。

```
error outputs (main[1]) ─→ Switch "Classify error"
                             ├─ message contains "timeout"    → Respond 504 upstream_timeout
                             ├─ message contains "rate limit" → Respond 503 service_unavailable
                             └─ fallback (extra output)       → Respond 500 internal_error
```

```json
{
  "type": "n8n-nodes-base.switch",
  "typeVersion": 3.4,
  "name": "Classify error",
  "parameters": {
    "mode": "rules",
    "rules": {
      "values": [
        {
          "conditions": {
            "options": { "caseSensitive": false, "leftValue": "", "typeValidation": "strict", "version": 3 },
            "conditions": [ { "leftValue": "={{ $json.error?.message ?? '' }}", "rightValue": "timeout", "operator": { "type": "string", "operation": "contains" } } ],
            "combinator": "and"
          },
          "renameOutput": true,
          "outputKey": "upstream_timeout"
        },
        {
          "conditions": {
            "options": { "caseSensitive": false, "leftValue": "", "typeValidation": "strict", "version": 3 },
            "conditions": [ { "leftValue": "={{ $json.error?.message ?? '' }}", "rightValue": "rate limit", "operator": { "type": "string", "operation": "contains" } } ],
            "combinator": "and"
          },
          "renameOutput": true,
          "outputKey": "service_unavailable"
        }
      ]
    },
    "options": { "fallbackOutput": "extra", "renameFallbackOutput": "internal_error" }
  }
}
```

每个 Respond 都是静态的，例如：

```json
{
  "type": "n8n-nodes-base.respondToWebhook",
  "name": "Respond 504",
  "parameters": {
    "respondWith": "json",
    "responseBody": "={{ { error: 'upstream_timeout', message: 'External service did not respond in time' } }}",
    "options": { "responseCode": 504 }
  }
}
```

- 没有 `fallbackOutput: "extra"` 时，没有规则匹配的错误会被丢弃，调用方一直等到超时。
- 恰好只有两种结果时，可以用一个带计算状态码的 Respond：在它的 Response Code 字段里写一个短三元表达式（`options.responseCode` = `={{ $json.error?.message?.includes('timeout') ? 504 : 500 }}`）。三种结果起，改用 Switch。

---

## 不要泄露内部细节

诱人的一行写法：

```javascript
responseBody: "={{ JSON.stringify({ error: 'internal_error', details: $json.error }) }}"  // ❌
```

`$json.error` 可能带着堆栈跟踪、内部节点名、连接字符串，以及内嵌 token 的上游响应体。把它暴露出去，等于递给攻击者一张地图，调用方却什么有用的都拿不到。

正确做法：完整错误写进私有日志，对外返回脱敏信息。

```javascript
// Error output → Log node (sends full $json.error to Sentry/Slack/your logger)
{ type: "addConnection", source: "Call External", target: "Log Full Error", sourceIndex: 1 }
{ type: "addConnection", source: "Log Full Error", target: "Respond Error",  sourceIndex: 0 }
```

```json
// Respond Error keeps the body clean:
{ "responseBody": "={{ { error: 'upstream_error', message: 'External service failed' } }}",
  "options": { "responseCode": 502 } }
```

调用方看到干净的信息；细节留在内部。完整的"不得外泄"清单见 **RESPONSE_SHAPES.md**。

---

## 关联 ID（可选）

如果你们做分布式追踪或日志关联，就给**每一条**成功和错误响应一致地加上 `request_id`（只覆盖一半比没有更糟）。两种来源：

- **调用方提供**：读取 `X-Request-ID` 请求头并透传。更适合跨系统追踪。
- **自行生成**：用 `{{ $execution.id }}` 或 UUID。更省事。

别把它和异步（202）端点返回的 `job_id` 混为一谈：`job_id` 是调用方之后轮询任务用的，不是关联字段。

---

## 异步 / 202 模式

如果任务耗时超过调用方愿意等的时间，先立即响应 202，再异步继续：

```
Webhook → validate → Respond (202, { job_id }) → continue processing → callback / queue / email on completion
```

它有自己的坑（幂等、回调重试、状态跟踪）：要有意识地设计。`job_id` 是内生的（之后靠它找到任务），区别于可选的 `request_id`。

---

## 验证 API 工作流

激活之前：

1. **用 `n8n_test_workflow` 测试成功路径**。确认响应形状和状态码。**API 工作流几乎总有副作用（数据库写入、第三方调用、对外发消息）：运行会触发副作用的测试前，先问用户。**
2. **触发一条错误路径**：喂一个会让处理节点失败的输入，运行，确认错误 Respond 以正确的状态码和响应体触发。
3. **用 `n8n_get_workflow` 验证连接**：每个易失败节点都设了 `onError: "continueErrorOutput"` 且 `main[1]` 已接线。（NODE_ERROR_OUTPUTS.md。）
4. **确认错误响应体没有泄露内部细节**。
5. **事后用 `n8n_executions` 检查真实失败**，确认实际发出去的状态码与预期一致。

任何一项不过，先修复再激活。
