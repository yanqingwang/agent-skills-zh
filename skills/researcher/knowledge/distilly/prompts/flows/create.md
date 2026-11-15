> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/flows/create.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 创建人物 Skill

适用于 `colleague`、`relationship` 与 `celebrity` 三个人物家族的流程。所有 `prompts/...` 与 `tools/...` 路径都相对 `{distilly_skill_root}` 解析（见 `SKILL.md`）。

## 家族矩阵

下文每一步都从这张表读取对应的提示词。

| character | intake | persona analyzer | persona builder | merger | storage root |
|-----------|--------|------------------|-----------------|--------|--------------|
| `colleague` | `prompts/colleague/intake.md` | `prompts/colleague/persona_analyzer.md` | `prompts/colleague/persona_builder.md` | `prompts/colleague/merger.md` | `./skills/colleague/{slug}` |
| `relationship` | `prompts/relationship/intake.md` | `prompts/relationship/persona_analyzer.md` | `prompts/relationship/persona_builder.md` | `prompts/relationship/merger.md` | `./skills/relationship/{slug}` |
| `celebrity` | `prompts/celebrity/intake.md` | `prompts/celebrity/persona_analyzer.md` | `prompts/celebrity/persona_builder.md` | `prompts/celebrity/merger.md` | `./skills/celebrity/{slug}` |

所有人物家族共用：
- 工作分析器：`prompts/shared/work_analyzer.md`
- 工作构建器：`prompts/shared/work_builder.md`
- 修正处理器：`prompts/shared/correction_handler.md`

## Step 0: 确认人物家族

如果用户输入了 `/distilly`，先确认要蒸馏哪个人物家族：

1. `owner`：用户本人（个人 Agent 首次运行时的默认项）
2. `colleague`
3. `relationship`
4. `celebrity`

如果是 `owner`（包括"蒸馏我自己"），到此为止，改走 `prompts/flows/owner.md`。

如果宿主已传入明确的人物家族，立即锁定。

如果当前家族是 `celebrity`，还要确认研究档位：

1. `budget-friendly`
2. `budget-unfriendly`

默认用 `budget-friendly`。仅当用户明确想要更深入的研究、更高的置信度，或接受更慢更贵的蒸馏流程时，才切换到 `budget-unfriendly`。

## Step 1: 基础信息收集

按上表走该家族的信息收集提示词。问题内容、顺序与确认摘要由它负责；对 `celebrity`，它还确定收集策略与 `research_profile`。除别名外一切都可以跳过。继续之前先汇总并让用户确认。

## Step 2: 素材导入

按 `prompts/flows/sources.md` 提供导入选项，并读取用户提供的素材。

如果用户说"没有文件"或"跳过"，就只用 Step 1 的答案生成 Skill。

## Step 3: 分析素材

如果家族是 `celebrity`，先按所选研究档位执行 `prompts/flows/celebrity_research.md`。

然后沿两条轨道分析：

**轨道 A（工作技能）**：
- 参照 `prompts/shared/work_analyzer.md`
- 提取：负责的系统、技术标准、工作流、输出偏好、经验
- 对 `celebrity`，把 `work` 理解为方法、判断框架和决策模式，而不是字面的职务范围

**轨道 B（人设）**：
- 使用该家族专属的人设分析器
- 如果是 `celebrity` 且 `research_profile=budget-unfriendly`，使用：
  - `prompts/celebrity/budget_unfriendly/persona_analyzer.md`
- 把用户提供的标签翻译成具体的行为规则
- 从素材中提取：沟通风格、决策模式、人际行为
- 对 `celebrity`，保留：
  - 心智模型
  - 决策启发式
  - 表达 DNA
  - 矛盾
  - 诚实边界

## Step 4: 生成与预览

用 `prompts/shared/work_builder.md` 生成工作内容。
用上表中该家族的人设构建器生成人设内容；`celebrity` + `budget-unfriendly` 使用 `prompts/celebrity/budget_unfriendly/persona_builder.md`。

向用户展示摘要（各 5-8 行），并询问：
```
Work Skill Summary:
  - Responsible for: {xxx}
  - Tech stack: {xxx}
  - CR focus: {xxx}
  ...

Persona Summary:
  - Core personality: {xxx}
  - Communication style: {xxx}
  - Decision pattern: {xxx}
  ...

Confirm generation? Or need adjustments?
```

