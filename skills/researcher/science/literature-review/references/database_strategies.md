> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/literature-review/references/database_strategies.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 文献数据库检索策略

审阅于 2026-09-30。本文件给出的是文献发现层面的约定，并不承诺检索的完整性。
请保存检索式、平台、日期/时间、日期字段的含义、筛选条件、原始页面、报告的总数、
导出的条数，以及任何失败情况。对于被截断或中断的检索，要在筛选之前先标记为不完整。

## 来源选择与检索式设计

1. 在看到结果之前先确定综述类型与纳入标准。干预类问题使用 PICO；
   其他问题可调整该框架。
2. 选择互补的文献数据库、相关注册库、预印本服务器与灰色文献来源。
   网络检索和生物实体数据库都不能替代某学科自己的文献索引。
3. 用 OR 构建同义词组，用 AND 组合概念。先在已知合格的论文上试跑。
   考虑结局筛选、语言限制、出版类型限制或 NOT 词是否会丢弃相关研究。
4. 把每条检索式翻译到对应平台。通配符与字段语法不可移植：不要把 PubMed 的 `[MeSH]`、
   arXiv 的 `ti:` 或搜索引擎运算符照搬到另一个 API。请记录实际翻译后的检索式，
   而不只是关键词。
5. 对系统综述，筛选时依据方案中的标准，不看出版方、作者声望、机构归属或被引次数。
   文献计量指标反映的是曝光度以及领域与年龄效应，而不是偏倚风险。

## PubMed 与 PMC

