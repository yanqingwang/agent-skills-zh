---
name: unity-tilemap-2d
description: >
  Unity 6.3 LTS 2D Tilemap：Tile Palette、搭配 Composite Collider 的 Tilemap Collider 2D、
  Rule Tiles 以及运行时的 SetTile。适用于绘制或生成瓦片关卡、瓦片碰撞体之间的接缝、
  找不到 RuleTile，或六边形与等距网格。不适用于关卡设计
  （`level-design`）、生成（`procedural-gen`）、移动（`unity-physics`）或 Godot
  （`godot-tilemap`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/unity/unity-tilemap-2d/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Unity 2D Tilemap

在 Unity 6.3 LTS（6000.3）中用 `Grid` 和 `Tilemap` 制作并脚本化基于瓦片的 2D 关卡，
使用合并后的碰撞体与运行时绘制，并通过回读地图来检查结果。

> **包说明：** `Grid`、`Tilemap`、`Tile` 和 `TilemapCollider2D` 为内置。Tile Palette
> 窗口与默认笔刷来自 2D Tilemap Editor 包
> （`com.unity.2d.tilemap`，已包含在 2D 模板中）。Rule Tiles、Animated Tiles 以及
> 额外的笔刷（Random、Line、GameObject、Group）位于 **2D Tilemap Extras**
> （`com.unity.2d.tilemap.extras`，Unity 6.3 对应 6.0.x 系列）。

## 何时使用

- 用瓦片排布 2D 关卡、`Grid` 带 `Tilemap` 子对象、地图的碰撞、
  用 Rule Tiles 自动拼接、从脚本生成或编辑瓦片。
- 场景中包含带 `Tilemap` 子对象的 `Grid`，或存在瓦片与调色板的 `.asset`
  文件。

**何时不使用：** 布局与节奏 → `level-design`；生成瓦片数据的噪声、房间和地牢
生成 → `procedural-gen`；在瓦片上行走的角色 → `unity-physics`；3D 网格此处
没有对应 Skill。若安装了 Unity 官方的 `create-tile-palette-or-rule-tiles`
Skill 且已连接 Editor，可用它构建调色板和 Rule Tile 资源；本 Skill 负责
运行时代码与碰撞体。

## 工作流程

1. **先确认包。** 在编写 `RuleTile` 或 `AnimatedTile` 代码前，确认
   `com.unity.2d.tilemap.extras` 已出现在 `Packages/packages-lock.json` 中；添加前先征询。
2. **搭建网格。** 每层一个 `Grid` 配一个 `Tilemap`（外加 `TilemapRenderer`）：
   背景、地面、前景。`Grid` 的 Cell Layout 可为 Rectangle、Hexagon、Isometric
   或 Isometric Z As Y。为每个 `TilemapRenderer` 显式指定 Sorting Layer 和 Order。
3. **制作瓦片。** 设计人员将切分好的 sprite sheet 拖入 Tile Palette。在代码中，
   编辑器脚本可从该图集的 sprites 创建 `Tile` 资源（见模式 3）。
4. **为实体层添加碰撞。** 添加 `TilemapCollider2D`，再加一个 `CompositeCollider2D`
   （它会自动加上 `Rigidbody2D`：将其设为 `Static`），并把 tilemap 碰撞体的 Composite
   Operation 设为 Merge。合并后的单一形状开销更低且没有接缝。
5. **在运行时以单元格坐标编辑**（`Vector3Int`）：`WorldToCell`、`SetTile`、
   `GetTile`、`SetTilesBlock`，然后仅对改动过的单元格调用 `RefreshTile`。
6. **按下面的检查项验证。**

## 常用模式

### 1. 运行时绘制与查询


```csharp
using UnityEngine;
using UnityEngine.Tilemaps;

public class TilePainter : MonoBehaviour
{
    [SerializeField] private Tilemap tilemap;
    [SerializeField] private TileBase groundTile;

    public void PaintAt(Vector3 worldPos) => tilemap.SetTile(tilemap.WorldToCell(worldPos), groundTile);

    public bool IsSolid(Vector3 worldPos) => tilemap.HasTile(tilemap.WorldToCell(worldPos));
}
```


### 2. 一次调用填充区域


```csharp
// SetTilesBlock writes a whole BoundsInt at once: use it for generated rooms and floors.
public static void FillFloor(Tilemap map, TileBase tile, int width, int height)
{
    var bounds = new BoundsInt(0, 0, 0, width, height, 1);
    var tiles = new TileBase[width * height];
    for (int i = 0; i < tiles.Length; i++) tiles[i] = tile;
    map.SetTilesBlock(bounds, tiles);
}
```


`SetTile(cell, null)` 会擦除一个单元格。`RefreshTile(cell)` 重新计算该单元格及其规则邻居；
`RefreshAllTiles()` 重新计算整张地图，因此只在整体重新生成时使用。

### 3. 从切分好的图集创建 Tile 资源（编辑器代码）

把它放进 `Editor` 文件夹；可从菜单运行，也可通过
`unity command script eval --code 'TileAssets.FromSheet("Assets/Art/terrain.png", "Assets/Tiles");'`，
或从无参数包装器用 `-executeMethod` 运行。


