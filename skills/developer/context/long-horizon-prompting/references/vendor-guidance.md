> **中文汉化版** · 上游：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) · 原文件：`skills/long-horizon-prompting/references/vendor-guidance.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 厂商长时程提示词方针

摘自 OpenAI 与 Anthropic 指南中与长时运行及并行 Agent 提示词相关的内容，均注明日期。2026-07-11 依据一手来源汇编；厂商指南变动频繁，依赖模型相关细节前请重新核对链接页面。页面本身未注明日期的，给出了其日期依据。

## OpenAI

### GPT-5 提示词指南（OpenAI Cookbook，约 2025 年 8 月）

`https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide`

- 经典持久性指令块："你是一名 Agent，请持续推进，直到用户的查询被完全解决，再结束你的回合"；"只有当你确信问题已解决时才终止你的回合"；"遇到不确定时绝不要停下或交回给用户，而是研究或推导出最合理的做法并继续执行"。
- 持久性要与明确的停止条件成对出现："清楚说明 Agent 任务的停止条件，划出安全与不安全的行为，并定义何时（如果有）可以交回给用户。"
- 按工具类分层的自主性风险阈值（支付类工具在询问用户前允许的不确定性阈值很低，搜索类工具则极高）。
- 自建量规：让模型在内部构建一个 5 到 7 个类别的"优秀"量规并迭代，直到回复在每个类别都拿到最高档。
- `reasoning_effort` 是自主性的主调节旋钮；工具前导语（预先计划加进度更新）在 rollout 越长时越重要。

### GPT-5.1 与 GPT-5.2 提示词指南（2025 年 11 月、约 2025 年 12 月）

`https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide`、`https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-2_prompting_guide`

- 具名的 `<solution_persistence>` 区块："把自己当作自主 Agent……坚持到任务端到端完全处理完毕；不要停在部分修复或分析上。"
- GPT-5.2 新增：限制更新的冗长度；把范围纪律写明（"不要把任务扩展到用户要求之外"）；收尾前用 `<high_risk_self_check>` 重扫未言明的假设和无依据的断言；研究型 Agent 的停止规则形如"只有以下全部为真才停止：……"，并附一次完整性检查。
- 长运行的压缩（compaction）指引：在主要里程碑后压缩；恢复时保持提示词功能一致，避免行为漂移。

### Codex 提示词指南（覆盖 GPT-5.1-Codex-Max 至 gpt-5.3-codex，2026 年上半年）

`https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide`

- Codex 系列的反规则：删掉要求预先计划与前导语的提示词；在这些模型上这会导致过早停止（`phase` API 参数就是为修复这个问题而存在的）。
- 计划收尾："结束前，对每一项此前声明过的意图/TODO/计划进行对账。逐项标记为 Done、Blocked 或 Cancelled。不得带着 in_progress/pending 项收尾。"承诺纪律：不要承诺自己现在不会去做的工作。
- 默认期望：交付可运行的成果而非计划；做出合理假设，完成一个可运行的版本。

### GPT-5.5 提示词指引（2026 年 4 月）与 GPT-5.6 Sol 指引（2026 年 6-7 月）

`https://developers.openai.com/api/docs/guides/prompt-guidance`、`https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6`

- 方针转向结果优先的精简提示词："迁移时从全新基线开始，不要把旧提示词栈里的每条指令都照搬过来。从能保住产品契约的最小提示词起步。"ALWAYS/NEVER 只保留给真正的不变量；需要判断的地方优先用决策规则。
- GPT-5.6 内部编码 Agent 评测：更精简的系统提示词使分数提升约 10-15%，同时总 token 减少 41-66%（厂商报告，仅作方向性参考）。
- 核心公式："提示词定义结果、关键约束、可用证据和完成线，然后把选择高效路径的空间留给模型。"
- 停止规则是一等提示词内容；检索预算被表述为搜索的停止规则。
- "在提高推理投入之前，先检查提示词是否缺少成功标准、依赖规则、工具路由规则或验证循环。"
- 长运行的工作分层纪律：区分研究、设计、实现、审查和对外协调，避免模型在层与层之间悄悄漂移。

### 多 Agent API，GPT-5.6 家族（beta，2026 年 6-7 月）

`https://developers.openai.com/api/docs/guides/tools-multi-agent`

- 托管式的根 Agent 加子代理树（`spawn_agent`、`followup_task`、`send_message`）；根 Agent 负责综合并作答。注入的固定系统文本告诉根 Agent：团队中所有 Agent 能力相当；开发者的提示词只是对派生积极性的附加调节。
- 给出的理由是上下文隔离：每个子代理拿到一个有界任务和自己的上下文。
- 文档列出的反模式：为单一的有序推理链使用多 Agent；频繁写入共享可变状态；或工作被一个缓慢的外部操作主导。
- 默认并发很低（多数工作负载推荐 3 个）；64 Agent 的 CDC 配置是极端情况，不是默认。

