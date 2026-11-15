> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-agents/HUMAN_REVIEW.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Agent 工具的人工审核

人工审核把一个工具置于"必须先有明确的人工批准"之后。在人工批准之前，被包装的工具不会运行，无论 Agent 多么自信。这是任何带用户可见副作用的 Agent 工具的默认安全模式。

n8n 在节点 ID 里称之为 **HITL** / human-in-the-loop（`slackHitlTool`、`discordHitlTool` 等），在 UI 里称为"Human Review"。同一个概念。

**在添加或跳过审核之前，先问用户。** 是否需要签核是产品/政策层面的决定（影响范围、审计要求、对模型的信任程度）。把问题摆出来，依据下面的标准给出建议，由他们决定。

---

## 拓扑

审核节点通过 `ai_tool` 连接，位于被包装工具与 Agent **之间**：

```
[wrapped tool]  --ai_tool-->  [review node]  --ai_tool-->  [Agent]
```

- **Agent 不知道审核节点的存在。** 它通过被包装工具自身的名称、描述和参数 schema 看到该工具。审核节点只是执行路径上一个透明的拦截器。
- 当 Agent 调用被包装工具时，审核节点会拦截：收集 Agent 构造好的参数，暂停，向人发送审批提示，只有在批准之后，被包装工具才带着这些参数运行。

在工作流 JSON 中，被包装工具的 `ai_tool` 输出指向**审核节点**，审核节点的 `ai_tool` 输出指向 **Agent**：

```json
"Refund customer": {
  "ai_tool": [[{ "node": "Slack approval", "type": "ai_tool", "index": 0 }]]
},
"Slack approval": {
  "ai_tool": [[{ "node": "AI Agent", "type": "ai_tool", "index": 0 }]]
}
```

不要把被包装工具接进 Agent 的 `main` 输入——那样 `validate_workflow` 会把被包装工具标成断连节点。被包装工具到审核节点的连线只能走 `ai_tool`。

---

## 告诉 Agent 审核环节的存在

由于 Agent 看不到审核节点，它不知道自己的工具被加了闸门。带安全先验的模型面对看起来有破坏性的工具（发送、删除、退款、扣款）会畏缩：拒绝执行、先向用户求确认，或者挑一条更绕的路径。审核环节再包一层，这种谨慎就叠加了，模型自我克制加上人工审核，有时模型根本走不到审核那一步。

如果你看到 Agent 对某个被包装工具过度畏缩，就在**被包装工具的描述**里加一句说明（遵循 **SYSTEM_PROMPT.md** 中的模块化提示词原则）：

> 该工具由人工审核环节把关。相关时尽管使用。发送任何内容之前，会有真人看到确切参数并批准。不要先向用户求确认。

不要预先给每个被包装工具都加上这句话：很多 Agent 没有它也能正常用工具。等症状真的出现（畏缩、拒绝、自己劝自己别试）再部署。

---

## 何时默认采用 / 推荐人工审核

- **发送、支付、退款、账户变更**：任何用户可见且难以回滚的操作。
- **审批者与聊天者不是同一人**：客户触发工作流，客服人员批准退款。客户永远看不到审批环节。
- **非聊天触发器**：收到订单、提交表单、定时触发。操作是代表某人执行的，运行前需要真人批准。
- **生产环境的 Agent 工具**：错误调用的代价（金钱、信任、声誉）超过一步延迟的代价。

工具只读、幂等且撤销成本低，或者部署是内部/探索性质且服务为 mock（测试替身）时，可以跳过审核。

---

## 可用的审核工具节点

| 节点 | 适用场景 |
|---|---|
| `n8n-nodes-base.slackHitlTool` | 审批者在 Slack 上（最常见的多渠道场景） |
| `n8n-nodes-base.discordHitlTool` | 审批者在 Discord 上 |
| `n8n-nodes-base.telegramHitlTool` | 审批者在 Telegram 上 |
| `n8n-nodes-base.gmailHitlTool` | 通过 Gmail 审批 |
| `n8n-nodes-base.emailSendHitlTool` | 通过通用 SMTP 邮件审批 |
| `n8n-nodes-base.googleChatHitlTool` | 在 Google Chat 中审批 |
| `n8n-nodes-base.microsoftOutlookHitlTool` | 通过 Outlook 审批 |

平台会陆续增加，请用 `search_nodes({ query: 'hitl' })` 核实。

---

## 响应类型

`responseType` 决定人看到的响应形式：

- **`approval`**：按钮式，通过 `approvalOptions.values.approvalType` 做子配置：
  - `'single'`（默认）：一个 Approve 按钮。审批者执行或忽略。
  - `'double'`：Approve / Disapprove。适用于"不批准"需要成为一个响亮且可留痕的选择的操作。
