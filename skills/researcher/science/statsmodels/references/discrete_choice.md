> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/researcher/science/statsmodels/references/discrete_choice.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 离散选择模型参考

本文件全面介绍 statsmodels 中的离散选择模型，涵盖二值、多项、计数与有序模型。

## 概览

离散选择模型处理以下几类结果变量：
- **二值**：0/1、成功/失败
- **多项**：多个无序类别
- **有序**：有序类别
- **计数**：非负整数

这类模型采用基于似然的估计。独立性与抽样假设依模型而异：条件模型把组截距条件掉，而整群抽样需要相应的协方差/设计。要检查估计值有限、设计矩阵满秩、收敛与分离；仅收敛并不能保证可识别。

## 二值模型

### Logit（逻辑回归）

对二值结果使用 logistic 分布。

**适用场景：**
- 二值分类（是/否、成功/失败）
- 二值结果的概率估计
- 可解释的 odds ratio

**模型**：P(Y=1|X) = 1 / (1 + exp(-Xβ))

```python
import statsmodels.api as sm
from statsmodels.discrete.discrete_model import Logit

# Prepare data
X = sm.add_constant(X_data)

# Fit model
model = Logit(y, X)
results = model.fit()

print(results.summary())
```

**解读：**
```python
import numpy as np

# Odds ratios
odds_ratios = np.exp(results.params)
print("Odds ratios:", odds_ratios)

# For 1-unit increase in X, odds multiply by exp(β)
# OR > 1: increases odds of success
# OR < 1: decreases odds of success
# OR = 1: no effect

# Confidence intervals for odds ratios
odds_ci = np.exp(results.conf_int())
print("Odds ratio 95% CI:")
print(odds_ci)
```

**边际效应：**
```python
# Average marginal effects (AME)
marginal_effects = results.get_margeff(at='overall')
print(marginal_effects.summary())

# Marginal effects at means (MEM)
marginal_effects_mem = results.get_margeff(at='mean', method='dydx')

# Marginal effects at representative values
marginal_effects_custom = results.get_margeff(at='mean',
                                              atexog={1: 1, 2: 5})  # Zero-based design-column indices
```

**预测：**
```python
# Predicted probabilities
probs = results.predict(X)

# Binary predictions (0.5 threshold)
predictions = (probs > 0.5).astype(int)

# Custom threshold
threshold = 0.3
predictions_custom = (probs > threshold).astype(int)

# For new data
X_new = sm.add_constant(X_new_data, has_constant="add")
new_probs = results.predict(X_new)
```

**模型评估：**
```python
from sklearn.metrics import (classification_report, confusion_matrix,
                             roc_auc_score, roc_curve)

# Classification report
print(classification_report(y, predictions))

# Confusion matrix
print(confusion_matrix(y, predictions))

# AUC-ROC
auc = roc_auc_score(y, probs)
print(f"AUC: {auc:.4f}")

# Pseudo R-squared
print(f"McFadden's Pseudo R²: {results.prsquared:.4f}")
```

### Probit

对二值结果使用正态分布。

**适用场景：**
- 二值结果
- 倾向正态分布假设
- 领域惯例（计量经济学常用 probit）

**模型**：P(Y=1|X) = Φ(Xβ)，其中 Φ 为标准正态 CDF

```python
from statsmodels.discrete.discrete_model import Probit

model = Probit(y, X)
results = model.fit()

print(results.summary())
```

**与 Logit 比较：**
- Probit 与 Logit 结果通常相近
- Probit：对称，基于正态分布
- Logit：尾部略厚，更易解读（odds ratio）
- 系数不可直接比较（尺度不同）

```python
# Marginal effects are comparable
logit_me = logit_results.get_margeff().margeff
probit_me = probit_results.get_margeff().margeff

print("Logit marginal effects:", logit_me)
print("Probit marginal effects:", probit_me)
```

## 多项模型

### MNLogit（多项 Logit）

用于含 3 个及以上类别的无序分类结果。

**适用场景：**
- 多个无序类别（如出行方式、品牌选择）
- 类别之间没有自然顺序
- 需要每个类别的概率

**模型**：P(Y=j|X) = exp(Xβⱼ) / Σₖ exp(Xβₖ)

```python
from statsmodels.discrete.discrete_model import MNLogit

# y should be integers 0, 1, 2, ... for categories
model = MNLogit(y, X)
results = model.fit()

print(results.summary())
```

**解读：**
```python
# One category is reference (usually category 0)
# Coefficients represent log-odds relative to reference

# For category j vs reference:
# exp(β_j) = odds ratio of category j vs reference

# Predicted probabilities for each category
probs = results.predict(X)  # Shape: (n_samples, n_categories)

# Most likely category
predicted_categories = np.asarray(probs).argmax(axis=1)
```

