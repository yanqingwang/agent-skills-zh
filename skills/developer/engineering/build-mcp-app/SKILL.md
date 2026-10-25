---
name: build-mcp-app
description: 当用户想要构建 "MCP app"（MCP 应用）、为 MCP server 添加 "interactive UI"（交互式 UI）或 "widgets"（小部件）、"render components in chat"（在对话中渲染组件）、构建 "MCP UI resources"（MCP UI 资源）、制作在对话中内联展示 "form"（表单）、"picker"（选择器）、"dashboard"（仪表盘）或 "confirmation dialog"（确认对话框）的工具，或在 MCP 语境下提到 "apps SDK" 时，应使用本技能。在 build-mcp-server 技能已确定部署模型之后再使用；或当用户已明确知道自己想要 UI 小部件时使用。
version: 0.1.0
---

> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 构建 MCP App（交互式 UI 小部件）

MCP app 是一个**同时提供 UI 资源**的标准 MCP server——即内联渲染在聊天界面中的交互式组件。构建一次，即可同时运行在 Claude *和* ChatGPT 以及任何实现了 apps surface 的宿主中。

UI 层是**增量式的**。底层仍然是 tools、resources 和相同的线上协议（wire protocol）。如果你还没有构建过普通的 MCP server，`build-mcp-server` 技能覆盖了这一基础层；本技能在其上添加小部件。

> **在 Claude 中测试：** 将 server 作为自定义 connector 添加到 claude.ai（本地开发时经由 Cloudflare tunnel）——这会走真实的 iframe sandbox 和 `hostContext`。参见 https://claude.com/docs/connectors/building/testing。

## Claude 宿主专属细节

| `_meta.ui.*` 键 | 位置 | 效果 |
|---|---|---|
| `resourceUri` | tool | 宿主为该工具的结果渲染哪个 `ui://` 资源。 |
| `visibility: ["app"]` | tool | 隐藏仅供小部件使用的辅助工具（例如通过 `callServerTool` 调用的几何/图片获取器），使其不出现在 Claude 的工具列表中。 |
| `prefersBorder: false` | resource | 去掉宿主的外层卡片边框（移动端）。 |
| `csp.{connectDomains, resourceDomains, baseUriDomains}` | resource | 声明外部来源；默认全部阻止。`frameDomains` 目前在 Claude 中受限。 |

- `hostContext.safeAreaInsets: {top, right, bottom, left}`（px）——为刘海屏和输入框浮层留出空间时请遵守这些值。
- 目录提交要求 OAuth 或 **authless**（`none`）——静态 bearer 仅适用于私有部署，且会导致无法上架——此外还需工具 `annotations` 和 3–5 张 PNG 截图；参见 `references/directory-checklist.md`。

---

## 什么时候小部件优于纯文本

不要为了 UI 而 UI——大多数工具返回文本或 JSON 就够了。满足以下任一条件时才添加小部件：

| 信号 | 小部件类型 |
|---|---|
| 工具需要 Claude 无法可靠推断的结构化输入 | 表单 |
| 用户必须从 Claude 无法排序的列表中挑选（文件、联系人、记录） | 选择器 / 表格 |
| 破坏性或计费操作需要显式确认 | 确认对话框 |
| 输出是空间性或视觉性的（图表、地图、diff、预览） | 展示型小部件 |
| 用户想盯着的长时间运行任务 | 进度 / 实时状态 |

如果都不满足，就跳过小部件。文本构建更快，用户用起来也更快。

---

## 小部件 vs Elicitation——正确路由

构建小部件之前，先检查 **elicitation** 是否已能覆盖需求。Elicitation 是协议原生能力，零 UI 代码，可在任何合规宿主中工作。

| 需求 | Elicitation | 小部件 |
|---|---|---|
| 确认是/否 | ✅ | 杀鸡用牛刀 |
| 从短枚举中挑选 | ✅ | 杀鸡用牛刀 |
| 填写扁平表单（姓名、邮箱、日期） | ✅ | 杀鸡用牛刀 |
| 从大型/可搜索列表中挑选 | ❌（不支持滚动/搜索） | ✅ |
| 选择前的可视化预览 | ❌ | ✅ |
| 图表 / 地图 / diff 视图 | ❌ | ✅ |
| 实时更新的进度 | ❌ | ✅ |

