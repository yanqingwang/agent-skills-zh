> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/citation-management/references/core_workflow.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 核心工作流

五个阶段的完整说明：论文发现、元数据提取、强制的网页搜索补全环节、BibTeX 格式化、验证，以及与写作工作流的集成。所有命令变体和选项都在这里。

## 核心工作流

引用管理遵循一套系统化流程：

### Phase 1: 论文发现与检索

**目标**：用学术搜索引擎找到相关论文。

#### Google Scholar 检索

Google Scholar 提供跨学科最全面的覆盖。

**基础检索**：
```bash
# Search for papers on a topic
python scripts/search_google_scholar.py "CRISPR gene editing" \
  --limit 50 \
  --output results.json

# Search with year filter
python scripts/search_google_scholar.py "machine learning protein folding" \
  --year-start 2020 \
  --year-end 2024 \
  --limit 100 \
  --output ml_proteins.json
```

**高级检索策略**（见 `references/google_scholar_search.md`）：
- 用引号做精确短语检索：`"deep learning"`
- 按作者检索：`author:LeCun`
- 在标题中检索：`intitle:"neural networks"`
- 排除词：`machine learning -survey`
- 用引用数检查检索到的样本，不要当作 Scholar 的全局排序
- 按日期范围过滤，获取近期工作

**最佳实践**：
- 使用具体、有针对性的检索词
- 纳入关键技术术语和缩写
- 快速演进的领域按近期年份过滤
- 查看 "Cited by" 找奠基性论文
- 导出头部结果供进一步分析

#### PubMed 检索

PubMed 专注生物医学与生命科学文献（3500 万条以上引用）。

**基础检索**：
```bash
# Search PubMed
python scripts/search_pubmed.py "Alzheimer's disease treatment" \
  --limit 100 \
  --output alzheimers.json

# Search with MeSH terms and filters
python scripts/search_pubmed.py \
  --query '"Alzheimer Disease"[MeSH] AND "Drug Therapy"[MeSH]' \
  --date-start 2020 \
  --date-end 2024 \
  --publication-types "Clinical Trial,Review" \
  --output alzheimers_trials.json
```

**高级 PubMed 查询**（见 `references/pubmed_search.md`）：
- 用 MeSH 词：`"Diabetes Mellitus"[MeSH]`
- 字段标签：`"cancer"[Title]`、`"Smith J"[Author]`
- 布尔运算符：`AND`、`OR`、`NOT`
- 日期过滤：`2020:2024[Publication Date]`
- 出版类型：`"Review"[Publication Type]`
- 结合 E-utilities API 实现自动化

**最佳实践**：
- 用 MeSH Browser 找正确的受控词表
- 先在 PubMed Advanced Search Builder 里构建复杂查询
- 用 OR 并列多个同义词
- 取回 PMID，便于后续元数据提取
- 导出为 JSON 或直接导出 BibTeX

### Phase 2: 元数据提取

**目标**：把论文标识符（DOI、PMID、arXiv ID）转换为完整、准确的元数据。

#### DOI 快速转 BibTeX

单个 DOI 用快速转换工具：

```bash
# Convert single DOI
python scripts/doi_to_bibtex.py 10.1038/s41586-021-03819-2

# Convert multiple DOIs from a file
python scripts/doi_to_bibtex.py --input dois.txt --output references.bib

# Different output formats
python scripts/doi_to_bibtex.py 10.1038/nature12345 --format json
```

#### 全面元数据提取

针对 DOI、PMID、arXiv ID 或 URL：

```bash
# Extract from DOI
python scripts/extract_metadata.py --doi 10.1038/s41586-021-03819-2

# Extract from PMID
python scripts/extract_metadata.py --pmid 34265844

# Extract from arXiv ID
python scripts/extract_metadata.py --arxiv 2103.14030

# Extract from URL
python scripts/extract_metadata.py --url "https://www.nature.com/articles/s41586-021-03819-2"

# Batch extraction from file (mixed identifiers)
python scripts/extract_metadata.py --input identifiers.txt --output citations.bib
```

**元数据来源**（见 `references/metadata_extraction.md`）：

