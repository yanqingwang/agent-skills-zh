> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/primitive-sketchy.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 手绘滤镜（sketchy 变体）

可选的位移滤镜，让每条描边和边缘轻微抖动：不改变布局，就把任何极简变体变成手绘"编辑"格调。当图表伴随的是一篇文章而非技术文档时使用。

## 语法

```svg
<defs>
  <filter id="sketchy" x="-2%" y="-2%" width="104%" height="104%">
    <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="4"/>
    <feDisplacementMap in="SourceGraphic" scale="1.5"/>
  </filter>
</defs>

<!-- Apply to a group wrapping shapes — NOT text -->
<g filter="url(#sketchy)">
  <!-- rects, paths, circles, lines go here -->
</g>

<!-- Text sits OUTSIDE the filtered group — legibility stays crisp -->
<text ...>Labels go here</text>
```

## 调参

| 参数 | 范围 | 效果 |
|---|---|---|
| `baseFrequency` | 0.01–0.04 | 低 = 慵懒的波浪线；高 = 抖动。默认 0.02。 |
| `numOctaves` | 1–3 | 越大噪点细节越多。2 足够。 |
| `scale` | 1–6 | 1 几乎不可见，1.5 默认，2 可见，4+ 卡通。 |
| `seed` | 整数 | 换一个随机图案。 |

## 关键规则

滤镜作用于形状，不作用于文字。位移映射过的文字会变得不可读。组织你的 SVG，让文字位于滤镜组之外的兄弟组里。

## 何时使用

- 图表是叙事页主角的文章 / 博文 / newsletter。
- "工作草图"格调：表明某事物尚在构思中，不是最终架构。

## 何时不用

- 技术文档（精确性重要）。
- 标签密集或对齐紧凑的图（滤镜看起来像噪点）。
- 深色变体：抖动在深色背景上读起来像渲染瑕疵。先测试。
