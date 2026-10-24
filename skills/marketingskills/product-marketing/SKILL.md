---
name: product-marketing
description: "当用户想要创建或更新其产品营销上下文文档时使用。当用户提到 'product context'、'marketing context'、'set up context'、'positioning'、'who is my target audience'、'describe my product'、'ICP'、'ideal customer profile'、'brand voice'、'tone of voice'、'brand guidelines'、'what have we learned'、'log this learning'，或希望避免在多个营销任务中重复陈述基础信息时，也应使用。在任何新项目开始时、使用其他营销 Skill 之前先使用本 Skill——它会创建 `.agents/product-marketing.md`，所有其他 Skill 都引用它来获取产品、受众与 positioning 上下文。"
metadata:
  version: 2.2.0
---

> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/product-marketing/SKILL.md` · License: MIT
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 产品营销上下文（Product Marketing Context）

你帮助用户创建并维护一份产品营销上下文文档。它记录基础性的 positioning（定位）与 messaging（信息传达）信息，供其他营销 Skill 引用，让用户不必重复自述。

该文档保存在 `.agents/product-marketing.md`。

## 工作流程

### 第 1 步：检查已有上下文

首先，检查 `.agents/product-marketing.md` 是否已存在。同时检查 `.claude/product-marketing.md` 以及旧文件名 `product-marketing-context.md`（位于 `.agents/` 或 `.claude/` 中）等旧版布置——如果在 `.agents/product-marketing.md` 以外的任何位置找到，主动提议将其移动到规范位置。

**如果已存在：**
- 读取它并概述其中已记录的内容——注明当前的 **Document version** 和最近几条 **Changelog** 条目，让用户看清文档现状与近期变更
- 询问用户想更新哪些章节
- 只为这些章节收集信息
- 每次实质性保存时，提升版本号并添加一条 changelog 条目（见第 4 步）。这份文档是其他所有营销 Skill 都要读取的共享上下文，因此值得保留一份带日期的 *改了什么、为什么改* 的书面记录。

**如果不存在，提供两个选项：**

1. **从代码库自动起草**（推荐）：你将研究这个仓库——README、落地页、营销文案、package.json 等——并起草上下文文档的 V1 版。随后由用户审阅、纠错并填补空白。这比从零开始更快。

2. **从零开始**：以对话方式逐节走查，每次收集一个章节的信息。

大多数用户偏好选项 1。展示草稿后，询问："有什么需要修正的？还缺什么？"

### 第 2 步：收集信息

**如果是自动起草：**
1. 阅读代码库：README、落地页、营销文案、关于页、meta description（元描述）、package.json、任何现有文档
2. 根据所见内容起草所有章节
3. 展示草稿，询问有什么需要修正或缺失
4. 迭代直到用户满意

**如果是从零开始：**
以下方章节为序，以对话方式逐节走查，一次一节。不要一次抛出所有问题。

对每个章节：
1. 简要说明你要记录什么
2. 提出相关问题
3. 确认准确性
4. 进入下一节

坚持获取客户的原话——确切措辞比润色过的描述更有价值，因为它们反映客户真实的思考与表达方式，能让文案更有共鸣。

---

## 需要记录的章节

### 1. 产品概述
- 一句话描述
- 它做什么（2-3 句）
- 产品品类（你摆在哪个"货架"上——客户如何搜索到你）
- 产品类型（SaaS、marketplace、电商、服务等）
- 商业模式与定价

### 2. 目标受众
- 目标公司类型（行业、规模、阶段）
- 目标决策者（角色、部门）
- 主要使用场景（你解决的核心问题）
- Jobs to be done（客户"雇用"你完成的 2-3 件事）
- 具体使用场景或情景

### 3. Personas（用户画像，仅限 B2B）
如果购买决策涉及多个利益相关者，为每个人记录：
- User（使用者）、Champion（倡导者）、Decision Maker（决策者）、Financial Buyer（财务买单人）、Technical Influencer（技术影响者）
- 每个人关心什么、面临什么挑战，以及你向其承诺的价值

### 4. 问题与痛点
- 客户在找到你之前面临的核心挑战
- 现有解决方案为何不够好
- 这让他们付出什么代价（时间、金钱、机会）
- 情绪张力（压力、恐惧、疑虑）

### 5. 竞争格局
- **直接竞争者**：相同的解决方案，相同的问题（例如 Calendly vs SavvyCal）
- **次级竞争者**：不同的解决方案，相同的问题（例如 Calendly vs Superhuman 的日程功能）
- **间接竞争者**：相冲突的方式（例如 Calendly vs 私人助理）
- 它们各自对客户而言为何不够好

### 6. 差异化
- 关键差异化优势（竞品欠缺的能力）
- 你如何以不同方式解决它
- 为什么这样更好（收益）
- 客户为何在众多选项中选择你

### 7. 异议与反向画像
- 销售中最常听到的 3 大异议及应对方式
- 谁并不是合适的客户（anti-persona，反向画像）

### 8. 切换动态
JTBD 四力（Four Forces）：
- **Push（推力）**：哪些不满驱使他们离开现有解决方案
- **Pull（拉力）**：什么吸引他们走向你
- **Habit（习惯）**：什么让他们固守现有做法
- **Anxiety（焦虑）**：什么让他们对切换感到担忧

### 9. 客户语言
- 客户如何描述问题（原话）
- 他们如何描述你的解决方案（原话）
- 应使用的词/短语
- 应避免的词/短语
- 产品专属术语表

### 10. Brand Voice（品牌语调）
- 3-5 个 voice 属性，每个属性注明：它意味着什么、不意味着什么，以及一句取自现有文案的真实例句
- 分场景的 tone（语气）：voice 在支持、发布、报错、销售、社交媒体等场景中如何变化
- 品牌用词：你独占的术语，以及绝不使用的词（附原因）

请基于已被验证有效的文案和创始人本人的文字来构建，而不是靠会议上挑选的形容词。提取步骤、一份完整的示例画像、修改前后对比示例，以及按人划分的 voice 指南，见 [references/brand-voice.md](references/brand-voice.md)。

### 11. Proof Points（证明点）
- 可引用的关键指标或成果
- 知名客户/Logo
- 用户见证（testimonial）摘录
- 主要价值主题及支撑证据

### 12. 目标
- 首要业务目标
- 关键转化动作（你希望人们做什么）
- 当前指标（如果已知）

### 13. 付费广告（可选，仅当其投放广告时）
**ads** Skill 会读取这一节，这样用户就不必每次会话都重新解释广告账户情况。
- 利润现实：维持业务盈利的目标 CPA（单次获客成本）或 ROAS（广告支出回报率），以及硬性底线（ROAS 低于该值、或 CPA 高于该值时须立即预警）
- 预算与节奏：月度预算与可接受的每日波动
- 转化的真实口径：哪些转化动作算数、各值多少，已知追踪缺陷（滞后、重复计数、线下缺口），以及优质线索与单纯填表单的分界
- 广告系列命名规范及每个广告系列的用途，各一行
- Agent 可以做什么（读取、对比、标记、起草、建议），以及未经批准不得做什么（更改预算或出价、暂停或开启、修改追踪、发布广告）

### 14. Learnings（经验记录）
此节初始为空。随着工作不断发布上线，它会逐步充实（见下方"维护 Learnings"）。

---

## 第 3 步：创建文档

收集完信息后，用以下结构创建 `.agents/product-marketing.md`：

```markdown
# Product Marketing Context

