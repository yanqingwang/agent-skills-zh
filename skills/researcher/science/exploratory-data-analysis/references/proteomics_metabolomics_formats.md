> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/exploratory-data-analysis/references/proteomics_metabolomics_formats.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 蛋白质组学与代谢组学格式

**审阅时间：** 2026-09-30
**可执行范围：** 仓库内脚本不解析任何组学原生标准。
矩形的 CSV/TSV 结果导出在确认模式、单位与缺失/删失编码之后，
可以使用通用的表格 CLI。

## 精确的能力边界

| 格式 | 仓库内自带原生检查 | 状态 |
|---|---|---|
| mzML/mzXML、厂商 RAW | 不支持 | 仅作参考的 MS 工具链；见 `spectroscopy_analytical_formats.md` |
| mzIdentML（`.mzid`、`.mzIdentML`） | 不支持 | 仅作参考、感知 PSI schema/CV 的工具链 |
| mzTab 1.0 / mzTab-M 2.0 | 不支持 | 仅作参考、区分版本的校验器；通用 TSV 解析不够用 |
| pepXML/protXML | 不支持 | 仅作参考、感知检索/推断的解析器 |
| featureXML/consensusXML/idXML | 不支持 | 仅作参考的 OpenMS 工具链 |
| 矩形的 `.csv`/`.tsv` 特征或丰度表 | 通用脚本 | 有界的聚合表格 EDA，不含组学语义 |
| `.h5`/`.hdf5` | 仅通用元数据 | 不读取载荷值，也不做约定校验 |
| `.h5ad`、`.loom` | 无语义支持 | 见生物信息学参考文件 |
| 被 pickle 的模型/结果 | **绝不** | 索取不可执行的导出 |

未知格式一律失败关闭。不会从自由文本元数据或
内容猜测来判定格式。

## mzML 与原始谱图

mzML 是 HUPO-PSI 关于谱图/色谱图的标准；请使用 PSI 感知的工具链。
厂商 RAW 扩展含义不明确，通常需要厂商库或
转换。请保留原件，并记录转换器、版本、选项与
校验和。

对于光谱 EDA，请清点：

- 采集方法、仪器、极性、MS 级数、扫描模式、前体
  隔离/激活、分辨率，以及是 centroid 还是 profile；
- 运行顺序、批次、空白样、混合 QC、标准品、残留、漂移与
  校准；
- 谱图/色谱图数量、保留时间/迁移时间范围、m/z 覆盖度、TIC/
  BPC、峰数量，以及缺失/损坏的扫描；以及
- 处理历史、受控词表术语、源文件与单位。

不要自动质心化、去噪、重新校准、对齐、寻峰或
丢弃谱图。

## 鉴定相关格式

### mzIdentML

mzIdentML 用受控词表表示肽段/蛋白质鉴定结果、评分、检索
参数、数据库、修饰以及与谱图的关联。请用 PSI 感知的工具链校验
schema 与 CV 映射。

检查：

- 搜索引擎/版本、序列数据库/版本、decoy 策略、酶、
  容差、固定/可变修饰，以及谱图引用；
- 评分方向/含义、排名、电荷、质量误差、肽段-谱图匹配、
  肽段、蛋白质与蛋白质组；
- 各报告层级上的 target/decoy 与 FDR 方法；以及
- 共享肽段、不可区分蛋白质与推断带来的歧义。

评分阈值并不自动等于经过验证的 FDR 阈值。不要在
缺少方法与 decoy 设计的情况下重算或重新解读置信度。

### pepXML/protXML

这些格式属于 Trans-Proteomic Pipeline 的约定。请在已知生成
软件/版本的前提下使用 Pyteomics 或 TPP 工具。保留搜索引擎、
PeptideProphet/ProteinProphet、修饰、decoy 与推断的上下文。

## mzTab 与 mzTab-M

HUPO-PSI 列出：

- mzTab 1.0.0 作为最终的蛋白质组学版本（2014 年 6 月通过）；以及
- mzTab-M 2.0.0 作为最终的代谢组学/小分子版本（2019 年 3 月
  通过）。

