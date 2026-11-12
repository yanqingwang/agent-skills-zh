---
name: level-design
description: >
  引擎无关的关卡设计，附 Godot 检查项：从真实控制器测得的角色指标、带软锁检查的钥匙与能力门禁，以及节奏把控。
  适用于规划关卡或类银河恶魔城的门禁布局，或玩家迷路、钥匙被锁在自家门后的情形。
  不适用于布局生成（`procedural-gen`）、绘制图块（`godot-tilemap`、`unity-tilemap-2d`）或跳跃调校（`platformer`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/disciplines/level-design/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 关卡设计

关卡是一连串通过空间呈现的预期体验。有效的顺序是：测量角色参数、用基础几何体搭建粗模、检查可达性与节奏、收集试玩反馈，最后再美化装饰。本 Skill 引擎无关，附 Godot 4.7 的检查项。绘制网格用 `godot-tilemap` 或 `unity-tilemap-2d`；生成布局用 `procedural-gen`。

## 适用场景

- 规划关卡结构：关键路径、可选分支、门禁顺序、遭遇战，以及某个机制在何处教学、何处考验。
- 搭建粗模，检查每一处必需的跳跃与门禁是否可行。
- 复盘让玩家困惑、感到乏味或陷入软锁的关卡。

**不适用本 Skill：** 布局生成器与地牢算法（`procedural-gen`）、跳跃与移动调校（`platformer` 及引擎移动 Skill）、空间中敌人的行为（`game-ai`）、镜头取景（`camera-systems`）。

## 核心工作流

1. **从游戏实测指标，而非凭记忆估计。** 从玩家脚本读取移动常量，再运行跳跃测量（模式 1）得到真实的最高点、跨越距离与滞空时间。所有缺口、平台与通道都按这些单位来定尺寸。
2. **用无贴图的基础几何体按真实比例搭建整个关卡的粗模**：Godot 中开启 `use_collision` 的 `CSGBox3D` 等节点、Unity ProBuilder（`com.unity.probuilder`）、Unreal 的 Modeling Mode，或 2D 中一套纯灰图块集。CSG 仅用于原型；发布上线前用 `bake_static_mesh()` 和 `bake_collision_shape()` 将其烘焙。
3. **编写房间图**（房间、出口、每个出口需要什么、每个房间给予什么）和节拍清单，放在关卡旁边。二者都是供下方检查读取的小数据文件。
4. **先铺关键路径，再铺黄金路径**（多数玩家会走的路线），然后是重新汇入主线的可选分支。
5. **把控节奏并做好教学。** 强度以锯齿状上升，每个高峰前安排一段喘息。每个机制先在失败代价低的地方出现，再放到有压力的情境下。
6. **带着意图设置门禁**，使用钥匙、能力和单向落差。用光照、引导线和地标来引导，而不是靠墙。
7. **运行各项检查**（见"检查"），修正粗模，之后才带着具体问题请用户试玩。
8. **最后再做美术装饰**，任何几何改动之后都要重新运行检查。

## 模式

### 1. 测量真实跳跃（无头模式）


```gdscript
# tools/measure_jump.gd: godot --headless --path . --script res://tools/measure_jump.gd
# Runs the real player scene on flat ground with run + jump held and prints the reach.
extends SceneTree

const PLAYER := "res://player.tscn"            # the game's player scene
const RUN := &"move_right"
const JUMP := &"jump"

func _initialize() -> void:
    var ground := StaticBody2D.new()
    var shape := CollisionShape2D.new()
    shape.shape = WorldBoundaryShape2D.new()     # infinite floor at y = 0, normal up
    ground.add_child(shape)
    root.add_child(ground)
    var player: CharacterBody2D = load(PLAYER).instantiate()
    player.position = Vector2(0, -64)
    root.add_child(player)
    for i in 30:                                 # let the player land and settle
        await physics_frame
    Input.action_press(RUN)
    for i in 30:                                 # reach full run speed
        await physics_frame
    var start := player.position
    Input.action_press(JUMP)
    var apex := 0.0
    var ticks := 0
    var airborne := false
    while ticks < 600:
        await physics_frame
        ticks += 1
        apex = maxf(apex, start.y - player.position.y)
        if not player.is_on_floor():
            airborne = true
        elif airborne:
            break                                # landed back on the same height
    Input.action_release(JUMP)
    Input.action_release(RUN)
    var dt := 1.0 / Engine.physics_ticks_per_second
    print("JUMP apex=%.1f distance=%.1f airtime=%.3fs" % [apex, player.position.x - start.x, ticks * dt])
    quit(0 if airborne else 1)
```


