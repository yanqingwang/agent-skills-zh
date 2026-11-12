---
name: egm-review-loop
license: Apache-2.0
disable-model-invocation: true
description: >-
  通过自动化的多 Agent 审查循环，执行
  Elephant-Goldfish Model（EGM）中的对抗式审查（Antagonistic-Review）流程：
  依据定性标准和结构模板审计文档，并自动应用已获批准的修复。
  在审查设计文档、README、功能规格、实现计划，或验证文档完整性与语气时使用
  （Use when reviewing design docs, READMEs, feature specifications,
  implementation plans, or verifying document completeness and tone）。
---

> **中文汉化版** · 上游：[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) · 原文件：`skills/egm-review-loop/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Goldfish Review：Loop（编排驱动器）

在 Codex 或 ChatGPT Work 中运行时，先阅读 [Codex 集成](../../docs/codex.md)。
在 Claude Code 或 Cowork 中，先阅读 `${CLAUDE_PLUGIN_ROOT}/docs/claude.md`。

## 概述

本 Skill 是驱动多 Agent
审查循环的中央编排引擎。它协调两种不同的 Agent 记忆模型：

*   **The Goldfish（对抗式审计员）**：在隔离的全新 context window 中生成的
    Subagent，用来在没有历史偏见的情况下捕捉未言明的假设。
*   **The Elephant（持久解决者）**：持有机构知识的主 Agent 上下文，
    负责评估各项发现并应用已批准的修复。

驱动器负责接收参数、为审查员和标准解析路径、
在每轮迭代前无条件地重新解析目标行范围、
按配置生成并发的专项 Goldfish 审计员、
并与 Elephant 上下文协作处置各项发现。

## 委派

Goldfish 运行在没有对话历史的全新上下文中。用你的 Harness 的 subagent 工具生成每个
Subagent（Antigravity：`invoke_subagent`；Claude Code：`Agent`；Codex：`spawn_agent`）。每个 Subagent 定义在 `agents/<file>.md` 中，其 frontmatter 的 `name`（例如 `egm-zoom-out`）
就是你的 Harness 注册具名 subagent 时要请求的 subagent 类型。否则就生成一个通用
Subagent，并让它先读那个人设文件。原样传入
提示词，然后等待报告。
如果你的 Harness 无法嵌套 subagent，
就用直接派发代替 synthesizer。参见 `docs/harnesses.md`。
如果你的 Harness 没有 subagent 工具，停下来告诉用户：
同上下文里的审查不是 Goldfish 审查。

## 输入

调用方或用户恰好提供这几个参数：

*   **`TargetFile`**：目标文档的绝对或相对路径。
*   **`SemanticTarget`**：描述性定位字符串（例如 *"定位 SS-ID 为 'S1.12' 的
    H4 块"*），或 `full file`。
*   **`Reviewers`**：审查员名字列表（短名或路径）。
*   **`Standards`**：审查员名字到标准名字的映射（短名或
    路径）。
*   **`GoldfishContext`**：一份阅读清单（源文件、目录或
    文档 URL），喂给审查员以建立他们的基线。

## 路径与标准解析逻辑

解析 `Reviewers` 和 `Standards` 中的名字时：

*   **审查员短名**：把审查员短名（例如 `design_critic`、
    `structural`、`style`、`implementation_readiness`、
    `codebase_details`、`comprehension`、`zoom_out`）映射到 `agents/{name}.md`。
    人设文件定义该审查员的核心职责、审计向量和
    输出格式。
*   **标准短名**：把标准短名（例如 `feature-spec-standard`、
    `implementation-readiness-standard`、`zoom-out-standard`、`heilmeier-standard`、
    `re-implementation-standard`）映射到 `resources/document_standards/{name}.md`。
*   **自定义路径**：如果名字包含斜杠（`/`），把它当作
    绝对路径或工作区相对路径，直接读取。

## 执行工作流

### 第 1 步：输入接收与配置交互

评估提供的输入（`TargetFile`、`SemanticTarget`、`Reviewers`、
`Standards`、`GoldfishContext`）。

1.  **识别缺失输入**：确定哪些必需参数
    缺失。
2.  **交互式引导**：
    *   如果**所有**输入齐备，进入第 2 步。
    *   如果**部分或全部**输入缺失，通过聊天消息逐项交互式询问用户，
        **只询问缺失的输入**，一次一项。
3.  **审查员推荐**：
    *   *功能规格*：推荐 `design_critic`（映射到
        `resources/document_standards/feature-spec-standard.md`）和
        `structural`（映射到 `resources/document_standards/feature-spec-standard.md`）。
    *   *实现计划*：推荐 `implementation_readiness`
        （映射到 `resources/document_standards/implementation-readiness-standard.md`）
        和 `codebase_details`。
4.  **确认配置**：展示整合后的计划（目标、审查员、
    映射的标准），请用户确认后再继续。

### 第 2 步：打磨循环（迭代循环）

以连续循环执行以下序列：

#### 2.1 无条件的目标解析

每轮迭代之前，无条件地重新扫描 `TargetFile`：读取文件，
并用稳定的 `SemanticTarget` 字符串（例如定位目标标题）来
动态确定更新后的绝对起止行号。即使文件在前几轮被编辑过，
这也能保证绝对准确。（如果指定了 `full
file` 模式，确认全文件的行边界。）

#### 2.2 审查蜂群执行

1.  **启动 Subagent 蜂群**：
    生成 Subagent 执行审查：
    *   **分层派发（Synthesizer）**：生成中间
        synthesizer Subagent（`agents/synthesizer.md` / `egm-synthesizer`）。
        synthesizer 并行生成 Goldfish 审查蜂群、
        对发现去重、写出报告工件，
        并返回单条摘要消息，避免污染根对话的上下文。
        把下文的 Failed Reviewers 规则传给它。它的摘要必须
        对每个请求的审查员给出状态：`completed` 或 `not run`。
    *   **直接派发（扁平蜂群）**：或者，直接生成
        `Reviewers` 中请求的每个审查员 Subagent。
        指示每个 Subagent 先读 `agents/{name}.md` 里的人设定义，
        再按解析出的行范围审计 `TargetFile`，
        以 `resources/document_standards/` 中指定的标准为依据，
        并提供 `GoldfishContext`。
    *   每个审查员产出的发现要带严重级别（🔴 Blocker、🟡 Major、🟢
        Nit）、行号、差异描述和理由。
2.  **汇总发现**：把所有审查员的发现收进一个扁平的
    `FindingsList`。给每条发现一个稳定 id
    （`<reviewer>-<round>-<n>`），记录其审查员、严重级别和受影响
    范围。
3.  **失败的审查员**：超时、失败或没有返回报告的审查员
    视为没有审查。重试一次。再次失败就在报告中记为 **not run**。
    绝不把它算作"零发现的审查员"。
    如果 synthesizer 的摘要没有给出某个请求审查员的状态，
    把该审查员记为 not run。

#### 2.3 聚合后的解决移交

1.  把 `TargetFile`、生效行范围和聚合的 `FindingsList`
    交给 **`egm-resolve`** 工作流。
2.  在主 Elephant 上下文中执行解决工作流：
    *   把发现归入 `CONTEST` 或 `PROPOSE FIX`。
    *   用你的文件写入工具保存 `goldfish_review_report.md`。
    *   展示交互式决策门（自动接受 Auto accept、继续 Continue、
        逐项交互 Interactive breakdown）。
    *   用你的文件编辑工具把已批准的文字修复应用到 `TargetFile`。

#### 2.4 迭代判定与轮次边界

新的审查员每轮采样都不同，所以即使文档在改善，
一轮零发现也很罕见。改用这些规则：

*   **已定案的发现（Settled findings）**：发现被抗辩成功，或
    记录在案但不修复（接受的风险），即为已定案。跨轮保留已定案清单。
    如果新审查员再次提出一条已定案的发现（相同受影响
    范围、相同问题），不要重新打开它。
*   **已修复的发现（Fixed findings）**：应用了修复并不等于定案。如果之后
    有审查员在相同范围提出同一问题，说明修复失败，或
    后续编辑又把问题引进来了。重新打开该发现。
*   **干净轮次（Clean round）**：当没有任何审查员提出未定案的 Blocker 或
    Major 发现时，该轮为干净。Nit 不阻塞。被记为
    not run 的审查员会使该轮不干净。要在应用该轮修复之前，
    就根据审查结果做出这个判定。
*   **收敛（Converged）**：连续两轮干净。一轮干净不够，
    因为下一个新审查员可能在同一段文本里找到不同的疏漏。
*   **上限（Cap）**：5 轮。
*   **震荡（Churn）**：新发现落在某个已应用修复的范围内，
    且撤销那个修复就能解决它。

收敛后进入第 3 步。触发上限或震荡时，按严重级别写出未决
发现的简短清单，然后问用户一个问题：接受并继续，
超过上限继续跑，还是把文档退回起草。

**关键的轮替要求**：某一轮的解决阶段结束后，循环驱动器
**必须遵守 `egm-resolve` 中的轮替检查点**。
驱动器必须在人类轮次之间保持空闲，
只有当用户明确确认想再跑一轮审查时，
才回到第 2.1 步。

### 第 3 步：输出边界与最终检查点

完成时（收敛、用户接受上限或震荡、或手动
中止）：

*   **程序化调用方**：如果作为 `egm-review` 的子流程运行，干净地退出，
    把执行交回父工作流。
*   **手动调用**：在聊天中输出完成摘要：*"审查循环已经
    在 [N] 轮后完成（[converged | accepted at cap | halted]）。
    未决发现都在报告里。要进入下一阶段吗，
    还是你还有最后的问题？"*
