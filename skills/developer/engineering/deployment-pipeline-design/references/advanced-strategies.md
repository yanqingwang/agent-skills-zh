> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/cicd-automation/skills/deployment-pipeline-design/references/advanced-strategies.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 高级部署策略参考

扩展配置、平台特定模式与高级回滚策略。
核心模式与决策表见 [`../SKILL.md`](../SKILL.md)。

---

## 平台特定流水线配置

### GitHub Actions：使用可复用 Workflow 的完整生产流水线

```yaml
# .github/workflows/production.yml
name: Production Pipeline

on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      skip_tests:
        type: boolean
        default: false

permissions:
  contents: read
  id-token: write   # for OIDC auth to cloud providers

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      image_tag: ${{ steps.meta.outputs.version }}
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Docker metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=sha,prefix=,format=short

      - name: Build and push (with layer cache)
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  security-scan:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Run Trivy vulnerability scan
        uses: aquasecurity/trivy-action@0.28.0
        with:
          image-ref: ghcr.io/${{ github.repository }}:${{ needs.build.outputs.image_tag }}
          exit-code: 1
          severity: CRITICAL,HIGH

      - name: SAST with Semgrep
        uses: semgrep/semgrep-action@v1
        with:
          config: auto

  test:
    needs: build
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
    steps:
      - uses: actions/checkout@v4
      - name: Run test suite
        run: make test-ci
        env:
          DATABASE_URL: postgres://postgres:test@localhost/test

  deploy-staging:
    needs: [test, security-scan]
    environment:
      name: staging
      url: https://staging.example.com
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials (OIDC)
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/deploy-staging
          aws-region: us-east-1

      - name: Deploy to EKS staging
        run: |
          aws eks update-kubeconfig --name my-cluster-staging
          kubectl set image deployment/my-app \
            app=ghcr.io/${{ github.repository }}:${{ needs.build.outputs.image_tag }}
          kubectl rollout status deployment/my-app --timeout=5m

  e2e-tests:
    needs: deploy-staging
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Playwright E2E suite
        run: npx playwright test --reporter=github
        env:
          BASE_URL: https://staging.example.com

  deploy-production:
    needs: e2e-tests
    environment:
      name: production
      url: https://app.example.com
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials (OIDC)
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/deploy-production
          aws-region: us-east-1

      - name: Deploy canary to production
        run: |
          aws eks update-kubeconfig --name my-cluster-prod
          kubectl argo rollouts set image my-app \
            app=ghcr.io/${{ github.repository }}:${{ needs.build.outputs.image_tag }}

      - name: Monitor canary promotion
        run: |
          kubectl argo rollouts status my-app --timeout=30m

      - name: Rollback on failure
        if: failure()
        run: kubectl argo rollouts abort my-app
```

---

### GitLab CI：带动态环境的多环境流水线

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - staging
  - production

variables:
  DOCKER_DRIVER: overlay2
  IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA

build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build --cache-from $CI_REGISTRY_IMAGE:latest -t $IMAGE .
    - docker push $IMAGE
    - docker tag $IMAGE $CI_REGISTRY_IMAGE:latest
    - docker push $CI_REGISTRY_IMAGE:latest

test:unit:
  stage: test
  image: $IMAGE
  script:
    - make test
  coverage: '/coverage: \d+\.\d+%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml

test:security:
  stage: test
  image:
    name: aquasec/trivy:latest
    entrypoint: [""]
  script:
    - trivy image --exit-code 1 --severity CRITICAL,HIGH $IMAGE

deploy:staging:
  stage: staging
  environment:
    name: staging
    url: https://staging.example.com
    on_stop: stop:staging
  script:
    - kubectl apply -f k8s/staging/
    - kubectl set image deployment/my-app app=$IMAGE -n staging
    - kubectl rollout status deployment/my-app -n staging
  only:
    - main

stop:staging:
  stage: staging
  environment:
    name: staging
    action: stop
  script:
    - kubectl delete namespace staging --ignore-not-found
  when: manual
  only:
    - main

deploy:production:
  stage: production
  environment:
    name: production
    url: https://app.example.com
  script:
    - kubectl set image deployment/my-app app=$IMAGE -n production
    - kubectl rollout status deployment/my-app -n production --timeout=10m
  when: manual
  only:
    - main
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual
      allow_failure: false
