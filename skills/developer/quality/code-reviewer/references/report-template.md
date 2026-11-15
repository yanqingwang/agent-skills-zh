> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/code-reviewer/references/report-template.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 报告模板

## 完整审查报告模板

```markdown
# Code Review: [PR Title]

## Summary
[1-2 sentence overview of the changes and overall assessment]

**Verdict**: [ ] Approve | [x] Request Changes | [ ] Comment

## Critical Issues (Must Fix)

### 1. [File:Line] Security: SQL Injection Risk
- **Current**: String interpolation in query
- **Suggested**: Use parameterized query
- **Impact**: Potential data breach

```typescript
// Current (vulnerable)
const query = `SELECT * FROM users WHERE id = ${id}`;

// Suggested (secure)
const query = 'SELECT * FROM users WHERE id = $1';
db.query(query, [id]);
```

## Major Issues (Should Fix)

### 1. [File:Line] Performance: N+1 Query
- **Current**: Fetching users in loop
- **Suggested**: Use eager loading with include
- **Impact**: ~100 extra DB queries per request

### 2. [File:Line] Logic: Missing edge case
- **Current**: No handling for empty array
- **Suggested**: Add guard clause
- **Impact**: Potential runtime error

## Minor Issues (Nice to Have)

### 1. [File:Line] Naming: Unclear variable name
- **Current**: `d`
- **Suggested**: `createdDate`

### 2. [File:Line] Style: Inconsistent formatting
- **Current**: Mixed quotes
- **Suggested**: Use single quotes consistently

## Positive Feedback
- Clean separation of concerns in service layer
- Comprehensive input validation on DTOs
- Good test coverage for edge cases
- Excellent error messages

## Questions for Author
- What's the expected behavior when X happens?
- Should this support pagination for large datasets?
- Is the retry logic intentional or accidental?

## Test Coverage Assessment
- [ ] Happy path tested
- [x] Error cases tested
- [ ] Edge cases tested (missing empty array test)
- [x] Integration tests present

## Checklist
- [x] No security vulnerabilities
- [ ] Performance is acceptable (N+1 issue)
- [x] Code is readable
- [x] Tests are adequate
- [x] Documentation is present
```

## 结论指南

| 结论 | 使用时机 |
|---------|-------------|
| **Approve** | 没有阻断性问题，只有少量建议 |
| **Request Changes** | 存在必须修复的严重或重要问题 |
| **Comment** | 有问题需要答复，但无阻断性问题 |

## 严重级别定义

| 严重级别 | 定义 | 示例 |
|----------|------------|----------|
| **Critical** | 安全风险、数据丢失、崩溃 | SQL 注入、鉴权绕过 |
| **Major** | 明显的性能或可维护性问题 | N+1 查询、上帝函数 |
| **Minor** | 风格、命名、小幅改进 | 变量名、格式 |

## 时间盒

| 环节 | 建议时长 |
|---------|----------------|
| 背景与理解 | 5 分钟 |
| 严重问题/安全审查 | 10 分钟 |
| 逻辑与性能 | 15 分钟 |
| 测试审查 | 10 分钟 |
| 撰写报告 | 10 分钟 |
| **总计** | 约 50 分钟 |

## 提交前快速检查

- [ ] 所有严重问题都有明确的修复办法
- [ ] 重要问题都说明了影响
- [ ] 至少包含一条正面评价
- [ ] 问题具体且可回答
- [ ] 结论与发现的问题一致