按住跳跃键测得的是完整跳跃；若控制器支持可变跳跃高度，可按住一个 tick 后松开，测得短跳。公式 `h = v² / 2g` 与 `d = run_speed * 2v / g` 只描述理想抛物线：`RUN_SPEED` 为 240、`JUMP_VELOCITY` 为 420、重力为 980 的控制器，理论上是 90 px 与 206 px，而这里实测得到 93.6 px 的跳跃顶点和 212 px 的跨越距离，因为固定步长按整 tick 积分。下落重力、空中加速度、碰撞体宽度以及落点更高，都会再次改变这个数值。必需缺口按实测跨越距离的约 0.7 来定尺寸，可选挑战的缺口保持在 0.95 附近。3D 场景改用 `StaticBody3D`、`WorldBoundaryShape3D` 和 `CharacterBody3D`。

### 2. 用数据描述节奏，并附带检查


```gdscript
# Author the level as beats with an intended intensity (0..1), then check the curve.
const BEATS := [
    { "room": "entry",      "type": "teach",   "intensity": 0.1 },
    { "room": "hall_1",     "type": "combat",  "intensity": 0.5 },
    { "room": "vista",      "type": "rest",    "intensity": 0.1 },  # breather + reward
    { "room": "gauntlet",   "type": "combat",  "intensity": 0.8 },
    { "room": "save_room",  "type": "rest",    "intensity": 0.2 },  # before the boss
    { "room": "boss",       "type": "climax",  "intensity": 1.0 },
]

# Returns the pacing problems in a beat list; empty means it passes.
func pacing_problems(beats: Array, high := 0.7, max_high_run := 2) -> PackedStringArray:
    var problems := PackedStringArray()
    var run := 0
    for i in beats.size():
        var beat: Dictionary = beats[i]
        run = run + 1 if beat["intensity"] >= high else 0
        if run > max_high_run:
            problems.append("%s: %d high-intensity beats in a row" % [beat["room"], run])
        if beat["type"] == "climax" and (i == 0 or beats[i - 1]["type"] != "rest"):
            problems.append("%s: no rest beat right before the climax" % beat["room"])
    if not beats.is_empty() and beats[0]["type"] != "teach":
        problems.append("%s: the level does not open with a teach beat" % beats[0]["room"])
    return problems
```


这些阈值是用户游戏的起点。用同一张表来驱动刷怪密度和音乐强度，让建成的关卡与规划一致。

### 3. 门禁与关键路径（一个小型图）


```gdscript
# Model the level as rooms + gated connections. Validate that the goal is
# reachable with the keys/abilities the player can actually obtain in order.
const ROOMS := {
    "entry":   { "exits": [ { "to": "hall_1" } ] },
    "hall_1":  { "exits": [ { "to": "vista", "needs": "double_jump" },
                            { "to": "side_room" } ] },           # optional branch
    "side_room": { "exits": [ { "to": "hall_1" } ], "grants": "double_jump" },
    "vista":   { "exits": [ { "to": "boss", "needs": "red_key" } ] },
}

# Search (room, held keys) states: keys from mutually exclusive one-way branches
# must not be combined. Keys are never consumed and doors never re-lock; model
# consumable keys as counts and persistent door changes as additional state.
# States grow exponentially with distinct keys; fine for hand-built room graphs.
func goal_reachable(rooms: Dictionary, start: String, goal: String) -> bool:
    var pending: Array[Dictionary] = [{"room": start, "keys": {}}]
    var visited := {}                             # "room|sorted keys" -> true
    while not pending.is_empty():
        var state: Dictionary = pending.pop_back()
        var room: String = state["room"]
        var have: Dictionary = state["keys"].duplicate()
        var info: Dictionary = rooms.get(room, {})
        var grant = info.get("grants")
        if grant != null:
            have[grant] = true
        var names := PackedStringArray(have.keys())
        names.sort()
        var id := room + "|" + ",".join(names)
        if visited.has(id):
            continue                              # cycles stop only at an equivalent state
        visited[id] = true
        if room == goal:
            return true
        for exit in info.get("exits", []):
            var open: bool = not exit.has("needs") or have.has(exit["needs"])
            if open:
                pending.append({"room": exit["to"], "keys": have})
    return false
# goal_reachable(ROOMS, "entry", "boss") is FALSE for the table above: no room
# grants "red_key". That is exactly the soft-lock this check exists to catch.
```


