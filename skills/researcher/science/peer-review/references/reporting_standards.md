> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/peer-review/references/reporting_standards.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 报告规范与领域元数据标准

已于 **2026-10-01** 对照一手或官方来源复核；各来源特有的访问限制记录在台账中。带日期的证据记录是 `assets/source_ledger.csv`；机器可读的选择器目录是 `assets/reporting_guidelines.json`。

## 报告规范做什么、不做什么

报告规范指出应当报告哪些信息，让读者能理解并评价一项研究。它本身不是：

- 设计或实施研究的方法
- 偏倚风险工具
- 统计再分析
- 对真实性、重要性、新颖性或稿件价值的度量
- 发表建议

绝不能把核对清单的完成情况自动换算成质量分数。报告完整的研究可能有严重的设计问题；报告不完整的研究可能根本无法评估。把缺失信息记录为报告缺口，再用合适的证据与专业知识，另行评估设计、实施、分析、可复现性或伦理方面的问题。

使用指南的现行声明时，要配合其说明与详述（explanation and elaboration）文档。检查适用的扩展版与目标期刊的投稿要求。当具体的、结合情境的意见更有用时，不要照抄核对清单的措辞。

## 选择流程

1. 确认**报告类型**：结果、方案、摘要，还是数据发布。
2. 确认**研究设计**，而不只是主题或期刊栏目。
3. 叠加横切特征：AI 干预、诊断 AI、常规采集数据、整群设计、定性访谈等。
4. 选定现行基础指南与适用的扩展版。
5. 用官方核对清单记录 `reported`、`partly_reported`、`not_reported`、`not_applicable` 或 `not_assessed`。
6. 对 `not_applicable` 给出理由；不要把它当作缺陷。
7. 报告覆盖度与方法学评价分开处理。

运行：

```bash
python3 scripts/select_reporting_guidelines.py \
  assets/study_profile_template.json \
  --coverage assets/reporting_checklist_template.csv
```

