> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/comparison.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 对比研究与综述

有明确对比意图时，在引擎执行和综述之前阅读。对比例外由根级输出法则定义。

## 若 QUERY_TYPE = COMPARISON

用户问 "X vs Y"（或 "X vs Y vs Z"）时，引擎并行发起 N 次完整 `pipeline.run()` 调用：每个实体一次。这恢复了旧的 N 轮架构（回退了牺牲每实体深度的单轮延迟优化）；并行执行让总耗时约等于单轮。

**宿主网页搜索可用时，逐实体解析是强制的。** 在一次引擎前的隔离网页搜索调度中解析每个实体（研究运行手册）。对每个实体解析完整的 Step 0.55 栈（X 句柄、subreddit、GitHub 用户/仓库、新闻背景）。然后组装把每个对手映射到其定向信息的 `--competitors-plan` JSON，用 vs 主题串调用一次引擎。宿主网页搜索不可用时，按根级要求跳过 Step 0.55 和 0.75。用下方无网页搜索命令调用，不带宿主查询计划；存在已配置解析器时，引擎独立解析主实体和每个对手，再在内部规划各子运行。没有已配置解析器时，关键词检索仍会运行，但实体定向可能更薄。Grok Bot X 连接器仍可经 `--competitors-plan` 提供逐实体帖子信封，无需查询计划。

对手定向条目接受 `x_handle`、`x_related`、`subreddits`、`github_user`、`github_repos`、`trustpilot_domain`、`context` 和 `x_posts`。相关句柄、subreddit 和仓库用数组。其他对手定向键会被忽略；不要为专属 subreddit、TikTok 或 Instagram 发明字段。

**每次运行的输出形态：**
- `--emit=compact` / `--emit=md` 时没有单独的合并 Markdown 原始文件。主主题保存为 `{main-slug}-raw.md`；每个对手保存为 `{peer-slug}-raw.md`。
- `--emit=html` 时，主保存产物是位于 `{main-slug}-vs-{peer-slug}-raw-html[...].html` 的合并对比 HTML；每个对手也可能另存自己的逐实体 HTML 产物。
- 引擎把每个写入文件记录为 `[last30days] Saved output to {path}`，对比运行还会跟一行 `[last30days] Comparison artifact set: main={path}; peers={path, ...}`。以该日志行为准，不要从 slug 重算路径。
- stdout 展示带 `## Head-to-Head` 脚手架和逐实体 Resolved Entities 块的合并对比。

网页搜索宿主上，只对 **TOPIC_A**（不是整个 vs 串）经 Step 0.75 生成 `QUERY_PLAN_JSON`。主实体接收该 `--plan`；对手子运行独立规划。对手计划提供对手定向，不提供对手查询计划。

把 `COMPETITORS_PLAN_JSON` 构建为合法 JSON，键为对手的准确名字，值为 JSON 编码的字符串。例如一个对手条目可以是 `{"Peer Widget":{"x_handle":"peer_widget","subreddits":["peer_widget"],"context":"The product says \"zero setup\""}}`。带 X 连接器的 Grok Bot 上，要包含每个实体（含主实体）的 `x_posts` 信封路径，以及其句柄通道对应的 `x_handle` 和 `x_related` 字段。主实体的句柄和相关句柄也要经外层 flag 传入。名字和抓取到的 context 中的引号、反斜杠、换行都要编码；绝不把原始值直接粘进 JSON 引号之间。选用数据中不出现的带引号 heredoc 分隔符。主题和主实体定向的 heredoc 同样遵守该分隔符规则。

双实体对比时，任一命令的主题 heredoc 中省略 ` vs {TOPIC_C}`。更多实体时，在引擎对比上限之内纳入每个名字。

### 宿主有网页搜索时

