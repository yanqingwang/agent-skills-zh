> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-expression-syntax/EXAMPLES.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# n8n 表达式示例

来自 n8n 工作流的真实可用示例。

---

## 示例 1：Webhook 表单提交

**场景**：表单提交 webhook 推送到 Slack

**工作流**：Webhook → Slack

**Webhook 输入**（POST）：
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "company": "Acme Corp",
  "message": "Interested in your product"
}
```

**Webhook 节点输出**：
```json
{
  "headers": {"content-type": "application/json"},
  "params": {},
  "query": {},
  "body": {
    "name": "John Doe",
    "email": "john@example.com",
    "company": "Acme Corp",
    "message": "Interested in your product"
  }
}
```

**在 Slack 节点中**（text 字段）：
```
New form submission! 📝

Name: {{$json.body.name}}
Email: {{$json.body.email}}
Company: {{$json.body.company}}
Message: {{$json.body.message}}
```

**输出**：
```
New form submission! 📝

Name: John Doe
Email: john@example.com
Company: Acme Corp
Message: Interested in your product
```

---

## 示例 2：HTTP API 到数据库

**场景**：从 API 拉取用户数据并插入数据库

**工作流**：Schedule → HTTP Request → Postgres

**HTTP Request 返回内容**：
```json
{
  "data": {
    "users": [
      {
        "id": 123,
        "name": "Alice Smith",
        "email": "alice@example.com",
        "role": "admin"
      }
    ]
  }
}
```

**在 Postgres 节点中**（INSERT 语句）：
```sql
INSERT INTO users (user_id, name, email, role, synced_at)
VALUES (
  {{$json.data.users[0].id}},
  '{{$json.data.users[0].name}}',
  '{{$json.data.users[0].email}}',
  '{{$json.data.users[0].role}}',
  '{{$now.toFormat('yyyy-MM-dd HH:mm:ss')}}'
)
```

**结果**：用户已插入，带当前时间戳

---

## 示例 3：多节点数据流

**场景**：Webhook → HTTP Request → Email

**工作流结构**：
1. Webhook 接收订单 ID
2. HTTP Request 拉取订单详情
3. Email 发送确认邮件

### 节点 1：Webhook

**接收内容**：
```json
{
  "body": {
    "order_id": "ORD-12345"
  }
}
```

### 节点 2：HTTP Request

**URL 字段**：
```
https://api.example.com/orders/{{$json.body.order_id}}
```

**返回内容**：
```json
{
  "order": {
    "id": "ORD-12345",
    "customer": "Bob Jones",
    "total": 99.99,
    "items": ["Widget", "Gadget"]
  }
}
```

### 节点 3：Email

**主题**：
```
Order {{$node["Webhook"].json.body.order_id}} Confirmed
```

**正文**：
```
Dear {{$node["HTTP Request"].json.order.customer}},

Your order {{$node["Webhook"].json.body.order_id}} has been confirmed!

Total: ${{$node["HTTP Request"].json.order.total}}
Items: {{$node["HTTP Request"].json.order.items.join(', ')}}

Thank you for your purchase!
```

**邮件结果**：
```
Subject: Order ORD-12345 Confirmed

Dear Bob Jones,

Your order ORD-12345 has been confirmed!

Total: $99.99
Items: Widget, Gadget

