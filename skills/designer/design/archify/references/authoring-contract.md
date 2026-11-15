> **中文汉化版** · 上游：[tt-a1i/archify](https://github.com/tt-a1i/archify) · 原文件：`archify/references/authoring-contract.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 创作契约（Authoring contract）

只在快速创作路径需要更多细节时才读本参考。schema 与示例仍是权威依据。

## 构成修复

修正已创作总览图的抽象层次时，先在重新分组之前，把每一条受影响的角色、关系方向、协议、边界、条件与来
源引用映射到其存留的节点或关系上。引用一家初创公司并不能证明存在一条消息协议。保留每条论断已被查验的
证据。用户给定或已商定的拓扑保持不动；仅"路由变少"不足以支撑合并。围绕单个节点画边界需要一条明确的隔
离事实，不得只是复述其标签。

## 标签修复

关系标签发生碰撞时，先移动标签、调整路由或间距，再在保留语义的前提下缩短措辞。只有当两端点已完全隐含
该含义、且它不传达协议、动作、方向、同步或异步行为或跨边界机制时，才可省略措辞。间距指清晰间隙而非中
心距；以实测遮罩宽度为准。第一稿的间隙预算见 [布局与布线](authoring-defaults.md#layout-and-routing)
。

对过大的子标签，保持其确切角色或协议简短，把补充事实放进备注或卡片。保留每一条必需的职责、协议与边界
事实。第一稿的节点宽度预算见 [布局与布线](authoring-defaults.md#layout-and-routing)。

## Schema 查阅

模式 schema 与 `schemas/common.schema.json` 都要读。各模式 schema 使用 `$ref`，共享枚举都在 common
文件里。

- `componentType`：`frontend`、`backend`、`database`、`cloud`、`security`、`messagebus`、`external`
- 实体关系文档使用 `entities` 与 `relationships`；`key` 接受 `pk`、`fk` 或 `uk`，
  `fromCardinality`/`toCardinality` 接受 `one` 或 `many`。
- `variant`：`default`、`emphasis`、`security`、`dashed`
- 关系 ID 使用共享标识符模式，并且必须在其集合内唯一。

不要发明字段。写下任何新字段、枚举或受限文本之前，先读它的 schema 定义，包括 common 的 `$ref` 目标。
尤其要检查边界种类、仓库身份与来源引用的形状。示例展示的是结构，并不枚举每个合法值。ID、措辞、事实与
布局都要全新创作。

## 工作流布局契约

新工作流使用 schema v2；当既有源必须保留固定几何时，保留 schema v1。两个版本中 `col` 都保持在 `0..5`
内，语义边标签永不作为间距修复而被删除。存在绝对坐标时，不要只改 `schema_version`：遵循规范的[迁移与
布局回执契约](../renderers/workflow/README.md#migration-and-layout-receipt)。完整的规范性不变量位于
工作流渲染器的[布局契约](../renderers/workflow/README.md#layout-contracts)。对叠放在一个容器内的顺序
阶段，使用一条 v2 lane 与 group，省略 `meta.viewBox`，并用对称的 `yOffset` 值（如 `-90 / 0 / 90`）使
节点围绕 lane 内容居中。保留语义边标签，并按编译器诊断采取行动。

## 图例契约

省略 `meta.legend` 即得到真实的默认值：`auto` 只列出 typed IR 中存在的语义种类。渲染器参考图用
`mode: "all"`；要移除完整图例用 `mode: "hidden"`。在 `entries` 下，只有所选模式 schema 列出的键才合
法；每个键接受 `label`、`visible` 或两者。`visible: true` 可以显示一个未被使用的受支持约定，
`visible: false` 则隐藏它。`hidden` 不可被覆盖。

标签覆盖只改变读者看到的措辞。绝不从散文中推断种类，也不用图例去补偿缺失的节点、状态、消息或流。长标
签会被实测并折行成确定的行。Architecture 的隐式自动 viewBox 从同一实测足迹生长，自动 ERD 画布也按同
样方式定尺寸，因此其默认图例总在生成内容内。为了向后兼容，没有 `meta.legend` 的旧文档可以省略一个放
不进其显式 viewBox 的隐式 auto 图例；这永不改变其 typed 拓扑。创作了 `meta.viewBox` 的 ERD 保留该固
定区域并报告图例容量，而不是丢弃图例。添加 `meta.legend` 意味着呈现是有意且严格的：若解析出的标签放
不进所创作的 viewBox，就缩短或隐藏它们，或按发出的诊断加宽 viewBox。

## 语言一致性

选定一种主要创作语言。用户的明确选择优先；否则使用请求的语言，若请求本身语言中立则使用对话的主导语言
。Viewer locale 单独选择。始终把匹配的 `meta.locale` 写成格式良好的语言标签：英语用 `"en"`，简体中文
用 `"zh-CN"`，西班牙语用 `"es"`，其他语言用对应标签。渲染器消费所创作的 locale，不从图内容字符串推断
语言。省略该字段的文档仍然有效，默认为英语。

`meta.locale` 只控制渲染器拥有的读者界面：`<html lang>`、文档标题后缀、默认 SVG description 与焦点标
签、默认图例标签，以及固定的 Viewer 控件、状态、无障碍名称与错误文本。它从不翻译已创作内容。主要语言
单独应用到标题、副标题、节点与关系文案、边界、lane、group、图例标签覆盖与卡片。双语图仍要为 Viewer
选定一种主要 locale；遵循明确的主要语言请求，其次按提示词顺序或对话主导语言。

捆绑的 Viewer 语言目录登记在 `locales/manifest.json`：目前有 `en`、`zh-CN`、`zh-TW`、`es`、`ko` 与
`ar`。对这些语言，仅凭 `meta.locale` 就能选中完整目录。标签匹配不区分大小写（`zh-cn` 选中 `zh-CN`）
，但地区与文字变体各自独立：`zh-Hant`、`es-MX` 或 `ko-KR` 不会选中任何捆绑目录。

`meta.translations` 是可选的按键覆盖：一个对象，把渲染器的规范消息键（`locales/en.json`，或
`renderers/shared/i18n.mjs` 中的 `catalogKeys()`）映射到译文字符串，其 `{placeholder}` 记号必须与英
文源完全一致。每条消息按此顺序解析：合法的 `meta.translations` 值 → 选中的捆绑目录 → 英语。对捆绑
locale，只提供图中需要改措辞的键；其余语言保留。省略该字段或提供 `{}` 表示无覆盖。对没有捆绑目录的语
言，在这里提供目录。从 `examples/locales/` 或之前已评审的目录复用合适的译文，翻译缺失的键，并用英文
源核对键与占位符。

未知键或占位符不匹配的值会被拒绝并保留较低优先级的消息；它在 stderr 上报告为
`i18n/invalid-translation`，并作为警告出现在 `validate --json`、`deliver` 与 `finalize` 回执的
`diagnostics[]` 中。在非英语 locale 下仍解析为英语的键报告为 `i18n/translation-coverage`，附缺失键及
其英文源文本；补上恰好这些键即可修复缺口。覆盖率描述的是最终解析出的目录，不是覆盖集的大小。

对无法提供 `meta.translations` 的请求语言，不要写一个既无捆绑目录也无译文的 `meta.locale`。把每条面
向读者的创作字符串都保持为请求语言，省略 `meta.locale` 让渲染器安全地使用英语，并明确告诉用户：固定
的 Viewer UI 与 `<html lang>` 仍是英语，产物没有完全本地化。该回退只适用于渲染器拥有的界面；它绝不许
可创作文案回退为英语。不要把 `zh-CN` 静默替换为其他语言或中文 locale，也不要在未披露"未经评审"的情况
下机翻 `meta.translations` 的值。

保持确切的产品名、代码标识符、命令、协议、API 路径与环境名不变。这些术语在本地化文案中可以保持英文，
但其周围的解释性散文必须使用所选语言。渲染器拥有的默认图例标签跟随 `meta.locale`；只有当图需要不同的
领域措辞时才创作 `meta.legend.entries.*.label` 覆盖，并且该创作覆盖保持主要语言。

## 视觉预设默认

默认省略 `meta.visual_preset`。此时渲染器在浅色与深色两种颜色模式下都以 `classic` 打开图。颜色模式与
视觉预设是相互独立的 Viewer 状态：切换 Light / Dark 必须保留当前预设。只在用户明确要求该视觉风格时才
创作 `signal-flow`、`blueprint` 或 `editorial`。

## 工程画像默认

普通系统架构省略 `meta.engineering_profile`。区域、集群与安全边界的措辞本身并不启用工程画像。只在用
户明确要求生产部署拓扑、所有权交接或 fail-closed 部署评审、且源事实已知时，才启用
`deployment-ownership`。一旦启用，不要仅仅为了通过验证而移除工程画像；修复所创作的事实，或如实报告诊
断。

## 标题层级

使用一条简洁标题，让图本身承担解释。默认省略 `meta.subtitle`，绝不用它复述标题、节点、边或卡片。只在
用户明确要求副标题时才包含一条简短支撑行；省略或空白的副标题不得在生成的查看器中留下空行。

## 可执行几何规则

为笔记本与外接显示器生成一个响应式产物，保留所创作的 SVG/viewBox、比例、语义几何与正常文档流。完整图
需要更高时，使用有实际内容的行与 Reader 声明的可读页面滚动；视口适配不授权改变拓扑或缩小字号。

- 节点锚点从边中点开始。`left`/`right` 改变水平端点；`top`/`bottom` 改变垂直端点。对自动
  Architecture 关系，轴偏移小于 16px 的无遮挡对向端口，在两端都保留 16px 角落留白时可以共享一条水
  平或垂直轴。若恰好一个端点属于扩散组，则只有其未配对的另一端移动；两端都扩散的关系保持各自的端口
  与外侧桥，除非一对相向端口能共同使用分离的直 lane，同时保持端点间距、标签以及所有周围路由与障碍
  物的间隙。
- 侧是一个方向契约。路由的首段与末段必须垂直，并沿所指方向向外/向内。
- 在 architecture 与 data-flow 图中，显式 `route: "straight"` 请求一条直段；当端点侧未被固定时，该段
  可以是对角线。产物检查器保留此意图；显式侧、不透明节点间隙与其他质量门槛仍然适用。`via` 优先并保
  留既有规则，包括 data-flow 对正交 via 段的要求。
- 自动端口扩散（Port Spread）是 architecture、workflow 与 data-flow 图的默认渲染器行为。共享的自动端
  点以 16px 角落留白确定且对称地扩散。它不适用于 sequence 消息、单一关系，或显式 `via`、`channelX`
  、`channelY`、`labelAt` 与非 `auto` 路由。
- showcase 路由节奏：每个非零段至少 8px；每个内部段至少 16px。当扩散端口近乎平行时，路由器使用 24px
  端点短段与 16px 外侧桥，而不是制造一个微小的折角。
- showcase 路由紧凑性：显式 Architecture 路由在其正交长度达到障碍感知合法路由的至少 2.5 倍、至少多出
  200px、并把一个控制点送到内容包络之外至少 96px 时，以 `composition/excessive-route-detour` 失败
  。证据记录两个长度、比值、超出量、边界与偏移。移除不必要的 `via` 或把诊断出的走廊向内移，而不是
  扩大画布。在同一外侧走廊上重叠至少 32px 的相关关系被视为有意的总线，仍然有效。
- 共享端点走廊只在语义上保持无歧义时才被允许。不相关共线重叠达 8px 或更多时 showcase 失败。
- 容器边框是有意的穿行几何，但沿结构边框长距离贴边运行的长边不是。
- 穿过不相关不透明节点的边永远是硬失败，与质量画像无关。

### 显式 `via` 坐标

使用解析出的出发锚点 `S = [sx, sy]` 与到达锚点 `T = [tx, ty]`。锚点从边中点开始，但自动路由与 Port
Spread 可以按上述方式移动它们；不要假设从自动路由复制的锚点就是一条新创作显式路由的锚点。显式 `via`
路由不会获得自动 Port Spread。

对第一个航点 `F = via[0]` 与最后一个航点 `L = via[via.length - 1]`，使用以下对齐与方向（SVG 的 y 向
下增大）：

| 侧 | 出发（`fromSide`）：`S` → `F` | 到达（`toSide`）：`L` → `T` |
| --- | --- | --- |
| `top` | `F[0] === sx`，`F[1] < sy` | `L[0] === tx`，`L[1] < ty` |
| `bottom` | `F[0] === sx`，`F[1] > sy` | `L[0] === tx`，`L[1] > ty` |
| `left` | `F[1] === sy`，`F[0] < sx` | `L[1] === ty`，`L[0] < tx` |
| `right` | `F[1] === sy`，`F[0] > sx` | `L[1] === ty`，`L[0] > tx` |

例如，给定 bottom 出发锚点 `S = [180, 160]` 与 left 到达锚点 `T = [360, 260]`，下面这条关系片段向下
离开、向右进入目标：

```json
{
  "from": "source",
  "to": "target",
  "fromSide": "bottom",
  "toSide": "left",
  "via": [[180, 200], [300, 200], [300, 260]]
}
```

完整路径是 `[180, 160] → [180, 200] → [300, 200] → [300, 260] → [360, 260]`。只把第一个航点改成
`[200, 200]` 会让出发变成对角线；改成 `[180, 120]` 则保持 x 对齐，但向上穿过 source 离开，而不是从其
底部向外。两者都违反 `fromSide: "bottom"` 并产生 `clean-flow/endpoint-side-direction`。该示例只确定
端点方向：保持整条路由远离不相关节点，并应用上述其他几何规则。

### 间距与标签

在 showcase Architecture 中，未固定的连接标签在无碰撞时保持默认位置。若发生碰撞，渲染器沿既有路由尝
试一组有界的邻近位置，避开已解析画布内的节点、边界标题、其他标签与其他路由。显式 `labelAt`、
`labelDx`、`labelDy` 或 `labelSegment`（包括零值）会禁用该回退。路由与拓扑保持不变；若没有邻近位置是
干净的，验证仍报告原始碰撞。添加控件之前，先用 `--layout-json` 检查解析出的标签。standard 放置保持既
有行为。

间距建议指方框之间的清晰间隙，不是中心距。165px 宽的节点之间 200px 的中心距只剩 35px 清晰间隙。

对关系标签，要求：

```text
clear gap > label mask width + 8px breathing room
label mask width ≈ 6.5px × ASCII units + 13px
CJK characters count as two units
```

关系标签是语义数据。若间隙太小，先移动标签、调整路由或间距，再在保留语义的前提下缩短措辞。只有已被两
端点完全隐含、且不携带协议、动作、方向、同步/异步行为或跨边界机制的措辞才可省略。保留每条有意义的标
签。删除标签不是间距修复。若一条关系因端点完全隐含而初始就无标签，要解释为何该措辞是冗余的；这是语义
创作选择，不是间距修复。在 workflow v2 中，先让编译器分配其实测遮罩，再应用诊断出的 `labelAt`、
`labelDx`/`labelDy` 或 `labelSegment`。除非多条边共享受限通道，否则一次只应用一个诊断出的几何控件。
若共享受限通道，按实测几何计划最小的一组耦合改动，并一起验证。Architecture/workflow 通过 `validate
<type> <candidate.json> --layout-json` 提供布局证据；其他类型使用验证诊断与渲染 SVG 的几何。添加手动
路由之前，检查是否有多余的代理添加控件禁用了自动端口扩散；保留用户要求的路由意图。使用上述实测间隙规
则，不要猜测坐标。

### 修复证据

对 architecture，`validate architecture <input.json> --layout-json` 暴露解析出的组件方框、边界框、连
接点与标签位置。可测量的被拒布局也返回这些字段，附带 `ok: false`、`contract:
"archify-architecture-layout-v1"`、诊断与退出码 1。这是修复证据，不是产物验收；它不写 HTML。畸形输入
或实现失败保留普通失败回执，不带布局。

对 `layout/boundary-out-of-bounds` 使用实测到的失败侧。左/上负坐标需要向内移动；增加 viewBox 宽/高只
解决右/下溢出。边界可以让成员跨行排布。保持真实成员关系不变，移动成员后重新检查相连的路由。

自动 architecture 画布包含路由点，以及节点、框与标签。已创作的 viewBox 仍是权威。在 showcase 中，
`layout/route-out-of-bounds` 指出被裁剪的路由点；负坐标需要向内路由，右/下溢出也可以用更大的创作画布
。放大画布后重新检查桌面可读性。

当多个交叉/走廊诊断涉及同一批节点时，先综合考虑它们的位置，再添加路由控件。应用一次连贯的修复并验证
；独立的标签微调修不好共享的布局瓶颈。按代码、对象与阶段比较诊断，不要只看总数。

### 修复顺序

1. 修复缺失/非法的 `meta.quality_profile` 与 schema 错误。
2. 修复节点重叠或越界放置。
3. 修复穿节点的边与端点方向错误。
4. 修复交叉、歧义走廊、贴边长跑、过度绕行与路由节奏。
5. 修复标签到节点、标签到标签，然后标签到路由的间隙。
6. 修复离开画布的标签：用 `labelAt`/`labelDx`/`labelDy`/`labelSegment` 移动标签，或加宽
   `meta.viewBox`。建议的 `labelDx`/`labelDy` 值是替换所创作字段，不是在其上累加。

每次编辑后，按交付契约的要求重跑完整的 `finalize`；两次 finalize 之间只用 `validate` 做聚焦诊断。按
稳定的 `code`、精确的 `subject`、实测的 `evidence` 与 `supportedFixes` 消费 `diagnostics[]`。若诊断
给出 `labelAt`，就使用那个点，不要另估偏移。

## 模式放置

### Architecture

用 [构成与语义](authoring-defaults.md#composition-and-meaning) 选择总览还是机制细节。使用一条明显的
主读路径；当所请求拓扑需要空间时，它可以跨越有内容的行。总览在其选定抽象层次上保持可读；当实现细节能
回答读者的问题时再展开。只对真实的所有权、信任、进程或部署边界分组。边界不替代关系。

schema 支持时优先网格放置。自由位置适合有界例外，不适合散文级的坐标规划。当事实如此时，让外部参与者
留在系统边界之外。边界绘制为围绕其全部成员的带内边距方框，因此要把成员放成一个紧凑的轴对齐簇（不留任
何空档让非成员坐进带内边距的框内），并让每个非成员都在该框之外；showcase 质量下，
`layout/boundary-encloses-non-member` 会报告被框吞进的组件。standard 保持既有验收行为。

### Workflow

lane 表达职责或阶段。列 `0..5` 表达逻辑推进。新工作流从 `readable-v2` 开始；只为旧几何兼容保留
`fixed-v1`。在 readable-v2 中，当不同的 `yOffset` 值为完整矩形、标签与连接路由留出空间时，节点可以共
享 `(lane, col)`。保持主路径单调，保留语义边标签，把重试与异常返回路由到主 lane 走廊之外。

#### Workflow 视口修复

当 `viewer/viewport-overflow` 包含 `workflowLanes` 时，先检查最高的渲染帧及其节点跨度，再改源。测量
值是 CSS 像素；节点上下的空间包含 lane 标题与路由，因此不是可移除空白预算。帧 ID 标识渲染出的 lane
序号。

运行 `validate workflow <source.json> --layout-json`，把这些帧匹配到源 lane 与节点。检查是否很多步骤
共享最后一个逻辑列并使用大的 `yOffset` 值。readable-v2 在偏移周围保留对称空间。在同列垂直堆叠、隐式
画布、无绝对路由或标签固定时，它逐 lane 独立测量。其他情形出于兼容保留共享高度几何；见规范的 [lane
测量契约](../renderers/workflow/README.md#readable-v2)。

在源的所有权与显式几何允许之处，把步骤重排到各逻辑列与有意义的 lane 上，保持主路径单调。保留每条必需
的节点、关系、标签与语义检查。若所有权或绝对固定阻止重排，报告该约束，而不是自动合并 lane 或移动固定
点。验证改后的 JSON，交付新的 HTML，然后重跑浏览器检查并检查首屏；仅静态通过不能断定视口适配。这些是
修复方向，不是保证坐标。

### Sequence

参与者按对话角色排序。消息拥有自己的垂直顺序。return/async/security 变体按语义使用，不作装饰；
sequence 不使用自动 Port Spread。段的 `from`/`to` 边必须与每条消息箭头（`message.y`）保持至少 4px：
沿箭头的边让读者无法判断消息属于哪个阶段，showcase 质量会报告 `sequence/segment-message-border-run`
。standard 保持既有验收行为。

第一稿形状：每条消息需要 `id`、`from`、`to`、`label` 与不小于 160 的整数 `y`。`from` 与 `to` 必须是
不同的参与者：不支持自消息（`sequence/self-message-unsupported`）。可选的阶段带是 `segments[]`，只有
`from`、`to` 与 `label`（segment 没有 `id`）。在参与者上发明 `pos`/`size` 会导致 schema 验证失败：顺
序本身就决定位置。省略 `meta.viewBox`，让自动高度适配时间线 + 图例（最小 327px 可读带）而不是固定
760px 下限；这样 2–3 个参与者的扩散在标签放得下时收在 920px 默认值之下（4 个及以上仍为 920px；长标签
仍会加宽）。

### Dataflow

阶段表达变换或托管。行分隔并行流。给每条流一个简明的数据契约或移动标签；按必需的 [Dataflow 创作默认
值](authoring-defaults.md#presentation-and-modes) 选择其视觉约定。

第一稿形状：声明 `stages[]`（每个是 `{label}`），然后用整数 `stage` 与 `row` 放置每个节点，不用
`pos`/`size`。流是 `flows[]`，必需 `from`、`to` 与非空 `label`。

省略 `meta.viewBox`，在任一质量画像下让画布宽度适配全部阶段与节点，包括显式节点宽度。宽度用内容 +
24px 右侧内边距，最小 480px（五个默认阶段仍需约 1068）；左缘溢出仍需节点修复。已创作的 viewBox 保持
固定。showcase 的节点增长、可读字号、内容高度、端口桥与有界标签放置，只在画布与全部节点宽度都省略时
适用。`--quality` 覆盖 `meta.quality_profile`；未给定时，渲染器使用设置的 `ARCHIFY_QUALITY_PROFILE`
，否则使用 JSON 画像。

### ERD

把 schema ERD 既当作表目录也当作关系图。若 schema 超过 8 张表或 50 个字段，它是密集的全 schema 图：
从 `meta.quality_profile: "standard"` 开始，不要用完整的字段可见性去换反复的 showcase 路由修复。把每
个物理列放进 `attributes`，保留源 SQL 类型，并在类型串中保留该字段的中文备注，形如 `SQL_TYPE｜中文备
注`，因为 schema 没有单独的 comment 属性。默认查看器在 `read` 级显示这些行；不要依赖悬停/聚焦或卡片
来展示物理字段。卡片可以解释约束、推断关系或领域规则，但绝不替代字段清单。

放方框之前，用核实过的表名、注释、模块路径与外键含义把表分类到功能域。把域名放进 `tag`，并给每个域一
整块实心网格矩形：单行、单列或填满的矩形块，不是 L 形或对角线，且矩形的每个格子都装着它的表之一。同
tag 的所有表聚在一起；不要在成员之间插入无关表。填满这样一个矩形的域绘制为其表后面的一条带标签色带，
因此不用逐框阅读也能看出分组；表没有填满一个矩形的 tag 得不到色带，而因为色带是唯一绘制域名的位置，
渲染器会报告 `erd/domain-not-drawn`，而不是发布一张无法命名该域的图。绝对坐标完全没有网格格，所以带
tag 的表总需要 `row`/`col`。把父表/核心表排向共享边界，并把它们的直接子表放在旁边或下方。列从左往右
读，行从上往下读，因此相邻列之间的关系是一条直走廊。绝不把无关实体放在两个对齐锚点之间；路由器可以绕
行，但干净走廊更短、读起来更好。连接表（junction table）有两个父表：把它放在紧邻两者或两者之间的格子
里，不要放在其中一个下方且两表之间隔着其他表，并保持共享其域 tag 的每张表都在一个实心格矩形内。关系
必须连接两个不同实体；`manager_id` 这样的自引用保持为外键列（可选加卡片），而不是
`employees`→`employees` 边。这种常规分组布局用 `row`/`col`，只有在诊断指出具体几何问题之后才用显式
`pos`/`via`。

在 `key` 中声明一列承载的每一个键角色，在 `references` 中声明真实引用。一列常常同时是多种角色：连接
表的 `tenant_id` 既在主键中，又是指向 `tenant.id` 的外键，因此 `key` 接受单个角色或列表（`["pk",
"fk"]`），丢掉角色就等于声明得比 schema 少。多对多对是模型的真实事实，要声明它，并在存在连接表时指出
连接表。关系有两个端，每端声明自己的最大基数，因此 `many` 对 `one` 的外键需要同时给出
`fromCardinality` 与 `toCardinality`；`fromOptional`/`toOptional` 只把同一端的最小基数从一降为零（可
选的 `one` 端读作零或一，可选的 `many` 端读作零或多）；`identifying: false` 绘制非标识虚线并拥有这条
虚线：schema 拒绝会让关系在其旁边画成实线的 `variant`。叉脚朝向它所描述的实体，所以绘制出的符号声明
的是该端的最大基数，不是行进方向。

表的一侧容纳的端数有限：端口最多按 `(side extent - 32) / (ends - 1)` 间隔扩散，而一个基数符号高 14
单位。关系端数超过这个容纳量就是 `layout/marker-capacity`，它会指出表、侧与出路：加字段让这一侧更高
、扩散各关系，或减少扇入。绝不用隐藏基数来修复。

当模型必须在一块笔记本视口内完整读下来时，给每个域各留一列。Reader 把宽画布放大到读者宽度，把高画布
收窄到整页适配，因此同样十一张表按四个水平域堆叠时比按四个垂直域堆叠更费字号。在长关系必须穿过域的地
方留出整块格：穿过被占用格的走廊会强制折行，而低于内部下限的折行是
`composition/short-interior-segment` 失败。

自动画布的尺寸保证默认图例总在生成内容内；作者用 `meta.viewBox` 固定的画布会报告其图例容量而不是丢掉
键。带、端口与读者契约见 [`../renderers/erd/README.md`](../renderers/erd/README.md)。

### Tree

树回答"这是如何分解的？"：一个根，其余每个节点都恰好命名一个 `parent`。链接只表示包含；不要用树表达
调用、数据移动或跨分支依赖。不做任何推断：缺失的父节点（`tree/missing-parent`）、零个或多个根（
`tree/root-count`）、父循环（`tree/cycle`，同时覆盖其下所有搁浅节点）与重复 id 都会被拒绝。子节点按
声明顺序阅读。

浅而均衡的分解用 `layout.direction: "down"`（默认）；深或叶多的树（如仓库布局）用 `"right"`。向右的
树把每个父与其第一个子对齐，并在 reader 中垂直滚动。标签在词间折行。`collapsed: true` 让分支在
Viewer 中初始折叠；它从不从产物中移除内容，每次导出都是完整树。对真实代码库，每个节点都要落在观察到
的路径上并附 `sources`。见 [`../renderers/tree/README.md`](../renderers/tree/README.md)。

### Class

类图解释一个模块内部的契约：存在哪些类型、哪些成员对解释重要、类型之间如何关联。按问题需要选择成员；
一个类型可以一个成员都不显示。每个类型声明其 `kind`（`class`、`abstract`、`interface`、`enum`、
`record`）；除 `class` 外的每种 kind 都绘制其 UML 关键字，因此 interface 永不会被读成空类。对真实代
码库，每个类型、成员与关系都要落在仓库证据上并附 `sources`。

每条关系读作 `from` -> `to`，其 `kind` 决定记号：`dependency`（`from` 使用 `to`，虚线开箭头）、
`association`（`from` 持有 `to`，实线开箭头）、`inheritance`（`from` 扩展 `to`，实线空心三角）、
`realization`（`from` 实现接口 `to`，虚线空心三角）、`composition` 与 `aggregation`（`from` 是整体，
实心或空心菱形在 `from` 端）。realization 必须从非接口指向接口；inheritance 不得跨越接口边界；继承循
环会被拒绝。

类型放在 `row`/`col` 网格上，父类型在子类型之上。指向同一父类型的两个或更多自动泛化画成一条带单个三
角的层级总线。成员永不截断：类型长到其最宽成员为止，上限 `layout.typeMaxW`，更长的成员在参数边界处折
行。见 [`../renderers/class/README.md`](../renderers/class/README.md)。

第一稿形状：类型用 `row`/`col`（不用 `pos`/`size`），字段放 `attributes[]`，操作放 `methods[]`，
`parameters` 是单个字符串如 `"msg: Message"`（不是对象数组）。枚举成员是只有 `name` 的 attribute。关
系需要 `id`、`from`、`to` 与 `kind`。

### Timeline

时间线回答"何时发生了什么，相隔多远？"。每个事件都需要带显式 `Z` 或 `±HH:MM` 偏移的 ISO 8601 `at`；
缺偏移的时间戳会被拒绝，而不是被猜。`meta.timezone`（IANA，默认 `UTC`）是刻度与标签的显示时钟，轴标
题会说明它。`meta.evidence` 必填：记录过的事件（日志、git 历史、值班记录）用 `observed`，解释性输入
用 `illustrative`。绝不把发明或近似的时间标为 observed，也绝不用输入中没有的事件填补空隙。

用 `lanes` 表达来源或类别（发布、监控、响应）；每个事件随后命名其中之一。每个事件的可见文本是
`title`（不是 `label`）。`kind`（`default`、`change`、`alert`、`action`、`recovery`）只给卡片上色；
发明 `milestone` 之类的值会导致 schema 验证失败。无论创作顺序如何，事件都按时间顺序绘制；同时与接近
的事件堆叠。默认情况下，超过中位间隙 8 倍且超过跨度 10% 的安静期绘制为固定宽度的断口，并标注被省略的
时长；`layout.breaks: "none"` 保留一条比例轴。见
[`../renderers/timeline/README.md`](../renderers/timeline/README.md)。

### Waterfall

瀑布图对一个请求、任务或 agent 运行回答"时间去哪了？"。每个 span 有 `id`、`name`、`start`，以及以
`meta.unit`（`us`、`ms`、`s`；默认 `ms`）计的 `end` 或 `duration`，另有可选的 `parent`、`status`、
`service` 与 `detail`。条的位置与长度只来自这些数字。`meta.evidence` 必填：只有记录过的计时（trace
导出、日志、profiler、计时运行）用 `measured`；否则用 `illustrative`。绝不从代码结构推断时长，也绝不
把估算数字呈现为实测。

没有记录到结束的 span 必须是 `status: "incomplete"`；它绘制为指向最后记录时刻的下界。矛盾的
end/duration、早于开始的 end、缺失的 parent 或 parent 循环都会被拒绝。百分比总是"占墙钟总时长"；父子
时长是包含性的，永不求和。除非输入声明了依赖，否则不要标注关键路径或等待时间。见
[`../renderers/waterfall/README.md`](../renderers/waterfall/README.md)。

### Lifecycle

Schema v3 是唯一的 lifecycle 契约。`mainPath` 列出从初始状态开始的主路径；每个相邻对都需要一条转移。
渲染器拥有全部几何：主路径是一行，回到较早阶段（或跳前）的转移变成其上方的弧，其他每个状态都位于其分
支来源状态之下，离主路径每远一步就深一行。等价出口只在以下条件同时成立时共享一条箭头：标签、备注与变
体都匹配，且至少两个主路径阶段中恰好有一个组符合该目标。相邻阶段获得复合框；不相邻阶段共享一条总线。
其他出口保持独立，包括其原转移上的不同备注。不要为强行共享而删除或复制备注。没有 lane、列、尺寸或路
由控件。布局重试保持转移文本的最小间隙，并在主路径行的最小宽度将超出原文本可读预算时停止加宽；最终的
宽度与标签间隙检查仍然适用。

主路径保持读者会走到的阶段，最多约六个状态，转移标签保持简短。可恢复的失败需要一条回到活跃状态的真实
转移；一张写着"retry"的卡片不是拓扑。

按读者应该注意到什么来选每个状态的 `type`，因为颜色与角落印记跟随它：对人、时间或输入的暂停用
`waiting`；评审或分支点用 `decision`；好或坏的结果用 `success` 或 `failure`；停放状态与两者皆非的结
果用 `neutral`；外部方持有工作时用 `external`；其余用 `active`。从 Mermaid `stateDiagram`：`[*] -->`
命名第一个 `mainPath` 状态；带 `--> [*]` 的状态是结果（`success`、`failure` 或 `neutral`；当它没有其
他出边时画为终结）；`<<choice>>` 变成 `decision` 状态。把复合 `state X { ... }` 展平为其内部状态，并
从每个内部状态以一个标签重复其出口；共享该出口的相邻主路径阶段自动成框。并发区域（`--`）没有
lifecycle 形态：每个区域画一张 lifecycle。

## 仓库证据

当图必须反映真实代码时，先检查仓库入口、运行时边界、存储、传输与部署配置，再创作。只记录你真正验证过
的证据。`--repo-root <path>` 被每种图类型的 `render`、`validate`、`deliver` 与 `preview`、
architecture 的 `compare` 以及 workflow 的 `migrate` 接受；每种模式以同样方式验证 `meta.repository`
与节点 `sources`。迁移带源证据的 workflow 需要同样的 `--repo-root`，使其候选在替换目标之前得到验证。
绝不只凭文件邻近或命名推断运行时因果。

声明 `meta.repository.url` 与一个完整的 40 字符 `revision`，然后把 `sources` 附到该模式的节点集合上
（Architecture 的 `components[]`，Workflow 与 Data Flow 的 `nodes[]`，Sequence 的 `participants[]`，
Lifecycle 的 `states[]`），带仓库相对 `path`、可选 `line`、`end_line` 与 `label`。验证在该 commit 读
取 blob，独立于工作树编辑。验证忽略本地 Git replacement refs，包括 `GIT_REPLACE_REF_BASE` 选中的那些
，并始终读取固定 SHA 处的原始对象。它不修改仓库配置，也不删除 replacement refs。每种链接模式都要求：
匹配的本地 origin、可用的 commit、有界路径、blob 与合法行号范围。验证是本地的，不发出远程请求；它既
不确立公开可用性，也不确立当前读者的访问权限。

`link_mode` 默认为 `web`。GitHub、Gitee 与 GitLab 的 HTTPS 仓库 URL 生成固定 revision 的链接；公共主
机 github.com、gitee.com 与 gitlab.com 自动选择 provider。可选的 `provider: "github"`、`"gitee"` 或
`"gitlab"` 必须与公共主机一致。自管 GitLab 主机声明 `provider: "gitlab"`；Archify 从不联系主机去探测
其 forge。既有的 GitHub 声明与默认交付回执字段保持兼容。

GitLab URL 可以命名嵌套组（`group/subgroup/project`）。源链接使用
`<url>/-/blob/<revision>/<path>#L<line>-<end_line>`，仓库链接使用 `<url>/-/tree/<revision>`。带行区
间的 Markdown 源（`.md`、`.markdown`）链接到纯文本视图（`?plain=1`），使被引用的行高亮，而不是渲染文
档。GitLab 仓库路径与 GitHub 一样按不区分大小写比较。

```json
{
  "url": "https://gitee.com/team/service",
  "revision": "0123456789abcdef0123456789abcdef01234567",
  "provider": "gitee"
}
```

```json
{
  "url": "https://git.example.com/platform/payments/service",
  "revision": "0123456789abcdef0123456789abcdef01234567",
  "provider": "gitlab"
}
```

对内部或不受支持的 forge，选择 `link_mode: "local-only"`。Viewer 保留 SRC 标记、可搜索的文件路径、行
区间与 revision 标签，不带仓库或源超链接。证据回执增加 `linkMode: "local-only"`。`url` 仍是必需的，
作为预期的来源身份；local-only 禁用的是链接，不是身份验证。没有 origin 的仓库不受支持。

```json
{
  "url": "http://git.internal:3000/Platform/Services/service",
  "revision": "0123456789abcdef0123456789abcdef01234567",
  "link_mode": "local-only"
}
```

local-only 接受 HTTP(S)、`git@host:path` 与 `ssh://git@host[:port]/path` 地址，包括嵌套命名空间。声
明不带凭证的地址；checkout 的 origin 上的 HTTP(S) 凭证不用于身份，并从诊断中脱敏。主机名按不区分大小
写比较；除 GitHub 与 GitLab 外，仓库路径保留大小写。末尾斜杠被归一化掉。只有 GitHub、Gitee 与 GitLab
（gitlab.com，或以 `provider: "gitlab"` 声明的主机）会归一化末尾 `.git`，并在同一主机上匹配标准
HTTPS/443 与 Git SSH/22；另一主机或端口的 GitLab SSH 端点不被推断。对其他主机，使用实际克隆地址：传
输、端口、`.git` 后缀以及 remote 相对与绝对路径都必须匹配。例如，`git@host:Team/repo` 与
`ssh://git@host/Team/repo` 不同；`git@host:/Team/repo` 与后者匹配。SCP 风格路径保留字面百分号转义，
而 URI 路径会解码它们。SSH 主机别名与 forge 特有的浏览/克隆前缀不做猜测。本版本未实现
Gitea/Forgejo/Bitbucket 的 web 链接；在经过测试的链接 provider 可用之前使用 local-only。未知 web
provider 以诊断失败，而不是发出猜测的链接。

## 手工放置回退

只在没有任何渲染器可运行时使用。从 `assets/template.html` 出发，保持语义 CSS 类，保留内联 SVG/无障碍
结构，并执行交付视觉清单。绝不引入破坏深/浅色一致性的内联字面色。

## 节点图标

对领域特定图，在 architecture 组件、workflow/dataflow 节点、sequence 参与者或 lifecycle 状态上设置可
选 `icon`。日常概念选 `calendar`、`clock`、`person`、`briefcase`、`flag` 或 `moon`；完整目录（包括既
有技术与 lifecycle 符号）在 `common.schema.json#/$defs/nodeIcon`。用 `icon: "none"` 隐藏角落符号。省
略 `icon` 保留基于类型的默认；lifecycle 的 `start`、`active` 与 `neutral` 状态默认无符号。这些内联
SVG 符号由渲染器拥有并随图导出；不接受 URL 与原始 SVG。

图标选择只改变角落符号。节点的类型仍决定颜色与语义分组；品牌标识保持独立。对假日工作流，把 `type:
"backend", icon: "calendar"` 与 `meta.legend.entries.backend.label: "假期"` 配对，补班工作用 `icon:
"briefcase"` 加合适的图例标签。保持节点标签有意义：图标是装饰性的，并对辅助技术隐藏。

完整 workflow 示例见 [假日规划](../examples/holiday-planning.workflow.json)。
