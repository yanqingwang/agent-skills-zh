> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/scientific-writing/references/cli_reference.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 本地 CLI 参考

所有随附命令只使用 Python 标准库。它们：

- 接受显式的 UTF-8 JSON、CSV 或 Markdown 文件；
- 拒绝符号链接形式的输入；
- 对文件大小、记录条数、字段数量、JSON 节点数与嵌套层级设置上限；
- 不发起任何网络调用；
- 不读取任何环境变量或 `.env` 文件；
- 不执行任何动态求值或 pickle 反序列化；
- 报告问题代码、ID 与行号，且不回显稿件原文或来源文本。

请在 skill 目录下用 Python 3.11 或更高版本运行。

## 脚手架

```bash
python3 scripts/scaffold_manuscript.py \
  --output-dir ./draft-workspace \
  --document-id local-draft \
  --study-design randomized_trial \
  --guideline consort-2025
```

输出目录必须尚不存在。该命令绝不覆盖已有文件。生成的文档被明确标注为不完整，
尚不具备投稿条件。

## 清单校验

```bash
python3 scripts/validate_manifest.py manuscript_manifest.json --kind manuscript
python3 scripts/validate_manifest.py source_manifest.json --kind source
python3 scripts/validate_manifest.py source_manifest.json --kind source --require-verified
```

校验器检查结构、ID、核验关卡、保密状态与必需声明状态。它不读取清单内部列出的文件。

## 报告指南路由与覆盖度

```bash
python3 scripts/select_reporting_guidelines.py select --study-design systematic_review
python3 scripts/select_reporting_guidelines.py check reporting_coverage.json
```

选择与覆盖度检查均不产生评分。选定之后请打开官方指南原文。

## 主张与引文审计

```bash
python3 scripts/audit_claims.py manuscript.md claims.csv source_manifest.json
```

CSV 必需的表头：

```text
claim_id,section,claim_kind,claim_text_sha256,evidence_ids,verification_status,uncertainty,analysis_intent
```

在 CSV 中用分号分隔多个证据 ID。使用行内 Markdown 标记：

```text
[claim:C001] [evidence:E001,E002]
```

每个物理行恰好放一个主张。审计会移除 `[claim:...]`、`[evidence:...]` 与 `[@E...]`
标记并折叠空白，然后对该行计算 SHA-256 摘要并与之比对。
它还会校验来源清单的核验元数据，并标记缺少主张标记的数值内容。
归一化规则与限制参见 `evidence_workflow.md`。

## 数值与方法-结果一致性

```bash
python3 scripts/check_consistency.py consistency_manifest.json
```

该命令检查跨章节的重复概念、单位、百分比与分子分母的对应关系、样本量、
证据 ID、已声明的方法、结局映射，以及确证性或探索性定位。

## 参考文献标识符与重复项

```bash
python3 scripts/check_references.py source_manifest.json
```

该命令检查 DOI、PMID、PMCID、ISBN、URL 与归一化标题的本地语法与重复情况。
它绝不解析标识符；每个值都必须由人工与打开后的来源逐项比对。

## 署名与披露

```bash
python3 scripts/validate_authorship.py authorship.json
```

该命令检查人类署名标准、CRediT 角色名称的精确匹配、通讯作者与保证人 ID、最终批准、
声明哈希语法、AI 披露、人工核验、期刊政策审查，以及受限材料的授权关卡。
其中的署名标准是 ICMJE 风格的本地关卡，并非所有期刊的标准。
声明哈希不与稿件正文比对；请人工核对实际声明内容。
记录的日期必须是 `YYYY-MM-DD` 形式的有效日历日期。

## 语言、占位符与保密性 lint

```bash
python3 scripts/lint_manuscript.py manuscript.md \
  --manifest manuscript_manifest.json
```

可能触及敏感内容的提示属于复核提醒，不是去标识化证明。
linter 有意在存在未解决的占位符时判定失败。

## 退出行为

- 退出码 `0`：没有错误级别的问题；
- 退出码 `1`：输入无效，或存在一个或多个错误级别的问题。

警告仍需人工复核。对于相同输入，JSON 输出是确定的。
