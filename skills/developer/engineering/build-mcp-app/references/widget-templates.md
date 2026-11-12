> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-app/references/widget-templates.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Widget 模板

常见 widget 形态的最小 HTML 脚手架。复制、填内容、发布上线。

所有模板在构建时内联 `@modelcontextprotocol/ext-apps` 的 `App` 类，因为 iframe 的 CSP 会拦截 CDN 脚本导入。刻意不依赖框架：widget 足够小，React/Vue 的 hydration 开销通常不值得。

---

## 提供 widget HTML

widget 是静态 HTML，只有一个占位符：`/*__EXT_APPS_BUNDLE__*/` 会在服务器启动时被替换为 `ext-apps/app-with-deps` bundle（改写后暴露 `globalThis.ExtApps`）。

```typescript
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { registerAppResource, RESOURCE_MIME_TYPE } from "@modelcontextprotocol/ext-apps/server";

const require = createRequire(import.meta.url);

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

registerAppResource(server, "Picker", "ui://widgets/picker.html", {},
  async () => ({
    contents: [{ uri: "ui://widgets/picker.html", mimeType: RESOURCE_MIME_TYPE, text: pickerHtml }],
  }),
);
```

每次服务器启动打一次 bundle（或在构建时完成）；`bundle` 字符串在所有 widget 模板间复用。

---

## Picker（单选列表）

```html
<!doctype html>
<meta charset="utf-8" />
<style>
  body { font: 14px system-ui; margin: 0; }
  ul { list-style: none; padding: 0; margin: 0; max-height: 280px; overflow-y: auto; }
  li { padding: 10px 14px; cursor: pointer; border-bottom: 1px solid #eee; }
  li:hover { background: #f5f5f5; }
  .sub { color: #666; font-size: 12px; }
</style>
<ul id="list"></ul>
<script type="module">
/*__EXT_APPS_BUNDLE__*/
const { App } = globalThis.ExtApps;
(async () => {
  const app = new App({ name: "Picker", version: "1.0.0" }, {});
  const ul = document.getElementById("list");

  app.ontoolresult = ({ content }) => {
    const { items } = JSON.parse(content[0].text);
    ul.innerHTML = "";
    for (const it of items) {
      const li = document.createElement("li");
      li.innerHTML = `<div>${it.label}</div><div class="sub">${it.sub ?? ""}</div>`;
      li.addEventListener("click", () => {
        app.sendMessage({
          role: "user",
          content: [{ type: "text", text: `Selected: ${it.id}` }],
        });
      });
      ul.append(li);
    }
  };

  await app.connect();
})();
</script>
```

**工具返回：** `{ content: [{ type: "text", text: JSON.stringify({ items: [{ id, label, sub? }] }) }] }`

---

## 确认对话框

```html
<!doctype html>
<meta charset="utf-8" />
<style>
  body { font: 14px system-ui; margin: 16px; }
  .actions { display: flex; gap: 8px; margin-top: 16px; }
  button { padding: 8px 16px; cursor: pointer; }
  .danger { background: #d33; color: white; border: none; }
</style>
<p id="msg"></p>
<div class="actions">
  <button id="cancel">Cancel</button>
  <button id="confirm" class="danger">Confirm</button>
</div>
<script type="module">
/*__EXT_APPS_BUNDLE__*/
const { App } = globalThis.ExtApps;
(async () => {
  const app = new App({ name: "Confirm", version: "1.0.0" }, {});

  app.ontoolresult = ({ content }) => {
    const { message, confirmLabel } = JSON.parse(content[0].text);
    document.getElementById("msg").textContent = message;
    if (confirmLabel) document.getElementById("confirm").textContent = confirmLabel;
  };

  await app.connect();

  document.getElementById("confirm").addEventListener("click", () => {
    app.sendMessage({ role: "user", content: [{ type: "text", text: "Confirmed." }] });
  });
  document.getElementById("cancel").addEventListener("click", () => {
    app.sendMessage({ role: "user", content: [{ type: "text", text: "Cancelled." }] });
  });
})();
</script>
```

**工具返回：** `{ content: [{ type: "text", text: JSON.stringify({ message, confirmLabel? }) }] }`

**注意：** 简单确认场景优先用 **elicitation** 而非 widget，参见 `../build-mcp-server/references/elicitation.md`。需要原生表单之外的自定义样式或上下文时，再使用本 widget。

---

## 进度（长任务）

