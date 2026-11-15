> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-code-javascript/ERROR_PATTERNS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 错误模式 - JavaScript Code 节点

避开 Code 节点最常见错误的完整指南。

---

## 概述

本指南覆盖 n8n Code 节点中**最常见的 5 类错误模式**。理解并避开它们，能省下大量调试时间。

**错误频率（大致排序）**：
1. 代码为空 / 缺 return：n8n 自己就会拒绝的最主要错误
2. 把表达式语法当代码：`{{ }}` 出现在该写 JavaScript 的地方
3. 返回结构：返回原始值/`null`（裸对象会自动包装）
4. 字符串断裂 / 转义：引号或括号不配对会抛 JS 语法错误
5. 缺空值检查：常见运行时错误

---

## 错误 #1：代码为空或缺少 return 语句

**频率**：最常见错误（占全部校验失败的 38%）

**现象**：
- 工作流执行失败
- 下游节点收不到数据
- 报错 "Code cannot be empty" 或 "Code must return data"

### 问题所在

```javascript
// ❌ ERROR: No code at all
// (Empty code field)
```

```javascript
// ❌ ERROR: Code executes but doesn't return anything
const items = $input.all();

// Process items
for (const item of items) {
  console.log(item.json.name);
}

// Forgot to return!
```

```javascript
// ❌ ERROR: Early return path exists, but not all paths return
const items = $input.all();

if (items.length === 0) {
  return [];  // ✅ This path returns
}

// Process items
const processed = items.map(item => ({json: item.json}));

// ❌ Forgot to return processed!
```

### 解决方法

```javascript
// ✅ CORRECT: Always return data
const items = $input.all();

// Process items
const processed = items.map(item => ({
  json: {
    ...item.json,
    processed: true
  }
}));

return processed;  // ✅ Return statement present
```

```javascript
// ✅ CORRECT: Return empty array if no items
const items = $input.all();

if (items.length === 0) {
  return [];  // Valid: empty array when no data
}

// Process and return
return items.map(item => ({json: item.json}));
```

```javascript
// ✅ CORRECT: All code paths return
const items = $input.all();

if (items.length === 0) {
  return [];
} else if (items.length === 1) {
  return [{json: {single: true, data: items[0].json}}];
} else {
  return items.map(item => ({json: item.json}));
}

// All paths covered
```

### 检查清单

- [ ] 代码字段不为空
- [ ] 存在 return 语句
- [ ] 所有代码路径都返回数据（if/else 各分支）
- [ ] 返回格式正确（`[{json: {...}}]`）
- [ ] 出错时也要返回（用 try-catch）

---

## 错误 #2：表达式语法混淆

**现象**：分两种情况，只有其中一种是语法错误：
- **字符串字面量里的 `{{ }}`**：是合法 JavaScript，能正常跑，但你得到的是 `{{ ... }}` 这段*字面文本*而不是值：n8n 不会在 Code 节点代码里求值表达式。这是逻辑 bug，不是校验错误。（n8n-mcp ≥ 2.63.0 不再标记字符串字面量里的 `{{ }}`：提示词模板、payload 占位符、`.replace()` 用的 token 都是合法的。）
- **`{{ }}` 当裸代码写**（如 `return {{ $json.x }}`）：真正的 JavaScript 语法错误。校验器报 "Expression syntax {{...}} is not valid in Code nodes"，n8n 抛 "Unexpected token"。

### 问题所在

n8n 有两套截然不同的语法：
1. **表达式语法** `{{ }}` - 用于其他节点（Set、IF、HTTP Request）
2. **JavaScript** - 用于 Code 节点

很多开发者想要一个*值*时，会误在 Code 节点里用表达式语法。把 `{{ }}` 放进字符串并不会插值：

```javascript
// ❌ LOGIC BUG: n8n never evaluates {{ }} in Code-node strings
const userName = "{{ $json.name }}";
const userEmail = "{{ $json.body.email }}";

return [{
  json: {
    name: userName,
    email: userEmail
  }
}];

// Result: Literal string "{{ $json.name }}", NOT the value!
// (This runs — it just doesn't do what you meant. Use $json.name directly.)
```

```javascript
// ❌ SYNTAX ERROR: {{ }} used as code, not inside a string
const value = {{ $now.toFormat('yyyy-MM-dd') }};  // "Unexpected token"
```

