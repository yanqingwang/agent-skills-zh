> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/literature-review/references/search_and_citation.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 检索、引文追溯与来源核验

当前的请求语法、认证方式、响应结构与分页限制请见
[database_strategies.md](database_strategies.md)。下文命令是示意性的发现操作，
不是真实执行过的检索，也不是完整的语料库。

## 补充性网络检索

Parallel CLI 0.9.3 支持下列参数。用 `parallel-cli auth` 或 `PARALLEL_API_KEY` 完成认证；
安装与认证方式见[官方 CLI 指南](https://docs.parallel.ai/integrations/cli)。
它对综述工作流而言是可选的，并且可能产生服务方费用。

```bash
mkdir -p sources
parallel-cli search "CRISPR sickle cell clinical studies" \
  -q 'CRISPR sickle cell clinical trial' --json --max-results 10 \
  --excerpt-max-chars-total 27000 \
  --include-domains 'pubmed.ncbi.nlm.nih.gov,biorxiv.org,medrxiv.org' \
  -o sources/scoping-web.json

parallel-cli extract 'https://arxiv.org/abs/1706.03762' \
  --full-content --json -o sources/paper-extract.json
```

`--max-results` 限制的是排序后返回的命中条数，不是数据库的总量。
`--full-content` 请求更完整的抽取；内容不可获取或被截断时，
仍须回到原始来源获取。请保存 URL、抽取状态、日期，以及支撑每一项推断的确切原文。
绝不要把标题、网络摘要或机器生成的摘要当作已评估过全文来报告。

## 引文追溯

- **向前追溯**：使用 Google Scholar 的 Cited by，或有文档说明的 Semantic Scholar /
  OpenAlex 引用检索。"papers citing ..." 这类搜索引擎检索式只是补充线索，
  不是完整的前向引用导出。
- **向后追溯**：查看合格报告及相关综述的参考文献表；
  获取候选记录后套用同一套纳入标准。
- 记录种子论文、使用的工具、日期、获取到的条数与筛选决策。
  在综合之前，把预印本、期刊论文、方案（protocol）与后续报告关联到同一个研究 ID。
  被引次数阈值与期刊声望都不是纳入规则；近期研究与阴性结果必须获得同等的纳入机会。

## DOI 检查与书目身份

```bash
python scripts/verify_citations.py review.md --output review_citation_report.json
```

可选的 `--email` 提供真实联系方式，以进入 Crossref 的礼貌池。
该辅助脚本提取去重后的 DOI 候选，做 URL 编码后检查
`GET https://doi.org/api/handles/{doi}`。判定注册成立需要 Handle 返回
`responseCode=1` 且标识符匹配，仅凭 HTTP 200 并不能说明问题。接着脚本会请求
`GET https://api.crossref.org/works/{doi}` 并检查元数据同一性。
这些公开的单例读取不需要密钥，也没有分页。

请把报告中的 `verified` 读作**注册已确认**，`failed` 读作**未能解析/缺失/无法定论**，
`metadata_unavailable` 读作**需要人工跟进补齐元数据**。瞬时错误与限流并不能证明存在捏造。
Crossref 并未覆盖所有注册机构。该脚本会保留原始的 Crossref message 与完整作者列表；
它提供的兼容性格式化方法只是预览，并非符合 APA 或 Nature 规范的输出。

DOI 提取采用启发式方法：请检查含义模糊的行尾标点，以及带括号的较老后缀。
没有 DOI 的引用需要人工核验。请核查标题、作者、年份、版本、更正/撤稿通知，
并确认来源确实支持所引用的论断。已注册标识符和可访问的 URL 并不能证明这些性质。

来源：[Handle proxy API](https://www.handle.net/proxy_servlet.html)、
[Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)。

## 参考文献的排版

请在 BibTeX/CSL JSON 中提供完整元数据，并使用当前版本、与目标出版方相适配的 CSL
文件。参见 [citation_styles.md](citation_styles.md)。使用 Pandoc 时，按
`[@citation_key]` 的形式引用；手工键入的参考文献串不会因为选了样式而被重新排版。

```bash
# Requires your populated review.bib and local styles/apa.csl.
python scripts/generate_pdf.py review.md --bibliography review.bib \
  --csl styles/apa.csl --output review.pdf
```

仓库内未捆绑 CSL 文件，也不会自动下载。同目录下的 `.bib` 会被识别；
否则请提供 `--bibliography` 或 Pandoc 的参考文献元数据。
省略 `--csl` 会使用 Pandoc 的默认引用样式。`--citation-style` 仍然是本地文件/名称的别名
（例如 `apa` 需要 `apa.csl`）。

请检查渲染出的 PDF 以及所有警告信息，包括未能解析的键。把正文引用与参考文献库一一对应，
并对照目标期刊的投稿说明人工核验排版。
[Pandoc 引文文档](https://pandoc.org/MANUAL.html#citations)。
