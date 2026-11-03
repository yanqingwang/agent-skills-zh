> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/peer-review/references/tool_reference.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 本地工具约定

所有随附工具都是确定性的、基于 Python 3.11+ 标准库的 CLI。它们不发起网络、
模型、图像、子进程、环境变量、动态代码或 pickle 调用。

## 共用的安全行为

- 输入：仅接受本地 JSON、CSV 或 Markdown
- 最大输入体积：4 MiB
- 最大 CSV 行数：5,000
- 仅限 UTF-8；拒绝 NUL 字节
- 拒绝符号链接的输入与输出
- 拒绝重复的 JSON 键与 CSV 表头
- JSON 校验器拒绝未知 schema 字段
- 除非显式给出 `--force`，否则不会替换已存在的输出
- JSON 与 Markdown 输出以原子方式写入，并在支持时使用仅限本人可读的权限
- 报告只包含 ID、计数、规则代码与行号 — 不含稿件、评审、主张、标题、
  作者或参考文献的正文

退出码：

- `0`：结构有效或执行完成
- `1`：解析有效的审计被阻断，或存在规则错误
- `2`：输入格式错误、路径不安全、字段不受支持，或 CLI 校验错误

在 skill 目录下运行工具，或使用脚本的绝对路径。

## 受理校验器

```bash
python3 scripts/validate_review_intake.py \
  assets/review_intake_template.json
```

用途：

- 确认已记录的授权与人类问责
- 记录角色、胜任领域与局限、利益冲突、目标发表载体的政策与评审模式
- 强制仅本地处理、不使用外部服务、不复用数据，以及删除/留存记录
- 以发表载体政策、许可与披露为前提，控制被批准的 AI 协助

随附模板在人类完成各项控制之前会保持阻断状态。

顶层 JSON 字段：

- `schema_version`：`2.0`
- `review_id`：安全的本地标识符，不是稿件标题
- `material`：状态与敏感数据标记
- `authorization`：依据与已记录的许可
- `reviewer`：工作量、问责、胜任力与利益冲突
- `venue_policy`：核查状态、评审模式、保密意见通道
- `ai_use`：政策、计划、许可、披露
- `handling`：仅本地、外部服务、复用、留存方面的控制
- `scope`：稿件类型、请求的重点、局限、专家评审需求

报告校验的是各项声明，而不是声明的真假。

`reviewer.conflict_status` 接受 `not_assessed`、`none_identified`、
`disclosed_to_editor`、`editor_cleared` 或 `unresolved`。仅仅披
露并不能解除冲突：`disclosed_to_editor` 会一直阻断，直到编辑实际放行参与。
校验器无法核实是否已获得放行。

## 报告指南选择器与覆盖度审计

仅选择：

```bash
python3 scripts/select_reporting_guidelines.py \
  assets/study_profile_template.json
```

选择并统计覆盖度：

```bash
python3 scripts/select_reporting_guidelines.py \
  assets/study_profile_template.json \
  --coverage assets/reporting_checklist_template.csv
```

画像字段：

- `schema_version`：`2.0`
- `profile_id`
- `study_types`：标识符，例如 `randomized_trial`
- `report_kind`：`results`、`protocol`、`abstract` 或 `data_release`
- `features`：例如 `ai_based`、`ai_intervention`、`large_language_model`
- `domains`：例如 `health`、`genomics`、`proteomics`

覆盖度列：

- `guideline_id`
- `item_id`：对于已知主条目数量的指南，汇总后的主条目编号
- `status`：`reported`、`partly_reported`、`not_reported`、
  `not_applicable`、`not_assessed`
- `location`：已报告或部分报告的条目必填
- `rationale`：不适用条目必填

目录是 `assets/reporting_guidelines.json`，审阅日期嵌在该文件内；各来源
特有的核验限制见 `assets/source_ledger.csv`。它不会抓取实时更新。输出刻
意不含百分比或质量评分。

对于 AI 试验方案，使用 `study_types: ["randomized_trial"]`、
`report_kind: "protocol"`、`features: ["ai_intervention"]` 与
`domains: ["health"]`；这会选中 SPIRIT 2025 与 SPIRIT-AI 2020。对于 LLM
的开发、调优、提示词工程或评估研究，使用 `study_types: ["llm_study"]`、
`report_kind: "results"`、`features: ["large_language_model"]` 与
`domains: ["health"]`。只有当该设计同样适用时才加上 `prediction_model`。
摘要使用不同的检查表；随附目录不含摘要检查表，因此没有匹配结果并不意味着
不存在适用的指南。

主条目行是汇总性的导航记录。`coverage_record_complete` 表示这些行 ID 都
已填入，即使全部为 `not_assessed`；它并不认证对子条目的覆盖，也不表示评
审已完成。

## 主张-证据矩阵校验器

```bash
python3 scripts/validate_claim_evidence.py \
  assets/claim_evidence_matrix_template.csv
```

列：

