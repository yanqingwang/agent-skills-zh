---
name: egm-review
license: Apache-2.0
disable-model-invocation: true
description: >-
  编排 EGM Goldfish Review Protocol。作为 EGM 流程的一部分，用于执行设计文档评审。执行五个评审阶段：初始拉远审视、理解评审、设计批判、中期拉远审视，以及实施就绪评审。
---

> **中文汉化版** · 上游：[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) · 原文件：`skills/egm-review/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 评审、验证与自动整改

在 Codex 或 ChatGPT Work 中运行时，先阅读 [Codex 集成](../../docs/codex.md)。
在 Claude Code 或 Cowork 中，先阅读 `${CLAUDE_PLUGIN_ROOT}/docs/claude.md`。

通过专门的评审角色对设计文档进行评审与验证。

## 委派

Goldfish 在一个全新的上下文中运行，没有任何对话历史。用你所用 Harness 的子 Agent 工具（Antigravity：`invoke_subagent`；Claude Code：`Agent`；Codex：`spawn_agent`）派生每个子 Agent。每个子 Agent 定义在 `agents/<file>.md` 中，其 frontmatter 的 `name`（例如 `egm-zoom-out`）就是在 Harness 注册具名子 Agent 时要请求的子 Agent 类型。否则派生一个通用子 Agent，并让它先读取对应的角色文件。原样传递提示词并等待报告。如果你的 Harness 无法嵌套子 Agent，改用直接派发而非综合器。参见 `docs/harnesses.md`。
如果你的 Harness 没有子 Agent 工具，停下来告诉用户：在同一上下文中的评审不是 Goldfish 评审。

## 执行约束（关键）

1.  **制品优先交付（强制）**：**严格禁止**直接在聊天窗格中给出大型提案、草稿、摘要或计划。你**必须**用文件写入工具把它们写到工作目录（或你所用 Harness 的制品目录，若有），然后在聊天中告诉用户文件路径并请其审阅。这适用于讨论摘要、设计草稿以及所有评审报告。
2.  **平实语言标准**：所有概念说明、摘要与沟通内容都**必须**用简单、直接、不堆砌术语的平实语言来写。直接解释技术机制。不要为求简洁而砍掉实质内容，也不要靠流行词撑场。不要使用没有依据的营销式形容词（例如 *seamless*、*robust*、*blazingly fast*）或装饰性副词（例如 *seamlessly*、*effortlessly*、*literally*、*drastically*、*obviously*）。
3.  **默认进行压力测试**：绝不默认同意。你的首要职责是对想法、策略与观点做压力测试。在肯定任何内容之前，先找出最薄弱之处、边界情况与盲点。
4.  **不吹捧**：杜绝谄媚。不要用 "great,"、"brilliant," 或 "smart." 之类的词评价想法。没有实质内容的恭维只是噪音。
5.  **批判优先**：即便想法本身站得住脚，也要先指出错误、缺漏或风险，再谈它的优点。
6.  **拒绝回音室式框定**：不要把用户的表述原样复述回去。若有人断言某个结论，不要条件反射式地附和。
7.  **主动构造反方论点**：对提出的每个策略，都要主动列出：用户忽略了什么？最有力的反方论点是什么？对立观点是否站得住脚？
8.  **让认同经得起检验**：只有当想法经受住严格、客观的审视之后，才表示同意。
9.  **禁用形容词（不恭维）**：在指代用户的输入、纠正或决定时，**严格禁止**使用 "brilliant,"、"great,"、"smart,"、"correct,"、"perfect,"、"excellent," 或 "spot-on" 这类肯定性形容词。
10. **禁用道歉**：受到质疑或被纠正时，**不得**输出客套的道歉语（例如 "I apologize,"、"I am sorry,"、"Forgive me"）。改为直接说明更正后的技术逻辑或权衡。
11. **交互不变量**：所有交互式关卡（若 Harness 具备 `ask_question` 之类的结构化提问工具，或直接用普通聊天）都**必须**严格只包含一个提问（`len(questions) == 1`），且是本轮唯一一次工具调用，并提供清晰、面向操作的选项，不带 `(Recommended)` 前缀。

## 输入

*   **`TargetFile`**：设计文档的绝对路径或相对路径。
*   **`GoldfishContext`**（可选）：用于建立系统基线的阅读清单。若省略，则只包含步骤 1.3 加入的链接文件。
*   **`Step`（可选）**：要运行的特定流水线预设或阶段（例如 `interactive`、`uninterrupted`、`feature_spec`、`implementation`，或单个阶段 `5`、`6`、`7`、`8`、`9`）。若省略，则向用户询问。

## 工作流

### 步骤 1：接收与设置

1.  检查是否提供了 `TargetFile`。若缺失：
    *   向用户说明，需要目标设计文档的路径才能分析其结构并发现语义切分。
    *   用普通文本消息在聊天中请用户提供该路径（**不要**使用 `ask_question` 之类的结构化提问工具，因为提供任意文件路径属于开放式文本输入，并非在固定选项间做选择），随后结束本轮。
2.  提供 `TargetFile` 后，检查是否提供了 `GoldfishContext`（空列表也算已提供，用户在提示词中明确声明不附加额外上下文直接继续，同样算已提供）。若缺失：
    *   向用户说明 Goldfish 上下文（文件阅读清单）是可选的，但能为评审员建立基线认知。
    *   说明工作目录内的链接文件会自动加入，而其他链接与 URL 需要批准。
    *   用普通文本在聊天中询问用户是否要提供额外的上下文文件。对开放式文件路径**不要**使用结构化提问工具。
3.  **链接文件（稍后执行）**：不要在接收阶段执行。等步骤 2 选定预设之后、在第一个接收 `GoldfishContext` 的阶段（除阶段 6 外的任意阶段）开始之前执行一次，`uninterrupted` 在内的任何流程都要执行。读取 `TargetFile`，跳过仅锚点链接（`#...`），去掉其他链接中的 `#fragment`，并相对设计文档所在文件夹解析每个相对链接。把真实路径（沿符号链接解析后）仍位于工作目录内的每个链接加入 `GoldfishContext`，跳过不存在的文件。若有链接解析到工作目录之外或本身是 URL，以普通文本在聊天中列出这些链接，询问要纳入哪些，并结束本轮；若无人能回答，例如无头运行，就全部排除并继续。只加入获批准的链接，并告诉用户哪些被排除。有些评审员无法打开 URL，因此把每个 URL 的原始页面保存为工作目录（或你所用 Harness 的制品目录）中的新文件，放入 `GoldfishContext`，并改为传递其绝对路径。若页面无法保存，请用户提供本地副本并结束本轮；若无人能回答，例如无头运行，就将其排除、告知用户并继续。把 `GoldfishContext` 传给除阶段 6 外的每个阶段（阶段 6 只读取文档本身）；并告知所有综合器把这些文件分发给每位评审员。

