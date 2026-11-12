---
name: camera-systems
description: >
  构建并调优游戏摄像机，不绑定具体引擎，提供 Godot 与 Cinemachine 3 的映射：带死区与前瞻的 2D 跟随、
  第三人称环绕、第一人称视角和分屏。适用于摄像机滞后、跟随时抖动、越出关卡边缘、穿墙或随帧率变化
  的情况。不适用于震屏（`game-feel`）或物理时间步抖动（`physics-tuning`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/disciplines/camera-systems/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 摄像机系统

优秀的摄像机在任何帧率下都能平滑跟随，让镜头走在动作之前，既不露出关卡之外的画面，也不穿墙。本 Skill 涵盖这些技术，并把它们对应到各引擎的摄像机节点或装置上；在自行手写之前，优先使用引擎内置的装置。

## 适用场景

- 2D 摄像机需要平滑跟随、忽略小幅移动、引导运动方向并保持在边界内。
- 3D 第三人称环绕或第一人称视角控制器，或对多个目标进行取景。
- 修复抖动、跳变、眩晕，或摄像机露出关卡边缘的问题。

**不适用场景：** 震屏幅度与触发器（`game-feel`；本 Skill 只提供偏移量），物理体本身的物理抖动（`physics-tuning`），`Camera3D` 与环境配置（`godot-3d-essentials`），玩家移动（`godot-2d-movement` 或对应引擎的移动 Skill），视角灵敏度输入曲线（`input-systems`）。

## 核心工作流

1. **明确摄像机服务的对象。** 平台跳跃（引导跳跃、看见危险）、俯视角（居中加死区）、第三人称（环绕加碰撞）、第一人称（仅视角）。
2. **优先使用内置装置**：Godot 的 `Camera2D` 平滑、边界与拖动边距，或 `SpringArm3D`；Unity 的 Cinemachine 3（`CinemachineCamera` 搭配 Position Composer、Orbital Follow、Deoccluder、Confiner）。只手写装置做不到的部分。
3. **用 `1 - exp(-rate * dt)` 做平滑**，或使用临界阻尼弹簧（`SmoothDamp`），绝不要每帧使用固定的 `lerp(a, b, 0.1)`。
4. **先加死区，再加前瞻**，并让前瞻缓动趋近目标值，避免方向翻转时镜头猛甩。
5. **限制视口而非中心点**，将其约束在关卡矩形内，并考虑缩放。
6. **3D 场景把视角与碰撞分开**：在一个枢轴上处理偏航与俯仰，用弹簧臂或射线把摄像机拉近，并限制俯仰。
7. **在目标移动之后再更新**（延迟更新，或在物理结算之后），启用物理插值时跟随目标的插值变换。
8. **先用可运行的检查验证，再用肉眼观察。** 以无头方式单步运行跟随代码，让目标以 300 px/s 移动 2 s，分别在 `dt = 1/30` 和 `dt = 1/144` 下运行，比较摄像机落后目标的距离。使用 `rate = 8` 的指数平滑时，滞后约为 33 px 和 37 px；固定的 `lerp(..., 0.1)` 约为 90 px 和 19 px，这说明跟随依赖帧率。然后请用户在低帧率和高帧率下跑向角落、墙壁与关卡边缘，报告是否出现抖动、露出边缘或跳变。

## 模式

### 1. Godot 2D 内置跟随：平滑 + 边界（不要一上来就手写）


```gdscript
# Godot 4.7 Camera2D. Engine-provided smoothing + hard limits + drag margins.
@onready var cam := $Camera2D
func _ready() -> void:
    cam.make_current()
    cam.position_smoothing_enabled = true
    cam.position_smoothing_speed = 6.0           # higher = snappier; lower = floatier
    cam.limit_left = 0; cam.limit_top = 0        # clamp to the level rect (pixels)
    cam.limit_right = level_width; cam.limit_bottom = level_height
    cam.drag_horizontal_enabled = true           # built-in deadzone via drag margins
```


### 2. 与帧率无关的平滑跟随（自行手写时）


```gdscript
# RIGHT: exponential smoothing — same feel at any FPS. `rate` ~ 5..12.
func _follow(dt: float) -> void:
    var t := 1.0 - exp(-rate * dt)               # converges correctly regardless of dt
    global_position = global_position.lerp(target.global_position, t)
# WRONG: global_position = global_position.lerp(target.global_position, 0.1)
#        → faster smoothing at higher FPS; different feel on every machine.
# Unity 6.3 LTS: Vector3.SmoothDamp(transform.position, target.position, ref vel, smoothTime) in
# LateUpdate gives the same spring behavior with built-in frame-rate correction.
```


### 3. 死区 + 前瞻（引导玩家，忽略抖动）


```gdscript
# Camera only chases once the target leaves the deadzone box, then aims AHEAD of motion.
func _camera_target(dt: float) -> Vector2:
    var to := target.global_position - _focus
    var dz := deadzone_half_extents                  # e.g. Vector2(48, 32)
    # Only move the focus by the overflow beyond the deadzone (per axis).
    _focus.x += clampf(absf(to.x) - dz.x, 0, INF) * signf(to.x)
    _focus.y += clampf(absf(to.y) - dz.y, 0, INF) * signf(to.y)
    var lead := target.velocity.normalized() * look_ahead_dist    # aim ahead of travel
    return _focus + lead
```


### 4. 带碰撞推近的 3D 第三人称环绕


