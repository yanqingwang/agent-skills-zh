> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/agent-teams/skills/task-coordination-strategies/references/task-decomposition.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 任务分解示例

把功能分解为可并行执行、归属清晰的任务的实战示例。

## 示例 1：用户认证功能

### 功能描述

添加邮箱/密码认证，包含登录、注册和个人资料页面。

### 分解方式（垂直切片）

**任务流 1：登录流程**（实现者 1）

- 所属文件：`src/pages/login.tsx`、`src/api/login.ts`、`tests/login.test.ts`
- 需求：登录表单、API 端点、输入校验、错误处理
- 接口：从 `src/types/auth.ts` 导入 `AuthResponse`

**任务流 2：注册流程**（实现者 2）

- 所属文件：`src/pages/register.tsx`、`src/api/register.ts`、`tests/register.test.ts`
- 需求：注册表单、API 端点、邮箱校验、密码强度
- 接口：从 `src/types/auth.ts` 导入 `AuthResponse`

**任务流 3：共享基础设施**（实现者 3）

- 所属文件：`src/types/auth.ts`、`src/middleware/auth.ts`、`src/utils/jwt.ts`
- 需求：类型定义、JWT 中间件、token 工具函数
- 依赖：无（其他任务流都依赖它）

### 依赖图

```
Stream 3 (types/middleware) ──→ Stream 1 (login)
                             └→ Stream 2 (registration)
```

## 示例 2：REST API 端点

### 功能描述

为新的 "Projects" 资源添加 CRUD 端点。

### 分解方式（按层）

**任务流 1：数据层**（实现者 1）

- 所属文件：`src/models/project.ts`、`src/migrations/add-projects.ts`、`src/repositories/project-repo.ts`
- 需求：Schema 定义、迁移、Repository 模式
- 依赖：无

**任务流 2：业务逻辑**（实现者 2）

- 所属文件：`src/services/project-service.ts`、`src/validators/project-validator.ts`
- 需求：CRUD 操作、校验规则、业务逻辑
- 依赖：被任务流 1 阻塞（需要模型/Repository）

**任务流 3：API 层**（实现者 3）

- 所属文件：`src/routes/projects.ts`、`src/controllers/project-controller.ts`
- 需求：REST 端点、请求解析、响应格式化
- 依赖：被任务流 2 阻塞（需要服务层）

## 任务模板

```markdown
## Task: {Stream Name}

### Objective

{1-2 sentence description of what to build}

### Owned Files

- {file1} — {purpose}
- {file2} — {purpose}

### Requirements

1. {Specific deliverable 1}
2. {Specific deliverable 2}
3. {Specific deliverable 3}

### Interface Contract

- Exports: {types/functions this stream provides}
- Imports: {types/functions this stream consumes from other streams}

### Acceptance Criteria

- [ ] {Verifiable criterion 1}
- [ ] {Verifiable criterion 2}
- [ ] {Verifiable criterion 3}

### Out of Scope

- {Explicitly excluded work}
```
