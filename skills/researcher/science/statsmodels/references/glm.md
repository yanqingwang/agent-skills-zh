> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/researcher/science/statsmodels/references/glm.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 广义线性模型（GLM）参考

本文件全面介绍 statsmodels 中的广义线性模型，涵盖分布族、连接函数与应用。

## 概览

GLM 通过以下几点把线性回归推广到非正态的响应分布：
1. **分布族**：指定响应的条件分布
2. **连接函数**：把条件均值映射到线性预测子；逆连接再映射回去
3. **方差函数**：把方差与均值关联起来

**一般形式**：g(μ) = Xβ，其中 g 为连接函数，μ = E(Y|X)

## 何时使用 GLM

- **二值结果**：Logistic 回归（Binomial 族配 logit 连接）
- **计数数据**：Poisson 或负二项回归
- **正的连续数据**：Gamma 或 Inverse Gaussian
- **条件均值/方差结构**：按响应机制选分布族，而不是对边际响应做正态性检验
- **连接函数**：预测变量与响应尺度之间需要非线性关系

公式预测接收带列名的原始列；数组预测接收与训练完全一致的设计矩阵。后续片段不要复用来自其他分布族的结果。使用正的有限 exposure，传 `exposure=e` 或 `offset=np.log(e)`（不要两者都传），预测新行时也要提供新的 exposure/offset。Binomial 比例需要试验次数（`var_weights=n`）或两列 `[successes, failures]` 响应；任意比例并不是 Bernoulli 观测。

## 分布族

### Binomial 族

用于二值结果（0/1）或比例（k/n）。

**适用场景：**
- 二值分类
- 成功/失败结果
- 比例或率

**常用连接：**
- Logit（默认）：log(μ/(1-μ))
- Probit：Φ⁻¹(μ)
- Log：log(μ)

```python
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Binary logistic regression
model = sm.GLM(y, X, family=sm.families.Binomial())
results = model.fit()

# Formula API
results = smf.glm('success ~ x1 + x2', data=df,
                  family=sm.families.Binomial()).fit()

# Access predictions (probabilities)
probs = results.predict(new_df)  # Raw named predictors after a formula fit

# Classification (0.5 threshold)
predictions = (probs > 0.5).astype(int)
```

**解读：**
```python
import numpy as np

# Odds ratios (for logit link)
odds_ratios = np.exp(results.params)
print("Odds ratios:", odds_ratios)

# For 1-unit increase in x, odds multiply by exp(beta)
```

### Poisson 族

用于计数数据（非负整数）。

**适用场景：**
- 计数结果（事件数）
- 稀有事件
- 率建模（带 offset）

**常用连接：**
- Log（默认）：log(μ)
- Identity：μ
- Sqrt：√μ

```python
# Poisson regression
model = sm.GLM(y, X, family=sm.families.Poisson())
results = model.fit()

# With exposure/offset for rates
# If modeling rate = counts/exposure
model = sm.GLM(y, X, family=sm.families.Poisson(),
               offset=np.log(exposure))
results = model.fit()

# Interpretation: exp(beta) = multiplicative effect on expected count
import numpy as np
rate_ratios = np.exp(results.params)
print("Rate ratios:", rate_ratios)
```

**过度离散检查：**
```python
# Pearson dispersion is a screening statistic, not a calibrated universal test
overdispersion = results.pearson_chi2 / results.df_resid
print(f"Overdispersion: {overdispersion}")

# If >> 1, consider Negative Binomial
if overdispersion > 1.5:
    print("Consider Negative Binomial model for overdispersion")
```

### 负二项族

用于过度离散的计数数据。

**适用场景：**
- 方差 > 均值的计数数据
- 零值过多或方差很大
- Poisson 模型显示过度离散

```python
# Negative Binomial GLM with fixed alpha
model = sm.GLM(y, X, family=sm.families.NegativeBinomial(alpha=1.0))
results = model.fit()

# Use the discrete count model when alpha should be estimated
from statsmodels.discrete.discrete_model import NegativeBinomial
nb_model = NegativeBinomial(y, X)
nb_results = nb_model.fit()

print(f"Dispersion parameter alpha: {np.asarray(nb_results.params)[-1]}")
```

### Gaussian 族

等价于 OLS，但用 IRLS（迭代重加权最小二乘）拟合。

**适用场景：**
- 想用 GLM 框架保持一致
- 需要稳健标准误
- 与其他 GLM 比较

**常用连接：**
- Identity（默认）：μ
- Log：log(μ)
- Inverse：1/μ

