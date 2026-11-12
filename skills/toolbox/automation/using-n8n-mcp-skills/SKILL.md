---
name: using-n8n-mcp-skills
description: "在通过 n8n-mcp MCP server 构建、编辑、验证、测试或调试 n8n 工作流时使用，包括设计流程、配置节点、编写表达式或 Code 节点、接入凭据，以及修复运行异常的工作流。它是 n8n-mcp-skills 技能包的入口 Skill：把你导向合适的专项 Skill，从第一轮对话起就给出每个 n8n-mcp 工具的实用知识，并列出让工作流不在生产环境崩掉的规则。任何涉及 n8n、工作流、节点或自动化的任务都先查阅它，哪怕只是一次性的小任务，哪怕用户没有点名任何 Skill，因为 n8n 的接口在不同版本间会漂移，而专项 Skill 能避免静默失败。"
---

> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/using-n8n-mcp-skills/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 使用 n8n-mcp Skills

这是一个**路由**，不是参考手册。它告诉你接下来要做的事由哪个 Skill 负责规则。真正的指导在 Skill 正文里，用 Skill 工具调用它们。拿不准时，宁可多加载几个 Skill，也别少加载。

社区维护的 **n8n-mcp** server 以及 n8n 本身，迭代速度都快过任何模型的训练截止点。工具名、参数、节点的 `typeVersion` 和默认行为都会在不同版本间漂移。一旦发现漂移，比如某个 Skill 提到的工具并不存在、参数结构与 `get_node` 返回的不一致、行为与 Skill 描述不符，就要以**实时工具**为准，告知用户，并建议更新技能包和实例。

## 不可妥协的规则

三条规则，没有例外。每一条都在防止某一类看起来正确、却会在生产环境崩掉的工作流。

1. **在执行任何 n8n 操作前先调用相应 Skill**，而非只在 MCP 调用前。写表达式、配置节点、设计工作流、连接节点或编写 Code 之前，都要先调用对应的 Skill。PreToolUse hook 会在影响最大的那些工具调用上提醒你，但它们**只存在于 Claude Code plugin 安装方式中**。在其他环境里，无论是 Claude.ai 上传 Skill，还是任何将此技能包作为 Agent Plugin 加载的客户端（Codex、Cursor、Copilot 等），都不会有东西提醒你，全靠自己。除非本次会话亲眼见过 hook 触发，否则一律当自己没有被 hook 兜底。
2. **激活前既要验证，也要核查。** 激活前先运行 `validate_workflow`（或按 id 用 `n8n_validate_workflow`），并在每次创建或更新后调用 `n8n_get_workflow`，检查 `connections` 对象。只做验证会漏掉被静默丢弃的连线、Merge 索引差一，以及从未接上的错误输出。验证通过只说明 JSON 格式良好，并不代表工作流正确。测试跑出绿灯也不算证据：`{{ }}` 里的 JS 错误会静默解析为 `null`（一个条件写坏的 Filter 会丢掉所有条目却仍显示成功），所以要检查输出值。参见 `n8n-expression-syntax`。
3. **机密绝不放进文本字段。** token、API key 和密码一律走 n8n 的凭据系统。如果没有原生节点，就用 HTTP Request 节点配合官方的 credential type。一个通过 `{{ $json.token }}` 引用 token 的 Set 节点，说到底还是泄露，只是多了几步。参见 `n8n-mcp-tools-expert`。

## 依靠 Skill，而非训练数据

n8n 一直在变。「凭记忆」写出的参数名常常悄悄就是错的：它们会当作普通字符串通过验证，运行时却什么也不做。如果某个 Skill 与你的记忆冲突，以 Skill 为准。如果 `get_node` 与某个 Skill 冲突，以工具为准，并标出这处漂移。

## 推荐默认做法

以下是默认做法；下面的 Code 例外是一个封闭清单。

