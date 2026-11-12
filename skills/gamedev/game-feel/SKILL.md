---
name: game-feel
description: >
  为已能正常运行的机制添加与引擎无关的打击感（juice）：基于 trauma 的屏幕震动、命中停顿（hit-stop）、
  缓动补间、挤压与拉伸，以及击退。当游戏手感平淡、轻飘或缺乏冲击力，或希望命中与跳跃更有满足感时使用。
  不适用于郊狼时间（`platformer`）、输入缓冲（`input-systems`）、镜头跟随（`camera-systems`）
  或 HUD 布局（`game-ui-ux`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/disciplines/game-feel/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 游戏手感（juice / 打击感）

反馈让动作更有说服力：在同一事件上同时触发若干个短促、夸张的小反馈。本 Skill 在已能正常运行的机制之上叠加这一层效果，从不改动模拟逻辑，因此震动只移动镜头、命中停顿只缩放时间，两者都不会移动实体，也不会让玩法逻辑停滞。

## 何时使用

- 命中、跳跃、落地、冲刺、拾取、死亡或按键已经能正常工作，但手感偏弱。
- 添加或调整震动、命中停顿、缓动、挤压与拉伸、闪白、击退、数字弹出。
- 判断打击感叠加到什么程度才算合适，并加入减弱震动与减弱闪光的选项。

**本 Skill 不适用：** 跳跃控制器的数学计算（`platformer`）、通用输入缓冲与按键重绑定（`input-systems`）、镜头跟随、死区与前瞻（`camera-systems`，它暴露了本 Skill 所写入的偏移量）、混音与闪避（`audio-design`）、着色器溶解效果（`shader-programming`）、补间与粒子节点 API（`godot-animation`、`unity-animation`）。

## 工作流

1. **找到事件钩子。** 打击感附着在离散事件上（`hit`、`landed`、`picked_up`、`died`）。如果机制不发出任何事件，先添加信号或 C# 事件；绝不要用轮询去获取它们。
2. **为每个事件指定一个档位**（见下表），然后通过一次 `feedback(tier, pos)` 调用触发该档位的整套反馈，使整个游戏保持比例协调。
3. **每个事件先从 2-3 个通道开始**（声音、粒子、震动），试玩后逐步增加通道，直到事件能被清晰感知。命中停顿和震动的效果最强，也最容易被滥用；把它们留给撞击类事件。
4. **给一切会动的元素加缓动。** 弹出用带回弹的过冲（`back`），回稳用缓出（ease-out），只有预备动作用缓入（ease-in）。
5. **决定命中停顿期间哪些逻辑继续运行。** 时间缩放会减慢计时器、补间以及 `_process`/`Update` 的 delta。震动衰减和 UI 补间通常应使用真实时间；被冻结的姿态则不应如此。
6. **发布上线无障碍开关**：震动强度 0-100 %、减弱闪光、减弱镜头运动。
7. **先用无头检查验证，再用肉眼确认。** 相隔 30 ms 触发事件两次，并断言：在较长的一次停顿结束后时间缩放回到 1.0、trauma 在 `1 / decay` 秒内归零、每个 scale 补间恰好停在其静止值。然后请用户试玩，并反馈命中是否清晰可感、是否有令人眩晕之处，以及冻结期间输入是否仍能被记录。

## 档位

| 档位 | 震动量（Trauma） | 命中停顿 | 粒子 | 额外效果 | 示例事件 |
|------|:------:|:--------:|:---------:|-------|----------------|
| small（小） | 0.10-0.20 | 无 | 0-4 | 短促音效 | 脚步、金币、UI 悬停 |
| medium（中） | 0.30-0.50 | 0.04-0.06 s | 6-12 | 闪光 | 普通命中、落地、拾取 |
| large（大） | 0.70-1.00 | 0.10-0.15 s | 20-40 | 闪光、缩放、数字弹出 | 暴击、Boss 命中、死亡、爆炸 |

## 模式

### 1. 基于衰减 Trauma 的屏幕震动

```gdscript
# Godot 4.7 Camera2D script. Shake = trauma^2, so light hits barely move and heavy hits punch.
# Writes the camera OFFSET (visual only). Uses real time so the shake keeps decaying during
# hit-stop instead of freezing the camera off-centre.
# Camera2D.ignore_rotation defaults to true; set it false or the roll does nothing.
extends Camera2D
@export var decay := 1.2          # trauma lost per real second
@export var max_offset := Vector2(12, 8)
@export var max_roll := 0.1       # radians
@export var strength := 1.0       # player setting, 0..1
var trauma := 0.0
var _t := 0.0

func add_trauma(amount: float) -> void:
    trauma = clampf(trauma + amount, 0.0, 1.0)   # hits add; they don't reset

func _process(dt: float) -> void:
    if trauma <= 0.0:
        return
    var real_dt := dt / maxf(Engine.time_scale, 0.0001)
    trauma = maxf(trauma - decay * real_dt, 0.0)
    var shake := trauma * trauma * strength
    _t += real_dt * 30.0
    # Summed sines at unrelated rates: smooth, never a per-frame random buzz.
    offset = Vector2(max_offset.x * shake * sin(_t * 1.7), max_offset.y * shake * sin(_t * 2.3))
    rotation = max_roll * shake * sin(_t * 1.1)
    if trauma == 0.0:
        offset = Vector2.ZERO
        rotation = 0.0
```

在 Unity 中：用 `trauma * trauma` 驱动 `CinemachineBasicMultiChannelPerlin` 的 `AmplitudeGain`/`FrequencyGain`，并通过 `Time.unscaledDeltaTime` 衰减；对于一次性命中，在攻击者上挂 `CinemachineImpulseSource`，在相机上挂 `CinemachineImpulseListener`。

