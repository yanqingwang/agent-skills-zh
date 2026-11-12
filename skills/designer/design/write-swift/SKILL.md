---
name: write-swift
description: 如何把现代 Swift 写好：用值类型建模，Swift 6 数据竞争安全与易用并发（@concurrent、main-actor-by-default、actor、task group），协议与泛型（some 与 any），API 设计，性能与 ARC，Swift Testing，宏，以及 Agent 还不了解的现代语言特性。Use when：编写、审查或迁移 Swift 时；或需要修复并发错误、卡死（hang）、数据竞争（data race）、循环引用（retain cycle）或性能问题时。
---

> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/write-swift/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 写好 Swift

## 初始响应

当这个 skill 在没有具体问题的情况下首次被调用时，只回应：

> 我已准备好帮你写现代 Swift，按这门语言想要被书写的方式来写。

在用户提问之前，不要提供任何其他信息。

如何按这门语言想要被书写的方式来写 Swift，内容更新至 Swift 6.4。

**工具链基线：Swift 6.3**（截至 2026 年 8 月的当前发布版本）。除标注 ⚠ 的内容外，本文所有代码都可在 6.3 上编译；⚠ 标记尚未发布的 Swift 6.4 特性。并发指南基于 Swift 6.2 模型：如果项目还在 6.1 或更早，§3 中关于 `async` 和 `@concurrent` 的规则不适用。

贯穿全文的主线：**Swift 是一门渐进式披露的语言。从最简单、最静态、最单线程的可行方案起步，只有在能说出理由的地方才引入动态性：并发、引用语义、存在类型（existential）、不安全指针。**下面的每条规则都是这一主线的应用。

把这张默认层级表当作模型。只有在能说出理由时才降一级：

| 需求         | 首选                    | 仅在此情况下降级                                           |
| ------------ | ----------------------- | ---------------------------------------------------------- |
| 数据         | `struct` / `enum`       | 需要身份、共享或继承时                                     |
| 抽象         | 具体类型                | 多个类型出现重复代码时                                     |
| 多态         | `some P`（泛型）        | 需要异构存储 → `any P`                                     |
| 执行         | 主 actor、同步          | 性能分析显示卡死 → `async` → `@concurrent` → `actor`       |
| 内存         | `Array`、`String`       | 性能分析显示开销 → `InlineArray`、`Span`                   |
| 安全         | 安全 API                | C 互操作或实测热点路径 → `Unsafe*`                         |

---

## 1. 用值类型建模

值类型是 Swift 的默认，不是特例。

- **默认用 `struct` 和 `enum`。只在需要身份、共享可变状态、继承或资源生命周期时才用 `class`。**窗口、数据库连接、渲染引擎中的实体有身份；`Point`、`Drink`、`Material` 没有。
- **默认 `let`；只在会修改时用 `var`。**这与 `some` 优先于 `any`、值优先于引用是同一条纪律：从窄处起步，有理由再放宽。
- **带可变引用类型属性的 struct 既不是值也不是引用。**副本共享同一个对象，修改会跨副本泄漏。要么让被引用的类型不可变，要么只暴露转发到它的计算属性，要么把它做成写时复制（copy-on-write）背后的 `private` 存储属性。
- **写时复制让你同时获得外部存储 _和_ 值语义。**用 struct 包住 final class，修改前检查 `isKnownUniquelyReferenced(&storage)`；不是唯一引用就先复制。`Array`、`String`、`Dictionary` 正是这么实现的。
- **枚举适合"固定的一组东西"和互斥状态。**把一堆可选存储属性（`isSharing`、`selectedRows`、`shareTarget`）换成一个 `enum State`，非法组合就变得无法表示，状态变更变成原子操作，而不是一串你可能忘了写完的属性赋值。
- **值组合起来还是值。**存储属性全为值类型的 struct 免费获得值语义，这正是撤销、diff 和状态恢复能用一条代码路径实现（而不是每个属性一条）的原因。

```swift
struct Material {                       // value semantics preserved
  var roughness: Double
  private var _texture: Texture         // a class

  var color: Color {
    get { _texture.color }
    set {
      if !isKnownUniquelyReferenced(&_texture) { _texture = Texture(copying: _texture) }
      _texture.color = newValue
    }
  }
}
```

**不可复制类型**（`~Copyable`）表达唯一所有权：文件描述符、银行转账、已打开的资源。禁止复制把"你不能运行两次"从断言变成编译错误，也让 struct 上的 `deinit` 有了意义。把终结方法标成 `consuming`，编译器就能证明它是最后一次使用。参数所有权随之显式化：`borrowing`（只读，默认）、`consuming`（拿走所有权）、`inout`/`mutating`（临时写权限）。

---

## 2. 错误与可选值：让失败路径可见

Swift 的错误处理建立在三点上：错误来源有标记，不会突然冒出来；错误携带足以采取行动的上下文；**可恢复的错误不同于程序员的失误**。

