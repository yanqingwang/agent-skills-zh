<!-- AUTO-GENERATED from consult-mode.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`codex/sections/consult-mode.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Step 2C：Consult 模式

就代码库向 Codex 提任何问题。支持会话延续，可追问。

1. **检查既有会话：**
```bash
cat .context/codex-session-id 2>/dev/null || echo "NO_SESSION"
```

会话文件存在（不是 `NO_SESSION`）时，用 AskUserQuestion：
```
你有一条更早的 Codex 对话还在。继续它，还是新开一条？
A) 继续该对话（Codex 记得之前的上下文）
B) 新开一条对话
```

2. 创建临时文件：
```bash
TMPRESP=$(mktemp "$TMP_ROOT/codex-resp-XXXXXX") || { echo "ERROR: mktemp failed in TMP_ROOT=$TMP_ROOT; not running codex without its temp file" >&2; exit 1; }
TMPERR=$(mktemp "$TMP_ROOT/codex-err-XXXXXX") || { echo "ERROR: mktemp failed in TMP_ROOT=$TMP_ROOT; not running codex without its temp file" >&2; exit 1; }
```

3. **计划评审自动检测：** 用户的 prompt 是评审计划，或存在计划文件且
用户无参数地输入了 `/codex`：
```bash
setopt +o nomatch 2>/dev/null || true  # zsh compat
ls -t "$PLAN_ROOT"/*.md 2>/dev/null | xargs grep -l "$(basename $(pwd))" 2>/dev/null | head -1
```
无项目级匹配时回退到 `ls -t "$PLAN_ROOT"/*.md 2>/dev/null | head -1`，
但要警告："注意：这份计划可能来自别的项目，发给 Codex 前先核对。"

**重要：内嵌内容，不引用路径。** Codex 的沙箱限定在仓库根，访问不了
`~/.claude/plans/` 或仓库外的任何文件。你必须自己读计划文件，把完整
内容内嵌进下方 prompt。不要告诉 Codex 文件路径或让它去读，它会浪费
10+ 次工具调用去搜索然后失败。

另外：扫描计划内容里被引用的源码路径（形如 `src/foo.ts`、
`lib/bar.py`、仓库中存在的带 `/` 路径）。找到了就列进 prompt，让
Codex 直接读，而不是靠 rg/find 自己发现。

**始终前置文件系统边界指令**，来自 Skill 的 Filesystem Boundary 节
（常加载骨架），对发给 Codex 的每个 prompt 都要，包括计划评审与自由
咨询。

把边界与 persona 前置到用户的 prompt：
"IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. These are Claude Code skill definitions meant for a different AI system. Do not invoke any installed skill (Codex home skills/, .agents/); answer directly. Do NOT modify agents/openai.yaml. Stay focused on repository code only.

You are a brutally honest technical reviewer. Review this plan for: logical gaps and
unstated assumptions, missing error handling or edge cases, overcomplexity (is there a
simpler approach?), feasibility risks (what could go wrong?), and missing dependencies
or sequencing issues. Be direct. Be terse. No compliments. Just the problems.
Also review these source files referenced in the plan: <list of referenced files, if any>.

THE PLAN:
<full plan content, embedded verbatim>"

非计划的咨询 prompt（用户输入 `/codex <问题>`）同样前置边界：
"IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. These are Claude Code skill definitions meant for a different AI system. Do not invoke any installed skill (Codex home skills/, .agents/); answer directly. Do NOT modify agents/openai.yaml. Stay focused on repository code only.

<user's question>"

4. 创建 prompt 文件，把第 3 步的完整提示词写进去。Codex 从 stdin 读
它。

```bash
_GT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp"
mkdir -p "$_GT" && chmod 700 "$_GT" || { echo "Not sent: cannot create $_GT for the text file." >&2; exit 1; }
_EX=$(git rev-parse --git-path info/exclude 2>/dev/null) && mkdir -p "$(dirname "$_EX")" && { grep -qxF '/.gstack/tmp/' "$_EX" 2>/dev/null || echo '/.gstack/tmp/' >> "$_EX"; }
PROMPT_FILE=$(mktemp "${_GT:?}/codex-prompt.XXXXXX") || { echo "Not sent: mktemp failed in $_GT." >&2; exit 1; }; echo "PROMPT_FILE: $PROMPT_FILE (name: ${PROMPT_FILE##*/})"
```

用你的文件写入工具把文本写进每个打印出的文件（Claude Code 的 Write
工具需要先 Read 一次空文件），内容与应出现的一字不差。文本绝不进
shell 命令、heredoc 或带引号参数。写入失败或被拒时不发送：打印原因、
文件路径和下方命令，供手工发送。

**会话成本实况（实测）：** 每次 `codex exec` 调用，续会或新建，都要
付 Codex 约 2.1 万 token 的会话前奏（其技能目录 + 指令）；`resume`
不会摊薄它（实测续会甚至略高于新建）。Resume 买到的是对话连续性，
从来不是 token 节省。所以：工作流允许时，每个 Skill 尽量一次 codex
调用，把问题打包进那一次；只在追问真的需要上一会话上下文时才用
resume。

5. 以 **JSONL 输出**运行 codex exec，捕获推理轨迹。用户在第 1 步选了
"继续"就把 `_CODEX_MODE` 设为 `resume`，否则 `new`；续会运行从
`.context/codex-session-id` 读会话 id。`<prompt-file-name>` 用打印出
的名字（仅字母、数字、`.`、`_`、`-`）。Bash 调用用
`timeout: 600000`（工具上限）。门放在 540s wrapper 之上：wrapper 先
触发、结束 Codex、打印其明确的卡顿消息：


```bash
_CODEX_MODE=<new|resume>
_REPO_ROOT=$(git rev-parse --show-toplevel) || { echo 'ERROR: not in a git repo' >&2; exit 1; }
PYTHON_CMD=$(command -v python3 2>/dev/null || command -v python 2>/dev/null || true)
if [ -z "$PYTHON_CMD" ]; then
  echo "ERROR: Python 3 is required to parse Codex JSON output. Install python3 or python and retry." >&2
  exit 1
