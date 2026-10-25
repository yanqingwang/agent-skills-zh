---
name: build-mcp-server
description: 当用户要求 "build an MCP server"（构建 MCP server）、"create an MCP"（创建 MCP）、"make an MCP integration"（制作 MCP 集成）、"wrap an API for Claude"（为 Claude 封装 API）、"expose tools to Claude"（向 Claude 暴露 tools）、"make an MCP app"（制作 MCP 应用），或讨论使用 Model Context Protocol 构建某物时，应使用本 Skill。它是 MCP server 开发的入口——负责探询用户的使用场景、确定合适的部署模型（remote HTTP、MCPB、本地 stdio）、选定 tool 设计模式，并移交给专门的 Skill。
version: 0.1.0
---

> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 构建 MCP Server

你将引导一位开发者设计并构建一个能与 Claude 无缝协作的 MCP server。MCP server 形态多样——早期选错形态会导致后续痛苦的重写。你的第一要务是**探明需求，而非写代码**。

**先加载 Claude 特有的上下文。**MCP 规范是通用的；Claude 有额外的认证类型、审查标准和限制。在回答问题或搭建脚手架之前，先获取 `https://claude.com/docs/llms-full.txt`（Claude connector 文档的完整导出），让你的指导符合 Claude 的实际约束。

在拿到 Phase 1 中各问题的答案之前，不要开始搭建脚手架。如果用户的首条消息已经回答了这些问题，确认这一点后直接跳到推荐环节。

---

## Phase 1 — 探询使用场景

以对话方式提出这些问题（合并到一条消息里发出，不要一条一条地审问）。根据用户已经告诉你的内容调整措辞。

### 1. 它连接什么？

| 如果连接的是… | 可能的方向 |
|---|---|
| 云端 API（SaaS、REST、GraphQL） | Remote HTTP server |
| 本地进程、文件系统或桌面应用 | MCPB 或本地 stdio |
| 硬件、操作系统级 API 或用户特定状态 | MCPB |
| 不连接任何外部——纯逻辑 / 计算 | 两者皆可——默认 remote |

### 2. 谁会使用它？

- **只有我 / 我的团队，在我们自己的机器上** → 本地 stdio 可接受（最容易做原型）
- **任何安装它的人** → Remote HTTP（强烈推荐）或 MCPB（如果*必须*本地运行）
- **想要 UI 小组件的 Claude desktop 用户** → MCP app（remote 或 MCPB）

### 3. 它暴露多少个不同的操作？

这决定了 tool 设计模式——见 Phase 3。

- **约 15 个以内操作** → 每个操作一个 tool
- **数十到数百个操作**（例如封装一个大型 API 表面） → search + execute 模式

### 4. tool 是否需要调用中途的用户输入或富显示？

- **简单结构化输入**（从列表选择、输入一个值、确认）→ **Elicitation**——规范原生，零 UI 代码。*Host 支持正在逐步推出*（Claude Code ≥2.1.76）——务必搭配能力检查与降级方案。见 `references/elicitation.md`。
- **富 / 可视化 UI**（图表、带搜索的自定义选择器、实时仪表盘）→ **MCP app widgets**——基于 iframe，需要 `@modelcontextprotocol/ext-apps`。见 `build-mcp-app` skill。
- **都不是** → 返回文本 / JSON 的普通 tool。

### 5. 上游服务使用什么认证方式？

- 无 / API key → 简单直接
- OAuth 2.0 → 你需要一个支持 CIMD（首选）或 DCR 的 remote server；见 `references/auth.md`

---

## Phase 2 — 推荐部署模型

根据答案，推荐**一条**路径。要有明确倾向。按优先级排序的选项：

### ⭐ Remote streamable-HTTP MCP server（默认推荐）

一种通过 streamable HTTP 说 MCP 的托管服务。对于封装云端 API 的任何场景，这是**推荐路径**。

**为什么它胜出：**
- 零安装摩擦——用户添加一个 URL，即告完成
- 一次部署服务所有用户；升级由你掌控
- OAuth 流程可正常工作（server 能处理重定向、DCR、token 存储）
- 跨 Claude desktop、Claude Code、Claude.ai 及第三方 MCP host 工作

**除非** server *必须*触及用户本地机器，否则选这个。

