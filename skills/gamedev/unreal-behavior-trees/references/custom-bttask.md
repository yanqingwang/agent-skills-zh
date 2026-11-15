> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/unreal/unreal-behavior-trees/references/custom-bttask.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 用 C++ 编写自定义 BTTask（UE 5.8）

`unreal-behavior-trees` 的深度参考：用 C++ 编写自定义行为树任务节点。已对照行为树文档与
`UBTTaskNode` API 验证。需要在 `*.Build.cs` 中添加 `AIModule` 依赖。

内容：
- 即时任务（立即返回）
- 潜在任务（随时间完成、每个 AI 独立的节点内存、`AbortTask`）
- 读写带类型的黑板值
- 注意事项：节点名称、Owner 访问、键选择器、自定义服务与装饰器

## 即时任务（立即返回）

```cpp
// BTTask_ClearTarget.h
#pragma once
#include "CoreMinimal.h"
#include "BehaviorTree/BTTaskNode.h"
#include "BTTask_ClearTarget.generated.h"

UCLASS()
class MYGAME_API UBTTask_ClearTarget : public UBTTaskNode
{
    GENERATED_BODY()
public:
    UBTTask_ClearTarget();
    virtual EBTNodeResult::Type ExecuteTask(UBehaviorTreeComponent& OwnerComp,
                                            uint8* NodeMemory) override;

    // Exposes a Blackboard key picker in the BT editor.
    UPROPERTY(EditAnywhere, Category = "Blackboard")
    FBlackboardKeySelector TargetKey;
};
```

```cpp
// BTTask_ClearTarget.cpp
#include "BTTask_ClearTarget.h"
#include "BehaviorTree/BlackboardComponent.h"

UBTTask_ClearTarget::UBTTask_ClearTarget()
{
    NodeName = "Clear Target";
}

EBTNodeResult::Type UBTTask_ClearTarget::ExecuteTask(UBehaviorTreeComponent& OwnerComp,
                                                     uint8* NodeMemory)
{
    if (UBlackboardComponent* BB = OwnerComp.GetBlackboardComponent())
    {
        BB->ClearValue(TargetKey.SelectedKeyName);
        return EBTNodeResult::Succeeded;     // done now
    }
    return EBTNodeResult::Failed;
}
```

`EBTNodeResult::Type` 的取值：`Succeeded`、`Failed`、`Aborted`、`InProgress`。

## 潜在任务（随时间完成）

先返回 `InProgress`，等工作完成（例如定时器、异步查询或委托回调）后再调用 `FinishLatentTask`。
任务默认**不做实例化**：所有运行该树的 AI 共享同一个节点对象，因此每次运行的状态（这里是定时器
句柄）必须放进节点的实例内存，绝不能放进成员变量。

```cpp
// BTTask_WaitRandom.h
#pragma once
#include "CoreMinimal.h"
#include "BehaviorTree/BTTaskNode.h"
#include "BTTask_WaitRandom.generated.h"

struct FBTWaitRandomMemory
{
    FTimerHandle TimerHandle;
};

UCLASS()
class MYGAME_API UBTTask_WaitRandom : public UBTTaskNode
{
    GENERATED_BODY()
public:
    virtual EBTNodeResult::Type ExecuteTask(UBehaviorTreeComponent& OwnerComp,
                                            uint8* NodeMemory) override;
    virtual EBTNodeResult::Type AbortTask(UBehaviorTreeComponent& OwnerComp,
                                          uint8* NodeMemory) override;

    virtual uint16 GetInstanceMemorySize() const override { return sizeof(FBTWaitRandomMemory); }
    virtual void InitializeMemory(UBehaviorTreeComponent& OwnerComp, uint8* NodeMemory,
                                  EBTMemoryInit::Type InitType) const override
    {
        InitializeNodeMemory<FBTWaitRandomMemory>(NodeMemory, InitType);
    }
    virtual void CleanupMemory(UBehaviorTreeComponent& OwnerComp, uint8* NodeMemory,
                               EBTMemoryClear::Type CleanupType) const override
    {
        CleanupNodeMemory<FBTWaitRandomMemory>(NodeMemory, CleanupType);
    }

    UPROPERTY(EditAnywhere, Category = "Wait") float MinTime = 1.f;
    UPROPERTY(EditAnywhere, Category = "Wait") float MaxTime = 3.f;
};
```

