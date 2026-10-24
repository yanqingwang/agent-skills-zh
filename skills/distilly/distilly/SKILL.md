---
name: distilly
description: "设置 owner profile，让个人 Agent 知道自己在为谁工作（首次运行设置，\"get to know me\"／了解我）；或将同事（colleague）、关系（relationship）、名人（celebrity）素材蒸馏为可复用的、供 Agent 使用的 Person Profile。"
argument-hint: "[character] [name-or-slug]"
version: "1.0.0"
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
---

> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`SKILL.md` · License: MIT
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

> **语言**：本说明以英文写成。请从用户的第一条消息检测其使用的语言，并在整个过程中以该语言回复用户。

> **Skill Root**：在读取随附的提示词文件或运行随附的脚本之前，先解析宿主实际加载的那份 `SKILL.md` 所在的绝对目录。在下述说明中，`{distilly_skill_root}` 即指该目录。Claude Code 将其暴露为 `${CLAUDE_SKILL_DIR}`；在所有其他宿主上，请使用该宿主的发现上下文所提供的已加载 Skill 路径。不要假设 shell 的当前工作目录就是 Skill 根目录，也不要猜测或硬编码安装路径。如果宿主未暴露已加载路径，或存在多个 Distilly 安装而无法分辨，请先让用户指明当前生效的安装，再运行代码。
>
> 请让 shell 保持在用户当前的工作区，以便 `./skills/...` 这类相对输出路径仍保持在项目本地。所有 `tools/...` 与 `prompts/...` 资源都相对于 `{distilly_skill_root}` 解析。例如，以 `python3 "{distilly_skill_root}/tools/owner_profile.py"` 的方式运行 `tools/owner_profile.py`；在实际的工具调用中把占位符替换为解析出的绝对路径。

# Distilly Creator

> Distilly 的前身是 **Colleague Skill / colleague-skill**。当前 Skill 的 frontmatter name 与创建者入口均为 `distilly`。

## 路由请求

只读取该请求所需的那份 flow 文件，然后照着执行。

| 用户说 | Flow |
|---------------|------|
| "设置我的 profile"／"了解我"／"我在你眼中是谁"、"蒸馏我自己"，或宿主首次运行且尚无 owner profile | `prompts/flows/owner.md` |
| `/distilly`、"帮我创建一个 Skill"、"创建一个新 Skill"、"我想蒸馏某个人"、"为 XX 做一个 Skill" | `prompts/flows/create.md`（其中的 Step 0 会把 `owner` 送回 owner flow） |
| "我有新文件"／"追加"、"这样不对"／"他不会这么做"／"他应该是"、`/update-skill {character} {slug}`，或别名 `/update-colleague {slug}` | `prompts/flows/evolve.md` |
| "展示我的 Skill"、回滚或删除某个已生成的 Skill | `prompts/flows/manage.md` |

create flow 还会引用 `prompts/flows/sources.md` 来导入素材，并在 `celebrity` 场景下引用 `prompts/flows/celebrity_research.md`。每个 flow 都会列明它需要的提示词文件；请等 flow 进行到那一步时再读取，不要提前预读。

## 每个 flow 的通用规则

- **存储**：生成的 Skill 存放在用户工作区的 `./skills/colleague/{slug}/`、`./skills/relationship/{slug}/` 或 `./skills/celebrity/{slug}/` 下。如需全局路径，请为该类别的存储根目录传入 `--base-dir`。
- **写入**：只能通过 `tools/skill_writer.py` 创建和更新生成的 Skill；绝不要手工构建或手工编辑它们的文件。
- **凭据**：App Secrets、访问令牌或刷新令牌、Bot Token 以及 OAuth 授权码绝不进入对话。绝不要向用户索要它们；用户应在自己的终端运行采集器的 `--setup` / `--login`。细节见 `prompts/flows/sources.md`。

## 兼容的宿主

Claude Code、OpenClaw、Hermes、Codex、DeepSeek Harness、Pi coding agent、Grok Build 与 OpenCode。在 Claude Code、Hermes、DeepSeek Harness 与 Grok Build 中以 `/distilly` 调用；在 OpenClaw 中用 `/distilly` 或 `/skill distilly`；在 Codex 中用 `$distilly` 或 `/skills`；在 Pi 中用 `/skill:distilly`。OpenCode 原生加载 Skill，没有专用命令。Grok Bot 无法直接导入本目录；不要把本仓库当作 Grok Bot 的安装来介绍。
