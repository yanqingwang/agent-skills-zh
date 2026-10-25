<!-- AUTO-GENERATED from transcript-gate.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`setup-gbrain/sections/transcript-gate.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

记忆同步接线之后（Step 7）、CLAUDE.md 配置持久化之前（Step 8），问
一次：本机的 coding-agent 会话 transcript 能否进 gbrain。策展的
`~/.gstack/` 产物（learnings、时间线、计划、设计、retro）无论答案如
何都同步；本问只涉及 transcript。用户选了 `recent`、`all` 或 `new`
（仅从现在开始的会话）之后才会摄取 transcript。

先检查用户是否已选过。门以 `has` 为键，因为 `get` 对从未设置的键会
打印 `off` 默认值：
```bash
_TIM=$(~/.claude/skills/gstack/bin/gstack-config get transcript_ingest_mode 2>/dev/null || true)
if ~/.claude/skills/gstack/bin/gstack-config has transcript_ingest_mode; then
  _T='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]t[0-9][0-9]:[0-9][0-9]:[0-9][0-9]z'
  case "$(printf '%s' "$_TIM" | tr -d '[:space:]' | tr '[:upper:]' '[:lower:]')" in
    recent|all|off|recent+repos|all+repos|new@$_T|new@$_T+repos)
      echo "TRANSCRIPT_MODE: $_TIM (repos: $(~/.claude/skills/gstack/bin/gstack-config get transcript_repos 2>/dev/null || true))" ;;
    *) echo "TRANSCRIPT_MODE: ask (stored value '$_TIM' is not recognized by this version)" ;;
  esac
else
  echo "TRANSCRIPT_MODE: ask (not set)"
fi
```

- `TRANSCRIPT_MODE:` 带值（`recent`、`all`、`off`、`new@<time>`，
  任何带 `+repos` 的组合）：用户已选过。不再问，继续 Step 8。
- `TRANSCRIPT_MODE: ask`：问一次，见下。`SESSION_KIND: spawned` 或
  `headless` 时不问也不存值。同意绝不自动代选；保持键未设
  （transcript 继续跳过），并报告下一次交互式 `/sync-gbrain` 会问。

用两个探测定问题的规模。`--sources transcript` 让探测统计
transcript，即使一个都还没获同意：
```bash
bun --no-env-file --config=/dev/null run ~/.claude/skills/gstack/bin/gstack-memory-ingest.ts --probe --sources transcript
bun --no-env-file --config=/dev/null run ~/.claude/skills/gstack/bin/gstack-memory-ingest.ts --probe --sources transcript --all-history
```
读各自的 `Total files in window`、`Total bytes` 与估算。

**没找到 transcript**（两个探测都报 0）：改问 yes/no：

> "要在 coding-agent 会话出现时摄取它们吗？"

Yes 存 `recent`（然后问下方的范围问题）；No 存 `off`。

**否则**，带计数发 AskUserQuestion。点名两个会话来源与 Step 4 的目标
大脑：用户的 Supabase 大脑（Paths 1、2a、2b）或本机的本地 PGLite 大脑
（Path 3）。

> "Found <N_recent> Claude Code and Codex sessions from the last 90 days
> (<N_all> in all history, <bytes>) across the projects on this machine
> that your repo policy allows. Ingest them into your <Supabase | local
> PGLite> brain?
>
> What you get: gstack skills load recent context from your past sessions,
> so the agent finds your prior work without you describing it, and you
> can ask 'what was I doing on day X'. Per-session pages are searchable,
> taggable and deletable. Secret scanning runs before any push.
>
> What stays the same: nothing leaves this machine unless brain sync is
> enabled (Step 7). Per-repo trust policies still apply. The first full
> sync can take a while on a large history (estimate: <est>); skills stay
> usable while it runs.
>
> Multi-machine note: with brain sync enabled, transcript pages sync across
> your machines. Deleting a page later removes it from gbrain, but git
> history keeps it in earlier commits. Use `gstack-transcript-prune` to
> delete in bulk, and `git filter-repo` on the brain remote to remove it
> from history."

选项：
- A) 是，最近 90 天（`recent`）
- B) 是，全部历史（`all`）
- C) 是，只从现在起的新会话（`new`）
- E) 否，绝不摄取 transcript（`off`）

任何"是"之后，问第二个独立问题："哪些仓库的会话？"A) repo 策略允许
的每个项目仓库，或 B) 只有本仓库（仅当 `git remote get-url origin`
在此成功才提供 B）。两个答案都拿到之前什么都不存；用户中途取消也
什么都不存。然后先存范围、再存模式值（绝不存字母；`new` 存 `new@`
加当前 UTC 时间）：
```bash
~/.claude/skills/gstack/bin/gstack-config set transcript_repos "$(git remote get-url origin)"  # only this repo
~/.claude/skills/gstack/bin/gstack-config unset transcript_repos                                 # every repo
~/.claude/skills/gstack/bin/gstack-config set transcript_ingest_mode <recent|all|off|new@$(date -u +%Y-%m-%dT%H:%M:%SZ)>
bun --no-env-file --config=/dev/null run ~/.claude/skills/gstack/lib/transcript-consent.ts --describe
```
把 `--describe` 那行转述给用户：用文字说明将摄取什么。

`recent`、`all` 或 `new@…` 时，现在就跑第一次同步：
```bash
bun --no-env-file --config=/dev/null run ~/.claude/skills/gstack/bin/gstack-gbrain-sync.ts --full --no-brain-sync
```
（`--no-brain-sync` 因为 Step 7 已接线该路径；此处跑代码导入与记忆摄
取阶段，`all` 会走完整历史。）
`off` 时此处什么都不跑；其他记忆在下次 `/sync-gbrain` 时照常同步。

新 transcript 在下一次 `/sync-gbrain` 运行时摄取。Skill 启动时没有任何
东西摄取它们。

用户参考文档：`setup-gbrain/memory.md#transcripts`。
