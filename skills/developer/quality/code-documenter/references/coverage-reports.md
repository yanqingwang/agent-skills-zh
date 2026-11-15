> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/developer/quality/code-documenter/references/coverage-reports.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 覆盖率报告

## 文档覆盖率报告模板

```markdown
# Documentation Report: {project_name}

## Summary
- **Files analyzed**: 45
- **Functions documented**: 120/150 (80%)
- **Classes documented**: 25/25 (100%)
- **API endpoints documented**: 30/30 (100%)

## Coverage Before/After
- Before: 45%
- After: 92%

## Files Modified

| File | Functions Added | Notes |
|------|-----------------|-------|
| src/services/user.ts | 8 | All public methods |
| src/services/auth.ts | 5 | Added examples |
| src/controllers/users.ts | 6 | Added @Api decorators |
| src/dto/user.dto.ts | 4 | Added @ApiProperty |

## API Documentation

- **Framework**: NestJS
- **Strategy**: @nestjs/swagger decorators
- **Swagger UI**: /api/docs
- **OpenAPI spec**: /api-json

## Documentation Style

- **Python**: Google style docstrings
- **TypeScript**: JSDoc with @param, @returns
- **API**: OpenAPI 3.0 via decorators

## Next Steps

### Recommendations
1. Run `npm run docs:lint` to validate JSDoc
2. Add `eslint-plugin-jsdoc` to enforce documentation
3. Consider adding examples for complex functions
4. Set up documentation CI checks

### Missing Documentation
| File | Missing | Priority |
|------|---------|----------|
| src/utils/crypto.ts | 3 functions | High |
| src/helpers/date.ts | 2 functions | Medium |

### CI Integration
```yaml
# Add to CI pipeline
- name: Check documentation
  run: npm run docs:check

- name: Generate API docs
  run: npm run docs:generate
```
```

## 文档编写检查清单

```markdown
## Documentation Checklist

### Before Starting
- [ ] Confirmed format preference (Google/JSDoc/etc.)
- [ ] Identified files to exclude (tests, generated)
- [ ] Detected framework for API docs

### Functions/Methods
- [ ] All public functions documented
- [ ] Parameters described with types
- [ ] Return values documented
- [ ] Exceptions/errors documented
- [ ] Examples added for complex functions

### Classes
- [ ] Class purpose described
- [ ] Constructor parameters documented
- [ ] Public methods documented
- [ ] Important attributes explained

### API Endpoints
- [ ] All endpoints have summaries
- [ ] Request bodies documented
- [ ] Response schemas defined
- [ ] Error responses documented
- [ ] Authentication requirements noted

### Final Checks
- [ ] Ran documentation linter
- [ ] Verified Swagger UI renders correctly
- [ ] No inaccurate documentation
- [ ] Coverage report generated
```

## 按框架做 lint

```bash
# JavaScript/TypeScript - ESLint
npm install eslint-plugin-jsdoc --save-dev
# Add to .eslintrc: "plugins": ["jsdoc"]

# Python - pydocstyle
pip install pydocstyle
pydocstyle --convention=google src/

# Python - interrogate (coverage)
pip install interrogate
interrogate -v src/
```

## 速查表

| 指标 | 良好 | 可接受 | 较差 |
|--------|------|------------|------|
| 函数覆盖率 | >90% | 70-90% | <70% |
| 类覆盖率 | 100% | >90% | <90% |
| API 端点覆盖率 | 100% | 100% | <100% |
| 示例覆盖率 | >50% | 30-50% | <30% |
