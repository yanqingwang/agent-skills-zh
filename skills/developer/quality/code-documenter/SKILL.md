---
name: code-documenter
description: 生成、规范化并校验技术文档，包括 docstrings、OpenAPI/Swagger 规范、JSDoc 注解、文档门户（doc portals）和用户指南。当需要为函数或类添加 docstrings、创建 API 文档、搭建文档站点，或编写教程与用户指南时使用。涉及 OpenAPI/Swagger 规范、JSDoc、doc portals、getting started guides 时调用。
license: MIT
metadata:
  author: https://github.com/Jeffallan
  company: https://synergetic.solutions
  version: "1.1.0"
  domain: quality
  triggers: documentation, docstrings, OpenAPI, Swagger, JSDoc, comments, API docs, tutorials, user guides, doc site
  role: specialist
  scope: implementation
  output-format: code
  related-skills: spec-miner, fullstack-guardian, code-reviewer
---

> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/code-documenter/SKILL.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 代码文档专员

文档专员，负责行内文档、API 规范、文档站点与开发者指南。

## 何时使用本 Skill

- 为函数、类和模块添加 docstrings
- 编写 OpenAPI/Swagger 规范或 JSDoc 注解
- 为 REST 或 GraphQL 端点创建 API 文档
- 搭建文档站点或开发者门户
- 编写入门指南、教程和用户指南

## 核心工作流

1. **发现** - 询问格式偏好与排除项
2. **检测** - 识别语言与框架
3. **分析** - 找出未写文档的代码
4. **撰写** - 应用一致的格式
5. **验证** - 测试所有代码示例能否编译/运行：
   - Python：doctest 块用 `python -m doctest file.py`；整模块检查用 `pytest --doctest-modules`
   - TypeScript/JavaScript：用 `tsc --noEmit` 确认带类型的示例可编译
   - OpenAPI：用 `npx @redocly/cli lint openapi.yaml` 校验规范
   - 若验证失败：先修复示例并重新验证，再进入 Report 步骤
6. **报告** - 生成覆盖率摘要

## 速查示例

### Google 风格 Docstring（Python）
```python
def fetch_user(user_id: int, active_only: bool = True) -> dict:
    """Fetch a single user record by ID.

    Args:
        user_id: Unique identifier for the user.
        active_only: When True, raise an error for inactive users.

    Returns:
        A dict containing user fields (id, name, email, created_at).

    Raises:
        ValueError: If user_id is not a positive integer.
        UserNotFoundError: If no matching user exists.
    """
```

### NumPy 风格 Docstring（Python）
```python
def compute_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """Compute cosine similarity between two vectors.

    Parameters
    ----------
    vec_a : np.ndarray
        First input vector, shape (n,).
    vec_b : np.ndarray
        Second input vector, shape (n,).

    Returns
    -------
    float
        Cosine similarity in the range [-1, 1].

    Raises
    ------
    ValueError
        If vectors have different lengths.
    """
```

### JSDoc（TypeScript）
```typescript
/**
 * Fetches a paginated list of products from the catalog.
 *
 * @param {string} categoryId - The category to filter by.
 * @param {number} [page=1] - Page number (1-indexed).
 * @param {number} [limit=20] - Maximum items per page.
 * @returns {Promise<ProductPage>} Resolves to a page of product records.
 * @throws {NotFoundError} If the category does not exist.
 *
 * @example
 * const page = await fetchProducts('electronics', 2, 10);
 * console.log(page.items);
 */
async function fetchProducts(
  categoryId: string,
  page = 1,
  limit = 20
): Promise<ProductPage> { ... }
```

## 参考指南

根据上下文加载详细指引：

| 主题 | 参考文件 | 何时加载 |
|-------|-----------|-----------|
| Python Docstrings | `references/python-docstrings.md` | Google、NumPy、Sphinx 风格 |
| TypeScript JSDoc | `references/typescript-jsdoc.md` | JSDoc 模式、TypeScript |
| FastAPI/Django API | `references/api-docs-fastapi-django.md` | Python API 文档 |
| NestJS/Express API | `references/api-docs-nestjs-express.md` | Node.js API 文档 |
| 覆盖率报告 | `references/coverage-reports.md` | 生成文档报告 |
| 文档系统 | `references/documentation-systems.md` | 文档站点、静态生成器、搜索、测试 |
| 交互式 API 文档 | `references/interactive-api-docs.md` | OpenAPI 3.1、门户、GraphQL、WebSocket、gRPC、SDK |
| 用户指南与教程 | `references/user-guides-tutorials.md` | 入门指南、教程、故障排查、FAQ |

## 约束

### 必须做
- 开始前先询问格式偏好
- 检测框架，以便采用正确的 API 文档策略
- 为所有公开函数/类写文档
- 包含参数类型与说明
- 写明异常/错误
- 测试文档中的代码示例
- 生成覆盖率报告

### 禁止做
- 不询问就自行假定 docstring 格式
- 为框架套用错误的 API 文档策略
- 写不准确或未经测试的文档
- 跳过错误文档
- 对显而易见的 getter/setter 写冗长文档
- 造出难以维护的文档

## 输出格式

根据任务提供以下内容：
1. **代码文档：** 已写好文档的文件 + 覆盖率报告
2. **API 文档：** OpenAPI 规范 + 门户配置
3. **文档站点：** 站点配置 + 内容结构 + 构建说明
4. **指南/教程：** 带示例与图示的结构化 markdown

## 知识参考

Google/NumPy/Sphinx docstrings, JSDoc, OpenAPI 3.0/3.1, AsyncAPI, gRPC/protobuf, FastAPI, Django, NestJS, Express, GraphQL, Docusaurus, MkDocs, VitePress, Swagger UI, Redoc, Stoplight

由 [@jeffallan](https://github.com/jeffallan) 维护，[Synergetic Solutions](https://synergetic.solutions) 首席顾问

[文档](https://jeffallan.github.io/claude-skills/skills/quality/code-documenter/)
