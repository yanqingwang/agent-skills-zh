> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/markdown.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Markdown 语言提示词片段

## 核心概念

- **标题层级**：`#` 到 `######` 构成文档结构，h1 为标题
- **Front Matter**：文件顶部的 YAML 元数据，由 `---` 分隔符包裹
- **围栏代码块**：三反引号加可选语言标识，用于语法高亮
- **引用式链接**：`[text][ref]` 配合 `[ref]: url` 定义，适合重复出现的 URL
- **表格**：竖线分隔列，带对齐标记（`:---`、`:---:`、`---:`）
- **提示块**：基于引用的标注（`> **Note:**`、`> **Warning:**`）用于强调
- **任务列表**：`- [ ]` 与 `- [x]` 用于 issue 跟踪器与 README 中的清单
- **HTML 嵌入**：可内联原始 HTML，覆盖 Markdown 原生不支持的功能

## 重要文件模式

- `README.md`：项目概览与新贡献者入口（高价值）
- `CONTRIBUTING.md`：贡献指南、代码风格、PR 流程
- `CHANGELOG.md`：遵循 Keep a Changelog 等格式的版本历史
- `docs/**/*.md`：文档目录，含指南、API 参考、教程
- 源码目录中的 `*.md`：模块或包的就近文档
- `ADR-*.md` 或 `adr/*.md`：架构决策记录

## 边模式

- Markdown 文件对其描述或引用的代码组件建立 `documents` 边
- 指向其他 `.md` 文件的链接在文档节点之间创建 `related` 边
- 代码块中提及的文件路径可能隐含指向这些文件的 `documents` 边
- 子目录中的 README 通常对该路径的模块建立 `documents` 边

## 摘要风格

> "项目概览文档：N 个章节，覆盖安装、使用与 API 参考。"
> "架构决策记录：记录为 [purpose] 选择 [technology] 的决策。"
> "贡献指南：代码风格规则、测试要求与 PR 流程。"
