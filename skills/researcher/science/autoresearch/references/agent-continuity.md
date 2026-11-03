> **中文汉化版** · 上游：[Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) · 原文件：`0-autoresearch-skill/references/agent-continuity.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Agent 续跑：让研究持续运转

自主研究要求 Agent 能持续工作 — 数小时、整夜，甚至数天。本参考说明如何在各平台上搭建墙钟循环。

## 强制：先于一切完成设置

启动 autoresearch 时，墙钟循环是你要做的第一件事。没有它，agent 干完一个周期就停。这个循环每 20 分钟触发一次，只是告诉 agent：“继续工作，检查有没有出什么问题。”

它与研究的内/外循环完全无关。墙钟循环是固定间隔的提示词注入。研究循环按实验节奏运行（每个周期从几分钟到几小时）。两者不会同步，也不需要同步。

## Claude Code：/loop

**把下面这条作为你的第一个动作执行：**

```
/loop 20m Continue autoresearch. Read research-state.yaml and findings.md. Check: is the current experiment done? Are there errors? Is progress stalling? If everything is on track, keep working. If something is wrong, step back and fix it. Never idle.
```

### 每次 tick 会发生什么

`/loop` 消息每 20 分钟触发一次。触发时：

1. **读取状态** — 读 `research-state.yaml` 与 `findings.md`，记住自己在哪里、已经学到什么
2. **检查健康度** — 当前实验在跑吗？报错了？训练在发散吗？
3. **若一切正常** → 继续手头的事（不要重启，也不要重新规划）
4. **若卡住或出错** → 退一步，诊断问题，修好，然后继续
5. **若闲着** → 不该如此。挑下一个假设，开一个实验

tick 是一次推动，不是一个阶段边界。如果上一个 tick 的活还没干完，就接着干。

### 当实验跑超过 20 分钟

这很正常，也在意料之中。下一次 tick 时：
- 检查实验是否已经结束
- 如果还在跑：监控报错，做些轻量工作（更新笔记、检索论文）
- 不要重启，也不要重复这个实验

### 上下文恢复

两次 tick 之间，你的主要记忆是 `research-state.yaml` 与 `findings.md`。每次实验与反思之后都要更新它们。如果上下文丢了，读这两个文件加上 `research-log.md`，重建自己所处的位置。

## OpenClaw：Cron 任务

**把下面这条作为你的第一个动作，在当前会话中设置一个 20 分钟的 cron 任务。** 用 `cron.add` 工具创建一个绑定到当前聊天会话的周期性任务：

```json
{
  "name": "autoresearch-loop",
  "schedule": { "kind": "every", "everyMs": 1200000 },
  "sessionTarget": "current",
  "payload": {
    "kind": "agentTurn",
    "message": "Continue autoresearch. Read research-state.yaml and findings.md. Check: is the current experiment done? Are there errors? Is progress stalling? If everything is on track, keep working. If something is wrong, step back and fix it. Never idle."
  }
}
```

关键细节：
- `sessionTarget: "current"` 把 cron 绑定到当前聊天会话（创建时解析为 `session:<sessionKey>`），因此它能在各次 tick 之间保持对话上下文
- `everyMs: 1200000` = 20 分钟
- 用 `cron.list` 确认任务已创建并处于启用状态
- 之后要查运行历史：用 `cron.runs` 加上任务 ID

### 两次 Cron Tick 之间的上下文

OpenClaw 的 cron 调用每次都可能是全新启动。你的工作区文件就是你的记忆：

- `research-state.yaml` — 你在哪里，什么在推进
- `findings.md` — 你学到了什么（每次都要读！）
- `research-log.md` — 按时间顺序发生了什么

每次动作之后都更新它们，好让下一次 cron tick 能无缝接手。

### 进度报告

OpenClaw 不像 Claude Code 那样能在本地 `open` HTML 文件。有东西要报告时：

1. 生成一份 PDF 进度摘要（用 Python 加 reportlab、matplotlib 或类似工具）
2. 包含：研究问题、关键结果、优化轨迹图、当前理解、下一步
3. 通过 Telegram、WhatsApp 或 Slack 发给用户 — 看他用哪个渠道
4. 拿到令人兴奋的结果或有意思的图时立刻发 — 不要等完整报告

## 以研究状态为事实基准

两个平台共享同一个事实基准：工作区文件。

| 文件 | 用途 | 更新频率 |
|---|---|---|
| `research-state.yaml` | 机器可读的状态 | 每次实验与反思之后 |
| `research-log.md` | 决策时间线 | 每次重要动作之后 |
| `findings.md` | 叙述性理解 + 项目记忆 | 每次外循环之后 |
| `experiments/*/results/` | 原始实验数据 | 每次实验之后 |

墙钟循环（`/loop` 或 cron）只是触发器。工作区文件才是记忆。保持它们是最新的。
