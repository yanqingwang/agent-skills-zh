> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-server/references/resources-and-prompts.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Resources 与 Prompts — 另外两个原语

MCP 定义了三个 server 侧原语。Tools 是模型控制的（由 Claude 决定何时调用）。另外两个不同：

- **Resources** 是应用控制的，由 host 决定把什么拉进上下文
- **Prompts** 是用户控制的，以斜杠命令或菜单项的形式呈现

多数 server 只需要 tools。当你的集成形态不适合“Claude 调用函数”时，再来用这两个。

---

## Resources

resource 是用 URI 标识的数据。与 tool 不同，它不是被*调用*的，而是被*读取*的。host 浏览可用的 resources，决定把哪些载入上下文。

**resource 优于 tool 的情形：**
- 大体量参考数据（文档、schema、配置），Claude 应能浏览
- 内容独立于对话而变化（日志文件、实时数据）
- 任何“由 Claude 决定去取”都是错误心智模型的场景

**tool 更合适的情形：**
- 操作有副作用
- 结果取决于 Claude 选定的参数
- 你希望由 Claude（而不是 host UI）决定何时拉取

### 静态 resources

```typescript
// TypeScript SDK
server.registerResource(
  "config",
  "config://app/settings",
  { name: "App Settings", description: "Current configuration", mimeType: "application/json" },
  async (uri) => ({
    contents: [{ uri: uri.href, mimeType: "application/json", text: JSON.stringify(config) }],
  }),
);
```

```python
# fastmcp
@mcp.resource("config://app/settings")
def get_settings() -> str:
    """Current application configuration."""
    return json.dumps(config)
```

### 动态 resources（URI 模板）

RFC 6570 模板让一次注册服务多个 URI：

```typescript
import { ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";

server.registerResource(
  "file",
  new ResourceTemplate("file:///{path}", { list: undefined }),
  { name: "File", description: "Read a file from the workspace" },
  async (uri, { path }) => ({
    contents: [{ uri: uri.href, text: await fs.readFile(path, "utf8") }],
  }),
);
```

```python
@mcp.resource("file:///{path}")
def read_file(path: str) -> str:
    return Path(path).read_text()
```

### 订阅

Resource 变化时可以通知客户端。在 capabilities 里声明 `subscribe: true`，然后发出 `notifications/resources/updated`。host 会重新读取。适合日志尾随、实时仪表盘、被监听的文件。

---

## Prompts

prompt 是参数化的消息模板。host 把它呈现为斜杠命令或菜单项。用户选中、填入参数，生成的消息进入对话。

**何时使用：** 用户会反复运行的固化工作流，如 `/summarize-thread`、`/draft-reply`、`/explain-error`。代码量近乎为零，UX 杠杆很高。

```typescript
server.registerPrompt(
  "summarize",
  {
    title: "Summarize document",
    description: "Generate a concise summary of the given text",
    argsSchema: { text: z.string(), max_words: z.string().optional() },
  },
  ({ text, max_words }) => ({
    messages: [{
      role: "user",
      content: { type: "text", text: `Summarize in ${max_words ?? "100"} words:\n\n${text}` },
    }],
  }),
);
```

```python
@mcp.prompt
def summarize(text: str, max_words: str = "100") -> str:
    """Generate a concise summary of the given text."""
    return f"Summarize in {max_words} words:\n\n{text}"
```

**约束：**
- 参数**只能是字符串**（没有数字、布尔、对象），在 handler 内自行转换
- 返回 `messages[]` 数组，可以内嵌 resources/图片，不限于文本
- 无副作用，handler 只是构建消息，不*执行*任何动作

---

## 快速决策表

| 你想… | 选用 |
|---|---|
| 让 Claude 按需带参数地取数据 | **Tool** |
| 暴露可浏览的上下文（文件、文档、schema） | **Resource** |
| 暴露一族动态资源（`db://{table}`） | **Resource template** |
| 给用户一个一键式工作流 | **Prompt** |
| 在 tool 中途问用户一个问题 | **Elicitation**（见 `elicitation.md`） |
