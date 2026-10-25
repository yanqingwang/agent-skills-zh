---
name: fastapi-templates
description: 创建生产可用的 FastAPI 项目，涵盖异步模式、依赖注入与完善的错误处理。在构建新的 FastAPI 应用或搭建后端 API 项目时使用。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/api-scaffolding/skills/fastapi-templates/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# FastAPI 项目模板

生产可用的 FastAPI 项目结构，涵盖异步模式、依赖注入、中间件，以及构建高性能 API 的最佳实践。

## 何时使用本 Skill

- 从零开始创建新的 FastAPI 项目
- 使用 Python 实现异步 REST API
- 构建高性能 Web 服务与微服务
- 创建基于 PostgreSQL、MongoDB 的异步应用
- 搭建结构合理、带测试的 API 项目

## 核心概念

### 1. 项目结构

**推荐布局：**

```
app/
├── api/                    # API routes
│   ├── v1/
│   │   ├── endpoints/
│   │   │   ├── users.py
│   │   │   ├── auth.py
│   │   │   └── items.py
│   │   └── router.py
│   └── dependencies.py     # Shared dependencies
├── core/                   # Core configuration
│   ├── config.py
│   ├── security.py
│   └── database.py
├── models/                 # Database models
│   ├── user.py
│   └── item.py
├── schemas/                # Pydantic schemas
│   ├── user.py
│   └── item.py
├── services/               # Business logic
│   ├── user_service.py
│   └── auth_service.py
├── repositories/           # Data access
│   ├── user_repository.py
│   └── item_repository.py
└── main.py                 # Application entry
```

### 2. 依赖注入

FastAPI 内置的 DI 系统，通过 `Depends` 使用：

- 数据库会话管理
- 认证/授权
- 共享业务逻辑
- 配置注入

### 3. 异步模式

正确的 async/await 用法：

- 异步路由处理器
- 异步数据库操作
- 异步后台任务
- 异步中间件

### 4. 依赖包

示例中导入的包：

```text
# requirements.txt
fastapi
uvicorn[standard]
pydantic-settings
sqlalchemy[asyncio]>=2.0  # DeclarativeBase; [asyncio] installs greenlet for the async engine
asyncpg                   # PostgreSQL driver: postgresql+asyncpg://...
PyJWT
pwdlib[argon2]
python-multipart          # only for a login route that uses OAuth2PasswordRequestForm

# requirements-dev.txt
pytest
pytest-asyncio
httpx
aiosqlite                 # test database: sqlite+aiosqlite:///:memory:
```

## 详细示例与模式

详细章节（以 `## Implementation Patterns` 开头）位于 `references/details.md`。当上面的导航概览不够用时，请阅读该文件。

## 测试

```python
# tests/conftest.py
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.core.database import get_db, Base

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

# Async fixtures need pytest_asyncio.fixture in pytest-asyncio's default strict mode
@pytest_asyncio.fixture
async def db_session():
    engine = create_async_engine(TEST_DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    AsyncSessionLocal = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    async with AsyncSessionLocal() as session:
        yield session
    await engine.dispose()

@pytest_asyncio.fixture
async def client(db_session):
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    # httpx 0.28 removed AsyncClient(app=...); use an ASGI transport
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
    app.dependency_overrides.clear()

# tests/test_users.py
import pytest

@pytest.mark.asyncio
async def test_create_user(client):
    response = await client.post(
        "/api/v1/users/",
        json={
            "email": "test@example.com",
            "password": "testpass123",
            "name": "Test User"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
```
