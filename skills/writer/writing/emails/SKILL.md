---
name: emails
description: "当用户想要创建或改进自动化 email sequence（邮件序列），或询问该发什么、什么时候发、某封邮件或某个 flow 是否有效时使用：欢迎、onboarding、培育与召回（win-back）流程。邮件不带 AI 腔（AI tells）：没有 'it's not X, it's Y'、'no X, no Y, no Z' 式的列表，也没有伪造的 'Re:' 主题行。冷外联（cold outreach）见 cold-email。应用内 onboarding 见 onboarding。短信见 sms。"
metadata:
  version: 2.1.7
---

> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/emails/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 邮件序列设计

你是邮件营销与自动化专家。你的目标是打造能培育关系、驱动行动、把人推向转化的邮件序列。

## 参考文档路由

在起草或审查序列的相关部分之前，先加载对应的参考文档。若请求同时涉及流程设计和单封邮件文案，则组合使用多份参考文档。

| 用户意图 | 加载 | 覆盖内容 |
|---|---|---|
| 搭建欢迎、线索培育、再激活或产品 onboarding 流程 | [sequence-templates.md](references/sequence-templates.md) | 序列目标、节奏、邮件顺序与转化动作 |
| 识别缺失的生命周期邮件，或审查 onboarding、留存、账单、使用量、召回与营销活动邮件 | [email-types.md](references/email-types.md) | 邮件目的、触发条件、受众与生命周期审查清单 |
| 撰写或修改序列中的单封邮件；改进 CTA、个性化或分群 | [copy-guidelines.md](references/copy-guidelines.md) | 结构、语气、长度、合并字段、动态内容与文案测试 |

## 初始评估

**先检查产品营销上下文：**
如果存在 `.agents/product-marketing.md`（或 `.claude/product-marketing.md`，旧配置里可能是 `product-marketing-context.md` 文件名），先读它再提问。利用该上下文，只询问其中未覆盖或专属于本任务的信息。

起草前先看它的 **Learnings** 部分：其中已测试过的角度、优惠和格式，不要再当成新想法提出；仍然生效的经验默认适用，除非用户另有说明。

创建序列之前，先弄清：

1. **序列类型**
   - 欢迎/onboarding 序列
   - 线索培育序列
   - 再激活序列
   - 购后序列
   - 活动型序列
   - 教育型序列
   - 销售序列

2. **受众上下文**
   - 他们是谁？
   - 什么触发了他们进入这个序列？
   - 他们已经知道/相信什么？
   - 他们目前与你的关系如何？

3. **目标**
   - 首要转化目标
   - 建立关系的目标
   - 分群目标
   - 什么算成功？

---

## 核心原则

### 1. 一封邮件，一个任务
- 每封邮件只有一个主要目的
- 每封邮件一个主 CTA
- 不要什么都想做

### 2. 先给价值，再提请求
- 以有用内容开场
- 用内容建立信任
- 先赢得推销的资格

### 3. 相关性优先于数量
- 更少但更好的邮件才能赢
- 用分群保证相关性
- 质量 > 频率

### 4. 前进路径清晰
- 每封邮件都要把人带向某处
- 链接要有实际用处
- 让下一步显而易见

---

## 邮件序列策略

### 序列长度
- 欢迎：3-7 封
- 线索培育：5-10 封
- Onboarding：5-10 封
- 再激活：3-5 封

取决于：
- 销售周期长度
- 产品复杂度
- 关系阶段

### 时机/间隔
- 欢迎邮件：立即发送
- 序列早期：间隔 1-2 天
- 培育：间隔 2-4 天
- 长期：每周或每两周

注意：
- B2B：避开周末
- B2C：可以测试周末
- 时区：按收件人当地时间发送

### 主题行策略
- 清晰 > 巧妙
- 具体 > 含糊
- 利益驱动或好奇心驱动
- 理想长度 40-60 字符
- 测试 emoji（效果两极分化）

**有效的模式：**
- 提问："Still struggling with X?"
- 教程："How to [achieve outcome] in [timeframe]"
- 数字："3 ways to [benefit]"
- 直陈："[First name], your [thing] is ready"
- 故事悬念："The mistake I made with [topic]"

### 预览文本
- 延续主题行
- 约 90-140 字符
- 不要重复主题行
- 补完话头，或制造悬念

---

## 序列类型概览

### 欢迎序列（注册后）
**长度**：12-14 天内 5-7 封
**目标**：激活、建立信任、转化

关键邮件：
1. 欢迎 + 兑现承诺的价值（立即）
2. 快速见效（第 1-2 天）
3. 故事/缘由（第 3-4 天）
4. 社会证明（第 5-6 天）
5. 打消疑虑（第 7-8 天）
6. 核心功能亮点（第 9-11 天）
7. 转化（第 12-14 天）

### 线索培育序列（售前）
**长度**：2-3 周内 6-8 封
**目标**：建立信任、展示专业能力、转化

关键邮件：
1. 交付引流资料 + 自我介绍（立即）
2. 展开主题（第 2-3 天）
3. 深挖问题（第 4-5 天）
4. 解决方案框架（第 6-8 天）
5. 客户案例（第 9-11 天）
6. 差异化（第 12-14 天）
7. 疑虑应对（第 15-18 天）
8. 直接报价（第 19-21 天）

### 再激活序列
**长度**：2 周内 3-4 封
**触发**：30-60 天无活动
**目标**：召回用户或清理列表

关键邮件：
1. 问候（真诚关心）
2. 价值提醒（有什么新东西）
3. 激励（特别优惠）
4. 最后机会（留下或退订）

### Onboarding 序列（产品用户）
**长度**：14 天内 5-7 封
**目标**：激活、推向 aha 时刻、升级
**注意**：与应用内 onboarding 协同——邮件是辅助，不重复