- **可恢复 → `throw`。程序员失误 → `precondition`/`fatalError`。**网络请求失败，程序继续运行。数组越界意味着代码写错了，必须在 bug 变成安全问题之前停机。
- **带关联值的枚举是最好的错误类型。**`case duplicateFriend(String)` 优于 `case duplicateFriend`——上下文才是关键。
- **错误条件用 `guard`**，因为它强制走退出路径。普通解包用 `if let`。
- **类型化 throws（`throws(MyError)`）用于内部函数、转发错误的泛型代码，以及装箱 `any Error` 代价过高的受限环境。**对公共 API，非类型化 `throws` 保留你日后修改错误类型的自由。注意这个统一：`throws` 就是 `throws(any Error)`，不抛错就是 `throws(Never)`——`map` 能同时抽象两者靠的就是这一点。
- **只在能说出不变量时才强制解包**，而且比起裸 `!`，更推荐带消息的、会失败的 `#require`/`precondition`。

---

## 3. 并发：在性能分析给出证据之前保持单线程

这是 Agent 最容易搞错的一节，因为模型在 Swift 6.2 变了。

每个应用都从纯主线程开始。单线程代码能走很远，大多数应用根本不需要离开它。

**按顺序进阶。不要跳步。**

1. **主 actor 上的单线程。**完全不用并发。对大多数应用足够。
2. **`async`/`await`** 用来隐藏延迟（网络、磁盘）。仍然没有你自己的并发，`URLSession.data(from:)` 这类 SDK API 会替你卸载。
3. **`@concurrent`** 把 _你自己的_ 昂贵工作挪下主线程。只在 Instruments 显示出卡死之后用。
4. **`actor`** 把 _状态_ 挪下主 actor。只在过多的主 actor 状态迫使任务不停跳回时用。

**先打开正确的构建设置。**每个项目都启用 **Approachable Concurrency**。对应用模块和面向 UI 的模块，再把 **Default Actor Isolation** 设为 **MainActor**：这是 Xcode 26 新建应用项目的默认值，而且能删掉你大部分 `@MainActor` 标注。在包里用 `swiftSettings: [.defaultIsolation(MainActor.self)]`。**不要给通用库设置 main-actor-by-default**——库应该提供 `nonisolated` API，让调用方决定工作在哪里运行。

### 变了的规则

**在 Swift 6.2 里，把函数标成 `async` 并 _不会_ 把它挪下当前 actor。**它就在被调用的地方运行。"最自然的写法"因此默认免于数据竞争。

- **`@concurrent`**：总是切换到并发线程池。用在 _你自己的_ CPU 密集工作上。
- **`nonisolated`**：在哪里调用就在哪里运行。**这是库 API 的正确默认**，因为由调用方决定。类型上的 `nonisolated` 让其所有成员都是 nonisolated（Swift 6.1+）。
- 两者都不加：留在调用方的 actor 上。

```swift
nonisolated struct PhotoProcessor {          // decoupled from the main actor
  @concurrent                                // guaranteed to run in the background
  func process(_ data: Data) async -> ProcessedPhoto {
    async let sticker = extractSticker(data)  // two independent jobs, in parallel
    async let colors  = extractColors(data)
    return await ProcessedPhoto(sticker: sticker, colors: colors)
  }
}
```

- **先做性能分析再卸载。**用 Instruments（Time Profiler、hangs）。如果不用并发也能让代码更快，永远先走那条路。并发有真实成本：任务分配、调度和心智负担。
- **别为琐事开任务。**为了读一个 `UserDefaults` 值开子任务，花的比省的多。
- **每个端到端操作一个任务。**必须按顺序进行的工作放进 _一个_ 任务；相互独立的操作分到不同任务，让运行时能交错执行。
- **`await` 是挂起点，它会打破原子性。**挂起期间状态可能改变，恢复时也可能换了个线程。每个 `await` 之后都重新检查假设。绝不在 `await` 期间持有锁。绝不跨 `await` 依赖线程本地存储。

### Actor 的可重入性

Actor 保证互斥，不保证事务。同一 actor 上两个 `await` 之间，别的工作会插进来运行。

- **在同步方法里修改 actor 状态。**actor 上的同步代码会不被打断地跑完，这就是你的事务边界。
- **让 actor 的异步方法保持薄**，由同步的事务性操作组合而成，并在每个 `await` 处都把 actor 留在一致状态。
- 经典 bug：查缓存 → `await` 下载 → 写缓存。两个任务都未命中，都去下载，第二个覆盖第一个。`await` 之后重新检查，或者对进行中的工作去重。
- **Actor 不是 FIFO。**它们优先运行最高优先级的工作，正是为了避免优先级反转。需要顺序时，用任务（从头跑到尾）或 `AsyncStream`，别用 actor。

---

## 4. Sendable 与数据共享

`Sendable` 标记一个类型可以安全地跨隔离域共享。编译器在每个任务和 actor 边界检查它。

