> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/CLIENT-SIDE.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 客户端与浏览器审查

#### 何时使用本文件

当有意义的信任决策或不可信渲染发生在浏览器里时使用本文件：单页应用、浏览器扩展、嵌入式 webview、service worker、离线应用，以及把攻击者可影响的内容渲染进 DOM、接收跨窗口消息或使用浏览器存储的代码。这些路径包括服务器永远看不到的来源，如 URL fragment、`window.name`、`postMessage` 和之前缓存的内容。

与 `ATTACK-CLASSES.md` 配合使用。本文件覆盖浏览器来源与汇点（sink）、origin 边界、浏览器持久化和跨站状态预言机（oracle）。webview 桥的 native 侧用 `DESKTOP-MOBILE-AND-LOCAL-IPC.md`，服务端 CSRF、session 和认证回调用 `WEB-PROTOCOL-AND-AUTH.md`。

## 核心纪律（加入本领域的每个 agent 提示词）

```
- A client-side candidate needs a controllable source and an executing or disclosing sink. Name both and show attacker-influenced data reaching the sink.
- The impact must reach a victim's session, another origin, or shared persistence. Self-injection and disclosure of the attacker's own data are not findings.
- Framework escaping, browser same-origin policy, CSP, COOP/CORP, service-worker scope, and modern noopener defaults are real controls. Verify them before assigning impact.
- Browser storage and caches are shared by origin and may outlive login state. Identify who writes, who reads, and which account, tenant, or worker lifecycle clears each record.
- Use `confirmed` only for complete source evidence plus bounded local browser tests. Use `needs_validation` when renderer, extension permission, deployed header, or browser-policy behavior is required but unavailable.
```

## DOM 与对象状态攻击类别（subagent_type: `general`）

**基于 DOM 的 XSS**
追踪 `location` 字段、`document.referrer`、`window.name`、消息数据、存储和浏览器控制的文档状态进入 `innerHTML`、`outerHTML`、`document.write`、字符串求值 API、可执行 URL、jQuery HTML API 或框架逃生通道。被框架转义的插值不是发现。

**DOM clobbering（DOM 命名遮蔽）**
攻击者注入的 `id` 或 `name` 属性遮蔽了稍后被代码信任的全局变量、form 属性、配置对象或初始化标志。要求既有一条保留该属性的标记路径，又有对被遮蔽值的安全相关使用。

**原型污染与 gadget 链**
攻击者可控的键到达递归写入（如 deep merge 或路径赋值）并修改原型状态。然后一个可达 gadget 消费被污染的属性，改变授权、执行、导航或渲染。`JSON.parse`、浅拷贝或没有 gadget 的污染不够。

## 跨源消息与网络攻击类别（subagent_type: `general`）

**`postMessage` origin 与来源信任**
handler 在没有精确 origin allowlist、以及（多 frame 共享 origin 时的）预期 `event.source` 的情况下用 `event.data` 执行敏感动作。发送侧，发到 `*` 的敏感数据到达非预期的嵌入者。弱的子串、前缀、后缀或未锚定的正则 origin 匹配不是 origin 检查。

**跨站 WebSocket 请求使用**
WebSocket 升级接受来自不可信 origin 的环境 cookie，而没有 `Origin` 检查或通道专属 token，让受害者的 session 读取或修改数据。同时确认升级行为和一个安全相关的消息 handler。

**带凭证的 CORS 信任**
服务器反射或弱匹配 `Origin` 却允许携带凭证，并返回敏感响应。带凭证的裸通配符会被浏览器拒绝；只报告实际反射/放行的 origin 路径和跨源数据或修改。

## Service worker 与浏览器存储攻击类别（subagent_type: `general`）

**Service worker 注册与作用域接管**
攻击者可影响的内容可以成为注册的 worker 脚本、控制一个接收过宽 `Service-Worker-Allowed` 作用域的路径，或在无完整性控制下修改更新导入。验证最终脚本 URL、响应 MIME 类型、origin、作用域，以及谁控制每一个被导入的脚本。正常同源、作用域符合预期的 worker 不是缺陷。