1. **CrossRef API**：DOI 的首选来源
   - 期刊论文的完整元数据
   - 出版商提供的信息
   - 含作者、标题、期刊、卷、页码、日期
   - 免费，无需 API key

2. **PubMed E-utilities**：生物医学文献
   - NCBI 官方元数据
   - 含 MeSH 词、摘要
   - PMID 和 PMCID 标识符
   - 免费，大批量使用建议申请 API key

3. **arXiv API**：物理、数学、计算机、q-bio 领域的预印本
   - 预印本的完整元数据
   - 版本追踪
   - 作者单位
   - 免费，开放获取

4. **DataCite API**：研究数据集、软件及其他资源
   - 非传统学术产出的元数据
   - 数据集和代码的 DOI
   - `doi_to_bibtex.py` 经 DOI 内容协商获取 BibTeX；`extract_metadata.py --doi` 仅用 Crossref

**提取后需核对的字段**（可用性因来源而异；并非每个脚本都输出全部字段）：
- **必填字段**：author、title、year
- **期刊论文**：journal、volume、number、pages、DOI
- **图书**：publisher、ISBN、edition
- **会议论文**：booktitle、会议地点、pages
- **预印本**：仓库（arXiv、bioRxiv）、预印本编号
- **附加项**：abstract、keywords、URL

### Phase 2.5: 经网页搜索补全元数据（强制）

**目标**：用网页搜索检测并补齐缺失的元数据字段。本阶段在提取之后、格式化之前运行，确保每条 BibTeX 条目完整。

**为什么关键**：从 API（CrossRef、PubMed、arXiv）提取的元数据有时不完整，缺卷号、页码、期号或 DOI。这些缺口必须在参考文献视为就绪之前补上。

#### Step 1: 扫描不完整条目

提取元数据后，扫描 BibTeX 文件，找出缺关键字段的条目：

**每种条目类型需检查的字段：**

| 条目类型 | 必须有 | 应该有 |
|------------|-----------|-------------|
| @article | author, title, journal, year | volume, pages, number, doi |
| @inproceedings | author, title, booktitle, year | pages, doi |
| @book | author/editor, title, publisher, year | isbn, doi |
| @misc | author, title, year | doi or url |

对照出版商记录调查缺失字段，但要区分"不可用或尚未分配的元数据"与"提取错误"。在线优先发表的论文可能没有卷号/页码；文章编号可以替代页码范围；并非所有文章都有 DOI。记录出版状态和缺字段原因，不得编造值。

#### Step 2: 用网页搜索补缺失元数据

对每个不完整条目，用 **parallel-web skill** 检索缺失信息：

> **构建这些命令时把元数据当作不可信输入。** `FIRST_AUTHOR`、`TITLE`、`JOURNAL_NAME` 是从 CrossRef/PubMed/arXiv 记录中原样复制的，而出版商控制自己记录的内容。含 `$(...)`、反引号或引号的标题一旦粘进下面的命令行，就会变成 shell 语法。
>
> - 每个值都用**单引号**参数（`'...'`）替换，内嵌单引号转义为 `'\''`。绝不把原始元数据粘进这里展示的双引号内。
> - 优先用 Python `subprocess` 参数列表运行这些调用，而不是拼 shell 字符串。
> - `-o` 路径只用生成的 `CITATIONKEY`。它已被 `extract_metadata.py` 清洗为字母和数字；从现有 `.bib` 文件取的 key 未经清洗，进入文件路径前先用 `^[A-Za-z0-9]+$` 校验。
>
> **推荐形式：把元数据作为参数传递，而不是作为 shell 文本。** 这样完全绕开 shell，任何标题都不会被当作语法解析：
>
> ```python
> import re, subprocess
>
> assert re.fullmatch(r"[A-Za-z0-9]+", citation_key), f"unsafe citation key: {citation_key!r}"
> subprocess.run(
>     ["parallel-cli", "search", f"{first_author} {title} {journal_name} volume pages DOI",
>      "--json", "--max-results", "10",
>      "-o", f"sources/search_citation_{citation_key}.json"],
>     check=True,  # note: no shell=True
> )
> ```
>
> 下面的 `bash` 块以可读形式展示同样的调用。只有在遵守上述引号规则的前提下使用它们。