- **值类型在其存储可共享时就是 `Sendable` 的**，非公开类型会自动推断。**公开类型永远不会被推断 sendability**：把公开类型标成 `Sendable` 是对客户端的承诺，所以 Swift 要求你亲手写。
- **Actor 和 `@MainActor` 类隐式 `Sendable`**，因为它们的状态是隔离的。
- **大多数模型类既不该是 `@MainActor` 也不该是 `Sendable`。**有意保持非 `Sendable`：这能防止模型的一半在主线程被改、另一半在后台被改。如果它们需要离开主 actor，把它们做成 `nonisolated`，而不是 `Sendable`。
- **非 `Sendable` 对象仍然可以 _发送_ 到另一个域**，只要发送方停止使用它。所有修改都在 _交接之前_ 做完；之后再碰它就是错误。
- 闭包也捕获状态。只有函数类型真的跨域时才标 `@Sendable`。
- **`@unchecked Sendable` 是编译器无法检查的承诺。**只留给真正有内部同步的类型（`Mutex`、锁）。全局变量上的 `nonisolated(unsafe)` 同理：最后手段，不是消警告的工具。

**遇到数据竞争错误时，按这张清单逐条处理：**

1. **别共享它。**把共享对象挪进局部变量，让每个并发任务拿到自己的实例。（这能解决绝大多数真实错误。）
2. **把它做成 `Sendable` 值类型**，这样"共享"其实就是复制。
3. **把它隔离到 actor**：主 actor，或你自己的。
4. 到这一步才考虑 `Synchronization` 模块里的 `Mutex`/`Atomic`（存放在 `let` 属性里），或 `@unchecked Sendable`。

**全局和静态变量是最常见的错误来源。**按优先顺序：改成 `let`；放到 `@MainActor`；包进 `Mutex`；`nonisolated(unsafe)`。注意 Swift 的全局变量是惰性 _且_ 原子初始化的，这点和 C 不同。

**桥接旧的回调 API：**自己拥有的委托协议标上 `@MainActor`。不是自己拥有的，把方法标成 `nonisolated` 并使用 `MainActor.assumeIsolated { }`：它做断言而非跳转，出问题会响亮地崩溃，而不是悄悄竞争。一致性上的 `@preconcurrency` 是同一件事的简写。用 `@preconcurrency import` 暂时压住某个尚未迁移模块的 sendability 警告；等它迁移完，警告会正确地回来。

---

## 5. 结构化并发

永远优先用结构化任务。

结构化任务（`async let`、task group）的作用域像局部变量：活不过所在代码块、被自动 await、并通过任务树继承取消、优先级和 task-local 值。非结构化任务（`Task { }`、`Task.detached`）这些都不自动给你。

- **`async let`** 用于数量固定、编译期已知的并发子任务。
- **`withTaskGroup`** 用于数量动态的情况。Task group 遵循 `AsyncSequence`，结果一到就能迭代。子任务不返回东西时用 **`withDiscardingTaskGroup`**：它立即释放每个子任务的资源，并在第一个错误时取消兄弟任务。
- **`Task { }`** 只在工作生命周期不适合作用域时用：响应委托回调、按钮点击、视图出现。它继承 actor 隔离和优先级；取消要自己管理。
- **`Task.detached`** 几乎不用。它什么都不继承：不继承隔离、不继承优先级、不继承 task-local。真需要分离的根任务时，在它 _内部_ 放一个 task group，而不是反复分离。

**取消是协作式的。**取消只是设置一个标志，什么也不会停。**在开始昂贵工作之前**检查 `Task.isCancelled` 或 `try Task.checkCancellation()`，同步的辅助函数里也要检查。对于处于挂起而非运行状态的工作（`AsyncSequence` 的 `next()`），用 `withTaskCancellationHandler`，并记住处理器会立即、与主体并发地运行，所以它触碰的状态需要真正的同步（原子操作或锁，而不是 actor；你无法在 actor 上保证顺序）。

**给并发设上限。**不要对无界列表每项开一个子任务。先开 N 个子任务，每完成一个再补一个新的。

**Task-local 值**（`@TaskLocal`）把上下文（请求 ID、追踪 span）沿任务树向下传递，不用在每个函数签名里穿参数。把它们设为可选，让未绑定时的读取有合理默认值。

**桥接回调：**`withCheckedContinuation` / `withCheckedThrowingContinuation`。契约是**每条路径上恰好恢复一次**：从不恢复会让调用方永远挂起；恢复两次是致命错误。对稍后才触发的委托 API，先存住 continuation，恢复时置为 nil。（尚未发布的 Swift 6.4 新增了一个在编译期检查单次恢复的 `Continuation` 类型。）

**`AsyncSequence`：**用 `for await` / `for try await` 迭代。用 `AsyncStream` / `AsyncThrowingStream` 改造现有的基于 handler 或委托的 API：在闭包里构造源，在 handler 里 `yield`，在 `onTermination` 里清理。

