> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/csharp.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# C# 语言提示词片段

## 核心概念

- **LINQ 查询**：语言集成查询，可用方法语法（`.Where().Select()`）或查询语法
- **Async/Await 与 Task**：异步编程模型，返回 `Task<T>` 实现非阻塞 I/O
- **泛型与约束**：类型参数带 `where T : class, IDisposable` 约束子句
- **属性（get/set）**：一等属性语法，含后备字段、自动属性与 init-only
- **委托与事件**：类型安全的函数指针，事件提供发布-订阅模式
- **特性（Attribute）**：`[HttpGet]`、`[Authorize]` 等元数据标注，用于声明式配置
- **可空引用类型**：用 `?` 标注实现编译器强制的空安全（C# 8+）
- **模式匹配**：`is` 与 `switch` 表达式支持类型、属性与关系模式
- **Record 与 init-only setter**：具有值相等语义的不可变引用类型（C# 9+）
- **内置依赖注入**：ASP.NET Core 的一等 DI 容器（`IServiceCollection`）

## 导入模式

- `using System.Collections.Generic`：导入命名空间，免限定使用类型
- `using static System.Math`：导入静态成员，直接访问方法
- `global using`：应用于整个项目的 using 声明（C# 10）
- `using Alias = Namespace.Type`：类型别名，用于消歧

## 文件模式

- `*.csproj`：MSBuild 项目文件，定义目标、包与构建属性
- `*.sln`：Visual Studio 解决方案文件，组织多个项目
- `Program.cs`：应用入口（.NET 6+ 的顶级语句）
- `Startup.cs`：服务与中间件配置（较旧的 ASP.NET Core 模式）
- `appsettings.json`：分层应用配置

## 常见框架

- **ASP.NET Core**：面向 API、MVC 与 Razor Pages 的跨平台 Web 框架
- **Entity Framework**：带 LINQ-to-SQL、迁移与变更跟踪的 ORM
- **Blazor**：用 C# 取代 JavaScript 的组件式 UI 框架
- **MAUI**：面向移动与桌面应用的跨平台原生 UI
- **xUnit**：支持 theory、fact 与依赖注入的现代测试框架

## 示例语言说明

> 用 LINQ 方法语法 `.Where().Select()` 在集合上组合查询管道。LINQ 操作
> 惰性求值：查询只在枚举结果时执行，无需中间分配即可高效组合。
>
> ASP.NET Core 内置 DI 容器在 `Program.cs` 注册服务，并通过构造器注入
> 解析，遵循组合根（composition root）模式。
