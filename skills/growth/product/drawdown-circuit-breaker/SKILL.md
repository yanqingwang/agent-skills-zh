---
name: drawdown-circuit-breaker
description: 根据 trader-memory-core 状态评估账户级回撤熔断（drawdown circuit breaker）规则，并决定今天是否允许承担新的交易风险。使用已实现盈亏（realized P&L）、连亏冷却期以及周/月回撤限额，无需任何外部 API。
---

> **中文汉化版** · 上游：[tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) · 原文件：`skills/drawdown-circuit-breaker/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 回撤熔断（Drawdown Circuit Breaker）

## 概述

评估交易者今天是否应承担新的交易风险，依据是账户级的已实现盈亏（realized P&L）与近期的终局交易结果。本 Skill 只读取 trader-memory-core 的 thesis YAML 文件。它产出一个 `circuit_breaker_decision` 工件，与 exposure-coach 生成的市场侧 `exposure_decision` 互为补充。

熔断机制是一个建议与记录工具。它不替代人类判断，也不会执行券商侧的阻止或自动拒单。

## 何时使用

- 在筛选或为任何新的波段交易候选确定仓位之前
- 在一笔亏损交易或部分减仓之后，检查是否有冷却期生效
- 在每日规划时，当 trader-memory-core 中包含近期已平仓或部分平仓的持仓
- 作为 swing-opportunity-daily 进入候选生成之前的工作流关卡
- 在审查日/周/月亏损限额是否被突破时

## 前置条件

- Python 3.9+
- 本地 trader-memory-core thesis YAML 文件，通常位于 `state/theses/`
- 以美元计的账户规模
- 无需 API 密钥或网络访问

## 工作流

### 步骤 1：读取交易者记忆状态

将脚本指向 thesis 状态目录：

```bash
python3 skills/drawdown-circuit-breaker/scripts/check_circuit_breaker.py \
  --state-dir state/theses \
  --account-size 100000 \
  --output-dir reports/
```

脚本会扫描每个 `th_*.yaml` 文件，并从每个 thesis 的 `status_history[]` 台账条目中读取已实现盈亏。它不使用 `_index.json` 来获取盈亏，因为该索引只是一个轻量查询文件，不包含所需的已实现盈亏台账。

对每个文件完成校验后，脚本按区分大小写、去除首尾空白的 `thesis_id` 对有效 thesis 分组。如果两个或更多有效文件共享同一 ID，它会把整个重复组从盈亏与连亏计算中排除，报告每个实际来源路径，并返回 `PARTIAL` + `HALTED`，直到重复状态被修复并重新运行决策。`metrics.theses_scanned` 只统计具有唯一 ID 的已接受 thesis。

如果状态目录缺失或是一个空目录，本 Skill 返回 `TRADING_ALLOWED` 且 `data_quality: EMPTY_STATE`，以免新用户因没有历史记录而被阻塞。如果配置的状态路径存在但不是目录，本 Skill 保守失败（fail closed），视为不完整的状态数据。

如果状态存在，但某个 thesis、台账事件或终局结果必须被跳过，或与其他已记录值冲突，本 Skill 会以 `data_quality: PARTIAL`、`recommendation: HALTED` 以及一条 `incomplete_state_data` 规则保守失败。请先修复警告并重新运行，再承担新风险。唯一可恢复的例外是：对于没有已实现盈亏台账条目的旧版（legacy）thesis，使用有限数值的终局 `outcome.pnl_dollars` 兜底；它仍以 `PARTIAL` 呈现，但不会单独覆盖计算出的建议。对于 `ACTIVE`、`PARTIALLY_CLOSED`、`CLOSED` 和 `INVALIDATED` 的 thesis，每条历史事件必须是带有可识别 `status` 和可解析 `at` 的对象，且最后一条历史状态必须与 thesis 状态一致。`ACTIVE` 和 `PARTIALLY_CLOSED` 的 thesis 还必须携带入场实际值；`PARTIALLY_CLOSED` 必须携带持仓。畸形、过期或骨架式的生命周期历史会使终局兜底失效并触发 HALTED。台账形态的事件若其 `realized_pnl` 缺失、无类型或为非有限值，同样会 HALTED，而不是被强制转换。

### 步骤 2：评估熔断规则

默认规则如下：

| 规则 | 默认值 | 触发状态 | 解除 |
|------|---------|-----------------|---------|
| 单日最大亏损 | 账户的 2.0% | HALTED | 下一个 ET 工作日 |
| 连亏冷却期 | 2 个终局亏损 thesis | COOLDOWN | 最近一次亏损退出后 24 小时 |
| 周回撤熔断 | 账户的 5.0% | HALTED | 下周一（ET） |
| 月回撤熔断 | 账户的 8.0% | HALTED | 下月第一天（ET） |

日、周、月边界使用 `America/New_York`。来自 `trader-memory-core` 的仅日期生产者
时间戳按其标注的 ET 日期计算。设置
`--as-of` 以获得确定性评估；仅日期的
`--as-of` 值覆盖整个 ET 交易日，而带时间戳的值会排除该时刻之后的未来事件：

```bash
python3 skills/drawdown-circuit-breaker/scripts/check_circuit_breaker.py \
  --state-dir state/theses \
  --account-size 100000 \
  --as-of 2026-07-02T12:00:00-04:00 \
  --output-dir reports/
