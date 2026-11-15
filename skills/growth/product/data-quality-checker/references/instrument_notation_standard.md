> **中文汉化版** · 上游：[tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) · 原文件：`skills/data-quality-checker/references/instrument_notation_standard.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 标的记号标准（Instrument Notation Standard）

供市场分析文档保持标的命名一致的参考文档。

## 标准记号表

| 资产 | 代码（ETF） | 代码（期货） | 全名（EN） | 日语 | 备注 |
|-------|-------------|-------------------|----------------|----------|-------|
| 黄金 | GLD | GC | Gold | 金 / ゴールド / 金先物 | GLD = SPDR Gold Shares ETF；GC = COMEX Gold Futures |
| 白银 | SLV | SI | Silver | 銀 | SLV = iShares Silver Trust；SI = COMEX Silver Futures |
| 标普 500 | SPY | ES | S&P 500 | S&P500 | SPY = SPDR S&P 500 ETF；SPX = 指数；ES = E-mini Futures |
| 标普 500 指数 | -- | SPX | S&P 500 Index | S&P500指数 | 现货指数，不能直接交易 |
| 波动率 | -- | VIX | CBOE VIX | 恐怖指数 / VIX | VIX = 指数；VXX/UVXY = ETP |
| 美国国债 | TLT | ZB | 20+ Year Treasury | 米国債 / 10年債 | TLT = iShares 20+ Year；ZB = 30Y futures |
| 原油 | USO | CL | WTI Crude Oil | 原油 / WTI | USO = United States Oil Fund；CL = NYMEX WTI Futures |

## 位数提示（价格量级校验）

位数提示系统用于校验一个报告的价格是否处于该标的正确的数量级。它统计小数点前的位数。

| 标的 | 位数区间 | 典型价格区间 | 有效示例 | 无效示例 |
|------------|------------|---------------------|---------------|-----------------|
| GLD | 2-3 | $100 - $999 | GLD: $268 | GLD: $2,800（期货价格） |
| GC | 3-4 | $1,000 - $9,999 | GC: $2,650 | GC: $265（ETF 价格） |
| SPY | 2-3 | $100 - $999 | SPY: $580 | SPY: $5,800（指数点位） |
| SPX | 4-5 | $1,000 - $99,999 | SPX: $5,800 | SPX: $580（ETF 价格） |
| VIX | 1-2 | $1 - $99 | VIX: $18 | VIX: $180 |
| TLT | 2-3 | $10 - $999 | TLT: $92 | TLT: $9 |
| SLV | 2-2 | $10 - $99 | SLV: $28 | SLV: $280 |
| SI | 2-2 | $10 - $99 | SI: $31 | SI: $3,100（整张合约价值） |
| USO | 2-2 | $10 - $99 | USO: $72 | USO: $720 |
| CL | 2-3 | $10 - $999 | CL: $78 | CL: $7 |

### 常见错误

1. **ETF/期货混淆**：把 GC（黄金期货）的价格标成 GLD，或反过来。黄金 ETF 约 $260 vs 黄金期货约 $2,600。
2. **指数/ETF 混淆**：把 SPX 的点位标成 SPY，或反过来。SPY 约 $580 vs SPX 约 $5,800。
3. **每股 vs 每张合约**：期货价格通常按单位计（例如黄金按金衡制盎司），ETF 价格按股计。

## 货币对记号

| 标准 | 备选 | 避免 |
|----------|-------------|-------|
| USD/JPY | USDJPY, ドル円 | JPY/USD（写反了） |
| EUR/USD | EURUSD, ユーロドル | USD/EUR（写反了） |
| GBP/USD | GBPUSD, ポンドドル | USD/GBP（写反了） |

**约定**：基准货币 / 报价货币。价格告诉你买入一个单位基准货币需要多少个单位的报价货币。

## 指数记号

| 首选 | 备选 | 语境 |
|-----------|-------------|---------|
| S&P 500 | S&P500, SP500 | 一般性指代 |
| SPX | S&P 500 Index | 引用现货指数点位时 |
| SPY | SPDR S&P 500 ETF | 引用 ETF 价格时 |
| Dow | DJIA, Dow Jones, DJI | Dow Jones Industrial Average |
| Nasdaq | COMP, QQQ, NDX | Nasdaq Composite（COMP）vs Nasdaq-100（NDX/QQQ） |
| Russell 2000 | RUT, IWM | RUT = 指数，IWM = ETF |

## 大宗商品记号

| 商品 | 期货代码 | ETF 代码 | 日语 |
|-----------|---------------|------------|----------|
| 黄金 | GC | GLD, IAU | 金, ゴールド |
| 白银 | SI | SLV | 銀 |
| 原油（WTI） | CL | USO | 原油, WTI |
| 天然气 | NG | UNG | 天然ガス |
| 铜 | HG | COPX | 銅 |

## 最佳实践

1. **每个文档选定一种记号**，全文一致。
2. **首次提及时**，写全名加代码："SPDR Gold Shares (GLD) traded at $268."
3. 同一资产**不要混用 ETF 和期货代码**，除非显式标注（如 "GLD (ETF) vs GC (futures)"）。
4. **日语文档**可以使用日语名称，但首次提及时要附代码："金（GLD）は$268で取引。"
