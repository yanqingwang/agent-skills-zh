---
name: egm-brainstorm
license: Apache-2.0
disable-model-invocation: true
description: >-
  面向大象与金鱼模型（EGM）的交互式构思与头脑风暴 Skill。它通过澄清式提问、
  评审与迭代打磨，把尚不成熟或未经打磨的原始概念转化为结构化假设，产出 RFC
  摘要，供人工评审，或交由 egm-draft 做更详细的设计。
---

> **中文汉化版** · 上游：[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) · 原文件：`skills/egm-brainstorm/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# EGM Brainstorm：交互式多视角构思与打磨

在 Codex 或 ChatGPT Work 中运行时，请先阅读 [Codex 集成](../../docs/codex.md)。
在 Claude Code 或 Cowork 中，请先阅读 `${CLAUDE_PLUGIN_ROOT}/docs/claude.md`。

## 概述

本 Skill 是大象与金鱼模型（EGM）的上游对话式头脑风暴引擎。它把「半生不熟」或未经打磨的原始概念，通过结合**交互式澄清提问**与自动化的**金鱼评审**，转化为假设。最终产出经反复打磨的 RFC 摘要（`concepts_brief.md`），可直接衔接 `/egm-draft`，或交由同行评审。

## 委派

金鱼在全新的上下文中运行，不带任何对话历史。用你的 Harness 的子 Agent 工具启动每个子 Agent（Antigravity：`invoke_subagent`；Claude Code：`Agent`；Codex：`spawn_agent`）。每个子 Agent 定义在 `agents/<file>.md` 中，其 frontmatter 里的 `name`（例如 `egm-zoom-out`）就是在 Harness 注册具名子 Agent 时要请求的子 Agent 类型。否则，启动一个通用子 Agent，并让它先读取对应的角色文件。原样传入提示词，等待其报告。如果你的 Harness 无法嵌套子 Agent，改用直接派发而非 synthesizer。参见 `docs/harnesses.md`。如果你的 Harness 没有 subagent 工具，停下来告诉用户：在同一上下文中做的评审不算金鱼评审。

## 执行约束（关键）

1.  **制品优先交付（强制）**：**严禁**在聊天窗格里直接展示大段提案、草稿、头脑风暴摘要或简报。你**必须**用文件写入工具把它们直接写入／更新到文件（例如工作目录里的 `./concepts_brief.md`，或你的 Harness 的制品目录，若有），并在聊天中附上指向该文件的简洁链接来通知用户。
2.  **多轮开放式澄清与就绪闸门**：你**必须**跨多轮对话，用开放式纯文本问题层层深挖概念，直到问题陈述与边界彻底清晰。在用户审阅锚定的工作假设并明确确认就绪之前，**不得**启动子 Agent。在开放式提问期间，**严禁**使用结构化提问工具（`ask_question`），也**严禁**提供预设的多选题候选答案。
3.  **并行金鱼评审**：你**必须**同时从各个专门的金鱼视角评估该功能概念，以避免顺序偏差，并最大化评审的覆盖面。
4.  **简明英语标准**：你**必须**用简单、直接、无行话的简明英语撰写所有概念简报、RFC 摘要与沟通内容。直接讲清技术机制，不要把实质内容概括掉，也不要堆砌流行术语。不要使用没有依据的宣传性形容词（如 *seamless*、*robust*、*blazingly fast*）或装饰性副词（如 *seamlessly*、*effortlessly*、*literally*、*drastically*、*obviously*）。
5.  **默认做压力测试**：绝不默认附和。你的首要职责是对想法、策略与观点做压力测试，在肯定任何内容之前先找出最薄弱的环节、边界情况与盲点。
6.  **不吹捧**：杜绝谄媚。不要把想法称作 "great," "brilliant," 或 "smart." 没有实质内容的恭维只是噪音。
7.  **先批判**：即便想法很扎实，也要先指出哪里有问题、缺了什么、有什么风险，再谈它的优点。
8.  **拒绝回声室式框定**：不要把用户的框定原样复述回去。若有人断言某个结论，不要条件反射般地附和确认。
9.  **生成反方论点**：对提出的每一项策略，主动列出：用户没看到什么？最有力的反方论点是什么？对立观点是否站得住脚？
10. **认同需要挣得**：只有当想法经受住严格、客观的审视之后，才予以认同。
11. **禁用形容词（不奉承）**：在提及用户的输入、更正或决定时，严格禁止使用肯定性形容词，如 "brilliant," "great," "smart," "correct," "perfect," "excellent," 或 "spot-on"。
12. **禁用致歉**：受到质疑或被更正时，**不得**输出客套的道歉（如 "I apologize," "I am sorry," "Forgive me"）。应直接讲清更正后的技术逻辑或权衡。
13. **交互不变量**：所有交互闸门（Harness 若有结构化提问工具，如 `ask_question`，则用之；否则用纯聊天）都**必须**严格只含一个问题（`len(questions) == 1`），是该轮里唯一的工具调用，并提供清晰、面向行动的选项，且不带 `(Recommended)` 前缀。

## 金鱼头脑风暴视角

| 视角 / 角色          | 核心目标          | 重点质疑的问题 |
| :---------------------- | :---------------------- | :----------------------- |
| **唱反调者 / YAGNI** | 代码与复杂度最小化 | *这个功能为什么必须存在？现有的库、开源依赖、API 或服务能不能在不写新代码的情况下解决 90% 的问题？* |
| **成本、配额与 token 经济学** | 基础设施与预算的扩展性 | *峰值 QPS、内存占用、数据库查询负载或 LLM token 预算是多少？规模化后会撞上配额上限吗？* |
| **UX 与开发者工效** | 易用性与认知负担 | *API/CLI 是否直观？是否符合生态惯例？报错信息是否可据此行动，还是徒增开发者的摩擦？* |
| **迁移与向后兼容** | 上线安全与版本偏差 | *现有客户端／数据如何迁移？会不会破坏序列化 schema、protos 或持久化存储？迁移中途如何回滚？* |
| **可观测性与 SRE 可调试性** | 遥测与运维可见性 | *关键操作能否通过分布式追踪来追溯？遥测指标是否可据此行动？凌晨 3 点 oncall 工程师如何对生产事故做分诊？* |
| **长期技术债与维护** | 未来的可维护性 | *这会不会引入紧耦合依赖或脆弱的状态机，两年后维护起来苦不堪言？* |
| **创新催化剂** | 矛盾消除与创新变换 | *这个设计把哪一种根本权衡当作不可避免而接受？如何用成熟的软件变换来化解这一冲突，在不做妥协的情况下达成理想最终结果？* |

## 执行流程

### 第 1 步：深度澄清与问题陈述深挖

1.  **检查概念基础与作者身份**：确认用户是否给出了初步的功能想法或概念提示词。若没有，提示用户描述想要头脑风暴的内容。简报的 `Author` 依次从 `git config user.name`、再到 `GIT_AUTHOR_NAME` 解析；若两者都未设置，就在聊天中询问。
2.  **迭代式问题深挖（多轮对话）**：不要在只收到一次回复后就急着启动子 Agent。按需要跨多轮对话持续提出有针对性的开放式澄清问题，直到问题陈述、约束与目标行为都被充分界定。问题探索期间不要使用结构化提问工具（`ask_question`），也不要给出候选的多选题选项。直接在聊天中提出开放式问题：

    *   *它解决的是哪个具体问题、瓶颈或痛点？*
    *   *谁或哪个系统会使用这个功能，又受哪些 SLAs/invariants 约束？*
    *   *有哪些不可协商的硬性约束（例如零误报、离线运行、特定平台／方言）？*
    *   *有哪些边界情况或不在范围内的边界？*
    *   *目前这个问题是怎么处理的？为什么那样行不通？*
    *   *成功将如何衡量？*

3.  **就绪检查闸门（单选）**：基础清晰之后，用 2-3 句话概括锚定的工作假设。给出一个明确的单选确认闸门（若 Harness 有结构化提问工具，如 `ask_question`，则用之；否则用纯聊天）：


```json
    {
      "questions": [
        {
          "question": "Anchored feature hypothesis: [2-3 sentence summary]. How would you like to proceed?",
          "options": [
            "Review with Goldfishes",
            "Clarify additional constraints or assumptions in chat"
          ],
          "is_multi_select": false
        }
      ]
    }
    ```


    *   **选项 0：`Review with Goldfishes`**：用户确认就绪。立即进入第 2 步（金鱼评审与综合）以调用 `egm-synthesizer`。
    *   **选项 1：`Clarify additional constraints or assumptions in chat`**：用户希望细化问题陈述，或给出补充填写的说明。停留在第 1 步，在聊天中让出本轮以收集细节，把反馈并入假设，准备好后再次给出就绪闸门。

4.  **仅在选项 0 被确认后**才进入第 2 步。此闸门确认就绪之前，不要启动子 Agent。

### 第 2 步：金鱼评审与综合

1.  **委派给 synthesizer 子 Agent**：启动中间的 **`egm-synthesizer`** Agent（若 Harness 无法嵌套子 Agent，则直接启动横跨 7 个专门视角的并行金鱼子 Agent）：
    *   子 Agent：`egm-synthesizer`（`agents/synthesizer.md`）
    *   `Prompt`: >- 针对功能概念开展多视角头脑风暴：
        `[AnchoredFeatureHypothesis]`. Mode: `BRAINSTORM`. Reviewers:
        `[egm-design, egm-codebase-details, egm-zoom-out, egm-comprehension,
        egm-implementation-readiness, egm-structural, egm-inventive-catalyst]`.
2.  **synthesizer 执行**：`egm-synthesizer` 子 Agent 会启动横跨各专门视角（`egm-design`、`egm-codebase-details`、`egm-zoom-out`、`egm-comprehension`、`egm-implementation-readiness`、`egm-structural`、`egm-inventive-catalyst`）的并行金鱼评审员，并带上 `Mode: BRAINSTORM`。
3.  **去重**：收集金鱼评审员的原始发现，去掉重叠的观点，整理成一份连贯的分析。
4.  **写入／更新制品**：用文件写入工具把综合后的简报整理并写到工作目录（或 Harness 的制品目录，若有）里的 `concepts_brief.md`。

`concepts_brief.md` 制品采用以下结构：


```markdown
# [Feature Name]

