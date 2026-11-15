> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/frameworks/fastapi.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# FastAPI 框架补充说明

> 检测到 FastAPI 时，将本文件注入 file-analyzer 与 architecture-analyzer 的提示词。
> 请勿单独作为提示词使用：必须始终附加在基础提示词模板之后。

## FastAPI 项目结构

分析 FastAPI 项目时，在基础分析规则之上应用以下附加约定。

### 规范文件角色

| 文件 / 模式 | 角色 | 标签 |
|---|---|---|
| `main.py`, `app.py` | 应用工厂：创建并配置 `FastAPI()` 实例 | `entry-point`, `config` |
| `*/routers/*.py`, `*/api/*.py` | `APIRouter` 模块：按领域分组相关端点 | `api-handler`, `routing` |
| `*/schemas.py`, `*/schemas/*.py` | Pydantic 请求/响应模型 | `type-definition`, `serialization` |
| `*/models.py`, `*/models/*.py` | SQLAlchemy ORM 模型或其他数据库模型 | `data-model` |
| `*/dependencies.py`, `*/deps.py` | `Depends()` 提供者函数：注入路由的共享逻辑 | `service`, `middleware` |
| `*/crud.py`, `*/repository.py` | 数据访问层：CRUD 操作 | `data-model`, `service` |
| `*/database.py`, `*/db.py` | 数据库引擎、会话工厂、连接管理 | `config`, `data-model` |
| `*/config.py`, `*/settings.py` | `pydantic-settings` / `BaseSettings` 配置类 | `config` |
| `*/middleware.py` | Starlette 中间件类 | `middleware` |
| `*/exceptions.py` | 自定义异常类与异常处理器 | `utility` |
| `*/security.py`, `*/auth.py` | 认证工具：JWT 解码、密码哈希、OAuth 辅助 | `service`, `middleware` |
| `*/tasks.py` | 后台任务或 Celery 任务定义 | `service`, `event-handler` |
| `*/tests/*.py`, `test_*.py` | pytest 测试文件 | `test` |
| `conftest.py` | pytest fixture 与测试配置 | `test`, `config` |

### 需要关注的边模式

**路由挂载链**：当 `main.py` 或路由聚合处出现 `app.include_router(some_router, prefix="/api")` 时，从主应用文件到每个路由模块创建 `imports` + `depends_on` 边。由此构建 URL 层级图。

**依赖注入树**：当路由函数或另一个 `Depends()` 提供者导入并调用 `Depends(some_function)` 时，从调用方到依赖提供者创建 `depends_on` 边。追踪这些链：它们常跨多个文件（如 路由 → 认证依赖 → 数据库会话依赖）。

**Pydantic 模型继承**：当一个 schema 类继承另一个（如 `class UserCreate(UserBase)`）时，在 schema 类节点之间创建 `inherits` 边。

**ORM 模型关系**：当 SQLAlchemy 模型使用 `relationship()`、`ForeignKey` 时，在模型类之间创建 `depends_on` 边。

**CRUD 与模型绑定**：当 `crud.py` 函数以模型类型为参数或直接引用模型类时，从 CRUD 文件到模型文件创建 `depends_on` 边。

### FastAPI 的架构分层

| 层 ID | 层名称 | 包含内容 |
|---|---|---|
| `layer:api` | API 层 | 路由文件、带 `@router.get/post/...` 装饰器的端点函数 |
| `layer:types` | 类型层 | Pydantic schema 文件、请求/响应模型 |
| `layer:service` | 服务层 | `dependencies.py`、`crud.py`、业务逻辑模块 |
| `layer:data` | 数据层 | ORM 模型、`database.py`、迁移 |
| `layer:config` | 配置层 | `main.py` / `app.py` 工厂、`settings.py`、`config.py` |
| `layer:middleware` | 中间件层 | `middleware.py`、`security.py`、`auth.py`、异常处理器 |
| `layer:test` | 测试层 | `tests/`、`conftest.py` |

### 需记录到 languageLesson 的重点模式

- **依赖注入即组合**：FastAPI 的 `Depends()` 是一等公民的 DI 系统：路由可声明任意数量的依赖，每个依赖又可有各自的依赖，形成请求时才解析的树
- **用 Pydantic 做校验**：请求体、查询参数与路径参数由 Pydantic 自动校验，无效输入在你的代码运行前就抛出 `422 Unprocessable Entity`
- **异步端点**：`async def` 路由跑在事件循环里，`def` 路由跑在线程池里，混用不当会造成性能问题
- **路径操作顺序**：FastAPI 按声明顺序匹配路由，通配路由若放在具体路由之前会遮蔽后者
