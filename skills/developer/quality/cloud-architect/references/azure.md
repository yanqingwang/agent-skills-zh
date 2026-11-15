> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/cloud-architect/references/azure.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Azure 架构参考

全面介绍 Azure 服务、架构模式与云采用框架（Cloud Adoption Framework）落地的指南。

## 云采用框架（Cloud Adoption Framework）

### 框架阶段

1. **战略（Strategy）**
   - 明确业务理由
   - 预期业务成果
   - 编制业务案例
   - 首批项目优先级排序

2. **计划（Plan）**
   - 数字资产评估
   - 初步的组织对齐
   - 技能准备计划
   - 云采用计划

3. **就绪（Ready）**
   - Azure 着陆区（Landing Zone）搭建
   - Azure 设置指南
   - 迁移就绪评估
   - 最佳实践校验

4. **采用（Adopt，迁移 + 创新）**
   - 迁移：评估、迁移、优化
   - 创新：构建云原生方案
   - 最佳实践与模式

5. **治理（Govern）**
   - 治理方法论
   - 治理基准
   - 初始治理基础
   - 成熟治理演进

6. **管理（Manage）**
   - 业务承诺
   - 运营基线
   - 平台与工作负载专业化

## Azure 卓越架构框架（Well-Architected Framework）

### 五大支柱

1. **成本优化（Cost Optimization）**
   - Azure Cost Management and Billing
   - 预留实例与节省计划
   - Azure 混合权益（Azure Hybrid Benefit）
   - 自动扩缩容与规格合理化

2. **运营卓越（Operational Excellence）**
   - 基础设施即代码（ARM、Bicep、Terraform）
   - Azure DevOps 与 GitHub Actions
   - Azure Monitor 与 Application Insights
   - 部署槽与蓝绿部署

3. **性能效率（Performance Efficiency）**
   - Azure CDN 与 Front Door
   - 自动扩缩容（VMSS、App Service）
   - 缓存（Redis、CDN）
   - 性能诊断

4. **可靠性（Reliability）**
   - 可用性区域（Availability Zones）与区域（Region）
   - Azure Site Recovery
   - Load Balancer 与 Traffic Manager
   - 备份与灾难恢复

5. **安全性（Security）**
   - Azure AD（Entra ID）
   - 网络安全组（NSG）与防火墙
   - Azure Key Vault
   - Microsoft Defender for Cloud

## 核心服务架构

### 计算

**虚拟机（Virtual Machines）**
- VM 规格：通用（D 系列）、计算（F 系列）、内存（E 系列）、GPU（N 系列）
- 可用性集（99.95% SLA）
- 可用性区域（99.99% SLA）
- VM 规模集（VM Scale Sets）支持自动扩缩容
- 最佳实践：使用托管磁盘、启用加速网络、使用邻近放置组

**App Service**
- Web 应用、API 应用、移动应用
- 部署槽（Deployment Slots）用于预发布
- 按指标或计划自动扩缩容
- 支持 .NET、Java、Node.js、Python、PHP、Ruby
- 最佳实践：使用部署槽、启用自动扩缩容、高效使用 App Service 计划

**Azure Functions**
- 消耗计划（Consumption Plan，serverless）
- 高级计划（Premium Plan，VNet 集成、无冷启动）
- 专用计划（Dedicated Plan，即 App Service 计划）
- Durable Functions 用于编排
- 最佳实践：函数保持短小、生产环境用高级计划、实现重试策略

**Azure Kubernetes Service（AKS）**
- 托管 Kubernetes 控制平面
- Azure CNI 或 kubenet 网络
- Azure AD 集成
- 虚拟节点（Azure Container Instances）
- 最佳实践：使用系统节点池、启用自动扩缩、实现网络策略

**Container Instances**
- Serverless 容器
- 启动快，无需管理基础设施
- 最适合批处理任务与突发性负载

**Azure Batch**
- 大规模并行与 HPC 负载
- 计算节点自动扩缩
- 任务调度与依赖管理

### 存储

