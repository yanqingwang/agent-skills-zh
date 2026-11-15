> **中文汉化版** · 上游：[tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) · 原文件：`skills/drawdown-circuit-breaker/references/circuit_breaker_framework.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 回撤熔断框架

## 目的

回撤熔断是面向新交易风险的账户级风险闸门。它在筛选或仓位计算之前回答一个问题："交易员的账户状态今天是否足够清晰，可以再开一笔新仓？"

它是市场侧敞口闸门的交易员侧配套件。Exposure-coach 问的是市场环境是否允许新敞口；Drawdown-circuit-breaker 问的是交易员已实现的账户损伤和近期执行结果是否允许新风险。

## 源数据

只读取来自 `state/theses/` 或调用方提供的 `--state-dir` 的 trader-memory-core 论文（thesis）YAML 文件。

使用这些字段：

- `status_history[][].realized_pnl`：已实现盈亏（P&L）账目条目
- `status_history[][].at`：已实现盈亏事件的时间戳
- `status`：识别终态论文（`CLOSED`、`INVALIDATED`）
- `exit.actual_date`，回退到最后一个终态 `status_history[].at`，解析并转换为 `America/New_York` 时区，用于终态交易排序
- `outcome.pnl_dollars`：终态盈亏分类

不要用 `_index.json` 做盈亏。它是一个轻量查询索引，不包含部分减仓或每日已实现盈亏记账所需的账目。

只有在论文文件通过校验之后，才把大小写敏感、去除首尾空白的 `thesis_id` 当作逻辑身份。如果多个有效文件共享同一个 ID，把该重复组中的每一个文件同时从已实现盈亏和终态连败计算中排除。发出包含每个实际来源路径的确定性警告，返回 `PARTIAL` + `HALTED`，并要求先修复状态再重跑。不要把输入 YAML 的 `_source_path` 值当作审计证据。`metrics.theses_scanned` 是 ID 唯一且被接受的有效论文数量。

## 日历规则

所有按日、周、月的已实现盈亏聚合都用 `America/New_York` 日期。

- 日：ET 日期等于 as-of 日期、且时间戳不晚于 `--as-of` 的事件
- 周：从周一 ET 到 as-of 时间戳的事件
- 月：从 ET 月份第一个自然日到 as-of 时间戳的事件

`trader-memory-core` 会把不带时间的生产方日期拉宽到 UTC 零点（例如
`2026-07-02T00:00:00+00:00`）。此类事件记在指定的 ET 记账日上，而不是前一个 ET 晚间。

脚本接受 `--as-of`，让测试和样例运行可以冻结评估日期。
仅日期的值覆盖整个 ET 当天；带时间戳的值是精确截止点。

## 默认规则

| 规则 | 默认 | 状态 | 生效至 |
|------|---------|-------|--------------|
| `max_daily_loss` | 在 as-of 的 ET 日期，已实现亏损达到账户规模的 2.0% | `HALTED` | 下一个 ET 工作日 |
| `losing_streak_cooldown` | 连续两笔终态论文的 `outcome.pnl_dollars` 为负 | `COOLDOWN` | 最新一次亏损退出后 24 小时 |
| `weekly_drawdown_halt` | 周初至今已实现亏损达到账户规模的 5.0% | `HALTED` | 下一个周一 ET |
| `monthly_drawdown_halt` | 月初至今已实现亏损达到账户规模的 8.0% | `HALTED` | 下一个 ET 月的第一天 |

盈亏打平的终态论文算作盈利。这与 trader-memory-core 的月度复盘行为一致：`pnl >= 0` 被分类为盈利。

如果多条规则同时触发，返回最严格的状态：

1. `HALTED`
2. `COOLDOWN`
3. `TRADING_ALLOWED`

即使更严格的规则决定了最终建议，JSON 工件中也要包含每一条已触发的活跃规则。

## 数据质量

| 取值 | 含义 |
|-------|---------|
| `OK` | 状态目录存在、论文文件加载成功，且没有跳过任何格式错误的账目或终态记录 |
| `EMPTY_STATE` | 状态目录缺失，或它是一个存在但不含任何 `th_*.yaml` 文件的目录 |
| `PARTIAL` | 至少发出过一条数据警告，包括被跳过/冲突的风险数据，或一个恢复出来的有限 legacy outcome |

`EMPTY_STATE` 返回 `TRADING_ALLOWED`。不应仅仅因为还没有 trader-memory-core 状态就阻止一个新用户。

`PARTIAL` 采取 fail-closed 并伴随 `HALTED` 和一条 `incomplete_state_data` 规则，以下情形都会触发：配置的状态路径不是目录；某个有效 `thesis_id` 重复；某个论文、账目条目或终态结果被跳过、格式错误、非有限值、缺失，或与另一个盈亏来源冲突。它的 `active_until` 为 `null`，因为解除需要修复状态并重跑，而不是等待时间流逝。唯一可恢复的警告是：某笔 legacy 终态论文没有已实现盈亏账目条目，但其余部分有可解析的终态历史，且使用了有限的 `outcome.pnl_dollars` 值。对 `ACTIVE`、`PARTIALLY_CLOSED`、`CLOSED` 和 `INVALIDATED` 论文，每条历史事件都必须是对象，带可识别的 `status` 和可解析的 `at`，且最后一条历史状态必须与论文状态一致。`ACTIVE` 和 `PARTIALLY_CLOSED` 论文还必须带入场实际值；`PARTIALLY_CLOSED` 必须带持仓。生命周期历史出现格式错误、过期或残缺，都会取消回退资格并触发 HALT。形如账目的事件（`status: PARTIALLY_CLOSED`，或含 `shares_sold`、`quantity_sold`、`price`、`proceeds` 之一）如果 `realized_pnl` 缺失、类型不对或非有限值，同样 HALT，而不是被强制转换。可恢复的回退仍保持 `PARTIAL` 以便审计可见，但它本身不改变计算出的建议。

账户规模和所有百分比/小时阈值必须为正且有限。非有限的盈亏值绝不进入指标或终态连败计算，JSON 输出序列化时禁用非有限值。

## 配置

默认值可以通过 CLI 标志或 JSON 配置文件覆盖。CLI 标志优先。

```json
{
  "max_daily_loss_pct": 2.0,
  "losing_streak_n": 2,
  "cooldown_hours": 24,
  "weekly_drawdown_pct": 5.0,
  "monthly_drawdown_pct": 8.0
}
```

保本模式用更低的阈值；只有在交易员书面说明为什么可以接受额外波动之后，才允许提高阈值。

## 工作流闸门契约

工作流工件 ID 为 `circuit_breaker_decision`。

swing-opportunity-daily 工作流只有在满足以下条件时才应进入新的候选生成：

```text
circuit_breaker_decision.recommendation == "TRADING_ALLOWED"
```

`COOLDOWN` 和 `HALTED` 都会阻止新开仓。它们不会自动强制平仓或触发券商操作。
