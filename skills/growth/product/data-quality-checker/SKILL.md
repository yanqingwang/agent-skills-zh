---
name: data-quality-checker
description: 在发布前校验市场分析文档与博客文章中的数据质量。用于检查价格量级不一致（ETF 对期货）、交易品种记号错误、日期/星期不匹配、配分比例加总错误以及单位混用问题。支持英文与日文内容。建议（advisory）模式——将问题标记为警告供人工复核，而非作为发布阻断项。
---

> **中文汉化版** · 上游：[tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) · 原文件：`skills/data-quality-checker/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 概述

在市场分析文档发布之前，检测其中常见的数据质量问题。该检查器校验五个类别：
价格量级一致性（price scale consistency）、交易品种记号（instrument notation）、
日期/星期准确性（date/weekday accuracy）、配分比例加总（allocation totals）以及
单位用法（unit usage）。所有发现均为建议性质——它们将潜在问题标记出来供人工
复核，而不是阻止发布。

## 何时使用

- 在发布每周策略博客或市场分析报告之前
- 在生成自动化市场摘要之后
- 在审校翻译文档（英文/日文）的数据准确性时
- 在将来自多个数据源（FRED、FMP、FINVIZ）的数据合并进同一份报告时
- 作为任何包含金融数据的文档的发布前预检（pre-flight check）

## 前置条件

- Python 3.9+
- 无需任何外部 API 密钥
- 无需任何第三方 Python 包（仅使用标准库）

## 工作流

### 第 1 步：接收输入文档

接受目标 markdown 文件路径及可选参数：
- `--file`：待校验的 markdown 文档路径（必需）
- `--checks`：以逗号分隔的待运行检查项列表（可选；默认：全部）
- `--as-of`：用于年份推断的参考日期，格式为 YYYY-MM-DD（可选）
- `--output-dir`：报告输出目录（可选；默认：`reports/`）

### 第 2 步：执行校验脚本

运行数据质量检查脚本：

```bash
python3 skills/data-quality-checker/scripts/check_data_quality.py \
  --file path/to/document.md \
  --output-dir reports/
```

仅运行指定检查项：

```bash
python3 skills/data-quality-checker/scripts/check_data_quality.py \
  --file path/to/document.md \
  --checks price_scale,dates,allocations
```

提供用于年份推断的参考日期（对日期中未显式写出年份的文档有用）：

```bash
python3 skills/data-quality-checker/scripts/check_data_quality.py \
  --file path/to/document.md \
  --as-of 2026-02-28
```

### 第 3 步：加载参考标准

阅读相关的参考文档，以便为发现的问题提供语境：

- `references/instrument_notation_standard.md` —— 各交易品种类别的标准
  ticker 记号、位数提示（digit-count hints）与命名约定
- `references/common_data_errors.md` —— 常见错误目录，包括 FRED 数据延迟、
  ETF/期货量级混淆、节假日疏漏、配分比例加总陷阱以及单位混淆模式

使用这些参考资料来解释发现的问题并给出修正建议。

### 第 4 步：审查发现

逐一检查输出中的每条发现：

- **ERROR** —— 高置信度问题（例如经日历计算核实的日期-星期不匹配）。
  强烈建议修正。
- **WARNING** —— 很可能有问题、需要人工判断的情况（例如价格量级异常、
  记号不一致、配分比例加总偏差超过 0.5%）。
- **INFO** —— 信息性备注（例如混用 bp/% 但可能是有意为之）。

### 第 5 步：生成质量报告

脚本会产出两个输出文件：

1. **JSON 报告**（`data_quality_YYYY-MM-DD_HHMMSS.json`）：机器可读的发现
   列表，包含严重级别（severity）、类别（category）、消息（message）、
   行号（line number）与上下文（context）。
2. **Markdown 报告**（`data_quality_YYYY-MM-DD_HHMMSS.md`）：按严重级别
   分组的人类可读报告。

将发现呈现给用户，并结合知识库进行解释。针对每个问题给出具体的修正建议。

## 输出格式

### JSON 发现结构

```json
{
  "severity": "WARNING",
  "category": "price_scale",
  "message": "GLD: $2,800 has 4 digits (expected 2-3 digits)",
  "line_number": 5,
  "context": "GLD: $2,800"
}
```

### Markdown 报告结构

```markdown
# Data Quality Report
**Source:** path/to/document.md
**Generated:** 2026-02-28 14:30:00
**Total findings:** 3

## ERROR (1)
- **[dates]** (line 12): Date-weekday mismatch: January 1, 2026 (Monday) -- actual weekday is Thursday

## WARNING (2)
- **[price_scale]** (line 5): GLD: $2,800 has 4 digits (expected 2-3 digits)
  > `GLD: $2,800`
- **[allocations]**: Allocation total: 110.0% (expected ~100%)
```

## 资源

- `scripts/check_data_quality.py` —— 主校验脚本
- `references/instrument_notation_standard.md` —— 记号与价格量级参考
- `references/common_data_errors.md` —— 常见错误模式与预防方法

## 关键原则

1. **建议模式（advisory mode）**：所有发现都是供人工复核的警告。只要脚本
   成功执行，就始终以退出码 0 结束，即使存在发现项也是如此。退出码 1 仅
   保留给脚本自身失败的情况（找不到文件、解析错误）。

2. **感知章节的配分比例检查（section-aware allocation checking）**：仅检查
   配分（allocation）章节内的百分比（通过诸如"配分"、"Allocation"之类的
   标题，或诸如"ウェイト"、"目安比率"之类的表格列名识别）。正文中的
   随机百分比（概率、RSI、同比增速）会被忽略。

3. **双语支持**：同时处理英文与日文的日期格式、星期名称及章节标题。全角
   字符（％、〜、en-dash）会在处理前被归一化（normalize）。

4. **年份推断**：对于未显式标明年份的日期，检查器按以下优先级推断年份：
   `--as-of` 选项、文档标题/元数据中找到的 YYYY 模式，或当前年份并辅以
   6 个月跨年启发式规则。

5. **位数启发式（digit-count heuristic）**：价格量级校验使用位数（小数点前
   的数字个数）而非绝对价格区间。这种做法对随时间推移的价格变动具有韧性，
   同时仍能捕获 ETF/期货混淆类错误。
