> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/claude-security/skills/claude-security/specs/report-spec.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

<!-- 读者：安全负责人（Security Lead），负责从工作流的发现汇总报告；扫描作业的交付步骤会写出 CLAUDE-SECURITY-RESULTS.md。仅当扫描到达交付阶段时才加载本文件。 -->

# CLAUDE-SECURITY-RESULTS.md——报告规格

Markdown 报告是唯一以散文形式撰写而非生成的产物。它是人类真正阅读的部分，因此要为一位特定的读者而写：一位拥有这份代码、很忙的工程师，他会用大约九十秒决定是否处理每条发现。

`render_report.py` 从 `findings.json` 和 `votes.json` 生成机器可读的配套产物。不要手写 JSONL、SARIF 或印章，也不要在这里复述 JSONL 的内容，这个文件是人类阅读的那一部分。

## 形态

```markdown
# Claude Security results

<one paragraph: what was scanned (path, revision, mode, scope), when, at what
effort, and the headline: how many findings at what severities, or that there
were none. Read `revision.dirty` in the run dir's scan-meta.json: on `true`,
say the repository's working tree held uncommitted changes or untracked files
-- which ones is not recorded, so never name or explain them; on `null`, say
the tree state could not be determined; otherwise say nothing of it.>

## Coverage

<what was examined and what was not. Name the components. If the scope was
narrowed, say to what and why. If write_scan_meta.py reported a sparse
checkout (`revision.not_checked_out_dirs` in the run dir's scan-meta.json
holds the list), say that only the checked-out part of the repository was
scanned and name those tracked top-level directories as not checked out.
Say how many verification runs the panel took
(coverage.verificationRun), and name any candidate never verified and why:
lost on the way to a further run (coverage.lostCandidates), or handed to a run
that did not complete.
If coverage.researchersReturned is below coverage.researchersDispatched:
- say how many researchers did not return and that their reading is missing
  from this scan;
- name each entry of coverage.lostResearchers by its reading, with its reason
  quoted;
- with more than 10 entries, group them by reason instead, each group with
  what its researchers were sent to read;
- describe why a researcher did not return only by its recorded reason;
- wherever the report says what the research covered or read, including the
  "What was verified" section, credit only readings in coverage.returnedReadings.
Name every area the scan deliberately did NOT examine, and WHY: each entry of
coverage.skippedComponents carries the paths left out and the componentizer's
one-line reason (vendored, generated, documentation, and the like); a
directory skipped on purpose is disclosure, not failure, so state the reason
rather than letting the area silently vanish.
If coverage.prunedBuckets is non-empty, each entry is a group's (or
component's) name, as coverage.components lists it, followed by
":memory-and-unsafe", the research lens it went without. Write each name
whole and say plainly that none of that group's researchers was asked about
memory-safety bugs, whatever the tier. An entry for "change boundary" has no
coverage.components row: it is the researcher working outward from the
change, under the same rule over every changed file, not a second group. Give
only the workflow's reason: it decided from the language alone -- the changed
files' extensions on a changes or commit scan, the inventory's language on a
codebase scan -- before the group's researchers were briefed, because it took
the code to be all in managed languages. Do not add that the lens does not
apply to such code, and never describe the prune as something the researchers
or the panel did, or as a lens dropped because a finding was in hand. A group
with no entry kept the lens.
On a whole-repository scan the
workflow requires the inventory to account for every top-level directory --
scanned or explicitly skipped -- and coverage.completenessCheckOutcome says whether
that check ran: "checked" (say the whole tree is accounted for),
"partial" (the inventory left some top-level directories in neither ledger and
the answer was used as it stood -- coverage.unaccountedTopLevelDirs names them;
list every one and say plainly they were neither scanned nor skipped, because
that is exactly the coverage a "no findings" would otherwise overstate),
"not-checkable" (the tree's directory list was not supplied, was unreadable, or
was empty while the inventory named subdirectories -- coverage.topLevelRejected
says which; say plainly that completeness could NOT be checked, since that is
what turns "no findings" into "clean" rather than "not examined"), or
"not-applicable" (a diff, commit, or scoped scan, whose target
is the change or the scope, or a low-effort run with no inventory). If
coverage.inventoryFallback is set, the inventory's partition was not used and
the whole tree was read as one component instead of the matrix -- complete,
but coarser -- and the reason is: "incomplete-partition" (its answer would have
credited coverage it never named -- a skip of the whole target, or nothing but
paths climbing out of the tree; the rejections are listed in
coverage.inventoryRejected),
"inventory-failed" (it did not answer), or "empty-partition" (it answered with
nothing). For a changes or commit scan, say that the change was reviewed
rather than the repository: name the change in plain words (following
`jobs/scan-changes.md`'s rules on the commit count and the branch) rather
than by the commit ids in coverage.range, the changed files by group
(coverage.components; coverage.diffFiles files of the coverage.changedFileCount
the helper counted, coverage.diffLines lines), and
how many researchers were dispatched and how many returned
(coverage.researchersDispatched, coverage.researchersReturned), and the
effort they were asked for (coverage.researchEffort -- asked, not measured:
the model's runtime may apply its own); say that a flaw the change takes no part in is out
of this review's scope and left to a scan of the codebase, and list every
entry of coverage.preExisting as a candidate the panel judged real but
predating the change. When the base is the branch's own pushed copy, so that
the diff holds only the unpushed commits, say that the commits already pushed
were not part of this review. If coverage.outsideScope is non-empty, say that those
findings (it names them) sit outside the requested scope and are reported
because the change reaches them. If coverage.changedFilesRejected is set, the changed-file
list could not be read or loaded: quote the recorded value and say the change
was reviewed as one group whose researchers listed it themselves; if
coverage.changedFilesMiscounted is set, the list handed over disagreed with
the count: give both, say which list was reviewed (its reviewed field) and
how many files that was (coverage.diffFiles). If a scoped
scan collapsed to the proportionate single-researcher shape rather than the
full component matrix, say so: coverage.collapsed is "small-scope" for a small
scope at medium (give coverage.scopeFiles) -- a fast targeted pass, still
panel-verified, not an exhaustive read. If a supplied scope size could not be
read (coverage.scopeSizeRejected), quote the recorded value and state its
actual consequence for the tier that ran: at medium, the scope was not
treated as small so the full pipeline ran instead of the fast path, and an
empty scope could not have been short-circuited.
Say how the run was sized when coverage.targetComponents is set: the target's
coverage.targetFiles tracked files, about coverage.targetComponents components
asked for (of roughly coverage.filesPerComponent files each, or larger when
the target holds more than coverage.componentCap components of that size),
at most coverage.componentCap kept. Then say what the researchers themselves report
not having read, as their account rather than as fact: coverage.research.components
lists, per component, the paths its researchers declared not reached and why --
summarize by directory with the reason, one line for a background tree (vendored
trees, and test and fixture trees under focus, left as background, are expected there
and are background, not gaps), and name individual files only up to a handful
per component. coverage.research.tree, when present, is that account checked
against the tracked files inside the components: how many were read to a
conclusion, how many lie under a declared not-reached path, and how many no
researcher accounted for at all (when coverage.research.capped is true an
account was truncated, so at least that many were read and at most that many
are unaccounted) -- list coverage.research.tree.unaccountedPaths (the first of them; the count
is the whole), because a component nobody finished reading would otherwise pass
for a clean one; files outside every component
(coverage.research.tree.outsideComponents) are the skipped and dropped areas
this section already names plus root files no component claims, not a
researcher's gap. When coverage.research is null or its tree absent, that
check did not run; say nothing of it, though any declared paths still stand.
This section is
what makes the rest of the report trustworthy: a reader who knows what you did
not look at can calibrate everything else.>

## Findings

The `F<n>` in each heading is that finding's `id` from `findings.json`, copied exactly — the findings arrive already in report order, so never renumber, reorder, or invent an id. A gap in the numbering is a candidate the panel did not keep under that id; call it rejected only when a complete panel refuted it, never when coverage.adversarialCasualties, coverage.preExisting or coverage.lostCandidates (the last by candidate id) names it.

### F1 — <title> (HIGH, confidence medium)

**Impact.** <what an attacker gets. Lead with this: it is what decides
priority.>

**Where.** `path/to/file.py:123` in `function_name` — <cwe_id, then
"(also <other_cwe_ids>)" when the finding carries further CWEs>

**Link to the change.** <a changes or commit scan only: the finding's
via_change, the changed line that takes part in the attack and how, named by
file:line and never quoted; omit the line for a scan of the codebase>

**What.** <the vulnerability, in two or three sentences. Name the untrusted
source, the dangerous operation, and why nothing in between stops it.>

**Exploit scenario.** <a concrete walk-through. Not "an attacker could inject
SQL" -- what they send, what happens, what they get.>

**Preconditions.** <bullets: what must be true. Authentication? A non-default
config? Victim interaction? An empty list means none, which is worth saying.>

**Fix.** <what to change, in outcome terms. The root cause at the sink, not a
patch at one caller.>

**Verification.** <n>/3 lens verifiers confirmed.

### F2 — ...

## What was verified

<one paragraph: the pipeline that produced these findings, the votes each
survived, and the stamp's verification.status. If the status is anything other
than "verified", explain what it means in plain language and what to do about
it -- do not bury it. If the status is "verified" and a researcher did not
return, say that "verified" does not cover the missing readings.>
```

