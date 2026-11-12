---
name: input-systems
description: >
  引擎无关的输入架构，附 Godot InputMap 代码：具名动作、摇杆死区、按键缓冲以及带冲突检查的
  重绑定。适用于手柄支持、重绑定菜单、摇杆漂移、AZERTY 上的 WASD，或按键丢失。不适用于
  coyote time（`platformer`）或 Unity 与 Unreal 的输入资产（`unity-input-system`、
  `unreal-enhanced-input`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/disciplines/input-systems/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 输入系统

玩法代码读取具名的**动作**（`jump`、`attack`、`move`）；从按键、按钮和触摸到这些动作的绑定只是数据。重绑定、多设备支持以及大部分输入无障碍能力，都源自这一层间接。本 Skill 讲引擎无关的架构，附 Godot 4.7 代码。引擎自带的输入资产请用 `unity-input-system` 或 `unreal-enhanced-input`；Godot 的 `InputMap` 在这里讲。

## 适用场景

- 设计输入层：动作、按设备区分的绑定、设备检测与提示。
- 摇杆处理：死区、响应曲线、灵敏度。
- 缓冲离散按键（收招期间攻击、闪避、连招衔接、菜单确认）。
- 带冲突处理、绑定保存和恢复默认值的重绑定界面。
- 无障碍控制：完整重映射、切换与按住、不强制组合键、可调的时间窗口。

**不适用本 Skill：** coyote time、跳跃缓冲和可变跳跃高度归 `platformer`，跳跃控制器由它负责。与缓冲交互的 hit-stop 及其他手感反馈属于 `game-feel`。绑定文件的写入归 `save-systems`。菜单焦点与导航规则归 `game-ui-ux`。

## 核心工作流

1. **动手前先盘点。** 列出现有动作（Godot：`[input]` 段，位于 `project.godot`；Unity：`.inputactions` 文件；Unreal：`IA_`/`IMC_` 资产），并在玩法代码里 grep 原始按键读取（`is_key_pressed`、`KEY_`、`Input.GetKey`）。原始读取是最先要替换的。
2. **按意图命名动作**，不按按键命名，并为每个动作给一套键盘和手柄绑定。触摸也走同一批动作。
3. **让读取方式匹配动作。** 离散动作用边沿（本帧或本 tick 按下），连续动作用按住或轴。
4. **用径向死区和独立的响应曲线过滤模拟输入。**
5. **缓冲离散按键**：在动作可用前一点点到达的按键，用游戏时间计量，在触发时消费。
6. **重绑定：** 捕获下一次输入，绑定物理按键，拒绝或交换冲突，保存，并提供恢复默认值。保留一条无法被解绑的返回暂停菜单的路径。
7. **先自行检查，再请用户做设备测试**（见下文 "检查"）。

## 模式

### 1. 动作优先于原始按键；边沿与按住


```gdscript
if Input.is_action_just_pressed("jump"):      # edge: true on the press frame or tick only
    try_jump()
var dir := Input.get_vector("move_left", "move_right", "move_up", "move_down")
# get_vector applies a radial deadzone, rescales past it and caps length at 1,
# so diagonals are not faster. Use get_axis for a single axis.
# WRONG: Input.is_key_pressed(KEY_SPACE): unrebindable, keyboard-only, and a held
# check, so jump re-fires every frame.
```


各引擎对应物：Unity Input System 的 `InputAction` 与 action maps；Unreal Enhanced Input 的 Actions 加 Mapping Contexts。

### 2. 模拟死区与灵敏度


```gdscript
# Raw sticks never rest at exactly zero. Apply a RADIAL deadzone (on the vector
# length), not per-axis, so diagonals aren't clipped into the axes.
func apply_deadzone(stick: Vector2, dead := 0.2, curve := 1.0) -> Vector2:
    # dead == 1 cannot be rescaled; report invalid settings before stopping movement.
    if not (dead >= 0.0 and dead < 1.0 and curve > 0.0):
        push_error("apply_deadzone requires 0 <= dead < 1 and curve > 0.")
        return Vector2.ZERO
    var mag := stick.length()
    if mag <= dead:
        return Vector2.ZERO                      # inside deadzone -> no movement
    # Rescale so motion ramps from 0 at the edge of the deadzone, not from `dead`.
    var scaled := minf((mag - dead) / (1.0 - dead), 1.0)  # some pads report > 1 on diagonals
    return stick / mag * pow(scaled, curve)      # curve > 1 = finer aim near center
# WRONG: clamping each axis separately — it carves a square hole and snaps to axes.
```


