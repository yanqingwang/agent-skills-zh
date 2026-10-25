---
name: godot-gdscript
description: >
  为 Godot 4.7 编写地道的 GDScript：静态类型、节点生命周期
  （_ready/_process/_physics_process）、@export/@onready/@tool 注解、
  信号（signals），以及用于异步流程的 await。适用于在 Godot 项目
  （project.godot）中编辑 .gd 脚本、编写或调试 GDScript，或将 3.x
  GDScript 迁移到 4.x（函数签名、yield 改 await、export 改 @export）时使用。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/godot/godot-gdscript/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Godot GDScript（4.x）

编写正确、静态类型的 GDScript，并按引擎期望的方式使用节点生命周期与信号
系统。目标版本为 **Godot 4.7**（GDScript 2.0）。

## 何时使用

- 在编写或修复 `.gd` 文件时使用：声明变量、函数、类，使用 `@export`/`@onready`，
  连接信号，或 await 协程/信号。
- 在把 Godot 3.x 脚本迁移到 4.x 且脚本已无法通过解析时使用。

**何时不使用：** 场景/节点结构与实例化问题 → `godot-nodes-scenes`；信号的
*架构*/解耦模式 → `godot-signals-groups`；改用 C# 而非 GDScript →
`godot-csharp`。

## 核心工作流

1. **能给一切标注类型就标注。** GDScript 2.0 支持静态类型
   （`var hp: int = 10`、`func add(a: int, b: int) -> int:`）。类型能在解析期
   捕获错误并加快 VM 运行。用 `:=` 表示推断类型。
2. **把生命周期回调用在它们该用的地方：** `_ready()` 在节点及其子节点进入
   场景树时运行一次；`_process(delta)` 每个渲染帧运行；`_physics_process(delta)`
   在固定的物理节拍上运行（移动/物理相关逻辑用它）。
3. **用 `@onready` 获取节点引用**，而不是在 `_init()` 里 ， 节点进入场景树
   之前子节点并不存在。
4. **用 `@export` 暴露可调参数**，让设计师能在 Inspector 中编辑。
5. **用信号 + `await` 响应事件**，在语义通顺的地方用它替代轮询。
6. **运行并阅读报错。** Debugger 面板会打印带行号的类型化错误；
   先修第一个错误（后面的错误往往是连锁反应）。

## 模式

### 1. 带生命周期、@export 与 @onready 的类型化脚本

```gdscript
extends Node2D
class_name Spinner            # registers a global type usable in other scripts

@export var speed: float = 90.0          # editable in the Inspector (degrees/sec)
@export_range(0, 10, 0.5) var wobble := 2.0
@onready var sprite: Sprite2D = $Sprite2D # resolved when the node enters the tree

func _ready() -> void:
    # Runs once, after children are ready. Safe to touch $Sprite2D here.
    sprite.modulate = Color.AQUA

func _process(delta: float) -> void:
    # delta is seconds since last frame; multiply rates by it for FPS independence.
    rotation_degrees += speed * delta
```

### 2. 信号：声明、发射、连接（4.x Callable 语法）

```gdscript
extends Node

signal health_changed(current: int, maximum: int)   # typed signal params

var health := 100

func take_damage(amount: int) -> void:
    health = maxi(health - amount, 0)    # maxi/maxf are typed; max() returns Variant
    health_changed.emit(health, 100)     # 4.x: emit as a method on the signal

func _ready() -> void:
    # 4.x: connect with a Callable, not a string method name.
    health_changed.connect(_on_health_changed)

func _on_health_changed(current: int, maximum: int) -> void:
    print("HP: %d/%d" % [current, maximum])
```

### 3. await ： 暂停直到计时器或信号触发（取代 3.x 的 yield）

```gdscript
func flash_then_continue() -> void:
    modulate = Color.RED
    await get_tree().create_timer(0.2).timeout   # resume after 0.2s
    modulate = Color.WHITE
    # await any signal: var result = await some_node.some_signal
```

### 4. Lambda、类型化数组与安全访问

```gdscript
var enemies: Array[Node] = []                    # typed array

func cull_dead() -> void:
    enemies = enemies.filter(func(e): return e.is_inside_tree())

func get_first_name(d: Dictionary) -> String:
    return d.get("name", "unknown")              # default avoids missing-key errors
```

## 陷阱

- **3.x → 4.x 的信号 API 变了。** `emit_signal("x")` 仍可用，但更推荐
  `x.emit(...)`；`connect("x", self, "_on_x")` 已被移除 ， 请使用带 Callable 的
  `x.connect(_on_x)`。`yield(obj, "sig")` 现在是 `await obj.sig`。
- **`export var` 现在是 `@export var`**（注解）。同理 `onready`→`@onready`、
  `tool`→`@tool`、RPC 关键字 `remote`/`master` → `@rpc(...)` 注解。
- **在 `_init()` 里使用 `@onready` 和 `$NodePath` 会失败** ， 此时节点尚未
  进入场景树。请在 `_ready()` 中或用 `@onready` 初始化节点引用。
- **整数除法会截断。** `5 / 2 == 2`。请使用 `5.0 / 2` 或转换为 `float`。
- **`_process` 与 `_physics_process` 的取舍。** 把 `move_and_slide()` 和物理
  逻辑放进 `_physics_process(delta)`；放在 `_process` 里会让运动依赖帧率。
- **`class_name` 必须全项目唯一**，且要想在其他脚本中使用该类型名、或将其
  用作 Inspector 类型，就必须声明它。
- **升级到 4.7 后某个 override 无法通过解析** → 自 4.7 起，覆写方法会继承
  父方法的类型化返回值，因此每条代码路径都必须 `return` 一个值（如有需要，
  在末尾补上 `return null`）。4.7 的另一项变化：对打包数组（packed array）
  属性的单个元素赋值（`points[0] = v`）不再触发该属性的 setter；若必须触发
  setter，请重新赋值整个数组。

## 参考资料

- 完整的注解列表、高级类型用法与风格约定，请阅读
  `references/annotations-and-typing.md`。

## 相关 Skill

- `godot-nodes-scenes` ， 场景树、实例化与 autoload。
- `godot-signals-groups` ， 基于信号与分组（groups）的事件驱动架构。
- `godot-resources` ， 基于自定义 `Resource` 类型的数据驱动设计。
- `godot-csharp` ， 用 C#/.NET 表达相同的引擎概念。
