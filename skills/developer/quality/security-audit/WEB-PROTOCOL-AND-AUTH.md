> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/WEB-PROTOCOL-AND-AUTH.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# HTTP 协议与认证（Authentication）审查

#### 何时使用本文件

当目标在解析、缓存、浏览器认证或身份边界上使用 HTTP 时使用本文件：Web 应用、API、反向代理、CDN、网关、自定义 HTTP 服务器，以及实现 session、JWT、OAuth/OIDC、SAML、密码找回、MFA、passkey、API key 或 mTLS 的服务。与 `ATTACK-CLASSES.md` 配合使用：访问控制审查问的是某个主体（principal）是否可以执行某项操作；本文件问的是 HTTP 或身份层能否混淆该操作所属的主体、请求、保障级别（assurance）或 token。

从 Phase 1 中挑选类别。把大型目标拆分为：请求分帧与缓存策略、浏览器认证、联邦身份、强认证与找回、服务凭证、session 生命周期。一个藏在无人观测的托管代理后面的单一服务器，几乎没有源码可确认的走私（smuggling）面；代理或自定义解析器的面则大得多。

## 核心纪律（加入本领域的每个 agent 提示词）

```
- Framing and cache findings require two interpretations of the same request, response, or key. Name both components and the exact normalized value on each side.
- For every credential, find the signature or secret verification and every binding required for its role: issuer, audience, origin, RP, client, session, principal, resource, assurance, expiry, and one-time state.
- Host, Forwarded, X-Forwarded-*, Origin, Referer, redirect targets, callback state, and request-derived URLs are trust decisions. Trace each to the affected identity or response.
- A missing header, cookie attribute, MFA prompt, or rate limit is not a finding alone. Require an accepted invalid request, cross-principal impact, assurance downgrade, or credential disclosure.
- Classify `confirmed` only from complete source evidence and bounded local request/token tests. Use `needs_validation` when proxy, IdP, browser, certificate, secret, or deployed configuration is required but not visible.
```

## HTTP 分帧与缓存攻击类别（subagent_type: `general`）

**请求分帧与失步（desynchronization）**
前端与后端对请求长度或头部规范化的理解不一致。审查多个 `Content-Length` 值、`Transfer-Encoding`、HTTP/2 或 HTTP/3 降级、头部名规范化、禁止的连接头部、CR/LF 转换。确认哪个组件把哪些字节划给一个请求，其对端把哪些字节划给下一个请求。

**通过未键入（unkeyed）输入污染 Web 缓存**
某个请求值改变了缓存内容或与安全相关的头部，但不在缓存键里。对比缓存键的构造与每一个响应变体，包括转发的 host/scheme、被选中的 cookie、查询规范化、语言/设备头部、授权状态。

**缓存欺骗（deception）与私有响应缓存**
缓存路由把私有动态路径当作公开静态资产，或缓存了身份与授权输入不在策略中的响应。对比边缘缓存能力与应用路由解析、后缀/路径参数规范化、响应缓存指令。

**Host 与 forwarded 头信任**
不可信的 host/代理元数据决定了绝对 URL、租户路由、回调、重置链接、缓存键或授权所用的客户端地址。确认谁能提供该头部，以及可信入口是否会移除客户端提供的副本。

**响应头注入**
不可信数据带着不安全控制字符或规范化差异到达 `Location`、`Set-Cookie`、CSP 或其他响应头。报告前先验证框架是否会拒绝，并要求一个与安全相关的响应变化。

## 浏览器会话攻击类别（subagent_type: `general`）

**普通 CSRF**
浏览器把环境凭证（ambient credentials）发送到一个接受跨站请求的状态变更端点，且没有有效的反 CSRF token、同站请求绑定或严格的 Origin/Referer 校验。清点每一个 cookie 认证的变更操作，包括 form、类 JSON、multipart、method-override 和遗留路由。SameSite 只对实际使用的 cookie 与浏览器上下文有效；登录 CSRF 和跨站子资源请求可能有不同的要求。

**会话固定（fixation）与失效**
登录、切换账户、完成 MFA、模拟（impersonation）或其他权限变化时 session 标识不轮换，或注销、改密、撤销、禁用账户后仍然有效。检查服务器 session、refresh token、签名 cookie、websocket 状态、缓存副本和后备端点。

**Cookie 作用域与传输**
敏感 cookie 的 `Domain` 或 `Path` 过宽、可跨越不安全传输，或与另一个组件选择方式不同的兄弟 cookie 冲突。仅有缺失的标志位属于加固建议，除非存在现实的更低信任来源、网络位置或浏览器路径能获取或替换该凭证。

## 联邦身份攻击类别（subagent_type: `general`）

先确立角色。授权服务器侧的控件（如 redirect allowlist 和 code 签发）不属于依赖方（RP）客户端。验证与绑定缺陷属于消费该工件（artifact）的组件。

**JWT 验证与声明（claim）绑定**
检查签名验证、服务端固定的算法和密钥来源，然后检查 `exp`、`nbf`、`aud` 和 `iss`。把 `kid`、`jku` 和 `x5u` 当作不可信的密钥选择器审查，还有重复/头部规范化以及"只解码不验证"的路径。另一个服务的有效 token 在这里无效，即使它由可信签发者签名。

**OAuth/OIDC 请求与回调绑定**
在目标是授权服务器时，校验精确的 `redirect_uri` 归属；session 绑定的 `state`；适用的 PKCE 与授权码绑定；ID token 的签发者/受众/签名/nonce；多提供方流程中的所选 IdP 绑定。对比初始回调、重试、移动/deep-link 和账户关联路由。

