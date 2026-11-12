> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/cicd-automation/skills/deployment-pipeline-design/references/details.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# deployment-pipeline-design：详细模式与完整示例

## 流水线阶段

### 标准流水线流程

```
┌─────────┐   ┌──────┐   ┌─────────┐   ┌────────┐   ┌──────────┐
│  Build  │ → │ Test │ → │ Staging │ → │ Approve│ → │Production│
└─────────┘   └──────┘   └─────────┘   └────────┘   └──────────┘
```

### 阶段详解

1. **Source**：代码检出，依赖图解析
2. **Build**：编译、打包、容器化，并对产物签名
3. **Test**：单元测试、集成测试、SAST/SCA 安全扫描
4. **Staging Deploy**：部署到 Staging 环境并执行冒烟测试
5. **Integration Tests**：E2E 测试、契约测试、性能基线
6. **Approval Gate**：人工审批或基于指标的自动门禁
7. **Production Deploy**：金丝雀、蓝绿或滚动策略
8. **Verification**：深度健康检查、拨测（synthetic monitoring）
9. **Rollback**：出现故障信号时自动回滚

## 审批门禁模式

### 模式 1：手动审批（GitHub Actions）

```yaml
production-deploy:
  needs: staging-deploy
  environment:
    name: production
    url: https://app.example.com
  runs-on: ubuntu-latest
  steps:
    - name: Deploy to production
      run: kubectl apply -f k8s/production/
```

GitHub 的环境保护规则会在该 job 开始前强制要求指定审核人。审核人在 **Settings → Environments → production → Required reviewers** 中配置。

### 模式 2：基于时间的审批（GitLab CI）

```yaml
deploy:production:
  stage: deploy
  script:
    - deploy.sh production
  environment:
    name: production
  when: delayed
  start_in: 30 minutes
  only:
    - main
```

### 模式 3：多审批人（Azure Pipelines）

```yaml
stages:
  - stage: Production
    dependsOn: Staging
    jobs:
      - deployment: Deploy
        environment:
          name: production
          resourceType: Kubernetes
        strategy:
          runOnce:
            preDeploy:
              steps:
                - task: ManualValidation@0
                  inputs:
                    notifyUsers: "team-leads@example.com"
                    instructions: "Review staging metrics before approving"
```

### 模式 4：自动化指标门禁

使用 AnalysisTemplate（Argo Rollouts）或自定义门禁脚本，在错误率超过阈值时阻断晋升：

```yaml
# Argo Rollouts AnalysisTemplate — blocks canary promotion automatically
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: success-rate
spec:
  metrics:
  - name: success-rate
    interval: 60s
    successCondition: "result[0] >= 0.95"
    failureCondition: "result[0] < 0.90"
    inconclusiveLimit: 3
    provider:
      prometheus:
        address: http://prometheus:9090
        query: |
          sum(rate(http_requests_total{status!~"5..",job="my-app"}[2m]))
          / sum(rate(http_requests_total{job="my-app"}[2m]))
```

## 部署策略

### 决策表

| 策略 | 停机时间 | 回滚速度 | 成本影响 | 最适用场景 |
|-------------|----------|----------------|-----------------|----------------------------------|
| 滚动（Rolling） | 无 | 约数分钟 | 无 | 大多数无状态服务 |
| 蓝绿（Blue-Green） | 无 | 即时 | 2 倍基础设施（临时） | 高风险部署或数据库迁移 |
| 金丝雀（Canary） | 无 | 即时 | 极小 | 高流量、指标驱动 |
| 重建（Recreate） | 是 | 快 | 无 | 开发/测试、批处理任务 |
| 功能开关（Feature Flag） | 无 | 即时 | 无 | 功能的渐进式暴露 |

### 1. 滚动部署（Rolling Deployment）

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 2         # at most 12 pods during rollout
      maxUnavailable: 1   # at least 9 pods always serving
