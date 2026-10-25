---
name: graham-net-net
description: "在评估本杰明·格雷厄姆式深度价值时使用：净净资产（net-net）、营运资本便宜货、安全边际、统计意义上的低估与资产负债表保护。"
invest: ./invest.md
---

> **中文汉化版** · 上游：[questflowai/investorskills](https://github.com/questflowai/investorskills) · 原文件：`skills/graham-net-net/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 格雷厄姆净净资产价值

用本 Skill 实践本杰明·格雷厄姆（Benjamin Graham）式的判断。

## 何时使用

当用户提出以下请求时使用本 Skill：

- 净净资产（net-net）筛选
- 深度统计价值
- 资产负债表便宜货
- 格雷厄姆式安全边际

触发词包括 `Graham`、`net-net`、`NCAV`、`margin of safety`、`cigar butt`、`Intelligent Investor`。

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

1. 计算 NCAV / 有形资产价值。
2. 对可疑资产打折，并核查负债。
3. 优先选择一篮子折价标的，而非单只"故事股"。
4. 当价格向价值收敛或资产发生减值时退出。

## 输出格式

```md
# Graham Net-Net Value View: [Subject]

## Verdict
Buy Basket / Buy Single / Watch / Asset Trap / Pass

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
