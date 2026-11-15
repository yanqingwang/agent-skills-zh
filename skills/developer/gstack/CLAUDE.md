> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/CLAUDE.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# gstack 开发

## 命令

```bash
bun install          # install dependencies
bun run dev <cmd>    # run CLI in dev mode, e.g. bun run dev goto https://example.com
bun run typecheck    # strict tsc over product code (zero errors required)
bun run typecheck:test  # test-code type-debt ratchet
bun run build        # gen docs + compile binaries
bun run gen:skill-docs  # regenerate SKILL.md files from templates
bun run skill:check  # health dashboard for all skills
bun run dev:skill    # watch mode: auto-regen + validate on change
bun run slop          # full slop-scan report (all files)
bun run slop:diff     # slop findings in files changed on this branch only
bun run audit:manifest  # file slices for /claude-api prompt-audit; rerun it at each frontier-model release (CONTRIBUTING.md)
```

测试与评估命令、各自的开销和前置条件汇总在一张表里：
[我该运行哪个命令？](CONTRIBUTING.md#which-command-do-i-run)。你最常用的两个是
`bun run test`（免费的验收）和 `bun run eval:bg:pr`（付费，覆盖变更部分）。已废弃的名字如
`test:evals` 和 `test:e2e` 会打印替代命令并以退出码 1 退出。

付费评估需要 `ANTHROPIC_API_KEY`。Codex E2E 测试（`test/codex-e2e.test.ts` 及其他 Codex 文件）使用 Codex 自己的认证：封闭式运行器只从
`${CODEX_HOME:-~/.codex}` 复制 `auth.json`，并在子进程环境里固定 `CODEX_HOME`，不需要
`OPENAI_API_KEY` 环境变量。

**封闭式 E2E 与环境变量键：** 每个 E2E 运行器都通过
`test/helpers/hermetic-env.ts` 启动子进程（白名单清洗过的环境变量、全新播种的
`CLAUDE_CONFIG_DIR`、临时 `GSTACK_HOME`、`--strict-mcp-config`）；每个测试的
`env:` 覆盖项最后合并到一个完整的封闭环境上，所以是安全的。
要在测试里输入 `/skill` 命令的 PTY 测试必须传 `seedSkills: true`。
用 `EVALS_HERMETIC=0` 针对真实操作者状态调试。完整细节
（env-shim、播种绊线、接线测试）：
[docs/TESTING_INTERNALS.md](docs/TESTING_INTERNALS.md)。

**测试选择与分层：** 分片的付费运行器（`test:pr`、
`eval:bg:pr`、`test:gate:sharded`）通过 `test/helpers/touchfiles.ts` 里的依赖清单从
`git diff` 选取测试（`EVALS_ALL=1` 强制全量；`eval:select` 预览 PR profile，`--profile full` 则是普通
touchfile 选择）。每个新 E2E 测试都要在 `E2E_TIERS` 里归类：安全护栏或
确定性功能测试归 `gate`；质量基准、Opus 模型测试、
非确定性或外部服务（Codex、Gemini）归 `periodic`。
`test/e2e-tier-alignment.test.ts` 强制执行该分层。CI 流水线与周期性
排除项：[docs/TESTING_INTERNALS.md](docs/TESTING_INTERNALS.md#test-selection-and-tiers)。

## 测试

```bash
bun run test         # final full free acceptance after focused repairs and source freeze
bun run eval:bg:pr   # required changed PR coverage, with explicit deferrals
```

遵循 [AGENTS.md 的验证纪律](AGENTS.md#validation-discipline)：
先用聚焦检查证明修复有效，完成必需的已选评估，
再在最终集成代码上完整跑一次免费套件。修复期间，
每次提交前用聚焦检查代替全量套件运行。

`bun run test` 经过 `scripts/test-free-shards.ts` 路由，其严格的
分片级分类会让缺少 bun 汇总行的分片直接失败。
`TREE_MUTATING` 列出仍在自己尾随串行分片里运行的文件（今天只有
`test/bootstrap-retention.test.ts`）。永远不要直接敲
`bun test` 跑套件：它会遍历整个仓库，加载付费评估文件，
还错过严格的分类器。`bun run test:pr` 运行所选的短时
真实行为测试与质量评判，并报告被推迟的宽覆盖项。发布前，
完整免费验收与必需的 PR 检查都必须通过。命令与实测目标见
[测试政策](CONTRIBUTING.md#test-tiers)。
需要 Aside 本体的测试会自跳过，除非某台 Mac 开着 Aside 应用。
分片打包、评判复用与引擎跳过：
[docs/TESTING_INTERNALS.md](docs/TESTING_INTERNALS.md#free-suite-runner-judge-reuse-and-engine-skips)。

新增或修改的测试遵循[测试价值标准](docs/test-value-bar.md)：每个测试都要
保护真实回归会破坏的行为，契约测试（SKILL.md golden 文件，以及下文定义的属于契约的提示词字节）保留。该标准的
源码是 `scripts/resolvers/test-value.ts`。

在本仓库，提示词字节只有在软件会读取它们时才算契约（某个
解析器、Hook、评分器或另一个 skill 消费这段确切文本），或有录制的
评估证明措辞重要。针对 skill 模板和生成的 SKILL.md 的
测试固定结构、步骤顺序、路由表、机器可读标记和
安全关键行；安全行按大小写不敏感、按语义而非大小写检查。行为留给 E2E 用例和评判。不要固定强调方式、
大小写、issue 编号，或行为检查已覆盖的句子，
重写改变了被固定的句子时，用结构级
或语义级检查替换该固定项，而不是固定新句子。术语定义在
[docs/test-value-bar.md](docs/test-value-bar.md)（"Prompt-byte contract"、
"Sentence pin"）。模板/SKILL.md 检查使用
`test/helpers/prompt-structure.ts`（`between`、
`expectTokens`、`expectAbsent`、`expectOrdered`、`expectMentions`）：
token 与顺序精确匹配，安全规则是
单句内大小写不敏感的关键词共现。
各项目用可选的 CLAUDE.md `## Test Coverage` 键调整 `/ship` 的覆盖率门禁，
默认全部缺省：`Minimum:`、`Target:`、`Generation cap:`（默认 5）、
`Base control:`（`auto` 或 `off`）、`Base control budget:`（秒，默认 90）与
`Star rating:`（`auto` 或 `off`）。

## 项目结构

完整注解目录树：[docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)。
速查：`browse/` 是 gstack 自带的无头浏览器 CLI（回退
引擎）加 `/browse` skill，`design/` 是 design 二进制，`make-pdf/` 是 PDF
二进制，`hosts/` 是带类型的主机配置，`scripts/` 是构建与开发效率工具
（gen-skill-docs、resolvers，其中 `resolvers/aside.ts` 是 Aside 契约），
`test/` 是验证与评估，`lib/` 是共享库（`aside-render.ts` 经
Aside 渲染本地 HTML，失败时回退到引擎；`design-catalog.ts` 是
每个设计 skill 都渲染的类型化设计反模式目录），`bin/`
是 CLI 工具（`gstack-render.ts` 是 skill 调用的渲染 CLI；
`gstack-design-detect.ts` 与 `gstack-design-md.ts` 是设计检测器
和 open-DESIGN.md 工具），`extension/` 是 Chrome
扩展，每个 skill 一个目录（`ship/`、`review/`、`qa/`……），
`.github/` 是 CI，`contrib/` 是贡献者工具，`docs/designs/` 是设计文档。

## SKILL.md 工作流

SKILL.md 文件是从 `.tmpl` 模板**生成**的。更新文档的步骤：

1. 编辑 `.tmpl` 文件（例如 `SKILL.md.tmpl` 或 `browse/SKILL.md.tmpl`）
2. 运行 `bun run gen:skill-docs`（或 `bun run build`，它会自动执行）
3. 把 `.tmpl` 和生成的 `.md` 文件一起提交，包括 tier 2+ skill 的
   `sections/preamble.md`（共享前导块，由
   `scripts/resolvers/preamble-hoist.ts` 渲染；要改就改 preamble resolver，永不改那个文件）

同一次 `gen:skill-docs` 运行还会从 `lib/` 写出两个生成文件：
`review/design-checklist.md`（来自 `lib/design-catalog.ts`，经
`scripts/resolvers/design-checklist.ts`）和 `lib/dom-dump.js`（来自
`lib/dom-dump-script.ts`）。编辑目录或脚本源码，重新生成，
两者一起提交；永远不要编辑生成文件
（`test/design-checklist-sync.test.ts` 在漂移时失败）。

生成使用各主机的 `defaultModel`（多数主机是 `claude`，Codex 是 `gpt`，Antigravity 的 `agy` 与 Gemini CLI 是 `gemini`），除非 `--model` 显式指定。Codex 安装还会读取
`${CODEX_HOME:-~/.codex}/config.toml` 的顶层模型；改了那个模型后重跑
`./setup --host codex`。注意：`bun run build` 和
裸跑 `gen:skill-docs --host codex` 渲染的是主机默认（gpt）：如果你的
Codex config.toml 固定了别的模型，之后重跑 `./setup --host codex`
恢复你的 profile（单一所有者持久化已记入
TODOS.md）。

skill 里的浏览器步骤是遵循
`scripts/resolvers/aside.ts` 的 `aside repl` 脚本，每个都带有回退
引擎对应的 `$B` 等价物。新增 browse 命令：加入 `browse/src/commands.ts` 并
重新构建。新增快照标志：加入 `browse/src/snapshot.ts` 的
`SNAPSHOT_FLAGS` 并重新构建。skill 模板中的本地 HTML 渲染
是一次 `bun run ~/.claude/skills/gstack/bin/gstack-render.ts` 调用；新渲染
选项进 `lib/aside-render.ts`（它负责回退），绝不进
skill 自己的 bash。

**体积预算：** 生成的 SKILL.md 超过 160KB（约 4 万 token）会告警；
`test/catalog-budget.test.ts` 给常驻加载的 skill 目录设置上限
`CATALOG_BUDGET_TOKEN_EQUIVALENTS`（当前 1,452；每个新 skill 都会推高它）；
`test/context-budget-ratchet.test.ts` 对照
`test/fixtures/context-budget.json` 固定每个 skill 的 token 上限
（正当增长或落地的缩减，重跑 `bun test/helpers/capture-context-budget.ts` 并在同一提交里提交
刷新后的 fixture）。理由与协议：
[docs/CONTRIBUTOR_REFERENCE.md](docs/CONTRIBUTOR_REFERENCE.md#skill-size-budgets)。

**SKILL.md 文件上的合并冲突：** 绝不要在生成的 SKILL.md
文件上用"接受任一方"解决冲突。正确做法：(1) 在 `.tmpl` 模板
和 `scripts/gen-skill-docs.ts`（事实来源）上解决冲突，(2) 运行 `bun run gen:skill-docs`
重新生成所有 SKILL.md 文件，(3) 暂存重新生成的文件。接受任一方的
生成输出会悄悄丢掉另一方的模板修改。

## 平台无关设计

Skill 绝不能硬编码框架特定的命令、文件模式或目录
结构。应当：

1. **读取 CLAUDE.md** 获取项目特定配置（测试命令、评估命令等）
2. **若没有就 AskUserQuestion**：让用户告诉你，或让 gstack 搜索仓库
3. **把答案持久化到 CLAUDE.md**，之后就再也不用问

这适用于测试命令、评估命令、部署命令和任何其他
项目特定行为。配置归项目所有；gstack 负责读取。

## 编写 SKILL 模板

SKILL.md.tmpl 文件是**供 Claude 阅读的提示词模板**，不是 bash 脚本。
每个 bash 代码块在独立的 shell 中运行：变量不会跨块保留。

规则：
- **用自然语言表达逻辑与状态。** 不要用 shell 变量在代码块之间传
  状态。改为告诉 Claude 要记住什么，并在正文里引用它（例如"第 0 步
  检测到的基础分支"）。
- **不要硬编码分支名。** 通过
  `gh pr view` 或 `gh repo view` 动态检测 `main`/`master` 等。面向 PR 的
  skill 使用 `{{BASE_BRANCH_DETECT}}`。正文里写"基础分支"，
  代码块占位符里写 `<base>`。
- **保持 bash 块自包含。** 每个代码块都应能独立工作。
  某块需要上一步的上下文时，在上面的正文里重述它。
- **用英文表达条件分支。** 不要在 bash 里嵌套 `if/elif/else`，
  改写编号决策步骤："1. 若 X，做 Y。2. 否则做 Z。"

## 写作风格（V1）

每个 tier ≥2 skill 的默认输出遵循
`scripts/resolvers/preamble/generate-writing-style.ts` 的 Writing Style 一节：术语首次出现时给注释（精选清单在
`scripts/jargon-list.json`，skill 运行时遇到第一个术语会 Read 它），提问用
结果语言（"如果你的用户……会坏掉什么"）而非实现语言，
句子短，决策落点带用户影响。想要更紧凑 V0 文风的高级用户设置
`gstack-config set explain_level terse`（二元开关，
无中间档）。完整设计理由见 `docs/designs/PLAN_TUNING_V1.md`。最初打算与写作风格
同行推进的审查节奏改造被拆到 V1.1，见 `docs/designs/PACING_UPDATES_V0.md`。

## 浏览器交互

gstack 优先驱动 Aside AI 浏览器（macOS 15+），Aside 缺席时回退到自己的
浏览器引擎。需要与浏览器交互
（QA、吃自己的狗粮、检查页面）时，使用 `/browse` skill：它探测 Aside
并在 `READY` 时驱动它，也就是用户的真实浏览器、真实会话，方式是遵循
`scripts/resolvers/aside.ts` 契约（`{{ASIDE_SETUP}}`）的
`aside repl` 脚本。每个浏览器 skill（`/qa`、
`/qa-only`、`/design-review`、`/canary`、`/benchmark`、`/scrape`）都这样做，
skill 里的网络研究先走 Aside 的 agent（`{{ASIDE_RESEARCH}}`）
再轮到 WebSearch 工具。探测结果是 `NEEDS_ASIDE` 或
`ASIDE_NOT_RUNNING`（Linux、Windows、Aside 应用未开）时，skill 按
`{{BROWSE_FALLBACK}}` 解析 `$B`，改跑 browse 二进制：在该语境下 `$B <command>`
是正当工具，cookie 导入、GStack Browser 有头
模式、`/pair-agent` 和 browser-skills/`/skillify` 都属于它。skill 自己生成的本地 HTML
（make-pdf、图表、设计预览）经
`bin/gstack-render.ts` / `lib/aside-render.ts` 渲染，它在
回环地址上提供该文件，并在 Aside 中打印或截图，Aside 缺席时用引擎：绝不要把渲染器指向某个网站。绝不使用
`mcp__claude-in-chrome__*` 工具：又慢又不可靠，也不是这个
项目用的东西。

**服务器 / 侧边栏 / 扩展内部机制：** 修改 `browse/src/server.ts`、
`extension/`、侧边栏 PTY、任何 SSE 端点或 CDP 会话代码前，先读
[docs/BROWSER_INTERNALS.md](docs/BROWSER_INTERNALS.md)：侧边栏消息流、
WebSocket 认证、隧道双监听器规则、出口处的 Unicode 消毒、
SSE/CDP 辅助函数、setup 符号链接加固、侧边栏安全栈都在那里，每项都有 CI 绊线固定。

**每个出机器的发送点都要有出口回执**（v1.63.0.0+）。每一次由 gstack 发起的
出机器发送，都必须在发送前写一条回执：TypeScript 调用方使用
`lib/egress-receipt.ts` 的 `writeReceipt`；shell 脚本 source
`bin/gstack-egress-lib.sh` 并使用 `_receipted_curl` / `_receipted_git`。
`test/egress-receipt-wiring.test.ts` 会在出现无回执的新发送点时让 CI 失败。
失败极性、扫描器豁免与 `_aside_exec` 包装器：
[docs/CONTRIBUTOR_REFERENCE.md](docs/CONTRIBUTOR_REFERENCE.md#egress-receipts)。

## 开发符号链接感知

开发 gstack 时，`.claude/skills/gstack` 可能是指回本
工作目录的符号链接（已 gitignore）。这意味着 skill 修改**立即生效**，
利于快速迭代，但在大重构期间有风险，写到一半的 skill
可能弄坏并发使用 gstack 的其他 Claude Code 会话。

**每个会话检查一次：** 运行 `ls -la .claude/skills/gstack` 看它是
符号链接还是真实副本。若是指向你工作目录的符号链接，注意：
- 模板修改 + `bun run gen:skill-docs` 立即影响所有 gstack 调用
- SKILL.md.tmpl 文件的破坏性修改可能弄坏并发的 gstack 会话
- 大重构期间，移除符号链接（`rm .claude/skills/gstack`），改用
  `~/.claude/skills/gstack/` 的全局安装

**Skill 链接与归属（#2119）：** setup 把每个 skill 安装为
顶层目录（短名 `qa` 或带命名空间的 `gstack-qa`，取决于 `skill_prefix`），
`setup` 与 `bin/gstack-relink` 只删除或覆盖它们能
证明属于 gstack 的条目；两处规则副本要保持同步。证明规则、
清理行为与固定测试：
[docs/CONTRIBUTOR_REFERENCE.md](docs/CONTRIBUTOR_REFERENCE.md#skill-linking-and-ownership)。

**注意：** 把 gstack vendor 进项目仓库的做法已废弃。改用全局安装
+ `./setup --team`。团队模式说明见 README.md。

**计划审查：** 审查修改 skill 模板或
gen-skill-docs 流水线的计划时，考虑这些改动是否应先隔离测试
再上线（尤其当用户正在其他窗口积极使用 gstack 时）。

**升级迁移：** 某个修改以可能破坏既有用户安装的方式改动磁盘状态
（目录结构、配置格式、过期文件）时，向 `gstack-upgrade/migrations/` 添加
迁移脚本。格式与测试要求见 CONTRIBUTING.md 的"Upgrade
migrations"一节。升级 skill 在 `/gstack-upgrade` 期间于 `./setup` 之后自动
运行它们。

## 编译产物二进制：绝不提交 browse/dist/、design/dist/ 或 make-pdf/dist/

`browse/dist/`、`design/dist/` 与 `make-pdf/dist/` 目录存放
编译好的 Bun 二进制（`browse`、`find-browse`、`design`，各约 62MB）。它们只有
Mach-O arm64 一种格式：在 Linux、Windows 或 Intel Mac 上都不能运行。
`./setup` 脚本为每个平台从源码构建。

这些目录**未被跟踪且已 gitignore**（`.gitignore:3-6`；
`browse/dist/` 的二进制在 `64d5a3e4`（v0.11.16.0）转为未跟踪；其余从未被
跟踪）。它们不会出现在 `git status` 里。若某个 dist 二进制真的
出现在 `git status`，说明有东西强制添加了它（`git add -f`）：不要提交
它；先取消暂存，再查明它怎么来的。

暂存文件时永远用具体文件名（`git add file1 file2`）：绝不
用 `git add .` 或 `git add -A`，它们会把构建产物和垃圾一并扫进来。

## 脱敏护栏（PII / 机密 / 法律内容）

`lib/redact-patterns.ts` + `lib/redact-engine.ts`（CLI `bin/gstack-redact`，
可选 Hook `bin/gstack-redact-prepush`）在外部发送点之前拦截凭据、PII 与法律内容。它是**护栏，不是滴水不漏的强制手段**；永不
声称它能拦住执意的泄密者。永远扫描将要发送的确切字节，skill 文档从 `scripts/resolvers/redact-doc.ts` 渲染。分级、
可见性、围栏与配置键：
[docs/CONTRIBUTOR_REFERENCE.md](docs/CONTRIBUTOR_REFERENCE.md#redaction-guard)。

## 提交风格

**永远按二分法拆提交。** 每个提交应是单一逻辑变更。你做了多项修改
（例如重命名 + 重写 + 新测试）时，推送前拆成
独立提交。每个提交都应能独立理解、独立回滚。

良好拆分的例子：
- 重命名/移动与行为变更分开
- 测试基础设施（touchfiles、helpers）与测试实现分开
- 模板修改与生成文件的再生成分开
- 机械重构与新功能分开

用户说"bisect commit"或"bisect and push"时，把暂存/未暂存
修改拆成逻辑提交并推送。

## Slop-scan：追求 AI 代码质量，而非掩饰 AI 代码

我们用 [slop-scan](https://github.com/benvinegar/slop-scan) 捕捉
AI 生成代码确实比人写得差的模式。我们不是在试图冒充人写的代码。我们是 AI 写的代码，并为此自豪。目标是代码质量。

```bash
npx slop-scan scan .          # human-readable report
npx slop-scan scan . --json   # machine-readable for diffing
```

配置：仓库根的 `slop-scan.config.json`（当前排除 `**/vendor/**`）。

修复任何发现前，先读 [docs/SLOP_SCAN.md](docs/SLOP_SCAN.md)：
它区分真正的质量修复（文件操作旁的空 catch 改为
`safeUnlink()`，进程终止改为 `safeKill()`）与我们拒绝的钻 linter
空子（靠字符串匹配错误信息、收紧尽力而为的清理）。
工具函数在 `lib/error-handling.ts`。不要追着分数跑。

## 社区 PR 护栏

审查或合并社区 PR 时，接受任何包含以下内容的提交前**必须先 AskUserQuestion**：

1. **触及 ETHOS.md**：这个文件是 Garry 的个人构建者哲学。外部贡献者或 AI agent 一概不得修改，没有例外。
2. **删除或弱化宣传性内容**：YC 引用、创始人视角与产品语气是有意为之。把它们说成"没必要"或"太像广告"的 PR 必须拒绝。
3. **改变 Garry 的语气**：skill 模板、CHANGELOG 与文档中的语气、幽默、直接与视角不是通用模板。把语气改写成更"中性"或"专业"的 PR 必须拒绝。

即使 agent 坚信某改动能改进项目，这三类仍需通过 AskUserQuestion 获得用户明确批准。没有例外。
不许自动合并。不许"我只是顺手清理一下"。

## 检出来自 garrytan-agents 的 PR

Fork PR（例如来自 `garrytan-agents/gstack`）拿不到基础仓库的 secrets，
评估 CI 会因空环境认证而失败。除非用户要求保留 fork PR，把分支推到
`garrytan/gstack` 并从那里重定 PR 目标：
[docs/CONTRIBUTOR_REFERENCE.md](docs/CONTRIBUTOR_REFERENCE.md#checking-out-prs-from-garrytan-agents)。

## CHANGELOG 与 VERSION 风格

**自主选择版本；默认 PATCH。** Garry 把发布版本决策委托给 agent。不要请他选择或批准版本，
包括已批准版本与另一个 PR 冲突时。本政策覆盖 `/ship` 与 `/document-release` 中通用的版本审批提示。

普通发布（包括修复、新增、
重构、测试基础设施与协调的多文件工作）优先 **PATCH (X.Y.Z+1.0)**。仅凭
diff 大小不构成选 MINOR 的理由。只有当把它称为 patch 会明显误导
（"离谱"）时才选 **MINOR (X.Y+1.0.0)** 或 **MAJOR
(X+1.0.0.0)**，例如不兼容的公共接口变更或真正全新
产品级发布。这一判断不需要再发起审批提问。

gstack 政策启用了 `changelog_fragments`（#3654），分支从不写
版本号，也从不检查 `bin/gstack-next-version` 找槽位。合并
列车的盖章（`train land`）在合并时分配基础版本 + PATCH。想要更高，
用 `bump: minor`（或 `major`）front matter 打开该分支的片段。更高的基础版本本身不需要 MINOR bump。保持 PR 处于 READY
供合并列车使用；自主版本决策不授权合并、
部署或跳过必需验证。

**CHANGELOG 条目是分支片段。** 每个发布分支在 `/ship` 时写一条
条目到 `changelog.d/<branch-slug>.md`（只有条目正文，无
`## [x]` 标题），面向用户描述本分支相对 main 新增了什么，
不写分支内部版本号或开发叙事。分支永不编辑
VERSION、package.json 或已发布的 CHANGELOG.md 小节：合并盖章把
片段按其版本折入 CHANGELOG.md，VERSION 保持 4 位，并通过 `bin/gstack-version-bump`
写出 package.json 的 3 位 npm 对应版本（[changelog fragments](docs/ship-policy.md#changelog-fragments)）。写条目前先读
[docs/CHANGELOG_STYLE.md](docs/CHANGELOG_STYLE.md)：它载有版本不变量、合并进 main 的检查、
不该出现的内容与条目格式。社区贡献永远用
`Contributed by @username` 署名。

## AI 效率压缩

估算或讨论工作量时，总是同时给出人类团队与 CC+gstack 两种耗时：

| 任务类型 | 人类团队 | CC+gstack | 压缩比 |
|-----------|-----------|-----------|-------------|
| 样板代码 / 脚手架 | 2 天 | 15 分钟 | ~100x |
| 编写测试 | 1 天 | 15 分钟 | ~50x |
| 功能实现 | 1 周 | 30 分钟 | ~30x |
| Bug 修复 + 回归测试 | 4 小时 | 15 分钟 | ~20x |
| 架构 / 设计 | 2 天 | 4 小时 | ~5x |
| 研究 / 探索 | 1 天 | 3 小时 | ~3x |

覆盖完整，代码最少。不要推荐会留下部分需求未覆盖的捷径，
也不要超出需求加代码：各选项覆盖面相同时，选更小的 diff。只有真正无关的跨季度迁移才算独立范围，绝不是覆盖缺口的借口。完整理念见 skill 前导块中的完整性原则。

## 先搜索再构建

设计任何涉及并发、陌生模式、
基础设施，或运行时/框架可能已有内置实现的方案之前：

1. 搜索 "{runtime} {thing} built-in"
2. 搜索 "{thing} best practice {current year}"
3. 查阅运行时/框架官方文档

知识分三层：久经考验（第 1 层）、新而流行（第 2 层）、
第一性原理（第 3 层）。第 3 层最珍贵。完整构建者哲学见 ETHOS.md。

## 本地计划

贡献者可以把长期愿景文档与设计文档存放在 `~/.gstack-dev/plans/`。
这些只存本地（不入库）。审阅 TODOS.md 时，检查 `plans/` 里的候选项，
看是否可以提升为 TODO 或实现。

## E2E 评估失败归因协议

E2E 评估在 `/ship` 或任何其他工作流中失败时，**未加证明绝不说"与
我们的改动无关"。** 这些系统存在隐形耦合：
前导块文本修改会影响 agent 行为，新 helper 会改变时序，
再生成的 SKILL.md 会移动提示词上下文。

**把失败归为"既有问题"之前必须做到：**
1. 在 main（或基础分支）上运行同一个评估，证明它在那里也失败
2. 在 main 上通过但在分支上失败，那就是你的改动。追查根因。
3. 无法在 main 上运行，就说"未验证：可能相关也可能无关"，并在 PR 正文里
   标记为风险

没有证据的"既有问题"是偷懒的说法。拿出证据，否则别说。

## 以 agent 身份运行评估：总是分离运行（防 SIGTERM）

绝不要把长评估当作普通后台 Bash 任务运行：回合边界的 SIGTERM
会把它中途杀掉。付费评估用 `bun run eval:bg:pr`
（diff 选取的 PR 门禁）或 `bun run eval:bg:release`（完整门禁 + 周期项）在后台运行；
`eval:bg:gate` 与 `eval:bg:periodic` 各跑一个层。四者都运行
`scripts/eval-bg.ts`，它打印 `[eval-bg] backend=<dispatch|local> …` 和
`gstack-detach LOG <path>` 后立即返回。

- **Dispatch 后端**（默认：HEAD 干净、已推送到 garrytan/gstack
  且 `gh` 可分发时）：CI 在已推送的修订上运行该流水线（`evals.yml`
  和/或 `evals-periodic.yml`，由 `expected_sha` 校验）；本地日志跟随
  该次运行并给出其 URL。分发运行是验证运行：全新环境，从不
  写 PR 回执。先提交并推送；有未提交文件或未推送
  提交时回退到本地，日志会说明原因。
- **Local 后端**（树脏、有未推送提交、fork、没有 `gh`，或 `--local`）：
  本机上的分片运行器，上限为 ceil(1.5 × 计划串行秒数
  / EVALS_JOBS) + 20 分钟，最多 4 小时（`--timeout SECS` 可覆盖）。先
  导出 `ANTHROPIC_API_KEY`（绝不把密钥放进 argv）。
- **强制：** `--dispatch` 会带着修复建议拒绝（"commit and push, or rerun with
  --local"）而不是回退；`--local` 或 `GSTACK_EVAL_BG_MODE=local`
  总是就地运行。
- **等待：** 轮询日志直到出现 `### gstack-detach EXIT=<code> ###`
  （0 通过、1 失败、130 取消、2 其他）；没消息不等于成功。持续检查直到
  出现哨兵或用户叫停，并在每次检查时报告进度。
  `bun run scripts/eval-bg.ts status <log-or-run-id>` 打印 running、passed、
  failed、cancelled 或 incomplete（死时无哨兵）。
- 两种后端都持有机器级 `gstack-evals` 锁，并发的
  worktree 排队而不是打满 API；日志在
  `~/.gstack-dev/eval-runs/` 下。同一修订与基础分支的第二个
  `eval:bg:<lane>` 跟随已排队、运行中或已变绿的分发，而不是再次分发。

人类在自己的终端跑评估不需要这些。后端、上限与旋钮：
[docs/TESTING_INTERNALS.md](docs/TESTING_INTERNALS.md#running-evals-as-an-agent-detach)。

## E2E 测试 fixture：提取，不要整份复制

**绝不把整个 SKILL.md 文件复制进 E2E 测试 fixture。** SKILL.md 文件有
1500-2000 行。`claude -p` 读这么大的文件时，上下文膨胀导致
超时、回合上限不稳定，以及测试耗时达到必要的 5-10 倍。

应当只提取测试真正需要的段落：

```typescript
// BAD — agent reads 1900 lines, burns tokens on irrelevant sections
fs.copyFileSync(path.join(ROOT, 'ship', 'SKILL.md'), path.join(dir, 'ship-SKILL.md'));

// GOOD — agent reads ~60 lines, finishes in 38s instead of timing out
const full = fs.readFileSync(path.join(ROOT, 'ship', 'SKILL.md'), 'utf-8');
const start = full.indexOf('## Review Readiness Dashboard');
const end = full.indexOf('\n---\n', start);
fs.writeFileSync(path.join(dir, 'ship-SKILL.md'), full.slice(start, end > start ? end : undefined));
```

另外，运行定向 E2E 测试调试失败时：
- 在**前台**运行（`bun test ...`），不要用 `&` 加 `tee` 放后台
- 绝不 `pkill` 正在运行的评估进程再重启：既丢结果又浪费钱
- 一次干净运行胜过三次杀了再重启

## 向 ClawHub 发布原生 OpenClaw skill

原生 OpenClaw skill 位于 `openclaw/skills/gstack-openclaw-*/SKILL.md`。
命令是 `clawhub publish`（不是 `clawhub skill publish`）：完整
流程、认证与验证见
[docs/OPENCLAW_PUBLISHING.md](docs/OPENCLAW_PUBLISHING.md)。

## 部署到生效的 skill

生效的 skill 位于 `~/.claude/skills/gstack/`。完成修改后：

1. 推送你的分支
2. 在 skill 目录里 fetch 并 reset：`cd ~/.claude/skills/gstack && git fetch origin && git reset --hard origin/main`
3. 重新构建：`cd ~/.claude/skills/gstack && bun run build`

`bun run build` 在从未运行过 setup 的 checkout 里渲染所有主机。在
安装环境（任何含 `.gstack-installed-hosts` 的 checkout，包括用
`bin/dev-setup` 建立的，它记录 Claude 与 Codex）里，它只渲染已记录的
主机并打印出来（#1694）；`GSTACK_RENDER_HOSTS=all bun run build` 在那里渲染
每个主机，下一次 `./setup` 再把多余的渲染清理到
`$GSTACK_STATE_ROOT/backups/host-renders/`。

**如果你使用 gbrain：** 第 2 步的 `git reset --hard` 会还原 `gstack-config
gbrain-refresh` 渲染进安装的脑感知（`GBRAIN_CONTEXT_LOAD` / `GBRAIN_SAVE_RESULTS`）块
（这些生成块与 `main` 不同是设计使然）。部署后重新运行 `gstack-config gbrain-refresh`，
在你所有项目的 Claude 会话中恢复它们。该操作幂等。

或者直接复制二进制：
- `cp browse/dist/browse ~/.claude/skills/gstack/browse/dist/browse`
- `cp design/dist/design ~/.claude/skills/gstack/design/dist/design`
- `cp make-pdf/dist/pdf ~/.claude/skills/gstack/make-pdf/dist/pdf`

## Skill 路由

用户请求匹配某个可用 skill 时，通过 Skill 工具调用它。只路由到
会话 available-skills 列表里的 skill；快速提问或小范围
编辑直接回答。

关键路由规则：
- 产品点子/头脑风暴 → 调用 /office-hours
- 战略/范围 → 调用 /plan-ceo-review
- 架构 → 调用 /autoplan
- 设计体系/计划审查 → 调用 /design-consultation 或 /plan-design-review
- 完整审查流水线 → 调用 /autoplan
- Bug/报错 → 直接修复：对原因做一次只读检查，原因不明时先写聚焦的失败测试；然后修复并运行该测试
- QA/测试站点行为 → 调用 /qa 或 /qa-only
- 代码审查/diff 检查 → 调用 /review
- 视觉打磨 → 调用 /design-review
- 发布/部署/PR → 调用 /ship（合并 + 部署：用户输入 /land-and-deploy）
- 保存进度 → 调用 /context-save
- 恢复上下文 → 调用 /context-restore

## 跨会话决策记忆

持久决策及其理由记录在 `~/.gstack/projects/<slug>/decisions.jsonl` 这个
只追加、事件溯源的存储里，让你和用户都不会跨会话重新争论已定的结论，
也不会丢失"当初为什么"。这是可靠、
纯文件的路径：gbrain 关闭时照样工作。（gbrain 语义召回是叠加在
其上的可选增强，绝不是依赖。）

- **重提**生效决策，在重新决策之前：`bin/gstack-decision-search`
  （`--recent N`、`--scope repo|branch|issue`、`--query KW`、`--all`、`--json`）。
  加 `--semantic`（配合 `--query`）可在 gbrain 可用时追加其记忆中的相关命中；
  gbrain 关闭时静默降级为可靠的文件结果。
  会话开始时 Context Recovery 已经浮现与当前范围相关的生效决策。
  决策在列，就把它连同理由当作已定；准备推翻它时，明确说出来。
- **捕获**持久决策，当你或用户做出一个时：
  `bin/gstack-decision-log '{"decision":"...","rationale":"...","scope":"repo|branch|issue","source":"user|skill|agent","confidence":1-10}'`。
  用 `--supersede <id>` 推翻先前记录；用 `--redact <id>` 清除误录入的机密；
  用 `--compact` 把日志重写为生效集合。非交互
  （从不弹问）、注入已消毒、写入时遇 HIGH 级机密即阻断。
- **持久指：** 架构选择、范围裁剪、工具/供应商选择，或对先前记录的
  推翻。不包括回合级修改、措辞微调或任何轻易
  可再推导的东西。捕获在源头就应精选：只记录持久决策，否则
  存储会变成噪音。

## GBrain Search Guidance（由 /sync-gbrain 配置）
<!-- gstack-gbrain-search-guidance:start -->

GBrain 已在本机完成设置并同步。问题偏语义、或你还不知道确切
标识符时，agent 应优先用 gbrain 而非 Grep。

**本 worktree 经仓库根的
`.gbrain-source` 文件固定到 worktree 级代码源**（kubectl 风格的 context）。在
本 worktree 下任意位置发起的
`gbrain code-def`、`code-refs`、`code-callers`、`code-callees` 或 `query`
调用默认路由到该源：
无需 `--source` 标志。同一仓库的 Conductor 兄弟 worktree
各有自己的 pin 和各自已索引的页面，语义结果
与本 worktree 磁盘上的实际代码一致。

`gbrain` CLI 可用两个已索引语料：
- 本 worktree 的代码（经 `.gbrain-source` 自动固定）。
- `~/.gstack/` 精选记忆：`gstack-artifacts-<user>` 源，以
  仓库 `gstack-artifacts-init` 创建的名字命名（转小写并截断到 32 字符；
  `gbrain sources list` 显示确切 id）。

以下情况优先用 gbrain：
- "X 在哪里处理？"／语义意图，还没有确切字符串：
    `gbrain search "<terms>"` 或 `gbrain query "<question>"`
- "符号 Y 定义在哪里？"／基于符号的代码问题：
    `gbrain code-def <symbol>` 或 `gbrain code-refs <symbol>`
- "谁调用 Y？"／"Y 依赖什么？"：
    `gbrain code-callers <symbol>` / `gbrain code-callees <symbol>`
- "上次我们定了什么？"／过去的计划、复盘、经验：
    `gbrain search "<terms>" --source gstack-artifacts-<user>`

已知确切字符串、正则、多行模式和
文件 glob 仍适合 Grep。有意义的代码修改后运行 `/sync-gbrain`；要在所有
worktree 持续自动同步，每台机器运行一次 `gbrain autopilot --install`：
gbrain 的守护进程按计划做增量刷新。

安全：`gbrain autopilot` 活跃时不要运行 `/sync-gbrain`：
编排器检测到运行中的 autopilot 时会拒绝破坏性源操作，
避免竞态（#1734）。用户仓库优先用 `gbrain sources
add --path <dir>` 注册（不加 `--url`）：URL 管理的源可能自动重新克隆，
对它们的同步代码遍历需要显式 `--allow-reclone` 选择加入。

<!-- gstack-gbrain-search-guidance:end -->