### 步骤 2：精选流水线预设选择

1.  **预设关卡检查**：
    *   若调用时显式提供了 `Step` 参数（例如 `interactive`、`uninterrupted`、`feature_spec`、`implementation`，或单个阶段 `5`、`6`、`7`、`8`、`9`），就映射到相应的预设或子流程，跳过交互式预设选择关卡。
    *   否则（若省略了 `Step`），你**必须**向用户展示"精选流水线预设"单选关卡（若 Harness 具备 `ask_question` 之类的结构化提问工具就用它，否则用普通聊天）。
2.  **弹窗不变量与载荷格式**：

    *   提问载荷**必须**严格只包含一个提问对象（`len(questions) == 1`）。严格禁止多提问载荷。
    *   提问工具**必须**是本轮载荷中唯一一次工具调用。调用后**必须**立即让出执行权。
    *   `is_multi_select` **必须**为 `false`。为保护拓扑依赖（5 → 6 → 7 → 8 → 9），严格禁止组合式的多选清单。
    *   选项 0 **必须**是主默认操作（不带 `(Recommended)` 前缀）。
    *   载荷规格：


```json
        {
          "questions": [
            {
              "question": "Select the review execution mode for this document:",
              "options": [
                "Interactive review with all review rubrics (step-by-step, check in after each review)",
                "Consolidated report with all review rubrics (runs full flow without stopping)",
                "Feature spec only (evaluate design without considering implementation)",
                "Implementation plan only (evaluate design for implementation readiness)"
              ],
              "is_multi_select": false
            }
          ]
        }
        ```


