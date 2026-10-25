---
name: deployment-pipeline-design
description: 设计带审批门禁、安全检查与部署编排的多阶段 CI/CD 流水线。在设计零停机部署流水线、实现金丝雀（canary）发布策略、搭建多环境晋升（promotion）工作流，或调试 CI/CD 中失败的部署门禁时使用此 Skill。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/cicd-automation/skills/deployment-pipeline-design/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 部署流水线设计（Deployment Pipeline Design）

面向多阶段 CI/CD 流水线的架构模式，涵盖审批门禁、部署策略与环境晋升（promotion）工作流。

## 目的

设计健壮、安全的部署流水线，通过合理的阶段组织、自动化的质量门禁（quality gate）与渐进式交付（progressive delivery）策略，在速度与安全之间取得平衡。本 Skill 既覆盖流水线架构的结构性设计，也覆盖实现可靠生产部署的运维模式。

## 输入 / 输出

### 你需要提供

- **应用类型**：语言/运行时、容器化还是裸金属、单体还是微服务
- **部署目标**：Kubernetes、ECS、虚拟机、serverless，还是平台即服务（PaaS）
- **环境拓扑**：环境数量（dev/staging/prod）、区域布局、物理隔离（air-gap）要求
- **发布要求**：可接受的停机时间、回滚 SLA、流量切分需求、金丝雀（canary）与蓝绿（blue-green）的偏好
- **门禁约束**：审批团队、要求的测试覆盖率阈值、合规扫描（SAST、DAST、SCA）
- **监控栈**：Prometheus、Datadog、CloudWatch 或其他用于自动化晋升决策的指标来源

### 本 Skill 产出

- **流水线配置**：阶段定义、作业依赖、并行度与缓存策略
- **部署策略**：选定的发布模式及带注释的配置（金丝雀权重、蓝绿切换、滚动更新参数）
- **健康检查设置**：浅层与深层就绪探针（readiness probe）、部署后冒烟测试脚本
- **门禁定义**：自动化指标阈值与人工审批工作流
- **回滚方案**：自动回滚触发条件与人工 runbook 步骤

## 何时使用

- 为新服务或平台迁移设计 CI/CD 架构
- 在环境之间实现部署门禁
- 配置带强制安全扫描的多环境流水线
- 以金丝雀（canary）或蓝绿（blue-green）策略建立渐进式交付
- 调试"阶段全部成功、但生产行为不对"的流水线
- 通过在指标劣化时自动回滚来缩短平均恢复时间（MTTR）

## 详细模式与完整示例

详细的模式文档位于 `references/details.md`。当上述导航层级的信息不够用时，请阅读该文件。

## 故障排查

### 流水线中健康检查通过，但服务在生产环境不健康

流水线的健康检查命中的是一个浅层的 `/ping` 端点，即使数据库不可达它也返回 200。请改用能验证真实依赖的深层就绪检查（参见上文"健康检查"一节）。

### 金丝雀部署始终无法晋升到 100%

Argo Rollouts 需要一个有效的 `AnalysisTemplate` 才能自动晋升。如果 Prometheus 查询没有返回数据（例如指标名变了），分析会一直处于不确定（inconclusive）状态，晋升随之停滞。添加 `inconclusiveLimit` 让发布快速失败而不是无限挂起：

```yaml
spec:
  metrics:
  - name: error-rate
    failureCondition: "result[0] > 0.05"
    inconclusiveLimit: 2   # fail after 2 inconclusive results, not hang indefinitely
    provider:
      prometheus:
        query: |
          sum(rate(http_requests_total{status=~"5.."}[2m]))
          / sum(rate(http_requests_total[2m]))
```

### staging 部署成功，但生产作业始终不启动

检查生产环境的保护规则（protection rules）是否已配置——缺少审核人分配时，审批门禁会无限等待且没有任何通知。在 GitHub Actions 中，确保在 **Settings → Environments → production** 中将 `Required reviewers` 设置为真实存在的用户或团队。

### Docker 层缓存每次构建都被击穿，导致构建缓慢

如果 `COPY . .` 出现在依赖安装之前，任何源文件的改动都会使依赖层失效。请调整顺序，先复制依赖清单文件：

```dockerfile
# Good: dependencies cached separately from source code
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
```

### 回滚代码后，数据库迁移仍停留在新版本

只回滚服务而不回滚迁移，会导致 schema 与代码不匹配的错误。务必让迁移保持向后兼容（只做加法、只增不改不删）至少一个发布周期，并将撤销脚本与迁移文件一起纳入版本管理：

```bash
# migrations/V20240315__add_nullable_column.sql       (forward)
# migrations/V20240315__add_nullable_column.undo.sql  (backward)
```

在旧代码版本从所有环境中完全下线之前，绝不要执行破坏性迁移（DROP COLUMN、ALTER NOT NULL）。

## 进阶主题

关于平台特定的流水线配置、多区域晋升工作流以及高级 Argo Rollouts 模式，参见：

- [`references/advanced-strategies.md`](references/advanced-strategies.md) — 扩展 YAML 示例、平台特定配置（GitHub Actions、GitLab CI、Azure Pipelines）、多区域金丝雀模式以及数据库迁移回滚策略

## 相关 Skill

- `github-actions-templates` - GitHub Actions 实现模式与可复用 workflow
- `gitlab-ci-patterns` - GitLab CI/CD 流水线实现
- `secrets-management` - CI/CD 流水线中的密钥管理
