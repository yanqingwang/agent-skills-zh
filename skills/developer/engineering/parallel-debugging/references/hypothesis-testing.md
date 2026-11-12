> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/agent-teams/skills/parallel-debugging/references/hypothesis-testing.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 假设检验参考

并行调试的任务模板、证据格式与仲裁决策树。

## 假设任务模板

```markdown
## Hypothesis Investigation: {Hypothesis Title}

### Hypothesis Statement

{Clear, falsifiable statement about the root cause}

### Failure Mode Category

{Logic Error | Data Issue | State Problem | Integration Failure | Resource Issue | Environment}

### Investigation Scope

- Files to examine: {file list or directory}
- Related tests: {test files}
- Git history: {relevant date range or commits}

### Evidence Criteria

**Confirming evidence** (if I find these, hypothesis is supported):

1. {Observable condition 1}
2. {Observable condition 2}

**Falsifying evidence** (if I find these, hypothesis is wrong):

1. {Observable condition 1}
2. {Observable condition 2}

### Report Format

- Confidence: High/Medium/Low
- Evidence: list with file:line citations
- Causal chain: step-by-step from cause to symptom
- Recommended fix: if confirmed
```

## 证据报告模板

```markdown
## Investigation Report: {Hypothesis Title}

### Verdict: {Confirmed | Falsified | Inconclusive}

### Confidence: {High (>80%) | Medium (50-80%) | Low (<50%)}

### Confirming Evidence

1. `src/api/users.ts:47` — {description of what was found}
2. `src/middleware/auth.ts:23` — {description}

### Contradicting Evidence

1. `tests/api/users.test.ts:112` — {description of what contradicts}

### Causal Chain (if confirmed)

1. {First cause} →
2. {Intermediate effect} →
3. {Observable symptom}

### Recommended Fix

{Specific code change with location}

### Additional Notes

{Anything discovered that may be relevant to other hypotheses}
```

## 仲裁决策树

```
All investigators reported?
├── NO → Wait for remaining reports
└── YES → Count confirmed hypotheses
          ├── 0 confirmed
          │   ├── Any medium confidence? → Investigate further
          │   └── All low/falsified? → Generate new hypotheses
          ├── 1 confirmed
          │   └── High confidence?
          │       ├── YES → Declare root cause, propose fix
          │       └── NO → Flag as likely cause, recommend verification
          └── 2+ confirmed
              └── Are they related?
                  ├── YES → Compound issue (multiple contributing causes)
                  └── NO → Rank by confidence, declare highest as primary
```

## 按错误类型的常见假设模式

### "500 内部服务器错误"（500 Internal Server Error）

1. 请求处理器中存在未处理的异常（Logic Error）
2. 数据库连接失败（Resource Issue）
3. 环境变量缺失（Environment）

### "竞态条件 / 间歇性失败"（Race condition / intermittent failure）

1. 共享状态在无锁情况下被修改（State Problem）
2. 对异步操作顺序的错误假设（Logic Error）
3. 缓存陈旧窗口期（State Problem）

### "本地正常，生产环境失败"（Works locally, fails in production）

1. 环境变量不一致（Environment）
2. 依赖版本不同（Environment）
3. 资源限制（内存、连接数）（Resource Issue）

### "部署后出现回归"（Regression after deploy）

1. 新代码引入了 bug（Logic Error）
2. 配置变更（Integration Failure）
3. 数据库迁移问题（Data Issue）
