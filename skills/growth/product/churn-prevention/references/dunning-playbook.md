> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/churn-prevention/references/dunning-playbook.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 催款手册（Dunning Playbook）

回收失败扣款、降低被动流失（involuntary churn）的完整指南。

---

## 催款为什么重要

- 失败扣款造成全部订阅流失的 30-50%
- 大部分失败扣款用对策略都能挽回
- 订阅制企业每年因被动流失损失估计 1290 亿美元
- 有效的催款能挽回 50-60% 的失败扣款

---

## 催款时间线

```
Day -30 to -7: Pre-dunning (prevent failures)
Day 0:         Payment fails → Smart retry #1 + Email #1
Day 1-3:       Smart retry #2 + Email #2
Day 3-5:       Smart retry #3
Day 5-7:       Smart retry #4 + Email #3
Day 7-10:      Final retry + Email #4 (final warning)
Day 10-14:     Grace period ends → Account paused/cancelled
Day 14+:       Win-back sequence begins
```

---

## 催款前预防：把失败挡在发生之前

### 卡片到期管理

| 时机 | 动作 |
|--------|--------|
| 到期前 30 天 | 邮件："尾号 4242 的卡下个月到期" |
| 到期前 15 天 | 邮件："更新支付方式，避免服务中断" |
| 到期前 7 天 | 邮件："你的卡 7 天后到期：现在就更新" |
| 到期前 3 天 | 应用内横幅："支付方式即将到期" |

**邮件模板（卡片即将到期）：**
```
Subject: Your card ending in 4242 expires soon

Hi [Name],

The card on file for your [Product] subscription expires on [date].

Update your payment method now to avoid any interruption:

[Update Payment Method →]

This takes less than 30 seconds.

— [Product] Team
```

### 卡片自动更新服务

主要卡组织都提供卡片自动更新计划：

| 服务 | 卡组织 | 作用 |
|---------|---------|--------------|
| Visa Account Updater (VAU) | Visa | 自动更新存储的卡号和有效期 |
| Mastercard Automatic Billing Updater (ABU) | Mastercard | Mastercard 同理 |
| Amex Cardrefresher | American Express | Amex 同理 |

**效果：**把因卡片过期/换卡导致的硬拒付减少 30-50%。

**如何开启：**
- **Stripe**：自动，默认开启
- **Chargebee**：通过网关设置开启
- **Recurly**：内置，默认开启
- **Braintree**：联系收单方开启

### 备用支付方式

引导用户添加第二种支付方式：
- 注册时："添加备用支付方式"（转化率低）
- 首次扣款成功后："用备用卡保护你的账户"（时机更好）
- 失败扣款被挽回后："添加备用方式，防止再次中断"（时机最佳：他们刚痛过一次）

### 扣款前通知

对年费套餐或高价值订阅：
- 续费前 7 天发邮件，写明金额和日期
- 附上更新支付方式的链接
- 展示续费包含的内容
- 部分法规对自动续费有此要求

---

## 智能重试策略

### 拒付类型分类

| 代码 | 类型 | 含义 | 是否重试？ |
|------|------|---------|--------|
| `insufficient_funds` | 软 | 余额暂时不足 | 是：2-3 天后重试 |
| `card_declined`（泛指） | 软 | 各种临时原因 | 是：重试 3-4 次 |
| `processing_error` | 软 | 网关/网络问题 | 是：24 小时内重试 |
| `expired_card` | 硬 | 卡已过期 | 否：请用户换新卡 |
| `stolen_card` | 硬 | 卡被挂失 | 否：请用户换新卡 |
| `do_not_honor` | 软/硬 | 银行拒绝（原因不明） | 再试一次，然后请用户换卡 |
| `authentication_required` | 验证 | 需要 SCA/3DS | 引导客户完成验证 |

### 各服务商的重试安排

**Stripe（智能重试，推荐）：**
- 在 Stripe Dashboard → Billing → Settings 里开启 "Smart Retries"
- Stripe 的机器学习模型基于数十亿笔交易选择最优重试时机
- 通常在 3-4 周内重试 4-8 次
- 比固定节奏重试多挽回约 15%

**手动重试节奏（没有智能重试时）：**

| 次数 | 时机 | 最佳日期/时间 |
|-------|--------|--------------|
| 1 | 第 1 天（失败后 24 小时） | 早上，与原扣款同一星期几 |
| 2 | 第 3 天 | 换一天中的不同时段 |
| 3 | 第 5 天 | 常见发薪日之后（1 号、15 号） |
| 4 | 第 7 天 | 下一工作日的早上 |
| 5（最后一次） | 第 10 天 | 宽限期结束前的最后一次尝试 |

