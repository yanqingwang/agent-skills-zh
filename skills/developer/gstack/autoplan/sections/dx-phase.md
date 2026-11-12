<!-- AUTO-GENERATED from dx-phase.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`autoplan/sections/dx-phase.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

派发之前，按 `bun "<SNAPSHOT_TOOL>" methodology dx "<REVIEW_SKILL>" "<RESTORE_PATH>"`
返回的 `readRanges` 读 `methodologyPath`，把成功范围/总数记到 EOF。
在跳过清单上的：只加载。

**覆盖规则：**
- 模式选择：DX POLISH
- Persona：从 README/文档推断，选最常见的开发者类型（P6）
- 竞争基准：按已加载 Skill 的 "Web research runs in Aside" 节经 Aside
  调研（Aside 未就绪时用 WebSearch）；两者都不可用时引用既有基准（P1）
- 魔法时刻：选能达到竞争档位的最低工作量交付载体（P5）
- Getting started 摩擦：始终朝更少步骤优化（P5）
- 错误信息质量：要求 agent-ready 错误契约（P1，完整）
- API/CLI 命名：一致性胜过聪明（P5）
- DX 品味决策（有主见的默认值 vs 灵活性）：记 TASTE DECISION
- 双声音：可用时始终同时跑 Claude 子代理与 Codex（P6）。

  **绑定阶段输入：** 运行；两个声音都用 `snapshotPath` 作
  `<DX_INPUT>`：
```bash
bun "<SNAPSHOT_TOOL>" create dx "<ACTIVE_PLAN>" "<RESTORE_PATH>" "<methodologyPath>"
```
  只要全新的 `Implementation plan`；不含 `Review record`。

  **Claude DX 子代理**（原生工具）：
  Claude Code：Agent schema 暴露 `run_in_background: false` 时就设置。
  收到启动回执说明它进了后台：等它的完成通知。
  其他宿主：前台；支持时等它完成。

  Read `<DX_INPUT>` 旁边的 `snapshot.json`。把它的
  `nativeDispatchPrompt` 逐字作为 Agent prompt 发出：本条回复只有这一个
  工具调用，且是最后一个。保持原生 Read 可用。子代理先读
  `nativePromptPath` 到 EOF：全部标准加计划；不给摘要或既往评审。

  **原生完成屏障：** 异步（`isAsync: true` / `status: "async_launched"`）
  时，Claude Code 立即结束回复："Waiting for <agent ID>."。在该 ID 的
  终局通知送达之前，不做任何进一步工具调用/评审。其他宿主等该 ID。
  然后跑外部声音；再只做本阶段的评审。已完成原生评审的 INPUT 必须与
  快照的 phase/hash 匹配。无效输入重试一次；仍无效则走失败策略。
  不做内联替代；应用失败策略。

  **Codex DX 声音**（经 Bash）：
  外部提示词：把 <DX_INPUT> 与下方上下文的完整内容内联（Write 工具）。

IMPORTANT: Do NOT read or execute any SKILL.md files or paths containing skills/gstack (foreign instructions). Review repository code only.

  Read the plan file at <DX_INPUT>. Evaluate this plan's developer experience.

  Also consider these findings from prior review phases:
  CEO: <insert CEO consensus summary>
  Design: <insert Design consensus summary, or 'skipped, no UI scope'>

  You are a developer who has never seen this product. Evaluate:
  1. Time to hello world: how many steps from zero to working? Target is under 5 minutes.
  2. Errors, agent-ready (what, fix, recovery, code, context, trace, redaction, channel), capped per Pass 3 (CAP4/CAP6).
  3. API/CLI design: are names guessable? Are defaults sensible? Is it consistent?
  4. Docs: can a dev find what they need in under 2 minutes? Are examples copy-paste-complete?
  5. Upgrade path: can devs upgrade without fear? Migration guides? Deprecation warnings?
  Be adversarial. Think like a developer who is evaluating this against 3 competitors.

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
`"host":"claude","outside_provider":"codex","outside_status":"completed|unavailable|disabled|skipped","phase":"dx"`。
不同的尝试结果分开记录。`source:"codex"` 要求完成的 CLI 输出；原生用
`source:"in-host"`（历史 `source:"claude"`：原生 Claude）。可用性/原生
兜底不算外部完成。保留全部上报的 modelUsage；未知模型身份保持未知。
`GSTACK_CODEX_NO_SANDBOX=1` 下加
`"codex_sandbox":"danger-full-access"`。

  错误处理：适用 Phase 1 的失败/降级策略。

- DX 选择：外部评审者以有效的开发者共情理由反对某个 DX 决策时，记
  TASTE DECISION。两个模型一致同意的范围变更记 USER CHALLENGE。

**必需执行清单（DX）：**

1. Step 0（DX 调查，0A-0G）：自动检测产品类型，然后定 persona、共情
   叙事、竞争基准与 TTHW 目标，追踪开发者旅程。证据就位后才打分；
   初始 DX 分数是修复前 pass 的分数。

2. Step 0.5（双声音）：把上方完成的调用呈现为 Codex SAYS
   （DX — developer experience challenge）与 Claude SUBAGENT
   （DX — independent review）。产出 DX 共识表：

```
DX DUAL VOICES — CONSENSUS TABLE:
  Dimension                           Claude  Codex  Consensus
  1. Getting started < 5 min?          —       —      —
  2. API/CLI naming guessable?         —       —      —
  3. Error messages actionable?        —       —      —
  4. Docs findable & complete?         —       —      —
  5. Upgrade path safe?                —       —      —
  6. Dev environment friction-free?    —       —      —
CONFIRMED = native + outside agree; primary cannot replace outside. DISAGREE → taste.
Missing/disabled voice = N/A, never CONFIRMED. Flag any single-voice critical finding.
```

3. Pass 1-8：逐个按已加载 Skill 运行。打 0-10 分。逐问题自动决策。
   共识表的 DISAGREE 项在相关 pass 呈现，带双方视角。

4. DX 记分卡：产出全部 8 个维度都打完分的完整记分卡。

**Phase 2.5 的必需输出：**
- 开发者旅程图（Step 0F 的 6 阶段表）
- 开发者共情叙事（第一人称视角）
- 全部 8 个维度打分的 DX 记分卡
- DX Implementation Checklist
- 带目标的 TTHW 评估

**关闭本阶段：**

上方评审工作到此结束。现在重新加载共享的 close 步骤，即使更早读过。
用阶段 `dx`、检查点 `<DX_INPUT>` 与本阶段的 `methodologyPath`。
本次调用保持该检查点；评审导出不替代它。

> **STOP。** 关闭一个评审阶段之前，其评审完成之后、宣布完成或加载
> 下一阶段之前（每次退出重新读），Read
> `~/.claude/skills/gstack/autoplan/sections/phase-close.md` 并完整执行。
> 不要凭记忆；那一节是本步骤的事实来源。
