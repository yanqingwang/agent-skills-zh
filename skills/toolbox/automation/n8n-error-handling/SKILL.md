---
name: n8n-error-handling
description: 配置 n8n 错误处理，让失败响亮、结构化且可恢复。在构建任何 webhook/API 工作流、定时或无人值守工作流，或任何静默失败会丢失用户可见工作的路径时使用——以及当用户提到 error handling、onError、continueErrorOutput、error branches/outputs（错误分支/错误输出）、retries（重试）、retryOnFail、Respond to Webhook 状态码、4xx/5xx、Error Trigger，或 "my workflow fails silently"（我的工作流静默失败）时使用。涵盖每节点错误输出与接线、重试/自愈、error-trigger 工作流，以及 4xx/5xx 响应形态。
---

> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-error-handling/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# n8n 错误处理

默认情况下，当一个 n8n 节点抛出错误时，**整个工作流会停摆**。对于你在现场盯着的交互式运行来说，这没问题，你能看到红色的节点并修复它。但对任何无人值守的场景（webhook API、cron 任务、队列 worker、agent 工具），这都是错误的默认：调用方得到超时或空的 500，运维收不到任何告警，症状表现为"集成突然不工作了"，没有日志，也没有线索。

本 Skill 的主题是让失败**响亮、结构化且可恢复**，最好能做到**自愈**，让瞬时抖动根本到不了人手上。

防止大多数静默失败的两个核心思想：

- **每节点错误输出** ， 节点的失败会沿你控制的第二个输出分流，而不是终结整个运行。
- **工作流级别的错误工作流** ， 一个兜底机制，凡逃过每节点处理的失败（超时、节点间崩溃、未接线的失败）都会触发它。

---

## 你什么时候真正需要这个

| 工作流形态 | 错误处理姿态 |
|---|---|
| Webhook / API（任何带 `Respond to Webhook` 的） | **必需。** 每个可能失败的节点的错误输出都要接线；状态码与原因匹配。 |
| 定时 / cron / 队列 worker / agent 工具（无人值守） | **必需。** 一个工作流级别的错误工作流，外加网络类节点上的 `retryOnFail`。 |
| 你自己运行并盯着看的内部一次性任务 | **可选。** 默认的 `onError: "stopWorkflow"` 就够了，你会看到红色节点并重跑。 |

分界线：**只要输出会被你以外的任何人看到**（下游系统、最终用户、值班工程师）失败就必须被处理，而不是被吞掉。如果唯一的观察者是你自己，且失败的代价是"我注意到然后重跑"，那宽松一点没问题。

---

## 头号静默陷阱：每节点错误输出是两步配置

这是 n8n 工作流"处理"错误时最常见的、实际上却把错误吞掉的方式。把节点的失败路由到处理器需要**两处**改动，只做其中一处看起来是完整的，但行为不对：

1. **在节点上设置 `onError: "continueErrorOutput"`。** 这一步*创建*出第二个输出。没有它，无论你怎么接线，`main[1]` 都不存在。
2. **把那个错误输出接线**（`connections.<node>.main[1]`，即 `sourceIndex: 1`）到一个真正的处理器。没有目标，错误数据就被发射到虚空里。

只做其一不做其二，就会踩中某种失败模式：

| 你的操作 | 运行时的表现 |
|---|---|
| `onError` 已设置，错误输出**未**接线 | 错误数据被静默丢弃。下游不触发。面板上这次运行显示为**成功**。最糟的情况，任何地方都没有错误日志。 |
| 错误输出已接线，`onError` **未**设置 | 插槽永不触发；处理器不可达。失败时工作流直接**停摆**（默认 `stopWorkflow`）。 |
| 两者都做了 | 失败沿 `main[1]` 路由到你的处理器。✅ |

### 用 `n8n_update_partial_workflow` 同时完成两步

```javascript
// 1) Turn on the error output (creates main[1])
{ type: "updateNode", nodeName: "HTTP Request",
  changes: { onError: "continueErrorOutput" } }

// 2) Wire the error output to a handler. sourceIndex: 1 = the error output.
{ type: "addConnection",
  source: "HTTP Request",
  target: "Handle Error",
  sourceIndex: 1 }
```

`sourceIndex: 0` 是成功路径，`sourceIndex: 1` 是错误路径。（对 IF 节点，别名 `branch: "true"`/`"false"` 映射到索引 0/1；对一般的可能失败节点，用显式的 `sourceIndex: 1`。）

