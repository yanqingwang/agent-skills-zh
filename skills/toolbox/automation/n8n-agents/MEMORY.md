> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-agents/MEMORY.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Agent 记忆

记忆是 Agent 上的一个子节点，通过 `ai_memory` 接线。没有它，每次调用都是无状态的。有了它，Agent 能跨轮次、（取决于类型）跨执行地维持一段对话，以你绑定到 `sessionKey` 的任何表达式为键。

记忆节点的可用性随 n8n 版本变动，用 `search_nodes({ query: 'memory' })` 确认装了什么。

---

## 两条没有商量余地的原则

1. **把稳定的键贯通下去。** 记忆按你绑定到 `sessionKey` 的值分桶。Chat Trigger 会自动填 `sessionId`。其他触发器要自己派生稳定标识（Slack `thread_ts`、webhook 会话 ID、生成的 UUID、多租户组合键），并转发给记忆和任何按会话取键的工具。同一会话内不一致，记忆就永远对不上。
2. **默认用 `memoryBufferWindow`。** 它经 n8n 内部存储跨执行持久化，以 `sessionKey` 为键，对几乎所有聊天 Agent 都是正确选择。只有记忆要在 Agent **之外**被读取时才上 Postgres/Redis。

---

## 记忆类型

### `memoryBufferWindow`（默认）

上下文内记忆最近 N 轮对话，经 n8n 存储跨执行持久化。

```json
{
  "parameters": {
    "sessionIdType": "customKey",
    "sessionKey": "={{ $json.sessionId }}",
    "contextWindowLength": 50
  },
  "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
  "typeVersion": 1.3,
  "name": "Simple Memory"
}
```

`contextWindowLength` 是保留的对话轮数。**默认值是 5，对现代聊天预期来说非常低**，用户默认对话近乎无限延续。**50 是合理的起点。** 越高 = 上下文越多，但每轮 token 越多。

**窗口外的消息被整体移除。** 缓冲一满，最老的轮次被丢弃，Agent 无法回忆、搜索，甚至不知道它们存在过。用户 60 轮前说过的话，窗口是 50 时，从 Agent 视角已经不存在。要回忆窗口之外的内容，调高 `contextWindowLength`，或把关键事实持久化到 Data Table，读取后注入系统提示词。

"窗口"只是上下文中保留多少消息的滑动上限，**不是**持久化的作用范围。用 `sessionIdType: 'customKey'` 可以把键绑定到任何表达式（`{{ $json.sessionId }}`、Slack `thread_ts`、多租户组合键）。每个用户/会话线程/上下文有自己的桶。

### `memoryPostgresChat` / `memoryRedisChat`

只在记忆需要在 Agent **之外**被查询或读取时用它们：在自己的 UI 里展示对话历史、对过往聊天做分析、跨系统共享记忆、或干净地迁移实例。

```json
{
  "parameters": {
    "sessionIdType": "customKey",
    "sessionKey": "={{ $json.sessionId }}"
  },
  "type": "@n8n/n8n-nodes-langchain.memoryPostgresChat",
  "typeVersion": 1.3,
  "name": "Postgres Memory"
}
```

**默认聊天场景用它们是错的**：`memoryBufferWindow` 已经能跨执行存活，而且是更干净的选择。

---

## 自定义模式（Chat Memory Manager）

多数 Agent 用不上。但当固定窗口不够时，`@n8n/n8n-nodes-langchain.memoryManager` 节点可对任何已接线的记忆后端操作，暴露三种模式：

- **`load`**（默认）：把当前记忆读进工作流（用于检查、按大小分支、喂给摘要器）。
- **`insert`**：追加一条消息。可选的 `hideFromUI` 标志覆盖那些要影响 Agent 但不该出现在聊天 UI 里的消息。
- **`delete`**：删除部分或全部消息。

### 模式：滚动摘要

对话拉长后，想留住旧轮次的大意而不是丢弃它们：

