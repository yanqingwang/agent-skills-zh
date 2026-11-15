> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/setup-gbrain/memory.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# gstack memory ingest：它做什么、什么留在本地、你能拿它做什么

这是 `/setup-gbrain` 与 `/sync-gbrain` 中转录 + 记忆摄入功能的
用户参考。如果其中任何一个问过你是否要把编码 agent 会话
摄入 gbrain，本文解释每个答案分别意味着什么。

## 会摄入什么

| 来源 | 类型 | 位置 | 敏感度 |
|---|---|---|---|
| Claude Code 会话 JSONL | `transcript` | `~/.claude/projects/*/` | 高：完整对话，含工具输入输出 |
| Codex CLI 会话 JSONL | `transcript` | `~/.codex/sessions/YYYY/MM/DD/` | 高 |
| Cursor 会话 SQLite（V1.0.1） | `transcript` | `~/Library/Application Support/Cursor/` | 同上：推迟到 V1.0.1 |
| Eureka 日志 | `eureka` | `~/.gstack/analytics/eureka.jsonl` | 中：你的洞见，通常非机密 |
| 项目经验 | `learning` | `~/.gstack/projects/<slug>/learnings.jsonl` | 中 |
| 项目时间线 | `timeline` | `~/.gstack/projects/<slug>/timeline.jsonl` | 低 |
| CEO 计划 | `ceo-plan` | `~/.gstack/projects/<slug>/ceo-plans/*.md` | 中 |
| 设计文档 | `design-doc` | `~/.gstack/projects/<slug>/*-design-*.md` | 中 |
| 复盘 | `retro` | `~/.gstack/projects/<slug>/retros/*.md` | 中 |
| Builder 画像 | `builder-profile-entry` | `~/.gstack/builder-profile.jsonl` | 低 |

## 转录

精选记忆（learnings、timeline、plans、designs、retros、eureka、builder
profile）在每次 `/sync-gbrain` 都会同步。会话转录只在
你选择分享之后才同步。这个选择就是 `transcript_ingest_mode` 配置
键，可选地用 `transcript_repos` 白名单收窄：

| 取值 | `/sync-gbrain` 摄入什么 |
|---|---|
| `recent` | 最近 90 天的会话 |
| `all` | 全部历史（`--full` 遍历每个会话文件） |
| `new@2026-10-03T17:00:00Z` | 只有首条记录在该 UTC 时刻或之后的会话。更早开始的会话即使后来被追加也不纳入。没有开始时间戳的会话不纳入。 |
| `off` | 不摄入转录；其他记忆照常同步 |
| `recent+repos`、`all+repos`、`new@…+repos` | 同样的窗口，但仅限 `transcript_repos` 里的仓库。gstack 自己增删 `+repos`。 |

两个来源都覆盖：Claude Code 会话（`~/.claude/projects/`）和
Codex 会话（`~/.codex/sessions/`），来自本机
每个 per-remote 信任策略允许的项目，不只当前仓库。页面进
你的脑：local-stdio 模式下进本地引擎（PGLite 或 Supabase），或
remote-http 模式下进远程脑拉取的 artifacts 仓库。

设置或修改：

```bash
gstack-config set transcript_ingest_mode recent   # or all, or off
gstack-config set transcript_ingest_mode "new@$(date -u +%Y-%m-%dT%H:%M:%SZ)"   # only sessions from now on
gstack-config set transcript_repos github.com/acme/app,github.com/acme/api       # only these repos
gstack-config unset transcript_repos                                             # every repo again
gstack-config has transcript_ingest_mode && gstack-config get transcript_ingest_mode
bun run lib/transcript-consent.ts --describe                                     # the effective consent in words
```

`gstack-config set` 拒绝任何其他取值并保留已存值。截断时刻只接受
`Z`（UTC）形式，精确到秒。`transcript_repos`
接受任何 git remote 写法（`https://…`、`git@…:…`，带不带
`.git` 均可）并存储其规范形式；空列表被拒绝。设置
或清除白名单会在同一次写入中更新 `+repos` 标记。
`gstack-config set transcript_ingest_mode <base>` 在白名单存在时保留标记，
`off` 永远不带标记。

