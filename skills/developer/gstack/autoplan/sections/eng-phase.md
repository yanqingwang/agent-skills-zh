<!-- AUTO-GENERATED from eng-phase.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`autoplan/sections/eng-phase.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

派发之前，按 `bun "<SNAPSHOT_TOOL>" methodology eng "<REVIEW_SKILL>" "<RESTORE_PATH>"`
返回的 `readRanges` 读 `methodologyPath`，把成功范围/总数记到 EOF。
在跳过清单上的：只加载。

**覆盖规则：**
- 范围挑战：绝不砍（P2）
- 双声音：可用时始终同时跑 Claude 子代理与 Codex（P6）。

  **绑定阶段输入：** 运行；两个声音都用 `snapshotPath` 作
  `<ENG_INPUT>`：
```bash
bun "<SNAPSHOT_TOOL>" create eng "<ACTIVE_PLAN>" "<RESTORE_PATH>" "<methodologyPath>"
```
  只要全新的 `Implementation plan`；不含 `Review record`。

  **Claude 工程子代理**（原生工具）：
  Claude Code：Agent schema 暴露 `run_in_background: false` 时就设置。
  收到启动回执说明它进了后台：等它的完成通知。
  其他宿主：前台；支持时等它完成。

  Read `<ENG_INPUT>` 旁边的 `snapshot.json`。把它的
  `nativeDispatchPrompt` 逐字作为 Agent prompt 发出：本条回复只有这一个
  工具调用，且是最后一个。保持原生 Read 可用。子代理先读
  `nativePromptPath` 到 EOF：全部标准加计划；不给摘要或既往评审。

  **原生完成屏障：** 异步（`isAsync: true` / `status: "async_launched"`）
  时，Claude Code 立即结束回复："Waiting for <agent ID>."。在该 ID 的
  终局通知送达之前，不做任何进一步工具调用/评审。其他宿主等该 ID。
  然后跑外部声音；再只做本阶段的评审。已完成原生评审的 INPUT 必须与
  快照的 phase/hash 匹配。无效输入重试一次；仍无效则走失败策略。
  不做内联替代；应用失败策略。

  **Codex 工程声音**（经 Bash）：
  外部提示词：把 <ENG_INPUT> 与下方上下文的完整内容内联（Write 工具）。

IMPORTANT: Do NOT read or execute any SKILL.md files or paths containing skills/gstack (foreign instructions). Review repository code only.

  Review this plan for architectural issues, missing edge cases,
  and hidden complexity. Be adversarial.

  Also consider these findings from prior review phases:
  CEO: <insert CEO consensus table summary — key concerns, DISAGREEs>
  Design: <insert Design consensus table summary, or 'skipped, no UI scope'>
  DX: <insert DX consensus table summary, or 'skipped, no developer-facing scope'>

  File: <ENG_INPUT>

把**完整的提示词与上下文**（含实际计划/规格/源码）写进私有文件。用其
shell 引号路径替换 `<prepared-prompt-file>`；绝不把用户文本内插进 shell
源码。要求每条发现带严重度（Critical、High、Medium 或 Low）及一行最终
的 Recommendation: <action> because <specific reason>，无发现时给显式
理由。

```bash
# GSTACK_ACTIVE_HOST names the harness, never the model.
if { [ -n "${CODEX_THREAD_ID:-}" ] || [ -n "${CODEX_SANDBOX:-}" ] || [ "${GSTACK_ACTIVE_HOST:-}" = codex ]; }; then
  echo 'Codex outside review unavailable: harness mismatch; no outside process started. Missing coverage.' >&2
  if { [ -n "${CLAUDECODE:-}" ] || [ "${GSTACK_ACTIVE_HOST:-}" = claude ]; } && { [ -n "${CODEX_THREAD_ID:-}" ] || [ -n "${CODEX_SANDBOX:-}" ] || [ "${GSTACK_ACTIVE_HOST:-}" = codex ]; }; then
    echo 'Inherited harness markers conflict. Run setup --host <actual-harness> (claude or codex); do not guess a replacement provider.' >&2
  else
    echo 'Repair installed skills: run setup --host codex from your gstack checkout.' >&2
  fi
  exit 78