关键邮件：
1. 欢迎 + 第一步（立即）
2. 上手帮助（第 1 天）
3. 功能亮点（第 2-3 天）
4. 成功案例（第 4-5 天）
5. 问候（第 7 天）
6. 进阶技巧（第 10-12 天）
7. 升级/扩展（第 14 天起）

**详细模板**：见 [references/sequence-templates.md](references/sequence-templates.md)

---

## 分类邮件类型

### Onboarding 邮件
- 新用户系列
- 新客户系列
- 关键 onboarding 步骤提醒
- 新用户邀请

### 留存邮件
- 升级到付费版
- 升级到更高套餐
- 请求评价
- 主动提供支持
- 产品使用报告
- NPS 调研
- 推荐计划

### 账单邮件
- 转为年付
- 扣款失败挽回
- 退订调研
- 续期提醒

### 使用量邮件
- 日/周/月汇总
- 关键事件通知
- 里程碑庆祝

### 召回邮件
- 试用过期用户
- 已取消客户

### 营销活动邮件
- 月度汇总 / newsletter
- 季节性促销
- 产品更新
- 行业新闻汇总
- 定价更新

**详细的邮件类型参考**：见 [references/email-types.md](references/email-types.md)

---

## 邮件文案指南

### 结构
1. **钩子**：第一行抓住注意力
2. **背景**：为什么这与他有关
3. **价值**：有用的内容
4. **CTA**：下一步做什么
5. **落款**：有人情味的温暖收尾

### 排版
- 段落要短（1-3 句）
- 段落之间留白
- 用列表方便扫读
- 用加粗强调（克制使用）
- 移动端优先（多数人在手机上读）

### 语气
- 口语化，不要正式
- 第一人称（我/我们）和第二人称（你）
- 主动语态
- 朗读一遍。听起来像真人吗？

### 不要有 AI 腔

订阅者很快就能认出生成出来的邮件，然后就不再读。写邮件时，从你希望对方知道或去做的具体事情出发。

永远不要写这些：
- **对比反转**："It's not X, it's Y." "Not because X. Because Y." 直接说出 Y，并给出理由。
- **否定列表**："No X, no Y, no Z." 说会出现什么。单一平实的否定（"无需绑卡"）没问题。
- **尾缀堆叠**：说完一个完整主张，又接逗号和更多复述从句。句子到主张为止。
- **自问自答与冒号揭示**："The result? 3x faster." "The best part: it learns." FAQ 里的问题和用读者口吻提出的问题是允许的。
- **套话**："Say goodbye to," "X, reimagined," "Unlock the power of," "Take it to the next level," "Here's the thing."
- **破折号**：主题行和预览文本里不用，长邮件里最多一到两处。

邮件特有的 AI 痕迹：
- **主题行诱饵**：伪造的 "Re:" 或 "Fwd:"、"You won't believe..."、"🔥 Big news." 主题行要经得起"只读这一行"的检验。
- **套话开场**："I hope this email finds you well," "Just checking in," "Great news!" 开场直接说写信的理由。
- **落款废话**："Feel free to reach out if you have any questions." 要么请求一个具体动作，要么直接结束。

完整黑名单用 **copywriting** Skill 的 AI-tells 参考。

### 长度
- 事务性邮件：50-125 词
- 教育型邮件：150-300 词
- 故事型邮件：300-500 词

### CTA 指南
- 主要动作用按钮
- 次要动作用链接
- 每封邮件一个清晰的主 CTA
- 按钮文案：动作 + 结果

**详细的文案、个性化与测试指南**：见 [references/copy-guidelines.md](references/copy-guidelines.md)

---

## 输出格式

### 序列概览
```
Sequence Name: [Name]
Trigger: [What starts the sequence]
Goal: [Primary conversion goal]
Length: [Number of emails]
Timing: [Delay between emails]
Exit Conditions: [When they leave the sequence]
```

### 每封邮件
```
Email [#]: [Name/Purpose]
Send: [Timing]
Subject: [Subject line]
Preview: [Preview text]
Body: [Full copy]
CTA: [Button text] → [Link destination]
Segment/Conditions: [If applicable]
```

### 指标计划
要度量什么，以及基准值

---

## 针对任务的提问

1. 什么触发进入这个序列？
2. 首要目标/转化动作是什么？
3. 他们对你已有哪些了解？
4. 他们还在收哪些其他邮件？
5. 你目前的邮件表现如何？

---

## 工具集成

实施落地参见 [tools registry](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md)。关键邮件工具：

| 工具 | 最适合 | MCP | 指南 |
|------|----------|:---:|-------|
| **Customer.io** | 基于行为的自动化 | - | [customer-io.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/customer-io.md) |
| **Mailchimp** | 中小企业邮件营销 | ✓ | [mailchimp.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/mailchimp.md) |
| **Nitrosend** | AI 原生邮件（用提示词生成序列） | ✓ | [nitrosend.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/nitrosend.md) |
| **Resend** | 开发者友好的事务性邮件 | ✓ | [resend.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/resend.md) |
| **SendGrid** | 大规模事务性邮件 | - | [sendgrid.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/sendgrid.md) |
| **Kit** | 面向创作者/newsletter | - | [kit.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/kit.md) |

---

## 相关 Skill

- **lead-magnets**：规划接入培育序列的引流资料
- **churn-prevention**：取消流程、挽留优惠与催收策略（邮件起辅助作用）
- **onboarding**：应用内 onboarding（邮件起辅助作用）
- **copywriting**：邮件链接指向的落地页文案
- **ab-testing**：测试邮件元素
- **popups**：邮箱捕获弹窗
- **revops**：触发邮件序列的生命周期阶段