3.  **按预设派发动作**：

    *   **预设 0：`Interactive review with all review rubrics`**：进入步骤 3 发现语义切分，然后依次执行阶段 5、6、7、8、9，各阶段之间设置交互式检查点关卡。
    *   **预设 1：`Consolidated report with all review rubrics`**：进入步骤 3 发现语义切分，然后执行全部五个阶段，不在检查点暂停，将发现汇总到 `consolidated_review_report.md`。
    *   **预设 2：`Feature spec only`**：**完全跳过步骤 3 的语义切分发现**。设置 `FeatureRange = 1..End`，设置 `DetailedRange =
        N/A`，执行带检查点的阶段 5、6、7、8。在阶段 8 之后、阶段 9 之前干净地终止评审。
    *   **预设 3：`Implementation plan only`**：进入步骤 3 发现语义切分，确认 `DetailedRange`，并直接跳到阶段 9（实施就绪测试）。

### 步骤 3：语义切分发现

1.  **切分跳过检查**：若选择了预设 2（`Feature spec only`），**完全跳过本步骤**。把 `FeatureRange` 设为覆盖整个文档（第 1 行至末尾），直接进入步骤 4。
2.  **检查文档**：读取 `TargetFile` 以检查其结构与行数。
3.  **发现切分边界**：扫描主分界标题 `##
    Detailed Implementation Plan`（或常见同义写法：`## Implementation
    Plan`、`## Work Breakdown`、`## Implementation Steps`）。
    *   **检测到标准布局**：若分界标题在第 $L$ 行被明确识别：
        *   自动赋值 `FeatureRange = 1..(L-1)`。
        *   自动赋值 `DetailedRange = L..End`。
        *   在聊天中向用户输出一条简短的确认消息：
            `"Discovered semantic boundary at line L. FeatureRange: 1..(L-1),
            DetailedRange: L..End."`
        *   直接进入步骤 4，不展示确认弹窗。
    *   **边界含糊 / 存在多个候选标题**：若存在多个相互冲突的标题或非标准结构：
        *   展示一个单选关卡（若 Harness 具备 `ask_question` 之类且 `len(questions) == 1` 的结构化提问工具就用它，否则用普通聊天），把最可能的切分行作为选项 0，选项 1 允许通过自填指定自定义行范围。
    *   **未找到实施计划**：若文档只包含高层级的功能规格：
        *   在聊天中告知用户未检测到实施计划。
        *   赋值 `FeatureRange = 1..End` 与 `DetailedRange = N/A`。
        *   提议执行阶段 5-8（功能规格关卡）并继续。

### 步骤 4：分阶段策略

语义切分与执行预设确认之后：

1.  **确认评审目标**：核实 `FeatureRange` 与 `DetailedRange` 均已绑定。
2.  **派发执行流水线**：
    *   **Interactive review with all review rubrics**：依次执行阶段 5 → 阶段 6 → 阶段 7 → 阶段 8 → 阶段 9。
    *   **Consolidated report with all review rubrics**：运行子流程：不间断完整流程。
    *   **Feature spec only**：执行阶段 5 → 阶段 6 → 阶段 7 → 阶段 8，然后干净地终止。
    *   **Implementation plan only**：直接跳到阶段 9（实施就绪测试）。

