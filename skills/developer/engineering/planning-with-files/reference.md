> **中文汉化版** · 上游：[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) · 原文件：`.agents/skills/planning-with-files/reference.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 参考：Manus 上下文工程原则

本 Skill 基于 Manus 的上下文工程原则。Manus 是一家 AI Agent 公司，2025 年 12 月被 Meta 以 20 亿美元收购。

## Manus 的 6 条原则

### 原则 1：围绕 KV-Cache 设计

> "KV-cache 命中率是生产级 AI Agent 唯一最重要的指标。"

**统计数据：**
- 输入与输出 token 比例约为 100:1
- 缓存命中 token：$0.30/MTok，未缓存：$3/MTok
- 成本相差 10 倍！

**实现要点：**
- 保持提示词前缀稳定（STABLE），改动一个 token 就会使缓存失效
- 系统提示词中不要放时间戳
- 让上下文只追加（APPEND-ONLY），并使用确定性序列化

### 原则 2：掩蔽，而非移除

不要动态移除工具（会破坏 KV-cache），改用 logit 掩蔽。

**最佳实践：** 使用一致的动作前缀（例如 `browser_`、`shell_`、`file_`），便于掩蔽。

### 原则 3：文件系统即外部记忆

> "Markdown 就是我在磁盘上的'工作记忆'。"

**公式：**
```
Context Window = RAM (volatile, limited)
Filesystem = Disk (persistent, unlimited)
```

**压缩必须可还原：**
- 即使丢弃网页内容，也要保留 URL
- 即使丢弃文档内容，也要保留文件路径
- 永远不要丢失指向完整数据的指针

### 原则 4：通过背诵（Recitation）操纵注意力

> "在整个任务过程中创建并更新 todo.md，把全局计划推到模型的近期注意力范围内。"

**问题：** 约 50 次工具调用之后，模型会忘记最初目标（"lost in the middle"效应）。

**解法：** 每次决策前重读 `task_plan.md`，目标就会出现在注意力窗口中。

```
Start of context: [Original goal - far away, forgotten]
...many tool calls...
End of context: [Recently read task_plan.md - gets ATTENTION!]
```

### 原则 5：把错误内容留在上下文中

> "把走错的弯路留在上下文里。"

**原因：**
- 带堆栈跟踪的失败动作能让模型隐式更新自己的信念
- 减少重复犯错
- 错误恢复是"真正 agentic 行为最清晰的信号之一"

### 原则 6：不要被 Few-Shot 带偏

> "千篇一律滋生脆弱。"

**问题：** 重复的"动作-观察"对会导致漂移与幻觉。

**解法：** 引入受控的变化：
- 措辞稍有变化
- 不要盲目复制粘贴既有模式
- 在重复性任务上重新校准

---

## 3 条上下文工程策略

基于 Lance Martin 对 Manus 架构的分析。

### 策略 1：上下文缩减

**压缩（Compaction）：**
```
Tool calls have TWO representations:
├── FULL: Raw tool content (stored in filesystem)
└── COMPACT: Reference/file path only

RULES:
- Apply compaction to STALE (older) tool results
- Keep RECENT results FULL (to guide next decision)
```

**摘要化（Summarization）：**
- 当压缩的收益递减时应用
- 使用完整工具结果生成
- 生成标准化的摘要对象

### 策略 2：上下文隔离（多 Agent）

**架构：**
```
┌─────────────────────────────────┐
│         PLANNER AGENT           │
│  └─ Assigns tasks to sub-agents │
├─────────────────────────────────┤
│       KNOWLEDGE MANAGER         │
│  └─ Reviews conversations       │
│  └─ Determines filesystem store │
├─────────────────────────────────┤
│      EXECUTOR SUB-AGENTS        │
│  └─ Perform assigned tasks      │
│  └─ Have own context windows    │
└─────────────────────────────────┘
```

**关键洞察：** Manus 最初用 `todo.md` 做任务规划，后来发现约 33% 的动作都花在更新它上，于是改为由专职的规划 Agent 调用执行子代理。

### 策略 3：上下文卸载

**工具设计：**
- 原子函数总数少于 20 个
- 把完整结果存进文件系统，而不是上下文
- 用 `glob` 和 `grep` 进行搜索
- 渐进式披露：只在需要时才加载信息

---

## Agent 循环

Manus 在一个连续的 7 步循环中运行：

```
┌─────────────────────────────────────────┐
│  1. ANALYZE CONTEXT                      │
│     - Understand user intent             │
│     - Assess current state               │
│     - Review recent observations         │
├─────────────────────────────────────────┤
│  2. THINK                                │
│     - Should I update the plan?          │
│     - What's the next logical action?    │
│     - Are there blockers?                │
├─────────────────────────────────────────┤
│  3. SELECT TOOL                          │
│     - Choose ONE tool                    │
│     - Ensure parameters available        │
├─────────────────────────────────────────┤
│  4. EXECUTE ACTION                       │
│     - Tool runs in sandbox               │
├─────────────────────────────────────────┤
│  5. RECEIVE OBSERVATION                  │
│     - Result appended to context         │
├─────────────────────────────────────────┤
│  6. ITERATE                              │
│     - Return to step 1                   │
│     - Continue until complete            │
├─────────────────────────────────────────┤
│  7. DELIVER OUTCOME                      │
│     - Send results to user               │
│     - Attach all relevant files          │
└─────────────────────────────────────────┘
```

---

## Manus 创建的文件类型

| 文件 | 用途 | 何时创建 | 何时更新 |
|------|---------|--------------|--------------|
| `task_plan.md` | 阶段跟踪、进度 | 任务开始时 | 完成阶段后 |
| `findings.md` | 发现与决策 | 任何一次发现之后 | 查看图片/PDF 之后 |
| `progress.md` | 会话日志、已完成内容 | 在检查点处 | 贯穿整个会话 |
| 代码文件 | 实现 | 执行之前 | 出错之后 |

---

## 关键约束

- **单动作执行（Single-Action Execution，Manus 2025 年的原始约束）：** 每轮只做一次工具调用，不并行执行。这记录的是 Manus 2025 年的沙箱实践。**2026 年更新：** 现代宿主（Claude Code、Codex CLI）已支持并行工具调用与子代理，这条约束不再按字面成立。协调点在于计划文件本身，而不是"每轮一次调用"的规则：并行调用与子代理通过磁盘上持久的 markdown 计划共享状态。
- **必须有计划：** Agent 必须始终清楚：目标、当前阶段、剩余阶段
- **文件即记忆：** 上下文是易失的。文件系统是持久的。
- **绝不重复失败：** 如果某个动作失败了，下一个动作必须不同
- **沟通即工具：** 消息类型：`info`（进度）、`ask`（阻塞）、`result`（终结）

---

## Manus 数据统计

| 指标 | 数值 |
|--------|-------|
| 每个任务的平均工具调用次数 | ~50 |
| 输入与输出 token 比例 | 100:1 |
| 收购价格 | 20 亿美元 |
| 达到 1 亿美元营收所用时间 | 8 个月 |
| 自发布以来的框架重构次数 | 5 次 |

---

## 关键语录

> "context window = RAM（易失、有限）。文件系统 = 磁盘（持久、无限）。任何重要的东西都会写入磁盘。"

> "if action_failed: next_action != same_action. 记录你尝试过什么。改变方法。"

> "错误恢复是真正 agentic 行为最清晰的信号之一。"

> "KV-cache 命中率是生产阶段 AI Agent 唯一最重要的指标。"

> "把走错的弯路留在上下文里。"

---

## 来源

基于 Manus 官方上下文工程文档：
https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