## 规则

**严重程度衡量的是可利用性与影响，不是置信度。** CRITICAL 表示影响严重且攻击者毫无阻碍。HIGH 表示影响严重，但存在一个真实障碍。MEDIUM 表示影响有边界，或严重影响需要满足多个条件。LOW 表示影响有限且利用门槛高。`findings.json` 中的严重程度是最终结果：当评审小组的确认投票者给某条发现的评级低于其研究员时，工作流已经把它调低了，coverage.severityLowered 会列出每条这样的发现及两个评级；在它的 **Verification.** 行如实说明，不要恢复原来的评级。不确定性属于 `confidence`，取值是一个词：`low`、`medium` 或 `high`，由评审小组投票约束：只有全票通过的评审小组才配得上 `high`，而工作流已经调低了其他任何 `high`；如果你把它改高，`render_report.py` 会再次调低。

**按严重程度排序，再按置信度排序。** 读者会中途停下，把要紧的放在顶部。

**发现超过二十条时分批写入。** 一次调用装下所有发现可能超出模型的输出上限，在那里被截断的 Write 会被整体拒绝。所以第一次 Write 包含开头段落、Coverage、前二十条发现和 What was verified，之后每二十条用 Edit 写入，插在 `## What was verified` 标题之上。

**每条发现都引用真实的 `file:line`。** 一条指向错误行号的发现，代价超过一条漏报：追查它的过程中，读者会失去对报告其余部分的信任。

