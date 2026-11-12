---
name: "email-template-builder"
description: "当新增或改造事务性邮件时使用（React Email 模板、Resend、Postmark、SendGrid 或 SES、预览、i18n、暗色模式、送达率）。端到端构建模板系统与服务商集成。"
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`engineering-team/skills/email-template-builder/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 邮件模板构建器

**Tier:** POWERFUL
**Category:** 工程团队
**Domain:** 事务性邮件 / 通信基础设施

---

## 概述

构建完整的事务性邮件系统：React Email 模板、服务商集成、预览服务器、i18n 支持、暗色模式、垃圾邮件优化和分析追踪。产出可用于 Resend、Postmark、SendGrid 或 AWS SES 的生产级代码。

---

## 核心能力

- React Email 模板（欢迎、验证、密码重置、发票、通知、摘要）
- MJML 模板，最大限度兼容各类邮件客户端
- 多服务商支持，提供统一的发送接口
- 带热重载的本地预览服务器
- 带类型化翻译键的 i18n / 本地化
- 使用媒体查询支持暗色模式
- 垃圾邮件评分优化清单
- 通过 UTM 参数追踪打开 / 点击

---

## 适用场景

- 为新产品搭建事务性邮件
- 从旧邮件系统迁移
- 新增邮件类型（发票、摘要、通知）
- 调试邮件送达率问题
- 为邮件模板实现 i18n

---

## 项目结构


```
emails/
├── components/
│   ├── layout/
│   │   ├── email-layout.tsx       # Base layout with brand header/footer
│   │   └── email-button.tsx       # CTA button component
│   ├── partials/
│   │   ├── header.tsx
│   │   └── footer.tsx
├── templates/
│   ├── welcome.tsx
│   ├── verify-email.tsx
│   ├── password-reset.tsx
│   ├── invoice.tsx
│   ├── notification.tsx
│   └── weekly-digest.tsx
├── lib/
│   ├── send.ts                    # Unified send function
│   ├── providers/
│   │   ├── resend.ts
│   │   ├── postmark.ts
│   │   └── ses.ts
│   └── tracking.ts                # UTM + analytics
├── i18n/
│   ├── en.ts
│   └── de.ts
└── preview/                       # Dev preview server
    └── server.ts
```


---

## 基础邮件布局


```tsx
// emails/components/layout/email-layout.tsx
import {
  Body, Container, Head, Html, Img, Preview, Section, Text, Hr, Font
} from "@react-email/components"

interface EmailLayoutProps {
  preview: string
  children: React.ReactNode
}

export function EmailLayout({ preview, children }: EmailLayoutProps) {
  return (
    <Html lang="en">
      <Head>
        <Font
          fontFamily="Inter"
          fallbackFontFamily="Arial"
          webFont={{ url: "https://fonts.gstatic.com/s/inter/v13/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuLyfAZ9hiJ-Ek-_EeA.woff2", format: "woff2" }}
          fontWeight={400}
          fontStyle="normal"
        />
        {/* Dark mode styles */}
        <style>{`
          @media (prefers-color-scheme: dark) {
            .email-body { background-color: #0f0f0f !important; }
            .email-container { background-color: #1a1a1a !important; }
            .email-text { color: #e5e5e5 !important; }
            .email-heading { color: #ffffff !important; }
            .email-divider { border-color: #333333 !important; }
          }
        `}</style>
      </Head>
      <Preview>{preview}</Preview>
      <Body className="email-body" style={styles.body}>
        <Container className="email-container" style={styles.container}>
          {/* Header */}
          <Section style={styles.header}>
            <Img src="https://yourapp.com/logo.png" width={120} height={40} alt="MyApp" />
          </Section>

          {/* Content */}
          <Section style={styles.content}>
            {children}
          </Section>

          {/* Footer */}
          <Hr style={styles.divider} />
          <Section style={styles.footer}>
            <Text style={styles.footerText}>
              MyApp Inc. · 123 Main St · San Francisco, CA 94105
            </Text>
            <Text style={styles.footerText}>
              <a href="{{unsubscribe_url}}" style={styles.link}>Unsubscribe</a>
              {" · "}
              <a href="https://yourapp.com/privacy" style={styles.link}>Privacy Policy</a>
            </Text>
          </Section>
        </Container>
      </Body>
    </Html>
  )
}