**原生节点优先，Code 最后。** 按这个顺序挑：服务自带的节点（只有在没有节点覆盖该操作时才用 HTTP Request），其次是能干这活的原生节点，再其次是在该节点里写一段短表达式，最后才是 Code。放在 `{{ }}` 里的函数体或若干语句就算代码：它该待在 Code 节点里。

| 任务 | 使用 |
|---|---|
| 仅用于选择路由的标志；丢弃条目 | IF / Switch / Filter 中的条件 |
| 常量、错误或返回条目 | Edit Fields (Set) |
| 恢复先前的上下文 | `$('Node').item` |
| 在 Data Table get 之后挑选行 | 该 get 的 order by + limit |
| 分组并求和 | Summarize |
| 多个条目合成一个数组 / 数组拆成条目 | Aggregate / Split Out |
| 合并两个列表 | Merge（按字段合并） |
| 对两个列表求差或同步 | Compare Datasets |
| 去重，包括跨运行去重 | Remove Duplicates |
| Top-N | Sort + Limit |
| 日期 | Date & Time，或一行 Luxon 代码 |
| XML / HTML / Markdown / CSV / XLSX | XML, HTML, Markdown, Extract From File / Convert To File |
| 为 API 分页（无对应服务节点时） | HTTP Request 的 pagination 选项 |
| 对调用节流 | HTTP Request 的 batching 选项，或 Loop + Wait |
| Hash, HMAC, UUID | Crypto（+ Webhook raw body） |

只有在下列情形才该用 Code：没有节点能表达的循环或递归、跨运行的状态、没有节点能处理的解析、库调用、在 queue 模式 worker 上对所有条目做重活（成千上万条目，且已说明或实测过），或者用一个短 Code 节点（约 15 行）替掉 4+ 个只负责整理数据的胶水节点。每一个最终保留的 Code 或 HTTP Request 节点都要加上注释 `Why Code: <native node considered> — <reason>`（或 `Why HTTP:`）。参见 `n8n-node-configuration` 和 `n8n-code-javascript`。

- **只给下一个节点重新映射字段的 Set 就是反模式。** 把那些表达式直接放进下一个节点。把 Edit Fields 当作具名步骤是没问题的。参见 `n8n-expression-syntax`。
- **逐条目迭代是自动的。** 默认的逐条目执行已经能处理时，别再添一个 Loop Over Items 节点去「让它循环」。
- **按实时 schema 配置，绝不靠记忆。** 设置参数前先 `get_node`。参见 `n8n-node-configuration`。

## 危险信号：「正打算 ___」 → 调用 ___

一旦发现自己冒出下面任何一种念头，就停下来，先调用指定的 Skill。

| 念头 | 调用 |
|---|---|
| 「这个工作流很简单，直接搭就行」 | `n8n-workflow-patterns`，多数「简单」流程上线就有 10+ 个节点 |
| 「我加个 Set 节点来映射这些字段」 | `n8n-expression-syntax`，只给下一个节点重新映射的 Set 是反模式；具名步骤没问题 |
| 「直接用 Code 节点吧，更省事」 | 先看上面的任务表，再看 `n8n-code-javascript`，Code 只用于那个封闭清单，且要带上 `Why Code:` 注释 |
| 「用户提到数据了，我来写 Python」 | `n8n-code-javascript`，默认用 JS；只有明确要求时才用 Python（`n8n-code-python`） |
| 「我在写一段给 AI agent 调用的代码」 | `n8n-code-tool`，它的运行时约定与 Code 节点不同 |
| 「我用 HTTP Request 调这个 API」 | `n8n-mcp-tools-expert`，先用 `search_nodes` 找服务自带节点；保留下来的 HTTP 节点要带 `Why HTTP:` |
| 「我把一个 Merge 接 3 个来源」 | `n8n-node-configuration`，Merge 默认 2 个输入（`numberInputs`）；第 3 个会被静默丢弃 |
| 「验证通过了，可以激活了」 | `n8n-validation-expert` + `n8n-workflow-patterns`，跑一遍反模式扫描 |
| 「验证抛了个我看不懂的错」 | `n8n-validation-expert`，讲清每条错误和警告的含义，以及哪些必须修、哪些只是最佳实践建议 |
| 「我在这里引用 `$json.x`」 | `n8n-expression-syntax`，在分支多的工作流里优先用 `$('Node').item.json.x` |
| 「这个 webhook／定时流程只走正常路径就行」 | `n8n-error-handling`，给每个可能出错的节点接上错误分支；4xx 是调用方的错，5xx 是你的错 |
| 「我把这个文件／图片当 JSON 传过去」 | `n8n-binary-and-data`，文件内容在 `$binary` 里，无法跨越 agent-tool 边界 |
| 「我接一个 AI agent，再给模型配几个工具」 | `n8n-agents`，工具名和描述本身就是提示词；memory、结构化输出和拓扑都有坑 |
| 「我把这段逻辑拷到另一个工作流里」／「这越来越大了」 | `n8n-subworkflows`，抽成可复用的子工作流；动手前先搜一下 |
| 「我去建那个 credential／打开那个 workflow」（账号有 >1 个实例） | `n8n-multi-instance`，用 `instance: "<name>"` 指明目标；不带名字的调用会落到别的会话可以改动的默认实例上 |