```

---

### Azure Pipelines：带审批与环境的多阶段流水线

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include:
      - main

variables:
  imageRepository: 'myapp'
  containerRegistry: 'myregistry.azurecr.io'
  tag: '$(Build.BuildId)'

stages:
  - stage: Build
    displayName: 'Build & Test'
    jobs:
      - job: BuildAndTest
        pool:
          vmImage: ubuntu-latest
        steps:
          - task: Docker@2
            displayName: Build image
            inputs:
              command: build
              repository: $(imageRepository)
              dockerfile: Dockerfile
              tags: $(tag)

          - task: Docker@2
            displayName: Push image
            inputs:
              command: push
              repository: $(imageRepository)
              tags: $(tag)

          - script: make test
            displayName: Run tests

  - stage: Staging
    displayName: 'Deploy to Staging'
    dependsOn: Build
    jobs:
      - deployment: DeployStaging
        environment: staging
        pool:
          vmImage: ubuntu-latest
        strategy:
          runOnce:
            deploy:
              steps:
                - task: KubernetesManifest@0
                  inputs:
                    action: deploy
                    manifests: k8s/staging/*.yaml
                    containers: $(containerRegistry)/$(imageRepository):$(tag)

  - stage: Production
    displayName: 'Deploy to Production'
    dependsOn: Staging
    jobs:
      - deployment: DeployProduction
        environment:
          name: production
          resourceType: Kubernetes
        pool:
          vmImage: ubuntu-latest
        strategy:
          canary:
            increments: [10, 25, 50]
            preDeploy:
              steps:
                - task: ManualValidation@0
                  inputs:
                    notifyUsers: 'release-managers@example.com'
                    instructions: 'Verify staging metrics. Approve to start canary.'
                    onTimeout: reject
            deploy:
              steps:
                - task: KubernetesManifest@0
                  inputs:
                    action: deploy
                    manifests: k8s/production/*.yaml
                    containers: $(containerRegistry)/$(imageRepository):$(tag)
            postRouteTraffic:
              steps:
                - script: ./scripts/verify-deployment.sh https://app.example.com
            on:
              failure:
                steps:
                  - task: KubernetesManifest@0
                    inputs:
                      action: reject
```

---

## 多区域金丝雀晋升

先部署到试点区域并完成验证，再并行晋升到其余区域：

```yaml
# deploy-multiregion.yml (GitHub Actions)
jobs:
  deploy-pilot:
    environment: production-us-east-1
    runs-on: ubuntu-latest
    steps:
      - name: Deploy canary to pilot region
        run: |
          aws eks update-kubeconfig --name cluster-us-east-1 --region us-east-1
          kubectl argo rollouts set image my-app app=$IMAGE
          kubectl argo rollouts status my-app --timeout=20m

  deploy-secondary:
    needs: deploy-pilot
    strategy:
      matrix:
        region: [us-west-2, eu-west-1, ap-southeast-1]
    environment: production-${{ matrix.region }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to ${{ matrix.region }}
        run: |
          aws eks update-kubeconfig --name cluster-${{ matrix.region }} \
            --region ${{ matrix.region }}
          kubectl argo rollouts set image my-app app=$IMAGE
          kubectl argo rollouts status my-app --timeout=20m
```

---

## 高级 Argo Rollouts 模式

### 基于实验的金丝雀（A/B 分析）

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: my-app
spec:
  replicas: 20
  strategy:
    canary:
      canaryService: my-app-canary
      stableService: my-app-stable
      trafficRouting:
        istio:
          virtualService:
            name: my-app-vsvc
      analysis:
        templates:
          - templateName: success-rate
          - templateName: latency-p99
        startingStep: 1
        args:
          - name: service-name
            value: my-app-canary
      steps:
        - setWeight: 5
        - experiment:
            templates:
              - name: baseline
                specRef: stable
              - name: canary
                specRef: canary
            analyses:
              - templateName: ab-test
                requiredForCompletion: true
        - setWeight: 20
        - pause: { duration: 10m }
        - setWeight: 50
        - pause: { duration: 15m }
        - setWeight: 100
```

### 基于请求头的金丝雀（流量切分前的内部测试）

```yaml
# Route users with X-Canary: true header to canary pods
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: my-app-vsvc
spec:
  http:
    - match:
        - headers:
            x-canary:
              exact: "true"
      route:
        - destination:
            host: my-app-canary
    - route:
        - destination:
            host: my-app-stable
          weight: 90
        - destination:
            host: my-app-canary
          weight: 10
```

---

## 数据库迁移回滚策略

### Expand/Contract 模式（安全的 Schema 变更）

不要在单个发布周期内破坏向后兼容性。把 expand/contract 模式分布在三个发布中执行：

```
Release N:   Add nullable column (expand)
Release N+1: Backfill data, deploy new code that reads new column
Release N+2: Drop old column (contract) — safe because no code references it
```

```bash
# Release N migration — backward compatible
cat > migrations/V20240315__expand_add_email_v2.sql <<'EOF'
ALTER TABLE users ADD COLUMN email_v2 VARCHAR(255);
CREATE INDEX CONCURRENTLY idx_users_email_v2 ON users(email_v2);
EOF

