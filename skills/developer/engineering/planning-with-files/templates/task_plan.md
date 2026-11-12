> **中文汉化版** · 上游：[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) · 原文件：`.agents/skills/planning-with-files/templates/task_plan.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 任务计划：[简述]

把本文件当作该任务的持久路线图。在复杂工作开始前创建它，阶段变化时保持更新。

## Goal

用一句清楚的话说明期望的最终结果。

[一句话描述最终状态]

## Next Step

记录接下来应该发生的单个动作。活跃阶段或当前动作一变就更新。

[下一个单独动作。阶段状态一变就更新。]

## Current Phase

写出当前正在进行的阶段。

Phase 1

## Phases

把任务拆成三到七个可验证的阶段。每个状态只使用 `pending`、`in_progress` 或 `complete`，工作推进时更新对应值。

### Phase 1: 需求与调研

- [ ] 理解用户意图
- [ ] 识别约束与需求
- [ ] 把发现记录到 findings.md
- **Status:** in_progress

### Phase 2: 规划与结构

- [ ] 确定技术方案
- [ ] 需要时创建项目结构
- [ ] 记录决策及其理由
- **Status:** pending

### Phase 3: 实现

- [ ] 按计划逐步执行
- [ ] 执行前先把代码写入文件
- [ ] 增量测试
- **Status:** pending

### Phase 4: 测试与验证

- [ ] 核对所有需求已满足
- [ ] 把测试结果记录到 progress.md
- [ ] 修复发现的问题
- **Status:** pending

### Phase 5: 交付

- [ ] 检查所有输出文件
- [ ] 确保交付物完整
- [ ] 交付给用户
- **Status:** pending

## 关键问题

记录重要问题，问题解决后用答案替换。

1. [待回答的问题]
2. [待回答的问题]

## Decisions Made

记录重要选择及每项选择的理由。

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
- 重大决策前重读 Goal 与 Next Step。
- 及时记录错误，避免重复走失败的路。
