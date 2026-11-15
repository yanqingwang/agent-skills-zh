> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/plan-devex-review/dx-hall-of-fame.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# DX 名人堂参考

只读当前审查轮次对应的小节。不要加载整个文件。

## Pass 1：入门体验

**黄金标准：**
- **Stripe**：7 行代码完成一次收款。登录后文档会预填你的测试 API 密钥。Stripe Shell 在文档页面里运行 CLI。无需本地安装。
- **Vercel**：`git push` 即全球 CDN 上的在线站点，带 HTTPS。每个 PR 都有预览 URL。一条 CLI 命令：`vercel`。
- **Clerk**：`<SignIn />`、`<SignUp />`、`<UserButton />`。3 个 JSX 组件，开箱即用的邮箱、社交登录与 MFA 认证。
- **Supabase**：创建一个 Postgres 表，立即自动生成 REST API + Realtime + 自述文档。
- **Firebase**：`onSnapshot()`。3 行代码实现跨所有客户端的实时同步，离线持久化内建。
- **Twilio**：控制台里的虚拟电话。不用买号码、不用信用卡即可收发 SMS。结果：激活率提升 62%。

**反面模式：**
- 在任何价值之前先要邮箱验证（打断流程）
- 沙箱之前要求信用卡
- 多路径的"自选冒险"（决策疲劳；一条黄金路径胜出）
- API 密钥藏在设置里（Stripe 把它们预填进代码示例）
- 无语言切换的静态代码示例
- 文档站与控制台分离（上下文切换）

## Pass 2：API/CLI/SDK 设计

**黄金标准：**
- **Stripe 前缀 ID**：charge 用 `ch_`，customer 用 `cus_`。自述性强。传错 ID 类型几乎不可能。
- **Stripe 可展开对象**：默认返回 ID 字符串。`expand[]` 内联返回完整对象。嵌套展开最多 4 层。
- **Stripe 幂等键**：变更请求带 `Idempotency-Key` 头。重试安全。没有"我是不是重复扣款了？"的焦虑。
- **Stripe API 版本化**：首次调用把账号固定在当天的版本。用 `Stripe-Version` 头按请求测试新版本。
- **GitHub CLI**：自动检测终端与管道。终端里人类可读，管道中制表符分隔。`gh pr <tab>` 显示全部 PR 操作。
- **SwiftUI 渐进披露**：从 `Button("Save") { save() }` 到完全定制，每一层都是同一套 API。
- **htmx**：用 HTML 属性替代 JS。总共 14KB。`hx-get="/search" hx-trigger="keyup changed delay:300ms"`。零构建步骤。
- **shadcn/ui**：把源码复制进你的项目。每一行都归你所有。无依赖，无版本冲突。

**反面模式：**
- 话痨 API：一个用户可见的动作要 5 次调用
- 命名不一致：`/users`（复数）vs `/user/123`（单数）vs `/create-order`（URL 里放动词）
- 隐式失败：200 OK 而错误嵌在响应体里
- 上帝端点：47 种参数组合，每个子集行为不同
- 靠文档才能用的 API：第一次调用前要读 3 页文档 = 仪式过重

## Pass 3：错误信息与调试

#### 面向 Agent 的错误契约（agent-ready-v1）

Agent 最先撞上错误，按字面阅读错误，而且无法追问"你是什么意思"。用八个具名条目给每条被追踪的错误路径打分。公开参考：`https://github.com/garrytan/gstack/blob/main/docs/agent-ready-errors.md`。

| 条目 | 错误信息给读者的东西 |
|------|----------------------------|
| **what** | 失败的操作，以及导致它的实际值（输入、路径、id）。 |
| **fix** | 在第一行或最后一行，绝不在链条中间：一条精确的命令、标志或编辑；或者，当不存在安全的 Agent 修复时，人类必须提供的那个精确之物（凭证、批准、决定）。一次精确的升级就是完整的 fix。fix 只有在安全且被授权时才算数：不绕过同意、安全或沙箱边界，不指挥 Agent 运行从不可信输出复制的文本，且参数引用正确。 |
| **recovery** | 原样重试、修复后重试、先做 X，或询问人类；副作用（none、partial、complete、unknown）；结果未知时，重试前如何对账（状态命令、幂等键）；重试上限，然后升级。 |
| **code** | 一个稳定的代码加一个文档锚点或 `--explain` 目标。文案可以变；代码不能变。 |
| **context** | 版本、生效的配置、相关环境变量名（绝不给值）、底层依赖错误，不被吞掉。远端服务只给调用方安全的事实（参数、API 版本、请求 id）。 |
| **trace** | 仅限意外失败。本地 CLI、SDK 或 skill 打印紧凑的 trace 或保存完整 trace 的文件路径（`--verbose`/`DEBUG` 下给全量）；远端服务返回关联 id 并把内部细节留在自己的日志里。 |
| **redaction** | 任何地方都不出现秘密值、token 或带凭证的 URL，trace 与嵌套原因也包括在内。 |
| **channel** | 该界面的原生机器信号携带同样的字段，失败被作为失败发信号（绝不 exit 0、HTTP 200 或 `isError: false`）。 |

