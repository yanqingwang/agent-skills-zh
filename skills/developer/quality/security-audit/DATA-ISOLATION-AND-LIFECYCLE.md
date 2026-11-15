> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/DATA-ISOLATION-AND-LIFECYCLE.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 数据隔离与生命周期审查

#### 何时使用本文件

当目标存储多租户或访问受控数据、派生搜索/索引/缓存/分析副本、签发对象链接、导出或恢复记录、迁移 schema，或承诺删除、吊销和保留行为时使用本文件。本领域跟踪一条数据经过每一份副本和每一次状态转换。端点级访问控制用 `ATTACK-CLASSES.md`，提供方级存储策略用 `CLOUD-AND-DEPLOYMENT.md`。

按主存储、缓存/搜索、对象/blob 存储、分析/日志、导出/备份、删除/吊销和迁移拆分大型目标。

## 核心纪律（加入本领域的每个 agent 提示词）

```
- A tenant or owner field on a record is not isolation. Find the query, key, path, policy, or row-level control that enforces it for each read and write path.
- Trace derived copies. Sanitized primary data can become unsafe in search, cache, analytics, export, previews, logs, replicas, and backups with different ACL and retention rules.
- Deletion and revocation are lifecycle contracts. Check current, historical, cached, indexed, exported, restored, and queued copies within the product's stated boundary.
- Privacy or retention preference is not automatically a security vulnerability. Require an explicit data-access boundary or deletion/revocation guarantee and an unauthorized reader or later operation.
- Use `confirmed` for complete source-visible lineage and bounded dummy-tenant tests. Use `needs_validation` when external storage policy, retention, CDN behavior, replica lag, or backup access is unavailable.
```

## 租户与对象隔离攻击类别（subagent_type: `general`）

**缺失的租户或所有者强制**
读、更新、删除、列表、计数或批量查询在识别对象时没有把它绑定到已认证的租户/所有者，或信任 body 字段来提供该身份。对比直接查找、嵌套关系、后台、admin、导入和遗留路径。

**复合键与 namespace 碰撞**
缓存键、对象路径、数据库唯一性、搜索文档 ID、临时文件或去重键省略了租户或环境。即使应用记录各归各的所有者，两个主体也可以覆盖或取回同一个逻辑键。

**策略与查询不一致**
行级策略、ORM 默认 scope、授权过滤器和原生/绕行客户端应用了不同的谓词。检查 join、聚合、别名、视图、事务、`unscoped` 或 service 客户端，以及上下文缺失的错误路径。

**Blob 与签名引用越权**
对象键、附件 ID、版本 ID、共享链接或签名 URL 允许超出签发主体访问范围的操作或 namespace，或在底层 ACL 变更后仍然有效。绑定操作、精确对象/版本、受众、有效期和租户。

## 派生数据与泄露攻击类别（subagent_type: `general`）

**搜索、缓存与索引 ACL 漂移**
主记录的 ACL 或生命周期变化了，却没有让可搜索、缓存、嵌入、缩略图、RSS、预览或索引的副本失效。在文档摄取与失效之外，还要在取回时刻验证过滤。

**分析、日志、追踪与诊断作为替代读取者**
私有内容或凭证被输出到访问更宽、保留更久或租户混杂的系统。确认数据类别和现实的读取者；仅字段名、公开标识符和预期策略下仅运维可见的内容还不够。

**枚举与聚合预言机（oracle）**
计数、过滤、排序、错误、唯一约束、计时、通知行为或存在性检查泄露受保护对象或账户的状态。要求一个具体的机密谓词和可观测的区分，而不是一般性的响应差异。

## 导出、备份、恢复与迁移攻击类别（subagent_type: `general`）

**导出与备份范围扩张**
导出、快照、可移植包、报告或备份包含了其他租户、不可访问的对象字段、软删除数据、秘密值或超出请求者权限的历史。在选择之后检查逐项授权，并对下载最终工件授权。

**导入与恢复权限扩张**
恢复/导入绕过所有者、schema、ACL、唯一性或验证规则、覆盖既有资源，或在请求者不可写的租户里重建记录。把归档内容当不可信数据验证，对由此产生的操作授权，而不是信任先前来源。

**迁移默认值与所有权混淆**
旧记录缺少租户/ACL/生命周期字段、不兼容的 ID 碰撞，或部分上线使新旧读取者应用不同的默认值。审查回填、双读/写、兼容、回滚和续跑迁移路径。

**备份与复制边界漂移**
加密密钥、存储账户、跨 region 副本、恢复环境或支持快照的身份或租户范围比主数据更宽。源码只能确认仓库内策略；托管访问与保留要求 `needs_validation`。

## 删除、吊销与生命周期攻击类别（subagent_type: `general`）

**软删除与墓碑（tombstone）绕过**
直接查找、搜索、关系遍历、对象链接、后台处理器或恢复忽略了生命周期谓词，返回或操作了已删除/已吊销的记录。检查软删除标识符能否在所有引用消失之前被重新注册。

**过期授权与派生副本使用**
成员移除、ACL 更新、同意撤回、秘密吊销或角色降级没有让 session、缓存、订阅、任务或物化数据失效，而它们继续为将来的操作授权。

**保留与排队工作超期**
删除在主存储完成了，而排队的处理器、重试、导出、分析或生成产物在承诺的边界之外重建或保留了数据。找到幂等删除和墓碑传播。

**恢复重新引入无效状态**
备份、撤销、取消删除或副本恢复恢复了当前策略已不允许的数据、凭证、成员资格或权限。对恢复的状态重新授权，并重新应用快照之后的生命周期变更。

## 通用手法（适用于以上所有类别）

- 挑一条受保护记录，画出主写、查询、缓存、索引、事件、导出、备份、删除和恢复路径。在每条边标记主体和租户。
- 通过同样的本地 service 方法对比两个 dummy 租户，然后在 ACL 变更、删除、换号和恢复之后重复。不要使用真实用户数据。
- 从绕行客户端、后台任务、迁移、全局唯一性和缓存键入手。这些路径常常省略交互式端点携带的请求级身份。

## 验证规则（报告本文件任何发现之前先执行）

1. 点名攻击者或更低信任主体、受保护数据/状态、受影响的所有者/租户、替代副本或操作，以及未授权的泄露或修改。
2. 同时引用预期的 source-of-truth 策略和省略或违背它的路径。确认没有另一层强制同样的租户/生命周期条件。
3. 用本地 dummy 租户和非敏感 fixture 证明跨范围访问或过期生命周期行为。到最小可观测记录或操作即止。
4. 需要外部缓存、对象存储、副本、分析、备份或保留策略时，归类为 `needs_validation` 并说明所有者观测检查。
5. 只有在完整的谱系加具体的边界影响时才返回 `confirmed`。`needs_validation` 要给出确切未决的存储、ACL、失效、保留或恢复事实。