**然后验证。** 这个陷阱在 `validate_workflow` 里不会暴露，半接线的错误输出能干净地通过校验。用 `n8n_get_workflow` 拉取工作流，确认**两半**都在：

- 节点的 `onError` 是 `"continueErrorOutput"`。
- `connections["HTTP Request"].main[1]` 包含你的处理器。

`onError` 的合法取值：

| 取值 | 效果 |
|---|---|
| `"stopWorkflow"`（默认） | 错误使整个工作流停摆。 |
| `"continueRegularOutput"` | 错误条目从**正常**输出流出。少见，通常是错的，下游拿到错误形状的数据还继续跑。 |
| `"continueErrorOutput"` | 错误条目从**独立的**错误输出（`main[1]`）流出。就是你要接线的那一个。 |

完整的失败模式目录、扇入/扇出形态与验证方法：**NODE_ERROR_OUTPUTS.md**。

### 错误输出永远看不到的失败

即使错误输出接线完全正确，仍会漏掉几类失败。已在 n8n 2.38.5 上验证：

| 失败 | `continueErrorOutput` 下 | `continueRegularOutput` 下 |
|---|---|---|
| `{{ }}` **内部**的 JS 错误（对缺失路径做 TypeError、对坏输入做 `JSON.parse`、抛出 `Error`、JMESPath 语法错误） | 什么都不触发；字段为 `null`，条目走**成功**路径 | 相同 |
| Python Code 节点**运行前被拒绝**（import 被拦截、dunder 访问：`Security violations detected`）或**返回形状不对**（each-item 模式下返回 list） | 节点被标记失败，但**未改变的输入条目从成功输出离开**；`main[1]` 保持为空，执行显示成功 | 未改变的输入条目直接通过 |
| 代码**运行中**抛出异常（`raise`/`throw`、`KeyError`、`NameError`） | 以 `{ error }` 路由到 `main[1]` ✅ | 主输出上出现 `{ error }` 条目 |

所以仅靠错误分支防不住这些：

- **守护数据本身，而不只是节点。** 在一个输出很重要的变换之后，检查你产出的
  字段是否存在（用 IF/Filter 判断 `{{ $json.total !== undefined && $json.total !== null }}`），
  并自己把缺失的情况送到错误路径上。
- **试运行并读取节点状态与输出值。** Python 的情形会显示绿色执行里嵌着一个红色节点。
  表达式的情形则只显示一串 `null`。
- 根因与修法：**n8n-expression-syntax**（Debugging 一节）与 **n8n-code-python**（Errors 与 `onError` 一节）。

---

## 自愈优先：先上 `retryOnFail`，再接错误路径

在构建错误分支之前，先把瞬时失败吸收掉，让它们根本到不了那些分支。在**任何调用网络服务的节点**上，HTTP Request、通讯类（Gmail/Slack/Discord）、数据库、AI 节点、第三方集成，设置节点级重试：

```javascript
{ type: "updateNode", nodeName: "HTTP Request",
  changes: {
    retryOnFail: true,
    maxTries: 3,
    waitBetweenTries: 5000   // ms
  } }
```

为什么这一步**先行**：429 或上游短暂抖动会自动重试并通常自己成功。错误输出于是只在*真正、持续*的失败时触发，你的 5xx 响应和值班告警反映的是真实问题而非噪音。

需要知道的引擎限制：重试在**任何**错误上都会触发（没有按状态码过滤的机制），`maxTries` 上限 5，`waitBetweenTries` 上限 5000ms，所以 5000 既是上限也是合理默认值。节点专属注意事项见 **n8n-node-configuration**（NODE_FAMILY_GOTCHAS.md）。

---

## API 工作流：标准形态

一个 webhook 触发、要响应调用方的工作流，有一条压倒一切的规则：**不允许有悬挂分支**。每条路径（成功与每一种错误）都必须终结于一个 `Respond to Webhook`，否则调用方会一直干等到超时。

```
Webhook (responseMode: "responseNode")
  ├── validate input → process → Respond (200, body)
  └── (any fallible node's error output → sourceIndex 1)
            → Respond (4xx/5xx, structured error body)
            → optional: log full error privately / notify
```

让这套形态成立的三件事：

