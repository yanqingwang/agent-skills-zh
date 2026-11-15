> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/frameworks/spring.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Spring Boot 框架补充说明

> 检测到 Spring Boot 时，将本文件注入 file-analyzer 与 architecture-analyzer 的提示词。
> 请勿单独作为提示词使用：必须始终附加在基础提示词模板之后。

## Spring Boot 项目结构

分析 Spring Boot 项目时，在基础分析规则之上应用以下附加约定。

### 规范文件角色

| 文件 / 模式 | 角色 | 标签 |
|---|---|---|
| `*Application.java`, `*Application.kt` | 应用入口：带 `main()` 方法的 `@SpringBootApplication` 类 | `entry-point`, `config` |
| `*Controller.java`, `*RestController.java` | REST 控制器：处理 HTTP 请求，委托给服务层 | `api-handler` |
| `*Service.java` | 服务接口：定义业务操作契约 | `service` |
| `*ServiceImpl.java` | 服务实现：包含业务逻辑 | `service` |
| `*Repository.java` | Spring Data 仓储：继承 JpaRepository/CrudRepository 的数据访问接口 | `data-model` |
| `*Entity.java` | JPA 实体：通过 `@Entity` 注解映射到数据库表 | `data-model` |
| `*DTO.java`, `*Request.java`, `*Response.java` | 数据传输对象：请求/响应载荷 | `type-definition` |
| `*Config.java`, `*Configuration.java` | 配置类：`@Configuration` Bean、安全配置、Web 配置 | `config` |
| `*Filter.java` | Servlet 过滤器：在请求到达控制器前拦截 | `middleware` |
| `*Interceptor.java` | 处理器拦截器：围绕控制器方法做前置/后置处理 | `middleware` |
| `*Advice.java`, `*ExceptionHandler.java` | 控制器通知：全局异常处理与响应包装 | `middleware` |
| `*Mapper.java` | 对象映射器：实体与 DTO 互转（MapStruct、ModelMapper） | `utility` |
| `application.yml`, `application.properties` | 应用配置：profile、数据源、服务器设置 | `config` |
| `*Test.java`, `*Tests.java`, `*IT.java` | 单元测试、集成测试 | `test` |

### 需要关注的边模式

**@Autowired 注入**：当类通过 `@Autowired`、构造器注入或 `@Inject` 注入依赖时，从消费方到被注入的 Bean 创建 `depends_on` 边。构造器注入是现代 Spring 的首选，也最常见。

**Controller-Service-Repository 调用链**：规范的调用链是 `@RestController` -> `@Service` -> `@Repository`。沿此链创建 `depends_on` 边，呈现分层架构。

**@Entity 关系**：当实体定义 `@OneToMany`、`@ManyToOne`、`@OneToOne` 或 `@ManyToMany` 注解时，在实体类之间创建 `depends_on` 边，描述中注明关系类型与方向。

**@Configuration Bean 定义**：当 `@Configuration` 类定义 `@Bean` 方法时，从该配置类到其产出的类型创建 `configures` 边。这些 Bean 可在整个应用中注入。

### Spring Boot 的架构分层

检测到时，将节点归入以下层：

| 层 ID | 层名称 | 包含内容 |
|---|---|---|
| `layer:api` | API 层 | `*Controller.java`、REST 端点、API 文档 |
| `layer:service` | 服务层 | `*Service.java`、`*ServiceImpl.java`、业务逻辑 |
| `layer:data` | 数据层 | `*Repository.java`、`*Entity.java`、JPA 映射、数据库迁移 |
| `layer:types` | 类型层 | `*DTO.java`、`*Request.java`、`*Response.java`、共享值对象 |
| `layer:config` | 配置层 | `*Configuration.java`、`application.yml`、安全配置、`*Application.java` |
| `layer:middleware` | 中间件层 | `*Filter.java`、`*Interceptor.java`、`*Advice.java`、安全过滤器 |
| `layer:test` | 测试层 | `*Test.java`、`*Tests.java`、`*IT.java`、测试配置 |

### 需记录到 languageLesson 的重点模式

- **构造器注入实现依赖注入**：Spring 偏好构造器注入而非字段注入（字段上的 `@Autowired`），它让依赖显式化、支持不可变性、简化测试
- **分层架构（Controller -> Service -> Repository）**：Spring Boot 应用遵循严格的分层模式：控制器处理 HTTP，服务承载业务逻辑，仓储管理持久化
- **Spring Security 过滤器链**：安全由一串 Servlet 过滤器实现，`SecurityFilterChain` Bean 配置认证、授权、CORS 与 CSRF 防护
- **JPA 实体生命周期**：实体在多个状态间流转（transient、managed、detached、removed），理解该生命周期对追踪持久化层的数据流至关重要
- **AOP 处理横切关注点**：带 `@Before`、`@After`、`@Around` 通知的 `@Aspect` 类在连接点注入行为，用于日志、事务（`@Transactional`）与缓存（`@Cacheable`）
