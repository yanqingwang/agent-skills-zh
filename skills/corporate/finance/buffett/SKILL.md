---
name: buffett
description: "在通过巴菲特式所有权视角、所有者盈余、持久护城河、管理层质量、资本配置与安全边际判断来评估一家企业时使用。"
invest: ./invest.md
---

> **中文汉化版** · 上游：[questflowai/investorskills](https://github.com/questflowai/investorskills) · 原文件：`skills/buffett/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 巴菲特式价值复利

用本 Skill 做巴菲特式的企业所有权分析：以低于保守内在价值的价格，买入可理解、生意持久、经济特征优秀、管理层诚实的企业。

## 何时使用

当用户提出以下请求时使用本 Skill：

- 长期企业质量承保（underwriting）
- 护城河与所有者盈余分析
- 内在价值与安全边际评估
- 某只股票是否是可持续复利的企业
- 对一笔长期持仓做复盘

触发词包括 `Buffett`、`owner earnings`、`moat`、`margin of safety`、`intrinsic value`、`quality business`、`compounder`。

## 何时不要使用

- 用户想要短期突破时点的判断。
- 企业超出能力圈（circle of competence）。
- 缺少主要财报文件或足够的经营历史。
- 论断主要依赖宏观时点、技术指标或杠杆。

## 所需输入

- 公司、股票代码与业务描述
- 10-K/10-Q 数据、所有者盈余或自由现金流、ROIC、利润率、债务
- 管理层与资本配置历史
- 当前股价、流通股数、净现金/净债务
- 保守的估值假设

## 流程

1. 判断这门生意是否可理解。
2. 评估护城河、持久性、资本回报率、定价权与再投资空间。
3. 审查管理层诚信与资本配置。
4. 以区间形式估算保守的内在价值。
5. 在给出买入结论前，先要求足够的安全边际。
6. 定义论断失效的条件与需持续跟踪的指标。

## 输出格式

```md
# Buffett View: [Company]

## Verdict
Buy / Watchlist / Pass / Too Hard

## One-Line Thesis

## Business Quality

## Management And Capital Allocation

## Intrinsic Value Range

## Margin Of Safety

## Main Risks

## Invalidation Triggers

## Missing Data
```

## 防护栏

- 不要把便宜的估值倍数当成价值。
- 不要用乐观假设强行推出买入结论。
- 不要忽视杠杆、股权稀释或错误的激励机制。
- 如果论断仍然成立，不要仅因股价下跌就卖出。
- 当企业无法被理解时，直接说 `Too Hard`。

## Questflow 场景下的用法

在 Questflow 中，本 Skill 最适合作为基金策略、观察名单与持仓复盘的长期股权承保模块。
