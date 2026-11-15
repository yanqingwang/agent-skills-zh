> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/cloud-architect/references/gcp.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# GCP 架构参考

全面介绍 Google Cloud Platform 服务、模式与架构框架的指南。

## Google Cloud 架构框架

### 五大支柱

1. **运营卓越（Operational Excellence）**
   - 基础设施即代码（Deployment Manager、Terraform）
   - 用 Cloud Build 做 CI/CD
   - 用 Cloud Monitoring（Stackdriver）做监控
   - SRE 原则与 SLO
   - 事件管理

2. **安全、隐私与合规（Security, Privacy, and Compliance）**
   - 身份与访问管理（Cloud IAM）
   - 用 VPC Service Controls 构建数据边界
   - 用 Binary Authorization 管控容器
   - 数据加密（静态存储与传输中默认加密）
   - Security Command Center

3. **可靠性（Reliability）**
   - 多可用区与多区域部署
   - 负载均衡与自动扩缩容
   - 灾难恢复规划
   - 混沌工程实践
   - SLI、SLO 与错误预算

4. **成本优化（Cost Optimization）**
   - 承诺使用折扣（Committed Use Discounts）
   - 持续使用折扣（Sustained Use Discounts，自动生效）
   - 抢占式虚拟机（Preemptible VM）与 Spot 虚拟机
   - 用 Recommender 做规格合理化（right-sizing）
   - 用 Active Assist 做优化

5. **性能优化（Performance Optimization）**
   - Cloud CDN 与 Media CDN
   - 缓存策略（Memorystore）
   - 数据库性能调优
   - 网络优化（Premium 层级 vs Standard 层级）
   - 区域级与可用区级资源部署

## 核心服务架构

### 计算

**Compute Engine**
- 机器类型：E2（成本优化）、N2（均衡）、C2（计算优化）、M2（内存优化）
- 可为特定需求自定义机器类型
- 抢占式虚拟机（最高 80% 折扣，最长 24 小时）
- Spot 虚拟机（与抢占式类似，可用性更好）
- 实例组：托管实例组（支持自动扩缩容）与非托管实例组
- 最佳实践：使用最新一代机型、购买承诺使用折扣、批处理任务用 Spot

**Cloud Run**
- 全托管的 Serverless 容器平台
- 可自动缩容到零
- 按请求付费
- 仅在处理请求期间分配 CPU
- 最佳实践：使用无状态容器、优化冷启动、批处理用 Cloud Run jobs

**Cloud Functions**
- 事件驱动的 Serverless 函数
- 第 1 代：HTTP 函数与后台函数
- 第 2 代：构建在 Cloud Run 之上，性能更好
- 事件来源：Pub/Sub、Cloud Storage、Firestore、HTTP
- 最佳实践：使用第 2 代、尽量减少冷启动、实现重试逻辑

**Google Kubernetes Engine (GKE)**
- 与 GCP 深度集成的托管 Kubernetes
- Autopilot 模式：全托管，按 Pod 计费
- Standard 模式：控制力更强，可自行管理节点
- 用 Workload Identity 安全访问 Google 服务
- 用 Binary Authorization 实施部署策略
- 最佳实践：求简用 Autopilot、启用 Workload Identity、配置网络策略

**App Engine**
- 全托管平台（PaaS）
- Standard 环境（沙箱隔离、自动扩缩容）
- Flexible 环境（Docker 容器、自定义运行时）
- 支持流量切分以做金丝雀发布
- 最佳实践：Web 应用用 Standard 环境、有自定义依赖用 Flexible 环境

### 存储

**Cloud Storage**
- 存储类别：Standard、Nearline（30 天）、Coldline（90 天）、Archive（365 天）
- 对象生命周期管理
- 对象版本控制与保留策略
- 用 Autoclass 自动转换存储层级
- 数据传输由请求方付费（Requester Pays）
- 最佳实践：使用 Autoclass、启用版本控制、配置生命周期策略

