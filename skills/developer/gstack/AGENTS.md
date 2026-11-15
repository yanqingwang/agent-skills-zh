> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/AGENTS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# gstack：AI 工程工作流

gstack 是一组 SKILL.md 文件，为 AI Agent 提供结构化的软件开发角色。
每个 Skill 都是一个专员：CEO 审查者、工程经理、设计师、QA 负责人、发布工程师、调试员，等等。

## 可用 Skill

Skill 位于 `.agents/skills/`（Claude Code 上是 `~/.claude/skills/gstack/`）。
按名称调用（如 `/office-hours`）。本索引只列名称；每个 Skill 做什么、带示例的说明在
[docs/skills.md](docs/skills.md)。iOS 配套 CLI（`gstack-ios-qa-daemon`、`gstack-ios-qa-mint`、`gstack-ios-qa-regen`）
在 [docs/howto-ios-testing-with-gstack.md](docs/howto-ios-testing-with-gstack.md)。

| Skill | 领域 |
|-------|------|
| `/office-hours` | 计划 |
| `/plan-ceo-review` | 计划 |
| `/plan-design-review` | 计划 |
| `/plan-devex-review` | 计划 |
| `/plan-tune` | 计划 |
| `/autoplan` | 计划 |
| `/design-consultation` | 计划 |
| `/spec` | 计划 |
| `/review` | 构建 + 审查 |
| `/deslop-shared-libs` | 构建 + 审查 |
| `/write-skill` | 构建 + 审查 |
| `/test-audit` | 构建 + 审查 |
| `/codex` | 构建 + 审查 |
| `/claude-code` | 构建 + 审查 |
| `/verify` | 构建 + 审查 |
| `/design-review` | 构建 + 审查 |
| `/design-shotgun` | 构建 + 审查 |
| `/design-html` | 构建 + 审查 |
| `/design-motion` | 构建 + 审查 |
| `/devex-review` | 构建 + 审查 |
| `/qa` | 构建 + 审查 |
| `/qa-only` | 构建 + 审查 |
| `/scrape` | 构建 + 审查 |
| `/skillify` | 构建 + 审查 |
| `/ship` | 发布 + 部署 |
| `/land-and-deploy` | 发布 + 部署 |
| `/modernize` | 发布 + 部署 |
| `/canary` | 发布 + 部署 |
| `/landing-report` | 发布 + 部署 |
| `/document-release` | 发布 + 部署 |
| `/document-generate` | 发布 + 部署 |
| `/setup-deploy` | 发布 + 部署 |
| `/gstack-upgrade` | 发布 + 部署 |
| `/context-save` | 运维 + 记忆 |
| `/context-restore` | 运维 + 记忆 |
| `/learn` | 运维 + 记忆 |
| `/retro` | 运维 + 记忆 |
| `/health` | 运维 + 记忆 |
| `/captain` | 运维 + 记忆 |
| `/benchmark` | 运维 + 记忆 |
| `/ubicloud` | 运维 + 记忆 |
| `/runaway-stopper` | 运维 + 记忆 |
| `/benchmark-models` | 运维 + 记忆 |
| `/eval-plan` | 运维 + 记忆 |
| `/cso` | 运维 + 记忆 |
| `/setup-gbrain` | 运维 + 记忆 |
| `/sync-gbrain` | 运维 + 记忆 |
| `/browse` | 浏览器 |
| `/open-gstack-browser` | 浏览器 |
| `/setup-browser-cookies` | 浏览器 |
| `/pair-agent` | 浏览器 |
| `/ios-qa` | iOS QA |
| `/ios-fix` | iOS QA |
| `/ios-design-review` | iOS QA |
| `/ios-clean` | iOS QA |
| `/ios-sync` | iOS QA |
| `/careful` | 安全 + 范围 |
| `/freeze` | 安全 + 范围 |
| `/guard` | 安全 + 范围 |
| `/unfreeze` | 安全 + 范围 |
| `/make-pdf` | 安全 + 范围 |
| `/diagram` | 安全 + 范围 |

