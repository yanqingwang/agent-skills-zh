> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/godot/godot-signals-groups/references/signal-patterns.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 信号与分组模式参考（Godot 4.7）

`godot-signals-groups` 的深度配套参考。

目录：连接标志 · bind 与 unbind · 带类型参数的自定义信号 ·
带超时等待信号 · 安全断开连接 · 分组 API · 信号与直接调用 ·
全局事件总线（autoload）

## 连接标志

`Object.connect` / `Signal.connect` 接受一个标志位掩码：

- `CONNECT_ONE_SHOT`：首次发出后自动断开连接。
- `CONNECT_DEFERRED`：在空闲时间（帧末）调用回调，而不是立即调用。回调要在物理处理期间修改场景树时很有用。
- `CONNECT_PERSIST`：连接随场景一起保存（编辑器中建立的连接）。
- `CONNECT_REFERENCE_COUNTED`：多个相同的连接按引用计数，需要断开相同次数才能全部解除。

```gdscript
sig.connect(cb, CONNECT_ONE_SHOT | CONNECT_DEFERRED)
```

## bind 与 unbind

- `cb.bind(a, b)`：调用时把 `a, b` 追加到参数列表末尾。
- `cb.unbind(n)`：丢弃末尾 `n` 个信号参数。回调要忽略信号负载时很好用：`sig.connect(_refresh.unbind(sig_arg_count))`。

## 带类型参数的自定义信号

```gdscript
signal stat_changed(stat_name: String, old_value: int, new_value: int)

var stats: Dictionary[String, int] = {}

func set_stat(stat: String, value: int) -> void:
    var old: int = stats.get(stat, 0)   # get() returns Variant, so type the variable
    stats[stat] = value
    stat_changed.emit(stat, old, value)
```

类型参数起文档作用，还能让编辑器的连接对话框显示参数名。`emit()` 不会对照声明检查实参；如果已连接的处理函数被以错误的参数数量调用，不匹配会以报错形式暴露出来。

## 带超时等待信号

`await` 没有内置超时。让信号与计时器赛跑：让两者无论谁先完成都发出同一个辅助信号，然后 await 它：

```gdscript
signal _race_finished(signal_won: bool)

## Returns true if `sig` fired within `seconds`, false on timeout.
func await_signal_or_timeout(sig: Signal, seconds: float) -> bool:
    var on_signal := func(..._args: Array) -> void: _race_finished.emit(true)
    var on_timeout := func() -> void: _race_finished.emit(false)
    var timer := get_tree().create_timer(seconds)
    sig.connect(on_signal, CONNECT_ONE_SHOT)
    timer.timeout.connect(on_timeout, CONNECT_ONE_SHOT)
    var won: bool = await _race_finished
    if sig.is_connected(on_signal):          # the loser is still connected
        sig.disconnect(on_signal)
    if timer.timeout.is_connected(on_timeout):
        timer.timeout.disconnect(on_timeout)
    return won

# Usage: if not await await_signal_or_timeout($Door.opened, 2.0): print("door stuck")
```

`..._args` 剩余参数（Godot 4.5+）让一个辅助函数能接受任意参数数量的信号。每个节点一次只跑一个竞争；两个重叠的调用会共用 `_race_finished`。

大多数玩法场景下，直接 await `animation_finished`、`timeout` 或 `tween_finished` 更简洁。

## 安全断开连接

```gdscript
if sig.is_connected(cb):
    sig.disconnect(cb)
```

发出者或持有 Callable 的对象被释放时，连接会自动移除。**lambda** 由创建它的脚本所在对象持有，而不是由它捕获的节点持有：如果被捕获的节点被释放，lambda 仍保持连接，下次信号发出时会报错（"Lambda capture at index 0 was freed"）。每个 `func():` 表达式也都是新的 Callable，因此 `is_connected()` 无法识别重复，每次重新连接都会多叠一层调用。把 lambda 存进变量以便之后断开连接，或者改为连接监听方上的方法。

## 分组：完整 API

```gdscript
add_to_group("saveable")                       # optional 2nd arg: persistent
remove_from_group("saveable")
is_in_group("saveable")
get_tree().get_nodes_in_group("saveable")      # Array[Node]
get_tree().get_first_node_in_group("player")   # first match or null
get_tree().call_group("enemies", "method", arg)
get_tree().set_group("enemies", "modulate", Color.RED)  # set a property on all
```

`call_group` 有标志变体（`call_group_flags`），支持延迟调用与唯一调用。

## 信号与直接调用：何时用哪个

- **信号**：发出者不该知道也不必关心谁在监听时使用（可复用场景、一对多、UI 与逻辑解耦）。
- **直接调用**：存在明确的拥有者→被拥有者关系、耦合可以接受时使用（控制器调用自己创建的组件上的方法）。对紧耦合代码过度使用信号只会徒增间接层。

## 全局事件总线（autoload）

跨场景的事件，在 autoload 上声明信号，任何场景都可以发出或连接：

```gdscript
# Events.gd (autoload). Emit: Events.player_died.emit(). Listen: Events.player_died.connect(...)
extends Node
signal player_died
signal level_completed(level_id: int)
```
