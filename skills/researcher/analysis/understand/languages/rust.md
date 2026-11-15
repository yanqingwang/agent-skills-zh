> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/rust.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Rust 语言提示词片段

## 核心概念

- **所有权与借用**：每个值只有一个所有者，引用借用而不取得所有权
- **生命周期**：`'a` 等标注保证引用在所需期间内有效
- **Trait 与 Trait 对象**：共享行为定义，`dyn Trait` 用于动态派发
- **模式匹配**：穷尽的 `match` 表达式解构枚举、结构体与元组
- **带数据的枚举**：代数数据类型，每个变体可携带不同的关联数据
- **Result/Option 错误处理**：`Result<T, E>` 表示可能失败的操作，`Option<T>` 表示可空值
- **宏**：声明式（`macro_rules!`）与过程式（derive、属性、类函数）代码生成
- **Async/Await 与 Tokio**：基于 `Future` trait 与运行时执行器的零开销异步
- **unsafe 块**：按需开启的代码块，用于裸指针解引用、FFI 与绕过借用检查器
- **泛型与 Trait 约束**：`<T: Clone + Send>` 约束泛型参数
- **闭包与 Fn trait**：`Fn`、`FnMut`、`FnOnce` 决定闭包如何捕获环境

## 导入模式

- `use crate::module::Item`：从当前 crate 导入
- `use std::collections::HashMap`：从标准库导入
- `use super::*`：导入父模块的全部内容
- `mod module_name`：声明子模块（从文件加载）

## 文件模式

- `mod.rs`：模块 barrel 文件（旧约定），或 `module_name.rs`（2018+ edition）
- `lib.rs`：定义公共 API 的库 crate 根
- `main.rs`：二进制 crate 入口
- `Cargo.toml`：项目清单，含依赖与元数据
- `build.rs`：编译前执行的构建脚本

## 常见框架

- **Actix-web**：基于 Actor 的高性能 Web 框架
- **Axum**：构建在 Tower 与 Hyper 之上的人体工学 Web 框架
- **Rocket**：声明式路由的类型安全 Web 框架
- **Diesel**：安全、可组合的 ORM 与查询构建器
- **Tokio**：提供 I/O、定时器与任务调度的异步运行时

## 示例语言说明

> 以 `&self` 借用读取状态而不转移所有权，返回 `Result<T, Error>`
> 显式传播错误。`?` 运算符简洁地沿调用栈向上传播错误，取代冗长的
> match 块。
>
> 模块系统映射到文件系统：`mod handlers;` 加载 `handlers.rs` 或
> `handlers/mod.rs`，在编译期确立模块树。
