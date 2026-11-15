> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/researcher/science/statsmodels/references/linear_models.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 线性回归模型参考

本文件详细介绍 statsmodels 中的线性回归模型，涵盖 OLS、GLS、WLS、分位数回归与专用变体。

## 核心模型类

### OLS（普通最小二乘）

OLS 估计线性条件均值。常规协方差假设误差同方差且不相关；误差正态时支持精确的小样本 t/F 推断。稳健协方差改变的是不确定性，而非遗漏变量或内生性偏误。

**适用场景：**
- 标准回归分析
- 误差独立且方差恒定
- 无自相关或异方差
- 最常用的起点

**基本用法：**
```python
import statsmodels.api as sm
import numpy as np

# Array interface: add a constant if an intercept is intended
X = sm.add_constant(X_data)  # Adds column of 1s for intercept

# Fit model
model = sm.OLS(y, X)
results = model.fit()

# View results
print(results.summary())
```

**主要结果属性：**
```python
results.params           # Coefficients
results.bse              # Standard errors
results.tvalues          # T-statistics
results.pvalues          # P-values
results.rsquared         # R-squared
results.rsquared_adj     # Adjusted R-squared
results.fittedvalues     # Fitted values (predictions on training data)
results.resid            # Residuals
results.conf_int()       # Confidence intervals for parameters
```

**带置信/预测区间的预测：**
```python
# For in-sample predictions
pred = results.get_prediction(X)
pred_summary = pred.summary_frame()
print(pred_summary)  # Contains mean, std, confidence intervals

# For out-of-sample predictions
X_new = sm.add_constant(X_new_data, has_constant="add")
pred_new = results.get_prediction(X_new)
pred_summary = pred_new.summary_frame()

# Access intervals
mean_ci_lower = pred_summary["mean_ci_lower"]
mean_ci_upper = pred_summary["mean_ci_upper"]
obs_ci_lower = pred_summary["obs_ci_lower"]  # Prediction intervals
obs_ci_upper = pred_summary["obs_ci_upper"]
```

**Formula API（R 风格）：**
```python
import statsmodels.formula.api as smf

# Automatic handling of categorical variables and interactions
formula = 'y ~ x1 + x2 + C(category) + x1:x2'
results = smf.ols(formula, data=df).fit()
```

### WLS（加权最小二乘）

处理异方差误差（对角 Σ），即方差随观测变化。

**适用场景：**
- 已知异方差（误差方差非恒定）
- 不同观测的可靠度不同
- 权重已知或可估计

**用法：**
```python
# If you know the weights (inverse variance)
weights = 1 / error_variance
model = sm.WLS(y, X, weights=weights)
results = model.fit()

# Common weight patterns:
# - 1/variance: when variance is known
# - n_i: sample size for grouped data
# - 1/x: when variance proportional to x
```

**可行 WLS（估计权重）：**
```python
# Step 1: Fit OLS
ols_results = sm.OLS(y, X).fit()

# Step 2: Model squared residuals to estimate variance
abs_resid = np.abs(ols_results.resid)
variance_model = sm.OLS(np.log(np.maximum(abs_resid**2, np.finfo(float).tiny)), X).fit()

# Step 3: Use estimated variance as weights
weights = 1 / np.exp(variance_model.fittedvalues)
wls_results = sm.WLS(y, X, weights=weights).fit()
```

### GLS（广义最小二乘）

处理任意协方差结构（Σ），是其他回归方法的超类。

**适用场景：**
- 协方差结构已知
- 误差相关
- 比 WLS 更一般

**用法：**
```python
# Specify covariance structure
# Sigma should be (n x n) covariance matrix
model = sm.GLS(y, X, sigma=Sigma)
results = model.fit()
```

### GLSAR（带自回归误差的 GLS）

面向时间序列数据的可行广义最小二乘，误差服从 AR(p)。

**适用场景：**
- 误差自相关的时间序列回归
- 需要考虑序列相关
- 误差独立性被破坏

**用法：**
```python
# AR(1) errors
model = sm.GLSAR(y, X, rho=1)  # rho=1 for AR(1), rho=2 for AR(2), etc.
results = model.iterative_fit(maxiter=20)  # Default maxiter=3 may be insufficient

print(results.summary())
print(f"Estimated rho: {results.model.rho}")
```

### RLS（递推最小二乘）

对固定系数回归做扩展窗口估计，并给出稳定性诊断；它不是随机时变系数模型。

**适用场景：**
- 随观测累积评估系数稳定性
- 查看递推残差与 CUSUM
- 用新增数据重新拟合；不要假装有流式更新接口