出口是单向的：普通门要写两个方向，落差只写一个方向。若关卡必须保证玩家永不被困，还要从玩家可达的每个房间调用 `goal_reachable`，检查能否回到起点或存档点；落入死胡同的单向落差会让这一调用失败。

## 检查

1. **可达性：** 在无头测试中运行 `goal_reachable` 检查起点到终点（参照 `godot-gdscript-headless-testing`），并从每个单向落差的落点房间检查能否回到存档点或出口。任何 `false` 都意味着软锁，要优先修复。
2. **指标：** 每次改动移动参数后都运行模式 1。列出粗模中每一处必需的缺口与平台，与实测跨越距离对比；关键路径上任何超过该距离约 0.7 的地方都需要给出理由。
3. **节奏：** `pacing_problems(BEATS)` 应返回空，或剩下的每一行都是你能向用户解释清楚的有意选择。
4. **借助用户试玩。** 你无法直接观察玩家，因此要请用户给出具体反馈，例如："从起点独自打到 boss 一次。告诉我哪里不确定该往哪走、有没有哪处跳跃失败超过三次、哪个房间让人觉得是苦差事，以及这趟流程花了多久。"把每条反馈对应到房间图，修正粗模，而不是改美术。

## 常见陷阱

- **还没玩通就先做美术。** 在最可能被改动的布局上，为未经验证的粗模做美术是开销最大的工作。
- **只用公式算指标。** 理想抛物线会高估或低估真实跨越距离，取决于步长、下落重力和碰撞体。要去实测真实控制器。
- **只验证连通性，不验证顺序。** 泛洪填充会显示每个房间都连通，可钥匙仍被锁在自家门后。要像模式 3 那样跟踪已持有的钥匙。
- **把双向边写成单向**（或反过来）会让困住玩家的关卡通过检查，或让正常的关卡不通过。每个出口都要按玩家实际可用的方向来写。
- **节奏平淡。** 从头到尾都是战斗、或从头到尾都很平静，都会让玩家麻木。要交替安排，并在高潮前留出喘息和存档点。
- **先考验机制、后教学。** 玩家第一次遇到危险时应当是安全的。
- **靠墙来引导。** 迷路的玩家通常需要的是视线、光照或地标，而不是屏障。
- **单向落差缺少提示** 会让玩家被困或受惊。对不可逆的移动要提前示意。
- **指望生成器给出人工编排的节奏。** 生成带来的是变化，不是意图；用 `procedural-gen` 获得变化，把需要意图的节拍手工编排出来。

## 参考资料

- `references/pacing-and-flow.md`：在塑造张力曲线、为新机制设计"引入-展开-转折-考验"循环、选择门禁工具、在 2D 或 3D 空间中引导玩家，或对粗模做评审时阅读。

## 相关 Skill

- `platformer`：产出这些指标的跳跃调校；改动后要重新测量。
- `procedural-gen`：作为人工结构补充的生成布局。
- `godot-tilemap`、`unity-tilemap-2d`：绘制 2D 网格。
- `game-ai`：在空间里寻路的敌人；`camera-systems`：玩家能看到什么。

## 版本说明

最后验证：2026-11-11。

- Godot 4.7：`CSGShape3D` 文档指出 CSG 的 CPU 开销显著，只适合做原型；`bake_static_mesh()` 和 `bake_collision_shape()` 会把它转成静态资源（https://github.com/godotengine/godot/blob/4.7-stable/modules/csg/doc_classes/CSGShape3D.xml）。
- 跳跃测量、节奏检查和可达性检查均在 Godot 4.7.2 无头模式下运行。
