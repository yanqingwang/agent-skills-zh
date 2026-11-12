---
name: "stripe-integration-expert"
description: "用于任何 Stripe 集成：在 Next.js、Express 或 Django 中处理订阅、试用期、按比例计费、结账、按用量计费、webhook、客户门户或开票。编写幂等的 webhook 处理程序，并调试投递失败。"
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`engineering-team/skills/stripe-integration-expert/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Stripe 集成专家

**层级：** 强大
**类别：** 工程团队
**领域：** 支付 / 计费基础设施

---

## 概述

实现生产级的 Stripe 集成：带试用期与按比例计费的订阅、一次性付款、按用量计费、结账会话、幂等的 webhook 处理程序、客户门户，以及开票。涵盖 Next.js、Express 和 Django 的实现模式。

---

## 核心能力

- 订阅生命周期管理（创建、升级、降级、取消、暂停）
- 试用期处理与转化跟踪
- 按比例计费的计算与抵扣处理
- 采用按量计价的按用量计费
- 带签名验证的幂等 webhook 处理程序
- 客户门户集成
- 发票生成与 PDF 获取
- 完整的 Stripe CLI 本地测试环境配置

---

## 适用场景

- 为任意 Web 应用加入订阅计费
- 实现带按比例计费的套餐升级/降级
- 构建按用量或按席位的计费
- 调试 webhook 投递失败
- 从一种计费模型迁移到另一种

---

## 订阅生命周期状态机


```
FREE_TRIAL ──paid──► ACTIVE ──cancel──► CANCEL_PENDING ──period_end──► CANCELED
     │                  │                                                    │
     │               downgrade                                            reactivate
     │                  ▼                                                    │
     │             DOWNGRADING ──period_end──► ACTIVE (lower plan)           │
     │                                                                        │
     └──trial_end without payment──► PAST_DUE ──payment_failed 3x──► CANCELED
                                          │
                                     payment_success
                                          │
                                          ▼
                                        ACTIVE
```


### DB 订阅状态取值：
`trialing | active | past_due | canceled | cancel_pending | paused | unpaid`

---

## Stripe 客户端配置


```typescript
// lib/stripe.ts
import Stripe from "stripe"

export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: "2024-04-10",
  typescript: true,
  appInfo: {
    name: "myapp",
    version: "1.0.0",
  },
})

// Price IDs by plan (set in env)
export const PLANS = {
  starter: {
    monthly: process.env.STRIPE_STARTER_MONTHLY_PRICE_ID!,
    yearly: process.env.STRIPE_STARTER_YEARLY_PRICE_ID!,
    features: ["5 projects", "10k events"],
  },
  pro: {
    monthly: process.env.STRIPE_PRO_MONTHLY_PRICE_ID!,
    yearly: process.env.STRIPE_PRO_YEARLY_PRICE_ID!,
    features: ["Unlimited projects", "1M events"],
  },
} as const
```


---

## 结账会话（Next.js App Router）


```typescript
// app/api/billing/checkout/route.ts
import { NextResponse } from "next/server"
import { stripe } from "@/lib/stripe"
import { getAuthUser } from "@/lib/auth"
import { db } from "@/lib/db"

export async function POST(req: Request) {
  const user = await getAuthUser()
  if (!user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 })

  const { priceId, interval = "monthly" } = await req.json()

  // Get or create Stripe customer
  let stripeCustomerId = user.stripeCustomerId
  if (!stripeCustomerId) {
    const customer = await stripe.customers.create({
      email: user.email,
      name: "username-undefined"
      metadata: { userId: user.id },
    })
    stripeCustomerId = customer.id
    await db.user.update({ where: { id: user.id }, data: { stripeCustomerId } })
  }

  const session = await stripe.checkout.sessions.create({
    customer: stripeCustomerId,
    mode: "subscription",
    payment_method_types: ["card"],
    line_items: [{ price: priceId, quantity: 1 }],
    allow_promotion_codes: true,
    subscription_data: {
      trial_period_days: user.hasHadTrial ? undefined : 14,
      metadata: { userId: user.id },
    },
    success_url: `${process.env.NEXT_PUBLIC_APP_URL}/dashboard?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${process.env.NEXT_PUBLIC_APP_URL}/pricing`,
    metadata: { userId: user.id },
  })

  return NextResponse.json({ url: session.url })
}
```


---

## 订阅升级/降级


```typescript
// lib/billing.ts
export async function changeSubscriptionPlan(
  subscriptionId: string,
  newPriceId: string,
  immediate = false
) {
  const subscription = await stripe.subscriptions.retrieve(subscriptionId)
  const currentItem = subscription.items.data[0]

  if (immediate) {
    // Upgrade: apply immediately with proration
    return stripe.subscriptions.update(subscriptionId, {
      items: [{ id: currentItem.id, price: newPriceId }],
      proration_behavior: "always_invoice",
      billing_cycle_anchor: "unchanged",
    })
  } else {
    // Downgrade: apply at period end, no proration
    return stripe.subscriptions.update(subscriptionId, {
      items: [{ id: currentItem.id, price: newPriceId }],
      proration_behavior: "none",
      billing_cycle_anchor: "unchanged",
    })
  }
}

