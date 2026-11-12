> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-app/references/iframe-sandbox.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Iframe 沙箱约束

MCP 应用的 widget 运行在宿主（Claude Desktop、claude.ai）的沙箱化 `<iframe>` 里。sandbox 与 CSP 属性锁死了 widget 能做的事。以下每一项都曾以"无声的空白 iframe"形式失败过，直到应用修复才恢复：报错只出现在 iframe 自己的 devtools 控制台，宿主控制台看不到。

---

## 问题 → 修复表

| 症状 | 根因 | 修复 |
|---|---|---|
| widget 渲染成空白矩形，无报错 | CSP `script-src` 拦截 esm.sh 拉取传递依赖 `@modelcontextprotocol/sdk` | 把 `ext-apps/app-with-deps` bundle 内联进 HTML |
| `window.open()` 没反应 | 沙箱缺少 `allow-popups` | 用 `app.openLink({ url })` |
| `<a target="_blank">` 没反应 | 同上 | 点击时 `e.preventDefault()` + `app.openLink({ url })` |
| 外部 `<img src>` 挂掉 | CSP `img-src` + referrer 防盗链 | 服务端抓取，以 `data:` URL 放进工具结果载荷 |
| 服务器重启后 widget 改动不生效 | 宿主缓存 UI 资源 | 完全退出宿主（⌘Q / Alt+F4）再重启 |
| 顶层 `await` 抛错 | 旧版 iframe 上下文 | 把模块主体包进 async IIFE |

---

## 内联 ext-apps bundle

`@modelcontextprotocol/ext-apps` 在 `app-with-deps` 导出点提供自包含的浏览器构建（约 300KB）。它是压缩过的 ESM，以 `export{…}` 结尾；要在内联 `<script type="module">` 块中使用，需在构建时把 export 语句改写为全局赋值：

```ts
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);

const bundle = readFileSync(
  require.resolve("@modelcontextprotocol/ext-apps/app-with-deps"),
  "utf8",
).replace(/export\{([^}]+)\};?\s*$/, (_, body) =>
  "globalThis.ExtApps={" +
  body.split(",").map((pair) => {
    const [local, exported] = pair.split(" as ").map((s) => s.trim());
    return `${exported ?? local}:${local}`;
  }).join(",") + "};",
);

const widgetHtml = readFileSync("./widgets/widget.html", "utf8")
  .replace("/*__EXT_APPS_BUNDLE__*/", () => bundle);
```

widget 一侧：

```html
<script type="module">
/*__EXT_APPS_BUNDLE__*/
const { App } = globalThis.ExtApps;
(async () => {
  const app = new App({ name: "…", version: "…" }, {});
  // …
})();
</script>
```

`() => bundle` 这种替换函数形式（而非裸字符串）很重要：`String.replace` 会在字符串替换里解释 `$…` 序列，而压缩后的 bundle 里全是这种序列。

---

## 外发链接

```js
// ✗ blocked
window.open(url, "_blank");
// ✗ blocked
<a href="…" target="_blank">…</a>

// ✓ host-mediated
await app.openLink({ url });
```

拦截锚点点击：

```js
el.addEventListener("click", (e) => {
  e.preventDefault();
  app.openLink({ url: el.href });
});
```

---

## 外部图片

CSP `img-src` 默认策略（加上很多 CDN 的 referrer 策略）会拦住 `<img src="https://external-cdn/…">` 加载。在工具处理器里服务端内联：

```ts
async function toDataUrl(url: string): Promise<string | undefined> {
  try {
    const res = await fetch(url, { signal: AbortSignal.timeout(5000) });
    if (!res.ok) return undefined;
    const buf = Buffer.from(await res.arrayBuffer());
    const mime = res.headers.get("content-type") ?? "image/jpeg";
    return `data:${mime};base64,${buf.toString("base64")}`;
  } catch {
    return undefined;
  }
}

// in the tool handler
const inlined = await Promise.all(
  items.map(async (it) =>
    it.thumb ? { ...it, thumb: await toDataUrl(it.thumb) ?? it.thumb } : it,
  ),
);
```

给 `<img>` 加 `referrerpolicy="no-referrer"`，兜底那些没被内联、仍走外链的 URL。

---

## 主题与宿主样式

宿主把 iframe 放在自己的卡片外观里渲染：背景画成**透明**，并采用宿主 CSS token，让 widget 在明暗主题之间、不同宿主之间都能融入。

```html
<meta name="color-scheme" content="light dark" />
```

```css
:root {
  --ink:  var(--color-text-primary,   #0f1111);
  --sub:  var(--color-text-secondary, #5a6270);
  --line: var(--color-border-default, #e3e6ea);
}
html, body { background: transparent; color: var(--ink); }
:root.dark .thumb { mix-blend-mode: normal; } /* multiply → images vanish in dark */
```

```js
const { App, applyHostStyleVariables } = globalThis.ExtApps;

function applyHostContext(ctx) {
  document.documentElement.classList.toggle("dark", ctx?.theme === "dark");
  if (ctx?.styles?.variables) applyHostStyleVariables(ctx.styles.variables);
}
app.onhostcontextchanged = applyHostContext;
await app.connect();
applyHostContext(app.getHostContext());
```

`applyHostStyleVariables` 会把宿主的 `--color-*` / `--font-*` / `--border-radius-*` token 写到 `:root` 上；上面的十六进制值是给不提供这些 token 的宿主用的兜底。

---

## 调试

iframe 有自己的控制台。在 Claude Desktop 里打开 DevTools（View → Toggle Developer Tools），然后把上下文下拉框（Console 标签页左上角）从 "top" 切到 widget 的 iframe。CSP 违规、未捕获异常、import 错误都会在那里浮出：宿主主控制台则始终安静。
