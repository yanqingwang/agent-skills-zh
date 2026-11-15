> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/gamedev/godot-3d-essentials/references/scene-and-environment.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 3D 场景与环境参考（Godot 4.7）

`godot-3d-essentials` 的进阶配套参考。

内容：Transform3D；Camera3D；灯光；环境与后处理；材质；GridMap 与 MeshLibrary；烘焙光照与探针。

## Transform3D

一个 `Node3D` 拥有一个 `Transform3D` = `Basis`（3x3 的旋转/缩放）+ `origin`（Vector3）。

```gdscript
global_position = Vector3(1, 0, 2)
rotate_y(deg_to_rad(90))                 # rotate about local Y
rotation_degrees = Vector3(0, 45, 0)
look_at(target_global_pos, Vector3.UP)   # global-space orientation
transform = transform.translated_local(Vector3.FORWARD * 2.0)  # move along local -Z
basis = basis.orthonormalized()          # fix drift after many rotations
```

Godot 的 3D 惯例：**-Z 为前方**，+Y 为上方，+X 为右方。

## Camera3D

- `projection`：`PROJECTION_PERSPECTIVE`（fov）或 `PROJECTION_ORTHOGONAL`（size）。
- `fov`、`near`、`far`、`current`、`make_current()`、`clear_current()`。
- `project_ray_origin(screen_pos)` / `project_ray_normal(screen_pos)` 用于把点击位置换算到
  世界坐标做拾取（配合物理射线检测）。
- `unproject_position(world_pos)` → 屏幕坐标（例如浮动血条）。
- 做跟随/环绕镜头时，把相机作为枢轴 `Node3D` 的子节点，然后旋转枢轴。

## 灯光

| 节点 | 作用 | 关键属性 |
|------|------|-----------|
| `DirectionalLight3D` | 太阳（平行光线） | `shadow_enabled`、`light_energy`、`directional_shadow_mode` |
| `OmniLight3D` | 点光源 | `omni_range`、`light_energy`、`shadow_enabled` |
| `SpotLight3D` | 锥形光 | `spot_range`、`spot_angle`、`shadow_enabled` |
| `AreaLight3D`（4.7+） | 矩形面（屏幕、灯箱面板） | `area_size`、`area_range`、`area_attenuation`、`area_texture` |

通用：`light_color`、`light_energy`、`light_indirect_energy`，以及各项阴影 bias 设置。
投射阴影的灯太多会拖累性能，能烘焙静态光照就尽量烘焙。
`AreaLight3D` 的开销高于 omni/spot 灯：在 Forward+ 下，画面里每有一个可见的 area light，
每个被渲染的物体都会增加成本；Compatibility 渲染器则画不出它的阴影。把它留给特写镜头
和高端目标平台。

## 环境与后处理

`WorldEnvironment.environment`（一个 `Environment` 资源）：

- **背景：** `BG_CLEAR_COLOR`、`BG_COLOR`、`BG_SKY`（搭配一个 `Sky` +
  `ProceduralSkyMaterial`/`PanoramaSkyMaterial`）。
- **环境光：** `ambient_light_source`（sky/color/disabled）、`ambient_light_color`、
  `ambient_light_energy`。
- **色调映射：** `tonemap_mode`（`TONE_MAPPER_LINEAR`、`_REINHARDT`、`_FILMIC`、`_ACES`、
  `_AGX`）、`tonemap_exposure`、`tonemap_white`。
- **后处理：** `glow_enabled`（+ bloom/levels）、`ssao_enabled`、`ssil_enabled`、
  `sdfgi_enabled`（实时 GI）、`fog_enabled`/`volumetric_fog_enabled`、
  `adjustment_enabled`（亮度/对比度/饱和度 + 颜色校正）。

`CameraAttributes` 资源（Practical/Physical 两种）额外提供景深（DOF）、自动曝光和曝光
控制，可挂在相机或环境上。

各渲染器的支持情况（4.7 文档，"Overview of renderers" 一节）：

| 功能 | Compatibility | Mobile | Forward+ |
|---|---|---|---|
| SSAO | 是 | 否 | 是 |
| SSIL、SSR、SDFGI、体积雾 | 否 | 否 | 是 |
| 雾、辉光、色调映射、调整 | 是 | 是 | 是 |

## 材质

`StandardMaterial3D`（PBR）关键字段：`albedo_color`/`albedo_texture`、`metallic`、
`roughness`、`normal_enabled`+`normal_texture`、`emission_enabled`+`emission`、
`transparency`（`TRANSPARENCY_ALPHA`/`ALPHA_SCISSOR`）、`cull_mode`、`shading_mode`
（`SHADING_MODE_PER_PIXEL` / `UNSHADED`）。通过 `MeshInstance3D.material_override`（覆盖
所有表面）或 `set_surface_override_material(i, mat)`（按表面单独设置）来应用。
`ORMMaterial3D` 把 occlusion/roughness/metallic 打包进一张纹理。

## GridMap 与 MeshLibrary

1. 搭一个场景，让每个子节点都是一个网格 + 可选的碰撞体；把它导出为
   `MeshLibrary`（Scene > Export As > MeshLibrary）。4.7+ 提供了专门的 `MeshLibrary` 编辑器
   （类似 2D 的 `TileSet` 编辑器），添加和编辑条目快得多。
2. 把 `MeshLibrary` 赋给 `GridMap.mesh_library`，并设置 `cell_size`。
3. 在编辑器里绘制，或从代码绘制（见下）。朝向来自
   `GridMap.get_orthogonal_index_from_basis(basis)`。

```gdscript
func gridmap_calls(grid: GridMap, cell: Vector3i, item_id: int, orientation: int) -> void:
    grid.set_cell_item(cell, item_id, orientation)
    print(grid.get_cell_item(cell))          # -1 if empty (GridMap.INVALID_CELL_ITEM)
    print(grid.get_used_cells())
    var centre := grid.map_to_local(cell)    # cell -> local position of its centre
    print(grid.local_to_map(centre) == cell) # position -> cell
    grid.clear()
```

## 烘焙光照与探针

- `LightmapGI`：把静态 GI 烘焙进光照贴图，用于静态几何体（把网格标记为 "bake"）。
- `ReflectionProbe`：为一片区域提供局部 cubemap 反射。
- `VoxelGI` / `SDFGI`：动态 GI（更重）。静态场景要达到发布上线品质就用烘焙光照贴图，
  实时 GI 留给动态需求。
