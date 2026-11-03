> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/statistical-power/references/effect_sizes.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 效应量的选择与换算

效应量是决定功效分析成败的输入，也是人们最常搞错的一个。基于猜测或被夸大的
效应量算出来的功效，比不做功效分析更糟，因为它带着虚假的权威感。本文件讲
如何选一个站得住脚的数值，以及如何在不同检验所用的指标之间换算。

## 如何选择（按优先顺序）

### 1. 最小关注效应量（SESOI）— 最佳

功效应当对准那个真正能**改变某个决策**、或在科学/临床上有意义的最小效应，
而不是你希望看到或预期会看到的效应。设定它的方式有：
- **锚定式**：患者/用户能感知到的最小差异，或跨越临床阈值的最小差异
  （例如某个经过验证的量表上变化 5 分）。
- **资源/决策式**：考虑到成本之后，值得采纳该干预的最小效应。
- **基准式**：小于这个效应你就把结果当作实际上没有差异。

以 SESOI 做功效计算是最站得住脚的选择：如果真实效应更大，你的功效只会更富余；
如果更小，那是你已经判定它无关紧要。

### 2. 先验估计 — 但要收缩
预试验估计往往很不确定。基于发表或显著性进行的筛选会让可用估计向上偏；
这并不意味着每个预试验都向上偏。使用相关的证据综合、有依据的收缩/保证
模型，或一个合理区间。置信边界的保护措施需要预先设定置信水平与方向。
如果区间包含零，那么没有任何有限样本能对区间内的每个取值都拥有高功效；
不要取一个绝对的负端点就称之为保守。不存在一个通用的预试验样本量门槛，
能让效应估计变得可靠。

### 3. 惯例值 — 最后手段，而且要说明
Cohen 的小/中/大是任意的，且对具体领域一无所知。它们从来就不是用来替代
领域知识的。只在别无选择时使用，并明确说明你这样做了，同时考察若干取值。
笼统的"小"这个标签，不是任何特定领域的科学依据。

## 永远要做敏感性分析

无论你选哪一个，都要报告所需 n 在一个合理效应量区间内如何变化
（例如一条功效曲线，或一张 d = 0.3、0.4、0.5 下 n 的小表）。单一的一个 n
会掩盖最大的不确定性来源。这才是一次好的功效分析真正的交付物。

## 基准值表（Cohen 的约定）

| 指标 | 适用场景 | 小 | 中 | 大 |
|--------|----------|-------|--------|-------|
| d | 均值差（t 检验） | 0.20 | 0.50 | 0.80 |
| f | ANOVA | 0.10 | 0.25 | 0.40 |
| f² | 回归 / 多元 R² | 0.02 | 0.15 | 0.35 |
| r | 相关 | 0.10 | 0.30 | 0.50 |
| η² (eta-squared) | ANOVA 解释的方差 | 0.01 | 0.06 | 0.14 |
| h | 比例（反正弦） | 0.20 | 0.50 | 0.80 |
| w | 卡方 | 0.10 | 0.30 | 0.50 |
优势比（OR）没有通用的小/中/大阈值。同一个 OR 在不同基线风险下对应不同的
绝对风险差；请使用有依据的基线与方向。

## 换算

**d ↔ r**（总体/两组的规划换算，转换为点二列 r，等分配且组内方差相同；
不是通用的 Pearson-r 换算，也不是精确的有限样本校正）
```
r = d / sqrt(d^2 + 4)            # equal groups
d = 2r / sqrt(1 - r^2)
```

**d ↔ Cohen's f**（k 组；两个等样本组时 f = d/2）
```
f = abs(d) / 2                   # two equal groups; f is nonnegative
```

**f ↔ η²**
```
f   = sqrt(eta2 / (1 - eta2))
eta2 = f^2 / (1 + f^2)
```

**f² ↔ R²**（回归）
```
f2 = R2 / (1 - R2)               # whole model
f2 = dR2 / (1 - R2_full)         # increment from added predictors
```

**比例 → Cohen's h**
```
h = 2*asin(sqrt(p1)) - 2*asin(sqrt(p2))
```
在 Python 中：`statsmodels.stats.proportion.proportion_effectsize(p1, p2)`。

**比例 → Cohen's w**（用于卡方，与期望值 p0_i 相比）
```
w = sqrt( sum( (p_i - p0_i)^2 / p0_i ) )
```
对于不带连续性校正的 Pearson 卡方统计量，`w = sqrt(chi2 / N)`，
且 `w = V * sqrt(min(r-1, c-1))`，其中 V 是 Cramér's V。

**优势比 → 对数几率**（用于按模拟做 logistic 回归的功效分析）
```
beta = log(OR)                   # log-odds change per specified predictor unit
```

对于连续预测变量，每个 SD 的 OR 为 `exp(beta * SD_x)`；对于二元预测变量，
它比较的是 x=1 与 x=0。在只有截距的基线 `p0` 下，
`intercept=log(p0/(1-p0))` 给出的是 x=0 时的条件风险，在加入协变量效应之后，
它一般不等于总体的边际风险。

**标准化 → 原始量纲**
标准化效应的效度取决于你除以的那个 SD。如果你知道原始差值和各组 SD，
就在原始量纲上工作，最后再换算：
`d = (mean1 - mean2) / sd_pooled`。配对设计中，`dz` 使用的是*差值*的 SD，
它取决于对内相关 — 参见 `closed_form_recipes.md`。

## 常见错误

- **用观察到的/期望的效应代替 SESOI** — 你会为你的期望而不是为重要的事情
  做足功效。
- **忽略先验估计的不确定性与选择偏倚** — 乐观的效应会低估所需的 n。
- **混淆 d 与 f，或 η² 与 f²** — 它们之间的差别见上面的换算；d 上差一个
  2 倍因子，会让所需 n 变成四倍或四分之一。
- **只报告一个数字** — 永远要给出敏感性区间。
- **把 Cohen 的基准值当作事实** — 它们是约定，不是测量结果。


审阅于 2026-10-01，对照 [Lakens (2022), Sample Size Justification](https://doi.org/10.1525/collabra.33267)、
[statsmodels proportion_effectsize](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_effectsize.html)
与 [statsmodels one-way effect-size definitions](https://www.statsmodels.org/stable/generated/statsmodels.stats.oneway.effectsize_oneway.html)。
这些是规划假设与代数换算，而不是对某个科学 SESOI、预试验人群或临床决策阈值的
验证。
