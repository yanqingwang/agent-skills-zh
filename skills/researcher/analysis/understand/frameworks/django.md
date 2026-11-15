> **中文汉化版** · 上游：[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) · 原文件：`understand-anything-plugin/skills/understand/frameworks/django.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Django 框架附录

> 检测到 Django 时注入 file-analyzer 与 architecture-analyzer 的提示词。
> 不要单独当提示词使用：始终附加在基础提示词模板之后。

## Django 项目结构

分析 Django 项目时，在基础分析规则之上应用以下附加约定。

### 规范文件角色

| 文件 / 模式 | 角色 | 标签 |
|---|---|---|
| `manage.py` | CLI 入口：开发服务器、迁移、管理命令 | `entry-point`, `config` |
| `*/settings.py`, `*/settings/*.py` | 项目级配置（数据库、已安装应用、中间件） | `config` |
| `*/urls.py` | URL 路由：把 URL 模式映射到视图 | `api-handler`, `routing` |
| `*/views.py`, `*/views/*.py` | 请求处理器（函数视图或类视图） | `api-handler`, `controller` |
| `*/models.py`, `*/models/*.py` | ORM 模型：映射到数据库表 | `data-model` |
| `*/serializers.py` | DRF 序列化器：模型与 JSON 互转 | `serialization`, `api-handler` |
| `*/forms.py` | Django 表单：校验与渲染逻辑 | `validation`, `ui` |
| `*/admin.py` | Admin 站点注册：把模型暴露在 Django admin 中 | `config` |
| `*/signals.py` | 信号处理器：模型事件上的横切副作用 | `event-handler` |
| `*/tasks.py` | Celery 异步任务定义 | `service`, `event-handler` |
| `*/middleware.py`, `*/middleware/*.py` | 请求/响应中间件类 | `middleware` |
| `*/permissions.py` | DRF 权限类 | `middleware`, `validation` |
| `*/filters.py` | DRF 过滤后端 | `utility` |
| `*/migrations/*.py` | 自动生成的 schema 迁移：不要单独总结 | `config` |
| `*/templates/**/*.html` | Django HTML 模板 | `ui` |
| `*/templatetags/*.py` | 自定义模板过滤器与标签 | `utility` |
| `*/management/commands/*.py` | 自定义管理命令（`./manage.py mycommand`） | `config`, `entry-point` |
| `wsgi.py`, `asgi.py` | WSGI/ASGI 服务器适配器：生产入口 | `config`, `entry-point` |
| `*/apps.py` | 应用配置与启动钩子（`AppConfig`） | `config` |
| `*/tests.py`, `*/tests/*.py` | 单元与集成测试 | `test` |

### 需要关注的边界模式

**URL 路由图**：当 `path()` 或 `re_path()` 把 URL 模式映射到视图函数或类时，
从 `urls.py` 节点到对应视图节点创建 `calls` 边。这些边表示 HTTP 路由链。

**信号接线**：当 `signals.py` 使用 `post_save.connect(handler, sender=Model)`
或 `@receiver(post_save, sender=Model)` 时，从信号处理函数到模型类创建
`subscribes` 边；再从模型到信号处理函数创建 `publishes` 边以表示触发方向。

**ORM 关系**：当 `models.py` 定义 `ForeignKey`、`OneToOneField` 或
`ManyToManyField` 时，在模型类之间创建 `depends_on` 边，并用描述注明
关系类型与基数。

**序列化器到模型的绑定**：当 DRF 序列化器的 `Meta` 类中含 `model = MyModel` 时，
从序列化器到模型创建 `depends_on` 边。

**视图到序列化器的绑定**：当 DRF ViewSet 或 APIView 引用某个序列化器类时，
从视图到序列化器创建 `depends_on` 边。

### Django 的架构分层

检测到时把节点归入以下层：

| 层 ID | 层名称 | 放入内容 |
|---|---|---|
| `layer:api` | API 层 | `views.py`, `serializers.py`, `urls.py`, DRF ViewSet 与 APIView |
| `layer:data` | 数据层 | `models.py`, `migrations/`, 数据库工具文件 |
| `layer:service` | 服务层 | `signals.py`, `tasks.py`, 自定义 manager, service 模块 |
| `layer:ui` | UI 层 | `templates/`, `forms.py`, `templatetags/` |
| `layer:middleware` | 中间件层 | `middleware.py`, `permissions.py`, 认证后端 |
| `layer:config` | 配置层 | `settings.py`, `urls.py`（根）, `wsgi.py`, `asgi.py`, `apps.py`, `manage.py` |
| `layer:test` | 测试层 | `tests.py`, `tests/` 目录, `conftest.py` |

### 需记录到 languageLesson 的显著模式

- **胖模型与瘦视图**：Django 鼓励把业务逻辑放在模型方法中，
  让视图保持为薄 HTTP 适配层
- **Django ORM 惰性求值**：QuerySet 直到迭代才求值，
  可以链式添加过滤而不触发数据库查询
- **类视图（CBV）**：`LoginRequiredMixin`、`PermissionRequiredMixin` 这类 Mixin
  通过多重继承组合行为
- **信号反模式**：信号制造不可见的耦合；
  `signals.py` 中的一个信号可能被代码库任意位置的 `save()` 调用触发
- **应用隔离**：每个 Django 应用（`INSTALLED_APPS`）都应自包含，
  拥有自己的 models、views、urls 与 migrations