使用 [PubMed 界面](https://pubmed.ncbi.nlm.nih.gov/advanced/) 或 NCBI E-utilities。
`gget search` 检索的是 Ensembl，没有 PubMed/bioRxiv 模式。
PubMed 存放书目记录；PMC 是全文仓库，两者语料库部分重叠。
不要把"能取到摘要"等同于"能取到全文"。

以下是一个小规模的首屏请求，并非完整的综述检索：

```bash
mkdir -p sources
curl --fail-with-body --get 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi' \
  --data-urlencode 'db=pubmed' \
  --data-urlencode 'term=(CRISPR[Title/Abstract]) AND ("Anemia, Sickle Cell"[MeSH Terms])' \
  --data-urlencode 'retmode=json' --data-urlencode 'retmax=5' \
  --data-urlencode 'tool=literature_review' -o sources/pubmed-first-page.json
```

- ESearch 返回 `esearchresult.count`（常常是字符串）、`idlist`，以及查询
  翻译结果与警告信息。请检查这些内容；仅凭 HTTP 200 并不能确认成功。
- 用 `retstart`/`retmax` 分页只能在**前 10,000 条 PubMed 匹配结果以内**进行。
  更大的检索要拆分成有记录、可去重的子查询，或使用有文档说明的批量方法；
  History 服务器不能绕过这一限制。
- EFetch 形如 `GET .../efetch.fcgi?db=pubmed&id=PMID1,PMID2&retmode=xml`（ID 集合较大时用 POST）。
  解析 `PubmedArticleSet` XML，保留文章与图书记录，并核对请求的 ID 与返回的 ID。
- 小规模请求不需要密钥。持续使用时请提供真实的联系 `email` 与 `tool`；
  可选的 `api_key` 会把默认的每 IP 3 次/秒共享上限提升到每个密钥 10 次/秒。
  请考虑并发客户端的影响。
- 使用显式的 `[Publication Date]` 区间，并记录所选用的字段。
  诸如 `2020:2024[DP]` 这类历史示例并不意味着"当前年份"。

来源：[NLM 参数指南](https://www.nlm.nih.gov/dataguide/eutilities/utilities.html)、
[PubMed 10,000 条结果上限](https://ncbiinsights.ncbi.nlm.nih.gov/2021/10/05/updated-pubmed-api/)、
[NCBI 使用指南](https://eutilities.github.io/site/API_Key/usageandkey/)。

## bioRxiv 与 medRxiv

[官方 API](https://api.biorxiv.org/) 提供的是按日期/DOI 获取元数据，
而不是通用关键词检索端点。关键词发现请使用该服务的检索界面，
或对下载到的元数据显式过滤。

- `GET https://api.biorxiv.org/details/{server}/{from}/{to}/{cursor}/json`，其中
  server 取 `biorxiv` 或 `medrxiv`，日期字符串格式为 `YYYY-MM-DD`，cursor 从 0 开始，
  并可选用 `category=cell_biology`。
- 响应中的 `collection[]` 存放记录；`messages[]` 说明状态、计数、
  cursor 与总数。按日期区间调用的返回记录不超过 30 条；按实际收到的条数推进 cursor，
  保留所有版本，并核对总数与状态。
- 单个 DOI：`/details/{server}/{doi}/na/json`。请保留 DOI、`version`、`date`、
  摘要、许可与 `published` 关联。一份预印本与一份已发表的报告可能描述同一项研究，
  但它们是彼此独立的报告。
- `/pubs/{server}/{from}/{to}/{cursor}` 映射出版关联，每页最多 100 条。
  它的 schema 不同（`biorxiv_doi`、`published_doi`）。
- 公开读取不需要 API 密钥。请保守地顺序调用，遇到限流或报错即停止；
  不要把缺少出版关联当成预印本仍未发表的证据。

## arXiv

`GET https://export.arxiv.org/api/query` 接受 `search_query`、`id_list`、
`start`（从 0 开始）、`max_results`、`sortBy` 与 `sortOrder`。无需密钥。

```bash
curl --fail-with-body --get 'https://export.arxiv.org/api/query' \
  --data-urlencode 'search_query=cat:q-bio.QM AND ti:"single cell"' \
  --data-urlencode 'start=0' --data-urlencode 'max_results=5' \
  --data-urlencode 'sortBy=submittedDate' --data-urlencode 'sortOrder=descending' \
  -o sources/arxiv-first-page.xml
```

解析 Atom 命名空间、`opensearch:totalResults` 与条目 ID；错误条目也可能出现在 Atom feed 中。
请保留 `vN`、原始的 `published` 与 `updated` 日期。`ti:` 是标题字段，不是 `title:`。
请使用单个连接，请求间隔至少三秒。每页不要超过 2,000 条，也不要指望 offset 能给出
30,000 条以上的匹配；请拆分为多个查询或使用批量接口。这是预印本的发现手段，
不等于经过同行评议的证据。

来源：[arXiv API 手册](https://info.arxiv.org/help/api/user-manual.html)。

## Semantic Scholar

使用 [Graph API 约定](https://api.semanticscholar.org/api-docs/graph)
（以及可下载的 [schema](https://api.semanticscholar.org/graph/v1/swagger.json)）。

- 相关性检索：`GET https://api.semanticscholar.org/graph/v1/paper/search`；
  纯文本 `query`，单独的 `year=2020-2024`，可选的 `fields`、`offset`、
  `limit`（最大 100）。响应含 `data[]`、`total` 与可选的 `next`。
  只有 1,000 条按相关性排序的记录可取，不是一次穷尽式导出。
- 批量检索：`GET .../paper/search/bulk`；检索式使用其有文档说明的布尔语法
  （`+`、`|`、`-`、引号、括号），另有独立的筛选条件与
  `fields`。响应含 `data[]` 与续传用的 `token`；请原样把该 token 传给下一个请求。
  每次调用最多 1,000 条，总量上限为 1,000 万条。
  该端点不提供嵌套的引用/被引数据。
- 不要为相关性 API 编造 `title:`/`author:` 运算符。只有在查阅过各自约定之后，
  才好使用单独的作者或标题检索路由。
- API 密钥放在 `x-api-key` 头中；可用性与配额取决于端点与账户。
  匿名访问走的是共享且受限流的资源池。请遵守分配给你的配额，
  检查 HTTP 429 响应并退避重试；过去那个笼统的"5 分钟 100 次请求"已不是当前的服务承诺。
- 被引次数与"高影响力被引"标签只是发现辅助。论文身份、缺失字段、日期覆盖范围
  与原文内容都要自己核查。

## OpenAlex、Crossref 与补充检索

[OpenAlex 认证](https://help.openalex.org/api/authentication/)允许无密钥的日常读取；
免费密钥可提高每日额度。使用 `api_key` 或 `Authorization: Bearer`，但不要把密钥
写进检索日志。`GET https://api.openalex.org/works` 接受 `search`、`filter`、`select` 与 `sort`。
响应含 `results[]` 与 `meta`。当前 `per_page` 上限为 100；
从 `cursor=*` 开始，并原样跟随 `meta.next_cursor`。基于页码的基础检索止于 10,000 条。
请遵守请求额度与限流响应头；无密钥不等于无限量。参见[分页说明](https://help.openalex.org/api/paging/)。

Crossref 的 `GET https://api.crossref.org/works/{doi}` 是单例元数据查询，返回 JSON `message`，
不需要密钥，也没有分页。404 并不能证明来自其他注册机构的 DOI 是无效的。
列表检索（`/works?query...`）的配额与分页规则不同：公开列表为 1 次/秒，礼貌池为 3 次/秒，
而单条记录查询为 5 次/秒与 10 次/秒。请提供真实的 `mailto` 以获得礼貌池访问；
遵循[响应头说明](https://community.crossref.org/t/refining-rest-api-limits-for-improved-stability-and-reliability/16137)。

Google Scholar 的[界面](https://scholar.google.com/intl/en/scholar/help.html)
提供 Cited by、Related articles 与 Cite 导出，但没有受支持的批量 API。
请记录检索式与已筛选的范围；不要承诺按被引次数排序、无限结果，
也不要承诺从排序样本获得完整覆盖。遇到访问拦截即停止。
Dimensions 与授权索引需要的是你所在机构实际持有的访问权限；
免费网站层级并不意味着具备 API 使用权。

## 结果规范化与可复现性

`search_databases.py` **不会**查询或合并原始的提供方响应信封。请给它一份由规范化对象
组成的 JSON 数组，同时把原始导出分开保存：

```json
[
  {"title": "Example title", "authors": "Author, A. and Author, B.",
   "first_author": "Author", "year": 2026, "source": "PubMed",
   "doi": null, "url": "https://pubmed.ncbi.nlm.nih.gov/", "citations": null}
]
```

title/authors/source 用字符串，被引数用数字或 null；
BibTeX 的作者字段需要用 `and` 分隔。把提供方 ID、检索/运行 ID、
获取日期与来源溯源保留为额外字段。缺失不等于零。

```bash
python scripts/search_databases.py combined_results.json --deduplicate \
  --format json --output unique_results.json --summary
```

去重保留首个规范化后的 DOI；标题回退匹配只比较没有 DOI 的记录。
请人工复核标题匹配结果，并利用原始重复项补全信息；
该脚本不会挑选最完整的元数据，也不会把一项研究的全部报告关联起来。
年份未知的记录留给人工复核。排序只是给导入的样本排列次序。
最终的 BibTeX 键取自导出结果；同作者同年的键会加上后缀区分。
导出时间戳不等于原始检索日期。

请使用官方的 [PRISMA 指南](https://www.prisma-statement.org/prisma-2020)
与 [Cochrane 遴选指南](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04)，
使筛选决策与报告/研究的对应关系保持可审计。
