> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/flows/owner.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Owner Profile（Owner 资料构建）

为 Agent 的 Owner 建立一份资料，让 Agent 从第一个会话起就知道自己在为谁工作。它是 Agent 每个会话都会读取的**上下文**，不是角色扮演 Skill：不要生成 `{character}-{slug}` Skill，绝不要写"you are <user>"。

1. 用 `{distilly_skill_root}/prompts/owner/intake.md` 收集信息：先**发现**这个 Agent 已有的来源（本会话中的工具、连接器和记忆，Agent 所在的平台如 Grok 的 X 账号，以及 `tools/owner_sources.py discover` 在本机找到的用户文件、连接器配置和导出），而不是走一份固定清单；提出建议读取的来源，询问用户用哪些、是否补充其他来源；只读用户选中的来源，且只读不写；然后只问来源没有回答的问题。只使用宿主自带的工具；在这条路径上绝不索要 API key 或要求配置 OAuth，也不要使用 Lark、钉钉或 Slack 采集器。
2. 用 `{distilly_skill_root}/prompts/owner/profile_builder.md` 构建资料，写入 `/tmp/distilly_owner_profile.md`，把全文展示给用户并按其修正意见修改。
3. 用户确认后保存：
   ```bash
   python3 "{distilly_skill_root}/tools/owner_profile.py" save --profile /tmp/distilly_owner_profile.md
   ```
4. 把资料链接进当前宿主的常驻用户文件。先展示 `--dry-run` 结果，用户同意后才写入：
   ```bash
   python3 "{distilly_skill_root}/tools/owner_profile.py" link --host claude-code --dry-run
   python3 "{distilly_skill_root}/tools/owner_profile.py" link --host claude-code
   ```
   Claude Code 使用 `~/.claude/CLAUDE.md`；OpenClaw（`--host openclaw`）使用工作区的 `USER.md`。其他宿主暂不支持；告诉用户完整资料在 `~/.distilly/owner/profile.md`。
5. 只有 Distilly 标记之间的文本会被改动；文件其余部分原样保留，且会先备份原文件。之后删除 `/tmp/distilly_owner_profile.md`。

更新：当用户纠正内容或补充信息时，编辑完整资料，然后重新运行 `save` 和 `link`。撤销方法：`owner_profile.py unlink --host <host>`。
