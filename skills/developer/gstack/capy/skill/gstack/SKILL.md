---
name: gstack
description: 在 Capy 和 Claude Code 中安装并使用 gstack。会话开始时加载以检查本机状态，并用于 gstack 的计划、代码审查、调试、QA、设计、安全、文档和发布工作流。
---

> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`capy/skill/gstack/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# gstack for Capy 和 Claude Code

## 会话开始：先检查，确有需要才安装

`scripts/install.sh` 相对本 SKILL.md 解析，不相对工作仓库。它是一个冻结
的引导器：先打印 `gstack-capy-skill: wrapper <n> (<path>)`，从 gstack
远端获知受支持的最低版本，然后移交到 checkout 自己的 wrapper
（`bin/gstack-capy-session`）。

1. 会话开始时运行 `bash scripts/install.sh --check`，已知工作流时加
   `--for <skill>`（`--for autoplan`、`--for review`、`--for qa`）。它会为
   每个组件打印一行 `PASS|FAIL|SKIP|WARN <component>`（`WARN` 是需要
   owner 处理的事项）、一行 `GSTACK_LAUNCH:`，并在最后一行恰好打印一个
   尾行：`gstack: ok <revision> for=<skill>[ (<notes>)]`（exit 0）或
   `gstack: fail <ids> …`（exit 1）。直接读 exit 状态并 grep `^gstack: `；
   绝不只用 `tail`、`head` 或 `grep` 管道处理检查输出。`--check` 不会
   移动 checkout。
2. 若尾行指出 `revision`、`runtime` 或 `pins`（`gstack: fail revision …`、
   `gstack: fail runtime,pins`、`gstack: fail pins`）且 checkout 存在，或
   ok 尾行带有 `behind=<n> (latest: <v>); fix: <command>`（checkout 落后
   origin <n> 个 commit；输出中还有一行
   `gstack-capy-session: behind origin/<branch>: …`），则运行同一命令但不
   带 `--check`（900 秒超时），或运行尾行指定的另一个 `fix:` 命令。逐字
   报告尾行，包括 `behind=`：落后的 lane 要说出来。对 `pins`，若 pin 指向
   一个已验证版本则安装项目固定的 Bun，否则以 `RUNTIME_PIN_CONFLICT`
   停止并点名要升级的 pin。任何干净、未 pin 且落后于 origin 的 checkout
   在安装模式中会被 fast-forward（低于 `GSTACK_MIN_REVISION` 下限的由
   引导器处理，打印 `gstack-capy-skill: upgraded <old> -> <new>`；高于下
   限的由 checkout 处理，打印 `SELF_UPGRADE: done <old> -> <new>`）、重装
   并重查，一步完成且全程加锁。被 pin 的（`--revision`、detached）、脏
   的、分叉的 checkout，或被另一个活跃会话持有租约的（`UPGRADE_BUSY`），
   一律不动：尾行会说明原因和确切命令（高于下限时，在
   `SELF_UPGRADE: skipped (<reason>)` 之后是 `fail behind` 尾行，附
   `UPGRADE_BUSY` 或 `UPGRADE_REFUSED`）。唤醒后 pid 被复用的租约会自动
   回收。`GSTACK_CAPY_AUTO_UPGRADE=0` 禁用所有 fast-forward，
   `GSTACK_CAPY_SELF_UPGRADE=off` 只禁用高于下限的那一种。
3. 若尾行是 `gstack: fail not-installed …` 且本次会话不运行任何 gstack
   工作流，记录该行并继续；什么都不安装。在第一个工作流之前再安装：
   `bash scripts/install.sh --for <skill>`（冷启动约 30 秒：clone、
   在没有可用 Bun 时安装经 SHA-256 校验的 Bun、两个 host profile（不含
   Chromium）、以及一个让新 shell 拿到所记录 Bun 的
   `~/.local/bin/bun` shim）。
4. 任何其他 `FAIL` 行都带 `fix:` 命令和带排障锚点的理由码；运行修复，
   再 `--check`。`SKIP codex-cli (optional; …)`、`SKIP browser (lazy; …)`、
   `SKIP pins (planning-only; …)` 和 `SKIP pins (helper runtime; …)` 不算
   失败。

**尾行规则。** 本机在本会话中没有 `^gstack: ok` 行，就意味着 gstack
未在本机安装：不要运行工作流，也不要声称 Skill 可用。一台机器的安装
永远覆盖不了另一台。

**子代理。** 子代理发给父代理的第一份报告，要逐字附上它自己那台机器
`--check` 的 `gstack:` 尾行，放在其标识符之后。父代理把缺失该行当作
`gstack: fail not-installed`。只读报告的评审子代理（/autoplan 的一个
voice、第二意见）改跑 `--for review-voice`：热态下只要几秒，无需
`./setup`，无需 host profile，Bun 用 gstack 自己的最低版本，且其尾行只
为只读 helper 作证（`gstack-pregate sealed`、`gstack-plan-reality`、
`gstack-artifact` 及 `gstack-autoplan` 的读操作）；每个工作流都会拒绝它
并给出 `--for <skill>` 修复。绝不告诉评审者"不需要安装"。没有本 Skill
的机器（你为子代理写的 brief）从其项目目录运行 checkout 自己的引导器：
`test -f "$HOME/.local/share/gstack/setup" || git clone --quiet --single-branch --depth 1 https://github.com/garrytan/gstack.git "$HOME/.local/share/gstack" && GSTACK_CAPY_ROOT="$HOME/.local/share/gstack" bash "$HOME/.local/share/gstack/capy/skill/gstack/scripts/install.sh" --for <skill>`。