## 验证纪律

修复失败或准备 `/ship` 时，按此顺序执行：

1. 列出已知的失败用例、它们的日志与源码修订、已证实的成因，以及能证明每个修复的最小检查。
   在 `.context/` 里维护一份当前清单；更新它，而不是另起互相重叠的修复计划。
   把 runner 的失败总数与具名失败、未处理或模块加载错误对账；仅凭具名测试的页脚不是完整清单。
2. 编辑之前先解决基分支集成，并为每个共享文件指定唯一负责人。修复保持在已观察到的失败和用户范围之内。
   fixture 通过链接写入之前，先解析其目标，并确认它停留在该 fixture 的临时根之内；活跃的 skill 注册可能指回本 checkout。
   当上游替换某个辅助 API 时，先清点每一个直接调用方、mock 适配器、源码快照、生成的 golden 和选择边界，再挑选聚焦检查。
   核实抽取出的测试适配器提供了当前的 import 与结果 schema；适配器失败不是生产失败的证据。
   独立的检查独立排期。一道检查只依赖它真正需要的输入或前置条件；一个无关失败不得把整个验证计划串行化。
   测试以活链接引用其文件时，保持源码固定不动。
3. 改代码之前先诊断。区分产品缺陷、无效的测试期望、检测器/fixture 缺陷、启动/环境失败。
   保留原始失败。没有证据不要说它是"本来就存在"。
   在把省略字段判定为模型不合规之前，先核实已固定的运行时工具 schema 和默认值。
   核实有界评测的 fixture 范围与自动回答是否支撑其指标。不要让驱动程序批准无关的扩展，然后把这份额外工作怪到 skill 头上；
   保留必需的发现与证据上限。
4. 用最小相关的测试复现。对 Agent 测试，在为另一次 Agent 运行付费之前，先在免费回归中复用已捕获的公开事件，包括阴性对照。
   检查行为与确认；只有当那段文字本身就是契约时才逐字匹配它。不要降低阈值、增加模型预算、跳过用例或改判失败来制造通过。
   预注册的固定面板不属于改判。
   对任何度量到的提速、回归或 eval 差值，指名移动的瓶颈与运行间波动；小于该波动的差距不算差异。
   对策略或验证类修复，用有代表性的原生输入实际调用注册的回调，并断言它使用了辅助函数的结果。
   当渲染器或解析器在同一边界反复失败时，对照固定的运行时核实受支持的输入类。保留对抗性对照；
   不要为每次付费失败新增一个拼写或字形。
   对工作流清晰度失败，通读被评测的完整摘录及其引用的源码。把所有已证实的歧义一起解决：顺序、
   定义、归属与审批。把密集的指令合并为可执行步骤，而不是追加更多从句。把 resulting workflow 作为整体复查；
   仅凭散文快照不能证明它清晰。
   对每道闸门，识别其输入何时存在，并追踪正常、跳过/不可用与晚期变更路径，以发现循环前置条件或被绕过的检查。
5. 付费工作之前，先运行必需的廉价 CI 检查，包括凭证扫描。
   同时运行相邻的廉价检查：生成内容新鲜度、提示词大小/parity 限制、源码断言、fixture 检查，以及适用的依赖选择。
   改过的提示词必须先通过这些，再进 eval。
   对 skill 编辑，包含 `bun test test/parity-suite.test.ts`：它历史上的 union 大小上限与其他提示词大小及上下文预算是分开的。
   当工作流措辞变化时，在整个测试树里搜索被删除的从句，包括始终加载的提示词守卫。包含 subprocess 示例的测试
   fixture 必须通过 `test/spawnsync-timeout-tripwire.test.ts`；它的扫描器也检查引号内代码。
   在读取同一改后提示词的长行为评测之前，先运行其选定的质量评判。如果一个修复覆盖了某个活跃运行的输入，
   取消那个运行，保留已完成的结果，并把未完成用例标为 cancelled。
   在运行依赖检查之前，先核对每个编辑或 setup 命令的结果。一次失败的编辑不是再次测试未变输入的理由。
