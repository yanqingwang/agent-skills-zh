<!-- AUTO-GENERATED from pr-body.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`ship/sections/pr-body.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

### 准备标题（Step 18）

把标题写进私有文件；Step 19 发的是那个文件，绝不是 shell 字符串：

```bash
_GT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp"
mkdir -p "$_GT" && chmod 700 "$_GT" || { echo "Not sent: cannot create $_GT for the text file." >&2; exit 1; }
_EX=$(git rev-parse --git-path info/exclude 2>/dev/null) && mkdir -p "$(dirname "$_EX")" && { grep -qxF '/.gstack/tmp/' "$_EX" 2>/dev/null || echo '/.gstack/tmp/' >> "$_EX"; }
TITLE_FILE=$(mktemp "${_GT:?}/pr-title.XXXXXX") || { echo "Not sent: mktemp failed in $_GT." >&2; exit 1; }; echo "TITLE_FILE: $TITLE_FILE (name: ${TITLE_FILE##*/})"
```

用你的文件写入工具把文本写进每个打印出的文件（Claude Code 的 Write
工具需要先 Read 一次空文件），内容与应出现的一字不差。文本绝不进
shell 命令、heredoc 或带引号参数。写入失败或被拒时不发送：打印原
因、文件路径和下方命令，供手工发送。

1. 已有开放 PR/MR 时（不是 Step 6.5 的提前 PR，它走第 2 条），从平台
   填充该文件，替换打印名、匹配到的编号与 `NEW_VERSION`；标题文本不
   经过你：
   ```bash
   TITLE_FILE="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp/<title-file-name>"
   gh pr view <pr-number> --json title -q .title | ~/.claude/skills/gstack/bin/gstack-pr-title-rewrite.sh <new-version> --stdin > "$TITLE_FILE" || exit 1
   ```
   GitLab 把 `glab mr view <pr-number> --output json | jq -r .title`
   接进同一管道。
2. 新 PR/MR 时，用文件写入工具把 `v<NEW_VERSION> <type>: <summary>`
   写进文件。
3. 每个新建或更新的标题必须以 `v$NEW_VERSION ` 开头；用
   `grep -Eq '^v<new-version>( |$)' "$TITLE_FILE"` 检查，绝不发布无
   前缀标题。
4. **NO_VERSION：**替代第 1-3 条：保留既有标题（平台标题直接管道进
   文件），或写 `<type>: <summary>`；无版本前缀。

保存标题文件名供 Step 19 使用。

---

## Step 19：创建 PR/MR

复查 Step 18 的 PR/MR 查找并记录。出错或匹配歧义会 STOP 发布。
开放 PR/MR 或标题变了，重复 Step 18 的身份/标题准备，然后回到这里重
新查找并写新正文再发布。

### 组装正文前解析 Linked Spec

1. 解析归档目录与分支：
   ```bash
   GSTACK_STATE_ROOT=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT); : "${GSTACK_STATE_ROOT:?gstack-paths failed; reinstall with ./setup or /gstack-upgrade}"
   SLUG=$(~/.claude/skills/gstack/bin/gstack-slug --get SLUG)
   CURRENT_BRANCH=$(git branch --show-current)
   SPEC_ARCHIVES="$GSTACK_STATE_ROOT/projects/$SLUG/specs"
   ```
2. 把归档 frontmatter 当数据读，绝不当 shell 源码。选与
   `CURRENT_BRANCH` 精确匹配 `spec_branch` 的；多个匹配取最新
   `spec_filed_at`。绝不从分支名推断 issue 编号。无可读匹配或非正整
   数 `spec_issue_number` 时，只省略 `## Linked Spec` 并继续组装
   PR。歧义匹配在链接 issue 之前解决。
3. 把该 spec 的验收标准与 Step 8 的结果对比。只有 Step 8 计划范围全
   部完成、且每条 spec 标准都验证过，才允许 `Closes #N`。部分、推
   迟、失败、放弃或未验证的范围用 `Linked to #N` 并点名剩余工作；
   绝不自动关闭。写归档文件名与 `spec_filed_at`，不写私有绝对路径；
   `gstack-post` 会随正文扫描它们。

### Issue 链接

跑 `~/.claude/skills/gstack/bin/gstack-issue-links --base <base> --out .gstack/tmp/issues.json`，
用户点名为已修复的 issue 每个加 `--issue <n>`，失败的 CI 运行每个加
`--ci-run <id>`。交互式：对它的 `(promote: fix #N)` 引用问一次（每个
`fix #<n>` 回复加 `--issue <n>`），`Related:` PR 的
`--supersedes <n>`/`--credit <n>` 仅在 owner 确认时加；任何变更后重
跑。完成消息列出未晋升候选、`Related:` 行与任何 `ISSUE_LOOKUP_FAILED`。

