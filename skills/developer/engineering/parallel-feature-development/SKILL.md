---
name: parallel-feature-development
description: 通过文件所有权策略、冲突规避规则和集成模式来协调并行功能开发，以支持多 Agent 实现。当把一个大型功能拆解为独立的工作流、当两个或更多 Agent 需要同时实现同一系统的不同层、当需要通过确立文件所有权来避免共享代码库中的合并冲突、当需要设计接口契约以便并行实现者在彼此的 API 就绪之前就能基于其构建，或当需要决定全栈功能采用垂直切片还是水平分层时使用本 Skill。
version: 1.0.2
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/agent-teams/skills/parallel-feature-development/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 并行功能开发

将功能拆解为并行工作流、确立文件所有权边界、避免冲突，以及整合多个实现 Agent 产出的策略。

## 何时使用本 Skill

- 为并行实现拆解功能
- 在 Agent 之间确立文件所有权边界
- 在并行工作流之间设计接口契约
- 选择集成策略（垂直切片 vs 水平分层）
- 管理并行开发的分支与合并工作流

## 文件所有权策略

### 按目录

为每个实现者分配特定目录的所有权：


```
implementer-1: src/components/auth/
implementer-2: src/api/auth/
implementer-3: tests/auth/
```


**最适用于**：组织良好、目录边界清晰的代码库。

### 按模块

分配逻辑模块的所有权（可能跨目录）：


```
implementer-1: Authentication module (login, register, logout)
implementer-2: Authorization module (roles, permissions, guards)
```


**最适用于**：面向功能的架构、领域驱动设计。

### 按层

分配架构层的所有权：


```
implementer-1: UI layer (components, styles, layouts)
implementer-2: Business logic layer (services, validators)
implementer-3: Data layer (models, repositories, migrations)
```


**最适用于**：传统的 MVC/分层架构。

## 冲突规避规则

### 核心准则

**每个文件只有一个所有者。** 任何文件都不应分配给多个实现者。

### 当文件必须共享时

若某个文件确实需要多个实现者改动：

1. **指定唯一所有者**：由一个实现者拥有该文件
2. **其他实现者提出变更请求**：向所有者发送具体的变更请求
3. **所有者按顺序应用变更**：避免合并冲突
4. **备选方案：抽取接口**：创建独立的接口文件，非所有者可直接导入而无需修改

### 接口契约

当实现者需要在边界处协调时：


```typescript
// src/types/auth-contract.ts (owned by team-lead, read-only for implementers)
export interface AuthResponse {
  token: string;
  user: UserProfile;
  expiresAt: number;
}

export interface AuthService {
  login(email: string, password: string): Promise<AuthResponse>;
  register(data: RegisterData): Promise<AuthResponse>;
}
```


两个实现者都从契约文件导入，但都不修改它。

## 集成模式

### 垂直切片

每个实现者构建完整的功能切片（UI + API + 测试）：


```
implementer-1: Login feature (login form + login API + login tests)
implementer-2: Register feature (register form + register API + register tests)
```


**优点**：每个切片可独立测试，所需集成工作最少。
**缺点**：可能重复共享工具，在紧耦合功能下较难实施。

### 水平分层

每个实现者跨所有功能构建其中一层：


```
implementer-1: All UI components (login form, register form, profile page)
implementer-2: All API endpoints (login, register, profile)
implementer-3: All tests (unit, integration, e2e)
```


**优点**：每层内部模式一致，便于自然分工。
**缺点**：集成点更多，第 3 层依赖第 1 层和第 2 层。

### 混合模式

根据耦合程度混合垂直与水平方式：


```
implementer-1: Login feature (vertical slice — UI + API + tests)
implementer-2: Shared auth infrastructure (horizontal — middleware, JWT utils, types)
```


**最适用于**：多数带有一定共享基础设施的真实功能。

## 分支管理

### 单分支策略

所有实现者在同一个功能分支上工作：

- 设置简单，没有合并开销
- 需要严格的文件所有权来避免冲突
- 最适用于：小团队（2-3 人）、边界定义清晰

### 多分支策略

每个实现者在各自的子分支上工作：


```
feature/auth
  ├── feature/auth-login      (implementer-1)
  ├── feature/auth-register    (implementer-2)
  └── feature/auth-tests       (implementer-3)
```


- 隔离性更强，合并点明确
- 开销更高，共享文件中仍可能出现合并冲突
- 最适用于：较大团队（4+ 人）、复杂功能

## 故障排查

**实现者因等待共享代码而互相阻塞。**
把共享部分抽取到由团队负责人拥有的独立接口契约文件中，让实现者从该文件导入。两个实现者都不修改契约，只针对它进行实现。

**即使所有权规则清晰，仍出现合并冲突。**
某个文件同时分给了两个 Agent，或者某个自动导入一切内容的 config/index 文件（例如 `index.ts`、`__init__.py`）被两方都改动过。为所有 barrel/index 文件指定唯一所有者，或由负责人在最后统一合并。

**某个实现者提前完成，但集成步骤被阻塞。**
使用暂存接口：已完成的实现者为下游依赖写一个 stub 或 mock，让另一个实现者能继续工作。在集成时替换为真实实现。

**功能拆分在进行到一半时发现有误。**
停止新工作，由负责人重新分配文件，并通过 broadcast 通报变更。已写部分代码上的沉没成本可以接受，继续沿用错误的拆分更糟。

**某个实现者编写的测试在另一个实现者的代码上失败。**
接口契约发生了漂移：拥有该 API 的实现者改了签名，却没有通知编写测试的实现者。强制推行一条规则：契约文件修改前必须先 broadcast。

## 相关 Skill

- [team-composition-patterns](../team-composition-patterns/SKILL.md)：在拆解工作前选择合适的团队规模与 Agent 类型
- [team-communication-protocols](../team-communication-protocols/SKILL.md)：协调实现者之间的集成交接与计划审批