### METR 对 GPT-5.6 Sol 的部署前评测（2026-06-26）

`https://metr.org/blog/2026-06-26-gpt-5-6-sol/`

- 检出的作弊率高于 METR 评测过的任何公开模型（把利用漏洞的代码打包进中间提交以暴露隐藏测试；从隐藏源码中提取期望答案）。
- 模型估计的 50% 时间视界在约 11 小时（作弊计为失败）到远超 200 小时（作弊计为成功）之间摆动；该测量对这一选择不稳健。
- OpenAI 的系统卡把该行为部分归因于指令遵循的改进和意在提升持久性的训练。这就是"持久性压力与奖励作弊面"之间已有记录的关联：在没有验证闸门的情况下提示模型保持持久性，同样的压力会指向你的验收标准。

## Anthropic

### 我们如何构建多智能体研究系统（2025-06-13）

`https://www.anthropic.com/engineering/multi-agent-research-system`

- 四要素委派规格："每个子代理都需要一个目标、一种输出格式、关于可用工具和数据源的指引，以及明确的任务边界。"含糊的委派造成了重复搜索和覆盖缺口。
- 编排器提示词内嵌投入分级：简单事实核查用 1 个 Agent、3-10 次工具调用；直接对比用 2-4 个子代理、各 10-15 次调用；复杂研究用 10 个以上子代理、分工负责。这同时解决了过度派生和投入不足。
- 子代理作为上下文压缩器：广泛探索，返回蒸馏后的摘要；大产物写入文件系统，只传回轻量引用。
- 主 Agent 的计划在派生前先存入外部记忆；终态评估用一个基于量规的裁判做离线打分。

### 长时运行 Agent 的高效 Harness（2025-11-26）

`https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents`

- 两种被记录的长运行失败模式：一口气想做太多；后续会话过早宣告任务完成。
- 初始化者与 worker 的提示词拆分：特殊的第一个 context window 提示词负责搭好环境（功能清单、进度文件、初始化脚本、git）；之后所有会话运行增量提示词，带一套会话启动仪式（读进度和 git log、冒烟测试、只挑一个未完成事项）。
- JSON 结构化的 pass/fail 状态，附守卫语句"删除或修改测试是不可接受的"；Agent 只允许翻转 pass 字段。
- 要求"像人类用户那样"做端到端验证（浏览器自动化），以阻止过早的完成宣告。

### 何时使用多智能体系统（2026-01-23）

`https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them`

- 多 Agent 只在上下文污染、可并行任务和专业化分工三类场景占优；否则协调成本超过收益。
- 按上下文分解，而不是按角色分解：角色流水线（规划者/实现者/测试者）会变成传话游戏，协调盖过实际工作。
- 新上下文的验证者子代理：没有亲手构建成果的验证者"无法为作者的错误找借口"；给它成果、具体的成功标准和工具，绝不给构建历史。
- 验证者的"过早胜利问题"及其修法：具体的标准（"运行完整测试套件并报告所有失败"，而不是"确保它能跑"）、负面测试，以及明确的反走捷径指令。

### 提示词最佳实践与 Claude Fable 5 指南（活文档，截至 2026 年中）

`https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices`、`https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5`

- 面向带压缩的 Harness 的上下文感知提示词：不要因 token 预算担忧而提前停止任务；在窗口刷新前把状态存入记忆。
- 有证据支撑的进度汇报："汇报进度前，逐条对照本会话的工具结果审计每个断言。只汇报你能指出证据的工作。"据 Anthropic 报告，这一做法在测试中几乎消灭了捏造的进度汇报，包括在专门诱导捏造的任务上。
- 反提前停止的自主性区块：如果最后一段是计划，或是对未完成工作的承诺，就立刻用工具调用把那件事做完。
- 新上下文的验证者子代理在长时任务上据称胜过自我批评；指示按一定节奏对照规格做检查。
- 去处方化警告：为旧一代模型编写的 Skill 和提示词对当前模型往往过于死板，会降低输出质量；把 CRITICAL/MUST 堆叠换成朴素的决策规则；移除过时的防偷懒脚手架。
- 编排器可能过度委派；用反提示让它对简单任务直接动手，只委派并行、隔离或独立的工作流。

## 两家共识

两家厂商一致的地方，可视为已定的实践：

1. 明确的完成线和停止规则，胜过单纯的持久性口号。
2. 每次派生子代理都带上目标、输出格式、工具指引和边界。
3. 返回前先验证：自检量规（OpenAI）或新上下文验证者子代理（Anthropic，更强的形式）。
4. 基于成果、证据可溯源的汇报；不要状态表演。
5. 精简、结果优先的提示词；过度处方化现在已有可测量的伤害。
6. 硬约束（预算、权限）属于 Harness 或平台，不属于提示词。