- **`freeText`**：人手输自由格式的回复。适用于 Agent 真的在提问、任何回答都有效的情况。
- **`customForm`**：多字段表单（文本、下拉、单选、复选、文件）。**这是"可编辑参数"的实际解法**：定义一个字段与被包装工具参数对应的表单，人就能覆盖 Agent 选的值。

双按钮的"语义选择"（"今天排期" / "明天排期"）不是独立类型，用 `approval` 加 `approvalType: 'double'`，再自定义 `approveLabel` / `disapproveLabel` 即可。

---

## 等待超时

`options.limitWaitTime`（秒）限制工作流暂停多久后报错退出。默认 45 分钟。**生产工作流要显式设置它**，否则审批者不动作时，暂停的执行会无限期挂着，队列越积越多。

---

## 审批消息内容：展示真实参数

参数由模型选定；人批准的是字面意义上的这次调用。通过 `{{ $tool.parameters.<name> }}` 引用真实值：

```
The agent wants to refund {{ $tool.parameters.amount }} to {{ $tool.parameters.customerId }}.
Reason: {{ $tool.parameters.reason }}.
```

`$tool.name` 是被包装工具的显示名称；`$tool.parameters` 是 Agent 构造的完整对象。为避免新增参数悄悄漏出消息，遍历全部参数：

```
The agent wants to call {{ $tool.name }}:
{{
  $tool.parameters.keys()
    .map(param => `${param}: ${$tool.parameters[param]}\n`)
    .join('')
}}
```

### 绝不用 `$fromAI()` 填充审批消息

`$fromAI()` 让*模型*生成一个值，如果放任不管，连审批文本本身也会由模型生成。这样人批准的就是模型转述的描述，而不是即将发送的字面参数。这完全背离了审核的目的。

```
// ❌ WRONG — the model paraphrases what it's about to do
message: ={{ $fromAI('approvalText', 'describe the action for approval') }}

// ✅ RIGHT — the literal call is visible
message: =Refund {{ $tool.parameters.amount }} to {{ $tool.parameters.customerId }}?
```

### 把值放进按钮标签

```json
"approvalOptions": {
  "values": {
    "approvalType": "double",
    "approveLabel": "=Approve {{ $tool.parameters.amount }} refund",
    "disapproveLabel": "Cancel"
  }
}
```

写着"Approve $50 refund"的按钮含义明确；单独一个"Approve"则不然。`slackHitlTool` 还提供 `buttonApprovalStyle` / `buttonDisapprovalStyle`（`'primary' | 'secondary'`）用于视觉强调。

---

## 多渠道模式：审批者与聊天者不是同一人

常见的生产形态：客户在网站上与 Agent 聊天（或通过邮件/订单/表单），客服人员在 Slack 中批准敏感操作。

```
[customer chat / order trigger]
   → [Agent]
       → [Slack review tool]  →  [refund / cancel / escalate tool]
```

客户永远看不到 Slack 频道。Slack 审核消息通过 `slackHitlTool.parameters.user`（资源定位器）路由。批准后，被包装工具触发，Agent 的响应沿原路径返回给客户。这套模式完全不需要聊天也能工作——触发器可以是 webhook、定时、表单或队列，审核工具是唯一面向人的界面。

---

## 可编辑参数：使用 customForm

对于"批准，但改成 40 而不是 50"这类工作流，使用 `responseType: 'customForm'`。人填写多字段表单，其值喂给被包装工具。不要试图在 `approval` 类型上堆出可编辑审批，表单模式才是受支持的路径。

> 注意：有反馈称表单模式的体验像是绕路。有时更好的 UX 是让用户拒绝，然后在聊天里说出修改内容。

---

## UI 怪癖：测试数据自动填充

构建审核工具时，在画布测试执行里点一次"Approve"。n8n 会自动填充测试数据，之后的运行无需手动输入。新手常以为工具坏了，因为 `$tool.parameters.<name>` 显示红色，那只是缺测试数据。

---

## 反模式

| 反模式 | 会出什么问题 | 修法 |
|---|---|---|
| 未经审核就变更用户可见状态的工具 | Agent 基于错误推断触发不可逆操作 | 用合适的审核工具节点包一层 |
| 审批消息经由 `$fromAI()` 生成 | 你批准的是转述，不是字面调用 | 使用 `$tool.parameters.<name>` |
| 没有上下文的"Approve"按钮 | 审批者没看到自己在批准什么就点了 | 把真实值嵌进标签 |
| 审核发在审批者不看的渠道 | 工具无限期挂着，执行堆积 | 选一个有人看的渠道；设置 `limitWaitTime` 加兜底 |
| 被包装工具接进 Agent 的 `main` 输入 | 校验时被标记为断连节点 | 只通过 `ai_tool` 连接：被包装工具 → 审核 → Agent |
