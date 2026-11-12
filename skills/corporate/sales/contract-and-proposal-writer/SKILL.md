---
name: "contract-and-proposal-writer"
description: "在起草适用于 US、EU、UK 或 DACH 司法辖区的自由职业合同、提案、SOW、NDA 或 MSA 时使用。输出结构化 Markdown，并附 docx 转换步骤；不构成法律意见。"
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`business-growth/skills/contract-and-proposal-writer/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 合同与提案撰写

**层级：** POWERFUL  
**类别：** Business Growth  
**领域：** Legal Documents, Business Development, Client Relations

---

## 概述

生成专业、契合司法辖区的商务文档：自由职业合同、项目提案、SOWs、NDAs 和 MSAs。输出结构化 Markdown，并附 docx 转换说明。覆盖 US（Delaware）、EU（GDPR）、UK 以及 DACH（德国法）等司法辖区。

**不能替代法律顾问。** 把这些模板当作扎实的起点；对高价值或复杂的委托，请交由律师审阅。

---

## 核心能力

- 自由职业开发合同（fixed-price & hourly）
- 含时间线/预算拆分的项目提案
- 带交付物矩阵的工作说明书（SOW）
- NDA（mutual & one-way）
- 主服务协议（MSA）
- 针对特定司法辖区的条款（US/EU/UK/DACH）
- GDPR 数据处理附录（EU/DACH）

---

## 关键条款参考

| 条款 | 选项 |
|--------|---------|
| 付款条款 | Net-30, milestone-based, monthly retainer |
| IP 归属 | Work-for-hire (US), assignment (EU/UK), license-back |
| 责任上限 | 1x contract value (standard), 3x (high-risk) |
| 终止 | For cause (14-day cure), convenience (30/60/90-day notice) |
| 保密 | 2-5 year term, perpetual for trade secrets |
| 保证 | "As-is" disclaimer, limited 30/90-day fix warranty |
| 争议解决 | Arbitration (AAA/ICC), courts (jurisdiction-specific) |

---

## 适用场景

- 启动新的客户合作，需要快速拿到合同
- 客户索要含报价与时间线的提案
- 合作或供应商关系需要 MSA
- 用 NDA 保护 IP 或机密信息
- EU/DACH 项目需要符合 GDPR 的数据条款

---

## 工作流程

### 1. 收集需求

向用户确认：

    1. 文档类型？（contract / proposal / SOW / NDA / MSA）
    2. 司法辖区？（US-Delaware / EU / UK / DACH）
    3. 合作方式？（fixed-price / hourly / retainer）
    4. 各方主体？（names, roles, business addresses）
    5. 范围摘要？（1-3 sentences）
    6. 总金额或小时费率？
    7. 开始日期 / 结束日期或时长？
    8. 特殊要求？（IP assignment, white-label, subcontractors）

### 2. 选择模板

| 类型 | 司法辖区 | 模板 |
|------|-------------|----------|
| 固定价开发合同 | Any | Template A |
| 咨询 retainer | Any | Template B |
| SaaS 合作 | Any | Template C |
| NDA mutual | US/EU/UK/DACH | NDA-M |
| NDA one-way | US/EU/UK/DACH | NDA-OW |
| SOW | Any | SOW base |

### 3. 生成并填写

填写所有 [BRACKETED] 占位符。把缺失的数据标记为 "REQUIRED"。

### 4. 转换为 DOCX


```bash
# Install pandoc
brew install pandoc        # macOS
apt install pandoc         # Ubuntu

# Basic conversion
pandoc contract.md -o contract.docx \
  --reference-doc=reference.docx \
  -V geometry:margin=1in

# With numbered sections (legal style)
pandoc contract.md -o contract.docx \
  --number-sections \
  -V documentclass=article \
  -V fontsize=11pt

# With custom company template
pandoc contract.md -o contract.docx \
  --reference-doc=company-template.docx
```


---

## 司法辖区说明

### US (Delaware)
- 管辖法律：State of Delaware
- 适用 Work-for-hire 原则（Copyright Act 101）
- 仲裁：AAA Commercial Rules
- 竞业限制：在合理的范围/期限内可执行

### EU (GDPR)
- 处理个人数据时必须包含 Data Processing Addendum
- 部分成员国要求 IP 转让另立书面契据
- 仲裁：ICC 或当地商会

### UK (post-Brexit)
- 适用英国法
- IP：Patents Act 1977 / CDPA 1988
- 仲裁：LCIA Rules
- 数据：UK GDPR（脱欧后对应法规）

### DACH（德国 / 奥地利 / 瑞士）
- BGB（Buergerliches Gesetzbuch）管辖合同
- 某些条款要求书面形式（para 126 BGB）
- IP：作者始终保留精神权利，必须明确转让 Nutzungsrechte
- 竞业限制：最长 2 years，须给予补偿（para 74 HGB）
- 管辖：德国法院（Landgericht）或 DIS 仲裁
- 处理个人数据强制适用 DSGVO（GDPR 实施法）
- Kuendigungsfristen：适用法定通知期

---

## Template A: Web 开发固定价合同


```markdown
# SOFTWARE DEVELOPMENT AGREEMENT

