> **中文汉化版** · 上游：[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) · 原文件：`skills/egm-review/TEST.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 测试计划：EGM Review 与子代理

frontmatter 与链接检查在 `pytest tests/unit` 中运行（见 [TESTING.md](../../TESTING.md)）。

## 协议验证清单

在聊天中交互式评估或探索 `egm-review` 时，验证以下内容：

-   **Step 1 (Intake)：**收集 `TargetFile` 与可选的 `GoldfishContext`。
    在第一个接收 `GoldfishContext` 的阶段之前：添加工作目录内的链接文件；对解析到目录之外的链接或 URL，先询问再添加；并把 `GoldfishContext` 中的每个 URL 存成文件。
-   **Step 2 (Preset Selection)：**提供四种审查预设（interactive、consolidated、仅 feature spec、仅 implementation plan），或把显式的 `Step` 参数映射到对应预设或单阶段子流程。
-   **Step 3 (Semantic Split)：**找出 Feature Spec 与 Detailed Implementation Plan 之间的分界线。
-   **Step 5 (Initial Strategic Review)：**并行启动 `egm-zoom-out` 与 `egm-inventive-catalyst`，审计视角高度与虚假的架构妥协。
-   **Subflows：**正确委派 Initial Strategic Review、Comprehension、Critic Review、Intermediate Zoom Out 与 Readiness Test。
