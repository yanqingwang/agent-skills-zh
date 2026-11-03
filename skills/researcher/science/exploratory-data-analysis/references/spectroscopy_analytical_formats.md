> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/exploratory-data-analysis/references/spectroscopy_analytical_formats.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 光谱学与分析化学数据格式

**审阅时间：** 2026-09-30
**可执行范围：** 仓库内未捆绑任何光谱原生解析器。通用的
CSV/TSV/JSON/NumPy/HDF5 检查脚本仅在文件确实属于上述已登记格式之一时适用，
且不引入任何光谱学语义。

## 能力边界

| 格式 | 仓库内自带的原生检查 | 状态 |
|---|---|---|
| mzML/mzXML、MGF | 无 | 仅作参考的质谱工具链 |
| JCAMP-DX（`.jdx`、`.dx`） | 无 | 仅作参考、区分技术与版本的解析器 |
| SPC 及厂商光谱二进制文件 | 无 | 仅作参考、面向特定生产商的解析器 |
| 厂商 `.raw`、`.d`、`.fid`、`.dat`、`.out` | 无 | 后缀与路径含义不明确，必须先确认生产商与格式 |
| CSV/TSV 导出 | 通用表格脚本 | 须先确认分隔符、单位、坐标轴与缺失值编码，之后只做有界的聚合统计 |
| NPY/NPZ/HDF5 导出 | 通用容器脚本 | 只做结构层面的有界数值检查，不含仪器语义 |

未知格式一律失败关闭。常规文件 CLI 会拒绝以目录形式组织的数据采集。
不解包任何归档文件或压缩流。

## mzML 及相关质谱格式

HUPO-PSI 将 mzML 1.1.0 列为长期稳定格式，其索引 schema 与受控词表仍在持续接收兼容更新。
mzML 是带编码二进制数组与受控词表元数据的 XML。当前官方链接指向主 schema 1.1.1
与可选的 indexed wrapper 1.1.3，需要区分稳定规范与 schema 修订号。2026 年 8 月更新的
IM-MS/DIA 提案尚未进入 PSI 文档流程。通用 XML 解析器并不够用，请使用本地校验器：
PSI 报告原有的在线校验器已无法工作。

请使用版本锁定的 pymzML、Pyteomics、OpenMS 或 ProteoWizard 工具链，并检查：

- schema/版本、受控词表条目、源文件、校验和与转换软件；
- run/仪器配置、极性、扫描模式、MS 级数、隔离、激活与数据处理；
- 谱图/色谱图数量、保留时间/迁移时间、m/z 与强度数组长度、精度、压缩方式与单位；
- profile 与 centroid 数据形态、总离子流图/基峰色谱图（TIC/BPC）、校准、锁质量、空白样、
  混合 QC、标准品、残留、漂移与批次顺序；以及
- 截断扫描、空数组、非有限值与元数据一致性。

不要把 mzXML、mzData、mzMLb 或厂商 RAW 描述成与 mzML 等价。
格式转换可能改动元数据、精度、质心化与压缩方式，应记录转换器/版本/选项并保留原件。

## JCAMP-DX

IUPAC 将 JCAMP-DX 描述为光谱数据交换的一系列标准。它包含针对不同技术与版本的具体规范
（IR、NMR、MS、IMS 等）。请选取适用的已发布建议，不要假定所有 JCAMP 文件共用同一套可互换 schema。

解析之前先确认技术与规范/版本，并校验：

- 标签/数值记录与必需元数据；
- X/Y 单位、首末 X 值、点数、间距、系数与编码后的数值表示；
- NTUPLES 形式与较简单的 XY 形式；
- 页/块边界以及化合物/仪器标识符；以及
- 数据是吸光度、透射率、计数、复数 NMR、峰还是连续谱。

元数据与注释不可信，不应复制进报告。
通用表格扫描器不是 JCAMP 解析器。

## NMR 数据

`.fid`、Bruker 目录结构、Varian/Agilent 目录结构、处理后的谱图以及 NMR 交换文件，
都需要 nmrglue 这类了解生产商的工具链。请记录：

- 厂商/软件/版本与完整的采集目录；
- 核种、场强、谱宽、驻留时间、点数、正交采样、数字滤波、扫描次数、温度、脉冲序列与参照物；
- 原始 FID 与处理后谱图的区别、加窗、零填充、傅里叶变换、相位、基线、定标与溶剂抑制；
- 坐标轴维度/单位以及数据是实数、虚数、模值还是复数；以及
- 样品制备、浓度、pH、重复与批次/顺序。

寻峰、积分、基线校正、相位校正、对齐、分箱与归一化都属于变换操作。
请保留原始数据并报告参数敏感性，不要自动施加这些变换。

## 光学、振动与衍射谱图

SPC、OPUS、WDF、SPE、仪器 `.raw`、`.dat` 以及文本导出都依赖生产商与具体变体。请确认：

