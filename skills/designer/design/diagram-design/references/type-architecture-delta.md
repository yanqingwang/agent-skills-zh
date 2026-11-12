> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-architecture-delta.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 架构增量图

**适用场景：** 用两张同步的拓扑快照，解释系统迁移、服务抽取、基础设施重构或集成变更。展示哪些组件与关系存续、出现、消失、属性变化、移动或重新连接。

**不适合本类型：**

- 单一系统的快照 → **架构图**（`type-architecture.md`）。
- 只有属性差异、没有拓扑故事 → **对比表**。两版配置不需要两张节点图。
- 随时间变化的请求 → **时序图**（`type-sequence.md`）；部署阶段 → **时间线**（`type-timeline.md`）。增量图只有两个状态，不建立迁移顺序、停机或因果。
- 单一环境内的主机/容器放置 → **部署图**（`type-deployment.md`）。

## 版式约定

- **三栏，一个阅读顺序：Before · Changes · After。** 两张拓扑栏同宽、同高、同内部网格间距。中栏是简短的变更台账，不是第三张拓扑。用有意义的版本号或日期为两张快照命名。
- **保持心理地图稳定。** 先把 Before 的坐标复制进 After。仅当某个留存组件的移动本身是故事的一部分、且获得 `MOVED` 条目时才移动它。不要对每一栏独立跑布局算法。
- **栏位位置不是组件位置。** 每张快照放进一个 SVG `<g transform="translate(x y)">`；组件边界与关系路径写在局部坐标中。Before 与 After 的原点共享一个 y 坐标，台账占据水平间隙。
- **共享网格：** 默认 4px 间距。每个组件的局部 x、y、宽、高都是该间距的倍数。随附示例使用两个 `336 480 4` 网格；整体 SVG 响应式缩放时不改变它们的局部几何。
- **预算：** 整个对比最多 **8 个唯一组件**、**10 条唯一关系**、**8 条台账条目**。一个留存 ID 只计一次，不是每张快照各计一次。既 changed 又 moved 的组件消耗两条台账条目。更大的迁移拆成命名的子系统或阶段；绝不为了塞下而删边。
- **连接线：** 使用架构图的圆角正交路由与挂点规则。本类型中，连直线连接线也是 `<path>` 元素，让关系身份与端点共用一套语法。路径先于组件绘制。一条稳定关系可以改道去接一个移动过的组件，而不算 `REWIRED`。
- **节点：** 两个状态中都打印同一个稳定 ID 与人类可读名称。把名称、职责、实现版本与协议当作语义属性；底层对象存续时，改名不断绝身份。
- **台账：** 每个 `(object ID, change)` 对一条简短条目。以大写变更词开头，点名对象，陈述实际差异。台账中不描述未变化的对象。保持可读的文字宽度，需要时用换行的 `<tspan>`。
- **响应式呈现：** 小屏幕上保留三栏对比，提供可访问的水平滚动区域与可见的滚动提示。不要把标签压缩到无法辨认，也不要把两张快照堆成各自缩放的图。打印与导出保留完整对比。

## 变更词汇与冗余编码

颜色是次要的。每个变更都能从文字加形状或线型处理读出；未变化的对象保持安静的背景。使用既有皮肤 token，把 accent 留给编辑焦点，而不是分配五种状态色。

| 状态 | 含义 | 非颜色处理 |
|---|---|---|
| `unchanged` | 同一身份、语义、位置与端点 | 普通实线轮廓；无台账条目 |
| `added` / **ADDED** | 仅在 After 中出现 | `+` 徽章或加号形标记；实线轮廓 |
| `removed` / **REMOVED** | 仅在 Before 中出现 | `−` 徽章加虚线轮廓/路径 |
| `changed` / **CHANGED** | 语义签名不同的留存对象 | `Δ` 徽章或内嵌线，外加显式的旧 → 新台账描述 |
| `moved` / **MOVED** | 局部 x 或 y 不同的留存组件 | 方向/位置标记，加一条点明迁移的台账条目 |
| `rewired` / **REWIRED** | 有序 source/target ID 不同的留存关系 | 不同的虚线处理或端点标记，旧 → 新端点写入台账 |

不要用 After 中缺失的节点代替一条没有 `REMOVED` 条目的删除。不要为了回避解释端点身份，就用 `ADDED` 边顶替 `REWIRED` 边。被替换的组件获得新的稳定 ID 与独立的删除/新增条目；仅凭位置无法确立连续性。

