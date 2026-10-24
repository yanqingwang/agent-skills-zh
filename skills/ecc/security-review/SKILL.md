---
name: security-review
description: 在添加身份验证（authentication）、处理用户输入、处理密钥（secrets）、创建 API 端点或实现支付/敏感功能时使用本 Skill。提供全面的安全检查清单与安全模式。
metadata:
  origin: ECC
---

> **中文汉化版** · 上游：[affaan-m/ECC](https://github.com/affaan-m/ECC) · 原文件：`skills/security-review/SKILL.md` · License: MIT
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 安全审查 Skill

本 Skill 确保所有代码遵循安全最佳实践，并识别潜在漏洞。

## 何时激活

- 实现身份验证（authentication）或授权（authorization）
- 处理用户输入或文件上传
- 创建新的 API 端点
- 处理密钥（secrets）或凭证（credentials）
- 实现支付功能
- 存储或传输敏感数据
- 集成第三方 API

## 安全检查清单

### 1. 密钥管理（Secrets Management）

#### FAIL：绝对不要这样做
```typescript
const apiKey = "sk-proj-xxxxx"  // Hardcoded secret
const dbPassword = "password123" // In source code
```

#### PASS：务必这样做
```typescript
const apiKey = process.env.OPENAI_API_KEY
const dbUrl = process.env.DATABASE_URL

// Verify secrets exist
if (!apiKey) {
  throw new Error('OPENAI_API_KEY not configured')
}
```

#### 验证步骤
- [ ] 没有硬编码的 API key、token 或密码
- [ ] 所有密钥（secrets）都存放在环境变量中
- [ ] `.env.local` 已加入 .gitignore
- [ ] git 历史中没有密钥
- [ ] 生产环境密钥配置在托管平台上（Vercel、Railway）

### 2. 输入验证（Input Validation）

#### 始终验证用户输入
```typescript
import { z } from 'zod'

// Define validation schema
const CreateUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  age: z.number().int().min(0).max(150)
})

// Validate before processing
export async function createUser(input: unknown) {
  try {
    const validated = CreateUserSchema.parse(input)
    return await db.users.create(validated)
  } catch (error) {
    if (error instanceof z.ZodError) {
      return { success: false, errors: error.issues }
    }
    throw error
  }
}
```

#### 文件上传验证
```typescript
function validateFileUpload(file: File) {
  // Size check (5MB max)
  const maxSize = 5 * 1024 * 1024
  if (file.size > maxSize) {
    throw new Error('File too large (max 5MB)')
  }

  // Type check
  const allowedTypes = ['image/jpeg', 'image/png', 'image/gif']
  if (!allowedTypes.includes(file.type)) {
    throw new Error('Invalid file type')
  }

  // Extension check
  const allowedExtensions = ['.jpg', '.jpeg', '.png', '.gif']
  const extension = file.name.toLowerCase().match(/\.[^.]+$/)?.[0]
  if (!extension || !allowedExtensions.includes(extension)) {
    throw new Error('Invalid file extension')
  }

  return true
}
```

#### 验证步骤
- [ ] 所有用户输入都经过 schema 验证
- [ ] 文件上传已受限（大小、类型、扩展名）
- [ ] 用户输入没有直接用于查询
- [ ] 白名单验证（而非黑名单）
- [ ] 错误消息不泄露敏感信息

### 3. SQL 注入（SQL Injection）防护

#### FAIL：绝对不要拼接 SQL
```typescript
// DANGEROUS - SQL Injection vulnerability
const query = `SELECT * FROM users WHERE email = '${userEmail}'`
await db.query(query)
```

#### PASS：始终使用参数化查询（parameterized queries）
```typescript
// Safe - parameterized query
const { data } = await supabase
  .from('users')
  .select('*')
  .eq('email', userEmail)

// Or with raw SQL -- the value goes in the params array, never in the
// string. Use your driver's placeholder syntax (Postgres numbers its
// placeholders, MySQL uses "?").
await db.query(
  'SELECT * FROM users WHERE email = ?',
  [userEmail]
)
```

<!-- Do not write a literal dollar-sign-N placeholder anywhere in this file.
     Invoking this skill with arguments substitutes it away, and the example
     above then renders as concatenated SQL -- the exact anti-pattern this
     section warns against. Use "?" and name the Postgres form in prose. -->

#### 验证步骤
- [ ] 所有数据库查询都使用参数化查询
- [ ] SQL 中没有字符串拼接
- [ ] ORM/查询构建器使用正确
- [ ] Supabase 查询已正确净化（sanitize）

### 4. 身份验证与授权（Authentication & Authorization）

#### JWT token 处理
```typescript
// FAIL: WRONG: localStorage (vulnerable to XSS)
localStorage.setItem('token', token)

// PASS: CORRECT: httpOnly cookies
res.setHeader('Set-Cookie',
  `token=${token}; HttpOnly; Secure; SameSite=Strict; Max-Age=3600`)
```

#### 授权检查
```typescript
export async function deleteUser(userId: string, requesterId: string) {
  // ALWAYS verify authorization first
  const requester = await db.users.findUnique({
    where: { id: requesterId }
  })

  if (requester.role !== 'admin') {
    return NextResponse.json(
      { error: 'Unauthorized' },
      { status: 403 }
    )
  }

  // Proceed with deletion
  await db.users.delete({ where: { id: userId } })
}
```

#### 行级安全（Row Level Security，Supabase）
```sql
-- Enable RLS on all tables
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Users can only view their own data
CREATE POLICY "Users view own data"
  ON users FOR SELECT
  USING (auth.uid() = id);

-- Users can only update their own data
CREATE POLICY "Users update own data"
  ON users FOR UPDATE
  USING (auth.uid() = id);
```

#### 验证步骤
- [ ] token 存储在 httpOnly cookie 中（而非 localStorage）
- [ ] 敏感操作前进行授权检查
- [ ] Supabase 中已启用行级安全（Row Level Security）
- [ ] 已实现基于角色的访问控制（role-based access control）
- [ ] 会话（session）管理安全

### 5. XSS（跨站脚本）防护

#### 净化 HTML（sanitize）
```typescript
import DOMPurify from 'isomorphic-dompurify'

// ALWAYS sanitize user-provided HTML
function renderUserContent(html: string) {
  const clean = DOMPurify.sanitize(html, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'p'],
    ALLOWED_ATTR: []
  })
  return <div dangerouslySetInnerHTML={{ __html: clean }} />
}
```

#### 内容安全策略（Content Security Policy，CSP）

一开始就采取严格策略，只有在有明确记录的移除计划时才放宽。不要默认使用
`'unsafe-inline'` 或 `'unsafe-eval'`；它们会大幅削弱 CSP 的保护效果，应被视为临时的兼容性欠账。

```typescript
// next.config.js
const securityHeaders = [
  {
    key: 'Content-Security-Policy',
    value: `
      default-src 'self';
      base-uri 'self';
      object-src 'none';
      frame-ancestors 'none';
      script-src 'self';
      style-src 'self';
      img-src 'self' data: https:;
      font-src 'self';
      connect-src 'self' https://api.example.com;
    `.replace(/\s{2,}/g, ' ').trim()
  }
]
```

#### 验证步骤
- [ ] 用户提供的 HTML 已净化
- [ ] 已配置 CSP 头
- [ ] 没有未经校验的动态内容渲染
- [ ] 使用了 React 内置的 XSS 防护

### 6. CSRF（跨站请求伪造）防护

#### CSRF token
```typescript
import { csrf } from '@/lib/csrf'

export async function POST(request: Request) {
  const token = request.headers.get('X-CSRF-Token')

  if (!csrf.verify(token)) {
    return NextResponse.json(
      { error: 'Invalid CSRF token' },
      { status: 403 }
    )
  }

  // Process request
}
```

#### SameSite cookie
```typescript
res.setHeader('Set-Cookie',
  `session=${sessionId}; HttpOnly; Secure; SameSite=Strict`)
```

#### 验证步骤
- [ ] 更改状态的操作上有 CSRF token
- [ ] 所有 cookie 都设置 SameSite=Strict
- [ ] 已实现双重提交 cookie 模式（double-submit cookie pattern）

### 7. 速率限制（Rate Limiting）

#### API 速率限制
```typescript
import rateLimit from 'express-rate-limit'

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  message: 'Too many requests'
})

// Apply to routes
app.use('/api/', limiter)
```

#### 高开销操作
```typescript
// Aggressive rate limiting for searches
const searchLimiter = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 10, // 10 requests per minute
  message: 'Too many search requests'
})

app.use('/api/search', searchLimiter)
```

#### 验证步骤
- [ ] 所有 API 端点都有速率限制
- [ ] 高开销操作有更严格的限制
- [ ] 基于 IP 的速率限制
- [ ] 基于用户的速率限制（已认证用户）

### 8. 敏感数据泄露（Sensitive Data Exposure）

#### 日志
```typescript
// FAIL: WRONG: Logging sensitive data
console.log('User login:', { email, password })
console.log('Payment:', { cardNumber, cvv })

// PASS: CORRECT: Redact sensitive data
console.log('User login:', { email, userId })
console.log('Payment:', { last4: card.last4, userId })
```

#### 错误消息
```typescript
// FAIL: WRONG: Exposing internal details
catch (error) {
  return NextResponse.json(
    { error: error.message, stack: error.stack },
    { status: 500 }
  )
}

// PASS: CORRECT: Generic error messages
catch (error) {
  console.error('Internal error:', error)
  return NextResponse.json(
    { error: 'An error occurred. Please try again.' },
    { status: 500 }
  )
}
```

#### 验证步骤
- [ ] 日志中没有密码、token 或密钥
- [ ] 面向用户的错误消息保持通用
- [ ] 详细错误只记录在服务器日志中
- [ ] 不向用户暴露堆栈跟踪（stack trace）

### 9. 区块链安全（Solana）

#### 钱包验证
```typescript
import { verify } from '@solana/web3.js'

async function verifyWalletOwnership(
  publicKey: string,
  signature: string,
  message: string
) {
  try {
    const isValid = verify(
      Buffer.from(message),
      Buffer.from(signature, 'base64'),
      Buffer.from(publicKey, 'base64')
    )
    return isValid
  } catch (error) {
    return false
  }
}
```

#### 交易验证
```typescript
async function verifyTransaction(transaction: Transaction) {
  // Verify recipient
  if (transaction.to !== expectedRecipient) {
    throw new Error('Invalid recipient')
  }

  // Verify amount
  if (transaction.amount > maxAmount) {
    throw new Error('Amount exceeds limit')
  }

  // Verify user has sufficient balance
  const balance = await getBalance(transaction.from)
  if (balance < transaction.amount) {
    throw new Error('Insufficient balance')
  }

  return true
}
```

#### 验证步骤
- [ ] 钱包签名已验证
- [ ] 交易详情已校验
- [ ] 交易前进行余额检查
- [ ] 不盲目签署交易

### 10. 依赖安全（Dependency Security）

#### 定期更新
```bash
# Check for vulnerabilities
npm audit

# Fix automatically fixable issues
npm audit fix

# Update dependencies
npm update

# Check for outdated packages
npm outdated
```

#### 锁文件（lock file）
```bash
# ALWAYS commit lock files
git add package-lock.json

# Use in CI/CD for reproducible builds
npm ci  # Instead of npm install
```

#### 验证步骤
- [ ] 依赖保持最新
- [ ] 没有已知漏洞（npm audit 通过）
- [ ] 锁文件（lock file）已提交
- [ ] GitHub 上启用了 Dependabot
- [ ] 定期进行安全更新

## 安全测试

### 自动化安全测试
```typescript
// Test authentication
test('requires authentication', async () => {
  const response = await fetch('/api/protected')
  expect(response.status).toBe(401)
})

// Test authorization
test('requires admin role', async () => {
  const response = await fetch('/api/admin', {
    headers: { Authorization: `Bearer ${userToken}` }
  })
  expect(response.status).toBe(403)
})

// Test input validation
test('rejects invalid input', async () => {
  const response = await fetch('/api/users', {
    method: 'POST',
    body: JSON.stringify({ email: 'not-an-email' })
  })
  expect(response.status).toBe(400)
})

// Test rate limiting
test('enforces rate limits', async () => {
  const requests = Array(101).fill(null).map(() =>
    fetch('/api/endpoint')
  )

  const responses = await Promise.all(requests)
  const tooManyRequests = responses.filter(r => r.status === 429)

  expect(tooManyRequests.length).toBeGreaterThan(0)
})
```

## 部署前安全检查清单

在任何生产部署之前：

- [ ] **密钥（Secrets）**：没有硬编码密钥，全部存于环境变量
- [ ] **输入验证**：所有用户输入均已验证
- [ ] **SQL 注入**：所有查询均已参数化
- [ ] **XSS**：用户内容已净化
- [ ] **CSRF**：防护已启用
- [ ] **身份验证**：token 处理正确
- [ ] **授权**：角色检查到位
- [ ] **速率限制**：所有端点均已启用
- [ ] **HTTPS**：生产环境强制使用
- [ ] **安全头**：CSP、X-Frame-Options 已配置
- [ ] **错误处理**：错误中不含敏感数据
- [ ] **日志**：未记录敏感数据
- [ ] **依赖**：保持最新，无漏洞
- [ ] **行级安全**：已在 Supabase 中启用
- [ ] **CORS**：已正确配置
- [ ] **文件上传**：已验证（大小、类型）
- [ ] **钱包签名**：已验证（如涉及区块链）

## 资源

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Next.js Security](https://nextjs.org/docs/security)
- [Supabase Security](https://supabase.com/docs/guides/auth)
- [Web Security Academy](https://portswigger.net/web-security)

---

**谨记**：安全不是可选项。一个漏洞就可能危及整个平台。拿不准时，宁可偏向谨慎一侧。
