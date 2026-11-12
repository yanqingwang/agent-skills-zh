> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-app/references/apps-sdk-messages.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# ext-apps 消息机制：widget ↔ 宿主 ↔ 服务器

`@modelcontextprotocol/ext-apps` 包提供 `App` 类（浏览器侧）和 `registerAppTool`/`registerAppResource` 辅助函数（服务器侧）。消息是双向且持久的。

## 构造

```js
const app = new App(
  { name: "MyWidget", version: "1.0.0" },
  {},                       // capabilities
  { autoResize: true },     // options
);
```

`autoResize: true` 会接线一个 `ResizeObserver`，发出 `ui/notifications/size-changed`，让宿主 iframe 的高度跟随渲染内容。不设的话 frame 是固定高度，过高的渲染会被裁切：高度依赖数据的 widget 都应设置它。

---

## Widget → 宿主

### `app.sendMessage({ role, content })`

向对话注入一条可见消息。用户动作就是这样变成对话轮次的。

```js
app.sendMessage({
  role: "user",
  content: [{ type: "text", text: "User selected order #1234" }],
});
```

消息会出现在聊天里，Claude 会回应它。用 `role: "user"`：widget 是替用户说话的。

### `app.updateModelContext({ content })`

**静默**更新 Claude 的上下文，不产生可见消息。用于需要告知但不值得冒出聊天气泡的状态。

```js
app.updateModelContext({
  content: [{ type: "text", text: "Currently viewing: orders from last 30 days" }],
});
```

### `app.callServerTool({ name, arguments })`

直接调用你 MCP 服务器上的工具，绕过 Claude。返回工具结果。

```js
const result = await app.callServerTool({
  name: "fetch_order_details",
  arguments: { orderId: "1234" },
});
```

适合不需要 Claude 推理的数据拉取：分页、详情查询、刷新。

### `app.openLink({ url })`

在新浏览器标签页打开 URL，由宿主中转。任何外发导航都**必须**用它：iframe 沙箱会拦截 `window.open()` 和 `<a target="_blank">`。

```js
await app.openLink({ url: "https://example.com/cart" });
```

对渲染 HTML 里的锚点，拦截点击：

```js
card.querySelector("a").addEventListener("click", (e) => {
  e.preventDefault();
  app.openLink({ url: e.currentTarget.href });
});
```

### `app.downloadFile({ name, mimeType, content })`

由宿主中转的下载（沙箱会拦截直接的 `<a download>`）。`content` 是 base64 字符串。

```js
const csv = rows.map((r) => Object.values(r).join(",")).join("\n");
app.downloadFile({
  name: "export.csv",
  mimeType: "text/csv",
  content: btoa(unescape(encodeURIComponent(csv))),
});
```

### `app.requestDisplayMode({ mode })`

请求宿主把 widget 在 `"inline"`、`"pip"` 或 `"fullscreen"` 之间切换。先检查 `getHostContext().availableDisplayModes`；未提供的模式就隐藏对应控件。宿主会以新的 `displayMode` 和 `containerDimensions` 触发 `onhostcontextchanged` 作为响应：按新尺寸重新渲染。

```js
if (app.getHostContext()?.availableDisplayModes?.includes("fullscreen")) {
  expandBtn.hidden = false;
  expandBtn.onclick = () => app.requestDisplayMode({ mode: "fullscreen" });
}
```

---

## 宿主 → Widget

### `app.ontoolresult = ({ content }) => {...}`

工具处理器的返回值被投递给 widget 时触发。这是主要的数据入口。

```js
app.ontoolresult = ({ content }) => {
  const data = JSON.parse(content[0].text);
  renderUI(data);
};
```

**务必在 `await app.connect()` 之前设置**：结果可能在连接完成后立即到达。

### `app.ontoolinput = ({ arguments }) => {...}`

携带 Claude 传给工具的参数触发。widget 需要知道请求内容时有用（例如高亮搜索词）。

### `app.ontoolinputpartial = ({ arguments }) => {...}` / `app.ontoolcancelled = () => {...}`

`ontoolinputpartial` 在 Claude 还在流式输出参数时触发：趁结果未落地先显示骨架屏（"Preparing: <title>…"）。调用被中止时触发 `ontoolcancelled`：清除骨架屏。

### `app.getHostContext()` / `app.onhostcontextchanged = (ctx) => {...}`

读取并订阅宿主上下文。`getHostContext()` 要在 `connect()` **之后**调用。订阅以获得实时更新（用户切换深色模式、展开为全屏）。

