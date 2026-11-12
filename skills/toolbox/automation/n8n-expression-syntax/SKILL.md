---
name: n8n-expression-syntax
description: 校验 n8n 表达式语法并修复常见错误。当编写 n8n 表达式、使用 {{}} 语法、访问 $json/$node 变量、排查表达式错误、在节点之间映射数据，或在工作流中引用 Webhook 数据时使用此 Skill。在配置引用前置节点数据的节点字段时应使用此 Skill：表达式是 n8n 在节点之间传递数据的方式，语法出错是工作流错误最常见的来源。当被问及复杂表达式是否影响性能时也使用此 Skill。
---

> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-expression-syntax/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# n8n 表达式语法

在工作流中编写正确 n8n 表达式的专家指南。

---

## 表达式格式

n8n 中所有动态内容都使用**双花括号**：


```
{{expression}}
```


**示例**：

```
✅ {{$json.email}}
✅ {{$json.body.name}}
✅ {{$node["HTTP Request"].json.data}}
❌ $json.email  (no braces - treated as literal text)
❌ {$json.email}  (single braces - invalid)
```


---

## 核心变量

### $json - 当前节点输出

访问当前节点的数据：


```javascript
{{$json.fieldName}}
{{$json['field with spaces']}}
{{$json.nested.property}}
{{$json.items[0].name}}
```


### $node - 引用其他节点

访问任意前置节点的数据：


```javascript
{{$node["Node Name"].json.fieldName}}
{{$node["HTTP Request"].json.data}}
{{$node["Webhook"].json.body.email}}
```


**重要**：
- 节点名称**必须**用引号括起
- 节点名称**区分大小写**
- 必须与工作流中的确切节点名称一致

### $now - 当前时间戳

访问当前日期/时间：


```javascript
{{$now}}
{{$now.toFormat('yyyy-MM-dd')}}
{{$now.toFormat('HH:mm:ss')}}
{{$now.plus({days: 7})}}
```


### $env - 环境变量

访问环境变量：


```javascript
{{$env.API_KEY}}
{{$env.DATABASE_URL}}
```


**警告**：某些 n8n 实例启用了 `N8N_BLOCK_ENV_ACCESS_IN_NODE`，会完全阻止 `$env` 访问。如果 `$env` 返回错误，请改用以下替代方案：
- 改为将值存入凭据
- 使用手动输入值的 Set 节点
- 通过 Webhook 查询参数传递值

---

## 🚨 关键：Webhook 数据结构

**最常见的错误**：Webhook 数据**不在**根节点！

### Webhook 节点输出结构


```javascript
{
  "headers": {...},
  "params": {...},
  "query": {...},
  "body": {           // ⚠️ USER DATA IS HERE!
    "name": "John",
    "email": "john@example.com",
    "message": "Hello"
  }
}
```


### 正确的 Webhook 数据访问


```javascript
❌ WRONG: {{$json.name}}
❌ WRONG: {{$json.email}}

✅ CORRECT: {{$json.body.name}}
✅ CORRECT: {{$json.body.email}}
✅ CORRECT: {{$json.body.message}}
```


**原因**：Webhook 节点把传入数据包装在 `.body` 属性下，以保留 headers、params 和查询参数。

---

## 常见模式

### 访问嵌套字段


```javascript
// Simple nesting
{{$json.user.email}}

// Array access
{{$json.data[0].name}}
{{$json.items[0].id}}

// Bracket notation for spaces
{{$json['field name']}}
{{$json['user data']['first name']}}
```


### 引用其他节点


```javascript
// Node without spaces
{{$node["Set"].json.value}}

// Node with spaces (common!)
{{$node["HTTP Request"].json.data}}
{{$node["Respond to Webhook"].json.message}}

// Webhook node
{{$node["Webhook"].json.body.email}}
```


### 组合变量


```javascript
// Concatenation (automatic)
Hello {{$json.body.name}}!

// In URLs
https://api.example.com/users/{{$json.body.user_id}}

// In object properties
{
  "name": "={{$json.body.name}}",
  "email": "={{$json.body.email}}"
}
```


---

## 何时不应使用表达式

### ❌ Code 节点

Code 节点使用**直接 JavaScript 访问**，而不是表达式！


```javascript
// ❌ WRONG in Code node
const email = '={{$json.email}}';
const name = '{{$json.body.name}}';

// ✅ CORRECT in Code node
const email = $json.email;
const name = $json.body.name;

// Or using Code node API
const email = $input.item.json.email;
const allItems = $input.all();
```


