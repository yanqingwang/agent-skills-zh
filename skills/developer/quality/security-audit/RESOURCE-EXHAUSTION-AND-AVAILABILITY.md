> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/RESOURCE-EXHAUSTION-AND-AVAILABILITY.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 资源耗尽与可用性排查

#### 何时使用本文件

当不可信的请求、消息、文件、租户状态或 Agent 工作可能消耗 CPU、内存、磁盘、连接、worker 槽位、付费 API 或队列容量，或可能导致共享服务死锁/崩溃时，使用本文件。本领域区分"源码可审的可用性漏洞"与"一般性能问题"。绝不通过压测共享或线上服务来验证。

内存完整性缺陷用 `MEMORY-SAFETY-AND-BINARY.md`，代理投递逻辑用 `PROTOCOLS-RPC-AND-MESSAGING.md`。只要可达的致命错误影响共享服务，即使底层解析器已在其他文件覆盖，也归入本文件。

## 核心纪律（加入本领域每个 Agent 的提示词中）

```
- Require an input-to-cost path, a missing effective bound, and impact on another user, shared service, safety function, or operator-owned spend. Self-limiting work in the requester's own process is not a service vulnerability.
- A missing rate limit is not enough. Check body/message/file caps, concurrency, queues, deadlines, database constraints, upstream gateways, and per-tenant quotas before calling a path unbounded.
- Do not run stress, saturation, or production tests. Use asymptotic analysis, small boundary fixtures, mocked paid calls, strict local resource limits, and deterministic cancellation tests.
- State attacker cost, service work, persistence, scope, and recovery. One bounded input with superlinear or persistent shared effect is materially different from sustained volume.
- Use `confirmed` for source-visible bounds failures demonstrated safely. Use `needs_validation` when upstream caps, deployed topology, autoscaling, paid quota, or recovery behavior is outside the repository.
```

## 计算放大攻击类别（subagent_type: `general`）

**超线性解析、匹配或求值**
很小的合法输入触发灾难性的正则回溯、嵌套解析、递归验证、符号求值、图遍历、模板展开或对抗性排序/哈希行为。推导可接受的深度/基数与复杂度，然后在本地演示一条有界的增长曲线。

**解压与表示放大**
压缩、稀疏、嵌套、别名引用或编码后的输入，膨胀后远超已检查的传输或文件大小。在每次展开之后、解析器各阶段之间都验证限制，覆盖压缩包、图片、字体、结构化文档和协议压缩表。

**数据库与下游查询放大**
一个小请求引发大范围扫描、病态连接、扇出、无界排序/聚合或大量下游调用，因为查询深度、过滤基数、分页或展开字段没有边界。确认授权并非有意允许同样的资源范围。

## 资源累积攻击类别（subagent_type: `general`）

**无界缓冲与基数**
请求体、乱序流、上传、会话、唯一缓存键、指标标签、日志字段、订阅或待处理任务不断累积，缺少逐条和总量限制。找出断连、超时、取消和部分解析场景下的清理与过期机制。

**文件描述符、句柄与临时资源泄漏**
畸形或被取消的工作错过清理，遗留套接字、文件、数据库游标、定时器、子进程、临时文件或对象引用。通过有界的本地迭代确认泄漏会重复出现，并影响共享池。

**取消后的脱管工作**
客户端超时、断连、取消的任务或失败的授权把控制权交还，但数据库、模型、网络或 worker 中的工作仍在运行。逐层追踪取消与截止时间的传播。

## 配额与调度攻击类别（subagent_type: `general`）

**认证前的工作量失衡**
昂贵的解析、密钥查找、密码学运算、解压或外部请求发生在认证与最早的大小/速率闸门之前。比较请求者最小成本与共享服务成本，并检查上游限制。

**配额计量的范围与重置缺口**
计量使用攻击者可影响的 IP、路由、租户、键前缀、任务 ID 或其他维度，使某个主体的工作逃出其应有的预算，或消耗另一个主体的配额。审查整数溢出、分布式竞态、重试、重连与账户切换。

**worker、池与优先级饥饿**
低优先级或攻击者控制的任务占用无关用户所需的共享锁、worker、数据库池、事件循环轮次或调度优先级。要求存在绕过队列/并发公平性或在截止时间之后仍占用槽位的路径。

## 失败与恢复攻击类别（subagent_type: `general`）

**可达的致命错误或死锁**
不可信输入在共享进程中触达 `panic`、abort、致命断言、未处理异常、进程退出、锁环或无限循环。确认 supervisor 的作用范围，以及是不可用的只是一个 worker 还是整个服务。重启隔离的 worker 可以减小影响，但不能抹掉缺陷。

**重试风暴与 fail-open 放大**
超时、依赖错误、部分处理的消息或健康检查失败，触发同步或无界的重试，缺少抖动、上限、熔断或去重。验证一个有界的失败来源就能产生持续的聚合工作量。

**毒记录与队头阻塞**
一条畸形记录或消息在共享队列、分区、启动扫描、迁移或恢复循环的头部反复失败。审查跳过/隔离策略、偏移量，以及其他租户是否共享这个被阻塞的单元。

**不安全的恢复与容量回滚**
重启、恢复、回退或清理路径重建无界状态、忽略当前配额，或把立即重复失败的输入原样恢复。恢复正确性是可用性的一部分。

## 通用动作（适用于以上各类）

- 建一张"输入到资源"对照表：最早接受的规模/基数、认证前的工作、下游扇出、持久化、共享池、限制与清理的归属方、恢复方式。
- 对比总量限制与单对象限制。一万个合法的单字节条目可能绕过单条消息上限，却耗尽租户级或进程级状态。
- 只在隔离的 fixture 中验证，施加严格的 CPU/内存/时间限制和很小的增长点。外部与付费调用一律 mock，一旦缺失的边界或取消行为可观察就停止。

## 验证规则（报告本文件任何发现之前必须执行）

1. 指明不可信输入、请求者工作量、服务放大或被保留的资源、共享影响范围与恢复方式。只有"缺少限制"而无具体共享影响的，属于加固建议。
2. 确认源码可见的上游、解析器、队列、租户或框架边界没有一个能阻止该路径。未知的已部署控制记为 `needs_validation`。
3. 超线性行为：确立可接受的复杂度与有界的本地增长。泄漏：展示在本应清理之后仍可重复观测的驻留。致命路径：识别进程/supervisor 隔离。
4. 按请求者工作量小、未认证即可触达、跨租户范围、持久性、恢复差来排序；不要用可用性影响来验证。
5. 只有具备安全的本地证明与有意义的共享影响才返回 `confirmed`；返回 `needs_validation` 时写明负责人必须核查的确切上游限制、拓扑、配额或恢复行为。
