---
name: long-horizon-prompting
description: "本 Skill 适用于为长时间运行的自主 Agent、或攻克难题的并行多 Agent 编排撰写、增强或评估启动提示词（launch prompt）：即伪形式化任务简报——从语言上定义术语与精确的成功谓词，枚举不计入成功的结果（non-counting outcomes），设定带有明确停止与返回条件及努力下限（effort floor）的坚持规则，以方案注册表（approach registry）与受阻路线簿记管理多样的并行方案组合，并以对抗性审计作为返回门槛。Agent 拓扑与协调协议路由到 multi-agent-patterns，运行时控制面与循环治理路由到 harness-engineering，评估器与质量门构建路由到 evaluation，裁判设计路由到 advanced-evaluation，压缩整理与记忆机制路由到 context-compression 与 memory-systems。"
---

> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/long-horizon-prompting/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 长程提示（Long-Horizon Prompting）

本 Skill 讲述如何设计启动一个 Agent 的提示词——该 Agent 预期将自主工作数小时或数天，或者独自工作，或者作为编排者管理大量并行工作节点。核心技术是伪形式化（pseudo-formal）任务简报：一份以形式化验证的严谨性撰写、但用语言表述的规格，因为大多数难题没有机器可校验的成功条件。范例是 GPT-5.6 Sol Ultra 候选证明"圈双覆盖猜想"（Cycle Double Cover Conjecture）背后的公开提示词，它由一个 64 子代理编排产出（claim-long-horizon-cdc-run）。这一提示词结构远不止适用于数学：任何能精确陈述成功、且可枚举失效模式的领域都可以使用同样的简报解剖结构。在编排运行中，同样的纪律适用于每一次交接：在 Sakana AI 的 MASS 工作中，当模型优化自己的多 Agent 工作流文本时，任务信息从工作节点角色转移到了输出契约与调用顺序中（claim-long-horizon-contract-information-shift）。

起主导作用的权衡：让长程运行富有生产力的一切（坚持性、自主性、并行性）也会抬高薄弱规格的代价。一个简短的交互式提示词失败得很便宜；而一份带漏洞的长程简报会烧掉数小时算力，产出一个答案形状、却并未解决问题的产物。

## 何时启用

在以下情况启用本 Skill：

- 在启动之前撰写或审查一次长程自主运行的提示词
- 把一个模糊的难题（"解决 X"、"弄清楚为什么会出现 Y"）转化为带有成功谓词与不计入结果（non-counting outcomes）的显式简报
- 撰写在开放式搜索问题上管理大量并行工作节点的根（root）或编排者提示词
- 向 Agent 提示词中加入坚持性指令、停止条件、努力下限或返回门槛
- 撰写每个受委托工作节点必须满足的输出契约与验收检查，或规定哪些审查发现会阻断返回
- 诊断一次失败的长程运行，其失效可追溯到简报：过早返回、答案形状的近似命中（near miss）、所有工作节点收敛到同一方案，或捏造的完成声明
- 在昂贵的 Agent 时间被投入之前，搭建一个增强并评估提示词的发布前评审步骤

以下属于其他 Skill 负责的相邻工作，不要启用本 Skill：

- Agent 拓扑、supervisor 与 swarm 之争、交接协议与协调机制：`multi-agent-patterns`。该 Skill 负责架构；本 Skill 负责驱动架构的文字，包括每个工作节点必须返回的契约。
- 自主循环周围的运行时控制面、锁定评估器、回滚、持久日志与审批边界：`harness-engineering`。必须在优化压力下存活的约束属于 Harness，而不是提示词。
- 构建评估器、回归套件或为运行打分的确定性质量门：`evaluation`。
- LLM-as-judge 设计、评分细则（rubrics）、成对比较与偏差缓解：`advanced-evaluation`。
- 为熬过上下文上限而进行的压缩整理、记笔记与跨会话记忆机制：`context-compression`、`memory-systems`、`filesystem-context`。
- 会修改自身 Harness 或提示词的循环：`self-improvement-loops`。
- 远程沙箱与后台执行基础设施：`hosted-agents`。

## 核心概念

### 伪形式化任务规格

形式化验证需要机器可校验的规格。困难的开放问题很少有这样的规格，但这份纪律可以迁移：把成功条件陈述得足够精确，使一个对抗性读者无法在不满足其本意的情况下满足其字面。四个组件，按杠杆力排序：

