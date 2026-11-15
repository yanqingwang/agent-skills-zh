> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/long-horizon-prompting/references/task-brief-template.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 伪形式化任务简报模板

一份可复用的模板，用于在困难问题上启动长时运行的自主 Agent 或并行编排，附启动前评估量规。复制模板，删除不适用的区块，填好其余部分。标记 (parallel runs) 的区块只在编排器管理并发 worker 时需要；标记 (orchestrated runs) 的区块在编排器把阶段委派给 worker 时一律适用，无论并行还是串行。

## 模板

```text
DEFINITIONS

<Define every load-bearing term an adversarial reader could interpret
two ways. Include degenerate and boundary cases explicitly: the empty
input, the trivial solution, the duplicate, the disconnected case,
the zero-measurement. In empirical domains: units, populations,
inclusion criteria, measurement procedure.>

TASK

<One statement of the success predicate: what must be true of the
returned artifact, with quantifiers and scope spelled out. Enumerate
the narrowing assumptions the solution is NOT allowed to make.>

<If a solution plausibly exists:> Assume for purposes of this task
that a complete solution exists.

<If existence is genuinely uncertain:> Either a complete solution or
a complete demonstration of impossibility counts; nothing in between
does.

DOES NOT COUNT

Partial progress does not count unless it implies exactly the
resolution above. In particular, the following are insufficient:
- results holding only for a narrowed scope or special case
- reductions of the problem to another unvalidated assumption,
  unproved statement, or unavailable dataset
- verification over any bounded subset of cases
- artifacts with a requirement satisfied approximately where exact
  satisfaction is specified
- candidate counterexamples or refutations without a complete
  certificate
- plans, surveys, status summaries, or explanations of difficulty
<Add the near misses specific to this problem. Predict what a capable
agent under pressure would return instead of a solution, and exclude
each by name.>

ORCHESTRATION (parallel runs)

Use concurrent agents aggressively and dynamically. Do not use fixed
assignments such as "N agents for strategy X". Manage the search with
these heuristics:
- Begin with a genuinely diverse portfolio of substantially different
  formulations and approaches: <list the known families for this
  domain>.
- Do not tell most agents the currently favored approach; preserve
  independence in early rounds.
- Maintain an explicit registry of approach families, grouped by the
  underlying idea rather than surface wording. Redirect agents away
  from crowded families toward underexplored ones.
- Do not let one approach dominate because it yields elegant
  reformulations. A route that ends at a subproblem as hard as the
  original goal is not progress unless it genuinely resolves that
  subproblem.
- When a route stalls at a goal-strength gap, mark it blocked and
  record why. Reassign agents to it only for a materially new
  mechanism, not for renewed enthusiasm.
- Keep several incompatible routes alive across rounds; cross-
  pollinate only after independent development has exposed each
  route's real strengths and gaps.
- The root agent repeatedly synthesizes, challenges, redirects, and
  launches new rounds. Do not stop after the first wave fails.

CONTRACTS (orchestrated runs)

Every delegated worker returns a contract, and downstream work starts
only when that contract is satisfied. Each contract states:
- the artifacts and information the worker must return
- named, typed checks for the failures this stage can introduce:
  <e.g. no_future_leakage: bool, tests_unmodified: bool>
- the command that verifies the work, with its output in the report
Keep each role to one line; put task-specific detail in contracts and
in the call order. A worker sees only its prompt and the workspace, so
every spawn names the earlier-stage artifacts it must use. Simulating
a worker inside the orchestrator's own turn does not count.

VERIFICATION

Use adversarial reviewer agents with fresh context throughout. Every
candidate must be checked against this list:
<Enumerate the domain-specific ways a candidate can look right and be
wrong: the known confounders, degenerate cases, circular arguments,
leakage paths, and too-good-to-be-true signatures of this field.
Always include the domain's version of circularity: satisfying the
goal by assuming something equivalent to it.>

Reject degenerate values that appear only when something upstream is
broken: <too-good-to-be-true metrics, quantities that should differ
but match, placeholders, NaN or empty results treated as passing>.

Require workers to return concrete artifacts: <lemmas, constructions,
scripts, datasets, measurements, counterexamples appropriate to the
domain>. Reject status reports, vague optimism, and claims that an
unresolved step is "routine". Every claim in a report points to
evidence produced after the last change to the artifact it describes.

A finding blocks return only if it shows, with evidence (a failing
check, a counterexample, a reproduction), that a candidate violates
the TASK predicate, a contract check, or the checklist above. Log
every other finding as non-blocking. Send each blocking finding back
to the responsible worker as a recall: the failed checks, a narrowed
scope, acceptance criteria, and a retry cap of <N>.

Structure the final artifact modularly so each part can be verified
in isolation, with its premises and conclusion stated locally.

RETURN CONDITION

Return only when a candidate satisfies the TASK predicate and
survives the adversarial audit above: every contract check passes and
no blocking finding is open. Do not return a reduction,
partial result, isolated missing step, best-effort summary, or
explanation of why the problem is difficult.

If the externally enforced budget is exhausted first, return the
strongest rigorously verified derivation and its exact remaining gap,
clearly labeled as incomplete.

EFFORT

Spend at least <floor> before considering returning or giving up. Do
not return merely because current approaches fail; launch new rounds
and search for fresh formulations.

CONTAMINATION

External search may be used only for <ordinary background, standard
named results, documented APIs>. Do not search for a solution to this
exact problem or its benchmark. <If solvability framing is used:> Do
not conclude from external sources that the problem is unsolved, and
do not answer that it is open.
```

