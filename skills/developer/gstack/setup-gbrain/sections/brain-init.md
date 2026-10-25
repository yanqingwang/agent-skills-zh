<!-- AUTO-GENERATED from brain-init.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`setup-gbrain/sections/brain-init.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

按路径各不相同。只跑 Step 2 所选路径（或 Step 2 选了引擎迁移时的
Switch 流程）对应的下方小节。

### Path 1（Supabase，已有 URL）

source 密钥读取 helper，用 `read -s` 收集 URL 并做脱敏预览：

```bash
. ~/.claude/skills/gstack/bin/gstack-gbrain-lib.sh
read_secret_to_env GBRAIN_POOLER_URL "Paste Session Pooler URL: " \
  --echo-redacted 's#://[^@]*@#://***@#'
```

然后做结构校验：

```bash
printf '%s' "$GBRAIN_POOLER_URL" | ~/.claude/skills/gstack/bin/gstack-gbrain-supabase-verify -
```

校验 exit 3（直连 URL）时，验证器自己的消息写明修法；转述它并重新
索要 Session Pooler URL。

成功后经环境变量交给 gbrain（绝不走 argv）：

```bash
GBRAIN_DATABASE_URL="$GBRAIN_POOLER_URL" gbrain init --non-interactive --json
```

然后立即 `unset GBRAIN_POOLER_URL GBRAIN_DATABASE_URL`。URL 现已由
gbrain 自己以 mode 0600 持久化在 `~/.gbrain/config.json`。

### Path 2a（Supabase，自动开通）

收集 token 之前逐字展示这份 PAT 范围披露：

> *This Supabase Personal Access Token grants full read/write/delete access
> to every project in your Supabase account, not just the `gbrain` one we're
> about to create. Supabase doesn't currently support scoped tokens. We use
> this PAT only to: create one project, poll it until healthy, read the
> Session Pooler URL — then discard it from process memory. The token
> remains valid on Supabase's side until you manually revoke it at
> https://supabase.com/dashboard/account/tokens — we recommend revoking
> immediately after setup completes.*

然后：

```bash
. ~/.claude/skills/gstack/bin/gstack-gbrain-lib.sh
read_secret_to_env SUPABASE_ACCESS_TOKEN "Paste PAT: "
```

经 AskUserQuestion 问档位："选哪个 Supabase 档位？"给出 Free（2 项目
上限、7 天不活动暂停）与 Pro（$25/月、不暂停、真实使用推荐）。说明
档位是**组织级**的（按 Management API 契约）：用户按其组织当前档位
选。Pro 可能需要他们先在 supabase.com 给组织升级。

列出组织、选一个（多个时 AskUserQuestion）：

```bash
orgs=$(~/.claude/skills/gstack/bin/gstack-gbrain-supabase-provision list-orgs --json)
```

`.orgs` 数组为空时提示："你的 Supabase 账户没有组织。去
https://supabase.com/dashboard 建一个，然后重跑 `/setup-gbrain`。"
STOP。

问用户选区域（默认 `us-east-1`；合法值是 Supabase Management API 的
18 个枚举值：列几个常见的，让他们选"Other"看完整列表）。

生成数据库密码（绝不展示给用户）：

```bash
export DB_PASS=$(openssl rand -base64 24)
```

设 SIGINT trap，让被打断的开通可恢复或可删除：

```bash
trap 'echo ""; echo "gstack-gbrain: interrupted. In-flight ref: $INFLIGHT_REF"; \
      echo "Resume: /setup-gbrain --resume-provision $INFLIGHT_REF"; \
      echo "Delete: https://supabase.com/dashboard/project/$INFLIGHT_REF"; \
      unset SUPABASE_ACCESS_TOKEN DB_PASS; exit 130' INT TERM
```

创建 + 等待 + 取 URL：

```bash
result=$(~/.claude/skills/gstack/bin/gstack-gbrain-supabase-provision \
  create gbrain "$REGION" "$ORG_SLUG" --json)
INFLIGHT_REF=$(echo "$result" | jq -r .ref)
~/.claude/skills/gstack/bin/gstack-gbrain-supabase-provision wait "$INFLIGHT_REF" --json
pooler=$(~/.claude/skills/gstack/bin/gstack-gbrain-supabase-provision \
  pooler-url "$INFLIGHT_REF" --json)