**Blob 存储**
- 存储层：热（Hot）、冷（Cool）、存档（Archive）
- 访问层：高级（Premium）、标准（Standard）
- 生命周期管理策略
- 面向合规的不可变存储
- 最佳实践：使用生命周期策略、启用软删除、实现版本控制

**Azure Files**
- SMB 与 NFS 文件共享
- 与 Azure File Sync 集成
- 高级层提供高性能
- 最佳实践：数据库场景用高级层、实现快照

**磁盘存储**
- 托管磁盘：高级 SSD、标准 SSD、标准 HDD、Ultra Disk
- 用 Azure Disk Encryption 做磁盘加密
- 快照与增量备份
- 最佳实践：生产环境用高级 SSD、启用加密

**Data Lake Storage Gen2**
- 面向大数据的分层命名空间（hierarchical namespace）
- 构建在 Blob 存储之上
- 与 Azure Synapse 和 Databricks 集成
- 最佳实践：启用分层命名空间、使用生命周期策略

**Azure NetApp Files**
- 企业级 NFS 与 SMB 共享
- 高性能、低延迟
- 快照与数据保护

### 数据库

**Azure SQL Database**
- Serverless 与预置计算
- 超大规模（Hyperscale）最高 100TB
- 弹性池管理多个数据库
- 自动优化与智能洞察
- 最佳实践：开发/测试用 Serverless、启用异地复制

**Azure SQL Managed Instance**
- 与 SQL Server 近 100% 兼容
- VNet 集成实现隔离
- 原生虚拟网络实现
- 最佳实践：用于直接迁移（lift-and-shift）场景

**Cosmos DB**
- 多模型 NoSQL 数据库
- 多主节点的全球分布
- 一致性级别：强（Strong）、有限过期（Bounded staleness）、会话（Session）、一致前缀（Consistent prefix）、最终（Eventual）
- API：SQL、MongoDB、Cassandra、Gremlin、Table
- 最佳实践：选择合适的一致性级别，分区键设计至关重要

**Azure Database for PostgreSQL/MySQL/MariaDB**
- 弹性服务器（Flexible Server，较新）vs 单服务器（Single Server，旧版）
- 区域冗余实现高可用
- 只读副本用于横向扩展
- 最佳实践：使用弹性服务器、启用高可用、实现连接池

**Azure Cache for Redis**
- 内存缓存
- 集群支持横向扩展
- 异地复制用于灾难恢复
- 最佳实践：生产环境用高级层、启用持久化

### 网络

**虚拟网络（VNet）**
- CIDR 规划（避免重叠）
- 子网配合网络安全组（NSG）
- 服务终结点与 Private Link
- VNet 对等互连实现连通
- 最佳实践：规划 IP 地址空间、使用 NSG、实现 Private Link

**Azure Load Balancer**
- 四层负载均衡
- 标准 SKU（区域冗余、含 SLA）
- 健康探测与分发算法
- 最佳实践：使用标准 SKU、配置健康探测

**Application Gateway**
- 七层负载均衡
- WAF（Web 应用防火墙）
- 基于 URL 的路由与 SSL 终止
- 最佳实践：启用 WAF、使用自动扩缩

**Azure Front Door**
- 全局负载均衡与 CDN
- 边缘 WAF
- Anycast 带来低延迟
- 最佳实践：全球应用使用、启用缓存

**VPN Gateway 与 ExpressRoute**
- 站点到站点 VPN 提供加密连接
- ExpressRoute 提供私有专用连接
- Virtual WAN 构建全球中转网络
- 最佳实践：生产环境用 ExpressRoute、实现冗余

**Azure Firewall**
- 托管防火墙服务
- 应用规则与网络规则
- 威胁情报
- 最佳实践：用于中心-分支（hub-spoke）拓扑、启用 DNS 代理

**Azure Private Link**
- 到 Azure 服务的私有连接
- 不暴露公网
- PaaS 服务可用
- 最佳实践：生产环境的所有 PaaS 服务都使用

### 安全与身份