```csharp
using System.Linq;
using UnityEditor;
using UnityEngine;
using UnityEngine.Tilemaps;

public static class TileAssets
{
    public static void FromSheet(string sheetPath, string outFolder)
    {
        if (!AssetDatabase.IsValidFolder(outFolder))   // e.g. "Assets/Tiles"; the parent must exist
        {
            int slash = outFolder.LastIndexOf('/');
            AssetDatabase.CreateFolder(outFolder.Substring(0, slash), outFolder.Substring(slash + 1));
        }

        foreach (Sprite sprite in AssetDatabase.LoadAllAssetsAtPath(sheetPath).OfType<Sprite>())
        {
            var tile = ScriptableObject.CreateInstance<Tile>();
            tile.sprite = sprite;
            AssetDatabase.CreateAsset(tile, $"{outFolder}/{sprite.name}.asset");
        }
        AssetDatabase.SaveAssets();
    }
}
```


该图集必须已按 Sprite (Multiple) 导入并完成切分；切分结果是 sprite
子资源。

## 验证

- **无需 Editor：** 场景 YAML 保存着地图。`Tilemap:` 文档在 `m_Tiles:` 下列出
  已绘制的单元格（`- first: {x: 0, y: 8, z: 0}`），设为合并的 `TilemapCollider2D`
  具有 `m_CompositeOperation: 1`。grep 这些字段以确认该层有瓦片且
  碰撞体已合并。
- **具备就绪 Editor 时的 Unity CLI：**


```bash
  unity command script eval --code 'var t = GameObject.Find("Ground").GetComponent<UnityEngine.Tilemaps.Tilemap>(); t.CompressBounds(); return t.GetUsedTilesCount() + " tiles, bounds " + t.cellBounds;'
  unity command script eval --code 'var c = GameObject.Find("Ground").GetComponent<CompositeCollider2D>(); return "paths=" + c.pathCount;'
  ```


  单个连通区域合并后的层应只报告少量路径，而不是每个瓦片一条。
  对 Rule Tiles，在临时 tilemap 中绘制一小块，并读取
  角、边和中心单元格的 `GetSprite(cell)`。
- **无 CLI：** PlayMode 或 EditMode 测试可在代码中构建 `Grid` 和 `Tilemap`，调用
  `SetTilesBlock`，并断言 `GetUsedTilesCount()` 和 `GetSprite` 的结果（配置见
  `unity-csharp-scripting`）。
- **外观：** 请用户进入 Play 模式，反馈任何可见的接缝或排序问题，
  尽可能附上截图。

## 常见陷阱

- **找不到 `RuleTile` 类型。** 2D Tilemap Extras 未安装或尚未解析。
- **每个瓦片一个碰撞体很慢，还会让角色卡在接缝上。** 通过
  `CompositeCollider2D` 配合静态 `Rigidbody2D` 以及 Composite Operation = Merge 来合并。
- **没有 "Used By Composite" 复选框，或 `usedByComposite` 出现弃用警告。** Unity 6
  用 `Collider2D.compositeOperation` 取代了它；`usedByComposite = true` 变为
  `CompositeOperation.Merge`。
- **合并后仍有细小缝隙。** 调高 Tilemap Collider 2D 的 Extrusion Factor，让
  相邻形状落在 composite 的 Vertex Distance 之内。
- **世界坐标与单元格坐标混淆。** `SetTile`/`GetTile` 接受 `Vector3Int` 单元格。
  用 `WorldToCell`/`CellToWorld` 转换（或用 `GetCellCenterWorld` 取瓦片中心）。
- **瓦片意外绘制在 sprite 之上或之下。** 显式设置每个 `TilemapRenderer` 的 Sorting
  Layer 和 Order in Layer；多个 tilemap 需要显式排序。
- **脚本编辑后 Rule 或动画瓦片不更新。** 用 `RefreshTile` 刷新改动过的单元格；
  在大地图上调用 `RefreshAllTiles()` 会卡顿。
- **`cellBounds` 比绘制区域大。** 擦除瓦片后边界不会收缩，除非
  调用 `CompressBounds()`。
- **绘制落到了错误的层上。** Tile Palette 会绘制到它的 Active Tilemap；检查
  该下拉框，或在代码中显式设置 tilemap 引用。

## 相关 Skill

- `level-design`：blockout、节奏与布局实践。
- `procedural-gen`：生成传给 `SetTilesBlock` 的瓦片数据。
- `unity-physics`：`Rigidbody2D` 移动以及针对合并后碰撞体的 2D 查询。
- `platformer`、`roguelike`、`puzzle`：将本章内容与移动和生成结合的游戏类型。

## 版本说明

最后验证日期：2026-11-11，基于 Unity 6000.3.28f1。

- 2D Tilemap Extras 6.0.3（2026-08-12）是 6.0.x 系列的最新版本，该系列
  面向 Unity 6000.3；4.1.x 面向 6000.0，10.0.x 面向 6000.7。来源：Unity package
  registry，https://packages.unity.com/com.unity.2d.tilemap.extras. 包手册：
  https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@6.0/manual/index.html
- `Collider2D.CompositeOperation`（`Merge = 1`）、`usedByComposite` 弃用、
  `Tilemap.GetUsedTilesCount`、`CompressBounds`、`GetSprite` 以及
  `CompositeCollider2D.pathCount` 均在标签 6000.3.28f1 的 Unity C# 参考源码中核对过
  （`Modules/Physics2D/`、`Modules/Tilemap/`）。
- 手册：https://docs.unity.com/en-us/engine/6000.3/manual/unity2d/tilemaps/reference/tilemap
- `script eval` 是 `com.unity.pipeline` 1.0.0-pre.1 的命令（预发布版）：
  https://docs.unity3d.com/Packages/com.unity.pipeline@1.0/manual/index.html
