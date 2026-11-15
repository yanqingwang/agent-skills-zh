> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/citation-management/references/metadata_extraction.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 元数据提取指南

通过各类 API 与服务，从 DOI、PMID、arXiv ID 和 URL 提取准确引文元数据的全面指南。

## 概述

准确的元数据是规范引文的基础。本指南覆盖：
- 识别论文标识符（DOI、PMID、arXiv ID）
- 查询元数据 API（CrossRef、PubMed、arXiv、DataCite）
- 各条目类型的必填 BibTeX 字段
- 处理边界情况与特殊情形
- 验证提取到的元数据

## 论文标识符

### DOI（数字对象标识符）

**格式**：`10.XXXX/suffix`

**示例**：
```
10.1038/s41586-021-03819-2    # Nature article
10.1126/science.aam9317       # Science article
10.1016/j.cell.2023.01.001    # Cell article
10.1371/journal.pone.0123456  # PLOS ONE article
```

**特性**：
- 永久标识符
- 元数据最可靠的来源
- 能解析到当前地址
- 由出版商分配

**在哪里找**：
- 论文首页
- 论文网页
- CrossRef、Google Scholar、PubMed
- 通常在出版商网站上很醒目

### PMID（PubMed ID）

**格式**：8 位数字（通常如此）

**示例**：
```
34265844
28445112
35476778
```

**特性**：
- 专属于 PubMed 数据库
- 仅限生物医学文献
- 由 NCBI 分配
- 永久标识符

**在哪里找**：
- PubMed 检索结果
- PubMed 上的论文页面
- 常出现在论文 PDF 页脚
- PMC（PubMed Central）页面

### PMCID（PubMed Central ID）

**格式**：PMC 后接数字

**示例**：
```
PMC8287551
PMC7456789
```

**特性**：
- PMC 中免费全文的论文
- PubMed 论文的子集
- 开放获取或作者手稿

### arXiv ID

**格式**：YYMM.NNNNN 或 archive/YYMMNNN

**示例**：
```
2103.14030        # New format (since 2007)
2401.12345        # 2024 submission
arXiv:hep-th/9901001  # Old format
```

**特性**：
- 预印本（未经同行评审）
- 物理、数学、计算机、q-bio 等
- 有版本追踪（v1、v2 等）
- 免费、开放获取

**在哪里找**：
- arXiv.org
- 常在正式发表前被引用
- 论文 PDF 页眉

### 其他标识符

**ISBN**（书籍）：
```
978-0-12-345678-9
0-123-45678-9
```

**arXiv 分类**：
```
cs.LG    # Computer Science - Machine Learning
q-bio.QM # Quantitative Biology - Quantitative Methods
math.ST  # Mathematics - Statistics
```

## 元数据 API

### CrossRef API

**DOI 的首选来源**：期刊论文元数据最全面。

**Base URL**：`https://api.crossref.org/works/`