### 解决方法

```javascript
// ✅ CORRECT: Use JavaScript directly (no {{ }})
const userName = $json.name;
const userEmail = $json.body.email;

return [{
  json: {
    name: userName,
    email: userEmail
  }
}];
```

```javascript
// ✅ CORRECT: JavaScript template literals (use backticks)
const message = `Hello, ${$json.name}! Your email is ${$json.email}`;

return [{
  json: {
    greeting: message
  }
}];
```

```javascript
// ✅ CORRECT: Direct variable access
const item = $input.first().json;

return [{
  json: {
    name: item.name,
    email: item.email,
    timestamp: new Date().toISOString()  // JavaScript Date, not {{ }}
  }
}];
```

### 对比表

| 场景 | 语法 | 示例 |
|---------|--------|---------|
| Set 节点 | `{{ }}` 表达式 | `{{ $json.name }}` |
| IF 节点 | `{{ }}` 表达式 | `{{ $json.age > 18 }}` |
| HTTP Request URL | `{{ }}` 表达式 | `{{ $json.userId }}` |
| **Code 节点** | **JavaScript** | `$json.name` |
| **Code 节点字符串** | **模板字面量** | `` `Hello ${$json.name}` `` |

### 快速修复指南

```javascript
// WRONG → RIGHT conversions

// ❌ "{{ $json.field }}"
// ✅ $json.field

// ❌ "{{ $now }}"
// ✅ new Date().toISOString()

// ❌ "{{ $node['HTTP Request'].json.data }}"
// ✅ $node["HTTP Request"].json.data

// ❌ `{{ $json.firstName }} {{ $json.lastName }}`
// ✅ `${$json.firstName} ${$json.lastName}`
```

---

## 错误 #3：返回结构

**实际情况**：n8n 比旧建议所暗示的更宽容：
- 在 *Run Once for All Items* 模式下，n8n 会**自动规范化**单个裸对象或裸对象数组：给每个对象套一层 `json` 属性。所以这些写法能跑。
- 真正会失败、报 "Code doesn't return items properly" 的，是返回**原始值**（string/number/boolean）或 **`null`/`undefined`**：没有东西可包。

（n8n-mcp ≥ 2.63.0 不再对裸对象返回报 "Return value must be an array of objects" 错误；旧说法与 n8n 的自动包装行为相矛盾。）

### 优先用规范形式

规范形式 `[{json: {...}}]` 无歧义，且在两种执行模式下行为完全一致，尽管更松散的写法会被自动包装，仍应把它作为默认：

```javascript
// ⚠️ Auto-wrapped → [{json: {result: 'success'}}]. Runs, but prefer the array + json form.
return {
  json: {
    result: 'success'
  }
};
```

```javascript
// ⚠️ Auto-wrapped → each object gets a json wrapper. Runs, but be explicit.
return [
  {id: 1, name: 'Alice'},
  {id: 2, name: 'Bob'}
];
```

```javascript
// ✅ Fine — input items already carry a json property; returning them unchanged is a valid passthrough
return $input.all();
```

```javascript
// ❌ FAILS: primitive value — nothing to wrap into an item
return "processed";
```

```javascript
// ❌ FAILS: null / undefined — no items to pass on
return null;
```

### 解决方法

```javascript
// ✅ CORRECT: Single result
return [{
  json: {
    result: 'success',
    timestamp: new Date().toISOString()
  }
}];
```

```javascript
// ✅ CORRECT: Multiple results
return [
  {json: {id: 1, name: 'Alice'}},
  {json: {id: 2, name: 'Bob'}},
  {json: {id: 3, name: 'Carol'}}
];
```

```javascript
// ✅ CORRECT: Transforming array
const items = $input.all();

return items.map(item => ({
  json: {
    id: item.json.id,
    name: item.json.name,
    processed: true
  }
}));
```

```javascript
// ✅ CORRECT: Empty result
return [];
// Valid when no data to return
```

```javascript
// ✅ CORRECT: Conditional returns
if (shouldProcess) {
  return [{json: {result: 'processed'}}];
} else {
  return [];
}
```

### 返回格式检查清单

