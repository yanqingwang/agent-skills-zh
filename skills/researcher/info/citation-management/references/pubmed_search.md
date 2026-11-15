> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/citation-management/references/pubmed_search.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# PubMed 检索指南

在 PubMed 中检索生物医学与生命科学文献的综合指南，涵盖 MeSH 主题词、字段标识、高级检索策略以及 E-utilities API 的用法。

## 概述

PubMed 是生物医学文献领域的首要数据库：
- **覆盖范围**：生物医学引文，包括 MEDLINE 记录和在线图书
- **学科范围**：生物医学与生命科学
- **来源**：MEDLINE、生命科学期刊、在线图书
- **权威性**：由美国国家医学图书馆（NLM）/ NCBI 维护
- **访问**：免费，无需注册账号
- **更新**：每日加入新引文
- **策展**：元数据质量高，有 MeSH 标引

## 基础检索

### 简单关键词检索

PubMed 会自动把检索词映射到 MeSH，并在多个字段中搜索：

```
diabetes
CRISPR gene editing
Alzheimer's disease treatment
cancer immunotherapy
```

**自动功能**：
- 自动 MeSH 映射
- 单复数变体
- 缩写展开
- 拼写检查

### 精确短语检索

用引号检索精确短语：

```
"CRISPR-Cas9"
"systematic review"
"randomized controlled trial"
"machine learning"
```

## MeSH（医学主题词表）

### 什么是 MeSH？

MeSH 是用于标引生物医学文献的受控叙词表：
- **层级结构**：按树状结构组织
- **标引一致**：同一概念始终用同一个主题词标引
- **覆盖全面**：涵盖疾病、药物、解剖结构、技术方法等
- **标引机制**：NLM 通过自动标引和人工策展分配 MeSH；较新记录和非 MEDLINE 记录可能没有 MeSH

### 查找 MeSH 主题词

**MeSH 浏览器**：https://meshb.nlm.nih.gov/search

**示例**：
```
Search: "heart attack"
MeSH term: "Myocardial Infarction"
```

**在 PubMed 中**：
1. 用关键词检索
2. 打开一篇相关文献的记录，若带有 MeSH 主题词则查看
3. 在 MeSH 浏览器中确认叙词
4. 将叙词与标题/摘要中的同义词组合使用

### 在检索中使用 MeSH

**基础 MeSH 检索**：
```
"Diabetes Mellitus"[MeSH]
"CRISPR-Cas Systems"[MeSH]
"Alzheimer Disease"[MeSH]
"Neoplasms"[MeSH]
```

**带副主题词的 MeSH 检索**：
```
"Diabetes Mellitus/drug therapy"[MeSH]
"Neoplasms/genetics"[MeSH]
"Heart Failure/prevention and control"[MeSH]
```

**常用副主题词**：
- `/drug therapy`：药物治疗
- `/diagnosis`：诊断方面
- `/genetics`：遗传方面
- `/epidemiology`：发生与分布
- `/prevention and control`：预防措施
- `/etiology`：病因
- `/surgery`：外科治疗
- `/metabolism`：代谢方面

### MeSH 扩展（Explosion）

默认情况下，MeSH 检索会包含更下位的主题词（即 explosion 扩展）：

```
"Neoplasms"[MeSH]
# Includes: Breast Neoplasms, Lung Neoplasms, etc.
```

**关闭扩展**（只检索该主题词本身）：
```
"Neoplasms"[MeSH:NoExp]
```

### MeSH 主要主题词

只检索该 MeSH 主题词作为主要焦点的文献：

```
"Diabetes Mellitus"[MeSH Major Topic]
# Only papers where diabetes is main topic
```

## 字段标识

字段标识指定在记录的哪个部分中检索。

### 常用字段标识

**标题与摘要**：
```
cancer[Title]                    # In title only
treatment[Title/Abstract]        # In title or abstract
"machine learning"[Title/Abstract]
```

**作者**：
```
"Smith J"[Author]
"Doudna JA"[Author]
"Collins FS"[Author]
```

**作者（全名）**：
```
"Smith, John"[Full Author Name]
```

**期刊**：
```
"Nature"[Journal]
"Science"[Journal]
"New England Journal of Medicine"[Journal]
"Nat Commun"[Journal]           # Abbreviated form
```

**出版日期**：
```
2023[Publication Date]
2020:2024[Publication Date]      # Date range
2023/01/01:2023/12/31[Publication Date]
```

**入库日期**：
```
2023[Date - Create]              # When added to PubMed
```

