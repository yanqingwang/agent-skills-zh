> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/archify/references/delivery-contract.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 交付契约

## finalize 失败与候选修复

`finalize` 在第一个未通过的闸门处停下。使用紧凑 stdout 或 `evidence.summaryReceipt`；只有当摘要缺少做出连贯修复所需的证据时，才去读它的完整 sidecar。一份只含四项 artifact 检查的回执只是基础校验，不是 showcase 验收：要求全部九项检查、零构图错误、零警告。先修 `meta.quality_profile` 与 schema 错误，再动几何。一张密集的全 schema ERD 在第一轮完整字段检查时可以保持 `standard`：要求零结构错误、无边穿过节点的失败、字段行完整、分组网格可读，并把构图警告记录下来，而不是在上面花无上限的时间。

遇到校验失败时，先按诊断指出的连通邻域修改既有 JSON，再重跑命令。保留请求的语义、有意义的标签、来源证据，以及已固定或已商定的拓扑。多条路由共享节点时需要做一次布点修复；该情况请阅读 [架构布局修复](architecture-layout-repair.md)。主路径被阻挡时做重排（reflow），而不是去挪动无关标签。无关几何的构图已经清晰可读时，保持不动。只有在紧凑证据缺少所需测量值时，才在修改前使用 `--layout-json`。Workflow v2 以其稳定的编译器回执作为创作证据，而不是求解器内部状态。

在视口修复之前，先保留通过路由检查的最佳候选。如果该修复引入了新的路由碰撞，恢复被测量的布局，并处理其剩余的画布或文本约束。

编辑之后，用 `--quality showcase` 重跑完整的 `finalize` 命令；对基于仓库的工作，还要带 `--repo-root <repo-root>`。如果输出路径已有来自另一个候选的浏览器证据，为新的 `finalize` 和任何 `visual-check` 都使用全新的 `--out-dir <output-stem>.review-<revision>`。编辑后省略先前的 `--candidate-sha256`，因为它绑定的是上一个候选。比较诊断时按代码、主体、阶段与证据来比较，绝不要只看错误数在下降。按持续存在的问题逐个跟踪修复上限，依据就是该问题的代码、主体、阶段与证据：新暴露的问题启动自己的修复序列。一个问题熬过两次聚焦修复仍未解决时，检查测量几何或相关契约；再做一次基于证据的重试之后，报告具体缺口。

独立的 `validate` 只用于聚焦诊断，基于仓库的工作要传 `--repo-root`。它的通过回执标记 `candidateFrozen: true`；运行 `nextAction.arguments`，只替换 `<output.html>`，不编辑、不重新校验、不重读候选。之后出现的环境或证据失败，针对这些冻结字节重试。有确切理由要修改时会创建新候选，此时调用完整 `finalize` 且不带旧哈希。

## 校验与交付

`render` 与各直接渲染器入口把已分类的创作失败以可读诊断
打印到 stderr，并以 1 退出。输入读取/JSON 解析失败
使用 `input/read` 或 `input/json-parse`；输出文件系统失败使用
`output/write`，并指明输出路径。schema 与布局失败保留
其既有规则码。要机器回执，使用对外公布的 `validate --json` 或
`deliver --json` 接口；`render` 没有 `--json` 标志。
意外实现失败在人类模式下保留调试信息，
在机器回执中保持为 `internal/unclassified`。

每个交付输出有两个 artifact 专属元数据路径。当输出 stem 对
这些派生文件名来说太长时，Archify 会缩短它并追加
一个稳定哈希：

- `<output-stem>.delivery.json` 记录最近一次已完成的尝试。
- `<output-stem>.delivery-pending.json` 是进行中
  尝试的恢复日志。

对于恰好撞上 Archify 保留的有界命名标记的字面 artifact stem，
当编码版 sidecar 不存在时，命名空间化之前的原始溯源 sidecar 仍可作为读取回退。命名空间化之前
的原始 pending 日志是独立的 fail-closed 屏障：即使编码版 pending 日志也存在，它照样
阻断检查与重交付，且两种日志
都不会被静默替换。

一个目录级 `.archify-delivery-lock.json` 把所有解析到同一物理输出目录的交付串行化。这是有意
为之，防止大小写、Unicode 规范化、Windows 短名与符号链接别名
给同一文件系统位置制造独立的所有者。代价是：
同一目录下交付到不同 artifact 名的操作也要串行；
溯源与 pending 日志仍按 artifact
区分。

为了迁移安全，Archify 还会检测并保留请求 artifact 旁边的旧版
`<output-stem>.delivery-lock.json`。已存在的旧版条目是一道 fail-closed 恢复屏障。
新交付持有目录互斥锁期间，还会同时持有针对请求拼写与既有 artifact
物理目标拼写的临时旧格式围栏（fence）。
它先获取目录锁，然后在写入日志或 artifact 之前取得所有必需的兼容围栏；释放时
先移除目录锁，再移除那些围栏。这样能阻止使用任一已知拼写的旧版 Archify 二进制
进入交付。若某个旧版围栏的原始 HEAD 时代文件名超出宿主的组件长度限制，
则将其省略，因为旧二进制在该宿主上也同样无法创建那个锁或交付那个 artifact。

`deliver` 在创建或替换恢复日志之前，用独占的 `open(..., "wx")` 取得锁。
独占创建成功会产生一个绑定到该次尝试的内部不透明所有权能力（capability）。
日志创建、失败溯源记录、成对提交、回滚、日志终结与
锁释放，每一步都在会改动共享状态的操作内部核验当前能力。
被拒绝的竞争者不会创建日志，
也不会写入失败溯源。

已存在的目录锁或旧版锁按以下方式处理，不做自动恢复：