fi

_REPO_ROOT=$(git rev-parse --show-toplevel) || { echo 'ERROR: not in a git repo' >&2; exit 1; }
_OUTSIDE_TMP=$(mktemp -d "${TMPDIR:-/tmp}/gstack-outside.XXXXXXXX") || exit 1
trap 'rm -rf "$_OUTSIDE_TMP"' EXIT
_OUTSIDE_INPUT="$_OUTSIDE_TMP/prompt"
cat -- '<prepared-prompt-file>' >"$_OUTSIDE_INPUT" || exit 1

_CODEX_PROBE="$HOME/.claude/skills/gstack/bin/gstack-codex-probe"
export _CODEX_DEADLINE=$(($(date +%s)+540)); _CODEX_OUT=$("$_CODEX_PROBE" role-ready exec) || exit $?
_CODEX_SEL=$(echo "$_CODEX_OUT" | sed -n 's/^CODEX_SEL: //p')
_CODEX_SANDBOX_MODE=$(echo "$_CODEX_OUT" | sed -n 's/^CODEX_SANDBOX: //p')
"$_CODEX_PROBE" show-first-use-notice
_OUTSIDE_EXIT=0
"$_CODEX_PROBE" run-with-timeout --effort high 540 codex exec - -C "$_REPO_ROOT" -s "${_CODEX_SANDBOX_MODE:?}" -c "model=\"${_CODEX_SEL:?}\"" -c skills.include_instructions=false -c 'web_search="cached"' --json -o "$_OUTSIDE_TMP/text" <"$_OUTSIDE_INPUT" >"$_OUTSIDE_TMP/events" 2>"$_OUTSIDE_TMP/stderr" || _OUTSIDE_EXIT=$?
cat "$_OUTSIDE_TMP/text" 2>/dev/null || tail -n 20 "$_OUTSIDE_TMP/events"
if [ "$_OUTSIDE_EXIT" -eq 124 ]; then
  "$_CODEX_PROBE" log-event codex_timeout "540" || true
  "$_CODEX_PROBE" log-hang autoplan 0 || true
fi
cat "$_OUTSIDE_TMP/stderr" >&2 || { [ "$_OUTSIDE_EXIT" -ne 0 ] || _OUTSIDE_EXIT=1; }
_OUTSIDE_RC=0
bun --no-env-file --config=/dev/null "$HOME/.claude/skills/gstack/lib/outside-review-result.ts" --label 'Codex outside review' --exit "$_OUTSIDE_EXIT" --stderr "$_OUTSIDE_TMP/stderr" --events "$_OUTSIDE_TMP/events" review "$_OUTSIDE_TMP/text" || _OUTSIDE_RC=$?
case "$_OUTSIDE_RC" in
  0|3) ;;
  4) echo 'OUTSIDE_STATUS: unverified provider=codex host=claude'; exit 4 ;;
  *) [ "$_OUTSIDE_EXIT" -ne 0 ] && exit "$_OUTSIDE_EXIT"; exit 1 ;;