**用法：**
```python
from statsmodels.regression.recursive_ls import RecursiveLS

model = RecursiveLS(y, X)
results = model.fit()

# Expanding-window filtered/smoothed coefficient estimates
params_over_time = results.recursive_coefficients.filtered
cusum = results.cusum  # CUSUM statistic for structural breaks
```

### Rolling 回归

在移动窗口上计算估计值，用于检测时变参数。

**适用场景：**
- 参数随时间变化
- 想检测结构变化
- 关系不断演变的时间序列

**用法：**
```python
from statsmodels.regression.rolling import RollingOLS, RollingWLS

# Rolling OLS with 60-period window
rolling_model = RollingOLS(y, X, window=60)
rolling_results = rolling_model.fit()

# Extract time-varying parameters
rolling_params = pd.DataFrame(rolling_results.params)  # Also handles NumPy inputs
rolling_rsquared = rolling_results.rsquared

# Plot parameter evolution
import matplotlib.pyplot as plt
rolling_params.plot()
plt.title('Time-Varying Coefficients')
plt.show()
```

### 分位数回归

分析条件分位数，而非条件均值。

**适用场景：**
- 关注分位数（中位数、第 90 百分位等）
- 对异常值稳健（中位数回归）
- 跨分位数的分布效应
- 异质效应

**用法：**
```python
from statsmodels.regression.quantile_regression import QuantReg

# Median regression (50th percentile)
model = QuantReg(y, X)
results_median = model.fit(q=0.5)

# Multiple quantiles
quantiles = [0.1, 0.25, 0.5, 0.75, 0.9]
results_dict = {}
for q in quantiles:
    results_dict[q] = model.fit(q=q)

# Plot quantile-varying effects
import matplotlib.pyplot as plt
coef_dict = {q: res.params for q, res in results_dict.items()}
coef_df = pd.DataFrame(coef_dict).T
coef_df.plot()
plt.xlabel('Quantile')
plt.ylabel('Coefficient')
plt.show()
```

## 混合效应模型

用于带随机效应的分层/嵌套数据。

**适用场景：**
- 整群/分组数据（学校里的学生、医院里的患者）
- 重复测量
- 需要随机效应来解释分组

**用法：**
```python
from statsmodels.regression.mixed_linear_model import MixedLM

# Random intercept model
model = MixedLM(y, X, groups=group_ids)
results = model.fit()

# Random intercept and slope
model = MixedLM(y, X, groups=group_ids, exog_re=X_random)
results = model.fit()

print(results.summary())
```

比较固定效应不同的混合模型时用 ML（`fit(reml=False)`）；这些设计之间 REML 似然不可比。推断前要检查收敛、随机效应协方差奇异与方差估计落在边界的情况。

## 诊断与模型评估

以下诊断使用一个 OLS 结果及其原始满秩设计。VIF、Cook's distance 与条件数阈值只是筛查经验法则，不是自动剔除规则；条件数还取决于预测变量的单位。稳健 SE 并不能在异方差下验证经典 OLS 的观测区间。

### 残差分析

```python
# Basic residual plots
import matplotlib.pyplot as plt

# Residuals vs fitted
plt.scatter(results.fittedvalues, results.resid)
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.axhline(y=0, color='r', linestyle='--')
plt.title('Residuals vs Fitted')
plt.show()

# Q-Q plot for normality
from statsmodels.graphics.gofplots import qqplot
qqplot(results.resid, line='s')
plt.show()

# Histogram of residuals
plt.hist(results.resid, bins=30, edgecolor='black')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Distribution of Residuals')
plt.show()
```

### 设定检验

```python
from statsmodels.stats.diagnostic import het_breuschpagan, het_white
from statsmodels.stats.stattools import durbin_watson, jarque_bera

# Heteroscedasticity tests
lm_stat, lm_pval, f_stat, f_pval = het_breuschpagan(results.resid, X)
print(f"Breusch-Pagan test p-value: {lm_pval}")

# White test
white_test = het_white(results.resid, X)
print(f"White test p-value: {white_test[1]}")

# Autocorrelation
dw_stat = durbin_watson(results.resid)
print(f"Durbin-Watson statistic: {dw_stat}")
# DW ~ 2 indicates no autocorrelation
# DW < 2 suggests positive autocorrelation
# DW > 2 suggests negative autocorrelation

# Normality test
jb_stat, jb_pval, skew, kurtosis = jarque_bera(results.resid)
print(f"Jarque-Bera test p-value: {jb_pval}")
```

### 多重共线性

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Calculate VIF for each variable
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif_data)
# VIF > 10 indicates problematic multicollinearity
# VIF > 5 suggests moderate multicollinearity

