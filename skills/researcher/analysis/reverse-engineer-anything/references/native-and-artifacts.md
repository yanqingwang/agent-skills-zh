> **中文汉化版** · 上游：[morluto/rea](https://github.com/morluto/rea) · 原文件：`.agents/skills/reverse-engineer-anything/references/native-and-artifacts.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 原生、托管与打包产物

在同一 MCP 连接上做发布对比时，保留每个目标的 `list_procedures` Evidence，
并在切换目标或 `close_binary` 之后复用其确切 ID。
若要交接或开启新进程，导出完整 bundle 并在新位置导入，包括其 source closure。
`reset_investigation` 会显式清除保留记录；可选的 `save_path` 在清除前对其做检查点。
`match_native_functions` 配对唯一的精确名称，并在提供时配对完整的已观测函数体字节。
同上下文的可选 `list_names`、`procedure_info`、`read_bytes` 结果与既有的
`analyze_function` 档案可复用为 `left_observations`/`right_observations`；
MCP 的 `analyze_function` 摘要回复以其 `parent_evidence_id` 作为
`retained-evidence` 引用参与配对，而不是摘要本身。不要为了配对而把每个函数都反编译。
其摘要保留一个父 Evidence，供 `inspect_analysis_view` 的
`function-matches` 集合 `matches` 与 `functions` 使用。
按列选取、批量传 ID 并分页读取单个事实；别名保持未解析。
未配对的观测不能证明存在新增/删除。已配对的档案对包含
`compare_functions` 所需输入；否则只分析选定的函数对。

用 `find_changed_behavior` 汇总已完成的对比，选择每个对比的确切
`retained-evidence` ID，而不是重发完整记录。
内联的对比 Evidence 仍然接受。引用只属于当前服务器：交接后请导入
原始 bundle 及其 source closure。不要用档案 ID 或摘要视图替代。
静态差异仍是行为候选，除非另行观测，运行时行为保持未知。

若被拒是因为匹配表示超限，检查 `details.limit`，用 `update_analysis_settings`
调高 `native.matching_representation_bytes`，然后原样重试该 MCP 请求。
CLI 启动种子：`REA_NATIVE_MATCHING_REPRESENTATION_BYTES`。
默认 96 MiB；策略范围是 1 字节到 1 GiB，且不约束进程 RSS。
保留完整清单：拆分会改变全局的名称/函数体唯一性。

## Apple 应用资源

对选定的应用路径使用 `open_bundle_resources`，然后用 `inspect_plist`、
`decode_interface_builder`、`inspect_asset_catalog` 或 `inspect_keyed_archive`。
资源会话只读取应用本身，不解析 `CFBundleExecutable`，也不启动深度 provider。
保留 `resource_root` 来源信息、已报告的逐资源哈希，以及空（null）的可执行身份；
目录路径不是可执行文件的摘要。在关闭或切换 root 之前先导出已保留的 Evidence。
二进制分析快照在此不适用。用 `open_binary` 切换到可执行文件分析，
用 `close_binary` 释放任意一种会话。

对应的四个 CLI 命令直接接受应用路径。对应用内部的归档文件，
使用 `inspect-keyed-archive APP_PATH RELATIVE_ARCHIVE_PATH`。
plist 与编译后资源/Interface Builder 工具的主机要求仍然适用；
仅资源的会话不代表 provider 可用。

## 桌面应用安装目录

当提供了安装目录且其运行时未知时，用 `inspect_desktop_application` 传入其绝对路径。
默认的 MCP 摘要投递会保留完整 Evidence。用 `inspect_analysis_view`
（kind `desktop-application`）读取 `files`、`omissions`、`candidates`、
`components` 或 `next_probes`，选择确切路径、批量文件/遗漏 ID 或类别，
并只取需要的字段和页。摘要中的 `probe_issues` 保留计数与有界预览。
选择 `has_issues: true` 的文件并取 `path`、`read_status`、`issues` 字段，
可直接拿到确切失败原因；预览文本只是展示数据，`file_id` 才用于选取完整事实。
保留来源覆盖范围、读取区间标识与未知项；目录快照标识不是每个文件内容的摘要。
组件路径标记不能证明运行时存在。需要紧凑的 CLI 输出时，使用
`inspect-desktop-application PATH --detail summary --evidence_output BUNDLE`。
另见 [桌面应用安装](https://github.com/morluto/rea/blob/main/docs/desktop-applications.md)。

## 发布暴露面

当问题是对已发布的 `.app`、安装目录、ASAR 或可执行文件做静态分析能还原什么时，
使用 `audit_release_exposure`（`rea audit-release-exposure PATH`）。
每个检查项有稳定 id、状态、背后的观测以及固定的修复建议。
未知与未评估的检查项也保留在报告中。该报告不能证明应用是安全的。

`text.credential_markers` 只报告规则 id 和位置。
匹配到的字节、预览、长度及匹配字节的哈希一律省略。

`native.hardening`、`macho.hardened_runtime` 和 `android.manifest` 不在此评估范围内。
它们的下一步探测分别是 `inspect_binary_hardening`、`inspect_signature`
和 `inspect_android_package`。

另见 [发布暴露面](https://github.com/morluto/rea/blob/main/docs/release-exposure.md)。

## Go 构建元数据

当问题涉及内嵌的编译器版本、模块/依赖版本、本地替换（replace）、构建设置，
或未以 NUL 结尾打包的静态 Go 字符串字面量时，对明确的本地 ELF、PE 或
Mach-O 文件（universal 文件需要 `architecture`）使用 `inspect_go_binary`。
传入 `include_string_literals: true`（`--include-string-literals`，
可选 `max_string_literals` / `--max-string-literals`）可从只读数据中恢复
有界的、推断出的按字对齐的 `(ptr, len)` UTF-8 字符串切片，
并通过 `go` 的 `string_literals` 视图分页读取。
无需 `open_binary`、Go 安装或运行目标。等价的 CLI 命令是 `inspect-go-binary PATH`。
保留产物 SHA-256、原始文件区间、带框架的模块字节以及每一条未解析的模块文本行。
记录缺失是未知项，不能证明它不是 Go 二进制；已观测的元数据不能自证其声明，
静态 `(ptr, len)` 字符串恢复不包含编译器内联到栈/立即数的字符串，
也不能证明运行时可达性。函数、源码与类型恢复是另一个原生分析问题。

## 模型文件

对本地 GGUF v2/v3 与 safetensors 声明使用 `inspect_model_artifact`
（`inspect-model-artifact PATH`），无需模型运行时。
仅头部模式不读取权重，也不建立整文件身份。
`hash: "full"` 会显式流式读取全部字节。
保留的 `model-artifact` 视图可对 `metadata`、`tensors` 及派生的 `types` 分页，
支持精确批量过滤与字段选择。数组保留带类型的计数与八元素预览；
省略的值、未知类型与运行时行为都显式标注。
另见 [模型文件](https://github.com/morluto/rea/blob/main/docs/model-artifacts.md)。

## IL2CPP 元数据

当问题涉及程序集镜像（assembly images）、名称、成员归属、字符串字面量、
命名空间或索引范围时，对明确的本地 Unity `global-metadata.dat`
（版本 24、27、29、31 和 39）使用 `inspect_il2cpp_metadata`。
无需 `open_binary`、Unity 安装或运行目标。
等价的 CLI 命令是 `inspect-il2cpp-metadata PATH`。
MCP 默认返回计数并保留完整 Evidence。通过 `inspect_analysis_view` 查询
`sections`、`images`、`types`、`methods`、`fields`、`properties`、`events`、
`parameters` 或 `string_literals`；使用精确名称、批量索引与选定字段。
行索引以产物 SHA-256 和集合为作用域；分页偏移量按过滤后的匹配数计算。
`parameters` 支持批量 `method_indices`，可直接读取某个方法的参数。
没有成员集合的历史报告保留未知计数，而不是空清单。
保留产物 SHA-256 与索引位宽。无法识别的魔数可能意味着已加密，
属于不支持的情况，而不是已被解密。把名称关联到 `GameAssembly` 或
`UnityFramework` 的代码地址仍是另一个原生分析问题。
另见 [IL2CPP 元数据](https://github.com/morluto/rea/blob/main/docs/il2cpp-metadata.md)。

## Rust 依赖元数据

当问题涉及嵌入在 `.dep-v0`（Mach-O: `__DATA,.dep-v0`）中的
cargo-auditable crate 清单时，对明确的本地 ELF、PE 或 Mach-O
（universal 文件需要 `architecture`）使用 `inspect_rust_binary`。
无需 `open_binary`、Rust 安装或运行目标。
等价的 CLI 命令是 `inspect-rust-binary PATH`。
保留产物 SHA-256、包顺序、依赖索引与该 section 的文件区间。
section 缺失表示元数据为 null，不能证明该二进制没有依赖。
被省略的包类型保持为 null。rustc 提交哈希是从只读的 `/rustc/<40-hex>/`
路径推断的，其本身不能确定编译器身份。
另见 [Rust 二进制](https://github.com/morluto/rea/blob/main/docs/rust-binaries.md)。

## PE Authenticode 证书表

当问题涉及 Authenticode 证书表、WIN_CERTIFICATE 类型，或内嵌 PKCS#7
签名者与 X.509 身份字段时，对明确的本地 PE32/PE32+ 镜像使用 `inspect_pe_certificates`。
无需 `open_binary`、Windows SDK 或运行目标。
等价的 CLI 命令是 `inspect-pe-certificates PATH`。
保留产物 SHA-256、表文件区间、载荷哈希、原始有效期时间的书写形式，
以及在签名者使用该形式时的 `subject_key_identifier_hex`。
`IMAGE_DIRECTORY_ENTRY_SECURITY` 目录缺失表示观测到该表不存在，
不能证明镜像在所有 catalog 或 overlay 意义上都未签名。
签名、证书链、时间戳与 Authenticode 摘要覆盖范围仍未观测。
另见 [PE Authenticode 证书表](https://github.com/morluto/rea/blob/main/docs/pe-certificates.md)。

## PE 导入与延迟加载表

当问题涉及导入的 DLL 与函数名、序号、延迟加载描述符，或 pefile 导入哈希时，
对明确的本地 PE32/PE32+ 镜像使用 `inspect_pe_imports`。
无需 `open_binary`、Windows SDK 或运行目标。
等价的 CLI 命令是 `inspect-pe-imports PATH`。
保留产物 SHA-256、目录文件区间、原始 DLL 书写形式与 ILT/IAT RVA。
`IMAGE_DIRECTORY_ENTRY_IMPORT` 目录缺失表示观测到该表不存在，
不能证明镜像从未通过其他表或 overlay 导入 API。
边界快照、已加载的 IAT 内容与导出转发解析仍未观测。
另见 [PE 导入与延迟加载表](https://github.com/morluto/rea/blob/main/docs/pe-imports.md)。

## Windows Shell Link 快捷方式

当问题涉及记录的目标路径、参数、工作目录、图标位置、卷序列号、网络共享名、
ExtraData 块或 Tracker droid 标识时，对明确的本地 `.lnk` 文件使用
`inspect_windows_shortcut`。无需 `open_binary`、Windows SDK、COM 或运行目标。
等价的 CLI 命令是 `inspect-windows-shortcut PATH`。
保留产物 SHA-256、FILETIME 原始十进制值、IDList 类型字节与 ExtraData 签名。
未知的 IDList 项与 ExtraData 签名保留原始字节及其 SHA-256；不做猜测。
Version-1 UUID 的 MAC 与时间戳值会标注为"派生"。
可选 section 缺失表示观测到该结构不存在。
另见 [Windows Shell Link 快捷方式](https://github.com/morluto/rea/blob/main/docs/guides/native/windows-shortcut.md)。

## PE TLS 回调与加载配置

当问题涉及通过 TLS 回调在入口点之前运行的代码，或加载配置中的安全 cookie、
SafeSEH、CFG、EH-continuation 与 XFG 声明时，对明确的本地 PE32/PE32+ 镜像
使用 `inspect_pe_load_config`。无需 `open_binary`、Windows SDK 或运行目标。
等价的 CLI 命令是 `inspect-pe-load-config PATH`。
保留产物 SHA-256、目录与回调数组的文件区间，以及以十六进制字符串表示的回调 VA。
声明 `Size` 之外的字段为 `null`。保护标志缓解措施带有 `evidence_kind: "inferred"`；
是否实际生效仍未观测。
另见 [PE TLS 回调与加载配置](https://github.com/morluto/rea/blob/main/docs/pe-load-config.md)。

## 二进制加固

当问题涉及 PIE 或 ASLR、NX、RELRO、栈保护或 FORTIFY 迹象、控制流标志或
剥离（strip）状态时，对明确的本地 ELF、PE 或 Mach-O 文件使用
`inspect_binary_hardening`。无需 `open_binary`、pwntools 或运行目标。
等价的 CLI 命令是 `inspect-binary-hardening PATH`。
universal Mach-O 文件会为每个 slice 返回一个镜像。
导入缺失是 `unknown`，不能证明保护被省略。
Authenticode 与 Mach-O 代码签名的行只报告存在性，不报告有效性。
`hardened_runtime` 保持未知，并指向 `inspect_signature`。
另见 [二进制加固](https://github.com/morluto/rea/blob/main/docs/binary-hardening.md)。

## ELF note 表

当问题涉及 PT_NOTE/SHT_NOTE 归属、GNU build-id 或 GNU ABI-tag 字段时，
对明确的本地 ELF32/ELF64 镜像使用 `inspect_elf_notes`。
无需 `open_binary` 或运行目标。等价的 CLI 命令是 `inspect-elf-notes PATH`。
保留产物 SHA-256、表文件区间、描述符哈希与原始归属名称的书写形式。
表缺失表示观测到这些声明不存在，不能证明镜像从未在其他容器中携带 note。
另见 [ELF note 表](https://github.com/morluto/rea/blob/main/docs/elf-notes.md)。

## ELF 与 Mach-O 初始化函数

当问题是哪些函数在 `main` 之前或退出时运行时，对明确的本地 ELF 或
Mach-O 镜像使用 `inspect_native_initializers`：涵盖 ELF 的 `DT_PREINIT_ARRAY`、
`DT_INIT`、`DT_INIT_ARRAY`、`DT_FINI`、`DT_FINI_ARRAY` 及旧式 `.ctors`/`.dtors`，
或 Mach-O 的 `__mod_init_func`、`__init_offsets` 与 `__mod_term_func`。
universal Mach-O 需传入 `architecture`。
等价的 CLI 命令是 `inspect-native-initializers PATH`。
PIE 槽位通过 RELATIVE、RELR 和 section 重定位解析，
Mach-O 槽位通过 chained fixups 解析。
保留每个条目的 `resolution`：`unresolved` 表示值未确立，
`unresolved_import` 指向一个外部符号。用 `offset` 和 `limit` 分页。
另见 [ELF 与 Mach-O 初始化函数](https://github.com/morluto/rea/blob/main/docs/guides/native/native-initializers.md)。

## ELF unwind 函数区间

当问题涉及在 `strip` 之后仍然保留的函数起始地址与长度、哪些函数有 LSDA，
或哪些区间没有精确符号时，对明确的本地 ELF32/ELF64 镜像使用
`inspect_elf_unwind_ranges`。无需 `open_binary` 或运行目标。
等价的 CLI 命令是 `inspect-elf-unwind-ranges PATH`。
保留产物 SHA-256、FDE 起止、所在 section、精确符号名、CIE 索引、
LSDA 与 personality。后续区间用 `offset` 和 `limit` 分页。
`.eh_frame` 缺失表示观测到该声明及 `PT_GNU_EH_FRAME` 不存在，
不能证明镜像没有函数。头部不一致属于限制项，不会丢弃已解码区间。
`.debug_frame` 只报告存在与否，不做解码。
CFA 指令只计数，不求值。间接 EH 指针不会被解引用。
另见 [ELF unwind 函数区间](https://github.com/morluto/rea/blob/main/docs/guides/native/elf-unwind-ranges.md)。

## Apple IPS 崩溃报告

当问题涉及崩溃元数据、异常与终止事实、线程、usedImages、无损寄存器或
已归档的崩溃类别时，对明确的本地 Apple `.ips` 文件使用 `inspect_apple_ips`。
无需 `open_binary`、Xcode、atos 或运行目标。
等价的 CLI 命令是 `inspect-apple-ips PATH`。
保留产物 SHA-256、作为字符串的 `bug_type`、大写的镜像 UUID，
以及超出 IEEE-754 范围的整数字面量。
只有 `bug_type` 为 `"309"` 才会产生崩溃正文；其他 DiagnosticReports 类型
不返回崩溃结果。传入 `join_path` 指定一个本地 Mach-O 或 dSYM，
可按 UUID 与架构将报告中的镜像匹配到 slice。
保留所选产物身份、slice 事实与未匹配原因；
已匹配的静态地址不会解析函数名或 dSYM 符号。
另见 [Apple IPS 崩溃报告](https://github.com/morluto/rea/blob/main/docs/apple-ips.md)。

## Linux 内核模块

当问题涉及 `.modinfo` 的 license、vermagic、alias、depends 或 parm 字符串、
`__versions` 符号 CRC，或附加的模块签名尾块时，对明确的本地 ELF32/ELF64
可重定位目标文件使用 `inspect_kernel_module`。
无需 `open_binary`、Linux 主机或 `modinfo` 程序。
等价的 CLI 命令是 `inspect-kernel-module PATH`。
保留产物 SHA-256、键顺序、重复键、CRC 十六进制值与 section 文件区间。
在 section 名称已知的前提下，section 缺失表示观测到其不存在，
不能证明模块从未携带该元数据。`.gnu.linkonce.this_module` 报告存在与否；
`struct module` 保持未知，因为其布局随内核版本变化。
`__ksymtab` 记录不做解码。PKCS#7 区间及其 SHA-256 属于观测结果；
证书、签名者与摘要覆盖范围仍未验证。尾块缺失不能证明模块在其他容器中未签名。
gzip、xz 和 zstd 整文件容器不受支持，并把 `external_decompression`
列为下一步探测：用外部编解码工具解压到单独文件，
再对该文件调用 `inspect_kernel_module`。
另见 [Linux 内核模块](https://github.com/morluto/rea/blob/main/docs/kernel-modules.md)。

## Linux 内核构建配置

当问题涉及内核版本或其配置方式时，对明确的本地内核镜像（`vmlinux` ELF、
裸 arm64 `Image`、x86 `bzImage`/`zImage` 或 `configs.ko`）使用
`inspect_kernel_build_config`。无需 `open_binary`、Linux 主机或 `extract-ikconfig`。
等价的 CLI 命令是 `inspect-kernel-build-config PATH`；传 `name` 可获取单个确切的
`CONFIG_*` 选项，用 `offset`/`limit` 对其余项分页。
保留 banner 版本、构建者与编译器、配置 SHA-256 与选项数量，
以及每个条目的值类型（`y`、`m`、`string`、`number`、`not_set`）。
只有当 `IKCFG_ST` 后紧跟有效的 gzip 成员且随后是 `IKCFG_ED` 时才接受该配置，
因此普通的 `IKCFG_ST` 字符串不构成配置。
带 `space: "inflated_payload"` 的偏移量是 bzImage 解压后载荷中的位置，
不是文件偏移。配置缺失只描述被搜索的字节；内核可能构建时未启用
`CONFIG_IKCONFIG`，或将其构建为模块。被截断的载荷属于"不完整"，而不是"不存在"。
无法解码、CRC 错误或包含非配置文本的带框 blob 标记为 `malformed`，而不是缺失。
xz、lz4、lzma、zstd、bzip2 与 lzo 载荷不受支持，并把 `external_decompression`
列为下一步：先用外部工具解压，再对结果调用 `inspect_kernel_build_config`。
另见 [Linux 内核构建配置](https://github.com/morluto/rea/blob/main/docs/guides/native/kernel-build-config.md)。

## CPython pyc 文件

当问题涉及头部魔数、PEP 552 源哈希或时间戳、嵌套 code-object 名称或
字节码身份时，对明确的本地 CPython 3.7–3.13 `.pyc` 使用 `inspect_python_pyc`。
无需 `open_binary`、Python 安装或运行目标。
等价的 CLI 命令是 `inspect-python-pyc PATH`。
保留产物 SHA-256、16 字节头部字段、嵌套代码名称与字节码 SHA-256。
字节码不做反编译。头部解码成功不能证明对应的 `.py` 存在。
另见 [CPython pyc 检查](https://github.com/morluto/rea/blob/main/docs/python-pyc.md)。

## Erlang BEAM 文件

当问题涉及 IFF chunk、原子（atom）名称、导出、导入、lambda 或 Code 头时，
对明确的本地 `FOR1`/`BEAM` 文件使用 `inspect_erlang_beam`。
无需 `open_binary`、Erlang 安装或执行字节码。
等价的 CLI 命令是 `inspect-erlang-beam PATH`。
保留产物 SHA-256、chunk 文件区间、从 1 开始的原子索引与原始原子书写形式。
缺失的可选表保持 null。只需要少量事实时，使用 `detail: "summary"`
配合 `beam` 视图，选择集合、精确名称/索引与字段；
后续页从 `parent_evidence_id` 或完整 Evidence bundle 读取。
同名导出保留每个 arity 与原始原子索引。CLI 摘要投递需要 `--evidence_output`。
null 表的计数与已解码的空表保持区分。
另见 [Erlang BEAM 文件](https://github.com/morluto/rea/blob/main/docs/erlang-beam.md)。

## SQLite 快照

对明确的本地数据库快照使用 `inspect_sqlite_database`，读取其 schema
以及某个确切普通表的可选行。它要求 Node.js 24.x（>=24.15）或 26+，
以使用原生 `DatabaseSync.limits` API。它同时会读取同目录已存在的 `-wal` 文件；
引用其结果时请保留两者的原始摘要。
默认输出是紧凑清单；被选中的表只展开自身 schema 并采样 20 行。
选择 `columns` 以避免无关或过大的单元格；只在需要完整 schema 细节时
请求 `schema_scope: "database"`。在有限采样有用时选择 `row_limit`，
并显式标注截断与未指定的行序。虚拟表、影子表与视图属于 schema 事实，
不是行读取目标。REA 只检查私有副本，不动源文件；
检查前请先获得一致的静默（quiescent）数据库/WAL 快照。
另见 [SQLite 快照](https://github.com/morluto/rea/blob/main/docs/guides/data/sqlite-databases.md)。

## 已记录的 Linux 崩溃

对明确的 Linux x86-64 ELF core 路径使用 `inspect_recorded_crash`，
检查历史线程寄存器、信号、原始 note 与原始文件区间。
它与当前激活的反汇编目标相互独立。与源绑定的寄存器值和 note 字节属于观测；
缺失的 note、信号与线程的关联以及当前可执行/库身份保持未知。
PID 只是历史元数据，绝不会授权对活进程的附加（attach）或控制。

可选的 `include_debugger_context` 切面通过调用方提供的 GDB/pwndbg，
在一个独占的仅 core 会话中添加映射候选。
显示名不能确立当前文件身份；报告的标志为零时权限保持未知。
请求不可用的上下文会失败并给出配置指引。确切的上游 profile、边界与
验证覆盖范围见 [已记录崩溃](https://github.com/morluto/rea/blob/main/docs/guides/native/recorded-crashes.md)。

## 离线 ELF 布局

对明确的本地 ELF 路径使用 `inspect_binary_layout`，无需打开反汇编目标
即可获得基于文件的 section、符号、重定位、链接名称与静态缓解推断。
若该完整记录已保留，调用 `inspect_analysis_view` 获取摘要、缓解或链接切面、
单个 section 或符号，或稳定的分页。
不要为了读单个对象而重新运行解码器。

## 离线 WASM

对选定的本地字节使用 `inspect_wasm_artifact`，WABT 由调用方提供。
需要计数、验证结果和 WAT 身份时，在首个 MCP 调用中选择 `detail: "summary"`。
完整的原始 Evidence 保持保留；用 `normalized_result.parent_evidence_id`
做精确导出或文本分页。省略 detail 或选择 complete 会保留既有的完整结果。
对已完成的结果，用 `inspect_analysis_view` 配合其报告的保留引用获取摘要，
或使用 `view: {kind: "wasm", facet: "exports", offset: 0, limit: 32}`。
切面还包括 sections、imports、candidates、glue、WAT、headers、details
与工具 profile。文本偏移按 UTF-16 码元计数；请跟随 `next_offset`。
即使 MCP 回复超限，完整源数据仍保持保留。
不暗示执行目标或获取网络资源；WAT 只是解码后的表示。

## 离线 APK 签名

对选定的本地 APK/ZIP/AAB 使用 `inspect_apk_signature`。
默认 MCP 摘要保留完整 Evidence。选择 `view.collection: signers/digests/lineage`，
配合 scheme 或 ID 批量、字段与分页；删除后需读取保留数据时，
用 kind 为 `apk-signature` 的 `inspect_analysis_view`。
ID 保留产物/scheme 作用域与签名者关联；`fields: []` 保留身份关联。
空页会保留部分解码原因与未知的真实性。
CLI 紧凑投递需要 `--evidence_output` 以保留完整父 Evidence。
它在不执行任何代码的前提下读取 APK Signing Block（v2/v3/v3.1）和
v1 `META-INF` 签名，报告每个签名者的证书事实（v1 为 PKCS#7 块的
SignerInfo 所指证书）、声明的 v3 轮换谱系、声明的 source-stamp 证书，
以及（对 SHA-256/SHA-512 摘要）声明的内容摘要是否与当前字节一致。
该匹配不是签名验证：任何改过字节的人都能重新算出摘要。
`posture` 汇总以下内容：仅 v1 签名（无法区分"本来就只有 v1"与
"v2/v3 块被移除"两种情况）、跨 scheme 观测到的签名者一致性、
v1 签名者是否等于块 scheme 签名者（为 `false` 值得注意）、
每个不一致的签名者是否出现在声明（未验证）的轮换谱系中，以及最强的 scheme。
它从不声称真实性：没有任何签名或谱系经过密码学验证。

## 原生目标

`open_binary` 之后，直接使用聚焦的搜索、procedure 或 function 工具。
当目标元数据或清单上下文有助于回答问题时，使用 `binary_overview`。
优先使用字面量搜索、名称、反编译、调用者、被调用者与交叉引用。
地址与还原的伪代码属于分析观测，不是原始源码。
provider 不可用与不支持的元数据保持未知，而不是当作 false。

伪代码较大时，在首个 MCP 调用中以 `detail: "summary"` 请求 `procedure_pseudo_code`。
它保留完整观测，并返回原始选择、文本可用性与长度，但不带函数体。
用 `normalized_result.parent_evidence_id` 配合 `inspect_analysis_view` 与
`view: {kind: "native", facet: "pseudocode", offset: 0, limit: 20000}`；
后续页跟随 `coverage.next_offset`。若单页超出客户端或传输预算，选择更小的 limit。
偏移与 limit 按 UTF-16 码元计数，不按行或 token。
各分页复用同一观测，不重复反编译。null 与空文本保持区分。
省略 detail 或用 `complete` 会保留完整的内联投递。
摘要投递要求有保留会话，且不减少反编译的工作量与内存占用。

对已完成的 `analyze_function` 档案，用 `inspect_analysis_view` 配合
`view: {kind: "native", facet: "value_flow_operations", offset: 0, limit: 32}`
和确切的保留 Evidence ID，无需重新分析即可读取选定事实。
默认 MCP 回复已是该档案的摘要：其 `normalized_result.parent_evidence_id`
就是用于分页的保留 ID，其 null 计数标记 provider 未记录或声明不可用的切面。
原生切面还包括 procedure、pseudocode、assembly、basic blocks、comments、
callers/callees、references、unresolved calls、引用的字符串与名称、
原生 API 记录以及值流摘要。伪代码的偏移与 limit 按 UTF-16 码元计数；
续读使用返回的 `next_offset`。provider 限制与不可用事实保持显式；
完整父 Evidence 已保留。

对大型 framework 运行 `inspect_macho` 会返回数 MB 的导入与导出。
选择 `detail: "summary"` 获取 slice 身份、UUID 与逐集合计数，
然后用 `view: {kind: "macho", facet: "exports", offset: 0, limit: 64}` 与
`normalized_result.parent_evidence_id` 对行分页。
切面包括 entrypoints、architectures、build_metadata、load_commands、
dependencies、imports、exports、segments 与 provenance。
`source_exhaustive: false` 表示可能存在未返回的符号。

要在一次运行中看到 Mach-O 实际调用了哪些函数或 Objective-C 方法，
使用 `observe_native_calls` 并显式设置断点与有界的 `duration_ms`/`max_events`。
它会在 LLDB 下启动新进程，目标会真实运行，可能改文件或访问网络。
hardened-runtime 目标需要 `get-task-allow` 权限。
函数断点使用确切的 LLDB 运行时名称：传 `inspect_macho` 导出/导入项的
`runtime_name`（`main`），而不是符号表 `name`（`_main`）。
REA 不会转换断点名称。若只想选中该镜像，将 `module` 设为其文件名；
否则已加载的系统镜像也会匹配。归因某次调用前，先检查保留的位置与模块路径。

不带参数调用 `binary_session` 可检查打开的目标、选定的 provider 及对齐情况。
其默认摘要的 `result.tool_availability` 携带按当前状态分组的完整工具清单。
展开每个组的 `names`，除非组级覆盖，否则继承清单级客户端要求；
可用性、原因、修复方式与模式保持内联。
provider 候选保留可用性与目标支持状态、代码及原因。
`omitted_fields` 列出摘要省略的内容；`{"detail": "complete"}` 会补充每个
不可用候选的 `remediation`、provider 诊断、候选能力集，以及工具面、
`effects` 与 `annotations`。这些数组只从固定词表中列出为真的标志，
因此被省略的已知标志即为假。当目标或 provider 状态变化时，
`tools/list` 仍是完整工具 schema 的权威来源。

provider 能力组携带 provider 身份与有序的限制列表。
把每组各自的 `shared_limitations` 前置到该组的 `limitations`，
即可还原该操作的完整有序限制列表。以完整 detail 返回的候选能力
描述可能的 provider。顶层会话能力描述当前路由，
`analysis_provider_binding` 标识选定的 provider。

## 跨进程延续可编辑的 Ghidra 分析

对跨越多个 agent 会话的任务，选择 Ghidra 后检查 `binary_session`：
当前 provider 的 `capabilities[].shared_limitations` 会说明 Program 检查点
是否启用或会话是否为临时（ephemeral）。成功的原生查询能区分初始分析与
真正恢复的已打包 Program；不要仅因检查点模式启用就推断恢复已发生。

临时模式下，选择一个私有的绝对目录，并在启动 REA 的环境中设置
`REA_GHIDRA_CHECKPOINT_DIR`。更改该启动配置后重启 MCP 服务器；
当前没有任何工具调用或运行时分析设置更新能启用它。
支持 Linux/macOS 上的标准 ELF/PE/Mach-O 导入；
详见 [检查点配置与限制](https://github.com/morluto/rea/blob/main/docs/getting-started/installation.md#automatically-checkpoint-an-owned-ghidra-program)。

启用该设置后，常规打开会自动恢复兼容的已保存 Program。
初始完成的分析会被保存，`close_binary` 会保存其后的元数据编辑；
无需单独的保存/恢复工具。若报告保存失败，先修复再重试关闭。
取消或进程失败可能丢失最后一次成功保存之后的编辑；
未完成的初始分析无法续跑。后续进程请保持相同的检查点配置。
Evidence/Unknown 历史与不可变的 REA 查询快照有各自独立的持久化流程。

## 复用调用方指定的 Ghidra 分析

当调用方提供已展开的工程时，配置 `REA_GHIDRA_PROJECT_PATH`（`.gpr` 标记文件）
及可选的 `REA_GHIDRA_PROGRAM_NAME`（一个根程序），然后在 `open_binary`
前重启/重连。CLI 使用相同配置。
REA 只用 `-process -noanalysis -readOnly` 打开一个与指纹绑定的自有副本；
原始工程文件不会被引擎打开或保存。
此模式下数据库编辑、导入覆盖与修复脚本均不可用。
将原始分析的完整性/设置视为未知，将既有编辑视为调用方工程状态。
程序记录的导入摘要必须与目标匹配；工程内容变更后需重新打开以获取新 profile。
详见 [配置与准备指南](https://github.com/morluto/rea/blob/main/docs/getting-started/installation.md#reuse-an-existing-ghidra-project)。

## Ghidra 启动时限恢复

首次 Ghidra 查询时的 `provider_timeout` 可能涵盖导入、自动分析、
bridge 启动与就绪等待。默认 330,000 ms，可通过 `REA_GHIDRA_STARTUP_TIMEOUT_MS`
配置；即使查询更小，冷启动导入时间不变。

当错误提到 `ghidra.startup_timeout_ms` 时，调用 `update_analysis_settings`，
用 `action: "set"` 并在报告的范围内取更大的值。
下一次启动尝试前先解决保留的清理项。无需重启 REA；
已接受的启动保持其原有预算。遵循错误中针对该会话的重启指引；
当修复要求关闭并重开目标这一生命周期步骤时，先保留有用的 Evidence。

若是单函数超时，更新 `ghidra.decompile_timeout_seconds`，
并在既有 Program 上重试同一函数。显式传 `null` 会移除该单函数时限。
错误已给出设置名与范围时，检查步骤可省。
运行时更新在 REA 退出后消失；环境变量变更只会影响未来启动的 REA 进程。

客户端的工具调用时限必须容纳启动加请求的查询；
服务器设置与进度通知无法覆盖它。CLI 分析可避开 MCP 客户端时限，
但 provider 时限仍然存在。例如：

```sh
REA_GHIDRA_STARTUP_TIMEOUT_MS=1800000 rea analyze /absolute/path/to/app.exe --provider ghidra --json
```

三十分钟只是示例预算，不是完成保证。保持主机 CPU 与内存控制不变。
只有在可接受其覆盖缺失时才禁用特定的高开销分析器，并保留由此产生的限制。
导出的 C 代码与内嵌资源仍是有用的独立证据，
但超时不能证明分析完整或代码不存在。
详见 [时限与客户端指南](https://github.com/morluto/rea/blob/main/docs/reference/mcp-contracts.md#ghidra-first-query-deadlines-and-recovery)。

## Bridge 请求上限

Hopper 与 Cutter 共用 `REA_BRIDGE_MAX_REQUEST_BYTES`。
未设置时，两侧均使用 16777216 字节。载荷预算不包含结尾 LF。
7464 到 536870887 之间的十进制整数可上调或下调该上限。
下限需容纳最大的有界符号名命令。即使空间紧张，Cutter 状态响应仍会返回
其会话 id 与最多 64 条完成回执。空间够就带上路径，不够则路径未知，
因此旧的描述符路径不会与新代配对。上限是编码后的载荷，
比 Node 字符串上限少一字节，以留出框架 LF。
Cutter 会测量、签名并以有界分块写出能放下的响应。
bridge 只在新读取的字节中搜索框架 LF。客户端在解析前会把每个 socket
分块反转义成单个响应字符串，因此该上限不需要同时容纳分页线框和另一份拼接副本。
无效值属于配置错误，不会回退到 16777216。
`bridge.max_request_bytes` 可通过 `update_analysis_settings` 在运行时修改。
启动种子环境变量是 `REA_BRIDGE_MAX_REQUEST_BYTES`。
请在同一环境中启动 Hopper 或 Cutter，使 bridge 保持其启动时的上限，
直到该 bridge 再次启动。未带该设置的带外（out-of-band）bridge 保持 16777216 字节。
只有在 hello 证明存在活跃且已认证的 bridge 后，客户端才在发现阶段报告该不匹配，
并且不会发送状态请求或该命令。过期的描述符会被忽略。
只要任一活跃 bridge 的上限不一致，发现就失败，即使另一个活跃会话匹配。
因该上限被丢弃的命令响应仍是执行结果未知，并带 `output_truncated`。
从未发送已认证帧的 hello 不会占据 accept 循环。
最多运行 8 个连接线程；更多 accept 会被关闭，
线程启动失败不会停止监听器。`completed_connection` 是已终止连接的最长前缀。
密集标量回复以有界批次编码。
25000 ms 的 Cutter 请求时限与 256 候选的发现预算仍无运行时覆盖。

## 选定的原生事实与调用图

对较大的 `get_call_graph`，或反复的 `procedure_address`、`procedure_callees`、
`procedure_callers` 与 `resolve_containing_procedure` 查询，
当前 64 条已记录观测足够时选择 `detail: "summary"`。
用返回的父 Evidence ID 读取后续 `native-observation` 页。
图消息 ID 索引该页的精确文本字典；保留层级、来源索引、失败节点
以及部分/未知的关系覆盖。通过 `native-context` 切面 `overview`、
`analysis-profile`、`limitations` 与 `result-limitations` 读取引用的源上下文。
仅对同一摘要（digest）复用已检查的上下文/profile 值；
在读完注意事项前，超出返回事实的解读保持未知。
完整 Evidence 保持保留且可导出。小型完整回复可能比额外的上下文/分页调用
更省 token；要把已完成任务与发现过程一起计入。

## 静态内存与原始文件字节

对 Ghidra，`read_bytes` 读取已初始化的分析内存（包括 loader fixup）；
它不读取运行中的进程。解码表之前先检查 `returned_bytes` 与 `complete`。
读取不完整表示覆盖缺失，而不是以零填充的尾部。
用 `list_segments` 检查所选块的初始化与地址空间事实，
不可用的事实保留为未知。

用 `address_to_file_offset` 把一个已观测地址锚定到原始文件字节。
首地址的映射不能确立整张表的连续映射，
loader fixup 也可能使分析字节不同于源字节。
请把源码区间与分析内存观测分开对待。

指针表可能指向由构造函数填充的可写槽位，而不是直接指向不可变资源。
未初始化的块或观测到的零不能确立该槽位之后的运行时值。
跟随 `xrefs` 与相关写入者的汇编或伪代码；
把已记录的赋值与推断的执行顺序区分开。
不要把不可读字节替换为零，也不要在没有必要初始化证据的情况下断定资源不存在。

## 用 Ghidra 处理 DOS MZ

对已接受的 DOS MZ 目标，使用 `inspect_native_load_image` 对照不可变快照
核对实测加载字节、文件映射、重定位与入口。
`mismatch` 与 `unsupported` 保持显式。
已验证的导入只覆盖报告的静态镜像，不覆盖运行时 DOS 或 PC-98 硬件行为。

加载镜像报告很大时，选择 `detail: "summary"`，并用 kind 为
`native-load-image` 的 `inspect_analysis_view` 查询其 `parent_evidence_id`。
选择 `relocations` 或 `mappings` 之类的集合，只取需要的字段，
用 offset/limit 分页。原始索引保留同地址的多个候选项。
null 集合保持未记录或不适用；分页不会把不支持的验证升级为支持。
CLI 摘要投递需要 `--evidence_output`，以保证完整源 Evidence 仍可访问。

对 Ghidra 反编译，`procedure_pseudo_code` 也接受 `procedure: "file-offset:0x..."`；
CLI `rea decompile <path> --file-offset=0x... --provider ghidra`
会在内部解析源字节偏移。无法解析的 0x 前缀数字 procedure 选择器
也会回退到唯一的文件映射。既有符号与分析地址优先；
多个映射会因歧义而失败。保留返回的文件偏移与地址位置，以及原始选择观测。
ELF 虚拟地址与文件偏移是两回事；
绝不要假设任意偏移加镜像基址就是分析地址。

完整函数体区间使用闭区间端点，且可能含空隙。不要把外层跨度当作代码。
对加壳目标，保留原始产物身份与单独派生的产物身份；
反编译解壳 stub 不会还原解壳后的程序。

读取 Objective-C 派发元数据时，要区分类的实现方法与协议要求：
类方法报告 null 的要求标志，而已解码的协议声明保留 required 与 optional 事实。
属性特征保持原始名称/值 token；用属性的 `atomicity` 字段表达解码后的
`N` 标记或默认原子行为。class/meta 标志、ivar 数量、原子性或只读值为 null，
表示所选 provider 未确立该事实。仅凭符号名不能证明某个类是根类或没有 ivar。

## 托管 PE/CLI

从 `inspect_managed_artifact` 开始。REA 的规范托管检查不执行任何代码：
不要声称它加载、反射、执行或解析了程序集。
保持托管/原生边界与不可用的还原事实显式。
自备的还原 oracle 与规范解析器相互独立，不得成为隐式的配置依赖。

对身份/分类问题，`inspect_managed_artifact` 可在首个 MCP 调用中
显式选择 `detail: "summary"`。它保留完整元数据，并返回一个带链接的概览，
包含完整分类/证据、可空的 module/MVID、frameworks、元数据覆盖/问题/限制
以及返回行数。默认的完整请求保持不变。
用 `inspect_analysis_view` 读取原始行，source 用
`normalized_result.parent_evidence_id`，并配
`view: {kind: "managed", collection: "attributes", offset: 0, limit: 16}`。
集合有 `references`、`resources` 与 `attributes`。分页不重复解析。
返回行耗尽不能在部分/不可用覆盖下证明元数据完整或不存在；
请保留构建局部 token 及其 artifact/MVID 作用域。

`inspect_managed_members` 总是返回整个程序集范围的 `member_refs`，
即使只选了一个类型。针对选定类型的问题，选择 `detail: "summary"` 并传
`type_names`；它会返回所选类型（含未匹配名称）、覆盖情况与逐集合计数。
用 `view: {kind: "managed-members", collection: "call_edges", offset: 0, limit: 64}`
对 `types`、`exported_types`、`fields`、`methods`、`member_refs`、`call_edges`、
`field_accesses` 或 `user_strings` 的行分页。
对支持的集合，先用精确的 `names` 与 `declaring_types` 过滤再分页。
需要紧凑的方法查询时，请求 `fields: ["name", "declaring_type", "signature"]`；
省略 `body` 可避免锚点。身份 token、原始 `source_index`、module/MVID
与来源覆盖保持不变。把空匹配解读为不存在之前，先检查 `unresolved_filter_rows`。

### .NET NativeAOT

NativeAOT 二进制包含原生机器码，普通 CIL 反编译器无法还原原始方法体。
托管元数据/CIL 缺失时，把它归类为原生分析路线，不要声称还原了源码。
用选定的深度 provider 打开原生镜像，检查函数、字符串、调用与引用；
把反编译器输出描述为伪代码与推断。

NativeAOT 镜像可以是 PE/COFF、ELF 或 Mach-O 的可执行文件与共享库。
用文件字节与 loader 元数据而非后缀名来识别。
对打包应用，用 REA 的 artifact 工具做清单/提取，并保留其中镜像的确切身份。
PDB、ELF 调试信息或 dSYM 附属文件只有在 provider 接受并匹配时才是额外证据。

REA 对带 .NET 8 RTR 9.1 元数据的 x64 PE 目标有内置只读快照解析器。
可选的 headless Ghidra 适配器在 Linux 上增加数据库注记与更广的元数据恢复；
它要求显式配置 NativeAOT JAR。两者是独立路线。
内置解析器也可在 Windows Ghidra P0 上运行；冻结字面量要从其报告读取，
因为 `search_strings` 不包含它们。配置、支持的布局与主机限制见
[NativeAOT 指南](https://github.com/morluto/rea/blob/main/docs/providers/ghidra-nativeaot.md)。
保留二进制身份，并把派生元数据与 Ghidra 数据库观测区分开。
还原的类型与原生伪代码不是原始 C# 源码。
Windows Ghidra P0 没有数据库修改权限。

## 包与提取

当产物图与发现有助于回答问题时，对应用包、归档、ZIP/APK/IPA/MSIX/AppX、
ASAR 或 DMG 输入使用 `inspect_artifact`。它内联返回完整产物图。
使用图 manifest ID 时请引用其 ID。

对 IPA 或 macOS 的 `.app`、ZIP 或 DMG，把清单 Evidence 传给
`project_apple_application_graph`。它按路径约定报告应用根与嵌套 bundle：
app 扩展、XPC 服务、framework、登录项、系统与驱动扩展以及插件。
它还列出特权 helper、launchd plist、符号链接，以及每个 bundle 的
`info_plist_path` 与可执行候选。角色只是路径约定，不是解析过的 plist；
请用 `inspect_plist` 读取列出的 plist。

对 `.app` 或 Mach-O 执行 `open_binary` 后，用 `trace_dylib_resolution`
查看对 bundle 中每个可执行文件，每个 `@rpath`、`@loader_path` 与
`@executable_path` 加载最终到达哪个文件。
它还列出缺失或弱加载，以及不存在的前序 `@rpath` 候选。
大 bundle 用 `roots` 或 `architecture` 缩小范围。
系统路径保持未确定，因为它们由 dyld 共享缓存提供。

需要从受支持格式落地实体文件时，使用 `extract_artifact`。
它提取当前目标，并接受可选的 `integrity_policy`；详见 [MCP 契约](https://github.com/morluto/rea/blob/main/docs/reference/mcp-contracts.md)。
它把所有普通文件落地到由 REA 选择的新临时目录。
符号链接与加密条目属于清单事实，不是可提取文件。
结果报告落地的目录；调用方不选择目的地。无需单独授权。

对经典 iNES 卡带，`open_binary` 能识别其字节签名，但其中没有可执行架构。
`inspect_artifact` 保留头部事实与每个 PRG/CHR 文件单元的偏移、长度与 SHA-256；
其嵌套清单的 `ines.reconstruction` 会用整文件摘要核对实际有序区域字节。
提取包含原始头部、可选 trainer 与未解释的尾部字节。
这些文件单元不是 mapper/CPU bank 映射。
NES 2.0、UNIF、不干净的旧式头部与截断载荷会被显式拒绝。
不执行模拟器或 6502 分析。详见 [iNES 指南](https://github.com/morluto/rea/blob/main/docs/ines-containers.md)。

在受支持的 macOS 主机上，原生 DMG 遍历自动使用只读挂载，
并配有自有临时挂载目录与清理。无需批准标志。
不支持的主机或挂载失败保持为显式限制；
只有根身份可用时不要声称有子清单。DMG 无法通过 `extract_artifact` 提取。
在 macOS 上访问 DMG 文件时，用你自己的工具创建只读挂载，
从挂载点选择文件做分析，结束后卸载你创建的挂载。
REA 的检查挂载是临时的，不是镜像内容的保留导出。

对无头的 DOS COM，用 `format: "dos-com"` 显式打开（CLI 为 `--target-format dos-com`）。
在信任函数分析前先检查加载镜像：入口为 `0x10100`，文件偏移为零，
并带强加的实模式段上下文。PSP/栈/设备状态仍未建模。
详见 [DOS 指南](https://github.com/morluto/rea/blob/main/docs/providers/ghidra-dos.md)。

提取前用 `inspect_byte_entropy` 对高/低熵区间做分诊。

对其他无头镜像（没有 ELF/Mach-O/PE/MZ 头的嵌入式固件），
用 `format: "raw-binary"`、`architecture`（`x86`、`x86_64`、`arm`、`arm64`、
`6502` 或 `m68k`）与 `entry_point`（`0x` 十六进制）打开。
文件偏移 0 被映射到该地址。Hopper 与 IDA 拒绝这种解释；
Ghidra 使用 `BinaryLoader` 与通用语言：`m68k` 为大端，其余为小端。
不支持大端 ARM、仅 Thumb 与 Cortex-M 变体。
`6502` 选择 NMOS 6502；入口与完整文件映射必须落在 `0x0000..0xffff` 内。
不支持 65C02、65816、卡带容器、bank 切换与 mapper 语义。
`m68k` 要求入口为偶数，并按 68000 家族的 68040 超集解码；
不支持 Amiga/Atari 容器与向量表入口发现。
Windows Ghidra P0 只接受 `6502` 的 raw 镜像。
详见 [raw binary 指南](https://github.com/morluto/rea/blob/main/docs/providers/raw-binary.md)。

Intel HEX、S-record、UF2 与 DfuSe 文件是容器而非 raw 镜像：
`inspect_artifact` 列出地址区域（UF2 按 familyID，
DfuSe 按 element 及其 alternate setting），`extract_artifact` 写出每个区域。
把提取出的区域按 `raw-binary` 打开，以其起始地址作为 `entry_point`。
UF2 编号空隙使覆盖保持未知；DfuSe 尾部 CRC 不匹配遵循 `integrity_policy`。
详见 [UF2 与 DfuSe](https://github.com/morluto/rea/blob/main/docs/uf2-dfuse.md)。

### Ghidra 中的函数注记

新导入会话允许注记；既有工程复用是只读的。
用 `annotate_native_function` 设置单个函数名和/或入口注释，
且至少有一处显式变更。内联查看其注记回读与刷新后的档案。
变更是原子的；空注释会清空，省略字段则保持不变。
后续 MCP 调用能看到编辑结果。在自有 Program 检查点模式启用时，
常规关闭会保存它们；临时模式则丢弃。
CLI `annotate-native-function` 在输出更新结果后关闭时遵循相同设置。
若编辑必须跨进程保留，先选择[检查点工作流](#continue-editable-ghidra-analysis-across-processes)。
原始可执行字节不变；编辑会使不可变快照失效。
Windows P0 不接受数据库修改。仅用于命名时，
`set_address_name` / `set_addresses_names` 也可用于 Ghidra：
它们为函数入口或数据地址（主标签）命名，
返回紧凑的逐地址成功布尔值，而不是档案。
Ghidra 会拒绝批量地址中请求相同名称、或请求另一个所选地址已占用名称的情况；
`raw_result.failures` 给出每个失败的原因。

切换 provider 或更换目标可能停用当前 Ghidra 数据库并丢弃其编辑，
即使新 provider 在后续调用中失败也一样。
同目标、同 profile 的重开保留当前数据库。
保留的注记 Evidence 记录发生了什么；它不会恢复编辑。

对 `compare_functions`，在 MCP 会话打开期间于编辑前后各取一次
`analyze_function` Evidence；注记 Evidence 不是对比输入。
若对比将在之后进行，请在关闭前导出所需 Evidence。
已认证的同产物坐标把改名条目保留为 `matched / same-entry`，
并内联规范 `entry_address`；名称与精确文本变更仍是独立维度。
这要求架构兼容、provider 自有的映射以及对所选镜像的一致承诺。
仅凭相同数字地址不能确立对应关系；
匹配仍有歧义时，检查保留的源 Evidence 与覆盖范围。

## 离线 PE 资源清单

用绝对 `path` 或 `rea inspect-pe-resources ./selected.exe --json` 调用
`inspect_pe_resources`，无需打开原生目标即可做可移植的 PE32/PE32+ 资源检查。
保留返回的 Evidence：类型/名称/语言 ID 与 UTF-16 名称、
原始目录/数据/载荷区间、代码页、载荷哈希与静态图标组引用。
同语言图标解析是显式的；缺失引用与大小不匹配保持可见。
其他载荷视为不透明；该操作不解码图像，也不模拟 Windows 资源加载。
预算与支持的树 profile 见
[离线二进制诊断](https://github.com/morluto/rea/blob/main/docs/guides/native/binary-diagnostics.md)。

## 离线 PE 与 ELF 导出表

用绝对 `path` 或 `rea inspect-native-exports ./libexample.so --json` 调用
`inspect_native_exports`，在任何主机上无需打开原生目标即可读取
PE 导出目录或 ELF 动态符号表。仅序号、转发与隐藏版本的导出保持区分；
部分或不支持的覆盖表示清单不完整，而不是导出不存在。
Mach-O 用 `inspect_macho`。详见
[离线二进制诊断](https://github.com/morluto/rea/blob/main/docs/guides/native/binary-diagnostics.md)。

需要精确的核心模块导入/导出差异时，用 `compare_wasm_interfaces`
配合两份完整检查 Evidence 记录（或当前会话的保留引用）与显式范围。
保留未知类型/重复名称；静态接口相等不等于运行时兼容。
CLI 在 `rea compare-wasm-interfaces input.json --json` 中接受完整内联 Evidence，
或用 `--evidence-bundle /absolute/path/evidence.json` 传确切引用。
检查返回摘要时，使用完整父 ID。

## Godot PCK

对独立 PCK，先 `open_binary` 再用 `detail: "summary"` 的 `inspect_artifact`，
可保留完整静态清单。用返回的 `parent_evidence_id` 配合 `inspect_analysis_view`，
按确切 `logical_paths` 或 `occurrence_ids` 过滤清单 occurrence，
并将 `artifact_id` 关联到按 `artifact_ids` 过滤的节点。
只取需要的字段；身份关联保留。
CLI 任务优先用 `inspect-artifact --detail summary --evidence_output PATH`；
同一 CLI 通过 EOF 尾块发现内嵌 pack，无需打开原生分析 provider。
常规原生打开流程不变。

区分声明的 MD5 与观测的 SHA-256，以及图/页完整性与 `source_coverage`。
加密目录与稀疏 bundle 的条目覆盖未知；加密成员的内容身份未知。
在覆盖未知时，空的过滤页不能证明不存在。
保留视图是历史记录，不是新的文件系统检查。
不提供解密、Godot 资源解码、GDScript 反编译或目标执行。
详见 [Godot PCK](https://github.com/morluto/rea/blob/main/docs/godot-pck.md)。

UnityFS AssetBundle 容器（`.bundle`、`.ab`、YooAsset 包及其他按字节识别的文件）
列出 `CAB-*` SerializedFiles 与 `.resS` 成员及其头部与节点事实；
none/LZ4/LZ4HC 成员块按需流式读取。
声明了 asset-bundle 加密的 bundle 保留头部事实但目录覆盖未知；
LZMA 成员字节保留具名 occurrence 但哈希不可用。
虚拟成员偏移不是物理承载位置。
格式 6–8 的读取器缓存一个已解码块，并支持保留的过滤/分页视图。
不提供解密或 SerializedFile 对象解码。详见 [UnityFS](https://github.com/morluto/rea/blob/main/docs/unityfs.md)。

微信小程序包（带 `0xBE`/`0xED` 标记的 `.wxapkg` 文件）列出成员及其声明名称
与绝对承载偏移；成员字节按原样存储。
`V1MMWX` PC 端包报告 `encrypted` 目录状态且覆盖未知，
提取时被拒绝；不做任何解密尝试。详见 [wxapkg](https://github.com/morluto/rea/blob/main/docs/wxapkg.md)。

U-Boot 旧式 uImage 使用相同的检查/提取流程。
头部事实或组件 ID 优先用保留摘要与选定的清单视图。
头部地址/CPU/OS 只是声明；载荷保持存储原样。
多文件组件保留其对齐的物理区间；完整载荷也会落地。
未知名称文本保留原始 32 字节。详见 [U-Boot uImage](https://github.com/morluto/rea/blob/main/docs/uimage.md)。

## ESP 镜像

对 ESP32 家族的应用或 bootloader 镜像，先 `open_binary` 再用
`detail: "summary"` 的 `inspect_artifact`。
`root_format_metadata` 保存观测到的 `header` 与 `descriptor`
（其 `kind` 是 app 或 bootloader 角色），以及派生的 `chip`、`checksum`、
`appended_sha256` 与 `undescribed_trailing` 区间。
段行（`segment-NN.bin`）带有 `load_addr`、`classification`（`mapped`、`loaded`、
`not-loaded` 或 `unknown`，依据 ESP-IDF 的 `should_map`/`should_load`；
RAM 区间不检查）与 `source_location`；
用 `inspect_analysis_view` 与 `logical_paths` 选取。
签名块为 `unverified`；`public_key_sha256` 与 eFuse 密钥摘要匹配。

未知 `source_coverage` 表示截断或未描述的尾部字节，
例如 `--ram-only-header` 镜像的 flash 段；不要据此推断不存在。
已擦除的 flash 会被描述。完整性不匹配是事实陈述，不是拒绝。
ESP8266 镜像被拒绝，flash 加密镜像不被识别。
段不做反汇编，RISC-V 或 Xtensa 段不能按 raw-binary 打开。
详见 [ESP 镜像](https://github.com/morluto/rea/blob/main/docs/esp-image.md)。

## ESP flash 镜像

整片 flash 转储按 `esp-flash-image` 打开。`root_format_metadata` 保存
`partition_table`（其 `method`：`default`、`caller` 或派生的 `scan`）、
`bootloader` 与 `apps` 的 ESP 镜像事实、`otadata` 记录、
`partitions_outside_dump` 与 `boot_selection`。
每个表都有 `boot_selection`：其 `basis` 指明 bootloader 的分支
（无 otadata 时为 `no-otadata`，bootloader 拒绝该表时为 `none`，
记录缺失时为 `unknown`），并列出其 `assumptions`；
`running_partition` 总是 `unknown`。每个镜像用 `path` 标明其入口。
用 `detail: "summary"` 时根 kind 为 `esp-flash-image-summary`，
每个镜像是紧凑 `summary`（芯片、入口点、段数、分类的加载区间、
签名块数、descriptor 身份、完整性）；完整 detail 保留每个段。
分区行（`partitions/<label>.bin`）带有声明的 `type`、`subtype`、名称、
`flash_address`、`size` 与标志；`encrypted` 是存储标志，不是密文的证明。
`written_offset`/`written_end` 界定未被擦除的字节：
事实为 `erased` 的 app 槽位仍可能保存更旧的镜像，限制说明里会写明这一点。
对从其他 flash 地址读取的转储，用 `format: "esp-flash-image"` 与
`flash_offset` 调用 `open_binary`；设置了 `flash_dump` 的 `esp-image`
会在下一步探测中给出该偏移；重定位的表可用 `partition_table_offset` 指明。
找不到表表示未知，通常因为 flash 加密。
提取时 `nvs_keys` 按普通数据写出。
详见 [ESP flash 镜像](https://github.com/morluto/rea/blob/main/docs/esp-flash-image.md)。

## Bun 独立可执行文件

`bun build --compile` 可执行文件把模块图存储在 Mach-O `__BUN,__bun`、
PE 或 ELF 的 `.bun` section，或附加尾块中。
先 `open_binary` 再 `inspect_artifact`，会报告根格式 `bun-standalone`，
包含载体、结构布局、模块数、入口点、原始标志与 compile exec-argv；
每个模块保留其 `/$bunfs/...` 源名称、loader、编码、大小与 SHA-256，
sourcemap、字节码与 module-info 区域作为单独子节点。
用摘要根元数据中的 `entry_point_logical_path` 作为确切的清单
`logical_paths` 选择器，然后按 artifact ID 读取所选内容节点；
虚拟名称归一化与索引回退由读取器负责。
`extract-artifact` 通过安全输出树写出存储内容；
提取出的 JavaScript 交给 `analyze_javascript_application` 处理。
布局标签描述记录形态，不是检测到的编译器版本；
未知或有歧义的布局不受支持。字节码只保留不解码，且绝不运行该可执行文件。
详见 [Bun 独立可执行文件](https://github.com/morluto/rea/blob/main/docs/bun-standalone.md)。

## Deno compile 可执行文件

`deno compile` 可执行文件把应用存储在 Mach-O `__SUI,d3n0l4nd` section、
Intel Mach-O `<~sui-data~>` 尾块、类型为 `0x53554901` 的 ELF `SUI` note，
或名为 `D3N0L4ND` 的 PE `RT_RCDATA` 资源中。
先 `open_binary` 再 `inspect_artifact`，会报告根格式 `deno-standalone`，
包含载体、入口点、记录的选项，以及每个虚拟文件一条 occurrence（含大小与 SHA-256）。
转译输出、CJS 导出分析与 source map 是独立的 occurrence，
带文件的 `index` 与各自的 `role`。
它们通常在文件路径上使用 `.deno-*` 后缀，冲突时移到带索引的路径，
因此请使用报告的 `logical_path`。符号链接目标保持为已记录的路径组成部分。
无法列出的虚拟文件系统使覆盖保持未知。
环境文件值与 CA 证书字节保留在本地 Evidence 中，并附带计数与字节长度。
npm 快照长度只报告，不解码。
`extract-artifact` 通过安全输出树写出存储文件；
提取出的 JavaScript 交给 `analyze_javascript_application` 处理。
其他布局不受支持，且绝不运行该可执行文件。
详见 [Deno compile 可执行文件](https://github.com/morluto/rea/blob/main/docs/deno-standalone.md)。
