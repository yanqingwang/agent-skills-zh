---
name: "pr-review-expert"
description: "逐文件审查拉取请求中的缺陷、安全与质量问题，并给出是否合并的结论。当用户要求在合并前审查、查看或检查 PR 或 diff 时加载本 Skill。"
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`engineering/skills/pr-review-expert/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# PR 审查专家

**层级：** POWERFUL
**类别：** Engineering
**领域：** 代码审查 / 质量保证

---

## 概述

针对 GitHub PR 与 GitLab MR 的结构化、系统化代码审查。它不止于风格细节，本 Skill 会执行影响范围分析、安全扫描、破坏性变更检测，以及测试覆盖率增量计算，最终产出可供审查者直接使用的报告，包含 30+ 项检查清单和按优先级排序的发现。

---

## 核心能力

- **影响范围分析**：追踪哪些文件、服务和下游使用方可能受影响
- **安全扫描**：SQL 注入、XSS、认证绕过、机密泄露、依赖漏洞
- **测试覆盖率增量**：新增代码与新增测试的比例
- **破坏性变更检测**：API 契约、数据库 schema 迁移、配置键
- **工单关联**：确认 Jira/Linear 工单存在且与改动范围一致
- **性能影响**：N+1 查询、打包体积回退、内存分配

---

## 何时使用

- 在合并涉及共享库、API 或数据库 schema 的任何 PR/MR 之前
- 当 PR 较大（改动 >200 行）且需要结构化审查时
- 帮助新贡献者上手，其 PR 需要详尽反馈时
- 涉及安全的敏感代码路径（认证、支付、PII 处理）
- 事故发生后，主动审查同类 PR

---

## 获取 Diff

### GitHub (gh CLI)

```bash
# View diff in terminal
gh pr diff <PR_NUMBER>

# Get PR metadata (title, body, labels, linked issues)
gh pr view <PR_NUMBER> --json title,body,labels,assignees,milestone

# List files changed
gh pr diff <PR_NUMBER> --name-only

# Check CI status
gh pr checks <PR_NUMBER>

# Download diff to file for analysis
gh pr diff <PR_NUMBER> > /tmp/pr-<PR_NUMBER>.diff
```


### GitLab (glab CLI)

```bash
# View MR diff
glab mr diff <MR_IID>

# MR details as JSON
glab mr view <MR_IID> --output json

# List changed files
glab mr diff <MR_IID> --name-only

# Download diff
glab mr diff <MR_IID> > /tmp/mr-<MR_IID>.diff
```


---

## 工作流程

### 步骤 1：获取上下文


```bash
PR=123
gh pr view $PR --json title,body,labels,milestone,assignees | jq .
gh pr diff $PR --name-only
gh pr diff $PR > /tmp/pr-$PR.diff
```


### 步骤 2：影响范围分析

对每个改动文件，识别以下内容：

1. **直接依赖方**：谁导入了这个文件？

```bash
# Find all files importing a changed module
grep -r "from ['\"].*changed-module['\"]" src/ --include="*.ts" -l
grep -r "require(['\"].*changed-module" src/ --include="*.js" -l

# Python
grep -r "from changed_module import\|import changed_module" . --include="*.py" -l
```


2. **服务边界**：此改动是否跨服务？

```bash
# Check if changed files span multiple services (monorepo)
gh pr diff $PR --name-only | cut -d/ -f1-2 | sort -u
```


3. **共享契约**：类型、接口、schema

```bash
gh pr diff $PR --name-only | grep -E "types/|interfaces/|schemas/|models/"
```


**影响范围严重程度：**
- CRITICAL：共享库、数据库模型、认证中间件、API 契约
- HIGH：被 >3 个其他服务使用、共享配置、环境变量
- MEDIUM：单个服务内部改动、工具函数
- LOW：UI 组件、测试文件、文档

### 步骤 3：安全扫描


```bash
DIFF=/tmp/pr-$PR.diff

# SQL Injection — raw query string interpolation
grep -n "query\|execute\|raw(" $DIFF | grep -E '\$\{|f"|%s|format\('

# Hardcoded secrets
grep -nE "(password|secret|api_key|token|private_key)\s*=\s*['\"][^'\"]{8,}" $DIFF

# AWS key pattern
grep -nE "AKIA[0-9A-Z]{16}" $DIFF

# JWT secret in code
grep -nE "jwt\.sign\(.*['\"][^'\"]{20,}['\"]" $DIFF

# XSS vectors
grep -n "dangerouslySetInnerHTML\|innerHTML\s*=" $DIFF

# Auth bypass patterns
grep -n "bypass\|skip.*auth\|noauth\|TODO.*auth" $DIFF

# Insecure hash algorithms
grep -nE "md5\(|sha1\(|createHash\(['\"]md5|createHash\(['\"]sha1" $DIFF

# eval / exec
grep -nE "\beval\(|\bexec\(|\bsubprocess\.call\(" $DIFF

