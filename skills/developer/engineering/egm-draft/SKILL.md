---
name: egm-draft
license: Apache-2.0
disable-model-invocation: true
description: >-
  依据 egm-brainstorm 的概念简报（或用户笔记）逐节起草设计文档。这是
  Elephant-Goldfish（EGM）功能流程的第二步。当你已就需求 + 方案达成一致、准备
  撰写设计文档时使用。
---

> **中文汉化版** · 上游：[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) · 原文件：`skills/egm-draft/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 设计起草（文档构建）

在 Codex 或 ChatGPT Work 中运行时，请先阅读 [Codex 集成](../../docs/codex.md)。
在 Claude Code 或 Cowork 中，请先阅读 `${CLAUDE_PLUGIN_ROOT}/docs/claude.md`。

本 Skill 基于头脑风暴阶段已对齐的问题与需求，引导用户逐步起草技术设计文档。

## 执行约束（关键）

1.  你**必须**阅读并遵循
    `resources/execution_instructions.md` 中的执行说明。
2.  **交付物优先（强制）**：严禁在聊天
    窗格中直接展示大段提案、草稿、总结或计划。你**必须**使用文件写入工具，将它们
    直接写入工作目录（或 Harness 的制品目录，若存在）中的 `design_draft.md`
    或 `./design_draft.md`，并在聊天中告知用户文件路径、请其审阅。此规则适用于
    讨论总结、设计草稿及所有评审报告。
3.  **平实表达标准**：你**必须**用简单、直接、不堆砌术语的平实中文撰写所有
    概念简报、总结与沟通内容。直接讲清技术机制，不要用概括稀释实质内容，也不要
    依赖流行术语。不要使用无依据的夸大形容词（例如
    *seamless*、*robust*、*blazingly fast*）或装饰性副词（例如
    *seamlessly*、*effortlessly*、*literally*、*drastically*、*obviously*）。
4.  **默认压力测试**：不要默认表示赞同。你的首要职责是对想法、策略和观点做压力
    测试。在肯定任何内容之前，先找出最薄弱之处、边界情况和盲点。
5.  **拒绝奉承**：消除谄媚。不要把想法称作 "great"、"brilliant" 或
    "smart"。没有实质内容的恭维只是噪音。
6.  **先批判**：即便想法很扎实，也要先指出错误、缺失或风险，再谈其优点。
7.  **拒绝回声室式表述**：不要把用户的表述原样复述回去。若有人断言某个结论，
    不要条件反射般地予以认可。
8.  **生成反方论点**：对提出的每一项策略，主动列出：用户没有看到什么？最有力的
    反方论点是什么？对立观点是否站得住脚？
9.  **让赞同经得起检验**：只有当想法经受住严格、客观的审视后，才表示赞同。
10. **禁用形容词（禁止吹捧）**：在提及用户的输入、纠正或决定时，严禁使用
    "brilliant"、"great"、"smart"、"correct"、"perfect"、"excellent"、
    "spot-on" 之类表示认可的形容词。
11. **禁用道歉**：受到质疑或被纠正时，**不得**输出客套的道歉语（例如
    "I apologize"、"I am sorry"、"Forgive me"）。改为直接说明纠正后的技术逻辑
    或权衡。
12. **交互不变量**：所有交互式门控（若 Harness 提供 `ask_question` 之类的结构化
    提问工具，或纯聊天）**必须**只包含一个问题（`len(questions) == 1`），且是
    该轮中唯一的工具调用，并提供清晰、可操作的选项，不带 `(Recommended)` 前缀。
13. **架构由作者决定**：当某个设计决策存在不止一个合理答案（例如数据模型、组件
    边界、存储、协议）时，最多给出三个选项，每个都说明其机制、权衡以及失效条件，
    并通过单选门控请作者选择。不要为选项排序、标注默认项或替其选定。若作者要求你
    来选（"just pick one"），重述各项权衡并再次给出同一门控。对于只有单一合理答案
    的机械性选择（例如文件命名、格式），由你自行决定。

## 输入

*   **`Context File`**（可选）：前置文档的文件路径（例如
    `docs/designs/<feature_name>.md`、`concepts_brief.md` 或
    `discussion_summary.md`）。若省略，本 Skill 默认消费前置上下文（例如
    `concepts_brief.md` 或 `discussion_summary.md`）。

## 执行工作流

按顺序执行以下步骤。按次序推进，但允许用户回头补做遗漏的阶段。未经用户明确
同意确认可在步骤间继续，不要跳步。随着对话在各章节间推进，迭代式地撰写文档。

### 章节审批门控（步骤 2–5）

在使用文件写入工具写入或更新 `design_draft.md` 中的每一章节后，必须在同一轮中
按以下严格的生成顺序给出审批门控：

1.  **可见的聊天摘要与链接（第一步）**：你**必须**在提问门控之前输出对话式的
    markdown 文本。说明起草或更新了哪一章节，点出 2–3 个关键决策或新增内容，并
    给出指向 `design_draft.md` 的链接或路径（例如在 Codex 中用
    `[design draft](/absolute/project/design_draft.md)`）。
2.  **审批门控（第二步）**：在同一轮中给出单选审批选项（若 Harness 提供
    `ask_question` 之类结构化提问工具，令 `len(questions) == 1` 且
    `is_multi_select: false`，或用纯聊天）：

> [!CAUTION] **负面约束（禁止空聊天气泡）**：绝不要发出响应文本为空的
> 结构化提问工具调用。在调用提问门控之前，务必先生成可见的聊天说明
> 和文件链接。


```json
{
  "questions": [
    {
      "question": "Drafted [Section Name] in design_draft.md. Please review. How would you like to proceed?",
      "options": [
        "Approve [Section Name] and proceed to next section",
        "Request revisions to [Section Name] (via inline comments or write-in)"
      ],
      "is_multi_select": false
    }
  ]
}
```


*   **选项 0（`Approve [Section Name] and proceed to next section`）**：
    *   若本轮上下文中还存在对 `design_draft.md` 的行内批注，先把这些行内更新
        应用到 `design_draft.md`，再推进到下一章节。
    *   否则，立即推进到起草下一章节。
*   **选项 1（`Request revisions to [Section Name] (via inline comments or
    write-in)`）或带行内批注的模态跳过**：
    *   **附行内批注和/或填写说明时**：同时检查填写的回复以及留在 `design_draft.md`
        上的行内批注（尊重要求保留高亮章节的正面批注，以及要求修订或删除内容的
        负面批注）。使用文件写入工具把所有修订应用到 `design_draft.md`，通知用户，
        并重新给出审批门控。
    *   **空填写防护（关键）**：若选中该项时既无填写文本，**又**无本轮上下文中的
        任何行内批注，**不要**循环或报错。在聊天中提示：`"Please specify the adjustments or additions
        needed for [Section Name] (either via inline comments on design_draft.md
        or here in chat) so I can revise the draft."`
        并让出主动执行，在聊天中等待用户澄清。

