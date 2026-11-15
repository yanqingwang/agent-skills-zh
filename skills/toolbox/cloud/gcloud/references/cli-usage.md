> **中文汉化版** · 上游：[google/skills](https://github.com/google/skills) · 原文件：`plugins/cloud/google-cloud-developer/skills/gcloud/references/cli-usage.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# gcloud CLI 使用说明

本文档提供在本地与自动化环境中安装、授权和配置 Google Cloud SDK（`gcloud` CLI）的参考
信息。

## 安装

如果执行环境中没有 `gcloud` 二进制文件，请参考权威的
[Google Cloud CLI 安装指南](https://docs.cloud.google.com/sdk/docs/install-sdk.md.txt)
获取各平台的安装说明（Linux、macOS、Windows、包管理器和容器镜像）。

> [!CAUTION]
> **安装 `gcloud` CLI 前必须获得用户明确确认：**
> 绝不能自主安装 Google Cloud CLI（`gcloud` CLI）或额外的 `gcloud` CLI 组件
> （`gcloud components install` / `gcloud components update`）。
>
> 在执行任何安装命令或包管理器脚本之前：
> 1. 告知用户 `gcloud` CLI（或所需组件）尚未安装，并概述你计划使用的安装方式。
> 2. 请求用户明确同意：`"I am ready to install the Google Cloud CLI (gcloud) on your
>    machine. Do you want me to proceed?"`
> 3. **关键**：在当前这一轮中，代理**绝不能**执行任何 `gcloud` 安装或组件安装命令。你必须
>    发出征询同意的提问，然后**严格停下**，等待用户的肯定答复。

### 组件管理

`gcloud components` 命令组管理可选的 CLI 组件（例如额外的工具、模拟器和语言运行时）：

-   **列出可用组件：**

    ```bash
    gcloud components list
    ```

-   **安装组件：**

    ```bash
    gcloud components install {component_id} --quiet
    ```

-   **更新所有已安装组件：**

    ```bash
    gcloud components update --quiet
    ```

*（注：如果 `gcloud` 是通过 APT 或 DNF 之类的系统包管理器安装的，请改用该系统包管理器
安装组件，而不是 `gcloud components install`。）*

## 授权与认证

根据运行环境，用以下方式向 Google Cloud 认证 CLI：

-   **用户账号（交互式）：**

    ```bash
    gcloud auth login
    ```

    按浏览器提示登录并授予访问权限。

-   **用户账号（无浏览器流程）：**

    适用于没有可用网页浏览器的环境（容器、远程 SSH）：

    ```bash
    gcloud auth login --no-browser
    ```

    复制生成的 URL，在另一台机器上打开以完成登录，再把授权码粘贴回终端。

-   **Application Default Credentials（ADC）：**

    为客户端库和本地应用配置凭证：

    ```bash
    gcloud auth application-default login
    ```

    在无头环境中追加 `--no-browser`。

-   **服务账号密钥（无头自动化）：**

    ```bash
    gcloud auth activate-service-account --key-file=path/to/key.json
    ```

    *安全提示：严格限制 JSON 密钥文件的权限，或优先改用 Workload Identity / 身份模拟。*

-   **服务账号身份模拟（开发与 Agent 场景首选）：**

    允许用户身份临时充当某个服务账号的身份，无需长期保存私钥文件：

    ```bash
    gcloud config set auth/impersonate_service_account {service_account_email}
    ```

    需要在目标服务账号上持有 `roles/iam.serviceAccountTokenCreator` 角色。这样能落实
    最小权限，并保证访问以目标身份执行、可审计。

-   **Workload Identity Federation：**

    适用于 CI/CD 和外部计算环境（GitHub Actions、AWS、本地机房），使用联合 token 认证，
    无需管理服务账号密钥。参见
    [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate.md.txt)。

## 本地配置管理

`gcloud config` 命令组管理本地配置设置、profile 和默认属性。

### 命名配置（Named Configurations）

配置（configuration）允许维护多套相互隔离的属性集（例如 dev、staging、prod）：

-   **新建配置：**

    ```bash
    gcloud config configurations create {config_name}
    ```

-   **列出现有配置：**

    ```bash
    gcloud config configurations list
    ```

-   **激活某个配置：**

    ```bash
    gcloud config configurations activate {config_name}
    ```

### 设置常用属性

属性为跨 `gcloud` 调用的标志设置默认值：

-   **设置当前项目：**

    ```bash
    gcloud config set core/project {project_id}
    ```

-   **设置默认的 compute region 与 zone：**

    ```bash
    gcloud config set compute/region {region}
    gcloud config set compute/zone {zone}
    ```

-   **查看所有生效的配置属性：**

    ```bash
    gcloud config list
    ```
