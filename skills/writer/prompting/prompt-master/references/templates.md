> **中文汉化版** · 上游：[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) · 原文件：`references/templates.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 提示词模板参考

Prompt Master 的完整模板库。用户任务类型匹配时，读取对应模板。不要一次性加载全部模板，只读需要的那一个。

## 目录

| 模板 | 适用场景 |
|----------|----------|
| [模板 A — RTF](#template-a--rtf) | 简单的一次性任务 |
| [模板 B — CO-STAR](#template-b--co-star) | 专业文档、商务写作 |
| [模板 C — RISEN](#template-c--risen) | 复杂的多步骤项目 |
| [模板 D — CRISPE](#template-d--crispe) | 创意工作、品牌语气 |
| [模板 E — 可审计推理](#template-e--auditable-reasoning) | 逻辑、数学、分析、调试 |
| [模板 F — Few-Shot](#template-f--few-shot) | 一致的结构化输出、模式复刻 |
| [模板 G — 文件范围](#template-g--file-scope) | Cursor、Windsurf、Copilot 等代码编辑 AI |
| [模板 H — ReAct + 停止条件](#template-h--react--stop-conditions) | Claude Code、Devin 等自主 Agent |
| [模板 I — 视觉描述](#template-i--visual-descriptor) | Midjourney、DALL-E、Stable Diffusion、Sora |
| [模板 J — 参考图编辑](#template-j--reference-image-editing) | 用参考图编辑已有图像 |
| [模板 K — ComfyUI](#template-k--comfyui) | ComfyUI 节点式图像工作流 |
| [模板 L — 提示词反编译](#template-l--prompt-decompiler) | 拆解、适配或拆分已有提示词 |
| [模板 M — 当前 Claude 任务简报](#template-m--current-claude-task-brief) | 当前 Claude 模型上的复杂、多步骤或 agentic 任务 |
| [模板 N — OpenAI 任务简报](#template-n--openai-task-brief) | GPT-6、GPT-6.1 Sol 或显式选择的 GPT-5.6 模型上的复杂任务 |

---

## 模板 A — RTF

*Role、Task、Format。适用于请求清晰简单、需要快速完成的一次性任务。*

```
Role: [One sentence defining who the AI is]
Task: [Precise verb + what to produce]
Format: [Exact output format and length]
```

**示例：**
```
Role: You are a senior technical writer.
Task: Write a one-paragraph description of what a REST API is.
Format: Plain prose, 3 sentences maximum, no jargon, suitable for a non-technical audience.
```

---

## 模板 B — CO-STAR

*Context、Objective、Style、Tone、Audience、Response。适用于专业文档、商务写作、报告，以及需要完整掌控上下文的营销内容。*

```
Context: [Background the AI needs to understand the situation]
Objective: [Exact goal — what success looks like]
Style: [Writing style: formal / conversational / technical / narrative]
Tone: [Emotional register: authoritative / empathetic / urgent / neutral]
Audience: [Who reads this — their knowledge level and expectations]
Response: [Format, length, and structure of the output]
```

**示例：**
```
Context: I am a founder pitching a B2B SaaS tool that automates expense reporting for mid-size companies.
Objective: Write a cold email that gets a reply from a CFO.
Style: Direct and conversational, not salesy.
Tone: Confident but not pushy.
Audience: CFO at a 200-person company, busy, skeptical of vendor emails.
Response: 5 sentences max. Subject line included. No bullet points.
```

---

## 模板 C — RISEN

*Role、Instructions、Steps、End Goal、Narrowing。适用于复杂项目、多步骤任务，以及任何需要明确行动顺序的输出。*

```
Role: [Expert identity the AI should adopt]
Instructions: [Overall task in plain terms]
Steps:
  1. [First action]
  2. [Second action]
  3. [Continue as needed]
End Goal: [What the final output must achieve]
Narrowing: [Constraints, scope limits, what to exclude]
```

**示例：**
```
Role: You are a product manager with 10 years of experience in mobile apps.
Instructions: Write a product requirements document for a habit tracking feature.
Steps:
  1. Define the problem statement in one paragraph
  2. List user stories in the format "As a [user], I want [goal] so that [reason]"
  3. Define acceptance criteria for each story
  4. List out-of-scope items explicitly
