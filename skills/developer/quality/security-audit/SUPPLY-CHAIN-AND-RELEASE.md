> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/SUPPLY-CHAIN-AND-RELEASE.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 供应链与发布排查

#### 何时使用本文件

当目标解析依赖、用不可信贡献构建、运行 CI、生成发布产物、签名或晋升构建、加载插件或更新已部署软件时，使用本文件。本领域覆盖从源码与依赖到用户实际运行产物之间的信任交接。本地二进制加载器内部的缺陷用 `MEMORY-SAFETY-AND-BINARY.md`，运行时工作负载权限用 `CLOUD-AND-DEPLOYMENT.md`。

把大型目标拆分为：依赖解析、CI 隔离、产物来源（provenance）、发布授权、更新器/插件信任。

## 核心纪律（加入本领域每个 Agent 的提示词中）

```
- A mutable or known-vulnerable dependency is not a finding by itself. Show who can influence resolution, which build consumes it, and what execution or release boundary follows.
- Follow integrity across every handoff: source identity, resolved inputs, build worker, artifact identity, test result, signature/attestation, promotion, and update consumer.
- CI configuration is authorization code. Establish which event triggered a workflow, whose code runs, which secrets and tokens exist, and what it may publish or mutate.
- A checksum fetched from the same untrusted location as the artifact does not establish independent integrity. Identify the trusted root and failure behavior.
- Use `confirmed` for in-repo control-flow failures with bounded local validation. Use `needs_validation` for branch protection, hosted-runner, registry, signing-service, or production promotion facts that are not observable.
```

## 依赖与构建输入攻击类别（subagent_type: `general`）

**依赖来源与命名空间混淆**
解析器配置可能选中非预期的公共/私有命名空间、回退 registry、镜像、仓库或源 URL。审查包名、来源优先级、lockfile 与校验和的使用、备选构建文件、平台相关解析，以及首次安装与更新时的行为差异。

**可变且未绑定的构建输入**
构建会消费分支、tag、未验证的 submodule、下载的工具、生成的资源、远程 include、浮动版本的 CI action 或容器 tag，这些内容不经源码审查就能改变。要求存在一个低信任的写入方，以及一条进入可信构建产物的路径；可复现性本身不能证明真实性。

**生成源码与 codegen 的来源缺口**
Schema、vendored 压缩包、生成的客户端、本地化文件、文档示例或二进制 blob，产生可执行或随产品发布的内容，却没有与源码相同的审查与完整性闸门。比较本地重新生成与已提交的产物，并核实输入与生成器分别由谁控制。

**构建上下文夹带**
机密、本地配置、仓库元数据、测试 fixture 或开发者产物进入包或镜像，原因是构建上下文与 ignore 规则超出了预期的发布输入。确认最终产物确实暴露了真实凭证、私有数据或特权配置。

## CI 与自动化攻击类别（subagent_type: `general`）

**特权工作流中的不可信代码**
pull request、issue 评论、fork、依赖更新或外部事件会运行贡献者可控的代码，而环境中存在受保护的机密、写令牌、部署权限或受信任的 runner。比较触发类型、checkout ref、审批闸门、环境保护与权限收敛。不要假设源码中不存在的托管平台默认行为。

**工作流命令与表达式混淆**
攻击者可控的分支名、commit message、issue 字段、产物名、matrix 值或生成输出进入 shell 命令、模板表达式、路径或特权工作流输入，缺少规范化校验。

**缓存、产物与工作区的信任混用**
低信任的 job 可以填充一个缓存、产物、共享工作区或输出，随后被更高信任的 job 恢复并执行或发布。审查缓存键与命名空间、产物生产者身份、摘要绑定、保留策略，以及晋升时是否按可变名称重新解析。

**自动化身份权限过大**
CI job 拿到超出所需操作、仓库、环境或时限的权限，且不可信的 job 输入可以选中受影响的资源。仅缺最小权限属于加固；要求存在可达的特权操作。

## 发布与更新攻击类别（subagent_type: `general`）

**构建到晋升的替换**
测试、审查、签名与发布引用的是可变的 tag、文件名、渠道或产物 ID，而非同一个不可变摘要。检查构建与发布之间的每一次复制、重打包、多架构合并与来源记录步骤。

**发布授权与签名策略缺口**
发布或签名被接受时，其来源的工作流、仓库、分支、环境、密钥角色或阈值不对。审查 attestation 内部的身份声明，并验证消费方确实校验这些声明，而不只是验证签名有效。策略要求之处，轮换、过期与吊销必须 fail closed。

**更新元数据与回滚混淆**
更新器只认证载荷字节，却不认证版本、产品、平台、渠道、目标路径、有效期或回滚状态；或者它把元数据与载荷当作两次不同的授权事务来接受。验证原子安装与恢复行为。缺少策略绑定的签名 API 调用是不完整的。

**插件与扩展的信任扩张**
扩展包获得超出其声明范围的主机权限；低信任发布者可以替换另一个发布者的身份；或者安装/更新 hook 在真实性与能力检查之前运行。有意安装任意同用户插件不构成权限边界。

## 通用动作（适用于以上各类）

- 从一个已发布的摘要或已安装的更新反向追溯：每一个来源、生成输入、凭证、worker、缓存、测试结果与授权决策。
- 并排比较不可信与受保护的工作流事件。标出两者之间每个持久化的信道跨越点，要求不可变身份加上生产者信任。
- 审查密钥吊销、下载失败、attestation 缺失、平台部分发布、回滚与 registry 故障等路径。失败策略是发布完整性的一部分。

## 验证规则（报告本文件任何发现之前必须执行）

1. 指明低信任行为者、其可控的来源/缓存/产物/元数据、消费该结果的可信 job 或更新器，以及由此导致的未授权发布、代码引入、机密泄露或特权执行。
2. 证明产物身份在断裂的交接点两侧不一致。一个不同的可变名称或未绑定摘要必须能到达真实消费者。
3. 针对锁定版本验证包管理器、托管平台、registry 与签名服务的内建默认行为。未知的托管控制记为 `needs_validation`。
4. 本地验证保持有界：使用无害的 fixture 仓库、假凭证标记、本地 registry/配置与非生产产物命名空间。不要发布或改动真实发布。
5. 只有具备完整的源码可见交接链与有意义结果才返回 `confirmed`；返回 `needs_validation` 时写明负责人必须观察的确切分支、runner、registry、签名或部署事实。
