> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-code-javascript/DATA_ACCESS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 数据访问模式 - JavaScript Code 节点

在 n8n Code 节点中用 JavaScript 访问数据的完整指南。

---

## 概述

在 n8n Code 节点中，你通过内置变量和方法访问前序节点的数据。弄清该用哪个方法，对工作流正确执行至关重要。

**数据访问优先级**（按常见使用频率）：
1. **`$input.all()`** - 最常用 - 批量操作、聚合
2. **`$input.first()`** - 很常用 - 单条目操作
3. **`$input.item`** - 常用 - 仅限 Each Item 模式
4. **`$node["NodeName"].json`** - 引用特定节点
5. **`$json`** - 直接取当前条目（旧式，改用 `$input`）

> **原生节点优先。** 这些模式说明的是：Code 节点通过了 SKILL.md 的准入门槛之后，如何在其中读取数据。这里的几个示例（过滤、排序与限量、去重、求和、分组）在真实工作流里本是原生节点的活：Filter、Sort + Limit、Remove Duplicates、Summarize。把它们当作 Code 的写法惯例，而不是新增 Code 节点的理由。

---

## 模式 1：$input.all() - 处理所有条目

**用法**：批量处理最常用的模式

**适用场景：**
- 处理多条记录
- 聚合数据（求和、计数、平均值）
- 过滤数组
- 转换数据集
- 比较条目
- 排序或排名

### 基本用法

```javascript
// Get all items from previous node
const allItems = $input.all();

// allItems is an array of objects like:
// [
//   {json: {id: 1, name: "Alice"}},
//   {json: {id: 2, name: "Bob"}}
// ]

console.log(`Received ${allItems.length} items`);

return allItems;
```

### 示例 1：过滤活跃条目

```javascript
const allItems = $input.all();

// Filter only active items
const activeItems = allItems.filter(item => item.json.status === 'active');

return activeItems;
```

### 示例 2：转换所有条目

```javascript
const allItems = $input.all();

// Map to new structure
const transformed = allItems.map(item => ({
  json: {
    id: item.json.id,
    fullName: `${item.json.firstName} ${item.json.lastName}`,
    email: item.json.email,
    processedAt: new Date().toISOString()
  }
}));

return transformed;
```

### 示例 3：聚合数据

```javascript
const allItems = $input.all();

// Calculate total
const total = allItems.reduce((sum, item) => {
  return sum + (item.json.amount || 0);
}, 0);

return [{
  json: {
    total,
    count: allItems.length,
    average: total / allItems.length
  }
}];
```

### 示例 4：排序与限量

```javascript
const allItems = $input.all();

// Get top 5 by score
const topFive = allItems
  .sort((a, b) => (b.json.score || 0) - (a.json.score || 0))
  .slice(0, 5);

return topFive.map(item => ({json: item.json}));
```

### 示例 5：按类别分组

```javascript
const allItems = $input.all();

// Group items by category
const grouped = {};

for (const item of allItems) {
  const category = item.json.category || 'Uncategorized';

  if (!grouped[category]) {
    grouped[category] = [];
  }

  grouped[category].push(item.json);
}

// Convert to array format
return Object.entries(grouped).map(([category, items]) => ({
  json: {
    category,
    items,
    count: items.length
  }
}));
```

### 示例 6：按 ID 去重

```javascript
const allItems = $input.all();

// Remove duplicates by ID
const seen = new Set();
const unique = [];

for (const item of allItems) {
  const id = item.json.id;

  if (!seen.has(id)) {
    seen.add(id);
    unique.push(item);
  }
}

return unique;
```

---

## 模式 2：$input.first() - 获取第一条目

**用法**：单条目操作中非常常用

**适用场景：**
- 前序节点返回单个对象
- 处理 API 响应
- 获取初始/首个数据点
- 访问配置或元数据

### 基本用法

```javascript
// Get first item from previous node
const firstItem = $input.first();

// Access the JSON data
const data = firstItem.json;

console.log('First item:', data);

return [{json: data}];
```

### 示例 1：处理单个 API 响应

```javascript
// Get API response (typically single object)
const response = $input.first().json;

// Extract what you need
return [{
  json: {
    userId: response.data.user.id,
    userName: response.data.user.name,
    status: response.status,
    fetchedAt: new Date().toISOString()
  }
}];
```

### 示例 2：转换单个对象

```javascript
const data = $input.first().json;

// Transform structure
return [{
  json: {
    id: data.id,
    contact: {
      email: data.email,
      phone: data.phone
    },
    address: {
      street: data.street,
      city: data.city,
      zip: data.zip
    }
  }
}];
```

