> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/disciplines/game-feel/references/feedback-recipes.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 反馈配方

目录：
1. trauma（创伤值）模型与调参范围
2. 缓动速查表，外加一个无需 tween 包的 Unity 缓动 pop 实现
3. 其余反馈手段清单（闪光、击退、数字弹出、粒子、顿帧）
4. 无障碍开关
5. 各引擎绑定速览

代码片段面向 Godot 4.7 与 Unity 6.3 LTS。

## 1. trauma 模型（为什么抖动手感好）

全程只跟踪一个 `trauma` 值，范围 `[0, 1]`。事件**累加** trauma；它每帧**线性衰减**。
实际抖动量取 `trauma^2`（或 `trauma^3`），因此：

- 小而频繁的事件几乎不会推动屏幕（trauma 低，平方后 → 极小），
- 大事件打击感十足（trauma 高，平方后 → 接近满幅），
- 抖动**总会自行结束**，因为 trauma 会衰减到 0。

偏移与旋转按 `max_* * shake * noise(t)` 计算。随时间采样噪声函数或叠加正弦波；绝不要
每帧取一个新的 `rand()`，那只会产生生硬的高频乱抖，而不是真正的抖动。

```gdscript
# 1D value-noise-ish sampler without an addon: layered sines at incommensurate rates.
func _shake_axis(seed: float, t: float) -> float:
    return 0.6 * sin(t * 11.0 + seed) + 0.4 * sin(t * 23.0 + seed * 2.0)
```

可调起始参数：`max_offset = (8..16, 6..10) px`、`max_roll = 0.05..0.12 rad`、
`decay = 1.0..1.5`（trauma/秒）、单次事件 trauma `0.15`（轻）→ `0.8`（重）。

## 2. 缓动速查表（什么活配什么曲线）

| 目标 | 缓动 | Godot `Tween` | 备注 |
|------|------|---------------|-------|
| UI/元素“pop”登场 | 过冲（overshoot） | `TRANS_BACK`, `EASE_OUT` | 冲过目标，再回稳 |
| 弹跳感的落地 | 弹跳/弹性 | `TRANS_ELASTIC`/`TRANS_BOUNCE`, `EASE_OUT` | 少用；观感偏卡通 |
| 收势 / 减速 | 缓出 | `TRANS_CUBIC`/`TRANS_QUAD`, `EASE_OUT` | “归于静止”的默认选择 |
| 预备 / 蓄力 | 缓入 | `TRANS_CUBIC`, `EASE_IN` | 快动作之前的慢起手 |
| 两端都平滑的 A→B | 缓入缓出 | `TRANS_SINE`, `EASE_IN_OUT` | 相机移动、菜单滑动 |

Unity 6.3 LTS 没有内置 tween 库；按偏好排序的选项：`Vector3.SmoothDamp`（弹簧式跟随）、
协程里的 `Mathf.SmoothStep` 或手写缓动、Animator 曲线，或项目已在用的第三方 tween 包。
无论工具怎么选，*曲线选择*保持一致。

```csharp
// Unity 6.3 LTS: an eased scale "pop" in a coroutine (no external deps).
static float EaseOutBack(float k) {                     // 0 -> 1, peaks ~10% past 1
    const float c1 = 1.70158f, c3 = c1 + 1f;
    float m = k - 1f;
    return 1f + c3 * m * m * m + c1 * m * m;
}

IEnumerator Pop(Transform t, float dur = 0.18f) {
    var squash = new Vector3(1.3f, 0.7f, 1f);            // squash on the event
    for (float e = 0f; e < dur; e += Time.deltaTime) {
        // Unclamped, so the overshoot past Vector3.one survives the lerp.
        t.localScale = Vector3.LerpUnclamped(squash, Vector3.one, EaseOutBack(e / dur));
        yield return null;
    }
    t.localScale = Vector3.one;
}
```

## 3. 其余反馈手段清单

- **闪光（Flash）：** 受击时把 sprite/材质染成白色 1–3 帧（`modulate`/材质颜色），再 tween 回原色。成本低，辨识度极高。
- **击退（Knockback）：** 沿受击法线方向施加一个向外的冲量，短促且有上限；稳定性交给 `physics-tuning` 负责。配合短暂的操作封锁，不要长时间封锁。
- **数字/文字弹出（Number/text pop）：** 生成一个伤害数字，上升、淡出、缓出收尾；随机化水平漂移，让连续命中的数字呈扇形散开。
- **粒子（Particles）：** 在接触点来一小簇短促爆发（火花、尘土、碎屑）。用对象池管理（`performance-optimization`），不要每次命中都实例化再释放。
- **顿帧（Freeze frame）：** 即正文中的 hit-stop；时长按重要性缩放（轻 0.04 秒 → 重 0.15 秒）。可选只冻结攻击者+受击者，而不是整个世界。
- **预备与跟随（Anticipation & follow-through）：** 大动作前加一点蓄力、动作后加一段收势，就能读出重量感；这是动画，不是代码（引擎动画 skill）。
- **色差/晕影/变焦冲击（Chromatic/vignette/zoom punch）：** 大场面用的后处理轻推；保持短促。

## 4. 无障碍（发布上线时带上这些开关）

- **减弱屏幕抖动**（用 0–100% 的设置缩放 trauma 输出，默认约 60–80%）。
- **减弱/关闭闪光**（光敏性）：把白闪替换为静态染色。即便开启闪光，任一秒内的大面积
  闪光也要控制在三次以内（[WCAG 2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html)
  一般闪烁阈值；[Xbox Accessibility Guideline 118](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/118)，
  Photosensitivity）。
- **减弱相机运动**：削减抖动 roll 与变焦冲击。

这些与 `game-ui-ux`（设置菜单）和 `input-systems`（无障碍章节）搭配使用。

## 5. 各引擎绑定速览

- **Godot 4.7：** `create_tween()` + `tween_property().set_trans().set_ease()`；`GPUParticles2D/3D`
  一次性发射（one-shot）；`Engine.time_scale` + `ignore_time_scale` 计时器；抖动作用于 `Camera2D.offset`。
- **Unity 6.3 LTS：** 协程 + `SmoothDamp`/曲线（或某个 tween 包）；`ParticleSystem.Play()`；
  `Time.timeScale` + `WaitForSecondsRealtime`；抖动用 `CinemachineBasicMultiChannelPerlin`
  的 amplitude/frequency，由 `trauma^2` 驱动；一次性打击则用 `CinemachineImpulseSource.GenerateImpulse()`
  （见 `camera-systems`）。
- **Web（Phaser/Pixi/three）：** tween 用引擎/库自带的 tween；Phaser 里用 `this.cameras.main.shake()`；
  其他引擎用 `requestAnimationFrame` 驱动的缓动。
