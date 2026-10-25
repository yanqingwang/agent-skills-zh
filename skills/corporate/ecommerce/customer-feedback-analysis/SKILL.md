---
nexscope:
  name: "Customer Feedback Analysis"
  category: "Reviews & Reputation"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "reviews"
    - "sentiment-analysis"
    - "customer-feedback"
    - "product-improvement"
  model: "any"
  tokens: "~2000"
  keywords:
    - "customer feedback analysis"
    - "review sentiment analysis"
---

> **中文汉化版** · 上游：[nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills) · 原文件：`customer-feedback-analysis/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 客户反馈分析

AI 驱动的客户反馈与评价情绪分析 Skill。从各电商平台客户评价中提取痛点、功能请求与改进优先级。

## 能力

- 基于你的具体业务背景生成可落地的评价与声誉管理框架
- 覆盖主流电商平台（Amazon、Shopify、Walmart、WooCommerce、Etsy、TikTok Shop）
- 提供带行业基准的数据驱动建议
- 输出可直接实施的方案，而非泛泛建议

## 安装

```
clawhub install customer-feedback-analysis
```

## 用法

**输入：**
产品评价、客户反馈数据、品牌/ASIN

**输出：**
情绪分析报告、痛点提取、功能请求排序、改进优先级矩阵

### 示例提示词

> "我在[平台]经营一家[你的业务类型]。帮我搭建客户反馈分析。这是我的现状：[描述背景]。"

## 局限

- 需要你的具体业务数据才能给出准确建议
- 市场基准基于美欧数据——其他地区需自行调整
- 建议应对照你平台当前政策验证
- 不替代专业监测 SaaS 工具——本 Skill 设计的是策略与框架

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
