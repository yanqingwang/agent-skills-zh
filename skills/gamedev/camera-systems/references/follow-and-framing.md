> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/disciplines/camera-systems/references/follow-and-framing.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 跟随与构图

目录：
1. 为什么用 `1 - exp(-rate*dt)`（帧率无关平滑）
2. 完整 2D 装置：死区、前瞻、边界
3. 3D 第三人称环绕
4. 第一人称视角
5. 多目标与群体构图、分屏
6. 电影化混合与转场
7. 各引擎装置对照（Godot 4.7、Cinemachine 3）

代码片段针对 Godot 4.7 与 Unity 6.3 LTS（含 Cinemachine 3）。

## 1. 为什么用 `1 - exp(-rate*dt)`（帧率无关平滑）

朴素的 `pos = lerp(pos, target, k)` 是*每帧*应用一次 `k`，144 FPS 下每秒的平滑量远大于 30 FPS，手感随硬件而变。指数平滑把速率按*每秒*固定：

```text
t = 1 - exp(-rate * dt)      # rate ≈ 5 (floaty) .. 12 (snappy)
pos = lerp(pos, target, t)   # identical convergence at any frame rate
```

临界阻尼弹簧（Unity 的 `Vector3.SmoothDamp`，或用 `smoothTime` 手写的弹簧）同样帧率无关，还带速度连续性（不会过冲）。优先用引擎内置的弹簧/平滑，别急着手写。

## 2. 完整 2D 装置：死区 + 前瞻 + 边界

目标移动后，每帧的处理顺序：

1. 计算目标超出**死区**（矩形或圆形）的部分 → 焦点只移动这个超出量。
2. 加**前瞻**：`focus += dir_of_motion * lookAheadDist`，但要让**前瞻偏移本身**朝目标值缓动，这样方向反转时视图不会猛跳。
3. 把相机**平滑**地移向焦点（第 1 节）。
4. **钳制**，让*可见矩形*留在边界内：每个轴把相机中心钳到 `[min + halfView, max - halfView]`（钳制的是视野，不是中心）。

```gdscript
# Godot 4.7: clamp the VIEW, accounting for zoom and viewport size.
func _clamp_to_level(center: Vector2) -> Vector2:
    var half := get_viewport_rect().size * 0.5 / zoom
    return Vector2(
        clampf(center.x, level_rect.position.x + half.x, level_rect.end.x - half.x),
        clampf(center.y, level_rect.position.y + half.y, level_rect.end.y - half.y))
# If the level is smaller than the view on an axis, center on that axis instead of clamping.
```

可调参数：死区 `32–64 px`；前瞻 `40–120 px`，用 `0.2–0.4 s` 缓动；平滑 `rate 6–10`。

## 3. 3D 第三人称环绕

- **装置（rig）：** 在角色肩部/头部高度放一个不可见的枢轴（pivot）；偏航（yaw）放在枢轴上，俯仰（pitch）放在子节点上；相机位于本地 Z 轴的 `-springLength` 处。
- **碰撞：** 弹簧臂（Godot 的 `SpringArm3D`）或遮挡射线，从枢轴投向期望的相机位置，并缩短到第一个命中点，相机就永远不会穿墙。
- **俯仰限制：** 约 `[-80°, +45°]`，这样相机既不会翻转，也不会钻进地板。
- **灵敏度与反转：** 暴露视角灵敏度和反转 Y 轴选项（见 `input-systems`）。
- **Cinemachine 3（Unity 6.3 LTS）：** 一个 `CinemachineCamera`（命名空间 `Unity.Cinemachine`），挂 **Orbital Follow** 组件和 **Cinemachine Deoccluder**（碰撞处理）；`Camera` 上的 `CinemachineBrain` 负责在相机之间做混合。这组名字取代了 v2 的 `CinemachineVirtualCamera` / `CinemachineCollider`。

## 4. 第一人称视角

- 偏航旋转身体（这样移动方向与视角一致）；俯仰只旋转相机头节点。
- 限制俯仰角；绝不让滚转（roll）累积。
- 鼠标：捕获光标（`Input.mouse_mode = Input.MOUSE_MODE_CAPTURED`），读取 `InputEventMouseMotion.screen_relative`，该值不受拉伸（stretch）设置缩放。
- 摇杆：应用响应曲线 + 死区（见 `input-systems`），转向速率按帧率缩放。

## 5. 多目标 / 群体构图

- 计算所有目标的包围盒；把相机放在包围盒中心。
- **2D：** 设置缩放，让包围盒（含留白）适配视口；钳制缩放的上下限。
- **3D：** 把相机后移（dolly）/ 调整 FOV 来容纳包围盒。Cinemachine 3 中，把相机的 Tracking Target 指向 `CinemachineTargetGroup`，再加 `CinemachineGroupFraming`。
- **分屏：** 每个玩家一台相机，各自渲染到一个视口矩形；把额外渲染开销计入预算（`performance-optimization`）。

## 6. 电影化混合与转场

- 在玩法相机与过场相机之间做短时混合（缓入缓出）。改变活跃相机的优先级时 Cinemachine 会自动混合；Godot 中则在标记（marker）变换之间对装置做补间，或带淡入淡出地切换 `current` 相机。
- 硬切/传送时重置平滑状态，避免相机横穿整张地图。

## 7. 各引擎装置对照

Unity 列对应 Cinemachine 3.x，命名空间 `Unity.Cinemachine`。v2 组件（`CinemachineVirtualCamera`、`CinemachineCollider`、`CinemachineFramingTransposer`）在 3.x 中已标记弃用，弃用提示指向 `CinemachineCamera`、`CinemachineDeoccluder` 与 `CinemachinePositionComposer`；新代码不要再用它们。`CinemachineDeoccluder` 让目标保持在视线内；`CinemachineDecollider` 只把相机从与之相交的几何体中拉出来。

| 需求 | Godot 4.7 | Unity 6.3 LTS |
|------|-----------|---------|
| 2D 跟随 + 平滑 + 限制 | `Camera2D`（`position_smoothing_*`、`limit_*`、`drag_*`） | `CinemachineCamera` + `CinemachinePositionComposer`（Damping、Dead Zone、Lookahead）+ `CinemachineConfiner2D` |
| 3D 跟随/环绕 | 枢轴 + `SpringArm3D` + `Camera3D` | `CinemachineCamera` + `CinemachineOrbitalFollow` + `CinemachineDeoccluder`（或 `CinemachineDecollider`） |
| 抖动 | 来自 `game-feel` 的叠加式 `offset` | `CinemachineBasicMultiChannelPerlin`（噪声）；`CinemachineImpulseSource` + `CinemachineImpulseListener`（冲击） |
| 边界 | `limit_*` / 手动钳制 | `CinemachineConfiner2D/3D` |
| 群体构图 | 手动包围盒 + 缩放 | `CinemachineTargetGroup` + `CinemachineGroupFraming` |
| 插件选项 | `PhantomCamera`（声明式 2D/3D 装置） | 内置 Cinemachine |