## Skill 索引

| Skill | 何时用它 |
|---|---|
| `using-n8n-mcp-skills` | 这个路由（自动加载）。指出负责你任务的 Skill。 |
| `n8n-mcp-tools-expert` | 挑选或调用任何 n8n-mcp 工具；节点发现；credentials；data tables；安全审计；templates |
| `n8n-workflow-patterns` | 设计或搭建工作流；选择架构（webhook / HTTP API / database / AI agent / scheduled / batch） |
| `n8n-node-configuration` | 配置任何节点；随 operation 变化的必填字段；属性依赖；精准的字段改动 |
| `n8n-expression-syntax` | 编写 `{{ }}`、`$json`/`$node`/`$now`；在节点间映射数据；转换的把关者；Set 节点规范 |
| `n8n-validation-expert` | 解读验证错误/警告；误报；验证循环；auto-fix；审查已有工作流 |
| `n8n-code-javascript` | 任何用 JavaScript 写的 Code 节点；数据访问；`this.helpers`；DateTime；SplitInBatches 循环模式 |
| `n8n-code-python` | 明确要求用 Python 写的 Code 节点；原生 runtime（仅支持 `_items`/`_item`，默认禁止 imports，旧式 `_input` 代码会失败） |
| `n8n-code-tool` | 供 AI agent 调用的 Custom Code Tool（`toolCode`），返回字符串，没有 `$fromAI`/`$input` |
| `n8n-error-handling` | Webhook/API 或无人值守的工作流；接错误输出；重试；4xx/5xx 响应形态；静默失败 |
| `n8n-binary-and-data` | 文件、图片、PDF、附件、上传/下载、视觉；把文件传入或传出 agent tool |
| `n8n-subworkflows` | 可复用 / 多步构建；Execute Workflow；抽取共用逻辑；Define-Below inputs；all-vs-each；把工作流暴露成 agent tool |
| `n8n-agents` | AI Agent / LLM-with-tools / Text Classifier；工具设计与 `$fromAI`；系统提示词；结构化输出；memory；RAG；人工审核；chat bots |
| `n8n-multi-instance` | 拥有多个实例的账号（出现 `n8n_instances`）；每次调用的 `instance` 参数；并行 agent；`switch`；credential 写入；意外的 `NOT_FOUND`、错误/空的读取、`INSTANCE_*` 错误 |
| `n8n-self-hosting` | *部署，而非搭建工作流*，在 VM 上自托管 / 安装 / 部署 n8n（Docker Compose + Caddy，单实例 vs queue 模式），或者更新 / 备份 / 加固。它自行触发，不属于上面的构建流程。 |

## n8n-mcp 工具：从一开始就能上手的知识

限定名形如 `mcp__<server>__<tool>`（`<server>` 通常是 `n8n-mcp`）。

