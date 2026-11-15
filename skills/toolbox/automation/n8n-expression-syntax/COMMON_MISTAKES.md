> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-expression-syntax/COMMON_MISTAKES.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# n8n 表达式常见错误

表达式错误的完整清单，附解释与修复方法。

---

## 1. 缺少花括号

**问题**：表达式未被识别，显示为字面文本

❌ **错误**：
```
$json.email
```

✅ **正确**：
```
{{$json.email}}
```

**为什么会出错**：n8n 把不含 {{ }} 的文本当作字面字符串。表达式必须包起来才会被求值。

**如何识别**：字段显示 "$json.email" 这样的原文，而不是实际值。

---

## 2. Webhook Body 访问

**问题**：访问 webhook 数据时得到 undefined

❌ **错误**：
```
{{$json.name}}
{{$json.email}}
{{$json.message}}
```

✅ **正确**：
```
{{$json.body.name}}
{{$json.body.email}}
{{$json.body.message}}
```

**为什么会出错**：Webhook 节点把传入数据包在 `.body` 属性下。根级 `$json` 包含 headers、params、query 和 body。

**Webhook 结构**：
```javascript
{
  "headers": {...},
  "params": {...},
  "query": {...},
  "body": {         // User data is HERE!
    "name": "John",
    "email": "john@example.com"
  }
}
```

**如何识别**：Webhook 工作流对明确已发送的字段显示 "undefined"。

---

## 3. 字段名带空格

**问题**：语法错误或 undefined 值

❌ **错误**：
```
{{$json.first name}}
{{$json.user data.email}}
```

✅ **正确**：
```
{{$json['first name']}}
{{$json['user data'].email}}
```

**为什么会出错**：空格会打断点号写法。JavaScript 把空格解释为属性名的结束。

**如何识别**：报"意外 token"类错误，或字段明明存在却得到 undefined。

---

## 4. 节点名带空格

**问题**：无法访问其他节点的数据

❌ **错误**：
```
{{$node.HTTP Request.json.data}}
{{$node.Respond to Webhook.json}}
```

✅ **正确**：
```
{{$node["HTTP Request"].json.data}}
{{$node["Respond to Webhook"].json}}
```

**为什么会出错**：节点名被当作对象属性名处理，含空格时必须加引号。

**如何识别**：报 "Cannot read property 'Request' of undefined" 之类的错误

---

## 5. 节点引用大小写错误

**问题**：返回 undefined 或错误数据

❌ **错误**：
```
{{$node["http request"].json.data}}  // lowercase
{{$node["Http Request"].json.data}}  // wrong capitalization
```

✅ **正确**：
```
{{$node["HTTP Request"].json.data}}  // exact match
```

**为什么会出错**：节点名**区分大小写**。必须与工作流中显示的完全一致。

**如何识别**：节点存在且有数据，值却是 undefined。

---

## 6. 双重包裹

**问题**：输出里出现字面 {{ }}

❌ **错误**：
```
{{{$json.field}}}
```

✅ **正确**：
```
{{$json.field}}
```

**为什么会出错**：只需要一组 {{ }}。多余的括号会被当作字面字符。

**如何识别**：输出显示 "{{value}}" 而不是 "value"。

---

## 7. 用点号访问数组

**问题**：语法错误或 undefined

❌ **错误**：
```
{{$json.items.0.name}}
{{$json.users.1.email}}
```

✅ **正确**：
```
{{$json.items[0].name}}
{{$json.users[1].email}}
```

**为什么会出错**：数组下标要用方括号，不能用点号。点号后跟数字不是合法的 JavaScript。

**如何识别**：语法错误，或 "Cannot read property '0' of undefined"

---

## 8. 在 Code 节点里用表达式

**问题**：得到字面字符串而非值，或报错

❌ **错误**（Code 节点内）：
```javascript
const email = '{{$json.email}}';
const name = '={{$json.body.name}}';
```

✅ **正确**（Code 节点内）：
```javascript
const email = $json.email;
const name = $json.body.name;

// Or using Code node API
const email = $input.item.json.email;
const allItems = $input.all();
```

**为什么会出错**：Code 节点对数据是**直接访问**的。{{ }} 语法是给其他节点的表达式字段用的，不是给 JavaScript 代码用的。

**如何识别**：Code 节点输出里出现字面字符串 "{{$json.email}}" 而不是实际值。

---

## 9. $node 引用缺引号

**问题**：语法错误

❌ **错误**：
```
{{$node[HTTP Request].json.data}}
```

✅ **正确**：
```
{{$node["HTTP Request"].json.data}}
```

