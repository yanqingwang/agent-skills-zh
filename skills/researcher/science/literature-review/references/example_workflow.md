> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/literature-review/references/example_workflow.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 示例工作流

这是一份端到端的示意性操作手册，不是真实执行过的综述。请在本 skill 目录下运行；
在执行后续命令之前，先准备好方案（protocol）、规范化的检索记录、参考文献库与 CSL 文件。
下文的日期刻意采用 2015-2024 这一历史区间。

## 示例工作流

一份生物医学文献综述的完整工作流：

```bash
# 1. Create review document from template
mkdir -p sources styles
cp assets/review_template.md crispr_sickle_cell_review.md

# 2. Optional supplementary discovery (authenticated Parallel account)
parallel-cli search "CRISPR Cas9 sickle cell disease gene therapy efficacy" \
  -q "CRISPR" -q "sickle cell" -q "gene therapy" \
  --json --max-results 10 --excerpt-max-chars-total 27000 \
  --include-domains "scholar.google.com,arxiv.org,pubmed.ncbi.nlm.nih.gov,semanticscholar.org,biorxiv.org,nature.com,science.org,cell.com,pnas.org,nih.gov" \
  -o sources/litreview_crispr_scd-academic.json

parallel-cli search "CRISPR sickle cell disease clinical trials treatment" \
  -q "CRISPR" -q "sickle cell" \
  --json --max-results 10 --excerpt-max-chars-total 27000 \
  -o sources/litreview_crispr_scd-general.json

# 3. Search specialized databases using appropriate skills
# - Use PubMed E-utilities and bioRxiv/medRxiv search or date-metadata APIs
# - Use direct API access for arXiv, Semantic Scholar
# - Save all pages and counts; document any API caps or failed requests
# - Normalize into a JSON array; keep raw exports and provenance

# 4. Process your normalized combined_results.json; raw API envelopes will fail
python scripts/search_databases.py combined_results.json \
  --deduplicate \
  --year-start 2015 \
  --year-end 2024 \
  --format markdown \
  --output search_results.md \
  --summary

# 5. Screen results and extract data
# - Request extracts with --full-content; obtain original reports and record failures
# - Use independent final full-text decisions and retain exclusion reasons
# - Track records, reports, studies, and overlapping participants separately
# - Extract key data into the review document
# - Organize by themes

# 6. Write the review following template structure
# - Introduction with clear objectives
# - Detailed methodology section
# - Results organized thematically
# - Critical discussion
# - Clear conclusions

# 7. Check DOI registration/metadata, then manually verify identity and claim support
python scripts/verify_citations.py crispr_sickle_cell_review.md

# Review the citation report
cat crispr_sickle_cell_review_citation_report.json

# Investigate missing/inconclusive results; transient failures do not invalidate citations
python scripts/verify_citations.py crispr_sickle_cell_review.md

# 8. Render after supplying bibliography, local CSL, and [@key] citations
# For manually typed references, omit those options; text will not be restyled
python scripts/generate_pdf.py crispr_sickle_cell_review.md \
  --bibliography crispr_sickle_cell_review.bib --csl styles/nature.csl \
  --output crispr_sickle_cell_review.pdf

# 9. Review final PDF and markdown outputs
```