---

## 6. SwiftUI 中的并发

- **`View` 隔离在 `@MainActor` 上**，它包含的一切也一样，包括你的 `@State`。你几乎从不需要在视图或视图模型上写 `@MainActor`；开了 main-actor-by-default 之后，已有的也能删掉。
- **SwiftUI 故意把你的部分代码放到主线程之外**，好让每一帧都便宜。信号是 API 签名里的 `@Sendable`：`visualEffect`、`Shape.path(in:)`、`Layout` 的需求、`onGeometryChange`。在这些闭包里撞上隔离错误时，**别发送 `self`：把你需要的那个值复制进闭包捕获列表。**

```swift
.visualEffect { [pulse] effect, proxy in    // copy the Bool, don't capture self
  effect.blur(radius: pulse ? 2 : 0)
}
```

- **SwiftUI 的动作回调故意是同步的。**对时间敏感的 UI 更新（响应手势或滚动事件启动动画）必须和事件发生在同一帧。把 `withAnimation` 的状态变更放进同步回调；只为随后的耗时工作开 `Task`。
- **在 UI 与异步工作的接缝处放一块状态。**视图启动任务；异步层完成后做一次同步修改；UI 做出反应。这样视图逻辑保持同步，异步逻辑不用导入 SwiftUI 也能测试。

---

## 7. 协议与泛型

不要从 class 开始。**也不要从协议开始。**

工作流：**先写具体类型 → 注意到它们之间的重复代码 → 把共享能力提炼成协议 → 针对协议写泛型代码。**函数体几乎相同的重载就是该泛化时的信号。

- **没有按类型自定义的协议是浪费。**如果每个遵循都会用同一个默认实现，那就改成在现有协议上写受限扩展。精巧的协议层级（"类型动物园"）消耗编译时间和二进制体积，换不来任何东西。
- **优先"有一个"而不是"是一个"。**如果协议的操作只有一部分对你的类型有意义，别去细化它：用泛型 struct 包住它，只暴露你真正想要的 API。（用 `GeometricVector<Storage: SIMD>` 而不是 `GeometricVector: SIMD`。）
- **协议要求（requirement）是自定义点**：它走动态派发，遵循类型的实现处处生效。**只写在扩展里的方法是静态派发的**，遵循类型的版本是 _遮蔽_ 而非重写，只认识 `any P` 的代码会调用扩展版本。如果类型应该能自定义某件事，就把它做成要求。
- **组合优于继承。**类继承是单体式的（只能有一个父类）、侵入式的（连存储属性和初始化器复杂度一起继承），还留下"什么可以重写、何时调用 super"的未成文契约。改用组合小值。
- **强制向下转型是代码坏味道**：它通常意味着类型关系被类层级或存在类型弄丢了。

### `some` 与 `any`

- **默认写 `some P`。需要存储任意类型时改成 `any P`。**和 `let` 优先于 `var` 是同一条纪律。
- `some P`：每个作用域一个固定的底层类型。所有类型关系（包括关联类型）都保留，编译器还能特化。
- `any P`：类型擦除的盒子，动态类型在运行时变化。异构集合、底层类型需要可选、或要完全隐藏抽象时需要它。代价：关联类型关系被擦除到上界，调用对优化器不透明。
- **不能在 `any P` 上调用带关联类型参数的方法。**擦除在生产位置有效（结果被擦到上界），在消费位置无效。解决办法是把存在类型传给接受 `some P` 的函数：编译器会拆箱，在那个作用域里类型重新固定。
- **受约束的存在类型和不透明类型**（`some Collection<Element>`、`any Collection<any Animal>`）让你隐藏 `LazyFilterSequence<[Animal]>` 的同时仍暴露元素类型。在自己的协议上声明主关联类型（`protocol Container<Item>`），为调用方实际提供的类型服务，而不是为 `Iterator` 这类实现细节。
- **`where` 子句中的同类型约束**用来钉死跨协议的关系（`where Self.CropType.FeedType == Self`）。没有它，"先种植再收获"无法通过类型检查，错误的遵循也能编译。

---

## 8. API 设计：使用之处的清晰性

使用之处的清晰性是这里压倒一切其他目标的目标。

- **纯 Swift 的 API 不加类型前缀。**模块名负责消歧。只有 API 在镜像 Objective-C 版本时才保留前缀。但避免借用具体框架里非常通用的名字：脱离上下文读不懂，还逼人手动消歧。
- **去掉开头的 `get`**，异步版本和一切直接返回结果的东西都如此。用 `persistentPosts`，不用 `getPersistentPosts`。
- **访问控制就是文档。**`private`（文件）、`internal`（模块，默认）、`package`、`public`。在边界处显式声明，才会逼你做出上面的 sendability 和 API 演进决策。
- **把模型设计成非法状态根本写不出来。**私有 setter 加一个做校验的 mutating 方法；封闭集合用枚举；用强类型的 `UUID` 而不是 `String`。
- **属性包装器**提炼出 _访问策略_（`@Argument`、`@Published`、防御性复制、惰性、线程本地），声明处用一个词就说明了策略。配合 key path 上的 `@dynamicMemberLookup` 可以穿透包装器做投影（`$binding.title` 就是这么工作的）。
- **Result builder** 用于声明式 DSL。**宏**用于样板代码本可以由编译器写出来的场合（§12）。

