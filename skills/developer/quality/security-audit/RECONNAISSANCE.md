> **中文汉化版** · 上游：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) · 原文件：`skills/security-audit/RECONNAISSANCE.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 侦察

### Phase 1: 梳理源码并规划覆盖

Parent 初始化 `run-metadata.json`，执行 `SKILL.md` 中严格的侦察前预算关卡，然后在猎取之前创建 Agent 的 scratch 根目录和共享台账。关卡未通过时，把不完整状态记入元数据，不启动任何侦察 Agent。侦察只读取目标和本地可得的构建/配置状态。它不接触已部署端点、外部身份提供方、注册表、消息中间件、云 API 或其他共享服务。

并行启动若干 `research` Agent。它们向 Parent 返回结构化事实，不写文件。

**Agent 1a：产品、技术栈与本地运行**

```text
Read the target at <target>. Do not use network access. Return:
1. Product type, users, operators, and ordinary trust-sensitive actions.
2. Languages, frameworks, build system, runtimes, and locally visible deployment models.
3. Repository-relative entry points and subsystem boundaries.
4. Exact build and test commands that could run offline with local dependencies, their expected write locations, and the target-controlled inputs they process. Do not run them during reconnaissance.
5. Comparable software or protocol visible from local documentation and dependencies. If no useful comparison is source-grounded, say so.
6. Missing local toolchains or runtime facts that limit bounded execution.
Return only source facts with repository-relative file:line references.
```

**Agent 1b：主体、权限与控制**

```text
Read all source that establishes identity, authorization, isolation, and privilege. Map:
1. Each lower-trust principal and the actions it has by design.
2. Authentication or peer identity at each entry surface.
3. Per-resource authorization and tenant/owner scope.
4. Process, browser, workload, CI, plugin, model/tool, device, or local-IPC authority.
5. Privilege changes, confirmation, revocation, recovery, and fallback paths.
6. Which controls are source-visible and which depend on an unobserved deployment fact.
Return trust boundaries and control locations with repository-relative file:line references. Do not infer live reachability.
```

**Agent 1c：入口面、副本与 sink**

```text
Inventory every source-visible place external or lower-trust input enters:
- HTTP/browser, RPC/message/protocol, files/archive/document, CLI/env/config, plugins/dependencies/CI, cloud events/IAM selectors, model context/tool arguments, mobile/deep-link/webview, and local IPC.
For each surface, follow major transformations, stored or derived copies, and security-relevant sinks. Record source-visible limits and parallel paths to the same effect.
Return repository-relative paths and line numbers. Be complete, but do not execute or send inputs.
```

**Agent 1d：本地执行与部署可见性**

```text
Read tests, build definitions, manifests, packaging, and maintained environment overlays. Return:
1. Small offline tests or existing fixtures that could validate trust boundaries with dummy data inside the required OS-enforced sandbox.
2. Processes that could use an isolated loopback network namespace without external or shared dependencies.
3. Commands that would fetch dependencies, publish artifacts, contact paid/provider APIs, or affect shared state; mark them prohibited for this run.
4. Deployed controls and attachments that source cannot establish and therefore require needs_validation if decisive.
5. The final active source path for each deployment mode only where the repository selects it deterministically.
6. Whether the local platform can enforce an empty allowlisted environment, no external network, read-only target/toolchain mounts, scratch-only writes, and explicit CPU, memory, process, file-size, disk, and wall-clock limits. Missing controls block target-controlled execution.
7. Whether trusted parent-side code can promote predeclared scratch files with path-confined no-follow descriptor traversal, nonblocking regular-file checks, no-follow traversal of every destination parent, exclusive regular-file destination creation, and explicit per-file and cumulative size bounds. Missing promotion controls block use of scratch files as evidence.
```

对这四个 Agent 没有覆盖到的重要差异部署模式或子系统，追加针对性侦察 Agent。不要静默省略：如果 `SKILL.md` 的预算关卡挡住了某个针对性 Agent，就不要为它启动任何东西，把未覆盖区域播种为一个 `deferred` 台账单元，原因为 `budget_cannot_reserve_critics_and_validation`，并在报告中披露这一缺口。

## 先前运行输入

在选择工作之前，Parent 读取同一仓库所有可用的先前 `coverage-ledger.json` 和 `findings.json`：

- 把每条先前记录和单元的源码位置、控制、条件以及源码派生的身份，与当前源码比对。
- 仅当先前 `confirmed` 记录的相关源码、条件和合格证据仍然成立时，才把它以相同指纹携带进当前候选集。把它链接到一个当前 `planned` 单元，`prior_status` 为 `"prior_confirmed_same_source"`，且只把该根因放进猎手排除清单。重新验证该携带记录的 Phase 3 验证者成为该单元的分配所有者；其源码复查是该单元的第一次检查，并把单元带着携带的指纹移入 `candidate`。
- 当任何相关源码或条件变化时，构建一个当前计划中的 `prior_confirmed_changed_source` 重验单元。不要把该根因排除出猎取范围，也不要假设先前判定仍然成立。
- 为每个先前 `needs_validation`、`deferred`、`blocked`、`out_of_scope` 和变源单元构建当前工作单元。这些状态是优先级输入，绝不用作去重或抑制键。
- 仅当当前源码支持其 trace 时，才以相同指纹携带仍然被阻塞的先前 `needs_validation` 记录。把它链接到一个当前 `planned` 单元，`prior_status` 为 `"prior_needs_validation"`；该记录保留未解决阻塞项。复查该携带记录的 Phase 3 验证者成为该单元的分配所有者；其复查是该单元的第一次检查，并把单元带着携带的指纹移入 `candidate`。把该记录纳入最终验证。
- 先前 rejected 记录视为过期断言，除非当前证据改变了失败的 trace 或缺失的条件。未变化的拒绝只抑制那一条断言，不抑制对该覆盖单元的审查。
- 记录缺失或不兼容的台账，而不是把它们当作空覆盖。

把用到的路径和源码 ref 写入 `run-metadata.json`。`architecture.md` 里只总结覆盖影响。

## 架构摘要与配套文件选择

Parent 撰写 `<output-dir>/architecture.md`，硬上限约 1,000 词。包括：

1. 产品、主体、常规权限与受保护资源。
2. Agent 1a 给出的同类软件基线（当它有源码依据时）：该同类软件接受了哪些安全权衡。用它校准投入与严重程度，绝不用它否定一条已论证的发现；如果同类软件在实践中也踩过同一个缺陷模式，这反而加强该发现。没有有意义的同类软件时省略此条。
3. 技术栈、源码可见的部署路径和离线构建/测试限制。
4. 入口面和重要的源码到 sink 或生命周期路径。
5. 信任边界及每条边界上最强的源码可见控制。
6. 仓库相对的起始路径。
7. 先前覆盖缺口、变源与被阻塞的重验目标，以及同源已确认的排除项。
8. 依据 [ATTACK-CLASSES.md](ATTACK-CLASSES.md) 得出的简短配套文件选择摘要：选中的文件，以及需要它们的源码可见边界。

分配级的普通攻击类别块、选中的配套块和带原因的排除块保存在每个台账单元里，不放进 `architecture.md`。这样架构摘要的上限对大规模运行依然成立，精确的猎手提示词映射也可被机器校验。

不要仅因为出现某个语言或依赖名就选择配套文件。选择它的理由是侦察发现了其 `When to use this file` 小节描述的信任敏感边界。不要只因为另一个 Agent 会审查相关类别，就排除一个可见边界。

## 确定性覆盖台账

Parent 把 `<output-dir>/coverage-ledger.json` 写成顶层 JSON 数组。按运行档位设定的粒度，为暴露面、信任边界、子系统和适用普通/配套攻击类别的每个重要组合派生一个单元（`quick` 用一个全范围内子系统标识；`deep` 额外加入生命周期模式）。限定范围的运行要为分配播种范围内的面，并把发现的被排除面保留为 `out_of_scope` 单元，让以后的完整运行能把它们变成当前工作。

每个维度都有一个人类可读标签，以及 `canonical_refs` 里一个稳定的源码派生值。同一源码对象跨运行使用同一个规范引用，即使其展示标签变化。合适的引用包括：仓库相对入口路径加导出范围、源码中定义的路由或消息标识、定义边界的源码控制、仓库包路径，以及精确的攻击类别块引用。块引用是 `FILE.md#` 加该文件中以粗体或标题形式书写的精确类名，它是用来与文件文本匹配的稳定标识符，不是渲染后的 HTML 锚点。配套小节块用括号限定语之前的标题文本（例如 `Core discipline`）。不要通过小写化或 slug 化展示标签来派生引用。

