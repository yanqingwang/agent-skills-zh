---
name: task-coordination-strategies
description: 分解复杂任务、设计依赖图，并以规范的任务描述与负载均衡协调多 Agent 协作。在为 Agent 团队拆分工作、管理任务依赖或监控团队进度时使用此 Skill。
version: 1.0.2
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/agent-teams/skills/task-coordination-strategies/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 任务协调策略

将复杂任务分解为可并行执行的单元、设计依赖图、撰写高效的任务描述，以及监控 Agent 团队间负载的策略集合。

## 何时使用此 Skill

- 将复杂任务拆分以便并行执行
- 设计任务依赖关系（blockedBy/blocks）
- 撰写带有清晰验收标准的任务描述
- 监控并重新均衡各 teammates 之间的负载
- 识别多任务工作流中的关键路径

## 任务分解策略

### 按架构层

按架构层拆分工作：

- 前端组件
- 后端 API 端点
- 数据库迁移/模型
- 测试套件

**最适合**：全栈功能、垂直切片

### 按组件

按功能组件拆分工作：

- 认证模块
- 用户资料模块
- 通知模块

**最适合**：微服务、模块化架构

### 按关注点

按横切关注点拆分工作：

- 安全审查
- 性能审查
- 架构审查

**最适合**：代码审查、审计

### 按文件归属

按文件/目录边界拆分工作：

- `src/components/` — 实现者 1
- `src/api/` — 实现者 2
- `src/utils/` — 实现者 3

**最适合**：并行实现、避免冲突

## 依赖图设计

### 原则

1. **最小化链深度** — 优先选择宽而浅的依赖图，而非深链
2. **识别关键路径** — 最长的链决定了最短完成时间
3. **节制使用 blockedBy** — 只添加真正必要的依赖
4. **避免循环依赖** — 任务 A 阻塞 B、B 又阻塞 A 就是死锁

### 模式

**独立型（并行度最佳）**：

```
Task A ─┐
Task B ─┼─→ Integration
Task C ─┘
```

**顺序型（必要的依赖）**：

```
Task A → Task B → Task C
```

**菱形（混合）**：

```
        ┌→ Task B ─┐
Task A ─┤          ├→ Task D
        └→ Task C ─┘
```

### 使用 blockedBy/blocks

```
TaskCreate: { subject: "Build API endpoints" }         → Task #1
TaskCreate: { subject: "Build frontend components" }    → Task #2
TaskCreate: { subject: "Integration testing" }          → Task #3
TaskUpdate: { taskId: "3", addBlockedBy: ["1", "2"] }  → #3 waits for #1 and #2
```

## 任务描述最佳实践

每个任务都应包含：

1. **目标** — 需要完成什么（1-2 句话）
2. **所属文件** — 该 teammate 可修改的文件/目录的明确清单
3. **需求** — 预期的具体交付物或行为
4. **接口契约** — 这份工作如何与他人的工作衔接
5. **验收标准** — 如何验证任务已正确完成
6. **范围边界** — 明确不在范围内的内容

### 模板

```
## Objective
Build the user authentication API endpoints.

## Owned Files
- src/api/auth.ts
- src/api/middleware/auth-middleware.ts
- src/types/auth.ts (shared — read only, do not modify)

## Requirements
- POST /api/login — accepts email/password, returns JWT
- POST /api/register — creates new user, returns JWT
- GET /api/me — returns current user profile (requires auth)

## Interface Contract
- Import User type from src/types/auth.ts (owned by implementer-1)
- Export AuthResponse type for frontend consumption

## Acceptance Criteria
- All endpoints return proper HTTP status codes
- JWT tokens expire after 24 hours
- Passwords are hashed with bcrypt

## Out of Scope
- OAuth/social login
- Password reset flow
- Rate limiting
```

## 负载监控

### 负载失衡的信号

| 信号                     | 含义             | 行动                      |
| ------------------------ | ---------------- | ------------------------- |
| 某 teammate 空闲，他人在忙 | 分配不均         | 重新分配待办任务      |
| 某 teammate 卡在一个任务上 | 可能存在阻塞     | 主动询问，提供帮助        |
| 所有任务都被阻塞         | 依赖问题         | 优先解决关键路径 |
| 某 teammate 的任务是他人 3 倍 | 负载过重         | 拆分任务或重新分配     |

### 重新均衡的步骤

1. 调用 `TaskList` 评估当前状态
2. 找出空闲或负载过重的 teammates
3. 使用 `TaskUpdate` 重新分配任务
4. 使用 `SendMessage` 通知受影响的 teammates
5. 持续观察吞吐量是否改善
