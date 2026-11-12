---
name: research-ops-skills
description: "当企业研究请求需要路由时使用（临床研究设计、R&D 财务、市场规模测算、用户研究）：'需要多少样本量'、'R&D 预算'。列出 research-ops 的各项子 Skill 并路由到其中一项。"
context: fork
license: MIT
metadata:
  version: 2.9.0
  author: claude-code-skills
  tags: [research-ops, clinical-research, research-finance, market-research, product-research, rd, orchestrator]
  compatible_tools: [claude-code, codex-cli, cursor, antigravity, opencode, gemini-cli]
---

> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`research-ops/skills/research-ops-skills/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 研究运营：领域编排器

研究运营这一层面定义了**企业如何规划、资助、界定范围并综合研究**，覆盖四条工作流：临床 R&D、R&D 财务、市场研究与产品研究。该编排器会派生其上下文，把你的请求路由到四个子 Skill 之一，然后返回一份摘要。体量较大的输入材料（方案草案、项目台账、问卷导出、访谈逐字稿）留在派生出的上下文中。

这是学术 `research/` 领域在企业侧的对应物。如果你的问题关乎**查找**文献、资助或专利，请用 `research/`；如果关乎把研究作为一项运营纪律来**规划、资助、界定范围或综合**，那你来对地方了。

## 何时调用

| 情形 | 子 Skill |
|---|---|
| "我们正在设计 2 期试验，终点和样本量该定多少？" | `clinical-research` |
| "我们的 R&D 项目资金消耗是多少，这笔成本算 CapEx 还是 OpEx？" | `research-finance` |
| "这个产品的 TAM 有多大，我们该如何对该细分做调研？" | `market-research` |
| "我们要访谈多少用户，又该如何综合这些发现？" | `product-research` |

## 路由逻辑（确定性）

沿用与 `commercial-skills` 相同的双信号阈值模式。单一信号 → 提出澄清问题；混合信号 → 先置信度最高的一条，第二条在后续轮次链式处理。绝不静默链式处理。

### 信号表

| 信号类别 | 关键词 | 子 Skill |
|---|---|---|
| **CLINICAL** | 临床试验、研究设计、方案、终点、样本量、检验效能、1/2/3 期、生物统计、入组资格、可行性、估计目标 | `clinical-research` |
| **RD_FINANCE** | R&D 预算、项目预算、资金消耗、资金续航期、F&A、间接费率、管理费用、资本化 vs 费用化、R&D 资本支出、组合 ROI、rNPV | `research-finance` |
| **MARKET** | TAM、SAM、SOM、市场规模测算、问卷设计、抽样、误差幅度、细分、竞争情报、市场研究 | `market-research` |
| **PRODUCT** | 用户访谈、JTBD、可用性测试、概念测试、原型测试、探索性研究、研究知识库、洞察综合、饱和 | `product-research` |

## 工作流（Matt Pocock 的追问纪律）

沿用 Matt Pocock 的 `grill-with-docs` 模式：**先探索后提问，每轮只问一个并给出推荐答案，深度优先地走决策树，跟踪依赖关系，把每一处质疑都锚定到研究准则**（各子 Skill 的 `references/`）。

### 第 1 步：先探索后提问

先检查用户的工作目录：
- 工作区里是否已经有方案草案、项目台账、TAM 模型或访谈提纲？
- 请求是否已经明确了所属条线（例如"双臂试验需要多少样本量"即对应 `clinical-research`，无需再问）？
- 是否有某个产物文件名就能确定条线（`protocol.json` → 临床；`program-budget.json` → 财务；`tam-model.json` → 市场；`interview-guide.md` → 产品）？

如果工作区已能确定条线，就**静默路由**。

### 第 2 步：仍不明确时，只提一个带推荐答案的强制性问题

Matt 的规矩：绝不把多个问题捆在一起，始终给出推荐答案。

模式：

```
Q1/1: [precise question naming the two candidate lanes]
Recommended: [Lane X, because <signal-table rationale>]