# Prototype pollution
grep -n "__proto__\|constructor\[" $DIFF

# Path traversal risk
grep -nE "path\.join\(.*req\.|readFile\(.*req\." $DIFF
```


### 步骤 4：测试覆盖率增量


```bash
# Count source vs test files changed
CHANGED_SRC=$(gh pr diff $PR --name-only | grep -vE "\.test\.|\.spec\.|__tests__")
CHANGED_TESTS=$(gh pr diff $PR --name-only | grep -E "\.test\.|\.spec\.|__tests__")

echo "Source files changed: $(echo "$CHANGED_SRC" | wc -w)"
echo "Test files changed:   $(echo "$CHANGED_TESTS" | wc -w)"

# Lines of new logic vs new test lines
LOGIC_LINES=$(grep "^+" /tmp/pr-$PR.diff | grep -v "^+++" | wc -l)
echo "New lines added: $LOGIC_LINES"

# Run coverage locally
npm test -- --coverage --changedSince=main 2>/dev/null | tail -20
pytest --cov --cov-report=term-missing 2>/dev/null | tail -20
```


**覆盖率增量规则：**
- 新增函数却没有对应测试 → 标记
- 删除了测试却没有删除对应代码 → 标记
- 覆盖率下降 >5% → 阻止合并
- 认证/支付路径 → 要求 100% 覆盖率

### 步骤 5：破坏性变更检测

#### API 契约变更

```bash
# OpenAPI/Swagger spec changes
grep -n "openapi\|swagger" /tmp/pr-$PR.diff | head -20

# REST route removals or renames
grep "^-" /tmp/pr-$PR.diff | grep -E "router\.(get|post|put|delete|patch)\("

# GraphQL schema removals
grep "^-" /tmp/pr-$PR.diff | grep -E "^-\s*(type |field |Query |Mutation )"

# TypeScript interface removals
grep "^-" /tmp/pr-$PR.diff | grep -E "^-\s*(export\s+)?(interface|type) "
```


#### 数据库 schema 变更

```bash
# Migration files added
gh pr diff $PR --name-only | grep -E "migrations?/|alembic/|knex/"

# Destructive operations
grep -E "DROP TABLE|DROP COLUMN|ALTER.*NOT NULL|TRUNCATE" /tmp/pr-$PR.diff

# Index removals (perf regression risk)
grep "DROP INDEX\|remove_index" /tmp/pr-$PR.diff
```


#### 配置 / 环境变量变更

```bash
# New env vars referenced in code (might be missing in prod)
grep "^+" /tmp/pr-$PR.diff | grep -oE "process\.env\.[A-Z_]+" | sort -u

# Removed env vars (could break running instances)
grep "^-" /tmp/pr-$PR.diff | grep -oE "process\.env\.[A-Z_]+" | sort -u
```


### 步骤 6：性能影响


```bash
# N+1 query patterns (DB calls inside loops)
grep -n "\.find\|\.findOne\|\.query\|db\." /tmp/pr-$PR.diff | grep "^+" | head -20
# Then check surrounding context for forEach/map/for loops

# Heavy new dependencies
grep "^+" /tmp/pr-$PR.diff | grep -E '"[a-z@].*":\s*"[0-9^~]' | head -20

# Unbounded loops
grep -n "while (true\|while(true" /tmp/pr-$PR.diff | grep "^+"

# Missing await (accidentally sequential promises)
grep -n "await.*await" /tmp/pr-$PR.diff | grep "^+" | head -10

# Large in-memory allocations
grep -n "new Array([0-9]\{4,\}\|Buffer\.alloc" /tmp/pr-$PR.diff | grep "^+"
```


---

## 工单关联验证


```bash
# Extract ticket references from PR body
gh pr view $PR --json body | jq -r '.body' | \
  grep -oE "(PROJ-[0-9]+|[A-Z]+-[0-9]+|https://linear\.app/[^)\"]+)" | sort -u

# Verify Jira ticket exists (requires JIRA_API_TOKEN to be SET in the environment).
# Credentials are fed to curl via a config read from stdin (-K -) so the token
# never appears in argv — `ps aux` / /proc/*/cmdline can't see it, and nothing
# secret lands in shell history. Never paste the raw token on the command line.
TICKET="PROJ-123"
: "${JIRA_API_TOKEN:?JIRA_API_TOKEN must be set}"
curl -s -K - "https://your-org.atlassian.net/rest/api/3/issue/$TICKET" <<EOF | \
  jq '{key, summary: .fields.summary, status: .fields.status.name}'
user = "user@company.com:$JIRA_API_TOKEN"
EOF

# Linear ticket — same pattern: the Authorization header goes through the
# stdin config, not a -H flag, to keep the key out of the process list.
LINEAR_ID="abc-123"
: "${LINEAR_API_KEY:?LINEAR_API_KEY must be set}"
curl -s -K - -H "Content-Type: application/json" \
  --data "{\"query\": \"{ issue(id: \\\"$LINEAR_ID\\\") { title state { name } } }\"}" \
  https://api.linear.app/graphql <<EOF | jq .