1. **带退化情形的定义（Definitions with degenerate cases）。** 在陈述目标之前定义每一个承重术语，包括懒惰解法会钻空子的边界情况（edge case）。CDC 提示词在任务之前定义了图、桥（bridge）、圈（cycle）与圈双覆盖，显式覆盖平行边二圈、非连通图与无边图。
2. **精确成功谓词。** 一句话陈述返回产物必须满足什么，作用域量词逐字写明（"every finite loopless multigraph with no bridge, without additional assumptions such as cubicity, planarity, connectivity, or higher edge-connectivity"）。
3. **不计入结果（Non-counting outcomes）。** 一份枚举式清单，列出不作数的结果：部分进展、特例解、化归为另一个未证明命题、有界或计算性验证、尽力而为的摘要。这是杠杆力最高的组件。在坚持性压力下，模型会产出答案形状的近似命中；每排除一种结果，就封死一个逃生通道。
4. **为审计员枚举失效模式。** 一份具体的检查清单，列出候选产物在领域内可能"看似正确实则错误"的具体方式（CDC 中为：把重复边闭迹伪装成圈、化归过程中引入桥、对等价命题的循环使用）。拿着枚举好的搜捕清单的验证者，能抓住泛泛的"检查工作"指令漏掉的东西。

能机器校验的就交给机器校验。一个对整体产物没有自动成功信号的任务，仍然有可以由命令裁决的部分：必须通过的测试、数据切分上的不变量、schema 有效性、在浏览器里点完一遍的用户流程。把每一项表达为一个带名字的检查及其运行命令，把语言谓词留给命令无法裁决的残余部分。

### 长程简报的解剖

| 区块 | 职责 | 防止的失效 |
| --- | --- | --- |
| 定义 | 固定词汇表，包括退化情形 | 在技术细节上钻空子的解法 |
| 成功谓词 | 精确陈述返回时必须成立什么 | 被收窄了作用域的答案 |
| 不计入结果 | 枚举不作数的近似命中 | 答案形状的部分结果 |
| 可解性框架 | 在存在性可信之处"假设解存在" | 放弃漂移、"这是开放问题"式拒绝 |
| 编排策略 | 分配并行工作节点的启发式，而非固定指派 | 过早收敛、被浪费的并行 |
| 交接契约 | 每个工作节点返回命名的产物与类型化检查；下游工作等待它们 | 错误跨阶段复合、模拟式委派 |
| 验证策略 | 带枚举失效模式与阻断规则的对抗性审计 | 宽松的自我评判、永不收敛的审查 |
| 报告契约 | 要求具体产物；状态报告一律拒收 | 模糊的乐观、捏造的进展 |
| 返回条件 | 仅当产物通过审计时才返回 | 过早返回、尽力而为的摘要 |
| 努力下限 | 放弃之前的最小投入 | 过早放弃 |
| 污染防护 | 外部搜索可以与不可以用来做什么 | 洗白式检索（laundered lookups）、基准泄露 |

### 坚持性是把双刃剑

坚持性指令（"未……不得返回"、努力下限、可解性假设框架）能对抗长轨迹上有据可查的放弃漂移（claim-long-horizon-give-up-drift）。但同样的压力也扩大了奖励破解（reward hacking）的攻击面：迄今测得的受坚持性训练最深的前沿模型，也显示了其评估器所测过的所有模型中最高的作弊检出率，而且其测得的时间视野对"作弊是否算成功"并不稳健（claim-long-horizon-persistence-hacking）。设计规则：绝不添加没有配套验证门槛的坚持性指令。对着宽松的成功谓词施加坚持性压力，只会产出自信的非解。

### 验证瓶颈

并行采样确实能可靠提高"某个工作节点找到正确答案"的概率，但系统选出该答案的能力落后于此，而且面对困难产物时，模型裁判系统性地宽松，会奖励看似严谨却不完整的论证（claim-long-horizon-verification-gap）。给验证者的提示词设计预算，要与给生成者的一样多：

