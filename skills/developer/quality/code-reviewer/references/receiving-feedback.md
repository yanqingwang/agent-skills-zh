> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/code-reviewer/references/receiving-feedback.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 接收反馈

---

## 核心心态

> "先验证，再实现。先提问，再假设。技术正确性优先于社交舒适。"

代码审查反馈是技术讨论，不是社交讨论。关注代码本身，不关注情绪。

---

## 六步流程

### Step 1: 完整阅读

**先不做反应。** 在形成任何回应之前，读完整条评论。

```markdown
❌ BAD: Read first sentence → start typing defense
✅ GOOD: Read entire comment → understand full context → then respond
```

### Step 2: 复述需求

用自己的话复述审查者的反馈，确认理解无误。

```markdown
Reviewer: "This function is doing too much. It handles validation,
transformation, and persistence all in one place."

Your restatement: "You're suggesting I split this into three separate
functions: validate(), transform(), and persist()?"
```

### Step 3: 对照代码库核实

在回应之前，对照真实代码情况验证反馈。

```typescript
// Reviewer says: "This will throw if user is null"

// Check the code:
function getUsername(user: User): string {
  return user.name;  // No null check - reviewer is correct
}

// Or discover context:
function getUsername(user: User): string {
  return user.name;  // TypeScript enforces User, null not possible
}
```

### Step 4: 评估技术合理性

考虑这条反馈是否适用于你的具体技术栈和上下文。

```markdown
Reviewer: "You should use useMemo here for performance"

Evaluate:
- Is this component re-rendering frequently? → Check React DevTools
- Is the computation expensive? → Profile it
- Does React 19's compiler auto-optimize this? → Check version
```

### Step 5: 有实质地回应

给出技术性确认，或有理有据的反驳。

```markdown
✅ GOOD: "Fixed. Split into validate(), transform(), persist()
         at lines 24, 45, 67."

✅ GOOD: "Respectfully disagree. This list has max 5 items
         (see schema.ts:12), so filter performance is O(5)."

❌ BAD: "You're absolutely right! Great catch!"
❌ BAD: "I don't think that's necessary."
```

### Step 6: 逐条实现

逐条处理每项反馈，并逐条验证。

```markdown
Feedback item 1: Add null check
→ Implement → Test → Commit → Verify → Move to next

Feedback item 2: Extract helper function
→ Implement → Test → Commit → Verify → Move to next

NOT: Try to address all feedback in one massive commit
```

---

## 避免"表演式认同"

### 问题所在

表演式的认同浪费时间，也不提供任何信息。当你写下"好观点！"时，你只是在增加噪音，不是在增加信号。

### 禁用短语

| 短语 | 为什么错 |
|--------|----------------|
| "你说得太对了！" | 谄媚，不提供信息 |
| "好观点！" | 空洞夸奖，不是回应 |
| "反馈太棒了！" | 奉承，不是投入讨论 |
| "谢谢你发现这个问题！" | 多余，直接修就行 |
| "我非常感谢……" | 社交客套，不涉技术 |

### 行动证明理解

```markdown
❌ "You're absolutely right! Great catch on that null check!
    Thanks so much for pointing this out!"

✅ "Fixed. Added null check at line 42."
```

代码改动表明你理解了。语言是多余的。

### 何时简短致谢是合适的

学到新东西时，简短、技术性的致谢是合适的：

```markdown
✅ "I wasn't aware of that edge case. Added handling at line 42."
✅ "Good point about thread safety. Added mutex at line 67."
```

---

## 何时反驳

### 反驳的正当理由

当反馈出现以下情况时，用技术理由反驳：

| 情况 | 如何回应 |
|-----------|----------------|
| 会破坏现有功能 | "这个改动会破坏功能 X（见 tests/feature-x.spec.ts:34 的测试）" |
| 缺少完整的代码库上下文 | "这个模式存在是因为 Y（见 architecture.md#constraints）" |
| 违反 YAGNI | "目前不需要这种灵活性，只有一个调用方" |
| 技术上不正确 | "这实际上能工作，因为 Z（附文档链接）" |
| 与既有架构冲突 | "这与我们的 JWT 方案冲突（见 auth/README.md）" |

### 好的反驳格式

```markdown
## Template
This conflicts with [X]. [Evidence]. Was that the intent, or should we [alternative]?

## Example
This conflicts with our JWT authentication architecture (see auth/token.js:45).
Switching to sessions would require restructuring the API middleware.
Was that the intent, or should we keep JWT?
```

### 糟糕的反驳

```markdown
❌ "I don't think that's right."
❌ "That won't work."
❌ "We've always done it this way."
❌ "That's too much work."
```

---

## 宣称修复之前的验证

### 清单

写下"已修复"或"完成"之前：

- [ ] 改动已实现
- [ ] 测试通过（完整测试套件，不只是改动的文件）
- [ ] 反馈中提到的具体行为已验证
- [ ] 边界情况已测试
- [ ] 没有引入意外的副作用

### 可接受的回应

```markdown
✅ "Fixed. Added null check. Tests pass."
✅ "Fixed at line 42. Verified with test case X."
✅ "Implemented. All 47 tests pass."
```

### 不可接受的回应

```markdown
❌ "I think this addresses your concern."
❌ "Should be fixed now."
❌ "Done, I believe."
❌ "Fixed (probably)."
```

### 无法验证时

如果无法验证修复：

```markdown
✅ "Implemented the change, but I'm unable to verify because
    [specific reason]. Can you confirm on your end?"
```

---

## 速查表

| 情况 | 回应 |
|-----------|----------|
| 审查者正确 | "已修复。[你改了什么]。" |
| 你需要澄清 | "确认一下：你是建议[复述]吗？" |
| 审查者不正确 | "这能工作是因为[证据]。[证明链接]。" |
| 你不同意方案 | "这与 [X] 冲突。是否应该[替代方案]？" |
| 你学到了新东西 | "我此前不知道 [X]。已在第 [N] 行修复。" |
| 你无法验证 | "已实现。无法验证，因为[原因]。" |

---

## 反模式

| 模式 | 问题 | 修复 |
|---------|---------|-----|
| 防御性回应 | 制造冲突，浪费时间 | 假设对方善意，用技术方式回应 |
| 道歉式回应 | 不专业，增加噪音 | 直接修 |
| 延迟回应 | 阻塞审查循环 | 几小时内回应，而不是几天 |
| 模糊回应 | 让审查者拿不准 | 具体说明改动 |
| 忽略反馈 | 不尊重，制造摩擦 | 逐条回应 |

---

*内容改编自 [obra/superpowers](https://github.com/obra/superpowers)（作者 Jesse Vincent (@obra)），MIT License。*