header = "Authorization: $LINEAR_API_KEY"
EOF
```


> **安全提示：** 如需反复使用 Jira，建议使用 `~/.netrc` 条目
> （`machine your-org.atlassian.net login user@company.com password <token>`，
> `chmod 600 ~/.netrc`），并调用 `curl -s --netrc …`，命令中完全不含
> 任何机密信息。

---

## 完整审查清单（30+ 项）


```markdown
## Code Review Checklist

### Scope & Context
- [ ] PR title accurately describes the change
- [ ] PR description explains WHY, not just WHAT
- [ ] Linked Jira/Linear ticket exists and matches scope
- [ ] No unrelated changes (scope creep)
- [ ] Breaking changes documented in PR body

### Blast Radius
- [ ] Identified all files importing changed modules
- [ ] Cross-service dependencies checked
- [ ] Shared types/interfaces/schemas reviewed for breakage
- [ ] New env vars documented in .env.example
- [ ] DB migrations are reversible (have down() / rollback)

### Security
- [ ] No hardcoded secrets or API keys
- [ ] SQL queries use parameterized inputs (no string interpolation)
- [ ] User inputs validated/sanitized before use
- [ ] Auth/authorization checks on all new endpoints
- [ ] No XSS vectors (innerHTML, dangerouslySetInnerHTML)
- [ ] New dependencies checked for known CVEs
- [ ] No sensitive data in logs (PII, tokens, passwords)
- [ ] File uploads validated (type, size, content-type)
- [ ] CORS configured correctly for new endpoints

### Testing
- [ ] New public functions have unit tests
- [ ] Edge cases covered (empty, null, max values)
- [ ] Error paths tested (not just happy path)
- [ ] Integration tests for API endpoint changes
- [ ] No tests deleted without clear reason
- [ ] Test names clearly describe what they verify

### Breaking Changes
- [ ] No API endpoints removed without deprecation notice
- [ ] No required fields added to existing API responses
- [ ] No DB columns removed without two-phase migration plan
- [ ] No env vars removed that may be set in production
- [ ] Backward-compatible for external API consumers

### Performance
- [ ] No N+1 query patterns introduced
- [ ] DB indexes added for new query patterns
- [ ] No unbounded loops on potentially large datasets
- [ ] No heavy new dependencies without justification
- [ ] Async operations correctly awaited
- [ ] Caching considered for expensive repeated operations

### Code Quality
- [ ] No dead code or unused imports
- [ ] Error handling present (no bare empty catch blocks)
- [ ] Consistent with existing patterns and conventions
- [ ] Complex logic has explanatory comments
- [ ] No unresolved TODOs (or tracked in ticket)
```


---

## 输出格式

按以下结构组织你的审查评论：


```
## PR Review: [PR Title] (#NUMBER)

Blast Radius: HIGH — changes lib/auth used by 5 services
Security: 1 finding (medium severity)
Tests: Coverage delta +2%
Breaking Changes: None detected

--- MUST FIX (Blocking) ---

1. SQL Injection risk in src/db/users.ts:42
   Raw string interpolation in WHERE clause.
   Fix: db.query("SELECT * WHERE id = $1", [userId])

--- SHOULD FIX (Non-blocking) ---

2. Missing auth check on POST /api/admin/reset
   No role verification before destructive operation.

--- SUGGESTIONS ---

3. N+1 pattern in src/services/reports.ts:88
   findUser() called inside results.map() — batch with findManyUsers(ids)

--- LOOKS GOOD ---
- Test coverage for new auth flow is thorough
- DB migration has proper down() rollback method
- Error handling consistent with rest of codebase
```


---

## 常见陷阱

- **重风格轻实质**：让 lint 工具处理风格，把精力放在逻辑、安全与正确性上
- **忽视影响范围**：共享工具里 5 行的改动可能破坏 20 个服务
- **批准未经测试的正常路径**：始终确认错误路径已被覆盖
- **忽视迁移风险**：新增 NOT NULL 列需要默认值或两阶段迁移
- **间接机密泄露**：机密出现在错误信息/日志中，而不只是硬编码值里
- **跳过大型 PR**：如果 PR 太大难以妥善审查，应要求拆分

---

## 最佳实践

1. 看代码前先读关联的工单，上下文有助于避免误报
2. 审查前先检查 CI 状态，不要审查构建失败的代码
3. 优先关注影响范围与安全，而非风格
4. 对非简单的认证或性能改动，在本地复现
5. 为每条评论清晰标注："nit:"、"must:"、"question:"、"suggestion:"
6. 把所有评论集中在一次审查中，不要零碎地给出反馈
7. 既肯定好的做法，也指出问题，具体的表扬有助于改善团队文化
