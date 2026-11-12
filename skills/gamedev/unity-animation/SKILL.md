---
name: unity-animation
description: >
  使用 Animator（Mecanim）实现 Unity 6.3 LTS 角色动画：状态与过渡、混合树、Avatar Mask 层、
  根运动与人形 IK。适用于 SetTrigger 接线、过渡延迟或从不触发、根运动打滑，或上半身层覆盖腿部的情况。
  不适用于 AI 状态机（`game-ai`）、打击感（`game-feel`）或 Godot（`godot-animation`）。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/unity/unity-animation/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Unity 动画（Animator / Mecanim）

在 Unity 6.3 LTS（6000.3）中用 `Animator` 与 Animator Controller 控制动画状态：参数、过渡、混合树、层与人形 IK。`.controller` 文件是文本形式的 YAML，因此无需打开 Editor 即可读取其中的参数与状态，也可以用编辑器代码来构建它，而不必依赖 Animator 窗口。

## 何时使用

- 把动画片段接入状态机、用脚本驱动它、混合移动（idle、walk、run）、在移动之上叠加上半身动作、脚部或手部 IK。
- 项目包含 `*.controller` 与 `*.anim` 资源，或带有 Avatar 的绑定骨骼模型。

**不适用场合：** 简单的数值补间（UI 淡入淡出、位置 lerp）→ `unity-csharp-scripting` 中的协程；NPC 应当攻击或逃跑时 → `game-ai`；Timeline 过场动画此处没有对应 Skill。2D 精灵逐帧动画使用同一个 Animator，只是关键帧针对精灵。

## 工作流

1. **写代码前先读控制器。** 在 `.controller` YAML 中，`m_AnimatorParameters` 列出每个参数的 `m_Name` 与 `m_Type`（1 为 Float、3 为 Int、4 为 Bool、9 为 Trigger），每个 `AnimatorState` 文档都有各自的 `m_Name`。脚本里的字符串必须与它们完全一致。
2. **设置骨架。** 人形 IK 与重定向要求模型以 Humanoid 方式导入（在模型的 `.meta` 中为 `animationType: 3`）；改动模型骨架前先征询，因为这会重建 Avatar。
3. **用参数驱动移动**（`SetFloat`、`SetBool`、`SetInteger`、`SetTrigger`），经由缓存的 `Animator.StringToHash` id 传入，让过渡自行判定。只有刻意的脚本切换（如受击反应）才用 `CrossFadeInFixedTime`。
4. **用混合树混合连续动作**，由一个 `Float`（2D 方向型则用两个）驱动，而不是堆大量状态与过渡。
5. **用 Avatar Mask 与 `SetLayerWeight` 叠加上半身动作层**。
6. **在无法使用 Editor 界面时用代码创建或修改控制器**（模式 3），随后重新读取 YAML 确认。
7. **验证**：按下方检查项执行。

## 模式

### 1. 用缓存的哈希值从脚本传入参数

```csharp
using UnityEngine;

[RequireComponent(typeof(Animator))]
public class CharacterAnim : MonoBehaviour
{
    private static readonly int Speed = Animator.StringToHash("Speed");
    private static readonly int IsGrounded = Animator.StringToHash("IsGrounded");
    private static readonly int Jump = Animator.StringToHash("Jump");
    private Animator _anim;

    private void Awake() => _anim = GetComponent<Animator>();

    public void Tick(float planarSpeed, bool grounded)
    {
        _anim.SetFloat(Speed, planarSpeed, 0.1f, Time.deltaTime);  // damped: no snapping
        _anim.SetBool(IsGrounded, grounded);
    }

    public void DoJump() => _anim.SetTrigger(Jump);   // consumed by the next matching transition
}
```

### 2. 等待刚触发的状态

```csharp
private System.Collections.IEnumerator AfterAttack()
{
    yield return null;   // let the Animator start the transition
    // During a transition the current state is the one being left; read the next one.
    AnimatorStateInfo info = _anim.IsInTransition(0)
        ? _anim.GetNextAnimatorStateInfo(0)
        : _anim.GetCurrentAnimatorStateInfo(0);
    yield return new WaitForSeconds(info.length);   // approximate inside blend trees
}
```

### 3. 用编辑器代码构建控制器

把它放进 `Editor` 文件夹。可以通过菜单项运行，用 Unity CLI 执行 `unity command script eval --code 'BuildLocomotionController.Build();'`，或在批处理模式下用 `-executeMethod BuildLocomotionController.Build`。

