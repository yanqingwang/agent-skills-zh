> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/json.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# JSON 语言提示词片段

## 核心概念

- **严格语法**：不允许尾逗号、不允许注释（JSONC、JSON5 除外），字符串必须双引号
- **数据类型**：对象、数组、字符串、数字、布尔与 null，没有 undefined 或日期类型
- **嵌套结构**：任意嵌套深度，用于层级化配置或数据
- **Schema 校验**：JSON Schema（`$schema` 关键字）校验结构与类型
- **JSONC**：带注释的 JSON 变体，VS Code、tsconfig.json 等工具使用
- **JSON5**：扩展 JSON，允许注释、尾逗号、不带引号的键等
- **JSON Lines**（`.jsonl`）：每行一个 JSON 对象，面向流式数据处理

## 重要文件模式

- `package.json`：Node.js 项目清单，含依赖、脚本与元数据
- `tsconfig.json`：TypeScript 编译器配置（实为 JSONC）
- `.eslintrc.json`：ESLint 规则与配置
- `*.schema.json`：用于校验的 JSON Schema 定义
- `composer.json`：PHP Composer 项目清单
- `appsettings.json`：.NET 应用配置
- `manifest.json`：浏览器扩展或 PWA 清单

## 边模式

- `package.json` 对构建工具链建立 `configures` 边，并定义项目依赖
- `tsconfig.json` 对所有 `.ts` 文件的 TypeScript 编译建立 `configures` 边
- JSON Schema 文件为 API 请求/响应校验建立 `defines_schema` 边
- 配置 JSON 文件对应用运行时行为建立 `configures` 边

## 摘要风格

> "Node.js 项目清单：定义 N 个依赖、构建脚本与项目元数据。"
> "TypeScript 编译器配置：启用严格模式，并为 monorepo 包配置路径别名。"
> "JSON Schema：定义用户 API 端点的请求/响应结构。"