**Persistent Disk**
- 类型：Standard（HDD）、Balanced SSD、SSD、Extreme
- 可用区级与区域级持久磁盘
- 快照备份（增量式）
- 不停机调整磁盘大小
- 最佳实践：多数工作负载用 Balanced SSD、启用快照

**Filestore**
- 托管的 NFS 文件存储
- 层级：Basic（1-63.9 TB）、Enterprise（1-10 TB，性能更好）
- 可备份到 Cloud Storage
- 最佳实践：生产环境用 Enterprise 层级、落实备份

**Cloud Storage for Firebase**
- 面向移动端与 Web 应用的对象存储
- 客户端 SDK 直接上传/下载
- 用安全规则做访问控制

### 数据库

**Cloud SQL**
- 托管的 MySQL、PostgreSQL、SQL Server
- 高可用配置（区域级）
- 只读副本支撑扩展
- 自动备份与时间点恢复
- 最佳实践：启用高可用、使用只读副本、通过 Cloud SQL Proxy 做连接池

**Cloud Spanner**
- 全球分布式关系型数据库
- 水平扩展同时保持强一致性
- 多区域配置提供 99.999% 可用性
- 用 TrueTime 实现全局一致性
- 最佳实践：合理设计 Schema 拆分、使用提交时间戳、优化热点

**Firestore (Native mode)**
- NoSQL 文档数据库
- 实时同步
- 支持移动端离线使用
- ACID 事务
- 最佳实践：仔细设计文档结构、谨慎使用集合组查询

**Bigtable**
- NoSQL 宽列数据库
- PB 级规模，个位数毫秒延迟
- 兼容 HBase API
- 通过增加节点实现线性扩展
- 最佳实践：设计行键避免热点、用副本实现高可用

**Memorystore**
- 托管的 Redis 与 Memcached
- Standard 层级（带副本的高可用）与 Basic 层级
- 最佳实践：生产环境用 Standard 层级、实现连接池

**BigQuery**
- Serverless 数据仓库
- 对 PB 级数据做 SQL 分析
- 列式存储
- 自动缓存与优化
- 最佳实践：对表做分区与聚簇、使用近似函数、用配额控制成本

### 网络

**VPC (Virtual Private Cloud)**
- 全局资源（子网为区域级）
- 自定义模式或自动模式网络
- 防火墙规则（有状态）
- VPC 对等连接与共享 VPC（Shared VPC）
- 通过 Private Google Access 访问 GCP 服务
- 最佳实践：使用自定义模式 VPC、规划 IP 网段、配置防火墙规则

**Cloud Load Balancing**
- 全局负载均衡（HTTP(S)、TCP/SSL Proxy、外部 TCP/UDP）
- 区域负载均衡（内部 HTTP(S)、内部 TCP/UDP）
- 用 Anycast IP 做全球分发
- 后端服务支持健康检查
- 最佳实践：多区域用全局负载均衡、启用 CDN、配置健康检查

**Cloud CDN**
- 全球内容分发网络
- 缓存失效与签名 URL
- 与 Cloud Storage 及计算服务集成
- 最佳实践：启用压缩、使用 cache-control 响应头

**Cloud Interconnect and VPN**
- 专用互连（Dedicated Interconnect，10 Gbps 或 100 Gbps）
- 合作伙伴互连（Partner Interconnect，50 Mbps 到 50 Gbps）
- Cloud VPN（HA VPN 提供 99.99% SLA）
- 最佳实践：做冗余用 HA VPN、高带宽用 Dedicated Interconnect

**Cloud Armor**
- DDoS 防护与 WAF
- 预配置规则与自定义规则
- 自适应防护（基于 ML）
- 最佳实践：面向互联网的服务启用、使用预配置规则

**Private Service Connect**
- 以私有方式连接 Google API 与服务
- 用 Service Directory 做服务发现
- 最佳实践：生产环境的所有托管服务都使用它

### Serverless 与事件驱动

