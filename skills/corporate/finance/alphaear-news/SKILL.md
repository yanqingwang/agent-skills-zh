---
name: alphaear-news
description: 抓取财经热点新闻、统一趋势与金融市场预测数据。当用户需要实时财经新闻、多来源（微博、知乎、华尔街见闻等）趋势报告，或 Polymarket 金融市场预测数据时使用。
---

> **中文汉化版** · 上游：[RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) · 原文件：`skills/alphaear-news/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# AlphaEar 新闻 Skill

## 概述

抓取实时热点新闻、生成统一趋势报告，并获取 Polymarket 预测数据。

## 能力

### 1. 抓取热点新闻与趋势

通过 `NewsNowTools` 使用 `scripts/news_tools.py`。

-   **抓取新闻**：`fetch_hot_news(source_id, count)`
    -   有效的 `source_id` 见 [sources.md](references/sources.md)（如 `cls`、`weibo`）。
-   **统一报告**：`get_unified_trends(sources)`
    -   聚合多个来源的头条新闻。

### 2. 获取预测市场

通过 `PolymarketTools` 使用 `scripts/news_tools.py`。

-   **市场摘要**：`get_market_summary(limit)`
    -   返回活跃预测市场的格式化报告。

## 依赖

-   `requests`, `loguru`
-   `scripts/database_manager.py`（本地数据库）
