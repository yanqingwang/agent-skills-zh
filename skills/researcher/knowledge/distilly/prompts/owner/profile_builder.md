> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/owner/profile_builder.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Owner Profile Builder（Owner 资料构建提示词）

把 intake 问答和用户提供的材料整理成一个 Markdown 文件，采用下面的结构。用 Owner 偏好的语言书写。各节标题可以翻译，但摘要标题必须原样保留 `## Always-on summary`，这样安装器才能找到它，无论资料其余部分用什么语言。（安装器也接受旧的中文标题，但新资料应使用英文标题。）

以第三人称书写 Owner，或写成对 Agent 的指令（"Prefers..."、"Ask before..."）。不要写成角色扮演人格。

```markdown
# Owner profile: {preferred name}

> Created by Distilly on {YYYY-MM-DD}. Reviewed by the owner.

## Always-on summary

- Name / how to address: ...
- Role and context: ...
- Timezone and languages: ...
- Current focus: ...
- Communication: ...
- Act vs. ask: ...
- Never: ...
- Rhythm: ...

## Work and projects
## Goals
## Communication preferences
## Decision style and autonomy
## Routines and availability
## Tools and accounts
## Boundaries and dislikes
## Open questions
## Sources

| Fact | Source | Date |
|------|--------|------|
| Prefers short replies | interview | {YYYY-MM-DD} |
| Deep work 9-12 on weekdays | calendar (inferred) | {YYYY-MM-DD} |
```

规则：

1. Always-on summary 每个会话都会加载，所以控制在 3,000 字符以内（OpenClaw 给 `USER.md` 的预算是 4,000 字符）。要点要短，最有价值的事实放最前面。
2. 其余小节存放细节，Agent 只在需要时才读。没有信息的小节直接跳过，不要凑内容。
3. 每一行都必须来自 Owner 的回答或材料。推断内容标注 `(inferred)`，未知项列入 `## Open questions`。
4. 遵守 `prompts/owner/intake.md` 中的隐私规则。
5. 资料中的每个事实都要在 `## Sources` 中有一行。来源标签从以下选用：`interview`、`host memory`、`user file`，或以 `<category>: <name>` 形式标注发现的来源（例如 `calendar: google-calendar`、`social: x`、`mail: gmail`），或 `export: <name>`。摘要要点里不要带来源标签；标签放在表格里。
6. 来源之间有冲突时，优先采用 Owner 在访谈中的说法，其次新的优先于旧的。未解决的冲突列入 `## Open questions`。
7. 摘要长度上限取决于宿主：摘要超出宿主可接受的长度时，安装器会拒绝（`tools/owner_profile.py`）。

保存前把完整资料展示给 Owner，并按其修正意见修改。
