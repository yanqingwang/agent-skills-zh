---
name: unity-navmesh
description: >
  使用 AI Navigation 包在 Unity 6.3 LTS 中寻路：NavMeshSurface 烘焙、NavMeshAgent、
  NavMeshLink 跳跃与运行时重新烘焙。当 Unity 中的敌人需要追逐或巡逻、Agent 不移动或发生瞬移、
  路径不完整，或 Bake 选项卡缺失时使用。不适用于决定 NPC 何时移动
  （`game-ai`、`ai-behavior-trees-utility-ai`），也不适用于受力驱动的移动
  （`unity-physics`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/unity/unity-navmesh/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Unity NavMesh（AI Navigation）

在 Unity 6.3 LTS（6000.3）中借助 AI Navigation 包 2.0 为 NPC 提供寻路能力：烘焙可行走表面，让 Agent 绕开障碍物移动，并通过读回网格与路径来证实它们确实存在。

> **版本陷阱：** 旧的内置 Navigation 窗口（Object 与 Bake 选项卡、"Navigation Static" 标志）
> 已经消失。烘焙改为基于组件：`NavMeshSurface`
> （`Unity.AI.Navigation`，包 `com.unity.ai.navigation`）持有烘焙设置与烘焙数据。
> 该包的 **Window > AI > Navigation** 只编辑 Agent 类型和区域。
> 运行时 API（`NavMeshAgent`、`NavMesh`、`NavMeshObstacle`）仍位于 `UnityEngine.AI`。

## 何时使用

- Agent 需要行走、追逐或巡逻到某个目标；关卡需要已烘焙的表面；门或箱子要在运行时阻断路径；你需要判断某个目标是否可达。
- 项目中包含 `com.unity.ai.navigation`、`NavMeshSurface`，或使用 `UnityEngine.AI` 的脚本。

**何时不用：** 决定何时、向何处移动 → `game-ai` 或 `ai-behavior-trees-utility-ai`；不属于寻路的受力驱动或运动学移动 → `unity-physics`。如果安装了 Unity 官方的 `initialize-ai-navigation` skill 且已连接 Editor，它可以替你添加并烘焙这些组件；本 Skill 仍负责 Agent 代码与各项检查。

## 工作流

1. **先把包这一关。** 在 `Packages/packages-lock.json` 中查找 `com.unity.ai.navigation`，而不只是 `manifest.json`：Editor 尚未解析的包与从未添加过的包会产生相同的 "type not found" 错误。若它缺失，先询问再把它加入 `manifest.json`。
2. **添加任何东西之前先盘点。** 在场景中 grep `NavMeshSurface`、`NavMeshAgent`、`NavMeshObstacle`、`NavMeshLink` 以及已弃用的 `OffMeshLink`。Agent 类型（半径、高度、台阶高度、坡度）和区域名称位于 `ProjectSettings/NavMeshAreas.asset`（`m_Settings`、`areas`）。
3. **烘焙表面。** 选择其中一条路径：
   - 已就绪 Editor 搭配 Unity CLI：`unity command navmesh bake_surfaces`（单纯的 `navmesh bake` 命令是旧的内置烘焙，不是 `NavMeshSurface`）。
   - 程序化或流式加载的关卡：在几何体存在之后调用 `surface.BuildNavMesh()`（模式 3）。不会向磁盘写入任何内容。
   - 否则请用户选中带有 `NavMeshSurface` 的 GameObject 并按下 **Bake**，然后从文件确认（第 6 步）。
   每当几何体、`NavMeshModifier` 或 Agent 设置发生变化时都要重新烘焙。
4. **添加 `NavMeshAgent`**，其 Agent 类型要与烘焙所用的类型一致，并生成在网格上。用 `SetDestination` 驱动它；用 `pathPending` 与 `remainingDistance` 判断到达。
5. **在运行时阻断路径**，使用 `NavMeshObstacle` 并设 `carving = true`，而不是重新烘焙。用 `NavMeshLink` 连接彼此分离的孤岛（台阶、缺口）。
6. **验证**，使用下面的检查。

## 常用模式

### 1. 带定时重寻路的追逐


```csharp
using UnityEngine;
using UnityEngine.AI;

[RequireComponent(typeof(NavMeshAgent))]
public class Chaser : MonoBehaviour
{
    [SerializeField] private Transform target;
    [SerializeField] private float repathInterval = 0.2f;
    private NavMeshAgent _agent;
    private float _nextRepath;

    private void Awake() => _agent = GetComponent<NavMeshAgent>();

    private void Update()
    {
        if (!target || Time.time < _nextRepath) return;
        _nextRepath = Time.time + repathInterval;
        _agent.SetDestination(target.position);
    }

    // pathPending guards the frames before the first path exists.
    public bool HasArrived() =>
        !_agent.pathPending && _agent.remainingDistance <= _agent.stoppingDistance;
}
```


### 2. 提交之前先检查可达性


```csharp
public static bool CanReach(NavMeshAgent agent, Vector3 destination)
{
    var path = new NavMeshPath();
    agent.CalculatePath(destination, path);
    return path.status == NavMeshPathStatus.PathComplete;   // Partial means another island
}
```


### 3. 运行时烘焙并跨越缺口


```csharp
using Unity.AI.Navigation;
using UnityEngine;

public class LevelNav : MonoBehaviour
{
    [SerializeField] private NavMeshSurface surface;

    // Call after spawning the level geometry.
    public void Rebuild() => surface.BuildNavMesh();

    // One-way drop from a ledge to the floor below.
    public NavMeshLink AddDrop(Vector3 ledge, Vector3 landing)
    {
        var link = gameObject.AddComponent<NavMeshLink>();
        // Points are local to this GameObject; the link ignores its scale.
        Quaternion toLocal = Quaternion.Inverse(transform.rotation);
        link.startPoint = toLocal * (ledge - transform.position);
        link.endPoint = toLocal * (landing - transform.position);
        link.width = 1f;
        link.bidirectional = false;
        return link;
    }
}
```


