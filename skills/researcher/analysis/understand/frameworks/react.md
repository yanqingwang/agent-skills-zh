> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/frameworks/react.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# React 框架补充说明

> 检测到 React 时，将本文件注入 file-analyzer 与 architecture-analyzer 的提示词。
> 请勿单独作为提示词使用：必须始终附加在基础提示词模板之后。

## React 项目结构

分析 React 项目时，在基础分析规则之上应用以下附加约定。

### 规范文件角色

| 文件 / 模式 | 角色 | 标签 |
|---|---|---|
| `src/App.tsx` | 根应用组件：挂载 Provider、路由与顶层布局 | `entry-point`, `ui` |
| `components/*.tsx`, `components/**/*.tsx` | 可复用 UI 组件 | `ui` |
| `hooks/*.ts`, `hooks/*.tsx` | 自定义 React Hook：封装可复用的有状态逻辑 | `service`, `utility` |
| `contexts/*.tsx`, `context/*.tsx` | React Context 提供者与消费者：跨组件树共享状态 | `service`, `state` |
| `pages/*.tsx`, `views/*.tsx` | 映射到路由的页面级组件 | `ui`, `routing` |
| `utils/*.ts`, `helpers/*.ts` | 纯工具函数：格式化、校验、转换 | `utility` |
| `types/*.ts`, `types/*.d.ts` | TypeScript 类型定义与接口 | `type-definition` |
| `services/*.ts`, `api/*.ts` | API 客户端函数与数据获取逻辑 | `service` |
| `store/*.ts`, `slices/*.ts` | 状态管理（Redux、Zustand 等） | `service`, `state` |
| `constants/*.ts` | 应用级常量与枚举 | `config` |
| `__tests__/*.tsx`, `*.test.tsx`, `*.spec.tsx` | 单元测试与集成测试 | `test` |

### 需要关注的边模式

**组件组合**：当父组件在其 JSX 返回中渲染子组件时，从父到子创建 `contains` 边。这些边构成组件树层级。

**Hook 使用**：当组件或 Hook 导入并调用自定义 Hook（`useX`）时，从消费方到该 Hook 模块创建 `depends_on` 边。Hook 是 React 中共享逻辑的主要机制。

**Context 提供者/消费者**：当 Context 提供者包裹组件时，从提供者到 Context 定义创建 `publishes` 边。当组件调用 `useContext` 或使用自定义 Context Hook 时，从消费者到该 Context 创建 `subscribes` 边。

**Props 逐层透传链**：当 props 穿过多层组件却未被中间层使用时，沿该链创建 `depends_on` 边，暴露耦合深度。

### React 的架构分层

检测到时，将节点归入以下层：

| 层 ID | 层名称 | 包含内容 |
|---|---|---|
| `layer:ui` | UI 层 | `components/`、`pages/`、`views/`、布局组件 |
| `layer:service` | 服务层 | `hooks/`、`contexts/`、`services/`、`api/`、`store/` |
| `layer:types` | 类型层 | `types/`、共享 TypeScript 接口与类型定义 |
| `layer:utility` | 工具层 | `utils/`、`helpers/`、纯函数 |
| `layer:config` | 配置层 | `App.tsx`、路由配置、Provider 设置、常量 |
| `layer:test` | 测试层 | `__tests__/`、`*.test.tsx`、`*.spec.tsx` |

### 需记录到 languageLesson 的重点模式

- **组件组合优于继承**：React 偏好通过 props 与 children 组合组件，而非类继承层级
- **自定义 Hook 承载可复用逻辑**：以 `use` 为前缀的 Hook 把有状态逻辑提取为可共享的模块，且不改变组件树
- **React.memo 用于性能**：包在 `React.memo` 里的组件在 props 不变时跳过重渲染，提示这是性能敏感路径
- **受控与非受控组件**：受控组件的状态来自 props，非受控组件用 ref 管理内部状态
- **Render props 模式**：组件接受函数作为 children 或 render prop，把渲染决策委托给消费方
