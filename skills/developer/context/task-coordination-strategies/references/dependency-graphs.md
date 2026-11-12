> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/agent-teams/skills/task-coordination-strategies/references/dependency-graphs.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 依赖图模式

任务依赖设计的可视化模式，附各自的取舍。

## 模式 1：完全独立（并行度最大）

```
Task A ─┐
Task B ─┼─→ Final Integration
Task C ─┘
```

- **并行度**：最大，所有任务同时运行
- **风险**：集成时才可能暴露不兼容问题
- **适用场景**：各任务操作的文件/模块完全分离
- **TaskCreate**：不设 blockedBy 关系；集成任务被所有任务阻塞

## 模式 2：顺序链（无并行）

```
Task A → Task B → Task C → Task D
```

- **并行度**：无，每个任务都要等前一个
- **风险**：每一步都是瓶颈，一处延迟层层传导
- **适用场景**：每个任务依赖前一个任务的输出（尽量避开）
- **TaskCreate**：每个任务 blockedBy 前一个任务

## 模式 3：菱形（共享基础）

```
           ┌→ Task B ─┐
Task A ──→ ┤          ├→ Task D
           └→ Task C ─┘
```

- **并行度**：A 完成后，B 和 C 并行执行
- **风险**：A 是瓶颈；D 必须等 B 和 C 都完成
- **适用场景**：B 和 C 都需要 A 的输出（如共享类型）
- **TaskCreate**：B 和 C blockedBy A；D blockedBy B 和 C

## 模式 4：Fork-Join（分阶段并行）

```
Phase 1:  A1, A2, A3  (parallel)
          ────────────
Phase 2:  B1, B2      (parallel, after phase 1)
          ────────────
Phase 3:  C1          (after phase 2)
```

- **并行度**：阶段内部任务并行
- **风险**：阶段边界带来同步等待
- **适用场景**：存在天然的阶段和依赖（构建 → 测试 → 部署）
- **TaskCreate**：阶段 2 的任务 blockedBy 阶段 1 的全部任务

## 模式 5：流水线（流式）

```
Task A ──→ Task B ──→ Task C
  └──→ Task D ──→ Task E
```

- **并行度**：两条并行链
- **风险**：两条链的实现思路可能分叉
- **适用场景**：从共同起点出发的两个独立功能分支
- **TaskCreate**：B blockedBy A；D blockedBy A；C blockedBy B；E blockedBy D

## 反模式

### 循环依赖（死锁）

```
Task A → Task B → Task C → Task A  ✗ DEADLOCK
```

**修复**：把共享依赖提取成一个独立任务，让三个任务都依赖它。

### 不必要的依赖

```
Task A → Task B → Task C
(where B doesn't actually need A's output)
```

**修复**：删除 blockedBy 关系，让 B 独立运行。

### 星型模式（单点瓶颈）

```
     ┌→ B
A →  ├→ C  → F
     ├→ D
     └→ E
```

**修复**：如果 A 很慢，所有下游任务都会被拖延。尽量把 A 的工作并行化。