GBRAIN_DATABASE_URL=$(echo "$pooler" | jq -r .pooler_url)
export GBRAIN_DATABASE_URL
gbrain init --non-interactive --json
unset SUPABASE_ACCESS_TOKEN DB_PASS GBRAIN_DATABASE_URL INFLIGHT_REF
trap - INT TERM
```

成功后发 PAT 吊销提醒：

> "Setup complete. Revoke the PAT you pasted at
> https://supabase.com/dashboard/account/tokens — we've already discarded
> it from memory and don't need it again. The gbrain project will continue
> working because it uses its own embedded database password."

### Path 2b（Supabase，手动）

陪用户走 supabase.com 的步骤：
1. 在 https://supabase.com/dashboard 登录
2. 点 "New Project"，命名为 `gbrain`，选区域，并复制生成的数据库
   密码：第 4 步的 pooler URL 必须带上它（粘贴前替换任何
   `[YOUR-PASSWORD]` 占位符）
3. 等约 2 分钟让项目初始化
4. Settings → Database → Connection Pooler → Session → 复制 URL
   （端口 6543）

然后走与 Path 1 相同的 密钥读取 + 校验 + 初始化 流程。

### Path 3（PGLite 本地）

```bash
# gstack default: voyage-code-3 (1024d) when VOYAGE_API_KEY is set — code
# retrieval beats general-purpose embeddings on real code queries (validated
# A/B). Without the key, gbrain auto-selects (OpenAI 1536d when available).
# Never select gbrain's legacy zeroentropyai recipe for a new brain: its hosted
# API's sunset date (September 4, 2026) has passed; the wireup helper warns existing installs.
set --  # flags ride the positional params — unquoted $VAR breaks under zsh word-splitting
if [ -n "${VOYAGE_API_KEY:-}" ]; then
  set -- --embedding-model voyage:voyage-code-3 --embedding-dimensions 1024
fi
gbrain init --pglite --json "$@"
```

完成。无网络、无密钥（设了 `VOYAGE_API_KEY` 时，同步期间的 Voyage
embedding API 调用除外，约 $0.18/百万 token，每仓库几美分）。

### Path 4（远程 gbrain MCP：带 bearer token 的 HTTP 传输）

适用于大脑跑在另一台机器上的用户（Tailscale、ngrok、内网或队友的服
务器）。不装本地 gbrain CLI、无本地 DB。本 Skill 注册远程 MCP 后停
止；摄取与索引发生在大脑宿主上。

**4a. 收集 MCP URL。**提示用户：

```
Paste your gbrain MCP URL (e.g. https://wintermute.tail554574.ts.net:3131/mcp):
```

用普通 `read -r` 读取（无需密钥级防护，URL 本身不是凭证）。校验以
`https://` 开头（任何非回环主机都要求 TLS）；非 localhost 拒绝
`http://`。

**4b. 经密钥读取 helper 收集 bearer token（绝不走 argv）。**

```bash
. ~/.claude/skills/gstack/bin/gstack-gbrain-lib.sh
read_secret_to_env GBRAIN_MCP_TOKEN "Paste bearer token: " \
  --echo-redacted 's/.\{6\}$/***REDACTED***/'
```

**4c. 经 gstack-gbrain-mcp-verify 验证。**跑 helper，捕获分类后的
JSON 输出：

```bash
verify_json=$(GBRAIN_MCP_TOKEN="$GBRAIN_MCP_TOKEN" \
  ~/.claude/skills/gstack/bin/gstack-gbrain-mcp-verify "$MCP_URL")
status=$(echo "$verify_json" | jq -r .status)
```

`status != "success"` 时，helper 已把失败归类为 NETWORK / AUTH /
MALFORMED 并输出一行修复提示。把提示放在 `error_text` 的原始错误之
上呈现，并带着清晰的"修复后重跑 /setup-gbrain"消息 **STOP**。验证
失败绝不继续 Step 5a：半截注册会让用户留在半坏状态。

从验证输出为后续步骤捕获两个值：
- `SERVER_VERSION`（如 `0.27.1`）：写入 Step 8 的 CLAUDE.md 块。
- `URL_FORM_SUPPORTED`（`true|false`）：传给 Step 7 的
  `gstack-artifacts-init`，控制打印哪种形式的大脑管理员接线命令。

**4d.（Path 4）提议本地 PGLite 做代码搜索。**问：

> D# — Want symbol-aware code search on this machine?
> Project/branch/task: <one-sentence grounding using detected slug + branch>
> ELI10: The remote brain at `<MCP_URL>` is great for cross-machine knowledge,
> but symbol queries like `gbrain code-def` / `code-refs` / `code-callers` need
> a local index of THIS machine's code. We can spin up a tiny isolated PGLite
> database (~30 seconds, no accounts, ~120 MB disk) just for code, separate
> from your remote brain. Transcripts and artifacts continue routing through
> the artifacts repo to the remote brain — local PGLite stays code-only.
> Stakes: without it, semantic code search in this repo's worktrees falls
> back to Grep.
> Recommendation: A — 30 seconds, no ongoing cost, unlocks the symbol tools.
> Completeness: A=10/10 (full split-engine), B=7/10 (remote-only).
> A) Yes, set up local PGLite for code (recommended)
>   ✅ Unlocks `gbrain code-def`, `code-refs`, `code-callers` per worktree
>   ✅ Independent engine — won't disturb remote brain or share transcripts
> B) No, remote MCP only
>   ✅ Zero local state — only `~/.claude.json` MCP registration
>   ❌ Symbol code queries fall back to Grep in this repo's worktrees
> Net: A = full split-engine; B = remote-only.