### ❌ Webhook 路径


```javascript
// ❌ WRONG
path: "{{$json.user_id}}/webhook"

// ✅ CORRECT
path: "user-webhook"  // Static paths only
```


### ❌ 凭据字段


```javascript
// ❌ WRONG
apiKey: "={{$env.API_KEY}}"

// ✅ CORRECT
Use n8n credential system, not expressions
```


---

## 转换把关准则

在添加节点（或编写任何代码）来转换数据之前，按以下顺序逐项判断，在第一个适用的方案处停下：

1. **服务自带的节点**在自己的字段里完成：CRM 节点的字段槽位、Slack 节点的 Blocks 字段、Data Table insert 的逐列槽位。仅当没有节点覆盖该操作时才用 HTTP Request。
2. **完成该任务的原生节点。** Filter、IF / Switch、Summarize、Aggregate、Split Out、Merge、Compare Datasets、Remove Duplicates、Sort + Limit、Date & Time、XML / HTML / Extract From File、HTTP Request 分页、Crypto。`using-n8n-mcp-skills` 中的任务到节点对照表把任务映射到节点；它们的配置在 `n8n-node-configuration` → NATIVE_NODES.md。
3. **简短表达式**（`{{ ... }}`），写在那个节点的字段里。属性访问、方法链（`.map().filter().join()`）、三元运算、字符串拼接、Luxon 日期运算、下面的辅助函数：在一个表达式里"取 A、产出 B"，不引入中间变量。
   - **查询嵌套 JSON 中的某个字段**（在数组内挑选、过滤、求和）→ 在同一个表达式里用 `$jmespath()`（规则见下）。若下游需要每个元素对应一个 item，改用 Split Out / Filter / Aggregate。
4. **Code 节点**，仅限以下封闭清单：没有节点能表达的循环或递归、跨运行的状态、没有节点能处理的解析、白名单内的库、繁重的全量 item 处理（数千个 item，已声明或已实测），或用一个简短 Code 节点（约 15 行）替换 4 个以上粘合节点。给它加一条 `Why Code:` 备注。见 `n8n-code-javascript`。

**函数体就是代码。** 当逻辑需要 `const`、`if`、`return` 或多条语句（即包在 `{{ }}` 里的 `(() => { ... })()`）时，它已经超出表达式的范畴。把它拆成一个原生节点加若干简短表达式，或移入带 `Why Code:` 备注的 Code 节点。冗长的表达式比两者都更难读，而且其中的运行时错误会静默解析为 `null`（见调试）。create/update Hook 会标记非 Code 节点里的函数体。

**为何顺序重要。** 可读性：原生节点在画布上直接说明它做什么，简短表达式留在用它的字段里可见，而不必藏在上游节点中让人点开查看。性能很少成为决定因素，在几百个 item 以下这些开销都无关紧要，实测模型见 `n8n-code-javascript`。

## `$jmespath()` - 用一个表达式查询嵌套 JSON


```
{{ $jmespath($json, "customers[?country=='PL' && revenue > `100000`].name") }}    →  ["Acme"]
```


已在 n8n 2.38 验证：这一个表达式返回的结果与 Split Out → Filter → Aggregate 完全相同，且无需额外节点。语法要求严格，**多数错误会静默失败**：

| 正确写法 | 不要这样写 | 错误形式的后果 |
|---|---|---|
| `$jmespath(object, "query")`，object 在前 | `$jmespath("query", object)` | 抛出 `expected two arguments (Object, string) for this function`（JMESPath 自己的文档写的是 `search(query, data)`） |
| 字符串用单引号：`country=='PL'` | `country=="PL"` | 双引号表示**字段名** → 返回 `[]`，不报错 |
| 数字/布尔值用反引号：`` revenue > `100000` `` | `revenue > 100000` | 解析错误 → 整个表达式变成 `null`（见调试） |
| `&&` `\|\|` `!` `==` | `and` `or` `=` | 解析错误 → `null` |
| 带连字符的键要加引号：`'customers[*].contact."first-name"'`（JS 字符串用单引号） | `contact.first-name` | 解析错误 → `null` |
| 跨 item 时保留包装：`$jmespath($('Node').all(), "[?json.country=='PL'].json.name")` 或 `$jmespath($input.all().map(i => i.json), "[?country=='PL'].name")` | 在 `.all()` 上用 `"[?country=='PL'].name"` | item 是 `{json: …}` 包装 → `[]` |

