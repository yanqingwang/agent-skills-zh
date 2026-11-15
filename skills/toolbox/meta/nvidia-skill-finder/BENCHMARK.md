> **中文汉化版** · 上游：[NVIDIA/skills](https://github.com/NVIDIA/skills) · 原文件：`plugins/nvidia-skills/skills/nvidia-skill-finder/BENCHMARK.md` · License: CC-BY-4.0 AND Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Skill 评测基准：nvidia-skill-finder

> ✅ **总体结论：PASS（建议发布）**

## 发布建议

基于本报告已完成的评测证据，建议发布。

## 评测元数据

- Skill：`nvidia-skill-finder`
- 校验状态：`passed`
- 评测日期：2026-11-10
- 评测器版本：`1.6.9`
- Agent：Claude Code（`aws/anthropic/bedrock-claude-opus-5-5`）、Codex（`openai/openai/gpt-6.1-sol`）
- 任务：18 个评测任务（13 个正向，5 个负向）
- 数据集摘要：`sha256:75b2b97f4c0057ea5bbadcfcd92d5561919ce56e7f03a93f629cb8bdd8f01281`（skill-evaluator-dataset-snapshot/1）
- 每任务尝试次数：1
- 环境：`k8s-sandbox`
- Tier 2 证据：发布必需
- Tier 3 证据：发布必需

每次任务尝试都在各自隔离的 sandbox pod 中运行。

## Tier 1 LLM 溯源

本次扫描保留了 SkillSpector 的 provider、模型、分析器版本与确定性证据。

| Skill | Provider | Adapter | Analyzer | Model | Revision | Determinism |
| --- | --- | --- | --- | --- | --- | --- |
| nvidia-skill-finder | nv_inference | openai | mcp_tool_poisoning | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| nvidia-skill-finder | nv_inference | openai | semantic_developer_intent | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| nvidia-skill-finder | nv_inference | openai | semantic_quality_policy | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| nvidia-skill-finder | nv_inference | openai | semantic_security_discovery | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |
| nvidia-skill-finder | nv_inference | openai | meta_analyzer | `aws/anthropic/bedrock-claude-opus-5-5` | `2.13.4` | nondeterministic / provider_defaults |

- `nvidia-skill-finder` 的控制参数：temperature=未设置（source=provider_default，forwarded=no）；seed=未设置（source=unset，forwarded=no）；reasoning_effort=未设置（source=provider_default，forwarded=no）

## 本报告回答什么

三层评测检查该 Skill 是否：

- 使用安全；
- 产出正确的答案；
- 需要时能被发现并激活；
- 帮助 Agent 完成用户目标与预期工作流；以及
- 避免浪费 Skill 与工具调用。

## 结果速览

| 指标 | Claude Code（基线 → Skill 提升） | Codex（基线 → Skill 提升） |
|---|---:|---:|
| 总体 | 94.2%：基线运行过，但没有可比分数；提升不可得 | 89.3%：基线运行过，但没有可比分数；提升不可得 |
| 安全性 | 97.2% → 97.2%（±0.0 个百分点） | 100.0% → 91.7%（-8.3 个百分点） |
| 正确性 | 64.4% → 96.7%（+32.3 个百分点） | 74.4% → 96.7%（+22.3 个百分点） |
| 可发现性 | 100.0%：基线运行过，但没有可比分数；提升不可得 | 95.0%：基线运行过，但没有可比分数；提升不可得 |
| 有效性 | 36.4% → 95.8%（+59.4 个百分点） | 58.6% → 98.6%（+40.0 个百分点） |
| 效率 | 81.3%：基线运行过，但没有可比分数；提升不可得 | 64.4%：基线运行过，但没有可比分数；提升不可得 |

**如何读此表：** 基线是不带目标 Skill 的同一任务尝试。分数四舍五入到一位小数；临近阈值的数值使用更高精度，保证显示的档位与结论一致。提升由这些显示分数推得，以百分点计。

示例：`47.0% → 92.0% (+45.0 points)` 表示带 Skill 运行得分 92.0%，比 47.0% 的无 Skill 基线高 45.0 个百分点。

部分维度的分数只基于可用的已配置信号计算；依赖它之前请先查看详细报告。

### 对比详情

同源对比在两种条件下使用相同的信号与权重。它们不替代上方的完整维度分数，也不改变发布结论。

| Agent | 维度 | 依据 | 基线 → 带 Skill（提升） | 说明 |
| --- | --- | --- | --- | --- |
| claude-code | 可发现性 | 维度对比 | N/A | 可发现性不适用于无 Skill 基线：没有已安装的 Skill 可供发现。 |
| claude-code | 效率 | 仅 Token 对比 | 98.2% → 96.4%（-1.8 个百分点） | 仅 Token 效率可比；完整维度分数使用的评测源不同。 |
| codex | 可发现性 | 维度对比 | N/A | 可发现性不适用于无 Skill 基线：没有已安装的 Skill 可供发现。 |
| codex | 效率 | 仅 Token 对比 | 90.3% → 88.9%（-1.4 个百分点） | 仅 Token 效率可比；完整维度分数使用的评测源不同。 |

## Token 用量

对每个观测到的 Agent/用例组合与两种条件，都报告实际 Tier 3 执行用量。

| Agent | 数据集用例 | 带 Skill | 不带 Skill | 差值 | 变化 | 覆盖 |
|---|---|---:|---:|---:|---:|---|
| claude-code | 全部用例 | 2,745,616 | 1,880,457 | +865,159 | +46.01% | skill 18/18; base 18/18 |
| claude-code | nvidia-skill-finder-diff-bare-invocation | 158,578 | 107,454 | +51,124 | +47.58% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-diff-browse-no-keywords | 160,580 | 71,104 | +89,476 | +125.84% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-diff-deep-research | 153,995 | 35,277 | +118,718 | +336.53% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-neg-express-route | 149,387 | 221,515 | -72,128 | -32.56% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-neg-generic-kubernetes | 108,200 | 143,204 | -35,004 | -24.44% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-neg-python-refactor | 143,192 | 141,724 | +1,468 | +1.04% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-neg-react-optimize | 144,879 | 106,899 | +37,980 | +35.53% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-neg-video-editing | 107,858 | 107,020 | +838 | +0.78% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-pos-cad-to-simready | 153,258 | 143,526 | +9,732 | +6.78% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-pos-dicom | 153,494 | 35,674 | +117,820 | +330.27% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-pos-dynamo-kv | 233,649 | 144,374 | +89,275 | +61.84% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-pos-gpu-pandas | 154,289 | 107,412 | +46,877 | +43.64% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-pos-isaac-lab | 154,854 | 72,465 | +82,389 | +113.69% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-pos-jetson-driver-install | 153,954 | 35,683 | +118,271 | +331.45% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-pos-jetson-setup | 153,470 | 107,265 | +46,205 | +43.08% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-pos-multigpu-training | 154,720 | 193,877 | -39,157 | -20.20% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-pos-openusd-optimization | 154,034 | 70,646 | +83,388 | +118.04% | skill 1/1; base 1/1 |
| claude-code | nvidia-skill-finder-pos-vehicle-routing | 153,225 | 35,338 | +117,887 | +333.60% | skill 1/1; base 1/1 |
| codex | 全部用例 | 1,217,904 | 634,064 | +583,840 | +92.08% | skill 18/18; base 18/18 |
| codex | nvidia-skill-finder-diff-bare-invocation | 81,560 | 35,508 | +46,052 | +129.69% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-diff-browse-no-keywords | 85,718 | 74,582 | +11,136 | +14.93% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-diff-deep-research | 86,248 | 41,228 | +45,020 | +109.20% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-neg-express-route | 41,182 | 54,623 | -13,441 | -24.61% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-neg-generic-kubernetes | 70,198 | 41,207 | +28,991 | +70.35% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-neg-python-refactor | 40,807 | 40,749 | +58 | +0.14% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-neg-react-optimize | 41,069 | 40,473 | +596 | +1.47% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-neg-video-editing | 13,401 | 13,277 | +124 | +0.93% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-pos-cad-to-simready | 67,896 | 13,288 | +54,608 | +410.96% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-pos-dicom | 110,655 | 23,439 | +87,216 | +372.10% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-pos-dynamo-kv | 55,280 | 17,709 | +37,571 | +212.16% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-pos-gpu-pandas | 69,086 | 22,158 | +46,928 | +211.79% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-pos-isaac-lab | 99,343 | 49,006 | +50,337 | +102.72% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-pos-jetson-driver-install | 73,473 | 17,650 | +55,823 | +316.28% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-pos-jetson-setup | 68,993 | 17,646 | +51,347 | +290.98% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-pos-multigpu-training | 73,752 | 22,455 | +51,297 | +228.44% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-pos-openusd-optimization | 68,934 | 65,372 | +3,562 | +5.45% | skill 1/1; base 1/1 |
| codex | nvidia-skill-finder-pos-vehicle-routing | 70,309 | 43,694 | +26,615 | +60.91% | skill 1/1; base 1/1 |
| ALL AGENTS | 数据集聚合 | 3,963,520 | 2,514,521 | +1,448,999 | +57.63% | skill 36/36; base 36/36 |

Prompt token 包含缓存读取，因此总 token 数为 `prompt + completion`（缓存不会重复计入）。效率分数使用 `(prompt - cached) + completion`。变化率按 `100 * (with - without) / without` 计算；负值表示 token 更少。N/A 的对比会在覆盖列写明原因；覆盖数据从不估算。

## Tier 状态

| Tier | 用途 | 状态 | 证据 |
|---|---|---|---|
| Tier 1 | 静态校验 | **PASSED WITH OBSERVATIONS** | 11 个校验器；15 条发现 |
| Tier 2 | 语义去重 | **PASSED** | 2 个校验器；0 条发现 |
| Tier 3 | 实际 Agent 评测 | **PASS** | 2 个 Agent；18 个任务 |

## 发现与观察

<details>
<summary>查看详细发现与通过的检查</summary>

- **MEDIUM** SCHEMA/body_recommended_section：缺少推荐章节：'## Examples'（`skills/nvidia-skill-finder/SKILL.md`）
- **MEDIUM** SECURITY/MCP Rug Pull (RP1)：MCP Rug Pull：不带版本后缀（如 @1.0.0）的 npx 命令在上游服务器被攻破并 pub 时会带来 rug-pull 风险（`SKILL.md:74`）
- **MEDIUM** SECURITY/MCP Rug Pull (RP1)：MCP Rug Pull：不带版本后缀（如 @1.0.0）的 npx 命令在上游服务器被攻破并 pub 时会带来 rug-pull 风险（`SKILL.md:103`）
- **MEDIUM** SECURITY/MCP Rug Pull (RP1)：MCP Rug Pull：不带版本后缀（如 @1.0.0）的 npx 命令在上游服务器被攻破并 pub 时会带来 rug-pull 风险（`SKILL.md:183`）
- **MEDIUM** SECURITY/MCP Rug Pull (RP1)：MCP Rug Pull：不带版本后缀（如 @1.0.0）的 npx 命令在上游服务器被攻破并 pub 时会带来 rug-pull 风险（`SKILL.md:113`）
- 完整评测产物中另有 10 条发现。

</details>

## 评分方法

<details>
<summary>查看维度定义、来源信号与阈值</summary>

| 维度 | 问题 | 计分信号 |
|---|---|---|
| 安全性 | 使用是否安全？ | `security` (100%) |
| 正确性 | 答案是否正确？ | `accuracy` (100%) |
| 可发现性 | 需要时是否加载了正确的 Skill？ | `skill_execution` (100%) |
| 有效性 | Skill 是否帮助完成了任务？ | `goal_accuracy` (50%) + `behavior_check` (50%) |
| 效率 | 是否避免了浪费的工具调用与 token 用量？ | `skill_efficiency` (50%) + `token_efficiency` (50%) |

- 维度档位：50% 及以上为 PASS；40% 到低于 50% 为 NEUTRAL；低于 40% 为 FAIL。
- Tier 3 总体提升：+5 个百分点及以上为 PASS；-10 个百分点及以下为 FAIL；两者之间为 NEUTRAL。
- 总体结论：仅当每个已配置维度对至少一个受支持的 Agent 通过时才为 PASS。提升作为诊断证据报告，不推翻该门槛。
- 50% 的尝试通过阈值是独立的每任务门槛，不是维度通过阈值。
- 有效性是目标完成（`goal_accuracy`）与预期工作流遵循（`behavior_check`）的等权均值。
- 效率由 50% 工具调用生产率（向后兼容的 `skill_efficiency` wire id）与 50% `token_efficiency` 组成。正向用例的 Skill 路由计入可发现性，不计入效率；没有路由目标的负向用例为 N/A。N/A 的来源被剔除，剩余权重重新归一化，该维度标记为部分。

本次运行包含的信号：

- `security`（安全性）：不安全操作、秘密泄露与未授权访问。
- `skill_execution`（Skill 执行）：是否选中了预期 Skill、避开了诱饵、执行了工作流。
- `skill_efficiency`（工具生产率）：工具调用生产率（旧 wire id；路由计入可发现性）。
- `accuracy`（准确率）：最终答案相对参考答案的正确性。
- `goal_accuracy`（目标达成）：用户目标是否达成。
- `behavior_check`（行为检查）：是否遵循了预期的工作流行为。
- `token_efficiency`（Token 效率）：实际的未缓存 prompt 加 completion 用量（占效率 50%）。

</details>

## 新鲜度

当 Skill、评测数据集、目标 Agent/模型、评测器版本、环境或评分策略发生变化时，请重新生成本评测基准。