1. **扇入到同一个错误响应器。** 多个可能失败的节点可以把各自的 `main[1]` 路由到一个 `Respond` 节点。保持图的可读性。
2. **校验失败（4xx）在上游检查，而不是靠错误输出。** 缺字段不是节点*崩溃*，它是一个有已知响应的预期结果。用 IF/Switch（或下面的按字段校验器）对它分支，并直接返回 400/401/403/404。错误输出留给*意外*失败（5xx）。
3. **`options.responseCode` 默认是 200，即使在错误分支上。** 这本身就是一个静默陷阱（见 RESPONSE_SHAPES.md 与 **n8n-node-configuration** 的 NODE_FAMILY_GOTCHAS.md）：返回 200 加错误体的错误分支，在调用方的 HTTP 客户端看来就是成功，于是他们的错误处理永不触发。在每个 Respond 节点上显式设置 `responseCode`。

### 输入校验：把条件放在画布上

把检查放进一个 **IF** 节点：每条规则一个布尔条件（`is true`），组合器用 `and`。true → 你的逻辑（200）；false → 一个 400 Respond，带静态的 `validation_error` 响应体，回显期望的 schema，让调用方能够自我纠正。当调用方需要**按字段**的消息（LLM 客户端、公开 API）时，把 IF 换成一个 **Code** 节点，遍历 schema 列表并返回 `{ valid, validationError, details, requiredSchema }`，并附注 `Why Code: IF considered — per-field messages need a loop over the schema`。两种模式、约束速查手册与转义规则都在 **API_WORKFLOWS.md**。

---

## 响应形态：把原因映射到状态码

一个返回 `text/plain "Internal Server Error"` 的 5xx，技术上算错误响应，实际上毫无用处。而且并非每个失败都是 5xx。**让状态码与请求失败的*原因*匹配**，因为调用方会据此分支：他们的监控对 5xx（你的锅）告警而不对 4xx（他们的锅）告警，并且 5xx 暗示"可以重试"而 4xx 暗示"别重试"。

**常见错误：** 把所有东西（包括坏输入）都接到一个返回 500 `internal_error` 的 `Respond` 上。于是调用方分不清他们的 bug 和你的宕机，你的错误率也无法区分真实事故与客户端噪音。

| 原因 | 状态码 | `error` 代码 | 在哪里处理 |
|---|---|---|---|
| 必填字段缺失 / 类型错误 | 400 | `validation_error` | 上游检查（IF 条件 / 按字段校验器），不是错误输出 |
| 认证缺失或无效 | 401 | `unauthorized` | 上游检查 |
| 已认证但无权限 | 403 | `forbidden` | 上游检查 |
| 请求中的资源 ID 格式合法，但你的数据里不存在 | 404 | `not_found` | 对查找*结果*分支，而不是对它的错误 |
| 与当前状态冲突（重复、竞态） | 409 | `conflict` | 用逻辑检测 |
| 调用方超过速率限制 | 429 | `rate_limit_exceeded` | 设置 `Retry-After` 头 |
| 节点抛错，原因不明 | 500 | `internal_error` | 错误输出路径 |
| 第三方 API 返回错误 | 502 | `upstream_error` | HTTP 节点的错误输出 |
| 当前无法处理（下游宕了） | 503 | `service_unavailable` | 检测特定错误，提示可重试 |
| 第三方 API 超时 | 504 | `upstream_timeout` | 错误输出按消息过滤 |

所以有两条截然不同的流：**4xx 在干活之前就决定了**（IF/Switch + 专用 Respond），**5xx 从错误输出里出来**（"我们试了，但它坏了"）。

**用 Switch 按原因路由；每个状态码一个静态 Respond。** 从错误中挑状态码是一个路由问题。一个基于错误消息的 Switch 对其分类，每个输出接到一个 `options.responseCode` 和响应体都固定的 Respond：

```
error outputs (main[1]) ─→ Switch "Classify error" (on $json.error.message)
                             ├─ contains "INVALID_ID"     → Respond 400 validation_error
                             ├─ contains "429"            → Respond 429 rate_limit_exceeded
                             ├─ contains "timeout"        → Respond 504 upstream_timeout
                             └─ fallback (extra output)   → Respond 500 internal_error
```

每个状态码都可见于画布之上，新增一个就是加一条规则。把 Switch 的 `options.fallbackOutput` 设为 `extra`，否则未匹配的错误会被丢弃、调用方会挂起。用一个 Respond 加计算出的状态码，只在恰好两种结果时可以接受，即在其 Response Code 字段里写一个简短的三元表达式。Switch 的 JSON 在 **API_WORKFLOWS.md**。

默认的信封是 `{ "error": "<code>", "message": "<human text>" }` ，HTTP 状态码已经说明了成功与失败，所以不需要 `ok: false` 标志。**绝不把内部细节**（堆栈、SQL、上游响应体、token）**泄漏进响应**，私下记录日志，返回经过净化的消息。关联 ID、`retry_after`、校验 `details` 与完整的禁止泄漏清单在 **RESPONSE_SHAPES.md**。

