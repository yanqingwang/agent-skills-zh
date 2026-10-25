---
name: spec-to-repo
description: "当用户说 'build me an app'（帮我做个应用）、'create a project from this spec'（按这份规格创建项目）、'scaffold a new repo'（搭建一个新仓库）、'generate a starter'（生成一个起始项目）、'turn this idea into code'（把这个想法变成代码）、'bootstrap a project'（初始化一个项目）、'I have requirements and need a codebase'（我有一份需求，需要一套代码库），或提供自然语言项目规格并期望得到完整、可运行的仓库时使用。与技术栈无关：Next.js、FastAPI、Rails、Go、Rust、Flutter 等。"
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`product-team/skills/spec-to-repo/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 规格转仓库（Spec to Repo）

将一份自然语言项目规格转化为完整、可运行的起始仓库。不是模板填充器——而是一台规格解释器，可为任意技术栈生成真实、可运行的代码。

## 何时使用

- 用户提供了应用的文字描述，并希望得到代码
- 用户手头有 PRD、需求文档或功能清单，需要一套代码库
- 用户说"build me an app that..."（帮我做个能……的应用）、"scaffold this"（把这个搭起来）、"bootstrap a project"（初始化一个项目）
- 用户想要的是一个能跑起来的起始仓库，而不只是一份文件树

**不适用本 Skill** 的情形：用户明确想要带 Stripe + Auth 的 SaaS 应用——请改用 `product-team/saas-scaffolder`。

## 核心工作流

### 阶段 1 — 解析与理解

通读规格。静默提取以下字段：

| 字段 | 来源 | 是否必需 |
|-------|--------|----------|
| 应用名称 | 显式给出，或从描述推断 | 是 |
| 描述 | 规格的第一句话 | 是 |
| 功能 | 描述行为的要点或句子 | 是 |
| 技术栈 | 显式指定（"use FastAPI"），或从上下文推断 | 是 |
| 认证 | "login"、"users"、"accounts"、"roles" | 如提及 |
| 数据库 | "store"、"save"、"persist"、"records"、"schema" | 如提及 |
| API 面 | "endpoint"、"API"、"REST"、"GraphQL" | 如提及 |
| 部署目标 | "Vercel"、"Docker"、"AWS"、"Railway" | 如提及 |

**技术栈推断规则**（当用户未指定时）：

| 信号 | 推断的技术栈 |
|--------|---------------|
| "web app"、"dashboard"、"SaaS" | Next.js + TypeScript |
| "API"、"backend"、"microservice" | FastAPI（Python）或 Express（Node） |
| "mobile app" | Flutter 或 React Native |
| "CLI tool" | Go 或 Python |
| "data pipeline" | Python |
| "high performance"、"systems" | Rust 或 Go |

解析完成后，向用户回呈一份结构化的理解结果：

```
## Spec Interpretation

**App:** [name]
**Stack:** [framework + language]
**Features:**
1. [feature]
2. [feature]

**Database:** [yes/no — engine]
**Auth:** [yes/no — method]
**Deploy:** [target]

