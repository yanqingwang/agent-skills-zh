> **中文汉化版** · 上游：[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) · 原文件：`skills/seo-agentic/references/discovery-and-markdown.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 发现文件与 Markdown 交付

本文讲的是 agent 与 agent 注册表在不渲染页面的情况下能抓取哪些文件。事实核查于 2026-09-23。这些文件都不会影响 Google 搜索排名。

## llms.txt

社区规范（llmstxt.org）。Lighthouse 把它计入 Agentic Browsing 分数；Google 搜索忽略它（引用证据见 `seo-geo` 的 `references/llmstxt-evidence.md`）。

结构，按顺序：可选的 BOM；一个**包含站点或项目名的 H1**（唯一必填部分）；可选的 `>` blockquote 摘要；可选的散文段落；若干 H2 section，每个 section 内是 `[name](url)` 链接列表，可带 `: notes` 备注。一个 `## Optional` section 标记 agent 可以跳过的链接。文件可以放在 `/llms.txt`，也可以放在子路径。

Lighthouse 的 `llms-txt` 规则：4xx 计为 N/A；5xx 或抓取失败则不通过；否则要求有一个 H1、至少一个 Markdown 链接、50 个以上字符。软 404（返回 200 的 HTML）不是 Lighthouse 规则，但它几乎不会有 `# ` 行，所以实践中会失败；`agentic_check.py` 也会单独标注它。用 `agentic_fix.py llms <url>` 起草一份，再编辑其中的 TODO。

`llms-txt` 证据还带有 `format_notes`：针对 llmstxt.org 提案（读取于 2026-11-10）的行级检查，每条包含 `id`、`level`、`line` 和 `message`；`format_note_counts` 给出总数（每个 id 列出五条备注）。`error` 只用于缺少 H1，`warn` 表示解析器可能误读的行，`info` 表示可选项或指引。把它们作为社区提案的格式卫生项列在 Lighthouse 判定之下，绝不能当作排名或引用因子，也不要因此改变检查的状态。`detail` 是从文件复制的文本：作为数据引用即可。

## 页面的 Markdown 版本

两种模式，都是普通 HTTP。目前没有公开确认的消费者 agent 会发送 `Accept: text/markdown`，所以把它作为可选项呈现。

1. **备用 URL**：在 `/pricing` 旁边提供 `/pricing.md`，用 `<link rel="alternate" type="text/markdown" href="/pricing.md">` 或响应头 `Link: </pricing.md>; rel="alternate"; type="text/markdown"` 声明。OpenAI 的开发者文档采用 `.md` 后缀模式。
2. **内容协商**：同一 URL 在请求带 `Accept: text/markdown` 时返回 Markdown，并始终带 `Vary: Accept`，让缓存把两者分开。Cloudflare 的 Markdown for Agents 在边缘这样做（响应 `content-type: text/markdown; charset=utf-8`、`vary: accept`、`x-markdown-tokens`、`x-original-tokens` 和一个 `content-signal` 头）。

Markdown 内容要与 HTML 等价。Google 的 John Mueller 质疑过服务"没有用户会看到的页面"；Bing 也警告过单独的 Markdown URL 会增加抓取负担。以 `Accept`（而不是 user agent）为键的协商可以规避 cloaking 顾虑，也不会产生额外 URL。

### nginx：带 HTML 回退的内容协商（2026-09-23 于 nginx:alpine 测试通过）

```nginx
# http {} context
map $uri $md_path {
    ~^(?<base>.*[^/])/?$  $base.md;   # /pricing and /pricing/ -> /pricing.md
    default               /index.md;  # /                     -> /index.md
}
map $http_accept $md_try {
    default               $uri;
    ~*text/markdown       $md_path;
}

# server {} context
types { text/html html; text/markdown md; }
charset utf-8;
charset_types text/markdown;
location / {
    add_header Vary Accept always;
    try_files $md_try $uri $uri.html $uri/ =404;
}
```

