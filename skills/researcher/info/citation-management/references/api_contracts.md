> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/citation-management/references/api_contracts.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 引文 API 契约

2026-09-30 对照官方文档审阅。随附客户端只使用只读请求；本 Skill 不涉及注册、账户变更或全文批量抓取。

| 服务 | 请求与认证 | 响应与分页 |
|---|---|---|
| OpenAlex | `GET https://api.openalex.org/works`；`search`，可选 `filter` 与 `sort=cited_by_count:desc`；可选来自 `OPENALEX_API_KEY` 的 `Authorization: Bearer`。支持无密钥的日常使用。`mailto` 是联系标识，不是配额升级。 | `results[]` 与 `meta.next_cursor`。以 `cursor=*` 起始，跟随返回的 cursor；支持的 `per_page` 最大值为 100（也接受 `per-page`）。到达请求上限或终止 cursor 时停止。任何一页失败都会中止导出。 |
| PubMed 检索 | `GET https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi`；`db=pubmed`、`term`、`retmax`、`retmode=json`、`tool`，可选 `email` 与 `api_key`。 | `esearchresult.count` 与 `idlist`。只能访问前 10,000 条匹配结果；`retstart` 无法突破这一上限。随附命令会限制请求量并报告该上限。 |
| PubMed 记录 | `GET .../efetch.fcgi`；`db=pubmed`、逗号分隔的 `id`、`retmode=xml`，以及相同的调用方参数。 | `PubmedArticleSet/PubmedArticle`；客户端每批处理 200 个 ID，并核实所有请求到的 ID 都被解析。PubmedBookArticle 未实现，会产生明确的检索不完整失败。 |
| PMC 转换 | `GET https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/`；`ids`、`format=json`、`tool`，可选 `email`。此处不发送 NCBI API key。 | `records[]` 仅为 PMC 收录的文章映射 PMID/PMCID/DOI。`pmid` 可以是数字形式。该辅助工具一次发送一个 ID；该服务每次请求接受 200 个同类型 ID，不分页。ID 转换器与已下线的 OA 下载服务仍是两个不同的东西。 |
| Crossref | `GET https://api.crossref.org/works/{encoded-doi}`；公开元数据不需要 key。 | 单例 JSON `message`；author/title/container/date 字段可能不完整。提取出版日期，而不是 `created`、`deposited` 或 `indexed`。无分页。公开的单条记录上限为 5/s；列表请求为 1/s。礼貌池的对应额度为 10/s 与 3/s；请遵守响应头。 |
| DataCite | `GET https://api.datacite.org/dois/{encoded-doi}`；公开可检索的记录不需要凭据。 | 单例 `data.id` 与 `data.attributes`，不是 Crossref 的 schema。DOI 校验器在 Crossref 返回 404 之后使用它。通用元数据提取器目前没有 DataCite 映射；请改用 DOI 转 BibTeX。 |
| DOI 内容协商 | `GET https://doi.org/{encoded-doi}`，带 `Accept: application/x-bibtex`；重定向会被跟随到注册机构。无需 key。 | 一条 BibTeX 记录；转换器拒绝非 BibTeX 响应，并生成它共享的引文键。无分页。支持 Crossref 之外的参与机构。 |
| DOI 解析器验证 | 同一个 DOI URL，在 Crossref 与 DataCite 都查无记录之后，以 GET 方式发起且不跟随重定向。 | 带 Location 的重定向确认已注册；404 表示 DOI 不存在。超时、限流、响应格式错误或其他状态仍属无法定论的警告，绝不构成一次成功的验证。出版商的可访问性与书目身份仍需人工复核。 |
| arXiv | `GET https://export.arxiv.org/api/query`；`id_list`、`max_results=1`；无需 key。所有 worker 合计最多每三秒一个请求，单连接。 | Atom feed，可选带 DOI/期刊参考。拒绝 API 错误条目；保留请求指定的 `vN` 版本。单 ID 查询不分页。仅有 DOI 并不能证明已在期刊发表。 |

PubMed 的 ESummary（`esummary.fcgi`，`retmode=json`）返回 `result.uids` 与以 UID 为键的记录。ELink（`elink.fcgi`，`cmd=neighbor`）返回链接集合；`pubmed_pmc` 要求目标 `db=pmc`，而 PubMed 内的相关/被引链接使用 `db=pubmed`。EInfo（`einfo.fcgi`）描述数据库字段与链接。PubMed 参考文档中的这些手工替代方案仅作示例，不被随附客户端使用。NCBI E-utilities 的限制是无 key 时 3 请求/s、有 key 时 10/s；请考虑到共享同一 IP/key 的其他进程。

Google Scholar 没有受支持的批量 API。`scholarly.search_pubs` 是带 `year_low`/`year_high` 的非官方迭代器；`--sort-by citations` 只对返回的样本排序。Google 把每个查询的显示结果上限设为 1,000 条。请遵守 robots.txt，遇到封锁就停止。代理支持是可选的，且未经验证。

## 验证证据与限制

2026-09-30 的无凭据只读冒烟检查返回 HTTP 200 与预期的解析结构：PMC 转换（PMC7611378 返回数字型 PMID 27102758）、ESearch/EFetch（PMID 34265844）、Crossref 与 DOI BibTeX 内容协商（10.1038/s41586-021-03819-2）、DataCite（10.14454/qdd3-ps68）、arXiv（1706.03762 返回 v7 的 Atom 条目）、OpenAlex（一条作品加一个 cursor）。这些检查只确认了当时的那些响应，既不证明可用性，也不证明批量覆盖能力。

回归测试模拟了分页失败、PubMed 批次缺失、arXiv 错误 feed/限速、DOI 传输失败、数字型 PMC ID 以及 CLI 输入契约。带认证的配额处理、Scholar/代理、任意出版商页面元数据、Zotero 导出以及所有示例性检索查询都未做线上实测。

## 官方来源

- [OpenAlex 认证](https://help.openalex.org/api/authentication/)、[分页](https://help.openalex.org/api/paging/) 与[检索](https://help.openalex.org/api/searching/)。
- [NCBI E-utilities 参考](https://www.ncbi.nlm.nih.gov/books/NBK25499/)、[NLM API 参数指南](https://www.nlm.nih.gov/dataguide/eutilities/utilities.html) 与 [PubMed 结果窗口变更](https://ncbiinsights.ncbi.nlm.nih.gov/2021/10/05/updated-pubmed-api/)。
- [PMC ID Converter API](https://pmc.ncbi.nlm.nih.gov/tools/id-converter-api/)。
- [Crossref REST API](https://github.com/CrossRef/rest-api-doc)、[当前的限流区分](https://community.crossref.org/t/refining-rest-api-limits-for-improved-stability-and-reliability/16137) 与[内容协商](https://www.crossref.org/documentation/retrieve-metadata/content-negotiation/)。
- [DataCite 公开 API](https://support.datacite.org/docs/rest-api) 与[单例 schema](https://support.datacite.org/docs/api-get-doi)。
- [arXiv API 手册](https://info.arxiv.org/help/api/user-manual.html) 与[使用限制](https://info.arxiv.org/help/api/tou.html)。
- [Google Scholar 帮助](https://scholar.google.com/intl/en/scholar/help.html) 与 [scholarly API](https://scholarly.readthedocs.io/en/stable/scholarly_user.html)。
- [Pyzotero 导出类型与分页](https://pyzotero.readthedocs.io/en/latest/)。
