> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/MEMORY-SAFETY-AND-BINARY.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 内存安全、二进制与内核审查

#### 何时使用本文件

当目标在内存不安全或特权上下文中处理不可信字节时使用本文件：C/C++/Objective-C、Rust `unsafe`、FFI、内核模块与驱动、解析器与解码器、网络守护进程、固件、二进制加载器、语言运行时和 JIT。协议授权与状态机逻辑用 `PROTOCOLS-RPC-AND-MESSAGING.md`；本文件负责进程完整性、内存安全、ABI 边界和加载器行为。

从 Phase 1 中挑选相关类别，并按解析器、分配器/生命周期、FFI、并发、加载器、运行时或特权接口拆分大型目标。

## 核心纪律（加入本领域的每个 agent 提示词）

```
- Re-derive every bound and lifetime from attacker-controlled inputs and all callers. Validate against the worst accepted case, not a typical test vector.
- A panic, sanitizer finding, or crash proves a defect only when a realistic untrusted input reaches it. Do not infer memory corruption, code execution, or shared availability impact from a label alone.
- Validate in a local harness with sanitizers, deterministic concurrency tests, existing fuzz targets, and debugger-assisted fault classification. Stop after proving the violated invariant and observable impact; do not develop post-corruption techniques.
- Assembly, JIT code, custom allocators, intra-object accesses, and foreign libraries can escape sanitizer coverage. Identify which relevant instructions are instrumented.
- Classify as `confirmed` only after source evidence and bounded local validation establish the defect and effect. Use `needs_validation` when ABI, allocator, architecture, feature, deployment, or reachability facts remain unknown.
```

## 边界、整数与表示攻击类别（subagent_type: `general`）

**越界读或越界写**
长度、偏移、索引或终止符在没有正确边界检查的情况下到达固定或已分配缓冲区。在前缀、对齐、填充和终止符之后重新计算可用余量。同时检查源与目标容量，以及是否在信任声明长度之前就读取了短输入。

**整数溢出、下溢、截断与符号性**
审查攻击者可控的算术：分配、拷贝、循环、索引和指针操作之前。高命中模式包括 `b > a` 时的 `a - b`、`count * element_size`、接近类型最大值的加法、负值转无符号、64 位长度收窄到 32 位字段、以及哨兵值（如 `-1`）变成巨大尺寸。确认稍后实际使用的是哪个经过检查的表示。

**单位与指针深度混淆**
代码混用了字节、元素、码元（code unit）、页、字、线上传输单位或嵌套指针的元素大小。在解析、验证、分配、API 边界和拷贝处对比所用单位。用与分配相同的错误单位做的边界检查，仍然是错的。

**未初始化或部分初始化的数据**
缓冲区、填充、结构体字段或 vector 容量在初始化之前被返回、比较、哈希、序列化或跨信任边界传递。要求一个可观测的消费者和现实的输出长度；栈分配本身不构成泄露。

## 生命周期、类型与并发攻击类别（subagent_type: `general`）

**释放后使用（use-after-free）、过期视图与双重释放**
所有者被释放时，回调、等待队列、定时器、迭代器、借出的切片或缓存的裸指针仍可能使用它们。审查每一条错误、取消、关闭和 realloc 路径。对嵌入式的通知锚点，每条 free 路径都必须排空或摘除全部观察者。

**类型混淆与非法向下转型**
标签、vtable、联合判别式、对象种类或外部句柄的检查方式与稍后读取的表示不一致。寻找未检查的动态转换、重用后过期的标签，以及被验证元素与被消费元素不同的序列化类型。在本地确认一次错误类型的读或写，测试不要超出被违反的不变量。

**引用计数与所有权竞态**
非原子的 retain/release、检查后无锁使用，或跨线程不一致的所有权，可能在访问期间释放或修改对象。对同一把锁和同一套所有权规则，对比快速、错误、关闭和兼容路径。

**共享状态竞态与 TOCTOU**
并发的解析器流、全局缓存、惰性初始化、信号处理程序和资源拆除会使先前建立的边界、策略或指针失效。用可复现的本地调度、屏障或 thread sanitizer 验证竞态；没有安全相关状态转换的假设性交错仍保持 `needs_validation`。

**锁顺序、死锁与饥饿**
外部可达的操作以不一致的顺序获取锁，或在回调和阻塞 I/O 期间持锁。只有当受限输入能停止共享进度时才按可用性报告；否则记为并发缺陷待修复。

## FFI 与 ABI 攻击类别（subagent_type: `general`）

