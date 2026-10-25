---
name: auto-paper-improvement-loop
description: "通过 GPT-6-Astra xhigh 审查 → 实施修复 → 重新编译，自主改进一篇已生成的论文，共 2 轮。当用户说 \"改论文\"、\"improve paper\"、\"论文润色循环\"、\"auto improve\"，或希望迭代润色一篇已生成的论文时使用。"
argument-hint: "[paper-directory] [— style-ref: <source>] [— edit-whitelist <path>]"
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, Skill, mcp__codex__codex, mcp__codex__codex-reply, mcp__antigravity__antigravity, mcp__antigravity__antigravity-reply, mcp__grok__grok, mcp__grok__grok-reply, mcp__claude-review__review, mcp__claude-review__review_reply, mcp__claude-review__review_start, mcp__claude-review__review_reply_start, mcp__claude-review__review_status
---

> **中文汉化版** · 上游：[wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) · 原文件：`skills/auto-paper-improvement-loop/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 论文自动改进循环：审查 → 修复 → 重新编译

> **在每个审查者席位（reviewer slot）之前**，遵循 [Selectable Reviewers](../shared-references/reviewer-backends.md)：
> 解析调用方式 → `.aris/reviewer.json` → Claude Code 默认（Codex MCP），
> 经由规范助手解析器 `reviewer_route.py`，保留本席位的层级（tier）、
> 全新上下文、源码/图片输入与确定性门控。
> 下文的 Codex 示例/钉死（pin）仅适用于 `backend=codex`；其他路由
> 使用各自的首调（first-call）/回复（reply）契约。保存所用路由与实际返回的身份；
> 不可用的选择记为 `REVIEW_UNAVAILABLE`。基于实际的家族/完成情况/范围判定验收。
> 将调用传入的 reviewer/model/effort 覆盖参数转发给携带审查者的子代理。
> 生成类 worker 保持不变。


> 🔒 **不要把本 Skill 包进 `/loop`、`/schedule` 或 `CronCreate`。** 它
> 已经在内部自带循环（审查 → 修复 → 重新编译），拥有自己的
> 轮次结构，并且每轮刻意带有"全新审查者"偏置护栏
> （不使用 `codex-reply`）。在墙钟定时器上反复要求它
> "改进论文"不会产生任何新信号，质量变化取决于
> *审查*的变化，而不是时钟的走动，而且一次定时重跑
> 如果还接受自己的输出来决定何时停止，就越界成了
> 自我开脱（`acceptance-gate.md`）。应当调度的是*它之前的
> 外部等待*，而不是改进循环本身。参见
> [`shared-references/external-cadence.md`](../shared-references/external-cadence.md)。

自主改进以下位置的论文：**$ARGUMENTS**

## 背景

本 Skill 设计为在 Workflow 3（`/paper-plan` → `/paper-figure` → `/paper-write` → `/paper-compile`）**之后**运行。它接收一篇已编译的论文，通过外部 LLM 审查对其进行迭代式改进。

与 `/auto-review-loop`（它迭代的是**研究**本身：跑实验、收集数据、重写叙事）不同，本 Skill 迭代的是**论文写作质量**，修复理论上的不一致、软化过度声称（overclaim）、补充缺失内容、改进呈现效果。

## 常量

- **MAX_ROUNDS = 2** — 两轮"审查→修复→重新编译"。经验上，第 1 轮捕捉结构性问题（4→6/10），第 2 轮捕捉剩余的呈现问题（6→7/10）。对纯写作改进而言，超过 2 轮收益递减。
- **REVIEWER_MODEL = `gpt-6-astra`** — 通过 Codex MCP 进行论文审查所用的模型。
- **REVIEWER_BIAS_GUARD = true** — 为 `true` 时，每轮审查都使用没有先前审查上下文的全新 `mcp__codex__codex` 线程。绝不在审查轮次中使用 `mcp__codex__codex-reply`。仅为有意调试旧行为时才设为 `false`。**经验证据：**对同一篇论文使用 `codex-reply` 加"自上轮以来我们做了 X"式提示词，多轮之后分数从真实的 3/10 被抬升到虚假的 8/10；切换到全新线程后恢复了真实的 3/10 评估。
- **REVIEW_LOG = `PAPER_IMPROVEMENT_LOG.md`** — 所有轮次的累积日志，存放在论文目录中。
- **HUMAN_CHECKPOINT = false** — 为 `true` 时，在每轮审查后暂停，向用户展示分数与弱点。用户可以批准修复、给出自定义修改指令、跳过特定修复或提前停止。为 `false`（默认）时，完全自主运行。
- **EDIT_WHITELIST = `null`** — 可选路径，指向一个 YAML/JSON 白名单文件，约束修复实施步骤可以触碰哪些路径与操作。为 `null`（默认）时，所有编辑不受约束地进行。通过 `— edit-whitelist <path>`（也接受 `— edit_whitelist <path>`）设置后，循环在启动时加载该文件，并在每次编辑前查询它；被拒绝的编辑会记录到 `PAPER_IMPROVEMENT_LOG.md`，而不是被静默丢弃。见下文"可选：编辑白名单"。

> 💡 覆盖方式：`/auto-paper-improvement-loop "paper/" — human checkpoint: true`

## 可选：风格参考（`— style-ref: <source>`，需显式开启）

让用户在改进过程中把**结构性修复**（章节重排提示、段落长度微调、图密度调整）导向一篇参考论文。**默认关闭：当用户未传入 `— style-ref` 时，行为与之前完全一致，不做任何额外操作。**

只有当 `— style-ref: <source>` 出现在 `$ARGUMENTS` 中时，才在循环开始前首先运行该助手：

```bash
# Resolve $STYLE_HELPER via the canonical strict-safe chain (see
# shared-references/integration-contract.md §2). Policy A — gate:
# unresolved helper means --style-ref cannot be satisfied, so abort.
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" || exit 1
if [ -z "${ARIS_REPO:-}" ] && [ -f .aris/installed-skills.txt ]; then
    ARIS_REPO=$(awk -F'\t' '$1=="repo_root"{print $2; exit}' .aris/installed-skills.txt 2>/dev/null) || true
