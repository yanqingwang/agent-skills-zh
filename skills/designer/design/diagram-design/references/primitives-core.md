> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/diagram-design/references/primitives-core.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 核心 SVG 基元

由 SKILL.md §6 路由而来。SKILL.md 把六条连线规则各留一行，加上箭头角色与一行式节点框摘要。本文件保存标记代码与每条规则的完整形式。复制来的模板已带背景 rect、带注释的点阵纸 pattern 和全部三个箭头 marker，需要确切标记或某条规则的边界情况时加载本文件。

类型专用基元（生命线、激活条、区域）在 SKILL.md §3 链接的相应类型参考里。

本文与各类型参考里的片段以角色命名颜色与字体，绝不按具体值：颜色用 `{ink}`、`{muted}`、`{paper}`、`{accent}`、`{link}`、`{soft}`，带透明度的角色用 `{ink @ 0.10}`，字体族用 `{title}`、`{node-name}`、`{sublabel}`、`{eyebrow}`、`{arrow-label}`、`{callout}`。输出之前，先对照 [`style-guide.md`](style-guide.md) 的当前皮肤解析每个占位符：`{ink @ 0.10}` 变成 `ink` 色的 `rgba(r,g,b,0.10)`，`{sublabel}` 变成该角色的完整字体族栈。大写名（`X`、`FILL`、`STROKE`）是你计算的几何与逐节点值。

## 背景

**默认：干净纸面，无点阵图案。** 单个 `<rect>`，填充 `paper`。不要把图包进二级容器背景里，图直接坐在页面上。

```svg
<rect width="100%" height="100%" fill="{paper}"/>
```

**可选：点阵纸变体。** 长篇编辑类图能从带纹理的底面获益时（随笔、专页上的主视觉图），加入 `dots` pattern 和第二个 rect 来启用：

```svg
<defs>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="1" cy="1" r="0.9" fill="{ink @ 0.10}"/>
  </pattern>
</defs>
<rect width="100%" height="100%" fill="{paper}"/>
<rect width="100%" height="100%" fill="url(#dots)" opacity="0.6"/>
```

图位于产品页、幻灯片或卡片内时不要用点阵图案，纹理会与周边 chrome 叠加，读起来像噪点。

## 箭头 marker（永远三个全定义）

```svg
<marker id="arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
  <polygon points="0 0, 8 3, 0 6" fill="{muted}"/>
</marker>
<marker id="arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
  <polygon points="0 0, 8 3, 0 6" fill="{accent}"/>
</marker>
<marker id="arrow-link" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
  <polygon points="0 0, 8 3, 0 6" fill="{link}"/>
</marker>
```

| 箭头 | 描边 | 何时 |
|---|---|---|
| 默认 | `muted` | 内部、一般 |
| 强调 | `accent` | 主线 / 高亮 / 标题 |
| 链接蓝 | `link` | HTTP/API 调用、外部系统 |
| 虚线 | `stroke-dasharray="5,4"` + 任意颜色 | 可选、被动、返回、异步 |

**先画箭头后画框**，让 z 序把线压在节点之下。

几何来源关卡排除只定义容器（`defs`、`symbol`、`marker`、`pattern`、`clipPath`、`mask`）内的形状，因为这些形状不在其局部坐标上绘制。关卡不解析 `<use>` 实例；被引用的图用渲染 lint 和目检来核查。惰性 HTML 注释、带引号的标签属性内的 `>`，都不会改变定义归属。关卡能读单引号和双引号的 SVG 属性。

## 强制连线规则

这六条规则**不可协商**。产出任何图之前，先跑输出前清单（SKILL.md §9）核实。

1. **必须使用圆角直角（正交）连线。** 不共享 x 轴或 y 轴的节点之间，绝不用斜 `<line>` 或直的斜线路径。每个拐弯必须是 `r=8` 的四分之一圆弧（紧凑布局最小 `r=6`）。拐弯路径公式见 `references/type-architecture.md`。纯直线 `<line>` 只留给端点共享同一 x 或 y 坐标的连接。斜连线自动判失败。连线从每框离开和进入时也要垂直于所接触的边，端口在该边的直段上、距拐角至少 8px。起于顶边或底边的水平段、起于侧边的垂直段，会沿边框走在节点填充之下，看起来像从拐角出来的箭头。在已安装的 skill 目录下，`python3 scripts/verify_geometry.py <file>` 会报告斜连线、贴边段与拐角端口。

