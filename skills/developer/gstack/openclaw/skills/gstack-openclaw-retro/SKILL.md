---
name: gstack-openclaw-retro
description: "周度工程复盘。分析 commit 历史、工作模式和代码质量指标，带持久历史与趋势跟踪。具备团队感知：按人给出贡献、表扬与成长点。被要求做 weekly retro、看本周发布了什么或工程复盘时使用。"
---

> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`openclaw/skills/gstack-openclaw-retro/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 周度工程复盘

生成一份全面的工程复盘，分析 commit 历史、工作模式和代码质量指标。
具备团队感知：先识别运行命令的用户，再分析每位贡献者，按人给出表扬
与成长机会。

## 参数

- 默认：最近 7 天
- `24h`：最近 24 小时
- `14d`：最近 14 天
- `30d`：最近 30 天
- `compare`：当前窗口与等长的上一窗口对比

## 指令

解析参数确定时间窗口。默认 7 天。所有时间以用户的**本地时区**报告。

**对齐午夜的窗口：** 以天为单位时，计算本地午夜的绝对起始日期。例如
今天是 2026-03-18、窗口为 7 天，则起始日期为 2026-03-11。git log 查询
用 `--since="2026-03-11T00:00:00"`。以小时为单位时用
`--since="N hours ago"`。

---

### Step 1：收集原始数据

先 fetch origin 并识别当前用户：

```bash
git fetch origin main --quiet
git config user.name
git config user.email
```

`git config user.name` 返回的名字就是 **"you"**——正在读这份复盘的人。
其他所有作者都是队友。

运行全部这些 git 命令（彼此独立）：

```bash
# 所有 commit：时间戳、subject、hash、作者、变更文件
git log origin/main --since="<window>" --format="%H|%aN|%ae|%ai|%s" --shortstat

# 每 commit 测试行数 vs 总行数（含作者）
git log origin/main --since="<window>" --format="COMMIT:%H|%aN" --numstat

# commit 时间戳：用于会话检测与小时分布
git log origin/main --since="<window>" --format="%at|%aN|%ai|%s" | sort -n

# 变更最频繁的文件（热点分析）
git log origin/main --since="<window>" --format="" --name-only | grep -v '^$' | sort | uniq -c | sort -rn

# commit message 中的 PR 编号
git log origin/main --since="<window>" --format="%s" | grep -oE '[#!][0-9]+' | sort -t'#' -k1 | uniq

# 按作者的文件热点
git log origin/main --since="<window>" --format="AUTHOR:%aN" --name-only

# 按作者的 commit 数
git shortlog origin/main --since="<window>" -sn --no-merges

# 测试文件数
git ls-files 2>/dev/null | grep -E '(\.test\.|\.spec\.|_test\.|_spec\.)' | wc -l

# 窗口内变更过的测试文件数
git log origin/main --since="<window>" --format="" --name-only | grep -E '\.(test|spec)\.' | sort -u | wc -l
```

---

### Step 2：计算指标

计算并在总结中呈现：

- **合入 main 的 commit：** N
- **贡献者：** N
- **已合并 PR：** N
- **总新增行：** N
- **总删除行：** N
- **净增 LOC：** N
- **测试 LOC（新增）：** N
- **测试 LOC 占比：** N%
- **版本区间：** vX.Y.Z → vX.Y.Z
- **活跃天数：** N
- **检测到的会话：** N
- **平均 LOC/会话小时：** N

紧随其下展示**按作者的排行榜**：

```
Contributor         Commits   +/-          Top area
You (garry)              32   +2400/-300   browse/
alice                    12   +800/-150    app/services/
bob                       3   +120/-40     tests/
```

按 commit 数降序排列。当前用户永远排第一，标注 "You (name)"。

---

### Step 3：commit 时间分布

以本地时间展示小时直方图：

```
Hour  Commits  ████████████████
 00:    4      ████
 07:    5      █████
 ...
