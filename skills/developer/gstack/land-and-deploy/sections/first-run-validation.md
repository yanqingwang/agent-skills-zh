<!-- AUTO-GENERATED from first-run-validation.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`land-and-deploy/sections/first-run-validation.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Step 1.5（dry-run 流程）：首次运行/配置变更验证

你在这里是因为骨架的 Step 1.5 检测打印了 `FIRST_RUN` 或
`CONFIG_CHANGED`（`CONFIRMED` 的运行绝不读本节）。还没有任何东西被
合并或部署。

**CONFIG_CHANGED：**说"你的部署配置变了，我再验证一遍。"
**FIRST_RUN：**说"这是本项目的第一次运行。我会检测部署设置、测试
只读访问，并在请求批准之前给你看合并会触发什么。"
两者都走 1.5a-e。每项检查都用平实语言解释；本 dry run 不部署任何
东西。

### 1.5a：部署基础设施检测

运行部署配置引导，检测平台与设置：

```bash
# Check for persisted deploy config in CLAUDE.md
DEPLOY_CONFIG=$(grep -A 20 "## Deploy Configuration" CLAUDE.md 2>/dev/null || echo "NO_CONFIG")
echo "$DEPLOY_CONFIG"

# If config exists, parse it
if [ "$DEPLOY_CONFIG" != "NO_CONFIG" ]; then
  # Cut at the FIRST ": ", not the last. A greedy 's/.*: *//' ate the scheme of
  # any URL: "Production URL: https://x.com" became "//x.com", because the last
  # ":" belongs to "https:".
  PROD_URL=$(echo "$DEPLOY_CONFIG" | grep -i "production.*url" | head -1 | sed 's/^[^:]*: *//')
  PLATFORM=$(echo "$DEPLOY_CONFIG" | grep -i "platform" | head -1 | sed 's/^[^:]*: *//')
  echo "PERSISTED_PLATFORM:$PLATFORM"
  echo "PERSISTED_URL:$PROD_URL"
fi

# Auto-detect platform from config files
[ -f fly.toml ] && echo "PLATFORM:fly"
[ -f render.yaml ] && echo "PLATFORM:render"
([ -f vercel.json ] || [ -d .vercel ]) && echo "PLATFORM:vercel"
[ -f netlify.toml ] && echo "PLATFORM:netlify"
[ -f Procfile ] && echo "PLATFORM:heroku"
([ -f railway.json ] || [ -f railway.toml ]) && echo "PLATFORM:railway"

# Detect deploy workflows
for f in $(find .github/workflows -maxdepth 1 \( -name '*.yml' -o -name '*.yaml' \) 2>/dev/null); do
  [ -f "$f" ] && grep -qiE "deploy|release|production|cd" "$f" 2>/dev/null && echo "DEPLOY_WORKFLOW:$f"
  [ -f "$f" ] && grep -qiE "staging" "$f" 2>/dev/null && echo "STAGING_WORKFLOW:$f"
done
```

CLAUDE.md 里找到 `PERSISTED_PLATFORM` 与 `PERSISTED_URL` 就直接用，
跳过手工检测。没有持久化配置就用自动检测的平台指导部署验证。什么
都没检测到就经下方决策树的 AskUserQuestion 问用户。

想把部署设置持久化给以后用，建议用户跑 `/setup-deploy`。

解析输出并记录：检测到的平台、生产 URL、部署工作流（若有）及
CLAUDE.md 里的既有配置。

### 1.5b：命令验证

逐个测试检测到的只读命令。先在 1.5c 收集 staging 事实，再展示下方
合并验证表；本 dry run 期间不触发任何部署。

```bash
# Test gh auth (already passed in Step 1, but confirm)
gh auth status 2>&1 | head -3

# Test platform CLI if detected
# Fly.io: fly status --app {app} 2>/dev/null
# Heroku: heroku releases --app {app} -n 1 2>/dev/null
# Vercel: vercel ls 2>/dev/null | head -3

# Test production URL reachability
# curl -sf {production-url} -o /dev/null -w "%{http_code}" 2>/dev/null
```

按检测到的平台跑相关命令。结果汇入这张表：

```
╔══════════════════════════════════════════════════════════╗
║         DEPLOY INFRASTRUCTURE VALIDATION                  ║
╠══════════════════════════════════════════════════════════╣
║  Platform:    {platform} (from {source})                   ║
║  App:         {app name or "N/A"}                          ║
║  Prod URL:    {url or "not configured"}                    ║
║  COMMAND VALIDATION                                        ║
║  ├─ gh auth status:     ✓ PASS                             ║
║  ├─ {platform CLI}:     ✓ PASS / ⚠ NOT INSTALLED / ✗ FAIL ║
║  ├─ curl prod URL:      ✓ PASS (200 OK) / ⚠ UNREACHABLE   ║
║  └─ deploy workflow:    {file or "none detected"}          ║
║  STAGING DETECTION                                         ║
║  ├─ Staging URL:        {url or "not configured"}          ║
║  ├─ Staging workflow:   {file or "not found"}              ║
║  └─ Preview deploys:    {detected or "not detected"}       ║
║  WHAT WILL HAPPEN                                          ║
║  1. Wait for all CI on this head (gstack-ci-gate)         ║
║  2. Readiness checks and explicit merge approval          ║
║  3. Merge PR via {merge method}                            ║
║  4. {Wait for deploy workflow / Wait 60s / Skip}           ║
║  5. {Run canary verification / Skip (no URL)}              ║
║  MERGE METHOD: {squash/merge/rebase} (from repo settings)  ║
║  MERGE QUEUE:  {detected / not detected}                   ║
╚══════════════════════════════════════════════════════════╝
```

**验证失败是 WARNING，不是 BLOCKER**（`gh auth status` 除外，它在
Step 1 就该失败）。`curl` 失败时注明"我够不到那个 URL，可能是网络问
题、需要 VPN，或地址不对。健康验证不可用。"平台 CLI 未安装时注明
"本机没装 {platform} CLI。平台状态不可用。HTTP 检查只能显示可达性，
看不到已部署的版本；我需要配置好的触发器及其部署证据。"

### 1.5c：Staging 检测

按此顺序检查 staging 环境：

1. **CLAUDE.md 持久化配置：**在 Deploy Configuration 节找 staging
   URL：
```bash
grep -i "staging" CLAUDE.md 2>/dev/null | head -3
```

2. **GitHub Actions staging 工作流：**找名字或内容含 "staging" 的工
   作流文件：
```bash
for f in $(find .github/workflows -maxdepth 1 \( -name '*.yml' -o -name '*.yaml' \) 2>/dev/null); do
  [ -f "$f" ] && grep -qiE "staging" "$f" 2>/dev/null && echo "STAGING_WORKFLOW:$f"
