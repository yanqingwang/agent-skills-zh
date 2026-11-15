> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/relationship/intake.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 关系型信息收集提示词

## 目标

用 3 轮对话收集蒸馏关系型 Skill 所需的最小上下文：

1. 基本信息
2. 一段最亲近的记忆
3. 可用的素材

这个分支适用于亲密或本人熟识的关系：父母、朋友、前任、兄弟姐妹、导师，或任何对用户情感上重要的人。

---

## 开场白

```text
I’ll help you create a relationship-based Skill. We’ll do this in 3 short turns.
Everything is skippable.
```

---

## Turn 1: 基本信息

这些问题放在一条消息里一起问：

```text
First, give me the basic profile of this person.

1. What should I call them?
2. What is their relationship to you?
3. What is your current status with them?
4. What basic information do you know about them? For example: gender, MBTI, zodiac, age range.
5. Roughly how long has it been since you last saw them or had meaningful contact?
```

记录：
- 展示名
- 别名
- slug 候选
- 关系子类型
- 当前状态
- 结构化画像线索
- 疏远程度或断联时长

---

## Turn 2: 一段最亲近的记忆

```text
Now tell me one memory that feels closest to this person.

- What happened?
- What did they say or do?
- Why does this moment still stay with you?

It does not need to be polished. A rough memory is enough.
```

记录：
- 场景锚点
- 语气与节奏
- 情绪触发点
- 冲突或关心模式
- 难忘的话或行为
- 为什么这段记忆能定义这个人

---

## Turn 3: 素材

```text
What materials can you provide for this person?

- chat history
- screenshots
- photos
- voice-note transcripts
- diary entries or memory notes
- no files, only memory

If you upload files, save them under this skill’s `knowledge/` folders before analyzing them.
For WeChat chat history import, you can try WeFlow first.
```

记录：
- 可用的素材类型
- 是否上传了文件
- 素材应放进哪个文件夹

---

## 输出摘要

```text
Summary:

  Name: {name}
  Relationship: {relationship_subtype}
  Status: {current_status}
  Basic profile: {profile_summary}
  Closest memory: {memory_summary}
  Materials: {source_summary}

Confirm? (confirm / edit [field])
```