```bash
(
# SKILL_DIR is already bound to the directory containing the loaded root SKILL.md.
# Never rebind it to this reference directory or search other installations.

if [ ! -f "$SKILL_DIR/scripts/last30days.py" ]; then
  echo "ERROR: scripts/last30days.py not found under SKILL_DIR=$SKILL_DIR" >&2
  echo "Re-check SKILL_DIR against the root SKILL.md loaded by the host; never use a reference directory." >&2
  exit 1
fi

COMPARISON_TOPIC=$(cat <<'TOPIC_EOF'
{TOPIC_A} vs {TOPIC_B} vs {TOPIC_C}
TOPIC_EOF
)
TOPIC_A_HANDLE=$(cat <<'HANDLE_EOF'
{TOPIC_A_HANDLE}
HANDLE_EOF
)
TOPIC_A_RELATED=$(cat <<'RELATED_EOF'
{TOPIC_A_RELATED}
RELATED_EOF
)
TOPIC_A_SUBS=$(cat <<'SUBS_EOF'
{TOPIC_A_SUBS}
SUBS_EOF
)
MAIN_TARGETING=()
[ -n "$TOPIC_A_HANDLE" ] && MAIN_TARGETING+=(--x-handle="$TOPIC_A_HANDLE")
[ -n "$TOPIC_A_RELATED" ] && MAIN_TARGETING+=(--x-related="$TOPIC_A_RELATED")
[ -n "$TOPIC_A_SUBS" ] && MAIN_TARGETING+=(--subreddits="$TOPIC_A_SUBS")

# BSD/macOS mktemp requires XXXXXX at the end of the template.
COMPETITORS_PLAN_FILE=$(mktemp "${TMPDIR:-/tmp}/last30days-competitors.XXXXXX")
trap 'rm -f -- "$COMPETITORS_PLAN_FILE"' EXIT
# >| not >: mktemp already created the file, so a plain > is refused under
# `set -o noclobber` (leaving the plan empty -> deterministic fallback).
cat >| "$COMPETITORS_PLAN_FILE" <<'PLAN_EOF'
{COMPETITORS_PLAN_JSON}
PLAN_EOF
"${LAST30DAYS_PYTHON}" -m json.tool "$COMPETITORS_PLAN_FILE" >/dev/null || exit 2

"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" "$COMPARISON_TOPIC" \
  --emit=compact \
  --plan - \
  --save-dir="${LAST30DAYS_MEMORY_DIR}" \
  --save-suffix=v3 \
  "${MAIN_TARGETING[@]}" \
  --competitors-plan "$COMPETITORS_PLAN_FILE" <<'QUERY_PLAN_EOF'
{QUERY_PLAN_JSON}
QUERY_PLAN_EOF
)
```

任何其他外层定向 flag，其值都经带引号 heredoc 捕获，并以带引号的变量展开加入 `MAIN_TARGETING`。未解析的 flag 省略。绝不把主题、句柄、subreddit 或抓取的 context 直接粘进 shell 命令词。带引号 heredoc 让 shell 活性文本保持字面；`json.tool` 会在研究运行前拒绝格式错误的对手 JSON。

清理 trap 会在研究后删除对手计划文件。之后要导出 HTML 时，按 `save-html-brief.md` 执行，用 `--cached-report` 和原始主题。不要重放已删除的计划路径。缓存保留每个实体的报告和定向；缓存过期时，先重建计划再重新研究。

### 宿主无网页搜索时

带官方 X 连接器的 Grok Bot 上，先按 `grok-bot-x.md` 为每个实体抓取并写入一个信封，再运行本命令。把 `COMPETITORS_PLAN_JSON` 替换为以每个实体名（含主实体）为键的 JSON，值含该信封的绝对路径作为 `x_posts`。信封含 `from` 或 `mention` 调用时，其计划条目还须含对应的 `x_handle`；含 `related` 调用时，把它们的句柄作为 `x_related` 数组。例如 `{"Main Brand":{"x_posts":"/tmp/main.json","x_handle":"mainbrand"},"Peer Brand":{"x_posts":"/tmp/peer.json","x_handle":"peerbrand"}}`。把下方 `TOPIC_A_HANDLE` 设为主实体对应的句柄，`TOPIC_A_RELATED` 设为其逗号分隔的相关句柄；没有已知句柄就留空。主实体的计划条目校验其信封，外层 flag 定向其 pipeline 运行。没有已知句柄时只抓一次 topic 调用并省略句柄字段。在与信封设置相同的 shell 中运行本命令，父级清理 trap 才能保持有效。其他宿主直接用本命令，不带对手计划。

