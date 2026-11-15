> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/dockerfile.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Dockerfile 语言提示词片段

## 核心概念

- **多阶段构建**：多个 `FROM` 语句分离构建与运行阶段，缩小镜像体积
- **层缓存**：每条指令生成一层；按改动频率从低到高排列指令以提高缓存命中
- **基础镜像**：`FROM image:tag` 选择起始镜像；优先选 slim/alpine 变体以减小体积
- **COPY 与 ADD**：本地文件用 `COPY`（推荐），URL 与 tar 解压用 `ADD`
- **构建参数**：`ARG` 定义构建期变量，`ENV` 定义运行时环境变量
- **健康检查**：`HEALTHCHECK` 指令供容器编排器做就绪探测
- **ENTRYPOINT 与 CMD**：`ENTRYPOINT` 设定可执行文件，`CMD` 提供默认参数
- **用户权限**：`USER` 指令以非 root 运行，提升安全性
- **忽略模式**：`.dockerignore` 把文件排除出构建上下文（类似 `.gitignore`）

## 重要文件模式

- `Dockerfile`：主容器镜像定义（项目根目录）
- `Dockerfile.dev` / `Dockerfile.prod`：环境专属 Dockerfile
- `docker-compose.yml`：多容器应用编排
- `docker-compose.override.yml`：本地开发覆盖配置
- `.dockerignore`：构建上下文排除模式

## 边模式

- Dockerfile 对其打包的应用入口（COPY/CMD 目标）建立 `deploys` 边
- docker-compose 对其引用构建的 Dockerfile 建立 `depends_on` 边
- Dockerfile 对其复制的包清单（package.json、requirements.txt）建立 `depends_on` 边，用于依赖安装
- docker-compose 服务在共同部署的组件之间创建 `related` 边

## 摘要风格

> "多阶段 Docker 构建：产出含 N 个构建阶段的极简 Node.js 生产镜像。"
> "Docker Compose 配置：编排 N 个服务，共享网络与持久卷。"
> "开发用 Dockerfile：支持热重载并挂载源码卷。"
