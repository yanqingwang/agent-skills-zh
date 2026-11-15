> **中文汉化版** · 上游：[latent-spaces/brag](https://github.com/latent-spaces/brag) · 原文件：`skills/brag/references/audio.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 音频参考

所有 SFX 均为 CC0（Kenney.nl，公有领域）。随附音乐为 Sascha Ende（ende.app）的 CC BY 4.0 作品；见 `assets/music/README.md`。默认应使用音乐和 SFX，除非用户传入 `--no-music`、`--no-sfx`，所需素材缺失，或者计划明确把静音选为最有力的创作手法。

倾向平滑、专业的成品：一段有品味的音乐底加少量掐准时机的 SFX，通常好过完全静音。

---

## 音频响应式视觉

有音乐时，除非 tone 要求静止或冷面克制，否则优先做轻微的音频响应式处理。这不是节拍检测。它的意思是：Hyperframes 可以预提取逐帧音频数据，用 RMS/频段能量来调制已有的视觉元素。

合适的用法：
- 主视觉光晕或天空色温随 RMS 轻微呼吸
- 产品卡片、手机或指标面板随低频获得轻微存在感
- 标题、引言或 logo 在音乐更强的段落泛起柔和的高频光晕
- 背景纵深、暗角或光效层随音乐底轻轻起伏

避免：
- 波形显示、均衡器柱条、音符图案或通用可视化图形
- 频闪、剧烈脉动或损害可读性的文字缩放
- 把音频响应当作良好场景时序的替代品
- 宣称精确的节拍/BPM 同步，除非真有节拍检测器

建议的计划写法：
```
Audio-reactive treatment: subtle; use music RMS/bass to make the hero glow and product card presence breathe. No waveform/equalizer visuals.
```

Hyperframes 实现说明：音频响应式处理遵循 `media-use` skill 自己维护的指引（`audio/references/captions/motion.md`；让该 skill 自己定位文件），用它提取逐帧音频数据，并在合成时间线内同步采样。那份文件是为字幕写的：把它的构建期音频调制模式用在品牌元素上（光晕、halo、卡片存在感），不要用在字幕组上。提取脚本（`audio/scripts/extract-audio-data.py`）随那个 skill 发布，`/brag` 不提供它，所以不要硬编码它的路径。

---

## 素材路径

下述路径都相对于 `<skill-dir>`，即本 skill 自己的目录（见 `SKILL.md` 的 "Skill directory" 一节）。它随安装方式而不同，请实际解析，不要假设是 `~/.claude/skills/brag/`。

SFX 位于 `<skill-dir>/assets/sfx/{casino,impact,interface,ui}/` 下，单独按键音集位于 `<skill-dir>/assets/sfx/keyboard/`。

音乐位于 `<skill-dir>/assets/music/`。

随附音乐的 cue 预设与音乐放在一起：

```text
<skill-dir>/assets/music/cues/<track-stem>.music-cues.md
<skill-dir>/assets/music/cues/<track-stem>.music-cues.json
```

SFX 分析文件与 SFX 库放在一起：

```text
<skill-dir>/assets/sfx/sfx-analysis.md
<skill-dir>/assets/sfx/sfx-analysis.json
```

**关键：渲染前先把音频文件复制进合成项目。** Hyperframes 从合成目录校验并提供素材。务必先把需要的文件复制进 `<output-dir>/composition/assets/`：

```bash
# Create local asset dirs
mkdir -p <output-dir>/composition/assets/sfx/interface <output-dir>/composition/assets/sfx/impact <output-dir>/composition/assets/sfx/casino <output-dir>/composition/assets/sfx/ui
mkdir -p <output-dir>/composition/assets/music

# Copy only the files you plan to use (not the entire library)
cp <skill-dir>/assets/sfx/interface/bong_001.ogg <output-dir>/composition/assets/sfx/interface/
cp <skill-dir>/assets/sfx/impact/impactBell_heavy_000.ogg <output-dir>/composition/assets/sfx/impact/
cp <skill-dir>/assets/music/happy-beats-business-moves-vol-1-by-ende-dot-app.mp3 <output-dir>/composition/assets/music/
```

然后在合成 HTML 里，路径**相对于 `composition/` 目录**：
```
assets/sfx/interface/bong_001.ogg
assets/sfx/impact/impactBell_heavy_000.ogg
assets/music/happy-beats-business-moves-vol-1-by-ende-dot-app.mp3
```

绝对不要用绝对路径（以 `/Users/...` 开头），它们在渲染器里会静默失败。

---

## SFX 库：已批准的文件

家族类 SFX（casino、impact、interface、ui）直接放在 `sfx/` 下；单独按键音集放在 `sfx/keyboard/`。

选文件前先读 `sfx-analysis.md`：它按用例列出更稳妥的选择，并标出高频风险高的文件。精致、反复出现的段落优先用低/中 HF 风险文件；高风险文件留给极小的孤立点缀或 chaotic tone。

### `keyboard/`：单独按键音

32 个 CC0 单键按压 WAV 文件（`keypress-001.wav` 到 `keypress-032.wav`）。每个都是不同的按键声，力度和音色略有差异。用于逐字符打字动画：在整个集合里随机抽取，避免重复字符听起来机械。

**来源：** [Keyboard Soundpack #1](https://opengameart.org/content/keyboard-soundpack-1-typing-and-single-keystrokes)，作者 unicae_games，CC0

### `interface/`：UI 音效

| 文件 | 特点 | 用途 |
|---|---|---|
| `click_001–005.ogg` | 清脆、精准 | 按钮点击、CTA、任何点击动作 |
| `glitch_002.ogg`, `glitch_004.ogg` | 数字失真 | 科技/AI 时刻、混乱点缀 |
| `error_005–006.ogg` | 否定的嗡鸣 | 喜剧式失败、答错 |
| `switch_001–002.ogg`, `switch_004–007.ogg` | 拨动开关 | 功能开启、二元状态 |
| `drop_001–003.ogg` | 柔和落下 | 元素落位、轻柔放置 |
| `bong_001.ogg` | 低沉钟声 | 戏剧性宣告，慎用 |
| `select_008.ogg` | 选中咔哒 | 导航、条目聚焦 |

### `impact/`：撞击音效

更具物理感和电影感。非常适合大时刻和转场。

| 文件 | 特点 | 用途 |
|---|---|---|
| `impactSoft_medium_000–004.ogg` | 中等闷响 | 重大揭晓、硬转场，最安全的家族 |
| `impactSoft_heavy_000–004.ogg` | 沉重闷响 | 喜剧闷击、重量感、搞笑时刻 |
| `impactBell_heavy_000.ogg`, `_003.ogg`, `_004.ogg` | 深沉共鸣钟声 | 电影式揭晓、logo 砸落、戏剧性时刻 |
| `impactPunch_heavy_000–004.ogg` | 重拳 | 攻击性节拍、chaotic tone |
| `impactPunch_medium_000–004.ogg` | 中等重击 | 强调冲击 |
| `impactWood_light_000–004.ogg` | 轻木敲击 | 温暖、有机的轻叩 |
| `impactWood_medium_000–004.ogg` | 木敲击 | 更暖的点缀 |
| `impactWood_heavy_000–004.ogg` | 重木击 | 电影感重量 |
| `impactPlank_medium_000–004.ogg` | 木板拍击 | 滑稽的物理时刻 |
| `impactPlate_heavy_000–004.ogg` | 金属板砸 | 大冲击、有攻击性 |
| `impactPlate_light_000–004.ogg` | 轻金属板 | 通知、清脆点缀 |
| `impactPlate_medium_000–004.ogg` | 中等金属板 | 中等分量点缀 |
| `impactTin_medium_000–004.ogg` | 铁皮罐敲击 | 怪趣、lo-fi 时刻 |
| `impactGeneric_light_000–004.ogg` | 通用轻击 | 万能的小点缀 |
| `impactMetal_medium_000–004.ogg` | 金属轻叩 | 中等点缀 |
| `impactMetal_heavy_000.ogg`, `_002.ogg`, `_004.ogg` | 沉重金属铿锵 | 攻击性打击 |
| `impactMetal_light_002–003.ogg` | 轻金属叮声 | 小通知 |
| `impactGlass_light_001–003.ogg` | 轻玻璃碰响 | 闪光、精巧的成就 |
| `impactGlass_medium_000.ogg`, `_002.ogg`, `_004.ogg` | 玻璃轻叩 | 中等分量点缀 |
| `impactGlass_heavy_002.ogg` | 玻璃碎裂 | 混乱打击 |
| `impactMining_001.ogg` | 采矿敲击 | 工业感、沉重 |
| `footstep_wood_000.ogg`, `_001.ogg`, `_002.ogg`, `_004.ogg` | 轻木脚步声 | 轻点、步进或滚动点缀 |

其余 `footstep_*` 文件（wood `_003`、concrete、grass、snow、carpet）未获批准。

### `casino/`：纸牌与筹码音效

用途具体，但非常适合滑动/发牌/堆叠时刻。

| 文件 | 特点 | 用途 |
|---|---|---|
| `card-slide-1–8.ogg` | 纸牌滑动 | 滑动动作、内容滑入 |
| `card-place-1–4.ogg` | 纸牌放置 | 条目落位、卡片出现 |
| `card-fan-1–2.ogg` | 展牌 | 多个条目依次出现 |
| `card-shove-1–4.ogg` | 纸牌推挤 | 用力的纸牌运动 |
| `card-shuffle.ogg` | 洗牌 | 带运动的转场 |
| `chip-lay-1–3.ogg` | 筹码放下 | 指标落位/确认 |
| `chips-stack-1–6.ogg` | 筹码堆叠 | 计数递增、堆叠动画 |
| `chips-collide-1–4.ogg` | 筹码碰响 | 庆祝、有分量的成功 |
| `chips-handle-1–4.ogg`, `chips-handle-6.ogg` | 筹码拨弄 | 随意的筹码移动 |
| `dice-shake-1–3.ogg` | 摇骰子 | 铺垫、悬念 |
| `dice-grab-1–2.ogg` | 抓骰子 | 拿起、快速动作 |
| `dice-throw-1–3.ogg` | 掷骰子 | 混乱/随机时刻 |
| `die-throw-1–4.ogg` | 单颗骰子掷出 | 更轻的随机点缀 |
| `cards-pack-open-1–2.ogg` | 拆包 | 揭晓、产品发布时刻 |

### `ui/`：点击与开关

| 文件 | 特点 | 用途 |
|---|---|---|
| `click1–5.ogg` | 多种点击音色 | 按钮点击，比 interface 点击更干净 |
| `mouseclick1.ogg` | 鼠标点击 | 模拟光标交互 |
| `rollover1–2.ogg`, `rollover4–5.ogg` | 悬停/划过 | 轻微悬停反馈、极柔的点缀 |
| `switch1–38.ogg`（大多数变体） | 开关变体 | 切换、模式改变，按音色挑选 |

---

## Tone 与 SFX 能量

| Tone | 能量 | 做法 |
|---|---|---|
| `default` | 适中 | 关键节点放 3-5 个 SFX。元素弹入用 `interface/click` 或 `interface/drop_*`，成功用 `impactBell_heavy_000`，揭晓用 `impactSoft_medium`。 |
| `polished` | 少而有 | 2-3 个非常轻微的 SFX。柔和点缀用 `interface/bong_001`。轻柔揭晓用 `interface/drop_001`。不要任何有攻击性的。 |
| `yc-parody` | 稀疏但有 | 2-3 个克制的提示。一次干脆的揭晓打击（`impactSoft_medium`）、一个 UI/纸牌点缀，合适时再来一个 logo 收尾音。 |
| `chaotic` | 密集 | 每个节拍都有 SFX，有时叠着来。混用 `impact/impactPunch_heavy`、`interface/glitch_002`、`casino/dice-throw`、`impact/impactMetal_heavy`。 |
| `deadpan` | 极稀疏 | 偏好一段安静的音乐底加 1-2 个干脆的提示。只有计划明确说静音本身就是笑点时才全静音。 |
| `cinematic` | 2-3 个大的 | `impactBell_heavy_000` 或 `_004` 用于高光时刻。`impactSoft_medium` 用于揭晓。`impactBell_heavy_003` 用于收尾。 |
| `app-store` | 稳定的轻量层 | 每张功能卡片配 `interface/drop_*` 或 `interface/click_*`。片尾用 `impactBell_heavy_000`。全部 0.65-0.75 音量。 |

---

## 时刻与声音的对应启发

把这些当作用法示例交给 Hyperframes，而不是固定配方。声音要为剪辑服务，而不是抢戏。

| 时刻类型 | 合适的声音家族 | 说明 |
|---|---|---|
| 卡片/条目依次开场 | `casino/card-slide-*`, `casino/card-place-*`, `casino/card-fan-*`, `interface/drop_*` | 贴合手势。卡片堆用纸牌音；柔和的产品网格可用落下音。密集序列只给第一个、最后一个或节奏上重要的条目加音。 |
| 大揭晓/包袱落地 | `impact/impactBell_heavy_000`, `_003`, 或 `_004`, `impact/impactSoft_medium_*`, `interface/bong_001` | 揭晓落地时来一记简短的宣告式提示。保持简短。 |
| 文字弹出/打字文案 | `keyboard/keypress-*.wav`（随机抽取）, `interface/drop_*` | 逐字符打字动画时，每个字符从 `keyboard/` 里随机选一个文件。柔和的标签弹入用 `drop_001` 或 `drop_002`。文案密集时减少或跳过。 |
| 模拟用户操作 | `interface/click_*`, `interface/select_008`, `interface/switch_*`, `ui/mouseclick1`, `ui/switch*` | 视频里出现光标、点击、按钮、开关、滑动或选择时用交互音。与可见动作匹配。 |
| 成功/完成 | `impact/impactBell_heavy_000`, `_003`, 或 `_004`, `casino/chips-collide-*` | 审批、匹配成功、指标、走完的流程或最终 CTA 用正面点缀。 |
| 混乱或喜剧节拍 | `interface/glitch_002`, `interface/glitch_004`, `interface/error_005–006`, `impact/impactPunch_heavy_*`, `casino/dice-throw-*` | 更响或更怪的提示留给能驾驭它们的 tone。 |

拿不准时，宁可少几个提示、把时机掐准。整支视频用统一的声音色调，好过一堆可爱的杂音。

---

## 时序规则

这些规则适用于 Hyperframes 实现合成、动效时序已知的情形：

- SFX 对齐动画的**起点**，不是终点
- 入场弹出：元素首个可见帧前 0.0–0.1 秒
- 转场：在转场开始时刻
- 成功叮声：指标/数据完全可见的那一刻
- 错峰出现的元素：通常只给第一个、最后一个或最强的一拍加音；只有这种节奏是有意设计且依然干净时，才给每一项都配音

合成写法：
```
Scene 2 — Reveal — 3s
  "Horse Tinder" scales in at 0.3s  →  SFX: impact/impactSoft_medium_001 at 0.2s
  Tagline fades up at 0.8s          →  (no SFX, let the reveal carry)
  Transition at 3.0s                →  SFX: interface/drop_001 at 2.9s
```

---

## 音乐

### 可用曲目

所有曲目都是 ende.app 的 "Happy Beats / Business Moves"。明快、干净、偏企业风。适用于多种 tone。

| 文件名 | 时长 | 特点 | 适合 |
|---|---|---|---|
| `happy-beats-business-moves-vol-1-by-ende-dot-app.mp3` | 2:44 | 完整明快曲目，能量最高 | `default`, `app-store` |
| `happy-beats-business-moves-vol-9-by-ende-dot-app.mp3` | 1:54 | 中等能量，稍放松 | `default`, `yc-parody` |
| `happy-beats-business-moves-vol-10-by-ende-dot-app.mp3` | 1:00 | 紧凑循环，短促有力 | `default`, `chaotic` |
| `happy-beats-business-moves-vol-11-by-ende-dot-app.mp3` | 1:28 | 温暖、商务感 | `yc-parody`, `app-store` |
| `happy-beats-business-moves-vol-12-by-ende-dot-app.mp3` | 1:58 | 稳定干净 | `polished`, `cinematic` |

`deadpan` tone：优先用 vol-12，音量压得很低（0.12-0.18）。只有计划明确选择静音时才不用音乐。

### 在合成中的用法

复制文件后（见上文"素材路径"），从 `composition/` 用相对路径引用：

```html
<audio id="bg-music" data-start="0" data-duration="[total]" data-track-index="10" data-volume="0.35" src="assets/music/happy-beats-business-moves-vol-1-by-ende-dot-app.mp3"></audio>
```

音量：常规音乐底 0.3-0.4。deadpan 或极度克制的戏仿用 0.12-0.22。绝不超过 0.5。SFX 用 0.55-0.85，polished/deadpan 取更低的值。

音乐文件不存在就跳过它，渲染完再告知用户。

### 节拍与 cue 来源

节拍同步需要 cue 来源。有三种可用，用环境支持的最丰富的那种。节拍同步现在对**任意**曲目都可用，不限随附曲目。两种任意曲目方法（2 和 3）的依赖互不重叠：方法 2 需要 Python，方法 3 需要较新的 Hyperframes，所以一种不可用时另一种通常能顶上。

1. **随附曲目 → 预计算预设（最丰富、即时、无依赖）。** 随附曲目自带 cue 元数据。读对应的 markdown 摘要，并在 `composition-brief.md` 里传入 JSON 路径：

```text
<skill-dir>/assets/music/cues/<track-stem>.music-cues.md
<skill-dir>/assets/music/cues/<track-stem>.music-cues.json
```

2. **任意曲目 → 扩展分析（对自定义曲目最丰富；需要 Python，任意 Hyperframes 版本）。** 自定义曲目（或刷新随附曲目）就对音频文件跑 `analyze_music_cues.py`。它对任意曲目产出同样丰富的 cue JSON/Markdown。经 `uv` 运行，它会按 `<skill-dir>/scripts/pyproject.toml` 自动备好依赖（`librosa`、`numpy`、`scipy`、`soundfile`），无需手动 `pip install`：

```bash
uv run --project <skill-dir>/scripts \
  python <skill-dir>/scripts/analyze_music_cues.py <track>.mp3 \
  --output-json <output-dir>/composition/assets/music/cues/<stem>.music-cues.json \
  --output-md  <output-dir>/composition/assets/music/cues/<stem>.music-cues.md
```

这是 `hyperframes beats`（方法 3）不可用时的后备，例如锁定了旧版 Hyperframes 时。`uv` 和 Python 依赖都不可用时，改用方法 3。

3. **任意曲目 → `hyperframes beats`（简单、无需 Python；需要 Hyperframes ≥ 0.6.99）。** 音乐接入合成后运行：

```bash
npx hyperframes beats <output-dir>/composition
```

它会写出一个按曲目的节拍文件：带逐拍时序和归一化 `strength`（0-1）的节拍网格，但没有单独的 `strongCues` 数组，所以"强"拍要自己取 `strength` 最高的那些。（确切输出路径见当前 hyperframes-cli 的 `beats` 指南。）`beats` 是 Hyperframes 0.6.99 加入的；锁定的旧版安装上没有它，退回方法 2（脚本），或用下方的 `unavailable` 写法。

预设与 `analyze_music_cues.py` 共用同一套丰富 schema：

- `duration`、`tempo`
- `beats`：节拍网格点，含 `time` 与归一化的 `intensity`
- `strongCues`：价值最高的落点时刻，含 `time`、`intensity` 和 `kind`（`strong_beat` / `onset_peak`）
- `scoring`：特征与归一化元数据

`hyperframes beats` 是更简单的下限：一个纯节拍网格，逐拍带 strength，没有 strong-cue 数组。

规划规则（适用于你手上的任何来源）：

- 用 cue 元数据为时序提供倾向，而不是控制时序。
- 大揭晓可以向强 cue 靠拢，幅度约 `±0.15s`。
- 较小的入场可对齐附近的节拍点，幅度约 `±0.10s`。
- 15-25 秒的视频用 1-3 个强 cue 锁定。
- cue 损害文案可读性、场景节奏或产品故事时，忽略它。
- deadpan 或高度克制的 tone，cue 应稀少、安静，或留给最后的 logo。

Cue/节拍元数据不能替代 Hyperframes 的音频响应式视觉：它帮助节拍/起伏的时序；音频响应式数据让细微的视觉属性随音乐呼吸。

没有任何来源可用（无预设、无 Python 依赖、也没跑 `hyperframes beats`）时，写下：

```text
Music cue guidance: unavailable; continue without beat/cue sync.
```

### 添加 SFX 元素

音乐底放低轨，每个叠加的 SFX 各占一个递增的 track-index（如音乐在 10，SFX 从 11 往上）。重叠的音频绝不共用 track-index。

```html
<audio id="sfx-1" data-start="0.2" data-duration="1" data-track-index="11" data-volume="0.80" src="assets/sfx/interface/drop_001.ogg"></audio>
```

每个 `<audio>` 片段按当前 hyperframes 的 Data Attributes + Video/Audio 契约接线（`data-track-index`、`data-volume`、`data-start`、`data-duration`）。`/brag` 只拥有上述音量策略和轨道分配约定；片段 schema 归 Hyperframes。