| 观察到的锁状态 | 要求的 `deliver` 结果 |
| --- | --- |
| 无目录条目 | 尝试独占创建；只有其成功才授予所有权。 |
| 合法的 schema-v1 锁，其 PID 正在运行，或无法确认其进程已死 | 以 `delivery/concurrent-attempt` 退出 1；保全每个共享路径。 |
| 合法的 schema-v1 锁，其 PID 已确认退出 | 以 `delivery/lock-stale` 退出 1；原样保全锁、artifact、日志与当前溯源。 |
| 不可读、格式错误、符号链接、悬空符号链接、目录或其他非普通文件的锁条目 | 以 `delivery/lock-invalid` 退出 1；保全该条目与所有其他共享路径。 |
| 已获取的能力不再匹配当前锁或日志 | 以 `delivery/ownership-lost` 退出 1；停止一切共享路径改动。 |
| 匹配的所有者无法移除自己的锁 | 以 `delivery/lock-release` 退出 1；保全该锁。 |

`delivery/lock-stale` 诊断会给出输出与锁的绝对路径，
外加原始 PID 与回执 ID。恢复被有意设计为显式且串行：
停止针对该物理输出目录的一切交付尝试，
确认没有活跃交付持有它、确认被报告的过期条目未被替换，
然后只移除被报告的锁，再重跑 `deliver`。
不要在过期锁恢复过程中移除 artifact、当前溯源或 pending 日志。

该锁协议面向 Node.js 18 及以上、本地文件系统上相互配合的 Archify 进程。
PID、回执与文件身份比较都是防御性检查，不是原子的 compare-and-swap。
兼容围栏覆盖请求拼写与既有的物理目标拼写；
它们无法枚举任意硬链接名或此前未知的文件系统别名，
因此经由这些别名的混版本交付仍在范围之外。
本契约不声称在 NFS、SMB 或其他网络文件系统上具备分布式锁正确性，
也无法阻止一个无视协议的外部进程替换共享路径。

每个禁止覆盖的 HTML 发布器（`render`、`deliver`、`compare` 与 `preview`）都会在暂存（staging）前捕获
所请求的目录条目、规范写入槽位、物理父目录，以及既有目标的类型、device/inode 身份与 mode，
然后在替换前立即重新校验这份快照。既有的写入目标必须是恰好只有一个硬链接名的普通文件。
有多个硬链接名的目标以 `output/target-hardlinked` fail-closed 失败：
替换所请求的名字无法把未知兄弟名一并当作同一次发布更新。
硬链接在读身份与输入/别名碰撞检查上仍然受支持；
只是作为写入目标不受支持。指向单链接普通文件的符号链接仍然受支持：
发布保留该符号链接条目，并把同一协议应用到其解析目标。
目录、FIFO、socket、设备文件、mode 变化、新主张者（claimant）
与身份不确定等情况都会在替换前失败。

发布是禁止覆盖且可恢复的，不是对既有目标的崩溃原子替换。
为避免覆盖最后一次身份检查之后才出现的主张者，
Archify 先把绑定的旧文件保留在私有的恢复备份中，
通过绑定身份的隔离（quarantine）移除公开名，
再用独占硬链接创建新的公开名。
被捕获的失败在公开槽位与恢复绑定仍允许时执行回滚。
如果进程在这些命名空间操作之间被打断，公开路径可能反而缺失，
而验证过的旧字节仍留在相邻的私有恢复备份里。
单 artifact 发布会在私有的
`.archify-remove-*/publication-recovery-v1.json` 中、`previous` 旁边
记录原始槽位/别名身份以及备份的 inode、mode、SHA-256 与字节数。
要让某次被打断的发布重新可见，先停止并发写入者，然后运行：

```bash
node bin/recover-output.mjs /absolute/path/to/.archify-remove-<id> --json
```

这是显式恢复，不是目录扫描器。建立链接之前，辅助脚本会检查：
父目录或别名是否变化、记录或备份是否被改动/被硬链接、
摘要或 inode 是否不匹配，以及公开目标是否已存在。
它只通过禁止覆盖的硬链接恢复，因此新的主张者会被保留而非覆盖；
它绝不递归删除未知条目。已完成的恢复是幂等的。
这份记录是要被独立验证的证据，不是恢复任意私有字节的授权：
辅助脚本只接受来自原始物理目标父目录下被记录的那个生成子目录、
且目录身份相同的记录。
要指明被中断进程报告的确切目录，并人工检查不确定的记录。
一个不配合的进程仍可能在那些检查之后、Node.js `linkSync` 之前调换路径名；
Node 没有暴露绑定描述符的链接操作。
链接后的身份验证于是 fail-closed 并保留恢复证据，
而不是声称恢复成功或删除不确定的名字。
如果恢复本身在建立链接之后被打断，旧的公开字节与私有备份可能同时留存；
后续恢复运行会保留公开目标，需要操作者显式裁决。
在支持目录同步的平台上，记录会先 fsync，然后旧公开名才退役，
经过测试的保证是"进程被杀后的恢复"；
这不是对断电、存储控制器、NFS 或 SMB 持久性的声明。
成对流程把备份保留在私有事务暂存区中。
对 `deliver` 来说，pending 日志与锁让严格检查器保持 fail-closed。
可移植的 Node.js 文件系统 API 没有这样的路径名 compare-and-swap：
既原子地替换既有名字，又拒绝覆盖迟到的主张者；
`rename` 只有靠覆盖那个主张者才能消除可见性缺口。

所有权建立之后，`deliver` 在渲染前创建日志，
并在可恢复的 HTML/sidecar 成对提交期间一直持有它。
只有该提交完成后才移除日志。因此，校验、渲染或成对提交失败，
或进程被打断，都可能留下一个日志。
这道日志是安全屏障：只要 journal 或锁路径上存在任何目录条目，
`check`、`browser-check` 与 `visual-check` 就 fail-closed 失败，
包括不可读文件、符号链接或悬空符号链接。
针对同一物理输出目录的交付要串行运行；
一次尝试必须完成或被恢复后，另一次才能开始。

