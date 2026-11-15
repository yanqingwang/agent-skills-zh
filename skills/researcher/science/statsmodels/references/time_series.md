> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/researcher/science/statsmodels/references/time_series.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 时间序列分析参考

本文件全面介绍 statsmodels 中的时间序列模型，涵盖 ARIMA、状态空间模型、VAR、指数平滑与预测方法。

## 概览

Statsmodels 提供丰富的时间序列能力：
- **单变量模型**：AR、ARIMA、SARIMAX、Exponential Smoothing
- **多变量模型**：VAR、VARMAX、Dynamic Factor Models
- **状态空间框架**：自定义模型、Kalman 滤波
- **诊断工具**：ACF、PACF、平稳性检验、残差分析
- **预测**：点预测与预测区间

使用有序、唯一、规则且记录了频率的时间网格；不要丢弃中间缺失的日期而悄悄压缩时间。状态空间模型能处理缺失响应，但外生数据必须有限且对齐，ADF/KPSS 不接受缺失值。带日期标签的预测要保留频率，并按模型列序提供未来的外生行。

## 单变量时间序列模型

### AutoReg（AR 模型）

自回归模型：当前值依赖过去值。

**适用场景：**
- 单变量时间序列
- 过去值可预测未来
- 平稳序列

**模型**：yₜ = c + φ₁yₜ₋₁ + φ₂yₜ₋₂ + ... + φₚyₜ₋ₚ + εₜ

```python
from statsmodels.tsa.ar_model import AutoReg
import pandas as pd

# Fit AR(p) model
model = AutoReg(y, lags=5)  # AR(5)
results = model.fit()

print(results.summary())
```

**带外生回归元：**
```python
# AR with exogenous variables (ARX)
model = AutoReg(y, lags=5, exog=X_exog)
results = model.fit()
```

**季节性 AR：**
```python
# Lags 1..12 plus seasonal dummies; use lags=[1, 12] for sparse seasonal lags
model = AutoReg(y, lags=12, seasonal=True, period=12)
results = model.fit()
```

### ARIMA（自回归积分滑动平均）

组合 AR、差分（I）与 MA 成分。

**适用场景：**
- 非平稳时间序列（需要差分）
- 过去值与误差共同预测未来
- 适用于许多时间序列的灵活模型

**模型**：ARIMA(p,d,q)
- p：AR 阶数（滞后数）
- d：差分阶数（用以达到平稳）
- q：MA 阶数（滞后预测误差）

```python
from statsmodels.tsa.arima.model import ARIMA

# Fit ARIMA(p,d,q)
model = ARIMA(y, order=(1, 1, 1))  # ARIMA(1,1,1)
results = model.fit()

print(results.summary())
```

**选择 p, d, q：**

1. **确定 d（差分阶数）**：
```python
from statsmodels.tsa.stattools import adfuller

# ADF test for stationarity
def check_stationarity(series):
    result = adfuller(series, result_object=True)
    print(f"ADF Statistic: {result.statistic:.4f}")
    print(f"p-value: {result.pvalue:.4f}")
    if result.pvalue <= 0.05:
        print("Reject unit-root null under the chosen deterministic specification")
        return True
    else:
        print("Do not reject unit root; this does not prove nonstationarity")
        return False

# Combine the test with trend/seasonal plots, sampling frequency and domain knowledge.
check_stationarity(y)
# Compare a prespecified candidate difference; do not repeatedly difference
# until a p-value crosses a threshold. ARIMA(y, order=(p,d,q)) uses original y.
y_diff = y.diff().dropna()
check_stationarity(y_diff)
```

2. **确定 p 和 q（ACF/PACF）**：
```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

# After differencing to stationarity
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# ACF: helps determine q (MA order)
plot_acf(y_stationary, lags=40, ax=ax1)
ax1.set_title('Autocorrelation Function (ACF)')

# PACF: helps determine p (AR order)
plot_pacf(y_stationary, lags=40, ax=ax2)
ax2.set_title('Partial Autocorrelation Function (PACF)')

plt.tight_layout()
plt.show()

# Rules of thumb:
# - PACF cuts off at lag p → AR(p)
# - ACF cuts off at lag q → MA(q)
# - Both decay → ARMA(p,q)
```

