> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-venn.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 维恩图 / 集合重叠

**适用场景：** 概念/领域的交集、类别之间的共享属性、"A 与 B 在哪里相遇"、ikigai 式框架（desirable × feasible × viable）。

## 布局约定
- **优先 2 或 3 个圆。** 避免 4 个以上（不可读：改用矩阵）。
- 圆描边：1px 发丝线，颜色随集合（ink、muted、soft）。
- 圆填充：极低透明度色调：ink 集用 `ink @ 0.04`，muted 集用 `muted @ 0.05`。色调在重叠区自然叠加。
- 半径：集合规模相近时相等；集合有明显差异时成比例。不要为了好看假装等大。
- **集合标签** 放在圆外，绝不跨过描边。集合名用 `node-name` 角色 12–14px 600，可选 `sublabel` 角色 9px。
- **交集标签** 放在重叠区内，`node-name` 角色 12px 600，居中。重叠太小时，用引线连到净空里的标签。
- **coral 强调**只用于唯一一个焦点交集："甜蜜点"。要么 `accent` 标签描边，要么 clipPath 界定的 `accent @ 0.10` 填充色调。
- 圆心和半径都可被 4 整除。

## 反模式
- 区域无标签：读者分不清哪个集合是哪个。
- 重叠才是重点时，圆却不重叠。
- 集合明显不同却画成等大的圆（不诚实）。
- coral 用在多个重叠区（焦点信号消失）。
- 标签压在圆的描边上（不可读）。
- 2–3 个圆够用却用 4 个以上。

## 示例
- `assets/example-venn.html` — 极简浅色
- `assets/example-venn-dark.html` — 极简深色
- `assets/example-venn-full.html` — 完整编辑排版
