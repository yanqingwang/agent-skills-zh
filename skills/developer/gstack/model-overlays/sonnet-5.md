{{INHERIT:claude}}

> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/model-overlays/sonnet-5.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

**Instructions are read literally（指令按字面读取）。** Sonnet 5 不会把一条
指令从一个条目静默推广到下一个，也不会推断你没有提出的请求。
当某条指令应该广泛适用时，明说出来（"apply this to every section,
not just the first"）。对遗留的风格类指令重新校准基线：它们现在会按字面生效。

**Scope work to the request（工作范围贴合请求）。** 尤其在低 effort 档位时，
Sonnet 5 只做被要求的事，不主动加码。如果在真正复杂的任务上推理显得浅，
那是 effort 信号：调高 effort，而不是加散文式护栏。

**Verbosity tracks task complexity（篇幅跟随任务复杂度）。** 回复长度按任务
看起来的复杂度校准：查询类更短，开放式分析更长。如果你需要特定长度或格式，
明说出来；给出目标格式的正面示例，胜过一句"don't be verbose"。
