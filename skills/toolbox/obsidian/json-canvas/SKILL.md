---
name: json-canvas
description: 创建和编辑 JSON Canvas 文件（.canvas），涵盖节点、连线、分组和连接。在处理 .canvas 文件、创建可视化画布、思维导图、流程图，或用户在 Obsidian 中提到 Canvas 文件时使用本 Skill。
---

> **中文汉化版** · 上游：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) · 原文件：`skills/json-canvas/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# JSON Canvas Skill

## 文件结构

Canvas 文件（`.canvas`）包含两个顶层数组，遵循 [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/)：

```json
{
  "nodes": [],
  "edges": []
}
```

- `nodes`（可选）：节点对象数组
- `edges`（可选）：连接节点的连线对象数组

## 常见工作流

### 1. 创建新 Canvas

1. 创建一个基础结构为 `{"nodes": [], "edges": []}` 的 `.canvas` 文件
2. 为每个节点生成唯一的 16 位十六进制 ID（例如 `"6f0ad84f44ce9c17"`）
3. 添加节点，必填字段：`id`、`type`、`x`、`y`、`width`、`height`
4. 添加连线，通过 `fromNode` 和 `toNode` 引用有效的节点 ID
5. **验证**：解析 JSON 确认其合法。核实所有 `fromNode`/`toNode` 值都存在于 nodes 数组中

### 2. 向现有 Canvas 添加节点

1. 读取并解析现有 `.canvas` 文件
2. 生成一个与现有节点或连线 ID 都不冲突的唯一 ID
3. 选择不与现有节点重叠的位置（`x`、`y`），留出 50-100px 间距
4. 将新节点对象追加到 `nodes` 数组
5. 可选：添加连线，将新节点与现有节点连接
6. **验证**：确认所有 ID 唯一，且所有连线引用都指向已存在的节点

### 3. 连接两个节点

1. 确定源节点和目标节点的 ID
2. 生成唯一的连线 ID
3. 将 `fromNode` 和 `toNode` 设为源 ID 和目标 ID
4. 可选：设置 `fromSide`/`toSide`（top、right、bottom、left）作为锚点
5. 可选：设置 `label` 作为连线上的描述文字
6. 将该连线追加到 `edges` 数组
7. **验证**：确认 `fromNode` 和 `toNode` 都引用已存在的节点 ID

### 4. 编辑现有 Canvas

1. 以 JSON 形式读取并解析 `.canvas` 文件
2. 通过 `id` 定位目标节点或连线
3. 修改所需属性（文本、位置、颜色等）
4. 将更新后的 JSON 写回文件
5. **验证**：编辑后重新检查 ID 唯一性和连线引用完整性

## 节点（Nodes）

节点是放置在画布上的对象。数组顺序决定 z-index：第一个节点在最底层，最后一个节点在最顶层。

### 通用节点属性

| 属性 | 必填 | 类型 | 说明 |
|-----------|----------|------|-------------|
| `id` | 是 | string | 唯一的 16 位十六进制标识符 |
| `type` | 是 | string | `text`、`file`、`link` 或 `group` |
| `x` | 是 | integer | X 坐标（像素） |
| `y` | 是 | integer | Y 坐标（像素） |
| `width` | 是 | integer | 宽度（像素） |
| `height` | 是 | integer | 高度（像素） |
| `color` | 否 | canvasColor | 预设 `"1"`-`"6"` 或十六进制（如 `"#FF0000"`） |

### 文本节点（Text Nodes）

| 属性 | 必填 | 类型 | 说明 |
|-----------|----------|------|-------------|
| `text` | 是 | string | 支持 Markdown 语法的纯文本 |

```json
{
  "id": "6f0ad84f44ce9c17",
  "type": "text",
  "x": 0,
  "y": 0,
  "width": 400,
  "height": 200,
  "text": "# Hello World\n\nThis is **Markdown** content."
}
```

**换行陷阱**：在 JSON 字符串中用 `\n` 表示换行。**不要**使用字面量 `\\n` —— Obsidian 会将其渲染为字符 `\` 和 `n`。

### 文件节点（File Nodes）

| 属性 | 必填 | 类型 | 说明 |
|-----------|----------|------|-------------|
| `file` | 是 | string | 系统内文件的路径 |
| `subpath` | 否 | string | 指向标题或块的链接（以 `#` 开头） |

```json
{
  "id": "a1b2c3d4e5f67890",
  "type": "file",
  "x": 500,
  "y": 0,
  "width": 400,
  "height": 300,
  "file": "Attachments/diagram.png"
}
```

