---
name: istio-traffic-management
description: 配置 Istio 流量管理，涵盖路由、负载均衡、熔断器与金丝雀部署。适用于实现服务网格流量策略、渐进式交付或弹性模式的场景。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/cloud-infrastructure/skills/istio-traffic-management/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Istio 流量管理

面向生产环境服务网格部署的 Istio 流量管理综合指南。

## 何时使用本 Skill

- 配置服务间路由
- 实现金丝雀或蓝绿部署
- 设置熔断器与重试
- 负载均衡配置
- 用于测试的流量镜像
- 用于混沌工程的故障注入

## 核心概念

### 1. 流量管理资源

| 资源            | 用途                       | 作用域         |
| ------------------- | ----------------------------- | ------------- |
| **VirtualService**  | 将流量路由到目标 | 基于主机    |
| **DestinationRule** | 定义路由后的策略 | 基于服务 |
| **Gateway**         | 配置入口/出口流量      | 集群边缘  |
| **ServiceEntry**    | 添加外部服务         | 网格范围     |

### 2. 流量流程


```
Client → Gateway → VirtualService → DestinationRule → Service
                   (routing)        (policies)        (pods)
```


## 模板

### 模板 1：基础路由


```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: reviews-route
  namespace: bookinfo
spec:
  hosts:
    - reviews
  http:
    - match:
        - headers:
            end-user:
              exact: jason
      route:
        - destination:
            host: reviews
            subset: v2
    - route:
        - destination:
            host: reviews
            subset: v1
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: reviews-destination
  namespace: bookinfo
spec:
  host: reviews
  subsets:
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
    - name: v3
      labels:
        version: v3
```


### 模板 2：金丝雀部署


```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: my-service-canary
spec:
  hosts:
    - my-service
  http:
    - route:
        - destination:
            host: my-service
            subset: stable
          weight: 90
        - destination:
            host: my-service
            subset: canary
          weight: 10
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: my-service-dr
spec:
  host: my-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        h2UpgradePolicy: UPGRADE
        http1MaxPendingRequests: 100
        http2MaxRequests: 1000
  subsets:
    - name: stable
      labels:
        version: stable
    - name: canary
      labels:
        version: canary
```


### 模板 3：熔断器


```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: circuit-breaker
spec:
  host: my-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http1MaxPendingRequests: 100
        http2MaxRequests: 1000
        maxRequestsPerConnection: 10
        maxRetries: 3
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 30s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
      minHealthPercent: 30
```


### 模板 4：重试与超时


```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: ratings-retry
spec:
  hosts:
    - ratings
  http:
    - route:
        - destination:
            host: ratings
      timeout: 10s
      retries:
        attempts: 3
        perTryTimeout: 3s
        retryOn: connect-failure,refused-stream,unavailable,cancelled,retriable-4xx,503
        retryRemoteLocalities: true
```


### 模板 5：流量镜像


```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: mirror-traffic
spec:
  hosts:
    - my-service
  http:
    - route:
        - destination:
            host: my-service
            subset: v1
      mirror:
        host: my-service
        subset: v2
      mirrorPercentage:
        value: 100.0
```


### 模板 6：故障注入


```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: fault-injection
spec:
  hosts:
    - ratings
  http:
    - fault:
        delay:
          percentage:
            value: 10
          fixedDelay: 5s
        abort:
          percentage:
            value: 5
          httpStatus: 503
      route:
        - destination:
            host: ratings
```


### 模板 7：入口网关


```yaml
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
  name: my-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 443
        name: https
        protocol: HTTPS
      tls:
        mode: SIMPLE
        credentialName: my-tls-secret
      hosts:
        - "*.example.com"
---
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: my-vs
spec:
  hosts:
    - "api.example.com"
  gateways:
    - my-gateway
  http:
    - match:
        - uri:
            prefix: /api/v1
      route:
        - destination:
            host: api-service
            port:
              number: 8080
```


## 负载均衡策略


```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: load-balancing
spec:
  host: my-service
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN # or LEAST_CONN, RANDOM, PASSTHROUGH
---
# Consistent hashing for sticky sessions
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: sticky-sessions
spec:
  host: my-service
  trafficPolicy:
    loadBalancer:
      consistentHash:
        httpHeaderName: x-user-id
        # or: httpCookie, useSourceIp, httpQueryParameterName
```


## 最佳实践

### 应该做

- **从简入手** - 逐步增加复杂度
- **使用 subsets** - 清晰地为服务划分版本
- **设置超时** - 始终配置合理的超时
- **启用重试** - 但要配合退避与上限
- **监控** - 使用 Kiali 和 Jaeger 实现可观测性

### 不应做

- **不要过度重试** - 可能引发级联故障
- **不要忽视 outlier detection** - 启用熔断器
- **不要向生产环境做镜像** - 应镜像到测试环境
- **不要跳过金丝雀** - 先用小比例流量测试

## 调试命令


```bash
# Check VirtualService configuration
istioctl analyze

# View effective routes
istioctl proxy-config routes deploy/my-app -o json

# Check endpoint discovery
istioctl proxy-config endpoints deploy/my-app

# Debug traffic
istioctl proxy-config log deploy/my-app --level debug
```