### Capy

跑
`[ "${GSTACK_CAPY:-}" = 1 ] && echo 'CAPY_PR: on' || echo 'CAPY_PR: off'`。
`CAPY_PR: on` 时，现在就读
`~/.claude/skills/gstack/ship/sections/capy-pr.md`：正文以下方各节之
前的 `## What changed`、`## Why` 与 `## Approvals` 开头。
`CAPY_PR: off` 时跳过它。

PR/MR 正文应包含这些节（绝不复用上一次运行的正文）：

```
## Summary
<Read `git log origin/<base>..HEAD --oneline`. Group every substantive commit by
theme, excluding VERSION/CHANGELOG bookkeeping. Do not paste the commit list.>

## Test Coverage
<coverage diagram from Step 7, or "All new code paths have test coverage.">
<If Step 7 ran: "Tests: {before} → {after} (+{delta} new)">
<If Step 7 ran: "Coverage: {X}% value-weighted ({Y}% including {W} weakly covered paths)">
<If Step 7 ran: "Test value: {K} tests written, {R} rejected by the authoring gate, {E} existing tests extended, {W} paths weakly covered (weak = ★, gate-failing or unrated)." Use the singular noun for a count of 1 ("1 test written", "1 existing test extended", "1 path weakly covered").>
<Weak paths and leftover gaps as proposed tests with value cards; each regression test's
"Regression proof — fails at HEAD · passes at base · passes after fix" line; Test value
details for cards whose file type has no known comment syntax.>
<One line per Step 5 lane: "Tests ran: <lane> N" from its receipt's `tests_ran`, or
"Tests ran: <lane> count unavailable" when the runner summary was not recognised. A
ZERO-RUN lane never reaches this body unresolved.>

## Pre-Landing Review
<findings from Step 9 code review, or "No issues found.">
<Gate edits: Step 9's latest `Gate edits:` line verbatim — `none detected (...)`,
`N listed, M read, K findings — J kept, R restored, O open`, `partial (...)` or
`UNAVAILABLE — ...`; never `none detected` for partial or UNAVAILABLE. Under it, each
kept finding's `gate`, path and `reason`, and each open finding's `gate` and path.
Identity and reason only; no hunk text.>
<Outside review: its verdict; `unverified` or `unavailable` is listed as missing coverage with its reason, never as passed.>

## Exploratory QA
<Step 9's current surfaces/charters, reproducers, approved regressions and red/green
proof, fixes and blocked/inconclusive/not-run coverage. Never present stale or
unavailable results as passing.>

## Design Review
<If design review ran: "Design Review (lite): N findings — M auto-fixed, K skipped. AI Slop: clean/N issues.">
<Detector: "clean" | "N findings (rule-id, rule-id)" | "not installed" | "not cached" | "off" — the state the probe printed; rule ids and counts only, finding text and snippets never reach the PR body.>
<If no frontend files changed: "No frontend files changed — design review skipped.">

## Eval Results
<If evals ran: suite names, pass/fail counts, cost dashboard summary. If skipped: "No prompt-related files changed — evals skipped.">

## Greptile Review
<Step 10 complete: list comments with [FIXED] / [FALSE POSITIVE] / [ALREADY FIXED], or "No Greptile comments." for a successful empty fetch.>
<Step 10 unavailable: include `Greptile triage: UNAVAILABLE (dispatch failed)` and the actual reason.>
<Step 10 no_pr: omit this section.>

## Scope Drift
<If scope drift ran: "Scope Check: CLEAN" or list of drift/creep findings>
<If no scope drift: omit this section>

## Plan Completion
<If plan file found: completion checklist summary from Step 8>
<If Step 8 printed the not-run line: that line verbatim.>
<If plan items deferred: list deferred items>

## Linked Spec
<Closes #N only when the Linked Spec check above permits it; otherwise
"Linked to #N (partial delivery — not auto-closing)" with remaining work and
"Close #N manually after follow-up lands." Include archive filename and filed date.
Without a valid match, omit this entire section.>

## Issues
<Issue links stdout, verbatim; omit on ISSUE_LINKS: none.>

## Verification Results
<Step 8.1 obligations executed at Step 9: N PASS, M FAIL, K BLOCKED, J NOT RUN,
not-applicable reasons, unresolved obligations and accepted deferrals.
Unavailable/inconclusive is never PASS.>

## TODOS
<If items marked complete: bullet list of completed items with version>
<If no items completed: "No TODO items completed in this PR.">
<If TODOS.md created or reorganized: note that>
<If TODOS.md doesn't exist and user skipped: omit this section>

## Documentation
<Embed Step 14.5's vetted nonempty `documentation_section` for this invocation:
its saved section file, inserted unchanged by the compose block's `DOCS_SECTION_FILE` lines.
A blocked audit shipped under a user exception has no section file: state its
blocked status, scope and exception here and drop the block's `DOCS_SECTION_FILE` guard
and its `cat -- "$DOCS_SECTION_FILE" && echo &&` step.>
<Always include the status and reviewed scope: updated, current, or blocked with the actual user's named risk exception. Never omit this section or reuse another invocation's audit.>

## Test plan
- [x] <Each executed test lane's command>: <observed passing summary>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

#### 组装正文，经 gstack-post 发布

公开仓库的 PR 正文全世界可读。`gstack-post` 扫描它发送的精确标题与
正文字节并作为参数传给 `gh`/`glab`，此处没有单独扫描。把 Codex /
Greptile / eval 输出的各节包进工具署名围栏（` ```codex-review ` /
` ```greptile `），让扫描器对其中示例凭证 WARN 降级而不是阻塞 PR
（围栏内的真实格式凭证仍然阻塞）。

把上方正文写进两个私有文件：第一个到 `## Documentation` 标题行为止，
第二个从 `## Test plan` 起。

