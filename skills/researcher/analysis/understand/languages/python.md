> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/python.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Python 语言提示词片段

## 核心概念

- **装饰器**：用 `@decorator` 语法包装其他函数或类的函数
- **列表/字典推导式**：从可迭代对象创建集合的简洁语法
- **生成器与 yield**：用 `yield` 实现惰性迭代，内存高效地处理数据
- **上下文管理器**：`with` 语句通过 `__enter__`/`__exit__` 管理资源
- **类型注解与 typing 模块**：为工具与文档提供可选的静态类型标注
- **Dunder 方法**：`__init__`、`__repr__`、`__eq__` 等定义对象行为的特殊方法
- **元类**：定义其他类如何被创建的类（`type` 是默认元类）
- **Dataclass**：`@dataclass` 装饰器根据字段注解自动生成样板代码
- **Protocol**：通过 `typing.Protocol` 实现结构化子类型，获得鸭子类型安全的接口
- **描述符**：定义 `__get__`、`__set__`、`__delete__` 以定制属性访问的对象
- **Async/Await 与 Asyncio**：用协程与事件循环实现协作式并发

## 导入模式

- `from module import name`：从模块导入指定名称
- `import module`：导入整个模块，通过 `module.name` 访问
- `from package.module import name`：从嵌套包绝对导入
- `from . import relative`：包内相对导入

## 文件模式

- `__init__.py`：包初始化文件（barrel 等价物），可再导出公共 API
- `__main__.py`：以 `python -m package` 运行时的包入口
- `conftest.py`：pytest 共享 fixture 与钩子（自动发现）
- `setup.py` / `pyproject.toml`：项目配置与构建元数据
- `requirements.txt`：固定版本的依赖列表

## 常见框架

- **Django**：自带 ORM、admin 与全套配件的全栈 Web 框架
- **FastAPI**：现代异步 API 框架，自动生成 OpenAPI 文档
- **Flask**：轻量 WSGI Web 微框架
- **SQLAlchemy**：采用工作单元模式的 SQL 工具箱与 ORM
- **Celery**：用于后台任务处理的分布式任务队列
- **Pydantic**：基于类型注解的数据校验与配置管理

## 示例语言说明

> 用 `@dataclass` 装饰器根据字段注解自动生成 `__init__`、`__repr__` 与
> `__eq__`。既消除样板代码，又保持类定义可读、生成的方法一致。
>
> 当 `__init__.py` 再导出符号时，它就是包的公共 API 表面：
> 使用者从包导入，而不是深入内部模块。
