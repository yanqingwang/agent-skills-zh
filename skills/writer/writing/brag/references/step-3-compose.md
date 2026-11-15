> **中文汉化版** · 上游：[latent-spaces/brag](https://github.com/latent-spaces/brag) · 原文件：`skills/brag/references/step-3-compose.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 第 3 步：交给 Hyperframes

## 撰写合成简报

在创建或编辑 Hyperframes 合成之前，先写 `<output-dir>/composition-brief.md`。

```markdown
# Hyperframes Composition Brief: [App Name]

## Objective
Create a short launch-style brag video for [App Name].

## Output
- Composition directory: `<output-dir>/composition/`
- Rendered video: `<output-dir>/brag.mp4`
- Format: [landscape / vertical / square] — [width]x[height]
- Duration: [15-25 seconds]

## Source Material
- Project root: [path]
- Primary files read: [index.html, styles.css, README, etc.]
- Product name: [name]
- Tagline / strongest claim: [line]
- Key UI or visual moment to recreate: [specific element]
- Copy that must appear verbatim:
  - [line 1]
  - [line 2]

## Creative Direction
- Tone preset: [default / polished / yc-parody / chaotic / deadpan / cinematic / app-store]
- Creative direction: [freeform phrase, inferred or user-provided]
- Interpretation: [how tone affects pacing, writing, visual energy, and restraint]
- Angle: [one paragraph from brag-plan.md]
- Hook: [first 2-3 seconds]
- Outro / punchline: [final line]
- Avoid:
  - Generic SaaS language
  - Abstract filler visuals
  - Unrelated visual redesign

## Visual Identity
- Background: [exact value from project]
- Text: [exact value from project]
- Accent: [exact value from project]
- Display font: [font or fallback decision]
- Body font: [font or fallback decision]
- Visual references from the project: [short list]

## Storyboard
Use the storyboard in `<output-dir>/brag-plan.md` as the creative contract.

Scene summary:
1. [Scene name] — [duration]s — [what must be seen / read]
2. [Scene name] — [duration]s — [what must be seen / read]
3. [...]

## Audio
- Audio role: [warm bed / sparse professional accents / cinematic support / dense rhythmic layer / intentional silence]
- Audio arc: [how sound changes across the video]
- Music: [filename, or none only if disabled, missing, or intentionally silent]
- Music treatment: [volume posture, fade-in/out intent, beat/swell notes; e.g. fade under final logo]
- Music cue guidance: [cue source — bundled preset path, or "detect at composition via analyze_music_cues.py / hyperframes beats" — plus concise optional timing hints; or unavailable]
- Audio-reactive treatment: [none / subtle / expressive; what visual qualities may respond to RMS/frequency energy]
- Audio-coupled moments:
  - [scene/moment] — [typing / beat reveal / counter / card sequence / simulated interaction / final logo]
  - [scene/moment] — [intent]
- SFX selection guidance: [how sound should match motion and interaction; examples only, not rigid rules]
- SFX analysis guidance: [path to sfx-analysis.md/json if present; use lower high-frequency-risk sounds for repeated or polished moments]
- Exact SFX choice: Hyperframes should choose filenames, timestamps, density, and volume based on the implemented animation.
- Audio files: copy the chosen music and any Hyperframes-selected SFX into `<output-dir>/composition/assets/`

## Hyperframes Instructions
Load the composition-building Hyperframes skills — `hyperframes` (composition contract + `data-*` timing, `references/format.md`; motion, eases and seek-safe keyframes in `references/motion.md`; look in `references/look.md`), `hyperframes-registry` (ready-made effects, transitions, titles), `media-use` (music, SFX, audio-reactive data), and `hyperframes-cli` (lint/check/render). /brag is its own workflow: skip the `hyperframes` storyline step: don't read `references/types/*` or `references/story.md`, don't propose storylines, and don't write a `SPEC.md`. The brag plan and composition brief replace them, including the LOOK line `references/look.md` asks for. Also skip its `usage`, `history`, `feedback` and REVIEW.md steps; `check` is brag's gate. Do not route into its generic launch-video workflow. Prefer native Hyperframes conventions over anything in `/brag`.

Requirements:
- Show at least one real UI, copy, or visual element from the source project.
- Keep all text readable in the final render.
- Keep the video within 15-25 seconds.
- Include the planned music/SFX layer unless audio was explicitly disabled or documented as intentionally silent.
- Treat `/brag` audio notes as guidance, not a fixed cue sheet. Choose SFX after the visual animation exists.
- Treat music cue metadata as optional timing hints. Hyperframes decides exact animation timing and should ignore cues that hurt readability, scene pacing, or the product story.
- Major reveals may move toward nearby strong cues within about 0.15s. Smaller entrances may align to nearby beat points within about 0.10s. Use only 1-3 strong cue locks in a 15-25s video unless the edit clearly benefits from more.
- Use SFX to support motion and interaction: card sounds for card-like reveals, short announcement cues for major payoffs, key/click sounds for text or user actions, and restraint when the edit is already busy.
- Honor planned music treatment such as fade-outs, ducking, beat-aligned reveals, or letting a final SFX ring over the music, using the best Hyperframes-supported implementation.
- When music is present and the treatment is not `none`, consider Hyperframes audio-reactive workflow: extract audio data and use RMS/frequency bands for subtle, brand-specific motion. Good targets are glow, depth, background warmth, card presence, title emphasis, or other existing visual elements. Avoid waveform/equalizer visuals, musical-note graphics, generic particle systems, strobing, or heavy pulsing.
- Use local assets for audio and any required runtime/media dependencies when possible.
- Run `hyperframes check` before render — it is brag's single gate.
- Keep creation and rendering local. Remote or publishing workflows require a separate explicit user request.
```

简报就是边界：属于产品定位、文案、tone、素材或时刻挑选的细节，由 `/brag` 指定；属于合成实现的细节，由 Hyperframes 决定。

---

## 音频素材准备

先读 [audio.md](audio.md)。构建合成前，把选定的音乐复制进 `<output-dir>/composition/assets/music/`。

```bash
mkdir -p <output-dir>/composition/assets/music
cp <skill-dir>/assets/music/<track>.mp3 <output-dir>/composition/assets/music/
```

`<skill-dir>` 是本 skill 自己的目录（见 `SKILL.md` 的 "Skill directory" 一节）。

Hyperframes 选定具体文件后，会把它挑中的 SFX 复制进同一个 `assets/` 目录树。

---

## 配音（仅当用户明确要求时）

配音默认关闭，除非用户明确要求，例如传 `--voice` 或说"给这个配解说"。正常的 `/brag` 运行中不要主动提供或开启解说。

配音关闭时，不写解说稿、不生成旁白、不转写音频、不压低音乐、不加人声轨、不把解说并进视频。正常导出的视频必须完全不依赖人声。

配音开启时，把解说句写进 `brag-plan.md` 的 `## Voiceover script` 小节，然后用 Kokoro 生成音频：

```bash
npx hyperframes tts "<narration text or path to script>" \
  --voice af_heart \
  --output <output-dir>/composition/assets/voiceover.wav
```

用户想要别的 Kokoro 音色，就跑 `npx hyperframes tts --list` 查看可选项。默认用上面的命令生成解说。

把它接到合成里独占一轨。解说期间音乐闪避到 0.12–0.15，结束后回到正常水平：

```html
<audio id="vo" data-start="0" data-track-index="3" data-volume="1" src="assets/voiceover.wav"></audio>
```

无论解说开不开，15-25 秒的窗口不变。解说稿要按这个窗口来写。窗口内各场景时长可以随生成的音频伸缩，而不是提前定死：生成后检查 WAV 时长，相应调整 `data-duration` 值。渲染出的解说超出窗口，就删减文稿重新生成；不要把视频拉过 25 秒去迁就它。

---

## 音频响应式提取（有音乐时）

有音乐且处理方式不是 `none` 时，合成可以对逐帧音频数据做出反应。**把提取工作交给 Hyperframes 的音频响应式流程**：`/brag` 不附带提取脚本，也不得硬编码脚本路径。

在合成环节，音频响应式处理遵循 `media-use` skill 自己维护的指引（`audio/references/captions/motion.md`；让该 skill 自己定位文件）。那份文件是为字幕写的：把它的构建期音频调制模式用在品牌元素上（光晕、halo、卡片存在感），不要用在字幕组上。数据格式、提取脚本（`audio/scripts/extract-audio-data.py`，随那个 skill 发布而非 `/brag`，所以要通过该 skill 自己的目录解析）和逐帧采样模式都归它管。让 Hyperframes 提取音频数据，并把至少一个视觉元素接到数据上。

提取不可用（没有脚本，或缺 ffmpeg）时，在简报里记一笔并跳过音频响应式，不要卡住渲染。

---

## 节拍同步（有 cue 来源时）

先拿到 cue 来源（见 `audio.md` 的 "Beat and cue sources"）：随附预设、对任意曲目跑 `analyze_music_cues.py`（需要 Python；经 `uv` 运行），或 `npx hyperframes beats`（无需 Python；需要 Hyperframes ≥ 0.6.99）。丰富来源（预设 / `analyze_music_cues.py`）给两个数组；`hyperframes beats` 给一个。

- **`strongCues`**：高强度节拍（重拍、渐强、重音）。用于**大时刻**：场景转场、主角揭晓、匹配包袱落地、logo 落定。每支视频锁 1–3 个。用 `hyperframes beats`（没有 `strongCues`）时，改取 `strength` 最高的节拍。
- **`beats`**：完整节拍网格。用来**把小的顺序事件吸附到音乐脉搏**上：卡片一张张到达、数据弹出、按序触发的 SFX。

### 如何实现

**大时刻（强 cue）：**
1. 加载 cue 来源：预设/分析 JSON（`strongCues` + `beats`），或 `hyperframes beats` 写出的节拍网格 JSON（纯节拍列表；位置见当前 hyperframes-cli skill）。
2. 在计划中的大视觉时刻附近挑 1–3 个强时间戳：`strongCues`，或 `strength` 最高的节拍。
3. 把揭晓的开始时间挪到 cue ±0.15 秒以内。
4. 做标记：`// beat-locked: 5.80s`

**顺序事件（节拍）：**
1. 确定顺序条目有几个（如 3 个数据、4 张资料卡）。
2. 为第一个条目找到距预期开始时间最近的节拍。
3. 后续每个条目用其后连续的节拍：各自吸附到某个节拍时间戳 ±0.10 秒以内。
4. 做标记：`// beat-grid: stat 1 at 12.65s, stat 2 at 13.17s, stat 3 at 13.70s`

**可读文本与节拍网格：**如果顺序条目是需要观众阅读的文本（数据标签、列表行、提示框），而节拍又很密（快节奏下间隔不足约 0.6 秒），不要每一拍都翻出新行，那样会超过阅读速度（bicycles 的规格行就是这么被赶坏的）。改为隔拍吸附，或快速全部显现后整组留在屏幕上。非文本点缀（光晕、圆点、刻度）仍可逐拍触发。阅读时长下限见 `step-2-plan.md`。

这给你两层音乐性：大时刻落在最强的重音上，小事件随脉搏跳动。

不要强行把每个补间都对到节拍上：可读性和场景节奏优先。补间吸附到节拍会伤害文案易读性或产品故事时，就用自然时序。

SFX 开启时，同时把 `<skill-dir>/assets/sfx/sfx-analysis.md` 作为选音参考传入。反复出现或精致的段落优先用高频风险低的文件。顺序事件上的 SFX 应与视觉同一时间戳触发：声音和动效同时落地。

---

## 调用 Hyperframes

`<output-dir>/brag-plan.md`、`<output-dir>/composition-brief.md` 和选定的音频素材就绪后：

1. 加载 Hyperframes skills（`hyperframes`、`hyperframes-registry`、`media-use`、`hyperframes-cli`）来创建或更新 `<output-dir>/composition/`。/brag 是自己独立的流程：跳过 `hyperframes` 的 storyline 步骤，不读 `references/types/*` 或 `references/story.md`，不提 storyline 方案，也不写 `SPEC.md`。brag 计划和合成简报取代它们，包括 `references/look.md` 要求的 LOOK 行。同时跳过它的 `usage`、`history`、`feedback` 与 REVIEW.md 步骤；`check` 是 brag 的门槛。不要汇入它通用的 launch-video 流程。
2. 把合成简报、brag 计划和它需要参考的源文件交给 Hyperframes。
3. 实现细节交给 Hyperframes 决定。
4. 跑 Hyperframes check（渲染前唯一的门槛）。
5. 渲染输出到 `<output-dir>/brag.mp4`。
6. 创作与渲染保持本地。远程或发布流程需要用户另行明确要求。

不要把这个 skill 里过时的合成片段手动复制进输出。委托的意义就在于吃到最新的 Hyperframes 指引。

---

## 自查清单

进入交付之前，逐项确认：

- [ ] `<output-dir>/composition-brief.md` 已存在。
- [ ] 简报明确指出了要展示的确切产品时刻。
- [ ] 合成用的是当前 Hyperframes 流程，而不是硬编码的 `/brag` 模板。
- [ ] 音乐文件已复制进 `<output-dir>/composition/assets/music/`。
- [ ] 至少一个视觉元素轻微响应音乐（有音频响应式处理），或已记录提取失败。
- [ ] 至少 1 个主要补间锁定到强 cue（某个 `strongCue`，或 `hyperframes beats` 中 `strength` 最高的节拍）±0.15 秒以内，并标了 `// beat-locked`（或为可读性选择了自然时序）。
- [ ] 顺序事件（卡片、数据、列表项）吸附到连续的 `beats[]` 时间戳（±0.10 秒），并标了 `// beat-grid`（或为可读性选择了自然时序）。
- [ ] 合成展示了项目中至少一个真实的 UI、文案或视觉元素。
- [ ] 屏幕上的每个事实性陈述都有项目依据（见下）。
- [ ] 总时长 15-25 秒。
- [ ] Hyperframes check 通过，或已为用户记录所有阻碍项。

### 事实性陈述的依据

`hyperframes check` 只审结构。它不管文案，所以一个场景可以写 "Ships 10x faster"，项目里没人写过这句话，检查照样干净通过。带着这个问题通读一遍合成内容，因为没有别的地方会问它。

分界线在于视频*断言了什么*，以及它*怎么表达*。

**必须有依据。**名称、数字、能力、功能主张、引语，一切以产品自己的口吻呈现的内容。一句话讲了产品的某个事实，这个事实就必须出现在项目里：它的文件、README、UI、真实输出。改大小写、删减、拆到多个元素上都行；凭空编造不行。"Streamline your workflow" 不合格，不是因为它笼统，而是因为项目从未做过这个主张。

**可以自由发挥。**tone、框架、笑点、钩子、转场、串联解说。"Here's the part nobody asked for" 是编的，而且受欢迎：这是手艺，它不断言任何产品事实。

想要的句子没有依据时，修法通常是引用项目本来就说的话，那几乎总比编出来的版本更怪、也更好。