```

### 步骤 3：按需覆盖阈值

在 CLI 上覆盖单个阈值：

```bash
python3 skills/drawdown-circuit-breaker/scripts/check_circuit_breaker.py \
  --account-size 100000 \
  --max-daily-loss-pct 1.5 \
  --losing-streak-n 3 \
  --cooldown-hours 48 \
  --weekly-drawdown-pct 4 \
  --monthly-drawdown-pct 6
```

或者提供一个 JSON 配置文件：

```json
{
  "max_daily_loss_pct": 1.5,
  "losing_streak_n": 3,
  "cooldown_hours": 48,
  "weekly_drawdown_pct": 4.0,
  "monthly_drawdown_pct": 6.0
}
```

CLI 参数优先于配置文件中的值。

### 步骤 4：解读决策

将生成的决策作为新交易风险的关卡：

| 建议 | 含义 |
|----------------|---------|
| TRADING_ALLOWED | 没有熔断规则生效；可以继续走工作流的后续环节，承担新交易风险 |
| COOLDOWN | 不要开新仓；继续管理现有持仓并复盘近期亏损 |
| HALTED | 停止新开仓，因为回撤限额已触发或账户状态数据不完整；先修复/重跑所有数据警告再继续 |

现有持仓的管理仍是人类决策。熔断机制旨在防止已实现损失之后的风险升级，而不是强制平仓。

基于时间的规则带有 ISO 8601 的 `active_until`。非基于时间的 `incomplete_state_data` 规则使用 `active_until: null`；其 Markdown 报告会说明该熔断持续到状态被修复并重新运行决策为止。

## 输出格式

脚本会写入 `circuit_breaker_decision_YYYY-MM-DD_HHMMSS.json`，以及（除非设置 `--json-only`）一份配套的 markdown 报告。

```json
{
  "schema_version": "1.0",
  "generated_at": "2026-07-02T16:00:00+00:00",
  "as_of_date": "2026-07-02",
  "recommendation": "COOLDOWN",
  "triggered_rules": [
    {
      "rule": "losing_streak_cooldown",
      "threshold": 2,
      "observed": 2,
      "active_until": "2026-07-02T15:30:00-04:00",
      "detail": "2 consecutive losing closes; last loss exit 2026-07-01T15:30:00-04:00."
    }
  ],
  "metrics": {
    "realized_pnl_today": 0.0,
    "realized_pnl_wtd": -250.0,
    "realized_pnl_mtd": -250.0,
    "consecutive_losses": 2,
    "last_loss_exit_at": "2026-07-01T15:30:00-04:00",
    "theses_scanned": 12
  },
  "account_size": 100000.0,
  "config": {
    "max_daily_loss_pct": 2.0,
    "losing_streak_n": 2,
    "cooldown_hours": 24.0,
    "weekly_drawdown_pct": 5.0,
    "monthly_drawdown_pct": 8.0
  },
  "data_quality": "OK",
  "warnings": [],
  "rationale": "Recent losing closes triggered a cooldown. Avoid new entries until the cooldown expires."
}
```

## 交易所日历契约

运行检查器之前先安装 `requirements.txt`。日、周、月熔断日期
使用实际的 XNYS 交易日。`active_until` 保持兼容：
熔断在下一个合资格交易日的 00:00（America/New_York）结束，而不是在该交易日的
开盘钟声时。使用 `--as-of` 进行确定性评估。

## 资源

- `scripts/check_circuit_breaker.py` - 主 CLI 与规则引擎
- `references/circuit_breaker_framework.md` - 规则定义、默认值与数据来源说明
- `skills/trader-memory-core/schemas/thesis.schema.json` - thesis 状态的来源 schema

## 关键原则

1. **只看已实现损失** - 日常计算使用已记录的已实现盈亏，而非未实现盈亏或 thesis 级别的累计字段。
2. **生存优先** - 熔断机制的存在是为了防止亏损后的风险升级。
3. **仅作建议，不做自动执行** - 输出用于提示工作流关卡；它不会下单、撤单或阻止券商订单。
4. **状态不完整时保守失败** - 空状态允许新用户开始，但畸形、已废弃、冲突或非有限值的风险数据会返回 `PARTIAL` + `HALTED` 而不崩溃。有限数值的旧版终局兜底被报告为可恢复的 `PARTIAL`，且不构成阻塞。
