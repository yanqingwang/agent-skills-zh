> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/developer/quality/kubernetes-specialist/references/service-mesh.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Service Mesh

---

## Istio 安装

```bash
# Install Istio CLI
curl -L https://istio.io/downloadIstio | sh -
export PATH=$PWD/istio-*/bin:$PATH

# Install Istio with default profile
istioctl install --set profile=default -y

# Enable sidecar injection for namespace
kubectl label namespace production istio-injection=enabled

# Verify installation
istioctl verify-install
kubectl get pods -n istio-system
```

## Istio Profiles

```bash
# Minimal - only control plane
istioctl install --set profile=minimal

# Default - control plane + ingress gateway
istioctl install --set profile=default

# Demo - includes egress gateway, extra features
istioctl install --set profile=demo

# Production - tuned for production
istioctl install --set profile=default \
  --set values.global.proxy.resources.requests.cpu=100m \
  --set values.global.proxy.resources.requests.memory=128Mi \
  --set values.global.proxy.resources.limits.cpu=500m \
  --set values.global.proxy.resources.limits.memory=256Mi
```

## VirtualService

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: myapp
  namespace: production
spec:
  hosts:
    - myapp
    - myapp.example.com
  gateways:
    - mesh                    # Internal mesh traffic
    - myapp-gateway           # External gateway
  http:
    # Route based on headers
    - match:
        - headers:
            x-version:
              exact: "v2"
      route:
        - destination:
            host: myapp
            subset: v2

    # Canary release (90/10 split)
    - match:
        - uri:
            prefix: /api
      route:
        - destination:
            host: myapp
            subset: v1
          weight: 90
        - destination:
            host: myapp
            subset: v2
          weight: 10

    # Default route
    - route:
        - destination:
            host: myapp
            subset: v1
      timeout: 30s
      retries:
        attempts: 3
        perTryTimeout: 10s
        retryOn: connect-failure,refused-stream,503
```

## DestinationRule

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: myapp
  namespace: production
spec:
  host: myapp
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
        connectTimeout: 5s
      http:
        h2UpgradePolicy: UPGRADE
        http1MaxPendingRequests: 100
        http2MaxRequests: 1000
        maxRequestsPerConnection: 100
    loadBalancer:
      simple: LEAST_REQUEST
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 10s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
  subsets:
    - name: v1
      labels:
        version: v1
      trafficPolicy:
        loadBalancer:
          simple: ROUND_ROBIN
    - name: v2
      labels:
        version: v2
```

## Gateway

```yaml
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
  name: myapp-gateway
  namespace: production
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 80
        name: http
        protocol: HTTP
      hosts:
        - myapp.example.com
      tls:
        httpsRedirect: true
    - port:
        number: 443
        name: https
        protocol: HTTPS
      hosts:
        - myapp.example.com
      tls:
        mode: SIMPLE
        credentialName: myapp-tls-secret
```

## 流量镜像（影子流量）

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: myapp-mirror
  namespace: production
spec:
  hosts:
    - myapp
  http:
    - route:
        - destination:
            host: myapp
            subset: v1
      mirror:
        host: myapp
        subset: v2
      mirrorPercentage:
        value: 100.0
```

## mTLS 配置

```yaml
# Strict mTLS for namespace
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: production
spec:
  mtls:
    mode: STRICT
---
# Per-workload mTLS
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: legacy-service
  namespace: production
spec:
  selector:
    matchLabels:
      app: legacy-service
  mtls:
    mode: PERMISSIVE  # Allow both mTLS and plaintext
---
# Mesh-wide mTLS policy
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: istio-system
spec:
  mtls:
    mode: STRICT
```

## 授权策略

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: myapp-authz
  namespace: production
spec:
  selector:
    matchLabels:
      app: myapp
  action: ALLOW
  rules:
    # Allow from specific service accounts
    - from:
        - source:
            principals:
              - "cluster.local/ns/production/sa/frontend"
              - "cluster.local/ns/production/sa/api-gateway"
      to:
        - operation:
            methods: ["GET", "POST"]
            paths: ["/api/*"]

    # Allow health checks from anywhere
    - to:
        - operation:
            methods: ["GET"]
            paths: ["/health", "/ready"]

    # Deny all other traffic (implicit deny when rules exist)
```

