> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/terraform.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Terraform 语言提示词片段

## 核心概念

- **声明式基础设施**：定义期望状态，Terraform 计算并应用差异
- **Provider**：连接云 API 的插件（AWS、GCP、Azure、Kubernetes 等）
- **Resource**：`resource "type" "name"` 块，声明基础设施组件
- **Data Source**：`data "type" "name"` 块，读取已有基础设施状态
- **变量**：`variable` 块，用默认值与校验规则参数化配置
- **输出**：`output` 块，暴露值供跨模块引用或人工查看
- **模块**：可复用、可组合的基础设施包，自带变量与输出
- **状态管理**：`.tfstate` 文件记录真实资源的映射（绝不提交到 git）
- **Workspace**：隔离的状态环境，用一份代码管理 dev/staging/prod
- **Plan 与 Apply**：`terraform plan` 预览变更，`terraform apply` 执行变更

## 重要文件模式

- `main.tf`：主要资源定义
- `variables.tf`：输入变量声明，含类型与默认值
- `outputs.tf`：输出值定义
- `providers.tf`：Provider 配置与版本约束
- `backend.tf`：远端状态后端配置（S3、GCS 等）
- `modules/**/*.tf`：可复用的基础设施模块
- `*.tfvars`：不同环境的变量值文件
- `terraform.lock.hcl`：Provider 版本锁定文件

## 边模式

- Terraform 文件对其定义的基础设施资源建立 `provisions` 边
- 模块引用在 Terraform 文件之间创建 `depends_on` 边
- Terraform 通过引用容器镜像或部署目标 `deploys` 应用代码
- 变量文件对其参数化的 Terraform 模块建立 `configures` 边

## 摘要风格

> "Terraform 配置：预配 N 个 AWS 资源，包括 VPC、ECS 集群与 RDS 实例。"
> "基础设施模块：定义带 RBAC 与网络策略的可复用 Kubernetes 命名空间。"
> "变量定义：N 个环境相关设置（region、实例类型、扩缩容）。"
