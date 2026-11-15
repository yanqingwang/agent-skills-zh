> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/cloud-architect/references/cost.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 云成本优化参考

全面介绍云成本优化的指南，涵盖预留实例、Spot/抢占式实例、规格合理化（right-sizing）与 FinOps 实践。

## FinOps 框架

### FinOps 原则

1. **团队需要协作** - 财务、工程与业务共同参与
2. **人人担责** - 成本责任分散化
3. **由中心化团队推动 FinOps** - 建立卓越中心，沉淀最佳实践
4. **报告应可访问且及时** - 实时的成本可见性
5. **决策由业务价值驱动** - 按业务成果衡量成本
6. **充分利用可变成本模型** - 按需弹性伸缩

### FinOps 生命周期

```
      Inform
         |
    +---------+
    |         |
    v         v
 Optimize --> Operate
    ^         |
    |         |
    +---------+
```

**Inform 阶段**
- 成本支出可见化
- 成本分摊与展示（showback）
- 基准对比与预测

**Optimize 阶段**
- 费率优化（预留实例、节省计划）
- 用量优化（规格合理化）
- 架构优化

**Operate 阶段**
- 持续改进
- 自动化与治理
- 异常检测

## 计算成本优化

### 预留实例 / 节省计划

**AWS 节省计划（Savings Plans）**

| 类型 | 灵活性 | 节省幅度 |
|------|-------------|---------|
| 计算节省计划（Compute Savings Plans） | 任意 EC2、Fargate、Lambda | 最高 66% |
| EC2 实例节省计划（EC2 Instance Savings Plans） | 特定实例家族、特定区域 | 最高 72% |
| 预留实例（Reserved Instances） | 特定实例类型、特定可用区 | 最高 72% |

**承诺策略**
```
Baseline (always-on): 1-year or 3-year Savings Plans
Variable (predictable): Scheduled Reserved Instances
Spiky (unpredictable): On-Demand + Spot
```

**Azure 预留**
```
# Azure CLI - Purchase reservation
az reservations reservation-order purchase \
  --sku Standard_D2s_v3 \
  --term P1Y \
  --billing-scope /subscriptions/{subscription-id} \
  --quantity 10 \
  --applied-scope-type Shared
```

**GCP 承诺使用折扣（Committed Use Discounts）**
- 基于资源：特定 vCPU 与内存
- 基于消费：按金额承诺，换取灵活性
- 1 年期（37% 折扣）或 3 年期（55% 折扣）

### Spot/抢占式实例

**何时使用 Spot**
- 批处理与分析
- CI/CD 构建节点
- 无状态 Web 服务器（配合自动扩缩容）
- 机器学习训练
- 开发与测试环境

**AWS Spot 最佳实践**
```yaml
# EC2 Auto Scaling with Spot
MixedInstancesPolicy:
  InstancesDistribution:
    OnDemandBaseCapacity: 2
    OnDemandPercentageAboveBaseCapacity: 20
    SpotAllocationStrategy: capacity-optimized
  LaunchTemplate:
    Overrides:
      - InstanceType: m5.large
      - InstanceType: m5a.large
      - InstanceType: m4.large
      - InstanceType: r5.large
```

**Spot 中断处理**
```python
# Check for spot termination notice (AWS)
import requests

def check_spot_termination():
    try:
        response = requests.get(
            "http://169.254.169.254/latest/meta-data/spot/termination-time",
            timeout=2
        )
        if response.status_code == 200:
            # 2-minute warning - gracefully shutdown
            graceful_shutdown()
    except requests.exceptions.RequestException:
        pass  # Not being terminated
```

**GCP 抢占式/Spot 虚拟机**
```hcl
# Terraform - GCP Spot VM
resource "google_compute_instance" "spot" {
  name         = "spot-instance"
  machine_type = "n2-standard-4"

  scheduling {
    preemptible                 = true
    automatic_restart           = false
    provisioning_model          = "SPOT"
    instance_termination_action = "STOP"
  }
}
```

### 规格合理化（Right-Sizing）