**文献类型**：
```
"Review"[Publication Type]
"Clinical Trial"[Publication Type]
"Meta-Analysis"[Publication Type]
"Randomized Controlled Trial"[Publication Type]
```

**语言**：
```
English[Language]
French[Language]
```

**DOI**：
```
10.1038/nature12345[DOI]
```

**PMID（PubMed ID）**：
```
12345678[PMID]
```

**文章 ID**：
```
PMC1234567[PMC]                  # PubMed Central ID
```

### 较少用但实用的标识

```
humans[MeSH Terms]               # Only human studies
animals[MeSH Terms]              # Only animal studies
"United States"[Place of Publication]
nih[Grant Number]                # NIH-funded research
"Female"[MeSH Terms]                    # Female subjects
"Aged, 80 and over"[MeSH Terms]        # Elderly subjects
```

## 布尔运算符

用布尔逻辑组合检索词。

### AND

两个检索词都必须出现（默认行为）：

```
diabetes AND treatment
"CRISPR-Cas9" AND "gene editing"
cancer AND immunotherapy AND "clinical trial"[Publication Type]
```

### OR

任一检索词出现即可：

```
"heart attack" OR "myocardial infarction"
diabetes OR "diabetes mellitus"
CRISPR OR Cas9 OR "gene editing"
```

**适用场景**：同义词及相关词

### NOT

排除检索词：

```
cancer NOT review
diabetes NOT animal
"machine learning" NOT "deep learning"
```

**注意**：可能把同时提到两个检索词的相关论文也排除掉。

### 组合运算符

用括号表达复杂逻辑：

```
(diabetes OR "diabetes mellitus") AND (treatment OR therapy)

("CRISPR" OR "gene editing") AND ("therapeutic" OR "therapy") 
  AND 2020:2024[Publication Date]

(cancer OR neoplasm) AND (immunotherapy OR "immune checkpoint inhibitor") 
  AND ("clinical trial"[Publication Type] OR "randomized controlled trial"[Publication Type])
```

## 高级检索构建器

**入口**：https://pubmed.ncbi.nlm.nih.gov/advanced/

**功能**：
- 可视化查询构建器
- 可添加多个查询框
- 从下拉菜单选择字段标识
- 用 AND/OR/NOT 组合
- 预览结果
- 显示最终查询字符串
- 保存查询

**操作流程**：
1. 在不同查询框中输入检索词
2. 选择字段标识
3. 选择布尔运算符
4. 预览结果
5. 按需调整
6. 复制最终查询字符串
7. 用于脚本或保存

**构建好的查询示例**：
```
#1: "Diabetes Mellitus, Type 2"[MeSH]
#2: "Metformin"[MeSH]
#3: "Clinical Trial"[Publication Type]
#4: 2020:2024[Publication Date]
#5: #1 AND #2 AND #3 AND #4
```

## 过滤器与限定条件

### 文献类型

```
"Review"[Publication Type]
"Systematic Review"[Publication Type]
"Meta-Analysis"[Publication Type]
"Clinical Trial"[Publication Type]
"Randomized Controlled Trial"[Publication Type]
"Case Reports"[Publication Type]
"Comparative Study"[Publication Type]
```

### 物种

```
humans[MeSH Terms]
mice[MeSH Terms]
rats[MeSH Terms]
```

### 性别

```
"Female"[MeSH Terms]
"Male"[MeSH Terms]
```

### 年龄组

```
"Infant"[MeSH Terms]
"Child"[MeSH Terms]
"Adolescent"[MeSH Terms]
"Adult"[MeSH Terms]
"Aged"[MeSH Terms]
"Aged, 80 and over"[MeSH Terms]
```

### 全文可得性

```
free full text[Filter]           # Free full-text available
```

### 期刊类别

```
"Journal Article"[Publication Type]
```

## E-utilities API

NCBI 通过 E-utilities（Entrez Programming Utilities）提供程序化访问。

### 概述

**基础 URL**：`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`

**主要工具**：
- **ESearch**：检索并返回 PMID
- **EFetch**：获取完整记录
- **ESummary**：获取文档摘要
- **ELink**：查找相关文献
- **EInfo**：数据库统计信息

**无需 API key**，但建议申请，理由如下：
- 更高的速率限制（10 次/秒 vs 3 次/秒）
- 更好的性能
- 标明你的项目身份

**获取 API key**：https://www.ncbi.nlm.nih.gov/account/

### ESearch - 检索 PubMed

