---
name: unity-csharp-scripting
description: >
  编写 Unity 6.3 LTS C# 游戏玩法脚本：MonoBehaviour 生命周期
  （Awake/OnEnable/Start/Update/FixedUpdate/LateUpdate）、GameObject 与组件访问、
  协程（coroutine）、以及 Inspector 序列化。在 Unity 项目中创建或编辑 .cs 脚本时使用，
  或当用户提到 MonoBehaviour、Start/Update、GetComponent、SerializeField、coroutine
  或 "Unity script"（Unity 脚本）时使用。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/unity/unity-csharp-scripting/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Unity C# 脚本编写（MonoBehaviour）

在 Unity 6 中编写正确、符合惯例的游戏玩法脚本。把生命周期、组件访问、序列化和协程
都处理到位，让行为具有确定性，并让 Inspector 始终保持可用。目标版本为 **Unity 6.3 LTS
(6000.3)**、C# / .NET Standard 2.1。

## 何时使用

- 编写或修复 `MonoBehaviour` 时使用：选择正确的生命周期回调、读取/缓存组件、把字段
  暴露给 Inspector，或用协程执行按时序推进的逻辑。
- 当项目中存在 `*.cs` 文件、`Assembly-CSharp` 或 `*.asmdef`，以及 `ProjectSettings/`
  文件夹时使用。

**何时不使用：** 移动刚体 / 碰撞响应 → `unity-physics`；读取玩家输入 →
`unity-input-system`；共享数据资产 / 配置 → `unity-scriptableobjects`；Animator 参数 →
`unity-animation`。本 Skill 只负责*脚本生命周期与 C# 基础管道*，不涉及上述子系统。

## 核心工作流

1. **按用途而非习惯挑选回调。** `Awake`（缓存引用，加载时执行一次）、`OnEnable`
   （订阅事件）、`Start`（依赖其他对象的 `Awake` 的初始化）、`Update`（每帧逻辑/输入
   轮询）、`FixedUpdate`（物理）、`LateUpdate`（移动之后的相机跟随）、
   `OnDisable`/`OnDestroy`（取消订阅/清理）。
2. **在 `Awake` 中缓存组件查找结果** ， 绝不要每帧调用 `GetComponent`。
3. **用 `[SerializeField] private` 暴露可调参数**，而不是 public 字段，这样其他代码无法
   修改它们，但策划可以在 Inspector 中编辑。
4. **在 `Update` 中用 `Time.deltaTime` 对每帧数值进行缩放**（`Time.fixedDeltaTime` 的
   语义在 `FixedUpdate` 中是自动处理的）。
5. **按时序推进的逻辑使用协程**（延迟、补间动画、"先做 X，等待，再做 Y"）；用
   `StartCoroutine` 启动，并以确定性的方式停止。
6. **在 Play 模式下验证**：检查 Console 是否有空引用异常，确认 Inspector 中的数值按预期
   更新，如果 `Update` 是热点则在 Profiler 中观察。
7. **收尾前检查 `.meta` 文件。** 在 Editor 之外创建、移动、重命名或删除脚本与资产时，
   移动文件时务必连同其 `.meta` 一起移动（新的 `.meta` 意味着新的 GUID 和被破坏的
   引用）。然后运行
   `python scripts/check_unity_project.py <project-dir>`（`--json` 可输出机器可读结果），
   修复每一个 `ERROR`（GUID 重复或格式错误、文件移动时未带 `.meta`、缺失的脚本引用），
   并重新运行直到脚本以 0 退出。全新文件缺少 `.meta` 只会给出警告；Unity 会在下次导入时
   自动创建。以相对于本 Skill 目录的路径运行该脚本，或先解析出已安装 Skill 的路径。它
   只需要 Python 3.10+，别无其他依赖，只读取文本序列化的资产，并且不能替代在 Unity 中
   打开项目。

## 模式

### 1. 生命周期 + 缓存组件（标准骨架）

```csharp
using UnityEngine;

[RequireComponent(typeof(Rigidbody))]      // auto-adds the dependency, prevents null refs
public class PlayerController : MonoBehaviour
{
    [SerializeField] private float moveSpeed = 6f;   // editable in Inspector, private in code
    private Rigidbody _rb;                            // cached, not fetched per frame

    private void Awake() => _rb = GetComponent<Rigidbody>();  // cache once on load

    private void Update()
    {
        // Per-frame, non-physics work. Scale by deltaTime so it is frame-rate independent.
        transform.Rotate(0f, 90f * Time.deltaTime, 0f);
    }

    private void FixedUpdate()
    {
        // Physics work belongs here (fixed timestep). See the unity-physics skill.
        _rb.MovePosition(_rb.position + transform.forward * moveSpeed * Time.fixedDeltaTime);
    }
}
```

