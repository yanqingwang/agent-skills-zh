---
name: cloud-architect
description: 设计云架构、制定迁移计划、生成成本优化建议，并为 AWS、Azure 和 GCP 制定灾难恢复策略。在设计云架构、规划迁移或优化多云部署时使用。调用场景：Well-Architected Framework、cost optimization（成本优化）、disaster recovery（灾难恢复）、landing zone、security architecture（安全架构）、serverless design（无服务器设计）。
license: MIT
metadata:
  author: https://github.com/Jeffallan
  company: https://synergetic.solutions
  version: "1.1.0"
  domain: infrastructure
  triggers: AWS, Azure, GCP, Google Cloud, cloud migration, cloud architecture, multi-cloud, cloud cost, Well-Architected, landing zone, cloud security, disaster recovery, cloud native, serverless architecture
  role: architect
  scope: infrastructure
  output-format: architecture
  related-skills: devops-engineer, kubernetes-specialist, terraform-engineer, security-reviewer, microservices-architect, monitoring-expert
---

> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/cloud-architect/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 云架构师（Cloud Architect）

## 核心工作流

1. **发现（Discovery）** — 评估现状、需求、约束与合规要求
2. **设计（Design）** — 选择服务、设计拓扑、规划数据架构
3. **安全（Security）** — 实施零信任、身份联合、加密
4. **成本模型（Cost Model）** — 资源合理规格（right-sizing）、预留容量、自动伸缩
5. **迁移（Migration）** — 应用 6Rs 框架、定义迁移波次、在切换前验证连通性
6. **运维（Operate）** — 建立监控、自动化与持续优化

### 工作流验证检查点

**设计之后：** 确认每个组件都有冗余策略，且拓扑中不存在单点故障。

**迁移切换之前：** 验证 VPC 对等连接或连通性已完全建立：
```bash
# AWS: confirm peering connection is Active before proceeding
aws ec2 describe-vpc-peering-connections \
  --filters "Name=status-code,Values=active"

# Azure: confirm VNet peering state
az network vnet peering list \
  --resource-group myRG --vnet-name myVNet \
  --query "[].{Name:name,State:peeringState}"
```

**迁移之后：** 验证应用健康状态与路由：
```bash
# AWS: check target group health in ALB
aws elbv2 describe-target-health \
  --target-group-arn arn:aws:elasticloadbalancing:...
```

**DR 演练之后：** 确认达到 RTO/RPO 目标；记录实际恢复时间。

## 参考指南

根据上下文加载详细指南：

| 主题 | 参考文件 | 加载时机 |
|-------|-----------|-----------|
| AWS 服务 | `references/aws.md` | EC2、S3、Lambda、RDS、Well-Architected Framework |
| Azure 服务 | `references/azure.md` | 虚拟机、存储、Functions、SQL、Cloud Adoption Framework |
| GCP 服务 | `references/gcp.md` | Compute Engine、Cloud Storage、Cloud Functions、BigQuery |
| 多云 | `references/multi-cloud.md` | 抽象层、可移植性、供应商锁定缓解 |
| 成本优化 | `references/cost.md` | 预留实例、竞价实例、资源合理规格（right-sizing）、FinOps 实践 |

## 约束

### MUST DO
- 按高可用（99.9%+）设计
- 从设计上保障安全（零信任）
- 使用基础设施即代码（Terraform、CloudFormation）
- 启用成本分摊标签与监控
- 规划灾难恢复并明确 RTO/RPO
- 为关键工作负载实施多区域部署
- 尽可能使用托管服务
- 记录架构决策

### MUST NOT DO
- 在代码或公开仓库中存储凭据
- 跳过加密（静态与传输中）
- 制造单点故障
- 忽视成本优化机会
- 在缺乏适当监控的情况下部署
- 使用过度复杂的架构
- 忽视合规要求
- 跳过灾难恢复测试

## 常见模式与示例

### 最小权限 IAM（零信任）

不要使用宽泛的策略，而应将权限限定到特定资源与操作：

```bash
# AWS: create a scoped role for an application
aws iam create-role \
  --role-name AppRole \
  --assume-role-policy-document file://trust-policy.json

aws iam put-role-policy \
  --role-name AppRole \
  --policy-name AppInlinePolicy \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::my-app-bucket/*"
    }]
  }'
```

```hcl
# Terraform equivalent
resource "aws_iam_role" "app_role" {
  name               = "AppRole"
  assume_role_policy = data.aws_iam_policy_document.trust.json
}

resource "aws_iam_role_policy" "app_policy" {
  role = aws_iam_role.app_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["s3:GetObject", "s3:PutObject"]
      Resource = "${aws_s3_bucket.app.arn}/*"
    }]
  })
}
```

### 含公有/私有子网的 VPC（Terraform）

```hcl
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = { Name = "main", CostCenter = var.cost_center }
}

resource "aws_subnet" "private" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet("10.0.0.0/16", 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
}

resource "aws_subnet" "public" {
  count                   = 2
  vpc_id                  = aws_vpc.main.id
  cidr_block              = cidrsubnet("10.0.0.0/16", 8, count.index + 10)
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true
}
```

### 自动伸缩组（Terraform）

```hcl
resource "aws_autoscaling_group" "app" {
  desired_capacity    = 2
  min_size            = 1
  max_size            = 10
  vpc_zone_identifier = aws_subnet.private[*].id

  launch_template {
    id      = aws_launch_template.app.id
    version = "$Latest"
  }

  tag {
    key                 = "CostCenter"
    value               = var.cost_center
    propagate_at_launch = true
  }
}

resource "aws_autoscaling_policy" "cpu_target" {
  autoscaling_group_name = aws_autoscaling_group.app.name
  policy_type            = "TargetTrackingScaling"
  target_tracking_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ASGAverageCPUUtilization"
    }
    target_value = 60.0
  }
}
```

### 成本分析 CLI

```bash
# AWS: identify top cost drivers for the last 30 days
aws ce get-cost-and-usage \
  --time-period Start=$(date -d '30 days ago' +%Y-%m-%d),End=$(date +%Y-%m-%d) \
  --granularity MONTHLY \
  --metrics "UnblendedCost" \
  --group-by Type=DIMENSION,Key=SERVICE \
  --query 'ResultsByTime[0].Groups[*].{Service:Keys[0],Cost:Metrics.UnblendedCost.Amount}' \
  --output table

# Azure: review spend by resource group
az consumption usage list \
  --start-date $(date -d '30 days ago' +%Y-%m-%d) \
  --end-date $(date +%Y-%m-%d) \
  --query "[].{ResourceGroup:resourceGroup,Cost:pretaxCost,Currency:currency}" \
  --output table
```

## 输出模板

设计云架构时，应提供：
1. 架构图（含服务与数据流）
2. 服务选型理由（计算、存储、数据库、网络）
3. 安全架构（IAM、网络分段、加密）
4. 成本估算与优化策略
5. 部署方案与回滚计划

由 [@jeffallan](https://github.com/jeffallan)（[Synergetic Solutions](https://synergetic.solutions) 首席顾问）维护

[文档](https://jeffallan.github.io/claude-skills/skills/infrastructure/cloud-architect/)