```bash
(
COMPARISON_TOPIC=$(cat <<'TOPIC_EOF'
{TOPIC_A} vs {TOPIC_B} vs {TOPIC_C}
TOPIC_EOF
)
MAIN_TARGETING=()
COMPETITORS_PLAN_ARGS=()
if [ "${LAST30DAYS_HOST:-}" = "grok-bot" ] && [ "${LAST30DAYS_X_HOST_LANE:-}" = "1" ]; then
  TOPIC_A_HANDLE=$(cat <<'HANDLE_EOF'
{TOPIC_A_HANDLE}
HANDLE_EOF
)
  TOPIC_A_RELATED=$(cat <<'RELATED_EOF'
{TOPIC_A_RELATED}
RELATED_EOF
)
  [ -n "$TOPIC_A_HANDLE" ] && MAIN_TARGETING+=(--x-handle="$TOPIC_A_HANDLE")
  [ -n "$TOPIC_A_RELATED" ] && MAIN_TARGETING+=(--x-related="$TOPIC_A_RELATED")
  COMPETITORS_PLAN_FILE=$(mktemp "${TMPDIR:-/tmp}/last30days-competitors.XXXXXX")
  trap 'rm -f "$COMPETITORS_PLAN_FILE"' EXIT
  cat >| "$COMPETITORS_PLAN_FILE" <<'PLAN_EOF'
{COMPETITORS_PLAN_JSON}
PLAN_EOF
  "${LAST30DAYS_PYTHON}" -m json.tool "$COMPETITORS_PLAN_FILE" >/dev/null || exit 2
  COMPETITORS_PLAN_ARGS=(--competitors-plan "$COMPETITORS_PLAN_FILE")
fi
"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" "$COMPARISON_TOPIC" \
  --emit=compact --auto-resolve \
  --save-dir="${LAST30DAYS_MEMORY_DIR}" --save-suffix=v3 \
  "${MAIN_TARGETING[@]}" \
  "${COMPETITORS_PLAN_ARGS[@]}"
)
```

本分支没有宿主编写的 `--plan`。无网页搜索场景下唯一的 `--competitors-plan` 就是上文的 Grok Bot 连接器交接。用户给了显式定向 flag 时，按上文经带引号变量传值。不要伪造宿主查询计划，也不要假装空的 `## Resolved Entities` 字段能证明在不支持该步骤的宿主上跳过了 Step 0.55。

主题 A（主主题，vs 串中的第一个）照常使用外层 `--x-handle`、`--x-related`、`--subreddits`、`--github-user`、`--github-repo`、`--trustpilot-domain`、`--tiktok-*`、`--ig-creators`。主题 B 和 C 的定向来自 `--competitors-plan` 条目（按实体名做键，大小写不敏感）：主主题条目不会覆盖那些外层定向 flag，所以主主题的 Trustpilot 域必须走外层 flag。逐实体 `x_posts` 条目是显式例外：它既能提供对手信封，也能提供主实体的连接器信封。

**宿主网页搜索可用时对 N 个实体执行 Step 0.55。** 适用于单实体主题的同一研究前协议，对 vs 运行中的每个实体都要执行。N=3 意味着 3 次 WebSearch 查 X 句柄、3 次查 subreddit、3 次查 GitHub、3 次查新闻背景，或等价的合并查询。在该宿主路径上，任何实体的 `## Resolved Entities` 块中出现横线，就意味着你跳过了该实体的 Step 0.55。用修正后的计划重跑。

