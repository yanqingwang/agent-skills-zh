> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/claude-security/skills/claude-security/specs/patch-spec.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 补丁产物规格

修复任务所写产物的形状。两半：Security Lead 手写的工作记录（`patches.json`），以及 `patch_artifacts.py` 从它加上 git 写出的原始 diff 渲染出的产物。这与 `report-spec.md` 一脉相承：模型叙述并决策，脚本写文件，所以在到达用户之前，没有任何 diff 字节和置信主张由模型重新键入。

## 工作记录：`patches.json`

由 Security Lead 写入补丁工作场（`<report dir>/.claude-security-run/patch-<ts>/patches.json`）。一个对象，带一个 `units` 数组，每个被选发现一条：

```json
{
  "units": [
    {
      "id": "F1",
      "title": "SQL injection in report export query",
      "status": "patch_written",
      "summary": "The export endpoint interpolated the user-supplied table name into SQL; the patch binds it against the allowlist of exportable tables instead.",
      "claims": {
        "targeted": { "state": "CONFIDENT", "evidence": "one hunk, export.py:88-94, only the query construction moved" },
        "no_new_vulnerability": { "state": "CONFIDENT", "evidence": "the allowlist is the existing EXPORT_TABLES constant; no new input reaches SQL" },
        "behaviour_unchanged": { "state": "CONFIDENT", "evidence": "tests/test_export.py covers all three exportable tables and passes" }
      },
      "untested": false,
      "tests_run": "python -m pytest tests/ -q (41 passed)",
      "reviewed_paths": ["M src/export.py"],
      "attempts": 1,
      "attack_paths": [
        { "kind": "set_aside", "text": "GET /admin/diag?host= reaches subprocess.run with shell=True at admin/diag.py:12; a command injection, pre-existing and unrelated to this finding" }
      ]
    },
    {
      "id": "F3",
      "title": "Path traversal in attachment download",
      "status": "declined",
      "attempts": 1,
      "claims": {
        "behaviour_unchanged": { "state": "UNSURE", "evidence": "no test covers the download handler and three callers pass paths I could not trace" }
      },
      "attack_paths": [
        { "kind": "still_reachable", "text": "GET /thumb?name=../../etc/passwd reaches the same unconfined attachment_path helper through the thumbnail handler" }
      ],
      "decline_reason": "I couldn't establish that the fix leaves existing download behaviour unchanged, and the fresh reviewer found the finding's exploit still reachable through the thumbnail handler, so no patch was written.",
      "recommendation": "Resolve the requested path against the attachments root and reject anything outside it before opening the file."
    },
    {
      "id": "F5",
      "title": "SQL injection via sort parameter in note search",
      "status": "declined",
      "attempts": 1,
      "confirmed": false,
      "decline_reason": "The verifier found the sort parameter only selects one of three constant column names and the query is parameterised, so the injection the report describes does not work at this revision.",
      "recommendation": "Whitelist the sort values and never format request data into the SQL string."
    }
  ]
}
```

字段，按单元：

| 字段 | 何时 | 含义 |
| ----------------- | ------------------------------------- | ----------------------------------------------------------------------- |
| `id` | 总是 | 发现 id，`^F[0-9]{1,9}$`：唯一被据以行动的来自报告的值 |
| `title` | 总是 | 发现标题，按原文引用 |
| `status` | 总是 | `patch_written`、`declined` 或 `skipped_stale` |
| `summary` | `patch_written` | 一行：根因与改动做了什么 |
| `confirmed` | 因未确认而被拒的 `declined` 单元 | `false`：验证者指出了改动前代码中挫败该发现利用方式的所在，因此该单元以未确认被拒；`true` 会被接受并带入 `patches.jsonl`，但不渲染任何东西；其余情况省略；在 `skipped_stale` 单元上被忽略 |
| `attempts` | `patch_written` / `declined` | 修复尝试次数：生成器被派发过的单元记 1，走过修订轮的记 2；只有工作区无法打开的被拒单元才记 0；在 `skipped_stale` 单元上被忽略 |
| `claims` | `patch_written`（三项全要）；否则为验证者陈述过的那些 | `targeted`、`no_new_vulnerability`、`behaviour_unchanged`，各为 `{state, evidence}`；`state` 为 `CONFIDENT`、`NOT_CONFIDENT` 或 `UNSURE` |
| `untested` | `patch_written`（必需，true/false） | 项目自己的测试套件没有任何测试执行被补丁代码时为 `true`（验证者临场自写的 harness 不算） |
| `tests_run` | `patch_written` | 验证者逐字记录的测试命令，或 "none possible: …" |
| `reviewed_paths` | `patch_written` | 验证者的 `REVIEWED_PATHS`（name-status 形式） |
| `attack_paths` | `patch_written`（必需，没有时为 `[]`）；否则只要有报告过就要 | 新起的 `scan-researcher` 的攻击路径，各为 `{kind, text}`：`kind` 为 `opened`（由改动打开）、`still_reachable`（该发现的利用经另一条路线）或 `set_aside`（既有且与本发现无关），按研究员的标注；在 `confirmed` 为 false 旁报告的通往其他代码的仍可抵达路径也记 `set_aside`；`text` 是路径的它的原话，一行 |
| `decline_reason` | `declined` / `skipped_stale` | 为什么没写补丁，用一句用户能读的话 |
| `recommendation` | `declined`（可选） | 报告原有的修复建议，让用户仍然保有它 |

