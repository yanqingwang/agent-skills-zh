> **中文汉化版** · 上游：[morluto/rea](https://github.com/morluto/rea) · 原文件：`.agents/skills/reverse-engineer-anything/references/android-applications.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Android 应用产物

使用已连接服务器所声明的 Android 工具。仓库 main 分支与 npm 4.1.0 都包含这一族工具。仅安装本 Skill 无法把它加入较旧的服务器。

先在调用方给出的 APK 路径上运行 `inspect_android_package`，获取包标识、manifest 声明、覆盖情况与内联证据（Evidence）。用 `search_android_classes` 查找候选项，用 `inspect_android_class` 查看单个类的成员，用 `inspect_android_method` 做反编译，用 `trace_android_references` 追传入的静态引用。每次调用各自带上 APK 路径与显式选择器；不要先打开原生会话。当方法存在歧义时，从类清单中选取 `overload_index`，不要靠猜。

对于 JNI 实现，先探查 `inspect_android_jni_bindings`。选择原始 DEX 类/方法标识，以及可选的描述符、ABI 或逻辑库路径。优先用 `detail: "summary"`；完整证据仍然保留，`android-jni` 视图会分页呈现声明、库、候选项或绑定行，并给出确切字段。全局 native-pair 的歧义不会因为选定了类而消失。保留 slot/relocation 的来源信息与源覆盖范围：matched 表示观察到候选存在；部分扫描不能确立唯一性，也不能确立不存在。该操作只读取 DEX/ELF 字节，不会把 APK 载入反编译器，也不会执行目标代码。运行时注册与加载情况仍属未知。参见 [JNI 指南](https://github.com/morluto/rea/blob/main/docs/android-analysis.md#link-native-declarations-to-jni-candidates)。

对于带 `mapping.txt` 的 R8/ProGuard 发布构建，把绝对路径的 `mapping_path` 传给 `inspect_android_class` 或 `inspect_android_method`。优先用 `detail: "summary"`，以拿到规范化符号或选定的函数体，且不会重复返回原始类元数据。完整证据在关联的父 ID 下保持保留，可以导出；CLI 摘要交付需要 `--evidence_output`。省略 detail 或请求完整 detail 都会保留完整的内联响应。继续按观察到的名称做选择；独立的 `mapping` 块会在核对 DEX 类型与原型之后，把每个符号报告为 `mapped`、`ambiguous` 或 `unmapped`。REA 不会核验该 mapping 是否属于该 APK 的那次构建。

该提供方需要另行提供的 headless JADX MCP JAR 0.7.1，以及 Java 17 或更新版本。`REA_JADX_MCP_JAR` 指定 JAR 的绝对路径；`JAVA_HOME` 可指定 Java。用 `rea doctor --provider jadx --json` 检查 JADX 配置，并取得缺失前置条件的补救办法。Java 与 headless JADX MCP JAR 始终由调用方提供；REA setup 不安装也不配置它们。配置就绪并不等于对某个特定 APK 的分析已经成功。

Linux 与 macOS 使用 POSIX 的自有进程边界。Windows x64 需要匹配的随包原生控件，并使用自有的 Job Object 与双向 stdio。每个主机都需要完整 JDK，包含 `jdk.compiler`；Windows 的 `JAVA_HOME` 指向 `bin\java.exe`。实际的主机验证覆盖范围请查阅 Android 指南。调用使用单个 worker 与提供方截止时间；可选的 `REA_JADX_HEAP_MIB` 指定 JVM 堆，`REA_JADX_OPERATION_TIMEOUT_MS` 指定单次操作的截止时间（整数毫秒，取值 1 到 2147483647，默认 120000）。要修改正在运行的 MCP 服务器上的该截止时间，通过 `update_analysis_settings` 设置 `jadx.operation_timeout_ms`，然后等工作与清理落定后再重试。新接受的操作使用该覆盖值；已接受的工作保留其原有预算。更改启动环境需要新起一个进程。MCP 客户端的工具超时也必须容纳所选的截止时间。APK 永远不会被启动，也不需要模拟器。

manifest 条目与反编译文本是静态观察结果，既不是执行，也不强制执行策略。传入引用是恢复出来的静态关系；反射、动态加载与未解析的调用仍属未知。保留产物摘要值、位置、诊断信息与不完整的覆盖情况。若你要处理的是归档成员而非代码分析，请使用 `open_binary` 与 `inspect_artifact`。