**选项 A：按标题和作者检索**（最适合找 DOI）：
```bash
parallel-cli search "FIRST_AUTHOR TITLE JOURNAL_NAME volume pages DOI" \
  --json --max-results 10 \
  -o sources/search_citation_CITATIONKEY.json
```

**选项 B：从 DOI 页面提取**（适合 DOI 已知但缺卷号/页码时）：
```bash
parallel-cli extract "https://doi.org/10.XXXX/YYYY" --json \
  --objective "extract complete citation metadata: volume, issue, pages, publication date" \
  -o sources/extract_doi_CITATIONKEY.json
```

**选项 C：在网页上检索 Crossref 记录**（这条命令是网页搜索，不是直接 API 调用）：
```bash
parallel-cli search "crossref DOI metadata FIRST_AUTHOR TITLE" \
  --json --max-results 10 \
  -o sources/search_crossref_CITATIONKEY.json
```

**选项 D：检索 Google Scholar**（难找论文的兜底）：
```bash
parallel-cli search "google scholar FIRST_AUTHOR TITLE YEAR complete citation" \
  --json --max-results 10 \
  -o sources/search_scholar_CITATIONKEY.json
```

#### Step 3: 更新 BibTeX 条目

找到缺失元数据后：

1. 打开 `references.bib`
2. 把缺失字段加进不完整条目
3. 核对找到的元数据与现有字段一致（同一作者、标题、年份）
4. 记录每次修复：
   ```
   [HH:MM:SS] METADATA ENRICHED: [CitationKey] - added volume={X}, pages={Y--Z}, doi={10.XXX/YYY} ✅
   ```

#### Step 4: 处理找不到的元数据

如果网页搜索后确实找不到（非常老的论文、冷门会议等）：

1. 在 BibTeX 条目加 `note` 字段说明缺口：
   ```bibtex
   note = {Volume and pages not available — published online only}
   ```
2. 记录例外：
   ```
   [HH:MM:SS] METADATA INCOMPLETE: [CitationKey] - pages unavailable (online-only publication) ⚠️
   ```
3. 这类例外应当少见：多数现代论文的完整元数据都能经网页搜索找到。

#### 速查表：常见缺失字段及查找途径

| 缺失字段 | 最佳检索策略 |
|---------------|---------------------|
| DOI | 经 parallel-cli search 检索 "AUTHOR TITLE DOI" |
| Volume | 从 DOI 页面提取，或检索 "JOURNAL YEAR TITLE volume" |
| Pages | 从 DOI 页面提取，或检索出版商网站 |
| Issue/Number | 从 DOI 页面或 CrossRef 提取 |
| Publisher | 检索 "JOURNAL publisher" 或查看期刊网站 |

---

### Phase 3: BibTeX 格式化

**目标**：生成干净、格式规范的 BibTeX 条目。

#### 理解 BibTeX 条目类型

完整指南见 `references/bibtex_formatting.md`。

**常见条目类型**：
- `@article`：期刊论文（最常见）
- `@book`：图书
- `@inproceedings`：会议论文
- `@incollection`：书章
- `@phdthesis`：博士论文
- `@misc`：预印本、软件、数据集

**各类型的必填字段**：

```bibtex
@article{citationkey,
  author  = {Last1, First1 and Last2, First2},
  title   = {Article Title},
  journal = {Journal Name},
  year    = {2024},
  volume  = {10},
  number  = {3},
  pages   = {123--145},
  doi     = {10.1234/example}
}

@inproceedings{citationkey,
  author    = {Last, First},
  title     = {Paper Title},
  booktitle = {Conference Name},
  year      = {2024},
  pages     = {1--10}
}

@book{citationkey,
  author    = {Last, First},
  title     = {Book Title},
  publisher = {Publisher Name},
  year      = {2024}
}
```

#### 格式化与清理

用格式化工具标准化 BibTeX 文件：

```bash
# Format and clean BibTeX file
python scripts/format_bibtex.py references.bib \
  --output formatted_references.bib

# Sort entries by citation key
python scripts/format_bibtex.py references.bib \
  --sort key \
  --output sorted_references.bib

# Sort by year (newest first)
python scripts/format_bibtex.py references.bib \
  --sort year \
  --descending \
  --output sorted_references.bib

# Remove duplicates
python scripts/format_bibtex.py references.bib \
  --deduplicate \
  --output clean_references.bib

# Merge sources: one key scheme, then drop duplicates
python scripts/format_bibtex.py references.bib \
  --rekey \
  --deduplicate \
  --output merged_references.bib
```