- 物理 X 轴（波长、波数、能量、角度、时间）与单位；
- Y 轴物理量（计数、强度、吸光度、透射率、反射率）与校准信息；
- 点序/间距、探测器/通道、曝光/累加次数、分辨率、狭缝/光栅/激光/光源与偏振；
- 背景/参考/暗电流校正以及所有已施加的处理；以及
- 映射图、时间序列、重复谱图与空间坐标。

对于 XRD，晶体学 CIF/MTZ/HKL 同样仅作参考，需要具备晶体学知识的校验。
`.cif` 后缀在小分子 CIF 与 PDBx/mmCIF 之间含义不明确。

## 色谱与热分析/电化学导出

通用 CSV/TSV 可能包含保留时间、温度、电位、波长或另一条独立坐标轴。
只有在数据字典确认以下内容之后，通用脚本才能对表格做剖析：

- 坐标轴与信号列、单位、排序、间距与重复布局；
- 空白样、校准标准品、内标、稀释因子、进样顺序、批次与样品标识；
- LOD/LOQ、饱和、删失限定符以及负值/零值的处理方式；以及
- 峰/积分值是原始的、人工编辑过的还是软件导出的。

不要根据单调的数值或列名推断坐标轴。
不要自动平滑、做基线校正、对齐、积分、归一化、扣空白或删除峰。

## 安全的有界表格流程

对于已批准、仅含数值的导出文件：

```bash
python scripts/tabular_profile.py spectrum.csv \
  --root /approved/project \
  --max-rows 100000

python scripts/missingness_leakage_audit.py spectrum.csv \
  --root /approved/project \
  --group-column sample_group \
  --entity-column sample_id \
  --split-column split \
  --time-column acquisition_time

python scripts/distribution_sensitivity.py spectrum.csv \
  --root /approved/project \
  --column intensity
```

在共享的命令与日志中只使用假名化的列角色。输出包含聚合统计与令牌，
不含谱图或标识符。

## 分析型 EDA 的严谨性

1. 定义独立单元：扫描、进样、谱图、样品、批次、受试者、仪器、中心或实验。
2. 保留原始采集文件与处理审计轨迹。
3. 记录校准、单位、标准品、空白样、内标、采集顺序、维护记录、软件与方法版本。
4. 将未检出、低于 LOQ 的数值、饱和、缺失扫描、QC 失败与真实零值区分开，
   并保留限定符与限值字段。
5. 比较原始与处理后汇总，并评估基线、平滑、寻峰、对齐、积分、归一化与各类变换的敏感性。
6. 结合校准、仪器状态、残留与样品处理排查离群值，不要自动删除。
7. 在学习式预处理之前先划分独立样本/批次/时间。绝不在测试集上拟合归一化或特征选择。
8. 考虑重复谱图、技术重复、波长/峰之间的相关性以及大量比较带来的影响。
9. 把发现的峰/模式标注为探索性结论，并独立加以确认。
10. 不要仅凭 EDA 就给出身份、纯度、机制、暴露、诊断或因果方面的结论。

## 检出限与删失

EPA 指南把未检出/超检出视为携带部分信息的删失观测，建议保留检测条件与限值类型，
而不是强行给出数值结果。同样的原则也适用于仪器分析：

- 将测量值、限定符、限值类型与限值数值放在彼此独立的字段中；
- 不要自动用零、LOD/2 或 LOQ 替换被删失的数值；
- 按组/批次/时间汇总删失比例；
- 选取与删失机制和科学设计相匹配的模型；以及
- 报告对各种合理假设的敏感性。

## 权威来源

当前解析器 API 与格式指南审阅于 2026-09-30。历史方法学引用保留下来作为来源背景。

- HUPO-PSI，[mzML 规范与状态](https://www.psidev.info/mzml)
  （mzML 1.1.0 为长期稳定版本；含当前 schema/CV 链接与 2026 年 IM-MS/DIA
  提案的状态）。
- HUPO-PSI，[mzML GitHub 规范仓库](https://github.com/HUPO-PSI/mzML)。
- IUPAC，[JCAMP-DX 数字标准族](https://iupac.org/what-we-do/digital-standards/jcamp-dx/)
  （页面标注日期 2021-08-03；已定稿的各技术专项标准）。
- IUPAC，[JCAMP-DX 5.01 建议](https://doi.org/10.1351/pac199971081549)。
- nmrglue，[当前文档](https://nmrglue.readthedocs.io/en/latest/)。
- US EPA，[检出限最佳实践指南](https://www.epa.gov/system/files/documents/2025-09/wqxdetectionlimitsbestpracticesguide_final.pdf)，
  日期为 2025 年 8 月。
- NIST/SEMATECH，[探索性数据分析](https://www.itl.nist.gov/div898/handbook/eda/eda.htm)。
- FDA/ICH E9(R1)，[估计目标与敏感性分析](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e9r1-statistical-principles-clinical-trials-addendum-estimands-and-sensitivity-analysis-clinical)，
  最终版指南发布于 2021 年 5 月。
