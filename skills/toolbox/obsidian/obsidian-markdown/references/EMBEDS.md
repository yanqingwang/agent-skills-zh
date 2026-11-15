> **中文汉化版** · 上游：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) · 原文件：`skills/obsidian-markdown/references/EMBEDS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 嵌入参考

## 嵌入笔记

```markdown
![[Note Name]]
![[Note Name#Heading]]
![[Note Name#^block-id]]
```

## 嵌入图片

```markdown
![[image.png]]
![[image.png|640x480]]    Width x Height
![[image.png|300]]        Width only (maintains aspect ratio)
```

## 外部图片

```markdown
![Alt text](https://example.com/image.png)
![Alt text|300](https://example.com/image.png)
```

## 嵌入音频

```markdown
![[audio.mp3]]
![[audio.ogg]]
```

## 嵌入 PDF

```markdown
![[document.pdf]]
![[document.pdf#page=3]]
![[document.pdf#height=400]]
```

## 嵌入 Bases

```markdown
![[BaseFile.base]]
![[BaseFile.base#View Name]]
```

## 嵌入列表

```markdown
![[Note#^list-id]]
```

当列表带有块 ID 时：

```markdown
- Item 1
- Item 2
- Item 3

^list-id
```

## 嵌入搜索结果

````markdown
```query
tag:#project status:done
```
````
