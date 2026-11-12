> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-server/references/auth.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# MCP Server 的认证

认证是多数人最终需要 **remote** server 的原因，即使本地 server 本来更简单。有真实托管端点可供回跳时，OAuth 重定向、token 存储与刷新都能顺畅工作。

## Claude 特有的认证

Claude 的 MCP 客户端只支持一组特定的认证类型，并非每个符合规范的流程都可用。完整参考：https://claude.com/docs/connectors/building/authentication

| 类型 | 说明 |
|---|---|
| `oauth_dcr` | 支持。对高流量的目录条目，优先用 CIMD 或 Anthropic 托管凭证，因为 DCR 每次新连接都会注册一个新客户端。 |
| `oauth_cimd` | 支持，目录条目推荐用它而非 DCR。 |
| `oauth_anthropic_creds` | 合作方把 `client_id`/`client_secret` 交给 Anthropic；需用户同意门控。联系 `mcp-review@anthropic.com`。 |
| `custom_connection` | 用户在连接时提供 URL/凭证（Snowflake 式）。联系 `mcp-review@anthropic.com`。 |
| `none` | 无认证。 |

**不支持：** 用户粘贴的 bearer token（`static_bearer`）；没有用户同意的纯机器对机器 `client_credentials` 授权。

**回调 URL**（所有端统一用这一个）：`https://claude.ai/api/mcp/auth_callback`

---

## 三个层级

### Tier 1：无认证 / 静态 API key

Server 从环境变量读一个 key。用户在配置时提供一次。完事。

```typescript
const apiKey = process.env.UPSTREAM_API_KEY;
if (!apiKey) throw new Error("UPSTREAM_API_KEY not set");
```

本地 stdio、MCPB、remote server 都适用。如果这就是你需要的全部，到此为止。

### Tier 2：经 CIMD 的 OAuth 2.0（规范 2025-11-25 起首选）

**Client ID Metadata Document。** MCP host 把自己的客户端元数据发布在一个 HTTPS URL 上，并直接用这个 URL *当作* `client_id`。你的授权服务器抓取该文档，校验后继续走授权码流程。没有注册端点，不存客户端记录。

规范 2025-11-25 把 CIMD 提升为 SHOULD（推荐）。在你的 OAuth AS 元数据中用 `client_id_metadata_document_supported: true` 声明支持。

**Server 职责：**

1. 在 `/.well-known/oauth-authorization-server` 提供 OAuth 授权服务器元数据（RFC 8414），含 `client_id_metadata_document_supported: true`
2. 提供指向 (1) 的 MCP 受保护资源元数据文档
3. 授权时：把 `client_id` 当作 HTTPS URL 抓取，校验返回的客户端元数据，然后继续
4. 对进入的 `/mcp` 请求校验 bearer token

```
┌─────────┐  client_id=https://...  ┌──────────────┐   upstream OAuth   ┌──────────┐
│ MCP host│ ──────────────────────> │ Your MCP srv │ ─────────────────> │ Upstream │
└─────────┘ <─── bearer token ───── └──────────────┘ <── access token ──└──────────┘
```

### Tier 3：经动态客户端注册（DCR）的 OAuth 2.0

**向后兼容的回退**，规范 2025-11-25 把 DCR 降级为 MAY。host 发现你的 `registration_endpoint`，POST 自己的元数据把自己注册为客户端，拿到 `client_id`，然后走授权码流程。

如果你需要支持还没迁移到 CIMD 的 host，就实现 DCR。server 职责与 CIMD 相同，区别是不再抓取 `client_id` URL，而是运行一个存储客户端记录的注册端点。

**客户端优先级顺序：** 预注册 → CIMD（若 AS 声明了 `client_id_metadata_document_supported`）→ DCR（若 AS 有 `registration_endpoint`）→ 提示用户。

---

## 内置 DCR/CIMD 支持的托管服务商

几家专注 MCP 的托管服务商会替你处理 OAuth 管道：你实现 tool 逻辑，他们运行授权服务器。当前能力以他们的文档为准。如果用户对托管没有强偏好，这通常是拿到一个可用的 OAuth 保护 server 的最快路径。

---

## 本地 server 与 OAuth

本地 stdio server **可以**做 OAuth（打开浏览器、在 localhost 端口上接住重定向、把 token 存进 OS keychain）。但它很脆弱：

- 在无头/远程环境中会坏
- 每个用户都要重走一遍这套流程
- 没有集中的 token 刷新或吊销

如果需要 OAuth，坚决倾向 remote HTTP。如果*必须*本地 + OAuth，`@modelcontextprotocol/sdk` 自带 localhost 重定向辅助工具，并使用 MCPB 打包，至少运行时可预测。

---

## Token 存储

| 部署形态 | Token 存放在 |
|---|---|
| Remote，无状态 | 哪儿都不存，host 每次请求都带 bearer |
| Remote，有状态 | 以 MCP session ID 为键的会话存储（Redis 等） |
| MCPB / 本地 | OS keychain（Node 用 `keytar`，Python 用 `keyring`）。**绝不明文落盘。** |

---

## Token audience 校验（规范强制）

只校验“这是不是一个有效的 bearer token”不够。规范要求校验“这个 token 是不是*为这个 server*签发的”，即 RFC 8707 audience。为 `api.other-service.com` 签发的 token 必须拒绝，哪怕签名验证通过。

**明确禁止 token 透传。** 不要收下 token 再原样转发给上游。如果你的 server 需要调用另一个服务，做 token 交换，或使用它自己的凭证。

---

## SDK 辅助工具 — 不要手搓

`@modelcontextprotocol/sdk/server/auth` 提供：
- `mcpAuthRouter()`，覆盖完整 OAuth AS 表面的 Express 路由（metadata、authorize、token）
- `bearerAuth`，用你的校验器验证 bearer token 的中间件
- `proxyProvider`，把认证转发给上游 IdP

如果要从零接线认证，先看这几个。