**分析流程**
1. 收集指标（CPU、内存、网络、磁盘 I/O）
2. 找出空闲或利用率过低的资源
3. 推荐合适的实例规格
4. 在维护窗口期间实施变更
5. 持续监控并迭代

**AWS Compute Optimizer**
```bash
# Enable Compute Optimizer
aws compute-optimizer update-enrollment-status \
  --status Active \
  --include-member-accounts

# Get recommendations
aws compute-optimizer get-ec2-instance-recommendations \
  --filters name=Finding,values=OVER_PROVISIONED
```

**规格合理化阈值**
| 指标 | 利用率过低 | 合理 | 利用率过高 |
|--------|---------------|---------|--------------|
| CPU | 平均 <20% | 平均 40-60% | 平均 >80% |
| 内存 | 平均 <30% | 平均 50-70% | 平均 >85% |
| 网络 | 容量 <10% | 不定 | 容量 >80% |

**Azure Advisor 建议**
```bash
# Get cost recommendations
az advisor recommendation list \
  --category Cost \
  --query "[?impact=='High']"
```

## 存储成本优化

### 对象存储分层

**AWS S3 存储类**
```
S3 Standard
    |
    | (30 days)
    v
S3 Standard-IA
    |
    | (90 days)
    v
S3 Glacier Instant Retrieval
    |
    | (180 days)
    v
S3 Glacier Deep Archive
```

**生命周期策略示例**
```json
{
  "Rules": [
    {
      "ID": "OptimizeCosts",
      "Status": "Enabled",
      "Filter": { "Prefix": "logs/" },
      "Transitions": [
        { "Days": 30, "StorageClass": "STANDARD_IA" },
        { "Days": 90, "StorageClass": "GLACIER" },
        { "Days": 365, "StorageClass": "DEEP_ARCHIVE" }
      ],
      "Expiration": { "Days": 730 }
    }
  ]
}
```

**S3 Intelligent-Tiering（智能分层）**
- 按访问模式自动分层
- 无检索费用
- 每个对象收取少量监控费用
- 最适合访问模式不可预测的场景

### 块存储优化

**EBS 卷选型**
| 类型 | 使用场景 | 美元/GB/月 |
|------|----------|------------|
| gp3 | 通用 | $0.08 |
| gp2 | 旧类型（应迁移到 gp3） | $0.10 |
| io2 | 高 IOPS 数据库 | $0.125+ |
| st1 | 高吞吐（大数据） | $0.045 |
| sc1 | 冷归档 | $0.015 |

**迁移到 gp3（节省 20%）**
```bash
# Modify EBS volume from gp2 to gp3
aws ec2 modify-volume \
  --volume-id vol-12345678 \
  --volume-type gp3 \
  --iops 3000 \
  --throughput 125
```

### 数据库存储

**Aurora 存储优化**
- 仅为实际使用的存储付费（自动扩容）
- 无需预先预配
- 以 10GB 为增量，上限 128TB

**DynamoDB 容量模式**
| 模式 | 适用场景 | 计价 |
|------|----------|---------|
| 按需（On-Demand） | 流量不可预测 | 按请求付费 |
| 预置（Provisioned） | 流量稳定 | 按容量单位付费 |
| 预置 + 自动扩缩 | 流量波动但可预测 | 成本低于按需 |

## 网络成本优化

### 数据传输成本

**AWS 数据传输定价**
```
Inbound: Free
Same AZ: Free
Cross-AZ: $0.01/GB each direction
Same Region (via public IP): $0.01/GB
Cross-Region: $0.02/GB
Internet Egress: $0.09/GB (first 10TB)
```

**优化策略**
1. 尽可能让流量留在同一可用区内
2. 为 AWS 服务使用 VPC 终端节点
3. 可缓存内容交给 CloudFront
4. 传输前先压缩数据
5. 尽量用区域级服务而非全局服务