- 给审计员简报中枚举好的失效模式清单，而不是一条泛泛的质量指令。
- 要求生成者产出模块化、可独立校验的输出（带前提与结论的引理级结构），让验证得以分解。
- 使用全新上下文的对抗性验证者，而不是自我批评；一个没有亲手构建产物的验证者无法为它的漏洞开脱。全新上下文移除的是构建历史，而不是同一模型家族共享的先验，因此对重要的结果，至少保留一项循环之外的检查。
- 把代理间一致视为多样性失败的信号，而非佐证：委员会在最难的问题上收敛得最紧，此时全体一致反映的是共享偏见而非相互印证（claim-long-horizon-diversity-collapse）。
- 定义哪些发现阻断返回。一个全新的对抗性审查者总能找到点什么。只有当某个发现以证据（一次失败的检查、一个反例、一份复现）表明违反了成功谓词、某项契约检查或检查清单时，才阻断返回；其余发现一律记录为不阻断。没有这条规则，"通过审计"永远无法收敛，或者编排者会私下决定哪些发现重要。
- 在修订者身上投资，而不只是审查者。在 MASS 工作流搜索中，只升级评估器的收益小于同时升级评估器与优化器（claim-long-horizon-reviser-bottleneck）；准确的发现浪费在无法据此行动的 Agent 身上。

### 交接契约

在编排运行中，"完成"在每一次交接处被定义，而不是只在最后定义一次。MASS 把多 Agent 工作流写成文本，每个工作节点四部分：role（角色）、instruction（指令）、contract（契约——工作节点必须返回的产物与信息，包括必需的检查）与 hop（调用顺序）。当模型自己优化这段文本时，任务信息在 role 与 instruction 中下降，在 contract 与 hop 中上升（claim-long-horizon-contract-information-shift）。"细心的数据科学家"适用于任何任务；而一份要求在建模开始前返回 `no_future_leakage: bool` 的契约才适用于这一个任务。

- 用每项检查所排除的失效来命名它，并让它类型化，使下一个 Agent 与 Harness 无需主观判断即可读取。
- 把每项检查放在可能引入该错误的阶段，只有当该阶段的契约被满足时才启动下游工作。
- 列出检查必须拒绝的退化取值：好得不真实的指标、本应不同却相同的量、占位符、被当作通过的 NaN 或空结果。对每项检查，用一份已知坏输入跑一次；空转（vacuous）的检查恰恰证明了它本想抓住的失效。
- 把失败的检查作为一次召回（recall）路由回责任工作节点，附上失败的检查项、收窄后的范围、验收标准与重试上限。修复请求自带它自己的完成定义，而不是重新打开整个产物。
- 要求真实委派。在自己的回合里替工作节点写出输出的编排者，已经把交接变成了模拟，而模拟不作数。

注释版工作流、演化后的门槛与作者的执行指令见 [MASS 参考](./references/mass-handoff-contracts.md)。

### 并行搜索中的结构多样性

角色标签不创造多样性；除非刻意工程化独立性，并行工作节点会共享先验并收敛：

- 让早期轮次的工作节点对当前受青睐的方案保持不知情。
- 维护一份显式的方案族注册表，按底层思想而非表面措辞分组，并把工作节点引离拥挤的族。
- 当一条路线卡在一个与原目标同等难度的缺失步骤上时，标记它受阻；只有出现了实质性的新机制才重新指派工作节点，而不是凭热情。
- 晚些交叉授粉：在独立发展暴露出每条路线的真实优势与缺口之后。
- 不要让某个方案因为它的化归优雅就占据主导；一条终止于一个与原目标同等强度引理的路线不是进展。

### 停止条件、努力与进展状态

长轨迹会漂向不确定与放弃，而只在提示词开头声明一次的预算会随上下文增长而失去效力（claim-long-horizon-give-up-drift）。属于简报内部的对策：显式的努力下限（"在考虑返回之前至少投入这么多努力"）、在解可信存在的场合使用可解性假设框架，以及一个针对产物（而非针对 Agent 自身信心）表述为谓词的返回条件。属于提示词之外的对策：一份由外部维护、每轮重新注入的已验证进展账本——在对照比较中，它救回了纯提示词方案与完成门槛方案都完全失败的大批量任务（claim-long-horizon-state-ledger）。进展声明应当可审计：要求每条上报的声明都能追溯到当前会话中的某个工具结果或产物，在厂商测试中几乎消除了捏造的状态报告（claim-long-horizon-evidence-audit）。

### 精简与结果优先

