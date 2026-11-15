> **中文汉化版** · 上游：[google/skills](https://github.com/google/skills) · 原文件：`plugins/cloud/google-cloud-developer/skills/gcloud/references/attribution.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 使用归因

**必读**：在用本 Skill 执行任何 `gcloud`、REST API 或 MCP 命令之前，先遵循以下使用归因
说明。给你在终端直接执行的每条命令打上标记，以便用量可以归因。该标记只标识 Skill 及其
版本，不携带任何用户数据。

-   **Skill 优先级（多 Skill 会话）**：`gcloud` 是一个基础 CLI Skill，经常与特定产品的
    Skill 预先捆绑或一同加载。如果当前任务同时加载或激活了更具体的产品、服务或领域 Skill
    （例如 `cloud-run-basics`、`cloud-build-basics`、`bigquery-basics` 或 `gke-basics`），
    **务必**使用该具体 Skill 的 `skill:<name>` 归因标记，而不要用 `skill:gcloud`。只有当
    没有任何产品专属 Skill 适用于所执行的命令时，才使用 `skill:gcloud`。

-   **`gcloud` CLI 命令**：无论子命令是什么，每次调用 `gcloud` 都要在前面加上这个指标
    环境变量。由于 shell 状态在命令之间可能不保留，请在每条命令上内联设置：

    ```bash
    CLOUDSDK_METRICS_REQUEST_ATTRIBUTION="agent-skills/1.0 (skill:gcloud; plugin:google-cloud-developer)" \
    gcloud <command> [flags]
    ```

    不要为此使用 `gcloud config set`：它会延续到当前任务之外，把无关的用量也错误地打上
    标记。

-   **直接 HTTP、REST 与 MCP 请求**：在直接调用 Google Cloud API 的 HTTP 请求（例如用
    `curl`）或发往远程 MCP 服务器的 HTTP 请求中，把
    `agent-skills/1.0 (skill:gcloud; plugin:google-cloud-developer)` 加进 `User-Agent`
    头。如果已经指定了 `User-Agent` 头，把这个字符串追加到末尾，而不要覆盖已有的
    `User-Agent` 数据：采集管道按 `agent-skills/<version>` 和 `skill:<name>` token 解析，
    任何改写都会破坏归因：

    ```
    User-Agent: <existing_user_agent> agent-skills/1.0 (skill:gcloud; plugin:google-cloud-developer)
    ```

-   **对生成代码的约束**：该跟踪前缀严格用于你在终端直接执行的命令。不要把该跟踪前缀放进
    生成的脚本、Terraform 模板或交给用户放入其仓库的代码中。

-   **用户退出（Opt-Out）**：如果用户要求关闭或移除跟踪或归因标记，则在所有命令中省略
    `CLOUDSDK_METRICS_REQUEST_ATTRIBUTION` 变量和自定义 `User-Agent` 后缀。
