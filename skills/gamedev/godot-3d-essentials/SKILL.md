---
name: godot-3d-essentials
description: >
  搭建 Godot 4.7 3D 场景：Node3D 变换、Camera3D、光照
  （DirectionalLight3D/OmniLight3D）、用于天空/环境光/色调映射/后处理的
  WorldEnvironment、MeshInstance3D 材质，以及用于基于瓦片的 3D 关卡的 GridMap。
  在 Godot 项目中构建 3D 场景、放置相机/灯光、配置环境与后处理，
  或处理 Node3D/.tscn 3D 内容与 GridMap 时使用。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/godot/godot-3d-essentials/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Godot 3D 基础（4.x）

组装一个可运行的 3D 场景：变换、相机、灯光、环境/后处理、材质，以及 `GridMap`
关卡白模（blockout）。面向 **Godot 4.7**。

## 何时使用

- 在开始搭建或修复 3D 场景时使用：摆放 `Camera3D`、添加灯光、设置
  `WorldEnvironment`（天空、环境光、色调映射、泛光/SSAO）、指定材质，或用
  `GridMap` 搭建关卡。

**何时不使用：** 编写空间着色器 → `godot-shaders`；3D 物理体与射线检测 →
`godot-physics`；角色动画混合 → `godot-animation`；完整 FPS 模板 →
`fps-shooter` 类型 Skill。

## 核心工作流

1. **一切 3D 对象都是 `Node3D`**，携带一个 `Transform3D`（位置、旋转基、缩放）。
   用 `global_position` 移动，用 `rotate_y(angle)` 或 `look_at(target)` 旋转。
2. **添加一个 `Camera3D`。** 将其标记为 `current`（或调用 `make_current()`）；设置
   `fov`、`near`、`far`。要做环绕或跟随相机，可把它挂到 rig/pivot（支架/枢轴）下。
3. **为场景打光。** `DirectionalLight3D` 相当于太阳；`OmniLight3D`/`SpotLight3D` 是
   局部光源；`AreaLight3D`（4.7+）是矩形面光源，开销高于 omni/spot。按灯逐个开启阴影。
   没有灯光和环境光时，表面会渲染成黑色。
4. **添加一个 `WorldEnvironment`**，并配置 `Environment` 资源：背景（天空/颜色）、
   环境光、色调映射，以及后处理（泛光、SSAO、雾、调整）。
5. **为网格指定材质**（`StandardMaterial3D` 或 `ShaderMaterial`），挂在
   `MeshInstance3D` 上。
6. **用 `GridMap` 搭建关卡白模**，它把 `MeshLibrary` 条目放置到 3D 网格上
   （相当于 3D 版的瓦片地图）。

## 模式

### 1. 跟随相机（第三人称、平滑）

```gdscript
extends Camera3D

@export var target: Node3D
@export var offset := Vector3(0, 4, 8)
@export var smooth := 6.0

func _physics_process(delta: float) -> void:
    if target == null:
        return
    var desired := target.global_position + offset
    global_position = global_position.lerp(desired, smooth * delta)  # smooth follow
    look_at(target.global_position, Vector3.UP)                      # face the target
```

### 2. 用代码创建太阳 + 环境

```gdscript
func _ready() -> void:
    var sun := DirectionalLight3D.new()
    sun.rotation_degrees = Vector3(-45, -30, 0)
    sun.shadow_enabled = true
    add_child(sun)

    var we := WorldEnvironment.new()
    var env := Environment.new()
    env.background_mode = Environment.BG_SKY
    env.sky = Sky.new()
    env.sky.sky_material = ProceduralSkyMaterial.new()
    env.ambient_light_source = Environment.AMBIENT_SOURCE_SKY
    env.tonemap_mode = Environment.TONE_MAPPER_FILMIC
    env.glow_enabled = true
    we.environment = env
    add_child(we)
```

### 3. 从代码指定 StandardMaterial3D

```gdscript
func tint_mesh(mesh: MeshInstance3D, color: Color) -> void:
    var mat := StandardMaterial3D.new()
    mat.albedo_color = color
    mat.metallic = 0.0
    mat.roughness = 0.6
    mat.emission_enabled = true
    mat.emission = color * 0.3
    mesh.material_override = mat       # overrides the mesh's surface materials
```

### 4. 向 GridMap 放置瓦片

```gdscript
@onready var grid: GridMap = $GridMap   # cell_size + mesh_library set in the editor

func build_floor(width: int, depth: int, item_id: int) -> void:
    for x in width:
        for z in depth:
            # set_cell_item(Vector3i cell, int item, orientation = 0)
            grid.set_cell_item(Vector3i(x, 0, z), item_id)
```

## 常见陷阱

- **场景渲染成黑色** → 没有灯光也没有环境光。添加一个 `DirectionalLight3D` 和/或一个
  带环境光/天空的 `WorldEnvironment`。新建场景默认两者皆无。
- **没有相机 / 相机不对。** 如果什么都看不到，说明没有 `Camera3D` 处于 `current`
  状态。设置 `current = true` 或调用 `make_current()`；每个视口只渲染一个相机。
- **混淆局部变换与全局变换。** `position`/`rotation` 相对父节点；
  `global_position`/`global_transform` 是世界空间。在旋转过的父节点下混用二者会得到
  出乎意料的结果。`look_at` 使用全局坐标。
- **缩放物理/灯光。** 在 `Node3D` 上使用非均匀 `scale` 会使子节点的碰撞体和灯光变形；
  建议改为缩放网格资源本身，或使用均匀缩放。
- **`look_at` 不生效并打印错误** → 目标与节点位置重合、`up` 向量与观察方向平行
  （例如用 `Vector3.UP` 垂直向下看），或节点尚未进入场景树。保留一个偏移、传入不同的
  `up`，或在节点入树前改用 `look_at_from_position()`。
- **没有 `MeshLibrary` 的 GridMap** 什么也放不了。创建一个 `MeshLibrary`（由场景生成）
  并赋给它；`set_cell_item(cell, -1)` 用于清除一个格子。
- **HDR/泛光过强** → 检查 `tonemap_mode` 和泛光阈值；在 filmic 色调映射下，原始
  自发光数值会产生很重的辉光。

## 参考资料

- 关于 Transform3D 数学、相机投影模式、灯光/阴影参数、完整的 Environment/后处理选项、
  `MeshLibrary` 创建，以及 `ReflectionProbe`/`LightmapGI` 光照，请阅读
  `references/scene-and-environment.md`。

## 相关 Skill

- `godot-physics` — 3D 物理体、Area 与射线检测。
- `godot-shaders` — 用于自定义 3D 表面的空间着色器。
- `godot-animation` — 面向 3D 角色的 `AnimationTree`。
- `camera-systems` — 第三人称环绕 / 第一人称视角的相机装置、取景与碰撞。
- `performance-optimization` — 让 3D 场景守住帧预算（draw call、灯光、LOD）。
- `fps-shooter` — 将 3D 移动、输入与 AI 组合成一整个游戏。
