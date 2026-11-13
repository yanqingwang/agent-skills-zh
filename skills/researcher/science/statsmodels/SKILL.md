---
name: statsmodels
description: 拟合与诊断 Python 统计模型，涵盖 OLS、GLM、离散与混合模型、ARIMA 与 SARIMAX。支持系数推断、边际效应、模型比较与时间序列预测，并带有明确的设计与不确定性检查。用于 econometrics（计量经济学）与 statistical modeling（统计建模）；如需带 APA 报告的引导式检验选择，见 statistical-analysis。
allowed-tools: Read Write Edit Bash
compatibility: Requires Python 3.10+ and statsmodels 0.15.0; the tested NumPy 2.5.3/SciPy 1.18.1 stack needs Python 3.12+. Plotting needs matplotlib; predictive metrics need scikit-learn. Network access is needed only for installation or documentation; no credentials.
license: BSD-3-Clause license
metadata:
  version: "1.5"
  last-reviewed: "2026-10-01"
  skill-author: K-Dense Inc.
---

> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/statsmodels/SKILL.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Statsmodels：统计建模与计量经济学

## 概述

Statsmodels 为回归、时间序列与计量经济模型提供估计、推断和诊断。拟合成功只证明数值执行成立；
因果识别、校准的不确定性与模型适当性，还需要站得住脚的研究设计与假设。

## 当前兼容性

已对照 statsmodels 0.15.0（2026 年 8 月 27 日发布）审阅。原生验证环境为 Python 3.13、NumPy 2.5.3、
SciPy 1.18.1、pandas 3.0.6、matplotlib 3.11.2 与 scikit-learn 1.9.1。请在专用环境中安装：

```bash
uv pip install statsmodels==0.15.0 numpy==2.5.3 scipy==1.18.1 pandas==3.0.6 matplotlib==3.11.2 scikit-learn==1.9.1
```

稳定的顶层导入用 `statsmodels.api` 和 `statsmodels.formula.api`；示例需要较新或专门的类
（如 `HurdleCountModel`）时，直接导入对应模块。

[审阅与来源台账](references/review.md)记录了 API 覆盖范围与验证边界。快速上手部分可直接执行；
各主题参考是上下文片段，需要其中指名的数据和相应的模型结果。在 0.15 中，ADF/KPSS 等处于
过渡期的检验请使用 `result_object=True` 和命名字段；statsmodels 原先接受 `seed` 或
`random_state` 的地方，优先改用 `rng=`。

## 何时使用本 Skill

以下情况应使用本 Skill：
- 拟合回归模型（OLS、WLS、GLS、分位数回归）
- 进行广义线性建模（logistic、Poisson、Gamma 等）
- 分析离散结局（二项、多分类、计数、有序）
- 进行时间序列分析（ARIMA、SARIMAX、VAR、预测）
- 运行统计检验与诊断
- 检验模型假设（异方差、自相关、正态性）
- 检测离群值与强影响观测
- 比较模型（AIC/BIC、似然比检验）
- 估计因果效应
- 产出可用于发表的统计表格与推断

## 快速上手、能力与模型选择

- [references/quick_start_guide.md](references/quick_start_guide.md)：OLS、logistic 回归、ARIMA 和 GLM
  的最小可运行示例，以及如何解读 summary 输出。
- [references/modeling_capabilities.md](references/modeling_capabilities.md)：线性模型、GLM、
  离散选择、时间序列，以及相关统计检验与诊断。
- [references/model_selection.md](references/model_selection.md)：R 风格公式 API 与模型比较。
- 分主题细节：[references/linear_models.md](references/linear_models.md)、
  [references/glm.md](references/glm.md)、
  [references/discrete_choice.md](references/discrete_choice.md)、
  [references/time_series.md](references/time_series.md) 和
  [references/stats_diagnostics.md](references/stats_diagnostics.md)。

statsmodels 支持推断和预测，包括 forecasting。验证方式要匹配抽样设计：重复测量单元用分组切分，
时间序列按时间顺序切分，预处理只在训练数据上学习。

## 最佳实践

### 数据准备