**无需 API key**。用 `User-Agent` 标明你的应用；把自己的联系邮箱作为 `mailto` 传入，进入 polite pool。单条记录请求限速：公共池 5 次/秒，polite pool 10 次/秒；列表查询分别为 1 次/秒与 3 次/秒。留意响应中的限速/并发响应头，收到 429 就退避。最新限速见 [Crossref 限速说明](https://community.crossref.org/t/refining-rest-api-limits-for-improved-stability-and-reliability/16137)。

#### 基本 DOI 查询

**请求**：
```
GET https://api.crossref.org/works/10.1038/s41586-021-03819-2
```

**响应**（简化）：
```json
{
  "message": {
    "DOI": "10.1038/s41586-021-03819-2",
    "title": ["Article title here"],
    "author": [
      {"given": "John", "family": "Smith"},
      {"given": "Jane", "family": "Doe"}
    ],
    "container-title": ["Nature"],
    "volume": "595",
    "issue": "7865",
    "page": "123-128",
    "published-print": {"date-parts": [[2021, 7, 1]]},
    "publisher": "Springer Nature",
    "type": "journal-article",
    "ISSN": ["0028-0836"]
  }
}
```

#### 可用字段

**标识/类型字段**：
- `DOI`: 数字对象标识符
- `title`: 论文标题（数组；可能缺失或为空）
- `type`: 内容类型（journal-article、book-chapter 等）

**通常存在**：
- `author`: 作者对象数组
- `container-title`: 期刊/书名
- `published-print`、`published-online`、`published` 或 `issued`: 出版日期（不要用注册/存档日期替代）
- `volume`、`issue`、`page`: 出版细节
- `publisher`: 出版商名称

**有时存在**：
- `abstract`: 论文摘要
- `subject`: 学科分类
- `ISSN`: 期刊 ISSN
- `ISBN`: 书籍 ISBN
- `reference`: 参考文献列表
- `is-referenced-by-count`: 被引次数

#### 内容类型

CrossRef `type` 字段的取值：
- `journal-article`: 期刊论文
- `book-chapter`: 书籍章节
- `book`: 书籍
- `proceedings-article`: 会议论文
- `posted-content`: 预印本
- `dataset`: 研究数据集
- `report`: 技术报告
- `dissertation`: 学位论文

### PubMed E-utilities API

**专为生物医学文献而设**：提供带 MeSH 主题词的编目元数据。

**Base URL**：`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`

**建议申请 API key**（免费）：
- 更高的限速额度
- 更好的性能

#### PMID 转元数据

**第 1 步：用 EFetch 获取完整记录**

```
GET https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?
  db=pubmed&
  id=34265844&
  retmode=xml&
  api_key=YOUR_KEY
```

**响应**：包含全面元数据的 XML

**第 2 步：解析 XML**

关键字段：
```xml
<PubmedArticle>
  <MedlineCitation>
    <PMID>34265844</PMID>
    <Article>
      <ArticleTitle>Title here</ArticleTitle>
      <AuthorList>
        <Author><LastName>Smith</LastName><ForeName>John</ForeName></Author>
      </AuthorList>
      <Journal>
        <Title>Nature</Title>
        <JournalIssue>
          <Volume>595</Volume>
          <Issue>7865</Issue>
          <PubDate><Year>2021</Year></PubDate>
        </JournalIssue>
      </Journal>
      <Pagination><MedlinePgn>123-128</MedlinePgn></Pagination>
      <Abstract><AbstractText>Abstract text here</AbstractText></Abstract>
    </Article>
  </MedlineCitation>
  <PubmedData>
    <ArticleIdList>
      <ArticleId IdType="doi">10.1038/s41586-021-03819-2</ArticleId>
      <ArticleId IdType="pmc">PMC8287551</ArticleId>
    </ArticleIdList>
  </PubmedData>
</PubmedArticle>
```

#### PubMed 特有字段

**MeSH 主题词**：受控词表
```xml
<MeshHeadingList>
  <MeshHeading>
    <DescriptorName UI="D003920">Diabetes Mellitus</DescriptorName>
  </MeshHeading>
</MeshHeadingList>
```

**出版物类型**：
```xml
<PublicationTypeList>
  <PublicationType UI="D016428">Journal Article</PublicationType>
  <PublicationType UI="D016449">Randomized Controlled Trial</PublicationType>
</PublicationTypeList>
```

**资助信息**：
```xml
<GrantList>
  <Grant>
    <GrantID>R01-123456</GrantID>
    <Agency>NIAID NIH HHS</Agency>
    <Country>United States</Country>
  </Grant>
</GrantList>
```

### arXiv API

**物理、数学、计算机、q-bio 领域的预印本**：免费、开放获取。

**Base URL**：`https://export.arxiv.org/api/query`

**无需 API key**

#### arXiv ID 转元数据

**请求**：
```
GET https://export.arxiv.org/api/query?id_list=1706.03762
```

**响应**：Atom XML

```xml
<!-- Illustrative response shape; namespaces are declared on the feed. -->
<entry>
  <id>http://arxiv.org/abs/1706.03762v7</id>
  <title>Attention Is All You Need</title>
  <author><name>Ashish Vaswani</name></author>
  <!-- Additional authors omitted in this schematic, never omit them in a citation. -->
  <published>2017-06-12T17:57:34Z</published>
  <summary>Abstract text...</summary>
  <category term="cs.CL" scheme="http://arxiv.org/schemas/atom"/>
</entry>
```

#### 关键字段

- `id`: arXiv URL
- `title`: 预印本标题
- `author`: 作者列表
- `published`: 首版日期
- `updated`: 最新版本日期
- `summary`: 摘要
- `arxiv:doi`: 可选 DOI；在称其为期刊版本之前，先核验其注册元数据
- `arxiv:journal_ref`: 已发表时的期刊引用信息
- `category`: arXiv 分类

#### 版本追踪

arXiv 会追踪版本：
- `v1`: 初次提交
- `v2`、`v3` 等：修订版

**务必检查**是否存在期刊版本：结合出版商元数据与 `arxiv:journal_ref` 判断。只有 DOI 不能证明经过同行评审。脚本会保留显式的 `vN` 标识符；不带版本号的请求返回当前版本。所有 worker 共用一条连接时，每 3 秒最多发一次请求。脚本在单个 extractor 实例内强制该间隔；即使传输层返回 HTTP 200，也会拒绝 Atom 错误条目。

### DataCite API

**研究数据集、软件和其他成果**：为非传统学术成果分配 DOI。

**Base URL**：`https://api.datacite.org/dois/`

**与 CrossRef 类似**，但面向数据集、软件、代码等。

**请求**：
```
GET https://api.datacite.org/dois/10.5281/zenodo.1234567
```

**响应**：位于 `data.attributes` 的 JSON:API 对象，包含 `titles`、`creators`、`publicationYear` 和 `types`；这不是 Crossref 的 `message` 模式。公开 GET 无需凭证，可取回 findable 状态的记录。DataCite 或 Crossref 里查不到记录，并不能证明 DOI 无效：其他注册机构也在注册 DOI。

`extract_metadata.py --doi` 目前只读 Crossref 记录。DataCite DOI 请用 `doi_to_bibtex.py`（DOI 内容协商）；Crossref 返回 404 后，`validate_citations.py` 也会检查 DataCite。参见 [DataCite 单条记录指南](https://support.datacite.org/docs/api-get-doi)。

### PMC ID 转换

`extract_metadata.py --pmcid PMC7611378` 使用 `GET https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/`，带 `ids`、`format=json`、`tool` 和可选的 `email`。它读取 `records[0].pmid`（可能是纯数字），随后走 PubMed；若没有 PMID，则尝试返回的 DOI。只有收录在 PMC 的文章才能完成映射。该服务每次调用最多接受 200 个同类型 ID，不分页；本 helper 每次只发一个 ID。

这个仍在运行的 [ID 转换器](https://pmc.ncbi.nlm.nih.gov/tools/id-converter-api/) 与已停用的 PMC OA Web Service 是两套服务。

## BibTeX 必填字段

### @article（期刊论文）

**必填**：
- `author`: 作者姓名
- `title`: 论文标题
- `journal`: 期刊名称
- `year`: 出版年份

**可选但推荐**：
- `volume`: 卷号
- `number`: 期号
- `pages`: 页码范围（如 123--145）
- `doi`: 数字对象标识符
- `url`: 无 DOI 时填 URL
- `month`: 出版月份

**示例**：
```bibtex
@article{Smith2024,
  author  = {Smith, John and Doe, Jane},
  title   = {Novel Approach to Protein Folding},
  journal = {Nature},
  year    = {2024},
  volume  = {625},
  number  = {8001},
  pages   = {123--145},
  doi     = {10.1038/nature12345}
}
```

### @book（书籍）

**必填**：
- `author` 或 `editor`: 作者或编者
- `title`: 书名
- `publisher`: 出版社名称
- `year`: 出版年份

**可选但推荐**：
- `edition`: 版次（非初版时）
- `address`: 出版地
- `isbn`: ISBN
- `url`: URL
- `series`: 丛书名称

**示例**：
```bibtex
@book{Kumar2021,
  author    = {Kumar, Vinay and Abbas, Abul K. and Aster, Jon C.},
  title     = {Robbins and Cotran Pathologic Basis of Disease},
  publisher = {Elsevier},
  year      = {2021},
  edition   = {10},
  isbn      = {978-0-323-53113-9}
}
```

### @inproceedings（会议论文）

**必填**：
- `author`: 作者姓名
- `title`: 论文标题
- `booktitle`: 会议/论文集名称
- `year`: 年份

**可选但推荐**：
- `pages`: 页码范围
- `organization`: 主办机构
- `publisher`: 出版商
- `address`: 会议地点
- `month`: 会议月份
- `doi`: 有则填 DOI

**示例**：
```bibtex
@inproceedings{Vaswani2017,
  author    = {Vaswani, Ashish and Shazeer, Noam and others},
  title     = {Attention is All You Need},
  booktitle = {Advances in Neural Information Processing Systems},
  year      = {2017},
  pages     = {5998--6008},
  volume    = {30}
}
```

### @incollection（书籍章节）

**必填**：
- `author`: 章节作者
- `title`: 章节标题
- `booktitle`: 书名
- `publisher`: 出版社名称
- `year`: 出版年份

**可选但推荐**：
- `editor`: 书籍编者
- `pages`: 章节页码范围
- `chapter`: 章节编号
- `edition`: 版次
- `address`: 出版地

**示例**：
```bibtex
@incollection{Brown2020,
  author    = {Brown, Peter O. and Botstein, David},
  title     = {Exploring the New World of the Genome with {DNA} Microarrays},
  booktitle = {DNA Microarrays: A Molecular Cloning Manual},
  editor    = {Eisen, Michael B. and Brown, Patrick O.},
  publisher = {Cold Spring Harbor Laboratory Press},
  year      = {2020},
  pages     = {1--45}
}
```

### @phdthesis（学位论文）

**必填**：
- `author`: 作者姓名
- `title`: 论文标题
- `school`: 授予机构
- `year`: 年份

**可选**：
- `type`: 类型（如 "PhD dissertation"）
- `address`: 机构所在地
- `month`: 月份
- `url`: URL

**示例**：
```bibtex
@phdthesis{Johnson2023,
  author = {Johnson, Mary L.},
  title  = {Novel Approaches to Cancer Immunotherapy},
  school = {Stanford University},
  year   = {2023},
  type   = {{PhD} dissertation}
}
```

### @misc（预印本、软件、数据集）

**必填**：
- `author`: 作者
- `title`: 标题
- `year`: 年份

**预印本另加**：
- `howpublished`: 仓库（如 "bioRxiv"）
- `doi`: 预印本 DOI
- `note`: 预印本 ID

**示例（预印本）**：
```bibtex
@misc{Zhang2024,
  author       = {Zhang, Yi and Chen, Li and Wang, Hui},
  title        = {Novel Therapeutic Targets in Alzheimer's Disease},
  year         = {2024},
  howpublished = {bioRxiv},
  doi          = {10.1101/2024.01.001},
  note         = {Preprint}
}
```

**示例（软件）**：
```bibtex
@misc{AlphaFold2021,
  author       = {DeepMind},
  title        = {{AlphaFold} Protein Structure Database},
  year         = {2021},
  howpublished = {Software},
  url          = {https://alphafold.ebi.ac.uk/},
  doi          = {10.5281/zenodo.5123456}
}
```

## 提取工作流

### 从 DOI 提取

**最佳实践**，最可靠的来源：

```bash
# Single DOI
python scripts/extract_metadata.py --doi 10.1038/s41586-021-03819-2

# Multiple DOIs
python scripts/extract_metadata.py \
  --doi 10.1038/nature12345 \
  --doi 10.1126/science.abc1234 \
  --output refs.bib
```

**流程**：
1. 用 DOI 查询 CrossRef API
2. 解析 JSON 响应
3. 提取必填字段
4. 确定条目类型（@article、@book 等）
5. 格式化为 BibTeX
6. 校验完整性

### 从 PMID 提取

**用于生物医学文献**：

```bash
# Single PMID
python scripts/extract_metadata.py --pmid 34265844

# Multiple PMIDs
python scripts/extract_metadata.py \
  --pmid 34265844 \
  --pmid 28445112 \
  --output refs.bib
```

**流程**：
1. 用 PMID 查询 PubMed EFetch
2. 解析 XML 响应
3. 提取引文字段（随库附带的 extractor 不保留 MeSH 主题词）
4. 检查响应中是否有 DOI
5. 若有 DOI，可再查 CrossRef 补充元数据
6. 格式化为 BibTeX

### 从 arXiv ID 提取

**用于预印本**：

```bash
python scripts/extract_metadata.py --arxiv 2103.14030
```

**流程**：
1. 用 ID 查询 arXiv API
2. 解析 Atom XML 响应
3. 检查期刊引用信息和 DOI，判断是否已有正式发表版本
4. 若确认已发表：用 DOI 重新显式提取出版商元数据
5. 若未发表：使用预印本元数据
6. 格式化为 @misc 并加预印本说明

**重要**：务必检查预印本是否已正式发表！

### 从 URL 提取

**手上只有 URL 时**：

```bash
python scripts/extract_metadata.py \
  --url "https://www.nature.com/articles/s41586-021-03819-2"
```

**流程**：
1. 解析 URL，提取标识符
2. 判断类型（DOI、PMID、arXiv）
3. 从 URL 中提取标识符
4. 查询相应的 API
5. 格式化为 BibTeX

**URL 模式**：
```
# DOI URLs
https://doi.org/10.1038/nature12345
https://dx.doi.org/10.1126/science.abc123
https://www.nature.com/articles/s41586-021-03819-2

# PubMed URLs
https://pubmed.ncbi.nlm.nih.gov/34265844/
https://www.ncbi.nlm.nih.gov/pubmed/34265844

# arXiv URLs
https://arxiv.org/abs/2103.14030
https://arxiv.org/pdf/2103.14030.pdf
```

### 批量处理

**从含混合标识符的文件提取**：

```bash
# Create file with one identifier per line
# identifiers.txt:
#   10.1038/nature12345
#   34265844
#   2103.14030
#   https://doi.org/10.1126/science.abc123

python scripts/extract_metadata.py \
  --input identifiers.txt \
  --output references.bib
```

**流程**：
- 脚本自动识别标识符类型
- 查询相应的 API
- 合并到单个 BibTeX 文件
- 妥善处理错误

## 特殊情形与边界情况

### 预印本后正式发表

**问题**：引的是预印本，但现在已有期刊版本。

**解决**：
1. 检查 arXiv 元数据中的 DOI 字段
2. 替换预印本前，先核实该 DOI 指向已发表版本
3. 把引文更新为期刊论文
4. 需要时在注释中记下预印本版本

**示例**：
```bibtex
% Example publisher citation; do not infer an arXiv-to-DOI mapping from this template.
% Published as:
@article{Jumper2021,
  author  = {Jumper, John and Evans, Richard and others},
  title   = {Highly Accurate Protein Structure Prediction with {AlphaFold}},
  journal = {Nature},
  year    = {2021},
  volume  = {596},
  pages   = {583--589},
  doi     = {10.1038/s41586-021-03819-2}
}
```

### 多作者（et al.）

**问题**：作者很多（10 人及以上）。

**BibTeX 做法**：
- 保留核实过的来源给出的完整作者列表。
- 显示名的截断交给参考文献样式处理；只有来源或样式要求时才用 `and others`。

**示例**：
```bibtex
@article{LargeCollaboration2024,
  author = {First, Author and Second, Author and Third, Author and others},
  ...
}
```

### 作者姓名变体

**问题**：同一作者以不同姓名格式发表。

**统一格式**：
```
# Common variations
John Smith
John A. Smith
John Andrew Smith
J. A. Smith
Smith, J.
Smith, J. A.

# BibTeX format (recommended)
author = {Smith, John A.}
```

**提取时的取舍**：
1. 有全名就用全名
2. 有中间名缩写就带上
3. 格式：Last, First Middle

### 无 DOI 可用

**问题**：较老的论文或书籍没有 DOI。

**解决**：
1. 有 PMID 就用（生物医学）
2. 书籍用 ISBN
3. 用指向稳定来源的 URL
4. 写全出版信息

**示例**：
```bibtex
@article{OldPaper1995,
  author  = {Author, Name},
  title   = {Title Here},
  journal = {Journal Name},
  year    = {1995},
  volume  = {123},
  pages   = {45--67},
  url     = {https://stable-url-here},
  note    = {PMID: 12345678}
}
```

### 会议论文与期刊论文

**问题**：同一成果同时有会议版和期刊版。

**最佳实践**：
- 两者都有时引期刊版本
- 期刊版本是存档版本
- 会议版本胜在时效

**引会议版时**：
```bibtex
@inproceedings{Smith2024conf,
  author    = {Smith, John},
  title     = {Title},
  booktitle = {Proceedings of NeurIPS 2024},
  year      = {2024}
}
```

**引期刊版时**：
```bibtex
@article{Smith2024journal,
  author  = {Smith, John},
  title   = {Title},
  journal = {Journal of Machine Learning Research},
  year    = {2024}
}
```

### 书籍章节与编辑文集

**正确提取**：
- 章节：用 `@incollection`
- 整本书：用 `@book`
- 书籍编者：列入 `editor` 字段
- 章节作者：列入 `author` 字段

### 数据集与软件

**用 @misc**，字段填适当内容：

```bibtex
@misc{DatasetName2024,
  author       = {Author, Name},
  title        = {Dataset Title},
  year         = {2024},
  howpublished = {Zenodo},
  doi          = {10.5281/zenodo.123456},
  note         = {Version 1.2}
}
```

## 提取后验证

提取的元数据务必验证：

```bash
python scripts/validate_citations.py extracted_refs.bib
```

**检查**：
- 所有必填字段齐全
- DOI 能正确解析
- 作者姓名格式一致
- 年份合理（4 位数字）
- 期刊/出版商名称正确
- 页码范围用 -- 而非 -
- 特殊字符处理得当

## 最佳实践

### 1. 有 DOI 就优先用 DOI

DOI 能提供：
- 永久标识符
- 最好的元数据来源
- 出版商核实过的信息
- 可解析的链接

### 2. 验证自动提取的元数据

抽查：
- 作者姓名与出版物一致
- 标题一致（含大小写）
- 年份正确
- 期刊名完整

### 3. 处理特殊字符

**LaTeX 特殊字符**：
- 保护大小写：`{AlphaFold}`
- 处理重音：`M{\"u}ller` 或用 Unicode
- 化学式：`H$_2$O` 或 `\ce{H2O}`

### 4. 引用键保持一致

**约定**：`FirstAuthorYEARkeyword`
```
Smith2024protein
Doe2023machine
Johnson2024cancer
```

### 5. 现代论文包含 DOI

已分配 DOI 就要包含；出版年份新不代表一定有 DOI：
```bibtex
doi = {10.1038/nature12345}
```

### 6. 注明来源

非标准来源要加 note：
```bibtex
note = {Preprint, not peer-reviewed}
note = {Technical report}
note = {Dataset accompanying [citation]}
```

## 总结

元数据提取工作流：

1. **识别**：判断标识符类型（DOI、PMID、arXiv、URL）
2. **查询**：用相应的 API（CrossRef、PubMed、arXiv）
3. **提取**：从响应中解析必填字段
4. **格式化**：生成格式规范的 BibTeX 条目
5. **验证**：检查完整性与准确性
6. **核对**：抽查关键引文

**用脚本**自动化：
- `extract_metadata.py`: 通用提取器
- `doi_to_bibtex.py`: 快速 DOI 转换
- `validate_citations.py`: 校验准确性

提交最终结果前，**务必验证**提取到的元数据！