const styles = {
  body: { backgroundColor: "#f5f5f5", fontFamily: "Inter, Arial, sans-serif" },
  container: { maxWidth: "600px", margin: "0 auto", backgroundColor: "#ffffff", borderRadius: "8px", overflow: "hidden" },
  header: { padding: "24px 32px", borderBottom: "1px solid #e5e5e5" },
  content: { padding: "32px" },
  divider: { borderColor: "#e5e5e5", margin: "0 32px" },
  footer: { padding: "24px 32px" },
  footerText: { fontSize: "12px", color: "#6b7280", textAlign: "center" as const, margin: "4px 0" },
  link: { color: "#6b7280", textDecoration: "underline" },
}
```


---

## 欢迎邮件


```tsx
// emails/templates/welcome.tsx
import { Button, Heading, Text } from "@react-email/components"
import { EmailLayout } from "../components/layout/email-layout"

interface WelcomeEmailProps {
  name: "string"
  confirmUrl: string
  trialDays?: number
}

export function WelcomeEmail({ name, confirmUrl, trialDays = 14 }: WelcomeEmailProps) {
  return (
    <EmailLayout preview={`Welcome to MyApp, ${name}! Confirm your email to get started.`}>
      <Heading style={styles.h1}>Welcome to MyApp, {name}!</Heading>
      <Text style={styles.text}>
        We're excited to have you on board. You've got {trialDays} days to explore everything MyApp has to offer — no credit card required.
      </Text>
      <Text style={styles.text}>
        First, confirm your email address to activate your account:
      </Text>
      <Button href={confirmUrl} style={styles.button}>
        Confirm Email Address
      </Button>
      <Text style={styles.hint}>
        Button not working? Copy and paste this link into your browser:
        <br />
        <a href={confirmUrl} style={styles.link}>{confirmUrl}</a>
      </Text>
      <Text style={styles.text}>
        Once confirmed, you can:
      </Text>
      <ul style={styles.list}>
        <li>Connect your first project in 2 minutes</li>
        <li>Invite your team (free for up to 3 members)</li>
        <li>Set up Slack notifications</li>
      </ul>
    </EmailLayout>
  )
}

export default WelcomeEmail

const styles = {
  h1: { fontSize: "28px", fontWeight: "700", color: "#111827", margin: "0 0 16px" },
  text: { fontSize: "16px", lineHeight: "1.6", color: "#374151", margin: "0 0 16px" },
  button: { backgroundColor: "#4f46e5", color: "#ffffff", borderRadius: "6px", fontSize: "16px", fontWeight: "600", padding: "12px 24px", textDecoration: "none", display: "inline-block", margin: "8px 0 24px" },
  hint: { fontSize: "13px", color: "#6b7280" },
  link: { color: "#4f46e5" },
  list: { fontSize: "16px", lineHeight: "1.8", color: "#374151", paddingLeft: "20px" },
}
```


---

## 发票邮件


```tsx
// emails/templates/invoice.tsx
import { Row, Column, Section, Heading, Text, Hr, Button } from "@react-email/components"
import { EmailLayout } from "../components/layout/email-layout"

interface InvoiceItem { description: string; amount: number }

interface InvoiceEmailProps {
  name: "string"
  invoiceNumber: string
  invoiceDate: string
  dueDate: string
  items: InvoiceItem[]
  total: number
  currency: string
  downloadUrl: string
}