把响应曲线（指数）与灵敏度（对结果施加的增益，通常是镜头转向速率）分开，并在设置里同时暴露两者。无效设置会报错并返回零位移。Godot 的 `get_vector` 已经做了死区和重缩放，使用四个动作死区的平均值（默认每个动作 0.2），除非你显式传入一个。

### 3. 离散按键的动作缓冲


```gdscript
# action_buffer.gd: remember discrete presses briefly so an early press still fires.
extends RefCounted

var window := 0.15                        # seconds; 0.1-0.2 suits attacks and dodges
var _pressed_at := {}                     # action -> game time of its latest press

func press(action: StringName, now: float) -> void:
    _pressed_at[action] = now

func consume(action: StringName, now: float) -> bool:
    if not _pressed_at.has(action) or now - _pressed_at[action] > window:
        return false
    _pressed_at.erase(action)             # one press fires one action
    return true

func clear() -> void:                     # on death, pause, cutscene, scene change
    _pressed_at.clear()
```


从输入读取处喂给它（`if Input.is_action_just_pressed("attack"): buffer.press(&"attack",
clock)`），并在动作变为可用的地方调用 `consume`，例如攻击收招后的第一帧。`clock` 是你在 `_physics_process` 中推进的游戏时间，因此窗口在暂停和 hit-stop 期间会冻结。当两个缓冲动作在同一 tick 变为可用时，按固定优先级取舍，而不是按字典顺序。跳跃缓冲和 coyote time 用的是同一思路，但归 `platformer`。

### 4. 带冲突检测的重绑定


```gdscript
# Godot 4.7. Capture the next physical input, reject conflicts, then persist.
var _waiting_for: StringName = &""               # set by the "press a key for Jump" button

func _unhandled_input(event: InputEvent) -> void:
    if _waiting_for != &"" and _is_bindable(event):
        get_viewport().set_input_as_handled()
        if not rebind(_waiting_for, event):
            show_conflict_warning(event)         # offer swap or cancel
        _waiting_for = &""

func _is_bindable(e: InputEvent) -> bool:
    if e is InputEventKey or e is InputEventJoypadButton or e is InputEventMouseButton:
        return e.pressed and not e.is_echo()     # ignore releases and key repeat
    return e is InputEventJoypadMotion and absf(e.axis_value) > 0.5  # ignore stick noise

func rebind(action: StringName, captured: InputEvent) -> bool:
    var event := _to_binding(captured)
    for other in InputMap.get_actions():
        if other != action and not String(other).begins_with("ui_") \
                and InputMap.action_has_event(other, event):
            return false                         # already used -> let UI warn/swap
    for old in InputMap.action_get_events(action):
        if old.get_class() == event.get_class():  # replace only this device kind's binding
            InputMap.action_erase_event(action, old)
    InputMap.action_add_event(action, event)
    save_bindings()                              # persist (see save-systems)
    return true

func _to_binding(e: InputEvent) -> InputEvent:
    if e is InputEventKey:                       # bind the physical key, not the layout's letter
        var k := InputEventKey.new()
        k.physical_keycode = e.physical_keycode
        return k
    var b := e.duplicate() as InputEvent
    b.device = -1                                # all devices: a pad binding must not stick to pad 0
    if b is InputEventJoypadMotion:
        b.axis_value = signf(b.axis_value)       # keep the direction only
    return b
```


键盘绑定使用 `physical_keycode`，并把 `keycode` 留在 0，这让 Godot 按按键位置匹配，于是 WASD 在 AZERTY 或 Dvorak 上仍在原位。用 `DisplayServer.keyboard_get_label_from_physical` 显示玩家自己的标签。用 `InputMap.load_from_project_settings()` 恢复默认值。Unity：`PerformInteractiveRebinding()` 以及 `SaveBindingOverridesAsJson()`/`LoadBindingOverridesFromJson()`。Unreal：Enhanced Input User Settings 配 player-mappable keys。

### 5. 绑定审计（headless，有问题时以 1 退出）


```gdscript
# tools/audit_bindings.gd: godot --headless --path . --script res://tools/audit_bindings.gd
extends SceneTree

const KEYBOARD_ONLY := [&"toggle_console"]   # actions allowed to have no gamepad binding

func _initialize() -> void:
    var problems := PackedStringArray()
    var actions := InputMap.get_actions().filter(func(a): return not String(a).begins_with("ui_"))
    for i in actions.size():
        var action: StringName = actions[i]
        var events := InputMap.action_get_events(action)
        if not events.any(func(e): return e is InputEventKey or e is InputEventMouseButton):
            problems.append("%s: no keyboard or mouse binding" % action)
        if action not in KEYBOARD_ONLY and not events.any(
                func(e): return e is InputEventJoypadButton or e is InputEventJoypadMotion):
            problems.append("%s: no gamepad binding" % action)
        for other in actions.slice(i + 1):
            for e in events:
                for o in InputMap.action_get_events(other):
                    if e.is_match(o, true):       # exact: axis direction and modifiers count
                        problems.append("%s and %s share %s" % [action, other, e.as_text()])
    for p in problems:
        printerr("BINDING: ", p)
    print("Checked %d actions, %d problems" % [actions.size(), problems.size()])
    quit(1 if problems.size() > 0 else 0)
```


