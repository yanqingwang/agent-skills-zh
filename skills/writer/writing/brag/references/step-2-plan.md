> **中文汉化版** · 上游：[latent-spaces/brag](https://github.com/latent-spaces/brag) · 原文件：`skills/brag/references/step-2-plan.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 第 2 步：写 brag 计划

写 `<output-dir>/brag-plan.md`。一页，聚焦。它是整支视频的创作北极星。

计划应写明视频必须传达什么、必须用到哪些项目素材。不应规定底层的 Hyperframes 实现细节。具体的合成结构、动画机制和渲染流程，Hyperframes 会根据第 3 步的简报自行决定。

## 创建输出目录

```bash
mkdir -p <output-dir>
```

## brag-plan.md 的结构

```markdown
# Brag Plan: [App Name]

## What is this app?
[One sentence. What it does, what makes it funny or impressive.]

## The angle
[The creative premise. The joke, the hook, the claim.
What makes this video specific to this project and not generic.]

## Hook (first 2-3 seconds)
[The opening moment. This is the most important decision.
What word, image, or motion earns the next 20 seconds?]

## Key moments (the middle)
[2-3 sharp highlights from the product.
Bullet points. Specific. "The altitude meter counting up." 
Not "feature callouts."]

## Outro / punchline
[How does it land? The final line. The beat before the logo.]

## User flow worth showing
[The 2–3 beats of *using* the product (entry → key action → result), pulled from
Step 1 question 9. This is the strongest material the video has — the centerpiece
scenes should show the flow, not just landing-page sections. If the project is
landing-page-only, write "none — landing-page only" and rely on Key moments instead.]

## Tone
- Preset: [default / polished / yc-parody / chaotic / deadpan / cinematic / app-store]
- Creative direction: [freeform phrase, inferred or user-provided]
- Interpretation: [one sentence on how this affects pacing, writing, visual energy, and restraint]

## Format: [landscape / vertical / square] — [width]x[height]
## Duration: [target seconds]

## Visual identity (from the project)
- Background: [exact color value]
- Accent: [exact color value]
- Text: [exact color value]
- Display font: [name]
- Body font: [name]
- Strongest visual element: [what from the site to reference]

## Share copy (draft)
[One sentence for Twitter/X/LinkedIn/Discord. Punchy. Not corporate.]

## Audio direction
- Role: [warm bed / sparse professional accents / cinematic support / dense rhythmic layer / intentional silence]
- Music: [candidate track / mood / none only if disabled, missing, or intentionally silent]
- Music treatment: [start time, volume posture, fade-in/out intent, beat/swell notes]
- Music cue guidance: [preset cue file read / unavailable; list 1-3 strongCue timestamps for major moments; list beat-grid windows for sequential events]
- Audio-reactive treatment: [none / subtle / expressive; what visual qualities may respond to music energy]
- SFX posture: [sparse / moderate / dense; motion-matched; professional restraint]
- Audio-coupled moments: [visual ideas that should consider sound, e.g. typed text, beat reveal, count-up, card sequence]
- Restraint rule: [what audio must not do]

## Storyboard

### Scene 1 — [name] — [duration]s
[What's on screen. What text appears. What product material must be referenced.]
Sequential/interaction: [yes — describe what appears one by one or what interaction is simulated, e.g. "3 stat cards arrive one by one" or "cursor clicks the match button"; or none]
Audio intent: [what the sound should do emotionally]
Audio-coupled idea: [typed text, beat-aligned reveal, counter ticks, card-by-card sequence, simulated tap/swipe/type — or none]
Music: [mood, or "none" only if disabled / missing / intentionally silent]
Transition mood: [clean / hard / dramatic / soft / chaotic] → Scene 2

### Scene 2 — [name] — [duration]s
[...]
Sequential/interaction: [yes — describe it; or none]
Audio intent: [what the sound should do emotionally]
Audio-coupled idea: [type or none]
Transition mood: [mood] → Scene 3

[... continue for all scenes]

**Music mood for this video:** [upbeat / cinematic / chaotic / deadpan / parody / none only if disabled / missing / intentionally silent]
**Audio summary:** [one sentence describing the full audio arc]
```

## 规划场景

默认模式是：
```
Hook → Reveal → 2-3 highlights → Punchline/outro
```

但要按需调整。每种 tone 合适的场景数如下：

| Tone | 场景数 | 节奏 |
|---|---|---|
| `default` | 4-5 | 舒适。每个时刻都有呼吸空间。 |
| `polished` | 3-4 | 场景更少，停留更长。用克制传递自信。 |
| `yc-parody` | 4-5 | 有结构。笑点在于讲得有多一本正经。 |
| `chaotic` | 6-8 | 快速。有些场景不足 2 秒。 |
| `deadpan` | 3-4 | 长停留。大片留白。一次一个词。 |
| `cinematic` | 4-5 | 大远景。大字号。戏剧性揭晓。 |
| `app-store` | 4-6 | 功能卡片。干净的揭晓。不凌乱。 |

## 时长指引

各场景时长总和必须在 15-25 秒。要真的去加一遍。

- 不足 15 秒：太单薄，加一个场景或拉长停留。
- 超过 25 秒：砍一个场景或收紧时序。
- 18-22 秒是大多数 brag 视频的甜点区。

## 阅读时间（保持节奏，不牺牲文字）

高节奏来自快动效、快转场和紧凑剪辑，而不是把文字没读完就拽下屏。观众必须读的每个文字元素，都需要足够的完全可见、稳定停留时间（已入场、尚未退场）让人真正读完：

- 短标签或 1-3 个词的行：约 0.8 秒稳定停留。
- 标题或完整句：每词约 0.3 秒，最少约 1.2 秒。钩子那句给最多。

先把这个下限排进去，其余一切保持快：入场和转场依然干脆（0.3-0.6 秒），动效依然有劲。一句话可以猛砸进来然后稳稳停住：快进加足够停留，既有冲击力又看得清。

两个要在计划阶段就设计掉的失败模式：

- **文字量超出场景时长。**4 秒场景按下限算只容得下 2-3 次短阅读，不是 6 次。场景文字超过时长能承载的量，就删文案或拆场景，不要加速。
- **顺序文本吸附到过快的节拍。**110+ BPM 下节拍网格的揭晓可以密到约 0.5 秒一个（bicycles 的规格行就是这么被赶坏的）。这种间隔给点缀（光晕、圆点、刻度）没问题，给要读的行太快。顺序文本要每项都守住下限：隔拍吸附，或快速全部显现后整组留在屏幕上。任何顺序文本揭晓都要在分镜里标出预期停留。

## 选什么来展示

每支 brag 视频必须展示产品里真实的东西。选项按优先级排列：

1. **复刻一个应用运行的瞬间**：上传界面、结果视图、带着真实感内容的仪表盘。用 `app/`、`pages/` 或路由组件里的真实源码，不只是落地页。产品有流程时这是最有说服力的选项。产品*做事*胜过产品*说自己做事*。
2. **用 HTML 复刻一个 UI 元素**：主视觉卡、滑动 UI、进度表、数据块。没有流程可展示时很有力。
3. **把核心概念做成动画**：产品是"给出租车打车的出租车"，就动画呈现两辆出租车、一辆装在另一辆里。纯图形，但扎根于想法。
4. **以文字为主的序列**：产品靠文案驱动（Psychologists for Chatbots）时，让文案本身当视觉。巨大的展示字体，极少的装饰。

绝不拿抽象图案、色块晕染或任何视频都能套的通用动效填场景。

## 分镜向用户流程倾斜

如果第 1 步问题 9 找到了真实的用户流程，**核心场景必须展示那个流程**，不能只是落地页复刻。

好（应用运行场景）：
- "上传界面：光标拖入一个视频文件。文件名出现。进度条 1.2 秒内从 0 充到 100%。"
- "三张结果缩略图依次弹出：0:15、0:23、0:31。每张都是竖版剪辑帧，配真实感的字幕。"
- "收件箱行出现，挂上绿色的 'resolved' 徽章，从列表顶部滑走。"

避免（有流程可用时只做营销场景）：
- "16:9 → 9:16 转换示意图"：那是*产品功能的示意图*，不是产品在做事。
- "三张数据卡：10x faster / 0 cuts / 3 clips"：那是落地页的社会证明栏，不是产品。

数据卡、标题块和落地页主视觉仍有位置：最多用一个，作为围绕流程的画框，不是替代品。核心是运行中的应用。

项目没有应用（纯落地页静态站）时，跳过这一节，改为复刻落地页最强的视觉。

## 找交互与顺序揭晓时刻

写分镜前先问：**这个产品有没有能一个个出现的东西，或能模拟的动作？**

这些是 brag 视频里最有效的时刻：它们让产品显得鲜活、真实，而不是一沓幻灯片。找这些：

- **顺序揭晓**：功能卡、数据、列表项、匹配结果、资料卡、菜单选项，一切成组出现的东西。设计成一个个出现，让声音和动效互相强化每一次登场。这是分镜决策，不是音频上的事后补丁。
- **模拟交互**：产品涉及滑动、点击、打字、选择或切换，就演出来。光标点按钮、卡片上滑动手势、往输入框里打字，都能把静态样机变成演示。手势进了分镜，声音自然就对上动作。

场景里有其中任何一种，就在场景描述里明确写死：
- 好："3 张马的资料卡一张张滑入，每张配一个纸牌音"
- 好："在 Thunder 的资料卡上模拟一次右滑"
- 好："钩子句逐字符打出，配键盘音"
- 避免：写得含糊，指望 Hyperframes 自己加节奏

Hyperframes 两种模式都能实现好：前提是计划写明什么在出现、按什么顺序、交互在被模拟。计划就是契约。

## 音频规划

在计划里定音乐方向。具体 SFX 文件选择和具体时间戳留给 Hyperframes 在合成时决定，因为 SFX 要贴合实际视觉实现。

默认姿态：带音频。选一段音乐底加几个有品味的 SFX，除非用户传了 `--no-music` / `--no-sfx`、素材缺失，或静音本身就是概念的一部分。

每个场景记下预期的音频角色和可能的声画耦合机会：

格式：`Audio-coupled idea: type the hook with subtle key ticks if Hyperframes uses a typing animation.`

音频响应式视觉要写明什么响应、克制到什么程度。示例：`Audio-reactive treatment: subtle; use music RMS/bass to make the hero glow and product card presence breathe, not to add waveform bars.`

`brag-plan.md` 里不要求写具体 SFX 文件名，除非用户明确点名某个声音，或对应关系无法避免。优先写时刻类型和意图。

具体文件、密度、时间戳由 Hyperframes 自由选择，目标是让视频顺滑、专业。

tone 要求克制时不要过度规定音频。`yc-parody` 或 `deadpan` 用更少更轻的提示，但精致的克制好过没有音频。

## 音乐 cue 指引

节拍/cue 同步现在对任意曲目可用（见 `audio.md` 的 "Beat and cue sources"）：随附曲目有预计算预设；自定义曲目在合成时用 `analyze_music_cues.py`（丰富、需要 Python）或 `npx hyperframes beats`（简单、零依赖）生成 cue。计划选了音乐，就在 `brag-plan.md` 加一个紧凑的 `Music cue guidance` 小节：

- 曲目名，以及有预设时的 tempo。
- 大视觉时刻要瞄准的 1-3 个强 cue 时间戳：随附曲目取自预设，否则注明"合成时检测"。
- 分镜中所有顺序揭晓的节拍网格窗口。
- tone 是 deadpan、yc-parody 或其他安静取向时，加一条克制说明。

cue 来源、JSON schema 和节拍同步容差见 `audio.md`。

SFX 开启时，记下可能的发声机会，具体文件名留给 Hyperframes。Hyperframes 应在合成时使用本 skill 的 `sfx-analysis.md`。

## 交接姿态

- 好："复刻滑动卡，用 Thunder 的资料和干草标签。"
- 好："用源站的琥珀/深色调和衬线标题感。"
- 好："数据揭晓要有 deadpan 创业指标幻灯片的感觉。"
- 避免："用 GSAP 时间线、这个选择器、这个缓动。"
- 避免："用这个确切的 HTML 结构。"
- 避免："加载这个具体的运行时 URL。"

## 转场词表

转场与 tone 匹配：

| Tone | 偏好转场 |
|---|---|
| `default` | 交叉淡化、干净擦除 |
| `polished` | 柔和交叉淡化、滑动 |
| `yc-parody` | 硬切、极简 |
| `chaotic` | 硬切、闪白、缩放 |
| `deadpan` | 缓慢交叉淡化、长停留 |
| `cinematic` | 戏剧性擦除、交叉淡化 |
| `app-store` | 滑动、平滑擦除 |
