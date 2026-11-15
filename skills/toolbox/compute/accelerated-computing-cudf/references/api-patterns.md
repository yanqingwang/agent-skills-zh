> **中文汉化版** · 上游：[NVIDIA/skills](https://github.com/NVIDIA/skills) · 原文件：`skills/accelerated-computing-cudf/references/api-patterns.md` · License: CC-BY-4.0 AND Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# cuDF API 模式、缺口与语义差异

## 与 pandas 的关键语义差异

### Null/NaN 处理

cuDF 比 pandas 更常保留可空 dtype，对可空数值列使用 Arrow 风格的 null，而不是提升成 float 的 `NaN`：

```python
import cudf
import pandas as pd

s = cudf.Series([1, None, 3])
print(s.dtype)   # int64; nulls use a separate validity mask

# Check for null
s.isnull()       # works as expected
s.isna()         # equivalent

# Fill nulls
s.fillna(0)      # works
```

差异：`pd.Series([1, None, 3])` 得到带 `NaN` 的 `float64`；cuDF 得到带有效性掩码和 `<NA>` 的 `int64`；`to_pandas(nullable=True)` 产出 pandas 的 `Int64`。

在当前版本中，字符串列的缺失值显示为 `None` 而不是 `<NA>`。不要编写依赖显示 repr 的测试；请用 `.isna()`、`.notna()` 或带类型的返回值做比较。

把 cuDF 输出与 pandas 可空参考实现比较时，用 `nullable=True` 转换：

```python
actual_pdf = gdf.to_pandas(nullable=True)
```

这样在存在可空 dtype 时会保留 pandas 的可空 dtype，而不是在比较边界处把 null 转成 `np.nan` 或 `None`。

对于以 null 为主的工作流，保留 pandas 行为作为简明参考，并让 GPU 路径保持显式：

- 标量、字典、前向和后向填充可直接映射到 cuDF
- 分组填充通常是先 `groupby().transform(...)`，再 `fillna(...)`
- 条件填充用布尔掩码加赋值，或用分组聚合再合并回原 frame
- 线性插值是语义边界；先核对已安装版本的 API 行为再使用 cuDF，或把这一小步留在 `cudf.pandas` 下并做一致性校验

验证行数、按列的 null 计数、有代表性的填充值、分组聚合，以及排序/插值敏感代码产出的任何行。

### 排序稳定性

Python `sort_values` 不接受 `stable=True`。传入 `kind="stable"` 或 `kind="mergesort"` 目前会发出警告并回退到快速排序。当 pandas 参考实现需要稳定排序时，用原始行位置作为最终排序键（选一个 schema 中不存在的临时列名）：

```python
import cupy as cp

# A unique final key preserves original order among equal primary keys.
ordered = df.assign(_row_position=cp.arange(len(df)))
ordered = ordered.sort_values(["col", "_row_position"]).drop(columns="_row_position")
```

匹配参考实现的排序方向与 null 位置，然后对照 pandas 验证相同键的行。

### 字符串操作 — GPU regex

cuDF 使用 libcudf 的 GPU regex 引擎，不是 Python 的 `re` 也不是 RE2。移植某个模式前，先查看[支持的 regex 特性](https://github.com/NVIDIA/cudf/blob/main/cpp/doxygen/regex.md)。搜索模式中的反向引用不受支持，但替换字符串支持对捕获组的反向引用：

```python
# These constructs are unsupported by libcudf regex:
# - Lookahead/lookbehind: (?=...), (?!...)
# - Backreferences within the search pattern: \1
# - Possessive quantifiers: ?+, *+

# Supported GPU patterns:
df["col"].str.contains(r"\d+")
df["col"].str.replace(r"[aeiou]", "", regex=True)

# Rewrite unsupported patterns or use a narrow CPU boundary:
df["col"].str.contains(r"(?=.*foo)")   # lookahead — use different approach
```

### CuPy 数组输出

在 cuDF Series/DataFrame 上访问 `.values`，得到的是 CuPy 数组（不是 NumPy）：

```python
import cudf
import cupy as cp

df = cudf.DataFrame({"a": [1, 2, 3]})
arr = df["a"].values     # CuPy array, not NumPy!
type(arr)                # <class 'cupy.ndarray'>

# To get NumPy explicitly:
np_arr = df["a"].to_numpy()
np_arr = cp.asnumpy(arr)
```

## 常见 API 缺口与变通方案

pandas 的 API 面非常大，cuDF 只覆盖其中有限的一个子集。本节列出一些常见缺口，但不应把它当作 cuDF 与 pandas API 之间差异的穷尽清单。

### cuDF 尚未支持的运算

| pandas 运算 | 状态 | 变通方案 |
|---|---|---|
| `df.apply(func, axis=0)` | 按列 apply：支持有限 | 改写为向量化的 cuDF 运算 |
| `df.apply(func, axis=1)` | 按行 apply：支持有限 | 简单函数可用 `df.apply()`；否则回退 `cudf.pandas` |
| 部分 `pd.Grouper` 选项 | 部分支持 | 改用 resample 或直接 groupby |
| `pd.read_html()` | 不支持 | 先用 pandas，再 `cudf.from_pandas()` |
| `pd.ExcelWriter` / `read_excel` | 不支持 | 先转换成 CSV/Parquet |
| `df.to_sql()` | 不支持 | 先转成 pandas，再用 pandas |
| 多级列（MultiIndex） | 部分支持 | 先展平列名 |

### Reshape 与 Crosstab 的一致性

`cudf.pivot_table`、`cudf.melt`、`cudf.crosstab`、`DataFrame.unstack` 和 `DataFrame.stack` 能覆盖很多 reshape 工作流。当流水线依赖 reshape 输出时，把源 pandas schema 当作可观测行为对待：

- 改写前，先从 pandas 路径捕获预期的索引标签、列标签或层级、名称、形状与代表值。
- 下游代码要消费 pandas MultiIndex 列时，保留它们。如果扁平 schema 才是 cuDF 的实际表示，就返回有文档说明的映射（如 `revenue_sum_2024`），并按该 schema 验证消费方。
- 对多聚合的 `pivot_table` 输出，把聚合名保留在 schema 里。必要时用显式的分组聚合构建 cuDF 结果，然后要么重建 pandas 的列层级，要么用确定性名称（如 `{value}_{agg}_{column}`）展平。
- 用显式 GPU 运算补齐缺失的 `crosstab` 便利功能：计数用 `cudf.crosstab`，边际用行/列求和，行归一化值用每行除以该行合计。
- 当目标是精确的 pandas reshape 语义、而显式 cuDF 需要大改 schema 时，把 `cudf.pandas` 当作兼容优先的路径。
- 加一个可复用的验证助手，在小型 fixture 上对照 pandas 参考，比较形状、索引/列标签、聚合名、null 位置与数值。

### 时间序列与滚动窗口的一致性

cuDF 支持 datetime 列、排序、分组运算、位移、累计运算以及许多滚动窗口模式。改写时保持 pandas 可见的时间语义：

- 把时区、timestamp dtype、频率与分桶标签保留为输出契约的一部分
- 在做分组 `shift`、`rolling`、累计或 expanding 类计算之前，先按分组键和 timestamp 排序
- 对照 pandas 参考验证稀疏或缺失的分桶；当下游消费方预期出现空档期时，显式物化所需的分桶网格
- 最终的 `.to_pandas()` 只用于展示、绘图或参考比较

### cuDF 支持的 I/O 格式

```python
# Fully supported (fast GPU I/O)
cudf.read_csv(), cudf.read_parquet(), cudf.read_json()
cudf.read_orc(), cudf.read_feather(), cudf.read_avro()

# Not supported (use pandas, convert with cudf.from_pandas())
# Excel, HTML, SQL, HDF5, SAS, Stata, pickle
```

## 实用的 cuDF 专属 API

```python
# Convert between pandas and cuDF
cudf_df = cudf.from_pandas(pd_df)
pd_df = cudf_df.to_pandas()

# Interop with CuPy
import cupy as cp
arr = cp.asarray(df["col"])          # zero-copy view
df["new_col"] = cudf.Series(arr)     # back to cuDF
```

## 性能建议

1. **精度允许时用 float32**：减少内存占用、保住所需精度，并在目标 GPU 上实测吞吐
2. **用 `cudf.read_parquet()` 而不是 CSV**：Parquet 是列式格式，读取速度大幅领先
3. **避免在 `.apply()` 中使用 Python lambda**：改用内置 cuDF 运算
4. **dask-cuDF 下用 `persist()`**：把已算好的数据留在 GPU worker 上，避免重复计算
5. **避免在流水线中途 `.to_pandas()`**：每次往返都是一次 PCIe 传输
