> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-nested.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 嵌套包含

**适用场景：** 用包含关系表达层级：作用域边界、信任域、文件夹嵌套、影响范围（blast radius）。外层 = 更宽泛，内层 = 更具体。

## 布局约定
- 3–5 个圆角矩形（`rx=8`），逐层嵌套，内边距保持一致（建议水平 24–32px，垂直 32–36px）。
- 每层在左上角用 `eyebrow` 角色标注（7–8px，letter-spacing 0.14em）。标签压在一个纸色遮罩矩形上，盖住外框的顶边。
- 描边层级：外圈最淡（`rgba(..,0.30–0.45)`），向内依次过渡到 muted、ink，最内层焦点用 coral。
- 填充不透明度由外向内递增：`rgba(..,0.015)` → `rgba(..,0.025)` → 最内层加 accent 色调。
- 每层内可放一个可选的文件图标字形（折角矩形），暗示该层范围的内容。
- 斜体 `callout` 角色的旁注（见 `references/primitive-annotation.md`），最多 1–2 条。

## 反模式
- 超过 6 层（信息向内消失）。
- 层与层之间间距不规律，嵌套不对齐会显得像失误。
- 圈里放了不属于该层级的内容，应改用并列的另一张图。
- 多层同时用 coral，层级感会崩塌。

## 示例
- `assets/example-nested.html` — 极简浅色
- `assets/example-nested-dark.html` — 极简深色
- `assets/example-nested-full.html` — 完整编辑排版
