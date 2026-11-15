> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/CLOUD-AND-DEPLOYMENT.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 云与部署审查

#### 何时使用本文件

当仓库定义了云身份、基础设施、容器、Kubernetes、service mesh、serverless 函数、edge worker、ingress、对象存储、托管服务或按环境区分的配置时使用本文件。本领域问的是：部署后的组件是否获得了预期的身份、隔离、网络可达性、秘密和策略。源码表达的常常是意图而非线上事实，所以要把源码可确认的缺陷与需要部署验证的部分分开。

构建与晋升（promotion）信任用 `SUPPLY-CHAIN-AND-RELEASE.md`，HTTP 代理语义用 `WEB-PROTOCOL-AND-AUTH.md`，数据存储的租户范围用 `DATA-ISOLATION-AND-LIFECYCLE.md`。

## 核心纪律（加入本领域的每个 agent 提示词）

```
- Do not infer a live exposure from a manifest alone. Establish which environment consumes it, what defaults or overlays modify it, and whether the source path is active.
- Map each workload's identity to specific operations and resources. Broad policy is a finding only when lower-trust input can reach an unauthorized action.
- Ingress, proxies, service mesh, metadata services, and admission policy are real boundaries, but only count a control when its configuration and attachment are visible.
- Secret references are not secret disclosure. Require a lower-trust reader, output, artifact, log path, or unsafe fallback.
- Use `confirmed` for active in-repo configurations and local rendering/policy validation. Use `needs_validation` for account policy, network attachment, runtime admission, hosted metadata, or drift that needs owner observation.
```

## 工作负载身份与 IAM 攻击类别（subagent_type: `general`）

**工作负载身份越权**
工作负载、pod、函数、edge worker 或节点身份可以对超出其角色的租户、账户、资源或 API 执行操作，且不可信的请求或任务输入选择了那个目标。审查云策略条件、资源模式、service account 绑定、namespace 映射和后备凭证。

**跨账户或跨租户角色混淆**
角色承担（role assumption）、external ID、token 交换、工作负载联邦或资源策略接受了未绑定到预期源账户、受众、仓库、namespace 或工作负载的身份声明。同时确立信任策略和调用者可控的声明。

**应用授权被委托给云元数据**
应用信任调用者提供的身份头、标签、注解、账户 ID 或资源元数据，却不验证它们来自云控制平面或可信代理。云 IAM 与应用授权是两个独立的检查。

## Ingress、网络与控制平面攻击类别（subagent_type: `general`）

**意外的服务或管理平面可达性**
ingress、service、listener、安全组、负载均衡器注解、端口映射或服务器绑定把 admin、调试、metrics、节点、控制平面或内部 API 暴露给更低信任的网络。仅有网络控制缺失是 `needs_validation`；仓库可控的通往敏感 handler 的公开路由可以是 `confirmed`。

**可信代理与 mesh 身份绕过**
后端接受来自预期 ingress/sidecar 之外的对端的转发身份、mTLS subject 或授权元数据，或另一端口与健康/遗留路径绕过了 mesh。验证头部剥离、对端可达性，以及代理缺席时的 fail-open 行为。

**元数据与内部服务可达性**
不可信的 URL、目的地或协议选择到达了实例/容器元数据、控制平面 socket 或带工作负载凭证的内部 API。URL 解析与重定向处理按 `ATTACK-CLASSES.md` 追踪；这里确立部署的网络、元数据版本和身份边界。

## 容器与编排攻击类别（subagent_type: `general`）

**宿主或控制平面能力暴露**
更低信任的工作负载可以选择特权模式、capabilities、宿主 namespace、宿主路径、设备挂载、容器运行时 socket 或跨越到节点/控制平面权限的 service account token。仅有 seccomp 或只读文件系统缺失属于加固问题，除非某个可达操作跨越了那条边界。

**准入与策略路径不一致**
一条部署路由强制了镜像身份、namespace、资源、秘密或特权策略，而另一条控制器、任务、升级、恢复或兼容路径没有。确认那条替代路由和最终部署的对象。

**Namespace 与标签信任混淆**
网络、准入、秘密或工作负载身份策略依赖更低信任主体可以设置的标签、注解、名称或 namespace。对比谁控制选择器（selector）与匹配授予什么权限。

## 配置与秘密生命周期攻击类别（subagent_type: `general`）

**安全控制优先级漂移**
开发值、chart 默认值、环境变量、命令行标志、特性门（feature gate）、sidecar 注入或按 region 的 overlay 在部署环境中关闭了认证、传输安全、租户范围限定或审计策略。为每个维护中的部署渲染最终配置，而不只是基础文件。

**秘密跨工作负载边界暴露**
秘密进入另一个工作负载或租户可访问的日志、崩溃报告、进程参数、共享环境、宽泛卷、构建产物、服务发现或读取 API。检查秘密类型和权限；公开的端点或 key ID 不是凭证。

**凭证续期与故障后备**
挂载、刷新、轮换或吊销工作负载凭证的失败导致过期凭证继续有效，或应用接受更低信任的身份模式。审查启动、就绪、重连和缓存客户端行为。

## 托管存储、事件与边缘攻击类别（subagent_type: `general`）

**对象与签名 URL 策略混淆**
bucket/container 策略、对象键、CDN origin 或签名 URL 未能绑定主体、操作、对象 namespace、受众或有效期。审查 list/version 操作和写路径，而不只是读。

**事件源身份混淆**
函数或 worker 把事件体字段当作源身份信任，却不验证提供方签名的信封、订阅/topic、账户、region 和重放状态。对比 push、pull、重试和死信路径。

**边缘/运行时边界不匹配**
边缘或 serverless 运行时假设的秘密、API、文件系统、隔离或租户策略与源运行时不同，回退到源运行时会改变权限或缓存行为。确认哪份配置选择了每条路径。

## 通用手法（适用于以上所有类别）

- 渲染每个维护中的环境，并做出一张矩阵：对外端口、工作负载身份、网络对端、挂载的秘密和云资源。差异需要所有者或策略解释。
- 跟随一个更低信任的请求、对象、标签或事件进入云策略。展示哪个工作负载凭证执行最终操作，以及本应由什么条件限定它。
- diff 正常部署、迁移、恢复、节点维护、故障转移和本地/模拟器路径。审查 mesh、准入、身份、秘密或策略服务不可用时的行为。

## 验证规则（报告本文件任何发现之前先执行）

1. 确立激活的源码路径和生效的部署对象；否则用 `needs_validation` 并说明缺了哪个渲染后的 manifest 或所有者观测的绑定。
2. 点名更低信任的调用者/工作负载、云或应用身份、可控选择器、受影响资源，以及未授权的操作或披露。
3. 在锁定版本上验证提供方与编排器的默认值。不要假设公开 IP、可达的元数据服务、宽松的防火墙或缺失的准入绑定。
4. 本地验证可以渲染模板、评估策略、在隔离 fixture 中检查容器/用户 namespace，或用 dummy 身份运行模拟器。不要探测在线端点或改动共享云资源。
5. 只有在完整的激活源码轨迹加具体的边界结果时才返回 `confirmed`。`needs_validation` 要给出所需的精确部署策略、身份绑定、overlay、网络或漂移观测。
