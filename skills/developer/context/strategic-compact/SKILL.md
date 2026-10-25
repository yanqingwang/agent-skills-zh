---
name: strategic-compact
description: 在工作流中的逻辑节点建议手动 compact（上下文压缩），以在任务阶段之间保留上下文，而非依赖任意的自动压缩（auto-compaction）。当会话接近上下文上限、且当前任务阶段正是适合压缩的天然节点时使用。
metadata:
  origin: ECC
---

> **中文汉化版** · 上游：[affaan-m/ECC](https://github.com/affaan-m/ECC) · 原文件：`skills/strategic-compact/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 策略性 Compact Skill

在工作流中的战略节点建议手动执行 `/compact`，而不是依赖任意的自动压缩（auto-compaction）。

## 何时激活

- 运行接近上下文上限（200K+ token）的长会话
- 处理多阶段任务（研究 → 计划 → 实现 → 测试）
- 在同一会话内切换到不相关的任务
- 完成一个重要里程碑并开始新工作之后
- 当响应变慢或连贯性下降时（上下文压力）

## 为什么需要策略性压缩？

自动压缩的触发点是任意的：
- 常常在任务中途触发，丢失重要上下文
- 对逻辑上的任务边界没有感知
- 可能打断复杂的多步操作

在逻辑边界进行策略性压缩：
- **探索之后、执行之前** — 压缩研究类上下文，保留实现计划
- **完成一个里程碑之后** — 为下一阶段开启全新起点
- **重大上下文切换之前** — 在开始不同任务前清掉探索性上下文

## 工作原理

`suggest-compact.js` 脚本挂在 PreToolUse（Edit/Write）上运行，结合两个信号：

1. **上下文大小（主要信号）** — 从会话转录（hook 载荷中的 `transcript_path`）读取最新的 `usage` 记录，并将 `input_tokens + cache_read_input_tokens + cache_creation_input_tokens` 求和（即该轮真实的上下文大小）。在一个按窗口大小缩放的阈值处建议 `/compact` ， 200k 窗口对应 160k token，1M 窗口对应 250k（通过模型 id 中的 `[1m]` 标记检测窗口大小，或在观测到的 token 已超过 200k 时推断）， 并且此后每增长 60k token 就再次提醒
2. **工具调用次数（次要信号）** — 统计会话中的工具调用次数；达到可配置阈值（默认：50 次）时建议压缩，此后每 25 次再提醒

仅靠工具调用次数是窗口压力的弱代理：几次大的文件读取或 MCP 响应就能在极少的调用次数内填满窗口，而大量微小的调用即使窗口接近全空也可能超过 50 次。上下文大小信号只在真正要紧的时候触发。

## Hook 配置

**以插件方式安装的？** 无需任何配置。插件的 `hooks/hooks.json` 已经注册了 `suggest-compact.js`（hook id 为 `pre:edit-write:suggest-compact`，在 `standard` 与 `strict` 两种 hook profile 中启用）。不要把下面的代码块复制进 `~/.claude/settings.json` ， 插件安装方式下 `~/.claude/scripts/` 并不存在，而且重复注册插件 Hook 会导致双重执行。

**如果是手动安装**（`./install.sh`），请在 `~/.claude/settings.json` 中加入：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [{ "type": "command", "command": "node ~/.claude/scripts/hooks/suggest-compact.js" }]
      },
      {
        "matcher": "Write",
        "hooks": [{ "type": "command", "command": "node ~/.claude/scripts/hooks/suggest-compact.js" }]
      }
    ]
  }
}
```

## 配置

环境变量：
- `COMPACT_THRESHOLD` — 首次建议前的工具调用次数（默认：50）
- `COMPACT_CONTEXT_THRESHOLD` — 触发上下文大小建议前的上下文 token 数（默认：200k 窗口为 160000，1M 窗口为 250000；设为 `0` 可禁用上下文信号）
- `COMPACT_CONTEXT_INTERVAL` — 建议重复触发前所需的额外上下文 token 数（默认：60000）
- `COMPACT_STATE_TTL_DAYS` — 临时目录中过期的每会话状态文件被清扫前的保留天数（默认：14）
- `ECC_CONTEXT_WINDOW_TOKENS` — 显式指定上下文窗口大小（单位 token），覆盖自动检测。对于报告的模型 id 不带 `[1m]` 标记的大窗口模型（例如 400k 的 Opus 4.x，或新的 1M 窗口模型家族），请设置此项，使阈值按真实窗口缩放，而不是按默认 200k 处理从而高估上下文占用。
- `CLAUDE_CODE_AUTO_COMPACT_WINDOW` — Claude Code 原生的窗口大小覆盖值（单位 token）；在 `ECC_CONTEXT_WINDOW_TOKENS` 未设置时作为后备被采纳。

> 在其他情况下，上下文窗口通过模型 id 中的 `[1m]` 标记自动检测，或在观测到的 token 已超过 200k 时推断。如果大窗口模型两个信号都不具备，请设置上述某个覆盖项，让 `/compact` 建议在正确的时机触发。

## 压缩决策指南

用这张表来决定何时压缩：

| 阶段转换 | 是否压缩？ | 原因 |
|-----------------|----------|-----|
| 研究 → 计划 | 是 | 研究上下文很庞大；计划才是蒸馏后的产出 |
| 计划 → 实现 | 是 | 计划已经写下来了（写入文件，或写入任务清单，如果你有的话）；把上下文腾给代码 |
| 实现 → 测试 | 视情况 | 如果测试引用了近期代码就保留；如果切换关注点就压缩 |
| 调试 → 下一个功能 | 是 | 调试痕迹会污染与后续工作无关的上下文 |
| 实现中途 | 否 | 丢失变量名、文件路径和部分完成的状态代价很高 |
| 某种方案失败之后 | 是 | 在尝试新方案之前清掉死胡同里的推理 |

## 压缩后什么会保留下来

理解什么能持久存留，能让你放心地压缩：

| 会保留 | 会丢失 |
|----------|------|
| CLAUDE.md 指令 | 中间推理与分析 |
| 磁盘上的文件 | 你之前读过的文件内容 |
| 记忆文件（`~/.claude/memory/`） | 多轮对话上下文 |
| Git 状态（commit、分支） | 工具调用历史与计数 |
| 任务清单 — **仅当你拥有 todo 工具时**（见下文） | 口头表述的微妙用户偏好 |

> ### 不要指望任务清单能在压缩后幸存，它可能根本不存在
>
> Claude Code **2.1.233 在 Opus 4.8、Sonnet 5、Fable 5、Mythos 5 及更新模型上默认移除了
> todo/task 工具**（`TodoWrite`、`TaskCreate/Get/Update/List`）。
> `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` 可以把它们找回来，但那是每台机器的环境设置 ，
> **它不会随这个 Skill 一起带过去**，所以你不能假定读者已经配置了它。
>
> 这一点很重要，因为"我的 todo 清单能在压缩后幸存"正是人们用压缩 *代替* 把状态
> 写下来的理由。如果工具不存在，就没有清单可言，计划就直接没了。**压缩前先把计划
> 写进文件** ， 文件在任何版本、任何模型上都能持久存留。把任务清单当作可能缺席的
> 便利品，永远不要把它当作你的持久记录。

## 最佳实践

1. **计划完成后压缩** — 一旦计划敲定 **并写入文件**，就压缩以全新开始
2. **调试结束后压缩** — 在继续之前清掉错误排查上下文
3. **不要在实现中途压缩** — 为相关的改动保留上下文
4. **认真读建议** — Hook 告诉你 *何时*，由你决定 *是否*
5. **压缩前先写下来** — 压缩前把重要上下文保存到文件或记忆中
6. **带摘要使用 `/compact`** — 附上一条自定义消息：`/compact Focus on implementing auth middleware next`

## Token 优化模式

### 触发表惰性加载
不要在会话开始时加载完整的 Skill 内容，而是使用把关键词映射到 Skill 路径的触发表。Skill 只在被触发时加载，可将基线上下文降低 50% 以上：

| 触发词 | Skill | 何时加载 |
|---------|-------|-----------|
| "test", "tdd", "coverage" | tdd-workflow | 用户提到测试 |
| "security", "auth", "xss" | security-review | 安全相关工作 |
| "deploy", "ci/cd" | deployment-patterns | 部署场景 |

### 上下文构成意识
监控是什么在消耗你的上下文窗口：
- **CLAUDE.md 文件** — 始终加载，保持精简
- **已加载的 Skill** — 每个 Skill 增加 1-5K token
- **对话历史** — 随每次交互增长
- **工具结果** — 文件读取、搜索结果都会增加体量

### 重复指令检测
常见的重复上下文来源：
- `~/.claude/rules/` 与项目 `.claude/rules/` 中存在相同的规则
- 重复 CLAUDE.md 指令的 Skill
- 多个 Skill 覆盖相互重叠的领域

### 上下文优化工具
- `token-optimizer` MCP — 通过内容去重实现 95% 以上的 token 自动削减
- `context-mode` — 上下文虚拟化（演示中从 315KB 降到 5.4KB）

## 相关资源

- [The Longform Guide](https://x.com/affaanmustafa/status/2014040193557471352) — Token 优化章节
- Memory persistence hooks — 用于在压缩后幸存的状态
- `continuous-learning` skill — 在会话结束前提取模式