export function InvoiceEmail({ name, invoiceNumber, invoiceDate, dueDate, items, total, currency = "USD", downloadUrl }: InvoiceEmailProps) {
  const formatter = new Intl.NumberFormat("en-US", { style: "currency", currency })

  return (
    <EmailLayout preview={`Invoice ${invoiceNumber} - ${formatter.format(total / 100)}`}>
      <Heading style={styles.h1}>Invoice #{invoiceNumber}</Heading>
      <Text style={styles.text}>Hi {name},</Text>
      <Text style={styles.text}>Here's your invoice from MyApp. Thank you for your continued support.</Text>

      {/* Invoice Meta */}
      <Section style={styles.metaBox}>
        <Row>
          <Column><Text style={styles.metaLabel}>Invoice Date</Text><Text style={styles.metaValue}>{invoiceDate}</Text></Column>
          <Column><Text style={styles.metaLabel}>Due Date</Text><Text style={styles.metaValue}>{dueDate}</Text></Column>
          <Column><Text style={styles.metaLabel}>Amount Due</Text><Text style={styles.metaValueLarge}>{formatter.format(total / 100)}</Text></Column>
        </Row>
      </Section>

      {/* Line Items */}
      <Section style={styles.table}>
        <Row style={styles.tableHeader}>
          <Column><Text style={styles.tableHeaderText}>Description</Text></Column>
          <Column><Text style={{ ...styles.tableHeaderText, textAlign: "right" }}>Amount</Text></Column>
        </Row>
        {items.map((item, i) => (
          <Row key={i} style={i % 2 === 0 ? styles.tableRowEven : styles.tableRowOdd}>
            <Column><Text style={styles.tableCell}>{item.description}</Text></Column>
            <Column><Text style={{ ...styles.tableCell, textAlign: "right" }}>{formatter.format(item.amount / 100)}</Text></Column>
          </Row>
        ))}
        <Hr style={styles.divider} />
        <Row>
          <Column><Text style={styles.totalLabel}>Total</Text></Column>
          <Column><Text style={styles.totalValue}>{formatter.format(total / 100)}</Text></Column>
        </Row>
      </Section>

      <Button href={downloadUrl} style={styles.button}>Download PDF Invoice</Button>
    </EmailLayout>
  )
}

export default InvoiceEmail

const styles = {
  h1: { fontSize: "24px", fontWeight: "700", color: "#111827", margin: "0 0 16px" },
  text: { fontSize: "15px", lineHeight: "1.6", color: "#374151", margin: "0 0 12px" },
  metaBox: { backgroundColor: "#f9fafb", borderRadius: "8px", padding: "16px", margin: "16px 0" },
  metaLabel: { fontSize: "12px", color: "#6b7280", fontWeight: "600", textTransform: "uppercase" as const, margin: "0 0 4px" },
  metaValue: { fontSize: "14px", color: "#111827", margin: 0 },
  metaValueLarge: { fontSize: "20px", fontWeight: "700", color: "#4f46e5", margin: 0 },
  table: { width: "100%", margin: "16px 0" },
  tableHeader: { backgroundColor: "#f3f4f6", borderRadius: "4px" },
  tableHeaderText: { fontSize: "12px", fontWeight: "600", color: "#374151", padding: "8px 12px", textTransform: "uppercase" as const },
  tableRowEven: { backgroundColor: "#ffffff" },
  tableRowOdd: { backgroundColor: "#f9fafb" },
  tableCell: { fontSize: "14px", color: "#374151", padding: "10px 12px" },
  divider: { borderColor: "#e5e5e5", margin: "8px 0" },
  totalLabel: { fontSize: "16px", fontWeight: "700", color: "#111827", padding: "8px 12px" },
  totalValue: { fontSize: "16px", fontWeight: "700", color: "#111827", textAlign: "right" as const, padding: "8px 12px" },
  button: { backgroundColor: "#4f46e5", color: "#fff", borderRadius: "6px", padding: "12px 24px", fontSize: "15px", fontWeight: "600", textDecoration: "none" },
}
```


---

## 统一发送函数


```typescript
// emails/lib/send.ts
import { Resend } from "resend"
import { render } from "@react-email/render"
import { WelcomeEmail } from "../templates/welcome"
import { InvoiceEmail } from "../templates/invoice"
import { addTrackingParams } from "./tracking"

const resend = new Resend(process.env.RESEND_API_KEY)

type EmailPayload =
  | { type: "welcome"; props: Parameters<typeof WelcomeEmail>[0] }
  | { type: "invoice"; props: Parameters<typeof InvoiceEmail>[0] }

