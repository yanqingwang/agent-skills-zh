> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/developer/quality/kubernetes-specialist/references/configuration.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Kubernetes 配置管理

## ConfigMap 模式

### 基础 ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: production
data:
  # Simple key-value pairs
  database.host: "postgres-service.database.svc.cluster.local"
  database.port: "5432"
  database.name: "appdb"

  # Multi-line configuration
  app.properties: |
    server.port=8080
    logging.level=INFO
    cache.enabled=true
    cache.ttl=3600

  # JSON configuration
  features.json: |
    {
      "featureA": true,
      "featureB": false,
      "maxConnections": 100
    }

  # YAML configuration
  config.yaml: |
    server:
      port: 8080
      timeout: 30s
    database:
      pool_size: 20
      max_connections: 100
```

### 从文件创建 ConfigMap

```bash
# Create from literal values
kubectl create configmap app-config \
  --from-literal=database.host=postgres \
  --from-literal=database.port=5432

# Create from file
kubectl create configmap nginx-config \
  --from-file=nginx.conf

# Create from directory
kubectl create configmap app-configs \
  --from-file=configs/
```

## Secret 模式

### Opaque Secret（通用）

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
  namespace: production
type: Opaque
stringData:
  # Plain text (will be base64 encoded)
  db-password: "<db-password>"
  api-key: "<api-key>"
  jwt-secret: "<jwt-secret>"
data:
  # Already base64 encoded
  tls.crt: <base64-encoded-certificate>
  tls.key: <base64-encoded-private-key>
```

### TLS Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: example-tls
  namespace: production
type: kubernetes.io/tls
stringData:
  tls.crt: |
    <PEM-encoded certificate>
  tls.key: |
    <PEM-encoded private key>
```

### Docker Registry Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: registry-credentials
  namespace: production
type: kubernetes.io/dockerconfigjson
stringData:
  .dockerconfigjson: |
    {
      "auths": {
        "myregistry.io": {
          "username": "<registry-username>",
          "password": "<registry-password>",
          "email": "user@example.com",
          "auth": "<base64 of username:password>"
        }
      }
    }
```

### Basic Auth Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: basic-auth
  namespace: production
type: kubernetes.io/basic-auth
stringData:
  username: <username>
  password: <password>
```

### SSH Auth Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ssh-key
  namespace: production
type: kubernetes.io/ssh-auth
stringData:
  ssh-privatekey: |
    <OpenSSH private key>
```

## 使用 ConfigMap 与 Secret

### 环境变量

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
  - name: app
    image: myapp:latest
    env:
    # Single value from ConfigMap
    - name: DATABASE_HOST
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: database.host

    # Single value from Secret
    - name: DATABASE_PASSWORD
      valueFrom:
        secretKeyRef:
          name: app-secrets
          key: db-password

    # All keys from ConfigMap as env vars
    envFrom:
    - configMapRef:
        name: app-config
      prefix: CONFIG_

    # All keys from Secret as env vars
    - secretRef:
        name: app-secrets
      prefix: SECRET_
```

### 卷挂载

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
  - name: app
    image: myapp:latest
    volumeMounts:
    # Mount entire ConfigMap as directory
    - name: config-volume
      mountPath: /etc/config
      readOnly: true

    # Mount specific key as file
    - name: app-properties
      mountPath: /etc/app/app.properties
      subPath: app.properties
      readOnly: true

    # Mount Secret as files
    - name: secrets-volume
      mountPath: /etc/secrets
      readOnly: true

    # Mount TLS certificates
    - name: tls-certs
      mountPath: /etc/tls
      readOnly: true

  volumes:
  - name: config-volume
    configMap:
      name: app-config

  - name: app-properties
    configMap:
      name: app-config
      items:
      - key: app.properties
        path: app.properties

  - name: secrets-volume
    secret:
      secretName: app-secrets
      defaultMode: 0400  # Read-only for owner

  - name: tls-certs
    secret:
      secretName: example-tls
```

## 不可变 ConfigMap 与 Secret

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: immutable-config
  namespace: production
immutable: true
data:
  key: value
---
apiVersion: v1
kind: Secret
metadata:
  name: immutable-secret
  namespace: production
type: Opaque
immutable: true
stringData:
  password: "<password>"
```

## External Secrets Operator

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
  namespace: production
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: SecretStore
  target:
    name: app-secrets
    creationPolicy: Owner
  data:
  - secretKey: db-password
    remoteRef:
      key: prod/database/password
  - secretKey: api-key
    remoteRef:
      key: prod/api/key
---
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: aws-secrets-manager
  namespace: production
spec:
  provider:
    aws:
      service: SecretsManager
      region: us-east-1
      auth:
        jwt:
          serviceAccountRef:
            name: external-secrets-sa
```

## Sealed Secrets（GitOps）

```yaml
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: app-secrets
  namespace: production
spec:
  encryptedData:
    db-password: <sealed-ciphertext>
    api-key: <sealed-ciphertext>
  template:
    metadata:
      name: app-secrets
      namespace: production
    type: Opaque
```

## 环境变量最佳实践

### 结构化环境变量

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
  - name: app
    image: myapp:latest
    env:
    # Application settings
    - name: APP_NAME
      value: "my-application"
    - name: APP_ENV
      value: "production"
    - name: APP_VERSION
      value: "v1.2.0"

    # Database configuration
    - name: DB_HOST
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: database.host
    - name: DB_PORT
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: database.port
    - name: DB_NAME
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: database.name
    - name: DB_USER
      valueFrom:
        secretKeyRef:
          name: app-secrets
          key: db-username
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: app-secrets
          key: db-password

    # Kubernetes metadata
    - name: POD_NAME
      valueFrom:
        fieldRef:
          fieldPath: metadata.name
    - name: POD_NAMESPACE
      valueFrom:
        fieldRef:
          fieldPath: metadata.namespace
    - name: POD_IP
      valueFrom:
        fieldRef:
          fieldPath: status.podIP
    - name: NODE_NAME
      valueFrom:
        fieldRef:
          fieldPath: spec.nodeName

    # Resource limits
    - name: MEMORY_LIMIT
      valueFrom:
        resourceFieldRef:
          containerName: app
          resource: limits.memory
    - name: CPU_REQUEST
      valueFrom:
        resourceFieldRef:
          containerName: app
          resource: requests.cpu
```

## 动态配置更新

```yaml
apiVersion: v1
kind: Deployment
metadata:
  name: app
spec:
  template:
    metadata:
      annotations:
        # Force pod restart on config change
        checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
        checksum/secret: {{ include (print $.Template.BasePath "/secret.yaml") . | sha256sum }}
    spec:
      containers:
      - name: app
        image: myapp:latest
        volumeMounts:
        - name: config
          mountPath: /etc/config
          readOnly: true
      volumes:
      - name: config
        configMap:
          name: app-config
```

## 最佳实践

1. **隔离**：非敏感数据用 ConfigMap，凭据用 Secret
2. **不可变**：生产配置标记为 immutable 更安全
3. **版本管理**：在 ConfigMap/Secret 名称里带版本，便于更新
4. **最小权限**：Secret 以文件挂载并设严格权限（0400）
5. **外部 Secret**：云上密钥管理用 External Secrets Operator
6. **不硬编码**：绝不在容器镜像里硬编码密钥
7. **加密**：为 etcd 中的 Secret 启用静态加密
8. **GitOps**：用 Sealed Secrets 保障 GitOps 流程安全
9. **轮换**：实现密钥轮换策略
10. **校验**：部署前校验配置
