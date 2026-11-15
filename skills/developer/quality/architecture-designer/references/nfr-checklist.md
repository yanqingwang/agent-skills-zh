> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/architecture-designer/references/nfr-checklist.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 非功能需求清单

## NFR 分类

### 可扩展性（Scalability）

| 问题 | 常见目标 |
|----------|----------------|
| 预期并发用户数？ | 100 / 1K / 10K / 100K |
| 每秒请求数？ | 10 / 100 / 1000 / 10000 |
| 数据量？ | GB / TB / PB |
| 增长率？ | 每年 10% / 50% / 100% |
| 峰值与平均负载比？ | 2x / 5x / 10x |

### 性能（Performance）

| 问题 | 常见目标 |
|----------|----------------|
| API 响应时间？ | < 100ms / 200ms / 500ms p95 |
| 页面加载时间？ | < 1s / 2s / 3s |
| 数据库查询时间？ | < 10ms / 50ms / 100ms |
| 批处理吞吐量？ | 1K / 10K / 100K 条记录/小时 |

### 可用性（Availability）

| 目标 | 年停机时间 | 使用场景 |
|--------|---------------|----------|
| 99% | 3.65 天 | 内部工具 |
| 99.9% | 8.76 小时 | 业务应用 |
| 99.95% | 4.38 小时 | 电子商务 |
| 99.99% | 52.6 分钟 | 金融系统 |
| 99.999% | 5.26 分钟 | 生命攸关系统 |

### 安全（Security）

| 问题 | 考虑点 |
|----------|----------------|
| 需要认证（Authentication）吗？ | JWT、OAuth、SAML、MFA |
| 授权（Authorization）模型？ | RBAC、ABAC、ACL |
| 数据敏感级别？ | 公开、内部、机密、PII |
| 合规要求？ | GDPR、HIPAA、PCI DSS、SOC 2 |
| 加密需求？ | 静态、传输中、端到端 |

### 可靠性（Reliability）

| 问题 | 考虑点 |
|----------|----------------|
| 可接受的数据丢失量？ | RPO: 0 / 1hr / 24hr |
| 恢复时间目标？ | RTO: 1hr / 4hr / 24hr |
| 备份频率？ | 实时 / 每小时 / 每天 |
| 灾难恢复？ | 单区域 / 多区域 |

### 可维护性（Maintainability）

| 问题 | 考虑点 |
|----------|----------------|
| 部署频率？ | 每天 / 每周 / 每月 |
| 部署策略？ | 蓝绿、金丝雀、滚动 |
| 监控要求？ | 日志、指标、追踪、告警 |
| 值班要求？ | 24/7、工作时间 |

### 成本（Cost）

| 问题 | 考虑点 |
|----------|----------------|
| 基础设施预算？ | $/月、$/用户、$/请求 |
| 运营预算？ | 维护人力（FTE） |
| 成本优化？ | 预留实例、竞价实例 |
| 成本告警？ | 通知阈值 |

## 模板

```markdown
## Non-Functional Requirements

### Performance
- API response time: < 200ms p95
- Page load time: < 2s
- Database query time: < 50ms

### Scalability
- Concurrent users: 10,000
- Requests per second: 1,000
- Data volume: 1TB

### Availability
- Target: 99.9% (8.76 hours/year downtime)
- RPO: 1 hour
- RTO: 4 hours

### Security
- Authentication: JWT with refresh tokens
- Authorization: Role-based (admin, user, guest)
- Compliance: GDPR, SOC 2

### Observability
- Logging: Structured JSON to ELK
- Metrics: Prometheus + Grafana
- Tracing: OpenTelemetry
- Alerts: PagerDuty integration
```

## 快速参考

| 分类 | 关键指标 |
|----------|------------|
| 性能 | 响应时间（p95） |
| 可扩展性 | 并发用户数、RPS |
| 可用性 | 在线时间百分比 |
| 可靠性 | RPO、RTO |
| 安全 | 合规要求 |
| 成本 | $/月预算 |