3. **模型选择（AIC/BIC）**：
```python
# Grid search for best (p,q) given d
import numpy as np

best_aic = np.inf
best_order = None
best_result = None
candidates = []

for p in range(5):
    for q in range(5):
        try:
            model = ARIMA(y, order=(p, d, q))
            results = model.fit()
            converged = results.mle_retvals.get("converged", False)
            candidates.append({"order": (p, d, q), "converged": converged, "aic": results.aic})
            if converged and np.isfinite(results.aic) and results.aic < best_aic:
                best_aic = results.aic
                best_order = (p, d, q)
                best_result = results
        except (ValueError, np.linalg.LinAlgError) as exc:
            candidates.append({"order": (p, d, q), "error": str(exc)})

if best_order is None:
    raise RuntimeError("No converged finite-likelihood candidate; inspect failures")
results = best_result  # Keep the selected fit, not the last grid candidate
print(pd.DataFrame(candidates))
print(f"Best order: {best_order} with AIC: {best_aic:.2f}")
```

### SARIMAX（带外生变量的季节性 ARIMA）

在 ARIMA 上加入季节性与外生回归元。

**适用场景：**
- 季节性形态（月度、季度数据）
- 外部变量影响序列
- 最灵活的单变量模型

**模型**：SARIMAX(p,d,q)(P,D,Q,s)
- (p,d,q)：非季节性 ARIMA
- (P,D,Q,s)：周期为 s 的季节性 ARIMA

```python
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Seasonal ARIMA for monthly data (s=12)
model = SARIMAX(y,
                order=(1, 1, 1),           # (p,d,q)
                seasonal_order=(1, 1, 1, 12))  # (P,D,Q,s)
results = model.fit()

print(results.summary())
```

**带外生变量：**
```python
# SARIMAX with external predictors
model = SARIMAX(y,
                exog=X_exog,
                order=(1, 1, 1),
                seasonal_order=(1, 1, 1, 12))
results = model.fit()
```

**示例：带趋势与季节性的月度销售额**
```python
# Typical for monthly data: (p,d,q)(P,D,Q,12)
# Start with (1,1,1)(1,1,1,12) or (0,1,1)(0,1,1,12)

model = SARIMAX(monthly_sales,
                order=(0, 1, 1),
                seasonal_order=(0, 1, 1, 12),
                enforce_stationarity=False,
                enforce_invertibility=False)
results = model.fit()
```

### Exponential Smoothing

对过去观测做加权平均，权重按指数递减。

**适用场景：**
- 简单、可解释的预测
- 存在趋势和/或季节性
- 不需要显式设定模型

**类型：**
- Simple Exponential Smoothing：无趋势、无季节性
- Holt's method：带趋势
- Holt-Winters：带趋势与季节性

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Simple exponential smoothing
model = ExponentialSmoothing(y, trend=None, seasonal=None)
results = model.fit()

# Holt's method (with trend)
model = ExponentialSmoothing(y, trend='add', seasonal=None)
results = model.fit()

# Holt-Winters (trend + seasonality)
model = ExponentialSmoothing(y,
                            trend='add',           # 'add' or 'mul'
                            seasonal='add',        # 'add' or 'mul'
                            seasonal_periods=12)   # e.g., 12 for monthly
results = model.fit()

print(results.summary())
```

**加性 vs 乘性：**
```python
# Additive: constant seasonal variation
# yₜ = Level + Trend + Seasonal + Error

# Multiplicative: proportional seasonal variation
# yₜ = Level × Trend × Seasonal × Error

# Choose based on data:
# - Additive: seasonal variation constant over time
# - Multiplicative: seasonal variation increases with level
```

**新息状态空间（ETS）：**
```python
from statsmodels.tsa.exponential_smoothing.ets import ETSModel

# Innovations state-space ETS, with an explicit error model
model = ETSModel(y,
                error='add',           # 'add' or 'mul'
                trend='add',           # 'add', 'mul', or None
                seasonal='add',        # 'add', 'mul', or None
                seasonal_periods=12)
results = model.fit()
```

## 多变量时间序列

### VAR（向量自回归）

方程组，每个变量依赖所有变量的过去值。

**适用场景：**
- 多条相互关联的时间序列
- 双向关系
- Granger 因果检验

**模型**：每个变量对所有变量做 AR：
- y₁ₜ = c₁ + φ₁₁y₁ₜ₋₁ + φ₁₂y₂ₜ₋₁ + ... + ε₁ₜ
- y₂ₜ = c₂ + φ₂₁y₁ₜ₋₁ + φ₂₂y₂ₜ₋₁ + ... + ε₂ₜ

```python
from statsmodels.tsa.api import VAR
import pandas as pd