# Condition number (from summary)
print(f"Condition number: {results.condition_number}")
# Condition number > 20 suggests multicollinearity
# Condition number > 30 indicates serious problems
```

### 影响点统计量

```python
from statsmodels.stats.outliers_influence import OLSInfluence

influence = results.get_influence()

# Leverage (hat values)
leverage = influence.hat_matrix_diag
# High leverage: > 2*p/n (p=predictors, n=observations)

# Cook's distance
cooks_d = influence.cooks_distance[0]
# Influential if Cook's D > 4/n

# DFFITS
dffits = influence.dffits[0]
# Influential if |DFFITS| > 2*sqrt(p/n)

# Create influence plot
from statsmodels.graphics.regressionplots import influence_plot
fig, ax = plt.subplots(figsize=(12, 8))
influence_plot(results, ax=ax)
plt.show()
```

### 假设检验

```python
# Test single coefficient
# H0: beta_i = 0 (automatically in summary)

# Test multiple restrictions using F-test
# Example: Test beta_1 = beta_2 = 0
R = [[0, 1, 0, 0], [0, 0, 1, 0]]  # Restriction matrix
f_test = results.f_test(R)
print(f_test)

# Formula-based hypothesis testing
f_test = results.f_test("x1 = x2 = 0")
print(f_test)

# Test linear combination: beta_1 + beta_2 = 1
r_matrix = [[0, 1, 1, 0]]
q_matrix = [1]  # RHS value
f_test = results.f_test((r_matrix, q_matrix))
print(f_test)

# Wald test (equivalent to F-test for linear restrictions)
wald_test = results.wald_test(R)
print(wald_test)
```

## 模型比较

```python
# Classical nested OLS F-test: same observations, larger model second
from statsmodels.stats.anova import anova_lm

# Fit restricted and unrestricted models
model_restricted = sm.OLS(y, X_restricted).fit()
model_full = sm.OLS(y, X_full).fit()

# ANOVA table for model comparison
anova_results = anova_lm(model_restricted, model_full)
print(anova_results)

# AIC/BIC for non-nested model comparison
print(f"Model 1 AIC: {model1.aic}, BIC: {model1.bic}")
print(f"Model 2 AIC: {model2.aic}, BIC: {model2.bic}")
# Lower AIC/BIC indicates better model
```

## 稳健标准误

在不重新加权的情况下处理异方差或整群结构。

```python
# Heteroscedasticity-robust (HC) standard errors
results_hc = results.get_robustcov_results(cov_type='HC0')  # White's
results_hc1 = results.get_robustcov_results(cov_type='HC1')
results_hc2 = results.get_robustcov_results(cov_type='HC2')
results_hc3 = results.get_robustcov_results(cov_type='HC3')  # Leverage-adjusted

# Newey-West HAC (Heteroscedasticity and Autocorrelation Consistent)
results_hac = results.get_robustcov_results(cov_type='HAC', maxlags=4)

# Cluster-robust standard errors
results_cluster = results.get_robustcov_results(cov_type='cluster',
                                                groups=cluster_ids)

# View robust results
print(results_hc3.summary())
```

## 最佳实践

1. **截距只设一次**：数组版模型要显式加；公式默认包含。预测列要保持训练时的顺序。
2. **检查假设**：跑诊断检验（异方差、自相关、正态性）
3. **分类变量用 formula API**：`smf.ols()` 会自动处理分类变量
4. **稳健标准误**：检出异方差但模型设定正确时使用
5. **模型选择**：非嵌套用 AIC/BIC，嵌套用 F 检验/似然比
6. **异常值与影响点**：始终检查 Cook's distance 与杠杆值
7. **多重共线性**：解读前先看 VIF 与条件数
8. **时间序列**：误差自相关时用 `GLSAR` 或稳健 HAC 标准误
9. **分组数据**：考虑混合效应模型或整群稳健标准误
10. **分位数回归**：需要稳健估计或关注分布效应时使用

## 常见陷阱

1. **忘记加常数项**：得到无截距模型
2. **忽略异方差**：用 WLS 或稳健标准误
3. **误差自相关仍用 OLS**：用 GLSAR 或 HAC 标准误
4. **多重共线性下过度解读**：先查 VIF
5. **不检查残差**：始终画残差对拟合值图
6. **秩亏**：检查设计矩阵秩与奇异值；伪逆拟合可能对不可识别设计也返回系数
7. **混淆预测区间与置信区间**：预测区间更宽
8. **分类变量处理不当**：用 formula API 或手工哑变量编码
9. **比较样本量不同的模型**：确保用同一批观测
10. **忽略影响点**：检查 Cook's distance 与 DFFITS