```

指出：
- 高峰时段
- 空窗时段
- 双峰模式（早/晚）还是连续型
- 深夜编码集群（晚 10 点后）

---

### Step 4：工作会话检测

用**45 分钟间隔**阈值（相邻 commit 之间）检测会话。

会话分类：
- **深度会话**（50 分钟以上）
- **中等会话**（20-50 分钟）
- **微型会话**（不到 20 分钟，单 commit）

计算：
- 总活跃编码时长
- 平均会话长度
- 每活跃小时 LOC

---

### Step 5：commit 类型构成

按 conventional commit 前缀分类（feat/fix/refactor/test/chore/docs），
用百分比条展示：

```
feat:     20  (40%)  ████████████████████
fix:      27  (54%)  ███████████████████████████
refactor:  2  ( 4%)  ██
```

fix 占比超过 50% 时要标示……这是"快速发布、快速修补"模式，可能意味着
评审环节有缺口。

---

### Step 6：热点分析

展示变更最多的前 10 个文件。标示：
- 变更 5 次以上的文件（churn 热点）
- 热点清单中测试文件与生产文件的比例
- VERSION/CHANGELOG 出现频率

---

### Step 7：PR 体量分布

估算 PR 体量并分桶：
- **Small**（<100 LOC）
- **Medium**（100-500 LOC）
- **Large**（500-1500 LOC）
- **XL**（1500+ LOC）

---

### Step 8：专注度得分 + 本周之最

**专注度得分：** 触及变更最频繁的那个顶级目录的 commit 占比。越高
表示专注越深。越低表示上下文切换频繁。

**本周之最：** 窗口内 LOC 最高的那个 PR。突出 PR 编号、变更 LOC 和它
为什么重要。

---

### Step 9：团队成员分析

对每位贡献者（含当前用户）计算：

1. **commit 与 LOC** …… 总 commit 数、新增、删除、净 LOC
2. **专注领域** …… 触及最多的目录/文件（前 3）
3. **commit 类型构成** …… 个人 feat/fix/refactor/test 分布
4. **会话模式** …… 何时编码（高峰时段）、会话数
5. **测试纪律** …… 个人测试 LOC 占比
6. **最大产出** …… 其影响最大的单个 commit 或 PR

**当前用户（"You"）：** 最深处理。包含全部会话分析、时间模式、专注度
得分。以第一人称表述。

**每位队友：** 2-3 句话，覆盖其发布内容和模式。然后：

- **表扬**（1-2 个具体点）：锚定在真实 commit 上。不要"干得漂亮"
  ……要说清楚具体好在哪。
- **成长机会**（1 个具体点）：表述为升级方向，不是批评。锚定在真实
  数据上。

**单人仓库：** 跳过团队拆解。

**AI 协作：** commit 带 `Co-Authored-By` AI trailer 时，把"AI 参与
commit"作为单独指标跟踪。

---

### Step 10：周环比趋势（窗口 >= 14d 时）

按周分桶并展示趋势：
- 每周 commit 数（总量与按作者）
- 每周 LOC
- 每周测试占比
- 每周 fix 占比
- 每周会话数

---

### Step 11：连击跟踪

从今天往回数连续有 commit 的天数：

```bash
# 团队连击
git log origin/main --format="%ad" --date=format:"%Y-%m-%d" | sort -u

# 个人连击
git log origin/main --author="<user_name>" --format="%ad" --date=format:"%Y-%m-%d" | sort -u
```

两者都展示：
- "团队发布连击：连续 47 天"
- "你的发布连击：连续 32 天"

---

### Step 12：加载历史并对比

检查 `memory/` 中的既往复盘：

有既往复盘时，加载最近一份并计算差值：

```
                    Last        Now         Delta
Test ratio:         22%    →    41%         ↑19pp
Sessions:           10     →    14          ↑4
LOC/hour:           200    →    350         ↑75%
Fix ratio:          54%    →    30%         ↓24pp (improving)
```

没有既往复盘时，注明"首次复盘已记录，下周再运行即可看到趋势"。

---

### Step 13：保存复盘历史

把 JSON 快照保存到 `memory/retro-YYYY-MM-DD.json`，含指标、作者、版本
区间、连击和一条可推特的总结。

---

### Step 14：撰写叙事

**按 Telegram 格式**（用 bullet 和粗体，最终输出不用 markdown 表格）。

结构：

**可推特的总结**（第一行）：
> Week of Mar 1: 47 commits (3 contributors), 3.2k LOC, 38% tests, 12 PRs, peak: 10pm | Streak: 47d

随后各节：

- **Summary** …… 关键指标
- **Trends vs Last Retro** …… 差值（首次复盘则跳过）
- **Time & Session Patterns** …… 团队何时编码、会话长度、深度 vs 微型
- **Shipping Velocity** …… commit 类型、PR 体量、fix 链检测
- **Code Quality Signals** …… 测试占比、热点、churn
- **Focus & Highlights** …… 专注度得分、本周之最
- **Your Week** …… 当前用户的个人深挖
- **Team Breakdown** …… 按队友分析，表扬 + 成长（单人则跳过）
- **Top 3 Team Wins** …… 影响最大的发布
- **3 Things to Improve** …… 具体、可执行、锚定在 commit 上
- **3 Habits for Next Week** …… 小、实用、现实（5 分钟内可养成）

---

## Compare 模式

用户说 "compare" 时：
- 对当前窗口跑一次复盘
- 对等长的上一窗口跑一次复盘
- 并排呈现指标，用箭头标示改善/回归
- 简要叙述最大变化

---

## 重要规则

- **所有时间用本地时区。** 绝不设置 `TZ`。
- **按 Telegram 格式。** 用 bullet 和粗体，最终输出避免 markdown 表格。
- **表扬锚定在 commit 上。** 绝不说"干得漂亮"却不说好在哪。
- **成长点锚定在数据上。** 没有证据就不批评。
- **保存历史。** 每次复盘都存到 `memory/` 用于趋势跟踪。
- **完成状态：**
  - DONE …… 复盘已生成、历史已保存
  - DONE_WITH_CONCERNS …… 已生成但缺数据（如无可对比的既往复盘）
  - BLOCKED …… 不在 git 仓库中，或窗口内无 commit
