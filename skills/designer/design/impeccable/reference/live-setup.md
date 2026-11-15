> **中文汉化版** · 上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 原文件：`.claude/skills/impeccable/reference/live-setup.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

一次性的 live 模式项目设置。仅当 `impeccable live` 报出 `config_missing` / `config_invalid`、需要处理 `configDrift`，或配置缺少 `cspChecked` 时，才从 [live.md](live.md) 加载本文件。不属于每会话的热路径。

## 写入配置

在 boot 报告的 `path` 处创建文件（默认 `.impeccable/live/config.json`）：

```json
{
  "files": ["<path-or-glob>", "<path-or-glob>", ...],
  "exclude": ["<optional-glob>", ...],
  "insertBefore": "</body>",
  "commentSyntax": "html",
  "cspChecked": true
}
```

`files` 是注入目标：**浏览器实际加载的 HTML 文件**，不一定是源码（这里不区分受版本控制的还是生成的；wrap 自带生成文件守卫）。条目是字面路径或 glob。`exclude`（可选）跳过 `files` 的 glob 本会包含的文件（邮件模板、演示 fixture）。`cspChecked` 记录下面的 CSP 步骤已经跑过；首次设置时没有这个键。

**硬排除路径（不可覆盖）：**`**/node_modules/**` 与 `**/.git/**`；往那里注入等于给第三方代码插桩。

**Glob 语法：**`**` 匹配任意多段（含零段），`*` 在单段内匹配，`?` 匹配一个字符。路径相对项目根，用正斜杠。

| 框架 | `files` | `insertBefore` | `commentSyntax` |
|-----------|---------|----------------|-----------------|
| 单 shell 的 SPA（Vite / React / 纯 HTML） | `["index.html"]` | `</body>` | `html` |
| Next.js（App Router） | `["app/layout.tsx"]` | `</body>` | `jsx` |
| Next.js（Pages） | `["pages/_document.tsx"]` | `</body>` | `jsx` |
| Nuxt | `["app.vue"]` | `</body>` | `html` |
| Svelte / SvelteKit | `["src/app.html"]` | `</body>` | `html` |
| TanStack Router（SPA，Vite） | `["index.html"]` | `</body>` | `html` |
| TanStack Start（SSR） | `["src/routes/__root.tsx"]` | `<Scripts` | `jsx` |
| Astro | `[" <root layout .astro>"]` | `</body>` | `html` |
| 多页（每路由独立 HTML） | `["public/**/*.html"]`，在对外服务的目录上做 glob | `</body>` | `html` |

选一个每个文件里都存在的锚点（`</body>` 几乎总有效）；`insertAfter` 则在一行之后匹配。多页站点优先用 glob，新页面就能自动纳入。页面由生成器重建的站点，注入只能活到下一次重新生成：每次构建后重新运行 `impeccable live`（accept 不受影响；它经 fallback 流程写真正的源码）。

**框架适配器（注入时自动检测）。**每次注入都把写入内容记录在 `.impeccable/live/inject-journal.json`；下一次注入或移除会修复崩溃或停错目录留下的残留。SvelteKit、Nuxt 与 TanStack Start 会对文档壳做服务端渲染，入口模板里的裸 `<script>` 未必可靠执行；`impeccable live-inject` 会识别它们并转给专用适配器（SvelteKit：基于 `+layout.svelte` 的仅开发期根组件；Nuxt：仅开发期的 `.client.ts` 插件；TanStack Start：在 `__root` 里生成仅开发期的 `ImpeccableLiveRoot` 组件）。`files` 的值仍是有效的检测/CSP 提示，但不再是字面插入点。普通 TanStack Router SPA 走基线 Vite 路径。

## 配置漂移

每次 boot 都会扫描常见页面根（`public/`、`src/`、`app/`、`pages/`）下、解析后的 `files` 列表未覆盖的 HTML 文件；它们以 `configDrift.orphans` 连同提示浮出。每会话告诉用户一次哪些文件未被覆盖，并提议补充或把 `files` 换成 glob。绝不自动改配置；由用户决定。无漂移时 `configDrift` 为 `null`。

## CSP 检测（仅首次）

下面所有放行一律仅限开发环境，手动改中间件和 meta 标签也一视同仁。不要为了让 localhost 助手加载而去改已部署生产站点的 CSP；生产环境检查的替代办法见 [live.md](live.md)。

若 `config.cspChecked === true`，整节跳过；用户已被问过一次。

```bash
.claude/skills/impeccable/scripts/impeccable detect-csp
```

输出 `{ shape, signals }`；shape 指明*补丁机制*，因此一个模板覆盖多个框架：

