> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-sequence.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 时序图（Sequence）

**适用场景：** 请求/应答流、协议交互、多参与者随时间的互动、API 调用链、事故还原、带分支的鉴权/token 刷新路径。

## 版式约定
- 参与者（Actor）画成顶部一行水平排列的方框。
- **生命线（Lifeline）**：从每个参与者向下延伸到底部的虚线。
- 消息：生命线之间的水平箭头；时间自上而下流动。
- **激活条（Activation bar）**：生命线上的窄矩形（`w=8`、muted 填充、0.8 发丝描边），覆盖该参与者持有控制权的区间。嵌套调用时堆叠。
- 自消息：回到同一条生命线的短 U 形环；标签放在环右侧。
- 返回消息：**虚线**描边 + **实心** marker（绝不用空心）。优先 muted；多跳调用栈配对时可选与发起调用同色。头条成功可用实线 coral（见消息种类）。
- coral 只用在主成功响应或头条消息上：一处，至多两处。参与者的 focal 描边不占 coral 消息预算。
- 流程**出现分支**时（token 有效 vs 无效、重试、可选步骤），画**组合片段（combined fragment）**框，不要发明游离的 if/else 箭头簇。

## 消息种类

| 种类 | 描边 | Marker | 何时 |
|---|---|---|---|
| 调用（同步） | 实线 muted 或 link-blue | 实心 | 期待应答的请求 |
| 返回 | **虚线** muted（或与调用同色） | 实心 | 同步调用的应答：绝不用实线 |
| 异步 / 发后即忘 | 虚线 muted | **空心**箭头头部 | 埋点、事件、单向通知 |
| 头条成功 | 实线 accent（≤1–2 条消息） | accent 实心 | 仅限主 happy-path 响应 |

### 空心箭头头部（异步）

在 `<defs>` 中定义一次，仅用于发后即忘：

```svg
<marker id="arrow-open" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
  <polyline points="0 0, 8 3, 0 6" fill="none" stroke="{muted}" stroke-width="1.2"/>
</marker>
```

深色模式：`muted` 随皮肤反转，描边无需改动。不要填充空心 marker：中空的头部就是异步信号。返回消息即使虚线也保持**实心** marker。

## 组合片段（`alt` / `opt` / `loop`）

用一个矩形**框**，只横跨参与该分支的生命线。操作符标签用 `eyebrow` 角色、大写，放在框左上角的小签条里。框内时间仍自上而下流动。

### 框基元（共用）

```svg
<!-- Frame: light ink wash + hairline. Label tab top-left. -->
<rect x="X" y="Y" width="W" height="H" rx="4"
      fill="{ink @ 0.02}" stroke="{ink @ 0.22}" stroke-width="1"/>
<!-- Operator tab -->
<rect x="X" y="Y" width="40" height="16" rx="2"
      fill="{paper}" stroke="{ink @ 0.22}" stroke-width="1"/>
<text x="X+20" y="Y+12" fill="{muted}" font-size="8"
      font-family="{eyebrow}" text-anchor="middle"
      letter-spacing="0.12em">ALT</text>
```

深色模式：角色随皮肤反转，因此只有框填充变化，从 `ink @ 0.02` 改为 `ink @ 0.04`。描边保持 `ink @ 0.22`，签条填充保持 `paper`，签条文字保持 `muted`。

### 操作符

| 操作符 | 区域 | 分隔线 | 守卫标签 |
|---|---|---|---|
| `opt` | 1 | 无 | 签条下方 `[if condition]`（`arrow-label` 角色，8px） |
| `alt` | **最多 2** | 横贯框的虚线水平发丝线 | 区域 1 放 `[guard]`；区域 2 放 `[else]`（或第二个守卫） |
| `loop` | 1 | 无 | 签条下方 `[for each item]` 或 `[retry ≤ 3]` |

### 守卫 + 分隔线基元

```svg
<!-- Guard: left-aligned inside the frame, mono -->
<text x="X+12" y="GUARD_Y" fill="{muted}" font-size="8"
      font-family="{arrow-label}" letter-spacing="0.04em">[token valid]</text>

<!-- alt region divider -->
<line x1="X+8" y1="DIV_Y" x2="X+W-8" y2="DIV_Y"
      stroke="{ink @ 0.20}" stroke-width="1" stroke-dasharray="4,3"/>
```

### 片段版式规则
- 框的左右两侧距最外侧参与生命线中心 ≥12px（让激活条留在框内）。
- 区域内相邻消息 y 层级之间 ≥24px（4px 网格）。
- 守卫位于签条下方约 20px 内；该区域首条消息在守卫基线下 ≥24px。
- 分隔线 y 落在 4px 网格上；与上下消息保持 ≥16px 净空。
- 嵌套片段：**最多 1 层**。深嵌套宁可拆成两张图。
- 默认：每张图**一个**片段。仅当两者都低于复杂度预算时才允许第二个。
- coral 全图只保留在**一条**头条成功消息上（通常是第一个 `alt` 区域内的 happy-path 返回，或 loop 之外的最终成功）。不要两个 `alt` 分支都上 coral。

### 范围之外（不要发明）
- `par`、`critical`、`break`、`ref` 等其他 UML 操作符：确有需要再开第二个 PR。
- 参与者的创建/销毁、found/lost 消息、持续时间条。

## 复杂度预算（时序图专属）
- 生命线上限：5（与 [layout-budget.md](layout-budget.md#complexity-budget-per-diagram) 的 §7 预算表一致）。
- 消息（箭头）上限：12。
- 组合片段上限：1（硬默认）；仅当各自都是单区域 `opt`/`loop` 时才允许 2。
- `alt` 区域上限：2。
- 片段嵌套深度上限：1。
- coral 元素上限：2（片段图优先 1）。

超了就拆：总览（happy path）+ 细节（失败 / 刷新路径）。

## 生命线基元
```svg
<line x1="CX" y1="TOP" x2="CX" y2="BOTTOM"
      stroke="{ink @ 0.20}" stroke-width="1" stroke-dasharray="3,3"/>
```

## 激活条基元
```svg
<rect x="CX-4" y="TOP" width="8" height="H"
      fill="{ink @ 0.06}" stroke="{muted}" stroke-width="0.8"/>
```

## 反模式
- 消息箭头指向*上方*（时间倒流：绝不）。
- 永远不闭合的激活条。
- 标签压在另一条生命线上：缩短或把 y 挪进空隙。
- 泳道式的车道而不是生命线（不同语法）。
- 把 `if/else` 画成两个**没有**片段框的游离箭头簇。
- `alt` 里再嵌 `alt`（拆成两张图）。
- 片段操作符标签用 `node-name` sans 字族：必须是 mono（`eyebrow`）：`ALT` / `OPT` / `LOOP`。
- 两个 `alt` 分支都上 coral。
- 框罩住参与者、框内却没有消息。
- 异步发后即忘用实心箭头头部（应使用空心 marker）。
- 返回消息用空心箭头头部（返回保持实心 + 虚线）。

## 示例
- `assets/example-sequence.html`：极简 light（冷缓存 happy path）
- `assets/example-sequence-dark.html`：极简 dark
- `assets/example-sequence-full.html`：完整编辑版
- `assets/example-sequence-oauth.html`：特例：bearer 调用 + `alt` 刷新（light）
- `assets/example-sequence-oauth-dark.html`：同一特例，dark
- `assets/example-sequence-oauth-full.html`：同一特例，完整编辑版