派生 `coverage_id` 时不做有损 slug：

1. 要求每个引用为 Unicode NFC，含有效标量值、有可见内容，不含控制、格式、行/段分隔符或默认可忽略码点，且首尾无空白。
2. 用 RFC 3986 百分号编码其 UTF-8 字节：只有 `A-Z a-z 0-9 - . _ ~` 保持不转义，其余每个字节用大写 `%HH`。
3. 用 `::` 连接编码后的 `surface`、`boundary`、`subsystem` 和 `attack_class` 引用；存在 `lifecycle` 时追加其编码值。

quick 档位粗化后的子系统维度使用固定规范值 `profile/quick/all-in-scope-subsystems`。引用或 ID 中不要包含波次号、Agent、判定、严重程度或行号。每次分配之前按 `coverage_id` 字典序排序单元。遇到重复 ID 即失败。如果重复 ID 的语义字段不同，视为规范标识冲突；绝不合并或静默覆盖。校验器同样拒绝用不同规范引用表示同一个语义元组。

每个单元记录：

```json
{
  "coverage_id": "...",
  "canonical_refs": {
    "surface": "src/router.ts#POST /users/:id",
    "boundary": "src/authz.ts#requireOwner",
    "subsystem": "packages/api",
    "attack_class": "ATTACK-CLASSES.md#Access control"
  },
  "surface": "...",
  "boundary": "...",
  "subsystem": "...",
  "attack_class": "...",
  "starting_paths": ["repo/relative/path"],
  "ordinary_attack_class_block": "ATTACK-CLASSES.md#Access control",
  "selected_companion_blocks": ["FILE.md#section"],
  "excluded_blocks": [{"block": "FILE.md#section", "reason": "..."}],
  "prior_status": "new|prior_confirmed_same_source|prior_confirmed_changed_source|prior_needs_validation|prior_deferred|prior_blocked|prior_out_of_scope|prior_covered_same_source|prior_covered_changed_source|prior_rejected_claim_changed|none",
  "attempts": [],
  "wave": 1,
  "status": "planned",
  "agent_id": null,
  "reviewed_paths": [],
  "local_checks": [],
  "result_fingerprints": [],
  "unresolved": []
}
```

