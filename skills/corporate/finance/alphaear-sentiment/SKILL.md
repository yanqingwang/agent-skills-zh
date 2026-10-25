---
name: alphaear-sentiment
description: 使用 FinBERT 或 LLM 分析财经文本情绪。当用户需要判定金融文本的市场情绪（正面/负面/中性）及评分时使用。
---

> **中文汉化版** · 上游：[RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) · 原文件：`skills/alphaear-sentiment/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# AlphaEar 情绪分析 Skill

## 概述

本 Skill 提供专为财经文本定制的情绪分析能力，支持 FinBERT（本地模型）与基于 LLM 的两种分析模式。

## 能力

### 1. 情绪分析（FinBERT / 本地）

用 `scripts/sentiment_tools.py` 跑高速的本地 FinBERT 情绪分析。

**关键方法：**

-   `analyze_sentiment(text)`：用本地化的 FinBERT 模型获取情绪分与标签。
    -   **返回**：`{'score': float, 'label': str, 'reason': str}`。
    -   **分数范围**：-1.0（负面）到 1.0（正面）。
-   `batch_update_news_sentiment(source, limit)`：批量处理数据库中未分析的新闻（仅 FinBERT）。

### 2. 情绪分析（LLM / 代理式）

需要更高精度或推理能力时，**你（Agent）本人**应使用下面的提示词直接调用 LLM 完成分析，必要时再回写数据库。

#### 情绪分析提示词

本地工具不够用或需要推理时，用这个提示词分析财经文本。

```markdown
请分析以下金融/新闻文本的情绪极性。
返回严格的 JSON 格式:
{"score": <float: -1.0到1.0>, "label": "<positive/negative/neutral>", "reason": "<简短理由>"}

文本: {text}
```

**评分指引：**
- **正面（0.1 到 1.0）**：乐观消息、利润增长、政策利好等。
- **负面（-1.0 到 -0.1）**：亏损、制裁、下跌、悲观。
- **中性（-0.1 到 0.1）**：事实报道、横盘、影响不明。

#### 辅助方法
- `update_single_news_sentiment(id, score, reason)`：把你的人工分析结果存入数据库。

## 依赖

-   `torch`（FinBERT 需要）
-   `transformers`（FinBERT 需要）
-   `sqlite3`（内置）

确保 `DatabaseManager` 已正确初始化。
