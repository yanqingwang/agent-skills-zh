> **中文汉化版** · 上游：[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) · 原文件：`understand-anything-plugin/skills/understand/frameworks/rails.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Ruby on Rails 框架附录

> 检测到 Rails 时注入 file-analyzer 与 architecture-analyzer 的提示词。
> 不要单独当提示词使用：始终附加在基础提示词模板之后。

## Rails 项目结构

分析 Ruby on Rails 项目时，在基础分析规则之上应用以下附加约定。

### 规范文件角色

| 文件 / 模式 | 角色 | 标签 |
|---|---|---|
| `config.ru` | Rack 入口：为 web 服务器引导 Rails 应用 | `entry-point` |
| `config/application.rb` | 应用配置：初始化 Rails、加载 gems、配置中间件 | `entry-point`, `config` |
| `app/controllers/*_controller.rb` | 控制器：处理 HTTP 请求、调度模型、渲染响应 | `api-handler` |
| `app/controllers/concerns/*.rb` | 控制器 concern：通过 mixin 共享控制器行为 | `middleware`, `utility` |
| `app/models/*.rb` | ActiveRecord 模型：映射数据库表，包含校验与关联 | `data-model` |
| `app/models/concerns/*.rb` | 模型 concern：通过 mixin 共享模型行为 | `utility` |
| `app/views/**/*.erb`, `app/views/**/*.haml` | 视图模板：内嵌 Ruby 的 HTML 渲染 | `ui` |
| `app/helpers/*_helper.rb` | 视图 helper：模板中可用的工具方法 | `utility` |
| `app/mailers/*_mailer.rb` | Action Mailer 类：发送邮件通知 | `service` |
| `app/jobs/*_job.rb` | Active Job 类：后台任务处理 | `service` |
| `app/channels/*_channel.rb` | Action Cable 频道：WebSocket 通信 | `service` |
| `app/serializers/*_serializer.rb` | API 序列化器：JSON 响应格式化（ActiveModelSerializers, Blueprinter） | `api-handler`, `utility` |
| `app/services/*.rb` | Service 对象：封装复杂业务逻辑 | `service` |
| `db/migrate/*.rb` | 数据库迁移：按时间戳版本化的 schema 变更 | `config`, `data-model` |
| `db/schema.rb`, `db/structure.sql` | 生成的 schema 快照：当前数据库结构 | `data-model`, `config` |
| `config/routes.rb` | 路由定义：把 URL 映射到控制器动作 | `routing`, `config` |
| `config/initializers/*.rb` | 初始化器：启动时运行一次，配置 gems 与服务 | `config` |
| `lib/**/*.rb` | 库代码：自定义类、Rake 任务、扩展 | `utility`, `service` |
| `spec/**/*_spec.rb`, `test/**/*_test.rb` | RSpec 或 Minitest 测试文件 | `test` |

### 需要关注的边界模式

**路由到控制器的映射**：当 `config/routes.rb` 定义 `resources :users` 或
`get '/foo', to: 'bar#baz'` 时，从路由文件到对应控制器创建 `configures` 边。
RESTful 资源会生成一整套动作映射。

**ActiveRecord 关联**：当模型定义 `has_many`、`belongs_to`、`has_one` 或
`has_and_belongs_to_many` 时，在模型文件之间创建 `depends_on` 边，
并用描述注明关联类型与方向。

**控制器到模型**：当控制器调用模型方法（`User.find`、`@post.save`）时，
从控制器到模型创建 `depends_on` 边。控制器是模型数据的主要消费者。

**回调**：当模型或控制器使用 `before_action`、`after_save`、`before_validation`
等回调时，将其记为类似中间件的边。回调制造的隐式执行路径在调用点看不到。

### Rails 的架构分层

检测到时把节点归入以下层：

| 层 ID | 层名称 | 放入内容 |
|---|---|---|
| `layer:api` | API 层 | `app/controllers/`, `app/serializers/`, API 专用控制器 |
| `layer:data` | 数据层 | `app/models/`, `db/migrate/`, `db/schema.rb` |
| `layer:ui` | UI 层 | `app/views/`, `app/helpers/`, `app/assets/`, `app/javascript/` |
| `layer:service` | 服务层 | `app/mailers/`, `app/jobs/`, `app/channels/`, `app/services/`, `lib/` |
| `layer:config` | 配置层 | `config/routes.rb`, `config/initializers/`, `config/application.rb`, `config.ru` |
| `layer:middleware` | 中间件层 | `app/middleware/`, 控制器 concern, Rack 中间件 |
| `layer:test` | 测试层 | `spec/`, `test/`, `*.spec.rb`, `*_test.rb` |

### 需记录到 languageLesson 的显著模式

- **约定优于配置**：Rails 从命名约定推导路由、表名与文件位置：
  `UsersController` 对应 `users_controller.rb`，处理 `/users`，查询 `users` 表
- **ActiveRecord 模式**：模型是数据库包装器：每个模型类映射一张表，
  实例映射行，属性映射列并自动做类型转换
- **用 concern 共享行为**：`ActiveSupport::Concern` 模块是被模型或控制器
  include 的 mixin，用于跨类共享校验、scope、回调与方法
- **用强参数防批量赋值**：`params.require(:user).permit(:name, :email)`
  对属性做白名单：控制器必须显式声明哪些字段可由用户输入设置
- **RESTful 资源路由**：`resources :posts` 生成七条标准 CRUD 路由：
  Rails 强烈鼓励每个控制器对应一个资源的 RESTful 设计
- **回调与观察者**：`before_save`、`after_create` 等回调把逻辑注入对象生命周期，
  制造出难以追踪的隐式执行路径