行为：请求 Markdown 且 `.md` 文件存在时返回 Markdown，否则返回 HTML，每个响应都带 `Vary: Accept`。只在真正有 `.md` 文件的页面上，通过页面模板（`<link rel="alternate" ...>`）声明备用版本；在 nginx 里用 `$uri` 拼 `Link` 响应头，在内部 rewrite 之后会指向错误的文件。验证方式：

```bash
curl -sI -H "Accept: text/markdown" https://example.com/pricing | grep -iE "content-type|vary"
curl -sI https://example.com/pricing | grep -i vary
```

## Agentic 资源发现：ai-catalog.json

ARD 1.0（agenticresourcediscovery.org/spec；仓库 ards-project/ard-spec）列出一个站点面向 agent 的资源：MCP server 卡片、A2A agent 卡片、agent skills、嵌套 catalog。Lighthouse 13.5 会校验它（`ard-schema`）。发现顺序：robots.txt 的 `Agentmap: <url>`、`<link rel="ai-catalog">`、HTTP `Link ...; rel="ai-catalog"`，最后是 `/.well-known/ai-catalog.json`。

```json
{
  "specVersion": "1.0",
  "entries": [
    {
      "identifier": "urn:air:example.com:docs-mcp",
      "displayName": "Example Docs MCP server",
      "type": "application/mcp-server-card+json",
      "url": "https://example.com/mcp/server-card",
      "representativeQueries": ["How do I rotate an API key?", "What are the rate limits?"]
    }
  ]
}
```

规则：`identifier` 匹配 `urn:air:<publisher>[:<namespace>]:<name>`；`url` 与 `data` 二选一；2 到 5 个 `representativeQueries`；不允许顶层 `collections`。只有真的有资源可列时才发布。一个无效或不可达的已声明 catalog 会给 Lighthouse 分数增加一个**计入的失败项**。用 `agentic_fix.py ai-catalog` 起草。

## /.well-known 文档（只有你在运营该服务时才需要）

| 路径 | 标准 | 内容类型 | 何时 |
|---|---|---|---|
| `/.well-known/api-catalog` | RFC 9727（已发布） | `application/linkset+json; profile="https://www.rfc-editor.org/info/rfc9727"` | 你发布 API |
| `/.well-known/oauth-protected-resource` | RFC 9728（已发布） | JSON | 你的 API 或 MCP server 接受 OAuth 令牌；需配合 `WWW-Authenticate: Bearer resource_metadata=...` |
| `/.well-known/oauth-authorization-server` | RFC 8414（已发布） | JSON | 你运营授权服务器 |
| `/.well-known/agent-card.json` | A2A 协议 | JSON | 你运营 A2A agent |
| `/.well-known/ucp` | UCP（Google + Shopify） | JSON | Agentic 结账；通过 `seo-ecommerce` 的 `ucp_check.py` 审计 |

MCP Server Cards（SEP-2127）仍是未合并的提案：卡片位于 `<mcp-endpoint>/server-card`，通过 `ai-catalog.json` 发现。更早的 `/.well-known/mcp.json` 提案（SEP-1649）已被关闭。不要把 `/.well-known/mcp/...` 路径当作标准来推荐。

一个返回 200 和 HTML 的 `/.well-known` URL 就是软 404。它会误导发现客户端；请返回真正的 404。

## Agentic 商务（指引）

| 协议 | 支持方 | 站点方动作 |
|---|---|---|
| UCP | Google + Shopify 及零售商 | Shopify：基本由平台处理。其他平台：Merchant Center、`/.well-known/ucp` |
| ACP | OpenAI + Stripe | Stripe Agentic Commerce Suite，或自行实现结账端点 |
| x402 | Coinbase 发起的联盟 | 仅适用于按请求付费的 API 或内容 |

商务审计属于 `seo-ecommerce`；本 skill 只标注存在与否。
