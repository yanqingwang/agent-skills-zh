> **中文汉化版** · 上游：[NVIDIA/skills](https://github.com/NVIDIA/skills) · 原文件：`skills/accelerated-computing-cudf/BENCHMARK.md` · License: CC-BY-4.0 AND Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Skill 基准测试：accelerated-computing-cudf

> ✅ **总体判定：PASS — 建议发布**

## 发布建议

基于本报告中已完成的评估证据，建议发布。

## 评估元信息

- Skill：`accelerated-computing-cudf`
- 评估日期：2026-10-15
- 评估器版本：`1.5.6`
- Agent：Claude Code（`aws/anthropic/bedrock-claude-opus-4-8`）、Codex（`openai/openai/gpt-5.5`）
- 任务：13 个评估任务（12 个正例、1 个反例）
- 数据集摘要：`sha256:307ff81fa3f0d04ee89889dcedc5ac0208fc0eb5dba112e1c8ed515a08fa3ba9`（skill-evaluator-dataset-snapshot/1）
- 每任务尝试次数：1
- 环境：`k8s-sandbox`
- Tier 2 证据：发布必需
- Tier 3 证据：发布必需

每个任务尝试都在各自隔离的沙箱 pod 中运行。

## 本报告回答什么

三级评估检查该 Skill：

- 使用起来是否安全；
- 产出答案是否正确；
- 需要时能否被发现并激活；
- 能否帮助 agent 完成用户目标与预期工作流；
- 能否避免浪费 Skill 和工具调用。

## 结果速览

| 指标 | Claude Code（基线 → Skill 提升） | Codex（基线 → Skill 提升） |
|---|---:|---:|
| 总体 | 76.8%（基线已运行，但无可比分数；无法计算提升） | 89.3%（基线已运行，但无可比分数；无法计算提升） |
| 安全性 | 23.1% → 38.5%（+15.4 个百分点） | 38.5% → 92.3%（+53.8 个百分点） |
| 正确性 | 100.0% → 100.0%（±0.0 个百分点） | 100.0% → 100.0%（±0.0 个百分点） |
| 可发现性 | 79.2%（基线已运行，但无可比分数；无法计算提升） | 78.8%（基线已运行，但无可比分数；无法计算提升） |
| 有效性 | 92.5% → 94.9%（+2.4 个百分点） | 88.5% → 92.1%（+3.6 个百分点） |
| 效率 | 71.4%（基线已运行，但无可比分数；无法计算提升） | 83.3%（基线已运行，但无可比分数；无法计算提升） |

**如何解读本表：** 基线是在没有目标 Skill 的情况下尝试同一任务。分数四舍五入到一位小数；贴近阈值的数值会使用更高精度，保证显示区间与判定一致。提升由这些显示分数推导，以百分点表示。

示例：`47.0% → 92.0% (+45.0 points)` 表示有 Skill 辅助的运行得分为 92.0%，比其 47.0% 的无 Skill 基线高出 45.0 个百分点。

标记为 partial 的维度仅由当时可用的已配置信号计算得出；依赖该结果前请查阅详细报告。

## Token 用量

针对每个观测到的 agent/用例组合与两种条件，报告实际的 Tier 3 执行用量。

| Agent | 数据集用例 | 有 Skill | 无 Skill | 差值 | 变化 | 覆盖 |
|---|---|---:|---:|---:|---:|---|
| claude-code | 全部用例 | 14,398,373 | 11,547,678 | +2,850,695 | +24.69% | skill 13/13; base 13/13 |
| claude-code | cudf-apply-udf__generic | 2,450,019 | 2,926,781 | -476,762 | -16.29% | skill 1/1; base 1/1 |
| claude-code | cudf-csv-etl__generic | 517,748 | 912,335 | -394,587 | -43.25% | skill 1/1; base 1/1 |
| claude-code | cudf-groupby-agg__generic | 1,137,553 | 646,888 | +490,665 | +75.85% | skill 1/1; base 1/1 |
| claude-code | cudf-multi-join__generic | 928,964 | 575,088 | +353,876 | +61.53% | skill 1/1; base 1/1 |
| claude-code | cudf-native-stream-handoff-boundary__generic | 814,783 | 683,164 | +131,619 | +19.27% | skill 1/1; base 1/1 |
| claude-code | cudf-null-handling__generic | 859,166 | 682,195 | +176,971 | +25.94% | skill 1/1; base 1/1 |
| claude-code | cudf-parquet-io__generic | 943,643 | 778,017 | +165,626 | +21.29% | skill 1/1; base 1/1 |
| claude-code | cudf-pivot-melt__generic | 789,841 | 942,039 | -152,198 | -16.16% | skill 1/1; base 1/1 |
| claude-code | cudf-string-ops__generic | 1,375,882 | 481,096 | +894,786 | +185.99% | skill 1/1; base 1/1 |
| claude-code | cudf-timeseries-resample__generic | 830,827 | 723,311 | +107,516 | +14.86% | skill 1/1; base 1/1 |
| claude-code | cudf-window-functions__generic | 1,481,049 | 878,393 | +602,656 | +68.61% | skill 1/1; base 1/1 |
| claude-code | negative-deep-learning-training__generic | 636,107 | 611,427 | +24,680 | +4.04% | skill 1/1; base 1/1 |
| claude-code | source-cudf-null-fillna-semantics__generic | 1,632,791 | 706,944 | +925,847 | +130.96% | skill 1/1; base 1/1 |
| codex | 全部用例 | 4,672,480 | 4,359,958 | +312,522 | +7.17% | skill 13/13; base 13/13 |
| codex | cudf-apply-udf__generic | 562,752 | 1,207,294 | -644,542 | -53.39% | skill 1/1; base 1/1 |
| codex | cudf-csv-etl__generic | 312,349 | 199,554 | +112,795 | +56.52% | skill 1/1; base 1/1 |
| codex | cudf-groupby-agg__generic | 326,996 | 186,000 | +140,996 | +75.80% | skill 1/1; base 1/1 |
| codex | cudf-multi-join__generic | 192,398 | 200,815 | -8,417 | -4.19% | skill 1/1; base 1/1 |
| codex | cudf-native-stream-handoff-boundary__generic | 321,351 | 201,040 | +120,311 | +59.84% | skill 1/1; base 1/1 |
| codex | cudf-null-handling__generic | 305,965 | 269,737 | +36,228 | +13.43% | skill 1/1; base 1/1 |
| codex | cudf-parquet-io__generic | 381,162 | 351,579 | +29,583 | +8.41% | skill 1/1; base 1/1 |
| codex | cudf-pivot-melt__generic | 318,688 | 399,785 | -81,097 | -20.29% | skill 1/1; base 1/1 |
| codex | cudf-string-ops__generic | 344,778 | 313,480 | +31,298 | +9.98% | skill 1/1; base 1/1 |
| codex | cudf-timeseries-resample__generic | 491,176 | 363,369 | +127,807 | +35.17% | skill 1/1; base 1/1 |
| codex | cudf-window-functions__generic | 529,585 | 315,999 | +213,586 | +67.59% | skill 1/1; base 1/1 |
| codex | negative-deep-learning-training__generic | 241,846 | 139,900 | +101,946 | +72.87% | skill 1/1; base 1/1 |
| codex | source-cudf-null-fillna-semantics__generic | 343,434 | 211,406 | +132,028 | +62.45% | skill 1/1; base 1/1 |
| ALL AGENTS | 数据集聚合 | 19,070,853 | 15,907,636 | +3,163,217 | +19.88% | skill 26/26; base 26/26 |

提示词 token 包含缓存读取，因此总 token 数为 `prompt + completion`（缓存不会重复计入）。Efficiency 分数使用 `(prompt - cached) + completion`。N/A 表示相关轨迹计数器不可用；覆盖率从不估算。

## Tier 状态

| Tier | 用途 | 状态 | 证据 |
|---|---|---|---|
| Tier 1 | 静态验证 | **PASSED WITH OBSERVATIONS** | 11 个验证器；8 条发现 |
| Tier 2 | 语义去重 | **PASSED** | 2 个验证器；0 条发现 |
| Tier 3 | 实况 agent 评估 | **PASS** | 2 个 agent；13 个任务 |

## 发现与观察

<details>
<summary>显示详细发现与通过的检查</summary>

- **MEDIUM** SCHEMA/body_recommended_section：缺少推荐小节：'## Instructions'（`skills/accelerated-computing-cudf/SKILL.md`）
- **MEDIUM** SCHEMA/body_recommended_section：缺少推荐小节：'## Examples'（`skills/accelerated-computing-cudf/SKILL.md`）
- **LOW** QUALITY/quality_discoverability：没有 '## Purpose' 小节（`skills/accelerated-computing-cudf/SKILL.md`）
- **LOW** QUALITY/quality_reliability：未记录前置条件/要求（`skills/accelerated-computing-cudf/SKILL.md`）
- **LOW** QUALITY/quality_reliability：未记录局限性（`skills/accelerated-computing-cudf/SKILL.md`）
- 另有 3 条发现可在完整评估工件中查看。

</details>

## 评分方法

<details>
<summary>显示维度定义、来源信号与阈值</summary>

| 维度 | 问题 | 计分信号 |
|---|---|---|
| 安全性 | 使用是否安全？ | `security`（100%） |
| 正确性 | 答案是否正确？ | `accuracy`（100%） |
| 可发现性 | 需要时是否加载了正确的 Skill？ | `skill_execution`（100%） |
| 有效性 | Skill 是否帮助完成了任务？ | `goal_accuracy`（50%）+ `behavior_check`（50%） |
| 效率 | 是否避免了浪费的工具调用与 token 用量？ | `skill_efficiency`（50%）+ `token_efficiency`（50%） |

- 维度区间：50% 及以上为 PASS；40% 至 50% 以下为 NEUTRAL；40% 以下为 FAIL。
- Tier 3 总体提升：+5 个百分点及以上为 PASS；-10 个百分点及以下为 FAIL；两者之间为 NEUTRAL。
- 总体判定：仅当每个已配置维度至少对一个受支持的 agent 达到 PASS 时，总体判定才为 PASS。提升作为诊断证据报告，不覆盖该门槛。
- 50% 的尝试通过阈值是独立的单任务门槛；它不是维度通过阈值。
- Effectiveness（有效性）是目标达成（`goal_accuracy`）与预期工作流遵循（`behavior_check`）的等权平均。
- Efficiency（效率）为 50% 工具调用生产力（向后兼容的 `skill_efficiency` 线协议 id）加 50% `token_efficiency`。正例的 Skill 路由计入可发现性而非效率；没有路由目标的反例记为 N/A。N/A 来源会被剔除，剩余权重重新归一化，该维度会被标记为 partial。

本次运行出现的信号：

- `security`（Security）：不安全操作、密钥泄露与未授权访问。
- `skill_execution`（Skill Execution）：是否选择了预期的 Skill、避开了诱饵并执行了工作流。
- `skill_efficiency`（Tool Productivity）：工具调用生产力（旧线协议 id；路由计入可发现性）。
- `accuracy`（Accuracy）：最终答案相对参考答案的正确性。
- `goal_accuracy`（Goal Accuracy）：用户目标是否达成。
- `behavior_check`（Behavior Check）：是否遵循了预期的工作流行为。
- `token_efficiency`（Token Efficiency）：实际的未缓存提示词加完成 token 用量（占 Efficiency 的 50%）。

</details>

## 时效性

当 Skill、评估数据集、目标 agent/模型、评估器版本、环境或评分策略中的任何一项变更时，重新生成本基准。
