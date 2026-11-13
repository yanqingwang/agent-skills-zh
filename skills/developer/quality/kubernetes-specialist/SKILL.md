---
name: kubernetes-specialist
description: 部署或管理 Kubernetes 工作负载时使用。调用本 Skill 可创建部署 manifest、配置 Pod 安全策略、设置 ServiceAccount、定义网络隔离规则、调试 Pod 崩溃、分析资源限额、查看容器日志，或为工作负载做资源 right-sizing。适用于 Helm chart、RBAC 策略、NetworkPolicy、存储配置、性能优化、GitOps 流水线与多集群管理。
license: MIT
metadata:
  author: https://github.com/Jeffallan
  company: https://synergetic.solutions
  version: "1.1.1"
  domain: infrastructure
  triggers: Kubernetes, K8s, kubectl, Helm, container orchestration, pod deployment, RBAC, NetworkPolicy, Ingress, StatefulSet, Operator, CRD, CustomResourceDefinition, ArgoCD, Flux, GitOps, Istio, Linkerd, service mesh, multi-cluster, cost optimization, VPA, spot instances
  role: specialist
  scope: infrastructure
  output-format: manifests
  related-skills: devops-engineer, cloud-architect, sre-engineer, terraform-engineer, security-reviewer, chaos-engineer
---

> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/kubernetes-specialist/SKILL.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Kubernetes 专家

## 何时使用本 Skill

- 部署工作负载（Deployment、StatefulSet、DaemonSet、Job）
- 配置网络（Service、Ingress、NetworkPolicy）
- 管理配置（ConfigMap、Secret、环境变量）
- 配置持久化存储（PV、PVC、StorageClass）
- 创建 Helm chart 做应用打包
- 排查集群与工作负载问题
- 落实安全最佳实践

## 核心工作流

1. **分析需求**：理解工作负载特性、扩缩容需求、安全要求
2. **设计架构**：选择工作负载类型、网络模式、存储方案
3. **编写 manifest**：创建带合理资源限额与健康检查的声明式 YAML
4. **加固安全**：应用 RBAC、NetworkPolicy、Pod Security Standards（Pod 安全标准）与最小权限
5. **验证**：运行 `kubectl rollout status`、`kubectl get pods -w` 和 `kubectl describe pod <name>` 确认健康状态；必要时用 `kubectl rollout undo` 回滚

## 参考指南

根据上下文加载详细指引：

| 主题 | 参考文件 | 加载时机 |
|-------|-----------|-----------|
| 工作负载 | `references/workloads.md` | Deployment、StatefulSet、DaemonSet、Job、CronJob |
| 网络 | `references/networking.md` | Service、Ingress、NetworkPolicy、DNS |
| 配置 | `references/configuration.md` | ConfigMap、Secret、环境变量 |
| 存储 | `references/storage.md` | PV、PVC、StorageClass、CSI 驱动 |
| Helm chart | `references/helm-charts.md` | chart 结构、values、模板、hooks、测试、仓库 |
| 故障排查 | `references/troubleshooting.md` | kubectl debug、日志、事件、常见问题 |
| 自定义 Operator | `references/custom-operators.md` | CRD、Operator SDK、controller-runtime、调谐（reconciliation） |
| Service Mesh | `references/service-mesh.md` | Istio、Linkerd、流量管理、mTLS、金丝雀发布 |
| GitOps | `references/gitops.md` | ArgoCD、Flux、渐进式交付、sealed secrets |
| 成本优化 | `references/cost-optimization.md` | VPA、HPA 调优、spot 实例、配额、资源合理设定（right-sizing） |
| 多集群 | `references/multi-cluster.md` | Cluster API、联邦（federation）、跨集群网络、容灾（DR） |

## 约束

### 必须做（MUST DO）
- 使用声明式 YAML manifest（避免命令式 kubectl 命令）
- 为所有容器设置 resource requests 与 limits
- 包含 liveness 与 readiness 探针
- 敏感数据使用 Secret（绝不硬编码凭证）
- 应用最小权限 RBAC
- 用 NetworkPolicy 实现网络分段
- 用 namespace 做逻辑隔离
- 一致地为资源打 label 以便组织管理
- 在 annotation 中记录配置决策

### 禁止做（MUST NOT DO）
- 不设资源限额就部署到生产环境
- 把密钥存进 ConfigMap 或明文环境变量
- 让应用 Pod 使用默认 ServiceAccount
- 允许不受限制的网络访问（默认全放行）
- 无正当理由就以 root 运行容器
- 跳过健康检查（liveness/readiness 探针）
- 生产镜像使用 latest 标签
- 暴露不必要的端口或服务

## 常见 YAML 模式

### 带资源限额、探针与安全上下文的 Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  namespace: my-namespace
  labels:
    app: my-app
    version: "1.2.3"
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
        version: "1.2.3"
    spec:
      serviceAccountName: my-app-sa   # never use default SA
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 2000
      containers:
        - name: my-app
          image: my-registry/my-app:1.2.3   # never use latest
          ports:
            - containerPort: 8080
          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "500m"
              memory: "512Mi"
          livenessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 15
            periodSeconds: 20
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: ["ALL"]
          envFrom:
            - secretRef:
                name: my-app-secret   # pull credentials from Secret, not ConfigMap
```

### 最小 RBAC（最小权限）

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-app-sa
  namespace: my-namespace
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: my-app-role
  namespace: my-namespace
rules:
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get", "list"]   # grant only what is needed
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: my-app-rolebinding
  namespace: my-namespace
subjects:
  - kind: ServiceAccount
    name: my-app-sa
    namespace: my-namespace
roleRef:
  kind: Role
  name: my-app-role
  apiGroup: rbac.authorization.k8s.io
```

### NetworkPolicy（默认拒绝 + 显式放行）

```yaml
# Deny all ingress and egress by default
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: my-namespace
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
---
# Allow only specific traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-my-app
  namespace: my-namespace
spec:
  podSelector:
    matchLabels:
      app: my-app
  policyTypes: ["Ingress"]
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

## 验证命令

部署后，验证健康状态与安全态势：

```bash
# Watch rollout complete
kubectl rollout status deployment/my-app -n my-namespace

# Stream pod events to catch crash loops or image pull errors
kubectl get pods -n my-namespace -w

# Inspect a specific pod for failures
kubectl describe pod <pod-name> -n my-namespace

# Check container logs
kubectl logs <pod-name> -n my-namespace --previous   # use --previous for crashed containers

# Verify resource usage vs. limits
kubectl top pods -n my-namespace

# Audit RBAC permissions for a service account
kubectl auth can-i --list --as=system:serviceaccount:my-namespace:my-app-sa

# Roll back a failed deployment
kubectl rollout undo deployment/my-app -n my-namespace
```

## 输出模板

实现 Kubernetes 资源时，提供：
1. 结构完整的 YAML manifest
2. 必要时的 RBAC 配置（ServiceAccount、Role、RoleBinding）
3. 用于网络隔离的 NetworkPolicy
4. 设计决策与安全考量的简要说明

由 [@jeffallan](https://github.com/jeffallan) 维护，[Synergetic Solutions](https://synergetic.solutions) 首席顾问

[文档](https://jeffallan.github.io/claude-skills/skills/infrastructure/kubernetes-specialist/)