→ **最快部署：** Cloudflare Workers — `references/deploy-cloudflare-workers.md`（两条命令从零到可用 URL）
→ **可移植的 Node/Python：** `references/remote-http-scaffold.md`（Express 或 FastMCP，可在任何主机上运行）

### Elicitation（结构化输入，无需构建 UI）

如果 tool 只需要用户确认、选择一项或填写一个简短表单，**elicitation** 可以零 UI 代码实现。server 发送一个扁平的 JSON schema；host 渲染原生表单。规范原生，无需额外包。

**注意：** Host 支持尚新（Claude Code 在 v2.1.76 中提供；Desktop 未确认）。如果客户端未声明该能力，SDK 会抛出异常。务必先检查 `clientCapabilities.elicitation` 并准备降级方案——标准模式见 `references/elicitation.md`。这是符合规范的正确做法；host 覆盖率会逐步跟上。

当你需要以下能力时，升级到 `build-mcp-app` widgets：嵌套 / 复杂数据、可滚动 / 可搜索的列表、可视化预览、实时更新。

### MCP app（remote HTTP + 交互式 UI）

同上，外加 **UI resources**——在聊天中渲染的交互式 widgets。带搜索的富选择器、图表、实时仪表盘、可视化预览。构建一次，即可在 Claude *和* ChatGPT 中渲染。

**当** elicitation 的扁平表单约束不适用时选择它——你需要自定义布局、大型可搜索列表、可视化内容或实时更新。

通常是 remote，但如果 UI 需要驱动本地应用，也可以以 MCPB 形式发布。

→ 移交给 **`build-mcp-app`** skill。

### MCPB（打包的本地 server）

**连同其运行时一起打包**的本地 MCP server，用户无需安装 Node/Python。发布本地 server 的官方认可方式。

**当** server *必须*运行在用户机器上时选择它——读取本地文件、驱动桌面应用、与 localhost 服务通信，或需要操作系统级访问。

→ 移交给 **`build-mcpb`** skill。

### 本地 stdio（npx / uvx）——*不推荐用于分发*

在用户机器上通过 `npx` / `uvx` 启动的脚本。适合**个人工具和原型**。分发起来很痛苦：用户需要正确的运行时，你无法推送更新，而且唯一的分发渠道是 Claude Code plugins。

只把它作为过渡跳板来推荐。如果用户坚持，就搭建脚手架，但注明 MCPB 升级路径。

---

## Phase 3 — 选定 tool 设计模式

每个 MCP server 都暴露 tools。如何切分它们比多数人预期的更重要——tool schema 会直接进入 Claude 的 context window。

### 模式 A：每个操作一个 tool（小表面）

当操作空间较小（< 约 15 个操作）时，为每个操作提供一个专属 tool，配以精炼的描述和 schema。

```
create_issue    — Create a new issue. Params: title, body, labels[]
update_issue    — Update an existing issue. Params: id, title?, body?, state?
search_issues   — Search issues by query string. Params: query, limit?
add_comment     — Add a comment to an issue. Params: issue_id, body
```

**为什么有效：** Claude 一次性读完 tool 列表，就确切知道能做什么。没有发现往返。每个 tool 的 schema 精确校验输入。

**特别适合** 一个或多个 tool 附带交互式 widget（MCP app）的情况——每个 widget 自然绑定一个 tool。

### 模式 B：Search + execute（大表面）

封装大型 API（数十到数百个端点）时，把每个操作都列成 tool 会淹没 context window 并降低模型性能。改为只暴露**两个** tools：

```
search_actions  — Given a natural-language intent, return matching actions
                  with their IDs, descriptions, and parameter schemas.
execute_action  — Run an action by ID with a params object.
```

server 在内部持有完整目录。Claude 搜索、挑选、执行。Context 保持精简。

**混合式：** 把最常用的 3–5 个操作提升为专属 tools，其余长尾保留在 search/execute 之后。

→ schema 示例与描述撰写指南见 `references/tool-design.md`。

---

## Phase 4 — 选定框架

推荐以下两者之一。其他框架也存在，但这两个的 MCP 规范覆盖度和 Claude 兼容性最好。

