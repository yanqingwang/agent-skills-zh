> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/cloud-architect/references/aws.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# AWS 架构参考

涵盖 AWS 服务、架构模式与 Well-Architected Framework 落地的综合指南。

## Well-Architected Framework

### 六大支柱

1. **卓越运营**
   - 基础设施即代码（CloudFormation、CDK、Terraform）
   - 持续集成/持续部署
   - 可观测性（CloudWatch、X-Ray）
   - Runbook 与 Playbook
   - 演练日（Game Day）与故障注入

2. **安全性**
   - 身份与访问管理（IAM）
   - 检测性控制（GuardDuty、Security Hub）
   - 基础设施防护（VPC、安全组、NACL）
   - 数据保护（KMS、静态/传输加密）
   - 事件响应自动化

3. **可靠性**
   - 多可用区（Multi-AZ）部署
   - Auto Scaling 组
   - Route 53 健康检查与故障转移
   - 备份与恢复（AWS Backup）
   - 混沌工程（AWS FIS）

4. **性能效率**
   - 用 Compute Optimizer 做实例规格选型
   - 缓存策略（CloudFront、ElastiCache）
   - 数据库优化（RDS Performance Insights）
   - 无服务器（Serverless）架构
   - 全球内容分发

5. **成本优化**
   - 预留实例（Reserved Instances）与 Savings Plans
   - 容错型工作负载使用 Spot 实例
   - S3 Intelligent-Tiering 与生命周期策略
   - 规格选型建议
   - 成本分摊标签与预算

6. **可持续性**
   - 优先选择使用可再生能源的区域
   - 用 Serverless 减少空闲资源
   - 高效的数据存储模式
   - 资源利用率优化

## 核心服务架构

### 计算

**EC2（Elastic Compute Cloud）**
- 实例族：通用型（t3、m5）、计算型（c5）、内存型（r5）、GPU 型（p3、g4）
- Auto Scaling：目标跟踪、步进扩缩、计划扩缩
- 置放群组：集群（cluster）、分区（partition）、分散（spread）
- 最佳实践：使用最新一代实例、合理选型、开启详细监控

**Lambda**
- 调用模型：同步、异步、事件源映射
- 并发：预留并发、预置并发、突发上限
- 用 Layer 共享依赖
- 最佳实践：保持函数精小、使用环境变量、设置超时

**ECS/EKS（容器服务）**
- ECS：要 Serverless 用 Fargate，要控制力用 EC2
- EKS：托管 Kubernetes，深度集成 AWS
- 服务网格：用 App Mesh 做可观测性
- 最佳实践：求简单用 Fargate，求可移植用 EKS

**Elastic Beanstalk**
- 面向 Web 应用的托管平台
- 内置自动扩缩与负载均衡
- 支持多语言与 Docker

### 存储

**S3（Simple Storage Service）**
- 存储类别：Standard、IA、One Zone-IA、Glacier、Deep Archive
- 用生命周期策略自动分层
- 用版本控制与 MFA 删除做保护
- 跨区域复制用于容灾
- 最佳实践：开启版本控制、使用生命周期策略、阻止公开访问

**EBS（Elastic Block Store）**
- 卷类型：gp3（通用）、io2（高 IOPS）、st1（高吞吐）、sc1（冷数据）
- 快照存到 S3 做备份
- 默认加密
- 最佳实践：多数工作负载用 gp3、开启加密

**EFS（Elastic File System）**
- NFSv4 文件系统，支持共享访问
- 性能模式：通用型（General Purpose）、Max I/O
- 吞吐模式：突发（Bursting）、预置（Provisioned）
- 最佳实践：使用生命周期管理、开启加密

**FSx**
- FSx for Windows File Server（SMB）
- FSx for Lustre（HPC 工作负载）
- FSx for NetApp ONTAP
- FSx for OpenZFS

### 数据库

**RDS（Relational Database Service）**
- 引擎：MySQL、PostgreSQL、MariaDB、Oracle、SQL Server、Aurora
- Multi-AZ 实现高可用
- 只读副本实现扩展
- 自动备份与时点恢复（PITR）
- 最佳实践：追求性能用 Aurora、开启 Multi-AZ、使用只读副本

