> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/scientific-writing/references/reporting_guidelines.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 报告指南的选择与覆盖度

## 目的与局限

报告指南帮助作者把研究设计、执行过程、分析与发现报告得足够完整，以便被评价。
它们不会让一项研究变得严谨，不能替代方案，无法修补缺失的方法，不评估偏倚风险，
不为合规性背书，也不预测稿件是否会被接收。随附的选择器与覆盖度检查器
刻意不产生评分 [SW-S06, SW-S12]。

务必打开当前的官方声明、核对清单、解释与扩展文件、相关扩展，以及目标期刊的
投稿须知。随附的登记簿是一份带日期的路由辅助工具，不是任何官方核对清单的副本。

## 检索到的当前主要指南

- **随机对照试验结果：** CONSORT 2025。官方联合站点提供声明、核对清单、
  扩展核对清单、流程图以及解释与扩展文件 [SW-S07, SW-S08]。
- **随机对照试验方案：** SPIRIT 2025 及其受试者时间线资源 [SW-S07, SW-S09]。
- **系统综述与 meta 分析：** PRISMA 2020。从官方 PRISMA 与 EQUATOR 站点
  选择相关的扩展，例如方案、范围综述、检索或诊断准确性方面的指导 [SW-S10, SW-S06]。
- **队列研究、病例对照研究与横断面研究：** STROBE 以及适用的
  设计专用核对清单 [SW-S11]。
- **诊断准确性研究：** STARD 2015；以 AI 为中心的诊断准确性研究另加 STARD-AI
  [SW-S12, SW-S13]。
- **临床预测模型：** TRIPOD+AI 2024 涵盖回归与机器学习预测模型研究，
  取代了 TRIPOD 2015；其适用范围内的生物医学或医疗 LLM 研究另加 TRIPOD-LLM [SW-S14]。
- **病例报告：** CARE 2013，包含对知情同意敏感的报告要求 [SW-S15]。
- **动物活体研究：** ARRIVE 2.0，按需同时使用 Essential 10 与 Recommended Set
  [SW-S16]。
- **医疗质量改进：** SQUIRE 2.0 [SW-S17]。
- **健康经济学评价：** CHEERS 2022 [SW-S18]。
- **定性研究：** 一般使用 SRQR，并通过 EQUATOR 核实 COREQ 或其他设计专用
  指南是否更为合适 [SW-S06]。

对于 AI 干预试验或方案，除当前的母声明之外还要查阅 CONSORT-AI 或 SPIRIT-AI。
对于常规收集的数据、伤害、公平性、患者报告结局、整群设计、非劣效设计、
先导研究以及其他特殊设计，请到 EQUATOR 检索当前的扩展 [SW-S06]。

## 选择器

使用离线登记簿：

```bash
python3 scripts/select_reporting_guidelines.py select --study-design randomized_trial
python3 scripts/select_reporting_guidelines.py select --study-design randomized_trial --protocol
python3 scripts/select_reporting_guidelines.py select --study-design diagnostic_accuracy --ai
python3 scripts/select_reporting_guidelines.py select --study-design prediction_model --ai --llm
```

输出结果是一组候选。必须由人确认：

- 实际的研究设计与文章类型；
- 写的是方案报告还是结果报告；
- 每一项相关的扩展；
- 当前版本与勘误情况；
- 目标期刊的要求。

如果本地没有匹配项，请到官方 EQUATOR 库中检索，而不是勉强套用最接近的指南。

## 覆盖度记录

随附的 `coverage_topics` 是原创的高层次提示。它们不复现官方条目的措辞或编号。

对每一个主题，记录：

- `addressed`，并附稿件中的位置；
- `not_applicable`，并附理由说明；
- `missing`。

然后运行：

```bash
python3 scripts/select_reporting_guidelines.py check reporting_coverage.json
```

通过意味着每个随附主题都带有允许的状态以及位置或理由说明。
这并不表示官方核对清单的每一条都已满足或都已得到良好报告。

## 工作流

1. 在规划阶段选择候选指南。
2. 打开官方声明与解释文件。
3. 在适用的情况下，把前瞻性条目记录到方案、登记簿或分析计划中。
4. 依据证据与方法记录起草稿件。
5. 用稿件中的实际位置完成官方核对清单。
6. 如实记录缺失条目，不要编造信息来填满它们。
7. 如果期刊要求，提交官方核对清单或流程图。
8. 在投稿前即刻重新核对指南与期刊的版本。

## 常见错误

- 把核对清单当成设计质量的评分；
- 只审查了其中一部分，却宣称已完全遵循；
- 使用过时的母声明，同时忽略了当前的更新；
- 遗漏了相关的扩展；
- 把实际未做的方法写成好像做过；
- 只勾选方框而不记录稿件中的位置；
- 以为期刊的认可意味着投稿要求在各文章类型之间完全相同。
