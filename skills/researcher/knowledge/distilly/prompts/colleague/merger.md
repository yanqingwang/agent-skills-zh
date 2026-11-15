> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/colleague/merger.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 增量合并提示词

## 任务

你会收到：
1. 已有的 `work.md` 内容
2. 已有的 `persona.md` 内容
3. 新素材（文件或消息）

你的任务是判断每条新内容应更新哪一部分，并输出增量更新。

**原则：只追加增量；绝不覆盖已有结论。有冲突就输出冲突提示，交给用户决定。**

---

## Step 1: 分类

给新内容里的每条信息分类：

| 信息类型 | 归入 |
|---------|------|
| 技术标准、代码风格、API 设计、工作流 | → work.md |
| 业务知识、系统职责、技术结论 | → work.md |
| 沟通风格、口头禅、表达习惯 | → persona.md |
| 决策行为、人际关系、情绪模式 | → persona.md |
| 两者都涉及 | → 分别归入各自文件 |

---

## Step 2: 检查冲突

把新内容与已有内容对照：

- 新内容是对已有信息的**补充**（新细节） → 直接追加
- 新内容**印证**已有信息 → 忽略（不要重写一遍）
- 新内容与已有信息**矛盾** → 输出冲突提示：

```
⚠️ Conflict found:
- Existing: {existing description}
- New finding: {new content description}
- Source: {file name/time}

Suggestion: [keep existing / update to new content / keep both and mark with timestamps]
Please let the user decide.
```

---

## Step 3: 生成更新补丁

更新 `work.md` 时使用以下输出格式：
```
=== work.md updates ===

[Append to "Technical Standards/Naming Conventions" section]
- {new content}

[Append to "Knowledge Base" section]
- {new knowledge conclusion}

[No updates] or [The sections above have updates]
```

更新 `persona.md` 时使用以下输出格式：
```
=== persona.md updates ===

[Append to "Layer 2/Catchphrases and Frequent Words" section]
- New catchphrase: "{xxx}"

[Append to "Layer 4/With Peers" section]
- {new behavior description}

[No updates] or [The sections above have updates]
```

---

## Step 4: 生成更新摘要

向用户展示：
```
Update summary:
- work.md: appended {N} new items ({brief description})
- persona.md: appended {N} new items ({brief description})
- Found {N} conflicts that need your confirmation (see above)

Version will be bumped from {vN} to {vN+1}.
Apply the updates?
```
