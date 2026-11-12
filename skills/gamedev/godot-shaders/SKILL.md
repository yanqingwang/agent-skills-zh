---
name: godot-shaders
description: >
  Godot 4.7 着色语言语法与流程：canvas_item、spatial 与粒子着色器、内置变量、ShaderMaterial 接线、
  无头编译检查以及 3.x 移植。适用于处理 .gdshader、SHADER ERROR、从 GDScript 设置着色器参数，
  或效果发白、排序错误等情况。不适用于溶解、描边之类的效果数学（`shader-programming`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/godot/godot-shaders/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Godot 着色器（4.x）

用 Godot 着色语言编写 `.gdshader` 文件、把它们接到材质上，并验证能够编译。面向 **Godot 4.7**（见版本说明）。效果技术（溶解、描边、卡通渐变的数学）属于 `shader-programming`；本 Skill 只讲 Godot 的语法、内置变量与流程。

## 何时使用

- 编写或移植 `.gdshader` 代码、修复 `SHADER ERROR`、接线 `ShaderMaterial`、选择渲染模式，或从代码设置 uniform。

**何时*不*使用：** 跨引擎的着色技术 → `shader-programming`；`StandardMaterial3D`、灯光与环境 → `godot-3d-essentials`。`GPUParticles` 节点属性（相对于 `particles` 着色器而言）不在本 Skill 范围内。

## 核心工作流

1. **在第一行选定着色器类型**：任何 `CanvasItem`（Sprite2D、TextureRect、Control）用 `shader_type canvas_item;`，3D 网格用 `shader_type spatial;`。此外还有 `particles`、`sky` 和 `fog`。
2. **写入该类型要求的输出**：`canvas_item` 写 `COLOR`；`spatial` 写 `ALBEDO`、`EMISSION`、`ROUGHNESS`、`METALLIC`。`vertex()` 移动几何体；`light()` 替换光照。
3. **把可调参数暴露为带提示的 `uniform`**（颜色用 `source_color`，滑块用 `hint_range`），使其显示在检查器中并纳入色彩管理。
4. **接线材质。** 在 `.tscn` 中它只是纯文本，因此无需在检查器中点击：

   ```ini
   [ext_resource type="Shader" path="res://fx/scroll.gdshader" id="1_fx"]

   [sub_resource type="ShaderMaterial" id="ShaderMaterial_fx"]
   shader = ExtResource("1_fx")
   shader_parameter/scroll_speed = 0.5

   [node name="Water" type="Sprite2D" parent="."]
   material = SubResource("ShaderMaterial_fx")
   ```

   从代码设置：`material.set_shader_parameter("scroll_speed", 0.5)`。
5. **收尾前先做检查。**
   - 用模式 4 对每个着色器做无头编译，再检索日志：

     ```bash
     godot --headless --path . --script res://tests/compile_shaders.gd > shaders.log 2>&1
     grep -nE "SHADER ERROR|Shader compilation failed" shaders.log   # no output = pass
     ```

     无头模式使用一个仍会运行 Godot 着色器编译器的虚拟渲染器，因此语法错误、未知内置变量、错误的输出变量与错误的提示都会暴露出来。它不会运行 GPU 驱动，所以请用户用项目所用的渲染器（Forward+、Mobile 或 Compatibility）打开场景，并反馈显示效果以及 Output 面板中的任何错误。
   - 如果你在 `.tscn` 里接线了材质，还要运行 `godot-nodes-scenes` Skill 的 `scripts/check_godot_project.py <project-dir>` 来确认 `ext_resource` 路径。
   - 如果没有可用的 Godot 可执行文件（`godot`、`godot4` 或 `$GODOT_BIN`），请用户运行上面的命令并把 `shaders.log` 贴回来。

## 模式

### 1. canvas_item：着色与滚动 UV

```glsl
shader_type canvas_item;

uniform vec4 tint : source_color = vec4(1.0);
uniform float scroll_speed : hint_range(0.0, 2.0) = 0.3;

void fragment() {
    vec2 uv = UV + vec2(TIME * scroll_speed, 0.0);
    COLOR = texture(TEXTURE, uv) * tint;          // TEXTURE = the node's own texture
}
```

节点的纹理必须设置为重复，滚动才能回绕：在 CanvasItem 上设置 `texture_repeat`，或自行采样 `uniform sampler2D tex : repeat_enable;`。

### 2. spatial：不透明材质上的自发光边缘光

```glsl
shader_type spatial;

uniform vec4 base_color : source_color = vec4(0.2, 0.5, 1.0, 1.0);
uniform vec3 rim_color : source_color = vec3(0.6, 0.8, 1.0);
uniform float rim_power : hint_range(0.5, 8.0) = 3.0;

void fragment() {
    ALBEDO = base_color.rgb;
    float rim = pow(1.0 - clamp(dot(NORMAL, VIEW), 0.0, 1.0), rim_power);  // view space
    EMISSION = rim_color * rim;                   // no ALPHA write: stays opaque
}
```

### 3. 读取屏幕的后处理效果（4.x 提示，而非 SCREEN_TEXTURE）

