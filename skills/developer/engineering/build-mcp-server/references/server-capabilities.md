> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-server/references/server-capabilities.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Server capabilities — 规范中的其余部分

三大核心原语之外的特性。多数是可选的，有几个几乎是白捡的收益。

---

## `instructions` — system prompt 注入

一行配置，直接落入 Claude 的 system prompt。用它来放那些放不进单个 tool description 的 tool 使用提示。

```typescript
const server = new McpServer(
  { name: "my-server", version: "1.0.0" },
  { instructions: "Always call search_items before get_item — IDs aren't guessable." },
);
```

```python
mcp = FastMCP("my-server", instructions="Always call search_items before get_item — IDs aren't guessable.")
```

这是规范里杠杆率最高的一行配置。如果 Claude 总是用错你的 tools，把修正写在这里。

---

## Sampling — 把 LLM 调用委托给 host

如果你的 tool 逻辑需要 LLM 推理（摘要、分类、生成），不要自带模型客户端。让 host 来做。

```typescript
// Inside a tool handler
const result = await extra.sendRequest({
  method: "sampling/createMessage",
  params: {
    messages: [{ role: "user", content: { type: "text", text: `Summarize: ${doc}` } }],
    maxTokens: 500,
  },
}, CreateMessageResultSchema);
```

```python
# fastmcp
response = await ctx.sample("Summarize this document", context=doc)
```

**需要客户端支持**，先检查 `clientCapabilities.sampling`。模型偏好提示按子串匹配（`"claude-3-5"` 匹配任何 Claude 3.5 变体）。

---

## Roots — 查询工作区边界

不要硬编码根目录，改为向 host 询问用户批准了哪些目录。

```typescript
const caps = server.getClientCapabilities();
if (caps?.roots) {
  const { roots } = await server.server.listRoots();
  // roots: [{ uri: "file:///home/user/project", name: "My Project" }]
}
```

```python
roots = await ctx.list_roots()
```

对 MCPB 本地 server 尤其相关，见 `build-mcpb/references/local-security.md`。

---

## Logging — 结构化、分级别

对 remote server 而言比 stderr 更好。客户端可以按级别过滤。

```typescript
// In a tool handler
await extra.sendNotification({
  method: "notifications/message",
  params: { level: "info", logger: "my-tool", data: { msg: "Processing", count: 42 } },
});
```

```python
await ctx.info("Processing", count=42)   # also: ctx.debug, ctx.warning, ctx.error
```

级别遵循 syslog：`debug`、`info`、`notice`、`warning`、`error`、`critical`、`alert`、`emergency`。客户端通过 `logging/setLevel` 设置最低级别。

---

## Progress — 供长耗时 tools 使用

客户端在请求 `_meta` 里带上 `progressToken`。server 针对它发出进度通知。

```typescript
async (args, extra) => {
  const token = extra._meta?.progressToken;
  for (let i = 0; i < 100; i++) {
    if (token !== undefined) {
      await extra.sendNotification({
        method: "notifications/progress",
        params: { progressToken: token, progress: i, total: 100, message: `Step ${i}` },
      });
    }
    await doStep(i);
  }
  return { content: [{ type: "text", text: "Done" }] };
}
```

```python
async def long_task(ctx: Context) -> str:
    for i in range(100):
        await ctx.report_progress(progress=i, total=100, message=f"Step {i}")
        await do_step(i)
    return "Done"
```

---

## Cancellation — 响应中止信号

长耗时的 tool 应检查 SDK 提供的 `AbortSignal`：

```typescript
async (args, extra) => {
  for (const item of items) {
    if (extra.signal.aborted) throw new Error("Cancelled");
    await process(item);
  }
}
```

fastmcp 通过 asyncio 取消机制处理这件事，只要你的 handler 是规范的 async 写法，就无需显式检查。

---

## Completion — 提示词参数的自动补全

如果你注册的 prompts 或 resource 模板带参数，可以提供自动补全：

```typescript
server.registerPrompt("query", {
  argsSchema: {
    table: completable(z.string(), async (partial) => tables.filter(t => t.startsWith(partial))),
  },
}, ...);
```

优先级不高，除非你的 prompts 有很多合法取值。

---

## 哪些能力需要客户端支持？

| 特性 | Server 声明 | 客户端必须支持 | 不支持时的回退 |
|---|---|---|---|
| `instructions` | 隐式 | — | —（始终可用） |
| Logging | `logging: {}` | — | stderr |
| Progress | — | 发送 `progressToken` | 静默跳过 |
| Sampling | — | `sampling: {}` | 自备 LLM |
| Elicitation | — | `elicitation: {}` | 返回文本，请 Claude 代为转问 |
| Roots | — | `roots: {}` | 用配置环境变量 |

使用最后三项之前，先用 `server.getClientCapabilities()`（TS）或 `ctx.session.client_params.capabilities`（fastmcp）检查客户端能力。