Does this match your intent? Any corrections before I generate?
```

标记出含糊之处。澄清提问**至多 3 个**。如果用户说"直接做就行"，则按最佳猜测的默认值继续。

### 阶段 2 — 架构设计

在写任何文件之前先做好设计：

1. **选择模板** — 匹配 `references/stack-templates.md` 中对应技术栈的模板
2. **定义文件树** — 列出将要创建的每一个文件
3. **功能映射到文件** — 每个功能至少对应一个文件/组件
4. **设计数据库模式** — 如适用，定义表/集合及其字段与类型
5. **确定依赖** — 列出每个包及其版本约束
6. **规划 API 路由** — 如适用，列出每个端点的方法、路径、请求/响应结构

在生成之前把文件树呈给用户确认：

```
project-name/
├── README.md
├── .env.example
├── .gitignore
├── .github/workflows/ci.yml
├── package.json / requirements.txt / go.mod
├── src/
│   ├── ...
├── tests/
│   ├── ...
└── ...
```

### 阶段 3 — 生成

写出每一个文件。规则：

- **真实代码，而非占位符。** 每个函数都要有真实实现。不允许 `// TODO: implement` 或 `pass` 之类的占位。
- **语法有效。** 每个文件都必须能在其语言下无错误地通过解析。
- **导入与依赖一致。** 每条 import 都必须对应清单文件（package.json、requirements.txt、go.mod 等）中的一个包。
- **包含类型。** TypeScript 项目使用类型；Python 项目使用类型注解；Go 项目使用带类型的结构体。
- **环境变量。** 生成 `.env.example`，收录每个必需变量，并注释其用途。
- **README.md。** 包含：项目描述、前置条件、搭建步骤（克隆、安装、配置环境变量、运行），以及可用的脚本/命令。
- **CI 配置。** 生成 `.github/workflows/ci.yml`，包含：install、lint（若依赖中有 linter）、test、build。
- **.gitignore。** 按技术栈给出合适的忽略项（node_modules、__pycache__、.env、构建产物）。

**文件生成顺序：**
1. 清单文件（package.json / requirements.txt / go.mod）
2. 配置文件（.env.example、.gitignore、CI）
3. 数据库模式 / 迁移
4. 核心业务逻辑
5. API 路由 / 端点
6. UI 组件（如适用）
7. 测试
8. README.md

### 阶段 4 — 验证

生成之后，逐项过一遍这份清单：

- [ ] 每个被导入的包都存在于清单中
- [ ] 每个被 import 引用的文件都存在于文件树中
- [ ] `.env.example` 列出了代码中用到的每一个环境变量
- [ ] `.gitignore` 覆盖了构建产物与机密信息
- [ ] README 中的搭建说明真实可用
- [ ] 没有硬编码的机密、API key 或密码
- [ ] 至少存在一个测试文件
- [ ] 构建/启动命令已写入文档且确实可行

对生成的目录运行 `scripts/validate_project.py`，以捕获常见问题。

## 示例

### 示例 1：任务管理 API

**输入规格：**
> "帮我做一个任务管理 API。用户可以创建、列出、更新和删除任务。任务有标题、描述、状态（todo/in-progress/done）和截止日期。用 FastAPI 加 SQLite。加上基于 API key 的基本认证。"

**输出文件树：**
```
task-api/
├── README.md
├── .env.example              # API_KEY, DATABASE_URL
├── .gitignore
├── .github/workflows/ci.yml
├── requirements.txt          # fastapi, uvicorn, sqlalchemy, pytest
├── main.py                   # FastAPI app, CORS, lifespan
├── models.py                 # SQLAlchemy Task model
├── schemas.py                # Pydantic request/response schemas
├── database.py               # SQLite engine + session
├── auth.py                   # API key middleware
├── routers/
│   └── tasks.py              # CRUD endpoints
└── tests/
    └── test_tasks.py         # Smoke tests for each endpoint
```

### 示例 2：食谱分享 Web 应用

**输入规格：**
> "我想要一个食谱分享网站。用户可以注册、发布带食材和步骤的食谱、浏览他人的食谱并收藏喜欢的。用 Next.js 加 Tailwind。数据存 PostgreSQL。"

**输出文件树：**
```
recipe-share/
├── README.md
├── .env.example              # DATABASE_URL, NEXTAUTH_SECRET, NEXTAUTH_URL
├── .gitignore
├── .github/workflows/ci.yml
├── package.json              # next, react, tailwindcss, prisma, next-auth
├── tailwind.config.ts
├── tsconfig.json
├── next.config.ts
├── prisma/
│   └── schema.prisma         # User, Recipe, Ingredient, Favorite models
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx          # Homepage — recipe feed
│   │   ├── recipes/
│   │   │   ├── page.tsx      # Browse recipes
│   │   │   ├── [id]/page.tsx # Recipe detail
│   │   │   └── new/page.tsx  # Create recipe form
│   │   └── api/
│   │       ├── auth/[...nextauth]/route.ts
│   │       └── recipes/route.ts
│   ├── components/
│   │   ├── RecipeCard.tsx
│   │   ├── RecipeForm.tsx
│   │   └── Navbar.tsx
│   └── lib/
│       ├── prisma.ts
│       └── auth.ts
└── tests/
    └── recipes.test.ts
```