(Confirm, or override?)
```


### 第 3 步：跨条线请求的决策树走查

如果请求确实跨越两条线（例如"设计这个试验并为它做预算" = CLINICAL + RD_FINANCE），就按深度优先推进：

1. 置信度最高的条线优先 → 在派生上下文中运行子 Skill → 生成摘要
2. 询问："现在运行 [second lane] 吗？推荐：是，因为 [dependency]。"
3. 链式处理前先确认。

绝不静默链式处理。

### 第 4 步：在派生上下文中调用子 Skill

转发原始提示词 + 结构化输入（方案 JSON、项目台账 CSV、市场模型、观察记录导出）。

### 第 5 步：返回带准则引证与质疑的摘要

≤ 200 词：已分析内容、前 3 条发现（锚定到准则引证）、前 3 项后续行动（适用时指明具名的人工负责人）、产物路径，以及给用户的**一处追问式质疑**。示例：

- "你的检验效能计算假设效应量为 0.5，却没有已发表的依据。ICH E9 要求给出经过论证、具临床意义的差异。0.5 从何而来？"
- "你的 TAM 只是一个自上而下的数字（占 $40B 市场的 1%）。Bessemer 的市场规模测算纪律要求做一次自下而上的交叉核验。单位数 × 单价 × 采用率分别是多少？"

## 强制性问题库（grill-with-docs 模式）

在调用子 Skill 之前，就决定条线归属的关键决策对用户追问。每轮只问一个，附带推荐答案与准则引证：

- **CLINICAL 线**："你的主要终点是临床结局还是替代终点，若为替代终点，是否已针对该适应证完成验证？推荐：除非该替代终点列在 FDA 的已验证清单中，否则选临床结局。准则：FDA Surrogate Endpoint Table；BEST glossary。"
- **RD_FINANCE 线**："这笔支出属于研究阶段还是开发阶段，你能否举证技术可行性？推荐：研究 = 费用化；开发 = 仅在有可行性证据时作为资本化候选，并转交给具名的财务负责人。准则：IAS 38；ASC 730。"
- **MARKET 线**："你的 TAM 是自上而下还是自下而上，是否已两种方式都算过以做三角验证？推荐：两者都算，并对差异做出解释。准则：Bessemer / a16z market-sizing；Fermi estimation。"
- **PRODUCT 线**："这项研究是生成性的（发现问题）还是评估性的（检验方案）？推荐：先明确类型，方法随之而定。准则：Rohrer's landscape of UX research methods (NN/g)。"

在决定条线归属的关键决策敲定之前，绝不运行子 Skill。

## 先做引导配置（按子 Skill）

在某个工作区中首次调用某个子 Skill 之前，先让用户填写该 Skill 的引导问卷，使各工具能按用户的上下文预先配置好再运行：


```bash
python3 skills/<sub-skill>/scripts/onboard.py          # interactive Q&A
python3 skills/<sub-skill>/scripts/onboard.py --show    # questions + current config
```


每个子 Skill 都有**自己专属**的问题集（临床：area/alpha/power/dropout/owners · 财务：area/F&A/runway/standard/owner · 市场：profile/confidence/MoE/method · 产品：profile/insight-threshold/method/stakes）。答案会持久化到 `~/.config/research-ops/<sub-skill>.json`（或在带 `--scope project` 时存到 `./.research-ops/<sub-skill>.json`），并由该 Skill 中的每个工具自动读取。在这里，定制是必须遵守的纪律，而非装饰；当用户开启一条全新的研究工作流时，要显式给出引导步骤。

## Autoresearch 交接（隔离、按需启用）

每个子 Skill 都自带 `skills/<sub-skill>/scripts/ar_evaluator.py`，它是通往 `engineering/autoresearch-agent` 的一条**隔离**桥梁。仅当用户明确要求 "optimize"、"improve" 或 "run a loop" 时才调用 autoresearch。交接按 Skill 各自进行（无共享耦合）：循环修改该 Skill 的输入文件，评估器对其打分（临床 → `feasibility_composite` 更高；财务 → `runway_months` 更高；市场 → `tam_divergence` 更低；产品 → `validated_insights` 更高）。绝不自动启动循环，也绝不让循环修改评估器。

## 假设

1. 用户具备研究决策权，或正在为具备该权限的人准备分析。
2. 用户要的是**确定性的决策支持**，而非最终答案：方案由临床医生批准，分录由主计长入账，市场数字由人来拍板。
3. 输入可能不完整；每个子 Skill 都附带模板样例，让用户先看清结构再填入自己的内容。

## 非目标

- 不是 EDC、临床试验管理系统、会计系统、问卷平台或研究知识库。
- 不把临床、会计或法律建议当作既定事实给出。每项输出都是**一条建议 + 一位具名的人工负责人**。
- 不跨会话存储研究历史。

## 区别于

- **`research/`（学术）**：该领域负责**查找**文献、资助与专利；本领域负责**规划、资助、界定范围并综合**研究。
- **`ra-qm-team`**：那是**法规/质量管理（QM）申报**（ISO 13485/14971、MDR、FDA 510(k)/PMA/QSR）。clinical-research 设计的是**研究**；申报工作转交 ra-qm-team。
- **`finance/financial-analysis`**：那是**公司结账 + 估值**。research-finance 管理的是 **R&D 项目/组合支出**。
- **`research/grants`**：那是**资助机会发现**。research-finance 管理的是**已到手的资金**。
- **`product-team`**：那是**画像/旅程产物、探索冲刺与在线 A/B 实验**。product-research 是**方法 + 知识库纪律**。
- **`marketing-skill`**：那是**活动分析与需求生成**。market-research 是**上游方法论**。

## 输出产物

| 子 Skill | 产物 |
|---|---|
| clinical-research | `protocol_synopsis.md` + `sample_size.json` |
| research-finance | `rd_program_budget.md` + `capex_opex_routing.json` |
| market-research | `market_sizing.md` + `sample_plan.json` |
| product-research | `research_plan.md` + `insight_synthesis.json` |

## 反模式（勿做）

- ❌ 把临床检验效能/终点输出当作事实呈现：它只是**一份估计**，且带有具名的临床负责人
- ❌ 自动判定资本化还是费用化：应转交**具名的财务负责人**
- ❌ 把市场规模当作一个没有出处的孤零数字来报告：应给出**方法 + 双向三角验证 + 假设**
- ❌ 凭单个参与者就断言一条产品洞察：应把它标注为**轶事**
- ❌ 为了"面面俱到"而把 4 个子 Skill 全跑一遍：选一个，出摘要，需要时再链式追加

## 参考资料

- 临床准则：ICH E8(R1)/E9/E9(R1)、CONSORT、SPIRIT、FDA Multiple Endpoints
- R&D 财务准则：IAS 38、ASC 730、2 CFR 200、Cooper stage-gate
- 市场准则：Cochran、Dillman、Kotler、Bessemer market-sizing
- 产品准则：Nielsen、Guest et al.、Christensen JTBD、ResearchOps/Polaris
- Path-B 构建模式：`documentation/implementation/research-ops-expansion-plan.md`