```csharp
using UnityEditor;
using UnityEditor.Animations;
using UnityEngine;

public static class BuildLocomotionController
{
    [MenuItem("Tools/Build Locomotion Controller")]
    public static void Build()
    {
        if (!AssetDatabase.IsValidFolder("Assets/Animation"))
            AssetDatabase.CreateFolder("Assets", "Animation");

        var controller = AnimatorController.CreateAnimatorControllerAtPath("Assets/Animation/Player.controller");
        controller.AddParameter("Speed", AnimatorControllerParameterType.Float);
        controller.AddParameter("Jump", AnimatorControllerParameterType.Trigger);

        AnimatorStateMachine sm = controller.layers[0].stateMachine;
        AnimatorState locomotion = sm.AddState("Locomotion");   // assign a clip or blend tree as its motion
        AnimatorState jump = sm.AddState("Jump");
        sm.defaultState = locomotion;

        AnimatorStateTransition toJump = locomotion.AddTransition(jump);
        toJump.hasExitTime = false;   // react to the trigger at once
        toJump.duration = 0.1f;
        toJump.AddCondition(AnimatorConditionMode.If, 0f, "Jump");

        AnimatorStateTransition back = jump.AddTransition(locomotion);
        back.hasExitTime = true;      // return when the jump clip nearly ends
        back.exitTime = 0.9f;

        AssetDatabase.SaveAssets();
    }
}
```

## 验证

- **无需 Editor：** 在 `.controller` 中检索 `m_AnimatorParameters` 与状态名，并与脚本里的每个字符串或 `StringToHash` 参数逐一比对。拼错在运行时不会有任何反应，因此这一步能顺手抓出最常见的 bug。
- **具备可用 Editor 的 Unity CLI：** `unity command animation.animator get_controller` 可读取控制器的完整结构（用 `--help` 查看其参数）。在 Play 模式下读取实时状态：`unity command script eval --code 'var a = GameObject.Find("Player").GetComponent<Animator>(); return a.GetCurrentAnimatorStateInfo(0).IsName("Locomotion") + " speed=" + a.GetFloat("Speed");'`
- **没有 CLI：** PlayMode 测试可以实例化角色 prefab、设置一个参数、等待若干帧，再断言 `GetCurrentAnimatorStateInfo(0).IsName(...)`；测试搭建见 `unity-csharp-scripting`。
- **视觉质量**（脚部打滑、跳变）：请用户在 Play 模式下观察 Animator 窗口，反馈触发了哪条过渡以及双脚是否打滑。

## 注意事项

- **Trigger 触发偏晚或"卡住"。** trigger 在被某条过渡消费前会一直保持置位。如果当前没有过渡能消费它，它会在之后某个意外的时刻才触发。时机过后调用 `ResetTrigger`，或对持续状态改用 `Bool`。
- **参数名拼错不会有任何效果。** 不会抛出异常。缓存哈希值并与控制器 YAML 比对（见验证）。
- **过渡感觉迟滞。** `Has Exit Time` 会等片段播放到其退出时间。对由条件驱动的过渡（跳跃、受击）应把它关掉。
- **角色打滑或无法移动。** `Apply Root Motion` 开启的同时代码也在移动 Transform，或者反过来。每个角色二选一：根运动或脚本移动。
- **上半身层覆盖了整个身体。** 指定 Avatar Mask，选择 Override 或 Additive，并设置层权重。
- **`CrossFade` 耗时远超预期。** 它的时长是按状态长度归一化的。`CrossFadeInFixedTime` 才以秒为单位。
- **IK 不起作用。** IK 只在 `OnAnimatorIK` 内生效，需要该层启用 IK Pass，并且需要 Humanoid Avatar。
- **重新启用的角色会重头播放动画。** 停用 GameObject 会重置它的 Animator；再次启用时会以默认参数从默认状态重新开始。不希望如此时设置 `animator.keepAnimatorStateOnDisable = true`，或者在从对象池取出对象时自行重置参数。

## 参考资料

- 在搭建 1D 或 2D 混合树、带 Avatar Mask 的层、人形 IK（`OnAnimatorIK`、注视、脚部 IK）或叠加式参考姿势时，阅读 `references/blend-trees-and-ik.md`。

## 相关 Skill

- `unity-csharp-scripting`：上文用到的 MonoBehaviour 与协同时序，以及测试。
- `unity-physics`：移动动画所呈现的身体。
- `game-ai`：决定何时播放哪个状态。

## 版本说明

最后验证时间：2026-11-11，基于 Unity 6000.3.28f1。

- `AnimatorControllerParameterType` 的取值（Float 1、Int 3、Bool 4、Trigger 9）与模式 3 中的编辑器 API（`CreateAnimatorControllerAtPath`、`AddParameter`、`AddState`、`AddTransition`、`AddCondition`、`hasExitTime`、`exitTime`、`duration`）、模型 `.meta` 的 `animationType` 取值（Human 为 3）以及 `Animator.keepAnimatorStateOnDisable`，均在标签 6000.3.28f1 的 Unity C# 参考源码中核对过（`Modules/Animation/ScriptBindings/`、`Editor/Mono/Animation/`、`Editor/Mono/StateMachine.bindings.cs`）。
- `animation.animator get_controller` 是 `com.unity.pipeline` 1.0.0-pre.1 的命令（预发布版）：https://docs.unity3d.com/Packages/com.unity.pipeline@1.0/manual/index.html
- 手册：https://docs.unity.com/en-us/engine/6000.3/manual 与 Scripting API `Animator`。
