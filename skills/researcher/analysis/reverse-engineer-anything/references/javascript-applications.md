> **中文汉化版** · 上游：[morluto/rea](https://github.com/morluto/rea) · 原文件：`.agents/skills/reverse-engineer-anything/references/javascript-applications.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# JavaScript 与 Electron 应用产物

对需要恢复可读源码的已捕获或已打包 JavaScript，使用 `recover_javascript_sources`，
传绝对 `path`，且 `output_directory` 不要已存在。
schema 支持时，在 `additional_paths` 中提供相关的运行时/共享/懒加载文件，
然后一并分析返回的 `analysis_input` 目录。
每个输入保留自己的快照、摘要与字节区间来源；输入与还原出的代码绝不执行。
还原需要调用方在 Linux x64 上提供 Wakaru；
详见 [还原指南](https://github.com/morluto/rea/blob/main/docs/guides/javascript/javascript-recovery.md)。

对操作者提供的 ASAR 或已解包目录直接使用 `analyze_javascript_application`。
当问题涉及已知源路径且所连 schema 宣告了 `source_paths` 时，
选择清单中的确切路径，如 `["package.json", "main.js", "preload.js"]`。
显式包含辅助的 manifest 或 source map；依赖不会被隐式分析。
REA 保留完整的产物清单与身份，但只读取并分析选定文件的源文本。
结果与摘要记录 `source_selection`；范围外文件及其关系保持未知，
因此部分应用覆盖不代表所选源有问题。
两条静态应用 CLI 路线都支持重复 `--source-path`；选择列表过长一行放不下时，
用 `--source-paths-json` 传 JSON 文件。问题要求完整应用分析时省略该选择；
`source_paths: []` 是无效值，不是"不过滤"的请求。
`detail: "summary"` 只减少投递量，本身不减少分析工作量。

ASAR 头部/索引准入默认 16 MiB / 16777216 字节；准入错误会指出
`asar.max_header_bytes` 及其范围（上限 256 MiB）。
用该设置、`action: "set"` 与足够的字节数调用 `update_analysis_settings`，
然后原样重试整个归档请求。无需检查或重启 REA。
`REA_ASAR_MAX_HEADER_BYTES` 为未来的 REA 进程提供启动种子。
`source_paths`、`detail` 与 `max_heap_mb` 不会绕过或抬高头部准入。
运行时 JavaScript 的超时/堆默认值也可编辑；
显式的每次调用 `analysis_timeout_ms` 与 `max_heap_mb` 优先。

精确的 `#alias` 指定符通过导入方所在包的 `imports` 映射解析为包内文件；
嵌套的 `node_modules` 包使用自己的映射。
通配符、递归与外部包导入目标在该限制下保持未解析。
大小未知或很大且所连 schema 宣告 `detail` 时，请求 `detail: "summary"`。
这会返回一条带独立 ID 的 `inspect_analysis_view` Evidence 记录，
其 `normalized_result.parent_evidence_id` 指向完整保留的应用分析。
source map 内容属于该静态分析的一部分。
先读发现、覆盖、限制与未知项，再追问一个具体的未答问题。
不支持 `detail` 的旧服务器在放得下时内联返回完整应用 Evidence。

所连 schema 宣告 `max_heap_mb` 与 `analysis_timeout_ms` 时，
它们分别设定隔离源分析器的老生代堆与单源时限。
默认为 1024 MiB 与 300000 ms。它们不改变 MCP 进程堆或客户端的工具时限。
主机超时且无 REA 输出时，使用
[时限恢复指南](connection-and-recovery.md#distinguish-client-and-server-deadlines)，
而不是调高服务器预算。Bun 承载的 REA 不强制堆选择；
在 Windows 上它改为把分析器的已提交内存限制为该值加 512 MiB 运行时保留。
受资源限制的分析会保留已完成的静态事实，
并报告部分语义覆盖与具体的未知范围；这不代表源码格式有问题。
重试某个源之前先检查这些限制。
当展开的关系超出父 Evidence 的可用内存时，检查该文件的 modules 条目视图，
其中有保留的 `static_analysis` 与 `semantic_module_analysis`。
即使图关联未知，这些事实仍然可用。
结果总量耗尽可能在检查完每个文件之前终止分析；
清单与剩余未知范围可区分这种情况。
源分析开始后的超时或取消会在同一会话中保留部分 Evidence。
返回的 `error.details.partial_observation` 引用可直接提供给 `inspect_analysis_view`。
若 SDK 在本地取消，先从 Evidence bundle 取回其记录的 ID，再检查部分分析。

## 盘点路由候选而不返回应用图

宣告的 schema 支持 `view` 时，用 `detail: "summary"` 配合
`view: {kind: "javascript-routes", collection: "routes", fields: ["path", "confidence"], limit: 20}`。
对已选定的已捕获源，同样的视图也适用于 `analyze_web_bundle`。
完整源 Evidence 已保留；用其 `parent_evidence_id` 配合 `inspect_analysis_view`
读取 `summary`、`routes`、`occurrences`、`sources` 或 `unknowns`。
请求更多字段前先过滤并批量传 ID，并跟随 `coverage.next_offset`。
CLI 的 summary 选择需要 `--evidence_output` 才能保留完整记录。
静态模式、推断的部署基址、启发式框架分类与不可用源，
都不能确立路由可达性或完整的应用路由分母。
详见 [路由盘点指南](https://github.com/morluto/rea/blob/main/docs/javascript-route-inventory.md)。

对已捕获的端点观测与推断事实，`analyze_web_bundle` 也接受
`view: {kind: "web-bundle", collection: "endpoints", limit: 32}` 配合 `detail: "summary"`。
后续 `endpoints`、`inferences` 或 `summary` 页从保留的父 Evidence 读取。
请求细节前先过滤；追溯来源时保留 `source_index` 连同父 ID 与集合，
并请求 `location` 或 `basis`。分页耗尽不代表产出完整：
检查 `completeness`、结构化的 `source_unknowns` 与限制项。
端点候选仍是推断，不是已确认的网络行为。

## 读取模块而不重复分析

在同一连接上用实际返回的父 ID 作为 `source.evidence_id`。
下面的 ID 都是占位符，请替换为返回值。
模块的 node ID 未知时，先分页读取身份列表再选条目。
分页只返回 node ID、路径与角色；选择合适的页大小，
需要更多页时跟随 `coverage.next_offset`：

```json
{
  "source": {
    "kind": "retained-evidence",
    "evidence_id": "ev_ACTUAL_PARENT_ID"
  },
  "view": { "kind": "page", "collection": "modules", "offset": 0, "limit": 16 }
}
```

按确切的 `node_id` 与已记录角色选择相关页条目：

```json
{
  "source": {
    "kind": "retained-evidence",
    "evidence_id": "ev_ACTUAL_PARENT_ID"
  },
  "view": {
    "kind": "item",
    "collection": "modules",
    "selector": { "node_id": "jag_node_ACTUAL_NODE_ID" }
  }
}
```

模块分页包含 asset、bundled 与 source 模块角色，因此一个路径可能对应多个条目。
只在唯一性已确立时才用 `selector.path`；
返回的 node ID 让你无需完整清单即可证明唯一性。
有歧义时，从分页或错误的候选项中选出匹配的 node ID。
需要更多页时跟随 `next_offset`。条目暴露该模块节点已记录的观测、
身份、哈希、导出与源区间；它不包含每个子语法观测、相关边或原始源文件。
条目缺失某个事实不代表整个应用中不存在。

要规范身份与保留源区间计数时，用类型化引用分页，而不是读每个完整条目：

```json
{
  "source": {
    "kind": "retained-evidence",
    "evidence_id": "ev_ACTUAL_PARENT_ID"
  },
  "view": {
    "kind": "javascript",
    "collection": "modules",
    "projection": "references",
    "where": { "path": "main.js", "kind": "javascript-module" },
    "offset": 0,
    "limit": 16
  }
}
```

过滤器匹配确切的保留字符串；省略某过滤器即包含所有值，
`path: null` 表示路径不可用，`path: ""` 表示记录到的空路径。
行保留规范 `identity`，并在 `basis` 中区分观测支持状态。
`retained_source_range_count` 统计保留的源区间观测数，
不是运行时导入或唯一引用点数。
用行的 `node_id` 配合上面的条目视图获取确切位置与完整支撑观测。
跟随 `coverage.next_offset`；分页耗尽只描述匹配到的保留行。
得出否定结论前，先检查 `source_coverage` 的源选择、
部分/未知图覆盖与未知计数。

## 只追踪剩下的那个问题

在父应用 Evidence 上用 `trace_application_feature` 追踪一个字面量 node ID、
路由、字符串、API、IPC 通道、模块或原生导出。
`incoming` 选指向种子的关系，`outgoing` 选离开种子的关系，
问题两者都需要时选 `both`。追踪遍历包含包含关系（containment），
因此即使种子很窄也可能展开大量节点；
双向追踪可能到达无关的兄弟模块。
条目或分页的观测已能回答问题时，优先用它们。
不要把所有到达的节点都当作该功能的参与者。
大范围追踪时，传 `view: {"kind": "feature-trace", "collection": "paths"}`
（或 `summary`）以保留完整追踪并先读终端路径；
需要时用 `inspect_analysis_view` 配合确切 `where.node_ids`
对 `nodes` 或 `edges` 分页。

服务器宣告支持时复用保留的父 Evidence，否则内联提供完整 Evidence。
仅当 Hopper 或 Ghidra Evidence 的产物摘要完全一致时才纳入。

## 恢复超大展示

超大响应会报告 `resource_constraint` 与 `details.resource: "transport"`。
用 `details.reported_limits.evidence_reference` 配合 `inspect_analysis_view`
获取摘要、单个模块或稳定的模块身份分页。
`export_evidence_bundle` 把完整的规范会话写到调用方选定的文件。
这些流程保留原始 Evidence 与覆盖；大范围的后续调用同样可能超出线框限制。

客户端可能在文本信封内截断成功结果，而 REA 并没有报 `resource_constraint`。
把截断提示或不完整 JSON 视为展示限制；不要声称已检查完整记录。
用已知父 ID 取更小的视图，或在会话仍开着时把完整 Evidence 导出到选定文件。
若预览中丢失了父 ID，用先前的分析摘要或显式台账条目找回；
不要编造 ID，也不要为了复现同样展示而重跑分析。

BrowserWindow 偏好、preload 与 contextBridge 面、IPC 注册、utility 进程
与原生绑定请求都属于静态语法观测。
只有唯一且精确的字面量 IPC 通道匹配才支持推断配对。
动态或有歧义的通道保持未解析。
被引用的 `.node` 成员不是已验证的原生导出。
绝不从静态分析断言运行时可达性、注册、默认值或策略执行。

版本对比：每个版本各分析一次，然后调用 `compare_application_versions`。
只接受其摘要、source map、结构指纹或非模块语义匹配。
模块序号与压缩后的名称不是持久身份。
只有在另一侧覆盖完整时才报告新增或移除；否则报告未知。

当问题是一个确切导出可调用物的返回对象形状如何变化时，
每个版本各分析一次，然后用显式模块路径与导出名调用
`compare_javascript_export_shapes`。两次分析调用使用同一连接上返回的 ID，
或完整内联 Evidence 记录。只接受通过该工具唯一精确字面量判别子建立的
变体配对。把 `unknown` 解读为"该名称未被观测到"之前，
先读 `property_inventories` 与每个变更的 `presence`：
清单会列出已观测的属性名，即使值仍未知，
每个配对或未配对变体都带 `source_range`。
数组空洞与被变更失效的槽位不算已观测属性。
父覆盖完整时，仅凭存在性的 `added`/`removed` 会被独立报告，不受未解析值影响。
引用对比 Evidence 并报告 JSON Pointer 变更；
动态值、歧义变体与不完整的父属性覆盖保持未知。
这是静态推断，不是运行时行为。需要运行时语义时，
对相关应用版本运行行为探测，并通过可用的浏览器、Electron 或进程工作流捕获。

## 复用应用 Evidence

所连服务器宣告支持时，应用追踪与对比工具的应用输入（`application`，
或 `left`/`right`）接受完整内联 Evidence 或
`{"kind":"retained-evidence","evidence_id":"ev_<64 lowercase hex characters>"}`。
`inspect_analysis_view` 在 `source` 中使用同样的保留引用形式或可移植内联
Evidence，投影出摘要、模块分页或带已记录观测的单个模块。
该记法只是模板：请替换为实际返回的 ID。
4.1.0 之前的版本只接受完整内联 Evidence。
使用同一 MCP 连接上生产方返回的确切 ID。
引用解析不运行分析、不选择 provider；发现仍然内联。
摘要或检查回复请选用完整的 `normalized_result.parent_evidence_id`。
原生观测数组与运行时对账的 `static_layers[].analysis` 与
`runtime_observations[]` 在宣告支持处也接受确切引用。
每个源可独立选择内联或保留，身份、覆盖与未知项都保留。
宣告 `--evidence-bundle` 的 CLI 工作流从显式选定的 bundle 解析这些输入。
`close_binary` 释放引擎，但在同一 MCP 连接上保留引用与完整 Unknown 历史。
`reset_investigation` 显式清除它们；可选 `save_path` 在清除前对完整 bundle
做检查点。在另一个连接导入该 bundle 可恢复其原始引用。
保留是有界的、内存中的，且绝不静默驱逐；
`binary_session.investigation` 报告预算。
缺失引用会附带其 ID 与恢复指引。

需要精确的文件/原生元数据或处理缺口时，用
`view: {kind: "javascript-facts", where: {paths: ["package.json"]}, property_keys: ["name", "operation", "analysis_status"], limit: 32}`。
行保留规范的节点/观测身份与原始 Evidence。
路径匹配 Evidence 的 artifact-path/source-range 位置；
缺失属性保持省略，源覆盖与分页耗尽相互独立。
批量传路径并只取需要的属性键；完整 Evidence 始终可通过导出访问。
名称未知时选择 `include_available_property_keys: true`；
它会列出每个返回观测的原始键，但不带未选值。
组合事实时保持每行的节点/观测身份成对。
这些行只选取应用图观测；语义关系与语义未知记录
仍留在完整父 Evidence 与追踪工具中。