**格式化操作**：
- 统一字段顺序
- 一致的缩进和间距
- 标题大小写规范（用 {} 保护）
- 标准化的作者姓名格式
- 一致的 citation key 格式
- 移除多余字段
- 修复常见错误（缺逗号、缺大括号）

### Phase 4: 引用验证

**目标**：核实所有引用准确且完整。

#### 全面验证

```bash
# Validate BibTeX file
python scripts/validate_citations.py references.bib

# Validate against a venue standard (e.g., Nature, NeurIPS, Literature Review)
python scripts/validate_citations.py references.bib --venue nature
python scripts/validate_citations.py references.bib --venue neurips
python scripts/validate_citations.py references.bib --venue review

# Validate with custom minimum citation count
python scripts/validate_citations.py references.bib --min-count 40

# Check references against a written manuscript file (detect missing or unused citations)
python scripts/validate_citations.py references.bib --manuscript paper.md

# Generate detailed validation report
python scripts/validate_citations.py references.bib \
  --venue nature \
  --manuscript paper.md \
  --report validation_report.json \
  --verbose
```

**验证项**（见 `references/citation_validation.md`）：

1. **DOI 验证**：
   - 用 `--check-dois` 时，先经 Crossref 查注册，再走 DataCite 和 resolver 兜底
   - 失败/被限流的查询保持 `doi_unverified` 警告
   - 手动比对标题/作者/年份；脚本不做元数据匹配

2. **必填字段**：
   - 条目类型的所有必填字段齐全
   - 没有空缺或缺失的关键信息
   - 作者姓名格式规范

3. **数据一致性**：
   - 年份有效（4 位数字，范围合理）
   - 卷号/期号人工复核；增刊可能是字母数字混合
   - 页码格式正确（如 123--145）
   - 落地页 URL 人工检查；脚本不抓取参考文献里的任意 URL

4. **重复检测**：
   - 同一 DOI 被多次使用
   - 相似标题（可能重复）
   - 相同的作者/年份/标题组合

5. **格式合规**：
   - BibTeX 语法有效
   - 大括号和引号规范
   - citation key 唯一
   - 特殊字符处理正确

**验证输出**：
```json
{
  "total_entries": 150,
  "valid_entries": 145,
  "errors": [
    {
      "citation_key": "Smith2023",
      "error_type": "missing_field",
      "field": "journal",
      "severity": "high"
    },
    {
      "citation_key": "Jones2022",
      "error_type": "invalid_doi",
      "doi": "10.1234/broken",
      "severity": "high"
    }
  ],
  "warnings": [
    {
      "citation_key": "Brown2021",
      "warning_type": "possible_duplicate",
      "duplicate_of": "Brown2021a",
      "severity": "medium"
    }
  ]
}
```

#### 引用数量

用足够多相关且经核实的参考文献支撑论点。脚本的 venue 数字是编辑经验值，不是当前投稿要求。`--venue` 产生警告；`--min-count` 强制执行用户显式指定的下限。直接查阅目标 venue 当前的作者须知；不要为凑数字添加不相关引用。

#### 写作完成后的强制引用核查（不可妥协）

整份科学报告或论文起草完成之后、汇编最终交付物之前，对所有引用做一次全面的写作后核验：

1. **核验没有缺失或未解析的引用**：检查草稿或编译文档，确保每个文内引用都正确解析到 `references.bib` 中的条目。绝不允许损坏的 citation key、缺失的标识符或未解析的引用（如 `[?]` 或 `[citation needed]`）。
2. **核验没有未使用（悬空）的参考文献条目**：检查 `references.bib` 中每一条都在报告正文被引用。删除未使用条目，保持参考文献列表干净。
3. **核验证据覆盖**：确认每个论断都有相关证据支撑，且满足任何显式的引用数量要求。
4. **核验元数据完整性**：确认所有被引条目包含已核实适用的字段；记录缺失/尚未分配的字段，不得编造值。