mzTab-M 2.1.0 被列为草案，不是最终标准。不要悄悄把它
当作 2.0。该草案已移至单独的
[HUPO-PSI/mzTab-M 仓库](https://github.com/HUPO-PSI/mzTab-M)；已发布的
2.0 材料仍保留在 HUPO-PSI/mzTab 中。

虽然 mzTab 是制表符分隔的，但它有分节专属的行类型、元数据、
受控词表、可选列与空值约定。通用的
矩形 TSV 扫描器不是校验器，会拒绝合法的
非矩形分节结构。请使用 PSI 规范/参考
校验器，必要时再导出一份受控的矩形分析表。

## 矩形定量表

常见输出把特征/肽段/蛋白质/代谢物放在行、样本放在列，
或者采用长表形式的测量值。在使用通用 CLI 之前，
请建立一份数据字典，记录：

- 行实体与标识符命名空间/版本；
- 样本/受试者/标本、条件、批次、进样顺序与 QC 角色；
- 丰度尺度（原始强度、面积、计数、比值、归一化/取对数）；
- 零值、缺失、被删失、被过滤、未鉴定与未定量的编码；
- 已经施加的归一化、变换、插补、上卷汇总与批次校正；
- 内标、稀释、LOD/LOQ、扣空白与检出频率；以及
- 肽段到蛋白质、特征到代谢物的歧义。

不要假定零值是实测零值。缺失常常依赖于丰度、
特征、批次或鉴定结果，并且可能不是随机的。

### 安全命令

```bash
python scripts/tabular_profile.py abundance.csv \
  --root /approved/project \
  --missing-token NA \
  --max-rows 100000

python scripts/missingness_leakage_audit.py abundance.csv \
  --root /approved/project \
  --group-column condition \
  --entity-column subject_id \
  --split-column split \
  --time-column acquisition_time

python scripts/distribution_sensitivity.py abundance.csv \
  --root /approved/project \
  --column intensity
```

这些列参数是精确的本地标识符；除非显式给出
`--reveal-identifiers`，输出会把它们令牌化。数值以及受试者/样本标识符
不会被输出。

## 缺失、删失与限值

至少要区分：

- 结构性缺失/不适用；
- 未检出；
- 已检出但低于定量限；
- 鉴定失败或未通过置信度过滤；
- 提取/积分失败；
- 在预处理阶段被过滤；
- 饱和/超出量程；以及
- 真正缺失的元数据。

把标记与限值放在彼此独立的列中。不要自动把
未检出替换为零、半最小值、LOD/2 或随机抽样值。按特征、样本、条件、批次与运行顺序
报告缺失/删失比例，并
比较各种有科学依据的处理策略下的结论。

## 分布与离群值敏感性

对于丰度表：

- 检查样本总量/检出率与特征检出频率；
- 在不覆盖原始数据的前提下，比较原始尺度与有科学依据的对数/方差稳定化
  诊断；
- 比较均值/标准差与中位数/IQR/MAD，以及留一样本/留一批次的敏感性；
- 结合空白样/QC/内标表现、
  采集顺序、污染、残留与样品处理排查离群值；以及
- 保留被排除的样本/特征并注明原因，同时展示敏感性。

PCA/聚类可以揭示结构，但不是批次、身份或
生物学分离的证据。只在训练数据上拟合变换与特征选择。

## 设计、泄漏与推断

1. 定义独立实验单元；技术进样、谱图、
   肽段或特征通常不是独立受试者。
2. 保留受试者/样本配对、重复测量、批次、场地与
   采集顺序。
3. 在归一化、插补、特征选择、PCA 或模型调参之前，
   先按受试者/标本/批次/时间划分。
4. 确保源自同一个样本的谱图/肽段/特征不会跨越
   训练/测试边界。
5. 区分 QC、空白样、混合样、校准物与生物样本。
6. 在评估错误率时，把鉴定/特征发现与差异检验当作彼此独立的
   选择阶段。
7. 定义假设族（特征、对比、终点），并报告
   效应量/不确定性以及合适的 FWER/FDR 方法。
8. 把来自 EDA 的发现标注为探索性，并在独立数据上确认。
9. 不要从描述性模式做出生物标志物、诊断、机理、暴露或因果方面的论断。

## HDF5 与相关容器

通用 HDF5 检查器只报告有界的层级/数据集元数据。它
不会：

- 读取谱图、丰度矩阵、注释或属性；
- 跟随软链接/外部链接或外部数据集存储；
- 校验 mzMLb、H5AD、Loom 或厂商 schema；或
- 调用 filter 插件来解压数据集。

语义问题请使用该约定官方的读取器/校验器。NumPy 对象
数组以及所有基于 pickle 的对象一律拒绝。

## 权威来源

当前解析器 API 与格式指南审阅于 2026-09-30。历史方法学
引用保留下来作为来源背景。

- HUPO-PSI，[mzML 规范/状态](https://www.psidev.info/mzml)
  （mzML 1.1.0 长期稳定）。
- HUPO-PSI，[mzIdentML](https://www.psidev.info/mzidentml)。
- HUPO-PSI，[mzTab 规范](https://www.psidev.info/mztab-specifications)
  （页面更新于 2024-04-19；mzTab 1.0.0 终稿、mzTab-M 2.0.0 终稿、
  mzTab-M 2.1.0 草案）。
- HUPO-PSI，[mzTab 仓库与已发布规范](https://github.com/HUPO-PSI/mzTab)。
- Hoffmann 等（2019），[mzTab-M 2.0](https://doi.org/10.1021/acs.analchem.8b04310)，
  发表于 2019-01-28。
- Pyteomics，[格式文档](https://pyteomics.readthedocs.io/en/latest/)。
- OpenMS，[可识别的文件类型](https://openms.de/documentation/structOpenMS_1_1FileTypes.html)。
- US EPA，[检出限最佳实践指南](https://www.epa.gov/system/files/documents/2025-09/wqxdetectionlimitsbestpracticesguide_final.pdf)，
  日期为 2025 年 8 月。
- FDA/ICH E9(R1)，[敏感性分析指南](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e9r1-statistical-principles-clinical-trials-addendum-estimands-and-sensitivity-analysis-clinical)，
  最终版发布于 2021 年 5 月。
- Benjamini 与 Hochberg（1995），[FDR 控制](https://academic.oup.com/jrsssb/article/57/1/289/7035855)。
- scikit-learn，[数据泄漏指南](https://scikit-learn.org/stable/common_pitfalls.html)。
