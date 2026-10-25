---
name: gstack-upgrade
version: 1.1.0
description: 把 gstack 升级到最新版本。
triggers:
  - upgrade gstack
  - update gstack version
  - get latest gstack
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`gstack-upgrade/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

<!-- AUTO-GENERATED from SKILL.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->

# /gstack-upgrade

把 gstack 升级到最新版本，并展示更新内容。

## 内联升级流程

当各 Skill 前导检测到 `UPGRADE_AVAILABLE` 时会引用本节。

### Step 1：询问用户（或自动升级）

先检查是否启用了自动升级：
```bash
_AUTO=""
[ "${GSTACK_AUTO_UPGRADE:-}" = "1" ] && _AUTO="true"
[ -z "$_AUTO" ] && _AUTO=$(~/.claude/skills/gstack/bin/gstack-config get auto_upgrade 2>/dev/null || true)
echo "AUTO_UPGRADE=$_AUTO"
```

**如果 `AUTO_UPGRADE=true` 或 `AUTO_UPGRADE=1`：**跳过 AskUserQuestion。记录日志 "Auto-upgrading gstack v{old} → v{new}..." 并直接进入 Step 2。setup 失败时，遵循 Step 4 按安装类型划分的恢复路径：vendored 安装恢复其备份；git 安装记录升级前 commit 后停止，不做破坏性 reset。除非恢复真正成功，否则绝不声称已恢复。

**否则**，使用 AskUserQuestion：
- 问题："gstack **v{new}** is available (you're on v{old}). Upgrade now?"
  四字段情形（`UPGRADE_AVAILABLE <old> <old>+<n> <sha>`，main 已移动）：问 "gstack main is **{n} commit(s)** past v{old} (at {sha}). Upgrade now?"
- 选项：["Yes, upgrade now", "Always keep me up to date", "Not now", "Never ask again"]

**若选 "Yes, upgrade now"：**进入 Step 2。

**若选 "Always keep me up to date"：**
```bash
~/.claude/skills/gstack/bin/gstack-config set auto_upgrade true
```
告诉用户："Auto-upgrade enabled. Future updates will install automatically." 然后进入 Step 2。

**若选 "Not now"：**写入带递增退避的暂缓状态（第一次暂缓 = 24 小时，第二次 = 48 小时，第三次及以后 = 1 周），然后继续当前 Skill。不要再提这次升级。
```bash
GSTACK_STATE_ROOT=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT); : "${GSTACK_STATE_ROOT:?gstack-paths failed; reinstall with ./setup or /gstack-upgrade}"
_SNOOZE_FILE="$GSTACK_STATE_ROOT/update-snoozed"
_REMOTE_VER="{new}"
_CUR_LEVEL=0
if [ -f "$_SNOOZE_FILE" ]; then
  _SNOOZED_VER=$(awk '{print $(1)}' "$_SNOOZE_FILE")
  if [ "$_SNOOZED_VER" = "$_REMOTE_VER" ]; then
    _CUR_LEVEL=$(awk '{print $(2)}' "$_SNOOZE_FILE")
    case "$_CUR_LEVEL" in *[!0-9]*) _CUR_LEVEL=0 ;; esac
  fi
fi
_NEW_LEVEL=$((_CUR_LEVEL + 1))
[ "$_NEW_LEVEL" -gt 3 ] && _NEW_LEVEL=3
echo "$_REMOTE_VER $_NEW_LEVEL $(date +%s)" > "$_SNOOZE_FILE"
```
注意：`{new}` 是 `UPGRADE_AVAILABLE` 输出中的远端版本——从更新检查结果代入。四字段行用 SHA（第四个字段）作为 `{new}`，这样 main 一移动暂缓即结束。

把暂缓时长告诉用户："Next reminder in 24h"（或 48h 或 1 week，取决于层级）。提示："Set `auto_upgrade: true` in `~/.gstack/config.yaml` for automatic upgrades."

**若选 "Never ask again"：**
```bash
~/.claude/skills/gstack/bin/gstack-config set update_check false
```
告诉用户："Update checks disabled. Run `~/.claude/skills/gstack/bin/gstack-config set update_check true` to re-enable."
继续当前 Skill。

### Step 2：检测安装类型

```bash
if [ -d "$HOME/.claude/skills/gstack/.git" ]; then
  INSTALL_TYPE="global-git"
  INSTALL_DIR="$HOME/.claude/skills/gstack"
