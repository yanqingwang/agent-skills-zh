> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-layers.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 分层图（Layer Stack）

**适用场景：** OSI 模型、CSS 层叠、上下文层级、技术栈、抽象层、内存层级。

## 布局约定
- 水平条带纵向堆叠。每层是一个全宽矩形（同一 x，同一宽度）。总共 4–6 层。
- 层高 56–72px，宽度在 1000px viewBox 内通常 800–880px。
- 每行（自左向右）包含：
  1. **索引标签** 在最左侧（`L3`、`07`、`APPLICATION`）：`eyebrow` 角色，8–9px。
  2. **层名** 在中偏左一点：`node-name` 角色，14–16px 600。
  3. **副标签 / 注记** 在最右侧：`sublabel` 角色，9–10px，`muted`。
- 层间边框：1px 发丝线 `ink @ 0.12`（`rule` 角色）。外轮廓 1px `ink` 或 `muted`。
- 填充：要么交替的细微深浅（paper / paper-2），要么全部 paper 加发丝线分隔。选定一种并保持一致。
- 方向指示器放在左边距（堆叠之外）：小的上/下箭头 + `eyebrow` 角色标签（`abstraction ↑`、`packets ↓`）。
- coral 只用于**一个**焦点层（描边 + 淡色调填充）：瓶颈层、撑起营收的那层，或正在讨论的那层。

## 反模式
- 各层并非真正的层级关系（改用泳道图或架构图）。
- 跳号（L3 与 L5 之间缺 L4 又无解释）。
- 每层一种颜色：层级关系不可见。
- 无理由地让各层高度不一致。

## 示例
- `assets/example-layers.html` — 极简浅色
- `assets/example-layers-dark.html` — 极简深色
- `assets/example-layers-full.html` — 完整编辑排版