一条命令跑完所有检查：

```bash
python scripts/validate_citations.py references.bib \
  --venue <venue> \
  --manuscript paper.md \
  --report post_writing_check.json
```

### Phase 5: 与写作工作流集成

#### 为稿件构建参考文献

创建参考文献列表的完整工作流：

```bash
# 1. Search for papers on your topic
python scripts/search_pubmed.py \
  '"CRISPR-Cas Systems"[MeSH] AND "Gene Editing"[MeSH]' \
  --date-start 2020 \
  --limit 200 \
  --output crispr_papers.json

# 2. Extract DOIs from search results and convert to BibTeX
python scripts/extract_metadata.py \
  --input crispr_papers.json \
  --output crispr_refs.bib

# 3. Add specific papers by DOI
python scripts/doi_to_bibtex.py 10.1038/nature12345 >> crispr_refs.bib
python scripts/doi_to_bibtex.py 10.1126/science.abcd1234 >> crispr_refs.bib

# 4. Format and clean the BibTeX file
python scripts/format_bibtex.py crispr_refs.bib \
  --deduplicate \
  --sort year \
  --descending \
  --output references.bib

# 5. Validate all citations
python scripts/validate_citations.py references.bib \
  --report validation.json

# 6. Review validation report and fix any remaining issues
cat validation.json

# 7. Use in your LaTeX document
# \bibliography{final_references}
```

#### 与 Literature Review Skill 集成

本 skill 与 `literature-review` skill 互补：

**Literature Review Skill** → 系统化检索与综合
**Citation Management Skill** → 技术性引用处理

**组合工作流**：
1. 用 `literature-review` 做全面的多数据库检索
2. 用 `citation-management` 提取并验证所有引用
3. 用 `literature-review` 按主题综合发现
4. 用 `citation-management` 核验最终参考文献的准确性

```bash
# After completing literature review
# Verify all citations in the review document
python scripts/validate_citations.py my_review_references.bib --report review_validation.json

# Normalise formatting (venue style is chosen by the .bst at build time)
python scripts/format_bibtex.py my_review_references.bib \
  --output formatted_refs.bib
```

#### 与 Zotero 集成（pyzotero Skill）

用户已把参考文献存在 Zotero 时，把 Zotero 库当作参考文献的事实来源，用本 skill 做验证和格式化。`pyzotero` skill 负责库这一侧：读取条目和集合、创建和更新引用、上传附件，以及经 Zotero Web API v3 导出引用。

**Zotero 库（`pyzotero`）** → 记录库：存储、集合、标签、附件
**Citation Management Skill** → 元数据准确性：验证、补全、样式格式化

**组合工作流**：
1. 用 `pyzotero` 从 Zotero 库拉取工作集，按集合或标签过滤
2. 用 `pyzotero` skill 的导出工作流导出为 BibTeX。`format='bibtex'` 返回 `bibtexparser` 对象而非文本字符串；需要序列化并处理分页。
3. 用 `citation-management` 验证导出条目并修复不完整元数据
4. 用 `citation-management` 按目标 venue 格式化
5. 可选用 `pyzotero` 把修正后的字段写回，让库也受益于这些修复

```bash
# 1-2. Export the desired collection from Zotero as BibTeX (pyzotero skill)
#      Follow the pyzotero export workflow: collect all pages, serialize the
#      returned bibtexparser object, and verify the exported item count.

# 3. Validate the exported bibliography
python scripts/validate_citations.py zotero_export.bib --report zotero_validation.json

# 4. Normalise the export (venue style comes from the .bst at build time)
python scripts/format_bibtex.py zotero_export.bib \
  --output formatted_refs.bib
```

Zotero 导出的质量取决于当初收录的质量：浏览器连接器收录的条目尤其常见缺 DOI、作者列表被截断，或仍是预印本元数据而论文后来已正式发表。投稿前先跑验证步骤，不要直接信任导出；并优先把修正写回 Zotero，同样的错误就不会在下篇稿件里重现。

pyzotero 导出的返回类型与分页：[官方文档](https://pyzotero.readthedocs.io/en/latest/)。Zotero 交接流程仅作示例；本次刷新未测试需要认证的库导出。
