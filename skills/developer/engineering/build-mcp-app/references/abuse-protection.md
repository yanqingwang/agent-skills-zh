> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-app/references/abuse-protection.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 无鉴权托管服务器的滥用防护

无鉴权的 StreamableHTTP 服务器，internet 上谁都能访问。要保护三种资源：你的算力、工具消耗的上游 API 配额，以及大体积 `callServerTool` 载荷占用的出口带宽。

## 拿不到每用户身份

无鉴权模式下没有 token，无状态传输也不给会话 ID。来自 claude.ai 的流量经 Anthropic 出口代理：每个 web 用户都从同一小段 IP 段过来：

```
160.79.104.0/21
2607:6bc0::/48
```

（见 https://platform.claude.com/docs/en/api/ip-addresses。）

Claude Desktop、Claude Code 和其他宿主**直接从用户机器**连接，这些确实有各自不同的用户 IP。所以按 IP 限流对直连客户端有效；对 claude.ai 只能限制 Anthropic 池子的总量。真需要每用户级别的限额，那就是该加 OAuth 的信号。

## 分层令牌桶（每副本兜底）

```ts
const ANTHROPIC_CIDRS = ["160.79.104.0/21", "2607:6bc0::/48"];
const TIERS = {
  anthropic: { capacity: 600, refillPerSec: 100 }, // shared pool
  other:     { capacity: 30,  refillPerSec: 2   }, // per-IP
};
```

把 `req.ip` 与这些 CIDR 匹配，选一个桶（`"anthropic"` 或 `"ip:<addr>"`），耗尽时返回 429 + `Retry-After`。这只是每副本的兜底：跨副本的执行要放在边缘层（Cloudflare、Cloud Armor），这样容器才能保持无状态。

## `trust proxy` 必须匹配你的拓扑

只有设置了 `app.set('trust proxy', N)`，`req.ip` 才会认 `X-Forwarded-For`。设 `true` 等于信任每一跳，直连客户端就能伪造 `X-Forwarded-For: 160.79.108.42`、冒充 Anthropic 层。把它设成可信跳数的精确值（比如单个 LB 后面设 `1`，Cloudflare → 源站 LB 后面设 `2`），生产环境**绝不设 `true`**。

## 硬白名单 Anthropic IP 是产品决策

拦掉 `160.79.104.0/21` 之外的一切，会把 Desktop、Claude Code 和所有其他 MCP 宿主一并锁在外面。这些 CIDR 用来给限流**分层**，不用来把门，除非"只服务 claude.ai"就是明确目标。

## 缓存上游响应

包装第三方 API 的工具，第一道成本控制是进程内 LRU 缓存，以归一化后的查询为键（TTL 数小时，键里不含秘密）：重复查询变为免费，还能吸收惊群。限流是安全网，不是第一道防线。
