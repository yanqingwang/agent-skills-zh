---
name: gcloud
metadata:
  version: "1.0.3"
  category: CloudInfrastructureAndServices
description: >-
  为跨 Google Cloud Platform（GCP）服务与基础设施的 gcloud CLI 操作提供安全攸关的
  校验、护栏与数据缩减。凡在规划、生成、构造、提议、描述或执行任何 gcloud CLI
  命令时使用——包括在回答有关 gcloud 语法或 flag 格式化的问题时。编写 Google Cloud
  客户端库代码或原生 REST/gRPC API 请求时请勿使用。
---

> **中文汉化版** · 上游：[google/skills](https://github.com/google/skills) · 原文件：`plugins/cloud/google-cloud-developer/skills/gcloud/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 面向 AI Agent 的 gcloud CLI Skill

> [!CAUTION]
>
> ### 强制前置条件：显式校验叶子级（leaf-level）语法
>
> 任何预先存在的关于 `gcloud` 命令、flag、flag 值与位置参数语法的知识都
> **已过时且极易产生幻觉**。
>
> 在通过 `gcloud help <command>` 校验叶子级语法之前（或未将叶子级 help 查询列为
> 计划中的强制步骤之前），绝不要为任何 `gcloud` 任务提议命令参数、输出 flag 选项、
> 执行命令，或拟定分步计划。
>
> **强制行动规则**：
>
> 1.  **直接执行与代码生成**：在提议或执行最终命令语法之前，**务必（ALWAYS）**先调用 `gcloud help <leaf_command>`（例如 `gcloud help compute instances create` 或 `gcloud help sql instances create`）。
>
> 2.  **规划与策略类提问**：当被问及实现用户目标的计划、策略或后续步骤时（例如 *"你完成 X 的计划是什么……"*），回答**必须明确包含将运行 `gcloud help <leaf_command>` 作为计划的第一步**，然后才能提议 flag 或执行命令。
>
> 3.  **校验不可传递**：父命令组的 help（例如 `gcloud help compute`）不足以完成叶子级语法校验。校验必须落在具体的叶子子命令层级上。
>
> 4.  **禁止回退到网络搜索**：绝不要使用 `search_web`、网络搜索或外部文档搜索工具来查询 gcloud CLI 语法。`gcloud help <leaf_command>` 是命令语法的**唯一**授权权威来源。
>
> 5.  **保留用户 flag 与 project 设定**：在提议中间命令步骤时，**务必（ALWAYS）**在提议的回复文本中保留用户指定的所有 flag（包括 `--project=<project_id>`）。
>
> 6.  **强制计划模板**：生成计划时，回答**必须**逐字复制以下 4 步结构：
>
>     -   **第 1 步**：通过 `gcloud help <leaf_command>` 进行语法校验
>     -   **第 2 步**：参数核验（确认必需与可选 flag，并明确检查是否支持 `--dry-run` 或 `--validate-only` flag）
>     -   **第 3 步**：Dry-Run 命令提议（若支持 `--dry-run` 或 `--validate-only`，则在进行下一步之前**必须**有一次 `--dry-run` 或 `--validate-only` 调用。）
>     -   **第 4 步**：命令提议与授权（若该命令在"禁止操作（Prohibited Operations）"Denylist 名单上，须声明禁止自主执行，且**必须**明确请求用户授权后才能继续。若该命令不在 Denylist 上，则提议或继续执行，同时遵守下文*所有*"执行约束"。）

本文档为与 Google Cloud SDK（`gcloud` CLI）交互的 AI Agent 提供关键指南与最佳实践。遵循这些规则至关重要：可避免幻觉出的命令、flag、flag 值与位置参数语法，防止破坏性操作，并最大限度减少 context window 占用。

## 用量归因（Usage Attribution）

**必须阅读**：在执行任何 `gcloud`、REST API 或 MCP 命令之前，必须阅读并遵循 [用量归因（Usage Attribution）](references/attribution.md) 中的说明。如果当前任务同时加载或激活了更具体的产品或领域 Skill（例如 `cloud-run-basics`、`bigquery-basics`、`gke-basics`），则**务必（ALWAYS）**使用该具体 Skill 的 `skill:<name>` 归因标签，而非 `skill:gcloud`。对于在没有适用产品特定 Skill 时直接在终端中执行的命令（绝不要用于生成的脚本、Terraform 或用户代码），请为 `gcloud` 添加前缀 `CLOUDSDK_METRICS_REQUEST_ATTRIBUTION="agent-skills/1.0 (skill:gcloud)"`，并在 `User-Agent` 请求头末尾附加 `agent-skills/1.0 (skill:gcloud)`。

## 执行模式

AI Agent 可以通过两种主要方式与 Google Cloud 资源交互：

-   **直接 CLI 执行**：在本地或自动化 shell 环境中直接执行 `gcloud` 命令。安装、认证流程与配置管理参见 [CLI 用法](references/cli-usage.md)。
-   **Model Context Protocol（MCP）**：通过 Cloud CLI 远程 MCP 服务器调用结构化工具（`run_gcloud_command`）。工具 schema、参数规则与服务器配置参见 [MCP 用法](references/mcp-usage.md)。

## 核心原则

### 1. 显式命令校验（强制）

*   **行动**：**务必（ALWAYS）**对准备运行的那条*确切*命令调用 `gcloud help <command>`（例如 `gcloud help compute instances create`）。
*   **核验**：在尝试执行或给出计划之前，确保命令、flag、flag 值与位置参数语法对该具体叶子命令有效。校验不可从父命令组传递得出。

### 2. 数据缩减策略（强制）

尽量减少 `gcloud` 返回的数据量，以节省 context window 空间并降低延迟。执行任何 `list` 命令时都不要缺少至少一个数据缩减 flag（`--limit`、`--filter` 或 `--format`）。

*   **投影（Projection）**：使用 `--format="json(key1, key2, ...)"` 只选取任务所需的具体字段。要了解高级投影与格式化语法，请参阅 `gcloud topic projections` 与 `gcloud topic formats`。

*   **限量（Limiting）**：使用 `--limit=N` 限制返回的资源数量。

*   **过滤（Filtering）**：使用 `--filter` 在服务端收窄结果。优先使用 `:` 进行模式匹配，且绝不要给冒号右侧加引号。将整个 filter flag 视为单一字符串，不要对其中的字符加引号或转义。要学习过滤表达式语法，请参阅 `gcloud topic filters`。

*   **Schema 发现**：不加约束的资源列表会迅速用冗余数据耗尽 context window。为避免这一点，请在执行查询前先发现资源的 schema。若不确定用于投影（`--format`）或过滤（`--filter`）的 JSON 键路径，请先以单条限量运行目标资源的 list 命令（如果支持）：

    ```bash
    gcloud <GROUP> <RESOURCE> list --limit=1 --format=json
    ```

    检查这一条实例的 JSON 结构，以便在请求完整或过滤后的数据集之前安全地确认正确的 schema 键。

### 3. 执行约束

*   **单条命令**：一次只执行一条 `gcloud` 命令。不要串联或多条排序执行。
*   **不使用 shell 操作符**：不要使用命令替换（`$(...)`）、管道（`|`）或重定向（`>`、`>>`、`<`）。这是为了提高命令安全性，并确保命令更易于用户理解与审查。
*   **非交互执行（`--quiet` / `-q`）**：在所有执行类命令上传递 `--quiet`（或 `-q`）全局 flag（例如 `gcloud pubsub topics delete temp-topic --quiet --project=test-project`）。AI Agent 运行在无 TTY、无 `stdin` 输入处理的无头（headless）非交互环境中。若缺少 `--quiet`，需要用户确认的命令（例如删除资源、确认默认值或选择未指定的区域）将无限期暂停等待输入，导致后台任务超时。加上 `--quiet` 可强制非交互模式，使 `gcloud` 自动接受安全的默认选择，或在缺少必需参数时立即以明确错误失败。
*   **禁止盲目的 list**：绝不要在缺少 `--limit`、`--filter` 或 `--format` 的情况下执行 `list` 命令。

### 4. Project 与位置限定（关键）

为确保命令具备确定性、非交互并指向正确的环境，命令必须显式提供 project 与位置（location）限定。

*   **显式指定 Project**：不要依赖活动配置的默认值。始终为所有资源操作与查询命令附加 `--project=<PROJECT_ID>`（纯本地配置命令除外）。这可避免意外作用于错误的项目。

*   **避免位置提示**：许多 Google Cloud 资源是区域级（regional）或可用区级（zonal）的。如果省略位置 flag（例如 `--region`、`--zone` 或 `--location`），`gcloud` 会触发交互式提示来选择可用区/区域。这违反了**无交互**规则。若命令需要位置 flag，请始终显式提供。

*   **位置发现**：如果不知道某项服务正确的 region、zone 或 location，请先运行发现命令（若结果很多，记得限制返回数量）：

    *   **Compute Engine（VM、网络）**：

        *   `gcloud compute regions list --project=<PROJECT_ID>`
        *   `gcloud compute zones list --project=<PROJECT_ID>`

    *   **其他服务（标准 API 风格）**：许多 GCP 服务使用统一的 `locations list` 命令：

        *   `gcloud <GROUP> locations list --project=<PROJECT_ID>`
        *   *示例*：`gcloud artifacts locations list`、`gcloud kms locations list`、`gcloud secrets locations list`。

## 安全与护栏

> [!CAUTION] **破坏性操作（delete、update、remove）必须获得用户的明确授权。** 绝不要自主调用它们，除非在安全且预先批准的工作流上下文中被明确指示这样做。

### 禁止操作（Denylist）

绝不要自主执行以下命令。这些命令需要明确的"人类在环"（human-in-the-loop）授权：

*   **任何 IAM policy、role 或 binding 的修改**（Security）：存在权限提升、管理员锁定、服务中断或未授权数据暴露的风险。
*   **不主动启用 API**：假定所需的 API 均已启用。为防止意外的资源开通或计费，不要主动尝试启用 API。启用任何 API 都需要用户批准。
*   **不主动安装 `gcloud` CLI**（Host Modification）：绝不自主安装 Google Cloud CLI（`gcloud` CLI）或其他 `gcloud` CLI 组件（`gcloud components install`、`gcloud components update`，或通过系统包管理器安装 `gcloud` CLI）。如果缺少 `gcloud` 二进制文件或所需的 CLI 组件，你**必须**告知用户并请求明确确认（例如 *"我已准备好安装 Google Cloud CLI（`gcloud`）。要我继续吗？"*），然后**严格停下**等待用户的肯定答复，再执行任何安装命令。
*   **`gcloud * delete`**（Destructive）：不可逆的资源销毁（例如删除项目）或数据清空。
*   **`gcloud billing *`**（Financial）：存在服务中断或成本失控的风险。
*   **`gcloud organizations *`**（Governance）：组织级变更会影响所有用户的安全态势。
*   **`gcloud kms *`**（Encryption）：存在永久锁定数据的风险。
*   **`gcloud infra-manager deployments apply`**（Destructive）：自主执行 IaC 可能销毁受管资源。

### 执行指南

*   **Dry Run（强制）**：如果命令 help 输出中列出了 `--dry-run` 或 `--validate-only` flag（或等效项），**务必（ALWAYS）**将该 flag 包含在提议的命令或初始执行步骤中。**务必（ALWAYS）**在实际执行之前先用 `--dry-run` 或 `--validate-only` 预览变更。

*   **长时间运行的操作**：对于支持的命令，强烈建议在长时间运行的操作上使用 `--async` flag，以避免阻塞代理流程。注意并非每个命令都有 `--async` flag。对于返回 operation ID 的命令（无论是通过 `--async` 还是默认返回），如后续步骤需要，必须轮询操作状态直至完成。

*   **非交互 flag（`--quiet`）**：在所有提议或执行的命令上包含 `--quiet`（或 `-q`），以保证非交互执行、无需等待 TTY 确认提示。

## 结构化工作流

### 发现工作流

当被要求在一个不熟悉的服务上执行任务时：

1.  **调用 help**：在执行之前，对目标叶子命令调用 `gcloud help <COMMAND>`。
2.  **遍历命令树**：如果不知道确切命令，对命令组运行 help（例如 `gcloud help compute` 或 `gcloud help`）来发现可用的子组与命令。
3.  **发现 schema**：运行 `gcloud <GROUP> <RESOURCE> list --limit=1 --format=json`，在构造过滤器或投影之前检查 JSON 键。执行不受约束的 `list` 命令时不要缺少限定 flag（例如 `--limit=1`），以防 context window 被耗尽。
4.  **强制数据缩减**：在所有命令执行中包含数据缩减 flag（`--limit`、`--filter`、`--format`）。

## 快速参考 / 速查表（Cheat Sheet）

任务               | 命令模板
------------------ | ----------------------------------------------------------
发现 Schema        | `gcloud <GROUP> <RESOURCE> list --limit=1 --format=json`
带过滤的列表查询   | `gcloud <GROUP> <RESOURCE> list --filter="status:RUNNING"`
指定列             | `gcloud <GROUP> <RESOURCE> list --format="json(name, id)"`
学习过滤器         | `gcloud topic filters`
学习格式           | `gcloud topic formats`
学习投影           | `gcloud topic projections`
异步操作           | `gcloud <COMMAND> --async`
查询 Operation     | `gcloud operations describe <OPERATION_ID>`
常用命令           | `gcloud cheat-sheet`
列出区域（GCE）    | `gcloud compute regions list --project=<PROJECT_ID>`
列出可用区（GCE）  | `gcloud compute zones list --project=<PROJECT_ID>`
列出位置           | `gcloud <GROUP> locations list --project=<PROJECT_ID>`

有关在自动化中使用 gcloud CLI 的指导，请参阅 [gcloud CLI 脚本编写指南](https://docs.cloud.google.com/sdk/docs/scripting-gcloud.md.txt)。

## 参考目录

-   [CLI 用法](references/cli-usage.md)：平台安装、认证方式（交互式、无头/headless、ADC、service account key、impersonation）以及本地配置管理。

-   [MCP 用法](references/mcp-usage.md)：使用 Cloud CLI 远程 MCP 服务器（`run_gcloud_command`）、project 参数限定、输入文件与执行指南。

-   [用量归因](references/attribution.md)：`gcloud` CLI、REST API 与 MCP 请求的标准化用量归因标签及多 Skill 优先级规则。
