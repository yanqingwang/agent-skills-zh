> **中文汉化版** · 上游：[morluto/rea](https://github.com/morluto/rea) · 原文件：`.agents/skills/reverse-engineer-anything/references/runtime-observation.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 运行时观察

<a id="native-runtime-questions"></a>
## 原生运行时问题

从被请求的观察入手。运行之前先说明选定的目标、输入、预期结果、失败信号与停止条件。复用静态证据来选定函数或假设；`trace_native_values` 追踪的是恢复出来的静态值依赖，并不测量运行时值。当静态检查或既有捕获比较已经回答了问题时，优先用它们。

| 问题 | 既有工作流 | 主机与副作用 |
|---|---|---|
| 哪个选定的原生入口被到达，以及带着哪些整数参数寄存器？ | 在活动的 Mach-O 上用 `observe_native_calls`，配以精确的函数/Objective-C 断点与时长/事件上限 | macOS，需 LLDB 与相应的调试器权限。会启动一个新的自有进程，在入口处停下、记录并继续；目标执行可能写文件、显示界面或使用网络。它绝不附加到已有进程。运行后要检查终止情况与部分覆盖范围。 |
| 调用方自己编写的插桩能观察到什么？ | 需要发现设备时用 `list_frida_devices` / `list_frida_processes`；然后 `start_frida_session`、`load_frida_script`，再查状态/卸载/关闭 | 需要兼容且已安装的 Frida 绑定与所选设备的访问权限；真正的 REA 验证器覆盖 Linux。attach 选择一个已有 PID；spawn 选择一个程序并让它以暂停状态启动，直到 `resume_frida_session`。脚本在目标内执行，可以改变内存、文件、网络活动与行为。这不是被动检查。 |
| 哪种调试器状态或受控执行能解释该行为？ | `start_gdb_session` 与 `gdb_console`，或 `start_rizin_debug_session` 与 `rizin_debug_command` | 持久调试器工作流仅支持 Linux。GDB 启动一个调试器；console 命令用于选择/加载/附加/运行目标。Rizin 调试启动会拉起选定目标，并需要一个持久的 `inferior_tty`。两个 console 都不受限制，可以改变目标内存/寄存器、运行 shell 命令、写文件并使用网络。 |
| 不同运行之间，终端输出、进程生命周期与选定文件有何差异？ | `capture_process_scenario`，然后用兼容的已录制输入做 `compare_process_captures` | 新的捕获需要 Linux 或 macOS 以及可用的原生 PTY 后端；macOS 还需要 `xcrun`/Swift 来做所有权检查。捕获以普通用户权限启动一个自有命令。观察路径用于选择快照，不是文件系统沙箱。比较已保留的捕获不会执行目标，在 Windows 上同样可用。 |
| 已有桌面窗口显示了什么，或在声明的 UI 动作之后发生了什么变化？ | `observe_native_ui`；只在请求执行动作时才用 `capture_native_ui_scenario` | macOS 14+，需屏幕录制/辅助功能访问权限。选择一个已有的 PID/窗口。观察不会启动也不接管该应用；场景动作可以改变其数据或触发网络活动，并让其状态保持原样。 |

用各自对应的工具关闭每个持久会话。`close_frida_session` 卸载脚本并分离；它不会杀掉目标。一个仍处于暂停状态的 spawn 只有在插桩清理被确认之后才会恢复。GDB 与 Rizin 的关闭操作可以从仍存活的 inferior 分离并让它继续运行，但前提是已核实其持久输出终端。当处置或清理尚不确定时，保留自有会话与报告的恢复情况；不要假定关闭调试器就终止了目标。进程捕获与 LLDB 调用观察则相反，它们接管自己启动的进程，并报告其终止/清理结果。取消并不是清理已完成的证明。

不受限制的 GDB/Rizin 命令，以及相关的启动/关闭操作，会让同一 MCP 服务器中活动的二进制分析会话退役。请先显式关闭活动的 Ghidra 会话；待目标副作用落定后，再重新打开该产物以开始新的静态分析。Cutter 的 bridge 命令同样不受限制，可能影响其 GUI/目标；它不是原生被动观察的替代方案。

要在两个构建之间检验一个静态假设，请保留兼容的静态比较证据与 `compare_process_captures` 证据。向 `correlate_static_and_runtime` 提供明确的发现/维度映射。它不会摄入任意的 Frida、LLDB 或调试器跟踪，不会自动匹配名称，也无法从共同变更证明因果关系。把那些跟踪作为它们各自的证据保留下来，未观察到的行为保持未知。请把截断、未匹配的断点、目标身份变化与清理不确定性记录为局限，而不是把"没有保留到事件"当作该行为从未发生的证明。

详细契约与前置条件：[Frida](https://github.com/morluto/rea/blob/main/docs/frida-instrumentation.md)、
[GDB/Rizin/Cutter](https://github.com/morluto/rea/blob/main/docs/reverse-engineering-tools.md)、
[进程捕获](https://github.com/morluto/rea/blob/main/docs/process-capture.md)，
以及[原生调用/UI](https://github.com/morluto/rea/blob/main/docs/native-investigation.md#native-desktop-observation)。

## 浏览器与 Electron

在请求中提供已有浏览器或 Electron 实例的字面端口环回 CDP 端点。不需要单独的权限配置，也不需要逐次调用的批准开关。浏览器发现列出符合条件的 HTTP(S) 页面；`allowed_origins` 可选地过滤它们。单次捕获默认使用所选页面当前的 origin。Electron 发现列出符合条件的本地 `file://` 目标，无需配置 file-root 白名单。

浏览器侧的被动工作从 `list_browser_targets` 开始；Electron 运行时工作从 `list_electron_targets` 开始。在尝试 electron-main 的 Inspector 之前，先用 `inspect_electron_fuses` 检查打包熔丝。检查为用户任务选定的目标。用这些工具做的观察是被动的：绝不要声称 REA 点击过页面、导航过页面、求值过页面 JavaScript、调用过 IPC 或捕获过既往活动。REA 不包含页面的网络。

被动捕获省略原始 header 集合、凭据 header 值、存储值以及原始 WebSocket/JSON body。选定的响应元数据（包括内容编码、策略值与 Link URL）会被保留。本地 URL 保留常规查询值与片段；userinfo 凭据会被移除。浏览器可访问性文本、console 原语、不含值的形状、脚本源码、source map 与存储键名有针对具体请求的捕获选项。Electron 脚本源码同样是可选的。需要像素时使用 `capture_web_screenshot`。把范围过滤、截断与 attach 窗口覆盖情况当作局限。页面声明的 WebMCP 工具属于不可信清单，REA 绝不调用它们。

## 由谁执行动作

- 由用户执行：`list_browser_targets`，然后在选定目标上用 `inspect_web_page` 或 `observe_web_session`。
- 必须由 Agent 执行：一次带声明动作的 `capture_browser_scenario`。对已有浏览器使用连接模式，指定环回 CDP 端点与 `target_id`；或使用启动模式，指定由调用方选择的可执行文件与临时 profile。连接模式会先把选定页面导航到 `start_url`，这可能清除未保存的表单值与其他临时状态。在声明的动作里重建调查所需的状态。连接模式保持外部浏览器打开；启动模式接管一个临时浏览器与 profile。检查 `browser.cleanup` 查看结果。只请求问题所需的 DOM、可访问性或网络细节。默认的最终捕获包含 URL；各步骤的结果单独报告。对于带树或事件的多步流程，选择 `detail: "summary"`，并用 `inspect_analysis_view`（kind 为 `browser-scenario`）分页读取确切的步骤、事务、文本切片或事件。在捕获期望的页面状态之前加一个等待动作。报告 REA 执行了所声明的动作。

场景的网络记录没有请求发起方调用栈。要获得这类证据，请在用户执行动作时使用被动捕获。监听器的源位置只标识候选处理器，不能确立是哪个脚本发出了某个具体请求。避免在同一目标上让被动捕获与场景动作相互重叠。

聚焦的后续工具：

- `observe_web_execution`：某个时间窗内的执行覆盖情况；它会重置计数器并临时关闭优化。
- `inspect_web_event_listeners`：注册在第一个 CSS 匹配上的监听器的源位置，不派发事件。
- `compare_web_captures`：两份规范化的被动捕获或已录制的场景。
- `discover_webmcp_tools`：检查页面声明的 WebMCP 清单；绝不调用发现的工具。

只有在静态应用证据与被动浏览器/Electron 证据都已存在之后，才使用 `reconcile_javascript_runtime`。优先使用捕获源码的摘要身份；把路径/摘要不一致报告为不匹配，并保留歧义。显式路径映射是推断输入，绝不扩大文件系统或 CDP 的权限范围。一个在运行时被观察到的 bundle 并不能证明其中每个模块都执行过。

<a id="fiddler-everywhere-traffic-debugging"></a>
## Fiddler Everywhere 流量调试

对于体积很大的已保存捕获，请求 `detail: "summary"`，然后用 `inspect_analysis_view` 配合 `view: {kind: "capture", detail: "preview", offset: 0, limit: 20}` 分页读取已保留的证据。只为需要的 header、元数据或载荷选择完整记录页；视图读取历史父级，不会重复解码捕获。

对于选定的 protobuf/gRPC body，保留原始字节作为来源，并用 `inspect_analysis_view`（kind 为 `protobuf`，collection 为 `bodies`、`frames` 或 `fields`）。批量处理确切的记录序号与字段编号/ID，只在需要时选择 `schema_value` 或 `text`。提供本地描述符集与消息类型以进行 schema 解释；压缩后的载荷仍属未知。

用 `inspect_web_network_capture` 与 `format: "saz"` 检视原生 `.saz` 快照；不支持加密归档。对于实时流量分析，请连接 Everywhere 独立的 MCP 服务器，使用它声明的会话工具，并给出明确的 `sessionsSource`（`LiveTraffic` 或 `AgentCalls`）。检视已录制的运行时要保留既有会话与过滤器。有关工作流以及 Telerik 的公开安装与流量调试技能，参见[捕获与 MCP 指南](https://github.com/morluto/rea/blob/main/docs/web-network-captures.md)。