```cpp
// BTTask_WaitRandom.cpp
#include "BTTask_WaitRandom.h"
#include "BehaviorTree/BehaviorTreeComponent.h"
#include "TimerManager.h"

EBTNodeResult::Type UBTTask_WaitRandom::ExecuteTask(UBehaviorTreeComponent& OwnerComp,
                                                    uint8* NodeMemory)
{
    UWorld* World = OwnerComp.GetWorld();
    if (!World) return EBTNodeResult::Failed;

    FBTWaitRandomMemory* Memory = CastInstanceNodeMemory<FBTWaitRandomMemory>(NodeMemory);
    const float Delay = FMath::FRandRange(MinTime, MaxTime);

    // Weak pointer: the component can be destroyed before the timer fires.
    TWeakObjectPtr<UBehaviorTreeComponent> WeakComp(&OwnerComp);
    World->GetTimerManager().SetTimer(Memory->TimerHandle,
        FTimerDelegate::CreateWeakLambda(this, [this, WeakComp]()
        {
            if (UBehaviorTreeComponent* Comp = WeakComp.Get())
            {
                FinishLatentTask(*Comp, EBTNodeResult::Succeeded);   // resumes the tree
            }
        }), Delay, /*bLoop*/ false);

    return EBTNodeResult::InProgress;        // tree waits on this node until FinishLatentTask
}

EBTNodeResult::Type UBTTask_WaitRandom::AbortTask(UBehaviorTreeComponent& OwnerComp,
                                                  uint8* NodeMemory)
{
    // A higher-priority branch took over: cancel the pending timer so it can't finish later.
    if (UWorld* World = OwnerComp.GetWorld())
    {
        World->GetTimerManager().ClearTimer(
            CastInstanceNodeMemory<FBTWaitRandomMemory>(NodeMemory)->TimerHandle);
    }
    return EBTNodeResult::Aborted;
}
```

`AbortTask` 能立即停止时返回 `Aborted`；如果取消本身就是异步操作，则改为返回 `InProgress`，
稍后再调用 `FinishLatentAbort(OwnerComp)`。

## 读写带类型的黑板值

```cpp
UBlackboardComponent* BB = OwnerComp.GetBlackboardComponent();
AActor* Target  = Cast<AActor>(BB->GetValueAsObject(TargetKey.SelectedKeyName));
FVector Loc     = BB->GetValueAsVector(TEXT("LastKnownLocation"));
BB->SetValueAsBool(TEXT("bIsInvestigating"), true);
```

## 注意事项

- 在构造函数中设置 `NodeName`，让节点在行为树图表中含义清晰。
- `OwnerComp.GetAIOwner()` 返回 `AAIController`；`GetAIOwner()->GetPawn()` 返回被控制的 Pawn。
  请用这两个接口，不要缓存世界指针。
- 需要每实例内存（计数器、句柄）的节点：重写 `GetInstanceMemorySize`，用 `InitializeNodeMemory<T>` /
  `CleanupNodeMemory<T>` 构造与销毁内存块，并用 `CastInstanceNodeMemory<T>` 读取（见上面的潜在任务
  示例）。非实例化节点上的成员 UPROPERTY 被所有使用处共享；请把它们当作只读配置项。
- 裸用的 `FBlackboardKeySelector` 会在编辑器里提供所有键，且在解析完成前只有 `SelectedKeyName` 可用。
  继承 `UBTTask_BlackboardBase` 会得到一个在 `InitializeFromAsset` 中解析好的 `BlackboardKey`；若用
  自定义选择器，请在构造函数里添加类型过滤（例如 `AddObjectFilter`），并在 `InitializeFromAsset` 中
  调用 `ResolveSelectedKey`。
- 自定义**服务**继承 `UBTService` 并重写 `TickNode`；自定义**装饰器**继承 `UBTDecorator` 并重写
  `CalculateRawConditionValue`。
