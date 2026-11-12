> **中文汉化版** · 上游：[tt-a1i/archify](https://github.com/tt-a1i/archify) · 原文件：`archify/references/authoring-defaults.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 绘制默认值（Authoring defaults）

写全新候选文件之前通读一次。已冻结、直接进入 `finalize` 的既有候选文件，只在修复改动其绘制内容时才需要本文件。

## 构成与语义（Composition and meaning）

对 Architecture，默认画一张以主用户旅程为主导的系统总览，除非用户要求更窄的机制、模块图或部署拓扑。当按角色分组仍能解释所请求的交互时，把协作角色归入命名准确的子系统。当分组会掩盖控制权归属、信任或持久化边界、生命周期行为或读者问及的其他区分时，拆开角色。次要能力与可选能力放在简短的、有来源的注释里，除非其路径对所提问题重要。标题中写明有意收窄的范围。

保留每一条被要求的责任、关系方向、协议和改变行为的条件。审批、授权和状态迁移闸门画在受影响的节点或关系上；仅凭一张卡片不能让本来无条件的箭头变成有条件的。每条断言的源证据随断言一起保留。边界表达真实的隔离、归属、运行时或持久化事实。卡片回答读者追加的问题；它们不能替代必需的拓扑。节点、边、来源、卡片或边界都没有数量配额。已绘制的总览在失败后需要重新分组时，使用 [构成修复](authoring-contract.md#composition-repair)；用户提供或商定的拓扑保持不动。

关系标签承载语义。给它们留出清晰空间，保留动作、协议、方向、异步行为或跨边界含义。当模式 schema 允许省略标签时，只有在两个端点已完全隐含该含义时才省略；碰撞要靠间距或布线修复解决。量测证据报告碰撞时，参见 [标签修复](authoring-contract.md#label-repair)。

## 布局与布线（Layout and routing）

先按实际连接摆好 Architecture 节点，再定坐标；路由器不会重排方框，摆位决定线条能否笔直。先给每条关系分类，再摆位：

- **主路径**：读者的主旅程，相邻节点按阅读顺序紧挨。中等长度的路径让它分几行逐级推进，不要压成一条浅浅的横带。
- **分支或存储**：直接放在拥有、读取或写入它的节点上方或下方，并对准该节点，让边成为一段直线。同一行的全部存储与分支放在该行的同一侧。
- **返回**（回到主路径上更早的节点）：把其源头放在主路径没有分支或存储的一侧，让它穿过空走廊而不是横穿它们。
- **二次进入**（进入已有入边的节点）：把新源头摆在能从另一侧到达该节点的位置，通常在其正下方或正上方。
- **扇出**：一侧有 k 条关系时至少需要 `32 + 14 × (k − 1)`px（四条需 74px）。把枢纽的对手方分散到两三个侧边，或加大枢纽。父节点在其子节点上居中，子节点与其唯一父节点对齐。

写坐标之前，逐条走查非主关系：它的直连或单弯走廊不得穿过其他节点，也不得与其他关系交叉。若违反，移动偏离主路径的那个端点。主参与者与其第一个相连步骤一起放在画布原点附近（约 `[40, 40]`，不是 `[200, 200]`）；用内容行制造纵向节奏。高起点留下的上方/左侧空白浪费画布，还会掉填充率，却不提升可读性。全新 Architecture 省略 `meta.viewBox`，让 Reader 量出固有高度。用户提供的固定几何保持权威。

从自动布线和自动端点侧开始。只在必要的分支、返回或用户提供的几何上钉定侧向。全新 Architecture 在没有必需侧向约束、且不妨碍平行直线时，让相邻的请求/回复方向保持自动；保留用户提供的侧向钉定。`via`、`channelX`、`channelY` 和标签坐标留给量测出的缺陷。写坐标之前，给每条位于并排方框之间的带标签边做预算（无论是否在主路径上）：净间隙按 `6.5px × ASCII 单位 + 21px` 计算，CJK 按两个单位计；用该标签自身的长度，而不是全行统一间隙。边界框是包住其全部成员的内边距盒：把成员摆成一个紧凑的轴对齐簇（不留能让非成员坐进内边距框里的空位），并把每个非成员（尤其是外部参与者）留在盒外。Architecture 画布宽度控制在 1240px 内，或当它至少是高的 1.55 倍时放宽到 1790px；超过后其 8px 关系标签会跌破桌面底线。Architecture 子标签按其偏好的 9px 字号取 `5.4px × 文本单位 + 8px`，CJK 按两个单位计；辅助文案保持简短，不丢必需事实。不要为减少交叉牺牲可读性或语义。已确诊的布局问题，其量测间距、端口、画布和布线规则见 [几何参考](authoring-contract.md#executable-geometry-rules)。

## 证据与 schema（Evidence and schema）

对真实仓库，在检查源码时遵循 [基于仓库的绘制](repository-authoring.md)。把无凭证的 origin 和 40 位 commit 冻结进 `meta.repository`，给每个关键语义节点附上检查过的仓库相对 `sources`，并在第一次 `finalize` 传入 `--repo-root`。每条引用只证明该位置可见的那个事实。沿实质关系和条件追到真实源码；不要把启动处的引用当作协议或持久化证据。

示例展示字段形状，不展示合法取值或来源事实。它们是完成态的展示品，其可选呈现字段（`meta.subtitle`、`meta.viewBox`、`meta.column_fit`、`via`、`labelAt`）不是默认值；这里的默认值优先。添加字段、枚举或受限文本前，先读模式 schema 和共享定义。尤其要检查 Architecture 边界种类。较长的证据放卡片，同时保留事实本身。细节见 [Schema 查阅](authoring-contract.md#schema-lookup)。

## 呈现与模式（Presentation and modes）

动效自动启用。省略 `meta.animation`；用 Viewer 的 Live/Still 按钮暂停或恢复播放。

主要绘制语言从用户的选择或请求/会话中取一种。设置 `meta.locale`；`en`、`zh-CN`、`zh-TW`、`es`、`ko` 和 `ar` 直接选用内置 Viewer 语言目录，无需其他操作。其他语言需提供带可复用 UI 译文的 `meta.translations`，或声明固定的 Viewer UI 与 `<html lang>` 保留英文回退。本地化周边说明时保留精确的产品、代码、协议、命令、API 和环境名称。双语场景见 [语言一致性](authoring-contract.md#language-consistency)。

经典样式省略 `meta.visual_preset`，只有标题的页头省略 `meta.subtitle`，真实自动图例省略 `meta.legend`，普通系统总览省略 `meta.engineering_profile`。显式样式和副标题需要用户明确提出。图例或部署归属分别按 [图例契约](authoring-contract.md#legend-contract) 或 [工程档案默认](authoring-contract.md#engineering-profile-default) 使用。品牌标识可选且必须显式：节点提到真实产品时才用；该分支的查找与抓取规则见 [品牌标识](brand-marks.md)。绝不让徽章替代语义类型、标签或关系事实。必填的 `meta.output` 设为工作目录内的可移植 POSIX 相对 `.html` 路径；原生路径例外见 [输出路径契约](delivery-contract.md#output-path-contracts)。

全新 Workflow 用 schema v2 并省略 `meta.viewBox`，让编译器量出真实占地；不要为凑视口比例加空白画布。保留用户提供的固定几何和 v1 来源。未钉定的草稿中省略节点 `width`：节点从 92px 起步，随标签、子标签和标签牌增长到最多 200px。显式画布与绝对布线/标签钉定仍沿用旧几何契约。泳道或群组几何需要细节时，用其 [布局契约](../renderers/workflow/README.md#layout-contracts)。

全新 Sequence 省略 `meta.viewBox` 和 `meta.column_fit`：自动高度贴合时间线（无 760px 下限），2–3 个短标签参与者在标签放得下时收缩到 920px 以下，画布仍会为拥挤标签加宽到可读宽度；保留已绘制的 `meta.viewBox`。需要历史固定坐标时显式设 `meta.column_fit: "fixed"`；宽 viewBox 留出未用水平空间或重要标签需要宽度时用 `spread`。参与者的内部动作用其周围真实跨参与者消息上的注释描述，保留含义与顺序；Sequence 不支持自消息环。全新摆位时，在放下一条消息前先为该注释预算纵向空间：28px 是无注释消息的基本间距，不是注释预算。注释延伸到其消息下方；共享该空间的下一条消息之前，一行至少留 44px，两行 55px，三行 66px（例如 y=200 处的三行注释，下一条消息要到 y=266 或更晚）。换行取决于最终泳道宽度，所以较长的注释留更多空间，并保留每条注释的含义而不是删掉。这些间隙不保证与段标题、其他注释或激活条留出净空。用户提供的固定 y 值仍具权威；代理绘制的新草稿中，按需一并调整后续消息、段边界和激活边界，保持顺序与含义，并在这些约束内用 `sequence/note-overlap` 证据做修复。

全新 Dataflow 从 2 到 5 个阶段、0 到 4 行的阶段/行网格开始，并遵循规范的 [Dataflow 画布与展示默认值](authoring-contract.md#dataflow)。相邻阶段中心相距 215px，默认节点宽 112px，节点间约留 100px，因此流标签控制在约 17 个文本单位内（CJK 按两个单位计），更多细节移入卡片；用户提供的几何或量测约束可加尺寸或布线控制。

Dataflow 溯源（lineage）从每个被要求的输出倒推到其生产者实际消费的值。把原始载荷与派生配置合起来的转换，各自拿到单独的带标签输入；每个上游节点只转发它实际输出的值。有证据的存储端点用 `database`，写明文件或存储名。计算出的内存结果通过其生产 `backend` 操作表达，并在其标签或子标签中写明结果字段。

Dataflow 要求每条流都有非空 `label`。按默认图例告诉读者的含义选 `variant`：省略/`default` 是普通数据流，`emphasis` 是主数据，`security` 是策略/PII，`dashed` 是异步批处理。普通依赖、返回或回退用 `default`；只有来源支持该含义时才用 `security` 或 `dashed`。用户要求别的视觉约定时，按 [图例契约](authoring-contract.md#legend-contract) 给受影响的 `meta.legend.entries.<variant>.label` 写出如实描述所有使用该 variant 之流的措辞。

Lifecycle 用 schema v3：在 `mainPath` 里列出主流程（happy path），并绘制每一条迁移（包括主路径上的）；渲染器摆放其余状态和路线。保留每个出口的标签、注释和 variant；[合格等价出口](../renderers/lifecycle/README.md#layout)自动共享布线。迁移标签要短；可恢复的失败需要一条真实的返回迁移。

Class 省略 `meta.viewBox`，网格保持三列；只有类型都接近 180px 默认宽度时才用四列：长成员会把类型撑向 `layout.typeMaxW`（300px），每加一列画布就更宽、所有文字就更接近可读底线，所以要加行而不是加列。`layout.gapX` 和 `layout.typeMaxW` 是宽度控制项。

仓库或目录 Tree 设 `layout.direction: "right"`；浅而均衡的拆分保留默认 `"down"`。特定模式的摆位或视口问题需要更多细节时，读 [模式摆位](authoring-contract.md#mode-placement)。

`finalize` 执行浏览器门禁。完整图形在桌面上保持舒适可读，水平溢出为零。必要时用有意义的纵向行和固有高度页面滚动。6px 投影文字检查是失败底线；在 1440px 下，普通上下文文字争取 7.5px 或更大。视口证据失败时见 [自动化浏览器证据](delivery-contract.md#automated-browser-evidence)。
