> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-code-javascript/BUILTIN_FUNCTIONS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 内置函数（JavaScript Code 节点）

n8n 内置 JavaScript 函数与辅助工具的完整参考。

---

## 概述

n8n Code 节点在标准 JavaScript 之外还提供强大的内置函数。本指南涵盖：

1. **沙箱限制** - 哪些被禁用以及为什么（先读这节）
2. **this.helpers.httpRequest()** - 发起 HTTP 请求（裸的 `$helpers` 全局变量在 task runner 中未定义）
3. **DateTime (Luxon)** - 高级日期/时间操作
4. **$jmespath()** - 查询 JSON 结构
5. **$getWorkflowStaticData()** - 持久化存储
6. **标准 JavaScript 全局对象** - Math、JSON、console 等
7. **可用的 Node.js 模块** - crypto、Buffer、URL

---

## 0. 沙箱限制（关键）

自 n8n v2.0 起，Code 节点运行在 **task runner 沙箱**（`JsTaskRunnerSandbox`）内，它刻意禁用了若干 API。旧的 vm2 沙箱正在被移除。弄清哪些被禁用，能省下数小时的排查："为什么激活后抛错，编辑器预览里却正常。"

### 被禁用的 helper

```javascript
// ❌ BLOCKED — throws UnsupportedFunctionError
await this.helpers.httpRequestWithAuthentication.call(this, 'credType', { ... });
await this.helpers.requestWithAuthenticationPaginated.call(this, { ... }, 'credType');
```

n8n 源码注释解释了原因：*"这些 helper 依赖检查当前节点类型（Code Node）的凭据，而 Code Node 没有凭据。"* 在 task runner 里**没有任何环境变量能重新启用它们**，禁用名单是编译进去的（`packages/@n8n/task-runner/src/runner-types.ts`）。

**解决办法**：不要试图在 Code 节点内部做认证。改为以下二者之一：
- 用挂了凭据的 HTTP Request 节点替换 Code 节点（标准做法），或者
- 让 Code 节点准备好 payload，然后委托给子工作流，由其 HTTP Request 节点持有凭据。

### `$env` 可能被禁用

`$env` 受 **`N8N_BLOCK_ENV_ACCESS_IN_NODE`** 控制。设为 `true` 时（生产环境常见的加固手段），任何对 `$env.SOMETHING` 的引用都会抛错。由于在 Code 节点内部无法判断它是否启用，**可移植的 Skill 不要依赖 `$env`**：把密钥当作凭据问题（交给 HTTP Request 节点），而不是 Code 节点的问题。

### `require()` 受白名单控制

```javascript
// May throw "Cannot find module 'crypto'" — depends on env vars
const crypto = require('crypto');
```

内置模块需要把 `N8N_RUNNERS_ALLOWED_BUILT_IN_MODULES`（或旧的 `NODE_FUNCTION_ALLOW_BUILTIN`）设为 `*`，或设为包含 `crypto` 的逗号分隔列表。外部 npm 包需要 `N8N_RUNNERS_ALLOWED_EXTERNAL_MODULES`，且该包要装进 runner 镜像。默认安装两者都没设置，`require()` 会抛错。

`Buffer` 和 `URL` 是全局变量（不需要 `require`），所以始终可用。

### 始终安全的内容

`$input.*`、`$json`、`$node[…]`、`this.helpers.httpRequest()`（不带认证）、`$jmespath()`、`$getWorkflowStaticData()`、`DateTime`（Luxon），以及所有标准 JavaScript 全局对象（`Math`、`JSON`、`Object`、`Array`、`console`、`Buffer`、`URL`、`URLSearchParams`）。

> **访问器陷阱**：裸的 `$helpers` 全局变量在 task runner 沙箱中是 **undefined** 的，`$helpers.httpRequest()` 会抛 `ReferenceError: $helpers is not defined`。可用的访问器是 **`this.helpers.httpRequest()`**（在丢失 `this` 的嵌套 async 函数里，用 `await fn.call(this, ...)` 调用）。n8n-mcp 校验器可能会错误地建议用 `$helpers`，忽略它。凡超出简单无认证 GET 的场景（分页、重试、凭据），优先用 **HTTP Request 节点**，Code 节点只留纯逻辑。

---

## 1. this.helpers.httpRequest() - HTTP 请求

