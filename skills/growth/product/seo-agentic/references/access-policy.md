> **中文汉化版** · 上游：[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) · 原文件：`skills/seo-agentic/references/access-policy.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Agent 访问策略：robots.txt、Content-Signal、WAF、Web Bot Auth

以下事实核查于 2026-09-23，以厂商文档为准，标注 secondary 的除外。robots.txt 是**偏好信号，不是访问控制**：多个由用户触发的 agent 并不把它当作约束，TollBit 的 State of the Bots 报告（secondary）发现有相当比例的 AI 抓取器访问了 disallow 的 URL。用身份认证保护私有路径。

## 按用途划分的 User-agent 令牌

检查与你主张相关的那个 bot。爬虫角色与可引用性规则在 `seo-geo` 中；本表补充对 agent 重要的部分。

| Token | 厂商 | 用途 | robots.txt（厂商文档） | 验证途径 |
|---|---|---|---|---|
| GPTBot | OpenAI | 模型训练 | 遵守 | openai.com/gptbot.json |
| OAI-SearchBot | OpenAI | ChatGPT 搜索索引 | 遵守 | openai.com/searchbot.json |
| ChatGPT-User | OpenAI | 用户发起的抓取与操作 | "may not apply" | openai.com/chatgpt-user.json；Web Bot Auth |
| OAI-AdsBot | OpenAI | 广告落地页检查 | 见厂商文档 | openai.com/adsbot.json |
| ClaudeBot | Anthropic | 模型训练 | 遵守（含 Crawl-delay） | claude.com/crawling/bots.json |
| Claude-SearchBot | Anthropic | Claude 搜索结果可引用性 | 遵守 | claude.com/crawling/bots.json |
| Claude-User | Anthropic | 用户发起的抓取 | 遵守 | claude.com/crawling/bots.json |
| PerplexityBot | Perplexity | 搜索索引 | 遵守 | perplexity.com/perplexitybot.json |
| Perplexity-User | Perplexity | 用户发起的抓取 | 通常忽略 | perplexity.com/perplexity-user.json |
| Google-Agent | Google | 用户触发的 agent 抓取 | 通常忽略 | developers.google.com/static/crawling/ipranges/user-triggered-agents.json |
| Google-Extended | Google | Gemini 训练/grounding（以及 Search 生成式 AI 模型训练）的控制令牌，不是爬虫；从不影响 Search 收录 | 遵守 | n/a |

Anthropic 的帮助中心曾说 IP 段未公开；截至 2026-08，它们已发布在 `claude.com/crawling/bots.json`。不要 IP 封禁 Anthropic 的爬虫：被封禁的爬虫根本读不到 robots.txt。

## RFC 9309 分组选择（最常见的错误）

爬虫**只**遵守点名它 token 的最具体分组。只要有任何分组点名了它，`*` 组对它就整体失效。所以放在 `User-agent: *` 里的行，在存在 `User-agent: GPTBot` 组时不会作用到 `GPTBot`。

这对 `Content-Signal` 很关键。Cloudflare 托管的 robots.txt 把它放在 `*` 组里，而没有任何规范性文本说它能绕过分组选择。当站点存在具名分组时，把该行在每个分组里重复一遍。`agentic_fix.py robots` 正是这样做的，且从不改动 Allow/Disallow。

Token 匹配不区分大小写，且按整词比较（RFC 9309 第 2.2.1 节）：`GPTBot` 不会选中 `GPTBot-Image` 组。`GPTBot/1.1` 或 `ClaudeBot*` 超出了 RFC 的 token 语法（字母、`_`、`-`）。Google 文档说明它会忽略多余文本；`agentic_check.py` 同样如此，并把这类行列为 `nonstandard_user_agent_lines`。推荐裸 token，因为其他爬虫可能更严格（读取于 2026-11-10）。

robots.txt 返回 5xx 时，合规爬虫会把站点视为完全禁止访问。4xx 表示"无限制"，但 429 例外：RFC 9309 没有单独点名它，但 Google 把它当服务器错误处理，而不是当作文件缺失。此时 `agentic_check.py` 会把 `robots-reachable` 报告为不确定。

## Content-Signal

语法：`Content-Signal: search=yes, ai-input=yes, ai-train=no`。

| 键 | 含义 |
|---|---|
| `search` | 建立搜索索引并展示链接/摘要（不含 AI 摘要） |
| `ai-input` | 把内容用作 AI 回答的输入（RAG、grounding） |
| `ai-train` | 训练或微调模型 |
| `use` | 实验性的 Cloudflare 字段（`immediate`、`reference`、`full`）；Cloudflare 托管默认值包含 `use=reference`（文档未给出日期） |

状态：Cloudflare 的 CC0 Content Signals Policy（2025-09-24 上线）。IETF 个人草案 `draft-romm-aipref-contentsignals` 已于 2026-04-04 过期；IETF AIPREF 工作组的词汇表（`draft-ietf-aipref-vocab`）尚未达成共识。我们没有找到 Google 关于 Content-Signal 的表态；Google 的 robots.txt 规范只列出它支持的字段，这不是其中之一。把它作为"已声明但无确认效果"的偏好来呈现。

## 示例 robots.txt（欢迎 agent 和搜索，不允许训练）

```
User-agent: *
Content-Signal: search=yes, ai-input=yes, ai-train=no
Allow: /