done
```

3. **Vercel/Netlify 预览部署：**在 PR 状态检查里找预览 URL：
```bash
gh pr checks "$PR_NUMBER" --repo "$REPO" --json name,state,bucket,link
```
找名字含 "vercel"、"netlify" 或 "preview" 的检查，并检查其 link 里
的预览 URL。check-details 链接不一定是预览本身。

记录的是候选，不是"该版本已部署"的证明。Step 3.5 每次运行刷新部署
事实，并在合并前处理任何真正的 staging 优先请求。

### 1.5d：就绪预览

告诉用户："合并任何 PR 之前，我会跑一系列就绪检查：代码评审、测试、
文档、PR 准确性。给你看看在这个项目里是什么样。"

预览 Step 3.5 将运行的就绪检查（不重跑测试）：

```bash
~/.claude/skills/gstack/bin/gstack-review-read 2>/dev/null
```

展示评审状态摘要：哪些评审跑过、多久没更新。同时检查 CHANGELOG.md
与 VERSION 是否已更新。

用平实语言解释："合并时我会检查：代码最近评审过吗？测试通过吗？
CHANGELOG 更新了吗？PR 描述准确吗？有不对的地方，合并前我会标出
来。"

### 1.5e：Dry-run 确认

告诉用户："我检测到的就是这些。看看上面的表，它和你项目实际的部署
方式一致吗？"

经 AskUserQuestion 呈现完整 dry-run 结果：

- **重新落地：**"这是 [project] 在 [branch] 分支的首次部署 dry-run。
  上面是我对你的部署基础设施的检测结果。还没有合并或部署任何东西，
  这只是我对你的设置的理解。"
- 展示上方 1.5b 的基础设施验证表。
- 列出命令验证的任何警告，附平实语言解释。
- 检测到 staging："我找到了 {url/workflow}。staging URL 不能证明生
  产被 hold 住。合并前我会检查触发器；合并后我可以验证既有 staging
  部署，但生产可能已经上线。"
- 未检测到 staging："没找到 staging。请求批准之前，我会弄清合并会
  触发什么。"
- **RECOMMENDATION：**全部验证通过选 A。有问题要修选 B。想更细致
  配置选 C 跑 /setup-deploy。
- A) 没错，我的项目就是这么部署的。开始吧。（Completeness: 10/10）
- B) 有出入，我来告诉你哪里不对（Completeness: 10/10）
- C) 我想先更仔细地配置一下（跑 /setup-deploy）（Completeness:
  10/10）

**选 A：**说"设置已确认。我会保存它的指纹，跳过未变更的 dry run，
并且每次合并批准前仍会刷新部署事实。"

保存部署配置指纹，以便将来检测变更：
```bash
GSTACK_STATE_ROOT=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT); : "${GSTACK_STATE_ROOT:?gstack-paths failed; reinstall with ./setup or /gstack-upgrade}"
SLUG=$(~/.claude/skills/gstack/bin/gstack-slug --get SLUG 2>/dev/null)
mkdir -p "$GSTACK_STATE_ROOT"/projects/$SLUG
CURRENT_HASH=$(sed -n '/## Deploy Configuration/,/^## /p' CLAUDE.md 2>/dev/null | shasum -a 256 | cut -d' ' -f1)
WORKFLOW_HASH=$(find .github/workflows -maxdepth 1 \( -name '*deploy*' -o -name '*cd*' \) 2>/dev/null | xargs cat 2>/dev/null | shasum -a 256 | cut -d' ' -f1)
echo "${CURRENT_HASH}-${WORKFLOW_HASH}" > "$GSTACK_STATE_ROOT"/projects/$SLUG/land-deploy-confirmed
```
继续 Step 2。

**选 B：****STOP。**"告诉我你的设置哪里不同，我来调整。也可以跑
`/setup-deploy` 走一遍完整配置。"

**选 C：****STOP。**"运行 `/setup-deploy` 会详细过一遍你的部署平
台、生产 URL 和健康检查。它把所有东西存进 CLAUDE.md，下次我就确切
知道该做什么。跑完后再运行 `/land-and-deploy`。"

---