在 Code 逻辑内部调用 API，例如递归算法的每一步做一次查询。单纯的一次 API 调用、翻页、重试或凭据，都应放进 HTTP Request 节点。访问器是 `this.helpers.httpRequest()`：裸的 `$helpers` 全局变量在 task runner 沙箱中未定义，会抛 `ReferenceError: $helpers is not defined`。非简单调用（分页、重试、凭据）请优先用 HTTP Request 节点。

### 基本用法

```javascript
const response = await this.helpers.httpRequest({
  method: 'GET',
  url: 'https://api.example.com/users'
});

return [{json: {data: response}}];
```

### 完整选项

```javascript
const response = await this.helpers.httpRequest({
  method: 'POST',  // GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS
  url: 'https://api.example.com/users',
  headers: {
    'Authorization': 'Bearer token123',
    'Content-Type': 'application/json',
    'User-Agent': 'n8n-workflow'
  },
  body: {
    name: 'John Doe',
    email: 'john@example.com'
  },
  qs: {  // Query string parameters
    page: 1,
    limit: 10
  },
  timeout: 10000,  // Milliseconds (default: no timeout)
  json: true,  // Auto-parse JSON response (default: true)
  simple: false,  // Don't throw on HTTP errors (default: true)
  resolveWithFullResponse: false  // Return only body (default: false)
});
```

### GET 请求

```javascript
// Simple GET
const users = await this.helpers.httpRequest({
  method: 'GET',
  url: 'https://api.example.com/users'
});

return [{json: {users}}];
```

```javascript
// GET with query parameters
const results = await this.helpers.httpRequest({
  method: 'GET',
  url: 'https://api.example.com/search',
  qs: {
    q: 'javascript',
    page: 1,
    per_page: 50
  }
});

return [{json: results}];
```

### POST 请求

```javascript
// POST with JSON body
// NOTE: For authenticated APIs, prefer an HTTP Request node with a credential
// attached. Embedding the token in a Code node only works when (a) the token
// arrives as runtime data (e.g. from a previous node), or (b) you're sure
// $env access is enabled on this instance. See section 0.
const apiToken = $input.first().json.apiToken;  // passed in from a credential-aware upstream node

const newUser = await this.helpers.httpRequest({
  method: 'POST',
  url: 'https://api.example.com/users',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${apiToken}`
  },
  body: {
    name: $json.body.name,
    email: $json.body.email,
    role: 'user'
  }
});

return [{json: newUser}];
```

### PUT/PATCH 请求

```javascript
// Update resource
const updated = await this.helpers.httpRequest({
  method: 'PATCH',
  url: `https://api.example.com/users/${userId}`,
  body: {
    name: 'Updated Name',
    status: 'active'
  }
});

return [{json: updated}];
```

### DELETE 请求

```javascript
// Delete resource
await this.helpers.httpRequest({
  method: 'DELETE',
  url: `https://api.example.com/users/${userId}`,
  headers: {
    'Authorization': `Bearer ${apiToken}`  // token passed in from upstream node, not $env
  }
});

return [{json: {deleted: true, userId}}];
```

### 认证模式

> **强烈建议**：不要在 Code 节点内做认证。用挂了凭据的 HTTP Request 节点，或委托给由 HTTP Request 节点持有凭据的子工作流。下面的模式只在 token 确实作为数据流经工作流时才适用。

```javascript
// Bearer Token (token came from a previous node, not $env)
const response = await this.helpers.httpRequest({
  url: 'https://api.example.com/data',
  headers: {
    'Authorization': `Bearer ${$input.first().json.token}`
  }
});
```

```javascript
// API Key in Header (key came from a previous node, not $env)
const response = await this.helpers.httpRequest({
  url: 'https://api.example.com/data',
  headers: {
    'X-API-Key': $input.first().json.apiKey
  }
});
```

```javascript
// Basic Auth (manual)
const credentials = Buffer.from(`${username}:${password}`).toString('base64');

const response = await this.helpers.httpRequest({
  url: 'https://api.example.com/data',
  headers: {
    'Authorization': `Basic ${credentials}`
  }
});
```

### 错误处理

```javascript
// Handle HTTP errors gracefully
try {
  const response = await this.helpers.httpRequest({
    method: 'GET',
    url: 'https://api.example.com/users',
    simple: false  // Don't throw on 4xx/5xx
  });

  if (response.statusCode >= 200 && response.statusCode < 300) {
    return [{json: {success: true, data: response.body}}];
  } else {
    return [{
      json: {
        success: false,
        status: response.statusCode,
        error: response.body
      }
    }];
  }
} catch (error) {
  return [{
    json: {
      success: false,
      error: error.message
    }
  }];
}
```

### 完整响应访问

```javascript
// Get full response including headers and status
const response = await this.helpers.httpRequest({
  url: 'https://api.example.com/data',
  resolveWithFullResponse: true
});

