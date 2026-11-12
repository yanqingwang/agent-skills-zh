> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-server/references/tool-design.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Tool 设计 — 写出 Claude 能正确使用的 tools

Tool schema 和 description 就是提示词工程。它们直接进入 Claude 的上下文，决定 Claude 能否用正确的参数选中正确的 tool。多数 MCP 集成 bug 都能追溯到含糊的 description 或宽松的 schema。

## Anthropic Directory 硬性要求

如果这个 server 要提交到 Anthropic Directory，以下是审查的通过/不通过标准（完整列表：https://claude.com/docs/connectors/building/review-criteria）：

- 每个 tool **必须**包含 `readOnlyHint`、`destructiveHint` 和 `title` annotations，它们决定 Claude 中的自动权限。
- Tool 名称**必须**不超过 64 个字符。
- 读操作和写操作**必须**拆到不同的 tools。单个 tool 同时接受 GET 和 POST/PUT/PATCH/DELETE 会被拒，在一个 tool 的 description 里说明安全与不安全操作满足不了这条要求。
- Tool description **不得**指示 Claude 的行为方式（例如 "always do X"、"you must call Y first"、覆盖系统指令、推销产品），审查时按 prompt injection 处理。
- 接受自由格式 API 端点/参数的 tools **必须**在 description 中引用目标 API 的文档。

---

## Descriptions

**description 就是契约。** 它是 Claude 在决定是否调用某个 tool 前唯一会读的东西。把它写成一行 manpage 词条，再加上消歧提示。

### 好的写法

```
search_issues — Search issues by keyword across title and body. Returns up
to `limit` results ranked by recency. Does NOT search comments or PRs —
use search_comments / search_prs for those.
```

- 说了它做什么
- 说了它返回什么
- 说了它*不*做什么（防止调错 tool）

### 坏的写法

```
search_issues — Searches for issues.
```

只要事情沾点搜索的边，Claude 都会调它，包括它根本做不到的事。

### 为同类 tools 消歧

两个 tool 相近时，每个 description 都应说明什么时候该用*另一个*：

```
get_user      — Fetch a user by ID. If you only have an email, use find_user_by_email.
find_user_by_email — Look up a user by email address. Returns null if not found.
```

---

## 参数 schema

**收紧 schema 能防止错误调用。** 你在 schema 里多写一条约束，运行时就少一处可能出错的地方。

| 别这样 | 应该这样 |
|---|---|
| ID 用 `z.string()` | `z.string().regex(/^usr_[a-z0-9]{12}$/)` |
| limit 用 `z.number()` | `z.number().int().min(1).max(100).default(20)` |
| 选项用 `z.string()` | `z.enum(["open", "closed", "all"])` |
| 可选却无任何提示 | `.optional().describe("Defaults to the caller's workspace")` |

**每个参数都要写 describe。** `.describe()` 的文本会出现在 Claude 看到的 schema 里。省掉它就是把好处白白扔掉。

```typescript
{
  query: z.string().describe("Keywords to search for. Supports quoted phrases."),
  status: z.enum(["open", "closed", "all"]).default("open")
    .describe("Filter by status. Use 'all' to include closed items."),
  limit: z.number().int().min(1).max(50).default(10)
    .describe("Max results. Hard cap at 50."),
}
```

---

## 返回形态

Claude 会读取你在 `content[].text` 里放的一切。让它可解析。

**应该：**
- 结构化数据返回 JSON（`JSON.stringify(result, null, 2)`）
- 变更操作返回简短确认（`"Created issue #123"`）
- 带上 Claude 后续调用需要的 ID
- 截断超大响应并明确说明（`"Showing 10 of 847 results. Refine the query to narrow down."`）

**不要：**
- 返回原始 HTML
- 返回数 MB 未经筛选的 API 响应
- 返回没有标识符的裸成功（create 之后只回 `"ok"`，Claude 无法引用它刚创建的东西）

---

## 多少个 tools 合适？

| Tool 数量 | 指导 |
|---|---|
| 1–15 | 每个操作一个 tool。最佳区间。 |
| 15–30 | 仍然可行。审查一遍，把可合并的近似重复合并掉。 |
| 30+ | 改用 search + execute。可选择性把最常用的 3–5 个提升为专属 tools。 |

这个上限不是硬性协议限制，而是 context window 的经济学。每个 tool schema 都是 Claude *每一轮*都要花掉的 token。30 个 schema 丰富的 tools 可能还没开始对话就吃掉 3–5k token。

---

## 错误

返回 MCP tool 错误，而不是让 transport 崩掉的异常。带上足够的细节，让 Claude 能恢复或换个方式重试。

```typescript
if (!item) {
  return {
    isError: true,
    content: [{
      type: "text",
      text: `Item ${id} not found. Use search_items to find valid IDs.`,
    }],
  };
}
```

这条提示（"use search_items…"）把死路变成下一步。

---

## Tool annotations

host 用于 UX 的提示：destructive 时弹红色确认按钮，readonly 时自动批准。全部默认未设置（host 按最坏情况处理）。

| Annotation | 含义 | Host 行为 |
|---|---|---|
| `readOnlyHint: true` | 无副作用 | 可自动批准 |
| `destructiveHint: true` | 删除/覆盖 | 确认对话框 |
| `idempotentHint: true` | 可安全重试 | 瞬时错误时可能自动重试 |
| `openWorldHint: true` | 会访问外部世界（web、API） | 可能显示网络指示器 |

```typescript
server.registerTool("delete_file", {
  description: "Delete a file",
  inputSchema: { path: z.string() },
  annotations: { destructiveHint: true, idempotentHint: false },
}, handler);
```

```python
@mcp.tool(annotations={"destructiveHint": True, "idempotentHint": False})
def delete_file(path: str) -> str:
    ...
```

配合 `build-mcpb/references/local-security.md` 中的读写拆分建议：每个只读 tool 都标注 `readOnlyHint: true`。

---

## 结构化输出

把 `JSON.stringify(result)` 放进 text 块可行，但规范有一等公民级别的类型化输出：`outputSchema` + `structuredContent`。客户端可以据此校验。

```typescript
server.registerTool("get_weather", {
  description: "Get current weather",
  inputSchema: { city: z.string() },
  outputSchema: { temp: z.number(), conditions: z.string() },
}, async ({ city }) => {
  const data = await fetchWeather(city);
  return {
    content: [{ type: "text", text: JSON.stringify(data) }],  // backward compat
    structuredContent: data,                                    // typed output
  };
});
```

始终保留 text 回退，目前并非所有 host 都会读取 `structuredContent`。

---

## text 之外的内容类型

Tools 能返回的不只是字符串：

| 类型 | 形态 | 用途 |
|---|---|---|
| `text` | `{ type: "text", text: string }` | 默认 |
| `image` | `{ type: "image", data: base64, mimeType }` | 截图、图表、示意图 |
| `audio` | `{ type: "audio", data: base64, mimeType }` | TTS 输出、录音 |
| `resource_link` | `{ type: "resource_link", uri, name?, description? }` | 指针，客户端稍后自行获取 |
| `resource`（内嵌） | `{ type: "resource", resource: { uri, text\|blob, mimeType } }` | 内联完整内容 |

**`resource_link` vs 内嵌：** 载荷大、或客户端可能不需要时用 link（让客户端自己决定）。内容小且总会用到时才内嵌。