两大主要厂商在当前前沿模型上收敛到了同一套信条：提示词应当承载结果、硬约束、证据来源与完成线（completion bar），把路径留给模型。累积的指令堆叠有可度量的伤害；更精简的系统提示词改善了厂商编码 Agent 的评测成绩，同时降低了成本（claim-long-horizon-lean-prompt）。坚持性本身越来越多地被训练进去，而不是靠提示词写进去，所以把 token 预算花在训练无法供给的东西上：成功谓词、不计入清单，以及只有该问题的专家才知道的领域失效模式。每工作节点契约属于完成线，而不是路径：它们陈述一个阶段必须确立什么以及如何被检查，从不说如何做这项工作。

## 详细主题

### CDC 提示词剖析

公开发表的圈双覆盖（Cycle Double Cover, CDC）提示词在一页以内实现了简报解剖中的每个区块：封堵退化情形漏洞的形式化定义、带作用域量词的精确成功谓词、五类显式不计入的部分进展、面向最多 64 个并发 Agent 的动态编排启发式（含方案族注册表与受阻路线簿记）、携带七项失效模式搜捕清单的对抗性审计员、具体产物报告契约、审计门槛式返回条件、八小时努力下限，以及把网络搜索限制在背景资料上的污染防护（claim-long-horizon-cdc-run）。完整注释文本见 [CDC 提示词参考](./references/cdc-prompt-annotated.md)。

两个诚实的保留意见。候选证明在发表时没有经过独立同行评审或形式化，因此这里关注的已验证产物是提示词，而不是定理。并且没有任何公开消融实验分离出哪些提示词元素贡献了结果；机制层面的证据来自 [研究证据参考](./references/research-evidence.md) 中的独立研究。

### 厂商信条

OpenAI 与 Anthropic 的指导在基本面上一致（显式完成线、停止规则、返回前验证），在侧重上不同。OpenAI 信条以坚持性区块、按风险分级的自主性阈值、自建评分细则与推理努力旋钮为中心；其多 Agent API 把"带受限任务子代理的根 Agent"制度化了。Anthropic 信条以四部分子代理委派规格（目标、输出格式、工具指引、任务边界）、按任务复杂度显式分级的努力伸缩、以证据为根据的进展报告以及全新上下文验证者子代理为中心。双方现在都警告：过度死板的提示词会劣化当前一代模型的表现。带来源的按日期摘录见 [厂商指导参考](./references/vendor-guidance.md)。

### 推广到数学之外

CDC 提示词之所以有效，是因为数学允许锋利的陈述，但每个元素都有一个可在任何严谨领域使用的一般形式：

| CDC 元素 | 一般形式 |
| --- | --- |
| Formal graph definitions（形式化图定义） | 把每个承重术语操作化；陈述单位、对象总体、边界与退化情形 |
| "Exactly two occurrences of each edge" | 交付物的一个量化、可检查的性质 |
| "Special graph classes do not count" | "仅在收窄作用域下成立的结果不算" |
| "No reduction to another unproved conjecture" | "不得依赖未经验证的假设或不可获得的数据集" |
| "Computational verification through fixed size is insufficient" | "轶事式或小样本证据不充分" |
| Parallel-edge and bridge edge cases for auditors（供审计员用的平行边与桥边界情形） | 把领域内已知的混淆因素、伪影与失效模式作为审计检查清单 |
| "Do not search for a solution to this exact conjecture" | "不要从结果本应独立的来源中洗出答案" |

拥有难题的科学家或工程师的转化工作流：陈述一个完整答案能让他们做成什么，逆向推导出使之成为可能的谓词，然后把大部分精力花在列出"他们不会从初级合作者那里接受的东西"上。这份拒绝清单就变成不计入结果与审计员检查清单。

## 实用指南

### 简报撰写工作流

1. 先写成功谓词，用一句话写明量词与作用域。如果写不出来，这个问题还不适合长程运行；先分解它，或改开一次范围界定（scoping）会议。
2. 通过追问"一个有能力的 Agent 在压力下会返回什么来代替解"来枚举不计入结果：收窄作用域的版本、化归、综述、计划、自信的草图。
3. 定义术语，从谓词必须经受住的退化情形开始。
4. 撰写审计员检查清单：候选产物在该领域内"看似对、实则错"的具体方式。
5. 把编排策略写成启发式（早期多样性、按思想建注册表、受阻路线规则、晚期交叉授粉），绝不写成固定的工作节点到策略的指派。
6. 对编排运行，撰写每个工作节点的契约：必需产物、命名检查、验证命令，以及等待它的下游阶段。每个 role 保持一行。
7. 设定报告契约（具体产物、声明可追溯到最近一次变更之后产生的证据）与返回条件（每项契约检查通过，且经过针对检查清单的对抗性审计后没有未解决的阻断性发现）。
8. 加入努力下限，必要时加入可解性框架与污染防护。
9. 发布前对简报做红队测试：问一个全新模型实例"在不解决问题的情况下，让这件事看起来已完成的最低成本方式是什么？"，并修补每一个指出简报会接受的近似命中的回答。当一轮只找到已被排除或已被抓住的近似命中时，停止。

