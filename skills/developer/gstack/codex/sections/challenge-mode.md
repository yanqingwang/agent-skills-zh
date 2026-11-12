<!-- AUTO-GENERATED from challenge-mode.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`codex/sections/challenge-mode.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Step 2B：Challenge（对抗）模式

Codex 试图弄坏你的代码：找出普通评审会漏掉的边界情况、竞态条件、
安全漏洞与失败模式。

1. 构造对抗提示词。**始终前置文件系统边界指令**，来自 Skill 的
Filesystem Boundary 节（常加载骨架）。用户给了焦点区域时（如
`/codex challenge security`），把它放在边界之后：

默认提示词（无焦点）：
"IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. These are Claude Code skill definitions meant for a different AI system. Do not invoke any installed skill (Codex home skills/, .agents/); answer directly. Do NOT modify agents/openai.yaml. Stay focused on repository code only.

Review the changes on this branch against the base branch. Run `git diff origin/<base>` to see the diff. Your job is to find ways this code will fail in production. Think like an attacker and a chaos engineer. Find edge cases, race conditions, security holes, resource leaks, failure modes, and silent data corruption paths. Be adversarial. Be thorough. No compliments — just the problems."

带焦点（如 "security"）：
"IMPORTANT: Do NOT read or execute any files under ~/.claude/, ~/.agents/, .claude/skills/, or agents/. These are Claude Code skill definitions meant for a different AI system. Do not invoke any installed skill (Codex home skills/, .agents/); answer directly. Do NOT modify agents/openai.yaml. Stay focused on repository code only.

Review the changes on this branch against the base branch. Run `git diff origin/<base>` to see the diff. Focus specifically on SECURITY. Your job is to find every way an attacker could exploit this code. Think about injection vectors, auth bypasses, privilege escalation, data exposure, and timing attacks. Be adversarial."

2. 创建 prompt 文件，把第 1 步的完整提示词写进去。Codex 从 stdin 读
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

3. 以 **JSONL 输出**运行 codex exec，捕获推理轨迹与工具调用。
`<prompt-file-name>` 用打印出的名字（仅字母、数字、`.`、`_`、`-`）。
Bash 调用用 `timeout: 600000`（工具上限）。门放在 540s wrapper 之上：
wrapper 先触发、结束 Codex、打印其明确的卡顿消息：


```bash
_REPO_ROOT=$(git rev-parse --show-toplevel) || { echo 'ERROR: not in a git repo' >&2; exit 1; }
PROMPT_FILE="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp/<prompt-file-name>"
[ -s "$PROMPT_FILE" ] || { echo "Not run: $PROMPT_FILE is missing or empty, so the prompt was never written. Write it, then run by hand: codex exec - -C $_REPO_ROOT < $PROMPT_FILE" >&2; exit 1; }
PYTHON_CMD=$(command -v python3 2>/dev/null || command -v python 2>/dev/null || true)
if [ -z "$PYTHON_CMD" ]; then
  echo "ERROR: Python 3 is required to parse Codex JSON output. Install python3 or python and retry." >&2
  exit 1
fi
# Fix 1+2: wrap with timeout (gtimeout/timeout fallback chain via probe helper),
# capture stderr to $TMPERR for auth error detection (was: 2>/dev/null).
[ -n "${TMPERR:-}" ] || TMPERR=$(mktemp "$TMP_ROOT/codex-err-XXXXXX") || { echo "ERROR: mktemp failed in TMP_ROOT=$TMP_ROOT; not running codex without its temp file" >&2; exit 1; }
TMPRESP=$(mktemp "$TMP_ROOT/codex-resp-XXXXXX") || { echo "ERROR: mktemp failed in TMP_ROOT=$TMP_ROOT; not running codex without its temp file" >&2; exit 1; }
_CODEX_PROBE=~/.claude/skills/gstack/bin/gstack-codex-probe
_CODEX_ROLE=''
if [ -n "$_CODEX_ROLE" ]; then export _CODEX_DEADLINE=$(($(date +%s)+540)); _CODEX_OUT=$("$_CODEX_PROBE" role-ready exec) || exit $?
else _CODEX_OUT=$("$_CODEX_PROBE" select-model exec) || exit 1; fi
_CODEX_SEL=$(echo "$_CODEX_OUT" | sed -n 's/^CODEX_SEL: //p')
_CODEX_SANDBOX_MODE=$(echo "$_CODEX_OUT" | sed -n 's/^CODEX_SANDBOX: //p')
"$_CODEX_PROBE" run-with-timeout --user-invoked --effort high --request-effort '<effort-level>' 540 codex exec - -C "$_REPO_ROOT" -s "${_CODEX_SANDBOX_MODE:?}" -c "model=\"${_CODEX_SEL:?}\"" -c skills.include_instructions=false -c 'web_search="cached"' --json -o "$TMPRESP" < "$PROMPT_FILE" 2>"$TMPERR" | tee "$TMPRESP.events" | PYTHONUNBUFFERED=1 "$PYTHON_CMD" -u -c "
import sys, json
turn_completed_count = 0
turn_failed = False
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    try:
        obj = json.loads(line)
        t = obj.get('type','')
        if t == 'item.completed' and 'item' in obj:
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
# Fix 2: three-way completeness check — a STATED failure is a failure,
# not a network problem; only silence with no terminal event is a disconnect.
if turn_failed:
    print('[codex] turn.failed received — the turn errored (reason above), not a disconnect.', flush=True, file=sys.stderr)
