> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`product-team/skills/spec-to-repo/references/spec-parsing-guide.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 规格解析指南

如何从含糊、不完整或对话式的自然语言规格中提取结构化需求。

---

## 解析策略

先把规格完整读一遍。第二遍读时，把字段提取进结构化理解表。凡是能合理推断的内容，都不要发问。

### 提取优先级

1. **显式陈述**："Use PostgreSQL"、"Build with Next.js"，不容商量
2. **强信号**："users can sign up" 意味着认证 + 用户模型 + 数据库
3. **上下文推断**："dashboard" 意味着 Web 应用；"track expenses" 意味着 CRUD + 数据库
4. **默认值**：什么都没指定时，选该领域最常见的选项

---

## 歧义消解

### 未指定技术栈

| 规格模式 | 默认技术栈 | 理由 |
|---|---|---|
| 带界面的 Web 应用 | Next.js + TypeScript | 最通用，SSR + API 路由 |
| 仅 API / 后端 | FastAPI | 脚手架搭建快，DX 好，带类型 |
| 移动应用 | Flutter | 跨平台，单一代码库 |
| CLI 工具 | Python | 发布上线最快，标准库丰富 |
| "Simple" / "lightweight" | Express 或 Flask | 开销最小 |
| "Fast" / "performance" | Go | 编译型，并发友好 |

### 未指定数据库

| 信号 | 默认 |
|---|---|
| 用户账户、持久化数据 | PostgreSQL |
| 小项目、仅本地、CLI | SQLite |
| 文档导向、模式灵活 | MongoDB（仅当用户有相关信号时） |
| 未提到数据持久化 | 不加数据库，不要擅自添加 |

### 未指定认证

| 信号 | 默认 |
|---|---|
| "Users"、"accounts"、"login" | 需要，基于 session 或 JWT |
| "Admin panel"、"roles" | 需要，带基于角色的访问控制 |
| 带 "API keys" 的 API | 需要，用 API key 中间件 |
| 没有面向用户的功能 | 不加认证，不要擅自添加 |

---

## 常见规格形态

### 形态 1：意识流

> "我想要一个应用，大家能在上面发布食谱，其他人可以评论、收藏喜欢的，或许再加个评分系统，而且在手机上看起来要漂亮"

**提取结果：**
- 功能：发布食谱、评论、收藏、评分
- 界面：响应式 / 移动端友好
- 隐含：认证（有用户）、数据库（食谱、评论、收藏、评分）、Web 应用

### 形态 2：功能清单

> "功能：1. 用户注册 2. 创建项目 3. 邀请团队成员 4. 看板 5. 文件上传"

**提取结果：**
- 功能：编号清单，每项各得一个路由/组件
- 认证：需要（有注册）
- 数据库：需要（用户、项目、团队、文件）
- 复杂功能：看板（拖拽）、文件上传（存储）

### 形态 3：技术规格

> "FastAPI 后端加 PostgreSQL。端点：POST /items、GET /items、GET /items/{id}、PUT /items/{id}、DELETE /items/{id}。使用 SQLAlchemy ORM。加 JWT 认证。"

**提取结果：**
- 技术栈：显式给出（FastAPI、PostgreSQL、SQLAlchemy、JWT）
- API：5 个 CRUD 端点，定义完整
- 几乎无需推断，要求什么就生成什么

### 形态 4：现成 PRD

> [一份多页文档，包含概述、用户画像、功能需求、验收标准]

**提取结果：**
- 先读概述，把握范围
- 把功能需求映射到文件
- 把验收标准当作测试用例的种子
- 忽略用户画像、市场分析、时间表，它们不影响代码生成

---

## 哪些要问，哪些可推断

**要问的（至多 3 个问题）：**
- 技术栈偏好：规格真正含糊、多种选择都说得通时
- 数据库选型：SQL 和 NoSQL 都同样可行时
- 部署目标：会实质影响代码时（serverless 还是容器）

**静默推断：**
- 认证方式（API 用 JWT，Web 应用用 session）
- 测试框架（该技术栈最流行的那个）
- linter / 格式化工具（技术栈默认）
- CSS 方案（React/Next 用 Tailwind，其余用技术栈默认）
- 包版本（最新稳定版）

**永远不要问：**
- "你想要什么样的目录结构？"：不用问，按技术栈惯例来
- "要用 TypeScript 吗？"：要，JS 项目一律用
- "要加错误处理吗？"：要，一律加
- "要写测试吗？"：要，一律写
