> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/gamedev/input-systems/references/buffering-and-accessibility.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 缓冲调优、设备、触屏与无障碍

内容：缓冲窗口；设备检测与按键提示；触屏控制；无障碍清单；游戏循环中的位置。

## 缓冲窗口

缓冲会记住一次稍早于合法时机到来的离散按键（收招硬直期间的攻击、落地期间的闪避、
过渡期间的菜单确认），并在允许触发的第一时间执行它。

- 典型窗口为 100-200 ms。格斗游戏的连招衔接通常更紧，且每个招式固定不变；
  菜单确认可以更长。
- 窗口用游戏时间的秒数表示，不用帧数，这样帧率变化、暂停和顿帧（hit-stop）都不会
  影响它。
- 触发即消费，保证一次按键对应一个动作；在死亡、场景切换和过场动画时清空缓冲。
- 窗口太长手感发糊，还会误触发动作；太短则显得没有响应。把窗口暴露为常量，便于
  根据试玩报告调整。
- 跳跃缓冲和土狼时间（coyote time）是同一思路用在跳跃控制器上；`platformer` 负责
  它们及其数值。

## 设备检测与按键提示

- 跟踪**最近使用的设备**：事件到来时，记录它来自键鼠、手柄（以及哪个家族）还是
  触屏，并据此切换图标和教学文本。
- 把按键映射到**位置**（South、East、West、North），再按家族挑选图标集。SDL3 就是
  这样命名按键的（`SDL_GAMEPAD_BUTTON_SOUTH` 及同类，配合 `SDL_GetGamepadButtonLabel`
  与 `SDL_GetGamepadType` 获取印刷标签和家族）；Godot 4.7 也是如此，其桌面端和 iOS
  的手柄驱动就是 SDL3：`JOY_BUTTON_A` 是下方按键，即 Xbox 的 A、PlayStation 的
  Cross、任天堂的 B。通过 `Input.get_joy_name()` 和 `Input.get_joy_info()`（厂商与
  产品 ID）读取家族。在 Android 和 Web 上 `get_joy_info()` 为空，此时回退到
  `get_joy_name()`。
- **Steam Input** 可能位于手柄和游戏之间。当某控制器对它开启时，游戏看到的是模拟
  出来的 Xbox 风格手柄，因此按名称和 ID 检查会把 PlayStation 或 Switch 手柄报告成
  Xbox。向 Steam 查询真实类型（`ISteamInput::GetControllerForGamepadIndex` 加上
  `GetInputTypeForHandle`；Godot 在 `get_joy_info()` 中以 `steam_input_index` 暴露
  该索引），或直接获取 Steam 自带的图标素材（`GetGlyphPNGForActionOrigin` /
  `GetGlyphSVGForActionOrigin`）。
- 支持**热插拔**：玩家可能开局用键盘，中途换用手柄。设备变化时无需重启即可重新
  解析按键提示。

## 触屏控制

- 屏上控件按拇指尺寸设计（虚拟摇杆和按钮）或改用手势，经由与物理输入相同的 action
  进行路由。
- 虚拟摇杆采用浮动原点（锚定在拇指落下的位置），并使用与物理摇杆相同的径向死区。
- 避免要求精确配合的多点触控组合键；使用较大的点击区域和宽松的判定时机。请玩家
  在最小和最大的目标屏幕上测试，并报告漏按和误按情况。

## 无障碍清单

- 每个设备的每个 action 都支持完整重映射，包含冲突处理和恢复默认。
- 默认为按住的操作（瞄准、蹲下、冲刺）提供切换/按住两种模式。
- 关键操作不要求同时按下多个输入；提供单键或依次按下的替代方案。
- 摇杆灵敏度和死区可调，另可选配瞄准辅助。
- 判定时间窗口在可行范围内可调（更长的缓冲、更慢的快速反应事件），并用长按选项
  替代连续狂按按键。
- 相机和移动的 X/Y 轴反向各自独立。
- 不人为添加输入延迟；离散按键在到达的那一帧或 tick 上处理。

## 游戏循环中的位置

- 在物理步进中读取按住状态和轴状态，使移动与模拟保持一致（见 `physics-tuning`）。
- 离散按键用事件捕获，或在消费它们的那个步进中做 just-pressed 检查，这样物理 tick
  之间的按键不会丢失。Godot 的 `is_action_just_pressed` 对很快又被松开的按键仍返回
  true，因此快速点按不会被丢弃。
- 启动时、在第一个游戏帧之前加载已保存的按键绑定。
