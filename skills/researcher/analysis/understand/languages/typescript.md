> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/typescript.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# TypeScript 语言提示词片段

## 核心概念

- **泛型**：参数化类型（`<T>`），实现可复用、类型安全的抽象
- **类型守卫**：运行时检查，在条件块内收窄类型（`is`、`in`、`typeof`、`instanceof`）
- **可辨识联合**：带共享字面量字段的联合类型，用于穷尽收窄
- **工具类型**：`Partial<T>`、`Pick<T, K>`、`Omit<T, K>`、`Record<K, V>` 等内置映射类型
- **接口与类型别名**：接口支持声明合并，类型别名支持联合与映射类型
- **枚举**：数字与字符串枚举表示命名常量集合；可能时优先用 `as const` 对象
- **映射类型**：用 `[K in keyof T]` 语法逐属性变换已有类型
- **条件类型**：`T extends U ? X : Y` 实现类型层分支逻辑
- **模板字面量类型**：用反引号语法在类型层操作字符串
- **声明合并**：同名接口自动合并成员
- **模块扩充**：用 `declare module` 块扩展第三方模块类型

## 导入模式

- `import { X } from 'module'`：具名导入（最常见）
- `import type { X } from 'module'`：仅类型导入（运行时擦除）
- `import * as X from 'module'`：命名空间导入
- `import X from 'module'`：默认导入

## 文件模式

- `index.ts`：barrel 文件，从目录再导出公共 API
- `*.d.ts`：类型声明文件（环境声明，无运行时代码）
- `tsconfig.json`：TypeScript 编译器配置与项目引用
- `*.tsx`：包含 JSX 的 TypeScript 文件（React 组件）

## 常见框架

- **React**：带 Hook 与 JSX 的 UI 组件库
- **Angular**：带装饰器与依赖注入的全功能框架
- **Next.js**：支持 SSR、SSG 与 API 路由的 React 元框架
- **NestJS**：受 Angular 启发的服务端框架（装饰器、模块、DI）
- **Express (with TS)**：带类型化请求/响应处理器的极简 HTTP 框架

## 示例语言说明

> 用泛型参数 `T extends BaseEntity` 保证仓储方法的类型安全。约束确保
> 所有实体共享 `id` 字段，同时让具体实体类型无需强转即可流经数据层。
>
> barrel 文件（`index.ts`）再导出符号，使用者从目录导入而非深入内部
> 模块路径，维持封装。
