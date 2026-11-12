> **中文汉化版** · 上游：[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) · 原文件：`.agents/skills/planning-with-files/templates/analytics_task_plan.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 任务计划：[数据分析项目简述]

把本文件当作数据分析或探索会话的持久路线图。分析推进时保持阶段状态为最新。

## Goal

用一句清楚的话说明要回答的分析问题或要交付的成果。

[一句话描述分析目标]

## Next Step

记录接下来应该发生的单个分析动作。活跃阶段或当前动作一变就更新。

[下一个单独分析动作。阶段状态一变就更新。]

## Current Phase

写出当前正在进行的阶段。

Phase 1

## Phases

每个状态只使用 `pending`、`in_progress` 或 `complete`。

### Phase 1: 数据摸底

- [ ] 识别数据源并建立连接
- [ ] 把 schema 与字段说明记录到 findings.md
- [ ] 评估数据质量（空值、重复、离群值、日期范围）
- [ ] 估算数据集规模与查询性能
- **Status:** in_progress

### Phase 2: 探索性分析

- [ ] 计算关键变量的汇总统计量
- [ ] 可视化分布与关系
- [ ] 识别离群值与异常
- [ ] 把初步模式记录到 findings.md
- **Status:** pending

### Phase 3: 假设检验

- [ ] 把探索阶段的发现形式化为假设
- [ ] 选择合适的统计检验
- [ ] 运行检验并把结果记录到 findings.md
- [ ] 用留出数据或其他方法交叉验证发现
- **Status:** pending

### Phase 4: 综合与报告

- [ ] 带证据总结关键发现
- [ ] 制作最终可视化
- [ ] 记录结论与建议
- [ ] 标注局限性与有待进一步研究的方向
- **Status:** pending

## 假设

把正在研究的问题记录为可检验的假设。

1. [待检验的假设]
2. [待检验的假设]

## Decisions Made

记录分析选择，包括检验方法、过滤条件、排除项及其理由。

| 决策 | 理由 |
|------|------|
|      |      |

## 遇到的错误

记录每个不同的错误、尝试次数与解决方式。重试失败的动作之前先换方法。

| 错误 | 尝试次数 | 解决方式 |
|------|----------|----------|
|      | 1        |          |

## 备注

- 工作推进时更新阶段状态：`pending` 到 `in_progress` 再到 `complete`。
- 重大分析决策前重读 Goal、Next Step 与 Current Phase。
- 及时记录错误，避免重复走失败的路。
- 把查询结果与可视化证据记录到 findings.md。
