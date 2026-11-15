> **中文汉化版** · 上游：[affaan-m/ECC](https://github.com/affaan-m/ECC) · 原文件：`skills/security-review/cloud-infrastructure-security.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

| name | description |
|------|-------------|
| cloud-infrastructure-security | 部署到云平台、配置基础设施、管理 IAM 策略、设置日志/监控或搭建 CI/CD 流水线时使用此 Skill。提供与最佳实践对齐的云安全检查清单。 |

# 云与基础设施安全 Skill

本 Skill 确保云基础设施、CI/CD 流水线与部署配置遵循安全最佳实践，并符合行业标准。

## 何时激活

- 将应用部署到云平台（AWS、Vercel、Railway、Cloudflare）
- 配置 IAM 角色与权限
- 搭建 CI/CD 流水线
- 实现基础设施即代码（Terraform、CloudFormation）
- 配置日志与监控
- 在云环境中管理密钥
- 配置 CDN 与边缘安全
- 实现灾难恢复与备份策略

## 云安全检查清单

### 1. IAM 与访问控制

#### 最小权限原则

```yaml
# PASS: CORRECT: Minimal permissions
iam_role:
  permissions:
    - s3:GetObject  # Only read access
    - s3:ListBucket
  resources:
    - arn:aws:s3:::my-bucket/*  # Specific bucket only

# FAIL: WRONG: Overly broad permissions
iam_role:
  permissions:
    - s3:*  # All S3 actions
  resources:
    - "*"  # All resources
```

#### 多因素认证（MFA）

```bash
# ALWAYS enable MFA for root/admin accounts
aws iam enable-mfa-device \
  --user-name admin \
  --serial-number arn:aws:iam::123456789:mfa/admin \
  --authentication-code1 123456 \
  --authentication-code2 789012
```

#### 验证步骤

- [ ] 生产环境不使用 root 账户
- [ ] 所有特权账户都启用 MFA
- [ ] 服务账户使用角色，而不是长期凭证
- [ ] IAM 策略遵循最小权限
- [ ] 定期执行访问审查
- [ ] 未使用的凭证已轮换或移除

### 2. 密钥管理

#### 云密钥管理服务

```typescript
// PASS: CORRECT: Use cloud secrets manager
import { SecretsManager } from '@aws-sdk/client-secrets-manager';

const client = new SecretsManager({ region: 'us-east-1' });
const secret = await client.getSecretValue({ SecretId: 'prod/api-key' });
const apiKey = JSON.parse(secret.SecretString).key;

// FAIL: WRONG: Hardcoded or in environment variables only
const apiKey = process.env.API_KEY; // Not rotated, not audited
```

#### 密钥轮换

```bash
# Set up automatic rotation for database credentials
aws secretsmanager rotate-secret \
  --secret-id prod/db-password \
  --rotation-lambda-arn arn:aws:lambda:region:account:function:rotate \
  --rotation-rules AutomaticallyAfterDays=30
```

#### 验证步骤

- [ ] 所有密钥存放在云密钥管理服务（AWS Secrets Manager、Vercel Secrets）
- [ ] 数据库凭证启用自动轮换
- [ ] API 密钥至少每季度轮换一次
- [ ] 代码、日志或错误信息中不出现密钥
- [ ] 密钥访问启用审计日志

### 3. 网络安全

#### VPC 与防火墙配置

```terraform
# PASS: CORRECT: Restricted security group
resource "aws_security_group" "app" {
  name = "app-sg"

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]  # Internal VPC only
  }

  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Only HTTPS outbound
  }
}

# FAIL: WRONG: Open to the internet
resource "aws_security_group" "bad" {
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # All ports, all IPs!
  }
}
```

#### 验证步骤

- [ ] 数据库不可公开访问
- [ ] SSH/RDP 端口仅限 VPN/堡垒机访问
- [ ] 安全组遵循最小权限
- [ ] 已配置网络 ACL
- [ ] 已启用 VPC 流日志

### 4. 日志与监控

#### CloudWatch/日志配置

```typescript
// PASS: CORRECT: Comprehensive logging
import { CloudWatchLogsClient, CreateLogStreamCommand } from '@aws-sdk/client-cloudwatch-logs';

const logSecurityEvent = async (event: SecurityEvent) => {
  await cloudwatch.putLogEvents({
    logGroupName: '/aws/security/events',
    logStreamName: 'authentication',
    logEvents: [{
      timestamp: Date.now(),
      message: JSON.stringify({
        type: event.type,
        userId: event.userId,
        ip: event.ip,
        result: event.result,
        // Never log sensitive data
      })
    }]
  });
};
```

#### 验证步骤

- [ ] 所有服务启用 CloudWatch/日志
- [ ] 记录失败的认证尝试
- [ ] 审计管理员操作
- [ ] 配置日志保留期（合规要求 90 天以上）
- [ ] 为可疑活动配置告警
- [ ] 日志集中存储且防篡改

### 5. CI/CD 流水线安全

#### 安全的流水线配置

```yaml
# PASS: CORRECT: Secure GitHub Actions workflow
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read  # Minimal permissions

    steps:
      - uses: actions/checkout@v4

      # Scan for secrets
      - name: Secret scanning
        uses: trufflesecurity/trufflehog@main

      # Dependency audit
      - name: Audit dependencies
        run: npm audit --audit-level=high

      # Use OIDC, not long-lived tokens
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/GitHubActionsRole
          aws-region: us-east-1
```

#### 供应链安全

```json
// package.json - Use lock files and integrity checks
{
  "scripts": {
    "install": "npm ci",  // Use ci for reproducible builds
    "audit": "npm audit --audit-level=moderate",
    "check": "npm outdated"
  }
}
```

#### 验证步骤

- [ ] 使用 OIDC 而非长期凭证
- [ ] 流水线中包含密钥扫描
- [ ] 依赖漏洞扫描
- [ ] 容器镜像扫描（如适用）
- [ ] 强制分支保护规则
- [ ] 合并前要求代码审查
- [ ] 强制签名提交

### 6. Cloudflare 与 CDN 安全

#### Cloudflare 安全配置

```typescript
// PASS: CORRECT: Cloudflare Workers with security headers
export default {
  async fetch(request: Request): Promise<Response> {
    const response = await fetch(request);

    // Add security headers
    const headers = new Headers(response.headers);
    headers.set('X-Frame-Options', 'DENY');
    headers.set('X-Content-Type-Options', 'nosniff');
    headers.set('Referrer-Policy', 'strict-origin-when-cross-origin');
    headers.set('Permissions-Policy', 'geolocation=(), microphone=()');

    return new Response(response.body, {
      status: response.status,
      headers
    });
  }
};
```

#### WAF 规则

```bash
# Enable Cloudflare WAF managed rules
# - OWASP Core Ruleset
# - Cloudflare Managed Ruleset
# - Rate limiting rules
# - Bot protection
```

#### 验证步骤

- [ ] 启用 WAF 并加载 OWASP 规则
- [ ] 配置速率限制
- [ ] Bot 防护生效
- [ ] 启用 DDoS 防护
- [ ] 配置安全响应头
- [ ] 启用 SSL/TLS 严格模式

### 7. 备份与灾难恢复

#### 自动备份

```terraform
# PASS: CORRECT: Automated RDS backups
resource "aws_db_instance" "main" {
  allocated_storage     = 20
  engine               = "postgres"

  backup_retention_period = 30  # 30 days retention
  backup_window          = "03:00-04:00"
  maintenance_window     = "mon:04:00-mon:05:00"

  enabled_cloudwatch_logs_exports = ["postgresql"]

  deletion_protection = true  # Prevent accidental deletion
}
```

#### 验证步骤

- [ ] 配置每日自动备份
- [ ] 备份保留期满足合规要求
- [ ] 启用时间点恢复
- [ ] 每季度执行备份恢复测试
- [ ] 灾难恢复计划已文档化
- [ ] RPO 与 RTO 已定义并经测试

## 部署前云安全检查清单

任何生产云部署之前：

- [ ] **IAM**：不使用 root 账户、启用 MFA、最小权限策略
- [ ] **密钥**：所有密钥存放在云密钥管理服务并启用轮换
- [ ] **网络**：安全组受限、数据库不公开
- [ ] **日志**：启用 CloudWatch/日志并配置保留期
- [ ] **监控**：为异常配置告警
- [ ] **CI/CD**：OIDC 认证、密钥扫描、依赖审计
- [ ] **CDN/WAF**：启用 Cloudflare WAF 并加载 OWASP 规则
- [ ] **加密**：静态数据与传输数据均已加密
- [ ] **备份**：自动备份且恢复经过测试
- [ ] **合规**：满足 GDPR/HIPAA 要求（如适用）
- [ ] **文档**：基础设施已文档化、运行手册已建立
- [ ] **事件响应**：已有安全事件应对计划

## 常见云安全配置错误

### S3 存储桶暴露

```bash
# FAIL: WRONG: Public bucket
aws s3api put-bucket-acl --bucket my-bucket --acl public-read

# PASS: CORRECT: Private bucket with specific access
aws s3api put-bucket-acl --bucket my-bucket --acl private
aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json
```

### RDS 公开访问

```terraform
# FAIL: WRONG
resource "aws_db_instance" "bad" {
  publicly_accessible = true  # NEVER do this!
}

# PASS: CORRECT
resource "aws_db_instance" "good" {
  publicly_accessible = false
  vpc_security_group_ids = [aws_security_group.db.id]
}
```

## 参考资源

- [AWS 安全最佳实践](https://aws.amazon.com/security/best-practices/)
- [CIS AWS 基础基准](https://www.cisecurity.org/benchmark/amazon_web_services)
- [Cloudflare 安全文档](https://developers.cloudflare.com/security/)
- [OWASP 云安全](https://owasp.org/www-project-cloud-security/)
- [Terraform 安全最佳实践](https://www.terraform.io/docs/cloud/guides/recommended-practices/)

**切记**：云配置错误是数据泄露的首要原因。一个暴露的 S3 存储桶或一条过于宽松的 IAM 策略就可能危及整个基础设施。始终遵循最小权限原则与纵深防御。