fi
if [ -z "${ARIS_REPO:-}" ] && [ -f "$HOME/.aris/repo" ]; then
    ARIS_REPO=$(cat "$HOME/.aris/repo" 2>/dev/null) || true
fi
STYLE_HELPER=".aris/tools/extract_paper_style.py"
[ -f "$STYLE_HELPER" ] || STYLE_HELPER="tools/extract_paper_style.py"
[ -f "$STYLE_HELPER" ] || { [ -n "${ARIS_REPO:-}" ] && STYLE_HELPER="$ARIS_REPO/tools/extract_paper_style.py"; }
[ -f "$STYLE_HELPER" ] || {
  echo "ERROR: extract_paper_style.py not resolved at .aris/tools/, tools/, \$ARIS_REPO/tools/, or via ~/.aris/repo." >&2
  echo "       Fix: rerun bash tools/install_aris.sh or smart_update.sh (refreshes ~/.aris/repo), export ARIS_REPO, or copy the helper to tools/." >&2
  echo "       --style-ref cannot be satisfied; aborting." >&2
  exit 1
}
STYLE_STATUS=0
CACHE=$(python3 "$STYLE_HELPER" --source "<source>") || STYLE_STATUS=$?
case "$STYLE_STATUS" in
  0) ;;                                       # use $CACHE/style_profile.md as structural guidance for the FIX phase only
  2) echo "warning: style-ref skipped (missing optional dep)" >&2 ;;
  3) echo "error: --style-ref source failed; aborting loop" >&2 ; exit 1 ;;
  *) echo "error: helper failed unexpectedly; aborting loop" >&2 ; exit 1 ;;
esac
```

接受的来源：本地 TeX 目录/文件、本地 PDF、arXiv id、http(s) URL。Overleaf URL/ID 会被拒绝，请先通过 `/overleaf-sync setup <id>` 克隆，再传入本地克隆路径。

**严格规则**（完整契约见 `tools/extract_paper_style.py` 的 docstring）：

- `style_profile.md` 仅在**修复实施**阶段使用，用于在落实审查反馈时微调结构性选择。审查反馈始终优先；风格参考只在*如何*落实某个修复上作为平局裁决者，而不是*是否*落实它。
- **在实施修复时，绝不复制**缓存可达范围内任何内容的行文、声称、示例或术语。
- **绝不将 `— style-ref`（或缓存内容）传给 GPT-6-Astra 审查者子代理。**下文的审查者独立性协议要求审查者只看到论文工件与用户的提示词，泄露风格参考会让作者侧上下文污染审查。**这是本 Skill 中最关键的不变量。**

## 可选：编辑白名单（`— edit-whitelist <path>`，需显式开启）

让调用方硬性约束**修复实施**步骤（Step 3 / Step 6）允许触碰哪些文件与操作。**默认关闭，当用户未传入 `— edit-whitelist`（或别名 `— edit_whitelist`）时，循环不加限制地落实所有审查驱动的编辑，与之前完全一致。**

这是上游流水线（如 `/resubmit-pipeline` Phase 2）用来强制执行"仅文本"重投稿微编辑的参数：不改动 `.bib`、不改动 `.sty` / `.bst`、不编辑既往投稿目录、不新增 `\cite{...}`、不新增定理环境、不新增数值声称。

### 白名单文件结构（Schema）

白名单文件为 YAML 或 JSON。四个部分均为可选：

```yaml
allowed_paths:
  - sec/*.tex
  - main.tex
  - figures/*.tex
forbidden_paths:
  - "**/*.bib"
  - "**/*.sty"
  - "**/*.bst"
  - "../OldSubmission/**"
forbidden_operations:
  - new_cite              # blocks \cite{...}, \citep{...}, \citet{...}, \citeauthor{...} additions
  - new_bibitem           # blocks \bibitem{...} additions
  - new_theorem_env       # blocks \begin{theorem|lemma|proposition|corollary} additions
  - numerical_claim       # blocks adding new numbers / percentages / metrics
forbidden_deletions:      # operations that block REMOVALS, not additions
  - delete_existing_cite  # blocks removal of \cite{...} from the body (use citation-audit --soft-only instead)
  - delete_theorem_env    # blocks removal of an existing \begin{theorem|...} block
requires_user_approval_for:  # operations that don't auto-reject but pause for explicit user OK
  - rewrite_abstract      # paraphrasing the entire abstract triggers a checkpoint
  - rewrite_intro_first_para
  - delete_section
