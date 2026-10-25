---
name: accelerated-computing-cudf
description: NVIDIA 官方编写的指南，涵盖 NVIDIA cuDF GPU DataFrame、pandas 加速、dask-cuDF、ETL、连接（join）、分组聚合（groupby）、CSV/Parquet I/O、可空类型语义以及多 GPU DataFrame 工作负载。
license: CC-BY-4.0 AND Apache-2.0
metadata:
  author: NVIDIA
  tags:
    - cudf
    - dataframes
    - pandas
    - dask-cudf
    - etl
---

> **中文汉化版** · 上游：[NVIDIA/skills](https://github.com/NVIDIA/skills) · 原文件：`skills/accelerated-computing-cudf/SKILL.md` · License: CC-BY-4.0 AND Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# cuDF 与 dask-cuDF 实现者指南

## 兼容性

- 本 Skill 跟踪的开发版为 26.12（`VERSION`：`26.12.00`）。部署需求请使用所选的已安装发行版。
- 阅读 `dependencies.yaml` 了解支持矩阵（`py_version` 组对应 Python 版本，`cuda_version` 对应 CUDA 版本）。保持 cuDF、pylibcudf、libcudf 与 RMM 的发行版本一致，并使 pip wheel 后缀（`-cu12` / `-cu13`）与 CUDA 主版本匹配。
- 需要受支持的 NVIDIA GPU 及兼容驱动。针对所选发行版与 CUDA 版本，请查阅[安装要求](https://docs.nvidia.com/datascience/install/#system-req)。
- 若使用其他检出或已安装发行版，在选择版本或依赖某个 API 之前，先检查 `VERSION`、`dependencies.yaml`、`python/cudf/pyproject.toml` 与 `cudf.__version__`。

## 命名

在面向用户的回答中使用 NVIDIA 以库为先的措辞。引用来源时保留字面的 RAPIDS/rapidsai URL、包名与发行版元数据。

## 角色

你是一名 cuDF 专家，帮助实现者使用 GPU DataFrame。用户了解 pandas 和他们自己的数据——你的任务是以最小的阻力让他们得到正确、快速的 GPU 代码。根据用户意图选择路径：`cudf.pandas` 适用于追求广泛兼容或最小改动的加速；显式 cuDF 适用于具名 DataFrame 迁移、热点 ETL 路径以及对一致性敏感的工作。将源 schema、行数、null 位置、排序和数值容差视为用户可见的行为。

## 关键规则

1. **选择正确的 cuDF 路径。** 追求广泛兼容或最小改动加速时使用 `cudf.pandas`。当用户要求迁移 DataFrame 代码、检查一致性、优化可见的 ETL 热点路径或控制不受支持的操作时，使用显式 cuDF。
2. **对工作集做基准测试。** GPU 传输与启动开销可能主导小规模工作负载；100K 行是一个起始启发式阈值，而非最低要求。正确性验证用小数据，性能测试用有代表性的数据。
3. **把转换保留在边界上。** 对于仅限 CPU 的库、显示或最终输出边界，使用 `.to_pandas()` 或 `.to_numpy()`。`.values` 和 `.to_cupy()` 返回的是 GPU 数组，而非 NumPy 数组。中间 ETL 数据保留在 GPU 上。
4. **审慎选择精度。** Float32 可减少内存占用并可能提升吞吐量，但在精度有要求时保留 float64，并在目标硬件上做基准测试。
5. **在有代表性的切片上验证语义。** 对于 null 处理、连接、时间序列、重塑或分组逻辑，保留一条小的 pandas 参考路径，在宣称一致性之前比较形状、标签、null 计数、排序和代表性值。
6. **数据超过 GPU 内存时**，迁移到 dask-cuDF 并设置 `enable_cudf_spill=True`。参见 `references/dask-cudf-patterns.md`。

## 通往 GPU DataFrame 的三条路径

### 路径 1：cudf.pandas 加速器（兼容 / 最小改动）

当用户需要小幅度代码改动、第三方 pandas 兼容性，或希望一条代码路径在遇到不受支持的操作时仍能回退继续运行时，使用此路径。

**Jupyter/IPython：**
```python
%load_ext cudf.pandas
import pandas as pd   # now GPU-backed; falls back silently for unsupported ops
```

**脚本：**
```bash
python -m cudf.pandas my_script.py
```

**配合多进程：**
```python
import cudf.pandas
cudf.pandas.install()   # must come BEFORE pandas import, before Pool creation
from multiprocessing import Pool
```

在宣称加速之前，先用 cudf.pandas profiler 确认。
有关 notebook、CLI 与统计示例，请阅读
`references/cudf-pandas-accelerator.md`。如果 profile 显示热点路径
运行在 CPU 上，请改用路径 2 以获得显式的 cuDF 控制。

### 路径 2：显式 cuDF API

适用于需要完全控制、热点路径优化、具名 DataFrame 迁移以及
对一致性敏感的操作：

```python
import cudf

# Read data directly to GPU
df = cudf.read_parquet("data.parquet")

# Operations mirror pandas
result = df.groupby("key")["value"].sum()
merged = df.merge(lookup, on="id", how="left")
filtered = df[df["amount"] > 1000]

# String operations
df["clean"] = df["name"].str.strip().str.lower()

# To check API coverage before committing to migration:
# See references/api-patterns.md for known gaps and workarounds
```

**让数据端到端留在 GPU 上。** 只在最后为显示或交接给 CPU 或非 GPU 环境时才调用 `.to_pandas()`。

涉及 `read_csv`/`read_parquet`、连接、
分组聚合、重塑、可空类型、`fillna`/`where`、时间分桶、滚动
窗口或 CPU/GPU 一致性检查的任务，优先使用显式 cuDF。当语义重要时，
增加一条小的 CPU/GPU 验证路径，而不是仅凭执行成功就下结论。

对于涉及 null 处理、重塑或时间序列行为的 pandas 代码，在重写之前
先阅读 `references/api-patterns.md` 中的相关语义清单。对于最小改动的请求，
一个 `cudf.pandas` 引导就足够了；而一个实现请求应当让热点路径
显式且可观测。

对于重塑密集的 pandas 代码（`pivot_table`、`melt`、`stack`/`unstack`、
`crosstab`），把源 schema 视为契约的一部分：索引标签、
列标签或层级、`fill_value`、`aggfunc`、margins 与 normalization。
在等价操作受支持的地方使用显式 cuDF；当精确的 pandas 重塑语义
比重写每个操作更重要时，使用 `cudf.pandas` 或一个
窄的兼容边界。在定稿之前，增加一条小的 pandas 参考一致性检查，
覆盖形状、标签和代表性值。参见
`references/api-patterns.md`。

### 路径 3：dask-cuDF（多 GPU / 大数据）

当数据集超出 GPU 内存时使用。完整模式参见 `references/dask-cudf-patterns.md`。

```python
from dask_cuda import LocalCUDACluster
from dask.distributed import Client
import dask
import dask.dataframe as dd

dask.config.set({"dataframe.backend": "cudf"})

cluster = LocalCUDACluster(enable_cudf_spill=True)  # one worker per GPU
client = Client(cluster)

ddf = dd.read_parquet("s3://bucket/data/*.parquet")
result = ddf.groupby("key").agg({"value": "sum"}).compute()
```

## 内存管理

**在 OOM 发生之前启用 spill**（而非事后）：
```python
import cudf
cudf.set_option("spill", True)   # spill to host RAM when GPU is full
```

**RMM async 分配器**（可在分配频繁的流水线中降低分配开销）。请在任何 cuDF 分配发生之前配置，并在其分配仍在使用期间保持该资源存活：
```python
import rmm
memory_resource = rmm.mr.CudaAsyncMemoryResource()
rmm.mr.set_current_device_resource(memory_resource)
```

| GPU 剩余空间 vs 数据集 | 策略 |
|---|---|
| 空闲 > 2× 数据集 | 单 GPU cuDF |
| 空闲 1–2× 数据集 | cuDF + `cudf.set_option("spill", True)` |
| 数据集 > GPU 内存 | dask-cuDF |
| 数据集 > 节点内存 | dask-cuDF + 多节点（参见 accelerated-computing-mpf） |

## 故障排查

**相比 pandas 没有加速：**
- 工作集太小？先测量传输与启动开销，再用有代表性的数据规模做基准测试。
- 运行 `%%cudf.pandas.profile` — CPU 占比高说明存在大量回退。找出并修复这些操作。
- 查阅 `references/api-patterns.md` 了解已知的 API 缺口。

**OOM（CUDA out of memory）：**
1. 启用 spill：`cudf.set_option("spill", True)`
2. 如果观察到分配器碎片化或重复分配的开销，请在 GPU 分配之前参考 `accelerated-computing-rmm` 的内存资源配置指引
3. 仍然失败：迁移到 dask-cuDF

**AttributeError / NotImplementedError：**
- 在 `references/api-patterns.md` 中查找该具体操作
- 把这一个操作放在窄边界上留给 CPU 处理，其余受支持的流水线继续在 GPU 上运行
- 仅对不受支持的操作使用 `.to_pandas()`，之后再用 `.from_pandas()` 转回

**与 pandas 结果不一致：**
- Null/NaN 处理不同：cuDF 默认使用 `<NA>`（可空），pandas 使用 `NaN`。参见 `references/api-patterns.md`。
- 排序稳定性：Python 的 `sort_values` 没有 `stable=True` 参数，而 `kind="stable"` / `kind="mergesort"` 目前会告警并回退到 quicksort。当相等键的排序次序重要时，增加一个按原始行位置的决胜键；参见 `references/api-patterns.md`。
- 浮点归约在 CPU 与 GPU 之间可能不同，因为算术运算不满足结合律。保留所需精度，使用显式容差进行比较，并排查超出容差的差异。

## 可空类型与填充语义

当用户明确关注 pandas 可空 dtype、`fillna`、
`where`/`mask` 或分组 null 行为时，把一致性检查视为实现的
一部分。可空 dtype 示例参见 `references/api-patterns.md`。

- 保留可空的整数/字符串列，而不是用哨兵值填充它们，
  除非源代码本来就是这么做的。
- 当 `where`/`mask` 编码的是条件时，保留其语义。仅当条件
  恰好只针对 null 时才使用宽泛的 `fillna`。
- 当 pandas 参考使用可空扩展 dtype 时，使用
  `to_pandas(nullable=True)` 进行比较。
- 把一致性检查放在 GPU 路径旁边的一个可复用辅助函数中，这样未来的
  改动会执行同样的可空转换与聚合检查。
- 在宣称语义一致之前，验证行数、null 计数、mask 真值表、分组聚合
  以及代表性 dtype。

## 参考文件

- `references/cudf-pandas-accelerator.md` — 性能剖析、回退检测、cudf.pandas 深入解析
- `references/api-patterns.md` — 已知 API 缺口、变通方案、语义差异
- `references/dask-cudf-patterns.md` — 多 GPU 模式、最佳实践、分区调优

## 外部文档

按需使用 WebFetch 获取详细的 API 签名、参数说明与示例。

- **cuDF 文档：** https://docs.nvidia.com/cudf/
- **dask-cuDF API 参考：** https://docs.nvidia.com/dask-cudf/
- **GitHub：** https://github.com/NVIDIA/cudf
- **CHANGELOG：** https://github.com/NVIDIA/cudf/blob/main/CHANGELOG.md