合法的 sidecar 应有 `schemaVersion: 1`、`status: "current"`、
`command: "deliver"`、唯一的 `receiptId`、图的 `type`、
绝对 `input` 路径、与受检 artifact 匹配的绝对 `output` 路径，
以及 specification/artifact 的 SHA-256 与字节数。
检查器把缺失、格式错误、不支持或前后不一致的字段判为无效。
它们也拒绝 sidecar 符号链接，包括悬空的。
检查器把溯源绑定到它实际检查的 artifact 字节，
并在报告成功前再次核验该绑定；并发字节变化即失败。
溯源目录条目本身必须是单链接普通文件：
当它还有另一个硬链接时，`deliver` 与严格检查
以 `delivery/provenance-hardlink-unsupported` fail-closed 失败，
且不会扫描或猜测兄弟名。

当一个当前已验证的所有者在旧 HTML 已存在之后失败，
Archify 会写入新的 `status: "failed"` sidecar，
并保留日志直到恢复完成。旧 HTML 不可读并不妨碍这个标记；
其 artifact 哈希与字节数可以缺失。
如果 sidecar 被锁住或因其他原因不可写，
Archify 保留先前的 sidecar 而不是删除证据，
日志则阻止检查器信任它。
被拒绝的并发、过期或无效锁尝试不会写入失败溯源。
如果所有权丢失，Archify 报告 `delivery/ownership-lost`，
不覆盖也不移除继任者的 artifact、溯源、日志或锁，
也不声称已记录失败溯源；失败回执可能报告 `provenance: "unrecorded"`。
如果所有元数据路径都不可用，同样适用未记录状态；
没有任何工具能跨进程保全这一事实。
先恢复元数据路径访问并完成一次成功的 `deliver`，再信任该输出。

没有 sidecar、日志或锁的 artifact 仍然受支持，
用于向后兼容以及更底层的 `render` 命令。
它们的检查器回执报告 `provenance: "unknown"`；
当工作流要求"成功交付过的 artifact"时，
用 `--require-provenance` 把该状态变成非零失败：

```bash
node bin/archify.mjs check <output.html> --require-provenance
node bin/archify.mjs browser-check <output.html> --json --require-provenance
```

## 输出路径契约

Archify 有意把持久化的创作路径与命令行路径分开：

- 必填的创作字段 `meta.output` 是可移植的 POSIX 相对路径，如 `reports/diagram.html`。
  它使用 `/`，以非空的 `.html` 基名结尾，且不得包含绝对或盘符相对前缀、
  URI、反斜杠、空段或点段、控制字符、不成对 UTF-16 代理对、
  Windows 备用数据流分隔符或非法文件名字符、结尾的点或空格、
  DOS 设备名，或超过 255 字节 UTF-8 或 255 码元 UTF-16 限制的组件。
  它从当前工作目录解析，且在跟随符号链接之后，
  必须仍物理位于该目录之内并以 `.html` 为目标。
  持久化输出/归档 profile 还保守地拒绝 Windows 8.3 短名形状，如 `PROGRA~1`；
  描述性的 repo/Git POSIX 路径使用另一套 profile，不受此限。
- 显式 CLI 输出参数使用当前宿主的原生语法。
  它们可以是相对或绝对路径，使用原生分隔符，
  并可解析到当前工作目录之外。
  在 Windows 上，支持普通的盘符绝对路径、UNC 与相对路径（包括普通的 `.` 与 `..` 导航）。
  当 Archify 能证明其物理身份时，接受系统解析出的既有文件或目录的 8.3 拼写；
  这种原生别名支持不放松持久化输出/归档 profile 对 8.3 形状名字的拒绝。
  扩展长度路径仅限于纯反斜杠的 `\\?\C:\...` 与 `\\?\UNC\server\share\...` 形式，且不得含点段；
  设备命名空间、畸形根、`C:file.html` 这类盘符相对路径、
  `\file.html` 这类当前盘根、备用数据流、保留设备名、
  非法或结尾文件名字符，以及超长组件都 fail-closed 失败。
  POSIX CLI 路径保留 POSIX 文件名规则，不继承 Windows 拼写限制。
  每个宿主都拒绝 NUL、不成对代理对，以及超出其支持上限的组件。

这两套契约不可互换：显式 CLI 输出掩盖不了无效的持久化 `meta.output`（包括缺失值），
而 `validate` 即使不发布到该路径也会检查创作输出。
Workflow v1 到 v2 的迁移可以通过
`migrate workflow old.json new.json --to-schema 2 --output reports/diagram.html`
显式接收一个可移植的持久化替换值；
该值只写入其单独的已验证 v2 目的地。
这一迁移候选例外不修复源，也不绕过任何非输出的 schema 或编译器错误。
其他一切修复，都是在 `meta.output` 中补一个可移植的 POSIX 相对 `.html` 路径；
除此之外不需要改 schema 版本。

在完整的首个候选上直接运行 `finalize`，并在每次修复编辑之后运行。
它内嵌的校验会在交付前检查候选；独立 `validate` 只用于聚焦诊断。
编辑之后，省略任何先前的 `--candidate-sha256`，它绑定的是上一个候选。
CLI HTML 输出路径必须以 `.html` 结尾，包括符号链接解析之后。
比较回执路径必须以 `.json` 结尾。类型不匹配会在写入前以
`output/cli-extension` 或 `output/cli-resolved-extension` 失败。
这些检查防止意外的文件类型覆盖；它们不沙箱显式 CLI 目录，
也不阻止替换既有的预期类型 artifact。

