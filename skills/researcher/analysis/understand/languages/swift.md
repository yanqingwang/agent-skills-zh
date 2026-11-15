> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/swift.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Swift 语言提示词片段

## 核心概念

- **可选值与可选链**：`Type?` 包装可能为 nil 的值，`?.` 安全链式访问
- **协议与协议扩展**：定义契约并通过扩展提供默认实现
- **值类型与引用类型**：struct 与 enum 是值类型，class 是引用类型
- **闭包**：捕获周围上下文的自包含功能块
- **属性包装器**：`@State`、`@Binding`、`@Published` 封装属性存储逻辑
- **Result Builder**：`@ViewBuilder`、`@resultBuilder` 支持声明式 DSL 语法
- **Actor 与结构化并发**：`actor` 类型隔离数据，`async let` 与 `TaskGroup` 管理并发
- **泛型**：类型参数带 `where` 子句与关联类型约束
- **带关联值的枚举**：每个 case 可携带不同类型的载荷
- **扩展**：为已有类型添加方法、计算属性与协议遵循

## 导入模式

- `import Foundation`：核心库，含数据类型、集合、网络
- `import UIKit`：iOS UI 框架，面向传统视图控制器架构
- `import SwiftUI`：声明式 UI 框架，带响应式状态管理
- `@testable import ModuleName`：以 internal 访问级别导入，用于单元测试

## 文件模式

- `Package.swift`：Swift Package Manager 清单，定义目标与依赖
- `*.xcodeproj` / `*.xcworkspace`：Xcode 项目与工作区配置
- `AppDelegate.swift`：UIKit 应用生命周期入口
- `App.swift`：用 `@main` 的 SwiftUI 应用入口
- `Tests/`：遵循 SPM 或 Xcode 约定的测试目标目录

## 常见框架

- **SwiftUI**：响应式数据流的声明式 UI 框架
- **UIKit**：用视图控制器与 Auto Layout 的命令式 UI 框架
- **Vapor**：支持异步的服务端 Swift Web 框架
- **Combine**：随时间处理值的响应式框架
- **Core Data**：对象图与持久化框架

## 示例语言说明

> 用 `@Published` 属性包装器在状态变化时自动通知 SwiftUI 视图。被包装
> 的值变化时，属性包装器触发外层 `ObservableObject` 的 `objectWillChange`，
> 使依赖的视图重渲染。
>
> 协议扩展提供默认实现：类型只需声明遵循即可，默认实现足够时无需
> 编写方法体。
