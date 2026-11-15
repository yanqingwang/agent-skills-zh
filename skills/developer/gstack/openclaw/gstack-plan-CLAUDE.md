> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/openclaw/gstack-plan-CLAUDE.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# gstack-plan：完整评审闯关

用户想为 Claude Code 项目做计划时，由 orchestrator 注入本文件。
追加到已有的 CLAUDE.md。

## 计划管线
1. 读 CLAUDE.md，理解项目上下文。
2. 运行 /office-hours 产出设计文档（问题陈述、前提、备选方案）。
3. 运行 /autoplan 评审该设计（CEO + eng + design + DX 评审 + codex 对抗评审）。
4. 把最终评审后的计划保存到 orchestrator 日后可引用的文件。
   写入当前 repo 的：plans/<project-slug>-plan-<date>.md。
   内容包括设计文档、全部评审决定和实现顺序。
5. 向 orchestrator 汇报：
   - 计划文件路径
   - 用一段话总结设计了什么、关键决定是什么
   - 已接受的范围扩展清单（如有）
   - 建议的下一步（通常是：spawn 一个 gstack-full 新会话来实施）

不要实现任何东西。本会话只做计划。
orchestrator 会把计划链接持久化到它自己的 memory/knowledge store。