Thank you for your purchase!
```

---

## 示例 4：日期格式化

**场景**：各种日期格式输出

**当前时间**：2025-10-20 14:30:45

### ISO 格式
```javascript
{{$now.toISO()}}
```
**输出**：`2025-10-20T14:30:45.000Z`

### 自定义日期格式
```javascript
{{$now.toFormat('yyyy-MM-dd')}}
```
**输出**：`2025-10-20`

### 仅时间
```javascript
{{$now.toFormat('HH:mm:ss')}}
```
**输出**：`14:30:45`

### 完整可读格式
```javascript
{{$now.toFormat('MMMM dd, yyyy')}}
```
**输出**：`October 20, 2025`

### 日期运算 - 未来
```javascript
{{$now.plus({days: 7}).toFormat('yyyy-MM-dd')}}
```
**输出**：`2025-10-27`

### 日期运算 - 过去
```javascript
{{$now.minus({hours: 24}).toFormat('yyyy-MM-dd HH:mm')}}
```
**输出**：`2025-10-19 14:30`

---

## 示例 5：数组操作

**数据**：
```json
{
  "users": [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"}
  ]
}
```

### 第一个用户
```javascript
{{$json.users[0].name}}
```
**输出**：`Alice`

### 最后一个用户
```javascript
{{$json.users[$json.users.length - 1].name}}
```
**输出**：`Charlie`

### 所有邮箱（Join）
```javascript
{{$json.users.map(u => u.email).join(', ')}}
```
**输出**：`alice@example.com, bob@example.com, charlie@example.com`

### 数组长度
```javascript
{{$json.users.length}}
```
**输出**：`3`

---

## 示例 6：条件逻辑

**数据**：
```json
{
  "order": {
    "status": "completed",
    "total": 150
  }
}
```

### 三元运算符
```javascript
{{$json.order.status === 'completed' ? 'Order Complete ✓' : 'Pending...'}}
```
**输出**：`Order Complete ✓`

### 默认值
```javascript
{{$json.order.notes || 'No notes provided'}}
```
**输出**：`No notes provided`（notes 字段不存在时）

### 多条件
```javascript
{{$json.order.total > 100 ? 'Premium Customer' : 'Standard Customer'}}
```
**输出**：`Premium Customer`

---

## 示例 7：字符串操作

**数据**：
```json
{
  "user": {
    "email": "JOHN@EXAMPLE.COM",
    "message": "  Hello World  "
  }
}
```

### 转小写
```javascript
{{$json.user.email.toLowerCase()}}
```
**输出**：`john@example.com`

### 转大写
```javascript
{{$json.user.message.toUpperCase()}}
```
**输出**：`  HELLO WORLD  `

### 去首尾空格
```javascript
{{$json.user.message.trim()}}
```
**输出**：`Hello World`

### 截取子串
```javascript
{{$json.user.email.substring(0, 4)}}
```
**输出**：`JOHN`

### 替换
```javascript
{{$json.user.message.replace('World', 'n8n')}}
```
**输出**：`  Hello n8n  `

---

## 示例 8：带空格的字段

**数据**：
```json
{
  "user data": {
    "first name": "Jane",
    "last name": "Doe",
    "phone number": "+1234567890"
  }
}
```

### 方括号写法
```javascript
{{$json['user data']['first name']}}
```
**输出**：`Jane`

### 组合
```javascript
{{$json['user data']['first name']}} {{$json['user data']['last name']}}
```
**输出**：`Jane Doe`

### 嵌套带空格字段
```javascript
Contact: {{$json['user data']['phone number']}}
```
**输出**：`Contact: +1234567890`

---

## 示例 9：Code 节点（直接访问）

**Code 节点**：转换 Webhook 数据

> 这里只展示 Code 节点内部的语法差异。真实工作流里，同样的转换用一个 Edit Fields 字段即可完成：
> `{{ $json.body.items.map(item => item.toUpperCase()) }}`，不需要 Code 节点。

**输入**（来自 Webhook 节点）：
```json
{
  "body": {
    "items": ["apple", "banana", "cherry"]
  }
}
```

**代码**（JavaScript）：
```javascript
// ✅ Direct access (no {{ }})
const items = $json.body.items;

// Transform to uppercase
const uppercased = items.map(item => item.toUpperCase());

// Return in n8n format
return [{
  json: {
    original: items,
    transformed: uppercased,
    count: items.length
  }
}];
```

**输出**：
```json
{
  "original": ["apple", "banana", "cherry"],
  "transformed": ["APPLE", "BANANA", "CHERRY"],
  "count": 3
}
```

---

## 示例 10：环境变量

**配置**：环境变量 `API_KEY=secret123`

### 在 HTTP Request 中（Headers）
```javascript
Authorization: Bearer {{$env.API_KEY}}
```
**结果**：`Authorization: Bearer secret123`

### 在 URL 中
```javascript
https://api.example.com/data?key={{$env.API_KEY}}
```
**结果**：`https://api.example.com/data?key=secret123`

---

## 真实工作流模板

**基于 n8n 模板 #2947**（Weather to Slack）

### 工作流结构
Webhook → OpenStreetMap API → Weather API → Slack

### Webhook 斜杠命令
**输入**：`/weather London`

**Webhook 接收内容**：
```json
{
  "body": {
    "text": "London"
  }
}
```

### OpenStreetMap API
**URL**：
```
https://nominatim.openstreetmap.org/search?q={{$json.body.text}}&format=json
```

### Weather API (NWS)
**URL**：
```
https://api.weather.gov/points/{{$node["OpenStreetMap"].json[0].lat}},{{$node["OpenStreetMap"].json[0].lon}}
```

### Slack 消息
```
Weather for {{$json.body.text}}:

Temperature: {{$node["Weather API"].json.properties.temperature.value}}°C
Conditions: {{$node["Weather API"].json.properties.shortForecast}}
```

---

## 总结

**关键模式**：
1. Webhook 数据在 `.body` 下
2. 表达式用 `{{}}`（Code 节点除外）
3. 用 `$node["Node Name"].json` 引用其他节点
4. 带空格的字段名用方括号
5. 节点名区分大小写

**最常用写法**：
- `{{$json.body.field}}` - Webhook 数据
- `{{$node["Name"].json.field}}` - 其他节点数据
- `{{$now.toFormat('yyyy-MM-dd')}}` - 时间戳
- `{{$json.array[0].field}}` - 数组访问
- `{{$json.field || 'default'}}` - 默认值

---

**相关**：错误示例与修复方法见 [COMMON_MISTAKES.md](COMMON_MISTAKES.md)。
