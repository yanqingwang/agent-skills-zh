> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/unity/unity-csharp-scripting/references/lifecycle-and-coroutines.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# MonoBehaviour 生命周期与协程（Unity 6.3 LTS）

本文件是 `unity-csharp-scripting` skill 的深度参考：完整的执行顺序，以及放不进主手册的那些协程模式。内容已对照 Unity 手册的"Event function execution order"页面与 `ScriptReference/MonoBehaviour` 核实。

## 目录

- 执行顺序
- 协程 yield 指令
- 用 `Awaitable`（async/await）替代协程
- 自定义 yield 指令
- 常见陷阱

## 执行顺序（对玩法重要的部分）

对每个对象，引擎按以下顺序调用这些回调：

| 阶段 | 回调 | 运行时机 | 用途 |
|-------|----------|------|---------|
| 加载 | `Awake` | 一次，对象加载时调用（脚本组件被禁用也会调用，但 GameObject 未激活时不会） | 缓存 `GetComponent` 结果，初始化自身 |
| 启用 | `OnEnable` | 对象/脚本每次启用时 | 订阅事件，重新启动协程 |
| 初始化 | `Start` | 一次，在首次 `Update` 之前、所有 `Awake` 之后 | 依赖其他对象的接线 |
| 物理 | `FixedUpdate` | 每个固定步长（默认 0.02s） | 刚体受力，`MovePosition` |
| 物理 | `OnTriggerXXX` / `OnCollisionXXX` | 在物理步期间 | 碰撞/触发器响应 |
| 帧 | `Update` | 每个渲染帧一次 | 输入轮询，非物理逻辑 |
| 帧 | `LateUpdate` | 每帧一次，在所有 `Update` 之后 | 相机跟随，IK 修正 |
| 禁用 | `OnDisable` | 对象/脚本每次禁用时 | 取消事件订阅 |
| 销毁 | `OnDestroy` | 一次，销毁时 | 释放原生句柄，保存数据 |

关键影响：

- 取决于帧率，`FixedUpdate` 每帧可能运行零次、一次或多次。绝不要在那里读取"每帧"原始输入：在 `Update` 中读取，在 `FixedUpdate` 中使用。
- 所有 `Awake` 都会在任何 `Start` 之前完成。除非你在 Project Settings 中设置了 Script Execution Order，否则多个 `Awake` 之间（以及多个 `Start` 之间）的先后顺序是不确定的。
- 首次启用时 `OnEnable` 在 `Awake` 之后运行，之后每次重新启用都会再次运行。`OnEnable` 中的每个订阅都要配上 `OnDisable` 中的取消订阅，避免出现重复的事件处理器。

## 协程 yield 指令

```csharp
yield return null;                          // resume at the start of the next frame
yield return new WaitForSeconds(2f);        // wait 2s of scaled game time (affected by Time.timeScale)
yield return new WaitForSecondsRealtime(2f);// wait 2s of real time (ignores timeScale; good for pause menus)
yield return new WaitForFixedUpdate();      // resume after the next physics step
yield return new WaitUntil(() => isReady);  // resume once the predicate is true
yield return new WaitWhile(() => isLoading);// resume once the predicate is false
yield return StartCoroutine(OtherRoutine());// run a nested coroutine to completion first
```

## 用 `Awaitable`（async/await）替代协程

Unity 6 自带 `UnityEngine.Awaitable`，一个面向 `async` 方法的低分配开销 awaitable。协程的等待方式与它一一对应：

| 协程 | `Awaitable` |
|-----------|-------------|
| `yield return null` | `await Awaitable.NextFrameAsync()` |
| `yield return new WaitForSeconds(t)` | `await Awaitable.WaitForSecondsAsync(t)` |
| `yield return new WaitForFixedUpdate()` | `await Awaitable.FixedUpdateAsync()` |
| `yield return new WaitForEndOfFrame()` | `await Awaitable.EndOfFrameAsync()` |
| （无对应项） | `await Awaitable.BackgroundThreadAsync()` / `MainThreadAsync()` |

```csharp
using System;
using UnityEngine;

public class Blinker : MonoBehaviour
{
    [SerializeField] private Renderer target;

    private async void Start()
    {
        try
        {
            while (true)
            {
                target.enabled = !target.enabled;
                // The token cancels the wait when this component is destroyed.
                await Awaitable.WaitForSecondsAsync(0.5f, destroyCancellationToken);
            }
        }
        catch (OperationCanceledException) { /* destroyed: stop quietly */ }
    }
}
```

与协程不同的规则：

- 对象被禁用或销毁时，async 方法**不会**停止。请传入 `destroyCancellationToken`（在对象销毁前读取它），或在每次 `await` 后检查状态。
- `Awaitable` 实例是池化对象：每个实例只能 await **一次**。要两次等待同一结果，请保存结果本身，而不是保存 `Awaitable`。
- `BackgroundThreadAsync` 之后，在 `await Awaitable.MainThreadAsync()` 之前，大多数 Unity API 都不可用。退出 Play 模式不会停止后台工作；要停止它，请使用 `Application.exitCancellationToken`。
- 自己调用的方法优先用 `async Awaitable` 而不是 `async void`，这样调用方才能 await 它们；`async void` 只保留给 `Start` 这类 Unity 消息。

## 自定义 yield 指令

当你需要一个可复用的等待条件时：

```csharp
public class WaitForAnimationEnd : CustomYieldInstruction
{
    private readonly Animator _a;
    private readonly int _layer;
    public WaitForAnimationEnd(Animator a, int layer = 0) { _a = a; _layer = layer; }
    // keepWaiting == true means "keep yielding"; false resumes the coroutine.
    public override bool keepWaiting => _a.GetCurrentAnimatorStateInfo(_layer).normalizedTime < 1f;
}
```

## 常见陷阱

- GameObject 被**停用**（`SetActive(false)`）或脚本被销毁时，协程会被终止；但如果对象保持激活、仅脚本组件被禁用，协程*不会*终止。需要时在 `OnEnable` 中重新启动。
- 每次循环迭代都分配 `new WaitForSeconds(x)` 会产生垃圾；请缓存该实例。