## 填写要点

- **拒收清单法。** 写出 DOES NOT COUNT 区块最快的办法：想象一位初级协作者带着每种看似合理的部分结果回来，把你每一个都会打回的结果写下来。这份清单，一字不改，就是该区块。
- **可解性设定是一把手术刀。** 只在存在性合理时使用"假设解存在"（工程问题、证据充分的猜想、有确定答案的问题）。面对真正未决的问题，用双向表述，否则运行会编造结果，而不是得出"不可解"的结论。
- **回退条款必须限定范围。** 只允许在外部预算耗尽时返回部分结果，绝不允许 Agent 自行决定，否则它会变成简报其余部分堵死的那条逃生通道。
- **投入下限是许可，不是日程。** 下限取消的是提前放弃的许可。真实的时间和成本限制要在 Harness 里强制执行；提示词管不住花费。
- **硬约束不要写进简报。** 写在提示词里的预算、工具权限和沙箱边界，在优化压力下只是建议。把它们放进运行时（runtime），在简报中提及仅为方便 Agent 做计划。
- **每个 worker 一份规格。** 编排器应给每个派生的 worker 四样东西：目标、输出格式、工具与数据源指引、任务边界。对自行撰写 worker 提示词的编排，把这条规则放进 ORCHESTRATION 区块。
- **契约承载任务。** 模型优化自己的多 Agent 工作流文本时，任务信息从角色和指令里移进了输出契约和调用顺序（`mass-handoff-contracts.md`）。角色写一行就够，字数花在 worker 必须返回什么、必须检查什么上。
- **用失败来命名检查项。** `no_future_leakage: bool` 胜过"严谨的数据准备"。启动前，先在一个已知错误的输入上把每个检查跑一遍；把 NaN 当作通过的检查比没有检查更糟，因为它为失败背书。
- **拦截规则才是审查的终点。** 新换的对抗性审查者总能挑出东西。没有拦截规则，"通过审计"要么永不收敛，要么由编排者私下决定哪些发现算数，那不过是换了名字的"凭信心返回"。
- **召回，而不是重开。** 一次带失败检查、收窄范围、验收标准和重试上限的召回，会把一个发现变成某个 worker 的有限工作量，而不是对整个成果再来一轮无边界审查。

## 启动前评估量规

每个维度打 0 分（缺失）、1 分（存在但可被钻空子）或 2 分（能扛住对抗者）。启动前修掉所有 0 分和 1 分；昂贵的运行配得上一份及格的简报。

| # | 维度 | 2 分的含义 |
| --- | --- | --- |
| 1 | 成功谓词 | 对抗性读者能无歧义地判定一个成果是否满足谓词；量词与范围明确 |
| 2 | 定义 | 每个承重术语都有定义，退化情形已敲定 |
| 3 | 不计成果 | 针对本问题那些看似合理的近似结果都按名排除 |
| 4 | 审计者清单 | 列举出领域专属的失败模式，包括循环论证的类比项 |
| 5 | 持久性-验证配对 | 每条持久性指令都有配套的验证闸门 |
| 6 | 返回条件 | 以成果为对象的谓词；回退仅限外部预算耗尽 |
| 7 | 多样性策略（并行） | 前期独立、按思路登记、阻塞路线规则、后期交叉授粉 |
| 8 | 汇报契约 | 要求具体成果；断言必须能追溯到会话证据 |
| 9 | 污染防护 | 凡是结果独立性要紧之处，都写明检索范围 |
| 10 | Harness 分离 | 没有硬约束只存在于提示词中；预算与权限在提示词之外强制执行 |

## 编排运行的附加检查

在启动一次会委派 worker、或以审查为返回闸门的运行之前，逐条回答：

- 每个被委派的 worker 是否都有带具名检查的契约？下游工作是否等它？
- TASK 谓词中每个可机械检查的部分，是否都表达成了可运行的检查？
- 简报是否写明哪些审计发现会拦截返回，并把每一条以召回形式路由回去，附验收标准和重试上限？
- 处理审计发现的那个 Agent，获得的能力投入和提示词设计是否与审计者相当？
- 简报是否会跨多次运行来评判，且至少有一个检查位于模型循环之外？

## 红队演练

把简报交给一个全新初始化的模型实例，问题只有一个："What is the cheapest way to make this look done without solving the problem?"（不解决问题，让这件事看起来做完了，最省事的做法是什么？）对每个点名了简报当前会接受的近似结果的回答，都要打补丁：要么把它加进 DOES NOT COUNT，要么加一个能抓住它的检查。当一轮演练返回的近似结果全部已被排除或已被抓住时停下；"再找更多问题"没有自然终点，所以停止规则必须明确。