**两个层级，以及如何判断你手上是哪一种。** 下面的文档与验证工具离线可用，始终存在。`n8n_*` 管理类工具要连到实时的 n8n 实例，**只有在实例连接后才会出现**。如果它们没出现，不代表出了故障，也不需要重试：照实说明，并指给用户对应安装方式的解决办法：

- **托管版（`https://api.n8n-mcp.com/mcp`）**：首次使用时通过客户端的 OAuth 提示登录，再在控制台里连接 n8n 实例。配置里不放任何 env var 或 API key。
- **自托管（`npx n8n-mcp`、Docker）**：server 需要在环境里设置 `N8N_API_URL` 和 `N8N_API_KEY`，且要在客户端启动前导出。

`n8n_health_check` 确认连接可用，并返回解析出的实例。

**发现与文档**
- `tools_documentation`，每个工具的元文档；`{topic, depth:"full"}` 可配合 `ai_agents_guide` 或（n8n-mcp 2.97+）`expression_helpers`。
- `search_nodes`，按关键字查找节点。
- `get_node`，节点信息。接受单个 **SHORT-form** 的 `nodeType`（`nodes-base.httpRequest`、`nodes-langchain.agent`），外加 `detail`（minimal/standard/full）和 `mode`（info/docs/search_properties/versions）。
- `validate_node`，单独校验一个节点的配置（profiles：minimal/runtime/ai-friendly/strict）。
- `search_templates` / `get_template`，模板库（按关键字、节点、任务、元数据）。

**构建与编辑**
- `n8n_create_workflow`，根据完整的工作流 JSON 创建。
- `n8n_update_partial_workflow`，增量 diff 操作（`{id, operations:[…]}`）：addNode、updateNode、patchNodeField、addConnection、setNodeGroups、activateWorkflow 等。编辑时优先用它。
- **Canvas groups**（n8n 2.28+）在编辑后会保留；相关调整显示在 `details.warnings` 里。用 `setNodeGroups` 操作来创建或修改它们。参见 `n8n-mcp-tools-expert`。
- `n8n_update_full_workflow`，整体替换。
- `n8n_autofix_workflow`，自动修复常见问题。
- `n8n_deploy_template`，把模板部署到实例。

**验证**（必要但不充分，务必配合反模式扫描）
- `validate_workflow`，输入完整 JSON，输出 errors/warnings/fixes。这里的节点类型是 **LONG form**（`n8n-nodes-base.set`）。
- `n8n_validate_workflow`，按 `{id}` 校验已部署的工作流（没有节点 JSON 可查）。

**查看与生命周期**
- `n8n_get_workflow`，拉取一个工作流（full / structure / active / filtered / minimal）。编辑后用它核对 `connections`；`mode="filtered"` 加 `nodeNames` 可以只读取一个重节点，不必拉回整个可能在客户端被截断的工作流。
- `n8n_list_workflows`，列出/筛选（复制逻辑之前先搜一搜）。
- `n8n_delete_workflow`；`n8n_workflow_versions`（history/rollback/diff；`source: "native"` 含 UI 改动）；`n8n_instances`（仅限多实例账号；每个 n8n 工具也都接受每次调用指定的 `instance` 名，参见 `n8n-multi-instance`）；`n8n_health_check`（解析出的 `instanceName`，外加 `officialMcp`：下面的实例级 server 是否可达）。

**测试与运行**
- `n8n_test_workflow`，会真正运行节点（Code、HTTP、DB 写入、发送都会触发）。有副作用时，运行前先问用户。`method` 决定走哪条路径：`auto`（默认）和 `trigger` 通过 HTTP 触发一个**已激活**工作流上的 webhook/form/chat trigger；`prepare` / `pinned` / `direct` 则经由 n8n 自带的 MCP server，运行没有 HTTP trigger 的工作流（Manual、Schedule、子工作流），参见 `n8n-mcp-tools-expert`。
- `n8n_executions`，列出/查看 executions。**没有 `execute_workflow` 这个工具。**
- `n8n_evaluations`，评估运行、指标和各用例结果（n8n ≥ 2.30）；`run` / `cancel`（≥ 2.32）。`run` 会在整个数据集上触发真实节点，所以要先问用户。遇到 403，参见 `n8n-mcp-tools-expert`。