如果 elicitation 能覆盖，就用它。参见 `../build-mcp-server/references/elicitation.md`。

---

## 架构：两种部署形态

### 远程 MCP app（最常见）

托管式 streamable-HTTP server。小部件模板以 **resource** 形式提供，工具结果引用它们。宿主拉取该资源，在 iframe sandbox 中渲染，并在小部件与 Claude 之间转发消息。

```
┌──────────┐  tools/call   ┌────────────┐
│  Claude  │─────────────> │ MCP server │
│   host   │<── result ────│  (remote)  │
│          │  + widget ref │            │
│          │               │            │
│          │ resources/read│            │
│          │─────────────> │  widget    │
│ ┌──────┐ │<── template ──│  HTML/JS   │
│ │iframe│ │               └────────────┘
│ │widget│ │
│ └──────┘ │
└──────────┘
```

### MCPB 打包的 MCP app（本地 + UI）

小部件机制相同，但 server 在 MCPB bundle 内本地运行。当小部件需要驱动**本地**应用时使用——例如浏览真实本地磁盘的文件选择器、控制桌面应用的对话框。

MCPB 打包的具体操作以 **`build-mcpb`** 技能为准。以下所有内容对两种形态均适用。

---

## 小部件如何挂接到工具

一个支持小部件的工具包含**两个独立的注册**：

1. **工具**通过 `_meta.ui.resourceUri` 声明一个 UI 资源。其 handler 返回纯文本/JSON——而不是 HTML。
2. **资源**单独注册，负责提供 HTML。

当 Claude 调用工具时，宿主看到 `_meta.ui.resourceUri`，拉取该资源，在 iframe 中渲染，并通过 `ontoolresult` 事件把工具的返回值送入 iframe。

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { registerAppTool, registerAppResource, RESOURCE_MIME_TYPE }
  from "@modelcontextprotocol/ext-apps/server";
import { z } from "zod";

const server = new McpServer({ name: "contacts", version: "1.0.0" });

// 1. The tool — returns DATA, declares which UI to show
registerAppTool(server, "pick_contact", {
  description: "Open an interactive contact picker",
  annotations: { title: "Pick Contact", readOnlyHint: true },
  inputSchema: { filter: z.string().optional() },
  _meta: { ui: { resourceUri: "ui://widgets/contact-picker.html" } },
}, async ({ filter }) => {
  const contacts = await db.contacts.search(filter);
  // Plain JSON — the widget receives this via ontoolresult
  return { content: [{ type: "text", text: JSON.stringify(contacts) }] };
});

// 2. The resource — serves the HTML
registerAppResource(
  server,
  "Contact Picker",
  "ui://widgets/contact-picker.html",
  {},
  async () => ({
    contents: [{
      uri: "ui://widgets/contact-picker.html",
      mimeType: RESOURCE_MIME_TYPE,
      text: pickerHtml,  // your HTML string
    }],
  }),
);
```

URI scheme `ui://` 只是约定。MIME 类型必须是 `RESOURCE_MIME_TYPE`（`"text/html;profile=mcp-app"`）——宿主据此将其渲染为交互式 iframe，而不是仅展示源码。

---

## 小部件运行时——`App` 类

在 iframe 内，你的脚本通过 `@modelcontextprotocol/ext-apps` 的 `App` 类与宿主通信。这是一条**持久的双向连接**——只要会话仍在进行，小部件就保持存活，接收新的工具结果并发送用户操作。

```html
<script type="module">
  /* ext-apps bundle inlined at build time → globalThis.ExtApps */
  /*__EXT_APPS_BUNDLE__*/
  const { App } = globalThis.ExtApps;

  const app = new App({ name: "ContactPicker", version: "1.0.0" }, {});

  // Set handlers BEFORE connecting
  app.ontoolresult = ({ content }) => {
    const contacts = JSON.parse(content[0].text);
    render(contacts);
  };

  await app.connect();

  // Later, when the user clicks something:
  function onPick(contact) {
    app.sendMessage({
      role: "user",
      content: [{ type: "text", text: `Selected contact: ${contact.id}` }],
    });
  }
</script>
```