**重试时机要点：**
- 在原扣款成功的同一个月同一天重试
- 在常见发薪日（每月 1 号和 15 号）之后重试
- 避免周末重试（通过率更低）
- 早间重试（当地时间 8-10 点）效果略好

---

## 催款邮件序列

### Email 1：扣款失败（第 0 天）

**语气：**友好、就事论事。不制造恐慌。

```
Subject: Action needed — your payment didn't go through

Hi [Name],

We tried to charge your [card type] ending in [last 4] for your
[Product] subscription ($[amount]), but it didn't go through.

This happens sometimes — usually a quick card update fixes it.

[Update Payment Method →]

Your access isn't affected yet. We'll retry automatically, but
updating your card is the fastest fix.

Need help? Just reply to this email.

— [Product] Team
```

### Email 2：提醒（第 3 天）

**语气：**帮忙口吻，紧迫感略强。

```
Subject: Quick reminder — update your payment for [Product]

Hi [Name],

Just a heads-up — we still haven't been able to process your
$[amount] payment for [Product].

[Update Payment Method →]

Takes less than 30 seconds. Your [data/projects/team access]
is safe, but we'll need a valid payment method to keep your
account active.

Questions? Reply here and we'll help.

— [Product] Team
```

### Email 3：紧迫（第 7 天）

**语气：**直接，后果说清。

```
Subject: Your [Product] account will be paused in 3 days

Hi [Name],

We've tried to process your payment several times, but your
[card type] ending in [last 4] keeps getting declined.

If we don't receive payment by [date], your account will be
paused and you'll lose access to:

• [Key feature/data they use]
• [Their projects/workspace]
• [Team access for X members]

[Update Payment Method Now →]

Your data won't be deleted — you can reactivate anytime by
updating your payment method.

— [Product] Team
```

### Email 4：最后警告（第 10 天）

**语气：**收尾，清楚，不带指责。

```
Subject: Last chance to keep your [Product] account active

Hi [Name],

This is our last reminder. Your payment of $[amount] is past
due, and your account will be paused tomorrow ([date]).

[Update Payment Method →]

After pausing:
• Your data is saved for [90 days]
• You can reactivate anytime
• Just update your card to restore access

If you intended to cancel, no action needed — your account
will be paused automatically.

— [Product] Team
```

---

## 宽限期管理

### 宽限期内会发生什么

| 设置项 | 建议 |
|---------|---------------|
| 时长 | 最后一次重试后 7-14 天 |
| 访问权限 | 降级（只读）或完整访问 |
| 界面呈现 | 应用内横幅："扣款已逾期，更新后继续使用" |
| 重试 | 宽限期内继续后台重试 |
| 沟通 | 催款邮件继续发 |

### 访问降级选项

**方案 A：宽限期内完整访问（B2B 推荐）**
- 摩擦更小，客户感到被尊重
- 挽回率更高（客户还能看到价值）
- 风险：部分客户会钻宽限期的空子

**方案 B：只读访问（B2C 推荐）**
- 能看，不能建/改
- 制造紧迫感，又没有丢数据的恐慌
- 信息明确："更新支付方式即可恢复完整访问"

**方案 C：立即锁定（不推荐）**
- 太激进，伤关系
- 挽回率更低
- 只适合极低价套餐

### 宽限期结束后

| 时机 | 动作 |
|--------|--------|
| 宽限期结束 | 暂停账户（不是删除） |
| 暂停后第 1 天 | "你的账户已暂停"邮件 |
| 暂停后第 7 天 | "你的数据还在"提醒 |
| 暂停后第 30 天 | 带新优惠的召回尝试 |
| 暂停后第 60 天 | 最后一次召回 |
| 暂停后第 90 天 | 数据删除警告（如适用） |

---

## 各服务商的配置

### Stripe

**开启智能重试：**
1. Dashboard → Settings → Billing → Subscriptions and emails
2. 在重试规则下开启 "Smart Retries"
3. 在 Dashboard → Settings → Emails 里配置扣款失败邮件

**自定义重试规则（不用智能重试时）：**
```
Retry 1: 3 days after failure
Retry 2: 5 days after failure
Retry 3: 7 days after failure
Final:   Mark subscription as unpaid after last retry
```

**需要处理的 webhook 事件：**
- `invoice.payment_failed`：触发催款
- `invoice.paid`：停止催款，恢复访问
- `customer.subscription.updated`：状态变更
- `customer.subscription.deleted`：最终取消

### Chargebee

**内置催款：**
1. Settings → Configure Chargebee → Retry Settings
2. 配置重试次数和间隔
3. Settings → Configure Chargebee → Email Notifications → Dunning