**为什么会出错**：方括号里的节点名必须是带引号的字符串。

**如何识别**：语法错误 "Unexpected identifier"

---

## 10. 属性路径错误

**问题**：undefined 值

❌ **错误**：
```
{{$json.data.items.name}}       // items is an array
{{$json.user.email}}            // user doesn't exist, it's userData
```

✅ **正确**：
```
{{$json.data.items[0].name}}    // access array element
{{$json.userData.email}}        // correct property name
```

**为什么会出错**：数据路径错了。数组要用下标，属性名必须完全一致。

**如何识别**：用表达式编辑器预览检查真实数据结构。

---

## 11. 在 JSON 之外使用 = 前缀

**问题**：输出里出现字面 "="

❌ **错误**（文本字段中）：
```
Email: ={{$json.email}}
```

✅ **正确**（文本字段中）：
```
Email: {{$json.email}}
```

**注意**：`=` 前缀**只**在 JSON 模式下、或想把整个字段值设为表达式结果时才需要：

```javascript
// JSON mode (set property to expression)
{
  "email": "={{$json.body.email}}"
}

// Text mode (no = needed)
Hello {{$json.body.name}}!
```

**为什么会出错**：在非 JSON 上下文里 `=` 被解析为字面文本。

**如何识别**：输出显示 "=john@example.com" 而不是 "john@example.com"

---

## 12. Webhook 路径里用表达式

**问题**：路径不更新，校验报错

❌ **错误**：
```
path: "{{$json.user_id}}/webhook"
path: "users/={{$env.TENANT_ID}}"
```

✅ **正确**：
```
path: "my-webhook"              // Static paths only
path: "user-webhook/:userId"    // Use dynamic URL parameters instead
```

**为什么会出错**：Webhook 路径必须是静态的。改用动态 URL 参数（`:paramName`），不要用表达式。

**如何识别**：Webhook 路径不变，或校验提示路径非法。

---

## 13. $node 引用漏掉 .json

**问题**：undefined 或错误数据

❌ **错误**：
```
{{$node["HTTP Request"].data}}          // Missing .json
{{$node["Webhook"].body.email}}         // Missing .json
```

✅ **正确**：
```
{{$node["HTTP Request"].json.data}}
{{$node["Webhook"].json.body.email}}
```

**为什么会出错**：节点数据总是在 `.json` 属性下（二进制数据在 `.binary`）。

**如何识别**：明知节点有数据，值却是 undefined。

---

## 14. `{{ }}` 之外的模板字符串与拼接

**问题**：反引号模板字符串或 `+` 拼接被显示为字面文本

❌ **错误**（写成整个字段值，没有 `{{ }}`）：
```
`Hello ${$json.name}!`          // bare backticks — printed verbatim
"Hello " + $json.name + "!"     // bare concatenation — printed verbatim
```

✅ **正确**（以下任一）：
```
Hello {{$json.name}}!                   // adjacent text + {{ }} auto-concatenate
{{ `Hello ${$json.name}!` }}            // a template literal INSIDE {{ }}
{{ "Hello " + $json.name + "!" }}       // + concatenation INSIDE {{ }}
```

**为什么会出错**：n8n 只对 `{{ }}` 里面的内容求值，其余都是字面文本。反引号和 `+` 不是问题所在，问题在于**缺了 `{{ }}`**。在表达式**内部**，带 `${...}` 插值的反引号模板字符串是完全支持的现代 JavaScript，所以下面这样是合法且会求值的：

```
={{ $json.items.map(i => `${i.name} — ${i.qty}`).join(', ') }}
```

可选链（`{{ $json.user?.email }}`）和字符串键的方括号访问（`{{ $json['some-prop'] }}`）同理，二者都是合法的 n8n 表达式。从 n8n-mcp ≥ 2.63.0 起，校验器不再对表达式内的模板字符串、可选链或方括号访问报错（更早的版本会对它们误报）。

**如何识别**：输出里出现字面反引号或 `+` 符号 → 代码没包在 `{{ }}` 里。

---

## 15. 空表达式括号

**问题**：输出里出现字面 {{}}

❌ **错误**：
```
{{}}
{{ }}
```

✅ **正确**：
```
{{$json.field}}                 // Include expression content
```

**为什么会出错**：空表达式括号里没有可求值的内容。

**如何识别**：输出里出现字面 "{{ }}" 文本。

---

## 16. JMESPath 字符串用了双引号

**问题**：`$jmespath` 过滤器返回 `[]`，明明存在匹配数据，却不报错

