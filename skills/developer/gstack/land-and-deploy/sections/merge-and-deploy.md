<!-- AUTO-GENERATED from merge-and-deploy.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`land-and-deploy/sections/merge-and-deploy.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Step 4：合并 PR

仅带 Step 3.5 对该 `PR_HEAD` 的批准进入。记录开始时间；初始化
`MERGE_ATTEMPT=none`、`MERGE_EXIT=0`、`MERGE_ERROR=''`、
`WAITED=false`。回读之间保持这些值；绝不为重试而重置。从 Deploy
Configuration 解析 `MERGE_METHOD`，并
`gh api "repos/$REPO" --jq '{squash: .allow_squash_merge, merge: .allow_merge_commit, rebase: .allow_rebase_merge}'`。
未配置时优先 squash，其次 merge，再次 rebase。不允许/未知的方式：
**STOP** 并询问。`MERGE_FLAG` 取 `--squash`、`--merge` 或 `--rebase`。
以下回读在**首次尝试之前**、每次尝试之后以及等待期间都要跑。它是唯
一的派发器；没有任何命令会漏到另一种合并。

### 4a-postfail：失败后的 PR 状态检查

**通用不变量：**`gh pr merge` 任何非零退出之后，重试或停止之前先查
权威 PR 状态。绝不盲目重试。参考：cli/cli#3442、cli/cli#13380。
`gh pr view` 不暴露队列成员身份；`autoMergeRequest` 与
`mergeQueueEntry` 都用 GraphQL。字段失败/不支持/缺失是未知，绝不是
"请求或队列条目不存在"的证据。

```bash
READBACK=$(gh api graphql -f query='query($owner:String!,$name:String!,$number:Int!) {
  repository(owner:$owner,name:$name) { pullRequest(number:$number) {
    state headRefOid baseRefName mergedAt mergeCommit { oid }
    autoMergeRequest { enabledAt } mergeQueueEntry { id state }
  } }
}' -f owner="${REPO%/*}" -f name="${REPO#*/}" -F number="$PR_NUMBER") || exit 1
printf '%s' "$READBACK" | jq -e '
  ((.errors // []) | length == 0) and
  (.data.repository.pullRequest | type == "object" and
    has("state") and has("headRefOid") and has("baseRefName") and has("mergeCommit") and
    has("autoMergeRequest") and has("mergeQueueEntry"))' >/dev/null || exit 1
PR_STATE=$(printf '%s' "$READBACK" | jq -er '.data.repository.pullRequest.state') || exit 1
CURRENT_HEAD=$(printf '%s' "$READBACK" | jq -er '.data.repository.pullRequest.headRefOid') || exit 1
CURRENT_BASE=$(printf '%s' "$READBACK" | jq -er '.data.repository.pullRequest.baseRefName') || exit 1
ACTIVE_REQUEST=$(printf '%s' "$READBACK" | jq -r '.data.repository.pullRequest | .autoMergeRequest != null or .mergeQueueEntry != null')
MERGE_ACTION=STOP
case "$PR_STATE" in
  MERGED)
    if [ "$CURRENT_HEAD" != "$PR_HEAD" ] || [ "$CURRENT_BASE" != "$BASE_BRANCH" ]; then
      MERGE_ACTION=MERGED_CHANGED
    else
      MERGE_ACTION=MERGED
    fi ;;
  OPEN)
    if [ "$CURRENT_HEAD" != "$PR_HEAD" ]; then
      MERGE_ACTION=HEAD_CHANGED
    elif [ "$CURRENT_BASE" != "$BASE_BRANCH" ]; then
      MERGE_ACTION=BASE_CHANGED
    elif [ "$ACTIVE_REQUEST" = true ]; then
      MERGE_ACTION=WAIT
    elif [ "$WAITED" = true ]; then
      MERGE_ACTION=STOP
    elif [ "$MERGE_ATTEMPT" = none ]; then
      MERGE_ACTION=START
    elif [ "$MERGE_ATTEMPT" = auto ] && [ "$MERGE_EXIT" -ne 0 ]; then
      case "$MERGE_ERROR" in
        *"Auto-merge is not allowed for this repository"*|*"Pull request is in clean status"*|*"Pull request is in unstable status"*) MERGE_ACTION=DIRECT ;;
      esac
    fi ;;
