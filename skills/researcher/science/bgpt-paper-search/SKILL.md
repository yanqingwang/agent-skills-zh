---
name: bgpt-paper-search
description: 按主题或 DOI 检索 BGPT 科学论文，并获取从全文中提取的论断级证据，包括实验、报告的统计数据、适用范围、局限性与来源出处。适用于文献综述、证据综合，以及查找摘要之外的实验细节。
license: MIT
compatibility: Requires a configured remote BGPT MCP connection and internet access to bgpt.pro. A stdio bridge additionally needs Node.js/npm. Paid access requires a BGPT API key configured as an Authorization header.
metadata:
  version: "1.3"
  skill-author: BGPT
  website: https://bgpt.pro/mcp/
  last-reviewed: "2026-09-30"
---

> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/bgpt-paper-search/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# BGPT 论文检索

## 适用场景

使用 BGPT 为某个研究问题或已知的 DOI 查找源自全文的证据。它返回的是提取出的论断及其支撑实验，而不仅是书目元数据。用这些记录来构建可追溯的证据表；它们既不是完整的系统综述检索，也不是经过验证的偏倚风险评估。

## 连接

使用前请先在宿主中配置 BGPT；安装本 Skill 并不会注册 MCP 服务器。该服务方支持以下两种传输方式：

| 传输方式 | 端点 |
| --- | --- |
| Streamable HTTP | `https://bgpt.pro/mcp/stream` |
| SSE | `https://bgpt.pro/mcp/sse` |

在宿主支持时，优先使用其原生的远程 MCP 配置。对于使用 `mcpServers` JSON 且需要本地 stdio 桥接的宿主，以下配置使用 `mcp-remote`（请按宿主实际的配置格式调整）：

```json
{
  "mcpServers": {
    "bgpt": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://bgpt.pro/mcp/stream", "--transport", "http-only"]
    }
  }
}
```