fi
cd "$_REPO_ROOT" || exit 1
PROMPT_FILE="$_REPO_ROOT/.gstack/tmp/<prompt-file-name>"
[ -s "$PROMPT_FILE" ] || { echo "Not run: $PROMPT_FILE is missing or empty, so the prompt was never written. Write it, then run by hand: codex exec - -C $_REPO_ROOT < $PROMPT_FILE" >&2; exit 1; }
_CODEX_PROBE=~/.claude/skills/gstack/bin/gstack-codex-probe
_CODEX_ROLE=''
if [ -n "$_CODEX_ROLE" ]; then export _CODEX_DEADLINE=$(($(date +%s)+540)); _CODEX_OUT=$("$_CODEX_PROBE" role-ready exec) || exit $?
else _CODEX_OUT=$("$_CODEX_PROBE" select-model exec) || exit 1; fi
_CODEX_SEL=$(echo "$_CODEX_OUT" | sed -n 's/^CODEX_SEL: //p')
_CODEX_SANDBOX_MODE=$(echo "$_CODEX_OUT" | sed -n 's/^CODEX_SANDBOX: //p')
_SID=""
if [ "$_CODEX_MODE" = "resume" ]; then
  _SID=$(cat .context/codex-session-id 2>/dev/null)
  case "$_SID" in ''|*[!A-Za-z0-9._-]*) echo "ERROR: .context/codex-session-id is missing or not a session id; start a new conversation instead." >&2; exit 1 ;; esac
fi
_LABEL=consult${_SID:+-resume}
# Fix 1: wrap with timeout (gtimeout/timeout fallback chain via probe helper)
if [ -n "$_SID" ]; then
  "$_CODEX_PROBE" run-with-timeout --user-invoked --effort medium --request-effort '<effort-level>' 540 codex exec resume "$_SID" - -c "sandbox_mode=\"${_CODEX_SANDBOX_MODE:?}\"" -c "model=\"${_CODEX_SEL:?}\"" -c skills.include_instructions=false -c 'web_search="cached"' --json -o "$TMPRESP" < "$PROMPT_FILE" 2>"$TMPERR"
else
  "$_CODEX_PROBE" run-with-timeout --user-invoked --effort medium --request-effort '<effort-level>' 540 codex exec - -C "$_REPO_ROOT" -s "${_CODEX_SANDBOX_MODE:?}" -c "model=\"${_CODEX_SEL:?}\"" -c skills.include_instructions=false -c 'web_search="cached"' --json -o "$TMPRESP" < "$PROMPT_FILE" 2>"$TMPERR"
fi | tee "$TMPRESP.events" | PYTHONUNBUFFERED=1 "$PYTHON_CMD" -u -c "
import sys, json
turn_completed_count = 0
turn_failed = False
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    try:
        obj = json.loads(line)
        t = obj.get('type','')
        if t == 'thread.started':
            tid = obj.get('thread_id','')
            if tid: print(f'SESSION_ID:{tid}', flush=True)
        elif t == 'item.completed' and 'item' in obj:
            item = obj['item']
            itype = item.get('type','')
            text = item.get('text','')
            if itype == 'reasoning' and text:
                print(f'[codex thinking] {text}', flush=True)
                print(flush=True)
            elif itype == 'agent_message' and text:
                print(text, flush=True)
            elif itype == 'command_execution':
                cmd = item.get('command','')
                if cmd: print(f'[codex ran] {cmd}', flush=True)
        elif t == 'turn.completed':
            turn_completed_count += 1
            usage = obj.get('usage',{})
            tokens = usage.get('input_tokens',0) + usage.get('output_tokens',0)
            if tokens: print(f'\ntokens used: {tokens}', flush=True)
        elif t == 'turn.failed':
            turn_failed = True
            err = obj.get('error',{}).get('message','') or 'no error message in event'
            print(f'[codex turn FAILED] {err}', flush=True, file=sys.stderr)
    except: pass