6. 在模型启动之前，声明 fixture 参与者支持的交互。把它的回答与权限处理保持在所声明的接口之内。
   把产物归属绑定到传给子级的同一份隔离状态；环境中的路径不确立归属。对照每个用例与配置的重试次数
   检查整文件与 CI 监督，而不是只看一次尝试。预检真正的启动器：所需二进制、隔离状态、需要时的显示器、
   明确的测试层级、选择与预期的执行用例数。与工作流及其容器镜像固定的运行时版本保持一致。
   在 runner 加入其嵌套目录之后，保持含 socket 的临时路径简短；在 smoke 检查中演练完全相同的布局。
   把长生命周期日志与 socket 目录分开存放。
   用一次零成本的 smoke 检查在该启动环境下验证所需工具确实能执行；仅有版本与认证不能证明它能用。
   显式设置私有产物模式并保留正常的 fixture 权限。付费工作之前，先证明诊断快照能在 fixture 清理后
   存活于最终产物目录；原生快照需要 EVALS_RUN_ID 或 GSTACK_EVAL_DIR。
   绑定完整的 spool 文件名，并把 Bun 的 tier 外 describe.skip 占位符单独归类，选择的用例记零分。
   把独立的 Git fixture 放在另一个 checkout 之外；解读失败之前，先核实其解析出的项目 slug 与状态根。
   在那里证明一个种子 commit 能成功：仓库本地的作者配置并不确立一个全新 fixture 仓库可用的身份。
   在调用 Bun 之前，拒绝缺失的显式测试文件；Bun 可能静默忽略不存在的文件选择器并通过其余文件。
   通过日志保留退出状态。使用文档记载的 detached runner 与 eval 锁。编辑之后复查最终的启动器；
   准备与 `--list` 模式不得启动监视器、驻留进程或测试进程。用前后进程对比核实这一点。长时间运行期间，
   检查最后的公开工具结果与待处理的权限状态；在等完被阻塞参与者的截止时间之前先诊断它。把取消与测试判定分开保留。
   跳过或未开始的用例
   不满足覆盖；保留每一次尝试。付费 eval 永不重试，只有一个例外：闸门可在同一 head 上把一条红色 rule、
   behavior 或 judge 用例的判定重跑一次（Garry，2026-10-19："可以直接把失败的测试再跑一次，并注明它是 flaky"）；
   通过记为绿色并加 flaky 标注与 flake 记录，第二次失败是真实的红色，而 harness、INFRA、INCOMPLETE
   或无法归因的红色永不重跑（`docs/TESTING_INTERNALS.md#flaky-reruns`）。每个用例的 kind（`E2E_KINDS`）在运行前
   固定其试验次数：`rule` 一次试验；`behavior` 3 次独立试验的面板，>= 2 次通过且无契约违例记 PASS；
   `judge` 对同一输出取 3 个样本，每个维度按其中位数（3 个样本中至少 2 个）对照不变的阈值把关。
   看到结果之后绝不追加试验、样本或派发；没有通过率证据绝不改 kind 来改判定；并报告每一次试验。
   隔离只遵循 `CASE_QUARANTINE` 的进入与退出规则（`EVAL_POLICY`、`docs/TESTING_INTERNALS.md`）。一次普查若每条红色
   都被机器归类为 INFRA 或 INCOMPLETE，可作为新运行再派发一次；报告两次运行。
7. 用聚焦测试证明所有已知修复，包括受影响的付费用例。只有在具体修复之后或启动问题被证实纠正之后，才重跑失败用例。
   在集成后的代码上运行其余必需的选定评测。不要用完整的免费套件去发现可预见的相邻失败。
   当一次通过检查所消费的输入与相关环境都没变时，复用它。对模型评判，比较展开后的提示词、rubric、
   参数与依赖；仅 commit 不同不使结果失效。
   不要为了简化启动器配置而对未变化的通过评判重新采样。
   保留其原始来源，并把结果标注为复用的证据。
   证明模型输入一致时，使用真正的提示词构建器并比较完整字节；在摘录中保留字面文本，并记录所消费的输入。
