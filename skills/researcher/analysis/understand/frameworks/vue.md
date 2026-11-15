> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/frameworks/vue.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Vue 框架补充说明

> 检测到 Vue 时，将本文件注入 file-analyzer 与 architecture-analyzer 的提示词。
> 请勿单独作为提示词使用：必须始终附加在基础提示词模板之后。

## Vue 项目结构

分析 Vue 项目时，在基础分析规则之上应用以下附加约定。

### 规范文件角色

| 文件 / 模式 | 角色 | 标签 |
|---|---|---|
| `src/App.vue` | 根应用组件：挂载顶层布局与路由视图 | `entry-point`, `ui` |
| `src/main.ts`, `src/main.js` | 应用引导：创建 Vue 应用实例、注册插件、挂载到 DOM | `entry-point`, `config` |
| `components/*.vue`, `components/**/*.vue` | 可复用 UI 组件 | `ui` |
| `views/*.vue`, `pages/*.vue` | 映射到路由的页面级组件 | `ui`, `routing` |
| `composables/*.ts`, `composables/*.js` | 组合式函数：用 Composition API 封装可复用的有状态逻辑 | `service`, `utility` |
| `store/*.ts`, `stores/*.ts` | 状态管理模块（Pinia store 或 Vuex module） | `service`, `state` |
| `router/*.ts`, `router/index.ts` | Vue Router 配置：路由定义、导航守卫 | `config`, `routing` |
| `plugins/*.ts`, `plugins/*.js` | Vue 插件注册：扩展应用功能（i18n、认证等） | `config` |
| `utils/*.ts`, `helpers/*.ts` | 纯工具函数 | `utility` |
| `types/*.ts`, `types/*.d.ts` | TypeScript 类型定义与接口 | `type-definition` |
| `api/*.ts`, `services/*.ts` | API 客户端函数与数据获取逻辑 | `service` |
| `directives/*.ts` | 自定义 Vue 指令 | `utility` |
| `tests/*.spec.ts`, `__tests__/*.spec.ts` | 单元测试与集成测试 | `test` |

### 需要关注的边模式

**组件父子关系**：当父组件在其 `<template>` 中使用子组件时，从父到子创建 `contains` 边。模板 ref 与 slot 用法进一步表明组合关系。

**组合式函数使用**：当组件或组合式函数导入并调用某个 `useX` 函数时，从消费方到该组合式函数模块创建 `depends_on` 边。组合式函数是共享有状态逻辑的主要机制。

**Store 的 actions/getters**：当组件或组合式函数导入并使用 Pinia store（`useXStore()`）时，从消费方到该 store 创建 `depends_on` 边。store 之间的依赖也要记录。

**路由视图映射**：当 `router/index.ts` 把路径映射到视图组件时，从路由器到每个视图组件创建 `configures` 边。导航守卫产生类似中间件的边。

**插件注册**：当 `main.ts` 调用 `app.use(plugin)` 时，从引导文件到每个插件创建 `configures` 边。

### Vue 的架构分层

检测到时，将节点归入以下层：

| 层 ID | 层名称 | 包含内容 |
|---|---|---|
| `layer:ui` | UI 层 | `components/`、`views/`、`pages/`、布局组件 |
| `layer:service` | 服务层 | `composables/`、`store/`、`stores/`、`api/`、`services/` |
| `layer:config` | 配置层 | `router/`、`plugins/`、`main.ts`、`App.vue`、配置文件 |
| `layer:utility` | 工具层 | `utils/`、`helpers/`、`directives/`、纯函数 |
| `layer:test` | 测试层 | `tests/`、`__tests__/`、`*.spec.ts` |

### 需记录到 languageLesson 的重点模式

- **Composition API 优于 Options API**：现代 Vue 偏好 `setup()` 与 `<script setup>` 搭配组合式函数，取代 Options API 的 data/methods/computed 分离写法
- **用 Pinia 做状态管理**：Pinia store 提供类型安全、模块化的状态与 actions、getters，每个 store 独立定义，且可依赖其他 store
- **Vue Router 与导航守卫**：`beforeEach`、`beforeEnter`、`afterEach` 守卫充当路由切换的中间件，用于认证与数据预取
- **单文件组件（.vue）**：每个 `.vue` 文件把 template、script、style 封装在一个文件里，`<script setup>` 语法是推荐的简洁写法
- **响应式 ref 与计算属性**：`ref()` 和 `reactive()` 创建响应式状态，`computed()` 派生自动更新的值，理解响应式是追踪数据流的关键
- **provide/inject 深层传值**：`provide()` 与 `inject()` 无需逐层传 prop 即可沿组件树向下传值，由此产生的隐式依赖应记录为边
