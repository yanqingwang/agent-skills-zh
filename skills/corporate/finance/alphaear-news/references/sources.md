> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/corporate/finance/alphaear-news/references/sources.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 新闻源参考

## 支持的新闻源

| 源 ID | 名称 | 分类 | 描述 |
|:----------|:-----|:---------|:------------|
| `cls` | 财联社 | 金融 | 实时财经新闻，聚焦 A 股与宏观经济。 |
| `wallstreetcn` | 华尔街见闻 | 金融 | 全球市场、宏观经济与深度分析。 |
| `xueqiu` | 雪球热榜 | 金融 | 社区驱动的股票讨论与热门话题。 |
| `weibo` | 微博热搜 | 综合 | 热门社会话题，适合把握公众情绪。 |
| `zhihu` | 知乎热榜 | 综合 | 热门话题的深度讨论与问答。 |
| `baidu` | 百度热搜 | 综合 | 大众搜索热点。 |
| `toutiao` | 今日头条 | 综合 | 算法推荐的新闻。 |
| `douyin` | 抖音热榜 | 综合 | 短视频热点（仅标题）。 |
| `thepaper` | 澎湃新闻 | 综合 | 严肃新闻与时事报道。 |
| `36kr` | 36氪 | 科技 | 创业、风投与科技行业新闻。 |
| `ithome` | IT之家 | 科技 | 消费电子与数码产品。 |
| `v2ex` | V2EX | 科技 | 开发者社区动态。 |
| `juejin` | 掘金 | 科技 | 开发者博客与教程。 |
| `hackernews` | Hacker News | 科技 | 全球科技与创业新闻（英文）。 |

## Polymarket

- **基础 URL**：`https://gamma-api.polymarket.com`
- **数据**：预测市场（如"美联储会降息吗？"）。
- **用法**：使用 `get_active_markets` 按成交量获取热门活跃市场。