elif turn_completed_count == 0:
    print('[codex warning] No turn.completed event received — possible mid-stream disconnect.', flush=True, file=sys.stderr)
"
_CODEX_EXIT=${PIPESTATUS[0]:-${pipestatus[1]}}  # bash sets PIPESTATUS; zsh (lowercase, 1-indexed) falls through
# Fix 1: hang detection — log + surface actionable message
if [ "$_CODEX_EXIT" = "124" ]; then
  "$_CODEX_PROBE" log-event codex_timeout "540"
  "$_CODEX_PROBE" log-hang "challenge" "$(wc -c < "$TMPERR" 2>/dev/null || echo 0)"
  echo "Codex stalled past 9 minutes. Common causes: model API stall, long prompt, network issue. Try re-running. If persistent, split the prompt or check ~/.codex/logs/."
elif [ "$_CODEX_EXIT" != "0" ]; then
  # Surface non-zero exits so the calling agent doesn't read "no output" as
  # a silent model/API stall.
  echo "[codex exit $_CODEX_EXIT] $(head -1 "$TMPERR" 2>/dev/null || echo "no stderr captured")"
  head -20 "$TMPERR" 2>/dev/null | sed 's/^/  /' || true
  "$_CODEX_PROBE" log-event codex_nonzero_exit "challenge:$_CODEX_EXIT"
fi
# Fix 2: surface auth errors from captured stderr instead of dropping them
if grep -qiE "auth|login|unauthorized" "$TMPERR" 2>/dev/null; then
  echo "[codex auth error] $(head -1 "$TMPERR")"
  "$_CODEX_PROBE" log-event codex_auth_failed
fi
bun --no-env-file --config=/dev/null ~/.claude/skills/gstack/lib/outside-review-result.ts --label 'Codex challenge' --exit "$_CODEX_EXIT" --stderr "$TMPERR" --events "$TMPRESP.events" execution "$TMPRESP"
rm -f "$TMPRESP" "$TMPRESP.events" "$PROMPT_FILE"
```

`VERDICT: unavailable` 表示挑战没有运行（其行写明原因，比如沙箱无法
启动）：如实说明，不要呈现来自它的任何发现。否则在下方呈现输出。

这段脚本解析 codex 的 JSONL 事件，提取推理轨迹、工具调用与最终回复。
`[codex thinking]` 行展示 codex 回答前想了什么。

4. 呈现完整的流式输出：

```
CODEX SAYS (adversarial challenge):
════════════════════════════════════════════════════════════
<full output from above, verbatim>
════════════════════════════════════════════════════════════
Tokens: N | Est. cost: ~$X.XX
```

4a. **综合建议（必需）。** 呈现完整对抗输出之后，输出一行建议，概括
用户该做什么，格式：

```
Recommendation: <action> because <one-line reason that names the most exploitable finding>
```

示例（最强的理由会比较各发现的爆炸半径，或修还是发）：
- `Recommendation: Fix the unbounded retry loop Codex flagged at queue.ts:78 because it DoSes the worker pool under sustained 429s, which is higher-blast-radius than the timing leak Codex also flagged that only touches a debug endpoint.`
- `Recommendation: Ship as-is because Codex's strongest finding is a theoretical race in cleanup that requires conditions we can't trigger in production, weaker than the runtime regressions a fix-now would risk.`

理由必须指向具体发现，并与备选项比较（其他发现、修还是发）。"因为
更安全"这类泛泛理由不合格式。**绝不静默跳过这一行。**

---