只在候选冻结之后，才使用最终已验证交付：

```bash
node bin/archify.mjs deliver <type> <candidate.json> <output.html> --quality showcase --json
```

`deliver` 只读取一次规格，把这些确切字节写入同目录下的私有候选快照，渲染该快照，运行完整的 artifact 检查器，只有全部 artifact 检查通过后才替换目标。JSON 回执包含 `specification` 与 `artifact` 二者的 SHA-256 与字节数。

对普通的代理交接路径，优先使用 finalizer：

```bash
node bin/archify.mjs finalize <type> <candidate.json> <output.html> --quality showcase --json
```

`finalize` 调用一次已验证的 `deliver`，复用其内嵌的 showcase 校验结果，
然后运行严格的 `check --require-provenance` 与 `browser-check --require-provenance`。
它在第一个失败或被跳过的阶段停下，并保全该阶段的完整回执。
它的 stdout 是一个紧凑 JSON 对象，含闸门状态、
有界的可行动诊断、artifact 身份与证据路径。
同一紧凑对象会被原子写入 `<output-stem>.finalize-summary.json`；
常规失败修复就用这个文件。当诊断被截断时，
`diagnosticSummary.omittedByCode` 按诊断代码统计未显示的条目数，
而不替换完整回执中的完整主体与修复证据。
完整阶段回执与计时仍可在 `<output-stem>.finalize.json` 中用于审计。带 `--out-dir` 时，两个文件都写在那里（除非显式 `--receipt` 覆盖了 finalize 回执路径；artifact HTML 仍留在请求的输出路径）；
`--receipt <path.json>` 覆盖完整回执路径，并派生出独立的 `<path>-summary.json`。
只在紧凑摘要被截断、且其显示的主体与证据无法定位出连贯的本地修复时，或在显式要求完整审计证据时，才去读完整回执。
紧凑回执报告 `visualReview: "not-requested"`；
自动化闸门不生成图片，也不要求感知型审查者。
紧凑的 `visualReviewRecommendation` 保留严格检查中正向的交叉与路由绕行指标，
让作者无需读完整回执就能套用下文的审查升级。
建议不改变机器退出码，也不声称审查发生过。
其 `affectedRoutes` 标出交叉对与绕行（各最多 8 个，带截断标志）；
完整严格检查的 `composition.routeReview` 保留所有受影响的关系。
用这些 ID 在捕获的默认视口中追踪路由。
绕行可能包含 `directCorridorBlockers`，指出对齐端点之间的节点。
这些是几何审查线索，不是新的校验失败，也不是推断出的主路径语义。
主路径被阻挡或多条路由纠缠时，遵循 [架构布局修复](architecture-layout-repair.md)，
先重排连通场景，再微调单条边或标签。
保全每个语义事实；无关位置只有在其周围构图已被认可时才保留。

对测得自动布局的 Architecture 且上方有大片未用区域时，
紧凑回执可能包含 `layoutReviewRecommendation`。
其 `composition.leadingSpace` 证据把节点、边界标题、路由与标签都计算在内。
检查这片空间是否有意为之；若无意，在保留语义与用户固定几何的前提下
重新摆放连通场景，然后再次 finalize。
这条建议不改变任何闸门或退出状态，也不需要截图。
固定画布或测量不确定时不会给出建议。

一份通过的 finalizer 回执就是全部四个闸门的充分证据。
仅仅点名这些闸门或要求每个闸门通过，不需要重放它们各自的独立命令。
只有当请求明确要求分别执行，或聚焦失败诊断需要时，
才重放单条命令。

各独立命令仍然权威且向后兼容。聚焦诊断、恢复或只需要一个闸门时，直接使用它们。
finalize 失败不放松任何闸门，也不会把被保全的旧 artifact 变成当前的成功交付。

`finalize` 只在交付与严格检查都通过之后才发现并启动私有 Chrome。
因此，输入、仓库证据、交付或 artifact 检查失败都不会启动浏览器。
它只在当前溯源验证通过后才加载 artifact。
浏览器闸门保留每一项视口、主题与稳定性检查；
浏览器在完成时或浏览器阶段失败时关闭。
其完整阶段回执记录 `execution: "in-process"` 以及用于重放的等价独立 `command`。
Chrome 启动不再与前面的阶段重叠，所以成功运行可能略慢一点。
这避免了在无效候选上做无谓启动；
它不修复宿主对 Chrome 启动的沙箱限制，也不放松浏览器闸门。

成对提交是可恢复的，不声称两条文件系统路径原子变化或断电后仍持久。
日志终结是这次提交的一部分：在校验或移除日志时捕获到的失败，
会在可能且所有权仍是最新的情况下回滚被替换的文件。
如果所有权丢失，旧尝试立即停止重命名、回滚、终结日志、
记录失败溯源或清理共享路径。
任何私有暂存或可恢复备份都仍然可用，并由失败诊断标识。
如果恢复因其他原因失败，失败回执同样会指出留存的备份以供恢复。
进程被打断可能留下日志、备份或私有暂存；此时检查器 fail-closed。
在同一输出上串行重跑 `deliver` 之前，先遵循被报告的恢复证据。
失败的尝试以非零退出，绝不调用打开器；它绝不授权收集视觉证据。

如果独占创建成功但锁初始化失败，只有当其能力仍指向那个确切条目时，
Archify 才可记录失败溯源并移除不完整的锁。替代者会被保全。
文件系统与清理错误与活跃并发交付分开报告。
活跃、过期、无法识别或以其他方式保全的锁，
都会独立地阻止检查器接受既有 artifact。
先修复被报告的文件系统错误再重试；
如果锁路径上含有无关数据，改用另一个物理输出目录。