esac
printf '%s\n' "$MERGE_ACTION"
```

回读失败或状态未知：**STOP**，保留命令错误、不合并。
HEAD_CHANGED/BASE_CHANGED：批准作废，**STOP** 并回到 Step 1 与新目
标的就绪流程。MERGED_CHANGED：报告权威的外部合并，但在变更的
head/base 对账之前**STOP** 清理/部署/回滚；旧的范围/批准不可用，绝
不重放。WAIT 进 §4a。STOP 呈现原始 stderr 与当前状态。**若
`state == "CLOSED"`：STOP**，PR 未合并即被关闭。

只有 START 做第一次尝试。任一合并命令执行之前立即重复回读与
Step 1 的本地 HEAD/分支/洁净检查。改目标或本地变更使就绪失效；
`--match-head-commit` 保护的是 head，不是目的地。
每个合并块都带 Step 3.5 的批准重跑 CI 门（`--auto` 也一样，它只等必
需检查）。门退出意味着没有合并发生：带其输出 **STOP**。只有分支保
护或合并队列让"检查到合并"成为原子。
```bash
CI_GATE=$(~/.claude/skills/gstack/bin/gstack-ci-gate --repo "$REPO" --pr "$PR_NUMBER" --expect-head "$PR_HEAD" "${CI_OVERRIDE[@]}")
echo "$CI_GATE"
case "${CI_GATE%%$'\n'*}" in "VERDICT PASS $PR_HEAD"|"VERDICT NO_CHECKS $NO_CI_APPROVED_HEAD") ;; *) exit 1 ;; esac
MERGE_ATTEMPT=auto
MERGE_EXIT=0
MERGE_ERROR=$(gh pr merge "$MERGE_FLAG" --auto --delete-branch "$PR_NUMBER" --repo "$REPO" --match-head-commit "$PR_HEAD" 2>&1) || MERGE_EXIT=$?
```
回到回读，exit 0 也一样。只有 DIRECT 允许**一次直接兜底**：回读已
确认 OPEN、无 auto 请求也无队列条目，且 auto 尝试返回了两类已文档化
拒绝之一：auto-merge 被禁用，或 PR 已 clean/unstable 且无必需检查
待跑。后者不等于 auto-merge 被禁用。
```bash
CI_GATE=$(~/.claude/skills/gstack/bin/gstack-ci-gate --repo "$REPO" --pr "$PR_NUMBER" --expect-head "$PR_HEAD" "${CI_OVERRIDE[@]}")
echo "$CI_GATE"
case "${CI_GATE%%$'\n'*}" in "VERDICT PASS $PR_HEAD"|"VERDICT NO_CHECKS $NO_CI_APPROVED_HEAD") ;; *) exit 1 ;; esac
MERGE_ATTEMPT=direct
MERGE_EXIT=0
MERGE_ERROR=$(gh pr merge "$MERGE_FLAG" --delete-branch "$PR_NUMBER" --repo "$REPO" --match-head-commit "$PR_HEAD" 2>&1) || MERGE_EXIT=$?
```
回到回读。direct 尝试没有兜底。**硬规则：MERGED 之后绝不重放合并，
绝不重试未知状态/错误。不用 `--admin` 绕过。**

**若 `state == "MERGED"`：**

服务端合并成功（可能本地清理阶段失败之前就完成了，或有并发合并落
地）。告诉用户："PR 在 GitHub 上已合并。"（不要说"合并成功"，这
样说能覆盖并发合并的情况。）

捕获合并 SHA：
```bash
MERGE_SHA=$(printf '%s' "$READBACK" | jq -er '.data.repository.pullRequest.mergeCommit.oid') || exit 1
```

squash/rebase 合并回读守卫：
- **不要**用"PR head SHA 是 base 分支祖先"来证明成功。GitHub 的
  squash 与 rebase 合并有意创建新 commit，所以即使 PR 已合并，
  `git merge-base --is-ancestor <head_sha> origin/<base>` 也可能失
  败。
- GitHub 报告 `state == "MERGED"` 且 `mergeCommit.oid` 非空即为权
  威。记录合并 SHA 并继续。
- 需要本地清理或回读时，fetch base 分支并与合并 commit 对比/同步，
  而不是旧的 PR 分支 commit：
```bash
git fetch "https://github.com/$REPO.git" "$BASE_BRANCH"
git diff --quiet "$MERGE_SHA" FETCH_HEAD || git log --oneline --decorate -1 "$MERGE_SHA" FETCH_HEAD
```
- 工作区干净、只是想让 squash 合并后不再显得分叉时，优先在合并
  commit 上建具名本地分支而非 detached HEAD，例如
  `git switch -c "post-merge/pr-$PR_NUMBER" "$MERGE_SHA"`（宿主有分
  支前缀就用它的，如 Codex Desktop 的 `codex/`，其 git action 工作
  进程要求 `git symbolic-ref --short HEAD` 返回一个分支）。绝不
  force-push 或 reset 用户的分支，除非他们明确要求。

工作区清理，非破坏性、基于候选：
```bash
git worktree list --porcelain
```
识别候选：worktree 过期的条件是 (a) 检出在 base 分支上，且 (b) 不
是用户当前主工作树，且 (c) 其内部 `git status --porcelain` 为空
（无未提交工作）。

- 每个干净候选：提议移除。说："`<path>` 有一个检出在 `<branch>`
  上、无未提交工作的过期 worktree。移除吗？"仅用户确认后移除
  （`git worktree remove <path> && git worktree prune`）。
- 候选有未提交工作：列出文件、告诉用户，不做任何移除地停止工作区
  清理。
- 绝不用 `--force`。绝不移除用户的主工作树。

远端分支对账：`--delete-branch` 可能没完成。验证分支结果，而不是从
合并 exit code 推断清理完成：

```bash
# gh leaves .headRepository.nameWithOwner EMPTY (gh 2.83): compose owner/name
# from headRepositoryOwner.login + headRepository.name.
IFS=$'\t' read -r HEAD_REPO HEAD_BRANCH <<< "$(gh pr view "$PR_NUMBER" --repo "$REPO" --json headRepositoryOwner,headRepository,headRefName \
  --jq '"\(.headRepositoryOwner.login)/\(.headRepository.name)\t\(.headRefName)"')"
