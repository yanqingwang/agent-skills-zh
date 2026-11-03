> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/statistical-power/references/simulation_based_power.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 基于模拟（蒙特卡洛）的功效

模拟是在假定的数据生成过程下，对某个指定分析流程所做的估计。当解析方法
遗漏了重要的设计特征时它很有用；但它的可信度完全取决于那些假设。若干 GLM、
整群、重复测量与生存设计确实存在解析近似。当解析方法与估计目标和计划的
分析相匹配时就用它；否则用模拟。

## 配方（始终相同）

1. **模拟**：从你假定的真值中生成一个大小为 *n* 的数据集：你想检出的效应，
   加上真实的结构（基线率、残差 SD、整群随机效应、脱落、协变量分布）。
2. **分析**：用真实研究计划的*确切*模型/检验来分析它。
3. **重复**：重复 R 次。功效 = 检验显著的那部分重复所占的比例。
   用 R ≥ 1,000；在 80% 决策点附近要得到稳定估计，用 5,000–10,000。

始终报告该估计的**蒙特卡洛置信区间**（`scripts/simulate_power.py` 这个运行
框架返回 Wilson 区间）。R = 1,000 时，在 p = 0.8 附近 ±2 SE 的宽度约为
±0.025，因此不要过度解读 0.81 与 0.79 的差别。

## 使用这个运行框架

`scripts/simulate_power.py` 提供了 `simulate_power()` 与 `find_sample_size()`。
你提供一个 `gen_and_test(n, rng) -> bool` 函数，它构建一个数据集、运行分析，
并返回结果是否显著。`rng` 是带种子的 `numpy.random.Generator`，
因此每次重复都会取到新的伪随机抽样。要复现还需要记录软件版本；
带种子的生成器流在未来的 NumPy 版本之间不保证保持一致。

```python
from simulate_power import (simulate_power, find_sample_size,
                            example_two_group_difference)

alpha = 0.05
# n is per group; use this as a runnable template and replace the generator/test.
gen_and_test = example_two_group_difference(effect=0.5, sd=1.0, alpha=alpha)
est = simulate_power(gen_and_test, n=64, n_sims=2000, alpha=alpha, seed=0)
print(est)

# A candidate, not a guarantee of globally minimal n under Monte Carlo noise.
n, est = find_sample_size(gen_and_test, target_power=0.80, n_sims=1000,
                          alpha=alpha, lo=40, hi=100, seed=0, verbose=False)
# Check neighboring sizes with more replicates and an independent seed.
checks = [simulate_power(gen_and_test, n=j, n_sims=5000,
                         alpha=alpha, seed=2026) for j in (n - 1, n, n + 1)]
```

该文件附带四个可改造的示例：两组差异（对照闭式 t 检验的合理性检查）、
logistic 回归、带 ICC 的整群随机化试验，以及重复测量线性混合模型。
复制最接近的一个，然后改写其中的数据生成部分。

## 模拟在什么时候有用

| 设计 / 分析 | 需要纳入的特征 | 要模拟什么 |
|-------------------|----------------|------------------|
| Logistic / Poisson 回归 | 功效取决于完整的协变量分布 | 生成预测变量、计算线性预测子、抽取结局、拟合 GLM |
| 混合效应 / 重复测量 | 随机效应 + 个体内相关 | 抽取受试者/整群随机效应，然后抽取观测值；拟合 `mixedlm` |
| 整群随机化试验 | ICC 抬高方差；整群才是分析单元 | 通过 ICC 抽取整群随机截距；拟合计划中的整群感知分析；检查小整群推断 |
| 生存分析（Cox / log-rank） | 删失与事件时间分布 | 抽取事件时间与删失时间；拟合 `lifelines` 的 CoxPH 或运行 log-rank 检验 |
| 交互项 | 目标是交互对比，而不是任一主效应 | 生成析因结构与交互效应；检验该系数 |
| 中介效应 | 系数乘积的零假设不是正态的 | 模拟路径模型；对间接效应做 bootstrap 或检验 |
| 非标准 / 自定义检验 | 解析假设与设计不匹配 | 你的分析脚本实际在做的任何事情 |

## 关键正确性要点

- **严格按计划分析。** 如果真实分析要调整协变量，就在模拟中把它们也纳入。
  如果它使用稳健标准误或某种特定校正，就在 `gen_and_test` 中照做。
  模拟的全部价值就在于对计划的忠实还原。
- **显式处理估计失败。** 随附示例会检查收敛性、分离/Hessian 失败以及
  p 值是否为有限值。它们对预期内的失败抛出 `SimulationFitError`；
  运行框架把这些运行留在分母中计为未拒绝，并报告 `n_failures` 与
  `failure_reasons`。非预期的异常则向上传播。这样计数失败，定义的是
  无条件的操作性拒绝率；它并不证明统计推断是有效的。
  频繁失败需要修订计划中的分析/设计，而不是悄悄丢掉这些重复。
  警告汇总在 `n_warned` 与 `warning_counts` 中；即使某次拟合报告了收敛，
  也要检查它们的类别。