`lifecycle` 为重要维度时，同时添加 `canonical_refs.lifecycle` 和人类可读的 `lifecycle` 字段。`ordinary_attack_class_block` 只在没有适用普通块时为 null。选中的配套列表包括每个适用类别及其配套的 `Core discipline`、`Universal moves` 和 `Validation rules`；`excluded_blocks` 记录每个考虑过但未选中的块，以及排除它的源码事实。

Parent 可以添加簿记字段，但保持上述语义字段稳定。在 `prior_status` 中，`new` 表示存在兼容先前台账时本运行首次见到的面；`none` 表示没有可用兼容先前台账时播种的单元。先前 `deferred`、`blocked`、`out_of_scope` 和变源单元，在现已进入范围时初始化为当前 `planned` 工作。先前同源已覆盖单元在当前台账中保持可见；先分配变源、重要生命周期路径和精确冲突，再用覆盖评审者决定它是否需要再过一遍。

`attempts` 是只追加的存档，保存被覆盖评审者重新打开的带证据分配。重新分配之前，追加先前单元的准确 `wave`、`status`、`agent_id`、`reviewed_paths`、`local_checks`、`result_fingerprints` 和 `unresolved`，外加评审者有源码依据的 `reassignment_reason`。只有 `blocked`、`covered` 和 `candidate` 状态可以归档。归档的尝试保持与活动单元相同的状态和证据不变量，使用严格递增且低于当前波次的编号，并保留其产出所有者与产物。下一次分配递增 `wave`，使用新所有者，从空的活动证据开始。如果档位或预算不允许再次分配，递增 `wave` 并使用 `deferred` 活动状态，所有者为 null、证据为空，附停止原因。绝不把归档所有者的检查或产物复制进活动状态。后续的活动终态只包含新尝试的证据；存档保持不变。

严格执行这张状态表：

| Status | 单元 `agent_id` | `reviewed_paths` / `local_checks` | `result_fingerprints` | `unresolved` |
|---|---|---|---|---|
| `planned` | null | 空 | 空 | 空 |
| `not_applicable`, `out_of_scope`, `deferred` | null | 空 | 空 | 非空原因 |
| `in_progress` | 规范所有者 | 空 | 空 | 空 |
| `blocked` | 规范所有者 | 两者均为非空的所属部分证据 | 空 | 非空阻塞项 |
| `covered` | 规范所有者 | 两者均非空 | 空 | 空 |
| `candidate` | 规范所有者 | 两者均非空 | 非空 | 可选 |

规范 Agent ID 匹配 `^[a-z0-9][a-z0-9_-]{0,63}$`，且不是 Windows 设备名。必须小写，因此一个台账不能包含大小写折叠的别名。单元的 `agent_id` 记录分配所有者。每个检查记录自己的 `agent_id` 和非空 `reviewed_paths`；单元级 `reviewed_paths` 恰为它们的并集。纯源码检查用 `artifact: null`。本地检查要求一个仅由可信父端代码提升到 `agents/<check.agent_id>/artifacts/` 之下的常规文件。这让猎手检查与验证者检查得以共存于一个单元。scratch 路径、输出根文件、符号链接、特殊文件以及另一个检查所有者的产物都不是证据。

台账就是覆盖声明。架构摘要、Agent 数量或泛泛的一句"审查过认证"都不是覆盖证据。Phase 2 只根据猎手结构化结果中的路径和检查关闭单元。

在播种之后、每次 Parent 更新之后以及 Phase 6 之前，运行 `node <skill-dir>/validate-coverage-ledger.cjs <output-dir>/coverage-ledger.json`。校验器拒绝超过 5 MiB、64 层嵌套、10,000 个单元、嵌套集合 1,000 个条目或 500,000 个遍历值的输入，并把报告的校验错误截在 100 条。实践中 5 MiB 字节上限大约容纳 2,000-5,000 个真实单元，所以它会先于 10,000 单元上限生效。分配工作或声称覆盖之前，修掉所有错误。