- **返回结果：** 路径或索引缺失 → `null`；过滤无匹配 → `[]`；对空投影执行 `sum()` → `0`。
- **第一个参数必须是对象或数组。** 字符串（例如返回文本响应的 HTTP Request）或 `undefined`（`$json.missingField`）会抛出同样的 `expected two arguments` 错误，而这一种确实会让节点失败。
- **常用片段：** `length()`、`sum()`、`max_by(arr, &field)`、`sort_by(arr, &field)`、`reverse()`、`contains()`、`starts_with()`、`keys()`、`to_number()`；投影 `[*]`、展平 `[]`、管道 `| [0]`、重塑 `{name: name, email: contact.email}`。
- **它返回的是值，不是 item。** 用在结果供单个字段消费的场景（消息文本、HTTP body、IF/Filter 条件）。当下游需要每个匹配对应一个 item 时，在 Edit Fields 里用 `$jmespath` 收窄，再对该字段接一个 Split Out。
- **适用范围：** 表达式和 JavaScript Code 节点（参数顺序相同）。原生 Python Code 节点里没有。

## 内置辅助函数

n8n 为 `{{ }}` 中的值附加了方法。与原生节点配合，它们可以替代大多数单行 Code 节点。**它们只存在于表达式中，不存在于 Code 节点里**：在 Code 里使用纯 JavaScript（并用 `toFormat()` 代替 `format()`）。它们只能看到当前 item 的值：跨 item 的任务（item 去重、分组求和、连接两个列表）应放在节点里。在 n8n-mcp 2.97.0+ 上，`tools_documentation({topic: "expression_helpers", depth: "full"})` 会列出每个辅助函数并附上经过测试的示例。

| 需求 | 表达式 | 说明 |
|---|---|---|
| 从每个对象取一个字段 | `{{ $json.items.pluck('name') }}` | 多个名称 → 每个对象一个数组 |
| 求和 / 平均 / 最小 / 最大 | `{{ $json.prices.sum() }}` | 遇到非数字会抛错，数字字符串也算在内 |
| 数组去重 | `{{ $json.rows.unique('email') }}` | 每个参数是一个字段名；不传参数 → 比较整个值（`removeDuplicates` 是别名） |
| 空值的默认值 | `{{ $ifEmpty($json.name, 'there') }}` | 空 = undefined、null、`''`、`[]`、`{}`；必须恰好两个参数 |
| 提取文本中的邮箱或域名 | `{{ $json.text.extractEmail() }}`, `.extractDomain()` | 无匹配时返回 `undefined` |
| 字符串哈希 | `{{ $json.email.hash('sha256') }}` | 默认 md5；HMAC 需要 Crypto 节点 |
| 两个日期之间的天数 | `{{ $now.diffTo($json.created_at, 'days') }}` | 接收者减去参数：参数更早时为正 |
| 字符串转日期 | `{{ $json.created_at.toDateTime().format('yyyy-MM-dd') }}` | 之后可接 `.diffTo()`、`.plus(7, 'days')`、`.extract('month')` |
| 把数组分批 | `{{ $json.ids.chunk(100) }}` | 用于批量 API body |
| 丢弃空值 | `{{ $json.tags.compact() }}`, `{{ $json.compact() }}` | 数组和对象 |

- `diffTo` 接受 DateTime、JS Date 或 ISO 字符串，以及可选单位（默认 `days`）或单位列表（此时返回对象）。`$json.created_at.toDateTime().diffToNow('days')` 对过去的日期是**负值**。
- 对字符串执行 `.sum()` 会抛错：`{{ $json.items.pluck('price').map(Number).sum() }}`。
- 在 `null` 或 `undefined` 上调用辅助函数会抛错：用 `?.`（`{{ $json.email?.extractDomain() }}`）或 `$ifEmpty()` 加以保护。
- 抛出异常的辅助函数（单位无效、参数个数不对、值缺失）会让节点失败；`{{ }}` 里的普通 JavaScript 错误会静默返回 `null`。两种情况都要用真实 item 测试。

## Set 节点反模式与分支汇合

### 删除只为下一个节点重映射字段的 Set 节点