**多个配置根。** 当 gstack 读取多于一个状态根（例如
`GSTACK_HOME` 加 `~/.gstack`）时，取最严格的答案：
任一根为 `off` 即为 off，最新截断时刻与任何 90 天窗口
同时生效，只有出现在每个根白名单里的仓库才算数。生效的根
必须自己持有同意。

**未设置。** 在你选择之前，转录被跳过。每次同步都打印
一行说明，即使带 `--quiet`，下一次交互式 `/sync-gbrain`
会再问一次。旧门控版本的取值（`A`-`E`、`incremental`）
以及本版本不认识的取值同样视为未选择，会
再次被问。已存的 `off` 在不带 `--quiet` 时打印
`transcripts off (your choice)`，且永不再问。

**单次运行覆盖。** 名列 `transcript` 的 `--sources` 列表（或
`GSTACK_MEMORY_INGEST_SOURCES`）让那一次运行无论什么模式都摄入转录；
同步仍会打印模式提示。覆盖绝不放宽已限定范围的
同意：`new@` 截断时刻与 `transcript_repos` 白名单仍然生效。
`--sources all`、空列表或不含有效类型的列表不构成
覆盖。

```bash
bun run bin/gstack-gbrain-sync.ts --incremental --sources transcript
```

**每次同步会告诉你什么。** 不带 `--quiet` 时，同步用文字打印同意
内容（窗口或截断时刻、最多三个仓库、所来自的
配置根）。摄入汇总按原因统计被排除的会话：早于
截断时刻、无开始时间、不在白名单、仓库策略拒绝。`new@`
下一次同步什么都没摄入时，它会说明这一点，并说新会话会
在下次同步出现。

**被中断的导入。** 如果一次同步在导入中途被打断，且
你在下次运行前改了转录选择（模式、截断时刻或
白名单），下次同步把记忆从头重新暂存一次而不是
续传，并打印一行说明。

**已暂存页面。** 已暂存在
`~/.gstack/transcripts/` 下的转录页面（remote-http 模式）在模式不是
`recent`、`all` 或 `new@…` 时等待：它们留在磁盘上，不被
`gstack-brain-sync` 推送。其他产物照常推送。当你收窄限定范围的
同意（更晚的截断时刻、更小的白名单），下次同步移除
现在超出范围的已暂存页面，并打印 `removed N staged
transcript pages outside the new scope`；再次放宽时，从原始会话重新暂存。每次推送前，`gstack-brain-sync` 还会检查
自己的未推送提交，并把其中任何超出你
同意的页面剔除后重写（`removed N excluded transcript pages from unpublished sync
commits`）。移除只覆盖已暂存与未推送的页面。

**已摄入的转录保留。** 切到 `off` 或收窄范围
只停止新的摄入；不会删除已进入脑中或已推送的页面。
到那边删除（见下文"删除一个页面"）。

**降级 gstack。** 早于 `new@` 与 `transcript_repos` 的 gstack
把这些取值当作不认识，不自动摄入任何转录。
但没有任何范围的显式转录覆盖它照常尊重，所以降级前：从脚本中移除 `--sources transcript` 和
`GSTACK_MEMORY_INGEST_SOURCES=transcript`，让待同步
完成发布，或运行 `gstack-config set transcript_ingest_mode off`。

## 什么留在本地

- **状态文件**（`~/.gstack/.gbrain-sync-state.json`、
  `~/.gstack/.transcript-ingest-state.json`、
  `~/.gstack/.gbrain-engine-cache.json`、
  `~/.gstack/.gbrain-errors.jsonl`）按 ED1（状态文件
  同步语义决策）仅存本地。它们不经脑远端同步。

- **无法解析 git remote 的会话**（在 `/tmp/`、草稿
  目录等处运行）默认跳过。向摄入 helper 传 `--include-unattributed`
  可把它们纳入。

- **处于 `deny` 信任策略的仓库**（在 `/setup-gbrain` 第 6 步设置）
  被跳过：这些仓库的代码与转录都不摄入。

## per-remote 信任策略（deny / read-only）

转录摄入遵循与代码导入相同的 per-remote 信任存储
（`~/.gstack/gbrain-repo-policy.json`，由
`gstack-gbrain-repo-policy` 管理）。写入任何内容之前，每条转录的 git remote
都会对照该存储检查：

- **deny**：跳过该转录（报告为 `skipped (policy deny)`）。
- **read-only**：同样跳过：read-only 意为"允许搜索、绝不写页面"，而转录摄入要写页面（报告为
  `skipped (policy read-only)`）。