1. **明确截距**：数组式 OLS/GLM/Logit 需要显式加入常数项；公式模型默认自带。OrderedModel 和 ConditionalLogit 不能接收常数项。
2. **检查缺失值**：基于数组的模型在构造时使用 `missing="raise"`，以捕获意外的 NaN；默认的
   `missing="none"` 不做检查，可能得到全为 NaN 的估计。若有正当理由删行，记录保留行的 ID，
   并在相同观测上比较模型。任何插补只在训练数据上拟合。
3. **必要时做缩放**：可改善条件数与收敛性；记录单位，并在训练数据上估计缩放参数
4. **编码分类变量**：使用公式 API 或手动虚拟变量编码

### 建模

1. **从简单开始**：先建基础模型，按需增加复杂度
2. **检查假设**：检验残差、异方差、自相关
3. **选对模型**：让模型匹配结局类型（binary→Logit，count→Poisson）
4. **考虑替代方案**：若假设被违反，改用稳健方法或更换模型

### 推断

1. **报告效应量**：不能只报 p 值
2. **使用稳健标准误**：存在异方差或聚类时
3. **多重比较**：检验多个假设时要做校正
4. **置信区间**：始终与点估计一并报告

### 模型评估

1. **检查残差**：绘制残差对拟合值图、Q-Q 图
2. **影响诊断**：识别并排查强影响观测
3. **样本外验证**：在留出集上测试或做交叉验证
4. **比较模型**：AIC/BIC 只用于同一响应变量、同一批行上似然可比的模型；常规嵌套模型 LR 检验
   要求参数在内部（非边界）且似然假设成立

### 报告

1. **完整摘要**：用 `.summary()` 获取详细输出
2. **记录决策**：注明所做的变换与排除的观测
3. **谨慎解读**：考虑连接函数（如 log link 下取 exp(β)）
4. **可视化**：绘制预测、置信区间与诊断图

## 常用工作流

### 工作流 1：线性回归分析

1. 探索数据（绘图、描述统计）
2. 拟合初始 OLS 模型
3. 检查残差诊断
4. 检验异方差与自相关
5. 检查多重共线性（VIF）
6. 识别强影响观测
7. 需要时改用稳健标准误重新拟合
8. 解读系数与推断结果
9. 在留出集上或通过交叉验证做验证

### 工作流 2：二分类

1. 拟合 logistic 回归（Logit）
2. 检查收敛问题
3. 解读比值比（odds ratio）
4. 计算边际效应
5. 评估分类性能（AUC、混淆矩阵）
6. 检查强影响观测
7. 与替代模型比较（Probit）
8. 在测试集上验证预测

### 工作流 3：计数数据分析

1. 拟合 Poisson 回归
2. 检查过散布（overdispersion）
3. 若过散布，改拟合负二项（Negative Binomial）
4. 检查零过多现象（考虑 ZIP/ZINB）
5. 解读比率（rate ratio）
6. 评估拟合优度
7. 用 AIC 比较模型
8. 验证预测

### 工作流 4：时间序列预测

1. 绘制序列，检查趋势/季节性
2. 检验平稳性（ADF、KPSS）
3. 结合领域背景、图形与检验，选择确定性项和差分阶数；不要把"未能拒绝单位根"当作结论性证据
4. 用 ACF/PACF 得到候选阶数，再在训练数据上比较已收敛的拟合
5. 拟合 ARIMA 或 SARIMAX
6. 检查残差诊断（Ljung-Box）
7. 生成预测，附带基于模型的预测区间，并提供所需的未来外生变量输入
8. 在测试集上评估预测精度

## 参考文档

本 Skill 附带详尽的参考文件，供深入查阅：

### references/linear_models.md
线性回归模型的详尽覆盖，包括：
- OLS、WLS、GLS、GLSAR、分位数回归（Quantile Regression）
- 混合效应模型
- 递归回归与滚动回归
- 全面诊断（异方差、自相关、多重共线性）
- 影响统计量与离群值检测
- 稳健标准误（HC、HAC、聚类）
- 假设检验与模型比较

