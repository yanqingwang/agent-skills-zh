---
version: alpha
name: Buffett Value Compounder
slug: buffett
aliases:
  - Buffett Value Investing
  - Quality Compounder
description: 持久经营的生意所有权、所有者盈余、护城河、管理层质量与安全边际
investor: Warren Buffett
style: value+quality
timeHorizon: 5-10 years
decisionCadence: quarterly
assetClasses:
  - public equities
circleOfCompetence:
  - consumer brands
  - insurance
  - financial services
  - utilities
  - railroads
  - capital-light compounders
universe:
  geographies:
    - United States
    - developed markets
  instruments:
    - stocks
  marketCap: mid-cap to large-cap
  liquidity: medium-high
  dataRequirements:
    - 10-K
    - 10-Q
    - annual letters
    - proxy statements
marketRegime:
  preferred: any, if price is below conservative value
  avoid: speculative mania where quality is priced for perfection
  posture: patient
signals:
  fundamental:
    ownerEarnings:
      weight: high
      direction: higher-is-better
      frequency: quarterly
      source: cash flow statement
      description: 扣除维持性资本需求后，真正归属所有者的现金。
    roic:
      weight: high
      direction: higher-is-better
      threshold: "> 15% preferred"
      frequency: annual
      source: financial statements
      description: 高资本回报率体现生意质量。
    moatDurability:
      weight: high
      frequency: annual
      source: business analysis
      description: 竞争优势应当能延续多年。
    managementIntegrity:
      weight: high
      frequency: annual
      source: letters, proxy, capital allocation history
      description: 诚实而理性的管理者守护所有者价值。
  valuation:
    marginOfSafety:
      weight: high
      direction: higher-is-better
      threshold: "> 30% discount to conservative value preferred"
      frequency: event-driven
      source: valuation model
      description: 价格必须能抵御分析失误。
filters:
  understandable: required
  durableMoat: required
  consistentOwnerEarnings: required
  managementIntegrity: required
  marginOfSafety: required
  heavyLeverage: disqualifier
sizing:
  maxPosition: "25%"
  maxPortfolio: 10-15 core positions
  convictionThreshold: high
  scalingRule: start partial, add when thesis strengthens and price remains attractive
  cashReserve: opportunistic
risk:
  marginOfSafety: "30% preferred"
  stopLoss: thesis-based
  maxDrawdown: price drawdown tolerated if thesis intact
  leverage: none
  positionCutRule: sell when thesis breaks or valuation becomes extreme
metrics:
  ownerEarnings:
    frequency: quarterly
    alert: cash conversion deteriorates
  roic:
    frequency: annual
    alert: sustained decline below quality threshold
  debt:
    frequency: quarterly
    alert: leverage threatens durability
playbooks:
  investmentMemo:
    verdictOptions: Buy / Watchlist / Pass / Too Hard
    requiredSections: business,moat,management,valuation,marginOfSafety,risk,invalidation
sources:
  - docs/youtube-list.md
  - docs/podcast-list.md
  - docs/reading-list.md
  - Warren Buffett shareholder letters
  - Berkshire Hathaway annual meeting transcripts
  - Benjamin Graham, The Intelligent Investor
---