- `claim_id`
- `location`
- `claim_type`
- `claim_summary`：仅作输入，绝不回显
- `evidence_ids`：以分号分隔的本地 ID
- `support_level`：`supported`、`partly_supported`、`unsupported`、
  `not_assessed`
- `alignment_issue`：direction、magnitude、population、outcome、timepoint、
  causal language、scope、uncertainty、selective reporting、other 或 none
- `limitation`：仅作输入，绝不回显
- `requested_action`：仅作输入，绝不回显

规则包括：

- 已支持的主张需要证据 ID，且没有声明的对齐问题。
- 部分支持的主张需要证据和问题代码；缺少 requested action 会给出警告，但仍
  需人工处理。
- 未获支持的主张需要问题代码。
- 主张 ID 必须唯一。

该工具不判断证据是否为真或是否充分。

## 统计与可复现性检查清单

```bash
python3 scripts/audit_statistics_reproducibility.py \
  assets/statistical_reproducibility_template.json
```

该 JSON 包含：

- 检查清单与研究设计 ID
- 专家评审声明
- 核心条目记录，含类别、适用性、状态、证据位置、备注与要求的动作

核心领域：

- 问题/估计目标的匹配
- 单位、独立性、样本量、分配与盲法
- 纳入/排除、缺失数据与数据处理
- 预先设定、方法匹配、假设、多重性与依赖性
- 效应估计、不确定性、分母、结局与危害
- 数据/材料访问、代码/环境与溯源
- 伦理/治理、主张解释与选择性报告

该工具要求提供核心条目 ID，但允许额外的安全 ID。它报告缺口与专家评审触发
项，不给出评分。

## 引用/参考文献一致性审计

Markdown 必须使用 Pandoc 风格的引用键：

```markdown
The synthetic method is described elsewhere [@ref-synthetic-2026].
Several sources may be grouped [@ref-one; @ref-two].
```

运行：

```bash
python3 scripts/audit_citations.py \
  local-manuscript.md \
  assets/citation_references_template.csv
```

参考文献 CSV 列：

- `reference_id`
- `title`
- `authors`
- `year`
- `doi`
- `url`
- `verification_status`：`verified_primary`、`verified_secondary` 或 `not_verified`

审计会发现：

- 没有对应参考文献行的引用键
- 未被引用的参考文献行
- 未标记为已核验的被引参考文献
- 缺少 DOI 或 URL 的参考文献
- 引用语法格式错误

它只校验 DOI/URL 的形状。它不解析标识符、不检索网络、不核实存在性，也不
判断某条参考文献是否支持某项主张。

该解析器是一个轻量的括号扫描器，不是 Pandoc。请使用单行分组，例如
`[@ref-one; @ref-two]`，键名以 ASCII 字母开头、最长 96 个字符，可包含字
母、数字、`.`、`_`、`:` 或 `-`。完整的 Pandoc 还支持其他键字符、带花括号
的键、正文中带作者名的引用等本工具不支持的构造。不支持多行分组；代码示例、
链接、转义文本或其他带括号的 `@` 文本都可能产生误匹配。请按
[官方 Pandoc 引用语法](https://pandoc.org/MANUAL.html#citation-syntax)另
行检查这些情况；干净的报告并不能证明每一条引用都被找到。

## 评审脚手架生成器

必须先通过受理校验：

```bash
python3 scripts/generate_review_scaffold.py \
  completed-intake.json \
  -o private-review.md
```

该生成器：

- 读取 `assets/review_scaffold_template.md`
- 只插值安全的受理标识符
- 绝不读取或嵌入稿件文本
- 把致作者的意见与致编辑的保密意见分开
- 提供结构化的主要/次要意见字段
- 包含人类问责与"不得作出编辑决定"的警告

它拒绝未解决的受理控制项与隐式覆盖。

## 语气与可执行性 lint

```bash
python3 scripts/lint_review.py private-review.md
```

必需的标题：

- `# Comments to authors`
- `# Confidential comments to editor`

结构化意见标题：

- `### Major comment M1`
- `### Minor comment m1`

每条意见都必须填写以下字段的非占位内容：

- `Location`
- `Observation`
- `Evidence or criterion`
- `Why it matters`
- `Requested action`

linter 会标记：

- 作者通道与编辑通道缺失或颠倒
- 作者通道中出现仅供编辑的标记
- 未解决的脚手架占位符
- 一小撮冒犯性或人身化用语
- 角色冒充与编辑决定类表述
- 缺失的可执行性字段
- 声称已执行分析但需要溯源支撑的内容

词汇 lint 会有误报与漏报。人工复核仍然必要。

## 私有输出示例

所有输出 JSON 报告的 CLI 都接受：

```bash
-o local-report.json
```

要刻意替换已有输出：

```bash
--force
```

除非授权与发表载体政策允许，不要把输出放在已同步或共享的目录中。按已记录
的评审政策删除或留存输入、草稿与报告。