User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
Content-Signal: search=yes, ai-input=yes, ai-train=no
Allow: /

User-agent: GPTBot
User-agent: ClaudeBot
User-agent: Google-Extended
Content-Signal: search=yes, ai-input=yes, ai-train=no
Disallow: /

Sitemap: https://example.com/sitemap.xml
```

封禁训练爬虫是商业决策。绝不要默认推荐它，也绝不要把它说成会影响 Google 搜索。Google-Agent 不需要写行，因为它通常忽略 robots.txt；把 `/checkout/` 和 `/account/` 放到身份认证之后。

## WAF 与 bot 管理

- 允许**已验证**的 bot 和签名 agent，而不是看 user-agent 字符串。Cloudflare、AWS WAF、Akamai、HUMAN 和 Vercel 都支持验证 Web Bot Auth 或已发布的 IP 段；Perplexity 文档化了 WAF 配方。
- 不要在内容和信息类页面上放 CAPTCHA 和挑战页。
- WAF 挑战一个携带 `GPTBot` 但未验证的请求，是在正确行事。`agentic_check.py --ua-matrix` 展示未验证流量如何被对待；再到 WAF 日志里确认真实 agent 的行为。

## Web Bot Auth

Agent 如何证明身份：HTTP Message Signatures（RFC 9421）、Ed25519 密钥、位于 `/.well-known/http-message-signatures-directory` 的密钥目录（`application/http-message-signatures-directory+json`），以及 `tag="web-bot-auth"`。

- 当前草案：`draft-ietf-webbotauth-httpsig-protocol-00`（2026-09-01），取代此前的 Meunier 个人草案。
- `Signature-Agent` 现在是**以签名标签为键的 dictionary**，例如 `Signature-Agent: sig1="https://signer.example"`。裸字符串形式已过时，但部分验证方可能仍在期待它，依赖前先测试。
- 已报告的签名方：OpenAI（agent 与云浏览器流量）、Google（实验性，`https://agent.bot.goog`）、Amazon Bedrock AgentCore、Shopify。Anthropic 与 Perplexity 的签名仅见于 secondary 来源。

站点所有者除非自己运营 agent，否则不发布密钥目录。他们在边缘验证签名。

## 报告规则

- 训练、搜索、用户抓取三类访问分开各占一行报告。
- Content-Signal 和 Web Bot Auth 标注为草案或政策，并附核查日期。
- 绝不承诺任何 robots 变更会带来排名、引用或流量效果。
