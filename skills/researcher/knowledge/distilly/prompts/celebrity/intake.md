> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/celebrity/intake.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 名人信息采集提示词

## 目标

收集足够的信息来启动“研究先行”的名人蒸馏工作流，同时主动帮助那些不确定要蒸馏谁、也不确定自己需要什么的用户。

---

## 入口路由

识别用户意图并据此路由：

### 直接路径

用户点名具体人物（例如“蒸馏 Paul Graham”、“做一个张一鸣 skill”）。

→ 直接进入下方的 Q1 到 Q5。

### 诊断路径

用户描述了模糊需求但没有点名人物（例如“我想要一个擅长产品思考的人”、“我需要有人帮我做投资决策”）。

→ 在 Q1 之前先跑诊断子流程。

---

## 诊断子流程（仅在未点名具体人物时）

### 第 1 轮：确定维度

```text
You haven't named a specific person. Let me help you find the right one.

What kind of thinking do you need help with?

Examples:
- Product decisions and taste
- Investment and risk judgment
- Engineering and systems design
- Communication and persuasion
- Creative writing and storytelling
- Management and team building
- Scientific thinking and explanation
```

记录：
- 领域 / 思考维度
- 用户是否偏好特定年代、文化或语言

### 第 2 轮：收窄并推荐

根据用户的维度，推荐 2 至 3 位候选。优先考虑：
1. 系统里已蒸馏为现有 Skill 的人物
2. 公开材料充足的人物（书籍、长访谈、有记录的决策）
3. 思维足够独特、能产出高质量 Skill 的人物

```text
Based on what you described, here are some candidates:

1. {Name A} — {one-line reason}
2. {Name B} — {one-line reason}
3. {Name C} — {one-line reason}

Who sounds right? Or name someone else.
```

用户选定后，进入 Q1。

---

## 开场（直接路径）

```text
I'll help you distill a public figure into a Skill. Answer 5 questions. Every question except Q1 is skippable.
```

---

## 问题

### Q1：是谁

```text
Who do you want to distill?

Examples:
- Steve Jobs
- Naval Ravikant
- Zhang Yiming
- Charlie Munger
- Richard Feynman
```

记录：
- 规范姓名
- 别名
- 可能的语言 / 地区
- 此人是知名人物（材料充足）还是相对冷门

### Q2：为什么选这个人

```text
What do you want from this person's Skill?

Examples:
- how they make decisions
- how they think about products
- how they explain complex ideas
- how they judge people and tradeoffs
- how they approach risk and uncertainty
```

记录：
- 使用场景
- 期望的视角 / 关注领域
- 输出偏向：策略 / 表达 / 讲解 / 判断 / 创造

### Q3：有哪些已知材料

```text
Do you already have source material? Books, interviews, talks, posts, podcasts, articles, screenshots — anything is fine.

If you have local files (PDF, transcripts, subtitle files, screenshots), mention them now.
```

记录：
- 本地材料（用户能直接提供的文件）
- 具体已知来源的 URL
- 按标题记录已知的书籍 / 演讲 / 访谈
- 是否应以本地优先（local-first）模式运行

### Q4：采集策略

根据 Q3，确定并确认采集策略：

```text
Based on what you've told me, I'll use this collection approach:

  [A] Local-first: You have substantial local material. I'll analyze that first,
      then only search the web for missing dimensions.

  [B] Web + local: You have some material. I'll combine it with web research.

  [C] Web-only: No local material. I'll do a full web research pass.

Sound right? (confirm / change)
```

三种策略决定 Phase 1 研究如何分配精力：
- **本地优先（local-first）**：先分析已有材料，盘点 6 个维度中哪些已覆盖，只对缺口搜索网络
- **网络 + 本地（web+local）**：先跑完整的 6 维度网络研究，再与本地材料合并，重叠处以本地材料为 ground truth
- **仅网络（web-only）**：标准的 6 维度网络研究轮

### Q5：研究深度

```text
Which research profile?

- budget-friendly: faster, lighter, 3-track minimum
- budget-unfriendly: slower, deeper, 6-track with audit + synthesis + validation gates

Default: budget-friendly
```

记录：
- 用户选择的研究档位
- 用户更看重速度还是置信度

---

## 冷门人物检测

Q1 之后，估计此人的公开材料是否充足。

冷门人物的信号：
- 没有维基百科条目，或条目极短
- 没有出版书籍或长篇访谈
- 只在社交媒体有存在感
- 用户说不出具体作品或演讲

如果判定为冷门人物：

```text
⚠️ Note: {name} appears to have limited public material.

This means:
- Mental models will be limited to 2–3 (instead of 3–7)
- Some dimensions may be marked as "based on limited information"
- The honest boundaries section will be larger than usual

This is fine — an honest 60-point Skill beats a fabricated 90-point one.

Continue? (yes / switch to someone else)
```

---

## 输出摘要

```text
Summary:

  Person: {name}
  Region/Language: {region}
  Main goal: {goal}
  Known sources: {source_summary}
  Collection strategy: {local-first / web+local / web-only}
  Research profile: {research_profile}
  Cold figure: {yes/no}

Confirm? (confirm / edit [field])
```
