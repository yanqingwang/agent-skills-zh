> **中文汉化版** · 上游：[tw93/Waza](https://github.com/tw93/Waza) · 原文件：`skills/check/references/mode-ship.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 发布价值评估与发布跟进

当请求是"这个值得发布吗"或 commit / push / publish / tag / issue 关闭跟进时，从 `check` Mode Picker 加载。Ship 扩展审查，不取代审查。

## 发布价值分析

当用户问"深入分析 X 是不是值得发新版本"、"is this worth a new release"、"值不值得发版"或类似问题时激活。

对上一个已发布 tag（tag 是基线，不是本地 VERSION 文件）以来的每个 commit 分类，然后输出：

- **Commit 摘要**：上次发布以来 N 个 feat、N 个 fix、N 个 chore
- **结论**：release / skip（一行）
- **建议的版本升级**：patch（仅修复）、minor（含 feat）、major（破坏性变更）
- **关键风险**：一句话说明本批次最大风险

如果结论是"release"，提议转入 Ship 模式。

## Ship / 发布跟进

当变更就绪后用户要求 commit、打 tag、release、publish、push、回复 issue/PR 或关闭 issue 时激活。

把显式授权的链条（如 review、fix、verify、commit、push、公开跟进）当作一张交付台账。只要还有安全的已授权工作未完成，就不要在其内部阶段之间把控制权交回。包含 push 时，本地 commit 不算完成；本地预期变更尚未提交时，空操作 push 也不算完成。预期范围已经干净时不要创建空 commit；用证据证明干净/最新状态即可。

本模式扩展审查，不跳过审查。在运行闸门之前，先选出授权请求覆盖的每个交付表面，并应用它们步骤的并集：

- **Commit/push：**检查预期 diff、运行其必需检查、同步受版本管理的生成输出，然后执行步骤 4-5。push 后核实远端 SHA 与相关 CI。除非变更或项目规则把它们纳入本任务，否则不要求 tag、release notes、registry 发布或上传资产。
- **发布就绪、打包或发布：**执行步骤 1-3，然后执行已授权的交付步骤。
- **公开回复、issue 关闭或表情回应：**在真实交付渠道上执行对应的步骤 6-7。仅有 commit/push 授权不能授权这些动作。

只执行所选表面的步骤；只要网络或 API 操作失败，步骤 8 就适用：

1. 从公开项目上下文提取发布规则：README、manifest、CI 工作流、release notes、package scripts、changelog，以及当前对话中的显式用户指令。
2. 填写 `references/project-context.md` 的 Release Gate 2.0 矩阵。用 `python3 <skill-base-dir>/scripts/release_gate.py --root <project>` 生成确定性行的初始值（worktree 状态、远端同步、tag 基线、版本字段同步、changelog 提及），并粘贴其状态行作为证据；其余行（生成产物、包/压缩包内容、发布资产、registry/appcast/CI、公开 issue/PR 状态）仍是需要自行举证的判断题。
3. 核实生成或打包输出、版本字段、release notes、包内容与必需产物已同步。生态提供 dry-run 命令时优先使用。起草 release notes 或更新文案时遵循 `/write` 及其 release-note 模式；中文文案要在第一稿之前加载它的中文 release-notes 规则，而不是被抱怨语气之后再补：翻译腔的中文 release notes 是缺陷，不是打磨项。
   起草 release notes 之前，先读仓库上一次已发布版本（对最新 tag 执行 `gh release view`），保留其标题惯例、单条长度与语言布局。其条目数量是历史，不是目标：使用候选产物中"不同用户可感知结果"的最小完整集合。
   生成的交付物包括受版本管理的压缩包、被 ignore 的 dist 文件、appcast、站点/下载文案、registry 包、校验和与发布资产。如果项目文档要求它们，即使被 git ignore 也要重新生成、检查并显式暂存或上传；不要从仅测源码的检查推断就绪。对远端资产，优先下载或回读已发布产物并比较条目、校验和或 manifest 内容；release 页面文本、文件大小或 workflow 成功本身不是产物证据。
   如果项目有 preview、beta、nightly、stable 或 App Store 通道，明确说出通道名。不要用 preview 或 beta 产物宣称 stable 发布就绪；当请求的通道只是 preview 时，不要触碰 stable 的 appcast、registry 或下载表面，除非项目文档要求。
   在断言什么已上线之前，先按部署表面给每个变更分类：打进打包产物（应用二进制、捆绑 CLI、发布压缩包）的代码要到下一次发布才到达用户；而站点、serverless 函数、CDN 配置与基础设施在默认分支更新时会自动部署。同一批变更可能在第一个表面尚未发布，却在第二个表面已经上线；逐个表面分别陈述，不要让"还没发布"盖住自动部署的代码。
4. 在 `SKILL.md` 的 Worktree Safety Preflight 约束下只 commit 预期文件，并串行化 git 操作，避免 index 锁或重叠的 add 破坏流程。在脏的或多 Agent 共用的 checkout 中，staging 前记录 `git rev-parse HEAD`，commit 前一刻与 push 前一刻再各读一次 `git status --short --branch -uall` 和 `git rev-parse HEAD`。如果 HEAD 移动、出现未知 commit，或 worktree 在预期文件之外发生变化，停下并报告不一致，不要 rebase、重新提交或 push。处于风险层级（`project-context.md`，Risk tiers by path）的 commit 要在提交说明中写明如何验证以及如何回滚。
5. 只有用户显式批准时才 push、publish、打 tag 或创建 release。项目中第一次 push 之前，检查 `git remote -v`、当前分支与已认证身份；用户指定了确切账户时，在第一次远端写入之前立即核实已认证的服务身份，不匹配即停；绝不悄悄换用其他账户。auth、OTP、CI、registry 或网络状态阻塞操作时，暂停并报告确切的阻塞原因。
6. issue/PR 跟进时，发帖之前用宿主的读取命令确认条目身份。GitHub 上用 `gh issue view` 或 `gh pr view`；其他宿主用项目文档或当前请求指定的 CLI/API。发帖、编辑、回读与关闭标准使用 `references/public-reply.md`；回复正文遵循 `/write` Public Reply Mode。
7. GitHub release 表情回应跟进：只在项目上下文或当前对话要求时执行。release 存在且必需资产核实之后，从 tag 解析 release id，用 `gh api` 或可用的 GitHub 工具把每个正面 release 表情 POST 到 `repos/<owner>/<repo>/releases/<id>/reactions`，然后重读表情确认。正面 release 表情是 `+1`、`laugh`、`heart`、`hooray`、`rocket` 和 `eyes`。
8. 网络或 API 失败之后，重读最终状态，不要假设成功或失败。对至多一次的操作（publish、打 tag、创建 release、支付），验证超时意味着未知而不是失败：registry 可能用一道扫描挡住刚上传成功的内容，几十分钟后才可见。在项目重试策略内做有界的只读检查；如果可见性仍未知，报告确切的未决状态并停止。绝不要为了让检查通过而重跑 publish。

交接之前，把每个已授权项对账为 `done`、`not applicable` 或 `blocked`，然后重读本地 `HEAD`、目标远端 ref/SHA、worktree 状态、CI 或已发布产物通道，以及本次运行中变更过的任何公开线程。绝不要把源码、CI、包、已部署渠道与公开线程的状态合并成一句"done"。

### 重做或取消的发布闸门

当发布候选被取消、preview 或 beta 出现反复的修复翻工，或用户询问一再推迟的发布是否终于安全时，激活本闸门。加载 `references/release-surfaces.md`（Reworked Or Cancelled Release Gate）：从上一个公开 stable tag 到 `HEAD`，按已发布的风险表面审查，输出两个决定：preview 是否继续接受用户测试，stable 发布准备是否可以开始。

结论以明确的 go / no-go 开头（可发布，或列出的阻塞项），然后是具体的已发布状态：commit hash、tag、release URL、registry/版本结果、已 push 的分支、发布资产状态、release 表情状态、issue/PR 状态，以及剩余阻塞项。不适用的字段省略。