锁释放是交付完成的一部分。如果 artifact/溯源对已提交、日志已终结，
但匹配的锁无法移除，`deliver` 以 `delivery/lock-release` 退出 1，
保全该锁，不打印成功回执，也不调用打开器。
被保全的锁让严格检查器保持 fail-closed。
只有成对提交、日志终结与锁释放全部成功之后，
`deliver` 才可以零退出、打印成功回执或运行 `--open`。

在 `deliver` 零退出之后再运行严格的 `check`。
`browser-check` 或可选的 `visual-check` 只在该严格检查零退出之后运行。
失败标记、恢复日志或交付锁会让每个检查器在接受被保全的 HTML 之前就失败；
先报告诊断并完成一次成功的恢复交付，
再收集新的浏览器证据。

静态 `check` 对受检关系线与结构边界使用同一套 SVG 路径分析。
它支持 `M/L/H/V/Q/Z` 及其小写相对形式、重复参数与有限数值。
每个 `M` 开始一个独立子路径；`Z` 只闭合当前子路径。
分离的子路径绝不会创造出图中不存在的连接线段。
被非共线 `Q` 隔开的直线段在路由分析中也保持分离；
曲线采样点不会变成直线路由预算或节奏检查中的微线段。
线段长度与拉伸按连续片段测量，而实际转弯按关系汇总。
超出预算的关系只计一次，且内部片段边界不享有
留给语义端点的短共享干线例外。

这不是对完整 SVG 命令集的支持承诺：`A/C/S/T` 产生
`artifact/svg-path-unsupported`；缺失参数、非法数值及其他
语法错误产生 `artifact/svg-path-malformed`。检查器以非零退出，
而不是跳过坏路径或无限等待。
路径失败会追加一个 `svg_path_data` 检查；
普通有效 artifact 保留既有的九项检查。
诊断携带受检的 `pathIndex`、`role`、可用的关系/边界 `id`，
以及解析位置 `tokenOffset`、可用的 `command` 与 `reason`，
以便定位并修复生成源。
`pathIndex` 从 1 开始；`tokenOffset` 是数字字符引用解码后的
`d` 字符串中从 0 开始的 UTF-16 偏移。
注释、CDATA 与属性文本中的疑似标签会被忽略。
静态路径检查通过并不等于浏览器或感知视觉验收通过。

<details>
<summary>中文说明</summary>

静态 `check` 对受检关系线和结构边界的 SVG 路径使用同一解析结果，支持
`M/L/H/V/Q/Z` 及其小写相对形式、重复参数和有限数值。每个 `M` 开始独立
子路径，`Z` 只闭合当前子路径；子路径之间不会被拼接成图中不存在的线段。
非共线 `Q` 前后的直线也保持分离，不会把曲线采样点计为直线路由预算或
节奏检查中的微线段。线段长度和伸长率按连续片段测量，真实转弯数汇总到原关系；超预算关系
只计一次，内部子路径断点不享有语义起终点的短共享线例外。
这不是完整 SVG 命令集的支持承诺：`A/C/S/T` 返回
`artifact/svg-path-unsupported`；缺少参数、非法数值等格式错误返回
`artifact/svg-path-malformed`，检查以非零状态结束，不跳过坏路径或无限等待。
路径失败时追加 `svg_path_data` 检查；普通有效产物仍保留原来的 9 项检查。
诊断携带受检路径的 `pathIndex`、`role`、可用的关系/边界 `id`，以及解析位置
`tokenOffset`、可用的 `command` 和 `reason`，用于定位并修复生成路径的来源。
`pathIndex` 从 1 开始；`tokenOffset` 是数字字符引用解码后的 `d` 字符串中
从 0 开始的 UTF-16 位置。注释、CDATA 和属性文本中的伪标签不参与检查。
静态路径检查通过仍不代表浏览器或感知视觉验收通过。

</details>

交付接口暴露四个互相独立的声明：

1. `deliver` 证明确定性的 artifact 检查与字节同一性。
2. `browser-check` 从确切的 artifact 收集必需的自动化浏览器证据，不采集图片。
3. `visual-check` 可选地追加绑定 artifact 的截图与联络表（contact sheet）。
4. 感知型视觉审查记录人类或具备图像能力的审查者的判断。

通过其中一个声明绝不暗示其他。绝不要声称确定性回执包含浏览器或感知审查证据。

## 恢复失败的比较

`compare` 把 HTML artifact 与其 JSON 回执作为一对提交。
如果提交失败，它会尝试恢复之前的文件。
完整回滚会照常移除临时目录。

如果先前的文件无法恢复，compare 以
`delta/commit-rollback-failed` 非零退出并保留恢复目录。在 JSON
失败回执中，`diagnostics[].evidence.recoveryDirectory` 指明该目录，
`recoveryFiles` 列出恢复失败的文件对应的 `{ backup, target }` 路径。
人类可读的诊断也会打印恢复路径。

先解决文件系统错误，检查当前目标，
并把每个列出的备份恢复到对应目标，然后再重试。
两个先前文件都恢复并验证完成之前，保留恢复目录；
它里面还可能有被拒绝的候选文件，不要误当成备份。
成功的比较与提交前的失败照常清理。

## 自动化浏览器证据

`finalize` 针对确切的受信 HTML 运行必需的浏览器闸门，
不重渲染也不修改它。聚焦诊断时，等价的独立命令是：

```bash
node bin/archify.mjs browser-check <output.html> --json --require-provenance
```

