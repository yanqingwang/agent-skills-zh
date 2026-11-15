> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/AI-AND-LLM.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# AI、LLM 与 Agent 审查

#### 何时使用本文件

当语言模型参与信任敏感决策时使用本文件：聊天机器人与助手、RAG 管道、持久化 agent 记忆、agent/工具调用循环、MCP 服务器与客户端、从不可信输入构建提示词的代码，或消费模型输出并据此行动的代码。关键数据流是*不可信内容 → 模型或记忆 → 能力、权限或汇点（sink）*。

与 `ATTACK-CLASSES.md` 配合使用，而不是替代它。传输、访问控制、查询构建、文件系统使用和输出渲染仍是普通的信任边界。本文件覆盖模型特有的委托层。按检索、记忆、工具派发、MCP 和输出处理拆分大型目标。

## 核心纪律（加入本领域的每个 agent 提示词）

```
- Prompt injection alone is not a finding. Require a code-level boundary failure: content reaches another principal's context, invokes authority the requester lacks, discloses data they cannot read, or drives a sink they cannot reach directly.
- Model output, memory, tool descriptions, and MCP responses are untrusted inputs. Point to the code that grants authority, trusts output, writes durable state, or feeds a sink.
- A guardrail prompt is not a security boundary. Count only deterministic checks, resource-scoped authorization, isolation, binding, and constrained credentials.
- State the attacker, affected principal, effective execution identity, resource, exact action, authority used, and observable impact. An intentional direct request to use the requester's existing authority is not a delegation defect merely because a model executes it.
- Authorization and action binding are separate controls. Attacker-controlled content that causes an action under an affected principal's valid authority is an action-binding failure when that principal did not intentionally request or approve the exact action.
- Classify every candidate as `confirmed` only after source evidence and bounded local validation establish the boundary and result. Use `needs_validation` when a required provider, deployment, model, renderer, or identity behavior is not observable locally.
```

## 上下文、检索与记忆攻击类别（subagent_type: `general`）

**通过检索或摄取内容的间接注入**
攻击者可以写入一个进入另一个主体模型上下文的 RAG 文档、被索引页面、文件、邮件、issue 正文、工具响应或元数据。追踪谁可以写每个来源、检索如何限定它、哪个 session 消费它、以及在那里启用了什么能力。隔离、资源授权、与消费主体意图的绑定要分开检查。缺陷是缺失的确定性控件，而不是有说服力的文本本身。

**跨 session 或跨租户上下文渗漏**
会话历史、embedding、检索结果或提示词缓存的键过宽。在查询本身和每个缓存键里验证租户与 ACL 过滤。对象上存了租户字段不等于强制，如果另一条查询、共享缓存或批处理路径省略了它。

**持久记忆投毒**
攻击者可控的内容或模型摘要被写进记忆，后来塑造另一个任务、用户或特权 session。审查谁可以创建、更新、合并、删除记忆；它的来源和租户范围；低信任观测是否会变成持久的指令或事实；以及检索是否区分用户偏好与工具策略。用户有意保存、且只用于该用户有意允许的请求的记忆，不是跨边界发现。

**提示词角色与来源混淆**
提示词组装让不可信文本冒充系统消息、先前轮次、工具结果、策略或记忆记录。寻找字符串拼接、无类型历史、调用者可控的角色字段，以及丢失来源标签的序列化往返。确认伪造的来源改变了一个确定性的信任决策，或到达了有意义的能力。

## 工具与动作攻击类别（subagent_type: `general`）

**工具参数注入到下游汇点**
模型生成的参数在没有 handler 侧验证的情况下到达 SQL、shell、文件、URL 抓取或特权 API。把工具 schema 当作输入解析，然后跟随每个字段从解码后的调用到汇点。结构化输出收窄了形状；它不建立授权、安全路径、安全 URL 或查询语义。

**过度代理与糊涂代理人（confused deputy）权限**
agent 使用服务身份或宽泛凭证，而工具 handler 不在指名资源上重新检查请求主体的权限。同时验证生效身份，以及调用者能否通过正常产品界面执行那个精确操作。带强制按用户查询范围的共享凭证不是缺陷。

