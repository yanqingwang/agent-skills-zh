> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/php.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# PHP 语言提示词片段

## 核心概念

- **命名空间**：用反斜杠分隔的路径组织代码，避免命名冲突
- **Trait**：横向代码复用机制，在无关类之间共享方法
- **类型声明**：参数、返回值与属性类型（标量、联合、交叉类型）
- **属性注解（PHP 8+）**：原生元数据标注，取代基于 docblock 的配置
- **枚举（PHP 8.1+）**：一等枚举类型，可带方法并实现接口
- **Fiber**：轻量协作式并发原语，用于非阻塞 I/O
- **闭包/匿名函数**：一等函数，用显式 `use` 捕获变量
- **魔术方法**：`__construct`、`__get`、`__set`、`__call` 等定义对象行为的特殊方法
- **依赖注入**：构造器注入，由 PSR-11 兼容容器管理
- **中间件**：现代 PHP 框架核心的请求/响应管道模式

## 导入模式

- `use Namespace\ClassName`：按完全限定名导入类
- `use Namespace\ClassName as Alias`：别名导入，避免冲突
- `namespace App\Http\Controllers`：声明当前文件的命名空间
- `use function Namespace\functionName`：导入带命名空间的函数

## 文件模式

- `composer.json`：依赖管理与 PSR-4 自动加载配置
- `index.php`：Web 应用入口（前端控制器）
- `artisan`：Laravel CLI 入口，用于命令与迁移
- `routes/`：路由定义文件（Laravel 的 web.php、api.php）
- PSR-4 自动加载把命名空间前缀映射到目录路径

## 常见框架

- **Laravel**：全功能框架，带 Eloquent ORM、Blade 模板与队列
- **Symfony**：组件化框架，支撑大量 PHP 项目与库
- **WordPress**：基于钩子插件架构的 CMS 平台
- **Slim**：面向 API 与小型应用的微框架
- **CodeIgniter**：极少配置的轻量 MVC 框架

## 示例语言说明

> 在控制器方法上用 PHP 8 属性注解 `#[Route('/api/users')]` 做声明式
> 路由映射。属性注解取代旧的 docblock 注解模式，为工具可反射的元数据
> 提供原生语言支持。
>
> `composer.json` 中的 PSR-4 自动加载把 `App\` 映射到 `src/`，因此类
> `App\Http\Controllers\UserController` 从
> `src/Http/Controllers/UserController.php` 加载。
