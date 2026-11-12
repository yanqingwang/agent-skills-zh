---
name: keyword-research
description: 从种子主题出发做关键词研究：生成创意，取得真实的 Google 搜索量/CPC、搜索意图与难度，并聚类成一份方案。当用户要求 "find keywords"、"keyword research for X"、"what should I rank for" 或 "build a keyword plan" 时使用。
---

> **中文汉化版** · 上游：[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · 原文件：`skills/keyword-research/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 关键词研究

## 前置要求

免费的 Ryze MCP 连接器（`https://connector.get-ryze.ai/mcp`）。Claude Code：`claude mcp add ryze --transport http https://connector.get-ryze.ai/mcp`。claude.ai / Desktop / Cursor：以同一 URL 添加为自定义连接器。设置说明：https://www.get-ryze.ai/how-to-connect-claude-to-google-meta-ads-mcp?utm_source=github&utm_content=open-seo-mcp-skills

种子词 → 创意 → 指标 → 聚类。搜索量来自 Google Ads 关键词规划师的数据（其他各家转售的正是这一来源），并用 DataForSEO 的搜索意图/难度数据加以补充。

## 工作流

1. **扩展种子词。** 用种子关键词和/或用户 URL 调用 `google_ads__generateKeywordIdeas`，最多收集 ~200 个创意。
2. **指标。** 对候选列表调用 `google_ads__generateKeywordHistoricalMetrics`，取得月搜索量、竞争程度、CPC 区间以及 12 个月趋势。
3. **搜索意图 + 难度（可选增强）。** 如果工作区提供了 DataForSEO 工具，就为排名靠前的 ~50 个词调用 Labs 的 `keyword_overview` 端点（搜索意图、关键词难度、SERP 特性）。请求形式：`native__get_provider_docs`，provider 取 `dataforseo`。如果不可用就静默跳过，仅凭 Google 指标已足够支撑 v1 方案。
4. **当前已有排名。** 调用 `google_search_console__runRawSearchAnalytics`（维度取 `query`，按主题过滤），标出网站已获得排名的关键词；这些属于优化现有页面、而非新建页面的目标。
5. **聚类。** 按搜索意图和主题分组，形成内容簇：支柱页面 + 支撑页面。每个簇给出：目标关键词、辅助关键词、总搜索量、搜索意图、已有页面（若有）或 "new page"。

## 输出

每个簇一张表（关键词、搜索量、CPC、搜索意图、当前排名，若有），随后给出排序后的方案：优先攻哪些簇、为什么（搜索量 × 可赢性，优先网站已接近首页排名的簇）。用平实语言，不堆砌废话。

## 规则

- 绝不编造搜索量。如果指标调用失败，就展示关键词但不带数字，并说明原因。
- CPC 必须出现在输出里：它告诉用户这些流量值多少钱，同时还能兼作广告否定关键词的来源。
