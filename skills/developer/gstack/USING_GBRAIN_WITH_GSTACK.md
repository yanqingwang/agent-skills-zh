> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/USING_GBRAIN_WITH_GSTACK.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 在 GStack 中使用 GBrain

你的编码 agent，配上它真正记得住的记忆。

[GBrain](https://github.com/garrytan/gbrain) 是一个为 AI agent 设计的持久知识库。它存下你的 agent 学到的东西、你做过的决定、哪些有效哪些无效，并让 agent 按需检索这一切。GStack 给你一条从零到"gbrain 已运行、我的 agent 能调用它"的单命令路径，覆盖本地试用、与团队共享以及两者之间的各种形态。

这是完整版：每个场景、每个标志、每个 helper bin、每个排障步骤。快速介绍见 [README 的 GBrain 一节](README.md#gbrain--persistent-knowledge-for-your-coding-agent)。错误码与同步专属问题见 [docs/gbrain-sync.md](docs/gbrain-sync.md)。

---

## 一条命令安装

```bash
/setup-gbrain
```

就这样。skill 检测你的当前状态，最多问三个问题，带你走完安装、init、Claude Code 的 MCP 注册和 per-repo 信任策略。在什么都没装的干净 Mac 上五分钟内完成。在已有部分设置的 Mac 上只要几秒（它检测既有状态并跳过已完成的工作）。

## 设置完成后你得到什么

`/setup-gbrain` 完成后，你的编码 agent 多了两个以前没有的检索面：

- **跨本仓库的语义代码搜索。** `gbrain search "browser security canary"` 返回按相关性排序的文件区域，不是精确匹配的 grep 命中。`gbrain code-def`、`code-refs`、`code-callers`、`code-callees` 按符号遍历调用图：不知道实现在哪个文件、但知道它做什么时很好用。问题偏语义时，agent 优先用它们而非 Grep；CLAUDE.md 会得到一个 `## GBrain Search Guidance` 块，教它路由规则。
- **跨会话记忆。** 过去会话的 plans、retros、决策与 learnings 存放在 `~/.gstack/`，并且（若你选择加入 artifacts sync）推送到一个 gbrain 会索引的私有 git 仓库。`gbrain search "what did we decide about auth?"` 真能找到当初的 CEO 计划，而不是你每个会话重新描述一遍上下文。

如果你还启用了远程 MCP（下文 Path 4），脑查询会路由到一台其他机器也能写入的共享脑服务器：你的笔记本、台式机和队友的机器看到同一份记忆。

## 四条路径

skill 问"你的脑应该住在哪？"时，你从中选一个。

### Path 1：Supabase，你已有连接串

适合：你（或队友的云 agent）已经开通了 Supabase 脑，想让这台本地机器使用同一份数据。

**会发生什么：** 粘贴 Session Pooler URL（Settings → Database → Connection Pooler → Session → copy URI，端口 6543）。skill 关闭回显读取它，给你看脱敏预览（`aws-0-us-east-1.pooler.supabase.com:6543/postgres`，主机可见，密码打码），经 `GBRAIN_DATABASE_URL` 环境变量交给 `gbrain init`，URL 绝不写入 argv 或你的 shell 历史。

**信任警告：** 粘贴这个 URL 等于给你的本地 Claude Code 对共享脑里每个页面的完整读写权限。这不是你想要的信任级别的话，改选 PGLite 本地（Path 3），并接受两边脑互不相通。

### Path 2a：Supabase，自动开通新项目

适合：全新的 Supabase 账号，想要零点击得到一个干净的新项目。

**会发生什么：** 你粘贴一个 Supabase Personal Access Token（PAT）。skill 先展示范围披露：*该 token 对你 Supabase 账号里每个项目都有完整访问权限，不只是我们将创建的那个*。它列出你的组织，询问选哪个组织和哪个区域（默认 `us-east-1`），生成数据库密码，调用 `POST /v1/projects`，每 5 秒轮询 `GET /v1/projects/{ref}` 直到项目 `ACTIVE_HEALTHY`（180 秒超时），取回 pooler URL，交给 `gbrain init`。端到端约 90 秒。

最后：明确提醒到 https://supabase.com/dashboard/account/tokens 吊销该 PAT。skill 已把它从内存丢弃。

**开通途中 Ctrl-C：** SIGINT 陷阱会打印你进行中的项目 ref 和一条续办命令。你可以在 Supabase 仪表盘删掉这个孤儿项目，或运行 `/setup-gbrain --resume-provision <ref>` 从中断处继续。

### Path 2b：Supabase，手动创建

适合：你宁愿自己在 supabase.com 上点，也不愿粘贴 PAT。

**会发生什么：** skill 带你走完四个手动步骤（注册 → 新项目 → 等约 2 分钟 → 复制 Session Pooler URL），然后从 Path 1 的粘贴步骤接管。安全处理与 Path 1 相同。

### Path 3：PGLite 本地

适合：先试试看，无账号、无云、不共享。或一个与任何云 agent 隔离的专用"这台 Mac 的脑"。

**会发生什么：** `gbrain init --pglite`。脑位于 `~/.gbrain/brain.pglite`。init 本身不发起网络调用。30 秒完成。

**嵌入模型。** 设置了 `VOYAGE_API_KEY` 时，gstack 以 `voyage-code-3`（1024 维）初始化 PGLite，这是 Voyage 的代码专用嵌入模型，在本代码库的符号查询上正面对比优于其通用型 `voyage-4-large` 和 OpenAI 的 `text-embedding-3-large`。没有 `VOYAGE_API_KEY` 时，gbrain 自动选择（有 `OPENAI_API_KEY` 就用 OpenAI 1536 维，否则沿其 provider 链下探）。无论哪种，嵌入都在同步期间调用所选 provider 的 API：运行 `/sync-gbrain` 前先设好你想要 provider 的密钥。

如果你只想在上云前感受一下 gbrain，这是最好的首选。以后随时可用 `/setup-gbrain --switch` 迁移。

### Path 4：远程 gbrain MCP（双引擎分离）

适合：你的脑运行在你控制的另一台机器上（Tailscale、ngrok、内网）或队友的服务器。你想要跨机器记忆的好处、又不想架设本地数据库，同时仍想在这台 Mac 上有符号感知的代码搜索。

**会发生什么：** 你粘贴一个 MCP URL（如 `https://wintermute.tail554574.ts.net:3131/mcp`）和一个 bearer token。skill 经网络验证 URL，把 gbrain 注册为 `~/.claude.json` 里 user scope 的 HTTP MCP，并提议再架一个小型本地 PGLite 用于代码搜索（约 30 秒，约 120 MB 磁盘）。

如果你接受本地 PGLite，就进入**双引擎分离模式（split-engine）**：

- **脑/上下文查询**（`mcp__gbrain__search`、`mcp__gbrain__query`、`mcp__gbrain__get_page`）路由到远程 MCP。Plans、retros、learnings、跨机器记忆：全在共享服务器上。
- **代码查询**（`gbrain code-def`、`code-refs`、`code-callers`、`code-callees`，以及面向代码的 `gbrain search`）经每个 worktree 的 `.gbrain-source` pin 路由到本地 PGLite。本地索引，快，绝不出机。

在这台机器的回环地址（`localhost`、`127.0.0.1`、`::1`）上运行 `gbrain serve --http`、且后端是这台机器自己的 Postgres 脑，不算 Path 4。那是 gbrain 为 Postgres 脑上的本地 agent 推荐的设置（`gbrain bootstrap harness`），gstack 把它当作本地脑：转录在这里经 `gbrain import` 摄入。gstack 只凭 URL 与本地 gbrain 配置判断，且只有带 Postgres `database_url` 的配置才算数。回环 URL 搭配本地 PGLite 仍是 Path 4，所以上面那套双引擎分离设置在你经 SSH 隧道或回环端口转发访问远程脑时照常工作。

两个引擎相互独立。清空本地 PGLite 不影响远程脑；轮换远程 MCP bearer 不影响本地代码搜索。如果远程脑管理员不能（或不该）索引每个开发者的 checkout，这也是正确配置：本地代码留在本地。

## 为 Claude Code 注册 MCP

默认情况下 skill 会问"要为 gbrain 给 Claude Code 一个带类型的工具面吗？"你答是，它就运行：

```bash
claude mcp add gbrain -- gbrain serve
```

这会把 gbrain 的 stdio MCP 服务器注册给 Claude Code。此后 `gbrain search`、`gbrain put`、`gbrain get` 等在每个会话里都是一等工具，不是 bash 外调。

**若 `claude` 不在 PATH**，skill 优雅跳过 MCP 注册并给出手动注册提示。CLI 解析器仍对任何会外调 `gbrain` 的 skill 有效：MCP 是升级项，不是前置条件。

**其他本地 agent**（Cursor、Codex CLI 等）需要各自的 MCP 注册。v1 的 skill 以 Claude Code 为目标；其他宿主可在自己的 MCP 配置里手动注册 `gbrain serve`。

## per-remote 信任策略（三元组）

你机器上每个仓库都有一个策略决定：**read-write**、**read-only** 或 **deny**。

- **read-write**：你的 agent 能在本仓库上下文中 `gbrain search`，还能把新页面写回脑。自己的项目默认用它。
- **read-only**：你的 agent 能搜索脑，但绝不从本仓库的会话写入新页面。多客户顾问的理想选择：搜索共享脑，在客户 B 的仓库里时不让客户 A 的代码污染它。
- **deny**：完全不与 gbrain 交互。该仓库对 gbrain 工具不可见。

第一次在该仓库运行 gstack skill 时，skill 逐仓库问一次。之后决定即固定：同一 git remote 的每个 worktree 和分支共享同一策略，设一次就跟着你走。

SSH 与 HTTPS 两种 remote 写法折叠为同一个键：`https://github.com/foo/bar.git` 与 `git@github.com:foo/bar.git` 是同一个仓库。

**修改策略：**

```bash
/setup-gbrain --repo      # re-prompt for this repo only

# Or directly:
~/.claude/skills/gstack/bin/gstack-gbrain-repo-policy set "github.com/foo/bar" read-only
```

**查看所有策略：**

```bash
~/.claude/skills/gstack/bin/gstack-gbrain-repo-policy list
```

存储：`~/.gstack/gbrain-repo-policy.json`，权限 0600，带 schema 版本，未来迁移保持确定性。

## 用 `/sync-gbrain` 让脑保持最新

`/setup-gbrain` 是一次性引导。`/sync-gbrain` 是你每次想让 gbrain 看到本仓库代码新变化时运行的动词。

```bash
/sync-gbrain                # incremental: mtime fast-path, ~seconds on a clean tree
/sync-gbrain --full         # full reindex (~25-35 minutes on a big Mac)
/sync-gbrain --code-only    # only the code stage; skip memory + brain-sync
/sync-gbrain --dry-run      # preview what would sync; no writes
```

skill 独立运行三个阶段：code、memory、brain-sync。一个失败不阻塞其他。状态持久化到 `~/.gstack/.gbrain-sync-state.json`，重跑能干净接续。

可能把数据送出机器的阶段（同步代码进可能远程的 gbrain 数据库、记忆摄入、brain-sync 推送）都会在发送前向出口账本（`~/.gstack/security/egress.jsonl`）写一条防篡改回执，fail-closed：回执写不出来时，该阶段以 `EGRESS_RECEIPT_FAILED` 拒绝，而不是无记录地同步。修复通常是 `mkdir -p ~/.gstack/security && chmod -R u+w ~/.gstack/security`，然后重跑。用 `gstack-egress list` 检查回执。

**在全新 worktree 上它做什么：**

1. **预检。** 检查 `gbrain_local_status`（本地引擎健康度）。引擎是 `broken-db` 或 `broken-config` 时，skill 停止（STOP）并给出修复菜单：它拒绝静默降级。本地引擎缺失且你处于远程 MCP 模式（Path 4）时，code 阶段干净地跳过（SKIP），只跑 brain-sync。
2. **code 阶段。** 经 `gbrain sources add` 把 cwd 注册为联邦源，在仓库根写一个 `.gbrain-source` pin 文件（kubectl 风格的 context：每个 worktree 有自己的 pin，Conductor 兄弟 worktree 互不冲突），运行 `gbrain sync --strategy code`。
3. **memory 阶段。** 暂存你的 `~/.gstack/` 转录 + 精选记忆。local-stdio MCP 模式下摄入本地引擎。remote-http MCP 模式下把暂存的 markdown 持久化到 `~/.gstack/transcripts/run-<pid>-<ts>/`，供远程脑管理员的拉取管线使用。摄入超时默认 30 分钟；脑很大时用 `GSTACK_INGEST_TIMEOUT_MS` 调高（接受 1 分钟至 24 小时）。超时时 gbrain import 检查点被保留，下一次 `/sync-gbrain` 从断点续传而不是从头再来。
4. **brain-sync 阶段。** 若配置了私有 artifacts 仓库，把精选产物（plans、designs、retros）推送上去。
5. **CLAUDE.md 指引。** 对往返做能力检查（写一个页面 → 搜索 → 找到它）。绿色则把 `## GBrain Search Guidance` 块写进你项目的 CLAUDE.md。红色则移除该块：绝不该告诉 agent 去用一个没安装的工具。

**水位线。** 同步状态按提交哈希推进。gbrain 碰到无法索引的文件（每文件 5 MB 硬上限，或文件在同步中途消失）时，水位线原地不动，后续同步重试。要承认一个无法修复的失败并越过它：

```bash
gbrain sync --source <source-id> --skip-failed
```

可重复运行、幂等，同一机器多终端并发运行安全（锁在 `~/.gstack/.sync-gbrain.lock`）。

## 以后切换引擎

选了 PGLite，现在想加入团队脑？一条命令：

```bash
/setup-gbrain --switch
```

skill 在 `timeout 180s` 包裹下运行 `gbrain migrate --to supabase --url "$URL"`。迁移是双向的（Supabase → PGLite 也行）且无损：pages、chunks、embeddings、links、tags、timeline 全部复制。原脑保留为备份。

**迁移卡住：** 可能是另一个 gstack 会话锁住了源脑。3 分钟触发超时，消息可直接行动。关掉其他工作区再重跑。

## GStack 记忆同步（另一件事）

这与 gbrain 本身是两回事。你的 gstack 状态（`~/.gstack/`：learnings、plans、retros、timeline、developer profile）默认只在单机。"GStack 记忆同步"可选地把一个精选、扫过机密的子集推到私有 git 仓库，让记忆跨机器跟着你，而且如果你在跑 gbrain，那个 git 仓库也能被索引。

这样开启：

```bash
gstack-artifacts-init
```

你会看到一次性的隐私提示：**everything allowlisted** / **artifacts only**（plans、designs、retros、learnings，跳过 timeline 这类行为数据）/ **off**。每次 skill 运行在开始和结束时同步队列：没有守护进程，没有后台进程。

形似机密的内容（AWS 密钥、GitHub token、PEM 块、JWT、bearer token）在离开你的机器之前就被挡在同步之外。

**在新机器上：** 把 `~/.gstack-artifacts-remote.txt` 拷过来（旧名
`~/.gstack-brain-remote.txt` 仍有效），运行 `gstack-brain-restore`，
昨天的 learnings 就出现在今天的笔记本上。

完整指南：[docs/gbrain-sync.md](docs/gbrain-sync.md)。错误索引：[docs/gbrain-sync-errors.md](docs/gbrain-sync-errors.md)。

`/setup-gbrain` 会在初始设置结束时提议帮你接好：多一次 AskUserQuestion，并接入同一套私有仓库基础设施。

## 清理孤儿项目

如果你在开通途中 Ctrl-C 过、换过三个名字才定下来，或以其他方式攒了一堆没在用的 gbrain 形态 Supabase 项目，有个子命令处理这个：

```bash
/setup-gbrain --cleanup-orphans
```

skill 重新收集一个 PAT（一次性，用后丢弃），列出你 Supabase 账号里每个名字以 `gbrain` 开头、且 ref 与你当前 `~/.gbrain/config.json` pooler URL 不匹配的项目。对每个孤儿逐项目询问：*"Delete orphan project `<ref>` (`<name>`, created `<date>`)?*"，不批量、没有"全部删除"捷径。当前脑永远不会被提供删除。

## 命令与标志参考

### `/setup-gbrain` 入口模式

| 调用方式 | 作用 |
|---|---|
| `/setup-gbrain` | 完整流程：检测状态、选路径、安装、init、MCP、策略、可选的 memory-sync |
| `/setup-gbrain --repo` | 只为当前仓库翻转 per-remote 信任策略 |
| `/setup-gbrain --switch` | 迁移引擎（PGLite ↔ Supabase），不重跑其他步骤 |
| `/setup-gbrain --resume-provision <ref>` | 续办在轮询期间被打断的 Path 2a 自动开通 |
| `/setup-gbrain --cleanup-orphans` | 列出并逐项目删除孤儿 Supabase 项目 |

### Bin helper（供脚本使用）

| Bin | 用途 |
|---|---|
| `gstack-gbrain-detect` | 把当前状态输出为 JSON：gbrain 在不在 PATH、版本、配置引擎、doctor 状态、同步模式。`--doctor` 运行 `/setup-gbrain` 第 5 步用的完整脑健康门禁（`gbrain doctor --json --scope=brain`）；打印 `brain_ok`、`brain_failures` 与 `skill_failures`，仅当 `brain_ok` 为真才退出 0。失败的 skill 检查（gbrain 给另一个 agent 的 skills 目录打分）绝不影响 `brain_ok`。 |
| `gstack-gbrain-install` | 先检测再安装（依次探测 `~/git/gbrain`、`~/gbrain`，然后全新克隆）。有 `--dry-run` 与 `--validate-only` 标志。PATH 遮蔽检查以退出码 3 失败并给出修复菜单。 |
| `gstack-gbrain-lib.sh` | 供 source，不可执行。提供 `read_secret_to_env VARNAME "prompt" [--echo-redacted "<sed-expr>"]` |
| `gstack-gbrain-supabase-verify` | 结构性 URL 检查。拒绝直连 URL（`db.*.supabase.co:5432`），退出码 3 |
| `gstack-gbrain-supabase-provision` | Management API 包装器。子命令：`list-orgs`、`create`、`wait`、`pooler-url`、`list-orphans`、`delete-project`。全部要求环境变量 `SUPABASE_ACCESS_TOKEN`。`create` 与 `pooler-url` 还要求 `DB_PASS`。每个子命令都有 `--json` 模式。 |
| `gstack-gbrain-repo-policy` | per-remote 信任三元组。子命令：`get`、`set`、`list`、`normalize` |
| `gstack-gbrain-source-wireup` | 经 `gbrain sources add` + `git worktree` 把你的 `~/.gstack/` 脑仓库注册为 gbrain 联邦源，然后跑一次初始 `gbrain sync`。幂等。取代 v1.12.x 已死的 `consumers.json + /ingest-repo` HTTP wireup。标志：`--strict`、`--source-id <id>`、`--no-pull`、`--uninstall`、`--probe`。 |

### gbrain CLI（上游工具）

gbrain 自带这些命令，gstack 对其包装：

| 命令 | 用途 |
|---|---|
| `gbrain init --pglite` | 初始化本地 PGLite 脑 |
| `gbrain init --non-interactive` | 经环境变量初始化（`GBRAIN_DATABASE_URL` 或 `DATABASE_URL`）。绝不要把 URL 放进 argv：它会泄漏到 shell 历史。 |
| `gbrain doctor --json` | 健康检查。返回 `{status: "healthy"|"warnings"|"unhealthy" (older gbrain: "ok"), health_score: 0-100, checks: [...]}`。`--scope=brain`（gbrain v0.41.20+）跳过 skill 检查。 |
| `gbrain migrate --to supabase --url ...` | 把 PGLite 脑迁到 Supabase（无损，源保留为备份） |
| `gbrain migrate --to pglite` | 反向迁移 |
| `gbrain search "query"` | 搜索脑 |
| `gbrain put "<slug>" --content "<markdown-with-frontmatter>"` | 写一个页面（title/tags 放在 `--content` 内的 YAML frontmatter 里） |
| `gbrain get "<slug>"` | 取一个页面 |
| `gbrain serve` | 启动 MCP stdio 服务器（`claude mcp add` 使用） |

### 配置文件与状态

| 路径 | 存放什么 |
|---|---|
| `~/.gbrain/config.json` | 引擎（pglite/postgres）、数据库 URL 或路径、API 密钥。权限 0600。由 `gbrain init` 写入。 |
| `~/.gstack/gbrain-repo-policy.json` | per-remote 信任三元组。schema v2。权限 0600。 |
| `~/.gstack/.setup-gbrain.lock.d` | 并发运行锁（原子 mkdir）。正常退出与 SIGINT 时释放。 |
| `~/.gstack/.brain-queue.d/` | gstack 记忆同步的待同步记录，maildir 风格 spool，一条记录一个文件。旧版的 `.brain-queue.jsonl` 会在下次 drain 时自动迁移。 |
| `~/.gstack/.brain-last-push` | 上次同步推送的时间戳（供 `/health` 打分） |
| `~/.gstack-artifacts-remote.txt` | 你的 gstack 记忆同步远端的 URL（可跨机器复制；旧名 `~/.gstack-brain-remote.txt` 仍可读） |
| `~/.gstack/.setup-gbrain-inflight.json` | 保留给未来 `--resume-provision` 的持久化状态 |

### 环境变量

| 变量 | 在哪读取 | 作用 |
|---|---|---|
| `SUPABASE_ACCESS_TOKEN` | `gstack-gbrain-supabase-provision` | 调 Management API 用的 PAT。每次设置运行后丢弃。 |
| `DB_PASS` | `gstack-gbrain-supabase-provision`（create、pooler-url） | 生成的数据库密码。绝不进 argv。 |
| `GBRAIN_DATABASE_URL` | `gbrain init`、`gbrain doctor` 等 | Postgres 连接串（对我们来说是 Supabase pooler URL）。环境变量优先于 `~/.gbrain/config.json`。 |
| `DATABASE_URL` | `gbrain init`（回退） | 与 `GBRAIN_DATABASE_URL` 语义相同；第二个检查。 |
| `SUPABASE_API_BASE` | `gstack-gbrain-supabase-provision` | 覆盖 Management API 主机。测试用它指向 mock 服务器。 |
| `GBRAIN_INSTALL_DIR` | `gstack-gbrain-install` | 覆盖默认安装路径（`~/gbrain`） |
| `GSTACK_HOME` | 每个 bin helper | 覆盖 `~/.gstack` 状态目录。测试重度使用。 |
| `VOYAGE_API_KEY` | `gbrain embed` 子进程；gstack PGLite init | 设置时，gstack 以 `voyage-code-3`（1024 维）初始化 PGLite，Voyage 的代码专用嵌入模型。在本代码库的符号查询上正面对比优于 `voyage-4-large` 与 OpenAI `text-embedding-3-large`。A/B 数据见 CHANGELOG v1.43.1.0。 |
| `OPENAI_API_KEY` | `gbrain embed` 子进程 | 未设 `VOYAGE_API_KEY` 时，用于 `gbrain sync` / `/sync-gbrain` 期间的嵌入（gbrain 自动选择的回退，`text-embedding-3-large` 1536 维）。两个密钥都没有时，页面按结构导入（符号表、chunks），但语义搜索降级：同步日志里会看到 `[gbrain] embedding failed for code file ...`。 |
| `ANTHROPIC_API_KEY` | `claude-agent-sdk`、付费评估 | 付费评估（`bun run eval:bg:pr`）及任何对 Claude 的直接 `query()` 调用所需。 |
| `GSTACK_OPENAI_API_KEY` | `lib/conductor-env-shim.ts` | Conductor 注入的回退。规范名为空时提升为 `OPENAI_API_KEY`。 |
| `GSTACK_ANTHROPIC_API_KEY` | `lib/conductor-env-shim.ts` | 与上相同的 Anthropic 模式。 |

## Conductor 与 GSTACK_* 环境变量

如果你在 [Conductor](https://conductor.build) 工作区里运行 gstack，**Conductor 会明确从工作区环境里剥掉 `ANTHROPIC_API_KEY` 和 `OPENAI_API_KEY`。** 在 `~/.zshrc` 或 `.env` 里设置没有用：剥离发生在环境继承之后。要把可用的 API 密钥送进工作区，改为在 Conductor 的工作区 env 配置里设置 `GSTACK_ANTHROPIC_API_KEY` 与 `GSTACK_OPENAI_API_KEY`。Conductor 原样放行这两个。

`lib/conductor-env-shim.ts` 在 gstack 侧补上这个缺口：作为副作用导入（`import "../lib/conductor-env-shim";`）时，它为任何看不到规范名的子进程把 `GSTACK_FOO_API_KEY` 提升为 `FOO_API_KEY`。该 shim 已接入：

- `bin/gstack-gbrain-sync.ts`：让 `/sync-gbrain` 取到 OpenAI 做嵌入
- `bin/gstack-model-benchmark`：让 `--judge` 运行无需手工环境映射
- `scripts/preflight-agent-sdk.ts`：让付费评估的认证探测可用
- `test/helpers/e2e-helpers.ts`：让付费评估找得到 Anthropic

新增会打付费 API 或需要 gbrain 嵌入的 TS 入口时，在顶部加上同样的一行导入。贡献者清单见 [CONTRIBUTING.md 的 "Conductor workspaces"](CONTRIBUTING.md#conductor-workspaces)。

`bin/gstack-codex-probe` 是 bash，不直接读这些：它依赖 Codex CLI 管理的 `~/.codex/` 认证。

## 安全模型

本 skill 接触的每个机密都守一条规则：**只走环境变量，绝不进 argv，绝不进日志，也绝不由我们写盘。** 唯一的持久存储是 gbrain 自己的 `~/.gbrain/config.json`（0600 权限），那是 gbrain 的纪律，不是我们的。

**代码内强制：**

- `test/skill-validation.test.ts` 里的 CI grep 测试在 `$SUPABASE_ACCESS_TOKEN` 或 `$GBRAIN_DATABASE_URL` 出现在 argv 位置时让构建失败
- `--insecure`、`-k` 或 `NODE_TLS_REJECT_UNAUTHORIZED=0` 出现在 `bin/gstack-gbrain-supabase-provision` 中时 CI grep 测试失败
- provision helper 顶部的 `set +x` 防止调试追踪泄漏 PAT
- 遥测载荷只含枚举的类别值（scenario、install result、MCP opt-in、trust tier）：绝不含可能带机密的自由字符串

**经测试强制：**

- `test/secret-sink-harness.test.ts` 用播种的机密运行每个处理机密的 bin，断言种子绝不出现在任何被捕获的通道（stdout、stderr、`$HOME` 下的文件、遥测 JSONL）。每个种子四种匹配规则：精确、URL 解码、前 12 字符前缀、base64。
- 同一测试文件里的阳性对照在每个被覆盖通道故意泄漏种子，并断言 harness 抓到每一个。没有阳性对照，静默漏报的 harness 看起来就和正常工作的一样。

**你仍然可能泄漏的**（v1 的诚实边界）：

- 你把机密粘进 `read -s` 之外的普通聊天消息，它就进了会话转录和任何宿主侧日志
- 泄漏 harness 不转储子进程环境：一个执行 `env >> ~/.log` 的 bin 能躲过检测（v1 没有这样的 bin；grep 测试防着它）
- 你 shell 自己的 `HISTFILE` 行为归你的 shell 管，不归我们：我们从不把机密传进 argv，所以它们不会经我们的代码落进去，但没人拦得住你亲手把机密粘进一条裸 `curl` 命令

## 排障

### 安装期间 "PATH SHADOWING DETECTED"

PATH 里另一个 `gbrain` 二进制排在安装器刚链接的那个前面。安装器的版本检查抓到了它。修复任选其一：

- 不需要另一个就 `rm $(which gbrain)`
- 在 shell rc 里把 `~/.bun/bin` 前置到 PATH，让刚链接的二进制胜出
- 把 `GBRAIN_INSTALL_DIR` 设为遮蔽二进制的安装目录并重跑

然后重跑 `/setup-gbrain`。

### "rejected direct-connection URL"

你粘贴了 `db.<ref>.supabase.co:5432` URL。它们只有 IPv6，在多数环境会失败。改用 Session Pooler URL：Supabase 仪表盘 → Settings → Database → Connection Pooler → **Session** → copy URI（端口 6543）。

### 自动开通在 180 秒超时

Supabase 项目还在初始化。你的 ref 已打印在退出消息里。等一分钟，然后：

```bash
/setup-gbrain --resume-provision <ref>
```

skill 重新收集 PAT，跳过项目创建，继续轮询。

### "Another `/setup-gbrain` instance is running"

你有一个过期的锁目录。确认确实没有其他实例在运行的话：

```bash
rm -rf ~/.gstack/.setup-gbrain.lock.d
```

然后重跑。

### 策略文件报 "No cross-model tension"

你手工编辑 `~/.gstack/gbrain-repo-policy.json` 用了旧版 `allow` 取值？没问题。下次读取时，gstack 自动把 `allow` 迁移为 `read-write` 并加 `_schema_version: 2`。stderr 一行日志，幂等，确定。

### `gbrain doctor` 报 "warnings"

`/health` 把它当黄色，不当红色。用 `gbrain doctor --json | jq .checks` 看哪些子检查在告警。典型原因：resolver MECE 重叠（skill 名冲突）或数据库连接尚未配置。

### `/sync-gbrain` 报 `OK` 但 `gbrain search` 搜不出语义结果

嵌入很可能在导入时失败了。符号查询（`code-def`、`code-refs`）仍然可用，因为它们不需要嵌入，但 `gbrain search "<terms>"` 会退到降级的 BM25 路径。在同步输出里找这样的行：

```
[gbrain] embedding failed for code file <name>: OpenAI embedding requires OPENAI_API_KEY
```

修复方法：重跑前把 provider API 密钥放进进程环境。代码场景首选 `VOYAGE_API_KEY`（设置时 gstack 默认 PGLite 用 `voyage-code-3`）；否则 `OPENAI_API_KEY` 回退到 `text-embedding-3-large`。在裸 Mac shell 上，调用前从 `~/.zshrc` source 密钥。Conductor 里，`lib/conductor-env-shim.ts` shim 自动把 `GSTACK_ANTHROPIC_API_KEY` / `GSTACK_OPENAI_API_KEY` 提升为规范名；`VOYAGE_API_KEY` 则直接设在 Conductor 工作区 env 里。重跑 `/sync-gbrain --code-only` 可为已导入页面回填嵌入。

### `gbrain sync` 卡在某个提交哈希：`FILE_TOO_LARGE`

你树里的某个文件超过 gbrain 的 5 MB 硬上限（`gbrain/src/core/import-file.ts` 的 `MAX_FILE_SIZE`）。常见元凶：响应回放缓存、截图、大型 JSON fixture。gbrain 的代码同步不认 `.gitignore` 风格的排除清单；唯一的旋钮是确认该失败：

```bash
gbrain sync --source <source-id> --skip-failed
```

水位线越过问题提交。同一文件再变更会再失败；届时再次跳过。

### ZeroEntropy 嵌入在 2026 年 9 月 4 日后失效

ZeroEntropy 被 Notion 收购，其托管 API 于 **2026 年 9 月 4 日**停服（新注册已停）。配置了 `zeroentropyai` 嵌入配方的 gbrain 在那之后仍继续导入页面，但嵌入静默失败：页面按结构落地，没有语义搜索。你的 `~/.gbrain/config.json` 指名该配方时，wireup helper 会警告；请在截止日前迁移到其他 provider（经 `VOYAGE_API_KEY` 用 Voyage，或经 `OPENAI_API_KEY` 用 OpenAI）。细节、自托管注意事项与迁移讨论：[garrytan/gstack#2365](https://github.com/garrytan/gstack/issues/2365)。

### PGLite → Supabase 切换卡住

兄弟 Conductor 工作区里的另一个 gstack 会话可能经其前导块的 `gstack-brain-sync` 调用锁住了你的本地 PGLite 文件。关掉其他工作区，重跑 `/setup-gbrain --switch`。超时上限 180 秒，不会真的永远等下去。

## 为什么这样设计

**为什么是 per-remote 信任三元组，而不是二元 allow/deny？** 多客户顾问需要只搜不写回。上午服务客户 A、下午服务客户 B 的自由开发者，不能让 A 的代码洞见泄漏进 B 可搜索的脑。read-only 干净地解决了这个问题。

**为什么不把 gbrain 捆进 gstack？** Gbrain 是独立、活跃开发的项目，有自己的发布节奏、schema 迁移和 MCP 面。捆绑意味着 gstack 必须给 gbrain 更新设闸，这会拖慢 gbrain 改进到达用户的速度。分离但集成，让各自按自己的节奏发布。

**为什么 `gbrain init --non-interactive` 走环境变量而不是标志？** 连接串含数据库密码。放 argv 会让密码落进 `ps`、shell 历史和进程列表。环境变量交接让机密只留在进程内存。Gbrain 同时支持 `GBRAIN_DATABASE_URL` 和 `DATABASE_URL`；我们用前者，避免与非 gbrain 工具撞名。

**为什么 PATH 遮蔽要硬失败，而不是警告后继续？** 被遮蔽的 `gbrain` 意味着后续每条命令调用的都是另一个二进制，不是我们刚装的那个。这是静默的版本漂移 bug，几周后以神秘的功能缺失浮现。安装类 skill 只有一件事：装出一个能用的环境。拒绝装进一个坏环境才是 setup skill 的正确行为。

**为什么不自动导入每个仓库？** 隐私 + 噪音。一个摄入你碰过的每个仓库的自动导入前导块 Hook 会：(a) 未经同意把工作代码泄漏进共享脑，(b) 用一次性仓库堵死搜索。per-remote 策略让摄入成为显式的逐仓库决定。`/setup-gbrain` 今天不装任何自动导入 Hook，但策略存储为将来接入留了前向兼容。

## 相关 skill 与下一步

- `/health`：其 0-10 综合分含 GBrain 维度（doctor 状态、同步队列深度、上次推送距今时间）。gbrain 未安装时该维度省略；在非 gbrain 机器上运行 `/health` 不会因此扣分。
- `/gstack-upgrade`：保持 gstack 自身最新。不会独立升级 gbrain。gbrain 默认装最新 HEAD；要刷新，在你的 gbrain 克隆（默认 `~/gbrain`）里 `git pull` 后重跑 `/setup-gbrain`。需要可复现性就用 `gstack-gbrain-install --pinned-commit <sha>` 固定到特定提交。低于最低已测版本的安装会被拒绝。
- `/retro`：memory sync 开启时，每周复盘从你的 gbrain 拉取 learnings 与 plans，让复盘能引用跨机器历史。

跑一次 `/setup-gbrain`，看看哪些留得下来。