# Data should be DataFrame with multiple columns
# Each column is a time series
df_multivariate = pd.DataFrame({'series1': y1, 'series2': y2, 'series3': y3})

# Fit VAR
model = VAR(df_multivariate)

# Select lag order using AIC/BIC
lag_order_results = model.select_order(maxlags=15)
print(lag_order_results.summary())

# Fit with optimal lags
results = model.fit(maxlags=5, ic='aic')
print(results.summary())
```

**Granger 因果检验：**
```python
# Test if series1 Granger-causes series2
from statsmodels.tsa.stattools import grangercausalitytests

# Requires 2D array [series2, series1]
test_data = df_multivariate[['series2', 'series1']]

# Test up to max_lag
max_lag = 5
granger_tests = grangercausalitytests(test_data, max_lag)

# P-values for each lag
for lag in range(1, max_lag + 1):
    p_value = granger_tests[lag][0]['ssr_ftest'][1]
    print(f"Lag {lag}: p-value = {p_value:.4f}")
```

Granger 可预测性并不识别干预效应。要预先指定滞后阶数，或对跨滞后搜索做校正。正交化 IRF 依赖 Cholesky 变量排序与结构性假设。预测区间以拟合参数/模型为条件，并不保证样本外覆盖率。

**脉冲响应函数（IRF）：**
```python
# Trace effect of shock through system
irf = results.irf(10)  # 10 periods ahead

# Plot IRFs
irf.plot(orth=True)  # Orthogonalized (Cholesky decomposition)
plt.show()

# Cumulative effects
irf.plot_cum_effects(orth=True)
plt.show()
```

**预测误差方差分解：**
```python
# Contribution of each variable to forecast error variance
fevd = results.fevd(10)  # 10 periods ahead
fevd.plot()
plt.show()
```

### VARMAX（带移动平均与外生变量的 VAR）

在 VAR 上加入 MA 成分与外部回归元。

**适用场景：**
- VAR 不够用（需要 MA 成分）
- 外部变量影响系统
- 更灵活的多变量模型

```python
from statsmodels.tsa.statespace.varmax import VARMAX

# VARMAX(p, q) with exogenous variables
model = VARMAX(df_multivariate,
               order=(1, 0),        # VAR example; unrestricted VARMA(p>0,q>0) is not identified
               exog=X_exog)
results = model.fit()

print(results.summary())
```

## 状态空间模型

用于自定义时间序列模型的灵活框架。

**适用场景：**
- 自定义模型设定
- 不可观测成分
- Kalman 滤波/平滑
- 缺失数据

```python
from statsmodels.tsa.statespace.mlemodel import MLEModel

# Extend MLEModel for custom state space models
# Example: Local level model (random walk + noise)
```

**Dynamic Factor Models：**
```python
from statsmodels.tsa.statespace.dynamic_factor import DynamicFactor

# Extract common factors from multiple time series
model = DynamicFactor(df_multivariate,
                      k_factors=2,          # Number of factors
                      factor_order=2)       # AR order of factors
results = model.fit()

# Estimated factors
factors = results.factors.filtered
```

## 预测

### 点预测

```python
# ARIMA forecasting
model = ARIMA(y, order=(1, 1, 1))
results = model.fit()

# Forecast h steps ahead
h = 10
forecast = results.forecast(steps=h)

# With exogenous variables (SARIMAX)
model = SARIMAX(y, exog=X, order=(1, 1, 1))
results = model.fit()

# Need future exogenous values
forecast = results.forecast(steps=h, exog=X_future)
```

### 预测区间

```python
# Continuing the SARIMAX fit with exogenous regressors above:
forecast_obj = results.get_forecast(steps=h, exog=X_future)
forecast_df = forecast_obj.summary_frame()

print(forecast_df)
# Contains: mean, mean_se, mean_ci_lower, mean_ci_upper

# Extract components
forecast_mean = forecast_df['mean']
forecast_ci_lower = forecast_df['mean_ci_lower']
forecast_ci_upper = forecast_df['mean_ci_upper']

# Plot
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(y.index, y, label='Historical')
plt.plot(forecast_df.index, forecast_mean, label='Forecast', color='red')
plt.fill_between(forecast_df.index,
                 forecast_ci_lower,
                 forecast_ci_upper,
                 alpha=0.3, color='red', label='95% prediction interval')
