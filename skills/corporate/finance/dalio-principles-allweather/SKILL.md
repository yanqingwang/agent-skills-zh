---
name: dalio-principles-allweather
description: "在通过瑞·达利欧式经济机器、债务周期、多元化、风险平价与全天候资产配置评估投资组合时使用。"
invest: ./invest.md
---

> **中文汉化版** · 上游：[questflowai/investorskills](https://github.com/questflowai/investorskills) · 原文件：`skills/dalio-principles-allweather/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 达利欧全天候原则

用本 Skill 实践瑞·达利欧（Ray Dalio）式的判断。

## 何时使用

当用户提出以下请求时使用本 Skill：

- 全天候（all-weather）组合设计
- 宏观环境（regime）下的资产配置
- 风险平价（risk parity）复盘
- 债务周期中的仓位安排

触发词包括 `Dalio`、`All Weather`、`risk parity`、`economic machine`、`debt cycle`、`diversify`。

## 何时不要使用

- 场景超出本模型适用范围，且另一个投资人 Skill 更合适。
- 关键数据缺失，而本模型必须依赖它。
- 用户想要保证收益或无上限的杠杆。
- 请求只是泛泛的市场闲聊，没有决策目的。

## 所需输入

- 资产、组合、主题或市场背景
- 相关的财务、市场、环境或结构性数据
- 时间跨度与风险约束
- 当前价格/估值或组合权重（若需要定仓位）

## 流程

1. 判断增长与通胀所处的宏观环境。
2. 识别债务周期阶段与政策约束。
3. 按风险贡献度在股票、债券、商品、黄金、现金之间配置。
4. 当环境或风险贡献度发生漂移时再平衡。

## 输出格式

```md
# Dalio Principles All-Weather View: [Subject]

## Verdict
Overweight / Underweight / Hedge / Neutral / Rebalance

## Setup / Thesis

## Evidence

## Risks

## Action Plan

## Invalidation

## Missing Data
```

## 防护栏

- 当筛选条件不满足时，不要强行交易。
- 不要忽视风险、流动性或环境约束。
- 除非用户要求对比，不要把本模型与其他模型混用。
- 把事实、假设与判断分开陈述。

## Questflow 场景下的用法

在 Questflow 中，本 Skill 最适合作为基金、研究工作流、监控与风险感知决策支持中的判断模块。
