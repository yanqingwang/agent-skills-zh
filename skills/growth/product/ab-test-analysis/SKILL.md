---
name: ab-test-analysis
description: "结合统计显著性（statistical significance）、样本量校验、置信区间来分析 A/B 测试结果，并给出 ship/extend/stop（发布/延长/停止）建议。适用于评估实验结果、检查测试是否达到显著性、解读 split test（AB 测试）数据，或决定是否发布某个实验变体。"
---

> **中文汉化版** · 上游：[phuryn/pm-skills](https://github.com/phuryn/pm-skills) · 原文件：`pm-data-analytics/skills/ab-test-analysis/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## A/B 测试分析

以严谨的统计方法评估 A/B 测试结果，并将研究发现转化为清晰的产品决策。

### 上下文

你正在分析 **$ARGUMENTS** 的 A/B 测试结果。

如果用户提供了数据文件（CSV、Excel 或分析平台导出文件），直接读取并分析它们。需要时生成 Python 脚本进行统计计算。

### 指令

1. **理解实验**：
   - 假设（hypothesis）是什么？
   - 改动了什么（即变体 variant）？
   - 主指标（primary metric）是什么？有没有护栏指标（guardrail metrics）？
   - 测试运行了多长时间？
   - 流量分配比例是多少？

2. **校验测试设置**：
   - **样本量**：对于预期的效应量（effect size），样本量是否足够大？
     - 使用公式：n = (Z²α/2 × 2 × p × (1-p)) / MDE²
     - 如果检验功效不足（<80% power），予以标记
   - **时长**：测试是否至少运行了 1-2 个完整业务周期？
   - **随机化**：是否有样本比例不匹配（SRM, sample ratio mismatch）的证据？
   - **新奇效应/首发效应（novelty/primacy effects）**：是否有足够时间让初期的行为变化消退？

3. **计算统计显著性**：
   - 对照组（control）与变体组的**转化率**
   - **相对提升（relative lift）**：(variant - control) / control × 100
   - **p 值（p-value）**：使用双尾 z 检验或卡方检验
   - **置信区间**：差异的 95% CI
   - **统计显著性**：p < 0.05 吗？
   - **实际显著性**：这个提升对业务有意义吗？

   如果用户提供了原始数据，生成并运行 Python 脚本来计算这些指标。

4. **检查护栏指标**：
   - 有没有护栏指标（收入、参与度、页面加载时间）出现劣化？
   - 主指标获胜但护栏指标劣化，可能并不是真正的胜利

5. **解读结果**：

   | 结果 | 建议 |
   |---|---|
   | 显著的正向提升，护栏指标无问题 | **Ship it（发布上线）** — 全量推出至 100% |
   | 显著的正向提升，护栏指标有隐忧 | **Investigate（调查）** — 发布前先弄清权衡取舍 |
   | 不显著，但呈正向趋势 | **Extend the test（延长测试）** — 需要更多数据或更大的效应 |
   | 不显著，表现持平 | **Stop the test（停止测试）** — 未检测到有意义的差异 |
   | 显著的负向提升 | **Don't ship（不要发布）** — 回退到对照组，分析原因 |

6. **给出分析摘要**：
   ```
   ## A/B Test Results: [Test Name]

   **Hypothesis**: [What we expected]
   **Duration**: [X days] | **Sample**: [N control / M variant]

   | Metric | Control | Variant | Lift | p-value | Significant? |
   |---|---|---|---|---|---|
   | [Primary] | X% | Y% | +Z% | 0.0X | Yes/No |
   | [Guardrail] | ... | ... | ... | ... | ... |

   **Recommendation**: [Ship / Extend / Stop / Investigate]
   **Reasoning**: [Why]
   **Next steps**: [What to do]
   ```

逐步思考。以 markdown 格式保存。如果提供了原始数据，生成用于计算的 Python 脚本。

---

### 延伸阅读

- [A/B Testing 101 + Examples](https://www.productcompass.pm/p/ab-testing-101-for-pms)
- [Testing Product Ideas: The Ultimate Validation Experiments Library](https://www.productcompass.pm/p/the-ultimate-experiments-library)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
