---
name: unreal-niagara
description: >
  Unreal Engine 5（UE 5.8）Niagara VFX：系统、发射器、User 参数、从 C++ 或
  蓝图生成、边界，以及 GPU 与 CPU 模拟。适用于任何 Unreal 粒子效果、NS_ 资源、
  枪口火焰或命中效果，以及不显示、在屏幕边缘消失或永不停止的效果。不适用于
  Unity VFX Graph、着色器编写（`shader-programming`）或命中停顿（`game-feel`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/unreal/unreal-niagara/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Unreal Niagara VFX

构建可由游戏逻辑生成、驱动和清理、且在摄像机实际朝向处持续渲染的 UE5 效果。
目标版本为 **UE 5.8**。Niagara 取代了已弃用的 Cascade。

## 何时使用

- 创建或编辑 Niagara Systems（`NS_`）和 Emitters（`NE_`）、模块顺序、User 参数、
  渲染器、边界与可扩展性。
- 从 C++ 或蓝图生成、附加、参数化、池化或停止效果。
- 调试不显示、错误剔除、泄漏或开销过高的效果。

**何时 *不* 使用：** Unity VFX Graph 或其他引擎中的粒子不在本文范围内。
材质与着色器逻辑 → `shader-programming`。屏幕震动、命中停顿之类的 Juice →
`game-feel`。效果的音频 → `audio-design`。

## 工作流程

1. **阅读项目。** 检查 `EngineAssociation`，列出现有 `NS_*`/`NE_*` 资源和
   发射器模板，并在 `Source` 中 grep `UNiagaraComponent`，找到当前已在使用的生成路径。
   C++ 访问需要在模块的 `*.Build.cs` 中加入 `"Niagara"`；否则 include 能编译通过，
   但链接会失败。
2. **将游戏逻辑要改动的内容暴露为 User 参数。** 只有 `User` 命名空间可以从蓝图或 C++ 设置；
   `System`、`Emitter` 和 `Particle` 的值是模拟内部使用的。
3. **有意安排模块顺序。** 各阶段内模块自上而下运行，因此放在初始化速度模块之前的力
   作用于零值。
4. **选择模拟目标。** 数量较少以及游戏逻辑会响应的对象（事件、碰撞回调）默认用 CPU；
   纯视觉粒子的大数量场景用 GPU，并为 GPU 发射器设置
   固定边界。
5. **从游戏逻辑生成，绝不要在 Construction Script 中生成。**
   世界空间的一次性效果用 `UNiagaraFunctionLibrary::SpawnSystemAtLocation`，
   跟随组件或插槽的效果用 `SpawnSystemAttached`。对于频繁的一次性效果
   （命中、脚步），传入池化方法，而不是每次都创建组件。
6. **掌控生命周期。** 一次性效果使用带自动销毁或自动释放的非循环系统；
   循环效果保留返回的组件，结束时调用 `Deactivate()`。
7. **检查（见「验证」）。**

## 常用模式

### 一次性命中效果（池化）与受驱动的循环效果


```cpp
#include "NiagaraFunctionLibrary.h"
#include "NiagaraComponent.h"

void AProjectile::SpawnImpact(const FVector& Location, const FRotator& Rotation)
{
    // ImpactSystem: UPROPERTY(EditAnywhere) TObjectPtr<UNiagaraSystem>, non-looping.
    UNiagaraFunctionLibrary::SpawnSystemAtLocation(
        GetWorld(), ImpactSystem, Location, Rotation, FVector(1.f),
        /*bAutoDestroy*/ true, /*bAutoActivate*/ true, ENCPoolMethod::AutoRelease);
    // With AutoRelease the component goes back to the pool when it finishes:
    // don't keep the returned pointer.
}

void ATorch::BeginPlay()
{
    Super::BeginPlay();
    Fire = UNiagaraFunctionLibrary::SpawnSystemAttached(   // Fire: UPROPERTY TObjectPtr<UNiagaraComponent>
        FireSystem, RootComponent, NAME_None, FVector::ZeroVector, FRotator::ZeroRotator,
        EAttachLocation::KeepRelativeOffset, /*bAutoDestroy*/ false);
    if (Fire)                                              // null on servers or when pre-culled
    {
        Fire->SetVariableFloat(TEXT("SpawnRate"), 250.f);  // the User.SpawnRate parameter
        Fire->SetVariableLinearColor(TEXT("FireColor"), FLinearColor::Red);
    }
}
```


蓝图使用相同的节点：Spawn System at Location 或 Spawn System Attached，然后在返回的组件上调用 Set
Niagara Variable（Float、LinearColor 等）。

