> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/godot/godot-shaders/references/shading-language.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Godot 着色语言参考（Godot 4.7）

本文件是 `godot-shaders` Skill 的深度配套参考。这门语言语法类似 GLSL，并附带引擎内置量。

目录：着色器类型与处理器函数 · 常用内置量 · uniform 提示 ·
渲染模式 · varying · vertex() 位移 · 自定义 light() · 2D 法线贴图 ·
可视化着色器 · 性能说明

## 着色器类型与处理器函数

| `shader_type` | 适用对象 | 主函数 | 关键输出写入 |
|---------------|---------|-------------------|--------------|
| `canvas_item` | 2D `CanvasItem` 材质 | `vertex`, `fragment`, `light` | `COLOR` |
| `spatial` | 3D `Mesh`/表面材质 | `vertex`, `fragment`, `light` | `ALBEDO`, `EMISSION`, `ALPHA`, `ROUGHNESS`, `METALLIC`, `NORMAL_MAP` |
| `particles` | `GPUParticles` 处理 | `start`, `process` | `VELOCITY`, `TRANSFORM`, `COLOR` |
| `sky` | `Sky` 材质 | `sky` | `COLOR` |
| `fog` | `FogVolume` | `fog` | `DENSITY`, `ALBEDO`, `EMISSION` |

## 常用内置量

canvas_item：`UV`、`COLOR`、`TEXTURE`、`TEXTURE_PIXEL_SIZE`、`SCREEN_UV`、
`SCREEN_PIXEL_SIZE`、`VERTEX`、`TIME`、`POINT_COORD`，以及 `vertex()` 中的 `MODEL_MATRIX`、
`CANVAS_MATRIX`、`SCREEN_MATRIX`（3.x 的 `MODELVIEW_MATRIX` 已不存在）。

spatial：`VERTEX`（模型/局部空间）、`NORMAL`、`TANGENT`、`UV`、`UV2`、`VIEW`、`ALBEDO`、
`ALPHA`、`EMISSION`、`ROUGHNESS`、`METALLIC`、`SPECULAR`、`NORMAL_MAP`、`TIME`、
`CAMERA_POSITION_WORLD`、`MODEL_MATRIX`、`VIEW_MATRIX`、`PROJECTION_MATRIX`、`FRAGCOORD`。

## Uniform 提示（4.x）

```glsl
uniform float speed : hint_range(0.0, 1.0) = 0.5;
uniform float gain  : hint_range(0.0, 2.0, 0.01);     // min, max, step
uniform vec4 col    : source_color = vec4(1.0);       // sRGB color picker
uniform sampler2D tex : source_color, filter_linear_mipmap, repeat_enable;
uniform sampler2D screen_tex : hint_screen_texture, filter_linear_mipmap;
uniform sampler2D depth_tex  : hint_depth_texture;
uniform sampler2D normal_rough : hint_normal_roughness_texture;
group_uniforms Movement;                               // Inspector grouping
uniform float amplitude = 1.0;
```

采样器的 filter/repeat 限定符：`filter_nearest`、`filter_linear`、
`filter_nearest_mipmap`、`filter_linear_mipmap`、`repeat_enable`、`repeat_disable`。

在代码中设置：`material.set_shader_parameter("name", value)`；
读取用 `get_shader_parameter("name")`。

## 渲染模式

紧跟在类型声明之后的首行修饰符，用逗号分隔：

- spatial：`unshaded`、`cull_disabled`、`cull_front`、`depth_draw_opaque`、
  `depth_test_disabled`、`blend_add`、`blend_mul`、`diffuse_toon`、`specular_toon`、
  `world_vertex_coords`、`vertex_lighting`、`shadows_disabled`、`ambient_light_disabled`。
- canvas_item：`blend_mix`（默认）、`blend_add`、`blend_sub`、`blend_mul`、
  `blend_premul_alpha`、`unshaded`、`light_only`。

```glsl
shader_type spatial;
render_mode unshaded, cull_disabled;
```

## varying（从 vertex 向 fragment 传递数据）

```glsl
varying vec3 world_pos;
void vertex()   { world_pos = (MODEL_MATRIX * vec4(VERTEX, 1.0)).xyz; }
void fragment() { ALBEDO = fract(world_pos); }
```

## vertex() 位移

```glsl
void vertex() {
    VERTEX.y += sin(VERTEX.x * 4.0 + TIME * 2.0) * 0.1;   // wave the mesh
}
```

## 自定义 light()（toon 色阶示例，spatial）

```glsl
void light() {
    float ndl = dot(NORMAL, LIGHT);
    float ramp = step(0.0, ndl);                 // hard two-tone
    DIFFUSE_LIGHT += ALBEDO * LIGHT_COLOR.rgb * ramp * ATTENUATION;
}
```

## 2D 法线贴图

要让 2D 物体受光，在 `canvas_item` 的 fragment 中写入 `NORMAL_MAP`（或在节点上指定
法线贴图），再向场景添加 `Light2D`/`PointLight2D`；`light()` 决定受光响应。

## 可视化着色器

`VisualShader` 可以逐节点搭建出同样的图，并导出为这门语言。适合迭代调试；生成的代码
就是标准 Godot 着色语言。需要精细控制或想在源码里做版本管理时，转成文本格式的
`.gdshader`。

## 性能说明

- 纹理采样与 `discard` 是常见操作中开销最大的两类，两者都要尽量少用。
- 基于 uniform（每次 draw 恒定）的分支很廉价；基于逐像素值的分支可能很慢。
- 某个值在三角形内呈线性变化时，先在 `vertex()` 里预计算，再用 `varying` 传递。
- 逐像素选择优先用 `mix()`、`step()`、`smoothstep()`、`clamp()`，而不是 `if`。
