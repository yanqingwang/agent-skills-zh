> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-error-handling/ERROR_WORKFLOWS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 工作流级错误工作流

节点级错误输出处理的是你预判到、且记得接线的那部分失败。**工作流级错误工作流**是其余一切的兜底——对无人值守的工作流（定时、cron、队列 worker）而言，它决定了你是"任务三天前就悄悄停了"，还是"一出问题警报就到了"。

节点级输出**接不住**的：

- 你忘了接线的节点上的失败。
- 节点之间的崩溃。
- 整个工作流超时。
- 触发器失败。

当未被处理的错误从上述任何一处漏出，n8n 会带着失败上下文调用指定的**错误工作流**。这个工作流建一次，就能服务于所有指向它的工作流。

---

## 错误工作流收到什么

它以一个 **Error Trigger** 节点开头，触发时的负载大致如下：

```json
{
  "execution": {
    "id": "...",
    "url": "https://your-n8n/workflow/<wfId>/executions/<execId>",
    "retryOf": "...",
    "error": {
      "name": "NodeApiError",
      "message": "...",
      "description": "...",
      "timestamp": 1715000000000
    },
    "lastNodeExecuted": "Fetch order",
    "mode": "trigger"
  },
  "workflow": { "id": "...", "name": "Sync Stripe customers" }
}
```

注意**没有**什么：负载里有错误消息和失败节点的*名称*（`lastNodeExecuted`），但**没有导致失败的输入数据**。拿回它要多走一步（见下）。

---

## 最小错误工作流（捕获 → 通知）

对多数工作流，这就够了：

```
Error Trigger → Slack / email (post to #incidents)
```

两个节点：警报文本直接用表达式写在消息字段里（见下），所以不需要 Set 节点。快、不容易错，还把沉默变成了消息。用 `n8n_create_workflow`（或部分更新 ops）建好，然后在 UI 里指派（见下文"指派"一节）。

---

## 警报里放什么

一条好的通知能让值班人员不开 n8n 就能行动。从负载里取这些：

| 字段 | 表达式 |
|---|---|
| 工作流名称 | `{{ $json.workflow.name }}` |
| 工作流 ID | `{{ $json.workflow.id }}` |
| 编辑器链接 | `{{ $json.execution.url.split('/executions/')[0] }}` |
| 执行 ID | `{{ $json.execution.id }}` |
| 执行链接 | `{{ $json.execution.url }}` |
| 失败节点 | `{{ $json.execution.lastNodeExecuted }}` |
| 错误消息 | `{{ $json.execution.error.message }}` |
| 错误描述 | `{{ $json.execution.error.description }}`（常常为空，有值时很有用） |
| 时间戳 | `{{ DateTime.fromMillis($json.execution.error.timestamp).toISO() }}` |

`timestamp` 是 Unix 毫秒数，用 Luxon 的 `DateTime.fromMillis(...)` 格式化。执行 `url` 是 `{base}/workflow/{id}/executions/{execId}`，去掉 `/executions/...` 尾部就得到编辑器 URL。

一段实用的 Slack 正文：

```
Workflow failure: *{{ $json.workflow.name }}* (`{{ $json.workflow.id }}`)
Open editor: {{ $json.execution.url.split('/executions/')[0] }}
Failed node: `{{ $json.execution.lastNodeExecuted }}`
Error: {{ $json.execution.error.message }}
Execution: {{ $json.execution.url }}
Time: {{ DateTime.fromMillis($json.execution.error.timestamp).toISO() }}
```

两个链接很关键：**编辑器链接**让值班人员开始修复，**执行链接**让他们看到确切失败的这次运行。少一个就多一步。"Workflow failed."不算警报，只是提醒你接下来要从零排查。

---

## 加强版：找回失败的输入

Error Trigger 负载告诉你*哪个*节点失败，不包括*什么数据*弄坏了它。要拿到肇事负载，用 **n8n** 节点取回这次执行：

```
Error Trigger
  → n8n  (resource: Execution, operation: Get,
          Execution ID: {{ $json.execution.id }},
          Include Execution Details: true)
  → Set  (extract failed-node input from the execution data)
  → Switch (route by severity)
        ├── high → PagerDuty
        ├── med  → Slack #incidents
        └── low  → Slack #monitoring
  → Data Table (log for tracking)
```