### 2. 可承受重叠命中的命中停顿

```gdscript
# Godot 4.7. Slow time, restore after a REAL-TIME delay; only the newest call restores.
var _hit_stop_id := 0

func hit_stop(duration := 0.08, slow := 0.05) -> void:
    _hit_stop_id += 1
    var my_id := _hit_stop_id
    Engine.time_scale = slow
    # 4th arg ignore_time_scale=true: the timer still fires while the game is slowed.
    await get_tree().create_timer(duration, true, false, true).timeout
    if my_id == _hit_stop_id:       # a newer hit-stop owns the restore
        Engine.time_scale = 1.0
```

```csharp
// Unity. WaitForSecondsRealtime ignores Time.timeScale; WaitForSeconds never finishes at 0.
int _hitStopId;
IEnumerator HitStop(float duration = 0.08f, float slow = 0.05f) {
    int myId = ++_hitStopId;
    Time.timeScale = slow;
    yield return new WaitForSecondsRealtime(duration);
    if (myId == _hitStopId) Time.timeScale = 1f;
}
```

### 3. 挤压、拉伸与过冲

```gdscript
# Godot 4.7. Keep area roughly constant: stretch one axis, squash the other, spring back.
func pop(node: Node2D) -> void:
    node.scale = Vector2(1.3, 0.7)
    var tw := node.create_tween()
    tw.tween_property(node, "scale", Vector2.ONE, 0.18) \
      .set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)   # overshoots past 1, settles
```

当事件可能重复触发时，要终止或复用同一属性上的旧补间（`if _tw: _tw.kill()`），否则两个补间会相互冲突，节点最终停在错误的 scale 上。

## 注意事项

- **震动实体而非相机**会让碰撞与瞄准失步。应震动相机偏移量或仅用于视觉的轴心节点。
- **每帧随机偏移**会像静电噪声一样嗡嗡作响。应使用噪声，或在衰减的 trauma 值之下叠加多个正弦波。
- **命中停顿永不结束**：Unity 的 `WaitForSeconds`，或未设置 `ignore_time_scale` 的 Godot 计时器，在时间缩放为 0 时不推进，在 0.05 时也几乎不动。应按真实时间等待。
- **重叠的命中停顿**（相隔 30 ms 的两次命中）会让第一个计时器在第二次冻结期间恢复时间。只允许最新的一次调用负责恢复。
- **命中停顿期间震动冻结在偏离中心的位置**，原因是它按缩放后的 delta 衰减。应按真实时间衰减（Godot 用 `dt / Engine.time_scale`，Unity 用 `Time.unscaledDeltaTime`）。
- **命中停顿期间 UI 与菜单补间慢如爬行。** Godot 用 `Tween.set_ignore_time_scale(true)`；Unity 用带 `Time.unscaledDeltaTime` 的协程。
- **时间缩放不会减慢音频**（Godot 与 Unity 皆然），所以长时间冻结会让撞击音效盖在静止画面上播放。要么让停顿保持短促，要么同时调低 `AudioServer.playback_speed_scale`。
- **对按住不放或多段攻击的每一帧都加命中停顿**会锁死游戏。每次撞击只加一次，并对处于生效停顿期间的命中跳过处理。
- **打击感效果永远回不到静止状态**（scale 漂移、震动不衰减）会让它不再被读作反馈。每个效果结束时都要对齐到静止值。
- **对常规动作过度叠加打击感**会引起眩晕，并掩盖真正的撞击。脚步只配 small 档，或者干脆不加。
- **反馈阻塞输入。** 长时间冻结与不可取消的动画会让人感觉卡顿；把冻结控制在约 0.15 s 以内，并在冻结期间对输入做缓冲。
- **闪光超过光敏阈值。** 大面积高亮闪光每秒须保持在三次及以下（WCAG 2.3.1），并应提供减弱闪光选项，用色调替代它们。

## 参考资料

- `references/feedback-recipes.md`：当你需要缓动速查表、不依赖补间包在 Unity 中实现缓动弹出、闪光、击退、数字弹出与粒子配方，或各引擎的绑定汇总（Godot、Unity、Phaser）时阅读。

## 相关 Skill

- `camera-systems`：负责跟随与构图；本 Skill 只写入震动偏移量。
- `godot-animation`、`unity-animation`：补间、`AnimationPlayer` 与粒子 API。
- `audio-design`：每套反馈组合中的声音层。
- `physics-tuning`：击退力度与稳定的时间步长。
- `platformer`：打击感所依附的跳跃手感控制。

## 版本说明

最后验证时间：2026-11-11。

- Godot 4.7：`SceneTree.create_timer(time_sec, process_always, process_in_physics, ignore_time_scale)`、`Tween.set_ignore_time_scale()`、`Camera2D.ignore_rotation`（默认 `true`）；`Engine.time_scale` 会缩放 `_process`/`_physics_process` 的 delta、`Timer` 与 `SceneTreeTimer`，但不影响音频（https://docs.godotengine.org/en/4.7/classes/class_engine.html）。
- Unity 6.3 LTS 搭配 Cinemachine 3.1（3.1.7 为 2026 年 6 月的最新发行版）：`CinemachineBasicMultiChannelPerlin`、`CinemachineImpulseSource`、`CinemachineImpulseListener`（https://packages.unity.com/com.unity.cinemachine）。
- WCAG 2.2 成功标准 2.3.1，三次或低于阈值的闪光（https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html）。
- 基于 Trauma 的震动源自 Squirrel Eiserloh 在 GDC 2016 的演讲 "Math for Game Programmers: Juicing Your Cameras With Math"。
