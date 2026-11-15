> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/unity/unity-animation/references/blend-trees-and-ik.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 混合树、动画层与人形 IK（Unity 6.3 LTS）

`unity-animation` 的深度参考。内容已对照 Unity 手册的 Animation 章节与
`ScriptReference/Animator` 核实。

## 混合树

混合树（Blend Tree）用一个或两个 `Float` 参数混合多个剪辑，让连续运动
（待机 → 行走 → 跑步，或 8 方向移动）只占一个节点，而不是一串状态。

- **1D**：单一参数（如 `Speed`）。把剪辑沿轴摆放（0 待机、2 行走、6 跑步），
  树按参数当前所在的位置做交叉淡入淡出。
- **2D Simple Directional**：剪辑位于互不相同的方向（前、后、侧移）。
- **2D Freeform Directional / Cartesian**：剪辑在二维平面上任意摆放
  （`MoveX`、`MoveY`）；Freeform Cartesian 适合非方向性的参数对（速度 × 转向）。

在脚本里驱动它，和驱动任何 float 参数完全一样，最好加阻尼：

```csharp
_anim.SetFloat("Speed", speed, 0.1f, Time.deltaTime);   // dampTime smooths the blend
_anim.SetFloat("MoveX", moveX);
_anim.SetFloat("MoveY", moveY);
```

提示：让混合阈值与各剪辑的真实根运动速度匹配，脚才不会滑步。

## 动画层 + Avatar 遮罩

动画层让上半身动作（瞄准、投掷）叠加在基础移动层之上播放。

- 每个层有**权重**（0–1）和**混合模式**：`Override`（替换）或 `Additive`
  （在基础姿势之上叠加）。
- **Avatar 遮罩**把层限制到选定的骨骼（如脊柱 + 手臂），这样手臂瞄准时
  双腿仍在行走。

```csharp
int aimLayer = _anim.GetLayerIndex("UpperBody");
_anim.SetLayerWeight(aimLayer, isAiming ? 1f : 0f);   // fade the layer in/out
```

## 人形 IK（`OnAnimatorIK`）

IK 在动画姿势采样*之后*，把手/脚/视线调整到目标。前提条件：
Humanoid Avatar，并在该层启用 **IK Pass**。

```csharp
[SerializeField] private Transform lookTarget, rightHandTarget;

// Called by the Animator once per frame, per layer, when IK Pass is on.
private void OnAnimatorIK(int layerIndex)
{
    if (lookTarget)
    {
        _anim.SetLookAtWeight(1f);                 // overall look-at weight
        _anim.SetLookAtPosition(lookTarget.position);
    }
    if (rightHandTarget)
    {
        _anim.SetIKPositionWeight(AvatarIKGoal.RightHand, 1f);   // 0..1 blend toward target
        _anim.SetIKRotationWeight(AvatarIKGoal.RightHand, 1f);
        _anim.SetIKPosition(AvatarIKGoal.RightHand, rightHandTarget.position);
        _anim.SetIKRotation(AvatarIKGoal.RightHand, rightHandTarget.rotation);
    }
}
```

`AvatarIKGoal` 的取值：`LeftFoot`、`RightFoot`、`LeftHand`、`RightHand`。把权重重新
调向 0，即可平滑释放 IK。

### 斜坡地面上的脚部 IK

- 在移动状态上启用 **Foot IK**。
- 对每只脚向下做射线检测（Raycast），再用 `SetIKPosition`/`SetIKRotation` 对齐到
  表面点与法线，让脚踩实斜坡，而不是穿模或悬空。

## 常见坑

- 在 `OnAnimatorIK` 之外调用 IK 会被忽略。
- `SetLookAtWeight` 还有身体/头部/眼睛/角度限制等额外参数，单参数重载
  就是常见情形的快捷写法。
- 层权重和 IK 权重不会自动归零；解除时要把它们 lerp 回 0，否则姿势会一直卡住。
- Additive 层叠加的是每个剪辑相对其参考姿势的差值；除非在剪辑导入设置中
  启用 **Additive Reference Pose**，参考姿势就是剪辑的第一帧。若那一帧不是
  中性姿势，整个层都会带偏移；请选一个中性帧。