### 2. 用 `TryGetComponent` 做安全的组件访问

```csharp
// Avoids allocating a null and is clearer than GetComponent + null check.
if (other.TryGetComponent<Health>(out var health))
    health.Apply(-10);
```

### 3. 能在 Inspector 中正确显示的序列化

```csharp
[SerializeField, Range(0f, 1f)] private float volume = 0.8f;  // slider
[SerializeField] private string playerName = "Hero";          // private but serialized

[System.Serializable]                 // REQUIRED for a plain class to serialize/show
public class Stats { public int hp = 100; public int mana = 50; }

[SerializeField] private Stats stats = new();  // nested struct-like data in the Inspector
```

### 4. 用协程实现按时序推进的逻辑

```csharp
private void Start() => StartCoroutine(FlashThenHide());

private System.Collections.IEnumerator FlashThenHide()
{
    yield return new WaitForSeconds(0.5f);   // wait half a second of game time
    GetComponent<Renderer>().enabled = false;
    yield return null;                       // resume next frame
}
```

## 陷阱

- **在 `Update` 中调用 `GetComponent`** ， 它每一帧都会进行搜索，严重拖累性能。把引用
  缓存在 `Awake`/`Start` 中。
- **在 `Update` 中做物理** ， 在 `FixedUpdate` 之外用力或 `MovePosition` 移动
  `Rigidbody` 会导致抖动和依赖时间步长的行为。在 `Update` 中读取输入，在 `FixedUpdate`
  中应用物理。
- **依赖各对象之间 `Start` 的执行顺序** ， `Start` 在*所有* `Awake` 之后运行，但各
  `Start` 之间的顺序是不确定的。跨对象的接线放在 `Start` 中，自身初始化放在 `Awake` 中。
- **仅仅为了在 Inspector 中显示就使用 `public` 字段** ， 这同时也允许任何脚本修改它们。
  请改用 `[SerializeField] private`。
- **`gameObject.tag == "Enemy"`** 会分配字符串且更慢；请使用
  `gameObject.CompareTag("Enemy")`。
- **GameObject 被禁用时协程会停止** ， 被禁用对象的协程会被终止；如果协程必须经受住
  启停切换，就在 `OnEnable` 中重新 `StartCoroutine`。仅把脚本设为 `enabled = false`
  *并不会*停止它们。
- **`FindObjectOfType` / `FindObjectsOfType` 的过时警告** ， Unity 6 已替换它们。请使用
  `FindFirstObjectByType`（旧行为）、`FindAnyObjectByType`（更快，任意匹配）或
  `FindObjectsByType(FindObjectsSortMode.None)`；它们都很慢，所以要缓存结果。
- **`async` 方法在其对象被销毁后仍会继续运行** ， `await` 不像协程那样与 GameObject
  绑定。把 `destroyCancellationToken` 传给 `Awaitable` 等待方法（之后它们会抛出
  `OperationCanceledException`），并且绝不要对同一个 `Awaitable` 实例 await 两次：实例
  来自对象池。
- **`Update` 永远不会在 `Start` 之前运行，但*第一个* `Update` 可能与 `Start` 在同一帧
  运行** ， 如果你把初始化拆得比较古怪，就要防范尚未初始化的字段。

## 参考资料

- 完整的事件执行顺序表、进阶协程模式（自定义 `CustomYieldInstruction`、按句柄停止、
  `WaitUntil`/`WaitWhile`）以及协程等待对应的 `Awaitable` 等价物，请阅读
  `references/lifecycle-and-coroutines.md`。
- `scripts/check_unity_project.py` ， 只读的 `.meta`/GUID 与缺失脚本检查器；
  `--help` 列出全部检查项与退出码。
- 主要文档：Unity Manual 的 "Event function execution order"
  （`https://docs.unity3d.com/Manual/execution-order.html`）、`ScriptReference/MonoBehaviour`，
  以及 Manual 页面 "Asynchronous programming with the Awaitable class"。

## 相关 Skills

- `unity-physics` ， `Rigidbody`、碰撞与 `FixedUpdate` 中的运动。
- `unity-input-system` ， 把玩家输入读入这些脚本。
- `unity-scriptableobjects` ， 在脚本之间共享数据/配置，而无需单例。
