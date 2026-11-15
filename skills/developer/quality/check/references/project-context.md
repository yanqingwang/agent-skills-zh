> **中文汉化版** · 上游：[tw93/Waza](https://github.com/tw93/Waza) · 原文件：`skills/check/references/project-context.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 项目审查上下文模板

运行 Waza `/check` 之前，用本模板压缩仓库上下文。上下文必须来自公开项目文件、diff、CI 配置或明确的用户指示。不得依赖私有机器路径或未公开的项目指令。

## 哪些内容属于项目上下文

下面的模板已覆盖大部分。另外还要记录：

- 受保护的文件和目录。
- 打包的事实来源：归档是由 `git ls-files`、显式 allowlist、生成的 manifest 还是源目录构建。
- 交付面：生成的产物是被追踪、被忽略、外部 release 资产、registry 上传、appcast、安装器元数据，还是站点/下载文案；它们如何再生成、检查、staging 或上传。
- diff 引入的运行时依赖：CI/文档中尚未声明的 Python 包、CLI、网络服务、包管理器或平台工具。
- 领域专属的安全规则。
- 项目已记录的已知 CI 或测试 flaky，以及如何把它们与真实失败区分开。

## 哪些内容不属于公开上下文

- 凭证路径、私钥文件名、密码、token 或秘密值。
- 仅维护者可用的机器路径。
- 不影响项目行为的一次性个人偏好。
- 被当作指引复制过来的一次性审查报告、记分卡或诊断快照，而不是蒸馏成稳定的项目规则。
- 来自其他项目的原始记忆、聊天摘录、截图、私有支持细节、本地路径、项目专属命令、issue/PR 编号、release tag 或 commit 哈希。
- Waza `/check` 各节的完整复制。

## 推荐的上下文形态

```markdown
## Project Commands

- Format: `<command>`
- Fast check: `<command>`
- Full verification: `<command>`

## CLI Command Surface

- Entrypoints: `<command or bin>`.
- Command contract: help/version, subcommands, flags, exit codes, stdout/stderr, JSON/schema output.
- Runtime shape: TTY vs non-interactive behavior, env/config precedence, completion/manpage or shell integration.
- Install/run proof: built package, temp prefix, PATH shim, shebang/executable bit, or package-manager path checked with `<command>`.
- Mutating commands: dry-run/confirmation, operation log, rollback/retry behavior, signal/partial-failure handling.

## Skill Or Plugin Install Surface

- User install path: `<package manager / release archive / marketplace entry / plugin id / installer script>`.
- Source path and generated mirror: `<source dir>` -> `<installed dir>`.
- Package/archive inclusion: new scripts, references, templates, rules, manifests, and executable bits checked with `<command>`.
- Isolated install smoke: fresh temp home/config/cache plus `<install command>` and `<list or invoke command>`.
- Noise filtering: cache files, local logs, screenshots, and temp outputs excluded or intentionally shipped.

## Project Hard Stops

- Do not modify `<protected path>` unless explicitly requested.
- If `<artifact>` is generated from `<source>`, verify it was regenerated.
- If `<artifact>` is ignored by git but required for release, verify the regeneration and force-stage, upload, or registry publish path named by the project.
- If `<package script>` builds from tracked files or an allowlist, verify newly introduced helpers, references, templates, and scripts are included in `<archive>`.
- If an installer fetches remote content, verify the default ref is pinned to a release tag or checksum-protected; floating `main` must be an explicit override.
- If a helper introduces a non-stdlib package or external CLI, verify CI installs it or the helper fails with a clear setup path.
- If `<artifact>` is listed in release notes, verify it exists before sign-off.

## Project-Specific Risks

- `<risk>`: `<how to inspect it>`

## Public Replies

See `public-reply.md` for posting, edit-or-new-comment, read-back, and closure criteria; the reply body follows `/write` Public Reply Mode. Do not restate the rules here.

## Release Follow-through

- Version fields to check: `<manifest>`, `<app config>`, `<lockfile>`.
- Generated artifacts to check: `<artifact>` from `<source>`.
- Distribution lane: `<preview/beta/nightly/stable/etc.>` and which public surfaces it is allowed to touch.
- Dry-run command before publishing: `<command>`.
- Remote asset proof: `<download/readback command>` that checks content, manifest, digest, appcast, or registry state.
- GitHub release reactions to add after asset verification: `<+1/laugh/heart/hooray/rocket/eyes or none>`.
- Public state to re-read after publishing or closing: `<registry/release/issue URL or command>`.
```

保持这份上下文简短。它为审查提供指引，不替代审查方法。

## Release Gate 2.0 矩阵

声称改动可以发布之前，先填完这张表。只有当项目确实没有对应面时才写 "n/a"。

| 面 | 证据 |
|---|---|
| Review base | 已审查的基线分支、最新 tag 和 commit 范围 |
| Worktree state | 脏文件、暂存文件和 untracked 文件都有交代 |
| Remote state | 已核对 `origin/main` 或发布分支的同步 |
| Version fields | manifest、应用配置、changelog、appcast 和 lockfile 的版本对齐 |
| Distribution lane | 指明了 preview、beta、nightly、stable、registry 或应用商店通道，无关通道未被触碰 |
| Runtime dependencies | 新引入的 Python 包、CLI、包管理器和网络工具已声明且在 CI 中可用 |
| Generated artifacts | 被追踪的归档、被忽略的 dist 输出、bundle/压缩文件、appcast、安装器元数据、checksum、站点/下载文案已再生成，或证明不再需要 |
| Package/archive contents | 检查了构建包中的必需文件、新引入的 helper/引用，以及缺失的 extras |
| Installed runtime | 当 diff 改动可安装面时，在干净环境中实际执行了包、skill、插件、CLI 或 marketplace 安装 |
| Release assets | GitHub release、appcast、下载归档、checksum 或安装器资产已下载或读回，验证超出页面文字或文件大小 |
| Registry/appcast | 发布后重新读取了 npm/crates/Homebrew/appcast/App Store 或等价状态 |
| CI status | 最新必需检查通过，或点名了阻塞项 |
| Issue/PR state | 评论、关闭、合并或宣布发布之前重新读取了目标 issue 或 PR |

## 安全敏感汇点（sink）审查

任何触碰以下汇点的 diff 都需要明确的验证和回滚思考：

- 删除、移动或覆盖用户文件、缓存、历史记录、偏好设置或生成产物。
- 从用户输入构建 shell、AppleScript、SQL、URL 或文件系统路径。
- 改变 cwd 处理、symlink 解析、路径穿越防护、沙箱权限、审批检查或鉴权提示。
- 改变签名、公证、appcast、更新、许可、支付或 release 资产生成。
- 改变 CI workflow、发布或发布脚本、安装器，或任何以提升权限运行的东西。

审查到达汇点的最小入口，再向下看调用链。验证缺失或回滚不清晰时，按硬停处理。

### 按路径划分的风险层级

层级跟随改动触碰的路径，不跟随其大小或作者。对 workflow、更新器、许可检查、安装器、提权 helper 或删除路径的一行改动，适用项目最重的门（完整或原生测试运行、一次安全审查、一名人类维护者的审查），agent、bot 或自动化审查者的批准不能顶替那个人。从项目文档提取它的层级；当项目保存了一个表驱动脚本、会为被改路径打印对应的门时，运行它并粘贴其输出行。这样的脚本只是建议，不是通行证：它点名的门可能在本会话无法证明其运行过的地方执行。该层级的 commit 和 PR 还要说明自己如何被验证、如何回滚（`mode-ship.md` 第 4 步）。
