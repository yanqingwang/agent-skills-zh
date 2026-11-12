---
name: python-project-structure
description: Python 项目组织、模块架构与公共 API 设计。在从零搭建新项目、组织模块、用 __all__ 定义公共接口，或规划目录布局时使用本 Skill。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/python-development/skills/python-project-structure/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Python 项目结构与模块架构

设计组织良好的 Python 项目，做到模块边界清晰、公共接口明确、目录结构易于维护。良好的组织让代码易于查找，让变更可预期。

## 何时使用本 Skill

- 从零开始一个新的 Python 项目
- 重新组织现有代码库以提升清晰度
- 用 `__all__` 定义模块公共 API
- 在扁平与嵌套目录结构之间做选择
- 确定测试文件的放置策略
- 创建可复用的库包

## 核心概念

### 1. 模块内聚

把会一起变化的相关代码归为一组。一个模块应当只有一个明确用途。

### 2. 显式接口

用 `__all__` 定义哪些内容是公共的。未列出的都属于内部实现细节。

### 3. 扁平层级

优先采用浅层目录结构。仅在确有子领域时才增加层级。

### 4. 一致的约定

在整个项目中统一应用命名与组织模式。

## 快速开始

```
myproject/
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── services/
│       ├── models/
│       └── api/
├── tests/
├── pyproject.toml
└── README.md
```

## 基础模式

### 模式 1：每个文件一个概念

每个文件应聚焦于单一概念或一组紧密相关的函数。当文件出现以下情况时，考虑拆分：

- 承担多个互不相关的职责
- 超过 300-500 行（视复杂度而定）
- 包含因不同原因而变化的类

```python
# Good: Focused files
# user_service.py - User business logic
# user_repository.py - User data access
# user_models.py - User data structures

# Avoid: Kitchen sink files
# user.py - Contains service, repository, models, utilities...
```

### 模式 2：用 `__all__` 定义显式公共 API

为每个模块定义公共接口。未列出的成员都是内部实现细节。

```python
# mypackage/services/__init__.py
from .user_service import UserService
from .order_service import OrderService
from .exceptions import ServiceError, ValidationError

__all__ = [
    "UserService",
    "OrderService",
    "ServiceError",
    "ValidationError",
]

# Internal helpers remain private by omission
# from .internal_helpers import _validate_input  # Not exported
```

### 模式 3：扁平目录结构

优先采用最少的嵌套。层级过深会让导入语句冗长、导航困难。

```
# Preferred: Flat structure
project/
├── api/
│   ├── routes.py
│   └── middleware.py
├── services/
│   ├── user_service.py
│   └── order_service.py
├── models/
│   ├── user.py
│   └── order.py
└── utils/
    └── validation.py

# Avoid: Deep nesting
project/core/internal/services/impl/user/
```

仅在确有需要隔离的子领域时才添加子包。

### 模式 4：测试文件组织

选择一种方式，并在整个项目中一致地贯彻。

**选项 A：就近放置测试**

```
src/
├── user_service.py
├── test_user_service.py
├── order_service.py
└── test_order_service.py
```

优点：测试紧邻其所验证的代码，容易发现覆盖缺口。

**选项 B：平行测试目录**

```
src/
├── services/
│   ├── user_service.py
│   └── order_service.py
tests/
├── services/
│   ├── test_user_service.py
│   └── test_order_service.py
```

优点：生产代码与测试代码清晰分离，是大型项目的标准做法。

## 高级模式

### 模式 5：包初始化

用 `__init__.py` 为包的使用方提供整洁的公共接口。

```python
# mypackage/__init__.py
"""MyPackage - A library for doing useful things."""

from .core import MainClass, HelperClass
from .exceptions import PackageError, ConfigError
from .config import Settings

__all__ = [
    "MainClass",
    "HelperClass",
    "PackageError",
    "ConfigError",
    "Settings",
]

__version__ = "1.0.0"
```

使用方随后可以直接从包导入：

```python
from mypackage import MainClass, Settings
```

### 模式 6：分层架构

按架构分层组织代码，实现清晰的关注点分离。

```
myapp/
├── api/           # HTTP handlers, request/response
│   ├── routes/
│   └── middleware/
├── services/      # Business logic
├── repositories/  # Data access
├── models/        # Domain entities
├── schemas/       # API schemas (Pydantic)
└── config/        # Configuration
```

每一层只应依赖其下方的层，绝不依赖上方的层。

### 模式 7：领域驱动结构

对于复杂应用，按业务领域而非技术分层来组织。

```
ecommerce/
├── users/
│   ├── models.py
│   ├── services.py
│   ├── repository.py
│   └── api.py
├── orders/
│   ├── models.py
│   ├── services.py
│   ├── repository.py
│   └── api.py
└── shared/
    ├── database.py
    └── exceptions.py
```

## 文件与模块命名

### 约定

- 所有文件与模块名使用 `snake_case`：`user_repository.py`
- 避免表意不清的缩写：用 `user_repository.py` 而非 `usr_repo.py`
- 类名与文件名对应：`UserService` 放在 `user_service.py` 中

### 导入风格

使用绝对导入，更清晰也更可靠：

```python
# Preferred: Absolute imports
from myproject.services import UserService
from myproject.models import User

# Avoid: Relative imports
from ..services import UserService
from . import models
```

模块被移动或重新组织时，相对导入可能失效。

## 最佳实践总结

1. **保持文件聚焦** - 每个文件一个概念，超过 300-500 行时考虑拆分（视复杂度而定）
2. **显式定义 `__all__`** - 让公共接口清晰明确
3. **优先采用扁平结构** - 仅在确有子领域时才增加层级
4. **使用绝对导入** - 更可靠也更清晰
5. **保持一致** - 在整个项目中统一应用模式
6. **名称与内容对应** - 文件名应说明其用途
7. **分离关注点** - 保持各层区分明确，依赖单向流动
8. **为结构编写文档** - 附上解释组织方式的 README