return [{
  json: {
    statusCode: response.statusCode,
    headers: response.headers,
    body: response.body,
    rateLimit: response.headers['x-ratelimit-remaining']
  }
}];
```

---

## 2. DateTime (Luxon) - 日期与时间操作

n8n 内置 Luxon，提供强大的日期/时间处理。通过 `DateTime` 全局对象访问。

### 当前日期/时间

```javascript
// Current time
const now = DateTime.now();

// Current time in specific timezone
const nowTokyo = DateTime.now().setZone('Asia/Tokyo');

// Today at midnight
const today = DateTime.now().startOf('day');

return [{
  json: {
    iso: now.toISO(),  // "2025-01-20T15:30:00.000Z"
    formatted: now.toFormat('yyyy-MM-dd HH:mm:ss'),  // "2025-01-20 15:30:00"
    unix: now.toSeconds(),  // Unix timestamp
    millis: now.toMillis()  // Milliseconds since epoch
  }
}];
```

### 日期格式化

```javascript
const now = DateTime.now();

return [{
  json: {
    isoFormat: now.toISO(),  // ISO 8601: "2025-01-20T15:30:00.000Z"
    sqlFormat: now.toSQL(),  // SQL: "2025-01-20 15:30:00.000"
    httpFormat: now.toHTTP(),  // HTTP: "Mon, 20 Jan 2025 15:30:00 GMT"

    // Custom formats
    dateOnly: now.toFormat('yyyy-MM-dd'),  // "2025-01-20"
    timeOnly: now.toFormat('HH:mm:ss'),  // "15:30:00"
    readable: now.toFormat('MMMM dd, yyyy'),  // "January 20, 2025"
    compact: now.toFormat('yyyyMMdd'),  // "20250120"
    withDay: now.toFormat('EEEE, MMMM dd, yyyy'),  // "Monday, January 20, 2025"
    custom: now.toFormat('dd/MM/yy HH:mm')  // "20/01/25 15:30"
  }
}];
```

### 解析日期

```javascript
// From ISO string
const dt1 = DateTime.fromISO('2025-01-20T15:30:00');

// From specific format
const dt2 = DateTime.fromFormat('01/20/2025', 'MM/dd/yyyy');

// From SQL
const dt3 = DateTime.fromSQL('2025-01-20 15:30:00');

// From Unix timestamp
const dt4 = DateTime.fromSeconds(1737384600);

// From milliseconds
const dt5 = DateTime.fromMillis(1737384600000);

return [{json: {parsed: dt1.toISO()}}];
```

### 日期运算

```javascript
const now = DateTime.now();

return [{
  json: {
    // Adding time
    tomorrow: now.plus({days: 1}).toISO(),
    nextWeek: now.plus({weeks: 1}).toISO(),
    nextMonth: now.plus({months: 1}).toISO(),
    inTwoHours: now.plus({hours: 2}).toISO(),

    // Subtracting time
    yesterday: now.minus({days: 1}).toISO(),
    lastWeek: now.minus({weeks: 1}).toISO(),
    lastMonth: now.minus({months: 1}).toISO(),
    twoHoursAgo: now.minus({hours: 2}).toISO(),

    // Complex operations
    in90Days: now.plus({days: 90}).toFormat('yyyy-MM-dd'),
    in6Months: now.plus({months: 6}).toFormat('yyyy-MM-dd')
  }
}];
```

### 时间比较

```javascript
const now = DateTime.now();
const targetDate = DateTime.fromISO('2025-12-31');

return [{
  json: {
    // Comparisons
    isFuture: targetDate > now,
    isPast: targetDate < now,
    isEqual: targetDate.equals(now),

    // Differences
    daysUntil: targetDate.diff(now, 'days').days,
    hoursUntil: targetDate.diff(now, 'hours').hours,
    monthsUntil: targetDate.diff(now, 'months').months,

    // Detailed difference
    detailedDiff: targetDate.diff(now, ['months', 'days', 'hours']).toObject()
  }
}];
```

### 时区操作

```javascript
const now = DateTime.now();