为查询返回 PMID。10,000 上限是总查询窗口，不是能用 cursor/history 参数绕开的单页限制。更大的检索请拆分成互不重叠的日期区间并去重，或使用 NCBI EDirect。参见 [NCBI 的 PubMed 更新公告](https://ncbiinsights.ncbi.nlm.nih.gov/2021/10/05/updated-pubmed-api/)。

**端点**：`/esearch.fcgi`

**参数**：
- `db`：数据库（pubmed）
- `term`：检索查询
- `retmax`：最大结果数（默认 20，上限 10000）
- `retstart`：前 10,000 条匹配内的零起算偏移；`retstart + retmax` 不能超过 10,000
- `sort`：PubMed 取值包括 `relevance`、`pub_date`、`Author` 和 `JournalName`
- `api_key`：你的 API key（可选，建议提供）

**URL 示例**：
```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?
  db=pubmed&
  term=diabetes+AND+treatment&
  retmax=100&
  retmode=json&
  api_key=YOUR_API_KEY
```

**响应示例（两条记录的节选）**：
```json
{
  "esearchresult": {
    "count": "250000",
    "retmax": "100",
    "idlist": ["12345678", "12345679"]
  }
}
```

### EFetch - 获取记录

获取 PMID 对应的完整元数据。

**端点**：`/efetch.fcgi`

**参数**：
- `db`：数据库（pubmed）
- `id`：逗号分隔的 PMID
- `retmode=xml`：完整 PubMed XML（省略 `rettype`）；JSON 不是 PubMed EFetch 支持的格式
- `retmode=text&rettype=abstract` 或 `retmode=text&rettype=medline`：文本视图
- `api_key`：可选的 NCBI API key；`tool` 和 `email` 用于标识调用方

**URL 示例**：
```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?
  db=pubmed&
  id=12345678,12345679&
  retmode=xml&
  api_key=YOUR_API_KEY
```

**响应**：包含完整元数据的 XML，其中含：
- 标题
- 作者（含单位）
- 摘要
- 期刊
- 出版日期
- DOI
- PMID、PMCID
- MeSH 主题词
- 关键词

### ESummary - 获取摘要

比 EFetch 更轻量的替代方案。

**示例**：
```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?
  db=pubmed&
  id=12345678&
  retmode=json&
  api_key=YOUR_API_KEY
```

**返回**：JSON `result.uids` 以及以 PMID 为键的记录；这不是 ESearch 的 `esearchresult` 结构。该端点只是示例性的手动替代方案；随附的检索脚本只用 ESearch 和 EFetch。

### ELink - 查找相关文献

查找相关文献或通向其他数据库的链接。

**示例**：
```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?
  dbfrom=pubmed&
  db=pubmed&
  id=12345678&
  linkname=pubmed_pubmed_citedin&
  cmd=neighbor&
  retmode=xml
```

**链接类型**：
- `pubmed_pubmed`：相关文献
- `pubmed_pubmed_citedin`：引用本文的论文
- `pubmed_pmc`：PMC 全文版本（目标库设为 `db=pmc`）
- `pubmed_protein`：相关蛋白质记录

存在匹配链接时，ELink XML 中包含 `LinkSet/LinkSetDb/Link/Id`；空链接集也是合法结果。cited-in（被引）关系不是完整的引文索引。EInfo（`einfo.fcgi?db=pubmed&retmode=json`）报告的是数据库字段和链接名称，不是文献记录。以上均为示例性的手动 API 调用。

### 速率限制

**无 API key**：
- 每秒 3 个请求
- 超限会被封禁

**有 API key**：
- 每秒 10 个请求
- 更适合程序化访问

**最佳实践**：
```python
import time
time.sleep(0.34)  # ~3 requests/second
# or
time.sleep(0.11)  # ~10 requests/second with API key
```

### API key 的使用

**获取 API key**：
1. 注册 NCBI 账号：https://www.ncbi.nlm.nih.gov/account/
2. Settings → API Key Management
3. 创建新的 API key
4. 复制 key

**在请求中使用**：
```
&api_key=YOUR_API_KEY_HERE
```

**安全存储**：
```bash
# In environment variable
export NCBI_API_KEY="your_key_here"

# In script
import os
api_key = os.getenv('NCBI_API_KEY')
```

## 检索策略

### 全面系统性检索

用于系统综述和 Meta 分析：

```
# 1. Identify key concepts
Concept 1: Diabetes
Concept 2: Treatment
Concept 3: Outcomes

# 2. Find MeSH terms and synonyms
Concept 1: "Diabetes Mellitus"[MeSH] OR diabetes OR diabetic
Concept 2: "Drug Therapy"[MeSH] OR treatment OR therapy OR medication
Concept 3: "Treatment Outcome"[MeSH] OR outcome OR efficacy OR effectiveness

# 3. Combine with AND
("Diabetes Mellitus"[MeSH] OR diabetes OR diabetic) 
  AND ("Drug Therapy"[MeSH] OR treatment OR therapy OR medication)
  AND ("Treatment Outcome"[MeSH] OR outcome OR efficacy OR effectiveness)

# 4. Add filters
AND 2015:2024[Publication Date]
AND ("Clinical Trial"[Publication Type] OR "Randomized Controlled Trial"[Publication Type])
AND English[Language]
AND humans[MeSH Terms]
```

### 查找临床试验

```
# Specific disease + clinical trials
"Alzheimer Disease"[MeSH] 
  AND ("Clinical Trial"[Publication Type] 
       OR "Randomized Controlled Trial"[Publication Type])
  AND 2020:2024[Publication Date]

# Specific drug trials
"Metformin"[MeSH] 
  AND "Diabetes Mellitus, Type 2"[MeSH]
  AND "Randomized Controlled Trial"[Publication Type]
```

### 查找综述

```
# Systematic reviews on topic
"CRISPR-Cas Systems"[MeSH] 
  AND ("Systematic Review"[Publication Type] OR "Meta-Analysis"[Publication Type])

# Reviews in high-impact journals
cancer immunotherapy 
  AND "Review"[Publication Type]
  AND ("Nature"[Journal] OR "Science"[Journal] OR "Cell"[Journal])
```

### 查找最新论文

```
# Papers from last year
"machine learning"[Title/Abstract] 
  AND "drug discovery"[Title/Abstract]
  AND 2024[Publication Date]

# Recent papers in specific journal
"CRISPR"[Title/Abstract] 
  AND "Nature"[Journal]
  AND 2023:2024[Publication Date]
```

### 追踪作者

```
# Specific author's recent work
"Doudna JA"[Author] AND 2020:2024[Publication Date]

# Author + topic
"Church GM"[Author] AND "synthetic biology"[Title/Abstract]
```

### 高质量证据

```
# Meta-analyses and systematic reviews
(diabetes OR "diabetes mellitus") 
  AND (treatment OR therapy)
  AND ("Meta-Analysis"[Publication Type] OR "Systematic Review"[Publication Type])

# RCTs only
cancer immunotherapy 
  AND "Randomized Controlled Trial"[Publication Type]
  AND 2020:2024[Publication Date]
```

## 脚本集成

随附的客户端以 200 条一批的方式获取显式 PMID，逐批检查完整性，任何一批失败或含有不支持的 PubmedBookArticle 记录时拒绝导出。它不导出完整的 PubMed XML。

### search_pubmed.py 用法

**基础检索**：
```bash
python scripts/search_pubmed.py "diabetes treatment"
```

**带 MeSH 主题词**：
```bash
python scripts/search_pubmed.py \
  --query '"Diabetes Mellitus"[MeSH] AND "Drug Therapy"[MeSH]'
```

**日期范围过滤**：
```bash
python scripts/search_pubmed.py "CRISPR" \
  --date-start 2020-01-01 \
  --date-end 2024-12-31 \
  --limit 200
```

**文献类型过滤**：
```bash
python scripts/search_pubmed.py "cancer immunotherapy" \
  --publication-types "Clinical Trial,Randomized Controlled Trial" \
  --limit 100
```

**导出为 BibTeX**：
```bash
python scripts/search_pubmed.py "Alzheimer's disease" \
  --limit 100 \
  --format bibtex \
  --output alzheimers.bib
```

**从文件读取复杂查询**：
```bash
# Save complex query in query.txt
cat > query.txt << 'EOF'
("Diabetes Mellitus, Type 2"[MeSH] OR "diabetes"[Title/Abstract])
AND ("Metformin"[MeSH] OR "metformin"[Title/Abstract])
AND "Randomized Controlled Trial"[Publication Type]
AND 2015:2024[Publication Date]
AND English[Language]
EOF

# Run search
python scripts/search_pubmed.py --query-file query.txt --limit 500
```

### 批量检索

```bash
# Search multiple topics
TOPICS=("diabetes treatment" "cancer immunotherapy" "CRISPR gene editing")

for topic in "${TOPICS[@]}"; do
  python scripts/search_pubmed.py "$topic" \
    --limit 100 \
    --output "${topic// /_}.json"
  sleep 1
done
```

### 提取元数据

```bash
# Search returns PMIDs
python scripts/search_pubmed.py "topic" --output results.json

# Extract full metadata
python scripts/extract_metadata.py \
  --input results.json \
  --output references.bib
```

## 技巧与最佳实践

### 检索式构建

1. **从 MeSH 主题词入手**：
   - 用 MeSH 浏览器找到正确的主题词
   - 比关键词检索更精确
   - 与文本词组合使用：并非每条 PubMed 记录都有 MeSH 标引

2. **纳入文本词变体**：
   ```
   # Better coverage
   ("Diabetes Mellitus"[MeSH] OR diabetes OR diabetic)
   ```

3. **恰当使用字段标识**：
   - `[MeSH]` 用于标准化概念
   - `[Title/Abstract]` 用于特定词语
   - `[Author]` 用于已知作者
   - `[Journal]` 用于特定期刊

4. **逐步构建**：
   ```
   # Step 1: Basic search
   diabetes
   
   # Step 2: Add specificity
   "Diabetes Mellitus, Type 2"[MeSH]
   
   # Step 3: Add treatment
   "Diabetes Mellitus, Type 2"[MeSH] AND "Metformin"[MeSH]
   
   # Step 4: Add study type
   "Diabetes Mellitus, Type 2"[MeSH] AND "Metformin"[MeSH] 
     AND "Clinical Trial"[Publication Type]
   
   # Step 5: Add date range
   ... AND 2020:2024[Publication Date]
   ```

### 优化结果

1. **结果太多**：加过滤器
   - 限定文献类型
   - 收窄日期范围
   - 换用更具体的 MeSH 主题词
   - 使用主要主题词：`[MeSH Major Topic]`

2. **结果太少**：放宽检索
   - 移除限制性过滤器
   - 用 OR 连接同义词
   - 扩大日期范围
   - 使用 MeSH 扩展（默认开启）

3. **结果不相关**：改进检索词
   - 换用更具体的 MeSH 主题词
   - 用 NOT 排除
   - 改用 Title 字段而不是全字段
   - 加 MeSH 副主题词

### 质量控制

1. **记录检索策略**：
   - 保存准确的查询字符串
   - 记录检索日期
   - 记录结果数量
   - 保存所用过滤器

2. **系统性导出**：
   - 使用一致的文件命名
   - 导出为 JSON，便于后续处理
   - 按需转换为 BibTeX
   - 保留原始检索结果

3. **验证检索到的引文**：
   ```bash
   python scripts/validate_citations.py pubmed_results.bib
   ```

### 保持跟进

1. **设置检索提醒**：
   - 在 PubMed 中保存检索（Save search）
   - 接收邮件更新
   - 可选每日、每周或每月

2. **追踪特定期刊**：
   ```
   "Nature"[Journal] AND CRISPR[Title]
   ```

3. **关注关键作者**：
   ```
   "Church GM"[Author]
   ```

## 常见问题与解决方法

### 问题：找不到 MeSH 主题词

**解决方法**：
- 检查拼写
- 使用 MeSH 浏览器
- 尝试相关主题词
- 退而用文本词检索

### 问题：结果为零

**解决方法**：
- 移除过滤器
- 检查查询语法
- 用 OR 扩大检索
- 尝试同义词

### 问题：结果质量差

**解决方法**：
- 加文献类型过滤器
- 限定近年文献
- 使用 MeSH 主要主题词
- 按期刊质量过滤

### 问题：不同来源的重复记录

**解决方法**：
```bash
python scripts/format_bibtex.py results.bib \
  --deduplicate \
  --output clean.bib
```

### 问题：API 速率限制

**解决方法**：
- 申请 API key（上限提升到每秒 10 次）
- 在脚本中加入延时
- 分批处理
- 避开高峰时段

## 小结

PubMed 提供权威的生物医学文献检索：

✓ **策展内容**：MeSH 标引、质量控制  
✓ **精确检索**：字段标识、MeSH 主题词、过滤器  
✓ **程序化访问**：E-utilities API  
✓ **免费访问**：无需订阅  
✓ **覆盖全面**：3500 万+ 条引文，每日更新  

关键策略：
- 用 MeSH 主题词做精确检索
- 与文本词组合，获得全面覆盖
- 恰当使用字段标识
- 按文献类型和日期过滤
- 用 E-utilities API 实现自动化
- 记录检索策略，保证可复现

如需跨学科更广的覆盖，可配合 Google Scholar 使用。
