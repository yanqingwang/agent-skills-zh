> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/primitive-annotation.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 标注气泡（斜体衬线旁注）

用于编辑性旁注：那个在不与主图语法竞争的前提下标记细节的"斜体指针"。想象页边批注：*"structure IS the index"*、*"no imports, no configuration"*。

## 语法

```svg
<!-- 1. Italic serif text: the `callout` role from style-guide.md -->
<text x="904" y="36" fill="{ink}" font-size="14" font-style="italic"
      font-family="{callout}" text-anchor="end">no imports, no configuration</text>
<!-- 2. Dashed Bézier leader -->
<path d="M 820 44 Q 700 84 520 216" fill="none"
      stroke="{ink @ 0.40}" stroke-width="1" stroke-dasharray="4,3"/>
<!-- 3. Landing dot -->
<circle cx="520" cy="216" r="2" fill="{ink}"/>
```

## 规则
- 斜体 + 衬线同时出现，才在图表的无衬线/等宽正文之间发出"编辑声音"。不要换成斜体无衬线或斜体等宽：这个组合是承重的。
- 虚线路径（`stroke-dasharray="4,3"`）把旁注引线与主箭头（实线）区分开。
- 旁注放在边距里（右上、左下）。绝不放进图的活跃区域。
- 每张图最多 2 个旁注。再多就成了评论，不是信号。

## 颜色

| 意图 | 文字 | 引线 |
|---|---|---|
| 中性旁注 | `ink` | `ink @ 0.40` |
| 焦点 / accent | `accent` | `accent @ 0.50` |
| 三级（muted） | `muted` | `ink @ 0.30` |

## 反模式
- 实线箭头引线（读起来像流程箭头）。
- 斜体无衬线或斜体等宽：衬线是承重的。
- 旁注穿过主箭头 / lifeline：挪到干净的边距。
- 用旁注去标注图本应直接标注的东西：把标签放到那个元素上。