```html
<!doctype html>
<meta charset="utf-8" />
<style>
  body { font: 14px system-ui; margin: 16px; }
  .bar { height: 8px; background: #eee; border-radius: 4px; overflow: hidden; }
  .fill { height: 100%; background: #2a7; transition: width 200ms; }
</style>
<p id="label">Starting…</p>
<div class="bar"><div id="fill" class="fill" style="width:0%"></div></div>
<script type="module">
/*__EXT_APPS_BUNDLE__*/
const { App } = globalThis.ExtApps;
(async () => {
  const app = new App({ name: "Progress", version: "1.0.0" }, {});
  const label = document.getElementById("label");
  const fill = document.getElementById("fill");

  // The tool result fires when the job completes — intermediate updates
  // arrive via the same handler if the server streams them
  app.ontoolresult = ({ content }) => {
    const state = JSON.parse(content[0].text);
    if (state.progress !== undefined) {
      label.textContent = state.message ?? `${state.progress}/${state.total}`;
      fill.style.width = `${(state.progress / state.total) * 100}%`;
    }
    if (state.done) {
      label.textContent = "Complete";
      fill.style.width = "100%";
    }
  };

  await app.connect();
})();
</script>
```

服务器端通过 `extra.sendNotification({ method: "notifications/progress", ... })` 发送进度，参见 `apps-sdk-messages.md`。

---

## 纯展示（图表 / 预览）

展示型 widget 不调用 `sendMessage`：只渲染，然后停在那里。工具应**随 widget 一起**返回文字摘要，让用户看可视化的同时 Claude 能继续推理：

```typescript
registerAppTool(server, "show_chart", {
  description: "Render a revenue chart",
  inputSchema: { range: z.enum(["week", "month", "year"]) },
  _meta: { ui: { resourceUri: "ui://widgets/chart.html" } },
}, async ({ range }) => {
  const data = await fetchRevenue(range);
  return {
    content: [{
      type: "text",
      text: `Revenue is up ${data.change}% over the ${range}. Chart rendered.\n\n` +
            JSON.stringify(data.points),
    }],
  };
});
```

```html
<!doctype html>
<meta charset="utf-8" />
<style>body { font: 14px system-ui; margin: 12px; }</style>
<canvas id="chart" width="400" height="200"></canvas>
<script type="module">
/*__EXT_APPS_BUNDLE__*/
const { App } = globalThis.ExtApps;
(async () => {
  const app = new App({ name: "Chart", version: "1.0.0" }, {});

  app.ontoolresult = ({ content }) => {
    // Parse the JSON points from the text content (after the summary line)
    const text = content[0].text;
    const jsonStart = text.indexOf("\n\n") + 2;
    const points = JSON.parse(text.slice(jsonStart));
    drawChart(document.getElementById("chart"), points);
  };

  await app.connect();

  function drawChart(canvas, points) { /* ... */ }
})();
</script>
```

---

## 轮播（多条目展示带操作）

用于在横向滚动栏里呈现多个条目（商品推荐、搜索结果）。实测有效的模式：

- **省略导航箭头（chevron）**：用户本来就懂怎么滚动。`scroll-snap-type` 可能造成初始渲染偏移几像素、未贴齐；省略它，并在渲染后设 `scrollLeft = 0`。
- **按条目数分叉布局**：`items.length === 1` 用详情/PDP 布局，`> 1` 用轮播。在 widget JS 里处理，工具 schema 保持扁平。
- **把 Claude 的推理放进每个条目**：`note` 字段在卡片上渲染成小标注，让用户就地看到"为什么"。
- **用 `updateModelContext` 静默同步状态**：购物车/选择变化应告知 Claude 但不刷屏。`sendMessage` 留给终态动作（"结账"、"完成"）。
- **外链走 `app.openLink`**：`window.open` 和 `<a target="_blank">` 会被沙箱拦截。

```html
<style>
  .rail { display: flex; gap: 10px; overflow-x: auto; padding: 12px; scrollbar-width: none; }
  .rail::-webkit-scrollbar { display: none; }
  .card { flex: 0 0 220px; border: 1px solid #ddd; border-radius: 6px; padding: 10px; }
  .thumb-box { aspect-ratio: 1 / 1; display: grid; place-items: center; background: #f7f8f8; }
  .thumb { max-width: 100%; max-height: 100%; object-fit: contain; }
  .note { font-size: 12px; color: #666; border-left: 3px solid orange; padding: 2px 8px; margin: 8px 0; }
</style>
<div class="rail" id="rail"></div>
```

**图片：** iframe 的 CSP 会拦截远程 `img-src`。在工具处理器里服务端抓取缩略图，以 `data:` URL 嵌入 JSON 载荷，再据此渲染。加 `referrerpolicy="no-referrer"` 作为兜底。
