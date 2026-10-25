---
name: breakout-trade-planner
description: 从 VCP 筛选器输出生成 Minervini 风格的突破（breakout）交易计划，包含最坏情况风险计算、组合热度（portfolio heat）管理，以及兼容 Alpaca 的订单模板（确认前用 stop-limit 括式单，确认后用限价括式单）。当用户已有 VCP 筛选器结果并希望获得含入场/止损/目标位与仓位规模的可执行交易计划时使用。
---

> **中文汉化版** · 上游：[tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) · 原文件：`skills/breakout-trade-planner/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 突破交易规划器（Breakout Trade Planner）

根据 Mark Minervini 的突破（breakout）方法论，从 VCP 筛选器输出生成交易计划。使用最坏情况入场价计算仓位规模，强制执行组合风险限额，并输出兼容 Alpaca API 的订单模板。

## 何时使用

- 用户已有 VCP 筛选器的 JSON 输出，需要交易计划
- 用户要求计算突破（breakout）的入场/止损/目标位
- 用户需要针对 VCP 突破候选股的 Alpaca 订单模板
- 用户需要带组合热度（portfolio heat）管理的仓位规模计算

## 前置条件

- 带有 `schema_version: "1.0"` 的 VCP 筛选器 JSON 输出
- 无需 API 密钥（使用本地 JSON 文件即可运行）
- 无外部 Skill 依赖（仓位规模计算为内置功能）

## 工作流

### 第 1 步：生成交易计划

以 VCP 筛选器输出运行规划器：

```bash
python3 skills/breakout-trade-planner/scripts/plan_breakout_trades.py \
  --input reports/vcp_screener_YYYY-MM-DD.json \
  --account-size 100000 \
  --risk-pct 0.5 \
  --output-dir reports/
```

### 第 2 步：审阅输出

阅读生成的 JSON 与 Markdown 报告。呈现以下内容：

1. **可执行订单** ， 突破前（pre-breakout）候选股及其订单模板
2. **复核确认** ， 需实时确认的突破中（breakout-state）候选股
3. **观察清单** ， 待监控的发展中 VCP 候选股
4. **已拒绝/推迟/受限** ， 被 Gate 或组合限额过滤掉的候选股
### 第 3 步：解释交易计划

对每笔可执行订单，解释：

- 入价位（信号价 vs 最坏情况价）与止损（stop loss）位置
- R 倍数目标与盈亏比（reward-risk ratio）
- 两种执行模式：pre_place（stop-limit 单）vs post_confirm（5 分钟确认后的限价单）
- 组合风险贡献与累计热度（heat）
- 券商与日内约束：这些模板只是规划产物，不构成券商许可。若该计划可能产生当日往返交易（same-day round trips）或使用融资，请确认用户券商特有的日内/日内交易（day-trading）控制规则。自 2026-06-04 起，FINRA 已用日内保证金标准取代了旧的日内交易者（pattern-day-trader）天数计算和 25,000 美元最低权益要求，券商可在 2027-10-20 前分阶段过渡。

## Minervini Gate（过滤条件）

候选股必须满足全部（ALL）条件：

| 条件 | 突破前（Pre-breakout） | 突破（Breakout） |
|-----------|-------------|----------|
| valid_vcp | True | True |
| rating_band | good/strong/textbook | good/strong/textbook |
| risk_pct_worst | <= 8.0% | <= 8.0% |
| breakout_volume | — | True |
| distance_from_pivot | — | <= max_chase_pct |
| current_price | — | <= worst_entry |

## CLI 参数

| 参数 | 默认值 | 说明 |
|-----------|---------|-------------|
| --account-size | (必填) | 账户权益（美元） |
| --risk-pct | 0.5 | 每笔交易的基础风险百分比 |
| --max-position-pct | 10.0 | 单一持仓最大百分比 |
| --max-sector-pct | 30.0 | 单一板块最大敞口百分比 |
| --max-portfolio-heat-pct | 6.0 | 总未平风险最大百分比 |
| --target-r-multiple | 2.0 | 止盈的 R 倍数 |
| --stop-buffer-pct | 1.0 | 收缩低点（contraction low）下方的止损缓冲 |
| --max-chase-pct | 2.0 | 相对枢轴点（pivot）的最大追价幅度 |
| --pivot-buffer-pct | 0.1 | buy-stop 触发用的枢轴点缓冲 |
| --current-exposure-json | None | 现有组合敞口 |

## 输出

- `breakout_trade_plan_YYYY-MM-DD_HHMMSS.json` — 含订单模板的结构化计划
- `breakout_trade_plan_YYYY-MM-DD_HHMMSS.md` — 人类可读的报告

## 交易所日历与回放

运行规划器前先安装 `requirements.txt`。`--as-of` 接受
`YYYY-MM-DD`（America/New_York 时区 00:00）或带偏移量的 ISO-8601 时间戳。
计划有效期基于当前尚未收盘的 XNYS 交易时段；若已收盘、为周末或交易所节假日，
则取下一个真实交易时段。

## 资源

- `references/minervini_entry_rules.md` — 入场方法论与规则