--------------------------------------------------------------------------------

## 子流程

### 子流程检查点关卡与暂停/恢复协议

所有交互式评审阶段都以一个明确的单选关卡收尾（若 Harness 具备 `ask_question` 之类且 `len(questions) == 1`、`is_multi_select: false`、本轮唯一一次工具调用的结构化提问工具就用它，否则用普通聊天）：

1.  **阶段检查点模式**：
    *   **阶段 5、6、8（视角高度与理解检查点）**：
        *   选项 0：`Proceed to next stage: Stage [N+1] ([Next Stage Name])`
            （阶段 8 终态则为 `Conclude review and begin detailed implementation planning`）。
        *   选项 1：`I will update doc first (pause session; notify me in chat
            when edits are complete to re-run)`。
        *   选项 2：`Pause Review (save progress and exit)`。
    *   **阶段 7、9（整改与就绪检查点）**：
        *   选项 0：`Proceed to next stage: Stage [N+1] ([Next Stage Name])`
            （阶段 9 终态则为 `Conclude review and finalize document`）。
        *   选项 1：`Resolve findings with agent (evaluate findings, propose
            fixes, and apply approved edits)`。
        *   选项 2：`I will update doc manually (pause session; notify me in
            chat when edits are complete to re-run)`。
        *   选项 3：`Pause Review (save progress and exit)`。
2.  **消解语义（阶段 7 与阶段 9 的选项 1）**：
    *   **移交给消解器**：该 Agent 在主 Elephant context window 中，针对目标范围（`FeatureRange` 或 `DetailedRange`）调用 `egm-resolve`，并传入从 `critic_report.md` 或 `implementation_readiness_report.md` 解析出的发现。
    *   **消解工作流**：Elephant 把每条发现归类（`PROPOSE
        FIX` 与 `CONTEST`），写入 `goldfish_review_report.md`，并通过文件编辑工具在 `TargetFile` 上执行获批准的修改。
    *   **收敛**：应用修改后，重新读取 `TargetFile` 以重算行边界，然后进入下一阶段或重跑该阶段审计（强制最多 1 次复审）。
3.  **暂停与恢复语义（手动修改文档）**：
    *   **让出本轮**：该 Agent 在聊天中确认评审已因手动修改文档而暂停，并立即让出执行权。
    *   **恢复通知**：当作者在聊天中回复表示修改已完成：
        *   重新读取 `TargetFile` 以重算行偏移。
        *   若步骤 1.3 已执行，则对之后新增的链接套用其规则。
        *   重跑当前阶段的子流程。
        *   **1 次审计收敛上限**：每个阶段最多允许 1 次复审。若在复审之后再次请求手动修改文档，就告知作者已达上限，把残留发现记录为已接受的权衡，自动绑定选项 0，并进入下一阶段。
4.  **优雅终止语义（`Pause Review`）**：
    *   立即终止执行，不调用任何工具，同时保留所有报告制品。

### 子流程：不间断完整流程

1.  **不间断阶段执行**：按顺序执行全部五个评审阶段，步骤之间不设交互式检查点暂停。每个阶段都把单独的报告文件写入工作目录（或你所用 Harness 的制品目录，若有）。把 `GoldfishContext` 传给除步骤 6 外的每一步。
    *   **步骤 5（初始拉远审视）**：以 `Reviewers: [egm-zoom-out, egm-inventive-catalyst]` 在 `full file` 上派生 `egm-synthesizer`（或直接派生子 Agent）→ 写入 `zoom_out_report.md`。
    *   **步骤 6（理解测试）**：在 `FeatureRange` 与 `DetailedRange` 上直接派生 `egm-comprehension` 子 Agent（不用综合器）→ 把其完整结果写入 `comprehension_report.md`。
    *   **步骤 7（批判性评审）**：以 `Reviewers: [egm-design, egm-structural, egm-style]` 在 `FeatureRange` 上派生 `egm-synthesizer`（或直接派生子 Agent）→ 写入 `critic_report.md`。
    *   **步骤 8（中期拉远审视）**：以 `Reviewers: [egm-zoom-out]` 在 `full file` 上派生 `egm-synthesizer`（或直接派生子 Agent）→ 写入 `intermediate_zoom_out_report.md`。
    *   **步骤 9（实施就绪测试）**：以 `Reviewers: [egm-implementation-readiness,
        egm-codebase-details, egm-style]` 在 `DetailedRange` 上派生 `egm-synthesizer`（或直接派生子 Agent）→ 写入 `implementation_readiness_report.md`。