**催款选项：**
- 自动重试，节奏可配置
- 内置催款邮件（模板可自定义）
- 按套餐配置宽限期

### Paddle

**托管催款：**
- Paddle 自动处理重试和催款
- 自定义空间有限（客户关系由 Paddle 管理）
- **Paddle Billing webhook**（点分式 `event_type` 命名）：
  - `transaction.payment_failed` 表示一次扣款失败。用其中的 `subscription_id` 关联订阅续费；一次性交易的失败不属于订阅流失。
  - `subscription.past_due` 表示订阅已逾期。
  - `subscription.canceled` 表示订阅已实际取消。安排在下一账期生效的取消会先发出 `subscription.updated`；在该变更生效之前，按订阅当前状态保留访问权限。
- 配置通知订阅时使用这些精确名称。`subscription.payment_failed` 和 `subscription.cancelled` 不是 Paddle Billing 的事件类型；不要把 Billing webhook 与 Paddle Classic 那套独立的告警名称混用。
- 在为账户状态变更接线之前，先核对 [payment-failure](https://developer.paddle.com/webhooks/transactions/transaction-payment-failed/) 与 [cancellation](https://developer.paddle.com/webhooks/subscriptions/subscription-canceled/) 的契约。
- 适合想完全甩手的团队

### Recurly

**收入挽回（Revenue Recovery）：**
1. Configuration → Dunning Management
2. 按套餐设置重试节奏
3. 配置宽限期和最终动作（暂停 vs. 取消）

**进阶功能：**
- 机器学习重试优化
- 按套餐的催款计划
- 内置 Account Updater

---

## 应用内催款

别只靠邮件。在应用内直接呈现扣款失败：

### 横幅模式
```
┌──────────────────────────────────────────────────────┐
│ ⚠ Your payment of $29 failed. Update your card to    │
│ avoid losing access. [Update Payment →]  [Dismiss]   │
└──────────────────────────────────────────────────────┘
```

**规则：**
- 催款期间每次页面加载都显示
- 允许关闭（但下次会话再显示）
- 直达更新支付方式入口（点击次数越少越好）
- 别挡着产品：让他们继续用

### 模态框模式（最后警告用）
```
┌─────────────────────────────────────┐
│                                     │
│  Your account will be paused        │
│  on [date]                          │
│                                     │
│  Update your payment method to      │
│  keep access to your [X] projects   │
│  and [Y] team members.              │
│                                     │
│  [Update Payment Method]            │
│  [Remind Me Later]                  │
│                                     │
└─────────────────────────────────────┘
```

---

## 度量催款效果

### 关键指标

| 指标 | 计算方式 | 目标 |
|--------|-----------------|--------|
| 挽回率 | 挽回的扣款 / 全部失败 | 50-60% |
| 按拒付类型的挽回率 | 各类型的挽回 / 失败 | 软拒付 70%+，硬拒付 40%+ |
| 挽回耗时 | 从失败到扣款成功的天数 | <5 天 |
| 催款前预防率 | 被预防的失败 / 预期失败 | 20-30% |
| 催款邮件打开率 | 打开 / 发送（每封） | 60%+ |
| 催款邮件点击率 | 点击 / 打开（每封） | 30%+ |
| 挽回收入（月度） | 挽回金额合计 | 追踪趋势 |
| 被动流失损失收入 | 失败且未挽回的金额合计 | 追踪趋势 |

### 基准对比

**按公司阶段：**

| 阶段 | 典型被动流失 | 优化后目标 |
|-------|--------------------------|--------------------------|
| 早期（< $1M ARR） | MRR 的 3-5%/月 | 1-2% |
| 成长期（$1-10M ARR） | MRR 的 2-4%/月 | 0.5-1.5% |
| 规模期（$10M+ ARR） | MRR 的 1-3%/月 | 0.3-0.8% |

### ROI 测算

```
Assumed failed invoice amount:       $10,000/month
Baseline collected amount:           30% ($3,000/month)
Scenario collected amount:           60% ($6,000/month)
Additional recovered cash:           $3,000/month
If repeated for 12 months:           $36,000/year
Assumed incremental tooling cost:    $200-500/month
Recovered-revenue / tooling ratio:   6-15x
After tooling alone / tooling cost:  5-14x (500-1,400%)
```

6–15x 是回收现金 ÷ 工具成本。扣除工具成本后是 5–14x（`(3,000 - 500) / 500 = 5`；`(3,000 - 200) / 200 = 14`），这是未计人力和支付手续费之前的数字。请用你自己的基线来验证 60% 的回收率目标。参见[毛利与净利](https://stripe.com/resources/more/gross-vs-net-profit-what-businesses-need-to-know)。
