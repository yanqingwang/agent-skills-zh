> **中文汉化版** · 上游：[google/skills](https://github.com/google/skills) · 原文件：`plugins/cloud/google-cloud-developer/skills/gcloud/references/mcp-usage.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Cloud CLI 远程 MCP 服务器使用说明

Google Cloud 资源可以通过模型上下文协议（MCP）来管理，让 AI Agent 通过结构化的工具调用
与 Google Cloud 交互，而不是直接执行本地 shell 命令。

`gcloud` 的 MCP 操作通过 **Cloud CLI 远程 MCP 服务器**执行（底层为 Cloud CLI Execution
API，`cloudcli.googleapis.com`）。

## 服务器端点与工具概览

-   **服务器端点：** `https://cloudcli.googleapis.com/mcp`
-   **传输方式：** HTTP（JSON-RPC 2.0）
-   **API 名称：** Cloud CLI Execution API（`cloudcli.googleapis.com`）
-   **可用工具：** `run_gcloud_command`

`run_gcloud_command` 工具在受管的远程环境中，代表用户安全地执行单条 `gcloud` 命令。

## 客户端配置（`mcp_config.json`）

要把 MCP 客户端（例如 Antigravity）连接到远程 Cloud CLI MCP 服务器，请在
`mcp_config.json` 中配置该服务器条目，并把 `authProviderType` 设置为
`"google_credentials"`：

```json
{
  "mcpServers": {
    "gcloud-remote": {
      "serverUrl": "https://cloudcli.googleapis.com/mcp",
      "authProviderType": "google_credentials"
    }
  }
}
```

> [!IMPORTANT] 必须指定 `"authProviderType": "google_credentials"`。它指示 MCP 客户端附带
> 带 `https://www.googleapis.com/auth/cloud-platform` OAuth 作用域的 Application Default
> Credentials（ADC）。省略该字段会导致客户端发送未认证请求，从而出现 `401 Unauthorized`
> 错误。

## 前提条件与 IAM 要求

使用 Cloud CLI 远程 MCP 服务器之前，目标项目和调用方身份必须满足两个强制前提条件：

### 1. 启用 API

必须在目标项目上启用 Cloud CLI Execution API（`cloudcli.googleapis.com`）。

-   **通过 Google Cloud 控制台（无需 CLI）：**

    1.  打开 [Google Cloud 控制台](https://console.cloud.google.com/)。
    2.  依次进入 **APIs & Services** --> **Library**。
    3.  搜索 **Cloud CLI Execution API**（或打开
        [Cloud CLI Execution API 库页面](https://console.cloud.google.com/apis/library/cloudcli.googleapis.com)）。
    4.  在项目下拉框中选择目标项目。
    5.  点击 **Enable**。

-   **通过 `gcloud` CLI：**

    ```bash
    gcloud services enable cloudcli.googleapis.com --project={project_id}
    ```

### 2. IAM 角色与权限

-   **MCP 访问角色：** 调用方身份必须在目标项目上持有 **MCP Tool User** 角色
    （`roles/mcp.toolUser`，该角色授予 `mcp.tools.call` 权限）。
-   **下游资源角色：** 调用方身份还必须对被查询或修改的底层资源持有标准 IAM 权限（例如
    `roles/compute.viewer`、`roles/run.developer`）。

> [!CAUTION] 如果 Cloud CLI Execution API 未启用，或调用方缺少 `roles/mcp.toolUser` 角色，
> 端点在工具发现（`tools/list`）和工具调用（`tools/call`）两个阶段都会返回
> **`403 Forbidden`**。

## 工具参数

对 `run_gcloud_command` 的调用接受以下参数：

-   **`command`**（字符串，必填）：要执行的完整 `gcloud` 命令行字符串（例如
    `"gcloud compute instances list --project={resource_project} --format=json"`）。
-   **`project`**（字符串，必填）：承载 Cloud CLI Execution API 的 Google Cloud 项目的
    资源名，格式为 `"projects/{api_project}"`（例如 `"projects/my-api-project"`）。
-   **`input_files`**（对象列表，可选）：在运行命令前预置到远程执行环境中的文件。每个条目
    包含相对路径 `path` 和字符串 `contents`。

> [!IMPORTANT] **API 宿主项目与资源项目上下文的区别：**
>
> -   顶层的 **`project`** 参数（`"projects/{api_project}"`）**严格用于
>     `cloudcli.googleapis.com` API 本身的配额、计费和 API 启用**。它不会为所执行的命令
>     设置项目上下文。
> -   对于**项目级命令**，必须在 `command` 字符串中显式包含
>     `--project={resource_project}`。目标 `{resource_project}` 不必是承载 Cloud CLI
>     Execution API 的项目。
> -   对于**非项目级命令**（例如账单、文件夹或组织查询），如果底层 API 要求配额项目，必须
>     在 `command` 字符串中包含 `--billing-project={billing_project}`。

### 调用示例

#### 1. 基础命令执行

```json
{
  "command": "gcloud compute instances list --project=my-resource-project --format=json",
  "project": "projects/my-cloudcli-api-project"
}
```

#### 2. 带输入文件的命令

```json
{
  "command": "gcloud run services replace service-config.yaml --region=us-central1 --project=my-resource-project",
  "project": "projects/my-cloudcli-api-project",
  "input_files": [
    {
      "path": "service-config.yaml",
      "contents": "apiVersion: serving.knative.dev/v1\nkind: Service\nmetadata:\n  name: my-service\n..."
    }
  ]
}
```

## 响应结构

该工具返回一个执行响应，包含：

-   `exit_code`：命令执行的数字退出状态。**这是判断命令成功与否的首要且权威的指标。**
-   `stdout`：命令的标准输出流。
-   `stderr`：命令的标准错误流。
-   `output_files`：命令生成的所有文件。

> [!NOTE] - **退出码权威性：** 当且仅当 `exit_code == 0` 时命令才算成功。`exit_code`
> 非零表示失败。
>
> -   **`stderr` 中的提示性输出：** 在 `gcloud` 中，即使命令执行成功（`exit_code == 0`），
>     `stderr` 也经常包含标准状态消息、进度更新和异步跟踪 ID（例如 `--async` 操作 ID）。
>     Agent 绝不能仅因 `stderr` 非空就认定命令失败。
> -   **错误诊断：** 如果 `exit_code != 0`，诊断错误信息可能出现在 `stderr` 或 `stdout`
>     中。要检查两个流，弄清失败原因并制定修正方案。

## 禁用与不支持的命令

Cloud CLI 远程 MCP 服务器运行在沙箱化、非交互式的环境中。下面列出部分不受支持的
`gcloud` 命令示例（例如管理本地机器配置、凭证、交互式 shell 或元数据的命令组）。该列表
并不详尽，命令可能在不另行通知的情况下被增删：

-   `gcloud auth`（本地认证与凭证管理）
-   `gcloud config`（本地 CLI 配置 profile 与属性）
-   `gcloud iam service-accounts`（服务账号管理）
-   `gcloud init`（交互式设置向导）
-   `gcloud survey`（用户反馈与调查）
-   `gcloud compute ssh` / `gcloud app instances ssh`（交互式 SSH shell）

## 安全与执行准则

-   **变更类操作必须获得用户同意：** 破坏性或改变状态的命令（例如 `create`、`delete`、
    `update`、`patch`）会修改或销毁 GCP 资源。除非用户已明确授权该操作，否则绝不能自主
    调用这些命令。
-   **异步操作（`--async`）：** 对于长时间运行的操作（例如创建 VM 实例、GKE 集群或数据库
    实例），务必在 `command` 字符串中附加 `--async` 标志，以避免执行超时。
-   **数据缩减与格式化：** 在 `command` 字符串中使用 `--format=json`、`--filter` 和
    `--limit` 来约束输出量，防止 context window 膨胀。
-   **非交互执行（`--quiet`）：** 对于可能触发交互式用户确认的命令，加上 `--quiet`
    （或 `-q`）。
