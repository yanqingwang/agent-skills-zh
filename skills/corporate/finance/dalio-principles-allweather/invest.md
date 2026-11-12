---
version: alpha
name: Dalio Principles All-Weather
slug: dalio-principles-allweather
aliases:
  - Ray Dalio
  - All Weather
  - Economic Machine
  - Risk Parity
description: 经济机器、债务周期、风险平价、分散化与全天候组合构建
investor: Ray Dalio
style: macro+multi-asset+risk-parity
timeHorizon: years
decisionCadence: monthly
assetClasses:
  - public equities
  - bonds
  - commodities
  - gold
  - cash
  - multi-asset
circleOfCompetence:
  - economic machine
  - debt cycles
  - inflation regimes
  - risk parity
  - diversified beta
universe:
  geographies:
    - global
  instruments:
    - 范围内相关的流动性工具
  liquidity: medium-high
  dataRequirements:
    - 模型所需的一手财务与市场数据
marketRegime:
  preferred: 本模型优势生效的市场条件
  avoid: 能力圈之外或缺乏所需数据的条件
  posture: 因模型而异且注重风险
signals:
  core:
    primaryEdge:
      weight: high
      frequency: monthly
      source: 模型专属数据
      description: 投资者模型的核心优势
filters:
  inUniverse: required
  evidenceSufficient: required
  riskDefined: required
  outsideCompetence: disqualifier
sizing:
  maxPosition: 按风险与模型调整
  maxPortfolio: 与模型集中度风格一致
  convictionThreshold: high
  scalingRule: 仅随证据与风险/回报的改善而加仓
risk:
  stopLoss: 基于论点或结构
  maxDrawdown: 结合模型设定
  correlationLimit: 避免隐性因子集中
  leverage: 除非模型明确允许，否则限制或不使用
  positionCutRule: 论点、结构或风险预算被打破时离场
metrics:
  thesisHealth:
    frequency: monthly
    alert: 核心证据走弱
  riskBudget:
    frequency: monthly
    alert: 风险超出计划
playbooks:
  decisionMemo:
    verdictOptions: "Overweight / Underweight / Hedge / Neutral / Rebalance"
    requiredSections: thesis,evidence,risk,action,invalidation
sources:
  - docs/youtube-list.md
  - docs/podcast-list.md
  - docs/reading-list.md
  - Ray Dalio, Principles
  - Bridgewater All Weather materials
  - How the Economic Machine Works
---

> **中文汉化版** · 上游：[questflowai/investorskills](https://github.com/questflowai/investorskills) · 原文件：`skills/dalio-principles-allweather/invest.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 达利欧全天候

不要把整个组合押在单一的宏观预测上。要让在不同增长与通胀状态下表现良好的资产相互平衡，控制各资产的风险贡献，并尊重债务周期的动态。

## 投资哲学

不要把整个组合押在单一的宏观预测上。要让在不同增长与通胀状态下表现良好的资产相互平衡，控制各资产的风险贡献，并尊重债务周期的动态。

## 标的池与市场状态

- **资产类别**：公开市场股票、债券、大宗商品、黄金、现金、多资产。
- **标的池**：上文所列能力圈之内的机会。
- **偏好状态**：模型优势生效的市场条件。
- **回避**：能力圈之外、数据缺失，或存在致命风险结构的情况。
- **姿态**：注重风险，以证据为驱动。

## 信号

- **growthRegime** (high)：增长正在上升还是下降？
- **inflationRegime** (high)：通胀正在上升还是下降？
- **debtCycleStage** (high)：短期与长期债务周期所处位置。
- **riskContribution** (high)：在各分散资产之间均衡的是风险，而不是资金。

## 筛选

- **regimeMapped** (required)
- **riskContributionDefined** (required)
- **singleAssetBet** (disqualifier)
- **noDiversifiers** (disqualifier)

## 分析

1. 标定当前的增长与通胀状态。
2. 识别债务周期阶段与政策约束。
3. 按风险贡献在股票、债券、大宗商品、黄金、现金之间配置。
4. 当状态或风险贡献漂移时进行再平衡。

## 仓位管理

- **初始仓位**：只有在筛选通过且风险已界定之后才建立。
- **加仓规则**：证据改善且风险/回报仍具吸引力时加仓。
- **最大仓位**：受模型风格与组合风险约束。
- **现金规则**：当没有机会达到标准时，持有现金或保持中性是有效选择。

## 风险管理

- **主要风险**：在模型优势之外或缺乏证据的情况下套用模型。
- **止损/失效**：基于论点、结构或风险预算。
- **相关性**：避免隐性集中于单一因子。
- **杠杆**：除非模型明确支持，否则限制使用。

## 执行

### 入场规则

1. 标的属于标的池内的机会。
2. 核心信号支持行动。
3. 筛选通过。
4. 风险与失效条件已界定。

### 离场规则

1. 论点被打破。
2. 证据反转。
3. 风险预算被突破。
4. 模型框架内出现更好的机会。

## 监控

- **频率**：每月。
- **指标**：核心证据、风险预算，以及相关的估值/状态/背景。
- **告警**：触发失效条件、关键数据缺失。

## 操作手册

### 决策备忘录

返回以下结论之一：Overweight / Underweight / Hedge / Neutral / Rebalance。需包含论点、证据、风险、行动计划与失效条件。

## 经典案例

- **全天候基金设计**：在增长/通胀状态之间分散，而不是预测单一结果。
- **2008 与危机分散的教训**：高度集中的股票 beta 在债务周期断裂时会失效。
- **经济机器框架**：把生产率、短期债务周期、长期债务周期作为组合背景。

## 应做与不应做

- 应坚守在模型优势范围之内。
- 应在确定仓位之前要求证据。
- 应界定失效条件。
- 不应强行交易。
- 不应忽视风险结构。
- 不应把叙事当作证明。



## 播客

- Odd Lots: https://open.spotify.com/search/Odd%20Lots%20Bloomberg/shows
- Macro Voices: https://open.spotify.com/search/Macro%20Voices/shows
- 共享播客列表：../../docs/podcast-list.md


## YouTube

- How the Economic Machine Works: https://www.youtube.com/watch?v=PHe0bXAIuk0
- 共享 YouTube 列表：../../docs/youtube-list.md

## 阅读清单

- Economic Principles: https://www.economicprinciples.org/
- Changing World Order: https://www.amazon.com/Changing-World-Order-Nations-Succeed/dp/1982160276
- 共享阅读清单：../../docs/reading-list.md

## 来源说明

本模型蒸馏自：

- Ray Dalio，《Principles》
- Bridgewater 全天候（All Weather）材料
- 《How the Economic Machine Works》

尽量使用一手来源。本文件是一个判断框架，不构成投资建议。