**Aurora**
- 兼容 MySQL 和 PostgreSQL
- 性能为 MySQL 的 5 倍、PostgreSQL 的 3 倍
- Aurora Global Database 做跨区域容灾
- Serverless v2 应对波动负载
- 最佳实践：负载不可预测时用 Aurora Serverless

**DynamoDB**
- NoSQL 键值与文档数据库
- 按需（on-demand）或预置（provisioned）容量
- Global Tables 实现多区域复制
- DynamoDB Streams 做变更数据捕获
- 最佳实践：流量不可预测用按需容量、谨慎设计 GSI

**ElastiCache**
- Redis 或 Memcached 内存缓存
- Redis 集群模式提升扩展性
- 最佳实践：用于会话存储、API 缓存

### 网络

**VPC（Virtual Private Cloud）**
- CIDR 规划：避免重叠、预留增长空间
- 子网：公有（IGW）、私有（NAT）、隔离（不通外网）
- 路由表与路由决策
- 安全组（有状态）与 NACL（无状态）
- 最佳实践：VPC 用 /16、子网用 /24、规划好 IP 空间

**Route 53**
- 带健康检查的 DNS 服务
- 路由策略：简单、加权、延迟、故障转移、地理位置
- 最佳实践：使用别名记录、开启 DNSSEC

**CloudFront**
- 全球 CDN，边缘节点分布广
- 源站类型：S3、ALB、自定义源站
- Lambda@Edge 处理请求/响应
- 最佳实践：开启压缩、使用字段级加密

**VPN 与 Direct Connect**
- Site-to-Site VPN 建立加密隧道
- Direct Connect 提供专用带宽
- Transit Gateway 构建中心辐射（hub-and-spoke）拓扑
- 最佳实践：高带宽用 Direct Connect，复杂路由用 Transit Gateway

**API Gateway**
- REST API、HTTP API、WebSocket API
- 限流与配额
- 与 Lambda、HTTP 端点、AWS 服务集成
- 最佳实践：成本敏感用 HTTP API、实现缓存

### 安全

**IAM（Identity and Access Management）**
- 最小权限原则
- 应用用角色（Role），不用访问密钥
- 特权用户启用 MFA
- 服务控制策略（SCP）做组织级管控
- 最佳实践：使用角色、开启 MFA、轮换凭证

**KMS（Key Management Service）**
- 客户托管密钥（CMK）
- 自动密钥轮换
- 信封加密模式
- 最佳实践：开启自动轮换、用 grant 做临时访问授权

**Secrets Manager**
- RDS 凭证自动轮换
- 版本管理与回滚
- 最佳实践：定期轮换密钥、使用 VPC 端点

**Security Hub**
- 集中管理安全发现（findings）
- CIS AWS Foundations Benchmark
- 与 GuardDuty、Inspector、Macie 集成

**GuardDuty**
- 基于 ML 的威胁检测
- 监控 CloudTrail、VPC Flow Logs、DNS 日志

## 架构模式

### 高可用

**Multi-AZ 模式**
```
- Application Load Balancer across 3 AZs
- Auto Scaling group with instances in each AZ
- RDS Multi-AZ for database
- S3 for static assets (11 9's durability)
```

**多区域（Multi-Region）模式**
```
- Route 53 with health checks and failover
- CloudFront for global distribution
- Aurora Global Database for <1s RPO
- S3 Cross-Region Replication
```

### Serverless 架构

**API 驱动模式**
```
API Gateway -> Lambda -> DynamoDB
              |
              v
          EventBridge -> Lambda (async processing)
```

**事件驱动模式**
```
S3 Event -> Lambda -> Process -> SNS
                                  |
                                  v
                              Multiple subscribers
```

### AWS 上的微服务

**基于容器**
```
ALB -> ECS Fargate (multiple services)
    |
    v
Service Discovery (Cloud Map)
    |
    v
RDS/DynamoDB per service
```

**服务网格**
```
App Mesh for traffic management
X-Ray for distributed tracing
CloudWatch Container Insights
```

### 数据湖架构