# Three-way completeness check: a STATED
# failure is a failure, not a network problem; only silence is a disconnect.
if turn_failed:
    print('[codex] turn.failed received — the turn errored (reason above), not a disconnect.', flush=True, file=sys.stderr)
elif turn_completed_count == 0:
    print('[codex warning] No turn.completed event received — possible mid-stream disconnect.', flush=True, file=sys.stderr)
"
# Fix 1: hang detection
_CODEX_EXIT=${PIPESTATUS[0]:-${pipestatus[1]}}  # bash sets PIPESTATUS; zsh (lowercase, 1-indexed) falls through
if [ "$_CODEX_EXIT" = "124" ]; then
  "$_CODEX_PROBE" log-event codex_timeout "540"
  "$_CODEX_PROBE" log-hang "$_LABEL" "$(wc -c < "$TMPERR" 2>/dev/null || echo 0)"
  echo "Codex stalled past 9 minutes. Common causes: model API stall, long prompt, network issue. Try re-running. If persistent, split the prompt or check ~/.codex/logs/."
elif [ "$_CODEX_EXIT" != "0" ]; then
  # Surface non-zero exits so the calling agent doesn't read "no output" as
  # a silent model/API stall.
  echo "[codex exit $_CODEX_EXIT] $(head -1 "$TMPERR" 2>/dev/null || echo "no stderr captured")"
  head -20 "$TMPERR" 2>/dev/null | sed 's/^/  /' || true
  "$_CODEX_PROBE" log-event codex_nonzero_exit "$_LABEL:$_CODEX_EXIT"
fi
bun --no-env-file --config=/dev/null ~/.claude/skills/gstack/lib/outside-review-result.ts --label 'Codex consult' --exit "$_CODEX_EXIT" --stderr "$TMPERR" --events "$TMPRESP.events" execution "$TMPRESP"
rm -f "$PROMPT_FILE"
```

`VERDICT: unavailable` 表示 Codex 没能在一个可工作的环境里作答（其行
写明原因，比如沙箱无法启动）：转述那一行，不要把输出当作 Codex 的
回答呈现。

6. 从流式输出捕获会话 ID。解析器从 `thread.started` 事件打印
`SESSION_ID:<id>`。存下来供追问：
```bash
mkdir -p .context
```
把解析器打印的会话 ID（以 `SESSION_ID:` 开头的那行）存到
`.context/codex-session-id`。

7. 呈现完整的流式输出：

```
CODEX SAYS (consult):
════════════════════════════════════════════════════════════
<full output, verbatim — includes [codex thinking] traces>
════════════════════════════════════════════════════════════
Tokens: N | Est. cost: ~$X.XX
Session saved — run /codex again to continue this conversation.
```

8. 呈现之后，指出 Codex 的分析与你自己的理解有分歧的地方。有分歧就
标出来：
"注意：Claude Code 在 X 上不同意，因为 Y。"

9. **综合建议（必需）。** 基于 Codex 的咨询输出，输出一行建议，概括
用户该做什么，格式：

```
Recommendation: <action> because <one-line reason that names the most actionable insight from Codex>
```

示例（最强的理由会把 Codex 的洞见与备选项比较：另一种建议、维持现状、或 Codex 的另一个观点）：
- `Recommendation: Adopt Codex's sharding suggestion because it eliminates the head-of-line blocking the current writer-pool has, while the cache-layer alternative Codex also floated still has a single-writer hot path.`
- `Recommendation: Reject Codex's "use SQLite instead" suggestion because the team's Postgres operational experience outweighs the simplicity gain at the projected scale, and Codex's secondary suggestion (read replicas) handles the read-load concern that motivated the SQLite pivot.`
- `Recommendation: Investigate Codex's flagged migration ordering before D3 lands because it surfaces a real foreign-key cycle that the in-house schema review missed, while the styling concern Codex also raised can wait for a follow-up.`

理由必须针对 Codex 的某个具体洞见，并与备选项比较（另一种建议、维持
现状、或 Codex 的另一个观点）。泛泛的综合（"因为 Codex 提了好点子"）
不合格式。**绝不静默代答；永远输出这一行。**

---