**VPC 终端节点（避开 NAT 网关）**
```hcl
# Gateway endpoint (free for S3, DynamoDB)
resource "aws_vpc_endpoint" "s3" {
  vpc_id       = aws_vpc.main.id
  service_name = "com.amazonaws.us-east-1.s3"
}

# Interface endpoint (cheaper than NAT for specific services)
resource "aws_vpc_endpoint" "ecr" {
  vpc_id            = aws_vpc.main.id
  service_name      = "com.amazonaws.us-east-1.ecr.api"
  vpc_endpoint_type = "Interface"
}
```

### CDN 优化

**CloudFront 成本节省**
- 数据传输费率低于直接回源
- 优化缓存命中率（目标 >90%）
- 用 Origin Shield 降低回源负载
- 压缩对象（Gzip/Brotli）

```yaml
# CloudFront cache optimization
CacheBehaviors:
  - PathPattern: "/static/*"
    CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6  # CachingOptimized
    Compress: true
    TTL:
      DefaultTTL: 86400
      MaxTTL: 31536000
```

## Serverless 成本优化

### Lambda 优化

**内存/CPU 调优**
```python
# Use AWS Lambda Power Tuning
# Finds optimal memory for cost vs performance

# Results example:
# 128MB:  $0.000021 per invocation, 3200ms duration
# 256MB:  $0.000025 per invocation, 1600ms duration
# 512MB:  $0.000031 per invocation, 800ms duration
# 1024MB: $0.000042 per invocation, 450ms duration
# Optimal: 512MB (best cost-performance balance)
```

**降本策略**
1. 合理设定内存配额
2. 尽量减少冷启动（关键路径用预置并发）
3. 使用 ARM64（Graviton2），便宜 20%
4. 优化包体积，加快冷启动
5. 共享依赖放进 Lambda Layers

**Graviton2 迁移**
```yaml
# SAM template with ARM64
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: python3.11
      Architectures:
        - arm64  # 20% cost savings
```

### 容器优化

**Fargate 计价优化**
```
# Fargate Spot: Up to 70% discount
# Use for fault-tolerant workloads

ECS Service:
  CapacityProviderStrategy:
    - CapacityProvider: FARGATE_SPOT
      Weight: 4
    - CapacityProvider: FARGATE
      Weight: 1
      Base: 2  # Minimum on-demand tasks
```

**合理设定容器资源**
```yaml
# Analyze actual usage with Container Insights
resources:
  requests:
    memory: "256Mi"  # Based on p95 usage + 20% buffer
    cpu: "100m"      # Based on p95 usage + 20% buffer
  limits:
    memory: "512Mi"  # 2x requests for burst
    cpu: "500m"
```

## 成本分摊与打标签

### 打标签策略

**必需标签**
```yaml
# Terraform - enforce tags
variable "required_tags" {
  default = {
    environment  = "prod"
    cost-center  = "engineering"
    owner        = "platform-team"
    project      = "api-gateway"
    managed-by   = "terraform"
  }
}

resource "aws_instance" "example" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.medium"
  tags          = var.required_tags
}
```

**标签强制执行**
```json
// AWS SCP - Deny untagged resources
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyUntaggedEC2",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "arn:aws:ec2:*:*:instance/*",
      "Condition": {
        "Null": {
          "aws:RequestTag/cost-center": "true"
        }
      }
    }
  ]
}
```

### 成本分摊报告

**AWS 成本与使用报告（CUR）**
```bash
# Enable detailed billing reports
aws cur put-report-definition \
  --report-definition '{
    "ReportName": "detailed-cost-report",
    "TimeUnit": "HOURLY",
    "Format": "Parquet",
    "Compression": "Parquet",
    "S3Bucket": "my-billing-bucket",
    "S3Region": "us-east-1",
    "AdditionalArtifacts": ["ATHENA"]
  }'
```

**用 Athena 做分析查询**
```sql
-- Cost by service and tag
SELECT
  line_item_product_code as service,
  resource_tags_user_cost_center as cost_center,
  SUM(line_item_unblended_cost) as cost
FROM cost_report
WHERE month = '2024-01'
GROUP BY 1, 2
ORDER BY 3 DESC;

-- Unused Reserved Instances
SELECT
  reservation_reservation_a_r_n,
  reservation_unused_quantity,
  reservation_unused_normalized_unit_quantity
FROM cost_report
WHERE reservation_unused_quantity > 0;
```