elif [ -d "$HOME/.gstack/repos/gstack/.git" ]; then
  INSTALL_TYPE="global-git"
  INSTALL_DIR="$HOME/.gstack/repos/gstack"
elif [ -d ".claude/skills/gstack/.git" ]; then
  INSTALL_TYPE="local-git"
  INSTALL_DIR=".claude/skills/gstack"
elif [ -d ".agents/skills/gstack/.git" ]; then
  INSTALL_TYPE="local-git"
  INSTALL_DIR=".agents/skills/gstack"
elif [ -d ".claude/skills/gstack" ]; then
  INSTALL_TYPE="vendored"
  INSTALL_DIR=".claude/skills/gstack"
elif [ -d "$HOME/.claude/skills/gstack" ]; then
  INSTALL_TYPE="vendored-global"
  INSTALL_DIR="$HOME/.claude/skills/gstack"
elif _SRC=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT 2>/dev/null) && _SRC=$(awk -F '\t' '$(1) == "claude" && $(6) != "-" { print $(6); exit }' "$_SRC/installs.tsv" 2>/dev/null) && [ -d "$_SRC/.git" ]; then
  # The install registry names the checkout setup activated for this host (e.g. a ~/gstack clone).
  INSTALL_TYPE="global-git"
  INSTALL_DIR="$_SRC"
else
  echo "ERROR: gstack not found"
  exit 1
fi
INSTALL_DIR=$(cd -- "$INSTALL_DIR" && pwd -P) || { echo "ERROR: cannot enter the gstack install directory" >&2; exit 1; }
echo "Install type: $INSTALL_TYPE at $INSTALL_DIR"
```

上面打印的安装类型与绝对目录会用于后续所有步骤。
显式携带 `INSTALL_TYPE`、`INSTALL_DIR`、`OLD_VERSION` 以及稍后的 `NEW_VERSION`：工具调用可能运行在全新 shell 中，所以每个后续代码块开头都要从已捕获的输出重新赋值（例如 `INSTALL_DIR=/abs/path/printed/above`）。不要依赖上一次调用的工作目录或 shell 变量。每个会改动文件的代码块都要先检查 `INSTALL_DIR`，当它未设置、为空、缺失、不可读、或不是 gstack 自己的 checkout 时，在任何 git 命令之前停止。

### Step 3：保存旧版本

下方使用 Step 2 输出的安装目录：

```bash
OLD_VERSION=$(cat "${INSTALL_DIR:?INSTALL_DIR is not set: re-run Step 2 and substitute the printed path}/VERSION" 2>/dev/null || echo "unknown")
echo "OLD_VERSION=$OLD_VERSION"
```

### Step 4：升级

使用 Step 2 检测到的安装类型与目录：

**git 安装**（global-git、local-git）：

先做 fast-forward，通过 `bin/gstack-ff-update`——与会话更新
自动升级用的是同一套代码：能干净合并的本地编辑随更新一起
带过去；冲突的编辑（或已暂存的改动、或未合并的文件）
会被存进一个 rescue ref，而不是留成冲突标记：
```bash
cd -- "${INSTALL_DIR:?INSTALL_DIR is not set: re-run Step 2 and substitute the printed path}" || exit 1
{ [ -f VERSION ] && [ -f setup ] && [ -f bin/gstack-config ] && _p=$(git rev-parse --show-prefix 2>/dev/null) && [ -z "$_p" ] && [ "$(git rev-parse --is-inside-work-tree 2>/dev/null)" = true ]; } || { echo "ERROR: $INSTALL_DIR is not a gstack checkout; nothing was changed. Re-run Step 2." >&2; exit 1; }
git fetch origin
# Same pre-advance check as the auto-updater: the incoming release's Bun floor,
# judged by bash whatever this tool shell is (zsh does not word-split).
HOLD=$(bash -c '. bin/gstack-bun-version.sh && gstack_bun_incoming_hold . origin/main' 2>/dev/null) && { case "$HOLD" in bun-version-unreadable*) echo "BUN_VERSION_UNREADABLE: $HOLD; nothing was changed" >&2 ;; *) echo "BUN_TOO_OLD: $HOLD; nothing was changed" >&2 ;; esac; exit 1; }
PRE_UPGRADE_COMMIT=$(git rev-parse HEAD)
echo "PRE_UPGRADE_COMMIT=$PRE_UPGRADE_COMMIT"
FF=$(bash bin/gstack-ff-update . origin/main); FF_RC=$?
echo "$FF"
case "$FF_RC" in
  0) if ./setup --refresh-registered; then echo "FF_OK"; else echo "SETUP_FAILED: git update succeeded; stop and inspect setup output (previous commit: $PRE_UPGRADE_COMMIT)" >&2; exit 1; fi ;;
  4) echo "FF_REFUSED" ;;
  *) echo "FF_STOPPED: $FF" >&2; exit 1 ;;