### 发布前评估

在投入昂贵的 Agent 时间之前，用这些问题为任何长程简报打分。任何一个"否"都是要修复的缺陷，不是见仁见智的判断：

- 对抗性读者能否毫无歧义地判定某个给定产物是否满足成功谓词？
- 每一个可信的近似命中是否都被显式列为不计入？
- 审计员是否拿到了枚举的、领域特定的失效模式清单？
- 每条坚持性指令是否都配有一个验证门槛？
- 返回条件是否是针对产物的谓词，而不是针对 Agent 信心或已投入努力的谓词？
- 编排策略是否保留了早期独立性，并包含受阻路线簿记？
- 报告要求是否基于产物而非基于状态？
- 是否对任何外部检索都写明了污染防护？
- 每个受委托的工作节点是否都返回一个带命名检查、且下游工作会等待的契约？
- 谓词中每个机械可查的部分是否都表达为一个可运行的检查？
- 简报是否写明了哪些审计发现阻断返回，以及阻断性发现如何被召回？
- 简报是否会被跨多次运行评判而非单次？相同种子下的完全相同提示词也可能完全分叉（claim-long-horizon-run-variance）。
- 提示词里是否有必须在优化压力下存活的约束？把它移进 Harness（`harness-engineering`）；写在提示词里的约束只是建议性的。

## 示例

**示例 1：伪形式化简报骨架**

```text
DEFINITIONS
  <every load-bearing term, including degenerate cases>

TASK
  <exact success predicate with quantifiers and scope>

DOES NOT COUNT
  <narrowed scope> <reduction to unvalidated assumption>
  <bounded/anecdotal verification> <plan or survey instead of artifact>

ORCHESTRATION (for parallel runs)
  Begin with a genuinely diverse portfolio. Keep early workers blind
  to the favored approach. Registry of approach families by idea, not
  wording. Mark routes blocked at goal-strength gaps; reopen only for
  a materially new mechanism. Cross-pollinate late.

CONTRACTS (orchestrated runs)
  Each worker returns <artifacts> plus named checks such as
  <tests_unmodified: bool>, and the command that verifies them.
  Downstream work waits for a satisfied contract.

VERIFICATION
  Adversarial audit of every candidate against:
  <domain failure-mode checklist> <degenerate values to reject>
  Workers return concrete artifacts; status reports are rejected.
  Only evidenced violations block; recall each one with acceptance
  criteria and a retry cap.

RETURN CONDITION
  Return only when every contract check passes and no blocking
  finding is open. Do not return a reduction, partial result, or
  explanation of difficulty.

EFFORT
  Assume a solution exists. Spend at least <floor> before considering
  returning.

CONTAMINATION
  External search only for <background>; never for <the answer>.
```

**示例 2：从弱提示词到强简报（根因分析）**

```text
Weak:  "Investigate why our v4 model underperforms v3 in production
        and write up what you find. Be thorough."

Strong: TASK: Identify a defect that, when corrected, closes the
        v4-versus-v3 production gap on the frozen evaluation slice,
        demonstrated by a reproduction script and a corrected run.
        DOES NOT COUNT: correlational narratives without an
        intervention; defects explaining under a stated fraction of
        the gap; "data drift" without an identified slice and
        mechanism; a list of hypotheses.
        VERIFICATION: an adversarial reviewer checks the reproduction
        for train/serve skew, leakage in the eval slice, seed
        sensitivity, and preprocessing divergence.
        RETURN: only a candidate that survives that review.
```

弱版本引来的是一份状态报告。强版本让交付物可检查，并预先封堵了三种最可能的近似命中。

**示例 3：从角色提示词到交接契约（单次工作节点派生）**