这条零依赖命令经由 DevTools 管道使用 Chrome/Chromium（或 Microsoft Edge）。
`ARCHIFY_CHROME` 一旦设置就是权威的，即使是无效路径：
Archify 不会静默回退到别的浏览器。
Windows 的自动发现先检查所有 Chrome/Chromium 安装位置与 PATH 命令，
然后检查 `%ProgramFiles(x86)%`、`%ProgramFiles%` 与 `%LocalAppData%` 下的 Edge，
再是 PATH 上的 `msedge`。
在 macOS 与 Linux 上，发现同样先查 Chrome/Chromium，
然后是 Edge 应用包（macOS）与 PATH 上的
`microsoft-edge`/`microsoft-edge-stable`。
它在 1440×900、1600×1000、1920×1080 与 2048×1320
测量浅色主题的收纳性，并验证请求的浅色主题在全部四个视口、
深色主题在两个端点视口，以及 READ/Still 运行时状态。
请求的主题若解析成另一个主题，将带着实测证据失败。
它创建一份 `<output-stem>.browser-check.json` 回执，
不产生截图或联络表。
传 `--out-dir <dir>` 可把回执放进单独的证据目录。
该回执绑定 artifact 的 SHA-256 与字节数，
标明 `evidenceKind: "automated-browser"`，并报告
`visualReview: "not-requested"`。

横向溢出一律失败。正常的文档级纵向滚动
只有在渲染器声明了契约且实测文本可读时才被接受。
自动画布声明 `data-reader-fit="intrinsic-height"`（按高度适配）
或 `data-reader-fit="width-first"`（Sequence 与 Waterfall 的阅读宽度）；
它们的自适应 Reader 必须达到可读宽度并暴露
`data-reader-overflow="authored"`。
带显式 `meta.viewBox` 的 Architecture 改为声明
`data-diagram-type="architecture"` 与 `data-reader-fit="authored-height"`：
其 SVG 坐标、纵横比与既有 Reader 宽度行为保持不变。
其完整 SVG 必须留在图表面板内，无内部滚动或裁剪，
且文档必须允许纵向滚动。
回执记录 `verticalScrollAccepted: true` 与
`overflowDisposition: "readable-vertical-scroll"`。
缺失或未知的声明、其他模式下的显式 viewBox、不可读文本、横向溢出、
裁剪与 Viewer 部件碰撞仍是失败。
不要添加内部图滚动器，也不要隐藏溢出。

`browser_evidence` 在交接中
只记录这条自动化命令的结果：

- `passed` 来自退出 0 且回执 `status: "pass"`，
  前提是每项必需测量都完成并通过。
- `failed` 来自退出 1 且回执 `status: "fail"`，
  当检查发现缺陷、命令失败，或运行时错误导致证据不完整。
- `skipped` 只来自退出 2 且回执 `status: "skipped"`，
  当没有受支持的浏览器可用、检查未运行。

运行时失败留下的证据不完整，不得被归一成
`skipped`。它们不会使已经成功的确定性交付失效。
环境类失败在可行时于具备浏览器能力的执行上下文中重试。
只要失败没有在有能力环境中经该接缝复现，
就保持打包的传输方式不变。

在 Windows 上，Chrome/Edge 启动重启可能在任何响应到达之前丢失继承的 DevTools 管道。
Archify 只从浏览器子进程环境中移除独立的
`__COMPAT_LAYER=DetectorsAppHealth`
（名称与值都不区分大小写）；父环境、未知层、组合层
以及与权限相关的兼容性设置不变。
这针对的是被报告的非提权 Git Bash 应用健康检查案例，不是每个
AppCompat 模式。提权 shell 的重启仍不受支持：从正常打开的
非提权 PowerShell 重跑，处于提权或兼容模式父进程之外。
Archify 不抑制浏览器降权，也不禁用沙箱
作为重启变通。零响应的启动诊断会建议这一补救，
而不声称提权或 AppCompat 是每起管道失败的原因。

溯源失败会在浏览器检查之前退出，并持久化一份
绑定到所尝试 artifact 的失败 browser-check 回执。如果失败回执
无法写入，诊断会点名那份不完整证据。

两个浏览器命令都检查确切交付的 HTML，不修改也不重渲染。

## Sequence 宽度审查

通过的 `finalize` 可能报告
`layoutReviewRecommendation.action: "inspect-sequence-width"`。
其 `evidence` 在计入消息标签、备注与段标题之后，
测量固定参与者列右侧的未用空间。
这条建议不新增警告、失败、截图要求或自动几何变更。

通过的 `validate --json`、`deliver` 或 `finalize` 回执可能带有
针对 Viewer locale 回退（`i18n/*`）的 `severity: "warning"` 的
`diagnostics[]` 条目。它们不让任何闸门失败。
当 artifact 应当完全本地化时，
按其 `evidence` 修复列出的键并重跑 `finalize`。

省略 `meta.column_fit` 的 Sequence 画布使用 `spread`，
无论是否提供 `meta.viewBox`。创作设定的 viewBox 仍是权威；
参与者容量不可行时直接失败，不会静默放大它。
显式 `meta.column_fit: "fixed"` 保留历史上的固定列。
对固定列宽度建议仍然存在的候选，先检查固定几何是否有意为之。
只有当该几何的变更是被授权的，才保存候选，
只把 `meta.column_fit` 设为 `"spread"`，
并用 `--out-dir <folder>/width-review` 完整重跑一次 `finalize`。
保留参与者顺序、消息及其 y 位置、标签、备注、来源与画布尺寸。
如果该尝试失败，恢复候选并用 `--out-dir <folder>/width-restore` finalize 它；
报告剩余的布局建议，而不是反复迭代。
保留有意的固定几何；变更未被授权时，披露该建议。
要为较旧的省略 fit 输入保留历史固定坐标，
显式设置 `meta.column_fit: "fixed"`。
这项审查只关乎水平构图；通过的回执仍不声称获得感知认可。

## 可选采集证据

`visual-check` 对请求的或升级触发的感知审查保持向后兼容：