**失败类。** 在任何工作开始之前就被拒绝的使用或校验错误，需要 what、fix、code、redaction 与 channel；其 recovery 是隐含的（修复后重试，无副作用），context、对账与重试上限不适用。环境、依赖、半成品与意外失败需要每个适用条目。trace 只适用于意外失败。

**界面。** 按 Applicability Gate 的产品类型键控：
- **CLI Tool：** channel 是 stderr 加一个不同的非零退出码，工具提供结构化输出时再加 `--json` 形式。
- **API/Service：** channel 是 HTTP 状态加 RFC 9457 problem-details 正文；context 对调用方安全；trace 是关联 id。
- **Library/SDK：** channel 是携带 code 与字段的类型化错误类；没有退出码。
- **Platform：** 错误到达哪个界面，就按那个界面的 CLI 或 API 规则。
- **Documentation：** 仅 what、fix、code 与 redaction。
- **Claude Code Skill：** channel 是 skill 打印的结果行与 code。MCP 工具（一种子情况）返回 `isError: true`，字段放在文本或结构化内容里。

**证据。** 每条路径上的每个条目记 pass、fail、N/A（带理由）或 unknown。在计划评审中，计划引入的路径上从未写明且适用的条目是缺口（fail）；unknown 只留给无法检查的既有行为。在线审计中，你从未触发的错误类是 unknown，不是外推。

**上限。** 每个上限都要指名其后的路径与条目，并展示更正后的错误行。
- **4/10（Critical 发现，标题 `CAP4:<path>:<item> <what fails>`）：** 路径泄露秘密、把失败发信号为成功、给出不安全的 fix，或阻塞等待终端（挂起，或因缺终端而失败且未给出 `--yes` 这类非交互替代）。
- **6/10（High 发现，标题 `CAP6:<path>:<item> <what fails>`）：** 路径缺少适用的 fix、recovery、context 或 trace 条目。

每个模式（DX TRIAGE 在内）都报告每条 CAP4 发现。

**校准。** 前三个例子展示单个条目做得好；没有一个单独满足所有条目。

**Elm（what、fix、第一行可读）：**
```
-- TYPE MISMATCH ---- src/Main.elm
I cannot do addition with String values like this one:
42|   "hello" + 1
     ^^^^^^^
Hint: To put strings together, use the (++) operator instead.
```
第一人称、完整句子、精确位置、建议修复。

**Rust（code、fix、`--explain`）：**
```
error[E0308]: mismatched types
 --> src/main.rs:4:20
help: consider borrowing here
  |
4 |     let name: &str = &get_name();
  |                       +
```
稳定的 code 配 `rustc --explain E0308`，主次标签，以及展示精确编辑的 help 行。

**Stripe API（code、文档锚点、结构化 channel）：**
```json
{"error":{"type":"invalid_request_error","code":"resource_missing","message":"No such customer: 'cus_nonexistent'","param":"customer","doc_url":"https://stripe.com/docs/error-codes/resource-missing"}}
```

**面向 Agent 的 CLI 错误（每个适用条目）。** stderr，exit 3：
```
deploy: push to registry.example.com/acme/api:1.4.2 failed: 401 unauthorized (REGISTRY_AUTH)
  cause: docker login token in ~/.docker/config.json expired; nothing was pushed (side effects: none)
  context: deploy 2.8.0, docker 27.1, config ./deploy.toml, env DEPLOY_REGISTRY set
  fix: run `deploy login --registry registry.example.com`, then rerun the same command (safe to retry once)
  docs: https://deploy.example.com/errors#REGISTRY_AUTH
```
用 `--json` 时，同样的字段成为带扩展成员的 RFC 9457 problem-details 对象：
```json
{"type":"https://deploy.example.com/errors#REGISTRY_AUTH","title":"Registry push unauthorized",
 "detail":"push to registry.example.com/acme/api:1.4.2 failed: 401","instance":"req_7f3a",
 "code":"REGISTRY_AUTH","fix":"deploy login --registry registry.example.com",
 "recovery":{"action":"fix_and_retry","side_effects":"none","max_retries":1},
 "context":{"version":"2.8.0","config":"./deploy.toml","env":["DEPLOY_REGISTRY"]}}
```
意外崩溃会追加 `trace: ~/.deploy/logs/crash-2026-10-16T18-02.log (rerun with
--verbose to print it)`。远端 API 返回 `instance` 作为关联 id，并把 trace 留在自己的日志里。`recovery.action` 的取值是 retry | fix_and_retry | do_first | ask_human；
`side_effects` 的取值是 none | partial | complete | unknown，为 unknown 时必须带 `reconcile`（一个状态命令）。这些成员名只是示例；按含义打分，不按拼写。