## Step 5: 写入文件

用户确认后，不要手工搭建 `skills/colleague/{slug}` 式的目录树。一律走 writer：

1. 解析当前存储根目录：
   - `colleague` → `./skills/colleague`
   - `relationship` → `./skills/relationship`
   - `celebrity` → `./skills/celebrity`
2. 用 `Write` 工具创建三个临时文件：
   - `/tmp/distilly_{slug}_meta.json`
   - `/tmp/distilly_{slug}_work.md`
   - `/tmp/distilly_{slug}_persona.md`
3. 临时 meta 文件至少要包含：
   - `name`
   - `display_name`
   - `character`
   - `research_profile`（`character=celebrity` 时必填）
   - `classification.language`（必须与用户的语言一致，例如 `zh-CN` 或 `en`）
   - `profile`
   - `tags`
   - `knowledge_sources`
4. 然后调用：
   ```bash
   python3 "{distilly_skill_root}/tools/skill_writer.py" \
     --action create \
     --character {character} \
     --research-profile {research_profile} \
     --slug {slug} \
     --name "{name}" \
     --meta /tmp/distilly_{slug}_meta.json \
     --work /tmp/distilly_{slug}_work.md \
     --persona /tmp/distilly_{slug}_persona.md \
     --base-dir {resolved_base_dir}
   ```
5. 这条命令会生成：
   - `SKILL.md`
   - `work.md`
   - `persona.md`
   - `work_skill.md`
   - `persona_skill.md`
   - `manifest.json`
   - `meta.json`
   - 要把生成的角色 Skill 安装进某个宿主，追加对应的旗标：
     - Claude Code：`--install-claude-skill`
     - OpenClaw：`--install-openclaw-skill`
     - Codex：`--install-codex-skill`
     - Hermes：运行 `python3 "{distilly_skill_root}/tools/install_generated_skill.py" --skill-dir "{resolved_base_dir}/{slug}" --host hermes --force`；对受信任的项目，追加 `--skills-dir .hermes/skills`，运行 `hermes skills trust`，然后开新会话或运行 `/reload-skills`。只有在 Hermes 的 `skills.external_dirs` 中明确配置时才使用 `~/.agents/skills`
     - DeepSeek Harness：运行 `python3 "{distilly_skill_root}/tools/install_generated_skill.py" --skill-dir "{resolved_base_dir}/{slug}" --host deepseek-harness --force`；项目级安装追加 `--skills-dir .dsh/skills`
     - Pi：运行 `python3 "{distilly_skill_root}/tools/install_generated_skill.py" --skill-dir "{resolved_base_dir}/{slug}" --host pi --force`；项目级安装追加 `--skills-dir .pi/skills`，然后用 `/skill:{character}-{slug}` 调用
     - Grok Build：运行 `python3 "{distilly_skill_root}/tools/install_generated_skill.py" --skill-dir "{resolved_base_dir}/{slug}" --host grok-build --force`；项目级安装追加 `--skills-dir .grok/skills`
     - OpenCode：运行 `python3 "{distilly_skill_root}/tools/install_generated_skill.py" --skill-dir "{resolved_base_dir}/{slug}" --host opencode --force`；项目级安装追加 `--skills-dir .opencode/skills`
     - 共享安装器只写入自包含的 `SKILL.md` 与安装元数据，并规范化安装副本中的旧式 frontmatter。不要手工复制整个生成目录；里面可能有私有素材
     - Windows 上的 Claude Code：可选追加 `--install-claude-command-shim`
6. 如果当前家族是 `celebrity`，创建之后运行质量检查：
   ```bash
   python3 "{distilly_skill_root}/tools/research/quality_check.py" "{resolved_base_dir}/{slug}/SKILL.md" --profile {research_profile}
   ```
7. 如果 `celebrity` Skill 的 `source_grounding` 仍然失败：
   - 可以补充诚实的能力限制说明，以及一份有真实来源依据的来源摘要
   - 只有真实、具体、可追溯的来源 URL 才能添加
   - **绝不**用站点根路径、专题页、搜索页或其他泛化链接冒充锚定
   - 如果没有可验证的外部来源，保持 FAIL 状态，并说明还缺什么素材

报告成功时，返回对应家族的正确存储位置，不要默认当成 colleague 的存储。