- [ ] 返回值是**数组** `[...]`（规范形式，首选）
- [ ] 数组每个元素都有 **`json` 属性**
- [ ] 结构为 `[{json: {...}}]` 或 `[{json: {...}}, {json: {...}}]`
- [ ] 不是原始值（string/number/boolean），也不是 `null`/`undefined`：真正会失败的就是这些形状

### 常见场景

```javascript
// Scenario 1: Single object from API
const response = $input.first().json;

// ✅ CANONICAL
return [{json: response}];

// ⚠️ Auto-wrapped to the same thing — runs, but prefer the array form
return {json: response};


// Scenario 2: Array of objects
const users = $input.all();

// ✅ CANONICAL
return users.map(user => ({json: user.json}));

// ✅ Also fine — a passthrough of items that already carry json
return users;


// Scenario 3: Computed result
const total = $input.all().reduce((sum, item) => sum + item.json.amount, 0);

// ✅ CANONICAL
return [{json: {total}}];

// ⚠️ Auto-wrapped → [{json: {total}}] in All Items mode — runs, but be explicit
return {total};


// Scenario 4: No results
// ✅ CORRECT
return [];

// ❌ FAILS — null has no items to pass on
return null;
```

---

## 错误 #4：字符串断裂与转义（JavaScript 语法错误）

**现象**：
- Code 节点在执行时抛出 JavaScript 语法错误："Unexpected token" 或 "Unexpected end of input"
- 原因是你自己的 JS：引号不配对，或普通引号字符串里有裸换行

这只是普通 JavaScript 层面的问题，**不是**校验器的检查项。校验器（n8n-mcp ≥ 2.63.0）不会标记配对的单引号、正则里的 `{ }`、或字符串字面量里的 `{{ }}`，这些都是合法 JavaScript。只有真正残缺的 JS 才会抛错，而且在运行时抛。

### 问题所在

发生条件：
1. 同种引号字符串内的引号没转义
2. 普通（非模板）字符串跨多行
3. 路径/正则里的反斜杠没转义

```javascript
// ✅ FINE: an apostrophe inside a double-quoted string is valid JavaScript
const message = "It's a nice day";

// ✅ FINE: braces in a regex literal are valid
const pattern = /\{(\w+)\}/;
```

```javascript
// ❌ SYNTAX ERROR: raw newline + unescaped inner double-quotes in a plain string
const html = "
  <div class="container">
    <p>Hello</p>
  </div>
";
```

### 解决方法

```javascript
// ✅ Mix quote styles or escape, whichever reads cleaner
const message = "It's a nice day";     // double quotes around an apostrophe — fine
const other   = 'She said "hello"';    // single quotes around double quotes — fine
```

```javascript
// ✅ Regex literals need no extra escaping of their own braces
const pattern = /\{(\w+)\}/;
```

```javascript
// ✅ CORRECT: Template literals for multi-line
const html = `
  <div class="container">
    <p>Hello</p>
  </div>
`;
// Backticks handle multi-line and quotes
```

```javascript
// ✅ CORRECT: Escape backslashes
const path = "C:\\\\Users\\\\Documents\\\\file.txt";
```

### 转义指南

| 字符 | 转义为 | 示例 |
|-----------|-----------|---------|
| 单引号字符串里的单引号 | `\\'` | `'It\\'s working'` |
| 双引号字符串里的双引号 | `\\"` | `"She said \\"hello\\""` |
| 反斜杠 | `\\\\` | `"C:\\\\path"` |
| 换行符 | `\\n` | `"Line 1\\nLine 2"` |
| 制表符 | `\\t` | `"Column1\\tColumn2"` |

### 最佳实践

```javascript
// ✅ BEST: Use template literals for complex strings
const message = `User ${name} said: "Hello!"`;

// ✅ BEST: Use template literals for HTML
const html = `
  <div class="${className}">
    <h1>${title}</h1>
    <p>${content}</p>
  </div>
`;

// ✅ BEST: Use template literals for JSON
const jsonString = `{
  "name": "${name}",
  "email": "${email}"
}`;
```

---

## 错误 #5：缺空值检查 / 访问 undefined

**频率**：非常常见的运行时错误

**现象**：
- 工作流执行停止
- 报错 "Cannot read property 'X' of undefined"
- 报错 "Cannot read property 'X' of null"
- 数据缺失时崩溃