case "$HEAD_REPO" in ''|/*|*/) HEAD_BRANCH= ;; esac
[ -n "$HEAD_BRANCH" ] && echo "HEAD: $HEAD_REPO $HEAD_BRANCH" && git ls-remote --heads "https://github.com/$HEAD_REPO.git" "refs/heads/$HEAD_BRANCH"
```

这些名字是 PR 数据：留在这些变量里，绝不重打。PR head 仓库是分支的
权威位置：同仓库 PR 就是 base 仓库；fork PR 就是那个 fork。不要拿检
出仓库的 `origin` 替代。没有 `HEAD:` 行表示查询失败：把分支状态视为
未知，不跑删除路径。

三种结果，绝不把失败的检查读成干净的分支：

- **exit 0、空输出**：远端分支已不在（GitHub 的合并后删除或并发行为
  先到了）。告诉用户："远端分支已被清理。"这让恢复流程的重跑保持
  幂等。
- **exit 0、一条 ref 行**：分支还在：失败的合并命令从没跑到它的
  `--delete-branch` 那一半。`HEAD_REPO` 等于 REPO 时提议删除，先确
  认（与上方工作区清理的姿态一致）："远端分支 `<head-branch>` 在
  `<head-repository>` 仍存在，失败的合并没有执行它的
  --delete-branch 部分。删除吗？"仅在确认后重跑该块前三行，然后
  `git push "https://github.com/$HEAD_REPO.git" --delete "refs/heads/$HEAD_BRANCH"`。
  `HEAD_REPO` 是 FORK 时不提议删除：分支属于贡献者，维护者通常在
  那里没有推送权；改为报告："分支在贡献者的 fork
  `<head-repository>` 上，留给他们处理。"存在同名本地分支时，同时
  提议 `git branch -d "$HEAD_BRANCH"`（`-d`，绝无 `-D`：非快进的
  本地分支由用户定夺）。
- **非零退出**：检查本身失败（网络、认证）。告诉用户："无法验证远
  端分支状态，先不动它。"完全跳过删除提议；失败的检查是未知状态，
  不是干净分支。

记录实际路径（`auto`、`direct`、`queue`，或我们尝试前已合并的
`external`），然后继续 §4b（CI 自动部署检测）。

### 4a：合并队列检测与提示

**若 `state == "OPEN"` 且任一请求非空：**auto-merge 已启用或正在用
合并队列。说明观察到的是哪一个；仅 auto 请求证明不了队列。队列会对
拟合并结果重跑 CI。仅当观察到 `mergeQueueEntry` 才记录
`MERGE_PATH=queue`，否则记 `auto`。

设 `WAITED=true`。每 30 秒重复回读，最多 30 分钟；每 2 分钟报告进
度。OPEN 且带活跃 auto 请求**或**队列条目期间持续等待。等待一旦开
始，绝不再派发 START 或 DIRECT：OPEN 且确认**两者皆无**意味着被移
除/取消，**STOP** 并指向 GitHub 的 checks/queue 页面。MERGED 回到
上方的合并 SHA/清理分支。CLOSED、head 变更、回读失败或超时都停止，
不重放也不取消服务端请求。说明超时的活跃请求之后仍可能合并。

### 4b：CI 自动部署检测

PR 合并后，检查合并是否触发了部署工作流：

```bash
gh run list --repo "$REPO" --branch "$BASE_BRANCH" --limit 10 --json databaseId,name,status,conclusion,workflowName,headSha
```

找匹配 `MERGE_SHA` 与批准前识别的部署工作流（读它的 job，不只看名
字）的运行。区分 staging 与生产。找到时：
- 告诉用户："PR 已合并。我看到部署工作流（'{workflow-name}'）自动
  启动了。我会盯着它，完成时告诉你。"

合并后没找到部署工作流：
- 告诉用户："PR 已合并。没看到部署工作流，你的项目可能用别的方式
  部署，或者它是不需要部署步骤的库/CLI。下一步我会找出正确的验
  证。"

`MERGE_PATH=queue` 且存在部署工作流：
- 告诉用户："PR 通过了合并队列，部署工作流正在运行。现在开始监
  控。"

记录合并时间戳、时长与合并路径，供部署报告使用。

---

## Step 5：部署策略检测

用保存的合并前范围与部署事实；不分类已清理的检出。本 Skill 观察既
有部署触发器，不发明新的。

**Step 5-7 的一条优先级规则：**显式验证 URL 或实际触发的部署，优先
于仅文档的捷径。按序评估：

选定下方生产路线后，先完成 Step 5a **再执行该路线**。仅文档的无部
署路线可以立即结束；它不需要 staging 提议。

1. 匹配的部署运行/平台发布：在 Step 6 监控它，仅文档变更也一样
  （可能是文档站）。已配置的工作流或平台触发器但其运行尚未出现时保
  持 pending；在 Step 6 的 deadline 内轮询匹配的 revision，不是别的
  运行。
2. 记录在案的命令触发（Deploy Configuration 把某命令记为部署触发
   器）：不跑它就没有任何部署。告诉用户生产尚未变动、点名命令，请
   他们运行，或仅在他们的显式批准下由你运行。然后为 `MERGE_SHA`
   轮询 Step 6 状态；零退出不是 revision 证明。
3. 显式 `VERIFY_URL`：仅文档变更也跑 Step 7。没有部署 revision 证
   据时，把站点健康与"本变更已上线"分开报告。
4. `DOCS_ONLY=true`、无显式 URL、无已触发/预期的部署：记录
   SKIPPED（docs-only），然后 Step 9 报 MERGED — NO DEPLOY
   NEEDED。部署检测未知不等于"什么都没被触发"；改用下方的提问。
5. 否则在 Step 6-7 用配置的生产 URL/状态检查。既无可用 URL 也无部
   署状态时问一次。Step 6 结束仍缺 canary 所需的生产 URL 时也要
   问：
   - **重新落地：**"PR #NNN 已合并。{已知部署状态}。我需要一个
     URL 检查健康；合并本身证明不了这个 revision 已上线。"
   - **RECOMMENDATION：**web 应用选 A；仅当不需要部署时选 B。
   - A) 提供生产 URL → 保存它，继续 Step 7
   - B) 无需部署（库/CLI）→ Step 9，MERGED — NO DEPLOY NEEDED
   - C) 不做验证直接结束 → Step 9，用基于证据的判定表
   仅在无观察也无预期部署时提供 B；它抹不掉正在运行/正在失败的部
   署。

### 5a：可选的 staging 验证，不是部署门

非文档变更时，仅当 staging/预览 URL 与成功部署记录能标识 `PR_HEAD`
（预览）或 `MERGE_SHA`（合并后 staging）时才提议。仅有 URL 不够。
不可用时记录 staging N/A 并走上方的生产路线。此处不执行任何 staging
触发或晋升。

- **重新落地：**"这个变更有一个部署在 {staging URL}。我可以顺便
  检查它，但生产可能已经上线；这不会 hold 或回滚生产。"
- **RECOMMENDATION：**A 增补 staging 证据而不放弃生产验证。
- A) 先验证 staging，再验证生产
- B) 只验证生产
- C) 只验证 staging；生产验证保持不完整

A/C 对 staging URL 跑 Step 7，`TARGET=staging`，staging 与生产证据
分开保留。staging 健康则设 `STAGING_STATUS=VERIFIED`：A 回到上方的
生产路线；C 进 Step 9，STAGING VERIFIED — PRODUCTION
UNVERIFIED。staging 失败时用 Step 7 的决策路径，绝不自动晋升。B 记
SKIPPED 并走生产路线。

---
