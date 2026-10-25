---
name: skill-builder
description: 自动检测来源类型，并使用 Skill Seekers 构建 AI Skill。当用户想从文档站点、仓库、PDF、视频或其他知识来源创建 Skill 时使用。
---

> **中文汉化版** · 上游：[yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) · 原文件：`skills/skill-seekers/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Skill Builder

你可以访问 Skill Seekers MCP 服务器，它提供 40 个工具，用于把知识来源转换为 AI 可用的 Skill。

## 何时使用本 Skill

当用户有以下需求时使用本 Skill：
- 想从文档站点、GitHub 仓库、PDF、视频或其他来源创建一个 AI Skill
- 需要把文档转换为适合 LLM 消费的格式
- 想根据其来源文档更新或同步已有的 Skill
- 需要把 Skill 导出到向量数据库（Weaviate、Chroma、FAISS、Qdrant）
- 询问如何为 AI 抓取、转换或打包文档

## 来源类型检测

根据用户输入自动检测来源类型：

| 输入模式 | 来源类型 | 使用的工具 |
|---------------|-------------|-------------|
| `https://...`（非 GitHub/YouTube） | 文档 | `scrape_docs` |
| `owner/repo` 或 `github.com/...` | GitHub | `scrape_github` |
| `*.pdf` | PDF | `scrape_pdf` |
| YouTube/Vimeo URL 或视频文件 | 视频 | `scrape_video` |
| 本地目录路径 | 代码库 | `scrape_codebase` |
| `*.ipynb`、`*.html`、`*.yaml`（OpenAPI）、`*.adoc`、`*.pptx`、`*.rss`、`*.1`-`.8` | 多种 | `scrape_generic` |
| JSON 配置文件 | 统一入口 | 使用配置配合 `scrape_docs` |

## 推荐工作流

1. 根据用户输入**检测来源类型**
2. 如有需要，使用 `generate_config` 或 `fetch_config` **生成或获取配置**
3. 对文档站点使用 `estimate_pages` **估算规模**
4. 使用合适的抓取工具**抓取来源**
5. 如果用户想要 AI 增强改进，使用 `enhance_skill` 进行**增强**
6. 使用 `package_skill` 为目标平台**打包**
7. 如有要求，使用 `export_to_*` 工具**导出到向量数据库**

## 可用的 MCP 工具

### 配置管理
- `generate_config` — 根据 URL 生成抓取配置
- `list_configs` — 列出可用的预设配置
- `validate_config` — 校验配置文件

### 抓取（按来源类型选用）
- `scrape_docs` — 文档站点
- `scrape_github` — GitHub 仓库
- `scrape_pdf` — PDF 文件
- `scrape_video` — 视频字幕/转录
- `scrape_codebase` — 本地代码分析
- `scrape_generic` — Jupyter、HTML、OpenAPI、AsciiDoc、PPTX、RSS、manpage、Confluence、Notion、聊天记录

### 后处理
- `enhance_skill` — AI 驱动的 Skill 增强
- `package_skill` — 为目标平台打包
- `upload_skill` — 上传到平台 API
- `install_skill` — 端到端安装工作流

### 高级
- `detect_patterns` — 代码中的设计模式检测
- `extract_test_examples` — 从测试中提取用法示例
- `build_how_to_guides` — 从测试生成 how-to 指南
- `split_config` — 把大型配置拆分为聚焦的 Skill
- `export_to_weaviate`、`export_to_chroma`、`export_to_faiss`、`export_to_qdrant` — 向量数据库导出