内置目录是带日期的辅助资料，不是实时注册库。当研究类型不明确或可能有更新的扩展版时，查阅 [EQUATOR Network](https://www.equator-network.org/) 与指南官网。

## 主要现行健康研究指南

### 随机试验结果：CONSORT 2025

- 现行声明：**CONSORT 2025**，2025 年 4 月 14 日发表
- 结构：30 条主核对清单条目和一张受试者流程图
- 取代：CONSORT 2010
- 适用对象：随机试验报告
- 配套使用：说明与详述文档，加上设计/干预扩展版
- 重要边界：声明明确表示它不是质量评估工具

检查注册情况、方案与统计分析计划的一致性、随机分配、受试者流程、结局与危害、效应估计与不确定性、方案变更、数据共享、利益冲突，以及如适用的患者/公众参与。

官方来源：[CONSORT–SPIRIT](https://www.consort-spirit.org/) 与 [CONSORT 2025 声明](https://www.bmj.com/content/389/bmj-2024-081123)。

### 随机试验方案：SPIRIT 2025

- 现行声明：**SPIRIT 2025**，2025 年 4 月 28 日发表
- 结构：34 条主核对清单条目和一张受试者时间线
- 取代：SPIRIT 2013
- 适用对象：随机试验方案

将方案与注册信息、统计分析计划、伦理记录、修订以及已完成的试验报告相互对照。有理由的明确不适用声明不算报告缺失。

官方来源：[CONSORT–SPIRIT](https://www.consort-spirit.org/) 与 [SPIRIT 2025 声明](https://www.bmj.com/content/389/bmj-2024-081477)。

### 系统综述：PRISMA 2020

- 现行声明：**PRISMA 2020**（名称为 2020，发表于 2021）
- 结构：27 条主条目、扩展核对清单、摘要核对清单与流程图
- 适用对象：已完成的系统综述，主要是干预效应综述
- 方案：使用 PRISMA-P
- 扩展版：范围综述、诊断准确性、个体参与者数据、网状 Meta 分析、公平性、危害或其他专门综述，使用相应扩展版

PRISMA 明确不评估综述的实施过程或方法学质量。请另行使用合适的方法与偏倚风险工具。

官方来源：[PRISMA 2020 资源](https://www.prisma-statement.org/prisma-2020) 与 [原始声明](https://www.bmj.com/content/372/bmj.n71)。

### 观察性研究：STROBE

- 现行基础声明：**STROBE 2007**
- 结构：22 条主条目，附队列、病例对照、横断面及合并版核对清单
- 适用对象：观察性流行病学研究报告
- 扩展版：例如常规采集健康数据的 RECORD、遗传关联研究的 STREGA、STROBE-MR，以及领域专用扩展版

STROBE 帮助识别选择、测量、偏倚、混杂、缺失数据、敏感性分析与外推性是否得到报告。它不能证明这些方法用得恰当。

官方来源：[STROBE](https://www.strobe-statement.org/)。

### 诊断准确度：STARD 2015

- 现行基础声明：**STARD 2015**
- 结构：30 条主条目和一张流程图
- 适用对象：以参考标准估计诊断准确度的研究

如相关，用合适的工具（如现行 QUADAS 系列）另行评估偏倚风险与适用性。STARD 官方实施指南明确表示不要把报告核对清单当作设计质量工具。

官方来源：[STARD 2015](https://www.equator-network.org/reporting-guidelines/stard/)。

### 以 AI 为核心的诊断准确度：STARD-AI

- 现行声明：**STARD-AI 2025**
- 发表：2025 年 9 月 15 日；2026 年 7 月 13 日发布了作者更正
- 结构：40 条条目，其中相对 STARD 2015 有 18 条新增或修改
- 适用对象：以 AI 为核心的诊断准确度研究，包括合适的诊断分类任务

检查数据集实践、待评价试验（index test）的规格、评估、算法偏倚与公平性、适用性与外推性。若主要目的是开发或评估多变量预测模型，改用 TRIPOD+AI。

官方来源：[STARD-AI](https://www.nature.com/articles/s41591-025-03953-8)。

### 临床预测模型：TRIPOD+AI

- 现行声明：**TRIPOD+AI 2024**
- 结构：27 条主条目，外加 13 条的摘要核对清单
- 取代：TRIPOD 2015
- 适用对象：用回归或机器学习方法开发、评估或更新诊断或预后预测模型

不要仅因论文中出现了名为"AI"的软件就选它。当研究的主要对象是预测模型时才选用。相关扩展版包括 TRIPOD-Cluster、TRIPOD-SRMA 与 TRIPOD-LLM。

官方来源：[TRIPOD](https://www.tripod-statement.org/) 与 [TRIPOD+AI 声明](https://www.bmj.com/content/385/bmj-2023-078378)。

### 病例报告：CARE

- 现行基础核对清单：**CARE 2013**
- 说明与详述/手册：2017
- 结构：13 条主条目
- 适用对象：临床病例报告

检查时间线、诊断推理、干预、结局、不良事件、可得时的患者视角、知情同意、隐私与目标期刊要求。

官方来源：[CARE 核对清单](https://www.care-statement.org/checklist)。

### 在体动物研究：ARRIVE 2.0

- 现行声明：**ARRIVE 2.0**，2020 年 7 月发表
- 结构：10 条必备项（Essential 10）加 11 条推荐项
- 适用对象：生物科学各学科中涉及活体动物的研究

10 条必备项是最低报告集，不是重要性排序。审查研究设计、样本量、纳入/排除、随机化、盲法、结局测量、统计、动物细节、操作流程与结果；同时评估伦理、福利、人道终点、不良事件、方案注册、数据获取与利益相关情况。

官方来源：[ARRIVE 2.0](https://arriveguidelines.org/arrive-guidelines)。

### 质量改进：SQUIRE 2.0

- 现行声明：**SQUIRE 2.0**，2015 年发表
- 结构：18 条主条目
- 适用对象：旨在改进医疗质量、安全、价值或公平的系统层面工作，且其方法致力于把结局与干预联系起来

SQUIRE 指出每一条都应考虑，但并非每个要素都要写进每篇稿件。关注局部情境、理由、干预演变、测量、分析、伦理、意外后果与可持续性。

官方来源：[SQUIRE 2.0](https://www.squire-statement.org/index.cfm?fuseaction=page.viewPage&pageID=471&nodeID=1)。

### 卫生经济学评价：CHEERS 2022

- 现行声明：**CHEERS 2022**
- 结构：28 条主条目
- 取代：CHEERS 2013
- 适用对象：卫生干预的经济学评价

评估视角、对照、时间范围、贴现、结局与成本测量、模型假设、异质性、如适用的分布效应、不确定性、相关方参与、资助与利益冲突。方法学质量请使用单独的批判性评价框架。

官方来源：[ISPOR CHEERS](https://www.ispor.org/heor-resources/good-practices/cheers)。

### 定性研究：SRQR 与 COREQ

- **SRQR**：覆盖面广的定性研究报告标准
- **COREQ**：专门针对访谈与焦点小组的 32 条核对清单

按方法选择，而不是看有没有引语。审查研究者反身性、抽样、情境、数据收集、分析过程、可信度、参与者声音、伦理与局限，不要把某一种认识论强加给所有定性研究传统。

官方注册记录：[SRQR](https://www.equator-network.org/reporting-guidelines/srqr) 与 [COREQ](https://www.equator-network.org/reporting-guidelines/coreq/)。

## AI 扩展版与重叠

选用与研究主要设计和论断匹配的指南：

- AI 干预的随机试验：CONSORT 2025 加 CONSORT-AI 2020
- 此类试验的方案：SPIRIT 2025 加 SPIRIT-AI 2020
- AI 诊断准确度：STARD-AI
- 预测模型开发或性能评估：TRIPOD+AI
- 生物医学 LLM 的开发、调参、提示词工程或评估，包括非预测任务：TRIPOD-LLM 2025；当预测模型报告也适用时，加用 TRIPOD+AI
- 医学影像 AI：在按设计选择的基础指南之外，考虑现行模态指南

2020 年的 AI 扩展版是针对 CONSORT 2010 与 SPIRIT 2013 编写的。应将其实质要求与现行基础指南配合使用，按含义映射，而不是复用旧条目编号。[官方扩展版索引](https://www.consort-spirit.org/extensions)区分了基于 2025 核对清单的扩展版与基于旧版本的扩展版。[CONSORT-AI](https://www.equator-network.org/reporting-guidelines/consort-artificial-intelligence/) 与 [SPIRIT-AI](https://www.equator-network.org/reporting-guidelines/spirit-artificial-intelligence/) 仍列于 EQUATOR。

TRIPOD-LLM 有 19 条主条目和单独的摘要核对清单。在本地选择器中，`llm_study` 搭配特征 `large_language_model` 会选中它，且不会把摘要生成或问答评估误判为预测模型。参见 [TRIPOD-LLM 记录](https://www.equator-network.org/reporting-guidelines/the-tripod-llm-reporting-guideline-for-studies-using-large-language-models/)。

可以同时适用多份指南，但不要制造重复要求。说明每个关注点由哪个基础版与哪个扩展版覆盖。该目录有意保持精简：针对摘要的核对清单与许多扩展版需要从官方来源手动选择。

## 领域元数据标准：经核验的沿用状态

这些标准描述实验或仓库的最低元数据。它们是对研究设计报告与方法学评价的补充，而非替代。

### MIAME 与 MINSEQE

**保留，但需加限定。**NCBI GEO 官方指南说明其提交流程支持：

- 微阵列实验用 MIAME
- 高通量功能基因组学测序实验用 MINSEQE

2026 年 10 月的实时抓取遇到浏览器人机验证；官方搜索索引中的 GEO 指南仍描述这两个标准。请核实现行仓库的字段、文件格式、原始/处理后数据要求与登录号要求；不要把这当作已执行过的仓库提交检查。

官方实施来源：[GEO 与 MIAME/MINSEQE](https://www.ncbi.nlm.nih.gov/geo/info/MIAME.html)。

### MIAPE

**保留为分模块、经时效核验的标准。**HUPO 蛋白质组学标准计划列出了已发布、各自带版本号的组件，包括质谱、质谱信息学、定量、凝胶电泳、凝胶信息学、色谱与毛细管电泳。

只选与实际工作流相关的组件，并核实现行仓库要求。不要把"MIAPE"呈现成一份无版本号的通用核对清单。

官方来源：[HUPO-PSI MIAPE](https://www.psidev.info/miape)。

### MIFlowCyt

**保留，但需加限定。**ISAC 仍将 MIFlowCyt 1.0 列为 ISAC 推荐标准，覆盖实验概述、样本、仪器与数据分析。同时核查现行的 FCS、设门（gating）、panel、对照与 FlowRepository 要求。

官方来源：[ISAC MIFlowCyt](https://isac-net.org/miflowcyt-2/)。

### MIAPPE

植物表型元数据**使用 MIAPPE 1.2**，2024 年 10 月发布。它与 1.1 保持兼容；截至核验日期，2.0 版仍在早期开发中。

官方来源：[MIAPPE 发布页](https://www.miappe.org/releases)。

### MIGS 与 MIMS

**不要把单独的 MIGS/MIMS 当作现行总纲。**基因组标准联盟（GSC）现已把这些旧核对清单归入 **MIxS**（Minimum Information about any Sequence），与更新的核对清单及环境包并列。选择现行 MIxS 版本及适用的核对清单加环境扩展；GSC 现在把这种配对称为 combination（旧文档用 package 一词）。

官方来源：[GSC 标准](https://www.gensc.org/pages/standards-intro.html)。

## 其他研究类型

EQUATOR 数据库收录了数百份指南。常见的补充选择包括：

- 方案：按设计选择的方案指南
- 常规采集的健康数据：RECORD
- 临床实践指南：RIGHT 与 AGREE 报告指南
- 调查研究：与设计匹配的调查报告指南
- 实施研究：现行实施研究报告指南
- 混合方法：现行混合方法指南
- 实验室与组学研究：研究设计报告加现行仓库元数据标准

如果没有合适的指南，就明说。不要硬套最接近的核对清单，也不要自己编造。

## 评审中的覆盖性表述

应当这样写：

> "第 12 条的报告不够清晰，无法确定分析人群。请指明纳入的参与者，并使该分母与图 1 一致。"

不要这样写：

> "该稿件在 CONSORT 上得 18/30 分，因此质量低下。"

报告计数或条目编号仅作为导航辅助。本地选择器刻意不输出任何百分比或价值评分。