| `ctx.` 字段 | 用途 |
|---|---|
| `theme` | `"light"` / `"dark"`：切换 `.dark` 类 |
| `styles.variables` | 宿主 CSS token：传给 `applyHostStyleVariables()`，让颜色/字体与宿主外观一致 |
| `displayMode` / `availableDisplayModes` | 当前模式，以及哪些 `requestDisplayMode` 目标可用 |
| `containerDimensions.{maxHeight,width}` | 按此尺寸渲染，不要写死 px |
| `deviceCapabilities.touch` | 把仅悬停的交互改为点按（`pointerdown`） |
| `safeAreaInsets` | 为刘海 / 输入框遮挡留 padding |

```js
const applyTheme = (t) =>
  document.documentElement.classList.toggle("dark", t === "dark");

app.onhostcontextchanged = (ctx) => applyTheme(ctx.theme);
await app.connect();
applyTheme(app.getHostContext()?.theme);
```

颜色放在 CSS 自定义属性里，配一个 `:root.dark {}` 覆盖块，并设置 `color-scheme: light | dark`，让原生表单控件跟随主题。

---

## 服务器 → Widget（进度）

长任务应发送进度通知。客户端在请求的 `_meta` 里带上 `progressToken`；服务器对着它发送进度。

```typescript
// In the tool handler
async ({ query }, extra) => {
  const token = extra._meta?.progressToken;
  for (let i = 0; i < steps.length; i++) {
    if (token !== undefined) {
      await extra.sendNotification({
        method: "notifications/progress",
        params: { progressToken: token, progress: i, total: steps.length, message: steps[i].name },
      });
    }
    await steps[i].run();
  }
  return { content: [{ type: "text", text: "Complete" }] };
}
```

没有 `{ notify }` 解构这回事：`extra` 是 `RequestHandlerExtra`，进度走 `sendNotification`。

---

## 生命周期

1. Claude 调用声明了 `_meta.ui.resourceUri` 的工具
2. 宿主拉取资源（你的 HTML），为本次调用挂载一个**全新 iframe**
3. widget 脚本运行、设置处理器、调用 `await app.connect()`
4. 宿主把工具返回值接进来 → `ontoolresult` 触发
5. widget 渲染，用户交互
6. widget 按需调用 `sendMessage` / `updateModelContext` / `callServerTool`
7. iframe 留存在会话记录里；**下一次调用同一工具会在旁边再挂载一个 iframe**

没有显式的"提交并关闭"：每个实例都是长驻的，但实例不会跨调用复用。

### 被取代（supersession）

早期实例保持挂载，所以较新的实例渲染后，旧 widget 上的一次点击仍可能 `sendMessage`。用 `BroadcastChannel` 检测这种情况，让旧实例失效：

```js
let superseded = false;
const seq = Date.now() + Math.random();
const bc = new BroadcastChannel("my-widget");
bc.onmessage = (e) => {
  if (e.data?.seq > seq) {
    superseded = true;
    document.body.classList.add("superseded"); // opacity:.45; pointer-events:none
  }
};
bc.postMessage({ seq });

// Guard outbound calls:
function safeSend(msg) {
  if (!superseded) app.sendMessage(msg);
}
```

---

## 沙箱与 CSP 陷阱

iframe 同时受 HTML `sandbox` 属性**和**严格 Content-Security-Policy 约束。实际效果就是几乎不允许任何外部内容：widget 应当自包含。

| 症状 | 原因 | 修复 |
|---|---|---|
| widget 是一块空白矩形，什么都不渲染 | CDN `import` ext-apps 被拦（传递性 SDK 拉取） | **内联** `ext-apps/app-with-deps` bundle，参见 `iframe-sandbox.md` |
| widget 渲染了但 JS 不跑 | 内联事件处理器被拦 | 用 `addEventListener`：HTML 里绝不写 `onclick="..."` |
| `eval` / `new Function` 报错 | script-src 限制 | 别用它们；数据解析用 JSON.parse |
| 对你的 API `fetch()` 失败 | 跨域被拦 | 改走 `app.callServerTool()` |
| 外部 CSS 加载不了 | `style-src` 限制 | 样式内联在 `<style>` 标签里 |
| 字体加载不了 | `font-src` 限制 | 用系统字体（`font: 14px system-ui`） |
| 外部 `<img src>` 挂掉 | CSP `img-src` + referrer 防盗链 | 服务端抓取，以 `data:` URL 内联进工具结果载荷 |
| `window.open()` 没反应 | 沙箱缺少 `allow-popups` | 用 `app.openLink({url})` |
| `<a target="_blank">` 没反应 | 同上 | 拦截点击 → `preventDefault()` → `app.openLink` |
| 改过的 HTML 在 Desktop 里不出现 | Desktop 缓存 UI 资源 | 完全退出（⌘Q）再重启，不能只关窗口 |

拿不准时，打开 **iframe 自己的** devtools 控制台（不是主应用的）：CSP 违规会记录在那里。bundle 内联模式参见 `iframe-sandbox.md`。
