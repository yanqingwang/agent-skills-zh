> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-server/references/elicitation.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Elicitation — 规范原生的用户输入

Elicitation 让 server 在 tool 调用中途暂停，向用户请求结构化输入。客户端渲染原生表单（没有 iframe，没有 HTML）。用户填完，server 继续。

**对简单输入而言，它就是正确答案。** Widgets（`build-mcp-app`）是为富 UI 准备的：图表、可搜索列表、可视化预览。如果你只需要一次确认、一个选中的选项或几个表单字段，elicitation 更简单、规范原生，且在任何合规 host 中都可用。

---

## ⚠️ 先检查能力，支持还很新

Host 的支持出现得很晚：

| Host | 状态 |
|---|---|
| Claude Code | ✅ 自 v2.1.76 起（`form` 和 `url` 两种模式都支持） |
| Claude Desktop | 未确认，大概率还没有，或非常新 |
| claude.ai | 未知 |

**如果客户端没有声明 elicitation 能力，SDK 会抛出 `CapabilityNotSupported`。** SDK 内置没有优雅降级。你必须先检查并准备好回退方案。

### 标准模式

```typescript
server.registerTool("delete_all", {
  description: "Delete all items after confirmation",
  inputSchema: {},
}, async ({}, extra) => {
  const caps = server.getClientCapabilities();
  if (caps?.elicitation) {
    const r = await server.elicitInput({
      mode: "form",
      message: "Delete all items? This cannot be undone.",
      requestedSchema: {
        type: "object",
        properties: { confirm: { type: "boolean", title: "Confirm deletion" } },
        required: ["confirm"],
      },
    });
    if (r.action === "accept" && r.content?.confirm) {
      await deleteAll();
      return { content: [{ type: "text", text: "Deleted." }] };
    }
    return { content: [{ type: "text", text: "Cancelled." }] };
  }
  // Fallback: return text asking Claude to relay the question
  return { content: [{ type: "text", text: "Confirmation required. Please ask the user: 'Delete all items? This cannot be undone.' Then call this tool again with their answer." }] };
});
```

```python
# fastmcp
from fastmcp import Context
from fastmcp.exceptions import CapabilityNotSupported

@mcp.tool
async def delete_all(ctx: Context) -> str:
    try:
        result = await ctx.elicit("Delete all items? This cannot be undone.", response_type=bool)
        if result.action == "accept" and result.data:
            await do_delete()
            return "Deleted."
        return "Cancelled."
    except CapabilityNotSupported:
        return "Confirmation required. Ask the user to confirm deletion, then retry."
```

---

## Schema 约束

Elicitation schema 有意做了限制，表单要保持简单：

- **只允许扁平对象**，不支持嵌套，不支持对象数组
- **只允许原始类型**：`string`、`number`、`integer`、`boolean`、`enum`
- 字符串 format 限定为：`email`、`uri`、`date`、`date-time`
- 每个 property 都要写 `title` 和 `description`，它们会成为表单标签

如果你的数据塞不进这些约束，那就是该升级到 widget 的信号。

---

## 三态响应

| Action | 含义 | 是否有 `content` |
|---|---|---|
| `accept` | 用户提交了表单 | ✅ 已按你的 schema 校验 |
| `decline` | 用户明确拒绝 | ❌ |
| `cancel` | 用户关闭了表单（按 Esc、点了别处） | ❌ |

如果这个区别要紧，`decline` 和 `cancel` 要区别对待：`decline` 是有意拒绝，`cancel` 可能是误操作。

TS SDK 的 `server.elicitInput()` 通过 Ajv 按你的 schema 自动校验 `accept` 响应。fastmcp 的 `ctx.elicit()` 返回带类型的可辨识联合（`AcceptedElicitation[T] | DeclinedElicitation | CancelledElicitation`）。

---

## fastmcp 的 response_type 简写

```python
await ctx.elicit("Pick a color", response_type=["red", "green", "blue"])  # enum
await ctx.elicit("Enter email", response_type=str)                         # string
await ctx.elicit("Confirm?", response_type=bool)                           # boolean

@dataclass
class ContactInfo:
    name: str
    email: str
await ctx.elicit("Contact details", response_type=ContactInfo)             # flat dataclass
```

可接受：原始类型、`list[str]`（转成 enum）、dataclass、TypedDict、Pydantic BaseModel。全部必须是扁平的。

---

## 安全

**绝不能通过 elicitation 请求密码、API key 或 token**，这是规范要求。这些信息应走 OAuth，或 MCPB 中带 `sensitive: true` 的 `user_config`，而不是运行时表单。

---

## 什么时候升级到 widgets

Elicitation 能应付：确认对话框、enum 选择器、简短的扁平表单。

需要以下能力时改用 `build-mcp-app` widgets：
- 嵌套或复杂的数据结构
- 可滚动/可搜索的列表（100+ 项）
- 选择前的可视化预览（图片缩略图、文件树）
- 实时更新的进度或流式内容
- 自定义布局、图表、地图
