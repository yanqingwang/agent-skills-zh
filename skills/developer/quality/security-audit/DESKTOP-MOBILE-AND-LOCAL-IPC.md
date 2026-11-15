> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/DESKTOP-MOBILE-AND-LOCAL-IPC.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 桌面、移动与本地 IPC 审查

#### 何时使用本文件

当目标是桌面或移动应用、特权 helper、更新器、本地守护进程、webview 宿主、deep-link 处理器、浏览器 native-messaging 宿主或本地 IPC 客户端/服务器时使用本文件。相关的不可信行为者可能是下载的文档、远程 Web 内容、另一个本地应用、另一个 OS 用户、沙箱化进程或更低权限账户。请陈述这一起始能力，而不是把所有本地用户等同视之。

浏览器侧 webview 行为用 `CLIENT-SIDE.md`，native 内存与加载器安全用 `MEMORY-SAFETY-AND-BINARY.md`，更新真实性用 `SUPPLY-CHAIN-AND-RELEASE.md`。

## 核心纪律（加入本领域的每个 agent 提示词）

```
- Establish the realistic local or remote-content attacker: another app, another OS user, a sandboxed child, an untrusted document, or a remote origin. Self-harm within the same account and authority is not a boundary violation.
- Paths, process names, bundle/package IDs, and claimed sender fields are not peer authentication. Use OS peer credentials, code identity, capability handles, or protected channel state.
- The native bridge or helper must authorize each operation and final resource after parsing. A trusted UI or broker does not make attacker-influenceable arguments trusted.
- OS sandbox, signing, entitlements, permissions, keychain ACLs, exported-component policy, and prompt behavior are real controls when pinned and visible.
- Use `confirmed` for source evidence plus bounded local/emulator tests. Use `needs_validation` when signing, manifest merge, OS version, device policy, installer ACL, or packaging is required but not observable.
```

## Deep-link、回调与导航攻击类别（subagent_type: `general`）

**自定义 scheme 与 deep-link 歧义**
另一个应用或页面可以调用一个会变更状态、导入数据、完成认证或选择账户的路由，而没有当前 session 与一次性回调绑定。审查 URI 规范化、重复查询字段、scheme/host/path 匹配、导出的 activity/handler 策略，以及过期/重放的链接。

**应用与账户交接混淆**
OAuth、SSO、magic-link、邀请、设备配对、免密或支付回调返回到了错误的应用、profile、租户或待处理事务。把状态绑定到发起应用的身份、当前 session、账户、提供方、操作和有效期。

**文件打开与 intent 权限混淆**
关联文件、分享 intent、拖放项、粘贴板/剪贴板记录、通知动作或文件打开事件在未确认内容类型、（适用时的）发送者信任、当前用户意图和最终目标的情况下触发特权操作。

## Webview 与 native 桥攻击类别（subagent_type: `general`）

**导航 origin 到桥的混淆**
远程或攻击者可控的 frame 可以到达本应只面向打包内容的 JavaScript/native 桥。在调用时刻以及每次导航、重定向、子 frame 创建、弹窗和错误/后备页面之后验证 origin。URL 前缀检查和首载检查不够。

**过宽的 native 桥能力**
Web 内容可以通过通用桥选择任意文件、命令、IPC 方法、凭证或系统动作。检查方法 allowlist、参数规范化、用户/租户权限、手势/确认要求和返回值披露。

**Webview 文件与 universal 访问**
远程内容可以读取应用本地文件、特权自定义 scheme 或内部 origin，因为文件访问、universal 访问、混合内容、调试接口或自定义协议处理器意外地合并了 origin。缺失 restrictive 设置但无可达的受保护内容属于加固问题。

## 本地 IPC 与导出组件攻击类别（subagent_type: `general`）

**IPC 对端认证缺口**
Unix socket、命名管道、XPC、Binder、D-Bus、native messaging、RPC、共享内存或 loopback 监听器在不检查 OS 凭证、代码身份、沙箱 token 或通道所有权的情况下接受更低信任的对端。要求通道之后有实质性的方法或披露。