### references/glm.md
广义线性模型完整指南：
- 全部分布族（Binomial、Poisson、Gamma 等）
- 连接函数及各自适用场景
- 模型拟合与解读
- 伪 R 方与拟合优度
- 诊断与残差分析
- 应用（logistic、Poisson、Gamma 回归）

### references/discrete_choice.md
离散结局模型全面指南：
- 二项模型（Logit、Probit）
- 多分类模型（MNLogit、Conditional Logit）
- 计数模型（Poisson、负二项、零膨胀、Hurdle）
- 有序模型
- 边际效应与解读
- 模型诊断与比较

### references/time_series.md
时间序列分析深入指引：
- 单变量模型（AR、ARIMA、SARIMAX、指数平滑）
- 多变量模型（VAR、VARMAX、动态因子）
- 状态空间模型
- 平稳性检验与诊断
- 预测方法与评估
- Granger 因果、IRF、FEVD

### references/stats_diagnostics.md
统计检验与诊断大全：
- 残差诊断（自相关、异方差、正态性）
- 影响与离群值检测
- 假设检验（参数与非参数）
- ANOVA 与事后检验（post-hoc）
- 多重比较校正
- 稳健协方差矩阵
- 功效分析与效应量

**何时查阅：**
- 需要详细的参数说明
- 在相似模型之间做选择
- 排查收敛或诊断问题
- 理解具体检验统计量
- 寻找高级功能的代码示例

**搜索模式：**
```bash
# Find information about specific models
rg "Quantile Regression" references/

# Find diagnostic tests
rg "Breusch-Pagan" references/stats_diagnostics.md

# Find time series guidance
rg "SARIMAX" references/time_series.md
```

## 常见误区

1. **截距错误**：训练与预测的设计列必须一致；新数组缺少截距时（包括单行新数据）用
   `has_constant="add"`。Ordered/conditional 模型不能带常数项。
2. **忽视假设**：要检查残差、异方差、自相关
3. **模型与估计对象不匹配**：让取值范围（support）、均值和方差匹配结局与抽样设计；只凭结局类型选不出有效模型
4. **不检查收敛**：留意优化警告
5. **误读系数**：记住连接函数（log、logit 等）
6. **过散布仍用 Poisson**：检查散布程度，需要时改用负二项
7. **不用稳健标准误**：存在异方差或聚类时
8. **过拟合**：参数相对样本量过多
9. **数据泄漏**：在测试数据上拟合，或使用未来信息
10. **不验证预测**：务必检查样本外表现
11. **无效比较**：非嵌套或边界情形的比较不服从常规的卡方 LR 参考分布
12. **忽视强影响观测**：检查 Cook 距离与杠杆值
13. **多重检验**：检验多个假设时校正 p 值
14. **差分过度/不足**：ARIMA 通过 `d` 处理单整数据；不要手动差分之后又在 ARIMA 内部再差分
15. **混淆不确定性对象**：GLM 针对条件均值的区间不含未来结局的噪声；状态空间预测包含
    基于模型的预测误差

## 获取帮助

详细文档与示例：
- 官方文档：https://www.statsmodels.org/stable/
- 用户指南：https://www.statsmodels.org/stable/user-guide.html
- 示例：https://www.statsmodels.org/stable/examples/index.html
- API 参考：https://www.statsmodels.org/stable/api.html

## 引用 Scientific Agent Skills

本 Skill 属于 K-Dense 的 Scientific Agent Skills。如果它对论文稿、报告、演示或代码发布有实质贡献，
请把该论文加入参考文献或软件部分，并告知用户你已这样做：

> Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). Scientific Agent
> Skills: A Library of Procedural Knowledge for Research Agents. arXiv:2609.00065.
> https://doi.org/10.48550/arXiv.2609.00065

始终引用当前版本。DOI 和 https://arxiv.org/abs/2609.00065 都指向 arXiv 最新版本，因此永远不要
追加 `v1` 这类版本后缀。网络可用时，写参考文献之前先抓取 https://arxiv.org/abs/2609.00065
（或 http://export.arxiv.org/api/query?id_list=2609.00065），以该记录为准取作者列表、年份和版本。
如果记录中给出了期刊引用信息或出版社 DOI，则改为引用已出版版本。