- **也要盯住 I 类错误。** 作为一项检查，在*零假设*下（效应 = 0）做模拟，
  确认拒绝率 ≈ α。如果它被抬高了（小整群混合模型或朴素的整群标准误中
  常见），那么你计划中的分析是偏保守的（反保守的），在修正分析之前，
  那个功效数字没有意义。
- **把搜索与确认分开。** 固定种子让结果可复现，但既不消除噪声，也不让功效
  随 n 单调。二分查找只是对"功效递增的设计"的一种启发式。请用更大规模的
  运行和全新的种子来确认选定的 n 以及附近可行的分配。在自适应选定的 n 上
  得到的普通 Wilson CI 并未做选择校正。如果离散检验、分配取整或失败导致
  非单调，请改为考察一个网格。
- **把 alpha 留在回调里。** 运行框架会校验它的 `alpha` 参数，但既不把它
  传给回调，也不用来对 p 值设阈值。回调必须返回 bool，
  并且必须使用同一套计划中的阈值/流程；返回原始 p 值会抛出 `TypeError`。
- **区分条件假设。** Logistic 的 `beta` 是按原始预测变量单位计的；
  `base_rate` 是 x=0 时的风险。对该示例而言，`n` 是观测总数；
  对整群示例是每臂的整群数；对重复测量是受试者数。
  混合模型示例使用 REML 随机截距与渐近 Wald 检验；
  它们没有实现小样本自由度校正，也没有实现随机斜率。

## 为真实的复杂情况建模

- **脱落。** 要么直接模拟缺失（按假定机制丢掉行或观测时点，再套用计划中
  的缺失数据分析 — 这估计的是该假定机制下的拒绝率，但它本身并不估计偏倚，
  也不验证 MAR/MNAR 假设），要么算出分析用的 n，再用 `1/(1−dropout)`
  放大入组人数。
- **聚类 / ICC。** 把总方差拆成整群之间（τ²）与残差（σ²）两部分，
  满足 `ICC = τ²/(τ²+σ²)`，抽取整群随机效应 ~ N(0, τ)，并加到该整群的
  每个成员上。参见 `example_cluster_randomized`。
- **不等分配 / 分层。** 生成设计实际会产生的组规模与分层；不要假定设计
  根本无法提供的平衡。
- **重复测量。** 受试者随机截距（必要时还有随机斜率）加上个体内残差；
  只有在随机截距、残差独立且同方差的例子中，相关性才是 `τ²/(τ²+σ²)`。
  随时间变化的残差相关/随机斜率需要更复杂的生成器与拟合。

## 报告一次基于模拟的功效分析

写清楚到别人能重跑的程度：

```text
Power was estimated at [n and its unit] with [R] independent replicates at each
prespecified sample size. The generator assumed [effect in raw units], [covariate
distribution], [conditional baseline risk / residual variance], [ICC, cluster sizes],
and [dropout/censoring]. The analysis used [model, estimand, test, multiplicity rule],
matching the protocol. At alpha [value], [hits]/[all R] runs rejected the null
([power], 95% Wilson Monte Carlo CI [low, high]); [failures] fits failed and were
retained as non-rejections. Warning categories were [counts]. Null simulations
at the same design gave [Type I error and MC CI]. Candidate n was confirmed with
[fresh seed and R]. Assumption sensitivity covered [ranges]. Code/versions: [link].
```

把每个方括号都替换为实际执行的结果；本模板不含任何虚构的研究结局。
蒙特卡洛 CI 量化的是固定假设下的抽样噪声，
而不是效应量、干扰参数或总体可推广性上的不确定性。

## 当前主要来源与执行范围

审阅于 2026-10-01；随附的四个生成器都在小规模合成数据上运行过，
使用 statsmodels 0.15.0 / SciPy 1.18.1 / NumPy 2.5.3 / pandas 2.3.3。
合并方差 t 检验带有原生的零假设/功效校准检查；其他模型只做了小规模冒烟
运行，用于验证软件机制，而非研究特定的 I 类错误或样本量是否充分。

- [SciPy ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)：合并方差对应 `equal_var=True`；Welch 是另一种分析。
- [statsmodels Logit.fit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Logit.fit.html)、[MixedLM.fit](https://www.statsmodels.org/stable/generated/statsmodels.regression.mixed_linear_model.MixedLM.fit.html) 与 [fit pitfalls](https://www.statsmodels.org/stable/pitfalls.html)。
- [NumPy Generator](https://numpy.org/doc/stable/reference/random/generator.html)：RNG 方法与版本兼容性。
- [lifelines statistics](https://lifelines.readthedocs.io/en/latest/lifelines.statistics.html)：logrank 检验，`sample_size_necessary_under_cph` / `power_under_cph` 提供特定的比例风险近似。[CoxPHFitter](https://lifelines.readthedocs.io/en/latest/fitters/regression/CoxPHFitter.html) 支持右删失的时间/事件拟合。这些生存分析扩展只是指引，并非随附的、经过校准的生存生成器；信息性删失与非比例风险需要额外的建模。
- [Arnold et al. (2011)](https://doi.org/10.1186/1471-2288-11-94)：模拟设计与报告。
