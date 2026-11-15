> **中文汉化版** · 上游：[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) · 原文件：`skills/egm-brainstorm/TEST.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 测试计划：EGM Brainstorm Skill

Frontmatter 与链接检查在 `pytest tests/unit` 中运行（参见 [TESTING.md](../../TESTING.md)）。

## 协议验证清单

在聊天中交互式评估或试用 `egm-brainstorm` 时，核验以下几点：

-   **第 1 步（开放式澄清与就绪闸门）：** 用开放式聊天问题层层深挖半生不熟的
    概念（不使用结构化提问工具，也不提供多选题列表），并在启动子代理之前
    强制执行用户就绪检查点闸门。
-   **第 2 步（上游多视角构思）：** 从 7 个专门的金鱼视角评估功能概念
    （唱反调者/YAGNI；成本、配额与 token 经济学；UX 与开发者工效；迁移与向后
    兼容；可观测性与 SRE 可调试性；长期技术债与维护；创新催化剂）。
-   **第 3 步与第 4 步（概念简报交付与交接）：** 汇总并保存综合后的
    `concepts_brief.md` 制品，供用户审阅，并交接给 `/egm-draft`。