**宿主网页搜索可用时，做 WebSearch 补充检索**（经研究运行手册中引擎后的隔离网页搜索调度），查询：`{TOPIC_A} vs {TOPIC_B} comparison {YEAR}` 和 `{TOPIC_A} vs {TOPIC_B} which is better`。它们能抓到逐实体检索可能漏掉的对手比较文章。

**逐实体使用 `RESOLVED_POSITIONING`（Step 0.55 第 6 项），两种用法。** 第一，把每个实体的 `What it is` 单元格锚定在其当前抓取到的宣传口径上：按它今天对自己的宣传来描述该实体，绝不用记忆。第二，若某实体一个月的证据与其宣传直接相关（支持某个具体主张、与之相悖，或讨论本身就聚焦宣传阵地），就在对比综述中该实体小节内用一句散文说明（紧跟 Community Sentiment 行之后：模板标出了该槽位），锚定到真实且互动良好的条目，点名但不带计数。当舆论与宣传正交（同实体，但谈的是宣传未涉及的东西）时，对宣传一字不写：省略才是正确输出，编造关联比沉默更糟。匹配高度：用具体主张（"zero-config"、"fastest"、某个在线率数字）对照具体帖子；绝不拿宽泛口号（"financial infrastructure"）对照单个帖子，太宽泛，谈不上命中或落空。表述限定在窗口内："本月讨论"，绝不用单个 30 天窗口撑不起来的趋势动词（如 "losing the narrative"）。某实体本次运行确实没有抓到定位信息时，两种用法都跳过：绝不从记忆里补宣传。

**用上文适用的对比调用替代研究运行手册的 Step 1 命令。** 宿主网页搜索可用时执行运行手册的 Step 2 补充和 Step 2.5 附录（对比运行会追加到每个逐实体文件），然后用下方对比模板写正文，替代 `synthesis.md` 的通用模板。

**对比表格脚手架（引擎生成，原样透传）：** 对比主题下，引擎的 compact 输出包含一个 `## Head-to-Head` 块，内含空 Markdown 表（列 = 实体，行 = "What it is"、"Philosophy"、"Best for" 之类的维度）。你的综述必须原样包含该块并填入单元格，位置在叙事与 emoji 树页脚之间。每个单元格 5-15 个词。单元格内用 ' - '（带空格的连字符），不用 em-dash。


### 若 QUERY_TYPE = COMPARISON

**对比查询有自己的综述模板。对比绝不要用通用查询的 `What I learned:` + 加粗引导段 + `KEY PATTERNS:` 结构。** 下方对比模板是被 4 月 9 日发布视频范例验证过的标准形态。逐节照做。

语态契约 LAWs 1、3、5 对比原样适用（省略多余的尾部来源清单、不用 em-dash、引擎页脚透传），服从更高优先级的宿主/工具要求与用户指令。LAWs 2 和 4 有对比专属例外（见 LAW 块：对比标题和下方五个小节标题是必需的，不算违规）。

**必需的对比结构（对齐 4 月 9 日范例）：**

