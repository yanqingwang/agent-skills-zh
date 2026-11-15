> **中文汉化版** · 上游：[NVIDIA/skills](https://github.com/NVIDIA/skills) · 原文件：`skills/accelerated-computing-cudf/references/cudf-pandas-accelerator.md` · License: CC-BY-4.0 AND Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# cudf.pandas 加速器：深入解析

## 工作原理

`cudf.pandas` 用一个代理替换 pandas 模块：支持的运算被路由到 cuDF，不支持的运算则静默回退到 CPU 上的标准 pandas。回退是透明的：代码仍能正确运行，只是不支持的算子跑在 CPU 上。

## 激活方式

| 方式 | 使用场景 |
|---|---|
| `%load_ext cudf.pandas` | Jupyter/IPython notebook |
| `python -m cudf.pandas script.py` | CLI 脚本执行 |
| `import cudf.pandas; cudf.pandas.install()` | 编程式调用、multiprocessing |

**关键**：激活必须在任何 pandas import 之前完成，直接和间接 import 都算。如果你在用 IPython 而 kernel 里已经 import 过 pandas，请重启并先执行激活。脚本里直接使用 `cudf.pandas.install()` 无法撤销，必须重启脚本。

## GPU 与 CPU 算子的性能分析

### 单元级性能分析（Jupyter）

```python
%load_ext cudf.pandas
import pandas as pd
```

在单独一个 cell 的开头运行 profiler magic：

```python
%%cudf.pandas.profile
df = pd.read_csv("data.csv")
result = df.groupby("category")["amount"].sum()
df.merge(lookup, on="id")
```

输出会显示每个运算的执行路径（GPU 还是 CPU）与耗时。

### 行级性能分析

```python
%%cudf.pandas.line_profile
df = pd.DataFrame({"a": range(1000000), "b": range(1000000)})
result = df.groupby("a")["b"].sum()    # shows GPU time
df.apply(lambda x: x + 1, axis=1)
```

### CLI 性能分析

```bash
python -m cudf.pandas --profile my_script.py
```

### 检测静默回退

性能分析工具也是检测静默回退的便捷手段。如果 profile 显示任务意外跑在 CPU 上，你可能撞上了不支持的 GPU 方法（相关局限在 api-patterns.md 参考文件中有深入讨论）。可以试着用不带 cudf.pandas 的原生 cudf 代码复现来验证。

## 验证确实用上了 GPU

```python
# Method 1: Run nvidia-smi during execution
# nvidia-smi dmon -s u -d 1

# Activate before importing pandas so the profiler can observe GPU dispatch.
import cudf.pandas
cudf.pandas.install()
from cudf.pandas import Profiler
import pandas as pd

with Profiler() as profiler:
    df = pd.read_csv("data.csv")
    result = df.groupby("category")["amount"].sum()
profiler.print_per_function_stats()
```

仅凭采样的 GPU 利用率偏低不能证明发生了回退：短暂的 GPU 运算可能没被采到。请用 `%%cudf.pandas.profile` 或 `Profiler` 来诊断。

## multiprocessing 支持

```python
# Top-level activation also runs when spawned workers import this module.
import cudf.pandas
cudf.pandas.install()           # must be FIRST, before everything else

from multiprocessing import Pool
import pandas as pd

def process_chunk(args):
    df = pd.read_csv(args)
    return df.groupby("key")["value"].sum()

if __name__ == "__main__":
    with Pool(4) as pool:
        results = pool.map(process_chunk, file_list)
```

## 局限

- **使用 NumPy C API**：许多项目带有自定义扩展模块，通过 NumPy C API 与 pandas dataframe 交互、操作单个 pandas 列。这类代码在 cudf.pandas 下永远无法工作。
- **子类化的 DataFrame**：继承 `pd.DataFrame` 的代码可能无法与 cudf.pandas 代理配合工作
- **pandas 私有 API**（`pd._libs.*` 等）：不支持
- **与外部代码进行原地操作**：如果第三方代码持有对 pandas 内部对象的引用，代理可能无法正确拦截
- **cudf.pandas 不会加速 Python 层循环**：先向量化，再加速

## 何时迁移到显式 cuDF

出现以下情况时，从 cudf.pandas 迁移到显式 cuDF：
1. Profile 显示热路径上 CPU 回退率超过 30%
2. 你需要 cuDF 专属特性（例如 `cudf.set_option("spill", True)`）
3. 你需要对 dtype 转换做显式控制（float32 优化）
4. 你在构建 cuDF 优先的库，而不是加速现有 pandas 代码