**声称的主体与通道身份不符**
已认证的进程/通道属于一个应用或用户，但请求字段选择了另一个用户、租户、profile 或能力。把每个方法和资源绑定到对端凭证，而不是调用者声明的标识符。

**导出的 service、activity、receiver 或 provider 越权**
移动组件或本地自动化端点可被外部调用，却执行本应面向应用自身的操作。审查最终合并的 manifest、intent filter、权限/签名级别、路径授权和替代别名。打包后 manifest 状态未知要求 `needs_validation`。

**IPC 生命周期与关联混淆**
可预测的请求 ID、重用的句柄、过期通道、继承的描述符、全局可写的 socket 路径或重启行为，让一个对端可以应答、取消或重用另一个对端的操作。审查 socket 文件、锁、端口和共享映射的创建权限与清理。

## 特权 helper 与本地文件攻击类别（subagent_type: `general`）

**特权 helper 成为糊涂代理人（confused deputy）**
低权限调用者可以在没有按操作授权的情况下选择特权命令、文件、服务、用户或系统设置。审查 sudo/polkit/UAC/XPC helper 规则，并确保 helper 独立验证规范化后的参数。

**安装、更新与修复路径信任**
特权安装器/helper 在授权之后读取更低信任行为者可写的 manifest、脚本、包、symlink、工作目录或修复状态。把授权绑定到不可变内容和安全的目标路径。

**本地文件所有权与 TOCTOU**
应用先检查文件/路径，然后在特权读写期间追上了替换、symlink、挂载或大小写/规范化变化。使用基于描述符的操作并验证最终所有权。文件打开之后的解析问题聚焦到 `MEMORY-SAFETY-AND-BINARY.md`。

**凭证存储与本地秘密边界不匹配**
keychain/keystore 条目、token 文件、备份、日志、剪贴板、通知预览或本地配置可被权限更低的另一个应用/profile/用户读取。仅同一预期 OS 账户可读的明文不自动构成漏洞；陈述更低信任的读取者和凭证权限。

## 应用状态与设备生命周期攻击类别（subagent_type: `general`）

**账户切换、注销与设备恢复泄露**
缓存数据、后台任务、widget、通知、本地数据库、webview 存储或生物识别批准在注销/换号后仍然存活，并出现在后来的账户之下。审查备份/恢复与多 profile 行为。

**待处理动作与用户在场混淆**
通知、widget、快捷方式、分享面板、生物识别提示或延迟操作授权了与显示不同的动作、在过期后执行，或使用另一个 profile 的待处理状态。把确认绑定到规范化动作、资源、账户和当前前台状态。

## 通用手法（适用于以上所有类别）

- 枚举每个进程、应用组件、本地端点、URI scheme、文件关联、webview origin 和 helper。记录 OS 身份、运行时权限、调用者和可调用操作。
- 读取最终打包输入：合并的 manifest、entitlements、安装器规则、native-messaging 注册、协议处理器和 ACL 创建。源码声明可能被下游覆盖。
- 在隔离机器/模拟器上用 dummy profile 和非敏感本地 fixture 验证。不要与其他用户的应用、凭证或生产服务交互。

## 验证规则（报告本文件任何发现之前先执行）

1. 点名攻击者起始能力、跨越的 OS/应用主体、入口通道、被接受的参数或状态，以及未授权的操作或披露。
2. 确认适用的 OS 沙箱、对端凭证、签名、entitlement、权限、用户同意和安装器控件。未知的打包/运行时事实要求 `needs_validation`。
3. 对 webview 桥，同时引用导航/origin 控件与特权 native 汇点（sink）。对 IPC，引用对端认证与按资源授权。对 helper，验证最终规范化目标。
4. 本地测试保持有界并使用 dummy 内容/账户。证明边界结果即止；不要把证明延伸到持久化或更广的系统修改。
5. 只有在完整的源码与本地证据链时才返回 `confirmed`。`needs_validation` 要给出所需的精确 OS、manifest、签名、ACL 或设备生命周期事实。