**Effective Date:** [DATE]
**Client:** [CLIENT LEGAL NAME], [ADDRESS] ("Client")
**Developer:** [YOUR LEGAL NAME / COMPANY], [ADDRESS] ("Developer")

---

## 1. SERVICES

Developer agrees to design, develop, and deliver:

**Project:** [PROJECT NAME]
**Description:** [1-3 sentence scope]

**Deliverables:**
- [Deliverable 1] due [DATE]
- [Deliverable 2] due [DATE]
- [Deliverable 3] due [DATE]

## 2. PAYMENT

**Total Fee:** [CURRENCY] [AMOUNT]

| Milestone | Amount | Due |
|-----------|--------|-----|
| Contract signing | 50% | Upon execution |
| Beta delivery | 25% | [DATE] |
| Final acceptance | 25% | Within 5 days of acceptance |

Late payments accrue interest at 1.5% per month.
Client has [10] business days to accept or reject deliverables in writing.

## 3. INTELLECTUAL PROPERTY

Upon receipt of full payment, Developer assigns all right, title, and interest in the
Work Product to Client as a work made for hire (US) / by assignment of future copyright (EU/UK).

Developer retains the right to display Work Product in portfolio unless Client
requests confidentiality in writing within [30] days of delivery.

Pre-existing IP (tools, libraries, frameworks) remains Developer's property.
Developer grants Client a perpetual, royalty-free license to use pre-existing IP
as embedded in the Work Product.

## 4. CONFIDENTIALITY

Each party keeps confidential all non-public information received from the other.
This obligation survives termination for [3] years.

## 5. WARRANTIES

Developer warrants Work Product will substantially conform to specifications for
[90] days post-delivery. Developer will fix material defects at no charge during
this period. EXCEPT AS STATED, WORK PRODUCT IS PROVIDED "AS IS."

## 6. LIABILITY

Developer's total liability shall not exceed total fees paid under this Agreement.
Neither party liable for indirect, incidental, or consequential damages.

## 7. TERMINATION

For Cause: Either party may terminate if the other materially breaches and fails
to cure within [14] days of written notice.

For Convenience: Client may terminate with [30] days written notice and pay for
all work completed plus [10%] of remaining contract value.

## 8. DISPUTE RESOLUTION

US: Binding arbitration under AAA Commercial Rules, [CITY], Delaware law.
EU/DACH: ICC / DIS arbitration, [CITY]. German / English law.
UK: LCIA Rules, London. English law.

## 9. GENERAL

- Entire Agreement: Supersedes all prior discussions.
- Amendments: Must be in writing, signed by both parties.
- Independent Contractor: Developer is not an employee of Client.

---

CLIENT: _________________________ Date: _________
[CLIENT NAME], [TITLE]

DEVELOPER: _________________________ Date: _________
[YOUR NAME], [TITLE]
```


---

## Template B: 月度咨询 Retainer


```markdown
# CONSULTING RETAINER AGREEMENT

**Effective Date:** [DATE]
**Client:** [CLIENT LEGAL NAME] ("Client")
**Consultant:** [YOUR NAME / COMPANY] ("Consultant")

---

## 1. SERVICES

Consultant provides [DOMAIN, e.g., "CTO advisory and technical architecture"] services.

**Monthly Hours:** Up to [X] hours/month
**Rollover:** Unused hours [do / do not] roll over (max [X] hours banked)
**Overflow Rate:** [CURRENCY] [RATE]/hr for hours exceeding retainer

## 2. FEES

**Monthly Retainer:** [CURRENCY] [AMOUNT], due on the 1st of each month.
**Payment Method:** Bank transfer / Stripe / SEPA direct debit
**Late Payment:** 2% monthly interest after [10]-day grace period.

## 3. TERM AND TERMINATION

**Initial Term:** [3] months starting [DATE]
**Renewal:** Auto-renews monthly unless either party gives [30] days written notice.
**Immediate termination:** For material breach uncured after [7] days notice.

On termination, Consultant delivers all work in progress within [5] business days.

## 4. INTELLECTUAL PROPERTY

Work product created under this Agreement belongs to [Client / Consultant / jointly].
Advisory output (recommendations, analyses) are Client property upon full payment.

## 5. EXCLUSIVITY

[OPTION A - Non-exclusive:]
This Agreement is non-exclusive. Consultant may work with other clients.

[OPTION B - Partial exclusivity:]
Consultant will not work with direct competitors of Client during the term
and [90] days thereafter.

