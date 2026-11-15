> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/researcher/analysis/understand/languages/javascript.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# JavaScript 语言提示词片段

## 核心概念

- **闭包**：捕获外层词法作用域变量的函数
- **原型**：所有 JavaScript 对象底层的原型链继承
- **Promise**：异步值容器，支持 `.then()` 链与 `async/await`
- **事件循环**：带微任务与宏任务队列的单线程并发模型
- **解构**：把对象与数组中的值提取到独立变量
- **展开/剩余运算符**：`...` 用于展开可迭代对象或收集剩余参数
- **Proxy**：元编程构造，拦截并定制对象操作
- **生成器**：用 `function*` 与 `yield` 实现惰性迭代
- **Symbol**：唯一且不可变的基本类型，用作非字符串属性键
- **WeakMap/WeakSet**：键为弱引用的集合，允许垃圾回收
- **模块（ESM 与 CJS）**：ES Modules 用 `import/export`，CommonJS 用 `require/module.exports`

## 导入模式

- `import { X } from 'module'`：ESM 具名导入
- `const X = require('module')`：CommonJS require
- `import('module')`：动态导入，返回 Promise（代码分割）
- `export default X` / `export { X }`：ESM 导出形式

## 文件模式

- `index.js`：barrel 文件或目录入口
- `.mjs`：显式 ES Module 文件
- `.cjs`：显式 CommonJS 文件
- `package.json` 的 `"type"` 字段：设定默认模块系统（`"module"` 或 `"commonjs"`）

## 常见框架

- **React**：带虚拟 DOM 与组件模型的声明式 UI
- **Vue**：带响应式系统与单文件组件的渐进式框架
- **Express**：极简灵活的 Node.js Web 应用框架
- **Next.js**：面向生产、支持混合渲染的 React 框架
- **Svelte**：把工作从运行时转到构建期的编译时框架

## 示例语言说明

> 闭包捕获外层 `config` 变量，无需类的开销即提供封装状态。返回对象的
> 方法共享同一个 `config` 引用，构成 ES Modules 普及前的标准模块模式。
>
> 遇到 `.mjs` 与 `.cjs` 扩展名时，模块系统由扩展名决定，与 `package.json`
> 的 type 字段无关，在混合代码库中很有用。
