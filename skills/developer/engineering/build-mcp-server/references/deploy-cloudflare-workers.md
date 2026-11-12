> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-server/references/deploy-cloudflare-workers.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 部署到 Cloudflare Workers

从零到可用的 `https://` MCP URL 的最快路径。免费档即可开始，无需信用卡，两条命令完成部署。

**取舍：** 这是 Workers 原生脚手架，不是 `remote-http-scaffold.md` 中 Express 脚手架的部署目标，两者运行时不同。需要跨主机可移植就继续用 Express；只想尽快上线，就从这里开始。

---

## 初始化

```bash
npm create cloudflare@latest -- my-mcp-server \
  --template=cloudflare/ai/demos/remote-mcp-authless
cd my-mcp-server
```

这会拉取一个最小模板，带齐依赖（`agents`、`zod`）和一份可用的 `wrangler.jsonc`。

---

## `src/index.ts`

把模板的计算器示例换成你的 tools。使用 `registerTool()`（与 Express 脚手架相同的 API，`McpServer` 实例完全一样）：

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { McpAgent } from "agents/mcp";
import { z } from "zod";

export class MyMCP extends McpAgent {
  server = new McpServer(
    { name: "my-service", version: "0.1.0" },
    { instructions: "Prefer search_items before get_item — IDs aren't guessable." },
  );

  async init() {
    this.server.registerTool(
      "search_items",
      {
        description: "Search items by keyword. Returns up to `limit` matches.",
        inputSchema: {
          query: z.string().describe("Search keywords"),
          limit: z.number().int().min(1).max(50).default(10),
        },
        annotations: { readOnlyHint: true },
      },
      async ({ query, limit }) => {
        const results = await upstreamApi.search(query, limit);
        return { content: [{ type: "text", text: JSON.stringify(results, null, 2) }] };
      },
    );
  }
}

export default {
  fetch(request: Request, env: Env, ctx: ExecutionContext) {
    const url = new URL(request.url);
    if (url.pathname === "/mcp") {
      return MyMCP.serve("/mcp").fetch(request, env, ctx);
    }
    return new Response("Not found", { status: 404 });
  },
};
```

`McpAgent` 是 Cloudflare 的包装层，负责 streamable-HTTP transport、会话路由和 Durable Object 管道。你的代码只接触 `this.server`，它就是 SDK 里同一个 `McpServer` 类。`tool-design.md` 和 `server-capabilities.md` 中的内容原样适用。

---

## `wrangler.jsonc`

模板自带这份配置。Durable Objects 块是**样板代码**，`McpAgent` 用 DO 存会话状态，你不需要直接操作它。

```jsonc
{
  "name": "my-mcp-server",
  "main": "src/index.ts",
  "compatibility_date": "2025-03-10",
  "compatibility_flags": ["nodejs_compat"],
  "migrations": [{ "new_sqlite_classes": ["MyMCP"], "tag": "v1" }],
  "durable_objects": {
    "bindings": [{ "class_name": "MyMCP", "name": "MCP_OBJECT" }]
  }
}
```

如果你重命名 `MyMCP` 类，把 `new_sqlite_classes` 和 `class_name` 一起改成一致。

---

## 运行与部署

```bash
npx wrangler dev     # → http://localhost:8787/mcp
npx wrangler deploy  # → https://my-mcp-server.<account>.workers.dev/mcp
```

`wrangler deploy` 会打印线上 URL。用户粘贴进 Claude 的就是它。

密钥（上游 API key）：`npx wrangler secret put UPSTREAM_API_KEY`，然后在 `init()` 里读 `env.UPSTREAM_API_KEY`。

---

## OAuth

Cloudflare 提供 `@cloudflare/workers-oauth-provider`，一个即插即用组件，处理授权服务器一侧（CIMD/DCR 端点、token 签发、同意界面）。它包装你的 `McpAgent`，把 `/mcp` 置于 token 检查之后。协议细节见 `auth.md`；CF 模板 `cloudflare/ai/demos/remote-mcp-github-oauth` 展示了接线方式。
