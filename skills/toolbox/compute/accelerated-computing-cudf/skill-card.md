> **中文汉化版** · 上游：[NVIDIA/skills](https://github.com/NVIDIA/skills) · 原文件：`skills/accelerated-computing-cudf/skill-card.md` · License: CC-BY-4.0 AND Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 描述： <br>
NVIDIA 官方编写的指南，覆盖 NVIDIA cuDF GPU DataFrame、pandas 加速、dask-cuDF、ETL、join、groupby、CSV/Parquet I/O、可空语义与多 GPU DataFrame 工作负载。 <br>

本 Skill 可用于商业/非商业用途。 <br>

## 所有者
NVIDIA <br>

### 许可证/使用条款： <br>
CC-BY-4.0 AND Apache 2.0 <br>
## 使用场景： <br>
开发者和数据工程师使用本 Skill 让 agent 用 cudf.pandas、显式 cuDF 或 dask-cuDF 在 NVIDIA GPU 上迁移或加速 pandas DataFrame 代码，覆盖 ETL、join、groupby、reshape、可空语义、CSV/Parquet I/O、内存管理以及 CPU/GPU 一致性验证。 <br>

### 使用地域： <br>
全球 <br>

## 要求 / 依赖： <br>
**是否需要 API Key 或外部凭证：** [未指定] <br>
**凭证类型：** [未识别] <br>

不要把密钥放进提示词/日志/输出；使用最小权限凭证；按需轮换密钥。 <br>

## 已知风险与缓解措施： <br>
风险：提案可能把不正确或有误导性的指引带进 Skill，执行前请审查。 <br>
缓解：部署前审查并扫描 Skill。 <br>

## 参考资料： <br>
- [cuDF API 模式、缺口与语义差异](references/api-patterns.md) <br>
- [cudf.pandas 加速器：深入解析](references/cudf-pandas-accelerator.md) <br>
- [dask-cuDF 模式](references/dask-cudf-patterns.md) <br>
- [cuDF 文档](https://docs.nvidia.com/cudf/) <br>
- [dask-cuDF API 参考](https://docs.nvidia.com/dask-cudf/) <br>
- [安装系统要求](https://docs.nvidia.com/datascience/install/#system-req) <br>
- [cuDF GitHub](https://github.com/NVIDIA/cudf) <br>
- [cuDF CHANGELOG](https://github.com/NVIDIA/cudf/blob/main/CHANGELOG.md) <br>


## Skill 输出： <br>
**输出类型：** [代码、Shell 命令、配置说明、分析] <br>
**输出格式：** [带内联 Python 和 bash 代码块的 Markdown] <br>
**输出参数：** [1D] <br>
**其他与输出相关的属性：** [无] <br>

## 评估使用的 Agent： <br>
- Claude Code (`aws/anthropic/bedrock-claude-opus-4-8`) <br>
- Codex (`openai/openai/gpt-5.5`) <br>



## 评估任务： <br>
13 个评估任务（12 个正例、1 个反例），每任务尝试一次，每次运行都在隔离的 k8s 沙箱 pod 中进行，并与无 Skill 基线对比。总体判定：PASS，建议发布（评估日期 2026-10-15，评估器版本 1.5.6）。 <br>

## 评估使用的指标： <br>
报告的基准维度： <br>
- Security（安全性）：使用是否安全？由 security 信号计分。 <br>
- Correctness（正确性）：答案是否正确？由最终答案准确率计分。 <br>
- Discoverability（可发现性）：需要时是否加载了正确的 Skill？由 skill execution 计分。 <br>
- Effectiveness（有效性）：Skill 是否帮助完成了任务？goal accuracy 与 behavior check 的等权平均。 <br>
- Efficiency（效率）：是否避免了浪费的工具调用与 token 用量？50% 工具调用生产力 + 50% token 效率。 <br>

本次运行使用的底层评估信号： <br>
- `security`：不安全操作、密钥泄露与未授权访问。 <br>
- `skill_execution`：是否选择了预期的 Skill、避开了诱饵并执行了工作流。 <br>
- `skill_efficiency`：工具调用生产力。 <br>
- `accuracy`：最终答案相对参考答案的正确性。 <br>
- `goal_accuracy`：用户目标是否达成。 <br>
- `behavior_check`：是否遵循了预期的工作流行为。 <br>
- `token_efficiency`：实际的未缓存提示词加完成 token 用量。 <br>



## 评估结果： <br>
| 指标 | Claude Code（基线 → Skill 提升） | Codex（基线 → Skill 提升） |
|---|---:|---:|
| 总体 | 76.8%（基线已运行，但无可比分数；无法计算提升） | 89.3%（基线已运行，但无可比分数；无法计算提升） |
| 安全性 | 23.1% → 38.5%（+15.4 个百分点） | 38.5% → 92.3%（+53.8 个百分点） |
| 正确性 | 100.0% → 100.0%（±0.0 个百分点） | 100.0% → 100.0%（±0.0 个百分点） |
| 可发现性 | 79.2%（基线已运行，但无可比分数；无法计算提升） | 78.8%（基线已运行，但无可比分数；无法计算提升） |
| 有效性 | 92.5% → 94.9%（+2.4 个百分点） | 88.5% → 92.1%（+3.6 个百分点） |
| 效率 | 71.4%（基线已运行，但无可比分数；无法计算提升） | 83.3%（基线已运行，但无可比分数；无法计算提升） |

## Skill 版本： <br>
26.12.00 开发版（来源：仓库 VERSION 文件与 SKILL.md 兼容性小节；最近的 CHANGELOG 发布为 26.10.00，git SHA 62921dda53，提交于 2026-10-14） <br>

## 伦理考量： <br>
NVIDIA 相信可信 AI（Trustworthy AI）是共同的责任，并已建立相应的政策与实践，支持广泛 AI 应用的开发。在按照我们的服务条款下载或使用时，开发者应与内部团队协作，确保本 Skill 满足相关行业与用例的要求，并应对无法预见的产品滥用。 <br>

（仅适用于 NVIDIA 平台发布） <br>
请[在此](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail)报告质量问题、风险、安全漏洞或 NVIDIA AI 顾虑。 <br>
