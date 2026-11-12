---
name: linkerd-patterns
description: 实现 Linkerd 服务网格的各类模式，适用于轻量级、以安全为核心的服务网格部署。在搭建 Linkerd、配置流量策略，或以最小开销实现零信任网络时使用。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/cloud-infrastructure/skills/linkerd-patterns/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Linkerd 模式

Linkerd 是面向 Kubernetes 的轻量级、安全优先的服务网格，本文给出其生产级使用模式。

## 何时使用本 Skill

- 搭建轻量级服务网格
- 实现自动 mTLS
- 为金丝雀发布配置流量拆分
- 配置 ServiceProfile 以获取按路由的指标
- 实现重试与超时
- 多集群服务网格

## 核心概念

### 1. Linkerd 架构


```
┌─────────────────────────────────────────────┐
│                Control Plane                 │
│  ┌─────────┐ ┌──────────┐ ┌──────────────┐ │
│  │ destiny │ │ identity │ │ proxy-inject │ │
│  └─────────┘ └──────────┘ └──────────────┘ │
└─────────────────────────────────────────────┘
                      │
┌─────────────────────────────────────────────┐
│                 Data Plane                   │
│  ┌─────┐    ┌─────┐    ┌─────┐             │
│  │proxy│────│proxy│────│proxy│             │
│  └─────┘    └─────┘    └─────┘             │
│     │           │           │               │
│  ┌──┴──┐    ┌──┴──┐    ┌──┴──┐            │
│  │ app │    │ app │    │ app │            │
│  └─────┘    └─────┘    └─────┘            │
└─────────────────────────────────────────────┘
```


### 2. 关键资源

| 资源                    | 用途                         |
| ----------------------- | ------------------------------------ |
| **ServiceProfile**      | 按路由的指标、重试、超时     |
| **TrafficSplit**        | 金丝雀发布、A/B 测试         |
| **Server**              | 定义服务端策略               |
| **ServerAuthorization** | 访问控制策略                 |

## 模板

### 模板 1：网格安装

使用与目标集群兼容的 CLI 版本。示例采用 Homebrew；
其他系统请参考[官方安装指南](https://linkerd.io/docs/getting-started/)。


```bash
# Install the CLI with Homebrew
brew install linkerd
linkerd version

# Validate cluster
linkerd check --pre

# Install CRDs
linkerd install --crds | kubectl apply -f -

# Install control plane
linkerd install | kubectl apply -f -

# Verify installation
linkerd check

# Install viz extension (optional)
linkerd viz install | kubectl apply -f -
```


### 模板 2：注入命名空间


```yaml
# Automatic injection for namespace
apiVersion: v1
kind: Namespace
metadata:
  name: my-app
  annotations:
    linkerd.io/inject: enabled
---
# Or inject specific deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  annotations:
    linkerd.io/inject: enabled
spec:
  template:
    metadata:
      annotations:
        linkerd.io/inject: enabled
```


### 模板 3：带重试的 ServiceProfile


```yaml
apiVersion: linkerd.io/v1alpha2
kind: ServiceProfile
metadata:
  name: my-service.my-namespace.svc.cluster.local
  namespace: my-namespace
spec:
  routes:
    - name: GET /api/users
      condition:
        method: GET
        pathRegex: /api/users
      responseClasses:
        - condition:
            status:
              min: 500
              max: 599
          isFailure: true
      isRetryable: true
    - name: POST /api/users
      condition:
        method: POST
        pathRegex: /api/users
      # POST not retryable by default
      isRetryable: false
    - name: GET /api/users/{id}
      condition:
        method: GET
        pathRegex: /api/users/[^/]+
      timeout: 5s
      isRetryable: true
  retryBudget:
    retryRatio: 0.2
    minRetriesPerSecond: 10
    ttl: 10s
```


### 模板 4：流量拆分（金丝雀）


```yaml
apiVersion: split.smi-spec.io/v1alpha1
kind: TrafficSplit
metadata:
  name: my-service-canary
  namespace: my-namespace
spec:
  service: my-service
  backends:
    - service: my-service-stable
      weight: 900m # 90%
    - service: my-service-canary
      weight: 100m # 10%
```


### 模板 5：Server 授权策略


```yaml
# Define the server
apiVersion: policy.linkerd.io/v1beta1
kind: Server
metadata:
  name: my-service-http
  namespace: my-namespace
spec:
  podSelector:
    matchLabels:
      app: my-service
  port: http
  proxyProtocol: HTTP/1
---
# Allow traffic from specific clients
apiVersion: policy.linkerd.io/v1beta1
kind: ServerAuthorization
metadata:
  name: allow-frontend
  namespace: my-namespace
spec:
  server:
    name: my-service-http
  client:
    meshTLS:
      serviceAccounts:
        - name: frontend
          namespace: my-namespace
---
# Allow unauthenticated traffic (e.g., from ingress)
apiVersion: policy.linkerd.io/v1beta1
kind: ServerAuthorization
metadata:
  name: allow-ingress
  namespace: my-namespace
spec:
  server:
    name: my-service-http
  client:
    unauthenticated: true
    networks:
      - cidr: 10.0.0.0/8
```


### 模板 6：用于高级路由的 HTTPRoute


```yaml
apiVersion: policy.linkerd.io/v1beta2
kind: HTTPRoute
metadata:
  name: my-route
  namespace: my-namespace
spec:
  parentRefs:
    - name: my-service
      kind: Service
      group: core
      port: 8080
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/v2
        - headers:
            - name: x-api-version
              value: v2
      backendRefs:
        - name: my-service-v2
          port: 8080
    - matches:
        - path:
            type: PathPrefix
            value: /api
      backendRefs:
        - name: my-service-v1
          port: 8080
```


### 模板 7：多集群配置


```bash
# On each cluster, install with cluster credentials
linkerd multicluster install | kubectl apply -f -

# Link clusters
linkerd multicluster link --cluster-name west \
  --api-server-address https://west.example.com:6443 \
  | kubectl apply -f -

# Export a service to other clusters
kubectl label svc/my-service mirror.linkerd.io/exported=true

# Verify cross-cluster connectivity
linkerd multicluster check
linkerd multicluster gateways
```


## 监控命令


```bash
# Live traffic view
linkerd viz top deploy/my-app

# Per-route metrics
linkerd viz routes deploy/my-app

# Check proxy status
linkerd viz stat deploy -n my-namespace

# View service dependencies
linkerd viz edges deploy -n my-namespace

# Dashboard
linkerd viz dashboard
```


## 调试


```bash
# Check injection status
linkerd check --proxy -n my-namespace

# View proxy logs
kubectl logs deploy/my-app -c linkerd-proxy

# Debug identity/TLS
linkerd identity -n my-namespace

# Tap traffic (live)
linkerd viz tap deploy/my-app --to deploy/my-backend
```


## 最佳实践

### 推荐做法

- **在所有位置启用 mTLS**，Linkerd 会自动完成
- **使用 ServiceProfiles**，获取按路由的指标与重试
- **设置重试预算**，避免重试风暴
- **监控黄金指标**，即成功率、延迟、吞吐量

### 应避免的做法

- **不要跳过检查**，每次变更后都要运行 `linkerd check`
- **不要过度配置**，Linkerd 的默认值已足够合理
- **不要忽略 ServiceProfiles**，它们能解锁高级特性
- **不要忘记超时**，按路由设置合适的取值