```

特点：渐进式上线、零停机、回滚简单，适合大多数应用。

### 2. 蓝绿部署（Blue-Green Deployment）

```bash
# Switch traffic from blue to green
kubectl apply -f k8s/green-deployment.yaml
kubectl rollout status deployment/my-app-green

# Flip the service selector
kubectl patch service my-app -p '{"spec":{"selector":{"version":"green"}}}'

# Rollback instantly if needed
kubectl patch service my-app -p '{"spec":{"selector":{"version":"blue"}}}'
```

特点：即时切换、回滚简单、基础设施成本暂时翻倍，适合预热时间长的高风险部署。

### 3. 金丝雀部署（Argo Rollouts）

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: my-app
spec:
  replicas: 10
  strategy:
    canary:
      analysis:
        templates:
          - templateName: success-rate
        startingStep: 2
      steps:
        - setWeight: 10
        - pause: { duration: 5m }
        - setWeight: 25
        - pause: { duration: 5m }
        - setWeight: 50
        - pause: { duration: 10m }
        - setWeight: 100
```

特点：流量渐进式迁移、以真实用户指标做验证、自动晋升或回滚；需要 Argo Rollouts 或服务网格。

### 4. 功能开关（Feature Flags）

```python
from flagsmith import Flagsmith

flagsmith = Flagsmith(environment_key="API_KEY")

if flagsmith.has_feature("new_checkout_flow"):
    process_checkout_v2()
else:
    process_checkout_v1()
```

特点：部署而不发布、A/B 测试、按用户分组即时回滚、独立于部署的细粒度控制。

## 流水线编排

### 多阶段流水线示例（GitHub Actions）

```yaml
name: Production Pipeline

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      image: ${{ steps.build.outputs.image }}
    steps:
      - uses: actions/checkout@v4
      - name: Build and push Docker image
        id: build
        run: |
          IMAGE=myapp:${{ github.sha }}
          docker build -t $IMAGE .
          docker push $IMAGE
          echo "image=$IMAGE" >> $GITHUB_OUTPUT

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Unit tests
        run: make test
      - name: Security scan
        run: trivy image ${{ needs.build.outputs.image }}

  deploy-staging:
    needs: test
    environment:
      name: staging
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to staging
        run: kubectl apply -f k8s/staging/

  integration-test:
    needs: deploy-staging
    runs-on: ubuntu-latest
    steps:
      - name: Run E2E tests
        run: npm run test:e2e

  deploy-production:
    needs: integration-test
    environment:
      name: production        # blocks here until required reviewers approve
    runs-on: ubuntu-latest
    steps:
      - name: Canary deployment
        run: |
          kubectl apply -f k8s/production/
          kubectl argo rollouts promote my-app

  verify:
    needs: deploy-production
    runs-on: ubuntu-latest
    steps:
      - name: Deep health check
        run: |
          for i in {1..12}; do
            STATUS=$(curl -sf https://app.example.com/health/ready | jq -r '.status')
            [ "$STATUS" = "ok" ] && exit 0
            sleep 10
          done
          exit 1
      - name: Notify on success
        run: |
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -d '{"text":"Production deployment successful: ${{ github.sha }}"}'
```

## 健康检查

### 浅层与深层健康端点

浅层的 `/ping` 在下游依赖已经故障时仍会返回 200。应使用深层的就绪（readiness）端点，在晋升流量之前先核实真实依赖。

```python
# /health/ready — checks real dependencies, used by pipeline gate
@app.get("/health/ready")
async def readiness():
    checks = {
        "database": await check_db_connection(),
        "cache":    await check_redis_connection(),
        "queue":    await check_queue_connection(),
    }
    status = "ok" if all(checks.values()) else "degraded"
    code = 200 if status == "ok" else 503
    return JSONResponse({"status": status, "checks": checks}, status_code=code)
```

### 部署后验证脚本