// Preview proration before confirming upgrade
export async function previewProration(subscriptionId: string, newPriceId: string) {
  const subscription = await stripe.subscriptions.retrieve(subscriptionId)
  const prorationDate = Math.floor(Date.now() / 1000)

  const invoice = await stripe.invoices.retrieveUpcoming({
    customer: subscription.customer as string,
    subscription: subscriptionId,
    subscription_items: [{ id: subscription.items.data[0].id, price: newPriceId }],
    subscription_proration_date: prorationDate,
  })

  return {
    amountDue: invoice.amount_due,
    prorationDate,
    lineItems: invoice.lines.data,
  }
}
```


---

## 完整的 Webhook 处理程序（幂等）


```typescript
// app/api/webhooks/stripe/route.ts
import { NextResponse } from "next/server"
import { headers } from "next/headers"
import { stripe } from "@/lib/stripe"
import { db } from "@/lib/db"
import Stripe from "stripe"

// Processed events table to ensure idempotency
async function hasProcessedEvent(eventId: string): Promise<boolean> {
  const existing = await db.stripeEvent.findUnique({ where: { id: eventId } })
  return !!existing
}

async function markEventProcessed(eventId: string, type: string) {
  await db.stripeEvent.create({ data: { id: eventId, type, processedAt: new Date() } })
}

export async function POST(req: Request) {
  const body = await req.text()
  const signature = headers().get("stripe-signature")!

  let event: Stripe.Event
  try {
    event = stripe.webhooks.constructEvent(body, signature, process.env.STRIPE_WEBHOOK_SECRET!)
  } catch (err) {
    console.error("Webhook signature verification failed:", err)
    return NextResponse.json({ error: "Invalid signature" }, { status: 400 })
  }

  // Idempotency check
  if (await hasProcessedEvent(event.id)) {
    return NextResponse.json({ received: true, skipped: true })
  }

  try {
    switch (event.type) {
      case "checkout.session.completed":
        await handleCheckoutCompleted(event.data.object as Stripe.Checkout.Session)
        break

      case "customer.subscription.created":
      case "customer.subscription.updated":
        await handleSubscriptionUpdated(event.data.object as Stripe.Subscription)
        break

      case "customer.subscription.deleted":
        await handleSubscriptionDeleted(event.data.object as Stripe.Subscription)
        break

      case "invoice.payment_succeeded":
        await handleInvoicePaymentSucceeded(event.data.object as Stripe.Invoice)
        break

      case "invoice.payment_failed":
        await handleInvoicePaymentFailed(event.data.object as Stripe.Invoice)
        break

      default:
        console.log(`Unhandled event type: ${event.type}`)
    }

    await markEventProcessed(event.id, event.type)
    return NextResponse.json({ received: true })
  } catch (err) {
    console.error(`Error processing webhook ${event.type}:`, err)
    // Return 500 so Stripe retries — don't mark as processed
    return NextResponse.json({ error: "Processing failed" }, { status: 500 })
  }
}

async function handleCheckoutCompleted(session: Stripe.Checkout.Session) {
  if (session.mode !== "subscription") return

  const userId = session.metadata?.userId
  if (!userId) throw new Error("No userId in checkout session metadata")

  const subscription = await stripe.subscriptions.retrieve(session.subscription as string)

  await db.user.update({
    where: { id: userId },
    data: {
      stripeCustomerId: session.customer as string,
      stripeSubscriptionId: subscription.id,
      stripePriceId: subscription.items.data[0].price.id,
      stripeCurrentPeriodEnd: new Date(subscription.current_period_end * 1000),
      subscriptionStatus: subscription.status,
      hasHadTrial: true,
    },
  })
}

async function handleSubscriptionUpdated(subscription: Stripe.Subscription) {
  const user = await db.user.findUnique({
    where: { stripeSubscriptionId: subscription.id },
  })
  if (!user) {
    // Look up by customer ID as fallback
    const customer = await db.user.findUnique({
      where: { stripeCustomerId: subscription.customer as string },
    })
    if (!customer) throw new Error(`No user found for subscription ${subscription.id}`)
  }

  await db.user.update({
    where: { stripeSubscriptionId: subscription.id },
    data: {
      stripePriceId: subscription.items.data[0].price.id,
      stripeCurrentPeriodEnd: new Date(subscription.current_period_end * 1000),
      subscriptionStatus: subscription.status,
      cancelAtPeriodEnd: subscription.cancel_at_period_end,
    },
  })
}

