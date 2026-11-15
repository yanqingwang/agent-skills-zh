> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/go.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Go 语言提示词片段

## 核心概念

- **Goroutine**：用 `go` 关键字启动的轻量并发函数
- **Channel**：goroutine 之间通信与同步的类型化管道
- **接口**：隐式满足的契约，无需 `implements` 关键字
- **结构体嵌入**：提供字段与方法提升的组合机制
- **错误处理**：显式返回错误值（`error` 接口），而非异常
- **Defer/Panic/Recover**：延迟清理、不可恢复错误与恢复机制
- **切片与数组**：数组是固定大小的值，切片是底层数组的动态视图
- **指针**：显式指针类型实现按引用传递（无指针运算）
- **Context 传递**：`context.Context` 携带截止时间、取消信号与请求作用域的值
- **init 函数**：包级 `init()` 在 `main()` 之前自动运行，用于初始化

## 导入模式

- `import "package"`：导入单个包
- `import alias "package"`：别名导入，避免命名冲突
- `import ( ... )`：分组导入块（标准库、外部依赖、内部包依次排列）
- `import _ "package"`：空白导入，只为副作用（如驱动注册）

## 文件模式

- `*_test.go`：同包内的测试文件（黑盒测试用 `_test` 包）
- `cmd/`：存放 main 包的目录（二进制入口）
- `internal/`：仅父模块可导入的包（由编译器强制）
- `pkg/`：公共库包（约定，不强制）
- `go.mod`：模块定义，含依赖版本
- `go.sum`：依赖的加密校验和

## 常见框架

- **Gin**：支持中间件的高性能 HTTP 框架
- **Echo**：内置中间件的极简 Web 框架
- **Fiber**：基于 fasthttp、借鉴 Express 的框架
- **Chi**：轻量、可组合的 HTTP 路由器
- **GORM**：支持关联、钩子与迁移的 ORM 库

## 示例语言说明

> 隐式实现 `io.Reader` 接口：无需显式声明，方法签名匹配即可。
> 任何带 `Read([]byte) (int, error)` 方法的类型都可用在期望
> `io.Reader` 的地方。
>
> `internal/` 目录由编译器强制封装，外部包无法导入其实现细节，
> 比命名约定更严格。
