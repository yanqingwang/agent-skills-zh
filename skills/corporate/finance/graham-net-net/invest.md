---
version: alpha
name: Graham Net-Net Value
slug: graham-net-net
aliases:
  - Benjamin Graham
  - Net-Net
  - Intelligent Investor
description: 净流动资产价值、统计型深度价值、安全边际与资产负债表优先的投资
investor: Benjamin Graham
style: value+deep-value
timeHorizon: 1-3 years
decisionCadence: quarterly
assetClasses:
  - public equities
circleOfCompetence:
  - net-nets
  - working capital analysis
  - liquidation value
  - statistical cheapness
universe:
  geographies:
    - global
  instruments:
    - relevant liquid instruments in scope
  liquidity: medium-high
  dataRequirements:
    - primary financial and market data for the model
marketRegime:
  preferred: conditions where this model's edge is active
  avoid: conditions outside competence or without required data
  posture: model-specific and risk-aware
signals:
  core:
    primaryEdge:
      weight: high
      frequency: quarterly
      source: model-specific data
      description: 投资人模型的主要优势
filters:
  inUniverse: required
  evidenceSufficient: required
  riskDefined: required
  outsideCompetence: disqualifier
sizing:
  maxPosition: risk- and model-adjusted
  maxPortfolio: consistent with model concentration style
  convictionThreshold: high
  scalingRule: add only as evidence and risk/reward improve
risk:
  stopLoss: thesis- or structure-based
  maxDrawdown: model-aware
  correlationLimit: avoid hidden factor concentration
  leverage: limited or none unless model explicitly allows
  positionCutRule: exit when thesis, structure, or risk budget breaks
metrics:
  thesisHealth:
    frequency: quarterly
    alert: core evidence weakens
  riskBudget:
    frequency: quarterly
    alert: risk exceeds plan
playbooks:
  decisionMemo:
    verdictOptions: "Buy Basket / Buy Single / Watch / Asset Trap / Pass"
    requiredSections: thesis,evidence,risk,action,invalidation
sources:
  - docs/youtube-list.md
  - docs/podcast-list.md
  - docs/reading-list.md
  - Benjamin Graham, The Intelligent Investor
  - Security Analysis
  - Graham-Newman partnership history
---

> **中文汉化版** · 上游：[questflowai/investorskills](https://github.com/questflowai/investorskills) · 原文件：`skills/graham-net-net/invest.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 格雷厄姆净净资产价值

以低于资产价值的价格买入，并留出足够大的安全边际，让不完美的分析仍能保护本金。

## 投资哲学

以低于资产价值的价格买入，并留出足够大的安全边际，让不完美的分析仍能保护本金。

## 选股范围与市场环境

- **资产类别**：公开市场股票。
- **选股范围**：上列能力圈范围内的机会。
- **偏好环境**：模型优势生效的市场条件。
- **回避**：能力圈之外、数据缺失，或致命的风险结构。
- **姿态**：风险感知且由证据驱动。

## 信号

- **ncavDiscount**（高）：价格相对净流动资产价值的折价。
- **balanceSheetProtection**（高）：现金、营运资本与低负债。
- **earningsStabilitySecondary**（中）：对纯 net-net 有帮助，但并非必需。
- **diversification**（高）：以一篮子方式捕捉统计意义上的便宜货。

## 过滤条件

- **discountToNCAVOrAssets**（必需）
- **debtNotFatal**（必需）
- **fraudRiskHigh**（否决项）
- **assetsIllusory**（否决项）

## 分析

1. 计算 NCAV / 有形资产价值。
2. 对可疑资产打折，并核查负债。
3. 优先选择一篮子折价标的，而非单只"故事股"。
4. 当价格向价值收敛或资产发生减值时退出。

## 仓位管理

- **初始仓位**：先通过全部筛选条件且风险已定义，再建初始仓位。
- **加仓规则**：证据改善且风险/回报仍有吸引力时加仓。
- **最大仓位**：受模型风格与组合风险约束。
- **现金规则**：当没有机会达到标准时，持有现金或中性仓位完全成立。

## 风险管理

- **主要风险**：在优势范围之外、或没有证据支撑的情况下套用本模型。
- **止损/失效**：基于论断、结构或风险预算。
- **相关性**：避免对单一因素的隐藏集中。
- **杠杆**：除非模型明确支持，否则仅限有限使用。

## 执行

### 买入规则

1. 机会在选股范围之内。
2. 核心信号支持行动。
3. 筛选条件通过。
4. 风险与失效条件已定义。

### 卖出规则

1. 论断被打破。
2. 证据反转。
3. 风险预算被突破。
4. 模型范围内出现更好的机会。

## 监控

- **节奏**：季度。
- **指标**：核心证据、风险预算，以及相关的估值/环境/背景。
- **警报**：论断失效触发条件与关键数据缺失。

## 操作手册

### 投资备忘录

返回以下之一：Buy Basket / Buy Single / Watch / Asset Trap / Pass。内容需包含论断、证据、风险、行动计划与失效条件。

## 经典案例

- **净流动资产价值便宜货**：以低于清算式营运资本价值的价格买入。
- **分散的便宜股组合**：格雷厄姆的统计化方法降低单一个股风险。
- **安全边际原则**：把价格保护当作价值投资的第一原则。

## 该做与不该做

- 要留在模型的优势范围之内。
- 要在决定仓位之前先拿到证据。
- 要预先定义失效条件。
- 不要强行交易。
- 不要忽视风险结构。
- 不要把叙事当成证据。



## 播客

- 共享播客清单（含 Spotify 链接）：../../docs/podcast-list.md


## YouTube

- 共享 YouTube 清单：../../docs/youtube-list.md

## 阅读清单

- 《聪明的投资者》：https://www.amazon.com/Intelligent-Investor-Definitive-Investing-Essentials/dp/0060555661
- 《证券分析》：https://www.amazon.com/Security-Analysis-Sixth-Foreword-Buffett/dp/0071592539
- 《超级投资者》文章：https://www8.gsb.columbia.edu/articles/columbia-business/superinvestors
- 共享阅读清单：../../docs/reading-list.md

## 来源说明

本模型蒸馏自：

- 本杰明·格雷厄姆《聪明的投资者》（The Intelligent Investor）
- 《证券分析》（Security Analysis）
- 格雷厄姆-纽曼合伙基金历史（Graham-Newman partnership history）

尽量使用一手资料。这是一个判断框架，不构成投资建议。
