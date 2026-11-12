> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-server/references/remote-http-scaffold.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 远程 Streamable-HTTP MCP Server — 脚手架

两个推荐框架下的最小可运行 server。从这里开始，然后再添加 tools。

---

## TypeScript SDK（`@modelcontextprotocol/sdk`）

```bash
npm init -y
npm install @modelcontextprotocol/sdk zod express
npm install -D typescript @types/express @types/node tsx
```

**`src/server.ts`**

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import express from "express";
import { z } from "zod";

const server = new McpServer(
  { name: "my-service", version: "0.1.0" },
  { instructions: "Prefer search_items before calling get_item directly — IDs aren't guessable." },
);

// Pattern A: one tool per action
server.registerTool(
  "search_items",
  {
    description: "Search items by keyword. Returns up to `limit` matches ranked by relevance.",
    inputSchema: {
      query: z.string().describe("Search keywords"),
      limit: z.number().int().min(1).max(50).default(10),
    },
    annotations: { readOnlyHint: true },
  },
  async ({ query, limit }, extra) => {
    // extra.signal is an AbortSignal — check it in long loops for cancellation
    const results = await upstreamApi.search(query, limit);
    return {
      content: [{ type: "text", text: JSON.stringify(results, null, 2) }],
    };
  },
);

server.registerTool(
  "get_item",
  {
    description: "Fetch a single item by its ID.",
    inputSchema: { id: z.string() },
    annotations: { readOnlyHint: true },
  },
  async ({ id }) => {
    const item = await upstreamApi.get(id);
    return { content: [{ type: "text", text: JSON.stringify(item) }] };
  },
);

// Streamable HTTP transport (stateless mode — simplest)
const app = express();
app.use(express.json());

app.post("/mcp", async (req, res) => {
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: undefined, // stateless
  });
  res.on("close", () => transport.close());
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});

app.listen(process.env.PORT ?? 3000);
```

**无状态 vs 有状态：** 上面的代码片段为每个请求新建一个 transport（无状态）。对多数封装 API 的 server 来说这就够了。如果 tools 确实需要在一个会话内跨调用共享状态（少见），使用按会话键索引的 transport 映射，参见 SDK 的 `examples/server/simpleStreamableHttp.ts`。

---

## FastMCP 3.x（Python）

```bash
pip install fastmcp
```

**`server.py`**

```python
from fastmcp import FastMCP

mcp = FastMCP(
    name="my-service",
    instructions="Prefer search_items before calling get_item directly — IDs aren't guessable.",
)

@mcp.tool(annotations={"readOnlyHint": True})
def search_items(query: str, limit: int = 10) -> list[dict]:
    """Search items by keyword. Returns up to `limit` matches ranked by relevance."""
    return upstream_api.search(query, limit)

@mcp.tool(annotations={"readOnlyHint": True})
def get_item(id: str) -> dict:
    """Fetch a single item by its ID."""
    return upstream_api.get(id)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=3000)
```

FastMCP 从类型标注推导 JSON schema，docstring 则成为 tool 的 description。docstring 要简短、面向动作，它们会原封不动地进入 Claude 的 context window。

---

## Search + execute 模式（大型 API 表面）

封装 50 个以上端点时，不要全部注册成 tools。只用两个：

```typescript
const CATALOG = loadActionCatalog(); // { id, description, paramSchema }[]

server.registerTool(
  "search_actions",
  {
    description: "Find available actions matching an intent. Call this first to discover what's possible. Returns action IDs, descriptions, and parameter schemas.",
    inputSchema: { intent: z.string().describe("What you want to do, in plain English") },
    annotations: { readOnlyHint: true },
  },
  async ({ intent }) => {
    const matches = rankActions(CATALOG, intent).slice(0, 10);
    return { content: [{ type: "text", text: JSON.stringify(matches, null, 2) }] };
  },
);

server.registerTool(
  "execute_action",
  {
    description: "Execute an action by ID. Get the ID and params schema from search_actions first.",
    inputSchema: {
      action_id: z.string(),
      params: z.record(z.unknown()),
    },
  },
  async ({ action_id, params }) => {
    const action = CATALOG.find(a => a.id === action_id);
    if (!action) throw new Error(`Unknown action: ${action_id}`);
    validate(params, action.paramSchema);
    const result = await dispatch(action, params);
    return { content: [{ type: "text", text: JSON.stringify(result) }] };
  },
);
```

起步阶段 `rankActions` 用简单的关键词匹配即可。如果精度要求高，再升级到 embeddings。

---

## 测试

MCP Inspector 可以连接任何 transport，让你交互式地摆弄 tools。

```bash
# Interactive — opens a UI on localhost:6274
npx @modelcontextprotocol/inspector
# → select "Streamable HTTP", paste http://localhost:3000/mcp, Connect
```

脚本化检查（CI、冒烟测试）：

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3000/mcp \
  --transport http --method tools/list

npx @modelcontextprotocol/inspector --cli http://localhost:3000/mcp \
  --transport http --method tools/call --tool-name search_items --tool-arg query=test
```

---

## 用户接入

部署完成后，用户直接添加 URL 即可，没有安装步骤。

| 使用端 | 接入方式 |
|---|---|
| **Claude Code** | `claude mcp add --transport http <name> <url>`（全局加 `--scope user`，需要认证时加 `--header "Authorization: Bearer ..."`） |
| **Claude Desktop / Claude.ai** | Settings → Connectors → Add custom connector。**不是** `claude_desktop_config.json`，配置在那里的 remote server 会被忽略。 |
| **Connector directory** | Anthropic 提供提交指南，用于进入公开 connector 目录。 |

---

## 部署

**最快路径：** Cloudflare Workers，免费档两条命令就能从零拿到可用的 `https://` URL。使用 Workers 原生脚手架（不是 Express）。→ `deploy-cloudflare-workers.md`

**这套 Express 脚手架**可运行在任何 Node 主机上：Render、Railway、Fly.io、VPS。容器化（`node:20-slim`、复制、`npm ci`、`node dist/server.js`）后即可上线。FastMCP 同理，换用 Python 基础镜像。

---

## 部署检查清单

- [ ] `POST /mcp` 对 `initialize` 请求返回 server capabilities
- [ ] `tools/list` 返回你的 tools，schema 完整
- [ ] 错误返回结构化 MCP 错误，而不是带 HTML 正文的 HTTP 500
- [ ] 如果会有浏览器客户端连接，设置好 CORS 头
- [ ] 在 `/mcp` 上校验 `Origin` 头（规范强制要求，防 DNS rebinding）
- [ ] 遵守 `MCP-Protocol-Version` 头（不支持的版本返回 400）
- [ ] 如果 tool 使用需要提示，设置 `instructions` 字段
- [ ] 健康检查端点与 `/mcp` 分开（主机会轮询它）
- [ ] 密钥来自环境变量，绝不硬编码
- [ ] 如果用 OAuth：实现 CIMD 或 DCR 端点，见 `auth.md`
