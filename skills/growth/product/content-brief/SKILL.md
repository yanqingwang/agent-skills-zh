---
name: content-brief
description: 面向目标关键词、由 SERP 驱动的内容简报：当前排名情况、该覆盖的内容、标题层级、要回答的问题，以及来自自有数据的内链。适用于被要求做"内容简报"、"为 X 列出排名大纲"、"这篇文章该覆盖什么"时，或在撰写任何 SEO 页面之前。
---

> **中文汉化版** · 上游：[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · 原文件：`skills/content-brief/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 内容简报

## 前置要求

免费的 Ryze MCP 连接器（`https://connector.get-ryze.ai/mcp`）。Claude Code：`claude mcp add ryze --transport http https://connector.get-ryze.ai/mcp`。claude.ai / Desktop / Cursor：用同一个 URL 把它添加为自定义连接器。配置说明：https://www.get-ryze.ai/how-to-connect-claude-to-google-meta-ads-mcp?utm_source=github&utm_content=open-seo-mcp-skills

一份以实时 SERP 加上站点自有数据为依据的简报，而非泛泛的大纲。

## 工作流

1. **SERP。** 若工作区提供了 DataForSEO SERP 工具，就拉取目标关键词的实时 Google 前 10 结果（用 `native__get_provider_docs`、provider 为 `dataforseo` 查看请求格式），取回标题、URL 与 SERP 特性（精选摘要、PAA、视频）。若没有这些工具，改用网页搜索抓取靠前的结果；无论哪种方式，简报都必须基于真实的 SERP 来构建。
2. **细读前 3 名。** 抓取并浏览排名靠前的页面：看它们的结构、深度、切入角度、都覆盖了什么（基本盘），以及都没覆盖什么（切入点）。
3. **关键词集合。** 以目标词为种子调用 `google_ads__generateKeywordIdeas`，得到值得纳入的次要关键词和问句变体，再用 `google_ads__generateKeywordHistoricalMetrics` 取搜索量。
4. **你已有的立足点。** 用 `google_search_console__runRawSearchAnalytics` 按主题过滤，找出站点已经有展现的查询（把它们写进标题），以及相近主题上的现有页面（作为内链来源；若某个页面已经覆盖了本主题的一半，还要标出来，应该扩充它而不是新建页面）。
5. **组装简报：**
   - 目标关键词 + 带搜索量的次要词
   - 搜索意图与所需形式（指南 / 列表 / 对比 / 工具页），依据实际排名结果推断
   - 拟定标题 + meta（为点击率 CTR 而写，控制在 60/155 字符以内）
   - H2/H3 大纲，每节附一行说明它必须讲什么
   - 要回答的问题（PAA + 问句关键词）
   - 基本盘 vs 差异化角度
   - 内链：从 3–5 个现有页面链过来，并给出锚文本
   - 目标长度：对齐排名页面的中位数，不要注水

## 输出

直接给出简报，可交给写手（或据此直接撰写）。不要加开场白。