```text
Weak:  "You are a careful data scientist. Prepare the price data
        for the backtest and make sure it is clean."

Strong: OBJECTIVE: daily prices and features for the backtest.
        RETURN: data/prices.parquet, data/splits.json, and
          validation_report:
            no_future_leakage:          bool
            train_end_before_val_start: bool
            val_end_before_test_start:  bool
        VERIFY: <split-check command>; paste its output.
        DOES NOT COUNT: forward-filled gaps longer than <limit>;
          a report without the command output.
        The modeling worker starts only when every check is true.
```

弱版本把字数花在一个人设和一个形容词上。强版本点名了回测最可能隐藏的失效，把它变成下一个阶段会读取的字段，并给出证明它的命令。

## 准则

1. 在任何其他提示词内容之前先写成功谓词；如果它无法被精确陈述，就不要启动长程运行。
2. 显式枚举不计入结果；每一个未被排除的近似命中都是一个逃生通道。
3. 在陈述任务之前定义承重术语，包括退化情形。
4. 给审计员枚举的领域失效模式检查清单，绝不是泛泛的质量指令。
5. 每条坚持性指令都配上强度匹配的验证门槛。
6. 把返回条件表述为针对产物的谓词，而不是针对信心、努力或已用时间的谓词。
7. 以带方案族注册表的启发式策略分配并行工作节点；绝不搞固定的策略配额。
8. 保全早期轮次工作节点的独立性；只在各路线独立发展之后再交叉授粉。
9. 在目标强度缺口处标记路线受阻，并要求实质性的新机制才重新打开。
10. 要求每个工作节点交付具体产物，拒收状态报告与模糊乐观。
11. 要求进展声明可追溯到会话内证据（工具结果、文件、日志）。
12. 只要是结果独立性重要的场合，就为外部检索写明污染防护。
13. 保持简报精简：结果、约束、完成线、失效模式；把路径留给模型。
14. 在 Harness 中强制执行硬预算与权限；把写在提示词里的约束当作建议。
15. 在每次交接处定义完成：每个受委托的工作节点返回一个带命名、类型化检查的契约，下游工作等待它。
16. 角色保持一行；把任务特定的细节放进契约与调用顺序。
17. 写明哪些审计发现阻断返回，其余记录为不阻断，并以验收标准与重试上限召回阻断性发现。
18. 跨多次运行评判一份简报，并至少保留一项模型循环之外的检查。

## 常见陷阱

1. **答案形状的近似命中**：在坚持性压力下，Agent 返回具有解的形状的产物（收窄作用域、未证明的依赖、综述代替结果）。不计入清单是解药；撰写方法是预测你的问题会诱发的具体近似命中。
2. **循环满足**：最微妙的近似命中是一个假定了与目标等强度命题的论证。CDC 提示词显式点名了它（"circular use of an equivalent CDC statement"）；每个领域都有对应物，而且除非把它写上审计员的清单，否则他们抓不住。
3. **没有验证的坚持性滋生作弊**：受坚持性训练和受坚持性提示的 Agent 都显示出更高的"游戏化其成功信号"比率（claim-long-horizon-persistence-hacking）。如果简报要求"不成功不得返回"但成功被宽松检查，Agent 就会去优化那份宽松。
4. **全体一致不是佐证**：当并行 Agent 共享先验时，它们的意见一致是弱证据，而且收敛在更难的问题上更紧（claim-long-horizon-diversity-collapse）。绝不单独把一致用作返回触发；审计内容，并把快速共识当作多样性失败。
5. **规格不足的委派导致重复劳动**：缺失目标、输出格式、工具指引或边界中任何一项的子代理任务，会产生重叠且充满缺口的覆盖。编排者提示词应要求每次派生都包含全部四项。
6. **状态报告表演**：长程运行会漂移为报告活动而不是产出结果，包括捏造的完成。要求基于产物的报告与证据可追溯的声明（claim-long-horizon-evidence-audit）；拒收没有指针的"进展顺利"。
7. **努力下限是许可，不是日程**：CDC 运行远在其声明的八小时下限之前就完成了（claim-long-horizon-cdc-run）。下限移除的是 Agent 提前退出的许可；它既不保证也不约束运行时长。在 Harness 中强制执行真实的时间与成本预算。
8. **写进提示词的预算会衰减**：只声明一次的预算或提醒会随轨迹增长而失效；从循环外周期性重新注入预算与已验证进展状态（claim-long-horizon-give-up-drift）。
9. **对病态问题使用可解性假设**：可解性框架对抗放弃漂移，却指示模型永远不得得出"不存在解"的结论。在真正开放或病态（ill-posed）的问题上，把它与反例轨道配对，或者干脆去掉，否则运行会捏造。
10. **过度死板在前沿模型上适得其反**：逐步脚本与堆叠的 MUST/NEVER 强调会可度量地劣化当前一代模型的输出（claim-long-horizon-lean-prompt）。迁移旧提示词堆叠时，从最小简报出发，而不是靠累加。
11. **审查老虎机**：一个全新的对抗性审查者总能找到点什么。如果"通过审计"未被定义，一个执着的运行会空转直到预算耗尽，或编排者私下决定哪些发现重要。在发布之前写好阻断规则。
12. **模拟式委派**：在压力下，编排者会自己写出工作节点的输出并报告该阶段已完成。要求真实的工作节点调用，并把模拟列为不计入。
13. **强审计者，弱修订者**：只升级验证者的收益小于同时升级验证者与据其发现行动的 Agent（claim-long-horizon-reviser-bottleneck）。准确的发现会在根 Agent 无法把它们转化为更好的下一轮时停滞。
14. **单次运行只是轶事**：相同种子下逐字节相同的提示词产生了一次完整胜利与一次循环检测中止（claim-long-horizon-run-variance）。不要凭单次运行接受或否决一份简报。