如果一个 Set / Edit Fields 节点的唯一工作就是复制或重命名字段，好让**下一个**节点能读取，它就是多余负担。改为把它的表达式内联到消费方。


```
❌  Webhook → Set { customer_id: {{ $json.body.customer_id }} } → Postgres: WHERE id = {{ $json.customer_id }}

✅  Webhook → Postgres: WHERE id = {{ $('Webhook').item.json.body.customer_id }}
```


Set 节点多了一跳、让画布更杂乱、带来重构隐患，而消费方自己完全做得到同样的事。要用 `n8n_update_partial_workflow` 干净地移除它：重新接线（从 Set 的源端与目标端 `removeConnection`，从源直接到消费方 `addConnection`），用 `patchNodeField` 把消费方的表达式改为按节点名引用原始来源，再 `removeNode` 删掉 Set。

**快速判断：** 这个 Set 是否只是重映射下一个节点本可直接读取的字段（`$('Source').item.json.x`）？
- **是** → 删掉它，把表达式内联到消费方。
- **否，它创造了新内容** → 保留为具名步骤（按它产出的内容命名）。

以下情况 **Edit Fields 有其价值**：
- **它创建常量 item**：固定配置、默认 payload、测试 fixture。
- **它构建错误或返回 item**：Respond 之前的 `{ error: 'validation_error', message: … }`，或子工作流的输出。
- **它构建 payload 对象**，供多个节点或整个请求 body 取用。
- **2 个以上消费方**读取同一派生值，且派生逻辑并不简单（命名有助于可读性，且只计算一次）。
- **它是子工作流最后的 Return 节点**，用于塑造输出契约。这里的"单一消费方"是所有调用方，因此 Set *就是* API 边界；配合 `Include Other Fields: false`，它会把输出形状列入白名单，避免内部临时字段外泄。
- **你要重命名或白名单化字段**，并希望这一点集中可见，而不是散落在各消费方表达式里。

### 分支汇合：用 NoOp 锚定

当分支汇合时（在 IF/Switch/Merge 之后），`$json` 会变成"最后触发的那条分支"的结果，这是不确定的，也是错误数据的隐形来源。在汇合处插入一个 **NoOp** 节点，用描述性名称命名（`Combine Inputs`），并让下游节点按名称引用它：


```
Branch A ──┐
           ├─→ [NoOp: Combine Inputs] ──→ downstream uses $('Combine Inputs').item.json.x
Branch B ──┘
```


NoOp 能扛住重构：日后在它与消费方之间插入转换节点，不会破坏 `$('Combine Inputs')` 引用。（如果各分支产出*不同*的形状，改用 Set 节点而不是 NoOp，把两者归一成同一种形状，见上面的例外情况。）

更广泛地说，在多分支的流程中，**优先用 `$('Node').item.json.x`，而不是深层 `$json.x`。** 一旦插入中间节点，或某个节点清空了 item 上下文（Aggregate、以 Run for All 运行的 Code、分支 Merge），`$json` 就会失效；这种失败是静默的，下游拿到错误数据却不报任何错误。按节点名引用始终明确，无论来源与消费方之间夹了什么。

---

## 校验规则

### 1. 始终使用 {{}}

表达式**必须**包在双花括号里。


```javascript
❌ $json.field
✅ {{$json.field}}
```


### 2. 空格与特殊字符要加引号

含空格、变音符号或特殊字符的字段名或节点名需要**方括号表示法**：


```javascript
❌ {{$json.field name}}
✅ {{$json['field name']}}

❌ {{$node.HTTP Request.json}}
✅ {{$node["HTTP Request"].json}}

// Bracket notation is mandatory for keys with special characters
✅ {{$json['Gross Price w/o shipment']}}
✅ {{$json['Cena brutto zł']}}
```


### 3. 匹配确切的节点名称

节点引用**区分大小写**：


```javascript
❌ {{$node["http request"].json}}  // lowercase
❌ {{$node["Http Request"].json}}  // wrong case
✅ {{$node["HTTP Request"].json}}  // exact match
```


### 4. 不要嵌套 {{}}

不要对表达式重复包裹：


```javascript
❌ {{{$json.field}}}
✅ {{$json.field}}
```


---

## 常见错误

完整的错误清单及修复方法，见 [COMMON_MISTAKES.md](COMMON_MISTAKES.md)

### 快速修复

