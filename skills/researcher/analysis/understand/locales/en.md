> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/locales/en.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 英语输出指南

本文件提供用英语生成知识图谱内容时的语言专属指南。

## 标签约定

使用小写、连字符分隔的英语标签：

| 模式 | 推荐标签 |
|---------|-----------------|
| 入口文件 | `entry-point`, `barrel`, `exports` |
| 工具函数 | `utility`, `helpers`, `common` |
| API 处理器 | `api-handler`, `controller`, `endpoint` |
| 数据模型 | `data-model`, `entity`, `schema` |
| 测试文件 | `test`, `spec`, `unit-test` |
| 配置 | `configuration`, `build-system`, `settings` |
| 基础设施 | `infrastructure`, `deployment`, `containerization` |
| 文档 | `documentation`, `guide`, `reference` |

## 摘要风格

写 1-2 句摘要，要求：
- 描述**用途**与**在项目中的角色**
- 使用主动语态（"提供……"、"处理……"、"管理……"）
- 避免复述文件名

**示例：**
- 好："提供 API 层各处使用的日期格式化与字符串清洗辅助函数。"
- 差："utils 文件包含工具函数。"

## 技术术语

以下术语保留英语（无需翻译）：
- `middleware`, `hook`, `barrel`, `entry-point`
- `ORM`, `REST API`, `CI/CD`, `CRUD`
- `singleton`, `factory`, `observer`
- `middleware`, `interceptor`, `guard`

## 层名称

使用标准英语层名称：
- `API Layer`, `Service Layer`, `Data Layer`, `UI Layer`
- `Infrastructure`, `Configuration`, `Documentation`
- `Utility Layer`, `Middleware Layer`, `Test Layer`
