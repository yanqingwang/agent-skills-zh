> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/celebrity/budget_unfriendly/synthesis.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 名人 budget-unfriendly 综合提示词

## 任务

阅读：

- 六轨研究笔记
- `knowledge/research/reviews/research_audit.md`
- `prompts/celebrity/budget_unfriendly/framework.md`

构建一份综合评审，把以下内容区分开：

- 候选心智模型
- 候选启发法
- 被丢弃的观察

综合写入 `knowledge/research/reviews/synthesis.md`。

## 方法

对每个候选心智模型应用三重门槛：

1. 跨语境复现
2. 生成性
3. 独特性

对每个通过的模型，记录：

- 定义
- 证据锚点
- 它最先看到什么
- 它过滤掉什么
- 失效模式

对每个降级为启发法的候选，记录：

- 操作规则
- 适用语境
- 为什么没有资格成为完整模型

同时记录：

- 仍然重要的未解矛盾
- 降低置信度的证据缺口
- 至少 2 个后续验证应测试的已知答案锚点
- 1 个迫使外推、又不产生幻觉式确定性的边界情况问题

## 版权安全

- 不要把长段源文复制进综合评审
- 使用简短的署名行和转述

## 输出约束

用用户的语言书写。