### 示例 3：CLI 记账工具

**输入规格：**
> "一个用 Python 写的记账 CLI 工具。命令：add、list、summary、export-csv。数据存本地 SQLite 文件。不调用外部 API。"

**输出文件树：**
```
expense-tracker/
├── README.md
├── .gitignore
├── .github/workflows/ci.yml
├── pyproject.toml
├── src/
│   └── expense_tracker/
│       ├── __init__.py
│       ├── cli.py            # argparse commands
│       ├── database.py       # SQLite operations
│       ├── models.py         # Expense dataclass
│       └── formatters.py     # Table + CSV output
└── tests/
    └── test_cli.py
```

## 反模式

| 反模式 | 修复方式 |
|---|---|
| **占位符代码** — `// TODO: implement`、`pass`、空的函数体 | 每个函数都要有真实实现。如果逻辑复杂，就实现一个可用的简化版本。 |
| **强行改技术栈** — 用户明明说了 Flask，你却选了 Next.js | 始终尊重显式给出的技术偏好。只在用户未指定时才做推断。 |
| **缺失 .gitignore** — 把 node_modules 或 .env 提交进仓库 | 把符合技术栈的 .gitignore 作为最早生成的文件之一。 |
| **幽灵导入** — 导入了清单中不存在的包 | 收尾前把每条 import 与 package.json / requirements.txt 交叉核对。 |
| **MVP 过度工程** — 给 v1 加上 Redis 缓存、限流、WebSocket | 先构建能跑通的最小实现。用户可以再迭代。 |
| **无视明确偏好** — 用户说 "PostgreSQL"，你却生成了 MongoDB | 仔细解析规格。显式偏好不容商量。 |
| **遗漏环境变量** — 代码读取 `process.env.X`，但 `.env.example` 里没有列出 | 代码中用到的每个环境变量都必须出现在 `.env.example` 中并附注释。 |
| **没有测试** — 交付一个零测试文件的仓库 | 至少做到：每个 API 端点一个冒烟测试，或每个核心函数一个测试。 |
| **臆造 API** — 生成的代码调用了并不存在的库方法 | 只用文档完善、稳定的 API。拿不准时，选最简单的做法。 |

## 验证脚本

### `scripts/validate_project.py`

检查生成的项目目录中的常见问题：

```bash
# Validate a generated project
python3 scripts/validate_project.py /path/to/generated-project

# JSON output
python3 scripts/validate_project.py /path/to/generated-project --format json
```

执行的检查项：
- README.md 存在且非空
- .gitignore 存在
- .env.example 存在（若代码引用了环境变量）
- 包清单文件存在（package.json、requirements.txt、go.mod、Cargo.toml、pubspec.yaml）
- 没有提交 .env 文件（机密泄漏）
- 至少存在一个测试文件
- 生成的代码中没有 TODO/FIXME 占位符

## 渐进增强

对于复杂的规格，分阶段生成：

1. **MVP** — 只做核心功能，端到端可运行
2. **认证** — 如有要求，加入身份认证
3. **打磨** — 错误处理、校验、加载状态
4. **部署** — Docker、CI、部署配置

MVP 完成后询问用户："核心功能已经能跑了。接下来要我加认证/打磨/部署，还是先在现有基础上迭代？"

## 交叉引用

- 相关：`product-team/saas-scaffolder` — 面向 SaaS 的脚手架（Next.js + Stripe + Auth）
- 相关：`engineering/spec-driven-workflow` — 规格先行的开发方法论
- 相关：`engineering/database-designer` — 数据库模式设计模式
- 相关：`engineering-team/senior-fullstack` — 全栈实现模式
