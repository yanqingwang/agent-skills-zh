> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/researcher/science/statsmodels/references/stats_diagnostics.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 统计检验与诊断参考

本文件全面介绍 statsmodels 中的统计检验、诊断与工具。

## 概览

Statsmodels 提供丰富的统计检验能力：
- 残差诊断与设定检验
- 假设检验（参数与非参数）
- 拟合优度检验
- 多重比较与事后检验
- 功效与样本量计算
- 稳健协方差矩阵
- 影响点与异常值检测

各片段需要对应的结果类型与对齐的输入；OLS 诊断不能自动套用到 GLM 或相关观测上。假设检验不显著并不等于验证了它的原假设。要按研究设计预先确定推断目标与协方差，而不是做完一串预检验后再挑推断方式。VIF/影响点阈值只是筛查经验法则，条件数还取决于单位。

## 残差诊断

### 自相关检验

**Ljung-Box 检验**：检验残差中的自相关

```python
from statsmodels.stats.diagnostic import acorr_ljungbox

# Test residuals for autocorrelation
lb_test = acorr_ljungbox(residuals, lags=10, return_df=True)
print(lb_test)

# H0: No autocorrelation up to lag k
# If p-value < 0.05, reject H0 (autocorrelation present)
```

**Durbin-Watson 检验**：检验一阶自相关

```python
from statsmodels.stats.stattools import durbin_watson

dw_stat = durbin_watson(residuals)
print(f"Durbin-Watson: {dw_stat:.4f}")

# DW ≈ 2: no autocorrelation
# DW < 2: positive autocorrelation
# DW > 2: negative autocorrelation
# Exact critical values depend on n and k
```

**Breusch-Godfrey 检验**：更一般的自相关检验

```python
from statsmodels.stats.diagnostic import acorr_breusch_godfrey

bg_test = acorr_breusch_godfrey(results, nlags=5, result_object=True)
lm_stat, lm_pval = bg_test.lm, bg_test.lmpval

print(f"LM statistic: {lm_stat:.4f}, p-value: {lm_pval:.4f}")
# H0: No autocorrelation up to lag k
```

### 异方差检验

**Breusch-Pagan 检验**：检验异方差

```python
from statsmodels.stats.diagnostic import het_breuschpagan

bp_test = het_breuschpagan(residuals, exog)
lm_stat, lm_pval, f_stat, f_pval = bp_test

print(f"Breusch-Pagan test p-value: {lm_pval:.4f}")
# H0: Homoskedasticity (constant variance)
# If p-value < 0.05, reject H0 (heteroskedasticity present)
```

**White 检验**：更一般的异方差检验

```python
from statsmodels.stats.diagnostic import het_white

white_test = het_white(residuals, exog)
lm_stat, lm_pval, f_stat, f_pval = white_test

print(f"White test p-value: {lm_pval:.4f}")
# H0: Homoskedasticity
```

**ARCH 检验**：检验自回归条件异方差

```python
from statsmodels.stats.diagnostic import het_arch

arch_test = het_arch(residuals, nlags=5, result_object=True)
lm_stat, lm_pval = arch_test.lm, arch_test.lmpval

print(f"ARCH test p-value: {lm_pval:.4f}")
# H0: No ARCH effects
# If significant, consider GARCH model
```

### 正态性检验

**Jarque-Bera 检验**：用偏度与峰度检验正态性

```python
from statsmodels.stats.stattools import jarque_bera

jb_stat, jb_pval, skew, kurtosis = jarque_bera(residuals)

print(f"Jarque-Bera statistic: {jb_stat:.4f}")
print(f"p-value: {jb_pval:.4f}")
print(f"Skewness: {skew:.4f}")
print(f"Kurtosis: {kurtosis:.4f}")

# H0: Residuals are normally distributed
# Normal: skewness ≈ 0, kurtosis ≈ 3
```

**Omnibus 检验**：另一种正态性检验（同样基于偏度/峰度）

```python
from statsmodels.stats.stattools import omni_normtest

omni_stat, omni_pval = omni_normtest(residuals)
print(f"Omnibus test p-value: {omni_pval:.4f}")
# H0: Normality
```