**选 A（是）**：以可回滚语义安装并初始化本地 PGLite：

```bash
~/.claude/skills/gstack/bin/gstack-gbrain-install || exit $?
# At this point the local gbrain CLI is on PATH. Init PGLite, but back up any
# existing ~/.gbrain/config.json first (rollback if init fails).
if [ -f "$HOME/.gbrain/config.json" ]; then
  BACKUP="$HOME/.gbrain/config.json.gstack-bak-$(date +%s)"
  mv "$HOME/.gbrain/config.json" "$BACKUP"
fi
# gstack default for local code-search PGLite: voyage-code-3 (1024d) when
# VOYAGE_API_KEY is set. It wins the A/B over voyage-4-large and OpenAI
# text-embedding-3-large on this codebase's symbol queries. Falls back to
# gbrain's auto-selected provider when the key isn't present.
set --  # flags ride the positional params — unquoted $VAR breaks under zsh word-splitting
if [ -n "${VOYAGE_API_KEY:-}" ]; then
  set -- --embedding-model voyage:voyage-code-3 --embedding-dimensions 1024
fi
if ! gbrain init --pglite --json "$@"; then
  if [ -n "${BACKUP:-}" ] && [ -f "$BACKUP" ]; then mv "$BACKUP" "$HOME/.gbrain/config.json"; fi
  echo "gbrain init failed. Existing config (if any) was restored. PGLite at ~/.gbrain/pglite/ may be in a partial state — \`rm -rf ~/.gbrain/pglite\` to reset." >&2
  echo "Continuing setup without local code search; you can re-run /setup-gbrain to retry." >&2
fi
```

然后继续 Step 5a。5a 的 remote-http MCP 注册原样运行；本地 PGLite
与 MCP 注册相互独立（Claude Code 经 MCP 查询远程大脑；`gbrain` CLI
对本地 PGLite 做 code-def/refs/callers）。

**选 B（否）**：跳过安装与初始化。本地引擎保持缺席。
`gbrain_local_status` 将是 `missing-config`（或未装 gbrain 时的
`no-cli`）。`/sync-gbrain` 会干净地 SKIP 代码阶段。

**4e. 选 B 时跳过 Step 3、Step 4（其他路径）与 Step 5（本地
doctor）。**选 A 时 Step 3 已跑（经 gstack-gbrain-install）、Step 4
已跑（经 `gbrain init --pglite`）；直接跳到 Step 5a。选 B 时
Step 3/4/5 是空操作；还要跳过 Step 7.5（transcript 摄取），因为
remote-http 模式下记忆阶段走产物管道。

bearer token（`GBRAIN_MCP_TOKEN`）留在进程环境里，直到 Step 5a 的
`claude mcp add --header` 消费它；然后立即
`unset GBRAIN_MCP_TOKEN`。token 安全权衡记录在
`setup-gbrain/memory.md`：`claude mcp add` 期间短暂的 argv 暴露，静
息状态在 `~/.claude.json` mode 0600。

### Switch（从 detect 的既有引擎状态）

```bash
# Going PGLite → Supabase, collect URL first (Path 1 flow), then:
timeout 180s gbrain migrate --to supabase --url "$URL" --json
# Going Supabase → PGLite:
timeout 180s gbrain migrate --to pglite --json
```

`timeout` 返回 124（超时退出码）时，转述这条消息（"Migration
didn't complete in 3 minutes — another gstack session may be holding a
lock on the source brain. Close other workspaces and re-run
`/setup-gbrain --switch`. Your original brain is untouched."）。STOP。
