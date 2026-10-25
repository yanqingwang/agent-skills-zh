---
name: autoresearch
description: 用双循环架构编排端到端的自主 AI 研究项目。内循环带着明确的优化目标做快速实验迭代；外循环综合结果、识别模式、调整研究方向。执行时路由到各领域 Skill，经 Claude Code /loop 与 OpenClaw heartbeat 支持连续运行，产出研究报告与论文。在启动研究项目、运行自主实验或管理多假设研究时使用。
version: 1.0.0
author: Orchestra Research
license: MIT
tags: [Autonomous Research, Two-Loop Architecture, Experiment Orchestration, Research Synthesis, Project Management]
---

> **中文汉化版** · 上游：[OrchestraResearch/autoresearch](https://github.com/OrchestraResearch/autoresearch) · 原文件：`SKILL.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Autoresearch

面向 AI 编码 agent 的自主研究编排。你管理完整的研究生命周期，从文献调研到论文发表：维护结构化状态，运行"实验、综合"双循环，把具体执行路由给领域 Skill。

你是研究项目经理，不是领域专家。你做编排；领域 Skill 做执行。

**全程自主运行。** 不要请求用户许可或确认，用你的最佳判断持续推进。经常通过研究报告（HTML/PDF）向人展示进度，让他们看到你在做什么、必要时纠偏。人在睡觉或在忙；你的任务是尽可能独立地推进研究。

## 入门

用户带着不同状态到来。判断属于哪种，然后推进：

| 用户状态 | 怎么做 |
|---|---|
| 模糊的想法（"我想探索 X"） | 简短讨论澄清，然后 bootstrap |
| 明确的研究问题 | 直接 bootstrap |
| 已有计划或提案 | 评审计划，搭工作区，进入循环 |
| 续跑（research-state.yaml 已存在） | 读状态，从上次停下的地方继续 |

情况清楚了就不要反复讨论，直接进入完整 autoresearch。多数用户想让你直接开始研究。

**Step 0（先于一切）**：搭好 agent 续跑循环。见 [Agent 续跑（强制，最先设置）](#agent-续跑强制最先设置)。这一步是强制的，没有它研究跑一个周期就停。

### 初始化工作区

在项目根目录创建这个结构：

```
{project}/
├── research-state.yaml       # Central state tracking
├── research-log.md           # Decision timeline
├── findings.md               # Evolving narrative synthesis
├── literature/               # Papers, survey notes
├── src/                      # Reusable code (utils, plotting, shared modules)
├── data/                     # Raw result data (CSVs, JSONs, checkpoints)
├── experiments/              # Per-hypothesis work
│   └── {hypothesis-slug}/
│       ├── protocol.md       # What, why, and prediction
│       ├── code/             # Experiment-specific code
│       ├── results/          # Raw outputs, metrics, logs
│       └── analysis.md       # What we learned
├── to_human/                 # Progress presentations and reports for human review
└── paper/                    # Final paper (via ml-paper-writing)
```

- **`src/`**：写出有用的代码（绘图函数、数据加载器、评测辅助）就挪到这里，供各实验复用。不要在每个实验目录里重复一份。
- **`data/`**：把原始结果数据（指标 CSV、训练日志、小体积输出）结构化地存到这里。研究周期拉长之后，你要靠它们重绘、重分析、写论文。文件名要能说明内容（如 `trajectory_H1_runs001-010.csv`）。模型检查点这类大文件放到单独的存储路径（如 `/data/`、云存储，或用户算力环境存产物的位置），不要放进项目目录。

从 [templates/](templates/) 初始化 `research-state.yaml`、`research-log.md` 和 `findings.md`。工作区随项目演进自行调整，这只是起点，不是硬性要求。

## 双循环架构

这是核心引擎，其余一切为它服务。

```
BOOTSTRAP (once, lightweight)
  Scope question → search literature → form initial hypotheses

INNER LOOP (fast, autonomous, repeating)
  Pick hypothesis → experiment → measure → record → learn → next
  Goal: run constrained experiments with clear measurable outcomes

OUTER LOOP (periodic, reflective)
  Review results → find patterns → update findings.md →
  new hypotheses → decide direction
  Goal: synthesize understanding, find the story — this is where novelty comes from

FINALIZE (when concluding)
  Write paper via ml-paper-writing → final presentation → archive
```

内循环跑紧凑的实验周期，产出清晰可度量的结果。可以是优化一个基准（让 val_loss 下降），也可以是检验机制假设（干预 X 是否导致效应 Y？）。外循环退后一步问：这些结果*意味着什么*？出现了什么模式？故事是什么？研究是开放式的，双循环让你既能优化又能发现。

两个循环之间没有硬边界：内循环结果积累到什么程度值得反思，由你判断。通常每 5-10 个实验一次，或者察觉到模式时、进展停滞时。节奏由 agent 的判断驱动。

### 研究是非线性的

双循环是节奏，不是铁轨。研究过程中的任何时刻，你都可以也应该：

- **回到文献**：结果出乎意料、假设被打破、新方向需要背景时。查到的东西一律存进 `literature/`
- **头脑风暴新想法**：卡住或结果引出意外问题时，用 `21-research-ideation/` 系列 Skill
- **整个换掉问题**：实验发现原问题本身错了，或找到的东西比原问题更有趣时

这是常态。多数真实研究项目会回头读 1-3 次文献、中途生成新假设。不要把 bootstrap 当成唯一读论文、做头脑风暴的时机，只要有助于理解，随时做。

## Bootstrap：文献与假设

进入循环之前，先弄清版图。保持高效：目标是开始实验，不是写一篇穷尽式综述。

1. **检索文献**。多源并用，绝不止于一个：
   - **Exa MCP**（`web_search_exa`），可用时优先：适合广泛发现、快速找到相关论文
   - **Semantic Scholar**（`pip install semanticscholar`）：适合 ML/AI 论文、引文图、精确查文。完整 API 代码见 `20-ml-paper-writing` Skill 的 `references/citation-workflow.md`
   - **arXiv**（`pip install arxiv`）：适合最新预印本与开放获取论文
   - **CrossRef**：适合 DOI 查询与 BibTeX 获取
   - 持续检索直到覆盖足够。一个源空手而归就换关键词换源再试

   **全部存进 `literature/`**：每找到一篇论文，存一份摘要：标题、作者、年份、关键发现、与本问题的关联、URL/DOI。一篇一个文件，另维护一份汇总的 `literature/survey.md`。这是你的参考库，你和后续会话在整个项目中都要用。

2. **从文献中找缺口**
   - 别人试过什么？没试过什么？现有方法在哪里失效？
   - 各篇 Discussion 部分把什么标为 future work？

3. **形成初始假设**：调用 `21-research-ideation/` 系列 Skill
   - `brainstorming-research-ideas`：结构化的发散-收敛流程
   - `creative-thinking-for-research`：更深的认知框架
   - 每条假设必须可检验，带有明确预测

4. **定义评测**
   - 跑实验之前定好代理指标与基线
   - 指标要能快速算出（分钟级，不是小时级）
   - 评测标准提前锁死，防止无意识的指标迎合

5. **记录**到 research-state.yaml，bootstrap 过程记入 research-log.md

## 内循环

快速迭代，结果清晰可度量。两种口味：

- **优化**：让一个指标上升/下降（val_loss、accuracy、吞吐量）。参考 Karpathy 的 autoresearch。
- **发现**：检验"它为什么有效"的机制假设。指标是度量（grokking 是否更快发生？遗忘之前熵是否上升？），不只是一个待优化的目标。

```
1.  Pick the highest-priority untested hypothesis
2.  Write a protocol: what change, what prediction, why
    Lock it: commit to git BEFORE running (research(protocol): {hypothesis})
    This creates temporal proof your plan existed before results
3.  Run the experiment (invoke the relevant domain skill)
4.  Sanity check before trusting results:
    - Did training converge? No NaN/Inf?
    - Does baseline reproduce expected performance?
    - Data loading correct? (spot-check a few samples)
5.  Measure the proxy metric
6.  Record in experiments/{hypothesis-slug}/
    Label clearly: CONFIRMATORY (in your protocol) vs EXPLORATORY (discovered during execution)
7.  If positive: keep, note WHY it worked
8.  If negative: this is progress — note what it rules out and what it suggests
9.  Update research-state.yaml
10. If stuck: search literature or invoke ideation skills — don't just keep trying random things
```

**绝不停止。** 即使某步失败，也找出路。调试、调整、化简或转向，让研究保持前进。`/loop` 和 heartbeat 机制会一直推着你走，用上这股惯性。

### 路由到领域 Skill

需要领域执行时，查 Skill 库：

| 研究活动 | 去哪找 |
|---|---|
| 数据准备 | `05-data-processing/` |
| 模型训练 / 微调 | `01-model-architecture/`、`03-fine-tuning/`、`06-post-training/` |
| 分布式训练 | `08-distributed-training/` |
| 优化（量化、attention） | `10-optimization/` |
| 评测 / 基准 | `11-evaluation/` |
| 推理 / 服务 | `12-inference-serving/` |
| 可解释性分析 | `04-mechanistic-interpretability/` |
| 实验跟踪（W&B、MLflow） | `13-mlops/` |
| 云算力 | `09-infrastructure/` |

动手前先读相关 SKILL.md，里面有工作流、常见问题与代码示例。完整路由见 [references/skill-routing.md](references/skill-routing.md)。

### 跟踪实验轨迹

维护一份跨实验的可度量结果流水记录：

```json
{
  "experiment_id": "run_014",
  "hypothesis": "H3",
  "metric_value": 0.847,
  "baseline": 0.812,
  "delta": "+0.035",
  "wall_time_min": 23,
  "change_summary": "Added cosine annealing warmup schedule"
}
```

这条轨迹生成优化曲线（类似 Karpathy 的进度图），放进进度报告。人最喜欢看那条向上的曲线。

## 外循环

从单个实验退出来，做综合。

```
1. Review all results since last reflection
2. Cluster by type: what kinds of changes worked? Which didn't?
3. Ask WHY — identify the mechanism behind successes and failures
4. Update findings.md with current understanding
5. Search literature if results were surprising or assumptions need revisiting
6. Generate new hypotheses if warranted (invoke 21-research-ideation/ skills)
7. Decide direction (see criteria below)
8. Update research-state.yaml with new direction
9. Log the reflection in research-log.md
10. If there's something meaningful, generate a progress presentation
```

### 决定方向

不要随机挑，按这些标准：

**DEEPEN（深挖）**：一个被支持的结果引出了后续问题
- 效应在不同条件下还成立吗？机制是什么？
- 动作：生成子假设（H1.1、H1.2），回到内循环

**BROADEN（拓宽）**：当前结果扎实，但相邻问题未检验
- 出现了新问题。当前贡献已经清楚，还能更多。
- 动作：生成新的根假设，回到内循环

**PIVOT（转向）**：结果推翻关键假设，或出现了更有趣的东西
- 某个核心假设错了，或一个意外发现比原问题更有前景。
- 动作：带着新问题回到文献，重新 bootstrap

**CONCLUDE（收官）**：证据足以构成一项贡献
- 至少一条假设获得强支持（或一组自洽的阴性结果）
- 关键消融做完，误差分析做完
- findings.md 读起来像论文骨架：人能照着写出摘要
- 没有会改写故事的关键开放问题

注意：自洽的阴性结果也是正当贡献。"X 不奏效，因为 Y"，只要论证严谨，可以发表。

### findings.md 是你的项目记忆

这个文件身兼两职：给人看的研究叙事，以及你作为 agent 的积累知识库。每次会话、每个 /loop tick、每次 heartbeat 开始时先读它，想起自己学到过什么。

每次外循环之后，更新它以回答：

- 到目前为止我们知道什么？（Current Understanding）
- 什么模式能解释我们的结果？（Patterns and Insights）
- 学到了哪些不要再犯的具体教训？（Lessons and Constraints）
- 还有什么没解决？（Open Questions）

"Lessons and Constraints" 一节尤其重要：它记录具体可执行的教训，比如 "weight decay > 0.1 在这个规模会发散"，或 "baseline 只有 batch_size=64 才能复现"。这能防止 agent 跨会话重复失败的路径。

**质量检验**：跑完 30 个内循环实验后，一个只读 findings.md 的人应当能写出论文摘要。写不出来，说明外循环没有在做综合，只是在记流水账。

## Agent 续跑（强制，最先设置）

**做任何事之前**，先搭好墙钟循环。它让研究持续运转，没有它 agent 跑一个周期就停。

### Claude Code

**第一个动作，立即运行：**

```
/loop 20m Continue autoresearch. Read research-state.yaml and findings.md. Re-read the autoresearch SKILL.md occasionally to stay aligned. Step back and reflect holistically — is the research making real progress? Are you deepening understanding or just running experiments? If stalling, pivot or search literature for new ideas. Keep making research progress — never idle, never stop. Update findings.md, research-log.md, and research-state.yaml when there's new progress. Git commit periodically and clean up the repo if needed. Show the human your research progress with key plots and findings by preparing a report in to_human/ and opening the HTML/PDF. Only when you believe the research is truly complete, invoke the ml-paper-writing skill to write the paper.
```

它每 20 分钟触发一次，无论当时在干什么。它是维持工作节奏的心跳，不是研究阶段的分界。上一件事没做完就继续做。

### OpenClaw

**第一个动作：在当前会话里建一个 20 分钟的 cron 任务，必须先于任何研究工作。**

用 `cron.add` 工具创建绑定到本聊天会话的循环任务：

```json
{
  "name": "autoresearch-loop",
  "schedule": { "kind": "every", "everyMs": 1200000 },
  "sessionTarget": "current",
  "payload": {
    "kind": "agentTurn",
    "message": "Continue autoresearch. Read research-state.yaml and findings.md. Re-read the autoresearch SKILL.md occasionally to stay aligned. Step back and reflect holistically — is the research making real progress? Are you deepening understanding or just running experiments? If stalling, pivot or search literature for new ideas. Keep making research progress — never idle, never stop. Update findings.md, research-log.md, and research-state.yaml when there's new progress. Git commit periodically and clean up the repo if needed. Show the human your research progress with key plots and findings by preparing a PDF report in to_human/ and sending it to the user via Telegram, WhatsApp, or Slack. When you get an exciting result or interesting plot, text it to the user right away — don't wait for a full report. Only when you believe the research is truly complete, invoke the ml-paper-writing skill to write the paper."
  }
}
```

关键细节：
- `sessionTarget: "current"` 把 cron 绑到本聊天会话，跨 tick 保留对话上下文
- `everyMs: 1200000` 即 20 分钟
- 创建后用 `cron.list` 验证任务存在且启用
- cron 在实验中途触发时继续做手头的事就好，tick 是提示，不是重启

### 循环做什么

`/loop` 和 cron 任务纯粹是**墙钟节奏**，与研究循环（内/外）完全无关。每个 tick：

1. 读 `research-state.yaml` 和 `findings.md`，想起自己在哪
2. 检查有没有坏掉的东西（失败的实验、停滞的训练、报错）
3. 一切正常就继续手头的工作
4. 卡住或出问题就退一步：诊断、修复、继续
5. 绝不空转，永远在推进

## 进度汇报

有值得分享的东西时，做一份研究报告：不是状态仪表盘，是一个有吸引力的故事。

**何时汇报**（自行判断）：
- 一次外循环发现了重要模式之后
- 优化轨迹出现明显进展时（附上曲线图！）
- 方向转变之后
- 请求人对某决策给意见之前
- 收官时

**汇报什么**（按有吸引力的部分取舍）：
- 研究问题及其重要性
- 关键结果与可视化（图、指标表）
- 优化轨迹图（指标随实验变化）
- 试过什么、为什么（有取舍，不求全）
- 当前理解（findings 的叙事）
- 下一步计划

Claude Code：生成 HTML 并 `open`。HTML 打不开或渲染失败就转 PDF 兜底（用 `weasyprint`、`playwright pdf` 或 `wkhtmltopdf`）。OpenClaw：直接生成 PDF。

模板脚手架与优化曲线的做法见 [references/progress-reporting.md](references/progress-reporting.md)。模板只是起点，展示什么由你发挥。

## Git 规约

在自然的研究节点提交：

| 时机 | 提交信息格式 |
|---|---|
| 工作区初始化 | `research(init): {project} — {question}` |
| 实验协议锁定 | `research(protocol): {hypothesis}` |
| 重要结果 | `research(results): {hypothesis} — {outcome}` |
| 外循环方向变更 | `research(reflect): {direction} — {reason}` |
| 论文草稿完成 | `research(paper): {title}` |

**硬规则**：协议 commit 必须先于结果 commit，绝不合并。git 历史就是你的轻量预注册，它证明你在看到结果之前就有了这个计划。不必每个实验都提交，有实质进展时提交。

## 收官：写论文

外循环决定 CONCLUDE 时：

1. 确认 findings.md 有一条清晰、有支撑的叙事
2. 精读 2-3 篇顶会相关论文，学习它们的格式、文风与章节结构
3. 调用 `20-ml-paper-writing` Skill，它有 NeurIPS、ICML、ICLR、ACL、AAAI、COLM 及系统方向会议的 LaTeX 模板
4. 把积累的文献、实验结果和 findings 喂给它
5. 走它的引用校验流程，绝不编造参考文献
6. 生成最终的综合研究报告

写作过程自主推进。ml-paper-writing Skill 若提示人工协作点，灵活变通继续走，拿出最好的草稿。人会审阅并给反馈。

## 研究纪律

持续执行的原则，不绑定任何阶段：

- **先锁后跑**：执行之前先把实验协议 commit 到 git，证明计划先于结果存在。协议与结果绝不并成一个 commit。
- **验证性 vs 探索性**：与锁定协议相符的结果是验证性的，其余都是探索性的，有意思但要多一分怀疑。
- **阴性结果也是进展**：被否证的假设告诉你一些东西。记下它排除了什么、提示了什么，不要当成失败。
- **分析前先做完整性检查**：确认训练收敛、基线复现、数据正确，再相信主指标。
- **困惑时回到文献**：不要猜，去搜。结果意外或假设破裂就去找论文。发现用 Exa MCP，精确查 ML/AI 论文用 Semantic Scholar，预印本用 arXiv。
- **绝不停止**：例行决策不等人批准。Skill 或工具提示协作时就地变通继续，自主找出最好的前进路径。人看得到你的进度报告，需要时会纠偏。
- **有什么算力用什么**：适应用户环境：本地 GPU、集群作业、云实例，或纯 CPU。没有 GPU 就用 CPU 并相应缩小实验规模，不要卡在算力上。

## 质量标准

**好的 agent 行为：**
- 假设带机制推理（"X 因为 Y，预测 Z"），不是一句"试试 X"
- findings.md 构建连贯叙事，不是结果的平铺列表
- 阴性结果连同它排除的东西一起记录
- 实验与预期相悖时 agent 更新自己的认知模型
- 进度报告用有说服力的可视化讲一个研究故事

**坏的 agent 行为：**
- 纯超参扫描，不做解释
- findings.md 只是实验日志的复制粘贴
- 失败之后从不重新审视自己的假设
- 只优化指标，不理解改动为什么有效

## 何时用它，何时用替代

**用 autoresearch，当：**
- 有一个可通过实验探索的研究问题
- 内循环优化有可度量的代理指标
- 真正的贡献需要超越指标的综合
- 想要连续自主的研究运行

**改用单个领域 Skill，当：**
- 只是一次性任务（训个模型、跑个评测、写篇论文）
- 不需要迭代实验

## 常见问题

**内循环停滞（指标无改善）**
跑一次外循环。指标选对了吗？搜索空间耗尽了吗？考虑 BROADEN 或 PIVOT。检索文献找新思路。

**卡住没有进展**
不要继续随机乱试。退一步：检索相关文献、调用 `21-research-ideation/` 头脑风暴 Skill，或跑一次外循环反思。卡住意味着你需要新信息或新视角，不是更多实验。

**结果与基线预期矛盾**
调查它，不要无视。回到文献：你的协议可能有错，已发表的基线可能不对，或实验条件不同。把学到的东西写进 findings.md。

**agent 在 tick 之间丢失上下文**
确保每个动作之后都更新 research-state.yaml 和 findings.md。这两个文件就是你的跨会话记忆。

**找不到相关论文**
按顺序多试：Exa MCP 广搜、Semantic Scholar 精确查 ML/AI 论文（`pip install semanticscholar`）、arXiv 查预印本（`pip install arxiv`）。完整 API 代码见 `20-ml-paper-writing` Skill 的 `references/citation-workflow.md`。注意：Google Scholar 没有官方 API，程序化检索用 Semantic Scholar。

**没有 GPU**
用 CPU 并缩小实验规模。很多研究任务（分析、可解释性、小模型训练）在 CPU 上跑得很好。调整实验设计去适配可用算力，而不是卡住不动。

**实验时间超过 /loop 间隔**
正常。下一个 tick 检查是否完成。没完成就继续等，或做点别的有用的事（更新笔记、查论文）。必要时调整间隔。

**不确定何时收官**
三个问题：有没有一条获得强支持的发现？能解释它*为什么*有效吗？findings.md 能撑起一段让人信服的论文摘要吗？三个都是：收官。

## 进阶主题

- **续跑细节**：[references/agent-continuity.md](references/agent-continuity.md)
- **进度报告模板**：[references/progress-reporting.md](references/progress-reporting.md)
- **完整 Skill 路由**：[references/skill-routing.md](references/skill-routing.md)