**Azure Active Directory（Microsoft Entra ID）**
- 身份与访问管理
- 条件访问（Conditional Access）策略
- 多因素认证
- B2B 与 B2C 场景
- 最佳实践：启用 MFA、使用条件访问、实现 PIM

**Azure Key Vault**
- 机密、密钥与证书管理
- 硬件安全模块（HSM）支撑
- 软删除与清除保护
- 最佳实践：启用软删除、使用 RBAC、实现 Private Link

**Microsoft Defender for Cloud**
- 安全态势管理
- 混合负载的威胁防护
- 合规仪表盘
- JIT 虚拟机访问
- 最佳实践：启用增强安全功能、落实安全建议

**Azure Policy**
- 规模化的治理与合规
- 内置与自定义策略
- Deny、audit、append 效果
- 最佳实践：在管理组层级分配、先测试后强制

**Azure Sentinel**
- 云原生 SIEM 与 SOAR
- AI 驱动的威胁检测
- 与 Microsoft 365 及第三方工具集成
- 最佳实践：启用数据连接器、创建自定义分析规则

## 架构模式

### 高可用

**区域冗余模式**
```
Azure Front Door (global)
    |
    v
Application Gateway (zone-redundant)
    |
    v
VM Scale Set (across availability zones)
    |
    v
Azure SQL Database (zone-redundant)
```

**多区域模式**
```
Azure Traffic Manager (DNS-based routing)
    |
    ├── Region 1: App Service + SQL Database (primary)
    └── Region 2: App Service + SQL Database (geo-replica)
```

### 中心-分支（Hub-Spoke）拓扑

```
Hub VNet
├── Azure Firewall
├── VPN Gateway
└── Shared Services
    |
    ├── Spoke VNet 1 (Production)
    ├── Spoke VNet 2 (Development)
    └── Spoke VNet 3 (DMZ)
```

### Serverless 架构

**事件驱动模式**
```
Event Grid -> Azure Functions -> Cosmos DB
                    |
                    v
              Service Bus -> Functions (processing)
```

**API 优先模式**
```
API Management
    |
    ├── Function App 1 (auth)
    ├── Function App 2 (business logic)
    └── Function App 3 (data access)
```

### Azure 上的微服务

**基于 AKS**
```
Azure Front Door
    |
    v
Application Gateway + WAF
    |
    v
AKS (multiple microservices)
    |
    ├── Cosmos DB (microservice A)
    ├── SQL Database (microservice B)
    └── Service Bus (async communication)
```

**Container Apps 模式**
```
Azure Container Apps
├── Dapr for state management
├── KEDA for event-driven scaling
└── Azure Monitor for observability
```

### 数据平台

```
Data Sources
    |
    v
Event Hubs / IoT Hub
    |
    v
Stream Analytics (real-time processing)
    |
    v
Data Lake Storage Gen2
    |
    v
Azure Synapse Analytics
    |
    v
Power BI (visualization)
```

## 着陆区设计

### 企业级着陆区

**管理组层级**
```
Tenant Root Group
├── Platform
│   ├── Management (monitoring, automation)
│   ├── Connectivity (hub networks, VPN)
│   └── Identity (domain controllers)
└── Landing Zones
    ├── Corp (internal workloads)
    └── Online (internet-facing workloads)
```

**网络拓扑**
```
Hub VNet (Connectivity subscription)
├── Azure Firewall
├── VPN Gateway
├── ExpressRoute Gateway
└── Bastion

Spoke VNets (Workload subscriptions)
├── Production VNet
├── Staging VNet
└── Development VNet
```

**治理**
- 用 Azure Policy 落实合规
- 用管理组构建层级
- 在合适的范围分配 RBAC
- 用资源标记做成本分摊
- 用 Azure Blueprints 实现可重复部署

## 迁移策略

### Azure Migrate

1. **评估（Assess）**
   - 用 Azure Migrate 设备做发现
   - 依赖关系分析
   - 基于性能的规格设定
   - 成本估算