❌ **错误**：
```
{{ $jmespath($json, 'customers[?country=="PL"].name') }}      // → []
```

✅ **正确**：
```
{{ $jmespath($json, "customers[?country=='PL'].name") }}      // → ["Acme", "Bar"]
{{ $jmespath($json, "customers[?revenue > `100000`].name") }} // numbers in backticks
```

**为什么会出错**：在 JMESPath 里，`"PL"` 是带引号的**字段名**，不是字符串。过滤器拿 `country` 和名为 `PL` 的字段比较，而该字段不存在，所以什么也匹配不上。字符串字面量用单引号，数字和布尔值用反引号。裸数字（`revenue > 100000`）、或用 `and`/`=` 代替 `&&`/`==`，都是解析错误，整个表达式会变成 `null`（见 #17）。

**对条目列表同样的坑**：`$jmespath($('Node').all(), "[?country=='PL']")` 也返回 `[]`。条目是 `{json: …}` 包装，所以要写成 `[?json.country=='PL'].json.name`，或先 map：`$input.all().map(i => i.json)`。

**如何识别**：输入面板里明明能看到数据，查询却返回 `[]` 或 `null`。

---

## 17. 运行时错误被隐藏成 `null`

**问题**：某个字段输出 `null`/为空（或 Filter 把所有条目都滤掉了），而节点和执行却显示成功

❌ **错误假设**："运行是绿的，说明表达式没问题。"

**原因**：在 n8n 2.38 默认表达式运行时上验证过：运行时 n8n 会吞掉 `{{ }}` 内除自带 `ExpressionError` 之外的 JavaScript 错误。`$json.missing.field`、对坏输入执行 `JSON.parse`、抛出的 `Error`、JMESPath 语法错误，全都解析为 `null` 而不是让节点失败。编辑器预览会显示错误，执行不会。其他版本或引擎可能改为让节点失败。无论哪种情况，都不要只凭一次绿色运行就放心。

✅ **修复/检查**：
```
{{ (() => { try { return JSON.stringify($json.payload.items.map(i => i.id)) } catch (e) { return 'ERROR: ' + e.message } })() }}
```
临时套上它看报错信息，修好路径后再去掉包装。测试运行后务必检查输出值，可选路径用 `?.` / `??` 防护。

**如何识别**：输出里出现意料之外的 `null`；Filter/IF 把所有条目都送到了 false 一侧。

---

## 快速参考表

| 错误 | 症状 | 修复 |
|-------|---------|-----|
| 没有 {{ }} | 字面文本 | 加上 {{ }} |
| Webhook 数据 | undefined | 加上 `.body` |
| 字段名带空格 | 语法错误 | 用 `['field name']` |
| 节点名带空格 | undefined | 用 `["Node Name"]` |
| 大小写错误 | undefined | 严格匹配大小写 |
| 双重 {{ }} | 字面括号 | 去掉多余的 {{ }} |
| .0 数组 | 语法错误 | 用 [0] |
| Code 里用 {{ }} | 字面字符串 | 去掉 {{ }} |
| $node 缺引号 | 语法错误 | 加引号 |
| 路径错误 | undefined | 检查数据结构 |
| 文本中的 = | 字面 = | 去掉 = 前缀 |
| 动态路径 | 不生效 | 用静态路径 |
| 漏掉 .json | undefined | 加上 .json |
| {{ }} 外的模板字符串 / `+` | 字面文本 | 包进 {{ }}（两者在内部都可用） |
| 空 {{ }} | 字面括号 | 填入表达式 |
| 过滤器里 JMESPath 写 `"PL"` | `[]`，不报错 | 字符串用 `'PL'`，数字用 `` `100` `` |
| JMESPath 作用于 `.all()` 但没写 `json.` | `[]` | `[?json.field=='x'].json.name` |
| {{ }} 内任何 JS 运行时错误 | `null`，节点仍成功 | 检查预览和输出值；用 try/catch 包装看报错信息 |

---

## 调试流程

表达式不工作时：

1. **检查括号**：有没有包在 {{ }} 里？
2. **检查数据来源**：是 webhook 数据吗？加上 `.body`
3. **检查空格**：字段名或节点名带空格？用方括号
4. **检查大小写**：节点名是否完全一致？
5. **检查路径**：属性路径对吗？
6. **用表达式编辑器**：预览会显示实际结果
   - 运行时错误会静默变成 `null`。如果输出是 `null`，预览里的错误才是真正原因。
7. **检查上下文**：是 Code 节点吗？去掉 {{ }}

---

**相关**：正确语法的可用示例见 [EXAMPLES.md](EXAMPLES.md)。