**指针长度与所有权契约不匹配**
调用方与被调方在谁分配、释放、固定（pin）或修改缓冲区、指针保持有效多久、长度是字节还是元素等问题上意见不一致。追踪每个 `extern`、CGo/JNI/Python/native 绑定和生成的包装器的两侧。检查 null、零长度、别名和回调持有。

**布局、对齐与枚举不一致**
外部代码收到的结构体、位域、紧凑记录、回调签名、整数宽度、枚举或调用约定因架构或构建标志而不同。验证 `repr`、打包、对齐、字节序和 ABI 特定类型。仓库内的声明不匹配可以本地确认；不透明的外部实现要求 `needs_validation`。

**栈展开、异常与线程亲和违规**
异常或 panic 穿越了禁止展开（unwinding）的 ABI、回调在拆除之后运行，或要求特定运行时线程的 API 在别处被调用。审查错误转换与取消。在判定影响之前，确认进程是中止还是状态损坏。

## 二进制加载与运行时攻击类别（subagent_type: `general`）

**库、插件与可执行文件搜索顺序信任**
特权进程从更低信任主体可写的路径加载库、插件、运行时镜像或 helper，或通过可被攻击者影响的工作目录或环境解析裸名称。对比预期的安装归属与每个后备及兼容搜索路径。用户把自己的插件加载进自己的进程不构成边界违规。

**缺失的工件身份或签名绑定**
加载器验证了一个文件或元数据记录，却映射了另一个镜像，因为路径解析、文件替换、架构分片或嵌入资源没有绑定到该检查。供应链真实性属于 `SUPPLY-CHAIN-AND-RELEASE.md`；本类别覆盖本地的"验证到映射"缺口。

**畸形二进制元数据与重定位处理**
偏移、计数、节、重定位、符号、字节码或调试元数据在范围、重叠和表示检查之前被信任。用受限的本地 fixture 和 sanitizer 测试解析器。把内存损坏与安全拒绝畸形文件区分开。

**JIT 与生成代码一致性**
验证器、解释器、优化器和生成代码对类型、边界、副作用或生命周期的理解不一致。用同一本地输入 diff 优化与未优化路径。确认进程完整性影响；保持在语言语义之内的输出差异不是发现。

**卸载、重载与拆除安全**
存活的函数指针、回调、工作线程或数据视图在模块卸载或运行时重置后仍然存在。对关闭和加载失败的清理要像启动一样仔细审查。

## 内核与特权接口攻击类别（subagent_type: `general`）

**用户拷贝边界与重复读取**
syscall、ioctl、驱动或内核解析器从用户内存导出一个可信事实，然后再次读取同一个可变地址。一次性完整拷贝请求，或对后一次拷贝重新验证。同时审计每个用户拷贝原语的大小、方向和访问检查。

**特权对象生命周期与分发一致性**
外部可达的对象有失衡的 retain/release、没有排空观察者的拆除、未检查的选择器/表索引，或省略了守卫的重复兼容路径。并排 diff 每一条分发路径和释放路径。

**授权不足的强力接口**
设备节点、管理 socket、helper 或管理 API 验证了形状，却没有验证调用者对该资源的权限。确立真实的接口所有权和可达性；仓库之外的权限或沙箱策略使这里为 `needs_validation`。

## 通用手法（适用于以上所有类别）

- 为同一"源到汇"形状审计修复补丁和重复路径。一个调用方、架构、协议角色、特性开关或兼容路径中的检查保护不了它的兄弟路径。
- 为每个解析器或 FFI 边界建一张表：接受的长度/类型、被检查的表示、分配所有者、消费者、线程和拆除。大多数 native 发现就是这张表里的一处分歧。
- 使用既有语料和小型本地生成的边界 fixture。保存精确的 sanitizer/运行时输出和触发它的输入属性；避免大量资源消耗和任何在线目标。

## 验证规则（报告本文件任何发现之前先执行）

1. 确立现实的不可信入口和违反边界、类型、生命周期、ABI、并发、加载器或权限不变量的精确操作。
2. 对可观测影响分类：非法读、非法写、过期别名、错误对象、未初始化输出、未授权镜像加载、死锁或安全的进程终止。不要声称比观测到更强的效果。
3. 运行复现该影响所需的最窄本地 harness、既有测试、sanitizer 或 fuzzer。核实对出错操作的 sanitizer 覆盖，并记录架构/构建条件。
4. 对并发，用确定性调度或 sanitizer 轨迹。对二进制加载，证明被检查的身份与被映射的身份不同，并点名更低信任的写入者。
5. `confirmed` 发现必须有精确输入、源码轨迹和观测结果。`needs_validation` 要指明具体未决的可达性、ABI、构建、部署或运行时事实，并说明所需的受限检查。
