---
name: munger
description: "在通过查理·芒格式心智模型评估一项决策时使用：逆向思考、激励机制、质量筛选、多学科推理与集中式判断。"
invest: ./invest.md
---

> **中文汉化版** · 上游：[questflowai/investorskills](https://github.com/questflowai/investorskills) · 原文件：`skills/munger/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 芒格心智模型

用本 Skill 实践查理·芒格式的判断力：把问题反过来想，先排除明显的愚蠢，审视激励机制，运用多个心智模型，并且只在质量与理解度都异常高时才行动。

## 何时使用

当用户提出以下请求时使用本 Skill：

- 对一项投资做心智模型分析
- 逆向思考与事前验尸（pre-mortem）复盘
- 激励机制与管理层质量分析
- 某项决策是否在能力圈之内
- 行动前的集中式决策复盘

触发词包括 `Munger`、`mental models`、`inversion`、`incentives`、`latticework`、`circle of competence`、`avoid stupidity`。

## 何时不要使用

- 用户需要机械化的技术性入场点。
- 决策只取决于短期价格波动。
- 信息不足以理解激励机制与生意质量。
- 用户只是想为已做的决策寻求认同。

## 所需输入

- 公司或决策背景
- 商业模式与经济特征
- 管理层、客户、监管方与竞争者的激励机制
- 已知风险、未知因素与失效模式
- 当前估值或机会成本（如相关）

## 流程

1. **逆向**：问自己这笔投资怎么会惨败。
2. 检查能力圈，拒绝无法理解的东西。
3. 审视激励机制与代理问题。
4. 多模型并用：竞争、规模、习惯、心理、杠杆、监管与机会成本。
5. 寻找"合奏效应"（lollapalooza）——多种力量相互强化之处。
6. 判断答案是否足够明显，以至于值得集中下注。

## 输出格式

```md
# Munger View: [Decision]

## Verdict
Act / Wait / Pass / Too Hard

## Inversion

## Incentives

## Mental Models Applied

## Quality Filter

## Opportunity Cost

## Biggest Ways This Fails

## Missing Data
```

## 防护栏

- 对本该被快速否决的事，不要过度复杂化。
- 不要忽视激励机制。
- 不要在能力圈之外投资。
- 不要把聪明误认为判断力。
- 先避开明显的愚蠢，再追求卓越。

## Questflow 场景下的用法

在 Questflow 中，本 Skill 最适合作为启动、复制、确定仓位或集中持仓之前的"决策质量层"，用于基金策略。