```python
# Gaussian GLM (equivalent to OLS)
model = sm.GLM(y, X, family=sm.families.Gaussian())
results = model.fit()

# Verify equivalence with OLS
ols_results = sm.OLS(y, X).fit()
print("Parameters close:", np.allclose(results.params, ols_results.params))
```

### Gamma 族

用于正的连续数据，常呈右偏。

**适用场景：**
- 正的结果（保险理赔、生存时间）
- 右偏分布
- 方差与均值² 成正比

**常用连接：**
- Inverse（默认）：1/μ
- Log：log(μ)
- Identity：μ

```python
# Gamma regression (common for cost data)
model = sm.GLM(y, X, family=sm.families.Gamma())
results = model.fit()

# Log link often preferred for interpretation
model = sm.GLM(y, X, family=sm.families.Gamma(link=sm.families.links.Log()))
results = model.fit()

# With log link, exp(beta) = multiplicative effect
import numpy as np
effects = np.exp(results.params)
```

### Inverse Gaussian 族

用于具有特定方差结构的正连续数据。

**适用场景：**
- 正偏结果
- 方差与均值³ 成正比
- Gamma 的替代

**常用连接：**
- Inverse squared（默认）：1/μ²
- Log：log(μ)

```python
model = sm.GLM(y, X, family=sm.families.InverseGaussian())
results = model.fit()
```

### Tweedie 族

灵活的分布族，涵盖多种分布。

**适用场景：**
- 保险理赔（零值与连续值混合）
- 半连续数据
- 需要灵活的方差函数

**特例（幂参数 p）：**
- p=0：Normal
- p=1：Poisson
- p=2：Gamma
- p=3：Inverse Gaussian
- 1<p<2：复合 Poisson-Gamma（保险常用）

```python
# Tweedie with power=1.5
model = sm.GLM(y, X, family=sm.families.Tweedie(link=sm.families.links.Log(),
                                                 var_power=1.5))
results = model.fit()
```

## 连接函数

连接函数把线性预测子与响应均值联系起来。

### 可用连接

```python
from statsmodels.genmod import families

# Identity: g(μ) = μ
link = families.links.Identity()

# Log: g(μ) = log(μ)
link = families.links.Log()

# Logit: g(μ) = log(μ/(1-μ))
link = families.links.Logit()

# Probit: g(μ) = Φ⁻¹(μ)
link = families.links.Probit()

# Complementary log-log: g(μ) = log(-log(1-μ))
link = families.links.CLogLog()

# Inverse: g(μ) = 1/μ
link = families.links.InversePower()

# Inverse squared: g(μ) = 1/μ²
link = families.links.InverseSquared()

# Square root: g(μ) = √μ
link = families.links.Sqrt()

# Power: g(μ) = μ^p
link = families.links.Power(power=2)
```

### 选择连接函数

**常见默认连接**（在这些分布族下按惯例缩放即为 canonical link）：
- Binomial → Logit
- Poisson → Log
- Gamma → Inverse
- Gaussian → Identity
- Inverse Gaussian → Inverse squared

默认的 Gamma inverse 连接与 binomial 的 log/identity 连接在某些设计下可能越出响应定义域。要检查警告、拟合均值有限性与支撑集；优化器收敛并不能把无效均值变有效。适当时改用正值均值连接。

**何时使用非 canonical：**
- **Binomial 配 Log 连接**：得到 risk ratio 而非 odds ratio
- **Identity 连接**：直接的加性效应（在合理时）
- **Probit 与 Logit**：结果相近，按领域偏好选择
- **CLogLog**：非对称关系，生存分析常用

```python
# Example: Risk ratios with log-binomial model
model = sm.GLM(y, X, family=sm.families.Binomial(link=sm.families.links.Log()))
results = model.fit()

# exp(beta) now gives risk ratios, not odds ratios
risk_ratios = np.exp(results.params)
```

## 模型拟合与结果

### 基本流程

```python
import statsmodels.api as sm

# Add constant
X = sm.add_constant(X_data)

# Specify family and link
family = sm.families.Poisson(link=sm.families.links.Log())

# Fit model using IRLS
model = sm.GLM(y, X, family=family)
results = model.fit()

# Summary
print(results.summary())
```

### 结果属性

```python
# Parameters and inference
results.params              # Coefficients
results.bse                 # Standard errors
results.tvalues            # Z-statistics
results.pvalues            # P-values
results.conf_int()         # Confidence intervals

# Predictions
results.fittedvalues       # Fitted values (μ)
results.predict(X_new)     # Predictions for new data

# Model fit statistics
results.aic                # Akaike Information Criterion
results.bic_llf            # Likelihood-based BIC (GLM .bic can be deviance-based)
results.deviance           # Deviance
results.null_deviance      # Null model deviance
results.pearson_chi2       # Pearson chi-squared statistic
results.df_resid           # Residual degrees of freedom
results.llf                # Log-likelihood

# Residuals
results.resid_response     # Response residuals (y - μ)
results.resid_pearson      # Pearson residuals
results.resid_deviance     # Deviance residuals
results.resid_anscombe     # Anscombe residuals
results.resid_working      # Working residuals
```

