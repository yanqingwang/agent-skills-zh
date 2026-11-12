---
name: chaos-engineer
description: 为分布式系统设计混沌实验、搭建故障注入框架、组织 game day 演练，产出 runbook、实验清单、回滚流程与复盘模板。适用于设计混沌实验、实现故障注入框架或开展 game day 演练。可用于混沌实验、韧性测试、爆炸半径控制、game day、反脆弱系统、故障注入、Chaos Monkey、Litmus Chaos。
license: MIT
metadata:
  author: https://github.com/Jeffallan
  company: https://synergetic.solutions
  version: "1.1.0"
  domain: devops
  triggers: chaos engineering, resilience testing, failure injection, game day, blast radius, chaos experiment, fault injection, Chaos Monkey, Litmus Chaos, antifragile
  role: specialist
  scope: implementation
  output-format: code
  related-skills: sre-engineer, devops-engineer, kubernetes-specialist
---

> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/chaos-engineer/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 混沌工程师

## 何时使用此 Skill

- 设计与执行混沌实验
- 实现故障注入框架（Chaos Monkey、Litmus 等）
- 规划与开展 game day 演练
- 构建爆炸半径控制与安全机制
- 在 CI/CD 中搭建持续混沌测试
- 基于实验结果提升系统韧性

## 核心工作流

1. **系统分析** - 梳理架构、依赖、关键路径与故障模式
2. **实验设计** - 定义假设、稳态、爆炸半径与安全控制
3. **执行混沌实验** - 在监控与快速回滚保障下运行受控实验
4. **总结与改进** - 记录发现、落实修复、完善监控
5. **自动化** - 将混沌测试集成到 CI/CD，实现持续韧性验证

## 参考指引

根据上下文加载详细指引：

| 主题 | 参考文档 | 加载时机 |
|-------|-----------|-----------|
| 实验 | `references/experiment-design.md` | 设计假设、爆炸半径、回滚 |
| 基础设施 | `references/infrastructure-chaos.md` | 服务器、网络、可用区、区域故障 |
| Kubernetes | `references/kubernetes-chaos.md` | Pod、node、Litmus、chaos mesh 实验 |
| 工具与自动化 | `references/chaos-tools.md` | Chaos Monkey、Gremlin、Pumba、CI/CD 集成 |
| game day | `references/game-days.md` | 规划、执行 game day 并从中总结 |

## 安全检查清单

每个实验都必须遵守、却容易被忽视的约束：

- **稳态优先**：注入任何故障前，先定义并验证基线指标
- **限制爆炸半径**：从最小的影响范围起步，验证通过后再扩大
- **自动回滚 ≤ 30 秒**：中止路径必须在实验开始前完成脚本化并经过测试
- **单一变量**：在充分掌握行为之前，每次只改变一个故障条件
- **无安全防护不上生产**：面向客户的环境必须具备熔断器、功能开关或金丝雀隔离
- **闭环**：每个实验都要产出书面总结，并至少落实一项可追踪的改进

## 输出模板

实施混沌工程时，需提供：
1. 实验设计文档（假设、指标、爆炸半径）
2. 实现代码（故障注入脚本/清单）
3. 监控搭建与告警配置
4. 回滚流程与安全控制
5. 学习总结与改进建议

## 具体示例：Pod 故障实验（Litmus Chaos）

下面展示一个完整实验：从假设到回滚，基于 Kubernetes 上的 Litmus Chaos。

### 步骤 1：定义稳态并应用实验


```bash
# Verify baseline: p99 latency < 200ms, error rate < 0.1%
kubectl get deploy my-service -n production
kubectl top pods -n production -l app=my-service
```


### 步骤 2：创建并应用 Litmus ChaosEngine 清单


```yaml
# chaos-pod-delete.yaml
apiVersion: litmuschaos.io/v1alpha1
kind: ChaosEngine
metadata:
  name: my-service-pod-delete
  namespace: production
spec:
  appinfo:
    appns: production
    applabel: "app=my-service"
    appkind: deployment
  # Limit blast radius: only 1 replica at a time
  engineState: active
  chaosServiceAccount: litmus-admin
  experiments:
    - name: pod-delete
      spec:
        components:
          env:
            - name: TOTAL_CHAOS_DURATION
              value: "60"          # seconds
            - name: CHAOS_INTERVAL
              value: "20"          # delete one pod every 20s
            - name: FORCE
              value: "false"
            - name: PODS_AFFECTED_PERC
              value: "33"          # max 33% of replicas affected
```



```bash
# Apply the experiment
kubectl apply -f chaos-pod-delete.yaml

# Watch experiment status
kubectl describe chaosengine my-service-pod-delete -n production
kubectl get chaosresult my-service-pod-delete-pod-delete -n production -w
```


### 步骤 3：实验期间进行监控


```bash
# Tail application logs for errors
kubectl logs -l app=my-service -n production --since=2m -f

# Check ChaosResult verdict when complete
kubectl get chaosresult my-service-pod-delete-pod-delete \
  -n production -o jsonpath='{.status.experimentStatus.verdict}'
```


### 步骤 4：稳态被破坏时回滚 / 中止


```bash
# Immediately stop the experiment
kubectl patch chaosengine my-service-pod-delete \
  -n production --type merge -p '{"spec":{"engineState":"stop"}}'

# Confirm all pods are healthy
kubectl rollout status deployment/my-service -n production
```


## 具体示例：使用 toxiproxy 注入网络延迟


```bash
# Install toxiproxy CLI
brew install toxiproxy   # macOS; use the binary release on Linux

# Start toxiproxy server (runs alongside your service)
toxiproxy-server &

# Create a proxy for your downstream dependency
toxiproxy-cli create -l 0.0.0.0:22222 -u downstream-db:5432 db-proxy

# Inject 300ms latency with 10% jitter — blast radius: this proxy only
toxiproxy-cli toxic add db-proxy -t latency -a latency=300 -a jitter=30

# Run your load test / observe metrics here ...

# Remove the toxic to restore normal behaviour
toxiproxy-cli toxic remove db-proxy -n latency_downstream
```


## 具体示例：Chaos Monkey（Spinnaker / 独立模式）


```bash
# chaos-monkey-config.yml — restrict to a single ASG
deployment:
  enabled: true
  regionIndependence: false
chaos:
  enabled: true
  meanTimeBetweenKillsInWorkDays: 2
  minTimeBetweenKillsInWorkDays: 1
  grouping: APP           # kill one instance per app, not per cluster
  exceptions:
    - account: production
      region: us-east-1
      detail: "*-canary"  # never kill canary instances

# Apply and trigger a manual kill for testing
chaos-monkey --app my-service --account staging --dry-run false
```


由 [@jeffallan](https://github.com/jeffallan) 维护，[Synergetic Solutions](https://synergetic.solutions) 首席顾问

[文档](https://jeffallan.github.io/claude-skills/skills/devops/chaos-engineer/)
