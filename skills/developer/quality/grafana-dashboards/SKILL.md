---
name: grafana-dashboards
description: 创建和管理生产级 Grafana 仪表盘，实时可视化系统与应用指标。用于构建监控仪表盘、可视化指标，或创建运维可观测性界面。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/observability-monitoring/skills/grafana-dashboards/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Grafana 仪表盘

创建和管理生产级的 Grafana 仪表盘，实现全面的系统可观测性。

## 用途

设计高效的 Grafana 仪表盘，用于监控应用、基础设施和业务指标。

## 何时使用

- 可视化 Prometheus 指标
- 创建自定义仪表盘
- 实现 SLO 仪表盘
- 监控基础设施
- 跟踪业务 KPIs

## 仪表盘设计原则

### 1. 信息层级


```
┌─────────────────────────────────────┐
│  Critical Metrics (Big Numbers)     │
├─────────────────────────────────────┤
│  Key Trends (Time Series)           │
├─────────────────────────────────────┤
│  Detailed Metrics (Tables/Heatmaps) │
└─────────────────────────────────────┘
```


### 2. RED 方法（服务）

- **Rate** - 每秒请求数
- **Errors** - 错误率
- **Duration** - 延迟/响应时间

### 3. USE 方法（资源）

- **Utilization** - 资源忙碌时间占比（%）
- **Saturation** - 队列长度/等待时间
- **Errors** - 错误计数

## 仪表盘结构

### API 监控仪表盘


```json
{
  "dashboard": {
    "title": "API Monitoring",
    "tags": ["api", "production"],
    "timezone": "browser",
    "refresh": "30s",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total[5m])) by (service)",
            "legendFormat": "{{service}}"
          }
        ],
        "gridPos": { "x": 0, "y": 0, "w": 12, "h": 8 }
      },
      {
        "title": "Error Rate %",
        "type": "graph",
        "targets": [
          {
            "expr": "(sum(rate(http_requests_total{status=~\"5..\"}[5m])) / sum(rate(http_requests_total[5m]))) * 100",
            "legendFormat": "Error Rate"
          }
        ],
        "alert": {
          "conditions": [
            {
              "evaluator": { "params": [5], "type": "gt" },
              "operator": { "type": "and" },
              "query": { "params": ["A", "5m", "now"] },
              "type": "query"
            }
          ]
        },
        "gridPos": { "x": 12, "y": 0, "w": 12, "h": 8 }
      },
      {
        "title": "P95 Latency",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service))",
            "legendFormat": "{{service}}"
          }
        ],
        "gridPos": { "x": 0, "y": 8, "w": 24, "h": 8 }
      }
    ]
  }
}
```


## 面板类型

### 1. 统计面板（单值）


```json
{
  "type": "stat",
  "title": "Total Requests",
  "targets": [
    {
      "expr": "sum(http_requests_total)"
    }
  ],
  "options": {
    "reduceOptions": {
      "values": false,
      "calcs": ["lastNotNull"]
    },
    "orientation": "auto",
    "textMode": "auto",
    "colorMode": "value"
  },
  "fieldConfig": {
    "defaults": {
      "thresholds": {
        "mode": "absolute",
        "steps": [
          { "value": 0, "color": "green" },
          { "value": 80, "color": "yellow" },
          { "value": 90, "color": "red" }
        ]
      }
    }
  }
}
```


### 2. 时序图


```json
{
  "type": "graph",
  "title": "CPU Usage",
  "targets": [
    {
      "expr": "100 - (avg by (instance) (rate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)"
    }
  ],
  "yaxes": [
    { "format": "percent", "max": 100, "min": 0 },
    { "format": "short" }
  ]
}
```


### 3. 表格面板


```json
{
  "type": "table",
  "title": "Service Status",
  "targets": [
    {
      "expr": "up",
      "format": "table",
      "instant": true
    }
  ],
  "transformations": [
    {
      "id": "organize",
      "options": {
        "excludeByName": { "Time": true },
        "indexByName": {},
        "renameByName": {
          "instance": "Instance",
          "job": "Service",
          "Value": "Status"
        }
      }
    }
  ]
}
```