### 问题所在

```javascript
// ❌ WRONG: No null check - crashes if user doesn't exist
const email = item.json.user.email;
```

```javascript
// ❌ WRONG: Assumes array has items
const firstItem = $input.all()[0].json;
```

```javascript
// ❌ WRONG: Assumes nested property exists
const city = $json.address.city;
```

```javascript
// ❌ WRONG: No validation before array operations
const names = $json.users.map(user => user.name);
```

### 解决方法

```javascript
// ✅ CORRECT: Optional chaining
const email = item.json?.user?.email || 'no-email@example.com';
```

```javascript
// ✅ CORRECT: Check array length
const items = $input.all();

if (items.length === 0) {
  return [];
}

const firstItem = items[0].json;
```

```javascript
// ✅ CORRECT: Guard clauses
const data = $input.first().json;

if (!data.address) {
  return [{json: {error: 'No address provided'}}];
}

const city = data.address.city;
```

```javascript
// ✅ CORRECT: Default values
const users = $json.users || [];
const names = users.map(user => user.name || 'Unknown');
```

```javascript
// ✅ CORRECT: Try-catch for risky operations
try {
  const email = item.json.user.email.toLowerCase();
  return [{json: {email}}];
} catch (error) {
  return [{
    json: {
      error: 'Invalid user data',
      details: error.message
    }
  }];
}
```

### 安全访问模式

```javascript
// Pattern 1: Optional chaining (modern, recommended)
const value = data?.nested?.property?.value;

// Pattern 2: Logical OR with default
const value = data.property || 'default';

// Pattern 3: Ternary check
const value = data.property ? data.property : 'default';

// Pattern 4: Guard clause
if (!data.property) {
  return [];
}
const value = data.property;

// Pattern 5: Try-catch
try {
  const value = data.nested.property.value;
} catch (error) {
  const value = 'default';
}
```

### Webhook 数据安全

```javascript
// Webhook data requires extra safety

// ❌ RISKY: Assumes all fields exist
const name = $json.body.user.name;
const email = $json.body.user.email;

// ✅ SAFE: Check each level
const body = $json.body || {};
const user = body.user || {};
const name = user.name || 'Unknown';
const email = user.email || 'no-email';

// ✅ BETTER: Optional chaining
const name = $json.body?.user?.name || 'Unknown';
const email = $json.body?.user?.email || 'no-email';
```

### 数组安全

```javascript
// ❌ RISKY: No length check
const items = $input.all();
const firstId = items[0].json.id;

// ✅ SAFE: Check length
const items = $input.all();

if (items.length > 0) {
  const firstId = items[0].json.id;
} else {
  // Handle empty case
  return [];
}

// ✅ BETTER: Use $input.first()
const firstItem = $input.first();
const firstId = firstItem.json.id;  // Built-in safety
```

### 对象属性安全

```javascript
// ❌ RISKY: Direct access
const config = $json.settings.advanced.timeout;

// ✅ SAFE: Step by step with defaults
const settings = $json.settings || {};
const advanced = settings.advanced || {};
const timeout = advanced.timeout || 30000;

// ✅ BETTER: Optional chaining
const timeout = $json.settings?.advanced?.timeout ?? 30000;
// Note: ?? (nullish coalescing) vs || (logical OR)
```

---

## 错误 #6：UnsupportedFunctionError（鉴权 helper 被禁）

**频率**：升级到 v2.0+ 之后，最常见的"昨天在旧版 n8n 还能跑"类错误

**现象**：
- 报错 `UnsupportedFunctionError: The function "helpers.httpRequestWithAuthentication" is not supported in the Code Node`
- `helpers.requestWithAuthenticationPaginated` 同样如此
- 执行时抛出，保存时不抛

### 问题所在

从 n8n v2.0 起，Code 节点在 **task runner 沙箱**中执行，沙箱有意禁用了鉴权 helper。旧的 vm2 沙箱曾经绑定这些 helper，所以老帖子和教程里它们看起来能用。n8n 源码注释解释了原因：Code 节点自己没有凭据，helper 无从鉴权；这个写法在语义上一直是坏的，只是一直没大声报出来。