2.  **跨阶段综合与去重**：
    *   汇总 5 份阶段报告中的所有发现。
    *   按优先级把观察结果整合为可执行的任务（🔴 阻断、🟡 主要、🟢 细节）。
    *   构建可追溯矩阵，把原始发现映射到整合后的行动项。
3.  **交付物交付**：用文件写入工具写入 `consolidated_review_report.md`。
4.  **通知用户**：输出一条简短的聊天通知，指向 `consolidated_review_report.md`（给出其路径）。

### 子流程：拉远审视

1.  **委派给综合器子 Agent**：在 `full file` 上派生 `egm-synthesizer`（或 `agents/zoom_out.md` 处的专用 `egm-zoom-out` 子 Agent），套用 `resources/document_standards/zoom-out-standard.md`。作为步骤 8（中期拉远审视）运行时，把 `zoom_out_report.md` 的路径纳入上下文，并聚焦理解阶段与批判阶段带来的新增内容与缓解项。作为步骤 5 运行时，同时并行派生 `egm-inventive-catalyst`，把两份结果都写入 `zoom_out_report.md`。
    在阶段 5 与阶段 8 中都要传递 `GoldfishContext`。
2.  **交付**：用文件写入工具把发现写入 `zoom_out_report.md`（阶段 5）或 `intermediate_zoom_out_report.md`（阶段 8）。
3.  **通知用户（不在聊天中倾倒内容）**：告知用户发现已写入报告文件（给出其路径）。
4.  **检查点关卡**：按检查点关卡协议展示三态关卡：
    *   **阶段 5**：提问：`"Stage 5 (Initial Zoom Out Review) completed.
        Findings written to zoom_out_report.md. How would you like to
        proceed?"`，选项 0：`"Proceed to next stage: Stage 6 (Comprehension
        Test)"`。
    *   **阶段 8（仅功能规格关卡）**：提问：`"Stage 8 (Intermediate
        Zoom Out) completed. High-level architecture verified. How would you
        like to proceed?"`，选项 0：`"Conclude review and begin detailed
        implementation planning"`。
    *   **阶段 8（交互式完整流程）**：提问：`"Stage 8 (Intermediate
        Zoom Out) completed. Findings written to
        intermediate_zoom_out_report.md. How would you like to proceed?"`，
        选项 0：`"Proceed to next stage: Stage 9 (Implementation Readiness
        Test)"`。
    *   所有情形都提供选项 1：`"I will update doc first (pause session;
        notify me in chat when edits are complete to re-run)"` 与选项 2：
        `"Pause Review (save progress and exit)"`。

### 子流程：理解测试