End Goal: A PRD that an engineering team can begin sprint planning from immediately.
Narrowing: No technical implementation details. No wireframes. Under 600 words total.
```

---

## 模板 D — CRISPE

*Capacity、Role、Insight、Statement、Personality、Experiment。适用于创意工作、品牌语气写作，以及任何人格、语调和迭代都很重要的任务。*

```
Capacity: [What capability or expertise the AI should have]
Role: [Specific persona to adopt]
Insight: [Key background insight that shapes the response]
Statement: [The core task or question]
Personality: [Tone and style — witty / authoritative / casual / sharp]
Experiment: [Request variants or alternatives to explore]
```

**示例：**
```
Capacity: Expert copywriter specializing in SaaS product launches.
Role: Brand voice for a productivity tool aimed at developers.
Insight: Developers hate marketing speak and respond to honesty and specificity.
Statement: Write the hero headline and sub-headline for the landing page.
Personality: Sharp, dry, confident — no adjectives, no exclamation marks.
Experiment: Give 3 variants ranging from minimal to bold.
```

---

## 模板 E — 可审计推理

*适用于逻辑密集型任务、数学、调试，以及不索取私有推理过程也能核查结果的多因素分析。*

```
[Task statement]

Return:
1. Conclusion
2. Assumptions
3. Evidence or intermediate results needed to audit the conclusion
4. Verification checks performed
5. Remaining uncertainty, if any

Do not reveal hidden chain-of-thought or private reasoning. Keep the rationale concise and decision-relevant.
```

**适用场景：**
- 原因不明显的调试
- 对比不同技术方案
- 需要验证的数学或计算
- 证据与假设必须可查验的分析

**不适用场景：**
- 答案一目了然的简单任务
- 审计记录只会添乱的创意任务

---

## 模板 F — Few-Shot

*适用于输出格式用示例展示比用文字描述更有效的情形。对格式敏感的任务，示例永远胜过书面指令。*

```
[Task instruction]

Here are examples of the exact format needed:

<examples>
  <example>
    <input>[example input 1]</input>
    <output>[example output 1]</output>
  </example>
  <example>
    <input>[example input 2]</input>
    <output>[example output 2]</output>
  </example>
</examples>

Now apply this exact pattern to: [actual input]
```

**规则：**
- 2 到 5 个示例是最佳区间。更多示例很少有帮助，只会浪费 token。
- 示例必须包含边界情况，不能只有简单情形。
- 用 XML 标签包裹示例，Claude 解析 XML 相当可靠。
- 如果同一个格式问题已经反复提示修正两次，改用 few-shot，而不是重写指令。

---

## 模板 G — 文件范围

*适用于 Cursor、Windsurf、GitHub Copilot，以及任何在代码库内编辑代码的 AI。这里最常见的失败模式是改错文件或破坏现有逻辑，本模板两者都能防住。*

```
File: [exact/path/to/file.ext]
Function/Component: [exact name]

Current Behavior:
[What this code does right now — be specific]

Desired Change:
[What it should do after the edit — be specific]

Scope:
Only modify [function / component / section].
Do NOT touch: [list everything to leave unchanged]

Constraints:
- Language/framework: [specify version]
- Do not add dependencies not in [package.json / requirements.txt]
- Preserve existing [type signatures / API contracts / variable names]

Done When:
[Exact condition that confirms the change worked correctly]
```

---

## 模板 H — ReAct + 停止条件

*适用于 Claude Code、Devin、AutoGPT，以及任何会自主执行动作的 AI。失控循环与范围膨胀是 agentic 工作流中最烧额度的两个杀手，停止条件不是可选项。*

```
Objective:
[Single, unambiguous goal in one sentence]

Starting State:
[Current file structure / codebase state / environment]

Target State:
[What should exist when the agent is done]

Allowed Actions:
- [Specific action the agent may take]
- Install only packages listed in [requirements.txt / package.json]

Forbidden Actions:
- Do NOT modify files outside [directory/scope]
- Do NOT run the dev server or deploy
- Do NOT push to git
- Do NOT delete files without showing a diff first
- Do NOT make architecture decisions without human approval

Stop Conditions:
Pause and ask for human review when:
- A file would be permanently deleted
- A new external service or API needs to be integrated
- Two valid implementation paths exist and the choice affects architecture
- An error cannot be resolved in 2 attempts
- The task requires changes outside the stated scope