max_edits_per_round: 30   # hard cap on number of accepted edits per round (rejections are not counted; if cap is hit, remaining proposed edits are deferred to the next round with a warning)
rationale: "Resubmit mode: text-only microedits, paper structure frozen by user constraint."
```

### 解析规则

- **`allowed_paths` 为空且 `forbidden_paths` 为空** → 白名单不生效（建议性质：文件仍会被加载且 `rationale` 会回显到日志，但不应用任何路径过滤）。
- **`allowed_paths` 为空、`forbidden_paths` 非空** → 所有未被 `forbidden_paths` 匹配的路径均可修改。
- **`allowed_paths` 非空、`forbidden_paths` 为空** → 只有匹配 `allowed_paths` 的路径可修改。
- **两者均非空** → 当且仅当目标匹配 `allowed_paths` 且不匹配 `forbidden_paths` 时，编辑才被允许。重叠时 `forbidden_paths` 恒胜。
- **`forbidden_operations` 缺失或为空** → 无操作级守卫；只应用路径级过滤。

### Glob 语义

使用 bash `extglob` / Python `fnmatch.fnmatch` 语义。`**` 匹配任意深度（零个或多个目录段）。模式是相对于**论文目录**的路径进行匹配的（例如论文目录为 `paper/` 时，`paper/sec/intro.tex` 匹配 `sec/*.tex`）。

### 禁止操作检测器

对每个候选编辑的 diff（即新增的行，删除行不受限），循环运行以下正则检查，任一禁止操作命中即拒绝：

| 操作 | 检测器（仅针对新增行） |
|-----------|------------------------------|
| `new_cite` | `\\cite[a-zA-Z]*\{[^}]+\}`（捕获 `\cite`、`\citep`、`\citet`、`\citeauthor`、`\citeyear`、`\citealp` 等） |
| `new_bibitem` | `\\bibitem\{[^}]+\}` |
| `new_theorem_env` | `\\begin\{(theorem|lemma|proposition|corollary)\*?\}` |
| `numerical_claim` | 新出现的、匹配 `\b\d+(\.\d+)?%?\b` 且未在被删除/被替换的行中出现过的 token（即真正新增的数字，而非对既有数字的修改） |

### 循环启动时的行为（第 1 轮修复实施之前）

1. 若 `$ARGUMENTS` 中存在 `— edit-whitelist <path>`，设置 `EDIT_WHITELIST = <path>`。
2. 加载该文件（`yaml.safe_load`；失败则回退到 `json.loads`）。加载失败时，以明确的错误中止循环，绝不要静默地不受约束地继续。
3. 将 `rationale`（若存在）回显到 `PAPER_IMPROVEMENT_LOG.md` 中一个新的 "Edit Whitelist" 前言小节，使审计留痕记录编辑为何受限。

### 修复实施期间的行为（Step 3 与 Step 6）

在应用每个拟定编辑之前：

1. 将目标文件路径解析为相对论文目录的路径。
2. 路径检查：若 `allowed_paths` 非空，目标必须至少匹配一个模式。然后若 `forbidden_paths` 非空，目标不得匹配任何模式。任一失败 → 以 `path` 违规拒绝。
3. 操作检查：为该拟定编辑构建统一 diff（或仅新增行的集合）。对 `forbidden_operations` 中的每一项，在新增行上运行其检测器。任一检测器命中 → 以 `operation` 违规拒绝。
4. 所有检查通过，则正常应用该编辑。
5. 若被拒绝，向 `PAPER_IMPROVEMENT_LOG.md` 追加一条记录，置于 `## Rejected by edit_whitelist (Round N)` 标题之下，格式如下：
   ```
   - file: <relative path>
     reason: path | operation
     pattern: <the offending forbidden_path glob, OR the offending forbidden_operation name + the matched substring>
     reviewer_concern: <the original Round-N weakness that motivated this edit>
   ```
6. 继续本轮剩余的编辑。绝不要因单次拒绝而中止整轮。

### 轮末汇总上报

在每轮结束时（重新编译之后、进入下一轮之前），如果该轮修复步骤中有任何编辑被拒绝：

- 向该轮的检查点输出打印一行摘要：`Edit whitelist rejected N edits this round (M path, K operation). See PAPER_IMPROVEMENT_LOG.md "Rejected by edit_whitelist (Round N)".`
- 若 `HUMAN_CHECKPOINT = true`，在展示给用户、等待其批准下一轮修复的检查点中包含该拒绝清单。

### 调用示例

```bash
# Resubmit-pipeline Phase 2 caller (text-only mode):
/auto-paper-improvement-loop "paper/" — edit-whitelist .resubmit/edit_whitelist.yaml

# Aliased form is accepted:
/auto-paper-improvement-loop "paper/" — edit_whitelist .resubmit/edit_whitelist.yaml

# Combined with other flags:
/auto-paper-improvement-loop "paper/" — human checkpoint: true — edit-whitelist constraints.yaml
```

### 设计理由

没有白名单时，循环中审查驱动的修复步骤可以随意新增引用、引入新的定理环境或改动数值声称，这些对首次投稿的润色都合理，但在结构被外部约束冻结的重投稿 / camera-ready / 仅 rebuttal 模式中是**被禁止的**。把这些约束通过一个一等参数来传递（而不是指望 LLM"记住"不要做这些事），约束才可执行、可经由 `PAPER_IMPROVEMENT_LOG.md` 审计，并在每轮检查点对用户可见。

## 输入

1. **已编译的论文** — `paper/main.pdf` + LaTeX 源文件
2. **全部章节 `.tex` 文件** — 拼接后用于审查提示词

## 状态持久化（紧凑恢复）

如果上下文窗口在循环中途被填满，Claude Code 会自动压缩（compact）。为了能够恢复，本 Skill 在每轮之后写入 `PAPER_IMPROVEMENT_STATE.json`：

```json
{
  "current_round": 1,
  "threadId": "019ce736-...",
  "last_score": 6,
  "status": "in_progress",
  "timestamp": "2026-03-13T21:00:00"
}
```

**启动时**：若 `PAPER_IMPROVEMENT_STATE.json` 存在、`"status": "in_progress"` 且 `timestamp` 在 24 小时之内，则读取它与 `PAPER_IMPROVEMENT_LOG.md` 以恢复上下文，然后从下一轮继续。否则（文件不存在、`"status": "completed"`、或已超过 24 小时），从头开始。

**每轮之后**：覆写状态文件。**完成时**：设置 `"status": "completed"`。

## 审查者独立性协议

审查者在每一轮都必须对上下文一无所知（context-naive）。以往轮次的摘要、修复清单、执行者解释都不是证据；它们是确认偏误的来源。如果审查者被告知了改了什么，即使稿件本身没有实质改进，分数也倾向于上漂。

规则：
- 每轮都以 `mcp__codex__codex` 开始，而不是 `mcp__codex__codex-reply`。
- 绝不把先前的 threadId 传入下一次审查提示词。
- 绝不在审查提示词中包含"自上轮以来"、"我们修复了"、"落实之后"或任何修复摘要。
- 唯一可接受的改进证据是当前的 `.tex` 源码与编译出的 PDF。
- 如果某个修复无法在文件中被观察到，就不应告知审查者它发生过。
- 如需恢复元数据，仅为崩溃恢复保存返回的 threadId；不要用它来延续审查上下文。

只有当你明确想要旧式的、携带上下文的行为来调试时，才设置 `REVIEWER_BIAS_GUARD = false`。

## 工作流

### Step 0: 保留原始版本

```bash
cp paper/main.pdf paper/main_round0_original.pdf
```

### Step 1: 收集论文文本

将所有章节文件拼接成一个文本块，用于审查提示词：

```bash
# Collect all sections in order
for f in paper/sections/*.tex; do
    echo "% === $(basename $f) ==="
    cat "$f"
done > /tmp/paper_full_text.txt
```

### Step 2: 第 1 轮审查

将完整论文文本与编译后的 PDF 一并发送给 GPT-6-Astra xhigh：

> 先解析此审查者席位；以下为 `backend=codex` 的示例。

```
mcp__codex__codex:
  model: gpt-6-astra
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    You are reviewing a [VENUE] paper. Please provide a detailed, structured review.

    Judge claim calibration in BOTH directions. Recommend narrowing only when the
    current scope or modality exceeds the evidence; do not ask for extra hedges
    around a supported result. Flag stacked hedges, self-defence ("we do not
    claim"), instruction confessions ("we do not address X"), and generic caveats
    outside Limitations as writing defects to remove. Tone fixes must never alter
    facts, negation, modality, scope, comparison direction, or numbers.
    Also flag narrative defects: a progress-report structure ("we first tried
    A, then B"), a story built on a metric the method loses, results narrated
    as defeats ("underperforms", "fails to surpass") instead of explained as a
    goal difference or tradeoff, experiments with no argumentative duty, an
    abstract or introduction that opens on background or implementation
    instead of problem -> gap -> idea -> strongest result, and a conclusion
    that ends on new self-negation. The fix is reframing and cutting where
    the evidence supports the reframing; a genuine weakness is stated
    neutrally and kept in Limitations. Never delete unfavorable numbers from
    tables, and never dress a weakness as a tradeoff.

    ## Paper Files:
    - LaTeX source: [list all section .tex files]
    - Compiled PDF: paper/main.pdf
    - Figures: [list figure files]

    Read BOTH the LaTeX source (for content/logic) AND the compiled PDF (for visual presentation).

    ## Review Instructions
    Please act as a senior ML reviewer ([VENUE] level). Provide:
    1. **Overall Score** (1-10, where 6 = weak accept, 7 = accept)
    2. **Summary** (2-3 sentences)
    3. **Strengths** (bullet list, ranked)
    4. **Weaknesses** (bullet list, ranked: CRITICAL > MAJOR > MINOR)
    5. **For each CRITICAL/MAJOR weakness**: A specific, actionable fix
    6. **Missing References** (if any)
    7. **Visual Review** (from the PDF):
       - Figure quality: readable? labels legible? colors distinguishable in grayscale?
       - Figure-caption alignment: does each caption match its figure?
       - Layout: orphaned headers, awkward page breaks, figures far from references?
       - Table formatting: aligned columns, consistent decimals, bold for best results?
       - Visual consistency: same color scheme across all figures?
    8. **Verdict**: Ready for submission? Yes / Almost / No

    Focus on: theoretical rigor, claims vs evidence alignment, writing clarity,
    self-containedness, notation consistency, AND visual presentation quality.
```

保存 threadId 供第 2 轮使用。

### Step 2b: 人工检查点（如启用）

**若 `HUMAN_CHECKPOINT = false` 则跳过。**

展示审查结果并等待用户输入：

```
📋 Round 1 review complete.

Score: X/10 — [verdict]
Key weaknesses (by severity):
1. [CRITICAL] ...
2. [MAJOR] ...
3. [MINOR] ...

Reply "go" to implement all fixes, give custom instructions, "skip 2" to skip specific fixes, or "stop" to end.
```

按与 `/auto-review-loop` 相同的方式解析用户回应：批准 / 自定义指令 / 跳过 / 停止。

### Step 3: 实施第 1 轮修复

解析审查结果并按严重程度实施修复：

**优先级顺序：**
1. CRITICAL 修复（假设不匹配、内部矛盾）
2. MAJOR 修复（过度声称、缺失内容、记号问题）
3. MINOR 修复（时间允许时）

**编辑白名单门控（若设置）：**若设置了 `EDIT_WHITELIST`，在应用每个拟定编辑之前，按"可选：编辑白名单"一节检查目标路径与 `allowed_paths` / `forbidden_paths`，并对照 `forbidden_operations` 检查新增行 diff。拒绝会记录到 `PAPER_IMPROVEMENT_LOG.md` 的 `## Rejected by edit_whitelist (Round 1)` 之下，含文件、原因（`path` 或 `operation`）、违规模式与原始审查关切。循环继续处理剩余编辑，一次拒绝绝不中止整轮。在轮末汇总上报拒绝摘要。

**在应用任何修复之前：**将声称校准到证据，并直接陈述它们；
泛泛的限定语只属于 Limitations；写作指令绝不是稿件内容；
语气编辑绝不改变论文已知的事实。

**常见修复模式：**

| 问题 | 修复模式 |
|-------|-------------|
| 假设-模型不匹配 | 重写假设使其匹配模型，添加连接两者的形式化命题 |
| 真实的过度声称 | 将声称本身收窄到被支持的范围/模态，绝不为了修复范围、比较或聚合问题而换一个听起来更软的同义词 |
| 被支持的声称裹着不必要的谨慎 | 删除冗余的模糊限定；保留使声称成立的范围限定词 |
| 散落各处的泛泛限定语 | 归并进 Limitations 并删除重复项 |
| 故事建立在一个必输的指标上，或把结果讲成失败 | 围绕论文取胜的那场较量重新框定；当证据支持时，把差距解释为目标差异或权衡，否则中性陈述并收窄声称；保留表中的每一个数字 |
| 没有论证职责的实验 | 删掉、缩短、移入附录，或重新设计使其能证明方法、机制、目标场景价值或排除某个替代方案 |
| 缺失指标 | 添加定量表格，参数量诚实，并附限定说明 |
| 定理不自包含 | 添加"Interpretation"段落，列出全部依赖 |
| 记号混乱 | 全局重命名冲突符号，添加记号说明段 |
| 缺失参考文献 | 加入 `references.bib`，在合适位置引用 |
| 理论-实践差距 | 明确将理论框定为理想化设定；添加合成数据验证小节 |
| 证明缺口（理论论文） | 若 PROOF_AUDIT.md 尚不存在则运行 `/proof-checker`；修复 FATAL/CRITICAL 问题 |
| 行文冗赘 / 被动语态 | 应用 sciwrite 五遍审计：冗赘提取 → 主动语态 → 句子架构 → 关键词一致性 → 数字完整性。见 `paper-write` Step 5 |
| 数字不一致（论文 vs 结果） | 若 PAPER_CLAIM_AUDIT.md 不存在则运行 `/paper-claim-audit`；修复所有 `number_mismatch` 或 `aggregation_mismatch` 声称 |
| 关键词不一致 | "香蕉规则（Banana Rule）"：若 Methods 写 "obese group"，Results 就不能写 "heavier group"。提取关键术语，核查所有章节的一致性 |

### Step 4: 重新编译第 1 轮

```bash
cd paper && latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf main_round1.pdf
```

验证：0 个未定义引用（undefined references），0 个未定义引文（undefined citations）。

### Step 4.5: 定理复述回归测试

每次重新编译之后，重跑一次定理陈述一致性检查，以防修复轮次重新引入附录漂移。**在 Step 4 之后运行一次，并在 Step 7 之后、最终格式检查之前再运行一次。**

**范围**
- 只比较 theorem/lemma/proposition/corollary 的陈述，不比较证明主体。
- 按 `main.tex` 的 input 顺序对文件分类：`\appendix` 之前的文件为主文；`\appendix` 之后的文件为附录。

**归一化比较逻辑**
- 去除注释、`\label{...}`、`\ref{...}`、`\eqref{...}`、`\cite...{...}` 以及纯空白差异。
- 将仅格式化类宏（如 `\emph{}`、`\textbf{}`、`\textit{}`、`\mathrm{}`、`\mathbf{}`、`\mathcal{}`、`\operatorname{}`）折叠为其内容。
- 保留量词、分情况（case split）、假设以及被定义对象的字面名称。
- 尽可能按定理 label 比较；否则按定理类型与顺序比较。
- 假设、分情况、量词顺序或术语（`stationary` vs `terminal`）的任何变化都标记为回归漂移。

```bash
python3 - <<'PY'
import re
def normalize(s):
    s = re.sub(r'%.*', '', s)
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    s = re.sub(r'\\(?:ref|eqref|cref|Cref|cite[a-zA-Z]*)\{[^}]*\}', '', s)
    s = re.sub(r'\\(?:emph|textbf|textit|mathrm|mathbf|mathsf|mathcal|operatorname)\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\begin\{[^}]+\}|\\end\{[^}]+\}', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()
# Compare normalized theorem blocks from the current main-body files
# against their appendix restatements. Any mismatch blocks completion.
PY
```

**经验动机：**在一次真实的投稿运行中，一个关键定理在正文中是多分情况的，在附录中却是单分情况陈述；一个关键变量在正文与附录中命名不一致。由于没有自动化检查捕捉回归，这些漂移在多轮修复中反复出现。

**可选的更深入检查：`/proof-checker --restatement-check`**

上述内联 Python 检查是默认项，对例行的正文-附录一致性已足够。如需更广覆盖，可以额外调用 `/proof-checker --restatement-check`（PR #189 新增），它把比较扩展到：

- 摘要表、摘要、"Key Contributions" 清单与讨论章节中的复述（不只是正文 vs 附录）。
- 由审查者归类的六种具名漂移特征：`conditional_loss`、`scope_change`、`quantifier_loss`、`regime_envelope_change`、`constant_change`、`variable_rename`。
- 以 `details.restatement_drift[]` 形式输出结构化发现到 `PROOF_AUDIT.json`，便于下游工具或审计留痕使用。

此项仅为建议，内联的 Step 4.5 检查仍是默认项，且在每轮循环中继续运行。在以下情况考虑调用 `/proof-checker --restatement-check`：(a) 你怀疑存在主文↔附录轴之外的跨位置漂移（例如摘要相对定理陈述过度声称），或 (b) 你想要审查者分级的漂移特征而非原始字符串不匹配。两者同时运行是支持的且相互独立：内联检查对字符串漂移快速失败，proof-checker 遍则暴露语义类漂移。

### Step 5: 第 2 轮审查

若 `REVIEWER_BIAS_GUARD = true`（默认），第 2 轮使用**全新的** `mcp__codex__codex` 线程。不要复用第 1 轮的 threadId 进行提示。返回的 threadId 仅保存用于恢复记录。

> 先解析此审查者席位；以下为 `backend=codex` 的示例。

```
mcp__codex__codex:
  model: gpt-6-astra
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    You are reviewing a [VENUE] paper. This is a fresh, zero-context review.

    Judge claim calibration in BOTH directions. Recommend narrowing only when the
    current scope or modality exceeds the evidence; do not ask for extra hedges
    around a supported result. Flag stacked hedges, self-defence ("we do not
    claim"), instruction confessions ("we do not address X"), and generic caveats
    outside Limitations as writing defects to remove. Tone fixes must never alter
    facts, negation, modality, scope, comparison direction, or numbers.
    Also flag narrative defects: a progress-report structure ("we first tried
    A, then B"), a story built on a metric the method loses, results narrated
    as defeats ("underperforms", "fails to surpass") instead of explained as a
    goal difference or tradeoff, experiments with no argumentative duty, an
    abstract or introduction that opens on background or implementation
    instead of problem -> gap -> idea -> strongest result, and a conclusion
    that ends on new self-negation. The fix is reframing and cutting where
    the evidence supports the reframing; a genuine weakness is stated
    neutrally and kept in Limitations. Never delete unfavorable numbers from
    tables, and never dress a weakness as a tradeoff.
    Ignore any prior review rounds, prior fix lists, or executor explanations.
    Judge the paper only from the current LaTeX source and compiled PDF.

    ## Paper Files:
    - LaTeX source: [list all section .tex files]
    - Compiled PDF: paper/main.pdf
    - Figures: [list figure files]

    Read BOTH the LaTeX source (for content/logic) AND the compiled PDF (for visual presentation).

    ## Review Instructions
    Please act as a senior ML reviewer ([VENUE] level). Provide:
    1. **Overall Score** (1-10, where 6 = weak accept, 7 = accept)
    2. **Summary** (2-3 sentences)
    3. **Strengths** (bullet list, ranked)
    4. **Weaknesses** (bullet list, ranked: CRITICAL > MAJOR > MINOR)
    5. **For each CRITICAL/MAJOR weakness**: A specific, actionable fix
    6. **Missing References** (if any)
    7. **Visual Review** (from the PDF):
       - Figure quality: readable? labels legible? colors distinguishable in grayscale?
       - Figure-caption alignment: does each caption match its figure?
       - Layout: orphaned headers, awkward page breaks, figures far from references?
       - Table formatting: aligned columns, consistent decimals, bold for best results?
       - Visual consistency: same color scheme across all figures?
    8. **Verdict**: Ready for submission? Yes / Almost / No

    Focus on: theoretical rigor, claims vs evidence alignment, writing clarity,
    self-containedness, notation consistency, and visual presentation quality.
```

若 `REVIEWER_BIAS_GUARD = false`（仅限旧版调试），使用保存的 threadId 调用 `mcp__codex__codex-reply`；这**不是**推荐路径。

### Step 5.5: Kill Argument 练习（仅限理论/范围重的论文）

只有当论文偏重理论（源码中出现 ≥5 个 `\begin{theorem}|\begin{lemma}|\begin{proposition}|\begin{corollary}` 环境）或标题/摘要中有明确的范围/普适性声称，并且只在其最后预定轮次（`current_round == MAX_ROUNDS`）上运行本步。

**委托给 `/kill-argument`** — 规范实现位于 `skills/kill-argument/SKILL.md`（2026 年 5 月抽出）。本步骤不重新实现"攻击与裁决"提示词模板，而是调用该 Skill 并读取其输出：

```bash
# Invoke the canonical adversarial-review primitive on the current paper.
# /kill-argument runs two fresh-thread codex gpt-6-astra ultra calls and writes
# KILL_ARGUMENT.{md,json} into the paper directory. It is detect-only —
# it never edits the paper itself.
/kill-argument "$PAPER_DIR"

# Read the structured verdict.
KILL_VERDICT=$(jq -r '.verdict' "$PAPER_DIR/KILL_ARGUMENT.json")
KILL_REASON=$(jq -r '.reason_code' "$PAPER_DIR/KILL_ARGUMENT.json")
```

**合并规则**（这是 auto-loop 的职责，`/kill-argument` 本身仅检测、不改动）：

- 从 `KILL_ARGUMENT.json` 读取 `details.decomposed_points`。
- 对每个满足 `verdict == "still_unresolved"` 或 `verdict == "partially_answered"` 且 `severity_if_unresolved == "critical"` 的点：
  - 按语义重叠（约 85% 相似度阈值）对照第 2 轮弱点清单去重。
  - 若为新发现，将其追加到 Step 6 修复清单，以 recommended_fix 作为行动描述。
- 若裁决显示该问题属于 `answered_by_current_text`，只有在亲自核实所引用的 file:line 证据之后，才可对既有弱点项降级。
- 将 `KILL_ARGUMENT.md` 与合并决策都记录到 `PAPER_IMPROVEMENT_LOG.md`。
- 若 `HUMAN_CHECKPOINT = true`，在请用户继续之前，把合并后的发现纳入检查点摘要。

本阶段直接衔接 Step 6。合并后的发现必须在最终重新编译之前落位。

若 `/kill-argument` 返回 `verdict: NOT_APPLICABLE`（论文不够理论/范围重，无需此检查），整体跳过 Step 5.5 并进入 Step 6。若返回 `BLOCKED` 或 `ERROR`，把原因记录到 `PAPER_IMPROVEMENT_LOG.md` 并在不合并的情况下继续，循环不应卡死在一个无法运行的对抗性检查上。

**经验动机：**在一次真实的投稿运行中，经过若干轮标准改进（分数 7-8/10）后，kill-argument 练习暴露了此前审查都未捕捉的框定弱点（例如某设定大多是有条件的而非真正普适，或某 baseline 与真实系统无关）。作者的 rebuttal 迫使其在摘要与讨论中写明范围限定。

### Step 5b: 人工检查点（如启用）

**若 `HUMAN_CHECKPOINT = false` 则跳过。** 同 Step 2b ， 展示第 2 轮审查，等待用户输入。

### Step 6: 实施第 2 轮修复

流程同 Step 3。典型的第 2 轮修复：
- 添加验证理论的受控合成实验
- 双向重新校准声称：收窄真实的过度声称，直接陈述
  被支持的声称，把散落的泛泛限定语归并进
  Limitations，并且不要把证据已经支持的声称重新软化
- 把非形式化论证形式化（例如截断 → 形式化命题）
- 只在缺失实质性局限时使 Limitations 更具体

**编辑白名单门控（若设置）：**同 Step 3 ， 若设置了 `EDIT_WHITELIST`，在应用每个拟定编辑之前运行路径 + 禁止操作检查。拒绝记录到 `PAPER_IMPROVEMENT_LOG.md` 的 `## Rejected by edit_whitelist (Round 2)` 之下，循环继续。轮末汇总上报拒绝摘要。

### Step 7: 重新编译第 2 轮

```bash
cd paper && latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cp main.pdf main_round2.pdf
```

### Step 8: 格式检查

在最终重新编译之后，运行**位置感知**的格式合规检查。

```bash
# If the log lacks file/line data, rerun the final compile once with -file-line-error.
cd paper && latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error main.tex
```

```bash
# 1. Page count vs venue limit
PAGES=$(pdfinfo paper/main.pdf | grep Pages | awk '{print $2}')
echo "Pages: $PAGES (limit: 9 main body for ICLR/NeurIPS)"

# 2. Duplicate labels: HARD BLOCK
DUP_LABELS=$(grep -Rho "\\\\label{[^}]*}" paper/main.tex paper/sections 2>/dev/null | sort | uniq -d || true)
if [ -n "$DUP_LABELS" ]; then
    echo "Duplicate labels found (BLOCKING):"
    echo "$DUP_LABELS"
fi

# 3. Overfull warnings with location classification
OVERFULLS=$(grep -n "Overfull \\\\hbox" paper/main.log 2>/dev/null || true)

# Main body = source files before \appendix in main.tex.
# Appendix = source files after \appendix, or files whose path contains "appendix".
# Bibliography = paper.bbl, references.bib, or bibliography-generated output.
MAIN_BODY_OVERFULL=$(echo "$OVERFULLS" | grep -v -E 'appendix|paper\.bbl|references\.bib' || true)
APPENDIX_OVERFULL=$(echo "$OVERFULLS" | grep -E 'appendix' || true)
BIB_OVERFULL=$(echo "$OVERFULLS" | grep -E 'paper\.bbl|references\.bib' || true)

echo "Main-body overfulls (any size BLOCKS):"
echo "$MAIN_BODY_OVERFULL"
echo "Appendix overfulls (>10pt blocks):"
echo "$APPENDIX_OVERFULL"
echo "Bibliography overfulls (>20pt blocks):"
echo "$BIB_OVERFULL"
```

**停止标准：**
- 任何重复 label 都会阻止完成。
- 正文中的任何 overfull（无论大小）都会阻止完成。
- 附录 overfull 只有超过 10pt 或可见裁切时才阻止完成。
- 参考文献 overfull 只有超过 20pt 或可见裁切时才阻止完成。
- underfull hbox 保持为警告，除非造成明显的版面损坏。

**自动修复模式（位置感知）：**

| 问题 | 修复 |
|-------|-----|
| 正文公式 overfull | 用 `aligned` / `split` / `multline` 拆分，或缩短记号 |
| 正文表格 overfull | 减小字号、缩放表格，或跨行断表 |
| 正文文本 overfull | 改写措辞；不要用全局 `\sloppy` 掩盖 |
| 附录 overfull ≤ 10pt | 仅警告，除非可见裁切 |
| 附录 overfull > 10pt | 若溢出可见则应用同样修复 |
| 参考文献 overfull ≤ 20pt | 仅警告，除非由格式错误的条目或裁切引起 |
| 参考文献 overfull > 20pt | 修复格式错误的条目、URL 或 DOI 格式 |
| 超页数上限 | 将内容移入附录、压缩表格、缩小图尺寸 |

**位置感知解读：**
- 按 `-file-line-error` 日志中报告的源文件分类。
- 无法分类的警告按正文处理并修复。

**经验动机：**在一次真实的投稿运行中，数十个 overfull hbox 警告（最大的远超 100pt，位于附录证明中）跨越多个改进轮次幸存下来，因为旧的"overfull > 10pt 阻止"一刀切规则过于宽松，对所有位置一视同仁。

### Step 9: 记录结果

在论文目录创建 `PAPER_IMPROVEMENT_LOG.md`：

```markdown
# Paper Improvement Log

## Score Progression

| Round | Score | Verdict | Key Changes |
|-------|-------|---------|-------------|
| Round 0 (original) | X/10 | No/Almost/Yes | Baseline |
| Round 1 | Y/10 | No/Almost/Yes | [summary of fixes] |
| Round 2 | Z/10 | No/Almost/Yes | [summary of fixes] |

## Round 1 Review & Fixes

<details>
<summary>GPT-6-Astra xhigh Review (Round 1)</summary>

[Full raw review text, verbatim]

</details>

### Fixes Implemented
1. [Fix description]
2. [Fix description]
...

## Round 2 Review & Fixes

<details>
<summary>GPT-6-Astra xhigh Review (Round 2)</summary>

[Full raw review text, verbatim]

</details>

### Fixes Implemented
1. [Fix description]
2. [Fix description]
...

## PDFs
- `main_round0_original.pdf` — Original generated paper
- `main_round1.pdf` — After Round 1 fixes
- `main_round2.pdf` — Final version after Round 2 fixes
```

### Step 9: 汇总

向用户报告：
- 分数演进表
- 每轮修复的 CRITICAL/MAJOR/MINOR 问题数量
- 最终页数
- 遗留问题（若有）

### 飞书通知（如已配置）

在每轮审查之后以及最终完成时，检查 `~/.claude/feishu.json`：
- **每轮之后**：发送 `review_scored` ， "Round N: X/10 — [key changes]"
- **最终轮之后**：发送 `pipeline_done` ， 分数演进表 + 最终页数
- 若配置不存在或 mode 为 `"off"`：完全跳过（no-op）

## 输出

```
paper/
├── main_round0_original.pdf    # Original
├── main_round1.pdf             # After Round 1
├── main_round2.pdf             # After Round 2 (final)
├── main.pdf                    # = main_round2.pdf
└── PAPER_IMPROVEMENT_LOG.md    # Full review log with scores
```

## 关键规则

- **大文件处理**：如果 Write 工具因文件大小失败，立即改用 Bash（`cat << 'EOF' > file`）分块写入重试。不要询问用户许可，直接静默执行。

- **保留所有 PDF 版本** ， 用户需要对比演进
- **保存完整原始审查文本** ， 不要对 GPT-6-Astra 的响应做摘要或截断
- **审查者独立性（第 2 轮及以后）**：当 `REVIEWER_BIAS_GUARD = true`（默认）时，每轮审查都使用**全新的** `mcp__codex__codex` 线程；绝不使用 `mcp__codex__codex-reply`，也绝不在提示词中包含"自上轮以来"/修复摘要。见上文"审查者独立性协议"一节。
- **修复后必须重新编译** ， 在继续之前验证 0 错误
- **不得捏造实验结果** ， 合成验证必须描述方法论，不得编造数字
- **尊重论文的声称** ， 收窄真实的过度声称而不是添加无支持的新声称，直接陈述被支持的声称而不是裹上新的模糊限定
- **全局一致性** ， 重命名记号或更改某声称的范围时，让所有文件（摘要、引言、方法、实验、理论章节、结论、表格、图注）中的每一处复述在语义上保持一致；一致指的是范围匹配，而不是到处复制免责声明句
- **编辑白名单拒绝会被记录，而不是被静默丢弃** ， 当设置了 `EDIT_WHITELIST` 且某个编辑因路径或禁止操作违规被拒绝时，该拒绝必须附加到 `PAPER_IMPROVEMENT_LOG.md`，含文件、原因、违规模式与原始审查关切。循环在每轮结束时报告拒绝摘要（若 `HUMAN_CHECKPOINT = true`，也包含在检查点中）。绝不静默吞掉白名单拒绝，审计留痕正是该参数的全部意义。

## 典型分数演进

基于对一次真实理论论文运行的端到端测试：

| 轮次 | 分数 | 关键改进 |
|-------|-------|-----------------|
| Round 0 | 4/10（内容） | 基线：假设-模型不匹配、过度声称、记号问题 |
| Round 1 | 6/10（内容） | 修复假设、软化声称、添加解释、重命名记号 |
| Round 2 | 7/10（内容） | 添加合成验证、形式化截断命题、更强的局限性 |
| Round 3 | 5→8.5/10（格式） | 移除 hero 图、附录，压缩结论，修复 overfull hbox |

**3 轮共提升 4.5 分**（2 轮内容 + 1 轮格式）对一篇结构良好但粗糙的初稿是典型水平。投稿时的最终状态：overfull hbox 清零、长度符合会议格式要求。

## 审查留痕

在每次 `mcp__codex__codex` 或 `mcp__codex__codex-reply` 审查者调用之后，按 `shared-references/review-tracing.md` 保存 trace（Policy C ， 取证级；绝不静默跳过）。使用 `save_trace.sh`（按 `shared-references/integration-contract.md` §2 的链条解析）或直接把文件写入 `.aris/traces/<skill>/<date>_run<NN>/`。遵守 `--- trace:` 参数（默认：`full`）。
