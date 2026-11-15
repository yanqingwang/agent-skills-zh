> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/frameworks/gin.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Gin (Go) 框架补充说明

> 检测到 Gin 时，将本文件注入 file-analyzer 与 architecture-analyzer 的提示词。
> 请勿单独作为提示词使用：必须始终附加在基础提示词模板之后。

## Gin 项目结构

分析 Gin 项目时，在基础分析规则之上应用以下附加约定。

### 规范文件角色

| 文件 / 模式 | 角色 | 标签 |
|---|---|---|
| `main.go` | 应用入口：初始化 Gin 引擎、注册路由、启动服务器 | `entry-point`, `config` |
| `cmd/*.go`, `cmd/**/*.go` | CLI 入口：多命令项目中的多个二进制入口 | `entry-point`, `config` |
| `handlers/*.go`, `handler/*.go` | HTTP 处理器：用 `gin.Context` 处理请求 | `api-handler` |
| `controllers/*.go`, `controller/*.go` | 控制器：HTTP 处理器的另一种命名 | `api-handler` |
| `routes/*.go`, `router/*.go` | 路由定义：注册端点与路由组 | `routing`, `config` |
| `models/*.go`, `model/*.go` | 数据模型：映射到数据库表的结构体定义 | `data-model` |
| `middleware/*.go` | 中间件函数：认证、日志、CORS、限流 | `middleware` |
| `services/*.go`, `service/*.go` | 业务逻辑：与 HTTP 层解耦的领域操作 | `service` |
| `repository/*.go`, `repo/*.go` | 数据访问层：数据库查询与持久化逻辑 | `data-model`, `service` |
| `config/*.go`, `config.go` | 应用配置：环境变量加载、基于结构体的配置 | `config` |
| `dto/*.go` | 数据传输对象：请求与响应结构体 | `type-definition` |
| `utils/*.go`, `pkg/*.go` | 共享工具包 | `utility` |
| `*_test.go` | 单元测试与集成测试 | `test` |

### 需要关注的边模式

**路由组注册**：当 `r.Group("/api")` 创建路由组并注册处理器时，从路由定义文件到每个处理器创建 `configures` 边。路由组按前缀与共享中间件组织端点。

**处理器调用服务**：当处理器函数调用服务方法时，从处理器到服务创建 `depends_on` 边。这体现 HTTP 处理与业务逻辑的分离。

**服务调用仓储**：当服务调用仓储方法做数据访问时，从服务到仓储创建 `depends_on` 边。这体现数据访问的抽象。

**中间件链**：当 `r.Use(middleware)` 或路由组应用中间件时，从路由器或路由组到中间件函数创建中间件边。中间件按注册顺序执行。

### Gin 的架构分层

检测到时，将节点归入以下层：

| 层 ID | 层名称 | 包含内容 |
|---|---|---|
| `layer:api` | API 层 | `handlers/`、`controllers/`、HTTP 处理函数 |
| `layer:data` | 数据层 | `models/`、`repository/`、数据库访问、迁移 |
| `layer:service` | 服务层 | `services/`、业务逻辑 |
| `layer:middleware` | 中间件层 | `middleware/`、认证、日志、限流 |
| `layer:config` | 配置层 | `main.go`、`routes/`、`config/`、环境配置 |
| `layer:utility` | 工具层 | `utils/`、`pkg/`、共享辅助包 |
| `layer:test` | 测试层 | `*_test.go`、测试 fixture、测试辅助 |

### 需记录到 languageLesson 的重点模式

- **带 gin.Context 的处理函数**：每个 Gin 处理器都接收 `*gin.Context` 参数，提供请求解析（`c.Bind`、`c.Param`、`c.Query`）、响应写出（`c.JSON`、`c.HTML`）与控制流（`c.Abort`、`c.Next`）
- **用 c.Next() 串起的中间件链**：中间件调用 `c.Next()` 把控制权交给链中下一个处理器，`c.Next()` 之前的代码在处理器前执行，之后的代码在处理器后执行
- **用路由组组织模块化 API**：`r.Group("/v1")` 创建可带自己中间件栈的模块化子路由器，支持在组级别做版本控制与访问控制
- **通过构造函数注入依赖（无框架 DI）**：Go 没有依赖注入框架，依赖以构造函数参数传入（如 `NewUserHandler(userService)`）并存为结构体字段
- **面向可测试性的接口化设计**：服务与仓储定义为接口，处理器依赖接口，测试中可用 mock 实现
- **用 gin.Error 处理错误**：Gin 通过 `c.Error(err)` 收集错误，中间件可在处理器执行后检查 `c.Errors`，实现集中式错误日志与响应格式化
