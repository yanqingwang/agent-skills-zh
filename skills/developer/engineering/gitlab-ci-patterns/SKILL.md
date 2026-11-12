---
name: gitlab-ci-patterns
description: 构建 GitLab CI/CD 流水线，涵盖多阶段工作流、缓存与分布式 runner，实现可扩展的自动化。在实现 GitLab CI/CD、优化流水线性能，或搭建自动化测试与部署时使用本 Skill。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/cicd-automation/skills/gitlab-ci-patterns/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# GitLab CI 模式

面向自动化测试、构建与部署的完整 GitLab CI/CD 流水线模式。

## 目的

创建高效的 GitLab CI 流水线，具备合理的阶段组织、缓存与部署策略。

## 何时使用

- 自动化基于 GitLab 的 CI/CD
- 实现多阶段流水线
- 配置 GitLab Runner
- 从 GitLab 部署到 Kubernetes
- 实现 GitOps 工作流

## 基础流水线结构

```yaml
stages:
  - build
  - test
  - deploy

variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: "/certs"

build:
  stage: build
  image: node:20
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/

test:
  stage: test
  image: node:20
  script:
    - npm ci
    - npm run lint
    - npm test
  coverage: '/Lines\s*:\s*(\d+\.\d+)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

deploy:
  stage: deploy
  image: bitnami/kubectl:1.31
  script:
    - kubectl apply -f k8s/
    - kubectl rollout status deployment/my-app
  only:
    - main
  environment:
    name: production
    url: https://app.example.com
```

## Docker 构建与推送

```yaml
build-docker:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker build -t $CI_REGISTRY_IMAGE:latest .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - docker push $CI_REGISTRY_IMAGE:latest
  only:
    - main
    - tags
```

## 多环境部署

将 `KUBE_CA_CERT_FILE` 设置为一个 GitLab 文件类型变量，内容为集群 CA 证书，并通过受保护、已遮蔽的 CI 变量提供 `KUBE_TOKEN`。该文件类型变量包含一个路径，kubectl 用它来校验 API 服务器证书。对 `develop` 和 `main` 都加以保护，以便部署作业能够读取受保护的令牌。

```yaml
.deploy_template: &deploy_template
  image: bitnami/kubectl:1.31
  before_script:
    - kubectl config set-cluster k8s --server="$KUBE_URL" --certificate-authority="$KUBE_CA_CERT_FILE" --embed-certs=true
    - kubectl config set-credentials admin --token="$KUBE_TOKEN"
    - kubectl config set-context default --cluster=k8s --user=admin
    - kubectl config use-context default

deploy:staging:
  <<: *deploy_template
  stage: deploy
  script:
    - kubectl apply -f k8s/ -n staging
    - kubectl rollout status deployment/my-app -n staging
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - develop

deploy:production:
  <<: *deploy_template
  stage: deploy
  script:
    - kubectl apply -f k8s/ -n production
    - kubectl rollout status deployment/my-app -n production
  environment:
    name: production
    url: https://app.example.com
  when: manual
  only:
    - main
```

## Terraform 流水线

```yaml
stages:
  - validate
  - plan
  - apply

variables:
  TF_ROOT: ${CI_PROJECT_DIR}/terraform
  TF_VERSION: "1.6.0"

before_script:
  - cd ${TF_ROOT}
  - terraform --version

validate:
  stage: validate
  image: hashicorp/terraform:${TF_VERSION}
  script:
    - terraform init -backend=false
    - terraform validate
    - terraform fmt -check

plan:
  stage: plan
  image: hashicorp/terraform:${TF_VERSION}
  script:
    - terraform init
    - terraform plan -out=tfplan
  artifacts:
    paths:
      - ${TF_ROOT}/tfplan
    expire_in: 1 day

apply:
  stage: apply
  image: hashicorp/terraform:${TF_VERSION}
  script:
    - terraform init
    - terraform apply -auto-approve tfplan
  dependencies:
    - plan
  when: manual
  only:
    - main
```

## 安全扫描

```yaml
include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Dependency-Scanning.gitlab-ci.yml
  - template: Security/Container-Scanning.gitlab-ci.yml

trivy-scan:
  stage: test
  image: aquasec/trivy:0.58.0
  script:
    - trivy image --exit-code 1 --severity HIGH,CRITICAL $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  allow_failure: true
```

## 缓存策略

```yaml
# Cache node_modules
build:
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
    policy: pull-push

# Global cache
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - .cache/
    - vendor/

# Separate cache per job
job1:
  cache:
    key: job1-cache
    paths:
      - build/

job2:
  cache:
    key: job2-cache
    paths:
      - dist/
```

## 动态子流水线

```yaml
generate-pipeline:
  stage: build
  script:
    - python generate_pipeline.py > child-pipeline.yml
  artifacts:
    paths:
      - child-pipeline.yml

trigger-child:
  stage: deploy
  trigger:
    include:
      - artifact: child-pipeline.yml
        job: generate-pipeline
    strategy: depend
```


## 最佳实践

1. **使用明确的镜像标签**（node:20，而非 node:latest）
2. **恰当地缓存依赖**
3. **用 artifacts 承载构建产物**
4. **为生产环境设置手动门禁**
5. **用 environments 跟踪部署**
6. **启用合并请求流水线**
7. **用流水线计划任务运行周期性作业**
8. **实施安全扫描**
9. **用 CI/CD 变量管理密钥**
10. **监控流水线性能**

## 相关 Skill

- `github-actions-templates` - 用于 GitHub Actions
- `deployment-pipeline-design` - 用于架构设计
- `secrets-management` - 用于密钥管理
