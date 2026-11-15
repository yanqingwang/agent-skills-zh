> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/frameworks/nextjs.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Next.js 框架补充说明

> 检测到 Next.js 时，将本文件注入 file-analyzer 与 architecture-analyzer 的提示词。
> 请勿单独作为提示词使用：必须始终附加在基础提示词模板之后。

## Next.js 项目结构

分析 Next.js 项目时，在基础分析规则之上应用以下附加约定。

### 规范文件角色

| 文件 / 模式 | 角色 | 标签 |
|---|---|---|
| `app/layout.tsx` | 根布局：包裹所有页面，定义 HTML 外壳与全局 Provider | `entry-point`, `config`, `ui` |
| `app/page.tsx` | 根页面组件：渲染在 `/` | `ui`, `routing` |
| `app/**/page.tsx` | 路由页面组件：文件路径决定 URL | `ui`, `routing` |
| `app/**/layout.tsx` | 嵌套布局：用共享 UI 包裹子路由 | `ui`, `config` |
| `app/**/loading.tsx` | 加载 UI：路由切换期间作为 Suspense fallback 显示 | `ui` |
| `app/**/error.tsx` | 错误边界：捕获该路由段内的错误 | `ui` |
| `app/**/not-found.tsx` | 404 UI：调用 `notFound()` 时显示 | `ui` |
| `app/api/**/route.ts` | API 路由处理器：Serverless 端点函数（GET、POST 等） | `api-handler` |
| `middleware.ts` | Edge 中间件：在请求到达路由前拦截 | `middleware` |
| `lib/*.ts`, `lib/**/*.ts` | 共享服务端工具、数据访问与业务逻辑 | `service` |
| `components/*.tsx`, `components/**/*.tsx` | 可复用 UI 组件 | `ui` |
| `next.config.js`, `next.config.mjs`, `next.config.ts` | Next.js 配置：重定向、重写、环境变量、webpack 覆盖 | `config` |
| `actions/*.ts`, `app/**/actions.ts` | Server Actions：可从客户端调用的服务端变更函数 | `service`, `api-handler` |

### 需要关注的边模式

**布局嵌套**：当 `app/foo/layout.tsx` 包裹 `app/foo/page.tsx` 与 `app/foo/bar/page.tsx` 时，从布局到其包裹的每个页面创建 `contains` 边。布局通过文件系统层级组合。

**API 路由处理器**：当 `route.ts` 文件导出命名函数（GET、POST、PUT、DELETE）时，根据 fetch 调用，从消费组件或 Server Action 到该路由处理器创建边。

**服务端/客户端组件边界**：文件顶部带 `"use client"` 指令的是客户端组件，`app/` 目录下其余组件默认是服务端组件。跨此边界的 `depends_on` 边要创建，并在边描述中注明该边界。

**并行路由**：出现 `app/@slot/page.tsx` 模式时，从父布局到每个并行插槽创建 `contains` 边。它们在同一布局中同时渲染。

**路由组**：用括号包裹的目录 `(group)` 在不影响 URL 路径的情况下组织路由。在节点描述中注明。

### Next.js 的架构分层

检测到时，将节点归入以下层：

| 层 ID | 层名称 | 包含内容 |
|---|---|---|
| `layer:ui` | UI 层 | `app/**/page.tsx`、`app/**/layout.tsx`、`components/`、加载/错误边界 |
| `layer:api` | API 层 | `app/api/**/route.ts`、API 路由处理器 |
| `layer:service` | 服务层 | `lib/`、Server Actions、数据获取工具 |
| `layer:middleware` | 中间件层 | `middleware.ts`、Edge 函数 |
| `layer:config` | 配置层 | `next.config.*`、根布局、`tailwind.config.*`、环境配置 |
| `layer:test` | 测试层 | `__tests__/`、`*.test.tsx`、`*.spec.tsx`、`e2e/` |

### 需记录到 languageLesson 的重点模式

- **默认服务端组件**：`app/` 目录中的组件都是服务端组件，除非声明了 `"use client"`，否则不会有 JavaScript 发送到客户端
- **用 Server Actions 做变更操作**：标记 `"use server"` 的函数可从客户端组件直接调用，在表单提交与变更操作上取代传统 API 路由
- **App Router 文件约定**：特殊文件（`page`、`layout`、`loading`、`error`、`not-found`、`route`）在文件系统路由器中按命名约定定义行为
- **ISR 与静态生成**：`generateStaticParams` 在构建时预渲染页面，重新验证策略控制缓存新鲜度
- **并行路由与拦截路由**：`@slot` 目录支持并行渲染，`(.)` 前缀目录支持路由拦截以实现弹窗模式