# Release N+2 migration — contract (only after old code retired)
cat > migrations/V20240415__contract_drop_email.sql <<'EOF'
ALTER TABLE users DROP COLUMN email;
ALTER TABLE users RENAME COLUMN email_v2 TO email;
EOF
```

### Flyway 与 Undo 脚本

```bash
# Forward migration
flyway migrate

# Undo the most recent migration (requires Flyway Teams)
flyway undo

# Undo a specific version
flyway undo -target=20240315
```

Undo 脚本命名约定：`U20240315__expand_add_email_v2.sql`（前缀用 `U` 而非 `V`）。

### 零停机索引创建（PostgreSQL）

```sql
-- Blocking (avoid in production):
CREATE INDEX idx_users_email ON users(email);

-- Non-blocking (safe for live systems):
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);
```

所有生产迁移都应使用 `CREATE INDEX CONCURRENTLY`。将其加入应用更新之前执行的预部署迁移步骤。

---

## 蓝绿部署与数据库（完整示例）

```yaml
# blue-green-deploy.yml
steps:
  - name: Deploy green environment
    run: |
      kubectl apply -f k8s/green/

  - name: Run database migrations (forward, backward-compatible)
    run: |
      kubectl exec -n production deploy/migration-job -- flyway migrate

  - name: Smoke test green
    run: |
      kubectl port-forward -n production svc/my-app-green 8080:80 &
      sleep 3
      curl -sf http://localhost:8080/health/ready

  - name: Switch traffic to green
    run: |
      kubectl patch service my-app \
        -p '{"spec":{"selector":{"slot":"green"}}}'

  - name: Verify green is live
    run: ./scripts/verify-deployment.sh https://app.example.com

  - name: Scale down blue
    run: |
      kubectl scale deployment my-app-blue --replicas=0

  - name: Rollback to blue on failure
    if: failure()
    run: |
      kubectl patch service my-app \
        -p '{"spec":{"selector":{"slot":"blue"}}}'
      kubectl scale deployment my-app-blue --replicas=5
```

---

## 部署冻结自动化

在冻结窗口期间自动阻断生产部署：

```python
#!/usr/bin/env python3
# scripts/check-freeze-window.py
import os
import sys
from datetime import datetime, timezone

FREEZE_WINDOWS = [
    # (month, day_start, day_end, description)
    (11, 25, 30, "US Thanksgiving"),
    (12, 20, 31, "Year-end freeze"),
    (1, 1, 2, "New Year"),
]

now = datetime.now(timezone.utc)
month, day = now.month, now.day

for fm, d_start, d_end, label in FREEZE_WINDOWS:
    if fm == month and d_start <= day <= d_end:
        print(f"BLOCKED: Deployment freeze active — {label}")
        print("Override with FORCE_DEPLOY=true environment variable if critical.")
        if os.environ.get("FORCE_DEPLOY") != "true":
            sys.exit(1)

print("No active freeze window — deployment allowed.")
```

在流水线中使用：

```yaml
- name: Check deployment freeze window
  run: python scripts/check-freeze-window.py
  env:
    FORCE_DEPLOY: ${{ vars.FORCE_DEPLOY }}
```

---

## 通知模板

### Slack 部署通知

```bash
#!/usr/bin/env bash
# scripts/notify-slack.sh
STATUS="${1:?pass 'success' or 'failure'}"
WEBHOOK="${SLACK_WEBHOOK:?SLACK_WEBHOOK not set}"
REPO="${GITHUB_REPOSITORY:-unknown}"
SHA="${GITHUB_SHA:-unknown}"
ACTOR="${GITHUB_ACTOR:-unknown}"

if [ "$STATUS" = "success" ]; then
  COLOR="good"
  EMOJI=":white_check_mark:"
  TEXT="Production deploy succeeded"
else
  COLOR="danger"
  EMOJI=":red_circle:"
  TEXT="Production deploy FAILED — rollback triggered"
fi

curl -sf -X POST "$WEBHOOK" \
  -H "Content-Type: application/json" \
  -d "{
    \"attachments\": [{
      \"color\": \"$COLOR\",
      \"text\": \"$EMOJI $TEXT\",
      \"fields\": [
        {\"title\": \"Repo\", \"value\": \"$REPO\", \"short\": true},
        {\"title\": \"SHA\", \"value\": \"${SHA:0:7}\", \"short\": true},
        {\"title\": \"Deployed by\", \"value\": \"$ACTOR\", \"short\": true}
      ]
    }]
  }"
```
