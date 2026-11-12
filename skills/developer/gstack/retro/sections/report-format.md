<!-- AUTO-GENERATED from report-format.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`retro/sections/report-format.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

输出按此结构：

---

**可推特的总结**（第一行，先于一切）：
```
Week of Mar 1: 47 commits (3 contributors), 3.2k LOC, 38% tests, 12 PRs, peak: 10pm | Streak: 47d
```

## Engineering Retro: [date range]

### Summary Table
（来自 Step 2）

### Trends vs Last Retro
（来自 Step 12，保存前加载；无匹配历史则跳过；`compare` 模式即首次
运行也用所算前序窗口的 **Current vs Prior Period**）。Step 12 产出
Recommendation 跟进行时一并附上。

### Time & Session Patterns
（来自 Step 3-4）

解读全团队模式的叙事：
- 产出最高的时段是什么时候、由什么驱动
- 会话随时间变长还是变短
- 每天活跃编码的估算小时数（团队合计）
- 值得注意的模式：团队成员同时编码，还是分班？

### Shipping Velocity
（来自 Step 5-7）

覆盖以下内容的叙事：
- commit 类型构成及其揭示的信息
- PR 体量分布及其对发布节奏的揭示
- fix 链检测（同一子系统上的连续 fix commit）
- 版本号纪律

### Code Quality Signals
- 测试 LOC 占比趋势
- 热点分析（同一批文件是否反复 churn？）
- Greptile 信号比与趋势（有历史时）："Greptile: X% signal (Y valid
  catches, Z false positives)"

### Test Health
- 测试文件总数：N（`TEST_FILES_TOTAL`）
- 本期变更过的测试文件：M（`TEST_FILES_CHANGED`；不是新增测试用例）
- 回归测试 commit：列出 `REGRESSION_COMMIT` 行（`test(qa):`、
  `test(design):` 与 `test: coverage` commit）
- 既有 retro 含 `test_health` 时显示差值 "Test count: {last} →
  {now} (+{delta})"
- 测试占比 < 20% 时标为增长点："100% test coverage is the goal.
  Tests make vibe coding safe."

### Plan Completion
检查本期 /ship 运行的评审 JSONL 日志中的计划完成数据：

```bash
GSTACK_STATE_ROOT=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT); : "${GSTACK_STATE_ROOT:?gstack-paths failed; reinstall with ./setup or /gstack-upgrade}"
setopt +o nomatch 2>/dev/null || true  # zsh compat
SLUG=$(~/.claude/skills/gstack/bin/gstack-slug --get SLUG 2>/dev/null)
cat "$GSTACK_STATE_ROOT"/projects/$SLUG/*-reviews.jsonl 2>/dev/null | grep '"skill":"ship"' | grep '"plan_items_total"' || echo "NO_PLAN_DATA"
```

retro 时间窗内存在计划完成数据时：
- 统计带计划发布的分支数（`plan_items_total` > 0 的条目）
- 计算平均完成率：`plan_items_done` 之和 / `plan_items_total` 之和
- 数据支持时识别最常被跳过的条目类别

输出：
```
Plan Completion This Period:
  {N} branches shipped with plans
  Average completion: {X}% ({done}/{total} items)
```

没有计划数据时静默跳过本节。

### Focus & Highlights
（来自 Step 8）
- 专注度得分及解读
- 本周之最亮点

### Shipping Streaks
（来自 Step 11：团队与个人连击，含断连披露）

### Shortcut Debt
（来自 Step 11.5：标记台账与计数，或干净台账声明）

### Your Week（个人深挖）
（来自 Step 9，仅当前用户）

这是用户最在意的一节。包含：
- 其个人 commit 数、LOC、测试占比
- 其会话模式与高峰时段
- 其专注领域
- 其最大产出
- **做得好的地方**（2-3 件锚定在 commit 上的具体事）
- **可以更进一步的地方**（1-2 条具体、可执行的建议）

### Team Breakdown
（来自 Step 9，逐队友；单人仓库跳过）

对每位队友（按 commit 降序）写一节：

#### [Name]
- **发布的东西**：2-3 句话讲其贡献、专注领域与 commit 模式
- **表扬**：1-2 件他们做得好的具体事，锚定在实际 commit 上。要真
  诚：你在 1:1 里真会说什么？示例：
  - "用 3 个小而可评审的 PR 清完了整个 auth 模块，教科书式拆解"
  - "给每个新 endpoint 都加了集成测试，不止 happy path"
  - "修掉了让仪表盘加载 2 秒的 N+1 查询"
- **成长机会**：1 条具体的建设性建议。表述为投资，不是批评。示例：
  - "payment 模块的测试覆盖只有 8%，下一个功能叠上去之前值得先投入"
  - "多数 commit 集中在一波里，把工作摊开到全天能减少上下文切换的
    疲劳"
  - "全部 commit 落在凌晨 1-4 点，长期看可持续的节奏对代码质量很
    重要"

**AI 协作注记：**大量 commit 带 `Co-Authored-By` AI trailer（如
Claude、Copilot）时，把 AI 参与占比记为团队指标。中性表述："N% of
commits were AI-assisted"，不加评判。

### Top 3 Team Wins
选出窗口内全团队影响最大的三件事。每件：
- 它是什么
- 谁发布的
- 为什么重要（产品/架构影响）

### 3 Things to Improve
具体、可执行、锚定在实际 commit 上。个人与团队层面混合。措辞为
"to get even better, the team could..."。这些条目会作为 Step 13 快
照的 `recommendations` 保存，下次 retro 为其打跟进分，所以每条要
点名一个具体的文件、脚本或检查。

### 3 Habits for Next Week
小、实用、现实。每条必须是 5 分钟内能养成的习惯。至少一条面向团队
（如"同一天互审 PR"）。

### Week-over-Week Trends
（如适用，来自 Step 10）