2. **标签与连线的间距：始终留 6–10px 空隙。** 标签绝不能*坐*在自己的箭头上，连线必须保持可见。标签居中放在线上方（垂直段放在侧面），标签掩码 rect 底边与连线描边之间至少 6px 空隙。不透明掩码 rect 防止箭头从标签底下透出，但掩码边缘与线之间*可见的*空隙保住了读者追踪连线的能力。标签大到 6px 显得局促时，放宽到 8–10px。掩码 rect 绝不接触或压到描边。

3. **连线不得重叠。** 两条连线绝不能共用同一条描边路径、平行叠着跑，或在任何一段上互相叠画。两条正交箭头必须在单点交叉时，套用 **bridge / hop** 基元（见 `references/type-architecture.md` § Crossing arrows）。两条箭头天然想重叠时，把路由错开 ≥12px，让每条线都能被独立追踪。发现自己在堆叠连线时，重新设计布局，这意味两个节点太近，或图的预算超了（拆成概览 + 细节）。

4. **共享边 → 扇开挂点。** 两条或更多连线进出于同一框的*同一条边*时，每条都要有自己的独立挂点，**任何两条连线不得共用框上的同一个点**。挂点沿边均匀分布，相邻点之间 **≥12px**（很小的框最小 8px）。路由规则：
   - 边长为 L 的边上有 N 条连线时，挂点 `k`（1..N）位于距该边前导拐角 `L * k / (N + 1)` 处。
   - 连线扇出到不同侧的目的地时，从各自挂点正交路由，不在框附近合并描边。
   - 两条平行连线同向而行时，全程保持 ≥12px 间距，不只挂点处。每条箭头必须端到端可独立追踪。

   任何连线不得遮挡另一条。一眼分不清两条箭头，布局就是失败的。

5. **连线不得从非其源或目的地的框背后穿过，除非该框在直接正交路径上几何上不可避免。** 默认绕开 intervening 框重路由。唯一正当例外：横切的节点（如页脚服务、水平分层条）物理上位于连线源与目的地之间、两者之间唯一一条直路上。该例外下：
   - 描边必须是**虚线**（如 `stroke-dasharray="4,3"`），示意"过境，不交互"，告诉读者 intervening 框不是端点。
   - 标签放在连线的**可见端**（通常靠近源），避免落入 intervening 框背后。
   - 任何 marker（箭头头部）不得落在 intervening 框的边上，marker 只在真正目的地解析。

   拿不准就重路由。这个例外只服务于几何上无法重路由的窄场景，不是省布局工作的捷径。

6. **标签掩码不得压到后画的节点。** 在共享画布（而不是各面板局部坐标）里、计入受支持的组与元素 `translate()` 偏移后，比较两者的边界。规则 2 保证标签离开自己的连线，这条保证它离开框。节点在标签之后绘制，落进节点内的掩码会被节点填充盖住，文字就成了骑在节点边框上的碎片。把标签放在穿过开放画布的那段连线上：离开节点右边的连线，掩码要在越过节点 `x + width` 之后才开始。完全在节点*内部*的掩码是徽章 chip，没问题；压到 zone 容器也没问题，因为 zone 先画。在已安装的 skill 目录下，用 `python3 scripts/verify_geometry.py <file>` 核实。

## 节点框，完整模式

```svg
<!-- 1. Opaque paper mask — prevents arrows bleeding through transparent fills -->
<rect x="X" y="Y" width="W" height="H" rx="6" fill="{paper}"/>
<!-- 2. Styled box -->
<rect x="X" y="Y" width="W" height="H" rx="6" fill="FILL" stroke="STROKE" stroke-width="1"/>
<!-- 3. Rectangular type tag (rx=2, NOT a pill) -->
<rect x="X+8" y="Y+6" width="28" height="12" rx="2" fill="transparent" stroke="STROKE@0.40" stroke-width="0.8"/>
<text x="X+22" y="Y+15" fill="STROKE@0.8" font-size="7" font-family="{eyebrow}"
      text-anchor="middle" letter-spacing="0.08em">API</text>
<!-- 4. Node name (node-name role, sans: human-readable) -->
<text x="CX" y="CY+2" fill="{ink}" font-size="12" font-weight="600"
      font-family="{node-name}" text-anchor="middle">Node Name</text>
<!-- 5. Technical sublabel (sublabel role, mono) -->
<text x="CX" y="CY+18" fill="{muted}" font-size="9"
      font-family="{sublabel}" text-anchor="middle">tech:port</text>
```