### 示例 3：校验单条目

```javascript
const item = $input.first().json;

// Validation logic
const isValid = item.email && item.email.includes('@');

return [{
  json: {
    ...item,
    valid: isValid,
    validatedAt: new Date().toISOString()
  }
}];
```

### 示例 4：提取嵌套数据

```javascript
const response = $input.first().json;

// Navigate nested structure
const users = response.data?.users || [];

return users.map(user => ({
  json: {
    id: user.id,
    name: user.profile?.name || 'Unknown',
    email: user.contact?.email || 'no-email'
  }
}));
```

### 示例 5：与其他方法组合使用

```javascript
// Get first item's data
const firstData = $input.first().json;

// Use it to filter all items
const allItems = $input.all();
const matching = allItems.filter(item =>
  item.json.category === firstData.targetCategory
);

return matching;
```

---

## 模式 3：$input.item - 当前条目（Each Item 模式）

**用法**：在 "Run Once for Each Item" 模式下常见

**适用场景：**
- 模式设置为 "Run Once for Each Item"
- 需要独立处理各条目
- 逐条目调用 API 或做校验
- 针对单条目的错误处理

**重要**：只能在 "Each Item" 模式下使用。在 "All Items" 模式下为 undefined。

### 基本用法

```javascript
// In "Run Once for Each Item" mode
const currentItem = $input.item;
const data = currentItem.json;

console.log('Processing item:', data.id);

return [{
  json: {
    ...data,
    processed: true
  }
}];
```

### 示例 1：附加处理元数据

```javascript
const item = $input.item;

return [{
  json: {
    ...item.json,
    processed: true,
    processedAt: new Date().toISOString(),
    processingDuration: Math.random() * 1000  // Simulated duration
  }
}];
```

### 示例 2：逐条目校验

```javascript
const item = $input.item;
const data = item.json;

// Validate this specific item
const errors = [];

if (!data.email) errors.push('Email required');
if (!data.name) errors.push('Name required');
if (data.age && data.age < 18) errors.push('Must be 18+');

return [{
  json: {
    ...data,
    valid: errors.length === 0,
    errors: errors.length > 0 ? errors : undefined
  }
}];
```

### 示例 3：针对单条目的 API 调用

```javascript
const item = $input.item;
const userId = item.json.userId;

// Make API call specific to this item
const response = await this.helpers.httpRequest({
  method: 'GET',
  url: `https://api.example.com/users/${userId}/details`
});

return [{
  json: {
    ...item.json,
    details: response
  }
}];
```

> ⚠️ **用 `this.helpers.httpRequest`，不要用 `$helpers`。** 在 Code 节点的 task-runner 沙箱（n8n v2.0 起默认）里，裸的 `$helpers` 全局变量不存在，`$helpers.httpRequest()` 会抛出 `ReferenceError: $helpers is not defined`。**鉴权 API 不要沿用这个模式。** `this.helpers.httpRequestWithAuthentication` 在 task-runner 沙箱中被禁止。改用挂了凭据的 HTTP Request 节点，或委托给一个子工作流，由其 HTTP Request 节点持有凭据。除了简单的无鉴权 GET，其他情况本来也该优先用 HTTP Request 节点。参见 ERROR_PATTERNS.md 错误 #6。

### 示例 4：条件处理

```javascript
const item = $input.item;
const data = item.json;

// Process based on item type
if (data.type === 'premium') {
  return [{
    json: {
      ...data,
      discount: 0.20,
      tier: 'premium'
    }
  }];
} else {
  return [{
    json: {
      ...data,
      discount: 0.05,
      tier: 'standard'
    }
  }];
}
```

---

## 模式 4：$node - 引用其他节点

**用法**：较少用，但在特定场景很强大

**适用场景：**
- 需要某个具名节点的数据
- 合并多个节点的数据
- 访问工作流执行相关的元数据

### 基本用法

```javascript
// Get output from specific node
const webhookData = $node["Webhook"].json;
const apiData = $node["HTTP Request"].json;

return [{
  json: {
    fromWebhook: webhookData,
    fromAPI: apiData
  }
}];
```

### 示例 1：合并多个数据源

```javascript
// Reference multiple nodes
const webhook = $node["Webhook"].json;
const database = $node["Postgres"].json;
const api = $node["HTTP Request"].json;

return [{
  json: {
    combined: {
      webhook: webhook.body,
      dbRecords: database.length,
      apiResponse: api.status
    },
    processedAt: new Date().toISOString()
  }
}];
```

### 示例 2：跨节点比较

```javascript
const oldData = $node["Get Old Data"].json;
const newData = $node["Get New Data"].json;