```bash
_GT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp"
mkdir -p "$_GT" && chmod 700 "$_GT" || { echo "Not sent: cannot create $_GT for the text file." >&2; exit 1; }
_EX=$(git rev-parse --git-path info/exclude 2>/dev/null) && mkdir -p "$(dirname "$_EX")" && { grep -qxF '/.gstack/tmp/' "$_EX" 2>/dev/null || echo '/.gstack/tmp/' >> "$_EX"; }
BODY_TOP_FILE=$(mktemp "${_GT:?}/pr-body-top.XXXXXX") || { echo "Not sent: mktemp failed in $_GT." >&2; exit 1; }; echo "BODY_TOP_FILE: $BODY_TOP_FILE (name: ${BODY_TOP_FILE##*/})"
BODY_REST_FILE=$(mktemp "${_GT:?}/pr-body-rest.XXXXXX") || { echo "Not sent: mktemp failed in $_GT." >&2; exit 1; }; echo "BODY_REST_FILE: $BODY_REST_FILE (name: ${BODY_REST_FILE##*/})"
```

用你的文件写入工具把文本写进每个打印出的文件（Claude Code 的 Write
工具需要先 Read 一次空文件），内容与应出现的一字不差。文本绝不进
shell 命令、heredoc 或带引号参数。写入失败或被拒时不发送：打印原
因、文件路径和下方命令，供手工发送。

在新的 shell 里，恢复 Step 14.5 保存的 section 文件路径为
`DOCS_SECTION_FILE` 并替换打印名。该块会删除两个草稿；要改正文就重
写新的。

```bash
: "${DOCS_SECTION_FILE:?Restore the saved Step 14.5 section file path before composing}"
PR_BODY_FILE=$(mktemp "${TMPDIR:-/tmp}/gstack-pr-body.XXXXXX") || { echo "ERROR: mktemp failed — cannot compose the PR body; refusing to publish." >&2; exit 1; }
BODY_TOP_FILE="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp/<body-top-file-name>"
BODY_REST_FILE="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp/<body-rest-file-name>"
[ -s "$BODY_TOP_FILE" ] && [ -s "$BODY_REST_FILE" ] || { echo "Not composed: $BODY_TOP_FILE or $BODY_REST_FILE is empty, so the body was never written. Write both, then rerun." >&2; exit 1; }
{ awk 1 "$BODY_TOP_FILE" && cat -- "$DOCS_SECTION_FILE" && echo && awk 1 "$BODY_REST_FILE"; } > "$PR_BODY_FILE" || exit 1
rm -f "$BODY_TOP_FILE" "$BODY_REST_FILE"
echo "PR_BODY_FILE: $PR_BODY_FILE"
```

先写移交记录（标识符能活过截断）。用文件写入工具把 Step 16 阶段 4
的逐 lane 计数（`{"<lane>":{"pass":N,"fail":N,"skip":N}}`）写进
`.gstack/tmp/ship-gate.json`，然后：

