> **中文汉化版** · 上游：[tw93/Waza](https://github.com/tw93/Waza) · 原文件：`skills/health/references/maintainability-findings.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# AI 可维护性结构化发现

从 `health` 输出（报告步骤）加载，用于 AI 可维护性通道。summary 模式读取 `AI MAINTAINABILITY SUMMARY`；deep 审计与显式的代码腐化请求读取 `DETAIL`。Agent 配置通道（指令漂移）留在 `SKILL.md`。下文的 `$HEALTH_SCRIPT` 与 `$HEALTH_LAUNCHER` 变量是 Step 1 已解析好的那两个。

**AI 可维护性缺口。** summary 模式用 `AI MAINTAINABILITY SUMMARY`，deep 模式用 `AI MAINTAINABILITY DETAIL`。当实现、CI、生成、发布、部署或其他重大风险本应有实质性可执行验证但 `verifier_evidence` 为空，或必需的文档引用断裂时，报告 `FAIL`。`commands` 只是发现清单，不是证明：列在 `hollow_verifiers` 下的目标或脚本只会打印、做 shell 准备或退出，不构成覆盖。以下情况报告 `WARN`：已确认的生成镜像漂移；引用了不存在的命令；相关任务触达不到的稳定非显而易见约束；反复失败却没有持久不变量与验证器；错过真实失败层级的空心包装；只存在于被 ignore 的/私有覆盖层中的持久规则；或持久文档保存的是原始一次性报告、记分卡、带日期的行号引用或诊断转储，而不是稳定不变量。另外，当运行时支持按路径加载，但无关会话反复为可以安全路由的大段领域特定指引付出上下文成本时，也要警告；把它移到按路径限定的规则、嵌套指令文件或 Skill 中，不删除其行为价值。`context_status: UNKNOWN` 表示存在实现或 CI 风险但没有受版本管理的上下文证据；先检查实际风险，再决定是否需要路由的不变量。`NOT_APPLICABLE` 表示采集器未观察到实现/CI 上下文需求。两种状态都不能成为伪造"一切正常"结论或要求画导图的理由。对过时报告的处理动作是：把稳定规则提炼进公开的 instructions、rules、references 或验证器脚本，然后移除或归档这份临时报告。

**对话衍生的指引。** 健康审计读取最近的 Agent 对话时，不要建议把对话或记分卡照抄进文档。建议改做一遍候选矩阵筛选：

| 字段 | 问题 |
|---|---|
| 独立复发 | 克隆的提示词、重试、自动化扇出的会话、粘贴的助手输出、平台续传消息，是否已被归并为同一个底层事件？ |
| 重复失败 | 该问题是否跨修复、发布、Agent 或用户报告反复出现？ |
| 持久不变量 | 经验能否表述为一条稳定规则，而不是带日期的事故摘要？ |
| 目标层级 | 它应放在项目指令、Waza Skill、全局规则还是私有记忆里？ |
| 验证器 | 是否存在能强制执行它的确定性命令、脚本、产物检查或运行时冒烟测试？ |
| 脱敏风险 | 这条经验是否需要包含本地路径、issue 编号、客户细节、机器状态、机密或未公开的发布事实？ |

分层规则：项目特有的命令、应用名、产物名与发布仪式留在项目里；可复用工作流（如取消发布审查闸门、原生冻结证据阶梯）属于 Waza Skill；通用的诚实与验证规则属于全局 CLAUDE/AGENTS；私有用户偏好与单机事实留在记忆中。如果经验过不了脱敏风险这一栏，就不要进入公开指引。

按加载表面划分范围，而不只是按层级。留在项目里的规则每个会话仍在支付上下文成本，除非它绑定到生效之处：语言与框架规则带文件类型的 `paths` 范围；项目领域规则绑定到其源码目录（`paths` frontmatter 或嵌套目录的 `CLAUDE.md`）；只有真正横切的约束才无条件地在常驻加载的根文件中加载。只在某一路径下才重要的规则，不该放进常驻加载的文件。

**集中的修复链。** 运行 `git -c core.fsmonitor=false log --oneline --since='2 weeks ago' | grep -i fix`，按领域分组（`:` 或 `(` 之前的前缀）。重复只是线索，不是发现：要读够证据，确认多个修复收敛于同一个不变量或失败层级，而不是共享前缀的无关工作。经过这一验证之后才报告 Structural `WARN`，指出重复出现的失败，并推荐最窄的路由规则加上可执行验证器（本来可以防止它）。

当这些修复针对的是已到达用户或已发布构建的缺陷，而项目没有事故台账（incident ledger），或台账从不被其检查校验时，加一条 Incremental 备注：为每个此类缺陷建议一行台账记录，写明漏掉它的层级与现在能抓住它的测试，具体见 `check` 的事故台账参考。窗口期内没有面向用户的修复的项目不加备注；仅缺台账本身不构成发现。

**非显而易见约束的可达性与有风险依据的热点归属。** 文件大小与模块形态本身不产生文档要求。当真实失败或高后果路径集中在某个区域，并暴露出无法从代码廉价还原的稳定边界时，核实相关任务能否触达一条简洁的归属规则以及锁定它的可执行检查。报告触达不到的约束或缺失的验证器，而不是要求一份笼统的"热点导图"。

**缺失稳定的验证器入口。** 把 `wrapper_findings` 当作发现线索。在 package scripts、原生构建工具、任务运行器、脚本与 CI 中检查文档默认入口及其可执行覆盖；不要求 Makefile。只有当碎片化检查导致必需验证被漏掉、且没有可用默认入口覆盖它时，才报告 Structural `WARN`。只打印成功的命名 target 不提供验证。

在项目根目录快速检查，复用 Step 1 已解析的 `$HEALTH_SCRIPT`。单独运行时，它打印同样的小节但没有 `AI MAINTAINABILITY SUMMARY` 包装，因此首行是 `=== PROJECT SHAPE ===`：

```powershell
& "$POWERSHELL" -NoLogo -NoProfile -ExecutionPolicy Bypass -File "$HEALTH_LAUNCHER" maintainability . summary
```

在 Linux 与 macOS 上：

```bash
BASH_ENV= ENV= /bin/bash -p "${HEALTH_SCRIPT%/*}/check-maintainability.sh" . summary
```

deep 审计：运行同样的命令，把 `summary` 换成 `deep`。

动作要具体且非侵入：添加或修复最小有用的路由指令表面；在真实失败层级添加一条可执行验证命令；修复生成镜像检查；或修复断裂的引用。只在边界已经清晰时才拆分。不要仅凭脚本输出就提出大范围重写。

**断裂的文档引用。** 运行下面的检查器；它会解析 `@...`、`docs/...`、`~` 与 Skill 相对的 `references/...`，每个 MISSING 都是一条发现，附带来源文件与行号。

在项目根目录快速检查，复用 Step 1 已解析的 `$HEALTH_SCRIPT`：

```powershell
& "$POWERSHELL" -NoLogo -NoProfile -ExecutionPolicy Bypass -File "$HEALTH_LAUNCHER" doc-refs .
```

在 Linux 与 macOS 上：

```bash
BASH_ENV= ENV= /bin/bash -p "${HEALTH_SCRIPT%/*}/check-doc-refs.sh" .
```

缺失引用按 Structural 发现报告，而不是 Critical，除非缺失文件被点名为硬依赖（例如项目发布 Skill 的 `release.md`）。

**断裂的 Markdown 引用。** deep 模式下，`check-maintainability.sh` 还会扫描仓库内的 Markdown 链接。当链接指向缺失的本地文件时按 Structural 发现报告，尤其是设计、安全、发布或交接文档这类 Agent 未来工作可能跟随的文档。

**过期的验证器缓存输出。** 如果验证输出指向已删除的临时 worktree 或不存在的 `/tmp` / `/private/tmp` 文件，用以下方式解析捕获的日志：

```powershell
& "$POWERSHELL" -NoLogo -NoProfile -ExecutionPolicy Bypass -File "$HEALTH_LAUNCHER" verifier-output . <log-file>
```

在 Linux 与 macOS 上：

```bash
BASH_ENV= ENV= /bin/bash -p "${HEALTH_SCRIPT%/*}/check-verifier-output.sh" . <log-file>
```

只把本脚本用于用户提供的或当前审计期间生成的既有命令输出。不要为了喂这个检查器而去运行项目测试。已知动作包括 `golangci-lint cache clean`、`go clean -cache -testcache` 和 `npm cache verify`；未知工具给出"诊断性重跑"动作。