// Compare
const changes = {
  added: newData.filter(n => !oldData.find(o => o.id === n.id)),
  removed: oldData.filter(o => !newData.find(n => n.id === o.id)),
  modified: newData.filter(n => {
    const old = oldData.find(o => o.id === n.id);
    return old && JSON.stringify(old) !== JSON.stringify(n);
  })
};

return [{
  json: {
    changes,
    summary: {
      added: changes.added.length,
      removed: changes.removed.length,
      modified: changes.modified.length
    }
  }
}];
```

### 示例 3：访问节点元数据

```javascript
// Get data from specific execution path
const ifTrueBranch = $node["IF True"].json;
const ifFalseBranch = $node["IF False"].json;

// Use whichever branch executed
const result = ifTrueBranch || ifFalseBranch || {};

return [{json: result}];
```

---

## 关键点：Webhook 数据结构

**最常见错误**：忘了 webhook 数据嵌套在 `.body` 之下

### 问题所在

Webhook 节点把所有传入数据都包在 `body` 属性下。很多开发者都会在这里栽跟头。

### 结构

```javascript
// Webhook node output structure:
{
  "headers": {
    "content-type": "application/json",
    "user-agent": "...",
    // ... other headers
  },
  "params": {},
  "query": {},
  "body": {
    // ← YOUR DATA IS HERE
    "name": "Alice",
    "email": "alice@example.com",
    "message": "Hello!"
  }
}
```

### 错误与正确写法

```javascript
// ❌ WRONG: Trying to access directly
const name = $json.name;  // undefined
const email = $json.email;  // undefined

// ✅ CORRECT: Access via .body
const name = $json.body.name;  // "Alice"
const email = $json.body.email;  // "alice@example.com"

// ✅ CORRECT: Extract body first
const webhookData = $json.body;
const name = webhookData.name;  // "Alice"
const email = webhookData.email;  // "alice@example.com"
```

### 示例：完整的 Webhook 处理

```javascript
// Get webhook data from previous node
const webhookOutput = $input.first().json;

// Access the actual payload
const payload = webhookOutput.body;

// Access headers if needed
const contentType = webhookOutput.headers['content-type'];

// Access query parameters if needed
const apiKey = webhookOutput.query.api_key;

// Process the actual data
return [{
  json: {
    // Data from webhook body
    userName: payload.name,
    userEmail: payload.email,
    message: payload.message,

    // Metadata
    receivedAt: new Date().toISOString(),
    contentType: contentType,
    authenticated: !!apiKey
  }
}];
```

### POST 数据、查询参数与请求头

```javascript
const webhook = $input.first().json;

return [{
  json: {
    // POST body data
    formData: webhook.body,

    // Query parameters (?key=value)
    queryParams: webhook.query,

    // HTTP headers
    userAgent: webhook.headers['user-agent'],
    contentType: webhook.headers['content-type'],

    // Request metadata
    method: webhook.method,  // POST, GET, etc.
    url: webhook.url
  }
}];
```

### 常见 Webhook 场景

```javascript
// Scenario 1: Form submission
const formData = $json.body;
const name = formData.name;
const email = formData.email;

// Scenario 2: JSON API webhook
const apiPayload = $json.body;
const eventType = apiPayload.event;
const data = apiPayload.data;

// Scenario 3: Query parameters
const apiKey = $json.query.api_key;
const userId = $json.query.user_id;

// Scenario 4: Headers
const authorization = $json.headers['authorization'];
const signature = $json.headers['x-signature'];
```

---

## 如何选对模式

### 决策树

```
Do you need ALL items from previous node?
├─ YES → Use $input.all()
│
└─ NO → Do you need just the FIRST item?
    ├─ YES → Use $input.first()
    │
    └─ NO → Are you in "Each Item" mode?
        ├─ YES → Use $input.item
        │
        └─ NO → Do you need specific node data?
            ├─ YES → Use $node["NodeName"]
            └─ NO → Use $input.first() (default)
```

### 速查表

| 场景 | 用这个 | 示例 |
|----------|----------|---------|
| 汇总所有金额 | `$input.all()` | `allItems.reduce((sum, i) => sum + i.json.amount, 0)` |
| 获取 API 响应 | `$input.first()` | `$input.first().json.data` |
| 独立处理每个条目 | `$input.item` | `$input.item.json`（Each Item 模式） |
| 合并两个节点 | `$node["Name"]` | `$node["API"].json` |
| 过滤数组 | `$input.all()` | `allItems.filter(i => i.json.active)` |
| 转换单个对象 | `$input.first()` | `{...input.first().json, new: true}` |
| Webhook 数据 | `$input.first()` | `$input.first().json.body` |

---

## 常见错误

### 错误 1：脱离上下文使用 $json

```javascript
// ❌ WRONG: $json is ambiguous
const value = $json.field;

