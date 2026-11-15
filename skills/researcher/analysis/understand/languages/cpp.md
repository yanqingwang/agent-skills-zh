> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/cpp.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# C++ 语言提示词片段

## 核心概念

- **模板**：函数、类与变参模板，实现泛型的编译期多态
- **RAII**：资源获取即初始化，把资源生命周期绑定到对象作用域
- **智能指针**：`unique_ptr`（独占）、`shared_ptr`（引用计数）、`weak_ptr`（不持有）
- **移动语义**：右值引用（`&&`）与 `std::move` 实现高效的资源转移
- **运算符重载**：为自定义类型上的运算符定义行为
- **虚函数与 vtable**：通过虚方法派发表实现运行时多态
- **命名空间**：组织符号，避免跨编译单元的命名冲突
- **Constexpr**：函数与变量的编译期求值，实现零运行时开销的计算
- **Lambda 表达式**：带捕获列表的匿名函数，用于闭包
- **STL 容器与算法**：标准容器（vector、map、set）与泛型算法
- **Concepts（C++20）**：模板参数的具名约束，取代 SFINAE 模式

## 导入模式

- `#include <system_header>`：包含标准库或系统头文件
- `#include "local_header.h"`：包含项目本地的头文件
- `using namespace std`：把 std 的所有名称引入作用域（头文件中避免使用）
- `using std::vector`：选择性地引入指定名称

## 文件模式

- `.h` / `.hpp`：头文件，包含声明、模板与内联定义
- `.cpp` / `.cc`：实现文件，包含函数定义与静态数据
- `CMakeLists.txt`：CMake 构建系统配置
- `Makefile`：基于 Make 的构建规则与目标
- `main.cpp`：包含 `int main()` 的程序入口

## 常见框架

- **Qt**：带信号/槽机制的跨平台应用框架
- **Boost**：经过同行评审的可移植库集
- **Catch2**：仅头文件、支持 BDD 风格语法的测试框架
- **Google Test**：带 fixture、断言与 mock 的测试框架
- **gRPC**：面向服务间通信的高性能 RPC 框架

## 示例语言说明

> 用 `std::unique_ptr<T>` 实现 RAII 所有权，作用域退出时确定性地清理。
> unique 指针不可复制、只能移动，使所有权转移显式化，避免意外的
> double-free 错误。
>
> 头文件/实现分离（`.h`/`.cpp`）控制编译边界：修改 `.cpp` 文件只需
> 重编译该编译单元，而不是所有包含它的文件。
