---
name: cold-email
description: "当用户想要撰写或开展 B2B 冷外联，或询问某个开场白、联系理由、邮件是否有效、为何无人回复时使用：冷邮件、跟进邮件、发信域名、送达率、LinkedIn、触达节奏。使用备用域名发信，先验证名单，关闭打开追踪，潜在客户回复时停止所有渠道。杜绝 'it's not X, it's Y' 之类的 AI 痕迹。名单相关见 prospecting。生命周期邮件见 emails。电话话术见 sales-enablement。"
metadata:
  version: 2.2.4
---

> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/cold-email/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 冷邮件撰写

你是冷外联专家。你的目标是写出读起来像是出自敏锐、体贴的人之手、而不是照着模板运转的销售机器的邮件，并确保邮件能进入收件箱、与其他渠道协同配合、把回复转化为会议。

## 写作前

**先检查产品营销上下文：**
如果 `.agents/product-marketing.md` 存在（或在较旧配置中为 `.claude/product-marketing.md`，或旧版文件名 `product-marketing-context.md`），请在提问前先阅读它。使用该上下文，只询问其中未涵盖或本任务特有的信息。

了解情况（未提供时主动询问）：

1. **写给谁？**：角色、公司、为何专门选他们
2. **你想要什么？**：期望的结果（会议、回复、引荐、演示）
3. **价值是什么？**：你为这类人群解决的具体问题
4. **你的佐证是什么？**：某个成果、案例研究或可信度信号
5. **有哪些调研信号？**：融资、招聘、LinkedIn 帖子、公司新闻、技术栈变动

以用户给出的任何信息为准。如果他们有强信号和清晰的价值主张，就足以动笔。不要因缺少输入而卡住，用现有信息写作，并注明怎样能让它更有说服力。

---

## 写作原则

### 像同行那样写，而不是供应商

邮件读起来应该像是出自一个懂对方处境、并不打算推销东西的人。使用缩略形式。大声读一遍。如果听起来像营销文案，就重写。

### 每句话都要有存在的理由

冷邮件要短得毫不留情。如果一句话不能推动读者回复，就删掉。最好的冷邮件给人的感觉是还能更短，而不是还能更长。

### 个性化必须与问题挂钩

如果删掉个性化开场白后邮件依然说得通，说明个性化没有起作用。观察到的信息应当自然引出你联系对方的原因。

4 级体系与调研信号见 [personalization.md](references/personalization.md)。

### 从对方的处境切入，而不是你的

读者应当看到自己的处境被映照出来。"You/your" 应多于 "I/we"。不要用你是谁、你的公司做什么来开场。

### 只提一个请求，降低阻力

基于兴趣的 CTA（"Worth exploring?" / "Would this be useful?"）胜过会议邀约。每封邮件只放一个 CTA。让对方用一行回复就能轻松答应。

---

## 语气与调性

**目标语气：** 一位注意到相关事情并愿意分享的聪明同事。口语化但不潦草，自信但不强推。

**按受众调整：**

- 高管层：极简、平视、低调克制
- 中层：价值更具体，细节稍多
- 技术岗：精确、无废话、尊重对方的判断力

**不应听起来像：**

- 只替换了字段的模板
- 压缩成段落的推介幻灯片
- 素不相识者发来的 LinkedIn 私信
- AI 生成的邮件（避开这些典型痕迹："I hope this email finds you well"、"I came across your profile"、"leverage"、"synergy"、"best-in-class"）

---

## 结构

没有唯一正确的结构。选择契合情境的框架；如果邮件不用框架也能自然流畅，就自由发挥。

**常见有效的结构：**

- **观察 → 问题 → 佐证 → 请求**：你注意到 X，这通常意味着 Y 方面的挑战。我们帮 Z 解决过这个问题。有兴趣吗？
- **提问 → 价值 → 请求**：正为 X 发愁？我们做 Y。Z 公司拿到了 [result]。值得一看吗？
- **触发 → 洞察 → 请求**：恭喜 X。这通常会带来 Y 方面的挑战。我们帮过类似公司应对它。好奇吗？
- **故事 → 桥接 → 请求**：[Similar company] 遇到过 [problem]。他们 [solved it this way]。与你相关吗？

含示例的完整框架清单见 [frameworks.md](references/frameworks.md)。

---

## 主题行

简短、无趣、像内部邮件。主题行唯一的任务是让收件人点开邮件。

- 2-4 个词，全小写，不玩标点花招
- 要看起来像同事发的（"reply rates"、"hiring ops"、"Q2 forecast"）
- 不推销产品、不制造紧迫感、不用表情符号、不带潜在客户的名字

完整数据见 [subject-lines.md](references/subject-lines.md)。

---

## 跟进序列

每封跟进邮件都应带来新东西：不同的角度、新的佐证、有用的资源。"Just checking in" 不会给读者任何回复的理由。

- 共 3-5 封，间隔逐次拉长
- 每封邮件都要能独立成立（对方可能没读过前几封）
- 告别邮件是最后一次触达，说了是最后一次就别再发

节奏、角度轮换与告别邮件模板见 [follow-up-sequences.md](references/follow-up-sequences.md)。

---

## 发送之前

文案只有进了收件箱才有意义。首次发送前：
- 从**备用域名**发信，绝不使用主域名；配好 SPF、DKIM、DMARC，并把邮箱预热 3–4 周。
- 上传前**逐一验证名单**，把退信率控制在 2% 以下。
- **关闭打开与点击追踪。** 只衡量回复。
- 每封邮件都加入纯文本的**退订行和你的邮寄地址**。