**Document version:** v1
**Last updated:** [date]

## Product Overview
**One-liner:**
**What it does:**
**Product category:**
**Product type:**
**Business model:**

## Target Audience
**Target companies:**
**Decision-makers:**
**Primary use case:**
**Jobs to be done:**
-
**Use cases:**
-

## Personas
| Persona | Cares about | Challenge | Value we promise |
|---------|-------------|-----------|------------------|
| | | | |

## Problems & Pain Points
**Core problem:**
**Why alternatives fall short:**
-
**What it costs them:**
**Emotional tension:**

## Competitive Landscape
**Direct:** [Competitor] — falls short because...
**Secondary:** [Approach] — falls short because...
**Indirect:** [Alternative] — falls short because...

## Differentiation
**Key differentiators:**
-
**How we do it differently:**
**Why that's better:**
**Why customers choose us:**

## Objections
| Objection | Response |
|-----------|----------|
| | |

**Anti-persona:**

## Switching Dynamics
**Push:**
**Pull:**
**Habit:**
**Anxiety:**

## Customer Language
**How they describe the problem:**
- "[verbatim]"
**How they describe us:**
- "[verbatim]"
**Words to use:**
**Words to avoid:**
**Glossary:**
| Term | Meaning |
|------|---------|
| | |

## Brand Voice
| Attribute | Means | Doesn't mean | Example line |
|-----------|-------|--------------|--------------|
| | | | |

**Tone by context:**
- Support:
- Launch:
- Errors:
- Sales:
- Social:
**Terms we own:**
**Never use (and why):**

## Proof Points
**Metrics:**
**Customers:**
**Testimonials:**
> "[quote]" — [who]
**Value themes:**
| Theme | Proof |
|-------|-------|
| | |

## Goals
**Business goal:**
**Conversion action:**
**Current metrics:**

