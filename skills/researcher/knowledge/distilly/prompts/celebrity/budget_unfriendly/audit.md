> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/celebrity/budget_unfriendly/audit.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 名人 budget-unfriendly 研究审计提示词

## 任务

在综合之前审计六轨名人研究集。

阅读：

- `knowledge/research/raw/` 下的全部文件
- `knowledge/research/merged/summary.md`
- `prompts/celebrity/budget_unfriendly/framework.md`

审计写入 `knowledge/research/reviews/research_audit.md`。

## 审计职责

审计是硬性关卡。不要把它当成装饰性摘要。
你必须判断研究集是否已准备好进入综合。

FAIL 意味着研究还要加功夫。PASS 意味着可以进入综合。

## 必需小节

使用以下结构：

```md
# Research Audit

## Verdict
- Status: PASS / FAIL
- Reason: ...

## Coverage Review
- Track coverage: {N}/6 dimensions covered
- Missing or weak tracks: ...
- Cross-track redundancy: {are tracks meaningfully distinct or cloning observations?}

## Source Quality Assessment

### Source Mix
- Primary-source count: ...
- Secondary-source count: ...
- Primary-source ratio: ...% (target: >50%)
- Grounding quality: {are URLs actual inspected pages?}

### Source Hierarchy Compliance
- Sources from weight 1-3 (highest quality): ...
- Sources from weight 4-5 (medium quality): ...
- Sources from weight 6-7 (lowest quality): ...
- Blacklisted sources used: {list any — these are automatic failures}

### Taste Principle Compliance
- Long-form vs. snippet ratio: ...
- Firsthand vs. secondhand ratio: ...
- Controversial/distinctive positions captured: {yes/no, examples}
- Thinking evolution documented: {yes/no}

## Contradictions Inventory
- Total contradictions found: ...
- Classification:
  - Temporal (view evolution): ...
  - Contextual (domain differences): ...
  - Inherent (value tensions): ...
- Quality: {are these substantive tensions or superficial?}

## Mental Model Candidates
- Candidate count: ... (target: ≥3)
- For each candidate:
  - Name: ...
  - Cross-context evidence: {present in which dimensions?}
  - Preliminary gate assessment: ...

## Known-Answer Bank
- Question 1: ...
  Evidence anchors: ...
- Question 2: ...
  Evidence anchors: ...
- Strength: {are these answerable from the research evidence?}

## Edge-Case Candidate
- Question: ...
- Why this is adjacent but under-evidenced: ...
- Expected reasoning approach: ...

## Cold Figure Assessment
- Total grounded sources: ...
- Is this a cold figure (<10 sources)? {yes/no}
- If yes: recommended degradation strategy: ...

## Backfill Tasks
(Specific, actionable items to improve the research before synthesis)
- ...
- ...
```

## 审计规则：FAIL 条件

出现以下任一情况即判 FAIL：

- 六轨不完整（缺任一维度）
- 各轨道没有实质区分（跨文件克隆观察）
- 锚定 URL 单薄或低质（实际核查页面 < 8 个）
- 一手材料相对评论太弱（一手占比 < 50%）
- 使用了任何黑名单来源作为证据
- 矛盾缺失或被抹平（实质性张力 < 3 处）
- 证据不足以支撑至少 3 个心智模型
- 已知答案库太弱，撑不起后续校验（问题 < 2 道）
- 长文来源相对片段占比偏低
- 来源层级重心偏低（大部分是权重 5-7 的来源）

## 审计规则：PASS 条件

满足以下条件即判 PASS：

- 6 个维度全部覆盖且内容有实质区分
- 至少 8 个来自实际核查页面的锚定 URL
- 一手来源占比 > 50%
- 无黑名单来源
- 至少记录 3 处实质性矛盾
- 至少 3 个有跨维度证据的候选心智模型
- 至少 2 道带证据锚点的已知答案问题
- 至少 1 道边界情况问题
- 品味原则大体得到遵守（有长文，一手优先）

## 版权安全

- 不要把大段源文粘贴进审计
- 所有笔记保持转述并注明来源

## 输出约束

用用户的语言书写。