// ✅ CORRECT: Be explicit
const value = $input.first().json.field;
```

### 错误 2：忘了 .json 属性

```javascript
// ❌ WRONG: Trying to access fields on item object
const items = $input.all();
const names = items.map(item => item.name);  // undefined

// ✅ CORRECT: Access via .json
const names = items.map(item => item.json.name);
```

### 错误 3：在 All Items 模式下使用 $input.item

```javascript
// ❌ WRONG: $input.item is undefined in "All Items" mode
const data = $input.item.json;  // Error!

// ✅ CORRECT: Use appropriate method
const data = $input.first().json;  // Or $input.all()
```

### 错误 4：不处理空数组

```javascript
// ❌ WRONG: Crashes if no items
const first = $input.all()[0].json;

// ✅ CORRECT: Check length first
const items = $input.all();
if (items.length === 0) {
  return [];
}
const first = items[0].json;

// ✅ ALSO CORRECT: Use $input.first()
const first = $input.first().json;  // Built-in safety
```

### 错误 5：修改原始数据

```javascript
// ❌ RISKY: Mutating original
const items = $input.all();
items[0].json.modified = true;  // Modifies original
return items;

// ✅ SAFE: Create new objects
const items = $input.all();
return items.map(item => ({
  json: {
    ...item.json,
    modified: true
  }
}));
```

---

## 进阶模式

### 模式：分页处理

不要在 Code 里自己攒分页。HTTP Request 节点的分页选项会抓取每一页并返回合并后的条目（支持页码、offset、cursor、下一页 URL 四类 API，带页数上限）：见 `n8n-node-configuration` → NATIVE_NODES.md → "HTTP Request pagination"。只有在某个 API 的翻页规则该选项表达不了时才在 Code 里分页，且那属于循环例外，要写 `Why Code:` 说明。

### 模式：条件节点引用

```javascript
// Access different nodes based on condition
const condition = $input.first().json.type;

let data;
if (condition === 'api') {
  data = $node["API Response"].json;
} else if (condition === 'database') {
  data = $node["Database"].json;
} else {
  data = $node["Default"].json;
}

return [{json: data}];
```

### 模式：多节点聚合

原生节点优先：`append` 模式的 Merge 节点（把 `numberInputs` 设为分支数）不用代码就能汇总各分支输出。只有在数据源是可选或条件性的、Merge 会一直等永不执行的分支时，才动用这个模式。

```javascript
// Collect data from multiple named nodes
const sources = ['Source1', 'Source2', 'Source3'];
const allData = [];

for (const source of sources) {
  const nodeData = $node[source]?.json;
  if (nodeData) {
    allData.push({
      source,
      data: nodeData
    });
  }
}