## 自动化与治理

### 自动化成本管控

**AWS Budgets 配合自动操作**
```yaml
# CloudFormation - Budget with auto-stop
Resources:
  MonthlyCostBudget:
    Type: AWS::Budgets::Budget
    Properties:
      Budget:
        BudgetName: monthly-cost-limit
        BudgetLimit:
          Amount: 10000
          Unit: USD
        TimeUnit: MONTHLY
        BudgetType: COST
      NotificationsWithSubscribers:
        - Notification:
            NotificationType: ACTUAL
            ComparisonOperator: GREATER_THAN
            Threshold: 80
          Subscribers:
            - SubscriptionType: EMAIL
              Address: finance@company.com
```

**计划扩缩（开发/测试环境）**
```yaml
# Stop non-prod resources nights/weekends
Resources:
  ScaleDownSchedule:
    Type: AWS::AutoScaling::ScheduledAction
    Properties:
      AutoScalingGroupName: !Ref DevASG
      DesiredCapacity: 0
      Recurrence: "0 20 * * MON-FRI"  # 8 PM weekdays

  ScaleUpSchedule:
    Type: AWS::AutoScaling::ScheduledAction
    Properties:
      AutoScalingGroupName: !Ref DevASG
      DesiredCapacity: 3
      Recurrence: "0 8 * * MON-FRI"   # 8 AM weekdays
```

### 成本异常检测

**AWS 成本异常检测**
```bash
# Create anomaly monitor
aws ce create-anomaly-monitor \
  --anomaly-monitor '{
    "MonitorName": "ServiceMonitor",
    "MonitorType": "DIMENSIONAL",
    "MonitorDimension": "SERVICE"
  }'

# Create anomaly subscription
aws ce create-anomaly-subscription \
  --anomaly-subscription '{
    "SubscriptionName": "CostAlerts",
    "MonitorArnList": ["arn:aws:ce::123456789:anomalymonitor/abc123"],
    "Subscribers": [{"Type": "EMAIL", "Address": "alerts@company.com"}],
    "Threshold": 100
  }'
```

## 成本指标与 KPI

### 关键指标

| 指标 | 公式 | 目标 |
|--------|---------|--------|
| 单位成本 | 总成本 / 业务指标 | 持续下降 |
| 覆盖率 | 预留时长 / 总时长 | >70% |
| 使用率 | 已用预留时长 / 已购时长 | >80% |
| 浪费 | 空闲资源成本 / 总成本 | <10% |
| 预测准确度 | 实际值 / 预测值 | 90-110% |

### 仪表盘示例

```sql
-- Cost efficiency dashboard metrics
WITH metrics AS (
  SELECT
    date_trunc('month', usage_date) as month,
    SUM(cost) as total_cost,
    SUM(CASE WHEN reservation_arn IS NOT NULL THEN cost END) as reserved_cost,
    COUNT(DISTINCT user_id) as active_users
  FROM cloud_costs
  GROUP BY 1
)
SELECT
  month,
  total_cost,
  reserved_cost / total_cost as reservation_coverage,
  total_cost / active_users as cost_per_user
FROM metrics;
```

## 快速见效清单

**立即省钱（本周）**
- [ ] 删除未使用的 EBS 卷和快照
- [ ] 关停不再需要的已停止 EC2 实例
- [ ] 清理未使用的弹性 IP
- [ ] 删除未使用的负载均衡器
- [ ] 审查并删除过时的 AMI

**短期（本月）**
- [ ] 对利用率过低的实例做规格合理化
- [ ] 把 gp2 卷迁移到 gp3
- [ ] 落实 S3 生命周期策略
- [ ] 启用 S3 Intelligent-Tiering
- [ ] 给开发/测试环境做定时开关机

**中期（本季度）**
- [ ] 为基线负载购买节省计划
- [ ] 容错负载改用 Spot
- [ ] 配置成本分摊标签
- [ ] 启用成本异常检测
- [ ] 建立 FinOps 实践
