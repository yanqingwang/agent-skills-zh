> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-error-handling/RESPONSE_SHAPES.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 响应形状

webhook API 响应体的约定，成功与错误都涵盖。目标是**可预测**：调用方、仪表盘或重试循环应能不靠猜地对你的响应做分支判断。选定一种形状，并在实例上的每个端点都保持一致。

本文件是一组带理由的偏好。唯一的硬规则是一致性：**项目内部的一致性优先于与本文件的一致。**如果你的仓库或公司已有成文的 API 风格，以它为准。

---

## 第一步：先对齐实例上已有的做法

采用本文件任何形状之前，先看已在运行的 API 工作流，复用它们的约定。一次性自定义形状一旦被调用方依赖就很难撤销；端点之间不一致比任何单个选择都糟。

先用 MCP 搜索，再逐个读取结果：

```javascript
search_nodes({ query: "webhook" })          // find webhook-shaped workflows via templates
n8n_list_workflows({ /* filter */ })          // list workflows on the instance
n8n_get_workflow({ id: "<id>" })               // read each one's Respond to Webhook nodes
```

在每个已有的 `Respond to Webhook` 里记下：

- 顶层键：信封还是裸数据，有没有 `error`/`message`/`request_id`。
- 成功响应体是包住 payload 还是裸返回。
- 实际在用的错误码字符串（`validation_error`、`bad_request` 还是 `INVALID_INPUT`）。
- 请求头约定（`Content-Type`、`Retry-After`、`X-Request-Id`）。

如果结果稀少、混杂，或看不出是否存在约定，**问用户**。"端点 A 和 B 用形状 X，C 用 Y；哪个是内部标准？"一句话省掉将来一次迁移。不要凭空发明领域前缀或信封。

---

## 成功形状

数据裸返回。对**创建或更新**资源的请求，优先在 200 里返回**完整资源**，而不是 `{ "ok": true }` 或只返回新 ID：

```json
{
  "customer_id": "cus_123",
  "balance": 4200,
  "currency": "USD",
  "created_at": "2026-04-25T12:34:00Z"
}
```

返回资源省掉调用方一次后续 GET，让它能确认实际落库的内容（服务端默认值、归一化后的值、生成的时间戳），也让要立即渲染结果的 UI 一次往返就拿到全部。

只在以下情况偏离：

- 资源确实很大且调用方不需要 → 返回 ID，并写明原因。
- 没有资源（事件采集、发完即忘）→ `{}` 或 `204 No Content`。
- payload 是列表形 → 顶层数组，或 `{ "items": [...] }`（对将来加分页元数据更友好）。

---

## 错误形状（默认信封）

```json
{
  "error": "<machine-readable code>",
  "message": "<human-readable explanation>"
}
```

- `error` 是**稳定的字符串标识符**，不是一句话。客户端按它分支。
- `message` 是给人看的版本：可安全记录，脱敏*之后*可安全展示给用户。
- 不要 `ok: false` 标志：HTTP 状态码已经区分了成功与失败。

按需附加的可选字段：

| 字段 | 何时包含 |
|---|---|
| `details` | 校验错误，附逐字段映射 |
| `retry_after` | 速率限制（同时设置 `Retry-After` 请求头） |
| `request_id` | 启用分布式追踪时（且要出现在*每条*响应上，不只错误） |
| `documentation_url` | 希望调用方先读文档的公开 API |

---

## `responseCode` 默认 200：每个错误分支都要显式设置

这是最常见的 API 错误处理 bug，值得单独一节，因为它产生*比没用更糟*的结果：响应体说失败，状态码说成功。

**每个 `Respond to Webhook` 节点的 `responseCode` 都默认 200**，包括你接到错误路径上的那些。返回 200 加 `{ "error": "..." }` 的错误分支，在调用方的 HTTP 客户端看来就是成功，于是它们的错误处理（以状态码为准）**永远不会触发**，错误响应体被当成数据处理。

所以：每个 Respond 节点都**显式**设置 `options.responseCode`，不只是成功那个。它在 `options` 之下；顶层 `responseCode` 会被忽略，节点照样返回 200。（这个坑也写在 **n8n-node-configuration** 的 NODE_FAMILY_GOTCHAS.md，"Webhook / Respond to Webhook"一节。）一个工作流可以有多个 Respond 节点，每种响应形状一个；n8n 返回最先触发的那个。

```json
{ "responseBody": "={{ { error: 'upstream_error', message: 'External service failed' } }}",
  "options": { "responseCode": 502 } }
```

要按原因选择状态码，用 Switch 路由到每个状态码一个静态 Respond：见 **API_WORKFLOWS.md** 的 "5xx: route by cause"。

---

## 状态码 → 原因

状态码是调用方收到的第一个信号，要认真选。

- **2xx**：成功。200 同步完成，202 "accepted, processing"（已受理，处理中）。
- **4xx**：调用方的问题。400 输入错误、401 未鉴权、403 不允许、404 不存在、409 冲突、429 限流。
- **5xx**：服务端的问题。500 内部意外错误、502 上游故障、503 暂不可用、504 上游超时。

区分 4xx 和 5xx 很重要，调用方的工具链依赖这个区分：

