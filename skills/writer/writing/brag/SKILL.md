---
name: brag
description: 使用 Hyperframes 把当前项目网站制作成简短、精致、可分享的发布视频。当有人说 "/brag"、"let's brag about this"（来 brag 一下）、"make a launch video"（做个发布视频）、"turn this into a video"（把它变成视频），或想分享自己构建的东西时使用。直接读取项目代码——无需在线 URL 或截图。
---

> **中文汉化版** · 上游：[latent-spaces/brag](https://github.com/latent-spaces/brag) · 原文件：`skills/brag/SKILL.md` · License: MIT
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# /brag

你把它构建出来了。现在来 brag 一下。

## 调用分派（必须最先执行）

**模型检查。** 如果你是 Claude Opus 5.5，且调用没有要求完整工作流（`--full`、"use the full brag"）或配音（`--voice`，brag-slim 不支持配音），切换到 brag-slim：读取 `<skill-dir>/slim.md`（即 /brag-slim skill，已收录在本目录），并在本次运行的剩余部分改用它，而不是本文件。把用户的输入传递过去，并将其他选项（`--no-music`、`--title` 等）作为自然语言指示传递。先用一句话告知用户，例如："你在用 Opus 5.5，所以我改用 /brag-slim：我自己构建整个视频。说 'use the full brag' 可以切回完整版。" 如果你是其他任何模型，或无法判断自己是什么模型，跳过此检查。

在检查项目之前，先解析完整的 `/brag` 调用。如果调用中包含
`--voice`，则设置 `voice.enabled = true`。仅在本次运行中启用旁白。
不要自动启用旁白，也不要回退到
普通的无语音工作流。

`/brag` 使用 Hyperframes 把当前项目网站或应用变成一个简短、精致、可分享的发布视频。它范围狭窄、观点鲜明，而且有趣。

## 这个 skill 做什么

1. 读取当前项目代码，理解这个应用。
2. 针对这个项目规划一个简短的 brag 创意。
3. 为视频撰写脚本和分镜。
4. 把一份聚焦的合成简报交给 Hyperframes。
5. 校验、渲染并撰写分享文案。

## 解析调用

用户可以用自然语言或标志（flags）调用：

```
/brag
/brag --tone chaotic
/brag --tone polished --format vertical
/brag this. Make it feel like a ridiculous startup launch.
```

解析以下选项：

| 选项 | 取值 | 默认值 |
|---|---|---|
| `--tone` | 预设或自由描述 | 推断 |
| `--format` | `landscape`、`vertical`、`square` | `landscape` |
| `--duration` | 秒数 | 自动（15-25 秒） |
| `--no-music` | 标志 | 开启音乐 |
| `--no-sfx` | 标志 | 开启音效 |
| `--title` | 字符串 | 从项目推断 |
| `--voice` | 标志 | 关闭旁白 |

配音是可选加入的。如果出现 `--voice`，通过 Hyperframes 使用 Kokoro，
不要添加任何供应商选择逻辑。语音工作流刻意保持
单一供应商。

Tone 可以是预设（`default`、`polished`、`yc-parody`、`chaotic`、`deadpan`、`cinematic`、`app-store`），也可以是创意方向，例如 "fake Series A launch from 2016"（2016 年的假 A 轮融资发布）、"museum exhibit"（博物馆展品）或 "overproduced mobile game ad"（过度制作的手机游戏广告）。

当用户给出自由格式的 tone 方向时，把它映射到最接近的预设以保证节奏和结构，但在计划和合成简报中保留用户的指示。

## 旁白指引

启用 `--voice` 时，撰写的旁白应与视觉画面互补，
而不是简单朗读屏幕上可见的文字；要匹配场景节奏，听起来自然、
口语化，并在场景之间平滑过渡。保持脚本简洁
且切合产品，让语音感觉是剪辑的一部分，而不是
独立的旁白轨道。

---

## 输出目录

默认情况下，输出到 `brag-output/`。为避免覆盖之前的运行结果，可使用带时间戳的目录：

```
brag-output-2026-05-04-143022/
```

在以下情况使用时间戳：
- 用户明确要求一次新的运行且不覆盖之前的结果
- 项目中已存在 `brag-output/` 目录

在运行开始时生成时间戳（`YYYY-MM-DD-HHmmss`），并在该次运行的所有输出路径中一致使用：计划、简报、合成、渲染和分享文案。

## Skill 目录

`<skill-dir>` 是包含本 `SKILL.md` 的目录。Claude Code 在 skill 加载时会以 "Base directory for this skill" 打印它；对其他 agent 来说，则是 skill 被安装到的位置。捆绑资源在 `<skill-dir>/assets/` 下，脚本在 `<skill-dir>/scripts/` 下。不要猜测安装路径：插件安装、`~/.claude/skills/` 副本和本仓库各自会把它放在不同的地方。

---

## 第 1 步：检查项目

**阅读：** [references/step-1-inspect.md](references/step-1-inspect.md)

扫描项目目录，提取规划 brag 视频所需的信息。

**门槛（Gate）：** 你能回答 brag 规划量规中的全部 9 个问题。

---

## 第 2 步：规划与分镜

**阅读：** [references/step-2-plan.md](references/step-2-plan.md)

写入 `<output-dir>/brag-plan.md`（其中 `<output-dir>` 是 `brag-output/` 或上面选择的时间戳变体）。回答规划量规。敲定一个创意角度。写出逐拍分镜，包括场景、文字、时序、转场和 SFX 提示。

选定音乐时，加入一个简短的 `Music cue guidance` 章节：如果存在，从 `<skill-dir>/assets/music/cues/` 读取捆绑曲目的 cue 预设；否则注明将在合成时检测 cue（现在任何曲目都支持节拍同步——见 `references/audio.md`）。Cue 元数据只是可选的时序指引：故事、可读性、节奏和产品清晰度始终优先。

**门槛（Gate）：** `<output-dir>/brag-plan.md` 存在且包含完整分镜。场景时长之和为 15–25 秒。

---

## 第 3 步：交接给 Hyperframes

**阅读：** Hyperframes skills——`hyperframes`（契约，`references/format.md`、`references/motion.md`、`references/look.md`）、`hyperframes-cli`、`hyperframes-registry`，以及音频相关的 `media-use`。/brag 有自己的工作流：跳过 `hyperframes` 的 storyline 步骤：不要读 `references/types/*` 或 `references/story.md`，不要提出 storyline，也不要写 `SPEC.md`。brag 计划和合成简报取代它们，包括 `references/look.md` 要求的 LOOK 行。同时跳过它的 `usage`、`history`、`feedback` 和 REVIEW.md 步骤；`check` 就是 brag 的门槛。不要进入它的通用 launch-video 工作流。
**阅读：** [references/step-3-compose.md](references/step-3-compose.md)
**阅读：** [references/audio.md](references/audio.md)

撰写合成简报，并使用 Hyperframes 在 `<output-dir>/composition/` 中创建视频实现。

`/brag` 负责产品角度、素材、分镜、tone、格式、音频选择、music cue 指引和交付预期。Hyperframes 负责具体的合成结构、精确的动画时序、动画机制、运行时选择、lint 规则和渲染工作流。

**门槛（Gate）：** 在 `<output-dir>/composition/` 内 `npx hyperframes check` 以零错误通过（渲染前的唯一浏览器门槛——它审计什么见 hyperframes-cli）。

---

## 第 4 步：校验、渲染与交付

**阅读：** [references/step-4-deliver.md](references/step-4-deliver.md)

校验、预览、渲染到 `<output-dir>/brag.mp4`，挑选最佳海报帧存入 `<output-dir>/brag.jpg`，把该海报烘焙为视频的第 0 帧使其在所有场景下都是静置缩略图，并写入 `<output-dir>/share-copy.txt`。

**门槛（Gate）：** `<output-dir>/brag.mp4` 存在。已挑选最佳帧海报 `<output-dir>/brag.jpg`（不是任意帧）并烘焙为 `brag.mp4` 的第 0 帧。分享文案已写入。

---

## Tone 系统

`/brag` 自带七个 tone 预设。每个预设都会改变脚本能量、节奏、排版个性和转场风格。预设是默认值，不是限制。

完整定义：[references/tones.md](references/tones.md)

| Tone | 能量 | 一句话简介 |
|---|---|---|
| `default` | 俏皮、干净、适合发帖 | 氛围友好的默认选项 |
| `polished` | 严肃、优雅 | 给不是开玩笑的项目 |
| `yc-parody` | 面无表情的创业能量 | 给荒诞项目套上假装的严肃 |
| `chaotic` | 快速、喧闹、激进 | 夸张过头、放飞自我 |
| `deadpan` | 平静、干、低调 | 笑点在于一切都不是笑话 |
| `cinematic` | 戏剧化、预告片级别 | 大动作，更大的口号 |
| `app-store` | 顺滑、功能卡片式干净 | 企业感但不无聊 |

始终允许自由创意方向去精调或覆盖预设。

---

## 创意法则

以下法则适用于每个 brag 视频，无论 tone 如何。

**短。** 15–25 秒。没有理由就不要多一秒。无论旁白是否开启都成立；旁白不会延长这个时间窗口。

**可读。** 通过运动和剪辑保持高节奏，绝不用闪烁文字来提速。观众需要阅读的每一行文字都要停留足够长的时间让人读完（短标签约 0.8 秒定格；一句话约每词 0.3 秒）。快速进入，然后停留——绝不能快速进入，然后消失。

**具体。** 视频必须让人感觉是为这个确切的项目制作的，而不是为任何项目。

**展示产品本身。** 至少一个场景必须展示产品的真实 UI、文案或关键视觉。不要抽象的填充内容。

**不要通用 SaaS 语言。** "Streamline your workflow"（简化你的工作流）是被禁止的。使用项目实际的文案和主张。

**钩子就是一切。** 前 2 秒决定人们是否继续观看。先规划钩子，再规划其他一切。

**幽默要配得上它的位置。** 幽默应来自项目本身的荒诞，而不是来自刻意搞笑。

**模式：**
```
Hook (2-3s) → Reveal (2-4s) → 2-3 sharp highlights (5-12s) → Punchline/outro (2-4s)
```

对这个模式进行调整。不是每个项目都需要恰好 3 个亮点。这个模式是起始形状，不是模板。
