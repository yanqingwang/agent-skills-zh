> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/celebrity/merger.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 名人人格合并

## 任务

当新材料到达或用户提出修正时，演进已有的名人 Skill。保留此人的复杂性：不要把他压扁成一个更“干净”却更失真的版本。

人格已有结构。你的任务是把新证据穿进正确的层，同时不破坏已经校准好的内容。

---

## 两种演进模式

### 模式 A：材料驱动的更新

触发条件：用户提供新研究材料（新访谈、演讲、文章、字幕，或经 `tools/research/transcribe_audio.py` 得到的转写稿）。

流程：

1. 只对**新**材料跑采集 / 研究流水线（放在 `knowledge/research/raw/` 下带日期的子文件夹里，保证来源清晰）。
2. 重跑 `tools/research/merge_research.py <skill_dir>`，用新增文件刷新合并摘要。
3. 重写任何内容之前，先把新提取结果与现有 `persona.md` 做对比。多数材料只会印证已有内容，只有少数会改变形态。

### 模式 B：修正驱动的更新

触发条件：用户说“这里错了”、“你理解错了”，给出与当前输出相矛盾的直接引语，或要求修正语气 / 边界。

流程：

1. 把修正逐字写入 Correction Log（修正日志），附时间戳和触发的用户原话。
2. 把修正定位到它触及的具体层（心智模型、启发法、表达 DNA、思想谱系等）。
3. 只对该层做最小调整。不要把编辑扩散到用户没有纠正的层。

---

## 合并优先级（按人格层）

### Layer 1：身份

仅当新材料揭示了当前身份简介漏掉的稳定自我描述，或用户纠正了激活免责声明时才改。

### Layer 2：表达 DNA

当新材料提供以下内容时更新：

- 能通过 100 词盲测的更多声音样本
- 有明确领域来源、反复出现的比喻或框架手法
- 在三个以上语境中得到印证的确定性语言标记或禁用词项

不要用新样本替换旧样本，除非旧样本未通过三重门槛（跨语境、生成性、独特性）。锚点材料的多样性比新旧更重要。

### Layer 3：心智模型

新心智模型只有通过三重门槛才能纳入：

1. **跨语境复现**：出现在至少三个不同主题或时段的独立来源中。
2. **生成性**：能产出新的推理，而不只是重新描述过去的某一个观点。
3. **独特性**：持不同世界观的人不会默认得出同样的结论。

新增模型时，标注：

- 证据锚点（来自不同语境的 2 个以上实例）
- 失效模式
- 应用边界
- 它与现有模型是互补、细化还是张力关系

不要删除现有模型。如果被反驳，在 Layer 6（内部张力）里明确标注张力。

### Layer 4：决策启发法

当新材料显示此人有一致的行为规则而当前人格没有捕捉到，或修正表明当前措辞过度泛化时更新。

保持“如果 X，那么 Y”的结构，附推理和语境边界。

### Layer 5：反模式与边界

用新出现的重复拒绝或新近承认的盲区来充实。如果新材料显示此人在此前的拒绝事项上改变了想法，把两者都记录下来：先前的拒绝和修改后的立场，并附日期。

### Layer 6：内部张力

如果新材料引入了矛盾，把它加进张力清单。分类为 Temporal / Contextual / Inherent（时间性 / 语境性 / 固有）。绝不要因为新材料偏向某一方就悄悄调和一处张力：记下倾斜方向和支撑证据，但只要张力仍然成立，就让它保持可见。

### Layer 7：思想谱系

当出现以下情况时，更新 `Influenced by` / `Diverged from` / `Influenced` / `Tradition`：

- 此人明确提到一位当前人格未记录的影响者
- 公开的批评把其工作归入人格漏掉的传统
- 有后继者公开承认借鉴了此人的工作

“diverged from”这一轴要保持清晰：它往往是此人独特立场最浓缩的信号。

### Layer 8：Agentic Protocol

当新材料揭示出当前分类器处理不了的问题类型时，更新 Step 1 的问题类别。当此人公开描述过尚未体现的研究习惯时，更新 Step 2 的研究维度（例如“我总是先看空头论点”、“我读摘要之前先读脚注”）。

不要为了迎合某一次新访谈重写协议。协议应在大量来源间保持稳定；一次性的怪癖放进反模式里。

### 认知时间线

只有当新材料揭示出真正的转折点（而非重复表述）时，才添加新的阶段条目。如果此人公开给这个转变起过名，引用那个命名短语。

### 验证锚点

当新材料给出一个干净的已知答案案例时，如果现有锚点已经陈旧，或新案例能锻炼某个测试不足的心智模型，考虑换入。

### Correction Log（修正日志）

模式 B 的条目落在这里。格式：

```text
- [YYYY-MM-DD] User correction: "{user phrase}"
  Affected layer: {layer name}
  Change made: {one-line summary}
  Evidence for change: {what backs the correction — user authority, cited
  source, contradiction with existing anchor, etc.}
```

绝不删除修正日志条目，即使已被取代。它们是审计轨迹。

---

## 规则

- 第一人称材料优先于评论。
- 逐级携带来源权重（1–7）；权重冲突时，以更高层级为准。
- 明确标注时效敏感的更新（例如对可能变化的立场标注“截至 2026-04”）。
- 保留跨时间的演变：不要把它压扁成当前状态。
- 如果新材料与现有锚点矛盾，两者都保留并标注矛盾，除非模式 B 修正明确覆盖。
- 合并后重跑 `tools/research/quality_check.py <skill_dir> --profile <profile>`。之前通过的检查必须仍然通过。

---

## 输出格式

```text
=== mode ===
{material-driven | correction-driven}

=== persona.md update ===
{patch — layer by layer, only touching changed layers}

=== correction_log.md update (if Mode B) ===
{appended entry}

=== summary ===
- layers touched: {list}
- mental models added: {n}
- mental models refined: {n}
- heuristics added / refined: {n}
- tensions added: {n}
- genealogy updates: {n}
- timeline phases added: {n}
- validation anchors updated: {n}
- corrections logged: {n}
- contradictions preserved (not flattened): {n}

=== quality gate ===
- research_metrics after merge: {paste relevant fields}
- quality_check.py result: {pass/fail with which checks flipped}
```
