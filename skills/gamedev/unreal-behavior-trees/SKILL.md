---
name: unreal-behavior-trees
description: >
  使用行为树（Behavior Tree）与黑板（Blackboard）在 Unreal Engine 5 中构建 NPC AI：组合节点
  （Selector/Sequence）、任务（Task）、装饰器（Decorator）、服务（Service），以及从 AIController
  运行行为树。适用于创建敌人/NPC AI、BT_/BB_ 资产、自定义 BTTask 或 BTService 节点，或当用户
  提到 Behavior Tree、Blackboard、AIController、BTTask、decorator 或 service 时使用。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/unreal/unreal-behavior-trees/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Unreal 行为树

在 UE5 中使用由黑板（Blackboard）驱动的行为树（Behavior Tree）编写 NPC 的决策逻辑：
用组合节点（composite）组织树结构，用装饰器（Decorator）限制分支执行，用服务
（Service）保持状态最新，并从 AIController 运行行为树。
目标版本为 **UE 5.8**。

## 何时使用

- 适用于构建敌人/NPC AI：创建 `BT_`/`BB_` 资产对、组织 Selector/Sequence 分支、添加装饰器
  （条件）与服务（周期更新）、编写自定义 `BTTask`/`BTService` 节点，或将 AIController 接线
  以运行行为树。
- 适用于项目已有行为树（`BT_`）与黑板（`BB_`）资产以及
  `AAIController` 的情况。

**何时不适用：** 讨论 AI 的*概念*（FSM vs BT vs steering，跨引擎）→ `game-ai`。纯粹的导航/寻路
数学属于引擎 navmesh（BT 的 `MoveTo` 使用它）。简单的一次性逻辑用小型状态机可能比
完整的树更划算。

**Behavior Tree 还是 StateTree？** UE 5.8 同时提供两者，且 Behavior Trees 并未被弃用。
StateTree 是 Epic 的通用分层状态机：它把 BT 式的选择机制与显式的 States 和
Transitions 结合起来。如果项目已经在使用 StateTree 资产，或者该 AI 天然是一组
带明确转换的模式（巡逻 → 警戒 → 战斗），在旁边添加 Behavior Tree 之前请先与
用户确认。项目已有 `BT_`/`BB_` 资产的地方继续使用 Behavior Tree。

## 核心工作流

1. **创建资产对：** 黑板（`BB_`）持有类型化的键（AI 的记忆：`TargetActor`、
   `LastKnownLocation`、`bIsInvestigating`）；行为树（`BT_`）引用该黑板。
2. **Possess 并运行。** `AAIController` possess 该 pawn 并调用 `RunBehaviorTree(BT)`，
   这同时会初始化所引用的黑板。
3. **用组合节点组织结构。** **Selector** 从左到右运行子节点，直到某个子节点*成功*（优先级/回退：
   "attack, else chase, else patrol"）。**Sequence** 运行子节点直到某个*失败*（全部执行：
   "move to cover → reload → peek"）。**Simple Parallel** 让一个主任务与一个次要任务并行
   运行。
4. **用 Decorator 限制分支**，Decorator 读取黑板键（例如"Has Target?"守护战斗分支）。设置
   **Observer Aborts**，使键变化时树会重新求值。
5. **用 Service 保持黑板最新**，Service 挂载在分支上，仅在该分支激活期间周期性 tick
   （例如通过视野检查更新 `TargetActor`）。
6. **在 Task 中执行具体工作**，Task 返回 `Succeeded`、`Failed` 或 `InProgress`（潜伏
   （latent）任务如 `MoveTo` 稍后才完成）。
7. **验证** ， 在 PIE 期间使用行为树调试器，它会高亮正在运行的节点并显示实时的黑板值，让你
   准确看到哪个分支在执行。

## 模式

### 1. 运行行为树的 AIController（C++）

```cpp
void AEnemyAIController::OnPossess(APawn* InPawn)
{
    Super::OnPossess(InPawn);
    if (BehaviorTree)                 // UPROPERTY(EditAnywhere) TObjectPtr<UBehaviorTree>
        RunBehaviorTree(BehaviorTree); // initializes & uses the Blackboard the BT references
}
```

### 2. 一个优先级行为树（节点结构）

```text
ROOT
└── Selector (try combat, else investigate, else patrol)
    ├── Sequence            [Decorator: Blackboard 'TargetActor' Is Set, Observer Aborts: Both]
    │     ├── Task: MoveTo (TargetActor)          // latent: returns InProgress then Succeeded
    │     └── Task: Attack
    ├── Sequence            [Decorator: 'LastKnownLocation' Is Set]
    │     ├── Task: MoveTo (LastKnownLocation)
    │     └── Task: Wait (3s) + clear key
    └── Task: Patrol (BTTask_FindPatrolPoint -> MoveTo)
```

`Observer Aborts: Both` 让战斗分支在 `TargetActor` 被设置的瞬间打断巡逻，并在其被清除时立即
退出，这正是让 AI 显得反应灵敏的关键。

### 3. 从代码更新黑板（例如看到玩家时）

```cpp
void AEnemyAIController::SetTarget(AActor* Target)
{
    if (UBlackboardComponent* BB = GetBlackboardComponent())
        BB->SetValueAsObject(TEXT("TargetActor"), Target);   // key name must match the BB asset
}
// Clear with BB->ClearValue(TEXT("TargetActor")); to drop back to a lower-priority branch.
```

## 常见陷阱

- **AI 永远不启动** ， pawn 未被 possess（把 Pawn 的 *Auto Possess AI* 设为 "Placed in World
  or Spawned" 并指定 AIController），或从未调用 `RunBehaviorTree`。
- **`MoveTo` 立即失败** ， 关卡中没有 NavMesh（添加一个 Nav Mesh Bounds Volume），或目标
  不在 navmesh 上。
- **分支不响应变化** ， 门控 Decorator 的 **Observer Aborts** 被设为 None；把它设为
  Self/Lower Priority/Both，键变化时树才会重新求值。
- **一个任务把树卡住** ， 自定义任务返回了 `InProgress` 却从不调用 `FinishLatentTask`。
  务必让潜伏任务最终完成。
- **只有在多个 NPC 共用一棵树时 AI 行为才异常** ， 自定义任务把运行状态存在了成员变量里。
  除非实例化，任务节点会被所有使用该资产的 AI 共享；每个 AI 自己的状态应保存在节点内存
  （node memory）中（见参考部分）。
- **黑板键拼写错误** ， `SetValueAsObject("Taget", ...)` 会静默地什么都不做；键名和类型
  必须完全匹配，或使用缓存的 `FBlackboardKeySelector`。
- **Sequence 与 Selector 混淆** ， Sequence = AND（遇到第一个失败即停止）；Selector = OR
  （遇到第一个成功即停止）。两者互换会导致行为完全颠倒。

## 参考

- 关于**自定义 C++ `UBTTaskNode`**（即时与潜伏的 `ExecuteTask` 并返回 `EBTNodeResult`、
  每个 AI 的节点内存、`AbortTask`，以及 `FBlackboardKeySelector`），请阅读
  `references/custom-bttask.md`。
- 主文档："Behavior Trees in Unreal Engine"
  （`https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees-in-unreal-engine`）。

## 相关技能

- `game-ai` ， 跨引擎的 AI 设计（FSM、BT、steering、寻路选择）。
- `unreal-cpp-gameplay` ， C++ 中的 AIController 与 pawn 类。
- `fps-shooter` / `tower-defense` ， 组合敌人 AI 的游戏类型。