---

## 9. 性能：先测量，再选择

Swift 底层性能由四种开销主导。要知道自己正在付哪一种。

1. **函数调用**：参数复制、静态还是动态派发、调用帧分配，以及被阻塞的优化。
2. **内存布局**：内联还是外部存储；动态大小的类型。
3. **分配**：全局（免费）、栈（便宜：一次减法）、堆（昂贵：搜索加锁）。
4. **复制**：retain/release 和递归的 struct 复制。

**但先做算法层面的工作。**每次写循环，都试着换成一次算法调用。最大的收益几乎从来不是微优化：

- **知道你调用的东西的复杂度。**`Array.remove(at:)` 是 O(n)，在循环里调用就是 O(n²)。`removeAll(where:)` 总共 O(n)。逐字节重新切片来构建 `Data` 是 O(n²)，`popFirst()` 是 O(1)。这两个都是藏在干净代码背后的 100 倍以上的性能回归。
- **链式 `map`/`flatMap`/`filter` 每个阶段都分配一个数组。**优雅 ≠ 快。如果管道在热循环里逐像素或逐元素运行，一次性确定输出大小然后往里写。
- **然后做性能分析。**用 Instruments 的 Time Profiler 和 Allocations，对着一个 _测试_ 运行（右键点击测试的运行按钮 → Profile），这样测的才正是你关心的代码。`platform_memmove` 占满火焰图意味着意外复制；上百万个瞬态分配意味着中间数组；`swift_beginAccess` 意味着运行时排他性检查；`swift_retain`/`swift_release` 意味着引用计数流量。

**具体的抓手，大致按收益排序：**

- **不打算子类化的类加 `final`**，把动态派发变成静态，解锁内联。全模块优化在许多情况下能让编译器替你证明这一点，还启用泛型特化，泛型从此零开销靠的就是它。
- **struct 的存储是内联的；class 的存储是外部的。**小 struct 免费；有三个引用类型字段的大 struct 每次复制要付三次 retain，而 class 只付一次。复制频繁就用写时复制。
- **`any P` 存在类型有 3 个字的内联缓冲区。**装得下的值内联存放；装不下的每次复制都要堆分配。同一招仍然有效：给大类型配上写时复制的间接存储，它又能装进缓冲区了。
- **同构的 `[MyModel]` 优于 `[any Model]`**：紧密排列、类型信息只传一次、可以特化。`[any Model]` 是灵活但不透明的选项；需要时就用它。
- **把泛型参数约束为类**（`T: AnyObject`），即使没有特化也给编译器一个已知的表示。
- **`InlineArray<N, T>`**（Swift 6.2）用于固定大小存储：元素内联存放、大小通过值泛型写进类型、无堆分配、无引用计数、无唯一性或排他性检查。会被复制或共享时是错误选择。
- **`Span` / `RawSpan` / `OutputSpan`**（Swift 6.2）取代 `withUnsafeBufferPointer`，直接访问连续存储。它们不可逃逸，编译器把生命周期绑定到容器上：拿到指针级性能且没有生命周期 bug，retain/release 也消失了。
- **把存储属性从嵌套类挪进父级 struct**，可以去掉运行时排他性检查。
- Swift 6.3 已随版本提供，先测出需求再用：`@inline(always)`（方法上配合 `final`）和 `@specialized(where T == ...)`（SE-0460），为热点具体类型预特化泛型。
- 随 Swift 6.4 落地（**未发布**，见 §15 下方的说明）：用 `borrow`/`mutate` 访问器替代 `get`/`set` 来处理大的存储值，`UniqueArray`/`UniqueBox`，以及把循环里的重复查找提出来的 `Ref`/`MutableRef`。

**异步函数**把状态保存在每任务 slab 分配器上而不是 C 栈上，并在每个挂起点拆成部分函数。开销特征与同步函数类似，调用开销略高，这也是"没有任何东西可 await 的函数就不要标 `async`"的又一个理由。

**进出主 actor 的跳转是一次真实的上下文切换。**批量化：把循环 _推进_ `loadArticles`/`updateUI` 内部，让它们接收数组，而不是每次迭代跳两次。

---

## 10. ARC 与对象生命周期

