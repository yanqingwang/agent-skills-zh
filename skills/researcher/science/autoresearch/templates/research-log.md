> **中文汉化版** · 上游：[Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) · 原文件：`0-autoresearch-skill/templates/research-log.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 研究日志

按时间顺序记录研究决策与动作。只追加。

| # | 日期 | 类型 | 摘要 |
|---|------|------|---------|
| | | | |

<!-- 条目类型：
  bootstrap    ：初始范围界定、文献检索、假设形成
  inner-loop   ：实验运行与结果
  outer-loop   ：综合、反思、方向决策
  pivot        ：研究方向变更
  report       ：生成进度汇报
  conclude     ：决定定稿并撰写论文

示例条目：
| 1 | 2026-03-15 | bootstrap | 检索 Semantic Scholar + arXiv 上高效 transformer 架构的文献。找到 8 篇相关论文。空白：小模型上缺少 GLU 变体的系统对比。形成 3 个假设。基线：NanoGPT 5 分钟训练，val_loss=4.82。 |
| 2 | 2026-03-15 | inner-loop | H1 run_001：FFN 中把 ReLU 换成 SwiGLU。5 分钟训练。val_loss=4.61（基线 4.82，delta -0.21）。保留。 |
| 3 | 2026-03-15 | inner-loop | H1 run_002：FFN 隐藏维度从 4x 提到 5.3x，以匹配 SwiGLU 的参数量。val_loss=4.58（比 run_001 -0.03）。收益边际：SwiGLU 的好处主要来自门控，而非额外参数。 |
| 4 | 2026-03-15 | inner-loop | H1 run_003：尝试用 GEGLU 替代 SwiGLU。val_loss=4.63。略差于 SwiGLU。该规模下 SwiGLU 更优。 |
| 5 | 2026-03-15 | inner-loop | H2 run_004：把可学习的位置嵌入换成 RoPE。val_loss=4.55（比 SwiGLU 基线 -0.06）。有前景：可与 SwiGLU 叠加。 |
| 6 | 2026-03-15 | inner-loop | H2 run_005：RoPE + SwiGLU 组合。val_loss=4.41（比最初基线 -0.41）。目前最佳。 |
| 7 | 2026-03-16 | outer-loop | 复盘 5 次运行。规律：门控机制（SwiGLU）与旋转位置编码（RoPE）带来独立且可叠加的收益。合计提升约 9%。但为什么能叠加？假设：二者作用于正交的方面（FFN 表达能力 vs 位置编码）。方向：DEEPEN，测试加入 RMSNorm 是否也能独立叠加。 |
| 8 | 2026-03-16 | inner-loop | H3 run_006：把 LayerNorm 换成 RMSNorm。val_loss=4.39（-0.02）。小幅收益。可以叠加，但归一化方面收益递减。 |
| 9 | 2026-03-17 | outer-loop | 8 次运行完成。优化在 val_loss=4.38 附近进入平台期。容易拿到的架构收益（SwiGLU、RoPE）已经到手。检索训练动力学文献，找到几篇小规模下 warmup 调度的论文。方向：BROADEN，从架构转向训练配方。 |
| 10 | 2026-03-17 | report | 生成 progress-001.html，其中的轨迹图显示架构改动带来 9% 提升。 |

示例条目（发现型研究：理解 grokking）：
| 1 | 2026-03-20 | bootstrap | 检索 grokking 与延迟泛化的文献。找到 Nanda et al. 的进展度量、Grokfast 谱滤波。空白：与神经科学的记忆巩固理论没有建立联系。形成 3 个假设。 |
| 2 | 2026-03-20 | inner-loop | H1 run_001：训练模加法 transformer 直到记忆完成（训练准确率 100%，测试 0%）。记忆所需步数：1200。基线已建立。 |
| 3 | 2026-03-20 | inner-loop | H1 run_002：用标准 weight decay 继续训练。第 48000 步出现 grokking。全程记录进展度量：第 44000 步出现急剧转变。 |
| 4 | 2026-03-20 | inner-loop | H1 run_003：在第 20000 步插入"睡眠阶段"（升高 weight decay + 振荡学习率，持续 500 步）。grokking 提前到第 31000 步。加速 35%。 |
| 5 | 2026-03-20 | inner-loop | H1 run_004：睡眠阶段放在第 10000 步。grokking 出现在第 27000 步。睡眠越早，grokking 越早。 |
| 6 | 2026-03-20 | inner-loop | H1 run_005：睡眠阶段放在第 5000 步（记忆尚未完成）。grokking 反而推迟到第 38000 步。太早有害：模型记得还不够多，巩固无从发挥作用。 |
| 7 | 2026-03-21 | outer-loop | 复盘 5 次运行。规律清晰：睡眠阶段能加速 grokking，但只在记忆完成之后。这与记忆巩固理论完全吻合：先有记忆形成，巩固才能重组它们。检索了神经慢波睡眠文献。睡眠阶段中的 weight decay + 振荡学习率模拟的是突触缩减（synaptic downscaling）。方向：DEEPEN，围绕记忆完成时点扫描睡眠插入时机。 |
| 8 | 2026-03-21 | inner-loop | H1.1 run_006-010：按记忆步数的 80%、100%、120%、150%、200% 扫描睡眠插入时机。最佳区间在 110-120%。3 个随机种子结果一致。 |
| 9 | 2026-03-22 | outer-loop | 10 次运行完成。故事已经清晰：神经网络像大脑一样"以梦助学"，巩固发生在编码之后，而非编码期间。Grokfast 用另一机制（梯度谱滤波）达到相近的加速。下一步：比较我们睡眠阶段与 Grokfast 滤波期间的梯度谱，看二者是否收敛到同一信号。方向：BROADEN。 |
| 10 | 2026-03-22 | report | 生成 progress-001.html，含睡眠时机与 grokking 步数的关系图。关键视觉：最佳区间曲线与神经科学的记忆巩固窗口形状吻合。 |
-->