## Paid Ads (optional)
**Target CPA / ROAS:**
**Hard floor:**
**Monthly budget and daily variance:**
**Conversions that count:**
| Action | Means | Value | Feeds bidding? |
|--------|-------|-------|----------------|
| | | | |
**Known tracking weaknesses:**
**Good lead vs. form fill:**
**Campaigns:** [name] — [what it's for]
**Agent may:** read, compare, flag, draft, recommend
**Agent may not (without approval):** change budgets or bids, pause or launch, edit tracking, publish ads

## Learnings
*Decisions and tested lessons. Newest first. Keep it to about 20 active entries.*
| Date | Learning | Evidence | Applies to | Status |
|------|----------|----------|------------|--------|
| | | | | |

## Changelog
*Newest first. One line per revision: what changed and why.*
- v1 ([date]) — Initial context.
```

---

## 第 4 步：确认、定版与保存

- 展示完成的文档
- 询问是否有需要调整之处
- **设定版本号与 changelog**——这是给所有其他 Skill 都会读取的文档留下的书面轨迹：
  - **新文档：** 设定 `Document version: v1` 和一条 Changelog 条目——`- v1 ([today]) — Initial context.`
  - **更新已有文档：** 递增版本号（v2 → v3 ……），把 `Last updated` 更新为今天，并在列表顶部**前置新增一条 Changelog 条目**（最新在前），用一行概括 *改了什么、为什么改*。绝不改写或重排过去的条目。
  - 一条好的条目会写明涉及的章节与原因，而不是笼统一句"更新了文档"。示例：
    - `- v3 (2026-07-16) — Repositioned from "email tool" to "deliverability platform"; added RevOps to the ICP.`
    - `- v2 (2026-06-02) — Rewrote value prop and objections after 5 customer interviews; added competitor Acme.`
  - 条目和 `Last updated` 中的日期使用 ISO 形式（YYYY-MM-DD）的今天。
  - **纯错别字修正：** 不提升版本号、不加 changelog 条目——直接保存修正即可。除此之外的任何变更都要提升版本号并获得一条条目。当这次变更是真正的重新定位时，请明说——下游 Skill 此后将基于新上下文来生成内容。
- 保存到 `.agents/product-marketing.md`
- 并告知用户："其他营销 Skill 现在会自动使用这份上下文。底部的 Changelog 记录每一次修订——查看它，就能看到你的 positioning 是如何演进的。随时运行 `/product-marketing` 来更新它。"

---

## 维护 Learnings

Changelog 记录文档如何变化。**Learnings** 记录团队在发布上线过程中发现了什么：哪些角度奏效，哪些 offer（优惠主张）失败，做了哪些决策、为什么。起草类 Skill（copywriting、emails、ads、ad-creative、social）在动笔前会读取它，让下一份 brief（创作简报）从已知信息出发。

**条目格式：** 每条经验一行。
- **Learning（经验）：** 一句话，具体到足以改动草稿。"定价锚定型标题在定价页上胜过结果型标题"是合格的；"写得更清楚些"则不合格。
- **Evidence（证据）：** 所依据的测试、广告活动或来源，附数字与样本量。"变体 B 试用注册 +18%，每组 2,400 位访客，历时 3 周。"
- **Applies to（适用于）：** 它影响的渠道、细分人群或 Skill。
- **Status（状态）：** `active`、`watch`（仅一个数据点，值得复测）或 `retired`。

**什么值得记录：**
- 达到计划样本量的测试结果，或在两个及以上广告活动中重复出现的同一模式
- 用户做出的、附带理由的决策（positioning、定价、砍掉某个渠道），未来草稿必须遵守
- 用户不止一次给出的纠正（"别把它称作平台"）

**什么不值得记录：** 仅跑过一次的轶事（这类记为 `watch` 或干脆不记）、任务备注，以及属于其他章节的内容。新异议进 Objections；新的客户用语进 Customer Language。

**何时将条目退役：** 后续测试与它矛盾、产品或市场在其之下已发生变化（新定价、新 ICP），或它已连续两个季度不再相关。把状态改为 `retired` 并加一行说明原因，而不是直接删除，这样没人会重测已有定论的问题。把已退役的行移到底部，当表格的活跃条目超过约 20 行时将其归档。

**谁来写入：** 任何完成测试、广告活动或复盘的 Skill 都可以提议一行。把拟议的行展示给用户，获批准后添加，并像其他实质性变更一样提升版本号、加一条 Changelog。按时间表定期运行的 loop 通过其会话结束步骤完成此事（见 **marketing-loops**）。

---

## 技巧

- **要具体**：问"是什么头号挫败感让他们找到你？"而不是"他们在解决什么问题？"
- **记录原话**：客户语言胜过润色过的描述
- **索要示例**："能举个例子吗？"能引出更好的回答
- **边走边验证**：每完成一节就概述并确认，然后再继续
- **跳过不适用的**：并非每个产品都需要全部章节（例如 B2C 场景下的 Personas，以及不投广告时的 Paid Ads）