**SAML 签名对象与断言绑定**
确保被验签的元素就是被用作身份的元素。审查未签名/后备路径、安全的 XML 解析器配置、规范化差异，以及新鲜度/绑定字段：有效期窗口、受众/接收方、请求关联和重放状态。

## MFA、passkey 与账户变更攻击类别（subagent_type: `general`）

**MFA 注册与保障级别降级**
注册、替换、停用、恢复码生成、可信设备创建和后备登录都要求预期的先前保障级别。检查一个有效的一因子是否能在没有策略要求的重新认证的情况下注册或替换第二因子，以及被停用或过期的因子是否停止对 session 的授权。

**Step-up 绑定与绕过**
一次成功的挑战升级了错误的 session、账户、租户、动作或 API 请求，或另一条路由省略了保障检查。把挑战绑定到主体、当前 session、保障目标、需要的操作或资源、有效期和一次性完成。对比 UI、API、批处理、找回和恢复流程路径。

**WebAuthn 与 passkey 验证**
注册时，把 challenge、RP ID、预期 origin、凭证、用户/userHandle、算法和策略要求的用户验证绑定到发起的 session。认证时，验证 challenge、RP/origin、凭证归属、签名，以及预期的用户在场/验证。检查账户发现和关联流程中的 userHandle 或凭证与账户混淆。签名计数器的处理只有在产品把回退当作克隆信号时才有意义。

**账户关联与身份碰撞**
向既有账户添加 IdP、passkey、邮箱、手机、设备或外部账户，必须要求当前已认证的 session、对新身份的所有权验证、策略要求的 step-up，以及绑定到发起关联账户的回调状态。审查解除关联/重新关联与邀请接受路径中的已验证标识符或租户碰撞。

**密码重置与更广的找回**
恢复 token、支持/管理员找回、备份码、设备迁移、邮箱或手机变更常常成为最弱的认证路径。验证 token 随机性、用户/动作绑定、有效期、一次性状态、速率/计数控制、投递 URL 信任，以及先前 token 和 session 的失效。只泄露公开账户存在性的不同响应不自动构成安全发现。

## API key 与 mTLS 攻击类别（subagent_type: `general`）

**API key 范围与资源绑定**
一个 key 能认证到比其服务端记录授予的更宽的租户、资源、动作或环境，或请求参数覆盖了这些绑定。审查 key 查找、前缀/完整密钥验证、可发布密钥与秘密密钥之间的类型混淆、范围检查、轮换、撤销缓存和批量端点。

**API key 暴露与不安全传输**
key 出现在客户端 bundle、URL、重定向、日志、错误路径、构建产物或更低信任主体可访问的响应里。被称为 key 的公开标识符不是秘密。确认 key 类型与泄露获得的权限。

**mTLS 对端与应用身份混淆**
进程信任来自任意网络对端的客户端证书身份头、验证了链却把可被攻击者影响的 subject 文本错误映射到账户，或接受了错误信任域、扩展用途、受众或有效期策略的证书。在可信代理终结 mTLS 的地方，验证只有该代理能连接、它移除入站身份头、后端把净化后的身份绑定到请求。

**证书生命周期后备**
过期、吊销、缺失或续期失败的证书导致静默回退为仅 bearer 或匿名运行，或长期存活的连接池连接在吊销后仍保留授权。缺少部署侧吊销数据使结果为 `needs_validation`；仓库内的 fail-open 分支可由源码确认。

## 通用手法（适用于以上所有类别）

- 对每个凭证和挑战，走一遍 issue → store → transmit → consume → refresh → revoke。对比正常、错误、重试、迁移、遗留和账户切换路径。
- 枚举通往同一身份的每一扇门、通往同一敏感操作的每一条路由。实际生效的策略是最弱的并行路径，不是最精致的 UI。
- 并排 diff 解析器、代理、路由器、缓存与应用的规范化。本地验证时，把相同的受限请求 fixture 喂给每个组件，而不是向线上部署发送流量。
- 对找回与关联，画出账户的前后图。每条边都必须点名当前主体、新身份的证明、要求的保障、回调/session 绑定和撤销效果。

## 验证规则（报告本文件任何发现之前先执行）

1. 施加源码可见性闸门。代理链、边缘缓存键、IdP 策略、证书信任、浏览器 cookie 行为、秘密和部署的认证模式可能在仓库之外。记录一个精确的 `needs_validation` 候选，而不是断言缺失的基础设施行为。
2. 对分帧与缓存发现，点名两个组件以及分歧的解析/键。用受限的本地 fixture 确认跨请求、跨用户或私有响应的影响。
3. 对 token、MFA、passkey、账户关联、找回、API key 和 mTLS 发现，引用验证代码行和缺失的主体/session/资源/origin/audience/action/保障绑定。证明服务器接受了无效的转换或凭证。
4. 对 CSRF，点名环境凭证、状态变更路由、被接受的跨站请求形状、浏览器 cookie 策略和缺失的有效检查。只读操作和需要非环境 bearer token 的路由不符合条件。
5. 验证框架与库的默认值。版本或配置未知时用 `needs_validation`；不要把一个未验证的 critical 主张降级成低严重级的 confirmed 发现。
6. 只有在完整的源码轨迹加可观测的未授权身份、状态或泄露时才返回 `confirmed`。对 `needs_validation`，点名缺失的事实，以及能解决它的安全的本地检查或所有者观测检查。