**Pub/Sub**
- 全球消息队列
- 至少一次（at-least-once）投递
- 推送与拉取两种订阅
- 消息排序与过滤
- 死信主题（dead-letter topics）
- 最佳实践：用消息属性做过滤、实现幂等处理

**Eventarc**
- 事件驱动架构
- 为 Cloud Run、Workflows、GKE 提供触发器
- 事件来源：Audit Logs、Pub/Sub、自定义事件
- 最佳实践：用于解耦架构、实现事件过滤

**Cloud Scheduler**
- 全托管的 cron 服务
- 目标支持 HTTP、Pub/Sub 与 App Engine
- 最佳实践：用于周期性任务、实现重试逻辑

**Workflows**
- 编排并自动化 GCP 与 HTTP 服务
- 基于 YAML 的工作流定义
- 内置错误处理与重试
- 最佳实践：用于复杂多步骤流程、实现补偿事务

### 安全与身份

**Cloud IAM**
- 资源层级：组织（Organization）-> 文件夹（Folder）-> 项目（Project）-> 资源（Resource）
- 角色：基本角色（Primitive：Owner、Editor、Viewer）、预定义角色、自定义角色
- 为应用使用服务账号
- GKE 使用 Workload Identity
- 最佳实践：使用预定义角色、遵循最小权限、应用使用服务账号

**Cloud Key Management (KMS)**
- 加密密钥管理
- 客户自管加密密钥（CMEK）
- 由硬件安全模块（HSM）支撑
- 自动密钥轮换
- 最佳实践：启用自动轮换、每个环境用独立密钥

**Secret Manager**
- 存储 API 密钥、密码、证书
- 版本管理与访问控制
- 集成自动轮换
- 最佳实践：定期轮换密文、用 IAM 做访问控制

**Security Command Center**
- 集中式安全与风险管理
- 资产发现与漏洞扫描
- 威胁检测与合规监控
- 最佳实践：启用全部检测器、定期审查发现的问题

**VPC Service Controls**
- 围绕 GCP 资源创建安全边界
- 防止数据外泄
- 最佳实践：敏感数据使用该功能、配置访问级别

### AI 与机器学习

**Vertex AI**
- 统一的 ML 平台
- 用 AutoML 训练自定义模型
- 预训练模型（Vision、Natural Language 等）
- 用 Pipeline 落地 MLOps
- 最佳实践：快速起步用 AutoML、搭建特征库（feature store）

**BigQuery ML**
- 用 SQL 创建并执行 ML 模型
- 模型类型：线性回归、逻辑回归、聚类等
- 与 Vertex AI 集成
- 最佳实践：简单模型用它、借助 BigQuery 的规模优势

## 架构模式

### 高可用

**多可用区模式**
```
Global HTTP(S) Load Balancer
    |
    v
Managed Instance Group (multi-zone)
    |
    v
Cloud SQL (regional, HA configuration)
    |
    v
Cloud Storage (multi-region)
```

**多区域模式**
```
Global HTTP(S) Load Balancer
    |
    ├── Backend Service Region 1 (Cloud Run)
    └── Backend Service Region 2 (Cloud Run)
         |
         v
    Cloud Spanner (multi-region)
```

### Serverless 架构

**事件驱动模式**
```
Cloud Storage upload event
    |
    v
Pub/Sub topic
    |
    v
Cloud Functions (image processing)
    |
    v
Firestore (metadata storage)
```

**API 优先模式**
```
Cloud Endpoints or API Gateway
    |
    v
Cloud Run (multiple services)
    |
    ├── Cloud SQL (transactional data)
    └── Firestore (user data)
```

### GKE 上的微服务

**GKE 与服务网格（Service Mesh）**
```
Global Load Balancer
    |
    v
GKE Ingress
    |
    v
Anthos Service Mesh (Istio)
    |
    v
Microservices (Cloud Spanner, Firestore, Memorystore)
```

### 数据分析平台