## 6. CONFIDENTIALITY AND DATA PROTECTION

EU/DACH: If Consultant processes personal data on behalf of Client, the parties
shall execute a Data Processing Agreement (DPA) per Art. 28 GDPR.

## 7. LIABILITY

Consultant's aggregate liability is capped at [3x] the fees paid in the [3] months
preceding the claim.

---

Signatures as above.
```


---

## Template C: SaaS 合作协议


```markdown
# SAAS PARTNERSHIP AGREEMENT

**Effective Date:** [DATE]
**Provider:** [NAME], [ADDRESS]
**Partner:** [NAME], [ADDRESS]

---

## 1. PURPOSE

Provider grants Partner [reseller / referral / white-label / integration] rights to
Provider's [PRODUCT NAME] ("Software") subject to this Agreement.

## 2. PARTNERSHIP TYPE

[ ] Referral: Partner refers customers; earns [X%] of first-year ARR per referral.
[ ] Reseller: Partner resells licenses; earns [X%] discount off list price.
[ ] White-label: Partner rebrands Software; pays [AMOUNT]/month platform fee.
[ ] Integration: Partner integrates Software via API; terms in Exhibit A.

## 3. REVENUE SHARE

| Tier | Monthly ARR Referred | Commission |
|------|---------------------|------------|
| Bronze | < $10,000 | [X]% |
| Silver | $10,000-$50,000 | [X]% |
| Gold | > $50,000 | [X]% |

Payout: Net-30 after month close, minimum $[500] threshold.

## 4. INTELLECTUAL PROPERTY

Each party retains all IP in its own products. No implied licenses.
Partner may use Provider's marks per Provider's Brand Guidelines (Exhibit B).

## 5. DATA AND PRIVACY

Each party is an independent data controller for its own customers.
Joint processing requires a separate DPA (Exhibit C - EU/DACH projects).

## 6. TERM

Initial: [12] months. Renews annually unless [90]-day written notice given.
Termination for Cause: [30]-day cure period for material breach.

## 7. LIMITATION OF LIABILITY

Each party's liability capped at [1x] fees paid/received in prior [12] months.
Mutual indemnification for IP infringement claims from own products.

---

Signatures, exhibits, and governing law per applicable jurisdiction.
```


---

## GDPR 数据处理附录 (EU/DACH 条款块)


```markdown
## DATA PROCESSING ADDENDUM (Art. 28 GDPR)

Controller: [CLIENT NAME]
Processor: [CONTRACTOR NAME]

### Subject Matter
Processor processes personal data on behalf of Controller solely to perform services
under the main Agreement.

### Categories of Data Subjects
[e.g., end users, employees, customers]

### Categories of Personal Data
[e.g., names, email addresses, usage data]

### Processing Duration
For the term of the main Agreement; deletion within [30] days of termination.

### Processor Obligations
- Process data only on Controller's documented instructions
- Ensure persons authorized to process have committed to confidentiality
- Implement technical and organizational measures per Art. 32 GDPR
- Assist Controller with data subject rights requests
- Not engage sub-processors without prior written consent
- Delete or return all personal data upon termination

### Sub-processors (current as of Effective Date)
| Sub-processor | Location | Purpose |
|--------------|----------|---------|
| [AWS / GCP / Azure] | [Region] | Cloud hosting |
| [Other] | [Location] | [Purpose] |

### Cross-border Transfers
Data transfers outside EEA covered by: [ ] SCCs  [ ] Adequacy Decision  [ ] BCRs
```


---

## 常见陷阱

1. **缺少 IP 转让条款** - 在 EU 仅写 "work for hire" 不够；在 DACH 需明确转让 Nutzungsrechte
2. **验收标准含糊** - 务必定义 "accepted" 的含义（书面签收、X days to reject）
3. **没有变更流程** - 范围蔓延会拖垮固定价项目；为超出范围的工作加上条款
4. **司法辖区错配** - 纯德国项目却选 Delaware 法律，会带来执行难题
5. **缺少责任限制** - 没有上限，一个 bug 就可能意味着无限赔偿
6. **口头修改** - 口头变更的合同难以执行；一律要求书面修订

---

## 最佳实践

- 对 >$10K 的项目，优先用 **milestone payments** 而非 net-30 - 降低现金流风险
- 针对 EU/DACH：务必确认是否需要 DPA（涉及任何个人数据 = 是）
- 针对 DACH：明确写入 **Schriftformklausel**（书面形式条款）
- 凡是超过 3 months 的项目，都要加上 **force majeure** 条款
- 对 retainer：定义响应时间 SLAs（例如 4h 紧急 / 24h 常规）
- 把模板纳入版本控制，用 `git diff` 跟踪改动
- 每年复审一次 - 法律会变，尤其是 GDPR 的执法解释
- 对 NDA：务必写明终止时机密材料的返还/销毁
