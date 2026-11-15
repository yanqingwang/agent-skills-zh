> **中文汉化版** · 上游：[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) · 原文件：`skills/seo-agentic/references/webmcp.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# WebMCP：状态、API、消费者与安全

WebMCP 让页面注册工具（name、description、JSON Schema 输入、handler），供浏览器内的 agent 调用，以替代驱动 UI。把它当作**渐进增强**：对有表单或交易的站点有用，绝不能替代一个健全的无障碍树。事实核查于 2026-09-23。

## 标准状态

| 项目 | 状态 |
|---|---|
| 规范 | W3C Web Machine Learning Community Group 草案（"not a W3C Standard nor on the Standards Track"）；规范最后提交于 2026-09-17。编辑来自 Microsoft 和 Google。 |
| Chrome | Origin trial M149 至 M156（chromestatus 5117755740913664）；dev flag `chrome://flags/#enable-webmcp-testing`（Chrome 的 WebMCP 文档，更新于 2026-08-07）。未宣布 ship 里程碑。 |
| Edge | 在 Canary/Dev 中测试；origin trial；MicrosoftEdge/webmcp-labs 示例与 WebMCP Explorer。没有证据表明 Copilot 消费工具。 |
| WebKit | 立场 `oppose`（standards-positions #670）：偏好无障碍树而非并行工具层。具体日期与引文来自 secondary 追踪源。 |
| Mozilla | 立场 `neutral`（#1412）：对 imperative API 感兴趣，对 declarative 不感兴趣。 |

## 今天谁在调用 WebMCP 工具

| 消费方 | Imperative | Declarative | 说明 |
|---|---|---|---|
| ChatGPT 桌面版内置浏览器（"site tools"） | 是 | **否** | 默认开启；仅顶层文档（不含 iframe）；Enterprise/Edu 不可用；确认策略仍然适用。文档：learn.chatgpt.com/docs/webmcp |
| Chrome / Edge（origin trial 或 flag） | 是 | 是 | Lighthouse 与 PSI 看到的就是这个 |
| Brave Leo | 实验性 | ? | Nightly 中位于 flag 之后 |
| Chrome 中的 Gemini、Claude for Chrome、Perplexity Comet | 无公开信号 | 否 | 依赖页面文本、DOM、截图和无障碍树 |

## API 表面（规范草案）

- 入口：**`document.modelContext`**（secure contexts）。旧引擎和部分工具用过 `navigator.modelContext`；对两者做特性检测，优先 `document`。Lighthouse 两种都识别。
- `registerTool(tool, { exposedTo, signal })` 返回 Promise。没有 `unregisterTool`：传入一个 `AbortSignal`，需要时 abort 它。
- 另有 `getTools()`、`executeTool()`，以及事件 `toolchange`、`toolactivated`、`toolcancel`。
- 工具字段：`name`（必填）、`title`、`description`（必填）、`inputSchema`、`execute(input, { signal })`（必填）、`annotations`。
- Annotations：`readOnlyHint`、`untrustedContentHint`、`consequentialHint`、`debugging`（默认都是 false）。
- Permissions policy 特性 `tools`（默认 `'self'`）：跨域 iframe 需要 `allow="tools"`；`Permissions-Policy: tools=()` 则禁用。

Declarative（explainer；规范章节仍是 TODO，仅 Chrome）：`<form>` 上的 `toolname`、`tooldescription` 和 `toolautosubmit`，控件上的 `toolparamdescription`；参数名取自每个控件的 `name`。`SubmitEvent.agentInvoked`（布尔值）和 `respondWith(Promise)` 让页面区分 agent 提交。CSS：`:tool-form-active`、`:tool-submit-active`。

## 在 Chrome 和 ChatGPT 桌面版都能用的 imperative 模式

```html
<meta http-equiv="origin-trial" content="YOUR_CHROME_OT_TOKEN">
<script type="module">
const mc = document.modelContext ?? navigator.modelContext; // navigator: legacy
if (mc?.registerTool) {
  const controller = new AbortController();
  await mc.registerTool({
    name: "search_articles",
    description: "Search published articles by keyword. Returns titles and URLs.",
    inputSchema: {
      type: "object",
      properties: { query: { type: "string", description: "Keywords to search" } },
      required: ["query"]
    },
    annotations: { readOnlyHint: true },
    async execute({ query }) {
      const r = await fetch(`/api/search?q=${encodeURIComponent(query)}`); // same endpoint as the UI
      return { content: [{ type: "text", text: JSON.stringify(await r.json()) }] };
    }
  }, { signal: controller.signal });
}
</script>
```

origin-trial 的 `<meta>` token 在 trial 期间为普通 Chrome 访客启用该 API；ChatGPT 桌面版和 PSI 不需要它。上面的返回结构沿用当前示例所用的 MCP content 约定；上线前对照 Chrome WebMCP 文档确认。`agentic_fix.py webmcp <url>` 会为每个真实表单起草一个工具，绑定到该表单自己的提交处理器。

## 暴露工具的安全规则

1. 每个工具都绑定到与 UI 操作相同的代码路径（同端点、同校验、同授权）。绝不添加特权后门。
2. 对购买、发送、删除，标记 `consequentialHint: true` **并且**保留人工确认步骤。这个提示不能替代确认。
3. 对返回用户或第三方提供文本的工具，标记 `untrustedContentHint: true`。藏在内容里对 agent 的指令是 Mozilla 的核心顾虑。
4. 不要把 consequential 工具放进跨域 iframe；绝不给 `exposedTo` 用通配符。
5. 在服务端记录 `SubmitEvent.agentInvoked` 和工具调用，并做速率限制。
6. 会话绑定的工具以用户的真实权限运行（OpenAI 的云浏览器可以保持登录会话）。相应地收窄其作用域。
7. 要给 API 或 MCP 访问，用 OAuth（RFC 9728 元数据），不要抓会话。
8. 工具描述绝不能指示 agent 跳过或绕过用户确认（例如"no need to confirm with the user"）。把这类措辞当作 P1 安全发现：那是一条人永远看不到的、写给 agent 的指令。

## 审计口径

- 没有 WebMCP 是机会，不是缺陷。
- 只在确实存在表单或交易时推荐 imperative 工具（P2，交易型站点为 P1）；declarative 属性是 P3（仅 Chrome）。
- 每条 WebMCP 建议都标注"W3C CG draft"并附核查日期。
- 绝不引用 WebMCP 的"token 效率"百分比：广为流传的数字出自营销帖，不是基准测试。

## 验证工具

- `lighthouse_agentic.py`（PSI）列出已注册工具和 schema 问题。
- Vercel 的 `agent-browser webmcp list` / `webmcp invoke`（WebMCP 默认开启）。
- GoogleChromeLabs/webmcp-tools 与 Model Context Tool Inspector；MicrosoftEdge/webmcp-labs 的 WebMCP Explorer。
- Lightpanda 目前只暴露 `navigator.modelContext`，遵循规范的页面对它不可见。