```
Data Sources
    |
    v
Pub/Sub (streaming)
    |
    v
Dataflow (Apache Beam)
    |
    v
BigQuery (data warehouse)
    |
    v
Looker or Data Studio (visualization)
```

**批处理**
```
Cloud Storage (raw data)
    |
    v
Dataproc (Apache Spark)
    |
    v
BigQuery (analytics)
```

## Landing Zone 设计

### 资源层级

```
Organization
├── Folders (by environment or team)
│   ├── Production Folder
│   │   ├── Project A
│   │   └── Project B
│   ├── Staging Folder
│   └── Development Folder
└── Shared Services Folder
    ├── Networking Project (Shared VPC host)
    ├── Security Project (KMS, Secret Manager)
    └── Logging Project (centralized logs)
```

### 网络设计

**共享 VPC（Shared VPC）模式**
```
Host Project (networking team)
├── Shared VPC
│   ├── Subnet Production (region A)
│   ├── Subnet Staging (region A)
│   └── Subnet Development (region B)

Service Projects (application teams)
├── Production Project (uses Production subnet)
├── Staging Project (uses Staging subnet)
└── Development Project (uses Development subnet)
```

**基于 VPN 的中心辐射（Hub-and-Spoke）模式**
```
On-premises Network
    |
    v
Cloud VPN / Interconnect
    |
    v
Hub VPC (shared services)
    |
    ├── Spoke VPC 1 (production workloads)
    ├── Spoke VPC 2 (development workloads)
    └── Spoke VPC 3 (analytics workloads)
```

### 治理

**组织政策（Organization Policies）**
- 限制公网 IP 分配
- 强制统一的存储桶级访问控制
- 限制虚拟机外部 IP
- 定义允许的资源位置

**IAM 策略**
- 用 Google 群组做角色分配
- 职责分离（网络管理员、安全管理员等）
- 每个应用独立服务账号
- GKE 工作负载使用 Workload Identity

**日志与监控**
```
All Projects
    |
    v
Log Router
    |
    ├── Cloud Logging (default sink)
    ├── BigQuery (long-term analysis)
    ├── Cloud Storage (archive)
    └── Pub/Sub (real-time processing)
```

## 迁移策略

### 虚拟机迁移（Migrate to Virtual Machines）

**工具**
- Migrate to Virtual Machines（前身为 Migrate for Compute Engine）
- 支持 VMware、AWS、Azure、物理服务器
- 无代理（agentless）或基于代理（agent-based）的迁移
- 分批（wave）迁移与测试克隆

**流程**
1. 评估：适配性评估与 TCO 分析
2. 计划：虚拟机分组、定义迁移批次
3. 部署：搭建基础设施（VPC、防火墙规则）
4. 迁移：测试迁移、正式切换（cutover）、验证
5. 优化：规格合理化（right-sizing）、承诺使用折扣

### 数据库迁移

**Database Migration Service**
- 最小停机时间迁移
- 支持 MySQL、PostgreSQL、SQL Server、Oracle
- 持续复制，切换时机可灵活选择

**Transfer Appliance**
- 用于超大规模数据传输的物理设备
- 容量最高 1 PB
- 离线数据传输

## 成本优化

### 计算成本节省

**承诺使用折扣（Committed Use Discounts）**
- 1 年或 3 年承诺
- 虚拟机最高省 57%
- 按资源承诺或按消费金额承诺

**持续使用折扣（Sustained Use Discounts）**
- 虚拟机当月运行超过 25% 时长即自动享受折扣
- 最高省 30%
- 无需任何承诺

**抢占式虚拟机与 Spot 虚拟机**
- 最高 80% 折扣
- 可能被 GCP 随时终止
- 最适合批处理、容错型工作负载

**Recommender**
- 虚拟机规格合理化建议
- 识别闲置资源
- 承诺使用折扣购买建议

### 存储成本节省