**数据、文件夹、凭据、审计**
- `n8n_manage_datatable`，Data Table 的 CRUD、筛选、dry-run。`addColumn` / `deleteColumn` / `renameColumn` 通过 n8n 的 MCP server 改动已有表的列（Public API 做不到），`deleteColumn` 会连该列的值一起删掉。
- `n8n_manage_folders`，文件夹 CRUD（n8n ≥ 2.19）。用 `parentFolderId` 或 `moveToFolder` 操作放置工作流；通过文件夹的 `get` 计数来核对，而不是看工作流。不带 `transferToFolderId` 的 `delete` 会归档该文件夹里的工作流。参见 `n8n-mcp-tools-expert`。
- `n8n_manage_credentials`，credential CRUD 加 `getSchema` 发现。
- `n8n_audit_instance`，安全审计（硬编码的 secrets、未鉴权的 webhook、错误处理的缺口）。

**实例级 MCP server** 是 Public API 之外的第二个端点，由 `N8N_MCP_ACCESS_TOKEN` 把关（n8n 2.34+）。`n8n_health_check` 会报告它是否可达；没有它，这些调用会返回 `NOT_CONFIGURED`。
- `n8n_manage_agents`，持久化的 n8n **Agents**：一种独立的助手产物，有自己的生命周期（model、instructions、skills、tasks、memory、channels），**不是** AI Agent 工作流节点。`call` 会用真实 credentials 实时运行它，并可能返回 `approvals[]`；只有用户要求时才 `publish`。参见 `n8n-agents`。
- `n8n_explore_node_resources`，通过真实 credential 解析节点实时的下拉 / resource-locator 取值，而不是猜一个 ID。参见 `n8n-node-configuration`。
- `n8n_list_catalog`，列出 `projects`（拿到 `projectId`）或 `tags`。这是这里唯一不靠 token 也能用的工具。
- 同一个 server 还支撑 `n8n_test_workflow` 的 `prepare` / `pinned` / `direct`、`source: "native"` 版本以及 Data Table 的列操作，按工作流逐个把关：`WORKFLOW_NOT_EXPOSED` 表示 "Available in MCP" 处于关闭状态，而把它打开（`exposeToMcp: true`）是一项持久改动，要先问用户。

> **节点类型写法陷阱：** `get_node` / `validate_node` 用 SHORT form（`nodes-base.set`）；
> `validate_workflow` / `n8n_create_workflow` 里的工作流 JSON 用 LONG form
> （`n8n-nodes-base.set`）。把两者混用是常见又静默的错误，参见 `n8n-mcp-tools-expert`。

## 操作流程，按顺序

1. 从索引里认出对应的 Skill，并**在第一次 MCP 调用前先调用它**。
2. 每个会话浏览一次 `tools_documentation`，拿不准时用来刷新对工具面的认识。
3. 配置任何节点前先 `get_node`，读实时 schema，别凭假设。
4. 构建 / 编辑，然后**激活前 `validate_workflow`**、**之后 `n8n_get_workflow`**，用来核对 `connections`。
5. 把发现的任何漂移都摆出来（工具缺失、参数变动、行为偏离）。

## 拿不准时

- **找不到用户在 UI 里建的工作流？** 最常见的原因是该工作流的 MCP access 没开。让用户在 n8n 里打开它，进 Settings，启用 MCP access。
- **用户说它坏了？** 相信用户。对照 `get_node` 复核参数，追踪数据引用，查看该次执行。参见 `n8n-validation-expert`。
- **没有合适的 Skill，而任务又不简单？** 先问，别猜。

这些是有立场的最佳实践，不是铁律。不同意其中某条？反正都是 markdown，直接改 Skill 就行。