| 框架 | 语言 | 使用时机 |
|---|---|---|
| **官方 TypeScript SDK**（`@modelcontextprotocol/sdk`） | TS/JS | 默认选择。规范覆盖最好，最先获得新特性。 |
| **FastMCP 3.x**（PyPI 上的 `fastmcp`） | Python | 用户偏好 Python，或封装 Python 库。基于装饰器，样板代码极少。这是 jlowin 的包——不是官方 `mcp` SDK 中内置的已冻结的 FastMCP 1.0。 |

如果用户已有偏好的语言 / 技术栈，就随它——两者产生完全相同的线缆协议（wire protocol）。

---

## Phase 5 — 搭建脚手架并移交

四项决策（部署模型、tool 模式、框架、认证）敲定后，执行以下**其一**：

1. **Remote HTTP，无 UI** → 使用 `references/remote-http-scaffold.md`（可移植）或 `references/deploy-cloudflare-workers.md`（最快部署）内联搭建脚手架。本 skill 可以完成整个工作。
2. **MCP app（UI widgets）** → 总结迄今的决策，然后加载 **`build-mcp-app`** skill。
3. **MCPB（打包本地）** → 总结迄今的决策，然后加载 **`build-mcpb`** skill。
4. **本地 stdio 原型** → 内联搭建脚手架（最简情形），并标注 MCPB 升级路径。

移交时，用一段话重述设计概要，让下一个 skill 不必重新询问。

---

## Tools 之外——其他原语

Tools 是 server 三大原语之一。多数 server 从 tools 起步且从不需要其他原语，但知道它们的存在可以避免重复造轮子：

| 原语 | 触发者 | 使用时机 |
|---|---|---|
| **Resources** | Host 应用（非 Claude） | 把文档 / 文件 / 数据暴露为可浏览的上下文 |
| **Prompts** | 用户（斜杠命令） | 固化的工作流（"/summarize-thread"） |
| **Elicitation** | Server，tool 执行中途 | 向用户请求输入而无需构建 UI |
| **Sampling** | Server，tool 执行中途 | 在 tool 逻辑中需要 LLM 推理 |

→ `references/resources-and-prompts.md`、`references/elicitation.md`、`references/server-capabilities.md`

---

## Phase 6 — 在 Claude 中测试并发布

server 跑起来之后：

1. **在真实 Claude 中测试**：在 Settings → Connectors 把 server URL 添加为自定义 connector（本地 server 用 Cloudflare tunnel）。Claude 在 initialize 时以 `clientInfo.name: "claude-ai"` 标识自己。→ https://claude.com/docs/connectors/building/testing
2. **执行提交前检查清单**——读 / 写 tool 拆分、必需的 annotations、名称限制、提示词注入规则。→ https://claude.com/docs/connectors/building/review-criteria
3. **提交到 Anthropic Directory。** → https://claude.com/docs/connectors/building/submission
4. **建议同时发布一个 plugin**，用 skills 包装这个 MCP——多数合作伙伴两者都发布。→ https://claude.com/docs/connectors/building/what-to-build

---

## 速查：决策矩阵

| 场景 | 部署方式 | Tool 模式 |
|---|---|---|
| 封装小型 SaaS API | Remote HTTP | 每操作一个 tool |
| 封装大型 SaaS API（50+ 端点） | Remote HTTP | Search + execute |
| 带富表单 / 选择器的 SaaS API | MCP app（remote） | 每操作一个 tool |
| 驱动本地桌面应用 | MCPB | 每操作一个 tool |
| 带聊天内 UI 的本地桌面应用 | MCP app（MCPB） | 每操作一个 tool |
| 读写本地文件系统 | MCPB | 取决于表面大小 |
| 个人原型 | 本地 stdio | 哪个最快用哪个 |

---

## 参考文件

- `references/remote-http-scaffold.md` — TS SDK 和 FastMCP 的最小 remote server
- `references/deploy-cloudflare-workers.md` — 最快部署路径（Workers 原生脚手架）
- `references/tool-design.md` — 撰写 Claude 能很好理解的 tool 描述与 schema
- `references/auth.md` — OAuth、CIMD、DCR、token 存储模式
- `references/resources-and-prompts.md` — 两个非 tool 原语
- `references/elicitation.md` — 规范原生的 tool 中途用户输入（能力检查 + 降级方案）
- `references/server-capabilities.md` — instructions、sampling、roots、logging、progress、cancellation
- `references/versions.md` — 版本敏感声明台账（更新时核对）
