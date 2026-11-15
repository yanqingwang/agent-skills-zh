> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/flows/manage.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 管理已生成的 Skill

所有 `tools/...` 路径都相对 `{distilly_skill_root}` 解析（见 `SKILL.md`）。`{character}` 取值为 `colleague`、`relationship` 或 `celebrity`；回滚或删除前先与用户确认。

列出一个家族的 Skill：
```bash
python3 "{distilly_skill_root}/tools/skill_writer.py" --action list --character {character} --base-dir ./skills/{character}
```

回滚某个 Skill 的指定版本：
```bash
python3 "{distilly_skill_root}/tools/version_manager.py" --action rollback --character {character} --slug {slug} --version {version} --base-dir ./skills/{character}
```

删除某个指定的 Skill：
```bash
rm -rf skills/{character}/{slug}
```