**Service worker 缓存与身份混淆**
worker 缓存了个性化响应，却没有把账户、租户、授权状态或请求模式纳入其策略，然后在换号或注销后继续返回它们。审查 fetch 事件路由、缓存名称与键、导航后备、缓存清理，以及错误/离线路径是否会返回另一个用户先前的响应。

**浏览器存储泄露与过期授权**
token、私有响应、草稿数据或授权决定留在 `localStorage`、`sessionStorage`、IndexedDB、Cache Storage、扩展存储或客户端状态里，变成另一个账户或更低信任的同源组件可读。仅存储一个 token 不是发现；要求一个权限更低的现实读取者，或吊销/注销后的继续使用。

**跨上下文存储与广播混淆**
`storage` 事件、`BroadcastChannel`、shared worker 或全 origin 缓存在标签页之间传递身份或命令，却没有绑定到当前 session。检查换号、隐私/普通窗口、租户变更，以及可能覆盖较新授权状态的过期标签页。

## 跨站信息泄露类别（subagent_type: `general`）

**XS-Leaks 与跨源状态预言机**
攻击者页面可以通过资源加载/错误事件、frame 或窗口状态、重定向行为、计时、缓存状态或响应大小区分受保护的跨源状态，同时浏览器附上受害者凭证。要求一个具体的携带秘密的谓词，例如某个私有对象、角色或账户是否存在。一般性计时差异或公开资源可用性不是发现。

**窗口与 opener 状态泄露**
跨源窗口允许的元数据或导航结果揭示了受保护状态，或被保留的 opener/命名窗口关系让攻击者可控页面影响一次特权导航。检查 COOP、frame 防护、`noopener`、精确 origin，以及可观测状态是否机密。

## UI 伪装与导航攻击类别（subagent_type: `general`）

**点击劫持（Clickjacking）**
被 frame 包裹的状态变更动作缺少有效的 `frame-ancestors`、`X-Frame-Options` 或等价的 UI 隔离。要求敏感动作存在，并确认它能在被 frame 状态下完成；只读内容缺头部属于加固建议。

**客户端导航混淆**
客户端来源控制重定向或导航而没有 scheme 与目的地策略，包括可执行的 `javascript:` 或 `data:` 目的地。反向标签劫持（reverse tabnabbing）只适用于代码显式保留 `window.opener`、不带隔离使用 `window.open`、或支持没有隐式 `noopener` 的浏览器的情况。

## 通用手法（适用于以上所有类别）

- 从 DOM、导航、worker、消息和存储汇点出发，反向追踪到浏览器独有和服务器控制的来源。记录本应阻断该路径的浏览器策略。
- 用本地测试 origin 和 dummy 账户测试换号、注销、worker 更新、离线后备和过期标签页状态。不要使用生产用户、origin 或共享服务。
- 对 XS-Leaks，只列出由源码和本地浏览器行为证明的谓词。然后指出能移除该预言机的响应头或渲染选择。

## 验证规则（报告本文件任何发现之前先执行）

1. 引用来源、汇点、浏览器策略、受影响的 origin/session，以及可观测的修改或泄露。
2. 对原型污染，证明递归写入和一个安全相关的 gadget。对 DOM clobbering，证明标记存活且被遮蔽值被使用。
3. 对 service worker 和存储，证明生命周期可达性：攻击者可控的写入或缓存条目必须到达不同的账户、租户或更晚的授权状态。
4. 对消息、CORS、WebSocket 和 XS-Leaks，展示精确的 origin/来源验证和被暴露的受保护状态或动作。确认 CSP、COOP/CORP、cookie 和 SameSite 策略没有已经阻断它。
5. `confirmed` 发现必须有完整的客户端路径和有界的本地证据。`needs_validation` 要给出所有者需要验证的精确部署头、扩展权限、浏览器版本或渲染器行为。