**动作确认与审批绑定**
用户批准了一个所描述的动作，但执行可以用被改过的参数、不同的资源、不同的主体或更晚的模型轮次。攻击者可控内容在受害者有效权限下引发副作用、而受害者没有有意请求或批准时，同样存在动作绑定缺陷，即使通用授权允许受害者执行它。审查意图或确认是否绑定了规范化工具名、完整参数对象、请求者、目标、金额、有效期和批次归属。检查重试与恢复的 session：一次审批不得授权被篡改或重复的副作用。

**工具 schema 与派发器不一致**
schema 接受别名、额外字段、重复键、类型强转、嵌套自由对象或超出范围的值，而派发器或 handler 对它们的解释不同。对比 schema 校验、规范化、生成的绑定和 handler 默认值。在值变成资源选择器或安全相关选项的地方再验证一次。

**无界的委托动作循环**
一个有界的请求可以在没有按请求预算、按动作授权、取消或幂等控制的情况下反复排队消费、发送、修改或外部 API 工作。确认对共享成本、配额、其他用户或持久状态的影响。不要用耗尽服务来测试；用代码级记账和本地有界循环。

## MCP 与子代理信任类别（subagent_type: `general`）

**子代理与 MCP 信任继承**
被委托的任务拿到了完整 session、凭证、记忆或能力，而不是所需的最小权限。检查每次调用携带的主体和租户、能力收窄、凭证受众，以及委托结果返回时是否被当作不可信数据对待。

**MCP 服务器与工具身份混淆**
调用或结果按可被攻击者影响的服务器名、工具名、请求 ID、资源 URI 或模型选择的别名路由，而不是按已认证连接和未决请求。检查两个服务器能否声明同一工具或资源身份、重连是否改变绑定、以及一个服务器的响应能否满足另一个服务器未决的调用。

**MCP 元数据与 schema 被当作策略**
MCP 对端提供的工具描述、资源元数据、提示词、补全提示或 schema 被当作策略或授权信任。这些字段可以引导模型，但不能授予能力。找到当元数据冲突时仍然权威的确定性 allowlist、服务器身份检查和 handler 授权。

## 输出与泄露攻击类别（subagent_type: `general`）

**不安全的输出渲染**
模型输出到达执行 HTML、Markdown、模板、URL 或命令汇点，而缺少该汇点要求的编码和策略。浏览器渲染时，在 `CLIENT-SIDE.md` 中验证自动加载的资源与 CSP 或净化；仓库之外的渲染器行为使候选为 `needs_validation`。

**敏感上下文提取**
组装的上下文包含凭证、另一个用户的数据、私有源码或本身授予访问的策略值，而受用户影响的输出暴露了它们。阅读提示词组装和数据获取代码。泄露不跨越数据边界的通用指令或行为不是发现。

## 通用手法（适用于以上所有类别）

- 先画四张图：每个执行身份、每项能力、每个可写的上下文或记忆来源、每个输出目的地。然后把起点的主体的线连到终点的权限。
- 从有副作用的工具出发，反向穿过派发器、schema、确认、模型上下文、检索和摄取。从持久记忆读取出发，追踪每一个写入者。
- 对同一动作对比直接、排队、重试、恢复、批处理和委托路径。最强的门必须在参数定稿之后、每个副作用之前生效。

## 验证规则（报告本文件任何发现之前先执行）

1. 点名被跨越的边界和可观测结果：攻击者、受影响的主体或共享资源、执行身份、目标，以及未授权或未请求的动作或泄露。
2. 对糊涂代理人权限主张，证明工具缺少请求者加资源的授权，且攻击者无法正常执行同一动作。对动作绑定主张，改为证明攻击者可控内容在受影响主体的权限下引发了主体没有有意请求或批准的动作。有效的通用授权不能确立意图。
3. 对记忆或检索主张，同时引用攻击者可控的写入和后来的跨主体读取或特权决策。没有可达消费者的共享记录不够。
4. 对动作绑定，确立（如果有的话）有意的请求或规范化批准对象，并与 handler 使用的对象比较。确认一个本地可观测的未请求动作、修改、重复或权限变化，测试不要延伸到有害执行。对 schema 不一致，比较规范化后的已验证对象与 handler 的对象。
5. 对 MCP 身份主张，验证已认证连接、请求关联、工具 namespace 和生效凭证。需要外部服务器身份或部署路由时标记 `needs_validation`。
6. `confirmed` 发现必须有完整的源码轨迹和有意义的结果。`needs_validation` 要给出具体未决的边界事实，并说明解决它所需的受限本地检查或所有者观测检查。