已发布的 `bgpt-mcp` 1.1.0 npm 包只是对 `mcp-remote` 的一层轻量 SSE 封装，并非本地论文数据库。其随包附带的 README 早于当前的工具契约与定价。请优先采用上文的原生连接或可配置桥接。审查时链接的 BGPT GitHub 仓库无法访问；请参照[当前服务方文档](https://bgpt.pro/mcp/)与实时工具 schema。

免费访问无需密钥。付费使用时，请在宿主的远程服务器请求头中配置 `Authorization: Bearer <key>`，并使用其凭据存储。对于桥接方式，[`mcp-remote` 支持 `--header-file`](https://github.com/punkpeye/mcp-remote#custom-headers)，可配合本地凭据文件使用。不要在 MCP 工具调用中传入 `api_key`：当前两个工具都未声明该参数。请通过连接完成鉴权。

## 检索与 DOI 查询

调用前先查明已连接服务器所提供的工具。2026-09-30 审查的线上 BGPT 2.14.7 schema 暴露如下：

| 工具 / 参数 | 契约 |
| --- | --- |
| `search_papers.query` | 必填字符串。请使用简短的英文检索词。 |
| `num_results` | 整数，1–100；默认 16。请显式设置以控制结果用量。 |
| `days_back` | 可选整数；仅返回最近 N 天内发表的论文。省略则不限日期。 |
| `min_citations` | 可选整数；指**该论文引用的参考文献**数量的下限，而非论文被引用的次数。 |
| `study_type` | 可选字符串：`primary study`、`systematic review`、`meta-analysis`、`narrative review`、`protocol`、`dataset`、`commentary` 或 `other`。 |
| `output_format` | `evidence`（默认）、`full` 或 `legacy`。 |
| `lookup_paper.doi` | 必填 DOI 字符串；也接受 `output_format`。查到的论文计为一条结果。 |

请使用过滤参数，不要把年份或过滤条件写进检索词里。该 schema 未记载任何布尔检索语法、offset、page 或 cursor。结果上限并不等于分页：不要臆造续传参数，也不要声称检索会枚举出所有匹配的论文。若需更广的覆盖，可运行明确的问题变体，按 DOI 去重并保留检索历史。

已用一条公开结果验证的检索示例（通过已连接的工具接口调用）：

```json
{"query": "CRISPR human cells", "num_results": 1, "output_format": "full"}
```

示意性的带过滤检索（过滤条件仅经 schema 校验，未实际执行）：

```json
{"query": "CRISPR delivery neurons", "num_results": 5, "days_back": 90, "study_type": "primary study", "output_format": "evidence"}
```

对于已确定的论文，请直接用其纯 DOI 调用 `lookup_paper`，而不要指望按标题检索能返回那篇确切的论文：

```json
{"doi": "10.1016/j.ymeth.2015.10.014", "output_format": "evidence"}
```

不要把连接错误、配额错误或工具错误解读成证据集为空。服务方公布的是结果额度，审查页面上并未给出数值化的请求速率限制；不要假定请求吞吐不受限制。

## 理解结果契约

检索返回一个包含 `results` 列表和 `count` 的信封；也要记录返回的 `query`，因为服务可能会改写检索词。DOI 查询返回 `found` 和单条 `result`；读取前先处理未找到的情况。在解读信封之前，先检查 MCP 结果中是否有工具错误。

- `evidence` 返回精简的证据记录；空的可选字段可能不出现。
- `full` 在证据记录之外追加旧版论文元数据。
- `legacy` 请求旧版的论文元数据表示形式。不要假定每篇论文都具备此前宣传的所有字段或质量评分。

服务方称 evidence/full 格式会略去没有提取到证据的论文。但线上冒烟测试在两种格式下都返回了一条记录，其 `schema_version: "legacy"`、`extraction_status: "legacy"`，且 `evidence_units` 列表为空。因此，返回的记录并不能保证论断级的来源出处。空检索结果或未查到的 DOI 也不能证明该论文不存在。在可用时保留 `doi`、`title`、`publication_date` 和 `publication_name`，然后检查 `central_claim` 与 `evidence.evidence_units`。每个单元把其论断关联到某个实验、报告的统计数据、已证实的适用范围和来源出处。保留 schema 版本：较旧的记录可能有不同的结构。旧版 full 元数据可能包含 null 值、数字字符串和序列化文本，而非原生列表；请保留原始值，切勿把它们当作代码执行。

服务方记载的 V4 上限为：每条记录五个证据单元、每个单元两段来源出处段落、每段 320 字符。这些是有界的提取结果，并非完整文章。综合之前，请检查 `extraction_status`、`normalization_warnings` 和 `evidence.record_provenance`，包括截断信息。

## 证据核查

对每条提取结果，保留其 DOI 以及来源的章节、表格或图。在用于综合之前，对照论文核实样本量、单位、实验分组、报告的统计数据和不确定性。区分作者自述的局限性与提取过程产生的解读。保留相互矛盾或混杂的证据以及已证实的适用范围。若存在旧版质量评分，只把它当作筛查辅助，而非针对具体研究的偏倚风险评估。

## 额度与审查范围

在审查之日，服务方宣传每网络 50 条免费**结果**，超出后按每条返回的结果收取 $0.02。一次成功的 DOI 查询计为一条结果；未查到的查询不计费。大批量操作前请重新核对额度与定价。配额已耗尽时不要反复重试请求。

来源：[服务方配置、记录格式与计费](https://bgpt.pro/mcp/)、[线上 MCP 端点](https://bgpt.pro/mcp/stream)、[已发布的 BGPT 封装包元数据](https://registry.npmjs.org/bgpt-mcp/latest)，以及[桥接文档](https://github.com/punkpeye/mcp-remote)。工具 schema、单条结果的 full 检索、对应的 evidence 格式 DOI 查询，以及 SSE 握手，均通过未鉴权请求核验。公开检索/查询返回的是一条旧版 schema 记录，而非 V4 fixture。付费鉴权、带过滤的检索行为以及宿主专属配置均未测试。