8. 在最终验收之前完成审查修复、生成、发布元数据与构建。冻结代码，然后在最后运行一次 `bun run test`。
   修复期间，每次提交前用聚焦检查替代全量套件。如果最终验收意外失败，保留失败、窄范围诊断，
   并在再跑全量之前报告变更后的验证计划；绝不盲目重试，也不拿旧修订声称通过。
9. 只在必需检查全部通过时发布，除非用户对已识别的失败明确给出例外。报告修订、实际的通过/失败/跳过计数，
   以及未完成的覆盖。通过的子集不是发布验收。

## 构建命令

```bash
bun install              # install dependencies
bun run typecheck        # strict tsc over product code; must report zero errors
bun run typecheck:test   # test-code type-debt ratchet (new diagnostics fail; --write-baseline locks in fixes)
bun run format:cso       # format lib/cso/*.ts (format:cso:check is the CI gate)
bun run test:quick       # fast measured free subset for edit feedback (not acceptance)
bun run test             # complete free suite via the strict shard runner (no API spend)
bun run eval:bg:pr       # changed live probes + selected judges; dispatches CI when HEAD is clean and pushed, else runs locally
bun run eval:bg:release  # fresh complete gate + periodic live coverage (same backend choice)
bun run test:health      # audit success metrics and weekly health from CI history (free; needs gh)
bun run build            # generate docs + compile binaries
bun run gen:skill-docs   # regenerate SKILL.md files from templates
bun run skill:check      # health dashboard for all skills
```

