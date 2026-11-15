> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/graphql.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# GraphQL 语言提示词片段

## 核心概念

- **类型系统**：强类型 schema 定义 API 契约，含标量、对象、枚举与联合类型
- **查询（Query）**：读取操作，按字段级选择获取数据（不过量取数）
- **变更（Mutation）**：写入操作，创建、更新、删除数据
- **订阅（Subscription）**：通过 WebSocket 连接实时推送数据
- **Resolver**：把 schema 字段映射到数据源（数据库、API、缓存）的函数
- **Fragment**：可复用的字段选择，减少跨操作的查询重复
- **指令**：`@deprecated`、`@include`、`@skip` 用于条件字段包含与 schema 元数据
- **输入类型**：`input` 关键字定义复杂变更参数
- **接口与联合**：多态类型，让多个对象类型共享字段
- **Schema Stitching / Federation**：把多个 GraphQL 服务组合成统一图谱

## 重要文件模式

- `schema.graphql` / `*.graphql`：schema 定义文件
- `*.gql`：GraphQL 文件的另一种扩展名
- `schema/*.graphql`：按领域拆分的 schema 文件（users.graphql、orders.graphql）
- `*.resolvers.ts` / `*.resolvers.js`：Resolver 实现（TypeScript/JavaScript 约定）
- `codegen.yml`：GraphQL Code Generator 配置

## 边模式

- GraphQL schema 文件为实现查询/变更处理器的 resolver 代码建立 `defines_schema` 边
- 类型定义在由字段引用连接的类型之间创建 `related` 边
- schema 文件为消费该 API 的客户端查询/变更文件建立 `defines_schema` 边
- codegen 配置对 schema 到代码的生成管线建立 `configures` 边

## 摘要风格

> "GraphQL schema：为用户管理 API 定义 N 个类型、M 个查询与 K 个变更。"
> "API schema：含产品、订单与支付处理的类型定义，支持分页。"
> "订阅 schema：为订单状态更新启用实时通知。"
