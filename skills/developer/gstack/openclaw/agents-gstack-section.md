> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/openclaw/agents-gstack-section.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 编码任务（gstack）

### 规则（不可协商）

1. **总是 spawn，绝不转介。** 当用户要求使用任何 gstack skill 时，
   总是通过 sessions_spawn 拉起一个 Claude Code 会话。绝不让用户自己去
   打开 Claude Code。绝不说"这需要在 Claude Code 里运行"。
   绝不说"那你需要打开 Claude Code"。直接去做。

2. **解析仓库。** 如果用户点名了某个 repo 或项目，把工作目录设为该 repo
   路径。如果不知道 repo 路径，询问是哪个 repo：不要拿"让用户自己打开
   Claude Code"来搪塞。

3. **Autoplan 端到端跑完。** 对 /autoplan 尤其如此：spawn 会话，
   让它跑完整个评审管线（CEO → design → eng），结束后把计划汇报回聊天。
   把计划写入 memory，方便用户日后查找。用户绝不应该需要离开 Telegram。

### 派发路由

被要求做编码工作时，选择派发档位：

**SIMPLE:** "改个错别字"、"更新那个 config"、单文件改动
→ sessions_spawn(runtime: "acp", prompt: "<just the task>")

**MEDIUM:** 多文件功能、重构、skill 编辑
→ sessions_spawn(runtime: "acp", prompt: "<gstack-lite content>\n\n<task>")

**HEAVY:** 需要特定 gstack 方法论
→ sessions_spawn(runtime: "acp", prompt: "Load gstack. Run /qa https://...")
  Skills: /cso, /review, /qa, /ship, /design-review, /benchmark, /gstack-upgrade

**FULL:** 构建完整功能、多日规模、需要计划 + 评审
→ sessions_spawn(runtime: "acp", prompt: "<gstack-full content>\n\n<task>")
  Claude Code runs: /autoplan → implement → /ship → report back

**PLAN:** 用户想为 Claude Code 项目做计划、把一个功能写成 spec，或在写任何代码之前先做设计
→ sessions_spawn(runtime: "acp", prompt: "<gstack-plan content>\n\n<task>")
  Claude Code runs: /office-hours → /autoplan → saves plan file → reports back
  把计划链接持久化到 memory/knowledge store。
  用户准备实现时，spawn 一个新的 FULL 会话并指向该计划。

### 决策启发

- 10 行以内代码能完成吗？→ **SIMPLE**
- 涉及多个文件但方法显而易见？→ **MEDIUM**
- 用户点名了具体 skill（/cso、/review、/qa）？→ **HEAVY**
- "Upgrade gstack"、"update gstack" → **HEAVY**，带 `Run /gstack-upgrade`
- 是功能、项目或目标（而非任务）？→ **FULL**
- 用户想先 PLAN 而暂不实现？→ **PLAN**
