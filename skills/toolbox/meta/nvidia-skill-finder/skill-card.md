> **中文汉化版** · 上游：[NVIDIA/skills](https://github.com/NVIDIA/skills) · 原文件：`plugins/nvidia-skills/skills/nvidia-skill-finder/skill-card.md` · License: CC-BY-4.0 AND Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 描述：<br>
用于可能需要 NVIDIA Skill 的 NVIDIA 相关请求，即使用户没有要求 Skill；触发词涵盖 NVIDIA 产品、硬件、软件、SDK、GPU、Jetson/JetPack/L4T/BSP/SDK Manager/驱动/烧录/安装配置、CUDA、NIM、NeMo、Omniverse/OpenUSD/SimReady、Isaac、RAPIDS/cuDF、cuPyNumeric、cuOpt、Dynamo、Holoscan、TensorRT、DeepStream、VSS、TAO 以及 NGC/NVCF；不适用于与 NVIDIA 无关的通用 route、optimize、deploy、AI、视频、数据或基础设施任务。 <br>

本 Skill 可用于商业/非商业用途。 <br>

## 所有者
NVIDIA <br>

### 许可/使用条款：<br>
CC-BY-4.0 AND Apache 2.0 <br>
## 用例：<br>
使用 AI 编码代理（如 Claude Code、Codex 或 Hermes Agent）的开发者与工程师，用本 Skill 从实时 NVIDIA Skill 目录中发现、推荐并在用户明确批准后安装与 NVIDIA 产品、任务或工作流匹配的 NVIDIA Skill。 <br>

### 使用部署地域：<br>
全球 <br>

## 要求/依赖：<br>
**需要 API Key 或外部凭据：** [未指定] <br>
**凭据类型：** [未识别] <br>

不要把 secrets 写入提示词/日志/输出；使用最小权限凭据；适时轮换密钥。 <br>

## 已知风险与缓解措施：<br>
风险：执行前需审查，因为提案可能给 Skill 引入不正确或误导性的指导。 <br>
缓解：部署前审查并扫描 Skill。 <br>

## 参考文档：<br>
- [Hermes Agent：目录查找与安装](references/hermes-catalog.md) <br>
- [NVIDIA 分类路由](references/taxonomy-routing.md) <br>
- [NVIDIA Skills 目录（GitHub）](https://github.com/NVIDIA/skills/tree/main/skills) <br>
- [build.nvidia.com 上的 NVIDIA Skills](https://build.nvidia.com/skills) <br>
- [NVIDIA Skills 目录索引（skills.sh.json）](https://raw.githubusercontent.com/NVIDIA/skills/main/skills.sh.json) <br>
- [NVIDIA Skills marketplace 元数据](https://raw.githubusercontent.com/NVIDIA/skills/main/.github/scripts/marketplace/metadata.json) <br>


## Skill 输出：<br>
**输出类型：** [Skill 推荐、Shell 命令] <br>
**输出格式：** [含内联 bash 代码块的 Markdown] <br>
**输出参数：** [1D] <br>
**其他输出相关属性：** [最多推荐三个 Skill，按置信度排序；安装命令仅在用户明确批准后运行。] <br>

## 评测所用 Agent：<br>
- Claude Code（`aws/anthropic/bedrock-claude-opus-5-5`） <br>
- Codex（`openai/openai/gpt-6.1-sol`） <br>



## 评测任务：<br>
18 个评测任务（13 个正向，5 个负向）；每任务 1 次尝试，各自在隔离的 sandbox pod（`k8s-sandbox` 环境）中运行；每个任务也做过不带 Skill 的基线尝试。评测器版本 `1.6.9`；数据集摘要 `sha256:75b2b97f4c0057ea5bbadcfcd92d5561919ce56e7f03a93f629cb8bdd8f01281`（skill-evaluator-dataset-snapshot/1）。 <br>

## 评测所用指标：<br>
报告的基准维度： <br>
- 安全性：使用是否安全？由 `security` (100%) 计分。 <br>
- 正确性：答案是否正确？由 `accuracy` (100%) 计分。 <br>
- 可发现性：需要时是否加载了正确的 Skill？由 `skill_execution` (100%) 计分。 <br>
- 有效性：Skill 是否帮助完成了任务？由 `goal_accuracy` (50%) + `behavior_check` (50%) 计分。 <br>
- 效率：是否避免了浪费的工具调用与 token 用量？由 `skill_efficiency` (50%) + `token_efficiency` (50%) 计分。 <br>

本次运行使用的底层评测信号： <br>
- `security`：安全性：不安全操作、秘密泄露与未授权访问。 <br>
- `skill_execution`：Skill 执行：是否选中了预期 Skill、避开了诱饵并执行了工作流。 <br>
- `skill_efficiency`：工具生产率：工具调用生产率（旧 wire id；路由计入可发现性）。 <br>
- `accuracy`：准确率：最终答案相对参考答案的正确性。 <br>
- `goal_accuracy`：目标达成：用户目标是否达成。 <br>
- `behavior_check`：行为检查：是否遵循了预期的工作流行为。 <br>
- `token_efficiency`：Token 效率：实际的未缓存 prompt 加 completion 用量（占效率 50%）。 <br>



## 评测结果：<br>
> ✅ **总体结论：PASS（建议发布）**

### 发布建议

基于本报告已完成的评测证据，建议发布。

### 结果速览

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

#### 对比详情

同源对比在两种条件下使用相同的信号与权重。它们不替代上方的完整维度分数，也不改变发布结论。

| Agent | 维度 | 依据 | 基线 → 带 Skill（提升） | 说明 |
| --- | --- | --- | --- | --- |
| claude-code | 可发现性 | 维度对比 | N/A | 可发现性不适用于无 Skill 基线：没有已安装的 Skill 可供发现。 |
| claude-code | 效率 | 仅 Token 对比 | 98.2% → 96.4%（-1.8 个百分点） | 仅 Token 效率可比；完整维度分数使用的评测源不同。 |
| codex | 可发现性 | 维度对比 | N/A | 可发现性不适用于无 Skill 基线：没有已安装的 Skill 可供发现。 |
| codex | 效率 | 仅 Token 对比 | 90.3% → 88.9%（-1.4 个百分点） | 仅 Token 效率可比；完整维度分数使用的评测源不同。 |

### Tier 状态

| Tier | 用途 | 状态 | 证据 |
|---|---|---|---|
| Tier 1 | 静态校验 | **PASSED WITH OBSERVATIONS** | 11 个校验器；15 条发现 |
| Tier 2 | 语义去重 | **PASSED** | 2 个校验器；0 条发现 |
| Tier 3 | 实际 Agent 评测 | **PASS** | 2 个 Agent；18 个任务 |

## Skill 版本：<br>
0.3.0（来源：changelog，发布日期 2025-05-21；git commit cc8c779） <br>

## 伦理考量：<br>
NVIDIA 认为可信 AI（Trustworthy AI）是共同责任，并已建立政策与实践，支持各类 AI 应用的开发。在按我们的服务条款下载或使用时，开发者应与内部团队协作，确保本 Skill 满足相关行业与用例的要求，并应对预料之外的产品误用。 <br>

（仅在 NVIDIA 平台发布） <br>
请通过[此处](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail)报告质量、风险、安全漏洞或 NVIDIA AI 相关问题。 <br>