## 验证

说明你运行了其中哪些项。

1. **编译**模块（`Build.bat`/`Build.sh`，做法见 `unreal-cpp-gameplay`）。
2. **校验资源：** `UnrealEditor-Cmd <Project>.uproject -run=DataValidation -unattended`，
   并修复改动过的系统中的错误。
3. **针对游戏逻辑生成效果的功能测试：** 在测试地图中生成系统，断言返回的组件有效且处于激活状态，
   然后（对一次性效果）断言其生命周期结束后已完成。Niagara 需要渲染器，因此用 `-RenderOffscreen`
   而非 `-nullrhi` 运行：
   `UnrealEditor-Cmd <Project>.uproject -ExecCmds="Automation RunTest Project.Functional Tests;Quit" -unattended -RenderOffscreen -ReportExportPath="<dir>"`。
4. **请用户**运行 PIE 并使用 Niagara Debugger（Tools > Debug > Niagara Debugger）
   或控制台：`fx.Niagara.Debug.Hud Enabled=1` 打开调试 HUD，`fx.Niagara.DumpComponents`
   在日志中列出存活组件，`stat Niagara` 查看开销。请他们反馈效果是否出现、
   原点离开屏幕时是否消失（边界），以及游玩一分钟后
   仍处于激活状态的组件数量（泄漏）。
5. **可选：** 安装后，Epic 的 `unreal-mcp` Skill 可在运行中的编辑器里编写和检查 Niagara 系统；
   上述检查并不依赖它。

## 常见陷阱

- **设置参数毫无效果：** 参数不在 `User` 命名空间中，或传给 `SetVariable*` 的名称
  与之不完全一致。
- **返回的组件导致崩溃：** 在没有系统资源、运行于专用服务器上，或可扩展性预剔除该效果时，
  生成函数会返回 `nullptr`。使用前先做空值检查。
- **效果在其原点离开屏幕时消失：** 边界过小，或从未计算动态边界。GPU 发射器需要
  在发射器或系统上设置固定边界。
- **循环效果永不停止或组件不断堆积：** 生成时关闭了自动销毁且从未停用，或本应
  为一次性效果的系统却是循环系统。
- **池化组件在你不知情时变化：** 使用 `AutoRelease` 时，池会在其完成后复用该组件。
  若必须持续驱动它，改用 `ManualRelease`（并自行释放）。
- **游戏逻辑无法读取粒子：** GPU 模拟数据不会回读到 CPU。游戏逻辑会响应的对象
  一律使用 CPU 发射器。
- **照搬 Cascade 教程：** 那是另一套系统。可用 Cascade To Niagara Converter Plugin
  迁移旧资源作为起点。
- **从 Construction Script 生成：** 生成函数在 Actor 构造期间被标记为不安全。
  请从 BeginPlay 或之后生成。
- **参数落错了位置：** `SpawnSystemAttached` 把 `PoolingMethod` 放在 `bAutoActivate` 之前，与
  `SpawnSystemAtLocation` 不同。传入可选参数前，先核对
  `NiagaraFunctionLibrary.h` 中的顺序。

## 参考资料

- Epic 文档：[Overview of Niagara Effects](https://dev.epicgames.com/documentation/unreal-engine/overview-of-niagara-effects-for-unreal-engine)，
  [Niagara Debugger](https://dev.epicgames.com/documentation/unreal-engine/niagara-debugger-for-unreal-engine)，
  [Console commands reference](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-console-commands-reference)。

## 相关 Skill

- `shader-programming`：粒子材质与着色器概念。
- `game-feel`：围绕效果的震动、命中停顿与时机。
- `unreal-cpp-gameplay`：模块配置以及生成效果的 Actor。
- `unreal-blueprints`：从图表触发效果。

## 版本说明

最后验证日期：2026-11-11。

- 当前版本：UE 5.8（5.8.4 热修复，2026 年 10 月）；UE 5.9 处于 Preview 阶段。
- 5.8：新增 Spawn By Trigger 模块、Random Jitter 与 Ramp In/Out 动态输入、面向少量粒子的 GPU bitonic
  sort，以及调试 HUD 命令的 `FiltersEnabled=` 选项。
- 5.9 Preview：Unreal Animation Framework 新增 Play Niagara Effect 通知处理器，
  AVBOIT 顺序无关透明改变了重叠半透明粒子的混合方式。
- 来源：[UE 5.8 release notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes)，
  [UE 5.9 Preview release notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-9-release-notes)，
  [Niagara Debugger](https://dev.epicgames.com/documentation/unreal-engine/niagara-debugger-for-unreal-engine)。
