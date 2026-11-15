> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/researcher/science/statsmodels/references/modeling_capabilities.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 核心统计建模能力

线性模型、广义线性模型、离散选择模型、时间序列分析，
以及统计检验与诊断——分别说明 statsmodels 在每个领域提供什么、
该用哪个类。

## 核心统计建模能力

### 1. 线性回归模型

面向连续结果、适配各类误差结构的完整线性模型集合。

**可用模型：**
- **OLS**：标准线性回归，误差 i.i.d.
- **WLS**：处理异方差误差的加权最小二乘
- **GLS**：适配任意协方差结构的广义最小二乘
- **GLSAR**：带自回归误差的 GLS，用于时间序列
- **Quantile Regression**：条件分位数（中位数拟合降低的是响应异常值敏感度，不降低高杠杆偏误）
- **Mixed Effects**：带随机效应的分层/多层模型
- **Recursive/Rolling**：扩展窗口或滚动窗口的系数估计

**主要特性：**
- 全面的诊断检验
- 稳健标准误（HC、HAC、整群稳健）
- 影响点统计量（Cook's distance、杠杆值、DFFITS）
- 假设检验（F 检验、Wald 检验）
- 模型比较（AIC、BIC、似然比检验）
- 带置信区间与预测区间的预测

**何时使用：** 连续结果变量，需要对系数做推断，需要诊断

**参考：** 模型选择、诊断与最佳实践详见 `references/linear_models.md`。

### 2. 广义线性模型（GLM）

把线性模型推广到非正态分布的灵活框架。

**分布族：**
- **Binomial**：二值结果或比例（logistic 回归）
- **Poisson**：计数数据
- **Negative Binomial**：过度离散的计数
- **Gamma**：正的连续、右偏数据
- **Inverse Gaussian**：带特定方差结构的正连续数据
- **Gaussian**：Identity 连接配不加权的独立误差可复现 OLS 系数
- **Tweedie**：面向半连续数据的灵活分布族

**连接函数：**
- Logit、Probit、Log、Identity、Inverse、Sqrt、CLogLog、Power
- 按解读需求与模型拟合情况选择

**主要特性：**
- 通过 IRLS 做极大似然估计
- Deviance 与 Pearson 残差
- 拟合优度统计量
- Pseudo R-squared 度量
- 稳健标准误

**何时使用：** 响应机制与条件均值/方差结构需要某个 GLM 分布族和连接函数时。仅边际非正态并不是判断标准。

**参考：** 分布族选择、连接函数、解读与诊断详见 `references/glm.md`。

### 3. 离散选择模型

面向分类与计数结果的模型。

**二值模型：**
- **Logit**：Logistic 回归（odds ratio）
- **Probit**：Probit 回归（正态分布）

**多项模型：**
- **MNLogit**：无序类别（3 个及以上水平）
- **Conditional Logit**：按组条件化的二值似然，无显式截距；choice set 定义组
- **Ordered Model**：有序结果（有序类别）

**计数模型：**
- **Poisson**：标准计数模型
- **Negative Binomial**：过度离散的计数
- **Zero-Inflated**：零值过多（ZIP、ZINB）
- **Hurdle Models**：零值较多数据的两阶段模型

**主要特性：**
- 极大似然估计
- 均值处边际效应或平均边际效应
- 用 AIC/BIC 比较模型
- 预测概率与分类
- 拟合优度检验

**何时使用：** 二值、分类或计数结果

**参考：** 模型选择、解读与评估详见 `references/discrete_choice.md`。

### 4. 时间序列分析

完整的时间序列建模与预测能力。

**单变量模型：**
- **AutoReg (AR)**：自回归模型
- **ARIMA**：自回归积分滑动平均
- **SARIMAX**：带外生变量的季节性 ARIMA
- **Exponential Smoothing**：简单、Holt、Holt-Winters
- **ETS**：新息状态空间模型

**多变量模型：**
- **VAR**：向量自回归
- **VARMAX**：带 MA 与外生变量的 VAR
- **Dynamic Factor Models**：提取公共因子
- **VECM**：向量误差修正模型（协整）

**进阶模型：**
- **State Space**：Kalman 滤波、自定义设定
- **Regime Switching**：Markov 切换模型
- **ARDL**：自回归分布滞后

**主要特性：**
- 用 ACF/PACF 分析做模型识别
- 平稳性检验（ADF、KPSS）
- 带预测区间的预测
- 残差诊断（Ljung-Box、异方差）
- Granger 因果检验
- 脉冲响应函数（IRF）
- 预测误差方差分解（FEVD）

**何时使用：** 按时间排序的数据、预测、理解时间动态

**参考：** 模型选择、诊断与预测方法详见 `references/time_series.md`。

### 5. 统计检验与诊断

用于模型验证的丰富检验与诊断能力。

**残差诊断：**
- 自相关检验（Ljung-Box、Durbin-Watson、Breusch-Godfrey）
- 异方差检验（Breusch-Pagan、White、ARCH）
- 正态性检验（Jarque-Bera、Omnibus、Anderson-Darling、Lilliefors）
- 设定检验（RESET、Harvey-Collier）

**影响点与异常值：**
- 杠杆值（hat values）
- Cook's distance
- DFFITS 与 DFBETAs
- 学生化残差
- 影响点图

**假设检验：**
- t 检验（单样本、双样本、配对）
- 比例检验
- 卡方检验
- 非参数检验（Mann-Whitney、Wilcoxon、Kruskal-Wallis）
- ANOVA（单因素、双因素、重复测量）

**多重比较：**
- Tukey's HSD
- Bonferroni 校正
- 错误发现率（FDR）

**效应量与功效：**
- Cohen's d、eta-squared
- t 检验、比例的功效分析
- 样本量计算

**稳健推断：**
- 异方差一致 SE（HC0-HC3）
- HAC 标准误（Newey-West）
- 整群稳健标准误

**何时使用：** 考察假设与敏感性。诊断检验未拒绝、稳健标准误本身都不能确立科学有效性。

**参考：** 完整的检验与诊断流程详见 `references/stats_diagnostics.md`。