**Anderson-Darling 检验**：分布拟合检验

```python
from statsmodels.stats.diagnostic import normal_ad

ad_stat, ad_pval = normal_ad(residuals)
print(f"Anderson-Darling test p-value: {ad_pval:.4f}")
```

**Lilliefors 检验**：修正的 Kolmogorov-Smirnov 检验

```python
from statsmodels.stats.diagnostic import lilliefors

lf_stat, lf_pval = lilliefors(residuals, dist='norm')
print(f"Lilliefors test p-value: {lf_pval:.4f}")
```

### 线性与设定检验

**Ramsey RESET 检验**：检验函数形式设定错误

```python
from statsmodels.stats.diagnostic import linear_reset

reset_test = linear_reset(results, power=2, use_f=True)
f_stat, f_pval = reset_test.fvalue, reset_test.pvalue

print(f"RESET test p-value: {f_pval:.4f}")
# H0: the added nonlinear terms have zero coefficients; not a general validity test
# If rejected, may need polynomial terms or transformations
```

**Harvey-Collier 检验**：检验线性

```python
from statsmodels.stats.diagnostic import linear_harvey_collier

hc_stat, hc_pval = linear_harvey_collier(results)
print(f"Harvey-Collier test p-value: {hc_pval:.4f}")
# H0: Linear specification is correct
```

## 多重共线性检测

**方差膨胀因子（VIF）**：

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd

# Calculate VIF for each variable
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                   for i in range(X.shape[1])]

print(vif_data.sort_values('VIF', ascending=False))

# Interpretation:
# VIF = 1: No correlation with other predictors
# VIF > 5: Moderate multicollinearity
# VIF > 10: Serious multicollinearity problem
# VIF > 20: Severe multicollinearity (consider removing variable)
```

**条件数**：来自回归结果

```python
print(f"Condition number: {results.condition_number:.2f}")

# Interpretation:
# < 10: No multicollinearity concern
# 10-30: Moderate multicollinearity
# > 30: Strong multicollinearity
# > 100: Severe multicollinearity
```

## 影响点与异常值检测

### 杠杆值

高杠杆点的预测变量取值极端。

```python
from statsmodels.stats.outliers_influence import OLSInfluence

influence = results.get_influence()

# Hat values (leverage)
leverage = influence.hat_matrix_diag

# Rule of thumb: leverage > 2*p/n or 3*p/n is high
# p = number of parameters, n = sample size
threshold = 2 * len(results.params) / len(y)
high_leverage = np.where(leverage > threshold)[0]

print(f"High leverage observations: {high_leverage}")
```

### Cook's Distance

衡量每个观测的整体影响。

```python
# Cook's distance
cooks_d = influence.cooks_distance[0]

# Rule of thumb: Cook's D > 4/n is influential
threshold = 4 / len(y)
influential = np.where(cooks_d > threshold)[0]

print(f"Influential observations (Cook's D): {influential}")

# Plot
import matplotlib.pyplot as plt
plt.stem(range(len(cooks_d)), cooks_d)
plt.axhline(y=threshold, color='r', linestyle='--', label=f'Threshold (4/n)')
plt.xlabel('Observation')
plt.ylabel("Cook's Distance")
plt.legend()
plt.show()
```

### DFFITS

衡量对拟合值的影响。

```python
# DFFITS
dffits = influence.dffits[0]

# Rule of thumb: |DFFITS| > 2*sqrt(p/n) is influential
p = len(results.params)
n = len(y)
threshold = 2 * np.sqrt(p / n)

influential_dffits = np.where(np.abs(dffits) > threshold)[0]
print(f"Influential observations (DFFITS): {influential_dffits}")
```

### DFBETAs

衡量对每个系数的影响。

```python
# DFBETAs (one for each parameter)
dfbetas = influence.dfbetas

# Rule of thumb: |DFBETA| > 2/sqrt(n)
threshold = 2 / np.sqrt(n)

for i, param_name in enumerate(results.params.index):
    influential = np.where(np.abs(dfbetas[:, i]) > threshold)[0]
    if len(influential) > 0:
        print(f"Influential for {param_name}: {influential}")
