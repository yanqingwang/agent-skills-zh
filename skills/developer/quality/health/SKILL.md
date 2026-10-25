---
name: health
description: "审计 Agent 配置、指令漂移、hooks 或 MCP 以及 AI 可维护性。当 Claude、Codex 或 Pi 的设置看起来不对时使用。不适用于应用 bug 或 PR 审查。"
when_to_use: "检查claude, 检查codex, 检查pi, Codex 配置, Pi 配置, agent instructions, 健康度, 配置检查, 配置对不对, AI coding 腐化, Claude ignoring instructions, Pi coding agent, check config, settings not working, audit config"
dispatch_intent: "Codex/Claude/Pi ignoring instructions, agent config audit, hooks/MCP broken, health token usage, AI coding code rot, risk-backed hotspot ownership, unreachable project constraints, unclear context, missing verification, stale verifier output"
---

> **中文汉化版** · 上游：[tw93/Waza](https://github.com/tw93/Waza) · 原文件：`skills/health/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Health：Agent 辅助工程健康度

在第一行开头内联加上 🥷，不要单独成段。

按照以下框架审计当前项目的 Agent 设置与 AI 编码可维护性：
`agent config → instruction surfaces → tools/runtime → verifiers → maintainability`

找出违规项。定位错位的层。以证据和风险为准校准，而不是以仓库规模为准。

## 成果契约

- 成果：一份兼顾预算的健康报告，把 Agent 配置风险与 AI 可维护性风险区分开。
- 完成标准：每条发现都指明错位的层、具体证据，以及可直接复制粘贴的处理动作或诊断命令。
- 证据：健康脚本采集的输出、纳入版本管理的项目指令、运行时配置摘要、验证器日志、hooks/MCP 暴露面，以及必要时进行的只读实时探测。
- 输出：按优先级排列、带状态/影响/下一步动作的发现清单，或一份明确的无问题结论及残余风险说明。

两条检查线共用一份报告：

- **Agent 配置健康度**：Codex/Claude/Pi 指令漂移、权限、hooks、MCP、Skill 与记忆供应链。
- **AI 可维护性健康度**：非显而易见约束的可达性、有风险依据的热点归属、验证器覆盖、生成产物检查，以及过期或误导性的持久文档。

**输出语言：** 遵循用户当前的语言或明确的语言要求。仅当请求未指定语言时，才使用适用的项目级与全局默认设置。

**预算姿态：** 从摘要级审计开始。当用户要求 deep、full、complete、thorough（深入、完整、彻底）或"继续跑完"的审计，或明确提到 AI coding 代码腐化、Codex/Claude 配置漂移、上下文不清晰、缺少验证、验证器输出指向过期路径，或"代码变烂"时，自动升级为深度审计；当当前项目指令或已记住的用户偏好表明默认运行深度健康检查时也升级；或当摘要轮暴露出无法在本地解决的关键歧义时升级。清单计数本身绝不触发升级。否则不要读取采样的对话摘录，也不要启动 inspector 子代理。升级前先告知用户，因为深度健康审计可能消耗大量 token 配额。

**对话范围：** 当请求只点名静态材料（`AGENTS.md`、Skill、规则、settings、"只审查指令和配置"）时，将 `instructions` 作为第一个参数传给 `collect-data.sh`，此次运行会跳过会话历史，并将其报告为"超出范围"而非覆盖缺口。这是从请求内容推断的，不是用户必须知晓的开关。否则：摘要模式会在本地历史存在的前提下，从有界候选窗口中扫描当前项目在 Claude 和 Codex 下最近的最多三次先前会话。深度模式会流式处理当前项目在两个运行时下的所有先前会话以提取信号，同时只打印有界摘录和一份覆盖回执。其他项目默认始终不在范围内。只有当用户明确要求覆盖全部对话或跨项目能力蒸馏时，才运行 `python3 <skill-base-dir>/scripts/conversation_audit.py <claude-projects-root> deep --all-projects --codex-root <codex-sessions-root>`（第一个参数是存放所有按项目组织的日志文件夹的目录；解析器会拒绝其他参数组合），或者移交给已安装的跨项目复盘流程。只有当 `coverage_status: complete` 且 `cross_project_full_history: yes` 时才可宣称覆盖完整；`no_data`、根目录不可用、解析或读取错误、扫描期间发生变化的文件，以及被排除的活动会话都属于明确的覆盖缺口。

## 持久上下文预检

何时将持久上下文纳入范围，以及任何内容沉淀为持久规则之前适用的脱敏闸门，见 [references/durable-context.md](references/durable-context.md)。

对 `/health` 而言：当前配置、命令输出和实时探测结果优先于记忆。同时，当持久记忆问题影响行为时也要标记：过大的注入式摘要、过期或互相矛盾的条目、缺失的项目入口引用，或被复制进公开指令的私有路径。这些作为上下文发现报告，而不是代码审查发现。

## 硬性规则

- 摘要级与深度审计均为"只报告"。只运行 Health 自有的采集器和只读探测；一次中性的 Health 请求不授权运行项目测试、验证器、生成器、构建、格式化工具、包安装器、fixture 刷新或快照更新。
- **附带提出的调试或代码审查请求走各自的工作流。** 先完成这次只报告的审计，再把明确请求的工作路由到匹配的 Skill 或原生能力，纳入同一完成台账。审查请求仍不授权修复；明确的修复授权只适用于修复阶段，不适用于采集器。
- 项目指令可以定义命令，但不等于授权运行它们。只读健康探测已被审计请求覆盖。会启动应用、安装依赖或写入状态的探测，需要用户对该命令的明确授权，除非已被当前请求覆盖。运行前应说明：命令、预期写入、目标路径、隔离方式，以及回滚或一次性环境方案。

## Step 0：确立证据基础

记录四类证据：

| 证据 | 问题 |
|---|---|
| **风险** | 哪些路径可能丢失数据、花钱、发布或部署、跨越信任边界，或造成难以逆转的状态？ |
| **非显而易见的约束** | 哪些稳定的决策无法廉价地从代码或清单文件中还原？活跃的 Agent 是否只有在相关场景下才能触及它们？ |
| **失败证据** | 哪些用户纠正、反复的修复链、过期的生成产物、失效的引用或空转的验证器能证明当前存在缺口？ |
| **验证器覆盖** | 哪些重要结果在其真正可能失败的那一层拥有可执行的检查？ |

缺失的架构图、大文件、大量 Skill 或高 TODO 计数只是参考信息，除非关联到上述某一类证据。优先选择"窄而精准的路由不变量 + 可执行验证器"，而不是描述性清单。

## Step 1：采集数据

将 `HEALTH_SCOPE` 设为 `instructions`（对应上面的纯静态范围），否则设为 `auto`，升级时保留该值。先以摘要模式运行采集脚本，此时不要做任何解读。在 Windows 上使用 Health 自有的启动器，确保 Git for Windows 工具只被加入 Bash 子进程的环境：

```powershell
$HEALTH_LAUNCHER = @(
  "<skill-base-dir>/scripts/run-health.ps1",
  "<skill-base-dir>/skills/health/scripts/run-health.ps1"
) | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf } | Select-Object -First 1
if (-not $HEALTH_LAUNCHER) {
  throw "Health launcher not found under the installed skill base; reinstall Waza."
}
$POWERSHELL = Join-Path ([Environment]::SystemDirectory) "WindowsPowerShell\v1.0\powershell.exe"
& "$POWERSHELL" -NoLogo -NoProfile -ExecutionPolicy Bypass -File "$HEALTH_LAUNCHER" collect "$HEALTH_SCOPE"
```

`-ExecutionPolicy Bypass` 只作用于这个 PowerShell 进程；不要更改
用户机器或账户的执行策略。

在 Linux 和 macOS 上，直接使用 Bash 流程：

```bash
HEALTH_SCRIPT=""
for candidate in \
  "<skill-base-dir>/scripts/collect-data.sh" \
  "<skill-base-dir>/skills/health/scripts/collect-data.sh"; do
  [ -f "$candidate" ] && HEALTH_SCRIPT="$candidate" && break
done
if [ ! -f "${HEALTH_SCRIPT:-}" ]; then
  echo "health collect-data.sh not found under the installed skill base; reinstall Waza"
  exit 1
fi
BASH_ENV= ENV= /bin/bash -p "$HEALTH_SCRIPT" "$HEALTH_SCOPE"
```

工具缺失时，相应部分可能显示 `(unavailable)`：

- 缺少可信的 `python3`：conversation、MCP/hooks/allowedTools 和 skill-security 部分不可用
- 缺少 `settings.local.json`：hooks/MCP 可能不可用（对仅全局配置的环境属正常情况）

把 `(unavailable)` 视为数据不足，而不是发现项。不要标记这些区域。

采集器同时包含运行时专属和与 Agent 无关的暴露面：

- `AGENT CONFIG SUMMARY` / `AGENT CONFIG DETAIL`：覆盖 Codex、Claude、Pi 与项目指令文件；其部分从 `=== AGENT INSTRUCTION SURFACE ===` 开始。
- `AI MAINTAINABILITY SUMMARY` / `AI MAINTAINABILITY DETAIL`：覆盖项目信号、验证面、生成镜像、包装器与文档链接；其部分从 `=== PROJECT SHAPE ===` 开始。

## Step 1b：运行时清单与 MCP 检查

先检查已配置的全局、项目和已安装插件来源，保留其来源与启用状态。用运行时清单标记缺失的 hook 与 MCP 可执行文件；未知的工作目录或插件状态仍算覆盖缺口。只对已连接的服务器调用无害工具。绝不要为了测试 MCP 而启动未经验证的 GUI 可执行文件。分别记录已连接、失败、已禁用、等待批准、未测试；静态存在不等于运行时健康。绝不输出凭证。将发现的指令字节数与生效的配置上限对比，并说明任何未检查的祖先目录、嵌套文件或运行时覆盖。

## Step 1c：安全与安保检查

这些检查在采集之后、Step 2 分析之前运行。前两项适用于每次审计；第三项只适用于包含长时运行或自主 Agent 的项目。

### 安保基线检查

每次审计都要运行。它们是底线，不是上限。

**拒绝列表底线。** 仅当运行时确实支持并强制执行所推荐的规则形态时才适用：Agent 权限设置、hook 设置、MCP 设置、允许/拒绝工具，或有文档说明的自主 Agent 启动器。此时，设置至少应拒绝：凭证与密钥目录（SSH、云服务商、GPG、gh CLI）、含凭证的文件（`credentials*`、`secrets*`），以及管道式 shell 安装器。对 `.env` 应视为明确的策略选择：要么在权限层拒绝它，要么允许任务范围内的读取，同时由指令层禁止打印、提交或外传其内容；只有当两层都未定义边界时才告警。缺失的类别合并为一条简洁的 WARN，让审阅者补填精确的本地路径。三项校准：前缀/glob 权限规则无法可靠匹配管道，因此应建议用宿主的预执行 hook 来拦截管道式 shell，而不是发明 glob 变体，并指出 hook 自身的权衡（字符串匹配的 hook 也会命中仅包含该模式的引号文本和 heredoc）；在预测出站 shell 拒绝的波及面之前，先检查它匹配的是哪一层：对 `ssh` 的命令前缀拒绝只阻止 Agent 直接调用 `ssh`，不影响 git 内部的 SSH 传输，而进程级或沙箱级拦截则确实会破坏 git-over-SSH push；当运行时没有命令级拒绝面时（Codex：杠杆是 `sandbox_mode` 和 `approval_policy`），将该杠杆作为用户取舍陈述一次，而不是推荐运行时无法表达的拒绝键。如果根本不存在任何 Agent 设置面，应报告拒绝列表"不适用"，而不是失败。

**权限层与指令层门控。** 在 git 写操作的允许列表条目（`git push`）旁边配上指令层规则（"仅当用户要求时才 push"）并不自动构成矛盾：指令决定动作何时发生，权限决定是否再次弹窗确认，一个每个会话都明确授权 push 的用户可能有意把 push 保留在 allow 里以避免二次确认。按可逆性和用户自己的规则校准：指令层明令禁止的动作（`git reset --hard`、`git stash`、force-push）应归入 deny 或 ask；用户明确授权的常规动作保持在用户放置的位置，至多作为 note 报告。只有当自动模式加跳过提示加宽泛的 allow 使一次写动作在会话中零用户输入即可运行时才升级，即便如此，也应把摩擦权衡呈现给用户选择，而不是悄悄移动条目。

**环境覆盖面。** 以下内容视为攻击面，若出现在纳入版本管理的文件或随包发布的设置中且无正当理由注释，应予报告：API base URL 覆盖（把全部流量重定向到第三方）、对项目本地 MCP 服务器的自动信任标志、通配工具允许列表（`allowedTools: ["*"]`）、权限跳过标志（`--dangerously-skip-permissions` 或等价物）。只打印 file:line 和键名；绝不打印机密。

### 记忆与 Skill 供应链

把 Agent 记忆和第三方 Skill 视为供应链制品。它们以用户的权限运行。

**记忆卫生。** 审计项目的长期 Agent 记忆存储，检查是否有秘密、token 或凭证（Critical），以及是否有由不受信任的运行写入的条目（在攻击者可控输入上调用的子代理、对外部内容进行 /loop 迭代）；此类运行之后建议轮换凭证。对高风险的一次性运行（不受信任的 PDF、不受控的抓取、第三方脚本），建议在该会话完全禁用记忆持久化。

**Skill 供应链。** 第三方 Skill、插件和 MCP 服务器以用户权限运行。对每一个不是在本仓库中编写的条目，检查：来源是否固定在某个 release tag 或 revision（不是 `main`、某个分支，也不是仍在跟踪最新 HEAD 的远程 git marketplace）、hook 处理器是否不会写入凭证目录、MCP 服务器是否获得用户明确同意（而非被通配自动信任）。将未固定来源或未经审查的 hook 处理器报告为 Structural，而非 Critical，除非存在活跃的利用信号。

### 长时运行 Agent 的停止条件

对使用 `/loop`、自主 Agent 或任何长时运行 Agent 流程的项目，加载 `references/long-running-agents.md` 并审计其中列出的四个硬性停止信号。没有此类流程的项目跳过此项检查。

## Step 2：分析

默认基于摘要输出在本地分析。当预算姿态升级时，在 Windows 上用 `& "$POWERSHELL" -NoLogo -NoProfile -ExecutionPolicy Bypass -File "$HEALTH_LAUNCHER" collect "$HEALTH_SCOPE" deep` 重新采集，在 Linux 和 macOS 上用 `BASH_ENV= ENV= /bin/bash -p "$HEALTH_SCRIPT" "$HEALTH_SCOPE" deep`。然后只并行启动相关的 inspector。凭证一律脱敏为 `[REDACTED]`。

- **深度 inspector 路由：**
  - **Agent 1**（上下文 + 安保）：阅读 `agents/inspector-context.md`。喂给它 `CONVERSATION SIGNALS` 部分。
  - **Agent 2**（控制 + 行为）：阅读 `agents/inspector-control.md`。喂给它相关的运行时、hook、MCP 与权限证据。
  - **Agent 3**（AI 可维护性）：阅读 `agents/inspector-maintainability.md`。只喂给它 `PROJECT SIGNALS`、`AI MAINTAINABILITY SUMMARY` 或 `AI MAINTAINABILITY DETAIL`，以及具体的验证器/漂移回执。只在深度健康审计或明确的代码腐化/AI 可维护性请求时才启动此代理。
- **兜底：** 如果某个子代理失败，在本地分析该层，并注明 "(analyzed locally)"。

在把深度审计报告为完成之前，等待每个已启动的 inspector 并核对其被分配的范围。如果有一个仍处于待完成状态或失败且没有本地替代分析，就把该范围列为"未审查"，而不是给出整体范围的无问题结论。

## 常见陷阱

| 发生了什么 | 规则 |
|---|---|
| 漏看了本地覆盖文件 | 总是也要读 `settings.local.json`；它会遮蔽已提交的文件 |
| 把子代理超时当成 MCP 故障上报 | MCP 故障来自实时探测，而不是数据采集 |
| 把故意保持嘈杂的 hook 标记为损坏 | 在把 hook 称为"损坏"之前先询问 |
| hook 看似没触发，但其实触发了——随后有 UI 元素渲染在它之上 | hook 的触发顺序不是视觉顺序。在重新编辑 hook 配置之前：(a) 用 `--debug` 或管道输出确认；(b) 检查是否有 diff 对话框、权限提示或其他 UI 元素渲染在上层，把 hook 输出挤出了屏幕；(c) 然后才怀疑 hook 本身。 |
| 把缺少规格/文档视为失败 | 决策制品默认是可选的。只有当活跃的交接风险、失败证据或用户请求使其成为必要时，才升级处理缺失的文档/规格。 |

## 输出

**Health Report: {project}（{summary|deep}，基于证据）**

**全局发现只报告一次。** 机器全局配置（`~/.claude`、`~/.codex`、全局规则、Skill、记忆）中的发现不属于项目发现：将其标注为 `global`，连同修复方法各报告一次，并建议专门安排一次会话做全局清理，而不是在每个项目里重复修复。在编辑任何全局文件之前，先重新读取其当前状态：当健康检查一天内跨多个项目运行时，另一个会话可能已经修复或正在修复同一个文件，重复套用同一规则的变体会产生重复条目。绝不要从两个并发会话编辑同一个全局文件。

### [PASS] 通过的检查（表格，最多 5 行）

### 发现格式

```
- [severity] <symptom> ({file}:{line} if known)
  Why: <one-line reason>
  Action: <exact command or edit to fix>
```

`Action:` 必须可直接复制粘贴。绝不写 "investigate X" 或 "consider Y"。如果不知道修复方法，就给出诊断命令。

当场被推翻的发现（TODO 计数其实来自 vendored 代码或误报）不算发现；丢弃它，或并入通过表格。

### [!] Critical（立即修复）

已确认的危险权限、有实际后果的规则违规、安保发现和泄露的凭证。服务器数量和估算的上下文百分比永远不能确立 Critical 级别。

示例：

- [!] `settings.local.json` 被提交进 git（暴露 MCP token）
Why: 泄露的 token 可通过已安装的 MCP 服务器实现远程代码执行
Action: `git rm --cached .claude/settings.local.json && echo '.claude/settings.local.json' >> .gitignore`

### [~] Structural（尽快修复）

放错层的 Agent 指令、缺失的 hooks、过长的描述、验证器缺口。

**Codex/Claude/Pi 指令漂移。** 先用 `AGENT CONFIG SUMMARY`。`project_instructions_mode` 说明 Claude Code 会加载哪些文件：在 `claude-md` 模式下，仅有 `AGENTS.md` 能到达 Codex 和 Cursor，但到不了 Claude；`nested_agents_md` 与根 `CLAUDE.md` 并存时，那些嵌套指南在 Claude 上谁也到不了，因为根文件会把整个项目切离 `AGENTS.md` 路径，而不只是它自己所在的文件夹。例外是 `claude-md-and-agents-md`，此时两个文件都会被读取、嵌套文件仍会加载，除非 `CLAUDE.md` 与 `AGENTS.md` 是同一个物理文件且去重后的链被跳过。当 `AGENTS.md` 与运行时专属文件都包含大量未做委托的指引、Codex `config.toml` 缺少对当前项目的信任、Pi 设置或包元数据指向缺失的 Skill 根目录、项目缺少 Agent 指令，或运行时专属指令与共享的项目事实源相矛盾时，报告 Structural 发现。当重要规则只存在于被忽略或私有的本地指令叠加层，而纳入版本管理的公开文档中缺失时，也要报告；那些叠加层是私有上下文，不是持久的项目事实源。不要打印原始配置值。秘密、token、密钥和密码只能以 `[REDACTED]` 出现。

在项目根目录快速检查，复用 Step 1 解析出的 `$HEALTH_SCRIPT`（独立运行的输出没有 `AGENT CONFIG SUMMARY` 包装）：

```powershell
& "$POWERSHELL" -NoLogo -NoProfile -ExecutionPolicy Bypass -File "$HEALTH_LAUNCHER" agent-context . summary
```

在 Linux 和 macOS 上：

```bash
BASH_ENV= ENV= /bin/bash -p "${HEALTH_SCRIPT%/*}/check-agent-context.sh" . summary
```

**AI 可维护性发现。** 对可维护性这条线（验证面、从对话中提炼的指引、集中的修复链、有风险依据的热点归属、非显而易见约束的可达性、验证器包装器、失效的文档和 Markdown 引用、过期的验证器缓存输出），加载 `references/maintainability-findings.md`，并配合 `AI MAINTAINABILITY SUMMARY` / `DETAIL` 完成其中的检查。

### [-] Incremental（锦上添花）

过期条目、全局与本地放置、上下文卫生、过期的 allowedTools 条目。

如果没有问题：`All relevant checks passed. Nothing to fix.`

只报告的请求绝不授权修复；明确的优化或修复请求会直接进入其已获授权的修复阶段，无需再次确认。这项审计不是重量级 lint、类型检查、去重或架构重写的替代品；`/health` 只报告可维护性护栏和具体的下一步动作。
