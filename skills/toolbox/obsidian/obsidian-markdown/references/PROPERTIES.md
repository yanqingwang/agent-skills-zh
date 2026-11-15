> **中文汉化版** · 上游：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) · 原文件：`skills/obsidian-markdown/references/PROPERTIES.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 属性（Frontmatter）参考

属性使用笔记开头的 YAML frontmatter：

```yaml
---
title: My Note Title
date: 2024-01-15
tags:
  - project
  - important
aliases:
  - My Note
  - Alternative Name
cssclasses:
  - custom-class
status: in-progress
rating: 4.5
completed: false
due: 2024-02-01T14:30:00
---
```

## 属性类型

| 类型 | 示例 |
|------|---------|
| 文本 | `title: My Title` |
| 数字 | `rating: 4.5` |
| 复选框 | `completed: true` |
| 日期 | `date: 2024-01-15` |
| 日期和时间 | `due: 2024-01-15T14:30:00` |
| 列表 | `tags: [one, two]` 或 YAML 列表 |
| 链接 | `related: "[[Other Note]]"` |

## 默认属性

- `tags` - 笔记标签（可搜索，显示在关系图谱中）
- `aliases` - 笔记的替代名称（用于链接建议）
- `cssclasses` - 应用于笔记阅读/编辑视图的 CSS 类

## 标签

```markdown
#tag
#nested/tag
#tag-with-dashes
#tag_with_underscores
```

标签可以包含：字母（任何语言）、数字（不能作为首字符）、下划线 `_`、连字符 `-`、正斜杠 `/`（用于嵌套）。

在 frontmatter 中：

```yaml
---
tags:
  - tag1
  - nested/tag2
---
```