- **对象的保证生命周期终止于最后一次使用，而不是右花括号。**观测到的生命周期是优化器的涌现属性，_一定会_ 变。依赖 `deinit` 何时运行的代码是潜在 bug。
- **`weak`/`unowned` 只用于打破引用循环，不为别的。**在强持有者最后一次使用之后读 `weak` 引用，合法地可能得到 `nil`。这里的可选绑定比强制解包更 _糟_：它把响亮的崩溃变成无声的错误答案。
- **比 `weak` 更好的：别造出循环。**把共享数据提炼成双方都引用的第三个类型，循环就变成了树。
- **次好的：重新设计 API**，让对象只能通过强引用到达。`withExtendedLifetime` 能用，但把正确性压到你身上还会在代码库里扩散。把它当补丁，不当设计。
- **让 `deinit` 的副作用保持局部。**从 `deinit` 上报指标或触发全局效应，顺序会和优化器的决策冲突。改在调用点用 `defer`，`deinit` 留给验证。
- Xcode 的 **Optimize Object Lifetimes** 构建设置会把观测生命周期压向保证最小值，恰好能暴露这些 bug。

---

## 11. 测试：默认用 Swift Testing

新测试用 **Swift Testing**。XCTest 只在三件事上仍是必需：UI 自动化（`XCUIApplication`）、性能指标（`XCTMetric`），以及必须用 Objective-C 编写或要捕获 Objective-C 异常的测试。

- **任何函数都能加 `@Test`**：全局、静态或实例函数；`async`、`throws`、全局 actor 隔离都可以。
- **`#expect(...)` 接受普通表达式。**不用记一堆 `XCTAssertEqual` 式的函数：`#expect(a == b)`、`#expect(list.isEmpty)`、`#expect(!x.contains(y))` 失败时都会捕获并显示子表达式的值。
- **`try #require(...)`** 让测试失败即停，并安全解包可选值。它取代 `continueAfterFailure = false`，还能按断言逐个选择。
- **套件是 `struct`。**每个测试函数都会创建新实例，状态无法在测试间泄漏。用 `init` 做准备；只有需要 `deinit` 做清理时才用 `class`/`actor`。嵌套套件来分组。
- **参数化，不要复制粘贴或写循环。**`@Test(arguments: [...])` 让每个用例独立、并行运行，可以单独重跑，结果里会点名失败的参数。两个参数集合产生完整笛卡尔积；想要配对就用 `zip()`。
- **Trait 承载意图：**`.enabled(if:)` / `.disabled("reason")` 表达条件（永远别注释掉测试，禁用的测试仍然编译）、`.bug(url)` 用于追踪、`.tags(...)` 跨文件和 target 关联测试、`.timeLimit`、测试真的无法并行时用 `.serialized`。用 `@available` 而不是运行时的 `#available` 检查，测试库才知道。
- **`withKnownIssue { }`** 用于因你控制之外的因素而失败的测试：它保持编译和运行，并在问题修复后告诉你，这点和 `.disabled` 不同。
- **`confirmation`** 用于触发 N 次的回调；没有异步重载的一次性回调用 `withCheckedContinuation`。
- **测试默认并行、随机顺序运行。**这是特性不是缺陷：它暴露隐藏的测试间依赖。去重构，而不是伸手拿 `.serialized`。
- **退出测试**（`#expect(processExitsWith: .failure) { ... }`）在隔离子进程里覆盖 `precondition`/`fatalError` 路径。仅限 macOS、Linux、FreeBSD、Windows。
- 迁移：两个框架可以在同一个 target 里共存，所以增量迁移，新测试今天就用 Swift Testing 写。**测试框架互操作**（swift-testing ST-0021；可用性取决于你的 Xcode 版本）让包装 `XCTFail` 的辅助函数能被 Swift Testing 测试调用，反过来也行；把模式设为 **complete** 或 **strict**（不要 **limited**，更不要 **none**），跨框架问题保持为错误，并指向 `Issue.record` 的替代写法。

---

## 12. 宏

当你在写编译器本可以推导出的代码时才用宏，而且只有这时才用。

- **宏在展开之前先做类型检查。**参数对照宏声明的签名检查，误用会在调用处给出干净的错误，而不是生成代码内部的一团糟。
- **独立宏（`#foo`）**产生表达式或声明。**附加宏（`@Foo`）**以五种角色之一增强声明：member、peer、accessor、member-attribute、conformance。角色可以组合：`@Observable` 就是 member + member-attribute + conformance。
- **把宏当作纯语法树变换来测试**，用 `assertMacroExpansion`。这是最快的反馈循环，也是避免"没人读的代码里藏 bug"的方法。在 `expansion` 里设断点，`po` 那个语法节点，看清它的形状。
- **宏不适用时发出真正的诊断。**抛出错误，或用 `context.addDiagnostic` 在特定位置给出警告和修复建议（fix-it）。绝不让宏悄悄生成编译不过的代码。
- 展开后的代码就是普通 Swift：可查看（"Expand Macro"）、可调试、可单步。

---

## 13. 日志与调试