### 4. 热力图


```json
{
  "type": "heatmap",
  "title": "Latency Heatmap",
  "targets": [
    {
      "expr": "sum(rate(http_request_duration_seconds_bucket[5m])) by (le)",
      "format": "heatmap"
    }
  ],
  "dataFormat": "tsbuckets",
  "yAxis": {
    "format": "s"
  }
}
```


## 变量

### 查询变量


```json
{
  "templating": {
    "list": [
      {
        "name": "namespace",
        "type": "query",
        "datasource": "Prometheus",
        "query": "label_values(kube_pod_info, namespace)",
        "refresh": 1,
        "multi": false
      },
      {
        "name": "service",
        "type": "query",
        "datasource": "Prometheus",
        "query": "label_values(kube_service_info{namespace=\"$namespace\"}, service)",
        "refresh": 1,
        "multi": true
      }
    ]
  }
}
```


### 在查询中使用变量


```
sum(rate(http_requests_total{namespace="$namespace", service=~"$service"}[5m]))
```


## 仪表盘中的告警


```json
{
  "alert": {
    "name": "High Error Rate",
    "conditions": [
      {
        "evaluator": {
          "params": [5],
          "type": "gt"
        },
        "operator": { "type": "and" },
        "query": {
          "params": ["A", "5m", "now"]
        },
        "reducer": { "type": "avg" },
        "type": "query"
      }
    ],
    "executionErrorState": "alerting",
    "for": "5m",
    "frequency": "1m",
    "message": "Error rate is above 5%",
    "noDataState": "no_data",
    "notifications": [{ "uid": "slack-channel" }]
  }
}
```


## 仪表盘预配置

**dashboards.yml:**


```yaml
apiVersion: 1

providers:
  - name: "default"
    orgId: 1
    folder: "General"
    type: file
    disableDeletion: false
    updateIntervalSeconds: 10
    allowUiUpdates: true
    options:
      path: /etc/grafana/dashboards
```


## 常见仪表盘模式

### 基础设施仪表盘

**关键面板：**

- 每个节点的 CPU 使用率
- 每个节点的内存使用量
- 磁盘 I/O
- 网络流量
- 按 namespace 统计的 Pod 数
- 节点状态

### 数据库仪表盘

**关键面板：**

- 每秒查询数
- 连接池使用率
- 查询延迟（P50, P95, P99）
- 活跃连接数
- 数据库大小
- 复制延迟
- 慢查询

### 应用仪表盘

**关键面板：**

- 请求速率
- 错误率
- 响应时间（百分位）
- 活跃用户/会话
- 缓存命中率
- 队列长度

## 最佳实践

1. **从模板入手**（Grafana 社区仪表盘）
2. **为面板和变量使用一致的命名**
3. **把相关指标分组到行中**
4. **设置合适的时间范围**（默认：最近 6 小时）
5. **使用变量**以保持灵活性
6. **添加面板描述**以提供上下文
7. **正确配置单位**
8. **为颜色设置有意义的阈值**
9. **跨仪表盘使用一致的颜色**
10. **用不同的时间范围进行测试**

## 仪表盘即代码

### Terraform 预配置


```hcl
resource "grafana_dashboard" "api_monitoring" {
  config_json = file("${path.module}/dashboards/api-monitoring.json")
  folder      = grafana_folder.monitoring.id
}

resource "grafana_folder" "monitoring" {
  title = "Production Monitoring"
}
```


### Ansible 预配置


```yaml
- name: Deploy Grafana dashboards
  copy:
    src: "{{ item }}"
    dest: /etc/grafana/dashboards/
  with_fileglob:
    - "dashboards/*.json"
  notify: restart grafana
```



## 相关 Skill

- `prometheus-configuration` - 用于指标采集
- `slo-implementation` - 用于 SLO 仪表盘
