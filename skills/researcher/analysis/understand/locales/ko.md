> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/locales/ko.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 韩语输出指南（Korean）

本文件提供用韩语生成知识图谱内容时的语言专属指南。

## 标签约定

使用韩语标签或通用的英语技术术语：

| 模式 | 推荐标签 |
|------|---------|
| 入口文件 | `진입점`, `barrel`, `exports` 或 `entry-point` |
| 工具函数 | `유틸리티`, `helpers`, `utility` |
| API 处理器 | `api-handler`, `controller`, `endpoint` |
| 数据模型 | `데이터모델`, `entity`, `schema` 或 `data-model` |
| 测试文件 | `테스트`, `unit-test`, `test` |
| 配置文件 | `설정`, `build-system`, `configuration` |
| 基础设施 | `인프라`, `deployment`, `infrastructure` |
| 文档 | `문서`, `guide`, `documentation` |

**混合策略：** 通用技术术语保留英语（`middleware`、`api-handler` 等），描述性标签可用韩语。

## 摘要风格

用韩语撰写 1-2 句摘要：
- 描述文件的**目的**与**作用**
- 使用主动语态（"提供……"、"处理……"、"管理……"）
- 避免重复文件名

**示例：**
- 好："提供 API 层各处使用的日期格式化与字符串清洗辅助函数。"
- 差："utils 文件包含工具函数。"

## 技术术语

以下术语保留英语（无标准翻译）：
- `middleware`, `hook`, `barrel`, `entry-point`
- `ORM`, `REST API`, `CI/CD`, `CRUD`
- `singleton`, `factory`, `observer`
- `interceptor`, `guard`

## 层名称

使用韩语层名称：
- `API 레이어`, `서비스 레이어`, `데이터 레이어`, `UI 레이어`
- `인프라`, `설정`, `문서`
- `유틸리티 레이어`, `미들웨어 레이어`, `테스트 레이어`

或保留英语（按团队习惯）：
- `API Layer`, `Service Layer`, `Data Layer`