esac
```

setup 的 `--refresh-registered` 会刷新此 checkout 注册过的每一个
安装（每台宿主的、全局的和本项目的），先打印来源，
最后以每安装一行的 `Upgrade summary` 收尾。按原样转述这些行。
`failed` 行表示该宿主保留了先前的安装；给出它的
重试命令，绝不说每个宿主都已刷新。`skipped` 行
属于另一个 checkout 或项目；转述其命令，不要执行。

如果输出以 `FF_OK` 结尾，升级即告完成——完全跳过下方
的回退流程。当它前一行读作
`rescued <old> <new> refs/gstack/rescue/<oid> unmerged=<0|1>` 时，告诉用户
他们冲突的本地编辑已保存在那里，并转述脚本打印的 `Inspect`、
`Export` 和 `Delete` 命令（导出时在临时 checkout 里用
`git apply -3`，绝不在安装目录里 `stash apply`；
`unmerged=1` 表示该 rescue 需要人工解决）。
遇 `FF_STOPPED`，STOP 并转述原因：什么都没有被改动。
`ff-busy` 表示另一个 gstack 更新正在运行（一分钟后重试）；
`autostash-unrecoverable` 点名是什么挡了路（某个新版本
会新增的未跟踪文件，或另一条 git 命令）；`index-unreadable` 表示 checkout 的
索引已损坏。
遇 `BUN_TOO_OLD`，STOP：让用户运行 `bun upgrade`，然后再次运行 /gstack-upgrade。
遇 `BUN_VERSION_UNREADABLE`，STOP：`bun --version` 没有打印出 gstack 能读取的版本，所以 `bun upgrade` 可能同样跑不起来；让用户从 https://bun.sh 重装 Bun（在 Git Bash 或 macOS/Linux 终端里执行 `curl -fsSL https://bun.sh/install | bash`），确认 `bun --version` 打印出类似 1.4.2 的版本，然后再运行一次 /gstack-upgrade（docs/troubleshooting.md#bun-version-unreadable）。
遇 `SETUP_FAILED`，STOP；保留用户改动并报告恢复用 commit。git 路径上没有 `.bak`。不要仅因 setup 失败就进入分叉回退。仅在 `FF_REFUSED`（本地 commit 或历史分叉）时进入；网络/认证失败停下来修理，而不是重置。

**回退（ff-only 被拒——本地 commit 或历史分叉）。**`git reset
--hard` 会毁东西：即使工作树干净，未推送的本地 commit
也会丢。必须设门：

1. 在 `$INSTALL_DIR` 中运行 `git status --porcelain` 和
   `git rev-list origin/main..HEAD --oneline`。
2. 如果两者都为空，这次 reset 可证明是安全的——不经询问直接运行
   下方的回退代码块。
3. 否则用 AskUserQuestion 询问（单向门——破坏性），逐项列出
   将被丢弃的内容：每个脏文件和每个未推送的 commit，
   附 hash + 主题。选项：**A)** Discard them and upgrade (reset)——
   必须显式键入字母；**B)** Abort the upgrade，让用户先抢救
   自己的工作（存在本地 commit 时为推荐项）。绝不在
   含糊回复上继续。

