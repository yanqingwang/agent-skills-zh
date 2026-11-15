> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/locales/vi.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 越南语输出指南（Vietnamese）

本文件提供用越南语生成知识图谱内容时的语言专属指南。

## 标签约定

使用越南语标签或通用的英语技术术语：

| 模式 | 推荐标签 |
|---------|---------|
| 入口文件 | `điểm-vào`, `barrel`, `exports` 或 `entry-point` |
| 工具函数 | `tiện-ích`, `helpers`, `utility` |
| API 处理器 | `api-handler`, `controller`, `endpoint` |
| 数据模型 | `mô-hình-dữ-liệu`, `entity`, `schema` 或 `data-model` |
| 测试文件 | `kiểm-thử`, `unit-test`, `test` |
| 配置文件 | `cấu-hình`, `build-system`, `configuration` |
| 基础设施 | `hạ-tầng`, `deployment`, `infrastructure` |
| 文档 | `tài-liệu`, `guide`, `documentation` |

**混合策略：** 通用技术术语保留英语（`middleware`、`api-handler` 等）；描述性标签可用越南语。

## 摘要风格

用越南语撰写 1-2 句摘要：
- 描述文件的**目的**与**作用**
- 使用主动语态（"提供……"、"处理……"、"管理……"）
- 避免重复文件名

**示例：**
- 好："提供日期格式化与字符串清洗的工具函数，在整个 API 层使用。"
- 差："utils 文件包含工具函数。"

## 技术术语

以下术语保留英语（无标准翻译时）：
- `middleware`, `hook`, `barrel`, `entry-point`
- `ORM`, `REST API`, `CI/CD`, `CRUD`
- `singleton`, `factory`, `observer`
- `interceptor`, `guard`

## 层名称

使用越南语层名称：
- `Tầng API`, `Tầng dịch vụ`, `Tầng dữ liệu`, `Tầng giao diện`
- `Hạ tầng`, `Cấu hình`, `Tài liệu`
- `Tầng tiện ích`, `Tầng middleware`, `Tầng kiểm thử`

或保留英语（按团队约定）：
- `API Layer`, `Service Layer`, `Data Layer`
