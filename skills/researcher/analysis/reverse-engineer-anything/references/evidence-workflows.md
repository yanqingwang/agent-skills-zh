> **中文汉化版** · 上游：[morluto/rea](https://github.com/morluto/rea) · 原文件：`.agents/skills/reverse-engineer-anything/references/evidence-workflows.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 证据、比较与验证工作流

产出证据的工具直接在 MCP `structuredContent` 与 CLI JSON 中返回完整的证据（Evidence）记录。操作数据读 `normalized_result`；当其他工具或你的说明需要一个稳定引用时，引用 `evidence_id`。保留权威性、局限、覆盖范围与残余未知项。如果某个结果不完整或已分页，只有在剩余数据对任务有影响时才继续；不要仅仅为了读取一个已经内联返回的结果就去取 bundle 或资源。当完整的 `inspect_binary_layout` 或 `analyze_javascript_application` 证据已经保留时，调用 `inspect_analysis_view` 获取摘要、单个 section/符号/模块，或一个稳定页面，而不是重复调用产出方。

对于任何声明了保留引用的逻辑证据来源，传入 `{kind: "retained-evidence", evidence_id}`，而不是把完整记录复制回调用中。同样的契约覆盖 native、process、JavaScript、managed、mobile 与 WASM 工作流中的单项、可选、数组与嵌套来源。各来源可以独立地混用内联记录与精确引用。解析过程保留来源的身份、来源信息、覆盖范围、部分事实与未知项；它既不重跑分析，也不会把不完整的事实变得完整。保持领域角色与身份要求：例如，原生 dossier 不能替代 managed 成员的观察结果。

从摘要页或检视页入手时，用它的 `normalized_result.parent_evidence_id` 引用完整来源。该视图自身的 `evidence_id` 只标识那个视图。`compare_artifacts` 明确支持产物摘要输入并解析其父级；不要假定每个消费方都支持这一点。当工作流沿着来源链接前进时，也让那些被链接的记录保持可用。

MCP 引用属于当前连接的台账（ledger）。若已知该 ID，直接传入；不需要发现调用，也不需要提供方配置。如果 ID 缺失，就导入导出的 bundle，或提供完整的内联证据。不要重试一个未改动的引用，也不要仅仅为了挪动已有记录而重跑产出方。当来源必须存活到会话结束之后时，在关闭会话之前导出。对于声明了 `--evidence-bundle` 的 CLI JSON 工作流，同一套引用 JSON 会针对一个显式选定的、已认证的 bundle 进行解析：

```bash
rea trace-application-feature request.json --evidence-bundle /absolute/path/evidence.json --json
```

这包括 JavaScript 追踪/比较与运行时对账、managed 重建/原生验证/图投影、Android/Apple/Harmony 图投影、WASM 接口比较以及保留的分析视图。managed 成员比较的 CLI 仍然接受两个程序集路径；进程比较接受两个捕获证据 JSON 路径。请查阅已安装版本的命令帮助。输入 bundle 不授予任何隐式的文件查找能力：`evidence-file` 与历史图文件选择器只被声明了它们的契约接受。参见 [CLI 复用指南](https://github.com/morluto/rea/blob/main/docs/cli.md#import-export-and-compare-evidence)。

已完成的 `inspect_artifact` 清单也支持摘要与 `view: {kind: "inventory", collection: "occurrences", logical_paths: ["package.json", "main.js"]}`。省略 `logical_paths` 则分页返回全部可用 occurrence；`[]` 表示一个都不选。其他清单集合还有 `nodes`、`edges` 与 `integrity_contradictions`。把 `source_complete` 与分页耗尽分开看：在部分来源的证据中匹配不到，不能确立不存在。后续视图使用返回的父证据 ID；当来源必须存活到会话结束之后时，在关闭会话之前导出。当 `tools/list` 声明了 `inspect_artifact.detail` 时，请求 `"summary"` 以保留其完整来源并立即收到该视图。没有这个声明选项时，保留现有的完整调用。CLI 检视返回可移植的完整证据；在投影选定的内联视图之前先把它保存下来。

对于原生的过程/名称/字符串清单，当已连接工具声明了 `detail: "summary"` 且任务需要计数或选定行时，就使用该摘要。用它的父证据 ID 配合 `view: {kind: "native-inventory", offset: 0, limit: 32, fields: ["value"]}`。搜索工具保留现有的 pattern/mode/case/document 选择。省略 `fields` 即返回完整记录；`record.address` 与 `source_index` 保留在选定行上。选择 `value` 会保留其字符串/解码限定条件。父证据 ID 加上源索引可以保留同地址的多个候选。只沿 `coverage.next_offset` 前进到问题所需的深度；耗尽保留的行并不能确立程序已被完整发现。

`batch_decompile` 会返回每一个函数体，除非你在已连接工具声明了 `detail: "summary"` 时选择它。用它的父证据 ID 配合 `view: {kind: "batch-decompile", collection: "items"}` 获取不含函数体的行以及确切的 `where.indices`、`addresses`、`procedure_addresses` 或 `statuses`。为若干个选定函数体加上 `include_pseudocode: true`，或用 `collection: "pseudocode"` 配合某一行的 `index` 来分页读取大型函数体。批量限制会汇总所有条目，因此不要把它们归到某一行成功结果上。

用 `record_unknown` 跟踪用户调查中的未决问题，并指明仍需要哪一方权威或哪种环境。提供支持性与相矛盾的证据 ID。它直接更新会话注册表。用 `update_unknown` 时带上当前修订号；遇到过期修订号就重新读取，而不是盲目重试。只有合格的观察证据才能验证一项结论。

在声称等价或不存在时，用完整且页面集合兼容的比较：

- `compare_artifacts` 按 occurrence 路径、内容、元数据与图关系比较清单页面。每一侧都写作 `{kind: "retained-evidence", evidence_id}`（一个 `inspect_artifact` 结果、其嵌套清单或它的摘要）或 `{kind: "evidence-file", path, evidence_id?}`，而不是重新发送证据。
- `compare_functions` 比较显式的函数证据，而不是模糊的整二进制匹配。它会拒绝 `analyze_function` 的摘要回复；请把该摘要的 `parent_evidence_id` 作为 `retained-evidence` 引用传入，或者传入完整 dossier。
- `compare_bundles` 比较规范化的 bundle 成员与未知项历史。
- `find_changed_behavior` 组合既有比较；静态差异仍然是候选，而不是因果证明。它的 `comparisons` 接受精确引用。
- `build_call_path` 需要来自同一个产物/提供方的显式函数 dossier；在 `functions` 中传入完整的父 ID。不完整的前沿会让"不存在"变成未知。
- `correlate_static_and_runtime` 使用显式映射；匹配的模式是假设，不是因果关系。两个比较数组都接受精确引用。
- `verify_reconstruction` 评估一份有限的有类型规格。通过只覆盖已声明的可比较论断，不代表全局等价。

进程捕获是可选接入的行为证据，不是安全沙箱。V3 捕获无法升级到 V4；请重跑原来的场景。区分根进程退出与后代进程结算，任务需要时要求新鲜度。一个必须写出最终报告的、超时的目标需要 `finalization_ms`：REA 向被捕获的根进程发送 SIGTERM，继续观察，并且仅当目标在该区间结束前仍未退出时发送一次 SIGKILL。`exit.finalization.signals` 列出每次尝试及其投递结果；观察到的退出信号留在 `exit.signal`，`exit.code` 对每次截止时间退出都是 null，自行退出的终结进程的退出码在 `exit.finalization.exit_code`（信号退出或未观察到退出时为 null）。

在保留的 `inspect_web_network_capture` HAR 证据上，用 `inspect_analysis_view` 配合 `view: {kind: "api-surface"}`，按 method、origin 与 path template 对观察到的请求行分组。格式匹配是推断，不是处理器身份或 schema。分组页引用父记录的序号；在声称完整性之前，先查阅记录覆盖范围与排除项。请求不会被重放。当已连接的 schema 声明了 `include_query_parameter_names` 时，在视图里选择它，以获取各自不同的观察到的名称及原始记录序号。查询值会被省略；名称既不能确立必需参数，也不能确立完整的服务器 schema。保留原始父证据以获取确切 URL。

在同样的保留 HAR 证据上，用 `inspect_analysis_view` 配合 `view: {kind: "environment-manifest"}`，把主 origin 的请求行投影为带 path template、参数、观察到的查询名称、不含值的 body 形状，以及指向 Agent 环境的记录指针。只在需要已记录的标识符时才启用 `template_rules`；每个 template、参数与合并后的兄弟项都是推断，不会复制任何 header、cookie 或 body 值，那三个声明过的未知项仍然无法解析。

用 `view: {kind: "environment-state"}` 配合 manifest 的 `template_rules`，提取这些读取所观察到的数据：实体类型与身份字段、带已记录值的实体、文档，以及逐工具的渲染计划（对照录制结果检查）。状态只来自首次相关写入之前的读取；类型、身份与列表成员关系都是推断。该视图还为每个会改变状态的工具给出写入计划；只有当后续某个已记录的读取确认了其效果且没有任何记录与之矛盾时，该计划才会被提供。`rea environment-serve manifest.json --evidence capture.json` 在启动时推导出该状态，用它回答读取工具，提供其计划被提供的写入工具（每个写入工具把自身效果应用到该状态），并在 `/agentenv` 上提供 `data/reset`、`data/add` 与 `data/get`；其他写入工具不被提供，而每个计划都在自己的 `reason` 中说明原因。当使用 `--replay-only` 或状态不可用时（无法推导，或目录超出发现预算），它改为重放该捕获，而它那个已停止文档的 `state` 说明哪些计划被应用了。

用 `view: {kind: "environment-coverage"}` 配合同样的规则，可以看到一个由捕获构建出来的环境会提供什么：读取工具由状态回答或被重放并附带原因，每个写入工具被提供或被扣留，并附带关于接下来该记录什么的提示；它不执行服务时的目录与状态规模检查。`rea environment-build <capture.har> <dir>` 一步完成检视、投影与导出，并打印同样的覆盖情况；当 bundle 提供的是重放时打印 `null`。

对于 PE/ELF 导出问题，`inspect_native_exports` 接受 `detail: "summary"` 并保留完整表格。用报告出的父证据 ID 查询 `inspect_analysis_view`，配合 `view: {kind: "native-exports", collection: "exports", names: ["selected_name"],
fields: ["name"], offset: 0, limit: 32}`。所有同名版本与别名都会保留；把 `source_index` 与父 ID 一起使用以获得稳定身份。`collection: "issues"` 分页呈现解析失败项。页面覆盖范围描述的是选定的保留行；`summary.coverage` 或 `exports.coverage` 描述的仍是源表格，因此一个空的部分页面并不能证明不存在。CLI 的 `inspect-native-exports --detail summary --evidence_output PATH` 会保存完整的 bundle，供后续 `inspect-analysis-view --evidence-bundle PATH` 请求使用。
