> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/citation-management/references/search_strategies.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 检索策略

Google Scholar 与 PubMed 的检索式构造：运算符、字段标签、MeSH 主题词、日期与出版类型筛选，
以及经过实际验证的检索式示例。

## 检索策略

### Google Scholar 最佳实践

使用 [Google Scholar 官方文档中的检索控件](https://scholar.google.com/intl/en/scholar/help.html)：
带引号的标题/短语、`author:`、排除词，以及高级检索中的出版物/标题/日期字段。请用年份控件
或脚本参数，而不是 `2020..2024`；Scholar 不提供全局 `sort:citations` 运算符。
引用次数会受文献年龄、学科领域和数据库收录范围影响；它们是发现线索，不是证据质量的
判定阈值。

```bash
# Find recent reviews; examples are illustrative searches.
python scripts/search_google_scholar.py 'CRISPR review' --year-start 2023 --year-end 2024

# Author and topic
python scripts/search_google_scholar.py 'author:Church "synthetic biology"'

# Citation sorting applies only to the retrieved sample.
python scripts/search_google_scholar.py '"deep learning"' \
  --year-start 2012 --year-end 2015 --sort-by citations --limit 50
```

若要按引用数对 API 检索命中的结果做全局排序，请用随附的 OpenAlex 客户端
（`--sort-by citations`）；同时说明不同数据库的收录范围差异。

### PubMed 最佳实践

**使用 MeSH 主题词**：
MeSH（Medical Subject Headings，医学主题词）提供受控词表，用于精确检索。

1. 在 https://meshb.nlm.nih.gov/search **查找 MeSH 主题词**
2. **在检索式中使用**：`"Diabetes Mellitus, Type 2"[MeSH]`
3. **与关键词组合**，以获得更全面的覆盖

**字段标签**：
```
[Title]              # Search in title only
[Title/Abstract]     # Search in title or abstract
[Author]             # Search by author name
[Journal]            # Search specific journal
[Publication Date]   # Date range
[Publication Type]   # Article type
[MeSH]              # MeSH term
```

**构造复杂检索式**：
```bash
# Clinical trials on diabetes treatment published recently
"Diabetes Mellitus, Type 2"[MeSH] AND "Drug Therapy"[MeSH] 
AND "Clinical Trial"[Publication Type] AND 2020:2024[Publication Date]

# Reviews on CRISPR in specific journal
"CRISPR-Cas Systems"[MeSH] AND "Nature"[Journal] AND "Review"[Publication Type]

# Specific author's recent work
"Smith AB"[Author] AND cancer[Title/Abstract] AND 2022:2024[Publication Date]
```

**用于自动化的 E-utilities**：
随附的 PubMed 脚本使用 ESearch 与 EFetch。其他 E-utilities 是文档中给出的手动替代方案：
- **ESearch**：检索并获取 PMID
- **EFetch**：获取完整元数据
- **ESummary**：获取摘要信息
- **ELink**：查找相关文献

完整的 API 文档见 `references/pubmed_search.md`。