```bash
#!/usr/bin/env bash
# verify-deployment.sh — run after every production deploy
set -euo pipefail

ENDPOINT="${1:?usage: verify-deployment.sh <base-url>}"
MAX_ATTEMPTS=12
SLEEP_SECONDS=10

for i in $(seq 1 $MAX_ATTEMPTS); do
  STATUS=$(curl -sf "$ENDPOINT/health/ready" | jq -r '.status' 2>/dev/null || echo "unreachable")
  if [ "$STATUS" = "ok" ]; then
    echo "Health check passed after $((i * SLEEP_SECONDS))s"
    exit 0
  fi
  echo "Attempt $i/$MAX_ATTEMPTS: status=$STATUS — retrying in ${SLEEP_SECONDS}s"
  sleep "$SLEEP_SECONDS"
done

echo "Health check failed after $((MAX_ATTEMPTS * SLEEP_SECONDS))s"
exit 1
```

## 回滚策略

### 流水线中的自动回滚

```yaml
deploy-and-verify:
  steps:
    - name: Deploy new version
      run: kubectl apply -f k8s/

    - name: Wait for rollout
      run: kubectl rollout status deployment/my-app --timeout=5m

    - name: Post-deployment health check
      id: health
      run: ./scripts/verify-deployment.sh https://app.example.com

    - name: Rollback on failure
      if: failure()
      run: |
        kubectl rollout undo deployment/my-app
        echo "Rolled back to previous revision"
```

### 手动回滚命令

```bash
# List revision history with change-cause annotations
kubectl rollout history deployment/my-app

# Rollback to previous version
kubectl rollout undo deployment/my-app

# Rollback to a specific revision
kubectl rollout undo deployment/my-app --to-revision=3

# Verify rollback completed
kubectl rollout status deployment/my-app
```

更多高级回滚策略（含数据库迁移回滚与 Argo Rollouts 中止流程）见 [`references/advanced-strategies.md`](references/advanced-strategies.md)。

## 监控与指标

### 需要跟踪的关键 DORA 指标

| 指标 | 目标（精英） | 测量方式 |
|--------------------------|----------------|------------------------------------------|
| 部署频率（Deployment Frequency） | 每天多次 | 每天流水线运行次数 |
| 变更前置时间（Lead Time for Changes） | < 1 小时 | 提交时间戳 → 生产部署 |
| 变更失败率（Change Failure Rate） | < 5% | 失败部署数 / 总部署数 |
| 平均恢复时间（Mean Time to Recovery） | < 1 小时 | 事件开始 → 服务恢复 |

### 部署后指标验证

```yaml
- name: Verify error rate post-deployment
  run: |
    sleep 60  # allow metrics to accumulate

    ERROR_RATE=$(curl -sf "$PROMETHEUS_URL/api/v1/query" \
      --data-urlencode 'query=sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))' \
      | jq '.data.result[0].value[1]')

    echo "Current error rate: $ERROR_RATE"
    if (( $(echo "$ERROR_RATE > 0.01" | bc -l) )); then
      echo "Error rate $ERROR_RATE exceeds 1% threshold — triggering rollback"
      exit 1
    fi
```

## 流水线最佳实践

1. **快速失败（Fail fast）**：先跑快的检查（lint、单元测试），再跑慢的（E2E、安全扫描）
2. **并行执行**：并发运行相互独立的 job，尽量缩短流水线总耗时
3. **缓存**：在多次运行之间缓存依赖层与构建产物
4. **产物晋升**：只构建一次，让同一产物贯穿所有环境
5. **环境对等**：让 Staging 基础设施尽量接近生产环境
6. **密钥管理**：使用密钥存储（Vault、AWS Secrets Manager、GitHub 加密 secrets），绝不硬编码
7. **部署窗口**：优先选择低流量时段；通过门禁策略强制执行变更冻结期
8. **幂等部署**：确保重复执行部署产出相同结果
9. **回滚自动化**：健康检查或指标阈值失败时自动触发回滚
10. **部署标注**：向监控工具（Datadog、Grafana）发送部署标记以便关联分析
