> **中文汉化版** · 上游：[tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) · 原文件：`skills/breakout-trade-planner/references/minervini_entry_rules.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Minervini 突破入场规则

## 入场方法论

Mark Minervini 的 VCP 突破入场遵循严格的顺序：

1. **Stage 2 确认**：依据 Trend Template（7-10 项过滤）
2. **VCP 形态**：回调逐级收缩、成交量枯竭
3. **枢轴点（pivot）突破**：成交量高于平均水平
4. **紧凑止损**：设在最后一个收缩低点（contraction low）下方

## 交易价格推导

```
signal_entry = pivot * (1 + pivot_buffer_pct / 100)    # Buy-stop trigger
worst_entry  = pivot * (1 + max_chase_pct / 100)       # Buy-limit ceiling
stop_loss    = last_contraction_low * (1 - stop_buffer_pct / 100)
```

- **闸门校验与仓位计算用 worst_entry**（最坏情形成交价）
- **信号入场与最坏入场都展示 R 倍数**
- **止盈始终以 worst_entry 为基准**

## 风险规则

- 单笔最大风险：从最坏入场价到止损 8%
- 账户默认风险：每笔 0.5%
- 组合热度上限：总持仓风险 6%
- 追价不得高出枢轴点 2% 以上

## 按评级定仓位

| 评级档位 | 分数 | 乘数 |
|------------|-------|------------|
| Textbook | 90+ | 1.75x |
| Strong | 80-89 | 1.0x |
| Good | 70-79 | 0.75x |
| Developing | 60-69 | 0.0x（仅观察） |

## 入场质量检查（供 breakout-monitor 使用）

在 5 分钟 K 线上确认突破时：

1. **close > pivot**：K 线收盘价高于枢轴点水平
2. **close_loc >= 0.60**：收盘价位于 K 线区间上部 60%
3. **RVOL >= 1.5**：分时段相对成交量高于阈值
4. **chase <= 2%**：价格高出枢轴点不超过 2%

## 订单类型

### Pre-place 模式（stop-limit 括式单）
- 开盘时挂单，价格到达枢轴点时自动触发
- buy_stop = signal_entry, buy_limit = worst_entry
- 括式单包含止损与止盈

### Post-confirm 模式（限价括式单）
- 通过 breakout-monitor 等待 5 分钟 K 线确认
- 条件核实后按 worst_entry 限价买入
- 括式单包含止损与止盈

## 止损位设置

- 首选：最后一个收缩低点减去缓冲（默认 1%）
- Alpaca 要求止损价至少低于入场价 $0.01
- 从 worst_entry 到止损的风险必须 <= 8%

## 来源

- Minervini, M.《Trade Like a Stock Market Wizard》(2013)
- Minervini, M.《Think & Trade Like a Champion》(2017)
- TrendSpider VCP Detector 公开扫描器实现
- ChartMill Minervini 策略文档