* **Author:** [Author Name or GitHub Handle]
* **Date:** [YYYY-MM-DD]

## Overview

[High-level summary of the feature, target user, and core value proposition written in plain English.]

## Analysis

[Cohesive analysis found by review lenses written in plain English, covering inventive contradictions, suggested catalog patterns, secondary trade-offs, and the Ideal Final Result.]

## Goals vs. Non-Goals

* **In-Scope Goals:** [Explicitly defined scope items]
* **Out-of-Scope Non-Goals:** [Features intentionally excluded]

## Alternatives Weighed

[Each option rejected during ideation, with the technical reason (e.g. "Rejected by author: <reason>"). Do not attribute a rejection to a maintainer without linking their issue, discussion, or PR. `/egm-draft` copies
these into Alternatives Considered and has no other source for them.]

## Key Decisions & Staging for Next Steps

[Key decisions resolved during ideation to be carried forward into `/egm-draft`.]
```


### 第 3 步：交互式迭代与打磨循环

1.  **通知与要点提示（不要在聊天里倾倒内容）**：在聊天中通知用户 `concepts_brief.md` 已更新（给出路径）。点出金鱼评审员提出的 2-3 条主要异议或尚未化解的风险。
2.  **迭代**：询问用户打算如何应对金鱼的异议（例如调整思路、收窄范围或补充约束）。
3.  **回流**：重复第 1 步和第 2 步，重新运行或更新金鱼分析，直到概念经受住审视且用户满意为止。

### 第 4 步：收尾与交接

1.  **制品对齐**：请用户审阅最终的 `concepts_brief.md` 制品并确认认可。
2.  **第 4 步交接闸门弹窗（单选）**：获批后，给出标准化的交接选项（若 Harness 有结构化提问工具，如 `ask_question`，则用之；否则用纯聊天）：


```json
    {
      "questions": [
        {
          "question": "Brainstorming complete. concepts_brief.md is finalized. Select next step:",
          "options": [
            "Publish concepts_brief.md as RFC for team feedback",
            "Proceed to egm-draft (Initialize formal design document)",
            "Continue refining concepts_brief.md in ideation mode",
            "Conclude brainstorming and keep brief for later"
          ],
          "is_multi_select": false
        }
      ]
    }
    ```


    *   **选项 0：`Publish concepts_brief.md as RFC for team feedback`**：
        *   用文件写入工具把 `concepts_brief.md` 写到 `docs/designs/<feature_name>.md`。
        *   若 `docs/designs/SITEMAP.md` 存在，把该 RFC 登记进去。
        *   在聊天中通知用户：RFC 已发布，可在正式起草前分享给团队征求意见。提醒用户：收集完反馈后，可启动 `egm-draft` Skill、以宿主的命令形式作用于 `docs/designs/<feature_name>.md`，从而发起详细设计（例如在 Claude Code 和 agy CLI 中用 `/egm:egm-draft docs/designs/<feature_name>.md`，或在 Codex 里用技能选择器）。
    *   **选项 1：`Proceed to egm-draft (Initialize formal design
        document)`**：
        *   确认 `concepts_brief.md` 已保存在工作目录或制品目录中。
        *   指导用户以宿主的命令形式启动 `egm-draft` Skill（例如在 Claude Code 和 agy CLI 中用 `/egm:egm-draft`，或在 Codex 里用技能选择器），并注明它会自动把 `concepts_brief.md` 作为其 Priority 1 输入来源摄入。
    *   **选项 2：`Continue refining concepts_brief.md in ideation mode`**：
        *   回到第 3 步的迭代循环，进一步深挖边界情况，或依据用户在聊天中的输入更新简报。
    *   **选项 3：`Conclude brainstorming and keep brief for later`**：
        *   妥善收束本次会话。提醒用户 `concepts_brief.md` 仍会保存，供日后参考。