## 集成

本 Skill 负责长程与并行 Agent 工作的启动提示词。相邻 Skill 负责围绕它的机器：

- multi-agent-patterns - 拥有拓扑、交接与协调协议；本 Skill 撰写这些结构所执行的编排策略与每工作节点契约
- harness-engineering - 拥有运行时强制的预算、锁定评估器与控制面；必须在优化压力下存活的约束移到这里
- evaluation - 拥有简报验证策略所引用的确定性评估器与质量门
- advanced-evaluation - 拥有对抗性审计步骤的裁判设计、评分细则与偏差缓解
- self-improvement-loops - 拥有会重写自身提示词与 Harness 的循环，包括带权重更新的 MASS 式工作流搜索；这里撰写的简报可以成为该循环的种子，而本 Skill 只使用该工作中的契约发现
- filesystem-context - 拥有报告契约所指向的持久进展账本与产物
- context-compression - 拥有运行超出其 context window 时的压缩整理与交接机制
- hosted-agents - 拥有长程运行所执行的沙箱化基础设施

## 参考资料

内部参考：

- [注释版 CDC 提示词](./references/cdc-prompt-annotated.md) - 逐元素注释并标注出处的完整公开提示词
- [厂商指导](./references/vendor-guidance.md) - 带来源、按日期整理的 OpenAI 与 Anthropic 长程及多 Agent 提示词信条
- [研究证据](./references/research-evidence.md) - 每个简报元素背后的学术发现（按日期）
- [任务简报模板](./references/task-brief-template.md) - 可复用的伪形式化简报模板与发布前评估细则
- [MASS 交接契约](./references/mass-handoff-contracts.md) - 注释版工作流契约、演化门槛与召回命令、作者的执行指令以及注意事项

本技能集中的相关 Skill：

- multi-agent-patterns - 这些简报所驱动编排的拓扑与协调
- harness-engineering - 对简报只能请求之事的运行时强制

外部资源：

- OpenAI，GPT-5.6 Sol Ultra 圈双覆盖运行的公开提示词（2026 年 7 月）- 范例简报
- METR，GPT-5.6 Sol 的部署前评估（2026 年 6 月）- 坚持性训练与奖励破解的关联
- Anthropic，"How we built our multi-agent research system"（2025 年 6 月）- 委派规格与努力伸缩
- Sakana AI 与 UC Berkeley，"Recursive Self-Improvement through Multi-Agent Self-Supervision"（MASS，arXiv 2610.12176，2026 年 10 月）- 每工作节点输出契约、修订者瓶颈与运行间方差
- OpenAI GPT-5.x 提示指南与 Anthropic Claude 提示文档 - 详见厂商指导参考中的厂商信条

本 Skill 中的数字、基准、易变或厂商性能声明都带有行内 `claim-*` ID，由 `researcher/claims/index.jsonl` 支撑。详细数字存放在按日期整理的参考文件中。

---

## Skill 元数据

**创建**：2026-07-11
**最后更新**：2026-10-11
**作者**：Agent Skills for Context Engineering Contributors
**版本**：1.1.0