1. 每轮之后 `load` 缓冲。
2. 接近上限时路由到摘要器（否则不做任何事）。
3. 用 LLM 摘要较老的轮次。
4. `delete` 缓冲。
5. `insert` 摘要为一条消息，外加最近几轮以保持连贯。

Agent 现在看到 `[summary of turns 1-40] + [recent 5 turns]`，输入 token 大幅减少，长历史上下文还在。

其他模式同理组装：**按相关性修剪**（`load` → 过滤 → `delete` → `insert` 留下的）、**注入运行时事实**（`insert` 加 `hideFromUI: true`）、**按命令重置**（收到 `/clear` 就 `delete` 全部）。

Memory Manager 节点比 n8n 其余记忆工具更新，在生产中依赖之前，先对照你装的版本核实这些模式。

---

## 各触发器的 session ID 处理

### Chat Trigger
自动填 `sessionId`。处处一致地接线：
- 记忆：`sessionKey: ={{ $('Chat Trigger').first().json.sessionId }}`
- 工具：`sessionId: ={{ $('Chat Trigger').first().json.sessionId }}`（**不要**经由 `$fromAI`）
- 存储取键：从 `sessionId` 派生存储桶键/文件名，便于按会话做简单清理。

### Webhook 触发器
由你管理：调用方传一个 header 或 body 字段（`body.sessionId`）由你转发，或者你首次调用时发放一个并要求带回来。无论哪种，整个会话期间（包括重连）必须一致。

### 手动 / 定时
通常没有会话。存在稳定的"对话"标识（工单 ID、线程 ID）就用它；否则记忆没有意义，直接省略。

---

## 记忆与工具

工具被调用时，工具的子工作流**看不到**对话记忆——记忆是 Agent 的上下文，不是工具的输入。需要什么上下文就通过 `$fromAI` 参数显式传。对按会话取键的状态，把 `sessionId` 贯通下去，让工具从 Data Table 或按会话取键的存储里查状态。

---

## 记忆与二进制

记忆存的是**文本轮次**。会话中上传的二进制不在记忆里，它只在那一轮的 Chat Trigger `files[]` 里。文本记忆只会记下"用户提到上传了文件"，但要在之后的工具调用里真正用上那个文件，它必须还在存储里，且它的键必须出现在**那一轮**的系统提示词里。实践中，每一轮都把该会话的文件清单注入系统提示词（按 `sessionId` 加载）。→ **n8n-binary-and-data**。

---

## 常见错误

- **写死 `sessionId: 'default'`**，所有对话共用一个桶，记忆失去意义。
- **记忆与工具的 `sessionId` 不一致**，记忆看着正常，工具却找不到关联状态。
- **聊天用无界的 `memoryBuffer`**，token 开销一路涨到超时。用有合理上限的 BufferWindow。
- **没有会话的地方加记忆**，"总结这篇文章"的工作流用不上。
- **指望工具看到记忆**，它们只看到自己的 `$fromAI` 参数和贯通下来的上下文。
- **表层与记忆漂移**，只要有什么绕过 Agent 发进了对话（定时回复、人工直接发言），Agent 就在不完整的视图上运转，并会与它看不见的消息相互矛盾。用户可见表层上出现的任何内容，也必须 `insert` 进记忆。

---

## 运维注意

- **记忆大小驱动 token 成本。** 200 token 一条消息的 15 轮缓冲，在用户开口之前每轮就是 3000 token 输入。提前规划。
- **限流。** 模型撞上限流会在对话中途失败；在那之前记忆都攒着，下一轮接着来（前提是 session ID 连续）。
- **并发会话。** 持久后端按 `sessionId` 取键，并发对话互不干扰。用两个同时进行的测试验证。

---

## 交叉引用

- Agent 的定位 → 父级 **SKILL.md**
- 把按会话取键的状态传进工具 → **SUBWORKFLOW_AS_TOOL.md**
- 聊天界面上的线程即会话 → **CHAT_AGENT_PATTERNS.md**
- 按会话取键的文件存储 → **n8n-binary-and-data**