return allData.map(item => ({json: item}));
```

---

## 小结

**最常用模式**：
1. `$input.all()` - 处理多条目、批量操作
2. `$input.first()` - 单条目、API 响应
3. `$input.item` - Each Item 模式下的逐条处理

**关键规则**：
- Webhook 数据在 `.body` 属性下

**最佳实践**：
- 写明确：用 `$input.first().json.field` 而不是 `$json.field`
- 始终检查 null/undefined
- 按模式选对方法（All Items 还是 Each Item）

**另见**：
- [SKILL.md](SKILL.md) - 概述与快速上手
- [COMMON_PATTERNS.md](COMMON_PATTERNS.md) - 生产级模式
- [ERROR_PATTERNS.md](ERROR_PATTERNS.md) - 避开常见错误

---

## 模式性能：为什么 "All Items" 更快

模式选择是 Code 节点里最大的性能杠杆，这个道理也适用于工作流的其余部分。n8n 每次把条目交给一个*逐条目*执行上下文，都要付出一次初始化开销。以下为 n8n 2.x 实例上的实测（小记录，约 1 万条）：

| 每条目执行什么 | 大约开销 | 原因 |
|---|---|---|
| Code **All Items**（整组只跑一次） | ~0.02 ms/item | 上下文只初始化一次，之后就是纯 JS，循环本身不额外花钱 |
| 任意节点里的表达式（IF / Set 等） | ~0.2 ms/item | 每条目一个轻量求值上下文 |
| Code **Each Item** | ~0.6 ms/item | 每条目一个完整代码沙箱，约为表达式的 3 倍、All Items 的 25–30 倍 |

所以对 1 万条目跑 `Run Once for Each Item`，纯开销约 6 秒；同样的逻辑在 `Run Once for All Items` 里只要约 0.2 秒。只有当条目确实需要隔离（独立的错误处理，或无法批量化的逐条 API 调用）时才用 Each Item；否则应在一个 All Items 节点*内部*循环。

两个你会经常碰到的推论：

- **表达式复杂度基本免费。** 复杂的 `{{ }}` 和简单的量出来一样：约 90% 的开销在 n8n 构建逐条目上下文，不在执行你的代码。别为提速简化表达式；要去减少*逐条目边界*的数量。
- **节点之间的每一次跳转都会把所有条目重新复制一遍**（每跳约 0.05 ms/item）。六个串联的 All Items Code 节点，开销约为一个节点做完同样六步的 7 倍。在实测过的热路径上（数千条目、以转换为主），这构成"单个 All Items 节点"这种重型例外，要在它的 `Why Code:` 说明里记录；低于这个量级，原生节点在可读性上更胜。绝不串联多个 *Each Item* Code 节点，逐条目的税会乘以节点数（6 节点 Each-Item 链跑 2000 条 ≈ 7 秒）。

**规模检查：** 几百条以下，这些都在 100 毫秒以内，不值得操心；而且多数真实工作流的耗时被 I/O 主导（HTTP / DB / Sheets 往返），节点开销微不足道。这些规则只用于热路径（条目多而 I/O 少），不要到处套用。

---

## 生产环境陷阱

来自真实 n8n 工作流部署的血泪教训。

### SplitInBatches 循环语义

SplitInBatches 节点有两个输出，命名很反直觉：
- `main[0]` = **done**，全部批次处理完后只触发一次
- `main[1]` = **each batch**，每个批次都触发（这就是循环体）

在 done 输出之后、下游处理之前，始终加一个 **Limit 1** 节点，防止 done 带着多余条目触发的边界情况。

### SplitInBatches：迭代次数就是成本

每次循环迭代都由工作流引擎重新执行整个循环体，每迭代约 0.8 毫秒纯开销，还不算循环体自身的开销。总计 ≈ `⌈items / batchSize⌉ × (~0.8 ms + body cost)`：

- 对 N 条目设 `batchSize: 1`，这份开销要付 N 次，等于循环版的 *Run Once for Each Item*（循环体里有多个节点的话，每次迭代还要把它们全部重付一遍）。
- 调大 `batchSize` 会按比例减少迭代次数，循环体仍然处理每个条目。在真实约束（API 限速、页大小、内存）允许的范围内，用**最大的批次**。如果根本不需要分批，就别循环：在一个 All Items 节点里处理整组数据。

### 跨迭代数据累积（关键）

SplitInBatches 循环结束后，`$('Node Inside Loop').all()` 返回的**只有最后一次迭代的数据**，不是累计结果。除最后一批之外的数据会被悄悄丢掉。

**修复方法**：用 workflow static data 跨迭代累积：

```javascript
// BEFORE the loop (reset accumulator):
const staticData = $getWorkflowStaticData('global');
staticData.results = [];
return $input.all();

// INSIDE the loop body (accumulate):
const staticData = $getWorkflowStaticData('global');
const results = [];
for (const item of $input.all()) {
  const processed = { /* ... */ };
  results.push({ json: processed });
  staticData.results.push(processed);
}
return results;

// AFTER the loop (read accumulated data):
const staticData = $getWorkflowStaticData('global');
const allResults = staticData.results || [];
// Now aggregate across ALL iterations
```

### 为新输出条目补 pairedItem

新建条目与输入条目不是一一对应时，要带上 `pairedItem`，否则下游 Set 节点会报 `paired_item_no_info` 而失败：

```javascript
const results = [];
for (let i = 0; i < $input.all().length; i++) {
  const item = $input.all()[i];
  results.push({
    json: { /* new data */ },
    pairedItem: { item: i }
  });
}
return results;
```

### 正确的节点引用语法

```javascript
// ❌ WRONG - .json directly on node reference
const data = $('HTTP Request').json;

// ✅ CORRECT - call .first() then access .json
const data = $('HTTP Request').first().json;

// ✅ Also correct - get all items
const allData = $('HTTP Request').all();
```

### 价格/货币比较的浮点精度

比较价格或货币数值时，浮点误差会造成误报。按分取整再比较：

```javascript
// ❌ Unreliable - float comparison
if (newPrice !== oldPrice) { /* triggers on noise */ }

// ✅ Reliable - compare at cent level
if (Math.round(newPrice * 100) !== Math.round(oldPrice * 100)) {
  // Real price change detected
}
```