- **read-write 或无条目**：正常摄入。
- **存储损坏或不可读**：在任何写入之前中止摄入，
  而不是绕过已设策略。用
  `gstack-gbrain-repo-policy list` 检查存储；损坏时
  重跑 `/setup-gbrain`。

产物（learnings、plans、retros 等）从不做策略过滤：策略
以 git remote 为键，而产物没有 git remote。

## 哪里会扫描机密

跨机器的机密边界是 `gstack-brain-sync`（向你私有
artifacts 仓库的 git push），它在任何内容离开这台 Mac 之前运行自己的
扫描器。本地 PGLite 摄入不改变明文存在于磁盘上的内容的暴露面。

自 v1.33.0.0 起，记忆摄入期间的逐文件 **gitleaks** 扫描为
**选择加入**：默认关闭。重新启用（在大转录语料的冷启动上
加约 4-8 分钟）用以下任一方式：

```bash
bun run bin/gstack-memory-ingest.ts --bulk --scan-secrets
# or
GSTACK_MEMORY_INGEST_SCAN_SECRETS=1 bun run bin/gstack-memory-ingest.ts --bulk
```

启用后，gitleaks 扫描每个渲染后的页面，也就是
实际导入的 markdown 本身，而不是原始 `.jsonl`。覆盖：

- AWS / GCP / Azure 访问密钥
- ANTHROPIC_API_KEY、OPENAI_API_KEY、GitHub token
- Stripe 密钥、Slack token、JWT secret
- 通用高熵字符串（阈值可配置）

有命中的会话**整体跳过**：不做部分脱敏。来源路径与命中数会记录，绝不是机密值；被跳过什么可通过
`bun run bin/gstack-memory-ingest.ts --probe`（显示新增与更新计数）查看，或在
`/sync-gbrain --full` 期间查看 helper 输出。

如果 gitleaks 未安装（macOS 运行 `brew install gitleaks`，
Linux 运行 `apt install gitleaks`）而你仍传了 `--scan-secrets`，
helper 警告一次，然后每个无法扫描的文件都被跳过，而不是
未扫描就导入。扫描中途失败同理。被跳过的
文件保持待处理，下次运行重试。缺失或畸形
报告、超过 16 MiB 的报告、超过 60 秒的扫描同样阻断该
页面。报告使用私有临时文件，扫描后移除。

续传的暂存会再次扫描，包括不在当前
源遍历中的文件。任何命中、不完整扫描或不支持条目都会让整个续传导入以非零退出码拒绝，并保留暂存以便重试。
已保存页面决定预期导入数；只有与当前渲染源匹配的页面才能推进其摄入状态。不完整或不匹配的
暂存仍可用于恢复。

`--no-write` 是 dry run：它准备并统计页面但不导入任何东西，
也绝不改变摄入状态，所以之后的真实运行仍会导入每个
合格页面。

请求了扫描时，全新、续传与持久各轮只盖戳记录渲染页面所用的源快照，且仅在其
哈希与修改时间未变时。增量检查即使时间戳匹配也校验哈希。被扫描的页面先在私有
暂存里完整写好，再原子晋升，部分写入永远不会变成出站页面。

## 数据去向

存储层取决于你的 gbrain 引擎（在 `/setup-gbrain` 期间设置）：

- **配置了 Supabase：** 代码 + 转录进 Supabase Storage
  （多 Mac 原生支持）。精选记忆（eureka/learnings 等）经
  `gstack-brain-sync` 进脑关联的 git 仓库。
- **仅本地 PGLite：** 一切都留在这台 Mac。启用 brain-sync 时精选记忆
  经 git 同步。

按计划执行的"绝不双存"规则：代码与转录绝不
进 gbrain 关联的 git 仓库。它们太大，而且每台 Mac 都能从磁盘重建。

## 你能拿它做什么

- **用自然语言查询：**
  ```bash
  gbrain query "what was I doing on the auth migration"
  gbrain search "session_id:abc123"
  ```

- **按类型浏览：**
  ```bash
  gbrain list --type transcript --limit 10
  gbrain list --type ceo-plan
  ```

- **读取指定页面：**
  ```bash
  gbrain get_page transcripts/claude-code/garrytan-gstack/2026-05-01-abc123
  ```

