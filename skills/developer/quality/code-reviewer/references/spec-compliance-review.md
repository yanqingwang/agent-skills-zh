> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/code-reviewer/references/spec-compliance-review.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 规格符合性审查

---

## 两阶段审查架构

```
                    ┌─────────────────────┐
                    │   Implementation    │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  STAGE 1: Spec      │
                    │  Compliance Review  │
                    └──────────┬──────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                  │
      ┌───────▼───────┐                ┌────────▼────────┐
      │   ✗ Issues    │                │   ✓ Compliant   │
      │     Found     │                │                 │
      └───────┬───────┘                └────────┬────────┘
              │                                  │
              │                        ┌────────▼────────┐
              │                        │  STAGE 2: Code  │
              │                        │  Quality Review │
              │                        └────────┬────────┘
              │                                  │
              │                    ┌─────────────┴─────────────┐
              │                    │                           │
              │            ┌───────▼───────┐         ┌────────▼────────┐
              │            │   ✗ Issues    │         │   ✓ Approved    │
              │            │     Found     │         │                 │
              │            └───────┬───────┘         └─────────────────┘
              │                    │
              └────────────────────┴────────────────────┐
                                                        │
                                              ┌─────────▼─────────┐
                                              │ Return to Author  │
                                              └───────────────────┘
```

**关键：** 先完成阶段 1（规格符合性），再进入阶段 2（代码质量）。绝不为不满足规格的功能做代码质量审查。

---

## 阶段 1：规格符合性审查

### 核心指令

> "实现者完成得快得可疑。其报告可能不完整、不准确，或过于乐观。"

以专业怀疑态度对待每次审查。独立验证各项声明。

### 三类验证

#### 类别 1：缺失的需求

**检查已要求但未实现的功能。**

| 问题 | 如何验证 |
|----------|---------------|
| 是否跳过了要求的功能？ | 将 PR 与原始需求逐行比对 |
| 边界情况是否处理？ | 检查错误路径、空状态、边界值 |
| 错误场景是否处理？ | 查找 try/catch、错误边界、校验 |
| 主路径是否完整？ | 手动走查主用例 |

```markdown
## Example Review Finding

**Missing Requirement:** Issue #42 requested "password must be at least 8 characters"

**Found in code:**
```typescript
// No length validation present
function validatePassword(password: string) {
  return password.length > 0;  // Only checks non-empty
}
```

**Status:** ❌ Incomplete - minimum length validation missing
```

#### 类别 2：多余的添加

**检查范围蔓延与过度设计。**

| 问题 | 如何验证 |
|----------|---------------|
| 功能超出规格？ | 与原始需求比对 |
| 过度设计？ | 复杂度是否有需求支撑？ |
| 过早优化？ | 是否没有测量数据就谈性能？ |
| 未被要求的抽象？ | 是否有只为单次使用而建的 helper/工具函数？ |

```markdown
## Example Review Finding

**Unnecessary Addition:** Added caching layer not in requirements

**Found in code:**
```typescript
// Original requirement: "Fetch user by ID"
// Actual implementation:
class CachedUserRepository {  // Not requested
  private cache = new Map();
  private ttl = 60000;

  async getUser(id: string) {
    if (this.cache.has(id)) { ... }
    // 50 lines of cache logic
  }
}
```

**Status:** ⚠️ Scope creep - discuss before merging
```

#### 类别 3：理解偏差

**检查对需求的误解。**

| 问题 | 如何验证 |
|----------|---------------|
| 对需求的理解不同？ | 请作者解释其理解 |
| 假设未澄清？ | 查找类似 "assuming..." 的注释 |
| 含糊的规格是否解决错了？ | 与类似的现有功能比对 |

```markdown
## Example Review Finding

**Interpretation Gap:** "Sort by date" implemented as ascending

**Requirement stated:** "Sort by date" (ambiguous)

**Author implemented:** Oldest first (ascending)

**Expected:** Most recent first is typical UX pattern

**Status:** ❓ Clarify - which sort order was intended?
```

---

## 顺序为何重要

### 阶段 1 必须先行

| 场景 | 顺序错误造成的浪费 |
|----------|------------------------|
| 跳过阶段 1 | 审查了 500 行代码质量，然后发现做错了功能 |
| 先做阶段 2 | 建议了重构，然后意识到这段代码本不该存在 |
| 两者混做 | 关注点混杂，遗漏系统性问题 |

### 关注点分离

- **阶段 1（规格）：** 做的是正确的事吗？
- **阶段 2（质量）：** 把事情做对了吗？

如果代码没有实现正确的功能，代码质量审查毫无意义。

---

## 规格符合性检查清单

### 开始之前

- [ ] 完整阅读原始 issue/工单
- [ ] 识别所有显式需求
- [ ] 从上下文识别隐式需求
- [ ] 记录列出的所有验收标准

### 审查过程中

**缺失的需求：**
- [ ] 所需功能全部存在
- [ ] 边界情况已覆盖（空、null、最大值）
- [ ] 按规格处理错误
- [ ] 主路径完全可用
- [ ] 如有设计稿/规格，UI 与之匹配

**多余的添加：**
- [ ] 没有未被要求的功能
- [ ] 没有投机性抽象
- [ ] 没有过早优化
- [ ] 范围与需求完全一致

**理解偏差：**
- [ ] 作者的理解与规格一致
- [ ] 含糊之处解决正确
- [ ] 假设已记录且成立
- [ ] 行为与类似现有功能一致

### 审查之后

- [ ] 记录所有发现，附 file:line 引用
- [ ] 归类为缺失/多余/理解偏差
- [ ] 分优先级：阻塞 vs 非阻塞问题

---

## 输出格式

### 符合规格的结果

```markdown
## Spec Compliance Review: ✅ PASS

All requirements verified:
- ✅ User can upload profile image (req #1)
- ✅ Image resized to 200x200 (req #2)
- ✅ Invalid formats rejected with error message (req #3)
- ✅ Progress indicator during upload (req #4)

**Proceed to:** Code Quality Review
```

### 发现问题

```markdown
## Spec Compliance Review: ❌ ISSUES FOUND

### Missing Requirements

1. **Progress indicator not implemented** (req #4)
   - File: `ProfileUpload.tsx`
   - Expected: Progress bar during upload
   - Found: No progress indication

2. **Error messages not user-friendly** (req #3)
   - File: `ProfileUpload.tsx:45`
   - Expected: "Please upload a JPG or PNG file"
   - Found: "Error: INVALID_FORMAT"

### Unnecessary Additions

1. **Image cropping feature not requested**
   - File: `ImageCropper.tsx` (new file, 150 lines)
   - Impact: Adds complexity, delays delivery
   - Recommendation: Remove or create separate PR

**Action Required:** Address missing requirements before code quality review
```

---

## 要避免的常见错误

| 错误 | 为什么不对 |
|---------|----------------|
| 先审代码风格，再审规格符合性 | 如果做的就不是对的东西，努力白费 |
| 假定规格已被遵守 | 要独立验证 |
| 跳过边界情况 | Bug 藏在边界里 |
| 接受"以后再加" | 技术债会累积 |
| 漏掉范围蔓延 | 未审查的代码进入代码库 |

---

*内容改编自 Jesse Vincent（@obra）的 [obra/superpowers](https://github.com/obra/superpowers)，MIT License。*