| 错误 | 修复 |
|---------|-----|
| `$json.field` | `{{$json.field}}` |
| `{{$json.field name}}` | `{{$json['field name']}}` |
| `{{$node.HTTP Request}}` | `{{$node["HTTP Request"]}}` |
| `{{{$json.field}}}` | `{{$json.field}}` |
| `{{$json.name}}` （Webhook） | `{{$json.body.name}}` |
| `'={{$json.email}}'` （Code 节点） | `$json.email` |

---

## 实操示例

真实工作流示例见 [EXAMPLES.md](EXAMPLES.md)

### 示例 1：Webhook 到 Slack

**Webhook 收到**：

```json
{
  "body": {
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello!"
  }
}
```


**在 Slack 节点的文本字段中**：

```
New form submission!

Name: {{$json.body.name}}
Email: {{$json.body.email}}
Message: {{$json.body.message}}
```


### 示例 2：HTTP Request 到 Email

**HTTP Request 返回**：

```json
{
  "data": {
    "items": [
      {"name": "Product 1", "price": 29.99}
    ]
  }
}
```


**在 Email 节点中**（引用 HTTP Request）：

```
Product: {{$node["HTTP Request"].json.data.items[0].name}}
Price: ${{$node["HTTP Request"].json.data.items[0].price}}
```


### 示例 3：格式化时间戳


```javascript
// Current date
{{$now.toFormat('yyyy-MM-dd')}}
// Result: 2025-10-20

// Time
{{$now.toFormat('HH:mm:ss')}}
// Result: 14:30:45

// Full datetime
{{$now.toFormat('yyyy-MM-dd HH:mm')}}
// Result: 2025-10-20 14:30
```


---

## 数据类型处理

### 数组


```javascript
// First item
{{$json.users[0].email}}

// Array length
{{$json.users.length}}

// Last item
{{$json.users[$json.users.length - 1].name}}
```


### 对象


```javascript
// Dot notation (no spaces)
{{$json.user.email}}

// Bracket notation (with spaces or dynamic)
{{$json['user data'].email}}
```


### 字符串


```javascript
// Concatenation (automatic)
Hello {{$json.name}}!

// String methods
{{$json.email.toLowerCase()}}
{{$json.name.toUpperCase()}}
```


### 数字


```javascript
// Direct use
{{$json.price}}

// Math operations
{{$json.price * 1.1}}  // Add 10%
{{$json.quantity + 5}}
```


---

## 进阶模式

### 条件内容


```javascript
// Ternary operator
{{$json.status === 'active' ? 'Active User' : 'Inactive User'}}

// Default values
{{$json.email || 'no-email@example.com'}}
```


### 日期处理


```javascript
// Add days
{{$now.plus({days: 7}).toFormat('yyyy-MM-dd')}}

// Subtract hours
{{$now.minus({hours: 24}).toISO()}}

// Set specific date
{{DateTime.fromISO('2025-12-25').toFormat('MMMM dd, yyyy')}}
```


### 字符串处理


```javascript
// Substring
{{$json.email.substring(0, 5)}}

// Replace
{{$json.message.replace('old', 'new')}}

// Split and join
{{$json.tags.split(',').join(', ')}}
```


---

## 性能：表达式复杂度（几乎）不花成本

常见的顾虑是复杂的 `{{ }}` 会很慢。并非如此，真正的开销在于 n8n *求值表达式的次数*，而不是每个表达式有多复杂。在 n8n 2.x 上实测，一个繁复的表达式（`sqrt`、`split`、`reduce`）每个 item 的成本与 `{{ $json.x > 50 }}` 大致相同：大部分成本来自 n8n 构建每个 item 的求值上下文。

实践中的含义：

- **不要为了速度把一个能用的简短表达式拆成额外节点**，也不要为了速度把它扩成函数体。按可读性来选：原生节点，然后简短表达式，然后 Code（见上面的把关准则）。
- 每个 item 的成本只有在数千个 item 时才显现，主要来自逐 item 边界的数量（以 "Each Item" 模式运行的 Code 是最坏情况）。**n8n Code JavaScript** Skill 里有实测的逐 item 模型。

---

## 调试表达式

### 运行时错误不会让节点失败，而是变成 `null`

