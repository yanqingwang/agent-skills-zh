> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/statistical-power/references/closed_form_recipes.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 闭式功效配方

`scripts/power.py` 这个辅助脚本支持的每一种检验，在这里都给出参数约定与其
底层的 statsmodels/scipy 调用。当你需要直接调用 statsmodels、看懂某个参数的
含义，或处理包装器没有覆盖的情形时，使用本文件。

四个求解量 — `effect_size`、样本量、`alpha`、`power` — 服从与检验相关的
方程：给 `solve_power` 恰好留一个为 `None`。请确认所请求的解确实存在，
并在取整之后重新评估功效。包装器要求 `alpha < target_power < 1`，校验定义域，
并拒绝意料之外的关键字参数。下面所有示例均于 2026-10-01 使用
statsmodels 0.15.0 / SciPy 1.18.1 执行。

## 目录
- [两个独立样本均值](#两个独立样本均值)
- [配对 / 单样本均值](#配对--单样本均值)
- [单因素 ANOVA](#单因素-anova)
- [两个比例](#两个比例)
- [单个比例](#单个比例)
- [相关](#相关)
- [卡方](#卡方)
- [多元回归](#多元回归)
- [各检验的效应量单位](#各检验的效应量单位)

---

## 两个独立样本均值

效应量 = **Cohen's d** = (μ₁ − μ₂) / σ_pooled。

```python
from statsmodels.stats.power import TTestIndPower
analysis = TTestIndPower()

# n per group for d=0.5, 80% power, two-sided
n1 = analysis.solve_power(effect_size=0.5, alpha=0.05, power=0.80,
                          ratio=1.0, alternative="two-sided")

# achieved power at n1=64 per group
pw = analysis.solve_power(effect_size=0.5, nobs1=64, alpha=0.05,
                          ratio=1.0, alternative="two-sided")

# minimum detectable d at n1=30 per group, 80% power
d_min = analysis.solve_power(nobs1=30, alpha=0.05, power=0.80, ratio=1.0,
                             alternative="two-sided")
```

`ratio = nobs2 / nobs1`。若为 2:1 分配，设 `ratio=2.0`；返回的 `nobs1`
是该比例下较小的组。返回 n1 后，第 2 组入组 `ceil(ratio*n1)` 人，
并用实际比例复核。辅助脚本假定方差相等；Welch/异方差或整群设计需要
相匹配的方法。效应量带符号，方向为均值1 减均值2。`alternative` ∈
`"two-sided"`、`"larger"`、`"smaller"`。

## 配对 / 单样本均值

配对设计用 **Cohen's dz** 作为效应量（均值差 / 差值的 SD），
单样本用 d。使用 `TTestPower`（单样本求解器）；`nobs` 是配对数或观测数。

```python
from statsmodels.stats.power import TTestPower
TTestPower().solve_power(effect_size=0.4, alpha=0.05, power=0.80,
                         alternative="two-sided")  # -> number of pairs
```

注意：配对设计中 dz 取决于对内相关 ρ：
只有当两个边际 SD 相等、且 d 使用该共同 SD 时，`dz = d / sqrt(2*(1-rho))` 才成立。
一般情况下 `SD(diff) = sqrt(SD1**2 + SD2**2 - 2*rho*SD1*SD2)`。ρ 越大 ⇒ dz 越大 ⇒ n 越小。
如果你只知道原始均值差和各组 SD，请估计 ρ 或改用模拟。

## 单因素 ANOVA

效应量 = **Cohen's f** = sqrt(η² / (1 − η²))。这里的 `nobs` 是各组**合计**的
n，前提是等分配且组内方差相同。先把每组 n 向上取整，再乘以 `k_groups`；
包装器执行的正是这种平衡取整。

```python
import math
from statsmodels.stats.power import FTestAnovaPower
total_n = FTestAnovaPower().solve_power(effect_size=0.25, k_groups=4,
                                        alpha=0.05, power=0.80)
per_group = math.ceil(total_n / 4)
total_enrolled = 4 * per_group
```

换算关系：f = 0.10（小）、0.25（中）、0.40（大）。由 η² 换算：
`f = sqrt(eta2/(1-eta2))`。由 R² 换算：同一公式，把 R² 代入即可。

## 两个比例

效应量 = **Cohen's h** = 2·asin(√p₁) − 2·asin(√p₂)。先把比例转换为 h，
再使用正态近似 `NormalIndPower`。

```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
h = proportion_effectsize(0.40, 0.55)
n1 = NormalIndPower().solve_power(effect_size=h, alpha=0.05, power=0.80,
                                  ratio=1.0, alternative="two-sided")
```

另一种做法是对"合并零假设 / 非合并备择"的 z 检验使用**正态近似**，
这与上面的反正弦计算不同，也不是精确二项检验：

```python
from statsmodels.stats.proportion import (
    samplesize_proportions_2indep_onetail, power_proportions_2indep,
)
n1 = samplesize_proportions_2indep_onetail(
    diff=0.55 - 0.40, prop2=0.40, power=0.80, ratio=1,
    alpha=0.05, alternative="two-sided",
)
pw = power_proportions_2indep(
    diff=0.15, prop2=0.40, nobs1=n1, ratio=1, alpha=0.05,
    alternative="two-sided", return_results=False,
)
```

`samplesize_proportions_2indep_onetail` 接受双侧备择，但在求解 n 时会忽略
远端的拒绝尾。请直接传入预期的 alpha；尾部的选择由它内部处理。
目前只支持差值为零的零假设。

对于小样本或罕见事件，优先使用**模拟**，并采用你实际要跑的精确检验
（Fisher 精确检验，或带连续性校正的卡方检验）。

## 单个比例

检验 p 与固定参考值 p₀。通过 Cohen's h 把两者都转换到反正弦尺度，
并选用 statsmodels 的单样本分支（`ratio=0` 是一个特殊开关，不是分配比例）。
这是反正弦-正态近似，不是精确二项检验。

```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
h = proportion_effectsize(0.60, 0.50)
n = NormalIndPower().solve_power(effect_size=h, alpha=0.05, power=0.80, ratio=0.0)
```

若要做精确的二项规划，请枚举二项结果，或用
`scipy.stats.binomtest(k, n, p=prop0, alternative=...)` 做模拟。
它的备择为 `"two-sided"`、`"greater"`、`"less"`；由于拒绝域是离散的，
功效随整数 n 的变化可能不规则。Cohen's h 只是一个效应量变换，
不是精确检验的功效计算。

`mde("one_proportion", nobs=100)` 与 `mde("two_proportions", nobs1=100)` 返回 h；
此时不传比例。要把基线 p0 处的带符号 h 转换为可实现的概率，令
`theta = asin(sqrt(p0)) + h/2`。只有当 `0 <= theta <= pi/2` 时才存在可行的 p1；
此时 `p1 = sin(theta)**2`。在上述区间之外取正弦的平方会得到虚假的概率。
对于双侧 h，请同时考察正负两个符号以及基线的可行性。

## 相关

效应量 = **Pearson r**。statsmodels 没有对应求解器；请使用 Fisher z 变换
（`power.py` 中已实现）。在功效为 1-beta、双侧（忽略远端尾部）的条件下，
r 的常用近似 n 为：

```
z_r = arctanh(r)
n   = ((z_{1-α/2} + z_{1-β}) / z_r)^2 + 3
```

辅助脚本对其完整的 Fisher-z 拒绝概率做反解，因此 `sample_size`、`power`
与 `mde` 使用同一套近似。它要求 `n > 3` 且 `abs(r) < 1`。对于 `"larger"`
只有上尾有贡献；对于 `"smaller"` 只有下尾有贡献。在 r=0 时，两者都返回 alpha。
与单侧备择方向相反的带符号效应无法达到高于 alpha 的目标功效。

`pingouin.power_corr(r=0.3, power=0.8, alternative="two-sided")` 使用偏差校正的
Fisher 变换与由 t 分布导出的临界相关；它与本脚本**并不数值等价**
（取整前为 84.07364 与约 84.92761；两者都取整为 85）。Pingouin 0.7.0 对方向性
备择使用 `"greater"`/`"less"`，与包装器的 `"larger"`/`"smaller"` 不同。
这两种方法都不覆盖偏相关/秩相关，也不覆盖任意非正态依赖，除非补充额外假设。

## 卡方

效应量 = **Cohen's w** = sqrt(Σ (p_i − p0_i)² / p0_i)。对于列联表，
`w = sqrt(χ²/N)`，等于 Cramér's V·sqrt(min(r−1, c−1))。自由度：
拟合优度在未拟合零假设参数时 `dof = k − 1`（适用时减去已拟合参数的自由度）；
列联表 `dof = (r−1)(c−1)`。`n_bins = dof + 1`。

```python
from statsmodels.stats.power import GofChisquarePower
n = GofChisquarePower().solve_power(effect_size=0.3, n_bins=5, alpha=0.05, power=0.80)
```

w 的基准值：0.10（小）、0.30（中）、0.50（大）。

## 多元回归

效应量 = **Cohen's f²**，整体模型用 R²/(1−R²)，一组新增预测变量用
ΔR²/(1−R²_full)。`power.py` 通过非中心 F、按声明的规划约定
`lambda = f2*n` 直接求解。所假定的 f² 必须与在干扰预测变量条件化之后
受检验的那个变量块相匹配；若指定了固定的协变量矩阵，请使用它实际的
非中心度或改用模拟。

Statsmodels 0.15.0 提供以 f² 为单位、自由度参数命名正确的 `FTestPowerF2`。
旧版 `FTestPower` 用的是 f（不是 f²），且自由度名称是颠倒的。
在 `FTestPowerF2` 中，`lambda=f2*(df_num+df_denom+ncc)`；要让它与本脚本
对受检验子集的处理一致，需要 `ncc=k_total-df_num+1`，而不是照搬其默认值 1。

```python
from power import sample_size, power
# detect f^2 = 0.15 from 3 tested predictors (3 total in the model)
sample_size("linear_regression", effect_size=0.15, df_num=3, k_total=3, power=0.80)
```

- `df_num` = 被**检验**的预测变量个数（分子自由度）。
- `k_total` = 完整模型中除截距以外的全部预测变量列数（包括控制变量与
  虚拟变量/交互项列，而不只算有名字的变量）。`df_denom = n − k_total − 1`。

包装器会拒绝非正的残差自由度，并在整数 n 上搜索至 1,000,000；对回归而言，
即使 `round_up=False` 仍会返回整数。如果在上限处无法达到目标，它会抛出异常。

f² 的基准值：0.02（小）、0.15（中）、0.35（大）。

## 各检验的效应量单位

| 检验 | `power.py` `test=` | 效应量 | 小 / 中 / 大 |
|------|--------------------|-------------|------------------------|
| 两个独立样本均值 | `t_ind` | Cohen's d | 0.2 / 0.5 / 0.8 |
| 配对 / 单样本 | `t_paired`, `t_one` | Cohen's d (dz) | 0.2 / 0.5 / 0.8 |
| 单因素 ANOVA | `anova` | Cohen's f | 0.1 / 0.25 / 0.4 |
| 两个比例 | `two_proportions` | Cohen's h（由比例自动换算） | 0.2 / 0.5 / 0.8 |
| 单个比例 | `one_proportion` | Cohen's h（自动） | 0.2 / 0.5 / 0.8 |
| 相关 | `correlation` | Pearson r | 0.1 / 0.3 / 0.5 |
| 卡方 | `chi2` | Cohen's w | 0.1 / 0.3 / 0.5 |
| 回归（ΔR²） | `linear_regression` | Cohen's f² | 0.02 / 0.15 / 0.35 |

基准值是最后手段的约定 — 优先使用最小关注效应。
参见 `effect_sizes.md`。


## 当前主要的 API/源码参考

- [statsmodels power source, v0.15.0](https://github.com/statsmodels/statsmodels/blob/v0.15.0/statsmodels/stats/power.py)：t 检验、正态、ANOVA、卡方与 FTestPowerF2 的契约。
- [statsmodels proportion source, v0.15.0](https://github.com/statsmodels/statsmodels/blob/v0.15.0/statsmodels/stats/proportion.py)：h 与比例 z 检验的近似。
- [Pingouin power source, v0.7.0](https://github.com/raphaelvallat/pingouin/blob/v0.7.0/src/pingouin/power.py)：相关性的近似与方向处理。
- [SciPy binomtest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html) 与 [noncentral F](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ncf.html)。