```bash
cd -- "${INSTALL_DIR:?INSTALL_DIR is not set: re-run Step 2 and substitute the printed path}" || exit 1
{ [ -f VERSION ] && [ -f setup ] && [ -f bin/gstack-config ] && _p=$(git rev-parse --show-prefix 2>/dev/null) && [ -z "$_p" ] && [ "$(git rev-parse --is-inside-work-tree 2>/dev/null)" = true ]; } || { echo "ERROR: $INSTALL_DIR is not a gstack checkout; nothing was changed. Re-run Step 2." >&2; exit 1; }
# Regenerable render-footprint dirt (setup re-renders it) never goes into the stash.
git checkout -- 'SKILL.md' '*/SKILL.md' '*/sections/*.md' 2>/dev/null || true
STASH_OUTPUT=$(git stash 2>&1)
git reset --hard origin/main
./setup --refresh-registered
```
如果 `$STASH_OUTPUT` 包含 "Saved working directory"，警告用户："Note: local changes were stashed (any modified generated SKILL.md/sections files were discarded first — they regenerate on setup). Run `git stash pop` in the skill directory to restore your own changes."

**vendored 安装**（vendored、vendored-global）：
```bash
(cd -- "${INSTALL_DIR:?INSTALL_DIR is not set: re-run Step 2 and substitute the printed path}" && [ -f VERSION ] && [ -f setup ] && [ -f bin/gstack-config ]) || { echo "ERROR: INSTALL_DIR=${INSTALL_DIR:-} is not a gstack install; nothing was changed. Re-run Step 2." >&2; exit 1; }
# A stale .bak from a previously crashed upgrade would make the mv below NEST
# the live install inside it and the failure-restore arm would "restore" the
# stale backup. It may also be the only good copy from that crashed run —
# abort and let the human inspect, never delete it silently.
[ -e "$INSTALL_DIR.bak" ] && { echo "ERROR: stale backup exists at $INSTALL_DIR.bak (from a previous failed upgrade?) — inspect it, salvage/remove it, then re-run." >&2; exit 1; }
TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/gstack-upgrade.XXXXXX") || { echo "ERROR: mktemp failed — aborting upgrade (install untouched)." >&2; exit 1; }
git clone --depth 1 https://github.com/garrytan/gstack.git "$TMP_DIR/gstack" || { echo "ERROR: clone failed — aborting upgrade (install untouched)." >&2; rm -rf "$TMP_DIR"; exit 1; }
mv "$INSTALL_DIR" "$INSTALL_DIR.bak" || { rm -rf "$TMP_DIR"; exit 1; }
if mv "$TMP_DIR/gstack" "$INSTALL_DIR"; then
  if (cd "$INSTALL_DIR" && ./setup --refresh-registered); then
    rm -rf "$INSTALL_DIR.bak" "$TMP_DIR"
  else
    rm -rf "$INSTALL_DIR"
    mv "$INSTALL_DIR.bak" "$INSTALL_DIR" || { echo "ERROR: restore failed; backup retained." >&2; exit 1; }
    rm -rf "$TMP_DIR"
    echo "ERROR: setup failed; previous install restored." >&2
    exit 1
  fi
else
  mv "$INSTALL_DIR.bak" "$INSTALL_DIR"
  echo "ERROR: swap failed — previous install restored; upgrade aborted." >&2
  rm -rf "$TMP_DIR"
  exit 1
fi
```

### Step 4.5：处理本地 vendored 副本

使用 Step 2 的安装目录。检查是否还存在本地 vendored 副本，以及团队模式是否开启：

```bash
_RESOLVED_PRIMARY=$(cd -- "${INSTALL_DIR:?INSTALL_DIR is not set: re-run Step 2 and substitute the printed path}" && pwd -P) || exit 1
_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
LOCAL_GSTACK=""
if [ -n "$_ROOT" ] && [ -d "$_ROOT/.claude/skills/gstack" ]; then
  _RESOLVED_LOCAL=$(cd "$_ROOT/.claude/skills/gstack" && pwd -P)
  if [ "$_RESOLVED_LOCAL" != "$_RESOLVED_PRIMARY" ]; then
    LOCAL_GSTACK="$_ROOT/.claude/skills/gstack"
  fi
fi
_TEAM_MODE=$(~/.claude/skills/gstack/bin/gstack-config get team_mode 2>/dev/null || echo "false")
echo "LOCAL_GSTACK=$LOCAL_GSTACK"
echo "TEAM_MODE=$_TEAM_MODE"
```

