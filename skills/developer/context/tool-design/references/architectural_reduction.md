> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/tool-design/references/architectural_reduction.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 架构精简：生产环境证据

本文档为 Agent 工具设计的"架构精简"方法提供详细证据与实现模式。

## 案例研究：Text-to-SQL Agent

一个生产环境的 text-to-SQL Agent 按架构精简原则完成了重建。原架构使用大量特化工具，配合重度提示词工程和精细的上下文管理。精简后的架构只使用一个 bash 命令执行工具。

### 原架构（大量特化工具）

原系统包含：
- GetEntityJoins：查找实体之间的关系
- LoadCatalog：加载数据目录信息
- RecallContext：召回先前的上下文
- LoadEntityDetails：获取实体规格
- SearchCatalog：搜索数据目录
- ClarifyIntent：澄清用户意图
- SearchSchema：搜索数据库模式
- GenerateAnalysisPlan：生成查询计划
- FinalizeQueryPlan：完成查询计划
- FinalizeNoData：处理无数据的情况
- JoinPathFinder：查找连接（join）路径
- SyntaxValidator：校验 SQL 语法
- FinalizeBuild：完成查询构建
- ExecuteSQL：执行 SQL 查询
- FormatResults：格式化查询结果
- VisualizeData：创建可视化
- ExplainResults：解释查询结果

每个工具都在解决团队预判模型会遇到的一个具体问题。背后的假设是：模型会在复杂模式（schema）中迷路、写出错误的连接、或幻觉出不存在的表名。

### 精简架构（两个原语工具）

精简后的系统包含：
- ExecuteCommand：在沙箱中运行任意 bash 命令
- ExecuteSQL：对数据库执行 SQL 查询

Agent 使用标准 Unix 工具探索语义层：

```python
from vercel_sandbox import Sandbox

sandbox = Sandbox.create()
await sandbox.write_files(semantic_layer_files)

def execute_command(command: str):
    """Execute arbitrary bash command in sandbox."""
    result = sandbox.exec(command)
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "exit_code": result.exit_code
    }
```

现在 Agent 用 `grep`、`cat`、`find` 和 `ls` 浏览包含维度定义、度量计算和连接关系的 YAML、Markdown 与 JSON 文件。

### 对比结果

| 指标 | 原架构（17 个工具） | 精简架构（2 个工具） | 变化 |
|--------|---------------------|-------------------|--------|
| 平均执行时间 | 274.8s | 77.4s | 快 3.5 倍 |
| 成功率 | 80% (4/5) | 100% (5/5) | +20% |
| 平均 token 用量 | ~102k tokens | ~61k tokens | 减少 37% |
| 平均步数 | ~12 步 | ~7 步 | 减少 42% |

原架构的最差案例：724 秒、100 步、145,463 个 token，并以失败告终。精简架构用 141 秒、19 步、67,483 个 token 成功完成了同一查询。

## 为什么精简有效

### 文件系统是强大的抽象

文件系统经过 50 多年的打磨。`grep` 这类标准 Unix 工具文档齐全、行为可预测，模型也理解它们。为 Unix 已经解决的问题再造自定义工具，只会增加复杂度而不产生价值。

### 工具曾束缚推理

那些特化工具在解决模型自己就能处理的问题：
- 预先过滤模型本可以自行浏览的上下文
- 限制模型本可以自行评估的选项
- 把交互包进模型并不需要的校验逻辑里

每条护栏都成了维护负担。每次模型升级都要重新校准这些约束。团队花在维护脚手架上的时间比改进 Agent 的时间还多。

### 好文档取代工具复杂度

语义层本来就有完善的文档：
- 维度定义存放在结构化 YAML 中
- 度量计算命名清晰
- 连接关系放在可浏览的文件里

自定义工具只是在转述本来就清晰可读的内容。模型需要的是直接读文档的权限，而不是盖在文档之上的抽象层。

## 实现模式

### 文件系统 Agent

```python
from ai import ToolLoopAgent, tool
from sandbox import Sandbox

# Create sandboxed environment with your data layer
sandbox = Sandbox.create()
await sandbox.write_files(data_layer_files)

# Single primitive tool
def create_execute_tool(sandbox):
    return tool(
        name="execute_command",
        description="""
        Execute a bash command in the sandbox environment.
        
        Use standard Unix tools to explore and understand the data layer:
        - ls: List directory contents
        - cat: Read file contents
        - grep: Search for patterns
        - find: Locate files
        
        The sandbox contains the semantic layer documentation:
        - /data/entities/*.yaml: Entity definitions
        - /data/measures/*.yaml: Measure calculations  
        - /data/joins/*.yaml: Join relationships
        - /docs/*.md: Additional documentation
        """,
        execute=lambda command: sandbox.exec(command)
    )

# Minimal agent
agent = ToolLoopAgent(
    model="claude-opus-4.5",
    tools={
        "execute_command": create_execute_tool(sandbox),
        "execute_sql": sql_tool,
    }
)
```

### 成功的前提条件

该模式在以下条件下有效：

1. **文档质量高**：文件结构良好、命名一致、定义清晰。

2. **模型能力足够**：模型无需手把手引导也能推理复杂问题。

3. **安全约束允许**：沙箱限制了 Agent 能访问和修改的范围。

4. **领域可导航**：问题空间可以通过查看文件来探索。

### 何时不适用

精简在以下情况下会失败：

1. **数据层混乱**：遗留命名约定、未文档化的连接关系、结构不一致。模型只会更快地产出错误的查询。

2. **需要专业知识**：领域专长无法写进文件。

3. **安全要求限制**：出于安全或合规必须约束某些操作。

4. **工作流确实复杂**：多步骤流程能从结构化编排中获益。

## 设计原则

### 以减法实现增益

最好的 Agent 可能恰恰是工具最少的那个。每个工具都是替模型做的一个选择。有时给模型原语能力而不是受约束的工作流，它会做出更好的选择。

### 信任模型的推理

现代模型能处理复杂问题。因为不信任模型的推理而去约束它，往往适得其反。先测试模型实际能做到什么，再决定是否建护栏。

### 投资于上下文，而非工具

地基比精巧的工具更重要：
- 清晰的文件命名约定
- 结构良好的文档
- 一致的数据组织
- 清晰可读的关系定义

### 为未来的模型而构建

模型的进步快于工具的跟进。为今天模型的局限而优化的架构，对明天模型的能力可能是过度约束。构建极简架构，让它从模型进步中受益。

## 评估框架

考虑架构精简时，评估以下几点：

1. **维护开销**：维护工具与改进结果，各花多少时间？

2. **失败分析**：失败源于模型局限还是工具约束？

3. **文档质量**：如果给模型直接访问权限，它能自行浏览你的数据层吗？

4. **约束必要性**：护栏防的是真实风险还是假设性担忧？

5. **模型能力**：工具设计之后，模型是否已经进步？

## 结论

架构精简并非普适，但它挑战了一个常见假设：更复杂的工具会带来更好的结果。有时恰恰相反。从最简单的架构起步，只在证明必要时才增加复杂度，并持续追问：工具是在赋能模型，还是在束缚模型。

## 参考资料

- Vercel Engineering: "We removed 80% of our agent's tools"（2025 年 12 月）
- AI SDK ToolLoopAgent 文档
- Vercel Sandbox 文档