`gstack-capy-skill: owner action — Drive copy is wrapper <n>, minimum <m>; copy <root>/capy/skill/gstack/ (CAPY_WRAPPER_STALE)` 表示本 Skill
文件夹比 checkout 期望的旧。运行仍可工作；告知 owner，由 owner 把该
目录复制覆盖 Skill 文件夹。绝不自己写 Skill 文件夹。

## 每条 gstack 命令都带上 GSTACK_LAUNCH 行

每次成功运行（包括 `--check`）都会打印
`GSTACK_LAUNCH: PATH=<dir>:$PATH GSTACK_SESSION_KIND=unattended GSTACK_STATE_ROOT=<path> GSTACK_EPHEMERAL=1 GSTACK_CAPY=1 GSTACK_INSTALL_VERDICT=<file>`（仅当验证过的 Bun 不在 PATH 首位时才含
`PATH=` 部分），随后为不便求值 shell 语法的调用方打印
`GSTACK_LAUNCH_PATH: <dir>`。给每条 gstack 命令加上这些前缀赋值，或在
运行它的 shell 里 export 一次；子 shell 的 export 配置不了父 shell 之后
的命令。PATH 部分正是让 gstack 的 `#!/usr/bin/env bun` 命令跑在尾行认证
过的 Bun 上的关键：Capy 镜像的 `/usr/local/bin/bun` 是 1.3.14，低于
gstack 的最低要求。

带 `GSTACK_CAPY=1` 时，在无人值守或派生会话中启动的工作流会检查上次
运行为本 checkout、HEAD 和工作流写入的安装裁定，以及 PATH 上的 Bun。
任一失败则打印一行 `INSTALL: fail …` 及其修复方法、输出
`GSTACK_RESULT: skill=<s> status=refused run=-` 并以 exit 3 退出：停下，
运行修复，重新开始。ok 但 pins 行为 `SKIP pins (planning-only; …)` 的
裁定，不允许运行 repo 测试的工作流（`review`、`ship`、`qa`）；没检查过
工作流所需组件的裁定同样不允许；先跑 `--for <那个 skill>`。

## 加载正确的工作流

Capy 运行 GPT-6 Astra 时，读
`${CODEX_HOME:-$HOME/.codex}/skills/gstack/SKILL.md` 获取路由，再读
`${CODEX_HOME:-$HOME/.codex}/skills/gstack-<skill>/SKILL.md` 获取选定的
工作流。这些是生成的 GPT-6 Astra 指令，不是 Claude 源文件。

Claude Code 中，读 `~/.claude/skills/gstack/SKILL.md` 获取路由，读
`~/.claude/skills/<skill>/SKILL.md` 获取选定的工作流。启动 Claude Code
会话时，告诉它加载 gstack 并点名预期工作流。Capy 运行 Claude 模型时，
可直接读 Claude 指令文件并按下面的 Capy 适配执行；这不会把 Capy 变成
Claude Code harness。

未指定具体 Skill 时，使用路由器的任务到 Skill 映射。只读选中的工作流
及其引用的文件。其他模型使用最接近的适用指令画像，但不得声称为其生成
或评估过模型专属画像。

## 为父代理做无人值守运行

Capy 驱动 `/autoplan` 时，读 checkout 中的 `autoplan/DRIVER.md`
（`~/.local/share/gstack/autoplan/DRIVER.md`）：紧凑的阶段循环、产物
契约和门控协议，不含交互式前导。没有该文件的 checkout 早于它；改按其
`autoplan/SKILL.md` 执行。每条命令都带 `GSTACK_LAUNCH` 赋值，把输出当
文件读而非读散文：run 目录里有 `run.json`、`decisions.jsonl`、
`findings.jsonl`、`tasks.jsonl`、`timing.json`、`plan.md` 和
`review-record.md`，运行以
`GSTACK_RESULT: skill=autoplan status=gate_pending run=<dir>` 结束。
`~/.local/share/gstack/bin/gstack-artifact validate <dir>/run.json` 是
完成检查。门控通过 `gstack-autoplan answer`（或 `gstack-gate parse`）
用打印出的 `gate_rev` 回答；无人值守运行绝不批准自己的门控。checkout
中的 `docs/unattended.md` 是契约。

