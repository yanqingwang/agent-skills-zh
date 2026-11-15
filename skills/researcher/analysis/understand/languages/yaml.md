> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/yaml.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# YAML 语言提示词片段

## 核心概念

- **缩进嵌套**：空白敏感的结构层级（只能用空格，不能用制表符）
- **锚点与别名**：`&anchor` 定义可复用块，`*anchor` 引用它避免重复
- **合并键**：`<<: *anchor` 把锚点内容合并进当前映射
- **多行字符串**：字面块（`|`）保留换行，折叠块（`>`）拼接行
- **文档分隔符**：`---` 开始新文档，`...` 结束文档（多文档流）
- **标签与类型**：`!!str`、`!!int`、`!!bool` 显式标型；自定义标签用于应用专属类型
- **流式风格**：内联 JSON 风格语法 `{key: value}` 与 `[item1, item2]`，表示紧凑写法
- **环境变量替换**：`${VAR}` 模式，用于 docker-compose 与 CI 配置

## 重要文件模式

- `docker-compose.yml` / `docker-compose.yaml`：多容器 Docker 应用定义
- `.github/workflows/*.yml`：GitHub Actions CI/CD 工作流定义
- `.gitlab-ci.yml`：GitLab CI/CD 流水线配置
- `kubernetes/*.yaml` / `k8s/*.yaml`：Kubernetes 资源清单
- `*.config.yaml`：应用配置文件
- `mkdocs.yml`：MkDocs 文档站点配置
- `serverless.yml`：Serverless Framework 配置

## 边模式

- YAML 配置文件对其控制的代码模块建立 `configures` 边（如数据库设置影响数据层）
- CI/CD YAML 文件对构建与部署流水线建立 `triggers` 边
- docker-compose YAML `deploys` 服务，并对其引用的 Dockerfile 建立 `depends_on` 边
- Kubernetes YAML 对应用服务建立 `deploys` 与 `provisions` 边

## 摘要风格

> "Docker Compose 配置：定义 N 个服务，含网络、卷与健康检查。"
> "GitHub Actions 工作流：push 时运行测试，合并到 main 后部署生产。"
> "Kubernetes 部署清单：N 个副本、资源限制与存活探针。"