```bash
~/.claude/skills/gstack/bin/gstack-ship-receipt write --pr <pr-number> --base <base> --gate @.gstack/tmp/ship-gate.json --pregate .gstack/tmp/pregate.json --issues @.gstack/tmp/issues.json --body "$PR_BODY_FILE"
```

仅当 Step 16 写过 tree-receipt（gate-ahead）时加
`--receipt .gstack/tmp/tree-receipt.json`。新 PR/MR：先省略 `--pr`，
创建后带编号重跑并重发正文。其 `SHIP_RECEIPT:` 行打开完成消息。
`RECEIPT_INVALID` 点名坏字段：修那个输入文件重跑；什么都没写入。
`ISSUE_LINKS_MISSING`：在 `## Issues` 下加所点名的行并重跑。
`PREGATE_STALE` 表示要在已盖章的树上重跑 `gstack-pregate`；
`PREGATE_REMOTE_UNCLEARED` 需要带 run URL 跑 `gstack-pregate clear`。
两者都停止发布。

下方每个块里，恢复字面 `PR_BODY_FILE` 路径并替换 Step 18 的标题文
件名；`gstack-post` 从远端与仓库可见性检测 GitHub 或 GitLab（查询不
可用，包括 GitLab 上，用扫描器的公开严格策略）。绝不重渲染正文：每
次重试发送同一批文件。

**已有开放 PR/MR**（复查得到的 `<pr-number>`）：

```bash
TITLE_FILE="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp/<title-file-name>"
~/.claude/skills/gstack/bin/gstack-post pr-body <pr-number> --body-file "${PR_BODY_FILE:?restore the composed body path}" && \
~/.claude/skills/gstack/bin/gstack-post pr-title <pr-number> --title-file "$TITLE_FILE"
```

它先更新正文再更新标题，把退役 GraphQL 编辑经 REST 重试并回读标
题。然后按 Step 9 的门控发现决定 draft 状态：

1. Step 6.5 把这个 PR 开成提前 draft、用户没要 draft、且无任何门控
   发现为 `open`：现在用 `gh pr ready <pr-number>` 标记 ready。
2. Step 6.5 开成提前 draft 且有门控发现为 `open`：保持 draft；打印
   `Draft kept: Gate edits: N open` 及 open 发现的 `gate` 与路径。
3. PR 已是 ready（非 draft）且有门控发现为 `open`：仅在 Step 17 记
   录的人工授权（那里的选项 B）下发布；正文已带
   `Gate edits: N open` 横幅。没有那份记录就 STOP 并报告。

打印既有 URL 并继续 Step 20；不要跑下方的创建命令。

**无开放 PR/MR：**任一门控发现为 `open` 时加 `--draft`（之后的
agent 绝不从"PR 存在"推断批准；人在处置完 open 项后标记 ready）。
否则直接以 ready 创建：

```bash
TITLE_FILE="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp/<title-file-name>"
~/.claude/skills/gstack/bin/gstack-post pr-create --base <base> --title-file "$TITLE_FILE" --body-file "${PR_BODY_FILE:?restore the composed body path}"
```

带 open 门控发现时，同一命令在 `--title-file` 之前携带 `--draft`。

按两个块之一的 exit code 分支：
- **0** 已发布。删除 `$PR_BODY_FILE` 与标题文件。
- **1** HIGH 发现：BLOCKED，不发布。在源头轮换并脱敏，然后组装全新
  文件。
- **2** MEDIUM 发现，以带 `TOKEN:` 的 `RULE:` 行打印。逐个发现
  AskUserQuestion（公开仓库语气更硬，不批量确认）。PII 提供自动脱
  敏：把
  `~/.claude/skills/gstack/bin/gstack-redact --from-file "$PR_BODY_FILE" --auto-redact <ids>`
  的输出写回正文文件并重跑该块（它会再扫描）。仅当用户照单接受发
  现时，在打印它的那条命令上追加 `--confirm <confirm-token>` 重跑；
  任何编辑都需要新 token。
- **3** `gh`/`glab` 失败，或 **64** 无可用远端或 CLI：打印错误、分
  支名、远端 URL 与供手工发布的命令块。不停：代码已推送；但绝不报
  告一个未创建的 PR。带 open 门控发现时，还要说明门控编辑未披露，
  并把 Step 16 的 open 项报告留在调用记录里；绝不把披露报告为已完
  成。
- 其他任何 exit 都是阻塞发布的错误，修好成因之前不发布。

**输出 PR/MR URL**，然后进入 Step 20。

---