其余所有测试与 eval 命令（Ubicloud、Windows 子集、单个付费层或用例、CI 中的分支验证、通过率、计划预览）
及其成本与前置条件，在 [我该运行哪个命令？](CONTRIBUTING.md#which-command-do-i-run)。Agent 轮询 `eval:bg:*` 日志等待
`### gstack-detach EXIT=<code> ###` 哨兵
（[CLAUDE.md](CLAUDE.md#running-evals-as-an-agent-always-detach-sigterm-proof)）。

## 平台支持

支持层级（full：macOS、Linux；minimal：Windows、Gemini 模型）见
[docs/support-tiers.md](docs/support-tiers.md)。

- **macOS** + **Linux**：支持完整测试套件。
- **Windows**：最小支持；[docs/support-tiers.md](docs/support-tiers.md)
  写明了承诺的范围。每个 PR 必须通过 `windows-smoke` 检查（`./setup`、
  核心 skill 能启动、最快的 Windows 安全测试）；精选的 Windows 安全子集每晚在 main 的
  `windows-free-tests` 运行，永不阻塞 PR。安装脚本（`./setup`）目前需要 Git Bash 或
  MSYS；原生 PowerShell 支持是未来的扩展。`bin/gstack-paths`
  辅助脚本通过 `CLAUDE_PLUGIN_DATA` / `GSTACK_HOME` 解析状态根，插件安装因此在所有平台可用。
- **CSO 原生辅助**：`/cso` 另外需要 Bun 的四个
  `--no-compile-autoload-*` 标志和一套原生工具链（Linux 上可静态链接的 C、
  macOS 上的 Xcode 命令行工具，或 Windows 上的 VS 2022 C++ 生成工具）。安装脚本会装好其余一切；
  缺少该可选工具链时，`/cso` 被显式标记为不可用。
- **浏览器与渲染器**：浏览器类 skill、`/make-pdf` 和 `/diagram` 优先驱动 Aside 浏览器，
  它只支持 macOS 15+。在 Linux 与 Windows（或 Aside 已关闭的 Mac）上，就绪检查会说明一次这一点，
  然后这些 skill 改用 gstack 自带的浏览器，由 `./setup` 构建。

## 关键约定

- SKILL.md 文件由 `.tmpl` 模板**生成**。编辑模板，不要编辑生成产物。
- 运行 `bun run gen:skill-docs --host codex` 重新生成 Codex 专属输出。
- Skill 中的浏览器步骤是 `aside repl` 脚本，规则见 `scripts/resolvers/aside.ts`（Aside 优先），
  每个步骤都带备用引擎的 `$B` 等价物：`$B <command>` 即 browse 二进制，
  当 Aside 探测没有打印 `READY` 时是合法工具。本地 HTML 经 `bin/gstack-render.ts` 渲染，它用同样的方式选择。
- 安全类 skill（careful、freeze、guard）使用内联的建议性文字：破坏性操作之前必须先确认。
- 状态路径通过一条链解析，归属 `lib/state-root.ts` 及其可 source 的 bash 孪生 `bin/gstack-state-root.sh`
  （`GSTACK_STATE_ROOT` → `GSTACK_HOME` → `GSTACK_STATE_DIR` → gstack 的 `CLAUDE_PLUGIN_DATA` → `~/.gstack`；见 docs/state-root.md）。
  Skill 文字使用 `GSTACK_STATE_ROOT=$(bin/gstack-paths --get GSTACK_STATE_ROOT)` 及其 `${GSTACK_STATE_ROOT:?…}` 守卫
  （worktree 隔离的 Claude Code 会话会拒绝 eval）；`test/state-root-ratchet.test.ts` 拒绝手搓的链。
- Browse 守护进程的 HTTP 路由是 `browse/src/routes/table.ts` 里的条目（其文件头展示了如何添加）；
  绝不在 `server.ts` 里对 `url.pathname` 分派。
- 两条测试通道都经 `scripts/lib/shard-engine.ts` 运行分片；免费与付费 runner 只持有通道策略。
  PTY Harness 代码位于 `test/helpers/pty/*`，经由 `claude-pty-runner.ts` barrel 导出。
- 外部意见失败的文案（auth、timeout、empty、fallback）只来自
  `scripts/resolvers/outside-voice.ts` 的 `outsideVoiceFailurePolicy()`。
- 每个环境变量宿主的围栏都以 `scripts/resolvers/runtime-root.ts` 的共享前奏开头（由其后渲染步骤插入）；
  绝不在模板里手工解析 gstack 的根目录。
- 每次 Codex 运行的判定都经过 `lib/outside-review-result.ts`；其原因码在 `lib/gate-outcomes.ts`，
  每个都有 `docs/troubleshooting.md` 锚点。
- `test/module-size-ratchet.test.ts` 把重构后的 owner 模块保持在 800 行以内（每个函数 150 行），
  并防止残余文件继续增长。
- `claude` CLI 二进制经 `lib/claude-bin.ts` 解析（browse 内部从 `browse/src/claude-bin.ts` 再导出；
  `Bun.which()` + `GSTACK_CLAUDE_BIN` 覆盖）。设置 `GSTACK_CLAUDE_BIN=wsl` 加
  `GSTACK_CLAUDE_BIN_ARGS='["claude"]'` 可在 Windows 上经 WSL 运行 Claude。
- 每个 gstack 启动的 Bun 都忽略工作目录的 `.env` 文件与 `bunfig.toml`：bun shebang 写作
  `#!/usr/bin/env -S bun --no-env-file --config=/dev/null`，skill 文字传入 `bun --no-env-file --config=/dev/null`，
  随附的 shell 文件定义 `GSTACK_BUN_CONFIG`，该行由 `test/bun-entry-isolation.test.ts` 强制
  （`OSTYPE` 为 `msys` 或 `cygwin` 且 `cygpath` 在 `PATH` 上时用 `NUL`，因为原生 Bun 打不开 `/dev/null`，#3415），
  并传入 `bun --no-env-file --config="${GSTACK_BUN_CONFIG:-/dev/null}"`，TypeScript 派生使用
  `lib/bun-isolation.ts` 的 `bunIsolationArgs()`，`bun build --compile` 加
  `--no-compile-autoload-dotenv --no-compile-autoload-bunfig`。`test/bun-entry-isolation.test.ts` 强制全部四条。