```bash
node bin/archify.mjs visual-check <output.html> --summary --require-provenance
```

`--summary` 返回紧凑 JSON，含全部诊断以及指向完整回执、联络表与每张截图的绝对路径。选定视觉审查时，检查相关捕获；捕获成功不是感知认可。`--json` 为既有消费者保留完整回执输出。两种模式运行同样的检查并保持同样的退出状态。如果发布后清理失败，摘要保留最终失败诊断与 `publication` 恢复细节；链接的回执记录更早的已提交证据。

它执行同样的自动化浏览器测量，
在 1440×900 与 2048×1320 采集浅色/深色截图，
并写出四份视口 PNG sidecar、一份相对路径的
HTML 联络表与一份 JSON 回执。`--out-dir <dir>` 把这些 sidecar 一起搬走。
用浏览器打开 HTML 联络表，或用图像阅读器检查视口 PNG。
其回执报告 `visualReview: "pending"`，因为采集本身
不构成感知判断。采集与溯源失败遵循下文的所有权规则。

回执、联络表与四张 PNG 构成一个有主证据集。
采集之前，`visual-check` 冻结每个被请求的目录条目、
其规范写入槽位与物理父目录，
以及目标的缺席/文件状态、类型、device/inode 身份与 mode。
硬链接的证据目标不是安全的写入目标。
所有候选文件都在物理证据目录之下一个随机的、
私有暂存目录中独占地创建；回执最后发布。
每个暂存候选在发布前必须恰好有一个硬链接名。
禁止覆盖的发布链接会暂时让暂存名与最终名的链接计数为 2；
解除已验证暂存名的链接之后，最终条目的链接计数必须为 1。
意外的外部硬链接 fail-closed 失败，其别名永不移除。

Chrome 在私有本地临时目录中检查捕获 artifact 的一个
经身份与内容核验的副本，
因此浏览器文件加载不依赖 UNC 或长路径支持。
六个发布候选留在证据卷上。
两个临时目录的清理都不递归删除未知内容；
被保留的条目附有其恢复位置。

在任何提交之前的一刻，`visual-check` 重新解析并核验
完整的六路径集合。
缺席路径的主张者、既有路径的替换、
符号链接或悬空链接的重定向、父目录拓扑变化、
硬链接或身份不确定，都会以
`viewer/evidence-path-conflict` fail-closed 失败。
主张者与其他所有最终证据路径保持原样。
清理只移除本次运行的暂存或已发布条目，
且在复核其捕获身份之后；变化或未知的条目被保留。

既有的视觉证据集只有在以下条件下才可替换：
一份常规 `visual-check` 回执证明了对同一 artifact 与证据目录的所有权，
且其确切的 sidecar 清单与每个既有联络表或 PNG 的
字节数与 SHA-256 摘要都匹配。
缺失、格式错误、未知、不匹配或不完整的所有权记录
绝不授权删除。失败与跳过的运行
只在所有权证明成功时、作为同一已验证事务的一部分
退役先前的截图/联络表；
否则它们保全所有未知证据并报告
`viewer/evidence-path-conflict`。

这条规则同样适用于 Chrome 不可用或溯源在浏览器检查之前失败的情况：
两条路径都不得盲目删除看似过期的证据。
已验证的有主证据集可以在发布跳过或失败回执之前
以可恢复方式退役；无主证据保持完好。
这些结果不会使已经成功的确定性交付失效，
也不会把感知型视觉审查变成 passed 或 failed。
环境类失败在可行时通过受支持的命令
在具备浏览器能力的执行上下文中重试。
只要失败没有在有能力环境中经该接缝复现，
就保持打包的传输方式不变。

`browser-check` 对其唯一的 JSON 回执应用同样的
私有快照、身份、所有权与禁止覆盖规则。
它的命名空间与 `visual-check` 分离，
因此仅浏览器的重跑无法移除采集证据。

## 既有输出路径上的新候选

浏览器证据属于确切的 artifact 字节。编辑一个其先前 HTML 已有浏览器证据的候选之后，在下一次 `finalize` 之前选一个全新的证据目录；这样既保全旧回执与捕获，又省去一次可避免的所有权冲突重试。`--out-dir` 搬迁新的 browser-check 回执，默认还搬迁 finalize 回执与摘要。显式 `--receipt` 覆盖 finalize 回执路径；其摘要跟随该路径。成功交付仍会重写请求的 HTML 及其同目录的 `*.delivery.json`。更早的浏览器或视觉证据仍绑定其原始 artifact 字节，不得当作已变更 HTML 的证据：

```bash
node bin/archify.mjs finalize architecture candidate.json diagram.html --quality showcase --repo-root <root> --out-dir diagram.review-2 --json
node bin/archify.mjs visual-check diagram.html --out-dir diagram.review-2 --summary --require-provenance
```

证据目录不是 HTML 的存档。只把 HTML 拷贝过去并不会重新绑定回执路径或溯源。需要历史快照时，在覆盖之前分别保全候选与 artifact；不要假设拷贝来的回执能验证被搬迁的 artifact。

保持请求的 HTML 路径稳定。每个变更过的候选用一个新的修订目录，字节未变的重试用同一目录。没有仓库证据的图省略 `--repo-root`。让命令自己创建输出目录。先前一次未产出 HTML 或浏览器证据的校验失败不需要新目录。绝不为了重试通过而移除未知证据。

## 可选打开

只在用户想要立即本地预览时加 `--open`。
它在已验证成对提交完成、其恢复日志已移除、
且交付锁已成功释放之后运行。
它使用一次参数数组式 OS 打开器，
macOS 与 Linux 上限时五秒，
Windows 上 PowerShell 启动限时十五秒。
回执记录 `open.status`；失败或不可用的启动尝试
还会包含归一化的 `open.failure` 细节。
CI、无人值守代理与非交互环境中保持关闭。
打开失败或不受支持不使交付失效；
其状态只证明本地打开器调用是否成功。