**相对风险比：**
```python
# Exponentiate coefficients for relative risk ratios
import numpy as np
import pandas as pd

# Get parameter names and values
params_df = pd.concat({
    'coef': pd.DataFrame(results.params),
    'RRR': pd.DataFrame(np.exp(results.params))
}, axis=1)
print(params_df)
```

### Conditional Logit

用于各备选方案带有自身特征的选择模型。

**适用场景：**
- 方案专属回归元（随选项变化）
- 含选择行为的面板数据
- 离散选择实验

```python
from statsmodels.discrete.conditional_models import ConditionalLogit

# Long format, binary choice indicator, no constant in X_alternatives.
# One group per choice occasion (not one person across multiple occasions).
model = ConditionalLogit(y_choice, X_alternatives, groups=choice_set_id)
results = model.fit()
```

## 计数模型

### Poisson

计数数据的标准模型。

**适用场景：**
- 计数结果（事件、发生次数）
- 稀有事件
- 均值 ≈ 方差

**模型**：P(Y=k|X) = exp(-λ) λᵏ / k!，其中 log(λ) = Xβ

```python
from statsmodels.discrete.discrete_model import Poisson

model = Poisson(y_counts, X)
results = model.fit()

print(results.summary())
```

**解读：**
```python
# Rate ratios (incident rate ratios)
rate_ratios = np.exp(results.params)
print("Rate ratios:", rate_ratios)

# For 1-unit increase in X, expected count multiplies by exp(β)
```

**检查过度离散：**
```python
# Dispersion concerns the conditional variance, not raw variance/mean.
mu = results.predict(X)
pearson_dispersion = np.sum((y_counts - mu)**2 / mu) / results.df_resid
print(f"Pearson dispersion: {pearson_dispersion:.2f}")
# A screening statistic: inspect mean misspecification, exposure and dependence.
```

**带 offset（用于率）：**
```python
# When modeling rates with varying exposure
# log(λ) = log(exposure) + Xβ

model = Poisson(y_counts, X, offset=np.log(exposure))
results = model.fit()
```

### 负二项

用于过度离散的计数数据（方差 > 均值）。

**适用场景：**
- 存在过度离散的计数数据
- Poisson 无法解释的多余方差
- 计数存在异质性

**模型**：加入离散参数 α 以刻画过度离散

```python
from statsmodels.discrete.discrete_model import NegativeBinomial

model = NegativeBinomial(y_counts, X)
results = model.fit()

print(results.summary())
print(f"Dispersion parameter alpha: {np.asarray(results.params)[-1]:.4f}")
```

**与 Poisson 比较：**
```python
# Fit both models
poisson_results = Poisson(y_counts, X).fit()
nb_results = NegativeBinomial(y_counts, X).fit()

# AIC comparison (lower is better)
print(f"Poisson AIC: {poisson_results.aic:.2f}")
print(f"Negative Binomial AIC: {nb_results.aic:.2f}")

# Alpha=0 is a boundary under the Poisson null. A naive chi-square(1)
# likelihood-ratio p-value is not the ordinary regular nested-model test.
# Use a justified boundary reference distribution or parametric bootstrap.
lr_stat = 2 * (nb_results.llf - poisson_results.llf)
print("Boundary LR statistic (no naive p-value):", lr_stat)
```

### 零膨胀模型

用于零值过多的计数数据。

**适用场景：**
- 零值多于 Poisson/NB 的预期
- 两个过程：一个产生零，一个产生计数
- 例子：就诊次数、保险理赔

**模型：**
- ZeroInflatedPoisson (ZIP)
- ZeroInflatedNegativeBinomialP (ZINB)

```python
from statsmodels.discrete.count_model import (ZeroInflatedPoisson,
                                               ZeroInflatedNegativeBinomialP)

# ZIP model
zip_model = ZeroInflatedPoisson(y_counts, X, exog_infl=X_inflation)
zip_results = zip_model.fit()

# ZINB model (for overdispersion + excess zeros)
zinb_model = ZeroInflatedNegativeBinomialP(y_counts, X, exog_infl=X_inflation)
zinb_results = zinb_model.fit()

print(zip_results.summary())
```

**模型的两部分：**
```python
# 1. Inflation model: P(Y=0 due to inflation)
# 2. Count model: distribution of counts

# Predicted probabilities of inflation
inflation_probs = 1 - zip_results.predict(
    X, exog_infl=X_inflation, which='prob-main')
zero_probs = zip_results.predict(X, exog_infl=X_inflation, which='prob-zero')
pmf = zip_results.predict(X, exog_infl=X_inflation, which='prob')

# Predicted counts
predicted_counts = zip_results.predict(X, exog_infl=X_inflation, which='mean')
```

### Hurdle 模型

两阶段模型：先判断是否有计数，再判断有多少。