- **`null`**：无 CSP；写入配置并带上 `cspChecked: true`，到此为止。
- **`append-arrays`**：CSP 是结构化的指令数组；可自动打补丁（带 `additionalScriptSrc`/`additionalConnectSrc` 的 monorepo 助手、SvelteKit `kit.csp.directives`、Nuxt `nuxt-security`）。
- **`append-string`**：CSP 是字面值字符串；可自动打补丁（`next.config.*` 内联的 `headers()`、Nuxt `routeRules`）。
- **`middleware`** / **`meta-tag`**：检测到但不自动打补丁。把检测到的文件展示给用户，请其手动把 `http://localhost:8400` 加进 `script-src` 与 `connect-src`，然后标记 `cspChecked: true` 并继续。

### 同意提示（照用这段话）

> **需要打 CSP 补丁。**我在你的项目里检测到一个内容安全策略（CSP），它拦着 `http://localhost:8400`：没有放行，live 取色器加载不了。我要做的改动是：
>
> ```diff
> [file: <patchTarget>]
> [exact diff, 2-5 lines]
> ```
>
> 它由 `NODE_ENV === "development"` 守护，所以这条额外条目只出现在开发环境，绝不会进入生产。你随时可以通过回退这个文件移除它。要应用吗？[y/n]

回答"否"：跳过补丁，说明在手动加放行之前 live 无法工作，但仍写入 `cspChecked: true`（问题已问过）。回答"是"：按下文该 shape 的补丁执行，然后写入 `cspChecked: true`。助手的端口要到首次成功 boot 才知道，所以放行写的是 8400，即助手的首选端口；如果那次 boot 报出不同的 `serverPort`（别的项目的助手占了 8400），在选择取色点之前把该端口加进同一条放行。

### append-arrays

在持有 CSP 数组的文件顶部附近声明，然后往 script-src 与 connect-src 数组追加 `...__impeccableLiveDev`：

```ts
// Dev-only allowance so impeccable live mode can load. Guarded by NODE_ENV.
const __impeccableLiveDev =
  process.env.NODE_ENV === "development" ? ["http://localhost:8400"] : [];
```

分框架：Next.js + monorepo 助手：改*应用自己的* `next.config.*`（不是共享助手），往 `additionalScriptSrc` / `additionalConnectSrc` 追加。SvelteKit：`svelte.config.js` 的 `kit.csp.directives['script-src']` 与 `['connect-src']`。Nuxt + nuxt-security：`nuxt.config.*` 的 `security.headers.contentSecurityPolicy['script-src']` 与 `['connect-src']`。参考产出：[nextjs-turborepo/expected-after-patch.ts](https://github.com/pbakaus/impeccable/blob/8dac6ae7e020c43ab10ce9b41939f6fd42627b96/tests/framework-fixtures/nextjs-turborepo/expected-after-patch.ts)、[sveltekit-csp/expected-after-patch.js](https://github.com/pbakaus/impeccable/blob/8dac6ae7e020c43ab10ce9b41939f6fd42627b96/tests/framework-fixtures/sveltekit-csp/expected-after-patch.js)。幂等性：若 `__impeccableLiveDev` 已存在于文件中，即视为补丁已应用；只需标记 `cspChecked: true`。

### append-string

两点式补丁：声明一个仅开发期的字符串，把它内插进两条指令的 CSP 值（带前导空格以便干净拼接；作为编辑的一部分，把字面量改成模板字符串）：

```ts
// Dev-only allowance so impeccable live mode can load.
const __impeccableLiveDev =
  process.env.NODE_ENV === "development" ? " http://localhost:8400" : "";
```

- `script-src 'self' 'unsafe-inline'` 变为 `` `script-src 'self' 'unsafe-inline'${__impeccableLiveDev}` ``
- `connect-src 'self'` 变为 `` `connect-src 'self'${__impeccableLiveDev}` ``

分框架：Next.js 是 `next.config.*` 里内联的 `headers()`；Nuxt 是 `nuxt.config.*` 里的 `routeRules['/**'].headers['Content-Security-Policy']`。参考产出：[nextjs-inline-csp/expected-after-patch.js](https://github.com/pbakaus/impeccable/blob/8dac6ae7e020c43ab10ce9b41939f6fd42627b96/tests/framework-fixtures/nextjs-inline-csp/expected-after-patch.js)、[nuxt-csp/expected-after-patch.ts](https://github.com/pbakaus/impeccable/blob/8dac6ae7e020c43ab10ce9b41939f6fd42627b96/tests/framework-fixtures/nuxt-csp/expected-after-patch.ts)。

## 排障

若用户对 CSP 补丁答了"否"、之后报告 live 不可用：是他们的开发环境 CSP 拦着 `http://localhost:8400`。从 `.impeccable/live/config.json` 删掉 `cspChecked`，重新运行 `impeccable live`；设置流程会再问一次。

设置完成后，重新运行 `impeccable live`。
