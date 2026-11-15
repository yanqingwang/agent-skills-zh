> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/researcher/science/statsmodels/references/model_selection.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Formula API 与模型选择

先讲 R 风格 formula API，再讲模型选择与比较：信息准则、
嵌套模型检验，以及统计模型交叉验证的注意事项。

## Formula API（R 风格）

Statsmodels 支持 R 风格公式，便于直观设定模型：

```python
import statsmodels.formula.api as smf

# OLS with formula
results = smf.ols('y ~ x1 + x2 + x1:x2', data=df).fit()

# Categorical variables (automatic dummy coding)
results = smf.ols('y ~ x1 + C(category)', data=df).fit()

# Interactions
results = smf.ols('y ~ x1 * x2', data=df).fit()  # x1 + x2 + x1:x2

# Polynomial terms
results = smf.ols('y ~ x + I(x**2)', data=df).fit()

# Logit
results = smf.logit('y ~ x1 + x2 + C(group)', data=df).fit()

# Poisson
results = smf.poisson('count ~ x1 + x2', data=df).fit()

# ARIMA (not available via formula, use regular API)
```

## 模型选择与比较

比较时要使用相同的响应定义、相同的观测，且似然可比。公式的缺失值处理可能悄悄改变样本：先选出/记录共同的行再比较。混合模型的固定效应要在 ML 下比较，不要用 REML。GLM 的似然 BIC 是 `bic_llf`；基于 deviance 的 BIC 是另一套约定。常规 LR 卡方推断不覆盖边界情形，如 Poisson 对 NB 的 alpha=0、分离与不可识别参数。

做完模型/变量选择后，不要把 p 值当成模型是预先设定好的那样去解读。

### 信息准则

```python
# Compare models using AIC/BIC
models = {
    'Model 1': model1_results,
    'Model 2': model2_results,
    'Model 3': model3_results
}

comparison = pd.DataFrame({
    'AIC': {name: res.aic for name, res in models.items()},
    'BIC': {name: res.bic for name, res in models.items()},
    'Log-Likelihood': {name: res.llf for name, res in models.items()}
})

print(comparison.sort_values('AIC'))
# Lower values rank comparable candidates; they do not establish absolute adequacy
```

### 似然比检验（嵌套模型）

```python
# For nested models (one is subset of the other)
from scipy import stats

lr_stat = 2 * (full_model.llf - reduced_model.llf)
df_diff = full_model.df_model - reduced_model.df_model
if df_diff <= 0:
    raise ValueError("Expected a larger full model")
p_value = stats.chi2.sf(lr_stat, df_diff)

print(f"LR statistic: {lr_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Reject the specified restrictions under regular LR assumptions")
else:
    print("No rejection of the specified restrictions; this is not equivalence")
```

### 交叉验证

此例假设观测相互独立，使用带截距的数值型 pandas 设计矩阵。相关数据要用分组或按时间顺序的划分，预处理要在每个训练折内拟合。Scikit-learn 的 LogisticRegression 默认带正则，不是可互换的 statsmodels MLE 封装。

```python
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = []

for train_idx, val_idx in kf.split(X):
    X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
    y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

    # Fit model
    model = sm.OLS(y_train, X_train).fit()

    # Predict
    y_pred = model.predict(X_val)

    # Score
    rmse = np.sqrt(mean_squared_error(y_val, y_pred))
    cv_scores.append(rmse)

print(f"CV RMSE: {np.mean(cv_scores):.4f} ± {np.std(cv_scores):.4f}")
```
