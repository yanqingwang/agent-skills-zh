> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/frameworks/express.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Express 框架补充说明

> 检测到 Express 时，将本文件注入 file-analyzer 与 architecture-analyzer 的提示词。
> 请勿单独作为提示词使用：必须始终附加在基础提示词模板之后。

## Express 项目结构

分析 Express 项目时，在基础分析规则之上应用以下附加约定。

### 规范文件角色

| 文件 / 模式 | 角色 | 标签 |
|---|---|---|
| `app.js`, `app.ts` | 应用入口：创建 Express 应用，挂载中间件与路由 | `entry-point`, `config` |
| `server.js`, `server.ts`, `index.js`, `index.ts` | 服务器引导：启动 HTTP 监听，可能导入 app | `entry-point`, `config` |
| `routes/*.js`, `routes/*.ts` | 路由定义：把 HTTP 方法与路径映射到处理器 | `api-handler`, `routing` |
| `controllers/*.js`, `controllers/*.ts` | 请求处理器：处理请求、编排服务、返回响应 | `api-handler`, `service` |
| `models/*.js`, `models/*.ts` | 数据模型：Mongoose schema、Sequelize 模型或普通数据定义 | `data-model` |
| `middleware/*.js`, `middleware/*.ts` | 中间件函数：认证、日志、校验、错误处理 | `middleware` |
| `services/*.js`, `services/*.ts` | 业务逻辑：与 HTTP 层解耦的领域操作 | `service` |
| `db/*.js`, `db/*.ts`, `database/*.js` | 数据库连接与配置 | `data-model`, `config` |
| `config/*.js`, `config/*.ts` | 应用配置：环境变量、功能开关 | `config` |
| `validators/*.js`, `validators/*.ts` | 请求校验 schema（Joi、Zod、express-validator） | `validation`, `utility` |
| `utils/*.js`, `utils/*.ts` | 共享工具函数 | `utility` |
| `tests/*.js`, `test/*.js`, `__tests__/*.js` | 单元测试与集成测试 | `test` |

### 需要关注的边模式

**路由挂载**：当 `app.use('/api/users', usersRouter)` 挂载路由器时，从主应用到该路由模块创建 `depends_on` 边。这些边构成 HTTP 路由树。

**中间件链**：当 `app.use(cors())`、`app.use(authMiddleware)` 或 `router.use(validate)` 注册中间件时，从应用或路由器到中间件函数创建中间件边。顺序很重要：中间件按注册顺序执行。

**控制器调用服务**：当控制器导入并调用服务函数时，从控制器到服务创建 `depends_on` 边。这体现 HTTP 处理与业务逻辑的分离。

**模型关系**：当模型相互引用（Mongoose `ref`、Sequelize 关联）时，在模型文件之间创建 `depends_on` 边，描述中注明关系类型。

### Express 的架构分层

检测到时，将节点归入以下层：

| 层 ID | 层名称 | 包含内容 |
|---|---|---|
| `layer:api` | API 层 | `routes/`、`controllers/`、请求校验器 |
| `layer:data` | 数据层 | `models/`、`db/`、迁移文件、种子数据 |
| `layer:service` | 服务层 | `services/`、业务逻辑模块 |
| `layer:middleware` | 中间件层 | `middleware/`、错误处理器、认证、日志 |
| `layer:config` | 配置层 | `app.js`、`config/`、环境配置、`server.js` |
| `layer:utility` | 工具层 | `utils/`、`helpers/`、共享纯函数 |
| `layer:test` | 测试层 | `tests/`、`__tests__/`、`*.test.js`、`*.spec.js` |

### 需记录到 languageLesson 的重点模式

- **中间件链（req, res, next）**：Express 通过一串中间件函数处理请求，每个都接收请求、响应和一个 `next()` 回调以向前传递控制权
- **错误处理中间件（4 个参数）**：签名为 `(err, req, res, next)` 的中间件负责捕获错误，必须注册在所有路由之后才能充当全局错误处理器
- **路由器模块化**：`express.Router()` 创建模块化、可挂载的路由处理器，可在不同路径前缀组合进主应用
- **MVC 模式**：Express 应用常按职责分离为 Model（数据）、View（响应格式化）与 Controller（请求处理）
- **请求体解析与校验**：请求体解析（`express.json()`、`express.urlencoded()`）与校验（Joi、Zod、express-validator）是路由处理器之前应用的中间件职责
