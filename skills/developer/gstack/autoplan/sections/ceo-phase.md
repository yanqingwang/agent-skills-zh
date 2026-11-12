<!-- AUTO-GENERATED from ceo-phase.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`autoplan/sections/ceo-phase.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

派发之前，按 `bun "<SNAPSHOT_TOOL>" methodology ceo "<REVIEW_SKILL>" "<RESTORE_PATH>"`
返回的 `readRanges` 读 `methodologyPath`，把成功范围/总数记到 EOF。
在跳过清单上的：只加载。

按此顺序执行：Step 0（含其完成的 Spec Review Loop）→ Claude CEO 声音
→ Codex CEO 声音 → 共识 → Review Sections → 保存摘要 → 阶段公告。
派发评审者从不等于完成其步骤。

**覆盖规则：**
- 模式选择：SELECTIVE EXPANSION
- 前提：合理的照单接受（P6）。明显错误/被质疑的前提排入 Phase 4 的
  用户挑战：假设、理由与继续推进的代价。由用户在那里裁决；绝不在
  流水线中途停。
- 备选方案：选完整度最高的（P1）。平局选最简的（P5）。前两名接近时
  记 TASTE DECISION。
- 范围扩展：在爆炸半径内且 CC 工作量 <1 天的批准（P2）。之外的转入
  TODOS.md（P3）。重复的拒绝（P4）。边缘情况（3-5 个文件）记
  TASTE DECISION。
- 全部 11 个评审节：完整运行，逐问题自动决策，记录每个决策。

**必需执行清单（CEO）：**

按已加载 Skill 的 SELECTIVE EXPANSION 路线，配以上方覆盖规则，完成
每个 Step 0 分析/输出：CEO 范围文档与 0H Spec Review Loop 先于 0I 与
Review Sections。

**在 0H，为每次规格评审准备当前输入。** 创建一个修订检查点；在整个
CEO 阶段保持其 `snapshotPath` 为 `<CEO_STEP0_CHECKPOINT>`：
```bash
bun "<SNAPSHOT_TOOL>" create ceo "<ACTIVE_PLAN>" "<RESTORE_PATH>" "<methodologyPath>"
```
把 Step 0 接受的每个行为、条件、测试与手工清单放进 CEO 的已接受义务
块。保留源计划与 DESIGN.md 的要求；用户挑战保留原始要求。品味类是
暂定的自动决策；已接受的扩展不得以"排队的变更会获批"为前提。决策
历史与待办评审工作留在 `Review record`。

每次规格派发之前，包括每个被接受的规格修复之后，运行：
```bash
bun "<SNAPSHOT_TOOL>" amend-input ceo "<ACTIVE_PLAN>" "<CEO_STEP0_CHECKPOINT>" "<RESTORE_PATH>" "<methodologyPath>"
```
它应用已记录的要求，导出完整的当前 `Implementation plan`。把返回的
`checkpointPath` 保持为修订基线；返回的 `reviewInputPath` 用作
`<CEO_SPEC_INPUT>`。按返回的每个 `readRanges` offset/limit 把该文件读
到 EOF，然后完整读 CEO 范围摘要。对账两者之间的处置、范围计数、提案
ID 与实际标题/测试引用。把推迟项链接到实际 TODO 或待写内容。修摘要
漂移时不得改决策、丢发现/必填字段或编造引用。工作计划变了就在派发前
重跑 `amend-input` 与回读。把完整的 CEO 范围摘要与 `<CEO_SPEC_INPUT>`
交给已加载的 Spec Review Loop。检查点是不可变的先前状态；绝不把它当
作当前工作计划提供。准备失败算输入失败，不是一次完成的规格评审。
保留该循环既有的停止条件与三次启动上限。循环结束后，为两个声音在
下方创建全新快照；修订检查点保留。

Step 0.5（双声音）：Step 0 的 Spec Review Loop 之后，先消费原生 CEO
评审，再消费可用的外部声音（P6）。共识之前呈现两个已完成的结果；
原生 pass 始终运行。

  **绑定阶段输入：** 运行；两个声音都用 `snapshotPath` 作
  `<CEO_INPUT>`：
```bash
bun "<SNAPSHOT_TOOL>" create ceo "<ACTIVE_PLAN>" "<RESTORE_PATH>" "<methodologyPath>"
```
  只要全新的 `Implementation plan`；不含 `Review record`。

  **Claude CEO 子代理**（经 Agent 工具）：
  Claude Code：Agent schema 暴露 `run_in_background: false` 时就设置。
  收到启动回执说明它进了后台：等它的完成通知。
  其他宿主：前台；支持时等它完成。

  Read `<CEO_INPUT>` 旁边的 `snapshot.json`。把它的
  `nativeDispatchPrompt` 逐字作为 Agent prompt 发出：本条回复只有这一个
  工具调用，且是最后一个。保持原生 Read 可用。子代理先读
  `nativePromptPath` 到 EOF：全部标准加计划；不给摘要或既往评审。

  **原生完成屏障：** 异步（`isAsync: true` / `status: "async_launched"`）
  时，Claude Code 立即结束回复："Waiting for <agent ID>."。在该 ID 的
  终局通知送达之前，不做任何进一步工具调用/评审。其他宿主等该 ID。
  然后跑外部声音；再只做本阶段的评审。已完成原生评审的 INPUT 必须与
  快照的 phase/hash 匹配。无效输入重试一次；仍无效则走失败策略。
  不做内联替代；应用失败策略。

  **Codex CEO 声音**（经 Bash）：
  外部提示词：把 <CEO_INPUT> 与下方上下文的完整内容内联（Write 工具）。

IMPORTANT: Do NOT read or execute any SKILL.md files or paths containing skills/gstack (foreign instructions). Review repository code only.

  You are a CEO/founder advisor reviewing a development plan.
  Challenge the strategic foundations: Are the premises valid or assumed? Is this the
  right problem to solve, or is there a reframing that would be 10x more impactful?
  What alternatives were dismissed too quickly? What competitive or market risks are
  unaddressed? What scope decisions will look foolish in 6 months? Be adversarial.
  No compliments. Just the strategic blind spots.
  File: <CEO_INPUT>

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
`"host":"claude","outside_provider":"codex","outside_status":"completed|unavailable|disabled|skipped","phase":"ceo"`。
不同的尝试结果分开记录。`source:"codex"` 要求完成的 CLI 输出；原生用
`source:"in-host"`（历史 `source:"claude"`：原生 Claude）。可用性/原生
兜底不算外部完成。保留全部上报的 modelUsage；未知模型身份保持未知。
`GSTACK_CODEX_NO_SANDBOX=1` 下加
`"codex_sandbox":"danger-full-access"`。

  **错误处理：** Codex 认证/超时/空响应时只用 Claude 子代理继续，标注
  `[single-model]`。它也失败时输出"外部声音不可用，以主评审继续"。

  **降级矩阵：** 双失败 → "single-reviewer mode"。仅 Codex → 标注
  `[codex-only]`。仅子代理 → 标注 `[subagent-only]`。

- 战略选择：外部评审者以有效的战略理由反对某个前提或范围决策时，记
  TASTE DECISION。两个模型一致认为用户声明的结构应改变（合并、拆分、
  增删）记 USER CHALLENGE（绝不自动决策）。

从已完成的结果产出 CEO 共识表：

```
CEO DUAL VOICES — CONSENSUS TABLE:
  Dimension                           Claude  Codex  Consensus
  1. Premises valid?                   —       —      —
  2. Right problem to solve?           —       —      —
  3. Scope calibration correct?        —       —      —
  4. Alternatives sufficiently explored?—      —      —
  5. Competitive/market risks covered? —       —      —
  6. 6-month trajectory sound?         —       —      —