### 链接节点（Link Nodes）

| 属性 | 必填 | 类型 | 说明 |
|-----------|----------|------|-------------|
| `url` | 是 | string | 外部 URL |

```json
{
  "id": "c3d4e5f678901234",
  "type": "link",
  "x": 1000,
  "y": 0,
  "width": 400,
  "height": 200,
  "url": "https://obsidian.md"
}
```

### 分组节点（Group Nodes）

分组是用于组织其他节点的可视化容器。子节点应位于分组边界之内。

| 属性 | 必填 | 类型 | 说明 |
|-----------|----------|------|-------------|
| `label` | 否 | string | 分组的文字标签 |
| `background` | 否 | string | 背景图片路径 |
| `backgroundStyle` | 否 | string | `cover`、`ratio` 或 `repeat` |

```json
{
  "id": "d4e5f6789012345a",
  "type": "group",
  "x": -50,
  "y": -50,
  "width": 1000,
  "height": 600,
  "label": "Project Overview",
  "color": "4"
}
```

## 连线（Edges）

连线通过 `fromNode` 和 `toNode` ID 连接节点。

| 属性 | 必填 | 类型 | 默认值 | 说明 |
|-----------|----------|------|---------|-------------|
| `id` | 是 | string | - | 唯一标识符 |
| `fromNode` | 是 | string | - | 源节点 ID |
| `fromSide` | 否 | string | - | `top`、`right`、`bottom` 或 `left` |
| `fromEnd` | 否 | string | `none` | `none` 或 `arrow` |
| `toNode` | 是 | string | - | 目标节点 ID |
| `toSide` | 否 | string | - | `top`、`right`、`bottom` 或 `left` |
| `toEnd` | 否 | string | `arrow` | `none` 或 `arrow` |
| `color` | 否 | canvasColor | - | 线条颜色 |
| `label` | 否 | string | - | 文字标签 |

```json
{
  "id": "0123456789abcdef",
  "fromNode": "6f0ad84f44ce9c17",
  "fromSide": "right",
  "toNode": "a1b2c3d4e5f67890",
  "toSide": "left",
  "toEnd": "arrow",
  "label": "leads to"
}
```

## 颜色

`canvasColor` 类型接受十六进制字符串或预设编号：

| 预设 | 颜色 |
|--------|-------|
| `"1"` | 红色 |
| `"2"` | 橙色 |
| `"3"` | 黄色 |
| `"4"` | 绿色 |
| `"5"` | 青色 |
| `"6"` | 紫色 |

预设颜色值有意保持未定义 —— 各应用使用自己的品牌色。

## ID 生成

生成 16 位小写十六进制字符串（64 位随机值）：

```
"6f0ad84f44ce9c17"
"a3b2c1d0e9f8a7b6"
```

## 布局指南

- 坐标可以为负（画布无限延伸）
- `x` 向右增大，`y` 向下增大；坐标指左上角位置
- 节点间距保持 50-100px；分组内部留出 20-50px 内边距
- 对齐网格（10 或 20 的倍数）以获得更整洁的布局

| 节点类型 | 建议宽度 | 建议高度 |
|-----------|-----------------|------------------|
| 小型文本 | 200-300 | 80-150 |
| 中型文本 | 300-450 | 150-300 |
| 大型文本 | 400-600 | 300-500 |
| 文件预览 | 300-500 | 200-400 |
| 链接预览 | 250-400 | 100-200 |

## 验证清单

创建或编辑 canvas 文件后，请核对：

1. 所有 `id` 值在节点和连线中均唯一
2. 每个 `fromNode` 和 `toNode` 都引用已存在的节点 ID
3. 每种节点类型的必填字段齐全（文本节点需 `text`，文件节点需 `file`，链接节点需 `url`）
4. `type` 为以下之一：`text`、`file`、`link`、`group`
5. `fromSide`/`toSide` 取值为以下之一：`top`、`right`、`bottom`、`left`
6. `fromEnd`/`toEnd` 取值为以下之一：`none`、`arrow`
7. 颜色预设为 `"1"` 到 `"6"` 或合法十六进制（如 `"#FF0000"`）
8. JSON 合法且可解析

若验证失败，检查 ID 重复、悬空的连线引用或格式错误的 JSON 字符串（尤其是文本内容中未转义的换行符）。

## 完整示例

完整 canvas 示例（含思维导图、项目看板、研究画布和流程图）见 [references/EXAMPLES.md](references/EXAMPLES.md)。

## 参考资料

- [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/)
- [JSON Canvas GitHub](https://github.com/obsidianmd/jsoncanvas)