2. **迁移（Migrate）**
   - Azure Migrate: Server Migration（无代理）
   - 数据库迁移服务（Database Migration Service）
   - App Service 迁移助手
   - 大规模数据传输用 Data Box

3. **优化（Optimize）**
   - 规格合理化建议
   - 预留实例
   - Azure 混合权益

### 迁移模式

**重新托管（Rehost）**：虚拟机用 Azure Migrate
**重新平台化（Replatform）**：App Service、Azure SQL Database
**重构（Refactor）**：Container Apps、AKS、Functions
**重建（Rebuild）**：Azure 原生服务（Cosmos DB、Cognitive Services）

## 成本优化

### 计算节省
- Azure 预留实例（1 年或 3 年，最高节省 72%）
- Azure Savings Plans for Compute（最高节省 65%）
- Spot VM 用于容错负载（最高节省 90%）
- Azure 混合权益（复用现有 Windows Server/SQL 许可证）
- 开发/测试 VM 自动关机

### 存储节省
- Blob 存储生命周期策略（热 -> 冷 -> 存档）
- Azure Files：一般用途用标准层
- 托管磁盘：可能的话用标准 SSD 替代高级 SSD
- 删除未使用的快照与磁盘

### 数据库节省
- Azure SQL Database 用 Serverless 层
- Cosmos DB 购买预留容量
- DTU 模型 vs vCore（按负载选择）
- Azure Synapse 闲置时暂停

### 监控
- Azure Cost Management + Billing
- 成本警报与预算
- Azure Advisor 建议
- 资源标记做成本分摊

## 灾难恢复

### Azure Site Recovery

**VM 复制**
- Azure 到 Azure 复制
- 本地到 Azure（VMware、Hyper-V、物理机）
- RPO：30 秒到几分钟
- 自动故障转移与故障回复

**恢复计划**
- 多层应用恢复
- 可自定义脚本与手动操作
- 与 Azure Automation 集成

### 备份策略

**Azure Backup**
- VM 备份（应用一致性）
- Azure VM 中的 SQL Server 与 SAP HANA
- Azure Files 备份
- 跨区域还原

**数据库备份**
- SQL Database：自动备份（7-35 天）
- Cosmos DB：连续备份（30 天）
- 长期保留策略

### 高可用

**RTO/RPO 目标**
- 双活（Active-Active）：多区域配合 Traffic Manager（接近零）
- 主备（Active-Passive）：异地复制加故障转移（分钟级）
- 备份还原：Azure Backup（小时级）

## 监控与可观测性

### Azure Monitor

**组件**
- 指标：时间序列数据（1 分钟粒度）
- 日志：Log Analytics 工作区供查询（KQL）
- 警报：指标、日志与活动日志警报
- 仪表盘：自定义可视化

**Application Insights**
- 面向 Web 应用的 APM
- 分布式追踪
- 实时指标流（Live Metrics Stream）
- 智能检测与异常检测
- 最佳实践：所有应用都接入探针、设置可用性测试

### Log Analytics

**KQL 查询**
```kusto
// Performance analysis
Perf
| where CounterName == "% Processor Time"
| summarize avg(CounterValue) by bin(TimeGenerated, 5m), Computer
| render timechart

// Failed requests
requests
| where success == false
| summarize count() by resultCode, bin(timestamp, 1h)
```

**工作簿（Workbooks）**
- 交互式报表
- 参数化查询
- 指标与日志结合

## 身份与访问

### Azure AD 最佳实践

- 为所有用户启用 MFA
- 使用条件访问策略
- 实现特权标识管理（PIM）
- 定期访问评审
- 紧急访问账户（break-glass）

### RBAC 设计

**内置角色**
- Owner：完全访问（含 RBAC）
- Contributor：除 RBAC 外的完全访问
- Reader：只读访问
- 针对特定需求自定义角色

**范围层级**
```
Management Group (highest)
    |
Subscription
    |
Resource Group
    |
Resource (lowest)
```

最佳实践：在合适的最高层级分配、使用组而非单个用户、落实最小权限
