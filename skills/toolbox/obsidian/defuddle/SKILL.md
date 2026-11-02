---
name: defuddle
description: 使用 Defuddle CLI 从 HTML 页面提取干净的 Markdown。
---

> **中文汉化版** · 上游：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) · 原文件：`skills/defuddle/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Defuddle

使用 Defuddle CLI 从网页中提取干净、可读的内容。对于标准网页，优先于 WebFetch 使用：它会移除导航、广告和杂乱内容，降低 token 消耗。

若未安装：`npm install -g defuddle`

## 用法

输出 Markdown 时始终使用 `--md`：

```bash
defuddle parse <url> --md
```

保存到文件：

```bash
defuddle parse <url> --md -o content.md
```

提取特定元数据：

```bash
defuddle parse <url> -p title
defuddle parse <url> -p description
defuddle parse <url> -p domain
```

## 输出格式

| 标志 | 格式 |
|------|--------|
| `--md` | Markdown（默认选择） |
| `--json` | JSON，同时包含 HTML 和 markdown |
| （无） | HTML |
| `-p <name>` | 指定的元数据 property |