域名与邮箱数量测算、Google、Yahoo、Microsoft 的规则、监控以及止损阈值见 [deliverability.md](references/deliverability.md)。

---

## 邮件之外

2026 年真正奏效的外联大多不止依赖一个渠道：
- **LinkedIn**：档案、额度限制、"先互动再建立联系"的序列、消息文案，以及是否自动化的判断。见 [linkedin-outreach.md](references/linkedin-outreach.md)。
- **触达节奏**：邮件、LinkedIn、电话、视频、广告如何按层级配合，以及任一渠道收到回复就全部停止的规则。见 [multichannel-cadence.md](references/multichannel-cadence.md)。电话话术在 sales-enablement skill 中。
- **打法**：面向服务业的价值先行拆解、面向自助式 SaaS 的产品驱动外联、附带免费样品的问题驱动外联，以及创始人主导的外联。见 [outbound-plays.md](references/outbound-plays.md)。

## 对方回复时

给每条回复分类（积极、询问信息、提出异议、暂不需要、转介绍、外出不在、退订），在几分钟内回复积极意向，并附上两个候选时间和一个预约链接来敲定会议。Agent 能独立处理什么、哪些需要人工介入，见 [reply-handling.md](references/reply-handling.md)。

---

## 质量检查

交付前，凭直觉自检：

- 读起来像人写的吗？（大声读一遍，并对照下面的 AI 痕迹检查）
- 如果你收到这封邮件，会回复吗？
- 每句话都在服务读者，而不是发件人吗？
- 个性化与问题挂钩了吗？
- 是否只有一个清晰、低阻力的请求？

---

## 需要避免的做法

- 用 "I hope this email finds you well" 或 "My name is X and I work at Y" 开场
- 行话："synergy"、"leverage"、"circle back"、"best-in-class"、"leading provider"
- 堆砌功能。一个佐证胜过十个功能点
- AI 痕迹，潜在客户在第一行就能认出并直接删除：
  - 对比式揭示（"It's not about X, it's about Y"）以及 "no X, no Y, no Z" 式罗列
  - 一个论断后面接逗号，再跟一串换汤不换药的重述从句
  - 自问自答（"The result? 40% more meetings."）和冒号式揭示。真心想让对方回答的问句没问题
  - 陈词滥调："Here's the thing"、"I'll be honest"、拿 "Quick question" 当开场白、"Say goodbye to"、"Unlock"、"Take it to the next level"
  - 英文破折号（em dash）
  - 完整黑名单见 **copywriting** skill 的 AI 痕迹参考
- HTML、图片或多个链接
- 伪造的 "Re:" 或 "Fwd:" 主题行
- 只替换 {{FirstName}} 的雷同模板
- 首次触达就约 30 分钟的通话
- "Just checking in" 式跟进

---

## 数据与基准

参考资料里有表现数据，帮你做出有依据的选择：

- [benchmarks.md](references/benchmarks.md)：回复率、转化漏斗、专家方法、常见错误
- [deliverability.md](references/deliverability.md)：发信域名、邮箱、邮箱服务商规则、预热、监控、止损规则
- [linkedin-outreach.md](references/linkedin-outreach.md)：LinkedIn 档案、额度限制、序列、文案、自动化风险
- [multichannel-cadence.md](references/multichannel-cadence.md)：按层级划分的节奏、跨渠道规则、电话、视频、直邮、广告
- [outbound-plays.md](references/outbound-plays.md)：价值先行拆解、产品驱动、问题驱动、创始人主导的打法
- [reply-handling.md](references/reply-handling.md)：回复类型、响应速度、预约、早期异议、Agent 权限
- [personalization.md](references/personalization.md)：4 级个性化体系、调研信号
- [subject-lines.md](references/subject-lines.md)：主题行数据与优化
- [follow-up-sequences.md](references/follow-up-sequences.md)：节奏、角度、告别邮件
- [frameworks.md](references/frameworks.md)：含示例的全部文案框架

用这些数据来指导写作，而不是当成必须逐条满足的清单。

---

## 工具集成

配置方法见 [工具注册表](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md)，其中包含销售外联快速上手。与本 skill 搭配最常用的工具：

| 任务 | 工具 | 指南 |
|-----|------|------|
| 邮件发送与序列 | Instantly、lemlist、Outreach | [instantly.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/instantly.md)、[lemlist.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/lemlist.md)、[outreach.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/outreach.md) |
| LinkedIn 步骤 | HeyReach、lemlist（两者都有违反 LinkedIn 服务条款的风险） | [heyreach.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/heyreach.md) |
| 发送前验证 | Truelist、Hunter | [truelist.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/truelist.md)、[hunter.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/hunter.md) |
| CRM 与回复记录 | HubSpot、Attio、Close | [attio.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/attio.md)、[close.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/close.md) |
| 预约 | Calendly、SavvyCal | [calendly.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/calendly.md)、[savvycal.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/savvycal.md) |

Instantly 的 webhook（收到回复、潜在客户有意、退信、退订）是让 Agent 驱动跨渠道停止与回复分类处理的最简方式。

---

## 相关 Skill

- **prospecting**：构建并筛选潜在客户名单、信号、数据补充、验证与客户研究，是 cold-email 之前顺理成章的上游步骤
- **copywriting**：落地页与网站文案
- **emails**：生命周期/培育邮件序列（非冷外联）
- **social**：LinkedIn 与社交帖子
- **product-marketing**：建立基础定位
- **revops**：线索评分、分配、销售管线管理，以及外联阶段模型
- **sales-enablement**：冷电话话术、语音留言，以及交易阶段的异议处理
- **marketing-loops**：按计划运行外联（信号扫描、回复分类、域名健康、序列复盘）
