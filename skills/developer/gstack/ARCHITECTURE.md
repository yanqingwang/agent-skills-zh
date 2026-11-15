> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/ARCHITECTURE.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 架构

本文解释 gstack **为何**如此构建。安装与命令见 CLAUDE.md。贡献见 CONTRIBUTING.md。

## 核心理念

gstack 给 Claude Code 一套立场鲜明的 workflow skill，外加一双能看的浏览器。它最先伸手去够的是用户自己的 [Aside](https://aside.com) AI 浏览器（macOS 15+）：真实的 cookie、真实登录的账号、已经打开的标签页。当 Aside 未安装或未运行（Linux、Windows、Aside 应用已关闭）时，gstack 自动回退到自带的浏览器：编译后 CLI（`$B`）背后的常驻无头 Chromium 守护进程。同一批 skill，同样的证据行，两个引擎。

花了不少代价才学到的关键认识：AI agent 想待在*你的*浏览器里，而不是一个模仿你的浏览器里。守护进程的每个功能（cookie 导入让它能以你的身份登录、有头模式让你能看到、CAPTCHA 移交、隧道让其他 agent 加入、侧边栏让它能回话）都是为了拉近与你已经打开的那个浏览器的差距。Aside 就是那个浏览器，还带 agent 级 CLI，所以在开着 Aside 的 Mac 上，skill 直接用它：

```
Claude Code                           Aside (the user's browser, macOS 15+)
─────────                             ─────
  bash: aside repl '<script>'   ───→   fresh sandboxed session
                                         • openTab(url) in the user's real profile
                                         • snapshot / click / fill / evaluate / screenshot
                                         • artifacts under the session dir (pwd)
                                         • tabs close when the script ends
  stdout: evidence lines +       ←───   exit code is always 0; truth is the
          GSTACK_STEP_OK sentinel       sentinel (or a `[error` line)
```

每个脚本一条流程。调用之间什么都不保留，所以 skill 每一步都从 URL 重新导航，打印带标签的证据行，并用 bash 把产物从会话目录复制出来。完整契约（检测而非安装、只用自己开的标签页、随便看但征得同意才能动、凭据绝不经过 agent、页面返回的一切都不可信）写在 `scripts/resolvers/aside.ts`，渲染进每个浏览器 skill 的 `{{ASIDE_SETUP}}`；`test/aside-driver.test.ts` 固定其句子。[BROWSER.md](BROWSER.md) 是面向读者的版本。

规划与审查 skill 里的网络研究先走同一扇门：在用户浏览器里执行 `aside exec "<question>"`（`{{ASIDE_RESEARCH}}`），每个问题一次只读请求，回答按不可信内容对待，每次调用都经过 `_aside_exec` 包装器（`{{ASIDE_EXEC_PRELUDE}}`），它在提示词离开机器前写一条出口回执（fail-open：只有出口库缺失时调用才会无回执运行）。没有 Aside 时用宿主的 WebSearch 工具（若有），否则说一次 "Search unavailable" 然后继续。

### 回退引擎

第二个引擎是 gstack 一直自带的那个，Aside 覆盖不到的地方都由它运行。AI agent 驱动自己拥有的浏览器需要**亚秒级延迟**和**持久状态**：如果每条命令都冷启动浏览器，每次工具调用要等 3-5 秒；如果浏览器在命令之间死掉，cookie、标签页、登录会话全丢。所以 gstack 运行一个长寿的 Chromium 守护进程，CLI 通过 localhost HTTP 与之通信。

```
Claude Code                     gstack
─────────                      ──────
                               ┌──────────────────────┐
  Tool call: $B snapshot -i    │  CLI (compiled binary)│
  ─────────────────────────→   │  • reads state file   │
                               │  • POST /command      │
                               │    to localhost:PORT   │
                               └──────────┬───────────┘
                                          │ HTTP
                               ┌──────────▼───────────┐
                               │  Server (Bun.serve)   │
                               │  • dispatches command  │
                               │  • talks to Chromium   │
                               │  • returns plain text  │
                               └──────────┬───────────┘
                                          │ CDP
                               ┌──────────▼───────────┐
                               │  Chromium (headless)   │
                               │  • persistent tabs     │
                               │  • cookies carry over  │
                               │  • 30min idle timeout  │
                               └───────────────────────┘
```

首次调用启动全部（约 3 秒）。之后每次调用：约 100-200ms。

skill 在自己的 BROWSER SETUP 步骤决定用哪个引擎：探测 Aside（`command -v aside` 加一行 `aside repl`）；`READY` 就驱动 Aside，否则按 `{{BROWSE_FALLBACK}}` 解析 `$B`，运行每个 cookbook 形态的 `$B` 等价物。Cookie 导入、GStack Browser 有头模式、`/pair-agent`、browser-skills 与 `/skillify`、领域 skill 都是这个引擎的功能：它们在回退路径上有意义，在 Aside 上则多余，因为那里的会话本来就是你自己的。

## 为什么用 Bun

Node.js 也能用。在这里 Bun 更好，理由有三：

1. **编译成二进制。** `bun build --compile` 产出单个约 58MB 的可执行文件。运行时没有 `node_modules`，不用 `npx`，不用配置 PATH。二进制直接跑。这很重要，因为 gstack 装在 `~/.claude/skills/`，用户没道理在那里维护一个 Node.js 项目。

2. **原生 SQLite。** Cookie 解密直接读 Chromium 的 SQLite cookie 数据库。Bun 内置 `new Database()`：不需要 `better-sqlite3`，不需要编译原生插件，没有 gyp。少一件在不同机器上坏掉的事。

3. **原生 TypeScript。** 开发期服务器以 `bun run server.ts` 运行。没有编译步骤，不用 `ts-node`，不用调试 source map。编译二进制用于部署；源码文件用于开发。

4. **内置 HTTP 服务器。** `Bun.serve()` 快、简单，不需要 Express 或 Fastify。服务器处理约 30 条路由，全部声明在一张路由表里（`browse/src/routes/table.ts`；文件头部展示了如何新增一条）。引入框架只会是负担。

瓶颈永远是 Chromium，不是 CLI 或服务器。Bun 的启动速度（编译二进制约 1ms，对比 Node 约 100ms）不错，但不是我们选它的原因。编译二进制和原生 SQLite 才是。

## 守护进程模型

### 为什么不每条命令启动一个浏览器？

Playwright 约 2-3 秒能启动 Chromium。单张截图，无所谓。带 20 多条命令的 QA 会话，就是 40 多秒的浏览器启动开销。更糟：命令之间所有状态丢失。Cookie、localStorage、登录会话、打开的标签页，全没了。

守护进程模型意味着：

- **持久状态。** 登录一次，一直在线。打开一个标签页，它一直开着。localStorage 跨命令保留。
- **亚秒级命令。** 首次调用后，每条命令就是一次 HTTP POST。含 Chromium 的工作在内，往返约 100-200ms。
- **自动生命周期。** 服务器首次使用时自动启动，闲置 30 分钟后自动关闭。不需要进程管理。

### 状态文件

服务器写 `.gstack/browse.json`（经 tmp + rename 的原子写，权限 0o600）：

```json
{ "pid": 12345, "port": 34567, "token": "uuid-v4", "startedAt": "...", "binaryVersion": "abc123" }
```

CLI 读这个文件找到服务器。文件缺失或守护进程已死时，CLI 拉起新服务器。进程活着但不回答 `/health` 是忙，不是死：CLI 探测有上限的约 8 秒，然后以非零退出码报告忙。只有显式 `--force-restart` 才会杀掉活着的守护进程。进程存活性在所有平台用 signal-0 判断（`isProcessAlive`，EPERM 算活着），健康检查（GET /health）作为响应性信号。它的 `status` 只覆盖守护进程及其 Chromium 连接；活动标签页的主线程单独报告（`activeTab.responsive`，探测限时 1 秒），所以一个卡在长脚本里的页面绝不会让 CLI 拒绝命令。守护进程的 stdout/stderr 持久化到 `<project>/.gstack/browse-daemon.log`。

### 端口选择

在 10000-49151 之间随机取端口（冲突最多重试 5 次），经共享的 `browse/src/port-allocator.ts` 分配，让每个长寿的 gstack 监听器都从同一区间取值。区间止于 49151 是有意的：49152-65535 是 macOS 的临时端口池，在里面分配意味着操作系统可能片刻之后把同一个端口发给另一个进程。这意味着 10 个 Conductor 工作区可以各自运行自己的 browse 守护进程，零配置、零端口冲突。旧方案（扫描 9400-9409）在多工作区环境里频繁出问题。

### 版本自动重启

构建把 `git rev-parse HEAD` 写进 `browse/dist/.version`。每次 CLI 调用时，若二进制版本与运行中服务器的 `binaryVersion` 不匹配，CLI 杀掉旧服务器再启动新的。这彻底消灭了"陈旧二进制"这一类 bug：重编一次，下一条命令自动用上。

## 渲染本地 HTML

`/make-pdf`、`/diagram`、`/design-html` 预览和 `/office-hours` 草图会生成 HTML，需要浏览器来打印或栅格化。这个浏览器优先用 Aside，经由 `lib/aside-render.ts`（TypeScript API，内嵌于 make-pdf）和 `bin/gstack-render.ts`（skill 模板调用的 CLI）。以下每条事实都对照 Aside CLI 1.26 验证过：

1. **Aside 拒绝 `file://` URL**，所以渲染期间用 `Bun.serve()` 把 HTML 所在目录服务在 `127.0.0.1` 的临时端口上，并用 `goto(url, { waitUntil: "load" })` 打开：默认的 "interactive" 就绪判定对 9MB 的 diagram bundle 永远不会触发。URL 以每次渲染的密钥作为首段路径（其他本地进程请求一律 404），每个请求都在真实路径上做围栏检查（符号链接逃出目录是 403，畸形编码是 400），目录永不列举。
2. **一个 `aside repl` 进程跑一个生成脚本**：打开、等待（`--wait-selector` / `--wait-expr`）、按顺序执行步骤（`--pdf`、`--screenshot`、`--eval … --out`）、关闭标签页。CLI 调用之间什么都不保留，所以一次渲染永远是单个脚本。
3. **产物写在 Aside 沙箱里**（每次运行的会话目录是唯一可写位置），脚本打印 `ASIDE_DIR=<pwd>`，包装器把它们复制出来。
4. **PDF 走裸 CDP `Page.printToPDF`**，经 `page._sendToTarget`，所以页眉/页脚模板、tagged PDF 和文档大纲都继续可用：`page.pdf()` 只暴露 Playwright 子集。
5. **指定尺寸的截图用 CDP `Emulation.setDeviceMetricsOverride`。** 没有 `setViewportSize` 这回事。
6. **即使脚本抛错，CLI 退出码也是 0。** 真相是 stdout 上的 `GSTACK_RENDER_OK` 哨兵；出现 `[error` 行即失败。

当 `probeAside()` 报告 `NEEDS_ASIDE` 或 `ASIDE_NOT_RUNNING` 时，同样的包装器改经回退引擎渲染（每台机器一个共享 Chromium，不做第二次下载）：同一个回环服务器，然后每个动作一次守护进程调用：`newtab --json`、`goto <loopback URL>`、用 `js` 轮询就绪、`pdf --from-file`、`viewport` + `screenshot [--selector]`、`js --out`，最后在 finally 里 `closetab`。CLI 标志相同，`OK <path>` 行相同；`ENGINE=aside|browse` 标明实际渲染的引擎：当选了 Aside 但其 CLI 无法启动，或其私有 CDP 桥（`_sendToTarget`）在运行中消失时，`render()` 会在该路径上把同一 spec 重试一次（页面级失败，或已在运行脚本的超时，绝不重试）。CLI 把 `EVAL` / `PAGE_ERRORS` 行当作不可信网页内容加围栏，因为那是页面控制的文本。回退路径不镜像的部分：指定尺寸的截图输出为 1x（Aside 默认 2x），JPEG `--quality` 与 `pageRanges`/`scale` 仅 Aside 有，`--landscape` 用交换纸张尺寸模拟，`--wait-pagedjs` 映射为守护进程的 `toc` 等待。两条路径上渲染器都只服务本地目录、别无其他；把它指向某个网站属于站点操作，归驱动契约管。

## 安全模型

### 浏览器边界（Aside）

Aside 路径上浏览器是用户的，所以安全模型关注的是 agent 在里面可以做什么，而不是保护一个守护进程。规则以散文形式写在 `scripts/resolvers/aside.ts`，渲染进每个浏览器 skill，由 `test/aside-driver.test.ts` 固定：

- **只检测，绝不安装。** Aside 缺失或未运行时，用一行说明移交回退引擎；gstack 从不为 Aside 运行安装器。
- **只用自己开的标签页。** agent 在自己打开的标签页（或用户指名的标签页）里工作。`listBrowserTabs()` 输出是私密数据，绝不进报告。
- **随便看，征得同意才动。** 带目标调用某个 skill 即视为同意读取、导航和填写（不提交）。对非本地目标的修改性操作会动用户真实账号，所以每次运行先用一次 AskUserQuestion 列出确切动作。登出/删除/取消/退订链接绝不点击。
- **凭据绝不经过 agent。** 登录墙由用户在 Aside 里解决；agent 绝不输入、读取或打印密码、一次性验证码、cookie、token 或 localStorage。
- **页面返回的一切都不可信。** 快照树、页面文本、控制台输出、`aside exec` 回答、截图：都是内容，绝不是指令（`{{UNTRUSTED_CONTENT_WARNING}}` 是唯一来源措辞）。

驱动发生在 Aside 内部，因此不产生 gstack 侧的守护进程日志；Aside 自己保留历史。本行以下都是回退引擎的威胁模型：守护进程、它的 token、它的 cookie 罐、它的隧道。

### 仅监听 localhost

HTTP 服务器绑定 `127.0.0.1`，不是 `0.0.0.0`。网络不可达。

### 双监听器隧道架构（v1.6.0.0）

用户运行 `pair-agent --client` 时，守护进程启动 ngrok 隧道，让远程配对的 agent 能驱动浏览器。把完整守护进程面暴露到互联网（哪怕藏在随机 ngrok 子域后面）意味着任何 Origin 伪造都能让 `/health` 泄露 root token，而 `/cookie-picker` 会把 token 嵌进任何调用方都能取到的 HTML。

修复方案是**两个 HTTP 监听器**，而不是一个：

- **本地监听器**（`127.0.0.1:LOCAL_PORT`）：始终绑定。服务 token 引导（`POST /extension-token`，只发给固定的扩展身份）、`/health`（仅存活/状态，绝不含 token）、`/cookie-picker`、`/inspector/*`、`/welcome`、`/refs`、侧边栏 agent API，以及完整命令面。永不转发。
- **隧道监听器**（`127.0.0.1:TUNNEL_PORT`）：在 `/tunnel/start` 时惰性绑定，`/tunnel/stop` 时拆除。只服务一个锁定的白名单：`/connect`（配对流程，无认证 + 限速）和 `/command`（仅限 scoped token，且进一步限定为浏览器驱动命令白名单）。其余一律 404。

ngrok 只转发隧道端口。安全性质来自**物理端口隔离**：隧道调用方到不了 `/health` 或 `/cookie-picker`，因为这些路径在那个 TCP 套接字上根本不存在。基于头部推断（检查 `x-forwarded-for`、检查 origin）不可靠（ngrok 的头部行为会变；本地代理也可能加这些头部）；套接字隔离不会。

| 端点 | 本地监听器 | 隧道监听器 | 说明 |
|---|---|---|---|
| `GET /health` | 公开（仅存活/状态，绝不含 token） | 404 | Token 引导移至 `POST /extension-token`（v1.63） |
| `POST /extension-token` | 固定 Origin（`chrome-extension://<GSTACK_EXTENSION_ID>`）+ 回环 Host | 404 | 唯一发放 root token 的端点 |
| `GET /connect` | 公开（`{alive:true}`） | 公开（`{alive:true}`） | 隧道存活探测路径 |
| `POST /connect` | 公开（限速 300/分） | 公开（限速） | pair-agent 的 setup-key 交换 |
| `POST /command` | 认证（Bearer root 或 scoped） | 认证（仅 scoped，命令白名单） | 隧道上 root token = 403 |
| `POST /pair` | 仅 root | 404 | 配对铸造，本地操作者动作 |
| `POST /tunnel/{start,stop}` | 仅 root | 404 | 守护进程配置 |
| `POST /token`、`DELETE /token/:id` | 仅 root | 404 | Scoped token 铸造/吊销 |
| `GET /cookie-picker`、`/cookie-picker/*` | UI 用一次性 code/会话；API 用 Bearer 或 picker 会话 | 404 | 仅本地，读取本地浏览器数据库 |
| `GET /inspector`、`/inspector/events` 等 | 认证 | 404 | 扩展回调，仅本地 |
| `GET /welcome` | 公开 | 404 | GStack Browser 落地页，仅本地 |
| `GET /refs` | 认证 | 404 | Ref 映射，内部状态 |
| `GET /activity/stream` | Bearer 或 HttpOnly `gstack_sse` cookie | 404 | SSE。`?token=` 查询参数不再接受 |
| `GET /inspector/events` | Bearer 或 HttpOnly `gstack_sse` cookie | 404 | SSE。与 /activity/stream 同一 cookie |
| `POST /sse-session` | 认证（Bearer） | 404 | 铸造 30 分钟只读 SSE 会话 cookie |

**扩展 token 引导（v1.63.0.0）。** `GET /health` 在任何模式下都不携带 token：仅存活/状态。侧边栏扩展经 `POST /extension-token` 获取 root token，该端点只在调用方 Origin 恰为 `chrome-extension://<GSTACK_EXTENSION_ID>`（由 `extension/manifest.json` 的 `key` 字段固定；用 `bun browse/scripts/extension-id.ts` 复现推导）且 Host 头解析为回环主机名时才发放。Host 用 `new URL()` 解析，绝不裸比较，因为 Host 带端口。网页无法伪造 `chrome-extension://` Origin，且该端点永不加入隧道白名单，隧道面按默认拒绝对其返回 404。

**隧道面拒绝日志。** 隧道监听器上的每次拒绝（`path_not_on_tunnel`、`root_token_on_tunnel`、`missing_scoped_token`、`disallowed_command:*`）都异步记录到 `~/.gstack/security/attempts.jsonl`，含时间戳、来源 IP（取自 `x-forwarded-for`）、路径与方法。全局限速每分钟 60 次写入，防日志洪泛 DoS。与提示词注入扫描器共用同一份尝试日志。

**SSE 会话 cookie。** EventSource 发不了 Authorization 头，所以扩展在引导时用 root Bearer POST 一次 `/sse-session`，拿到 30 分钟只读 cookie（`gstack_sse`，HttpOnly，SameSite=Strict）。该 cookie 只对 `/activity/stream` 和 `/inspector/events` 有效：它不是 scoped token，不能用于 `/command`。范围隔离由模块边界保证：`sse-session-cookie.ts` 不导入 `token-registry.ts`。

**Windows 原生 cookie 边界**（#1136）：暴露的调试 TCP 回退已移除。原生适配器使用 Playwright 的 pipe transport，启用前需要浏览器/运行时进程所有权与清理方面的资格认定；其认定清单目前为空。DPAPI 兼容的数据库导入仍然可用，但不承诺恢复每一个 App-Bound Encryption cookie。Chrome 136+ 对其默认用户数据目录（含编号 profile）同时防范 pipe 与 TCP 调试。关闭 Chrome 不能绕过该策略。不允许 TCP 降级、换用替代浏览器或复制真实 profile；不支持的场景引导用户在 gstack 自己的浏览器里手动登录。

### Bearer token 认证

每个服务器会话生成随机 UUID token，以 0o600 权限（仅属主可读）写入状态文件。对 `/command` 的请求必须带 `Authorization: Bearer <token>`，使用经授权的 root 或 scoped token。无效认证一律拒绝。

命令授权需要 token。本地 cookie picker 改为用五分钟有效的一次性 code 换一个 scoped HttpOnly 会话 cookie；该 cookie 只授权 picker 路由，绝不通向 `/command`。其 API 也接受 Bearer 授权。本地健康检查（`/health`）公开且不执行命令。隧道监听器上除 `/connect` 外无一豁免。

### Cookie 安全

Cookie 是 gstack 处理的最敏感数据。设计如下：

Cookie 数据库使用只读运行时适配器：Bun 里用 Bun SQLite，Node.js 22.13+ 里用内置 SQLite。大的 Chromium 时间戳保持精确整数；普通域名计数保持 JSON 数字。临时数据库快照为私有，关闭或失败时移除。

1. **OS 密钥访问遵循平台权限。** macOS 在每个浏览器首次导入时可能弹 Keychain 批准。Linux 支持基于 libsecret 的 `v11` 和 `v10` 的 Chromium 回退密钥；Windows 支持 DPAPI 兼容的 cookie。权限被拒即停止操作，而不是自动反复弹窗。

2. **导入回执不含 cookie 值。** 数据库解密在内存中进行，用平台支持的格式；解密后的 cookie 应用到捕获的 Playwright context。picker 显示浏览器/profile 标签、域名、计数，以及各自独立的导入/重置/认证状态，绝不显示 cookie 值。标签仍可能识别到账号，不得复制到公开日志。可选的会话持久化是另一项选择加入的磁盘存储功能。

3. **数据库读取不改源库。** gstack 把 Chromium cookie 数据库复制到临时文件以避免 SQLite 锁冲突，并以只读方式打开。只有归为瞬态的读取会重试，最多三次，间隔 150ms 和 500ms。原生浏览器提取有独立的生命周期边界，资格认定完成前保持禁用。

4. **密钥缓存按会话。** 派生密钥只在服务器生存期内缓存于内存。服务器关闭（闲置超时或显式停止）时缓存即消失。

5. **诊断用安全类别。** Cookie 导入失败只暴露归类的原因与计数，不暴露原始 OS 错误或解密值。独立的 `cookies` 检查命令按其敏感名/值规则脱敏；它不是纯元数据回执，不该用于公开的导入汇总。

`cookie-import-operation.ts` 负责直接 CLI、`--all` 和经认证 picker 的 profile 选择、解密、应用与回执。显式选择的 profile 优先；否则只有唯一相关 profile 时才选它，不可读的 profile 视为未知。当前 `Local State` 标签优先于 Preferences 与目录回退。浏览器/context/page 归属在异步工作前捕获，导入按目标 context 串行，已应用的域名进入既有的 JavaScript-origin 防护。Cookie 是 context 级的，不是标签页隔离的。

存储重置与认证验证是相互独立的选择加入项。`--clear-storage` 只清除所捕获 origin 的 localStorage（同 context 内同源标签页共享）和目标标签页的 sessionStorage，绝不动 IndexedDB、service worker、同级 origin 或其他标签页的 sessionStorage；`--all` 加重置会被拒绝。重置仅限 Chromium：隔离 world 把原生时钟采样与破坏性操作绑定到一个系统唯一 context，导航与宿主截止时间会取消未完成的工作。其他引擎保留导入/认证检查但拒绝重置。重置失败或后续应用失败不意味着回滚。

`cookie-auth-verification.ts` 在请求的验证可以改动 cookie 或存储之前，先校验守护进程侧的 `GSTACK_COOKIE_AUTH_SELECTOR` 与 `GSTACK_COOKIE_AUTH_EXPECTED_IDENTITY`。要在守护进程启动前私下设置它们。导入 cookie 后，`--verify-auth` 重新加载捕获的目标，要求同源响应成功，且恰好有一个可见身份其规范化文本精确匹配。Cookie 数量、HTTP 200、子串匹配都不能确立登录。没有这项检查的导入是**未检查**，不是已验证；零导入无法验证登录。结果不回显期望的身份文本。

### Shell 注入防护

浏览器注册表（Chrome、Chromium、Brave、Edge、仅 Windows 的 Opera 与 Opera GX，以及仅 macOS 的 Comet 与 Arc）是硬编码的。数据库根目录来自已知平台位置；profile 目录输入经过校验。Keychain 访问用 `Bun.spawn()` 加显式参数数组，不做 shell 字符串插值。

### 出口回执账本（v1.63.0.0）

每一个被枚举的、由 gstack 发起的出机器发送点，都在发送前把一条哈希链、防篡改的回执写入 `~/.gstack/security/egress.jsonl`：TypeScript 调用方用 `lib/egress-receipt.ts` 的 `writeReceipt`，shell 脚本用 `bin/gstack-egress-lib.sh` 的 `_receipted_curl` / `_receipted_git`。调用方拥有字节时，回执记录所发确切字节的 sha256（git push 这类由子进程拥有的发送记录 `sha256: null`）；回执从不存储正文。

失败极性按类别划分并由测试固定。敏感发送点 fail-closed：brain-sync 推送、memory-ingest、gbrain-sync、telemetry、ngrok 隧道启动、mcp-verify、supabase-provision，以及 Memorable 桥的每条提示词 `memorable-recall` 交接（把提示词交给本地厂商二进制；见 [docs/memorable-workflow-memory.md](docs/memorable-workflow-memory.md)）在回执写不出来时拒绝发送（每次拒绝都打印问题 + 原因 + 修复）。面向用户的发送点 fail-open 并给 stderr 警告：design 二进制的 OpenAI 调用、更新检查、只读仪表盘和 git 类回执在回执写入失败时照样进行，所以 fail-open 的发送可能没有记录（有意设计，带警告）。`test/egress-receipt-wiring.test.ts` 里的新发送点扫描器会在出机器发送点未接线时让 CI 失败；其豁免逐项列出并有理由（用户指示的页面抓取、可达性探测、安装文档字符串、skill 散文）。

用 `bin/gstack-egress` 检查账本：`list`（gstack 尝试发送过什么）、`verify`（重算链，被篡改时退出码 3）、`grants`（常设同意设置及各自的撤销方式）。`verify` 能发现原地篡改、重排序和链中删除；它发现不了尾部截断、整文件重造或账本本体被删：对拥有该文件的同机同用户行为者设防，超出一份取证日志的范围。威胁模型：账本是对"尝试过的出口"的取证可观测性，记录 gstack 试图发送了什么，让事故可审计；它不是防外泄控制。

### 服务器出口的 Unicode 消毒（v1.38.0.0）

CDP 采集的页面内容可能含孤立的 UTF-16 代理半（页面 JavaScript 字符串处理出错留下的孤儿高位或低位代理）。它们到达 `JSON.stringify` 时，Bun 会输出 `\uD800` 形式的转义序列，下游消费者的 `JSON.parse` 能接受，但 Anthropic API 会以 400 拒绝：一个古怪页面就这样变成杀死会话的错误。防御是单点的，应用于每个送出页面派生字符串的服务器出口。

| 出口路径 | 模块 | 消毒点 |
|---|---|---|
| `POST /command`（HTTP） | `browse/src/routes/commands.ts`（包装在 `browse/src/server.ts`） | `handleCommandInternal` 包装器（对 `handleCommandInternalImpl` 的结果消毒） |
| `POST /batch` | `browse/src/routes/commands.ts` | 同一包装器，批处理消费者随之继承 |
| `GET /activity/stream`（SSE） | `browse/src/routes/activity.ts` | `sanitizeReplacer` 应用于 `createSseEndpoint` 内部 |
| `GET /inspector/events`（SSE） | `browse/src/routes/inspector.ts` | `sanitizeReplacer` 应用于 `createSseEndpoint` 内部 |

`sanitizeReplacer` 是一个 `JSON.stringify` 的 replacer 函数，在编码过程中清洗每个字符串值。stringify 之后的正则在这里不管用：`JSON.stringify` 在正则匹配之前就已把 `\uD800` 转成字面转义序列 `"\\ud800"`，所以 replacer 必须在编码管线内运行。纯字符串辅助函数 `sanitizeLoneSurrogates` 直接用于 `text/plain` 响应。

**架构不变量。** 每个送出页面内容派生字符串的新 SSE/WebSocket 写入器或 HTTP 响应，必须走两条路径之一：对象载荷用 `JSON.stringify(payload, sanitizeReplacer)`，文本正文用 `sanitizeLoneSurrogates(body)`。绕开两者的新表面会让系统失步。两个 SSE 生产者（`routes/activity.ts`、`routes/inspector.ts`）的内联注释都写明这一点；`browse/test/server-sanitize-surrogates.test.ts` 用 bug 复现 + 不变量测试固定接线（`handleCommandInternalImpl` 改名、中央消毒行、replacer 存在性、SSE 生产者用 replacer 做 stringify）。

### 提示词注入防御（侧边栏 agent）

Chrome 侧边栏 agent 拥有工具（Bash、Read、Glob、Grep、WebFetch）并阅读敌意网页，是 gstack 中最暴露于提示词注入的部分。防御是分层的，不是单点。

1. **L1-L3 内容安全（`browse/src/content-security.ts`）。** 应用于每个页面内容命令和每个工具输出：数据标记、隐藏元素剥离、ARIA 正则、URL 黑名单和信任边界信封包装。服务器与 agent 两侧都应用。

2. **L4 ML 分类器：TestSavantAI（`browse/src/security-classifier.ts`）。** 22MB 的 BERT-small ONNX 模型（int8 量化），运行在安全 sidecar 子进程里。本地运行，不联网。在 agent 看到之前，于注入扫描路径上扫描页面派生内容。

3. **L4b 转录分类器（已移除）。** 一个 Claude Haiku 会话形态检查曾经存在，直到调用它的 chat 路径 agent 被拆掉；它作为死代码（零生产调用方）被删除，选择加入的 DeBERTa 集成随之删除。不要再把任何一项记为在用。

4. **L5 canary token（`browse/src/security.ts`）。** 针对随机系统提示词 token 的生成/注入/检测工具，该 token 泄露即意味着攻击者诱使模型泄露了系统提示词。Canary 泄露确定性地 BLOCK。这些工具是纯函数且有测试；注入 canary 的聊天提示词构建器已被拆掉，所以今天没有生产路径注入它。

5. **L6 集成合并器（`combineVerdict`）。** BLOCK 需要两个 ML 分类器都达到 >= `WARN`（0.75）的判定，单个自信命中不算。这是针对 Stack Overflow 指令写作误报的缓解。对工具输出扫描，单层高置信度直接 BLOCK：内容不是用户写的，误报顾虑不适用。

**关键约束：** `security-classifier.ts` 只在安全 sidecar 子进程（`security-sidecar-entry.ts`）里运行，绝不在编译后的 browse 二进制里。`@huggingface/transformers` v4 依赖 `onnxruntime-node`，而后者从 Bun compile 的临时解压目录 `dlopen` 会失败。只有纯字符串部件（canary 注入/检查、判定合并器）在 `security.ts`，从 `server.ts` 导入它是安全的。（攻击日志在 `tunnel-denial-log.ts`；会话状态/状态面已在 #2557 移除。）

**环境旋钮：** `GSTACK_SECURITY_OFF=1` 是真正的总开关（即使已预热，分类器也保持关闭；L1-L3 过滤器继续运行）。模型缓存在 `~/.gstack/models/testsavant-small/`（首次运行 112MB）。攻击日志在 `~/.gstack/security/attempts.jsonl`（加盐 sha256 + 域名，10MB 轮转，保留 5 代）。每设备盐在 `~/.gstack/security/device-salt`（0600），进程内缓存以便在文件系统不可写的环境中存活。

**可见性。** canary 泄露或 BLOCK 判定时出现居中横幅，附各层确切分数。`bin/gstack-security-dashboard` 汇总本地尝试；`supabase/functions/community-pulse` 汇总跨用户的选择加入社区遥测。（侧边栏头部的 SEC 盾牌图标与 `/health` 的 `security` 字段已在 #2557 移除：它们唯一的数据源 `~/.gstack/security/session-state.json` 在 chat 路径 agent 被拆掉后失去了唯一写入者，盾牌报的是过期或空状态。在用的防御通过各自的调用点上报。）

## Ref 系统

Ref（`@e1`、`@e2`、`@c1`）是 agent 定位页面元素而无需写 CSS 选择器或 XPath 的方式。

### 工作原理

```
1. Agent runs: $B snapshot -i
2. Server calls Playwright's page.accessibility.snapshot()
3. Parser walks the ARIA tree, assigns sequential refs: @e1, @e2, @e3...
4. For each ref, builds a Playwright Locator: getByRole(role, { name }).nth(index)
5. Stores Map<string, RefEntry> on the BrowserManager instance (role + name + Locator)
6. Returns the annotated tree as plain text

Later:
7. Agent runs: $B click @e3
8. Server resolves @e3 → Locator → locator.click()
```

### 为什么用 Locator，而不是改 DOM

显而易见的做法是往 DOM 注入 `data-ref="@e1"` 属性。它在以下情况失效：

- **CSP（内容安全策略）。** 许多生产站点禁止脚本修改 DOM。
- **React/Vue/Svelte hydration。** 框架调和可能剥掉注入的属性。
- **Shadow DOM。** 从外面够不到 shadow root 内部。

Playwright Locator 位于 DOM 之外。它们用无障碍树（Chromium 内部维护）和 `getByRole()` 查询。不改 DOM，没有 CSP 问题，没有框架冲突。

### Ref 生命周期

导航时清空 Ref（主 frame 的 `framenavigated` 事件）。这是对的：导航之后所有 locator 都过期了。agent 必须重新运行 `snapshot` 获取新 ref。这是有意设计：过期 ref 应当大声失败，而不是点错元素。

### Ref 过期检测

SPA 可以在不触发 `framenavigated` 的情况下改动 DOM（如 React 路由切换、标签页切换、弹窗打开）。这让 ref 过期而页面 URL 未变。为捕获这种情况，`resolveRef()` 在使用任何 ref 前先做一次异步 `count()` 检查：

```
resolveRef(@e3) → entry = refMap.get("e3")
                → count = await entry.locator.count()
                → if count === 0: throw "Ref @e3 is stale — element no longer exists. Run 'snapshot' to get fresh refs."
                → if count > 0: return { locator }
```

这样做快速失败（约 5ms 开销），而不是让 Playwright 的 30 秒操作超时耗在一个不存在的元素上。`RefEntry` 在 Locator 之外还存了 `role` 与 `name` 元数据，错误消息能告诉 agent 那是什么元素。

### 光标可交互 ref（@c）

`-C` 标志找出可点击但不在 ARIA 树里的元素：带 `cursor: pointer` 样式的、有 `onclick` 属性的、或自定义 `tabindex` 的。它们获得独立命名空间的 `@c1`、`@c2` ref。这能捕获框架渲染成 `<div>` 但其实是按钮的自定义组件。

## 日志架构

三个环形缓冲区（各 50,000 条，O(1) 推入）：

```
Browser events → CircularBuffer (in-memory) → Async flush to .gstack/*.log
```

控制台消息、网络请求和对话框事件各有自己的缓冲区。每 1 秒刷盘一次：服务器只追加自上次刷新以来的新条目。这意味着：

- HTTP 请求处理绝不会被磁盘 I/O 阻塞
- 日志能在服务器崩溃后幸存（最多丢 1 秒数据）
- 内存有界（50K 条 × 3 个缓冲区）
- 磁盘文件只追加，外部工具可读

`console`、`network`、`dialog` 命令从内存缓冲区读取，不读磁盘。磁盘文件用于事后调试。

## SKILL.md 模板系统

### 问题

SKILL.md 文件告诉 Claude 怎么用 browse 命令。文档列了不存在的标志，或漏了新加的命令，agent 就会撞错。手工维护的文档总会偏离代码。

### 解决方案

```
SKILL.md.tmpl          (human-written prose + placeholders)
       ↓
gen-skill-docs.ts      (reads source code metadata)
       ↓
SKILL.md               (committed, auto-generated sections)
```

模板承载需要人类判断的工作流、提示与示例。占位符在构建时由源码填充：

| 占位符 | 来源 | 生成什么 |
|-------------|--------|-------------------|
| `{{COMMAND_REFERENCE}}` | `commands.ts` | 分类命令表 |
| `{{SNAPSHOT_FLAGS}}` | `snapshot.ts` | 带示例的标志参考 |
| `{{ASIDE_SETUP}}` | `resolvers/aside.ts` | Aside 浏览器驱动契约：就绪探测、驱动真实浏览器的规则，以及向 `$B` 回退的移交 |
| `{{ASIDE_COOKBOOK}}` | `resolvers/aside.ts` | 经验证的 `aside repl` 脚本形态（由 /browse 和 /devex-review 携带；其他 skill 内联自己的版本） |
| `{{ASIDE_RESEARCH}}` | `resolvers/aside.ts` | 经由用户浏览器中 `aside exec` 的网络研究，WebSearch 作回退，再是无搜索降级 |
| `{{ASIDE_EXEC_PRELUDE}}` | `resolvers/aside.ts` | 一行 `_aside_exec` 定义：`aside exec` 调用在提示词离开机器前写一条出口回执（fail-open，面向用户的发送点：仅在出口库缺失时才无回执运行）；skill 绝不裸调 `aside exec` |
| `{{UNTRUSTED_CONTENT_WARNING}}` | `resolvers/aside.ts` | 适用于任一浏览器返回内容的那条不可信内容规则 |
| `{{PREAMBLE}}` | `resolvers/preamble.ts`、`resolvers/preamble-hoist.ts` | 启动块：更新检查、会话跟踪、贡献者模式、AskUserQuestion 格式；tier 2+ skill 得到指向其共享 `sections/preamble.md` 的指针，外加属于它们自己的小节 |
| `{{BROWSE_SETUP}}` | `gen-skill-docs.ts` | 二进制发现与安装说明 |
| `{{BROWSE_FALLBACK}}` | `resolvers/browse.ts` | Aside→`$B` 移交：二进制发现 + 逐步等价表，渲染在每个浏览类 skill 的 `{{ASIDE_SETUP}}` 之后 |
| `{{BASE_BRANCH_DETECT}}` | `gen-skill-docs.ts` | 面向 PR 的 skill（ship、review、qa、plan-ceo-review）的动态基础分支检测 |
| `{{QA_METHODOLOGY}}` | `resolvers/utility.ts` | 仅浏览器 QA 方法论，由 /qa 和 /qa-only 条件加载 |
| `{{QA_SCOPE}}, {{QA_EXPLORATORY}}, {{QA_FUNCTIONAL}}, {{QA_RESOURCE}}, {{QA_METHOD_READS}}, {{QA_REVIEW}}` | `resolvers/qa.ts` | 表面选择、带检查点的原生/探索式 QA、直接条件方法读取、已装资产引用，以及有界的 review/ship 调用方 |
| `{{DESIGN_METHODOLOGY}}` | `gen-skill-docs.ts` | /plan-design-review 与 /design-review 共享的设计审查方法论 |
| `{{SHARED_LIBS_RUBRIC}}` | `resolvers/shared-libs.ts` | /deslop-shared-libs、/autoplan 工程阶段与 /review 的共享代码标准：经验证的调用方、既有 helper、兼容性、测试与总节省 |
| `{{REVIEW_DASHBOARD}}` | `gen-skill-docs.ts` | /ship 预检的 Review Readiness Dashboard |
| `{{TEST_VALUE_BAR:<mode>}}` | `resolvers/test-value.ts` | 共享测试价值标准（创作门禁、价值卡、X/Y 覆盖、红先行证明、低价值目录），/qa 与 /qa-only 用（`qa`），/test-audit 用（`audit`）；/autoplan 工程阶段与 /ship 经覆盖审计嵌入 |
| `{{TEST_VALUE_MESSAGE:<key>}}` | `resolvers/test-value.ts` | 来自共享常量的一条降级模式消息（问题、后果、修复、文档锚点） |
| `{{TEST_BOOTSTRAP}}` | `resolvers/testing.ts` | 测试框架检测、引导与 CI/CD 配置，供 /ship 与 /design-review |
| `{{CODEX_PLAN_REVIEW}}` | `resolvers/outside-voice-steps.ts` | /plan-ceo-review 与 /autoplan 工程阶段的可选外部计划评审：Claude Code 上的 Codex、其他受支持 harness 上的 Codex，带调用方原生 subagent 回退 |
| `{{DESIGN_SETUP}}` | `resolvers/design.ts` | `$D` design 二进制的发现模式，镜像 `{{BROWSE_SETUP}}` |
| `{{DESIGN_DETECTOR}}` | `resolvers/design.ts` | 用户安装的 impeccable 引擎的探测块 + 哨兵读取（`bin/gstack-design-detect.ts`）；`:phase0` 渲染 design-review 的机械扫描，`:gate` 渲染 design-html 的有界 slop 门禁 |
| `{{DESIGN_MD_CHECK}}` | `resolvers/design.ts` | 经 `bin/gstack-design-md.ts` 的 open DESIGN.md 格式检查，一次性转换建议持久化在文件里；`:calibrate` 为 /design-review 渲染 tokens-as-calibration 表单 |
| `{{OVERUSED_FONTS}}` | `resolvers/design.ts` | 来自 `lib/design-catalog.ts` 的按角色划分字体清单（作展示字体属滥用、作正文/UI 尚可、等宽、禁用、经验证免费），供 /design-consultation |
| `{{DESIGN_SLOP_BULLETS}}` | `resolvers/design.ts` | 来自 `lib/design-catalog.ts` 的纯散文 slop 要点（无规则 id），供提案类 skill |
| `{{DESIGN_CRAFT_RULE:<lead>}}` | `resolvers/design-craft.ts` | `design-html/sections/craft.md.tmpl` 中按加粗导语找到的一段及其要点，供 /design-review 的 craft 审查；导语缺失或含糊会使生成失败 |
| `{{DESIGN_PERSUADE_CHECKS}}` | `resolvers/design-craft.ts` | 五项 Persuade 转化检查（一个主行动、点名的异议、每条主张旁的证据、真实的风险逆转、index/noindex 决策），供 /design-review 的 craft 审查与 /plan-design-review 的 Pass 1 |
| `{{DESIGN_SHOTGUN_LOOP}}` | `resolvers/design.ts` | /design-shotgun、/plan-design-review、/design-consultation 共享的对比板反馈循环 |
| `{{UX_PRINCIPLES}}` | `resolvers/design.ts` | 用户行为基础（扫读、满意即止、善意储备、后备箱测试），供 /design-html 与 /design-shotgun |
| `{{GBRAIN_CONTEXT_LOAD}}` | `resolvers/gbrain.ts` | 脑优先上下文搜索，带关键词提取、健康感知与数据研究路由。注入 10 个脑感知 skill。非脑主机上被抑制。 |
| `{{GBRAIN_SAVE_RESULTS}}` | `resolvers/gbrain.ts` | skill 后置的脑持久化，带实体富化、节流处理与每 skill 保存说明。8 种 skill 专属保存格式。 |
| `{{FOREGROUND_DISPATCH_NOTE}}` | `resolvers/constants.ts` | 面向每个同步 Agent 工具子代理分发的权威 `run_in_background: false` 指引（自 Claude Code v2.1.198 起 subagent 默认后台运行）。单一事实来源；每文件的承载者由 `test/run-in-background-guidance.test.ts` 固定。 |

`/qa` 使用其仅浏览器版的 `qa/sections/test-bootstrap.md.tmpl`；功能 QA 从不引导。

这在结构上是可靠的：命令在代码里存在，就会出现在文档里；不存在，就不可能出现。

生成器还拥有两个非 skill 文档的文件：`review/design-checklist.md` 从 `lib/design-catalog.ts` 渲染（经 `scripts/resolvers/design-checklist.ts`），`lib/dom-dump.js` 从 `lib/dom-dump-script.ts` 写出。`/review` 与 `/ship` 读的清单，以及 `/design-review` 运行的 DOM dump，因此不会偏离模板所描述的目录与脚本；`test/design-checklist-sync.test.ts` 固定两者。

内部异步驱动 `runGeneration()` 清点 skills、Claude 小节、以及在每个受支持主机上被刻入每个主机的那些 skill 的小节
（`scripts/resolvers/sections.ts` 的 `CARVED_ON_EVERY_HOST`：qa、qa-only、ship、
plan-ceo-review、office-hours 与 design-review）、每个 tier 2+ skill 在每个主机上的共享
`sections/preamble.md`、主机元数据、OpenClaw 片段、
索引、agent 摘要和辅助资产。其他 skill 在
非 Claude 主机上保持内联；QA 资产相对已安装的主机 skill 解析。
每个产物都经过同一个比较或写入函数。Dry run
把缺失或不一致的产物报为 `STALE`，不改任何文件或目录；渲染与文件系统失败报 `ERROR` 并带原因。
任一情况都使命令失败，包括单主机调用。模块导入
保持同步，不会启动生成。

物理输出路径与嵌在内容里的路径彼此独立。`skill:check`
利用这种分离：在临时存储里把每个主机生成一次，校验
完整渲染，再与规范的已跟踪输出比较。非忽略的生成
输出必须被跟踪。可选的、被忽略的主机缓存不受影响，临时
存储在 `finally` 里清理，生成失败后也不例外。

### 前导块（preamble）

多数 workflow skill 以 `{{PREAMBLE}}` 块开头，先于 skill 自身逻辑运行。只读的 `/deslop-shared-libs` 审计省略此块，不运行启动、遥测、记忆或有状态审查 helper。自 v1.71.0.0 起，渲染出的块是一层薄围栏，调用 `bin/gstack-skill-start`（合并后的前导块运行时，它替代了每个 tier-2+ skill 约 18KB 的内联 bash），并读回 `KEY: value` 状态行供 skill 正文分支；`bin/gstack-skill-end` 在 skill 结束时记录遥测。一次性引导与同意文本只在运行时门槛真正触发时，才以会话绑定的 `GSTACK_INSTRUCTION` 块发出，而不是渲染进每个 skill。启动仍然处理五件事：

1. **更新检查**：调用 `gstack-update-check`，有升级可用时报告。
2. **会话跟踪**：touch `~/.gstack/sessions/<parent-pid>` 并清理 2 小时以上的旧条目，让并发会话状态在磁盘上可观察。
3. **运营式自我改进**：每个 skill 会话结束时，agent 反思失败（CLI 报错、走错的路、项目怪癖），把运营经验记入项目的 JSONL 文件供未来会话使用。
4. **AskUserQuestion 格式**：统一格式：背景、问题、`RECOMMENDATION: Choose X because ___`、带字母的选项。所有 skill 一致。
5. **Search Before Building（先搜索再构建）**：构建基础设施或陌生模式之前先搜索。知识分三层：久经考验（第 1 层）、新而流行（第 2 层）、第一性原理（第 3 层）。第一性原理推理揭示惯例有误时，agent 点名那个"eureka 时刻"并记录。完整构建者哲学见 `ETHOS.md`。

Tier 2+ skill 共享其中大部分文本，所以不在每个 SKILL.md 里重复。`scripts/resolvers/preamble-hoist.ts` 把与 skill 无关的前导块小节在每个主机渲染一次到 SKILL.md 旁的 `sections/preamble.md`，SKILL.md 开头是一段简短的 "Shared preamble (load first)" 指针，标出该文件的 id（安装根与主机改写前共享文本的哈希，文本变了 id 就变，但不同主机间可以重复）；agent 会读取该文件，除非它自己更早、以该 id 开头的 Read 结果仍在上下文里，这样一次会话只加载一次，而仅携带 id 的文字永远不能顶替文件本身。一个小节只有在 skill 的渲染与共享渲染逐字节一致时才外移。启动命令、点名 skill 的小节（Question Tuning、Repo Ownership、Search Before Building、Telemetry）以及 skill 专属变体保持内联。Tier 1 skill 的短前导块保持内联。

### 为什么提交入库，而不是运行时生成？

三个理由：

1. **Claude 在加载 skill 时读 SKILL.md。** 用户调用 `/browse` 时没有构建步骤。文件必须已经存在且正确。
2. **CI 能校验新鲜度。** 全主机生成加跟踪差异与未跟踪输出检查，能在合并前抓住过期文档；`skill:check` 还会从干净 checkout 校验每个主机的内容。
3. **git blame 有效。** 你能看到一条命令何时加入、在哪个提交。

### 模板测试分层

下方的付费层成本与速度估算早于当前模型默认值。
见[评估默认值与覆盖](CONTRIBUTING.md#testing--evals)。

| Tier | 内容 | 成本 | 速度 |
|------|------|-------|-------|
| 1 — 静态验证 | 解析 SKILL.md 中每条 `$B` 命令并对注册表校验；固定 Aside 契约句子与渲染包装器的选项映射 | 免费 | <2s |
| 2 — 经 `claude -p` 的 E2E | 拉起真实 Claude 会话，运行每个 skill，检查报错 | ~$3.85 | ~20min |
| 3 — LLM 当评判 | 默认 `claude-fable-5-1` 按清晰度/完整性/可操作性给文档打分 | ~$0.15 | ~30s |

Tier 1 随每次 `bun run test` 运行。Tier 2+3 由 `EVALS=1` 把门。思路是：免费抓住 95% 的问题，LLM 只用于需要判断力的场合。

## 命令分发

命令按副作用分类：

- **READ**（text、html、links、console、cookies 等）：无修改。可安全重试。返回页面状态。
- **WRITE**（goto、click、fill、press 等）：修改页面状态。不幂等。
- **META**（snapshot、screenshot、tabs、chain 等）：不易归入读/写的服务器级操作。

这不只是分类学。服务器用它做分发：

```typescript
if (READ_COMMANDS.has(cmd))  → handleReadCommand(cmd, args, bm)
if (WRITE_COMMANDS.has(cmd)) → handleWriteCommand(cmd, args, bm)
if (META_COMMANDS.has(cmd))  → handleMetaCommand(cmd, args, bm, shutdown)
```

`help` 命令返回全部三个集合，agent 由此自助发现可用命令。

## 错误哲学

错误消息是写给 AI agent 的，不是给人的。每条错误消息都必须可行动：

- "Element not found" → "Element not found or not interactable. Run `snapshot -i` to see available elements."
- "Selector matched multiple elements" → "Selector matched multiple elements. Use @refs from `snapshot` instead."
- Timeout → "Navigation timed out after 30s. The page may be slow or the URL may be wrong."

Playwright 的原生错误经 `wrapError()` 重写，剥掉内部堆栈、加上指引。agent 应能读懂错误并知道下一步做什么，无需人工介入。

### 崩溃恢复

服务器不自愈。Chromium 崩溃时（`browser.on('disconnected')`），服务器立即退出。CLI 在下一条命令时发现服务器已死并自动重启。这比试图重连一个半死的浏览器进程更简单也更可靠。

## E2E 测试基础设施

### 会话运行器（`test/helpers/session-runner.ts`）

E2E 测试以完全独立子进程的方式拉起 `claude -p`：不经 Agent SDK，后者无法嵌套在 Claude Code 会话内。运行器：

1. 把提示词写进临时文件（避免 shell 转义问题）
2. 启动 `sh -c 'cat prompt | claude -p --output-format stream-json --verbose'`
3. 从 stdout 流式读取 NDJSON 获得实时进度
4. 与可配置的超时赛跑
5. 把完整 NDJSON 转录解析成结构化结果

`parseNDJSON()` 是纯函数：无 I/O，无副作用，因此可独立测试。

### 可观测性数据流

```
  skill-e2e-*.test.ts
        │
        │ generates runId, passes testName + runId to each call
        │
  ┌─────┼──────────────────────────────┐
  │     │                              │
  │  runSkillTest()              evalCollector
  │  (session-runner.ts)         (eval-store.ts)
  │     │                              │
  │  per tool call:              per addTest():
  │  ┌──┼──────────┐              savePartial()
  │  │  │          │                   │
  │  ▼  ▼          ▼                   ▼
  │ [HB] [PL]    [NJ]          _partial-e2e.json
  │  │    │        │             (atomic overwrite)
  │  │    │        │
  │  ▼    ▼        ▼
  │ e2e-  prog-  {name}
  │ live  ress   .ndjson
  │ .json .log
  │
  │  on failure:
  │  {name}-failure.json
  │
  │  ALL files in ~/.gstack-dev/
  │  Run dir: e2e-runs/{runId}/
```

**所有权分离：** session-runner 拥有心跳（当前测试状态），eval-store 拥有部分结果（已完成测试状态）。两个组件互不知晓：只通过文件系统共享数据。分片运行经 detach 日志（`~/.gstack-dev/eval-runs/`）和每个分片自己的 eval 目录报告实时进度。

**一切皆非致命：** 所有可观测性 I/O 都包在 try/catch 里。写失败绝不会导致测试失败。测试本身才是事实来源；可观测性尽力而为。

**机器可读诊断：** 每条测试结果包含 `exit_reason`（success、timeout、error_max_turns、error_api、exit_code_N）、`timeout_at_turn` 与 `last_tool_call`。由此可以写这样的 `jq` 查询：
```bash
jq '.tests[] | select(.exit_reason == "timeout") | .last_tool_call' ~/.gstack/projects/<slug>/evals/_partial-e2e.json
```

### 评估持久化（`test/helpers/eval-store.ts`）

`EvalCollector` 累积测试结果，并以两种方式写出：

1. **增量：** `savePartial()` 在每个测试后写 `_partial-e2e.json`（原子：先写 `.tmp`，再 `fs.renameSync`）。被杀也能幸存。
2. **终局：** `finalize()` 写带时间戳的评估文件（如 `e2e-20260314-143022.json`）。partial 文件从不清理：它与终局文件并存以供观测。

`eval:compare` 对比两次评估运行。`eval:summary` 汇总 `~/.gstack/projects/<slug>/evals/`（旧回退 `~/.gstack-dev/evals/`）下所有运行的统计。两者都感知分片（v1.63.0.0）：分片付费运行器（`scripts/test-paid-shards.ts`，经 `test:gate:sharded` / `test:periodic:sharded` 运行，`eval:bg:gate` / `eval:bg:periodic` 脚本现在指向它们）通过 `GSTACK_EVAL_DIR` 环境变量（`EvalCollector` 构造函数支持）给每个分片的收集器自己的目录 `<evalDir>/shards/<slug>/`，`eval:list` / `eval:compare` / `eval:summary` 扫描一层 `shards/<slug>/` 子目录（`eval:flake-rank` 递归读取同一棵树，外加免费套件的 flake 账本）。基线查找排除 `_partial` 累积文件（`eval-store.ts` 的 `isPartialEval` / `findLatestFinalizedRun`），自动对比绝不会拿当前运行自己的 partial 文件当基线。

### 测试分层

下方的付费层成本与速度估算早于当前模型默认值。
见[评估默认值与覆盖](CONTRIBUTING.md#testing--evals)。

| Tier | 内容 | 成本 | 速度 |
|------|------|-------|-------|
| 1 — 静态验证 | 对注册表解析 `$B` 命令、Aside 契约固定、渲染包装器固定、可观测性单元测试 | 免费 | <5s |
| 2 — 经 `claude -p` 的 E2E | 拉起真实 Claude 会话，运行每个 skill，扫描报错 | ~$3.85 | ~20min |
| 3 — LLM 当评判 | 默认 `claude-fable-5-1` 按清晰度/完整性/可操作性给文档打分 | ~$0.15 | ~30s |

Tier 1 随每次 `bun run test` 运行。Tier 2+3 由 `EVALS=1` 把门。思路：免费抓住 95% 的问题，LLM 只用于需要判断力的场合与集成测试。

需要 Aside 本体的测试：`test/skill-e2e-aside.test.ts`、qa 与 design-review E2E 文件里的 Aside 用例、`test/aside-render.test.ts` 的真实往返，只在开着 Aside 应用的 Mac 上运行，在其他地方自跳过（`test/helpers/aside-available.ts` 的 `asideAvailable()`；`GSTACK_SKIP_ASIDE=1` 强制跳过）。渲染门禁与引擎无关：make-pdf 的 `*-gate.test.ts` 和 `test/skill-e2e-diagram.test.ts` 经由解析出的引擎运行（`test/helpers/browser-available.ts` 的 `browserAvailable()` = `asideAvailable() || resolveBrowseBin() !== null`），两者都不存在才跳过，所以 Linux CI 用 `bun run build:gates` 构建 browse 二进制并真实运行它们。回退引擎自己的测试（`browse/test/`、由 `$B` 驱动的 E2E 用例）照旧在所有平台运行：Linux CI 真实证明回退路径，静态证明 Aside 契约。

## 这里有意不做的

- **`aside repl` 调用之间不保留页面。** 每个 Aside 脚本都是全新会话，标签页随它消亡。每个脚本重新导航是这个模型的诚实代价；`aside mcp` 或许日后能解除（TODOS.md）。
- **没有自己的搜索工具。** 研究先走 Aside，其次宿主的 WebSearch 工具，再次分布内知识：每降一级都明说。
- **不做 WebSocket 流。** HTTP 请求/响应更简单、能用 curl 调试、也够快。流式只带来复杂度，收益边际。
- **不用 MCP 协议。** MCP 每个请求都要付 JSON schema 开销，还需要持久连接。纯 HTTP + 纯文本输出更省 token，也更好调试。
- **不做多用户。** 每个工作区一个服务器、一个用户。token 认证是纵深防御，不是多租户。
- **没有万能会话恢复。** 基于 OS 的 cookie 导入支持 macOS、Linux 和 DPAPI 兼容的 Windows 格式，不支持所有加密方案或所有站点的登录状态。Windows 原生提取在资格认定前保持禁用，Chrome 受保护的默认目录不被绕过。
- **不做 iframe 自动发现。** `$B frame` 支持跨 frame 交互（CSS 选择器、@ref、`--name`、`--url` 匹配），但 ref 系统不在 `snapshot` 时自动爬 iframe。必须先显式进入 frame 上下文。