## 公开的 HTML 元数据契约

这是编写与校验面，不是从可见标签反推的序列化。以下属性在适用处全部必需；空的、布尔式的、重复的或畸形的声明都算 finding。ID 区分大小写，匹配 `[A-Za-z][A-Za-z0-9_.:-]*`；不含空白。

### 图与快照

文件恰好有一个 `<svg data-diagram="architecture-delta">`。保留标准的可访问 SVG title/description 契约。两个直接子 `<g>` 元素声明 `data-snapshot="before"` 与 `data-snapshot="after"`。各自具备：

- `data-grid="<width> <height> <pitch>"`：两张栏中相同的三个正有限数。宽与高必须是间距的倍数。
- `transform="translate(<x> <y>)"`：恰好一个有限的两数平移，仅用于栏位原点。也接受逗号分隔的平移。

对象归属从外层分组继承。对象不能同时在两张快照之外、处于嵌套快照中、或嵌套在另一个对象内部。其他几何变换、嵌套 SVG 视口、SVG 动画、`<use>` 与外来对象都在此静态语法之外。不要把对象或台账条目放进 `<defs>`、`<symbol>`、模板或其他不渲染的容器。

### 组件

每个组件是一个 `<g>`，声明：

| 属性 | 契约 |
|---|---|
| `data-kind="component"` | 标识组件分组 |
| `data-object-id` | 稳定对象身份，在各快照内唯一 |
| `data-status` | 一个小写状态，或空格分隔的组合 `changed moved` |
| `data-signature` | 非空语义签名；见下方签名规则 |

分组内恰好包含一个**直接**的 `<rect data-role="bounds">`，带显式的有限数值 `x`、`y`、`width`、`height`。位置非负，尺寸为正，矩形落在其局部网格之内。四个值全部对齐网格间距。这些就是实际绘制的节点边界，不是隐藏的代理矩形。

### 关系

每条关系是一个 `<path>`，带 `data-kind="relationship"`、`data-object-id`、`data-status`、`data-signature` 与 `data-from` / `data-to`。其稳定 ID 与组件 ID 相互独立。两个端点都解析为**同一张快照**内的组件 ID。端点顺序有方向：交换 source 与 target 就是一次 rewire。

快照之内、组件之外的每条 path 都是关系，必须携带完整元数据。装饰性路径属于组件内部，或位于快照之外（如栏位规则线与台账分隔线）。把连接线上的元数据全部删掉，它也不能从校验中消失。

关系状态为 `unchanged`、`added`、`removed`、`changed`、`rewired`，或组合 `changed rewired`。`moved` 只适用于组件；`rewired` 只适用于关系。`unchanged`、`added`、`removed` 不得与任何其他 token 组合。

`d` 属性是一个绝对 `M` 后接绝对 `L`、`H`、`V`、`Q` 或 `C` 段。接受隐式重复坐标组。相对命令、额外子路径、闭合路径、弧、缺失坐标与非有限坐标一律判负（fail closed）。标准版式用正交线与二次曲线拐角；三次段留给小型的跨越桥。端点与控制点保持在局部网格之内。路径起点贴到源矩形的周长，终点贴到目标的周长，描边/箭头圆角容许 2px。

### 状态与签名规则

- 只出现在 Before 的 ID 恰好为 `removed`；只出现在 After 的 ID 恰好为 `added`。
- 留存 ID 保持其 kind 与两张快照中相同的状态集合。绝不用组件 ID 循环充当关系，反之亦然。
- 语义签名不同**当且仅当**留存对象为 `changed`。用你想比较的语义属性确定性构造，例如 `orders-api:v2;mode=enqueue` 或 `protocol=https;operation=create-order`。改名属于故事的一部分时，把新显示名包含进来。值未变化时保持属性顺序与拼写。
- 签名排除对象 ID、快照、状态、坐标、视觉样式与关系端点。这些各有自己的检查。单纯移动或 rewire 不得改变签名。
- 留存组件的局部 `(x,y)` 不同**当且仅当**它是 `moved`。宽/高变化额外要求 `changed` 与变化的签名。签名变化本身不要求边界不同。
- 留存关系的有序 `(data-from,data-to)` 对不同**当且仅当**它是 `rewired`。该对保持相同时路径可以改道，例如端点组件移动时。
- 数值声明是有限的，绝对值不超过 10,000,000；单位后缀、百分比与 CSS 计算不算坐标声明。

