---
name: godot-signals-groups
description: >
  Godot 4.7 的信号与节点组：带类型的信号、使用 Callable 的 `connect()`、一次性与延迟连接、
  作为自动加载的事件总线，以及 `call_group` 广播。当节点之间需要通信又不希望持有硬引用、
  处理函数触发两次或从不触发，或日志提示 "already connected" 时使用。
  不适用于 GDScript 语法（`godot-gdscript`）或自动加载的配置（`godot-nodes-scenes`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/godot/godot-signals-groups/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Godot 信号与节点组（4.x）

用信号解耦节点，用节点组一次性对多个节点执行操作，而不是在场景之间硬编码引用。面向 **Godot 4.7**（见版本说明）。

## 何时使用

- 某个节点需要宣告"发生了某件事"（玩家死亡、道具被拾取、一波敌人清空），却不想持有对监听者的引用。
- 一整类节点需要一次调用即可全部处理（"暂停所有敌人"、"保存每个检查点"）。

**何时*不*使用：** 通用 GDScript 语法 → `godot-gdscript`；场景结构与自动加载注册 → `godot-nodes-scenes`。

## 核心工作流

1. **确定方向。** 子节点或子场景向上*发出*信号，父节点负责*连接*。子节点保持可复用，且无需知道谁在监听。向下调用你自己拥有的子节点只是一次普通方法调用，不是信号。
2. 在发射方**声明带类型的信号**，并让 `emit()` 传入的参数与声明完全一致。
3. **用 Callable 连接**（`sig.connect(_on_sig)`）。一次性触发使用 `CONNECT_ONE_SHOT`，传递额外上下文使用 `bind()`。
4. **编辑器中的连接与节点组在 `.tscn` 里只是纯文本**，因此无需打开"节点"面板即可读写它们：

   ```ini
   [node name="Goblin" type="CharacterBody2D" parent="Enemies" groups=["enemies"]]

   [connection signal="pressed" from="UI/StartButton" to="." method="_on_start_pressed"]
   ```

   `from`/`to` 是相对于场景根节点的路径，且 `method` 必须存在于 `to` 节点所挂的脚本上。
5. **用节点组做广播**：先 `add_to_group()`，再 `get_tree().call_group(...)` 或遍历 `get_nodes_in_group(...)`。
6. **跨场景事件把信号放到自动加载上**（事件总线，见参考资料）。
7. **收尾前先做检查。**
   - 如果你改动过 `.tscn` 连接，运行 `godot-nodes-scenes` Skill 的 `scripts/check_godot_project.py <project-dir>`；它会报告 `from`/`to` 节点不存在的 `[connection]` 条目，但不检查方法名。
   - 用无头测试（模式 4）在运行时验证接线，或者冒烟运行场景并检索日志：

     ```bash
     godot --headless --path . --fixed-fps 60 --quit-after 300 --scene res://level.tscn > run.log 2>&1
     grep -nE "^ *(SCRIPT ERROR|ERROR):" run.log   # signal errors print as ERROR: lines
     ```

     如果没有可用的 Godot 可执行文件（`godot`、`godot4` 或 `$GODOT_BIN`），请用户运行该命令并把 `run.log` 贴回来。

## 模式

### 1. 向上发出信号，由父节点连接

```gdscript
# coin.gd (reusable pickup; knows nothing about the player or HUD)
extends Area2D
signal collected(value: int)

func _ready() -> void:
    body_entered.connect(_on_body_entered)

func _on_body_entered(body: Node2D) -> void:
    if body.is_in_group("player"):
        collected.emit(10)
        queue_free()
```

```gdscript
# level.gd (the parent wires coins to game state)
func _ready() -> void:
    for coin in get_tree().get_nodes_in_group("coins"):
        coin.collected.connect(_on_coin_collected)

func _on_coin_collected(value: int) -> void:
    GameState.add_score(value)
```

### 2. 一次性连接与绑定参数

```gdscript
func _ready() -> void:
    $Door.opened.connect(_on_door_opened, CONNECT_ONE_SHOT)   # auto-disconnects
    # bind() appends its arguments after the signal's own arguments.
    $RedButton.pressed.connect(_on_button.bind("red"))

func _on_button(color: String) -> void:
    print("Pressed the %s button" % color)
```

### 3. 节点组：向多个节点广播