```

### 影响点图

```python
from statsmodels.graphics.regressionplots import influence_plot

fig, ax = plt.subplots(figsize=(12, 8))
influence_plot(results, ax=ax, criterion='cooks')
plt.show()

# Combines leverage, residuals, and Cook's distance
# Large bubbles = high Cook's distance
# Far from x=0 = high leverage
# Far from y=0 = large residual
```

### 学生化残差

```python
# Studentized residuals (outliers)
student_resid = influence.resid_studentized_internal

# Externally studentized residuals use the leave-one-out variance estimate
student_resid_external = influence.resid_studentized_external

# Outliers: |studentized residual| > 3 (or > 2.5)
outliers = np.where(np.abs(student_resid_external) > 3)[0]
print(f"Outliers: {outliers}")
```

## 假设检验

### t 检验

**单样本 t 检验**：检验均值是否等于某个特定值

```python
from scipy import stats

# H0: population mean = mu_0
t_stat, p_value = stats.ttest_1samp(data, popmean=mu_0)

print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

**双样本 t 检验**：比较两组的均值

```python
# H0: mean1 = mean2 (equal variances)
t_stat, p_value = stats.ttest_ind(group1, group2)

# Welch's t-test (unequal variances)
t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)

print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

**配对 t 检验**：比较配对观测

```python
# H0: mean difference = 0
t_stat, p_value = stats.ttest_rel(before, after)

print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

### 比例检验

**单比例检验**：

```python
from statsmodels.stats.proportion import proportions_ztest

# H0: proportion = p0
count = 45  # successes
nobs = 100  # total observations
p0 = 0.5    # hypothesized proportion

z_stat, p_value = proportions_ztest(count, nobs, value=p0, prop_var=p0)

print(f"z-statistic: {z_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

**双比例检验**：

```python
# H0: proportion1 = proportion2
counts = [45, 60]
nobs = [100, 120]

