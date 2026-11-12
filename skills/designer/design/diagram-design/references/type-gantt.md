> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-gantt.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 甘特图

**适用场景：** 项目计划与路线图：带明确开始和结束日期的任务，归入各阶段。当读者需要一眼看到时间重叠、并行轨道和里程碑顺序时使用。

## 布局约定

- **左侧标签列：** x=20–200（180px）。任务名用 `node-name` 角色 11px 600。阶段标签用 `eyebrow` 7px，放在每组上方。
- **时间轴区：** x=200–960（760px）。时间轴自左向右。
- **行高：** 每个任务 40px。每根条占 h=24px，在行内居中（顶部留 8px）。
- **时间轴：** `arrow-label` 角色 8px 的周/月标签放在 x=200+i×pitch、y=56（第一行任务正上方）。y=64 一条发丝线分隔。
- **阶段分组：** 每个阶段的各行背后垫一个浅淡的区域矩形（与架构图区域同一模式），眉标放在左上边距。填充用 `ink @ 0.02`，描边用 `ink @ 0.10`。
- **焦点任务条：** 1 根条用 accent 填充/描边（关键交付物或关键路径任务）。其余全部：muted 填充 @ 0.15，muted 描边。
- **今天 / 里程碑标记：** 可选的竖直虚线，`muted`，放在当前周的 x 位置。

### 任务条模式

```svg
<!-- Non-focal task -->
<rect x="X_start" y="ROW_Y+8" width="DURATION_PX" height="24" rx="4"
      fill="{muted @ 0.15}" stroke="{muted}" stroke-width="1"/>
<text x="X_start+8" y="ROW_Y+25" fill="{ink}" font-size="10" font-weight="600"
      font-family="{node-name}">Task name</text>

<!-- Focal task -->
<rect x="X_start" y="ROW_Y+8" width="DURATION_PX" height="24" rx="4"
      fill="{accent @ 0.12}" stroke="{accent}" stroke-width="1"/>
<text x="X_start+8" y="ROW_Y+25" fill="{accent}" font-size="10" font-weight="600"
      font-family="{node-name}">Key task</text>
```

像素时长：`(end_week - start_week) × pitch`。Pitch = timeline_width / total_weeks。

## 反模式

- 超过 12 个任务（拆成子计划，或收拢为阶段级视图）。
- 每个阶段超过 5 条并行轨道（重叠不可读）。
- v1 里任务之间画依赖箭头（只在确有必要时加；标签改用标注原语）。
- 把开始/结束日期写进条标签（放到 x 轴或 tooltip 注释里）。
- 所有条视觉重量相同（焦点任务必须跳出来）。

## 示例

- `assets/example-gantt.html` — 极简浅色
- `assets/example-gantt-dark.html` — 极简深色
- `assets/example-gantt-full.html` — 完整编辑排版
