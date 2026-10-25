---
name: cohort-analysis
description: "对用户参与度数据执行同期群（cohort）分析——留存曲线、功能采用趋势，以及分层级洞察。适用于按同期群分析用户留存、研究功能随时间的采用情况、调查流失（churn）模式，或识别参与度趋势时使用。"
---

> **中文汉化版** · 上游：[phuryn/pm-skills](https://github.com/phuryn/pm-skills) · 原文件：`pm-data-analytics/skills/cohort-analysis/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 同期群分析（Cohort Analysis）与留存探索

## 目的
按同期群分析用户参与度与留存模式，识别用户行为、功能采用和长期参与度的趋势。将定量洞察与定性研究建议相结合。

## 工作原理

### 第 1 步：读取并校验你的数据
- 接受包含用户同期群信息的 CSV、Excel 或 JSON 数据文件
- 核验数据结构：同期群标识符、时间段、参与度指标
- 检查缺失值与数据质量问题
- 汇总关键统计信息（同期群规模、日期范围、可用指标）

### 第 2 步：生成定量分析
- 计算同期群留存率与参与度趋势
- 识别留存曲线、衰减模式与异常
- 计算各同期群的功能采用率
- 计算环比（month-over-month 或 period-over-period）变化
- 如有要求，生成使用 pandas 和 numpy 的 Python 分析脚本

### 第 3 步：创建可视化
- 生成留存热力图（同期群 vs. 时间段）
- 创建展示同期群演进过程的折线图
- 构建功能采用对比图
- 可视化衰减点与参与度趋势
- 输出为交互式图表或静态图片

### 第 4 步：识别洞察与模式
- 发现一个或多个显著模式：
  - 特定同期群的早期流失
  - 后期参与度变化
  - 功能采用聚类
  - 季节性或时间性趋势
- 突出令人意外的发现与偏离
- 比较各同期群的表现以建立基线

### 第 5 步：建议后续研究
- 推荐定性研究方法：
  - 针对流失用户的定向用户访谈
  - 面向高参与度同期群的功能使用调研
  - 关键交互模式的会话回放
  - 高留存与低留存同期群的赢单/丢单（win/loss）分析
- 设计后续定量研究
- 建议 A/B 测试或功能实验

## 使用示例

**示例 1：上传 CSV 数据**
```
Upload cohort_engagement.csv with columns: cohort_month, weeks_active,
user_id, feature_x_usage, engagement_score

Request: "Analyze retention patterns and identify why Q4 2025 cohorts
underperform compared to Q3"
```

**示例 2：描述数据格式**
```
"I have monthly user cohorts from Jan-Dec 2025. Each row shows:
cohort date, user ID, purchase frequency, and support tickets.
Analyze which cohorts show best long-term retention."
```

**示例 3：功能采用分析**
```
Upload feature_usage.xlsx with cohort adoption data.

Request: "Compare adoption curves for our new feature across cohorts.
Which cohorts adopted fastest? Any patterns?"
```

## 核心能力

- **数据读取**：导入 CSV、Excel、JSON、SQL 查询结果
- **留存分析**：计算并可视化随时间变化的留存率
- **同期群比较**：比较各同期群组之间的指标
- **异常检测**：标记异常模式或衰减
- **Python 脚本**：生成可复用的分析代码，用于持续分析
- **可视化**：创建热力图、图表和交互式仪表盘
- **研究设计**：建议定向的后续研究与访谈方法
- **统计摘要**：提供定量指标与相关性分析

## 获得最佳效果的技巧

1. **包含时间维度**：提供跨多个时间段的数据
2. **清晰定义同期群**：明确同期群分组方式（注册月份、功能上线日期等）
3. **提供背景信息**：说明该期间内的产品变更、发布或事件
4. **多个指标**：包含留存、参与度、功能使用、营收等
5. **充足的数据**：至少 3-4 个同期群才能识别出有意义的模式
6. **提出具体的输出要求**：明确要求可视化、Python 脚本或研究建议

## 输出格式

你将收到：
- **数据摘要**：同期群概览与数据质量评估
- **定量发现**：关键指标、留存率与趋势分析
- **可视化**：展示留存曲线、采用模式的图表
- **模式识别**：来自数据的 2-3 个重要洞察
- **研究建议**：具体的定性与定量后续动作
- **分析脚本**（如有要求）：用于可复现分析的 Python 代码
- **后续步骤**：基于发现按优先级排序的行动

---

### 延伸阅读

- [Cohort Analysis 101: How to Reduce Churn and Make Better Product Decisions](https://www.productcompass.pm/p/cohort-analysis)
- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