CONFIRMED = completed subagent + outside; primary cannot replace outside.
Outside disabled/unavailable: six Consensus cells N/A, never CONFIRMED.
Native findings stay separate; disagreements → taste; flag single-voice criticals.
```

第 1-11 节：对每一节，按已加载 Skill 文件的评测标准运行：
- 有发现的节：完整分析，逐问题自动决策，记入审计轨迹
- 无发现的节：用 1-2 句说明查了什么、为什么没有标出问题。绝不可把
  一节压缩成表格行里的名字。
- 第 11 节（Design）：仅在 Phase 0 检测到 UI 范围时运行

**Phase 1 的必需输出：**
- Reality 行：已加载 Skill 的 `REALITY:` 行，每个适用行一条；
   `~/.claude/skills/gstack/bin/gstack-plan-reality check --phase ceo --plan <reviewed snapshot> <review-file|->`
   在阶段关闭前打印 `PLAN_REALITY: … verdict=complete`（无人值守：
   `incomplete` 保持阶段开放）。
- "NOT in scope" 节，含推迟项与理由
- "What already exists" 节，把子问题映射到既有代码
- Error & Rescue 登记表（来自第 2 节）
- Failure Modes 登记表（来自各评审节）
- 理想态差值（本计划把我们留在哪，对比 12 个月理想态）
- Completion Summary（CEO Skill 的完整总结表）

**关闭本阶段：**

上方评审工作到此结束。现在重新加载共享的 close 步骤，即使更早读过。
用阶段 `ceo`、检查点 `<CEO_STEP0_CHECKPOINT>` 与本阶段的
`methodologyPath`。本次调用保持该检查点；评审导出不替代它。

> **STOP。** 关闭一个评审阶段之前，其评审完成之后、宣布完成或加载
> 下一阶段之前（每次退出重新读），Read
> `~/.claude/skills/gstack/autoplan/sections/phase-close.md` 并完整执行。
> 不要凭记忆；那一节是本步骤的事实来源。