### 步骤 1：摄入前置上下文（概念简报或笔记）

1.  **Context File**：若指定了 `Context File`，直接读取并解析。
2.  **多态摄入**：若省略，则按严格的优先级顺序检查各来源来发现上下文：
    *   **优先级 1：现代构思简报（`concepts_brief.md`）**：在
        `./concepts_brief.md`、对话制品目录或 `scratch/concepts_brief.md` 中查找
        `concepts_brief.md`。若找到，摄入并解析该简报。
    *   **优先级 2：讨论总结（`discussion_summary.md`）**：若未找到
        `concepts_brief.md`，则在 `./discussion_summary.md`、对话制品目录或
        `scratch/discussion_summary.md` 中查找 `discussion_summary.md`。若找到，
        摄入并解析该总结。**不要**提示用户启动 `/egm-brainstorm`，也不要警告其
        已弃用。
    *   **优先级 3：交互式聊天提示**：若两个文件都不存在，则在聊天中提示用户提供
        该功能的问题陈述、目标和技术上下文，或建议用户以宿主的命令形式启动
        `egm-brainstorm` skill（例如在 Claude Code 和 agy CLI 中用
        `/egm:egm-brainstorm`，或在 Codex 中用 skill 选择器）。
3.  **核对状态**：解析文档，向用户给出一次快速确认，确保起始上下文正确。
4.  **达成共识**：取得明确同意后开始起草文档。
5.  **确定作者**：若摄入的简报带有 `Author`，使用它；否则依次使用
    `git config user.name`、`GIT_AUTHOR_NAME`。若两者都未设置，在聊天中提示用户。
    将作者记录在文档头部。