"Include Execution Details: true" 会请求 `GET /executions/{id}?includeData=true` 并返回完整运行数据，你可以从 `data.resultData.runData[<lastNodeExecuted>]` 里取出失败节点的输入。这样值班消息就能带上真正的肇事负载（哪个客户、哪个订单号），而不只是"节点 X 报错了"。

注意事项，每一条都可能让错误工作流自己变成*新的*静默失败：

- **需要在这个工作流上配置 n8n API 凭据**（Settings → API → personal access token，然后挂到 n8n 节点上）。没有它，节点抛 401，这是*错误工作流内部*的未处理错误。
- **要求失败的工作流持久化执行数据**（Save Execution Data，实例默认或按工作流设置）。否则 API 只返回元数据。
- **n8n 节点调用本身可能失败**（API 宕机、限流）。把它的错误输出（`sourceIndex: 1`）接到一个仍会发通知的兜底上，否则原始错误会消失在取数失败背后。

多数时候最小版就够。加强版的价值在生产关键工作流上，就是那些值班响应以分钟计的场景。

---

## 指派（只能通过 UI，MCP 做不到）

> 错误工作流在 n8n **UI** 中指派：按工作流在 **Workflow Settings → Error Workflow** 下设置，或设为实例级默认。社区 MCP **没有**设置该指派的工具。`n8n_update_partial_workflow` 提供 `updateSettings` op，但错误工作流设置经它写入并不可靠，请在 UI 里确认。

所以 Agent 的职责是：**用 MCP 建好错误工作流，然后把确切的 UI 步骤交给用户**（"打开失败的工作流 → Settings → Error Workflow → 选择 '<name>'"），并提醒对*每个*无人值守工作流都做一遍（或者一次性设好实例默认）。只建不指派等于白建；触发器只对指向它的工作流生效。

---

## 错误工作流何时触发（何时不触发）

**触发**于：

- 某节点抛出未处理错误（没有接到已连线的节点级错误输出）。
- 工作流本身失败（超时、OOM）。
- 触发器失败（少见，非 webhook 触发器可能出现）。

**不触发**于：

- 节点的错误输出已接线——即使处理器什么都不做。n8n 认为错误已被*处理*。
- 你手动停止了执行。
- 工作流处于暂停/未激活状态。

第二种情况最隐蔽：**节点级错误输出接到一个丢弃数据的空操作上，会*压制*错误工作流。** 在 n8n 看来错误已被处理，尽管它被吞掉了。所以只有当你真的要对错误采取行动时才做节点级捕获；想让失败冒泡到兜底，就别接线。

---

## 错误工作流不应该做什么

- **发起自己也可能失败、且没有兜底的外部调用。** 错误工作流一旦失败，原始错误就消失了，你在第一个静默失败之上又加了一个。
- **耗时明显。** 它同步运行；慢的错误工作流会放大原始失败的影响。

保持快：解析、通知、返回。

---

## 递归陷阱

如果被监控的工作流向 Slack 发警报，而*错误*工作流也向 Slack 发警报，那 Slack 一宕机两个都完，错误工作流失败，失败无人知晓。n8n 不会因自身失败再次触发（不会无限循环），但警报丢了。

缓解手段：

- **用与被监控工作流不同的渠道。** 如果全都通知 Slack，错误工作流就该用邮件（反之亦然）。
- **加兜底**，主通知失败时写入 Data Table（`n8n_manage_datatable`），保证总有痕迹。
- **依赖实例级日志**（服务器日志、Sentry），让错误工作流的失败也能在 n8n 之外露出痕迹。

---

## 验证它真的有效

建好并指派之后：

1. 做一个一次性的必失败工作流——比如向无效 URL 发 HTTP Request，**不**接错误输出，让失败保持未处理。
2. 运行它。
3. 确认错误工作流触发、通知送达。

这能抓住那些直到真实事故才现形的配置错误：指派错工作流、渠道不对、缺 API 凭据。在依赖这套警报之前做一次。

---

## 漂移观察

Error Trigger 负载的字段结构可能随 n8n 版本变动。如果某个字段不在本文件所说的位置，查当前 n8n 文档并更新你的表达式，改名的字段会静默地表现为空警报，而不是抛错。
