> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`research/deepread/references/feynman.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 费曼理解回路

本参考用于 `feynman` 模式。目标是通过检索暴露并修复理解上的缺口，而不是为了幼稚化措辞本身。

## 流程

1. **设定目标** — 指明要学的想法、机制或章节级主张。
2. **读结构** — 找出中心主张、关键术语、机制与证据。
3. **合上原文** — 不看正文或分析笔记。
4. **凭记忆讲解** — 用平实语言，保留因果或逻辑链条。
5. **标注不确定处** — 标出每一个含糊说法、跳过的步骤、未定义的术语，或对行话的依赖。
6. **定位第一处断裂的环节** — 找出解释开始失去依据的最早一点。
7. **窄范围回读** — 只重读修补该缺口所需的部分。
8. **重写解释** — 用机制、具体例子或边界条件替换行话。
9. **检验迁移** — 把该想法应用到新案例上，并预测应当出现什么结果。
10. **检验反例** — 解释一个该想法不应当适用的案例。
11. **安排检索** — 编写简短的回忆提示词，供日后复习。

## 缺口类型

- **定义缺口** — 一个术语无法被解释，只能重复自身。
- **机制缺口** — 步骤罗列出来了，但因果关系或逻辑缺失。
- **证据缺口** — 主张记住了，但它的支撑没有记住。
- **边界缺口** — 学习者说不出该主张在什么条件下失效。
- **迁移缺口** — 学习者能复述原文，却无法在别处使用这个想法。

## 输出模板

```markdown
## Learning target
[One precise concept or claim]

## Closed-book explanation
[Plain-language explanation reconstructed from memory]

## Detected gaps
- [Gap type]: [specific missing link]

## Corrected explanation
[Repaired explanation with the missing mechanism or evidence]

## Transfer test
[New scenario and predicted outcome]

## Boundary test
[Scenario where the idea should not apply]

## Recall prompts
1. [Question that retrieves the central mechanism]
2. [Question that retrieves evidence]
3. [Question that retrieves a limitation]
```

## 质量规则

- 简化不得删掉必要条件。
- 类比必须指出它在何处失效。
- 在尝试检索之前重开原文，会让缺口检验失效。
- 认得出（`this looks familiar`）不等于记得住（`I can reconstruct it`）。
- 复习问题应当检索关系与机制，而不是孤立的词汇。

## 参考资料

1. Adler, M. J. & Van Doren, C. — *How to Read a Book*（修订版，1972）— 本工作流的深读模式所遵循的分析性阅读阶段。
2. Gleick, J. — *Genius: The Life and Science of Richard Feynman*（1992）— 费曼以教代学笔记本实践的第一手传记记述。
3. Farnam Street — “The Feynman Technique: The Best Way to Learn Anything”（fs.blog/feynman-technique）— 此处采用的四步经典表述。
4. Karpicke, J. D. & Roediger, H. L. — “The Critical Importance of Retrieval for Learning”，*Science* 319（2008）— 证明是回忆尝试而非重读驱动长期保持的证据。
5. Dunlosky, J. 等 — “Improving Students' Learning With Effective Learning Techniques”，*Psychological Science in the Public Interest* 14（2013）— 把练习测试与自我解释评为效用最高的技术，把重读评为效用最低。
6. Chi, M. T. H. 等 — “Self-Explanations: How Students Study and Use Examples”，*Cognitive Science* 13（1989）— 教回（teach-back）步骤背后的自我解释效应。