**硬编码凭证类发现不写"Link to the change"行。** 凡在 `cwe_id` 或 `other_cwe_ids` 中带有 CWE-798、CWE-259、CWE-321 或 CWE-671 的发现都是如此：它本要点名的那行改动就是凭证本身，JSONL 和 SARIF 已经隐去了这一链接。

**不允许控制字符。** 只允许 `\n` 和 `\t`。报告在终端里阅读，转义序列可能改写人类看到的内容。如果被扫描的源码里确实出现了这样的字节，描述它，而不是复现它。

**不含糊其辞，不注水凑数。** 不要为了对代码客气而软化真实发现，也不要为了显得全面而夸大小问题。"无发现"是一份完整的报告，把它写好（覆盖了什么、没覆盖什么）比一页"可能有问题"更有价值。

**研究员的视角不是评审小组的视角。** 研究员的视角是漏洞类别：一个类别，或其所在组保留的全部类别。评审小组投票者的视角是可达性、影响或防御。绝不要把评审小组的这三者说成研究员的。

**绝不声称运行过没有运行的东西。** 扫描中没有任何环节会执行仓库的代码：没有运行过测试，没有发射过利用，没有验证过任何概念验证。每条发现都来自阅读。如实说明，不要暗示做过演示。

## 达标示例

不要这样写：

> 代码可能存在 SQL 注入漏洞。建议按最佳实践使用参数化查询。

要这样写：

> **Impact.** `GET /users?name=` 的任何未认证调用方都能读取 `users` 表的每一行，包括密码哈希和邮箱地址。
>
> **Where.** `api/app.py:3` 的 `get_user`——CWE-89
>
> **What.** `name` 在 `handlers.py:41` 从查询字符串进入，然后用 `%` 插值进 SQL 字符串。两者之间的路径上没有任何转义或校验；`handlers.py:38` 的 `validate_name` 只检查长度。
>
> **Exploit scenario.** `GET /users?name=' OR '1'='1` 让 WHERE 子句成为恒真式，JSON 响应返回整张表。