1.  **直接派生评审员**：在 `FeatureRange` 与 `DetailedRange` 上、不套用任何文档标准，派生 `agents/comprehension.md` 处的 `egm-comprehension` 子 Agent。不要使用综合器：它的报告只保留发现，而作者必须看到释义。该测试考的是自成一体，而非细节。不要套用 `re-implementation-standard.md`：它要求代码层面的细节，而拉远审视标准禁止在 `FeatureRange` 中出现这类细节。
2.  **交付**：用文件写入工具把完整的评审结果写入 `comprehension_report.md`。先原样保留两个释义标题，再给出发现。即便没有发现，也要保留释义。
3.  **通知用户（不在聊天中倾倒内容）**：告知用户发现已写入 `comprehension_report.md`（给出其路径）。
4.  **检查点关卡**：展示阶段 6 的三态关卡：
    *   提问：`"Stage 6 (Comprehension Test) completed. Findings written to
        comprehension_report.md. How would you like to proceed?"`
    *   选项 0：`"Proceed to next stage: Stage 7 (Critic Review)"`
    *   选项 1：`"I will update doc first (pause session; notify me in chat
        when edits are complete to re-run)"`
    *   选项 2：`"Pause Review (save progress and exit)"`

### 子流程：批判性评审

1.  **启动对抗式评审循环**：在 `FeatureRange` 上线程内调用 `egm-review-loop`，评审员为 `[egm-design, egm-structural, egm-style]`，标准为 `{"egm-design": "feature-spec-standard", "egm-structural":
    "feature-spec-standard"}`，并附带 `GoldfishContext`。
2.  **通知用户（不在聊天中倾倒内容）**：告知用户发现已写入 `critic_report.md`（给出其路径）。
3.  **检查点关卡**：展示阶段 7 关卡：
    *   提问：`"Stage 7 (Critic Review) completed. Findings written to
        critic_report.md. How would you like to proceed?"`
    *   选项 0：`"Proceed to next stage: Stage 8 (Intermediate Zoom Out
        Review)"`
    *   选项 1：`"Resolve findings with agent (evaluate findings, propose
        fixes, and apply approved edits)"`
    *   选项 2：`"I will update doc manually (pause session; notify me in chat
        when edits are complete to re-run)"`
    *   选项 3：`"Pause Review (save progress and exit)"`
4.  **整改与消解（选项 1）**：
    *   在主 Elephant 上下文中、针对 `FeatureRange` 调用 `egm-resolve`，传入 `critic_report.md`（或 `goldfish_review_report.md`）中的发现。
    *   用文件编辑工具直接在 `TargetFile` 上执行获批准的修改。
    *   应用修改后，重新读取 `TargetFile` 以重算行边界，然后进入阶段 8（或重跑阶段 7，最多 1 次复审）。

### 子流程：实施就绪测试

1.  **启动对抗式评审循环**：在 `DetailedRange` 上线程内调用 `egm-review-loop`，评审员为 `[egm-implementation-readiness,
    egm-codebase-details, egm-style]`，标准为
    `{"egm-implementation-readiness": "implementation-readiness-standard",
    "egm-codebase-details": "implementation-readiness-standard"}`，并附带 `GoldfishContext`。
2.  **通知用户（不在聊天中倾倒内容）**：告知用户发现已写入 `implementation_readiness_report.md`（给出其路径）。
3.  **终态检查点关卡**：展示阶段 9 的终态关卡：
    *   提问：`"Stage 9 (Implementation Readiness Test) completed. Report
        written to implementation_readiness_report.md. How would you like to
        proceed?"`
    *   选项 0：`"Conclude review and finalize document"`
    *   选项 1：`"Resolve findings with agent (evaluate findings, propose
        fixes, and apply approved edits)"`
    *   选项 2：`"I will update doc manually (pause session; notify me in chat
        when edits are complete to re-run)"`
    *   选项 3：`"Pause Review (save progress and exit)"`
4.  **整改与消解（选项 1）**：
    *   在主 Elephant 上下文中、针对 `DetailedRange` 调用 `egm-resolve`，传入 `implementation_readiness_report.md`（或 `goldfish_review_report.md`）中的发现。
    *   用文件编辑工具直接在 `TargetFile` 上执行获批准的修改。
    *   应用修改后，重新读取 `TargetFile` 以重算行边界，然后结束本次评审会话（或重跑阶段 9，最多 1 次复审）。
