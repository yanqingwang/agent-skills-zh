---
name: product-discovery
description: 在验证产品机会、映射假设、规划 discovery sprint，或在投入交付资源之前测试问题-方案契合度（problem-solution fit）时使用。
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`product-team/skills/product-discovery/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 产品探索（Product Discovery）

运行结构化的探索流程，识别高价值机会并降低产品押注的风险。

## 何时使用

在以下场景使用本 Skill：
- 机会解决方案树（Opportunity Solution Tree, OST）引导
- 假设映射与测试规划
- 问题验证访谈与证据综合
- 借助原型/实验进行方案验证
- Discovery sprint（探索冲刺）规划与产出

## 核心探索工作流

1. 定义期望结果（desired outcome）
- 设定一个要改进的可衡量结果。
- 确立基线与目标时间范围。

2. 构建机会解决方案树（OST）
- 结果 -> 机会 -> 方案构想 -> 实验
- 让机会始终扎根于用户证据，而非内部意见。

3. 映射假设
- 识别合意性（desirability）、商业可行性（viability）、技术可行性（feasibility）与可用性（usability）假设。
- 按风险和确定性给假设评分。

使用：
```bash
python3 scripts/assumption_mapper.py assumptions.csv
```

4. 验证问题
- 开展访谈与行为分析。
- 确认问题的频率、严重程度以及解决问题的意愿。
- 尽早否决较弱的机会。

5. 验证方案
- 先做原型，再动手构建。
- 运行概念测试、可用性测试与价值测试。
- 衡量行为，而不只是口头偏好。

6. 规划 discovery sprint
- 1-2 周的周期，带有明确的假设
- 每日证据评审
- 以决策收尾：继续（proceed）、转向（pivot）或停止（stop）

## 机会解决方案树（Teresa Torres）

结构：
- 结果（Outcome）：你想推动的指标
- 机会（Opportunities）：未被满足的客户需求/痛点
- 方案（Solutions）：候选干预手段
- 实验（Experiments）：最快的学习行动

质量检查：
- 在收敛之前至少有 3 个彼此独立的机会。
- 每个头部机会至少对应 2 个实验。
- 每一条分支都关联到证据来源。

## 假设映射

假设类别：
- 合意性（Desirability）：用户想要它
- 商业可行性（Viability）：存在商业价值
- 技术可行性（Feasibility）：团队能够构建/运营它
- 可用性（Usability）：用户能成功使用它

优先级规则：
- 高风险 + 低确定性的假设先测试。

## 问题验证技术

- 聚焦当前行为的问题访谈
- 旅程摩擦点映射
- 工单与销售电话记录综合
- 行为分析数据交叉验证

证据阈值示例：
- 同一痛点在多个目标用户身上重复出现
- 可观察到的变通行为（workaround）
- 当前痛点可衡量的代价

## 方案验证技术

- 概念测试（价值主张的理解度）
- 原型可用性测试（任务成功率/完成时长）
- Fake door（假门）或 concierge（人工代办）测试（需求信号）
- 小范围 beta 用户群（留存/激活信号）

## Discovery Sprint 规划

建议的 10 天结构：
- 第 1-2 天：结果 + 机会界定
- 第 3-4 天：假设映射 + 测试设计
- 第 5-7 天：问题与方案测试
- 第 8-9 天：证据综合 + 决策选项
- 第 10 天：利益相关者决策评审

## 工具

### `scripts/assumption_mapper.py`

CLI 实用工具，功能包括：
- 从 CSV 或内联输入读取假设
- 按风险/确定性评分排出优先级
- 输出附带建议测试类型的、已排定优先级的测试计划

框架细节参见 `references/discovery-frameworks.md`。