```javascript
// ❌ BLOCKED in task runner sandbox (default since v2.0)
const data = await this.helpers.httpRequestWithAuthentication.call(
  this,
  'baseLinkerApi',
  { url: '...', method: 'POST' }
);
```

### 解决方法

runner 里**没有任何环境变量**能重新启用它们：deny-list 是编译进去的。从下面三选一：

**方案 A：把 Code 节点换成 HTTP Request 节点**（最佳）：

HTTP Request 节点原生支持挂凭据，URL/body/headers 都支持完整表达式。多数"Code 节点调 API"的写法，都是 HTTP Request 还没有分页和表达式支持时的遗留产物。

**方案 B：子工作流加 HTTP Request 节点**（前后需要代码级逻辑时）：

```javascript
// Parent Code node — prepare payloads, then delegate
return $input.all().map(i => ({ json: {
  url: 'https://api.example.com/things',
  method: 'POST',
  body: { sku: i.json.sku }
}}));
```

然后接到 **Execute Workflow** → 带 **Execute Workflow Trigger** 的子工作流 → **HTTP Request** 节点，使用 `={{ $json.url }}`、`={{ $json.body }}`，凭据原生挂载。

**方案 C：token 作为运行时数据**（仅当 token 确实随工作流数据流转时）：

```javascript
// ✅ Works — manual auth header, token came from upstream
const token = $('Get Token').first().json.access_token;

const data = await this.helpers.httpRequest({
  url: 'https://api.example.com/data',
  headers: { 'Authorization': `Bearer ${token}` }
});
```

### 决策指南

| 需求 | 做法 |
|------|-----|
| 单次鉴权 API 调用 | 直接用 HTTP Request 节点 |
| 多次 API 调用 + 前后处理 | 子工作流模式（方案 B） |
| token 已在数据流里 | 手动 `this.helpers.httpRequest()` 加 header |
| `httpRequestWithAuthentication` | **不可用：从上面 A、B、C 里选** |

---

## 错误 #7：$env is not defined / 无法访问 $env

**频率**：在加固过的生产实例中常见

**现象**：
- 报错 `$env is not defined` 或 `ReferenceError: $env is not defined`
- 代码看着没问题，开发实例上正常跑，生产上抛错

### 问题所在

`$env` 访问由 **`N8N_BLOCK_ENV_ACCESS_IN_NODE`** 环境变量把关。设为 `true`（常见的生产加固配置）时，`$env` 会从 Code 节点沙箱中彻底移除。注重安全的部署越来越多默认这么配。

```javascript
// ❌ Throws if N8N_BLOCK_ENV_ACCESS_IN_NODE=true
const apiKey = $env.API_KEY;
```

### 解决方法

把密钥当成**凭据问题**，而不是 Code 节点问题：

```javascript
// ✅ Token arrives as data from an upstream node that used a credential
const apiKey = $('Set Secret').first().json.apiKey;

// Or: secret was attached server-side by an HTTP Request node with the credential
// — your Code node never sees the raw secret, which is the whole point
```

确实需要从工作流外部注入的值（配置，而非密钥），用：
- 在工作流顶部放一个 **Set** 节点写死常量，或
- 用 HTTP Request 节点引用一个 **n8n 凭据**，或
- 你的版本支持的话，用 **External Secrets** 集成（`$secrets`）。

### 为什么这件事重要

2024 年之前写的 Skill 和教程常直接用 `$env.API_KEY`，因为那是最省事的路。现代 n8n 配置把它禁掉：允许 Code 节点读任意环境变量等于开了一个提权面，任何有工作流编辑权限的用户都能把 `DB_PASSWORD`、`N8N_ENCRYPTION_KEY` 等偷走。别跟限制较劲，让密钥走凭据。

---

## 错误预防清单

部署 Code 节点前，先过一遍这个清单：

### 代码结构
- [ ] 代码字段不为空
- [ ] 存在 return 语句
- [ ] 所有代码路径都返回数据

### 返回格式
- [ ] 返回条目，不是原始值/`null`
- [ ] 规范形状 `[{json: {...}}]`（裸对象会自动包装，但仍要写明确）

### 语法
- [ ] 没有 `{{ }}` 当代码写（它是给其他节点字段用的；放进字符串只是字面文本）
- [ ] 模板字面量用反引号：`` `${variable}` ``
- [ ] 引号与括号全部配对
- [ ] 字符串正确转义

