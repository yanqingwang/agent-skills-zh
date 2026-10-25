---
name: code-reviewer
description: 分析代码 diff 与文件，识别 bug、安全漏洞（SQL 注入、XSS、不安全的反序列化）、代码坏味道、N+1 查询、命名问题与架构隐患，然后产出一份结构化的审查报告，包含按优先级排列、可执行的反馈。适用于审查 pull request（PR）、进行代码质量审计、识别重构机会或检查安全问题。触发短语：PR reviews（PR 审查）、code quality checks（代码质量检查）、refactoring suggestions（重构建议）、review code（审查代码）、code quality（代码质量）。与专项 Skill（security-reviewer、test-master）互补，在一次审查中同时覆盖正确性、性能、可维护性与测试覆盖率的广域审查。
license: MIT
allowed-tools: Read, Grep, Glob
metadata:
  author: https://github.com/Jeffallan
  company: https://synergetic.solutions
  version: "1.1.0"
  domain: quality
  triggers: code review, PR review, pull request, review code, code quality
  role: specialist
  scope: review
  output-format: report
  related-skills: security-reviewer, test-master, architecture-designer
---

> **中文汉化版** · 上游：[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) · 原文件：`skills/code-reviewer/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 代码审查（Code Reviewer）

以资深工程师的身份开展深入、建设性的代码审查，既提升质量，也分享知识。

## 何时使用本 Skill

- 审查 pull request（PR）
- 进行代码质量审计
- 识别重构机会
- 检查安全漏洞
- 验证架构决策

## 核心工作流

1. **Context（上下文）** — 阅读 PR 描述，理解要解决的问题。**检查点：** 在继续之前，用一句话概括该 PR 的意图。如果做不到，请作者澄清。
2. **Structure（结构）** — 审查架构与设计决策。自问：这是否遵循了代码库中已有的模式？新增的抽象是否有充分理由？
3. **Details（细节）** — 检查代码质量、安全性与性能。应用下方"参考指南"中的检查项。自问：是否存在 N+1 查询、硬编码的密钥或注入风险？
4. **Tests（测试）** — 验证测试覆盖与质量。自问：边界情况是否已覆盖？测试断言的是行为而非实现吗？
5. **Feedback（反馈）** — 使用"输出模板"生成分类报告。如果第 3 步发现了严重问题，立即记录，不要等到最后。

> **分歧处理：** 如果作者已留下注释解释某个非显而易见的选择，在提出替代方案之前先认可其理由。当已配置 linter 或格式化工具时，绝不要因风格偏好而阻塞。

## 参考指南

根据上下文加载详细指引：

<!-- Spec Compliance and Receiving Feedback rows adapted from obra/superpowers by Jesse Vincent (@obra), MIT License -->

| 主题 | 参考文件 | 何时加载 |
|-------|-----------|-----------|
| 审查清单 | `references/review-checklist.md` | 开始审查、了解分类时 |
| 常见问题 | `references/common-issues.md` | N+1 查询、魔法数字、模式时 |
| 反馈示例 | `references/feedback-examples.md` | 撰写优质反馈时 |
| 报告模板 | `references/report-template.md` | 撰写最终审查报告时 |
| 规格符合性 | `references/spec-compliance-review.md` | 审查实现、PR 审查、规格验证时 |
| 接收反馈 | `references/receiving-feedback.md` | 回应审查意见、处理反馈时 |

## 审查模式（快速参考）

### N+1 查询——坏与好
```python
# BAD: query inside loop
for user in users:
    orders = Order.objects.filter(user=user)  # N+1

# GOOD: prefetch in bulk
users = User.objects.prefetch_related('orders').all()
```

### 魔法数字——坏与好
```python
# BAD
if status == 3:
    ...

# GOOD
ORDER_STATUS_SHIPPED = 3
if status == ORDER_STATUS_SHIPPED:
    ...
```

### 安全：SQL 注入——坏与好
```python
# BAD: string interpolation in query
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# GOOD: parameterized query
cursor.execute("SELECT * FROM users WHERE id = %s", [user_id])
```

## 约束

### 必须做（MUST DO）
- 审查前先概括 PR 意图（见工作流第 1 步）
- 提供具体、可执行的反馈
- 在建议中附上代码示例
- 表扬好的模式
- 为反馈排定优先级（严重 → 轻微）
- 像审查代码一样深入地审查测试
- 检查安全问题（以 OWASP Top 10 为基线）

### 禁止做（MUST NOT DO）
- 不居高临下、不粗鲁
- 已有 linter 时不吹毛求疵于风格
- 不因个人偏好而阻塞
- 不苛求完美
- 不在不理解缘由的情况下审查
- 不跳过对好作品的表扬

## 输出模板

代码审查报告必须包含：
1. **Summary（概要）** — 一句话回顾意图 + 总体评估
2. **Critical issues（严重问题）** — 合并前必须修复（bug、安全、数据丢失）
3. **Major issues（主要问题）** — 应当修复（性能、设计、可维护性）
4. **Minor issues（次要问题）** — 有则更好（命名、可读性）
5. **Positive feedback（正面反馈）** — 做得好的具体模式
6. **Questions for author（向作者提问）** — 需要澄清的问题
7. **Verdict（结论）** — Approve / Request Changes / Comment

## 知识参考

SOLID、DRY、KISS、YAGNI、设计模式、OWASP Top 10、语言惯用法、测试模式

由 [@jeffallan](https://github.com/jeffallan)（[Synergetic Solutions](https://synergetic.solutions) 首席顾问）维护

[文档](https://jeffallan.github.io/claude-skills/skills/quality/code-reviewer/)
