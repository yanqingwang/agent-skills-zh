> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/code-reviewer/references/feedback-examples.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 反馈示例

## 好反馈与坏反馈

### 要具体，不要含糊

```markdown
BAD: "This is confusing"

GOOD: "This function handles both validation and persistence. Consider
      splitting into `validateUser()` and `saveUser()` for single
      responsibility and easier testing."
```

### 要可执行，不要只批评

```markdown
BAD: "Fix the query"

GOOD: "This will cause N+1 queries - one per post. Use `include: [Author]`
      to eager load authors in a single query. See: [link to docs]"
```

### 要有建设性，不要颐指气使

```markdown
BAD: "Add tests"

GOOD: "Missing test for the case when `email` is already taken. Add a test
      that verifies 409 is returned with appropriate error message."
```

### 要提问，不要臆断

```markdown
BAD: "This is wrong"

GOOD: "I notice this returns null instead of throwing. Is that intentional?
      The other methods throw on not-found. Should this be consistent?"
```

## 表扬示例

用具体的表扬强化好模式：

```markdown
"Great use of early returns here - much more readable than nested ifs!"

"Nice extraction of this validation logic into a reusable function."

"Excellent error messages - they'll help debugging in production."

"Good choice using a discriminated union here instead of optional fields."

"Appreciate the comprehensive test coverage, especially the edge cases."
```

## 按类别划分的反馈

### Critical（必须修复）

```markdown
**[CRITICAL] Security: SQL Injection**
Location: `src/users/service.ts:45`

The query uses string interpolation:
`SELECT * FROM users WHERE id = ${id}`

This is vulnerable to SQL injection. Use parameterized query:
`db.query('SELECT * FROM users WHERE id = $1', [id])`
```

### Major（应当修复）

```markdown
**[MAJOR] Performance: N+1 Query**
Location: `src/posts/service.ts:23`

Current code fetches users in a loop (N+1 problem):
```typescript
for (const post of posts) {
  post.author = await User.findById(post.authorId);
}
```

Suggestion: Use eager loading:
```typescript
const posts = await Post.findAll({ include: [User] });
```

Impact: ~100 extra DB queries per request with current approach.
```

### Minor（锦上添花）

```markdown
**[MINOR] Naming: Unclear variable**
Location: `src/utils/date.ts:12`

`d` is unclear. Consider `createdDate` or `timestamp` for better readability.

**[MINOR] Style: Prefer const**
Location: `src/config/index.ts:8`

`let config` is never reassigned. Use `const` for immutability.
```

## 提问格式

```markdown
**[QUESTION]**
Location: `src/orders/service.ts:67`

What's the expected behavior when the user has an existing pending order?
Should this:
- Return the existing order?
- Create a new one anyway?
- Return an error?
```

## 总结格式

```markdown
## Summary

Overall this is a solid implementation of the user registration flow.
The validation logic is clean and the error handling is comprehensive.

**Blocking Issues**: 1 critical (SQL injection)
**Suggestions**: 2 major, 3 minor

Once the SQL injection is fixed, this is ready to merge. The major
suggestions are performance improvements worth considering.
```

## 速查表

| 反馈类型 | 语气 | 要求的动作 |
|---------------|------|-----------------|
| Critical | 坚定、清晰 | 合并前必须修复 |
| Major | 建议式 | 应当修复 |
| Minor | 可选 | 锦上添花 |
| Praise | 正面 | 无（起强化作用） |
| Question | 好奇 | 需要回应 |
