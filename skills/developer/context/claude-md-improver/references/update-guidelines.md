> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/claude-md-management/skills/claude-md-improver/references/update-guidelines.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# CLAUDE.md 更新指南

## 核心原则

只添加能真正帮助未来 Claude 会话的信息。context window 十分宝贵，每一行都必须配得上自己的位置。

## 应该添加什么

### 1. 分析过程中发现的命令/工作流

```markdown
## Build

`npm run build:prod` - Full production build with optimization
`npm run build:dev` - Fast dev build (no minification)
```

理由：省得未来的会话再摸索一遍。

### 2. 坑点与非显而易见的模式

```markdown
## Gotchas

- Tests must run sequentially (`--runInBand`) due to shared DB state
- `yarn.lock` is authoritative; delete `node_modules` if deps mismatch
```

理由：避免再经历一轮重复的调试。

### 3. 包之间的关系

```markdown
## Dependencies

The `auth` module depends on `crypto` being initialized first.
Import order matters in `src/bootstrap.ts`.
```

理由：从代码里一眼看不出来的架构知识。

### 4. 行之有效的测试方法

```markdown
## Testing

For API endpoints: Use `supertest` with the test helper in `tests/setup.ts`
Mocking: Factory functions in `tests/factories/` (not inline mocks)
```

理由：沉淀有效的模式。

### 5. 配置上的怪癖

```markdown
## Config

- `NEXT_PUBLIC_*` vars must be set at build time, not runtime
- Redis connection requires `?family=0` suffix for IPv6
```

理由：环境专属的知识。

## 不该添加什么

### 1. 代码中显而易见的信息

反例：
```markdown
The `UserService` class handles user operations.
```

类名本身已经说明了这一点。

### 2. 通用的最佳实践

反例：
```markdown
Always write tests for new features.
Use meaningful variable names.
```

这是普遍适用的建议，不是项目专属信息。

### 3. 一次性修复

反例：
```markdown
We fixed a bug in commit abc123 where the login button didn't work.
```

不会复现，只会让文件变乱。

### 4. 冗长的解释

反例：
```markdown
The authentication system uses JWT tokens. JWT (JSON Web Tokens) are
an open standard (RFC 7519) that defines a compact and self-contained
way for securely transmitting information between parties as a JSON
object. In our implementation, we use the HS256 algorithm which...
```

正例：
```markdown
Auth: JWT with HS256, tokens in `Authorization: Bearer <token>` header.
```

## 更新的 Diff 格式

对每处建议的修改：

### 1. 指明文件

```
File: ./CLAUDE.md
Section: Commands (new section after ## Architecture)
```

### 2. 展示修改内容

```diff
 ## Architecture
 ...

+## Commands
+
+| Command | Purpose |
+|---------|---------|
+| `npm run dev` | Dev server with HMR |
+| `npm run build` | Production build |
+| `npm test` | Run test suite |
```

### 3. 说明理由

> **为什么有帮助：** 构建命令此前没有记录，导致不清楚如何运行项目。这省得未来会话再去翻 `package.json`。

## 校验清单

定稿更新之前，逐项核对：

- [ ] 每条增补都是项目专属信息
- [ ] 没有通用建议或显而易见的信息
- [ ] 命令经过测试且确实可用
- [ ] 文件路径准确无误
- [ ] 新的 Claude 会话会觉得这些内容有帮助吗？
- [ ] 这是不是表达该信息最精炼的方式？