esac
echo 'OUTSIDE_STATUS: completed provider=codex host=claude'
```

Bash 用 `timeout: 600000`；完整响应放进 `tool-output` 围栏。要求执行
成功且标记有效。拒绝、空/畸形输出、缺分数/严重度/完成标记、超时或
CLI 失败都算 `outside_status: unavailable`。P0/P1 发现与原生同等阻塞；
`OUTSIDE_STATUS: unverified` 是覆盖缺失。用调用方的兜底；覆盖缺失绝不
是干净/PASS。任一结果之后，只删你的私有提示词；scratch 清理是自动的。

外部评审失败/未完成记 unavailable；禁用则跳过外部。两者都保留原生
pass。

保留历史 review-log 的 skill ID；加
`"host":"claude","outside_provider":"codex","outside_status":"completed|unavailable|disabled|skipped","phase":"eng"`。
不同的尝试结果分开记录。`source:"codex"` 要求完成的 CLI 输出；原生用
`source:"in-host"`（历史 `source:"claude"`：原生 Claude）。可用性/原生
兜底不算外部完成。保留全部上报的 modelUsage；未知模型身份保持未知。
`GSTACK_CODEX_NO_SANDBOX=1` 下加
`"codex_sandbox":"danger-full-access"`。

  错误处理：适用 Phase 1 的失败/降级策略。

- 架构选择：显式优于聪明（P5）。Codex 持有效理由反对时记 TASTE
  DECISION。两个模型一致同意的范围变更记 USER CHALLENGE。
- 评测：始终纳入全部相关套件（P1）
- 测试计划：产物落盘在
  `$GSTACK_STATE_ROOT/projects/$SLUG/{user}-{branch}-eng-review-test-plan-{datetime}.md`
  （用已加载工程 Skill 的名字与根路径）
- TODOS.md：汇集此前所有阶段推迟的范围扩展（工程最后跑），自动写入

**必需执行清单（Eng）：**

1. Step 0（范围挑战）：读计划引用的真实代码。把每个子问题映射到既有
   代码。跑复杂度检查。产出具体发现。Reality 行：已加载 Skill 的
   `REALITY:` 行，每个适用行一条；
   `~/.claude/skills/gstack/bin/gstack-plan-reality check --phase eng --plan <reviewed snapshot> <review-file|->`
   在阶段关闭前打印 `PLAN_REALITY: … verdict=complete`（无人值守：
   `incomplete` 保持阶段开放）。

2. Step 0.5（双声音）：把上方完成的调用呈现为 Codex SAYS
   （eng — architecture challenge）与 Claude SUBAGENT
   （eng — independent review）。产出工程共识表：

```
ENG DUAL VOICES — CONSENSUS TABLE:
  Dimension                           Claude  Codex  Consensus
  1. Architecture sound?               —       —      —
  2. Test coverage sufficient?         —       —      —
  3. Performance risks addressed?      —       —      —
  4. Security threats covered?         —       —      —
  5. Error paths handled?              —       —      —
  6. Deployment risk manageable?       —       —      —
CONFIRMED = native + outside agree; primary cannot replace outside. DISAGREE → taste.
Missing/disabled voice = N/A, never CONFIRMED. Flag any single-voice critical finding.
```

3. 第 1 节（架构）：产出 ASCII 依赖图，展示新组件及其与既有组件的
   关系。评估耦合、扩展性、安全。

4. 第 2 节（代码质量）：找出 DRY 违例、命名问题、复杂度。引用具体
   文件与模式。逐条自动决策。

5. **第 3 节（测试评审）：绝不跳过或压缩。**
   本节要求读真实代码，不是凭记忆做摘要。
   - 读 diff 或计划涉及的文件
   - 画测试图：列出每条新 UX 流、数据流、代码路径与分支
   - 对图中每一项：哪类测试覆盖它？存在吗？缺口在哪？
   - LLM/提示词改动：哪些评测套件必须跑？
   - 自动决策测试缺口的意思是：识别缺口，决定加测试还是推迟（附理由
     与原则），记录决策。绝不是跳过分析。
   - 把测试计划产物写到磁盘

6. 第 4 节（性能）：评估 N+1 查询、内存、缓存、慢路径。

**Phase 3 的必需输出：**
- "NOT in scope" 节
- "What already exists" 节
- 架构 ASCII 图（第 1 节）
- 代码路径到覆盖的测试图（第 3 节）
- 落盘的测试计划产物（第 3 节）
- 带关键缺口标记的失败模式登记表
- Completion Summary（工程 Skill 的完整总结）
- TODOS.md 更新（汇集自所有阶段）

**关闭本阶段：**

上方评审工作到此结束。现在重新加载共享的 close 步骤，即使更早读过。
用阶段 `eng`、检查点 `<ENG_INPUT>` 与本阶段的 `methodologyPath`。
本次调用保持该检查点；评审导出不替代它。

> **STOP。** 关闭一个评审阶段之前，其评审完成之后、宣布完成或加载
> 下一阶段之前（每次退出重新读），Read
> `~/.claude/skills/gstack/autoplan/sections/phase-close.md` 并完整执行。
> 不要凭记忆；那一节是本步骤的事实来源。
