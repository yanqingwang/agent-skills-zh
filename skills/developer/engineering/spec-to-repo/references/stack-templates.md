> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`product-team/skills/spec-to-repo/references/stack-templates.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 技术栈模板

常见技术栈的速查模板。每个模板定义：文件结构、清单文件、入口点，以及构建/运行命令。

---

## Next.js（TypeScript + Tailwind）

**适用场景：** Web 应用、仪表盘、SaaS、带动态内容的落地页。

**清单文件：** `package.json`
```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "jest"
  }
}
```

**核心依赖：** `next`、`react`、`react-dom`、`tailwindcss`、`postcss`、`autoprefixer`
**认证：** `next-auth`（默认）或 `clerk`
**数据库：** `prisma`（ORM）+ `@prisma/client`
**测试：** `jest`、`@testing-library/react`

**文件结构：**
```
src/app/layout.tsx        — Root layout with providers
src/app/page.tsx          — Homepage
src/app/api/*/route.ts    — API routes
src/components/*.tsx       — Shared components
src/lib/*.ts              — Utilities, DB client
prisma/schema.prisma      — Database schema (if DB)
```

**配置文件：** `tsconfig.json`、`tailwind.config.ts`、`next.config.ts`、`postcss.config.mjs`

---

## FastAPI（Python）

**适用场景：** REST API、后端、微服务、数据驱动的服务。

**清单文件：** `requirements.txt`
```
fastapi>=0.110.0
uvicorn>=0.29.0
sqlalchemy>=2.0.0
pydantic>=2.0.0
pytest>=8.0.0
httpx>=0.27.0
```

**文件结构：**
```
main.py                   — FastAPI app, CORS, lifespan
models.py                 — SQLAlchemy models
schemas.py                — Pydantic schemas
database.py               — Engine, session factory
routers/*.py              — Route modules
tests/test_*.py           — pytest tests
```

**运行：** `uvicorn main:app --reload`
**测试：** `pytest`

---

## Express（TypeScript）

**适用场景：** Node.js API、重中间件的后端、实时服务。

**清单文件：** `package.json`
```json
{
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js",
    "test": "jest"
  }
}
```

**核心依赖：** `express`、`cors`、`dotenv`
**开发依赖：** `typescript`、`tsx`、`@types/express`、`@types/node`、`jest`、`ts-jest`

**文件结构：**
```
src/index.ts              — App setup, middleware, listen
src/routes/*.ts           — Route handlers
src/middleware/*.ts        — Auth, validation, error handling
src/models/*.ts           — Data models / ORM entities
src/lib/*.ts              — Utilities
tests/*.test.ts           — Jest tests
```

---

## Go（net/http 或 Gin）

**适用场景：** 高性能 API、CLI 工具、系统编程。

**清单文件：** `go.mod`

**文件结构（API）：**
```
main.go                   — Entry point, router setup
handlers/*.go             — HTTP handlers
models/*.go               — Data structs
middleware/*.go            — Auth, logging
db/*.go                   — Database connection
*_test.go                 — Table-driven tests
```

**文件结构（CLI）：**
```
main.go                   — Entry point, flag parsing
cmd/*.go                  — Subcommands
internal/*.go             — Business logic
*_test.go                 — Tests
```

**运行：** `go run .`
**测试：** `go test ./...`
**构建：** `go build -o app .`

---

## Rust（Actix-web 或 Axum）

**适用场景：** 高性能、安全攸关的 API 与系统。

**清单文件：** `Cargo.toml`

**文件结构：**
```
src/main.rs               — Entry point, server setup
src/routes/*.rs           — Route handlers
src/models/*.rs           — Data structs, serde
src/db.rs                 — Database pool
src/error.rs              — Error types
tests/*.rs                — Integration tests
```

**运行：** `cargo run`
**测试：** `cargo test`

---

## Flutter（Dart）

**适用场景：** 跨平台移动应用（iOS + Android）。

**清单文件：** `pubspec.yaml`

**文件结构：**
```
lib/main.dart             — Entry point, MaterialApp
lib/screens/*.dart        — Screen widgets
lib/widgets/*.dart        — Reusable components
lib/models/*.dart         — Data classes
lib/services/*.dart       — API clients, storage
lib/providers/*.dart      — State management
test/*_test.dart          — Widget tests
```

**运行：** `flutter run`
**测试：** `flutter test`

---

## Rails（Ruby）

**适用场景：** 全栈 Web 应用、以 CRUD 为主的应用、快速原型。

**清单文件：** `Gemfile`

**文件结构：** 标准 Rails 惯例（`app/`、`config/`、`db/`、`spec/`）。

**运行：** `bin/rails server`
**测试：** `bin/rspec`

---

## Django（Python）

**适用场景：** Python 全栈 Web 应用、重后台管理的应用、内容管理。

**清单文件：** `requirements.txt`
```
django>=5.0
djangorestframework>=3.15
pytest-django>=4.8
```

**文件结构：**
```
manage.py
config/settings.py        — Settings
config/urls.py            — Root URL config
apps/<name>/models.py     — Models
apps/<name>/views.py      — Views or ViewSets
apps/<name>/serializers.py — DRF serializers
apps/<name>/urls.py       — App URL config
tests/test_*.py
```

**运行：** `python manage.py runserver`
**测试：** `pytest`

---

## CI 模板（.github/workflows/ci.yml）

按技术栈自行调整：

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup [runtime]
        uses: actions/setup-[runtime]@v5
        with:
          [runtime]-version: '[version]'
      - name: Install
        run: [install command]
      - name: Lint
        run: [lint command]
      - name: Test
        run: [test command]
      - name: Build
        run: [build command]
```

---

## 各技术栈的 .gitignore 要点

| 技术栈 | 必须忽略 |
|-------|------------|
| Node/Next.js | `node_modules/`、`.next/`、`.env`、`dist/`、`.turbo/` |
| Python | `__pycache__/`、`*.pyc`、`.venv/`、`.env`、`*.egg-info/` |
| Go | 二进制文件名、`.env`、`vendor/`（若不提交进仓库） |
| Rust | `target/`、`.env` |
| Flutter | `.dart_tool/`、`build/`、`.env`、`*.iml` |
| Rails | `log/`、`tmp/`、`.env`、`storage/`、`node_modules/` |

所有技术栈通用：`.env`、`.DS_Store`、`*.log`、IDE 目录（`.idea/`、`.vscode/`）
