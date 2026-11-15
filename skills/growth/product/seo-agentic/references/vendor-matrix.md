> **中文汉化版** · 上游：[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) · 原文件：`skills/seo-agentic/references/vendor-matrix.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Agent 厂商矩阵（带日期、按来源分级）

变化快的事实只放在这里，本 skill 其他地方不重复。每行带来源分级：**P** = 一手（厂商文档、规范、源代码），**S** = 仅二手，**C** = 来源冲突。最近一次全面核查：**2026-09-23**。引用任何超过 60 天的行之前先刷新（见“刷新流程”）。

## 各 Agent 读什么，是否调用 WebMCP

| 厂商 / 产品 | 读取内容 | WebMCP | 身份 | 分级 |
|---|---|---|---|---|
| OpenAI：ChatGPT 桌面端内置浏览器（“site tools”） | ARIA / 无障碍树（publisher FAQ） | **是，仅命令式调用**，顶层文档，默认开启，Enterprise/Edu 不适用 | ChatGPT-User；用 Web Bot Auth 签署 agent 与云端浏览器流量 | P |
| OpenAI：云端浏览器（ChatGPT Work）、Codex | 同上 | 未有文档 | Web Bot Auth | S |
| Google：Chrome 中的 Gemini、Chrome auto browse | 页面元素与屏幕位置 | 无公开的消费证据；Google 参与共同编辑该规范 | Google-Agent（用户触发，一般无视 robots.txt）；正以 `https://agent.bot.goog` 试验 Web Bot Auth | P（身份），S（读取） |
| Microsoft：Edge、Copilot Mode | 未有文档 | Edge 支持 WebMCP 用于测试；无证据表明 Copilot 消费工具 | 未调研 | P（Edge），S（Copilot） |
| Anthropic：Chrome 中的 Claude（Claude Code、Cowork、Desktop）、computer use | 页面文本、DOM、控制台与网络、截图 | 无（公开 issue 报告发现能力缺失） | ClaudeBot、Claude-SearchBot、Claude-User；均遵守 robots.txt；IP 见 claude.com/crawling/bots.json | P（bot），S（读取） |
| Perplexity：Comet | 无障碍树与截图 | 无公开信号 | PerplexityBot 遵守 robots.txt；Perplexity-User 一般不遵守 | P（bot），S（读取） |
| Brave：Leo | 未有文档 | 实验性，Nightly 中藏于 `brave://flags/#enable-webmcp-testing` | 未验证 | S |
| Opera Neon、Dia、Sigma、Fellou | 未有文档 | 无公开信号 | 未验证 | S |
| Apple：Safari / WebKit | n/a | **反对**（Agent 更接近辅助技术；网站不应检测它们） | n/a | P（立场），S（引语） |
| Mozilla：Firefox | n/a | 中立；不实现 | n/a | P |

报告里要明说两个缺口：没有任何一手来源显示有消费级 Agent 发送过 `Accept: text/markdown`；Dia、Opera 和 Comet 的 agent 操作在 robots.txt 上如何表现，未经验证。

## 产品状态备注

| 项目 | 状态 | 分级 |
|---|---|---|
| ChatGPT Atlas 浏览器 | 据报道已于 2026-08-09 停止；ChatGPT agent 于 2026 年 8 月初移除 | S |
| ChatGPT Instant Checkout | 据报道于 2026-03 移入 Apps | S |
| Project Mariner | 据报道已于 2026-05-04 关闭 | S |
| Chrome WebMCP origin trial | M149 至 M156；未宣布发布里程碑 | P（区间），S（截止日 2026-11-17） |
| Lighthouse | 13.5.0（npm latest，2026-09-18）；PSI 运行 13.5.0 | P |
| Web Bot Auth | `draft-ietf-webbotauth-httpsig-protocol-00`（2026-09-01）；`Signature-Agent` 字典形式 | P |
| Content-Signal | Cloudflare CC0 政策；IETF 个人草案已于 2026-04-04 过期（P）；未找到 Google 表态，且 Google 的 robots.txt 规范未列出该字段（S） | P/S |
| MCP Server Card | SEP-2127 开放且未合并（更新于 2026-09-12） | P |

## 影响证据（厂商数字须打标）

- Cloudflare 关于 Markdown 的 token 缩减数字来自厂商。
- WebMCP 的“token 效率”百分比来自营销帖，无可追溯的基准。不要引用。
- WebArena 之类的 Agent 基准测的是模型，不是网站质量。
- 没有公开的对照研究把无障碍树质量或 WebMCP 与 agent 任务成功率关联起来。此类说法一律当作假设。

## 有争议或未验证（未经复核不得引用）

- WebKit 与 Mozilla 立场的确切日期，以及 WebKit 引语（二手追踪来源，其中之一由自动化 agent 撰写）。去查 GitHub 时间线。
- WebKit 关于新工作组或 TPAC 研讨会的提议（仅有厂商追踪来源的转述）。
- Anthropic 与 Perplexity 的 Web Bot Auth 签名（仅二手）。
- Cloudflare 对字典形式 `Signature-Agent` 的验证（有报告称不匹配，未经测试）。
- Content-Signal 是否按 robots.txt 组限定生效（无规范性文本）。
- ChatGPT site-tools 的模型要求（厂商页面相互矛盾）。

## 刷新流程

1. PSI：运行 `lighthouse_agentic.py https://claude-seo.md/ --json`。若 `lighthouse_version` 有变，把该分类的 `auditRefs` 与 `references/lighthouse-agentic-category.md` 做 diff。
2. Lighthouse 源码：`npm view lighthouse version`，然后读 `core/config/default-config.js` 和 `core/audits/agentic/` 看新 tag。
3. WebMCP：规范的最后一次 commit（webmachinelearning/webmcp）、chromestatus feature 5117755740913664、learn.chatgpt.com/docs/webmcp。
4. Bot：developers.openai.com/api/docs/bots、support.claude.com 的 crawler 文章、docs.perplexity.ai/guides/bots、Google 的 user-triggered fetchers 页面。
5. 草案：datatracker.ietf.org 查 webbotauth 与 aipref。
6. 在同一次变更里更新本文件的日期和 `agentic_check.py` 中的 `CHECKED_ON` 常量。