Checkpoints:
After each major step, output: ✅ [what was completed]
At the end, output a full summary of every file changed.
```

---

## 模板 I — 视觉描述

*适用于 Midjourney、DALL-E 3、Stable Diffusion、Sora、Runway，以及任何图像或视频生成工具。*

```
Subject: [Main subject — specific, not vague]
Action/Pose: [What the subject is doing]
Setting: [Where the scene takes place]
Style: [photorealistic / cinematic / anime / oil painting / vector / etc.]
Mood: [dramatic / serene / eerie / joyful / etc.]
Lighting: [golden hour / studio / neon / overcast / candlelight / etc.]
Color Palette: [dominant colors or named palette]
Composition: [wide shot / close-up / aerial / Dutch angle / etc.]
Aspect Ratio: [16:9 / 1:1 / 9:16 / 4:3]
Negative Prompts: [blurry, watermark, extra fingers, distortion, low quality]
Style Reference: [artist / film / aesthetic reference if applicable]
```

**各工具专用语法：**
- **Midjourney**: 用逗号分隔的描述词，不要写成散文。结尾追加 `--ar`、`--style`、`--v 6`。
- **Stable Diffusion**: 使用 `(word:1.3)` 权重语法。CFG 值取 7 到 12。负面提示词必须提供。
- **DALL-E 3**: 散文式描述效果很好。除非需要文字，否则加上 "do not include any text in the image"。
- **Sora / 视频**: 写明运镜方式（慢速推轨、固定机位、升降摇臂）、以秒计的时长和剪辑风格。

---

## 模板 J — 参考图编辑

*适用于用户想修改一张已有图像的情形。与生成完全不同：永远不要从零描述整个场景，只描述要改的部分。*

**写提示词之前，务必先告诉用户：**
"发送此提示词前，请先把你的参考图附到 [tool name] 上。"

**先探测该工具的编辑能力：**
- Midjourney: 用 `--cref [image URL]` 做角色参考，或用 `--sref` 做风格参考
- DALL-E 3: 用 Edit 端点，不要用 Generate 端点。用户必须在 ChatGPT 中并启用图像编辑
- Stable Diffusion: 用 img2img 模式，不要用 txt2img。把去噪强度设为 0.3-0.6 以保留原图

```
Reference image: [attached / URL]
What to keep exactly the same: [list everything that must not change]
What to change: [specific edit only — be precise]
How much to change: [subtle / moderate / significant]
Style consistency: maintain the exact style, lighting, and mood of the reference
Negative prompt: [what to avoid introducing]
```

**示例：**
```
Reference image: [attached portrait photo]
What to keep exactly the same: face, hair, clothing, background, lighting
What to change: head angle — rotate from facing left to facing straight forward
How much to change: subtle, preserve all facial features exactly
Style consistency: maintain photorealistic style, same lighting direction
Negative prompt: no new elements, no style changes, no background changes
```

---

## 模板 K — ComfyUI

*适用于 ComfyUI 节点式工作流。务必把正向提示词与负面提示词分成两个独立区块输出。动笔前先问清 checkpoint 模型，各模型的语法与 token 上限不同。*

**未说明时先问：**
"你用的是哪个 checkpoint 模型？（SD 1.5、SDXL、Flux 还是其他）"

**各模型注意事项：**
- SD 1.5: 提示词更短效果更好，每块不超过 75 个 token，使用 (word:weight) 语法
- SDXL: 能容纳更长的提示词，加权语法之外还支持更多自然语言
- Flux: 自然语言效果好，对加权语法依赖更少，对风格描述的响应非常灵敏

```
POSITIVE PROMPT:
[subject], [style], [mood], [lighting], [composition], [quality boosters: highly detailed, sharp focus, 8k]

NEGATIVE PROMPT:
[what to exclude: blurry, low quality, watermark, extra limbs, bad anatomy, distorted, oversaturated]

CHECKPOINT: [model name]
SAMPLER: Euler a (recommended starting point)
CFG SCALE: 7 (increase for stricter prompt adherence)
STEPS: 20-30
RESOLUTION: [width x height — must be divisible by 64]
```

---

## 模板 L — 提示词反编译

*适用于用户粘贴一段已有提示词，想拆解它、为其他工具适配它、简化它，或理解其结构的情形。这是分析与适配，不是从零构建。*

**先判断需要哪种反编译任务：**
- **Break down**：解释提示词各部分的作用
- **Adapt**：为其他工具重写，同时保留原意
- **Simplify**：去除冗余、收紧表达，不损失含义
- **Split**：把复杂的一次性提示词拆分成更清晰的顺序提示词

**Adapt 任务务必先问：**
"原始提示词来自哪个工具？你要适配到哪个工具？"

**Break down 输出格式：**
```
Original prompt: [paste]

