> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/citation-management/references/script_reference.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 随附脚本参考

`scripts/` 中每个脚本的用途、参数与用法示例：
`search_openalex.py`、`search_pubmed.py`、`search_google_scholar.py`、
`extract_metadata.py`、`validate_citations.py`、`format_bibtex.py`，
以及 `doi_to_bibtex.py`。

`_common.py` 不是命令。它保存了支持花括号嵌套的 BibTeX 解析器、条目渲染器、
页码范围归一化器，以及上述每个脚本共享的引文键方案——正是这套共享机制
让通过不同数据库找到的条目能够彼此去重。

## 工具与脚本

### search_openalex.py

跨学科检索 OpenAlex。支持无密钥的日常使用；可选的账户 key 会提升可用额度。

**特性**：
- 无密钥 REST API，带 cursor 分页
- 年份范围与作品类型过滤
- 按相关性或被引次数排序
- 从 OpenAlex 的倒排索引重建摘要
- 每条记录都带有开放获取状态
- 导出为 JSON 或 BibTeX

**用法**：
```bash
# Basic search
python scripts/search_openalex.py "quantum computing"

# Most-cited work in a window
python scripts/search_openalex.py "quantum computing" \
  --year-start 2020 \
  --year-end 2024 \
  --limit 100 \
  --sort-by citations \
  --output quantum_papers.json

# Reviews only, straight to BibTeX
python scripts/search_openalex.py "CRISPR gene editing" \
  --type review \
  --limit 50 \
  --format bibtex \
  --output crispr_reviews.bib
```

设置 `OPENALEX_API_KEY` 以使用你的账户额度；它会通过 Authorization 头发送。`OPENALEX_EMAIL`/`--email` 提供可选的联系信息。客户端使用受支持的 100 条分页上限；若任何一页请求失败就报错退出，避免把不完整的参考文献当成完整的报告出来。

### search_google_scholar.py

检索 Google Scholar 并导出结果。

**特性**：
- 可选的非官方 `scholarly` 抓取器；Google 不提供批量 API
- 分页支持
- 年份范围过滤
- 导出为 JSON 或 BibTeX
- 被引次数信息

**用法**：
```bash
# Basic search
python scripts/search_google_scholar.py "quantum computing"

# Advanced search with filters
python scripts/search_google_scholar.py "quantum computing" \
  --year-start 2020 \
  --year-end 2024 \
  --limit 100 \
  --sort-by citations \
  --output quantum_papers.json

# Export directly to BibTeX
python scripts/search_google_scholar.py "machine learning" \
  --limit 50 \
  --format bibtex \
  --output ml_papers.bib
```

`--sort-by citations` 只对取回的样本排序；它不是 Google Scholar 的全局排序。年份边界会传给 `scholarly.search_pubs`。被封锁/失败的检索不会返回参考文献。

### search_pubmed.py

用 E-utilities API 检索 PubMed。

**特性**：
- 复杂查询支持（MeSH、字段标签、布尔运算）
- 日期范围过滤
- 出版类型过滤
- 批量检索并附带元数据
- 导出为 JSON 或 BibTeX

**用法**：
```bash
# Simple keyword search
python scripts/search_pubmed.py "CRISPR gene editing"

# Complex query with filters
python scripts/search_pubmed.py \
  --query '"CRISPR-Cas Systems"[MeSH] AND "therapeutic"[Title/Abstract]' \
  --date-start 2020-01-01 \
  --date-end 2024-12-31 \
  --publication-types "Clinical Trial,Review" \
  --limit 200 \
  --output crispr_therapeutic.json

# Export to BibTeX
python scripts/search_pubmed.py "Alzheimer's disease" \
  --limit 100 \
  --format bibtex \
  --output alzheimers.bib
```

### extract_metadata.py

从论文标识符中提取可获得的元数据。检索得到的 JSON 记录需要 DOI、PMID、PMCID、arXiv ID 或文章 URL；不支持原始 OpenAlex ID。