## 验证

说明你采用了哪条路径。

- **搭配已就绪 Editor 的 Unity CLI：** 烘焙之后读回网格和一条真实路径：

  
```bash
  unity command script eval --code 'var t = UnityEngine.AI.NavMesh.CalculateTriangulation(); return "triangles=" + t.indices.Length / 3;'
  unity command script eval --code 'var p = new UnityEngine.AI.NavMeshPath(); UnityEngine.AI.NavMesh.CalculatePath(GameObject.Find("Enemy").transform.position, GameObject.Find("Player").transform.position, UnityEngine.AI.NavMesh.AllAreas, p); return p.status.ToString();'
  ```


  三角形数为零表示没有烘焙或加载任何内容。在 Play 模式下，还要为每个 Agent 读取
  `agent.isOnNavMesh` 与 `agent.pathStatus`。用 `unity command --query navmesh`
  查找当前的命令名称。
- **不使用 CLI：** 已烘焙的表面会在场景文件中保存一个引用。在 `.unity` 文件里 grep 该表面的 `m_NavMeshData:` 行；`{fileID: 0}` 表示从未烘焙或已被清空，`guid:` 表示存在烘焙数据（确认该资源文件确实存在）。然后编写一个 PlayMode 测试，加载场景，在两个已知点之间调用 `NavMesh.CalculatePath` 并断言 `PathComplete`；按 `unity-csharp-scripting` 中描述的方式运行它。
- **无法断言的行为：** 请用户按下 Play，并报告每个 Agent 是否到达目标、大约耗时多久。

## 常见陷阱

- **还在找 Bake 选项卡或 Navigation Static。** 它们已随 AI Navigation 2.0 移除。请从 `NavMeshSurface` 烘焙。
- **Agent 不移动或瞬移到原点。** 它不在已烘焙的网格上，或者没有表面被烘焙或启用（只有活跃 GameObject 上已启用的表面才会加载其数据）。用 `NavMesh.SamplePosition` 把生成位置吸附到网格上，并用 `agent.Warp` 移动它，而不是改 Transform。
- **`PathPartial`。** 目标位于另一个孤岛。添加 `NavMeshLink`，或扩展几何体让一个表面覆盖两侧；部分路径只能到达近侧的边缘。
- **Agent 忽略新增的几何体。** 网格是烘焙出来的数据。运行时道具需要启用 carving 的 `NavMeshObstacle`，或调用 `BuildNavMesh()`。
- **带 Rigidbody 的 NPC 抖动或漂移。** Agent 与非运动学的 `Rigidbody` 都在移动 Transform。在 Agent 掌控期间把刚体设为运动学。
- **同一 GameObject 上同时挂了 `NavMeshObstacle` 的 Agent 会打转或滑动。** 它在躲避自己。一次只启用其中一个，例如当 NPC 永久停下时关掉 Agent、打开障碍物。
- **Agent 尺寸与烘焙用的 Agent 类型不匹配。** 它会卡在缝隙里或悬空。让该 Agent 的类型、半径和高度与表面的 Agent 类型保持一致。
- **旧场景里的 `OffMeshLink`。** 在 AI Navigation 2.0 中已弃用，并从 Add Component 菜单中移除。用 `NavMeshLink` 替换它，后者增加了 Transform 端点和 `activated` 标志。
- **对大量 Agent 每帧都调用 `SetDestination`。** 会浪费路径查询；改用定时器重寻路（模式 1），或在目标移动超过某个阈值时再重寻路。
- **Agent 彼此之间抖动。** 调整 `avoidancePriority` 和障碍物避让质量，或者对永不移动的阻挡物使用一个障碍物。

## 参考资料

- AI Navigation 手册：https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/index.html
  （更改烘焙设置或把 Agent 与物理混合使用时，请阅读 `NavMeshSurface`、`NavMeshLink` 以及 "Use NavMesh Agent with other components" 这几页）。

## 相关 Skill

- `game-ai`：借助这套移动方式做出的、与引擎无关的决策（FSM、转向、感知）。
- `unity-csharp-scripting`：围绕 Agent 的 MonoBehaviour、测试程序集以及 `.meta` 检查器。
- `tower-defense`、`fps-shooter`：把寻路与玩法结合起来的游戏类型。

## 版本说明

最后验证日期：2026-11-11。

- 据 Unity 包注册表（https://packages.unity.com/com.unity.ai.navigation），AI Navigation 2.0.16（发布于 2026-10-07）是面向 Unity 6000.0 及更高版本的最新 2.0 包。`NavMeshSurface.m_NavMeshData`、`NavMeshLink` 的属性以及 `BuildNavMesh` 均在 2.0.16 的包源码中核对过。
- `OffMeshLink` 的弃用说明：https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/whats-new.html
- `navmesh bake_surfaces` 是 `com.unity.pipeline` 1.0.0-pre.1 的一条命令（预发布版）：https://docs.unity3d.com/Packages/com.unity.pipeline@1.0/manual/index.html
- 运行时 API 已在 Unity C# 参考源码的 6000.3.28f1 标签处核对，位于 `Modules/AI/`（`NavMesh.CalculateTriangulation`、`CalculatePath`、`SamplePosition`、`NavMeshAgent.isOnNavMesh`）。