`/autoplan` 的 Capy 检查清单：驱动 `gstack-autoplan`，绝不把手工改编
冒充为一次运行。转发 `gstack-gate render <dir>/gate.json --all`，默认
答复为单词 `rec`（涵盖每条 recommendation，包括计划变更）；回答用
`--by agent:<id> --owner-reply "<他们的原话>"`。把
`GSTACK_AUTOPLAN_CHECKPOINT_DIR` 设为私有的项目用户 Drive 文件夹；换机
后 `gstack-autoplan resume --out <新目录> --from <该目录>` 恢复最新的
有效检查点。

## 在 Captain 之下工作

当你为 Capy Captain（crew 线程）或直接为某个人工作时，gstack 的决策
经由你传达。每次带 `GSTACK_LAUNCH` 行启动的工作流都会打印 `CAPY: on`
和一个重复这些规则的 `capy-asks` 块。带完整示例和可复制模板的完整指南
见本文件夹的 [captain.md](captain.md)。

- **审批如何流转。** crew 线程从不直接问人。它把请求作为 needs-you
  报告发给 Captain，由 Captain 用平实的语言问人并带回其确切答复。
  没有 Captain 的线程用 Capy 提问。一个答复只覆盖它被询问的线程和范围。
- **常设审批无需再问。** 这些是 Captain 在其规则中列出的（例如
  "绿灯即合并，走 train"）。引用规则即可，不必再问。
- **这些始终需要新的审批：** 产品或行为决策、超过既定上限的花费、
  任何发布到仓库之外的东西、对阈值/预算/试用次数的更改、未合入就关闭
  他人的贡献，以及任何破坏性操作。
- **记录每个答复。** 用
  `gstack-approvals add --ask … --words "<他们的确切原话>" --by … --scope …`；
  autoplan 答复之后用 `gstack-approvals import --autoplan <run dir> --by <name>`。
  `gstack-approvals render` 打印供报告和 PR 正文使用的 `## Approvals`
  表。各行经过密钥扫描，在 Capy 上会镜像到私有 Drive 文件夹。
- **计划审批** 用 `gstack-owner-brief render --captain --out <run dir>`。
  它打印 before → after、为什么重要、本次工作的起因、重大决策（选项、
  选择、理由、什么会推翻它）和需要什么，`rec` 为推荐的一词答复。完整
  转发。门控码只出现在最后一行，那是给你看的。若以
  `CAPTAIN_BRIEF_INCOMPLETE` 退出，先补齐缺失的计划章节。
- **合并请求。** /ship 的 PR 正文以 `## What changed`（`gstack-pr-shots`
  的前后对比图或 UI 截图，用 Capy 的 PR 资产工具上传）、`## Why` 和
  `## Approvals` 开头。你的 READY 报告附上关键图片。

## 任何 push 或 PR 之前

在配置了 sealed（`.gstack/pregate.json` 中有 `sealed` 键）的仓库中，每次
push 和创建 PR 之前运行
`~/.local/share/gstack/bin/gstack-pregate sealed`：Capy 的 PR 工具可能
不运行本地 git hook，因此这是防止 sealed 或 eval 输出流入公开仓库的
检查。拒绝时会点名文件、行和规则；通过之前不要 push。

## 把 host 专属指令适配到 Capy

- "调用 `Skill`"的指令意味着用可用的文件读取工具读取并遵循选定的
  SKILL.md。不要调用不存在的 Skill 工具，也不要假定斜杠命令已在 Capy
  的 UI 中注册。
- 用 Capy 的用户可见消息与提问工具做输出和决策。纯助手文本在 Capy 中
  不是已送达的消息。用 Capy 的任务和 PR 工作流，替代不可用的 Claude 或
  Codex host 工具。
- Capy 没有原生 gstack host 目标。Claude hook 不会变成受强制的 Capy
  hook；安全类 Skill 在此仅为建议性，`/autoplan` 会打印一次
  `autoplan guard: not enforced by this host` 说明此事。缺失的能力要
  报告，不要静默声称有等价强制。
- 在 Capy 中选择 GPT-6 Astra 或 Claude 不会安装或认证 Codex 或
  Claude Code CLI。跨模型评审时，另一模型家族上的子代理就是一个完整的
  外部声音；记录实际参与评审的模型。其他 runner 已评审时，不要把缺失
  Codex CLI 报告为覆盖降级。
- 保留用户要求的范围、决策和同意。不要代他们开启 telemetry 或远程产物
  共享。安装 gstack 不授权合并、部署、破坏性操作或绕过审批。

## 维护

`bash scripts/install.sh --check` 是健康检查；`bash scripts/install.sh`
负责安装、修复并把低于受支持下限的 checkout fast-forward。两次下限
调整之间，`~/.local/share/gstack/bin/gstack-upgrade --check` 报告
checkout 是否落后，`~/.local/share/gstack/bin/gstack-upgrade` 把它
fast-forward 到默认分支顶端并重装（拒绝脏、分叉或被 pin 的 checkout，
绝不 stash 或 reset）。安装器面向 Capy 的 Ubuntu 云机器，需 Git、curl、
Node.js、flock 和 timeout；未经许可不要在个人设备上运行。