**如果 `LOCAL_GSTACK` 非空且 `TEAM_MODE` 为 `true`：**删除 vendored 副本。团队模式以全局安装为唯一事实来源。

```bash
(cd -- "${LOCAL_GSTACK:?LOCAL_GSTACK is not set: re-run the detection block above and substitute the printed path}" && [ -f VERSION ] && [ -f setup ] && [ -f bin/gstack-config ]) || { echo "ERROR: LOCAL_GSTACK=${LOCAL_GSTACK:-} is not a gstack copy; nothing was changed." >&2; exit 1; }
_ROOT=${LOCAL_GSTACK%/.claude/skills/gstack}
{ [ "$_ROOT" != "$LOCAL_GSTACK" ] && cd -- "${_ROOT:?}" && _p=$(git rev-parse --show-prefix 2>/dev/null) && [ -z "$_p" ] && [ "$(git rev-parse --is-inside-work-tree 2>/dev/null)" = true ]; } || { echo "ERROR: $LOCAL_GSTACK is not the vendored copy at the root of a git repository; nothing was changed." >&2; exit 1; }
git rm -r --cached .claude/skills/gstack/ 2>/dev/null || true
if ! grep -qF '.claude/skills/gstack/' .gitignore 2>/dev/null; then
  echo '.claude/skills/gstack/' >> .gitignore
fi
rm -rf "$LOCAL_GSTACK"
```
告诉用户："Removed vendored copy at `$LOCAL_GSTACK` (team mode active — global install is the source of truth). Commit the `.gitignore` change when ready."

**如果 `LOCAL_GSTACK` 非空且 `TEAM_MODE` 不为 `true`：**从刚升级完的主安装复制更新它（与 README 的 vendored 安装同一做法）：
```bash
(cd -- "${INSTALL_DIR:?INSTALL_DIR is not set: re-run Step 2 and substitute the printed path}" && [ -f VERSION ] && [ -f setup ] && [ -f bin/gstack-config ]) || { echo "ERROR: INSTALL_DIR=${INSTALL_DIR:-} is not a gstack install; nothing was changed." >&2; exit 1; }
(cd -- "${LOCAL_GSTACK:?LOCAL_GSTACK is not set: re-run the detection block above and substitute the printed path}" && [ -f VERSION ] && [ -f setup ] && [ -f bin/gstack-config ]) || { echo "ERROR: LOCAL_GSTACK=${LOCAL_GSTACK:-} is not a gstack copy; nothing was changed." >&2; exit 1; }
[ -e "$LOCAL_GSTACK.bak" ] && { echo "ERROR: stale vendored backup; inspect it before retrying." >&2; exit 1; }
mv "$LOCAL_GSTACK" "$LOCAL_GSTACK.bak" || exit 1
if cp -Rf "$INSTALL_DIR" "$LOCAL_GSTACK" && rm -rf "$LOCAL_GSTACK/.git" && (cd "$LOCAL_GSTACK" && ./setup --refresh-registered); then
  rm -rf "$LOCAL_GSTACK.bak"
  echo "LOCAL_SYNC_OK"
else
  rm -rf "$LOCAL_GSTACK"
  mv "$LOCAL_GSTACK.bak" "$LOCAL_GSTACK" || { echo "ERROR: restore failed; backup retained." >&2; exit 1; }
  echo "ERROR: sync failed; previous vendored copy restored." >&2
  exit 1
fi
```
仅在 `LOCAL_SYNC_OK` 时告诉用户："Also updated vendored copy at `$LOCAL_GSTACK` — commit `.claude/skills/gstack/` when you're ready." 否则停止并报告恢复结果；不要继续迁移或宣布成功。

### Step 4.75：运行版本迁移

`./setup` 完成后，运行旧版本与新版本之间所有版本的迁移脚本。
迁移处理 `./setup` 单独覆盖不到的状态修复
（过期配置、孤儿文件、目录结构变更）。