- **用 `os` 的 `Logger`，不用 `print`。**每个子系统加类别各建一个。消息以优化过的形式存储，只在展示时渲染，日志便宜到可以一直留在代码里。
- **非数字插值默认被隐去。**用 `privacy: .public` 按值选择公开，只用于确实不涉及个人信息的数据。需要关联数值又不暴露它们时用 `.private(mask: .hash)`。
- **级别控制持久化和成本：**`debug`（从不持久化，最快，不流式传输时消息构造被完全优化掉）、`info`、`notice`（默认）、`error`、`fault`（最持久，最慢）。bug 报告里会想要的东西记在 `error`/`fault`。
- **记一个关联 ID**（任务或请求的 UUID），不用复现就能从设备日志归档里筛出整场失败的来龙去脉。`log collect --device --start ...`，然后在 Console 里按子系统过滤。
- `format:` 和 `align:` 是免费的，用上它们，日志才可读、可按列筛选。
- LLDB 懂 Swift 任务：它能跨线程单步穿过 `await`，`swift task info` 显示优先级和子任务，命名任务在调试器和 Instruments 的 Swift Concurrency 模板里都会出现。

---

## 14. 不安全代码与互操作

- **"Unsafe"的意思是这个 API 无法完全验证输入，违反前置条件就是未定义行为**，并不是说它会崩溃。安全 API 是 _会_ 故意 trap 的；干净的致命错误才是安全的结果。
- **优先 `Span` 而不是 `Unsafe*Pointer`。**从 Swift 6.2 起有了一条安全、不可逃逸、同样快的途径去访问连续存储。裸指针留给 C 互操作。
- 必须用指针时：让不安全区域尽量小；用 **buffer** 指针（地址 + 数量）而不是裸指针，让边界可追踪；绝不让指针逃出提供它的闭包；打开 **Address Sanitizer**。
- 在安全关键的模块里启用 **strict memory safety**：它强制每一处不安全使用都在源码里被显式承认，这才让审计成为可能。Swift 6.4 的 `@diagnose` 特性（未发布）可以按单个函数开启。
- **互操作是双向且增量的。**C、Objective-C、C++ 类型直接映射进 Swift（包括 C++ 值语义、容器映射为 Swift 集合、move-only 类型映射为 `~Copyable`）。Swift 6.3 的 `@c` 特性把 Swift 函数暴露回 C（声明已存在于头文件时配 `@implementation`）。一次一个文件地引入 Swift；不要重写。

---

## 15. 你应该用起来的现代语法

Agent 一贯写出下面这些东西的旧版、更长的写法。

**标了 ⚠ 的行属于尚未发布的 Swift 6.4。**当前版本是 6.3.x。它们的提案已被接受并在 main 分支实现，所以可以放心围绕它做规划，但今天就写进代码不安全。使用前检查项目的工具链；目标为 6.3 或更早时优先用旧写法。

| 别再用                                                                | 应该写                                                                                                   | 起始版本 |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------- |
| 嵌套三元；用立即执行的闭包初始化 `let`                                 | `if`/`switch` **表达式**                                                                                  | 5.9      |
| 为 1、2、3… 个参数写重载                                               | **parameter pack**（`each T`），以及对 pack 的 `for`                                                      | 5.9      |
| 每个属性都 `ObservableObject` + `@Published`                            | **`@Observable`**                                                                                         | 5.9      |
| 轮询对象等变化                                                         | **`Observations { ... }`**（事务性更新的 `AsyncSequence`）                                                | 6.2      |
| `NotificationCenter` 配字符串类型的 `userInfo`                          | 具体通知类型（`MainActorMessage` / `AsyncMessage`）                                                       | 6.2      |
| 脚本场景用 `Process` + 管道                                            | **Subprocess** 包（`AsyncBufferSequence.strings()` 逐行输出；1.0 随 6.4 发布）                             | 6.2+     |
| 手写字符串下标运算                                                     | **Swift Regex**（字面量求简洁，`RegexBuilder` 求结构）                                                    | 5.7      |
| 热路径里固定大小的 `[String]`                                          | **`InlineArray<N, T>`**                                                                                   | 6.2      |
| `withUnsafeBufferPointer`                                              | **`.span`** / **`.bytes`**（`RawSpan`）/ `OutputSpan`                                                     | 6.2      |
| 手动搬弄 `Task.isCancelled` 来完成一次写入                             | `Task` **取消护盾**（SE-0504）                                                                            | 6.4 ⚠    |
| 为了用 key 手工重建字典                                                | **`mapKeyedValues`**                                                                                      | 6.4 ⚠    |
| `@available(iOS ..., macOS ..., tvOS ..., watchOS ..., visionOS ...)`  | **`@available(anyAppleOS ...)`**                                                                          | 6.4 ⚠    |
| 类型遮蔽模块时的 `Rocket.SaturnV`                                      | **模块选择器** `Rocket::SaturnV`                                                                          | 6.3      |
| 一刀切的"警告即错误"                                                   | 按声明 / 警告组的 **`@diagnose`**                                                                          | 6.4 ⚠    |
| 因为一个 `weak var` 就用 `@unchecked Sendable`                         | `weak let`；或用 **`~Sendable`** 声明不可发送                                                             | 6.4 ⚠    |
| 用指针手工解析二进制格式                                               | **Swift Binary Parsing**（`ParserSpan`、带溢出检查的解析初始化器）                                        | 6.2      |
| 别扭的测试函数名                                                       | **raw identifier**：`` @Test func `fruits have a tropical climate`() ``                                    | 6.0      |