---

## 工作流级错误工作流（兜底）

每节点输出处理的是你预见到的、且记得接线的节点上的失败。**错误工作流**接住其余一切：你忘了接线的节点、节点之间的崩溃、整个工作流的超时、触发器失败。对无人值守的工作流，这是把"它静默地停了"变成"一条告警到了"的安全网。

把它建成一个独立的、以 **Error Trigger** 节点开头的工作流。n8n 会带着失败上下文调用它：

```json
{
  "execution": { "id": "...", "url": "...", "lastNodeExecuted": "Fetch order",
    "error": { "name": "NodeApiError", "message": "...", "timestamp": 1715000000000 } },
  "workflow": { "id": "...", "name": "Sync Stripe customers" }
}
```

最小版本，**捕获 → 通知**：

```
Error Trigger → Slack/email (post to #incidents; the alert text is built with expressions in the message field)
```

一条好的告警包含工作流名称、编辑器链接与失败执行的链接、失败节点名，以及**真实的**错误消息（而不是"工作流失败了"）。字段表达式和可选的"通过 n8n 节点取回失败输入"升级见 **ERROR_WORKFLOWS.md**。

两个值得提前点名的陷阱：

- **递归陷阱。** 如果错误工作流向 Slack 发通知，而挂掉的恰恰是 Slack，错误工作流也会失败，原始错误随之消失。在与被监控工作流所用*不同*的渠道上发通知（多数工作流向 Slack 告警 → 错误工作流用邮件），并加一个兜底（写入 Data Table），让失败的通知也留下痕迹。
- **被"处理过"的错误不会冒泡。** 如果节点的错误输出接到了一个丢弃数据的 no-op，n8n 会认为该错误*已被处理*，错误工作流**不会**触发。只有当你真的要用这个错误做点什么时才做每节点捕获。

> **社区 MCP 做不到的事：** 指派错误工作流（实例默认或按工作流覆盖）是 n8n 的 **UI 设置**，Workflow Settings → Error Workflow。没有 MCP 工具能设置它。用 MCP 搭好错误工作流，然后告诉用户确切的 UI 步骤把它接上，并对每个无人值守工作流重复这一步（或设置实例默认）。

---

## 社区 MCP 做不到的事

| 想做的事 | 现实 |
|---|---|
| 设置工作流的 **Error Workflow** 设置 | 仅 UI（Workflow Settings → Error Workflow）。无 MCP 工具。先建工作流，再把 UI 步骤交给用户。 |
| 切换其他**工作流设置**（Save Execution Data、时区、超时、caller policy） | 仅 UI。`n8n_update_partial_workflow` 有 `updateSettings`，但错误工作流指派并未可靠暴露，在 UI 中确认。 |
| 启用实例级错误日志（Sentry、服务器日志） | 实例配置，完全在 n8n 工作流之外。 |

MCP **能**做的：搭建错误工作流、在节点上设置 `onError`/`retryOnFail`（`updateNode`/`patchNodeField`）、接线错误输出（`addConnection` 加 `sourceIndex: 1`）、校验（`validate_workflow`、`n8n_validate_workflow`）、自动修复常见问题（`n8n_autofix_workflow`）、测试（`n8n_test_workflow`）、检查失败（`n8n_executions`）。

---

## 反模式