export async function sendEmail(to: string, payload: EmailPayload) {
  const templates = {
    welcome: { component: WelcomeEmail, subject: "Welcome to MyApp — confirm your email" },
    invoice: { component: InvoiceEmail, subject: `Invoice from MyApp` },
  }

  const template = templates[payload.type]
  const html = render(template.component(payload.props as any))
  const trackedHtml = addTrackingParams(html, { campaign: payload.type })

  const result = await resend.emails.send({
    from: "MyApp <hello@yourapp.com>",
    to,
    subject: template.subject,
    html: trackedHtml,
    tags: [{ name: "email-type", value: payload.type }],
  })

  return result
}
```


---

## 预览服务器搭建


```typescript
// package.json scripts
{
  "scripts": {
    "email:dev": "email dev --dir emails/templates --port 3001",
    "email:build": "email export --dir emails/templates --outDir emails/out"
  }
}

// Run: npm run email:dev
// Opens: http://localhost:3001
// Shows all templates with live preview and hot reload
```


---

## i18n 支持


```typescript
// emails/i18n/en.ts
export const en = {
  welcome: {
    preview: (name: string) => `Welcome to MyApp, ${name}!`,
    heading: (name: string) => `Welcome to MyApp, ${name}!`,
    body: (days: number) => `You've got ${days} days to explore everything.`,
    cta: "Confirm Email Address",
  },
}

// emails/i18n/de.ts
export const de = {
  welcome: {
    preview: (name: string) => `Willkommen bei MyApp, ${name}!`,
    heading: (name: string) => `Willkommen bei MyApp, ${name}!`,
    body: (days: number) => `Du hast ${days} Tage Zeit, alles zu erkunden.`,
    cta: "E-Mail-Adresse bestätigen",
  },
}

// Usage in template
import { en, de } from "../i18n"
const t = locale === "de" ? de : en
```


---

## 垃圾邮件评分优化清单

- [ ] 发件域名已配置 SPF、DKIM 和 DMARC 记录
- [ ] 发件地址使用自有域名（而非 gmail.com/hotmail.com）
- [ ] 主题行少于 50 个字符，不用全大写，不用 "FREE!!!"
- [ ] 文字与图片比例：文字至少占 60%
- [ ] 除 HTML 外同时提供纯文本版本
- [ ] 每封营销邮件都含退订链接（CAN-SPAM、GDPR）
- [ ] 不使用短链接：改用完整的品牌链接
- [ ] 主题中不含风险词："guarantee"、"no risk"、"limited time offer"
- [ ] 每封邮件只放一个 CTA：不要塞 5 个不同按钮
- [ ] 每张图片都有 alt 文本
- [ ] HTML 通过校验：没有损坏的标签
- [ ] 首次发送前用 Mail-Tester.com 测试（目标：9+/10）

---

## 分析追踪


```typescript
// emails/lib/tracking.ts
interface TrackingParams {
  campaign: string
  medium?: string
  source?: string
}

export function addTrackingParams(html: string, params: TrackingParams): string {
  const utmString = new URLSearchParams({
    utm_source: params.source ?? "email",
    utm_medium: params.medium ?? "transactional",
    utm_campaign: params.campaign,
  }).toString()

  // Add UTM params to all links in the email
  return html.replace(/href="(https?:\/\/[^"]+)"/g, (match, url) => {
    const separator = url.includes("?") ? "&" : "?"
    return `href="${url}${separator}${utmString}"`
  })
}
```


---

## 常见陷阱

- **必须使用内联样式**：多数邮件客户端会剥离 `<head>` 样式，React Email 会处理好这一点
- **最大宽度 600px**：超过会在 Gmail 移动端错版
- **不要用 flexbox / grid**：使用 react-email 的 `<Row>` 和 `<Column>`，而非 CSS grid
- **暗色模式的媒体查询**：必须用 `!important` 覆盖内联样式
- **缺少纯文本**：各大服务商都提供纯文本字段，务必填写
- **事务性邮件 vs 营销邮件**：使用独立的发件域名 / IP 以保护送达率
