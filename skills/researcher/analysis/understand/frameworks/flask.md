> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/frameworks/flask.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Flask 框架补充说明

> 检测到 Flask 时，将本文件注入 file-analyzer 与 architecture-analyzer 的提示词。
> 请勿单独作为提示词使用：必须始终附加在基础提示词模板之后。

## Flask 项目结构

分析 Flask 项目时，在基础分析规则之上应用以下附加约定。

### 规范文件角色

| 文件 / 模式 | 角色 | 标签 |
|---|---|---|
| `app.py`, `__init__.py`（应用包内） | 应用工厂（`create_app()`）或直接的 `Flask(__name__)` 实例 | `entry-point`, `config` |
| `run.py`, `wsgi.py` | 生产/开发服务器入口 | `entry-point`, `config` |
| `*/views.py`, `*/routes.py` | 带 `@app.route` 或 `@blueprint.route` 的路由处理函数 | `api-handler`, `routing` |
| `*/blueprints/*.py`, `*/api/*.py` | Blueprint 模块：按功能分组路由 | `api-handler`, `routing` |
| `*/models.py` | SQLAlchemy 模型或其他 ORM 模型 | `data-model` |
| `*/forms.py` | WTForms 表单类 | `validation`, `ui` |
| `*/schemas.py` | Marshmallow 序列化 schema | `serialization`, `type-definition` |
| `*/config.py` | 配置类（`DevelopmentConfig`、`ProductionConfig`） | `config` |
| `*/extensions.py` | Flask 扩展初始化（`db = SQLAlchemy()`、`login_manager = LoginManager()`） | `config`, `singleton` |
| `*/decorators.py` | 自定义路由装饰器（认证守卫、限流） | `middleware`, `utility` |
| `*/utils.py`, `*/helpers.py` | 共享工具函数 | `utility` |
| `*/templates/**/*.html` | Jinja2 模板 | `ui` |
| `*/static/` | CSS、JS 与静态资源文件 | `assets` |
| `*/tests/*.py`, `test_*.py` | pytest 或 unittest 测试文件 | `test` |

### 需要关注的边模式

**Blueprint 注册**：当应用工厂中出现 `app.register_blueprint(bp, url_prefix='/api')` 时，从应用工厂到每个 Blueprint 模块创建 `depends_on` 边。

**扩展耦合**：当视图从 `extensions.py` 导入（如 `from .extensions import db, login_manager`）时，创建 `imports` 边，标明哪些视图依赖哪些扩展。

**请求前/后钩子**：当 `@app.before_request` 或 `@blueprint.before_request` 装饰某个函数时，从这些函数到其挂载的应用/Blueprint 创建 `middleware` 边。

### Flask 的架构分层

| 层 ID | 层名称 | 包含内容 |
|---|---|---|
| `layer:api` | API 层 | Blueprint 路由文件、视图函数 |
| `layer:data` | 数据层 | `models.py`、数据库迁移文件 |
| `layer:service` | 服务层 | 业务逻辑模块、`schemas.py`、服务类 |
| `layer:ui` | UI 层 | `templates/`、`forms.py`、`static/` |
| `layer:config` | 配置层 | `app.py` 工厂、`config.py`、`extensions.py` |
| `layer:middleware` | 中间件层 | `decorators.py`、请求前/后钩子 |
| `layer:test` | 测试层 | 测试文件、`conftest.py` |

### 需记录到 languageLesson 的重点模式

- **应用工厂模式**：`create_app()` 函数支持多个应用实例（如测试用），并延迟扩展初始化，避免循环导入
- **Blueprint 模块化**：Blueprint 把相关路由、模板与静态文件分组，以 URL 前缀注册到应用，可独立测试
- **Flask 扩展协议**：扩展遵循 `init_app(app)` 做延迟初始化：扩展对象全局创建，之后再绑定到具体应用实例