````
{the engine's first line, copied verbatim}

# {TOPIC_A} vs {TOPIC_B} [vs {TOPIC_C}]: What the Community Says (/Last30Days)

## Quick Verdict

[One paragraph. Frame the thesis (are these competitors or layers of a stack? who's dominant? who's challenging?). Include scale stats for each entity inline (GitHub stars, user counts, whatever metric is comparable). End with one quotable community framing — a tweet, a Reddit quote, a YouTube clip — that captures how the community sees the relationship.]

## {Entity 1}

**Community Sentiment:** [Positive / Mixed / Negative / Enthusiastic / Security-concerned / etc.] ({N}+ mentions across {source list})

[Optional pitch-vs-pulse sentence - ONLY if `RESOLVED_POSITIONING` was captured for this entity AND the month's evidence directly supports a specific claim, cuts against one, or is squarely about the pitched ground: one windowed prose sentence anchored to a real, well-engaged item, named without its count. Otherwise omit entirely - silence, not a placeholder.]

**Strengths (what people love)**
- [Specific strength with `per <source>` attribution]
- [Specific strength with `per <source>` attribution]
- [Specific strength with `per <source>` attribution]

**Weaknesses (common complaints)**
- [Specific complaint with `per <source>` attribution]
- [Specific complaint with `per <source>` attribution]

## {Entity 2}

[Same structure: Community Sentiment, Strengths bullets, Weaknesses bullets]

## {Entity 3}

[Same structure]

## Head-to-Head

| Dimension | {Entity 1} | {Entity 2} | {Entity 3} |
|---|---|---|---|
| What it is | ... | ... | ... |
| GitHub stars | ... | ... | ... |
| Philosophy | ... | ... | ... |
| Skills | ... | ... | ... |
| Memory | ... | ... | ... |
| Models | ... | ... | ... |
| Security | ... | ... | ... |
| Best for | ... | ... | ... |
| Install | ... | ... | ... |

(Engine emits this scaffold; fill the cells with 5-15 words each. If an axis does not apply to the topic class, write "N/A" or a topic-appropriate substitute rather than inventing data. Ground the `What it is` row in `RESOLVED_POSITIONING` when captured - each entity described as it pitches itself today, fetched this run, never from memory.)

## The Bottom Line

**Choose {Entity 1} if** [specific use case, comfort profile, tradeoff]. [One supporting sentence with attribution.]

**Choose {Entity 2} if** [specific use case, comfort profile, tradeoff]. [One supporting sentence with attribution.]

**Choose {Entity 3} if** [specific use case, comfort profile, tradeoff]. [One supporting sentence with attribution.]

## The emerging stack

[One paragraph. Name the combination pattern the community is converging on. Cite specific sources (`per @handle`, `per r/sub`, `per {channel} on YouTube`). This is the synthesis moment of the piece. If the data does not support an emerging-stack observation, write "No emerging stack pattern has crystallized in the research window yet" rather than fabricating one.]

```text
---
✅ All agents reported back!
├─ 🟠 Reddit: ...
├─ 🔵 X: ...
(engine footer passed through when emitted, LAW 5; include its saved-file pointer only if emitted)
---
```

I've compared {TOPIC_A} vs {TOPIC_B} [vs ...] using the latest community data. Some things you could ask:
- [follow-up referencing comparison specifics, e.g. "Deep dive into {Entity} alone with /last30days {Entity}"]
- [follow-up referencing a specific claim from the Strengths/Weaknesses block]
- [follow-up on a specific dimension from the Head-to-Head table]
- [follow-up on the emerging-stack combination pattern]
````

**Claude Code 上**（设置了 `CLAUDECODE`），`references/synthesis.md` 的 NO MARKDOWN LISTS 规则同样适用：Strengths、Weaknesses 和后续提问列表写成 `• ` 行，不用 `- ` 列表。

**不要：**
- 使用 `What I learned:` 散文标签（那是通用查询语态）
- 正文使用带 ` - ` 分隔的加粗引导段（那是通用查询语态）
- 使用 `KEY PATTERNS from the research:` 编号列表（已被逐实体 Strengths/Weaknesses 列表和新兴组合段取代）
- 伪造 `## Notable Stats` 块（引擎页脚就是统计块，见 LAW 5）
- 给引语和署名附加点赞、顶、浏览或得分计数，或添加 pulled-quote 行（见 `references/synthesis.md` 的 COUNTS IN PROSE；实体规模数据保留）
- 产出上列六个之外的小节标题（依 LAW 4 对比例外，只允许 `## Quick Verdict`、每个实体的 `## {Entity}`、`## Head-to-Head`、`## The Bottom Line`、`## The emerging stack`）

**参考范例：** `$LAST30DAYS_MEMORY_DIR/openclaw-vs-hermes-vs-paperclip-LAUNCH-VIDEO-april9-exemplar.md` 保存了 4 月 9 日的标准输出和完整结构分析。逐节对齐这个形态。