### 步骤 2：起草概述、目标与问题陈述

1.  **复核上下文**：用摄入的信息框定业务问题和用户痛点。
2.  **起草内容**：依照设计文档模板（`references/design_doc.md`），用清晰、平实的
    中文 Markdown 撰写 "The Problem"、"Overview"、"Goals" 和 "Non-Goals"。
3.  **聚焦**：强调*为什么*（用户需求与业务价值），而不是*怎么做*（技术实现）。
4.  **写入草稿交付物（强制）**：使用文件写入工具，把这份初始草稿保存到工作目录
    （或 Harness 的制品目录，若存在）中的 `design_draft.md`。
5.  **通知与核对（禁止在聊天中倾倒内容）**：严禁在聊天中打印草稿。改为在对话式
    聊天文本中告知用户概述与问题陈述已起草完成，给出指向 `design_draft.md` 的
    可点击链接或路径，并针对 `Overview & Goals` 给出章节审批门控。

### 步骤 3：起草技术方案

1.  **综合架构**：复核摄入上下文中提出的高层架构与方案。
2.  **起草方案**：用清晰的文字描述拟做的改动，指出新增组件、改动的文件和 API
    变更。加入基于文本的块状图（例如 ASCII 或 Mermaid）来说明数据流。
3.  **更新草稿交付物（强制）**：使用文件写入工具更新 `design_draft.md`，追加/
    插入 "Technical Plan" 章节。
4.  **通知与核对（禁止在聊天中倾倒内容）**：严禁在聊天中打印技术方案。在对话式
    聊天文本中告知用户技术方案已添加，给出指向 `design_draft.md` 的可点击链接
    或路径，并针对 `Technical Plan` 给出章节审批门控。

### 步骤 4：起草备选方案

1.  **复核备选方案**：从摄入上下文的 `Alternatives Weighed` 章节读取头脑风暴中
    已否决的备选方案。不要依赖记忆：起草常常在新的会话中进行。若该章节缺失，
    询问用户否决了哪些备选方案、原因是什么。
2.  **起草内容**：用平实的中文、以 Markdown 格式撰写 "Alternatives Considered"
    章节。
3.  **详述理由**：对每个备选方案，明确说明*为什么*被否决（例如延迟更高、扩展
    受限、团队不熟悉）。用 `Rejected by author: [technical rationale]` 记录
    作者的决定。除非引用上游维护者的 issue、讨论或 PR URL，否则**不要**写
    `Rejected by maintainer`。
4.  **更新草稿交付物（强制）**：使用文件写入工具更新 `design_draft.md`，追加/
    插入 "Alternatives Considered" 章节。
5.  **通知与核对（禁止在聊天中倾倒内容）**：严禁在聊天中打印备选方案。在对话式
    聊天文本中告知用户备选方案章节已添加，给出指向 `design_draft.md` 的可点击
    链接或路径，并针对 `Alternatives Considered` 给出章节审批门控。

### 步骤 5：起草实施方案

起草一份详细的实施计划，聚焦于如何实现该功能。这份计划必须足够详尽。你应当提问
并补充足够的细节，使得仅凭这份计划就能完成实现，而不必再做任何有影响的决策。
遵循以下准则：

1.  **单一实施清单**：把需要做的所有事项列在同一个统一章节中。
2.  **枚举文件**：列出每一个将被改动、新建或删除的文件。包含所有应更新的文档、
    schema、config、proto 或测试文件。你**必须**引用计划涉及的每一个文件。