z_stat, p_value = proportions_ztest(counts, nobs)
print(f"z-statistic: {z_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

### 卡方检验

**卡方独立性检验**：

```python
from scipy.stats import chi2_contingency

# Contingency table
contingency_table = pd.crosstab(variable1, variable2)

chi2, p_value, dof, expected = chi2_contingency(contingency_table)

print(f"Chi-square statistic: {chi2:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Degrees of freedom: {dof}")

# H0: Variables are independent
```

**卡方拟合优度**：

```python
from scipy.stats import chisquare

# Observed frequencies
observed = [20, 30, 25, 25]

# Expected frequencies (equal by default)
expected = [25, 25, 25, 25]

chi2, p_value = chisquare(observed, expected)

print(f"Chi-square statistic: {chi2:.4f}")
print(f"p-value: {p_value:.4f}")

# H0: Data follow the expected distribution
```

### 非参数检验

**Mann-Whitney U 检验**（独立样本）：

```python
from scipy.stats import mannwhitneyu

# H0: Distributions are equal
u_stat, p_value = mannwhitneyu(group1, group2, alternative='two-sided')

print(f"U statistic: {u_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

**Wilcoxon 符号秩检验**（配对样本）：

```python
from scipy.stats import wilcoxon

# H0: the paired-difference distribution is symmetric about zero
w_stat, p_value = wilcoxon(before, after)

print(f"W statistic: {w_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

**Kruskal-Wallis H 检验**（多于 2 组）：

```python
from scipy.stats import kruskal

# H0: All groups have same distribution
h_stat, p_value = kruskal(group1, group2, group3)

print(f"H statistic: {h_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

**符号检验**：

```python
from statsmodels.stats.descriptivestats import sign_test

# H0: Median = m0
result = sign_test(data, mu0=0)
print(result)
```

### ANOVA

**单因素 ANOVA**：

```python
from scipy.stats import f_oneway

# H0: All group means are equal
f_stat, p_value = f_oneway(group1, group2, group3)

print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

**双因素 ANOVA**（用 statsmodels）：

```python
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# Fit model
model = ols('response ~ C(factor1) + C(factor2) + C(factor1):C(factor2)',
            data=df).fit()

# ANOVA table
anova_table = anova_lm(model, typ=2)
print(anova_table)
```

**重复测量 ANOVA**：

```python
from statsmodels.stats.anova import AnovaRM

# Fully balanced within-subject data; no between-subject effects or sphericity correction
aovrm = AnovaRM(df, depvar='score', subject='subject_id', within=['time'])
results = aovrm.fit()

print(results.summary())
```

## 多重比较

### 事后检验

**Tukey's HSD**（Honest Significant Difference）：

```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Perform Tukey HSD test
tukey = pairwise_tukeyhsd(data, groups, alpha=0.05, use_var="equal")
# In statsmodels 0.15+, unequal variances use Games-Howell:
games_howell = pairwise_tukeyhsd(data, groups, alpha=0.05, use_var="unequal")

print(tukey.summary())

# Plot confidence intervals
tukey.plot_simultaneous()
plt.show()
```

**Bonferroni 校正**：

```python
from statsmodels.stats.multitest import multipletests

# P-values from multiple tests
p_values = [0.01, 0.03, 0.04, 0.15, 0.001]

# Apply correction
reject, pvals_corrected, alphac_sidak, alphac_bonf = multipletests(
    p_values,
    alpha=0.05,
    method='bonferroni'
)

print("Rejected:", reject)
print("Corrected p-values:", pvals_corrected)
```

**错误发现率（FDR）**：

```python
# FDR correction (less conservative than Bonferroni)
reject, pvals_corrected, alphac_sidak, alphac_bonf = multipletests(
    p_values,
    alpha=0.05,
    method='fdr_bh'  # Benjamini-Hochberg
)

print("Rejected:", reject)
print("Corrected p-values:", pvals_corrected)
```

## 稳健协方差矩阵

### 异方差一致（HC）标准误

```python
# After fitting OLS
results = sm.OLS(y, X).fit()

# HC0 (White's heteroskedasticity-consistent SEs)
results_hc0 = results.get_robustcov_results(cov_type='HC0')

# HC1 (degrees of freedom adjustment)
results_hc1 = results.get_robustcov_results(cov_type='HC1')

# HC2 (leverage adjustment)
results_hc2 = results.get_robustcov_results(cov_type='HC2')

# HC3 uses squared leverage adjustment; it is not a universal small-sample guarantee
results_hc3 = results.get_robustcov_results(cov_type='HC3')

print("Standard OLS SEs:", results.bse)
print("Robust HC3 SEs:", results_hc3.bse)
```

### HAC（异方差与自相关一致）

**Newey-West 标准误**：

```python
# For time series with autocorrelation and heteroskedasticity
results_hac = results.get_robustcov_results(cov_type='HAC', maxlags=4)

print("HAC (Newey-West) SEs:", results_hac.bse)
print(results_hac.summary())
```

### 整群稳健标准误

```python
# For clustered/grouped data
results_cluster = results.get_robustcov_results(
    cov_type='cluster',
    groups=cluster_ids
)

print("Cluster-robust SEs:", results_cluster.bse)
```

## 描述统计

**基本描述统计**：

```python
from statsmodels.stats.api import DescrStatsW

# Comprehensive descriptive stats
desc = DescrStatsW(data)

print("Mean:", desc.mean)
print("Std Dev:", desc.std)
print("Variance:", desc.var)
print("Confidence interval:", desc.tconfint_mean())

# Quantiles
print("Median:", desc.quantile(0.5))
quartiles = desc.quantile([0.25, 0.75], return_pandas=False)
print("IQR:", quartiles[1] - quartiles[0])
```

**加权统计**：

```python
# With weights
desc_weighted = DescrStatsW(data, weights=weights)

print("Weighted mean:", desc_weighted.mean)
print("Weighted std:", desc_weighted.std)
```

**比较两组**：

```python
from statsmodels.stats.weightstats import CompareMeans

# Create comparison object
cm = CompareMeans(DescrStatsW(group1), DescrStatsW(group2))

# t-test
print("t-test:", cm.ttest_ind())

# Confidence interval for difference
print("CI for difference:", cm.tconfint_diff())

# For an independent-samples variance check, use SciPy (not a CompareMeans method):
from scipy.stats import levene
print("Brown-Forsythe:", levene(group1, group2, center="median"))
```

## 功效分析与样本量

**t 检验的功效**：

```python
from statsmodels.stats.power import tt_ind_solve_power

# Solve for sample size
effect_size = 0.5  # Cohen's d
alpha = 0.05
power = 0.8

n = tt_ind_solve_power(effect_size=effect_size,
                        alpha=alpha,
                        power=power,
                        alternative='two-sided')

print(f"Required sample size per group: {int(np.ceil(n))}")

# Solve for power given n
power = tt_ind_solve_power(effect_size=0.5,
                           nobs1=50,
                           alpha=0.05,
                           alternative='two-sided')

print(f"Power: {power:.4f}")
```

**比例检验的功效**：

```python
from statsmodels.stats.power import zt_ind_solve_power

# For proportion tests (z-test)
from statsmodels.stats.proportion import proportion_effectsize
effect_size = proportion_effectsize(0.5, 0.35)  # Cohen's h, not raw difference
alpha = 0.05
power = 0.8

n = zt_ind_solve_power(effect_size=effect_size,
                        alpha=alpha,
                        power=power,
                        alternative='two-sided')

print(f"Required sample size per group: {int(np.ceil(n))}")
```

**功效曲线**：

```python
from statsmodels.stats.power import TTestIndPower
import matplotlib.pyplot as plt

# Create power analysis object
analysis = TTestIndPower()

# Plot power curves for different sample sizes
sample_sizes = range(10, 200, 10)
effect_sizes = [0.2, 0.5, 0.8]  # Small, medium, large

fig, ax = plt.subplots(figsize=(10, 6))

for es in effect_sizes:
    power = [analysis.solve_power(effect_size=es, nobs1=n, alpha=0.05)
             for n in sample_sizes]
    ax.plot(sample_sizes, power, label=f'Effect size = {es}')

ax.axhline(y=0.8, color='r', linestyle='--', label='Power = 0.8')
ax.set_xlabel('Sample size per group')
ax.set_ylabel('Power')
ax.set_title('Power Curves for Two-Sample t-test')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()
```

## 效应量

**Cohen's d**（标准化均值差）：

```python
def cohens_d(group1, group2):
    """Calculate Cohen's d for independent samples"""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)

    # Pooled standard deviation
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))

    # Cohen's d
    d = (np.mean(group1) - np.mean(group2)) / pooled_std

    return d

d = cohens_d(group1, group2)
print(f"Cohen's d: {d:.4f}")

# Interpretation:
# |d| < 0.2: negligible
# |d| ~ 0.2: small
# |d| ~ 0.5: medium
# |d| ~ 0.8: large
```

**Eta-squared**（用于 ANOVA）：

```python
# From ANOVA table
# For a ONE-WAY ANOVA only: η² = SS_between / SS_total.
# This sum is not a general multifactor type-II/III eta-squared denominator.

def eta_squared(anova_table):
    return anova_table['sum_sq'].iloc[0] / anova_table['sum_sq'].sum()

# After running ANOVA
eta_sq = eta_squared(anova_table)
print(f"Eta-squared: {eta_sq:.4f}")

# Interpretation:
# 0.01: small effect
# 0.06: medium effect
# 0.14: large effect
```

## 列联表与关联性

**McNemar 检验**（配对二值数据）：

```python
from statsmodels.stats.contingency_tables import mcnemar

# 2x2 contingency table
table = [[a, b],
         [c, d]]

result = mcnemar(table, exact=True)  # or exact=False for large samples
print(f"p-value: {result.pvalue:.4f}")

# H0: Marginal probabilities are equal
```

**Cochran-Mantel-Haenszel 检验**：

```python
from statsmodels.stats.contingency_tables import StratifiedTable

# For stratified 2x2 tables
strat_table = StratifiedTable(tables_list)
result = strat_table.test_null_odds()

print(f"p-value: {result.pvalue:.4f}")
```

## 处理效应与因果推断

**处理效应估计**（`TreatmentEffect`）：

```python
import statsmodels.api as sm
from statsmodels.treatment.treatment_effects import TreatmentEffect

# exog: observed confounders (with constant); treatment: 0/1 indicator
exog = sm.add_constant(confounders)
select_model = sm.Probit(treatment, exog)  # treatment (selection) model
outcome_model = sm.OLS(outcome, exog)      # outcome model

te = TreatmentEffect(outcome_model, treatment,
                     results_select=select_model.fit(disp=0))

res = te.ipw()             # inverse probability weighting
print(res.summary_frame())  # ATE and potential-outcome means POM0/POM1 with GMM SEs
print(te.ra().summary_frame())    # regression adjustment
print(te.aipw().summary_frame())  # augmented IPW (doubly robust)
# Also available: te.aipw_wls(), te.ipw_ra() -- both need a 6-parameter
# selection model unless return_results=False; see the caveats below
```

**倾向得分**（用于诊断或自定义加权）：

```python
ps_model = sm.Logit(treatment, exog).fit(disp=0)
propensity_scores = ps_model.predict(exog)
# statsmodels does not implement matching; estimating scores
# alone is not propensity score matching
```

因果注意事项：

- 因果解读需要一致性、无干扰、无未测量混杂与正值性，外加相应估计量/模型的假设
- 检查两组间倾向得分分布的重叠；得分极端接近
  0 或 1 会让 IPW 不稳定
- 加权后检查协变量平衡（如标准化均值差）
- 默认目标是样本 ATE（`effect_group="all"`）。ATT/ATU：
  `te.ipw(effect_group=1)` / `te.ipw(effect_group=0)`（也见 `ra`、`ipw_ra`）。
  `aipw` / `aipw_wls` 不提供
- 结果模型仅支持 OLS（0.15 仍如此）；尚不支持 Logit/Poisson 结果
  变量
- 在已发布的 0.15.0 中核实：`ipw_ra` 与 `aipw_wls` 会抛出 `ValueError` 形状错误，除非
  选择模型恰有 6 个参数；`return_results=False` 跳过
  GMM 步骤，返回不带标准误的 `(ate, pom0, pom1)`。不要
  添加哑协变量来凑够六参数；这是实现层面的限制。

**双重差分**：

```python
# Did formula: outcome ~ treatment * post
model = ols('outcome ~ treatment * post', data=df).fit(
    cov_type='cluster', cov_kwds={'groups': df['unit_id']})

# DiD estimate is the interaction coefficient
did_estimate = model.params['treatment:post']
print(f"DiD estimate: {did_estimate:.4f}")
```

这里展示的 DiD 是简单的两组/两期设计。因果解读还需要平行未处理趋势、无预期/干扰、恰当的抽样，以及有依据的整群层级；该公式不是通用的交错采纳估计量。

## 最佳实践

1. **始终检查假设**：解读结果前先做检验
2. **报告效应量**：不只报 p 值
3. **用恰当的检验**：检验要匹配数据类型与分布
4. **校正多重比较**：检验次数多时
5. **检查样本量**：保证足够功效
6. **目视检查**：检验前先画图
7. **报告置信区间**：与点估计一并给出
8. **考虑替代方案**：假设不成立时用非参数方法
9. **稳健标准误**：存在异方差/自相关时使用
10. **记录决策**：注明用了哪些检验及原因

## 常见陷阱

1. **不检查检验假设**：可能使结果失效
2. **多重检验不做校正**：抬高 Type I error
3. **正态性检验后改估计目标**：秩检验一般并不检验均值差；要明确选定估计目标与抽样假设
4. **忽略异方差**：用稳健 SE
5. **混淆统计显著与实际显著**：查看效应量
6. **不报告置信区间**：只有 p 值不够
7. **用错检验**：检验要匹配研究问题
8. **功效不足**：有 Type II error（假阴性）风险
9. **p-hacking**：反复试多个设定直到显著
10. **过度解读 p 值**：记住 NHST 的局限
