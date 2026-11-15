> **中文汉化版** · 上游：[NVIDIA/skills](https://github.com/NVIDIA/skills) · 原文件：`skills/accelerated-computing-cudf/references/dask-cudf-patterns.md` · License: CC-BY-4.0 AND Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# dask-cuDF 模式

## 首选 API：dask.dataframe 后端

新代码优先使用 `dask.dataframe` 后端配置。当前的 dask-cuDF 使用 Dask 表达式查询规划来实现谓词与投影下推。直接调用 `dask_cudf.read_*` 也会委托给该后端。

```python
import dask
dask.config.set({"dataframe.backend": "cudf"})

import dask.dataframe as dd

# Read — now GPU-backed with query planning
ddf = dd.read_parquet("data/*.parquet")
ddf = dd.read_csv("data/*.csv")

# Check operation support against the cuDF backend before migration.
result = ddf.groupby("key")["value"].sum()
```

**显式调用 `dask_cudf` 读取同样会走查询规划：**
```python
import dask_cudf
ddf = dask_cudf.read_parquet("data/*.parquet")
```

## 集群配置

本地 GPU worker 使用 `LocalCUDACluster`，并用 `enable_cudf_spill=True` 启用 worker 侧的 cuDF 溢写。多节点部署需要自行配置调度器与 GPU worker：

```python
from dask_cuda import LocalCUDACluster
from dask.distributed import Client
import dask
dask.config.set({"dataframe.backend": "cudf"})

# Standard setup — one worker per GPU
cluster = LocalCUDACluster(
    enable_cudf_spill=True,    # cuDF-native spill; preferred over device_memory_limit
    rmm_pool_size=0.8,         # leave headroom for non-RMM allocations
)
client = Client(cluster)

# Use GPU-aware transport for communication-heavy workloads.
cluster = LocalCUDACluster(
    enable_cudf_spill=True,
    rmm_pool_size=0.8,
    protocol="ucx",
)
```

## 分区大小

分区大小是影响最大的调优参数：

| 工作负载 | 目标分区大小 |
|---|---|
| 通用 ETL | 单张 GPU 显存的 1/32 – 1/8 |
| Shuffle 密集（groupby、join、sort） | GPU 显存的 1/32 – 1/16 |

```python
# Check current partitions
print(f"Partitions: {ddf.npartitions}")

# Tune at read time (most efficient)
ddf = dd.read_parquet("data/", blocksize="256MB")  # adjust to hit target partition size

# Repartition after load if needed
ddf = ddf.repartition(npartitions=64)
```

## 读取数据

### 本地 Parquet（推荐）

```python
import dask.dataframe as dd

# Project only needed columns — pushed down to storage
ddf = dd.read_parquet("data/*.parquet", columns=["col1", "col2", "key"])

# aggregate_files=True merges small files into larger partitions
ddf = dd.read_parquet("data/", aggregate_files=True, blocksize="512MB")
```

### 远端存储（S3、GCS）

```python
# Use blocksize=None to avoid slow metadata collection on remote stores
ddf = dd.read_parquet(
    "s3://bucket/prefix/",
    blocksize=None,
    filesystem="arrow",    # pyarrow filesystem for S3/GCS
    columns=["col1", "col2"],
)
```

## 聚合模式

### 低基数 groupby

```python
# split_out=1 avoids unnecessary shuffle for few output groups
result = ddf.groupby("status_code")["amount"].sum(split_out=1)
```

### 高基数 groupby（默认）

```python
result = ddf.groupby("customer_id").agg({"amount": "sum", "count": "count"})
```

## Join / Merge 模式

```python
# Standard join (both datasets distributed)
merged = large_ddf.merge(other_large_ddf, on="id", how="left")

# Small table join: broadcast=True avoids shuffling the large table
merged = large_ddf.merge(
    small_lookup_df,    # cuDF DataFrame or small dask-cuDF
    on="id",
    how="left",
    broadcast=True,     # sends small_lookup to all workers; no shuffle
)
```

## Sort 与 Shuffle

```python
# Global ordering requires an expensive shuffle; use it only when needed.
sorted_ddf = ddf.sort_values("timestamp")   # use sparingly

# If you need rows grouped by key (not sorted), use shuffle instead:
shuffled = ddf.shuffle(on="customer_id")
```

## 构建分布式集合

```python
# Preferred: from_map enables column projection pushdown
from dask.dataframe import from_map
import cudf

def load_partition(path, columns=None):
    return cudf.read_parquet(path, columns=columns)

files = ["data/part_0000.parquet", "data/part_0001.parquet"]
ddf = from_map(
    load_partition,
    files,
    meta=cudf.read_parquet(files[0], nrows=0),   # avoids eager first-partition read
)

# from_delayed works but loses projection pushdown
from dask import delayed
from dask.dataframe import from_delayed
parts = [delayed(cudf.read_parquet)(f) for f in files]
ddf = from_delayed(parts)
```

## 执行与物化成本

要区分立即执行的调用与惰性操作，后者在被真正计算时需要代价高昂的 shuffle：

| 调用 | 为何昂贵 |
|---|---|
| 对大型集合调用 `.compute()` | 把全部数据拉到一张 GPU 上 |
| `.persist()` | 用分布式客户端异步启动计算；把分区保留在 worker 上 |
| `len(ddf)` | 全量扫描 |
| `ddf.head()` / `ddf.tail()` | 物化第一个/最后一个分区 |
| `ddf.sort_values(...)` | 惰性图，执行时带一次完整 shuffle |
| `ddf.set_index(col)` | 可能急切地计算 divisions；执行时做 shuffle 和排序 |

**Persist 模式**（对同一份数据反复查询时）：
```python
from dask.distributed import wait

ddf = client.persist(ddf)
wait(ddf)   # Wait before timing reuse; partitions may spill under memory pressure.
result1 = ddf[ddf["a"] > 0].compute()
result2 = ddf[ddf["b"] > 0].compute()  # fast — data already in memory
```

调用 `.compute()` 会把结果收集到一张 GPU 上。大型输出应保持分区并用 `to_parquet()` 写出，而不是靠溢写让结果硬塞进单卡显存。

## 写出结果

```python
# Parquet (recommended — partitioned output)
ddf.to_parquet("output/", write_index=False)

# To single cuDF DataFrame — only when result fits in GPU memory
result_cudf = ddf.compute()

# To pandas — only at the very end for CPU or non-GPU handoff
result_pd = result_cudf.to_pandas()
```

## OOM 诊断

```python
# Step 1: Check worker memory pressure from dashboard
print(client.dashboard_link)   # open in browser → Workers tab

# Step 2: Increase partition count to reduce per-partition memory
ddf = ddf.repartition(npartitions=ddf.npartitions * 2)

# Step 3: If not already enabled, add cuDF-native spilling
# (restart cluster with enable_cudf_spill=True, rmm_pool_size=0.9)

# Step 4: Move filter/project before expensive operations
ddf = ddf[["needed_col1", "needed_col2", "key"]]  # project first
ddf = ddf[ddf["amount"] > 0]                      # filter early
result = ddf.groupby("key")["needed_col1"].sum().compute()
```

## 反模式

新的 dask-cuDF 代码请采用上文"首选 API"小节展示的后端配置。本节示例聚焦于选定后端之后的执行与物化错误。

```python
# AVOID: calling .compute() mid-pipeline
intermediate = ddf.groupby("a")["b"].sum().compute()
# The intermediate is a single cuDF Series; distributed execution has ended.
result = intermediate.mean()

# CORRECT: chain lazily, compute once
result = (
    ddf.groupby("a")["b"].sum()
       .mean()
       .compute()
)

# AVOID: collecting huge dataset to display
print(ddf.compute())   # OOM risk

# CORRECT: sample or head
print(ddf.head(10))    # shows first 10 rows only
```
