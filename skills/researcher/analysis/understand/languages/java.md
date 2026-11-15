> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/java.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Java 语言提示词片段

## 核心概念

- **泛型（含类型擦除）**：参数化类型在运行时被擦除，只在编译期保证安全
- **注解**：`@Override`、`@Autowired` 等元数据标记，在编译期或运行时处理
- **接口与抽象类**：带默认方法（Java 8+）与部分实现的契约
- **Streams API**：对集合做函数式管道操作（filter、map、reduce）
- **Lambda**：面向函数式接口的简洁匿名函数语法
- **Sealed 类**：显式列出许可子类的受限类层级（Java 17+）
- **Record**：自动生成访问器、equals、hashCode 的不可变数据载体（Java 16+）
- **依赖注入**：Spring 的核心 IoC 模式，支持构造器、字段或方法注入
- **受检与非受检异常**：受检异常必须声明或捕获，非受检异常继承 RuntimeException
- **Optional**：可空值的容器，鼓励显式处理而非判空

## 导入模式

- `import package.Class`：导入指定类
- `import package.*`：通配导入包内所有类
- `import static package.Class.method`：静态导入，直接访问方法/常量

## 文件模式

- `src/main/java/`：遵循 Maven/Gradle 标准布局的源码根目录
- `src/test/java/`：与主代码包结构对应的测试源码根目录
- `pom.xml`：Maven 项目配置与依赖管理
- `build.gradle`：Gradle 构建脚本（Groovy 或 Kotlin DSL）
- `Application.java`：带 `@SpringBootApplication` 的 Spring Boot 入口

## 常见框架

- **Spring Boot**：为生产就绪的 Spring 应用提供默认约定的框架
- **Jakarta EE**：面向服务端开发的企业级 Java 标准（前身为 Java EE）
- **Quarkus**：针对 GraalVM 与容器优化的云原生框架
- **Micronaut**：面向微服务与 serverless 的编译期 DI 框架
- **Hibernate**：实现 JPA 规范的 ORM 框架

## 示例语言说明

> 用 `@Autowired` 注解做构造器注入，遵循 Spring IoC 容器模式。构造器注入
> 优于字段注入：依赖显式化，并支持不可变性。
>
> Maven 标准目录布局（`src/main/java`、`src/test/java`）是强约定：
> 大多数构建工具与 IDE 默认都按此结构解析。
