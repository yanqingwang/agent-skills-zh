---
name: autonomous-loops
description: "用于 Claude Code 自主循环（autonomous loop）的模式与架构——从简单的顺序流水线到 RFC 驱动的多 Agent DAG 系统。仅为兼容性保留：当需要新的自主循环指引时，请改用 `continuous-agent-loop`。"
metadata:
  origin: ECC
---

> **中文汉化版** · 上游：[affaan-m/ECC](https://github.com/affaan-m/ECC) · 原文件：`skills/autonomous-loops/SKILL.md` · License: MIT
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 自主循环（Autonomous Loops）Skill

> 兼容性说明（v1.8.0）：`autonomous-loops` 仅保留一个发布周期。
> 规范的 Skill 名称现在是 `continuous-agent-loop`。新的循环指引
> 应写在那里，而本 Skill 仍保持可用，以免破坏现有工作流。

在循环中自主运行 Claude Code 的模式、架构与参考实现。涵盖从简单的 `claude -p` 流水线到完整的 RFC 驱动多 Agent DAG 编排的一切内容。

## 何时使用

- 搭建无需人工干预即可运行的自主开发工作流
- 为你的问题选择合适的循环架构（简单 vs 复杂）
- 构建 CI/CD 式的持续开发流水线
- 运行带合并协调的并行 Agent
- 在循环迭代之间实现上下文持久化
- 为自主工作流添加质量门禁与清理步骤

## 循环模式谱系

从最简单到最复杂：

| 模式 | 复杂度 | 最适合 |
|---------|-----------|----------|
| [顺序流水线](#1-sequential-pipeline-claude--p) | 低 | 日常开发步骤、脚本化工作流 |
| [NanoClaw REPL](#2-nanoclaw-repl) | 低 | 交互式持久会话 |
| [无限 Agentic 循环](#3-infinite-agentic-loop) | 中 | 并行内容生成、规格驱动的工作 |
| [Continuous Claude PR 循环](#4-continuous-claude-pr-loop) | 中 | 带 CI 门禁的跨多天迭代项目 |
| [De-Sloppify 模式](#5-the-de-sloppify-pattern) | 附加 | 任何实现者步骤之后的质量清理 |
| [Ralphinho / RFC 驱动 DAG](#6-ralphinho--rfc-driven-dag-orchestration) | 高 | 大型特性、带合并队列的多单元并行工作 |

---

## 1. 顺序流水线（`claude -p`）

**最简单的循环。** 把日常开发拆解为一系列非交互的 `claude -p` 调用。每次调用都是一个聚焦的步骤，配有明确的提示词。

### 核心洞见

> 如果连这样的循环你都搭不起来，那说明你在交互模式下甚至连让 LLM 修复你的代码都做不到。

`claude -p` 标志让 Claude Code 以非交互方式带提示词运行，完成后即退出。把多次调用串联起来即可构建流水线：

```bash
#!/bin/bash
# daily-dev.sh — Sequential pipeline for a feature branch

set -e

# Step 1: Implement the feature
claude -p "Read the spec in docs/auth-spec.md. Implement OAuth2 login in src/auth/. Write tests first (TDD). Do NOT create any new documentation files."

# Step 2: De-sloppify (cleanup pass)
claude -p "Review all files changed by the previous commit. Remove any unnecessary type tests, overly defensive checks, or testing of language features (e.g., testing that TypeScript generics work). Keep real business logic tests. Run the test suite after cleanup."

# Step 3: Verify
claude -p "Run the full build, lint, type check, and test suite. Fix any failures. Do not add new features."

# Step 4: Commit
claude -p "Create a conventional commit for all staged changes. Use 'feat: add OAuth2 login flow' as the message."
```

### 关键设计原则

1. **每一步相互隔离** —— 每次 `claude -p` 调用都是全新的上下文窗口，步骤之间不会出现上下文渗漏。
2. **顺序很重要** —— 步骤按序执行。每一步都建立在上一步留下的文件系统状态之上。
3. **否定式指令很危险** —— 不要说“不要测试类型系统”，而应增加一个独立的清理步骤（参见 [De-Sloppify 模式](#5-the-de-sloppify-pattern)）。
4. **退出码会传播** —— `set -e` 会在失败时中止流水线。

### 变体

**配合模型路由：**
```bash
# Research with Opus (deep reasoning)
claude -p --model opus "Analyze the codebase architecture and write a plan for adding caching..."

# Implement with Sonnet (fast, capable)
claude -p "Implement the caching layer according to the plan in docs/caching-plan.md..."

# Review with Opus (thorough)
claude -p --model opus "Review all changes for security issues, race conditions, and edge cases..."
```

**配合环境上下文：**
```bash
# Pass context via files, not prompt length
echo "Focus areas: auth module, API rate limiting" > .claude-context.md
claude -p "Read .claude-context.md for priorities. Work through them in order."
rm .claude-context.md
```

**配合 `--allowedTools` 限制：**
```bash
# Read-only analysis pass
claude -p --allowedTools "Read,Grep,Glob" "Audit this codebase for security vulnerabilities..."

# Write-only implementation pass
claude -p --allowedTools "Read,Write,Edit,Bash" "Implement the fixes from security-audit.md..."
```

---

## 2. NanoClaw REPL

**ECC 内置的持久化循环。** 一个具备会话感知能力的 REPL，同步调用 `claude -p` 并携带完整会话历史。

```bash
# Start the default session
node scripts/claw.js

# Named session with skill context
CLAW_SESSION=my-project CLAW_SKILLS=tdd-workflow,security-review node scripts/claw.js
```

### 工作原理

1. 从 `~/.claude/claw/{session}.md` 加载会话历史
2. 每条用户消息都会连同完整历史作为上下文发送给 `claude -p`
3. 响应追加写入会话文件（以 Markdown 作为数据库）
4. 会话在重启后依然保留

### 何时用 NanoClaw vs 顺序流水线

| 使用场景 | NanoClaw | 顺序流水线 |
|----------|----------|-------------------|
| 交互式探索 | 是 | 否 |
| 脚本化自动化 | 否 | 是 |
| 会话持久化 | 内置 | 手动 |
| 上下文累积 | 每轮增长 | 每步全新 |
| CI/CD 集成 | 差 | 优秀 |

完整细节参见 `/claw` 命令文档。

---

## 3. 无限 Agentic 循环

**一个双提示词系统**，编排并行子代理完成规格驱动的生成任务。由 disler 开发（credit: @disler）。

### 架构：双提示词系统

```
PROMPT 1 (Orchestrator)              PROMPT 2 (Sub-Agents)
┌─────────────────────┐             ┌──────────────────────┐
│ Parse spec file      │             │ Receive full context  │
│ Scan output dir      │  deploys   │ Read assigned number  │
│ Plan iteration       │────────────│ Follow spec exactly   │
│ Assign creative dirs │  N agents  │ Generate unique output │
│ Manage waves         │             │ Save to output dir    │
└─────────────────────┘             └──────────────────────┘
```

### 该模式

1. **规格分析** —— 编排者读取一份定义了要生成什么的规格文件（Markdown）
2. **目录侦察** —— 扫描已有输出，找出最高的迭代编号
3. **并行部署** —— 启动 N 个子代理，每个子代理获得：
   - 完整规格
   - 一个独特的创作方向
   - 一个特定的迭代编号（互不冲突）
   - 已有迭代的快照（用于保证唯一性）
4. **波次管理** —— 无限模式下，以 3-5 个 Agent 为一波持续部署，直至上下文耗尽

### 通过 Claude Code 命令实现

创建 `.claude/commands/infinite.md`：

```markdown
Parse the following arguments from $ARGUMENTS:
1. spec_file — path to the specification markdown
2. output_dir — where iterations are saved
3. count — integer 1-N or "infinite"

PHASE 1: Read and deeply understand the specification.
PHASE 2: List output_dir, find highest iteration number. Start at N+1.
PHASE 3: Plan creative directions — each agent gets a DIFFERENT theme/approach.
PHASE 4: Deploy sub-agents in parallel (Task tool). Each receives:
  - Full spec text
  - Current directory snapshot
  - Their assigned iteration number
  - Their unique creative direction
PHASE 5 (infinite mode): Loop in waves of 3-5 until context is low.
```

**调用：**
```bash
/project:infinite specs/component-spec.md src/ 5
/project:infinite specs/component-spec.md src/ infinite
```

### 批处理策略

| 数量 | 策略 |
|-------|----------|
| 1-5 | 全部 Agent 同时启动 |
| 6-20 | 每批 5 个 |
| infinite | 3-5 个一波，复杂度递进 |

### 核心洞见：通过指派保证唯一性

不要指望 Agent 自行差异化。由编排者**指派**每个 Agent 特定的创作方向和迭代编号。这可以避免并行 Agent 之间出现重复的概念。

---

## 4. Continuous Claude PR 循环

**一个生产级的 shell 脚本**，让 Claude Code 持续循环运行：创建 PR、等待 CI、并自动合并。由 AnandChowdhary 创建（credit: @AnandChowdhary）。

### 核心循环

```
┌─────────────────────────────────────────────────────┐
│  CONTINUOUS CLAUDE ITERATION                        │
│                                                     │
│  1. Create branch (continuous-claude/iteration-N)   │
│  2. Run claude -p with enhanced prompt              │
│  3. (Optional) Reviewer pass — separate claude -p   │
│  4. Commit changes (claude generates message)       │
│  5. Push + create PR (gh pr create)                 │
│  6. Wait for CI checks (poll gh pr checks)          │
│  7. CI failure? → Auto-fix pass (claude -p)         │
│  8. Merge PR (squash/merge/rebase)                  │
│  9. Return to main → repeat                         │
│                                                     │
│  Limit by: --max-runs N | --max-cost $X             │
│            --max-duration 2h | completion signal     │
└─────────────────────────────────────────────────────┘
```

### 安装

> **警告：**请先审阅代码，再从其仓库安装 continuous-claude。不要把外部脚本直接通过管道喂给 bash。

### 用法

```bash
# Basic: 10 iterations
continuous-claude --prompt "Add unit tests for all untested functions" --max-runs 10

# Cost-limited
continuous-claude --prompt "Fix all linter errors" --max-cost 5.00

# Time-boxed
continuous-claude --prompt "Improve test coverage" --max-duration 8h

# With code review pass
continuous-claude \
  --prompt "Add authentication feature" \
  --max-runs 10 \
  --review-prompt "Run npm test && npm run lint, fix any failures"

# Parallel via worktrees
continuous-claude --prompt "Add tests" --max-runs 5 --worktree tests-worker &
continuous-claude --prompt "Refactor code" --max-runs 5 --worktree refactor-worker &
wait
```

### 跨迭代上下文：SHARED_TASK_NOTES.md

关键创新点：一个 `SHARED_TASK_NOTES.md` 文件在迭代之间持久存在：

```markdown
## Progress
- [x] Added tests for auth module (iteration 1)
- [x] Fixed edge case in token refresh (iteration 2)
- [ ] Still need: rate limiting tests, error boundary tests

## Next Steps
- Focus on rate limiting module next
- The mock setup in tests/helpers.ts can be reused
```

Claude 在迭代开始时读取该文件，并在迭代结束时更新它。这在相互独立的 `claude -p` 调用之间架起了上下文桥梁。

### CI 失败恢复

当 PR 检查失败时，Continuous Claude 会自动：
1. 通过 `gh run list` 获取失败的 run ID
2. 启动一个新的 `claude -p`，附带 CI 修复上下文
3. Claude 通过 `gh run view` 查看日志、修复代码、提交并推送
4. 重新等待检查（最多 `--ci-retry-max` 次尝试）

### 完成信号

Claude 可以通过输出一句魔法短语来表示“我完成了”：

```bash
continuous-claude \
  --prompt "Fix all bugs in the issue tracker" \
  --completion-signal "CONTINUOUS_CLAUDE_PROJECT_COMPLETE" \
  --completion-threshold 3  # Stops after 3 consecutive signals
```

连续三次迭代发出完成信号即停止循环，避免在已完成的工作上浪费运行。

### 关键配置

| 标志 | 用途 |
|------|---------|
| `--max-runs N` | 成功迭代 N 次后停止 |
| `--max-cost $X` | 花费 $X 后停止 |
| `--max-duration 2h` | 经过指定时长后停止 |
| `--merge-strategy squash` | squash、merge 或 rebase |
| `--worktree <name>` | 通过 git worktree 并行执行 |
| `--disable-commits` | 试运行模式（不执行 git 操作） |
| `--review-prompt "..."` | 每次迭代附加一次审查者步骤 |
| `--ci-retry-max N` | 自动修复 CI 失败（默认：1） |

---

## 5. De-Sloppify 模式

**一个可附加到任何循环的模式。** 在每个实现者（Implementer）步骤之后，增加一个专门的清理/重构步骤。

### 问题所在

当你让 LLM 用 TDD 实现功能时，它会把“写测试”理解得过于字面：
- 验证 TypeScript 类型系统本身能正常工作的测试（测试 `typeof x === 'string'`）
- 对类型系统已经保证的事情做过度的防御性运行时检查
- 针对框架行为而非业务逻辑的测试
- 过度的错误处理，反而遮蔽了真正的代码

### 为什么不用否定式指令？

在实现者的提示词中加入“不要测试类型系统”或“不要添加不必要的检查”会产生下游影响：
- 模型会对**所有**测试变得畏手畏脚
- 它会跳过合理的边界情况测试
- 质量以不可预测的方式劣化

### 解决方案：独立的清理步骤

与其约束实现者，不如让它充分展开。然后再加一个专注清理的 Agent：

```bash
# Step 1: Implement (let it be thorough)
claude -p "Implement the feature with full TDD. Be thorough with tests."

# Step 2: De-sloppify (separate context, focused cleanup)
claude -p "Review all changes in the working tree. Remove:
- Tests that verify language/framework behavior rather than business logic
- Redundant type checks that the type system already enforces
- Over-defensive error handling for impossible states
- Console.log statements
- Commented-out code

Keep all business logic tests. Run the test suite after cleanup to ensure nothing breaks."
```

### 在循环中的运用

```bash
for feature in "${features[@]}"; do
  # Implement
  claude -p "Implement $feature with TDD."

  # De-sloppify
  claude -p "Cleanup pass: review changes, remove test/code slop, run tests."

  # Verify
  claude -p "Run build + lint + tests. Fix any failures."

  # Commit
  claude -p "Commit with message: feat: add $feature"
done
```

### 核心洞见

> 与其添加会带来下游质量影响的否定式指令，不如增加一个独立的 de-sloppify 步骤。两个各司其职的 Agent 胜过一个处处受限的 Agent。

---

## 6. Ralphinho / RFC 驱动的 DAG 编排

**最复杂的模式。** 一个 RFC 驱动的多 Agent 流水线：把规格分解为依赖 DAG，让每个单元经过分层质量流水线，再通过 Agent 驱动的合并队列落地。由 enitrat 创建（credit: @enitrat）。

### 架构总览

```
RFC/PRD Document
       │
       ▼
  DECOMPOSITION (AI)
  Break RFC into work units with dependency DAG
       │
       ▼
┌──────────────────────────────────────────────────────┐
│  RALPH LOOP (up to 3 passes)                         │
│                                                      │
│  For each DAG layer (sequential, by dependency):     │
│                                                      │
│  ┌── Quality Pipelines (parallel per unit) ───────┐  │
│  │  Each unit in its own worktree:                │  │
│  │  Research → Plan → Implement → Test → Review   │  │
│  │  (depth varies by complexity tier)             │  │
│  └────────────────────────────────────────────────┘  │
│                                                      │
│  ┌── Merge Queue ─────────────────────────────────┐  │
│  │  Rebase onto main → Run tests → Land or evict │  │
│  │  Evicted units re-enter with conflict context  │  │
│  └────────────────────────────────────────────────┘  │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### RFC 分解

AI 阅读 RFC 并产出工作单元：

```typescript
interface WorkUnit {
  id: string;              // kebab-case identifier
  name: string;            // Human-readable name
  rfcSections: string[];   // Which RFC sections this addresses
  description: string;     // Detailed description
  deps: string[];          // Dependencies (other unit IDs)
  acceptance: string[];    // Concrete acceptance criteria
  tier: "trivial" | "small" | "medium" | "large";
}
```

**分解规则：**
- 优先更少、更内聚的单元（最小化合并风险）
- 尽量减少跨单元的文件重叠（避免冲突）
- 测试与实现放在同一单元（绝不拆成“实现 X” + “测试 X”）
- 只在存在真实代码依赖时才建立依赖

依赖 DAG 决定执行顺序：
```
Layer 0: [unit-a, unit-b]     ← no deps, run in parallel
Layer 1: [unit-c]             ← depends on unit-a
Layer 2: [unit-d, unit-e]     ← depend on unit-c
```

### 复杂度分层

不同分层对应不同的流水线深度：

| 分层 | 流水线阶段 |
|------|----------------|
| **trivial** | implement → test |
| **small** | implement → test → code-review |
| **medium** | research → plan → implement → test → PRD-review + code-review → review-fix |
| **large** | research → plan → implement → test → PRD-review + code-review → review-fix → final-review |

这样既避免对简单改动动用昂贵操作，又确保架构级改动得到彻底审视。

### 独立的上下文窗口（消除作者偏误）

每个阶段都在自己的 Agent 进程中运行，拥有自己的上下文窗口：

| 阶段 | 模型 | 用途 |
|-------|-------|---------|
| Research | Sonnet | 阅读代码库 + RFC，产出上下文文档 |
| Plan | Opus | 设计实现步骤 |
| Implement | Codex | 按照计划编写代码 |
| Test | Sonnet | 运行构建 + 测试套件 |
| PRD Review | Sonnet | 规格符合性检查 |
| Code Review | Opus | 质量 + 安全检查 |
| Review Fix | Codex | 处理审查发现的问题 |
| Final Review | Opus | 质量门禁（仅 large 分层） |

**关键设计：**审查者从未写过它所审查的代码。这消除了作者偏误——自我审查中最常见的漏检根源。

### 带驱逐机制的合并队列

质量流水线完成后，各单元进入合并队列：

```
Unit branch
    │
    ├─ Rebase onto main
    │   └─ Conflict? → EVICT (capture conflict context)
    │
    ├─ Run build + tests
    │   └─ Fail? → EVICT (capture test output)
    │
    └─ Pass → Fast-forward main, push, delete branch
```

**文件重叠智能：**
- 互不重叠的单元以投机方式并行落地
- 相互重叠的单元逐个落地，每次都先 rebase

**驱逐恢复：**
被驱逐时，会捕获完整上下文（冲突文件、diff、测试输出），并在下一轮 Ralph pass 时回传给实现者：

```markdown
## MERGE CONFLICT — RESOLVE BEFORE NEXT LANDING

Your previous implementation conflicted with another unit that landed first.
Restructure your changes to avoid the conflicting files/lines below.

{full eviction context with diffs}
```

### 阶段间的数据流

```
research.contextFilePath ──────────────────→ plan
plan.implementationSteps ──────────────────→ implement
implement.{filesCreated, whatWasDone} ─────→ test, reviews
test.failingSummary ───────────────────────→ reviews, implement (next pass)
reviews.{feedback, issues} ────────────────→ review-fix → implement (next pass)
final-review.reasoning ────────────────────→ implement (next pass)
evictionContext ───────────────────────────→ implement (after merge conflict)
```

### Worktree 隔离

每个单元都在一个隔离的 worktree 中运行（使用 jj/Jujutsu，而非 git）：
```
/tmp/workflow-wt-{unit-id}/
```

同一单元的各流水线阶段**共享**同一个 worktree，从而在 research → plan → implement → test → review 之间保留状态（上下文文件、计划文件、代码改动）。

### 关键设计原则

1. **确定性执行** —— 事前分解锁定了并行性与执行顺序
2. **在杠杆点安排人工审查** —— 工作计划是杠杆率最高的单一干预点
3. **关注点分离** —— 每个阶段都在独立的上下文窗口中由独立的 Agent 负责
4. **带上下文的冲突恢复** —— 完整的驱逐上下文支持智能重跑，而非盲目重试
5. **分层决定深度** —— trivial 改动跳过 research/review；large 改动接受最严格的审视
6. **可恢复的工作流** —— 完整状态持久化到 SQLite；可从任意节点恢复

### 何时用 Ralphinho vs 更简单的模式

| 信号 | 用 Ralphinho | 用更简单的模式 |
|--------|--------------|-------------------|
| 多个相互依赖的工作单元 | 是 | 否 |
| 需要并行实现 | 是 | 否 |
| 合并冲突概率高 | 是 | 否（顺序执行即可） |
| 单文件改动 | 否 | 是（顺序流水线） |
| 跨多天的项目 | 是 | 也许（continuous-claude） |
| 规格/RFC 已写好 | 是 | 也许 |
| 对一件事快速迭代 | 否 | 是（NanoClaw 或流水线） |

---

## 选择合适的模式

### 决策矩阵

```
Is the task a single focused change?
├─ Yes → Sequential Pipeline or NanoClaw
└─ No → Is there a written spec/RFC?
         ├─ Yes → Do you need parallel implementation?
         │        ├─ Yes → Ralphinho (DAG orchestration)
         │        └─ No → Continuous Claude (iterative PR loop)
         └─ No → Do you need many variations of the same thing?
                  ├─ Yes → Infinite Agentic Loop (spec-driven generation)
                  └─ No → Sequential Pipeline with de-sloppify
```

### 组合各模式

这些模式可以很好地组合：

1. **顺序流水线 + De-Sloppify** —— 最常见的组合。每个实现步骤都配一次清理步骤。

2. **Continuous Claude + De-Sloppify** —— 为每次迭代附加一条带 de-sloppify 指令的 `--review-prompt`。

3. **任意循环 + 验证** —— 在提交前用 ECC 的 `/verify` 命令或 `verification-loop` Skill 作为门禁。

4. **在更简单的循环中运用 Ralphinho 的分层思路** —— 即使在顺序流水线里，也可以把简单任务路由给 Haiku、复杂任务路由给 Opus：
   ```bash
   # Simple formatting fix
   claude -p --model haiku "Fix the import ordering in src/utils.ts"

   # Complex architectural change
   claude -p --model opus "Refactor the auth module to use the strategy pattern"
   ```

---

## 反模式

### 常见错误

1. **没有退出条件的无限循环** —— 务必设置 max-runs、max-cost、max-duration 或完成信号之一。

2. **迭代之间没有上下文桥梁** —— 每次 `claude -p` 调用都是从零开始。用 `SHARED_TASK_NOTES.md` 或文件系统状态来衔接上下文。

3. **原样重试同一失败** —— 某次迭代失败时，不要只是重试。要捕获错误上下文并喂给下一次尝试。

4. **用否定式指令代替清理步骤** —— 不要说“不要做 X”，而是增加一个专门移除 X 的步骤。

5. **所有 Agent 挤在一个上下文窗口里** —— 对复杂工作流，应把关注点拆分到不同的 Agent 进程。审查者绝不应是作者本人。

6. **并行工作时无视文件重叠** —— 如果两个并行 Agent 可能编辑同一文件，就需要合并策略（顺序落地、rebase 或冲突解决）。

---

## 参考资料

| 项目 | 作者 | 链接 |
|---------|--------|------|
| Ralphinho | enitrat | credit: @enitrat |
| Infinite Agentic Loop | disler | credit: @disler |
| Continuous Claude | AnandChowdhary | credit: @AnandChowdhary |
| NanoClaw | ECC | 本仓库中的 `/claw` 命令 |
| Verification Loop | ECC | 本仓库中的 `skills/verification-loop/` |