它读取项目的 `[input]` 段。精确匹配很关键：用默认的宽松匹配时，同一摇杆轴两个方向上的 `move_left` 和 `move_right` 会被算作冲突。两个从不同时激活的动作（一个菜单动作和一个玩法动作）可以共用一个键；把这类配对列出来，而不是删掉检查。

## 检查

1. 运行绑定审计，修好它打印出的每一行。在 Unity 或 Unreal 中，对 `.inputactions` JSON 或列出 mapping-context 的键做同样的审查。
2. 用固定输入对纯逻辑部分做 headless 单元测试：死区在 0、在死区边界以及在对角线上的输出；一次缓冲按键只触发一次，并在窗口过后过期。runner 和退出码参照 `godot-gdscript-headless-testing`。
3. 再次在玩法代码里 grep 原始按键读取；除调试工具外，数量应为零。
4. 请用户接上手柄，把一个动作重绑定到某个正面按钮，重启游戏，并报告新绑定是否仍生效、提示是否在键盘与手柄图标之间切换，以及第二只手柄能否使用重绑定后的按钮。你无法自己按按钮，所以不要报告未经确认的设备行为。

## 易踩的坑

- **混淆边沿与按住。** 对跳跃用按住检查会每帧重复触发；对移动用边沿检查会丢掉按住的输入。
- **逐轴死区**会削掉对角线，并把移动吸附到轴上。改用径向死区。
- **一次缓冲按键触发两次**，因为 `consume` 从不清空它；或者在重生后触发，因为没有谁调用 `clear()`。
- **缓冲在 hit-stop 或暂停期间过期**，说明它在计墙上时钟时间（`Time.get_ticks_msec`）。改用物理步里的游戏时间。
- **重绑定不做冲突处理**，会让两个动作共用一个键，或因解绑菜单而把玩家困住。要检测冲突，并保留一条不可解绑的返回路径。
- **WASD 在 AZERTY 或 QWERTZ 上位置错乱**：按按键字母存储的绑定会跟着布局走。存储物理位置并显示该布局的标签。
- **重绑定后的手柄按钮只对 player 1 有效**：捕获的事件保留了 pad 0 的设备 ID。除非刻意给手柄分配，否则为所有设备存储绑定（Godot `device = -1`）。
- **用 `==` 比较 InputEvents** 对两个不同对象恒为假。改用 `action_has_event` 或 `is_match`。
- **给手柄玩家显示 "Press Space"。** 追踪最后一次发送输入的设备，每次变化时切换图标，无需重启。
- **Steam Input 把每只手柄都报告成 Xbox**（当它对该控制器启用时），于是按名称和 ID 判断会选错图标。向 Steam 查询真实类型（细节见参考文档）。
- **只有按住的动作、强制组合键和固定灵敏度**会挡住部分玩家。提供切换与按住、单输入替代方案以及灵敏度设置。

## 参考

- `references/buffering-and-accessibility.md`：在调整缓冲窗口、按控制器系列选择按钮图标（SDL3 位置、Steam Input）、构建触摸控制，或审查控制的无障碍清单时阅读。

## 相关 Skill

- `platformer`：coyote time、跳跃缓冲、可变跳跃高度和跳跃手感。
- `unity-input-system`、`unreal-enhanced-input`：引擎输入资产和 API。
- `save-systems`：持久化绑定和输入设置。
- `game-ui-ux`：菜单焦点与导航；`camera-systems`：视角灵敏度与反转。

## 版本说明

最后验证：2026-11-11。

- Godot 4.7：`Input.is_action_just_pressed` 在按下的那一帧或物理 tick 为真；`InputEvent.is_match(event, exact_match = true)`；`get_joy_info()` 在 Windows、Linux、macOS 和 iOS 上填充 `raw_name`、`vendor_id` 和 `product_id`，仅在桌面端填充 `steam_input_index`（https://github.com/godotengine/godot/blob/4.7-stable/doc/classes/Input.xml）。
- 上文的绑定审计和动作缓冲在 Godot 4.7.2 headless 上运行过。
