> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/kotlin.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Kotlin 语言提示词片段

## 核心概念

- **协程与 Flow**：挂起函数实现结构化并发，Flow 用于响应式流
- **数据类**：自动生成 `equals`、`hashCode`、`toString`、`copy` 与解构
- **Sealed 类/接口**：受限层级，支持穷尽的 `when` 表达式
- **扩展函数**：不通过继承或包装即给已有类添加方法
- **空安全**：`?.` 安全调用、`!!` 非空断言、`?:` Elvis 运算符提供默认值
- **委托（by 关键字）**：把接口实现或属性访问委托给另一个对象
- **DSL 构建器**：带接收者的 lambda 语法，实现类型安全的构建器模式
- **内联函数与 reified 类型**：inline 消除 lambda 开销，reified 在运行时访问类型
- **伴生对象**：与类关联的具名或匿名单例（取代静态成员）
- **作用域函数**：`let`、`run`、`apply`、`also`、`with` 用于简洁的对象配置与变换

## 导入模式

- `import package.ClassName`：导入指定类
- `import package.*`：通配导入包内所有声明
- `import package.function as alias`：别名导入，解决命名冲突

## 文件模式

- `build.gradle.kts`：使用 Kotlin DSL 的 Gradle 构建脚本
- `Application.kt`：应用入口（Spring Boot 或 Ktor）
- `src/main/kotlin/`：遵循 Gradle 约定的主源码根目录
- `src/test/kotlin/`：与主代码包结构对应的测试源码根目录
- `settings.gradle.kts`：多模块项目配置

## 常见框架

- **Spring Boot (Kotlin)**：Kotlin 优先支持，带协程与 DSL 扩展
- **Ktor**：JetBrains 出品的 Kotlin 原生异步 Web 框架
- **Jetpack Compose**：用可组合函数构建的 Android 声明式 UI 工具包
- **Exposed**：轻量 SQL 框架，带类型安全 DSL 与 DAO 模式
- **Koin**：用 Kotlin DSL 的务实依赖注入框架

## 示例语言说明

> 用 sealed 类层级配合 `when` 穷尽匹配处理所有可能的 API 响应状态。
> 编译器强制覆盖每个变体，既省去兜底的 `else` 分支，又在编译期捕获
> 遗漏的 case。
>
> 扩展函数可添加 `String.toSlug()` 这类工具方法而无需修改原类，
> 并可通过 IDE 自动补全被发现。