另外值得知道：**Swift Regex 的解析器可以和 Foundation 的真解析器组合**（`.date(...)`、`.currency(...)`），永远不要在正则里手写日期或数字解析。把 locale 显式写出来，不要继承系统的。用 `NegativeLookahead` 或 `Local`（原子组）阻止模式在整个输入上回溯。

---

## 16. 把现有代码库迁移到 Swift 6

顺序很重要，混着做就是迁移停滞的原因。

1. **先用新编译器构建。**源兼容性保证这应当直接通过，在 Swift 5 模式下。
2. **按 target 开启 complete 并发检查**（Swift 5 模式 + 全部 Swift 6 警告）。从 **UI/应用层**开始，而不是下面的框架：SDK 已经给很多东西标好了主 actor，修复率高。
3. **修警告，从最便宜的修起。**几百条警告往往来自少数几个根因：该是 `let` 的 `var` 全局变量、该放 `@MainActor` 的自由函数、需要 `: Sendable` 的一个公开 struct。一行能清掉几十条。
4. **把 target 切到 Swift 6 语言模式**，把成果锁住。
5. **换下一个 target，重复。**
6. **之后单独做重构。**绝不要把大重构和开启数据竞争安全绑在一起，否则两者都得回退。

你可以把严格检查再关掉照样发布上线；做过的每一处修复都是能留下来的真实改进。**开始之前**就启用 **Approachable Concurrency**，应用模块再加上 main-actor-by-default：两者都会大幅减少你会看到的错误数量，Xcode 还自带迁移工具，能替你完成许多修改（swift.org/migration）。

---

## 速查表

| 需求                               | 用什么                          | 别用                                      |
| ---------------------------------- | ------------------------------- | ----------------------------------------- |
| 数据类型                           | `struct` / `enum`               | 没有身份或共享需求的 `class`              |
| 共享可变状态                       | `actor`，或 `@MainActor` 类     | `class` + 一个你得记住去加的锁            |
| 把工作挪下主线程                   | `@concurrent func … async`      | `Task.detached`、`DispatchQueue.global()` |
| 库 API 的隔离                      | `nonisolated`                   | `@MainActor`、`@concurrent`               |
| 固定数量的并行任务                 | `async let`                     | N 个非结构化 `Task`                       |
| 动态数量的并行任务                 | `withTaskGroup`（有界）         | 每元素一个任务、无界                      |
| 不返回结果的子任务                 | `withDiscardingTaskGroup`       | 从不取空的 `withTaskGroup`                |
| 绑定 UI 事件的工作                 | 回调里的 `Task { }`             | 把回调改成 `async`                        |
| 修数据竞争                         | 停止共享对象                    | `@unchecked Sendable`                     |
| 共享的模型类                       | 非 `Sendable`，或 `@MainActor`  | `Sendable` + 手动加锁                     |
| 跨 `await` 的阻塞原语              | 没有，重构结构                  | `DispatchSemaphore`、`NSCondition`        |
| 多态                               | `some P`                        | `any P`，除非你需要存储                   |
| 异构集合                           | `[any P]`                       | 类层级                                    |
| 共享行为、无需自定义               | 受限 `extension`                | 新协议                                    |
| 自定义点                           | 协议 **requirement**            | 只在扩展里的方法                          |
| 打破引用循环                       | 重构为树                        | `weak` + `withExtendedLifetime`           |
| 删除匹配元素                       | `removeAll(where:)`（O(n)）     | 循环里的 `remove(at:)`（O(n²)）           |
| 直接访问连续内存                   | `.span`                         | `withUnsafeBufferPointer`                 |
| 热路径里的固定大小缓冲区           | `InlineArray<N, T>`             | `Array`                                   |
| 新测试                             | `@Test` + `#expect`             | `XCTestCase` + `XCTAssertEqual`           |
| 同一测试跑多个输入                 | `@Test(arguments:)`             | `for` 循环或复制粘贴                      |
| 失败即停测试                       | `try #require`                  | `continueAfterFailure = false`            |
| 暂时失败的测试                     | `withKnownIssue`                | `.disabled` 或注释掉                      |
| 发布代码里的诊断                   | `Logger` + 关联 ID              | `print`                                   |
| 决定要不要优化                     | 对做了性能分析的测试跑 Instruments | 直觉                                   |