```bash
MIGRATIONS_DIR="${INSTALL_DIR:?INSTALL_DIR is not set: re-run Step 2 and substitute the printed path}/gstack-upgrade/migrations"
: "${OLD_VERSION:?OLD_VERSION is not set: substitute the value Step 3 printed}"
if [ -d "$MIGRATIONS_DIR" ]; then
  for migration in $(find "$MIGRATIONS_DIR" -maxdepth 1 -name 'v*.sh' -type f 2>/dev/null | sort -V); do
    # Extract version from filename: v0.15.2.0.sh → 0.15.2.0
    m_ver="$(basename "$migration" .sh | sed 's/^v//')"
    # Run if this migration version is newer than old version
    # (simple string compare works for dotted versions with same segment count)
    if [ "$OLD_VERSION" != "unknown" ] && [ "$(printf '%s\n%s' "$OLD_VERSION" "$m_ver" | sort -V | head -1)" = "$OLD_VERSION" ] && [ "$OLD_VERSION" != "$m_ver" ]; then
      echo "Running migration $m_ver..."
      # GSTACK_INSTALL_DIR: migrations that clean the INSTALL (not just
      # ~/.gstack state) default to ~/.claude/skills/gstack when unset —
      # a repo-local install would silently no-op without this.
      GSTACK_INSTALL_DIR="$INSTALL_DIR" bash "$migration" || echo "  Warning: migration $m_ver had errors (non-fatal)"
    fi
  done
fi
```

迁移是 `gstack-upgrade/migrations/` 里的幂等 bash 脚本。每个都命名
为 `v{VERSION}.sh`，只在从更旧版本升级时运行。如何新增迁移
见 CONTRIBUTING.md。

### Step 4.8：停掉所有过期守护进程（无条件执行）

升级前启动的 browse 守护进程在被停掉之前会一直跑旧二进制的
代码——它能在 `git reset --hard` 和 `./setup` 之后幸存，因为运行中的
进程持有旧的可执行文件。此步骤始终执行，使用
Step 2 检测到的安装目录。

```bash
INSTALL_DIR_PLACEHOLDER="<install dir from Step 2>"
NEW_HASH=$(cat "$INSTALL_DIR_PLACEHOLDER/browse/dist/.version" 2>/dev/null || echo "")
_STATE_FILE="${BROWSE_STATE_FILE:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/browse.json}"
if [ -z "$NEW_HASH" ] || [ ! -f "$_STATE_FILE" ]; then
  echo "DAEMON_CHECK=none (no state file or no fresh build hash)"
else
  DAEMON_PID=$(sed -n 's/.*"pid"[[:space:]]*:[[:space:]]*\([0-9][0-9]*\).*/\1/p' "$_STATE_FILE" | head -1)
  DAEMON_PORT=$(sed -n 's/.*"port"[[:space:]]*:[[:space:]]*\([0-9][0-9]*\).*/\1/p' "$_STATE_FILE" | head -1)
  OLD_HASH=$(sed -n 's/.*"binaryVersion"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$_STATE_FILE" | head -1)
  if [ -z "$DAEMON_PID" ] || ! kill -0 "$DAEMON_PID" 2>/dev/null; then
    echo "DAEMON_CHECK=dead (no live daemon to stop)"
  elif [ "$OLD_HASH" = "$NEW_HASH" ]; then
    echo "DAEMON_CHECK=current (daemon already runs the new binary)"
  elif curl -fsS --max-time 2 "http://127.0.0.1:$DAEMON_PORT/health" 2>/dev/null | grep -q '"status":"healthy"'; then
    echo "DAEMON_CHECK=stale-responsive pid=$DAEMON_PID hash=${OLD_HASH:-unknown} -> $NEW_HASH"
    "$INSTALL_DIR_PLACEHOLDER/browse/dist/browse" stop && echo "DAEMON_STOPPED=yes"
  else
    echo "DAEMON_CHECK=stale-busy pid=$DAEMON_PID hash=${OLD_HASH:-unknown} -> $NEW_HASH"
  fi
fi
```

运行前把 `<install dir from Step 2>` 替换为实际的安装目录。
按以下方式解读 `DAEMON_CHECK` 结果：

1. **`stale-responsive` + `DAEMON_STOPPED=yes`：**告诉用户 "Stopped the
   old browse daemon (binary {OLD_HASH} → {NEW_HASH}). The next browse command
   starts a fresh daemon on the new binary."
2. **`stale-busy`：**守护进程跑的是旧二进制但正在干活——让位于
   它，绝不在升级期间杀死忙碌的守护进程。告诉用户："A browse daemon
   is still running the pre-upgrade binary ({OLD_HASH} → {NEW_HASH}) but is
   busy right now. When it finishes, stop it with `browse stop` — or force it
   immediately with `browse --force-restart stop` (loses that session's
   tabs/cookies/logins)."