```gdscript
# Godot 4.7. Yaw/pitch a pivot; a SpringArm3D auto-pulls the camera in when blocked.
func _unhandled_input(e):
    if e is InputEventMouseMotion and Input.mouse_mode == Input.MOUSE_MODE_CAPTURED:
        # screen_relative is unscaled; `relative` is scaled by the stretch settings, so
        # sensitivity would change with window size. The docs recommend screen_relative
        # for captured-mouse aiming.
        _yaw -= e.screen_relative.x * sensitivity
        _pitch = clampf(_pitch - e.screen_relative.y * sensitivity,
                        deg_to_rad(-80.0), deg_to_rad(45.0))       # clamp pitch!
func _process(_dt):
    pivot.rotation = Vector3(_pitch, _yaw, 0)
    # $SpringArm3D handles wall collision: set spring_length + collision_mask; the child
    # Camera3D slides in automatically. RIGHT: spring arm. WRONG: camera clips through walls.
# Unity 6.3 LTS: a Cinemachine 3 CinemachineCamera (namespace Unity.Cinemachine) with an Orbital
# Follow + Cinemachine Deoccluder; the CinemachineBrain on the Camera blends automatically.
```


### 5. 震屏 Hook（所属触发器位于 `game-feel`）


```gdscript
# Expose an additive offset the game-feel trauma model writes to; follow + shake compose.
var shake_offset := Vector2.ZERO                 # set each frame by game-feel (trauma^2 * noise)
func _apply(final_focus: Vector2) -> void:
    global_position = final_focus + shake_offset  # shake rides ON TOP of smooth follow
# Unity Cinemachine 3: CinemachineBasicMultiChannelPerlin (AmplitudeGain/FrequencyGain) for
# continuous noise driven by trauma; for one-off impacts, a CinemachineImpulseSource on the
# hitter plus a CinemachineImpulseListener on the camera.
```


## 常见陷阱

- **每帧使用 `lerp(pos, target, const)`** 依赖帧率：30 FPS 下更飘，144 FPS 下更跟手。请改用 `1 - exp(-rate * dt)` 或 `SmoothDamp`。
- **跟随物理体时的抖动**：物理体按物理步长（60 Hz）移动，摄像机按显示帧率移动。请开启物理插值（Godot 的 `physics/common/physics_interpolation`），在 `_process` 中跟随物理体的插值变换（3D 中用 `get_global_transform_interpolated()`），或者在物理步中以 `Camera2D.process_callback = CAMERA2D_PROCESS_PHYSICS` 跟随。两者混用正是抖动的根源。
- **一帧滞后**：在目标移动之前于常规更新里跟随就会产生。请在 `LateUpdate`（Unity）中跟随，或等移动与物理结算完成后再跟随。
- **把摄像机挂到移动中的玩家节点下** 会继承每一次颠簸，并与插值冲突。请把摄像机放在独立分支上（或设 `top_level = true`），通过代码或装置跟随。
- **钳制中心点而非视口** 会在边缘之外露出黑边。应钳制到 `[min + half_view, max - half_view]`，关卡在任一轴上小于视口时，则在该轴上居中。
- **快节奏游戏不加死区** 会让摄像机随每一次微小位移而抖动；矩形死区与圆形死区手感不同，要有意识地选择。
- **俯仰不设限** 会让摄像机越过头顶翻过去。环绕视角约为 -80° 到 +45°，第一人称约为 ±80°。
- **Godot 中鼠标视角灵敏度随窗口尺寸变化**：`InputEventMouseMotion.relative` 会受拉伸设置缩放；捕获鼠标瞄准时请读取 `screen_relative`。
- **3D 中穿墙**：使用弹簧臂或遮挡射线，探测半径略大于摄像机近平面的一半尺寸。
- **传送或重生后的弹射**：平滑摄像机会猛地扫过整个关卡。应硬切并重置平滑状态（Godot 的 `Camera2D.reset_smoothing()`），或刻意做快速缓动。
- **把震屏写进跟随目标** 会让跟随与震屏互相冲突。先做平滑跟随，最后再叠加震屏偏移。

## 参考资料

- `references/follow-and-framing.md`：阅读以了解平滑公式推导、完整的「死区 + 前瞻 + 边界」2D 装置、环绕与第一人称细节、群组取景与分屏、过场动画混合，以及 Godot/Cinemachine 3 组件映射表。

## 相关 Skill

- `game-feel`：震屏 trauma 与触发器；写入本 Skill 的偏移量。
- `godot-2d-movement`、`godot-3d-essentials`：摄像机所取景的玩家与世界。
- `physics-tuning`：所跟随物理体的时间步与插值。
- `input-systems`：视角灵敏度、反转与摇杆响应曲线。

## 版本说明

最后验证日期：2026-11-11。

- Godot 4.7：`Camera2D.position_smoothing_*`、`limit_*`、`drag_*`、`process_callback`、`reset_smoothing()`；`InputEventMouseMotion.screen_relative`；物理插值与手动摄像机插值参见 https://docs.godotengine.org/en/4.7/tutorials/physics/interpolation/advanced_physics_interpolation.html。
- Unity 6.3 LTS 搭配 Cinemachine 3.1（3.1.7 为最新版本，发布于 2026 年 6 月 9 日；命名空间 `Unity.Cinemachine`）。2.x 中的名称 `CinemachineVirtualCamera`、`CinemachineCollider` 与 `CinemachineFramingTransposer` 在 3.x 中已弃用（https://packages.unity.com/com.unity.cinemachine）。
- PhantomCamera（Godot 插件）最新版本 v0.11.0.4，2026 年 10 月（https://github.com/ramokz/phantom-camera/releases）。
