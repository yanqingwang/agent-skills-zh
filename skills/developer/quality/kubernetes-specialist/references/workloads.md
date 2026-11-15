> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/developer/quality/kubernetes-specialist/references/workloads.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Kubernetes 工作负载

## Deployment 模式

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: production
  labels:
    app: web-app
    tier: frontend
spec:
  replicas: 3
  revisionHistoryLimit: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
        tier: frontend
        version: v1.2.0
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
    spec:
      serviceAccountName: web-app-sa
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 2000
      containers:
      - name: app
        image: myregistry.io/web-app:v1.2.0
        imagePullPolicy: IfNotPresent
        ports:
        - name: http
          containerPort: 8080
          protocol: TCP
        env:
        - name: ENVIRONMENT
          value: production
        - name: DB_HOST
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: database.host
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: db-password
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: http
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /ready
            port: http
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 2
        volumeMounts:
        - name: config
          mountPath: /etc/config
          readOnly: true
        - name: cache
          mountPath: /var/cache
      volumes:
      - name: config
        configMap:
          name: app-config
      - name: cache
        emptyDir: {}
```

## StatefulSet 模式

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
  namespace: database
spec:
  serviceName: postgres-headless
  replicas: 3
  podManagementPolicy: OrderedReady
  updateStrategy:
    type: RollingUpdate
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      serviceAccountName: postgres-sa
      securityContext:
        runAsUser: 999
        fsGroup: 999
      containers:
      - name: postgres
        image: postgres:15-alpine
        ports:
        - name: postgres
          containerPort: 5432
        env:
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-secrets
              key: password
        - name: PGDATA
          value: /var/lib/postgresql/data/pgdata
        resources:
          requests:
            cpu: 500m
            memory: 1Gi
          limits:
            cpu: 2000m
            memory: 4Gi
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
        livenessProbe:
          exec:
            command:
            - pg_isready
            - -U
            - postgres
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          exec:
            command:
            - pg_isready
            - -U
            - postgres
          initialDelaySeconds: 10
          periodSeconds: 5
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: fast-ssd
      resources:
        requests:
          storage: 50Gi
```

## DaemonSet 模式

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: node-exporter
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      hostNetwork: true
      hostPID: true
      serviceAccountName: node-exporter-sa
      tolerations:
      - effect: NoSchedule
        operator: Exists
      containers:
      - name: node-exporter
        image: prom/node-exporter:latest
        args:
        - --path.procfs=/host/proc
        - --path.sysfs=/host/sys
        - --collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)
        ports:
        - name: metrics
          containerPort: 9100
          protocol: TCP
        resources:
          requests:
            cpu: 50m
            memory: 64Mi
          limits:
            cpu: 200m
            memory: 128Mi
        volumeMounts:
        - name: proc
          mountPath: /host/proc
          readOnly: true
        - name: sys
          mountPath: /host/sys
          readOnly: true
      volumes:
      - name: proc
        hostPath:
          path: /proc
      - name: sys
        hostPath:
          path: /sys
```

## Job 模式

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migration-20231214
  namespace: production
spec:
  backoffLimit: 3
  ttlSecondsAfterFinished: 3600
  template:
    metadata:
      labels:
        app: db-migration
    spec:
      restartPolicy: OnFailure
      serviceAccountName: migration-sa
      containers:
      - name: migrate
        image: myregistry.io/migrations:v1.2.0
        command: ["/bin/sh", "-c"]
        args:
        - |
          echo "Starting migration..."
          /app/migrate up
          echo "Migration complete"
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secrets
              key: connection-string
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
```

## CronJob 模式

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: backup-database
  namespace: production
spec:
  schedule: "0 2 * * *"  # Daily at 2 AM
  timeZone: "America/New_York"
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      backoffLimit: 2
      ttlSecondsAfterFinished: 86400
      template:
        metadata:
          labels:
            app: backup
        spec:
          restartPolicy: OnFailure
          serviceAccountName: backup-sa
          containers:
          - name: backup
            image: myregistry.io/backup-tool:latest
            command: ["/usr/local/bin/backup.sh"]
            env:
            - name: S3_BUCKET
              valueFrom:
                configMapKeyRef:
                  name: backup-config
                  key: s3-bucket
            - name: AWS_ACCESS_KEY_ID
              valueFrom:
                secretKeyRef:
                  name: backup-secrets
                  key: aws-access-key
            - name: AWS_SECRET_ACCESS_KEY
              valueFrom:
                secretKeyRef:
                  name: backup-secrets
                  key: aws-secret-key
            resources:
              requests:
                cpu: 200m
                memory: 256Mi
              limits:
                cpu: 1000m
                memory: 1Gi
            volumeMounts:
            - name: backup-volume
              mountPath: /backup
          volumes:
          - name: backup-volume
            emptyDir:
              sizeLimit: 10Gi
```

## Init 容器

```yaml
spec:
  initContainers:
  - name: wait-for-db
    image: busybox:latest
    command: ['sh', '-c']
    args:
    - |
      until nc -z postgres-service 5432; do
        echo "Waiting for database..."
        sleep 2
      done
      echo "Database is ready"
  - name: migrate-schema
    image: myregistry.io/migrations:latest
    command: ["/app/migrate", "up"]
    env:
    - name: DATABASE_URL
      valueFrom:
        secretKeyRef:
          name: db-secrets
          key: url
  containers:
  - name: app
    image: myregistry.io/app:latest
```

## 最佳实践

1. **资源管理**：始终设置 requests 与 limits
2. **健康检查**：同时包含存活与就绪探针
3. **安全**：尽量用非 root 用户、只读文件系统
4. **标签**：标签保持一致，便于组织与选择
5. **更新策略**：选合适的策略（RollingUpdate、Recreate）
6. **Service Account**：绝不用 default，建专用 SA
7. **镜像标签**：用具体版本，生产环境别用 `latest`
8. **清理**：给 Job 设 TTL，自动清理已完成的 Pod
