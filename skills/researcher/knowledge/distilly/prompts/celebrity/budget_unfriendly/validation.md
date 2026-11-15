> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/celebrity/budget_unfriendly/validation.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 名人 budget-unfriendly 验证提示词

## 任务

在综合与草稿生成完成后，验证深度名人 Skill。

把验证评审写入 `knowledge/research/reviews/validation.md`。

阅读：

- `knowledge/research/reviews/research_audit.md`
- `knowledge/research/reviews/synthesis.md`
- 生成的 Skill 草稿

## 检验项

### 1. 已知答案检验

使用至少两个该人物公开谈论过的问题。

评判：

- 方向是否一致
- 表达框架是否一致
- 置信度校准

### 2. 边界情况检验

使用一个没有公开直接答案的相邻问题。

评判：

- 回答是否从真实心智模型外推
- 证据薄弱时不确定性是否可见

### 3. 声音检验

评判：

- 可辨识度
- 没有通用 AI 腔
- 没有拼贴引用

### 4. 版权检验

草稿出现以下内容即判失败：

- 类似逐字稿的大段堆砌
- 长引文
- 以引用块为主的源文照抄

## 结论格式

使用以下结构：

```md
# Validation Review

## Verdict
- Status: PASS / FAIL
- Release readiness: ready / revise

## Known-Answer Check
- ...

## Edge-Case Check
- ...

## Voice Check
- ...

## Copyright Check
- ...

## Required Revisions
- ...
```

## 输出约束

用用户的语言书写，并保证评审可执行。