**特性**：
- 支持 DOI、PMID、PMCID、arXiv ID、URL；标识符参数可重复使用
- 查询 CrossRef、PubMed、arXiv API
- 处理多种标识符类型
- 从换行分隔的标识符或随附的检索 JSON（`results`/`entries`）批量处理
- 输出 BibTeX 或 JSON；部分提取失败时在明确报告失败后以状态码 2 退出

**用法**：
```bash
# Single DOI
python scripts/extract_metadata.py --doi 10.1038/s41586-021-03819-2

# Single PMID
python scripts/extract_metadata.py --pmid 34265844

# Single arXiv ID
python scripts/extract_metadata.py --arxiv 2103.14030

# From URL
python scripts/extract_metadata.py \
  --url "https://www.nature.com/articles/s41586-021-03819-2"

# Batch processing (file with one identifier per line)
python scripts/extract_metadata.py \
  --input paper_ids.txt \
  --output references.bib

# Different output formats
python scripts/extract_metadata.py \
  --doi 10.1038/nature12345 \
  --format json  # or bibtex
```

### validate_citations.py

校验 BibTeX 条目的准确性、完整性、引文数量标准的符合度与手稿集成情况。

**特性**：
- 通过 Crossref、DataCite 与解析器回退做 DOI 注册检查；无法定论的查询记为警告
- 必填字段检查
- 重复项检测
- 格式校验
- 针对指定 venue 的**启发式引文数量警告**；只有显式传入的 `--min-count` 才会强制
- **写作后必做检查**：把手稿中的引文（Markdown 或 LaTeX）与已定义的 BibTeX 条目对应，检测未解析/缺失或未被使用的参考文献
- 详细报告

**用法**：
```bash
# Basic validation
python scripts/validate_citations.py references.bib

# Validate against a venue standard (e.g., Nature, NeurIPS, Literature Review)
python scripts/validate_citations.py references.bib --venue nature
python scripts/validate_citations.py references.bib --venue neurips
python scripts/validate_citations.py references.bib --venue review

# Validate with custom minimum citation count
python scripts/validate_citations.py references.bib --min-count 40

# Check references against a written manuscript file (detect missing or unused citations)
python scripts/validate_citations.py references.bib --manuscript paper.md

# Combined full validation
python scripts/validate_citations.py references.bib \
  --venue nature \
  --manuscript paper.md \
  --report validation_report.json \
  --verbose
```

### format_bibtex.py

格式化并清理 BibTeX 文件。

**特性**：
- 统一格式
- 排序条目（按键、年份、作者）
- 移除重复项
- 校验语法
- 修复常见错误
- 强制引文键命名惯例

**用法**：
```bash
# Basic formatting
python scripts/format_bibtex.py references.bib

# Sort by year (newest first)
python scripts/format_bibtex.py references.bib \
  --sort year \
  --descending \
  --output sorted_refs.bib

# Remove duplicates
python scripts/format_bibtex.py references.bib \
  --deduplicate \
  --output clean_refs.bib

# Complete cleanup
python scripts/format_bibtex.py references.bib \
  --rekey \
  --deduplicate \
  --sort year \
  --output final_refs.bib
```

### doi_to_bibtex.py

快速把 DOI 转为 BibTeX。

**特性**：
- 快速转换单个 DOI
- 从换行分隔的标识符或随附的检索 JSON（`results`/`entries`）批量处理
- 输出 BibTeX 或 JSON；部分提取失败时在明确报告失败后以状态码 2 退出
- 使用独立的操作系统工具管道到剪贴板（例如 `pbcopy`）

**用法**：
```bash
# Single DOI
python scripts/doi_to_bibtex.py 10.1038/s41586-021-03819-2

# Multiple DOIs
python scripts/doi_to_bibtex.py \
  10.1038/nature12345 \
  10.1126/science.abc1234 \
  10.1016/j.cell.2023.01.001

# From file (one DOI per line)
python scripts/doi_to_bibtex.py --input dois.txt --output references.bib

# Copy to clipboard (macOS; use xclip on Linux)
python scripts/doi_to_bibtex.py 10.1038/nature12345 | pbcopy
```