Structure analysis:
- Role/Identity: [what role is assigned and why]
- Task: [what action is being requested]
- Constraints: [what limits are set]
- Format: [what output shape is expected]
- Weaknesses: [what is missing or could cause wrong output]

Recommended fix: [rewritten version with gaps filled]
```

**Adapt 输出格式：**
```
Original ([source tool]): [original prompt]

Adapted for [target tool]:
[rewritten prompt using target tool syntax and best practices]

Key changes made:
- [change 1 and why]
- [change 2 and why]
```

**Split 输出格式：**
```
Original prompt: [paste]

This prompt is doing [N] things. Split into [N] sequential prompts:

Prompt 1 — [what it handles]:
[prompt block]

Prompt 2 — [what it handles]:
[prompt block]

Run these in order. Each output feeds the next.
```
---

## 模板 M — 当前 Claude 任务简报

*适用于当前 Claude 模型（Claude.ai、API 或 Claude Code）上的复杂、多步骤或 agentic 任务。它把结果、上下文、范围和行动边界前置，同时避开已过时的手动思考脚手架。*

```
## Objective
[What needs to be built, fixed, or produced — one clear sentence. Add WHY if it affects approach.]

## Context
[What exists now — relevant files, current behavior, stack already in place, what was tried and failed]

## Target State
[What done looks like — specific files changed, behavior produced, tests passing. Binary where possible.]

## Scope
- Work only in: [specific files and directories]
- Do NOT touch: [forbidden files — .env, package-lock.json, configs, anything outside scope]

## Constraints
- [Stack version, naming conventions, no new dependencies without asking]
- Only make changes directly requested. Do not add features, abstractions, or files beyond what was asked.

## Acceptance Criteria
- [ ] [Binary check 1]
- [ ] [Binary check 2]
- [ ] [Binary check 3]

## Action Boundaries
- Proceed with reversible, in-scope inspection, edits, and validation.
- Stop and ask before destructive or irreversible actions, external writes, purchases, material scope expansion, or decisions that require user-only input.

## Progress Evidence
For long-running work, report progress only when it changes or when a checkpoint is reached. Ground every completion claim in a tool result, changed artifact, or verification output.
```

**Effort**：在 API 或 Harness 中配置，而不是在提示词里索取私有推理过程。从模型默认值起步，常规的范围明确工作调低，仅当任务难度配得上这笔成本时才调高。

**仅限 Claude Code**，相关时附加 Session Strategy 区块：
```
## Session Strategy
[Pick one:]
- New session — unrelated to prior context, start fresh
- Continue — prior context still needed
- Subagent — delegate only [independent, sizeable workstream], with a bounded deliverable
- Compact first — compact around [decisions, constraints, and current state], then begin
```

**适用场景：** 任意界面上的当前 Claude 模型，任务复杂、多文件、有歧义或 agentic 时使用。简单的一次性任务不需要。

---

## 模板 N — OpenAI 任务简报

*适用于在 ChatGPT、Codex 或 API 中面向 OpenAI 模型的复杂任务。简单请求保持简短，省略不影响结果的区块。*

```text
Goal:
[The concrete result to deliver.]

Context:
[Relevant inputs, current state, prior decisions, and failed attempts.]

Constraints:
[Scope, requirements, compatibility, and limits.]

Actions:
[For tool-based tasks: available tools, actions already authorized,
and actions requiring additional approval.]

Done:
[Observable acceptance criteria and appropriate verification.]

Output:
[Deliverable, format, level of detail, and required evidence.]
```

**适配启发式（在代表性任务上评估）：**
- Luna: 收窄任务，并让输出契约明确。
- Sol: 强调实现上下文与验收标准。
- Astra: 为困难工作加入决策标准与证据要求。
- 保留显式选择的 GPT-5.6 模型，并在 SKILL.md 中应用其兼容性指引。
- 相关任务共享同一结果时合并；当依赖关系、审查检查点或上下文限制足以支持分开运行时拆分。
- 索取结论、假设、简要依据、证据与核查项，而不是隐藏的思维链。
- 涉及最新事实时，若环境提供检索与引用能力就加以使用；缺少访问权限要如实披露，而不是编造来源。
- 只为 agentic 任务定义工具访问与授权。长任务索要里程碑与阻塞点，而不是每个动作之后都发一条消息。
- 把 API 与 Harness 设置写进提示词之外的配置说明。针对确切的模型、端点与界面验证受支持的控制项。

任务简报与适配启发式是 Prompt Master 的建议，不是 OpenAI 官方模板或基准测试结果。
