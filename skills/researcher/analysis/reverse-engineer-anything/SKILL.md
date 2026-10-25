---
name: reverse-engineer-anything
description: 使用 REA 对原生、托管、Electron/JavaScript、打包、固件与浏览器目标进行逆向工程，并从运行实例或捕获文件构建 Web 应用的 Agent 环境（AgentEnv bundle）。利用随发布产物或按需获取的运行时证据来解释功能、比较版本、反编译代码或指导重建。对于普通的源码仓库架构分析，跳过 REA。
metadata:
  version: "49"
---

> **中文汉化版** · 上游：[morluto/rea](https://github.com/morluto/rea) · 原文件：`.agents/skills/reverse-engineer-anything/SKILL.md` · License: MIT
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# REA

当某个论断依赖于已发布的二进制或软件包、反编译结果、
按需获取的运行时证据，或与现有源码无法确立的
行为进行比较时，使用 REA。对于完整源码仓库的
常规分析，请使用普通的仓库工具，不要运行 REA
的就绪检查或提供方命令。

## 仅在需要时连接

安装本 Skill 只提供说明；它不会注册 REA MCP 服务器、安装分析引擎，
也不会向已在运行的 Agent 添加工具。

如果 REA 工具可用，且没有理由认为其注册已过期，就直接前往目标。
不要在每次调查前都运行诊断或安装步骤。使用已连接服务器实际的
工具列表和输入 schema；从仓库 main 分支安装的 Skill 可能描述了
旧版 npm 发布包中不存在的能力。当该服务器未声明
保留引用（retained references）时，
请完整保留内联证据（Evidence）。

如果工具缺失、某次调用被客户端拦截，或所需的提供方（provider）
不可用，请阅读[连接与恢复指南](references/connection-and-recovery.md)。
先诊断观察到的阻碍，继续完成可行的受支持工作，并在修复后恢复原任务。
客户端批准、shell PATH、注册状态与引擎可用性各有不同的
补救方式；不要对所有情况都重复同一套安装流程。
如果宿主超时而没有返回 REA 结果，不要原样重复该调用，
也不要假设工作已经停止。重试前先阅读恢复指南中对截止时间
（deadline）的区分。
如果 MCP 连接中断，仅当该调用可以安全重复、或已知尚未开始时，
才重试一次。如果它可能已经改变了目标，或者再次失败，
请告知用户并请其重启 MCP 客户端。如果 REA 无法建立连接，
重试一次，然后告知用户并请其重启 MCP 客户端。不要重试
返回相同结果的启动失败。当 REA 无法启动，或重启后
工具仍然缺失时，运行 `rea doctor`。对于 `cleanup_incomplete`、
可重试的容量限制或 `configuration_invalid`，在请求重启之前
先按照恢复指南的阶梯处理。在进行第二次修复尝试之前，先阅读该指南。

1. 在不更改 REA 或客户端配置的前提下进行诊断。`npx` 可能会下载
   软件包并写入 npm 缓存。对于 Codex，运行
   `npx -y rea-agents@latest doctor --client codex --json`。替换为
   当前支持的客户端：`claude_code`、`claude_desktop`、`codex`、
   `cursor`、`gemini_cli`、`windsurf`、`devin`、`opencode`、
   `antigravity`、`copilot_cli`、`commandcode`、`vscode`、
   `grok_build`、`omp` 或 `grok_bot`。`grok_bot` 没有本地文件注册：
   doctor 会报告 Grok Bot 聊天步骤，且 setup 不会写入 `mcp.json`。
   如果客户端未知，先使用 `doctor --json` 并检查其注册结果，
   再选择安装范围。
2. 区分原因。注册缺失、格式错误或过期需要进行范围化的配置修复。
   注册一致但活动会话中没有工具，则需要重启/重新连接；
   doctor 无法证明当前 Agent 已经连接。缺少某个提供方只影响
   需要该提供方的任务：静态 JavaScript 检查既不需要 Hopper
   也不需要 Ghidra，Android 检查则有各自独立的
   自带 JADX/Java 前置条件。
3. 进行配置修复时，先准备只读计划：
   `npx -y rea-agents@latest setup --client codex --dry-run --json`。
   使用当前客户端的 ID，展示其确切的建议路径、备份与变更，
   并在 setup 写入配置或安装 Hopper 之前获得批准。Setup 通常
   也会安装配套的内置 Skill；请把该替换纳入审查的计划中。
   获得批准后，用 `npx -y rea-agents@latest setup --client codex --yes`
   应用同样的范围。只有当确实需要那个单独的安装、
   且已获明确批准时，才添加 `--install-hopper`。
4. 重启/重新连接受影响的 Agent。验证 REA 工具确实出现在会话中，
   然后恢复原来的调查。如果工具仍然缺失，检查客户端的
   MCP 启动错误，而不是重复 setup。

REA setup 永远不会安装或升级 Node.js、npm、Homebrew、Java、Ghidra、
IDA、JADX、Kuna、Binwalk 或 Unblob。使用已有的前置条件；
不要为了修复 MCP 注册而安装无关软件。对于不支持的客户端，
使用手动 stdio 注册并固定版本的 `rea-agents` 包，或继续通过 CLI 操作。

对于操作者提供的 JavaScript 目录树或 ASAR，一个具体的 CLI 兜底方案是：

```bash
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json
```

无需 MCP 注册，也无需原生引擎。请以与 MCP 结果同等的谨慎态度阅读
返回的证据（Evidence）、图（graph）、局限性（limitations）与未知项
（unknowns）；CLI 会直接返回证据记录。这一兜底方案并不能证明
MCP 已配置。原生 CLI 任务仍需要其选定的引擎。
优先使用已安装的 `rea` CLI。当没有安装任何 CLI、且获取 REA
软件包在授权范围内时，用 `npx -y rea-agents@latest` 代替。
配置修复从只读的 setup 计划开始；在应用授权的变更之前，
先展示路径、备份与 Skill 替换。
保留既有的批准与目标执行边界。

## 先对目标分类路由

根据用户提供的对象选择第一个工具。针对活动目标的原生或归档
工作流使用 `open_binary`；免目标（target-free）工具自带
明确的路径或端点，不需要它。

- ASAR 或已解包的 JavaScript/Electron 目录树：
  `analyze_javascript_application`。
- 归档/软件包成员清单（ZIP/APK/IPA/MSIX/AppX、DMG 或 PyInstaller
  可执行文件）：对提供的本地路径使用 `open_binary`；当其图与发现
  （findings）有助于回答问题时使用 `inspect_artifact`。PyInstaller
  CArchive 是应用层；bootloader 只是原生前缀。对大型清单先用
  `detail: "summary"`，再使用保留的清单视图查看选定成员的字段/页面。
  一个完整的小清单可能比额外的调用与 schema 更省。
  运行时选项是元数据，不是文件。
  紧凑交付仍会清点并哈希成员。
  参见 [Python 打包应用指南](https://github.com/morluto/rea/blob/main/docs/python-packaged-applications.md)。
- Apple 应用的 plist、Interface Builder、资源目录（asset catalog）
  或键控归档（keyed archive）资源：先 `open_bundle_resources`，
  再用选定的资源工具。这不需要 `CFBundleExecutable` 或深度提供方。
  资源会话没有可执行文件摘要或二进制快照；原生代码请使用 `open_binary`。
- Android APK 的代码、类、方法或传入引用：先 `inspect_android_package`，
  在其声明可用时再用聚焦的 Android 工具。
  归档成员清单仍走上述归档路由。
- 托管 PE/CLI 程序集：`inspect_managed_artifact`。
- 固件镜像：在其声明可用时使用 `inspect_firmware_regions`。
  当需要提取时使用 `extract_firmware`，并指定由调用者选择的
  新绝对输出目录。这些工具在 Linux 上使用调用者提供的
  Binwalk/Unblob；参见[固件指南](https://github.com/morluto/rea/blob/main/docs/firmware-analysis.md)。
- .NET NativeAOT PE/ELF：原生 Ghidra 分析。原生代码可以产出伪代码；
  可选的元数据恢复及其支持的主机/布局边界，请查阅
  `references/native-and-artifacts.md` 中的 NativeAOT 工作流。
- 原生程序行为、活跃调用、插桩（instrumentation）或命令运行效果：
  选择匹配的[原生运行时工作流](references/runtime-observation.md#native-runtime-questions)。
  `open_binary` 与 `trace_native_values` 确立静态事实；它们不观察执行。
  运行时工具具有各自的启动、附加（attach）、变更与清理效果，
  除非其自身的契约如此要求，
  否则不需要先建立静态会话。
- 用户已打开的自有浏览器页面：`list_browser_targets`。
- 需要由 Agent 执行的浏览器操作（点击、输入、导航）：
  使用带已声明动作的 `capture_browser_scenario`。
  连接/启动方式见[运行时观察](references/runtime-observation.md)，
  以及聚焦的后续浏览器工具。
- Web 应用的 Agent 环境（AgentEnv bundle）：录制前先阅读
  [environments](references/environments.md)；它通过
  `capture_browser_scenario` 录制，并用 `export_environment_bundle` 写出 bundle。
- Fiddler Everywhere 流量或原生 `.saz` 捕获：阅读
  [Fiddler 工作流](references/runtime-observation.md#fiddler-everywhere-traffic-debugging)。
  用 `inspect_web_network_capture` 与 `format: "saz"` 检查已保存的 SAZ；
  实时流量请连接 Everywhere 独立的 MCP 服务器。
- 已保留的 HAR/SAZ/原生 mitmproxy/aioquic qlog 捕获：
  `inspect_web_network_capture`。在有用时选择原始记录序号；
  检查生产者字段与字节/数字附属文件（sidecar），
  不要抓取已记录的 URL，也不要声称实时归属。
  HAR/SAZ/qlog 旧生代堆由 `REA_CAPTURE_DECODER_OLD_GENERATION_MIB`
  控制（默认 192 MiB，下限 8，最大 16384），在 REA 启动处设置。
  宿主内存与 `NODE_OPTIONS` 无法抬高它。确切的上游配置与凭据排除项
  参见[历史捕获文档](https://github.com/morluto/rea/blob/main/docs/web-network-captures.md)。
  Qlog 支持从 aioquic 1.5.0 JSON 0.3 开始；流覆盖与端点丢包声明
  不会恢复报文主体，也不能确立网络丢包。优先使用 detail summary，
  然后使用 kind qlog 的 trace/stream 页面；为 contribution/range
  页面选择一条 trace、流 ID 与方向。事实层面保留
  “选择之前的全部已记录事件”范围。其他 qlog 布局与 PCAP 关联
  不受支持。
- 用户已打开的自有 Electron 运行时：`list_electron_targets`。在尝试 electron-main Inspector 之前，先用 `inspect_electron_fuses` 检查打包 fuse；`EnableNodeCliInspectArguments` 被禁用意味着应用会忽略 `--inspect`。
- 数据包字段发现：在选择 `inspect_packet_capture` 的字段之前，
  先用 `inspect_packet_fields` 搜索已安装的协议与字段名称/类型。
  查询/分页相关记录；注册记录不能证明观察到的流量。
- 已记录的数据包捕获：使用选定的 TShark 字段、显示过滤器与
  decode-as 规则进行 `inspect_packet_capture`。需要 Linux、
  util-linux prlimit 与 `REA_TSHARK_COMMAND`；参见
  [捕获指南](https://github.com/morluto/rea/blob/main/docs/packet-captures.md)。
  数据包限制在过滤之前统计输入数据包。输出默认 50 个匹配帧；
  后续页使用 `match_offset` / `match_limit`，或用显式 null 限制
  获取完整匹配输出。跨页面保留源摘要。这不会执行实时捕获。
  地址/DNS/SNI/协议摘要请使用带 MCP detail summary 的
  `inspect_pcap_capture`，然后使用保留的 kind pcap 页面。
  需要 Wireshark 4.x tshark 与 capinfos，并在 Linux 上用 prlimit
  或在 Windows 上用 Job Objects；参见
  [数据包摘要](https://github.com/morluto/rea/blob/main/docs/pcap-analysis.md)。
  为地址页面选择确切的 DNS 问题；分页耗尽不能证明网络完整性。
  这读取的是记录，不会采集流量。
- 解码器发现：`inspect_signal_decoders` 搜索已安装的解码器 ID
  或选定的解码器帮助，包括通道与选项。在确定设置之前
  查询并分页相关细节；这不会扫描硬件。
- 已记录的逻辑/信号轨迹：使用显式解码器、通道与协议设置进行
  `decode_signal_recording`。在配有 util-linux prlimit 的 Linux 上，
  通过 `REA_SIGROK_COMMAND` 提供 sigrok-cli 0.7.2；参见
  [记录指南](https://github.com/morluto/rea/blob/main/docs/signal-recordings.md)。
  输出默认 50 行字面行；选择注解类别并用 `line_offset` / `line_limit`
  分页，或用显式 null 获取全部剩余输出。窗口计数是显示行数，
  不是注解数或样本数。跨页面保留源摘要。这读取的是已有文件；
  它不会采集硬件信号。
- 显式本地 WebAssembly 产物：`inspect_wasm_artifact`。通过
  `REA_WABT_BIN_DIRECTORY` 提供 WABT 1.0.42；保留确切的
  字节/工具身份与解码后的 WAT。显式选择 JavaScript glue 与
  候选路径，并保留 URL/路径的歧义性。不进行隐式抓取或目标执行；
  WAT 不是原始源码。参见 [WASM 指南](https://github.com/morluto/rea/blob/main/docs/wasm-artifacts.md)。
- 显式本地 Android APK（或 ZIP/AAB）签名：`inspect_apk_signature`。
  优先使用其摘要或选定的 signer/digest/lineage 页面；保留完整证据，
  后续查询使用 kind 为 `apk-signature` 的 `inspect_analysis_view`。
  报告存在哪些方案（v1 JAR、v2、v3、v3.1）、每个签名者的
  证书 SHA-256 指纹（含 v1，取自其 PKCS#7 块）、v3 密钥轮换
  lineage、source stamp，以及每个已签名摘要是否仍与
  字节一致（自洽性）。这是身份与完整性，
  不是信任或真实性裁定。参见 [APK 签名指南](https://github.com/morluto/rea/blob/main/docs/apk-signature.md)。
- 显式本地 EVM 字节码载体：使用调用者选择的 `raw` 或 `hex` 编码进行
  `inspect_evm_interface`。自有 worker 的截止时间是 `timeout_ms`
  （默认 30000 ms，范围 1..2147483647，见下一次调用）。它不会
  抬高固定的字节、地址空间或 CPU 配额。保留载体/解码摘要，
  并将选择器、参数字符串与可变性视为推断的候选；
  这不执行链上查询或目标执行。要获得不带 hex 或重复 stdout 的
  完整推断接口，先发现支持情况并选择 `detail: "summary"`；
  完整证据仍以原始身份保留。使用返回的 `parent_evidence_id`
  获取精确函数或 `bytecode_hex`/stdout/stderr 页面。
  候选覆盖不能证明接口完整。参见
  [EVM 字节码指南](https://github.com/morluto/rea/blob/main/docs/evm-bytecode.md)。
- 内嵌的 Go 编译器、模块或构建设置元数据：使用显式本地文件
  进行 `inspect_go_binary`。这一内置免目标检查不需要
  Go 安装或反汇编器。保留原始模块字节与源码范围；
  缺少元数据不能证明二进制不是 Go，
  且未解析的文本记录保持显式。参见
  [Go 二进制指南](https://github.com/morluto/rea/blob/main/docs/go-binaries.md)。
- 内嵌的 CUDA/HIP 代码对象：`inspect_gpu_code_objects`；先清点目标，
  再解码选定的载荷并查询保留的 GPU 证据。
- 内嵌的 GGUF 或 safetensors 模型声明：使用显式本地文件进行
  `inspect_model_artifact`。默认只哈希头部，整体文件身份未知；
  `hash: "full"` 会额外读取全部权重以计算 SHA-256。MCP 返回
  保留的摘要；可选的 `view` 在初始调用中选择一页。批量元数据键、
  张量名或类型总数、选定字段与页面，请使用 kind 为
  `model-artifact` 的 `inspect_analysis_view`。保留头部范围的索引
  与数组预览的省略；不要从声明的架构或张量类型推断模型行为。
  参见
  [模型文件指南](https://github.com/morluto/rea/blob/main/docs/model-artifacts.md)。
- 来自 `global-metadata.dat` 的 Unity IL2CPP 名称、成员归属与字符串
  字面量：使用显式本地文件进行 `inspect_il2cpp_metadata`，MCP 默认
  返回紧凑计数。通过 `inspect_analysis_view` 与返回的
  `parent_evidence_id` 查询 sections、images、types、methods、
  fields、properties、events、parameters 或 string_literals，使用
  精确过滤器、批量索引与选定字段。参数接受 `method_indices`，避免
  扫描全部参数页面。历史证据中缺失的集合保持未知。支持版本 24、
  27、29、31 与 39；不运行 Unity、IL2CPP 二进制或反汇编器。无法
  识别的 magic（可能已加密）与其他版本不受支持。可选的匹配
  `binary_path` 可启用静态原生地址与类型引用；用索引或地址/状态
  查询 `method_addresses`，保留每个共享方法体（shared-body）方法与
  两个产物身份。没有链接的二进制时，原生计数保持未知。字节模式
  回退属于推断；不证明运行时行为或同构建配对。参见
  [IL2CPP 元数据指南](https://github.com/morluto/rea/blob/main/docs/il2cpp-metadata.md)。
- 内嵌的 cargo-auditable Rust 依赖元数据：使用显式本地 ELF、PE 或
  thin Mach-O 文件进行 `inspect_rust_binary`。这一内置
  免目标检查不需要 Rust 安装或反汇编器。保留
  包顺序、依赖索引与 section 文件范围。缺少
  `.dep-v0` section 是空元数据，不是二进制没有依赖的证明。
  rustc commit hash 是从只读的 `/rustc/<40-hex>/` 路径做出的推断。
  要查看选定的 crate，在首次调用中使用
  `view: {collection: "packages", names: [...],
  fields: ["name", "version", "source"]}`；显式包含
  `dependencies` 以获得直接索引引用。用 `detail: "summary"` 获取计数
  与范围，或对后续过滤使用保留的 `inspect_analysis_view`
  Rust 包/边页面。保持完整父证据可访问；CLI 紧凑
  交付需要 `--evidence_output`。
  参见
  [Rust 二进制指南](https://github.com/morluto/rea/blob/main/docs/rust-binaries.md)。
- PE Authenticode 证书表：使用显式
  本地 PE32/PE32+ 文件进行 `inspect_pe_certificates`。这一内置免目标
  检查不需要
  Windows SDK。保留 WIN_CERTIFICATE 范围、类型、载荷 SHA-256，以及
  PKCS#7 签名者/X.509 身份字段，包括签名者使用该形式时的
  `subject_key_identifier_hex`。缺少 security directory 是对该表缺失的
  观察，不是镜像在所有目录意义上均未签名的证明。
  签名不会被验证。参见
  [PE 证书指南](https://github.com/morluto/rea/blob/main/docs/pe-certificates.md)。
- PE 导入与延迟加载表：使用显式
  本地 PE32/PE32+ 文件进行 `inspect_pe_imports`。这一内置免目标检查
  不需要
  Windows SDK。保留 DLL 名称、具名与序号函数、ILT/IAT RVA、
  delay-load 描述符，以及标准导入表的 pefile import hash。
  缺少导入目录是对该表缺失的观察，不是
  镜像从未通过其他表导入 API 的证明。边界快照
  与已加载的 IAT 内容仍未被观察。参见
  [PE 导入指南](https://github.com/morluto/rea/blob/main/docs/pe-imports.md)。
- PE TLS 回调与加载配置：使用
  显式本地 PE32/PE32+ 文件进行 `inspect_pe_load_config`。这一内置
  免目标检查不需要
  Windows SDK。以字符串形式保留回调 VA 及其 RVA、文件偏移
  与所在 section，以及大小覆盖的 security cookie、SafeSEH、CFG、
  EH-continuation 与 XFG 字段。Guard 标志的缓解声明是推断
  的链接器声明，不是已强制执行的证明。缺少目录是观察到的
  声明缺失。参见
  [PE 加载配置指南](https://github.com/morluto/rea/blob/main/docs/pe-load-config.md)。
- ELF note 表：使用显式本地 ELF32/ELF64
  文件进行 `inspect_elf_notes`。这一内置免目标检查不需要反汇编器。
  保留 PT_NOTE 与 SHT_NOTE 范围、所有者、类型、描述符 SHA-256，
  以及 GNU build-id 或 ABI-tag 字段。缺少表是对那些
  声明缺失的观察，不是镜像从未携带 note 的证明。参见
  [ELF notes 指南](https://github.com/morluto/rea/blob/main/docs/elf-notes.md)。
- Apple `.ips` 崩溃报告：使用显式本地
  文件进行 `inspect_apple_ips`。这一内置免目标检查不需要
  Xcode、atos 或 pwntools。保留首行元数据、作为字符串的
  `bug_type`、进程与异常事实、无损整数寄存器、usedImages UUID，以及
  文档化的分类匹配。只有 `bug_type` 为 `"309"` 才会产生
  崩溃主体；其他类型（包括 `"288"` stackshots）不返回崩溃结果。
  已打开的 Mach-O 与 dSYM UUID 连接仍未被观察。参见
  [Apple IPS 指南](https://github.com/morluto/rea/blob/main/docs/apple-ips.md)。
- Linux 内核模块元数据：使用显式本地
  ELF32/ELF64 可重定位文件进行 `inspect_kernel_module`。这一内置
  免目标检查不需要
  Linux 主机或 `modinfo`。保留 `.modinfo` 键顺序与重复键、
  `__versions` CRC 十六进制、section 文件范围，以及附加签名
  尾部的 PKCS#7 SHA-256。当 section 名称已知时，缺少 section 是观察到的缺失，
  不是模块从未携带该元数据的证明。
  `struct module` 不会被解码。签名不会被校验。gzip、xz 与
  zstd 容器不受支持；请用外部编解码工具解压到单独文件，
  再检查解压后的 `ET_REL` 镜像。参见
  [内核模块指南](https://github.com/morluto/rea/blob/main/docs/kernel-modules.md)。
- CPython 3.7–3.13 的 `.pyc` 头部、嵌套 marshal 代码对象与字节码
  身份：使用显式本地文件进行 `inspect_python_pyc`。这一内置
  免目标检查不需要 Python 安装。保留 magic、
  PEP 552 哈希或 mtime/size、嵌套名称与字节码 SHA-256。字节码
  不会被反编译，解码出的头部也不能证明对应的 `.py` 存在。参见
  [CPython pyc 指南](https://github.com/morluto/rea/blob/main/docs/python-pyc.md)。
- Erlang BEAM IFF 容器：使用显式本地
  `.beam` 文件进行 `inspect_erlang_beam`。这一内置免目标检查
  不需要 Erlang
  安装。保留 chunk 名称、atom 顺序、export/import/lambda 表，
  以及 Code 头部。对选定事实，优先使用 `detail: "summary"` 加一个
  `beam` 视图（collection、names/indices、fields 与分页），
  并保留完整证据。CLI 摘要需要 `--evidence_output`。缺失的表计数
  保持 null；已解码的空表计为零。字节码不会被执行。参见
  [Erlang BEAM 指南](https://github.com/morluto/rea/blob/main/docs/erlang-beam.md)。

- 显式本地 SQLite 数据库快照：`inspect_sqlite_database`。检查时
  需要 Node.js 24.x >=24.15 或 26+ 提供原生 SQLite 限制。先读取
  schema（默认紧凑清单），或在需要行数据时选择确切的普通表
  与 `columns`。默认为选定表的 schema 与 20 行；要获取完整的存储
  schema，请请求 `schema_scope: "database"`。同时保留数据库与
  已存在的同目录 WAL 的身份；行样本会报告截断且顺序未定义。使用
  静止（quiescent）快照，而不要假设活着的数据库/WAL 对是原子复制的。
  参见 [SQLite 指南](https://github.com/morluto/rea/blob/main/docs/sqlite-databases.md)。
- 显式 Linux ELF 文件，用于离线布局、符号、重定位或静态
  缓解证据：`inspect_binary_layout`。这一免目标操作使用
  调用者提供的 pwntools，不打开反汇编器数据库。保留其
  原始位置与推断/覆盖限制；参见
  [离线二进制指南](https://github.com/morluto/rea/blob/main/docs/binary-diagnostics.md)。
- 提供的 Linux x86-64 ELF core：`inspect_recorded_crash`。读取每个已记录
  线程、原始 note 与源绑定寄存器，不打开活动目标。
  历史 PID 不能选择活动进程。仅当仅凭 core 的映射候选有帮助时
  才请求 `include_debugger_context`；参见
  [已记录崩溃指南](https://github.com/morluto/rea/blob/main/docs/recorded-crashes.md)。
- PE 资源类型/名称/语言树与静态图标组引用：
  使用显式路径进行 `inspect_pe_resources`。这一可移植操作不需要
  活动目标或引擎；不透明载荷保留文件范围与 SHA-256。
- PE 导出目录与 ELF 动态符号导出：使用显式路径进行
  `inspect_native_exports`；可移植，不需要活动目标或引擎。
- 原生可执行文件、库或分析数据库：先 `open_binary`，然后
  直接使用聚焦的分析工具；当选定提供方可提供且元数据或
  清单上下文有用时调用 `binary_overview`。

对于已有的 IDA MCP 配置，对原始
输入二进制使用 `open_binary` 并指定 `provider_id: "ida"`；
不要传入 `.idb` 或 `.i64` 数据库。
旧版附加（attached）配置通过 SHA-256 绑定已在 GUI 中打开的输入，
并保持其数据库打开。新版无头（headless）配置会创建并关闭一个
自有私有数据库，不保存。安装与注册复用
[mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)；参见
[IDA 提供方指南](https://github.com/morluto/rea/blob/main/docs/ida-provider.md)。
打开后直接进行 `analyze_function`、伪代码或函数/字符串搜索；
IDA 不提供 `binary_overview`。在组合更大工作流时请考虑会话可用性。
现代直接调用者与不支持的档案（dossier）切面保持未知；
实时 IDA 结果不会从快照回放。

配置 `REA_KUNA_COMMAND` 后，`provider_id: "kuna"` 可从 Kuna 缓存的
全程序导出中回答过程列表、查找、伪代码、汇编与
`analyze_function`。调用者/被调用者使用会话共享的独立无主体
（body-free）图；`xrefs` 返回精确地址的传入位置并过滤转发
别名。这些查询与清单查找不会触发 C 导出。间接
目标保持未知，并可能使关系覆盖不完整。引用
缓存在关闭时过期；新的 CLI 进程会重复原生引用遍历。
类型化引用、CFG、原始内存工具与注解仍不受支持。冷的首次
回答可能来自单函数运行（其局限性会说明）；汇编
要等导出完成。对于伪代码与汇编，`raw_result.source` 会指出
缓存的 `.c`/`.asm` 文件与字节区间，你可以直接搜索它而不必
逐函数调用。参见
[Kuna 提供方指南](https://github.com/morluto/rea/blob/main/docs/kuna-provider.md)。

如果用户只说“我的应用”而没有名称、路径，或没有已为
此任务选定的目标，请在搜索产物之前询问是哪个应用。无关的
已保存报告中的路径和附近的测试 fixture 不能代表用户的目标。
尽可能把一个真实的人类可读应用名解析为一个明确的已安装产物；
匹配有歧义时询问。永远不要替用户选择示例应用。

在免目标会话中，对任何其分析工具作用于活动目标的
归档/软件包或原生目标，使用 `open_binary` 绑定。不要调用
未声明的工具；用 `{}` 检查 `binary_session` 及其
`result.tool_availability` 获取可用性原因与补救方法。将每个
组的 `names` 展开为条目，继承清单级客户端要求，
除非该组覆盖了它们。在其关闭效果与注解词表中，
列出的标志为真，省略的已知标志为假。分组名称并集
就是完整的工具清单；规范工具 schema 请使用 `tools/list`。
提供方候选事实描述可能的提供方，而顶层会话
能力描述当前路由，`analysis_provider_binding` 指明
选定的提供方。不要把这些范围当作可互换的。

对于大型原生目标上的 Ghidra 启动超时，在放弃深度分析或重复
同样的冷导入之前，先遵循
[deadline recovery](references/native-and-artifacts.md#ghidra-startup-deadline-recovery)。
默认 330 秒可配置；更改服务器的环境需要新的
REA 进程。

## 以摘要优先方式工作

从默认结果开始，使用其内联证据与图上下文。
对于大小未知或很大的 JavaScript 应用或 ELF 布局，
先用 `"detail": "summary"` 调用 `analyze_javascript_application` 或
`inspect_binary_layout`，再用 `inspect_analysis_view` 检查保留的
`parent_evidence_id`。在 MCP 上，`analyze_function` 无需标志即为
摘要优先：其默认回复就是摘要，完整档案（dossier）保持
在 `parent_evidence_id` 下供切面分页。将该 ID 作为
`retained-evidence` 引用传给 `compare_functions`，或传入
`match_native_functions` 的 `left_observations`/`right_observations`；
只有当档案必须内联传输时（如 `build_call_path` 所要求的），
才请求 `"detail": "complete"`。
先分页模块身份并选择返回的 `node_id`，再请求某个条目；
单个文件路径可以代表多个图角色。不要在没有更改输入或
解决阻碍的情况下重复相同的分析或被拒绝的调用。
当生命周期变化使该状态有意义时，重新检查会话状态。
只有当返回的结果留下某个具体问题未回答时，
才进行聚焦的后续操作。

如果 MCP 报告 `resource_constraint` 且 `details.resource: "transport"`，
用其报告的同会话证据引用调用 `inspect_analysis_view`，获取
摘要、某个 section/模块或一个稳定页面。一旦种子已知，
就使用 `trace_application_feature`，或调用 `export_evidence_bundle`
把完整会话写到选定路径。分析在台账（ledger）中仍是完整的；
不要仅仅为了再次请求同样过大的响应而重复分析。
完整的 CLI JSON 输出也会流式返回，而不依赖单个 MCP 帧。

当保留的父 ID 未知时，用 `detail: "summary"` 与精确过滤器
（按操作、目标 SHA-256、分析配置摘要或规范过程地址）
调用 `get_evidence_bundle`。选择其返回的证据 ID 用于下一个视图，
而不是请求完整 bundle。
`retention: "complete-record"` 表示整条记录已存储；原生
值流截断与未知元数据仍要分开对待。对于已导出的
可移植 bundle，使用包含 `path`、`detail: "summary"` 与相同
`filters` 的 JSON 运行 `rea inspect-evidence-bundle`。读取该文件
仍需要在本地内存预算内验证其全部内容。

客户端也可能在没有 REA 传输错误的情况下截断一次成功的工具结果。
把该预览视为不完整；当需要完整记录时，使用保留的父 ID
获取更小的视图或导出。不要把预览当作规范的 JSON 来解析，
也不要重复生产者。对于 JavaScript，在深入大型图之前先阅读
[module-view 与 trace 配方](references/javascript-applications.md)；
即使经过摘要分析，一次宽泛的双向 trace 也可能扩展无关的
包含关系。

每个结论都必须区分观察、推断与未知。引用
证据 ID，保留局限性与不完整覆盖，绝不能暗示
静态分析观察到了执行。运行时请求会执行声明的
目标与生命周期；不要把目标或动作扩大到这些字段之外。

在用户请求的调查范围内，直接调用可用的分析工具
即可。REA 不需要权限授予或逐调用批准标志。
Agent 客户端可以独立要求批准。遵循声明的请求
范围与宿主实际的访问要求；观察到客户端策略拒绝时
使用恢复指南。

## 规划更大范围的调查

对于跨越多个功能或子系统的请求，使用分阶段工作流：

1. 把请求转化为问题清单，以及每个答案所需的证据。在再次索要
   信息之前，先从对话与工作区中确定目标身份与约束。
2. 检查当前 REA 会话、产物身份、已保存的分析数据库、
   书签与既有证据。复用匹配的状态；不要打开重复
   会话或重复相同的分析。
3. 从最小的有用概览或清单开始。对每个问题，从其入口出发，
   穿过相关数据与状态变化，直到其结果。
   围绕特定假设批量执行相关操作，只有当
   返回的证据留下具体缺口时才扩展。
4. 当代码旁的打包资源与配置影响问题时，一并检查它们。
   使用格式感知的清单与解析器；不要仅凭文件名、字符串或
   布局推断行为。
5. 用结论所需的证据类型来佐证结论。只有当静态证据无法回答问题、
   且所需宿主运行时与 OS 访问可用时，才使用运行时观察。
   对 JavaScript 行为，
   通过可用的浏览器、Electron 或进程捕获工作流对实际应用运行探针。
6. 把工作分解为独立的问题。当并行 worker 可用且问题彼此不依赖时，
   分配不同的范围，让 worker 指向既有证据，并要求它们返回来源、
   结论与未解决的缺口。否则按顺序工作。
7. 维护一份简洁的发现台账，把每个结论与证据 ID、
   置信度/证据类型、搜索边界及剩余未知项关联起来。更新
   共享索引或调查报告，让后续轮次可以复用结果。

结束之前，回顾原始清单。根据证据把每个问题标记为
已回答、部分回答或未解决；让有界的否定搜索保持有界，
并且在必答问题尚未解决时，不要把一次宽泛的调查
描述为已完成。

## 只阅读相关指南

- 原生二进制、托管程序集、归档与提取：
  [references/native-and-artifacts.md](references/native-and-artifacts.md)
- ASAR、已解包的 JavaScript、功能追踪与版本比较：
  [references/javascript-applications.md](references/javascript-applications.md)
- Android APK 声明、类、方法与静态引用：
  [references/android-applications.md](references/android-applications.md)
- 原生插桩、调试器与进程捕获；浏览器/Electron
  观察；静态/运行时比较：
  [references/runtime-observation.md](references/runtime-observation.md)
- 证据分页、比较、残留未知项与验证：
  [references/evidence-workflows.md](references/evidence-workflows.md)
- Web 应用的 Agent 环境（AgentEnv bundle），从
  运行实例或 HAR 录制：
  [references/environments.md](references/environments.md)

## 完成任务

用通俗语言解释发现，并将其与返回的证据关联起来。当
用户要求构建某物时，使用普通的编码工具，并把观察到的
行为与设计选择分开。调查完成后，用
`close_binary` 关闭已打开的原生会话。
