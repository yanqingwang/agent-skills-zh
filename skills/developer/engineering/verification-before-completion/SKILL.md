---
name: verification-before-completion
description: 在即将宣称工作已完成、已修复或已通过时、在 commit 或创建 PR 之前使用——要求先运行验证命令并确认输出，然后才能做出任何成功断言；永远先证据后断言
---

> **中文汉化版** · 上游：[obra/superpowers](https://github.com/obra/superpowers) · 原文件：`skills/verification-before-completion/SKILL.md` · License: MIT
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 完成前的验证

## 概述

**核心原则：** 永远先证据，后断言。

**违反这条规则的字面，就是违反这条规则的精神。**

## 铁律

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

如果你没有在本条消息中运行过验证命令，你就不能宣称它通过。

## 闸门函数

```
BEFORE claiming any status or expressing satisfaction:

1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
   - If NO: State actual status with evidence
   - If YES: State claim WITH evidence
5. ONLY THEN: Make the claim

Skip any step = lying, not verifying
```

## 常见失败

| 断言 | 需要 | 不算数 |
|-------|----------|----------------|
| 测试通过 | 测试命令输出：0 个失败 | 之前的运行、"应该会通过" |
| linter 干净 | linter 输出：0 个错误 | 部分检查、外推推断 |
| 构建成功 | 构建命令：exit 0 | linter 通过、日志看起来不错 |
| bug 已修复 | 测试原始症状：通过 | 代码改了，想当然认为修好了 |
| 回归测试有效 | 红-绿循环已验证 | 测试通过了一次 |
| Agent 完成任务 | VCS diff 显示有改动 | Agent 自报"success" |
| 需求已满足 | 逐条核对清单 | 测试通过 |

## 红色信号——停下

- 使用"应该"、"大概"、"看起来"
- 在验证之前表达满足（"太好了！"、"完美！"、"搞定了！"等）
- 没有验证就准备 commit/push/PR
- 轻信 Agent 的成功报告
- 依赖部分验证
- 想着"就这一次"
- 累了，想赶紧收工
- **任何在没运行验证的情况下暗示成功的措辞**

## 合理化防御

| 借口 | 现实 |
|--------|---------|
| "现在应该能跑了" | 去运行验证 |
| "我很有信心" | 信心 ≠ 证据 |
| "就这一次" | 没有例外 |
| "linter 通过了" | linter ≠ 编译器 |
| "Agent 说成功了" | 独立验证 |
| "我累了" | 疲劳 ≠ 借口 |
| "部分检查就够了" | 部分什么也证明不了 |
| "换个说法规则就不适用了" | 精神高于字面 |

## 关键模式

**测试：**
```
✅ [Run test command] [See: 34/34 pass] "All tests pass"
❌ "Should pass now" / "Looks correct"
```

**回归测试（TDD 红-绿）：**
```
✅ Write → Run (pass) → Revert fix → Run (MUST FAIL) → Restore → Run (pass)
❌ "I've written a regression test" (without red-green verification)
```

**构建：**
```
✅ [Run build] [See: exit 0] "Build passes"
❌ "Linter passed" (linter doesn't check compilation)
```

**需求：**
```
✅ Re-read plan → Create checklist → Verify each → Report gaps or completion
❌ "Tests pass, phase complete"
```

**Agent 委派：**
```
✅ Agent reports success → Check VCS diff → Verify changes → Report actual state
❌ Trust agent report
```

## 何时应用

**永远在以下动作之前：**
- 任何形式的成功/完成断言
- 任何满足感的表达
- 任何关于工作状态的正面陈述
- commit、创建 PR、宣布任务完成
- 进入下一个任务
- 委派给 Agent

**规则同样约束：**
- 精确措辞
- 转述和近义词
- 对成功的暗示
- 任何暗示完成/正确的沟通