async function handleSubscriptionDeleted(subscription: Stripe.Subscription) {
  await db.user.update({
    where: { stripeSubscriptionId: subscription.id },
    data: {
      stripeSubscriptionId: null,
      stripePriceId: null,
      stripeCurrentPeriodEnd: null,
      subscriptionStatus: "canceled",
    },
  })
}

async function handleInvoicePaymentFailed(invoice: Stripe.Invoice) {
  if (!invoice.subscription) return
  const attemptCount = invoice.attempt_count

  await db.user.update({
    where: { stripeSubscriptionId: invoice.subscription as string },
    data: { subscriptionStatus: "past_due" },
  })

  if (attemptCount >= 3) {
    // Send final dunning email
    await sendDunningEmail(invoice.customer_email!, "final")
  } else {
    await sendDunningEmail(invoice.customer_email!, "retry")
  }
}

async function handleInvoicePaymentSucceeded(invoice: Stripe.Invoice) {
  if (!invoice.subscription) return

  await db.user.update({
    where: { stripeSubscriptionId: invoice.subscription as string },
    data: {
      subscriptionStatus: "active",
      stripeCurrentPeriodEnd: new Date(invoice.period_end * 1000),
    },
  })
}
```


---

## 按用量计费


```typescript
// Report usage for metered subscriptions
export async function reportUsage(subscriptionItemId: string, quantity: number) {
  await stripe.subscriptionItems.createUsageRecord(subscriptionItemId, {
    quantity,
    timestamp: Math.floor(Date.now() / 1000),
    action: "increment",
  })
}

// Example: report API calls in middleware
export async function trackApiCall(userId: string) {
  const user = await db.user.findUnique({ where: { id: userId } })
  if (user?.stripeSubscriptionId) {
    const subscription = await stripe.subscriptions.retrieve(user.stripeSubscriptionId)
    const meteredItem = subscription.items.data.find(
      (item) => item.price.recurring?.usage_type === "metered"
    )
    if (meteredItem) {
      await reportUsage(meteredItem.id, 1)
    }
  }
}
```


---

## 客户门户


```typescript
// app/api/billing/portal/route.ts
import { NextResponse } from "next/server"
import { stripe } from "@/lib/stripe"
import { getAuthUser } from "@/lib/auth"

export async function POST() {
  const user = await getAuthUser()
  if (!user?.stripeCustomerId) {
    return NextResponse.json({ error: "No billing account" }, { status: 400 })
  }

  const portalSession = await stripe.billingPortal.sessions.create({
    customer: user.stripeCustomerId,
    return_url: `${process.env.NEXT_PUBLIC_APP_URL}/settings/billing`,
  })

  return NextResponse.json({ url: portalSession.url })
}
```


---

## 使用 Stripe CLI 测试


```bash
# Install Stripe CLI
brew install stripe/stripe-cli/stripe

# Login
stripe login

# Forward webhooks to local dev
stripe listen --forward-to localhost:3000/api/webhooks/stripe

# Trigger specific events for testing
stripe trigger checkout.session.completed
stripe trigger customer.subscription.updated
stripe trigger invoice.payment_failed

# Test with specific customer
stripe trigger customer.subscription.updated \
  --override subscription:customer=cus_xxx

# View recent events
stripe events list --limit 10

# Test cards
# Success: 4242 4242 4242 4242
# Requires auth: 4000 0025 0000 3155
# Decline: 4000 0000 0000 9995
# Insufficient funds: 4000 0000 0000 9995
```


---

## 功能门控辅助函数


```typescript
// lib/subscription.ts
export function isSubscriptionActive(user: { subscriptionStatus: string | null, stripeCurrentPeriodEnd: Date | null }) {
  if (!user.subscriptionStatus) return false
  if (user.subscriptionStatus === "active" || user.subscriptionStatus === "trialing") return true
  // Grace period: past_due but not yet expired
  if (user.subscriptionStatus === "past_due" && user.stripeCurrentPeriodEnd) {
    return user.stripeCurrentPeriodEnd > new Date()
  }
  return false
}

// Middleware usage
export async function requireActiveSubscription() {
  const user = await getAuthUser()
  if (!isSubscriptionActive(user)) {
    redirect("/billing?reason=subscription_required")
  }
}
```


---

## 常见陷阱

- **Webhook 投递顺序无法保证**：始终从 Stripe API 重新拉取，绝不只凭事件数据更新 DB
- **webhook 重复处理**：Stripe 遇到 500 会重试；务必使用幂等表
- **试用期转化跟踪**：在 DB 中存 `hasHadTrial: true`，防止滥用试用
- **按比例计费带来意外**：升级前先预览按比例计费结果，确认前把金额展示给用户
- **客户门户未配置**：必须在 Stripe 控制台的「账单 → 客户门户设置」中启用相应功能
- **结账缺少 metadata**：务必在 metadata 中带上 `userId`；否则无法把订阅关联到用户