**适用场景：**
- 零值过多
- 零值与正计数来自不同过程
- 零值与正值在结构上不同

```python
from statsmodels.discrete.truncated_model import HurdleCountModel

# Poisson-Poisson hurdle model; use `zerodist` for the zero hurdle process
model = HurdleCountModel(y_counts, X,
                         dist='poisson',
                         zerodist='poisson')
results = model.fit()

print(results.summary())
```

## 有序模型

### Ordered Logit/Probit

用于有序分类结果。

**适用场景：**
- 有序类别（如低/中/高、1-5 评分）
- 自然顺序有意义
- 希望保留有序结构

**模型**：带分界点的累积概率模型

```python
from statsmodels.miscmodels.ordinal_model import OrderedModel

# Ordered integers or an ordered pandas categorical; X_data has NO constant
model = OrderedModel(y_ordered, X_data, distr='logit')  # or 'probit'
results = model.fit(method='bfgs')

print(results.summary())
```

**解读：**
```python
# Cutpoints (thresholds between categories)
cutpoints = results.model.transform_threshold_params(results.params)[1:-1]
print("Cutpoints:", cutpoints)

# Coefficients
coefficients = np.asarray(results.params)[:results.model.k_vars]
print("Coefficients:", coefficients)

# Predicted probabilities for each category
probs = results.predict(X_data)  # Shape: (n_samples, n_categories)

# Most likely category
predicted_categories = np.asarray(probs).argmax(axis=1)
```

**比例优势假设：**
```python
# Separate binary fits can be exploratory, but comparing coefficients visually
# is not a calibrated Brant test. A formal proportional-odds assessment needs
# the covariance between cutpoint-specific estimates.
```

Hurdle 模型对两个过程使用同一组 exog；`zerodist` 是删失计数分布，不是 logit 关键字。要检查 NB 零过程参数的可识别性。OrderedModel 在首个阈值之后报告的是变换后的增量；只有 `transform_threshold_params` 才给出真正的分界点。

## 模型诊断

每段代码都要选对应的结果类型；pseudo-R²/零似然与边际效应辅助方法并非对所有计数/有序结果都通用。除非把 X/y 换成留出数据，下面的二值指标都是样本内诊断。阈值与调参必须在不用测试集的前提下确定。

### 拟合优度

```python
# Pseudo R-squared (McFadden)
print(f"Pseudo R²: {results.prsquared:.4f}")

# AIC/BIC for model comparison
print(f"AIC: {results.aic:.2f}")
print(f"BIC: {results.bic:.2f}")

# Log-likelihood
print(f"Log-likelihood: {results.llf:.2f}")

# Likelihood ratio test vs null model
lr_stat = 2 * (results.llf - results.llnull)
from scipy import stats
lr_pval = stats.chi2.sf(lr_stat, results.df_model)
print(f"LR test p-value: {lr_pval}")
```

### 分类指标（二值）

```python
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score)

# Predictions
probs = results.predict(X)
predictions = (probs > 0.5).astype(int)

# Metrics
print(f"Accuracy: {accuracy_score(y, predictions):.4f}")
print(f"Precision: {precision_score(y, predictions):.4f}")
print(f"Recall: {recall_score(y, predictions):.4f}")
print(f"F1: {f1_score(y, predictions):.4f}")
print(f"AUC: {roc_auc_score(y, probs):.4f}")
```

### 分类指标（多项）

```python
from sklearn.metrics import accuracy_score, classification_report, log_loss

# Predicted categories
probs = results.predict(X)
predictions = np.asarray(probs).argmax(axis=1)

# Accuracy
accuracy = accuracy_score(y, predictions)
print(f"Accuracy: {accuracy:.4f}")

# Classification report
print(classification_report(y, predictions))

# Log loss
logloss = log_loss(y, probs)
print(f"Log Loss: {logloss:.4f}")
```

### 计数模型诊断

```python
# Expected frequencies require probabilities, not rounded conditional means.
# This example is specifically a fitted ordinary Poisson result.
values = np.arange(int(np.max(y_counts)) + 1)
pmf = results.predict(X, which="prob", y_values=values)
expected = pmf.sum(axis=0)
observed = np.bincount(np.asarray(y_counts, dtype=int), minlength=len(values))
import matplotlib.pyplot as plt
plt.plot(values, observed, label="Observed")
plt.plot(values, expected, label="Model expected")
plt.legend()
plt.show()
# Include/report the model tail beyond values[-1] when assessing total mass.
```

### 影响点与异常值

```python
# Pearson residuals for an ordinary Poisson model only.
mu = results.predict(X)
std_resid = (y_counts - mu) / np.sqrt(mu)

# Check for outliers (|std_resid| > 2)
outliers = np.where(np.abs(std_resid) > 2)[0]
print(f"Number of outliers: {len(outliers)}")

# Leverage (hat values) - for logit/probit
# from statsmodels.stats.outliers_influence
```