```
Data Sources -> Kinesis Data Streams
                      |
                      v
              Kinesis Firehose
                      |
                      v
                S3 (raw bucket)
                      |
                      v
        Glue ETL or Lambda processing
                      |
                      v
            S3 (processed bucket)
                      |
                      v
          Athena/Redshift Spectrum
                      |
                      v
              QuickSight dashboards
```

## 迁移策略（6R）

1. **Rehost（Lift-and-Shift，原样上云）**
   - AWS Application Migration Service（MGN）
   - 改动最小，迁移最快
   - 适用于有合规约束的遗留应用

2. **Replatform（Lift-Tinker-and-Shift，小幅改造后上云）**
   - 自管数据库换成 RDS
   - 自建应用服务器换成 Elastic Beanstalk
   - 迁移过程中做少量优化

3. **Repurchase（Drop-and-Shop，弃旧换新）**
   - 改用 SaaS（如 Salesforce、Workday）
   - 降低维护负担

4. **Refactor/Re-architect（重构/重设计）**
   - 现代化为 Serverless 或容器
   - 投入最大，收益也最大
   - 适用于构成竞争优势的应用

5. **Retire（退役）**
   - 下线不再使用的应用
   - 缩小攻击面、降低成本

6. **Retain（保留）**
   - 暂时留在本地（on-premises）
   - 以后再迁，或因监管原因长期保留

## Landing Zone 设计

**AWS Control Tower**
- 多账号策略（AWS Organizations）
- 账号工厂（Account Factory）实现标准化
- 用防护栏（Guardrails）做治理（SCP）
- 集中式日志（CloudTrail、Config）

**账号结构**
```
Root
├── Security OU
│   ├── Log Archive Account
│   └── Security Tooling Account
├── Infrastructure OU
│   ├── Network Account (Transit Gateway, VPN)
│   └── Shared Services Account
└── Workloads OU
    ├── Production Account
    ├── Staging Account
    └── Development Account
```

**网络设计**
```
Transit Gateway (hub)
    |
    ├── Production VPC
    ├── Staging VPC
    ├── Development VPC
    └── On-premises (Direct Connect/VPN)
```

## 成本优化策略

**计算成本节省**
- Compute Savings Plans（最高省 66%）
- EC2 预留实例（1 年或 3 年）
- 批处理/容错型工作负载用 Spot 实例
- Lambda：尽量降低内存配置，使用预留并发

**存储成本节省**
- 访问模式不可预测用 S3 Intelligent-Tiering
- 用生命周期策略转入 Glacier/Deep Archive
- EBS 用 gp3 替代 gp2（便宜 20%，性能更好）
- 删除无用的快照与卷

**数据库成本节省**
- 波动负载用 Aurora Serverless v2
- RDS 预留实例
- DynamoDB 负载不可预测用按需容量
- 只读副本放在同区域，减少跨可用区数据传输

**监控与告警**
- 用 AWS Cost Explorer 做分析
- 用 AWS Budgets 做告警
- 成本异常检测（Cost Anomaly Detection）
- 用 Trusted Advisor 获取建议

## 灾难恢复

**RPO 与 RTO 目标**
- 备份恢复（Backup and Restore）：RPO/RTO 小时级（成本最低）
- 导引灯（Pilot Light）：RPO 分钟级，RTO 小时级
- 温备（Warm Standby）：RPO 秒级，RTO 分钟级
- 多站点双活（Multi-Site Active/Active）：RPO/RTO 接近零（成本最高）

**落地手段**
- 用 AWS Backup 集中管理备份
- 用 Aurora Global Database 做跨区域复制
- S3 跨区域复制
- Route 53 健康检查与故障转移路由
- 用 CloudFormation/Terraform 定期做容灾演练

## 监控与可观测性

**CloudWatch**
- 指标：标准（5 分钟）与详细（1 分钟）粒度
- 告警联动 SNS 通知
- 用 Logs Insights 分析日志
- 用仪表盘做可视化

**X-Ray**
- 微服务分布式追踪
- 服务地图可视化
- 追踪注解（annotations）与元数据

**AWS Config**
- 资源清单与变更跟踪
- 合规规则评估
- 资源间关系跟踪