**Cloud Storage**
- 用 Autoclass 自动转换存储层级
- 生命周期策略（删除或转换存储类别）
- Nearline（30 天以上）、Coldline（90 天以上）、Archive（365 天以上）
- 数据传输由请求方付费（Requester Pays）

**Persistent Disk**
- 删除孤立磁盘
- 尽量用 Balanced SSD 替代 SSD
- 按实际用量调整磁盘大小

### BigQuery 成本节省

**按需定价（On-Demand Pricing）**
- 每处理 1 TB 计费 $5
- 使用分区与聚簇
- 重复查询命中查询缓存，不收费

**固定费率定价（Flat-Rate Pricing）**
- 重度用户成本可预期
- 提供自动扩缩容的槽位（slot）
- Flex slots 适合短期承诺

**最佳实践**
- 使用近似聚合函数（APPROX_COUNT_DISTINCT）
- 避免 SELECT *，明确指定列
- 常用查询用物化视图
- 用自定义配额设置成本控制

### 成本监控

**Cloud Billing**
- 预算与告警
- 按项目、服务、SKU 细分成本
- 导出到 BigQuery 做分析
- 来自 Active Assist 的优化建议

## 灾难恢复

### 备份策略

**虚拟机备份**
- 持久磁盘快照（增量式）
- 机器映像（包含元数据与配置）
- 跨区域复制快照
- 用快照计划实现自动化

**数据库备份**
- Cloud SQL：自动备份（保留 7-365 天）
- Cloud Spanner：按需备份或定时备份
- Firestore：每日自动导出
- Bigtable：备份到 Cloud Storage

### 高可用

**RTO/RPO 矩阵**

| 模式 | RPO | RTO | 成本 |
|---------|-----|-----|------|
| 双活多区域（Active-Active Multi-Region） | 秒级 | 秒级 | 高 |
| 带副本的主备（Active-Passive with Replication） | 分钟级 | 分钟级 | 中 |
| 温备（Warm Standby） | 分钟级 | 10-30 分钟 | 中 |
| 备份恢复（Backup and Restore） | 小时级 | 小时级 | 低 |

**Cloud SQL 高可用**
- 区域级配置，同步复制
- 自动故障转移
- 99.95% SLA（单可用区为 99.5%）

**Cloud Spanner**
- 多区域配置
- 99.999% 可用性 SLA
- 跨区域同步复制

### 灾难恢复演练

- 定期 DR 演练（建议每季度一次）
- 编写运维手册（runbook）
- 测试恢复流程
- 对比目标度量实际 RTO/RPO

## 监控与可观测性

### Cloud Monitoring（前身为 Stackdriver）

**指标**
- 系统指标（CPU、内存、磁盘、网络）
- 通过 Cloud Monitoring API 定义自定义指标
- 用 Metric Scope 做跨项目监控
- 用 Uptime Check 检测可用性

**仪表盘与图表**
- GCP 服务自带预定义仪表盘
- 支持过滤与分组的自定义仪表盘
- 基于 SLO 与错误预算的监控

### Cloud Logging

**日志类型**
- 管理活动日志（始终启用，不收费）
- 数据访问日志（需手动启用）
- 系统事件日志
- 访问透明度日志（记录 Google 方的访问）

**日志接收器（Sink）**
- 将日志路由到 BigQuery、Cloud Storage、Pub/Sub
- 组织/文件夹级别的聚合 Sink
- 用排除过滤器降低成本

### Cloud Trace

**分布式追踪**
- App Engine、Cloud Run、GKE 自动插桩
- 用客户端库手动插桩
- 延迟分析与性能洞察
- 与 Zipkin 集成

### Cloud Profiler

**持续性能剖析**
- CPU 与内存剖析
- 开销低（CPU 占用 < 0.5%）
- 用火焰图做可视化
- 支持语言：Java、Go、Python、Node.js

### Error Reporting

**聚合的错误跟踪**
- 自动错误分组
- 堆栈跟踪分析
- 与 Cloud Logging 集成
- 出现新错误时通知
