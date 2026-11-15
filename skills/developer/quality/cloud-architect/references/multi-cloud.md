> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/cloud-architect/references/multi-cloud.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 多云架构参考

涵盖多云策略、抽象层、可移植模式与厂商锁定缓解的完整指南。

## 多云策略

### 何时使用多云

**合理场景**
- 法规合规要求特定区域的数据驻留
- 择优选择服务（分析用 BigQuery，机器学习用 AWS）
- 并购整合（合并后的组织各自使用不同的云）
- 灾难恢复，把云厂商当作故障域
- 作为与云厂商谈判的筹码

**不适合多云的理由**
- 没有具体退出场景就谈"避免厂商锁定"
- 以为可移植性免费（实际成本很高）
- 缺乏技术依据的政治性决策
- 在各厂商间随意分散工作负载

### 多云模式

**双活（Active-Active）**
```
Users -> Global Load Balancer
              |
    +---------+---------+
    |                   |
  AWS Region        GCP Region
    |                   |
    +----> Data Sync <--+
```
- 复杂度和成本最高
- 最适合全球延迟优化
- 需要可靠的数据同步

**主备（Active-Passive，DR）**
```
Users -> Primary (AWS)
              |
         [Failover]
              |
         Secondary (Azure)
```
- 复杂度低于双活
- 云厂商成为故障域
- 备云中冷备或温备

**按工作负载切分**
```
Analytics -> GCP (BigQuery)
Core App  -> AWS (ECS, RDS)
Office    -> Azure (M365 integration)
```
- 每个工作负载放在最合适的云上
- 无跨云数据同步
- 最简单的多云模式

## 抽象层

### 基础设施抽象

**Terraform（推荐）**
```hcl
# Provider-agnostic module structure
module "compute" {
  source = "./modules/compute"

  provider_type = var.cloud_provider  # aws, azure, gcp
  instance_type = var.instance_size
  region        = var.region
}

# Provider-specific implementations
# modules/compute/aws.tf
resource "aws_instance" "main" {
  count         = var.provider_type == "aws" ? 1 : 0
  ami           = data.aws_ami.latest.id
  instance_type = local.aws_instance_map[var.instance_size]
}

# modules/compute/azure.tf
resource "azurerm_virtual_machine" "main" {
  count    = var.provider_type == "azure" ? 1 : 0
  vm_size  = local.azure_vm_map[var.instance_size]
}
```

**Pulumi（代码优先）**
```typescript
// Abstract cloud resources with TypeScript
interface ComputeConfig {
  size: "small" | "medium" | "large";
  region: string;
}

function createCompute(config: ComputeConfig, provider: "aws" | "gcp") {
  if (provider === "aws") {
    return new aws.ec2.Instance("web", {
      instanceType: sizeMap.aws[config.size],
      // ...
    });
  } else {
    return new gcp.compute.Instance("web", {
      machineType: sizeMap.gcp[config.size],
      // ...
    });
  }
}
```

### 容器编排（Kubernetes）

**可移植的 Kubernetes 部署**
```yaml
# Same manifests work across EKS, AKS, GKE
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    spec:
      containers:
      - name: web
        image: myregistry/web:v1
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

**云特定注意事项**
| 特性 | EKS | AKS | GKE |
|---------|-----|-----|-----|
| 负载均衡 | ALB/NLB 注解 | Azure LB | GCP LB |
| 存储类 | gp3, io2 | managed-premium | pd-ssd |
| IAM 集成 | IRSA | Workload Identity | Workload Identity |
| Ingress | AWS ALB Controller | AGIC | GKE Ingress |

### 应用抽象

**数据库抽象**
```python
# Use standard protocols (SQL, Redis, S3 API)
from sqlalchemy import create_engine

# Same code works with:
# - AWS RDS PostgreSQL
# - Azure Database for PostgreSQL
# - GCP Cloud SQL PostgreSQL
# - Self-managed PostgreSQL

DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_engine(DATABASE_URL)
```

**对象存储抽象**
```python
import boto3
from botocore.config import Config

# S3-compatible API works with:
# - AWS S3
# - GCP Cloud Storage (interoperability mode)
# - MinIO
# - Cloudflare R2

s3_client = boto3.client(
    's3',
    endpoint_url=os.environ.get("S3_ENDPOINT"),  # Override for non-AWS
    aws_access_key_id=os.environ["ACCESS_KEY"],
    aws_secret_access_key=os.environ["SECRET_KEY"],
)
```

## 数据同步

### 数据库复制

**跨云 PostgreSQL**
```
AWS RDS Primary
      |
      | Logical Replication
      v
GCP Cloud SQL Replica (read-only)
```

配置：
```sql
-- On primary (AWS RDS)
CREATE PUBLICATION my_publication FOR ALL TABLES;

-- On replica (GCP Cloud SQL)
CREATE SUBSCRIPTION my_subscription
  CONNECTION 'host=aws-rds-endpoint dbname=mydb user=repl'
  PUBLICATION my_publication;
```

**冲突解决策略**
- 最后写入胜出（基于时间戳）
- 应用层冲突解决
- 最终一致数据使用 CRDT 数据结构
- 事务型数据避免多主

### 对象存储同步

**用 Rclone 做跨云同步**
```bash
# Sync S3 to GCS
rclone sync s3:my-bucket gcs:my-bucket \
  --transfers 32 \
  --checkers 16 \
  --s3-upload-concurrency 8

# Bidirectional sync with conflict handling
rclone bisync s3:bucket gcs:bucket \
  --conflict-resolve newer
```

**事件驱动复制**
```
S3 Bucket -> S3 Event -> Lambda -> GCS Upload
                              |
                              v
                       Consistency Check