3.  **说明理由**：每个文件都要附上理由，说明*改什么*以及*为什么*必须改。
4.  **链接格式**：已知时给出文件完整路径，否则给出清晰的文件名；包内与同级文档
    链接使用相对路径（例如 `./sub/README.md` 或 `../sibling/README.md`）。
5.  **禁止代码**：不要在这份设计草稿中生成真正的实现代码。伪代码、API 或 schema
    允许出现。
6.  **更新草稿交付物（强制）**：使用文件写入工具更新 `design_draft.md`，追加/
    插入 "Detailed Implementation" 章节。
7.  **通知与核对（禁止在聊天中倾倒内容）**：严禁在聊天中打印实施计划。在对话式
    聊天文本中告知用户详细实施计划已添加，给出指向 `design_draft.md` 的可点击
    链接或路径，并针对 `Detailed Implementation` 给出章节审批门控。

### 步骤 6：写出设计文档定稿

当被要求写出或保存设计文档时，严格遵循以下规则：

1.  **与前置上下文对照**：不要在此按 Zoom Out 标准评判草稿。撰写草稿的会话已认可
    它；`/egm-review` 第 5 阶段会在全新上下文中执行该检查。改为重读步骤 1 摄入的
    上下文，与草稿比对。没有 Goldfish 能做这项检查，因为没有 Goldfish 会读取简报。
    *   **矛盾**：简报已就某个问题做出决定，而草稿的决定不同。逐一报告。
    *   **新增**：草稿决定了简报未提出的问题。仅当它改变架构、外部接口或依赖时
        才报告。

    先列矛盾，每条一行，引用简报与草稿的原文。请用户逐条裁定。不要自行改动草稿
    去迎合简报：草稿可能是对的，因为起草会读到头脑风暴未读过的代码。若没有任何
    分歧，用一行说明即可。若步骤 1 未找到前置文件，跳过此步。

    若存在未决的矛盾，停下来等待用户。在步骤 6.2 之前，把每一项决定应用到
    `design_draft.md`。

2.  **目标目录**：若用户指定了目标目录或文件，使用它。否则探查工作区中已有的
    设计目录（来自 `Context File` 所在目录、`docs/designs/` 或
    `<project>/docs/designs/`），绑定 `[DiscoveredPath]`（默认 `docs/designs/`），
    并给出单选门控（若 Harness 提供 `ask_question` 之类结构化提问工具，令
    `len(questions) == 1` 且 `is_multi_select: false`，或用纯聊天）：


```json
    {
      "questions": [
        {
          "question": "Where should the design be saved?",
          "options": [
            "Save to detected directory: [DiscoveredPath]",
            "Specify custom target directory"
          ],
          "is_multi_select": false
        }
      ]
    }
    ```


    *   **选项 0**：把 `<DESIGN_DIR>` 设为 `[DiscoveredPath]`。
    *   **选项 1**：若填写文本中提供了自定义路径，把 `<DESIGN_DIR>` 设为该路径。
        若填写为空，在聊天中提示：
        `"Please specify the custom target directory path where you would like
        to save the design document."`
        并让出主动执行。

3.  **更新站点地图**：若 `<DESIGN_DIR>/SITEMAP.md` 存在，在其中登记新设计
    （Link、Date、Author、Components、Description）。

4.  **写出文档**：定稿后，使用文件写入工具把 `design_draft.md` 的内容写到目标
    文件 `<DESIGN_DIR>/<FEATURE>.md`。若需调整最终结构，遵循
    [模板](references/design_doc.md)。

5.  **清理格式**：确保 Markdown 格式整洁规范、表格语法有效、代码块围栏正确。

6.  **交接**：给出指向定稿的可点击链接，并建议用户以宿主的命令形式在
    `<DESIGN_PATH>` 上启动 `egm-review` skill 来评审（例如在 Claude Code 和
    agy CLI 中用 `/egm:egm-review <DESIGN_PATH>`，或在 Codex 中用 skill
    选择器）。
