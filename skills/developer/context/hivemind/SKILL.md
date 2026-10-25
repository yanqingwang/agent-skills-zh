---
name: hivemind
description: 从 Claude Code 编排免费的 opencode worker，以削减 token 成本。当需要把粗重工作委托给单个 worker 或具备 worktree 隔离的并行 swarm（scout/coder/tester）、针对 opencode 做基准测试，或用户提到 "spawn a worker"（派生 worker）、"swarm"（蜂群）、"delegate to opencode"（委托给 opencode）或 "/oc" 时使用。
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`engineering/hivemind/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Hivemind：Claude Code 当编排者，opencode 当免费 worker 蜂群

Claude Code = 大脑（规划、审查、合并）。opencode = 免费模型上的一次性 worker
（默认 `opencode/mimo-v2.5-free`；已验证每次运行 $0.00）。

## 前置条件（外部依赖）

本 Skill 是 **[opencode](https://opencode.ai)**（一个第三方 CLI）之上的薄编排层。
它不随包附带 —— 请先自行安装并完成认证：

| 要求 | 说明 |
|---|---|
| Node.js >= 18 | 脚本使用了 `fetch` 和 `node:timers/promises`。 |
| `opencode` CLI 在 `PATH` 上 | `npm i -g opencode-ai`（或 opencode 文档提供的安装器）。 |
| 一个已完成认证的 opencode 账号 | `opencode auth login`。Worker 以你的账号运行。 |
| 默认模型 `opencode/mimo-v2.5-free` | 这是 opencode（而非 Anthropic）提供的免费档位。可用性、速率限制和定价由 opencode 自行变更 —— 随时可用 `--model` 覆盖。 |
| 仅 Windows：`OPENCODE_GIT_BASH_PATH` | 指向 `C:\Program Files\Git\bin\bash.exe`，需持久化设置。 |

## 数据流向（安装前必读）

Hivemind 是可选加入的，不随任何领域 bundle 附带。**默认情况下，你的代码会离开你的机器：**
默认模型 `opencode/mimo-v2.5-free` 运行在 opencode 的托管服务上，因此每个 worker 都会
把它的提示词，以及你交给它的任何文件或 diff，发送到 opencode 的端点。
Worker 侧不会有任何东西调用 Anthropic API。

若要让代码留在本地，请把 `--model` 指向你自有机器上提供的模型（例如在
你的 opencode 配置里配置好的 Ollama 或 LM Studio provider）。使用托管模型时，
只委托你被允许发送给该 provider 的代码，并且绝不委托机密信息。

## 安装（Setup）

1. 把本 Skill 文件夹放到你的 Agent 加载 skills 的位置（例如 `~/.claude/skills/hivemind`）。
2. 导出 `HIVEMIND_HOME` 指向该文件夹 —— 内置的 slash 命令会用到它：
   ```
   export HIVEMIND_HOME="$HOME/.claude/skills/hivemind"
   ```
3. 把内置资产复制到位：
   - `assets/commands/*.md` -> `~/.claude/commands/`（`/hive`、`/oc`、`/swarm` 等入口）
   - `assets/agents/*.md` -> `~/.config/opencode/agent/`（scout / coder / tester worker 角色）

两份复制都是可选的：这些命令所做的一切都可以通过直接调用
`scripts/oc-worker.mjs` 来驱动，并且任何 opencode agent 名称都能配合 `--agent` 使用。

运行时状态（`.runs/*.jsonl`）写在本文件夹内，且已被 gitignore。

## 组件

| 路径（相对于本 skill 目录） | 用途 |
|---|---|
| `scripts/oc-worker.mjs` | 唯一被认可的 worker 调用方式。加固过的接入点。 |
| `scripts/oc-status.mjs` | 从运行日志读取蜂群进度（`oc-status.mjs <run-id>`） |
| `scripts/oc-aggregate.mjs` | 对 N 个 worker 的输出去重/综合；共识结论优先 |
| `scripts/bench/run-bench.mjs` | 基准测试配置 A（claude 单干）、B（opencode 单干）、C（编排蜂群） |
| `scripts/bench/grader-prompt.md` | 盲评评分细则（最高 12 分 + PASS/FAIL 门槛） |
| `scripts/oc-verify.mjs` | 把某个 worker 的断言发给运行在不同模型上的验证者；返回计数 + `needs_review` |
| `assets/commands/` | 复制到 `~/.claude/commands/` 的 slash 命令入口 |
| `assets/agents/` | 供 opencode 使用的 scout / coder / tester / verifier agent 定义 |

Slash 命令（随包附带于 `assets/commands/`，复制到 `~/.claude/commands/`）：
- `/hive <task>` - 自动路由器（AUTO-ROUTER）。把任务分类 -> 单 worker、通用蜂群或模板。默认入口；优先使用它而非手动路由。
- `/oc <task>` - 单 worker 委托
- `/swarm <task>` - 通用并行蜂群
- `/review-panel <diff>` - 4 视角并行审查（正确性/安全性/性能/风格）+ 共识聚合
- `/research-sweep <question>` - 3-5 个并行研究角度，综合汇总
- `/migration <task>` - 按 worktree 分批的迁移 worker + 顺序化合并
- `/test-fleet <target>` - 带安全检查的分区并行测试运行

Worker agent（随包附带于 `assets/agents/`，复制到 `~/.config/opencode/agent/`）：
- **scout** - 只读调研（无 write/edit/bash）
- **coder** - 在自己的 worktree 中实现一个子任务
- **tester** - 只运行测试，绝不编辑源码

## 调用契约（Invocation contract）

```
node "<skill-dir>\scripts\oc-worker.mjs" [--agent scout|coder|tester] [--dir <path>] [--model <p/m>] [--timeout 900] [--run <id> --label <name>] [--json] "TASK TEXT"
```

只返回恰好一行紧凑 JSON：
`{ ok, result, tokens:{total,input,output,cache}, cost_usd, duration_ms, label, agent, model }`

失败时：`{ ok:false, stage:"args"|"exec"|"api"|"parse"|"empty"|"schema", error }`，stderr 截断至 300 字符。

`--json` 使 `result` 成为一个 JSON 值：脚本会从回复中提取它，给模型一次
纠正性重试，若仍得不到可解析的 JSON 则以 `stage:"schema"` 失败。

`--run <id>` + `--label <name>` 会把生命周期事件（start/done/fail）追加到本 skill 目录内的
`.runs/<id>.jsonl`。每个蜂群 worker 都要使用它们，这样即使编排者的上下文丢失，
进度仍可通过 `oc-status.mjs` 恢复。

脚本自动管理共享服务端：对 `127.0.0.1:4096` 做健康检查，若已死则启动 `opencode serve`，等待 5 秒，回退到冷启动。Worker 对其 `--dir` 是幂等的；放弃前先重试一次 `ok:false`。

`HIVEMIND_SERVER_URL` 可覆盖该地址（默认 `http://127.0.0.1:4096`）。它必须是
带数字端口的有效 URL；任何其他取值都会以一行 `stage:"args"` JSON 快速失败，
而不会到达被启动的进程。


## 验证而非重读（在你相信一个断言之前先做这件事）

自己复核每个 worker 的断言，其成本会超过委托省下的开销。改为把断言
发给一个验证者（verifier）：

```
node scripts/oc-verify.mjs --dir <same dir the worker saw> --claims findings.json --run <id>
```

返回 `{ confirmed, refuted, unsupported, unverified, needs_review[] }`。只需阅读
`needs_review` —— 那些就是被驳倒和未被支持的断言。已确认的断言只有计数，
没有长篇文字，不会回流到你的上下文里。

本阶段的硬性规则：
- 验证者必须运行在与 worker 不同的模型上。同模型 = 同样的盲区 = 走过场式的橡皮图章。验证者默认使用
  `opencode/nemotron-3.5-lightning-free`，对抗 worker 默认的 `opencode/mimo-v2.5-free`；
  如果二者你改了任何一个，就传 `--model`。
- 验证者看到的是文件和断言，永远看不到 worker 的推理过程。
- 不确定时默认判 REFUTED（驳倒），因为一个错误的 CONFIRMED（确认）会被不加核查地执行。
- `unverified > 0` 表示验证者跳过了部分断言。把它们当作未验证，而不是已通过。
- 仍要自己抽检一部分。两个免费模型意见一致是证据，不是证明。

## 免费模型并不总是可用

免费的 `opencode/*` 模型返回 provider 404 和空响应体的频率之高，足以让
无人值守的蜂群无法依赖其中任何一个。绝不硬编码免费模型 id：它们
会在毫无预警的情况下不再是免费的。对定时或批量任务请显式传 `--model`，
并且当某个免费模型失败两次后，遵循下文的回退阶梯，而不是继续重试。

## 黄金法则（不可协商）

原始 opencode NDJSON 流绝不能进入你的 context window。所有输出都经由脚本的
单行 JSON 到达。绝不要把 `opencode run --format json` 直接管道进本
对话；绝不要重新实现脚本所做的事。

## 单 worker 流程（/oc）

对一个只读问题或小型委托：不带 worktree 运行 oc-worker.mjs。
只读任务可省略 `--agent`/`--dir`。向用户总结 `result`。
如果写入了文件：在让用户 commit 之前先展示 `git diff`。

## 蜂群流程（多 worker）

1. 把任务分解为 2-5 个相互独立的子任务（不共享文件）。
2. 要写入的 worker 先拿到隔离的 worktree：`git worktree add ../<repo>-wt-N -b swarm/N`。
3. 在同一条消息中，以并行的 Bash 工具调用发出全部 worker 调用。
4. 亲自审查每一个 diff（`git diff main...swarm/N`）。你是唯一的合并者。
5. 合并已批准的分支，移除 worktree，运行测试。
6. 报告表格：子任务 | agent | token 数 | 结果 + worker token 总数。

硬性规则：worker 之间绝不共享目录；绝不委托合并/审查；
只有当某个免费模型 worker 明确失败两次时，才升级到你自己的 Sonnet。

## 基准测试（Benchmarking）

```
node scripts\bench\run-bench.mjs --repo <project> [--configs a,b,c] [--task 1-5]
```
把 JSONL 记录（ts, config, tokens, cost, duration）追加到 `bench-results.jsonl`。
用 `grader-prompt.md` 盲评产物（评分者只看到任务规格 + 输出）。
配置：A=claude 单干基线，B=opencode 单干，C=claude 编排 2 个 worker。

## 回退阶梯（所有流程通用）

1. Worker `ok:false` -> 对同一目录重新调用一次。
2. 仍然失败 -> 编排者在线（inline）自行完成该子任务，并标记 `[orchestrator-sourced]`。
3. opencode 彻底宕机（`exec`/`api` 失败两次）-> 宣告情况，放弃 worker，直接自行完成任务。
绝不要让蜂群搞砸一个 Claude 本可以自己完成的任务。

## 蜂群模式（Fleet patterns）

四种可复用的拓扑以 slash 命令形式随包附带（见上表）。共享的不变量：
在一条消息中并行启动；每个 worker 都带 `--run/--label`；当 3 个及以上 worker
产出结论时通过 `oc-aggregate.mjs` 聚合；共识胜过单一视角的断言；
只要有任何 worker 要写入，就使用 worktree 隔离。

## Windows 注意事项（血泪经验）

- 需要 `OPENCODE_GIT_BASH_PATH=C:\Program Files\Git\bin\bash.exe`（持久化设置）。
- 脚本通过解析 npm 的 `.cmd` shim 来定位真正的 `opencode.exe` —— Node 的
  EINVAL 策略会阻止直接启动 `.cmd`。不要把该解析器"简化"回
  `where.exe` 取第一行的写法。
- 免费模型：`opencode/mimo-v2.5-free`、`opencode/nemotron-3.5-lightning-free`、
  `opencode/hy3-free`。注意：`opencode-go/*` 模型需要 workspace 计费 —— 避免使用。

## 已知局限

- 免费档位的速率限制在重负载蜂群下可能触发 429；重试之间要拉开间隔。
- Worker 质量参差不齐；务必审查 diff。Scout 的回答附有证据引用。
- 基准配置 C 会为编排消耗真实的 Claude token（约 1-2k/任务）。

## 反模式

| 反模式 | 为什么会坏 | 应该这样做 |
|---|---|---|
| 把 `opencode run --format json` 直接管道进编排者 | 原始 NDJSON 淹没上下文 —— 正是本 Skill 要避免的那笔成本 | 始终经由 `scripts/oc-worker.mjs`，它只返回一行紧凑 JSON |
| 两个要写入的 worker 共处一个目录 | 并发编辑互相破坏对方的 diff | 每个写入型 worker 一个 git worktree，在启动前创建 |
| 让 worker 合并、审查或批准自己的分支 | 免费档位 worker 是对自身产出最不可靠的评判者 | 编排者是唯一的合并者，也是唯一的审查者 |
| 逐条消息顺序启动 worker | 完全失去蜂群的墙钟时间收益 | 在同一条消息中，以并行调用发出每一个 worker 调用 |
| 无限重试一个失败的 worker | 烧光速率配额并卡住任务 | 重试一次，然后在线自行完成该子任务并标记 `[orchestrator-sourced]` |
| 委托机密、凭证或私有代码 | Worker 流量会流向 opencode 的端点 | 敏感上下文留在编排者手里；只把可安全共享的内容发给 worker |
| 把 `cost_usd: 0` 当作永久保证 | 免费档位属于 opencode，随时可变 | 在依赖零成本做批量工作之前，重新核对定价 |

## 交叉引用

- `engineering/llm-cost-optimizer` —— 在 Hivemind 决定*怎么做*之前，先判断一个任务*值不值得*委托
- `engineering/agent-harness` —— 编排者一侧循环的 Harness 模式
- `engineering/workflow-builder` —— 适合不需要独立 worker 判断力的确定性流水线
- `engineering/skills` 与 `engineering/write-a-skill` —— `assets/agents/` 中 worker agent 定义所采用的编写规范
