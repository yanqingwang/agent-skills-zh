> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/gamedev/godot-gdscript/references/annotations-and-typing.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# GDScript 注解与类型标注参考（Godot 4.7）

`godot-gdscript` 的深度配套参考。在 GDScript 2.0 中，所有注解都以 `@` 开头。

## 常用导出注解

```gdscript
@export var title: String = "Level 1"
@export var enabled := true
@export_range(0, 100, 1) var percent: int = 50          # min, max, step
@export_range(0.0, 1.0, 0.01, "or_greater") var gain := 1.0
@export_enum("Idle", "Walk", "Run") var state: int       # int-backed dropdown
@export_enum("Sword", "Bow") var weapon: String          # string-backed dropdown
@export_flags("Fire", "Water", "Earth") var resist: int  # bitmask
@export_file("*.json") var data_path: String             # file picker
@export_dir var folder: String
@export_multiline var description: String                 # multi-line text box
@export_color_no_alpha var tint: Color
@export_node_path("Camera2D") var cam_path: NodePath
@export_group("Movement")                                 # groups Inspector fields
@export var speed := 200.0
@export_subgroup("Air")
@export var air_control := 0.4
```

导出类型化的资源数组（非常适合数据驱动设计）：

```gdscript
@export var waves: Array[PackedScene] = []
@export var loot: Array[ItemResource] = []
```

## 其他注解

- `@onready var x = $Child`：节点进入场景树时赋值。
- `@tool`：在编辑器中运行脚本（放在文件顶部）。编辑器专属代码要用
  `if Engine.is_editor_hint():` 保护。
- `@icon("res://icon.svg")`：为 `class_name` 类型设置自定义 Inspector 图标。
- `@rpc("any_peer", "call_local", "reliable")`：标记网络方法（参见
  `godot-multiplayer`）。
- `@warning_ignore("unused_variable")`：屏蔽指定的解析器警告。
- `@static_unload`：允许卸载脚本的静态变量。
- `@export_tool_button("Rebuild") var rebuild_action := rebuild`：Inspector 中的按钮，
  点击时调用一个 `Callable`（4.4+；脚本还必须是 `@tool`）。
- `@export_storage var cache: Array`：随场景/资源一并保存，但在 Inspector 中
  不显示。
- `@abstract`（4.5+）：用在类上（置于 `class_name` 之前）时该类不可实例化；用在
  无方法体的方法上时，每个具体子类都必须实现它。

## 静态类型细节

```gdscript
var a: int = 3                 # explicit type
var b := 3                     # inferred int via :=
var c: float                   # typed, defaults to 0.0
var nodes: Array[Node2D] = []  # typed array (element type enforced)
var scores: Dictionary[String, int] = {}  # typed dictionary (Godot 4.4+)
var any_data: Dictionary = {}  # untyped: keys and values can be anything

func clamp_hp(hp: int) -> int:
    return clampi(hp, 0, 100)  # clampi/clampf are typed variants

func best_score(name: String) -> int:
    var s: int = scores.get(name, 0)  # get() returns Variant even on a typed dictionary,
    return s                          # so `var s := scores.get(...)` fails to parse
```

带类型的代码运行更快，因为 VM 可以跳过运行时类型检查；编辑器还能在你运行之前
提供自动补全并标出类型不匹配。

## 生命周期回调（顺序）

1. `_init()`：对象已构造（尚无场景树，子节点也未解析）。
2. `_enter_tree()`：节点已加入场景树（子节点可能尚未就绪）。
3. `_ready()`：节点及其全部子节点都已进入场景树（只运行一次）。`@onready` 变量
   在此之前刚完成赋值。
4. `_process(delta)`：每个渲染帧执行（用 `set_process(false)` 可跳过）。
5. `_physics_process(delta)`：每个固定物理刻执行（默认 60 Hz）。
6. `_exit_tree()`：节点从场景树移除。
7. `_notification(what)`：底层兜底回调（例如 `NOTIFICATION_WM_CLOSE_REQUEST`）。

## 惯用写法

- 操作可能已被释放的节点前，先检查 `is_instance_valid(node)`。
- 在一帧之内安全删除节点，用 `queue_free()`（延迟执行）而非 `free()`。
- `match` 是 GDScript 的 switch：支持值、数组 `[1, var x]`，以及 `_` 默认分支。
- 字符串格式化：`"%s scored %d" % [name, score]`。
- 用 `assert(cond, "msg")` 写只在调试时生效的断言（发布构建中会被剥离）。