`/*__EXT_APPS_BUNDLE__*/` 占位符由 server 在启动时替换为 `@modelcontextprotocol/ext-apps/app-with-deps` 的内容——为什么必须这样做以及改写代码片段见 `references/iframe-sandbox.md`。**不要** `import { App } from "https://esm.sh/..."`；iframe 的 CSP 会阻断传递依赖的拉取，小部件会渲染成一片空白。

| 方法 | 方向 | 用途 |
|---|---|---|
| `app.ontoolresult = fn` | 宿主 → 小部件 | 接收工具的返回值 |
| `app.ontoolinput = fn` | 宿主 → 小部件 | 接收工具的输入参数（Claude 传入的内容） |
| `app.sendMessage({...})` | 小部件 → 宿主 | 向会话注入一条消息 |
| `app.updateModelContext({...})` | 小部件 → 宿主 | 静默更新上下文（不产生可见消息） |
| `app.callServerTool({name, arguments})` | 小部件 → server | 调用你 server 上的另一个工具 |
| `app.openLink({url})` | 小部件 → 宿主 | 在新标签页打开 URL（sandbox 阻止 `window.open`） |
| `app.getHostContext()` / `app.onhostcontextchanged` | 宿主 → 小部件 | 主题、宿主 CSS 变量、`containerDimensions`、`displayMode`、`deviceCapabilities` |
| `app.requestDisplayMode({mode})` | 小部件 → 宿主 | 请求 `inline` / `pip` / `fullscreen` |
| `app.downloadFile({name, mimeType, content})` | 小部件 → 宿主 | 经宿主中转的下载（base64 内容） |
| `new App(info, caps, {autoResize: true})` | — | iframe 高度跟随渲染内容 |

`sendMessage` 是典型的"用户选好了某样东西，告诉 Claude"路径。`updateModelContext` 用于 Claude 应当知晓但不应刷屏聊天记录的状态。任何对外跳转都**必须**用 `openLink`——`window.open` 和 `<a target="_blank">` 都会被 sandbox 属性阻止。

**小部件做不到的事：**
- 访问宿主页面的 DOM、cookie 或存储
- 向任意来源发起网络请求（受 CSP 限制——请经由 `callServerTool` 中转）
- 打开弹窗或直接导航——请使用 `app.openLink({url})`
- 可靠地加载远程图片——请在 server 端内联为 `data:` URL

保持小部件**小而单一职责**。选择器就负责选，图表就负责显示。不要在 iframe 里造一个完整的子应用——把它拆成多个工具，各配一个聚焦的小部件。

---

## 脚手架：最小选择器小部件

**安装：**

```bash
npm install @modelcontextprotocol/sdk @modelcontextprotocol/ext-apps zod express
```

**Server（`src/server.ts`）：**

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { registerAppTool, registerAppResource, RESOURCE_MIME_TYPE }
  from "@modelcontextprotocol/ext-apps/server";
import express from "express";
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { z } from "zod";

const require = createRequire(import.meta.url);
const server = new McpServer({ name: "contact-picker", version: "1.0.0" });

// Inline the ext-apps browser bundle into the widget HTML.
// The iframe CSP blocks CDN script fetches — bundling is mandatory.
const bundle = readFileSync(
  require.resolve("@modelcontextprotocol/ext-apps/app-with-deps"), "utf8",
).replace(/export\{([^}]+)\};?\s*$/, (_, body) =>
  "globalThis.ExtApps={" +
  body.split(",").map((p) => {
    const [local, exported] = p.split(" as ").map((s) => s.trim());
    return `${exported ?? local}:${local}`;
  }).join(",") + "};",
);
const pickerHtml = readFileSync("./widgets/picker.html", "utf8")
  .replace("/*__EXT_APPS_BUNDLE__*/", () => bundle);

