> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/review/specialists/maintainability.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Maintainability Specialist 评审清单

范围：Always-on（每次评审）
输出：JSON 对象，每条发现一行。Schema：
{"severity":"INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"maintainability","summary":"...","fix":"...","fingerprint":"path:line:maintainability","specialist":"maintainability"}
可选字段：line、fix、fingerprint、evidence、test_stub。
若无发现：只输出 `NO FINDINGS`，不输出任何其他内容。

---

## 类别

### 死代码与无用 import
- 被赋值但从未读取的变量（限被改动文件）
- 定义了却从未调用的函数/方法（用 Grep 全仓检查）
- 变更后不再被引用的 import/require
- 被注释掉的代码块（要么删除，要么说明它为何存在）

### 魔法数字与字符串耦合
- 逻辑中使用的裸数字字面量（阈值、上限、重试次数），应为具名常量
- 被别处用作查询过滤条件或分支条件的错误信息字符串
- 应进 config 的硬编码 URL、端口或主机名
- 多个文件中重复的字面量值

### 过时注释与 docstring
- 本 diff 改动代码后仍描述旧行为的注释
- 引用已完成工作的 TODO/FIXME 注释
- 参数列表与当前函数签名不符的 docstring
- 与代码流程不再匹配的注释内 ASCII 图
- 守卫条件在本 diff 中变了、文案却没变的用户可见字符串（错误、toast、标签）

### 带缺陷的重复行为
- 会产生已证实的错误结果、漏掉必需的错误处理、或违反同一契约的分叉副本
- 通过正常的 Fix-First 流程报告具体缺陷及其证据；仅凭语法相似或重复行数不构成发现
- 可选的共享 helper 抽取属于核心共享代码检查。不要重复它的提案，也不要把结构性偏好当成缺陷

### 条件性副作用
- 按条件分支、却在某个分支上遗漏副作用的代码路径
- 声称某操作已发生、而该操作实际被条件跳过的日志消息
- 一个分支更新关联记录、另一个分支不更新的状态转换
- 只在 happy path 触发、漏掉错误/边界路径的事件发送

### 模块边界违规
- 伸进另一模块的内部实现（访问按约定私有的方法）
- controller/view 中本应经由 service/model 的直接数据库查询
- 本应通过接口通信的组件之间紧耦合
