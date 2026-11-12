<!-- AUTO-GENERATED from design-phase.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`autoplan/sections/design-phase.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

派发之前，按 `bun "<SNAPSHOT_TOOL>" methodology design "<REVIEW_SKILL>" "<RESTORE_PATH>"`
返回的 `readRanges` 读 `methodologyPath`，把成功范围/总数记到 EOF。
在跳过清单上的：只加载。

**覆盖规则：**
- 聚焦区域：全部相关维度（P1）
- 结构性问题（缺失状态、层级混乱）：自动修复（P5）
- 审美/品味问题：标记 TASTE DECISION
- 设计系统对齐：DESIGN.md 存在且修复显而易见时自动修复
- 双声音：可用时始终同时跑 Claude 子代理与 Codex（P6）。

  **绑定阶段输入：** 运行；两个声音都用 `snapshotPath` 作
  `<DESIGN_INPUT>`：
```bash
bun "<SNAPSHOT_TOOL>" create design "<ACTIVE_PLAN>" "<RESTORE_PATH>" "<methodologyPath>"
```
  只要全新的 `Implementation plan`；不含 `Review record`。

  **Claude 设计子代理**（原生工具）：
  Claude Code：Agent schema 暴露 `run_in_background: false` 时就设置。
  收到启动回执说明它进了后台：等它的完成通知。
  其他宿主：前台；支持时等它完成。

  Read `<DESIGN_INPUT>` 旁边的 `snapshot.json`。把它的
  `nativeDispatchPrompt` 逐字作为 Agent prompt 发出：本条回复只有这一个
  工具调用，且是最后一个。保持原生 Read 可用。子代理先读
  `nativePromptPath` 到 EOF：全部标准加计划；不给摘要或既往评审。

  **原生完成屏障：** 异步（`isAsync: true` / `status: "async_launched"`）
  时，Claude Code 立即结束回复："Waiting for <agent ID>."。在该 ID 的
  终局通知送达之前，不做任何进一步工具调用/评审。其他宿主等该 ID。
  然后跑外部声音；再只做本阶段的评审。已完成原生评审的 INPUT 必须与
  快照的 phase/hash 匹配。无效输入重试一次；仍无效则走失败策略。
  不做内联替代；应用失败策略。

  **Codex 设计声音**（经 Bash）：
  外部提示词：把 <DESIGN_INPUT> 与下方上下文的完整内容内联（Write 工具）。

IMPORTANT: Do NOT read or execute any SKILL.md files or paths containing skills/gstack (foreign instructions). Review repository code only.

  Read the plan file at <DESIGN_INPUT>. Evaluate this plan's
  UI/UX design decisions.

  Also consider these findings from the CEO review phase:
  <insert CEO dual voice findings summary — key concerns, disagreements>

  Does the information hierarchy serve the user or the developer? Are interaction
  states (loading, empty, error, partial) specified or left to the implementer's
  imagination? Is the responsive strategy intentional or afterthought? Are
  accessibility requirements (keyboard nav, contrast, touch targets) specified or
  aspirational? Does the plan describe specific UI decisions or generic patterns?
  What design decisions will haunt the implementer if left ambiguous?
  Be opinionated. No hedging.

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
`"host":"claude","outside_provider":"codex","outside_status":"completed|unavailable|disabled|skipped","phase":"design"`。
不同的尝试结果分开记录。`source:"codex"` 要求完成的 CLI 输出；原生用
`source:"in-host"`（历史 `source:"claude"`：原生 Claude）。可用性/原生
兜底不算外部完成。保留全部上报的 modelUsage；未知模型身份保持未知。
`GSTACK_CODEX_NO_SANDBOX=1` 下加
`"codex_sandbox":"danger-full-access"`。

  错误处理：适用 Phase 1 的失败/降级策略。

- 设计选择：外部评审者以有效的 UX 理由反对某个设计决策时，记
  TASTE DECISION。两个模型一致同意的范围变更记 USER CHALLENGE。

**必需执行清单（Design）：**

1. Step 0（设计范围）：给完整度打 0-10。检查 DESIGN.md。梳理既有模式。

2. Step 0.5（双声音）：把上方完成的调用呈现为 Codex SAYS
   （design — UX challenge）与 Claude SUBAGENT（design — independent
   review）。按 plan-design-review 产出设计试金石记分卡。CEO 发现只进
   外部声音；原生声音保持独立。外部缺失/禁用记 N/A，不是 CONFIRMED；
   主评审替代不了它。

3. Pass 1-7：逐个按已加载 Skill 运行。打 0-10 分。逐问题自动决策。
   记分卡的 DISAGREE 项在相关 pass 呈现，带双方视角。

**关闭本阶段：**

上方评审工作到此结束。现在重新加载共享的 close 步骤，即使更早读过。
用阶段 `design`、检查点 `<DESIGN_INPUT>` 与本阶段的 `methodologyPath`。
本次调用保持该检查点；评审导出不替代它。

> **STOP。** 关闭一个评审阶段之前，其评审完成之后、宣布完成或加载
> 下一阶段之前（每次退出重新读），Read
> `~/.claude/skills/gstack/autoplan/sections/phase-close.md` 并完整执行。
> 不要凭记忆；那一节是本步骤的事实来源。