plt.legend()
plt.title('Forecast with Prediction Intervals')
plt.show()
```

状态空间汇总用 `mean_ci_*` 标签表示预测不确定性。默认情况下，预测误差方差在给定拟合参数的条件下包含未来观测不确定性；它与 GLM 的均值置信区间不是同一目标量。

### 动态 vs 静态预测

```python
# Static (one-step-ahead, using actual values)
static_forecast = results.get_prediction(start=split_point, end=len(y)-1)

# Dynamic (multi-step, using predicted values)
dynamic_forecast = results.get_prediction(start=split_point,
                                          end=len(y)-1,
                                          dynamic=True)

# Plot comparison
fig, ax = plt.subplots(figsize=(12, 6))
y.plot(ax=ax, label='Actual')
static_forecast.predicted_mean.plot(ax=ax, label='Static forecast')
dynamic_forecast.predicted_mean.plot(ax=ax, label='Dynamic forecast')
ax.legend()
plt.show()
```

## 诊断检验

### 平稳性检验

```python
from statsmodels.tsa.stattools import adfuller, kpss

# Augmented Dickey-Fuller (ADF) test
# H0: unit root (non-stationary)
adf_result = adfuller(y, autolag='AIC', result_object=True)
print(f"ADF Statistic: {adf_result.statistic:.4f}")
print(f"p-value: {adf_result.pvalue:.4f}")
if adf_result.pvalue <= 0.05:
    print("Reject the unit-root null for this specification")
else:
    print("Unit-root null not rejected; stationarity remains unresolved")

# KPSS test
# H0: stationary (opposite of ADF)
kpss_result = kpss(y, regression='c', nlags='auto', result_object=True)
print(f"KPSS Statistic: {kpss_result.statistic:.4f}")
print(f"p-value: {kpss_result.pvalue:.4f}")
if kpss_result.pvalue <= 0.05:
    print("Reject level-stationarity null for this specification")
else:
    print("Level-stationarity null not rejected; not proof of stationarity")
```

### 残差诊断

```python
# Ljung-Box test for autocorrelation in residuals
from statsmodels.stats.diagnostic import acorr_ljungbox

# For the ARIMA(1,1,1) example, p+q=2 fitted dynamic parameters.
# Use standardized one-step forecast errors after initialization burn-in.
innov = results.filter_results.standardized_forecasts_error[0]
innov = innov[results.loglikelihood_burn:]
lb_test = acorr_ljungbox(innov, lags=[10], model_df=2, return_df=True)
print(lb_test)
# A large p-value is failure to reject, not evidence that the model is correct.
# Adjust model_df to the fitted dynamic structure; lags must exceed model_df.

# Plot residual diagnostics
results.plot_diagnostics(figsize=(12, 8))
plt.show()

# Components:
# 1. Standardized residuals over time
# 2. Histogram + KDE of residuals
# 3. Q-Q plot for normality
# 4. Correlogram (ACF of residuals)
```

### 异方差检验

```python
from statsmodels.stats.diagnostic import het_arch

# ARCH test for heteroskedasticity
arch_test = het_arch(innov, nlags=10, ddof=2, result_object=True)
print(f"ARCH test statistic: {arch_test.lm:.4f}")
print(f"p-value: {arch_test.lmpval:.4f}")

# If significant, consider GARCH model
```

## 季节性分解

```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Decompose into trend, seasonal, residual
decomposition = seasonal_decompose(y,
                                   model='additive',  # or 'multiplicative'
                                   period=12)         # seasonal period

# Plot components
fig = decomposition.plot()
fig.set_size_inches(12, 8)
plt.show()

# Access components
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# STL decomposition (more robust)
from statsmodels.tsa.seasonal import STL

stl = STL(y, period=12, seasonal=13, robust=True)  # seasonal smoother length is odd
stl_result = stl.fit()

fig = stl_result.plot()
plt.show()

# Multiple seasonalities, e.g., hourly data with daily and weekly patterns
from statsmodels.tsa.seasonal import MSTL

mstl_result = MSTL(hourly_series, periods=(24, 24 * 7)).fit()
fig = mstl_result.plot()
plt.show()
```

## 模型评估

### 样本内指标

```python
# From results object
print(f"AIC: {results.aic:.2f}")
print(f"BIC: {results.bic:.2f}")
print(f"Log-likelihood: {results.llf:.2f}")

# MSE on training data
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y, results.fittedvalues)
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.4f}")

# MAE
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y, results.fittedvalues)
print(f"MAE: {mae:.4f}")
```

### 样本外评估

```python
# Train-test split for time series (no shuffle!)
train_size = int(0.8 * len(y))
y_train = y.iloc[:train_size]
y_test = y.iloc[train_size:]

