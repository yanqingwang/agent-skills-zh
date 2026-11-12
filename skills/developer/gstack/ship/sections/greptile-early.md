<!-- AUTO-GENERATED from greptile-early.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`ship/sections/greptile-early.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Step 6.5：Greptile 提前 PR（免费测试通过之后）

仓库用 Greptile 时，现在推送并开 PR，让 Greptile 在 Step 7-9 运行期间
评审；Step 10 收它的评论。没有 Greptile 则什么都不变。

```bash
~/.claude/skills/gstack/bin/gstack-greptile-early detect
```

- **`GREPTILE_EARLY: off`**：打印原因（及重新开启的那行）并继续
  Step 7。
- **`GREPTILE_EARLY: ask`**（公开仓库，或首次未知可见性）：
  AskUserQuestion：
  > 本仓库是公开的。提前 Greptile 评审会在 /ship 自己的评审之前推送
  > 分支并开一个 draft PR，代码在那次评审结束前就可见。若 /ship 之后
  > 停止，draft 留在原处并附一条说明原因的评论。

  A) 本仓库提前推送（记住）· B) 本仓库维持今天的顺序（记住）。
  A 运行 `~/.claude/skills/gstack/bin/gstack-greptile-early consent yes`，
  B 运行 `consent no`。B 继续 Step 7。
- **`GREPTILE_EARLY: on`** 或选了 A 之后：向用户展示打印的
  `Greptile: found …` 行，然后按下方 1-3 执行。

**1.** 推送：`git push -u origin <branch-name>`。失败则记录
"Greptile early review: not run (push failed)" 并继续 Step 7；Step 17
稍后推送。

**2.** 把临时的 `<type>: <summary>` 标题（Step 18 会替换）写进私有
文件：

```bash
_GT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp"
mkdir -p "$_GT" && chmod 700 "$_GT" || { echo "Not sent: cannot create $_GT for the text file." >&2; exit 1; }
_EX=$(git rev-parse --git-path info/exclude 2>/dev/null) && mkdir -p "$(dirname "$_EX")" && { grep -qxF '/.gstack/tmp/' "$_EX" 2>/dev/null || echo '/.gstack/tmp/' >> "$_EX"; }
TITLE_FILE=$(mktemp "${_GT:?}/early-title.XXXXXX") || { echo "Not sent: mktemp failed in $_GT." >&2; exit 1; }; echo "TITLE_FILE: $TITLE_FILE (name: ${TITLE_FILE##*/})"
```

用你的文件写入工具把文本写进每个打印出的文件（Claude Code 的 Write
工具需要先 Read 一次空文件），内容与应出现的一字不差。文本绝不进
shell 命令、heredoc 或带引号参数。写入失败或被拒时不发送：打印原因、
文件路径和下方命令，供手工发送。

**3.** 用打印出的名字打开 draft。仅当用户明确要非 draft PR 时才加
`--ready`：

```bash
TITLE_FILE="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp/<title-file-name>"
~/.claude/skills/gstack/bin/gstack-greptile-early open --base <base> --title-file "$TITLE_FILE"
```

它经 `gstack-post` 打开 PR，正文注明 /ship 提前开了它；Greptile 跳过
draft 时补一条 `@greptileai` 评论。把打印的 `EARLY_PR` 与
`EARLY_PR_OPENED_AT` 存进调用记录。`EARLY_PR: none` 表示 PR 已开：
Step 10 照常分诊。exit 1 或 2 表示 `gstack-post` 对临时标题有意见：
写一个更朴素的再跑。exit 3：记录错误，不带提前评审继续。

**提前 PR 已开而 /ship 在 Step 19 发布之前停止时**，保留 draft（绝不
关闭或 force-push），并发一条评论说明 /ship 停止及原因：用文件写入
工具把原因写进私有文件，然后运行
`~/.claude/skills/gstack/bin/gstack-post pr-comment <pr-number> --body-file <that file>`。

---