**一个部分达标的例子，gstack 自己的工作流错误：**
```
findings.jsonl:12: severity must be one of Critical, High, Medium, Low, Informational (ARTIFACT_SCHEMA)
```
它覆盖 what（文件、行、约束）、code（带承载 `fix:` 的 `docs/troubleshooting.md` 锚点）与 channel（exit 1）。它缺少行内的 fix、recovery 类与 context。它会被评为 CAP6:fix。

**标准映射。** CLI Agent Spec (cli-agent-spec.github.io)：按退出码的 `retryable` 与 `side_effects` → recovery。RFC 9457：`type` → code + 文档锚点，`detail` → what，`instance` → 远端服务的 trace。Stripe：`code` + `doc_url` → code。MCP 工具：模型可读的 `isError: true` 结果 → channel。clig.dev "Errors"：读者所在位置的可行行，意外错误的调试信息 → fix、trace。

**反面模式：** TypeScript 把"Did you mean?"埋在链条中间：把 fix 放在第一行或最后一行。`Error: operation failed` 配 exit 0。没有终端附着时挂起的提示。打印 API token 的堆栈 trace。

## Pass 4：文档与学习

**黄金标准：**
- **Stripe docs**：三栏布局（导航 / 内容 / 实时代码）。登录时注入 API 密钥。语言切换器在所有页面持久。悬停高亮。浏览器内调用 API 的 Stripe Shell。构建并开源了 Markdoc。文档不定稿，功能不上线。文档贡献影响绩效评估。
- 52% 的开发者被文档缺乏阻塞（Postman 2023）
- 拥有世界级文档的公司采用率提升 2.5x
- "文档即产品"：随功能一起发布，否则功能不发布

## Pass 5：升级与迁移路径

**黄金标准：**
- **Next.js**：`npx @next/codemod upgrade major`。一条命令升级 Next.js、React、React DOM，并运行所有相关 codemod。
- **AG Grid**：v31 起每个 release 都带 codemod。
- **Stripe API 版本化**：内部一个代码库。按账号固定版本。破坏性变更从不突袭你。
- **Martin Fowler 的 pipeline 模式**：组合小而可测的变换，而不是一个单体 codemod。
- Maven Central 中 21.9% 的破坏性变更未写文档（Ochoa et al., 2021）

## Pass 6：开发者环境与工具

**黄金标准：**
- **Bun**：比 npm install 快 100x，比 Node.js 运行时快 4x。速度就是 DX。
- 每天平均被打断 87 次；每次恢复要 25 分钟。开发者每天只写 2-4 小时代码。
- DXI 每提升 1 分 = 每位开发者每周节省 13 分钟。
- **GitHub Copilot**：任务完成快 55.8%。PR 时间从 9.6 天到 2.4 天。

## Pass 7：社区与生态

- 开发工具售出前需要约 14 次曝光（Matt Biilmann, Netlify）。与季度 OKR 周期不兼容。
- 开发者体验强的团队有 4-5x 的绩效乘数（DevEx framework）。

## Pass 8：DX 度量

**三个学术框架：**
1. **SPACE**（Microsoft Research, 2021）：满意度、绩效、活动、沟通、效率。至少度量 3 个维度。
2. **DevEx**（ACM Queue, 2023）：反馈循环、认知负荷、心流状态。结合感知数据与工作流数据。
3. **Fagerholm & Munch**（IEEE, 2012）：认知、情感、意动。心理学"心智三部曲"。

## Claude Code Skill DX 清单

在评审 Claude Code skill、MCP server 或 AI agent 工具的计划时使用。

- [ ] **AskUserQuestion 设计**：每次调用只问一个问题。重新锚定上下文（项目、分支、任务）。视觉反馈转交浏览器。
- [ ] **状态存储**：全局（~/.tool/）vs 每项目（$SLUG/）vs 每会话。审计轨迹用只追加 JSONL。
- [ ] **渐进同意**：带标记文件的一次性提示。绝不重问。可撤销。
- [ ] **自动升级**：带缓存 + 暂缓退避的版本检查。迁移脚本。内联提供。
- [ ] **Skill 组合**：受益链。审查链式调用。带小节跳过的内联调用。
- [ ] **错误恢复**：从失败处继续。保留部分结果。检查点安全。
- [ ] **Agent 可读错误**：每个错误满足面向 Agent 的错误契约（Pass 3）：安全的 fix、recovery 类、code、context，以及带 code 的结果行。
- [ ] **会话连续性**：时间线事件。压缩恢复。跨会话学习。
- [ ] **有界自主**：清晰的操作上限。破坏性操作强制升级。审计轨迹。

参考实现：gstack 的 design-shotgun 循环、自动升级流程、渐进同意、分层存储。
