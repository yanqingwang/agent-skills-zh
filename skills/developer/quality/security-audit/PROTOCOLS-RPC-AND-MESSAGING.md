> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/PROTOCOLS-RPC-AND-MESSAGING.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 协议、RPC 与消息机制排查

#### 何时使用本文件

当目标使用 gRPC、GraphQL 传输层、Cap'n Proto、Thrift、Protobuf、自定义二进制协议、流式 RPC、webhook、消息代理、队列、发布/订阅或事件总线时，使用本文件。本文件涵盖对端身份、消息的逻辑解读、路由、重放、排序与投递语义。解析器的内存安全问题用 `MEMORY-SAFETY-AND-BINARY.md`，HTTP 帧格式用 `WEB-PROTOCOL-AND-AUTH.md`，可用性影响用 `RESOURCE-EXHAUSTION-AND-AVAILABILITY.md`。

拆分大型系统时按以下维度：生产者/消费者对、外部/内部对端角色、同步 RPC、流式，以及异步消息路径。

## 核心纪律（加入本领域每个 Agent 的提示词中）

```
- "Internal" is not authentication. Name the peer identity at every hop and show how it becomes the application principal used for authorization.
- Schema validation proves message shape, not provenance, resource authority, ordering, or safe values. Follow decoded fields to policy and side effects.
- Broker guarantees and application guarantees differ. Write down retry, ordering, acknowledgement, deduplication, and transaction behavior before evaluating state changes.
- Parser disagreement requires two concrete consumers, schema versions, or wire representations and one security-relevant divergent value.
- Use `confirmed` for source-complete paths plus bounded local producer/consumer tests. Use `needs_validation` for broker ACL, service-mesh identity, topic attachment, or compatibility behavior outside the repository.
```

## 帧、Schema 与解读攻击类别（subagent_type: `general`）

**消息边界与规范化分歧**
各组件在长度、压缩、重复字段、未知字段、编码、数值宽度、规范化或信封/正文优先级上不一致。比较生成的解析器与手写解析器、网关、语言绑定和版本转换器。确认解码之后哪个主体（principal）、资源或操作发生了差异。

**联合类型、枚举与默认值混淆**
未知变体、缺失的判别字段、零值、默认权限或兼容性映射，流入假定"已验证分支"的代码。审查穷举分发、默认分支，以及旧消费者如何解读新添加的字段。

**信封与载荷身份不一致**
授权依据的是看起来可信的路由或信封元数据，而处理逻辑实际作用于正文中与之冲突的租户、账户、主体、对象或发送者。确定哪个来源是权威的，并确保客户端无法覆盖它。

## RPC 身份与授权攻击类别（subagent_type: `general`）

**拦截器与方法路径不一致**
认证/授权拦截器只覆盖一元方法，却不覆盖流、反射、健康检查、网关转码路径、兼容性服务或单条流消息。把每一处注册和路由与同一操作逐一比对。

**对端身份与应用主体混淆**
mTLS、工作负载身份、bearer 元数据、转发身份或代理凭证只认证了一条信道，但用户或租户却由调用方可控的字段选定。信道身份与所声称的主体必须由确定性策略绑定。

**逐条与流式授权缺口**
一条流、订阅、批处理或批量消息只授权一次，后续条目却指向不同资源，或在角色、成员资格或令牌被撤销后继续执行。重新检查范围可能在何处变化，并把订阅绑定到其原始主体。

**回调与应答关联混淆**
可预测、复用或跨租户的关联 ID，会让某个响应、webhook、取消或确认去满足另一个调用方的未决操作。把每个未完成请求绑定到已认证的对端、租户、操作和生命周期。

## 代理与队列隔离攻击类别（subagent_type: `general`）

**主题、路由键与订阅范围缺口**
发布者或订阅者可以选中另一个租户的主题、通配符、消费者组、分区、应答队列或死信路由。在可见之处检查由代理强制执行的 ACL，以及应用侧的命名空间构造。载荷内部的租户文本不是隔离。

**死信、重试与诊断信息泄露**
被路由到死信队列、错误主题、追踪或运维视图的消息，可能包含低信任消费者可访问的机密或跨租户载荷。审查失败路径上的策略与脱敏处理，而不只是正常投递路径。

**不可信生产者被当作控制面**
消息体可以自我声明为管理员事件、提供商回调、复制记录或迁移指令，而无需经过独立认证的生产者和事件类型。在特权处理之前验证签名以及来源/账户/受众绑定。

## 重放、排序与事务攻击类别（subagent_type: `general`）

**重复投递与幂等缺口**
重试或重新投递重复了某个副作用，原因是去重缺失、发生在变更之后，或使用的键在租户或操作之间冲突。确认代理的投递模型，以及那个并非天然幂等的副作用。

**乱序与过期消息被接受**
旧状态、已撤销的成员资格、已取消的工作，或二次认证（step-up）之前颁发的授权，在新状态之后到达并将其覆盖。审查序号/版本检查、墓碑记录、分区变更以及恢复/重放工作流。

**确认/提交顺序缺陷**
确认发生在持久化提交之前，导致安全相关的工作丢失；或者提交发生在不可靠的确认之前，导致变更重复。评估事务性 outbox/inbox 行为与失败恢复。

**多消费者部分完成的状态迁移**
多个消费者共同实现一个授权或业务状态迁移，但重试与部分失败导致只有一部分被提交。找出必须原子性持久化的不变量，或用当前授权进行补偿。

## 通用动作（适用于以上各类）

- 为每个消息家族画出 生产者 → 代理/传输 → 网关 → 消费者 → 存储。在每个跳点记录已认证的对端、权威的租户/资源字段、验证与副作用。
- 把同一份小型 fixture 喂给仓库内每个 schema 版本或语言绑定。测试重复、缺失、未知、边界、重放和乱序消息，且不产生负载。
- 对比正常、重试、死信、重放、迁移、反射、流式与网关转码等路由。安全策略必须在传输方式变化后依然成立。

## 验证规则（报告本文件任何发现之前必须执行）

1. 指明真实可信的生产者或对端、被接受的消息、已认证的信道身份、受影响的主体/资源，以及未授权的变更或泄露。
2. 提出"解读不一致"类主张时，引用双方解析器/消费者以及产生分歧的解码值。任何一方安全地拒绝该输入，结论就无法确认。
3. 提出"重放/排序"类主张时，先确立实际投递保证，并用有界的本地/内存传输复现不变量被破坏的过程。
4. 授权与隔离类：验证源码中可见的所有拦截器、代理 ACL、网关与消费者层。存在外部附加配置时，候选发现记为 `needs_validation`。
5. 只有掌握完整消息生命周期并观察到有意义的结果才返回 `confirmed`；返回 `needs_validation` 时附上所需的确切代理、服务身份、路由或投递事实。
