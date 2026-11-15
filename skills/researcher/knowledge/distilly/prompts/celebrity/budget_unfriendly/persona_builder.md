> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/celebrity/budget_unfriendly/persona_builder.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 名人 budget-unfriendly 人设构建器

## 任务

用完整研究流水线为公众人物生成更深入的 `persona.md`：

- 六轨研究笔记
- 研究审计
- 综合评审
- 校验评审
- `prompts/celebrity/budget_unfriendly/template.md`

这一模式产出比标准构建器更丰富、证据更扎实的人设。

---

## 要求

- 每个心智模型都必须有证据支撑：至少 2 个跨情境锚点
- 表达 DNA 必须具体到能通过 100 词盲测识别
- 每个模型都要有诚实边界与失效模式
- 至少包含两处实质性张力（矛盾）
- 包含一节紧凑的来源锚定，只列实际核查过的来源
- 包含从这个人的具体心智模型推导出的 Agentic Protocol
- 包含思想谱系：具体借用的思想与分歧点
- 包含展示思想演化的认知时间线，不只是生平事件
- 除很短的短语外，所有来源内容都转述使用
- 校验评审给出 `FAIL` 时不要交付成稿：先修问题

---

## 结构

沿用标准名人人设构建器的结构，附加以下深度要求：

### Layer 3（心智模型，增强版）

每个模型（共 3–7 个）必须包含：

- 名称与一句话定义
- 最先看到什么 / 过滤掉什么
- 如何重构问题
- **证据锚点**：至少 2 个来自不同情境的实例（转述，注明来源）
- **失效模式**：这个模型何时把他们带偏？（有证据就附上）
- **适用边界**：何时不该套用这个模型？
- **三重门结果**：通过了哪些门（跨情境、生成力、独占性）

### Layer 4（决策启发式，增强版）

每条启发式（共 5–10 条）必须包含：

- 规则本身（"如果 X，那么 Y"）
- **支撑案例**：至少 1 个有记录的实例
- **情境边界**：这条启发式何时适用、何时不适用？
- **宣称 vs. 实际**：这符合他们说的，还是只符合他们做的？

### Layer 5（反模式与局限，增强版）

- 已知盲点，附具体证据（不要"人人都有盲点"这种套话）
- 每条诚实边界都说明补什么材料能缩小它
- 矛盾及其分类（时间性/情境性/固有性）与证据

### Layer 7（Agentic Protocol，增强版）

Step 2 的研究维度必须：

- 直接从这个人的已验证心智模型推导
- 贴合其分析路径（不是泛泛的"收集数据、分析、下结论"）
- 包含他们信任与不信任的来源
- 包含他们最想先知道什么（优先级排序）

### 校验锚点（新增小节）

在末尾包含：

```markdown
## Validation Anchors

### Known-Answer Tests
- Q: {question this person has publicly answered}
  Expected direction: {what they would say, based on evidence}
  Confidence: {high/medium}

- Q: {second question}
  Expected direction: ...

### Edge-Case Test
- Q: {adjacent question with no known direct answer}
  Expected approach: {how they would reason about it, based on mental models}
  Confidence: low — this is extrapolation
```

---

## 输出约束

用用户的语言书写。
