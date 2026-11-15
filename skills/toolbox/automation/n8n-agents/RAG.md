> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-agents/RAG.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# RAG（检索增强生成）

n8n 的 RAG 建在 LangChain 原语上：文档加载器、文本分割器、嵌入、向量存储、检索器、重排序器。它们接上 Agent 和 chain 的方式与模型、记忆相同（通过 `ai_*` 连接）。

本参考刻意**单薄**。部件都能用，但带立场的端到端配方（"选哪个向量存储、怎么分块、何时重排序"）高度依赖数据形态和规模。默认值请对照当前 n8n 文档和你们团队的选择去核实。

---

## 上向量之前：先排除更便宜的查找

不是每个检索问题都需要向量存储。先排除三种更便宜的替代：

- **数据库或 Data Table 做精确查找。** "查客户 X 的记录"、"取 issue #1234"、"取 status = 'open' 的行"不是 RAG 问题，直接查询就行。DB 节点 → **n8n-node-configuration**。
- **要新鲜就用实时搜索。** 你索引的东西里没有的信息（当前新闻、实时 API 状态、一切时效性内容）该用搜索工具（Tavily 等），不是 RAG。
- **文档少或结构化就用 grep/文件浏览工具。** 文档少到可以列出来（一个仓库、一个文档站、几百个 markdown 文件）时，给 Agent 列表/抓取/搜索工具，让它自己导航。举例：浏览 GitHub 仓库的 Agent 可以用 `githubTool`（列文件）加一个对着仓库 contents 端点的 HTTP Request Tool 拉原始文本——不用摄取、不用嵌入，引用里还带完整源路径。

文档多到列不完、查询是语义性的而非导航性的、且需要低延迟的相似度检索时，才上向量 RAG。

---

## 最快上手：内存向量存储

跑通 RAG 流程最快的路径用 `@n8n/n8n-nodes-langchain.vectorStoreInMemory`：无外部服务、无需开通、除已在用的嵌入/聊天模型提供商外不需要额外凭据。数据在工作流重启后丢失，所以适合原型、学习和测试，不适合生产。

- **摄取**：任何产出文档的触发器 → Default Data Loader → Vector Store In-Memory（`mode: 'insert'`），并接一个 Embeddings 节点到 `ai_embedding`。带文件上传字段的 Form Trigger 是不写脚本就灌入 PDF/CSV 的快捷方式。
- **查询**：Chat Trigger → Agent → Vector Store In-Memory（`mode: 'retrieve-as-tool'`），用同一个 `memoryKey` 和与摄取相同的嵌入模型。

数据要跨重启存活或要扩到单实例之外时，把内存节点换成持久存储，其余接线不变。

---

## 向量 RAG：部件

n8n 把 LangChain 原语暴露为子节点：

- **文档加载器**（`documentDefaultDataLoader`）：从来源拉取，可选带元数据。接进向量存储的 `ai_document`。
- **文本分割器**（`textSplitter*`）：切成可检索的小块。简单场景下默认加载器可内联完成。
- **嵌入**（`embeddingsOpenAi`、`embeddingsCohere` 等）：把块变成向量。**摄取和查询**两端都要接 `ai_embedding`。
- **向量存储**：`vectorStoreInMemory`、`vectorStoreQdrant`、`vectorStoreSupabase`（Postgres pgvector）、`vectorStorePinecone`。各有模式：`insert`（摄取）、`retrieve-as-tool`（Agent 的 `ai_tool` 槽位）及其他直查模式。

Default Data Loader 的 `metadata` 字段是**承重的**：任何想过滤或随结果一起展示的东西（来源 URL、文档类型、租户 ID）都放这里。没有它，结果只是没有出处的碎块。

---

## 向量 RAG：两条工作流

### 摄取

```
[Trigger]
  →  [Vector Store, mode: 'insert']
        ai_document   <- [Default Data Loader (with metadata)]
        ai_embedding  <- [Embeddings]
```

**摄取不必是工具。** 多数时候它是一个独立的定时工作流，按节奏（如每晚）预填充存储；或一个 webhook 触发的工作流。只有当文档随对话动态变化（Agent 学到了该记住的东西）时才把它接成 Agent 工具。静态或系统管理的集合，独立工作流更简单。

### 查询

```
[Chat / webhook trigger]
  →  [Agent]
        ai_tool          <- [Vector Store, mode: 'retrieve-as-tool']
                               ai_embedding <- [Embeddings (SAME model as ingest)]
        ai_languageModel <- [Chat Model]
        ai_memory        <- [Memory]
```

接成 `ai_tool` 后，向量存储成为一个工具，Agent 判断检索相关时就调用。只有**每一**轮都需要检索时，才把检索直接接进主流程（Agent 之前），实践中很少见。

**嵌入模型必须匹配。** 摄取时嵌入文档的模型，必须就是嵌入查询的那个。模型不匹配只会检索出垃圾。换模型 → 重新摄取。

---

## 待定决策（按上下文核实）

### 向量存储选型

- **内存**：零运维，重启即失。原型和测试。
- **Qdrant**：开源、可自托管、快，在 n8n 里成熟。
- **Postgres pgvector / Supabase**：已经在跑 Postgres 就理想；SQL 侧元数据过滤和关系联表组合顺畅。
- **Pinecone**：全托管，按请求计价。

### 嵌入模型

OpenAI `text-embedding-3-large`、Cohere `embed-v3` 和开源模型都常见。成本、维度数和质量各不相同，一开始就慎重选，免得重新嵌入。

### retrieve-as-tool 与 retrieve-before-agent

- **Retrieve-as-tool**：Agent 决定检索何时相关，**并且**自己措辞查询（改写、分解、扩展模糊表述）。每次检索多一跳，但浪费的检索更少、命中率更高。
- **Retrieve-before-agent**：更简单也更可预测，但每一轮都付成本，**而且**拿用户原始输入当查询，模糊表述（"那个东西怎么用来着？"）会原样进搜索。

多能力 Agent 里工具式组合更好（检索只是若干工具之一）。窄域问答机器人每个问题都是知识库问题，总是检索即可。

---

## 交叉引用

- Agent 基础 → 父级 **SKILL.md**
- 接子工作流（及 agentic 检索工具）→ **SUBWORKFLOW_AS_TOOL.md**
- 检索工具上的命名/描述 → **TOOLS.md**
- 小规模结构化数据用 Data Table 替代向量存储 → **n8n-node-configuration**