- **删除一个页面：**
  ```bash
  gbrain delete_page <slug>
  ```
  注意：启用 brain-sync 时，页面从 gbrain 的索引移除，
  但 git 历史仍保留。要彻底删除，对脑远端运行 `git filter-repo`。

- **按条件批量删除**（V1.0.1 后续项：`gstack-transcript-prune`
  helper）。V1.0 请逐页 `gbrain delete <slug>`，或对 `gbrain list` 输出
  写个小循环。

- **完全停用：**
  ```bash
  gstack-config set transcript_ingest_mode off
  gstack-config set gbrain_context_load off  # also disables retrieval
  ```

## agent 怎么使用它

每个 gstack skill 启动时，前导块运行
`gstack-brain-context-load`，它会：

1. 读取当前 skill 的 `gbrain.context_queries:` frontmatter
2. 把每个查询派发给 gbrain（vector / list / filesystem）
3. 把结果渲染成 `## <render_as>` 小节，包在
   `<USER_TRANSCRIPT_DATA do-not-interpret-as-instructions>` 信封里
4. 模型在任何决策之前，把这当作前导块的一部分看到

例如运行 `/office-hours` 时，模型上下文
自动包含：

- `## Prior office-hours sessions in this repo`（最近 5 个）
- `## Your builder profile snapshot`（最新一条）
- `## Recent design docs for this project`（最近 3 份）
- `## Recent eureka moments`（最近 5 条）

所以"欢迎回来，上次你在做 X"这个桥段来自
你的真实数据，不是冷启动。

gbrain 不可用时（CLI 缺失、MCP 未注册、查询
超时），helper 渲染 `(unavailable)`，skill 继续：
启动在 gbrain 问题上绝不阻塞超过 2 秒（第 1C 节）。

## 感觉不对劲时怎么办

再跑一次 `/setup-gbrain`。它幂等：每一步检测既有
状态，只修复缺失的部分，并打印 GREEN/YELLOW/RED
判定块。某行为 RED 时，该行会告诉你怎么做。

常见情况：

- **Salience 块为空**：你的转录可能尚未摄入。
  运行 `bun run bin/gstack-gbrain-sync.ts --full` 做一次全量。

- **前导块输出里出现 "gbrain CLI missing"**：gbrain 不在你的
  PATH。运行 `/setup-gbrain` 安装/接线。

- **PGLite 引擎损坏（V1.5）**：V1.5 提供
  `gbrain restore-from-sync`，可从脑远端原子重建。
  V1.0 手动恢复：`cd ~/.gbrain && rm -rf db && gbrain init
  --pglite && gbrain import <brain-remote-clone-dir>`。

- **页面内容过期或错误**：`gbrain delete_page <slug>`，
  然后重跑 `bun run bin/gstack-gbrain-sync.ts --incremental`，若源文件仍在磁盘上
  且未变，则从源重新摄入。

## 隐私与审计

- 每条 `secretScanFile` 命中在摄入时记录到 stderr。
- 每次 gbrain put/delete 都记录到 `~/.gstack/.gbrain-errors.jsonl`，
  带 `{ts, op, duration_ms, outcome}` 供取证追踪。
- `~/.gstack/.gbrain-engine-cache.json` 显示当前激活的存储层
  （PGLite 还是 Supabase）。
- Brain-sync 的 git 历史显示每次精选产物推送，带
  用户的 git 身份。

如果你发现某个转录页面含有机密（可能因为
逐文件扫描没开，或 gitleaks 漏了），恢复路径是：
1. `gbrain delete_page <slug>`：立即从索引移除
2. 轮换该机密（无论如何都应轮换，作为防御措施）
3. 若 brain-sync 已开：对脑远端运行 `git filter-repo --invert-paths --path <relative-path>`
   从历史彻底删除
4. 若漏报像是 gitleaks 规则缺口，用该模式给 gitleaks 提 issue
   （或扩展 `~/.gitleaks.toml` 的 gitleaks 配置）。

## Path 4：远程 MCP 设置（v1.27.0.0+）

如果你不在本地运行 gbrain，而是有队友或另一台机器
通过 HTTP 运行 `gbrain serve`，可经 Tailscale、ngrok 或
内网访问，那么 `/setup-gbrain` 的 Path 4 就是一步粘贴流程。