```gdscript
func pause_all_enemies() -> void:
    get_tree().call_group("enemies", "set_paused", true)   # skips nodes without the method
```

### 4. 无头测试：验证信号只到达处理函数一次

```gdscript
# res://tests/test_signals.gd
extends SceneTree

func _initialize() -> void:
    var level: Node = load("res://level.tscn").instantiate()
    root.add_child(level)                          # parent _ready() connects the coins
    await process_frame
    var coin: Node = get_first_node_in_group("coins")
    var failed := 0
    if coin == null or coin.collected.get_connections().size() != 1:
        failed += 1
        push_error("coin.collected should have exactly one connection")
    print("Results: %d failed" % failed)
    quit(1 if failed > 0 else 0)
```

用 `godot --headless --path . --script res://tests/test_signals.gd` 运行它并查看退出码。要检查处理函数的效果，可在测试中发出信号，并对它应当改变的状态做断言。

## 注意事项

- **3.x 的 `connect` 签名已废弃。** `connect("died", self, "_on_died")` → `died.connect(_on_died)`。`Object.connect("died", Callable(self, "_on_died"))` 仍然可用；方法名字符串形式则不可用。优先用 `died.emit()` 而非 `emit_signal("died")`：这样拼错信号名会在解析期报错，而不是在运行时。
- **把同一个方法连接两次**会打印 "Signal '...' is already connected to given callable"，并只保留一条连接。每次新建一个 lambda 都是*不同*的 Callable，因此会悄悄叠加，处理函数按连接次数触发。把 lambda 存进变量，或用 `if not sig.is_connected(cb):` 做保护。
- **lambda 的生命周期长于它捕获的节点。** 当发射方或 Callable 的持有者被释放时，Godot 会移除连接；但 lambda 属于创建它的脚本，捕获了后来被释放节点的 lambda 仍会继续触发并报错。连接监听方法，或自行断开已保存的 lambda。
- **参数不匹配会在发出信号时才失败。** `emit()` 不会依据 `signal` 声明校验参数；参数个数不同的处理函数会记录 "Error calling from signal ... Method expected N argument(s)"。声明带类型的参数，并严格按这些参数发出。
- **节点组对整个 `SceneTree` 全局有效**，而非按场景划分。两个关卡若使用同名节点组会共享成员；如有必要，给名称加上命名空间前缀。
- **`call_group` 会静默忽略缺少该方法的节点**，因此拼写错误会无声地失败。当契约很重要时，优先用带类型的信号。
- **指向不存在方法的 `[connection]`** 不会被检查脚本捕获；场景实例化时 Godot 会打印 "Cannot connect" 错误，因此冒烟运行能发现它。
- **在物理处理期间改动节点树的处理函数**（会触发 "flushing queries" 错误）→ 用 `CONNECT_DEFERRED` 连接，或用 `call_deferred` 延迟改动。

## 参考资料

- 当你需要全部连接标志、`unbind()`、带超时地等待信号、安全断开与 lambda 生命周期、完整的节点组 API、自动加载事件总线，或在"信号 vs 直接调用"之间做取舍时，阅读 `references/signal-patterns.md`。

## 相关 Skill

- `godot-gdscript`：信号与 `await` 语法。
- `godot-nodes-scenes`：用作全局事件总线的自动加载，以及检查脚本。
- `godot-gdscript-headless-testing`：把模式 4 纳入 CI。
- `game-ai`：驱动并消费这些事件的状态机。

## 版本说明

最后验证时间：2026-11-11，基于 Godot 4.7.2-stable（发布于 2026-08-18）。

- 参考资料中超时辅助函数用到的可变剩余参数（`..._args`）自 GDScript 4.5 起存在。
- "already connected" 与 "Method expected N argument(s)" 两条消息与 4.7.2 的 `object.cpp`、`variant.cpp` 一致。

来源：[object.cpp @ 4.7.2-stable](https://github.com/godotengine/godot/blob/4.7.2-stable/core/object/object.cpp)、[variant.cpp @ 4.7.2-stable](https://github.com/godotengine/godot/blob/4.7.2-stable/core/variant/variant.cpp)、[Signal @ 4.7.2-stable](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/Signal.xml)、[使用信号](https://docs.godotengine.org/en/stable/getting_started/step_by_step/signals.html)。