## 熔断器

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: myapp-circuit-breaker
  namespace: production
spec:
  host: myapp
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 50
      http:
        http1MaxPendingRequests: 100
        http2MaxRequests: 100
        maxRequestsPerConnection: 10
    outlierDetection:
      consecutive5xxErrors: 3
      interval: 10s
      baseEjectionTime: 30s
      maxEjectionPercent: 100
      minHealthPercent: 0
```

## 故障注入（测试）

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: myapp-fault
  namespace: production
spec:
  hosts:
    - myapp
  http:
    - match:
        - headers:
            x-test-fault:
              exact: "inject"
      fault:
        delay:
          percentage:
            value: 50
          fixedDelay: 5s
        abort:
          percentage:
            value: 10
          httpStatus: 503
      route:
        - destination:
            host: myapp
    - route:
        - destination:
            host: myapp
```

## Linkerd 安装

```bash
# Install Linkerd CLI
curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/install | sh
export PATH=$HOME/.linkerd2/bin:$PATH

# Validate cluster
linkerd check --pre

# Install CRDs
linkerd install --crds | kubectl apply -f -

# Install control plane
linkerd install | kubectl apply -f -

# Check installation
linkerd check

# Enable injection for namespace
kubectl annotate namespace production linkerd.io/inject=enabled

# Inject existing deployments
kubectl get deploy -n production -o yaml | linkerd inject - | kubectl apply -f -
```

## Linkerd Service Profile

```yaml
apiVersion: linkerd.io/v1alpha2
kind: ServiceProfile
metadata:
  name: myapp.production.svc.cluster.local
  namespace: production
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
      timeout: 5s

    - name: POST /api/orders
      condition:
        method: POST
        pathRegex: /api/orders
      isRetryable: true
      timeout: 10s

  retryBudget:
    retryRatio: 0.2
    minRetriesPerSecond: 10
    ttl: 10s
```

## Linkerd 流量拆分（金丝雀）

```yaml
apiVersion: split.smi-spec.io/v1alpha1
kind: TrafficSplit
metadata:
  name: myapp-canary
  namespace: production
spec:
  service: myapp
  backends:
    - service: myapp-v1
      weight: 900m    # 90%
    - service: myapp-v2
      weight: 100m    # 10%
```

## 多集群网格（Istio）

```yaml
# Primary cluster - create remote secret
istioctl x create-remote-secret \
  --context=cluster1 \
  --name=cluster1 | kubectl apply -f - --context=cluster2

# Enable endpoint discovery
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  values:
    global:
      meshID: mesh1
      multiCluster:
        clusterName: cluster1
      network: network1
```

## Kiali 仪表盘

```bash
# Install Kiali
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.20/samples/addons/kiali.yaml

# Access dashboard
istioctl dashboard kiali
```

## Jaeger 链路追踪

```bash
# Install Jaeger
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.20/samples/addons/jaeger.yaml

# Access dashboard
istioctl dashboard jaeger
```

## Service Mesh 对比

| 特性 | Istio | Linkerd |
|---------|-------|---------|
| Sidecar | Envoy | linkerd2-proxy（Rust） |
| 资源占用 | 较高 | 较低 |
| 功能 | 更丰富 | 聚焦、更简洁 |
| mTLS | 内置 | 内置 |
| 流量管理 | 高级 | 基础（SMI） |
| 多集群 | 原生支持 | 需额外配置 |
| 学习曲线 | 较陡 | 较平缓 |

## 最佳实践

1. **从宽松 mTLS 起步**，逐步迁到严格模式
2. **用熔断器**：防止级联故障
3. **设合理超时**与重试预算
4. **启用分布式追踪**：提升可观测性
5. **上线前用故障注入测试**
6. **监控 sidecar 资源占用**并据此调优
7. **用流量镜像**：安全地验证新版本
8. **实施授权策略**：落实零信任
9. **保持 service mesh 版本更新**：及时打安全补丁
10. **在 VirtualService 里记录流量路由决策**
