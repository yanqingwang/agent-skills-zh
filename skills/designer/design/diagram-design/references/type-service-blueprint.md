> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-service-blueprint.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 服务蓝图（Service Blueprint）

**适用场景：** 展示一项服务在几个阶段里究竟如何运转：客户做什么、能看到什么、什么始终隐藏。**可见性线（line of visibility）**是承重元素：客户与前台动作位于其上，后台与支持位于其下，共用同一张阶段网格。当读者需要看清"失败其实是一个计费作业、一条队列或一次欺诈检查，尽管客户那一行看上去只是简单的重试"时使用。

**不适合本类型：**

- 跨阶段的情绪起伏、没有后台 → **用户旅程图**（`type-journey.md`）。旅程图的承重元素是情绪曲线。说不出前台/后台的切分，画的就不是蓝图。
- 在命名责任方之间交接的流 → **泳道图**（`type-swimlane.md`）。那里箭头才是论断。蓝图是一次普查：阶段顺序就是序列，等待时间是单元格文字。
- 带数据载荷的顺序节点 → **流程图**（`type-process.md`）。
- 单个人的阶段、等待、重试 → 状态机上的**生命周期阶段图**（`semantic-patterns.md` § 9）。
- 按列的状态普查、没有可见性线 → **看板**（`type-kanban.md`）。那里的列是*状态*，不是叙事阶段。
- 叙事主轴 × 发布切片 → **故事地图**（`type-story-map.md`）。那里的切线是范围，不是可见性。
- 没有阶段列的抽象条带 → **分层堆叠**（`type-layers.md`）。

## 版式约定

- **方向：** 阶段为等宽列（按叙事顺序从左到右），层为带标签的行（自上而下）。本版本没有连接箭头：那是泳道的地盘。
- **ViewBox：** 极简示例用 `0 0 1280 720`。完整编辑版保留同一 SVG，另加卡片。
- **左边距：** 层标签占 96px。Geist Mono 8px、大写、水平、在 x=88 处 `text-anchor="end"`。**绝不**用 `writing-mode: vertical`。
- **阶段网格：** 4–6 列。实操示例为 5 列 × 208px，沟槽 16px（`col_x = 96 + i·224`）。每个头部在列起点处的 rect 上带 `data-stage`；该列的每个单元格用同一个 `x`。
- **层顺序，自上而下：**
  1. 实体证据（可选）：48px
  2. 客户动作（必需）：64px
  3. 交互线（发丝线）
  4. 前台动作：台前的员工或可见产品（必需）：64px
  5. **可见性线**（承重；比其他线更重）
  6. 后台动作（必需）：64px
  7. 内部交互线（发丝线）
  8. 支持流程（可选）：48px
- **发丝线：** 含描边共 8px 带。交互线与内部交互线为 1px `rule`（`data-role="interaction"` / `data-role="internal-interaction"`）。可见性线为 2px `ink`、透明度 0.55（`data-role="visibility"`），必须对纸面过 3:1——0.45 在浅纸上过不了这条线，所以不要再细。
- **单元格：** 每层每阶段一个动作。Geist 12px、单行、列内居中。允许第二条 muted mono 行表示系统或等待（`dunning-job · 4h`）。必需单元格留空时，仅当 `data-name` 与打印文字都显式为 `—` 或 `Not applicable` 才可以。
- **填充：** 客户与前台为纸色/白色加 `ink` 描边。后台与支持取浅 `ink` 染色，让线下那条带读起来是隐藏的工作，而不是又一行台前动作。
- **焦点单元格（≤1，可选）：** 这张图为它而生的失败、等待或交接：通常在可见性线上或其下。accent 填充 `rgba(191,69,32,0.12)`（深色：`rgba(240,138,89,0.18)`）、accent 描边、`data-focal="true"`。
- **图例：** 发丝分隔线之后的水平条，三个键按此顺序：可见性线、后台层、焦点单元格。

### 机器可读数据契约

每个层分组：`data-layer="evidence|customer|frontstage|backstage|support"`。