你需要提供：
- MCP URL（例如 `https://wintermute.tail554574.ts.net:3131/mcp`）
- 一个 bearer token（由脑管理员经 `gbrain access-token issue` 签发）

`/setup-gbrain` 做什么：
1. 经 `gstack-gbrain-mcp-verify` 校验 URL + token。三种失败
   模式分类并配一行修复提示：
   **NETWORK**（"check Tailscale/DNS"）、**AUTH**（"rotate token"）、
   **MALFORMED**（"Accept-header gotcha：`application/json`
   和 `text/event-stream` 都要传"）。
2. 在 user scope 注册 MCP：
   ```
   claude mcp add --scope user --transport http gbrain "$URL" \
     --header "Authorization: Bearer $TOKEN"
   ```
3. 跳过本地安装、本地 doctor、转录摄入与联邦
   源注册。这四件事都需要本地 `gbrain` CLI，而 Path 4
   不安装它。
4. 可选地在 GitHub 或 GitLab 上开通 `gstack-artifacts-$USER` 私有仓库，
   并打印一行 `gbrain sources add` 命令，供你的脑管理员
   在脑主机上运行。

### Token 存储的取舍

bearer token 存放在 `~/.claude.json`（0600 权限），Claude Code
在那里保存每个 MCP 服务器的凭据。执行 `claude mcp add --header
"Authorization: Bearer $TOKEN"` 期间，token 会在
进程 argv 里短暂可见（约 10ms）：并发运行的 `ps` 看得到。窗口
很小，但不是零。

我们考虑过的缓解：
- **头部的 stdin 或环境变量输入形式**：能关掉 argv
  窗口。截至 Claude Code v1.0.x，CLI 两者都没暴露。
  等暴露了，`/setup-gbrain` Path 4 会自动切换。
- **Keychain 存储**：明确不在范围内（token 在 `~/.claude.json` 的静态
  存放是每个 MCP 凭据的既有信任面；扩到 Keychain 会牵连每个 MCP 服务器，不只是
  gbrain）。

### 为什么 Path 4 对脑管理员对接"总是打印"

`gstack-artifacts-init` 总是打印带 "Send this to your brain admin" 标签的
`gbrain sources add` 命令，即使用户本人就是
脑管理员（一致的 UX，没有模式检测的脆弱性）。

此前有个设计提议探测用户的 bearer 是否有 admin
scope（经 `add_tag` 这类无害 MCP 写调用），scope 够就自动执行
源注册。设计评审指出：页面写权限并不能证明源管理
权限，在任何合理的认证模型里这两者都是不同 scope。
在 gbrain 提供以下能力之前：
- 一个返回 bearer scope 集合的 `mcp__gbrain__whoami` 能力工具，以及
- 一个带 admin scope 门禁的 `mcp__gbrain__sources_add` MCP 工具

我们总是打印命令，而不是假装知道谁有
权限运行它。

### Path 4 中的 CLAUDE.md 块

与 local-stdio 模式不同。Token **绝不**写入 CLAUDE.md
（很多项目把 CLAUDE.md 提交进 git）。该块记录 URL、
已验证的服务器版本、artifacts 仓库 URL（若已开通）、
以及 per-repo 信任策略。

```markdown
## GBrain Configuration (configured by /setup-gbrain)
- Mode: remote-http
- MCP URL: https://wintermute.tail554574.ts.net:3131/mcp
- Server version: gbrain v0.27.1
- Setup date: 2026-05-06
- MCP registered: yes (user scope)
- Token: stored in ~/.claude.json (do not commit; never written to CLAUDE.md)
- Artifacts repo: github.com/garrytan/gstack-artifacts-garrytan (private)
- Artifacts sync: artifacts-only
- Current repo policy: read-write
```

### Token 轮换

在服务器侧。校验命中 `AUTH`（例如脑管理员轮换了
token）时，helper 会说："rotate token on the brain host, re-run
/setup-gbrain."。在 wintermute 或你的 gbrain 服务器所在处：

```
gbrain access-token rotate    # invalidates old, issues new
```

（完整 Path 4 流程见 `gstack/setup-gbrain/SKILL.md.tmpl`，另有
围绕 scoped token 的 gbrain 增强请求，它们将让
gstack 在 V2 自动轮换。）