> **中文汉化版** · 上游：[questflowai/investorskills](https://github.com/questflowai/investorskills) · 原文件：`skills/buffett/invest.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 巴菲特式价值复利

股票是一门生意的部分所有权。目标是：以低于保守内在价值的价格，买入由诚实的管理者经营、可理解且持久的生意。

## 投资哲学

正确的问题是：以这个价格把整门生意买下来，我们是否安心？在恐惧、无聊、复杂或短期失望之中，市场常常给优质生意定错价。

耐心本身就是优势的一部分。如果没有生意达到标准，就持有现金等待。

## 选股范围与市场环境

- **资产类别**：公开市场股票。
- **选股范围**：具备足够经营历史与原始申报文件的可理解公司。
- **偏好环境**：只要价值有吸引力，任何市场环境皆可。最好的机会常常出现在恐惧之中。
- **回避**：脆弱的杠杆、不透明的会计、大宗商品投机、炒作风潮。
- **姿态**：耐心且集中。

## 信号

### 基本面

- **所有者盈余**（高，季度）：按真实现金创造与维持性资本开支调整后的净利润。
- **ROIC**（高，年度）：持续的高回报体现生意质量与再投资潜力。
- **护城河持久性**（高，年度）：品牌、转换成本、网络效应、成本优势、监管或分销渠道。
- **管理层诚信**（高，年度）：理性的资本配置与诚实的沟通。

### 估值

- **安全边际**（高，事件驱动）：只有当保守估值以有意义的幅度高于价格时，才出手买入。

## 过滤条件

- **可理解**（必需）：如果没法用简单的话讲清这门生意，归入 `Too Hard`。
- **持久护城河**（必需）：优势必须能够合理地长期延续。
- **所有者盈余稳定**（必需）：账面利润应当能转化为现金。
- **管理层诚信**（必需）：避开糟糕的激励机制与浮夸宣传的行为。
- **高杠杆**（否决项）：债务会把波动变成永久性损失。

## 分析

### 1. 定义这门生意

它卖什么、谁付钱、客户为什么选它，什么在驱动单位经济模型？

### 2. 判断生意质量

评估护城河、持久性、回报、再投资空间、定价权与现金转化。

### 3. 审视管理层

评估激励机制、沟通、回购、收购、债务使用与每股价值创造。

### 4. 估算内在价值

使用保守的所有者盈余或自由现金流。给出保守、基准与乐观三档区间。

## 仓位管理

- **初始仓位**：质量与安全边际都清晰时，先建部分仓位。
- **加仓规则**：论断得到强化或价格变得更好时加仓。
- **最大仓位**：品质与价值都出众时，最高可到 25%。
- **现金规则**：机会成本不佳时，持有现金完全可以接受。

## 风险管理

- **主要风险**：为优质付出过高的价格，或误判护城河的持久性。
- **止损**：基于论断，而非基于价格。
- **相关性**：避免对同一经济驱动因素的隐藏敞口。
- **杠杆**：不用。

## 执行

### 买入规则

1. 生意可理解。
2. 护城河与经济特征能够持久。
3. 管理层值得信任。
4. 价格低于保守内在价值。

### 卖出规则

1. 论断被打破。
2. 管理层失去信誉。
3. 经济特征出现结构性恶化。
4. 估值相对价值变得极端。

## 监控

- **节奏**：季度业绩跟踪，年度深度复盘。
- **指标**：所有者盈余、ROIC、利润率、债务、股数、资本配置。
- **警报**：会计问题、杠杆激增、护城河受侵蚀、管理层变动。

## 操作手册

### 投资备忘录

返回 `Buy`、`Watchlist`、`Pass` 或 `Too Hard`，并附上生意质量、管理层、估值、风险与论断失效触发条件。

## 经典案例

- **美国运通，1964 年**：色拉油丑闻对一家特许经营特质依旧持久的公司造成短暂恐慌，巴菲特此时买入。教训是：把新闻头条造成的暂时伤害，与对生意的永久性损害区分开来。
- **GEICO，1976 年**：一家陷入困境但仍可理解的特许经营企业，承保问题掩盖了其长期的品牌、分销与成本优势。教训是：当可修复的困境创造出安全边际时，买入优质企业。
- **可口可乐，1988 年**：一个拥有定价权、分销规模与漫长再投资空间的持久全球品牌。教训是：为复利型生意支付合理价格，而不是只买统计意义上便宜的资产。

研究这些案例时，重点关注护城河持久性、所有者盈余、管理层质量，以及价格相对保守内在价值的位置。

## 该做与不该做

- 要使用一手资料。
- 要用区间估值。
- 要敢于承认 `Too Hard`。
- 不要把便宜当成优质。
- 不要仅因价格下跌就卖出。
- 不要使用杠杆。




## 播客

- Invest Like the Best: https://open.spotify.com/search/Invest%20Like%20the%20Best/shows
- We Study Billionaires: https://open.spotify.com/search/We%20Study%20Billionaires/shows
- Acquired: https://open.spotify.com/search/Acquired%20podcast/shows
- 共享播客清单：../../docs/podcast-list.md


## YouTube

- 伯克希尔股东大会：https://www.youtube.com/results?search_query=Berkshire+Hathaway+Annual+Meeting
- 共享 YouTube 清单：../../docs/youtube-list.md

## 阅读清单

- 伯克希尔致股东信：https://www.berkshirehathaway.com/letters/letters.html
- 《超级投资者》文章：https://www8.gsb.columbia.edu/articles/columbia-business/superinvestors
- 共享阅读清单：../../docs/reading-list.md

## 来源说明

本模型蒸馏自巴菲特致股东信、伯克希尔年度股东大会实录，以及格雷厄姆的安全边际原则。