registerAppTool(server, "pick_contact", {
  description: "Open an interactive contact picker. User selects one contact.",
  annotations: { title: "Pick Contact", readOnlyHint: true },
  inputSchema: { filter: z.string().optional().describe("Name/email prefix filter") },
  _meta: { ui: { resourceUri: "ui://widgets/picker.html" } },
}, async ({ filter }) => {
  const contacts = await db.contacts.search(filter ?? "");
  return { content: [{ type: "text", text: JSON.stringify(contacts) }] };
});

registerAppResource(server, "Contact Picker", "ui://widgets/picker.html", {},
  async () => ({
    contents: [{ uri: "ui://widgets/picker.html", mimeType: RESOURCE_MIME_TYPE, text: pickerHtml }],
  }),
);

const app = express();
app.use(express.json());
app.post("/mcp", async (req, res) => {
  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
  res.on("close", () => transport.close());
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});
app.listen(process.env.PORT ?? 3000);
```

对于仅本地运行的小部件应用（驱动桌面应用、读取本地文件），把 transport 换成 `StdioServerTransport`，并经由 `build-mcpb` 技能打包。

**小部件（`widgets/picker.html`）：**

```html
<!doctype html>
<meta charset="utf-8" />
<style>
  body { font: 14px system-ui; margin: 0; }
  ul { list-style: none; padding: 0; margin: 0; max-height: 300px; overflow-y: auto; }
  li { padding: 10px 14px; cursor: pointer; border-bottom: 1px solid #eee; }
  li:hover { background: #f5f5f5; }
  .sub { color: #666; font-size: 12px; }
</style>
<ul id="list"></ul>
<script type="module">
/*__EXT_APPS_BUNDLE__*/
const { App } = globalThis.ExtApps;
(async () => {
  const app = new App({ name: "ContactPicker", version: "1.0.0" }, {});
  const ul = document.getElementById("list");

  app.ontoolresult = ({ content }) => {
    const contacts = JSON.parse(content[0].text);
    ul.innerHTML = "";
    for (const c of contacts) {
      const li = document.createElement("li");
      li.innerHTML = `<div>${c.name}</div><div class="sub">${c.email}</div>`;
      li.addEventListener("click", () => {
        app.sendMessage({
          role: "user",
          content: [{ type: "text", text: `Selected contact: ${c.id} (${c.name})` }],
        });
      });
      ul.append(li);
    }
  };

  await app.connect();
})();
</script>
```

更多小部件形态参见 `references/widget-templates.md`。

---

## 帮你省掉一次重写的设计要点

**每个工具一个小部件。**忍住做一个全能巨型小部件的冲动。一个工具 → 一个聚焦的小部件 → 一种清晰的结果形态。Claude 对这种结构的推理要好得多。

**工具描述必须提到小部件。**Claude 在决定调用什么时只看得到工具描述。描述里写上"打开一个交互式选择器"，才能让 Claude 主动用它，而不是瞎猜一个 ID。

**小部件在运行时是可选的。**不支持 apps surface 的宿主会直接忽略 `_meta.ui`，正常渲染工具的文本内容。由于你的工具 handler 本来就返回有意义的文本/JSON（即小部件的数据），降级是自动的——Claude 直接看到数据，而不经由小部件。

**只读工具不要阻塞等待小部件结果。**纯粹*展示*数据的小部件（图表、预览）不应要求用户操作才能算完成。在同一个结果中同时返回展示型小部件 *和* 文本摘要，让 Claude 无需等待即可继续推理。

**按条目数量分支布局，而不是按工具数量。**如果一个用例是"详细展示单个结果"，另一个是"并排展示多个结果"，不要做两个工具——做一个接受 `items[]` 的工具，让小部件选择布局：`items.length === 1` → 详情视图，`> 1` → 轮播。这样 server schema 保持简单，也让 Claude 自然决定数量。

**把 Claude 的推理放进 payload。**在每个条目上加一个简短的 `note` 字段（说明 Claude 为什么选它），在卡片上渲染为标注框，用户就能在选择旁边直接看到理由。在工具描述里提到这个字段，Claude 才会去填。

**在 server 端归一化图片形状。**如果你的数据源返回的图片长宽比千奇百怪，先在为 data-URL 内联而拉取*之前*改写成可预期的变体（如限定为方形）。然后给小部件的图片容器设置固定的 `aspect-ratio` + `object-fit: contain`，让所有内容居中放置。

**跟随宿主主题。**用 `app.getHostContext()?.theme`（在 `connect()` 之后）加 `app.onhostcontextchanged` 做实时更新。在 `<html>` 上切换 `.dark` 类，颜色放在 CSS 自定义属性中，配一个 `:root.dark {}` 覆盖块，并设置 `color-scheme`。深色模式下禁用 `mix-blend-mode: multiply`——它会让图片消失。

---

## 测试

**Claude Desktop**——当前版本仍要求 `command`/`args` 配置形态（没有原生 `"type": "http"`）。用 `mcp-remote` 包一层并强制 `http-only` transport，避免 SSE 探测吞掉小部件能力协商：

```json
{
  "mcpServers": {
    "my-server": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://localhost:3000/mcp",
               "--allow-http", "--transport", "http-only"]
    }
  }
}
```

Desktop 对 UI 资源的缓存非常激进。编辑小部件 HTML 之后，**彻底退出**（⌘Q / Alt+F4，而不是关窗口）再重启，强制冷重新拉取资源。

**无头 JSON-RPC 循环**——不用在 Desktop 里点来点去，快速迭代：

```bash
# test.jsonl — one JSON-RPC message per line
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"t","version":"0"}}}
{"jsonrpc":"2.0","method":"notifications/initialized"}
{"jsonrpc":"2.0","id":2,"method":"tools/list"}
{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"your_tool","arguments":{...}}}