### Pseudo R-squared

```python
# Likelihood-based McFadden measure: appropriate for discrete outcomes
pseudo_r2 = results.pseudo_rsquared(kind="mcf")
print(f"McFadden pseudo R²: {pseudo_r2:.4f}")
# Cox-Snell is available for discrete or continuous likelihoods
print("Cox-Snell:", results.pseudo_rsquared(kind="cs"))
# 1 - deviance/null_deviance is a different measure; do not label it McFadden.
```

## 诊断

### 拟合优度

```python
# Chi-square goodness-of-fit approximations need adequate expected cell counts;
# these are not generally calibrated for sparse counts or ungrouped Bernoulli data
from scipy import stats

deviance_pval = stats.chi2.sf(results.deviance, results.df_resid)
print(f"Deviance test p-value: {deviance_pval}")

# Pearson chi-squared test
pearson_pval = stats.chi2.sf(results.pearson_chi2, results.df_resid)
print(f"Pearson chi² test p-value: {pearson_pval}")

# Check for overdispersion/underdispersion
dispersion = results.pearson_chi2 / results.df_resid
print(f"Dispersion: {dispersion}")
# For a Poisson model with an adequate mean, >1 flags extra-Poisson dispersion.
# Gaussian/Gamma/InverseGaussian estimate scale; this ratio need not be 1.
```

### 残差分析

```python
import matplotlib.pyplot as plt

# Deviance residuals vs fitted
plt.figure(figsize=(10, 6))
plt.scatter(results.fittedvalues, results.resid_deviance, alpha=0.5)
plt.xlabel('Fitted values')
plt.ylabel('Deviance residuals')
plt.axhline(y=0, color='r', linestyle='--')
plt.title('Deviance Residuals vs Fitted')
plt.show()

# Q-Q plot of deviance residuals
from statsmodels.graphics.gofplots import qqplot
qqplot(results.resid_deviance, line='s')
plt.title('Q-Q Plot of Deviance Residuals')
plt.show()

# For binary outcomes: binned residual plot
if isinstance(results.model.family, sm.families.Binomial):
    from statsmodels.graphics.gofplots import qqplot
    # Group predictions and compute average residuals
    # (custom implementation needed)
    pass
```

### 影响点与异常值

```python
from statsmodels.stats.outliers_influence import GLMInfluence

influence = results.get_influence()  # Supplies the GLM-specific leverage and scale

# Leverage
leverage = influence.hat_matrix_diag

# Cook's distance
cooks_d = influence.cooks_distance[0]

# Standardized approximate change in fitted means (not OLS DFFITS)
d_fitted_scaled = influence.d_fittedvalues_scaled

# Find influential observations
influential = np.where(cooks_d > 4/len(y))[0]
print(f"Influential observations: {influential}")
```

## 假设检验

```python
# Wald test for single parameter (automatically in summary)

# Likelihood ratio test for nested models
# Fit reduced model
model_reduced = sm.GLM(y, X_reduced, family=family).fit()
model_full = sm.GLM(y, X_full, family=family).fit()

# LR statistic
lr_stat = 2 * (model_full.llf - model_reduced.llf)
df_diff = model_full.df_model - model_reduced.df_model

from scipy import stats
lr_pval = stats.chi2.sf(lr_stat, df_diff)
print(f"LR test p-value: {lr_pval}")

# Wald test for multiple parameters
# Test beta_1 = beta_2 = 0
R = [[0, 1, 0, 0], [0, 0, 1, 0]]
wald_test = results.wald_test(R)
print(wald_test)
```

## 稳健标准误

```python
# Heteroscedasticity-robust (sandwich estimator)
results_robust = results.model.fit(cov_type='HC0')

# Cluster-robust
results_cluster = results.model.fit(cov_type='cluster',
                                    cov_kwds={'groups': cluster_ids})

# Compare standard errors
print("Regular SE:", results.bse)
print("Robust SE:", results_robust.bse)
```

稳健协方差在其渐近假设下修正方差计算。它不能修复分离、错误的均值模型、过少的独立群组或内生性。GLM 的影响点近似仍是实验性的，带 exposure/offset 时尤其如此。

## 模型比较