## 假设检验

```python
# Single parameter test (automatic in summary)

# Multiple parameters: Wald test
# Test H0: β₁ = β₂ = 0
R = [[0, 1, 0, 0], [0, 0, 1, 0]]
wald_test = results.wald_test(R)
print(wald_test)

# Likelihood ratio test for nested models
model_reduced = Logit(y, X_reduced).fit()
model_full = Logit(y, X_full).fit()

lr_stat = 2 * (model_full.llf - model_reduced.llf)
df_diff = model_full.df_model - model_reduced.df_model
from scipy import stats
lr_pval = stats.chi2.sf(lr_stat, df_diff)
print(f"LR test p-value: {lr_pval:.4f}")
```

## 模型选择与比较

```python
# Fit multiple models
models = {
    'Logit': Logit(y, X).fit(),
    'Probit': Probit(y, X).fit(),
    # Add more models
}

# Compare AIC/BIC
comparison = pd.DataFrame({
    'AIC': {name: model.aic for name, model in models.items()},
    'BIC': {name: model.bic for name, model in models.items()},
    'Pseudo R²': {name: model.prsquared for name, model in models.items()}
})
print(comparison.sort_values('AIC'))

# Cross-validation for predictive performance
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

# Use sklearn wrapper or manual CV
```

## Formula API

用 R 风格公式更便于设定模型。

```python
import statsmodels.formula.api as smf

# Logit with formula
formula = 'y ~ x1 + x2 + C(category) + x1:x2'
results = smf.logit(formula, data=df).fit()

# MNLogit with formula
results = smf.mnlogit('choice ~ x1 + x2', data=df).fit()  # Numeric category codes

# Poisson with formula
results = smf.poisson('count ~ x1 + x2', data=df).fit()

# Negative Binomial with formula
results = smf.negativebinomial('count ~ x1 + x2', data=df).fit()
```

## 常见应用

### 二值分类（营销响应）

```python
# Predict customer purchase probability
X = sm.add_constant(customer_features)
model = Logit(purchased, X)
results = model.fit()

# Targeting: select top 20% likely to purchase
probs = results.predict(X)
top_20_pct_idx = np.argsort(probs)[-int(0.2*len(probs)):]
```

### 多项选择（出行方式）

```python
# Predict transportation mode choice
model = MNLogit(mode_choice, X)
results = model.fit()

# Predicted mode for new commuter
new_commuter = sm.add_constant(new_features, has_constant="add")
mode_probs = results.predict(new_commuter)
predicted_mode = np.asarray(mode_probs).argmax(axis=1)
```

### 计数数据（就诊次数）

```python
# Model healthcare utilization
model = NegativeBinomial(num_visits, X)
results = model.fit()

# Expected visits for new patient
expected_visits = results.predict(new_patient_X)
```

### 零膨胀（保险理赔）

```python
# Many people have zero claims
# Zero-inflation: some never claim
# Count process: those who might claim

zip_model = ZeroInflatedPoisson(claims, X_count, exog_infl=X_inflation)
results = zip_model.fit()

# Fitted structural-zero mixture probability; not a permanent individual trait
structural_zero_prob = 1 - results.predict(
    X_count, exog_infl=X_inflation, which='prob-main')

# Expected claims
expected_claims = results.predict(X_count, exog_infl=X_inflation, which='mean')
```

## 最佳实践

1. **检查数据类型**：确保响应变量与模型匹配（二值、计数、类别）
2. **正确设定截距**：数组版 Logit/Poisson 通常需要常数项；OrderedModel 与 ConditionalLogit 禁止加常数项
3. **缩放连续预测变量**：利于收敛与解读
4. **检查收敛**：留意收敛警告
5. **使用 formula API**：处理分类变量与交互项
6. **边际效应**：报告边际效应，不只是系数
7. **模型比较**：用 AIC/BIC 与交叉验证
8. **验证**：预测模型用留出集或交叉验证
9. **检查过度离散**：计数模型要检验 Poisson 假设
10. **考虑替代模型**：零值过多时用零膨胀或 Hurdle 模型

## 常见陷阱

1. **漏掉常数项**：没有截距项
2. **完全分离**：Logit/probit 可能不收敛
3. **过度离散仍用 Poisson**：先检查，改用负二项
4. **误读系数**：记住它们处在 log-odds/对数尺度
5. **不检查收敛**：优化可能悄悄失败
6. **分布选错**：模型要与数据类型匹配（二值/计数/分类）
7. **忽略多余零值**：必要时用 ZIP/ZINB
8. **不验证预测**：始终检查样本外表现
9. **比较非嵌套模型**：用 AIC/BIC，不用似然比检验
10. **把有序当无序**：有序类别要用 OrderedModel
