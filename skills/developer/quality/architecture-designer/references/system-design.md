> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/architecture-designer/references/system-design.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 系统设计模板

## 设计模板

```markdown
# System: {System Name}

## Requirements

### Functional
- [What the system must do]
- [Core features and capabilities]

### Non-Functional
- **Performance**: Response time < 200ms p95
- **Availability**: 99.9% uptime (8.76 hours downtime/year)
- **Scalability**: Support 10,000 concurrent users
- **Security**: PCI DSS compliance required

### Constraints
- Budget: $X/month for infrastructure
- Timeline: MVP in 3 months
- Team: 5 backend, 3 frontend engineers

## High-Level Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│  API Gateway │────▶│  Service    │
│   (Web)     │     │   (Kong)    │     │  (Node.js)  │
└─────────────┘     └─────────────┘     └─────────────┘
                           │                   │
                           ▼                   ▼
                    ┌─────────────┐     ┌─────────────┐
                    │    Auth     │     │  Database   │
                    │  (Auth0)    │     │ (PostgreSQL)│
                    └─────────────┘     └─────────────┘
```

## Component Details

### API Layer
- Technology: Node.js with Express/NestJS
- Responsibilities: Request routing, validation, auth
- Scaling: Horizontal via load balancer

### Data Layer
- Primary: PostgreSQL (transactions, relationships)
- Cache: Redis (sessions, hot data)
- Storage: S3 (files, images)

### External Services
- Auth: Auth0 (SSO, MFA)
- Email: SendGrid (transactional)
- Monitoring: Datadog (APM, logs)

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| PostgreSQL over MongoDB | Relational data, ACID needed |
| Redis for caching | Sub-ms latency required |
| Auth0 over custom | Reduce security risk |

## Scaling Strategy

### Current (MVP)
- Single region deployment
- 2 API instances behind ALB
- Single RDS instance

### Future (10x growth)
- Multi-region with CDN
- Auto-scaling API (2-10 instances)
- RDS read replicas

## Security Considerations
- All traffic over TLS 1.3
- JWT tokens with 15-min expiry
- Rate limiting: 100 req/min per user
- WAF for common attacks

## Failure Modes

| Failure | Impact | Mitigation |
|---------|--------|------------|
| DB down | Full outage | Multi-AZ failover |
| Cache down | Degraded perf | Fallback to DB |
| Auth down | No new logins | Cache valid tokens |
```

## 快速参考

| 节 | 关键问题 |
|---------|---------------|
| Requirements | 它必须做什么？做到什么程度？ |
| Architecture | 有哪些组件？如何连接？ |
| Decisions | 为什么选这些方案？ |
| Scaling | 如何增长？ |
| Failures | 什么会坏？如何恢复？ |