(cat test.jsonl; sleep 10) | npx mcp-remote http://localhost:3000/mcp --allow-http
```

`sleep` 让 stdin 保持打开足够久，以便收齐所有响应。用 `jq` 或一行 Python 解析 jsonl 输出。

**小部件开发循环**——通过一个普通 GET 路由提供内联后的小部件 HTML，并配一个假的 `ExtApps` shim（从查询参数触发 `ontoolresult`），彻底避开 ⌘Q-重启循环：

```ts
app.get("/widget-preview", (_req, res) => {
  const shim = `globalThis.ExtApps={applyHostStyleVariables:()=>{},App:class{
    constructor(){this.h={}} ontoolresult;onhostcontextchanged;
    async connect(){const p=new URLSearchParams(location.search).get("payload");
      if(p)this.ontoolresult?.({content:[{type:"text",text:p}]});}
    getHostContext(){return{theme:"light"}}
    sendMessage(m){console.log("sendMessage",m)} updateModelContext(){}
    callServerTool(){return Promise.resolve({content:[]})} openLink(){} downloadFile(){}
  }};`;
  res.type("html").send(widgetHtml.replace("/*__EXT_APPS_BUNDLE__*/", shim));
});
```

在普通浏览器标签页中打开 `http://localhost:3000/widget-preview?payload={"rows":[...]}`，用常规 devtools 迭代。

**宿主降级**——用一个不支持 apps surface 的宿主（或 MCP Inspector），确认工具的文本内容能优雅降级。

**CSP 调试**——打开 iframe 自身的 devtools console。CSP 违规是小部件静默失败的第一大原因（空白矩形，主 console 无报错）。参见 `references/iframe-sandbox.md`。

---

## 参考文件

- `references/iframe-sandbox.md` — CSP/sandbox 约束、bundle 内联模式、图片处理、宿主主题适配
- `references/widget-templates.md` — 选择器 / 确认 / 进度 / 展示的可复用 HTML 脚手架
- `references/apps-sdk-messages.md` — `App` 类 API：小部件 ↔ 宿主 ↔ server 的消息传递、生命周期与取代（supersession）
- `references/payload-budgeting.md` — 宿主工具结果大小上限、先裁剪后截断、重型资源经 `callServerTool` 传输
- `references/abuse-protection.md` — Anthropic 出口 CIDR、分级限流、`trust proxy`、响应缓存
- `references/directory-checklist.md` — connector 目录提交前的检查清单
