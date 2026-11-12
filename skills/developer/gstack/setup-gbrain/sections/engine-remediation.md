<!-- AUTO-GENERATED from engine-remediation.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`setup-gbrain/sections/engine-remediation.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

### Step 1.5 修复：损坏引擎的 AskUserQuestion 与修复分支

用户的本地引擎不可用（例如 `~/.gbrain/config.json` 指向一个已死的
Postgres URL）。在 Step 2 之前发一个有针对性的 AskUserQuestion：

> D# — Your local gbrain engine isn't responding. How do you want to fix it?
> Project/branch/task: <one-sentence grounding using detected slug + branch>
> ELI10: gbrain has a config at `~/.gbrain/config.json` but the engine it points
> at isn't reachable. That could be a transient outage (Postgres container
> stopped, Tailscale down) OR a stale config you want to abandon. Different
> remediation for each case.
> Stakes if we pick wrong: "Switch to PGLite" overwrites your existing config
> (one-way door if the user actually wanted the broken engine). "Retry" preserves
> existing state for transient cases.
> Recommendation: A (Retry) — always try the cheap option first; if engine is
> just temporarily down it'll come back without any destructive change.
> Note: options differ in kind, not coverage — no completeness score.
> A) Retry — re-probe the engine (recommended; ~80ms)
>   ✅ Cheapest test: re-runs `gbrain sources list` to see if engine is back
>   ✅ Zero side effects; existing config preserved
>   ❌ If engine is permanently dead, retries forever; user must choose another option
> B) Switch to local PGLite (one-way — moves existing config to .bak)
>   ✅ Fastest path to a working local engine if user has abandoned the old one
>   ✅ ~30s; no accounts; private to this machine
>   ❌ Destructive — existing config moved to ~/.gbrain/config.json.gstack-bak-{ts}
> C) Switch brain mode (continue to Step 2 path picker)
>   ✅ Lets user pick Path 1/2/3/4 to re-init from scratch
>   ✅ Preserves existing config until they explicitly init the new one
>   ❌ Longer flow if user just wants to repair to PGLite
> D) Quit (do nothing)
>   ✅ No cons — this is a hard-stop choice
>   ❌ N/A
> Net: A is the right starting move; B/C are explicit destructive paths; D bails.

**选 A（Retry）**：带 `GSTACK_DETECT_NO_CACHE=1`（击穿 60s 缓存）重跑
`~/.claude/skills/gstack/bin/gstack-gbrain-detect`。新的
`gbrain_local_status` 为 `ok` 时继续 Step 2。仍是 `broken-db` 或
`broken-config` 时再次发同一个 AskUserQuestion（由用户再选）。

**选 B（切到 PGLite）**：执行可回滚的安全初始化序列：

```bash
BACKUP="$HOME/.gbrain/config.json.gstack-bak-$(date +%s)"
mv "$HOME/.gbrain/config.json" "$BACKUP"
# gstack default: voyage-code-3 (1024d) when VOYAGE_API_KEY is set — best for
# code retrieval. Without the key, fall back to gbrain's own auto-selected
# embedding provider chain (OpenAI 1536d when OPENAI_API_KEY is present, etc.).
# Never select gbrain's legacy zeroentropyai recipe for a new brain: its hosted
# API's sunset date (September 4, 2026) has passed; the wireup helper warns existing installs.
set --  # flags ride the positional params — unquoted $VAR breaks under zsh word-splitting
if [ -n "${VOYAGE_API_KEY:-}" ]; then
  set -- --embedding-model voyage:voyage-code-3 --embedding-dimensions 1024
fi
if ! gbrain init --pglite --json "$@"; then
  # Restore on failure
  mv "$BACKUP" "$HOME/.gbrain/config.json"
  echo "gbrain init failed. Your previous config was restored at $HOME/.gbrain/config.json." >&2
  echo "PGLite directory at ~/.gbrain/pglite/ may be in a partial state — \`rm -rf ~/.gbrain/pglite\` if needed before retrying." >&2
  exit 1
fi
echo "Switched to local PGLite. Previous config saved at $BACKUP — review before deleting."
```

然后跳到 Step 5a（MCP 注册；新的 PGLite 引擎按 local-stdio 注册）。

**选 C（切换大脑模式）**：继续 Step 2 的常规路径选择。

**选 D（退出）**：干净地 STOP 本 Skill。