```python
# AIC/BIC for non-nested models
models = [model1_results, model2_results, model3_results]
for i, res in enumerate(models, 1):
    print(f"Model {i}: AIC={res.aic:.2f}, BIC={res.bic_llf:.2f}")

# Likelihood ratio test for nested models (as shown above)

# Cross-validation for predictive performance
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import log_loss

# Binary independent observations only; X already includes the intercept.
X_array, y_array = np.asarray(X), np.asarray(y)
family = sm.families.Binomial()
kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = []

for train_idx, val_idx in kf.split(X_array, y_array):
    X_train, X_val = X_array[train_idx], X_array[val_idx]
    y_train, y_val = y_array[train_idx], y_array[val_idx]

    model_cv = sm.GLM(y_train, X_train, family=family).fit()
    pred_probs = model_cv.predict(X_val)

    score = log_loss(y_val, pred_probs)
    cv_scores.append(score)

print(f"CV Log Loss: {np.mean(cv_scores):.4f} ± {np.std(cv_scores):.4f}")
```

## 预测

```python
# Point predictions
predictions = results.predict(X_new)

# For classification: get probabilities and convert
if isinstance(family, sm.families.Binomial):
    probs = predictions
    class_predictions = (probs > 0.5).astype(int)

# For counts: predictions are expected counts
if isinstance(family, sm.families.Poisson):
    expected_counts = predictions

# Conditional mean confidence intervals, not intervals for a new observation
mean_prediction = results.get_prediction(X_new, which="mean")
mean_ci = mean_prediction.conf_int(alpha=0.05)
mean_table = mean_prediction.summary_frame()
# A bootstrap of fitted means alone also omits future outcome noise.
# Outcome prediction intervals need the fitted family/scale plus parameter uncertainty.
```

## 常见应用

### Logistic 回归（二值分类）

```python
import statsmodels.api as sm

# Fit logistic regression
X = sm.add_constant(X_data)
model = sm.GLM(y, X, family=sm.families.Binomial())
results = model.fit()

# Odds ratios
odds_ratios = np.exp(results.params)
odds_ci = np.exp(results.conf_int())

# Classification metrics
from sklearn.metrics import classification_report, roc_auc_score

probs = results.predict(X)
predictions = (probs > 0.5).astype(int)

print(classification_report(y, predictions))
print(f"AUC: {roc_auc_score(y, probs):.4f}")

# ROC curve
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

fpr, tpr, thresholds = roc_curve(y, probs)
plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()
```

### Poisson 回归（计数数据）

```python
# Fit Poisson model
X = sm.add_constant(X_data)
model = sm.GLM(y_counts, X, family=sm.families.Poisson())
results = model.fit()

# Rate ratios
rate_ratios = np.exp(results.params)
print("Rate ratios:", rate_ratios)

# Check overdispersion
dispersion = results.pearson_chi2 / results.df_resid
if dispersion > 1.5:
    print(f"Elevated Pearson dispersion ({dispersion:.2f}); investigate mean, dependence and count family.")
```

### Gamma 回归（成本/时长数据）

```python
# Fit Gamma model with log link
X = sm.add_constant(X_data)
model = sm.GLM(y_cost, X,
               family=sm.families.Gamma(link=sm.families.links.Log()))
results = model.fit()

# Multiplicative effects
effects = np.exp(results.params)
print("Multiplicative effects on mean:", effects)
```

## 最佳实践

1. **检查条件假设**：查看响应支撑集、均值结构、exposure 与残差形态；边际响应是否正态并不能决定用哪个 GLM
2. **核对连接函数**：除非有理由，否则用 canonical link
3. **检查残差**：离散 deviance 残差不必正态；按分布族选用校准与基于模拟的诊断
4. **检验过度离散**：Poisson 模型尤其要做
5. **正确使用 offset**：用于 exposure 变化的率建模
6. **考虑稳健 SE**：方差假设存疑时
7. **比较模型**：非嵌套用 AIC/BIC，嵌套用 LR 检验
8. **在原尺度上解读**：对系数做变换（如 log 连接取 exp）
9. **检查影响点**：用 Cook's distance
10. **验证预测**：用交叉验证或留出集

## 常见陷阱

1. **忘记加常数项**：没有截距项
2. **分布族选错**：先查看响应分布
3. **忽略过度离散**：改用负二项而非 Poisson
4. **误读系数**：记住连接函数的变换
5. **不检查收敛**：IRLS 可能不收敛，留意警告
6. **logistic 中完全分离**：某些类别完美预测结果
7. **有界结果用 identity 连接**：可能预测到有效范围之外
8. **比较样本不同的模型**：要用同一批观测
9. **率模型漏掉 offset**：必须用 log(exposure) 作 offset
10. **不考虑替代方案**：复杂数据可用混合模型、零膨胀模型