- 调用方的监控对 5xx（你方问题）告警，不对 4xx（他们的问题）告警。对坏输入返回 500，等于让*他们*因*自己*的 bug 被*你*的告警吵醒。
- 5xx 意味着"可重试"，4xx 意味着"别重试了"。
- 汇总错误率按类别分段：全压成 500，这个分段就没了。

### 错误码（小而稳定的一组）

加一个码没问题；改已有码的名字会破坏调用方。

**4xx：调用方的问题**

| 码 | 含义 |
|---|---|
| `validation_error` | 必填字段缺失 / 类型错误 |
| `invalid_input` | 字段存在但值无效 |
| `unauthorized` | 未鉴权或鉴权过期 |
| `forbidden` | 已鉴权但不被允许 |
| `not_found` | 资源不存在 |
| `conflict` | 与当前状态冲突（键重复、竞态） |
| `rate_limit_exceeded` | 请求过多 |
| `unsupported_media_type` | Content-Type 错误 |

**5xx：服务端的问题**

| 码 | 含义 |
|---|---|
| `internal_error` | 兜底，意外失败 |
| `upstream_error` | 第三方 API 返回错误 |
| `upstream_timeout` | 第三方 API 未及时响应 |
| `service_unavailable` | 暂时无法处理（宕机，或上游限流） |
| `not_implemented` | 此版本不支持该操作 |

---

## 校验错误详情（400）

`validation_error` 要带逐字段详情，让调用方不用猜就能修正请求。逐字段 Code 校验器（API_WORKFLOWS.md → "Exception: per-field messages"）直接产出这种结构：

```json
{
  "error": "validation_error",
  "message": "Validation failed (3 issues):\n• name: Missing required field \"name\"\n• email: \"not-an-email\" is not valid - Contact email address\n• plan: \"premium\" is not allowed. Must be one of: starter, pro, enterprise - Subscription plan",
  "details": { "name": "Missing required field \"name\"", "email": "\"not-an-email\" is not valid", "plan": "\"premium\" is not allowed" },
  "request_schema": { "type": "object", "properties": { } }
}
```

`message` 是给人看的概要（可展示），`details` 是结构化的逐字段映射（可绑定到 UI 字段），`request_schema` 是回显的 schema，让 LLM 驱动或程序化调用方在下一次尝试时自我修正。

---

## 限流响应（429）

```json
{
  "error": "rate_limit_exceeded",
  "message": "Too many requests. Retry after 30s.",
  "retry_after": "2026-05-08T21:10:05.135Z"
}
```

同时设置 HTTP `Retry-After` 请求头（在 Respond 节点的 `options.responseHeaders` 里）。守规矩的客户端只看请求头，不解析响应体。

---

## 错误响应里不能放什么

响应体会交给调用方。里面的所有内容都按公开对待。

| 不要包含 | 原因 |
|---|---|
| **堆栈跟踪**：`{ "stack": "Error at line 42 of /opt/..." }` | 暴露路径、版本、库名。对攻击者是礼物，对调用方没用。 |
| **上游错误原文**：`{ "details": "<raw upstream body>" }` | 上游可能在其中内嵌*它方*的 token 和 PII。对外只说 "upstream service failed" 加一个 request id；细节进你的日志。 |
| **SQL 查询**：`{ "query": "SELECT * FROM users WHERE ..." }` | 暴露 schema 和访问模式。 |
| **token / 凭据 / 鉴权值** | 看似无害的 `headers`、`config` 或 `request` 字段也可能带 token 值。审计错误响应体：泄露比你想象的容易。 |

模式始终一样：**完整错误只进私有日志，对外返回脱敏信息。**先记日志再响应的接线见 API_WORKFLOWS.md 的 "Don't leak internals"。

---

## Respond 节点形状（JSON，供社区 MCP 用）

成功：

```json
{
  "type": "n8n-nodes-base.respondToWebhook",
  "name": "Respond Success",
  "parameters": {
    "respondWith": "json",
    "responseBody": "={{ $json }}",
    "options": { "responseCode": 200, "responseHeaders": { "entries": [{ "name": "Content-Type", "value": "application/json" }] } }
  }
}
```

错误：

```json
{
  "type": "n8n-nodes-base.respondToWebhook",
  "name": "Respond Error",
  "parameters": {
    "respondWith": "json",
    "responseBody": "={{ { error: 'upstream_error', message: 'External service failed' } }}",
    "options": { "responseCode": 502, "responseHeaders": { "entries": [{ "name": "Content-Type", "value": "application/json" }] } }
  }
}
```

两个容易坑人的点：

- **始终显式设置 `Content-Type: application/json`。**默认行为取决于响应体形状，不可靠。
- **用 `respondWith: "json"` 时传对象，不要传字符串化后的字符串。**给它 `JSON.stringify(obj)`，节点会把那个字符串*再*序列化一次，得到双重编码的响应体。要么用 `respondWith: "json"` 配对象表达式（`={{ { error: 'x' } }}`），要么保留 `JSON.stringify(...)` 让节点把它当作已定稿的响应体：二选一并保持一致。（见 **n8n-node-configuration** 的 NODE_FAMILY_GOTCHAS.md。）