## Last-Good 实时预览

仅用于活跃的桌面创作循环：

```bash
node bin/archify.mjs preview <type> <input>.json <output>.html --quality showcase
```

Preview 在回环地址上监视一个显式输入，把每个稳定摘要绑定到私有快照，且只在既有已验证交付管线通过之后才前进。无效、写了一半、已删除或被取代的输入会让屏幕上和磁盘上都保持先前已验证的修订。相同字节不重建也不重载。

预览运行时随零依赖 Skill ZIP 一起分发，必须在没有 `node_modules` 时也能工作。

绝不默认启动它。不要把它用于 CI、无人值守代理、远程共享或移动端使用。`--no-open` 只给将自行打开打印出的本地 URL 的用户，或用于循环测试。交接前用 Ctrl-C 停止它。第一次 Ctrl-C 排空活跃交付但不发布；第二次 Ctrl-C 强制关闭交付进程与 HTTP 连接，包括未完成的请求。关闭时保全最后一个已验证 artifact，只移除所有权可验证的暂存文件。如果交付在其回执到达 Preview 之前被打断，未确认文件与恢复材料可能留在私有暂存目录；关闭不会递归删除未知内容。服务器状态、端口、源路径、诊断、错误文本与重载令牌绝不能进入生成的 artifact 或任何导出。

## 感知审查

自动化路径以确定性浏览器闸门收尾，并报告
`visual_review: not_requested`。普通生成不需要截图
或读图步骤，包括新创作或重新摆放的 Architecture。
感知审查是可选的；用于显式请求或具体的视觉排查。
可能的理由包括：

- 紧凑 finalizer 包含针对交叉或绕行的
  `visualReviewRecommendation`（建议性质，不是交付闸门）；
- 用户显式请求美学或视觉审查；
- 模板、渲染器或 Viewer 的变更需要视觉回归证据；
- 新颖布局或浏览器诊断留下的置信度低；
- 该运行被抽中做抽检或 dogfood。

对默认的独立桌面查看器，测量 1440×900、1600×1000、1920×1080 与 2048×1320。在每个受检尺寸都要求 `document.documentElement.scrollWidth <= window.innerWidth`。优先 `scrollHeight <= window.innerHeight`；页面级纵向滚动只接受上文定义的 Reader 声明的可读例外。在最大的受检视口，检查渲染构图是否有显眼的下方空带：主面板与必要的结论卡应把可用高度当作平衡的整体来用，而不是塌缩成浅浅一条。出现意外溢出时，先只移除真正冗余的内容或压缩间距来修复创作构图，然后才考虑缩小节点、标签或主面板。不要隐藏溢出、裁剪内容、引入内部图滚动器，或缩小节点/标签字体来让测量通过。窄屏/移动端的收纳可以保留页面纵向滚动。

升级审查时，对当前已 finalize 的 artifact 运行 `visual-check`，
用具备图像能力的阅读器或人检查其联络表，
并核对两个端点主题、默认 READ 视图、
线交叉/走廊、标签遮挡、节点/卡片契合、
焦点/搜索/passport 闭合与导出洁净度。
这项审查是补充性的，绝不改变 `browser_evidence`。
无约束的浏览器一瞥只能支持感知审查。

在诊断性或结构化交接中，报告一个如实的可选审查状态：

- `visual_review: not_requested`：没有审查触发条件成立；这不是视觉验收声明。
- `visual_review: passed`：只在检查过渲染出的 artifact 之后。
- `visual_review: skipped (image reader unavailable)`：请求的或触发的审查未能运行。
- `visual_review: failed`：附上具体的可见缺陷。

升级审查用 `correction_rounds: 0`、`correction_rounds: 1` 或
`correction_rounds: 2`；聚焦修正轮绝不超过两轮。
未请求审查时用 `correction_rounds: 0`。
绝不报告 `visual_review: passed` 而没有检查过 artifact。
如果感知审查改变了候选，重跑 `finalize`，
因为先前的规格与 artifact 回执已不再有效。

## 交接回执

被请求的诊断性或结构化交接，从既有回执推导以下细节。
普通面向用户的回复遵循 [输出](../SKILL.md#output)；
这份清单不是默认聊天回复。

```text
diagram_type: <actual diagram type>
output: /absolute/path/to/file.html
specification_sha256: <receipt value>
artifact_sha256: <receipt value>
validation: <actual quality profile, check counts, errors, and warnings>
browser_evidence: passed|failed|skipped
visual_review: not_requested|passed|skipped (image reader unavailable)|failed
correction_rounds: 0|1|2
```

`browser_evidence` 只从最新的绑定 artifact 的
`browser-check` 回执推导，通常就是 `finalize` 内嵌的阶段。
可选采集或人工浏览器工作要单独记录，
带上其 artifact 绑定、视口/主题范围与观察；
绝不把它或 `visual_review` 用于覆盖自动化状态。

打开、预览状态、Share Cards 与其他 viewer 导出不是校验声明。

finalize 回执的发布使用上文所述的
同一身份绑定、禁止覆盖发布器与显式恢复记录。
完整回执与摘要回执必须区别于候选、artifact、
交付元数据与浏览器回执。
它们的目标必须缺席，或是单链接普通文件；
符号链接回执条目与被硬链接的目标 fail-closed 失败。
后到的主张者或变化的父目录会让发布停止并保持原样。
默认回执名共享物理 artifact 命名空间，
并按宿主文件名上限截断。
两份回执各自独立发布，不是崩溃原子成对；
只有完整跑完且通过的命令才算成功交接。
