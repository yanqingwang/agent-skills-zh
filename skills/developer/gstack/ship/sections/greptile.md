<!-- AUTO-GENERATED from greptile.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`ship/sections/greptile.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Step 10：处理 Greptile 评审评论（PR 存在时）

先检查有没有 PR。Greptile 评审的是 PR，所以没有 PR、没有 `gh`、`gh`
未登录或非 GitHub 远端时，暂时没有可分诊的东西：

```bash
if ! command -v gh >/dev/null 2>&1; then echo "PR: skip (gh not installed)"
elif ! gh auth status >/dev/null 2>&1; then echo "PR: skip (gh not logged in)"
elif ! _GH_ERR=$(gh repo view --json nameWithOwner -q .nameWithOwner 2>&1 >/dev/null); then echo "PR: skip (not a GitHub remote: $(printf '%s' "$_GH_ERR" | head -1))"
elif _PR_ERR=$(gh pr view --json number -q .number 2>&1 >/dev/null); then echo "PR: exists"
else case "$_PR_ERR" in *"no pull requests found"*) echo "PR: skip (no PR yet)" ;; *) echo "PR: skip (PR lookup failed: $(printf '%s' "$_PR_ERR" | head -1))" ;; esac
fi
```

只有 `PR: exists` 才派发。`PR: skip (<原因>)` 时不派发；记录
"Greptile: not run (<原因>); runs on the PR once it exists" 并继续
Step 11。

**提前 PR（Step 6.5）：** 调用记录持有 `EARLY_PR` 与
`EARLY_PR_OPENED_AT` 时，先等 Greptile 对该 PR 的评审，代入这两个值：

```bash
~/.claude/skills/gstack/bin/gstack-greptile-early wait <pr-number> --since <opened-at>
```

每次调用约 90 秒内返回；转述其进度行。`GREPTILE_REVIEW: pending` 时
重跑。`complete` 则往下派发。`timeout` 或 `unavailable` 走下方的不可
用分诊路线，以那一行为原因，绝不宣称零评论。对提前 head 的评论按当前
diff 分诊（代码已前进则 `already_fixed`）。

经 Agent 派发一个子代理，`subagent_type: "general-purpose"` 且
`run_in_background: false`，遵循 Step 7 的共享前台派发规则。它抓取并
分类全部 Greptile 评论，含升级层级；父级做决策并把获批的修复排队。

**子代理提示词：**

> You are classifying Greptile review comments for a /ship workflow. Read `~/.claude/skills/gstack/review/greptile-triage.md` and follow the fetch, filter, classify, and **escalation detection** steps. Do NOT fix code, do NOT reply to comments, do NOT commit — report only.
>
> For each comment, assign: `classification` (`valid_actionable`, `already_fixed`, `false_positive`, `suppressed`), `escalation_tier` (1 or 2), the file:line or [top-level] tag, body summary, and permalink URL.
>
> Return one JSON object on the LAST LINE:
> `{"status":"complete|no_pr|unavailable","total":N,"comments":[{"classification":"...","escalation_tier":N,"ref":"file:line","summary":"...","permalink":"url"},...],"reason":"..."}`
> Use `complete` only after a successful fetch, including zero comments; `no_pr` only after confirming no PR exists; `unavailable` for `gh`/API errors or incomplete classification. The latter two return zero total and an empty array. State the failure reason for `unavailable`; otherwise use an empty reason.

**父级处理：**

把最后一行解析为 JSON。要求声明的状态、与 comments 数组一致的非负
整数 total，以及上述状态/原因不变量。状态未知或缺失按 unavailable，
绝不是一个空的成功评审。

`no_pr` 记录 "Greptile: no PR exists"；零评论的 `complete` 记录
"Greptile: fetched, zero comments"。两者都继续 Step 11。

**不可用分诊：** 返回 `unavailable`、派发失败、结果无效或约 10 分钟
后仍未完成都走这条路。先停掉运行中的子代理，确认停了再继续。打印
`Greptile triage did not complete — review the PR comments manually`。
在 Step 19 的评审结果里写明
`Greptile triage: UNAVAILABLE (dispatch failed)` 与真实原因；Step 20
没有分诊字段。继续 Step 11，不宣称零评论或已完成分诊。这个可选分诊
不阻塞 ship。

否则打印：`+ {total} Greptile comments ({valid_actionable} valid,
{already_fixed} already fixed, {false_positive} FP)`。

对 `comments` 里的每条评论：

**VALID 且 ACTIONABLE：** 用 AskUserQuestion：
- 评论内容（file:line 或 [top-level] + 正文摘要 + permalink URL）
- `RECOMMENDATION: Choose A because [one-line reason]`
- 选项：A) 现在修，B) 确认后照常发布，C) 这是误报
- 选 A：把获批的修复排队，不在此处编辑。该修复通过评审与测试后，
  用 greptile-triage.md 的**Fix 回复模板**（内联 diff + 说明）并保存
  项目级/全局 greptile-history（type: fix）。
- 选 C：用 greptile-triage.md 的**误报回复模板**回复（附证据 + 建议
  的重排），同时保存项目级与全局 greptile-history（type: fp）。

**VALID 但已修复：** 用 greptile-triage.md 的**Already Fixed 回复
模板**回复，无需 AskUserQuestion：
- 写明做了什么与修复 commit 的 SHA
- 同时保存项目级与全局 greptile-history（type: already-fixed）

**FALSE POSITIVE：** 用 AskUserQuestion：
- 展示评论与你认为它错在哪（file:line 或 [top-level] + 正文摘要 +
  permalink URL）
- 选项：
  - A) 回复 Greptile 说明误报（明显错时推荐）
  - B) 还是修掉（如果很简单）
  - C) 静默忽略
- 选 A：用**误报回复模板**回复（附证据 + 建议的重排），同时保存项目
  级与全局 greptile-history（type: fp）
- 选 B：按上文把获批的修复排队。

**SUPPRESSED：** 静默跳过，它们是既往分诊确认过的已知误报。

**分诊之后：** 有获批的修复就保存其批准与评论引用。跑 Step 9 的完整
评审/修复循环，然后回到这里。不再就已完成的修复发问，完成保存的
回复，并对新评论分类。没有排队的修复就继续 Step 11。

---
