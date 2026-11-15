> **中文汉化版** · 上游：[morluto/rea](https://github.com/morluto/rea) · 原文件：`.agents/skills/reverse-engineer-anything/references/connection-and-recovery.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 连接与任务恢复

仅在出现已观测到的连接、命令、审批或 provider 阻塞时阅读本指南。
始终围绕用户的目标与问题。说明是什么阻碍了操作以及下一步该做什么；
修复后继续调查。

下面的命令使用已安装的 `rea`。若不可用，且获取 REA 已获授权，
使用 `SKILL.md` 中的包调用方式。
以所连服务器的 schema 与已装 CLI 的帮助为准，
不要假设仓库 main 与旧版本暴露相同参数。
工具名前缀属于客户端：在其真实的工具列表与服务器关联中确认规范的 REA 操作，
再断定它不存在。仅凭共享前缀不能确立审批通配符覆盖哪台服务器。
另见 [客户端工具名与发现](https://github.com/morluto/rea/blob/main/docs/getting-started/client-configuration.md#client-tool-names-and-discovery)。

## 依据观测到的故障选择补救

| 观测                                                             | 含义与下一步                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 当前会话中没有 REA 工具                                          | 若 REA 以客户端插件方式安装，参照下文插件章节。否则用 `rea doctor --client codex --json` 检查注册。仅安装 skill 不会注册 MCP。                                                                                                                                                                                                                                                                                                                                                                                     |
| 注册缺失、畸形或过期                                             | 准备有范围限定的配置计划；只应用已授权的变更并保留备份。                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 注册一致但没有已连接工具                                         | 重启/重连客户端。doctor 检查注册；它无法确立当前 agent 的连接。重连失败时检查客户端的启动错误。                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MCP 连接断开或 REA 无法启动                                      | 连接断开时，仅当该调用可安全重复或已知未开始执行时才重试一次。若它可能已改变目标，或同样故障再次出现，告知用户 REA 连接失败并请其重启 MCP 客户端。若 REA 无法建立连接，重试一次，然后告知用户并请其重启 MCP 客户端。启动失败返回同样结果时不要重试。REA 无法启动或重启后工具仍缺失时运行 `rea doctor`。doctor 自身无法恢复活连接。 |
| `MCP tool call requires approval, but approval policy is never`  | Codex 在 REA 执行前拒绝了该调用。不要为此客户端策略决定安装引擎或重复配置。见下文审批章节。                                                                                                                                                                                                                                                                                                                                                                                                                          |
| REA 返回 `provider_unavailable` 或不可用工具条目                 | 读取该操作的 provider 诊断或 `binary_session.result.tool_availability`。展开每组的工具名，除非组级覆盖，否则继承共享客户端要求。使用该操作的可用性、原因与修复建议；完整的工具目录不代表每个操作都可用。`{"detail": "complete"}` 只用于 provider 诊断。                                                                                                                                                                                                   |
| 子 shell 中缺少 `rea`，或 Node 不兼容                            | 检查实际的 shell PATH 与启动器/运行时。prefix 安装可能不在登录 shell 的 PATH 中；这不代表 MCP 注册损坏。                                                                                                                                                                                                                                                                                                                                                                                                             |

若客户端无法启动其 shell/沙箱 helper 或读取已安装的 skill，检查其启动诊断。
例如 CODEX_HOME 在 `/tmp` 下时 Codex 可能拒绝 helper 别名；
改用 OS 临时目录之外的已授权 profile。
REA 配置无法修复客户端的执行器。
保留沙箱，不要为了让分析命令跑通而悄悄禁用它。

静态 JavaScript 与普通 ZIP 清单既不需要 Hopper 也不需要 Ghidra。
HAR 检查是离线的，不需要活浏览器。
原生反编译、Android 分析与固件提取各有自备前提。
当受支持的清单/静态证据能回答部分问题时就用它，不可用的证据另行说明。
不要换目标。普通 shell 工具得到的观测要如实标注；
只有真实的 REA 输出才算 REA Evidence。

## 区分客户端与服务器时限

类似 `timed out awaiting tools/call` 的宿主消息且没有 REA 结果，
表示客户端时限在结果到达前已到期。
它不能确立 REA 已完成、已成功取消或已释放全部资源。
不要原样重复分析。只在有用时检查可用的会话/provider 状态与保留 Evidence；
空闲的 `binary_session` 不能证明所有无目标操作都已停止。
绝不编造缺失的 Evidence 引用。

让宿主工具时限覆盖执行、取消/清理与响应投递。
在 Codex 中，该设置是 `mcp_servers.<server-id>.tool_timeout_sec`，
单位是**秒**，不是 `startup_timeout_sec`。
为实际操作预算与余量选值，不要设一个万能超时。见
[官方 MCP 配置参考](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)。
只在授权范围内应用配置变更，保留无关条目与备份；
按宿主要求重连/重启。配置不可编辑时，报告所需的设置
或使用已授权的 CLI 后备。不要悄悄放宽权限或更换目标。

REA 返回的 `provider_timeout` 则表示**服务器/provider**到达其时限。
遵循其 `remediation.action`，复用可访问的部分 Evidence，
并在重试前解决已报告的未完成清理。
仅当返回的修复建议明确推荐时才修改请求字段或 `REA_*` 设置。
该文本说明值在启动时读取时，重启 REA。
提到某控件不会抬高时限，不是让你修改它的建议。
不要发明修复建议没有提到的设置。
只抬高客户端时限不会改变此服务器预算。
对静态 JavaScript，`analysis_timeout_ms`
（CLI 为 `rea analyze-javascript-application <path> --analysis-timeout-ms <milliseconds>`）
以**毫秒**控制每个源的启动、分析与传输时限。
任务允许时，增大该预算，或减少语义工作量/选择清单中确切的 `source_paths`。
要覆盖全部源则省略 `source_paths`；`[]` 无效。
`detail: "summary"` 减少投递，不减少分析工作。
单源预算不约束整个多源应用的总耗时。
部分 Evidence 检查可避免重复计算；
读取器不可用本身不构成阻止一次已修正的静态分析重试的理由。
简写 `rea analyze <path>` 不暴露该超时标志；
修改该预算时使用显式的 JavaScript 命令。

参数无效时，使用所连工具的当前输入 schema，或已装 CLI 的命令帮助。
目录过期就刷新；不要凭旧 skill 猜字段，
也不要为了修一个字段而返回整个目录。重试前修正所有被报告的字段。

## 恢复阶梯

遵循返回的修复建议。仅当该文本明确推荐时才修改请求字段或 `REA_*` 设置。
它说明值在启动时读取时重启 REA。提到某控件不会抬高限额，
不是修改它的建议。不要发明设置。
除非修复建议说明如此，宿主内存与 `NODE_OPTIONS` 不会抬高 REA 准入。

- MCP 连接断开：仅当该调用可安全重复或已知未开始执行时才重试一次。
  若它可能已改变目标，或再次失败，告知用户 REA 连接失败
  并请其重启 MCP 客户端。不要为断连本身运行 `rea doctor`。
- REA 无法建立连接：重试一次，然后告知用户并请其重启 MCP 客户端。
  REA 无法启动或该重启后工具仍缺失时运行 `rea doctor`。
  启动失败返回同样结果时不要重试。
- `cleanup_incomplete` 或错误详情中的保留清理所有者：
  重试那个确切的清理所有者。在该所有者确认释放之前，
  不要开始需要这些资源的新工作。重复原始调用不算这种重试。
- 容量：结果为 `resource_constraint` 且 `retryable` 为 true 时，
  等待当前准入完成，然后在报告的限额内重试。
  不要为了腾出槽位而重启 REA。
- `configuration_invalid`：错误报告 `update_mode: "runtime"` 时，
  对该设置调用 `update_analysis_settings`。报告 `update_mode: "parameter"` 时，
  修改该调用的参数；设置器不接受它。否则在启动 REA 的环境
  （shell 或 MCP 注册）中修正所指设置，然后再次启动 REA。
  运行 `rea doctor` 查看 `runtime-configuration:` 检查。
  当注册必须携带新设置时，为该客户端重新运行 `rea setup`，然后重连。
- `invalid_request`：按当前 schema 修正被报告的字段。不要原样重复调用。

## REA 以客户端插件方式安装

Claude Code、Codex 或 Cursor Marketplace 插件拥有自己的 `rea` 服务器与本 skill。
doctor 的 `--client` 与 `--skill` 检查以及 `rea setup`
只读写配置所有（setup-owned）的状态，因此对纯插件安装它们会报告 `missing`，
而执行 setup 会添加第二个 `rea` 服务器。
若本 skill 由插件加载，或客户端列出 `rea` 插件，
不要为缺失工具准备配置计划。改为：

- 用客户端自己的列表确认插件已安装并启用：Claude Code 中是
  `claude plugin list` 与 `/mcp`，Codex 中是 `codex plugin list`，
  Marketplace 安装则是 Cursor 的插件设置。
- 重启或重连客户端；工具仍缺失时读取其 `rea` 服务器的启动错误。
  Claude Code 与 Codex 启动插件自带的运行时；
  缺少构建或版本不匹配需要重装，从源码开发时则需重新构建。
  Cursor Marketplace 安装以插件 `mcp.json` 中固定的版本启动 `npx`。
  下载失败需要能访问该已发布版本的网络。
- 通过所连服务器的 `binary_session.result.tool_availability` 检查分析引擎。
  在 shell 中运行 `rea doctor --provider <id> --json` 报告的是该 shell 的环境，
  可能与客户端给插件服务器的环境不同。若仍要通过包运行器运行，
  使用插件 manifest 服务器条目固定的版本（`rea-agents@<version>`），
  不要用 `@latest`，以匹配插件启动的服务器。

仅当用户想要配置所有的注册来替代插件时，才使用下文的配置修复，
并先移除或禁用插件。

## 需要时修复注册

对 Codex：

```bash
rea doctor --client codex --json
rea setup --client codex --dry-run --json
```

使用当前受支持客户端的 ID：`claude_code`、`claude_desktop`、`codex`、
`cursor`、`gemini_cli`、`windsurf`、`devin`、`opencode`、`antigravity`、
`copilot_cli`、`commandcode`、`qwen_code`、`vscode`、`trae`、`grok_build`、
`omp`、`pi`、`hermes`、`qoder`、`droid`、`zcode`、`dsh`、`freebuff` 或 `grok_bot`。
不确定时，先检查 `doctor --json` 再选择范围。
`grok_bot` 使用聊天注册步骤而非本地 `mcp.json`。
不支持的客户端，用所选安装的绝对运行时与入口脚本做手动 stdio 注册，
或继续走 CLI。从目标项目之外的可信目录获取包。
注册使用包运行器期间，保持该安装及其运行时可用。

展示计划的确切路径、备份、变更与内置 skill 替换。
该具体范围未获授权时先取得写许可，然后用 `rea setup --client codex --yes`
应用同一范围。只在单独需要且明确批准时加 `--install-hopper`。
不要安装或升级无关的前提依赖。重启/重连，确认工具真实出现，
然后继续原任务。仍然缺失时，检查启动失败原因，而不是反复跑配置。

## Codex 工具审批独立于 REA 就绪状态

REA 工具没有权限授予握手。操作会创建自有资源、启动 helper 或有清理副作用时，
Codex 仍可能要求审批。宣告的工具或成功的 doctor 结果不能覆盖该客户端策略。
仅 `workspace-write` 不能解决 MCP 审批拒绝，
`approval_policy = "never"` 也不表示每个 MCP 工具都已预批准。

交互式审批可用时，对所请求操作使用客户端的审批流程。
无人值守运行中，执行环境允许时改走已授权的 CLI 工作流，
否则报告被阻塞的操作与继续所需的审批。
不要重试同一个被拒绝的调用，不要悄悄放宽审批，
也不要把 MCP 副作用改述为只读。

对明确想在一次性 Codex profile 中预批准指定操作的操作者，
当前 Codex 支持按工具配置。例如打开与关闭分析会话可分别授权：

```toml
[mcp_servers.rea.tools.open_binary]
approval_mode = "approve"

[mcp_servers.rea.tools.close_binary]
approval_mode = "approve"
```

使用实际的服务器 ID，且只对已批准效果的操作授权；
本例不批准检查、提取或运行时执行。
写入前展示拟议的配置修改并保留无关条目与备份。
托管策略可能约束客户端设置。已装客户端支持的设置见
[Codex 配置参考](https://learn.chatgpt.com/docs/config-file/config-reference)。
这是可选的恢复手段，不是每个 REA 任务的前提。

## 修复可编辑的 REA 限额

若 `details.limit` 指明可编辑设置及其范围，直接调用 `update_analysis_settings`，
`changes` 条目含 `setting`、`action: "set"` 与 `value`。
这些信息已在手时 `inspect_analysis_settings` 可省。
等工作与清理结束后原样重试同一输入。
运行时默认值只影响新工作；显式的每次调用参数优先，
被选用时必须直接修正。重置恢复启动值。
更新跨目标关闭/打开保留，但 REA 重启后消失。
它们不修改宿主时限、响应缓冲、注册或固定限额。

## 通过已安装的 CLI 继续

仅当启动器失败时检查命令环境：

```bash
command -v rea
command -v node
node --version
rea --version
```

子 shell 丢失 prefix 安装时，在 PATH 上受支持的既有 Node 环境下，
使用已知安装路径的公开启动器。
避免内部 `dist/cli.js` 入口或全局工具链变更。
shell 解析不到 `rea` 时，MCP 可能仍有自己的有效启动器。

对用户提供的 JavaScript 目录树或 ASAR，在授权工作区内选择输出文件，
并在读取视图前保存完整 Evidence：

```bash
rea analyze-javascript-application /absolute/path/to/app --json > app-evidence.json
jq -c '{source: {kind: "inline", evidence: .}, view: {kind: "summary"}}' app-evidence.json > app-view.json
rea inspect-analysis-view app-view.json
```

这些命令不注册 MCP，也不安装分析引擎。
CLI JavaScript JSON 是完整的且可能非常大；重定向到文件，不要载入上下文。
没有 `jq` 时用现成的 JSON 处理器，不要为这个配方专门安装。
用同样的内联 source 配合 [JavaScript 配方](javascript-applications.md)
检查模块分页或条目。保留图覆盖、限制与未知项。
原生 CLI 分析仍需所选引擎，且所有 CLI 操作继承宿主的执行权限。