3. **`none` / `dead` / `current`：**无事可做——什么都不说。

### Step 5：写入标记 + 清缓存

```bash
GSTACK_STATE_ROOT=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT); : "${GSTACK_STATE_ROOT:?gstack-paths failed; reinstall with ./setup or /gstack-upgrade}"
mkdir -p "$GSTACK_STATE_ROOT"
echo "$OLD_VERSION" > "$GSTACK_STATE_ROOT"/just-upgraded-from
rm -f "$GSTACK_STATE_ROOT"/last-update-check
rm -f "$GSTACK_STATE_ROOT"/update-snoozed
```

### Step 6：展示更新内容

阅读 `$INSTALL_DIR/CHANGELOG.md`。找出旧版本与新版本之间的所有版本条目。按主题分组成 5-7 条摘要。不要堆砌——聚焦面向用户的变更。内部重构除非重大，否则跳过。

四字段情形：把 `git -C "$INSTALL_DIR" log --oneline <PRE_UPGRADE_COMMIT>..HEAD`（≤7 条）摘要表述为 "gstack v{old}, main at {sha}"。

格式：
```
gstack v{new} — upgraded from v{old}!

What's new:
- [bullet 1]
- [bullet 2]
- ...

Happy shipping!
```

### Step 7：继续

展示完更新内容后，继续用户最初调用的那个 Skill。升级已完成——无需进一步操作。

---

## 独立使用

当直接以 `/gstack-upgrade` 调用（而非来自前导）时：

1. 强制做一次新的更新检查（绕过缓存）：
```bash
~/.claude/skills/gstack/bin/gstack-update-check --force 2>/dev/null || \
.claude/skills/gstack/bin/gstack-update-check --force 2>/dev/null || true
```
根据输出判断是否有可用升级。

2. 若为 `UPGRADE_AVAILABLE`（三或四个字段）：遵循上面的 Step 2-6。

   若为 `CHECK_FAILED ...`：远端版本读不到，更新状态
   未知。展示该行（它点名失败的 URL）并告诉
   用户检查失败；绝不报告"已是最新版本"。停止。

3. 若无输出（主安装已是最新）：检查是否有过期的本地 vendored 副本。

运行上面的 Step 2 bash 代码块检测主安装的类型与目录（`INSTALL_TYPE` 和 `INSTALL_DIR`）。然后运行上面的 Step 4.5 检测 bash 代码块，检查本地 vendored 副本（`LOCAL_GSTACK`）与团队模式状态（`TEAM_MODE`）。

**如果 `LOCAL_GSTACK` 为空**（无本地 vendored 副本）：告诉用户 "You're already on the latest version (v{version})."

**如果 `LOCAL_GSTACK` 非空且 `TEAM_MODE` 为 `true`：**用上面 Step 4.5 的团队模式移除 bash 代码块删除 vendored 副本。告诉用户："Global v{version} is up to date. Removed stale vendored copy (team mode active). Commit the `.gitignore` change when ready."

**如果 `LOCAL_GSTACK` 非空且 `TEAM_MODE` 不为 `true`**，比较版本：
```bash
PRIMARY_VER=$(cat "${INSTALL_DIR:?INSTALL_DIR is not set: re-run Step 2 and substitute the printed path}/VERSION" 2>/dev/null || echo "unknown")
LOCAL_VER=$(cat "${LOCAL_GSTACK:?LOCAL_GSTACK is not set: re-run the Step 4.5 detection block}/VERSION" 2>/dev/null || echo "unknown")
echo "PRIMARY=$PRIMARY_VER LOCAL=$LOCAL_VER"
```

**如果版本不同：**遵循上面 Step 4.5 的同步 bash 代码块，用主安装更新本地副本。告诉用户："Global v{PRIMARY_VER} is up to date. Updated local vendored copy from v{LOCAL_VER} → v{PRIMARY_VER}. Commit `.claude/skills/gstack/` when you're ready."

**如果版本相同：**告诉用户 "You're on the latest version (v{PRIMARY_VER}). Global and local vendored copy are both up to date."