## 箭头标签：必须加掩码，必须留间距

每个箭头标签背后都要有不透明 rect，否则会从线里透出来。**而且标签要以可见空隙悬在连线上方，绝不压在线上。**

```svg
<!-- Mask sits 14px above the arrow (8px text height + 6px gap). Stroke is at ARROW_Y. -->
<rect x="MID_X-18" y="ARROW_Y-20" width="36" height="12" rx="2" fill="{paper}"/>
<text x="MID_X" y="ARROW_Y-11" fill="{soft}" font-size="8"
      font-family="{arrow-label}" text-anchor="middle" letter-spacing="0.06em">WRITE</text>
```

规则：

- ≤14 个字符，全大写，居中于段中点。
- 掩码 rect 底边与箭头描边之间**强制 6–10px 空隙**。连线必须保持可见，藏掉自己箭头的标签是硬失败。
- 绝不使用 `writing-mode` 竖排。
- 垂直段把标签放在侧面（不在线上），保持同样的 6–10px 水平空隙。

**字体替换。** 不要估算逐字符宽度，用 `style-guide.md` 的预算（每字符 0.60em sans / 0.62em mono）。某次生产运行按约 0.47em/字符给 mono 标签定宽，被裁剪了两次；校准后的预算同时适配默认皮肤的 mono 字面（Geist Mono）和常见替换 mono 字面（Menlo、Courier New、Monaco，都约 0.60em）。经 `rsvg`/`inkscape` 的预览拉不到注入的 Google Fonts，所以用 skill 目录下的 `python3 scripts/verify_geometry.py <file>` 核实，它检查掩码对后画节点的关系，不检查文字适配。`scripts/self_check.py` 检查文字与它所在的可见框，不检查箭头标签掩码，所以在掩码上守住预算是你的责任。

## 图例：底部的水平条带

**绝不要把图例放进图区。** 作为水平条带放在所有节点之后，带一条发丝分隔线：

```svg
<line x1="30" y1="LEGEND_Y-8" x2="VIEWBOX_W-30" y2="LEGEND_Y-8"
      stroke="{ink @ 0.10}" stroke-width="0.8"/>
<text x="30" y="LEGEND_Y+8" fill="{muted}" font-size="8" font-family="{eyebrow}"
      letter-spacing="0.14em">LEGEND</text>
<!-- Items — horizontal row, ~160px apart -->
```

把 SVG `viewBox` 高度扩大约 60px。

## 可访问 SVG 契约

SKILL.md §12 把这六点各列一行；这里是完整形式。

每张图默认都是可访问图形：

1. `<svg>` 带 `role="img"` 和 `aria-labelledby`，指向图的 `<title>` 与 `<desc>`。
2. `<title>` 是 `<svg>` 的第一个子元素，位于 `<defs>` 之前。辅助技术可能忽略放在后面的 title。
3. ID 按图与变体加前缀：`<slug>-title` / `<slug>-desc`，slug 与文件对应（`loop`、`loop-dark`、`loop-full`）。禁止裸 `title` / `desc` ID，否则两张内嵌图会共享一个 ID，第二张可能被播报成第一张的名字。每个命名 ID 还必须在整个文档内唯一，包括非 SVG 元素；随包的 `scripts/self_check.py` 拒绝这类冲突。
4. `<title>` 是主体的短名，大致是页面 `<h1>`，约 60 字符以内。
5. `<desc>` 是一句话，用读者在没有图时需要的语言说明图展示什么。描述内容，不描述几何："Org chart showing a command center routing work to specialist agents and escalation owners"，而不是"A box at the top with five boxes below it"。逐形状的旁白还不如没有有用的描述。
6. 纯装饰性 SVG，比如 `assets/icons.html` 里的字形样本，改用 `aria-hidden="true"`。