### 数据安全
- [ ] 可选属性做空值检查
- [ ] 访问数组前检查长度
- [ ] Webhook 数据经 `.body` 访问
- [ ] 有风险的操作用 try-catch
- [ ] 缺失数据给默认值

### 测试
- [ ] 用空输入测试
- [ ] 用缺失字段测试
- [ ] 用意外数据类型测试
- [ ] 检查浏览器控制台报错

---

## 错误速查表

| 报错信息 | 可能原因 | 修复 |
|---------------|--------------|-----|
| "Code cannot be empty" | 代码字段为空 | 写入有意义的代码 |
| "Code must return data" | 缺 return 语句 | 加上 `return [...]` |
| "Code doesn't return items properly" | 返回了原始值（string/number）或 `null` | 返回 `[{json:{...}}]`（对象/数组会自动包装；原始值不会） |
| "Not all items have a json key" | 混合返回：有的条目带包装，有的裸 | 每个条目都包上 `{json: {...}}` |
| "Expression syntax {{...}} is not valid in Code nodes" / "Unexpected token" | `{{ }}` 当代码写（不在字符串里） | 用 JavaScript：`$json.x` 或 `` `${$json.x}` `` |
| "Cannot read property X of undefined" | 缺空值检查 | 用可选链 `?.` |
| "Cannot read property X of null" | 访问了 null 值 | 加卫语句或默认值 |
| "Unexpected end of input" | JS 里引号/括号不配对 | 转义字符串，或用反引号模板字面量 |
| "UnsupportedFunctionError ... httpRequestWithAuthentication" | task runner 里鉴权 helper 被禁 | 用 HTTP Request 节点 + 凭据，或子工作流模式（错误 #6） |
| "$env is not defined" | `N8N_BLOCK_ENV_ACCESS_IN_NODE=true` | 密钥走凭据，不走 `$env`（错误 #7） |
| "Cannot find module 'crypto'" | `require()` 白名单未设置 | 把逻辑移出 Code 节点，或设置 `N8N_RUNNERS_ALLOWED_BUILT_IN_MODULES` |

---

## 调试技巧

### 1. 用 console.log()

```javascript
const items = $input.all();
console.log('Items count:', items.length);
console.log('First item:', items[0]);

// Check browser console (F12) for output
```

### 2. 返回中间结果

```javascript
// Debug by returning current state
const items = $input.all();
const processed = items.map(item => ({json: item.json}));

// Return to see what you have
return processed;
```

### 3. 用 Try-Catch 排查问题

```javascript
try {
  // Your code here
  const result = riskyOperation();
  return [{json: {result}}];
} catch (error) {
  // See what failed
  return [{
    json: {
      error: error.message,
      stack: error.stack
    }
  }];
}
```

### 4. 校验输入结构

```javascript
const items = $input.all();

// Check what you received
console.log('Input structure:', JSON.stringify(items[0], null, 2));

// Then process
```

---

## 小结

**最需要避开的 7 个错误**：
1. **代码为空 / 缺 return**：始终返回数据
2. **表达式语法当代码**：用 JavaScript，别用 `{{ }}`（字符串里的 `{{ }}` 只是字面文本）
3. **返回结构**：优先 `[{json: {...}}]`；原始值/`null` 会失败（裸对象自动包装）
4. **字符串断裂**：引号/括号不配对会抛 JS 语法错误；转义或用模板字面量
5. **缺空值检查**：用可选链 `?.`
6. **`httpRequestWithAuthentication` 被禁**：用 HTTP Request 节点 + 凭据
7. **`$env` 被禁**：密钥走凭据，不走环境变量访问

**快速预防**：
- 优先用规范的 `[{json: {...}}]` 返回；绝不返回原始值或 `null`
- 写 JavaScript：别在该写代码的地方放 `{{ }}`
- 访问前检查 null/undefined
- 用空数据和非法数据测试
- 用浏览器控制台调试

**另见**：
- [SKILL.md](SKILL.md) - 概述与最佳实践
- [DATA_ACCESS.md](DATA_ACCESS.md) - 安全的数据访问模式
- [COMMON_PATTERNS.md](COMMON_PATTERNS.md) - 可用的完整示例
