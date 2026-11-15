> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/scala.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Scala 语言提示词片段

## 核心概念

- **Case Class**：不可变数据载体，自动生成 `equals`、`hashCode`、`copy` 并支持模式匹配
- **模式匹配**：`match` 表达式穷尽解构 ADT；对 sealed 层级，编译器会对遗漏分支告警
- **Trait**：接口加实现的混入；通过线性化叠加行为
- **Implicits / Given 实例**：Scala 2 的 `implicit` / Scala 3 的 `given`+`using` 在编译期解析 type-class 实例与上下文参数
- **Type Class**：通过 implicit/given 实现的特设多态（如 Cats 的 `Functor`、`Monad`）；留意 `F[_]` 类型参数
- **高阶类型（Higher-Kinded Types）**：对类型构造器（`F[_]`）的抽象，是 tagless-final 服务定义的基础
- **For 推导式**：`flatMap`/`map` 链的语法糖，是串接效应（`IO`、`Future`、`Either`）的标准方式
- **效应系统**：Cats Effect（`IO`、`Resource`、`Fiber`）、ZIO 与 FS2 把副作用建模为可组合的值，在“世界尽头”才运行
- **伴生对象**：与类/trait 配对的单例，存放工厂方法、type-class 实例与 ADT 构造器
- **Sealed 层级（ADT）**：`sealed trait` + case class/object 建模封闭的和类型；Scala 3 中为 enum

## 导入模式

- `import package.ClassName`：导入指定成员
- `import package.{A, B}`：选择器列表，一次导入多个成员
- `import package._`（Scala 2）/ `import package.*`（Scala 3）：通配导入
- `import package.{Name => Alias}`（Scala 2）/ `import package.Name as Alias`（Scala 3）：导入时重命名
- `import cats.syntax.all._`：语法扩展导入，启用扩展方法（Typelevel 代码中常见）

## 文件模式

- `build.sbt`：sbt 构建定义；`project/` 存放构建支持代码
- `build.sc` / `build.mill`：Mill 构建定义
- `Main.scala` / `*App.scala`：入口（Cats Effect 用 `object ... extends IOApp`，其余用 `extends App`/`@main`）
- `package.scala`：包对象，存放包级成员（Scala 2 惯用法）
- `src/main/scala/`：遵循 sbt 约定的主源码根目录
- `src/test/scala/`：测试源码根目录；测试按惯例以 `*Spec.scala` / `*Suite.scala` 结尾

## 常见框架

- **Cats Effect**：纯函数式运行时，提供 `IO`、`Resource` 与基于 fiber 的并发
- **ZIO**：带类型化错误与环境（`ZIO[R, E, A]`）的效应系统
- **Akka / Pekko**：基于 actor 的并发、流处理与集群
- **Play Framework**：全栈 MVC Web 框架
- **http4s**：构建在 Cats Effect 与 FS2 之上的纯函数式 HTTP 服务端/客户端
- **Spark**：分布式数据处理；留意 `Dataset`/`DataFrame` 转换

## 示例语言说明

> 服务定义为 tagless-final trait `UserRepo[F[_]]`，同一份业务逻辑
> 在生产中跑 `IO`，在测试中跑状态 monad。
> 伴生对象中的 given/implicit 实例装配生产实现。

> 用 sealed trait `Command` 及其 case class 变体，在解释器中穷尽匹配：
> 新增变体时编译器会标记所有未处理的命令。