# Fit on training data
model = ARIMA(y_train, order=(1, 1, 1))
results = model.fit()

# Forecast test period
forecast = results.forecast(steps=len(y_test))

# Metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error

rmse = np.sqrt(mean_squared_error(y_test, forecast))
mae = mean_absolute_error(y_test, forecast)
mape = (np.mean(np.abs((y_test - forecast) / y_test)) * 100
        if np.all(np.asarray(y_test) > 0) else np.nan)

print(f"Test RMSE: {rmse:.4f}")
print(f"Test MAE: {mae:.4f}")
print(f"Test MAPE: {mape:.2f}%")
```

### Rolling 预测

```python
# More realistic evaluation: rolling one-step-ahead forecasts
forecasts = []

for t in range(len(y_test)):
    # Refit or update with new observation
    y_current = y.iloc[:train_size + t]
    model = ARIMA(y_current, order=(1, 1, 1))
    fit = model.fit()

    # One-step forecast
    fc = np.asarray(fit.forecast(steps=1))[0]
    forecasts.append(fc)

forecasts = np.array(forecasts)

rmse = np.sqrt(mean_squared_error(y_test, forecasts))
print(f"Rolling forecast RMSE: {rmse:.4f}")
```

### 交叉验证

```python
# Time series cross-validation (expanding window)
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
rmse_scores = []

for train_idx, test_idx in tscv.split(y):
    y_train_cv = y.iloc[train_idx]
    y_test_cv = y.iloc[test_idx]

    model = ARIMA(y_train_cv, order=(1, 1, 1))
    results = model.fit()

    forecast = results.forecast(steps=len(test_idx))
    rmse = np.sqrt(mean_squared_error(y_test_cv, forecast))
    rmse_scores.append(rmse)

print(f"CV RMSE: {np.mean(rmse_scores):.4f} ± {np.std(rmse_scores):.4f}")
```

## 进阶主题

### ARDL（自回归分布滞后）

连接单变量与多变量时间序列。

```python
from statsmodels.tsa.ardl import ARDL

# ARDL(p, q) model
# y depends on its own lags and lags of X
model = ARDL(y, lags=2, exog=X, order=2)
results = model.fit()
```

### 误差修正模型

用于协整序列。

```python
from statsmodels.tsa.vector_ar.vecm import coint_johansen

# Test for cointegration
johansen_test = coint_johansen(df_multivariate, det_order=0, k_ar_diff=1)

# Fit VECM if cointegrated
from statsmodels.tsa.vector_ar.vecm import VECM

model = VECM(df_multivariate, k_ar_diff=1, coint_rank=1)
results = model.fit()
```

### Regime Switching 模型

用于结构断点与状态切换。

```python
from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

# Switching intercept/variance; MarkovRegression.order does not add AR terms.
# Use MarkovAutoregression for regime-switching autoregressive coefficients.
model = MarkovRegression(y, k_regimes=2, switching_variance=True)
results = model.fit()

# Smoothed probabilities of regimes
regime_probs = results.smoothed_marginal_probabilities
```

## 最佳实践

1. **检查平稳性**：必要时差分，用 ADF/KPSS 检验确认
2. **画数据**：建模前始终先可视化
3. **识别季节性**：用合适的季节性模型（SARIMAX、Holt-Winters）
4. **模型选择**：用 AIC/BIC 与样本外验证
5. **残差诊断**：检查自相关、正态性、异方差
6. **预测评估**：用 rolling 预测与恰当的时间序列 CV
7. **避免过拟合**：偏好更简单的模型，用信息准则
8. **记录假设**：注明任何数据变换（log、差分）
9. **预测区间**：始终给出不确定性估计
10. **定期重拟合**：新数据到来时更新模型

## 常见陷阱

1. **误用平稳性检验**：ADF/KPSS 的原假设与确定性设定不同；ARIMA 可以通过 d 对单整建模
2. **数据泄漏**：变换中用到了未来数据
3. **季节周期选错**：季度用 S=4，月度用 S=12
4. **过拟合**：参数相对数据太多
5. **忽略残差自相关**：模型不充分
6. **用不恰当的指标**：MAPE 遇到零或负值会失效
7. **不处理缺失数据**：影响模型估计
8. **外生变量外推**：SARIMAX 需要未来的 X 值
9. **混淆静态与动态预测**：多步预测下动态更贴近实际
10. **不验证预测**：始终检查样本外表现