```glsl
shader_type canvas_item;

uniform sampler2D screen_tex : hint_screen_texture, filter_linear_mipmap;
uniform float blur : hint_range(0.0, 4.0) = 1.0;

void fragment() {
    vec2 px = SCREEN_PIXEL_SIZE * blur;
    vec4 c = texture(screen_tex, SCREEN_UV);
    c += texture(screen_tex, SCREEN_UV + vec2(px.x, 0.0));
    c += texture(screen_tex, SCREEN_UV - vec2(px.x, 0.0));
    COLOR = c / 3.0;
}
```

### 4. 对每个 `.gdshader` 做无头编译检查

```gdscript
# res://tests/compile_shaders.gd
extends SceneTree

func _initialize() -> void:
    var paths := _find("res://", "gdshader")
    for path in paths:
        print("compiling ", path)                 # a SHADER ERROR prints right after this
        var shader := load(path) as Shader
        shader.get_shader_uniform_list()         # forces the compile; load() alone is lazy
    print("Compiled %d shaders" % paths.size())
    quit(0)

func _find(dir: String, ext: String) -> PackedStringArray:
    var found := PackedStringArray()
    for file in DirAccess.get_files_at(dir):
        if file.get_extension() == ext:
            found.append(dir.path_join(file))
    for sub in DirAccess.get_directories_at(dir):
        if not sub.begins_with("."):             # skips .godot/ and other hidden folders
            found.append_array(_find(dir.path_join(sub), ext))
    return found
```

嵌入在 `.tscn` 中的着色器（`[sub_resource type="Shader"]`）不是文件；通过冒烟运行该场景（`--scene res://... --quit-after 10`）并用同样方式检索日志来覆盖它们。

## 注意事项

- **3.x → 4.x 的重命名。** `SCREEN_TEXTURE` 与 `DEPTH_TEXTURE` 已移除；改为声明 `uniform sampler2D x : hint_screen_texture;`（或 `hint_depth_texture`）并用 `SCREEN_UV` 采样。Forward+ 还提供 `hint_normal_roughness_texture`。`hint_color`/`hint_albedo` → `source_color`；`hint_white`/`hint_black` → `hint_default_white`/`hint_default_black`。在 `canvas_item` 的 `vertex()` 中，3.x 的 `MODELVIEW_MATRIX` 现为 `MODEL_MATRIX` / `CANVAS_MATRIX` / `SCREEN_MATRIX`。
- **输出变量写错。** 在 `spatial` 的 `fragment()` 中，`COLOR` 是只读的顶点色，给它赋值会导致编译错误；应写 `ALBEDO`。
- **不带 `source_color` 的颜色 uniform** 会被当作原始线性值，看起来发白或偏暗。
- **物体绘制顺序错乱、不投射阴影，或跳过 SSAO（3D）** → spatial 着色器读取或写入了 `ALPHA`，即便该值恒为 `1.0`，也会把整个材质移到透明管线。对于硬裁剪，改用 `ALPHA_SCISSOR_THRESHOLD`，它仍留在不透明通道。
- **在 [0,1] 之外采样 UV 会被钳制**，除非采样器 uniform 带有 `repeat_enable`（或对 `TEXTURE` 而言，节点开启了 `texture_repeat`）。
- **效果每小时跳变一次** → `TIME` 会在 `rendering/limits/time/time_rollover_secs` 处回绕（默认 3600）。选择能整除回绕周期的周期，或传入自己的时间 uniform。
- **仅调用 `load()` 不会编译着色器。** `Shader` 在首次使用时会创建其 GPU 端对象，这正是模式 4 调用 `get_shader_uniform_list()` 的原因。
- **`discard` 会破坏早期深度测试**，在部分 GPU 上开销更大；在混合模式允许的地方优先用 alpha。

## 参考资料

- 当你需要各着色器类型的内置变量、渲染模式名称、采样器过滤/重复限定符、`varying`、`vertex()` 位移、自定义 `light()` 函数、2D 法线贴图或性能规则时，阅读 `references/shading-language.md`。

## 相关 Skill

- `shader-programming`：效果技术（溶解、描边、菲涅尔、暗角）。
- `godot-3d-essentials`：材质、环境，以及 spatial 着色器的归属。
- `godot-ui-control`：把着色器应用到 UI。
- `godot-gdscript-headless-testing`：在 CI 中运行模式 4。

## 版本说明

最后验证时间：2026-11-11，基于 Godot 4.7.2-stable（发布于 2026-08-18）。

- 无头（虚拟）渲染器会用引擎的着色器编译器编译着色器并打印 `SHADER ERROR:` 行；`Shader` 资源在首次使用时惰性编译。
- 参考资料中列出的渲染模式与内置变量存在于 4.7.2 的 `shader_types.cpp`。

来源：[dummy material_storage.cpp @ 4.7.2-stable](https://github.com/godotengine/godot/blob/4.7.2-stable/servers/rendering/dummy/storage/material_storage.cpp)、[shader.cpp @ 4.7.2-stable](https://github.com/godotengine/godot/blob/4.7.2-stable/scene/resources/shader.cpp)、[shader_types.cpp @ 4.7.2-stable](https://github.com/godotengine/godot/blob/4.7.2-stable/servers/rendering/shader_types.cpp)、[着色语言](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html)、[从 Godot 3 升级到 4](https://docs.godotengine.org/en/stable/tutorials/migrating/upgrading_to_godot_4.html)。
