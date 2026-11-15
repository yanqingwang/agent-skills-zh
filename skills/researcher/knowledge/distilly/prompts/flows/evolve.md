> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/flows/evolve.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 演进已有 Skill

所有 `prompts/...` 和 `tools/...` 路径都相对 `{distilly_skill_root}` 解析（见 `SKILL.md`）。

## 追加新材料

当用户提供新文件或新文本时：

1. 按 `prompts/flows/sources.md` 读取新内容
2. 解析当前家族的基础目录
3. `Read` 已有的 `{resolved_base_dir}/{slug}/work.md` 和 `persona.md`
4. 用 `prompts/{character}/merger.md` 做增量分析
5. 归档当前版本（Bash）：
   ```bash
   python3 "{distilly_skill_root}/tools/version_manager.py" \
     --action backup \
     --character {character} \
     --slug {slug} \
     --base-dir {resolved_base_dir}
   ```
6. 把 work/persona 的增量写入临时补丁文件
7. 调用：
   ```bash
   python3 "{distilly_skill_root}/tools/skill_writer.py" \
     --action update \
     --character {character} \
     --slug {slug} \
     --work-patch /tmp/distilly_{slug}_work_patch.md \
     --persona-patch /tmp/distilly_{slug}_persona_patch.md \
     --base-dir {resolved_base_dir}
   ```
8. 如果当前家族是 `celebrity`，更新后重跑质量检查

## 从对话中修正

当用户表达"这样不对" / "他应该是"时：

1. 参照 `prompts/shared/correction_handler.md` 识别修正内容
2. 判断它属于 Work（技术 / 工作流）还是 Persona（性格 / 沟通）
3. 属于 Work 时：
   - 生成 `/tmp/distilly_{slug}_work_patch.md`
   - 补丁必须是一个或多个可整体替换的 `##` 小节
   - 调用：
     ```bash
     python3 "{distilly_skill_root}/tools/skill_writer.py" \
       --action update \
       --character {character} \
       --slug {slug} \
       --work-patch /tmp/distilly_{slug}_work_patch.md \
       --base-dir {resolved_base_dir}
     ```
4. 属于 Persona 时：
   - 把修正记录写入 `/tmp/distilly_{slug}_correction.json`
   - 单条修正写 `{scene, wrong, correct}`
   - 多条人格修正写 `{"persona_corrections": [{...}, {...}]}`
   - 调用：
     ```bash
     python3 "{distilly_skill_root}/tools/skill_writer.py" \
       --action update \
       --character {character} \
       --slug {slug} \
       --correction-json /tmp/distilly_{slug}_correction.json \
       --base-dir {resolved_base_dir}
     ```
5. 如果当前家族是 `celebrity`，更新后重跑质量检查
6. 不要手改 `work.md`、`persona.md`、`SKILL.md` 或 `meta.json`；始终通过 `skill_writer.py` 更新