### 台账

每条条目是两张快照之外的一个可见 SVG `<text>`，带 `data-change="ADDED|REMOVED|CHANGED|MOVED|REWIRED"` 与 `data-target="<一个对象 ID>"`。其渲染文字以同一个大写词开头，后接解释。检查措辞时会包含后代的 `<tspan>` 文字；元数据只放外层 `<text>` 上。

台账是由对象状态推出的 `(target, change)` 对的精确集合。没有缺失条目、重复对、未知目标，也没有未变化对象的条目。同一目标只在声明两个变更时才有两条条目。每张图至少一条台账条目、每张快照至少一个组件、整体至少一条关系。

### 元数据示例

以下摘录展示一个 changed 组件；完整图还需要其余组件、关系与可访问的 SVG title/description。

```svg
<svg data-diagram="architecture-delta" viewBox="0 0 1000 400">
  <g data-snapshot="before" data-grid="320 320 4" transform="translate(24 64)">
    <g data-kind="component" data-object-id="orders" data-status="changed"
       data-signature="orders-api:v1;mode=dispatch">
      <rect data-role="bounds" x="80" y="96" width="144" height="64"/>
      <text x="96" y="120">orders · direct dispatch</text>
    </g>
  </g>
  <g data-snapshot="after" data-grid="320 320 4" transform="translate(656 64)">
    <g data-kind="component" data-object-id="orders" data-status="changed"
       data-signature="orders-api:v2;mode=enqueue">
      <rect data-role="bounds" x="80" y="96" width="144" height="64"/>
      <text x="96" y="120">orders · enqueue</text>
    </g>
  </g>
  <text data-change="CHANGED" data-target="orders" x="376" y="176">
    <tspan>CHANGED orders</tspan>
    <tspan x="376" dy="20">Direct dispatch → enqueue</tspan>
  </text>
</svg>
```

## 校验及其边界

运行 `python3 scripts/verify-architecture-delta.py --all`（或传入显式 HTML 路径）与 `python3 scripts/test-verify-architecture-delta.py`。无参数时也检查随附示例。标准库 HTML 解析器读取真实属性（含未加引号的值与实体），忽略注释，并拒绝畸形的 SVG 嵌套。合成 fixture 独立于随附坐标，同时证明合法情形与对抗性变更；light、dark、full 三个变体都会检查。

校验器强制执行声明的结构、差分语义、网格/边界几何、绘制的关系端点、预算与精确的台账覆盖。它拒绝 CSS transform/位置覆盖、可能改变边界的 CSS 尺寸、转义的 CSS 声明、显式隐藏的对象/台账，以及常见的 CSS 隐藏规则。外层 SVG 的普通响应式缩放仍然合法。

它**不是**浏览器渲染器，也不是对源系统的证明。诚实的签名、与签名一致的标签、可读的形状/虚线处理、准确的迁移故事，仍是作者的责任。花哨的 CSS 级联/变量效果、裁切与遮挡、连接线交叉、中间线段净空、台账摆放与屏幕阅读器质量，仍需要常规的皮肤、可访问性、几何与渲染版式闸门，加上桌面/移动目视审查。把语义几何留在 SVG 属性里，不要让 CSS 成为数据模型的一部分。

## 反模式

- 两张各自独立排布的快照，制造出虚假的移动。
- 中间台账只写"更新了"，不点名对象与差异。
- 只用颜色的状态，或每种变更各配一种亮色。
- 未变化的节点位置为了腾地方而漂移，却没有 `MOVED` 条目。
- 语义修改藏在未变的签名后面，或只因快照变了就把所有签名重新生成一遍。
- 把边重画到另一个组件，端点元数据却保持不变。
- 把留存对象计两次，用来给对比中丢弃其他对象找理由。
- 把这张对比当作可执行的迁移计划。排序、回滚、可用性与数据一致性需要各自的解释。

## 示例

- `assets/example-architecture-delta.html`：极简 light，订单履约迁移；涵盖全部五种变更。
- `assets/example-architecture-delta-dark.html`：极简 dark，ID、签名、拓扑与坐标完全相同。
- `assets/example-architecture-delta-full.html`：同一次迁移的完整编辑版处理。

示例保留了 storefront 与 order store，把订单 API 改为入队，移除遗留 dispatcher，新增持久订单队列，移动履约 worker，并重连订单提交。稳定关系跟随 worker 的新位置，同时保持其 ID 与端点语义。
