---
name: unreal-cpp-gameplay
description: >
  编写 Unreal Engine 5 的 C++ gameplay 代码：UCLASS/UPROPERTY/UFUNCTION 反射宏、
  Gameplay 框架（GameMode、Pawn、Character、PlayerController、Actor 组件），以及模块的
  Build.cs。适用于编写或调试 UE C++、从 AActor/ACharacter/AGameModeBase 派生、把属性暴露给
  编辑器或 Blueprints，或用户提到 Unreal C++、UCLASS、GENERATED_BODY、GameMode、ACharacter、
  .Build.cs 时使用。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/unreal/unreal-cpp-gameplay/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Unreal C++ Gameplay

编写正确的 UE5 gameplay C++：把 C++ 连接到编辑器和 Blueprints 的反射宏、Gameplay 框架的
类职责，以及模块依赖。目标版本为 **UE 5.8**。

## 何时使用

- 创建 C++ gameplay 类（`AActor`、`APawn`、`ACharacter`、`AGameModeBase`、
  `UActorComponent`）时；用 `UPROPERTY`/`UFUNCTION` 暴露属性/函数时；设置
  GameMode 的默认类时；或在 `*.Build.cs` 中添加模块依赖时使用。
- 项目有 `Source/` 目录树、其中 `*.h`/`*.cpp` 使用 `UCLASS`，以及 `*.Build.cs` 时使用。

**何时不使用：** 面向策划的可视化逻辑 → `unreal-blueprints`。玩家输入绑定细节 →
`unreal-enhanced-input`。AI 逻辑 → `unreal-behavior-trees`。本 Skill 只负责那些 Skill 所
依赖的 C++ 类/反射基础。

## 核心工作流

1. **用正确的前缀命名。** `A` = 派生自 Actor，`U` = 派生自 `UObject`/组件，`F` = 普通结构体，
   `E` = 枚举，`I` = 接口。前缀必须与基类匹配。
2. **用反射宏声明类。** 类定义上方写 `UCLASS()`，类体内第一行写
   `GENERATED_BODY()`，并在头文件中把 `#include "ClassName.generated.h"` 作为
   **最后一个** include。
3. **用 `UPROPERTY` 暴露数据**（同时承担编辑器/Blueprint 可见性*和*垃圾回收追踪），用
   `UFUNCTION` 暴露行为（`BlueprintCallable` 等）。
4. **在构造函数中创建组件**，使用 `CreateDefaultSubobject<T>(TEXT("Name"))` 并设置
   `RootComponent`。
5. **理解框架各角色：** `AGameModeBase` 制定规则 + 默认类；`APawn`/
   `ACharacter` 是可操控的躯体；`APlayerController` 是玩家的意志；
   `UActorComponent` 是可复用的行为。
6. **添加模块依赖**到 `*.Build.cs`（例如 `EnhancedInput`），否则随后会出现未解析符号的链接
   错误。
7. **验证：** 编译（编辑器内用 Live Coding `Ctrl+Alt+F11`，或关闭编辑器后
   从 IDE 完整构建），并确认类/属性出现在编辑器中。要跑自动化测试，以
   无头模式运行
   `UnrealEditor-Cmd <Project>.uproject -ExecCmds="Automation RunTest MyGame;Quit"`
   （`RunTest` 接受测试名、点号前缀，或 `Group:<name>`）。

## 模式

### 1. 最小化 Actor 类（头文件 + 源文件）

```cpp
// Pickup.h
#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Pickup.generated.h"          // MUST be the last include

UCLASS()
class MYGAME_API APickup : public AActor   // MYGAME_API = your module's export macro
{
    GENERATED_BODY()
public:
    APickup();

    // EditAnywhere = tweak per-instance & on the CDO; BlueprintReadWrite = BP get/set.
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Pickup")
    int32 ScoreValue = 10;

    // UPROPERTY on a UObject* pointer is what keeps it from being garbage-collected.
    UPROPERTY(VisibleAnywhere)
    TObjectPtr<UStaticMeshComponent> Mesh;   // UE5: TObjectPtr instead of raw UStaticMeshComponent*

    UFUNCTION(BlueprintCallable, Category = "Pickup")
    void Collect();

protected:
    virtual void BeginPlay() override;
};
```

```cpp
// Pickup.cpp
#include "Pickup.h"
#include "Components/StaticMeshComponent.h"

APickup::APickup()
{
    Mesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Mesh"));
    RootComponent = Mesh;                     // the mesh is this actor's root
}

void APickup::BeginPlay() { Super::BeginPlay(); }   // always call Super
void APickup::Collect()   { Destroy(); }
```

### 2. GameMode 接线其默认类

```cpp
// MyGameMode.cpp — set in the constructor so the engine spawns your classes.
AMyGameMode::AMyGameMode()
{
    DefaultPawnClass      = AMyCharacter::StaticClass();
    PlayerControllerClass = AMyPlayerController::StaticClass();
}
```

### 3. Build.cs 中的模块依赖

```csharp
// MyGame.Build.cs
PublicDependencyModuleNames.AddRange(new string[]
{
    "Core", "CoreUObject", "Engine", "InputCore", "EnhancedInput"
});
```

## 常见陷阱

- **`generated.h` 不是最后一个 include / 缺失** — 出现类似 "Cannot find generated header" 或
  "Expected an include" 的编译错误。它必须是头文件中最后一个 include。
- **忘记 `GENERATED_BODY()`** — UHT（Unreal Header Tool）报错；它必须是类体内的
  第一个内容。
- **裸 `UObject*` 指针没有 `UPROPERTY`** — 垃圾回收器看不到它，可能在你毫不知情时把它销毁。
  用 `UPROPERTY` 追踪每一个 UObject 指针（UE5 中使用 `TObjectPtr`）。
- **用 Live Coding 修改头文件/UPROPERTY** — 函数体修改是可靠的。结构性修改（新增函数、新增
  `UPROPERTY`）依赖 Object Reinstancing，它默认开启但稳定性较差；缓存了指向被重建对象指针的
  代码必须刷新这些指针。如果此类修改后编辑器或 Blueprints 行为异常，关闭编辑器并从 IDE 构建。
- **类前缀错误** — 把 Actor 命名为 `UFoo`（或把组件命名为 `AFoo`）会破坏 UHT；前缀必须与
  基类型匹配。
- **链接时 Unresolved external symbol** — 提供 API 的模块不在 `Build.cs` 的
  `PublicDependencyModuleNames` 里。
- **在重写的 `BeginPlay`/`Tick` 等函数中不调用 `Super::`** — 会跳过引擎的初始化设置。

## 参考资料

- 关于 `UActorComponent` 的创建/挂接、`UPROPERTY` 的垃圾回收所有权规则（`TObjectPtr`、
  `TArray<TObjectPtr<>>`、`TWeakObjectPtr`、在普通 C++ 类中持有 UObject），以及一份复制
  （replication）入门，请阅读
  `references/components-and-gc.md`。
- 主要文档："Unreal Engine CPP Quick Start" 与 "Gameplay Framework"
  （`https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine`）。

## 相关 Skill

- `unreal-blueprints` — 把 C++ 暴露给策划；BP/C++ 互操作。
- `unreal-enhanced-input` — 在 C++ Pawn/Character 中绑定输入。
- `unreal-behavior-trees` — 由行为树驱动的 C++ AI 任务。