被拒绝的尝试不留存：工作树和原始 diff 都活不过这次运行，因为它被拒绝了；被拒说明改为携带什么挡住了它、以及该次尝试的 diffstat。没有任何字段点名临时目录或保存的 diff，因为产物写完之后整个工作场都会被移除。

`title`、`summary`、`tests_run` 和每条 claim 的 `evidence` 是写入补丁 `#` 注释头的单行字段，每条攻击路径的 `text` 是说明的一条要点，所以其中任何内嵌换行都会折叠成一个空格。更长的解释放进说明字段，那是 markdown 正文，不是头注释行。

脚本在以下情况拒绝该记录（退出码 1，消息点名字段）：

- 单元 id 格式错误、状态未知，或 `attempts` 在 written 或 declined 单元上缺失、不是整数、或在 written 单元上为 0；
- `patch_written` 单元缺一条 claim、有任何 claim 不是 `CONFIDENT`、省略 `untested` 或 `attack_paths`，或携带一条未被搁置的攻击路径；
- 任何攻击路径 kind 未知或没有 text；
- declined 单元没有理由，或 `confirmed` 不是 true/false、在未 declined 的单元上为 false，或与一条 `still_reachable` 攻击路径并存时为 false；
- 必需的 `F<n>.diff` 缺失或不含 `diff --git` 节；
- 记录点名的单元 id 不是 `--prepare` 在 `findings/` 里准备过的。

补丁是逐字节忠实的：git 写出的 diff 原样到达 `F<n>.patch`，包括 CRLF 和非 UTF-8 文件。它还拒绝写到 `CLAUDE-SECURITY-<timestamp>` 报告目录内的 `patches/` 之外的任何地方，所以错误的路径永远不会让任意目录被套上 `.gitignore` 栅栏。拒绝被修正后重跑脚本：绝不变通绕过。

## 产物：`<report dir>/patches/`

| 文件 | 内容 |
| ---------------- | --------------------------------------------------------------------------------------- |
| `F<n>.patch` | git 写出的原始 diff（`F<n>.diff`），第一行 `diff --git` 之上是 `#` 注释头：点名发现、信任标签（由 agent 评审组验证：独立验证者，加上一名质疑该 diff 是否打开攻击路径、或给它所关发现的利用留下另一条路线的新审查者）、三项 claim 及其证据、`untested` 为 true 时的覆盖告知、以及一行应用命令。`git apply` 忽略头注释。 |
| `F<n>.md` | 每个单元旁边的说明：written patch 记：同样的 agent 评审组信任标签、summary、claims、diffstat（重命名显示为 `old => new`，文件权限变化写在其路径旁，二进制文件标注 `(binary)`）、运行的测试、`git apply --check` 结果、如何应用——命令中的报告路径经 shell 引号包裹，父目录名含空格时命令仍可直接粘贴；declined 单元记：做了多少次尝试而没有一次通过评审组审查，或（当 `confirmed` 为 false 时）审查认定该发现在本修订版下并不像报告描述的那样可利用，还有原因、任何未以置信度作出的 claim、被拒尝试的 diffstat（当验证者审查过一份 diff 时）、以及原有建议；两种情况都记：新审查者报告的攻击路径，各归其 kind，set-aside 的注明此处不处理。 |
| `PATCHES.md` | 单页索引：已写的补丁（各注明由 agent 评审组验证，`untested` 为 true 时标记覆盖告诫）、没有补丁的单元、尝试多少次或发现未获确认及其原因、审查者搁置的路径、应用说明。用户读到的信任标签永远是评审组的验证，绝不是 "tested"/"untested" 标签。 |
| `patches.jsonl` | 每单元一条记录：`id`、`status`、`base`（每个补丁所适用的修订版）、`patch`、`note`、`claims`、`untested`、`tests_run`、`reviewed_paths`、`attack_paths`、`attempts`、`confirmed`、`diffstat`、`apply_check`、`decline_reason`。 |

每次运行脚本还会移除早前运行遗留在文件夹里、而这次没有写出的任何 `F<n>.patch` / `F<n>.md`，让文件夹始终与索引一致（以前赢得过补丁、现在被拒的发现绝不留下过期的、未列出的补丁）；文件夹里的其他文件永不触碰。脚本还会在报告目录缺 `.gitignore` 时补一个含 `*` 的，这样走火的 `git add` 永远不会把建议的补丁卷进提交；并用 `git apply --check` 对用户仓库以只读方式校验每个已写补丁，记录结果：不再能干净应用的补丁会被报告，绝不丢弃，因为它基于记录的修订版构建，工作树可能只是移动了。最后移除整个补丁工作场：每个临时工作区（`scratch-F<n>`），然后是 `patch-<ts>` 目录本身连同 `patches.json`、准备好的 `findings/` 和原始 diff，以及上面的 `.claude-security-run/` 目录（没有其他东西残留时）。每次移除都限定在那个精确布局之内，移除不了的路径是一条打印的警告，绝不是一次失败的运行。修复运行最后只留下 `patches/` 产物。
