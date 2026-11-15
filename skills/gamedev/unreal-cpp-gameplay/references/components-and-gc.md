> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/unreal/unreal-cpp-gameplay/references/components-and-gc.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 组件、垃圾回收与网络复制入门（UE 5.8 C++）

本文是 `unreal-cpp-gameplay` 的深度参考。内容已对照 Gameplay Framework 文档与 UE5 C++ 编程参考核实。涵盖组件的创建与挂接、让新手栽跟头的 UPROPERTY/GC 所有权规则，以及一个最小的复制示例。

内容：
- 创建与挂接组件（构造函数 vs 运行时）
- 垃圾回收所有权（`UPROPERTY`、`TObjectPtr`、`TWeakObjectPtr`、`TStrongObjectPtr`、`FGCObject`）
- 用于反射数据的 USTRUCT 与 UENUM
- 最小复制示例（`ReplicatedUsing`、`DOREPLIFETIME`）
- 常见坑

## 创建与挂接组件

默认子对象在构造函数中创建；运行时组件使用 `NewObject` + `RegisterComponent`。

```cpp
// In the constructor — built into the Class Default Object, editable in the Blueprint subclass.
ACharacterBase::ACharacterBase()
{
    SpringArm = CreateDefaultSubobject<USpringArmComponent>(TEXT("SpringArm"));
    SpringArm->SetupAttachment(RootComponent);          // attach to an existing component
    SpringArm->TargetArmLength = 300.f;

    Camera = CreateDefaultSubobject<UCameraComponent>(TEXT("Camera"));
    Camera->SetupAttachment(SpringArm);                 // socket chain: root -> arm -> camera
}
```

```cpp
// At runtime (e.g. add a component after spawn):
UAudioComponent* Audio = NewObject<UAudioComponent>(this);
Audio->RegisterComponent();                              // required, or it won't tick/render
Audio->AttachToComponent(RootComponent, FAttachmentTransformRules::KeepRelativeTransform);
```

- `CreateDefaultSubobject` **只**能在构造函数中调用；之后再调用会触发断言。
- `SetupAttachment` 用于构造函数期搭建层级；`AttachToComponent` 是运行时调用的接口。

## 垃圾回收所有权（新手第一大崩溃来源）

UE 垃圾回收器只有通过反射引用触达 `UObject`，才会让它保持存活。不是 `UPROPERTY` 的裸 `UObject*` 成员对 GC 不可见，可能被回收，留下悬空指针。

```cpp
UPROPERTY()                                  // GC sees it -> stays alive while this owner lives
TObjectPtr<UMyDataObject> Data;

UPROPERTY()
TArray<TObjectPtr<AActor>> Tracked;          // containers of UObjects also need UPROPERTY

UMyDataObject* Raw;                           // BUG: not tracked; may be GC'd -> crash
```

规则：
- 每个必须长期存活的 `UObject`/Actor 指针都要加 `UPROPERTY`（UE5 中用 `TObjectPtr<T>`；裸指针仍能编译，但 `TObjectPtr` 在编辑器中额外提供访问追踪）。
- 普通 C++ 数据（int、FString、FVector、POD 类型的 USTRUCT）不需要这些，它们按值持有。
- 你自己创建的 UObject 若没有任何 UPROPERTY 持有者（少见情况），`AddToRoot()` 可将其固定，`RemoveFromRoot()` 解除固定；但更推荐规范的所有权。
- 普通 C++ 类（非 UObject）不能用 `UPROPERTY`。要在其中持有 UObject，用 `TStrongObjectPtr<T>`，或继承 `FGCObject` 并在 `AddReferencedObjects` 中上报引用（同时还需实现 `GetReferencerName`）。
- 对于不应让目标保持存活的引用（缓存的目标 Actor、监听器），用 `TWeakObjectPtr<T>`，并在每次使用前检查 `IsValid()`/`Get()`。

## 用于反射数据的 USTRUCT 与 UENUM

```cpp
UENUM(BlueprintType)
enum class EWeaponType : uint8 { Pistol, Rifle, Shotgun };

USTRUCT(BlueprintType)
struct FWeaponStats
{
    GENERATED_BODY()
    UPROPERTY(EditAnywhere, BlueprintReadWrite) int32 Damage = 10;
    UPROPERTY(EditAnywhere, BlueprintReadWrite) float FireRate = 0.25f;
};
```

`BlueprintType` 让枚举/结构体可以用作 Blueprint 变量。

## 最小复制示例（多人游戏）

```cpp
// Header
UPROPERTY(ReplicatedUsing = OnRep_Health)
float Health = 100.f;

UFUNCTION()
void OnRep_Health();                          // client callback when Health replicates

// Source
#include "Net/UnrealNetwork.h"
void AMyActor::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& Out) const
{
    Super::GetLifetimeReplicatedProps(Out);
    DOREPLIFETIME(AMyActor, Health);          // register the property for replication
}
```

- 在构造函数中设置 `bReplicates = true;`，Actor 才会进行复制。
- 服务器权威：玩法改动发生在服务器上；客户端接收复制过来的状态，并在 `OnRep_` 回调中做出反应。

## 常见坑

- `NewObject` 之后不调用 `RegisterComponent`，得到的组件虽然存在，但永不 tick、永不渲染。
- 忘了 `#include "Net/UnrealNetwork.h"` 会让 `DOREPLIFETIME` 报错。
- `TObjectPtr` 会隐式转换成裸指针参与调用，所以现有的 `->`/`.` 用法不变；差别在于 GC 可见性与编辑器工具支持，不在于调用处的语法。