```

## 厂商锁定缓解

### 锁定风险评估

| 服务类型 | 锁定风险 | 缓解策略 |
|--------------|--------------|---------------------|
| 计算（VM） | 低 | 标准 OS 镜像、IaC |
| Kubernetes | 低 | 可移植清单，避免专有插件 |
| 对象存储 | 低 | S3 兼容 API、标准格式 |
| 托管数据库 | 中 | 标准 SQL、逻辑备份 |
| Serverless 函数 | 高 | 抽象层、容器 |
| 专有 AI/ML | 高 | 开源替代、ONNX 模型 |
| 托管服务 | 高 | 采用前先评估可移植性 |

### 缓解策略

**1. 使用开放标准**
- SQL 数据库优先于专有 NoSQL
- Kubernetes 优先于 ECS/Cloud Run
- 对象存储用 S3 API
- 可观测性用 OpenTelemetry
- 认证用 OIDC

**2. 抽象专有服务**
```typescript
// Wrap cloud-specific services
interface QueueService {
  send(message: string): Promise<void>;
  receive(): Promise<string>;
}

class SQSQueue implements QueueService {
  async send(message: string) {
    await this.sqsClient.sendMessage({ QueueUrl: this.url, MessageBody: message });
  }
}

class PubSubQueue implements QueueService {
  async send(message: string) {
    await this.pubsubClient.topic(this.topic).publish(Buffer.from(message));
  }
}

// Factory pattern for cloud selection
function createQueue(provider: string): QueueService {
  switch (provider) {
    case "aws": return new SQSQueue();
    case "gcp": return new PubSubQueue();
  }
}
```

**3. 保持退出能力**
- 定期测试数据导出
- 记录云特有依赖
- IaC 保持跨厂商可移植
- 每年估算迁移工作量

**4. 一切容器化**
```dockerfile
# Portable container runs anywhere
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

## 网络连通

### 跨云网络

**VPN 互联**
```
AWS VPC                          GCP VPC
   |                                |
   +---> AWS VPN Gateway            |
              |                     |
              | IPsec tunnel        |
              |                     |
              +---> GCP Cloud VPN <-+
```

**专线互联（企业级）**
```
On-Premises Data Center
         |
    +----+----+
    |         |
AWS Direct  GCP Cloud
Connect     Interconnect
    |         |
    v         v
AWS VPC    GCP VPC
    |         |
    +----+----+
         |
    Transit Hub (e.g., Megaport, Equinix)
```

### 跨云服务网格

**Istio 多集群**
```yaml
# Primary cluster (AWS EKS)
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  values:
    global:
      meshID: multi-cloud-mesh
      multiCluster:
        clusterName: eks-primary
      network: aws-network

# Remote cluster (GCP GKE)
spec:
  values:
    global:
      meshID: multi-cloud-mesh
      multiCluster:
        clusterName: gke-secondary
      network: gcp-network
```

## 成本管理

### 跨云成本可见性

**FinOps 工具**
- VMware 的 CloudHealth
- Apptio Cloudability
- Spot.io（现属 NetApp）
- Kubernetes 用 Kubecost

**统一打标策略**
```
Required Tags (all clouds):
- environment: prod/staging/dev
- cost-center: engineering/marketing/sales
- owner: team-name
- project: project-code
- managed-by: terraform/manual
```

### 成本对比框架

```
| Workload Type | AWS | Azure | GCP | Decision |
|---------------|-----|-------|-----|----------|
| General Compute | EC2 m5 | D-series | n2-standard | Compare $/vCPU/hour |
| GPU Training | p4d | NC-series | A2 | GCP often cheaper |
| Object Storage | S3 | Blob | GCS | Similar, check egress |
| Analytics | Redshift | Synapse | BigQuery | BigQuery for ad-hoc |
| Kubernetes | EKS | AKS | GKE | GKE Autopilot simplest |
```

## 可观测性

### 统一监控栈

**OpenTelemetry Collector**
```yaml
# Collect from all clouds, export to single backend
receivers:
  otlp:
    protocols:
      grpc:
      http:

processors:
  batch:
  attributes:
    actions:
      - key: cloud.provider
        action: upsert
        value: ${CLOUD_PROVIDER}

exporters:
  prometheus:
    endpoint: "0.0.0.0:8889"
  jaeger:
    endpoint: jaeger:14250

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch, attributes]
      exporters: [jaeger]
    metrics:
      receivers: [otlp]
      processors: [batch, attributes]
      exporters: [prometheus]
```

**用 Grafana 做统一仪表盘**
- AWS CloudWatch 数据源
- Azure Monitor 数据源
- GCP Cloud Monitoring 数据源
- 所有云的单一视图

## 安全考量

### 身份联合

**跨云身份**
```
Corporate IdP (Okta/Azure AD)
         |
    SAML/OIDC
         |
    +----+----+----+
    |    |    |    |
  AWS  Azure  GCP  K8s
  IAM   AD   IAM  RBAC
```

### 密钥管理

**HashiCorp Vault（云无关）**
```hcl
# Single secrets management across clouds
resource "vault_aws_secret_backend_role" "aws_role" {
  backend = vault_aws_secret_backend.aws.path
  name    = "app-role"
  credential_type = "iam_user"
}

resource "vault_gcp_secret_roleset" "gcp_role" {
  backend     = vault_gcp_secret_backend.gcp.path
  roleset     = "app-role"
  project     = var.gcp_project
  token_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
}
```

### 网络安全

**跨云零信任**
- 所有服务间使用 mTLS（服务网格）
- 不基于网络位置给予隐式信任
- 基于身份的访问控制
- 云间传输加密（VPN/专线）