| 反模式 | 会出什么问题 | 修法 |
|---|---|---|
| `onError` 已设置但错误输出未接线 | 错误被静默丢弃；运行显示为**成功** | 把 `sourceIndex: 1` 接到真正的处理器，或把 `onError` 改回 `stopWorkflow` 让失败响亮 |
| 错误输出已接线但 `onError` 未设置 | 插槽永不触发；处理器不可达；失败时工作流停摆 | 设置 `onError: "continueErrorOutput"` |
| Webhook → 处理 → 响应，没有错误分支 | 调用方得到超时或 n8n 的通用 500 | 把每个可能失败节点的错误输出接到一个 Respond |
| 错误分支返回 200 加 `{error}` 响应体 | 调用方的客户端读到成功；其错误处理永不触发 | 在错误 Respond 上显式设置 `options.responseCode` 为 4xx/5xx |
| 万物皆 500 `internal_error` | 调用方分不清他们的坏输入和你的宕机 | 按原因映射状态码（4xx 调用方，5xx 你） |
| 在 Code 节点里捕获错误并作为数据返回 | 下游处理错误形状的数据并继续跑 | 让它抛出；用 `onError: "continueErrorOutput"` + 接好线的路径 |
| 网络节点没有 `retryOnFail` | 每个瞬时 429/抖动都变成 5xx 冒出来；告警被噪音触发 | `retryOnFail: true, maxTries: 3, waitBetweenTries: 5000` |
| 在 Respond 的 Response Code 或响应体里塞函数体 | 路由逻辑藏在字段里，运行时错误变成静默的 `null` | 按原因 Switch → 每个状态码一个静态 Respond |
| 无人值守工作流没有错误工作流 | 真实的失败无处可去 | 搭建 Error Trigger 工作流并在 UI 中指派 |
| 错误工作流向工作流所监控的同一渠道发通知 | 渠道挂了 → 错误工作流也失败 → 错误消失 | 用不同渠道 + Data Table 兜底 |
| 把 `$json.error`（堆栈/SQL/token）泄漏进响应 | 向调用方/攻击者暴露内部细节 | 私下记日志，返回净化后的消息 |

---

## 参考文件

| 文件 | 何时读 |
|---|---|
| **NODE_ERROR_OUTPUTS.md** | 在单个可能失败的节点上接线每节点错误输出 |
| **API_WORKFLOWS.md** | 构建/审查 webhook → Respond 工作流，包括输入校验（IF 条件、按字段 Code 校验器） |
| **RESPONSE_SHAPES.md** | 定义响应体约定、状态码以及什么不能泄漏 |
| **ERROR_WORKFLOWS.md** | 为无人值守工作流搭建工作流级兜底 |

---

## 与其他 Skill 的集成

- **n8n-workflow-patterns** ， webhook/API 与定时模式是错误处理的栖身之处。用它定整体形态；用本 Skill 加固它。
- **n8n-node-configuration** ， `onError`/`retryOnFail` 属于节点配置；NODE_FAMILY_GOTCHAS.md 深入讲解 Webhook/Respond 的响应码陷阱。
- **n8n-validation-expert** ， 半接线的错误输出（两步缺一）是连接/配置审计项，不是校验错误。本 Skill 就是修法。
- **n8n-expression-syntax** ， 基于 `$json.error.message` 的 Switch 条件和告警消息表达式依赖正确的 `{{ }}` 语法和 `$json.error` 访问。
- **n8n-code-javascript / n8n-code-python** ， 如果你在 Code 节点*内部*捕获错误，要有意识地决策：重新抛出以走错误输出，或处理并继续。不要返回错误形状的数据还假装成功。
- **n8n-code-tool** ， agent 的 Code Tool 会把抛出的错误回传给 LLM，由 LLM 重试；那是与工作流节点不同的错误契约。
- **n8n-binary-and-data** ， 文件/二进制操作同样会失败；像任何网络节点一样接好它们的错误输出。

---

## 速查清单

对一个 **API / webhook** 工作流：

- [ ] Webhook 触发器使用 `responseMode: "responseNode"`
- [ ] 输入在上游校验 → 4xx Respond（IF 条件，或按字段 Code 校验器）
- [ ] 每个可能失败的节点都有 `onError: "continueErrorOutput"` **且** `main[1]` 已接线
- [ ] 网络节点已配置 `retryOnFail: true, maxTries: 3, waitBetweenTries: 5000`
- [ ] 错误路径终结于一个带**显式** 4xx/5xx `options.responseCode` 的 Respond（顶层 `responseCode` 会被忽略）
- [ ] 状态码与原因匹配（4xx 调用方，5xx 你）
- [ ] 错误响应体为 `{ error, message }` ， 没有堆栈、SQL 或 token
- [ ] 已用 `n8n_get_workflow` 验证：每个可能失败的节点上 `onError` 与 `main[1]` 都在

对一个**无人值守**（定时/cron/队列）工作流：

- [ ] 网络节点已配置 `retryOnFail`
- [ ] 存在一个 Error Trigger 工作流（捕获 → 通知，可选重试）
- [ ] 错误工作流用不同渠道通知 + 有兜底（递归陷阱）
- [ ] 错误工作流设置已在 n8n UI 中指派（MCP 做不到，提醒用户）

---

**记住**：默认是沉默。错误处理就是两个动作，让失败*可路由*（每节点 `onError` + 接好线的输出，或一个兜底错误工作流），并让它*开口说话*（一个讲真话的状态码和响应体）。只做半个动作比不做更糟，因为它看起来像是做完了。