return [{
  json: {
    // Current timezone
    local: now.toISO(),

    // Convert to different timezone
    tokyo: now.setZone('Asia/Tokyo').toISO(),
    newYork: now.setZone('America/New_York').toISO(),
    london: now.setZone('Europe/London').toISO(),
    utc: now.toUTC().toISO(),

    // Get timezone info
    timezone: now.zoneName,  // "America/Los_Angeles"
    offset: now.offset,  // Offset in minutes
    offsetFormatted: now.toFormat('ZZ')  // "+08:00"
  }
}];
```

### 时间段的起点/终点

```javascript
const now = DateTime.now();

return [{
  json: {
    startOfDay: now.startOf('day').toISO(),
    endOfDay: now.endOf('day').toISO(),
    startOfWeek: now.startOf('week').toISO(),
    endOfWeek: now.endOf('week').toISO(),
    startOfMonth: now.startOf('month').toISO(),
    endOfMonth: now.endOf('month').toISO(),
    startOfYear: now.startOf('year').toISO(),
    endOfYear: now.endOf('year').toISO()
  }
}];
```

### 星期与月份信息

```javascript
const now = DateTime.now();

return [{
  json: {
    // Day info
    weekday: now.weekday,  // 1 = Monday, 7 = Sunday
    weekdayShort: now.weekdayShort,  // "Mon"
    weekdayLong: now.weekdayLong,  // "Monday"
    isWeekend: now.weekday > 5,  // Saturday or Sunday

    // Month info
    month: now.month,  // 1-12
    monthShort: now.monthShort,  // "Jan"
    monthLong: now.monthLong,  // "January"

    // Year info
    year: now.year,  // 2025
    quarter: now.quarter,  // 1-4
    daysInMonth: now.daysInMonth  // 28-31
  }
}];
```

---

## 3. $jmespath() - JSON 查询

使用 JMESPath 语法查询和转换 JSON 结构。

> **先考虑表达式。** `$jmespath` 在 `{{ }}` 里用法相同，只喂一个字段的查询很少需要 Code 节点。
> 见 **n8n-expression-syntax** → `$jmespath()`。

### 容易踩的规则（在 n8n 2.38 上验证）

- **参数顺序是 `$jmespath(object, query)`**，与 JMESPath 官方文档（`search(query, data)`）相反。
  顺序颠倒，或把字符串/`undefined` 当作对象传入，会抛
  `expected two arguments (Object, string) for this function`。
- **字符串字面量用单引号**（`tier == 'premium'`），所以要用 JS
  **双引号**字符串包裹查询。查询里用双引号写的 `"premium"` 是*字段名*，会
  静默返回 `[]`。
- **数字和布尔值用反引号**（`` age >= `18` ``、`` inStock == `true` ``）。裸写的
  `18` 是解析错误。
- 用 `&&` `||` `!` `==`，不要用 `and` / `or` / `=`。
- **对 `$input.all()` 的条目**，要带上包装层（`[?json.age >= \`18\`].json.name`），或先 map：
  `$jmespath($input.all().map(i => i.json), '[?age >= \`18\`].name')`。
- **解析错误在 Code 节点中会抛出**，但报错信息会被 task runner 弄乱：
  `Cannot assign to read only property 'name' of object 'Error: Invalid token (Number): "18"'`。
  看到它时先检查查询里的字面量。（在 `{{ }}` 里同样的错误会静默变成
  `null`。）
- 路径缺失 → `null`；过滤器无匹配 → `[]`。

### 基础查询

```javascript
const data = $input.first().json;

// Extract specific field
const names = $jmespath(data, 'users[*].name');

// Filter array
const adults = $jmespath(data, 'users[?age >= `18`]');

// Get specific index
const firstUser = $jmespath(data, 'users[0]');

return [{json: {names, adults, firstUser}}];
```

### 高级查询

```javascript
const data = $input.first().json;

// Sort and slice
const top5 = $jmespath(data, 'users | sort_by(@, &score) | reverse(@) | [0:5]');

// Extract nested fields
const emails = $jmespath(data, 'users[*].contact.email');

// Multi-field extraction
const simplified = $jmespath(data, 'users[*].{name: name, email: contact.email}');

// Conditional filtering
const premium = $jmespath(data, "users[?subscription.tier == 'premium']");

return [{json: {top5, emails, simplified, premium}}];
```

### 常见模式

```javascript
// Pattern 1: Filter and project
const query1 = $jmespath(data, 'products[?price > `100`].{name: name, price: price}');

// Pattern 2: Aggregate functions
const query2 = $jmespath(data, 'sum(products[*].price)');
const query3 = $jmespath(data, 'max(products[*].price)');
const query4 = $jmespath(data, 'length(products)');

// Pattern 3: Nested filtering
const query5 = $jmespath(data, 'categories[*].products[?inStock == `true`]');

return [{json: {query1, query2, query3, query4, query5}}];
```

---

## 4. $getWorkflowStaticData() - 持久化存储

存储跨工作流执行而持久保留的数据。

### 基本用法

```javascript
// Get static data storage
const staticData = $getWorkflowStaticData();

// Initialize counter if doesn't exist
if (!staticData.counter) {
  staticData.counter = 0;
}

// Increment counter
staticData.counter++;

return [{
  json: {
    executionCount: staticData.counter
  }
}];
```

### 使用场景

```javascript
// Use Case 1: Rate limiting
const staticData = $getWorkflowStaticData();
const now = Date.now();

if (!staticData.lastRun) {
  staticData.lastRun = now;
  staticData.runCount = 1;
} else {
  const timeSinceLastRun = now - staticData.lastRun;

  if (timeSinceLastRun < 60000) {  // Less than 1 minute
    return [{json: {error: 'Rate limit: wait 1 minute between runs'}}];
  }

  staticData.lastRun = now;
  staticData.runCount++;
}

return [{json: {allowed: true, totalRuns: staticData.runCount}}];
```

```javascript
// Use Case 2: Tracking last processed ID
const staticData = $getWorkflowStaticData();
const currentItems = $input.all();

// Get last processed ID
const lastId = staticData.lastProcessedId || 0;

// Filter only new items
const newItems = currentItems.filter(item => item.json.id > lastId);

// Update last processed ID
if (newItems.length > 0) {
  staticData.lastProcessedId = Math.max(...newItems.map(item => item.json.id));
}

return newItems;
```

```javascript
// Use Case 3: Accumulating results
const staticData = $getWorkflowStaticData();

if (!staticData.accumulated) {
  staticData.accumulated = [];
}

// Add current items to accumulated list
const currentData = $input.all().map(item => item.json);
staticData.accumulated.push(...currentData);

return [{
  json: {
    currentBatch: currentData.length,
    totalAccumulated: staticData.accumulated.length,
    allData: staticData.accumulated
  }
}];
```

---

## 5. 标准 JavaScript 全局对象

### Math 对象

```javascript
return [{
  json: {
    // Rounding
    rounded: Math.round(3.7),  // 4
    floor: Math.floor(3.7),  // 3
    ceil: Math.ceil(3.2),  // 4

    // Min/Max
    max: Math.max(1, 5, 3, 9, 2),  // 9
    min: Math.min(1, 5, 3, 9, 2),  // 1

    // Random
    random: Math.random(),  // 0-1
    randomInt: Math.floor(Math.random() * 100),  // 0-99

    // Other
    abs: Math.abs(-5),  // 5
    sqrt: Math.sqrt(16),  // 4
    pow: Math.pow(2, 3)  // 8
  }
}];
```

### JSON 对象

```javascript
// Parse JSON string
const jsonString = '{"name": "John", "age": 30}';
const parsed = JSON.parse(jsonString);

// Stringify object
const obj = {name: "John", age: 30};
const stringified = JSON.stringify(obj);

// Pretty print
const pretty = JSON.stringify(obj, null, 2);

return [{json: {parsed, stringified, pretty}}];
```

### console 对象

```javascript
// Debug logging (appears in browser console, press F12)
console.log('Processing items:', $input.all().length);
console.log('First item:', $input.first().json);

// Other console methods
console.error('Error message');
console.warn('Warning message');
console.info('Info message');

// Continues to return data
return [{json: {processed: true}}];
```

### Object 方法

```javascript
const obj = {name: "John", age: 30, city: "NYC"};

return [{
  json: {
    keys: Object.keys(obj),  // ["name", "age", "city"]
    values: Object.values(obj),  // ["John", 30, "NYC"]
    entries: Object.entries(obj),  // [["name", "John"], ...]

    // Check property
    hasName: 'name' in obj,  // true

    // Merge objects
    merged: Object.assign({}, obj, {country: "USA"})
  }
}];
```

### Array 方法

```javascript
const arr = [1, 2, 3, 4, 5];

return [{
  json: {
    mapped: arr.map(x => x * 2),  // [2, 4, 6, 8, 10]
    filtered: arr.filter(x => x > 2),  // [3, 4, 5]
    reduced: arr.reduce((sum, x) => sum + x, 0),  // 15
    some: arr.some(x => x > 3),  // true
    every: arr.every(x => x > 0),  // true
    find: arr.find(x => x > 3),  // 4
    includes: arr.includes(3),  // true
    joined: arr.join(', ')  // "1, 2, 3, 4, 5"
  }
}];
```

---

## 6. 可用的 Node.js 模块

### crypto 模块

> **受控**：`require('crypto')` 只有在 `N8N_RUNNERS_ALLOWED_BUILT_IN_MODULES`（或旧的 `NODE_FUNCTION_ALLOW_BUILTIN`）包含 `crypto`（或为 `*`）时才可用。默认安装会抛 "Cannot find module 'crypto'"。哈希、HMAC、签名或 UUID 请改用 **Crypto 节点**（typeVersion 2；HMAC 与签名密钥来自 `crypto` 凭据），不需要白名单。只在 Crypto 节点做不到、且确认实例允许时才用 `require('crypto')`。

```javascript
const crypto = require('crypto');

// Hash functions
const hash = crypto.createHash('sha256')
  .update('my secret text')
  .digest('hex');

// MD5 hash
const md5 = crypto.createHash('md5')
  .update('my text')
  .digest('hex');

// Random values
const randomBytes = crypto.randomBytes(16).toString('hex');

return [{json: {hash, md5, randomBytes}}];
```

### Buffer（内置）

```javascript
// Base64 encoding
const encoded = Buffer.from('Hello World').toString('base64');

// Base64 decoding
const decoded = Buffer.from(encoded, 'base64').toString();

// Hex encoding
const hex = Buffer.from('Hello').toString('hex');

return [{json: {encoded, decoded, hex}}];
```

### URL / URLSearchParams

```javascript
// Parse URL
const url = new URL('https://example.com/path?param1=value1&param2=value2');

// Build query string
const params = new URLSearchParams({
  search: 'query',
  page: 1,
  limit: 10
});

return [{
  json: {
    host: url.host,
    pathname: url.pathname,
    search: url.search,
    queryString: params.toString()  // "search=query&page=1&limit=10"
  }
}];
```

---

## 不可用的功能

**外部 npm 包不可用**（除非通过 `N8N_RUNNERS_ALLOWED_EXTERNAL_MODULES` 显式加入白名单*且*装进 runner 镜像，很少见）：
- ❌ axios
- ❌ lodash
- ❌ moment（改用 DateTime/Luxon）
- ❌ request
- ❌ 其他任何 npm 包

**认证 helper 在 task runner 沙箱中被禁用**（见第 0 节）：
- ❌ `this.helpers.httpRequestWithAuthentication`
- ❌ `this.helpers.requestWithAuthenticationPaginated`

**有条件禁用**（取决于实例配置）：
- ⚠️ `$env.*` — `N8N_BLOCK_ENV_ACCESS_IN_NODE=true` 时被禁用
- ⚠️ `require('crypto')` / `require('fs')` 等 — `N8N_RUNNERS_ALLOWED_BUILT_IN_MODULES` 不包含它们时被禁用

**解决办法**：
- 带认证的 HTTP → 挂凭据的 HTTP Request 节点，或子工作流模式
- 密钥 → 作为数据从上游 HTTP Request / 感知凭据的节点传入
- 哈希/加密 → Crypto 节点（hash、HMAC、sign、UUID），无需白名单

---

## 总结

**最有用的内置功能**：
1. **this.helpers.httpRequest()** - 在 Code 逻辑内调用 API；单纯的调用应放进 HTTP Request 节点（裸的 `$helpers` 全局变量未定义）
2. **DateTime** - 专业的日期/时间处理
3. **$jmespath()** - 复杂 JSON 查询
4. **Math、JSON、Object、Array** - 标准 JavaScript 工具

**常见模式**：
- API 调用：用 this.helpers.httpRequest()（更推荐 HTTP Request 节点）
- 日期操作：用 DateTime (Luxon)
- 数据过滤：Code 节点前放 Filter 节点；Code 内部用 $jmespath() 或 .filter()
- 持久数据：用 $getWorkflowStaticData()
- 哈希：用 Crypto 节点；`require('crypto')` 仅在白名单允许时使用

**另见**：
- [SKILL.md](SKILL.md) - 概述
- [COMMON_PATTERNS.md](COMMON_PATTERNS.md) - 实际用法示例
- [ERROR_PATTERNS.md](ERROR_PATTERNS.md) - 错误预防