每个单元格：`data-stage="<stage-id>"`（与某个头部的 `data-stage` 匹配），外加承载打印动作的 `data-name`。

可见性线：`data-role="visibility"`。两条发丝线：`data-role="interaction"` 与 `data-role="internal-interaction"`。

可选焦点单元格：至多一个单元格带 `data-focal="true"`。

禁止 `transform`、几何 `style` 或会移动标记的 `<style>` 规则。

`scripts/verify-service-blueprint.py` 读取以上声明，绘图与声明不一致时判构建失败。

### 服务蓝图元素模式

```svg
<!-- Stage header at column origin x=96; cells in this column reuse that x -->
<rect x="96" y="24" width="208" height="48" fill="none" data-stage="sign-up"/>
<text x="200" y="60" fill="#2d3142" font-size="12" font-weight="600"
      font-family="'Geist', sans-serif" text-anchor="middle">Sign up</text>

<g data-layer="customer">
  <rect x="544" y="128" width="208" height="64" rx="4" fill="#ffffff" stroke="#2d3142"
        stroke-width="1" data-stage="hit-limit" data-name="Retry payment"/>
  <text x="648" y="164" fill="#2d3142" font-size="12" font-family="'Geist', sans-serif"
        text-anchor="middle">Retry payment</text>
</g>

<!-- Visibility line: 2px ink @ 0.55, between frontstage bottom and backstage top -->
<line x1="96" y1="268" x2="1200" y2="268" stroke="rgba(45,49,66,0.55)" stroke-width="2"
      data-role="visibility"/>

<g data-layer="backstage">
  <rect x="544" y="272" width="208" height="64" rx="4" fill="rgba(191,69,32,0.12)"
        stroke="#bf4520" stroke-width="1" data-stage="hit-limit"
        data-name="dunning-job timeout" data-focal="true"/>
  <text x="648" y="300" fill="#bf4520" font-size="12" font-weight="600"
        font-family="'Geist', sans-serif" text-anchor="middle">dunning-job timeout</text>
  <text x="648" y="318" fill="#4f5d75" font-size="8" font-family="'Geist Mono', monospace"
        text-anchor="middle">dunning-job · 4h</text>
</g>
```

## 反模式

- **没有可见性线**，或线放在了错误的间隙（不在前台与后台之间）。没有这条线，这就只是一张行组成的表。
- **在蓝图上画情绪曲线。** 那是旅程图；把图拆开。
- **跨层的箭头。** 那是泳道。
- **每个失败单元格都上 accent。** 焦点单元格只有一个；网格的其余部分是普查。
- **必需层留空**却没有 `—` / `Not applicable` 标记。
- **超过 6 个阶段**；单元格文字超过两行。
- **`writing-mode` 竖排的层标签。** 只用水平，放左边距里。

## 诚实规则

- **网格是普查，不是流程图。** 阶段顺序就是序列。等待时间与系统名是单元格文字，不是边。
- **必需层必须完整。** 每个阶段都有客户单元格、前台单元格与后台单元格。空槽位仍占据其列，并如实说明。
- **可见性线是可检查的。** 它横贯绘图区、落在前台/后台间隙里，其描边对纸面过 3:1。
- **打印文字与 `data-name` 一致。** 画着 "Retry payment" 却声明另一个动作的单元格，是在讲两个故事。

这些规则可执行：`scripts/verify-service-blueprint.py` 读取声明，在层顺序、可见性、网格、普查、焦点、预算、打印标签、对比度或被 CSS 移动的标记任一项不合规时判负。`scripts/test-verify-service-blueprint.py` 证明两种极性：随附示例通过，上列每一类改动都以具名 finding 失败。

## 示例

- `assets/example-service-blueprint.html`：极简 light。*从试用到付费：客户永远看不到的事*，5 个阶段，焦点后台单元格 "Hit the limit" 之下的 `dunning-job timeout`。
- `assets/example-service-blueprint-dark.html`：极简 dark，同一数据。
- `assets/example-service-blueprint-full.html`：完整编辑版：容器框架 + 3 张不同宽度的摘要卡片 + 页脚。
