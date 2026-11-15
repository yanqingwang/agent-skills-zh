> **中文汉化版** · 上游：[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) · 原文件：`skills/egm-draft/TEST.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 测试计划：EGM Draft Skill

Frontmatter 与链接检查在 `pytest tests/unit` 中运行（参见 [TESTING.md](../../TESTING.md)）。

## 协议验证清单

在聊天中交互式评估或试用 `egm-draft` 时，核验以下几点：

-   **步骤 4（备选方案）：** 从简报的 `Alternatives Weighed` 章节读取已否决的
    备选方案；若该章节缺失，则询问用户。
-   **步骤 6（定稿）：** 在选择目录之前，报告简报与草稿之间的矛盾，并等待用户
    逐条裁定。不会按 Zoom Out 标准对草稿做自我评判。