已在 n8n 2.38 的默认表达式运行时验证：执行期间，每个 `{{ }}` 外围的处理器只重新抛出 n8n 自身的 `ExpressionError`，并吞掉其他 JavaScript 错误，于是该字段解析为空/`null`，节点仍报告**成功**。`$json.missing.field`（TypeError）、`JSON.parse('{bad')`、`throw new Error(...)` 以及 JMESPath 语法错误都产出 `null`。在 Filter 或 IF 条件里，每个 item 随后都会静默地不通过检查。在其他版本或表达式引擎上，同样的错误可能反而让节点失败。无论如何，切勿只凭一次绿色运行就放心。

这不是避开表达式的理由（Code 节点自己也有静默陷阱），而是**用真实 item 测试**的理由：

- 用真实数据核对表达式编辑器的预览。预览*确实*会显示错误。
- 测试运行后查看输出值。本该有数据的地方出现 `null` 就是症状。`validate_workflow` 和绿色执行不会告诉你。
- 要暴露真实信息，临时把表达式包起来：
  `{{ (() => { try { return JSON.stringify(<expr>) } catch (e) { return 'ERROR: ' + e.message } })() }}`
- n8n 自身的错误仍会让节点失败（例如给 `$jmespath` 传入非对象参数）。

### 在表达式编辑器中测试

1. 点击带表达式的字段
2. 打开表达式编辑器（点击 "fx" 图标）
3. 查看结果的实时预览
4. 检查以红色高亮的错误

### 常见错误信息

这些会出现在编辑器预览里；运行时它们大多反而解析为 `null`（见上文）。

**"Cannot read property 'X' of undefined"**
→ 父对象不存在
→ 检查数据路径

**"X is not a function"**
→ 试图在非函数上调用方法
→ 检查变量类型

**表达式显示为字面文本**
→ 缺少 {{ }}
→ 补上花括号

---

## 表达式辅助方法

### 可用方法

**字符串**：
- `.toLowerCase()`, `.toUpperCase()`
- `.trim()`, `.replace()`, `.substring()`
- `.split()`, `.includes()`

**数组**：
- `.length`, `.map()`, `.filter()`
- `.find()`, `.join()`, `.slice()`

**DateTime** (Luxon)：
- `.toFormat()`, `.toISO()`, `.toLocal()`
- `.plus()`, `.minus()`, `.set()`

**数字**：
- `.toFixed()`, `.toString()`
- 数学运算：`+`, `-`, `*`, `/`, `%`

**JSON 查询**：
- `$jmespath(object, "query")`: 过滤/挑选/聚合嵌套 JSON（引号规则见 `$jmespath()` 一节）

---

## 最佳实践

### ✅ 要做的

- 动态内容始终使用 {{ }}
- 含空格的字段名使用方括号表示法
- 从 `.body` 引用 Webhook 数据
- 用 $node 引用其他节点的数据
- 在表达式编辑器中测试表达式

### ❌ 不要做的

- 不要在 Code 节点里使用表达式
- 含空格的节点名别忘了加引号
- 不要用多余的 {{ }} 重复包裹
- 不要以为 Webhook 数据在根节点（它在 .body 下！）
- 不要在 Webhook 路径或凭据中使用表达式

---

## 相关 Skill

- **n8n MCP Tools Expert**：学习如何用 MCP 工具校验表达式
- **n8n Workflow Patterns**：在真实工作流示例中查看表达式
- **n8n Node Configuration**：理解何时需要表达式

---

## 小结

**核心规则**：
1. 表达式包在 {{ }} 里
2. Webhook 数据在 `.body` 下
3. Code 节点里不要用 {{ }}
4. 含空格的节点名加引号
5. 节点名区分大小写
6. `{{ }}` 里的运行时错误会静默变成 `null`。测试运行后检查输出值
7. `$jmespath(object, "query")`：`'string'`、`` `number` ``、`"field"`；在 `.all()` 上要加 `json.` 前缀

**最常见的错误**：
- 缺少 {{ }} → 补上花括号
- Webhook 里的 `{{$json.name}}` → 改用 `{{$json.body.name}}`
- Code 里的 `{{$json.email}}` → 改用 `$json.email`
- `{{$node.HTTP Request}}` → 改用 `{{$node["HTTP Request"]}}`

更多细节见：
- [COMMON_MISTAKES.md](COMMON_MISTAKES.md) - 完整错误清单
- [EXAMPLES.md](EXAMPLES.md) - 真实工作流示例

---

**需要帮助？** 查阅 n8n 表达式文档，或使用 n8n-mcp 校验工具检查表达式。
