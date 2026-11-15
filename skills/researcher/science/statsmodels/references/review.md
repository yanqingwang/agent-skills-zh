> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/researcher/science/statsmodels/references/review.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 维护与核验台账

2026-10-01 对照 **statsmodels 0.15.0** 复核，环境为 Python 3.13.3、
NumPy 2.5.3、SciPy 1.18.1、pandas 3.0.6、matplotlib 3.11.2 及
scikit-learn 1.9.1。包自身支持 Python 3.10+；这套精确的数值
依赖栈要求 3.12+。这些统计工作流不含远程服务端点、认证或
分页。

当前的 [release notes](https://www.statsmodels.org/stable/release/version0.15.0.html)
与 [tagged source](https://github.com/statsmodels/statsmodels/tree/v0.15.0/statsmodels)，已用安装好的 wheel 核对。覆盖模型、
诊断、绘图与 treatment 导入的 47 个源文件，与发布标签
逐字节一致。API 审查涵盖每份参考件中的构造函数、
拟合选项、结果属性与预测语义。查看源码
与数值执行是两回事。

快速上手可依次执行。其余参考件是情境片段：
要提供其中具名的输入，并为每节保留对应的模型结果；
它们不是可以拼接的单一脚本。原生合成检查覆盖修正后的
契约、线性/GLM/离散/时间序列模型与诊断。它们确立的是 API
行为与数值恒等式，不是估计量校准、真实研究的功效、
因果识别，也不是已拟合科学模型的有效性。可选的自定义
MLEModel 子类、手工比例优势检验与任意用户数据集仍只是
示意，需要单独验证。

## 主要 API 来源与关键契约

- [OLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html),
  [robust covariance](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.get_robustcov_results.html),
  [RecursiveLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.recursive_ls.RecursiveLS.html),
  [MixedLM.fit](https://www.statsmodels.org/stable/generated/statsmodels.regression.mixed_linear_model.MixedLM.fit.html):
  截距/设计对齐；递推估计是扩展窗口估计；
  ML 与 REML 之别、协方差假设都要留意。
- [GLM.fit](https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_linear_model.GLM.fit.html),
  [GLM prediction](https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_linear_model.GLMResults.get_prediction.html),
  [pseudo R-squared](https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_linear_model.GLMResults.pseudo_rsquared.html):
  拟合时指定稳健协方差，预测时请求目标量，用
  基于似然的 pseudo-R² 与 `bic_llf`，并为新数据保留 exposure。
- [Marginal effects](https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.DiscreteResults.get_margeff.html),
  [ZIP prediction](https://www.statsmodels.org/stable/generated/statsmodels.discrete.count_model.ZeroInflatedPoisson.predict.html),
  [OrderedModel](https://www.statsmodels.org/stable/generated/statsmodels.miscmodels.ordinal_model.OrderedModel.html),
  [ConditionalLogit](https://www.statsmodels.org/stable/generated/statsmodels.discrete.conditional_models.ConditionalLogit.html),
  [hurdle](https://www.statsmodels.org/stable/generated/statsmodels.discrete.truncated_model.HurdleCountModel.html):
  `overall` 给出 AME；`atexog` 的键是列号；膨胀与
  观测到零不同；有序/条件模型禁止常数项；有序阈值
  增量需要变换。Hurdle 的零/计数两个过程共用 exog。
- [ADF](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.adfuller.html),
  [KPSS](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.kpss.html),
  [SARIMAX forecasting](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAXResults.get_forecast.html),
  [Ljung-Box](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.acorr_ljungbox.html),
  [VARMAX](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.varmax.VARMAX.html):
  用具名结果对象，区分各检验的原假设，提供未来 exog，考虑
  已拟合的动态参数与初始化，避免不可识别的无约束
  VARMA 设定。`MarkovRegression.order` 不会添加 AR 系数。
- [RESET](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.linear_reset.html),
  [AnovaRM](https://www.statsmodels.org/stable/generated/statsmodels.stats.anova.AnovaRM.html),
  [pairwise comparisons](https://www.statsmodels.org/stable/generated/statsmodels.stats.multicomp.pairwise_tukeyhsd.html),
  [proportion effect size](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_effectsize.html),
  [SciPy Levene](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html):
  RESET 返回结果对象；重复测量 ANOVA 要求数据平衡，且
  缺少球形性校正；0.15 通过 `use_var="unequal"` 加入 Games-Howell；
  比例功效用 Cohen's h，CompareMeans 没有 `test_equal_var` 方法。
- [TreatmentEffect](https://www.statsmodels.org/stable/generated/statsmodels.treatment.treatment_effects.TreatmentEffect.html)
  及其 [released implementation](https://github.com/statsmodels/statsmodels/blob/v0.15.0/statsmodels/treatment/treatment_effects.py):
  OLS 结果建模仍是受支持的路径。`ipw_ra`/`aipw_wls` 的 GMM 仍
  切取最后六个选择参数；非六参数设计会抛出形状
  错误。仅点估计的路径不提供标准误。不要为迁就
  该实现缺陷而改动科学设计。

## 已执行的检查与局限

隔离套件运行 8 项原生测试，涵盖全部 173 个带显式合成
情境的 Python 围栏块（有些块只导入或说明某工作流）。
断言覆盖设计形状、OLS 区间宽度、GLM 均值不确定性与稳健
协方差、AME 导数、ZIP 混合概率、有序阈值、多项
结果、选定 ARIMA 的收敛与预测日期保留，以及处理效应
恒等式与已知的 GMM 失败。

宽泛的 ARIMA 网格对部分候选给出预期的不收敛警告；
选择过程会排除这些候选并保留选定的结果。KPSS 报告
表边界 p 值。Gamma inverse/binomial log 连接会发出定义域警告，
真实数据上需要显式检查支撑集。Johansen 检验在所测 NumPy
栈中给出复数转实数警告；合成特征值的虚部恰为零，
迹/最大特征值统计量有限。该夹具检查并不能
普遍证明在其他数据上可以丢弃复数分量。绘图用非交互式
Agg backend 跑过；未做出版排版认证，
也未做区间覆盖率的实证研究。
